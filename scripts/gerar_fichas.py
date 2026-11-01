#!/usr/bin/env python3
"""Gera as fichas (data/orixas/<id>.json) e o grafo (data/conexoes.json)
a partir do fichamento (data/fichamento/<id>.json).

- Gera ficha para TODA entidade de data/entidades.json com ao menos um
  registro 'fichado'/'revisado' (orixá, qualidade, divindade suprema, conceito
  cosmológico ou ancestral). O rótulo vem da lista-mestra. Ficha de entidade que
  deixou de ter registro lido é apagada.
- Atualiza `status_conteudo` em data/entidades.json (sem_fichamento, pre, fichado).
- Sincroniza data/itans.json: versões espelhadas de um registro (campo
  `registro`) recebem valor, resumo (= paráfrase), tradições, casa, fontes, nota
  e status do registro; `arestas` de cada itã = arestas do grafo sustentadas por
  registros do itã. Título, entidades e odu são editados à mão.

Regras:
- Usa SOMENTE registros com status 'fichado' ou 'revisado'. Registros
  'pre_fichamento' (não lidos na fonte) nunca entram na ficha nem no grafo.
- Cada registro vira uma versão {valor, tradicoes, casa_ou_regiao, sources,
  source_id, via_source_id, localizacao, ...}. Divergências aparecem como
  várias versões do mesmo atributo, sem hierarquia.
- Atributos em RETIDOS (tabus, alimentos) ficam fora da ficha pública até
  decisão do conselho consultivo; são listados em pendencias.
- Revisão (scripts/revisao.py): a versão leva o status EFETIVO ('revisado' só
  com aprovação vigente) e, quando houver, `revisoes` com o resumo das revisões
  vigentes, sem dados pessoais. 'contestado' não remove a versão; 'nao_publicar'
  a tira da ficha pública e a lista em pendencias.retidos_ate_conselho. O campo
  `revisao` da ficha agrega revisor × tradição.
- Arestas do grafo vêm do mapa manual data/conexoes_alvos.json (leitura
  estruturada do 'valor' de registros de parentesco/equivalencias/sincretismo).

Não editar as saídas à mão: corrigir o fichamento (ou o mapa) e regenerar.
Uso: python3 scripts/gerar_fichas.py
"""
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import entidades as ent  # noqa: E402
import revisao  # noqa: E402

REVISORES = revisao.por_id(revisao.carregar_revisores(RAIZ))
SCHEMA_FICH = json.loads((RAIZ / "schemas" / "fichamento.schema.json").read_text(encoding="utf-8"))
ATRIBUTOS = SCHEMA_FICH["properties"]["atributo"]["enum"]
ROTULOS = {e["id"]: e["rotulo"] for e in ent.lista(RAIZ)}
STATUS_OK = ("fichado", "revisado")
RETIDOS = ("tabus", "alimentos")  # ver docs/ESTADO.md, decisão sobre tabus e alimentos
ATRS_GRAFO = ("parentesco", "equivalencias", "sincretismo")
SUBTIPOS_SIMETRICOS = {"irmao_de", "conjuge_de"}
TIPOS_SIMETRICOS = {"equivalencia", "companheiro_de_culto", "rivalidade"}


def ler(p):
    return json.loads(p.read_text(encoding="utf-8"))


def escrever(p, dados):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def versao(r, tradicoes=None, revisores=None):
    revisores = REVISORES if revisores is None else revisores
    v = {
        "valor": r["valor"],
        "tradicoes": tradicoes or r["tradicoes"],
        "casa_ou_regiao": r.get("casa_ou_regiao"),
        "sources": [{"id": r["source_id"], "loc": r["localizacao"], "via": r.get("via_source_id")}],
        "source_id": r["source_id"],
        "via_source_id": r.get("via_source_id"),
        "localizacao": r["localizacao"],
        "parafrase": r["parafrase"],
        "nota": r.get("nota"),
        "registro": r["id"],
        "status": revisao.status_efetivo(r, revisores),
    }
    resumo = revisao.resumo_publico(r, revisores)
    if resumo:  # sem revisão, a versão fica igual à de antes do campo existir
        v["revisoes"] = resumo
    return v


def agregar_revisao(atributos):
    """Uma entrada por revisor × tradição, com a data mais recente."""
    agg = {}
    for vs in atributos.values():
        for v in vs:
            for rv in v.get("revisoes", []):
                e = agg.setdefault((rv["revisor"], rv["tradicao"]),
                                   {"revisor_id": rv["revisor"], "tradicao": rv["tradicao"], "data": rv["data"], "versoes": 0})
                e["data"] = max(e["data"], rv["data"])
                e["versoes"] += 1
    return sorted(agg.values(), key=lambda e: (e["revisor_id"], e["tradicao"]))


