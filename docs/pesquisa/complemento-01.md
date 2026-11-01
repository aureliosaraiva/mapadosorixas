# Complemento 01 — Chiousse, Halloy, Toutain e Ferreira pelo acervo

**Sessão:** compl01 (2026-11-01), trabalhadora coordenada pela orquestradora. **Arquivos editados:** `data/fichamento/` (13 entidades + `orunmila.json`, novo), `data/itans.json`, `data/conexoes_alvos.json`, `data/fontes/catalogo.json` (só `observacoes` de 4 fontes) e os gerados (`data/orixas/`, `data/conexoes.json`, `data/entidades*.json`, `divergencias.json`). **Não tocados:** `data/capitulos/`, `site/` e os validadores de capítulos (estão com outra sessão).

Acervo montado no início com `python3 scripts/baixar_refs.py` (47 textos em `acervo/txt`, local e ignorado pelo git; nenhum PDF ou texto integral commitado).

## 1. Resultado

| Fonte | Páginas lidas (impressas) | Registros | Entidades |
|---|---|---:|---|
| Chiousse 1995 (impressa = PDF − 1) | 225–291 (Parte III inteira) | 62 | Oxalá 15, Omulu 12, Oxum 11, Iansã 9, Nanã 5, Orunmilá/Ifá 4, Iemanjá 2, Xangô 2, Ogum 1, Olorun 1 |
| Halloy 2005 (impressa = PDF − 1) | 163–186, 276–277, 322–326 | 46 | Oxalá 8, Oxum 8, Nanã 7, Iansã 7, Omolu 5, Orunmilá 5, Oxóssi 2, Xangô, Iemanjá, Ogum, Exu |
| Toutain 2019 (impressa = PDF − 11) | 8, 41, 56–58, 74, 124–125, 172–178, 210–212 | 19 | Exu 4, Orunmilá 4, Oxalá 2, Omolu 2, Oxum 2, Iansã 2, Iemanjá, Xangô, Ossaim |
| Ferreira (Saraiva) 2017 (impressa = PDF + 6) | 7–19 (integral) | 4 | Exu (Legbá) |
| **Total** | | **131** | 13 entidades + Orunmilá |

- **Registros:** 705 → **836** (820 `fichado`, 16 `pre_fichamento`). **Orunmilá** passa de `sem_fichamento` a `fichado` (13 registros, ficha nova): a lista-mestra fica com 26 entidades `fichado` e 8 `sem_fichamento` (Oxalufã e Oxaguiã seguem no arquivo de Oxalá).
- **Itãs:** 26 → **30 itãs, 45 versões** (+4 itãs, +9 versões): ita-027 *Olorun entrega a Oxalá os elementos* (Chiousse, pp. 225–226), ita-028 *Oxalá despedaçado pela pedra de Atowoda* (p. 227), ita-029 *Oyá, a mãe dos nove filhos* (p. 251), ita-030 *Omulu, o filho expulso que volta para curar a aldeia* (p. 270). Versões novas em itãs existentes: ita-005 (Halloy p. 323: Ossaim inicia Odé), ita-012 (Chiousse p. 228: o vinho de palma), ita-013 (Chiousse p. 286: Ifá pescador e Oxum), ita-014 (Chiousse p. 246: Oxum Ioni), ita-016 (Chiousse p. 242: quiabos de Xangô).
- **Grafo:** 111 → **117 nós**, 139 → **150 arestas** (sincretismo 48, parentesco 36). Nós novos: Orunmilá/Ifá (orixá), Senhor do Bonfim, Santa Catarina, São Lázaro, N. S. da Penha, São Francisco de Assis, Joana d’Arc. Arestas novas sustentadas pelo `valor`: Oxum filha/esposa de Orunmilá (Chiousse p. 286; Halloy p. 168), Oxumaré e Omolu filhos de Nanã (Halloy p. 166), Ibeji filhos de Oxum (Halloy p. 324), Oxalá cônjuge de Iemanjá (Halloy p. 169), Omolu cônjuge de Nanã e de Obá (Chiousse p. 270), sincretismos lucumi (Elegguá/São Pedro, Changó/Santa Bárbara, Babalú Ayé/São Lázaro, Orula/São Francisco). 0 avisos `sem_mapa`.
- **Divergências:** 113 → 124 atributos com versões divergentes.
- **Retidos (tabus):** 3 novos (oxala-049, oxala-061, iansa-038), fora da ficha pública; no texto dos itãs e festas os interditos e pratos ficaram de fora com nota "retido".

## 2. Divergências novas que valem destaque

