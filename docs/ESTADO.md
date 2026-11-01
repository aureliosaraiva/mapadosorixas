# Estado do projeto

> Arquivo de passagem entre sessões. **Toda sessão começa lendo este arquivo e termina atualizando-o.** Mantenha-o curto, com no máximo uma página: o detalhe fica nos relatórios linkados.

**Última atualização:** 2026-11-01 (sessões trad02, fichamento-06, fichamento-07, revisao e anticopia)

## Onde estamos

**Fase 1 — Levantamento e fichamento** (em andamento), **Fase 2 — Modelo de dados** (iniciada: esquemas, fichas geradas e grafo) e **Fase 5 — Site estático: protótipo feito** (`site/`, Astro + Cytoscape.js + Pagefind; compila no CI, sem deploy). Ver [`PLANO.md`](PLANO.md). **Fase 4 — Conselho: preparação feita** ([`conselho/`](conselho/): candidatos, kit do revisor, proposta do campo `revisao`) e **registro da revisão implementado** (passos 1–3 da proposta; [`conselho/como-registrar-revisao.md`](conselho/como-registrar-revisao.md)); contato e convites dependem do autor. Fases 3, 6 e 7 ainda não começaram.

| Indicador | Valor | Como conferir |
|---|---:|---|
| Fontes no catálogo | 316 (227 `conferido_web`, 62 `a_verificar`, 27 `pista`); **todas as fontes usadas no fichamento estão `conferido_web` ou acima**. Varredura 3 (coleta por API): +129 `conferido_web`, +17 `pista`, 11 promovidas ([relatório](pesquisa/relatorio-varredura-03.md)) | `python3 scripts/validar_fontes.py` |
| Registros de fichamento | 302 (286 `fichado`, 16 `pre_fichamento`, 0 `revisado`); fichamento-06: +81 ([relatório](pesquisa/fichamento-06.md)); fichamento-07: +16, voduns × orixás do Tambor de Mina em Prandi 2005 ([relatório](pesquisa/fichamento-07.md)) | `python3 scripts/validar_fichamento.py` |
| Atributos com versões divergentes | 41 | `python3 scripts/divergencias.py` |
| Fichas geradas (`data/orixas/`) | 5 fichas, 284 versões (2 registros retidos: tabus/alimentos) | `python3 scripts/validar_fichas.py` |
| Grafo (`data/conexoes.json`) | 54 nós, 61 arestas (23 sincretismo, 24 equivalência, 10 parentesco, 3 companheiro de culto, 1 associação) | idem |
| Entidades equivalentes (`data/entidades_equivalentes.json`) | 24 (14 voduns: Legba, Gu, Badé, Sobo e, no fichamento-07, Abê, Naê, Vondereji, Averequete, Xadantã, Doçu, Bedigá, Doçupé, Agüê, Azacá; 3 inquices; 7 nomes fon/banto não classificados) | idem |
| Tradições (`data/tradicoes.json`) | 19: 16 `com_fonte`, 3 `rascunho_sem_fonte` (benim, arara, orisha_trinidad). Fichamento-07: `candomble_efon` ganhou descrição mínima (Castillo 2022) e as páginas de Halloy em tradições e glossário viraram página impressa (PDF − 1). Sessão trad02: palo_monte e xango_sergipe ganharam fonte; 7 reforçadas ([relatório](pesquisa/tradicoes-02.md)) | idem |
| Glossário (`data/glossario.json`) | 54 termos com fonte e página (+7 na trad02: Regla de Ocha, Palo Monte, nfumbi, mpungu, cabildo, Xambá, abatá); 6 pendentes em `_meta.pendentes` | idem |
| Anti-cópia | Sem referências: 0 erros. **Auditoria 01 com o texto integral de 29 obras** ([relatório](pesquisa/anticopia-01.md)): **10 erros** (8+ palavras) em 9 registros (7 de Prandi 2001, 1 de Seixas 2018, 1 de Queiroga & Nascimento 2019; 1 falso positivo) e 31 campos com redação próxima demais; 43 reescritas propostas, **não aplicadas**. Tradições e glossário: 0 erros. Oro 2008 não coberto | `ANTICOPIA_REFS=<pasta> python3 scripts/anticopia.py` |
| Site (`site/`) | 14 páginas: início com busca, catálogo, 5 fichas (com mini-grafo e termos do glossário ligados), grafo, tradições, glossário, fontes, metodologia, baixar dados, sobre (+ 12 arquivos em `/dados/`). Screenshots em `docs/screenshots/` | `cd site && npm ci && npm run build` |
| QA do site | 284/284 versões batem com `data/orixas`; 54/54 termos do glossário e 19/19 tradições conferidos contra os dados (fontes, ano e página); texto das 3 tradições sem fonte ausente do site; 0 vazamento de pré-fichamento/retidos; selo e `noindex` em tudo; ~1760 links e âncoras internos sem 404; axe-core sem violações (14 páginas × 2 larguras) | `python3 scripts/qa_site.py`; `node site/scripts/acessibilidade.cjs` |
| Revisão do conselho | 0 revisores em `data/revisores.json`, 0 revisões; 37 testes (`tests/test_revisao.py`) e teste ponta a ponta com dados sintéticos numa cópia temporária (`tests/e2e_revisao_site.py`) | `python3 -m unittest discover -s tests`; `python3 tests/e2e_revisao_site.py` |
| Idiomas no catálogo | pt 159 · en 94 · fr 36 · es 18 · de 6 · it 2 · yo 1 | — |

