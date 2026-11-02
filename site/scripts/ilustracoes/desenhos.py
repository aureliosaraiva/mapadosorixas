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


def exu():
    s = []
    # encruzilhada em X: dois caminhos que se cruzam (contorno, depois o miolo por cima)
    rects = ''.join(f'<rect x="-120" y="-17" width="240" height="34" transform="translate(100 100) rotate({a})"/>' for a in (45, -45))
    s.append(f'<g class="c">{rects}</g>')
    s.append(f'<g class="c" stroke="none">{rects}</g>')
    for a in (45, -45):
        s.append(f'<path stroke-width="1.6" stroke-dasharray="7 7" opacity=".7" d="M-20 0H240" transform="translate(100 100) rotate({a}) translate(-110 0)"/>')
    # no centro, um montículo de laterita (terra avermelhada)
    s.append('<ellipse cx="100" cy="114" rx="30" ry="6" class="c" stroke-width="2"/>')
    s.append('<path class="a" d="M66 114C72 100 86 94 100 94C114 94 128 100 134 114Z"/>')
    s.append('<path stroke-width="1.4" opacity=".55" d="M80 106q8 -4 16 0M100 102q8 -4 16 0M90 110q8 -3 16 0"/>')
    # búzios nos quatro quadrantes entre os caminhos
    for (x, y, ang) in ((100, 40, 90), (100, 162, 90), (38, 100, 0), (162, 100, 0)):
        s.append(buzio(x, y, 22, 14, ang))
    return ''.join(s)


def oxossi():
    s = []
    # mata: folhas embaixo (acento)
    for (x0, y0, x1, y1, w) in ((70, 196, 34, 136, 10), (130, 196, 166, 136, 10), (86, 196, 64, 128, 10),
                                (114, 196, 136, 128, 10), (100, 196, 100, 132, 11)):
        s.append(folha(x0, y0, x1, y1, w, extra='stroke-width="2.4" '))
        s.append(nervura(x0, y0, x1, y1, .78, 1.3))
    # arco e flecha (ofá), na diagonal
    s.append('<g transform="translate(88 98) rotate(-45)">')
    s.append('<path stroke-width="4" d="M0 -60Q-46 0 0 60"/>')
    s.append('<path stroke-width="1.6" d="M0 -60L0 60"/>')
    s.append('<path stroke-width="3" d="M-44 0H52"/>')
    s.append('<polygon class="c" stroke-width="2.4" points="50,-7 68,0 50,7"/>')
    s.append('<path stroke-width="2" d="M-44 0l-9 -8M-38 0l-9 -8M-44 0l-9 8M-38 0l-9 8"/>')
    s.append('</g>')
    # eruquerê: espanta-moscas de rabo de boi
    s.append('<path class="c" stroke-width="3" d="M146 168L150 134L158 134L156 168Z"/>')
    s.append('<path stroke-width="2.4" d="M146 140h12M147 150h10"/>')
    fios = ''.join(f'M{152 + dx * .3} 134C{150 + dx} 110 {146 + dx * 1.4} 86 {150 + dx * 1.8} 58' for dx in (-6, -3, 0, 3, 6, 9))
    s.append(f'<path stroke-width="1.7" d="{fios}"/>')
    return ''.join(s)


