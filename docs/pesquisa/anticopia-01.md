# Auditoria anti-cópia 01

Sessão `anticopia` (2026-11-01). Tarefa: sugestão (b) da sessão do glossário no [`ESTADO.md`](../ESTADO.md), repetir o anti-cópia **com o texto integral das fontes** para todas as obras abertas já lidas no fichamento, nas tradições e no glossário. **Nada em `data/`, `schemas/` ou `site/` foi alterado:** este relatório só aponta os trechos e propõe reescritas. A aplicação fica para uma sessão que possa editar `data/`.

## 1. Resumo

- **Há cópia, e o problema está concentrado nas fontes das rodadas 1–3, que nunca tinham passado pelo anti-cópia com referências.** Rodando `ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py`, o script dá **10 erros** (8+ palavras idênticas) em **9 registros** do fichamento. Sete vêm de Prandi 2001, um de Seixas 2018 e um de Queiroga & Nascimento 2019. Um deles (exu-022.nota) é falso positivo: uma referência bibliográfica.
- A checagem própria, com 6+ palavras e comparando cada texto **só com a fonte que ele cita**, achou **86 trechos em 75 campos**, já contando os registros do fichamento-07, que entrou na `main` durante a sessão (§3.5). Separados à mão:
  - **Classe A, erro pela regra do projeto (8+ palavras): 10 campos.** É preciso reescrever (§3.1).
  - **Classe B, redação próxima demais da fonte: 31 campos.** São trechos de 7 palavras, paráfrases “coladas” que o teste de 5 palavras revelou, ou trechos de 6 palavras com fraseado característico da fonte. A reescrita é recomendada (§3.2, 3.3 e 3.5).
  - **Classe C, coincidência sem problema: 40 trechos.** Nomes próprios, listas de nomes, datas e lugares, referências bibliográficas, termos técnicos e expressões comuns (“no primeiro quartel do século XX”, “a maioria dos terreiros de Mina”). Não há o que fazer (§4).
- As **43 propostas** de reescrita foram testadas contra as mesmas fontes. Nenhuma tem 6+ palavras em comum com o original; as sobras de 5 palavras são nomes e expressões comuns (“festa do Mercadão de Madureira”, “sob o nome de Gu”).
- **Tradições e glossário:** nenhum erro. Só 1 nota de tradição (Tambor de Mina, 7 palavras) e 1 definição do glossário (candomblé, 6 palavras) entram na classe B.
- **Por que não apareceu antes:** Prandi 2001, Seixas 2018, Queiroga & Nascimento 2019, Silva 2012, Blass 2007, Bastide (capítulos do fichamento-02), Castillo 2022 etc. foram fichados antes de existir a opção `ANTICOPIA_REFS`, ou não tiveram o `.txt` incluído quando ela foi usada. As rodadas glossário/trad02/fichamento-06 passaram só com as obras lidas naquelas sessões.

## 2. Fontes cobertas e não cobertas

Os PDFs foram baixados em `/tmp/refs-pdf/` e convertidos para `.txt` em `/tmp/refs/` com `pdftotext`, **fora do repositório**. As palavras hifenizadas na quebra de linha foram juntadas antes da comparação (`religi-⏎ões` → `religiões`). Comparar com o texto sem esse ajuste dá o mesmo resultado (10 erros).

**Cobertas: 29 obras, todas no texto integral do PDF**

| Fonte (id) | Uso | Acesso nesta sessão | Págs. PDF |
|---|---|---|--:|
| Prandi 2001 (`prandi-2001-exu-diabo`) | fichamento, tradições, glossário | revistas.usp.br | 18 |
| Bastide 1961 (`bastide-1958-candomble`) | fichamento, tradições, glossário | bdor.sibi.ufrj.br (PDF com OCR) | 370 |
| Chiousse 1995 (`chiousse-1995-divins`) | fichamento, tradições, glossário | HAL (arquivo direto) | 438 |
| Silva 2012 (`silva-2012-exu-brasil`) | fichamento, tradições, glossário | periodicos.usp.br | 30 |
| Blass 2007 (`blass-2007-iemanja`) | fichamento | revistas.pucsp.br | 18 |
| Seixas 2018 (`seixas-2018-maria-iemanja`) | fichamento | revistas.pucsp.br | 14 |
| Queiroga & Nascimento 2019 (`queiroga-nascimento-2019-iemanja`) | fichamento | periodicos.ufmg.br | 21 |
| Souza 2020, *Mosaico* (`mosaico-2020-oxossi`) | fichamento | seer.pucgoias.edu.br | 7 |
| Nogueira 2017 (`ufg-2017-exu-umbanda`) | fichamento | repositorio.bc.ufg.br | 410 |
| Pinheiro 2011 (`ufpb-2011-sao-jorge`) | fichamento | repositorio.ufpb.br | 105 |
| Costa 2007 (`costa-2007-xango-pe`) | fichamento | periodicos.ufba.br | 29 |
| Cardoso Filho 2015 (`cardoso-filho-2015-iemanja`) | fichamento (resumo) | ppgsa.propesp.ufpa.br | 242 |
| Teixeira 2021 (`teixeira-2021-iemanja`) | fichamento (resumo) | maxwell.vrac.puc-rio.br | 213 |
| Castillo 2022 (`castillo-2022-ogum`) | fichamento | revistas.usp.br | 37 |
| Costa 1980 (`costa-1980-exu-umbanda`) | fichamento | periodicos.ufba.br (PDF com OCR) | 19 |
| Nascimento, Souza & Trindade 2001 (`nascimento-2001-exus`) | fichamento | repositório UFES (API DSpace) | 7 |
| Vallier 2011 (`vallier-2011-esu`) | fichamento | HAL | 38 |
| Capo Chichi 2025 (`capo-chichi-2025-shango`) | fichamento | journals.flvc.org | 12 |
| Prandi 2005, *Nas pegadas dos voduns* (`prandi-2005-pegadas-voduns`) | tradições, glossário | site do autor (USP) | 36 |
| Botão 2007 (`botao-2007-angola`) | tradições, glossário | repositorio.unesp.br | 128 |
| Tomba 2019 (`tomba-2019-bantu`) | tradições | rima.ufrrj.br | 118 |
| Oro 2012 (`oro-2012-campo`) | tradições, glossário | revistaseletronicas.pucrs.br | 10 |
| Halloy 2005 (`halloy-2005-intimite`) | tradições, glossário | HAL | 814 |
| Pitta (`pitta-2011-mitos`) | tradições | periodicos.fundaj.gov.br | 6 |
| M. Ferretti 2001 (`ferretti-m-2020-pureza`) | tradições, glossário | periodicos.sbu.unicamp.br | 20 |
| S. Ferretti 2011 (`ferretti-2011-comida`) | tradições | periodicos.pucminas.br (link do OpenAlex) | 26 |
| Toutain 2019 (`toutain-2019-santos`) | tradições, glossário | theses.hal.science | 609 |
| Argyriadis 2005 (`argyriadis-2005-ramas`) | tradições, glossário | journals.openedition.org | 32 |
| Cerqueira 2015 (`cerqueira-2015-lebabimibome`) | tradições | theses.hal.science | 377 |

Dos **877 textos** verificados depois do rebase (765 campos do fichamento, 80 do glossário, 32 das tradições), **831** têm ao menos uma fonte coberta. Antes do rebase eram 730 textos e 683 cobertos. Registros de 2ª mão são comparados com a fonte efetivamente lida (`via_source_id`).

