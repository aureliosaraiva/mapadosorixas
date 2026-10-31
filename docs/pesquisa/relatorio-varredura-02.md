# Fase 1 — Relatório da varredura nº 2

**Data:** 2026-10-31 · **Método:** buscas na web feitas com IA, seguindo o roteiro do [relatório nº 1](relatorio-varredura-01.md). **Nenhum item passou por conferência humana ainda.**

## Limitação técnica desta rodada

O ambiente de execução **bloqueia o acesso direto às APIs** de bases bibliográficas (OpenAlex, Crossref, BDTD/VuFind, Open Library, theses.fr, Redalyc). Por isso, não foi possível fazer uma varredura exaustiva e reproduzível por API, e a coleta continuou só por buscador web. Para a próxima etapa, há duas saídas:

- liberar esses domínios nas configurações de rede do ambiente e rodar scripts de coleta (`scripts/`), que permitem reproduzir e contar os resultados; ou
- fazer as buscas manualmente na BDTD, no Catálogo CAPES e no WorldCat, exportando para o Zotero.

## Resumo

| Indicador | Varredura 1 | Varredura 2 |
|-----------|------------:|------------:|
| Fontes no catálogo | 117 | **151** |
| `conferido_web` | 35 | **57** |
| `a_verificar` | 79 | 82 |
| `pista` | 3 | 12 |
| Idiomas | pt, en, es, fr, de | pt 74 · en 48 · es 13 · fr 9 · de 4 · it 2 · **yo 1** |
| Teses e dissertações | 10 | **24** |

## Conferências de clássicos

| Fonte | Resultado |
|-------|-----------|
| Juana Elbein dos Santos, *Os Nàgô e a morte* | Vozes, Petrópolis, 1976. Tese defendida na Sorbonne em 1972, mas **as fontes divergem se é doutorado ou mestrado**. 14ª ed. em 2012. |
| Verger, *Orixás* | Corrupio, Salvador, 1981, confirmado. Há reedição com prefácio de Mãe Stella. |
| Bastide, *O candomblé da Bahia* | Edição em português: Companhia Editora Nacional, 1961 (Brasiliana v. 313), tradução de Maria Isaura Pereira de Queiroz. Há cópia digitalizada na UFRJ. |
| Bolívar, *Los orishas en Cuba* | Ediciones Unión, Havana, 1990, confirmado. |
| Lachatañeré, *¡¡Oh, mío Yemayá!!* | 1938, confirmado. 2ª ed. em 1992, com introdução de Fernando Ortiz. Edição em inglês: Markus Wiener, 2014. |
| Lachatañeré, *Manual de Santería* | Ano 1942 confirmado; **editora e local não confirmados**. |
| Mãe Stella, *Meu tempo é agora* | **O ano diverge: 1992, 1993 ou 1995.** Nova edição pela Assembleia Legislativa da Bahia (2025). |

## Coleção Orixás (Pallas)

A série pretende cobrir os 16 principais orixás cultuados no Brasil e é coordenada por Helena Theodoro. Situação até agora:

| Vol. | Orixá | Autor(a) | Ano | Situação |
|-----:|-------|----------|-----|----------|
| 1 | Logunedé | Nei Lopes | 2006 | confirmado |
| 8 | Iansã | Helena Theodoro | 2010 | confirmado (ISBN 9788534704076) |
| 9? | Exu | Vagner Gonçalves da Silva | 2015 | confirmado |
| — | Oxóssi | V. G. da Silva e J. P. da Silva Neto | 2025 | confirmado |
| — | Ossaim | Rogério Athayde | 2025 | título exato a conferir |
| — | Ogum | Reginaldo Prandi | ? | autoria citada em notícia; livro não localizado |
| — | Iemanjá | Armando Vallado | ? | autoria citada em notícia; livro não localizado |
| — | Nanã, Obá | ? | ? | aparecem no catálogo da editora sem autor |

**Pendente:** abrir cada página de produto da Pallas, ou pedir a lista à editora.

## Novidades por orixá do MVP