def oxum():
    s = []
    # águas doces: cachoeira que cai atrás do abebé até um poço
    for i, x in enumerate(range(52, 152, 12)):
        s.append(f'<path stroke-width="1.8" opacity=".75" d="M{x} 10C{x - 2} 60 {x + 3} 110 {x} 152"/>')
    for (rx, ry, sw) in ((62, 12, 2.4), (44, 8, 2), (24, 4.5, 1.6)):
        s.append(f'<ellipse cx="100" cy="164" rx="{rx}" ry="{ry}" stroke-width="{sw}" class="f"/>')
    # otá: seixo liso de rio
    s.append('<ellipse class="c" cx="138" cy="166" rx="15" ry="8.5" stroke-width="2.6"/>')
    # abebé (leque redondo), metal ouro/latão -> acento
    s.append('<path stroke-width="6" d="M100 112V148"/>')
    s.append('<circle class="c" cx="100" cy="150" r="5" stroke-width="2.4"/>')
    s.append('<circle class="a" cx="100" cy="72" r="42"/>')
    s.append('<circle cx="100" cy="72" r="30" stroke-width="2"/>')
    for i in range(24):
        x0, y0 = polar(100, 72, 31, i * 15)
        x1, y1 = polar(100, 72, 40, i * 15)
        s.append(f'<path stroke-width="1.6" d="M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}"/>')
    s.append(f'<polygon class="c" stroke-width="2.2" points="{estrela(100, 72, 18, 9, 8, -90)}"/>')
    s.append('<circle class="a" cx="100" cy="72" r="5" stroke-width="2"/>')
    return ''.join(s)


def iansa():
    s = []
    # ventania: três correntes de vento com volutas
    s.append('<path stroke-width="3" d="M14 72C44 58 70 84 104 70C126 61 140 44 128 34C118 26 106 38 114 46"/>')
    s.append('<path stroke-width="3" d="M14 112C48 96 82 124 120 106C142 96 160 82 150 70C142 62 130 70 136 78"/>')
    s.append('<path stroke-width="2.4" opacity=".8" d="M30 146C60 136 88 156 112 146C122 142 126 134 120 130"/>')
    # centelha / relâmpago (acento)
    s.append('<polygon class="a" stroke-width="2.4" points="160,102 142,138 154,138 136,172 168,126 154,126 172,102"/>')
    # espada
    s.append('<polygon class="c" stroke-width="3" points="62,40 70,40 72,136 66,146 60,136"/>')
    s.append('<path stroke-width="1.5" d="M66 48V132"/>')
    s.append('<path stroke-width="5" d="M48 140H84"/>')
    s.append('<path stroke-width="6" d="M66 142V166"/>')
    s.append('<circle class="c" cx="66" cy="170" r="5" stroke-width="2.4"/>')
    return ''.join(s)


def nana():
    s = []
    # chuva
    for (x, y) in ((40, 40), (58, 64), (34, 90), (52, 116), (150, 44), (168, 70), (146, 96), (162, 122)):
        s.append(f'<path stroke-width="2" d="M{x} {y}l-6 12"/>')
    # águas das chuvas e do dilúvio, embaixo
    s.append(f'<path class="f" stroke-width="2.6" d="{onda(160, 4, 30)}V230H-20Z"/>')
    s.append(f'<path stroke-width="2" opacity=".8" d="{onda(174, 3.5, 30)}" transform="translate(8 0)"/>')
    # chachará: feixe de varetas amarradas
    for i in range(9):
        k = (i - 4) / 4
        x_top, x_bot = 100 + k * 24, 100 + k * 12
        s.append(f'<path stroke-width="2.2" d="M{f(x_top)} {f(38 + abs(k) * 8)}Q{f(100 + k * 10)} 110 {f(x_bot)} 164"/>')
        s.append(f'<circle class="t" stroke="none" cx="{f(x_top)}" cy="{f(36 + abs(k) * 8)}" r="2.6"/>')
    for (y, w) in ((112, 30), (140, 30)):
        s.append(f'<rect class="a" x="{100 - w / 2}" y="{y - 5}" width="{w}" height="10" rx="3" stroke-width="2.4"/>')
    return ''.join(s)


