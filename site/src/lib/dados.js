// Leitura dos dados gerados na raiz do repositório (data/). O site só exibe
// esses dados: nada sobre orixás é escrito aqui.
import catalogoJson from '../../../data/fontes/catalogo.json';
import conexoesJson from '../../../data/conexoes.json';
import entidadesJson from '../../../data/entidades_equivalentes.json';
import tradicoesJson from '../../../data/tradicoes.json';
import divergenciasJson from '../../../data/fichamento/divergencias.json';
import glossarioJson from '../../../data/glossario.json';
import revisoresJson from '../../../data/revisores.json';
import listaMestraJson from '../../../data/entidades.json';
import itansJson from '../../../data/itans.json';

const fichasMod = import.meta.glob('../../../data/orixas/*.json', { eager: true });
const fichamentoMod = import.meta.glob('../../../data/fichamento/*.json', { eager: true });

const valor = (m) => (m && m.default ? m.default : m);

// Lista-mestra (data/entidades.json): só identificadores. A ordem dela é a ordem
// de exibição (os 5 do MVP primeiro).
export const listaEntidades = listaMestraJson.entidades;
export const listaMeta = listaMestraJson._meta;
export const entidadePorId = Object.fromEntries(listaEntidades.map((e) => [e.id, e]));
const ORDEM = listaEntidades.map((e) => e.id);

export const fichas = Object.values(fichasMod)
  .map(valor)
  .sort((a, b) => ORDEM.indexOf(a.id) - ORDEM.indexOf(b.id));

export const fichaPorId = Object.fromEntries(fichas.map((f) => [f.id, f]));

export const ROTULO_TIPO_ENTIDADE = {
  orixa: 'Orixá',
  qualidade: 'Qualidade',
  divindade_suprema: 'Divindade suprema',
  conceito_cosmologico: 'Conceito cosmológico',
  ancestral: 'Ancestrais',
};
export const ROTULO_GRUPO_ENTIDADE = { funfun: 'Orixás funfun', aboro: 'Aborós', iaba: 'Iabás' };
// grupo só é exibido quando confirmado por registro fichado (ver data/entidades.json)
export const grupoConfirmado = (e) => (e?.grupo && e.grupo.confirmado_por.length ? e.grupo : null);

// Link de uma entidade: a ficha, se houver; senão o cartão "em pesquisa" no catálogo.
export function hrefEntidade(id) {
  if (fichaPorId[id]) return url(`orixas/${id}`);
  if (entidadePorId[id]) return url(`catalogo#e-${id}`);
  return null;
}
export const rotuloEntidade = (id) => entidadePorId[id]?.rotulo ?? rotuloNo(id);

// ---------------------------------------------------------------- itãs
// Só versões lidas na fonte (fichado/revisado) aparecem; itã sem nenhuma fica de fora.
const LIDO = new Set(['fichado', 'revisado']);
export const itansMeta = itansJson._meta;
export const itans = itansJson.itans
  .map((it) => ({ ...it, versoes: it.versoes.filter((v) => LIDO.has(v.status)) }))
  .filter((it) => it.versoes.length > 0);
export const itaPorId = Object.fromEntries(itans.map((it) => [it.id, it]));
export const itaDoRegistro = Object.fromEntries(itans.flatMap((it) => it.versoes.filter((v) => v.registro).map((v) => [v.registro, it])));

export const fontes = catalogoJson.fontes;
export const fontePorId = Object.fromEntries(fontes.map((f) => [f.id, f]));

export const conexoes = conexoesJson;
export const entidades = entidadesJson.entidades;
export const entidadesMeta = entidadesJson._meta;
export const tradicoes = tradicoesJson.tradicoes;
export const tradicoesMeta = tradicoesJson._meta;
export const tradicaoPorId = Object.fromEntries(tradicoes.map((t) => [t.id, t]));
export const divergencias = divergenciasJson.divergencias;
export const glossario = [...glossarioJson.termos].sort((a, b) => a.termo.localeCompare(b.termo, 'pt-BR'));
export const glossarioMeta = glossarioJson._meta;
export const termoPorId = Object.fromEntries(glossario.map((t) => [t.id, t]));

