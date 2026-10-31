#!/usr/bin/env python3
"""Valida as fichas (data/orixas/*.json), data/conexoes.json e data/tradicoes.json.

Checagens:
- esquema (schemas/orixa.schema.json, conexao.schema.json, tradicao.schema.json), se jsonschema estiver instalado;
- toda versão tem ao menos uma fonte, e toda fonte (id e via) existe no catálogo;
- source_id/via_source_id/localizacao da versão batem com sources[0];
- nenhuma versão vem de registro 'pre_fichamento' (confere contra o fichamento);
- cada versão bate com o registro de origem (valor, fonte, página);
- toda tradição citada existe em data/tradicoes.json;
- fichas e grafo estão em dia com o fichamento (regenerar com scripts/gerar_fichas.py).

Uso: python3 scripts/validar_fichas.py
"""
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def ler(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


FONTES = {f["id"] for f in ler(RAIZ / "data/fontes/catalogo.json")["fontes"]}
TRADICOES = ler(RAIZ / "data/tradicoes.json")["tradicoes"]
TRAD_IDS = {t["id"] for t in TRADICOES}
REGS = {}
for p in (RAIZ / "data/fichamento").glob("*.json"):
    if p.name != "divergencias.json":
        REGS.update({r["id"]: r for r in ler(p)["registros"]})


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
    if (r["valor"], r["source_id"], r.get("via_source_id"), r["localizacao"], r["status"]) != \
       (v["valor"], v["source_id"], v.get("via_source_id"), v["localizacao"], v["status"]):
        erros.append(f"{onde}: versão diverge do registro {r['id']} (regenerar fichas)")


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
        for s in t["sources"]:
            if s["id"] not in FONTES:
                erros.append(f"tradicoes/{t['id']}: fonte inexistente: {s['id']}")

    n_versoes = 0
    fichas = sorted((RAIZ / "data/orixas").glob("*.json"))
    for p in fichas:
        f = ler(p)
        if vo:
            erros += [f"{p.name}: {e.message} em /{'/'.join(map(str, e.path))}" for e in vo.iter_errors(f)]
        for a, versoes in f.get("atributos", {}).items():
            for i, v in enumerate(versoes):
                n_versoes += 1
                checar_versao(v, f"{p.stem}/{a}[{i}]", erros)

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

    # em dia com o fichamento? (regera em memória e compara)
    antes = {p: p.read_text(encoding="utf-8") for p in fichas + [RAIZ / "data/conexoes.json"]}
    subprocess.run([sys.executable, str(RAIZ / "scripts/gerar_fichas.py")], capture_output=True, check=True)
    for p, txt in antes.items():
        if p.read_text(encoding="utf-8") != txt:
            erros.append(f"{p.relative_to(RAIZ)}: desatualizado em relação ao fichamento (foi regenerado agora; conferir o diff)")

    print(f"{len(fichas)} fichas, {n_versoes} versões; {len(c['arestas'])} arestas; {len(TRADICOES)} tradições"
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