def omolu():
    s = []
    # palha: franja radial no alto (acento neutro = ocre do site, cor de palha)
    for i in range(41):
        ang = 196 + i * 3.7
        x0, y0 = polar(100, 104, 88, ang)
        x1, y1 = polar(100, 104, 58 - (i % 3) * 4, ang)
        s.append(f'<path class="sa" stroke-width="2" d="M{f(x0)} {f(y0)}L{f(x1)} {f(y1)}"/>')
    a0, a1 = polar(100, 104, 62, 190), polar(100, 104, 62, 350)
    s.append(f'<path stroke-width="1.6" opacity=".6" d="M{f(a0[0])} {f(a0[1])}A62 62 0 0 1 {f(a1[0])} {f(a1[1])}"/>')
    # terra
    s.append('<path class="f" stroke-width="2.6" d="M-10 162Q100 152 210 162V220H-10Z"/>')
    for x in range(30, 180, 16):
        s.append(f'<path stroke-width="1.4" opacity=".55" d="M{x} 174l6 -4"/>')
    # xaxará: feixe de varetas (vassoura), na diagonal
    s.append('<g transform="rotate(-24 100 120)">')
    for i in range(11):
        k = (i - 5) / 5
        s.append(f'<path stroke-width="1.8" d="M{f(100 + k * 8)} 146Q{f(100 + k * 12)} 110 {f(100 + k * 28)} {f(70 + abs(k) * 10)}"/>')
    s.append('<rect class="a" x="91" y="124" width="18" height="9" rx="3" stroke-width="2.2"/>')
    s.append('<path class="c" stroke-width="2.4" d="M92 146h16l-3 18h-10Z"/>')
    s.append('</g>')
    # otá cheio de buraquinhos
    s.append('<path class="c" d="M120 166C120 150 134 144 146 146C158 148 164 158 160 168Z"/>')
    for (x, y) in ((132, 156), (142, 152), (150, 160), (138, 162), (152, 151)):
        s.append(f'<circle class="t" stroke="none" cx="{x}" cy="{y}" r="1.7"/>')
    return ''.join(s)


def oxala():
    s = []
    # abóbada celeste
    a0, a1 = polar(100, 128, 76, 196), polar(100, 128, 76, 344)
    s.append(f'<path stroke-width="1.8" stroke-dasharray="2 6" d="M{f(a0[0])} {f(a0[1])}A76 76 0 0 1 {f(a1[0])} {f(a1[1])}"/>')
    # paxorô: vara de ferro
    s.append('<path stroke-width="5" d="M50 46V172"/>')
    for y in (60, 70, 80):
        s.append(f'<path stroke-width="2.2" d="M44 {y}h12"/>')
    s.append('<circle class="c" cx="50" cy="42" r="6" stroke-width="2.6"/>')
    # cabaça dupla: duas metades encaixadas (céu e terra)
    s.append('<path class="c" d="M66 118A34 30 0 0 1 134 118Z"/>')
    s.append('<path class="c" d="M64 124H136A36 32 0 0 1 64 124Z"/>')
    s.append('<path stroke-width="1.6" opacity=".6" d="M80 104q20 -10 40 0M78 138q22 10 44 0"/>')
    # pomba no alto do emblema (de frente, asas abertas)
    s.append('<path class="c" stroke-width="2.4" d="M98 66C86 50 72 46 60 52C72 56 84 66 96 74Z"/>')
    s.append('<path class="c" stroke-width="2.4" d="M102 66C114 50 128 46 140 52C128 56 116 66 104 74Z"/>')
    s.append('<path class="c" stroke-width="2.4" d="M94 84L100 92L106 84Z"/>')
    s.append('<ellipse class="c" cx="100" cy="70" rx="6" ry="13" stroke-width="2.4"/>')
    s.append('<circle class="c" cx="100" cy="54" r="5" stroke-width="2.4"/>')
    # flor de algodão
    for ang in range(-90, 270, 72):
        x, y = polar(142, 152, 8, ang)
        s.append(f'<circle class="c" cx="{f(x)}" cy="{f(y)}" r="7" stroke-width="2.2"/>')
    s.append('<circle class="c" cx="142" cy="152" r="5" stroke-width="2"/>')
    s.append('<path stroke-width="2.4" d="M142 166V176"/>')
    return ''.join(s)


