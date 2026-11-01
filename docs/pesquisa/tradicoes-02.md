# Tradições 02: fontes P2 da varredura 3

Sessão `trad02` (2026-11-01). Tarefa: dar fonte às tradições ainda `rascunho_sem_fonte` e reforçar as demais com as fontes abertas P2 do [relatório da varredura 3](relatorio-varredura-03.md). Só foram editados `data/tradicoes.json` e `data/glossario.json`. **Catálogo e fichamento não foram tocados**: as correções de catálogo e as afirmações sobre os 5 orixás ficam listadas abaixo para a orquestradora encaminhar.

Os PDFs ficaram fora do repositório (`/tmp`). O anti-cópia rodou contra o texto das 8 obras lidas (`ANTICOPIA_REFS`), com 0 erros. Três frases da descrição do Tambor de Mina e três trechos curtos (6 palavras) de outras descrições foram reescritos depois da checagem.

## 1. Fontes lidas no original

| Fonte (id no catálogo) | Acesso | Páginas lidas | Paginação (impressa × PDF) |
|---|---|---|---|
| Halloy 2005, tese (`halloy-2005-intimite`) | arquivo direto no HAL (a página do HAL tem desafio anti-robô, o arquivo não) | 24–31, 84–86, 96–98, 115–121, 163–170 | impressa = PDF |
| Pitta, "Mitos e símbolos nos xangôs de Pernambuco" (`pitta-2011-mitos`) | periodicos.fundaj.gov.br (o endereço `fundaj.emnuvens.com.br` deu 502) | 263–268 (integral) | impressa = PDF + 262 |
| M. Ferretti, "Pureza nagô e nações africanas no tambor de Mina" (`ferretti-m-2020-pureza`) | periodicos.sbu.unicamp.br (o endereço `econtents.bc.unicamp.br` deu 502) | 75–84 | impressa = PDF + 74 |
| S. Ferretti 2011, "Comida ritual…" (`ferretti-2011-comida`) | PUC Minas (link de download via OpenAlex) | 242–265 | impressa = PDF + 241 |
| Oro 2012, "O atual campo afro-religioso gaúcho" (`oro-2012-campo`) | PUCRS | 556–565 (integral) | impressa = PDF + 555 |
| Toutain 2019, tese (`toutain-2019-santos`) | arquivo direto no HAL (theses.hal.science) | 2, 6–11, 18–21, 107–112 | impressa = PDF − 11 (parte em algarismos arábicos) |
| Argyriadis 2005 (`argyriadis-2005-ramas`) | journals.openedition.org (PDF) | 153–157, 175–176 | impressa = PDF + 151 |
| Cerqueira 2015, tese (`cerqueira-2015-lebabimibome`) | arquivo direto no HAL (theses.hal.science, tel-01778552) | 82–83, 88, 132, 155, 165 | impressa = PDF − 1 |

**Não lidas (bloqueadas):** Santana 2023 (Xambá), Mendes 2014 (Candomblé Angola), Niell 2023 (Lucumí), S. Ferretti 1996 (Acossi) e Corrêa 1996 (Batuque) → §5 e [PENDENCIAS](PENDENCIAS.md) §1. Nenhum id faltou no catálogo.

## 2. Tradições

**Antes:** 13 `com_fonte`, 6 `rascunho_sem_fonte`. **Depois:** 15 `com_fonte`, 4 `rascunho_sem_fonte` (benim, candomble_efon, arara, orisha_trinidad).

