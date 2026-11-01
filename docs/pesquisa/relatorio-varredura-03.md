# Fase 1 — Relatório da varredura nº 3 (coleta automatizada)

**Data:** 2026-10-31 · **Método:** coleta por API, reproduzível, com scripts em [`scripts/coleta/`](../../scripts/coleta/). **Nenhum item passou por conferência humana.** Nada foi fichado nesta rodada: só catálogo.

## Resumo

| Indicador | Antes | Depois |
|---|---:|---:|
| Fontes no catálogo | 169 | **315** |
| `conferido_web` | 80 | **220** (129 novas + 11 promovidas de `a_verificar`/`pista`) |
| `a_verificar` | 79 | 68 |
| `pista` | 10 | 27 (17 novas) |
| Idiomas | pt 84 · en 52 · es 13 · fr 13 · de 4 · it 2 · yo 1 | pt 158 · en 94 · fr 36 · es 18 · de 6 · it 2 · yo 1 |
| Tradições menos cobertas (fontes no catálogo) | Angola 18 · Jeje 8 · Batuque 5 · Xangô-PE 5 · Mina 3 · Trinidad 7 | Angola 27 · Jeje 15 · Batuque 15 · **Xangô-PE 25** · **Mina 18** · **Trinidad 23** |

## Como reproduzir

```bash
python3 scripts/coleta/coletar.py --data 2026-10-31   # consulta as bases e grava data/fontes/coleta/<data>/<base>.json
python3 scripts/coleta/triar.py --data 2026-10-31     # deduplica e compara com o catálogo → candidatos.json
python3 scripts/coleta/triagem_2026-10-31.py          # decisões manuais (legíveis no script) → triagem.json
python3 scripts/coleta/incorporar.py --data 2026-10-31   # aplica ao catálogo; grava triagem_resumo.json
```

- `consultas.json`: as 61 consultas (id, termo, idioma, alvo). Cada consulta roda em todas as bases, com até 20 resultados por base.
- `pertinencia.py`: termos de pertinência. Termos **fortes** (orixá, candomblé, santería, lucumí, vodou/vodum, inquice, batuque, tambor de mina, terreiro, nomes dos orixás em grafias não ambíguas) bastam. Termos **fracos** (Ogun, Exu/Esu, Sango, Yoruba, Oyo, Fon) só contam junto com outro termo, para excluir, por exemplo, "Ogun State".
- **Resumos (abstracts) não são gravados**, porque são texto de terceiros. Guardamos só os termos encontrados neles.
- Deduplicação por DOI, ISBN (normalizado para ISBN-13), título sem subtítulo + ano e, por fim, o mesmo registro da base devolvido por várias consultas. Fontes já no catálogo são reconhecidas também por identificadores e DOI nas evidências.
- `incorporar.py` reconsulta cada DOI no Crossref antes de gravar. Isso confirma o DOI e completa o subtítulo, que a coleta de 2026-10-31 não pedia (o coletor já foi corrigido). O idioma é detectado pelo título, porque a DOAJ informa os idiomas da revista e o Crossref não informa idioma; 6 casos foram corrigidos à mão.

## Acesso às bases (testado em 2026-10-31)

| Base | Situação | Itens baixados |
|---|---|---:|
| Crossref (`api.crossref.org`) | ✅ funciona; 429 intermitente depois de ~300 requisições (backoff resolve) | 1.118 |
| Open Library (`openlibrary.org/search.json`) | ✅ | 451 |
| theses.fr (API `/api/v1/theses/recherche`) | ✅ | 96 |
| HAL (`api.archives-ouvertes.fr`) | ✅ (não pedida, incluída) | 113 |
| DOAJ (`doaj.org/api`) | ✅ (não pedida, incluída) | 308 |
| BDTD (VuFind API) | 🔴 `HTTP 400 Problem connecting to Solr` em todas as consultas; páginas HTML dão 500 | 0 |
| OpenAlex | 🔴 429: o orçamento diário sem chave, compartilhado pelo IP do ambiente, estava esgotado. O coletor aceita `OPENALEX_API_KEY` | 0 |
| DataCite, BASE | 🔴 desafio anti-robô ("Making sure you're not a bot") | — |
| SciELO Search, CORE API | 🔴 403 / redirecionamento para login | — |
| oasisbr (VuFind) | 🔴 503 | — |

