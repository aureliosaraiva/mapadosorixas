// Renderiza as ilustrações em PNG (claro/escuro, grande/pequeno) para revisão.
// Uso: node site/scripts/ilustracoes/renderizar.cjs <pasta-saida> [ids...]
// Monta uma página local com o CSS do site (variáveis --il-*), sem servidor.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const raiz = path.resolve(__dirname, '..', '..', '..');
const dir = path.join(raiz, 'site', 'src', 'assets', 'ilustracoes');
const css = fs.readFileSync(path.join(raiz, 'site', 'src', 'styles', 'global.css'), 'utf8');
const saida = path.resolve(process.argv[2] || 'ilustracoes-png');
const ids = process.argv.slice(3).length ? process.argv.slice(3)
  : fs.readdirSync(dir).filter((f) => f.endsWith('.svg')).map((f) => f.slice(0, -4)).sort();
fs.mkdirSync(saida, { recursive: true });

function pagina(tema, tam) {
  const figs = ids.map((id) => `<figure><div class="il-caixa" style="width:${tam}px">${fs.readFileSync(path.join(dir, id + '.svg'), 'utf8')}</div><figcaption>${id}</figcaption></figure>`).join('');
  return `<!doctype html><html lang="pt-BR" data-tema="${tema}"><head><meta charset="utf-8"><style>${css}
  body{padding:16px;display:block} .g{display:flex;flex-wrap:wrap;gap:${tam > 100 ? 24 : 12}px}
  figure{margin:0;text-align:center;font:12px sans-serif;color:var(--texto-2)} .il-caixa svg{display:block;width:100%;height:auto;color:var(--texto)}
  </style></head><body><div class="g">${figs}</div></body></html>`;
}

(async () => {
  const b = await chromium.launch();
  for (const tema of ['claro', 'escuro']) {
    for (const [nome, tam] of [['grande', 320], ['pequeno', 72]]) {
      const p = await b.newPage({ viewport: { width: tam > 100 ? 1100 : 900, height: 400 }, deviceScaleFactor: 2 });
      await p.setContent(pagina(tema, tam));
      const arq = path.join(saida, `galeria-${nome}-${tema}.png`);
      await p.screenshot({ path: arq, fullPage: true });
      console.log(arq);
      await p.close();
    }
  }
  await b.close();
})();
