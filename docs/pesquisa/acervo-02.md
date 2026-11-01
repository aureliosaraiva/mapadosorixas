# Acervo 02 — texto integral no repositório privado `orixas-fontes`

**Sessão:** acervo2 · **Data:** 2026-11-01 · **Status:** parcial — scripts e documentação prontos; **carga do repositório privado bloqueada por permissão**.

Só metadados: nenhum texto integral entra neste repositório público.

## 1. Decisão do autor

O acervo de textos integrais fica no repositório **privado** `aureliosaraiva/orixas-fontes` (branch `main`, commit e push direto). O `mapadosorixas` é público e continua sem nenhum texto integral (`.gitignore` e guardas de CI mantidos).

## 2. O que foi feito neste repositório

| Arquivo | Mudança |
|---|---|
| `scripts/acervo_dir.py` | novo: resolve o acervo — `ACERVO_DIR` → `../orixas-fontes` (se o clone existir) → `acervo/` local (ignorado pelo git) |
| `scripts/baixar_refs.py` | destino padrão = acervo resolvido; procura o PDF primeiro no destino e, se o destino for externo, no `acervo/` local (copia sem baixar); só baixa o que falta; `urls_extras.json` continua em `acervo/` (metadado) |
| `scripts/anticopia.py` | referências padrão = `txt/` do acervo resolvido; na falta, `acervo/txt` |
| `scripts/acervo_sync.sh` | novo: `pull` (início: clona/atualiza `orixas-fontes`) e `push` (fim: commit + push de `pdf/`, `txt/`, `indice.json`, `INDICE.md` na `main` dele, com retentativas) |
| `CLAUDE.md`, `acervo/LEIAME.md`, `docs/ESTADO.md`, `PENDENCIAS.md` | regra nova do acervo; bloqueio registrado |

## 3. Bloqueio: anexar o `orixas-fontes`

A ferramenta `add_repo` (owner `aureliosaraiva`, repo `orixas-fontes`, access `push`) foi **negada pelo controle de permissões automático da sessão**. Sem ela não há credencial para clonar nem fazer push. Por isso **não foram feitos**:

1. clone em `/home/user/orixas-fontes` e conferência de que o repositório é privado;
2. estrutura no repo privado (`pdf/`, `txt/`, `indice.json`, `INDICE.md`, `LEIAME.md`, `.gitattributes` com PDF binário);
3. carga das obras e push em lotes.

Para destravar (autor): permitir `mcp__claude-code-remote__add_repo` nas permissões da sessão (ou anexar o `orixas-fontes` ao ambiente) e repetir os passos 1–3. Com o clone em `../orixas-fontes`, basta: `ACERVO_DIR=../orixas-fontes python3 scripts/baixar_refs.py` (copia do `acervo/` local o que já estiver lá), criar `LEIAME.md` e `.gitattributes`, e `scripts/acervo_sync.sh push`.

## 4. Acervo montado nesta sessão (local, efêmero, fora do git)

Para rodar o anti-cópia, o acervo foi remontado em `acervo/` (fallback local):

- 75 fontes tentadas: **46 com texto próprio**, 6 repetidas (mesmo PDF de outra fonte, citada de 2ª mão), 2 sem texto extraível (Nina Rodrigues 1932, Ogungbemi 2021 — imagem sem OCR), **21 sem download**.
- **322 MB** de PDF, 17 MB de texto. **Nenhum PDF passa de 100 MB**; o total fica abaixo de 1 GB → quando for para o `orixas-fontes`, não precisa de Git LFS nem divisão (maiores: Frobenius ~55 MB, Johnson ~48 MB).
- Sem download (já em PENDENCIAS §1b): sem URL no catálogo (Bascom 1969, Bastide 1960, Cabrera 1954, Carneiro 1948, Herskovits 1938, Idowu 1962, Landes 1947, Ortiz 1978, Ribeiro 1952); SciELO 403 (Ferretti 1985, Giumbelli 2024, Noleto 2025, Prandi 1995); HathiTrust 403 (Nina Rodrigues 1900); sem link de PDF (Argyriadis 2005, Barnes 1989, Tishken 2009, Verger 1957, Verger 1981); conexão recusada (Oro 2008).

## 5. Validadores

`validar_fontes`, `validar_fichamento`, `divergencias` (113 atributos divergentes), `gerar_fichas` (sem mudança em `data/`), `validar_fichas`: OK. `anticopia.py` com 46 textos (acervo local): **0 erros, 43 avisos** — os mesmos de sessões anteriores (classe C, já justificados). Ainda não rodado com o acervo externo, que não pôde ser clonado.
