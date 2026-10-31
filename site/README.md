# Site (protótipo da Fase 5)

Site estático em [Astro](https://astro.build) que **só exibe** os dados gerados em `../data/`
(fichas, conexões, entidades, tradições, catálogo de fontes e divergências). Nada sobre orixás é
escrito aqui: para corrigir conteúdo, corrija o fichamento e rode `scripts/gerar_fichas.py`.

- Grafo: [Cytoscape.js](https://js.cytoscape.org); a mesma informação existe em tabela (funciona sem JS).
- Busca: [Pagefind](https://pagefind.app), gerada no `npm run build` (não aparece no `npm run dev`).
- Requer Node ≥ 22.23 (exigência do Astro 7).

```sh
cd site
npm ci
npm run dev        # http://localhost:4321
npm run build      # gera dist/ e o índice do Pagefind
npx astro preview  # serve dist/
node scripts/screenshots.cjs   # com o preview rodando: salva em docs/screenshots/
```

Publicação num subcaminho (ex.: GitHub Pages): `SITE_BASE=/mapadosorixas npm run build`.
Deploy e domínio ainda não estão configurados (ver `docs/pesquisa/PENDENCIAS.md`).

| Página | Arquivo |
|---|---|
| Início (com busca) | `src/pages/index.astro` |
| Catálogo | `src/pages/catalogo.astro` |
| Ficha | `src/pages/orixas/[id].astro` |
| Grafo | `src/pages/grafo.astro` |
| Fontes | `src/pages/fontes.astro` |
| Metodologia e limitações | `src/pages/metodologia.astro` (cita registros via `src/components/Ref.astro`; o build falha se o registro não existir ou não estiver fichado) |
