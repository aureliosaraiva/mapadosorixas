# Capítulos narrativos — sessão cap05 (2026-11-02)

Sessão trabalhadora coordenada pela orquestradora: **ajustes técnicos pedidos pelas sessões de capítulos** ([cap03](capitulos-03.md) §3, [cap04](capitulos-04.md) §2 e §6) e **capítulo-panorama da cosmologia**. Nenhum fichamento, itã, catálogo ou tradição foi editado; o único capítulo existente que mudou foi o de Logunedé (uma grafia, §1).

## 1. Validador: acentos iorubás (diacríticos combinantes)

- **Problema** (cap03 §3): em `candidatos()`, o regex `[\w][\w'’-]*` não casa marcas combinantes (categoria Unicode `Mn`), e "Éfọ̀n" (o tom grave sobre ọ não tem forma pré-composta) era partido em "Éfọ" + "n" e cobrado como o nome "efo", ausente dos registros.
- **Correção:** função `sem_marcas()` (NFD → remove `Mn` → NFC), que tira só os diacríticos e mantém letras e caixa (a caixa decide o que é candidato a nome próprio). `candidatos()` passa a varrer o texto já sem marcas, e `norm()` usa a mesma função; o levantamento de palavras minúsculas do fichamento (`Ctx.comuns`) também.
- **Efeito nos 25 capítulos:** nenhum erro ou aviso novo, nem sumido (saída do validador idêntica antes e depois). Em Logunedé, a grafia que a cap03 tinha simplificado voltou à do registro `logunede-014`: "Éfọ̀n Aláayè".
- **Testes** (`tests/test_capitulos.py`, classe `Normalizacao`): `norm("Éfọ̀n Ifẹ̀ Ọ̀yọ́ Ọ̀ṣun") == "efon ife oyo osun"`; caixa preservada; candidatos com tom grave; heurística aceita "Éfọ̀n Aláayè" contra o corpus de `logunede-014`.

## 2. Nomes curtos na checagem de divergência

- **Problema** (cap04 §3): a checagem "versão divergente nomeia tradição, casa ou região" só aceitava palavras de 4+ letras; "Oyó" e "Ifẹ̀" (3 letras normalizadas) não contavam, e a cap04 teve de escrever "historiadores da corte" ou "mitologia de Ifẹ̀".
- **Correção, sem afrouxar a regra geral:** lista `TOPONIMOS_CURTOS` (oyo, ife, fon, ewe, e, por clareza, ketu, jeje, efon, ijexa, que já tinham 4+ letras) somada às palavras de 3 letras dos campos `nacao` e `matriz` de `data/tradicoes.json` e das variantes dos termos `religiao_e_grupo` do glossário (hoje só acrescenta "fon"). Uma palavra curta só conta se for aceita **e** aparecer inteira no parágrafo (`\bife\b`); "rio", "ilê", "pai", "são" continuam de fora. As palavras longas seguem casando pelo começo, como antes.
- **Efeito nos capítulos existentes:** nenhum (não havia erro pendente: as sessões contornaram o problema). Os parágrafos reescritos pela cap04 ficaram como estão; voltar a "Oyó"/"Ifẹ̀" é opcional numa revisão de estilo.
- **Testes** (`DivergenciaCurta`, com `odudua-006`, casa "mitologia de Ifẹ̀ segundo Johnson"): "Em Ifẹ̀…" e "Em Ifé…" passam; sem o lugar continua erro; "Ifetayo" não conta (palavra curta só inteira); `nome_tradicao()` recusa rio/ile/pai/sao/de.

## 3. Aviso de entidade sensível na página do capítulo