// Registros de fichamento (para números da metodologia)
export const registros = Object.entries(fichamentoMod)
  .filter(([caminho]) => !caminho.endsWith('divergencias.json'))
  .flatMap(([, m]) => valor(m).registros);

// ---------------------------------------------------------------- rótulos

export const ROTULO_ATRIBUTO = {
  nomes: 'Nomes',
  origem: 'Origem',
  dominios: 'Domínios',
  funcoes: 'Funções',
  elementos: 'Elementos',
  cores: 'Cores',
  dia_semana: 'Dia da semana',
  saudacao: 'Saudação',
  simbolos: 'Símbolos e ferramentas',
  alimentos: 'Alimentos rituais',
  animais: 'Animais',
  qualidades: 'Qualidades',
  parentesco: 'Parentesco nos itãs',
  equivalencias: 'Equivalências entre tradições',
  sincretismo: 'Sincretismo',
  itans: 'Itãs (resumos parafraseados)',
  tabus: 'Tabus',
  festas: 'Festas e calendário',
  historia_culto: 'História do culto',
  iconografia: 'Iconografia',
  interpretacao_academica: 'Interpretação acadêmica',
  hierarquia: 'Hierarquia e posição cosmológica',
};
export const ORDEM_ATRIBUTOS = Object.keys(ROTULO_ATRIBUTO);
export const rotuloAtributo = (a) => ROTULO_ATRIBUTO[a] || a;

export const ROTULO_GRUPO = {
  culto_africano: 'Culto na África',
  candomble: 'Candomblé',
  afro_brasileira_regional: 'Religiões afro-brasileiras regionais',
  umbanda: 'Umbanda',
  diaspora_caribenha: 'Diáspora caribenha',
};

// Ordem de exibição dos grupos na página Tradições: Candomblé (nações), demais
// religiões afro-brasileiras, Umbanda, culto na África, diáspora caribenha.
export const ORDEM_GRUPOS = ['candomble', 'afro_brasileira_regional', 'umbanda', 'culto_africano', 'diaspora_caribenha'];

export const ROTULO_CATEGORIA_GLOSSARIO = {
  divindade_e_entidade: 'Divindades e entidades',
  cargo_e_pessoa: 'Cargos e pessoas',
  religiao_e_grupo: 'Religiões e grupos',
  lugar_e_objeto: 'Lugares e objetos',
  rito_e_oferenda: 'Ritos e oferendas',
  musica_e_danca: 'Música, dança e louvação',
  adivinhacao: 'Adivinhação',
  conceito: 'Conceitos',
};

export const rotuloTradicao = (id) => {
  const t = tradicaoPorId[id];
  return t ? t.nome : id;
};
// rótulo curto: sem o parêntese final
export const rotuloTradicaoCurto = (id) => rotuloTradicao(id).replace(/\s*\(.*\)\s*$/, '');
export const grupoTradicao = (id) => tradicaoPorId[id]?.grupo || 'outro';

export const ROTULO_ARESTA = {
  parentesco: 'Parentesco (itãs)',
  equivalencia: 'Equivalência entre tradições',
  sincretismo: 'Sincretismo',
  companheiro_de_culto: 'Companheiro de culto',
  associacao: 'Associação',
};
export const ROTULO_SUBTIPO = {
  conjuge_de: 'cônjuge de',
  filho_de: 'filho(a) de',
  senhor_de: 'senhor de',
  irmao_de: 'irmão(ã) de',
};
export const ROTULO_NO = {
  orixa: 'Orixá',
  santo_catolico: 'Santo católico',
  figura_crista: 'Figura cristã',
  vodum: 'Vodum',
  inquice: 'Inquice',
  nome_fon_ou_banto: 'Nome fon ou banto (não classificado)',
  entidade: 'Entidade',
};