def ossaim():
    s = []
    # mato selvagem embaixo
    for (x0, y0, x1, y1, w) in ((80, 190, 34, 150, 9), (120, 190, 166, 150, 9), (88, 192, 58, 136, 9),
                                (112, 192, 142, 136, 9), (70, 196, 30, 176, 7), (130, 196, 170, 176, 7)):
        s.append(folha(x0, y0, x1, y1, w, extra='stroke-width="2.3" '))
        s.append(nervura(x0, y0, x1, y1, .75, 1.2))
    # ferro de ossaim: haste pontuda, ramos abertos para cima e pássaro no alto
    s.append('<path stroke-width="5" d="M100 186V70"/>')
    s.append('<polygon class="t" points="96,180 104,180 100,192"/>')
    for ang in (-160, -140, -118, -62, -40, -20):
        x0, y0 = polar(100, 118, 6, ang)
        x1, y1 = polar(100, 118, 60, ang)
        cx_, cy_ = polar(100, 118, 34, ang + (8 if ang < -90 else -8))
        s.append(f'<path stroke-width="3" d="M{f(x0)} {f(y0)}Q{f(cx_)} {f(cy_)} {f(x1)} {f(y1)}"/>')
        s.append(f'<circle class="c" cx="{f(x1)}" cy="{f(y1)}" r="4" stroke-width="2.2"/>')
    s.append('<circle class="c" cx="100" cy="118" r="7" stroke-width="2.6"/>')
    # pássaro
    s.append('<path class="c" stroke-width="2.6" d="M84 60C88 50 98 46 108 48L116 42L114 52C116 60 110 68 100 70C92 70 86 66 84 60Z"/>')
    s.append('<path stroke-width="2.4" d="M84 60L72 64L84 66"/>')
    s.append('<path stroke-width="1.8" d="M92 58q8 4 16 -2"/>')
    s.append('<circle class="t" stroke="none" cx="110" cy="50" r="1.5"/>')
    s.append('<polygon class="t" points="115,47 122,49 115,51"/>')
    return ''.join(s)


def oxumare():
    s = []
    # arco-íris: faixas concêntricas, sem eleger cores
    for i, (r, op) in enumerate(((74, .9), (64, .55), (54, .9), (44, .55), (34, .9))):
        a0, a1 = polar(100, 132, r, 180), polar(100, 132, r, 360)
        s.append(f'<path stroke-width="7" opacity="{op}" class="{"sa" if i % 2 else ""}" d="M{f(a0[0])} {f(a0[1])}A{r} {r} 0 0 1 {f(a1[0])} {f(a1[1])}"/>')
    # chão
    s.append('<path class="f" stroke-width="2.6" d="M-10 150H210V220H-10Z"/>')
    # dois ferros que desenham serpentes
    for (x, sinal) in ((80, 1), (120, -1)):
        d = f'M{x} 182'
        y = 182
        for k in range(5):
            d += f'q{8 * sinal * (1 if k % 2 == 0 else -1)} -9 0 -18'
            y -= 18
        s.append(f'<path stroke-width="4.4" d="{d}"/>')
        s.append(f'<polygon class="t" stroke-width="2" points="{x - 5},{y + 2} {x + 5},{y + 2} {x + 3 * sinal},{y - 12}"/>')
    s.append('<path stroke-width="3" d="M66 184H134"/>')
    return ''.join(s)


def logunede():
    s = []
    # pena de ave de caça no alto
    s.append('<path class="c" stroke-width="2.6" d="M118 78C106 60 108 38 122 22C130 42 128 62 118 78Z"/>')
    s.append('<path stroke-width="1.8" d="M118 78C118 62 120 42 122 24"/>')
    for k in range(4):
        y = 40 + k * 10
        s.append(f'<path stroke-width="1.3" opacity=".7" d="M{f(119 + k * .3)} {y + 4}l7 -6M{f(119 + k * .3)} {y + 4}l-8 -5"/>')
    # ofá (arco e flecha), à esquerda
    s.append('<g transform="translate(78 126) rotate(-125)">')
    s.append('<path stroke-width="3.6" d="M0 -46Q-34 0 0 46"/>')
    s.append('<path stroke-width="1.5" d="M0 -46V46"/>')
    s.append('<path stroke-width="2.8" d="M-32 0H40"/>')
    s.append('<polygon class="c" stroke-width="2.2" points="38,-6 54,0 38,6"/>')
    s.append('</g>')
    # abebé (leque), à direita
    s.append('<g transform="translate(4 10) rotate(24 128 128)">')
    s.append('<path stroke-width="5" d="M128 144V176"/>')
    s.append('<circle class="a" cx="128" cy="118" r="28"/>')
    s.append('<circle cx="128" cy="118" r="19" stroke-width="1.8"/>')
    s.append(f'<polygon class="c" stroke-width="2" points="{estrela(128, 118, 12, 6, 8)}"/>')
    s.append('</g>')
    return ''.join(s)


