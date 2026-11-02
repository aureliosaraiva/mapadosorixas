// Screenshots das ilustrações no site (sessão ilustra): topo do catálogo, da página do
// orixá e da abertura do capítulo, desktop/celular, claro/escuro, servindo dist/ (ou BASE=url).
// Uso: npm run build && node scripts/screenshots-ilustracoes.cjs [ids...]   (padrão: ogum iemanja xango)
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const DIST = path.resolve(__dirname, '../dist');
const SAIDA = path.resolve(__dirname, '../../docs/screenshots/ilustracoes');
const PREFIXO = ((process.env.SITE_BASE ?? '/mapadosorixas') || '/').replace(/\/$/, '');
const TIPOS = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.wasm': 'application/wasm' };
const IDS = process.argv.slice(2).length ? process.argv.slice(2) : ['ogum', 'iemanja', 'xango'];
const PAGINAS = [['catalogo', '/catalogo/', 1400], ...IDS.flatMap((id) => [[`orixa-${id}`, `/orixas/${id}/`, 0], [`capitulo-${id}`, `/orixas/${id}/capitulo/`, 0]])];

function servidor() {
  return http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (PREFIXO) {
      if (p !== PREFIXO && !p.startsWith(PREFIXO + '/')) { res.writeHead(404); return res.end(); }
      p = p.slice(PREFIXO.length) || '/';
    }
    let f = path.join(DIST, p);
    if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
    if (!fs.existsSync(f)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': TIPOS[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  });
}

(async () => {
  let base = process.env.BASE;
  let srv;
  if (!base) { srv = servidor().listen(0); base = `http://localhost:${srv.address().port}${PREFIXO}`; }
  fs.mkdirSync(SAIDA, { recursive: true });
  const browser = await chromium.launch();
  for (const [larg, alt, suf, esquema] of [[1280, 900, 'desktop', 'light'], [1280, 900, 'desktop-escuro', 'dark'], [390, 844, 'celular', 'light'], [390, 844, 'celular-escuro', 'dark']]) {
    const page = await browser.newPage({ viewport: { width: larg, height: alt }, colorScheme: esquema });
    for (const [nome, p, extra] of PAGINAS) {
      await page.goto(base + p, { waitUntil: 'networkidle' });
      await page.waitForTimeout(200);
      // catálogo: desce até a grade de cartões
      const y = extra ? await page.evaluate(() => (document.getElementById('cartoes')?.getBoundingClientRect().top ?? 0) + scrollY - 20) : 0;
      await page.screenshot({ path: `${SAIDA}/${nome}-${suf}.jpg`, type: 'jpeg', quality: 60, clip: { x: 0, y, width: larg, height: extra && larg > 500 ? 1100 : alt }, fullPage: true });
    }
    await page.close();
  }
  await browser.close();
  if (srv) srv.close();
  console.log(`screenshots em ${SAIDA}`);
})();
