# Acervo interno de texto integral das fontes

**Uso exclusivamente interno de pesquisa.** Esta pasta guarda cópias integrais
(PDF e texto convertido) das obras usadas no fichamento, nas tradições e no
glossário, para **leitura, releitura e conferência anti-cópia**
(`scripts/anticopia.py`). Decisão do autor em 2026-11-01 ([`docs/ESTADO.md`](../docs/ESTADO.md)).

## O que NÃO pode acontecer

- **Nada daqui vai para o site.** O site mostra só paráfrase com fonte citada.
  O build (`site/`) não lê esta pasta e `scripts/qa_site.py` falha se algum
  arquivo, PDF ou trecho do acervo aparecer em `site/dist` (inclusive em `/dados/`).
- **O conteúdo não pode ser publicado nem redistribuído.** Os direitos são dos
  autores e editoras, mesmo quando a obra está em acesso aberto: a licença de
  cada obra não foi conferida uma a uma.
- **O repositório não pode ser público com PDFs/textos versionados aqui.**
  O workflow de deploy e o de validação **falham** se o repositório estiver
  público e houver arquivo versionado em `acervo/pdf/` ou `acervo/txt/`.

## Situação atual (2026-11-01): repositório PÚBLICO

O repositório está público (o GitHub Pages da conta pessoal exige isso sem o
GitHub Pro). Por isso **os PDFs e os textos não são versionados**: o
`.gitignore` mantém `acervo/pdf/*` e `acervo/txt/*` fora do git e só o índice,
este LEIAME e as URLs extras entram no repositório. O acervo é remontado a cada
sessão com `python3 scripts/baixar_refs.py` (≈ minutos; o índice diz o que baixa).

Para versionar o conteúdo, o autor escolhe uma saída (ver
[`docs/pesquisa/acervo-01.md`](../docs/pesquisa/acervo-01.md) §5):

1. **Repositório privado à parte** (recomendado), p.ex. `mapadosorixas-acervo`,
   clonado em `acervo/` ou baixado por sessão; o site continua público no Pages.
2. **Tornar este repositório privado e assinar o GitHub Pro** (Pages de repo
   privado). Atenção: o histórico já público pode ter sido clonado; o acervo só
   deve entrar *depois* da troca de visibilidade. Então remover as linhas do
   acervo no `.gitignore`.
3. Manter como está (acervo efêmero, remontado por sessão).

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `pdf/<source_id>.pdf` | PDF original baixado (ou salvo à mão com esse nome) |
| `txt/<source_id>.txt` | `pdftotext` em ordem de leitura, hifenização de fim de linha desfeita |
| `indice.json` / `INDICE.md` | por fonte: título curto, URL de origem, data do download, páginas, palavras, sha256, observação de acesso; também as que falharam (gerados pelo script — não editar à mão) |
| `urls_extras.json` | links diretos tentados antes dos do catálogo (HAL etc.) |

## Como usar

```bash
python3 scripts/baixar_refs.py                 # baixa o que falta e atualiza o índice
python3 scripts/baixar_refs.py --so-converter  # depois de salvar um PDF à mão em acervo/pdf/<source_id>.pdf
python3 scripts/anticopia.py                   # já compara com acervo/txt
```

O nome do arquivo é sempre o `source_id` do catálogo. Fonte que não baixar vai
para `docs/pesquisa/PENDENCIAS.md` com a URL. O script não contorna desafio
anti-robô nem paywall.
