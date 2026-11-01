# Capítulos narrativos — sessão cap01 (2026-11-01)

Pedido do autor, repassado pela orquestradora: **uma página por orixá com texto narrativo, como capítulo de livro**, dentro das regras de conteúdo do projeto. Durante a sessão, a orquestradora repassou um ajuste de estilo do autor (sem citação no corpo do texto; atribuição pela tradição, casa ou região; notas agrupadas no rodapé). Os cinco capítulos foram reescritos nesse estilo e o validador passou a cobrar a regra. Formato e regras: [`docs/capitulos-guia.md`](../capitulos-guia.md).

## 1. O que foi feito

| Peça | Arquivo |
|---|---|
| Formato (Markdown + frontmatter, marcadores `{{ref}}`, `{{lacuna}}`, `{{pendencia}}`, links `ita:`/`orixa:`/`glossario:`/`tradicao:`/`grafo:`) | `data/capitulos/<id>.md`, `scripts/capitulos.py` |
| JSON gerado para o site (notas agrupadas por grupo de marcadores) | `data/capitulos/<id>.json`, `schemas/capitulo.schema.json` |
| Validador (12 regras, ver guia §4) | `scripts/validar_capitulos.py` (`--gerar` regenera o JSON) |
| Testes (18: um caso válido e 16 violações, mais o formato das notas) | `tests/test_capitulos.py` |
| Anti-cópia passa a conferir cada trecho dos capítulos com as fontes dos registros citados | `scripts/anticopia.py` |
| Página do capítulo, índice "Livro", item no menu, link na ficha | `site/src/pages/orixas/[id]/capitulo.astro`, `site/src/pages/livro.astro`, `site/src/lib/capitulos.js` |
| QA do site §12 (parágrafos, chamadas e notas idênticos ao JSON; registro publicável com autor, ano, página e link; Livro e ficha) | `scripts/qa_site.py` |
| CI: novo passo "Capítulos narrativos" | `.github/workflows/validar.yml` |
| Guia | `docs/capitulos-guia.md` |
| Screenshots | `docs/screenshots/livro*.png`, `capitulo-*.png` |

Ajustes colaterais: o nome curto de obra organizada mostrava "(org.)" no lugar do sobrenome (ex.: "(org.) (1989)" para Barnes); `sobrenome()` em `site/src/lib/dados.js` passou a ignorar "(org.)", o que corrige também as notas das fichas. `Selo.astro` aceita um texto próprio. Os testes ponta a ponta de revisão e do modelo 2 removem os capítulos da cópia temporária (os dados sintéticos tornam registros citados inexistentes ou retidos); o de revisão antes confirma que o validador de capítulos acusa o registro marcado `nao_publicar`.

## 2. Os cinco capítulos

| Capítulo | Parágrafos | Palavras | Registros citados | Notas | Registros publicáveis do orixá fora do texto |
|---|---:|---:|---:|---:|---|
| Exu | 36 | ~3 490 | 108 | 57 | `exu-052` (animais de sacrifício: a nota do registro pede para não detalhar ritos) |
| Ogum | 28 | ~2 470 | 68 | 36 | nenhum |
| Oxóssi | 22 | ~1 590 | 43 | 29 | nenhum |
| Xangô | 29 | ~2 250 | 59 | 44 | nenhum |
| Iemanjá | 25 | ~2 050 | 63 | 39 | nenhum |

"Registros citados" inclui os de outras entidades que tocam o orixá (itãs e parentescos: `oxum-029`, `oxala-029`, `logunede-026`, `odudua-019`, `olodumare-013`, `ibeji-021` etc.). A extensão acompanha o material: Oxóssi, com 32 registros publicáveis, tem menos da metade de Exu, com 102. Tabus e alimentos retidos (`exu-012`, `oxossi-018`) não entram; o validador recusa citá-los, e uma `{{lacuna:tabus}}` de Exu seria falsa, porque o registro existe, só está retido.

**Registros novos durante a sessão.** O `git pull` trouxe 25 registros dos 5 orixás fichados por outra sessão (Halloy pp. 276–277 e 323; Toutain pp. 41–174; Chiousse pp. 237–266; Saraiva 2017). O validador acusou na hora uma lacuna que tinha deixado de ser verdadeira ("funções" de Xangô, agora com `xango-054`). Os 25 foram incorporados.

## 3. Conferência manual e o que a heurística pegou

Cada parágrafo foi escrito com o despejo dos registros ao lado (valor, paráfrase, nota, casa, fonte e confiabilidade) e relido contra eles. A heurística (nomes próprios, números, dias e cores do trecho precisam estar nos registros citados) acusou erros reais da redação:

- **prenomes errados escritos de memória**: "Alexandre Pinheiro" (é Roncalli Dantas Pinheiro), "Luiz Cerqueira" (é Hildebrando Almeida Cerqueira); prenomes de autores de obras pendentes ("Olga", "Yeda", "Rita") que não estão nos registros;
- **datas e épocas sem apoio**: "anos 1940 e 1950" para Bastide, "século XX" para Carneiro, "anos 1990" (o registro diz "até 1993"), "Atlântico";
- **lugar não citado no trecho**: "Bahia" num trecho cujo registro diz "Salvador (BA)", "São Paulo" num itã sem casa registrada.

Também se ajustou à mão:

