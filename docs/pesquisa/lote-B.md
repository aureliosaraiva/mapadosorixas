# Lote B (parcial): Ossaim, Obá, Ibeji, Iroko/Tempo, Logunedé, Oxumarê e Ewá

**Data:** 2026-11-01 · **Sessão:** lote B (trabalhadora, coordenada pela orquestradora) · **Plano:** [varredura 4](relatorio-varredura-04.md) §6, lote B.

Arquivos editados: só `data/fichamento/{ossaim,oba,ibeji,iroko,logunede,oxumare,ewa}.json` e os arquivos gerados (`data/orixas/*.json`, `data/fichamento/divergencias.json`, `status_conteudo` em `data/entidades.json`). **Não foram editados** `data/fontes/catalogo.json`, `data/itans.json`, `data/conexoes_alvos.json`, `site/` nem `schemas/`. Itãs e arestas estão nas §6 e §7, para integração posterior.

## 1. Resumo

| Entidade | Registros | Retidos (tabus/alimentos) | Fontes |
|---|---:|---:|---|
| Ossaim (`ossaim`) | 39 | 0 | Bastide, Chiousse, Halloy, Ellis, Farrow, Sallum & Silva, Botão, Prandi 2005 |
| Ibeji (`ibeji`) | 40 | 4 | Bastide, Chiousse, Halloy, Ellis, Farrow, Ogunbunmi, Botão, Nogueira |
| Oxumarê (`oxumare`) | 33 | 1 | Bastide, Chiousse, Halloy, Ellis, Farrow, Sallum & Silva, Prandi 2005, Botão, Nogueira, S. Ferretti |
| Logunedé (`logunede`) | 25 | 2 | Bastide, Chiousse, Sallum & Silva, Santos 2023, Prandi 2005, Botão, S. Ferretti |
| Obá (`oba`) | 19 | 1 | Bastide, Chiousse, Halloy, Ellis, Dennett, Botão, S. Ferretti, Nogueira |
| Iroko/Tempo (`iroko`) | 12 | 0 | Bastide, Halloy, Botão |
| Ewá (`ewa`) | 8 | 1 | Halloy, Prandi 2005, Botão, S. Ferretti |
| **Total** | **176** (todos `fichado`) | **9** | 13 fontes, todas já `conferido_web` no catálogo |

- Fichas geradas: 5 → **12**; versões públicas: 285 → **452**; atributos com versões divergentes: 41 → **66** (+25, todos das entidades novas).
- Cosmologia: **14 versões de `hierarquia`** passam a aparecer (antes: nenhuma).
- Nenhuma fonte nova no catálogo; fontes que faltam vão para a §8 e para [PENDENCIAS](PENDENCIAS.md) §3d.

## 2. Fontes lidas e paginação

| Fonte (id) | Conf. | Páginas lidas nesta sessão | Paginação |
|---|:-:|---|---|
| Bastide 1961 (`bastide-1958-candomble`) | A | 85, 92–98, 103–105, 108, 116–123, 127, 137–138, 144, 153–162, 165, 204, 254–262 | PDF = impressa (cópia UFRJ, OCR ruim) |
| Chiousse 1995 (`chiousse-1995-divins`) | A | 203–205, 236, 239, 247, 251–259, 270, 279–288 | impressa = PDF − 1 |
| Halloy 2005 (`halloy-2005-intimite`) | B | 165–170, 276–277, 322–324, 806–809 | impressa = PDF − 1 |
| Ellis 1894 (`ellis-1894-yoruba`) | C | 45, 48, 77, 79–82, 95 | texto OCR (`_djvu.txt`) do IA; página pelo cabeçalho |
| Dennett 1910 (`dennett-1910-nigerian`) | C | 101–102, 168–169 | texto do IA |
| Farrow 1926 (`farrow-1926-faith`) | C | 58–59, 65–67 | texto do IA |
| Sallum & Silva 2006 (`sallum-2006-ossaim`) | B | 291–305, 312 | impressa = PDF + 290 |
| Santos 2023 (`santos-2023-logunede`) | B | 71–82 | impressa = PDF + 70 |
| Ogunbunmi 2026 (`ogunbunmi-2026-twins`) | B | 169–177 | impressa = PDF + 168 |
| Botão 2007 (`botao-2007-angola`) | B | 40–45, 64, 104 | impressa = PDF − 1 |
| Prandi 2005 (`prandi-2005-pegadas-voduns`) | A | 7, 14–15, 25–27, 34 (versão do autor) | versão do autor |
| S. Ferretti 2011 (`ferretti-2011-comida`) | B | 260–262 | impressa |
| Nogueira 2017 (`ufg-2017-exu-umbanda`) | B | 139, 171, 197, 311, 324 | PDF = impressa |

