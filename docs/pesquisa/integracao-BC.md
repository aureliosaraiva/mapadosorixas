# Integração dos lotes B e C: itãs, arestas e entidade Orí

**Data:** 2026-11-01 · **Sessão:** integBC (trabalhadora, coordenada pela orquestradora; única sessão editando `data/` nesta rodada) · **Base:** [lote B](lote-B.md) §6–§7 e [lote C](lote-C.md) §5, §6 e §8.

**Arquivos editados:** `data/fichamento/{odudua,olokun,iemanja,egungun,logunede}.json` (registros de itã novos), `data/fichamento/ori.json` (novo), `data/entidades.json` (entidade `ori`), `data/itans.json`, `data/conexoes_alvos.json`, os gerados (`data/orixas/*`, `conexoes.json`, `entidades_equivalentes.json`, `divergencias.json`, `status_conteudo`) e docs. **Não editados:** `data/fontes/catalogo.json`, `site/`, `schemas/`, `scripts/`.

## 1. Resumo

| Indicador | Antes | Depois |
|---|---:|---:|
| Registros de fichamento | 685 | **705** (+10 itãs, +10 Orí; todos `fichado`) |
| Lista-mestra | 33 | **34** (+ `ori`) |
| Fichas / versões públicas | 24 / 658 | **25 / 678** |
| Itãs / versões | 17 / 20 | **26 / 36** (odu nomeado: 2) |
| Grafo: nós / arestas | 85 / 104 | **111 / 139** (equivalência 60, sincretismo 40, parentesco 33, associação 3, companheiro de culto 3) |
| Entidades equivalentes | 40 | **53** |
| Avisos `sem_mapa` | 52 | **0** |
| Atributos com versões divergentes | 107 | 113 |
| Versões de `hierarquia` (Cosmologia) | 57 | 62 |
| Anti-cópia com texto integral (41 obras) | — | **0 erros**; 43 avisos, os mesmos de antes (nenhum nos registros novos) |

## 2. Itãs

Regra seguida: cada itã foi conferido na página do original; se ainda não havia registro `itans`, ele foi criado primeiro no fichamento da entidade principal (status `fichado`, resumo próprio) e só depois espelhado em `data/itans.json`. Os registros de itã do lote B já existiam (fichados pela sessão loteB); as páginas foram reconferidas.

### 2.1 Registros de itã novos (conferidos nesta sessão)

| Registro | Fonte e página conferida | Itã |
|---|---|---|
| odudua-015 | Ellis 1894, p. 42 (IA, `_djvu.txt` Wellcome) | ita-023, casal na cabaça (Dennett p. 74 e Farrow p. 45 só repetem Ellis: citados na nota) |
| odudua-016 | Dennett 1910, pp. 17–18; identificação Yemuhu = Odudua na p. 18, nota, e p. 73 | ita-024, criação em Ilobe |
| odudua-017, odudua-018 | Jock 2020, p. 6 (duas versões) | ita-012, criação da terra firme |
| odudua-019 | Ogungbemi 2021, pp. 50–51 (OCR local; transcreve K. Abimbola) | ita-012 |
| olokun-006 | Ellis 1894, p. 71 | ita-025, dilúvio de Olokun (Dennett pp. 114–115 copia) |
| olokun-007 | Ellis 1894, p. 64 (variante ligada a Ifá) | ita-025 |
| iemanja-060 | Ellis 1894, pp. 43–45 (versão direta; antes só via Pitta, iemanja-052) | ita-003 |
| egungun-015 | Fámúlẹ̀ 2021, pp. 14–15; odu Ọ̀wọ̀rìn-Àṣẹ́yìn na p. 14 | ita-026 |
| logunede-026 | Santos 2023, p. 76 (versão rara; antes só como parentesco, logunede-008) | ita-022 |

**Correção ao relatório do lote C (§5, item 8):** o odu Ọ̀wọ̀rìn-Àṣẹ́yìn fala dos *sayégún*, os primeiros egúngún, mandados por Olódùmarè. Os "400 irúnmọlẹ̀ que descem com os egúngún" estão em outro odù, Ogbè-Ròsùn (p. 15, adaptado de Bascom 1969). A versão traz só o primeiro como odu; o segundo ficou na nota. O pacto ritual que o mito funda (p. 15) não foi fichado (decisão do lote C sobre detalhe ritual de Egungun).

### 2.2 Versões acrescentadas a itãs existentes

| Itã | Versão nova | Observação |
|---|---|---|
| ita-003 Iemanjá e o nascimento das águas | iemanja-060 (Ellis direto) | `entidades` + olokun, xango, ogum, iansa, oxum, oba, orixa_oko, oxossi, aje_xaluga (nomeados por Ellis; ver §5a) |
| ita-012 (novo título: "A criação da terra firme: Oxalá, Odudua e o vinho de palma") | odudua-017, -018, -019 | + olodumare (Olorun/Olodumare nomeados), ogum (a corrente de ferro, em Ogungbemi) |
| ita-015 A orelha de Obá | oba-003 (Chiousse, p. 247) | mesma narrativa de Bastide (oxum-028) |
| ita-017 Iansã e as folhas de Ossaim | ossaim-018 (Chiousse, pp. 251–252) | + olodumare (Olorun na versão de Chiousse). O item 7 do lote C ("partilha do universo", Cabrera via Bastide, pp. 189–190) **é** este itã: a partilha já estava em olodumare-018 e olokun-005 |

