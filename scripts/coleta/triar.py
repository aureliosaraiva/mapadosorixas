#!/usr/bin/env python3
"""Deduplica e pré-tria a coleta de uma data (varredura nº 3).

Lê `data/fontes/coleta/<data>/<base>.json`, agrupa itens iguais entre bases
(DOI, ISBN, título normalizado + ano), compara com `data/fontes/catalogo.json`
e grava `data/fontes/coleta/<data>/candidatos.json`:

  - `estatisticas`: contagens por base, por idioma da consulta e por alvo;
  - `ja_no_catalogo`: grupos que casam com fonte já catalogada (com o id);
  - `candidatos`: grupos pertinentes (pontuação ≥ 1) fora do catálogo,
    ordenados por pontuação; cada um com `chave` estável para a triagem;
  - `descartados_auto`: contagem dos grupos com pontuação 0 (sem termo de
    religião afro-diaspórica no título/assuntos/resumo) e uma amostra.

A decisão final (entra / pista / descarta) fica em `triagem.json`, editado à
mão, e é aplicada por `incorporar.py`.

Uso: python3 scripts/coleta/triar.py [--data 2026-10-31]
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pertinencia import norm, pontuacao  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "fontes" / "catalogo.json"
COLETA = RAIZ / "data" / "fontes" / "coleta"
BASES_ARQ = ["crossref", "openlibrary", "thesesfr", "hal", "doaj", "bdtd", "openalex"]


def titulo_norm(t):
    t = norm(t)
    t = re.split(r"\s[:\-–—]\s|:\s|\.\s", t)[0]  # sem subtítulo
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def isbn13(i):
    i = re.sub(r"[^0-9Xx]", "", i or "").upper()
    if len(i) == 13:
        return i
    if len(i) == 10:
        core = "978" + i[:9]
        s = sum(int(c) * (1 if k % 2 == 0 else 3) for k, c in enumerate(core))
        return core + str((10 - s % 10) % 10)
    return None


def chaves(it):
    ks = set()
    if it.get("doi"):
        ks.add("doi:" + it["doi"].lower())
    for i in it.get("isbn") or []:
        x = isbn13(i)
        if x:
            ks.add("isbn:" + x)
    tn = titulo_norm(it.get("titulo", ""))
    if len(tn) >= 8 and it.get("ano"):
        ks.add(f"ta:{tn}|{it['ano']}")
    return ks


def chaves_catalogo(f):
    ks = set()
    for k, v in (f.get("identificadores") or {}).items():
        if "doi" in k:
            ks.add("doi:" + v.lower())
        if "isbn" in k:
            x = isbn13(v)
            if x:
                ks.add("isbn:" + x)
    for e in (f.get("evidencias") or []) + [f.get("url") or ""]:
        m = re.search(r"doi\.org/(10\.[^\s?#]+)", e or "")
        if m:
            ks.add("doi:" + m.group(1).lower())
    tn = titulo_norm(f["titulo"])
    if f.get("ano"):
        ks.add(f"ta:{tn}|{f['ano']}")
    ks.add(f"t:{tn}")
    return ks


class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        self.p[self.find(a)] = self.find(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=dt.date.today().isoformat())
    a = ap.parse_args()
    pasta = COLETA / a.data

    itens, bases_status = [], {}
    est_consulta = []
    for b in BASES_ARQ:
        arq = pasta / f"{b}.json"
        if not arq.exists():
            continue
        d = json.loads(arq.read_text(encoding="utf-8"))
        bases_status[b] = {"status": d["status"], "erro": d.get("erro")}
        for c in d["consultas"]:
            est_consulta.append({"base": b, "consulta": c["id"], "q": c["q"], "idioma": c["idioma"], "alvo": c["alvo"],
                                 "status": c["status"], "total": c["total"], "n": c["n"]})
            for it in c["itens"]:
                it = dict(it, consulta=c["id"], idioma_consulta=c["idioma"], alvo=c["alvo"])
                it["pontuacao"] = pontuacao(it["termos_titulo"], it["termos_resumo"])
                itens.append(it)

    # agrupa
    uf = UF()
    for n, it in enumerate(itens):
        uf.find(n)
        uf.union(n, f"id:{it['base']}:{it['id_base']}")  # mesmo registro em várias consultas
        for k in chaves(it):
            uf.union(n, k)
    grupos = defaultdict(list)
    for n in range(len(itens)):
        grupos[uf.find(n)].append(itens[n])

    # catálogo
    cat = json.loads(CATALOGO.read_text(encoding="utf-8"))["fontes"]
    idx = defaultdict(set)
    for f in cat:
        for k in chaves_catalogo(f):
            idx[k].add(f["id"])

    ja, cands, desc = [], [], []
    for g in grupos.values():
        ks = set().union(*(chaves(it) for it in g))
        ks |= {"t:" + titulo_norm(it["titulo"]) for it in g if len(titulo_norm(it["titulo"])) >= 15}
        ids = set().union(*(idx.get(k, set()) for k in ks))
        forte = {k for k in ks if not k.startswith("t:")}
        ids_fortes = set().union(*(idx.get(k, set()) for k in forte))
        principal = max(g, key=lambda it: (it["pontuacao"], bool(it.get("doi")), len(it.get("autores") or [])))
        resumo = {
            "chave": "c" + hashlib.sha1("|".join(sorted(ks - {k for k in ks if k.startswith("t:")}) or sorted(f"{it['base']}:{it['id_base']}" for it in g)).encode()).hexdigest()[:10],
            "titulo": principal["titulo"], "autores": principal["autores"][:6], "ano": principal["ano"],
            "tipo_base": principal["tipo_base"], "doi": next((it["doi"] for it in g if it.get("doi")), None),
            "isbn": sorted({isbn13(i) for it in g for i in (it.get("isbn") or []) if isbn13(i)})[:4],
            "periodico": next((it["periodico"] for it in g if it.get("periodico")), None),
            "editora": next((it["editora"] for it in g if it.get("editora")), None),
            "idioma": next((it["idioma"] for it in g if it.get("idioma")), None),
            "assuntos": sorted({s for it in g for s in it.get("assuntos", [])})[:12],
            "acesso_aberto": any(it.get("acesso_aberto") for it in g),
            "urls": sorted({it["url"] for it in g if it.get("url")})[:4],
            "bases": sorted({it["base"] for it in g}),
            "consultas": sorted({it["consulta"] for it in g}),
            "alvos": sorted({it["alvo"] for it in g}),
            "termos": sorted({t for it in g for t in it["termos_titulo"] + it["termos_resumo"]}),
            "pontuacao": max(it["pontuacao"] for it in g),
        }
        if ids_fortes or ids:
            resumo["catalogo"] = sorted(ids_fortes or ids)
            resumo["casamento"] = "forte" if ids_fortes else "so_titulo"
            ja.append(resumo)
        elif resumo["pontuacao"] >= 1:
            cands.append(resumo)
        else:
            desc.append(resumo)

    cands.sort(key=lambda r: (-r["pontuacao"], r["alvos"], r["titulo"]))
    por_base = Counter()
    for e in est_consulta:
        por_base[e["base"]] += e["n"]
    est = {
        "bases": bases_status,
        "itens_baixados": len(itens),
        "itens_por_base": dict(por_base),
        "total_informado_por_base_e_idioma": {},
        "grupos_unicos": len(grupos),
        "ja_no_catalogo": len(ja),
        "candidatos": len(cands),
        "descartados_auto_sem_termo": len(desc),
        "consultas": est_consulta,
    }
    tbi = defaultdict(lambda: defaultdict(int))
    for e in est_consulta:
        if e["total"]:
            tbi[e["base"]][e["idioma"]] += int(e["total"])
    est["total_informado_por_base_e_idioma"] = {b: dict(v) for b, v in tbi.items()}

    saida = {"data": a.data, "gerado_por": "scripts/coleta/triar.py", "estatisticas": est,
             "ja_no_catalogo": ja, "candidatos": cands,
             "descartados_auto": {"n": len(desc), "amostra": [d["titulo"] for d in desc[:40]]}}
    (pasta / "candidatos.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(itens)} itens → {len(grupos)} grupos; {len(ja)} já no catálogo; "
          f"{len(cands)} candidatos; {len(desc)} sem termo (descarte automático)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
