// Screenshots do redesign (antes/depois), desktop e celular, servindo dist/ localmente
// sob o prefixo do build (SITE_BASE, padrão /mapadosorixas) ou de uma URL (BASE=...).
// Uso: npm run build && node scripts/screenshots-redesign.cjs depois
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const ROTULO = process.argv[2] || 'depois';
const DIST = path.resolve(__dirname, '../dist');
const SAIDA = path.resolve(__dirname, '../../docs/screenshots/redesign');
const PREFIXO = ((process.env.SITE_BASE ?? '/mapadosorixas') || '/').replace(/\/$/, '');
const TIPOS = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.wasm': 'application/wasm' };
const PAGINAS = [
  ['inicio', '/'],
  ['orixas', '/catalogo/'],
  ['orixa-xango', '/orixas/xango/'],
  ['capitulo-ogum', '/orixas/ogum/capitulo/'],
  ['livro', '/livro/'],
  ['mitos', '/itans/'],
  ['mapa', '/grafo/'],
  ['sobre', '/sobre/'],
  ['fontes', '/fontes/'],
];

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
  for (const [larg, alt, suf, esquema] of [[1280, 900, 'desktop', 'light'], [390, 844, 'celular', 'light'], [1280, 900, 'desktop-escuro', 'dark']]) {
    const page = await browser.newPage({ viewport: { width: larg, height: alt }, colorScheme: esquema });
    for (const [nome, p] of PAGINAS) {
      if (esquema === 'dark' && !['inicio', 'capitulo-ogum', 'orixa-xango'].includes(nome)) continue;
      await page.goto(base + p, { waitUntil: 'networkidle' });
      await page.waitForTimeout(nome === 'mapa' ? 1500 : 300);
      // página inteira até 3000 px de altura (as longas são cortadas)
      const h = await page.evaluate(() => document.documentElement.scrollHeight);
      await page.screenshot({ path: `${SAIDA}/${ROTULO}-${nome}-${suf}.jpg`, type: "jpeg", quality: 55, clip: { x: 0, y: 0, width: larg, height: Math.min(h, 3000) }, fullPage: true });
    }
    await page.close();
  }
  await browser.close();
  if (srv) srv.close();
  console.log(`screenshots "${ROTULO}" em ${SAIDA}`);
})();
