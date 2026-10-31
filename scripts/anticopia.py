#!/usr/bin/env python3
"""Detector anti-cópia simples (n-gramas).

Regra do projeto: nunca copiar trechos de livros; sempre parafrasear e citar.
Este script procura sinais de cópia nos textos redigidos pelo projeto
(valor, parafrase e nota do fichamento; descrições e notas de data/tradicoes.json;
definições, divergências e notas de data/glossario.json):

1. Citação longa entre aspas (>= LIMITE_CITACAO palavras) -> ERRO.
   Citações curtas (>= 6 palavras) são listadas como aviso para conferência.
2. Comparação com textos de referência (opcional): se a variável de ambiente
   ANTICOPIA_REFS apontar para um diretório com arquivos .txt (textos das
   obras, mantidos FORA do repositório), qualquer sequência de N palavras
   (padrão 8) idêntica entre um texto do projeto e uma referência -> ERRO.
3. Paráfrases de registros diferentes da mesma fonte que compartilham uma
   sequência de N palavras -> aviso (pode indicar redação colada da fonte).

Uso: python3 scripts/anticopia.py [--n 8]
     ANTICOPIA_REFS=~/refs-orixas python3 scripts/anticopia.py
Sai com código 1 se houver erro.
"""
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LIMITE_CITACAO = 15
AVISO_CITACAO = 6
ASPAS = re.compile(r"[\"“”«»]([^\"“”«»]{3,})[\"“”«»]|(?<!\w)['‘’]([^'‘’]{3,}?)['‘’](?!\w)")


def normalizar(t):
    t = unicodedata.normalize("NFC", t.lower())
    return re.findall(r"\w+", t)


def ngramas(palavras, n):
    return {" ".join(palavras[i:i + n]) for i in range(len(palavras) - n + 1)}


def textos_do_projeto():
    """(rótulo, fonte, texto) para cada campo redigido pelo projeto."""
    for p in sorted((RAIZ / "data" / "fichamento").glob("*.json")):
        if p.name == "divergencias.json":
            continue
        for r in json.loads(p.read_text(encoding="utf-8"))["registros"]:
            fonte = r.get("via_source_id") or r["source_id"]
            for campo in ("valor", "parafrase", "nota"):
                if r.get(campo):
                    yield f"{r['id']}.{campo}", fonte, r[campo]
    trad = json.loads((RAIZ / "data" / "tradicoes.json").read_text(encoding="utf-8"))
    for t in trad["tradicoes"]:
        yield f"tradicoes/{t['id']}.descricao", None, t["descricao"]
        if t.get("nota"):
            yield f"tradicoes/{t['id']}.nota", None, t["nota"]
    glos = RAIZ / "data" / "glossario.json"
    if glos.exists():
        for t in json.loads(glos.read_text(encoding="utf-8"))["termos"]:
            yield f"glossario/{t['id']}.definicao", None, t["definicao"]
            for i, d in enumerate(t.get("divergencias", [])):
                yield f"glossario/{t['id']}.divergencias[{i}]", None, d["texto"]
            if t.get("nota"):
                yield f"glossario/{t['id']}.nota", None, t["nota"]


def main():
    n = int(sys.argv[sys.argv.index("--n") + 1]) if "--n" in sys.argv else 8
    erros, avisos = [], []
    textos = list(textos_do_projeto())

    for rot, _, txt in textos:
        for m in ASPAS.finditer(txt):
            trecho = m.group(1) or m.group(2)
            k = len(normalizar(trecho))
            if k >= LIMITE_CITACAO:
                erros.append(f"{rot}: citação entre aspas com {k} palavras (limite {LIMITE_CITACAO - 1}) — parafrasear")
            elif k >= AVISO_CITACAO:
                avisos.append(f"{rot}: citação curta ({k} palavras) — conferir se é necessária: “{trecho}”")

    refs_dir = os.environ.get("ANTICOPIA_REFS")
    n_refs = 0
    if refs_dir:
        indice = defaultdict(set)
        for p in sorted(Path(refs_dir).expanduser().rglob("*.txt")):
            n_refs += 1
            for g in ngramas(normalizar(p.read_text(encoding="utf-8", errors="ignore")), n):
                indice[g].add(p.name)
        for rot, _, txt in textos:
            iguais = [g for g in ngramas(normalizar(txt), n) if g in indice]
            if iguais:
                obras = sorted({o for g in iguais for o in indice[g]})
                erros.append(f"{rot}: {len(iguais)} sequência(s) de {n} palavras idêntica(s) a {', '.join(obras)} — ex.: “{iguais[0]}”")

    por_fonte = defaultdict(list)
    for rot, fonte, txt in textos:
        if fonte and rot.endswith(".parafrase"):
            por_fonte[fonte].append((rot, ngramas(normalizar(txt), n)))
    for fonte, itens in por_fonte.items():
        for i, (r1, g1) in enumerate(itens):
            for r2, g2 in itens[i + 1:]:
                comum = g1 & g2
                if comum:
                    avisos.append(f"{r1} e {r2} ({fonte}): repetem “{sorted(comum)[0]}”")

    print(f"{len(textos)} textos verificados; n={n}; referências externas: "
          + (f"{n_refs} arquivo(s) em {refs_dir}" if refs_dir else "nenhuma (defina ANTICOPIA_REFS)"))
    for a in avisos:
        print(" aviso:", a)
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
