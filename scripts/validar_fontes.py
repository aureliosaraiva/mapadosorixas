#!/usr/bin/env python3
"""Valida data/fontes/catalogo.json.

Usa `jsonschema` se estiver instalado; sempre roda as checagens próprias
(ids únicos, regras de status). Uso: python3 scripts/validar_fontes.py
"""
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CATALOGO = RAIZ / "data" / "fontes" / "catalogo.json"
SCHEMA = RAIZ / "schemas" / "fonte.schema.json"


def main() -> int:
    doc = json.loads(CATALOGO.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    fontes = doc["fontes"]
    erros = []

    try:
        import jsonschema
        validador = jsonschema.Draft202012Validator(schema)
        for f in fontes:
            for e in validador.iter_errors(f):
                erros.append(f"{f.get('id', '?')}: {e.message}")
    except ImportError:
        obrig = schema["required"]
        enums = {k: set(v["enum"]) for k, v in schema["properties"].items() if "enum" in v}
        trad_ok = set(schema["$defs"]["tradicao"]["enum"])
        for f in fontes:
            for campo in obrig:
                if campo not in f:
                    erros.append(f"{f.get('id', '?')}: campo obrigatório ausente: {campo}")
            for campo, valores in enums.items():
                if campo in f and f[campo] not in valores:
                    erros.append(f"{f['id']}: valor inválido em {campo}: {f[campo]!r}")
            for t in f.get("tradicoes", []):
                if t not in trad_ok:
                    erros.append(f"{f['id']}: tradição desconhecida: {t}")
            extras = set(f) - set(schema["properties"])
            if extras:
                erros.append(f"{f['id']}: campos não previstos: {sorted(extras)}")

    ids = Counter(f["id"] for f in fontes)
    erros += [f"id duplicado: {i}" for i, n in ids.items() if n > 1]

    for f in fontes:
        st = f.get("status_verificacao")
        if st in {"conferido_web", "verificado", "fichado", "revisado"} and not (f.get("evidencias") or f.get("url")):
            erros.append(f"{f['id']}: status {st} exige 'evidencias' ou 'url'")

    print(f"{len(fontes)} fontes")
    print("status:", dict(Counter(f["status_verificacao"] for f in fontes)))
    print("idiomas:", dict(Counter(f["idioma"] for f in fontes)))
    print("categorias:", dict(Counter(f["categoria"] for f in fontes)))
    trad = Counter(t for f in fontes for t in f["tradicoes"])
    print("tradições:", dict(trad.most_common()))
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
