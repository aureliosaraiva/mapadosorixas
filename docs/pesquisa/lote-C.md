# Lote C — cosmologia e hierarquia

**Data:** 2026-11-01 · **Sessão:** loteC (trabalhadora, coordenada pela orquestradora) · **Plano:** [varredura 4](relatorio-varredura-04.md) §6, lote C.

**Arquivos editados:**

- `data/fichamento/{olodumare,orum,aie,odudua,olokun,egungun,iyami}.json` (novos);
- `data/fontes/catalogo.json` (única sessão autorizada nesta rodada);
- arquivos gerados (`data/orixas/*`, `data/entidades.json`, `divergencias.json`);
- docs.

**Não editados, por regra da rodada:** `data/itans.json` e `data/conexoes_alvos.json`. O que achei para esses dois arquivos está em §5 e §8, para integração posterior.

## 1. Resumo

Os números de "Antes" já incluem o lote A, que entrou na `main` durante esta sessão (rebase).

| Indicador | Antes | Depois |
|---|---:|---:|
| Registros de fichamento | 442 | **509** (+67, todos `fichado`) |
| Entidades com ficha | 10 | **17** (+ Olodumare, Orum, Aiê, Odudua, Olokun, Egungun, Iyami) |
| Versões nas fichas | 424 | 491 |
| Versões de `hierarquia` (página Cosmologia) | 5 | **43** (+38) |
| Atributos com versões divergentes | 74 | 82 |
| Fontes no catálogo | 422 | 423 (+ Verger 1965, Persée) |
| Anti-cópia com texto integral (38 obras) | — | **0 erros; 0 avisos "próximo" nos registros novos** |

Registros por entidade:

| Entidade | Registros |
|---|---:|
| Olodumare | 18 |
| Odudua | 14 |
| Egungun | 14 |
| Orum | 9 |
| Olokun | 5 |
| Iyami | 4 |
| Aiê | 3 |

**Sem registro:**

- **Orixás funfun:** nenhuma fonte lida usa o termo.
- **Orí:** não há entidade na lista-mestra; o achado está em §6.

## 2. Fontes lidas e páginas

| Fonte | Conf. | Texto | Páginas lidas e fichadas |
|---|:-:|---|---|
| Ellis 1894 | C | IA, `_djvu.txt` da cópia Wellcome `b21781370`, com OCR melhor nas pp. 37–38 que a cópia Google | 35–45 (Olorun, Obatala, Odudua, Yemaja), 70–72 (Olokun, Olosa), 86–92 (comentários e mitos de origem), 107–109 (Egungun), 125–128 (Olori e almas) |
| Dennett 1910 | C | IA `_djvu.txt` | 17–21 (criação em Ilobe, pedras de Ifẹ̀), 28–29 e 58–59 (Egun), 72 (Olorun e Jakuta), 73–77 (Odudua), 106–115 (Olokun) |
| Farrow 1926 | C | IA `_djvu.txt` | 23–33 (Ser Supremo), 43–45 (Obatala, Odudua), 130–133 (alma, Orun) |
| Johnson 1921 | B | IA `_djvu.txt` | 3–4 (migração de "Meca"), 26–28 (religião, Ori), 143 (Oduduwa) |
| Ogungbemi 2021 | B | PDF sem camada de texto, lido por **OCR local (tesseract)** | 41–43, 48–51, 62–63 |
| Bewaji 1998 | B | PDF (ASQ) | 1, 7–10 |
| Akin-Otiko 2024 | B | PDF; PDF p. 1 = p. 54 | 58, 60 |
| Jock 2020 | B | PDF (HTS) | 1, 6–7 |
| Fámúlẹ̀ 2021 | B | PDF (YSR) | 1–17 |
| Santos 2008 | B | PDF (Sankofa); PDF p. 1 = p. 59 | integral; fichadas 59–60 e 72 |
| Carvalho et al. 2019 | B | PDF (Fractal) | 214–219; fichadas 215–216 |
| Zacharias 2010 | B | PDF (Esboços) | 158–159 |
| Bastide 1961 | A | PDF UFRJ; paginação do PDF = livro | cap. III, "A estrutura do mundo", **pp. 134–207**, mais 48, 96–99, 115–116, 124, 224, 243, 262 e 290–292 (Olorum, Odudua) |

**Não lidas:**

- Igboin 2014 e Layi 2016: `journal.sadra.ac.id` responde HTTP 500.
- Baudin 1885: texto baixado, mas fora da lista do lote; ficou sem fichamento.

