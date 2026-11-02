# Fichamento 10 — quatro fontes enviadas pelo autor (Peel 2016, Verger 1965, S. Ferretti 1996, Corrêa 1996) e a tradição uruguaia

**Sessão:** fich10 (trabalhadora, coordenada pela orquestradora), 2026-11-02.
**Escopo:** fichar quatro fontes que o ambiente não baixava (OAPEN, Persée, SciELO) e que o autor pôs no acervo privado `aureliosaraiva/orixas-fontes`; criar a tradição `afroumbanda_uruguai` proposta na fich09; atualizar grafo, itãs e capítulos. Um commit por fonte.

## 1. Acesso

- `add_repo` (owner `aureliosaraiva`, repo `orixas-fontes`, access `push`) funcionou; clone raso em `../orixas-fontes` (55 textos). Os quatro PDFs e textos já estavam no acervo; nenhum arquivo novo foi gerado ali, então o `acervo_sync.sh push` não tinha o que enviar.
- Páginas citadas são as impressas.

| Fonte | Lido | Página impressa × PDF | Licença |
|---|---|---|---|
| Peel 2016, *Christianity, Islam, and Oriṣa Religion* (UC Press, Luminos) | caps. 1 (pp. 35–37), 3 (pp. 52–70, inteiro), 4 (pp. 75–78), 11 (pp. 214–228); trechos de 2 (p. 47), 7 (pp. 133–135), 8 (pp. 154–155), 9 (pp. 168–169); nota 7 do cap. 11 (p. 285). Os caps. 5–10 tratam de cristianismo e islã e não falam de orixás além do que foi fichado | impressa = PDF − 15 | CC BY-NC-ND |
| Verger 1965, "Grandeur et décadence du culte de ìyámi òsòròngà", *JSA* 35(1) | parte analítica, pp. 141–160 (os textos de Ifá, pp. 160–243, foram só percorridos para delimitar o que não fichar) | impressa = PDF + 140 | acesso livre (Persée) |
| S. Ferretti 1996, "Festa de Acossi e o arrambã", *Horizontes Antropológicos* 2(4) | integral, pp. 61–70 | impressa = PDF + 60 | CC BY 4.0 |
| Corrêa 1996, "A cozinha é a base da religião", *Horizontes Antropológicos* 2(4) | integral, pp. 49–60 | impressa = PDF + 48 | — |

Catálogo: DOI de Peel (`10.1525/luminos.8`, sugerido pela própria obra) acrescentado; Verger 1965 deixou de constar como "não lido"; observações de leitura nas quatro entradas. Noleto & Negrão 2025 ganhou `afroumbanda_uruguai` entre as tradições.

## 2. Registros

**+85 registros `fichado`** (997 → 1082; 1066 `fichado`, 16 `pre_fichamento`). Fichas: 26 → **27** (Orixá Okô), 967 → **1049** versões; retidos: 14 → **17**.

| Fonte | Registros | Entidades |
|---|---:|---|
| Peel 2016 | 52 | Ogum 13, Orunmilá 8, Xangô 6, Exu 3, Odudua 3, Oxalá 4, Orixá Okô 4 (arquivo novo), Olodumare 2, Egungun 2, Oxum 2, Iemanjá, Iansã, Olokun, Orí, Omolu |
| Corrêa 1996 | 22 | Exu 3, Xangô 3 (com o itã), Oxum 3, Omolu 2, Egungun 2, Ogum 2, Obá 2, Iansã, Oxóssi, Ossaim, Iemanjá, Oxalá |
| S. Ferretti 1996 | 3 | Omolu (família de Acossi) |
| Verger 1965 | 8 | Iyami |

### 2.1 Peel 2016

Peel lê cerca de 780 menções a orixás nos diários e cartas dos agentes da Church Missionary Society (1845–1912), em sua maioria iorubás. Todos os registros que dependem desse material levam a mesma nota: são relatos missionários lidos por um historiador e mostram o que chamava a atenção dos missionários, não a frequência real do culto (pp. 53–55).