**Não cobertas**

| Fonte | Motivo | Textos afetados |
|---|---|---|
| Oro 2008 (`oro-2008-rs`) | `seer.ufrgs.br`: conexão cortada nas 6 tentativas com curl. O PDF lido no fichamento-05 veio pela ferramenta de busca web, que não devolve o texto literal → [PENDENCIAS](PENDENCIAS.md) §1 | tradições `batuque_rs`, `candomble_ijexa` e `umbanda`; termos `linha-cruzada`, `nacao` e `umbanda`. Todos têm outras fontes cobertas, mas os trechos que vêm só de Oro 2008 ficaram sem comparação |
| Barnes 1989, Beier 1970, Brown 1989, Carneiro 1948, Pérez 2013, Ribas 2010, Silva & Silva Neto 2025, Tishken 2009, Verger 1954, Verger 1981 | obras impressas, pagas ou fora do ar, já em [PENDENCIAS](PENDENCIAS.md) §1–2. Sustentam só os 16 `pre_fichamento`, que não vão para as fichas | 16 registros `pre_fichamento` |

**Limites da checagem**

1. **Tradução não é detectada.** Chiousse, Halloy, Toutain, Argyriadis, Cerqueira e Vallier estão em francês; Capo Chichi está em inglês. A comparação por n-gramas não pega tradução literal. Fica uma conferência por pessoa bilíngue, por amostragem → [PENDENCIAS](PENDENCIAS.md) §3.
2. **OCR ruim** em Bastide 1961 e Costa 1980 (ex.: “divmdade”, “informaçiio”, “bastidc”) pode esconder coincidências. Com isso, a contagem nessas duas obras é um piso.
3. Os textos gerados (`data/orixas/*.json`, site) repetem o fichamento. Corrigir o fichamento e regenerar resolve tudo.

## 3. Trechos suspeitos e propostas de reescrita (não aplicadas)

Páginas: a página citada no registro (impressa) e, entre parênteses, a página do PDF onde o trecho aparece. O “trecho idêntico” vem normalizado (minúsculas, sem pontuação) e aqui foi restaurado com a grafia do registro.

### 3.1 Classe A — erros pela regra do projeto (8+ palavras idênticas): 10 campos em 9 registros

#### `exu-014.parafrase` — Prandi 2001, p. 50 (PDF 5) — 13 palavras

- **Trecho idêntico:** “Exu é o patrono da cópula que gera filhos e garante a continuidade”
- **Texto atual:** Exu é o patrono da cópula que gera filhos e garante a continuidade das famílias e do povo; dessa ligação com a reprodução, expressa nos símbolos fálicos, nasceu sua imagem mítica de libidinoso.
- **Proposta:** Para Prandi, Exu protege o ato sexual que produz descendência e, com ela, a sobrevivência das famílias e do povo; dessa associação com a reprodução, visível nos emblemas fálicos, veio sua fama mítica de libidinoso.
- **Obs.:** A frase de abertura reproduz o original quase inteiro.

#### `exu-031.parafrase` — Prandi 2001 (Carneiro via Prandi), p. 62 (PDF 17) — 11 palavras

- **Trecho idêntico:** “a Ogunjá, um Ogum que mora com Oxóssi e Exu e”
- **Texto atual:** Edison Carneiro registrou que não se dizia que alguém era filho de Exu, mas que tinha um carrego de Exu, obrigação vitalícia entregue a Ogunjá — um Ogum que mora com Oxóssi e Exu e come comida crua.
- **Proposta:** Edison Carneiro anotou que ninguém era chamado de filho de Exu; dizia-se que a pessoa tinha um carrego de Exu, compromisso para a vida toda confiado a Ogunjá, qualidade de Ogum que divide a morada com Oxóssi e Exu e recebe alimento cru.

#### `ogum-002.parafrase` — Prandi 2001 (Carneiro via Prandi), p. 62 (PDF 17) — 9 palavras

- **Trecho idêntico:** “Oxóssi e Exu e se alimenta de comida crua”
- **Texto atual:** Carneiro descreveu Ogunjá como um Ogum que vive junto de Oxóssi e Exu e se alimenta de comida crua.
- **Proposta:** Segundo Carneiro, citado por Prandi, Ogunjá é uma forma de Ogum assentada junto de Oxóssi e Exu e que recebe comida crua.
- **Obs.:** Mesma frase da fonte que exu-031; as propostas usam redações diferentes entre si.

#### `ogum-002.valor` — Prandi 2001 (Carneiro via Prandi), p. 62 (PDF 17) — 8 palavras

- **Trecho idêntico:** “Ogum que mora com Oxóssi e Exu e”
- **Texto atual:** Ogunjá — Ogum que mora com Oxóssi e Exu e come comida crua
- **Proposta:** Ogunjá — Ogum que tem assento junto de Oxóssi e Exu e cujas oferendas são cruas

#### `iemanja-002.parafrase` — Prandi 2001, p. 51 (PDF 6) — 9 + 8 palavras

- **Trecho idêntico:** “e passaram a compor a imagem pecaminosa de Pombagira / das Grandes Mães, inclusive Iemanjá e Oxum, foram”
- **Texto atual:** Seguindo Monique Augras, Prandi afirma que vários traços africanos das Grandes Mães, inclusive Iemanjá e Oxum, foram suavizados ou apagados no culto brasileiro e passaram a compor a imagem 'pecaminosa' de Pombagira.
- **Proposta:** Com base em Monique Augras, Prandi sustenta que muitos traços africanos das Grandes Mães — Iemanjá e Oxum entre elas — foram amenizados ou suprimidos no Brasil e acabaram transferidos para a figura de Pombagira, tida como 'pecaminosa'.
- **Obs.:** Dois trechos no mesmo campo.

#### `iemanja-036.valor` — Seixas 2018 (Verger via Seixas), p. 115 (PDF 3) — 9 palavras

- **Trecho idêntico:** “o mais poderoso dos orixás, porque preside as águas”
- **Texto atual:** o mais poderoso dos orixás, porque preside as águas (segundo Verger)
- **Proposta:** o orixá de maior poder, por reger as águas (segundo Verger)
- **Obs.:** A paráfrase (6 palavras) e a nota do mesmo registro também foram revistas abaixo.

#### `iemanja-040.parafrase` — Queiroga & Nascimento 2019 (Vallado via Q&N), PDF p. 2 — 9 + 7 palavras

- **Trecho idêntico:** “o culto original de Iemanjá também a […] ao plantio e à colheita do inhame e à”
- **Texto atual:** O culto original de Iemanjá também a liga ao plantio e à colheita do inhame e à pesca.
- **Proposta:** Em sua forma africana, o culto a Iemanjá também se relacionava com o cultivo e a colheita do inhame e com a pesca.
- **Obs.:** 89% das palavras do campo coincidem com a fonte (só “associa” → “liga” e o fim mudaram). O `valor` do mesmo registro também foi reescrito.

#### `exu-010.parafrase` — Prandi 2001, p. 49 (PDF 4) — 8 palavras