Tudo isso foi registrado em [`PENDENCIAS.md`](PENDENCIAS.md) §1.

## Contagens

**2.086 itens baixados** → **1.466 grupos únicos** após a deduplicação → 42 já estavam no catálogo · 506 sem nenhum termo de pertinência (descarte automático) · **918 candidatos** pertinentes para a triagem.

### Itens baixados por base e idioma da consulta

| Base | pt | es | en | fr | de | it | yo | total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| crossref | 400 | 119 | 260 | 160 | 60 | 40 | 79 | 1118 |
| openlibrary | 141 | 73 | 82 | 55 | 7 | 24 | 69 | 451 |
| thesesfr | 13 | 4 | 4 | 20 | 0 | 13 | 42 | 96 |
| hal | 21 | 6 | 5 | 39 | 0 | 0 | 42 | 113 |
| doaj | 167 | 38 | 15 | 25 | 0 | 0 | 63 | 308 |

### Resultados por consulta (total informado pela base / itens baixados)

Atenção ao comparar os números:

- O **total do Crossref não é contagem de correspondência exata**: a busca bibliográfica pontua qualquer registro que tenha algum dos termos (por exemplo, "festa de Iemanjá" retorna 10 milhões). Só os 20 primeiros, ordenados por relevância, foram baixados.
- Nas grafias com diacríticos iorubás (`Èṣù`, `Ṣàngó`), Open Library, HAL e DOAJ removem os acentos e casam com "esu" e "sango" comuns, o que infla o total.
- `Ọ̀ṣọ́ọ̀sì` não deu nenhum resultado em nenhuma base.