Registros por orixá: Exu 93 · Ogum 64 · Iemanjá 59 · Xangô 52 · Oxóssi 34.

**Fontes já lidas no original:** Prandi 2001; Bastide 1961 (pp. 26–32, 89–128, 165, 182–192); Chiousse 1995 (pp. 225–291); Silva 2012 (parcial); Blass 2007; Seixas 2018; Queiroga & Nascimento 2019; Souza 2020; resumos de Cardoso Filho 2015 e Teixeira 2021; Nogueira 2017 (pp. 9, 16–22, 195–197, 382–385); Pinheiro 2011 (pp. 28–41, 61–72, 83–84); Costa 2007 (integral); Oro 2008 (pp. 11–14); Botão 2007 (p. 15 e glossário); Tomba 2019 (pp. 25, 91–92); Prandi 2005, *Nas pegadas dos voduns* (integral, versão do autor, no fichamento-07); glossários de Bastide (pp. 353–358) e Chiousse (pp. 371–380); **trad02:** Halloy 2005 (pp. 24–31, 84–86, 96–98, 115–121, 163–170), Pitta 1985 (integral), M. Ferretti 2001 (pp. 75–84), S. Ferretti 2011 (integral), Oro 2012 (integral), Toutain 2019 (pp. 2, 6–11, 18–21, 107–112), Argyriadis 2005 (pp. 153–157, 175–176), Cerqueira 2015 (pp. 82–83, 88, 132, 155, 165); **fichamento-06:** Castillo 2022 (integral), Costa 1980 (integral), Nascimento et al. 2001 (integral), Vallier 2011 (pp. 811–831), Capo Chichi 2025 (integral); páginas da trad02 conferidas para os orixás (Halloy pp. 163–169, Pitta 263–267, Toutain 7–11, S. Ferretti 260–262, Cerqueira 82–88). Ver [`fichamento-04`](pesquisa/fichamento-04.md), [`fichamento-05`](pesquisa/fichamento-05.md), [`tradicoes-02`](pesquisa/tradicoes-02.md) [`fichamento-06`](pesquisa/fichamento-06.md) e [`fichamento-07`](pesquisa/fichamento-07.md).

## Próximas tarefas (em ordem)

