// Notas de rodapé que abrem ao toque/clique (e ao passar o mouse, em telas com
// ponteiro fino) numa caixa junto ao número, sem tirar o leitor do lugar.
// Sem JavaScript, o número continua sendo um link para a nota no fim da página.
// A caixa recebe o foco ao abrir pelo teclado, fecha com Esc, com o botão ✕ ou
// clicando fora, e devolve o foco ao número (WCAG 1.4.13 e 2.1.2).
const caixa = document.createElement('div');
caixa.className = 'dica-nota';
caixa.setAttribute('role', 'dialog');
caixa.setAttribute('aria-modal', 'false');
caixa.hidden = true;
caixa.tabIndex = -1;
document.body.appendChild(caixa);

let origem: HTMLAnchorElement | null = null;
let timer: number | undefined;
const ponteiroFino = matchMedia('(hover: hover) and (pointer: fine)').matches;

function conteudoDa(href: string) {
  const li = document.getElementById(href.slice(1));
  if (!li) return null;
  const copia = li.cloneNode(true) as HTMLElement;
  copia.querySelectorAll('.voltar-nota, [id]').forEach((n) => {
    if (n.classList.contains('voltar-nota')) n.remove(); else n.removeAttribute('id');
  });
  return copia.innerHTML;
}

function abrir(a: HTMLAnchorElement, focar: boolean) {
  const href = a.getAttribute('href') || '';
  const html = conteudoDa(href);
  if (html === null) return false;
  window.clearTimeout(timer);
  origem = a;
  const n = a.textContent?.replace(/\D/g, '') || '';
  caixa.setAttribute('aria-label', `Nota ${n}`);
  caixa.innerHTML = `<div class="dica-cabeca"><span>Nota ${n}</span><button type="button" aria-label="Fechar nota">✕</button></div><div class="dica-corpo">${html}</div><a class="dica-ir" href="${href}">Ver todas as notas</a>`;
  caixa.hidden = false;
  caixa.querySelector('button')!.addEventListener('click', () => fechar(true));
  caixa.querySelector('.dica-ir')!.addEventListener('click', () => { caixa.hidden = true; });
  const r = a.getBoundingClientRect();
  const largura = Math.min(416, document.documentElement.clientWidth - 24);
  caixa.style.width = `${largura}px`;
  const esq = Math.max(12, Math.min(r.left + window.scrollX - 20, window.scrollX + document.documentElement.clientWidth - largura - 12));
  caixa.style.left = `${esq}px`;
  caixa.style.top = `${r.bottom + window.scrollY + 8}px`;
  if (focar) caixa.focus();
  return true;
}
function fechar(devolverFoco: boolean) {
  if (caixa.hidden) return;
  caixa.hidden = true;
  if (devolverFoco) origem?.focus();
  origem = null;
}

for (const a of document.querySelectorAll<HTMLAnchorElement>('sup.ref a[href^="#nota-"]')) {
  a.setAttribute('aria-haspopup', 'dialog');
  a.addEventListener('click', (e) => {
    if (origem === a && !caixa.hidden) { e.preventDefault(); fechar(true); return; }
    // clique pelo teclado (Enter) leva o foco para a caixa; toque/mouse não
    if (abrir(a, (e as MouseEvent).detail === 0)) e.preventDefault();
  });
  if (ponteiroFino) {
    a.addEventListener('mouseenter', () => { timer = window.setTimeout(() => abrir(a, false), 180); });
    a.addEventListener('mouseleave', () => { window.clearTimeout(timer); timer = window.setTimeout(() => { if (!caixa.matches(':hover, :focus-within')) fechar(false); }, 250); });
  }
}
caixa.addEventListener('mouseleave', () => { if (ponteiroFino && !caixa.contains(document.activeElement)) timer = window.setTimeout(() => fechar(false), 250); });
caixa.addEventListener('mouseenter', () => window.clearTimeout(timer));
document.addEventListener('keydown', (e) => { if (e.key === 'Escape') fechar(true); });
document.addEventListener('click', (e) => {
  const t = e.target as Node;
  if (!caixa.hidden && !caixa.contains(t) && !(origem && origem.contains(t))) fechar(false);
});