**HAL:** o `curl` direto no arquivo baixou os PDFs de Chiousse e Halloy (a página do registro segue com Anubis, e `baixar_refs.py`, com `requests`, ainda recebe o desafio). Os dois PDFs ficaram em `/tmp/refs-pdf/` (fora do repo) e foram convertidos com `--so-converter`. Ellis: o PDF do IA não tem texto; o `_djvu.txt` foi salvo à mão em `/tmp/refs/ellis-1894-yoruba.txt`.

**Procurados e sem conteúdo útil para o lote:** Nina Rodrigues 1935 e Baudin 1885 (não baixados nesta sessão), Silva 2012 (sem menção aos sete), Costa 1980 (só "vários Ibeji" citando Bastide). Prandi 2001 (*Mitologia*) é impresso e não foi usado. Queiroga & Nascimento 2019 só nomeiam "Euá ou Yewá" numa lista de nomes de Iemanjá (§5).

**Fontes C** (Ellis, Dennett, Farrow) entram como documento histórico, com aviso padrão na `nota` e nunca sozinhas para um atributo: cada atributo que elas sustentam tem também versão de fonte A/B, salvo quatro casos, registrados aqui como lacuna a cobrir com exemplar: `oba/dominios` (rio Oba, Ellis), `oba/elementos` (nuvens, Dennett), `ibeji/dominios` (divindade tutelar dos gêmeos, Ellis; Chiousse e Ogunbunmi dizem o equivalente em `funcoes` e `hierarquia`) e `oxumare/animais` (píton *ere*; Farrow repete Ellis). Farrow copia Ellis em boa parte; onde é cópia, a nota diz.

## 3. Candomblé × Umbanda e outras tradições

- Candomblé queto/nagô (Bahia, São Paulo), Xangô de Pernambuco, Batuque (Porto Alegre), Candomblé angola-congo, Tambor de Mina, Candomblé ijexá/efon (Logunedé) e culto iorubá na Nigéria ficam em `tradicoes` separados, com a casa em `casa_ou_regiao`.
- **Umbanda** aparece só onde a fonte fala dela: as linhas de Rubens Saraceni (Oxumaré na linha do Amor, Obá na do Conhecimento) e de Diamantino Trindade (Ibeji = Tenda Cosme e Damião), ambas via Nogueira 2017, com nota "não vale para o Candomblé". Chiousse leva `candomble_ketu` + `umbanda` como nos registros anteriores, porque o campo dela mistura terreiros dos dois.
- Equivalências com voduns e inquices valem para a casa descrita, nunca como identidade (decisão do fichamento-07).

## 4. Divergências registradas (lado a lado, sem eleger versão)

