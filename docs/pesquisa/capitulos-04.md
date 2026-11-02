# Capítulos narrativos — sessão cap04 (2026-11-02)

Sessão trabalhadora coordenada pela orquestradora: capítulos da **cosmologia e da hierarquia**, no formato e no estilo dos anteriores ([guia](../capitulos-guia.md), [cap01](capitulos-01.md), [cap03](capitulos-03.md)). Arquivos tocados: só `data/capitulos/{olodumare,orum,aie,ori,odudua,olokun,egungun}.*`, este relatório, a linha de capítulos do [`ESTADO.md`](../ESTADO.md) e o §3e de [`PENDENCIAS.md`](PENDENCIAS.md). Nenhum fichamento, itã, validador, catálogo ou arquivo de `site/` foi editado.

## 1. Os sete capítulos

| Capítulo | Parágrafos | Palavras | Registros citados | Notas | Registros próprios fora do texto |
|---|---:|---:|---:|---:|---|
| Olodumare | 20 | ~1 690 | 30 | 35 | nenhum (19/19) |
| Orum | 14 | ~960 | 19 | 25 | nenhum (9/9) |
| Aiê | 12 | ~580 | 7 | 21 | nenhum (3/3) |
| Orí | 14 | ~1 040 | 11 | 28 | nenhum (10/10) |
| Odudua | 17 | ~1 410 | 24 | 32 | nenhum (19/19) |
| Olokun | 14 | ~780 | 10 | 24 | nenhum (7/7) |
| Egungun | 18 | ~1 410 | 20 | 36 | nenhum (15/15) |

"Registros citados" inclui os de outras entidades que tocam a cosmologia: `oxala-003/018/031/040`, `orunmila-002`, `orum-006` e `olokun-005` em Olodumare; `exu-011/078`, `egungun-009/015`, `oxala-040`, `olokun-007` e `olodumare-002/017` em Orum; `exu-011`, `orum-008/009` e `egungun-015` em Aiê; `odudua-016` em Orí; `oxala-010/031`, `olokun-002/007` e `iemanja-060` em Odudua; `odudua-007`, `olodumare-018` e `iemanja-060` em Olokun; `orum-007`, `iansa-006/036`, `omolu-040` e `exu-034` em Egungun. Só registros `fichado`; nenhum retido (nenhuma das entidades tem retidos).

**Títulos de seção adaptados.** O slug das seções é o fixo do guia; o título exibido mudou onde o atributo de orixá não cabe: "O lugar no cosmos" (Olodumare), "Um mundo de cima" (Orum), "O mundo de baixo" (Aiê), "A terra e o casal primordial" (Odudua), "O mar e as águas" (Olokun), "Os ancestrais entre os vivos" (Egungun). Seções sem material (sincretismo de quase todos, Lucumí, Umbanda) ficam com uma frase e `{{lacuna}}`, sem enchimento.

## 2. Não escritos, e por quê

- **Iyami — não escrito; decisão para o conselho.** Os 4 registros (`iyami-001`–`004`) estão fichados, mas cada um traz na nota "registro a confirmar pelo conselho" (PENDENCIAS §3b, "Lote C — decisões para o conselho", item a), e a entidade é `sensivel`. A página do capítulo (`site/src/pages/orixas/[id]/capitulo.astro`) não exibe o aviso de tema sensível que a ficha e o catálogo exibem; um capítulo daria aos registros mais visibilidade do que a ficha com aviso. Pela regra "na dúvida, deixar de fora", o capítulo espera: (a) o conselho confirmar os 4 registros; (b) a página do capítulo mostrar o aviso `aviso-sensivel` quando a entidade for sensível. Nenhum dado de Iyami entrou nos outros capítulos (nem em Egungun, onde `iyami-003` faria o paralelo com as sociedades femininas).
- **Orixás funfun — sem capítulo:** a entidade continua `sem_fichamento` (nenhuma fonte lida usa o termo). O capítulo de Odudua diz isso nas lacunas, com as pendências "Orixás funfun: seguem sem fonte" e "Rótulos provisórios de `grupo`".
- **`cosmologia.md` (visão de conjunto) — não escrito; proposta para a orquestradora.** O validador exige que `orixa` seja um id da lista-mestra com ficha gerada (`validar_capitulos.py`, l. 259–265), e a página só existe em `/orixas/<id>/capitulo/`. Proposta: (1) aceitar no validador um capítulo de tipo "panorama" (`tipo: panorama` no frontmatter, id livre, sem a exigência de ficha, seções próprias — p. ex. `hierarquia`, `planos`, `ancestrais`, `lacunas`) e (2) uma rota `/cosmologia/capitulo/` ou um bloco de texto na página `/cosmologia/` atual. O conteúdo já existe disperso nos 7 capítulos (Olodumare no topo, Orum e Aiê, Orí na pessoa, Egungun nos ancestrais), e o panorama seria uma costura curta, com links para eles.

