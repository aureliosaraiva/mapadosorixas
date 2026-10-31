#!/usr/bin/env python3
"""Gera as fichas (data/orixas/<orixa>.json) e o grafo (data/conexoes.json)
a partir do fichamento (data/fichamento/<orixa>.json).

Regras:
- Usa SOMENTE registros com status 'fichado' ou 'revisado'. Registros
  'pre_fichamento' (não lidos na fonte) nunca entram na ficha nem no grafo.
- Cada registro vira uma versão {valor, tradicoes, casa_ou_regiao, sources,
  source_id, via_source_id, localizacao, ...}. Divergências aparecem como
  várias versões do mesmo atributo, sem hierarquia.
- Atributos em RETIDOS (tabus, alimentos) ficam fora da ficha pública até
  decisão do conselho consultivo; são listados em pendencias.
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
SCHEMA_FICH = json.loads((RAIZ / "schemas" / "fichamento.schema.json").read_text(encoding="utf-8"))
ATRIBUTOS = SCHEMA_FICH["properties"]["atributo"]["enum"]
ORIXAS = SCHEMA_FICH["properties"]["orixa"]["enum"]
ROTULOS = {"exu": "Exu", "ogum": "Ogum", "oxossi": "Oxóssi", "xango": "Xangô", "iemanja": "Iemanjá"}
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


def versao(r, tradicoes=None):
    return {
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
        "status": r["status"],
    }


def gerar_ficha(orixa, regs):
    usados = [r for r in regs if r["status"] in STATUS_OK]
    pre = [r for r in regs if r["status"] not in STATUS_OK]
    atributos, retidos = {}, {}
    for a in ATRIBUTOS:
        doa = [r for r in usados if r["atributo"] == a]
        if not doa:
            continue
        if a in RETIDOS:
            retidos[a] = [r["id"] for r in doa]
        else:
            atributos[a] = [versao(r) for r in doa]
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
        "revisao": [],
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


def main():
    todos = []
    for o in ORIXAS:
        p = RAIZ / "data" / "fichamento" / f"{o}.json"
        if not p.exists():
            continue
        regs = ler(p)["registros"]
        todos += regs
        ficha = gerar_ficha(o, regs)
        escrever(RAIZ / "data" / "orixas" / f"{o}.json", ficha)
        m = ficha["_meta"]
        print(f"{o}: {m['registros_usados']} versões em {len(ficha['atributos'])} atributos; "
              f"{m['registros_pre_fichamento_excluidos']} pre_fichamento excluídos; {m['registros_retidos']} retidos; "
              f"sem registro: {len(ficha['pendencias']['sem_registro'])}")
    conexoes, avisos = gerar_conexoes(todos)
    escrever(RAIZ / "data" / "conexoes.json", conexoes)
    print(f"conexoes: {conexoes['_meta']['total_nos']} nós, {conexoes['_meta']['total_arestas']} arestas {conexoes['_meta']['por_tipo']}")
    for a in avisos:
        print(" aviso:", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
