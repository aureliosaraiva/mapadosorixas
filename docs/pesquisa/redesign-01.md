# Redesign 01 — visual e linguagem do site para o público leigo

**Sessão:** redesign (trabalhadora, coordenada pela orquestradora), 2026-11-02.
**Pedido do autor:** o site parecia de layout antigo e técnico demais; o público é leigo. Redesign completo do visual e da linguagem da interface, **sem mudar o conteúdo** (`data/` não foi tocado: `git diff data/` vazio).

## 1. O que mudou

### Identidade visual
- **Tipografia:** Literata (serifada feita para leitura longa em tela, usada nos títulos, capítulos e definições) e Inter (interface). As duas são **auto-hospedadas** pelos pacotes `@fontsource-variable/literata` e `@fontsource-variable/inter` (licença OFL), sem Google Fonts em tempo de execução: nenhum pedido a terceiros e nada de rastreamento. Os subconjuntos com `unicode-range` cobrem as letras iorubás com ponto (ẹ, ọ, ṣ).
- **Paleta sóbria:** papel quente (#fbf9f5), tinta escura, índigo para links e ocre como destaque discreto. Contraste AA conferido pelo axe nos dois temas.
- **Modo claro e escuro:** segue o sistema e tem um botão no cabeçalho (a escolha fica guardada no navegador; sem armazenamento, vale só na página). O desenho do mapa de conexões troca de cores junto com o tema.
- **Sem imagens de divindades:** só tipografia, cor, ícones de traço genéricos (livro, grade, folha, órbita, rede) e um padrão geométrico de círculos concêntricos na capa. Nada de estética "exótica".
- **Mobile-first:** menu recolhido atrás de um botão no celular (com Esc e foco corretos), cartões em uma coluna, filtros empilhados, índice do capítulo recolhido no topo.

### Leitura dos capítulos (livro/revista)
- Coluna de cerca de 40rem, Literata em 1,15–1,2rem com entrelinha 1,78, hifenização e capitular na abertura.
- **Notas discretas que abrem ao toque/clique** (e ao passar o mouse em computador) numa caixa junto ao número, sem tirar o leitor do lugar (`site/src/lib/notas-popover.ts`). Pelo teclado, Enter abre e leva o foco à caixa; Esc fecha e devolve o foco. Sem JavaScript, o número continua sendo link para a nota no fim da página.
- **Índice lateral** fixo no computador, com a seção atual destacada; no celular vira botão "Neste capítulo" no topo.
- Tempo de leitura estimado, número de notas e data de atualização na cabeça do capítulo.

### Páginas e navegação
| Antes (menu com 12 itens) | Depois |
|---|---|
| Início, Catálogo, Livro, Itãs, Cosmologia, Grafo, Tradições, Glossário, Fontes, Metodologia, Baixar dados, Sobre | **Menu:** Livro, Orixás, Mitos, Cosmologia, Mapa de conexões, Glossário, Sobre (+ ícones de busca e de tema). **Rodapé:** Fontes e bibliografia, Tradições e nações, Glossário, Sobre, Buscar, Dados abertos para pesquisa |

- **Início:** o que é, aviso de revisão, "Por onde começar" (Livro, Orixás, Mitos, Cosmologia), os orixás com página, "Como ler este site" (tudo tem fonte; não há versão única; respeito às tradições) e "Para ir além".
- **Orixás** (`/catalogo/`): cartões limpos (tipo, nome, até 4 etiquetas de tradição, "Capítulo para ler", número de mitos e de obras); filtros simples (nome, tipo, tradição, mostrar). Primeiro os que têm página; os "Em pesquisa" depois, só com nome e tipo.
- **Página do orixá:** resumo em destaque ("Em resumo": domínios, elementos, cores, dia, símbolos, sincretismo, lugar na cosmologia, até 3 versões cada, com nota) → destaque do capítulo ("Ler o capítulo") → **Em cada tradição** (todas as versões, por item) → **Variações entre casas e nações** (quadros comparativos recolhíveis) → **Mitos** → **Conexões** (desenho carregado só quando a seção chega à tela, e lista) → Palavras desta página → **O que ainda falta** → **Fontes desta página**.
- **Livro:** cartões com capítulo, orixá, seções e tempo de leitura; visões de conjunto primeiro; "Capítulos em preparo".
- **Mitos** e página de cada mito; **Cosmologia**; **Mapa de conexões** com explicação em três passos ("cada ponto é um nome…"), aviso "Equivalente não quer dizer igual" e lista completa; **Glossário** com índice por letra e por assunto; **Fontes** como bibliografia legível (obras citadas no site primeiro, depois a bibliografia de pesquisa); **Buscar** (página própria, Pagefind).
- **Sobre** absorveu a **Metodologia** (a página `/metodologia/` saiu): o que é, conteúdo em revisão, como foi feito (5 passos), diferenças entre tradições (com os exemplos citados de antes: dias da semana, a hesitação do pai de santo, o itã de Oxóssi em disputa), Candomblé e Umbanda, respeito e sigilo, limites, correções, créditos e direitos de uso. Os exemplos continuam com fonte (componente `Ref`, que derruba o build se o registro não estiver fichado).

**Por que fundir Metodologia e Sobre:** para o leigo, "Metodologia" é jargão e as duas páginas repetiam o mesmo assunto (regras, revisão, limites). Juntas, numa só página em linguagem simples, a honestidade sobre limites e divergências fica no mesmo lugar em que se explica o que o site é. Nada da substância saiu: princípios, os 5 passos, os exemplos com fonte, sigilo, revisão e limitações estão lá, só sem os nomes de arquivos, status e códigos.

**Por que manter "Baixar dados", mas só no rodapé:** para o leigo, a página não faz sentido e saiu da navegação principal. Mas ela é útil para pesquisadores e é a forma de os dados circularem com as fontes; por isso ficou no rodapé como "Dados abertos para pesquisa", com texto simples ("arquivos no formato JSON, que pode ser aberto em qualquer editor"), o aviso "Direitos de uso: a definir pelo autor" e as mesmas exclusões do site. Os nomes de arquivo de origem no repositório saíram da tabela.

### Linguagem para leigos
| Antes | Depois |
|---|---|
| "Rascunho — aguardando revisão de praticantes e pesquisadores" + link para issues | **"Conteúdo em revisão por especialistas"** (faixa discreta em todas as páginas, com "Saiba mais" → Sobre) |
| ids de registro nas notas (`ogum-012`) e "Registro `x`" | nada visível; o vínculo fica no atributo `data-registro` (conferido pelo QA) |
| "Nota do fichamento" | "Observação" |
| "Fonte:" / ids de fonte | "De acordo com …" e "Fontes desta página" |
| "Divergências" | "Variações entre casas e nações" |
| atributos ("Itãs (resumos parafraseados)", "Interpretação acadêmica", "Hierarquia e posição cosmológica") | "Mitos (itãs)", "Leituras de pesquisadores", "Lugar na cosmologia" |
| "Pendências e campos sem fonte", ids em pré-fichamento, "Retidos até decisão do conselho" | "O que ainda falta": itens sem obra lida; "à espera da leitura da obra original" (só contagem); "guardados até a revisão" (só contagem e tema) |
| confiabilidade A/B/C/D, status `conferido_web`/`a_verificar`/`pista`, "Observações" técnicas do catálogo | fora do site; obras de nível C marcadas "Lida com cautela: documento de época ou obra de divulgação…" |
| "Lacuna: Nenhum registro fichado de … (conferido pelo validador)" | "As obras reunidas até agora não dizem nada sobre …" + link "O que ainda falta" |
| "Obra ou decisão pendente … (registro de pendências)" com link para o GitHub | "Assunto ainda em estudo, à espera de uma obra ou de uma decisão da revisão: …" |
| "nós", "arestas", "grafo" | "nomes", "relações", "mapa de conexões" |
| "Descrição pendente de fonte" | "Descrição em preparo" |

- **Sem nomes de pessoas do projeto nem contatos.** O Sobre não cita o autor nem revisores, e não há e-mail (já conferido pelo QA). As linhas de crédito de revisão por versão ("Revisado por … (tradição)") continuam, porque obedecem ao consentimento de cada revisor e são garantia do QA §9; hoje não há revisor cadastrado, logo nada aparece (decisão registrada em PENDENCIAS §3b, redesign).
- **Sem issues do GitHub.** Ficou sem canal de correções: o Sobre diz que um canal simples será aberto junto com o grupo de revisão. **Pendência P1 do autor** (PENDENCIAS §3b, redesign).
- O texto que vem de `data/` (capítulos e observações das fichas) **não foi mudado**. Ali ainda há "fichamento" (82 trechos em 25 capítulos), códigos de registro nas observações (102 versões) e "confiabilidade C" (36 versões). Fica como sugestão para as sessões de conteúdo (PENDENCIAS §3b, redesign).

## 2. Garantias mantidas e QA

`scripts/qa_site.py` foi adaptado **sem afrouxar** nada:
- selo e faixa conferidos pelo novo texto (`SELO = "Conteúdo em revisão por especialistas"`, igual a `site/src/lib/textos.js`);
- notas das fichas: o registro de cada nota é lido de `data-registro` (antes, de um `<code>` visível); continua conferindo fonte, via, ano e página de cada versão, e a tabela de variações contra a nota;
- versão dentro da seção do seu atributo: título `h3` (ou `h2`) com `id` = atributo;
- estado da revisão: atributos `data-revisadas`/`data-total` + texto;
- pré-fichamento e retidos: o id não pode aparecer como versão, nota (`<code>` **ou** `data-registro`) nem fora de "O que ainda falta" (onde, agora, nem aparece);
- Início: o aviso de versão inicial precisa dizer que o conteúdo está em revisão e linkar para Sobre (#revisao), no lugar do link de issues;
- Sobre: Fontes, #contribuir, aviso de revisão, licenças e autoria a cargo do autor, nenhum e-mail;
- tradições sem fonte: aviso "Descrição em preparo" e o texto do rascunho ausente de todas as páginas;
- **novo §13 — linguagem para leigos:** nenhum link de issues em nenhuma página e, no texto visível da interface, nada de status internos, "fichamento", códigos de confiabilidade, JSON (fora de Dados abertos), "validador" nem códigos de registro. O texto que vem de `data/` (frases de ≥ 2 palavras) é descontado, porque é conteúdo de outras sessões. Testado por adulteração (link de issue, "pre_fichamento", "confiabilidade A", "exu-001" → 5 erros) e nos e2e.
- Testes e2e atualizados (`tests/e2e_modelo2_site.py`, `tests/e2e_revisao_site.py`) para a nova marcação, com dois casos novos de adulteração de linguagem.

Mantidos: `noindex` em todas as páginas, sem sitemap nem `canonical`; aviso de tema sensível no catálogo, na página do orixá e no capítulo; nada de pré-fichamento, retidos ou acervo no site (§2 e acervo do QA); fontes sempre a um toque, nas notas.

## 3. Acessibilidade, teclado e desempenho

- **axe-core** (WCAG 2.1 A/AA + boas práticas; `site/scripts/acessibilidade.cjs`, agora também com uma amostra de 10 páginas no **tema escuro**): 94 páginas × 1280 e 390 px + 10 no escuro = 198 verificações, **0 violações** (graves ou não). Durante a sessão o axe pegou os links "↩" das notas sem sublinhado (link-in-text-block); corrigido.
- **Teclado e toque** (novo `site/scripts/teclado.cjs`, 21 verificações): "Pular para o conteúdo"; nota abre com Enter, recebe o foco, fecha com Esc e devolve o foco; clique abre sem rolar a página e fecha ao clicar fora; tema troca e é lembrado; menu do celular abre, fecha com Esc e devolve o foco; índice do capítulo recolhido no celular e fecha ao escolher uma seção; sem JavaScript, menu visível e nota como link. Tudo ok.
- **Lighthouse 12.6.1** (perfil de celular, servidor local, build com `SITE_BASE=/mapadosorixas`):

| Página | Desempenho | Acessib. | Boas práticas | SEO |
|---|:-:|:-:|:-:|:-:|
| Início | 100 | 100 | 100 | 60* |
| Orixás | 100 | 100 | 100 | 60* |
| Xangô | 92 | 100 | 100 | 60* |
| Capítulo de Ogum | 100 | 100 | 100 | 60* |
| Mapa de conexões | 91 | 100 | 100 | 60* |
| Glossário | 95 | 100 | 100 | 60* |

\* SEO 60 é proposital: o Lighthouse desconta o `noindex`, que fica até a revisão.

Ajustes de desempenho feitos para chegar lá: CSS embutido no HTML (`inlineStylesheets: 'always'`, sem pedido que bloqueie a pintura); índice do capítulo sem "pulo" de layout (CLS 0,32 → 0,03); **posições do mapa calculadas no build** (Cytoscape sem tela no Node, layout `cose`; o navegador só desenha com `preset`: bloqueio 1,4 s → 0,35 s, nota 75 → 91); desenho de conexões da página do orixá carregado só quando a seção se aproxima da tela; etiquetas-link com 24 px de altura (alvo de toque).

## 4. Screenshots

Em [`docs/screenshots/redesign/`](../screenshots/redesign/): `antes-*` (site anterior) e `depois-*`, para Início, Orixás, Xangô, capítulo de Ogum, Livro, Mitos, Mapa, Sobre e Fontes, em desktop (1280 px) e celular (390 px), e Início, capítulo e Xangô no tema escuro (`*-desktop-escuro`; no "antes" não havia tema escuro). JPEG, até 3000 px de altura. Gerados por `site/scripts/screenshots-redesign.cjs <antes|depois>` (com `BASE=<url>` tira da URL publicada).

## 5. Validadores e testes

Rodados no fim da sessão: `validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas` (sem diferença em `data/`), `validar_fichas`, `anticopia` (0 erros; avisos já existentes), `validar_capitulos`, `python3 -m unittest discover -s tests` (82 testes ok), build com `SITE_BASE=/mapadosorixas`, `qa_site.py` ok, os 3 e2e, axe, teclado e Lighthouse (acima). Conferência da URL publicada: ver §6 (ok).

## 6. Publicação

Push direto na `main`; o workflow `deploy-pages.yml` ([execução nº 34](https://github.com/aureliosaraiva/mapadosorixas/actions/runs/41442688455), validadores + build + QA + deploy) terminou com sucesso.

**Conferência da URL publicada** (<https://aureliosaraiva.github.io/mapadosorixas/>, Playwright, 2026-11-02): as 14 páginas principais (Início, Orixás, Xangô, capítulo de Ogum, Livro, Mitos, Cosmologia, Mapa, Glossário, Fontes, Sobre, Tradições, Buscar, Dados abertos) com a faixa "Conteúdo em revisão por especialistas", `noindex`, nenhum link de issues e a fonte Literata carregada; nota do capítulo abre na caixa; mapa desenhado (117 nomes, 150 relações); busca "Ogum" → 5 resultados, links com o prefixo; **nenhum erro de rede ou de JavaScript**. Screenshots `publicado-inicio-desktop.jpg` e `publicado-capitulo-ogum-celular.jpg` na pasta do redesign.

## 7. Pendências abertas (em PENDENCIAS §3b, "Redesign do site")

1. **Canal de correções para leigos** (P1, autor).
2. **Jargão no conteúdo de `data/`** (P2, sessões de conteúdo).
3. Crédito de revisores por versão quando houver revisores (P3, autor).
4. Leitor de tela real nas caixas de nota e no menu do celular (P3).