- **Trecho idêntico:** “praticamente a primeira pesquisadora no Brasil a se”
- **Texto atual:** Prandi lembra que Bastide, nos anos 1950, chamou Exu de divindade caluniada, e que Juana Elbein dos Santos foi praticamente a primeira pesquisadora no Brasil a se dedicar a recuperar seus atributos africanos, encobertos pelas reinterpretações católicas.
- **Proposta:** Prandi lembra que Bastide, nos anos 1950, chamou Exu de divindade caluniada, e que Juana Elbein dos Santos foi, na prática, a pioneira entre os pesquisadores no Brasil no esforço de resgatar os atributos africanos de Exu, encobertos pelas reinterpretações católicas.

#### `exu-033.parafrase` — Prandi 2001, pp. 62–63 (PDF 18) — 8 palavras

- **Trecho idêntico:** “as encruzilhadas e guarda a porta das casas”
- **Texto atual:** Com a dessincretização, Exu tende a voltar a ser o orixá mensageiro que detém a transformação e o movimento, vive na estrada, frequenta as encruzilhadas e guarda a porta das casas — nem santo nem demônio.
- **Proposta:** Com a dessincretização, a tendência seria Exu reassumir o papel de orixá mensageiro, que governa mudança e movimento, anda pelos caminhos, ronda as encruzilhadas e vigia a entrada das casas — sem ser santo nem demônio.
- **Obs.:** O resto da frase também segue a ordem do original (“vive na estrada, frequenta…”).

#### `exu-022.nota` — Prandi 2001, p. 55 (PDF 10) — 8 palavras

- **Trecho idêntico:** “Verger 1997, pp. 76–8; 1999, p. 132”
- **Texto atual:** Verger (1997, pp. 76–8; 1999, p. 132). Laroiê aparece como nome; verificar relação com a saudação.
- **Proposta:** Verger 1997: pp. 76–78; Verger 1999: p. 132. Laroiê aparece como nome; verificar relação com a saudação.
- **Obs.:** **Falso positivo:** é uma referência bibliográfica, não texto de Prandi. A proposta só muda a grafia para o detector não acusar. O mesmo acontece em exu-021.nota e exu-004.nota (6 palavras, só números e autor-ano), que não precisam de mudança.

### 3.2 Classe B — 7 palavras, ou 5–6 com paráfrase colada (abaixo do limite, mas redação próxima demais da fonte): 13 campos

#### `iemanja-047.parafrase` — Teixeira 2021, resumo (PDF 8) — 7 palavras

- **Trecho idêntico:** “oferendas e pedidos escritos diante da estátua”
- **Texto atual:** No Rio de Janeiro, a festa do Mercadão de Madureira (17ª edição na pesquisa) ocupa todo o mês de dezembro, com oferendas e pedidos escritos diante da estátua de Iemanjá, e se destaca por homenagear a divindade sem santos católicos associados.
- **Proposta:** No Rio de Janeiro, a festa do Mercadão de Madureira (17ª edição na pesquisa) dura o mês de dezembro inteiro: os fiéis deixam oferendas e bilhetes com pedidos junto à estátua de Iemanjá, e a festa se distingue por homenagear a divindade sem santos católicos associados.

#### `iemanja-028.parafrase` — Bastide 1961, p. 93 — 7 palavras

- **Trecho idêntico:** “há lugares privilegiados, como o Dique, Montserrat”
- **Texto atual:** Nem todo ponto da praia serve para as oferendas; há lugares privilegiados, como o Dique, Montserrat e a praia do Rio Vermelho.
- **Proposta:** Nem todo ponto da orla serve às oferendas; alguns são preferidos, como o Dique, Montserrat e a praia do Rio Vermelho.

#### `iemanja-009.valor` — Bastide 1961, p. 119, nota 79 — 7 palavras

- **Trecho idêntico:** “o filho que ela traz ao colo”
- **Texto atual:** sexta-feira (com Odé, 'o filho que ela traz ao colo')
- **Proposta:** sexta-feira (com Odé, descrito como o filho que Iemanjá carrega no colo)
- **Obs.:** Já está entre aspas (o detector também avisa). Fala de informante citada por Bastide; a proposta parafraseia para tirar a citação.

#### `exu-076.parafrase` — Nascimento et al. 2001, pp. 109–111 (PDF 4) — 7 palavras

- **Trecho idêntico:** “de exus e pombas-giras com ruas”
- **Texto atual:** Os autores registram que a ligação de exus e pombas-giras com ruas, encruzilhadas e cemitérios é quase constante nos pontos, mas ressalvam que isso não indica morada: as entidades estariam nesses lugares por afinidade ou pelo tipo de trabalho que fazem ali.
- **Proposta:** Os autores registram que, nos pontos, exus e pombas-giras aparecem quase sempre associados a ruas, encruzilhadas e cemitérios, mas ressalvam que isso não indica morada: as entidades estariam nesses lugares por afinidade ou pelo tipo de trabalho que fazem ali.

#### `ogum-036.parafrase` — Castillo 2022, pp. 7–8 — 7 palavras

- **Trecho idêntico:** “mas também de ferreiros, caçadores e de”
- **Texto atual:** Para Castillo, Ogum é invocado como caçador e guerreiro contra inimigos humanos e espirituais, mas a raiz dessa força é o domínio do trabalho com o ferro. Por isso seria patrono não só de soldados, mas também de ferreiros, caçadores e de todas as profissões que dependem de objetos de ferro.
- **Proposta:** Para Castillo, Ogum é invocado como caçador e guerreiro contra inimigos humanos e espirituais, mas a raiz dessa força é o domínio do trabalho com o ferro. Por isso seria padroeiro de soldados, ferreiros e caçadores e de qualquer ofício que use instrumentos de ferro.

#### `ogum-041.parafrase` — Castillo 2022, p. 10 — 7 palavras

- **Trecho idêntico:** “mariô, palavra iorubá usada no candomblé para”
- **Texto atual:** Castillo descreve o mariô, palavra iorubá usada no candomblé para a franja de folhas de dendezeiro desfiadas, como um dos símbolos centrais de Ogum: adorna a roupa do orixá em transe e, pendurado sobre portas e janelas dos terreiros, chama sua proteção contra espíritos e energias ruins.
- **Proposta:** Castillo descreve o mariô — termo iorubá que, no candomblé, designa a franja de folhas desfiadas do dendezeiro — como um dos símbolos centrais de Ogum: adorna a roupa do orixá em transe e, pendurado sobre portas e janelas dos terreiros, chama sua proteção contra espíritos e energias ruins.

#### `ogum-046.parafrase` — Castillo 2022, p. 24 — 7 palavras

- **Trecho idêntico:** “Ogum é cultuado com os mesmos atributos”
- **Texto atual:** Segundo Castillo, Ogum é cultuado com os mesmos atributos, sob o nome de Gu, pelos povos chamados jejes no Brasil. No Daomé, Gu ganhou importância por sua ligação com ferreiros e ofícios do ferro e, na cosmologia fon, integra um grupo de voduns tidos como de origem nagô.
- **Proposta:** Segundo Castillo, os povos chamados jejes no Brasil cultuam Ogum, com atributos iguais, sob o nome de Gu. No Daomé, Gu ganhou importância por sua ligação com ferreiros e ofícios do ferro e, na cosmologia fon, integra um grupo de voduns tidos como de origem nagô.

#### `ogum-049.parafrase` — Castillo 2022, p. 27 — 7 palavras