| Consulta | Termo | Idioma | crossref | openlibrary | thesesfr | hal | doaj |
|---|---|:-:|---:|---:|---:|---:|---:|
| `exu-pt-1` | Exu orixá | pt | 316/20 | 6/6 | 2/2 | 2/2 | 22/20 |
| `exu-pt-2` | Exu candomblé | pt | 1400/20 | 10/10 | 2/2 | 1/1 | 19/19 |
| `exu-pt-3` | Exu umbanda | pt | 808/20 | 40/20 | 2/2 | 1/1 | 17/17 |
| `exu-yo-1` | Èṣù | yo | 16/16 | 434/20 | 38/20 | 682/20 | 465/20 |
| `exu-en-1` | Eshu Yoruba | en | 4448/20 | 12/12 | 1/1 | 2/2 | 0/0 |
| `exu-en-2` | Esu Elegbara | en | 2207/20 | 3/3 | 0/0 | 0/0 | 0/0 |
| `exu-es-1` | Elegguá | es | 7/7 | 20/20 | 1/1 | 2/2 | 6/6 |
| `exu-es-2` | Eleguá santería | es | 356/20 | 0/0 | 1/1 | 0/0 | 0/0 |
| `exu-fr-1` | Legba vodou | fr | 966/20 | 6/6 | 0/0 | 0/0 | 1/1 |
| `exu-fr-2` | Legba dieu fon | fr | 13234/20 | 1/1 | 0/0 | 0/0 | 0/0 |
| `ogum-pt-1` | Ogum orixá | pt | 161/20 | 7/7 | 0/0 | 0/0 | 4/4 |
| `ogum-pt-2` | Ogum São Jorge | pt | 147732/20 | 2/2 | 0/0 | 0/0 | 2/2 |
| `ogum-yo-1` | Ògún òrìṣà | yo | 33/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `ogum-en-1` | Ogun Yoruba god iron | en | 533107/20 | 1/1 | 1/1 | 0/0 | 2/2 |
| `ogum-es-1` | Ogún oricha | es | 38/20 | 1/1 | 0/0 | 0/0 | 0/0 |
| `ogum-fr-1` | Ogou vodou | fr | 977/20 | 4/4 | 0/0 | 0/0 | 1/1 |
| `oxossi-pt-1` | Oxóssi | pt | 21/20 | 44/20 | 0/0 | 0/0 | 19/19 |
| `oxossi-pt-2` | Oxóssi caçador orixá | pt | 764/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `oxossi-yo-1` | Ọ̀ṣọ́ọ̀sì | yo | 0/0 | 0/0 | 0/0 | 0/0 | 0/0 |
| `oxossi-es-1` | Ochosi | es | 2/2 | 9/9 | 0/0 | 0/0 | 1/1 |
| `oxossi-en-1` | Oshosi orisha | en | 143/20 | 2/2 | 0/0 | 0/0 | 0/0 |
| `xango-pt-1` | Xangô orixá | pt | 143/20 | 9/9 | 2/2 | 3/3 | 1/1 |
| `xango-yo-1` | Ṣàngó | yo | 6/6 | 509/20 | 18/18 | 106/20 | 156/20 |
| `xango-en-1` | Shango Oyo | en | 4904/20 | 0/0 | 0/0 | 0/0 | 1/1 |
| `xango-en-2` | Sango Yoruba thunder | en | 9207/20 | 1/1 | 0/0 | 1/1 | 3/3 |
| `xango-es-1` | Changó santería | es | 416/20 | 9/9 | 0/0 | 0/0 | 0/0 |
| `iemanja-pt-1` | Iemanjá | pt | 82/20 | 59/20 | 0/0 | 2/2 | 41/20 |
| `iemanja-pt-2` | festa de Iemanjá | pt | 10363256/20 | 5/5 | 0/0 | 0/0 | 6/6 |
| `iemanja-yo-1` | Yemọja | yo | 4/4 | 9/9 | 3/3 | 1/1 | 4/4 |
| `iemanja-en-1` | Yemoja orisha | en | 163/20 | 1/1 | 1/1 | 1/1 | 0/0 |
| `iemanja-es-1` | Yemayá | es | 10/10 | 70/20 | 1/1 | 3/3 | 11/11 |
| `iemanja-fr-1` | Yemanja déesse | fr | 408/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `angola-pt-1` | candomblé de Angola | pt | 10367846/20 | 12/12 | 1/1 | 8/8 | 28/20 |
| `angola-pt-2` | inquice candomblé | pt | 1139/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `angola-pt-3` | nkisi candomblé congo angola | pt | 53137/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `jeje-pt-1` | candomblé jeje vodum | pt | 1586/20 | 0/0 | 0/0 | 0/0 | 1/1 |
| `jeje-fr-1` | vodun Bénin culte | fr | 6665/20 | 1/1 | 7/7 | 11/11 | 0/0 |
| `jeje-en-1` | vodun Fon Dahomey religion | en | 415901/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `batuque-pt-1` | batuque Rio Grande do Sul religião | pt | 1937304/20 | 0/0 | 0/0 | 0/0 | 2/2 |
| `batuque-pt-2` | batuque orixás Porto Alegre | pt | 60061/20 | 1/1 | 1/1 | 0/0 | 1/1 |
| `xangope-pt-1` | Xangô do Recife | pt | 1799103/20 | 4/4 | 0/0 | 1/1 | 7/7 |
| `xangope-pt-2` | Xangô de Pernambuco terreiro | pt | 10360950/20 | 2/2 | 0/0 | 0/0 | 0/0 |
| `mina-pt-1` | Tambor de Mina | pt | 10367254/20 | 14/14 | 3/3 | 3/3 | 32/20 |
| `mina-pt-2` | Casa das Minas São Luís | pt | 1208500/20 | 9/9 | 0/0 | 0/0 | 8/8 |
| `lucumi-es-1` | Regla de Ocha | es | 10359321/20 | 13/13 | 1/1 | 1/1 | 20/20 |
| `lucumi-es-2` | lucumí orichas Cuba | es | 34140/20 | 1/1 | 0/0 | 0/0 | 0/0 |
| `lucumi-en-1` | Lucumí religion | en | 413080/20 | 14/14 | 0/0 | 0/0 | 2/2 |
| `lucumi-en-2` | Santería orishas Cuba | en | 34357/20 | 20/20 | 1/1 | 0/0 | 0/0 |
| `trinidad-en-1` | Orisha Trinidad | en | 14983/20 | 21/20 | 0/0 | 1/1 | 7/7 |
| `trinidad-en-2` | Shango Trinidad cult | en | 77852/20 | 3/3 | 0/0 | 0/0 | 0/0 |
| `trinidad-en-3` | Spiritual Baptists Trinidad Orisha | en | 89563/20 | 5/5 | 0/0 | 0/0 | 0/0 |
| `geral-fr-1` | candomblé orixás | fr | 1309/20 | 62/20 | 4/4 | 12/12 | 54/20 |
| `geral-fr-2` | religion des orisha | fr | 3058070/20 | 83/20 | 2/2 | 10/10 | 1/1 |
| `geral-fr-3` | santería cubaine | fr | 575/20 | 3/3 | 7/7 | 6/6 | 2/2 |
| `geral-de-1` | Candomblé Religion Brasilien | de | 416346/20 | 6/6 | 0/0 | 0/0 | 0/0 |
| `geral-de-2` | Orisha Yoruba Religion Götter | de | 418913/20 | 0/0 | 0/0 | 0/0 | 0/0 |
| `geral-de-3` | Santería Kuba Religion | de | 416546/20 | 1/1 | 0/0 | 0/0 | 0/0 |
| `geral-it-1` | candomblé religione | it | 2128/20 | 393/20 | 13/13 | 0/0 | 0/0 |
| `geral-it-2` | santería culto orisha | it | 2924/20 | 4/4 | 0/0 | 0/0 | 0/0 |
| `geral-yo-1` | ẹ̀sìn òrìṣà | yo | 13/13 | 0/0 | 0/0 | 0/0 | 1/1 |
| `geral-yo-2` | òrìṣà Yorùbá | yo | 895/20 | 37/20 | 1/1 | 1/1 | 18/18 |