- **Ogum (cap. 3):** o ferro como o próprio deus; sem imagem esculpida (Alajogun, em Oyó, sim); bigorna e ferramentas; força no leste (14% das menções; Ondo, Ilesha) e pouca presença no sudoeste (Xangô 4:1); festa cívica com milícias e batalhas encenadas; culto cívico onde o ferro era escasso; o culto de Ogum como serpente, sobretudo de mulheres, nas cidades oyó (1852–1911); mulheres devotas de Ogum; justiça e purificação; festa do inhame novo variando por cidade; Exu e Ogum como castigo divino (Ibadan, 1855); adaptação à modernidade; Ogum como caso para a tese dos complexos de culto locais.
- **Xangô:** antigo alafin divinizado, divindade oyó estranha ao leste; o orixá mais citado com Ifá, culto expansivo (multas após raio, epidemias de Ondo em 1879–1880); machado do raio; Xangô figurado como mulher onde chega depois de outro deus do trovão; festa de Oyó e o alafin muçulmano; o nome Xangô designando o culto em Trinidad e em partes do Brasil (tradições `orisha_trinidad` e `xango_pernambuco`, a segunda com nota de aproximação).
- **Orunmilá/Ifá:** 256 odus e o funcionamento da consulta; Orunmilá acima dos orixás e canal de Olodumare; babalaôs que recomendavam conversão; hipótese da origem islâmica da forma; culto masculino e sem possessão; Ifá quase extinto no Brasil e firmado em Havana (cinco babalaôs fundadores da Regla de Ifá); releitura cristã e Igreja de Orunmilá (1934); festa de Ilesha.
- **Odudua, Olodumare, Egungun, Exu, Oxum, Iemanjá, Iansã, Olokun, Oxalá, Orí, Omolu:** ver a lista de ids no §2.4. Destaques: Odudua masculino no centro-leste e feminino no sudoeste (variação regional, nota 7); Olodumare age pelos orixás; orixás comparados por babalaôs aos chefes menores (1854); distribuição regional das deusas de rio (Iemanjá a oeste, Oxum no centro-leste, Oiá ao norte); Orixalá como nome brasileiro de Obatalá; Sopona (Babaluaye) ligado a Omolu pelo nome já registrado em omolu-001.
- **Orixá Okô** (arquivo novo `data/fichamento/orixa_oko.json`): deus da roça com bastão de ferro; Irawo e os julgamentos de feitiçaria; prestígio entre as mulheres de Abeokuta; uma das três divindades de Ibadan, ligada ao inhame novo e às chuvas; declínio no século XX. O interdito dos devotos (contato com cadáveres, p. 63) não foi fichado (tabu).
- **Tradição `ioruba_nigeria`:** a frase sobre a ausência de panteão único volta à descrição, com Peel pp. 52, 63, 216–217, 224–225 (PENDENCIAS §2 ✅), junto com a origem do nome "iorubá" e a ideia de que a religião unificada se formou nas Américas; a nota registra a crítica de Peel ao termo "panteão".
- **Não fichado:** Ajé, "deusa do dinheiro" consultada por meio de Ogum (p. 60), porque nenhuma fonte lida a identifica com `aje_xaluga`; o mito de Ogum e Iemanjá (p. 65), que Peel só resume de Matory (não catalogado); detalhes de execuções e sacrifícios humanos (pp. 66–67), que não são atributo de entidade.

### 2.2 S. Ferretti 1996 e Corrêa 1996 (comida ritual)

Seguindo a instrução da orquestradora, o foco foi a descrição das tradições, festas, organização e leitura acadêmica.

