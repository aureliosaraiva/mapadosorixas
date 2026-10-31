# Fase 1 — Fichamento nº 1 (Exu, Ogum, Oxóssi, Xangô, Iemanjá)

**Data:** 2026-10-31 · **Arquivos:** [`data/fichamento/`](../../data/fichamento/) · **Esquema:** [`schemas/fichamento.schema.json`](../../schemas/fichamento.schema.json) · **Validação:** `python3 scripts/validar_fichamento.py`

## Situação

- **35 registros**, todos com status **`pre_fichamento`**: são afirmações *identificadas* em buscas e atribuídas a uma fonte A/B do catálogo, mas **ainda não lidas no texto original** (página = "a conferir"). Pelas regras do projeto, nenhum deles pode ir para uma ficha publicada.
- O validador **impede** que um registro passe a `fichado` sem página e sem fonte verificada.

### Por que não houve leitura das fontes

1. **Rede**: o ambiente bloqueia os repositórios onde estão os textos abertos (`periodicos.usp.br`, `revistas.usp.br`, `reginaldoprandi.fflch.usp.br`, HAL, SciELO, repositórios de teses). Só funciona o buscador, que devolve resumos sem página.
2. **Obras centrais impressas**: Verger (*Orixás*, *Dieux d'Afrique*), Prandi (*Mitologia dos Orixás*), Bastide, Cabrera, Cacciatore e Beniste não estão em acesso aberto e precisam ser lidas em exemplar físico ou digital legítimo.
3. **Atributos básicos** (cores, dia, saudação, símbolos, alimentos): os resultados de busca trazem quase só **blogs e sites de divulgação (nível D)**, que não podem sustentar ficha. **Não registrei nada vindo deles.** Por isso essas linhas da tabela abaixo estão vazias.

## Cobertura de atributos (nº de registros)

| atributo | exu | ogum | oxossi | xango | iemanja |
|---|---:|---:|---:|---:|---:|
| nomes | — | — | — | 1 | 1 |
| origem | — | — | 1 | 1 | 1 |
| dominios | — | — | 1 | — | — |
| funcoes | 1 | — | — | — | — |
| elementos | — | — | — | — | 1 |
| cores | — | — | — | — | — |
| dia_semana | — | — | — | — | — |
| saudacao | — | — | — | — | — |
| simbolos | — | — | — | — | — |
| alimentos | — | — | — | — | — |
| animais | — | — | — | — | — |
| qualidades | — | — | — | — | 1 |
| parentesco | — | — | — | — | 1 |
| equivalencias | 1 | 1 | — | — | — |
| sincretismo | 1 | 2 | — | — | 1 |
| itans | — | — | 1 | — | — |
| tabus | — | — | — | — | — |
| festas | — | — | — | — | 3 |
| historia_culto | 1 | 3 | 1 | 2 | 1 |
| iconografia | 2 | — | — | — | — |
| interpretacao_academica | 4 | — | — | 1 | — |

## Divergências já identificadas (a documentar com página)

| Orixá | Tema | Versões |
|-------|------|---------|
| Xangô | Posição na lista de alafins de Oyó | 3º × 4º rei, conforme a fonte |
| Xangô | Recepção no território iorubá | central em Oyó × visto como estrangeiro no leste iorubá até o fim do séc. XIX (resenha de Tishken et al. 2009) |
| Xangô | Divindades do trovão | Xangô × Ara (Tishken et al. 2009) |
| Iemanjá | Domínio aquático | rio Ògùn/Abeokuta (Nigéria) × mar (Brasil) × "águas doces e salgadas" (leitura de Verger) |
| Iemanjá | Formas | sete ou oito Iemanjás na Bahia (Verger) × "várias", sem número fixo (Bastide) |
| Iemanjá | Sincretismo e festas | N. Sra. dos Navegantes / da Conceição (Brasil, por região) × Virgem de Regla (Cuba) |
| Oxóssi | Culto em Ketu (África) | "quase desaparecido" (atribuído a Verger) × contestação |
| Exu | Natureza | orixá mensageiro (Candomblé) × exus como eguns/espíritos (Umbanda) |
| Ogum | Perfil nas Américas | Ogum (Brasil) × Ogou político-militar (Haiti) |

## Plano de leitura para o fichamento real

Prioridade 1 é o texto aberto, que pode ser lido assim que os domínios forem liberados. Prioridade 2 depende de exemplar.

| Prioridade | Fonte | Orixás | O que extrair |
|-----------:|-------|--------|---------------|
| 1 | Prandi 2001, *Revista USP* (aberto) | Exu | conferir os 7 registros e fixar páginas; funções, nomes, iconografia |
| 1 | Silva 2012, *Rev. Antropologia* (aberto) | Exu | nomes por nação, lugar no ritual (padê), Umbanda × Candomblé |
| 1 | Bastide 1961, digitalizado na UFRJ (BDOR) | todos | atributos no Ketu baiano dos anos 1950; qualidades de Iemanjá; leitura de Exu |
| 1 | Chiousse 1995 (HAL) | todos | orixás e saúde; atributos registrados em campo |
| 1 | Mones Guevara 2024 (SciELO México) | todos (lucumí) | nomes e conceitos lucumís para as equivalências |
| 1 | Peel 2016 (OAPEN) | Exu, Ogum, Xangô | culto iorubá no séc. XIX; Xangô e Oyó |
| 2 | Verger 1981 *Orixás* / 1957 *Notes* | todos | origem africana, cidades de culto, cores, dias, saudações, símbolos, equivalências fon |
| 2 | Prandi 2001 *Mitologia dos Orixás* | todos | itãs (para resumir com palavras próprias), parentescos |
| 2 | Cacciatore 1977; Beniste 1997/2011 | todos | nomes, saudações, termos iorubás com grafia |
| 2 | Cabrera 1954/1974; Bolívar 1990 | todos (lucumí) | nomes, caminhos, sincretismos cubanos |
| 2 | Parés 2006 | Exu, Ogum, Xangô | voduns jeje equivalentes (Legba, Gu, Sogbo/Badé) |
| 2 | Castro 2001; Lopes 1988 | todos | inquices equivalentes (Aluvaiá/Pambu Njila, Nkosi, Mutalambô, Nzazi, Kayala) — **a confirmar** |
| 2 | Barnes 1989/97; Tishken 2009; Otero & Falola 2013; Falola 2013 | Ogum, Xangô, Iemanjá, Exu | perspectivas nigeriana, cubana e brasileira |

> Os nomes de inquices e voduns da penúltima linha vêm do conhecimento geral da equipe e servem só como **roteiro de busca**. Ainda não são registros.

## Fontes adicionadas ao catálogo nesta etapa

- Verger, *Dieux d'Afrique* (1954?): origem egbá de Iemanjá, ano a conferir.
- Baudin, *Fétichisme et féticheurs* (1884): texto missionário citado por Prandi, nível C.
- "Oxóssi: o herói de uma flecha só" (*Revista Mosaico*, 2020): pista.
- Valéria Gomes Costa (*Afro-Ásia*, 2007), sobre o xangô em Pernambuco: pista.

## O que destrava a próxima etapa

1. **Liberar os domínios** na rede do ambiente: `periodicos.usp.br`, `revistas.usp.br`, `reginaldoprandi.fflch.usp.br`, `bdor.sibi.ufrj.br`, `halshs.archives-ouvertes.fr`, `hal.science`, `scielo.org.mx`, `scielo.br`, `library.oapen.org` (e, para a coleta automatizada, `api.openalex.org`, `api.crossref.org`, `bdtd.ibict.br`, `theses.fr`).
2. **Acesso humano às obras impressas** da prioridade 2, ou envio de trechos e páginas pelo autor do projeto para fichamento assistido. O texto copiado serve só para a leitura; o que entra no repositório é paráfrase com página.