- a abertura de Iemanjá dizia "ligada a um rio": a origem fluvial aparece só na nota de um registro, não numa paráfrase fichada, e saiu do texto;
- "nenhum orixá teria mais poder que Iemanjá" é uma opinião de Verger (`iemanja-036`), e não das tradições: o texto passou a dizer "há também quem diga";
- a abertura de Ogum falava do lugar do assentamento sem citar `ogum-039`, e a referência foi acrescentada;
- no mito do gorro de Exu, as versões ficaram atribuídas a "candomblés brasileiros" e à "Nigéria", com o odu só na versão que o registra.

## 4. Divergências, Candomblé × Umbanda e fontes coloniais

- Nenhum aviso de "divergência narrada pela metade": em todos os atributos divergentes dos 5 orixás, as versões citadas aparecem juntas, cada uma com sua tradição, casa ou região (o validador confere isso por versão).
- Debates acadêmicos com nomes de pesquisadores ficam só em "Leituras acadêmicas": a origem de Xangô (rei divinizado nos terreiros × Capo Chichi e Akinyemi × Idowu), a demonização de Exu (Prandi, Verger, Bastide, Costa, Vallier, Bewaji), o trickster (Silva × Vallier) e Ogum lavrador (Verger × Castillo).
- Cada capítulo tem uma subseção "Umbanda" que a apresenta como outra religião. Onde o fichamento não tem registro próprio da Umbanda (Oxóssi, Xangô), o capítulo diz isso com `{{lacuna:…@umbanda}}`.
- Documentos de confiabilidade C anteriores a 1950 (Ellis 1894, Baudin 1884, Bowen 1857, Pommegorge 1789, Burton 1863, Frobenius 1912) aparecem no texto como "relatos de missionários do século XIX", "um documento de 1894, escrito por um oficial britânico…" ou "documento de época", e o nome fica na nota. A bibliografia de cada capítulo marca as fontes C.

## 5. Anti-cópia

- **Contra o fichamento** (validador): 0 sequências de 8+ palavras. Restam 103 avisos de 6–7 palavras contra as paráfrases do próprio projeto, quase todos nomes, listas, datas e expressões como "pai de santo da nação Omolocô", "nos xangôs do Recife e de", "23 de abril, dia de São Jorge". Na redação, foram reescritos cerca de 150 trechos que repetiam 8+ palavras das paráfrases.
- **Contra o texto integral** (`baixar_refs.py --destino /tmp/refs`, 45 obras baixadas; `ANTICOPIA_REFS=/tmp/refs/txt`): **0 erros** no projeto todo. A 1ª passada deu 1 erro num capítulo (Ogum: "também nos reinos vizinhos de Ijexá e Ondo", 8 palavras iguais a Castillo 2022), reescrito. Dos 19 avisos "próximo" dos capítulos, 7 foram reescritos e 12 ficam, todos de classe C:

| Trecho (6–7 palavras) | Fonte | Por que fica |
|---|---|---|
| "na casa das minas de são luís" | M. Ferretti 2020 | nome de casa e cidade |
| "de tambor de mina do maranhão" (×2) | S. Ferretti 2011 | nome de tradição e estado |
| "de iré no reino de ekiti" | Castillo 2022 | topônimos |
| "no pátio da casa de iemanjá" | Blass 2007 | nome de lugar (a casa no Rio Vermelho) |
| "mito do caçador de uma flecha só" / "o caçador de uma flecha só" | Souza 2020 | título do itã e epíteto corrente |
| "no primeiro quartel do século xx" | Prandi 2001 | expressão de data |
| "o azul marinho e o verde" | Pinheiro 2011 | lista de cores |
| "a segunda feira é o dia" | Bastide 1958 | expressão corrente |
| "entre o criador e os voduns" | Ferreira Saraiva 2017 | termos técnicos |
| "que chefia a linha da mata" | Ferreira Saraiva 2017 | termo técnico ("linha da mata") |

Das 32 obras lidas que os capítulos citam, 3 ficaram sem texto para a comparação: Pitta 2011 (erro de proxy), Santos 2023 (erro de SSL) e Ogungbemi 2021 (PDF sem camada de texto). Foram para [PENDENCIAS](PENDENCIAS.md).

## 6. Verificações finais

`validar_fontes`, `validar_fichamento`, `divergencias` (124), `gerar_fichas`, `validar_fichas`, `validar_capitulos` (0 erros), `anticopia` (0 erros, com e sem referências); 66 testes unitários; e2e revisão e e2e modelo 2 ok; build (73 páginas); `qa_site.py` ok (5 capítulos, 140 parágrafos conferidos; teste de adulteração acusado); `acessibilidade.cjs` sem violação grave (todas as páginas, 2 larguras).

## 7. Próximos passos sugeridos

1. Capítulos dos demais orixás com ficha (Oxum, Iansã, Oxalá, Omolu, Nanã, Oxumarê, Ossaim, Logunedé, Obá, Ewá, Ibeji, Iroko e as entidades cosmológicas), em lotes de 3 a 5 por sessão, seguindo o guia §5. Ewá (8 registros) e Iroko (12) talvez rendam só um capítulo curto ou devam esperar exemplar.
2. A cada lote de fichamento novo dos 5 orixás, rodar `validar_capitulos.py`: lacuna que deixa de ser verdadeira vira erro, e o registro novo precisa entrar no texto.
3. Levar os capítulos ao conselho junto com as fichas: o capítulo só deixa o rascunho quando todos os registros citados estiverem `revisado`.
4. Versões es/en dos capítulos ficam para a fase de idiomas.
