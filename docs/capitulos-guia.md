# Guia dos capítulos narrativos

Pedido do autor (sessão cap01, 2026-11-01): **uma página por orixá com texto corrido, como capítulo de livro**, dentro das regras de conteúdo do projeto. O capítulo não traz informação nova: reconta, em prosa, o que já está no fichamento, e cada trecho remete a registros dele.

- Fonte do texto: `data/capitulos/<id>.md` (editado à mão).
- JSON gerado, lido pelo site: `data/capitulos/<id>.json` (`python3 scripts/validar_capitulos.py --gerar`; esquema `schemas/capitulo.schema.json`). Não editar o JSON.
- Página: `/orixas/<id>/capitulo/` (com o aviso de tema sensível quando a entidade é `sensivel`, como na ficha); índice: `/livro/`; a ficha linka para o capítulo.
- Validador: `scripts/validar_capitulos.py` (também no CI e nos testes `tests/test_capitulos.py`); `scripts/anticopia.py` confere os trechos dos capítulos; `scripts/qa_site.py` §12 confere o HTML contra o JSON.

## 1. Formato do arquivo

```markdown
---
orixa: ogum
titulo: Ogum, o ferro, a guerra e os caminhos
status: rascunho
atualizado: 2026-11-01
---

Parágrafo de abertura (opcional) ... {{ref:ogum-036,ogum-053}}

## Nomes e origem {#nomes-e-origem}

Texto corrido ... {{ref:ogum-049,ogum-050}}

### Subtítulo opcional

Texto com [link para o itã](ita:ita-004) ... {{ref:ogum-047}}
```

- Blocos separados por linha em branco. `## Título {#slug}` abre seção; `### Título` abre subtítulo; o resto é parágrafo. Itálico: `*texto*`.
- `status`: `rascunho` (padrão) ou `revisado` (só quando **todos** os registros citados estiverem `revisado`).
- Seções, nesta ordem, todas obrigatórias (o título exibido pode mudar; o slug, não):

| slug | conteúdo |
|---|---|
| `nomes-e-origem` | nomes por nação e língua, etimologias, origem africana |
| `historia-do-culto` | África, travessia, Brasil, Cuba; documentos históricos e etnografia |
| `dominios-e-simbolos` | domínios, funções, elementos, símbolos, cores, dias, festas |
| `mitos` | itãs recontados, com a casa ou tradição de cada versão e link para `/itans/` |
| `tradicoes` | o orixá em cada tradição (Ketu, Jeje, Angola, Batuque, Xangô do Recife, Mina, **Umbanda à parte**, Lucumí), com `###` por tradição |
| `sincretismo` | santos católicos, por casa ou região |
| `leituras-academicas` | debates entre pesquisadores (único lugar onde se nomeia autor no texto) |
| `lacunas` | "O que as fontes não dizem": o que falta e por quê |

A seção "Fontes" não se escreve: o site gera as notas e a lista de fontes citadas.

## 2. Marcadores

Todo trecho de texto termina num marcador. Um marcador cobre o texto desde o marcador anterior (ou o início do parágrafo); marcadores vizinhos viram **uma** nota de rodapé.

| Marcador | Significa | O validador confere |
|---|---|---|
| `{{ref:id1,id2}}` | registros do fichamento que sustentam o trecho | existem, estão `fichado`/`revisado`, não estão retidos (tabus, alimentos, parecer `nao_publicar`) |
| `{{lacuna:atributo}}` ou `{{lacuna:atributo@tradicao}}` | o fichamento não tem registro desse atributo (nessa tradição) | que de fato não há registro `fichado`/`revisado` (um registro retido também invalida a lacuna) |
| `{{pendencia:texto}}` | obra bloqueada ou que depende de exemplar | que o texto está em `docs/pesquisa/PENDENCIAS.md` |

Links: `[rótulo](ita:ita-006)`, `(orixa:ogum)`, `(glossario:pade)`, `(tradicao:candomble_jeje)`, `(grafo:ogum)`, `(capitulo:ori)` (outro capítulo de orixá/entidade); o validador confere que o alvo existe e está publicado.

### Capítulo-panorama (sessão cap05)

Um panorama costura vários capítulos sobre um tema (o primeiro é `data/capitulos/cosmologia.md`). Mesmas regras de texto, marcadores, notas e estilo; muda o seguinte:

- Frontmatter: `tipo: panorama` e `id: <id>` (igual ao nome do arquivo, só minúsculas e `_`, e **não** pode ser id da lista-mestra) no lugar de `orixa`; não exige ficha.
- Seções, nesta ordem, todas obrigatórias: `hierarquia`, `planos-do-mundo`, `a-pessoa` (Orí), `ancestrais`, `lacunas`.
- Sem `{{lacuna:…}}` (a lacuna é por entidade): o que falta vai em `{{pendencia:…}}` ou no registro que diz a ausência.
- A distinção Candomblé × Umbanda vale para o texto todo (não há seção de tradições).
- Página: `/<id>/capitulo/` (ex.: `/cosmologia/capitulo/`); o Livro lista os panoramas antes dos capítulos; `/cosmologia/` linka para o seu; o capítulo que um panorama linka mostra o panorama em "Ver também".

## 3. Estilo (diretrizes do autor, repassadas pela orquestradora em 2026-11-01)

