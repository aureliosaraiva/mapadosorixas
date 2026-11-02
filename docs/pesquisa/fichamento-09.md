# Fichamento 09 — três fontes P1 liberadas pelo autor (Prandi 1995, Giumbelli & Lima 2024, Noleto & Negrão 2025)

**Sessão:** fich09 (trabalhadora, coordenada pela orquestradora), 2026-11-02.
**Escopo:** fichar as três fontes que o SciELO bloqueava desde 2026-11-01 (PENDENCIAS §1 e §1b), cujos PDFs o autor enviou e a orquestradora pôs no acervo privado `aureliosaraiva/orixas-fontes` (`pdf/` e `txt/`); atualizar grafo, fichas e capítulos.

## 1. Acesso

- `add_repo` (owner `aureliosaraiva`, repo `orixas-fontes`, access `push`) **funcionou nesta sessão trabalhadora**; clone raso em `../orixas-fontes` e `scripts/acervo_sync.sh pull` (51 textos). Nenhum arquivo novo foi gerado no acervo (os três PDFs e textos já estavam lá), portanto não houve `acervo_sync.sh push`.
- Leitura integral dos três textos (`txt/<source_id>.txt`). As tabelas do anexo de Prandi 1995 saem embaralhadas no texto extraído; foram relidas com `pdftotext -layout` e, nas linhas ambíguas (correspondências jeje e banto de Exu, Oxum e Logun-Edé), com as coordenadas das palavras (`pdftotext -bbox`), para não trocar coluna de vodum por coluna de inquice.

| Fonte | Páginas impressas | Relação PDF × impressa | Licença |
|---|---|---|---|
| Prandi 1995, *Horizontes Antropológicos* 1(3) | 10–30 (texto 10–22; anexo 23–27) | impressa = PDF + 9 | CC BY 4.0 |
| Giumbelli & Lima, *Religião e Sociedade* 43(3) | 201–228 (São Luís: 215–220; conclusões 221–222) | impressa = PDF + 200 | CC BY-NC 4.0 |
| Noleto & Negrão, *Religião & Sociedade* 45(1), e450102 | 1–44 (numeração própria do artigo) | igual ao PDF até a p. 6; a partir do PDF 7, impressa = PDF + 1 (o PDF junta as pp. 6–7) | — |

Correções de catálogo (`observacoes`, sem trocar ids nem anos): o DOI impresso no PDF de Prandi é `10.1590/S0104-71831995000300002` (resolve a dúvida da PENDENCIAS §2; o pid `…000300010` segue sendo de outro artigo); o fascículo de Giumbelli & Lima é datado de **2023** (aprovado em 11/12/2023; o id mantém 2024); tradições das duas fontes de Iemanjá corrigidas para o que a leitura mostrou.

## 2. Registros

**161 registros `fichado`** (836 → 997 no total; 981 `fichado`, 16 `pre_fichamento`). Todos com página impressa e paráfrase própria.

| Fonte | Registros | Entidades |
|---|---:|---|
| Prandi 1995 | 138 | Exu, Ogum, Oxóssi, Ossaim, Oxumarê, Omolu, Xangô, Iansã, Obá, Oxum, Logunedé, Ewá, Iemanjá, Nanã, Oxalá (Oxaguiã/Oxalufã), Orí, Orum |
| Giumbelli & Lima 2024 | 12 | Iemanjá |
| Noleto & Negrão 2025 | 11 | Iemanjá (9), Oxum (1), Exu (1) |

Por atributo: domínios 25, sincretismo 16, elementos 15, cores 15, dia da semana 15, símbolos 15, equivalências 14, história do culto 12, **saudação 9** (antes havia só 2 no projeto), festas 5, iconografia 5, nomes 4, parentesco 4, hierarquia 3, funções 3, interpretação acadêmica 1.

### 2.1 Prandi 1995

- **Texto (pp. 10–22):** atributos "mais usuais" de nove orixás segundo os seguidores (pesquisa em 60 terreiros paulistas, nota 1): funções, domínios, sincretismo, saudações (Laroyê, Ogunhê, Okê arô, Atotô, Kaô kabiesile, Ora yeyê ô, Eparrei, Odoyá, Epa Babá), parentescos (Exu irmão de Ogum; Oxum e Iansã esposas de Xangô), a iconografia do transe de Oxalufã e Oxaguiã, a imagem de sereia e as estátuas de Iemanjá no litoral; Orí (orixá dono da cabeça e juntó; "cabeça ruim não tem orixá") e Orum (destino do orixá após o axexê). Como o autor fala de "candomblé" sem nação nessa seção, os registros levam `candomble_ketu` com nota de aproximação (o artigo toma o rito queto como referência e diz que os traços coincidem com Salvador, Rio e África).
- **Anexo "Atributos básicos dos orixás no candomblé (Nação queto)" (pp. 23–27):** para 14 orixás e as duas formas de Oxalá, um registro por coluna aproveitável: atribuição + patronagem (domínios), elemento natural + mítico, cores das roupas e das contas, dia da semana, objetos rituais, santo católico e correspondências jeje/banto.
- **Não fichado (decisão desta sessão; PENDENCIAS §3a):** animais sacrificiais, comidas favoritas e tabus dos filhos (regra dos retidos), números no jogo de búzios e composição dos assentamentos (fundamento), os estereótipos de personalidade dos filhos (não há atributo no esquema) e o panorama sociológico geral (nações, Umbanda × Candomblé, clientela), que não é afirmação sobre uma entidade da lista-mestra.
- **Leitura das colunas:** Exu tem na coluna "vodum jeje" Elegbara, Bara e Eleguá; Bara é o nome de Exu no Batuque (o próprio quadro diz) e Eleguá é nome cubano, por isso o mapa do grafo liga só Elegbara e os inquices (nota no exu-112). Logun-Edé: "Bosso Jara" está inteiro na coluna de voduns. Oxum: Aziritobosse, Navê e Navezuarina (voduns), Samba e Quissambo (inquices).

