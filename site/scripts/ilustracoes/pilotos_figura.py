"""Piloto de ilustração FIGURATIVA (pedido do autor, sessão ilustra 2).
Figura estilizada em silhueta recortada (cor do traço da página), sem traços de
rosto, só com atributos fichados. Não entra no site até o autor aprovar.
Uso: python3 site/scripts/ilustracoes/pilotos_figura.py"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from base import svg, folha, nervura, pts

RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))


def membro(juntas):
    """Membro afinando: lista de (x, y, largura); devolve polígono + círculos nas juntas."""
    import math
    esq, dir_ = [], []
    for i, (x, y, w) in enumerate(juntas):
        xa, ya = juntas[max(i - 1, 0)][:2]
        xb, yb = juntas[min(i + 1, len(juntas) - 1)][:2]
        dx, dy = xb - xa, yb - ya
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L * w / 2, dx / L * w / 2
        esq.append((x + nx, y + ny))
        dir_.append((x - nx, y - ny))
    poly = f'<polygon points="{pts(esq + dir_[::-1])}"/>'
    return poly + ''.join(f'<circle cx="{x}" cy="{y}" r="{w / 2:.2f}"/>' for x, y, w in juntas)


def oxossi_figura():
    s = []
    # mata ao fundo (acento verde: oxossi-013, -025, -029)
    for (x0, y0, x1, y1, w) in ((30, 196, 16, 118, 10), (46, 198, 42, 110, 9), (166, 196, 180, 124, 10),
                                (154, 198, 156, 116, 9), (60, 200, 30, 152, 8), (140, 200, 172, 156, 8)):
        s.append(folha(x0, y0, x1, y1, w, extra='stroke-width="2.2" '))
        s.append(nervura(x0, y0, x1, y1, .75, 1.2))
    s.append('<path stroke-width="2.4" d="M18 178H182"/>')
    # --- figura em silhueta (cor do traço), sem traços de rosto ---
    fig = []
    fig.append(membro([(98, 114, 9), (118, 141, 7), (125, 172, 4.6)]))          # perna da frente
    fig.append('<path d="M121 170L136 174Q138 177 134 177H121Z"/>')
    fig.append(membro([(88, 114, 9), (78, 146, 6.6), (64, 172, 4.4)]))           # perna de trás
    fig.append('<path d="M61 170L75 174Q77 177 73 177H60Z"/>')
    fig.append('<path d="M82 69C88 65 98 65 103 69C105 78 103 92 100 104L99 115H85L83 102C80 90 80 78 82 69Z"/>')  # tronco
    fig.append(membro([(90, 66, 5.6), (88, 58, 4.8)]))                          # pescoço
    fig.append('<ellipse cx="85.5" cy="49" rx="7.4" ry="9" transform="rotate(-32 85.5 49)"/>')
    fig.append(membro([(85, 72, 6.4), (68, 66, 4.8), (90, 62, 4)]))             # braço que puxa a corda
    fig.append(membro([(100, 72, 6.4), (114, 58, 4.8), (126, 46, 4.2)]))        # braço do arco
    corpo = ''.join(fig)
    # contorno só por fora (visível no tema escuro), preenchimento por cima
    s.append(f'<g class="p" style="stroke-width:3.2">{corpo}</g><g class="p" style="stroke:none">{corpo}</g>')
    # roupa genérica (sem cor afirmada): pano na cintura, no tom claro
    s.append('<path class="c" stroke-width="2" d="M83 107H101L106 131Q93 127 79 131Z"/>')
    s.append('<path stroke-width="1.2" opacity=".6" d="M89 110L87 127M96 110L98 127"/>')
    # colar de contas verdes
    for i in range(7):
        t = i / 6
        x = 84.5 + 17 * t
        y = 70 + 6.5 * (1 - (2 * t - 1) ** 2)
        s.append(f'<circle class="a" cx="{x:.1f}" cy="{y:.1f}" r="2.1" stroke-width="1.1"/>')
    # eruquerê preso à cintura, atrás
    s.append('<path class="c" stroke-width="1.8" d="M80 109l5 1 -2 10 -5 -1z"/>')
    s.append('<path stroke-width="1.4" d="M79 120C77 129 73 137 69 146M80 120C79 130 77 139 75 148M81 121C81 131 81 140 80 149M78 119C74 127 69 134 63 141"/>')
    # arco, corda e flecha (oxossi-014)
    s.append('<path stroke-width="3.4" d="M138.3 73.4Q142.4 38.6 113.7 18.6"/>')
    s.append('<path stroke-width="1.2" d="M138.3 73.4L90 62L113.7 18.6"/>')
    s.append('<path stroke-width="2.2" d="M84 64.7L140 39.8"/>')
    s.append(f'<polygon class="c" stroke-width="1.8" points="{pts([(138, 36.5), (148, 35.5), (141.5, 43.5)])}"/>')
    s.append('<path stroke-width="1.4" d="M84 64.7l-5 -5M88 62.9l-5 -5M84 64.7l-1.5 7M88 62.9l-1.5 7"/>')
    return ''.join(s)


ALT = ('Ilustração figurativa estilizada de Oxóssi: uma figura em silhueta, sem traços de rosto, '
       'puxa um arco com flecha apontada para o alto; usa um colar de contas verdes e traz um '
       'espanta-moscas de rabo de boi (eruquerê) na cintura, diante das folhas da mata.')

if __name__ == '__main__':
    destino = os.path.join(RAIZ, 'site', 'src', 'assets', 'ilustracoes', 'pilotos')
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(destino, 'oxossi-figura.svg'), 'w', encoding='utf-8').write(svg('oxossi-figura', ALT, 'verde', oxossi_figura()) + '\n')
    print('ok')
