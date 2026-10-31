# Fase 1 — Fichamento nº 2 (leitura das fontes)

**Data:** 2026-10-31 · Com a rede liberada, quatro fontes de texto aberto foram **lidas no original**, com a página registrada em cada afirmação.

## Fontes lidas

| Fonte | Trecho lido | Registros `fichado` |
|-------|-------------|--------------------:|
| Prandi, "Exu, de mensageiro a diabo" (*Revista USP* 50, 2001) | integral, pp. 46–63 | 39 |
| Bastide, *O candomblé da Bahia* (ed. pt 1961, cópia digital UFRJ) | cap. sobre o tempo sagrado, pp. 105–128 | 40 |
| Chiousse, *Divins thérapeutes* (tese EHESS, 1995, HAL) | parte sobre os orixás, pp. 225–291 | 49 |
| Silva, "Exu do Brasil" (*Rev. Antropologia* 55/2, 2012) | pp. 1085–1090 e 1100 | 12 |

**Total:** 166 registros, sendo **140 `fichado`** (lidos na fonte, com página) e 26 ainda em `pre_fichamento`. Nenhum está `revisado`: a revisão humana por praticantes e pesquisadores continua pendente, conforme o `CLAUDE.md`.

Afirmações que a fonte lida atribui a outra obra (por exemplo, Prandi citando Baudin, ou Bastide citando Nina Rodrigues) ficam com `source_id` = obra original e `via_source_id` = fonte efetivamente lida.

## Correções ao pré-fichamento

- Prandi (2001, p. 49) atribui a recuperação dos atributos africanos de Exu a **Bastide e Juana Elbein dos Santos**, não a Verger. O registro antigo foi substituído.
- O subtítulo do artigo de Silva (2012) foi confirmado: *tropos de uma identidade afro-brasileira nos trópicos*.
- A paginação de Prandi foi confirmada: pp. 46–63.

## Cobertura atual (nº de registros por atributo)

| atributo | exu | ogum | oxossi | xango | iemanja |
|---|---:|---:|---:|---:|---:|
| nomes | 5 | — | — | 1 | 1 |
| origem | — | — | 2 | 3 | 1 |
| dominios | 4 | 2 | 4 | 2 | 1 |
| funcoes | 6 | — | — | — | 1 |
| elementos | — | 1 | — | 2 | 3 |
| cores | 1 | 1 | 1 | 1 | 1 |
| dia_semana | 4 | 4 | 5 | 6 | 4 |
| saudacao | — | — | — | — | — |
| simbolos | 3 | 2 | 1 | 2 | 1 |
| alimentos | — | — | 1 | — | — |
| animais | 1 | — | — | 1 | — |
| qualidades | 3 | 2 | 1 | 1 | 1 |
| parentesco | — | 1 | 2 | 2 | 3 |
| equivalencias | 4 | 1 | 1 | — | — |
| sincretismo | 4 | 4 | 1 | 2 | 4 |
| itans | 2 | — | 3 | 2 | — |
| tabus | 1 | — | — | — | — |
| festas | 3 | 1 | 1 | 1 | 5 |
| historia_culto | 8 | 3 | 1 | 2 | 2 |
| iconografia | 5 | — | — | — | — |
| interpretacao_academica | 7 | 1 | 1 | 1 | — |

**Lacuna principal: saudações** (Laroiê, Ogunhê, Okê arô, Kaô Kabiecilê, Odoyá). Nenhuma das quatro fontes lidas as registra explicitamente. Fontes a consultar: Cacciatore (1977), Beniste (2011), Verger (1981).

## Divergências documentadas com página

A matriz completa é gerada automaticamente em [`data/fichamento/divergencias.json`](../../data/fichamento/divergencias.json) por `python3 scripts/divergencias.py` (**26 atributos** com mais de uma versão). Destaques:

