# Modelo de dados 2: panteão completo, hierarquia e itãs

Sessão **modelo2** (2026-11-01), primeira etapa da Fase 7 antecipada ([`PLANO.md`](PLANO.md)). O objetivo foi preparar dados, gerador, validadores e site para o panteão completo **sem inventar conteúdo**: nenhuma afirmação factual nova foi escrita. Os 5 orixás do MVP continuam com as mesmas 285 versões.

## 1. Lista-mestra: `data/entidades.json`

Esquema: `schemas/entidades.schema.json`. Não confundir com `entidade.schema.json`, que descreve as fichas leves geradas de voduns e inquices equivalentes.

| Campo | O que é | O que **não** é |
|---|---|---|
| `id` | identificador estável; nome do arquivo `data/fichamento/<id>.json` e prefixo dos registros (`<id>-NNN`) | — |
| `rotulo` | rótulo de exibição em pt-BR (os 5 do MVP mantêm o rótulo anterior) | nome "oficial" |
| `grafias` | formas de escrever o identificador, para busca | equivalência entre tradições. Nomes lucumís, fons ou bantos (Obatalá, Orula, Agayú…) ficaram de fora de propósito: vão para o atributo `nomes` do fichamento, com fonte |
| `tipo` | classificação de trabalho: `orixa`, `qualidade`, `divindade_suprema`, `conceito_cosmologico`, `ancestral` | posição cosmológica (essa vai no atributo `hierarquia`, com fonte) |
| `grupo` | `{rotulo: funfun/aboro/iaba, confirmado_por: [registros]}`, rótulo **a confirmar** | afirmação: o site e o download só mostram o grupo quando `confirmado_por` lista registros fichados. Hoje todos estão vazios |
| `qualidade_de` | só em `tipo: qualidade` (Oxalufã, Oxaguiã → Oxalá), vínculo de modelagem pedido no escopo | — |
| `prioridade_mvp2` | 1 = 5 do MVP + ~15 do PLANO; 2 = cosmologia, Orunmilá, Odudua; 3 = depois | — |
| `sensivel` | Iyami: só o que for público em fonte acadêmica, sem fundamento; aviso no site | — |
| `status_conteudo` | `sem_fichamento` / `pre` / `fichado`, **recalculado por `gerar_fichas.py`** | campo editável |
| `nota_modelagem` | por que dois nomes estão juntos (Omolu/Obaluaê, Iroko/Tempo, Olodumare/Olorum/Olofin) ou separados (Ewá e Iyewa) | afirmação sobre a tradição |

33 entidades: Exu, Ogum, Oxóssi, Xangô, Iemanjá, Oxum, Iansã, Omolu/Obaluaê, Nanã, Oxumarê, Ossaim, Logunedé, Obá, Ewá, Oxalá, Oxalufã, Oxaguiã, Ibeji, Iroko/Tempo, Orunmilá/Ifá, Odudua, Orixá Okô, Olokun, Aganju, Erinlé/Inlé, Ajê Xalugá, Iyewa, Olodumare/Olorum/Olofin, Orum, Aiê, orixás funfun, Egungun, Iyami.

Os ids reaproveitam os nós já existentes no grafo (`oxala`, `iansa`, `oba`, `oxum`); `validar_fichas.py` exige que todo nó de tipo `orixa` em `conexoes_alvos.json` esteja na lista-mestra.

## 2. Fichamento genérico

- `schemas/fichamento.schema.json`: `orixa` deixou de ser enum de 5 e passou a ser um id (`^[a-z][a-z_]*$`) validado contra a lista-mestra. O campo continua se chamando `orixa` para não mudar os 303 registros nem os hashes de revisão. Ids de registro: `^[a-z][a-z_]*-[0-9]{3}$`.
- Novo atributo **`hierarquia`**: posição ou relação cosmológica (com a divindade suprema, o Orum/Aiê, um grupo, os ancestrais), sempre como versão de uma fonte e tradição. Entra também na matriz de divergências.
- `validar_fichamento.py`: arquivo `data/fichamento/<id>.json` só para id da lista-mestra; registros com `orixa` = `<id>` e id `<id>-NNN`; validação da lista-mestra (esquema, `qualidade_de`, `grupo.confirmado_por`); histórico das revisões lido de todos os arquivos do fichamento no commit base (não mais de 5 nomes fixos).
- `scripts/entidades.py` concentra a leitura (lista-mestra, arquivos do fichamento, `status_conteudo`), usada por validadores, gerador, divergências, anti-cópia e testes.

**Única mudança nas 5 fichas:** `pendencias.sem_registro` ganhou `hierarquia` (é verdade: nenhum registro desse atributo ainda). Versões, grafo, entidades equivalentes e divergências ficaram byte a byte iguais.