### 2.3 Itãs novos só com registros do lote B

ita-018 (ossaim-017, Bastide p. 157), ita-019 (ossaim-019, Chiousse p. 256), ita-020 (oxumare-012, Chiousse p. 287), ita-021 (logunede-010, Santos p. 76). Paginação de Chiousse reconferida: o número da página vem no rodapé, antes da quebra de página do PDF; Obá fica na p. 247 e Oxumarê na p. 287, como no lote B.

### 2.4 Não integrados

- **Migração de Okambi** (lote C §5, item 3; Ellis, pp. 90–92): conferida, mas não nomeia nenhuma entidade da lista-mestra (o enviador é "uma certa pessoa"), e o esquema exige `entidades` nomeadas. Fica fora até haver fonte que a ligue a Odudua ou a outra entidade; não foi agrupada com a criação da terra firme, para não afirmar paralelo sem fonte.
- Sugestões do lote B §6 que dependem de exemplar (Verger 1981, Prandi 2001 via Sallum & Silva): ficam para quando houver o livro.
- Santos 2023, pp. 82–85: itã de Prandi 2001 (Logunedé disfarçado de Oxum e possuído por Oxóssi) e patakí cubano via Dianteill 2007, com odu. Não estavam nos relatórios; registrados em PENDENCIAS §3a.

## 3. Arestas (`data/conexoes_alvos.json`)

Os 52 registros com aviso `sem_mapa` foram lidos um a um; só viraram aresta os alvos que o `valor` diz.

- **Parentesco (+13 arestas):** Obá cônjuge de Xangô (oba-001, -006, -009, -012, -013) e de Omolu (oba-007); Obá, Olokun e os Ibeji filhos de Iemanjá (oba-014/015, olokun-002/004, ibeji-021); Ibeji filhos de Xangô (ibeji-021) e de Oxum (ibeji-022) e irmãos de Xangô em Cuba (ibeji-013); Logunedé filho de Oxum, Oxóssi, Erinlé, Ogum e Oyá, conforme a versão (logunede-002, -004, -005, -007, -008); Oxumarê filho de Nanã e irmão de Omolu (oxumare-017, -028); Odudua cônjuge de Olokun (odudua-007).
- **Equivalência (+14):** voduns Dangbê, Idarço, Alogué, Boço Jara, Boçalabê, Eowá; inquices Hongolo/Angoro, Katende/Mpanzu (de Ossaim e, por aproximação, de Iroko), Tere-Kompenso/Gongobira, Vunji, Kitembo/Tembu; Anyiewo e Hoho (Ellis, "dos povos ewe").
- **Sincretismo (+6):** S. Bartolomeu (Oxumarê), S. Cosme e S. Damião (Ibeji, inclusive a linha de Umbanda), S. Crispim e S. Crispiniano (Ibeji, Recife), Santo Expedito (Logunedé), Santa Teresa e N. S. do Carmo (Ewá).
- **Associação (+2):** Ossaim–Oxóssi (ossaim-034) e Iroko–Nanã (iroko-002), sem subtipo: o valor diz "associado"/"relacionada", não parentesco.
- **Lista vazia (8, sem aresta):** oxumare-015 (santo não identificado), ossaim-038 (Katende distinto de Ossaim), oba-017 e ewa-007 (sem equivalente angola), logunede-009 ("Yewá": Ewá ou Iyewa não decidido), ewa-005 (Euá é aí o vodum filho de Azonce, não o orixá), ibeji-010 e ibeji-016 (Doú/Doum, sem nó). O commit das arestas fala em 10 por engano; são 8.
- **Alvos que ficaram só no `valor`:** Olosa, Olokun-su, Oranmiyan e Isedale (fora da lista-mestra, sem nó); "avô de Ogum" (odudua-007), sem subtipo de aresta para avô.
- Nós novos: 8 orixás da lista-mestra (ossaim, logunede, ibeji, erinle, iroko, ewa, odudua, olokun), 5 santos, 8 voduns, 5 inquices.

## 4. Entidade Orí