| Entidade / atributo | Versões |
|---|---|
| Ossaim / transe | não se incorpora (Bastide, Bahia; Halloy, Recife) × "o Ossaim de uma pessoa" vestido de folhas (Sallum & Silva) |
| Ossaim / Katende | associado a Ossain (Botão p. 40) × não confundir com Ossain (adeptos, p. 104); Bastide e Carneiro o aproximam de Irocô |
| Ossaim / gênero | homem nos itãs × "a dona das folhas" (Bastide) e tratado no feminino ou andrógino (Chiousse) |
| Ibeji / estatuto | não baixam, ancestrais míticos (Bahia e Recife, Bastide; nagô, Papai em Chiousse; Recife, Halloy) × baixam e são honrados como orixás (Porto Alegre, Bastide) × alguns terreiros confirmam transe (Chiousse p. 204) × òrìṣà na Nigéria (Ogunbunmi) |
| Ibeji / mãe | Oxum (Recife, Halloy) × Iemanjá, com Xangô (alguns informantes de Chiousse) |
| Ibeji / festa | 27 set. (Bastide, Halloy) × 23, 26 ou 27 set. (Chiousse) × 12 fev. num terreiro do Recife (Bastide) |
| Ibeji / sincretismo | Cosme e Damião (todas) × às vezes Crispim e Crispiniano (Recife, Bastide) |
| Logunedé / pai | Inlé (Bastide; Lopes via Santos) × Oxóssi (Chiousse; Santos) × Erinlé, "tipo de Oxóssi" (Sallum & Silva) × Ogum, com mãe Oyá (versão rara, Santos) |
| Logunedé / gênero | "seis meses homem, seis mulher" é crença corrente que Santos considera equívoco (registrado como leitura do autor) |
| Oxumarê / iniciação | tem filhos de santo (Chiousse) × sem assentamento nem iniciados (Recife, Halloy) |
| Oxumarê / dia | terça com Nanã (Bahia) × terça com Ogum e Nanã (Opô Afonjá) × sem dia fixo (Recife) |
| Oxumarê / cores | amarelo e verde (Chiousse) × cores do arco-íris (Halloy) |
| Oxumarê / sincretismo | S. Bartolomeu (Bastide; Prandi) × não identificado (Chiousse) |
| Oxumarê / posição | servo de Shango (Ellis) × filho de Nanã, de origem jeje (Halloy, Prandi, Bastide) |
| Obá / esposa | de Xangô (todas), com ordem variável (Halloy n. 364: 1ª em João do Rio, 3ª em Verger) × em algumas versões, de Omulu após o repúdio (Chiousse) |
| Obá / culto no Recife | sem assentamento nem sacrifício (Carvalho 1984) × hoje com sacrifício, possessão e ritmo próprio (Halloy) |
| Iroko / estatuto | orixá × árvore sagrada × árvore morada do orixá (Recife, Halloy) |

## 5. Decisões e cuidados desta sessão

- **Fundamento:** a colheita ritual das ervas (Bastide, pp. 157–161: cantos, horários, pagamento a Ossaim, 16 folhas e múltiplos na iniciação) **não foi fichada**; o que entrou é o nível público (Ossaim não entra no mundo cultivado; o babalosaim colhe as ervas). Vai para o conselho ([PENDENCIAS](PENDENCIAS.md) §3d).
- **Tabus e alimentos** foram fichados e ficam retidos pelo gerador (9 registros). Os registros retidos de fontes C têm nota própria, porque o QA acusou a nota-padrão de fonte C (que aparece em fichas públicas) como texto de registro retido.
- **Ewá × Iyewa:** "Yewá" (Santos, amiga de Logunedé) ficou só no registro de Logunedé, com nota, sem decidir a entidade. Queiroga & Nascimento (p. 8, n. 5) listam "Euá ou Yewá" entre nomes de Iemanjá usados como chave de busca em letras de música: **não fichado** (lista de busca, não afirmação dos autores); fica como pista de que Ewá/Yewá é tratada como nome de Iemanjá em parte do repertório popular. Decisão do autor (PENDENCIAS §3d).
- **Iroko/Tempo:** nenhuma fonte lida usa "Tempo" como nome do orixá do Candomblé queto; Botão (p. 42) liga o inquice Kitembo a "Irocô ou Tempo". O agrupamento da lista-mestra continua sem sustentação ampla (PENDENCIAS §3a e §3d).
- **2ª mão:** afirmações que a fonte lida atribui a outro autor fora do catálogo ou `a_verificar` (Artur Ramos, Thompson 1983, Lopes 2019, Silveira 2003, Verger 2002, Gonçalves Fernandes, René Ribeiro, Ortiz) ficaram com `source_id` da fonte lida e o autor citado na `nota`, sem `via_source_id`, porque a regra exige primária `conferido_web`.

