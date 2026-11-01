#!/usr/bin/env python3
"""Revisão pelo conselho: regras comuns ao validador, ao gerador e ao QA do site.

Ver docs/conselho/proposta-registro-revisao.md (proposta) e
docs/conselho/como-registrar-revisao.md (passo a passo).

A revisão vive no REGISTRO de fichamento (campo opcional `revisoes`), nunca na
ficha gerada. O cadastro público de revisores fica em data/revisores.json
(esquema schemas/revisor.schema.json), só com o que o termo de consentimento
autoriza.

Uso como programa (ajuda a registrar uma revisão):
  python3 scripts/revisao.py hash <id-do-registro>      # hash atual do registro
  python3 scripts/revisao.py modelo <id> <rev-NNN> <tradicao> [parecer]
                                                        # imprime a entrada pronta para colar
"""
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Campos que entram no hash do registro (proposta, parte 1). Se algum mudar
# depois da revisão, ela fica desatualizada.
CAMPOS_HASH = ("valor", "parafrase", "tradicoes", "casa_ou_regiao", "source_id", "localizacao")
APROVACOES = ("aprovado", "aprovado_com_ressalva")
PARECERES = APROVACOES + ("contestado", "nao_publicar")
CREDITOS = ("nome_e_tradicao", "so_nome", "generico", "anonimo")
STATUS_LIDOS = ("fichado", "revisado")
VERBO = {"aprovado": "Revisado", "aprovado_com_ressalva": "Revisado com ressalva", "contestado": "Contestado"}
ANONIMO = "revisor/a anônimo/a"

RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
RE_TELEFONE = re.compile(r"\+?\d[\d\s().-]{7,}\d")


# ----------------------------------------------------------------- leitura

def ler_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def carregar_revisores(raiz=RAIZ):
    p = Path(raiz) / "data" / "revisores.json"
    return ler_json(p)["revisores"] if p.exists() else []


def por_id(revisores):
    return {r["id"]: r for r in revisores}


# ----------------------------------------------------------------- hash

