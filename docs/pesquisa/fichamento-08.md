# Fichamento 08: últimas fontes abertas da varredura 3 (Halloy, M. Ferretti, Argyriadis, Toutain, Querebentã)

Sessão `fich08` (2026-11-01). Só esta sessão editou `data/` nesta rodada. Esquemas, validadores e site não foram tocados.

**Resultado em uma linha:** das cinco tarefas, só a de M. Ferretti 2001 rendeu registro (1 novo, exu-094). Argyriadis 2005 foi lido inteiro e não trata dos 5 orixás. Halloy 2005 e Toutain 2019 estão atrás do desafio anti-robô do HAL e não foram lidos. *Querebentã* não tem texto aberto. Os bloqueios estão em [PENDENCIAS](PENDENCIAS.md) §1–2.

## 1. Restante de Halloy 2005 (tarefa 1): bloqueado

O PDF integral (`hal.science/tel-04260456/file/...`) devolve a página do Anubis ("Making sure you're not a bot"), o mesmo bloqueio que a sessão anticopia2 registrou. `scripts/baixar_refs.py` também falhou. Pela regra do projeto, não contornei o desafio. Também procurei espelhos institucionais legítimos: o Wayback não tem cópia do arquivo principal e o registro da ULB (DI-fusion) não deu acesso daqui. **Nenhum registro novo.** As pp. 163–169, fichadas na fich06, continuam valendo (exu-083 a exu-086, ogum-053 a ogum-056, oxossi-028 a oxossi-031, xango-040 a xango-042, iemanja-048 a iemanja-050).

→ [PENDENCIAS](PENDENCIAS.md) §1 (linha do HAL, agora P2): o autor salva o PDF em `/tmp/refs-pdf/halloy-2005-intimite.pdf` e uma sessão retoma a tarefa. Lembrete para quem retomar: página impressa = PDF − 1.

## 2. M. Ferretti 2001, pp. 84–94 (tarefa 2)

**Acesso.** O PDF baixou pelo `baixar_refs.py` (`periodicos.sbu.unicamp.br`). Li as pp. 84–94 no original (impressa = PDF + 74) e voltei às pp. 77–81 para conferir a Casa de Nagô.

**O que as páginas contêm.** As pp. 84–89 tratam da Casa Fanti-Ashanti, de Pai Euclides, e do documentário *Atlântico Negro: Na rota dos orixás* (1998). O texto discute a relação do terreiro com o Benin e a troca da identidade "fanti-ashanti" por jeje-nagô, jeje-mahi e ketu. Seguem a conclusão (pp. 87–89), as notas (pp. 89–91) e a bibliografia (pp. 91–94). **Não há lista de voduns e orixás da Casa de Nagô nem equivalências com a Casa das Minas.** Sobre a Casa de Nagô, o artigo só diz que lá voduns e orixás se manifestam de modo discreto, sem brado e dançando em conjunto, como os voduns da Casa das Minas (p. 78). Isso foi lido pela trad02 e não fala de nenhum dos 5 orixás.

**1 registro novo `fichado`:**

| Orixá | Registro | Atributo | Conteúdo | Casa | Página |
|---|---|---|---|---|---|
| Exu | exu-094 | historia_culto | a mina-jeje maranhense não cultua Exu nem joga búzios; na Casa Fanti-Ashanti esses traços vieram de fora dessa tradição (contato com africanos, discos cubanos) | São Luís: tradição jeje (Casa das Minas) × Casa Fanti-Ashanti | 85 |

O registro converge com exu-092 (Legba sem culto organizado na Casa das Minas, que é S. Ferretti lido via Prandi) e contrasta com exu-093 (Legbara assentado na casa paulista de Pai Francelino). A nota indica que a Casa Fanti-Ashanti também faz toques de Candomblé, para não confundir as tradições.

**`data/conexoes_alvos.json` não mudou.** As páginas não trazem equivalência vodum × orixá nem sincretismo, e exu-094 é `historia_culto`, que não gera aresta.