0. **(P1) Aplicar as reescritas da auditoria anti-cópia** ([`anticopia-01`](pesquisa/anticopia-01.md) §3): 10 campos da classe A (erro) e 31 da classe B em `data/fichamento/` (exu, iemanja, ogum, oxossi, xango), 1 nota de `data/tradicoes.json` e 1 definição de `data/glossario.json`. Depois regenerar as fichas e rodar o anti-cópia com as referências (baixar de novo para `/tmp/refs`, com as URLs do §2 do relatório) até 0 erros. Na mesma sessão, ou em outra, ajustar `scripts/anticopia.py` como pede o §5.2 (hifenização, falso positivo de referência bibliográfica, aviso para 6–7 palavras iguais à fonte citada).
1. **Saudações, itãs e origem africana** dos 5 orixás. Depende de Verger, Prandi (*Mitologia*), Cacciatore e Beniste, que precisam de exemplar → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §2.
2. **Equivalências com inquices e voduns.** Depende de Castro 2001, Parés 2006 e Lopes 1988 (exemplar). *(Tambor de Mina: feito no fichamento-07 com Prandi 2005, em duas casas, a Casa das Minas (via S. Ferretti, a conferir no original) e a Casa das Minas de Tóia Jarina (SP). Falta o Jeje da Bahia (Parés) e os inquices.)*
3. **Resolver os 16 `pre_fichamento`.** As fontes são pagas, impressas ou estão fora do ar: Tishken 2009 (3), Brown 1989 (2), Silva & Silva Neto 2025 (2), Verger 1954 (2), Pérez 2013 (2), Ribas 2010 (1, oasisbr fora do ar), Beier 1970, Barnes 1989, Verger 1981 e Carneiro 1948 (1 cada).
4. **Fontes P1 bloqueadas do fichamento-06** (Iemanjá teve registros novos só do Recife, de Cuba e do Maranhão): Prandi 1995, Giumbelli & Lima 2024 e Noleto & Negrão 2025 (SciELO com desafio anti-robô) e Ferreira 2017 (UnB 403). O autor baixa e anexa, ou libera o acesso → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §1. Ribas 2010 (ogum-005) tem PDF no repositório da PUC-SP, também atrás de desafio anti-robô. *(Busca de texto aberto para os 16 `pre_fichamento`: feita em 2026-11-01, nenhum acessível; ver [`fichamento-06`](pesquisa/fichamento-06.md).)*
5. **Fase 2 (restante):** as 3 tradições sem fonte (Arará, Orisha de Trinidad e o rótulo `benim`) e o reforço de Efon (Lima 2014) e os termos pendentes do glossário. Dependem de Barnet 1995, Cabrera 1954 e de uma obra sobre o Orisha de Trinidad. Dantas 1988 ampliaria o Xangô de Sergipe, que hoje só tem descrição mínima; Mones 2024 e Arango 2018 estão bloqueados neste ambiente → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md). *(Tradições com fonte (13) e glossário (47 termos): feitos em 2026-10-31, ver [`fichamento-05`](pesquisa/fichamento-05.md). Sessão trad02 (2026-11-01): 15 tradições com fonte e 54 termos, ver [`tradicoes-02`](pesquisa/tradicoes-02.md).)*
6. **Fase 3:** redigir os resumos de itãs e a tabela de equivalências por orixá, conforme o fichamento avançar (tarefas 1 e 2).
7. **Site (Fase 5, restante):** versões es/en (Fase 7). *(Mini-grafo, Baixar dados, QA, e — na sessão site2 — páginas Glossário, Tradições e Sobre/Créditos com termos ligados nas fichas: feitos em 2026-10-31.)* Deploy, domínio, licenças e texto final dos créditos dependem do autor → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §3b.
8. **Conselho consultivo:** o autor contata os candidatos ([`conselho/candidatos.md`](conselho/candidatos.md): 29 pesquisadores e caminhos institucionais para praticantes) com os modelos de [`conselho/kit-revisao.md`](conselho/kit-revisao.md). A primeira revisão segue [`conselho/como-registrar-revisao.md`](conselho/como-registrar-revisao.md). Falta decidir o critério do selo e `comunicacao_pessoal`; a página Créditos fica para quando houver o primeiro revisor → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §3c. *(Preparação: feita em 2026-10-31. Passos 1–3 da proposta — campo `revisoes`, `data/revisores.json`, regras no validador, gerador e site prontos para exibir revisões, QA e testes: feitos em 2026-11-01, sessão revisao.)*