def _silhueta(formas, cls='c', sw=3):
    """Desenha a união de formas: contorno de todas e, por cima, o miolo sem traço."""
    return f'<g class="{cls}" stroke-width="{sw}">{formas}</g><g class="{cls}" stroke="none">{formas}</g>'


def oba():
    s = []
    # nuvens revoltas que se encontram
    nuvem = ('<path d="M10 76C8 62 22 54 34 60C38 44 60 40 70 54C78 46 94 50 96 64C102 68 100 78 92 80Q54 90 16 80Z"/>')
    s.append(_silhueta(nuvem))
    s.append(f'<g transform="translate(200 0) scale(-1 1)">{_silhueta(nuvem)}</g>')
    s.append('<path stroke-width="2" d="M40 70c4 -8 14 -8 16 0M144 70c4 -8 14 -8 16 0"/>')
    # rio Oba
    rio = 'M100 84C82 106 124 122 104 144C92 158 70 170 58 200'
    s.append(f'<path stroke-width="28" d="{rio}"/>')
    s.append(f'<path class="sc" stroke-width="22" d="{rio}"/>')
    s.append('<path stroke-width="1.6" opacity=".6" d="M100 104q6 6 2 12M98 150q-6 6 -12 8M80 176q-6 6 -8 12"/>')
    return ''.join(s)


def iroko():
    s = []
    # céu: arco pontilhado que a árvore alcança
    a0, a1 = polar(100, 120, 80, 200), polar(100, 120, 80, 340)
    s.append(f'<path stroke-width="1.8" stroke-dasharray="2 6" d="M{f(a0[0])} {f(a0[1])}A80 80 0 0 1 {f(a1[0])} {f(a1[1])}"/>')
    # chão e raízes
    s.append('<path stroke-width="2.6" d="M14 152H186"/>')
    s.append('<path stroke-width="2.2" d="M92 152C82 162 62 166 40 174M96 152C92 166 80 176 70 188M104 152C108 166 120 176 130 188M108 152C118 162 138 166 160 174M100 152V184"/>')
    # tronco e galhos
    s.append('<path class="c" stroke-width="3" d="M88 154C92 132 90 118 80 104L92 100C98 112 100 112 100 112C100 112 102 112 108 100L120 104C110 118 108 132 112 154Z"/>')
    s.append('<path stroke-width="3" d="M84 102C76 92 66 88 54 88M116 102C124 92 134 88 146 88M100 112V80"/>')
    # copa larga
    copa = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in ((56, 82, 22), (80, 62, 26), (120, 62, 26), (144, 82, 22), (100, 74, 26), (100, 48, 20)))
    s.append(_silhueta(copa, 'c'))
    for (x, y) in ((60, 80), (84, 58), (116, 58), (140, 80), (100, 72), (100, 46), (76, 84), (124, 84)):
        s.append(f'<path stroke-width="1.6" opacity=".55" d="M{x - 5} {y + 2}q5 -6 10 0"/>')
    # raízes aéreas
    s.append('<path stroke-width="1.4" opacity=".7" d="M62 100V128M70 96V120M136 96V122M142 100V130"/>')
    return ''.join(s)