## 6. Itãs encontrados (para `data/itans.json`, sessão de integração)

Todos estão fichados como registros `itans` (status `fichado`) e podem virar versões espelhadas.

| Registro | Fonte e página | Resumo próprio | Entidades nomeadas | Odu |
|---|---|---|---|---|
| ossaim-017 | Bastide 1961, p. 157 | Ossaim perde uma perna (em Cuba, também olho e braço) numa briga com Xangô | ossaim, xango | — |
| ossaim-018 | Chiousse 1995, pp. 251–252 | Iansã, a pedido de Xangô, levanta um vento que abre a cabaça de folhas de Ossãe; os orixás repartem as plantas | ossaim, iansa, xango, (Olorun) | — |
| ossaim-019 | Chiousse 1995, p. 256 | Ossãe, escravo de Ifá, recusa cortar ervas que curam; Ifá o faz mestre das plantas | ossaim, orunmila (como "Ifá") | — |
| oba-003 | Chiousse 1995, p. 247 | Oxum engana Obá, que corta a orelha para Xangô e é repudiada | oba, oxum, xango | — |
| oxumare-012 | Chiousse 1995, p. 287 | Oxumaré: seis meses macho e arco-íris, seis meses fêmea e cobra | oxumare | — |
| logunede-010 | Santos 2023, p. 76 | Logunedé passa metade do ano caçando com Oxóssi e metade pescando com Oxum | logunede, oxossi, oxum | — |
| logunede-008 (parentesco) | Santos 2023, p. 76 | versão rara: abandonado por Oxum, criado por Ogum, coroado por Oyá | logunede, oxum, xango, ogum, iansa | — |

**Itãs vistos e não fichados como itã** (sugestões): Sallum & Silva (p. 296) resumem, a partir de Verger (1981, p. 122), o mito do pássaro que sobrevoa o mundo e conta a Ossaim o que viu, e (p. 312) a versão em que Ossaim ordena que as folhas voltem e depois dá uma a cada orixá (Prandi 2001, pp. 153–154): entram como versões quando houver o exemplar. Chiousse (p. 256): Ossãe abandonado nu pelos pais, que se cobre de folhas (fichado em `iconografia`, ossaim-033). Ellis (p. 45, mito de Orungan e Yemaja, já em iemanja-052 via Pitta): Oba nasce do corpo de Yemaja (oba-014) — pode virar entidade a mais nesse itã.

## 7. Arestas sugeridas (para `data/conexoes_alvos.json`)

Os registros abaixo geram aviso `sem_mapa`. Sugestão de alvo; a sessão de integração confere o `valor` antes de mapear.