**Pistas verificadas:**

| Pista | Resultado |
|---|---|
| Verger 1965, Ìyámi (*Journal de la Société des Africanistes* 35, pp. 141–243) | **Aberto no Persée** e catalogado como `verger-1965-iyami` (`conferido_web`). O PDF tem desafio anti-robô (altcha); não contornei. → PENDENCIAS §1 |
| Verger 1966, "The Yoruba High God" (*Odu* 2) | Nenhuma cópia aberta (IA, Crossref). Anotado em `verger-2007-high-god` |
| Abimbola 1975, UNESDOC | Cloudflare 403; não deu para verificar. Anotado em `abimbola-1975-sixteen` |

## 3. Critérios aplicados

- **Fontes coloniais e missionárias** (Ellis, Dennett, Farrow) entram como documento histórico, com nota de viés em todo registro. Nenhum atributo fica sustentado só por elas: cada um tem pelo menos uma versão de fonte B ou A, ou fica explicitamente em contraste com elas.
  - Ellis: evolucionismo, "deus da natureza".
  - Farrow: monoteísmo primitivo, missão declarada.
  - Dennett: esquema próprio, Jakuta como "deus-pai".
- **Farrow e Dennett repetem Ellis.** Onde só repetem (Olori; dilúvio de Olokun em Dennett, pp. 114–115), cito Ellis e não dupliquei o registro.
- **Tradições.**
  - Nigéria/Costa dos Escravos → `ioruba_nigeria`, com `casa_ou_regiao`: Lagos, Abeokuta, Oyó, Ifẹ̀, Òkèigbó.
  - Bahia → `candomble_ketu`.
  - Cuba → `lucumi`, via Bastide citando Cabrera, *El Monte*, p. 100.
  - Zacharias, Santos e Carvalho dizem "candomblé" sem nação; a aproximação a `candomble_ketu` está anotada em `nota`.
- **Iyami** (entidade `sensivel`):
  - só 4 registros, de leitura acadêmica e histórica do culto: designação "Mães Ancestrais"; pouca difusão no Brasil; sociedades Gẹ̀lẹ̀dẹ́ e Ẹgbẹ́; Sociedade Osoronga no Rio de Janeiro;
  - nada de poderes, mitos, cânticos, aves ou práticas;
  - todos com nota para o conselho.
- **Egungun:** fichei a posição cosmológica, as festas e a distribuição por nação. **Não fichei** cargos, objetos, fixação dos mortos, iniciação nem etapas rituais, que Bastide (pp. 172–180) e Fámúlẹ̀ descrevem em parte (§7).
- **Sacrifícios humanos** mencionados por Ellis (Olokun, p. 71), Dennett (p. 110) e Johnson (p. 143, Oduduwa) não foram fichados. São afirmações de terceiros, de olhar colonial, sem relação com a hierarquia; ficam anotados aqui.

## 4. Versões lado a lado (destaques)

- **Olodumare/Olorun.** Seis leituras convivem:
  - deus do céu ocioso, sem culto e sem onipotência (Ellis, olodumare-001);
  - Ser Supremo de classe à parte (Farrow, olodumare-004);
  - Todo-Poderoso, distante demais, com os orixás como mediadores (Johnson, olodumare-007);
  - desenvolvimento de Jakuta (Dennett, olodumare-009);
  - fonte de tudo e não idêntico ao Deus cristão (Ogungbemi, Bewaji, Akin-Otiko);
  - no Candomblé da Bahia, criador que delegou a criação a Oxalá, depois substituído por ele no céu (Bastide, olodumare-015/016; Zacharias, olodumare-017). Em Cuba, o "Pai Eterno" que reparte o universo (olodumare-018).

  A disputa Ellis × Farrow sobre a influência missionária está registrada como `interpretacao_academica` (olodumare-003, 011, 013).
- **Odudua.**
  - Deusa-terra coeva de Olorun (Ellis).
  - Herói migrante masculino (F. S. em Dennett; Johnson).
  - Filho de Olodumare que cria a terra (Johnson, mitologia de Ifẹ̀).
  - Mensageiro que toma o lugar de Orixanlá (Ogungbemi).
  - Sexo que varia por região (Bastide, via Dennett e Frobenius).
  - Na Bahia, metade-terra do par com Obatalá e culto desaparecido (Bastide).