export const ROTULO_TIPO_FONTE = {
  livro: 'Livro', capitulo: 'Capítulo', artigo: 'Artigo', tese: 'Tese',
  dissertacao: 'Dissertação', site: 'Site', audiovisual: 'Audiovisual',
  acervo: 'Acervo', documento: 'Documento',
};
export const ROTULO_IDIOMA = {
  pt: 'Português', en: 'Inglês', es: 'Espanhol', fr: 'Francês',
  de: 'Alemão', it: 'Italiano', yo: 'Iorubá',
};
export const ROTULO_STATUS = {
  pista: 'Pista (não verificada)',
  a_verificar: 'A verificar',
  conferido_web: 'Conferido na web',
  verificado: 'Verificado',
  fichado: 'Fichado',
  revisado: 'Revisado',
};
// Rubrica de docs/PLANO.md §1.5
export const ROTULO_CONFIABILIDADE = {
  A: 'A — pesquisa revisada por pares, etnografia documentada, corpus oral publicado, obra de sacerdote/a reconhecido/a',
  B: 'B — divulgação séria com bibliografia, dicionários especializados, registros oficiais',
  C: 'C — sites de terreiros, entrevistas, enciclopédias gerais (só indicação de prática corrente)',
  D: 'D — blogs sem autoria, conteúdo comercial (só pista)',
};

// ---------------------------------------------------------------- citações

function sobrenome(nome) {
  const partes = nome.replace(/\(orgs?\.\)/g, '').trim().split(/\s+/);
  return partes[partes.length - 1];
}

export function autorCurto(fonte) {
  if (!fonte) return '?';
  const a = fonte.autores || [];
  if (a.length === 0) return '?';
  if (a.length === 1) return sobrenome(a[0]);
  if (a.length === 2) return `${sobrenome(a[0])} & ${sobrenome(a[1])}`;
  return `${sobrenome(a[0])} et al.`;
}

export function chaveCurta(id) {
  const f = fontePorId[id];
  if (!f) return id;
  return `${autorCurto(f)} (${f.ano ?? 's.d.'})`;
}

// Fontes usadas nas fichas: id -> nº de versões que a citam
export const usoDasFontes = (() => {
  const uso = {};
  const somar = (id) => { if (id) uso[id] = (uso[id] || 0) + 1; };
  for (const f of fichas) {
    for (const versoes of Object.values(f.atributos)) {
      for (const v of versoes) for (const s of v.sources) { somar(s.id); somar(s.via); }
    }
  }
  // versões de itã redigidas direto em data/itans.json (as espelhadas já contam na ficha)
  for (const it of itans) for (const v of it.versoes) if (!v.registro) for (const s of v.sources) { somar(s.id); somar(s.via); }
  return uso;
})();

// ---------------------------------------------------------------- revisão do conselho
// Crédito conforme o termo de consentimento (data/revisores.json). A mesma regra
// está em scripts/revisao.py (quem, linha_credito), usada pelo QA do site.

export const revisores = revisoresJson.revisores;
export const revisorPorId = Object.fromEntries(revisores.map((r) => [r.id, r]));
const ANONIMO = 'revisor/a anônimo/a';
const VERBO_REVISAO = { aprovado: 'Revisado', aprovado_com_ressalva: 'Revisado com ressalva', contestado: 'Contestado' };

export function quemRevisou(id) {
  const r = revisorPorId[id];
  if (!r || r.consentimento?.revogado_em || r.credito === 'anonimo') return ANONIMO;
  if (r.credito === 'so_nome') return r.nome_publico;
  if (r.credito === 'generico') return r.descricao_publica;
  return `${r.nome_publico}, ${r.descricao_publica}`;
}

const dataBr = (iso) => iso.split('-').reverse().join('/');

// "Revisado por … (tradição) em dd/mm/aaaa[: nota]"
export function linhaRevisao(rv) {
  const t = `${VERBO_REVISAO[rv.parecer]} por ${quemRevisou(rv.revisor)} (${rotuloTradicao(rv.tradicao)}) em ${dataBr(rv.data)}`;
  return rv.nota ? `${t}: ${rv.nota}` : t;
}

export const versoesRevisadas = (ficha) =>
  Object.values(ficha.atributos).reduce((n, vs) => n + vs.filter((v) => v.status === 'revisado').length, 0);

