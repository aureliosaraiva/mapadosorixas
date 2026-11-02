"""Composições da série, uma função por entidade. Cada uma devolve o corpo do SVG
(dentro do grupo com traço currentColor). Ver base.py e data/ilustracoes.json."""
import math
from base import f, pts, polar, folha, nervura, onda, estrela, buzio


def ogum():
    s = []
    # folhas de espada-de-ogum (Sansevieria), só nas laterais, atrás do leque
    for lado in (-1, 1):
        for (bx, by, tx, ty, w) in ((44, 170, 62, 84, 8), (54, 168, 82, 100, 7.5), (34, 170, 44, 104, 6.5)):
            s.append(folha(100 - lado * bx, by, 100 - lado * tx, ty, w, extra='stroke-width="2.4" '))
    # emblema de ferro: barra-base e sete pontas em leque estreito
    cx, cy = 100, 150
    for i in range(7):
        ang = -135 + i * 15
        x0, y0 = polar(cx, cy, 22, ang)
        x1, y1 = polar(cx, cy, 72, ang)
        s.append(f'<path stroke-width="3.4" d="M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}"/>')
        b1, b2 = polar(cx, cy, 70, ang - 2.6), polar(cx, cy, 70, ang + 2.6)
        m1, m2 = polar(cx, cy, 77, ang - 3.6), polar(cx, cy, 77, ang + 3.6)
        tip = polar(cx, cy, 94, ang)
        s.append(f'<polygon class="c" stroke-width="2.2" points="{pts([b1, m1, tip, m2, b2])}"/>')
    a0, a1 = polar(cx, cy, 24, -150), polar(cx, cy, 24, -30)
    s.append(f'<path class="c" stroke-width="3.4" d="M{f(a0[0])} {f(a0[1])}A24 24 0 0 1 {f(a1[0])} {f(a1[1])}Z"/>')
    s.append(f'<path stroke-width="1.6" d="M{f(cx - 12)} {f(cy - 9)}h24"/>')
    # mariô: franja de folhas de dendezeiro desfiadas, presa num cordão
    cord = []
    for i in range(0, 34):
        x = 38 + i * 3.94
        y = 148 + 9 * math.sin(math.pi * (x - 38) / 130)
        cord.append((x, y))
    franja = ''.join(f'M{f(x)} {f(y + 1)}l{f(-1 + (i % 3) * .8)} {f(24 - abs(i - 16.5) * .4)}' for i, (x, y) in enumerate(cord))
    s.append(f'<path stroke-width="1.3" opacity=".85" d="{franja}"/>')
    s.append(f'<polyline stroke-width="3.4" points="{pts(cord)}"/>')
    return ''.join(s)


def iemanja():
    s = []
    # lua crescente com estrela (emblema), metal prata -> .c
    s.append('<path class="c" d="M96 34A34 34 0 1 0 128 86A28 28 0 1 1 96 34Z"/>')
    s.append(f'<polygon class="c" stroke-width="2.4" points="{estrela(124, 50, 11, 4.6)}"/>')
    # mar: ondas; a de baixo preenchida com o acento
    s.append(f'<path class="a" stroke-width="3" d="{onda(150, 6, 44)}V230H-20Z"/>')
    s.append(f'<path d="{onda(131, 6, 44)}"/>')
    s.append(f'<path stroke-width="2.4" d="{onda(114, 5, 44)}" transform="translate(11 0)"/>')
    s.append(f'<path stroke-width="1.8" opacity=".7" d="{onda(170, 4, 36)}" transform="translate(9 0)"/>')
    # otá: seixo marinho
    s.append('<ellipse class="c" cx="100" cy="174" rx="20" ry="10.5"/>')
    s.append('<path stroke-width="1.5" opacity=".6" d="M88 171q12 -5 24 0"/>')
    return ''.join(s)


def xango():
    s = []
    # raio (acento) caindo sobre a pedra
    s.append('<polygon class="a" stroke-width="2.6" points="152,40 124,96 140,96 110,150 116,112 100,112 128,40"/>')
    # oxê: machado de cabo longo, lâmina em meia-lua com furo decorativo
    s.append('<g transform="translate(14 4)">')
    s.append('<path stroke-width="6" d="M78 40V166"/>')
    s.append('<path class="c" stroke-width="3" d="M78 52L60 50C46 40 36 34 30 34C24 52 24 84 30 102C36 102 46 96 60 86L78 84Z"/>')
    s.append('<circle class="f" cx="54" cy="68" r="6" stroke-width="2.2"/>')
    s.append('<path stroke-width="1.5" d="M35 44C32 58 32 78 35 92"/>')
    s.append('<rect class="c" x="72" y="32" width="12" height="9" rx="2" stroke-width="2.4"/>')
    s.append('</g>')
    # otá: pedra de raio
    s.append('<polygon class="c" points="70,176 80,158 104,150 126,156 138,172 120,184 86,184"/>')
    s.append('<path stroke-width="1.6" d="M80 158l18 12 28 -14M98 170l-12 14M98 170l22 14"/>')
    for a in (-70, -30, 10):
        x0, y0 = polar(113, 148, 9, a)
        x1, y1 = polar(113, 148, 16, a)
        s.append(f'<path stroke-width="2" d="M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}"/>')
    return ''.join(s)


DESENHOS = {'ogum': ogum, 'iemanja': iemanja, 'xango': xango}