def hash_registro(r):
    base = {c: r.get(c) for c in CAMPOS_HASH}
    txt = json.dumps(base, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(txt.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------- revisões de um registro

def _revogado(rev):
    return bool((rev.get("consentimento") or {}).get("revogado_em"))


def revisao_vigente(rv, r, revisores_por_id):
    """Revisão que vale para o texto atual do registro: revisor cadastrado, hash
    atual e tradição presente no registro e nas tradições do revisor."""
    rev = revisores_por_id.get(rv.get("revisor_id"))
    return bool(rev) and rv.get("hash_registro") == hash_registro(r) \
        and rv.get("tradicao") in r.get("tradicoes", []) and rv.get("tradicao") in rev.get("tradicoes", [])


def nao_publicar(r, revisores_por_id):
    """Pedido de retirada vale mesmo com hash desatualizado: retirar é a opção
    conservadora, e só o autor (depois de ouvir o conselho) desfaz."""
    return any(rv.get("parecer") == "nao_publicar" and rv.get("revisor_id") in revisores_por_id
               for rv in r.get("revisoes") or [])


def publicavel(r, revisores_por_id):
    return r["status"] in STATUS_LIDOS and not nao_publicar(r, revisores_por_id)


def status_efetivo(r, revisores_por_id):
    """'revisado' só quando o registro diz 'revisado' E há aprovação vigente.
    Revisão desatualizada (hash mudou) faz o registro voltar a 'fichado'."""
    if r["status"] != "revisado":
        return r["status"]
    ok = any(rv.get("parecer") in APROVACOES and revisao_vigente(rv, r, revisores_por_id)
             for rv in r.get("revisoes") or [])
    return "revisado" if ok else "fichado"


def resumo_publico(r, revisores_por_id):
    """Resumo sem dados pessoais copiado para a versão: só revisões vigentes e
    exibíveis (nao_publicar retira o registro, não aparece como selo)."""
    saida = []
    for rv in r.get("revisoes") or []:
        if rv.get("parecer") in VERBO and revisao_vigente(rv, r, revisores_por_id):
            saida.append({"revisor": rv["revisor_id"], "tradicao": rv["tradicao"], "data": rv["data"],
                          "parecer": rv["parecer"], "nota": rv.get("nota")})
    return sorted(saida, key=lambda x: (x["data"], x["revisor"], x["tradicao"]))


# ----------------------------------------------------------------- crédito exibido

def quem(rev):
    """Como o revisor aparece em público, conforme o consentimento."""
    if rev is None or _revogado(rev) or rev.get("credito") == "anonimo":
        return ANONIMO
    c = rev.get("credito")
    if c == "so_nome":
        return rev["nome_publico"]
    if c == "generico":
        return rev["descricao_publica"]
    return f"{rev['nome_publico']}, {rev['descricao_publica']}"


def data_br(iso):
    a, m, d = iso.split("-")
    return f"{d}/{m}/{a}"


def linha_credito(resumo, revisores_por_id, nome_tradicao):
    """Texto exibido no site para uma revisão (a mesma regra está em site/src/lib/dados.js)."""
    t = f"{VERBO[resumo['parecer']]} por {quem(revisores_por_id.get(resumo['revisor']))} " \
        f"({nome_tradicao(resumo['tradicao'])}) em {data_br(resumo['data'])}"
    return t + (f": {resumo['nota']}" if resumo.get("nota") else "")


# ----------------------------------------------------------------- validação

def _data_ok(s):
    try:
        return _dt.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def validar_revisores(revisores, trad_ids):
    """Consentimento de crédito público. Devolve lista de erros."""
    erros = []
    ids = [r.get("id") for r in revisores]
    erros += [f"revisores: id repetido {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for r in revisores:
        onde = f"revisores/{r.get('id')}"
        nome, desc, cred = r.get("nome_publico"), r.get("descricao_publica"), r.get("credito")
        cons = r.get("consentimento") or {}
        if cons.get("revogado_em"):
            if nome is not None or desc is not None:
                erros.append(f"{onde}: consentimento revogado — nome_publico e descricao_publica devem ser null")
        elif cred == "nome_e_tradicao" and not (nome and desc):
            erros.append(f"{onde}: crédito nome_e_tradicao exige nome_publico e descricao_publica")
        elif cred == "so_nome" and not (nome and desc is None):
            erros.append(f"{onde}: crédito so_nome exige nome_publico e descricao_publica null")
        elif cred == "generico" and not (desc and nome is None):
            erros.append(f"{onde}: crédito generico exige descricao_publica e nome_publico null")
        elif cred == "anonimo" and (nome is not None or desc is not None):
            erros.append(f"{onde}: crédito anonimo exige nome_publico e descricao_publica null")
        if cons.get("remover_revisoes") and not cons.get("revogado_em"):
            erros.append(f"{onde}: remover_revisoes só vale com consentimento revogado (revogado_em)")
        ini, fim = _data_ok(cons.get("data")), cons.get("revogado_em")
        if fim and (not _data_ok(fim) or (ini and _data_ok(fim) < ini)):
            erros.append(f"{onde}: revogado_em inválido ou anterior ao consentimento")
        for t in r.get("tradicoes", []):
            if t not in trad_ids:
                erros.append(f"{onde}: tradição desconhecida {t}")
        for campo in ("nome_publico", "descricao_publica"):
            v = r.get(campo) or ""
            if RE_EMAIL.search(v) or RE_TELEFONE.search(v):
                erros.append(f"{onde}: {campo} parece conter contato (e-mail/telefone) — contatos ficam fora do repositório")
    return erros


def validar_revisoes(regs, revisores, trad_ids, hoje=None):
    """Regras da proposta (parte 1). Devolve (erros, avisos)."""
    hoje = hoje or _dt.date.today()
    rp = por_id(revisores)
    erros, avisos = [], []
    for r in regs:
        revs = r.get("revisoes") or []
        rid = r.get("id")
        if revs and r["status"] not in STATUS_LIDOS:
            erros.append(f"{rid}: revisão em registro '{r['status']}' (só registros fichados podem ser revisados)")
        atual = hash_registro(r)
        vistos = set()
        for i, rv in enumerate(revs):
            onde = f"{rid}/revisoes[{i}]"
            rev = rp.get(rv.get("revisor_id"))
            chave = json.dumps(rv, sort_keys=True, ensure_ascii=False)
            if chave in vistos:
                erros.append(f"{onde}: revisão repetida")
            vistos.add(chave)
            if rev is None:
                erros.append(f"{onde}: revisor_id {rv.get('revisor_id')} não existe em data/revisores.json")
            t = rv.get("tradicao")
            if t not in trad_ids:
                erros.append(f"{onde}: tradição desconhecida {t}")
            elif t not in r.get("tradicoes", []):
                erros.append(f"{onde}: revisão em nome de '{t}', que não está nas tradições do registro (a aprovação vale só para a tradição de quem revisou)")
            if rev is not None and t not in rev.get("tradicoes", []):
                erros.append(f"{onde}: '{t}' não está nas tradições do revisor {rev['id']}")
            d = _data_ok(rv.get("data"))
            if d is None:
                erros.append(f"{onde}: data inválida")
            elif d > hoje:
                erros.append(f"{onde}: data no futuro ({rv['data']})")
            elif rev is not None:
                cons = rev.get("consentimento") or {}
                ini, fim = _data_ok(cons.get("data")), _data_ok(cons.get("revogado_em"))
                if ini and d < ini:
                    erros.append(f"{onde}: revisão anterior ao termo de consentimento de {rev['id']} ({cons['data']})")
                if fim and d > fim:
                    erros.append(f"{onde}: revisão posterior à revogação do consentimento de {rev['id']}")
            if rv.get("parecer") == "contestado" and not (rv.get("nota") or "").strip():
                erros.append(f"{onde}: parecer contestado exige nota com o motivo (parafraseado)")
            if rv.get("hash_registro") != atual:
                avisos.append(f"{onde}: revisao_desatualizada (o registro mudou depois da revisão; hash atual {atual[:15]}…)")
        aprov = [rv for rv in revs if rv.get("parecer") in APROVACOES]
        vigentes = [rv for rv in aprov if revisao_vigente(rv, r, rp)]
        if r["status"] == "revisado" and not vigentes:
            if aprov:
                avisos.append(f"{rid}: status 'revisado' só com aprovação desatualizada ou inválida — tratado como 'fichado' na geração até nova revisão")
            else:
                erros.append(f"{rid}: status 'revisado' exige ao menos uma revisão aprovada (aprovado/aprovado_com_ressalva) de revisor cadastrado, na tradição do registro")
        if r["status"] == "fichado" and vigentes:
            avisos.append(f"{rid}: tem aprovação vigente mas status 'fichado' (pode passar a 'revisado')")
        if nao_publicar(r, rp):
            avisos.append(f"{rid}: parecer nao_publicar — retirado da ficha pública (pendencias.retidos_ate_conselho)")
    return erros, avisos


def comparar_historico(regs_base, regs_atuais, revisores):
    """Revisão não apaga nada: registro com revisão não some, e revisão
    registrada não é removida nem alterada (só acrescentada). Exceção: revisor
    que revogou o consentimento e pediu a remoção (consentimento.remover_revisoes)."""
    rp = por_id(revisores)
    atuais = {r["id"]: r for r in regs_atuais}
    erros = []
    for rb in regs_base:
        revs_b = rb.get("revisoes") or []
        if not revs_b:
            continue
        ra = atuais.get(rb["id"])
        if ra is None:
            erros.append(f"{rb['id']}: registro com revisão foi removido do fichamento (revisão não apaga versões; use nota ou nao_publicar)")
            continue
        revs_a = ra.get("revisoes") or []
        for rv in revs_b:
            if rv in revs_a:
                continue
            cons = (rp.get(rv.get("revisor_id")) or {}).get("consentimento") or {}
            if cons.get("remover_revisoes") and cons.get("revogado_em"):
                continue
            erros.append(f"{rb['id']}: revisão de {rv.get('revisor_id')} em {rv.get('data')} foi removida ou alterada (revisões só se acrescentam)")
    return erros


# ----------------------------------------------------------------- CLI

def _registros(raiz=RAIZ):
    regs = []
    for p in sorted((Path(raiz) / "data" / "fichamento").glob("*.json")):
        if p.name != "divergencias.json":
            regs += ler_json(p)["registros"]
    return {r["id"]: r for r in regs}


def main(argv):
    if len(argv) < 2 or argv[0] not in ("hash", "modelo"):
        print(__doc__)
        return 2
    regs = _registros()
    r = regs.get(argv[1])
    if r is None:
        print(f"registro inexistente: {argv[1]}")
        return 1
    if argv[0] == "hash":
        print(hash_registro(r))
        return 0
    if len(argv) < 4:
        print(__doc__)
        return 2
    entrada = {"revisor_id": argv[2], "data": _dt.date.today().isoformat(), "tradicao": argv[3],
               "parecer": argv[4] if len(argv) > 4 else "aprovado",
               "aspectos": ["parafrase", "fonte", "tradicao", "tom", "publicavel"],
               "hash_registro": hash_registro(r), "nota": None}
    print(json.dumps(entrada, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