| Tradição | Mudança | Fontes novas (página) |
|---|---|---|
| `palo_monte` | **ganhou fonte.** Origem banto como descrição usual; Regla Conga; variantes mayombe, briyumba, kimbisa; cosmologia (Nsambi, mpungus, nfumbis); trânsito entre palo, santería, Ifá e espiritismo. Iniciação e objetos de culto ficaram fora por serem fundamento | Toutain pp. 2 (notas 3–4), 9–11; Argyriadis p. 176 (nota 5) |
| `xango_sergipe` | **ganhou fonte, descrição mínima.** Nome xangô aplicado de fora ao culto aos orixás em Sergipe (Bastide, via Halloy); pesquisa de Dantas sobre "pureza nagô" (via M. Ferretti). A nota avisa que são citações de segunda mão e que Dantas 1988 continua necessária | Halloy p. 31; M. Ferretti p. 76 |
| `xango_pernambuco` | reforço: rótulo exógeno e autodenominação "candomblé nagô"; caráter regional e expansão nos anos 1950; nações nagô e Xambá; terreiros jeje e jeje-ketu recentes; classificação de Motta na nota | Halloy pp. 29, 31, 85–86, 98, 120–121; Pitta p. 263 |
| `tambor_de_mina` | reforço: Casa das Minas e Casa de Nagô como matrizes; predomínio do modelo nagô, distante do "nagô puro" baiano; discrição sobre mitologia; festas de cultura popular; influência de candomblé e umbanda; Fanti-Ashanti na nota | M. Ferretti pp. 76–78, 82; S. Ferretti pp. 245, 247–248, 264–265 |
| `batuque_rs` | reforço: nações (Jeje-Ijexá a mais importante), origem em Pelotas e Rio Grande, duas versões do mito fundador, Umbanda (1926) e Linha Cruzada (anos 1970), censos 2000/2010, expansão para Argentina e Uruguai | Oro 2012 pp. 557–560, 564; Halloy p. 30 |
| `umbanda` | reforço: difusão nacional, vista pelos adeptos como religião nacional; no RS, ritos em português, sem tambores nem sacrifício, culto a caboclos, pretos-velhos e bejis. Divergência de data de origem na nota | Oro 2012 pp. 557, 560; Halloy p. 30 |
| `lucumi` | reforço: lucumí como etnônimo colonial que passou a indicar o caminho religioso; cabildos; cosmologia (eggún, Olofí/Olodumare/Olorun, orichas); Ifá, palo e espiritismo ao lado; difusão para fora de Cuba. Na nota: crítica de Guanche à equação lucumí = iorubá; uso de "santería" | Toutain pp. 2, 7–8, 10–11, 19–20, 111; Argyriadis pp. 154, 175 |
| `candomble_jeje` | reforço: papel dos jejes libertos em Salvador; Bogum e Seja Hundê fundados por africanos de regiões sob o Daomé; jeje = nações que dizem vodum; nação jeje marrim (mahi). Marcado na nota como resumo de Parés 2006, ainda não lido | Cerqueira pp. 82, 132, 155, 165 |

**Sem mudança:**
- `arara`: Toutain (pp. 19, 107) só cita *arará* como nação colonial dos cabildos e dos engenhos de Matanzas, o que não basta para descrever a Regla Arará.
- `candomble_angola`: Mendes 2014 bloqueado.
- `candomble_efon`, `orisha_trinidad` e `benim`: nenhuma das fontes lidas trata deles.

**Divergências e ressalvas registradas em `nota`:**
- Umbanda: primeiro quartel do século XX (Prandi) × anos 1930 no Rio de Janeiro (Halloy).
- Batuque: Oro fala em doze orixás, mas lista onze nomes.
- Batuque: "início" (Oro 2008) × "primeira metade" do século XIX (Oro 2012).
- Tambor de Mina: Casa das Minas dominante (Bastide) × maioria dos terreiros no modelo da Casa de Nagô (M. Ferretti).
- Xangô de Pernambuco: Motta classifica como xangô umbandizado um terreiro que outros contam como jeje.
- Xangô de Pernambuco: grafia do fundador da Xambá (Artur Rosendo × Arthur Roseno).

## 3. Glossário

**Antes:** 47 termos. **Depois:** 54 termos. Todos os novos têm fonte `conferido_web` e página.

