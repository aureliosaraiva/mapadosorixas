#!/usr/bin/env python3
"""Monta o acervo de texto integral das fontes (`acervo/`), para leitura e anti-cópia.

Para cada fonte do catálogo usada em registro `fichado`/`revisado` do fichamento
(como `source_id` ou `via_source_id`), em `data/tradicoes.json` ou em
`data/glossario.json` — mais as de `acervo/urls_extras.json` —, tenta baixar o
PDF a partir de `url` e `evidencias` do catálogo (e das URLs extras):

- link que já devolve PDF: salvo direto;
- página HTML (OJS, DSpace, HAL etc.): procura links de PDF/download na página
  (inclusive a troca OJS `article/view/X/Y` -> `article/download/X/Y`);
- se `requests` não conseguir (ex.: desafio Anubis do HAL na página), tenta o
  link com `curl`, que no HAL baixa o arquivo direto.

Destino padrão: o acervo externo no repositório PRIVADO `aureliosaraiva/orixas-fontes`
(variável `ACERVO_DIR`; sem ela, `../orixas-fontes` se o clone existir; senão o
`acervo/` local, ignorado pelo git). Ver `scripts/acervo_dir.py` e `scripts/acervo_sync.sh`.
Antes de baixar, procura o PDF no destino e, se o destino for externo, no `acervo/` local
(copiado sem novo download).

Estrutura (no destino; aqui como `acervo/`):
  acervo/pdf/<id>.pdf   PDF original (ou um PDF salvo à mão com esse nome)
  acervo/txt/<id>.txt   `pdftotext`, ordem de leitura, hifenização de fim de linha
                        desfeita (`religi-⏎ões` -> `religiões`)
  acervo/indice.json    id, título curto, URL de origem, data do download, páginas,
                        palavras, sha256 e observação de acesso (inclusive falhas)
  acervo/INDICE.md      o mesmo índice em tabela (gerado)

O que já existe é pulado (não baixa de novo; só reconverte com `--reconverter`).
Fontes que não baixarem são listadas no fim e marcadas no índice, para registro
em `docs/pesquisa/PENDENCIAS.md`; o autor salva o PDF à mão em `acervo/pdf/<id>.pdf`
e roda com `--so-converter`.

ATENÇÃO: o conteúdo de `acervo/pdf` e `acervo/txt` é de uso interno (direitos dos
autores/editoras). Não vai para o site, e só pode ser versionado se o repositório
for PRIVADO (ver acervo/LEIAME.md). Enquanto o repositório for público, o
`.gitignore` mantém esses arquivos fora do git e o CI falha se algum entrar.

Não contorna desafio anti-robô nem paywall (regra do projeto).

Uso: python3 scripts/baixar_refs.py [--destino DIR] [--ids id1,id2]
                                    [--so-converter] [--reconverter]
Depois: python3 scripts/anticopia.py   (usa acervo/txt por padrão)
"""
import argparse
import datetime
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from acervo_dir import acervo_padrao  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
ACERVO = RAIZ / "acervo"  # local, ignorado pelo git; guarda também urls_extras.json (metadado)
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


def candidatos(fonte, extras=()):
    urls = []
    for u in list(extras) + [fonte.get("url")] + list(fonte.get("evidencias") or []):
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


def baixar_curl(url):
    """Baixa com curl (segue redirecionamentos); devolve bytes se for PDF."""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
        # user-agent padrão do curl (identificação honesta); com ele o HAL serve o
        # arquivo direto, sem a página de desafio que recebe o UA de navegador
        r = subprocess.run(["curl", "-sSL", "--max-time", "300", "-o", tmp.name, url],
                           capture_output=True, text=True)
        dados = Path(tmp.name).read_bytes()
    if r.returncode == 0 and dados[:5] == b"%PDF-":
        return dados
    return None


def archive_org(url, sessao, texto=False):
    """Internet Archive (`/details/<id>`): pega o PDF do item pela API de metadados
    (ou, com texto=True, o OCR `_djvu.txt`, para PDF digitalizado sem camada de texto)."""
    m = re.match(r"https?://archive\.org/(?:details|download)/([^/?#]+)", url or "")
    if not m:
        return None
    item = m.group(1)
    try:
        arquivos = [f["name"] for f in sessao.get(f"https://archive.org/metadata/{item}", headers=UA, timeout=60).json().get("files", [])]
        sufixos = ("_djvu.txt",) if texto else ("_text.pdf", ".pdf")
        for suf in sufixos:
            for nome in arquivos:
                if nome.endswith(suf):
                    r = sessao.get(f"https://archive.org/download/{item}/{urllib.parse.quote(nome)}", headers=UA, timeout=300)
                    if r.status_code == 200 and (texto or eh_pdf(r)):
                        return r.content
    except (requests.RequestException, ValueError):
        return None
    return None


