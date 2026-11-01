#!/usr/bin/env python3
"""Valida data/fichamento/*.json contra o esquema e o catálogo de fontes,
e mostra a cobertura de atributos por entidade (lacunas).

Lista-mestra (data/entidades.json, esquema schemas/entidades.schema.json):
- esquema, ids únicos, `qualidade_de` aponta para entidade existente;
- `grupo.confirmado_por` só cita registros fichados/revisados;
- cada arquivo data/fichamento/<id>.json tem <id> na lista-mestra, e cada
  registro dele tem `orixa` = <id> e id <id>-NNN.

Revisão do conselho (scripts/revisao.py; docs/conselho/como-registrar-revisao.md):
- data/revisores.json contra schemas/revisor.schema.json e as regras de
  consentimento de crédito público;
- `revisoes` de cada registro: revisor cadastrado, tradição do registro e do
  revisor, datas dentro do consentimento, 'revisado' só com aprovação vigente;
- histórico: comparado com --base REF (padrão: HEAD, se houver git), nenhum
  registro com revisão some e nenhuma revisão é removida ou alterada.

Uso: python3 scripts/validar_fichamento.py [--markdown] [--base REF | --sem-historico]
"""
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((RAIZ / "schemas" / "fichamento.schema.json").read_text(encoding="utf-8"))
CATALOGO = json.loads((RAIZ / "data" / "fontes" / "catalogo.json").read_text(encoding="utf-8"))
FONTES = {f["id"]: f for f in CATALOGO["fontes"]}
ATRIBUTOS = SCHEMA["properties"]["atributo"]["enum"]
TRAD_IDS = {t["id"] for t in json.loads((RAIZ / "data" / "tradicoes.json").read_text(encoding="utf-8"))["tradicoes"]}

sys.path.insert(0, str(RAIZ / "scripts"))
import entidades  # noqa: E402
import revisao  # noqa: E402

ENTIDADES = entidades.lista(RAIZ)
ENT_IDS = [e["id"] for e in ENTIDADES]


def carregar():
    return entidades.todos_registros(RAIZ)


def validar_entidades(regs):
    erros = []
    try:
        import jsonschema
        s = json.loads((RAIZ / "schemas" / "entidades.schema.json").read_text(encoding="utf-8"))
        erros += [f"entidades.json: {e.message} em /{'/'.join(map(str, e.path))}"
                  for e in jsonschema.Draft202012Validator(s).iter_errors(entidades.carregar(RAIZ))]
    except ImportError:
        pass
    vistos = Counter(ENT_IDS)
    erros += [f"entidades.json: id duplicado: {i}" for i, n in vistos.items() if n > 1]
    por_reg = {r["id"]: r for r in regs}
    for e in ENTIDADES:
        q = e.get("qualidade_de")
        if q and q not in vistos:
            erros.append(f"entidades/{e['id']}: qualidade_de aponta para entidade inexistente: {q}")
        if (e.get("tipo") == "qualidade") != bool(q):
            erros.append(f"entidades/{e['id']}: qualidade_de só (e sempre) para tipo 'qualidade'")
        for rid in (e.get("grupo") or {}).get("confirmado_por", []):
            r = por_reg.get(rid)
            if not r or r["status"] not in ("fichado", "revisado"):
                erros.append(f"entidades/{e['id']}: grupo confirmado por registro inexistente ou não fichado: {rid}")
    for p in entidades.arquivos_fichamento(RAIZ):
        if p.stem not in vistos:
            erros.append(f"data/fichamento/{p.name}: entidade '{p.stem}' fora de data/entidades.json")
        for r in json.loads(p.read_text(encoding="utf-8"))["registros"]:
            if r.get("orixa") != p.stem:
                erros.append(f"{r.get('id')}: campo orixa '{r.get('orixa')}' difere do arquivo {p.name}")
            if not str(r.get("id", "")).startswith(p.stem + "-"):
                erros.append(f"{r.get('id')}: id deve começar por '{p.stem}-'")
    return erros


