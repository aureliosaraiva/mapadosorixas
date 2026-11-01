#!/usr/bin/env python3
"""Coleta automatizada de metadados bibliográficos (varredura nº 3).

Roda cada consulta de `scripts/coleta/consultas.json` em cada base e grava a
saída bruta normalizada em `data/fontes/coleta/<data>/<base>.json`, com a
contagem de resultados por consulta (`total` informado pela base e `n`
itens efetivamente baixados).

Bases:
  crossref    api.crossref.org/works (query.bibliographic)
  openlibrary openlibrary.org/search.json
  thesesfr    theses.fr/api/v1/theses/recherche
  hal         api.archives-ouvertes.fr/search
  doaj        doaj.org/api/search/articles
  bdtd        bdtd.ibict.br/vufind/api/v1/search (VuFind)
  openalex    api.openalex.org/works (só com OPENALEX_API_KEY ou se não der 429)

Uso:
  python3 scripts/coleta/coletar.py [--bases crossref,openlibrary] [--data 2026-10-31]
                                    [--linhas 20] [--consultas exu-pt-1,ogum-pt-1]

Variáveis de ambiente opcionais:
  COLETA_MAILTO      e-mail para o "polite pool" do Crossref/OpenAlex
  OPENALEX_API_KEY   chave gratuita do OpenAlex

Resumos (abstracts) NÃO são gravados: são texto de terceiros. Guardamos só os
termos de pertinência encontrados neles (`termos_resumo`).
"""
import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pertinencia import termos_encontrados  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
CONSULTAS = Path(__file__).resolve().parent / "consultas.json"
SAIDA = RAIZ / "data" / "fontes" / "coleta"
UA = "mapadosorixas-coleta/1.0 (https://github.com/aureliosaraiva/mapadosorixas)"
MAILTO = os.environ.get("COLETA_MAILTO", "")


class Bloqueado(Exception):
    """Base inacessível (HTTP 4xx/5xx persistente ou erro de rede)."""


def get_json(url, tentativas=4, espera=2.0, headers=None):
    h = {"User-Agent": UA + (f" mailto:{MAILTO}" if MAILTO else ""), "Accept": "application/json"}
    h.update(headers or {})
    ultimo = None
    for i in range(tentativas):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            corpo = e.read()[:300].decode("utf-8", "replace")
            ultimo = f"HTTP {e.code}: {corpo}"
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(espera * (2 ** i))
                continue
            raise Bloqueado(ultimo)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            ultimo = f"rede: {e}"
            time.sleep(espera * (2 ** i))
        except json.JSONDecodeError as e:
            raise Bloqueado(f"resposta não-JSON: {e}")
    raise Bloqueado(ultimo)


def item(base, id_base, titulo, autores, ano, tipo, url, **extra):
    d = {
        "base": base,
        "id_base": id_base,
        "titulo": (titulo or "").strip(),
        "autores": [a for a in (autores or []) if a],
        "ano": ano,
        "tipo_base": tipo,
        "url": url,
        "doi": None,
        "isbn": [],
        "idioma": None,
        "periodico": None,
        "editora": None,
        "assuntos": [],
        "acesso_aberto": None,
    }
    d.update({k: v for k, v in extra.items() if k != "resumo"})
    resumo = extra.get("resumo") or ""
    d["termos_titulo"] = termos_encontrados(d["titulo"] + " " + " ".join(d["assuntos"]))
    d["termos_resumo"] = termos_encontrados(resumo)
    return d


def ano_de(s):
    try:
        return int(str(s)[:4])
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------- bases

def crossref(q, n):
    p = {"query.bibliographic": q, "rows": n,
         "select": "DOI,title,subtitle,author,issued,type,container-title,publisher,ISBN,subject,URL,abstract"}
    if MAILTO:
        p["mailto"] = MAILTO
    d = get_json("https://api.crossref.org/works?" + urllib.parse.urlencode(p))
    msg = d["message"]
    out = []
    for w in msg.get("items", []):
        autores = [" ".join(x for x in (a.get("given"), a.get("family")) if x) or a.get("name", "") for a in w.get("author", [])]
        ano = None
        dp = (w.get("issued") or {}).get("date-parts") or [[None]]
        ano = dp[0][0] if dp and dp[0] else None
        titulo = " ".join(w.get("title") or [])
        sub = " ".join(w.get("subtitle") or [])
        if sub and sub.lower() not in titulo.lower():
            titulo = f"{titulo.rstrip(': ')}: {sub}"
        out.append(item("crossref", w.get("DOI"), titulo, autores, ano, w.get("type"),
                        f"https://doi.org/{w['DOI']}" if w.get("DOI") else w.get("URL"),
                        doi=(w.get("DOI") or "").lower() or None, isbn=w.get("ISBN", []),
                        idioma=w.get("language"), periodico=" ".join(w.get("container-title") or []) or None,
                        editora=w.get("publisher"), assuntos=w.get("subject", []), resumo=w.get("abstract")))
    return msg.get("total-results"), out


