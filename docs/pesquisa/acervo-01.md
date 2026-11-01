# Acervo 01 — acervo interno de texto integral das fontes

**Sessão:** acervo (2026-11-01). **Arquivos:** `acervo/`, `scripts/baixar_refs.py`, `scripts/anticopia.py`, `scripts/qa_site.py`, `.gitignore`, `.gitattributes`, `.github/workflows/*`, `CLAUDE.md`, `docs/`. `data/` não foi tocado.

## 1. Achado que mudou a execução: o repositório é PÚBLICO

A decisão do autor (guardar cópias integrais no repositório) tem como condição o repositório privado. Pela API (`search/repositories`, 2026-11-01) o repositório **`aureliosaraiva/mapadosorixas` está público** — o autor o tornou público na sessão pages para o GitHub Pages funcionar na conta pessoal sem o GitHub Pro ([`publicacao.md`](../publicacao.md)).

Commitar os PDFs e textos agora seria **publicar** 47 obras com direitos de autores e editoras; um push num repositório público é praticamente irreversível (clones, forks, caches, e o histórico continua mesmo depois de tornar privado). Por isso esta sessão:

- montou toda a estrutura, o script, as proteções e o índice, e **baixou o acervo localmente** (usado no anti-cópia desta sessão);
- **não versionou `acervo/pdf/*` nem `acervo/txt/*`**: o `.gitignore` os mantém fora do git, com comentário explicando quando retirar;
- entram no repositório só `acervo/LEIAME.md`, `acervo/indice.json`, `acervo/INDICE.md` (metadados: título, URL, data, páginas) e `acervo/urls_extras.json`.

A escolha de onde versionar fica com o autor (§5, e `PENDENCIAS.md` §1b).

## 2. O que foi feito

1. **Estrutura** `acervo/pdf/<source_id>.pdf`, `acervo/txt/<source_id>.txt`, `acervo/indice.json` + `acervo/INDICE.md` (gerados; por fonte: título curto, URL de origem, data do download, páginas, palavras, sha256, bytes, observação de acesso — inclusive das falhas) e `acervo/LEIAME.md` (finalidade interna, proibição de publicar e de tornar o repo público com acervo versionado, opções de versionamento).
2. **`scripts/baixar_refs.py`**: destino padrão `acervo/` (`--destino` mantido; dentro do repo só `acervo/` é aceito); pula PDF existente (`--reconverter` refaz o `.txt`); grava o índice; lê `acervo/urls_extras.json` (links diretos tentados primeiro); **fallback por `curl` com o user-agent padrão** para arquivos `/file/…pdf` e `/document` (é o que passa no HAL — sem resolver desafio nem fingir navegador); **Internet Archive** pela API de metadados (PDF do item) e, quando o PDF digitalizado não tem camada de texto, o OCR `_djvu.txt` do próprio item.
3. **`scripts/anticopia.py`**: sem `ANTICOPIA_REFS`, usa `acervo/txt` se houver textos; `ANTICOPIA_REFS=` (vazio) desliga; `ANTICOPIA_REFS=/pasta` continua valendo. No CI o acervo está vazio, então o comportamento lá não muda.
4. **`.gitattributes`**: `acervo/pdf/** binary`.
5. **Proteção do site** — `scripts/qa_site.py` §12: falha se algum arquivo do `site/dist` (inclusive `/dados/`) tiver "acervo" no caminho, for PDF, tiver nome de arquivo do acervo, se o site citar `acervo/pdf|txt/`, ou se **qualquer sequência de 20 palavras** de um texto de `acervo/txt` aparecer no texto do site (descontado trecho que contém 10 palavras seguidas do catálogo de fontes: títulos e referências bibliográficas, que a página Fontes mostra). Testado com vazamento simulado (PDF em `/dados/` e um parágrafo de Bastide 1958 na página Sobre): os três erros aparecem; no site real, 0. O build não lê `acervo/` (o Astro importa só `data/`, e `site/public/` não tem nada do acervo).
6. **Guarda nos workflows** (`deploy-pages.yml` e `validar.yml`): passo "Acervo só em repositório privado" — falha, com mensagem explicando o motivo, se houver arquivo versionado em `acervo/pdf` ou `acervo/txt` e `github.event.repository.private` não for `true`. **Desvio consciente do pedido** ("falhar se público enquanto `acervo/` existir"): como o repositório já é público e `acervo/` existe (LEIAME e índice), a regra literal derrubaria todo deploy do site já hoje; a regra aplicada protege o que importa (o texto integral).
7. **`CLAUDE.md`**: regra do anti-cópia aponta para `acervo/` (não mais `/tmp/refs` fora do repo) e regra nova do acervo (interno, nunca no site, só versionado com repo privado).

## 3. O que entrou no acervo (local)