def validar(regs):
    erros = []
    try:
        import jsonschema
        v = jsonschema.Draft202012Validator(SCHEMA)
        for r in regs:
            erros += [f"{r.get('id')}: {e.message}" for e in v.iter_errors(r)]
    except ImportError:
        pass
    ids = Counter(r["id"] for r in regs)
    erros += [f"id duplicado: {i}" for i, n in ids.items() if n > 1]
    for r in regs:
        for campo in ("source_id", "via_source_id"):
            sid = r.get(campo)
            if sid and sid not in FONTES:
                erros.append(f"{r['id']}: {campo} inexistente no catálogo: {sid}")
        # A fonte efetivamente lida é a intermediária (via_source_id), quando houver.
        lida = r.get("via_source_id") or r["source_id"]
        f = FONTES.get(lida)
        if f and r["status"] in ("fichado", "revisado"):
            if f["status_verificacao"] in ("pista", "a_verificar"):
                erros.append(f"{r['id']}: status {r['status']} exige fonte verificada (fonte está '{f['status_verificacao']}')")
            if r["localizacao"].strip().lower() == "a conferir":
                erros.append(f"{r['id']}: status {r['status']} exige localização (página)")
    return erros


def validar_revisores(revisores):
    erros = []
    try:
        import jsonschema
        s = json.loads((RAIZ / "schemas" / "revisor.schema.json").read_text(encoding="utf-8"))
        v = jsonschema.Draft202012Validator(s)
        for r in revisores:
            erros += [f"revisores/{r.get('id')}: {e.message}" for e in v.iter_errors(r)]
    except ImportError:
        pass
    return erros + revisao.validar_revisores(revisores, TRAD_IDS)


def registros_em(ref):
    """Registros do fichamento numa revisão do git, ou None se não der para ler."""
    regs = []
    try:
        subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref + "^{commit}"], cwd=RAIZ,
                       check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    r = subprocess.run(["git", "ls-tree", "--name-only", ref, "data/fichamento/"], cwd=RAIZ, capture_output=True)
    nomes = [n for n in r.stdout.decode("utf-8").split() if n.endswith(".json")
             and Path(n).name not in entidades.GERADOS_NO_FICHAMENTO]
    for n in nomes:
        r = subprocess.run(["git", "show", f"{ref}:{n}"], cwd=RAIZ, capture_output=True)
        if r.returncode == 0:
            regs += json.loads(r.stdout.decode("utf-8"))["registros"]
    return regs


def cobertura(regs, markdown=False):
    cob = defaultdict(lambda: defaultdict(int))
    for r in regs:
        cob[r["orixa"]][r["atributo"]] += 1
    ORIXAS = [i for i in ENT_IDS if i in cob]  # só entidades com algum registro
    sem = [i for i in ENT_IDS if i not in cob]
    if markdown:
        print("| atributo | " + " | ".join(ORIXAS) + " |")
        print("|---|" + "---:|" * len(ORIXAS))
        for a in ATRIBUTOS:
            print(f"| {a} | " + " | ".join(str(cob[o][a] or "—") for o in ORIXAS) + " |")
    else:
        for o in ORIXAS:
            falta = [a for a in ATRIBUTOS if not cob[o][a]]
            print(f"{o}: {sum(cob[o].values())} registros; sem registro: {', '.join(falta)}")
        print(f"lista-mestra: {len(ENT_IDS)} entidades; {len(ORIXAS)} com fichamento; "
              f"{len(sem)} sem fichamento ({', '.join(sem)})")


def main():
    regs = carregar()
    erros = validar(regs) + validar_entidades(regs)
    revisores = revisao.carregar_revisores(RAIZ)
    erros += validar_revisores(revisores)
    e_rev, avisos = revisao.validar_revisoes(regs, revisores, TRAD_IDS)
    erros += e_rev
    base = None if "--sem-historico" in sys.argv else (
        sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD")
    regs_base = registros_em(base) if base else None
    if regs_base is not None:
        erros += revisao.comparar_historico(regs_base, regs, revisores)
    elif "--base" in sys.argv:
        erros.append(f"--base {base}: revisão do git inexistente (histórico das revisões não conferido)")
    md = "--markdown" in sys.argv
    if not md:
        print(f"{len(regs)} registros; status: {dict(Counter(r['status'] for r in regs))}")
        n_rev = sum(len(r.get("revisoes") or []) for r in regs)
        print(f"revisão: {len(revisores)} revisor(es) cadastrado(s), {n_rev} revisão(ões) registrada(s); "
              + (f"histórico conferido contra {base}" if regs_base is not None else "histórico não conferido"))
    cobertura(regs, md)
    if avisos and not md:
        print(f"\n{len(avisos)} aviso(s) de revisão:")
        for a in avisos:
            print(" -", a)
    if erros:
        print(f"\n{len(erros)} erro(s):")
        for e in erros:
            print(" -", e)
        return 1
    if not md:
        print("\nOK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