**Ficou de fora, de propósito:**
- o nome religioso de Pai Euclides e as cenas do vídeo com vodunsis e tobôssis (p. 84);
- a menção a "Raminho de Oxossi" (p. 87; nome de pessoa, não afirmação sobre o orixá);
- o "Terreiro de Yemanjá" de Jorge Itaci (nota 4, p. 89; nome de terreiro).

## 3. Argyriadis 2005 (tarefa 3): lido, nada a fichar

**Acesso.** `journals.openedition.org/jsa/3022` não tem link de PDF, mas o texto em HTML abriu. Percorri o artigo inteiro, com notas e bibliografia (¶1–¶56, notas 1–31), pela ferramenta de leitura de páginas (em duas partes, até o fim), procurando Yemayá, Elegguá, Oggún, Ochosi e Changó, com variantes de grafia, e também "guerrier": **nenhuma ocorrência.** O único orixá citado pelo nome é Ochún (¶17), na fala de uma entrevistada. **Regla** aparece só como bairro de Havana (¶38), ao lado de Guanabacoa e Marianao. O artigo trata de redes de padrinhos e afilhados (*ramas*), parentesco ritual e da difusão da santería entre Cuba e o México, não de atributos de orixás. A sugestão "Yemayá de Regla" da varredura não se confirma nesta fonte. **Nenhum registro.**

Isso fica anotado em [PENDENCIAS](PENDENCIAS.md) §1, na linha do OpenEdition. Para o anti-cópia, o texto não precisa entrar em `/tmp/refs`, porque nenhum registro do fichamento cita Argyriadis. As citações dele estão só em `tradicoes.json` e no glossário, que já foram conferidos na trad02.

## 4. Toutain 2019, p. 57 (tarefa 4): bloqueado

O PDF (`theses.hal.science/tel-03191332/file/Toutain_Maxime.pdf`) está atrás do mesmo Anubis. O Wayback tem uma captura de 2024-11-15, mas o download dela foi recusado neste ambiente, e não insisti. **A "fiesta de Elegguá" (22–24 de outubro, casa de Elegguá Alagbana, p. 57) não foi fichada.** A paráfrase no §3 do [fichamento-07](fichamento-07.md) é leitura de outra sessão, e a regra exige leitura no original. O registro exu-089 (festa de Elegguá em outubro, p. 11) continua como está.

→ [PENDENCIAS](PENDENCIAS.md) §1 (linha do HAL). Ao retomar: impressa = PDF − 11.

## 5. S. Ferretti, *Querebentã* (tarefa 5)

Busquei texto aberto (repositórios UFMA, CORE, SciELO) e não achei. Só há exemplar comercial, e o panteão da Casa das Minas continua lido via Prandi. A linha em [PENDENCIAS](PENDENCIAS.md) §2 foi atualizada.

## 6. Anti-cópia

- `python3 scripts/baixar_refs.py --destino /tmp/refs`: 23 de 57 fontes com texto, entre elas `ferretti-m-2020-pureza`. Halloy, Toutain, Argyriadis e outras não baixaram, todas já listadas em PENDENCIAS.
- `ANTICOPIA_REFS=/tmp/refs python3 scripts/anticopia.py`: a 1ª passagem deu **1 erro**, no `valor` de exu-094 ("o culto a Exu e o jogo de", 8 palavras iguais à p. 85). Reescrevi como "a mina-jeje maranhense não cultua Exu nem joga búzios". **Resultado final: 0 erros.**
- Avisos "próximo" (6–7 palavras): 35, nenhum em exu-094. Os outros são os mesmos classe C já justificados em [anticopia-02](anticopia-02.md).
- Sem referências: OK.

## 7. Números depois da rodada

- **Registros:** 303 (287 `fichado`, 16 `pre_fichamento`). Por orixá: Exu 94, Ogum 64, Iemanjá 59, Xangô 52, Oxóssi 34.
- **Divergências:** 41 atributos, sem mudança.
- **Fichas:** 285 versões.
- **Grafo:** 54 nós, 61 arestas; 24 entidades equivalentes, sem mudança.
- **Catálogo:** sem mudança (316 fontes).
