#!/usr/bin/env python3
"""Teste ponta a ponta dos capítulos no site: dados sintéticos numa CÓPIA do
repositório → build → qa_site.py. Nada é escrito em data/ do repositório.

Cenários:
- capítulo SINTÉTICO de uma entidade sensível (iyami, que não tem capítulo real:
  ele espera o conselho) → a página do capítulo mostra o aviso 'aviso-sensivel';
  sem o aviso, o QA acusa;
- panorama da cosmologia → página /cosmologia/capitulo/, listado no Livro, com
  link a partir de /cosmologia/; sem o link, ou com link para capítulo inexistente,
  o QA acusa;
- capítulo de entidade não sensível com aviso → o QA acusa.

Uso: python3 tests/e2e_capitulos_site.py   (precisa de site/node_modules)
"""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e2e_revisao_site import RAIZ, copiar_repo, rodar  # noqa: E402

SINTETICO = """---
orixa: iyami
titulo: SINTETICO capítulo de teste
status: rascunho
atualizado: 2026-11-02
---

SINTETICO parágrafo de teste {{ref:iyami-001}}.
"""


def main():
    if not (RAIZ / "site" / "node_modules").exists():
        raise SystemExit("site/node_modules ausente: rode antes `cd site && npm ci`")
    sys.path.insert(0, str(RAIZ / "scripts"))
    import capitulos as cap
    with tempfile.TemporaryDirectory(prefix="e2e-capitulos-") as tmp:
        raiz = Path(tmp)
        copiar_repo(raiz)
        md = raiz / "data/capitulos/iyami.md"
        md.write_text(SINTETICO, encoding="utf-8")
        est, errs = cap.parse(md)
        assert not errs, errs
        (raiz / "data/capitulos/iyami.json").write_text(json.dumps(cap.gerar_json(est), ensure_ascii=False, indent=2) + "\n",
                                                         encoding="utf-8")
        assert (raiz / "data/capitulos/cosmologia.json").exists(), "panorama da cosmologia ausente"
        py = sys.executable
        rodar(["npm", "run", "build"], raiz / "site")
        r = rodar([py, "scripts/qa_site.py"], raiz)
        dist = raiz / "site/dist"
        pag = (dist / "orixas/iyami/capitulo/index.html").read_text(encoding="utf-8")
        assert 'class="aviso-sensivel' in pag, "capítulo de entidade sensível sem aviso"
        assert (dist / "cosmologia/capitulo/index.html").exists(), "panorama não gerado"
        assert 'data-capitulo="cosmologia"' in (dist / "livro/index.html").read_text(encoding="utf-8")
        print(r.stdout.strip().splitlines()[-1])

        # adulterações → o QA precisa acusar
        casos = [
            ("orixas/iyami/capitulo/index.html", 'class="aviso-sensivel', 'class="sem-aviso', "entidade sensível sem o aviso"),
            ("orixas/ogum/capitulo/index.html", "<h1>", '<p class="aviso-sensivel">x</p><h1>', "aviso de tema sensível numa entidade"),
            ("cosmologia/index.html", 'id="link-panorama"', 'id="link-panorama" hidden', None),  # marcador conferido abaixo
            ("cosmologia/capitulo/index.html", "/orixas/olodumare/capitulo", "/orixas/nao_existe/capitulo", "que não foi gerado"),
        ]
        for rel, de, para, msg in casos:
            arq = dist / rel
            orig = arq.read_text(encoding="utf-8")
            assert de in orig, f"marcador ausente em {rel}: {de}"
            if msg is None:
                continue
            arq.write_text(orig.replace(de, para, 1), encoding="utf-8")
            r = rodar([py, "scripts/qa_site.py"], raiz, esperado=None)
            assert r.returncode != 0 and msg in r.stdout, f"QA não acusou '{msg}':\n{r.stdout[-1500:]}"
            arq.write_text(orig, encoding="utf-8")
        # sem nenhum link para o panorama na página da cosmologia
        arq = dist / "cosmologia/index.html"
        orig = arq.read_text(encoding="utf-8")
        arq.write_text(orig.replace("/cosmologia/capitulo", "/cosmologia/xx"), encoding="utf-8")
        r = rodar([py, "scripts/qa_site.py"], raiz, esperado=None)
        assert r.returncode != 0 and "não linka para o panorama" in r.stdout, r.stdout[-1500:]
        arq.write_text(orig, encoding="utf-8")
    print("e2e capítulos: OK")


if __name__ == "__main__":
    main()
