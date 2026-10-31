// Tira screenshots das páginas principais do site servido em BASE (padrão http://localhost:4321).
// Uso: npm run build && npx astro preview & node scripts/screenshots.cjs
const { chromium } = require('playwright');
const path = require('path');
const BASE = process.env.BASE || 'http://localhost:4321';
const SAIDA = path.resolve(__dirname, '../../docs/screenshots');
const paginas = [
  ['inicio', '/'],
  ['catalogo', '/catalogo/'],
  ['ficha-xango', '/orixas/xango/'],
  ['ficha-exu-divergencias', '/orixas/exu/#divergencias'],
  ['grafo', '/grafo/'],
  ['fontes', '/fontes/'],
  ['metodologia', '/metodologia/'],
  ['baixar-dados', '/baixar-dados/'],
  ['ficha-xango-conexoes', '/orixas/xango/#conexoes'],
  ['glossario', '/glossario/'],
  ['tradicoes', '/tradicoes/'],
  ['sobre', '/sobre/'],
];
(async () => {
  const browser = await chromium.launch();
  const erros = [];
  for (const [larg, alt, sufixo] of [[1280, 900, ''], [390, 844, '-mobile']]) {
    const page = await browser.newPage({ viewport: { width: larg, height: alt } });
    page.on('pageerror', (e) => erros.push(`${page.url()}: ${e.message}`));
    page.on('console', (m) => { if (m.type() === 'error') erros.push(`${page.url()}: ${m.text()}`); });
    for (const [nome, p] of paginas) {
      if (sufixo && !['inicio', 'ficha-xango', 'grafo', 'glossario', 'tradicoes'].includes(nome)) continue;
      await page.goto(BASE + p, { waitUntil: 'networkidle' });
      await page.waitForTimeout(nome === 'grafo' || nome.includes('conexoes') ? 1500 : 300);
      await page.screenshot({ path: `${SAIDA}/${nome}${sufixo}.png`, fullPage: nome !== 'grafo' && nome !== 'fontes' && !p.includes('#') });
    }
    await page.close();
  }
  // dica do glossário aberta por foco de teclado numa ficha
  {
    const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
    await page.goto(BASE + '/orixas/exu/', { waitUntil: 'networkidle' });
    const termo = page.locator('a.termo-gl').first();
    await termo.scrollIntoViewIfNeeded();
    await termo.focus();
    await page.waitForTimeout(200);
    if (!(await page.locator('.dica-gl').isVisible())) erros.push('dica do glossário não apareceu ao focar o termo');
    await page.screenshot({ path: `${SAIDA}/ficha-exu-dica-glossario.png` });
    await page.keyboard.press('Escape');
    if (await page.locator('.dica-gl').isVisible()) erros.push('dica do glossário não fechou com Esc');
    await page.close();
  }
  // sem JavaScript: o conteúdo textual precisa continuar lá
  const ctx = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 1280, height: 900 } });
  const p2 = await ctx.newPage();
  await p2.goto(BASE + '/orixas/iemanja/');
  await p2.screenshot({ path: `${SAIDA}/ficha-iemanja-sem-js.png` });
  await browser.close();
  if (erros.length) { console.error(erros.join('\n')); process.exit(1); }
  console.log('ok');
})();
