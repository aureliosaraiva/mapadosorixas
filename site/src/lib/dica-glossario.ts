// Dica (tooltip) dos termos do glossário: ao passar o mouse ou focar um link
// .termo-gl, mostra a definição que o link já referencia por aria-describedby
// (o leitor de tela lê essa descrição sem depender deste script). A dica some
// com Esc, ao tirar o mouse/foco, e pode receber o ponteiro (WCAG 1.4.13).
const dica = document.createElement('div');
dica.className = 'dica-gl';
dica.setAttribute('aria-hidden', 'true');
dica.hidden = true;
document.body.appendChild(dica);

let alvo: HTMLElement | null = null;
let timer: number | undefined;

function mostrar(a: HTMLElement) {
  const def = document.getElementById(a.getAttribute('aria-describedby') || '');
  if (!def) return;
  window.clearTimeout(timer);
  alvo = a;
  dica.textContent = def.textContent;
  dica.hidden = false;
  const r = a.getBoundingClientRect();
  const larg = Math.min(360, document.documentElement.clientWidth - 16);
  dica.style.maxWidth = `${larg}px`;
  const esq = Math.max(8, Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - larg - 8));
  dica.style.left = `${esq}px`;
  dica.style.top = `${r.bottom + window.scrollY + 6}px`;
}
function esconder() {
  timer = window.setTimeout(() => { dica.hidden = true; alvo = null; }, 150);
}

for (const a of document.querySelectorAll<HTMLElement>('a.termo-gl')) {
  a.addEventListener('mouseenter', () => mostrar(a));
  a.addEventListener('focus', () => mostrar(a));
  a.addEventListener('mouseleave', esconder);
  a.addEventListener('blur', esconder);
}
dica.addEventListener('mouseenter', () => window.clearTimeout(timer));
dica.addEventListener('mouseleave', esconder);
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && alvo) { dica.hidden = true; alvo = null; }
});