def ibeji():
    s = []
    # dois motivos iguais e espelhados (os gêmeos) e um terceiro, menor, entre eles
    for (x, y, R) in ((66, 76, 22), (134, 76, 22), (100, 108, 13)):
        s.append(f'<circle class="c" cx="{x}" cy="{y}" r="{R}"/>')
        s.append(f'<polygon class="a" stroke-width="2" points="{estrela(x, y, R * .72, R * .34, 8)}"/>')
        s.append(f'<circle class="c" cx="{x}" cy="{y}" r="{f(R * .2)}" stroke-width="1.8"/>')
    s.append('<path stroke-width="2" stroke-dasharray="3 5" d="M88 76H112"/>')
    # três pratinhos de barro
    for (x, w) in ((50, 24), (100, 17), (150, 24)):
        s.append(f'<path class="a" d="M{x - w} 148H{x + w}C{x + w - 4} 164 {x - w + 4} 164 {x - w} 148Z"/>')
        s.append(f'<ellipse class="c" cx="{x}" cy="148" rx="{w}" ry="5" stroke-width="2.4"/>')
    s.append('<path stroke-width="2.4" d="M14 166H186"/>')
    return ''.join(s)


def orunmila():
    s = []
    # opelê: colar de adivinhação (contas pequenas, sem contar peças)
    contas = []
    for i in range(40):
        x, y = 100 + 54 * math.cos(math.radians(i * 9)), 86 + 42 * math.sin(math.radians(i * 9))
        contas.append((x, y))
    s.append(f'<polygon stroke-width="1.6" points="{pts(contas)}"/>')
    for (x, y) in contas[::2]:
        s.append(f'<circle class="c" cx="{f(x)}" cy="{f(y)}" r="3.6" stroke-width="2"/>')
    # nozes de palmeira (coquinhos), no centro
    for (x, y, a) in ((88, 80, -20), (104, 76, 10), (118, 86, 30), (94, 96, -40), (110, 98, 0)):
        s.append(f'<ellipse class="a" cx="{x}" cy="{y}" rx="7" ry="9" transform="rotate({a} {x} {y})" stroke-width="2.4"/>')
        s.append(f'<path stroke-width="1.3" opacity=".6" d="M{x - 3} {y - 2}q3 -3 6 0" transform="rotate({a} {x} {y})"/>')
    # chão
    s.append('<path stroke-width="2.4" d="M30 160H170"/>')
    for x in range(42, 166, 18):
        s.append(f'<path stroke-width="1.4" opacity=".5" d="M{x} 170h8"/>')
    return ''.join(s)


def orum():
    s = []
    s.append('<path class="c" stroke-width="3" d="M22 140A78 78 0 0 1 178 140Z"/>')
    s.append('<path stroke-width="1.6" opacity=".6" d="M36 140A64 64 0 0 1 164 140"/>')
    for (x, y, R) in ((100, 82, 7), (70, 104, 5), (132, 100, 5.5), (84, 120, 3.5), (120, 124, 4), (100, 106, 3)):
        s.append(f'<polygon class="t" stroke="none" points="{estrela(x, y, R, R * .32, 4)}"/>')
    s.append('<path stroke-width="3" d="M10 140H190"/>')
    for (y, op) in ((154, .5), (166, .35)):
        s.append(f'<path stroke-width="1.6" opacity="{op}" d="M30 {y}H170"/>')
    return ''.join(s)


def aie():
    s = []
    a0, a1 = polar(100, 104, 70, 180), polar(100, 104, 70, 360)
    s.append(f'<path stroke-width="1.8" stroke-dasharray="2 6" d="M{f(a0[0])} {f(a0[1])}A70 70 0 0 1 {f(a1[0])} {f(a1[1])}"/>')
    s.append('<path class="c" stroke-width="3" d="M10 104H190V200H10Z"/>')
    s.append('<path stroke-width="3" d="M10 104H190"/>')
    s.append('<path class="a" stroke-width="2.4" d="M24 104C50 92 74 90 100 98C126 90 150 92 176 104Z"/>')
    for i, y in enumerate((124, 144, 164, 184)):
        s.append(f'<path stroke-width="{2 - i * .2}" opacity="{.8 - i * .12}" d="{onda(y, 3, 50 - i * 6)}" transform="translate({i * 7} 0)"/>')
    return ''.join(s)


