#!/usr/bin/env python3
"""Teste ponta a ponta do modelo 2 (lista-mestra, fichamento genérico, itãs,
cosmologia): dados sintéticos numa CÓPIA do repositório → gerador → validadores
→ build → qa_site.py. Nada é escrito em data/ do repositório.

Cenários:
- registro sintético 'hierarquia' em Exu (fichado) → aparece na Cosmologia;
- entidade não-orixá (olodumare) com um registro fichado e um em pré-fichamento →
  ficha gerada em data/orixas/olodumare.json, cartão do catálogo com link,
  status_conteudo 'fichado'; o texto do pré-fichamento não aparece no site;
- entidade sensível (iyami) só com pré-fichamento → status 'pre', cartão "Em
  pesquisa" com aviso de tema sensível, sem ficha;
- itã com versão própria em pré-fichamento → fora da página e do download;
- adulterações no HTML (cartão em pesquisa com texto, aviso da Cosmologia de volta
  com versões, resumo de itã trocado) → o QA acusa.

Uso: python3 tests/e2e_modelo2_site.py   (precisa de site/node_modules)
"""
import json
import re
import sys
import shutil
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e2e_revisao_site import RAIZ, copiar_repo, escrever, ler, rodar  # noqa: E402

PRE = "SINTETICO texto de pre fichamento que nunca pode aparecer"


def injetar(raiz: Path):
    p = raiz / "data/fichamento/exu.json"
    d = ler(p)
    r0 = next(r for r in d["registros"] if r["status"] == "fichado")
    base = {k: v for k, v in r0.items() if k != "revisoes"}
    d["registros"].append({**base, "id": "exu-999", "atributo": "hierarquia", "valor": "SINTETICO hierarquia de Exu",
                           "parafrase": "SINTETICO paráfrase de hierarquia em Exu", "nota": None})
    escrever(p, d)
    escrever(raiz / "data/fichamento/olodumare.json", {"registros": [
        {**base, "id": "olodumare-001", "orixa": "olodumare", "atributo": "hierarquia", "valor": "SINTETICO valor olodumare",
         "parafrase": "SINTETICO paráfrase olodumare", "nota": None},
        {**base, "id": "olodumare-002", "orixa": "olodumare", "atributo": "nomes", "valor": "SINTETICO pre olodumare",
         "parafrase": PRE, "nota": None, "status": "pre_fichamento"}]})
    escrever(raiz / "data/fichamento/iyami.json", {"registros": [
        {**base, "id": "iyami-001", "orixa": "iyami", "atributo": "nomes", "valor": "SINTETICO pre iyami",
         "parafrase": PRE + " (iyami)", "nota": None, "status": "pre_fichamento"}]})
    it = raiz / "data/itans.json"
    d = ler(it)
    d["itans"][0]["versoes"].append({"registro": None, "valor": "SINTETICO versão não lida", "resumo": PRE + " (itã)",
                                     "tradicoes": ["candomble_ketu"], "casa_ou_regiao": None, "odu": None,
                                     "sources": [{"id": r0["source_id"], "loc": "a conferir", "via": None}],
                                     "nota": None, "status": "pre_fichamento"})
    escrever(it, d)


def main():
    if not (RAIZ / "site" / "node_modules").exists():
        raise SystemExit("site/node_modules ausente: rode antes `cd site && npm ci`")
    with tempfile.TemporaryDirectory(prefix="e2e-modelo2-") as tmp:
        raiz = Path(tmp)
        copiar_repo(raiz)
        injetar(raiz)
        shutil.rmtree(raiz / "data/capitulos", ignore_errors=True)  # capítulos não são o assunto deste teste
        py = sys.executable
        rodar([py, "scripts/gerar_fichas.py"], raiz)
        rodar([py, "scripts/divergencias.py"], raiz)
        rodar([py, "scripts/validar_fichamento.py", "--sem-historico"], raiz)
        rodar([py, "scripts/validar_fichas.py"], raiz)
        rodar([py, "scripts/anticopia.py"], raiz)
        ents = {e["id"]: e for e in ler(raiz / "data/entidades.json")["entidades"]}
        assert ents["olodumare"]["status_conteudo"] == "fichado", ents["olodumare"]
        assert ents["iyami"]["status_conteudo"] == "pre", ents["iyami"]
        assert (raiz / "data/orixas/olodumare.json").exists() and not (raiz / "data/orixas/iyami.json").exists()
        ol = ler(raiz / "data/orixas/olodumare.json")
        assert ol["rotulo"] == ents["olodumare"]["rotulo"] and list(ol["atributos"]) == ["hierarquia"], ol["atributos"].keys()

        rodar(["npm", "run", "build"], raiz / "site")
        r = rodar([py, "scripts/qa_site.py"], raiz)
        n_hier = sum(len(ler(f)["atributos"].get("hierarquia", [])) for f in (raiz / "data/orixas").glob("*.json"))
        assert n_hier >= 2 and f"cosmologia: {n_hier} versões de hierarquia" in r.stdout, r.stdout[-800:]
        dist = raiz / "site/dist"
        cat = (dist / "catalogo/index.html").read_text(encoding="utf-8")
        assert re.search(r'id="e-olodumare"[^>]*>.*?orixas/olodumare', cat, re.S), "cartão de olodumare sem link"
        assert "Tema sensível" in cat.split('id="e-iyami"', 1)[1].split("</li>", 1)[0]
        for pag in dist.rglob("*.html"):
            assert PRE not in pag.read_text(encoding="utf-8"), f"pré-fichamento em {pag}"
        assert PRE not in (dist / "dados/itans.json").read_text(encoding="utf-8")

        # adulterações → o QA precisa acusar
        casos = [
            ("catalogo/index.html", '<p class="tipo-entidade">Ancestrais</p><h2>Iyami</h2>', '<p class="tipo-entidade">Ancestrais</p><h2>Iyami</h2><p>texto inventado</p>', "cartão em pesquisa com texto"),
            ("cosmologia/index.html", '<h2 id="versoes-hierarquia">O que cada obra diz</h2>', '<h2 id="versoes-hierarquia">O que cada obra diz</h2><p id="aviso-sem-hierarquia">x</p>', "aviso de estrutura vazia"),
            # linguagem para leigos: jargão e códigos internos na interface
            ("catalogo/index.html", "<h1>", '<p>Abra uma <a href="https://github.com/x/y/issues">issue</a></p><h1>', "instrução do GitHub"),
            ("catalogo/index.html", "<h1>", "<p>Registro olodumare-001, status pre_fichamento.</p><h1>", "código interno de registro"),
            ("itans/ita-002/index.html", 'class="resumo">', 'class="resumo">ADULTERADO ', "resumo difere"),
        ]
        for rel, de, para, msg in casos:
            arq = dist / rel
            orig = arq.read_text(encoding="utf-8")
            assert de in orig, f"marcador ausente em {rel}: {de}"
            arq.write_text(orig.replace(de, para, 1), encoding="utf-8")
            r = rodar([py, "scripts/qa_site.py"], raiz, esperado=None)
            assert r.returncode != 0 and msg in r.stdout, f"QA não acusou '{msg}':\n{r.stdout[-1500:]}"
            arq.write_text(orig, encoding="utf-8")
    print("e2e modelo 2: OK")


if __name__ == "__main__":
    main()
