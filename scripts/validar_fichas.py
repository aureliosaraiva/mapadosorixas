#!/usr/bin/env python3
"""Valida as fichas (data/orixas/*.json), data/conexoes.json, data/entidades_equivalentes.json, data/tradicoes.json e data/glossario.json.

Checagens:
- esquema (schemas/orixa.schema.json, conexao.schema.json, tradicao.schema.json), se jsonschema estiver instalado;
- toda versão tem ao menos uma fonte, e toda fonte (id e via) existe no catálogo;
- source_id/via_source_id/localizacao da versão batem com sources[0];
- entidades_equivalentes.json (esquema entidade.schema.json) aponta para arestas existentes;
- nenhuma versão vem de registro 'pre_fichamento' (confere contra o fichamento);
- cada versão bate com o registro de origem (valor, fonte, página);
- toda tradição citada existe em data/tradicoes.json;
- tradições 'com_fonte' e termos do glossário: esquema, fontes existentes e lidas (status >= conferido_web),
  ids únicos e ver_tambem apontando para termos existentes;
- revisão: status da versão é o efetivo (scripts/revisao.py) e `revisoes` bate com
  as revisões vigentes do registro; toda revisão da ficha (`revisao`) aponta para
  revisor cadastrado; nenhum registro publicável some — cada registro
  fichado/revisado está na ficha como versão ou em pendencias.retidos_ate_conselho;
- fichas e grafo estão em dia com o fichamento (regenerar com scripts/gerar_fichas.py).

Uso: python3 scripts/validar_fichas.py
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import revisao  # noqa: E402


def ler(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


CATALOGO = {f["id"]: f for f in ler(RAIZ / "data/fontes/catalogo.json")["fontes"]}
FONTES = set(CATALOGO)
LIDAS = {"conferido_web", "verificado", "fichado", "revisado"}
TRADICOES = ler(RAIZ / "data/tradicoes.json")["tradicoes"]
TRAD_IDS = {t["id"] for t in TRADICOES}
REGS = {}
for p in (RAIZ / "data/fichamento").glob("*.json"):
    if p.name != "divergencias.json":
        REGS.update({r["id"]: r for r in ler(p)["registros"]})
REVISORES = revisao.por_id(revisao.carregar_revisores(RAIZ))


def validador(nome):
    try:
        import jsonschema
        from referencing import Registry, Resource
    except ImportError:
        return None
    reg = Registry()
    for p in (RAIZ / "schemas").glob("*.schema.json"):
        s = ler(p)
        res = Resource.from_contents(s)
        reg = reg.with_resources([(s["$id"], res), (p.name, res)])
    s = ler(RAIZ / "schemas" / nome)
    return jsonschema.Draft202012Validator(s, registry=reg)


def checar_versao(v, onde, erros):
    if not v.get("sources"):
        erros.append(f"{onde}: versão sem fonte")
        return
    for s in v["sources"]:
        for sid in (s.get("id"), s.get("via")):
            if sid and sid not in FONTES:
                erros.append(f"{onde}: fonte inexistente no catálogo: {sid}")
    s0 = v["sources"][0]
    if (v.get("source_id"), v.get("via_source_id"), v.get("localizacao")) != (s0["id"], s0.get("via"), s0["loc"]):
        erros.append(f"{onde}: source_id/via_source_id/localizacao diferentes de sources[0]")
    for t in v.get("tradicoes", []):
        if t not in TRAD_IDS:
            erros.append(f"{onde}: tradição desconhecida: {t}")
    r = REGS.get(v.get("registro"))
    if not r:
        erros.append(f"{onde}: registro de origem inexistente: {v.get('registro')}")
        return
    if r["status"] == "pre_fichamento" or v.get("status") == "pre_fichamento":
        erros.append(f"{onde}: contém registro pre_fichamento ({r['id']})")
    if (r["valor"], r["source_id"], r.get("via_source_id"), r["localizacao"], revisao.status_efetivo(r, REVISORES)) != \
       (v["valor"], v["source_id"], v.get("via_source_id"), v["localizacao"], v["status"]):
        erros.append(f"{onde}: versão diverge do registro {r['id']} (regenerar fichas)")
    if not revisao.publicavel(r, REVISORES):
        erros.append(f"{onde}: registro {r['id']} com parecer nao_publicar exibido como versão")
    if v.get("revisoes", []) != revisao.resumo_publico(r, REVISORES):
        erros.append(f"{onde}: revisões da versão diferem das revisões vigentes do registro {r['id']} (regenerar fichas)")
    if v["status"] == "revisado" and not any(x["parecer"] in revisao.APROVACOES for x in v.get("revisoes", [])):
        erros.append(f"{onde}: versão 'revisado' sem aprovação vigente")


def checar_fontes(fontes, onde, erros):
    for s in fontes:
        for sid in (s.get("id"), s.get("via")):
            if not sid:
                continue
            if sid not in FONTES:
                erros.append(f"{onde}: fonte inexistente: {sid}")
            elif CATALOGO[sid]["status_verificacao"] not in LIDAS:
                erros.append(f"{onde}: fonte {sid} ainda {CATALOGO[sid]['status_verificacao']} (exige conferido_web ou acima)")


def checar_glossario(erros):
    p = RAIZ / "data/glossario.json"
    if not p.exists():
        erros.append("data/glossario.json ausente")
        return 0
    termos = ler(p)["termos"]
    vg = validador("glossario.schema.json")
    ids = [t.get("id") for t in termos]
    for i in {i for i in ids if ids.count(i) > 1}:
        erros.append(f"glossario/{i}: id repetido")
    for t in termos:
        onde = f"glossario/{t.get('id')}"
        if vg:
            erros += [f"{onde}: {e.message}" for e in vg.iter_errors(t)]
        checar_fontes(t.get("sources", []), onde, erros)
        for d in t.get("divergencias", []):
            checar_fontes(d.get("sources", []), onde, erros)
        for tr in t.get("tradicoes", []):
            if tr not in TRAD_IDS:
                erros.append(f"{onde}: tradição desconhecida: {tr}")
        for v in t.get("ver_tambem", []):
            if v not in ids:
                erros.append(f"{onde}: ver_tambem aponta para termo inexistente: {v}")
    return len(termos)


def main():
    erros = []
    vo, vc, vt = validador("orixa.schema.json"), validador("conexao.schema.json"), validador("tradicao.schema.json")
    if vt:
        for t in TRADICOES:
            erros += [f"tradicoes/{t.get('id')}: {e.message}" for e in vt.iter_errors(t)]
    enum = set(ler(RAIZ / "schemas/fonte.schema.json")["$defs"]["tradicao"]["enum"])
    if enum != TRAD_IDS:
        erros.append(f"tradicoes.json difere do enum de fonte.schema.json: {sorted(enum ^ TRAD_IDS)}")
    for t in TRADICOES:
        checar_fontes(t["sources"], f"tradicoes/{t['id']}", erros)
        if t["status"] == "rascunho_sem_fonte" and t["sources"]:
            erros.append(f"tradicoes/{t['id']}: tem fontes mas status rascunho_sem_fonte")
    n_termos = checar_glossario(erros)

    n_versoes = 0
    fichas = sorted((RAIZ / "data/orixas").glob("*.json"))
    for p in fichas:
        f = ler(p)
        if vo:
            erros += [f"{p.name}: {e.message} em /{'/'.join(map(str, e.path))}" for e in vo.iter_errors(f)]
        presentes = set()
        for a, versoes in f.get("atributos", {}).items():
            for i, v in enumerate(versoes):
                n_versoes += 1
                presentes.add(v.get("registro"))
                checar_versao(v, f"{p.stem}/{a}[{i}]", erros)
        # revisão não apaga versões: todo registro lido está na ficha ou listado como retido
        retidos = {i for ids in f.get("pendencias", {}).get("retidos_ate_conselho", {}).values() for i in ids}
        for r in REGS.values():
            if r["orixa"] == p.stem and r["status"] in revisao.STATUS_LIDOS and r["id"] not in presentes | retidos:
                erros.append(f"{p.stem}: registro {r['id']} ({r['status']}) sumiu da ficha sem estar em retidos_ate_conselho")
        for x in f.get("revisao", []):
            if x["revisor_id"] not in REVISORES:
                erros.append(f"{p.stem}: revisao cita revisor inexistente {x['revisor_id']}")

    c = ler(RAIZ / "data/conexoes.json")
    nos = {n["id"] for n in c["nos"]}
    for a in c["arestas"]:
        if vc:
            erros += [f"conexoes/{a.get('id')}: {e.message}" for e in vc.iter_errors(a)]
        for n in (a["origem"], a["destino"]):
            if n not in nos:
                erros.append(f"conexoes/{a['id']}: nó inexistente {n}")
        for i, v in enumerate(a["versoes"]):
            checar_versao(v, f"conexoes/{a['id']}[{i}]", erros)

    ve = validador("entidade.schema.json")
    ents = ler(RAIZ / "data/entidades_equivalentes.json")["entidades"]
    ids_arestas = {a["id"] for a in c["arestas"]}
    for e in ents:
        if ve:
            erros += [f"entidades/{e.get('id')}: {m.message}" for m in ve.iter_errors(e)]
        for q in e["equivale_a"]:
            if q["aresta"] not in ids_arestas:
                erros.append(f"entidades/{e['id']}: aresta inexistente {q['aresta']}")
        for i, v in enumerate(e["versoes"]):
            checar_versao(v, f"entidades/{e['id']}[{i}]", erros)

    # em dia com o fichamento? (regera em memória e compara)
    antes = {p: p.read_text(encoding="utf-8") for p in fichas + [RAIZ / "data/conexoes.json", RAIZ / "data/entidades_equivalentes.json"]}
    subprocess.run([sys.executable, str(RAIZ / "scripts/gerar_fichas.py")], capture_output=True, check=True)
    for p, txt in antes.items():
        if p.read_text(encoding="utf-8") != txt:
            erros.append(f"{p.relative_to(RAIZ)}: desatualizado em relação ao fichamento (foi regenerado agora; conferir o diff)")

    print(f"{len(fichas)} fichas, {n_versoes} versões; {len(c['arestas'])} arestas; {len(ents)} entidades; {len(TRADICOES)} tradições; {n_termos} termos no glossário"
          + ("" if vo else " (jsonschema ausente: esquema não checado)"))
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