1. **Idade de Oxalufã e Oxaguiã.** Chiousse (p. 228) chama Oxalufã de jovem e Oxaguiã de velho; Bastide (oxala-022) e Halloy (p. 169: Orixálufã velho, Orixáogiã jovem com força de Xangô) dizem o contrário. Registrado como está, com nota, sem correção (decisão do lote A sobre contradições).
2. **Corpo e saúde (Chiousse).** Para cada orixá, a autora registra versões por chefe de culto: Oxalá na cabeça (maioria, Mãe Sevi) × cabeça e corpo inteiro (Mãe Celeste); Iansã nos ossos (Papai) × organismo inteiro (outros); Ogum só em cirurgias × nervos (Papai) × peito (Mãe Celeste). As listas de plantas e usos terapêuticos não foram fichadas uma a uma (só os nomes simbólicos, como o algodão de Oxalá).
3. **Oxum mãe dos Ibejis (Halloy p. 324):** o próprio autor diz que o laço vem da posição dos assentamentos no peji, sem mito conhecido; a aresta entra porque o `valor` afirma o parentesco atribuído pelos participantes.
4. **Orunmilá × Ifá no Recife:** nos anos 1980 eram nomes não equivalentes (Carvalho via Halloy); hoje a retomada do jogo de Ifá tornou a obrigação anual. Em Cuba (Toutain p. 8), Orula é a "testemunha da criação" e só homens autorizados por Changó fazem Ifá. Em Chiousse (p. 285), Papai não pode falar de Ifá por ser o orixá da sua família.
5. **Obatalá feminino (Toutain p. 178):** "hoje macho e fêmea, antes mulher, a mãe do mundo", segundo Julio-Enrique Blázquez, ao lado das versões masculinas do Candomblé.
6. **Festa de Elegguá (Toutain p. 57):** 22–24 de outubro no central Méjico, ligada à iniciação de Celida Sánchez Zulueta; antes, segundo a família, 4 de dezembro, Reis e primeiro sábado do ano (pp. 172–173). Fecha a pendência das sessões fichamento-07/08.
7. **Legbá na Casa das Minas (Ferreira 2017):** ausente das famílias de voduns, função de mensageiro com os toquéns; hipótese (do autor) de que reaparece como o caboclo Légua Boji Buá no Terecô de Codó.

## 3. Candomblé × Umbanda, tradição e fontes de 2ª mão

- Chiousse fez campo em terreiros de candomblé e de umbanda (Salvador e São Paulo) e muitas vezes não separa: os registros mantêm `candomble_ketu` + `umbanda` (padrão das sessões anteriores) e citam o chefe de culto quando a autora o nomeia (Papai, Mãe Celeste, Mãe Sevi, Mãe Bia). Onde ela fala da Nigéria (justiça de Xangô) entrou `ioruba_nigeria` com nota.
- Halloy: sempre `xango_pernambuco` (nagô do Recife, família de santo estudada). Exu ligado a Santo Antônio aparece "no meio da jurema" e o registro diz isso.
- Toutain: `lucumi`, casa = central Méjico (Matanzas); o que ele diz da santería em geral leva casa "Cuba".
- Ferreira: `tambor_de_mina` (Casa das Minas); o trecho sobre Aguessy, `vodun_benim`. **O Terecô de Codó não está em `data/tradicoes.json`** → PENDENCIAS.
- O que os autores citam de outros (Segato, Ribeiro, Carvalho 1984, Cabrera 1954, Bolívar Aróstegui, Aguessy 1970, Barreto 1977, S. Ferretti 2009, M. Ferretti 2012, Verger 2002, Pessoa de Barros 1983, Mestre Didi 1987) ficou na `nota`, com `source_id` da fonte lida; nenhuma `via_source_id` nova (as primárias não foram conferidas).

## 4. O que ficou de fora (de propósito)

- **Mito de Xangô expulso do balé dos eguns (Halloy p. 168):** fichado nesta sessão e depois **retirado** antes do commit final, porque PENDENCIAS §3 já o deixa para o conselho (segredo de culto). Continua pendente.
- **Nascimento de Ifá** (Chiousse p. 285): é uma citação longa de Pessoa de Barros (1983), fora do catálogo; não fichado.
- **Interditos alimentares** de Oxalá (Chiousse p. 228; Halloy p. 324) e de Oyá (Chiousse p. 251; Halloy p. 325): só registros `tabus` retidos.
- **Disposição do peji e composição dos assentamentos** (Halloy pp. 322–326; Toutain p. 177): só o nível de hierarquia (quem fica ao lado de quem, Oxalá no fim, Orunmilá no alto); objetos e procedimento não.
- **Animais sacrificiais** entraram como já vinham sendo fichados (`animais`: Oxalá, Omulu, segundo Chiousse); a decisão geral sobre animais segue com o conselho.
- **Vallier 2011 e Cerqueira 2015** (item 4, "se houver tempo"): não relidos. Vallier já tinha pp. 811–831 lidas (falta só a parte final com notas e bibliografia); Cerqueira tem 377 pp. no acervo, das quais só pp. 82–88, 132, 155, 165 foram usadas.
- **Halloy, resto da tese** (pp. 186–814): a busca por nome de orixá mostra muitas ocorrências nos capítulos de iniciação e possessão (pp. 391–530), mais rituais que mitológicas; ficam para uma próxima sessão, com cuidado com fundamento.

## 5. Anti-cópia

Com `acervo/txt` (47 textos): **0 erros, 43 avisos "próximo"**, os mesmos de antes da sessão. Nos registros novos houve 3 avisos (Ferreira, em português): exu-101, exu-102, exu-103, todos **reescritos**. Limite conhecido: as fontes francesas (Chiousse, Halloy, Toutain) não são checadas contra tradução (PENDENCIAS §3); as paráfrases foram escritas reorganizando a ordem e o vocabulário e mantendo entre aspas só termos de informantes ("vaidosa", "visita da saúde", "fiesta de Elegguá").

## 6. Validadores

`validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas`, `validar_fichas`, `anticopia` (0 erros): OK. `python3 -m unittest discover -s tests` (48): OK. `e2e_revisao_site.py` e `e2e_modelo2_site.py`: OK. `cd site && npm ci && npm run build`: OK. `qa_site.py`: OK (68 páginas, 806/806 versões, 45 versões de itã, 0 vazamentos do acervo).
