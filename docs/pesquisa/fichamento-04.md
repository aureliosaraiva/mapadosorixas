# Fase 1: fichamento nº 4 (três fontes que sustentavam `pre_fichamento`)

**Data:** 2026-10-31

Tarefa 4 do [`ESTADO.md`](../ESTADO.md): ler no original as três fontes recém-localizadas, confirmar ou corrigir os registros que dependiam delas e passá-los a `fichado`. Os PDFs foram baixados fora do repositório. No repo entram só metadados, páginas e paráfrases.

## O que foi lido

| Fonte | Acesso | Trechos lidos | Registros |
|---|---|---|---|
| Nogueira (2017), tese UFG, *Da África para o Brasil, de orixá a egum* (`ufg-2017-exu-umbanda`) | PDF no repositório UFG (410 p.) | resumo (p. 9), introdução (pp. 16–22), §3.3 (pp. 195–197), conclusão (pp. 382–385) | exu-034 (corrigido) + exu-062, exu-063, exu-064 |
| Pinheiro (2011), dissertação UFPB, *São Jorge: performance nômade…* (`ufpb-2011-sao-jorge`) | PDF no repositório UFPB | §1.5 (pp. 28–40), cap. 2 (p. 41), §3.4 (pp. 61–72), §4.1 (pp. 83–84) | ogum-006 (corrigido) + ogum-030 a ogum-033 |
| Costa (2007), *Afro-Ásia* n. 36, pp. 199–227 (`costa-2007-xango-pe`) | PDF no portal de periódicos da UFBA (o Redalyc continua dando 403) | integral | xango-005 (confirmado) |

Paginação: na tese de Nogueira, a página do PDF coincide com a impressa. Na dissertação de Pinheiro, página impressa = página do PDF − 2. Nos registros vale sempre a página impressa.

## Registros que estavam em `pre_fichamento`

| Registro | Resultado | O que mudou |
|---|---|---|
| exu-034 | **confirmado e ampliado** | p. 9 (resumo) e pp. 196, 385. A tese diz que na Umbanda **e na Quimbanda** Exu passa de orixá a egum (espírito de morto), e que esse Exu-egum convive com o Exu-orixá dos candomblés mais tradicionais. Tradição: só `umbanda` (o autor inclui a Quimbanda no campo umbandista, p. 16, nota 2). |
| ogum-006 | **corrigido** | pp. 34, 36, 83. O sincretismo com São Jorge está documentado em casas de **Umbanda** de João Pessoa. Saiu `candomble_ketu`: a fonte não fala de Ketu. A casa de Candomblé estudada (Kwe Ceja Azirin, bairro de Valentina) é de nação **Jeje** (p. 39), e o texto não diz que a imagem de São Jorge está no altar dela. A p. 34 fala também em "gongás de iniciados", sem indicar nação. |
| xango-005 | **confirmado** | pp. 199–200. Em Pernambuco, "xangô" nomeia a religião, o orixá do trovão, o terreiro e as festas (toques). Região: Pernambuco. Na nota: segundo a autora, o termo "candomblé" também passou a ser usado lá, porque "xangô" ficou estigmatizado pela repressão dos anos 1930 (p. 199, n. 1). |

Nenhum registro foi removido.

## Registros novos (todos `fichado`, com página)

| Registro | Atributo | Valor resumido | Tradição | Pág. |
|---|---|---|---|---|
| exu-062 | interpretacao_academica | três estatutos de Exu: orixá (África e alguns candomblés), escravo dos orixás (maioria dos candomblés), egum (Umbanda/Quimbanda) | ioruba_nigeria, candomble_ketu, umbanda | p. 22, n. 5 |
| exu-063 | historia_culto | Exu-egum formado no início do séc. XX, no trânsito entre Bahia, macumbas cariocas e espiritismo; já é entidade na 1ª obra umbandista (Leal de Souza, 1933) | umbanda | pp. 384–385 |
| exu-064 | funcoes | guardião do terreiro (assentamento na entrada), segundo Landes; 2ª mão via Nogueira | candomble_ketu | p. 384 |
| ogum-030 | cores | verde e vermelho nas festas de Ogum; azul quase ausente (Umbanda, João Pessoa) | umbanda | pp. 69–70 |
| ogum-031 | cores | azul-marinho e verde no candomblé baiano (nagô, jeje, ketu), segundo o autor | candomble_ketu, candomble_jeje | pp. 69–70 |
| ogum-032 | simbolos | capacete e espada em estilo romano, vindos da iconografia de São Jorge | umbanda | p. 71 |
| ogum-033 | qualidades | sete legiões da linha de Ogum na Umbanda (Ortiz, via Pinheiro) | umbanda | p. 83 |

**Cuidados:**
- exu-062: a tese diz "candomblés" sem indicar nação. `candomble_ketu` é uma aproximação, anotada no registro para a revisão conferir.
- exu-063 é hipótese do autor ("é provável", "teria se formado") e foi registrada assim.
- ogum-031 é afirmação do autor sem fonte explícita no trecho, numa fonte de nível C.
- exu-064 e ogum-033 são de 2ª mão (`via_source_id`). Para isso, Landes (1947) e Ortiz (1978) foram conferidos na Open Library e passaram a `conferido_web`.
- Não fichei a comida de Ogum na Umbanda (feijoada, p. 72): alimentos rituais ficam fora até decisão do conselho.

## Candomblé × Umbanda

As três leituras reforçam a distinção:

- **Exu:** é orixá no Candomblé e egum na Umbanda/Quimbanda (exu-034, exu-062).
- **Ogum:** em João Pessoa, a Umbanda usa vermelho, verde e iconografia europeia (ogum-030, ogum-032). Segundo Pinheiro, o candomblé baiano usa azul-marinho e verde (ogum-031).
- **Xangô:** em Pernambuco, "xangô" nomeia uma religião de culto aos orixás distinta da Umbanda, embora polícia e imprensa tenham confundido as duas (xango-005).

## Divergências novas

| Orixá | Tema | Versões |
|---|---|---|
| Ogum | cores | azul-escuro (Ketu) × verde e vermelho (nagôs) (Chiousse, p. 266) × verde e vermelho, quase sem azul (Umbanda, João Pessoa; Pinheiro, pp. 69–70) × azul-marinho e verde (candomblé baiano, segundo Pinheiro) |

Total: 32 atributos com versões divergentes (eram 31).

## Grafo

ogum-006 entrou em `data/conexoes_alvos.json` (sincretismo → `santo:sao-jorge`). A aresta Ogum–São Jorge já existia, então o número de arestas não mudou (43). Agora ela tem mais uma fonte.

## Validação

`validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas`, `validar_fichas` e `anticopia` deram OK. O anti-cópia também rodou com `ANTICOPIA_REFS` apontando para o texto das três fontes, fora do repo: nenhuma sequência de 8 palavras idênticas.
