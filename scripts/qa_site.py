#!/usr/bin/env python3
"""QA do site gerado (site/dist), depois do `npm run build`.

Confere, sem rede e só com a biblioteca padrão:

1. Conteúdo das fichas HTML contra data/orixas/*.json — TODAS as versões (não só
   amostra): valor, paráfrase, fonte(s), página e registro de cada versão exibida
   correspondem a uma versão da ficha JSON; nenhuma versão da ficha falta no HTML;
   linhas das tabelas de divergência batem com a nota que citam.
2. Nada de pré-fichamento nem de registros retidos (tabus/alimentos) em nenhum
   arquivo publicado (HTML, JSON, TXT): paráfrase, nota e valor (quando o valor
   não coincide com o de um registro publicável). Os ids desses registros só podem
   aparecer na seção "Pendências" das fichas e no campo `pendencias` dos JSON.
3. Selo de rascunho em todas as fichas e `noindex` em todas as páginas.
4. Links internos (href/src) apontam para arquivos existentes e âncoras (#id)
   existentes na página de destino.
5. /dados/: cópias idênticas a data/ (exceto tradicoes.json, que só pode perder
   descrições sem fonte, e LEIAME.txt), com aviso de licença.

Uso: python3 scripts/qa_site.py [--dist site/dist]
Respeita SITE_BASE (o mesmo do build) para resolver links absolutos.
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

RAIZ = Path(__file__).resolve().parent.parent
DATA = RAIZ / "data"
SELO = "Rascunho — aguardando revisão de praticantes e pesquisadores"
VAZIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

erros: list[str] = []


def erro(msg: str) -> None:
    erros.append(msg)


def norm(t: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(t or "")).strip()


# ----------------------------------------------------------------- árvore HTML mínima

class No:
    __slots__ = ("tag", "attrs", "filhos", "pai")

    def __init__(self, tag, attrs, pai):
        self.tag, self.attrs, self.filhos, self.pai = tag, dict(attrs), [], pai

    def texto(self) -> str:
        partes = []
        for f in self.filhos:
            if isinstance(f, str):
                partes.append(f)
            elif f.tag not in ("script", "style"):
                partes.append(f.texto())
        return "".join(partes)

    def classes(self):
        return (self.attrs.get("class") or "").split()

    def todos(self):
        for f in self.filhos:
            if isinstance(f, No):
                yield f
                yield from f.todos()

    def busca(self, tag=None, classe=None, **attrs):
        for n in self.todos():
            if tag and n.tag != tag:
                continue
            if classe and classe not in n.classes():
                continue
            if any(n.attrs.get(k) != v for k, v in attrs.items()):
                continue
            yield n

    def primeiro(self, *a, **k):
        return next(self.busca(*a, **k), None)

    def dentro_de(self, pred) -> bool:
        p = self.pai
        while p is not None:
            if pred(p):
                return True
            p = p.pai
        return False


class Arvore(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raiz = No("#doc", {}, None)
        self.atual = self.raiz

    def handle_starttag(self, tag, attrs):
        n = No(tag, attrs, self.atual)
        self.atual.filhos.append(n)
        if tag not in VAZIOS:
            self.atual = n

    def handle_startendtag(self, tag, attrs):
        self.atual.filhos.append(No(tag, attrs, self.atual))

    def handle_endtag(self, tag):
        p = self.atual
        while p is not None and p.tag != tag:
            p = p.pai
        if p is not None and p.pai is not None:
            self.atual = p.pai

    def handle_data(self, data):
        self.atual.filhos.append(data)


def parse(caminho: Path) -> No:
    a = Arvore()
    a.feed(caminho.read_text(encoding="utf-8"))
    return a.raiz


# ----------------------------------------------------------------- dados

def carregar():
    fichas = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted((DATA / "orixas").glob("*.json"))}
    fontes = {f["id"]: f for f in json.loads((DATA / "fontes" / "catalogo.json").read_text(encoding="utf-8"))["fontes"]}
    registros = []
    for p in sorted((DATA / "fichamento").glob("*.json")):
        if p.name != "divergencias.json":
            registros += json.loads(p.read_text(encoding="utf-8"))["registros"]
    return fichas, fontes, registros


# ----------------------------------------------------------------- 1 e 3: fichas

def conferir_fichas(dist: Path, fichas: dict, fontes: dict) -> int:
    conferidas = 0
    for oid, ficha in fichas.items():
        arq = dist / "orixas" / oid / "index.html"
        if not arq.exists():
            erro(f"[ficha] {oid}: página {arq.relative_to(dist)} não foi gerada")
            continue
        doc = parse(arq)
        selo = doc.primeiro("p", "selo")
        if selo is None or SELO not in norm(selo.texto()):
            erro(f"[selo] {oid}: selo de rascunho ausente")

        esperadas = {v["registro"]: (a, v) for a, vs in ficha["atributos"].items() for v in vs}
        notas = {}
        for li in doc.busca("li"):
            m = re.fullmatch(r"nota-(\d+)", li.attrs.get("id", ""))
            if m:
                notas[int(m.group(1))] = li

        vistas = set()
        for li in doc.busca("li", "versao"):
            reg = li.attrs.get("id", "")[2:]
            if reg not in esperadas:
                erro(f"[versão] {oid}: versão exibida '{reg}' não existe em data/orixas/{oid}.json")
                continue
            if reg in vistas:
                erro(f"[versão] {oid}: versão '{reg}' exibida mais de uma vez")
            vistas.add(reg)
            atributo, v = esperadas[reg]
            # a versão precisa estar na seção do seu atributo
            secao = li.pai.pai if li.pai is not None else None
            h2 = secao.primeiro("h2") if secao is not None else None
            if h2 is None or h2.attrs.get("id") != atributo:
                erro(f"[versão] {oid}/{reg}: exibida fora da seção '{atributo}'")
            valor = li.primeiro("span", "valor")
            if valor is None or norm(valor.texto()) != norm(v["valor"]):
                erro(f"[versão] {oid}/{reg}: valor difere do JSON")
            ps = [norm(p.texto()) for p in li.busca("p") if "nota" not in p.classes()]
            if norm(v["parafrase"]) not in ps:
                erro(f"[versão] {oid}/{reg}: paráfrase difere do JSON")
            nota_fich = li.primeiro("p", "nota")
            if (v.get("nota") or None) and (nota_fich is None or norm(v["nota"]) not in norm(nota_fich.texto())):
                erro(f"[versão] {oid}/{reg}: nota do fichamento ausente ou diferente")
            ref = li.primeiro("a")
            m = re.fullmatch(r"#nota-(\d+)", (ref.attrs.get("href") if ref else "") or "")
            if not m or int(m.group(1)) not in notas:
                erro(f"[versão] {oid}/{reg}: chamada de nota quebrada")
                continue
            nota = notas[int(m.group(1))]
            txt = norm(nota.texto())
            code = nota.primeiro("code")
            if code is None or norm(code.texto()) != reg:
                erro(f"[nota] {oid}/{reg}: a nota {m.group(1)} cita outro registro")
            links = {a.attrs.get("href", "").split("#fonte-")[-1] for a in nota.busca("a") if "#fonte-" in a.attrs.get("href", "")}
            for s in v["sources"]:
                if s["id"] not in links:
                    erro(f"[nota] {oid}/{reg}: fonte {s['id']} não aparece na nota")
                if s.get("via") and s["via"] not in links:
                    erro(f"[nota] {oid}/{reg}: fonte intermediária {s['via']} não aparece na nota")
                if norm(s["loc"]) not in txt:
                    erro(f"[nota] {oid}/{reg}: página '{s['loc']}' não aparece na nota")
                f = fontes.get(s["id"])
                if f is None:
                    erro(f"[nota] {oid}/{reg}: fonte {s['id']} fora do catálogo")
                elif str(f.get("ano") or "s.d.") not in txt:
                    erro(f"[nota] {oid}/{reg}: ano da fonte {s['id']} não aparece na nota")
            conferidas += 1

        for reg in sorted(set(esperadas) - vistas):
            erro(f"[versão] {oid}: versão '{reg}' do JSON não aparece no HTML")
        # tabus e alimentos retidos: a seção não pode existir se o JSON não a tem
        for a in ficha["pendencias"].get("retidos_ate_conselho", {}):
            if a not in ficha["atributos"] and doc.primeiro("h2", id=a) is not None:
                erro(f"[retido] {oid}: seção '{a}' exibida, mas os registros estão retidos")

        # tabelas de divergência: cada linha cita uma nota; valor e página precisam bater
        sec = doc.primeiro("section", **{"aria-labelledby": "divergencias"})
        for tr in (sec.busca("tr") if sec else []):
            tds = [c for c in tr.filhos if isinstance(c, No) and c.tag == "td"]
            if not tds:
                continue
            a = tds[-1].primeiro("a")
            m = re.fullmatch(r"#nota-(\d+)", (a.attrs.get("href") if a else "") or "")
            if not m or int(m.group(1)) not in notas:
                erro(f"[divergência] {oid}: linha '{norm(tds[0].texto())[:40]}' sem nota válida")
                continue
            reg = norm(notas[int(m.group(1))].primeiro("code").texto())
            _, v = esperadas.get(reg, (None, None))
            if v is None or norm(tds[0].texto()) != norm(v["valor"]) or norm(v["localizacao"]) not in norm(tds[-1].texto()):
                erro(f"[divergência] {oid}: linha '{norm(tds[0].texto())[:40]}' não corresponde ao registro {reg}")
    return conferidas


# ----------------------------------------------------------------- 2: proibidos

def conferir_proibidos(dist: Path, fichas: dict, registros: list) -> int:
    retidos = {r for f in fichas.values() for ids in f["pendencias"].get("retidos_ate_conselho", {}).values() for r in ids}
    proibidos = [r for r in registros if r["status"] == "pre_fichamento" or r["id"] in retidos]
    valores_publicos = {norm(r["valor"]) for r in registros if r["status"] in ("fichado", "revisado") and r["id"] not in retidos}
    textos = {}
    for p in dist.rglob("*"):
        if p.suffix in (".html", ".json", ".txt") and "pagefind" not in p.parts:
            bruto = p.read_text(encoding="utf-8")
            if p.suffix == ".json":
                # junta todos os textos do JSON, sem o bloco `pendencias` (que só lista ids)
                def walk(x, chave=None):
                    if chave == "pendencias":
                        return []
                    if isinstance(x, dict):
                        return [t for k, v in x.items() for t in walk(v, k)]
                    if isinstance(x, list):
                        return [t for v in x for t in walk(v)]
                    return [str(x)] if isinstance(x, str) else []
                textos[p] = (norm(" ¦ ".join(walk(json.loads(bruto)))), bruto)
            else:
                textos[p] = (norm(re.sub(r"<[^>]+>", " ", bruto)), bruto)

    for r in proibidos:
        tipo = "retido" if r["id"] in retidos else "pre_fichamento"
        trechos = [norm(r.get("parafrase", "")), norm(r.get("nota") or "")]
        valor = norm(r["valor"]) if norm(r["valor"]) not in valores_publicos else ""
        for p, (txt, bruto) in textos.items():
            rel = p.relative_to(dist)
            # o valor é curto e pode coincidir com metadados bibliográficos: só é
            # procurado onde há conteúdo de fichas (não no catálogo de fontes)
            com_valor = trechos + ([valor] if valor and "fontes" not in rel.parts and rel.name != "fontes.json" else [])
            for t in filter(None, com_valor):
                if len(t) >= 12 and t in txt:
                    erro(f"[{tipo}] {r['id']}: texto do registro aparece em {rel}: '{t[:50]}…'")
            # o id só pode aparecer como lista de pendências
            if p.suffix == ".html" and re.search(rf'id="v-{re.escape(r["id"])}"|<code>{re.escape(r["id"])}</code>', bruto):
                erro(f"[{tipo}] {r['id']}: exibido como versão/nota em {rel}")
            if p.suffix == ".html" and r["id"] in bruto:
                doc_ok = any(r["id"] in norm(s.texto()) for s in parse(p).busca("section", **{"aria-labelledby": "pendencias"}))
                fora = bruto.count(r["id"]) - (bruto.split('aria-labelledby="pendencias"', 1)[-1].split("</section>", 1)[0].count(r["id"]) if doc_ok else 0)
                if fora > 0:
                    erro(f"[{tipo}] {r['id']}: id aparece fora da seção Pendências em {rel}")
    return len(proibidos)


# ----------------------------------------------------------------- 3 e 4: páginas e links

def conferir_paginas_e_links(dist: Path) -> tuple[int, int]:
    base = (os.environ.get("SITE_BASE") or "/").rstrip("/")
    paginas = sorted(dist.rglob("*.html"))
    ids_cache: dict[Path, set] = {}

    def ids_de(p: Path) -> set:
        if p not in ids_cache:
            ids_cache[p] = {n.attrs["id"] for n in parse(p).todos() if "id" in n.attrs} | \
                           {n.attrs["name"] for n in parse(p).busca("a") if "name" in n.attrs}
        return ids_cache[p]

    def resolver(origem: Path, caminho: str) -> Path | None:
        if caminho.startswith("/"):
            if base and not (caminho == base or caminho.startswith(base + "/")):
                return None
            rel = caminho[len(base):].lstrip("/")
            alvo = dist / rel
        else:
            alvo = (origem.parent / caminho).resolve()
        for c in (alvo, alvo / "index.html", alvo.with_suffix(".html")):
            if c.is_file():
                return c
        return None

    nlinks = 0
    for p in paginas:
        doc = parse(p)
        rel = p.relative_to(dist)
        robots = doc.primeiro("meta", name="robots")
        if robots is None or "noindex" not in robots.attrs.get("content", ""):
            erro(f"[noindex] {rel}: falta <meta name=robots content=noindex>")
        if doc.primeiro("html") is None or not doc.primeiro("html").attrs.get("lang"):
            erro(f"[html] {rel}: falta lang")
        vistos_ids = [n.attrs["id"] for n in doc.todos() if "id" in n.attrs]
        dup = {i for i in vistos_ids if vistos_ids.count(i) > 1}
        if dup:
            erro(f"[html] {rel}: ids duplicados {sorted(dup)[:5]}")
        for n in doc.todos():
            for at in ("href", "src"):
                v = n.attrs.get(at)
                if not v or n.tag == "script" and at == "src" and v.startswith("http"):
                    continue
                u = urlsplit(v)
                if u.scheme or v.startswith("//") or v.startswith("mailto:"):
                    continue
                nlinks += 1
                alvo = p if not u.path else resolver(p, unquote(u.path))
                if alvo is None:
                    erro(f"[link] {rel}: {at}='{v}' não existe em dist/")
                    continue
                if u.fragment and alvo.suffix == ".html" and unquote(u.fragment) not in ids_de(alvo):
                    erro(f"[âncora] {rel}: '{v}' — #{u.fragment} não existe em {alvo.relative_to(dist)}")
    return len(paginas), nlinks


# ----------------------------------------------------------------- 5: downloads

def conferir_downloads(dist: Path) -> int:
    d = dist / "dados"
    if not d.is_dir():
        erro("[dados] dist/dados/ não foi gerado")
        return 0
    pares = {f"orixas/{p.name}": p for p in (DATA / "orixas").glob("*.json")}
    pares |= {"conexoes.json": DATA / "conexoes.json", "entidades_equivalentes.json": DATA / "entidades_equivalentes.json",
              "divergencias.json": DATA / "fichamento" / "divergencias.json", "fontes.json": DATA / "fontes" / "catalogo.json"}
    if (DATA / "glossario.json").exists():
        pares["glossario.json"] = DATA / "glossario.json"
    for nome, origem in pares.items():
        p = d / nome
        if not p.exists():
            erro(f"[dados] falta dados/{nome}")
        elif p.read_bytes() != origem.read_bytes():
            erro(f"[dados] dados/{nome} difere de {origem.relative_to(RAIZ)}")
    t = d / "tradicoes.json"
    if t.exists():
        for x in json.loads(t.read_text(encoding="utf-8"))["tradicoes"]:
            if x.get("status") == "rascunho_sem_fonte" and x.get("descricao"):
                erro(f"[dados] tradicoes.json publica descrição sem fonte de {x['id']}")
    else:
        erro("[dados] falta dados/tradicoes.json")
    leia = d / "LEIAME.txt"
    if not leia.exists() or "a definir pelo autor" not in leia.read_text(encoding="utf-8"):
        erro("[dados] LEIAME.txt ausente ou sem aviso de licença")
    pag = dist / "baixar-dados" / "index.html"
    if not pag.exists() or "a definir pelo autor" not in pag.read_text(encoding="utf-8"):
        erro("[dados] página Baixar dados ausente ou sem aviso de licença")
    publicados = {str(p.relative_to(d)) for p in d.rglob("*") if p.is_file()}
    extras = publicados - set(pares) - {"tradicoes.json", "LEIAME.txt"}
    if extras:
        erro(f"[dados] arquivos não previstos em dados/: {sorted(extras)}")
    return len(publicados)


def main():
    dist = RAIZ / "site" / "dist"
    if "--dist" in sys.argv:
        dist = Path(sys.argv[sys.argv.index("--dist") + 1]).resolve()
    if not (dist / "index.html").exists():
        sys.exit(f"{dist} não tem index.html — rode antes: cd site && npm run build")
    fichas, fontes, registros = carregar()
    nv = conferir_fichas(dist, fichas, fontes)
    npro = conferir_proibidos(dist, fichas, registros)
    npag, nlinks = conferir_paginas_e_links(dist)
    ndados = conferir_downloads(dist)
    total = sum(len(vs) for f in fichas.values() for vs in f["atributos"].values())
    print(f"QA do site: {len(fichas)} fichas, {nv}/{total} versões conferidas contra data/orixas; "
          f"{npro} registros proibidos (pré-fichamento/retidos) procurados; {npag} páginas, {nlinks} links internos; "
          f"{ndados} arquivos em dados/")
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print("  -", e)
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    main()
