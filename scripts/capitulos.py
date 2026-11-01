"""Capítulos narrativos por orixá: leitura de data/capitulos/<id>.md e geração do JSON.

Um capítulo é texto corrido do projeto, montado só com registros do fichamento.
Formato (detalhes em docs/capitulos-guia.md):

    ---
    orixa: ogum
    titulo: Ogum, senhor do ferro e dos caminhos
    status: rascunho
    atualizado: 2026-11-01
    ---

    Parágrafo de abertura ... {{ref:ogum-049}}

    ## Nomes e origem {#nomes-e-origem}

    Texto ... {{ref:ogum-049,ogum-050}} Mais texto, com [link](ita:ita-004) ... {{ref:ogum-047}}

    ### Subtítulo opcional

    ... {{lacuna:saudacao}} ... {{pendencia:Cacciatore, *Dicionário}}

Blocos separados por linha em branco. `## Título {#slug}` abre seção (slug da lista
SECOES, na ordem); `### Título` abre subtítulo. Todo o resto é parágrafo.

Marcadores (cada trecho de texto termina num marcador que o sustenta):
- `{{ref:id1,id2}}`  registros do fichamento (só fichado/revisado e não retidos);
- `{{lacuna:atributo}}` ou `{{lacuna:atributo@tradicao}}`  o fichamento NÃO tem
  registro publicado desse atributo (nessa tradição) para o orixá — conferido;
- `{{pendencia:texto}}`  o texto aparece em docs/pesquisa/PENDENCIAS.md (obra
  bloqueada, exemplar a obter) — conferido.
Links: `[rótulo](ita:ita-006)`, `(orixa:ogum)`, `(glossario:pade)`,
`(tradicao:candomble_jeje)`, `(grafo:ogum)`. Itálico: `*texto*`.

O JSON gerado (data/capitulos/<id>.json) é o que o site lê: estrutura, segmentos
e notas numeradas por ordem de primeira aparição. Gerar: scripts/validar_capitulos.py --gerar.
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "data" / "capitulos"

# (slug, título padrão, obrigatória)
SECOES = [
    ("nomes-e-origem", "Nomes e origem", True),
    ("historia-do-culto", "História do culto", True),
    ("dominios-e-simbolos", "Domínios, elementos e símbolos", True),
    ("mitos", "Mitos", True),
    ("tradicoes", "Em cada tradição", True),
    ("sincretismo", "Sincretismo", True),
    ("leituras-academicas", "Leituras acadêmicas", True),
    ("lacunas", "O que as fontes não dizem", True),
]
SLUGS = [s for s, _, _ in SECOES]
CAMPOS_FRONT = {"orixa", "titulo", "status", "atualizado"}
TIPOS_LINK = {"ita", "orixa", "glossario", "tradicao", "grafo"}

RE_MARCADOR = re.compile(r"\{\{(ref|lacuna|pendencia):([^}]*)\}\}")
RE_LINK = re.compile(r"\[([^\]]+)\]\((ita|orixa|glossario|tradicao|grafo):([^)\s]+)\)")
RE_TOKEN = re.compile(RE_MARCADOR.pattern + "|" + RE_LINK.pattern)
RE_SECAO = re.compile(r"^##\s+(.+?)\s*\{#([a-z0-9-]+)\}\s*$")
RE_SUB = re.compile(r"^###\s+(.+?)\s*$")


class ErroFormato(Exception):
    pass


def ler_md(caminho):
    texto = Path(caminho).read_text(encoding="utf-8")
    if not texto.startswith("---\n"):
        raise ErroFormato("falta o frontmatter (--- no início)")
    fim = texto.find("\n---\n", 4)
    if fim < 0:
        raise ErroFormato("frontmatter sem o --- de fechamento")
    front = {}
    for n, linha in enumerate(texto[4:fim].splitlines(), 2):
        if not linha.strip():
            continue
        if ":" not in linha:
            raise ErroFormato(f"frontmatter, linha {n}: esperado 'chave: valor'")
        k, v = linha.split(":", 1)
        front[k.strip()] = v.strip()
    corpo = texto[fim + 5:]
    linha0 = texto[:fim + 5].count("\n") + 1
    return front, corpo, linha0


def blocos(corpo, linha0):
    """[(linha, texto)] de blocos separados por linha em branco."""
    out, atual, ini = [], [], None
    for i, linha in enumerate(corpo.splitlines()):
        if linha.strip():
            if not atual:
                ini = linha0 + i
            atual.append(linha.strip())
        elif atual:
            out.append((ini, atual))
            atual = []
    if atual:
        out.append((ini, atual))
    return out


def tokens(texto):
    """Divide um parágrafo em tokens: texto, link, ref, lacuna, pendencia."""
    out, pos = [], 0
    for m in RE_TOKEN.finditer(texto):
        if m.start() > pos:
            out.append({"t": "texto", "v": texto[pos:m.start()]})
        if m.group(1):
            tipo, arg = m.group(1), m.group(2).strip()
            if tipo == "ref":
                out.append({"t": "ref", "ids": [x.strip() for x in arg.split(",") if x.strip()]})
            elif tipo == "lacuna":
                atr, _, trad = arg.partition("@")
                out.append({"t": "lacuna", "atributo": atr.strip(), "tradicao": trad.strip() or None})
            else:
                out.append({"t": "pendencia", "ancora": arg})
        else:
            out.append({"t": "link", "rotulo": m.group(3), "tipo": m.group(4), "alvo": m.group(5)})
        pos = m.end()
    if pos < len(texto):
        out.append({"t": "texto", "v": texto[pos:]})
    return out


def texto_simples(tks):
    """Texto legível do parágrafo/segmento (sem marcadores; links pelo rótulo; sem *)."""
    s = "".join(t["v"] if t["t"] == "texto" else t["rotulo"] if t["t"] == "link" else " " for t in tks)
    return re.sub(r"\s+", " ", s.replace("*", "")).strip()


def segmentos(tks):
    """[(tokens do trecho, [marcadores])]; o último pode ter marcadores vazios (trecho sem apoio)."""
    segs, atual, marc = [], [], []
    for t in tks:
        if t["t"] in ("ref", "lacuna", "pendencia"):
            marc.append(t)
        else:
            if marc:
                segs.append((atual, marc))
                atual, marc = [], []
            atual.append(t)
    if atual or marc:
        segs.append((atual, marc))
    return segs


def chave_marcador(m):
    if m["t"] == "ref":
        return None
    if m["t"] == "lacuna":
        return f"lacuna:{m['atributo']}" + (f"@{m['tradicao']}" if m["tradicao"] else "")
    return f"pendencia:{m['ancora']}"


def parse(caminho):
    """Lê o .md e devolve (estrutura, erros_de_formato)."""
    erros = []
    front, corpo, linha0 = ler_md(caminho)
    secoes = [{"slug": "abertura", "titulo": None, "blocos": []}]
    for linha, linhas in blocos(corpo, linha0):
        primeira = linhas[0]
        if primeira.startswith("## "):
            m = RE_SECAO.match(primeira)
            if not m or len(linhas) > 1:
                erros.append(f"linha {linha}: título de seção deve ser '## Título {{#slug}}' sozinho no bloco")
                continue
            secoes.append({"slug": m.group(2), "titulo": m.group(1), "blocos": []})
        elif primeira.startswith("### "):
            m = RE_SUB.match(primeira)
            if not m or len(linhas) > 1:
                erros.append(f"linha {linha}: subtítulo deve ser '### Título' sozinho no bloco")
                continue
            secoes[-1]["blocos"].append({"tipo": "subtitulo", "texto": m.group(1), "linha": linha})
        elif primeira.startswith("#"):
            erros.append(f"linha {linha}: só ## e ### são aceitos")
        else:
            texto = " ".join(linhas)
            secoes[-1]["blocos"].append({"tipo": "paragrafo", "linha": linha, "tokens": tokens(texto)})
    if not secoes[0]["blocos"]:
        secoes.pop(0)
    return {"front": front, "secoes": secoes}, erros


def gerar_json(estrutura):
    """JSON para o site: seções, parágrafos (tokens) e notas de rodapé.

    Cada grupo de marcadores vizinhos ({{ref}}, {{lacuna}}, {{pendencia}} sem texto
    entre eles) vira UMA nota de rodapé, numerada na ordem do texto, com a lista de
    itens (registros, lacunas, pendências). No texto, a nota aparece como um número
    sobrescrito no lugar dos marcadores."""
    notas = []
    secoes = []
    for s in estrutura["secoes"]:
        bl = []
        for b in s["blocos"]:
            if b["tipo"] == "subtitulo":
                bl.append({"tipo": "subtitulo", "texto": b["texto"]})
                continue
            tks, grupo = [], []

            def fechar():
                if grupo:
                    notas.append({"n": len(notas) + 1, "itens": list(grupo)})
                    tks.append({"t": "nota", "n": len(notas)})
                    grupo.clear()

            for t in b["tokens"]:
                if t["t"] == "ref":
                    grupo.extend({"tipo": "registro", "registro": i} for i in t["ids"])
                elif t["t"] in ("lacuna", "pendencia"):
                    item = {"tipo": t["t"]}
                    item.update({k: v for k, v in t.items() if k != "t"})
                    grupo.append(item)
                elif t["t"] == "texto" and not t["v"].strip() and grupo:
                    continue  # espaço entre marcadores vizinhos
                else:
                    fechar()
                    tks.append(t)
            fechar()
            bl.append({"tipo": "paragrafo", "tokens": tks})
        secoes.append({"slug": s["slug"], "titulo": s["titulo"], "blocos": bl})
    f = estrutura["front"]
    return {
        "_meta": {
            "gerado_por": "scripts/validar_capitulos.py --gerar",
            "fonte": f"data/capitulos/{f.get('orixa')}.md",
            "aviso": "Gerado a partir do .md; não editar à mão.",
        },
        "orixa": f.get("orixa"),
        "titulo": f.get("titulo"),
        "status": f.get("status"),
        "atualizado": f.get("atualizado"),
        "secoes": secoes,
        "notas": notas,
    }


def arquivos_md(raiz=RAIZ):
    return sorted((Path(raiz) / "data" / "capitulos").glob("*.md"))


def textos_para_anticopia(raiz=RAIZ):
    """(rótulo, registros citados, texto) para cada trecho de cada capítulo."""
    for p in arquivos_md(raiz):
        est, _ = parse(p)
        for s in est["secoes"]:
            for b in s["blocos"]:
                if b["tipo"] != "paragrafo":
                    continue
                for k, (tks, marc) in enumerate(segmentos(b["tokens"])):
                    ids = [i for m in marc if m["t"] == "ref" for i in m["ids"]]
                    txt = texto_simples(tks)
                    if txt:
                        yield f"capitulos/{p.stem}:{b['linha']}#{k + 1}", ids, txt
