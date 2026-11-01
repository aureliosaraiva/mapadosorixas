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

| Página | Arquivo |
|---|---|
| Início (com busca) | `src/pages/index.astro` |
| Catálogo | `src/pages/catalogo.astro` (toda a lista-mestra `data/entidades.json`; sem ficha = "Em pesquisa", sem texto) |
| Ficha | `src/pages/orixas/[id].astro` (qualquer entidade com registro lido) |
| Itãs | `src/pages/itans/index.astro` e `src/pages/itans/[id].astro` (só versões lidas de `data/itans.json`) |
| Cosmologia | `src/pages/cosmologia.astro` (só versões do atributo `hierarquia`; sem nenhuma, aviso de estrutura vazia) |
| Grafo | `src/pages/grafo.astro` (filtros por tipo de conexão, tipo de entidade e tradição) |
| Fontes | `src/pages/fontes.astro` |
| Baixar dados | `src/pages/baixar-dados.astro` + `src/pages/dados/[...arquivo].js` (lista em `src/lib/downloads.js`; não publica o fichamento bruto) |
| Tradições | `src/pages/tradicoes.astro` (descrição só quando `com_fonte`; sem fonte, "descrição pendente de fonte") |
| Glossário | `src/pages/glossario.astro`; termos ligados nas fichas por `marcarGlossario` (`src/lib/dados.js`), `TextoGlossario.astro` e a dica `src/lib/dica-glossario.ts` |
| Sobre e créditos | `src/pages/sobre.astro` (contribuições pelas issues do repositório) |
| Metodologia e limitações | `src/pages/metodologia.astro` (cita registros via `src/components/Ref.astro`; o build falha se o registro não existir ou não estiver fichado) |
