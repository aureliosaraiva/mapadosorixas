#!/usr/bin/env python3
"""Monta a pasta de referências do anti-cópia (texto integral das fontes, FORA do repo).

Para cada fonte do catálogo usada em registro `fichado`/`revisado` do fichamento
(como `source_id` ou `via_source_id`), em `data/tradicoes.json` ou em
`data/glossario.json`, tenta baixar o PDF a partir de `url` e `evidencias`:

- link que já devolve PDF: salvo direto;
- página HTML (OJS, DSpace, HAL etc.): procura links de PDF/download na página
  (inclusive a troca OJS `article/view/X/Y` -> `article/download/X/Y`).

Os PDFs vão para `<destino>-pdf/<id>.pdf` e o texto para `<destino>/<id>.txt`
(`pdftotext`, ordem de leitura, com a hifenização de quebra de linha desfeita:
`religi-⏎ões` -> `religiões`). Fontes que não baixarem são listadas no fim, para
registro em `docs/pesquisa/PENDENCIAS.md`. Um PDF obtido à mão pode ser posto em
`<destino>-pdf/<id>.pdf`: o script só converte, sem baixar de novo.

Não contorna desafio anti-robô nem paywall (regra do projeto).

Uso: python3 scripts/baixar_refs.py [--destino /tmp/refs] [--ids id1,id2] [--so-converter]
Depois: ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "Mozilla/5.0 (mapadosorixas anticopia; uso academico)"}
HIFEN = re.compile(r"(\w)-\s*\n\s*(\w)")


def fontes_usadas():
    """(fontes usadas, fontes lidas como via_source_id)."""
    usadas, vias = set(), set()
    for p in sorted((RAIZ / "data" / "fichamento").glob("*.json")):
        if p.name == "divergencias.json":
            continue
        for r in json.loads(p.read_text(encoding="utf-8"))["registros"]:
            if r.get("status") in ("fichado", "revisado"):
                usadas.add(r["source_id"])
                if r.get("via_source_id"):
                    usadas.add(r["via_source_id"])
                    vias.add(r["via_source_id"])
    for arq, chave in (("tradicoes.json", "tradicoes"), ("glossario.json", "termos")):
        for t in json.loads((RAIZ / "data" / arq).read_text(encoding="utf-8"))[chave]:
            for s in t.get("sources", []):
                usadas.add(s["id"])
            for d in t.get("divergencias", []):
                for s in d.get("sources", []):
                    usadas.add(s["id"])
    return usadas, vias


def candidatos(fonte):
    urls = []
    for u in [fonte.get("url")] + list(fonte.get("evidencias") or []):
        if u and u not in urls and "api.crossref.org" not in u and "openlibrary.org" not in u:
            urls.append(u)
    return urls


def eh_pdf(resp):
    return resp.content[:5] == b"%PDF-"


def links_pdf(html, base):
    achados = []
    for href in re.findall(r'(?:href|content)="([^"]+)"', html):
        h = href.replace("&amp;", "&")
        baixo = h.lower()
        if (".pdf" in baixo or "/download/" in baixo or "bitstream" in baixo
                or "citation_pdf_url" in baixo):
            achados.append(urllib.parse.urljoin(base, h))
    # meta citation_pdf_url
    m = re.search(r'name="citation_pdf_url"\s+content="([^"]+)"', html)
    if m:
        achados.insert(0, m.group(1))
    # OJS: view/X/Y -> download/X/Y
    for h in list(achados):
        if "/article/view/" in h:
            achados.append(h.replace("/article/view/", "/article/download/"))
    vistos, saida = set(), []
    for a in achados:
        if a not in vistos:
            vistos.add(a)
            saida.append(a)
    return saida


def dspace7(url, sessao):
    """DSpace 7 (página Angular sem links): pega o PDF do bundle ORIGINAL pela API REST."""
    m = re.match(r"(https?://[^/]+)/items/([0-9a-f-]{36})", url)
    if not m:
        return None
    api = f"{m.group(1)}/server/api/core/items/{m.group(2)}/bundles"
    try:
        bundles = sessao.get(api, headers=UA, timeout=60).json()["_embedded"]["bundles"]
        for b in bundles:
            if b["name"] != "ORIGINAL":
                continue
            bits = sessao.get(b["_links"]["bitstreams"]["href"], headers=UA, timeout=60).json()
            for bit in bits["_embedded"]["bitstreams"]:
                r = sessao.get(bit["_links"]["content"]["href"], headers=UA, timeout=120)
                if eh_pdf(r):
                    return r.content
    except (requests.RequestException, ValueError, KeyError):
        return None
    return None


def baixar(url, sessao, profundidade=0):
    conteudo = dspace7(url, sessao)
    if conteudo:
        return conteudo, None
    try:
        r = sessao.get(url, headers=UA, timeout=60, allow_redirects=True)
    except requests.RequestException as e:
        return None, f"{url}: {type(e).__name__}"
    if r.status_code != 200:
        return None, f"{url}: HTTP {r.status_code}"
    if eh_pdf(r):
        return r.content, None
    if profundidade >= 2 or "html" not in r.headers.get("content-type", ""):
        return None, f"{url}: não é PDF"
    ultimo = f"{url}: nenhum link de PDF"
    for link in links_pdf(r.text, r.url)[:12]:
        conteudo, erro = baixar(link, sessao, profundidade + 1)
        if conteudo:
            return conteudo, None
        ultimo = erro
    return None, ultimo


def converter(pdf, txt):
    bruto = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    txt.write_text(HIFEN.sub(r"\1\2", bruto), encoding="utf-8")
    return len(bruto.split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--destino", default="/tmp/refs")
    ap.add_argument("--ids", default="")
    ap.add_argument("--so-converter", action="store_true")
    a = ap.parse_args()
    destino = Path(a.destino)
    if RAIZ in destino.resolve().parents or destino.resolve() == RAIZ:
        sys.exit("O destino deve ficar FORA do repositório.")
    pdfs = Path(str(destino) + "-pdf")
    destino.mkdir(parents=True, exist_ok=True)
    pdfs.mkdir(parents=True, exist_ok=True)

    catalogo = {f["id"]: f for f in json.loads((RAIZ / "data/fontes/catalogo.json").read_text(encoding="utf-8"))["fontes"]}
    usadas, vias = fontes_usadas()
    ids = sorted(a.ids.split(",")) if a.ids else sorted(usadas)
    # a fonte efetivamente lida (via) vem antes da fonte de 2ª mão, que costuma
    # apontar para o mesmo PDF; PDF repetido não gera segundo .txt
    ids.sort(key=lambda i: i not in vias)
    sessao = requests.Session()
    falhas, hashes, repetidos = [], {}, []
    for i in ids:
        pdf, txt = pdfs / f"{i}.pdf", destino / f"{i}.txt"
        if not pdf.exists() and not a.so_converter:
            erros = []
            for u in candidatos(catalogo.get(i, {})):
                conteudo, erro = baixar(u, sessao)
                if conteudo:
                    pdf.write_bytes(conteudo)
                    break
                erros.append(erro)
            if not pdf.exists():
                falhas.append((i, "; ".join(erros) or "sem url/evidencias no catálogo"))
                continue
        if pdf.exists():
            h = hashlib.sha256(pdf.read_bytes()).hexdigest()
            if h in hashes:
                txt.unlink(missing_ok=True)
                repetidos.append((i, hashes[h]))
                continue
            hashes[h] = i
            n = converter(pdf, txt)
            print(f"ok  {i}: {n} palavras")
            if n < 1000:
                txt.unlink()
                falhas.append((i, f"PDF sem texto extraível ({n} palavras; imagem sem OCR?)"))
    for i, j in repetidos:
        print(f"=   {i}: mesmo PDF que {j} (fonte citada de 2ª mão); comparada via {j}.txt")
    print(f"\n{len(ids) - len(falhas) - len(repetidos)}/{len(ids)} fontes com texto próprio em {destino}")
    if falhas:
        print("\nNão baixadas (registrar em docs/pesquisa/PENDENCIAS.md se ainda não estiverem):")
        for i, motivo in falhas:
            print(f" - {i}: {motivo}")


if __name__ == "__main__":
    main()