- **Trecho idêntico:** “nos reinos vizinhos de Ijexá e Ondo”
- **Texto atual:** Castillo afirma que Ogum está entre os poucos orixás cultuados historicamente em todas as regiões iorubás, mas que seus oríkì e os versos de Ifá apontam a origem do culto em Iré, no reino de Ekiti, no leste; o culto também seria especialmente forte nos reinos vizinhos de Ijexá e Ondo.
- **Proposta:** Castillo afirma que Ogum está entre os poucos orixás cultuados historicamente em todas as regiões iorubás, mas que seus oríkì e os versos de Ifá apontam a origem do culto em Iré, no reino de Ekiti, no leste; o culto teria força particular também em Ijexá e Ondo, reinos próximos.

#### `ogum-052.parafrase` — Castillo 2022, pp. 7, 26 — 7 + 6 + 6 palavras

- **Trecho idêntico:** “a única qualidade de Ogum de que / literatura etnográfica sobre o candomblé jeje / o poder de afastar o mal”
- **Texto atual:** Castillo afirma que a única qualidade de Ogum de que a literatura etnográfica sobre o candomblé jeje dá notícia é Ogum Xoroquê, que no Jeje divide com Legba o poder de afastar o mal.
- **Proposta:** Segundo Castillo, Ogum Xoroquê é a única qualidade de Ogum mencionada nos estudos etnográficos sobre o candomblé jeje; ali, ele compartilha com Legba a função de afastar o mal.
- **Obs.:** 56% das palavras do campo vêm da fonte em trechos de 5+.

#### `tradicoes/tambor_de_mina.nota` — M. Ferretti 2001, p. 77 (PDF 1) — 7 palavras

- **Trecho idêntico:** “o modelo da Casa de Nagô e”
- **Texto atual:** Bastide descreve a Casa das Minas como o grupo dominante em São Luís; M. Ferretti (p. 77) registra que a maioria dos terreiros reproduz o modelo da Casa de Nagô, e S. Ferretti (2011, p. 247) que as duas casas matrizes perderam participantes, mas mantêm prestígio.
- **Proposta:** Bastide descreve a Casa das Minas como o grupo dominante em São Luís; M. Ferretti (p. 77) registra que a maior parte dos terreiros segue o padrão da Casa de Nagô, e S. Ferretti (2011, p. 247) que as duas casas matrizes perderam participantes, mas mantêm prestígio.
- **Obs.:** Proposta só para a 1ª frase; o resto da nota não muda.

#### `exu-007.parafrase` — Prandi 2001 (Baudin via Prandi), pp. 48–49 (PDF 3) — 7 palavras

- **Trecho idêntico:** “azeite de dendê e sangue de galinha”
- **Texto atual:** Baudin descreve a imagem de Exu colocada diante das casas, praças e caminhos: figura humana de barro, sentada, com cabeça grande, penas como cabelo e búzios como olhos e dentes, que recebe azeite de dendê e sangue de galinha; ao lado ficam cabos de enxada e bastões nodosos; os abutres seriam seus mensageiros.
- **Proposta:** Baudin descreve a imagem de Exu colocada diante das casas, praças e caminhos: figura humana de barro, sentada, com cabeça grande, penas como cabelo e búzios como olhos e dentes, regada com dendê e sangue de galinha; ao lado ficam cabos de enxada e bastões nodosos; os abutres seriam seus mensageiros.
- **Obs.:** Sintagma comum de oferenda; troca opcional.

#### `exu-052.parafrase` — Silva 2012, p. 1087 — 7 palavras

- **Trecho idêntico:** “de bebidas alcoólicas e azeite de dendê”
- **Texto atual:** Na África Ocidental, Exu recebe sangue de bodes, galos pretos, cães e porcos, além de bebidas alcoólicas e azeite de dendê.
- **Proposta:** Na África Ocidental, Exu recebe o sangue de bodes, cães, porcos e galos pretos, além de libações de bebida alcoólica e de dendê.
- **Obs.:** Junto com a lista de animais (6 palavras, também no `valor`), 62% do campo coincide. Lista de animais é dado factual; a proposta muda só a ordem e o fim.

#### `exu-012.valor` — Prandi 2001, p. 50 — 5 palavras

- **Trecho idêntico:** “deve ser propiciado sempre que (+ “orixá recebe oferenda”)”
- **Texto atual:** deve ser propiciado sempre que outro orixá recebe oferenda
- **Proposta:** recebe sua parte toda vez que outro orixá é alimentado
- **Obs.:** Achado pelo teste de 5 palavras: são 8 palavras da fonte com uma única troca (“algum” → “outro”).

### 3.3 Classe B — 6 palavras com redação característica da fonte: 16 campos (reescrita recomendada, prioridade menor)

#### `iemanja-036.parafrase` — Seixas 2018, p. 115 — 6 palavras

- **Trecho idêntico:** “o mais poderoso dos orixás, porque”
- **Texto atual:** Segundo Verger, Iemanjá seria o mais poderoso dos orixás, porque governa as águas, sem as quais nada se faz.
- **Proposta:** Segundo Verger, Iemanjá teria mais poder que qualquer outro orixá, pois rege as águas, indispensáveis a qualquer ação.

#### `iemanja-036.nota` — Seixas 2018, p. 115 — 6 palavras

- **Trecho idêntico:** “divindade das águas doces e salgadas”
- **Texto atual:** CORRIGE pré-registro: a frase 'divindade das águas doces e salgadas' é da autora Seixas, não de Verger.
- **Proposta:** CORRIGE pré-registro: a expressão que liga Iemanjá às águas doces e às salgadas é de Seixas, não de Verger.
- **Obs.:** Citação curta entre aspas (o detector já avisava).

#### `exu-005.parafrase` — Prandi 2001 (Bouche via Prandi), p. 48 — 6 palavras

- **Trecho idêntico:** “aquele que se apodera de nós”
- **Texto atual:** O pastor Bowen (1857) afirmou que em iorubá o diabo se chama Exu e explicou o nome Elegbara como 'o poderoso'; o abade Bouche (1885) disse que os africanos chamavam Satã de Elegbara, 'aquele que se apodera de nós'.
- **Proposta:** O pastor Bowen (1857) afirmou que em iorubá o diabo se chama Exu e explicou o nome Elegbara como 'o poderoso'; o abade Bouche (1885) disse que os africanos chamavam Satã de Elegbara, nome que ele traduzia como o que toma posse das pessoas.
- **Obs.:** Citação curta entre aspas (o detector já avisava). Pode ficar como citação; a proposta é para quem preferir parafrasear.

#### `exu-057.valor` — Silva 2012, p. 1089 — 6 palavras

- **Trecho idêntico:** “menos de uma dezena de avatares”
- **Texto atual:** menos de uma dezena de avatares no candomblé (Tiriri, Lonã, Marabô...); legiões na Umbanda
- **Proposta:** menos de dez avatares no candomblé (Tiriri, Lonã, Marabô...); legiões na Umbanda
- **Obs.:** A paráfrase do mesmo registro já diz “menos de dez”.

#### `ogum-038.parafrase` — Castillo 2022, pp. 8, 22 — 6 palavras

- **Trecho idêntico:** “padroeiro de uma família de lavradores”
- **Texto atual:** A autora argumenta que africanos libertos que assentaram orixás em seus pomares tinham interesse direto nas safras, e que até cativos cultivavam hortas. O caso do Candeal, onde Ogum foi padroeiro de uma família de lavradores por mais de um século, sugere que a mudança apontada por Verger ainda não tinha ocorrido naquela época.
- **Proposta:** A autora argumenta que africanos libertos que assentaram orixás em seus pomares tinham interesse direto nas safras, e que até cativos cultivavam hortas. O caso do Candeal, onde Ogum protegeu uma família de lavradores durante mais de um século, sugere que a mudança apontada por Verger ainda não tinha ocorrido naquela época.