**Sugestões da sessão trad02:**
- ~~**(P1)** Encaminhar ao fichamento as afirmações do §4 de [`tradicoes-02`](pesquisa/tradicoes-02.md)~~: feito no fichamento-06 (39 registros; Oro 2012 e o mito do balé ficaram de fora, ver adendo do [relatório](pesquisa/fichamento-06.md)). Em Halloy, página impressa = PDF − 1, e não = PDF.
- ~~A sessão do catálogo deve anotar as correções do §5~~: feito nos fichamentos 06 e 07.
- Baixar manualmente Santana 2023, Mendes 2014, Niell 2023, S. Ferretti 1996 e Corrêa 1996, bloqueados no ambiente.
- ~~QA do site falhando após o rebase sobre a fich06 (ids `pre_fichamento` em notas)~~: corrigido no commit final do fichamento-06 (notas de ogum-048 e xango-038 reescritas); `qa_site.py` sem erros.

**Sugestões da varredura 3:** P1 fichadas em 2026-11-01, menos as 4 bloqueadas (tarefa 4). As afirmações da trad02 sobre os 5 orixás já foram fichadas. Próximas candidatas abertas: Argyriadis 2005 e M. Ferretti 2001 (lidos pela trad02 só para as tradições), e o restante da tese de Halloy. ~~**Sugestão do fichamento-06:** Castillo 2022 como pista para `candomble_efon`~~ (feito no fichamento-07). **Sugestões do fichamento-07:** (a) conferir em S. Ferretti, *Querebentã*, o panteão da Casa das Minas lido via Prandi; (b) ler o resto de M. Ferretti 2001 (pp. 84–94) para voduns e orixás na Casa de Nagô; (c) fichar a "fiesta de Elegguá" do central Méjico (Toutain, p. 57: 22–24 de outubro). Repetir a coleta para BDTD e OpenAlex quando estiverem acessíveis (`scripts/coleta/coletar.py --bases bdtd,openalex`).

**Sugestões da sessão do glossário:** (a) ~~ler Prandi 2005 inteiro~~ (feito no fichamento-07); (b) ~~repetir o anti-cópia com referências para as obras das rodadas 1–4~~ (feito na sessão anticopia: 10 erros, ver tarefa 0); (c) ~~glossário no site com links a partir das fichas~~ (feito na sessão site2).

## Decisões já tomadas

