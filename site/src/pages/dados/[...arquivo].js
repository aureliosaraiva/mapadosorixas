// Publica cópias dos dados em /dados/<arquivo> (ver src/lib/downloads.js).
import { arquivosDados } from '../../lib/downloads.js';

export function getStaticPaths() {
  return arquivosDados.map((a) => ({ params: { arquivo: a.caminho }, props: { a } }));
}

export function GET({ props }) {
  const tipo = props.a.caminho.endsWith('.json') ? 'application/json; charset=utf-8' : 'text/plain; charset=utf-8';
  return new Response(props.a.conteudo, { headers: { 'Content-Type': tipo } });
}
