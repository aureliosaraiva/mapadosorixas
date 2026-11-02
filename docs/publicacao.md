# Publicação do site (GitHub Pages, rascunho público)

**URL prevista:** <https://aureliosaraiva.github.io/mapadosorixas/>

**Estado (2026-11-01, sessão pages): PUBLICADO como rascunho público** em <https://aureliosaraiva.github.io/mapadosorixas/> pela [execução nº 4](https://github.com/aureliosaraiva/mapadosorixas/actions/runs/41292757137) do workflow (validadores, build, QA e deploy ok).

Histórico: as execuções nº 1–3 pararam em "Configurar Pages" (`Get Pages site failed: Not Found` / `Create Pages site failed: Resource not accessible by integration`): o `GITHUB_TOKEN` não consegue habilitar o Pages, nem com `enablement: true`, e o repositório era privado. O autor tornou o repositório público e gravou **Settings → Pages → Source: GitHub Actions**; a partir daí o deploy passou. Pela API desta sessão, `workflow_dispatch` e reexecução dão 403: as execuções vêm de push na `main` ou do botão Run workflow, pelo autor.

**Redesign (2026-11-02):** conferido na URL publicada após a [execução nº 34](https://github.com/aureliosaraiva/mapadosorixas/actions/runs/41442688455): 14 páginas com a faixa "Conteúdo em revisão por especialistas", `noindex`, sem link de issues, fonte Literata carregada, notas, mapa e busca funcionando, sem erros de rede ou JS ([relatório](pesquisa/redesign-01.md) §6).

**Conferência da URL publicada (Playwright, 2026-11-01):** Início (faixa de rascunho, aviso de versão inicial, `noindex`), ficha de Exu, grafo (Cytoscape renderizado), busca do Pagefind ("Ogum" → 5 resultados, links com o prefixo) e os 12 arquivos de Baixar dados (todos 200; `LEIAME.txt` com "licença a definir pelo autor"); nenhum erro de rede ou de JavaScript. Screenshots em [`screenshots/pages/`](screenshots/pages/).

## O que é publicado

- O site estático de `site/` (Astro + Cytoscape.js + Pagefind), com Início, Livro, Orixás, páginas de cada orixá e capítulo, Mitos, Cosmologia, Mapa de conexões, Glossário, Tradições, Fontes, Sobre (que absorveu a antiga Metodologia), Buscar e Dados abertos (só no rodapé), mais os arquivos de `/dados/`. Fontes tipográficas Literata e Inter auto-hospedadas (pacotes `@fontsource-variable`, licença OFL), sem chamadas a serviços externos.
- **Status de rascunho (redesign de 2026-11-02, [relatório](pesquisa/redesign-01.md)):** faixa discreta "Conteúdo em revisão por especialistas" no topo de **todas** as páginas (com link para Sobre → "Conteúdo em revisão"), selo com o mesmo título nas páginas dos orixás, capítulos, mitos e Livro, aviso de versão inicial no Início e no Sobre, e `<meta name="robots" content="noindex">` em todas as páginas. Não há sitemap nem `canonical`. **Sem links de issues do GitHub nem nomes ou contatos de pessoas do projeto** (o canal de correções para leigos está pendente: PENDENCIAS §3b, redesign).
- **Nada retido nem em pré-fichamento:** tabus/alimentos (`retidos_ate_conselho`) e registros `pre_fichamento` não aparecem; o fichamento bruto não é publicado. O `qa_site.py` confere isso em todos os arquivos do `dist/` antes do deploy.
- **Licença:** ainda não decidida pelo autor. O rodapé, a página Dados abertos e o `LEIAME.txt` de `/dados/` dizem "a definir pelo autor".

## Como o deploy funciona

Workflow [`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml), disparado a cada push na `main` e manualmente (`workflow_dispatch`, aba Actions → "Publicar no GitHub Pages (rascunho)" → Run workflow):

1. **build** — roda os validadores do `CLAUDE.md` (`validar_fontes`, `validar_fichamento --base`, `divergencias` + `git diff`, `gerar_fichas` + `git diff data/`, `validar_fichas`, `anticopia`), instala o site (`npm ci`), faz o build com `SITE_BASE=/mapadosorixas` e roda `scripts/qa_site.py` (versões × dados, pré-fichamento/retidos, selo, faixa de rascunho, `noindex`, links e âncoras com o prefixo, downloads). Qualquer falha impede a publicação. Depois `actions/configure-pages` (com `enablement: true`, que tenta habilitar o Pages se ainda não estiver) e `actions/upload-pages-artifact` com `site/dist`.
2. **deploy** — `actions/deploy-pages` no ambiente `github-pages`.

Permissões: `contents: read`, `pages: write`, `id-token: write`; `concurrency: pages` (um deploy por vez, sem cancelar o que está em andamento). O workflow `validar.yml` continua rodando à parte em push e PR.

### Prefixo (base path)

- `site/astro.config.mjs`: `site: https://aureliosaraiva.github.io` e `base: /mapadosorixas` (padrão). `SITE_BASE=/` serve na raiz (domínio próprio); `SITE_URL` troca a origem.
- Todos os links internos, assets, `/dados/`, o Pagefind e os links dos nós do grafo passam por `url()` (`site/src/lib/dados.js`), que aplica o prefixo.
- `scripts/qa_site.py`, `site/scripts/acessibilidade.cjs` e `site/scripts/screenshots.cjs` usam o mesmo padrão (`SITE_BASE`, default `/mapadosorixas`). O QA acusa como quebrado qualquer link absoluto fora do prefixo, e o servidor do teste de acessibilidade responde 404 fora do prefixo.
- Conferido localmente em 2026-11-01: QA ok (285/285 versões, 14 páginas, 2424 links internos, 0 vazamentos), axe-core sem violações em 14 páginas × 2 larguras, testes da revisão e e2e ok.

## Primeira publicação (passos do autor)

1. ~~Autorizar o push~~ (feito em 2026-11-01). **Todos os passos abaixo foram feitos; ficam como referência para um repositório novo.**
2. ~~**Repositório privado:**~~ (feito: repositório público em 2026-11-01) em conta pessoal, o Pages para repositório privado exige GitHub Pro. Escolher: (a) tornar o repositório público (Settings → General → Danger Zone → Change visibility) ou (b) assinar o Pro. Atenção: mesmo com o repositório privado, **o site do Pages é público** (só o Enterprise Cloud permite Pages privado), e o link "issues do repositório" que o site exibe só funciona para quem tem acesso ao repo — com o repo privado, o canal de correções não funciona para o público.
3. ~~**Habilitar o Pages:**~~ (feito pelo autor em 2026-11-01) **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. ~~Rodar de novo~~ (feito: execução nº 4): **Actions → "Publicar no GitHub Pages (rascunho)" → Run workflow** (branch `main`).
5. Conferir a URL; a sessão seguinte salva screenshots em `docs/screenshots/pages/` (`BASE=https://aureliosaraiva.github.io/mapadosorixas node site/scripts/screenshots.cjs`, ajustando a pasta de saída).

## Como reverter ou despublicar

- **Voltar a uma versão anterior:** reverter o commit na `main` (`git revert <sha>` e push) — o workflow publica de novo. Ou, em Actions, abrir uma execução antiga bem-sucedida e usar "Re-run all jobs" (republica aquele commit).
- **Pausar os deploys:** Actions → workflow → "…" → Disable workflow (o site atual continua no ar).
- **Despublicar:** Settings → Pages → "Unpublish site" (ou trocar Source para "None"/desabilitar o Pages). Remover/desabilitar o workflow para que o próximo push não publique de novo.
- **Retirar um conteúdo específico com urgência** (ex.: algo que não deveria ser público): marcar o registro como retido/`nao_publicar` no fichamento, regenerar (`scripts/gerar_fichas.py`) e fazer push; ou despublicar enquanto isso.

## O que falta

| Item | Situação |
|---|---|
| Licença de código, textos e dados | **a definir pelo autor**; até lá, "licença a definir" no site e nos dados |
| Domínio próprio | a escolher (`.org`/`.com`; ver PENDENCIAS §3b). Ao apontar: `SITE_BASE=/` e `SITE_URL=https://<domínio>` no workflow, arquivo `CNAME` em `site/public/` e domínio em Settings → Pages |
| Revisão por praticantes e pesquisadores | conselho ainda a formar (PENDENCIAS §3c). Só depois retirar a faixa de rascunho e o `noindex` |
| Créditos e autoria na página Sobre | a confirmar pelo autor (PENDENCIAS §3b) |

## Observações

- O runner avisou que `actions/checkout@v4`, `setup-node@v4`, `setup-python@v5` e `configure-pages@v5` usam Node.js 20 (descontinuado; hoje forçados a Node 24). Funciona, mas vale atualizar as versões das actions quando houver nova major (vale também para `validar.yml`).