## 3. Itãs: `data/itans.json`

Esquema: `schemas/ita.schema.json`. Um itã tem `titulo` (descritivo, do projeto), `entidades` (ids da lista-mestra ou nós do grafo **nomeados** na versão), `versoes` lado a lado, `arestas` (geradas) e `nota_curadoria` (por que as versões estão juntas).

Cada versão: `registro` (rastreabilidade), `valor`, `resumo` (parafraseado), `tradicoes`, `casa_ou_regiao`, `odu` (`{nome, loc}`, só se a fonte disser), `sources` com página, `nota`, `status`.

- **Versão espelhada** (`registro` preenchido): `gerar_fichas.py` copia do registro valor, resumo (= paráfrase), tradições, casa, fontes, nota e status; `validar_fichas.py` acusa divergência. Título, entidades, odu e nota de curadoria são editados à mão.
- **Versão própria** (`registro: null`): para itãs fichados direto aqui; se `fichado`, exige fonte lida e página; `anticopia.py` confere valor, resumo e nota (e o título e a nota de curadoria de todos os itãs).
- `arestas` = arestas de `data/conexoes.json` sustentadas por registros do itã. Hoje nenhuma: os 12 registros de itã não estão no mapa do grafo.
- Só versões `fichado`/`revisado` vão para o site e para `/dados/itans.json`.

Conteúdo inicial: os 12 registros `itans` já fichados, em 10 itãs. Agrupamentos (decisão editorial, registrada em `nota_curadoria`): exu-009 + exu-082 (o gorro de duas cores; exu-082 traz o odu Òdí Méjì, que está no `valor` do registro) e oxossi-023 + oxossi-026 (o caçador de uma flecha só). Em iemanja-052, Obatalá e Orungã são nomeados mas não viraram `entidades`: Obatalá não foi identificado com `oxala` sem fonte, e Orungã não está na lista-mestra.

## 4. Gerador

`gerar_fichas.py` agora: gera ficha para **toda** entidade com registro `fichado`/`revisado` (rótulo da lista-mestra) e apaga a ficha de quem deixou de ter; recalcula `status_conteudo`; sincroniza os espelhos e as arestas dos itãs. `validar_fichas.py` confere que tudo isso está em dia (inclui fichas criadas ou removidas ao regenerar).

## 5. Site

- **Catálogo:** um cartão por entidade da lista-mestra (33). Sem ficha: nome, tipo e "Em pesquisa" (com a distinção `pre`/sem fichamento), nenhum outro texto, nenhum link. Filtros por tipo, situação, tradição e atributo. Âncora `#e-<id>` para links de entidades sem ficha.
- **Ficha:** funciona para qualquer tipo; mostra o tipo quando não é orixá, aviso em entidade sensível e, em cada versão de itã, o link para a página do itã.
- **Itãs:** `/itans/` (lista) e `/itans/<id>/` (versões lado a lado, odu da fonte, fontes, ligação com a ficha e com arestas do grafo).
- **Cosmologia:** `/cosmologia/` mostra só versões de `hierarquia`; sem nenhuma, um aviso de estrutura vazia. Lista as entidades cosmológicas da pauta só pelo nome.
- **Grafo:** filtro "Tipos de entidade" (tipo da lista-mestra quando o nó está nela; senão o tipo do nó: santo, vodum, inquice…).
- **Baixar dados:** `/dados/entidades.json` (sem grupo não confirmado) e `/dados/itans.json` (só versões lidas).
- **URL das fichas:** continua `/orixas/<id>/` para qualquer tipo, para não quebrar links publicados.

## 6. Verificação

- Validadores: `validar_fontes`, `validar_fichamento`, `divergencias` (41, igual), `gerar_fichas`, `validar_fichas`, `anticopia` (0 erros, sem referências: a sessão não fichou fonte nova; os resumos dos itãs são as paráfrases já auditadas).
- Testes: 48 (`tests/test_modelo2.py` +11) e dois ponta a ponta: `e2e_revisao_site.py` e o novo `e2e_modelo2_site.py` (entidade não-orixá ganha ficha; Iyami só em pré-fichamento fica "Em pesquisa" com aviso; registro de hierarquia aparece na Cosmologia; texto de pré-fichamento nunca aparece; adulterações no HTML são acusadas pelo QA). Também no CI.
- `qa_site.py` §11: catálogo × lista-mestra, itãs × JSON (valor, resumo, odu, nota, fontes, tradições), Cosmologia × versões de `hierarquia`, filtro do grafo, downloads filtrados. 26 páginas, sem erro.
- Acessibilidade (axe-core): 26 páginas × 2 larguras, nenhuma violação grave.