| Termo | Fontes | Observação |
|---|---|---|
| Regla de Ocha (santería) | Toutain pp. 7, 8, 11 (nota 27); Argyriadis p. 175 (nota 1) | divergência sobre o alcance de "santería" (Ocha × Ocha-Ifá) |
| Palo Monte (palo, Regla Conga) | Toutain pp. 9, 11; Argyriadis p. 176 (nota 5) | — |
| nfumbi | Toutain p. 9; Argyriadis p. 176 (nota 5) | — |
| mpungu | Toutain p. 9 | divergência: divindades mediadoras (Toutain) × conjuntos de forças naturais sem forma humana (Argyriadis p. 176, nota 9) |
| cabildo de nación | Toutain pp. 19, 20 (nota 38) | — |
| Xambá | Halloy pp. 86, 120–121 | grafia do fundador na nota |
| abatá (bata) | M. Ferretti pp. 78–79; Halloy p. 120 (nota 261) | Maranhão × Recife |

Termos existentes que ganharam fonte:
- **Linha Cruzada:** Oro 2012, pp. 557, 559–560 (origem nos anos 1970, críticas internas).
- **nação:** Halloy p. 28 (sentido étnico → modelo teológico e litúrgico).

Em `_meta.pendentes`, "Regla de Ocha, Palo Monte, Arará, Shango (Trinidad)" virou "Arará, Shango (Trinidad)".

Ficaram de fora de propósito, por serem iniciação ou fundamento: *nganga*/*prenda*, *rayamiento*, *kariocha*/*asiento*, *itá* cubano, *santos guerreros*. Também ficou de fora *eggún* (já coberto por `egum`).

## 4. Afirmações sobre os 5 orixás (para a orquestradora encaminhar ao fichamento)

Nenhuma destas entrou em `data/fichamento/`. São paráfrases com página, com a tradição indicada pela própria fonte. **Alimentos e oferendas** (S. Ferretti 2011, pp. 259–264) ficaram fora de propósito, conforme a decisão de reter tabus e alimentos até o conselho. Detalhes sacrificiais de Halloy (p. 165, "Exu do tempo") também ficaram fora.

### Halloy 2005: nação nagô do Recife (família de santo descendente de Pai Adão), `xango_pernambuco`

| Orixá | Página | Paráfrase |
|---|---|---|
| Exu | p. 164 | Os participantes distinguem o Exu do peji, orixá mensageiro entre humanos e orixás, sem o qual nada se começa, e o Exu da rua, guardião das soleiras que protege o terreiro. Nota 348: em Salvador, este se chama "Exu do portão". |
| Exu | p. 164 | Descrito como o mais humano dos orixás, ambivalente ("nem bom nem mau"), brincalhão e semeador de discórdia. |
| Exu | pp. 164–165 | Tem duas naturezas: orixá ou espírito da jurema. Como orixá não toma posse de seus filhos; como espírito é incorporado com frequência e procurado para magia ofensiva. Lugares: encruzilhadas e rua. |
| Exu | p. 165 | Cores vermelho, preto e branco (as duas primeiras dominantes); dia, segunda-feira. Nota 353: os dias da semana pesam pouco na prática, salvo segunda (Exu), sexta (Oxalá) e sábado (Oxum e Iemanjá), e são preferências, não regras. |
| Ogum | pp. 165–166 | Deus ferreiro, "dono do ferro", responsável pelos utensílios desse metal, inclusive a faca ritual; arquétipo do guerreiro, temperamento impetuoso; domínios: mata e rua (associado à violência que nela ocorre); abridor de caminhos. Desce em possessão, mas tem poucos filhos no nagô do Recife. Cores vermelho e verde; dia, terça-feira. |
| Oxóssi (Odé) | p. 166 | Deus caçador, irmão mais novo de Ogum, ligado a uma atividade humana (a caça) e à mata; possessão ainda mais rara que a de Ogum no nagô do Recife. Nota 356: contraste com a Bahia, onde é muito popular. Cor principal verde, às vezes com vermelho ou branco; pode aparecer vestido de peles; sem dia fixo. |
| Xangô | p. 168 | "O Rei Xangô", o orixá mais popular no Recife; divindade do raio e do trovão, guerreiro, impetuoso, orixá da justiça que pune com severidade; sedutor, teve por esposas Obá, Oiá e Oxum. Nota 364: a ordem das esposas varia entre mitos e tradições (João do Rio 1904; Verger 1985; Segato 1995). |
| Xangô | p. 169 | Cores vermelho e branco. Nota 363 (p. 168): a popularidade explicaria o nome "xangô" dado ao culto. |
| Xangô | p. 169 | Mito citado: Xangô expulso do balé (lugar dos eguns) por revelar segredos, segundo Segato 1995 (nota 366, verbete Oiá). |
| Iemanjá | p. 169 | Divindade das águas salgadas, mulher de Oxalá e "mãe de todos os orixás"; arquétipo da mãe que gera e protege, mas pode ser severa com os filhos; Segato fala em caráter "duplo", que Halloy diz que vai matizar. Cor azul profundo. |
| Iemanjá | p. 170 | Com Orixalá, forma o casal demiurgo que gerou os demais orixás, exceto Nanã, Obaluaiê e Oxumarê. |

