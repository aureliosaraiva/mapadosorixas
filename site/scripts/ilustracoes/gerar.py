"""Gera site/src/assets/ilustracoes/<id>.svg a partir de desenhos.py e dos
metadados de data/ilustracoes.json (título/texto alternativo e acento).
Uso: python3 site/scripts/ilustracoes/gerar.py [ids...]"""
import json, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from base import svg
from desenhos import DESENHOS

RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
SAIDA = os.path.join(RAIZ, 'site', 'src', 'assets', 'ilustracoes')
META = os.path.join(RAIZ, 'data', 'ilustracoes.json')


def main(ids):
    meta = json.load(open(META, encoding='utf-8'))
    por_id = {i['entidade']: i for i in meta['ilustracoes']}
    os.makedirs(SAIDA, exist_ok=True)
    alvo = ids or list(por_id)
    for e in alvo:
        m = por_id[e]
        txt = svg(e, m['texto_alternativo'], m['cor']['acento'], DESENHOS[e]())
        open(os.path.join(SAIDA, f'{e}.svg'), 'w', encoding='utf-8').write(txt + '\n')
        print(f'{e}: {len(txt)} bytes')


if __name__ == '__main__':
    main(sys.argv[1:])