def openlibrary(q, n):
    p = {"q": q, "limit": n,
         "fields": "key,title,subtitle,author_name,first_publish_year,isbn,publisher,language,subject,ebook_access"}
    d = get_json("https://openlibrary.org/search.json?" + urllib.parse.urlencode(p))
    out = []
    for w in d.get("docs", []):
        t = w.get("title", "") + (f": {w['subtitle']}" if w.get("subtitle") else "")
        out.append(item("openlibrary", w.get("key"), t, w.get("author_name", []), w.get("first_publish_year"), "book",
                        f"https://openlibrary.org{w['key']}", isbn=(w.get("isbn") or [])[:6],
                        idioma=",".join(w.get("language", [])[:3]) or None,
                        editora=(w.get("publisher") or [None])[0], assuntos=(w.get("subject") or [])[:15],
                        acesso_aberto=w.get("ebook_access") in ("public", "borrowable")))
    return d.get("numFound"), out


def thesesfr(q, n):
    p = {"q": q, "nombre": n, "debut": 0}
    d = get_json("https://theses.fr/api/v1/theses/recherche/?" + urllib.parse.urlencode(p))
    out = []
    for t in d.get("theses", []):
        autores = [f"{a.get('prenom', '')} {a.get('nom', '')}".strip() for a in t.get("auteurs", [])]
        assuntos = [s.get("libelle", "") for s in t.get("sujetsRameau", [])] + \
                   [s.get("libelle", "") if isinstance(s, dict) else str(s) for s in t.get("sujets", [])]
        out.append(item("thesesfr", t.get("id"), t.get("titrePrincipal"), autores, ano_de((t.get("dateSoutenance") or "")[-4:]),
                        f"these ({t.get('status')})", f"https://theses.fr/{t.get('id')}",
                        doi=t.get("doi"), editora=t.get("etabSoutenanceN"), periodico=t.get("discipline"),
                        assuntos=assuntos[:15]))
    return d.get("totalHits"), out


def hal(q, n):
    p = {"q": q, "wt": "json", "rows": n,
         "fl": "halId_s,title_s,authFullName_s,producedDateY_i,docType_s,doiId_s,isbn_s,language_s,journalTitle_s,publisher_s,keyword_s,uri_s,openAccess_bool,abstract_s"}
    d = get_json("https://api.archives-ouvertes.fr/search/?" + urllib.parse.urlencode(p))
    r = d["response"]
    out = []
    for w in r.get("docs", []):
        isbn = w.get("isbn_s")
        out.append(item("hal", w.get("halId_s"), " ".join((w.get("title_s") or [])[:1]), w.get("authFullName_s", []),
                        w.get("producedDateY_i"), w.get("docType_s"), w.get("uri_s"),
                        doi=(w.get("doiId_s") or "").lower() or None, isbn=[isbn] if isinstance(isbn, str) else (isbn or []),
                        idioma=",".join(w.get("language_s", [])) or None, periodico=w.get("journalTitle_s"),
                        editora=", ".join(w.get("publisher_s", [])) or None, assuntos=(w.get("keyword_s") or [])[:15],
                        acesso_aberto=w.get("openAccess_bool"), resumo=" ".join(w.get("abstract_s") or [])))
    return r.get("numFound"), out


def doaj(q, n):
    url = "https://doaj.org/api/search/articles/" + urllib.parse.quote(q) + "?" + urllib.parse.urlencode({"pageSize": n})
    d = get_json(url)
    out = []
    for r in d.get("results", []):
        b = r.get("bibjson", {})
        doi = next((i.get("id") for i in b.get("identifier", []) if i.get("type", "").lower() == "doi"), None)
        link = next((lk.get("url") for lk in b.get("link", []) if lk.get("type") == "fulltext"), None)
        j = b.get("journal", {})
        out.append(item("doaj", r.get("id"), b.get("title"), [a.get("name") for a in b.get("author", [])],
                        ano_de(b.get("year")), "article", link or (f"https://doi.org/{doi}" if doi else None),
                        doi=(doi or "").lower() or None, idioma=",".join(j.get("language", [])) or None,
                        periodico=j.get("title"), editora=j.get("publisher"),
                        assuntos=(b.get("keywords") or [])[:15], acesso_aberto=True, resumo=b.get("abstract")))
    return d.get("total"), out


