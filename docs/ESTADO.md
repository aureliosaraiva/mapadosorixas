# Estado do projeto

> Arquivo de passagem entre sessões. **Toda sessão começa lendo este arquivo e termina atualizando-o.** Mantenha-o curto, com no máximo uma página: o detalhe fica nos relatórios linkados.

**Última atualização:** 2026-10-31

## Onde estamos

**Fase 1 — Levantamento e fichamento** (em andamento), **Fase 2 — Modelo de dados** (iniciada: esquemas, fichas geradas e grafo) e **Fase 5 — Site estático: protótipo feito** (`site/`, Astro + Cytoscape.js + Pagefind; compila no CI, sem deploy). Ver [`PLANO.md`](PLANO.md). **Fase 4 — Conselho: preparação feita** ([`conselho/`](conselho/): candidatos, kit do revisor, proposta do campo `revisao`); contato e convites dependem do autor. Fases 3, 6 e 7 ainda não começaram.

| Indicador | Valor | Como conferir |
|---|---:|---|
| Fontes no catálogo | 169 (80 `conferido_web`, 79 `a_verificar`, 10 `pista`); **todas as fontes usadas no fichamento estão `conferido_web` ou acima** | `python3 scripts/validar_fontes.py` |
| Registros de fichamento | 205 (189 `fichado`, 16 `pre_fichamento`, 0 `revisado`) | `python3 scripts/validar_fichamento.py` |
| Atributos com versões divergentes | 32 | `python3 scripts/divergencias.py` |
| Fichas geradas (`data/orixas/`) | 5 fichas, 187 versões (2 registros retidos: tabus/alimentos) | `python3 scripts/validar_fichas.py` |
| Grafo (`data/conexoes.json`) | 40 nós, 43 arestas (20 sincretismo, 11 equivalência, 8 parentesco, 3 companheiro de culto, 1 associação) | idem |
| Entidades equivalentes (`data/entidades_equivalentes.json`) | 11 (1 vodum, 3 inquices, 7 nomes fon/banto não classificados) | idem |
| Tradições (`data/tradicoes.json`) | 19: 13 `com_fonte`, 6 `rascunho_sem_fonte` (benim, efon, xango_sergipe, palo_monte, arara, orisha_trinidad) | idem |
| Glossário (`data/glossario.json`) | 47 termos com fonte e página; 6 pendentes em `_meta.pendentes` | idem |
| Anti-cópia | 0 erros, também contra o texto das 8 obras lidas na rodada do glossário (4 paráfrases antigas reescritas); 3 citações curtas (≤7 palavras) e 1 repetição interna como aviso | `python3 scripts/anticopia.py` |
| Site (`site/`) | 11 páginas: início com busca, catálogo, 5 fichas (com mini-grafo), grafo, fontes, metodologia, baixar dados (+ 11 arquivos em `/dados/`). Screenshots em `docs/screenshots/` | `cd site && npm ci && npm run build` |
| QA do site | 187/187 versões batem com `data/orixas`; 0 vazamento de pré-fichamento/retidos; selo e `noindex` em tudo; ~1200 links e âncoras internos sem 404; axe-core sem violações (11 páginas × 2 larguras) | `python3 scripts/qa_site.py`; `node site/scripts/acessibilidade.cjs` |
| Idiomas no catálogo | pt, en, es, fr, de, it, yo | — |

Registros por orixá: Exu 64 · Iemanjá 47 · Xangô 34 · Ogum 33 · Oxóssi 27.

**Fontes já lidas no original:** Prandi 2001; Bastide 1961 (pp. 26–32, 89–128, 165, 182–192); Chiousse 1995 (pp. 225–291); Silva 2012 (parcial); Blass 2007; Seixas 2018; Queiroga & Nascimento 2019; Souza 2020; resumos de Cardoso Filho 2015 e Teixeira 2021; Nogueira 2017 (pp. 9, 16–22, 195–197, 382–385); Pinheiro 2011 (pp. 28–41, 61–72, 83–84); Costa 2007 (integral); Oro 2008 (pp. 11–14); Botão 2007 (p. 15 e glossário); Tomba 2019 (pp. 25, 91–92); Prandi 2005, *Nas pegadas dos voduns* (pp. 1–2 da versão do autor); glossários de Bastide (pp. 353–358) e Chiousse (pp. 371–380). Ver [`fichamento-04`](pesquisa/fichamento-04.md) e [`fichamento-05`](pesquisa/fichamento-05.md).

## Próximas tarefas (em ordem)