def gerar_ficha(orixa, regs, revisores=None):
    revisores = REVISORES if revisores is None else revisores
    usados = [r for r in regs if r["status"] in STATUS_OK]
    pre = [r for r in regs if r["status"] not in STATUS_OK]
    atributos, retidos = {}, {}
    for a in ATRIBUTOS:
        doa = [r for r in usados if r["atributo"] == a]
        if not doa:
            continue
        if a in RETIDOS:
            retidos[a] = [r["id"] for r in doa]
            continue
        # parecer nao_publicar: fica fora da ficha pública, mas listado (não apagado)
        fora = [r["id"] for r in doa if not revisao.publicavel(r, revisores)]
        if fora:
            retidos[a] = fora
        pub = [versao(r, revisores=revisores) for r in doa if revisao.publicavel(r, revisores)]
        if pub:
            atributos[a] = pub
    com_registro = {r["atributo"] for r in regs}
    so_pre = {}
    for a in ATRIBUTOS:
        if a in com_registro and not any(r["atributo"] == a for r in usados):
            so_pre[a] = [r["id"] for r in pre if r["atributo"] == a]
    return {
        "_meta": {
            "gerado_por": "scripts/gerar_fichas.py",
            "fichamento": f"data/fichamento/{orixa}.json",
            "aviso": "Gerado automaticamente — não editar à mão. Conteúdo ainda não revisado por praticantes/pesquisadores (status 'fichado').",
            "registros_usados": sum(len(v) for v in atributos.values()),
            "registros_pre_fichamento_excluidos": len(pre),
            "registros_retidos": sum(len(v) for v in retidos.values()),
        },
        "id": orixa,
        "rotulo": ROTULOS[orixa],
        "atributos": atributos,
        "pendencias": {
            "sem_registro": [a for a in ATRIBUTOS if a not in com_registro],
            "so_pre_fichamento": so_pre,
            "retidos_ate_conselho": retidos,
        },
        "revisao": agregar_revisao(atributos),
    }


def gerar_conexoes(todos):
    mapa = ler(RAIZ / "data" / "conexoes_alvos.json")
    nos, por_reg = mapa["nos"], mapa["registros"]
    arestas, avisos = {}, []
    usados_nos = set()
    for r in todos:
        if r["atributo"] not in ATRS_GRAFO:
            continue
        if r["status"] not in STATUS_OK:
            if r["id"] in por_reg:
                avisos.append(f"{r['id']}: está no mapa mas é '{r['status']}' — ignorado")
            continue
        if not revisao.publicavel(r, REVISORES):
            avisos.append(f"{r['id']}: parecer nao_publicar — fora do grafo")
            continue
        if r["id"] not in por_reg:
            avisos.append(f"{r['id']}: sem_mapa (registro de {r['atributo']} sem entrada em data/conexoes_alvos.json)")
            continue
        for alvo in por_reg[r["id"]]:
            tipo, sub = alvo["tipo"], alvo.get("subtipo")
            o, d = alvo.get("origem", r["orixa"]), alvo["destino"]
            for n in (o, d):
                if n not in nos:
                    avisos.append(f"{r['id']}: nó desconhecido '{n}'")
            trads = alvo.get("tradicoes")
            if trads and not set(trads) <= set(r["tradicoes"]):
                avisos.append(f"{r['id']}: tradicoes da aresta fora das do registro: {trads}")
            simetrica = tipo in TIPOS_SIMETRICOS or (tipo == "parentesco" and sub in SUBTIPOS_SIMETRICOS)
            if simetrica and o > d:
                o, d = d, o
            chave = (o, d, tipo, sub)
            if chave not in arestas:
                aid = f"{tipo}:{sub + ':' if sub else ''}{o}>{d}"
                arestas[chave] = {"id": aid, "origem": o, "destino": d, "tipo": tipo, "subtipo": sub,
                                  "direcionada": not simetrica, "versoes": []}
            arestas[chave]["versoes"].append(versao(r, trads))
            usados_nos |= {o, d}
    lista = sorted(arestas.values(), key=lambda a: a["id"])
    saida = {
        "_meta": {
            "descricao": "Gerado por scripts/gerar_fichas.py a partir do fichamento (só 'fichado'/'revisado') e de data/conexoes_alvos.json — não editar à mão. Cada aresta agrupa as versões que a sustentam, sem hierarquia. Equivalência não é identidade; sincretismo varia por casa e região.",
            "esquema": "schemas/conexao.schema.json",
            "total_nos": len(usados_nos),
            "total_arestas": len(lista),
            "por_tipo": dict(Counter(a["tipo"] for a in lista)),
        },
        "nos": [{"id": n, **nos[n]} for n in sorted(usados_nos) if n in nos],
        "arestas": lista,
    }
    return saida, avisos


TIPOS_ENTIDADE = ("vodum", "inquice", "lwa", "oricha_lucumi", "nome_fon_ou_banto")