- Commit e push **direto na `main`**, sem branch nem PR (pedido do autor).
- Só fontes A/B sustentam ficha. Blogs e sites de divulgação (nível D) servem apenas como pista.
- Registro `fichado` exige página e fonte lida pelo menos `conferido_web`. Afirmação de 2ª mão leva `via_source_id`.
- Divergências ficam lado a lado, com casa, região e fonte, sem eleger versão correta (gerado por `scripts/divergencias.py`).
- **Tabus e alimentos rituais:** não detalhar. Decidir com o conselho o que é público.
- Todo bloqueio (domínio, paywall, livro impresso, conferência humana) vai para [`pesquisa/PENDENCIAS.md`](pesquisa/PENDENCIAS.md).
- **Fichas são geradas, não editadas:** `scripts/gerar_fichas.py` monta `data/orixas/*.json` e `data/conexoes.json` a partir do fichamento (só `fichado`/`revisado`). Corrigir sempre no fichamento e regenerar; `validar_fichas.py` acusa ficha desatualizada.
- **Versão = um registro:** cada versão carrega `source_id`, `via_source_id`, `localizacao` e `sources: [{id, loc, via}]`; esquema comum em `schemas/_versao.schema.json`.
- **Arestas do grafo** vêm de `data/conexoes_alvos.json`, mapa manual registro → alvos, que só estrutura o que o `valor` diz (ex.: "mãe de vários orixás" fica sem aresta). Registro novo de parentesco/equivalência/sincretismo sem entrada no mapa gera aviso `sem_mapa`. "Nossa Senhora" e "Virgem Maria" ficam como nós separados, como escrito nas fontes.
- **Tabus e alimentos** fichados ficam fora da ficha pública (`pendencias.retidos_ate_conselho`) até decisão do conselho.
- **Entidades equivalentes** são geradas das arestas de equivalência; nomes que a fonte não atribui a fon ou banto ficam como `nome_fon_ou_banto`.
- **Anti-cópia:** citação entre aspas com 15+ palavras é erro. Para comparar com o texto das obras, aponte `ANTICOPIA_REFS` para uma pasta de `.txt` **fora do repo**; qualquer sequência idêntica de 8 palavras é erro.
- **CI** (`.github/workflows/validar.yml`) roda todos os validadores e o build do site a cada push e PR.
- **Site só exibe dados:** `site/` lê `data/` em tempo de build; nenhum texto sobre orixás é escrito no código. Afirmações da página de Metodologia citam registros pelo componente `Ref.astro`, e o build falha se o registro não existir ou não estiver `fichado`. Tradições `com_fonte` aparecem com descrição e fontes na página Tradições; `rascunho_sem_fonte` aparecem só pelo nome com o aviso "Descrição pendente de fonte" (nem o texto do rascunho nem região/matriz são exibidos).
- **QA do site:** `scripts/qa_site.py` roda após o build (também no CI) e confere todas as versões exibidas contra `data/orixas`, ausência de pré-fichamento e retidos em qualquer arquivo publicado, selo, `noindex`, links/âncoras e cópias de `/dados/`. Acessibilidade: `site/scripts/acessibilidade.cjs` (axe-core; falha em violação `serious`/`critical`), local, fora do CI. Rodar os dois no fechamento de sessões que mexem no site.
- **Glossário e tradições no site (sessão site2):** página Glossário (A–Z, por categoria, divergências lado a lado, pendentes sem definição) e página Tradições (grupos na ordem Candomblé, afro-brasileiras regionais, Umbanda, culto na África, diáspora caribenha; o site mostra só descrição, fontes e nota, não região/matriz). Nas fichas, a 1ª ocorrência de cada termo vira link com `aria-describedby` para a seção "Termos do glossário nesta página" (`marcarGlossario` em `site/src/lib/dados.js`). Etiquetas de tradição só viram link nos resumos (cabeçalho da ficha e cartões do catálogo), para não multiplicar paradas de Tab. `qa_site.py` confere glossário, tradições e Sobre (issues como canal, nenhum e-mail no site).
- **Baixar dados:** `/dados/` publica só dados públicos gerados (fichas, grafo, entidades, divergências, catálogo) `glossario.json` e `tradicoes.json` (sem as descrições ainda `rascunho_sem_fonte`); **nunca** o fichamento bruto. Licença "a definir pelo autor".
- **Site:** Astro 7 (Node ≥ 22.23), saída estática, `SITE_BASE` para subcaminho. Selo "Rascunho — aguardando revisão de praticantes e pesquisadores" em todas as fichas e `noindex` em todas as páginas até a revisão. Etiquetas de Umbanda com borda tracejada, para distinguir de Candomblé sem depender de cor. Filtros e grafo são aprimoramento progressivo: sem JS, aparecem tabelas e listas completas.
- **Conferência de metadados:** Open Library, Internet Archive, Crossref e repositórios institucionais valem como evidência para `conferido_web`; a URL vai em `evidencias`. Divergência de edição ou ano é anotada em `observacoes`, sem trocar o ano citado. WorldCat (429), Gallica (403) e Google Books (cota) não respondem neste ambiente.
- **Coleta por API (varredura 3):** `scripts/coleta/` é o caminho padrão para novas varreduras. A saída bruta vai para `data/fontes/coleta/<data>/`, sem resumos (texto de terceiros). As decisões de triagem ficam num script legível (`triagem_<data>.py`) e só entram no catálogo itens sobre orixás ou religiões afro-diaspóricas, com metadado de API. Autopublicação e editoras esotéricas ficam de fora. Candidatos pertinentes mas periféricos continuam em `candidatos.json`, sem entrar no catálogo.
- PDFs baixados ficam fora do repositório. No repo entram só metadados e paráfrase.
- **Página nos registros é a página impressa**, não a do PDF. Quando as duas diferem, a relação é anotada no relatório da rodada.
- **Página sem número impresso** (ex.: PDF da *Afro-Ásia* antiga): citar "PDF p. N" e registrar em PENDENCIAS para conversão. **Desafio anti-robô** (SciELO, CORE, PUC-SP, arquivo): não contornar; registrar e pedir o arquivo ao autor. Espelhos legítimos (repositório institucional dos autores, HAL) valem.
- **Tradição só entra se a fonte disser.** Exemplo: ogum-006 perdeu `candomble_ketu` porque Pinheiro documenta o sincretismo em casas de Umbanda e a casa de Candomblé estudada é Jeje. Se a fonte diz "candomblé" sem nação, o registro anota a aproximação em `nota`.
- Fonte primária de registro de 2ª mão (`source_id` com `via_source_id`) também é conferida em catálogo (Open Library etc.) antes de entrar como `fichado`.
- **Glossário** (`data/glossario.json`, esquema `schemas/glossario.schema.json`): só entra termo com fonte lida (`conferido_web` ou acima) e página; sentidos diferentes vão em `divergencias`, lado a lado. Definição em nível público, sem fundamento iniciático; termos ligados a tabu ou iniciação (quizila, bori, kelê) esperam o conselho. `validar_fichas.py` valida glossário e tradições; `anticopia.py` confere definições e notas.
- **Tradições `com_fonte`** exigem fontes `conferido_web` ou acima (checado por `validar_fichas.py`). O que a fonte não sustenta sai da descrição e vai para `nota` ou PENDENCIAS.
- **Afirmações sobre os 5 orixás achadas em leituras de outra tarefa** (tradições, glossário) não entram direto no fichamento: vão para o relatório da sessão, com fonte, página e paráfrase, e a orquestradora as encaminha.
- **Equivalência vodum × orixá (fichamento-07):** vale para a casa que a fonte descreve (`casa_ou_regiao`), nunca como identidade. No grafo, só o santo do próprio orixá vira aresta de sincretismo; os santos dos voduns correspondentes ficam no `valor`. Panteão que a fonte lida resume de outro autor (Prandi resumindo S. Ferretti) leva `source_id` do autor resumido e `via_source_id` da fonte lida.
- **Anti-cópia com referências:** ao ler uma obra, salvar o `.txt` fora do repo e rodar `ANTICOPIA_REFS=<pasta> python3 scripts/anticopia.py`. A checagem sem referências não pega cópia de obra.