- `site/src/pages/orixas/[id]/capitulo.astro` mostra `<p class="aviso-sensivel nota-caixa">Tema sensível: este capítulo traz só o que é público em fonte acadêmica, sem fundamento iniciático.</p>` quando a entidade tem `sensivel: true` (mesma frase e classe da ficha).
- `qa_site.py` §12: entidade sensível sem o aviso na página do capítulo é erro; aviso numa entidade não sensível também.
- Como não há capítulo real de entidade sensível (Iyami espera o conselho, e **não** foi escrito), a cobertura é um teste ponta a ponta novo, `tests/e2e_capitulos_site.py` (também no CI): numa cópia temporária, um capítulo SINTÉTICO de Iyami → build → o aviso aparece e o QA passa; retirado o aviso, o QA acusa; aviso posto no capítulo de Ogum, o QA acusa. Nada do capítulo sintético toca `data/`.
- **Refatoração:** o corpo do capítulo (texto, notas, fontes citadas, termos) saiu da página para o componente `site/src/components/CorpoCapitulo.astro`, usado pela página do orixá e pela do panorama, com o mesmo HTML que o QA confere. Duas mudanças pequenas no caminho: a nota de um registro de **outra** entidade passa a linkar para a ficha dela quando a versão está lá (antes só os da própria entidade tinham link); a nota de pendência diz "Obra ou decisão pendente" (há pendências que são decisões do conselho).

## 4. Capítulo-panorama

**Formato** (detalhe no [guia](../capitulos-guia.md), "Capítulo-panorama"): `tipo: panorama` e `id` livre no frontmatter (não pode ser id da lista-mestra), sem exigência de ficha; seções próprias e obrigatórias `hierarquia`, `planos-do-mundo`, `a-pessoa`, `ancestrais`, `lacunas`; sem `{{lacuna}}` (que é por entidade); novo tipo de link `(capitulo:<id>)`, válido também nos capítulos de orixá, que o validador confere (capítulo existente, de entidade com ficha). O JSON leva `tipo` e `id` no lugar de `orixa` (`schemas/capitulo.schema.json`, `oneOf`).

**Site:** rota `/<id>/capitulo/` (`site/src/pages/[panorama]/capitulo.astro`) → `/cosmologia/capitulo/`; a página `/cosmologia/` ganha a caixa "Em texto corrido" com o link; o Livro lista "Panoramas" antes dos capítulos (`data-capitulo="cosmologia"`, `data-tipo="panorama"`); cada capítulo costurado mostra o panorama em "Ver também". `qa_site.py` §12: página gerada, selo, título, parágrafos e notas idênticos ao JSON (a mesma conferência dos capítulos), `/cosmologia/` linka para o panorama, e todo link `capitulo` aponta para página gerada.

**Texto** (`data/capitulos/cosmologia.md`, *A cosmologia em resumo: do Ser Supremo aos ancestrais*): 16 parágrafos, ~1 030 palavras, 41 registros citados (todos `fichado`, nenhum retido), 20 notas. Costura curta dos 7 capítulos da cap04, com link para cada um:

| Seção | Conteúdo | Capítulos |
|---|---|---|
| (abertura) | o que o texto é; panteão diferente em cada tradição | os 7 |
| Hierarquia | Olodumare no topo (estudos iorubás × terreiros de Salvador/SP); a partilha na Bahia, na leitura junguiana e em Cuba; as três leituras coloniais; Odudua (Bahia × Ilê-Ifẹ̀ × relato de 1894); Olokun (Lagos × Ifẹ̀ × Cuba) | Olodumare, Odudua, Olokun |
| Os planos do mundo | Orum e Aiê (culto iorubá, Ketu do Rio, leitura do candomblé); Exu entre os planos; céus e terra dos mortos nos relatos de época; aiye como universo | Orum, Aiê |
| A pessoa e o Orí | Ori em Oyó e no relato de 1894; Eledá × orixá na Bahia; Cuba | Orí |
| Os ancestrais | egúngún nas cidades de origem Ọ̀yọ́; Egun na Bahia, nações, Umbanda à parte; fundamento à espera do conselho; **Iyami: só a frase de que o tema aguarda o conselho** | Egungun |
| O que as fontes não dizem | **funfun como lacuna** (nenhuma fonte usa o termo); Idowu, Beniste, J. E. dos Santos | — |

**Regras:** sem citação no corpo (autores só nas lacunas, para obras pendentes); versões atribuídas por tradição/região (o validador cobrou o nome da tradição para `orum-006` e `orum-007`: "No culto iorubá da Nigéria… nas cidades de origem Ọ̀yọ́" — esta última já com o nome curto aceito); fontes coloniais sinalizadas ("um oficial britânico, em 1894", "um missionário anglicano, em 1926", "um administrador colonial de 1910", "relatos de época"); Umbanda dita outra religião, com o egum umbandista distinto do Egungun ancestral; nada de Iyami além da pendência "Lote C — decisões para o conselho" (item a).

