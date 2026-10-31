#!/usr/bin/env python3
"""Gera a matriz de divergências a partir do fichamento.

Agrupa registros por (orixá, atributo) e lista os valores distintos com
tradição, casa/região e fonte. Saída: data/fichamento/divergencias.json e,
com --markdown, uma tabela em stdout.
Só considera registros 'fichado' ou 'revisado' (lidos na fonte).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ATRS = {"dia_semana", "cores", "sincretismo", "festas", "parentesco", "origem", "elementos", "qualidades", "simbolos", "itans", "equivalencias"}


def main():
    grupos = defaultdict(list)
    for p in sorted((RAIZ / "data" / "fichamento").glob("*.json")):
        if p.name == "divergencias.json":
            continue
        for r in json.loads(p.read_text(encoding="utf-8"))["registros"]:
            if r["status"] in ("fichado", "revisado") and r["atributo"] in ATRS:
                grupos[(r["orixa"], r["atributo"])].append(r)
    saida = []
    for (o, a), regs in sorted(grupos.items()):
        valores = {r["valor"] for r in regs}
        if len(valores) < 2:
            continue
        saida.append({"orixa": o, "atributo": a, "versoes": [
            {"valor": r["valor"], "tradicoes": r["tradicoes"], "casa_ou_regiao": r["casa_ou_regiao"],
             "fonte": r["source_id"], "via": r["via_source_id"], "localizacao": r["localizacao"], "registro": r["id"]}
            for r in regs]})
    (RAIZ / "data" / "fichamento" / "divergencias.json").write_text(
        json.dumps({"_meta": {"descricao": "Gerado por scripts/divergencias.py — não editar à mão. Lista atributos com mais de uma versão registrada; versões NÃO são hierarquizadas.", "total": len(saida)}, "divergencias": saida},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    if "--markdown" in sys.argv:
        for d in saida:
            print(f"\n#### {d['orixa']} — {d['atributo']}\n")
            print("| versão | tradição | casa/região | fonte |\n|---|---|---|---|")
            for v in d["versoes"]:
                fonte = v["fonte"] + (f" (via {v['via']})" if v["via"] else "") + f", {v['localizacao']}"
                print(f"| {v['valor']} | {', '.join(v['tradicoes'])} | {v['casa_ou_regiao'] or '—'} | {fonte} |")
    else:
        print(f"{len(saida)} atributos com versões divergentes")


if __name__ == "__main__":
    main()