// O selo de rascunho só sai quando TODAS as versões publicadas têm revisão vigente
// (critério da proposta; a confirmar com o autor).
export const fichaRevisada = (ficha) => totalVersoes(ficha) > 0 && versoesRevisadas(ficha) === totalVersoes(ficha);

// ---------------------------------------------------------------- utilidades

export function url(caminho = '') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}/${caminho.replace(/^\//, '')}`;
}

export function tradicoesDaFicha(ficha) {
  const s = new Set();
  for (const versoes of Object.values(ficha.atributos)) for (const v of versoes) v.tradicoes.forEach((t) => s.add(t));
  return [...s].sort((a, b) => tradicoes.findIndex((t) => t.id === a) - tradicoes.findIndex((t) => t.id === b));
}

export function totalVersoes(ficha) {
  return Object.values(ficha.atributos).reduce((n, v) => n + v.length, 0);
}

export function fontesDaFicha(ficha) {
  const s = new Set();
  for (const versoes of Object.values(ficha.atributos)) for (const v of versoes) for (const x of v.sources) s.add(x.id);
  return s;
}

export function rotuloNo(id) {
  const n = conexoes.nos.find((x) => x.id === id);
  return n ? n.rotulo : id;
}

// ---------------------------------------------------------------- glossário nas fichas

const escapar = (t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
// Formas procuradas no texto: termo e variantes, das mais longas às mais curtas.
// Ficam de fora formas com parêntese ("exu (entidade de Umbanda)") e formas que
// coincidem com nomes de orixá nas fichas (ex.: "exus"), para não ligar o orixá
// à entidade de Umbanda. Também ficam de fora variantes que são palavras comuns do
// português com outro sentido ("lado", "despacho", "invocação", "avatar").
const FORMAS_COMUNS = new Set(['lado', 'despacho', 'invocação', 'avatar']);
// Formas ambíguas (iguais em dois termos, como "ita" para itã e otá) também ficam de fora.
const contagemFormas = {};
for (const t of glossario) for (const f of new Set([t.termo, ...t.variantes].map((x) => x.toLocaleLowerCase('pt-BR')))) contagemFormas[f] = (contagemFormas[f] || 0) + 1;
const FORMAS_GLOSSARIO = glossario
  .flatMap((t) => [t.termo, ...t.variantes].map((f) => ({ f, id: t.id })))
  .filter(({ f }) => contagemFormas[f.toLocaleLowerCase('pt-BR')] === 1)
  .filter(({ f, id }) => !f.includes('(') && id !== 'exu-entidade' && f.length >= 3 && !FORMAS_COMUNS.has(f.toLocaleLowerCase('pt-BR')))
  .sort((a, b) => b.f.length - a.f.length);
const RE_GLOSSARIO = new RegExp(
  `(?<![\\p{L}\\p{N}])(${FORMAS_GLOSSARIO.map((x) => escapar(x.f)).join('|')})(?:s|es)?(?![\\p{L}\\p{N}])`,
  'giu',
);
const idDaForma = Object.fromEntries(FORMAS_GLOSSARIO.map(({ f, id }) => [f.toLocaleLowerCase('pt-BR'), id]));

/**
 * Divide um texto em pedaços [{texto}|{texto, termo}] marcando a PRIMEIRA ocorrência
 * de cada termo do glossário ainda não marcado na página (`vistos` é compartilhado
 * entre as chamadas da mesma página). O texto em si não muda.
 */
export function marcarGlossario(texto, vistos) {
  if (!texto) return [];
  const partes = [];
  let ultimo = 0;
  for (const m of texto.matchAll(RE_GLOSSARIO)) {
    const id = idDaForma[m[1].toLocaleLowerCase('pt-BR')];
    if (!id || vistos.has(id)) continue;
    vistos.add(id);
    if (m.index > ultimo) partes.push({ texto: texto.slice(ultimo, m.index) });
    partes.push({ texto: m[0], termo: id });
    ultimo = m.index + m[0].length;
  }
  if (ultimo < texto.length) partes.push({ texto: texto.slice(ultimo) });
  return partes;
}