- **Conselho (implementado, sessão revisao):** a aprovação fica no **registro de fichamento** (`revisoes`: revisor, data, tradição, parecer, aspectos, hash do registro), não na ficha gerada; aprovação vale só para a tradição que esteja no registro **e** no cadastro do revisor; `revisado` exige aprovação vigente (hash atual), e revisão desatualizada volta a `fichado` na geração; `contestado` não apaga versão; `nao_publicar` retira da ficha pública (vai para `retidos_ate_conselho`, também fora do grafo e das divergências), mesmo com hash antigo; revisões só se acrescentam (checado contra `--base`, no CI o commit anterior). Cadastro em `data/revisores.json`, não em `data/conselho/`, só com o crédito autorizado; contatos e termos assinados ficam fora do repositório. A versão gerada só ganha `revisoes` quando há revisão, então os dados sem revisão não mudaram. Selo "Rascunho" sai só quando **todas** as versões da ficha estão revisadas (a confirmar com o autor). Regras em `scripts/revisao.py`; o crédito exibido é calculado igual em `site/src/lib/dados.js`. Praticantes são procurados **por instituição** (terreiro tombado, federação, núcleo universitário), nunca listados por nome.

## Sessões em paralelo

- **Podem rodar juntas:** sessões que editam arquivos diferentes, por exemplo um orixá cada (`data/fichamento/<orixa>.json`).
- **`data/fontes/catalogo.json` é compartilhado:** só uma sessão por vez deve adicionar ou editar fontes.
- Sempre começar com `git pull origin main` e terminar com `git pull --rebase` antes do `push`.

