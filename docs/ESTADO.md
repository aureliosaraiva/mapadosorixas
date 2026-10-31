# Estado do projeto

> Arquivo de passagem entre sessões. **Toda sessão começa lendo este arquivo e termina atualizando-o.** Mantenha-o curto, com no máximo uma página: o detalhe fica nos relatórios linkados.

**Última atualização:** 2026-10-31

## Onde estamos

**Fase 1 — Levantamento, catalogação e fichamento** (ver [`PLANO.md`](PLANO.md), seção "Fase 1"). As fases 2 a 7 ainda não começaram.

| Indicador | Valor | Como conferir |
|---|---:|---|
| Fontes no catálogo | 168 (60 `conferido_web`, 95 `a_verificar`, 13 `pista`) | `python3 scripts/validar_fontes.py` |
| Registros de fichamento | 198 (179 `fichado`, 19 `pre_fichamento`, 0 `revisado`) | `python3 scripts/validar_fichamento.py` |
| Atributos com versões divergentes | 31 | `python3 scripts/divergencias.py` |
| Idiomas no catálogo | pt, en, es, fr, de, it, yo | — |

Registros por orixá: Exu 61 · Iemanjá 47 · Xangô 34 · Ogum 29 · Oxóssi 27.

**Fontes já lidas no original:** Prandi 2001; Bastide 1961 (pp. 26–32, 89–128, 165, 182–192); Chiousse 1995 (pp. 225–291); Silva 2012 (parcial); Blass 2007; Seixas 2018; Queiroga & Nascimento 2019; Souza 2020; resumos de Cardoso Filho 2015 e Teixeira 2021.

## Próximas tarefas (em ordem)

1. **Saudações, itãs e origem africana** dos 5 orixás. Depende de Verger, Prandi (*Mitologia*), Cacciatore e Beniste, que precisam de exemplar → [`PENDENCIAS.md`](pesquisa/PENDENCIAS.md) §2.
2. **Equivalências com inquices e voduns.** Depende de Castro 2001, Parés 2006 e Lopes 1988 (exemplar).
3. **Resolver os 19 `pre_fichamento`.** São fontes pagas ou fora do ar (Tishken 2009, Brown 1989, Pérez 2013, Barnes 1989, Beier 1970, teses PUC-SP/UFPB/UFG).
4. **Conferir as fontes `a_verificar`** usadas no fichamento (WorldCat, ISBN, DOI).
5. **Fase 2:** esquema das fichas (`data/orixas/*.json`), `tradicoes.json` e `conexoes.json`, a partir do fichamento.
6. **Conselho consultivo:** levantar possíveis revisores (praticantes e pesquisadores) e começar a revisão das fichas → status `revisado`.

## Decisões já tomadas

- Commit e push **direto na `main`**, sem branch nem PR (pedido do autor).
- Só fontes A/B sustentam ficha. Blogs e sites de divulgação (nível D) servem apenas como pista.
- Registro `fichado` exige página e fonte lida pelo menos `conferido_web`. Afirmação de 2ª mão leva `via_source_id`.
- Divergências ficam lado a lado, com casa, região e fonte, sem eleger versão correta (gerado por `scripts/divergencias.py`).
- **Tabus e alimentos rituais:** não detalhar. Decidir com o conselho o que é público.
- Todo bloqueio (domínio, paywall, livro impresso, conferência humana) vai para [`pesquisa/PENDENCIAS.md`](pesquisa/PENDENCIAS.md).
- PDFs baixados ficam fora do repositório. No repo entram só metadados e paráfrase.

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
| `scripts/` | validação e geração |

## Pedido de abertura sugerido

> Leia `CLAUDE.md` e `docs/ESTADO.md`. Tarefa desta sessão: **[tarefa]**. Ao terminar: rode os validadores, atualize `docs/ESTADO.md` e `docs/pesquisa/PENDENCIAS.md`, faça o commit e o push na `main`.
