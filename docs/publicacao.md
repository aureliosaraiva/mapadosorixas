# Publicação do site (GitHub Pages, rascunho público)

**URL prevista:** <https://aureliosaraiva.github.io/mapadosorixas/>

**Estado (2026-11-01, sessão pages):** configuração e workflow prontos e testados localmente com o prefixo `/mapadosorixas`. **A primeira publicação ainda não aconteceu**: o push para a `main` (que dispara o deploy) foi bloqueado pela política de permissões da sessão, por ser um deploy de produção, e aguarda autorização do autor. Ver [`pesquisa/PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §3b.

## O que é publicado

- O site estático de `site/` (Astro + Cytoscape.js + Pagefind), com as 14 páginas e os arquivos de `/dados/`.
- **Status de rascunho:** faixa "Rascunho — aguardando revisão de praticantes e pesquisadores" no cabeçalho de **todas** as páginas (com link para as issues), selo nas fichas, aviso de versão inicial em revisão no Início e no Sobre, e `<meta name="robots" content="noindex">` em todas as páginas. Não há sitemap nem `canonical`. (Um `robots.txt` em `/mapadosorixas/robots.txt` não teria efeito: buscadores só leem o da raiz do domínio, que pertence ao GitHub. O que vale é o `noindex`.)
- **Nada retido nem em pré-fichamento:** tabus/alimentos (`retidos_ate_conselho`) e registros `pre_fichamento` não aparecem; o fichamento bruto não é publicado. O `qa_site.py` confere isso em todos os arquivos do `dist/` antes do deploy.
- **Licença:** ainda não decidida pelo autor. O rodapé, a página Baixar dados e o `LEIAME.txt` de `/dados/` dizem "licença a definir pelo autor".

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

1. Autorizar o push desta sessão (ou fazer `git push origin main` com os commits locais).
2. Se o passo "Configurar Pages" falhar com "Resource not accessible by integration" / "Create Pages site failed" (o `GITHUB_TOKEN` não pode habilitar o Pages), ou se o repositório for privado num plano sem Pages: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Para repositório privado, o Pages exige plano pago (Pro/Team) ou tornar o repositório público.
3. Rodar de novo: **Actions → "Publicar no GitHub Pages (rascunho)" → Run workflow** (branch `main`).
4. Conferir a URL; a sessão seguinte salva screenshots em `docs/screenshots/pages/` (`BASE=https://aureliosaraiva.github.io/mapadosorixas node site/scripts/screenshots.cjs`, ajustando a pasta de saída).

## Como reverter ou despublicar

- **Voltar a uma versão anterior:** reverter o commit na `main` (`git revert <sha>` e push) — o workflow publica de novo. Ou, em Actions, abrir uma execução antiga bem-sucedida e usar "Re-run all jobs" (republica aquele commit).
- **Pausar os deploys:** Actions → workflow → "…" → Disable workflow (o site atual continua no ar).
- **Despublicar:** Settings → Pages → "Unpublish site" (ou trocar Source para "None"/desabilitar o Pages). Remover/desabilitar o workflow para que o próximo push não publique de novo.
- **Retirar um conteúdo específico com urgência** (ex.: algo que não deveria ser público): marcar o registro como retido/`nao_publicar` no fichamento, regenerar (`scripts/gerar_fichas.py`) e fazer push; ou despublicar enquanto isso.

## O que falta

| Item | Situação |
|---|---|
| Primeira execução do deploy | aguardando autorização do push / habilitação do Pages (PENDENCIAS §3b) |
| Licença de código, textos e dados | **a definir pelo autor**; até lá, "licença a definir" no site e nos dados |
| Domínio próprio | a escolher (`.org`/`.com`; ver PENDENCIAS §3b). Ao apontar: `SITE_BASE=/` e `SITE_URL=https://<domínio>` no workflow, arquivo `CNAME` em `site/public/` e domínio em Settings → Pages |
| Revisão por praticantes e pesquisadores | conselho ainda a formar (PENDENCIAS §3c). Só depois retirar a faixa de rascunho e o `noindex` |
| Créditos e autoria na página Sobre | a confirmar pelo autor (PENDENCIAS §3b) |