1. **Saudações, itãs e origem africana** dos 5 orixás. Depende de Verger, Prandi (*Mitologia*), Cacciatore e Beniste, que precisam de exemplar → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §2.
2. **Equivalências com inquices e voduns.** Depende de Castro 2001, Parés 2006 e Lopes 1988 (exemplar).
3. **Resolver os 16 `pre_fichamento`.** As fontes são pagas, impressas ou estão fora do ar: Tishken 2009 (3), Brown 1989 (2), Silva & Silva Neto 2025 (2), Verger 1954 (2), Pérez 2013 (2), Ribas 2010 (1, oasisbr fora do ar), Beier 1970, Barnes 1989, Verger 1981 e Carneiro 1948 (1 cada).
4. **Procurar texto aberto para os `pre_fichamento` restantes**, por exemplo a dissertação de Ribas 2010 em outro espelho e capítulos de Tishken 2009 e Barnes 1989 em repositórios de autores. *(Leitura de Nogueira 2017, Pinheiro 2011 e Costa 2007: feita em 2026-10-31; exu-034 e xango-005 confirmados, ogum-006 corrigido, 7 registros novos.)*
5. **Fase 2 (restante):** as 6 tradições sem fonte (Efon, Xangô de Sergipe, Palo Monte, Arará, Orisha de Trinidad e o rótulo `benim`) e os termos pendentes do glossário. Dependem de Dantas 1988, Barnet 1995, Cabrera 1954 e de uma obra sobre o Orisha de Trinidad; Mones 2024 e Arango 2018 estão bloqueados neste ambiente → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md). *(Tradições com fonte (13) e glossário (47 termos): feitos em 2026-10-31, ver [`fichamento-05`](pesquisa/fichamento-05.md).)*
6. **Fase 3:** redigir os resumos de itãs e a tabela de equivalências por orixá, conforme o fichamento avançar (tarefas 1 e 2).
7. **Site (Fase 5, restante):** glossário e página Sobre/Créditos (dependem de `glossario.json` com fonte); versões es/en (Fase 7). *(Mini-grafo na ficha, Baixar dados e QA de conteúdo/links/acessibilidade: feitos em 2026-10-31.)* Deploy, domínio e licenças dependem do autor → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §3b.
8. **Conselho consultivo:** o autor contata os candidatos ([`conselho/candidatos.md`](conselho/candidatos.md): 29 pesquisadores e caminhos institucionais para praticantes) com os modelos de [`conselho/kit-revisao.md`](conselho/kit-revisao.md). Antes da primeira revisão, implementar os passos 1–3 de [`conselho/proposta-registro-revisao.md`](conselho/proposta-registro-revisao.md) (campo `revisoes` por registro, `revisores.json`, regras no validador) → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §3c. *(Preparação: feita em 2026-10-31.)*

