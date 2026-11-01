# Fichamento 07: voduns × orixás no Tambor de Mina (Prandi 2005), nação Efon e correções de catálogo

Sessão `fich07` (2026-11-01). Nesta rodada, só esta sessão editou `data/fontes/catalogo.json`, `data/fichamento/*.json`, `data/tradicoes.json` e `data/glossario.json`. Esquemas, validadores e site não foram tocados.

**Mudança de escopo.** A tarefa 1 (fichar o §4 de [`tradicoes-02`](tradicoes-02.md)) foi cancelada pela orquestradora no meio da sessão, porque a fich06 já a tinha feito (39 registros, ver o adendo de [`fichamento-06`](fichamento-06.md)). Eu tinha conferido no original as páginas de Halloy, Pitta, Toutain, Oro e Cerqueira, mas ainda não tinha gravado nenhum registro. Por isso não houve duplicata para descartar. O que essa conferência rendeu de útil está no §3.

Os PDFs ficaram fora do repositório (`/tmp`). O anti-cópia rodou contra o texto de Prandi 2005, Castillo 2022 e M. Ferretti 2001 (`ANTICOPIA_REFS`). Deu 1 erro, na descrição de `candomble_efon`, que reescrevi. Resultado final: 0 erros.

## 1. Prandi 2005, *Nas pegadas dos voduns* (tarefa 2)

**Acesso.** Versão do autor no site da USP, lida inteira (pp. 1–36). A nota final diz que é a versão atualizada, de janeiro de 2005, do artigo publicado em *Afro-Ásia* 19/20 (1997), pp. 109–133. A paginação citada é a da versão do autor. A correspondência com o livro *Somavó* (pp. 63–94) continua pendente.

**Duas casas, dois tipos de registro.**
- **Casa das Minas (São Luís), pp. 5–8.** Prandi diz que resume o panteão a partir de S. Ferretti (1989; *Querebentã*, 2ª ed. 1996). Esses registros levam `source_id: ferretti-1985-querebenta` e `via_source_id: prandi-2005-pegadas-voduns`.
- **Casa das Minas de Tóia Jarina (Diadema, SP), de Pai Francelino.** É o campo de pesquisa do próprio Prandi: pp. 13–16 e o Quadro 1, na p. 25. A casa se define como mina-jeje, mina-nagô e encantaria. Fonte direta.

**16 registros novos `fichado`**, todos com tradição `tambor_de_mina`:

| Orixá | Registro | Atributo | Conteúdo | Casa | Página |
|---|---|---|---|---|---|
| Exu | exu-091 | equivalencias | Legba/Legbara, chamado Exu em outras nações; papel de trapaceiro | Casa das Minas (via) | 8 |
| Exu | exu-092 | sincretismo | sem culto organizado, identificado com Satanás, não é mensageiro (papel dos toqüéns); cantigas para que se afaste | Casa das Minas (via) | 8 |
| Exu | exu-093 | historia_culto | Legbara assentado para a casa e para filhos, com quarto próprio, propiciado nas grandes obrigações | Tóia Jarina | 13–14 |
| Ogum | ogum-062 | equivalencias | Doçu e Bedigá → Ogum; Doçupé → Ogunjá | Tóia Jarina | 25 |
| Ogum | ogum-063 | sincretismo | São Jorge (Ogum); Santos Reis (Doçu, Bedigá); Santo Antônio (Doçupé) | Tóia Jarina | 25 |
| Ogum | ogum-064 | festas | 23 de abril (São Jorge) | Tóia Jarina | 15 |
| Oxóssi | oxossi-033 | equivalencias | Agüê e Azacá → Oxóssi | Tóia Jarina | 25 |
| Oxóssi | oxossi-034 | sincretismo | Santa Helena (Odé, Agüê); São Sebastião (Azacá) | Tóia Jarina | 25 |
| Xangô | xango-049 | equivalencias | Badé, vodum do corisco (Quevioçô), "Xangô dos nagôs" | Casa das Minas (via) | 8 |
| Xangô | xango-050 | equivalencias | Badé e Boço Vondereji → Xangô; Averequete → Xangô Aganju; Xadantã → Xangô Airá | Tóia Jarina | 25 |
| Xangô | xango-051 | sincretismo | São Pedro (Xangô, Badé); São Benedito, Santo Antônio, São José para os outros voduns | Tóia Jarina | 25 |
| Xangô | xango-052 | festas | Badé de 28 a 30 de junho (São Pedro); Badé Zorogama em 29 de setembro | Tóia Jarina | 15–16 |
| Iemanjá | iemanja-056 | equivalencias | Abé, vodum jovem e feminino do cometa (Quevioçô), corresponde a Iemanjá | Casa das Minas (via) | 8 |
| Iemanjá | iemanja-057 | equivalencias | Abê e Naê → Iemanjá | Tóia Jarina | 14, 25 |
| Iemanjá | iemanja-058 | sincretismo | N. S. das Candeias (Iemanjá); N. S. da Conceição (Abê) | Tóia Jarina | 14, 25 |
| Iemanjá | iemanja-059 | festas | 8 de dezembro (Abê, Naité, Iemanjá); 2 de fevereiro (presente de Abê) | Tóia Jarina | 15–16 |

