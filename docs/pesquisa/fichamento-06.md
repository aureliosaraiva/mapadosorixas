# Fichamento 06 — fontes abertas P1 da varredura 3

Tarefa: fichar as fontes abertas P1 do [relatório da varredura 3](relatorio-varredura-03.md) e procurar texto aberto para os 16 registros `pre_fichamento` (tarefa 4 do [`ESTADO.md`](../ESTADO.md)). Data: 2026-11-01. Os PDFs ficaram fora do repositório (`/tmp`). No repo entram só metadados, páginas e paráfrases.

## Resumo

- **5 de 9 fontes P1 lidas no original** (Castillo 2022, Costa 1980, Nascimento et al. 2001, Vallier 2011, Capo Chichi 2025), com **42 registros novos `fichado`**: Ogum 19, Exu 18, Xangô 5.
- **4 fontes P1 bloqueadas:** Prandi 1995, Giumbelli & Lima 2024, Noleto & Negrão 2025 e Ferreira 2017. SciELO e UnB respondem com desafio anti-robô, que não foi contornado. Por isso **Iemanjá não ganhou registros** nesta rodada.
- **Tarefa 4:** nenhum dos 16 `pre_fichamento` tem texto aberto acessível daqui. Detalhes abaixo.
- Catálogo: +1 fonte (`bastide-1945-imagens`) e 5 fontes primárias de 2ª mão promovidas a `conferido_web` pela Open Library: Bastide 1960, Bascom 1969, Herskovits 1938, Idowu 1962 e Johnson 1921.
- Grafo: novo nó `vodum:gu`. Três arestas novas: Ogum–Santo Antônio (sincretismo), Ogum–Gu (equivalência) e Exu–Ogum (irmãos). As demais versões novas reforçam arestas que já existiam: Exu–Legba e Ogum–Oxóssi.

## Fontes lidas no original

| Fonte | Acesso | Páginas lidas | Paginação | Registros |
|---|---|---|---|---|
| Castillo 2022, culto familiar a Ogum no Candeal (`castillo-2022-ogum`) | revistas.usp.br (PDF) | integral, 1–37 | própria do artigo (= PDF) | ogum-034 a ogum-052 |
| Costa 1980, Exu na Umbanda do Rio (`costa-1980-exu-umbanda`) | periodicos.ufba.br (PDF) | integral, 19 p. | **sem número impresso**: citada a página do PDF | exu-065 a exu-072 |
| Nascimento, Souza & Trindade 2001, pontos de Exu e Pomba-Gira (`nascimento-2001-exus`) | repositório da UFES (o SciELO está bloqueado) | integral, 107–113 | impressa | exu-073 a exu-076 |
| Vallier 2011, Èṣù e a noção de trickster (`vallier-2011-esu`) | HAL (versão com a paginação da revista) | 811–831 (sem bibliografia) | impressa | exu-077 a exu-082 |
| Capo Chichi 2025, etimologia de Xangô (`capo-chichi-2025-shango`) | journals.flvc.org (PDF) | integral, 1–10 | própria do artigo | xango-035 a xango-039 |

## Registros novos por orixá

**Ogum (19).** A principal fonte é Castillo, que mistura documentos de arquivo, tradição oral de uma família e literatura africanista.
- História do culto: o culto familiar do Candeal Pequeno (034); os assentamentos ao ar livre na África e em casinhas nos terreiros (039, via Verger); Ogou no Haiti (048, via Cosentino em Barnes).
- Domínios: guerra e ferro (036).
- Símbolos: o assentamento, de ferro no Brasil e de pedra na África (040); o mariô (041); plantas como aroeira, espada-de-Ogum e peregun (042).
- Funções: abrir caminhos no Ketu × no Jeje (043, via Parés).
- Parentesco: irmão de Exu (044, via Parés) e de Oxóssi (045, via Verger).
- Equivalência: Gu (046). Itã: o mito daomeano da gubasa (047, via Barnes & Ben-Amos).
- Origem e nomes: Iré, no leste iorubá (049); o título Onirê (050).
- Qualidades: as sete do Ketu, com Ogunjá (051); Xoroquê como a única registrada no Jeje (052).
- Sincretismo: Santo Antônio no Candeal (035).
- Agricultura: Verger diz que Ogum perdeu no Brasil o papel de protetor da lavoura (037); Castillo contesta (038).

