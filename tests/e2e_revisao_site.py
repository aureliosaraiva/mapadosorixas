#!/usr/bin/env python3
"""Teste ponta a ponta da revisão: dados sintéticos → validadores → gerador →
build do site → qa_site.py.

Nada é escrito em data/ do repositório. O script copia o repositório para uma
pasta temporária, acrescenta NA CÓPIA revisores fictícios e revisões
sintéticas (ids rev-9xx), regenera as fichas, compila o site e roda o QA.
Depois confere que o QA acusa erro quando o HTML é adulterado (selo de
rascunho de volta numa ficha revisada, linha de revisão removida, nome de
revisor anônimo exposto).

Cenários cobertos:
- ficha de Oxóssi inteira revisada (rev-901, crédito nome_e_tradicao) → sem selo;
- Exu: aprovação com ressalva (rev-903, so_nome) + contestação de outra pessoa
  (rev-902, anônimo) na mesma versão → as duas linhas aparecem, versão mantida;
- Exu: parecer nao_publicar (rev-901) → versão fora do site, listada em retidos;
- Exu: revisor que revogou o consentimento depois de revisar (rev-904) → aparece
  como "revisor/a anônimo/a";
- Exu: revisão desatualizada (hash antigo) → versão volta a 'fichado', sem linha.

Uso: python3 tests/e2e_revisao_site.py   (precisa de site/node_modules: cd site && npm ci)
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATA_REV = "2026-06-15"
TERMO = "2026-01-01"
NOME_ANONIMO_SECRETO = "Nome Que Nunca Pode Aparecer"


def rodar(cmd, cwd, esperado=0):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if esperado is not None and r.returncode != esperado:
        print(r.stdout[-4000:], r.stderr[-4000:], sep="\n")
        raise SystemExit(f"FALHOU ({r.returncode}, esperado {esperado}): {' '.join(map(str, cmd))}")
    return r


def copiar_repo(dest: Path):
    arqs = rodar(["git", "ls-files", "-co", "--exclude-standard"], RAIZ).stdout.splitlines()
    for a in arqs:
        o = RAIZ / a
        if o.is_file():
            (dest / a).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(o, dest / a)
    (dest / "site" / "node_modules").symlink_to(RAIZ / "site" / "node_modules")


def ler(p):
    return json.loads(p.read_text(encoding="utf-8"))


def escrever(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def injetar(raiz: Path):
    sys.path.insert(0, str(raiz / "scripts"))
    import revisao
    trads = [t["id"] for t in ler(raiz / "data/tradicoes.json")["tradicoes"]]

    def revisor(id_, credito, nome, desc, revogado=None):
        return {"id": id_, "credito": credito, "nome_publico": nome, "descricao_publica": desc, "tipo": "pesquisador",
                "tradicoes": trads, "consentimento": {"versao_termo": "teste", "data": TERMO, "revogado_em": revogado}}

    rp = ler(raiz / "data/revisores.json")
    rp["revisores"] = [
        revisor("rev-901", "nome_e_tradicao", "Pessoa Fictícia de Teste", "fixture sintética do e2e"),
        revisor("rev-902", "anonimo", None, None),
        revisor("rev-903", "so_nome", "Nome Fictício Só", None),
        revisor("rev-904", "nome_e_tradicao", None, None, revogado="2026-07-01"),
    ]
    escrever(raiz / "data/revisores.json", rp)

    def rev(r, rid, parecer="aprovado", nota=None, hash_=None):
        return {"revisor_id": rid, "data": DATA_REV, "tradicao": r["tradicoes"][0], "parecer": parecer,
                "aspectos": ["parafrase", "tradicao"], "hash_registro": hash_ or revisao.hash_registro(r), "nota": nota}

    # Oxóssi inteiro revisado
    p = raiz / "data/fichamento/oxossi.json"
    d = ler(p)
    for r in d["registros"]:
        if r["status"] == "fichado":
            r["status"] = "revisado"
            r["revisoes"] = [rev(r, "rev-901")]
    escrever(p, d)

    # Exu: cenários variados em registros publicáveis fora de tabus/alimentos,
    # fora do grafo e não citados na metodologia
    p = raiz / "data/fichamento/exu.json"
    d = ler(p)
    citados = set()
    for pag in (raiz / "site/src/pages").rglob("*.astro"):
        citados |= set(__import__("re").findall(r'registro="([a-z]+-\d+)"', pag.read_text(encoding="utf-8")))
    no_grafo = set(ler(raiz / "data/conexoes_alvos.json")["registros"])
    livres = [r for r in d["registros"] if r["status"] == "fichado" and r["atributo"] not in ("tabus", "alimentos")
              and r["id"] not in citados and r["id"] not in no_grafo]
    a, b, c, e = livres[:4]
    a["status"] = "revisado"
    a["revisoes"] = [rev(a, "rev-903", "aprovado_com_ressalva", "ressalva sintética do teste"),
                     rev(a, "rev-902", "contestado", "contestação sintética do teste")]
    b["revisoes"] = [rev(b, "rev-901", "nao_publicar")]
    c["status"] = "revisado"
    c["revisoes"] = [rev(c, "rev-904")]
    e["status"] = "revisado"
    e["revisoes"] = [rev(e, "rev-901", hash_="sha256:" + "0" * 64)]
    escrever(p, d)
    return {"ressalva": a["id"], "nao_publicar": b["id"], "revogado": c["id"], "desatualizado": e["id"]}


def main():
    if not (RAIZ / "site" / "node_modules").exists():
        raise SystemExit("site/node_modules ausente: rode antes `cd site && npm ci`")
    with tempfile.TemporaryDirectory(prefix="e2e-revisao-") as tmp:
        raiz = Path(tmp)
        copiar_repo(raiz)
        ids = injetar(raiz)
        py = sys.executable
        rodar([py, "scripts/gerar_fichas.py"], raiz)
        rodar([py, "scripts/divergencias.py"], raiz)
        r = rodar([py, "scripts/validar_fichamento.py", "--sem-historico"], raiz)
        assert "revisao_desatualizada" in r.stdout and "nao_publicar" in r.stdout, r.stdout[-2000:]
        rodar([py, "scripts/validar_fichas.py"], raiz)
        # o capítulo de Exu cita o registro que o revisor pediu para não publicar:
        # o validador de capítulos precisa acusar; depois os capítulos saem da cópia
        # (não são o assunto deste teste)
        r = subprocess.run([py, "scripts/validar_capitulos.py"], cwd=raiz, capture_output=True, text=True)
        if any(ids["nao_publicar"] in t for t in (raiz / "data/capitulos").glob("*.md") for t in [t.read_text(encoding="utf-8")]):
            assert r.returncode == 1 and "retido" in r.stdout, r.stdout[-2000:]
        shutil.rmtree(raiz / "data/capitulos")

        exu, oxossi = ler(raiz / "data/orixas/exu.json"), ler(raiz / "data/orixas/oxossi.json")
        vex = {v["registro"]: v for vs in exu["atributos"].values() for v in vs}
        assert all(v["status"] == "revisado" for vs in oxossi["atributos"].values() for v in vs)
        assert ids["nao_publicar"] not in vex
        assert any(ids["nao_publicar"] in xs for xs in exu["pendencias"]["retidos_ate_conselho"].values())
        assert sorted(x["parecer"] for x in vex[ids["ressalva"]]["revisoes"]) == ["aprovado_com_ressalva", "contestado"]
        assert vex[ids["desatualizado"]]["status"] == "fichado" and "revisoes" not in vex[ids["desatualizado"]]
        assert "Pessoa Fictícia" not in json.dumps(exu, ensure_ascii=False), "nome de revisor vazou para a ficha JSON"

        rodar(["npm", "run", "build"], raiz / "site")
        r = rodar([py, "scripts/qa_site.py"], raiz)
        print(r.stdout.strip().splitlines()[0])

        html_exu = (raiz / "site/dist/orixas/exu/index.html").read_text(encoding="utf-8")
        html_ox = (raiz / "site/dist/orixas/oxossi/index.html").read_text(encoding="utf-8")
        assert "Conteúdo em revisão por especialistas" not in html_exu and 'class="selo"' not in html_exu
        assert 'class="selo"' not in html_ox and "selo-revisado" in html_ox
        assert "Revisado com ressalva por Nome Fictício Só" in html_exu
        assert "Contestado por revisor/a anônimo/a" in html_exu
        assert "Pessoa Fictícia de Teste, fixture sintética do e2e" in html_ox

        # o QA precisa acusar adulterações
        casos = {
            "aviso de rascunho de volta numa ficha revisada": ("oxossi", lambda h: h.replace('<p class="selo-revisado"', '<p class="selo" role="note">Conteúdo em revisão por especialistas</p><p class="selo-revisado"', 1)),
            "linha de revisão removida": ("exu", lambda h: h.replace('class="revisao"', 'class="revisao-x"', 1)),
            "crédito trocado": ("exu", lambda h: h.replace("Nome Fictício Só", "Outro Nome", 1)),
        }
        for desc, (oid, f) in casos.items():
            arq = raiz / f"site/dist/orixas/{oid}/index.html"
            orig = arq.read_text(encoding="utf-8")
            arq.write_text(f(orig), encoding="utf-8")
            r = rodar([py, "scripts/qa_site.py"], raiz, esperado=None)
            arq.write_text(orig, encoding="utf-8")
            assert r.returncode != 0, f"QA não acusou: {desc}"
            print(f"QA acusa: {desc}")

        # nome de revisor anônimo cadastrado por engano: validador e QA acusam
        rv = ler(raiz / "data/revisores.json")
        rv["revisores"][1]["nome_publico"] = NOME_ANONIMO_SECRETO
        escrever(raiz / "data/revisores.json", rv)
        assert rodar([py, "scripts/validar_fichamento.py", "--sem-historico"], raiz, esperado=None).returncode != 0
        arq = raiz / "site/dist/orixas/exu/index.html"
        arq.write_text(arq.read_text(encoding="utf-8").replace("</main>", f"<p>{NOME_ANONIMO_SECRETO}</p></main>", 1), encoding="utf-8")
        assert rodar([py, "scripts/qa_site.py"], raiz, esperado=None).returncode != 0
        print("QA acusa: nome de revisor anônimo exposto")
    print("e2e revisão: ok")


if __name__ == "__main__":
    main()
