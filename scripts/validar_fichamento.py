#!/usr/bin/env python3
"""Valida data/fichamento/*.json contra o esquema e o catálogo de fontes,
e mostra a cobertura de atributos por orixá (lacunas).

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
ORIXAS = SCHEMA["properties"]["orixa"]["enum"]
TRAD_IDS = {t["id"] for t in json.loads((RAIZ / "data" / "tradicoes.json").read_text(encoding="utf-8"))["tradicoes"]}

sys.path.insert(0, str(RAIZ / "scripts"))
import revisao  # noqa: E402


def carregar():
    regs = []
    for o in ORIXAS:
        p = RAIZ / "data" / "fichamento" / f"{o}.json"
        if p.exists():
            regs += json.loads(p.read_text(encoding="utf-8"))["registros"]
    return regs


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
    for o in ORIXAS:
        r = subprocess.run(["git", "show", f"{ref}:data/fichamento/{o}.json"], cwd=RAIZ, capture_output=True)
        if r.returncode == 0:
            regs += json.loads(r.stdout.decode("utf-8"))["registros"]
    return regs


def cobertura(regs, markdown=False):
    cob = defaultdict(lambda: defaultdict(int))
    for r in regs:
        cob[r["orixa"]][r["atributo"]] += 1
    if markdown:
        print("| atributo | " + " | ".join(ORIXAS) + " |")
        print("|---|" + "---:|" * len(ORIXAS))
        for a in ATRIBUTOS:
            print(f"| {a} | " + " | ".join(str(cob[o][a] or "—") for o in ORIXAS) + " |")
    else:
        for o in ORIXAS:
            falta = [a for a in ATRIBUTOS if not cob[o][a]]
            print(f"{o}: {sum(cob[o].values())} registros; sem registro: {', '.join(falta)}")


def main():
    regs = carregar()
    erros = validar(regs)
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