| Registro | Tipo | Alvo(s) |
|---|---|---|
| oba-001, oba-006, oba-009, oba-012, oba-013 | parentesco (esposa) | xango |
| oba-007 | parentesco (esposa, algumas versões) | omolu |
| oba-014, oba-015 | parentesco (filha) | iemanja |
| ibeji-022 | parentesco (mãe) | oxum |
| ibeji-021 | parentesco (pais, alguns informantes) | iemanja, xango |
| ibeji-002, ibeji-014, ibeji-026 | sincretismo | São Cosme e São Damião (nó de santo novo) |
| ibeji-012 | sincretismo | São Crispim e São Crispiniano |
| ibeji-028 | equivalência | Hoho (ewe) |
| ibeji-039 | equivalência | Vunji (inquice) |
| ibeji-040 | sincretismo (Umbanda) | São Cosme e São Damião |
| logunede-002 | parentesco | erinle (Inlé), oxum |
| logunede-004, logunede-007 | parentesco | oxossi, oxum |
| logunede-005 | parentesco | erinle |
| logunede-008 | parentesco (versão rara) | ogum, iansa |
| logunede-022 / -023 | equivalência / sincretismo | Boço Jara (vodum) / Santo Expedito |
| logunede-024 | equivalência | Tere-Kompenso / Gongobira (inquice) |
| oxumare-017, oxumare-028 | parentesco | nana (mãe); omolu (irmão) |
| oxumare-008, oxumare-030 | sincretismo | São Bartolomeu |
| oxumare-023 | equivalência | Anyiewo (ewe) |
| oxumare-029 | equivalência | Dangbê, Idarço (voduns) |
| oxumare-031 | equivalência | Hongolo / Angoro (inquice) |
| ossaim-034 | associação | oxossi |
| ossaim-037 | equivalência | Katende (inquice) — ver divergência com ossaim-038 |
| ossaim-039 | equivalência | Alogué (vodum) |
| iroko-002 | associação | nana |
| iroko-011 | equivalência | Kitembo / Tembu (inquice) |
| ewa-003 / ewa-004 | equivalência / sincretismo | Boçalabê, Eowá (voduns) / Santa Teresa, N. S. do Carmo |
| oba-017, ewa-007 | — | sem aresta (ausência de equivalente) |
| oxumare-015, oxumare-012 | — | sem aresta |

## 8. O que falta (→ [PENDENCIAS](PENDENCIAS.md) §3d)

- **Ewá** e, em menor grau, **Iroko**: quase nada aberto; dependem de Verger 1981, Prandi 2001 e obras da Pallas.
- **Oxumarê**: itãs de Prandi/Verger, Bessém/Dã no jeje baiano (Parés 2006), Santos 2019 (OJS 403).
- **Ossaim**: Barros 2011; Verger 1967 e 1995.
- **Ibeji**: Houlberg 1973, Mobolade 1971, Chappel 1974, Renne 2001, Thompson 1971.
- **Fontes novas sugeridas para o catálogo** (não adicionadas: o catálogo é de outra sessão): Chappel, "The Yoruba cult of twins in historical perspective", *Africa* 44(3), 1974; Renne, "Twinship in an Ekiti Yoruba town", *Ethnology* 40(1), 2001; Mobolade, "Ibeji custom in Yorubaland", *African Arts* 4(3), 1971; Thompson, "Sons of thunder", *African Arts* 4(3), 1971; Lopes, *Logunedé* (reed. 2019, anotar em `lopes-2006-logunede`); Silveira, *O candomblé da Barroquinha* (2006, já `a_verificar`) para a narrativa do Alaketo e do ilê Maroiá Láji; Carvalho, J. J. de, tese sobre o Xangô do Recife (1984), citada por Halloy para Obá e Orunmilá.

## 9. Anti-cópia e verificação

- `python3 scripts/baixar_refs.py --destino /tmp/refs` (33 textos), mais Chiousse e Halloy por `curl` + `--so-converter` e o `_djvu.txt` de Ellis.
- 1ª passagem: **8 erros** (sequências de 8 palavras: Ferretti, Bastide, Sallum, Santos ×2, Nogueira, Prandi) e **19 avisos novos** de 6–7 palavras. Todos reescritos.
- Final: `ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py` → **0 erros**, 36 avisos "próximo" (os mesmos 36 de antes da sessão, classe C, nenhum do lote B). Ressalva de sempre: fontes em francês e inglês (Chiousse, Halloy, Ellis, Dennett, Farrow, Ogunbunmi) não são checáveis contra tradução.
- Validadores: `validar_fontes`, `validar_fichamento`, `divergencias` (66), `gerar_fichas` (12 fichas, 452 versões; avisos `sem_mapa` esperados, §7), `validar_fichas`, `anticopia`: OK. Testes: 48 unitários OK; `e2e_revisao_site.py` e `e2e_modelo2_site.py` OK. Build do site e `scripts/qa_site.py`: OK (33 páginas, 452/452 versões, 14 versões de hierarquia na Cosmologia).
- O gerador dos registros desta sessão ficou fora do repo (`/tmp/lb/gen.py`); os registros no JSON são a fonte da verdade.
