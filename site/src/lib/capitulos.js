// Capítulos narrativos (data/capitulos/<id>.json, gerados de <id>.md por
// scripts/validar_capitulos.py --gerar). O site só exibe o JSON: o texto é do
// projeto e cada nota remete a registros do fichamento (fichado/revisado).
import { registros, fontePorId, autorCurto, fichaPorId, rotuloAtributo, rotuloTradicao, url, entidadePorId } from './dados.js';

const mods = import.meta.glob('../../../data/capitulos/*.json', { eager: true });
const valor = (m) => (m && m.default ? m.default : m);

const ORDEM = Object.keys(entidadePorId);
const todos = Object.values(mods).map(valor);
export const capitulos = todos
  .filter((c) => c.orixa && fichaPorId[c.orixa])
  .sort((a, b) => ORDEM.indexOf(a.orixa) - ORDEM.indexOf(b.orixa));
export const capituloPorId = Object.fromEntries(capitulos.map((c) => [c.orixa, c]));
// Capítulos-panorama (tipo "panorama"): costura de vários capítulos; rota /<id>/capitulo/
export const panoramas = todos.filter((c) => c.tipo === 'panorama').sort((a, b) => a.id.localeCompare(b.id));
export const panoramaPorId = Object.fromEntries(panoramas.map((c) => [c.id, c]));

export const TITULO_SECAO = {
  'nomes-e-origem': 'Nomes e origem',
  'historia-do-culto': 'História do culto',
  'dominios-e-simbolos': 'Domínios, elementos e símbolos',
  mitos: 'Mitos',
  tradicoes: 'Em cada tradição',
  sincretismo: 'Sincretismo',
  'leituras-academicas': 'Leituras acadêmicas',
  lacunas: 'O que as fontes não dizem',
  // panorama
  hierarquia: 'Hierarquia',
  'planos-do-mundo': 'Os planos do mundo',
  'a-pessoa': 'A pessoa e o Orí',
  ancestrais: 'Os ancestrais',
};

const regPorId = Object.fromEntries(registros.map((r) => [r.id, r]));
export const registro = (id) => {
  const r = regPorId[id];
  if (!r) throw new Error(`Capítulo cita registro inexistente: ${id}`);
  if (r.status !== 'fichado' && r.status !== 'revisado') throw new Error(`Capítulo cita registro não fichado: ${id}`);
  return r;
};

export const PENDENCIAS_URL = 'https://github.com/aureliosaraiva/mapadosorixas/blob/main/docs/pesquisa/PENDENCIAS.md';

// Fontes citadas no capítulo (fonte lida e, se houver, a obra citada por ela), por autor
export function bibliografia(cap) {
  const ids = new Set();
  for (const n of cap.notas) for (const it of n.itens) {
    if (it.tipo !== 'registro') continue;
    const r = registro(it.registro);
    ids.add(r.source_id);
    if (r.via_source_id) ids.add(r.via_source_id);
  }
  return [...ids].map((id) => fontePorId[id]).filter(Boolean)
    .sort((a, b) => autorCurto(a).localeCompare(autorCurto(b), 'pt-BR') || (a.ano ?? 0) - (b.ano ?? 0));
}

export const totalPalavras = (cap) => cap.secoes.reduce((n, s) => n + s.blocos.reduce((m, b) => m + (b.tipo === 'paragrafo'
  ? b.tokens.reduce((k, t) => k + (t.t === 'texto' ? t.v.split(/\s+/).filter(Boolean).length : t.t === 'link' ? t.rotulo.split(/\s+/).length : 0), 0)
  : 0), 0), 0);

export const registrosCitados = (cap) => new Set(cap.notas.flatMap((n) => n.itens.filter((i) => i.tipo === 'registro').map((i) => i.registro)));

// Divide um texto em pedaços [{texto, italico}] a partir de *itálico*
export function italicos(texto) {
  return texto.split(/(\*[^*]+\*)/).filter(Boolean).map((p) => (p.startsWith('*') && p.endsWith('*') && p.length > 2
    ? { texto: p.slice(1, -1), italico: true }
    : { texto: p, italico: false }));
}

export function hrefLink(t) {
  switch (t.tipo) {
    case 'ita': return url(`itans/${t.alvo}`);
    case 'orixa': return url(`orixas/${t.alvo}`);
    case 'glossario': return url(`glossario#termo-${t.alvo}`);
    case 'tradicao': return url(`tradicoes#t-${t.alvo}`);
    case 'grafo': return url('grafo');
    case 'capitulo': return url(`orixas/${t.alvo}/capitulo`);
    default: throw new Error(`link desconhecido ${t.tipo}`);
  }
}

export const textoLacuna = (it, cap) => `Nenhum registro fichado de “${rotuloAtributo(it.atributo)}”${it.tradicao ? ` na tradição ${rotuloTradicao(it.tradicao)}` : ''} para ${fichaPorId[cap.orixa].rotulo} (conferido pelo validador).`;