## Triagem: quantos entraram e por quê

| Decisão | n | Motivo |
|---|---:|---|
| **entra** (`conferido_web`) | **129** | tema central = orixás do MVP ou tradições com poucas fontes; periódico com revisão por pares, tese ou editora universitária; metadados de API, com a URL em `evidencias` e a justificativa da confiabilidade em `observacoes` |
| **pista** | 17 | sem ano no registro (8 dissertações/teses), possível resenha (Nascimento 2007), periódico pouco conhecido, divulgação (Pallas), ano a conferir (Segato, *Iemanjá em família*) |
| descarta (manual) | 17 | 11 duplicatas de fontes já catalogadas (reedições, traduções: Parés 2013 em inglês, Verger em francês, Barnet em alemão, Cabrera no Brasil etc.), 3 usadas para conferir fontes do catálogo, 1 resenha de disco, 1 tese já representada pelo livro |
| não incorporado: autopublicação ou editora esotérica | 67 | CreateSpace, Independently Published, Lulu, Llewellyn, Original Publications, Madras, Eco, Espiritualista, Inner Traditions, Panapo etc. |
| não incorporado: tipo não bibliográfico | 45 | componentes, verbetes do OED, vídeos, datasets |
| não incorporado: capítulo de obra catalogada | 17 | capítulos de Parés 2006/2013, Cros Sandoval 2007, Capone 2010, Matory, Brown (*Mama Lola*) |
| não incorporado: resenha | 10 | resenhas de livros |
| não incorporado: periférico | 616 | pertinentes, mas centrados em literatura, artes, educação, saúde, turismo ou tema geral, sem foco nos 5 orixás nem nas tradições-alvo. **Continuam em `candidatos.json`** para rodadas futuras (por exemplo, quando o projeto passar dos 5 orixás). Este é o maior grupo e foi decidido por regra, não item a item; a lista completa, com motivo, está em `triagem_resumo.json` |

