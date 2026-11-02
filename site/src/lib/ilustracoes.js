// Ilustrações simbólicas (sessão ilustra): SVG desenhados em código, um por entidade,
// em src/assets/ilustracoes/<id>.svg, com metadados em data/ilustracoes.json.
// Entidade sensível nunca recebe ilustração, mesmo que exista arquivo.
import meta from '../../../data/ilustracoes.json';
import { entidadePorId } from './dados.js';

const arquivos = import.meta.glob('../assets/ilustracoes/*.svg', { query: '?raw', import: 'default', eager: true });
const svgPorId = Object.fromEntries(Object.entries(arquivos).map(([p, txt]) => [p.split('/').pop().replace('.svg', ''), txt]));

export const LEGENDA_ILUSTRACAO = 'Ilustração simbólica inspirada nos elementos descritos nas fontes';

export const ilustracaoPorId = Object.fromEntries(meta.ilustracoes
  .filter((m) => svgPorId[m.entidade] && !entidadePorId[m.entidade]?.sensivel)
  .map((m) => [m.entidade, { ...m, svg: svgPorId[m.entidade] }]));