1. **Sem citação no corpo do texto.** Nada de "Segundo Fulano (ano)…" ou "Para Bastide…" no meio da narrativa: o texto flui como capítulo de livro. As referências ficam no rodapé, com marcadores discretos (número sobrescrito), **agrupados no fim da frase ou do parágrafo**, e não um após cada oração. A nota lista autor, ano, página e link para a bibliografia, e pode agrupar vários registros.
2. **Versões divergentes se atribuem pela tradição, casa ou região** ("na Bahia…", "no Batuque de Porto Alegre…", "em Cuba…"), não pelo autor; o autor fica na nota. Exceção: quando o próprio debate acadêmico é o assunto (seção `leituras-academicas`), o pesquisador pode ser nomeado uma vez, com sobriedade. Obras pendentes também podem ser nomeadas na seção `lacunas`.
3. **Fontes coloniais e missionárias** são sinalizadas no texto de forma natural ("relatos de missionários do século XIX descreviam…", "um documento de 1894, escrito por um oficial britânico…"); autor e detalhes ficam na nota.
4. **O rigor não muda:** cada parágrafo continua vinculado a registros do fichamento, sem cópia, com divergências lado a lado e Candomblé distinto de Umbanda.

Outras regras de redação:

- Narrativo, respeitoso e acessível; extensão proporcional ao material (sem encher: Oxóssi, com 34 registros, tem metade do tamanho de Exu, com 94).
- Só o que está no fichamento. Ao juntar registros num parágrafo, não somar inferências que nenhum deles faz.
- Divergências: as versões aparecem juntas, cada uma com sua tradição ou casa; nunca "a versão correta", "na verdade", "de fato", "sem dúvida" (o validador recusa).
- Candomblé × Umbanda: a seção de tradições tem uma subseção própria para a Umbanda, que é dita "outra religião, e não uma nação do Candomblé" quando o orixá tem registro umbandista.
- Lacunas ditas com honestidade: saudações sem registro, itãs que dependem de Prandi e Verger, nomes angola sem fonte etc.
- Não repetir as paráfrases do fichamento: o capítulo é uma redação nova. Sequência de 8+ palavras iguais a uma paráfrase, valor ou nota é erro; 6–7 é aviso (aceitável para nomes, listas, datas e expressões correntes).
- Fontes de confiabilidade C antigas (antes de 1950) e outras fontes C: ler com cautela; a bibliografia do capítulo as marca.

## 4. O que o validador confere

1. Formato, frontmatter, seções obrigatórias na ordem, `orixa` com ficha gerada.
2. Todo parágrafo tem marcador e nenhum trecho fica sem marcador no fim.
3. Referências, lacunas, pendências e links válidos (tabela acima).
4. **Heurística de sustentação** (palavras comparadas sem diacríticos: NFD, marcas `Mn` removidas sem perder letras, de modo que "Éfọ̀n" vale "efon", e não "efo"): nomes próprios, números, dias da semana e cores de cada trecho aparecem nos registros citados por ele (valor, paráfrase, nota, casa, tradição, fonte) ou no alvo dos links. A tradição traz sua geografia implícita (Candomblé/Umbanda → Brasil; iorubá → África, Nigéria; Lucumí → Cuba). A heurística não substitui a conferência manual, feita por quem escreve e registrada no relatório da sessão; na sessão cap01 ela acusou, por exemplo, prenomes errados de autores escritos de memória.
5. Divergências (`data/fichamento/divergencias.json`): o parágrafo que cita uma versão divergente nomeia a tradição, a casa ou a região dela (palavra de 4+ letras do nome da tradição ou do campo casa/região, ou um nome curto aceito — Oyó, Ifé/Ifẹ̀, fon, ewe e as palavras de 3 letras de `nacao`/`matriz` em `data/tradicoes.json` —, este só como palavra inteira); aviso quando só uma versão de um atributo divergente é narrada.
6. Candomblé × Umbanda: registro só de Umbanda exige a palavra "Umbanda" no parágrafo; registro só de Umbanda junto de registro só de Candomblé exige os dois nomes; a seção de tradições distingue os dois.
7. Fontes C anteriores a 1950: o parágrafo marca o caráter de documento histórico.
8. Estilo: sobrenome de autor de fonte citada no parágrafo fora de `leituras-academicas` e `lacunas` é erro.
9. Cópia do fichamento (8+ palavras: erro; 6–7: aviso) e JSON em dia com o `.md` e com o esquema.

## 5. Como escrever um capítulo novo (sessão de lote)

1. `git pull origin main`; ler `docs/ESTADO.md` e este guia.
2. Despejar os registros `fichado`/`revisado` do orixá (fora os retidos, listados em `data/orixas/<id>.json` → `pendencias.retidos_ate_conselho`) e os de outras entidades que o mencionam (itãs compartilhados, parentescos).
3. Escrever `data/capitulos/<id>.md` seguindo as seções; agrupar os marcadores no fim das frases ou parágrafos.
4. `python3 scripts/validar_capitulos.py --gerar` até 0 erros; reescrever os avisos de 6–7 palavras que não sejam nomes, listas, datas ou expressões correntes.
5. Anti-cópia com o texto integral: `python3 scripts/baixar_refs.py --destino /tmp/refs` e `ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py` (0 erros nos trechos `capitulos/…`).
6. Build, `python3 scripts/qa_site.py`, `node site/scripts/acessibilidade.cjs`, screenshots.
7. Conferência manual: reler cada parágrafo ao lado dos registros citados e anotar no relatório o que foi ajustado.
