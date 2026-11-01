// Estilo visual do grafo (página Grafo e mini-grafo das fichas). Cor nunca é o
// único código: nós têm formas e arestas têm estilos de linha diferentes.
import { conexoes, fichaPorId, entidadePorId, ROTULO_TIPO_ENTIDADE, ROTULO_NO, url } from './dados.js';

export const CORES_ARESTA = {
  parentesco: { cor: '#6b3b8f', estilo: 'solid' },
  equivalencia: { cor: '#1d6b4a', estilo: 'dashed' },
  sincretismo: { cor: '#22578f', estilo: 'dotted' },
  companheiro_de_culto: { cor: '#8a5a00', estilo: 'solid' },
  associacao: { cor: '#555555', estilo: 'dashed' },
};
export const FORMA_NO = {
  orixa: { forma: 'ellipse', cor: '#7a3b12', rotulo: 'círculo' },
  santo_catolico: { forma: 'round-rectangle', cor: '#22578f', rotulo: 'retângulo' },
  figura_crista: { forma: 'diamond', cor: '#22578f', rotulo: 'losango' },
  vodum: { forma: 'hexagon', cor: '#1d6b4a', rotulo: 'hexágono' },
  inquice: { forma: 'triangle', cor: '#1d6b4a', rotulo: 'triângulo' },
  nome_fon_ou_banto: { forma: 'vee', cor: '#4f6b5e', rotulo: 'seta (V)' },
  entidade: { forma: 'octagon', cor: '#8a5a00', rotulo: 'octógono' },
};
export const ROTULO_LINHA = { solid: 'contínua', dashed: 'tracejada', dotted: 'pontilhada' };

// Tipo de entidade de um nó, para o filtro do grafo: o `tipo` da lista-mestra
// (orixá, qualidade, divindade suprema…) quando o nó está nela; senão o tipo do nó
// no mapa do grafo (santo católico, vodum, inquice…).
export const tipoEntidadeNo = (n) => entidadePorId[n.id]?.tipo ?? n.tipo;
export const rotuloTipoEntidade = (t) => ROTULO_TIPO_ENTIDADE[t] ?? ROTULO_NO[t] ?? t;

export const tradDaAresta = (e) => [...new Set(e.versoes.flatMap((v) => v.tradicoes))];

// Elementos Cytoscape para um conjunto de nós e arestas de data/conexoes.json.
export function elementosCytoscape(nos, arestas) {
  return [
    ...nos.map((n) => ({
      data: {
        id: n.id, label: n.rotulo, tipo: n.tipo, tipoEnt: tipoEntidadeNo(n),
        cor: FORMA_NO[n.tipo]?.cor ?? '#666', forma: FORMA_NO[n.tipo]?.forma ?? 'ellipse',
        href: fichaPorId[n.id] ? url(`orixas/${n.id}`) : '',
      },
    })),
    ...arestas.map((e) => ({
      data: {
        id: e.id, source: e.origem, target: e.destino, tipo: e.tipo,
        cor: CORES_ARESTA[e.tipo]?.cor ?? '#555', estilo: CORES_ARESTA[e.tipo]?.estilo ?? 'solid',
        seta: e.direcionada ? 'triangle' : 'none',
        tradicoes: tradDaAresta(e),
      },
    })),
  ];
}

// Vizinhança direta de um nó: as arestas que o tocam e os nós nas pontas.
export function vizinhanca(id) {
  const arestas = conexoes.arestas.filter((e) => e.origem === id || e.destino === id);
  const ids = new Set([id, ...arestas.flatMap((e) => [e.origem, e.destino])]);
  return { nos: conexoes.nos.filter((n) => ids.has(n.id)), arestas };
}