#### `glossario/candomble.definicao` — Bastide 1961, p. 354 (glossário) — 6 palavras

- **Trecho idêntico:** “qualquer dança ou festa de negros”
- **Texto atual:** Religião afro-brasileira de culto aos orixás, voduns e inquices, organizada em nações. Bastide dá três sentidos à palavra: o lugar das festas religiosas africanas, o conjunto dessas cerimônias e, no sul do país, qualquer dança ou festa de negros.
- **Proposta:** Religião afro-brasileira de culto aos orixás, voduns e inquices, organizada em nações. Bastide dá três sentidos à palavra: o lugar das festas religiosas africanas, o conjunto dessas cerimônias e, no sul do país, toda dança ou festa da população negra.
- **Obs.:** Definição de glossário de Bastide; reproduzida sem aspas.

#### `exu-063.parafrase` — Nogueira 2017, pp. 384–385 — 6 palavras

- **Trecho idêntico:** “a primeira codificação umbandista, em 1933”
- **Texto atual:** Nogueira propõe que o Exu entendido como espírito de morto se formou nas primeiras décadas do século XX, na troca entre os terreiros baianos, de onde vinham os orixás, e as macumbas do Rio, onde circulavam ideias espíritas. Quando Leal de Souza publicou a primeira codificação umbandista, em 1933, Exu já aparecia como entidade, ligado a uma 'linha negra' que o autor separava da Umbanda; mesmo assim, em muitos terreiros cariocas Exu era cultuado junto de pretos-velhos e caboclos.
- **Proposta:** Nogueira propõe que o Exu entendido como espírito de morto se formou nas primeiras décadas do século XX, na troca entre os terreiros baianos, de onde vinham os orixás, e as macumbas do Rio, onde circulavam ideias espíritas. Quando Leal de Souza publicou, em 1933, o primeiro texto a codificar a Umbanda, Exu já aparecia como entidade, ligado a uma 'linha negra' que o autor separava da Umbanda; mesmo assim, em muitos terreiros cariocas Exu era cultuado junto de pretos-velhos e caboclos.

#### `exu-072.parafrase` — Costa 1980, PDF pp. 15–16 (PDF 12) — 6 palavras

- **Trecho idêntico:** “em vida mulher de sete exus”
- **Texto atual:** Costa apresenta a Pomba-Gira como o exu feminino habitual nas sessões de exus e, citando Kochmeyer, aproxima o nome do correspondente de Exu na nação Angola. Na versão corrente entre os pais de santo ouvidos, ela teria sido em vida mulher de sete exus e é procurada sobretudo para questões amorosas e sexuais.
- **Proposta:** Costa apresenta a Pomba-Gira como o exu feminino habitual nas sessões de exus e, citando Kochmeyer, aproxima o nome do correspondente de Exu na nação Angola. Na versão corrente entre os pais de santo ouvidos, ela teria sido, quando viva, companheira de sete exus e é procurada sobretudo para questões amorosas e sexuais.

#### `ogum-047.parafrase` — Castillo 2022 (Barnes via Castillo), pp. 24–25 — 6 palavras

- **Trecho idêntico:** “na forma de uma espada cerimonial”
- **Texto atual:** Castillo resume um mito de criação daomeano relatado por Barnes e Ben-Amos: o Criador teria vindo à Terra segurando Gu na forma de uma espada cerimonial e, com ela, abriu o mato e ensinou as pessoas a erguer casas, plantar e trabalhar o metal. A autora liga o mito às miniaturas de enxadas e ferramentas nos altares de Gu.
- **Proposta:** Castillo resume um mito de criação daomeano relatado por Barnes e Ben-Amos: o Criador teria vindo à Terra segurando Gu em forma de espada de cerimônia e, com ela, abriu o mato e ensinou as pessoas a erguer casas, plantar e trabalhar o metal. A autora liga o mito às miniaturas de enxadas e ferramentas nos altares de Gu.

#### `xango-012.parafrase` — Bastide 1961, p. 107 — 6 palavras

- **Trecho idêntico:** “um dos equivalentes católicos de Xangô”
- **Texto atual:** São Jerônimo, festejado em 30 de setembro, é um dos equivalentes católicos de Xangô; no Gantois, a cerimônia de encerramento do ano (baiani) é feita o mais perto possível dessa data.
- **Proposta:** São Jerônimo, festejado em 30 de setembro, é um dos santos católicos associados a Xangô; no Gantois, a cerimônia de encerramento do ano (baiani) é feita o mais perto possível dessa data.

#### `oxossi-009.parafrase` — Bastide 1961, p. 123 — 6 palavras

- **Trecho idêntico:** “é o patrono dos caçadores e”
- **Texto atual:** Oxóssi é o patrono dos caçadores e, com Ogum, tem seus objetos sagrados assentados fora do peji, ao ar livre.
- **Proposta:** Oxóssi protege os caçadores e, com Ogum, tem seus objetos sagrados assentados fora do peji, ao ar livre.

#### `exu-050.parafrase` — Silva 2012, p. 1087 — 6 palavras

- **Trecho idêntico:** “ou Exu é um deus mensageiro”
- **Texto atual:** Entre fons e iorubás, Legba ou Exu é um deus mensageiro, ligado à fertilidade e ao dinamismo, que tomou parte na criação do mundo; guarda a ordem e, por ser trickster, também a desordem, e é saudado sempre em primeiro lugar.
- **Proposta:** Entre fons e iorubás, Legba ou Exu é um mensageiro divino, ligado à fertilidade e ao dinamismo, que tomou parte na criação do mundo; guarda a ordem e, por ser trickster, também a desordem, e é saudado sempre em primeiro lugar.

#### `exu-051.parafrase` — Silva 2012, p. 1087 — 6 palavras

- **Trecho idêntico:** “de terra em forma de cabeça”
- **Texto atual:** Na África Ocidental, Exu é cultuado numa pedra de laterita, num monte de terra em forma de cabeça com grande falo, ou numa estátua com búzios; leva um cajado fálico com que se desloca.
- **Proposta:** Na África Ocidental, Exu é cultuado numa pedra de laterita, num monte de terra modelado como cabeça e dotado de grande falo, ou numa estátua com búzios; leva um cajado fálico com que se desloca.

#### `exu-060.parafrase` — Silva 2012, p. 1100 — 6 palavras

- **Trecho idêntico:** “por meio do bastão que carrega”
- **Texto atual:** Segundo o mito, Exu circula pelo tempo e pelo espaço, nas quatro direções, por meio do bastão que carrega; por isso a encruzilhada é lugar preferido de suas oferendas.
- **Proposta:** Segundo o mito, Exu circula pelo tempo e pelo espaço, nas quatro direções, graças ao bastão que leva; por isso a encruzilhada é lugar preferido de suas oferendas.

#### `exu-019.parafrase` — Prandi 2001, p. 54 — 6 palavras