## 3. Estilo e regras de conteúdo

- **Sem citação no corpo.** Autores só em "Leituras acadêmicas" (Ellis, Farrow, Dennett, Ogungbemi, Bewaji, Idowu/Crowther/Mbiti via Ogungbemi e Bewaji, Carvalho et al., Zacharias, Bastide, Jock, Johnson, Fámúlẹ̀) e nas lacunas (obras pendentes: Idowu 1962, Beniste 1997, J. E. dos Santos 1976). O validador acusou "Stephen" (prenome ausente do registro) em Odudua: ficou "o missionário Farrow".
- **Fontes coloniais.** Ellis 1894, Dennett 1910 e Farrow 1926 aparecem sempre como "relato de 1894, escrito por um oficial britânico", "administrador colonial", "missionário anglicano", e os capítulos dizem quando eles divergem entre si (Olodumare: deus da natureza × monoteísmo primitivo × derivação de Jakuta; Orum: dois céus × terra dos mortos no subsolo; Olokun: filho de Yemaja × deusa esposa de Oduduwa). Olokun, cuja base é quase toda colonial, avisa isso na abertura. Johnson 1921 (B) é tratado como "historiador e clérigo iorubá", sem a marca de documento colonial, mas com a ressalva de leitura monoteísta em Leituras.
- **Versões por tradição/região.** O validador cobrou o nome da tradição ou casa em 11 parágrafos (hierarquia de Olodumare, Odudua e Orum; origem e itãs de Odudua; parentesco e itãs de Olokun; símbolos de Orí; festas e hierarquia de Egungun). Um achado útil: "Oyó" e "Ifẹ̀" têm 3 letras normalizadas e não contam para a checagem de divergência (só palavras de 4+ letras); foi preciso nomear "iorubá", "Lagos", "litoral", "mitologia de Ifẹ̀" ou "historiadores da corte".
- **Candomblé × Umbanda.** Todo capítulo tem a subseção "Umbanda", que a chama de outra religião. Registro umbandista só em Olodumare (`olodumare-019`, campo misto de Salvador/SP, e `oxala-018`, sincretismo Olorum = Deus Pai) e em Egungun (`exu-034`: na Umbanda, egum é espírito de morto que se manifesta, e Exu passa a essa categoria), em que o capítulo distingue esse egum do Egungun ancestral do Candomblé, que aparece sem transe (`egungun-013`). Nas demais, `{{lacuna:…@umbanda}}`.
- **Egungun sem fundamento.** Ficaram fora: os cargos sacerdotais (o nome do sacerdócio dos Egun em `egungun-013` foi omitido de propósito), objetos, etapas rituais e o pacto que o mito de `egungun-015` funda (a própria nota do registro diz que não foi fichado). O capítulo diz isso na abertura e nas lacunas, com a pendência "Lote C — decisões para o conselho".
- **"O que as fontes não dizem"** em todos: atributos de orixá que não se aplicam a planos do cosmos (cores, dia, saudação) e as obras que faltam (Idowu, Beniste, J. E. dos Santos, Akande 2019, Olokun do Benim).

## 4. Conferência manual

Cada parágrafo foi escrito com o despejo dos registros ao lado e relido. Ajustes além do que o validador pegou:

- Orí: "Esse relato de época é a base de quase tudo o que se escreveu depois sobre o tema em inglês" — inferência sem registro; passou a "foi retomado quase sem mudança por um missionário anglicano em 1926" (`ori-005`).
- Olodumare: a etimologia de Johnson ("aquele que não se pode ultrapassar") foi reescrita como "terminação que indicaria o que não admite ser excedido", mais perto do registro e sem repetir o valor.
- Olodumare: "São relatos de época" — o "São" capitalizado vira nome para a heurística (mesma armadilha da cap03); reescrito.
- Orum e Olodumare: "século XX"/"século XIX" acusados pela heurística quando o registro não traz o numeral; trocados por anos que estão no catálogo (1894, 1926) ou por "no começo do século passado".
- Odudua: "o relato de 1894, o bispo Crowther e os informantes de Ilobe" — o trecho não citava Ellis; ficou "outras fontes, o bispo Crowther entre elas".
- Olokun: "nem de sua presença no Brasil" → "nos terreiros" (o trecho não cita registro brasileiro).

## 5. Validadores e anti-cópia

| Verificação | Resultado |
|---|---|
| `validar_capitulos.py --gerar` | 25 capítulos, **0 erros**; 8 avisos de 6–7 palavras nos capítulos novos, todos justificados abaixo |
| `baixar_refs.py` + `anticopia.py` (acervo `orixas-fontes`, clonado nesta sessão) | **0 erros**; 1 aviso "próximo" num capítulo novo (Odudua, "o céu e Odudua a terra", Bastide), reescrito; 0 depois |
| `validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas`, `validar_fichas` | OK (sem mudança de dados) |
| build do site + `qa_site.py` | 93 páginas, 25 capítulos (546 parágrafos conferidos), 0 vazamentos do acervo; OK |
| `site/scripts/acessibilidade.cjs` | nenhuma violação grave |
| screenshots 390 px | `/orixas/olodumare/capitulo/` e `/orixas/egungun/capitulo/` renderizam; o índice `/livro/` lista os novos |

Todas as obras citadas pelos 7 capítulos estão no acervo (`ellis-1894`, `dennett-1910`, `farrow-1926`, `johnson-1921`, `ogungbemi-2021`, `bewaji-1998`, `akin-otiko-2024`, `jock-2020`, `famule-2021`, `carvalho-2019`, `zacharias-2010`, `bastide-1958`, `chiousse-1995`, `prandi-2001-exu-diabo`, `vallier-2011`, `halloy-2005`), exceto `cabrera-1954-monte`, lido via Bastide (`bastide-1958` está no acervo).

Avisos de 6–7 palavras mantidos (todos expressão de nome, glosa ou data):

- Egungun: "o que traz estabilidade, união e paz" (glosa do nome, `egungun-008`); "são aparições e os orixás, manifestações" (fórmula da casa baiana); "2 de novembro, Dia de Finados" (data); "uma imagem de Iansã de Balé" (nome).
- Odudua: "Iya agbe, a mãe que recebe" e "o que existe por si" (tradução de título e de nome); "Oduduwa, seu irmão mais novo" (parentesco).
- Olodumare: "a noção de um Ser Supremo" (termo técnico).

## 6. Para a orquestradora

1. **Iyami:** capítulo à espera do conselho e do aviso de tema sensível na página do capítulo (§2).
2. **Panorama `cosmologia.md`:** precisa de suporte no validador e no site (§2); proposta de formato acima.
3. **Página do capítulo:** exibir `aviso-sensivel` quando `entidade.sensivel` for verdadeiro (hoje só a ficha, o catálogo e a cosmologia exibem).
4. **Validador:** palavras de 3 letras (Oyó, Ifẹ̀, Ilê) não contam como nome de casa na checagem de divergência; vale considerar uma lista de topônimos curtos aceitos.
5. **Revisão do conselho:** os 7 capítulos são `rascunho`; atenção especial a Egungun (limite do que é público) e às leituras coloniais de Olodumare, Orum e Olokun.
