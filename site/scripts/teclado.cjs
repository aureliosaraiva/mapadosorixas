// Interações do redesign com teclado e toque: link "Pular para o conteúdo", menu do
// celular (abre, fecha com Esc e devolve o foco), troca de tema (e escolha lembrada),
// nota de rodapé que abre numa caixa (Enter leva o foco para ela; Esc fecha e devolve
// o foco ao número; toque abre sem sair do lugar) e índice do capítulo.
// Uso: npm run build && node scripts/teclado.cjs   (serve dist/ sob SITE_BASE)
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const DIST = path.resolve(__dirname, '../dist');
const PREFIXO = ((process.env.SITE_BASE ?? '/mapadosorixas') || '/').replace(/\/$/, '');
const TIPOS = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.woff2': 'font/woff2' };
const srv = http.createServer((req, res) => {
  let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (PREFIXO) { if (!p.startsWith(PREFIXO)) { res.writeHead(404); return res.end(); } p = p.slice(PREFIXO.length) || '/'; }
  let f = path.join(DIST, p);
  if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
  if (!fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TIPOS[path.extname(f)] || 'application/octet-stream' });
  fs.createReadStream(f).pipe(res);
});

const falhas = [];
const conferir = (ok, msg) => { console.log(`${ok ? 'ok ' : 'ERRO'} ${msg}`); if (!ok) falhas.push(msg); };

(async () => {
  srv.listen(0);
  const base = `http://localhost:${srv.address().port}${PREFIXO}`;
  const browser = await chromium.launch();
  const erros = [];

  // desktop: pular para o conteúdo, tema, nota pelo teclado
  const pg = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  pg.on('pageerror', (e) => erros.push(e.message));
  await pg.goto(`${base}/orixas/ogum/capitulo/`, { waitUntil: 'networkidle' });
  await pg.keyboard.press('Tab');
  conferir(await pg.evaluate(() => document.activeElement.classList.contains('pular')), 'Tab leva primeiro ao "Pular para o conteúdo"');
  await pg.keyboard.press('Enter');
  conferir(await pg.evaluate(() => document.activeElement.id === 'conteudo' || location.hash === '#conteudo'), 'Enter no link pula para o conteúdo');

  const nota = pg.locator('.capitulo sup.ref a').first();
  await nota.focus();
  await pg.keyboard.press('Enter');
  conferir(await pg.locator('.dica-nota').isVisible(), 'Enter num número de nota abre a caixa da nota');
  conferir(await pg.evaluate(() => document.activeElement.classList.contains('dica-nota')), 'o foco vai para a caixa da nota');
  conferir(/\(\d{4}|s\.d\./.test(await pg.locator('.dica-nota').innerText()), 'a caixa mostra autor e ano da fonte');
  await pg.keyboard.press('Escape');
  conferir(!(await pg.locator('.dica-nota').isVisible()), 'Esc fecha a caixa da nota');
  conferir(await pg.evaluate(() => document.activeElement?.closest('sup.ref') !== null), 'o foco volta ao número da nota');
  const y0 = await pg.evaluate(() => scrollY);
  await nota.click();
  conferir(await pg.locator('.dica-nota').isVisible() && Math.abs((await pg.evaluate(() => scrollY)) - y0) < 5, 'clique abre a nota sem sair do lugar');
  await pg.mouse.click(5, 300);
  conferir(!(await pg.locator('.dica-nota').isVisible()), 'clique fora fecha a nota');
  conferir(await pg.locator('#lista-indice a').first().isVisible(), 'índice lateral visível no desktop');

  const tema0 = await pg.evaluate(() => getComputedStyle(document.body).backgroundColor);
  await pg.locator('#alternar-tema').click();
  const tema1 = await pg.evaluate(() => getComputedStyle(document.body).backgroundColor);
  conferir(tema0 !== tema1 && (await pg.getAttribute('#alternar-tema', 'aria-pressed')) === 'true', 'botão troca para o tema escuro (aria-pressed)');
  await pg.goto(`${base}/`, { waitUntil: 'networkidle' });
  conferir((await pg.evaluate(() => document.documentElement.dataset.tema)) === 'escuro', 'a escolha de tema é lembrada na página seguinte');
  await pg.close();

  // celular: menu e índice recolhido
  const cel = await browser.newPage({ viewport: { width: 390, height: 844 }, hasTouch: true });
  cel.on('pageerror', (e) => erros.push(e.message));
  await cel.goto(`${base}/livro/`, { waitUntil: 'networkidle' });
  conferir(!(await cel.locator('#menu-principal').isVisible()), 'celular: menu começa recolhido');
  await cel.locator('#abrir-menu').focus();
  await cel.keyboard.press('Enter');
  conferir(await cel.locator('#menu-principal a', { hasText: 'Mitos' }).isVisible(), 'celular: botão abre o menu');
  await cel.keyboard.press('Escape');
  conferir(!(await cel.locator('#menu-principal').isVisible()) && (await cel.evaluate(() => document.activeElement.id)) === 'abrir-menu', 'celular: Esc fecha o menu e devolve o foco');
  await cel.goto(`${base}/orixas/exu/capitulo/`, { waitUntil: 'networkidle' });
  conferir(!(await cel.locator('#lista-indice').isVisible()), 'celular: índice do capítulo recolhido no topo');
  await cel.locator('.botao-indice').tap();
  conferir(await cel.locator('#lista-indice a').first().isVisible(), 'celular: botão abre o índice');
  await cel.locator('#lista-indice a').nth(1).tap();
  conferir(!(await cel.locator('#lista-indice').isVisible()), 'celular: escolher uma seção recolhe o índice');
  await cel.locator('.capitulo sup.ref a').first().tap();
  conferir(await cel.locator('.dica-nota').isVisible(), 'celular: toque no número abre a nota');
  await cel.close();

  // sem JavaScript: nota continua sendo link para o rodapé, menu visível
  const ctx = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
  const sj = await ctx.newPage();
  await sj.goto(`${base}/orixas/exu/capitulo/`);
  conferir(await sj.locator('#menu-principal a').first().isVisible(), 'sem JS: menu visível');
  await sj.locator('.capitulo sup.ref a').first().click();
  conferir(/#nota-\d+$/.test(sj.url()), 'sem JS: número da nota leva à nota no fim da página');
  await browser.close();
  srv.close();
  for (const e of erros) conferir(false, `erro de JavaScript: ${e}`);
  if (falhas.length) { console.error(`\n${falhas.length} falha(s)`); process.exit(1); }
  console.log('\nteclado e toque: ok');
})();