## Mapa dos arquivos

| Caminho | Conteúdo |
|---|---|
| `CLAUDE.md` | contexto, regras de conteúdo, regras de trabalho |
| `docs/PLANO.md` | plano completo (fases 0–7) |
| `docs/ESTADO.md` | este arquivo |
| `docs/pesquisa/PENDENCIAS.md` | bloqueios a resolver pelo autor |
| `docs/pesquisa/relatorio-varredura-0*.md` | rodadas de busca de fontes (a nº 3 é automatizada) |
| `scripts/coleta/` | coleta por API, deduplicação, triagem e incorporação ao catálogo (ver `README.md`) |
| `data/fontes/coleta/<data>/` | saída bruta da coleta por base, `candidatos.json`, `triagem.json`, `triagem_resumo.json` |
| `docs/pesquisa/fichamento-0*.md` | rodadas de fichamento (fontes lidas, correções, divergências) |
| `docs/pesquisa/anticopia-01.md` | auditoria anti-cópia com o texto integral de 29 obras: trechos suspeitos e reescritas propostas |
| `docs/pesquisa/tradicoes-02.md` | 2ª rodada de tradições e glossário; afirmações sobre os 5 orixás a encaminhar |
| `data/fontes/catalogo.json` | catálogo de fontes (esquema em `schemas/fonte.schema.json`) |
| `data/fichamento/<orixa>.json` | registros atômicos por orixá (esquema em `schemas/fichamento.schema.json`) |
| `data/fichamento/divergencias.json` | gerado, não editar à mão |
| `data/orixas/<orixa>.json` | fichas (gerado; esquema `schemas/orixa.schema.json`) |
| `data/conexoes.json` | grafo (gerado; esquema `schemas/conexao.schema.json`) |
| `data/conexoes_alvos.json` | mapa manual registro → arestas (editar aqui) |
| `data/entidades_equivalentes.json` | voduns, inquices etc. (gerado; esquema `schemas/entidade.schema.json`) |
| `data/tradicoes.json` | tradições (esquema `schemas/tradicao.schema.json`) |
| `data/glossario.json` | glossário (esquema `schemas/glossario.schema.json`) |
| `data/revisores.json` | cadastro público de revisores (vazio; esquema `schemas/revisor.schema.json`) |
| `tests/` | testes da revisão com fixtures sintéticas (`python3 -m unittest discover -s tests`) e ponta a ponta (`e2e_revisao_site.py`) |
| `scripts/` | validação e geração; `qa_site.py` confere o site gerado |
| `site/` | protótipo do site (Astro); ver `site/README.md` |
| `docs/conselho/` | Fase 4: candidatos a revisor, kit do revisor (guia, sigilo, termo, convites pt/es), proposta de registro da revisão e passo a passo para registrar uma revisão |
| `docs/screenshots/` | capturas das páginas principais (`site/scripts/screenshots.cjs`) |

## Pedido de abertura sugerido

> Leia `CLAUDE.md` e `docs/ESTADO.md`. Tarefa desta sessão: **[tarefa]**. Ao terminar: rode os validadores, atualize `docs/ESTADO.md` e `docs/pesquisa/PENDENCIAS.md`, faça o commit e o push na `main`.
