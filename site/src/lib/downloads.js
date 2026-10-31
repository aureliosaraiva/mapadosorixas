// Arquivos publicados em /dados/ no build (página "Baixar dados").
// Só entram os dados PÚBLICOS gerados (fichas, grafo, entidades, divergências,
// catálogo de fontes, glossário). O fichamento bruto (data/fichamento/<orixa>.json) NÃO é
// publicado: contém registros em pré-fichamento e registros retidos até decisão
// do conselho (tabus e alimentos rituais).
import { readFileSync, readdirSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import path from 'node:path';

// O build roda dentro de site/; os dados ficam na raiz do repositório.
const DATA = path.resolve(process.cwd(), '..', 'data');

export const LICENCA = 'Licença dos dados: a definir pelo autor. Enquanto não houver licença, consulte o autor pelo repositório antes de reutilizar.';

const ler = (rel) => readFileSync(path.join(DATA, rel));

// Tradições: descrições com status rascunho_sem_fonte não têm fonte lida e não são
// exibidas no site (a página Tradições mostra "descrição pendente de fonte");
// no arquivo publicado elas ficam com descricao: null.
function tradicoesPublicas() {
  const t = JSON.parse(ler('tradicoes.json').toString('utf-8'));
  const tradicoes = t.tradicoes.map((x) => {
    if (x.status === 'rascunho_sem_fonte') {
      const { descricao, ...resto } = x;
      return { ...resto, descricao: null };
    }
    return x;
  });
  const meta = { ...t._meta, publicacao: 'Cópia publicada pelo site: descrições com status rascunho_sem_fonte foram removidas (descricao: null) até terem fonte.' };
  return Buffer.from(JSON.stringify({ _meta: meta, tradicoes }, null, 2) + '\n', 'utf-8');
}

function leiame(arquivos) {
  const linhas = [
    'Mapa dos Orixás — dados publicados (rascunho)',
    '',
    LICENCA,
    '',
    'Conteúdo ainda NÃO revisado por praticantes (babalorixás, iyalorixás) nem por pesquisadores.',
    'Cada versão traz fonte (source_id) e página (localizacao); as fontes estão em fontes.json.',
    'Os arquivos são cópias de data/ no repositório https://github.com/aureliosaraiva/mapadosorixas',
    'gerados por scripts/gerar_fichas.py e scripts/divergencias.py. Não incluem o fichamento bruto',
    '(registros em pré-fichamento e registros retidos até decisão do conselho).',
    '',
    'Arquivos:',
    ...arquivos.map((a) => `- ${a.caminho}: ${a.descricao} (sha256 ${a.sha256})`),
    '',
  ];
  return Buffer.from(linhas.join('\n'), 'utf-8');
}

function montar() {
  const lista = [];
  const add = (caminho, descricao, conteudo, origem) =>
    lista.push({ caminho, descricao, conteudo, origem, bytes: conteudo.length, sha256: createHash('sha256').update(conteudo).digest('hex') });

  for (const nome of readdirSync(path.join(DATA, 'orixas')).filter((n) => n.endsWith('.json')).sort()) {
    const rotulo = JSON.parse(ler(`orixas/${nome}`).toString('utf-8')).rotulo;
    add(`orixas/${nome}`, `ficha de ${rotulo} (versões com fonte e página)`, ler(`orixas/${nome}`), `data/orixas/${nome}`);
  }
  add('conexoes.json', 'grafo: nós e arestas com versões e fontes', ler('conexoes.json'), 'data/conexoes.json');
  add('entidades_equivalentes.json', 'voduns, inquices e outros nomes equivalentes', ler('entidades_equivalentes.json'), 'data/entidades_equivalentes.json');
  add('divergencias.json', 'atributos com mais de uma versão, lado a lado', ler('fichamento/divergencias.json'), 'data/fichamento/divergencias.json');
  add('fontes.json', 'catálogo de fontes com status de verificação', ler('fontes/catalogo.json'), 'data/fontes/catalogo.json');
  if (existsSync(path.join(DATA, 'glossario.json'))) {
    add('glossario.json', 'glossário de termos, com fonte e página', ler('glossario.json'), 'data/glossario.json');
  }
  add('tradicoes.json', 'tradições (id, nome e grupo; descrições sem fonte removidas)', tradicoesPublicas(), 'data/tradicoes.json (filtrado)');
  add('LEIAME.txt', 'aviso de licença e descrição dos arquivos', leiame(lista), 'gerado no build');
  return lista;
}

export const arquivosDados = montar();