- **Tambor de Mina (Ferretti):** a família de Acossi (voduns da terra, cura de doenças de pele) e a festa de Acossi (19–21 de janeiro; comida de obrigação servida por dois voduns no dia de São Sebastião; jonu e nadopé), em Omolu, com a nota de correspondência de omolu-024. A descrição de `tambor_de_mina` ganhou: religião de gente pobre; sem rito sem comida; ritos públicos, semiprivados e secretos; guma, comé e cozinha como lugares mais sagrados, com piso de terra; a cozinheira dos voduns; os voduns que "não comem"; a festa de Acossi e o arrambã (despedida dos voduns antes da Quaresma), comparado à bancada da Casa de Nagô. A nota traz a leitura maussiana do autor e sua avaliação da continuidade da Casa das Minas.
- **Batuque (Corrêa):** o panteão de doze orixás com seus domínios (Bará, Ogum, Oiá/Iansã, Xangô, Odé e Otim, Obá, Ossanhe, Xapanã, Oxum, Iemanjá, Oxalá); Bará Lodê e Bará Jelu; Bará chamado Elegbara ou Legba em outras áreas nagôs; Xangô dono dos instrumentos e senhor dos mortos; Xapanã Velho e o Cristo das Chagas (sincretismo, com nó novo no grafo); as danças de Oxum Docô e de Obá; Oxalá, o mais velho e pai de todos; os eguns e a cerimônia anual (aressum) em nível geral; **um itã** (Xangô larga Oxalá, Ogum fica com Iansã, a fuga e a luta; encenado na dança do atã), sem o castigo alimentar. A descrição de `batuque_rs` ganhou o perfil dos adeptos, a organização dos templos, a "religião africana" × "festa brasileira", o prestígio de quem distribui e a cozinha ritual como marca regional; a nota põe lado a lado as datas de Corrêa (Umbanda nos anos 1930, Linha Cruzada em 1940–1950) e de Oro (1926; anos 1970).
- **Retidos (3):** ogum-091 e oxum-067 (Corrêa, exemplos que o autor usa para mostrar o caráter regional da cozinha) e omolu-060 (a comida da festa de Acossi), todos fora da ficha pública.
- **Não fichado (PENDENCIAS §3c):** graus de iniciação, sacrifícios e provas de possessão; receitas e pratos por orixá; oferendas e feitiçaria; interdições alimentares e de pureza; etapas e objetos do culto aos mortos.

### 2.3 Verger 1965 (Iyami)

Tema sensível. Ficharam-se só análise acadêmica e história publicadas, todos os registros com a nota "Entidade sensível: só leitura acadêmica pública, sem fundamento; registro a confirmar pelo conselho (PENDENCIAS §3c)":

| id | atributo | conteúdo |
|---|---|---|
| iyami-005 | nomes | designações indiretas (ìyámi òṣòròngà, ìyámi, ẹlẹ́yẹ, àgbà/ìyá àgbà) e o termo àjẹ́ |
| iyami-006 | interpretacao_academica | tese do autor: feitiçaria ligada aos orixás e aos mitos da criação; imagem popular como forma degradada |
| iyami-007 | historia_culto | sociedades Gẹ̀lẹ̀dẹ́ (Ketu, Egba, Egbado), dirigidas por mulheres; título erelu |
| iyami-008 | historia_culto | festa dos Gẹ̀lẹ̀dẹ́ em Salvador, 8 de dezembro, Boa Viagem, presidida por Maria Júlia Figueiredo (Engenho Velho), iyálóde-erelú (`candomble_ketu`) |
| iyami-009 | historia_culto | a Ìyálóde e a lelu dos nupe (extinta sob o islã) |
| iyami-010 | historia_culto | movimentos antifeitiçaria (Atinga, c. 1940–1950) e as idosas guardiãs de santuários |
| iyami-011 | interpretacao_academica | leituras sociológicas (Morton-Williams, Beier) e a hipótese dos três períodos |
| iyami-012 | interpretacao_academica | Iyami como fator de moderação contra excessos de poder |

**Não fichado** (lista para o conselho, PENDENCIAS §3c): os dez textos de Ifá e seus resumos (mitos de origem; Iyami e Orunmilá; Odù e Orixalá; o pano de Egungun); poderes e práticas (pássaro, cabaça, reuniões, interditos, oferendas de proteção); a saudação e o oríkì cantados em Salvador (p. 158); o conceito de àṣẹ; a nota sobre Egungun e Oro; a variante cubana do casal criador (Lydia Cabrera). **Nenhum capítulo de Iyami foi escrito.**

### 2.4 Ids novos