- **Olokun.** Deus masculino do mar, filho de Yemaja (Ellis, Dennett) × deusa do oceano, mulher de Oduduwa (Johnson, mitologia de Ifẹ̀) × dono do mar na partilha cubana (Cabrera via Bastide).
- **Orum.**
  - Céu como abóbada sólida (Ellis) e como morada divina (Farrow).
  - Terra dos mortos sob a terra (Ellis) × Orun-rere como morada dos mortos (Farrow).
  - Reino dos ancestrais (Fámúlẹ̀).
  - Plano espiritual oposto ao Aiyê (Carvalho; Zacharias).
- **Aiê:** mundo físico (Carvalho, Zacharias) × "o mundo, terra e céus" (glosa de Farrow).
- **Egungun.**
  - Etimologias: "osso" (Ellis) × "o que traz estabilidade" (Fámúlẹ̀).
  - Festa em junho (Ellis, Costa dos Escravos) × 2 de novembro na Bahia (Bastide).
  - Aparição só nas casas nagôs; ausente em Ijexá, Jeje e Angola (Bastide, egungun-012).

## 5. Itãs achados (para `data/itans.json`; não editado)

Resumos próprios, com fonte e página. Nenhum odu é citado pelas fontes nestes trechos, salvo onde indicado.

1. **O casal na cabaça.** Ellis, pp. 42–43; repetido por Dennett, p. 74, e Farrow, p. 45.
   - Obatala e Odudua ficam presos, no princípio, numa cabaça escura.
   - Na briga, ele a cega; ela o amaldiçoa a comer só caramujos.
   - Entidades: `odudua`, Obatala (não ligado a `oxala` sem fonte).
2. **A criação em Ilobe.** Dennett, pp. 17–19, relato da sacerdotisa Oja por meio de Togun.
   - Yemuhu e Orishala fazem o mundo, acompanhados de Ajajuno, e viram pedra.
   - Os 16 caramujos de Yemuhu tornam-se a cabeça de Eleda; Eleda dá forma a Ifá.
   - Dennett identifica Yemuhu a Odudua (p. 73).
3. **A terra sobre as águas (migração de Okambi).** Ellis, pp. 90–92.
   - Enviados vindos do interior acham só água.
   - Uma noz de dendê e terra caem de um pano preto; nasce uma palmeira de 16 ramos; uma galinha espalha a terra; o lugar vira Ifẹ̀.
4. **A criação da terra firme.**
   - Versões resumidas por Jock, p. 6 (Olorun envia Oduduwa com terra, galo e dendê; ou Obatala embriagado e Oduduwa assumindo a tarefa, via Akintoye e Ayandele).
   - Versão de Ogungbemi, pp. 50–51 (via K. Abimbola): Oduduwa cria a terra com os objetos de Obatala e reina em Ifẹ̀.
   - Bastide, p. 48: na Bahia, Oxalá bebe vinho de palma e completa a tarefa com Odudua.
5. **O dilúvio de Olokun.** Ellis, pp. 64 e 71; Dennett, pp. 114–115, copia Ellis.
   - Irado com o abandono dos homens, Olokun inunda a terra.
   - Obatala salva os sobreviventes, puxando-os ao céu por uma corrente, ou prende Olokun com sete correntes.
   - Ifá e Odudua tornam o mundo habitável de novo.
6. **Os filhos de Yemaja.** Ellis, pp. 43–45.
   - Yemaja, filha de Obatala e Odudua, casa com Aganju; o filho Orungan a violenta.
   - Do corpo dela nascem 15 divindades (Olokun, Xangô, Ogum, Oxóssi, Oxum, Oyá, Obá etc.); no lugar ergue-se Ifẹ̀.
   - Relevante para os 5 do MVP; nenhum registro novo foi criado para Iemanjá (arquivo de outra entidade).
7. **A partilha do universo** (Cuba). Cabrera via Bastide, pp. 189–190: o Pai Eterno reparte os domínios entre os filhos; o vento de Oyá espalha as ervas de Ossaim.
8. **Egúngún e a estabilidade do mundo** (odù Ọ̀wọ̀rìn-Àṣẹ́yìn). Fámúlẹ̀, pp. 14–15: com o mundo ameaçado de ruir, Ifá prescreve oferenda a Olódùmarè, que manda 400 divindades e Egúngún à terra. **Odu citado pela fonte.**

## 6. Orí (sem entidade na lista-mestra)

