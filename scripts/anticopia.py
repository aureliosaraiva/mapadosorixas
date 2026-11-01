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
   Com referências, também se compara cada texto SÓ com a(s) fonte(s) que ele
   cita (arquivo `<source_id>.txt`): sequência de AVISO_FONTE a N-1 palavras
   (padrão 6–7) igual à fonte citada -> aviso "redação próxima da fonte". É
   onde aparecem as paráfrases "coladas" (auditorias anticopia-01 e -02). Cada
   aviso deve ser reescrito ou justificado (nome próprio, lista, data, termo
   técnico, expressão corrente) no relatório da sessão.
3. Paráfrases de registros diferentes da mesma fonte que compartilham uma
   sequência de N palavras -> aviso (pode indicar redação colada da fonte).

Sequências formadas sobretudo por números e marcas de página (ex.: a
referência bibliográfica "Verger 1997, pp. 76–8; 1999, p. 132") não contam:
são citação bibliográfica, não texto da obra. Palavras comuns não são
ignoradas; a regra de 8 palavras continua valendo para qualquer texto.

Como montar a pasta de referências (sempre FORA do repositório):
  python3 scripts/baixar_refs.py --destino /tmp/refs
  - lê `url` e `evidencias` do catálogo das fontes usadas em registros
    `fichado`/`revisado`, em tradições e no glossário; baixa os PDFs para
    /tmp/refs-pdf/ e grava /tmp/refs/<source_id>.txt (pdftotext, ordem de
    leitura, hifenização de fim de linha desfeita: "religi-\nões" -> "religiões");
  - PDF obtido à mão: salvar como /tmp/refs-pdf/<source_id>.pdf e rodar com
    --so-converter; texto de página HTML: salvar como /tmp/refs/<source_id>.txt;
  - o nome do arquivo deve ser o `source_id`, para a comparação por fonte citada;
  - fontes que não baixarem vão para docs/pesquisa/PENDENCIAS.md.
Toda sessão que ficha uma fonte roda este script com o texto integral dela
antes do commit (regra do CLAUDE.md).

Uso: python3 scripts/anticopia.py [--n 8]
     ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py
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
AVISO_FONTE = 6
HIFEN = re.compile(r"(\w)-[ \t]*\n\s*(\w)")
# tokens de referência bibliográfica: números, marcas de página/volume
REF_TOKENS = {"p", "pp", "v", "vol", "n", "cf", "apud", "ed", "fl", "f", "nota"}
ASPAS = re.compile(r"[\"“”«»]([^\"“”«»]{3,})[\"“”«»]|(?<!\w)['‘’]([^'‘’]{3,}?)['‘’](?!\w)")


def normalizar(t):
    t = unicodedata.normalize("NFC", t.lower())
    return re.findall(r"\w+", t)


def ngramas(palavras, n):
    return {" ".join(palavras[i:i + n]) for i in range(len(palavras) - n + 1)}


def eh_referencia(grama):
    """N-grama formado sobretudo por números e marcas de página (citação bibliográfica)."""
    toks = grama.split()
    k = sum(1 for t in toks if t.isdigit() or t in REF_TOKENS)
    return k * 2 >= len(toks)


def textos_do_projeto():
    """(rótulo, fontes, texto) para cada campo redigido pelo projeto.

    `fontes` é a lista de source_ids citados (no fichamento, a fonte lida
    `via_source_id` vem primeiro)."""
    for p in sorted((RAIZ / "data" / "fichamento").glob("*.json")):
        if p.name == "divergencias.json":
            continue
        for r in json.loads(p.read_text(encoding="utf-8"))["registros"]:
            fontes = [f for f in (r.get("via_source_id"), r["source_id"]) if f]
            for campo in ("valor", "parafrase", "nota"):
                if r.get(campo):
                    yield f"{r['id']}.{campo}", fontes, r[campo]
    trad = json.loads((RAIZ / "data" / "tradicoes.json").read_text(encoding="utf-8"))
    for t in trad["tradicoes"]:
        fontes = [s["id"] for s in t.get("sources", [])]
        yield f"tradicoes/{t['id']}.descricao", fontes, t["descricao"]
        if t.get("nota"):
            yield f"tradicoes/{t['id']}.nota", fontes, t["nota"]
    glos = RAIZ / "data" / "glossario.json"
    if glos.exists():
        for t in json.loads(glos.read_text(encoding="utf-8"))["termos"]:
            fontes = [s["id"] for s in t.get("sources", [])]
            yield f"glossario/{t['id']}.definicao", fontes, t["definicao"]
            for i, d in enumerate(t.get("divergencias", [])):
                fd = [s["id"] for s in d.get("sources", [])] or fontes
                yield f"glossario/{t['id']}.divergencias[{i}]", fd, d["texto"]
            if t.get("nota"):
                yield f"glossario/{t['id']}.nota", fontes, t["nota"]


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
    proximos = []
    if refs_dir:
        indice = defaultdict(set)
        por_id = {}
        com_erro = set()
        for p in sorted(Path(refs_dir).expanduser().rglob("*.txt")):
            n_refs += 1
            palavras = normalizar(HIFEN.sub(r"\1\2", p.read_text(encoding="utf-8", errors="ignore")))
            por_id[p.stem] = palavras
            for g in ngramas(palavras, n):
                indice[g].add(p.name)
        for rot, _, txt in textos:
            iguais = sorted(g for g in ngramas(normalizar(txt), n) if g in indice and not eh_referencia(g))
            if iguais:
                obras = sorted({o for g in iguais for o in indice[g]})
                com_erro.add(rot)
                erros.append(f"{rot}: {len(iguais)} sequência(s) de {n} palavras idêntica(s) a {', '.join(obras)} — ex.: “{iguais[0]}”")
        # redação próxima da fonte citada: trechos de AVISO_FONTE+ palavras
        # iguais à fonte citada, fundidos em trechos máximos (< n palavras)
        cache = {}
        for rot, fontes, txt in textos:
            pal = normalizar(txt)
            vistos = set()
            for f in fontes or []:
                if f not in por_id:
                    continue
                if f not in cache:
                    cache[f] = ngramas(por_id[f], AVISO_FONTE)
                k = AVISO_FONTE
                pos = [i for i in range(len(pal) - k + 1)
                       if " ".join(pal[i:i + k]) in cache[f] and not eh_referencia(" ".join(pal[i:i + k]))]
                trechos, ini, fim = [], None, None
                for i in pos:
                    if ini is not None and i == fim + 1:
                        fim = i
                    else:
                        if ini is not None:
                            trechos.append((ini, fim))
                        ini = fim = i
                if ini is not None:
                    trechos.append((ini, fim))
                for a, b in trechos:
                    tam = b - a + k
                    trecho = " ".join(pal[a:b + k])
                    # trechos fundidos de 8+ só aparecem aqui se o campo não deu erro
                    # (6-gramas vizinhos no texto, mas não contíguos na fonte)
                    if (tam < n or rot not in com_erro) and trecho not in vistos:
                        vistos.add(trecho)
                        proximos.append(f"{rot}: {tam} palavras iguais a {f} — “{trecho}”")

    por_fonte = defaultdict(list)
    for rot, fontes, txt in textos:
        if fontes and rot.endswith(".parafrase"):
            por_fonte[fontes[0]].append((rot, ngramas(normalizar(txt), n)))
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
    if proximos:
        print(f"\n{len(proximos)} aviso(s) de redação próxima da fonte citada "
              f"({AVISO_FONTE}–{n - 1} palavras; reescrever ou justificar no relatório):")
        for a in proximos:
            print(" próximo:", a)
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
