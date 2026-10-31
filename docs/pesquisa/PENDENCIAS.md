# Pendências de acesso e verificação

Lista viva de tudo o que **ficou bloqueado** durante a pesquisa: sites inacessíveis neste ambiente, obras pagas ou impressas, e conferências que dependem de uma pessoa. Cada vez que um bloqueio aparecer, ele entra aqui. Quando for resolvido, mude o status para ✅ e anote como se resolveu.

**Legenda de status:** 🔴 bloqueado · 🟡 parcial ou intermitente · ✅ resolvido
**Prioridade:** P1 destrava os 5 orixás do MVP · P2 melhora a cobertura · P3 complementar

---

## 1. Domínios bloqueados ou instáveis no ambiente

Para resolver: em **Network access**, nas configurações do ambiente, adicionar o domínio em *Allowed domains* ([instruções](https://code.claude.com/docs/en/cloud-environments#network-access)). Se o erro for 403 do próprio site (proteção anti-robô), liberar o domínio não basta: baixe o arquivo manualmente e anexe na conversa.

| Status | Domínio | Erro | O que está atrás | Prioridade |
|:-:|---|---|---|:-:|
| 🔴 | `www.redalyc.org` | 403 no proxy do ambiente | artigos de *Afro-Ásia* (Costa 2007; Amaral & Silva 2006; Brumana 2007), Romeu 2006, Rossbach de Olmos | P2 |
| 🔴 | `library.oapen.org` | 403 (anti-robô do site) | Peel 2016, *Christianity, Islam, and Oriṣa Religion* (acesso aberto) | P2 |
| 🔴 | `scielo.org.mx` / `www.scielo.org.mx` | conexão recusada | Mones Guevara 2024, *Cuicuilco* (Santería) | P2 |
| 🔴 | `core.ac.uk` | 403 | verbete acadêmico sobre Yemọja (core.ac.uk/download/213811235.pdf) | P2 |
| 🔴 | `muse.jhu.edu` | 403 (provável paywall) | Brown 1989, "Ogou in Haiti" (cap. de *Africa's Ogun*) | P1 |
| 🔴 | `www.religion.ucsb.edu` | 404 (arquivo removido) | Pérez 2013, "Nobody's Mammy" (Yemayá em Cuba). Buscar outra cópia | P2 |
| 🟡 | `bdtd.ibict.br` (páginas de registro) | 500 | tese UFG 2017 sobre Exu na Umbanda | P2 |
| 🟡 | `oasisbr.ibict.br` | 503 | dissertação Ribas 2010 (*Saravá Ogum*); teses PUC-SP sobre Exu | P2 |
| 🟡 | `revistas.usp.br` | falha de DNS intermitente | artigos da USP (funcionou na 2ª tentativa) | — |
| 🟡 | `api.openalex.org` | 429 (limite de requisições) | coleta automatizada de metadados; tentar mais tarde ou com chave/e-mail | P3 |

## 2. Obras impressas ou pagas (precisam de exemplar)

Para resolver: fotografar ou escanear as páginas indicadas e anexar na conversa. Faço a paráfrase com página, e no repositório entra só o resumo.

| Status | Obra | O que extrair | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Verger, *Orixás* (Corrupio, 1981) | origem africana, cidades de culto, cores, saudações e símbolos dos 5 orixás | **P1** |
| 🔴 | Verger, *Notas sobre o culto aos orixás e voduns* (Edusp, 1999/2000) | Iemanjá pp. 293–295; Exu pp. 119, 132–139; equivalências fon | **P1** |
| 🔴 | Verger, *Lendas africanas dos orixás* (Corrupio) | itãs dos 5 orixás | **P1** |
| 🔴 | Prandi, *Mitologia dos Orixás* (Cia. das Letras, 2001) | itãs e parentescos dos 5 orixás (só parafrasear) | **P1** |
| 🔴 | Cacciatore, *Dicionário de cultos afro-brasileiros* (1977) | saudações, nomes, termos | **P1** |
| 🔴 | Beniste, *Dicionário yorubá-português* (2011) e *Òrun-Àiyé* (1997) | grafias iorubás, etimologias e saudações (Laroiê, Ogunhê, Okê arô, Kaô Kabiecilê, Odoyá) | **P1** |
| 🔴 | Castro, *Falares africanos na Bahia* (2001) | nomes dos inquices equivalentes (Angola) | **P1** |
| 🔴 | Parés, *A formação do candomblé* (2006) | voduns equivalentes (Legba, Gu, Sogbo/Badé etc.) | **P1** |
| 🔴 | Lopes, *Bantos, malês e identidade negra* (1988) | inquices | P2 |
| 🔴 | Vallado, *Iemanjá* (Pallas, 2008) | confirmar título; origem e qualidades de Iemanjá | P2 |
| 🔴 | Silva & Silva Neto, *Oxóssi: o caçador divino* (Pallas, 2025) | Oxóssi: origem (Ketu, Ifé, Oyó), domínios, itãs | P2 |
| 🔴 | Tishken, Falola & Akinyemi (orgs.), *Ṣàngó in Africa and the African Diaspora* (2009) | Xangô em Oyó × leste iorubá; Ara × Xangô | P2 |
| 🔴 | Barnes (org.), *Africa's Ogun* (1989/1997) | Ogum na Nigéria e nas Américas | P2 |
| 🔴 | Otero & Falola (orgs.), *Yemoja* (2013); Falola (org.), *Èṣù* (2013) | perspectivas nigeriana e cubana | P2 |
| 🔴 | Carneiro, *Candomblés da Bahia* (1948/1954) | conferir p. 77 (carrego de Exu, Ogunjá) e Xangô "mais africano" | P2 |
| 🔴 | Santos, *Os Nàgô e a morte* (1976) | Exu, pp. 130–139 | P2 |
| 🔴 | Cabrera, *El Monte* (1954) e *Yemayá y Ochún* (1974); Bolívar, *Los orishas en Cuba* (1990) | equivalências lucumís | P2 |
| 🔴 | Beier, *Yoruba Poetry* (1970); Barber, *I Could Speak Until Tomorrow* (1991) | ìjálá e oríkì de Ogum e Xangô | P3 |

## 3. Conferências que dependem de pessoa ou instituição

| Status | Item | Como resolver | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Datas de tombamento do IPHAN (Alaketu: 2004, 2005 ou 2008; Gantois, Bate Folha, Casa das Minas: 2005 ou 2006) | consultar Livro do Tombo / banco de pareceres do IPHAN | P2 |
| 🔴 | 95 fontes com status `a_verificar` e 13 `pista` no catálogo | conferir no WorldCat, ISBN ou DOI, começando pelas usadas no fichamento | P2 |
| 🔴 | Lista completa da Coleção Orixás (Pallas) | site ou contato com a editora | P2 |
| 🔴 | Revisão das fichas por praticantes e pesquisadores | formar o conselho consultivo (Fase 4 do plano) | **P1** |
| 🔴 | Decidir o que é público em "tabus" e "alimentos" (hoje retidos das fichas: exu-012, oxossi-018) | conselho consultivo | P1 |
| 🔴 | Descrições das 19 tradições em `data/tradicoes.json` estão sem fonte (`rascunho_sem_fonte`) | fichar uma obra de referência geral por grupo (Candomblé por nação, Umbanda, religiões regionais, Cuba/Haiti/Trinidad) e revisar com o conselho | P2 |

## 4. Resolvidos

| Data | Item | Como |
|---|---|---|
| 2026-10-31 | Acesso a USP, UFRJ, HAL, Crossref, BDTD, theses.fr, Open Library | domínios liberados pelo autor nas configurações do ambiente |
| 2026-10-31 | Divergência aparente entre Bastide e Chiousse sobre a espada-de-ogum | Bastide, p. 165: registra o uso diurético; p. 192: o vínculo religioso vem da forma. Sem contradição |
