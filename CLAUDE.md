# Projeto: Enciclopédia interativa dos Orixás

## Contexto e motivação
- Não existe hoje um portal único, organizado e com fontes citadas sobre orixás (origem, história, itãs, símbolos, variações por nação).
- Sites existentes (Significados, Toda Matéria, Wikipédia) são introdutórios e raramente citam fontes.
- Acervos sérios existem, mas são dispersos (ex.: Museu Afro Digital da UFBA, mais imagem/acervo que texto).
- Oportunidade: um projeto curado, com fontes por ficha e que mostre explicitamente as divergências entre tradições.

## Referência de formato
https://mapadelaconsciencia.es/ — enciclopédia interativa de teorias da consciência (222 teorias, 864 conexões), feita com Claude. NÃO trata de orixás; serve só como modelo de formato:
- Catálogo com filtros e busca
- Grafo interativo de conexões
- Fichas com fontes citadas (autor + ano)
- Página de metodologia e limitações
- Bilíngue (es/en)

## Escopo proposto
- **Catálogo** de orixás com filtros: nação (Ketu, Jeje, Bantu), elemento, domínios, região de origem na África.
- **Grafo de conexões** (diferencial): parentesco nos itãs, equivalências entre tradições (inquices bantos, voduns jeje, Santería/Lucumí cubana, culto iorubá na Nigéria), sincretismo com santos católicos.
- **Ficha por orixá**: nomes por nação, origem, domínios, elementos, cores, dia da semana, saudação, símbolos/ferramentas, sincretismo, resumo de itãs (parafraseados), divergências entre casas/nações, fontes.
- **Metodologia e limitações**: tradição oral, variação entre casas, nenhum panteão único e idêntico nem mesmo em território iorubá.
- **Idiomas**: pt-BR primeiro; depois es e en (público hispânico da Santería/Lucumí).

## MVP
1. Esquema de dados (JSON) para orixás, nações, conexões e fontes.
2. 5 orixás iniciais: Exu, Ogum, Oxóssi, Xangô, Iemanjá.
3. Site estático com catálogo + ficha + grafo.
4. Depois expandir para ~15 orixás principais cultuados no Brasil.

## Regras de conteúdo (obrigatórias)
- Toda afirmação factual deve ter fonte em `sources` na ficha.
- NUNCA copiar trechos de livros (Prandi, *Mitologia dos Orixás*; Pierre Verger; Roger Bastide etc.). Sempre parafrasear e citar.
- Quando fontes divergirem, registrar as versões lado a lado indicando nação/casa, sem escolher uma "correta".
- Tom respeitoso; conteúdo deve ser revisado por praticantes (babalorixás/iyalorixás) e/ou pesquisadores antes de publicar.
- Distinguir claramente Candomblé (e suas nações) de Umbanda.

## Fontes de referência
- Reginaldo Prandi — *Mitologia dos Orixás*
- Pierre Verger — *Orixás*; *Notas sobre o culto aos orixás e voduns*
- Roger Bastide
- Artigos acadêmicos (Google Scholar, SciELO, repositórios USP/UFBA/UNESP)
- Museu Afro Digital UFBA: https://museuafrodigitalufba.org/orixas-2/

## Domínio (não verificado)
Candidatos a checar: atlasdosorixas.com.br, enciclopediaorixas.com.br, panteaoorixa.com.br, orixas.wiki, orixas.info.
Obs.: o autor mora na Espanha; `.com.br` exige CPF/CNPJ — `.com`/`.org` evita isso.

## Stack
A definir. Sugestão inicial: site estático (ex.: Astro ou Next.js export) + dados em JSON versionados no repo + grafo com D3/Cytoscape.js. Deploy em GitHub Pages, Vercel ou Cloudflare Pages.

## Idioma de trabalho
Responder e documentar em português do Brasil.

## Registro de bloqueios
- Todo acesso bloqueado (domínio inacessível, 403/404, paywall, obra só impressa) ou conferência que dependa de pessoa deve ser registrado em `docs/pesquisa/PENDENCIAS.md`, com status, o que está atrás do bloqueio e prioridade. O autor resolve depois; não substituir por conteúdo inventado.

## Fluxo entre sessões
- **Abertura:** toda sessão começa com `git pull origin main` e lendo `docs/ESTADO.md` (estado atual, próximas tarefas, decisões já tomadas). Não reler relatórios inteiros sem necessidade.
- **Escopo:** uma sessão = uma tarefa fechada (uma fonte, um orixá, um lote de pendências ou uma fase).
- **Fechamento:** rodar os validadores (`scripts/validar_fontes.py`, `scripts/validar_fichamento.py`, `scripts/divergencias.py`, `scripts/gerar_fichas.py`, `scripts/validar_fichas.py`, `scripts/anticopia.py`), atualizar `docs/ESTADO.md` (números, próximas tarefas, decisões novas) e `docs/pesquisa/PENDENCIAS.md`, depois commit e push direto na `main`.
- **Anti-cópia com o texto integral (obrigatório):** toda sessão que ficha uma fonte (fichamento, tradições ou glossário) roda o anti-cópia com o texto integral dessa fonte **antes do commit**: `python3 scripts/baixar_refs.py` (procura primeiro no acervo e só baixa o que falta, gravando no acervo: `pdf/<source_id>.pdf`, `txt/<source_id>.txt`, `indice.json`; PDF salvo à mão em `pdf/` + `--so-converter`) e depois `python3 scripts/anticopia.py` (usa o `txt/` do acervo por padrão). Meta: 0 erros; cada aviso "próximo" (6–7 palavras iguais à fonte citada) é reescrito ou justificado no relatório da sessão (nome, lista, data, termo técnico, expressão corrente). Fonte que não baixar vai para `PENDENCIAS.md`.
- **Acervo (texto integral das fontes) = repositório PRIVADO `aureliosaraiva/orixas-fontes`** (decisão do autor, sessão acervo2): uso interno de pesquisa (leitura, releitura, anti-cópia); **nunca vai para o site**, para `/dados/` (o `qa_site.py` confere) nem para este repositório, que é **público**. **Início da sessão:** anexar o repo (`add_repo`, owner `aureliosaraiva`, repo `orixas-fontes`, access `push`) e rodar `scripts/acervo_sync.sh pull` (clona/atualiza em `../orixas-fontes`; outro lugar: variável `ACERVO_DIR`). **Fim da sessão:** `scripts/acervo_sync.sh push` (commit e push dos textos novos direto na `main` do `orixas-fontes`). Sem o clone, os scripts caem no `acervo/` local, que o `.gitignore` mantém fora do git; os workflows deste repo falham se algum PDF/texto de `acervo/` for versionado. Não tornar o `orixas-fontes` público. Ver `acervo/LEIAME.md`.
- **Capítulos narrativos:** `data/capitulos/<id>.md` reconta o fichamento em prosa, sem citação no corpo (atribuição pela tradição/casa; autor na nota de rodapé); regras em `docs/capitulos-guia.md`, e toda sessão que mexe em capítulos ou no fichamento dos orixás com capítulo roda também `scripts/validar_capitulos.py --gerar`.
- **Paralelismo:** sessões simultâneas só em arquivos diferentes; `data/fontes/catalogo.json` é editado por uma sessão de cada vez.