def bdtd(q, n):
    p = [("lookfor", q), ("type", "AllFields"), ("limit", n)] + \
        [("field[]", f) for f in ("id", "title", "authors", "publicationDates", "formats", "urls", "institutions")]
    d = get_json("https://bdtd.ibict.br/vufind/api/v1/search?" + urllib.parse.urlencode(p), tentativas=2)
    if d.get("status") != "OK":
        raise Bloqueado(str(d)[:200])
    out = []
    for r in d.get("records", []):
        aut = [a for grp in (r.get("authors") or {}).values() for a in (grp if isinstance(grp, list) else list(grp))]
        out.append(item("bdtd", r.get("id"), r.get("title"), aut, ano_de((r.get("publicationDates") or [None])[0]),
                        ",".join(r.get("formats", [])), f"https://bdtd.ibict.br/vufind/Record/{r.get('id')}",
                        editora=", ".join(r.get("institutions", [])) or None))
    return d.get("resultCount"), out


def openalex(q, n):
    p = {"search": q, "per-page": n}
    if MAILTO:
        p["mailto"] = MAILTO
    if os.environ.get("OPENALEX_API_KEY"):
        p["api_key"] = os.environ["OPENALEX_API_KEY"]
    d = get_json("https://api.openalex.org/works?" + urllib.parse.urlencode(p), tentativas=2)
    out = []
    for w in d.get("results", []):
        src = ((w.get("primary_location") or {}).get("source") or {})
        out.append(item("openalex", w.get("id"), w.get("display_name"),
                        [a["author"]["display_name"] for a in w.get("authorships", [])], w.get("publication_year"),
                        w.get("type"), w.get("doi") or w.get("id"),
                        doi=(w.get("doi") or "").replace("https://doi.org/", "").lower() or None,
                        idioma=w.get("language"), periodico=src.get("display_name"),
                        acesso_aberto=(w.get("open_access") or {}).get("is_oa")))
    return d.get("meta", {}).get("count"), out


BASES = {"crossref": (crossref, 1.0), "openlibrary": (openlibrary, 1.2), "thesesfr": (thesesfr, 0.6),
         "hal": (hal, 0.6), "doaj": (doaj, 0.8), "bdtd": (bdtd, 1.0), "openalex": (openalex, 1.0)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bases", default=",".join(BASES))
    ap.add_argument("--data", default=dt.date.today().isoformat())
    ap.add_argument("--linhas", type=int, default=20)
    ap.add_argument("--consultas", default="")
    a = ap.parse_args()

    consultas = json.loads(CONSULTAS.read_text(encoding="utf-8"))["consultas"]
    if a.consultas:
        sel = set(a.consultas.split(","))
        consultas = [c for c in consultas if c["id"] in sel]
    pasta = SAIDA / a.data
    pasta.mkdir(parents=True, exist_ok=True)

    for nome in a.bases.split(","):
        fn, pausa = BASES[nome]
        res = {"base": nome, "data": a.data, "linhas_por_consulta": a.linhas,
               "gerado_por": "scripts/coleta/coletar.py", "status": "ok", "erro": None, "consultas": []}
        falhas_seguidas = 0
        for c in consultas:
            reg = dict(c, status="ok", erro=None, total=None, n=0, itens=[])
            if falhas_seguidas >= 3:
                reg.update(status="nao_executada", erro="base bloqueada nas 3 consultas anteriores")
                res["consultas"].append(reg)
                continue
            try:
                total, itens = fn(c["q"], a.linhas)
                reg.update(total=total, n=len(itens), itens=itens)
                falhas_seguidas = 0
            except Bloqueado as e:
                reg.update(status="erro", erro=str(e)[:300])
                falhas_seguidas += 1
            res["consultas"].append(reg)
            print(f"{nome:12} {c['id']:16} {reg['status']:6} total={reg['total']} n={reg['n']}", flush=True)
            time.sleep(pausa)
        execs = [c for c in res["consultas"] if c["status"] == "ok"]
        if not execs:
            res["status"] = "bloqueada"
            res["erro"] = next((c["erro"] for c in res["consultas"] if c["erro"]), None)
        elif len(execs) < len(res["consultas"]):
            res["status"] = "parcial"
        (pasta / f"{nome}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"== {nome}: {res['status']} → {pasta / (nome + '.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