**47 fontes com texto próprio** (2,752,893 palavras, 8,059 páginas, **327 MB de PDF**, 17 MB de texto) + **6** fontes citadas de 2ª mão que apontam para o mesmo PDF de outra (comparadas pelo `.txt` desta) + **22** sem texto (§4). Das 75 fontes usadas (fichamento, tradições, glossário e `urls_extras.json`).

Novidades em relação às sessões anteriores: **Chiousse 1995, Halloy 2005, Toutain 2019** (HAL, curl direto), **Vallier 2011 e Cerqueira 2015** (HAL, `/document` achado pela API do HAL), **Ferreira 2017** (P1 bloqueada: veio pela cópia do CORE), **Ellis 1894, Burton 1863 e Nina Rodrigues 1932** (OCR do Internet Archive) e **Farrow 1926** (PDF do Internet Archive).

| source_id | páginas | palavras | MB | acesso |
|---|---|---|---|---|
| `akin-otiko-2024-olodumare` | 8 | 5184 | 0.4 | download direto (acesso aberto) |
| `bastide-1958-candomble` | 370 | 119803 | 6.4 | download direto (acesso aberto) |
| `bewaji-1998-olodumare` | 17 | 9553 | 0.5 | download direto (acesso aberto) |
| `blass-2007-iemanja` | 18 | 6657 | 0.2 | download direto (acesso aberto) |
| `botao-2007-angola` | 128 | 44765 | 0.8 | download direto (acesso aberto) |
| `bowen-1857-adventures` | 382 | 104446 | 28.3 | download direto (acesso aberto) |
| `burton-1863-abeokuta` | 364 | 87424 | 18.1 | PDF sem camada de texto; texto = OCR (_djvu.txt) do Internet Archive |
| `capo-chichi-2025-shango` | 12 | 4429 | 0.4 | download direto (acesso aberto) |
| `cardoso-filho-2015-iemanja` | 242 | 108822 | 1.6 | download direto (acesso aberto) |
| `carvalho-2019-iyami` | 6 | 5411 | 0.3 | download direto (acesso aberto) |
| `castillo-2022-ogum` | 37 | 15888 | 0.5 | download direto (acesso aberto) |
| `cerqueira-2015-lebabimibome` | 377 | 143089 | 2.3 | download direto (acesso aberto) |
| `chiousse-1995-divins` | 438 | 127823 | 4.9 | download direto (acesso aberto) |
| `costa-1980-exu-umbanda` | 19 | 6246 | 0.7 | download direto (acesso aberto) |
| `costa-2007-xango-pe` | 29 | 10225 | 0.6 | download direto (acesso aberto) |
| `dennett-1910-nigerian` | 278 | 61690 | 13.6 | download direto (acesso aberto) |
| `ellis-1894-yoruba` | 423 | 97966 | 17.8 | PDF sem camada de texto; texto = OCR (_djvu.txt) do Internet Archive |
| `famule-2021-ayan` | 50 | 16662 | 10.3 | download direto (acesso aberto) |
| `farrow-1926-faith` | 228 | 55661 | 14.4 | download direto (acesso aberto) |
| `ferreira-2017-legba` | 14 | 5347 | 0.5 | download direto (acesso aberto) |
| `ferretti-2011-comida` | 26 | 10899 | 0.2 | download direto (acesso aberto) |
| `ferretti-m-2020-pureza` | 20 | 7901 | 0.1 | download direto (acesso aberto) |
| `frobenius-1912-afrika` | 842 | 251115 | 55.1 | download direto (acesso aberto) |
| `halloy-2005-intimite` | 814 | 334933 | 6.2 | download direto (acesso aberto) |
| `jock-2020-oduduwa` | 8 | 8238 | 0.6 | download direto (acesso aberto) |
| `johnson-1921-history` | 742 | 316357 | 47.6 | download direto (acesso aberto) |
| `mosaico-2020-oxossi` | 7 | 3491 | 0.5 | download direto (acesso aberto) |
| `nascimento-2001-exus` | 7 | 4598 | 0.1 | download direto (acesso aberto) |
| `nina-rodrigues-1932-africanos` | 425 | 110285 | 19.4 | PDF sem camada de texto; texto = OCR (_djvu.txt) do Internet Archive |
| `ogunbunmi-2026-twins` | 12 | 4713 | 0.4 | download direto (acesso aberto) |
| `oro-2012-campo` | 10 | 3917 | 0.3 | download direto (acesso aberto) |
| `pares-2006-formacao` | 6 | 2080 | 0.3 | download direto (acesso aberto) |
| `prandi-2001-exu-diabo` | 18 | 10213 | 2.1 | download direto (acesso aberto) |
| `prandi-2005-pegadas-voduns` | 36 | 10254 | 0.4 | download direto (acesso aberto) |
| `queiroga-nascimento-2019-iemanja` | 21 | 6590 | 0.9 | download direto (acesso aberto) |
| `sallum-2006-ossaim` | 30 | 14423 | 0.9 | download direto (acesso aberto) |
| `santos-2008-ia-mi` | 23 | 10074 | 0.1 | download direto (acesso aberto) |
| `santos-2023-logunede` | 22 | 7423 | 3.9 | download direto (acesso aberto) |
| `seixas-2018-maria-iemanja` | 14 | 4928 | 0.8 | download direto (acesso aberto) |
| `silva-2012-exu-brasil` | 30 | 5875 | 21.8 | download direto (acesso aberto) |
| `teixeira-2021-iemanja` | 213 | 75285 | 7.9 | download direto (acesso aberto) |
| `tomba-2019-bantu` | 118 | 39782 | 1.4 | download direto (acesso aberto) |
| `toutain-2019-santos` | 609 | 255129 | 5.7 | download direto (acesso aberto) |
| `ufg-2017-exu-umbanda` | 410 | 175531 | 5.6 | download direto (acesso aberto) |
| `ufpb-2011-sao-jorge` | 105 | 21031 | 10.2 | download direto (acesso aberto) |
| `vallier-2011-esu` | 38 | 15474 | 11.6 | download direto (acesso aberto) |
| `zacharias-2010-olori` | 13 | 5263 | 0.1 | download direto (acesso aberto) |