**Conferência manual:** cada frase relida ao lado dos registros. Ajustes: duas sequências de 8+ palavras iguais a paráfrases (`olodumare-017`, "mais por parentesco do que por uma escala…"; `exu-034`, "…que se manifesta para ajudar os vivos") reescritas; a frase "não há registro de Olokun nos terreiros" saiu (em panorama não há `{{lacuna}}` e nenhum registro a sustenta); "venerado por quem vive da pesca e da navegação" vem de `olokun-001` (1894) e o parágrafo cita também `olokun-004` (1910) para "nascido de Yemaja".

## 5. Acervo e anti-cópia

- Acervo `orixas-fontes` anexado (`add_repo` aceito para esta sessão) e clonado em `../orixas-fontes`; `acervo_sync.sh pull`: 47 textos.
- **Ogungbemi 2021** (PDF sem camada de texto, PENDENCIAS §1b): OCR com `tesseract` 5.3 (eng, 300 dpi, instalado com `apt-get`) → `txt/ogungbemi-2021-olodumare.txt` (10 342 palavras; o OCR troca alguns diacríticos iorubás, p. ex. "Ol6dumaré"), índice atualizado (`status: ok`) e enviado ao `orixas-fontes` com `acervo_sync.sh push`. O acervo passa a 48 textos.
- `baixar_refs.py` + `anticopia.py` com os 48 textos: **0 erros**; 68 avisos "próximo", **nenhum no panorama nem em Logunedé**, os mesmos de antes nos outros capítulos. Das 16 obras citadas pelo panorama, 15 têm texto no acervo; `cabrera-1954-monte` entra só via `bastide-1958-candomble` (no acervo).
- **`qa_site.py` procurava vazamento só em `acervo/` local** (0 textos quando o acervo está no `orixas-fontes`): passou a usar `scripts/acervo_dir.py` (`ACERVO_DIR` → `../orixas-fontes` → `acervo/`). Com isso: 153 nomes de arquivo e 48 textos procurados, 0 vazamentos.

## 6. Validadores, testes e site

| Verificação | Resultado |
|---|---|
| `validar_capitulos.py --gerar` | 26 capítulos (25 + panorama), **0 erros**; avisos 6–7 palavras: os mesmos de antes, nenhum no panorama |
| `validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas`, `validar_fichas` | OK (124 divergências, 26 fichas, 806 versões; sem mudança de dados) |
| `python3 -m unittest discover -s tests` | 82 testes OK (34 em `test_capitulos.py`, +17) |
| `e2e_revisao_site.py`, `e2e_modelo2_site.py`, `e2e_capitulos_site.py` (novo) | OK |
| build + `qa_site.py` | 94 páginas, 26 capítulos (562 parágrafos conferidos), 0 vazamentos do acervo |
| `site/scripts/acessibilidade.cjs` | nenhuma violação grave (inclui `/cosmologia/capitulo/`, 1280 e 390 px) |
| screenshots 390 px (avulsos, não versionados) | `/cosmologia/capitulo/`, `/cosmologia/` e `/livro/` renderizam; `screenshots.cjs` ganhou `panorama-cosmologia` |

## 7. Para a orquestradora

1. **Iyami:** a página do capítulo já mostra o aviso de tema sensível; o capítulo continua à espera do conselho (item a das decisões do lote C).
2. **Panorama:** o formato aceita outros temas (ex.: um panorama das iabás ou das nações quando houver capítulos suficientes); cada novo panorama precisa só do `.md` e, se tiver página temática, de um link nela (o QA confere `/<id>/` se existir).
3. **Estilo opcional:** os parágrafos da cap04 que trocaram "Oyó"/"Ifẹ̀" por perífrases podem voltar ao nome curto numa revisão.
4. **Revisão do conselho:** o panorama é `rascunho`, como os capítulos que ele costura.