def odudua():
    s = []
    # água
    s.append(f'<path class="f" stroke-width="2.4" d="{onda(158, 4, 34)}V230H-20Z"/>')
    s.append(f'<path stroke-width="1.8" opacity=".7" d="{onda(174, 3.5, 34)}" transform="translate(9 0)"/>')
    # terra lançada sobre a água
    s.append('<path class="a" stroke-width="2.6" d="M44 160C56 140 80 132 100 132C120 132 144 140 156 160Z"/>')
    # dendezeiro de 16 ramos
    s.append('<path stroke-width="4.4" d="M100 136C98 112 104 88 100 62"/>')
    for y in range(72, 132, 10):
        s.append(f'<path stroke-width="1.6" d="M96 {y}h8"/>')
    for i in range(16):
        lado = -1 if i < 8 else 1
        k = i % 8
        ang = (-178 + k * 11) if lado < 0 else (-2 - k * 11)
        x1, y1 = polar(100, 60, 56 - abs(k - 3.5) * 3, ang)
        cx_, cy_ = polar(100, 56, 34, ang + (-10 if lado < 0 else 10))
        s.append(f'<path stroke-width="2.2" d="M100 60Q{f(cx_)} {f(cy_)} {f(x1)} {f(y1 + 8)}"/>')
    for (x, y) in ((95, 66), (105, 66), (100, 70)):
        s.append(f'<circle class="a" cx="{x}" cy="{y}" r="3.4" stroke-width="1.8"/>')
    return ''.join(s)


def olokun():
    s = []
    # sete correntes de ferro que descem ao fundo do mar
    for j, x in enumerate(range(40, 161, 20)):
        topo = 26 + abs(x - 100) * .5
        y = topo
        k = 0
        while y < 120:
            rx = 4.2 if k % 2 == 0 else 1.6
            s.append(f'<ellipse cx="{x}" cy="{f(y + 6)}" rx="{rx}" ry="7" stroke-width="2.2"/>')
            y += 11
            k += 1
    # mar profundo: camadas de ondas, a de baixo mais escura
    s.append(f'<path class="c" stroke-width="2.8" d="{onda(112, 6, 40)}V230H-20Z"/>')
    s.append(f'<path stroke-width="2.4" d="{onda(132, 5, 40)}" transform="translate(10 0)"/>')
    s.append(f'<path class="a" stroke-width="2.6" d="{onda(152, 5, 40)}V230H-20Z"/>')
    s.append(f'<path stroke-width="2" opacity=".7" d="{onda(172, 4, 34)}" transform="translate(6 0)"/>')
    return ''.join(s)


def ori():
    s = []
    # meia cabaça coberta de búzios
    s.append('<path class="c" stroke-width="3" d="M40 140A60 60 0 0 1 160 140Z"/>')
    s.append('<path stroke-width="3" d="M30 140H170"/>')
    for (r, n, a0, a1) in ((48, 9, 194, 346), (32, 6, 200, 340), (16, 3, 220, 320)):
        for i in range(n):
            ang = a0 + (a1 - a0) * i / (n - 1)
            x, y = polar(100, 140, r, ang)
            s.append(buzio(x, y, 13, 8.5, ang + 90, 'f'))
    s.append(buzio(100, 98, 13, 8.5, 90, 'f'))
    s.append('<path stroke-width="1.6" opacity=".5" d="M48 152H152M64 162H136"/>')
    return ''.join(s)


DESENHOS = {k: v for k, v in globals().items() if callable(v) and k in (
    'ogum iemanja xango exu oxossi oxum iansa nana omolu oxala ossaim oxumare logunede oba iroko ibeji orunmila '
    'orum aie odudua olokun ori').split()}