| Orixá | Atributo | Versões (fonte, página) |
|-------|----------|--------------------------|
| Ogum | dia da semana | quinta, com Oxóssi (Bahia em geral) × terça (Opô Afonjá) × quinta (Porto Alegre), todas em Bastide 1961, pp. 119–127 |
| Ogum | cores | azul-escuro (Ketu) × verde e vermelho (casas que se dizem nagôs), Chiousse p. 266 |
| Xangô | dia da semana | quarta (Bahia, Gantois, Opô Afonjá) × terça (Porto Alegre) × quinta (Recife), Bastide pp. 106, 119, 120, 127 |
| Xangô | sincretismo e festa | São Jerônimo (30/9) × São João (24/6) × Reis (6/1); "Xangô velho × jovem" (Agodô/Aganju), Chiousse pp. 240–241; Bastide p. 107 |
| Xangô | origem | 3º ou 4º alafin de Oyó, Chiousse p. 240 |
| Xangô | itã | quem rouba a magia do fogo: Iansã (Bahia) × Oxum (Rio de Janeiro), Bastide p. 123 |
| Iemanjá | dia da semana | sábado (Bahia) × sexta, com Odé (Porto Alegre), Bastide pp. 119–120 |
| Iemanjá | parentesco | filha de Oxalá (Bastide p. 125) × esposa de Oxalá e mãe de Xangô, às vezes de todos os orixás (Chiousse p. 236) |
| Oxóssi | dia da semana | quinta (Bahia) × segunda e sexta, como Odé (Porto Alegre), Bastide p. 119 |
| Oxóssi | itã de origem | caçador de uma flecha só (Verger) × médico que aprende com Ossaim (versão de um pai de santo, que **recusa** a de Verger), Chiousse pp. 259–260 |
| Oxóssi | qualidades | Logunedé como forma de Oxóssi (informantes de Chiousse, p. 259) × orixá distinto (Lopes 2006) |
| Exu | sincretismo | Diabo (Prandi pp. 51–52) × Santo Antônio, São Gabriel, São Benedito, São Pedro, São Bartolomeu (Silva p. 1088; Chiousse p. 289) × Menino Jesus (Cuba; Silva p. 1088) |
| Exu | qualidades | menos de dez avatares no candomblé (Silva p. 1089) × pelo menos 21 (Chiousse p. 290) × lista de 18 nomes (Ferreira 2000 via Prandi p. 55) |
| Exu | estatuto | orixá pleno × raramente iniciado ("carrego" ou "carga" de Exu): Carneiro via Prandi p. 62; Chiousse p. 290 |

## Observações metodológicas para a página "Metodologia e limitações"

- Chiousse (p. 241) registra um pai de santo hesitando entre as duas qualidades de Xangô e os santos correspondentes. É um exemplo concreto de que a tradição oral varia, até dentro de uma mesma casa.
- Bastide (pp. 119–128) mostra que a distribuição dos orixás pelos dias da semana muda de cidade para cidade e de casa para casa. Ele mesmo lembra que a semana iorubá tem quatro dias e que a adaptação à semana de sete dias gerou variação.
- Fontes coloniais e missionárias (Baudin, Bowen, Bouche, Frobenius) aparecem como **documento do olhar europeu**, sempre lidas via autores que as criticam.

## Ainda não lido (texto aberto, mas o acesso falhou)

- Mones Guevara (2024, SciELO México): conexão recusada por `scielo.org.mx`.
- Peel (2016, OAPEN): ainda não tentado.

## Próximos passos

1. **Saudações e nomes iorubás**: Cacciatore (1977) e Beniste (2011), que precisam de exemplar.
2. **Verger (1981, 1957)** e **Prandi, *Mitologia dos Orixás* (2001)**: base dos itãs e da origem africana. Também precisam de exemplar.
3. **Equivalências** com inquices e voduns: Parés (2006), Castro (2001) e Lopes (1988).
4. Concluir o pré-fichamento restante (26 registros), lendo as fontes ou descartando registros.
5. **Revisão humana**: enviar as 5 fichas de fichamento a um(a) praticante e a um(a) pesquisador(a).