**Exu (18).**
- Costa 1980 (Umbanda carioca, c. 1970):
  - trajetória de Nina Rodrigues a Bastide (065);
  - Bastide 1960 contra a identificação Legba = Exu (066);
  - anjo decaído × recusa da identificação com o diabo (067);
  - Exu-coroado × Exu-batizado (068);
  - escala do pagão ao coroado (069);
  - Exu como irmão mais novo de Ogum, no Omolocô (070);
  - Exu como "empregado" das entidades (071);
  - Pomba-Gira (072).
- Nascimento et al. 2001:
  - exus como "espíritos das trevas", via Ortiz (073);
  - funções nos pontos cantados (074);
  - estereótipos de gênero, raça e classe (075);
  - rua, encruzilhada e cemitério (076).
- Vallier 2011 (Nigéria e Benim):
  - Èṣù não é o diabo (077);
  - mensageiro que recebe a primeira parte dos sacrifícios (078);
  - culto presente em casas, mercados, palácios e templos, via Herskovits (079);
  - Legba como equivalente parcial (080);
  - crítica ao rótulo trickster (081);
  - o gorro de duas cores, via Bascom (082).

**Xangô (5).** Capo Chichi 2025:
- etimologia gbari/nupe e negação do rei histórico (035);
- a tradição de Oyó sobre o alafin enforcado, via Johnson, com a variante de Hethersett (036);
- Akinyemi: o deus é anterior a Oyó (037, via Tishken et al. 2009);
- difusão do culto com o império de Oyó (038);
- o epíteto Jakuta e as grafias do nome (039, via Idowu).

## Correções

Nenhum registro antigo foi alterado. Três notas novas citavam ids em `pre_fichamento` e foram reescritas antes do push, porque o `qa_site.py` acusa id de pré-fichamento fora da seção Pendências.

## Divergências novas ou ampliadas

O total foi de 32 para 33 atributos com versões divergentes. O atributo novo é `ogum.parentesco`. Várias divergências de conteúdo caíram em atributos que já estavam na lista:

| Atributo | Versões lado a lado |
|---|---|
| Xangô, origem | rei humano divinizado (xango-001, Prandi; xango-021, Chiousse) × teônimo emprestado do gbari via nupe, **sem rei histórico** (xango-035, Capo Chichi) × deus anterior a Oyó e tutelar do alafin (xango-037, Akinyemi) |
| Exu, equivalências | Legba como equivalente (exu-001, exu-040, exu-044) × equivalente só "sob certos aspectos rituais" (exu-080, Vallier) × **não identificar** Legba e Exu (exu-066, Bastide 1960 via Costa) |
| Ogum, sincretismo | São Jorge (Umbanda e Ketu: ogum-006, ogum-019) × Santo Antônio (Candeal, Salvador, desde 1950: ogum-035) |
| Ogum, interpretação | perda do papel agrícola no Brasil (ogum-037, Verger) × culto de lavradores libertos no séc. XIX (ogum-038, Castillo) |
| Ogum, qualidades | Ogunjá "come cru" e mora com Oxóssi e Exu (ogum-002, Carneiro via Prandi) × Ogunjá ligado a Exu, entre sete qualidades ketu (ogum-051) × Xoroquê, a única registrada no Jeje (ogum-052) |
| Exu, estatuto | orixá × mensageiro × "empregado" das entidades × egum (exu-065, 068, 071, com exu-034 e exu-062) |
| Exu, leitura acadêmica | trickster (exu-050, exu-056) × crítica ao rótulo (exu-081) |

