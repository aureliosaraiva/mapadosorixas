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
| 🟡 | `dialnet.unirioja.es` | erro de SSL na conexão | nada no momento: Ferretti 2011 (*Horizonte*) foi achado aberto no site da PUC Minas pela DOAJ (`ferretti-2011-comida`) | P3 |
| 🟡 | `seer.ufrgs.br` | curl tem a conexão cortada; o PDF veio pela ferramenta de busca web | Debates do NER (Oro 2008 já lido). Para outros artigos do NER, usar o mesmo caminho | P3 |
| 🔴 | `muse.jhu.edu` | 403 (provável paywall) | Brown 1989, "Ogou in Haiti" (cap. de *Africa's Ogun*) | P1 |
| 🔴 | `www.religion.ucsb.edu` | 404 (arquivo removido) | Pérez 2013, "Nobody's Mammy" (Yemayá em Cuba). Buscar outra cópia | P2 |
| 🔴 | `bdtd.ibict.br` (API VuFind e páginas) | API: `HTTP 400 Problem connecting to Solr` nas 61 consultas da varredura 3 (2026-10-31); páginas: 500. Problema do servidor da BDTD, não do ambiente | **teses e dissertações brasileiras recentes** sobre os 5 orixás e sobre Angola, Jeje, Batuque e Mina (lacuna da varredura 3). Repetir `python3 scripts/coleta/coletar.py --bases bdtd` mais tarde | P2 |
| 🟡 | `oasisbr.ibict.br` | 503 | dissertação Ribas 2010 (*Saravá Ogum*, sustenta ogum-005, ainda `pre_fichamento`); teses PUC-SP sobre Exu | P2 |
| 🟡 | `revistas.usp.br` | falha de DNS intermitente | artigos da USP (funcionou na 2ª tentativa) | — |
| 🔴 | `api.openalex.org` | 429 mesmo com `mailto`: o orçamento diário sem chave é compartilhado pelo IP do ambiente e estava esgotado (2026-10-31) | coleta OpenAlex da varredura 3. **Para resolver:** o autor cria uma chave gratuita (help.openalex.org/api/authentication) e a coloca como variável `OPENALEX_API_KEY` nas configurações do ambiente; depois rodar `coletar.py --bases openalex` | P3 |
| 🔴 | `api.datacite.org`, `www.base-search.net` | desafio anti-robô ("Making sure you're not a bot") | metadados DataCite (DOIs do HAL e de repositórios) e o agregador BASE | P3 |
| 🔴 | `search.scielo.org`, `api.core.ac.uk` | 403 / redirecionamento para login (o CORE exige chave) | busca SciELO direta (os artigos SciELO vieram pelo Crossref e pela DOAJ) e CORE | P3 |
| 🔴 | `revistas.uece.br` | 403 em todos os downloads (2026-11-01) | Santana 2023, primeira ialorixá do Terreiro da Nação Xambá (`santana-2023-xamba`): reforço de `xango_pernambuco` e do termo Xambá | P2 |
| 🔴 | `www.e-publicacoes.uerj.br` | conexão cortada nas 3 tentativas (2026-11-01); a cópia do Redalyc também dá 403 | Mendes 2014, Candomblé angola e caboclo (`mendes-2014-angola-caboclo`): reforço de `candomble_angola` | P2 |
| 🔴 | `www.scielo.br` | desafio anti-robô (Bunny Shield), também no PDF (2026-11-01) | S. Ferretti 1996, Acossi (`ferretti-1996-acossi`), para `tambor_de_mina`; Corrêa 1996, culinária do batuque (`correa-1996-cozinha`), para `batuque_rs`. Baixar manualmente | P2 |
| 🔴 | `www.mdpi.com` | 403 (Akamai) na página e no PDF (2026-11-01) | Niell 2023, santuário de Regla (`niell-2023-regla`): Yemayá de Regla e reforço de `lucumi`. Acesso aberto (CC BY); baixar manualmente | P2 |
| 🟡 | `fundaj.emnuvens.com.br`, `econtents.bc.unicamp.br` | 502 no túnel (2026-11-01) | nada bloqueado: Pitta veio por `periodicos.fundaj.gov.br` e M. Ferretti por `periodicos.sbu.unicamp.br` | — |
| 🟡 | `hal.science` (páginas) | desafio anti-robô na página do registro | nada bloqueado: o arquivo do PDF (`/file/...` ou `/document`, achado pela API do HAL) baixa direto | — |
| 🟡 | `api.crossref.org` | 429 intermitente depois de ~300 requisições seguidas; o backoff do coletor resolve | nada bloqueado | — |

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
| 🟡 | Dantas, *Vovó nagô e papai branco* (1988) | descrição do **Xangô de Sergipe** além do mínimo: casas, nações, ritos. `xango_sergipe` tem hoje só uma descrição curta, de segunda mão (Halloy p. 31, que cita Bastide; M. Ferretti p. 76, que cita Dantas) | P2 |
| 🔴 | Barnet, *Cultos afrocubanos* (1995); Cabrera, *El Monte* (1954) | descrição da **Regla Arará** (ainda sem fonte: Toutain 2019 só cita arará como nação colonial); reforço de **Palo Monte** (que já tem fonte em Toutain 2019 e Argyriadis 2005); conferir em Cabrera a comparação Cuba × Bahia que Bastide (p. 78) faz | P2 |
| 🔴 | Parés, *A formação do candomblé* (2006), pp. 23–38 e 125–168 | conferir no original o que Cerqueira 2015 resume sobre os jejes em Salvador e as casas Bogum e Seja Hundê (`candomble_jeje`) | P2 |
| 🔴 | Obra de referência sobre o **Orisha/Shango de Trinidad** (nenhuma aberta no catálogo; Bastide p. 95 só cita o culto dos *Shouters*) | descrição de `orisha_trinidad` (sem fonte) | P3 |
| 🔴 | Obra que descreva a **nação Efon** | descrição de `candomble_efon` (sem fonte); nenhuma fonte lida menciona Efon | P2 |
| 🔴 | Verger 1957/1999 (*Notas sobre o culto*) ou Peel 2016 | sustentar que o culto iorubá varia de cidade para cidade, sem panteão único (frase retirada de `ioruba_nigeria`) | P2 |
| 🔴 | Cacciatore (1977), Beniste (2011), Prandi, *Mitologia* (2001) | 2ª fonte para **itã** (hoje só Chiousse) e verbete **saudação** no glossário | P2 |

## 3. Conferências que dependem de pessoa ou instituição

| Status | Item | Como resolver | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Datas de tombamento do IPHAN (Alaketu: 2004, 2005 ou 2008; Gantois, Bate Folha, Casa das Minas: 2005 ou 2006) | consultar Livro do Tombo / banco de pareceres do IPHAN | P2 |
| 🟡 | 68 fontes `a_verificar` e 27 `pista` no catálogo, nenhuma usada no fichamento. A varredura 3 promoveu 11 a `conferido_web` e acrescentou 17 pistas (8 dissertações ou teses sem ano no registro, possível resenha em *Afro-Ásia* 2007, Segato com ano a conferir etc.) | conferir no WorldCat, ISBN ou DOI quando entrarem no fichamento | P3 |
| 🔴 | Varredura 3: tradição e confiabilidade das 129 fontes novas foram atribuídas por título e resumo, **sem leitura**. Nação não explícita está anotada em `observacoes` ("nação a confirmar") | confirmar na leitura, ao fichar | P3 |
| 🔴 | Orisha de Trinidad: as fontes centrais achadas na varredura 3 (Simpson 1962/1965, Henry 1983, Trotman 1976/2007, Aiyejina & Gibbons 1999, Houk 2024, Castor 2017, Stewart 2022) são pagas ou impressas | exemplar ou PDF de biblioteca, para dar fonte a `orisha_trinidad` | P3 |
| 🔴 | Vallado, *Iemanjá: a grande mãe africana do Brasil*: Open Library registra a ed. de 2002 (ISBN 85-347-0246-2); Queiroga & Nascimento citam 2008 | conferir no exemplar ou na Pallas se 2008 é reedição; ajustar `ano`/id se for a mesma edição | P3 |
| 🔴 | Capítulos de Augras (1989) e Ferreira (2000): obras coletivas conferidas, mas título e páginas dos capítulos não | sumário das obras (exemplar ou catálogo de biblioteca) | P3 |
| 🔴 | Lista completa da Coleção Orixás (Pallas) | site ou contato com a editora | P2 |
| 🔴 | exu-062: Nogueira (2017, p. 22) fala em "candomblés" sem nação; o registro usa `candomble_ketu` como aproximação | revisor confirma ou ajusta a tradição | P3 |
| 🟡 | Revisão das fichas por praticantes e pesquisadores | preparação feita em [`docs/conselho/`](../conselho/); falta o contato (§3c) | **P1** |
| 🔴 | Decidir o que é público em "tabus" e "alimentos" (hoje retidos das fichas: exu-012, oxossi-018) | conselho consultivo | P1 |
| 🟡 | Tradições: 15 de 19 já têm fonte; faltam benim, candomble_efon, arara, orisha_trinidad (obras no §2). `benim` é rótulo editorial do catálogo: decidir se funde com `vodun_benim`/`ioruba_nigeria` | autor decide sobre `benim`; revisão das 15 descrições pelo conselho | P2 |
| 🔴 | Catálogo (sessão do catálogo): `pitta-2011-mitos` saiu em 1985 (*Cad. Est. Soc.*, v. 1, n. 2, pp. 263–268); `ferretti-m-2020-pureza` é o artigo de 2001 (*Ciências Sociais e Religião*, ano 3, n. 3, pp. 75–94); evidências novas para Halloy, Toutain e Cerqueira | anotar em `observacoes`/`evidencias` sem trocar o ano citado (detalhes em [tradicoes-02](tradicoes-02.md) §5) | P3 |
| 🔴 | Afirmações sobre os 5 orixás achadas na leitura das fontes de tradições (Halloy, Pitta, Toutain, Oro 2012, S. Ferretti 2011, Cerqueira): **não entraram no fichamento** | orquestradora encaminha a uma sessão de fichamento ([tradicoes-02](tradicoes-02.md) §4) | P1 |
| 🔴 | Glossário: decidir se entram **quizila/ewó**, **bori** e **kelê** (as fontes abertas os definem, mas tocam tabu ou iniciação) e revisar as 54 definições | conselho consultivo | P2 |
| 🔴 | Prandi 2005, *Nas pegadas dos voduns*: a versão do autor tem paginação própria; falta a correspondência com o livro *Somavó* (pp. 63–94) | conferir no exemplar | P3 |

## 3b. Site (Fase 5): decisões do autor

O protótipo em `site/` (Astro) compila no CI, mas **não está publicado**. Nada abaixo foi configurado, porque depende de conta, pagamento ou decisão do autor.

| Status | Item | O que decidir ou fazer | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Deploy | escolher Cloudflare Pages, GitHub Pages ou Vercel e conectar a conta. Para GitHub Pages, buildar com `SITE_BASE=/mapadosorixas` (ver `site/README.md`) | P2 |
| 🔴 | Domínio | registrar `.org`/`.com` (`.com.br` exige CPF/CNPJ). **Consulta RDAP em 2026-10-31: sem registro (provavelmente livres) — `mapadosorixas.org`, `mapadosorixas.com`, `atlasdosorixas.org`, `atlasdosorixas.com`, `enciclopediaorixas.org`, `enciclopediaorixas.com`, `orixas.wiki`, `orixas.info`, `panteaoorixa.com`. Já registrados: `orixas.com`, `orixa.org`.** Confirmar no registrador antes de comprar e apontar para o deploy | P2 |
| 🔴 | Licenças de código, textos e dados | sugestão do plano: MIT, CC BY-SA 4.0, CC BY 4.0 (ou NC), a confirmar com o conselho. O rodapé do site diz "a definir" | P2 |
| 🔴 | Indexação | o site sai com `<meta name="robots" content="noindex">` enquanto for rascunho. Retirar só depois da revisão das fichas | P1 (no lançamento) |
| 🟡 | Revisão de acessibilidade com leitor de tela real e Lighthouse | automatizado feito: axe-core (WCAG 2.1 A/AA + boas práticas) em todas as 14 páginas, 1280 e 390 px, sem violações (`site/scripts/acessibilidade.cjs`; em 2026-10-31 corrigido o campo de busca sem rótulo visível). Falta auditoria humana (NVDA/VoiceOver), em especial do mini-grafo e do grafo (canvas: o leitor de tela recebe só o `aria-label` e a lista/tabela equivalente), e Lighthouse ≥ 90 | P2 |
| 🔴 | Dados publicados em "Baixar dados" (`/dados/`) | a página publica cópias de `data/orixas/*.json`, `conexoes.json`, `entidades_equivalentes.json`, `divergencias.json`, `glossario.json` e do catálogo de fontes, com aviso "licença a definir pelo autor". Decidir: (a) a licença dos dados; (b) se o catálogo deve sair inteiro, incluindo fontes `pista` (nível D) e observações internas; (c) se as fichas JSON devem continuar listando os **ids** de registros retidos e em pré-fichamento em `pendencias` (só ids, sem conteúdo, como na seção Pendências das fichas HTML). O fichamento bruto **não** é publicado (tem registros retidos e em pré-fichamento) e `tradicoes.json` sai sem as descrições ainda sem fonte | P2 |
| 🔴 | Página Sobre/Créditos (`/sobre/`) | redigida em 2026-10-31 a partir do `CLAUDE.md`, com canal de contribuição pelas **issues do repositório** (nenhum contato pessoal). Conferir: (a) a forma final dos créditos de autoria (nome do autor? coletivo?); (b) a frase que declara o preparo com assistência de IA (Claude) sob curadoria do autor — manter, reescrever ou retirar; (c) se as issues continuam sendo o canal ou se haverá e-mail/formulário do projeto; (d) o crédito ao Mapa de la Conciencia como inspiração de formato | P2 |
| 🟡 | Glossário nas fichas | a primeira ocorrência de cada termo em cada ficha vira link para o glossário, com dica acessível (`aria-describedby` + tooltip que fecha com Esc). Ficaram fora variantes que são palavras comuns ("lado", "despacho", "invocação", "avatar"), formas ambíguas ("ita") e a entidade "exu (Umbanda)", para não ligar o orixá Exu à entidade. Revisores devem conferir se algum outro termo é ligado num sentido errado | P3 |
| 🟡 | Axe e Lighthouse no CI | o CI roda `scripts/qa_site.py` após o build, mas não o axe: exigiria instalar Playwright/Chromium no runner. Decidir se vale o tempo extra de CI | P3 |

## 3c. Conselho consultivo (Fase 4): depende do autor

Material pronto em [`docs/conselho/`](../conselho/). **Nenhuma pessoa ou instituição foi contatada.**

| Status | Item | O que fazer | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Convidar pesquisadores | escolher 1–3 em [`candidatos.md`](../conselho/candidatos.md) §1 (sugestão: Parés para Jeje/voduns, Castro ou Nei Lopes para Angola, Oro para Batuque, Pérez ou Otero para Lucumí); conferir a página institucional antes de escrever; usar o convite de [`kit-revisao.md`](../conselho/kit-revisao.md) §4 | **P1** |
| 🔴 | Convidar praticantes (≥2 nações) | contatar **instituições** de [`candidatos.md`](../conselho/candidatos.md) §2 (terreiros tombados, federações, CEAO/UFBA, NER/UFRGS) e pedir indicação; olorisha lucumí com o convite em espanhol (§5 do kit) | **P1** |
| 🔴 | Confirmar vida e atividade dos marcados ❓ | Monique Augras, Norton F. Corrêa, Indira Mones Guevara, Juana Elbein dos Santos; falecimento de Rita Amaral é só inferido | P2 |
| 🔴 | Conflito de interesse | Prandi e V. G. da Silva são as fontes mais citadas; decidir se revisam fichas que se baseiam na própria obra | P2 |
| 🔴 | Termo de consentimento | revisão jurídica rápida (RGPD art. 9 / LGPD art. 11: religião é dado sensível); traduzir guia e termo para o espanhol | P2 |
| 🔴 | Decisões da proposta de registro | aprovar `revisoes` por registro; critério para tirar o selo "Rascunho" (ficha inteira × atributo); aceitar ou não `comunicacao_pessoal` como fonte ([`proposta-registro-revisao.md`](../conselho/proposta-registro-revisao.md) §4) | P1 |
| 🔴 | Tombamentos não confirmados | Sítio de Pai Adão (Recife) e Tumba Junsara (Salvador): conferir no portal do IPHAN (junto com as datas do §3) | P3 |
| 🔴 | Lacunas de diversidade | sem caminho institucional verificado para Umbanda (federação nacional), sacerdotisas lucumís e casas lucumís na Espanha; pedir indicação aos primeiros conselheiros | P2 |

## 4. Resolvidos

| Data | Item | Como |
|---|---|---|
| 2026-11-01 | `palo_monte` e `xango_sergipe` ganharam fonte; 7 tradições reforçadas; +7 termos no glossário (Regla de Ocha, Palo Monte, nfumbi, mpungu, cabildo, Xambá, abatá) | Halloy 2005, Pitta (1985), M. Ferretti (2001), S. Ferretti 2011, Oro 2012, Toutain 2019, Argyriadis 2005, Cerqueira 2015 ([tradicoes-02](tradicoes-02.md)) |
| 2026-10-31 | Ferretti 2011, "Comida ritual em festas de Tambor de Mina" (antes atrás do Dialnet) | texto aberto no site da PUC Minas, achado pela DOAJ na varredura 3 |
| 2026-10-31 | Coleta automatizada de metadados (antes impossível por bloqueio de API) | Crossref, Open Library, theses.fr, HAL e DOAJ respondem; `scripts/coleta/` ([relatório 3](relatorio-varredura-03.md)) |
| 2026-10-31 | Descrições de 13 tradições com fonte e página; glossário com 47 termos | Bastide 1961, Chiousse 1995, Prandi 2001 e 2005, Silva 2012, Oro 2008, Botão 2007, Tomba 2019 ([fichamento-05](fichamento-05.md)) |
| 2026-10-31 | Leitura de Nogueira 2017 (UFG), Pinheiro 2011 (UFPB) e Costa 2007 (*Afro-Ásia*): exu-034, ogum-006 e xango-005 passaram a `fichado` | PDFs nos repositórios UFG e UFPB e no portal de periódicos da UFBA ([fichamento-04](fichamento-04.md)) |
| 2026-10-31 | Metadados de Ortiz 1978 e Landes 1947, usados como fonte primária de registros de 2ª mão | Open Library → `conferido_web` |
| 2026-10-31 | Metadados das 17 fontes `a_verificar`/`pista` usadas no fichamento | Open Library, Internet Archive, Crossref, repositórios UFG/UFPB; autores das teses identificados (Nogueira 2017, Pinheiro 2011) e título de Costa 2007 (DOI 10.9771/aa.v0i36.21145) |
| 2026-10-31 | Acesso a USP, UFRJ, HAL, Crossref, BDTD, theses.fr, Open Library | domínios liberados pelo autor nas configurações do ambiente |
| 2026-10-31 | Divergência aparente entre Bastide e Chiousse sobre a espada-de-ogum | Bastide, p. 165: registra o uso diurético; p. 192: o vínculo religioso vem da forma. Sem contradição |