**Divergências novas ou ampliadas.** Todas ficam lado a lado e nenhuma versão é eleita.
- **Xangô, equivalências.** Badé no Tambor de Mina (xango-047, xango-049, xango-050) × Sobo no Seja Hundê (xango-048). Na casa paulista, Sobô corresponde a Oiá-Iansã (pp. 14, 25). Na Casa das Minas, Nochê Sobô é a mãe dos voduns de Quevioçô e representa raio e trovão (p. 7). Isso está anotado em xango-049 e xango-050.
- **Exu, lugar de Legba.** Sem culto e associado a Satanás na Casa das Minas (exu-092) × assentado e propiciado na casa paulista (exu-093). Também contrasta com outros terreiros de São Luís, onde Legba tem lugar de destaque (exu-092).
- **Oxóssi, sincretismo.** Santa Helena e São Sebastião na casa paulista × os santos já fichados para Bahia e Umbanda.
- **Iemanjá, sincretismo.** Candeias para a orixá × Conceição para o vodum Abê, na mesma casa.
- **Ogum e Iemanjá, festas.** Datas da casa paulista × as já fichadas.

**Ficaram de fora, de propósito:**
- iniciação (aperê, recolhimento, tobóssi, pp. 17–18);
- sacrifícios e comida dos tambores (pp. 16–17);
- a lista de iniciados com nomes (Quadros 3–5) e as relações familiares dos membros (pp. 19–20), que são dados pessoais;
- a frequência de assentamentos do Quadro 2 (p. 26). Dela só entrou uma menção em nota (ogum-062).

**Grafo** (`data/conexoes_alvos.json`). 10 voduns novos: Abê/Abé, Naê, Boço Vondereji, Averequete, Xadantã, Doçu, Bedigá, Doçupé, Agüê e Azacá. Também o santo Santa Helena. Foram mapeados os 12 registros de equivalência e sincretismo; exu-092 vai para o nó `figura:diabo`. Totais depois de regenerar:
- **54 nós e 61 arestas**: 24 de equivalência, 23 de sincretismo, 10 de parentesco, 3 de companheiro de culto e 1 de associação;
- **24 entidades equivalentes**.

## 2. Correções de catálogo e `candomble_efon` (tarefa 3)

A fich06 já tinha corrigido Pitta (1985), Cerqueira, Toutain e a nota de paginação de Halloy. Nesta sessão:

