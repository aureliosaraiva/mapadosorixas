// @ts-check
import { defineConfig } from 'astro/config';

// Publicação: GitHub Pages em https://aureliosaraiva.github.io/mapadosorixas/ (ver docs/publicacao.md).
// SITE_BASE troca o subcaminho (SITE_BASE=/ para servir na raiz, ex.: domínio próprio);
// SITE_URL troca a origem. scripts/qa_site.py usa o mesmo padrão de SITE_BASE.
const BASE = (process.env.SITE_BASE ?? '/mapadosorixas') || '/';
export default defineConfig({
  output: 'static',
  site: process.env.SITE_URL || 'https://aureliosaraiva.github.io',
  base: BASE,
  trailingSlash: 'ignore',
  build: { format: 'directory' },
  vite: {
    // os dados ficam na raiz do repositório, fora de site/
    server: { fs: { allow: ['..'] } },
  },
});
