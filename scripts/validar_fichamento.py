#!/usr/bin/env python3
"""Valida data/fichamento/*.json contra o esquema e o catálogo de fontes,
e mostra a cobertura de atributos por orixá (lacunas).

Uso: python3 scripts/validar_fichamento.py [--markdown]
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((RAIZ / "schemas" / "fichamento.schema.json").read_text(encoding="utf-8"))
CATALOGO = json.loads((RAIZ / "data" / "fontes" / "catalogo.json").read_text(encoding="utf-8"))
FONTES = {f["id"]: f for f in CATALOGO["fontes"]}
ATRIBUTOS = SCHEMA["properties"]["atributo"]["enum"]
ORIXAS = SCHEMA["properties"]["orixa"]["enum"]


def carregar():
    regs = []
    for o in ORIXAS:
        p = RAIZ / "data" / "fichamento" / f"{o}.json"
        if p.exists():
            regs += json.loads(p.read_text(encoding="utf-8"))["registros"]
    return regs


def validar(regs):
    erros = []
    try:
        import jsonschema
        v = jsonschema.Draft202012Validator(SCHEMA)
        for r in regs:
            erros += [f"{r.get('id')}: {e.message}" for e in v.iter_errors(r)]
    except ImportError:
        pass
    ids = Counter(r["id"] for r in regs)
    erros += [f"id duplicado: {i}" for i, n in ids.items() if n > 1]
    for r in regs:
        for campo in ("source_id", "via_source_id"):
            sid = r.get(campo)
            if sid and sid not in FONTES:
                erros.append(f"{r['id']}: {campo} inexistente no catálogo: {sid}")
        # A fonte efetivamente lida é a intermediária (via_source_id), quando houver.
        lida = r.get("via_source_id") or r["source_id"]
        f = FONTES.get(lida)
        if f and r["status"] in ("fichado", "revisado"):
            if f["status_verificacao"] in ("pista", "a_verificar"):
                erros.append(f"{r['id']}: status {r['status']} exige fonte verificada (fonte está '{f['status_verificacao']}')")
            if r["localizacao"].strip().lower() == "a conferir":
                erros.append(f"{r['id']}: status {r['status']} exige localização (página)")
    return erros


def cobertura(regs, markdown=False):
    cob = defaultdict(lambda: defaultdict(int))
    for r in regs:
        cob[r["orixa"]][r["atributo"]] += 1
    if markdown:
        print("| atributo | " + " | ".join(ORIXAS) + " |")
        print("|---|" + "---:|" * len(ORIXAS))
        for a in ATRIBUTOS:
            print(f"| {a} | " + " | ".join(str(cob[o][a] or "—") for o in ORIXAS) + " |")
    else:
        for o in ORIXAS:
            falta = [a for a in ATRIBUTOS if not cob[o][a]]
            print(f"{o}: {sum(cob[o].values())} registros; sem registro: {', '.join(falta)}")


def main():
    regs = carregar()
    erros = validar(regs)
    md = "--markdown" in sys.argv
    if not md:
        print(f"{len(regs)} registros; status: {dict(Counter(r['status'] for r in regs))}")
    cobertura(regs, md)
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    if not md:
        print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