| Fonte | Correção |
|---|---|
| `ferretti-m-2020-pureza` | Anotado em `observacoes`: o texto é o artigo de 2001 (*Ciencias Sociales y Religión / Ciências Sociais e Religião*, ano 3, n. 3, pp. 75–94, out. 2001), conferido no cabeçalho do PDF. Ano citado mantido. Impressa = PDF + 74. Nova evidência em `periodicos.sbu.unicamp.br` |
| `halloy-2005-intimite` | Evidência do PDF integral no HAL. Nota sobre a conversão de páginas abaixo |
| `toutain-2019-santos` | Evidência do PDF integral (`/file/Toutain_Maxime.pdf`) |
| `prandi-2005-pegadas-voduns` | Lido inteiro. Anotados a origem em *Afro-Ásia* 1997 e o critério de `via` para o panteão da Casa das Minas |
| `castillo-2022-ogum` | Anotado o uso para `candomble_efon` |

**Páginas de Halloy em `tradicoes.json` e `glossario.json`.** A trad02 citou as páginas do PDF. Conferi cada trecho e todas valem PDF − 1, inclusive as notas 148, 261, 266 e 267. Convertidas para a página impressa:
- `xango_pernambuco`: pp. 28, 30, 85, 97, 119–120; nota: p. 84, p. 85 (nota 148), pp. 85 e 119;
- `xango_sergipe`: p. 30;
- `batuque_rs`: p. 29;
- `umbanda`: p. 29;
- glossário: abatá, p. 119 (nota 261); nação, p. 27; Xambá, pp. 85, 119–120.

**`candomble_efon` → `com_fonte`**, com descrição mínima tirada de Castillo 2022:
- p. 28, nota 54: Efon é cidade do território ekiti, no leste da Iorubalândia, vizinha de Ijexá, e a nação efon é associada à ijexá. Havia em Salvador um antigo terreiro de nação efon, chefiado pela liberta Maria Bernarda da Paixão, onde Cristóvão Lopes dos Anjos foi iniciado por volta de 1913;
- p. 23: "efon" como nação africana, subgrupo iorubá, no século XIX.

A nota da tradição avisa que a descrição é mínima e que Lima 2014 (nação efon em Duque de Caxias, RJ) ainda não foi lido. "Nigéria" saiu da descrição, porque a fonte fala em Iorubalândia. Tradições: **16 `com_fonte`**, 3 `rascunho_sem_fonte` (benim, arara, orisha_trinidad).

## 3. Conferência do §4 da trad02 feita antes do cancelamento

As paráfrases do §4 batem com o original. Uma observação que a fich06 pode aproveitar:
- **Toutain:** a "fiesta de Elegguá" do central Méjico é uma festa comemorativa de 22 a 24 de outubro, na casa de Elegguá Alagbana. Ela celebra, entre outras coisas, a iniciação da fundadora (p. 57). Não foi fichada, porque a tarefa foi cancelada. Fica como sugestão de complemento ao registro de festa de Exu feito pela fich06.

## 4. Bloqueios

- **S. Ferretti 2011 (PUC Minas):** o download devolveu 415 neste ambiente. Não tentei contornar. Não chega a ser bloqueio de fato, porque a fich06 baixou o mesmo arquivo; fica só anotado.
- **Panteão da Casa das Minas:** lido de 2ª mão, via Prandi. Falta conferir em S. Ferretti, *Querebentã de Zomadônu* (1985/1996) e "Voduns da Casa das Minas" (1989), obras impressas → [PENDENCIAS](PENDENCIAS.md) §2.
- **Lima 2014, nação Efon (dissertação, PUC-SP):** não está no catálogo e não foi buscada. O repositório da PUC-SP tem desafio anti-robô → [PENDENCIAS](PENDENCIAS.md) §2.

## 5. Números depois da rodada

- **Registros:** 302 (286 `fichado`, 16 `pre_fichamento`). Por orixá: Exu 93, Ogum 64, Iemanjá 59, Xangô 52, Oxóssi 34.
- **Divergências:** 41 atributos (eram 37).
- **Fichas:** 284 versões.
- **Grafo:** 54 nós, 61 arestas; 24 entidades equivalentes.
- **Catálogo:** 316 fontes (227 `conferido_web`).
- **Site:** build OK; `qa_site.py` sem erros (284/284 versões).