**Tamanho:** 327 MB de PDF, **acima dos ~300 MB** do pedido. Os maiores são digitalizações antigas (Frobenius 1912, 55 MB; Johnson 1921, 48 MB; Bowen 1857, 28 MB). Se o acervo vier a ser versionado, propor **Git LFS** para `acervo/pdf/**` (não ativado: depende do autor; a cota gratuita do LFS é 1 GB de armazenamento e 1 GB/mês de banda) ou versionar só os `.txt` (17 MB), guardando os PDFs fora.

## 4. O que falhou

- **SciELO (Bunny Shield, 403)**: Prandi 1995, Giumbelli & Lima 2024, Noleto & Negrão 2025 (tentados também os links `sci_pdf` da Crossref e o Wayback — sem cópia arquivada) e Ferretti 1985.
- **Conexão**: `seer.ufrgs.br` (Oro 2008, ConnectionError) e `fundaj.emnuvens.com.br` (Pitta 2011, ProxyError).
- **Sem PDF aberto**: Argyriadis 2005 (OpenEdition só HTML), Barnes 1989, Tishken 2009, Verger 1957 (Cambridge, pago), Verger 1981, Nina Rodrigues 1900 (HathiTrust 403).
- **PDF sem texto**: Ogungbemi 2021 (imagem; sem OCR disponível).
- **Impressas sem URL no catálogo**: Bascom 1969, Bastide 1960, Cabrera 1954, Carneiro 1948, Herskovits 1938, Idowu 1962, Landes 1947, Ortiz 1978, Ribeiro 1952.
- As P1 impressas (Verger, *Orixás*; Prandi, *Mitologia*; Cacciatore; Beniste; Castro; Parés) continuam dependendo de exemplar (PENDENCIAS §2). Brown 1989 (`muse.jhu.edu`) não está no catálogo como fonte usada.

Tudo listado com URL em `PENDENCIAS.md` §1b.

## 5. Decisão pendente do autor: onde versionar o acervo

1. **Repositório privado à parte** (recomendado): `mapadosorixas-acervo`, privado, clonado em `acervo/` (que já está no `.gitignore` deste) ou baixado no início da sessão. O site continua público no Pages, sem custo, e o texto integral nunca toca o histórico público.
2. **Tornar este repositório privado + GitHub Pro** (Pages de repo privado; o site continua público). O acervo só pode ser commitado **depois** da troca; então remover as linhas do acervo do `.gitignore` — o passo do CI passa a aceitar.
3. **Manter efêmero** (como agora): cada sessão roda `python3 scripts/baixar_refs.py` (~15 min) e os PDFs salvos à mão se perdem com o contêiner.

## 6. Validadores

- `validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas` (sem diff em `data/`), `validar_fichas`: OK. Testes (`tests/`): OK.
- **Anti-cópia com `acervo/txt` (47 textos, antes 25): 0 erros.** 43 avisos "próximo", nenhum de fonte nova do acervo; são nomes, datas, títulos e expressões correntes ("13 de dezembro ao meio dia", "Tiriri, Jelebara…", "P. Cavalcanti, As seitas africanas no Recife", "no primeiro quartel do século XX"), já vistos nas auditorias anteriores. Esta sessão não fichou fonte nem pode editar `data/`: ficam para a próxima sessão de revisão justificar ou reescrever os poucos de paráfrase (ex.: `exu-012`, `ogum-006`, `ogum-050`, `castillo-2022` nas tradições).
- Build do site e `qa_site.py` (com a checagem nova do acervo): OK, 0 vazamentos.
