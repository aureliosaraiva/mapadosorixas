#!/usr/bin/env python3
"""Valida os capítulos narrativos (data/capitulos/<id>.md) e gera o JSON que o site lê.

Regras (docs/capitulos-guia.md):
 1. Formato: frontmatter (orixa, titulo, status, atualizado); orixa = nome do
    arquivo, da lista-mestra e com ficha; seções da lista fixa, na ordem, todas
    as obrigatórias presentes.
 2. Todo parágrafo tem marcador, e todo trecho de texto termina num marcador
    ({{ref:...}}, {{lacuna:...}} ou {{pendencia:...}}): não sobra frase sem apoio.
 3. Toda referência existe e é `fichado`/`revisado`; nunca `pre_fichamento` nem
    registro retido (tabus, alimentos ou parecer nao_publicar).
 4. {{lacuna:atributo[@tradicao]}} só se o fichamento de fato não tem registro
    fichado/revisado desse atributo (nessa tradição) para o orixá;
    {{pendencia:texto}} só se o texto está em docs/pesquisa/PENDENCIAS.md.
 5. Links (ita, orixa, glossario, tradicao, grafo) apontam para itens existentes
    e publicados.
 6. Heurística de sustentação: nomes próprios, números, dias da semana e cores de
    cada trecho aparecem nos registros citados por ele (valor, paráfrase, nota,
    casa, tradição, fonte) ou no alvo dos links do trecho. Não substitui a
    conferência manual, registrada no relatório da sessão.
 7. Divergências: parágrafo que cita versão de atributo divergente
    (data/fichamento/divergencias.json) nomeia a tradição, a casa ou o autor de
    cada versão citada; frases que elegem versão ("a versão correta", "na
    verdade"...) são erro. Aviso quando só uma versão de um atributo divergente
    é narrada.
 8. Candomblé × Umbanda: parágrafo que cita registro só de Umbanda diz
    "Umbanda"; parágrafo que mistura Umbanda e Candomblé nomeia os dois; a
    seção de tradições distingue os dois quando o orixá tem registro de Umbanda.
 9. Fontes C antigas (documentos coloniais/missionários, ano < 1950): o
    parágrafo nomeia o autor ou o ano e marca o caráter de documento histórico.
10. Cópia do fichamento: trecho com 8+ palavras seguidas iguais a valor,
    paráfrase ou nota de qualquer registro → erro; 6–7 → aviso. (A comparação
    com o texto das obras fica em scripts/anticopia.py, que inclui os capítulos.)
11. data/capitulos/<id>.json em dia com o .md (e com schemas/capitulo.schema.json).

Uso: python3 scripts/validar_capitulos.py            (valida; sai 1 se houver erro)
     python3 scripts/validar_capitulos.py --gerar    (regenera os JSON e valida)
"""
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import capitulos as cap  # noqa: E402
import entidades as ent  # noqa: E402