### 2.2 Giumbelli & Lima 2024

Só a parte de Iemanjá (São Luís). Iemanjá partilhada pelo Tambor de Mina (ao lado dos voduns), pela encantaria e pela Umbanda (no comando de entidades); a imagem pública difundida desde meados do século XX (mulher branca, próxima das imagens marianas) e as versões africanizadas (apoiadas em Salomão 2012, não lido); a estátua de Eduardo Sereno (feições negras e indígenas); a história das três imagens da Praia do Olho d'Água; a festa de 31/12 (desde os anos 1930) e de 2/2; as críticas das lideranças (praça pequena, esgoto, falta de assentamento, "escultura turística"); oferendas no pedestal; o ataque de 23/07/2023; a segunda imagem no Porto do Itaqui; a leitura comparativa dos autores. Tradições: `tambor_de_mina` e/ou `umbanda`, conforme o trecho. O assentamento é citado só pela definição genérica dos autores, sem rito.

### 2.3 Noleto & Negrão 2025

Festa de 2 de fevereiro na Playa Ramírez (Montevidéu); calendário público afroumbandista uruguaio (Iemanjá 2/2 e Oxum 8/12); descrição da festa (acampamento, tendas, flores, velas, frutas, barco azul-celeste e branco); federações que reúnem umbanda, batuque, quimbanda e candomblé; origem da festa nos anos 1960 (Constantino Rayol, relato de Mãe Susana Andrade); o Monumento a Iemanjá e suas **duas cronologias, lado a lado** (Intendencia: 1994; Massonnier 2015: 1988–1994–1998); a chegada do culto via Rio Grande do Sul a partir dos anos 1950; as **versões sobre a origem** (imprensa uruguaia: Nigéria direto; devotos e Mãe Susana: matriz afro-brasileira, com ritos próprios nas Salas de Nación); imagens nas tendas; Exu e a rua.

**Tradição nova?** As religiões "afroumbandistas" do Uruguai não têm tradição própria em `data/tradicoes.json`. Nesta sessão os registros ficaram como `umbanda` + `batuque_rs`, com `casa_ou_regiao` "Montevidéu (Uruguai)…" ou "Uruguai: …" e nota explicando. **Proposta** (PENDENCIAS §3a): criar `afroumbanda_uruguai` (grupo diáspora), com Noleto & Negrão pp. 10 e 23 e Prandi 1995 p. 12 como fontes iniciais, e retaguear os registros.

## 3. Grafo, fichas, itãs

- `conexoes_alvos.json`: 35 registros de parentesco/equivalência/sincretismo mapeados (2 sem aresta, por equivalerem a vodum de mesmo nome: ewa-015, nana-041); **21 nós novos** (inquices Bombogira, Aluviá, Incáci, Roximucumbe, Mutacalombo, Cafunã, Zázi, Bumburucema, Samba, Quissambo, Zambi; voduns Dã, Bessém, Queviosô, Aziritobosse, Navê; santos Santo Onofre, São Roque, São Miguel Arcanjo, Santa Lúcia, N. S. da Conceição Aparecida). Dã/Bessém, Queviosô e Aziritobosse ficaram separados de Dangbê, Quevioçô e Aziri por não haver fonte que os identifique (PENDENCIAS §3a). Arestas de qualidade: Oxaguiã → Menino Jesus; Oxalufã → Jesus Cristo, Liçá e Zambi.
- Grafo: 117 → **138 nós**, 150 → **179 arestas** (equivalência 79, sincretismo 58, parentesco 36); entidades equivalentes 53 → **68**; 0 avisos `sem_mapa`.
- Fichas: 26, **967 versões** (antes 806); divergências: 124 → **137 atributos**.
- `itans.json`: nenhuma mudança — as três fontes não narram itãs (a menção a Oxaguiã e o pilão entrou como domínio).

## 4. Capítulos

17 capítulos editados (`validar_capitulos.py --gerar`: 0 erros):

