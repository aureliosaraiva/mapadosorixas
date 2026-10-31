# Pendências de acesso e verificação

Lista viva de tudo o que **ficou bloqueado** durante a pesquisa: sites inacessíveis neste ambiente, obras pagas ou impressas, e conferências que dependem de uma pessoa. Cada vez que um bloqueio aparecer, ele entra aqui. Quando for resolvido, mude o status para ✅ e anote como se resolveu.

**Legenda de status:** 🔴 bloqueado · 🟡 parcial ou intermitente · ✅ resolvido
**Prioridade:** P1 destrava os 5 orixás do MVP · P2 melhora a cobertura · P3 complementar

---

## 1. Domínios bloqueados ou instáveis no ambiente

Para resolver: em **Network access**, nas configurações do ambiente, adicionar o domínio em *Allowed domains* ([instruções](https://code.claude.com/docs/en/cloud-environments#network-access)). Se o erro for 403 do próprio site (proteção anti-robô), liberar o domínio não basta: baixe o arquivo manualmente e anexe na conversa.

| Status | Domínio | Erro | O que está atrás | Prioridade |
|:-:|---|---|---|:-:|
| 🔴 | `www.redalyc.org` | 403 no proxy do ambiente | artigos de *Afro-Ásia* (Amaral & Silva 2006; Brumana 2007), Romeu 2006, Rossbach de Olmos. Para *Afro-Ásia*, usar o portal `periodicos.ufba.br`, que funciona (Costa 2007 foi lido por lá) | P2 |
| 🔴 | `library.oapen.org` | 403 (anti-robô do site) | Peel 2016, *Christianity, Islam, and Oriṣa Religion* (acesso aberto) | P2 |
| 🔴 | `scielo.org.mx` / `www.scielo.org.mx` | conexão cortada (curl) e 503 (busca web), confirmado de novo em 2026-10-31 | Mones Guevara 2024, *Cuicuilco* (Santería): fonte para a tradição `lucumi` e para termos da Ocha (aché, moyugba) | P2 |
| 🔴 | `core.ac.uk` | 403 | verbete acadêmico sobre Yemọja (core.ac.uk/download/213811235.pdf); artigo em português sobre os sistemas afro-cubanos segundo Fernando Ortiz: Ocha, Arará, Abakuá, Palo Monte (core.ac.uk/download/51396375.pdf), que daria fonte a `palo_monte` e `arara` | P2 |
| 🔴 | `bibliotecadigital.udea.edu.co` | 403 + verificação anti-robô | Arango 2018, dissertação sobre Ocha na Colômbia (`arango-2018-ache`). Baixar manualmente e anexar | P2 |
| 🔴 | `dialnet.unirioja.es` | erro de SSL na conexão | Ferretti 2011, "Comida ritual em festas de Tambor de Mina", *Horizonte* v. 9, n. 21 (DOI 10.5752/P.2175-5841.2011v9n21p242). Tentar o site da PUC Minas | P3 |
| 🟡 | `seer.ufrgs.br` | curl tem a conexão cortada; o PDF veio pela ferramenta de busca web | Debates do NER (Oro 2008 já lido). Para outros artigos do NER, usar o mesmo caminho | P3 |
| 🔴 | `muse.jhu.edu` | 403 (provável paywall) | Brown 1989, "Ogou in Haiti" (cap. de *Africa's Ogun*) | P1 |
| 🔴 | `www.religion.ucsb.edu` | 404 (arquivo removido) | Pérez 2013, "Nobody's Mammy" (Yemayá em Cuba). Buscar outra cópia | P2 |
| 🟡 | `bdtd.ibict.br` (páginas de registro) | 500 | nada no momento: a tese UFG 2017 foi lida direto no repositório da UFG | P3 |
| 🟡 | `oasisbr.ibict.br` | 503 | dissertação Ribas 2010 (*Saravá Ogum*, sustenta ogum-005, ainda `pre_fichamento`); teses PUC-SP sobre Exu | P2 |
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
| 🔴 | Beier, *Yoruba Poetry* (1970); Barber, *I Could Speak Until Tomorrow* (1991) | ìjálá e oríkì de Ogum e Xangô; definição ampliada de oríkì no glossário | P3 |
| 🔴 | Dantas, *Vovó nagô e papai branco* (1988) | descrição do **Xangô de Sergipe** (`xango_sergipe` está sem fonte) | P2 |
| 🔴 | Barnet, *Cultos afrocubanos* (1995); Cabrera, *El Monte* (1954) | descrições de **Palo Monte** e **Regla Arará** (sem fonte); conferir em Cabrera a comparação Cuba × Bahia que Bastide (p. 78) faz | P2 |
| 🔴 | Obra de referência sobre o **Orisha/Shango de Trinidad** (nenhuma aberta no catálogo; Bastide p. 95 só cita o culto dos *Shouters*) | descrição de `orisha_trinidad` (sem fonte) | P3 |
| 🔴 | Obra que descreva a **nação Efon** | descrição de `candomble_efon` (sem fonte); nenhuma fonte lida menciona Efon | P2 |
| 🔴 | Verger 1957/1999 (*Notas sobre o culto*) ou Peel 2016 | sustentar que o culto iorubá varia de cidade para cidade, sem panteão único (frase retirada de `ioruba_nigeria`) | P2 |
| 🔴 | Cacciatore (1977), Beniste (2011), Prandi, *Mitologia* (2001) | 2ª fonte para **itã** (hoje só Chiousse) e verbete **saudação** no glossário | P2 |

## 3. Conferências que dependem de pessoa ou instituição

| Status | Item | Como resolver | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Datas de tombamento do IPHAN (Alaketu: 2004, 2005 ou 2008; Gantois, Bate Folha, Casa das Minas: 2005 ou 2006) | consultar Livro do Tombo / banco de pareceres do IPHAN | P2 |
| 🟡 | 79 fontes `a_verificar` e 10 `pista` no catálogo, nenhuma usada no fichamento (as 19 usadas foram conferidas em 2026-10-31) | conferir no WorldCat, ISBN ou DOI quando entrarem no fichamento | P3 |
| 🔴 | Vallado, *Iemanjá: a grande mãe africana do Brasil*: Open Library registra a ed. de 2002 (ISBN 85-347-0246-2); Queiroga & Nascimento citam 2008 | conferir no exemplar ou na Pallas se 2008 é reedição; ajustar `ano`/id se for a mesma edição | P3 |
| 🔴 | Capítulos de Augras (1989) e Ferreira (2000): obras coletivas conferidas, mas título e páginas dos capítulos não | sumário das obras (exemplar ou catálogo de biblioteca) | P3 |
| 🔴 | Lista completa da Coleção Orixás (Pallas) | site ou contato com a editora | P2 |
| 🔴 | exu-062: Nogueira (2017, p. 22) fala em "candomblés" sem nação; o registro usa `candomble_ketu` como aproximação | revisor confirma ou ajusta a tradição | P3 |
| 🔴 | Revisão das fichas por praticantes e pesquisadores | formar o conselho consultivo (Fase 4 do plano) | **P1** |
| 🔴 | Decidir o que é público em "tabus" e "alimentos" (hoje retidos das fichas: exu-012, oxossi-018) | conselho consultivo | P1 |
| 🟡 | Tradições: 13 de 19 já têm fonte; faltam benim, candomble_efon, xango_sergipe, palo_monte, arara, orisha_trinidad (obras no §2). `benim` é rótulo editorial do catálogo: decidir se funde com `vodun_benim`/`ioruba_nigeria` | autor decide sobre `benim`; revisão das 13 descrições pelo conselho | P2 |
| 🔴 | Glossário: decidir se entram **quizila/ewó**, **bori** e **kelê** (as fontes abertas os definem, mas tocam tabu ou iniciação) e revisar as 47 definições | conselho consultivo | P2 |
| 🔴 | Prandi 2005, *Nas pegadas dos voduns*: a versão do autor tem paginação própria; falta a correspondência com o livro *Somavó* (pp. 63–94) | conferir no exemplar | P3 |

## 3b. Site (Fase 5): decisões do autor

O protótipo em `site/` (Astro) compila no CI, mas **não está publicado**. Nada abaixo foi configurado, porque depende de conta, pagamento ou decisão do autor.

| Status | Item | O que decidir ou fazer | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Deploy | escolher Cloudflare Pages, GitHub Pages ou Vercel e conectar a conta. Para GitHub Pages, buildar com `SITE_BASE=/mapadosorixas` (ver `site/README.md`) | P2 |
| 🔴 | Domínio | registrar `.org`/`.com` (ver candidatos no `CLAUDE.md`; `.com.br` exige CPF/CNPJ) e apontar para o deploy | P2 |
| 🔴 | Licenças de código, textos e dados | sugestão do plano: MIT, CC BY-SA 4.0, CC BY 4.0 (ou NC), a confirmar com o conselho. O rodapé do site diz "a definir" | P2 |
| 🔴 | Indexação | o site sai com `<meta name="robots" content="noindex">` enquanto for rascunho. Retirar só depois da revisão das fichas | P1 (no lançamento) |
| 🔴 | Revisão de acessibilidade com leitor de tela real e Lighthouse | conferido só com Playwright (sem estouro horizontal em 360 px, sem erros de console, conteúdo textual sem JS). Falta auditoria humana (NVDA/VoiceOver) e Lighthouse ≥ 90 | P2 |

## 4. Resolvidos

| Data | Item | Como |
|---|---|---|
| 2026-10-31 | Descrições de 13 tradições com fonte e página; glossário com 47 termos | Bastide 1961, Chiousse 1995, Prandi 2001 e 2005, Silva 2012, Oro 2008, Botão 2007, Tomba 2019 ([fichamento-05](fichamento-05.md)) |
| 2026-10-31 | Leitura de Nogueira 2017 (UFG), Pinheiro 2011 (UFPB) e Costa 2007 (*Afro-Ásia*): exu-034, ogum-006 e xango-005 passaram a `fichado` | PDFs nos repositórios UFG e UFPB e no portal de periódicos da UFBA ([fichamento-04](fichamento-04.md)) |
| 2026-10-31 | Metadados de Ortiz 1978 e Landes 1947, usados como fonte primária de registros de 2ª mão | Open Library → `conferido_web` |
| 2026-10-31 | Metadados das 17 fontes `a_verificar`/`pista` usadas no fichamento | Open Library, Internet Archive, Crossref, repositórios UFG/UFPB; autores das teses identificados (Nogueira 2017, Pinheiro 2011) e título de Costa 2007 (DOI 10.9771/aa.v0i36.21145) |
| 2026-10-31 | Acesso a USP, UFRJ, HAL, Crossref, BDTD, theses.fr, Open Library | domínios liberados pelo autor nas configurações do ambiente |
| 2026-10-31 | Divergência aparente entre Bastide e Chiousse sobre a espada-de-ogum | Bastide, p. 165: registra o uso diurético; p. 192: o vínculo religioso vem da forma. Sem contradição |
