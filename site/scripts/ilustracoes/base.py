"""Base comum da série de ilustrações simbólicas (sessão ilustra).

Cada ilustração é um SVG 200×200 desenhado em código: um medalhão (disco + anéis
concêntricos discretos, como o padrão da capa) e, dentro dele, uma composição de
símbolos documentados no fichamento. Cores:
  - traço: currentColor (o texto da página; funciona no claro e no escuro);
  - .f  fundo do medalhão  -> var(--il-fundo)
  - .r  anéis              -> var(--il-borda)
  - .c  "metal"/claro      -> var(--il-claro)
  - .a  acento (no máximo um por ilustração) -> var(--a), definido no <svg>
As variáveis --il-* vêm de site/src/styles/global.css (claro/escuro); os valores
depois da vírgula são o fallback para ver o arquivo solto.
"""
import math

ESTILO = ('.il .f{fill:var(--il-fundo,#f4f0e8)}.il .r{fill:none;stroke:var(--il-borda,#d9d0bf)}'
          '.il .c{fill:var(--il-claro,#fffdf9)}.il .a{fill:var(--a,#8c4c0c)}'
          '.il .sa{stroke:var(--a,#8c4c0c)}.il .n{fill:none}.il .t{fill:currentColor}')

ACENTOS = {
    # nome: (variável CSS, fallback claro)
    'neutro': ('--il-ocre', '#b07a3c'),
    'verde': ('--il-verde', '#4f7a45'),
    'vermelho': ('--il-vermelho', '#b0503c'),
    'azul': ('--il-azul', '#4d6fae'),
    'ouro': ('--il-ouro', '#c19a2e'),
    'violeta': ('--il-violeta', '#7d5ea3'),
}


def f(x):
    s = f'{x:.1f}'
    return s[:-2] if s.endswith('.0') else s


def pts(ps):
    return ' '.join(f'{f(x)},{f(y)}' for x, y in ps)


def polar(cx, cy, r, ang_graus):
    a = math.radians(ang_graus)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def folha(x0, y0, x1, y1, larg, cls='a', extra=''):
    """Folha lanceolada da base (x0,y0) à ponta (x1,y1)."""
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    mx, my = x0 + dx * .42, y0 + dy * .42
    c1 = (mx + nx * larg, my + ny * larg)
    c2 = (mx - nx * larg, my - ny * larg)
    return (f'<path class="{cls}" {extra}d="M{f(x0)} {f(y0)}Q{f(c1[0])} {f(c1[1])} {f(x1)} {f(y1)}'
            f'Q{f(c2[0])} {f(c2[1])} {f(x0)} {f(y0)}Z"/>')


def nervura(x0, y0, x1, y1, k=.8, sw=1.5):
    return f'<path stroke-width="{sw}" d="M{f(x0)} {f(y0)}L{f(x0 + (x1 - x0) * k)} {f(y0 + (y1 - y0) * k)}"/>'


def onda(y, amp=6, comp=40, fase=0, x0=-20, x1=220):
    """Linha ondulada (curvas quadráticas alternadas)."""
    d = [f'M{f(x0)} {f(y)}']
    x = x0 + fase
    d = [f'M{f(x0)} {f(y)}']
    meio = comp / 2
    sinal = 1
    x = x0
    while x < x1:
        d.append(f'q{f(meio / 2)} {f(-amp * sinal)} {f(meio)} 0')
        x += meio
        sinal = -sinal
    return ''.join(d)


def estrela(cx, cy, R, r, n=5, rot=-90):
    ps = []
    for i in range(2 * n):
        ps.append(polar(cx, cy, R if i % 2 == 0 else r, rot + i * 180 / n))
    return pts(ps)


def buzio(cx, cy, comp=14, larg=9, ang=0, cls='c'):
    """Búzio estilizado: oval com a fenda dentada."""
    a = comp / 2
    s = [f'<g transform="translate({f(cx)} {f(cy)}) rotate({f(ang)})">',
         f'<ellipse class="{cls}" rx="{f(a)}" ry="{f(larg / 2)}" stroke-width="2"/>',
         f'<path stroke-width="1.4" d="M{f(-a * .62)} 0Q0 {f(-larg * .12)} {f(a * .62)} 0"/>']
    for i in range(-2, 3):
        x = i * a * .24
        s.append(f'<path stroke-width="1.1" d="M{f(x)} -1.6V1.6"/>')
    s.append('</g>')
    return ''.join(s)


def svg(id_, titulo, acento, corpo, recorte=True):
    var, cor = ACENTOS[acento]
    clip = f'<clipPath id="ilc-{id_}"><circle cx="100" cy="100" r="86"/></clipPath>' if recorte else ''
    abre_g = f'<g clip-path="url(#ilc-{id_})">' if recorte else '<g>'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" class="il il-{id_}" '
        f'role="img" aria-labelledby="ilt-{id_}" style="--a:var({var},{cor})">'
        f'<title id="ilt-{id_}">{titulo}</title>'
        f'<defs><style>{ESTILO}</style>{clip}</defs>'
        '<circle class="f" cx="100" cy="100" r="96"/>'
        '<circle class="r" cx="100" cy="100" r="95" stroke-width="1.5"/>'
        '<circle class="r" cx="100" cy="100" r="86" stroke-width="1"/>'
        + ''.join(f'<circle class="t" cx="{f(x)}" cy="{f(y)}" r=".9" opacity=".35"/>'
                  for x, y in (polar(100, 100, 90.5, a) for a in range(0, 360, 15)))
        + f'{abre_g}<g fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
        f'stroke-linejoin="round">{corpo}</g></g></svg>'
    )
