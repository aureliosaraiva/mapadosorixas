// @ts-check
import { defineConfig } from 'astro/config';

// Deploy e domínio ainda não definidos (ver docs/pesquisa/PENDENCIAS.md).
// SITE_BASE permite publicar num subcaminho (ex.: GitHub Pages: /mapadosorixas).
export default defineConfig({
  output: 'static',
  base: process.env.SITE_BASE || '/',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
  vite: {
    // os dados ficam na raiz do repositório, fora de site/
    server: { fs: { allow: ['..'] } },
  },
});