**Os 129 que entraram:** confiabilidade A 19 · B 110. Tipos: 80 artigos, 35 livros, 9 teses, 4 capítulos, 1 documento. Idiomas: pt 61 · en 41 · fr 21 · es 4 · de 2. Por tradição: Ketu 22 · iorubá/Nigéria 21 · Lucumí 21 · **Xangô de Pernambuco 18** · Umbanda 17 · **Trinidad 16** · **Tambor de Mina 13** · **Batuque 9** · Angola 5 · Jeje 5 · vodum/Benim 5.

**Conferências (11 promovidas a `conferido_web`):** Carybé 1980, Prandi 2005 (*Segredos guardados*), Silva 1994, Matory 2005, Brown 2003, Henry 2003, Houk 1995, Seyfeli-Kul 2020 (Crossref), Falola & Genova 2005, Cabrera 1954 (*El Monte*) e Cabrera 1974 (Open Library só registra a ed. de 1980; o ano citado foi mantido e a divergência anotada).

**Critérios de confiabilidade:** A = monografia de pesquisador de referência, ou estudo clássico citado na literatura (Wescott 1962, Pemberton 1975, Barber 1990, Costa Lima 1966, Simpson 1965, Valente 1954, Fernandes 1937, Verger 1981 *Oxossi*, Santos 2014 *Èṣù*, Ferretti 1995 etc.); B = artigo com revisão por pares, tese ou capítulo acadêmico, ou obra publicada por sacerdote(isa) (Mãe Stella de Oxóssi, Adalberto Ojuobá Pernambuco), marcada como `praticante`. Tradições inferidas de título ou resumo, sem nação explícita, estão anotadas em `observacoes` ("nação a confirmar").

## Lacunas que continuam

- **BDTD e OpenAlex** não responderam. As teses brasileiras vieram só pelo Crossref (dissertações USP/UnB, quase sempre sem ano) e pelo theses.fr (teses francesas sobre o Brasil). **A lacuna de teses brasileiras recentes continua.**
- **Oxóssi** continua a lacuna principal do MVP: só Verger 1981 (*Oxossi, o caçador*), Mãe Stella 2006 e 2016 e capítulos de Cros Sandoval. `Ọ̀ṣọ́ọ̀sì` e `Ochosi` quase não aparecem em bases acadêmicas.
- **Candomblé Angola/inquices e Jeje:** só 5 entradas cada. Os nomes dos inquices equivalentes continuam dependendo de Castro 2001 e Lopes (impressos).
- **Iorubá (yo):** nenhuma obra escrita em iorubá entrou. As consultas em iorubá trouxeram literatura em inglês (Barber, Oyèláràn, Capo Chichi).
- **Italiano e alemão:** pouco além de Rauhut 2012 e Zander-Giacomuzzi 1981. As consultas em italiano trouxeram sobretudo itens periféricos.
- **Saudações e itãs** não aparecem em metadados: continuam dependendo de Verger, Prandi, Cacciatore e Beniste (impressos).

## Fontes abertas prioritárias para fichamento

Texto integral aberto, ordenado pelo que destrava no MVP:

