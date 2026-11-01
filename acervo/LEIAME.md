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

## Onde fica o acervo (decisão do autor, sessão acervo2, 2026-11-01)

O texto integral fica no **repositório PRIVADO `aureliosaraiva/orixas-fontes`**
(branch `main`; commit e push direto nele). Este repositório (`mapadosorixas`) é
**público** e continua **sem nenhum texto integral**: esta pasta guarda só este
LEIAME, o índice gerado e `urls_extras.json` (metadados).

- `scripts/acervo_dir.py` resolve o acervo: `ACERVO_DIR`; senão `../orixas-fontes`
  (clone irmão deste repo), se existir; senão este `acervo/` local, ignorado pelo git.
- `scripts/acervo_sync.sh pull` (início da sessão) clona ou atualiza o `orixas-fontes`;
  `scripts/acervo_sync.sh push` (fim) faz commit e push dos arquivos novos na `main` dele.
  Em sessão na nuvem, anexar antes o repositório com `add_repo` (access `push`).
- `scripts/baixar_refs.py` grava no acervo resolvido, procura o arquivo primeiro lá
  (e no `acervo/` local) e só baixa o que faltar.
- `.gitignore` e as guardas de CI deste repo continuam: `acervo/pdf/*` e
  `acervo/txt/*` nunca entram aqui.

Situação em 2026-11-01: a anexação do `orixas-fontes` à sessão acervo2 foi negada
pelo controle de permissões da sessão; a estrutura do repo privado e a carga das
obras ficaram pendentes ([acervo-02](../docs/pesquisa/acervo-02.md); PENDENCIAS §1b).

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `pdf/<source_id>.pdf` | PDF original baixado (ou salvo à mão com esse nome) |
| `txt/<source_id>.txt` | `pdftotext` em ordem de leitura, hifenização de fim de linha desfeita |
| `indice.json` / `INDICE.md` | por fonte: título curto, URL de origem, data do download, páginas, palavras, sha256, observação de acesso; também as que falharam (gerados pelo script — não editar à mão) |
| `urls_extras.json` | links diretos tentados antes dos do catálogo (HAL etc.) |

## Como usar

```bash
scripts/acervo_sync.sh pull                    # início: clona/atualiza ../orixas-fontes
python3 scripts/baixar_refs.py                 # baixa o que falta e atualiza o índice no acervo
python3 scripts/baixar_refs.py --so-converter  # depois de salvar um PDF à mão em <acervo>/pdf/<source_id>.pdf
python3 scripts/anticopia.py                   # já compara com <acervo>/txt
scripts/acervo_sync.sh push                    # fim: push dos textos novos no orixas-fontes
```

O nome do arquivo é sempre o `source_id` do catálogo. Fonte que não baixar vai
para `docs/pesquisa/PENDENCIAS.md` com a URL. O script não contorna desafio
anti-robô nem paywall.