Peel: ogum-077–089, xango-066–071, orunmila-014–021, odudua-020–022, olodumare-020–021, egungun-016–017, exu-115–117, oxum-063–064, iemanja-096, iansa-052, olokun-008, oxala-078–081, ori-013, omolu-057, orixa_oko-001–004. Ferretti: omolu-058–060. Corrêa: exu-118–120, ogum-090–091, iansa-053, xango-072–074, oxossi-047, oba-026–027, ossaim-048, omolu-061–062, oxum-065–067, iemanja-097, oxala-082, egungun-018–019. Verger: iyami-005–012.

## 3. Tradição `afroumbanda_uruguai`

- Criada em `data/tradicoes.json` (`com_fonte`): "Religiões afroumbandistas do Uruguai", grupo novo **`diaspora_afro_brasileira`** ("Diáspora afro-brasileira"), matriz mista. Fontes: Noleto & Negrão 2025, pp. 8 (nota 6), 10, 19–20, 23; Prandi 1995, p. 12. A descrição diz o que o termo cobre (umbanda, batuque, quimbanda, candomblé; federações), de onde vêm as linhagens (Porto Alegre e Santana do Livramento, desde os anos 1950; expansão à Argentina), o porquê do nome (substitui "afro-brasileira") e as festas públicas (Iemanjá, Oxum). A nota mantém lado a lado a versão de origem direta africana e registra que a explicação do termo é de Bem 2012, não lido.
- Os 11 registros de Noleto & Negrão (iemanja-087 a 095, oxum-062, exu-114) passaram de `umbanda`/`batuque_rs` para `afroumbanda_uruguai`; a nota de cada um foi atualizada.
- Mínimo necessário fora de `data/`: enum de grupo em `schemas/tradicao.schema.json`, enum de tradição em `schemas/fonte.schema.json`, rótulo e ordem do grupo em `site/src/lib/dados.js` e frase de abertura do grupo em `site/src/pages/tradicoes.astro`. O padrão de id de registro em `schemas/_versao.schema.json` passou a aceitar `_` (necessário para `orixa_oko-NNN`).

## 4. Grafo e itãs

- `conexoes_alvos.json`: xango-073 → cônjuge de Iansã (aresta já existente, ganhou versão do Batuque); omolu-062 → nó novo `santo:cristo-das-chagas`. Grafo 138/179 → **139 nós, 180 arestas**; 0 `sem_mapa`.
- `itans.json`: **ita-031** "Xangô larga Oxalá no barro, e Ogum fica com Iansã" (Batuque de Porto Alegre; entidades Xangô, Iansã, Ogum, Oxalá), espelhado de xango-074. 31 itãs, 46 versões.
- Divergências: 137 atributos (inalterado).

## 5. Capítulos

17 capítulos editados; `validar_capitulos.py --gerar`: 0 erros.

- **Ogum:** dois parágrafos na história (Iorubalândia oitocentista: leste × sudoeste, festa cívica, culto da serpente; castigo de 1855; modernidade), um em domínios (o ferro como deus, Alajogun, justiça, inhame novo), Batuque reescrito (domínios + o itã do atã) e leitura de Peel em "Leituras acadêmicas".
- **Xangô:** história (divindade oyó, culto expansivo, alafin, Trinidad e Brasil), domínios (machado; Batuque), mito do Batuque com link para ita-031, Batuque reescrito, leitura de Peel sobre o Xangô feminino.
- **Orunmilá:** história (culto masculino, conversões, Ilesha, Igreja de Orunmilá; Brasil × Havana), funcionamento do oráculo, leitura de Peel sobre a origem da forma.
- **Odudua, Olodumare, Egungun:** parágrafos na história e na subseção iorubá; Egungun também com os eguns do Batuque.
- **Exu, Oxum, Iemanjá, Iansã, Oxalá, Omolu, Obá, Ossaim, Oxóssi:** Batuque reescrito com o panteão de Corrêa (as frases "o fichamento só guarda…" saíram); Iorubalândia regional para as deusas de rio; Omolu com Sopona, a família e a festa de Acossi (Mina) e o Cristo das Chagas; Iemanjá com a subseção **"No Uruguai: as religiões afroumbandistas"** (link para a tradição nova).
- **Orí e Olokun:** as lacunas de história do culto viraram texto (ori-013; olokun-008, com pendência de Verger 1981). Ogum: a lacuna de alimentos virou pendência do conselho (há registro retido).

