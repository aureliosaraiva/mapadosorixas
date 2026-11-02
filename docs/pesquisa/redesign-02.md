# Redesign 02 — avisos retirados, licença MIT e autoria (pedido do autor)

**Sessão:** redesign (continuação), 2026-11-02. Pedido do autor, depois do [redesign 01](redesign-01.md):

1. retirar do site os avisos de que o conteúdo não foi revisado;
2. pôr só uma nota no rodapé: todo o conteúdo é um agrupamento organizado do que já existe publicado;
3. direitos: os das obras são exclusivamente dos seus autores; o site (conteúdo e toda a organização) é MIT, também no repositório;
4. retirar o parágrafo de créditos de software (Astro, Cytoscape.js, Pagefind, fontes);
5. no Sobre, a nota de que o conteúdo foi criado por Aurelio Saraiva, que tem contato com a cultura e é praticante, mas não é líder religioso nem especialista no assunto.

`data/` não foi tocado.

## O que mudou

- **Avisos retirados:** a faixa do topo, o selo das páginas de orixá, capítulo, mito e Livro (componente `Selo.astro` removido), o aviso de versão inicial do Início, a seção "Conteúdo em revisão" do Sobre, a linha "Revisão por especialistas" em "O que ainda falta" e as menções a "revisão" nos textos de interface (notas de pendência, Dados abertos, Sobre). Continuam: o aviso "Tema sensível" (é sobre o tema, não sobre a revisão), a política de guardar tabus e alimentos rituais fora do site ("Guardados fora do site") e, se um dia houver, as linhas de crédito de revisão por versão e o aviso de página inteiramente revisada.
- **Rodapé de todas as páginas:** "Todo o conteúdo deste site é um agrupamento organizado do que já existe publicado em livros, pesquisas e outras fontes públicas, sempre com a indicação da obra de origem." e "Os direitos sobre as obras consultadas pertencem exclusivamente aos seus autores. O site, incluindo os textos de resumo e toda a organização do conteúdo, é distribuído sob a licença MIT" (link para o `LICENSE`).
- **Repositório:** `LICENSE` (MIT, Copyright (c) 2026 Aurelio Saraiva, com um parágrafo de escopo em português: cobre código, resumos e organização; as obras citadas são dos seus autores; o acervo privado não faz parte), seção "Licença e direitos" no `README.md`, `"license": "MIT"` em `site/package.json`, e o `LEIAME.txt` de `/dados/` com a licença.
- **Sobre:** nova seção "Quem fez" com a nota do autor e a de agrupamento; "Créditos e direitos de uso" sem o parágrafo de software e com a licença MIT; "Correções" sem menção ao grupo de revisão (canal segue pendente).
- **`noindex` mantido:** não fazia parte do pedido. Decisão do autor registrada em PENDENCIAS §3b.

## QA e testes

`scripts/qa_site.py`: saíram as exigências de selo, faixa, aviso do Início e estado da revisão; entraram as garantias do pedido: **nenhuma página** com aviso de conteúdo não revisado (textos, faixa ou selo), rodapé de todas as páginas com a nota de agrupamento, a licença MIT e os direitos dos autores; Sobre com licença MIT, direitos dos autores, nota de autoria e de agrupamento; Dados abertos e `LEIAME.txt` com MIT. Testado por adulteração (aviso reinserido e licença trocada → acusados). `tests/e2e_revisao_site.py` ajustado. Rodada final: validadores do `CLAUDE.md`, testes unitários, os 3 e2e, `qa_site.py`, axe (sem violações graves) e teste de teclado, todos ok.