### Pitta (1985; catálogo: 2011): xangôs tradicionais do Recife e de Olinda (30 entrevistas com iniciados), `xango_pernambuco`

| Orixá | Página | Paráfrase |
|---|---|---|
| Iemanjá, Ogum, Xangô | p. 263 | Entre os mitos mais citados no Recife e em Olinda estão os de Oxum, Iemanjá e Iansã e, também, os de Xangô e Ogum. Iemanjá reina sobre as águas salgadas e é mãe de todos os orixás (Oxum é sua filha); Ogum é o orixá do ferro e da guerra; Xangô é a divindade das tempestades, raios e trovões. |
| Iemanjá | pp. 263–264 | Mito cosmogônico (versão transcrita de Ellis, 2ª mão): Iemanjá e Aganju nascem da união de Odudua e Obatalá; Orungã, filho de Iemanjá, a violenta; do corpo dela saem as águas e os orixás. Para Pitta, a figura reúne sedução e fertilidade, e Iemanjá está na base de toda a criação. Os elementos masculinos do mito foram esquecidos e Iemanjá segue muito cultuada. |
| Xangô | pp. 264–265 | Mito de Oxalá velho que viaja para ver o filho Xangô, é preso injustamente pelos servidores de Xangô e libertado após consulta ao babalaô (Xangô como filho de Oxalá). |
| Iemanjá | p. 267 | Nas conclusões: as divindades femininas (Iemanjá, Oxum, Iansã) são ativas e guerreiras, e Iemanjá é parte ativa da criação. |

### Toutain 2019: santería do central Méjico, Matanzas (Cuba), `lucumi`

| Orixá | Página | Paráfrase |
|---|---|---|
| Exu (Elegguá), Ogum (Oggún), Oxóssi (Ochosí) | p. 7 | A entrada no culto começa pela recepção dos "santos guerreiros", Elegguá, Oggún e Ochosí, junto com Osún. |
| Xangô (Changó), Iemanjá (Yemayá) | p. 7 | Changó e Yemayá estão entre os orichas maiores (com Obatalá e Ochún). Nota 13: Changó é tido como antigo aláàfin (rei) de Oyó e, ao mesmo tempo, associado ao raio, ao fogo, aos tambores e à guerra. |
| Exu, Ogum | p. 8 (nota 18) | Cores dos colares: preto e vermelho para Elegguá; verde e preto para Oggún. |
| Exu | p. 11 | Uma associação de Ifá das Canárias viaja todo ano, em outubro, ao central Méjico para a "fiesta de Elegguá". |

### Oro 2012: Batuque, `batuque_rs`

| Orixá | Página | Paráfrase |
|---|---|---|
| Exu (Bará), Ogum, Xangô, Oxóssi (Odé/Otim), Iemanjá | p. 557, nota 3 | Estão entre os orixás do Batuque. A cada orixá se atribuem características, símbolos, animais sacrificados e correspondências com santos católicos, vindas dos mitos das duas tradições. |

### S. Ferretti 2011: Tambor de Mina, terreiro de Pai Itaparandi (nagô/cambinda), `tambor_de_mina`