| Prioridade | Fonte | Para quê | Texto |
|:-:|---|---|---|
| P1 | Castillo 2022, culto familiar a Ogum (Rev. História USP) | Ogum: história de culto em Salvador | [revistas.usp.br](https://www.revistas.usp.br/revhistoria/article/view/180892) |
| P1 | Ferreira 2017, Legbá do vodum ao caboclo (Calundu) | Exu/Legba no Tambor de Mina: equivalência e divergência | [periodicos.unb.br](https://periodicos.unb.br/index.php/revistacalundu/article/view/7621) |
| P1 | Nascimento et al. 2001, Exus e Pombas-Giras (Psicologia em Estudo) | distinção Exu orixá × exus da Umbanda | [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1413-73722001000200015) |
| P1 | Costa 1980, Exu na Umbanda do Rio (Afro-Ásia) | idem, com perspectiva histórica | [doi:10.9771/aa.v0i13.20812](https://doi.org/10.9771/aa.v0i13.20812) |
| P1 | Prandi 1995, Deuses africanos no Brasil contemporâneo (Horizontes) | panorama de orixás e nações (autor de referência) | [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0104-71831995000300010&lng=pt&tlng=pt) |
| P1 | Giumbelli & Lima 2024, monumentos a Iemanjá (Rel. & Soc.) e Noleto & Negrão 2025, Iemanjá em Montevidéu | Iemanjá: culto público e transnacional | [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-85872023000300201&tlng=pt) · [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-85872025000100101&lng=pt&tlng=pt) |
| P1 | Capo Chichi 2025, etimologia de "Shango" (Yoruba Studies Review) | Xangô: nome e grafias | [journals.flvc.org](https://journals.flvc.org/ysr/article/view/139147) |
| P1 | Vallier 2011, Èṣù (Cahiers d'études africaines) | Exu no Benim/Nigéria | [HAL](https://hal.science/hal-02443068v1) |
| P2 | Halloy 2005, tese sobre o Xangô do Recife | descrição de `xango_pernambuco` e dos orixás nessa tradição | [HAL](https://hal.science/tel-04260456v1) |
| P2 | Pitta 2011, Mitos e símbolos nos xangôs de Pernambuco (Fundaj) | idem | [fundaj](https://fundaj.emnuvens.com.br/CAD/article/view/977) |
| P2 | Santana 2023, ialorixá do Xambá | idem (Nação Xambá) | [revistas.uece.br](https://revistas.uece.br/index.php/redufor/article/view/11423) |
| P2 | M. Ferretti 2020, Pureza nagô e nações no Tambor de Mina; Ferretti 1996, Acossi; Ferretti 2011, Comida ritual | `tambor_de_mina`; voduns × orixás | [CSR](https://econtents.bc.unicamp.br/inpec/index.php/csr/article/view/13302) · [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0104-71831996000400061&lng=pt&tlng=pt) · [PUC Minas](http://periodicos.pucminas.br/index.php/horizonte/article/view/2092) |
| P2 | Mendes 2014, candomblé angola e caboclo (Periferia) | `candomble_angola` | [UERJ](http://www.e-publicacoes.uerj.br/index.php/periferia/article/view/17276) |
| P2 | Oro 2012, campo afro-religioso gaúcho (Civitas); Corrêa 1996, culinária do batuque | `batuque_rs` | [PUCRS](https://revistaseletronicas.pucrs.br/ojs/index.php/civitas/article/viewFile/13015/8684) · [SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0104-71831996000400049&lng=pt&tlng=pt) |
| P2 | Argyriadis 2005 (JSA), Niell 2023 (*Religions*) | `lucumi` (Yemayá de Regla) | [doi:10.4000/jsa.3022](https://doi.org/10.4000/jsa.3022) · [MDPI](https://www.mdpi.com/2077-1444/14/12/1545) |
| P2 | Toutain 2019 e Cerqueira 2015 (teses, theses.fr) | Lucumí em Matanzas; vodum jeje Lebabimibome | [theses.fr](https://theses.fr/2019TOU20076) · [theses.fr](https://theses.fr/2015USPCB181) |
| P3 | Fontes 2021 (Afro-Ásia), Ramos 2010 (Resgate), Ogunleye 2015 (Inkanyiso), Marques 2018, Queiroz 2022 | complementares | ver `url` no catálogo |

Para **Orisha de Trinidad** (tradição ainda sem fonte), as fontes centrais (Simpson 1962/1965, Henry 1983, Trotman 1976/2007, Aiyejina & Gibbons 1999, Houk 2024) estão em periódicos ou editoras pagos. Os PDFs de *Caribbean Quarterly* e *American Anthropologist* costumam estar em bibliotecas, o que fica como pendência de exemplar.

## Limitações

- A triagem manual olhou título, autoria, revista, editora e termos do resumo, **sem ler os textos**. Tradição e confiabilidade são preliminares.
- 616 candidatos pertinentes foram deixados de fora por uma regra de recorte (periférico), não por erro de pertinência. Se o escopo crescer, revisitar `candidatos.json`.
- A coleta é uma amostra: até 20 itens por consulta e por base. Repetir com `--linhas 50` e com BDTD/OpenAlex quando estiverem acessíveis.