- **Iemanjá** (2 110 → 3 340 palavras): abertura; três subtítulos novos em "História do culto" (*As estátuas do litoral*; *São Luís, entre o Tambor de Mina, a encantaria e a Umbanda*; *Do Rio Grande do Sul ao Uruguai*, com as duas cronologias do monumento e as duas versões de origem lado a lado); domínios, cores, dia e símbolos do quadro queto; angola (correspondências do quadro); Tambor de Mina e Umbanda em São Luís; subseção nova **No Uruguai: Umbanda e Batuque**; sincretismo (Aparecida); leituras acadêmicas (Giumbelli & Lima; Noleto & Negrão); lacunas (Odoyá conferida em segunda fonte; Salomão 2012 e Massonnier 2015 como pendências).
- **Exu, Ogum, Oxóssi, Omolu, Xangô, Iansã, Oxum, Oxalá:** parágrafo novo em domínios (terreiros paulistas + quadro queto), saudação nas lacunas (deixou de ser lacuna), correspondências jeje/banto na subseção ketu, santos no sincretismo; Xangô e Iansã/Oxum com os casamentos; Oxum com a festa de 8/12 no Uruguai; Exu com Bara no Batuque e Exu na festa de Montevidéu.
- **Ossaim, Obá, Logunedé, Oxumarê, Nanã, Ewá:** domínios, cores, dia, símbolos e santo do quadro queto; as lacunas de sincretismo (Ossaim, Obá), elementos e dia (Logunedé, Ossaim, Ewá) foram reescritas como "vem de um único quadro". Ewá deixou de ser "sem domínios nem cores".
- **Orí e Orum:** juntó e o provérbio da cabeça; o axexê e o retorno ao Orum (sem detalhe ritual).

**Conferência manual.** Cada parágrafo novo foi relido ao lado dos registros citados. Ajustes: o parágrafo de dias da semana de Iemanjá teve as notas reagrupadas (o marcador novo cortava o trecho de Bahia/Opô Afonjá); em Oxumarê, a grafia Oxunmarê foi situada em Salvador para nomear a casa da versão divergente; "Rio Grande do Sul" foi acrescentado à paráfrase de iemanja-093 para sustentar o trecho do capítulo; as frases sobre a festa de Montevidéu dizem "afroumbandista" e a seção de tradições separa Umbanda e Batuque uruguaios do Candomblé.

## 5. Anti-cópia (texto integral, acervo `orixas-fontes`, 51 textos)

**0 erros.** 13 erros iniciais (8 palavras iguais ao quadro de Prandi e a uma frase de Noleto) e 8 em capítulos foram reescritos. Avisos "próximo" restantes ligados a estas fontes, mantidos e justificados:

| Campo | Trecho | Justificativa |
|---|---|---|
| exu-105.valor | "porrete fálico e tridentes de ferro" | lista de objetos (termos) |
| iansa-047, oxumare-036, oxala-074 (valor/paráfrase); capítulo Iansã | listas de cores do quadro | lista |
| xango-061 | "trovão e pedras (pedra de raio)" | termo do quadro |
| iemanja-075.parafrase | "Mãe d'Água, botos, cobras, sereias, marinheiros" | lista de encantados |
| iemanja-089.valor | "flores no Río de la Plata" | nome de lugar |
| capítulo Iemanjá | "na Praia do Olho d'Água" | nome de lugar |
| capítulo Iemanjá, Nanã | "a partir de meados do século"; "contas brancas rajadas de azul-cobalto" | expressão corrente; lista de cores |

Paráfrases do anexo que repetiam um mesmo molde entre registros (aviso de repetição interna) foram reescritas em moldes curtos, com o nome do orixá no meio.

## 6. Validação

`validar_fontes`, `validar_fichamento`, `divergencias` (137), `gerar_fichas` (0 avisos), `validar_fichas`, `anticopia` (0 erros), `validar_capitulos --gerar` (0 erros), `python3 -m unittest discover -s tests` (82 testes OK), build do site e `qa_site.py` (94 páginas, 967/967 versões, 26 capítulos com 610 parágrafos, 0 vazamentos do acervo): **ok**. Acessibilidade (`site/scripts/acessibilidade.cjs`): ver adendo no fim.

## 7. Pendências novas ou alteradas

- ✅ SciELO para Prandi 1995, Giumbelli & Lima e Noleto & Negrão (§1, §1b); ✅ LUME (dispensado); ✅ DOI de Prandi 1995 (§2).
- 🔴 §2: obras citadas pelas fontes e não lidas (Salomão 2012; Massonnier 2015; Anjos 2006; Segato 1998; Frigerio 2013 e 2021; Bem 2012).
- 🟡 §3a: tradição uruguaia; colunas não fichadas do quadro de Prandi; possíveis nós duplicados no grafo.

## 8. Sugestões

1. Decidir a tradição `afroumbanda_uruguai` e, se aprovada, retaguear os 11 registros de Noleto & Negrão e escrever a descrição com fonte.
2. Fichar Frigerio 2021 (Iemanjá na Argentina, "casi una Virgen del Mar") e Bahia 2018 (Iemanjá no Rio), citados por Noleto & Negrão, para ter festas de Iemanjá no Rio e na Argentina.
3. O revisor de tradição jeje/angola deve conferir o quadro de correspondências de Prandi, que é síntese do autor e não diz de que casas vem cada par.
