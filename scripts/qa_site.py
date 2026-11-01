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
3. Selo de rascunho em toda ficha que tenha alguma versão sem revisão vigente
   (sem selo, e com o aviso de ficha revisada, só quando TODAS as versões estão
   'revisado'); `noindex` em todas as páginas.
4. Links internos (href/src) apontam para arquivos existentes e âncoras (#id)
   existentes na página de destino.
5. /dados/: cópias idênticas a data/ (exceto tradicoes.json, que só pode perder
   descrições sem fonte, e LEIAME.txt), com aviso de licença.
6. Glossário: todos os termos de data/glossario.json exibidos, com definição,
   divergências e nota idênticas ao JSON e cada fonte (link, ano e página)
   conferida; nenhum termo sem fonte ou fora do JSON exibido; pendentes sem
   definição. Termos ligados nas fichas existem no glossário e a definição
   referenciada por aria-describedby é a do JSON.
7. Tradições: todas exibidas no grupo certo; `com_fonte` com descrição e fontes
   idênticas ao JSON; `rascunho_sem_fonte` com o aviso "Descrição pendente de
   fonte" e o texto do rascunho (descrição e nota) ausente de TODAS as páginas.
   Fichas e catálogo linkam para a página Tradições.
8. Sobre: canal de contribuição pelas issues do repositório, link para Fontes,
   aviso de que licenças, domínio e autoria dependem do autor e nenhum e-mail.
9. Revisão do conselho: cada versão mostra exatamente as linhas "Revisado por …
   (tradição) em …" / "Contestado por …" das suas `revisoes`, com o crédito que o
   consentimento permite (scripts/revisao.py: quem, linha_credito); versão sem
   revisão não mostra nenhuma; o estado da revisão na seção Pendências bate com
   os dados; data/revisores.json não é publicado em /dados/; revisores anônimos
   ou que revogaram o consentimento não aparecem por nome em nenhuma página.

Uso: python3 scripts/qa_site.py [--dist site/dist]
Respeita SITE_BASE (o mesmo do build; padrão /mapadosorixas, o subcaminho do
GitHub Pages; SITE_BASE=/ para a raiz) para resolver links absolutos: link
absoluto fora do prefixo conta como quebrado.
11. Lista-mestra, itãs e cosmologia (modelo 2): o catálogo tem um cartão por
   entidade de data/entidades.json; com ficha → link para a ficha; sem ficha →
   "Em pesquisa", sem link de ficha nem texto além de nome e tipo; rótulo de grupo
   só se confirmado por registro; aviso em entidade sensível. Página Itãs lista
   todos os itãs com versão lida; cada página de itã mostra exatamente as versões
   fichadas/revisadas (valor, resumo, tradições, odu, nota e fontes idênticos ao
   JSON) e nenhuma em pré-fichamento. Cosmologia mostra exatamente as versões de
   'hierarquia' das fichas ou, sem nenhuma, o aviso de estrutura vazia. Grafo
   tem o filtro por tipo de entidade. /dados/entidades.json e /dados/itans.json
   são as cópias filtradas.
12. Acervo interno (acervo/, texto integral das fontes; uso interno): nenhum
   arquivo do dist (inclusive /dados/) tem "acervo" no caminho, é PDF, tem o nome
   de um arquivo do acervo (<source_id>.pdf/.txt) nem cita os arquivos do
   acervo (indice.json, INDICE.md, LEIAME.md, urls_extras.json); e, se
   acervo/txt tiver textos, nenhuma sequência de 20 palavras de um deles aparece
   no texto do site (descontadas as que estão no catálogo de fontes: títulos).
10. Publicação (rascunho): faixa "Rascunho — aguardando revisão…" em TODAS as
   páginas; Início com o aviso de versão inicial em revisão e link para as
   issues; nenhum <link rel=canonical>/sitemap que convide indexação.
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
sys.path.insert(0, str(RAIZ / "scripts"))
import revisao  # noqa: E402

REVISORES = revisao.por_id(revisao.carregar_revisores(RAIZ))
NOME_TRAD = {t["id"]: t["nome"] for t in json.loads((DATA / "tradicoes.json").read_text(encoding="utf-8"))["tradicoes"]}
SELO = "Rascunho — aguardando revisão de praticantes e pesquisadores"
VAZIOS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

erros: list[str] = []


def site_base() -> str:
    """Prefixo do site, igual ao de site/astro.config.mjs ('' quando na raiz)."""
    return (os.environ.get("SITE_BASE", "/mapadosorixas") or "/").rstrip("/")


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
        versoes = [v for vs in ficha["atributos"].values() for v in vs]
        n_rev = sum(v["status"] == "revisado" for v in versoes)
        if versoes and n_rev == len(versoes):
            if selo is not None:
                erro(f"[selo] {oid}: todas as versões revisadas, mas o selo de rascunho continua")
            if doc.primeiro("p", "selo-revisado") is None:
                erro(f"[selo] {oid}: falta o aviso de ficha revisada")
        elif selo is None or SELO not in norm(selo.texto()):
            erro(f"[selo] {oid}: selo de rascunho ausente ({n_rev}/{len(versoes)} versões revisadas)")
        estado = doc.primeiro("dd", id="estado-revisao")
        esperado_estado = f"{n_rev} de {len(versoes)} versões" if n_rev else "Ainda não revisada."
        if estado is None or esperado_estado not in norm(estado.texto()):
            erro(f"[revisão] {oid}: estado da revisão em Pendências não diz '{esperado_estado}'")

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
            esperadas_rev = [revisao.linha_credito(rv, REVISORES, lambda x: NOME_TRAD.get(x, x)) for rv in v.get("revisoes", [])]
            vistas_rev = [norm(x.texto()) for x in li.busca("li", "revisao")]
            if vistas_rev != [norm(x) for x in esperadas_rev]:
                erro(f"[revisão] {oid}/{reg}: revisões exibidas {vistas_rev} ≠ esperadas {esperadas_rev}")
            nota_fich = li.primeiro("p", "nota")
            if (v.get("nota") or None) and (nota_fich is None or norm(v["nota"]) not in norm(nota_fich.texto())):
                erro(f"[versão] {oid}/{reg}: nota do fichamento ausente ou diferente")
            ref = next((a for a in li.busca("a") if (a.attrs.get("href") or "").startswith("#nota-")), None)
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
    base = site_base()
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
    for nome, esperado in (("entidades.json", entidades_publicas()), ("itans.json", itans_publicos())):
        q = d / nome
        if not q.exists():
            erro(f"[dados] falta dados/{nome}")
        elif json.loads(q.read_text(encoding="utf-8")) != esperado:
            erro(f"[dados] dados/{nome} difere da cópia filtrada esperada de data/{nome}")
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
    extras = publicados - set(pares) - {"tradicoes.json", "LEIAME.txt", "entidades.json", "itans.json"}
    if extras:
        erro(f"[dados] arquivos não previstos em dados/: {sorted(extras)}")
    return len(publicados)


# ----------------------------------------------------------------- 6, 7, 8: glossário, tradições, sobre

def conferir_citacoes(cont, sources: list, fontes: dict, onde: str) -> None:
    """Cada fonte de `sources` aparece em `cont` como span.citacao com link para
    a fonte, ano e página; nenhuma citação extra."""
    cits = [c for c in cont.busca("span", "citacao")]
    if len(cits) != len(sources):
        erro(f"{onde}: {len(cits)} citação(ões) exibidas, {len(sources)} no JSON")
    for i, s in enumerate(sources):
        c = next((x for x in cits if x.attrs.get("data-fonte") == s["id"]), None)
        if c is None:
            erro(f"{onde}: fonte {s['id']} não exibida")
            continue
        hrefs = [a.attrs.get("href", "") for a in c.busca("a")]
        if not any(h.endswith(f"fontes#fonte-{s['id']}") for h in hrefs):
            erro(f"{onde}: fonte {s['id']} sem link para a página Fontes")
        if s.get("via") and not any(h.endswith(f"fontes#fonte-{s['via']}") for h in hrefs):
            erro(f"{onde}: fonte intermediária {s['via']} sem link")
        loc = c.primeiro("span", "loc")
        if loc is None or norm(loc.texto()) != norm(s["loc"]):
            erro(f"{onde}: página '{s['loc']}' de {s['id']} difere do JSON")
        f = fontes.get(s["id"])
        if f is None:
            erro(f"{onde}: fonte {s['id']} fora do catálogo")
        elif f.get("status_verificacao") not in ("conferido_web", "verificado", "fichado", "revisado"):
            erro(f"{onde}: fonte {s['id']} com status {f.get("status_verificacao")} (exige conferido_web ou acima)")
        elif str(f.get("ano") or "s.d.") not in norm(c.texto()):
            erro(f"{onde}: ano de {s['id']} não aparece")


def conferir_glossario(dist: Path, fontes: dict) -> tuple[int, int]:
    g = json.loads((DATA / "glossario.json").read_text(encoding="utf-8"))
    termos = {t["id"]: t for t in g["termos"]}
    arq = dist / "glossario" / "index.html"
    if not arq.exists():
        erro("[glossário] página glossario/ não foi gerada")
        return 0, 0
    doc = parse(arq)
    exibidos = {n.attrs.get("data-termo"): n for n in doc.busca("div", "termo")}
    for tid in sorted(set(exibidos) - set(termos)):
        erro(f"[glossário] termo exibido '{tid}' não existe em data/glossario.json")
    for tid, t in termos.items():
        onde = f"[glossário] {tid}"
        n = exibidos.get(tid)
        semfonte = t.get("status") != "com_fonte" or not t.get("sources")
        if semfonte:
            if n is not None:
                erro(f"{onde}: termo sem fonte exibido")
            continue
        if n is None:
            erro(f"{onde}: termo não exibido")
            continue
        if n.attrs.get("id") != f"termo-{tid}":
            erro(f"{onde}: âncora termo-{tid} ausente")
        nome = n.primeiro("span", "termo-nome")
        if nome is None or norm(nome.texto()) != norm(t["termo"]):
            erro(f"{onde}: nome do termo difere do JSON")
        d = n.primeiro("p", "definicao")
        if d is None or norm(d.texto()) != norm(t["definicao"]):
            erro(f"{onde}: definição difere do JSON")
        fp = n.primeiro("p", "fontes-termo")
        if fp is None:
            erro(f"{onde}: sem bloco de fontes")
        else:
            conferir_citacoes(fp, t["sources"], fontes, onde)
        divs = list(n.busca("li", "divergencia-termo"))
        if len(divs) != len(t.get("divergencias") or []):
            erro(f"{onde}: {len(divs)} divergência(s) exibidas, {len(t.get('divergencias') or [])} no JSON")
        for li, dv in zip(divs, t.get("divergencias") or []):
            tx = li.primeiro("span", "texto")
            if tx is None or norm(tx.texto()) != norm(dv["texto"]):
                erro(f"{onde}: texto de divergência difere do JSON")
            conferir_citacoes(li.primeiro("span", "fontes-div") or li, dv["sources"], fontes, f"{onde} (divergência)")
        nota = n.primeiro("p", "nota")
        if (t.get("nota") or None) and (nota is None or norm(t["nota"]) not in norm(nota.texto())):
            erro(f"{onde}: nota ausente ou diferente")
        vt = n.primeiro("p", "ver-tambem")
        alvos = {a.attrs.get("href", "") for a in (vt.busca("a") if vt else [])}
        for v in t["ver_tambem"]:
            if f"#termo-{v}" not in alvos:
                erro(f"{onde}: 'ver também' {v} sem link")
    # pendentes: listados, mas nunca como termo definido
    pend = doc.primeiro("ul", "pendentes-glossario")
    for p in g["_meta"].get("pendentes", []):
        if pend is None or norm(p["termo"]) not in norm(pend.texto()):
            erro(f"[glossário] pendente '{p['termo']}' não listado")

    # termos ligados nas fichas (e em qualquer página)
    nligados = 0
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        d = parse(pag)
        defs = {n.attrs["id"]: n for n in d.todos() if "id" in n.attrs}
        for a in d.busca("a", "termo-gl"):
            nligados += 1
            tid = a.attrs.get("data-termo")
            rel = pag.relative_to(dist)
            t = termos.get(tid)
            if t is None or t.get("status") != "com_fonte":
                erro(f"[glossário] {rel}: termo ligado '{tid}' não está no glossário com fonte")
                continue
            if not (a.attrs.get("href") or "").endswith(f"glossario#termo-{tid}"):
                erro(f"[glossário] {rel}: link do termo '{tid}' não aponta para o glossário")
            alvo = defs.get(a.attrs.get("aria-describedby") or "")
            if alvo is None or norm(alvo.texto()) != norm(t["definicao"]):
                erro(f"[glossário] {rel}: aria-describedby de '{tid}' ausente ou com definição diferente do JSON")
    return len(exibidos), nligados


def conferir_tradicoes(dist: Path, fontes: dict) -> tuple[int, int]:
    trads = json.loads((DATA / "tradicoes.json").read_text(encoding="utf-8"))["tradicoes"]
    arq = dist / "tradicoes" / "index.html"
    if not arq.exists():
        erro("[tradições] página tradicoes/ não foi gerada")
        return 0, 0
    doc = parse(arq)
    itens = {n.attrs.get("id", "")[2:]: n for n in doc.busca("li", "tradicao")}
    ids = {t["id"] for t in trads}
    for tid in sorted(set(itens) - ids):
        erro(f"[tradições] tradição exibida '{tid}' não existe em data/tradicoes.json")
    for n in doc.busca(None, "descricao"):
        li = n
        while li is not None and not (li.tag == "li" and "tradicao" in li.classes()):
            li = li.pai
        t = next((x for x in trads if li is not None and li.attrs.get("id") == f"t-{x['id']}"), None)
        if t is None or t["status"] != "com_fonte" or not t.get("sources"):
            erro(f"[tradições] descrição exibida fora de uma tradição com fonte: '{norm(n.texto())[:50]}'")
    rascunhos = []
    for t in trads:
        onde = f"[tradições] {t['id']}"
        n = itens.get(t["id"])
        if n is None:
            erro(f"{onde}: não exibida")
            continue
        sec = n
        while sec is not None and sec.tag != "section":
            sec = sec.pai
        if sec is None or sec.attrs.get("aria-labelledby") != f"grupo-{t['grupo']}":
            erro(f"{onde}: fora do grupo '{t['grupo']}'")
        h3 = n.primeiro("h3")
        if h3 is None or norm(h3.texto()) != norm(t["nome"]):
            erro(f"{onde}: nome difere do JSON")
        pendente = n.primeiro("p", "pendente-fonte")
        if t["status"] == "com_fonte":
            d = n.primeiro("p", "descricao")
            if d is None or norm(d.texto()) != norm(t["descricao"]):
                erro(f"{onde}: descrição difere do JSON")
            fp = n.primeiro("p", "fontes-tradicao")
            if fp is None:
                erro(f"{onde}: sem bloco de fontes")
            else:
                conferir_citacoes(fp, t["sources"], fontes, onde)
            if (t.get("nota") or None):
                nota = n.primeiro("p", "nota")
                if nota is None or norm(t["nota"]) not in norm(nota.texto()):
                    erro(f"{onde}: nota ausente ou diferente")
            if pendente is not None:
                erro(f"{onde}: tradição com fonte marcada como pendente")
        else:
            rascunhos.append(t)
            if pendente is None or "Descrição pendente de fonte" not in norm(pendente.texto()):
                erro(f"{onde}: falta o aviso 'Descrição pendente de fonte'")
            if n.primeiro("span", "citacao") is not None or n.primeiro("p", "nota") is not None:
                erro(f"{onde}: tradição sem fonte exibe citação ou nota")
    # o texto dos rascunhos não pode aparecer em nenhuma página
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        txt = norm(re.sub(r"<[^>]+>", " ", pag.read_text(encoding="utf-8")))
        for t in rascunhos:
            for campo in ("descricao", "nota"):
                v = norm(t.get(campo) or "")
                if len(v) >= 12 and v in txt:
                    erro(f"[tradições] texto sem fonte de {t['id']} ({campo}) aparece em {pag.relative_to(dist)}")
    # fichas e catálogo linkam para a página Tradições
    for rel in ["catalogo/index.html"] + [f"orixas/{p.stem}/index.html" for p in (DATA / "orixas").glob("*.json")]:
        p = dist / rel
        if p.exists() and not any("tradicoes" in (a.attrs.get("href") or "") for a in parse(p).busca("a")):
            erro(f"[tradições] {rel} não linka para a página Tradições")
    return len(itens), len(rascunhos)


def conferir_sobre(dist: Path) -> None:
    arq = dist / "sobre" / "index.html"
    if not arq.exists():
        erro("[sobre] página sobre/ não foi gerada")
        return
    bruto = arq.read_text(encoding="utf-8")
    doc = parse(arq)
    hrefs = [a.attrs.get("href", "") for a in doc.busca("a")]
    if not any(re.search(r"github\.com/[^/]+/[^/]+/issues", h) for h in hrefs):
        erro("[sobre] falta link para as issues do repositório")
    if not any(h.rstrip("/").endswith("fontes") for h in hrefs):
        erro("[sobre] falta link para a página Fontes")
    txt = norm(doc.texto())
    for k in ("licenças", "domínio", "autoria", "dependem do autor"):
        if k not in txt.lower():
            erro(f"[sobre] falta o aviso sobre '{k}'")
    if SELO not in txt:
        erro("[sobre] falta o aviso de rascunho")
    if doc.primeiro("section", id="contribuir") is None and 'id="contribuir"' not in bruto:
        erro("[sobre] falta a seção #contribuir")
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        b = pag.read_text(encoding="utf-8")
        if "mailto:" in b or re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", re.sub(r"<[^>]+>", " ", b)):
            erro(f"[sobre] e-mail exposto em {pag.relative_to(dist)}")


# ----------------------------------------------------------------- 11: lista-mestra, itãs, cosmologia

LIDOS = ("fichado", "revisado")


def entidades_publicas():
    t = json.loads((DATA / "entidades.json").read_text(encoding="utf-8"))
    ents = [{**e, "grupo": e["grupo"] if e.get("grupo") and e["grupo"]["confirmado_por"] else None} for e in t["entidades"]]
    return {"_meta": {**t["_meta"], "publicacao": "Cópia publicada pelo site: rótulos de grupo ainda não confirmados por registro fichado foram removidos (grupo: null)."}, "entidades": ents}


def itans_publicos():
    t = json.loads((DATA / "itans.json").read_text(encoding="utf-8"))
    its = [{**it, "versoes": [v for v in it["versoes"] if v["status"] in LIDOS]} for it in t["itans"]]
    its = [it for it in its if it["versoes"]]
    return {"_meta": {**t["_meta"], "total": len(its), "publicacao": "Cópia publicada pelo site: só versões lidas na fonte (fichado/revisado)."}, "itans": its}


def conferir_modelo2(dist: Path, fichas: dict, fontes: dict) -> tuple[int, int, int]:
    lista = json.loads((DATA / "entidades.json").read_text(encoding="utf-8"))["entidades"]
    rot_grupo = {"funfun": "Orixás funfun", "aboro": "Aborós", "iaba": "Iabás"}
    # catálogo
    arq = dist / "catalogo" / "index.html"
    doc = parse(arq) if arq.exists() else None
    if doc is None:
        erro("[catálogo] página catalogo/ não foi gerada")
    else:
        cartoes = {n.attrs.get("data-entidade"): n for n in doc.busca("li", "cartao")}
        for x in sorted(set(cartoes) - {e["id"] for e in lista}):
            erro(f"[catálogo] cartão '{x}' fora de data/entidades.json")
        for e in lista:
            c = cartoes.get(e["id"])
            onde = f"[catálogo] {e['id']}"
            if c is None:
                erro(f"{onde}: entidade da lista-mestra sem cartão")
                continue
            if c.attrs.get("id") != f"e-{e['id']}":
                erro(f"{onde}: âncora e-{e['id']} ausente")
            links_ficha = [a for a in c.busca("a") if (a.attrs.get("href") or "").rstrip("/").endswith(f"orixas/{e['id']}")]
            if e["id"] in fichas:
                if not links_ficha:
                    erro(f"{onde}: tem ficha, mas o cartão não linka para ela")
                if "em-pesquisa" in c.classes():
                    erro(f"{onde}: tem ficha, mas está marcado como em pesquisa")
            else:
                txt = norm(c.texto())
                if "em-pesquisa" not in c.classes() or "Em pesquisa" not in txt:
                    erro(f"{onde}: sem ficha e sem o aviso 'Em pesquisa'")
                if links_ficha or c.primeiro("a") is not None:
                    erro(f"{onde}: cartão em pesquisa com link")
                ps = [p for p in c.busca("p") if not ({"tipo-entidade", "status-pesquisa", "aviso-sensivel"} & set(p.classes()))]
                if ps:
                    erro(f"{onde}: cartão em pesquisa com texto fora de nome/tipo/aviso: '{norm(ps[0].texto())[:50]}'")
            g = e.get("grupo")
            if g and not g["confirmado_por"] and rot_grupo[g["rotulo"]] in norm(c.texto()):
                erro(f"{onde}: rótulo de grupo não confirmado exibido")
            if e.get("sensivel") and c.primeiro("p", "aviso-sensivel") is None:
                erro(f"{onde}: entidade sensível sem aviso")
    # itãs
    pub = itans_publicos()["itans"]
    todos = json.loads((DATA / "itans.json").read_text(encoding="utf-8"))["itans"]
    pre = [v for it in todos for v in it["versoes"] if v["status"] not in LIDOS]
    arq = dist / "itans" / "index.html"
    if not arq.exists():
        erro("[itãs] página itans/ não foi gerada")
    else:
        listados = {n.attrs.get("data-ita") for n in parse(arq).busca("li", "cartao")}
        if listados != {it["id"] for it in pub}:
            erro(f"[itãs] lista difere dos itãs com versão lida: {sorted(listados ^ {it['id'] for it in pub})}")
    nv = 0
    for it in pub:
        onde = f"[itã] {it['id']}"
        arq = dist / "itans" / it["id"] / "index.html"
        if not arq.exists():
            erro(f"{onde}: página não gerada")
            continue
        doc = parse(arq)
        if doc.primeiro("p", "selo") is None:
            erro(f"{onde}: falta o selo de rascunho")
        h1 = doc.primeiro("h1")
        if h1 is None or norm(h1.texto()) != norm(it["titulo"]):
            erro(f"{onde}: título difere do JSON")
        lis = list(doc.busca("li", "versao-ita"))
        if len(lis) != len(it["versoes"]):
            erro(f"{onde}: {len(lis)} versões exibidas, {len(it['versoes'])} lidas no JSON")
        for li, v in zip(lis, it["versoes"]):
            nv += 1
            ov = f"{onde}/{v.get('registro') or '?'}"
            if (li.attrs.get("data-registro") or None) != v.get("registro"):
                erro(f"{ov}: versão fora de ordem ou de outro registro")
            for cls, esperado in (("valor", v["valor"]), ("resumo", v["resumo"])):
                n = li.primeiro(None, cls)
                if n is None or norm(n.texto()) != norm(esperado):
                    erro(f"{ov}: {cls} difere do JSON")
            if v.get("nota"):
                n = li.primeiro("p", "nota")
                if n is None or norm(v["nota"]) not in norm(n.texto()):
                    erro(f"{ov}: nota ausente ou diferente")
            odu = li.primeiro("p", "odu")
            if bool(odu) != bool(v.get("odu")) or (odu and norm(v["odu"]["nome"]) not in norm(odu.texto())):
                erro(f"{ov}: odu exibido difere do JSON")
            fp = li.primeiro("p", "fontes-ita")
            if fp is None:
                erro(f"{ov}: sem bloco de fontes")
            else:
                conferir_citacoes(fp, v["sources"], fontes, ov)
            etiquetas = {norm(x.attrs.get("title", "")).split(" — ")[0] for x in li.busca("span", "etiqueta")}
            if etiquetas != {norm(NOME_TRAD.get(t, t)) for t in v["tradicoes"]}:
                erro(f"{ov}: tradições exibidas diferem do JSON")
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        txt = norm(re.sub(r"<[^>]+>", " ", pag.read_text(encoding="utf-8")))
        for v in pre:
            r = norm(v["resumo"])
            if len(r) >= 12 and r in txt:
                erro(f"[itã] resumo de versão não lida aparece em {pag.relative_to(dist)}")
    # cosmologia
    arq = dist / "cosmologia" / "index.html"
    nh = 0
    if not arq.exists():
        erro("[cosmologia] página cosmologia/ não foi gerada")
    else:
        doc = parse(arq)
        esperadas = {v["registro"]: v for f in fichas.values() for v in f["atributos"].get("hierarquia", [])}
        vistas = {n.attrs.get("data-registro"): n for n in doc.busca("li", "versao-hierarquia")}
        if set(vistas) != set(esperadas):
            erro(f"[cosmologia] versões exibidas diferem das versões de hierarquia das fichas: {sorted(set(vistas) ^ set(esperadas))}")
        for rid, v in esperadas.items():
            n = vistas.get(rid)
            if n is None:
                continue
            nh += 1
            if norm((n.primeiro(None, "valor") or n).texto()) != norm(v["valor"]) or norm((n.primeiro("p", "resumo") or n).texto()) != norm(v["parafrase"]):
                erro(f"[cosmologia] {rid}: valor ou paráfrase difere da ficha")
            conferir_citacoes(n.primeiro("p", "fontes-hierarquia") or n, v["sources"], fontes, f"[cosmologia] {rid}")
        if not esperadas and doc.primeiro("p", id="aviso-sem-hierarquia") is None:
            erro("[cosmologia] sem versões de hierarquia e sem o aviso de estrutura vazia")
        if esperadas and doc.primeiro("p", id="aviso-sem-hierarquia") is not None:
            erro("[cosmologia] aviso de estrutura vazia exibido apesar de haver versões")
    # grafo: filtro por tipo de entidade
    g = dist / "grafo" / "index.html"
    if g.exists() and not list(parse(g).busca("input", name="tipo-entidade")):
        erro("[grafo] falta o filtro por tipo de entidade")
    return len(lista), nv, nh


# ----------------------------------------------------------------- 10: publicação em rascunho

ISSUES = re.compile(r"github\.com/[^/]+/[^/]+/issues")


def conferir_publicacao(dist: Path) -> None:
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        doc = parse(pag)
        faixa = doc.primeiro("div", "faixa-rascunho")
        if faixa is None or SELO not in norm(faixa.texto()):
            erro(f"[rascunho] {pag.relative_to(dist)}: falta a faixa de rascunho")
        if any("canonical" in l.attrs.get("rel", "") for l in doc.busca("link")):
            erro(f"[rascunho] {pag.relative_to(dist)}: <link rel=canonical> não deve existir enquanto o site é rascunho")
    if list(dist.glob("sitemap*.xml")):
        erro("[rascunho] sitemap publicado: não convidar indexação até a revisão")
    inicio = parse(dist / "index.html")
    aviso = inicio.primeiro("div", "aviso-versao")
    if aviso is None:
        erro("[rascunho] Início: falta o aviso de versão inicial em revisão")
    elif not any(ISSUES.search(a.attrs.get("href", "")) for a in aviso.busca("a")):
        erro("[rascunho] Início: o aviso de versão inicial não linka para as issues")


# ----------------------------------------------------------------- 9: revisão (privacidade)

def conferir_revisores(dist: Path) -> int:
    if (dist / "dados" / "revisores.json").exists():
        erro("[revisão] data/revisores.json não deve ser publicado em /dados/")
    # nomes que NÃO podem aparecer: só existem se alguém errar o cadastro (o
    # validador já exige null), mas o QA confere o site publicado mesmo assim
    proibidos = []
    for r in REVISORES.values():
        cons = r.get("consentimento") or {}
        if cons.get("revogado_em") or r.get("credito") == "anonimo":
            proibidos += [x for x in (r.get("nome_publico"), r.get("descricao_publica")) if x]
        elif r.get("credito") == "so_nome" and r.get("descricao_publica"):
            proibidos.append(r["descricao_publica"])
        elif r.get("credito") == "generico" and r.get("nome_publico"):
            proibidos.append(r["nome_publico"])
    for pag in sorted(dist.rglob("*.html")):
        if "pagefind" in pag.parts:
            continue
        txt = norm(re.sub(r"<[^>]+>", " ", pag.read_text(encoding="utf-8")))
        for x in proibidos:
            if norm(x) in txt:
                erro(f"[revisão] {pag.relative_to(dist)}: crédito não autorizado pelo consentimento aparece no site")
    return len(REVISORES)


# ----------------------------------------------------------------- acervo interno

N_ACERVO = 20
PALAVRA = re.compile(r"\w+", re.U)


def conferir_acervo(dist: Path) -> tuple[int, int]:
    """Nada de acervo/ no site: caminhos, PDFs, nomes de arquivo e trechos de 20 palavras."""
    acervo = RAIZ / "acervo"
    nomes = set()
    for sub in ("pdf", "txt"):
        nomes |= {p.name for p in (acervo / sub).glob("*") if p.name != ".gitkeep"}
    indice = acervo / "indice.json"
    if indice.exists():
        for e in json.loads(indice.read_text(encoding="utf-8"))["itens"]:
            nomes |= {f"{e['source_id']}.pdf", f"{e['source_id']}.txt"}
    nomes |= {"indice.json", "INDICE.md", "urls_extras.json"}
    textos = []
    for arq in sorted(dist.rglob("*")):
        if not arq.is_file():
            continue
        rel = arq.relative_to(dist)
        if any("acervo" in parte.lower() for parte in rel.parts):
            erro(f"acervo: arquivo do acervo no site: {rel}")
        if arq.name in nomes:
            erro(f"acervo: arquivo com nome de arquivo do acervo no site: {rel}")
        with arq.open("rb") as fh:
            if fh.read(5) == b"%PDF-":
                erro(f"acervo: PDF no site: {rel}")
        if arq.suffix in (".html", ".json", ".txt", ".js", ".xml", ".csv"):
            textos.append(arq.read_text(encoding="utf-8", errors="ignore"))
    site = "\n".join(textos)
    if re.search(r"acervo/(?:pdf|txt)/", site):
        erro("acervo: o site referencia caminhos acervo/pdf ou acervo/txt")
    # trechos: 20 palavras seguidas de algum texto do acervo no texto do site
    refs = sorted((acervo / "txt").glob("*.txt"))
    if not refs:
        return 0, 0
    sem_tags = html.unescape(re.sub(r"<[^>]+>", " ", site)).lower()
    pal = PALAVRA.findall(sem_tags)
    grams = {hash(tuple(pal[i:i + N_ACERVO])) for i in range(len(pal) - N_ACERVO + 1)}
    # títulos e notas do catálogo de fontes (página Fontes, citações) são referência
    # bibliográfica, não texto da obra: descontados
    # (trecho que contém 10 palavras seguidas do catálogo é título/referência)
    cat = PALAVRA.findall((DATA / "fontes" / "catalogo.json").read_text(encoding="utf-8").lower())
    cat10 = {tuple(cat[i:i + 10]) for i in range(len(cat) - 9)}
    texto_site = " ".join(pal)
    for ref in refs:
        rp = PALAVRA.findall(ref.read_text(encoding="utf-8", errors="ignore").lower())
        for i in range(len(rp) - N_ACERVO + 1):
            g = tuple(rp[i:i + N_ACERVO])
            if hash(g) in grams and " ".join(g) in texto_site:
                if any(g[j:j + 10] in cat10 for j in range(N_ACERVO - 9)):
                    continue
                erro(f"acervo: trecho de {N_ACERVO} palavras de {ref.name} no site: “{' '.join(g)}”")
                break
    return len(nomes), len(refs)


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
    ntermos, nligados = conferir_glossario(dist, fontes)
    ntrad, nrasc = conferir_tradicoes(dist, fontes)
    conferir_sobre(dist)
    conferir_publicacao(dist)
    nrevisores = conferir_revisores(dist)
    nents, nvitans, nhier = conferir_modelo2(dist, fichas, fontes)
    nnomes_acervo, nrefs_acervo = conferir_acervo(dist)
    total = sum(len(vs) for f in fichas.values() for vs in f["atributos"].values())
    nrev_vers = sum(1 for f in fichas.values() for vs in f["atributos"].values() for v in vs if v.get("revisoes"))
    print(f"QA do site: {len(fichas)} fichas, {nv}/{total} versões conferidas contra data/orixas; "
          f"{npro} registros proibidos (pré-fichamento/retidos) procurados; {npag} páginas, {nlinks} links internos; "
          f"{ndados} arquivos em dados/; glossário: {ntermos} termos, {nligados} links de termo nas páginas; "
          f"tradições: {ntrad} exibidas, {nrasc} com descrição pendente de fonte (texto ausente do site); "
          f"revisão: {nrevisores} revisor(es) cadastrado(s), {nrev_vers} versão(ões) com revisão exibida; "
          f"lista-mestra: {nents} entidades no catálogo; itãs: {nvitans} versões conferidas; cosmologia: {nhier} versões de hierarquia; "
          f"acervo: {nnomes_acervo} nomes de arquivo e {nrefs_acervo} texto(s) de acervo/txt procurados (0 vazamentos se ok); "
          f"prefixo: {site_base() or '/'}")
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print("  -", e)
        sys.exit(1)
    print("ok")


if __name__ == "__main__":
    main()
