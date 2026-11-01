#!/usr/bin/env python3
"""Aplica `data/fontes/coleta/<data>/triagem.json` ao catálogo.

`triagem.json` (editado à mão, depois de ler `candidatos.json`):

  {
    "decisoes": {
      "<chave do candidato>": {
        "decisao": "entra" | "pista" | "descarta",
        "motivo": "por que entra/descarta",
        "fonte": {                       # só para entra/pista
          "id": "autor-ano-palavra", "tipo": "artigo", "categoria": "academica",
          "tradicoes": ["candomble_ketu"], "confiabilidade_preliminar": "B",
          "idioma": "pt",                # opcional; senão vem da base
          "titulo": "...", "autores": [...], "ano": 2020   # opcionais (correções)
        },
        "justificativa": "por que a confiabilidade é essa"
      }
    },
    "conferencias": {
      "<id já no catálogo>": {"chave": "<chave do grupo em ja_no_catalogo>", "nota": "..."}
    }
  }

`entra` → `status_verificacao: conferido_web` com a URL do registro na API em
`evidencias`. `pista` → `status_verificacao: pista`. `conferencias` promove
uma fonte `a_verificar`/`pista` a `conferido_web` (acrescenta evidência e
identificadores; não muda título nem ano: divergências vão em observações).

Idempotente: ids já existentes não são duplicados.
Uso: python3 scripts/coleta/incorporar.py --data 2026-10-31 [--seco]
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "fontes" / "catalogo.json"
COLETA = RAIZ / "data" / "fontes" / "coleta"
IDIOMAS = {"por": "pt", "eng": "en", "spa": "es", "fre": "fr", "fra": "fr", "ger": "de", "deu": "de",
           "ita": "it", "yor": "yo", "PT": "pt", "EN": "en", "ES": "es", "FR": "fr"}
ORDEM = ["id", "tipo", "categoria", "autores", "titulo", "ano", "idioma", "tradicoes",
         "confiabilidade_preliminar", "observacoes", "status_verificacao", "evidencias", "url",
         "identificadores", "periodico", "editora", "local"]


RODADAS = {"2026-10-31": "Varredura 3", "2026-11-01": "Varredura 4"}
ROTULO = "Varredura 3"
UA = "mapadosorixas-coleta/1.0 (https://github.com/aureliosaraiva/mapadosorixas)"
AUTOPUB = re.compile(r"independently|createspace|lulu|llewellyn|original pub|madras|\beco\b|espiritualista|"
                     r"inner traditions|destiny books|weiser|xlibris|palibrio|oshun publications|panapo|prophet|"
                     r"autografia|athelia|caliope|crossing press|orunmila|shinseken|namast", re.I)
RESENHA = re.compile(r"\bresenha\b|review|reseña|compte[- ]rendu|rezension|\(\w[\w ]* (university )?press|"
                     r"\d+ p\.$", re.I)
NAO_BIB = {"component", "dataset", "IMG", "BLOG", "VIDEO", "other", "OTHER", "NOTICE", "UNDEFINED",
           "posted-content", "reference-entry"}


def limpa_titulo(t):
    t = html.unescape(html.unescape(t or ""))
    t = re.sub(r"<sup>.*?</sup>", "", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"\s*DOI:.*$", "", t)
    t = re.split(r"\s=\s", t)[0]
    return re.sub(r"\s+", " ", t).strip()


def crossref(doi, tentativas=5):
    """Confere o DOI no Crossref. Devolve o registro, None se 404, ou levanta erro se a API não responder."""
    for i in range(tentativas):
        try:
            req = urllib.request.Request(f"https://api.crossref.org/works/{doi}", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))["message"]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(3 * 2 ** i)
        except (urllib.error.URLError, TimeoutError):
            time.sleep(3 * 2 ** i)
    raise RuntimeError(f"Crossref não respondeu para {doi}")


def motivo_auto(c, fontes_chave):
    """Motivo de não incorporação para candidatos sem decisão manual."""
    if c["tipo_base"] in NAO_BIB:
        return "tipo não bibliográfico (componente, verbete de dicionário, vídeo, dataset etc.)"
    if RESENHA.search(c["titulo"]):
        return "resenha de livro"
    if AUTOPUB.search(c.get("editora") or ""):
        return "autopublicação ou editora esotérica/de divulgação comercial"
    if c["tipo_base"] == "book-chapter" and any(fc and fc in (c.get("periodico") or "").lower() for fc in fontes_chave):
        return "capítulo de obra já catalogada ou incorporada"
    return "pertinente, mas periférico ao recorte desta rodada (literatura, artes, educação, saúde, turismo, " \
           "tema geral) ou sem foco nos 5 orixás e tradições-alvo; fica em candidatos.json para rodadas futuras"


def evidencia_api(c):
    """URL do registro na base idônea (de preferência a API/registro, não o buscador)."""
    ev = []
    if c.get("doi"):
        ev.append(f"https://api.crossref.org/works/{c['doi']}")
    for u in c.get("urls", []):
        if any(h in u for h in ("openlibrary.org", "theses.fr", "hal.science", "archives-ouvertes", "doi.org")) \
                or "doaj" in c["bases"]:
            ev.append(u)
    return list(dict.fromkeys(ev))


PALAVRAS = {
    "pt": "o os a as um uma do da dos das no na nos nas em com para por sobre entre e não ao à como seus suas".split(),
    "es": "el los la las un una del de en con para por sobre entre y al su sus como".split(),
    "fr": "le les la un une des du de en avec pour par sur entre et au aux dans à l d".split(),
    "en": "the of and in on for with from to an a its their between".split(),
    "de": "der die das und im in ein eine von zu mit den des".split(),
    "it": "il lo gli la le di del della e nel con per tra".split(),
}
SINAIS = {"pt": r"ção|ções|ã|õ|ê", "es": r"ción|ñ|¿|¡", "fr": r"è|ç(?!ão)|œ|eaux?\b", "de": r"ß|ü|ä|ö"}


def detecta_idioma(t):
    pal = re.findall(r"[\wÀ-ÿ']+", t.lower().replace("’", "'"))
    pal = [w for p in pal for w in p.split("'")]
    pts = {k: sum(w in v for w in pal) for k, v in PALAVRAS.items()}
    for k, rx in SINAIS.items():
        pts[k] += 2 * len(re.findall(rx, t.lower()))
    melhor = max(pts, key=pts.get)
    return melhor if pts[melhor] > 0 else None


def idioma(c, f, titulo):
    if f.get("idioma"):
        return f["idioma"]
    i = (c.get("idioma") or "").split(",")
    if len(i) == 1 and i[0] and IDIOMAS.get(i[0]) and c["bases"] == ["openlibrary"]:
        return IDIOMAS[i[0]]  # Open Library informa o idioma da edição
    return detecta_idioma(titulo) or IDIOMAS.get(i[0], "pt")


def montar(c, dec, status):
    f = dec["fonte"]
    ident = {}
    if c.get("doi"):
        ident["doi"] = c["doi"]
    if c.get("isbn"):
        ident["isbn"] = c["isbn"][0]
    obs = f"{ROTULO} (coleta por API: {', '.join(c['bases'])}). " \
          f"Confiabilidade {f['confiabilidade_preliminar']}: {dec['justificativa']}"
    if dec.get("motivo"):
        obs += f" Pertinência: {dec['motivo']}"
    if status == "pista":
        obs = "PISTA — " + obs
    reg = {
        "id": f["id"], "tipo": f["tipo"], "categoria": f["categoria"],
        "autores": f.get("autores") or c["autores"] or ["(autor a conferir)"],
        "titulo": limpa_titulo(f.get("titulo") or c["titulo"]), "ano": f.get("ano", c["ano"]),
        "idioma": idioma(c, f, limpa_titulo(f.get("titulo") or c["titulo"])), "tradicoes": f["tradicoes"],
        "confiabilidade_preliminar": f["confiabilidade_preliminar"], "observacoes": obs,
        "status_verificacao": status, "evidencias": evidencia_api(c),
        "url": f.get("url") or (next((u for u in c["urls"] if "openlibrary" not in u), None)
                                if c.get("acesso_aberto") else None),
        "identificadores": ident,
    }
    if c.get("tipo_base") in ("journal-article", "article", "ART") and c.get("periodico"):
        reg["periodico"] = c["periodico"]
    elif c.get("editora") and f["tipo"] in ("livro", "tese", "dissertacao"):
        reg["editora"] = c["editora"]
    for k in ("editora", "local", "periodico"):
        if f.get(k):
            reg[k] = f[k]
    return {k: reg[k] for k in ORDEM if k in reg}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--seco", action="store_true")
    ap.add_argument("--sem-crossref", action="store_true", help="não reconsulta o Crossref (subtítulos/DOI)")
    a = ap.parse_args()
    global ROTULO
    ROTULO = RODADAS.get(a.data, f"Coleta de {a.data}")
    pasta = COLETA / a.data
    cand = json.loads((pasta / "candidatos.json").read_text(encoding="utf-8"))
    tri = json.loads((pasta / "triagem.json").read_text(encoding="utf-8"))
    por_chave = {c["chave"]: c for c in cand["candidatos"] + cand["ja_no_catalogo"]}

    doc = json.loads(CATALOGO.read_text(encoding="utf-8"))
    fontes = doc["fontes"]
    ids = {f["id"] for f in fontes}
    novos, conf, faltando = [], [], []

    for chave, dec in tri.get("decisoes", {}).items():
        if dec["decisao"] == "descarta":
            continue
        c = por_chave.get(chave)
        if not c:
            faltando.append(chave)
            continue
        status = "conferido_web" if dec["decisao"] == "entra" else "pista"
        reg = montar(c, dec, status)
        if reg["id"] in ids:
            continue
        if reg["identificadores"].get("doi") and not a.sem_crossref:
            m = crossref(reg["identificadores"]["doi"])
            time.sleep(1)
            if m is None:  # DOI não resolve no Crossref (ex.: DOI DataCite do HAL)
                reg["evidencias"] = [e for e in reg["evidencias"] if "api.crossref.org" not in e]
            else:
                sub = " ".join(m.get("subtitle") or [])
                if sub and sub.lower() not in reg["titulo"].lower() and "titulo" not in dec["fonte"]:
                    reg["titulo"] = limpa_titulo(f"{reg['titulo'].rstrip(': ')}: {sub}")
        if status == "conferido_web" and not reg["evidencias"]:
            raise SystemExit(f"{chave}: 'entra' sem evidência de API")
        fontes.append(reg)
        ids.add(reg["id"])
        novos.append(reg["id"])

    por_id = {f["id"]: f for f in fontes}
    for fid, cf in tri.get("conferencias", {}).items():
        f, c = por_id.get(fid), por_chave.get(cf["chave"])
        if not f or not c:
            faltando.append(f"{fid}/{cf['chave']}")
            continue
        ev = evidencia_api(c)
        novas = [e for e in ev if e not in (f.get("evidencias") or [])]
        if f["status_verificacao"] in ("a_verificar", "pista") and ev:
            f["status_verificacao"] = "conferido_web"
            nota = f"Metadados conferidos na {ROTULO.lower()} ({', '.join(c['bases'])})."
            if cf.get("nota"):
                nota += " " + cf["nota"]
            f["observacoes"] = (f.get("observacoes") + " " if f.get("observacoes") else "") + nota
            conf.append(fid)
        f["evidencias"] = (f.get("evidencias") or []) + novas
        f.setdefault("identificadores", {})
        if c.get("doi") and not any("doi" in k for k in f["identificadores"]):
            f["identificadores"]["doi"] = c["doi"]
        if c.get("isbn") and not any("isbn" in k for k in f["identificadores"]) and cf.get("isbn", True):
            f["identificadores"]["isbn"] = c["isbn"][0]

    # resumo da triagem (manual + automática)
    titulos_cat = [t for t in (limpa_titulo(f["titulo"]).lower()[:25] for f in fontes) if len(t) >= 12]
    linhas, cont = [], Counter()
    decs = tri.get("decisoes", {})
    for c in cand["candidatos"]:
        d = decs.get(c["chave"])
        if d:
            dec_, mot = d["decisao"], d.get("motivo") or (d.get("fonte") or {}).get("id")
        else:
            dec_, mot = "nao_incorporado", motivo_auto(c, titulos_cat)
        cont[(dec_, mot if dec_ == "nao_incorporado" else "")] += 1
        linhas.append({"chave": c["chave"], "titulo": c["titulo"][:160], "ano": c["ano"], "decisao": dec_, "motivo": mot})
    resumo = {"gerado_por": "scripts/coleta/incorporar.py",
              "contagem": [{"decisao": k[0], "motivo": k[1], "n": n} for k, n in cont.most_common()],
              "ja_no_catalogo": len(cand["ja_no_catalogo"]),
              "descartados_auto_sem_termo": cand["descartados_auto"]["n"],
              "promovidos_conferido_web": conf, "itens": linhas}
    (pasta / "triagem_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for r in resumo["contagem"]:
        print(f"  {r['n']:4} {r['decisao']} {r['motivo'][:90]}")

    fontes.sort(key=lambda f: f["id"])
    doc["_meta"]["total"] = len(fontes)
    doc["_meta"]["atualizado_em"] = a.data
    print(f"novos: {len(novos)}; promovidos a conferido_web: {len(conf)}; chaves não encontradas: {faltando}")
    if not a.seco:
        CATALOGO.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if faltando else 0


if __name__ == "__main__":
    sys.exit(main())