- **Exu**: quatro teses de doutorado (UFC 2008, Educação; UFG 2017, História, sobre Exu na Umbanda; PUC-SP 2018 e 2021, Ciência da Religião) e uma dissertação na UERJ (2019). A tese da UFG serve para a distinção obrigatória entre **Exu do Candomblé e exus da Umbanda**.
- **Ogum**: dissertação *Saravá Ogum* (PUC-SP, 2010) sobre a procissão de São Jorge; capítulo de Karen McCarthy Brown sobre **Ogou no Haiti** (em Barnes, 1989), que sustenta a equivalência Ogum ↔ Gu (fon) ↔ Ogou (Vodou).
- **Xangô**: livro novo de Prandi, *Orixás* (2025), organizado em 18 orixás; tese "Kalunga e o direito", sobre a "justiça de Xangô" (pista). Teses específicas sobre Xangô e Oyó **não apareceram**: é uma lacuna.
- **Oxóssi**: nenhuma tese específica encontrada; o livro da Pallas (2025) continua sendo a principal monografia.
- **Iemanjá**: artigo de Blass (2007) sobre o 2 de Fevereiro no Rio Vermelho. As fontes divergem sobre a origem da festa: 1923 ou por volta de 1910.

## Novidades por tradição e idioma

- **Espanhol**: Mones Guevara (2024, *Cuicuilco*/SciELO México), revisão de conceitos da Ocha; dissertações sobre a Santería na Colômbia (Medellín, 2018) e sobre a comida dos orishas (Colorado State, 2015); Rossbach de Olmos sobre os orichas na Alemanha.
- **Francês**: tese de Sylvie Chiousse (EHESS, 1995), *Divins thérapeutes*, em acesso aberto no HAL; artigo de Teisenhoffer sobre Umbanda e New Age.
- **Alemão**: Hubert Fichte, *Xango* (S. Fischer, 1976), que cobre Bahia, Haiti e Trinidad, com o volume de fotos de Leonore Mau; uma tese em alemão, *Die Erfahrung der Orixás*, ainda sem autor identificado.
- **Italiano**: Bruno Barba, *Santi, demoni e orixás* (Odoya, 2020); dois artigos sobre o candomblé na Itália (pistas).
- **Iorubá**: Abímbọ́lá, *Ìjìnlẹ̀ ohùn ẹnu Ifá* (1968), a primeira fonte em língua iorubá do catálogo. Também *Ifá Divination Poetry* (1977).
- **Haiti**: Karen McCarthy Brown, *Mama Lola* (1991).

## Divergências registradas nesta rodada (para fichar depois)

1. **Iemanjá**: as datas de festa variam por local (2 de fevereiro no Rio Vermelho; 8 de dezembro em outros lugares, ligado a Nossa Senhora da Conceição ou dos Navegantes). Também diverge a data de origem da festa do Rio Vermelho.
2. **Exu**: o orixá mensageiro do Candomblé e os exus/eguns da Umbanda (tese UFG 2017) são coisas diferentes, que precisam aparecer separadas na ficha.
3. **Ogum**: no Haiti, Ogou ganha um perfil político-militar próprio (Brown 1989). Equivalência não significa identidade.

## Lacunas que continuam

- **Teses sobre Xangô e Oxóssi**: quase nada específico. Buscar direto na BDTD e no Catálogo CAPES.
- **Inquices bantos**: nenhuma novidade nesta rodada.
- **EUA (Oyotunji, Lucumí nos EUA)**: a busca não trouxe resultados.
- **Periódicos cubanos (*Catauro*)**, **Persée/theses.fr** e **DNB/SBN**: precisam de consulta direta (bloqueada aqui).
- 82 fontes continuam `a_verificar` e 12 são `pista`, várias sem autor identificado.

## Próximos passos sugeridos

1. Liberar as APIs no ambiente, ou fazer uma rodada manual na BDTD, no CAPES e no WorldCat (ver "Limitação técnica").
2. Resolver as 12 pistas: autor, título e ano.
3. Começar o **fichamento** dos 5 orixás do MVP com as fontes A/B já `conferido_web` que têm texto aberto: Prandi 2001 (*Revista USP*), Silva 2012 (*Rev. Antropologia*), Chiousse 1995 (HAL), Mones Guevara 2024 (SciELO), Peel 2016 (OAPEN) e Bastide 1961 (cópia digital da UFRJ).
4. Iniciar a lista de possíveis revisores a partir dos autores ativos identificados, como Vagner G. da Silva, Reginaldo Prandi, Luis Nicolau Parés e Ari Pedro Oro.
