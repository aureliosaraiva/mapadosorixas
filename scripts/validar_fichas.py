#!/usr/bin/env python3
"""Valida as fichas (data/orixas/*.json), data/conexoes.json, data/entidades_equivalentes.json, data/tradicoes.json, data/glossario.json, data/entidades.json (lista-mestra) e data/itans.json.

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
- lista-mestra: toda ficha é de uma entidade de data/entidades.json; toda entidade
  com registro fichado tem ficha; nós de tipo 'orixa' do grafo estão na lista-mestra;
- itãs (schemas/ita.schema.json): ids únicos; entidades na lista-mestra ou no
  grafo; versão espelhada bate com o registro (atributo 'itans'); versão própria
  'fichado' tem fonte lida e página; tradições existentes; arestas existentes;
  um registro de itã não aparece em dois itãs;
- fichas, grafo, status_conteudo da lista-mestra e espelhos dos itãs estão em dia
  com o fichamento (regenerar com scripts/gerar_fichas.py).

Uso: python3 scripts/validar_fichas.py
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import entidades as ent  # noqa: E402
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


def checar_lista_mestra(fichas, erros):
    lista = ent.por_id(RAIZ)
    for p in fichas:
        if p.stem not in lista:
            erros.append(f"{p.name}: ficha de entidade fora de data/entidades.json")
        elif ler(p).get("rotulo") != lista[p.stem]["rotulo"]:
            erros.append(f"{p.name}: rótulo difere de data/entidades.json")
    com_ficha = {p.stem for p in fichas}
    for eid, regs in ent.registros_por_entidade(RAIZ).items():
        if any(r["status"] in revisao.STATUS_LIDOS for r in regs) and eid not in com_ficha:
            erros.append(f"entidades/{eid}: tem registro fichado mas não tem ficha (regenerar)")
    for nid, n in ler(RAIZ / "data/conexoes_alvos.json")["nos"].items():
        if n.get("tipo") == "orixa" and nid not in lista:
            erros.append(f"conexoes_alvos/{nid}: nó de tipo orixa fora de data/entidades.json")
    return len(lista)


def checar_itans(arestas, nos_grafo, erros):
    p = RAIZ / "data/itans.json"
    if not p.exists():
        return 0, 0
    itans = ler(p)["itans"]
    vi = validador("ita.schema.json")
    validos = set(ent.ids(RAIZ)) | set(nos_grafo)
    ids = [i.get("id") for i in itans]
    for i in {i for i in ids if ids.count(i) > 1}:
        erros.append(f"itans/{i}: id repetido")
    usados, nv = {}, 0
    for it in itans:
        onde = f"itans/{it.get('id')}"
        if vi:
            erros += [f"{onde}: {e.message} em /{'/'.join(map(str, e.path))}" for e in vi.iter_errors(it)]
        for e in it.get("entidades", []):
            if e not in validos:
                erros.append(f"{onde}: entidade desconhecida {e} (nem na lista-mestra nem no grafo)")
        for a in it.get("arestas", []):
            if a not in arestas:
                erros.append(f"{onde}: aresta inexistente {a}")
        for k, v in enumerate(it.get("versoes", [])):
            nv += 1
            ov = f"{onde}[{k}]"
            for t in v.get("tradicoes", []):
                if t not in TRAD_IDS:
                    erros.append(f"{ov}: tradição desconhecida: {t}")
            rid = v.get("registro")
            if rid:
                if rid in usados:
                    erros.append(f"{ov}: registro {rid} já está em {usados[rid]}")
                usados[rid] = it.get("id")
                r = REGS.get(rid)
                if r is None:
                    erros.append(f"{ov}: registro inexistente {rid}")
                    continue
                if r["atributo"] != "itans":
                    erros.append(f"{ov}: registro {rid} não é do atributo 'itans'")
                esperado = {"valor": r["valor"], "resumo": r["parafrase"], "tradicoes": r["tradicoes"],
                            "casa_ou_regiao": r.get("casa_ou_regiao"), "nota": r.get("nota"), "status": r["status"],
                            "sources": [{"id": r["source_id"], "loc": r["localizacao"], "via": r.get("via_source_id")}]}
                for c, x in esperado.items():
                    if v.get(c) != x:
                        erros.append(f"{ov}: campo {c} difere do registro {rid} (regenerar com gerar_fichas.py)")
            elif v.get("status") in revisao.STATUS_LIDOS:
                checar_fontes(v.get("sources", []), ov, erros)
                if any(s["loc"].strip().lower() == "a conferir" for s in v.get("sources", [])):
                    erros.append(f"{ov}: versão {v['status']} exige página")
    return len(itans), nv


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

    n_lista = checar_lista_mestra(fichas, erros)
    n_itans, n_vitans = checar_itans(ids_arestas, nos, erros)

    # em dia com o fichamento? (regera e compara)
    extras = [RAIZ / "data" / n for n in ("conexoes.json", "entidades_equivalentes.json", "entidades.json", "itans.json")]
    antes = {p: p.read_text(encoding="utf-8") for p in fichas + extras if p.exists()}
    subprocess.run([sys.executable, str(RAIZ / "scripts/gerar_fichas.py")], capture_output=True, check=True)
    for p, txt in antes.items():
        if not p.exists():
            erros.append(f"{p.relative_to(RAIZ)}: removido ao regenerar (entidade sem registro lido)")
        elif p.read_text(encoding="utf-8") != txt:
            erros.append(f"{p.relative_to(RAIZ)}: desatualizado em relação ao fichamento (foi regenerado agora; conferir o diff)")
    for p in sorted((RAIZ / "data/orixas").glob("*.json")):
        if p not in antes:
            erros.append(f"{p.relative_to(RAIZ)}: ficha nova criada ao regenerar (conferir e versionar)")

    print(f"{len(fichas)} fichas, {n_versoes} versões; {len(c['arestas'])} arestas; {len(ents)} entidades equivalentes; "
          f"{n_lista} entidades na lista-mestra; {n_itans} itãs ({n_vitans} versões); {len(TRADICOES)} tradições; {n_termos} termos no glossário"
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