## Candomblé × Umbanda

- Os registros de Costa e de Nascimento são todos `umbanda`. Duas exceções: exu-065 (trajetória na literatura baiana e carioca) e exu-066/exu-072, onde a fonte fala do Angola.
- A nação Omolocô, citada por Costa, ficou em `casa_ou_regiao` porque não há tradição própria em `data/tradicoes.json`.
- Castillo descreve um culto **familiar**, fora de terreiro. O registro ogum-034 usa `candomble_ketu` como aproximação e explica isso na nota.

## Fundamento iniciático e retidos

Nada sobre preparo de assentamento, oferendas detalhadas ou iniciação entrou nos registros. Ficaram de fora:
- o sacrifício de cachorro como "comida preferida" de Ogum e Gu (Castillo, p. 25);
- a oferenda prescrita no verso de Ifá do gorro (Vallier, p. 825);
- a lista de animais e folhas citada nesse verso.

O primeiro e o terceiro tocam `alimentos`/`animais`, que esperam o conselho.

## Anti-cópia

Com o texto das 5 obras em `ANTICOPIA_REFS`, a checagem achou 11 trechos com 8 palavras seguidas idênticas ao original. Eram listas de funções em Nascimento e frases curtas de Castillo. Todos foram reescritos. Resultado final: **0 erros**.

## Tarefa 4: texto aberto para os 16 `pre_fichamento`

| Registros | Fonte | Resultado da busca |
|---|---|---|
| ogum-005 | Ribas 2010, *Saravá Ogum* (PUC-SP) | o PDF existe no repositório da PUC-SP, mas o site responde com desafio anti-robô (HTTP 468) → PENDENCIAS §1 |
| ogum-003, ogum-004 | Brown 1989 (cap. de *Africa's Ogun*) | só o trecho do Project MUSE, que dá 403; nenhuma cópia aberta |
| ogum-008 | Barnes 1989 | livro pago; nenhuma cópia aberta |
| ogum-007 | Beier 1970 | livro impresso |
| xango-002 a xango-004 | Tishken et al. 2009 | nenhum capítulo aberto. O que Capo Chichi resume de Akinyemi entrou como xango-037, mas **não** resolve esses três registros, que tratam de outros pontos |
| xango-006 | Carneiro 1948 | nenhum texto integral aberto (há só estudos sobre a obra) |
| iemanja-003, iemanja-004 | Verger 1954 | livro impresso |
| iemanja-005, iemanja-006 | Pérez 2013 | o PDF da UCSB continua 404; o capítulo está no JSTOR, que é pago |
| oxossi-002, oxossi-003 | Silva & Silva Neto 2025 | livro impresso (Pallas) |
| oxossi-004 | Verger 1981 | livro impresso (as cópias que circulam não são autorizadas e não foram usadas) |

## Continua bloqueado (→ [`PENDENCIAS.md`](PENDENCIAS.md))

- `www.scielo.br`: Prandi 1995, Giumbelli & Lima 2024, Noleto & Negrão 2025. O PDF de Noleto tem cópia no Internet Archive (2026-07-30), mas o acesso por aqui foi recusado; o autor pode baixá-lo manualmente.
- `periodicos.unb.br` (403) e `core.ac.uk` (desafio anti-robô): Ferreira 2017.
- `lume.ufrgs.br` (conexão cortada): o número de 1995 de *Horizontes Antropológicos*.
- Prandi 1995: o DOI do catálogo não resolve, e o pid da varredura 3 é de outro artigo (Augé). É preciso conferir os dois.
- Costa 1980: falta a paginação impressa.
- Fontes de 2ª mão citadas pelas lidas e não conferidas no original. A lista está em PENDENCIAS §3.
- Pista: Castillo cita uma casa de **nação Efon** em Salvador e remete a Lima 2014, p. 148. Pode servir para dar fonte a `candomble_efon`, por uma sessão autorizada a editar `tradicoes.json`.