- **Trecho idêntico:** “com capa preta e vermelha e”
- **Texto atual:** Incorporado na Umbanda/quimbanda, Exu aparece com capa preta e vermelha e tridente, imita cascos, gargalha, bebe e fuma — muito diferente do mensageiro brincalhão dos iorubás.
- **Proposta:** Incorporado na Umbanda/quimbanda, Exu aparece de capa vermelha e preta e tridente, imita cascos, gargalha, bebe e fuma — muito diferente do mensageiro brincalhão dos iorubás.

#### `iemanja-030.parafrase` — Bastide 1961, p. 92 — 6 palavras

- **Trecho idêntico:** “água salgada e da água doce”
- **Texto atual:** Bastide chama Iemanjá e Oxum de deusas da água salgada e da água doce, ambas vaidosas, o que explica o tipo de presente que recebem.
- **Proposta:** Bastide chama Iemanjá e Oxum de deusas do mar e das águas doces, ambas vaidosas, o que explica o tipo de presente que recebem.

### 3.5 Adendo: registros novos do fichamento-07 e da tradição Efon (auditados depois do rebase)

Durante esta sessão, o fichamento-07 e a sessão `revisao` entraram na `main`. Por isso a auditoria foi refeita sobre os dados atualizados: **877 textos** (765 do fichamento, 80 do glossário, 32 das tradições), 831 com fonte coberta. Resultado: **nenhum erro novo** (os mesmos 10 do §3.1) e **12 trechos novos de 6–7 palavras**. Dez são classe C: nomes (“Abê, Iemanjá e Nossa Senhora da Conceição”, “pela africana liberta Maria Bernarda da Paixão”, “a nação Efon em Duque de Caxias”), epítetos comuns (“o orixá do ferro e da guerra”, “representa o raio e o trovão”) e expressões correntes (“a correspondência entre vodum e orixá”, “do panteão da Casa das Minas”). Os outros dois são classe B:

#### `exu-093.valor` — Prandi 2005, versão do autor, pp. 13–14 (PDF 14) — 7 palavras

- **Trecho idêntico:** “assentado para a casa e para muitos” (mais “propiciado nas grandes obrigações”, 4 palavras na mesma ordem da fonte)
- **Texto atual:** Legbara assentado para a casa e para muitos filhos, com quarto próprio, e propiciado nas grandes obrigações
- **Proposta:** Legbara com assentamento coletivo, da casa e de vários filhos, em quarto próprio, e cultuado nas obrigações maiores

#### `exu-092.parafrase` — Prandi 2005, versão do autor, p. 8 — 6 palavras

- **Trecho idêntico:** “mal; não é aceito como mensageiro”
- **Texto atual:** (1ª frase) Segundo o texto, na Casa das Minas Legba fica sem culto organizado e é associado a Satanás, ao mal; não é aceito como mensageiro, tarefa que lá cabe aos voduns jovens chamados toqüéns.
- **Proposta:** (1ª frase) Segundo o texto, na Casa das Minas Legba fica sem culto organizado e é associado a Satanás, ao mal; não exerce a função de mensageiro, que lá cabe aos voduns jovens chamados toqüéns. (O resto do campo não muda.)

As duas propostas têm 0 sequência de 5+ palavras em comum com a fonte.

### 3.4 Propostas complementares (mesmo registro dos itens acima)

- `iemanja-040.valor` (5 palavras da fonte, “colheita do inhame e à”): **na origem africana, ligado ao cultivo do inhame e à pesca**
- `exu-052.valor` (lista de animais em 6 palavras): **bodes, cães, porcos e galos pretos (sacrifício na África Ocidental)**

## 4. Classe C — coincidências sem problema (40 trechos)

São os trechos marcados com **C** no apêndice. Nenhum pede reescrita:

- **Nomes, listas de nomes, eventos, datas e lugares:** exu-023.valor (nomes de Exu em cultos fon e banto), exu-070.valor (título do mito “filho caçula do rei do Congo”), oxossi-026.valor (epíteto “caçador de uma flecha só”), iemanja-031 (2 de fevereiro, Dique do Tororó), iemanja-033 (Colônia de pescadores do Rio Vermelho), iemanja-035 (escultura de Manoel do Bonfim), iemanja-047.valor (nome da festa).
- **Referências bibliográficas:** exu-004.nota, exu-021.nota (autor, ano e páginas).
- **Dito ou termo corrente:** exu-012.parafrase (“Exu não trabalha sem pagamento”), exu-034 e exu-062 (“nos terreiros de Umbanda e Quimbanda”), ogum-031 (cores), ogum-050 (“no candomblé ketu/nagô é comum”), ogum-006 (duas expressões comuns), ogum-048, iemanja-011, exu-002.
- **Registros do fichamento-07 e tradição `candomble_efon`:** os 10 trechos listados no §3.5.
- **Tradições e glossário:** expressões comuns como “no primeiro quartel do século XX” (umbanda), “a maioria dos terreiros de Mina” (tambor_de_mina; aparece nas duas obras dos Ferretti), “numa mistura de kimbundu e kikongo”, “como o bumba-meu-boi”, “em São Paulo e no Rio”, “em todos os terreiros de Mina” (abatá).

## 5. Recomendações

1. **(P1) Aplicar as propostas da classe A** numa sessão que possa editar `data/fichamento/` (exu, iemanja, ogum), regenerar as fichas e rodar `ANTICOPIA_REFS=… python3 scripts/anticopia.py` até zerar. Na mesma sessão, aplicar as da classe B. As 43 propostas estão neste relatório.
2. **Ajustar o detector:** (a) juntar a hifenização de quebra de linha ao ler as referências; (b) ignorar n-gramas formados sobretudo por números e autor-ano (falso positivo de exu-022.nota); (c) acrescentar um aviso para **6–7 palavras idênticas à fonte citada** no registro, que é onde estão as paráfrases coladas desta auditoria.
3. **Manter o `.txt` de toda obra lida** junto da sessão e rodar o anti-cópia com referências **antes** do commit, como já manda a decisão do ESTADO. A pasta `/tmp/refs` some com o contêiner. Fica a sugestão de o autor guardar uma cópia local fora do repo.
4. **Conferência de tradução** (francês/inglês) por pessoa bilíngue, por amostragem: ver limite 1 do §2.

## Apêndice — os 86 trechos de 6+ palavras (dados de depois do rebase)

Classe: **A** = erro (8+); **A\*** = falso positivo do detector; **B** = reescrita recomendada; **C** = coincidência sem problema.