**Sugestões da sessão do glossário:** (a) ler Prandi 2005, *Nas pegadas dos voduns*, inteiro (36 p., aberto): pode adiantar a tarefa 2 (voduns equivalentes no Tambor de Mina); (b) repetir o anti-cópia com referências para as obras das rodadas 1–4 que ainda não passaram por ele (Nogueira 2017, Pinheiro 2011, Costa 2007, Blass 2007 etc.); (c) o site pode mostrar o glossário com links a partir das fichas (campo `ver_tambem`).

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
- **Site só exibe dados:** `site/` lê `data/` em tempo de build; nenhum texto sobre orixás é escrito no código. Afirmações da página de Metodologia citam registros pelo componente `Ref.astro`, e o build falha se o registro não existir ou não estiver `fichado`. Tradições aparecem só pelo nome, porque as descrições ainda estavam sem fonte (desde a sessão do glossário, 13 das 19 têm `status: com_fonte`; o site pode passar a exibi-las).
- **QA do site:** `scripts/qa_site.py` roda após o build (também no CI) e confere todas as versões exibidas contra `data/orixas`, ausência de pré-fichamento e retidos em qualquer arquivo publicado, selo, `noindex`, links/âncoras e cópias de `/dados/`. Acessibilidade: `site/scripts/acessibilidade.cjs` (axe-core; falha em violação `serious`/`critical`), local, fora do CI. Rodar os dois no fechamento de sessões que mexem no site.
- **Baixar dados:** `/dados/` publica só dados públicos gerados (fichas, grafo, entidades, divergências, catálogo) `glossario.json` e `tradicoes.json` (sem as descrições ainda `rascunho_sem_fonte`); **nunca** o fichamento bruto. Licença "a definir pelo autor".
- **Site:** Astro 7 (Node ≥ 22.23), saída estática, `SITE_BASE` para subcaminho. Selo "Rascunho — aguardando revisão de praticantes e pesquisadores" em todas as fichas e `noindex` em todas as páginas até a revisão. Etiquetas de Umbanda com borda tracejada, para distinguir de Candomblé sem depender de cor. Filtros e grafo são aprimoramento progressivo: sem JS, aparecem tabelas e listas completas.
- **Conferência de metadados:** Open Library, Internet Archive, Crossref e repositórios institucionais valem como evidência para `conferido_web`; a URL vai em `evidencias`. Divergência de edição ou ano é anotada em `observacoes`, sem trocar o ano citado. WorldCat (429), Gallica (403) e Google Books (cota) não respondem neste ambiente.
- PDFs baixados ficam fora do repositório. No repo entram só metadados e paráfrase.
- **Página nos registros é a página impressa**, não a do PDF. Quando as duas diferem, a relação é anotada no relatório da rodada.
- **Tradição só entra se a fonte disser.** Exemplo: ogum-006 perdeu `candomble_ketu` porque Pinheiro documenta o sincretismo em casas de Umbanda e a casa de Candomblé estudada é Jeje. Se a fonte diz "candomblé" sem nação, o registro anota a aproximação em `nota`.
- Fonte primária de registro de 2ª mão (`source_id` com `via_source_id`) também é conferida em catálogo (Open Library etc.) antes de entrar como `fichado`.
- **Glossário** (`data/glossario.json`, esquema `schemas/glossario.schema.json`): só entra termo com fonte lida (`conferido_web` ou acima) e página; sentidos diferentes vão em `divergencias`, lado a lado. Definição em nível público, sem fundamento iniciático; termos ligados a tabu ou iniciação (quizila, bori, kelê) esperam o conselho. `validar_fichas.py` valida glossário e tradições; `anticopia.py` confere definições e notas.
- **Tradições `com_fonte`** exigem fontes `conferido_web` ou acima (checado por `validar_fichas.py`). O que a fonte não sustenta sai da descrição e vai para `nota` ou PENDENCIAS.
- **Anti-cópia com referências:** ao ler uma obra, salvar o `.txt` fora do repo e rodar `ANTICOPIA_REFS=<pasta> python3 scripts/anticopia.py`. A checagem sem referências não pega cópia de obra.

- **Conselho (proposta, não implementada):** a aprovação fica no **registro de fichamento** (`revisoes`: revisor, data, tradição, parecer, hash do registro), não na ficha gerada; aprovação vale só para a tradição de quem revisou; `contestado` não apaga versão; `nao_publicar` retira da ficha pública. Nome de revisor só com termo de consentimento; contatos e termos assinados ficam fora do repositório. Praticantes são procurados **por instituição** (terreiro tombado, federação, núcleo universitário), nunca listados por nome.

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
| `docs/pesquisa/relatorio-varredura-0*.md` | rodadas de busca de fontes |
| `docs/pesquisa/fichamento-0*.md` | rodadas de fichamento (fontes lidas, correções, divergências) |
| `data/fontes/catalogo.json` | catálogo de fontes (esquema em `schemas/fonte.schema.json`) |
| `data/fichamento/<orixa>.json` | registros atômicos por orixá (esquema em `schemas/fichamento.schema.json`) |
| `data/fichamento/divergencias.json` | gerado, não editar à mão |
| `data/orixas/<orixa>.json` | fichas (gerado; esquema `schemas/orixa.schema.json`) |
| `data/conexoes.json` | grafo (gerado; esquema `schemas/conexao.schema.json`) |
| `data/conexoes_alvos.json` | mapa manual registro → arestas (editar aqui) |
| `data/entidades_equivalentes.json` | voduns, inquices etc. (gerado; esquema `schemas/entidade.schema.json`) |
| `data/tradicoes.json` | tradições (esquema `schemas/tradicao.schema.json`) |
| `data/glossario.json` | glossário (esquema `schemas/glossario.schema.json`) |
| `scripts/` | validação e geração; `qa_site.py` confere o site gerado |
| `site/` | protótipo do site (Astro); ver `site/README.md` |
| `docs/conselho/` | Fase 4: candidatos a revisor, kit do revisor (guia, sigilo, termo, convites pt/es), proposta de registro da revisão |
| `docs/screenshots/` | capturas das páginas principais (`site/scripts/screenshots.cjs`) |

## Pedido de abertura sugerido

> Leia `CLAUDE.md` e `docs/ESTADO.md`. Tarefa desta sessão: **[tarefa]**. Ao terminar: rode os validadores, atualize `docs/ESTADO.md` e `docs/pesquisa/PENDENCIAS.md`, faça o commit e o push na `main`.