def baixar(url, sessao, profundidade=0):
    conteudo = archive_org(url, sessao) if profundidade == 0 else None
    if conteudo:
        return conteudo, None
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


def paginas(pdf):
    saida = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", saida, re.M)
    return int(m.group(1)) if m else None


def titulo_curto(fonte):
    autores = fonte.get("autores") or []
    primeiro = autores[0] if autores else ""
    if isinstance(primeiro, dict):
        primeiro = primeiro.get("sobrenome") or primeiro.get("nome") or ""
    primeiro = str(primeiro).strip()
    sobrenome = primeiro.split(",")[0].strip() if "," in primeiro else (primeiro.split() or [""])[-1]
    titulo = (fonte.get("titulo") or "").split(":")[0].strip()
    if len(titulo) > 70:
        titulo = titulo[:67].rstrip() + "…"
    return f"{sobrenome} {fonte.get('ano', '')} — {titulo}".strip(" —")


def carregar_indice(destino):
    arq = destino / "indice.json"
    if arq.exists():
        return {e["source_id"]: e for e in json.loads(arq.read_text(encoding="utf-8"))["itens"]}
    return {}


def gravar_indice(destino, itens):
    ordenados = [itens[k] for k in sorted(itens)]
    (destino / "indice.json").write_text(json.dumps({
        "descricao": "Índice do acervo interno de texto integral das fontes (uso de pesquisa; "
                     "não publicar). Gerado por scripts/baixar_refs.py.",
        "itens": ordenados}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ok = [e for e in ordenados if e["status"] == "ok"]
    linhas = [
        "# Índice do acervo",
        "",
        "> Gerado por `scripts/baixar_refs.py` a partir de `indice.json`. Uso interno de pesquisa: "
        "ver [`LEIAME.md`](LEIAME.md). Não editar à mão.",
        "",
        f"**{len(ok)}** fontes com texto · **{sum(1 for e in ordenados if e['status'] == 'repetido')}** "
        f"com o mesmo PDF de outra · **{sum(1 for e in ordenados if e['status'] == 'falhou')}** sem download "
        f"· {sum(e.get('bytes') or 0 for e in ok) / 1e6:.1f} MB de PDF.",
        "",
        "| source_id | título curto | páginas | palavras | baixado em | origem | acesso |",
        "|---|---|---|---|---|---|---|",
    ]
    for e in ordenados:
        origem = f"[link]({e['url_origem']})" if e.get("url_origem") else "—"
        linhas.append(f"| `{e['source_id']}` | {e.get('titulo_curto', '').replace('|', '/')} | "
                      f"{e.get('paginas') or '—'} | {e.get('palavras') or '—'} | {e.get('baixado_em') or '—'} | "
                      f"{origem} | {e.get('acesso', '').replace('|', '/')} |")
    (destino / "INDICE.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--destino", default=str(acervo_padrao()))
    ap.add_argument("--ids", default="")
    ap.add_argument("--so-converter", action="store_true")
    ap.add_argument("--reconverter", action="store_true", help="reconverte .txt já existentes")
    a = ap.parse_args()
    destino = Path(a.destino).resolve()
    print(f"acervo: {destino}")
    if (RAIZ in destino.parents or destino == RAIZ) and destino != ACERVO.resolve():
        sys.exit("Dentro do repositório, o único destino permitido é acervo/.")
    pdfs, txts = destino / "pdf", destino / "txt"
    pdfs.mkdir(parents=True, exist_ok=True)
    txts.mkdir(parents=True, exist_ok=True)

    catalogo = {f["id"]: f for f in json.loads((RAIZ / "data/fontes/catalogo.json").read_text(encoding="utf-8"))["fontes"]}
    arq_extras = ACERVO / "urls_extras.json"
    extras = json.loads(arq_extras.read_text(encoding="utf-8"))["urls"] if arq_extras.exists() else {}
    usadas, vias = fontes_usadas()
    ids = sorted(a.ids.split(",")) if a.ids else sorted(usadas | set(extras))
    # a fonte efetivamente lida (via) vem antes da fonte de 2ª mão, que costuma
    # apontar para o mesmo PDF; PDF repetido não gera segundo .txt
    ids.sort(key=lambda i: i not in vias)
    indice = carregar_indice(destino)
    hoje = datetime.date.today().isoformat()
    sessao = requests.Session()
    falhas, hashes, repetidos = [], {}, []
    for i in ids:
        fonte = catalogo.get(i, {})
        pdf, txt = pdfs / f"{i}.pdf", txts / f"{i}.txt"
        ent = indice.get(i, {"source_id": i})
        ent["titulo_curto"] = titulo_curto(fonte) if fonte else i
        local = ACERVO / "pdf" / f"{i}.pdf"
        if not pdf.exists() and destino != ACERVO.resolve() and local.exists():
            pdf.write_bytes(local.read_bytes())  # já baixado antes no acervo local
        if not pdf.exists() and not a.so_converter:
            erros = []
            for u in candidatos(fonte, extras.get(i, [])):
                conteudo, erro = baixar(u, sessao)
                if not conteudo and (u.lower().endswith(".pdf") or "/file/" in u or u.endswith("/document")):
                    conteudo = baixar_curl(u)
                    erro = erro if not conteudo else None
                if conteudo:
                    pdf.write_bytes(conteudo)
                    ent.update(url_origem=u, baixado_em=hoje, acesso="download direto (acesso aberto)")
                    break
                erros.append(erro)
            if not pdf.exists():
                motivo = "; ".join(e for e in erros if e) or "sem url/evidencias no catálogo"
                falhas.append((i, motivo))
                ent.update(status="falhou", acesso=motivo[:300],
                           url_origem=ent.get("url_origem") or fonte.get("url") or "")
                indice[i] = ent
                continue
        if not pdf.exists():
            continue
        dados = pdf.read_bytes()
        h = hashlib.sha256(dados).hexdigest()
        ent.update(arquivo_pdf=f"pdf/{pdf.name}", sha256=h, bytes=len(dados), paginas=paginas(pdf))
        ent.setdefault("baixado_em", hoje)
        ent.setdefault("acesso", "PDF salvo à mão em acervo/pdf/")
        if h in hashes:
            txt.unlink(missing_ok=True)
            repetidos.append((i, hashes[h]))
            ent.update(status="repetido", arquivo_txt=f"txt/{hashes[h]}.txt",
                       acesso=f"mesmo PDF que {hashes[h]} (fonte citada de 2ª mão)")
            indice[i] = ent
            continue
        hashes[h] = i
        if txt.exists() and not a.reconverter and ent.get("palavras"):
            n = ent["palavras"]
        else:
            n = converter(pdf, txt)
        ent.update(palavras=n, arquivo_txt=f"txt/{txt.name}", status="ok")
        if n >= 1000:
            print(f"ok  {i}: {n} palavras")
        if n < 1000:
            # PDF digitalizado sem OCR: tenta o OCR do Internet Archive para o mesmo item
            for u in candidatos(fonte, extras.get(i, [])):
                ocr = archive_org(u, sessao, texto=True)
                if ocr and len(ocr.split()) >= 1000:
                    txt.write_text(HIFEN.sub(r"\1\2", ocr.decode("utf-8", "ignore")), encoding="utf-8")
                    n = len(ocr.split())
                    print(f"ok  {i}: {n} palavras (OCR do Internet Archive)")
                    ent.update(palavras=n, arquivo_txt=f"txt/{txt.name}", status="ok",
                               acesso="PDF sem camada de texto; texto = OCR (_djvu.txt) do Internet Archive")
                    break
        if n < 1000:
            txt.unlink(missing_ok=True)
            ent.update(status="sem_texto", arquivo_txt=None,
                       acesso=f"PDF sem texto extraível ({n} palavras; imagem sem OCR?)")
            falhas.append((i, ent["acesso"]))
        indice[i] = ent
    gravar_indice(destino, indice)
    for i, j in repetidos:
        print(f"=   {i}: mesmo PDF que {j} (fonte citada de 2ª mão); comparada via {j}.txt")
    print(f"\n{len(ids) - len(falhas) - len(repetidos)}/{len(ids)} fontes com texto próprio em {txts}")
    if falhas:
        print("\nNão baixadas (registrar em docs/pesquisa/PENDENCIAS.md se ainda não estiverem):")
        for i, motivo in falhas:
            print(f" - {i}: {motivo}")


if __name__ == "__main__":
    main()