| Orixá | Página | Paráfrase |
|---|---|---|
| Xangô, Ogum, Iemanjá | p. 261 | Calendário da casa: oferendas a Xangô no dia de São Pedro, a Iemanjá em dezembro e a Ogum em 23 ou 24 de abril. |
| Xangô | pp. 260, 262 | Na mesma casa, Xangô aparece emparelhado com o vodum Badé ("para Xangô ou Badé"); a festa de Badé é no dia de São Pedro. |

O conteúdo das oferendas foi omitido por ser alimento ritual.

### Cerqueira 2015: Candomblé Jeje, Seja Hundê (Cachoeira), `candomble_jeje`

| Orixá | Página | Paráfrase |
|---|---|---|
| Xangô | p. 82 | No Seja Hundê, os voduns maiores Bessem, Sobo e Azançu correspondem, segundo o autor, a Oxumarê, Xangô e Obaluaê. Serve de equivalência vodum × orixá para Xangô (Sobo). |
| Exu | pp. 82–83 | O vodum Lebabimibome, guardião do terreiro, é descrito como resultado de uma fusão com Exu-Legba. |
| Exu, Ogum | p. 88 | Em entrevista, o ogã Buda descreve Legba e Ogum Xoroquê como parceiros na guarda da casa, e Ogum Metametá como reunindo traços de Ogum Xoroquê e de Exu. É depoimento de praticante (Ogum "Xoroquê" pede revisão do conselho). |

## 5. Bloqueios e correções de catálogo (para PENDENCIAS e para a sessão do catálogo)

**Acesso bloqueado** (registrado em [PENDENCIAS](PENDENCIAS.md) §1):

| Fonte | Endereço | Erro |
|---|---|---|
| Santana 2023 | `revistas.uece.br` | 403 em todos os downloads |
| Mendes 2014 | `www.e-publicacoes.uerj.br` | conexão cortada (3 tentativas) |
| Mendes 2014 | `www.redalyc.org` | 403 (já listado) |
| S. Ferretti 1996, Corrêa 1996 | `www.scielo.br` | desafio anti-robô (Bunny Shield) |
| Niell 2023 | `www.mdpi.com` | 403 (Akamai) |

**Correções sugeridas para o catálogo** (não editado nesta sessão):
- `pitta-2011-mitos`: o artigo saiu em 1985 (*Cadernos de Estudos Sociais*, Recife, v. 1, n. 2, pp. 263–268). 2011 deve ser a data da versão online. Anotar em `observacoes`, sem trocar o ano citado.
- `ferretti-m-2020-pureza`: o texto é o artigo de 2001 (*Ciencias Sociales y Religión / Ciências Sociais e Religião*, Porto Alegre, ano 3, n. 3, pp. 75–94; DOI 10.22456/1982-2650.2170). O link funcional é `periodicos.sbu.unicamp.br/ojs/index.php/csr/article/download/8669436/28738`.
- `cerqueira-2015-lebabimibome`: acrescentar a evidência `https://theses.hal.science/tel-01778552`.
- `halloy-2005-intimite`: o PDF integral está em `https://hal.science/tel-04260456/file/Th%C3%A8se%20Arnaud%20Halloy.pdf`.
- `toutain-2019-santos`: o PDF integral está em `https://theses.hal.science/tel-03191332/file/Toutain_Maxime.pdf`.

## 6. Próximos passos sugeridos

1. Encaminhar o §4 ao fichamento. Halloy tem cores, dias e domínios dos 5 orixás numa tradição (nagô do Recife) ainda pouco representada, e pode abrir divergências com a Bahia (Oxóssi popular × raro no Recife).
2. Ler Parés 2006 para confirmar o que Cerqueira resume sobre o Jeje e para as equivalências de voduns (tarefa 2 do ESTADO).
3. Arará, Efon e Orisha de Trinidad continuam sem fonte aberta ([PENDENCIAS](PENDENCIAS.md) §2).
4. Baixar manualmente Santana 2023, Mendes 2014, Niell 2023, S. Ferretti 1996 e Corrêa 1996.
