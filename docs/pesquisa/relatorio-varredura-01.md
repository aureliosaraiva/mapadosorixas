# Fase 1 — Relatório da varredura nº 1

**Data:** 2026-10-31 · **Método:** buscas na web (catálogos de bibliotecas, editoras, periódicos, repositórios de teses) feitas com IA, conforme a seção 1.3 do [`PLANO.md`](../PLANO.md). **Nenhum item passou por conferência humana ainda.**

## Resumo

| Indicador | Antes | Depois |
|-----------|------:|-------:|
| Fontes no catálogo | 78 | **117** |
| `conferido_web` (metadados batidos com página de catálogo, editora ou periódico) | 0 | **35** |
| `a_verificar` | 78 | 79 |
| `pista` (dados incompletos) | 0 | 3 |
| Idiomas | pt, en, es, fr, de | pt 56 · en 44 · es 9 · fr 7 · de 1 |

Catálogo: [`data/fontes/catalogo.json`](../../data/fontes/catalogo.json). Validação: `python3 scripts/validar_fontes.py`.

## O que foi feito

1. **Conferência do catálogo inicial**: datas e editoras de Ferretti, UNESCO (Ifá), Dantas, Barnes, Verger (1957), Parés, Prandi (2001), Cabrera (1974) e dos tombamentos do IPHAN.
2. **Busca por orixá do MVP** (Exu, Ogum, Oxóssi, Xangô, Iemanjá) em pt/en/es.
3. **Busca por tradição**: inquices bantos, jeje/vodum, Batuque (RS), Xangô do Recife, Santería/Lucumí, vodun no Benim/Togo (fr), poesia oral iorubá (oríkì, ìjálá).
4. **Busca por idioma** em alemão e italiano (sem resultado útil; ver lacunas).

## Correções e divergências encontradas no catálogo inicial

| Fonte | Achado |
|-------|--------|
| Ferretti, *Querebentã de Zomadônu* | 1ª ed. **1985** (EDUFMA) confirmada; 2ª ed. revista em 1996; 3ª ed. pela Pallas. Uma citação com data de 1995 parece ser erro. |
| UNESCO, Ifá | Proclamado **Obra-Prima em 2005**; inscrito na Lista Representativa em **2008**. Há fontes que confundem as duas datas. |
| Dantas, *Vovó nagô e papai branco* | Graal, 1988; edição em inglês pela UNC Press (2009). Nasceu do mestrado na Unicamp. |
| Barnes (org.), *Africa's Ogun* | 1989 confirmado; 2ª ed. ampliada (1997) traz cinco ensaios novos sobre Ogum nas Américas. |
| Cabrera, *Yemayá y Ochún* | Ano 1974 confirmado, mas **local e editora divergem** (uma bibliografia indica "New York: Ediciones C.R."). Madri não foi confirmado. |
| Nei Lopes, *Bantos, malês e identidade negra* | 1ª edição em **1987 ou 1988** (as fontes divergem). |
| IPHAN, tombamentos | Casa Branca: decisão em 1984, homologação em 1986. Opô Afonjá: 2000. **Alaketu: 2004, 2005 ou 2008** e **Gantois, Bate Folha e Casa das Minas: 2005 ou 2006**, conforme a fonte. Oxumaré: 2014. Precisa ser conferido no Livro do Tombo. |

## Fontes novas mais relevantes para o MVP

- **Exu**: Prandi, "Exu, de mensageiro a diabo" (*Revista USP*, 2001, acesso aberto); Vagner G. da Silva, "Exu do Brasil" (*Rev. Antropologia*, 2012), *Exu: o guardião da casa do futuro* (Pallas, 2015) e *Exu: um deus afro-atlântico no Brasil* (Edusp, 2022); Falola (org.), *Èṣù* (2013).
- **Ogum**: Barnes (org.) 1989/1997 (já estava no catálogo); dissertação de Paola Odònílé (UNEB, 2023).
- **Oxóssi**: Silva & Silva Neto, *Oxóssi: o caçador divino* (Pallas, 2025).
- **Xangô**: Tishken, Falola & Akinyemi (orgs.), *Ṣàngó in Africa and the African Diaspora* (2009). Uma resenha registra que, no leste iorubá, Xangô era visto como divindade estrangeira até o fim do séc. XIX, o que é **material direto para a seção de divergências**.
- **Iemanjá**: Otero & Falola (orgs.), *Yemoja* (2013); capítulo de Elizabeth Pérez sobre Yemayá em Cuba; teses sobre festas de Iemanjá em Belém (UFPA, 2015) e no Rio (PUC-Rio, 2021).

