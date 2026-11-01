# Coleta automatizada de fontes (varredura nº 3 em diante)

Pipeline reproduzível: coleta por API → deduplicação → triagem manual registrada em script → incorporação ao catálogo.

| Script | Faz | Saída |
|---|---|---|
| `coletar.py` | roda `consultas.json` em Crossref, Open Library, theses.fr, HAL, DOAJ, BDTD e OpenAlex | `data/fontes/coleta/<data>/<base>.json` (itens normalizados, `total` e `n` por consulta; sem resumos) |
| `triar.py` | agrupa duplicatas (DOI, ISBN-13, título + ano, id da base), compara com o catálogo e pontua a pertinência (`pertinencia.py`) | `candidatos.json` |
| `triagem_<data>.py` | decisões manuais (`entra` / `pista` / `descarta`) e conferências de fontes já catalogadas, por trecho de título | `triagem.json` |
| `incorporar.py` | aplica a triagem ao catálogo (reconsulta DOIs no Crossref) e dá motivo automático aos demais candidatos | `data/fontes/catalogo.json`, `triagem_resumo.json` |

Variáveis opcionais: `COLETA_MAILTO` (pool "polite" do Crossref/OpenAlex) e `OPENALEX_API_KEY`.
Só uma sessão por vez pode rodar `incorporar.py`, porque ele edita `catalogo.json`. Relatório da primeira rodada: `docs/pesquisa/relatorio-varredura-03.md`. Varredura 4 (2026-11-01, expansão para o panteão): consultas `v4-*`, `triagem_2026-11-01.py` e `dominio_publico_2026-11-01.py` (obras em domínio público com texto integral e correções manuais; idempotente); relatório em `docs/pesquisa/relatorio-varredura-04.md`.
