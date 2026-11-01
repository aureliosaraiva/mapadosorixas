// Acessibilidade básica com axe-core (WCAG 2.1 A/AA + boas práticas) em todas as
// páginas HTML de dist/, servidas por um servidor estático local embutido.
// Uso: npm run build && node scripts/acessibilidade.cjs
// Serve dist/ sob o mesmo prefixo do build (SITE_BASE, padrão /mapadosorixas, como no
// GitHub Pages): pedido fora do prefixo dá 404, então link sem base aparece como erro.
// Falha (exit 1) com violações de impacto "serious" ou "critical"; as demais são listadas.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const DIST = path.resolve(__dirname, '../dist');
const AXE = require.resolve('axe-core/axe.min.js');
const PREFIXO = ((process.env.SITE_BASE ?? '/mapadosorixas') || '/').replace(/\/$/, '');
const TIPOS = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.txt': 'text/plain; charset=utf-8', '.wasm': 'application/wasm' };

function servidor() {
  return http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    if (PREFIXO) {
      if (p !== PREFIXO && !p.startsWith(PREFIXO + '/')) { res.writeHead(404); return res.end('404 (fora do prefixo)'); }
      p = p.slice(PREFIXO.length) || '/';
    }
    let f = path.join(DIST, p);
    if (!f.startsWith(DIST)) { res.writeHead(403); return res.end(); }
    if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
    if (!fs.existsSync(f)) { res.writeHead(404); return res.end('404'); }
    res.writeHead(200, { 'Content-Type': TIPOS[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  });
}

function paginas(dir = DIST, base = '') {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    if (e.isDirectory()) return e.name === 'pagefind' || e.name === '_astro' ? [] : paginas(path.join(dir, e.name), `${base}/${e.name}`);
    return e.name === 'index.html' ? [`${base}/`] : [];
  });
}

(async () => {
  const srv = servidor().listen(0);
  const porta = srv.address().port;
  const browser = await chromium.launch();
  let graves = 0;
  const erros404 = [];
  for (const [larg, alt] of [[1280, 900], [390, 844]]) {
    const page = await browser.newPage({ viewport: { width: larg, height: alt } });
    page.on('response', (r) => { if (r.status() >= 400) erros404.push(`${r.status()} ${r.url()}`); });
    page.on('pageerror', (e) => erros404.push(`erro JS em ${page.url()}: ${e.message}`));
    for (const p of paginas()) {
      await page.goto(`http://localhost:${porta}${PREFIXO}${p}`, { waitUntil: 'networkidle' });
      await page.waitForTimeout(p.includes('grafo') || p.includes('orixas') ? 800 : 200);
      await page.addScriptTag({ path: AXE });
      const r = await page.evaluate(async () => {
        // eslint-disable-next-line no-undef
        const res = await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'best-practice'] } });
        return res.violations.map((v) => ({ id: v.id, impacto: v.impact, ajuda: v.help, nos: v.nodes.slice(0, 3).map((n) => n.target.join(' ')), total: v.nodes.length }));
      });
      for (const v of r) {
        const grave = v.impacto === 'serious' || v.impacto === 'critical';
        if (grave) graves++;
        console.log(`${grave ? 'ERRO' : 'aviso'} [${larg}px] ${p} ${v.id} (${v.impacto}, ${v.total} nó(s)): ${v.ajuda} — ${v.nos.join(' | ')}`);
      }
      if (!r.length) console.log(`ok [${larg}px] ${p}`);
    }
    await page.close();
  }
  await browser.close();
  srv.close();
  for (const e of [...new Set(erros404)]) console.log(`ERRO ${e}`);
  if (graves || erros404.length) { console.error(`\n${graves} violação(ões) graves; ${new Set(erros404).size} erro(s) de rede/JS`); process.exit(1); }
  console.log('\nacessibilidade: nenhuma violação grave');
})();