## Achados úteis para a futura seção de divergências (a fichar)

- Iemanjá: na Nigéria, ligada ao rio Ògùn e a Abeokuta; no Brasil, ao mar. Verger contou sete ou oito "Iemanjás" na Bahia.
- Exu: de mensageiro e princípio de ordem a trickster, e depois associado ao diabo pelo sincretismo (Prandi 2001; Silva 2012).
- Xangô: quarto alafin de Oyó, segundo a tradição oral de Oyó, mas com recepção diferente no leste iorubá (Tishken et al. 2009).
- Batuque (RS): nações Jeje, Ijexá (a predominante), Oyó, Cabinda e Nagô; 12 orixás. Os nomes também variam: Bará, Odé, Xapanã etc. (Oro 2008).

> Estes pontos ainda **não** são conteúdo de ficha: precisam ser lidos na fonte, fichados com página e parafraseados.

## Coleção Orixás (Pallas) — mapear completa

É uma série de monografias por orixá, cada uma escrita por um especialista. Volumes identificados até agora: Exu (Vagner G. da Silva), Ogum (Reginaldo Prandi?), Iemanjá (Armando Vallado?), Iansã (Helena Theodoro), Logunedé (Nei Lopes), Oxóssi (Silva & Silva Neto, 2025), Ossaim (Rogério Athayde, 2025) e talvez Xangô (Ildásio Tavares, 2006). Os volumes de Ogum e Iemanjá **não foram confirmados**. Próximo passo: levantar a lista completa no site da Pallas.

## Lacunas identificadas

1. **Alemão e italiano**: nenhuma obra relevante apareceu na busca aberta. Buscar diretamente nos catálogos da DNB (Alemanha) e do SBN (Itália).
2. **Inquices bantos**: só há dissertações de mestrado e poucas obras de referência. É a tradição mais pobre em fontes; vale priorizar Yeda Pessoa de Castro, Nei Lopes, Robert Slenes e contato com casas Angola.
3. **Periódicos cubanos** (*Catauro*, *Del Caribe*): nada encontrado na busca aberta; consultar direto no site das revistas, na Redalyc e na Dialnet.
4. **Oxford Research Encyclopedia of Religion**: verbetes não localizados; consultar no site.
5. **Fontes em iorubá** (oríkì, ẹsẹ Ifá publicados em iorubá): ainda não buscadas a fundo.
6. **Teses (BDTD/CAPES)**: falta uma varredura sistemática por orixá, com os termos de busca da seção 1.3.
7. **Trinidad, Haiti e EUA**: só as obras do catálogo inicial; não houve busca nova.

## Fontes de baixa qualidade a evitar (vistas nesta rodada)

- PDFs genéricos do tipo "Handbook of Yoruba Religious Concepts" em sites agregadores: conteúdo de SEO, alguns com texto de preenchimento.
- Portais de divulgação (Significados, sites de horóscopo ou "orixá do ano"): nível D, servem só como pista.

## Próxima varredura (nº 2)

1. Varredura sistemática na BDTD e no Catálogo CAPES para cada orixá do MVP e para "inquice", "vodum", "Batuque", "Xangô de Pernambuco".
2. Lista completa da Coleção Orixás (Pallas).
3. SciELO, Redalyc e Dialnet com os termos em espanhol; números de *Afro-Ásia* com temática de orixás.
4. theses.fr, HAL e Persée (francês).
5. Catálogos da DNB e do SBN (alemão e italiano).
6. Conferir no WorldCat as 79 fontes ainda `a_verificar`, começando pelas que serão usadas nas fichas do MVP.

## Evidências (páginas consultadas nesta rodada)

As URLs ficam no campo `evidencias` de cada fonte no catálogo.