def gerar_entidades(conexoes):
    """Fichas leves das entidades de outras tradições ligadas a orixás por
    arestas de equivalência. Tudo vem das arestas (e, portanto, dos registros
    fichados); nada é acrescentado."""
    nos = {n["id"]: n for n in conexoes["nos"]}
    ents = {}
    for a in conexoes["arestas"]:
        if a["tipo"] != "equivalencia":
            continue
        for ent, orx in ((a["origem"], a["destino"]), (a["destino"], a["origem"])):
            n = nos.get(ent)
            if not n or n["tipo"] not in TIPOS_ENTIDADE or nos.get(orx, {}).get("tipo") != "orixa":
                continue
            e = ents.setdefault(ent, {"id": ent, "rotulo": n["rotulo"], "tipo": n["tipo"],
                                      "tradicoes": [], "equivale_a": [], "versoes": []})
            e["equivale_a"].append({"orixa": orx, "aresta": a["id"]})
            e["versoes"] += a["versoes"]
    for e in ents.values():
        e["tradicoes"] = sorted({t for v in e["versoes"] for t in v["tradicoes"]})
    lista = sorted(ents.values(), key=lambda e: e["id"])
    return {
        "_meta": {
            "descricao": "Gerado por scripts/gerar_fichas.py a partir das arestas de equivalência de data/conexoes.json — não editar à mão. Fichas leves de voduns, inquices e outros nomes equivalentes. Equivalência não é identidade: cada entidade tem culto, mitos e atributos próprios na sua tradição.",
            "esquema": "schemas/entidade.schema.json",
            "aviso": "tipo 'nome_fon_ou_banto': a fonte lista o nome como usado em cultos de origem fon ou banto sem dizer qual; não classificar sem nova fonte.",
            "total": len(lista),
        },
        "entidades": lista,
    }


def atualizar_status_conteudo(por_ent):
    """Recalcula status_conteudo na lista-mestra (preserva o resto do arquivo)."""
    p = RAIZ / "data" / "entidades.json"
    dados = ler(p)
    for e in dados["entidades"]:
        e["status_conteudo"] = ent.status_conteudo(por_ent.get(e["id"], []))
    dados["_meta"]["total"] = len(dados["entidades"])
    escrever(p, dados)
    return Counter(e["status_conteudo"] for e in dados["entidades"])


ESPELHO = ("valor", "resumo", "tradicoes", "casa_ou_regiao", "sources", "nota", "status")


def espelho(r):
    """Campos de uma versão de itã que vêm do registro de fichamento."""
    return {
        "valor": r["valor"],
        "resumo": r["parafrase"],
        "tradicoes": r["tradicoes"],
        "casa_ou_regiao": r.get("casa_ou_regiao"),
        "sources": [{"id": r["source_id"], "loc": r["localizacao"], "via": r.get("via_source_id")}],
        "nota": r.get("nota"),
        "status": r["status"],
    }


def sincronizar_itans(todos, conexoes):
    p = RAIZ / "data" / "itans.json"
    if not p.exists():
        return None
    dados = ler(p)
    regs = {r["id"]: r for r in todos}
    por_registro = {}
    for a in conexoes["arestas"]:
        for v in a["versoes"]:
            por_registro.setdefault(v["registro"], set()).add(a["id"])
    for it in dados["itans"]:
        arestas = set()
        for v in it["versoes"]:
            r = regs.get(v.get("registro"))
            if r is None:
                continue
            novo = espelho(r)
            for k in ESPELHO:
                v[k] = novo[k]
            arestas |= por_registro.get(r["id"], set())
        it["arestas"] = sorted(arestas)
    dados["_meta"]["total"] = len(dados["itans"])
    escrever(p, dados)
    return dados


def main():
    todos = []
    por_ent = ent.registros_por_entidade(RAIZ)
    geradas = set()
    for o, regs in por_ent.items():
        todos += regs
        if o not in ROTULOS or not any(r["status"] in STATUS_OK for r in regs):
            continue
        geradas.add(o)
        ficha = gerar_ficha(o, regs)
        escrever(RAIZ / "data" / "orixas" / f"{o}.json", ficha)
        m = ficha["_meta"]
        print(f"{o}: {m['registros_usados']} versões em {len(ficha['atributos'])} atributos; "
              f"{m['registros_pre_fichamento_excluidos']} pre_fichamento excluídos; {m['registros_retidos']} retidos; "
              f"sem registro: {len(ficha['pendencias']['sem_registro'])}")
    for p in (RAIZ / "data" / "orixas").glob("*.json"):
        if p.stem not in geradas:
            p.unlink()
            print(f"{p.stem}: sem registro lido — ficha removida")
    cont = atualizar_status_conteudo(por_ent)
    print(f"entidades: {sum(cont.values())} na lista-mestra; status_conteudo {dict(cont)}")
    conexoes, avisos = gerar_conexoes(todos)
    escrever(RAIZ / "data" / "conexoes.json", conexoes)
    entidades = gerar_entidades(conexoes)
    escrever(RAIZ / "data" / "entidades_equivalentes.json", entidades)
    print(f"entidades_equivalentes: {entidades['_meta']['total']}")
    itans = sincronizar_itans(todos, conexoes)
    if itans is not None:
        print(f"itans: {len(itans['itans'])} itãs, {sum(len(i['versoes']) for i in itans['itans'])} versões")
    print(f"conexoes: {conexoes['_meta']['total_nos']} nós, {conexoes['_meta']['total_arestas']} arestas {conexoes['_meta']['por_tipo']}")
    for a in avisos:
        print(" aviso:", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
