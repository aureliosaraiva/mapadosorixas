# Estado do projeto

> Arquivo de passagem entre sessões. **Toda sessão começa lendo este arquivo e termina atualizando-o.** Mantenha-o curto, com no máximo uma página: o detalhe fica nos relatórios linkados.

**Última atualização:** 2026-10-31

## Onde estamos

**Fase 1 — Levantamento e fichamento** (em andamento) e **Fase 2 — Modelo de dados** (iniciada: esquemas, fichas geradas e grafo). Ver [`PLANO.md`](PLANO.md). As fases 3 a 7 ainda não começaram.

| Indicador | Valor | Como conferir |
|---|---:|---|
| Fontes no catálogo | 168 (79 `conferido_web`, 79 `a_verificar`, 10 `pista`); **todas as fontes usadas no fichamento estão `conferido_web` ou acima** | `python3 scripts/validar_fontes.py` |
| Registros de fichamento | 205 (189 `fichado`, 16 `pre_fichamento`, 0 `revisado`) | `python3 scripts/validar_fichamento.py` |
| Atributos com versões divergentes | 32 | `python3 scripts/divergencias.py` |
| Fichas geradas (`data/orixas/`) | 5 fichas, 187 versões (2 registros retidos: tabus/alimentos) | `python3 scripts/validar_fichas.py` |
| Grafo (`data/conexoes.json`) | 40 nós, 43 arestas (20 sincretismo, 11 equivalência, 8 parentesco, 3 companheiro de culto, 1 associação) | idem |
| Entidades equivalentes (`data/entidades_equivalentes.json`) | 11 (1 vodum, 3 inquices, 7 nomes fon/banto não classificados) | idem |
| Tradições (`data/tradicoes.json`) | 19, todas `rascunho_sem_fonte` | idem |
| Anti-cópia | 0 erros (também contra o texto das 3 fontes desta rodada); 3 citações curtas (≤7 palavras) e 1 repetição interna como aviso | `python3 scripts/anticopia.py` |
| Idiomas no catálogo | pt, en, es, fr, de, it, yo | — |

Registros por orixá: Exu 64 · Iemanjá 47 · Xangô 34 · Ogum 33 · Oxóssi 27.

**Fontes já lidas no original:** Prandi 2001; Bastide 1961 (pp. 26–32, 89–128, 165, 182–192); Chiousse 1995 (pp. 225–291); Silva 2012 (parcial); Blass 2007; Seixas 2018; Queiroga & Nascimento 2019; Souza 2020; resumos de Cardoso Filho 2015 e Teixeira 2021; Nogueira 2017 (pp. 9, 16–22, 195–197, 382–385); Pinheiro 2011 (pp. 28–41, 61–72, 83–84); Costa 2007 (integral). Ver [`fichamento-04`](pesquisa/fichamento-04.md).

## Próximas tarefas (em ordem)

1. **Saudações, itãs e origem africana** dos 5 orixás. Depende de Verger, Prandi (*Mitologia*), Cacciatore e Beniste, que precisam de exemplar → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §2.
2. **Equivalências com inquices e voduns.** Depende de Castro 2001, Parés 2006 e Lopes 1988 (exemplar).
3. **Resolver os 16 `pre_fichamento`.** As fontes são pagas, impressas ou estão fora do ar: Tishken 2009 (3), Brown 1989 (2), Silva & Silva Neto 2025 (2), Verger 1954 (2), Pérez 2013 (2), Ribas 2010 (1, oasisbr fora do ar), Beier 1970, Barnes 1989, Verger 1981 e Carneiro 1948 (1 cada).
4. **Procurar texto aberto para os `pre_fichamento` restantes**, por exemplo a dissertação de Ribas 2010 em outro espelho e capítulos de Tishken 2009 e Barnes 1989 em repositórios de autores. *(Leitura de Nogueira 2017, Pinheiro 2011 e Costa 2007: feita em 2026-10-31; exu-034 e xango-005 confirmados, ogum-006 corrigido, 7 registros novos.)*
5. **Fase 2 (restante):** dar fonte às descrições de `data/tradicoes.json` e criar `glossario.json`. Ambos dependem de fichar definições em obra de referência; não redigir sem fonte. *(Esquemas, fichas, grafo, entidades equivalentes, validador, anti-cópia e CI: feitos em 2026-10-31.)*
6. **Fase 3:** redigir os resumos de itãs e a tabela de equivalências por orixá, conforme o fichamento avançar (tarefas 1 e 2).
7. **Conselho consultivo:** levantar possíveis revisores (praticantes e pesquisadores) e começar a revisão das fichas → status `revisado`.

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
- **CI** (`.github/workflows/validar.yml`) roda todos os validadores a cada push e PR.
- **Conferência de metadados:** Open Library, Internet Archive, Crossref e repositórios institucionais valem como evidência para `conferido_web`; a URL vai em `evidencias`. Divergência de edição ou ano é anotada em `observacoes`, sem trocar o ano citado. WorldCat (429), Gallica (403) e Google Books (cota) não respondem neste ambiente.
- PDFs baixados ficam fora do repositório. No repo entram só metadados e paráfrase.
- **Página nos registros é a página impressa**, não a do PDF. Quando as duas diferem, a relação é anotada no relatório da rodada.
- **Tradição só entra se a fonte disser.** Exemplo: ogum-006 perdeu `candomble_ketu` porque Pinheiro documenta o sincretismo em casas de Umbanda e a casa de Candomblé estudada é Jeje. Se a fonte diz "candomblé" sem nação, o registro anota a aproximação em `nota`.
- Fonte primária de registro de 2ª mão (`source_id` com `via_source_id`) também é conferida em catálogo (Open Library etc.) antes de entrar como `fichado`.

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
| `scripts/` | validação e geração |

## Pedido de abertura sugerido

> Leia `CLAUDE.md` e `docs/ESTADO.md`. Tarefa desta sessão: **[tarefa]**. Ao terminar: rode os validadores, atualize `docs/ESTADO.md` e `docs/pesquisa/PENDENCIAS.md`, faça o commit e o push na `main`.