- `ori` criada na lista-mestra (`conceito_cosmologico`, prioridade 2; grafias Orí, Ori, Orì, Olori; nota de modelagem sem afirmação factual).
- **Nenhum registro existente tratava de Orí** (busca por Orí/Olori/Eleda no fichamento: só Eleda como epíteto de Olorun, em olodumare-002/005/009, que continuam onde estão). Nada foi movido.
- Os achados do lote C §6 foram conferidos e fichados em `data/fichamento/ori.json` (10 registros): Ellis pp. 125–126 (Olori/Ori, um dos três espíritos que habitam a pessoa; símbolo: meia cabaça com búzios), Johnson p. 27 (divindade doméstica do destino; 41 búzios em coroa; o lote C dava pp. 27–28, mas o trecho cabe na p. 27), Farrow p. 130 (repete Ellis; lê Olori como deificação da inteligência), Bastide pp. 184–185 (Eleda como anjo da guarda, distinto do orixá de cabeça nas casas tradicionais), Bastide pp. 314–315 (Cabrera, Cuba: Eleda, ori e Obatalá misturados; maioria dos informantes baianos identifica eleda com o orixá individual que fica no ori) e Zacharias pp. 158–159 (Olori assimilado ao Eledá; leitura junguiana).
- Bastide se contradiz entre p. 185 e p. 315: registrado como está (ori-006 × ori-008), com nota.
- Ofertas e sangue no rito de Olori (Ellis p. 126, Farrow p. 130) e o bori (Zacharias p. 159) **não** foram fichados (rito; glossário já deixa bori para o conselho).

## 5. Decisões desta sessão (para o revisor)

a. **Grafias de Ellis e Dennett** (Yemaja/Yemoja, Shango, Oya, Oshun, Oshosi, Ogun, Orisha Oko, Aje Shaluga) foram lidas como o mesmo orixá da lista-mestra, como grafias. **Não** foram ligados: Obatala/Orishala/Orisa-nla a `oxala` (decisão já tomada na sessão modelo2), Shankpanna a `omolu`, Dada, Olosa, Oke, Orungan.
b. **Ewe:** Anyiewo e Hoho ficaram como nós `vodum`, com "(ewe)" no rótulo, porque o esquema não tem tipo para divindade ewe; "nome_fon_ou_banto" seria menos exato.
c. **ewa-004:** o registro é o sincretismo da própria Euá na casa descrita (um santo por vodum correspondente), por isso os dois santos viraram arestas da Ewá. Difere do caso de omolu-024, em que os santos são dos voduns.
d. **Ifá → `orunmila`** nas entidades de ita-019, ita-024, ita-025 e ita-026, como já feito no lote A (ita-013).
e. **ita-024:** Eleda → `olodumare` e Yemuhu → `odudua` só porque o próprio Dennett faz essas identificações (pp. 17, 18 e 73).

## 6. Anti-cópia e verificação

- `python3 scripts/baixar_refs.py --destino /tmp/refs` + reposição manual: `_djvu.txt` do IA para Ellis (Wellcome `b21781370`), Dennett, Farrow e Johnson (o script troca Ellis por um PDF de 496 palavras); OCR de Ogungbemi com `tesseract` (instalado nesta sessão; o PDF não tem texto); Jock, Santos 2023 e Zacharias baixados com `--ids`. Total: 41 textos.
- 1ª passagem: **1 erro** (iemanja-060.nota: a lista de nascimentos de Ellis, 8 nomes na mesma ordem) e 3 avisos "próximo" (ori-008, ori-009, ori-010). Todos reescritos.
- Final: `ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py` → **0 erros**; 43 avisos, os mesmos de antes da sessão (classe C). Resumos de Ellis, Dennett, Farrow, Johnson, Jock, Ogungbemi e Fámúlẹ̀ (em inglês) não são checáveis contra tradução: a paráfrase foi feita com estrutura própria.
- Validadores: `validar_fontes`, `validar_fichamento`, `divergencias` (113), `gerar_fichas` (0 avisos), `validar_fichas`, `anticopia`: OK. Testes: 48 unitários; `e2e_revisao_site.py` e `e2e_modelo2_site.py`: OK. `npm run build` (56 páginas indexadas) e `scripts/qa_site.py` (62 páginas, 678/678 versões, 36 versões de itã, 62 de hierarquia): OK. Acessibilidade (axe) não rodada: o código do site não mudou.
- Scripts da sessão fora do repo (`/tmp/integ/`); os JSON são a fonte da verdade.

## 7. O que ainda falta em B e C

- **Dependem de exemplar:** Ewá (8 registros) e Iroko (12): Verger 1981, Prandi 2001, Pallas; itãs de Ossaim em Prandi 2001 e Verger; Oxumarê (Bessém/Dã, Parés 2006); funfun (Verger 1981, Santos 1976, Beniste 1997); Idowu 1962.
- **Bloqueados no ambiente:** Igboin 2014 e Layi 2016 (HTTP 500), Verger 1965 (Persée, anti-robô; leitura também depende do conselho).
- **Decisões:** Ewá × Iyewa ("Yewá" de Santos); agrupamento Iroko/Tempo; o que publicar sobre Iyami e sobre ritos de Egungun; Olokun edo; Eleda como entidade própria ou não; identificações do §5.
- **Funfun:** segue sem fonte; nada foi escrito (PENDENCIAS §3a).
