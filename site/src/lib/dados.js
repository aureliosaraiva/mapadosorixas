// Leitura dos dados gerados na raiz do repositório (data/). O site só exibe
// esses dados: nada sobre orixás é escrito aqui.
import catalogoJson from '../../../data/fontes/catalogo.json';
import conexoesJson from '../../../data/conexoes.json';
import entidadesJson from '../../../data/entidades_equivalentes.json';
import tradicoesJson from '../../../data/tradicoes.json';
import divergenciasJson from '../../../data/fichamento/divergencias.json';

const fichasMod = import.meta.glob('../../../data/orixas/*.json', { eager: true });
const fichamentoMod = import.meta.glob('../../../data/fichamento/*.json', { eager: true });

const valor = (m) => (m && m.default ? m.default : m);

// Ordem do MVP (CLAUDE.md)
const ORDEM = ['exu', 'ogum', 'oxossi', 'xango', 'iemanja'];

export const fichas = Object.values(fichasMod)
  .map(valor)
  .sort((a, b) => ORDEM.indexOf(a.id) - ORDEM.indexOf(b.id));

export const fichaPorId = Object.fromEntries(fichas.map((f) => [f.id, f]));

export const fontes = catalogoJson.fontes;
export const fontePorId = Object.fromEntries(fontes.map((f) => [f.id, f]));

export const conexoes = conexoesJson;
export const entidades = entidadesJson.entidades;
export const entidadesMeta = entidadesJson._meta;
export const tradicoes = tradicoesJson.tradicoes;
export const tradicoesMeta = tradicoesJson._meta;
export const tradicaoPorId = Object.fromEntries(tradicoes.map((t) => [t.id, t]));
export const divergencias = divergenciasJson.divergencias;

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
  const partes = nome.trim().split(/\s+/);
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
  return uso;
})();

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