| # | Campo | Fonte | Pág. citada no registro | Pág. do PDF | Palavras | Trecho idêntico (normalizado) | Classe |
|--:|---|---|---|--:|--:|---|:-:|
| 1 | `exu-014.parafrase` | `prandi-2001-exu-diabo` | pp. 50–51 | 5 | 13 | exu é o patrono da cópula que gera filhos e garante a continuidade | A |
| 2 | `exu-031.parafrase` | `prandi-2001-exu-diabo` | p. 62 | 17 | 11 | a ogunjá um ogum que mora com oxóssi e exu e | A |
| 3 | `iemanja-002.parafrase` | `prandi-2001-exu-diabo` | p. 51 | 6 | 9 | e passaram a compor a imagem pecaminosa de pombagira | A |
| 4 | `iemanja-036.valor` | `seixas-2018-maria-iemanja` | p. 115 (Seixas); Verger, Notas (Edusp 2000), p. 293 | 3 | 9 | o mais poderoso dos orixás porque preside as águas | A |
| 5 | `iemanja-040.parafrase` | `queiroga-nascimento-2019-iemanja` | PDF p. 2 | 2 | 9 | ao plantio e à colheita do inhame e à | A |
| 6 | `ogum-002.parafrase` | `prandi-2001-exu-diabo` | p. 62 | 17 | 9 | oxóssi e exu e se alimenta de comida crua | A |
| 7 | `exu-010.parafrase` | `prandi-2001-exu-diabo` | p. 49 | 4 | 8 | praticamente a primeira pesquisadora no brasil a se | A |
| 8 | `exu-022.nota` | `prandi-2001-exu-diabo` | p. 55 | 10 | 8 | verger 1997 pp 76 8 1999 p 132 | A* |
| 9 | `exu-033.parafrase` | `prandi-2001-exu-diabo` | pp. 62–63 | 18 | 8 | as encruzilhadas e guarda a porta das casas | A |
| 10 | `iemanja-002.parafrase` | `prandi-2001-exu-diabo` | p. 51 | 6 | 8 | das grandes mães inclusive iemanjá e oxum foram | A |
| 11 | `ogum-002.valor` | `prandi-2001-exu-diabo` | p. 62 | 17 | 8 | ogum que mora com oxóssi e exu e | A |
| 12 | `exu-007.parafrase` | `prandi-2001-exu-diabo` | pp. 48–49 | 3 | 7 | azeite de dendê e sangue de galinha | B |
| 13 | `exu-023.valor` | `prandi-2001-exu-diabo` | p. 55 | 10 | 7 | tiriri jelebara jiguidi mavambo emberequetê sinza muzila | C |
| 14 | `exu-052.parafrase` | `silva-2012-exu-brasil` | p. 1087 | 3 | 7 | de bebidas alcoólicas e azeite de dendê | B |
| 15 | `exu-076.parafrase` | `nascimento-2001-exus` | pp. 109–111 | 4 | 7 | de exus e pombas giras com ruas | B |
| 16 | `exu-093.valor` | `prandi-2005-pegadas-voduns` | versão do autor, pp. 13–14 | 14 | 7 | assentado para a casa e para muitos | B |
| 17 | `iemanja-009.valor` | `bastide-1958-candomble` | ed. pt 1961, p. 119, nota 79 | 118 | 7 | o filho que ela traz ao colo | B |
| 18 | `iemanja-028.parafrase` | `bastide-1958-candomble` | ed. pt 1961, p. 93 | 92 | 7 | há lugares privilegiados como o dique montserrat | B |
| 19 | `iemanja-031.parafrase` | `blass-2007-iemanja` | PDF p. 6 | 6 | 7 | 2 de fevereiro no dique do tororó | C |
| 20 | `iemanja-040.parafrase` | `queiroga-nascimento-2019-iemanja` | PDF p. 2 | 2 | 7 | o culto original de iemanjá também a | A |
| 21 | `iemanja-047.parafrase` | `teixeira-2021-iemanja` | Resumo | 8 | 7 | oferendas e pedidos escritos diante da estátua | B |
| 22 | `iemanja-047.valor` | `teixeira-2021-iemanja` | Resumo | 17 | 7 | festa de iemanjá no mercadão de madureira | C |
| 23 | `iemanja-057.parafrase` | `prandi-2005-pegadas-voduns` | versão do autor, pp. 14, 25 (Quadro 1) | 14 | 7 | abê iemanjá e nossa senhora da conceição | C |
| 24 | `ogum-036.parafrase` | `castillo-2022-ogum` | pp. 7–8 | 8 | 7 | mas também de ferreiros caçadores e de | B |
| 25 | `ogum-041.parafrase` | `castillo-2022-ogum` | pp. 10, 20 | 10 | 7 | mariô palavra iorubá usada no candomblé para | B |
| 26 | `ogum-046.parafrase` | `castillo-2022-ogum` | pp. 24–25 | 24 | 7 | ogum é cultuado com os mesmos atributos | B |
| 27 | `ogum-049.parafrase` | `castillo-2022-ogum` | pp. 26–27 | 27 | 7 | nos reinos vizinhos de ijexá e ondo | B |
| 28 | `ogum-052.parafrase` | `castillo-2022-ogum` | pp. 7, 26 | 26 | 7 | a única qualidade de ogum de que | B |
| 29 | `ogum-057.parafrase` | `pitta-2011-mitos` | p. 263 | 1 | 7 | o orixá do ferro e da guerra | C |
| 30 | `ogum-062.parafrase` | `prandi-2005-pegadas-voduns` | versão do autor, p. 25 (Quadro 1) | 14 | 7 | na casa de pai francelino os voduns | C |
| 31 | `tradicoes/candomble_efon.descricao` | `castillo-2022-ogum` | p. 28 (nota 54); p. 23 | 28 | 7 | pela africana liberta maria bernarda da paixão | C |
| 32 | `tradicoes/candomble_efon.nota` | `castillo-2022-ogum` | p. 28 (nota 54); p. 23 | 34 | 7 | a nação efon em duque de caxias | C |
| 33 | `tradicoes/tambor_de_mina.nota` | `ferretti-m-2020-pureza` | pp. 76–78 (edição de 2001) | 1 | 7 | o modelo da casa de nagô e | B |
| 34 | `exu-002.parafrase` | `prandi-2001-exu-diabo` | p. 47 | 2 | 6 | que o identifiquem com o diabo | C |
| 35 | `exu-004.nota` | `prandi-2001-exu-diabo` | p. 48 | 3 | 6 | duncan 1847 v i p 114 | C |
| 36 | `exu-005.parafrase` | `prandi-2001-exu-diabo` | p. 48 | 3 | 6 | aquele que se apodera de nós | B |
| 37 | `exu-012.parafrase` | `prandi-2001-exu-diabo` | p. 50 | 5 | 6 | que exu não trabalha sem pagamento | C |
| 38 | `exu-019.parafrase` | `prandi-2001-exu-diabo` | p. 54 | 9 | 6 | com capa preta e vermelha e | B |
| 39 | `exu-021.nota` | `prandi-2001-exu-diabo` | p. 55 | 10 | 6 | ferreira 2000 pp 19 21 também | C |
| 40 | `exu-034.parafrase` | `ufg-2017-exu-umbanda` | p. 9 (resumo); pp. 196, 385 | 9 | 6 | nos terreiros de umbanda e quimbanda | C |
| 41 | `exu-050.parafrase` | `silva-2012-exu-brasil` | p. 1087 | 3 | 6 | ou exu é um deus mensageiro | B |
| 42 | `exu-051.parafrase` | `silva-2012-exu-brasil` | p. 1087 | 3 | 6 | de terra em forma de cabeça | B |
| 43 | `exu-052.parafrase` | `silva-2012-exu-brasil` | p. 1087 | 3 | 6 | bodes galos pretos cães e porcos | B |
| 44 | `exu-052.valor` | `silva-2012-exu-brasil` | p. 1087 | 3 | 6 | bodes galos pretos cães e porcos | B |
| 45 | `exu-057.valor` | `silva-2012-exu-brasil` | p. 1089 | 5 | 6 | menos de uma dezena de avatares | B |
| 46 | `exu-060.parafrase` | `silva-2012-exu-brasil` | p. 1100 | 16 | 6 | por meio do bastão que carrega | B |
| 47 | `exu-062.parafrase` | `ufg-2017-exu-umbanda` | p. 22, nota 5 | 9 | 6 | nos terreiros de umbanda e quimbanda | C |
| 48 | `exu-063.parafrase` | `ufg-2017-exu-umbanda` | pp. 384–385 | 384 | 6 | a primeira codificação umbandista em 1933 | B |
| 49 | `exu-070.valor` | `costa-1980-exu-umbanda` | PDF pp. 5, 10–11 | 8 | 6 | filho caçula do rei do congo | C |
| 50 | `exu-072.parafrase` | `costa-1980-exu-umbanda` | PDF pp. 15–16 | 12 | 6 | em vida mulher de sete exus | B |
| 51 | `exu-092.parafrase` | `prandi-2005-pegadas-voduns` | versão do autor, p. 8 (panteão da Casa das Minas segundo S. Ferretti 1989, 1996) | 8 | 6 | mal não é aceito como mensageiro | B |
| 52 | `glossario/abata.definicao` | `ferretti-m-2020-pureza` | pp. 78–79 (edição de 2001) | 5 | 6 | em todos os terreiros de mina | C |
| 53 | `glossario/candomble.definicao` | `bastide-1958-candomble` | pp. 17, 354 (glossário) | 339 | 6 | qualquer dança ou festa de negros | B |
| 54 | `iemanja-011.parafrase` | `bastide-1958-candomble` | ed. pt 1961, p. 124 | 123 | 6 | é também a do presente de | C |
| 55 | `iemanja-030.parafrase` | `bastide-1958-candomble` | ed. pt 1961, p. 92 | 91 | 6 | água salgada e da água doce | B |
| 56 | `iemanja-033.parafrase` | `blass-2007-iemanja` | PDF p. 1 | 6 | 6 | pescadores da colônia do rio vermelho | C |
| 57 | `iemanja-035.parafrase` | `blass-2007-iemanja` | PDF p. 4 | 8 | 6 | no pátio da casa de iemanjá | C |
| 58 | `iemanja-035.parafrase` | `blass-2007-iemanja` | PDF p. 4 | 4 | 6 | uma escultura de manoel do bonfim | C |
| 59 | `iemanja-036.nota` | `seixas-2018-maria-iemanja` | p. 115 (Seixas); Verger, Notas (Edusp 2000), p. 293 | 3 | 6 | divindade das águas doces e salgadas | B |
| 60 | `iemanja-036.parafrase` | `seixas-2018-maria-iemanja` | p. 115 (Seixas); Verger, Notas (Edusp 2000), p. 293 | 3 | 6 | o mais poderoso dos orixás porque | B |
| 61 | `ogum-006.parafrase` | `ufpb-2011-sao-jorge` | pp. 34, 36, 83 | 36 | 6 | entre ogum e são jorge é | C |
| 62 | `ogum-006.parafrase` | `ufpb-2011-sao-jorge` | pp. 34, 36, 83 | 36 | 6 | ao lado de santos e orixás | C |
| 63 | `ogum-031.parafrase` | `ufpb-2011-sao-jorge` | pp. 69–70 | 72 | 6 | o azul marinho e o verde | C |
| 64 | `ogum-038.parafrase` | `castillo-2022-ogum` | pp. 8, 22 | 22 | 6 | padroeiro de uma família de lavradores | B |
| 65 | `ogum-047.parafrase` | `castillo-2022-ogum` | pp. 24–25 (Barnes & Ben-Amos, ed. 1997, pp. 53–54) | 25 | 6 | na forma de uma espada cerimonial | B |
| 66 | `ogum-048.parafrase` | `castillo-2022-ogum` | p. 25 (Cosentino, ed. 1997, pp. 298–301, 312) | 25 | 6 | que o culto a gu já | C |
| 67 | `ogum-050.parafrase` | `castillo-2022-ogum` | p. 27 | 27 | 6 | no candomblé ketu nagô é comum | C |
| 68 | `ogum-052.parafrase` | `castillo-2022-ogum` | pp. 7, 26 | 26 | 6 | literatura etnográfica sobre o candomblé jeje | B |
| 69 | `ogum-052.parafrase` | `castillo-2022-ogum` | pp. 7, 26 | 7 | 6 | o poder de afastar o mal | B |
| 70 | `ogum-057.valor` | `pitta-2011-mitos` | p. 263 | 1 | 6 | orixá do ferro e da guerra | C |
| 71 | `ogum-062.nota` | `prandi-2005-pegadas-voduns` | versão do autor, p. 25 (Quadro 1) | 14 | 6 | a correspondência entre vodum e orixá | C |
| 72 | `oxossi-009.parafrase` | `bastide-1958-candomble` | ed. pt 1961, p. 123 | 122 | 6 | é o patrono dos caçadores e | B |
| 73 | `oxossi-026.valor` | `mosaico-2020-oxossi` | p. 58–59 (Souza); Verger, Lendas africanas dos orixás, 4ª ed. 1997 | 2 | 6 | o caçador de uma flecha só | C |
| 74 | `tradicoes/candomble_angola.descricao` | `botao-2007-angola` | p. 15 e nota 2 | 37 | 6 | numa mistura de kimbundu e kikongo | C |
| 75 | `tradicoes/candomble_angola.nota` | `botao-2007-angola` | p. 15 e nota 2 | 82 | 6 | em são paulo e no rio | C |
| 76 | `tradicoes/candomble_angola.nota` | `prandi-2005-pegadas-voduns` | versão do autor, p. 1 | 2 | 6 | pelos orixás nagôs nos candomblés bantos | C |
| 77 | `tradicoes/candomble_efon.descricao` | `castillo-2022-ogum` | p. 28 (nota 54); p. 23 | 28 | 6 | um antigo terreiro de nação efon | C |
| 78 | `tradicoes/candomble_jeje.descricao` | `prandi-2005-pegadas-voduns` | versão do autor, p. 1 | 2 | 6 | recôncavo a religião dos voduns é | C |
| 79 | `tradicoes/tambor_de_mina.descricao` | `prandi-2005-pegadas-voduns` | versão do autor, pp. 1–2 | 3 | 6 | como o bumba meu boi e | C |
| 80 | `tradicoes/tambor_de_mina.descricao` | `ferretti-m-2020-pureza` | pp. 76–78 (edição de 2001) | 1 | 6 | a maioria dos terreiros de mina | C |
| 81 | `tradicoes/tambor_de_mina.descricao` | `ferretti-2011-comida` | pp. 245, 247–248, 264–265 | 1 | 6 | a maioria dos terreiros de mina | C |
| 82 | `tradicoes/umbanda.descricao` | `prandi-2001-exu-diabo` | pp. 52–53 | 7 | 6 | no primeiro quartel do século xx | C |
| 83 | `tradicoes/umbanda.nota` | `prandi-2001-exu-diabo` | pp. 52–53 | 7 | 6 | no primeiro quartel do século xx | C |
| 84 | `xango-012.parafrase` | `bastide-1958-candomble` | ed. pt 1961, p. 107 | 106 | 6 | um dos equivalentes católicos de xangô | B |
| 85 | `xango-049.nota` | `prandi-2005-pegadas-voduns` | versão do autor, p. 8 (panteão da Casa das Minas segundo S. Ferretti 1989, 1996) | 7 | 6 | representa o raio e o trovão | C |
| 86 | `xango-049.parafrase` | `prandi-2005-pegadas-voduns` | versão do autor, p. 8 (panteão da Casa das Minas segundo S. Ferretti 1989, 1996) | 5 | 6 | do panteão da casa das minas | C |