**Conferência manual.** Os parágrafos novos foram relidos ao lado dos registros. Ajustes: "ganhou dela a mão" (Ogum) virou "recebeu Iansã como recompensa", que é o que o mito diz; "por isso não se esculpia" virou "talvez por isso", porque a explicação é hipótese de Peel; o Ọọni passou a ser "tido como" Odudua renascido; "século XIX" e "Atlântico" foram trocados onde os registros citados não os traziam (heurística do validador); 29 trechos com 8+ palavras iguais às paráfrases foram reescritos.

## 6. Anti-cópia (texto integral, acervo `orixas-fontes`, 55 textos)

**0 erros** em todos os commits. Erros iniciais reescritos: 2 na descrição/nota das tradições (Ferretti, "bancada da Casa de Nagô…"; Corrêa, datas da Linha Cruzada) e 1 num capítulo (Bará Jelu). Avisos "próximo" restantes ligados a estas fontes, mantidos e justificados:

| Campo | Trecho | Justificativa |
|---|---|---|
| exu-120.valor | "Bará Jelu de dentro de casa" | nome de qualidade + expressão corrente |
| tradicoes/batuque_rs.nota | "e a Linha Cruzada nos anos" | nome próprio + expressão de data (frase sobre Oro) |
| capítulo Egungun | "entre os egbá, a sociedade Oro" | nomes |
| capítulo Exu | "os principais cultos públicos de Ondo" | expressão corrente + nome de lugar |
| capítulo Odudua | "que teria reinado em Ilê-Ifé" | nome de lugar |
| capítulo Ogum | "de Ifá e de Exu no"; "em Ijaye, Ibadan, Abeokuta e Oyó" | nomes; lista de cidades |
| capítulo Omolu | "de 19 a 21 de janeiro" | data |
| capítulo Orunmilá | "Peel, a estrutura de dezesseis opções" | nome + termo técnico |
| capítulo Oxalá | "em Ibadan, Ogiyan, um dos orixás" | nomes |
| capítulo Xangô | "as epidemias de varíola de 1879" | data e termo |

As paráfrases de Peel e Verger são traduções próprias do inglês e do francês (sem checagem por tradutor, como nas fontes estrangeiras anteriores).

## 7. Validação

`validar_fontes`, `validar_fichamento`, `divergencias` (137), `gerar_fichas` (0 avisos), `validar_fichas`, `anticopia` (0 erros), `validar_capitulos --gerar` (0 erros), `python3 -m unittest discover -s tests` (82 testes OK), os três `tests/e2e_*.py` (OK), build do site e `qa_site.py` (96 páginas, 1049/1049 versões, 26 capítulos com 636 parágrafos, 20 tradições, 0 vazamentos do acervo): **ok**. `node site/scripts/acessibilidade.cjs`: nenhuma violação grave.

## 8. Pendências novas ou alteradas

- ✅ §1: Persée (Verger 1965), OAPEN (Peel 2016), SciELO (S. Ferretti 1996, Corrêa 1996). ✅ §2: frase do panteão de `ioruba_nigeria`. ✅ §3a: tradição uruguaia.
- 🔴 §2: obras citadas e não lidas (Bem 2012, Morton-Williams 1956, Beier 1956, Nadel, Matory 1994, Abraham).
- 🔴 §3c: o que ficou fora de Verger 1965 (P1, conselho) e de Corrêa/Ferretti (P2, conselho).

## 9. Sugestões

1. Capítulo de Orixá Okô quando houver uma segunda fonte (hoje só 4 registros de Peel).
2. Conselho: decidir o que publicar de Verger 1965 além da camada acadêmica e se os 12 registros de Iyami podem ir para um capítulo.
3. Glossário: arrambã, comé, guma, aressum, mesa dos prontos e Gẹ̀lẹ̀dẹ́ têm definição pública e página nas fontes desta sessão.
4. Ajé/Ajê Xalugá: procurar fonte que identifique a deusa do dinheiro de Peel (p. 60) com `aje_xaluga` antes de fichar.
5. Revisor de Batuque (Oro, no conselho) conferir o panteão de Corrêa e o itã da dança do atã.