def ler(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


ROTULO_ATRIBUTO = {
    "nomes": "Nomes", "origem": "Origem", "dominios": "Domínios", "funcoes": "Funções",
    "elementos": "Elementos", "cores": "Cores", "dia_semana": "Dia da semana", "saudacao": "Saudação",
    "simbolos": "Símbolos e ferramentas", "alimentos": "Alimentos rituais", "animais": "Animais",
    "qualidades": "Qualidades", "parentesco": "Parentesco nos itãs", "equivalencias": "Equivalências entre tradições",
    "sincretismo": "Sincretismo", "itans": "Itãs", "tabus": "Tabus", "festas": "Festas e calendário",
    "historia_culto": "História do culto", "iconografia": "Iconografia",
    "interpretacao_academica": "Interpretação acadêmica", "hierarquia": "Hierarquia e posição cosmológica",
}
LIDO = {"fichado", "revisado"}
AVALIATIVOS = re.compile(
    r"\b(vers[aã]o (correta|verdadeira|certa|aut[eê]ntica)|a verdadeira (vers[aã]o|hist[oó]ria|origem)|"
    r"o correto [eé]|na verdade|de fato|erroneamente|equivocadamente|sem d[uú]vida|indiscutivelmente|obviamente|"
    r"claramente)\b", re.IGNORECASE)
HISTORICO = ("missionári", "viajante", "oficial", "colonial", "documento", "século xix", "séc. xix",
             "relato", "olhar europeu", "pastor", "abade", "padre", "militar", "britânic", "evolucionista")
DIAS = {"segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"}
CORES = {"vermelho", "vermelha", "vermelhos", "preto", "preta", "pretos", "branco", "branca", "brancas", "brancos",
         "azul", "verde", "verdes", "amarelo", "amarela", "prata", "dourado", "rosa", "roxo", "marrom", "azuis"}
# geografia implícita na tradição (por grupo ou id): "no Brasil" é sustentado por
# registro de Candomblé, Umbanda ou religião afro-brasileira regional, e assim por diante
GEO_TRADICAO = {
    "candomble": "Brasil", "afro_brasileira_regional": "Brasil", "umbanda": "Brasil",
    "culto_africano": "África", "ioruba_nigeria": "África Nigéria iorubás", "vodun_benim": "África Daomé Benim fons",
    "lucumi": "Cuba cubana", "palo_monte": "Cuba", "arara": "Cuba", "vodou_haiti": "Haiti", "orisha_trinidad": "Trinidad",
}
# palavras que começam frase ou nomeiam coisas genéricas; nunca contam como "entidade"
STOP = set("""
a à ao aos as às o os um uma uns umas e é em no na nos nas num numa do da dos das de dum duma
para pra por pelo pela pelos pelas com sem sob sobre entre até após ante desde contra
se que quem qual quais cujo cuja onde quando como porque pois porém mas ou nem já ainda também
só apenas mesmo mesma assim daí ali lá aqui aí então logo enquanto embora conforme segundo
ele ela eles elas isso isto esse essa esses essas este esta estes estas aquele aquela aqueles aquelas
seu sua seus suas outro outra outros outras cada todo toda todos todas nenhum nenhuma algum alguma alguns algumas
há houve havia ser foi era são sendo tem têm teve tinha ter fica ficou vem veio diz dizem disse
mais menos muito muita muitos muitas pouco poucos tanto tanta tão bem mal antes depois hoje nunca sempre
nesse nessa neste nesta nisso naquele naquela desse dessa deste desta disso daquele daquela
primeiro primeira segunda terceiro quarto outro último última
conta contam contou lembra registra registram descreve descrevem resume observa anota afirma
nota notas capítulo fontes fonte versão versões leitura leituras mito mitos itã itãs orixá orixás
""".split())


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def palavras(t):
    return re.findall(r"\w+", norm(t))


class Ctx:
    def __init__(self, raiz=RAIZ):
        self.raiz = Path(raiz)
        self.lista = ent.por_id(raiz)
        self.regs = {r["id"]: r for r in ent.todos_registros(raiz)}
        self.catalogo = {f["id"]: f for f in ler(self.raiz / "data/fontes/catalogo.json")["fontes"]}
        self.trad = {t["id"]: t for t in ler(self.raiz / "data/tradicoes.json")["tradicoes"]}
        self.glos = {t["id"]: t for t in ler(self.raiz / "data/glossario.json")["termos"]}
        self.itans = {it["id"]: it for it in ler(self.raiz / "data/itans.json")["itans"]}
        self.nos = {n["id"]: n for n in ler(self.raiz / "data/conexoes.json")["nos"]}
        self.fichas = {p.stem: ler(p) for p in (self.raiz / "data/orixas").glob("*.json")}
        self.retidos = {i for f in self.fichas.values()
                        for ids in f["pendencias"].get("retidos_ate_conselho", {}).values() for i in ids}
        pend = self.raiz / "docs/pesquisa/PENDENCIAS.md"
        self.pendencias = pend.read_text(encoding="utf-8") if pend.exists() else ""
        div = ler(self.raiz / "data/fichamento/divergencias.json")["divergencias"]
        self.divergente = {}  # registro -> (orixa, atributo)
        self.versoes_div = defaultdict(set)
        for d in div:
            for v in d["versoes"]:
                self.divergente[v["registro"]] = (d["orixa"], d["atributo"])
                self.versoes_div[(d["orixa"], d["atributo"])].add(v["registro"])
        self.sobrenomes = set()
        for f in self.catalogo.values():
            for a in f.get("autores") or []:
                if a.strip():
                    self.sobrenomes.add(norm(a.strip().split()[-1].strip("().,")))
        self.nomes_entidades = set()
        for e in self.lista.values():
            for nome in [e["rotulo"], *e.get("grafias", [])]:
                self.nomes_entidades.update(palavras(nome))
        for n in self.nos.values():
            self.nomes_entidades.update(palavras(n["rotulo"]))
        # palavras que aparecem em minúscula no português do projeto: no início de frase não são nome próprio
        minusc = set()
        for r in self.regs.values():
            for campo in ("parafrase", "nota"):
                minusc.update(w for w in re.findall(r"\w+", r.get(campo) or "") if w[:1].islower())
        self.comuns = {norm(w) for w in minusc} - self.nomes_entidades - self.sobrenomes

    # ------------------------------------------------------------ corpus de apoio
    def corpus_registro(self, r):
        partes = [r["valor"], r["parafrase"], r.get("nota") or "", r.get("casa_ou_regiao") or "", r["localizacao"]]
        for t in r["tradicoes"]:
            partes += [t.replace("_", " "), self.trad.get(t, {}).get("nome", ""), GEO_TRADICAO.get(self.trad.get(t, {}).get("grupo"), ""),
                       GEO_TRADICAO.get(t, "")]
        for fid in (r["source_id"], r.get("via_source_id")):
            f = self.catalogo.get(fid) if fid else None
            if f:
                partes += [" ".join(f.get("autores") or []), f.get("titulo", ""), str(f.get("ano", ""))]
        e = self.lista.get(r["orixa"])
        if e:
            partes += [e["rotulo"], *e.get("grafias", [])]
        return " ".join(partes)

    def corpus_link(self, t):
        tipo, alvo = t["tipo"], t["alvo"]
        if tipo == "ita" and alvo in self.itans:
            it = self.itans[alvo]
            return " ".join([it["titulo"], *(self.rotulo(e) for e in it["entidades"])])
        if tipo in ("orixa", "grafo"):
            return self.rotulo(alvo)
        if tipo == "glossario" and alvo in self.glos:
            g = self.glos[alvo]
            return " ".join([g["termo"], *g.get("variantes", [])])
        if tipo == "tradicao" and alvo in self.trad:
            return self.trad[alvo]["nome"]
        return ""

    def rotulo(self, i):
        if i in self.lista:
            e = self.lista[i]
            return " ".join([e["rotulo"], *e.get("grafias", [])])
        if i in self.nos:
            return self.nos[i]["rotulo"]
        return i


def indice_corpus(texto):
    ws = set(palavras(texto))
    pref = set()
    for w in ws:
        for k in range(4, len(w) + 1):
            pref.add(w[:k])
    return ws, pref


def casa(token, idx):
    ws, pref = idx
    if token in ws:
        return True
    if token.isdigit() or len(token) < 5:
        return False
    return token[:max(4, len(token) - 2)] in pref


def candidatos(texto, ctx):
    """Nomes próprios, números, dias e cores mencionados no trecho."""
    out = []
    for m in re.finditer(r"[\w][\w'’-]*", texto):
        w = m.group(0)
        for parte in re.split(r"[-'’]", w):
            if not parte:
                continue
            n = norm(parte)
            if parte.isdigit():
                out.append(n)
            elif parte[0].isupper():
                if n in STOP or len(n) < 2:
                    continue
                if n in ctx.comuns and n not in ctx.nomes_entidades:
                    continue
                out.append(n)
            elif n in {norm(x) for x in DIAS} or n in {norm(x) for x in CORES}:
                out.append(n)
    return out


def ngramas(ws, n):
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


REF_TOKENS = {"p", "pp", "v", "vol", "n", "cf", "apud", "ed", "nota"}


def eh_referencia(g):
    toks = g.split()
    return sum(1 for t in toks if t.isdigit() or t in REF_TOKENS) * 2 >= len(toks)


# ---------------------------------------------------------------- validação de um capítulo

def validar_arquivo(p, ctx, erros, avisos, grams8, grams6):
    rot = f"capitulos/{p.name}"
    try:
        est, errs = cap.parse(p)
    except cap.ErroFormato as e:
        erros.append(f"{rot}: {e}")
        return None
    erros += [f"{rot}: {e}" for e in errs]
    f = est["front"]
    faltam = cap.CAMPOS_FRONT - set(f)
    sobram = set(f) - cap.CAMPOS_FRONT
    if faltam:
        erros.append(f"{rot}: frontmatter sem {sorted(faltam)}")
    if sobram:
        erros.append(f"{rot}: frontmatter com campos desconhecidos {sorted(sobram)}")
    oid = f.get("orixa")
    if oid != p.stem:
        erros.append(f"{rot}: orixa '{oid}' diferente do nome do arquivo")
    if oid not in ctx.lista:
        erros.append(f"{rot}: orixa '{oid}' fora da lista-mestra")
    elif oid not in ctx.fichas:
        erros.append(f"{rot}: '{oid}' não tem ficha gerada (sem registro fichado)")
    if f.get("status") not in ("rascunho", "revisado"):
        erros.append(f"{rot}: status deve ser 'rascunho' ou 'revisado'")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", f.get("atualizado", "")):
        erros.append(f"{rot}: atualizado deve ser AAAA-MM-DD")

    # seções
    slugs = [s["slug"] for s in est["secoes"] if s["slug"] != "abertura"]
    for s in slugs:
        if s not in cap.SLUGS:
            erros.append(f"{rot}: seção desconhecida {{#{s}}} (válidas: {', '.join(cap.SLUGS)})")
    conhecidos = [s for s in slugs if s in cap.SLUGS]
    if len(set(conhecidos)) != len(conhecidos):
        erros.append(f"{rot}: seção repetida")
    if conhecidos != sorted(conhecidos, key=cap.SLUGS.index):
        erros.append(f"{rot}: seções fora da ordem {cap.SLUGS}")
    for s, _, obrig in cap.SECOES:
        if obrig and s not in slugs:
            erros.append(f"{rot}: falta a seção obrigatória {{#{s}}}")
    for s in est["secoes"]:
        if s["slug"] != "abertura" and not any(b["tipo"] == "paragrafo" for b in s["blocos"]):
            erros.append(f"{rot}: seção {{#{s['slug']}}} sem parágrafo")

    nome_orixa = indice_corpus(ctx.rotulo(oid) if oid else "")
    citados = set()
    tem_umbanda = False
    for s in est["secoes"]:
        for b in s["blocos"]:
            if b["tipo"] != "paragrafo":
                continue
            onde = f"{rot}:{b['linha']}"
            texto_par = cap.texto_simples(b["tokens"])
            ntexto = norm(texto_par)
            segs = cap.segmentos(b["tokens"])
            if not any(m for _, m in segs):
                erros.append(f"{onde}: parágrafo sem nenhuma referência")
                continue
            ult_tks, ult_m = segs[-1]
            if not ult_m and re.search(r"\w", cap.texto_simples(ult_tks)):
                erros.append(f"{onde}: trecho final sem referência: “{cap.texto_simples(ult_tks)[:80]}”")
            if AVALIATIVOS.search(texto_par):
                erros.append(f"{onde}: expressão que elege versão ou julga fonte na voz do narrador: “{AVALIATIVOS.search(texto_par).group(0)}”")
            refs_par = []
            for tks, marc in segs:
                corpus = [ctx.rotulo(oid) if oid else ""]
                for m in marc:
                    if m["t"] == "ref":
                        for i in m["ids"]:
                            r = ctx.regs.get(i)
                            if not r:
                                erros.append(f"{onde}: registro inexistente {i}")
                                continue
                            if r["status"] not in LIDO:
                                erros.append(f"{onde}: {i} está '{r['status']}' (só fichado/revisado)")
                                continue
                            if i in ctx.retidos:
                                erros.append(f"{onde}: {i} está retido até o conselho (não publicar)")
                                continue
                            citados.add(i)
                            refs_par.append(r)
                            corpus.append(ctx.corpus_registro(r))
                    elif m["t"] == "lacuna":
                        a, t = m["atributo"], m["tradicao"]
                        if a not in ROTULO_ATRIBUTO:
                            erros.append(f"{onde}: lacuna de atributo desconhecido '{a}'")
                            continue
                        if t and t not in ctx.trad:
                            erros.append(f"{onde}: lacuna com tradição desconhecida '{t}'")
                            continue
                        existentes = [r["id"] for r in ctx.regs.values()
                                      if r["orixa"] == oid and r["atributo"] == a and r["status"] in LIDO
                                      and (not t or t in r["tradicoes"])]
                        if existentes:
                            erros.append(f"{onde}: lacuna falsa — {a}{'@' + t if t else ''} tem registro(s) {', '.join(existentes[:4])}")
                        corpus += [ROTULO_ATRIBUTO[a], a.replace("_", " "), ctx.trad.get(t, {}).get("nome", "") if t else ""]
                    else:
                        anc = re.sub(r"\s+", " ", m["ancora"]).strip()
                        if len(anc) < 6 or norm(anc) not in norm(re.sub(r"\s+", " ", ctx.pendencias)):
                            erros.append(f"{onde}: pendência “{anc}” não está em docs/pesquisa/PENDENCIAS.md")
                        corpus.append(ctx.pendencias)
                for t in tks:
                    if t["t"] == "link":
                        ok = {
                            "ita": lambda a: a in ctx.itans and any(v["status"] in LIDO for v in ctx.itans[a]["versoes"]),
                            "orixa": lambda a: a in ctx.fichas,
                            "glossario": lambda a: a in ctx.glos,
                            "tradicao": lambda a: a in ctx.trad,
                            "grafo": lambda a: a in ctx.nos,
                        }[t["tipo"]](t["alvo"])
                        if not ok:
                            erros.append(f"{onde}: link {t['tipo']}:{t['alvo']} aponta para item inexistente ou não publicado")
                        corpus.append(ctx.corpus_link(t))
                txt = cap.texto_simples(tks)
                if not txt or not marc:
                    continue
                idx = indice_corpus(" ".join(corpus))
                faltam = sorted({c for c in candidatos(txt, ctx) if not casa(c, idx) and not casa(c, nome_orixa)})
                if faltam:
                    erros.append(f"{onde}: heurística — {', '.join(faltam)} não aparece(m) nos registros citados no trecho “{txt[:70]}…”")
                # cópia do fichamento (rótulos de link ficam de fora: são títulos já conferidos)
                ws = palavras(cap.texto_simples([t for t in tks if t["t"] != "link"]))
                for g in ngramas(ws, 8):
                    if g in grams8 and not eh_referencia(g):
                        erros.append(f"{onde}: 8+ palavras iguais a {grams8[g]}: “{g}”")
                        break
                else:
                    for g in sorted(ngramas(ws, 6)):
                        if g in grams6 and not eh_referencia(g):
                            avisos.append(f"{onde}: 6–7 palavras iguais a {grams6[g]}: “{g}”")
                            break
            # divergências: cada versão citada vem com tradição, casa ou autor
            for r in refs_par:
                if r["id"] not in ctx.divergente:
                    continue
                ids = []
                for t in r["tradicoes"]:
                    ids += [w for w in palavras(ctx.trad.get(t, {}).get("nome", "")) if len(w) >= 4 and w not in STOP]
                    ids += [w for w in palavras(t.replace("_", " ")) if len(w) >= 4]
                ids += [w for w in palavras(r.get("casa_ou_regiao") or "") if len(w) >= 4 and w not in STOP]
                for fid in (r["source_id"], r.get("via_source_id")):
                    fo = ctx.catalogo.get(fid) if fid else None
                    for a in (fo or {}).get("autores") or []:
                        ids.append(norm(a.split()[-1].strip("().,")))
                if not any(re.search(rf"\b{re.escape(w)}", ntexto) for w in ids):
                    erros.append(f"{onde}: {r['id']} é versão divergente de {ctx.divergente[r['id']][1]} e o parágrafo não nomeia tradição, casa ou autor")
            # Candomblé × Umbanda
            trads = [set(r["tradicoes"]) for r in refs_par]
            so_umb = any(t == {"umbanda"} for t in trads)
            so_cand = any("umbanda" not in t and any(x.startswith("candomble") for x in t) for t in trads)
            tem_umbanda |= any("umbanda" in t for t in trads)
            if so_umb and "umband" not in ntexto:
                erros.append(f"{onde}: cita registro só de Umbanda sem dizer 'Umbanda'")
            # registro marcado com as duas tradições é generalização da fonte; "mistura" é
            # citar no mesmo parágrafo um registro só de Umbanda e outro só de Candomblé
            if so_umb and so_cand and not ("umband" in ntexto and re.search(r"candombl|ketu|jeje|angola|nag[oô]", ntexto)):
                erros.append(f"{onde}: mistura registros de Umbanda e de Candomblé sem nomear os dois")
            # fontes C antigas: documento histórico
            for r in refs_par:
                fo = ctx.catalogo.get(r["source_id"], {})
                if fo.get("confiabilidade_preliminar") != "C":
                    continue
                sob = [norm(a.split()[-1].strip("().,")) for a in fo.get("autores") or []]
                ano = str(fo.get("ano") or "")
                if not (any(s and s in ntexto for s in sob) or (ano and ano in ntexto)):
                    erros.append(f"{onde}: {r['id']} vem de fonte C ({r['source_id']}) e o parágrafo não nomeia o autor nem o ano")
                if ano.isdigit() and int(ano) < 1950 and not any(norm(h) in ntexto for h in HISTORICO):
                    erros.append(f"{onde}: {r['id']} vem de documento antigo de confiabilidade C ({r['source_id']}, {ano}) e o parágrafo não o marca como documento histórico")

    # seção de tradições distingue Candomblé e Umbanda
    if tem_umbanda:
        sec = next((s for s in est["secoes"] if s["slug"] == "tradicoes"), None)
        txt = norm(" ".join(cap.texto_simples(b["tokens"]) for b in (sec or {"blocos": []})["blocos"] if b["tipo"] == "paragrafo"))
        if not ("umband" in txt and "candombl" in txt):
            erros.append(f"{rot}: a seção {{#tradicoes}} precisa distinguir Candomblé e Umbanda (o capítulo cita registros de Umbanda)")
    # status revisado só com todos os registros revisados
    if f.get("status") == "revisado" and any(ctx.regs[i]["status"] != "revisado" for i in citados):
        erros.append(f"{rot}: status 'revisado' exige que todos os registros citados estejam 'revisado'")
    # divergências narradas pela metade
    for (o, a), vs in ctx.versoes_div.items():
        if o == oid:
            usados = vs & citados
            if len(usados) == 1:
                avisos.append(f"{rot}: só uma versão de {a} citada ({next(iter(usados))}); a divergência tem {len(vs)} versões")
    return est, citados


def validar(raiz=RAIZ, gerar=False, saida=print):
    ctx = Ctx(raiz)
    erros, avisos = [], []
    grams8, grams6 = {}, {}
    for r in ctx.regs.values():
        for campo in ("valor", "parafrase", "nota"):
            ws = palavras(r.get(campo) or "")
            for g in ngramas(ws, 8):
                grams8.setdefault(g, f"{r['id']}.{campo}")
            for g in ngramas(ws, 6):
                grams6.setdefault(g, f"{r['id']}.{campo}")
    schema = ler(Path(raiz) / "schemas/capitulo.schema.json")
    try:
        import jsonschema
    except ImportError:
        jsonschema = None
    resumo = []
    arquivos = cap.arquivos_md(raiz)
    for p in arquivos:
        res = validar_arquivo(p, ctx, erros, avisos, grams8, grams6)
        if not res:
            continue
        est, citados = res
        js = cap.gerar_json(est)
        destino = p.with_suffix(".json")
        novo = json.dumps(js, ensure_ascii=False, indent=2) + "\n"
        if gerar:
            destino.write_text(novo, encoding="utf-8")
        elif not destino.exists() or destino.read_text(encoding="utf-8") != novo:
            erros.append(f"capitulos/{destino.name}: desatualizado — rode scripts/validar_capitulos.py --gerar")
        if jsonschema:
            for e in jsonschema.Draft202012Validator(schema).iter_errors(js):
                erros.append(f"capitulos/{destino.name}: esquema: {e.message} em {list(e.path)}")
        npar = sum(1 for s in est["secoes"] for b in s["blocos"] if b["tipo"] == "paragrafo")
        npal = sum(len(cap.texto_simples(b["tokens"]).split()) for s in est["secoes"] for b in s["blocos"] if b["tipo"] == "paragrafo")
        resumo.append(f"{p.stem}: {npar} parágrafos, {npal} palavras, {len(citados)} registros citados, {len(js['notas'])} notas")
    for j in (Path(raiz) / "data/capitulos").glob("*.json"):
        if not j.with_suffix(".md").exists():
            erros.append(f"capitulos/{j.name}: JSON sem .md correspondente")
    saida(f"{len(arquivos)} capítulo(s)" + (" (JSON regenerado)" if gerar else ""))
    for r in resumo:
        saida("  " + r)
    for a in avisos:
        saida(" aviso: " + a)
    if erros:
        saida(f"\n{len(erros)} erro(s):")
        for e in erros:
            saida(" - " + e)
    else:
        saida("OK")
    return erros, avisos


def main():
    erros, _ = validar(gerar="--gerar" in sys.argv)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