| Fonte | Página | Achado (paráfrase) |
|---|---|---|
| Ellis 1894 (C) | 125–126 | Três espíritos interiores; Olori, "dono da cabeça", também chamado Ori, é guardião e traz sorte; símbolo: meia-cabaça com búzios |
| Johnson 1921 (B) | 27–28 | Ori, divindade doméstica do destino, cultuada pelos adultos; imagem de 41 búzios em forma de coroa, destruída à morte do dono |
| Farrow 1926 (C) | 130–131 | Repete Ellis; lê Olori como "deificação da inteligência e prudência" |
| Zacharias 2010 (B) | 158–159 | No Brasil, Olori = orixá de cabeça, assimilado ao Eledá; Ori como cabeça e psique (leitura junguiana) |
| Bastide 1961 (A) | 184–185 | Eleda como "anjo da guarda", intermediário entre deuses e homens. As casas tradicionais não o confundem com o orixá de cabeça; nas bantas há essa tendência. Cita Dennett, cap. VII |

Sugestão: criar `ori` como `conceito_cosmologico` (decisão da sessão de modelo; PENDENCIAS §3a).

## 7. Para o conselho (não registrado)

- **Iyami.** Santos 2008 descreve poderes, cólera, aves e cânticos do Gẹ̀lẹ̀dẹ́ a partir de Prandi e Verger. Carvalho 2019 trata de uma sociedade fechada cujo tema de pesquisa é o segredo. Fichei só a camada histórico-acadêmica. Verger 1965, aberto mas não baixado, é a obra central: a leitura depende da decisão do conselho.
- **Egungun.** Detalhes rituais publicados por Bastide (pp. 172–180: cargos, varas, fixação em vasos, Yansan e Eruosaim na sociedade, evocação do 7º ano) e por Fámúlẹ̀ (etapas do Ọdún Egúngún em Òkèigbó). Têm caráter de fundamento: não fichados.
- **Olokun do Benim (Edo).** Dennett, p. 110: rio Benim, esposas Oha e Sapoba. O recorte segue pendente (varredura 4 §3).
- **Oxalá como "divindade suprema" na Bahia** (Bastide, pp. 115, 192) e **Orisala** com nomes locais (Johnson, p. 27). São achados para a sessão de Oxalá, que pode também confirmar o grupo funfun com outra fonte.

## 8. Arestas propostas (para `data/conexoes_alvos.json`; não editado)

| Registro | Tipo | Alvos | Observação |
|---|---|---|---|
| odudua-007 | parentesco | Odudua ↔ Olokun (cônjuges); Odudua → Ogum (avô) | Oranmiyan e Isedale não estão na lista-mestra |
| olokun-002 | parentesco | Yemaja → Olokun (mãe); Olokun ↔ Olosa (cônjuges, irmãos) | Yemaja de Ellis = nó `iemanja`? Decidir; Olosa e Olokun-su não estão na lista-mestra |
| olokun-004 | parentesco | Iemanjá/Yemoja → Olokun (mãe) | idem |

Os três aparecem como aviso `sem_mapa` no `gerar_fichas.py`, o que é esperado.

## 9. Anti-cópia

- `/tmp/refs` com 38 textos integrais (`baixar_refs.py`).
- Os `_djvu.txt` do IA para Ellis, Dennett, Farrow e Johnson e o OCR de Ogungbemi foram repostos à mão depois do script. O `baixar_refs.py` substitui o texto de Ellis por um PDF do IA sem OCR (496 palavras) e o de Ogungbemi por um PDF sem texto; convém que a próxima sessão também reponha esses arquivos.
- 1ª passagem: **1 erro** (orum-009, 8 palavras de Zacharias) e 5 avisos "próximo" (egungun-013, iyami-002, odudua-011, olodumare-017, olodumare-018). Todos reescritos.
- 2ª passagem: **0 erros, 0 avisos** nos registros novos.
- Três citações curtas entre aspas ficaram por serem glosas de etimologia (olodumare-008, odudua-005, egungun-008).

## 10. Verificação

- `validar_fontes`, `validar_fichamento`, `divergencias` (82 após o rebase), `gerar_fichas`, `validar_fichas`: OK.
- `anticopia` com referências: OK.
- `unittest`: 48 testes OK; `e2e_revisao_site`: ok.
- `e2e_modelo2_site`: falhou depois do rebase. A adulteração "cartão em pesquisa com texto" mirava o 1º cartão de tipo "Ancestrais", e Egungun agora tem ficha. Ajustei o marcador para o cartão de Iyami, que no cenário sintético continua em pesquisa (`tests/e2e_modelo2_site.py`, uma linha). Depois do ajuste: ok.
- `npm run build` e `qa_site.py`: ok, antes e depois do rebase sobre o lote A (números finais no ESTADO).
