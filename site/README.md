# Site (protótipo da Fase 5)

Site estático em [Astro](https://astro.build) que **só exibe** os dados gerados em `../data/`
(fichas, conexões, entidades, tradições, catálogo de fontes e divergências). Nada sobre orixás é
escrito aqui: para corrigir conteúdo, corrija o fichamento e rode `scripts/gerar_fichas.py`.

- Grafo: [Cytoscape.js](https://js.cytoscape.org); a mesma informação existe em tabela (funciona sem JS). Cada ficha tem um mini-grafo dos vizinhos diretos, com a lista de conexões como alternativa. Estilos comuns em `src/lib/grafo.js` e `src/lib/estilo-cytoscape.ts`.
- Busca: [Pagefind](https://pagefind.app), gerada no `npm run build` (não aparece no `npm run dev`).
- Requer Node ≥ 22.23 (exigência do Astro 7).

```sh
cd site
npm ci
npm run dev        # http://localhost:4321
npm run build      # gera dist/ e o índice do Pagefind
npx astro preview  # serve dist/
node scripts/screenshots.cjs   # com o preview rodando: salva em docs/screenshots/
python3 ../scripts/qa_site.py  # QA de conteúdo, links/âncoras e downloads sobre dist/ (também no CI)
node scripts/acessibilidade.cjs # axe-core em todas as páginas de dist/ (servidor embutido; usa o Chromium do ambiente)
```

Publicação num subcaminho (ex.: GitHub Pages): `SITE_BASE=/mapadosorixas npm run build`.
Deploy e domínio ainda não estão configurados (ver `docs/pesquisa/PENDENCIAS.md`).

Identidade visual e linguagem: ver `docs/pesquisa/redesign-01.md` (Literata + Inter auto-hospedadas, modo claro/escuro em `src/styles/global.css`, textos para público leigo; jargão interno proibido na interface pelo `qa_site.py` §13).

| Página (rótulo no menu) | Arquivo |
|---|---|
| Início | `src/pages/index.astro` |
| Livro | `src/pages/livro.astro`; capítulo em `src/pages/orixas/[id]/capitulo.astro` e panorama em `src/pages/[panorama]/capitulo.astro`, ambos com `src/components/Capitulo.astro` (índice lateral, notas que abrem ao toque: `src/lib/notas-popover.ts`) |
| Orixás | `src/pages/catalogo.astro` (toda a lista-mestra `data/entidades.json`; sem ficha = "Em pesquisa", sem texto) |
| Página do orixá | `src/pages/orixas/[id].astro` (resumo, capítulo, "Em cada tradição", variações, mitos, conexões, o que falta, fontes) |
| Mitos | `src/pages/itans/index.astro` e `src/pages/itans/[id].astro` (só versões lidas de `data/itans.json`) |
| Cosmologia | `src/pages/cosmologia.astro` (só versões do atributo `hierarquia`; sem nenhuma, aviso de estrutura vazia) |
| Mapa de conexões | `src/pages/grafo.astro` (posições calculadas no build; filtros por tipo de relação, tipo de nome e tradição) |
| Glossário | `src/pages/glossario.astro`; termos ligados por `marcarGlossario` (`src/lib/dados.js`), `TextoGlossario.astro` e `src/lib/dica-glossario.ts` |
| Sobre | `src/pages/sobre.astro` (absorveu a antiga Metodologia; cita registros via `src/components/Ref.astro`, e o build falha se o registro não existir ou não estiver fichado) |
| Rodapé: Fontes | `src/pages/fontes.astro` |
| Rodapé: Tradições e nações | `src/pages/tradicoes.astro` (descrição só quando `com_fonte`; sem fonte, "Descrição em preparo") |
| Rodapé: Buscar | `src/pages/buscar.astro` (Pagefind) |
| Rodapé: Dados abertos | `src/pages/baixar-dados.astro` + `src/pages/dados/[...arquivo].js` (lista em `src/lib/downloads.js`; não publica o fichamento bruto) |

Testes do site (depois do build): `python3 ../scripts/qa_site.py`, `node scripts/acessibilidade.cjs` (axe), `node scripts/teclado.cjs` (teclado e toque), `node scripts/screenshots-redesign.cjs depois`.
