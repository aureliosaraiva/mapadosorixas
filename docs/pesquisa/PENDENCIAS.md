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
| 🔴 | `www.persee.fr` (PDF `docAsPDF`) | página do artigo abre; o PDF tem desafio anti-robô (altcha) — lote C, 2026-11-01 | Verger 1965, "Grandeur et décadence du culte de ìyámi òsòròngà" (`verger-1965-iyami`, acesso livre no Persée). Baixar à mão em `/tmp/refs-pdf/verger-1965-iyami.pdf`; leitura de Iyami só depois da decisão do conselho (§3a) | P2 |
| 🔴 | `journal.sadra.ac.id` | HTTP 500 em `view` e `download` (lote C, 2026-11-01) | Igboin 2014 e Layi 2016 (debate "Is Olodumare, God in Yoruba belief, God?"), previstos no lote C e não lidos | P2 |
| 🔴 | `unesdoc.unesco.org` | 403 Cloudflare "Just a moment" (lote C, 2026-11-01) | verificar se há PDF oficial de Abimbola, *Sixteen Great Poems of Ifá* (UNESCO, 1975) | P2 |
| 🔴 | `library.oapen.org` | 403 (anti-robô do site) | Peel 2016, *Christianity, Islam, and Oriṣa Religion* (acesso aberto) | P2 |
| 🔴 | `scielo.org.mx` / `www.scielo.org.mx` | conexão cortada (curl) e 503 (busca web), confirmado de novo em 2026-10-31 | Mones Guevara 2024, *Cuicuilco* (Santería): fonte para a tradição `lucumi` e para termos da Ocha (aché, moyugba) | P2 |
| 🔴 | `core.ac.uk` | 403 | verbete acadêmico sobre Yemọja (core.ac.uk/download/213811235.pdf); artigo em português sobre os sistemas afro-cubanos segundo Fernando Ortiz: Ocha, Arará, Abakuá, Palo Monte (core.ac.uk/download/51396375.pdf), que daria fonte a `palo_monte` e `arara` | P2 |
| 🔴 | `bibliotecadigital.udea.edu.co` | 403 + verificação anti-robô | Arango 2018, dissertação sobre Ocha na Colômbia (`arango-2018-ache`). Baixar manualmente e anexar | P2 |
| 🟡 | `dialnet.unirioja.es` | erro de SSL na conexão | nada no momento: Ferretti 2011 (*Horizonte*) foi achado aberto no site da PUC Minas pela DOAJ (`ferretti-2011-comida`) | P3 |
| 🟡 | `seer.ufrgs.br` | curl tem a conexão cortada (de novo na auditoria anti-cópia, 6 tentativas em 2026-11-01); o PDF veio pela ferramenta de busca web, que não devolve o texto literal | Debates do NER (Oro 2008 já lido). **Oro 2008 ficou fora da auditoria anti-cópia** ([anticopia-01](anticopia-01.md) §2): o autor baixa o PDF e anexa, para comparar os trechos de `batuque_rs`, `candomble_ijexa`, `umbanda` e dos termos `linha-cruzada`, `nacao` e `umbanda` | P2 |
| 🔴 | `muse.jhu.edu` | 403 (provável paywall) | Brown 1989, "Ogou in Haiti" (cap. de *Africa's Ogun*) | P1 |
| 🔴 | `www.religion.ucsb.edu` | 404 (arquivo removido) | Pérez 2013, "Nobody's Mammy" (Yemayá em Cuba). Buscar outra cópia | P2 |
| 🔴 | `www.scielo.br` | desafio anti-robô (Bunny Shield) em todas as páginas e PDFs, também pela ferramenta de busca web (2026-11-01) | **P1 do fichamento-06:** Prandi 1995, *Deuses africanos no Brasil contemporâneo*; Giumbelli & Lima 2024 (monumentos a Iemanjá); Noleto & Negrão 2025 (Iemanjá em Montevidéu; o PDF tem cópia no Internet Archive de 2026-07-30). Baixar manualmente e anexar. Nascimento 2001 foi lido pela cópia do repositório da UFES | **P1** |
| 🔴 | `periodicos.unb.br` | 403 (2026-11-01); a cópia em `core.ac.uk/download/231243654.pdf` pede desafio anti-robô | Ferreira (Saraiva) 2017, *De vodum a caboclo* (Legba no Tambor de Mina e no Terecô), P1 do fichamento-06. Baixar manualmente e anexar | **P1** |
| 🔴 | `lume.ufrgs.br` | conexão cortada (curl, 4 tentativas, 2026-11-01) | número 3 (1995) de *Horizontes Antropológicos* em PDF, alternativa para Prandi 1995 | P1 |
| 🔴 | `repositorio.pucsp.br` | desafio anti-robô (SafeLine, HTTP 468) em 2026-11-01 | dissertação de Ribas 2010, *Saravá Ogum* (sustenta ogum-005, `pre_fichamento`): PDF em `repositorio.pucsp.br/xmlui/bitstream/handle/1785/1/Jose%20Dalmo%20Ribeiro%20Ribas.pdf`. Baixar manualmente e anexar | P2 |
| 🔴 | `bdtd.ibict.br` (API VuFind e páginas) | API: `HTTP 400 Problem connecting to Solr` nas 61 consultas da varredura 3 (2026-10-31); páginas: 500. Problema do servidor da BDTD, não do ambiente | **teses e dissertações brasileiras recentes** sobre os 5 orixás e sobre Angola, Jeje, Batuque e Mina (lacuna da varredura 3). Repetir `python3 scripts/coleta/coletar.py --bases bdtd` mais tarde | P2 |
| 🟡 | `oasisbr.ibict.br` | 503 | teses PUC-SP sobre Exu. (O registro da dissertação de Ribas 2010 aponta para o repositório da PUC-SP, ver linha `repositorio.pucsp.br`.) | P2 |
| 🟡 | `revistas.usp.br` | falha de DNS intermitente | artigos da USP (funcionou na 2ª tentativa) | — |
| 🔴 | `api.openalex.org` | 429 mesmo com `mailto`: o orçamento diário sem chave é compartilhado pelo IP do ambiente e estava esgotado (2026-10-31) | coleta OpenAlex da varredura 3. **Para resolver:** o autor cria uma chave gratuita (help.openalex.org/api/authentication) e a coloca como variável `OPENALEX_API_KEY` nas configurações do ambiente; depois rodar `coletar.py --bases openalex` | P3 |
| 🔴 | `api.datacite.org`, `www.base-search.net` | desafio anti-robô ("Making sure you're not a bot") | metadados DataCite (DOIs do HAL e de repositórios) e o agregador BASE | P3 |
| 🔴 | `search.scielo.org`, `api.core.ac.uk` | 403 / redirecionamento para login (o CORE exige chave) | busca SciELO direta (os artigos SciELO vieram pelo Crossref e pela DOAJ) e CORE | P3 |
| 🔴 | `revistas.uece.br` | 403 em todos os downloads (2026-11-01) | Santana 2023, primeira ialorixá do Terreiro da Nação Xambá (`santana-2023-xamba`): reforço de `xango_pernambuco` e do termo Xambá | P2 |
| 🔴 | `www.e-publicacoes.uerj.br` | conexão cortada nas 3 tentativas (2026-11-01); a cópia do Redalyc também dá 403 | Mendes 2014, Candomblé angola e caboclo (`mendes-2014-angola-caboclo`): reforço de `candomble_angola` | P2 |
| 🔴 | `www.scielo.br` | desafio anti-robô (Bunny Shield), também no PDF (2026-11-01) | S. Ferretti 1996, Acossi (`ferretti-1996-acossi`), para `tambor_de_mina`; Corrêa 1996, culinária do batuque (`correa-1996-cozinha`), para `batuque_rs`. Baixar manualmente | P2 |
| 🔴 | `www.mdpi.com` | 403 (Akamai) na página e no PDF (2026-11-01) | Niell 2023, santuário de Regla (`niell-2023-regla`): Yemayá de Regla e reforço de `lucumi`. Acesso aberto (CC BY); baixar manualmente | P2 |
| 🟡 | `fundaj.emnuvens.com.br`, `econtents.bc.unicamp.br` | 502 no túnel (2026-11-01) | nada bloqueado: Pitta veio por `periodicos.fundaj.gov.br` e M. Ferretti por `periodicos.sbu.unicamp.br` | — |
| 🔴 | `hal.science`, `theses.hal.science`, `halshs.archives-ouvertes.fr` | desafio anti-robô (Anubis, "Making sure you're not a bot") na página do registro **e agora também em `/document` e `/file/...`** (sessão anticopia2, 2026-11-01; na anticopia-01 o arquivo ainda baixava) | texto integral de Chiousse 1995, Halloy 2005, Toutain 2019, Cerqueira 2015 e Vallier 2011 para o anti-cópia ([anticopia-02](anticopia-02.md) §2). Todas em francês, onde a comparação por n-gramas não pega tradução; mesmo assim, o autor pode baixar os PDFs e guardar uma cópia local para `scripts/baixar_refs.py --so-converter` | **P2** (fichamento-08: o bloqueio agora impede também fichar o restante de Halloy 2005 — qualidades, festas, símbolos e parentescos fora das pp. 163–169 — e a "fiesta de Elegguá" de Toutain 2019, p. 57, 22–24 de outubro; o PDF também não abre no Wayback a partir deste ambiente. O autor salva os dois PDFs em `/tmp/refs-pdf/halloy-2005-intimite.pdf` e `/tmp/refs-pdf/toutain-2019-santos.pdf` e uma sessão retoma as tarefas 1 e 4 do [fichamento-08](fichamento-08.md). **Lote A (2026-11-01):** o bloqueio impediu fichar Chiousse 1995, pp. 225–291, para Oxalá, Oxum, Iansã, Nanã e Omolu (e Ibeji, Ifá, Oxumarê do lote B), também pelo link direto `/file/tel-00003395.pdf`; salvar em `/tmp/refs-pdf/chiousse-1995-divins.pdf` ([lote-A](lote-A.md) §2, §9)) |
| 🟡 | `journals.openedition.org` | página do artigo sem link de PDF (texto só em HTML); `baixar_refs.py` não acha o arquivo | Argyriadis 2005 (`argyriadis-2005-ramas`), em francês, fora da 2ª passagem do anti-cópia. Salvar o texto da página como `/tmp/refs/argyriadis-2005-ramas.txt` quando for preciso | P3 (fichamento-08: o texto HTML foi lido inteiro; o artigo não trata de Exu, Ogum, Oxóssi, Xangô nem Iemanjá — Regla aparece só como bairro de Havana, ¶38 — e não rendeu registro) |
| 🟡 | `fundaj.emnuvens.com.br` (de novo 502, 2026-11-01) | o catálogo só traz essa URL para Pitta; a cópia lida na trad02 veio de `periodicos.fundaj.gov.br`, que não está em `evidencias` | Pitta (`pitta-2011-mitos`) fora da 2ª passagem do anti-cópia (só trechos classe C na anticopia-01). Acrescentar a URL de `periodicos.fundaj.gov.br` às `evidencias` na próxima sessão do catálogo | P3 |
| 🟡 | `api.crossref.org` | 429 intermitente depois de ~300 requisições seguidas; o backoff do coletor resolve | nada bloqueado | — |
| 🔴 | `babel.hathitrust.org` e `www.hathitrust.org` | desafio anti-robô (Cloudflare) no leitor (varredura 4, 2026-11-01); a **API de catálogo** (`catalog.hathitrust.org/api/volumes/brief/…`) funciona e serve como prova de domínio público | leitura de Nina Rodrigues 1900 (`coo.31924020011759`, pd). Baixar o PDF manualmente se a edição francesa for preferida à de 1935 (aberta no IA) | P3 |
| 🔴 | `en.wikisource.org` / `pt.wikisource.org` (API) | 429, limite de requisições do IP compartilhado (2026-11-01) | busca de textos em domínio público no Wikisource | P3 |
| 🔴 | `www.dominiopublico.gov.br` | 403 (Cloudflare) | portal Domínio Público do MEC (obras brasileiras em domínio público) | P3 |
| 🟡 | `archive.org/download/…_djvu.txt` | HTTP 500 intermitente (2026-11-01): `osafricanosnobrasil` falhou 3 vezes; Bowen 1857 baixou na 2ª | texto de *Os africanos no Brasil* (Nina Rodrigues 1932) para o anti-cópia e a leitura. Tentar de novo ou baixar o PDF do item | P2 |
| 🔴 | `books.scielo.org` | 403 (2026-11-01) | Caprara 1998, "Médico ferido: Omolu…" (`caprara-1998-omolu`) e Silva 2022, Mina Nagô (`silva-2022-mina-nago`), ambos em acesso aberto: **lotes A e B** da expansão | P2 |
| 🔴 | `periodicos.urca.br`, `www.periodicos.unimontes.br` | 403 (2026-11-01) | Santos 2019, Casa de Oxumarê (`santos-h-2019-osumare`); Carrillo 2026, Ochún (`carrillo-2026-ochun`) | P2 |
| 🔴 | `periodicos2.uesb.br`, `periodicos.ufpa.br` | 503 / página de bloqueio do servidor (2026-11-01) | Noguera 2018, Orunmilá (`noguera-2018-orunmila`); Monteiro & Azevedo 2021, Iyá Mi Oxorongá (`monteiro-2021-iya-mi`) | P3 |
| 🟡 | `digibug.ugr.es` | erro de protocolo HTTP/2 no curl (2026-11-01) | Fernández Cano 2005, Oyá e Santa Teresa (`fernandez-cano-2005-oya`) | P3 |
| 🔴 | `www.mdpi.com` (de novo) | 403 | Akande 2019, Egúngún (`akande-2019-egungun`); Ofuasia 2023, Ifá (`ofuasia-2023-ifa-hell`): acesso aberto, **lote C/D** | P2 |
| 🟡 | `hal.science` (de novo) | Anubis na página do registro; **em 2026-11-01 (lote B) o `curl` direto no arquivo baixou os PDFs de Chiousse 1995 (`halshs.archives-ouvertes.fr/tel-00003395v1/file/tel-00003395.pdf`) e de Halloy 2005 (`hal.science/tel-04260456/file/…`)**; `baixar_refs.py` (requests) continua recebendo a página do desafio. Os PDFs ficam em `/tmp/refs-pdf/` só durante a sessão: a próxima sessão repete o `curl` e usa `--so-converter` | **Chiousse 1995, pp. 225–291: os perfis dos orixás além dos 5 sustentam o lote A da expansão** ([varredura 4](relatorio-varredura-04.md) §5); dossiê Ọ̀ṣun-Òṣogbo (Joffroy 2004). O autor salva o PDF em `/tmp/refs-pdf/chiousse-1995-divins.pdf` | **P1 (expansão)** |

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
| 🟡 | Dantas, *Vovó nagô e papai branco* (1988) | descrição do **Xangô de Sergipe** além do mínimo: casas, nações, ritos. `xango_sergipe` tem hoje só uma descrição curta, de segunda mão (Halloy p. 30, que cita Bastide; M. Ferretti p. 76, que cita Dantas) | P2 |
| 🔴 | Barnet, *Cultos afrocubanos* (1995); Cabrera, *El Monte* (1954) | descrição da **Regla Arará** (ainda sem fonte: Toutain 2019 só cita arará como nação colonial); reforço de **Palo Monte** (que já tem fonte em Toutain 2019 e Argyriadis 2005); conferir em Cabrera a comparação Cuba × Bahia que Bastide (p. 78) faz | P2 |
| 🔴 | Parés, *A formação do candomblé* (2006), pp. 23–38 e 125–168 | conferir no original o que Cerqueira 2015 resume sobre os jejes em Salvador e as casas Bogum e Seja Hundê (`candomble_jeje`) | P2 |
| 🔴 | S. Ferretti, *Querebentã de Zomadônu* (1985/1996) e "Voduns da Casa das Minas" (em Moura (org.), *Meu sinal está no teu corpo*, 1989) | conferir no original o panteão da Casa das Minas lido de 2ª mão em Prandi 2005 (exu-091, exu-092, xango-049, iemanja-056: Legba, Badé e Abé) | P2 (fichamento-08: busca de texto aberto sem resultado; só exemplar comercial) |
| 🔴 | Obra de referência sobre o **Orisha/Shango de Trinidad** (nenhuma aberta no catálogo; Bastide p. 95 só cita o culto dos *Shouters*) | descrição de `orisha_trinidad` (sem fonte) | P3 |
| 🟡 | Obra que descreva a **nação Efon** além do mínimo: Lima, Alexandre Mantovani de, *Memórias e identidades de um terreiro de Candomblé: a Nação Efon em Duque de Caxias* (dissertação, PUC-SP, 2014; Castillo cita a p. 148). Não está no catálogo; o repositório da PUC-SP tem desafio anti-robô | `candomble_efon` ganhou descrição mínima no fichamento-07 (Castillo 2022, p. 28, nota 54); faltam ritos, panteão e casas atuais | P2 |
| 🔴 | Verger 1957/1999 (*Notas sobre o culto*) ou Peel 2016 | sustentar que o culto iorubá varia de cidade para cidade, sem panteão único (frase retirada de `ioruba_nigeria`) | P2 |
| 🔴 | Cacciatore (1977), Beniste (2011), Prandi, *Mitologia* (2001) | 2ª fonte para **itã** (hoje só Chiousse) e verbete **saudação** no glossário | P2 |
| 🔴 | Prandi, *Mitologia dos Orixás* (2001) e Verger, *Lendas africanas dos orixás* (1985) | **itãs de todos os orixás da expansão** (lote D da [varredura 4](relatorio-varredura-04.md) §6); sem eles o lote D não começa | **P1 (expansão)** |
| 🔴 | Verger, *Orixás* (1981) | origem africana, cidades de culto e saudações de Oxalá, Oxum, Iansã, Nanã, Omolu, Oxumarê, Ossaim, Logunedé, Obá, **Ewá** (sem nenhuma outra fonte) e Iroko | **P1 (expansão)** |
| 🔴 | Abimbola, *Sixteen Great Poems of Ifá* (1975), *Ifá: An Exposition* (1976), *Ifá Divination Poetry* (1977); Bascom 1969 e 1980 | corpus de Ifá e odù (lote D). As cópias online achadas (IA, item de usuário; thinkyorubafirst.org) **não têm licença clara: não usar** | P2 |
| 🔴 | Santos, *Os Nàgô e a morte* (1976); Idowu, *Olódùmarè* (1962); Beniste, *Òrun-Àiyé* (1997); Augras (1989) | cosmologia e hierarquia: Egungun, Olodumare, Orum/Aiê, Iyami (lote C) | P2 |
| 🔴 | Murphy & Sanford (orgs.), *Ọ̀ṣun across the Waters* (2001); Gleason, *Oya* (1987); Theodoro, *Iansã* (2010) | Oxum e Iansã na África e nas Américas (lote A) | P2 |
| 🔴 | Barros, *A floresta sagrada de Ossaim* (2011); Verger, *Awọn ewé Ọ̀sanyìn* (1967) e *Ewé* (1995); Lopes, *Logunedé* (2006); Houlberg 1973 e Ọlayẹmi 1971 (Ìbejì) | lote B | P2 |
| 🔴 | Literatura de praticantes da Pallas (Coleção Orixás) sobre **Ewá, Oxumarê, Nanã, Obá e Iroko** | lacunas sem fonte acadêmica aberta (varredura 4 §7) | P2 |

## 3. Conferências que dependem de pessoa ou instituição

| Status | Item | Como resolver | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Datas de tombamento do IPHAN (Alaketu: 2004, 2005 ou 2008; Gantois, Bate Folha, Casa das Minas: 2005 ou 2006) | consultar Livro do Tombo / banco de pareceres do IPHAN | P2 |
| 🟡 | 59 fontes `a_verificar` e 46 `pista` no catálogo (varredura 4: +19 pistas, 2 promovidas), nenhuma usada no fichamento (o fichamento-06 promoveu 6 a `conferido_web` pela Open Library). A varredura 3 promoveu 11 a `conferido_web` e acrescentou 17 pistas (8 dissertações ou teses sem ano no registro, possível resenha em *Afro-Ásia* 2007, Segato com ano a conferir etc.) | conferir no WorldCat, ISBN ou DOI quando entrarem no fichamento | P3 |
| 🔴 | Varredura 4: direitos de obras antigas para **reprodução** (paráfrase e citação não dependem disso): Farrow 1926 (data de morte do autor desconhecida); Ortiz 1906 (domínio público em Cuba e nos EUA; na Espanha só em 2050); notas de A. Ramos na ed. 1935 de Nina Rodrigues (na Espanha, 2030); Epega e Lijadu (iorubá, datas e edições a conferir) | consultar catálogo de autoridades (VIAF) ou especialista; não publicar trechos dessas obras no site | P3 |
| 🔴 | Varredura 4: **Olokun do Benim (Edo)** ficou fora do recorte (Rosen 1989, Ben-Amos 1973, Imasogie 1980, Izevbigie 1978) | autor ou conselho decide se o grafo inclui o culto edo | P3 |
| 🔴 | Varredura 4: tradição e confiabilidade das 75 fontes novas e 13 obras em domínio público foram atribuídas por título, resumo e sumário, **sem leitura**; a cobertura por orixá das obras antigas veio de sumário e contagem de nomes no OCR | confirmar na leitura, ao fichar (lotes A–D) | P3 |
| 🔴 | Varredura 3: tradição e confiabilidade das 129 fontes novas foram atribuídas por título e resumo, **sem leitura**. Nação não explícita está anotada em `observacoes` ("nação a confirmar") | confirmar na leitura, ao fichar | P3 |
| 🔴 | Orisha de Trinidad: as fontes centrais achadas na varredura 3 (Simpson 1962/1965, Henry 1983, Trotman 1976/2007, Aiyejina & Gibbons 1999, Houk 2024, Castor 2017, Stewart 2022) são pagas ou impressas | exemplar ou PDF de biblioteca, para dar fonte a `orisha_trinidad` | P3 |
| 🔴 | Vallado, *Iemanjá: a grande mãe africana do Brasil*: Open Library registra a ed. de 2002 (ISBN 85-347-0246-2); Queiroga & Nascimento citam 2008 | conferir no exemplar ou na Pallas se 2008 é reedição; ajustar `ano`/id se for a mesma edição | P3 |
| 🔴 | Capítulos de Augras (1989) e Ferreira (2000): obras coletivas conferidas, mas título e páginas dos capítulos não | sumário das obras (exemplar ou catálogo de biblioteca) | P3 |
| 🔴 | Lista completa da Coleção Orixás (Pallas) | site ou contato com a editora | P2 |
| 🔴 | exu-062: Nogueira (2017, p. 22) fala em "candomblés" sem nação; o registro usa `candomble_ketu` como aproximação | revisor confirma ou ajusta a tradição | P3 |
| 🟡 | Revisão das fichas por praticantes e pesquisadores | preparação feita em [`docs/conselho/`](../conselho/); falta o contato (§3c) | **P1** |
| 🔴 | Decidir o que é público em "tabus" e "alimentos" (hoje retidos das fichas: exu-012, oxossi-018) | conselho consultivo | P1 |
| 🟡 | Tradições: 16 de 19 já têm fonte (candomble_efon ganhou descrição mínima no fichamento-07); faltam benim, arara, orisha_trinidad (obras no §2). `benim` é rótulo editorial do catálogo: decidir se funde com `vodun_benim`/`ioruba_nigeria` | autor decide sobre `benim`; revisão das 16 descrições pelo conselho | P2 |
| ✅ | Catálogo (sessão do catálogo): `pitta-2011-mitos` saiu em 1985 (*Cad. Est. Soc.*, v. 1, n. 2, pp. 263–268); `ferretti-m-2020-pureza` é o artigo de 2001 (*Ciências Sociais e Religião*, ano 3, n. 3, pp. 75–94); evidências novas para Halloy, Toutain e Cerqueira | anotar em `observacoes`/`evidencias` sem trocar o ano citado (detalhes em [tradicoes-02](tradicoes-02.md) §5) | P3 (**resolvido** no fichamento-06/07: ver [fichamento-07](fichamento-07.md)) |
| ✅ | Afirmações sobre os 5 orixás achadas na leitura das fontes de tradições (Halloy, Pitta, Toutain, Oro 2012, S. Ferretti 2011, Cerqueira): **não entraram no fichamento** | orquestradora encaminha a uma sessão de fichamento ([tradicoes-02](tradicoes-02.md) §4) | P1 (**resolvido** no fichamento-06/07: ver [fichamento-07](fichamento-07.md)) |
| 🔴 | Glossário: decidir se entram **quizila/ewó**, **bori** e **kelê** (as fontes abertas os definem, mas tocam tabu ou iniciação) e revisar as 54 definições | conselho consultivo | P2 |
| 🔴 | Prandi 2005, *Nas pegadas dos voduns*: a versão do autor tem paginação própria; falta a correspondência com o livro *Somavó* (pp. 63–94) | conferir no exemplar | P3 |
| 🔴 | Fichamento-06 (adendo): o mito de Xangô expulso do balé por revelar segredos dos eguns (Halloy 2005, p. 168, via Segato 1995) e a nota de Oro 2012 (p. 557) sobre animais sacrificados no Batuque não foram fichados | conselho decide se entram (segredo de culto; animais) | P3 |
| 🔴 | Costa 1980 (*Afro-Ásia* n. 13): o PDF não traz números de página impressos, e nem a OJS nem o Crossref informam o intervalo. Os registros exu-065 a exu-072 citam "PDF p. N" | conferir no exemplar ou no sumário impresso do n. 13 e converter para a página impressa | P3 |
| 🔴 | Prandi 1995 (`prandi-1995-deuses`): o DOI do catálogo (`10.1590/s0104-71831995000300002`) não resolve no Crossref, e o pid `S0104-71831995000300010` citado na varredura 3 é de outro artigo (Augé, *L'Anthropologie aujourd'hui*) | conferir DOI e pid corretos no sumário de *Horizontes Antropológicos* n. 3 (1995) quando o SciELO ou o LUME responderem | P2 |
| 🔴 | Fichamento-06, fontes de 2ª mão citadas pelas lidas e **não conferidas no original**: Bastide 1945 (via Costa), Bastide 1960 (via Costa), Herskovits 1938 e Bascom 1969 (via Vallier), Johnson 1921, Idowu 1962 e Akinyemi em Tishken 2009 (via Capo Chichi), Verger 1981, Parés 2006 e Barnes 1989/1997 (via Castillo); Kochmeyer (via Costa) e Hethersett 1941 (via Capo Chichi) nem estão no catálogo | conferir as páginas citadas quando houver exemplar (§2) | P3 |
| ✅ | Castillo 2022 (p. 28, nota 54) cita uma casa de **nação Efon** em Salvador (Maria Bernarda da Paixão) e remete a Lima 2014, p. 148, para a nação Efon no Brasil: pista para dar fonte a `candomble_efon` | sessão autorizada a editar `data/tradicoes.json` lê Lima 2014 (ou usa Castillo como fonte parcial) | P2 (**resolvido** no fichamento-06/07: ver [fichamento-07](fichamento-07.md)) |
| ✅ | **Auditoria anti-cópia 01** ([anticopia-01](anticopia-01.md)): 10 campos com 8+ palavras idênticas à fonte (classe A) e 31 com redação próxima demais (classe B) | **resolvido** na sessão anticopia2 ([anticopia-02](anticopia-02.md)): 40 campos do fichamento, 1 nota de tradição e 1 definição do glossário reescritos; exu-022.nota tratado no script como referência bibliográfica; `ANTICOPIA_REFS` com 25 obras dá 0 erros | — |
| 🔴 | Catálogo: a evidência de Parés 2006 (`pares-2006-formacao`) em `periodicos.usp.br/revhistoria/...64670` é uma **resenha** (Bonciani), não o livro; `baixar_refs.py` baixa a resenha, que foi descartada da pasta de referências | sessão do catálogo marca a URL como resenha em `observacoes` (ou a tira de `evidencias`); o livro continua em §2 (exemplar) | P3 |
| 🔴 | Anti-cópia **não detecta tradução**: as fontes em francês (Chiousse, Halloy, Toutain, Argyriadis, Cerqueira, Vallier) e em inglês (Capo Chichi) ficaram sem checagem efetiva de cópia traduzida | pessoa bilíngue confere uma amostra de paráfrases contra o original | P2 |
| 🔴 | Lote A ([lote-A](lote-A.md) §6): **iemanja-013** e **ogum-014** dizem "Centro Africano S. Jorge (Bahia)", mas Bastide (p. 105, nota 54) cita P. Cavalcanti, "As seitas africanas no Recife": o centro é do Recife | sessão que edita `iemanja.json` e `ogum.json` troca a casa para Recife e a tradição para `xango_pernambuco` (os registros novos do lote A já usam Recife) | P2 |
| 🔴 | Lote A: afirmações de 2ª mão lidas em Bastide 1961 cujas fontes **não estão no catálogo** nem foram conferidas: Le Hérissé 1911 (Sakpata "rei da terra", omolu-006), P. Cavalcanti 1937 (calendários do Recife), L. Cabrera, *El Monte* (itã das folhas de Ossaim, iansa-021), Gonçalves Fernandes, *Xangôs do Nordeste*, O. Alvarenga, *Xangô* (itã de Ogum e Oxum, oxum-029), Manuel Querino (Anamburocú/Sant'Ana, nana-003) | sessão do catálogo inclui as obras; conferência no original quando houver exemplar | P3 |
| 🔴 | Lote A: Bastide 1961 se contradiz sobre Oxalufã e Oxaguiã (p. 110: Oxalufã velho, Oxaguiã jovem; p. 204: o inverso) e sobre a Oxum mais velha (p. 142: Yabá Omi; p. 205: Lobá). Registrados como estão (oxala-021/022, oxum-022) | conferir em outra edição (3ª ed., 1978) ou com revisor | P3 |
| 🔴 | OCR ruim nos PDFs de Bastide 1961 (UFRJ) e Costa 1980: a auditoria anti-cópia nessas obras é um piso | se houver PDF com texto melhor (ou exemplar), repetir a comparação | P3 |

## 3a. Expansão do panteão (Fase 7, sessão modelo2): decisões e conferências

A sessão modelo2 preparou o modelo de dados ([`modelo-dados-2.md`](../modelo-dados-2.md)) sem escrever conteúdo. Ficaram para o autor, o conselho ou as sessões de fichamento:

| Status | Item | O que decidir ou fazer | Prioridade |
|:-:|---|---|:-:|
| 🔴 | Escolha final da primeira leva (~15 orixás, `prioridade_mvp2: 1`) e da ordem de trabalho | autor confirma a lista (hoje: os 12 do PLANO, Fase 7, além dos 5 do MVP) e, depois, o conselho | P1 |
| 🔴 | **Iyami** (`sensivel`): o que é publicável | conselho decide; até lá só se ficha o que estiver em fonte acadêmica pública, sem fundamento, e o site mostra só o nome com aviso | P1 |
| 🔴 | Rótulos provisórios de `grupo` (funfun: Oxalá, Oxalufã, Oxaguiã, Odudua; iabá: Iemanjá, Oxum, Iansã, Nanã, Obá, Ewá, Iyewa) | confirmar com fonte, por tradição, pondo os registros em `grupo.confirmado_por`; até lá ficam fora do site e do download. Nenhum rótulo "aborô" foi atribuído | P2 |
| 🔴 | Agrupamentos provisórios num só identificador: Omolu/Obaluaê, Iroko/Tempo, Orunmilá/Ifá, Olodumare/Olorum/Olofin; e separação de Ewá e Iyewa | as sessões de fichamento registram, com fonte, se as tradições tratam esses nomes como a mesma divindade, aspectos ou qualidades; o autor decide se divide ou funde ids (trocar id depois exige migrar registros e links) | P2 |
| 🔴 | **Lote C — decisões para o conselho** ([relatório](lote-C.md) §7) | (a) Iyami: confirmar os 4 registros mínimos (iyami-001–004) ou retirá-los; Verger 1965 só depois; (b) Egungun: Bastide (pp. 172–180) e Fámúlẹ̀ descrevem cargos, objetos e etapas rituais — não fichados; decidir o que é público; (c) Olokun do Benim (Edo), citado por Dennett: entra no recorte? | P1 |
| 🔴 | Orí sem entidade na lista-mestra | o lote C achou 6 fontes (Ellis, Johnson, Farrow, Zacharias, Bastide, Dennett via Bastide; relatório §6); a sessão de modelo decide criar `ori` (tipo conceito cosmológico) | P2 |
| 🔴 | Orixás funfun: nenhuma fonte do lote C usa o termo | `grupo` funfun continua sem `confirmado_por`; depende de Verger 1981, Santos 1976 ou Beniste 1997 (§2) | P2 |
| 🔴 | Itãs e arestas do lote C (criação em Ifẹ̀, dilúvio de Olokun, casal na cabaça, filhos de Yemaja; parentescos de odudua-007, olokun-002, olokun-004) | integrar em `itans.json` e `conexoes_alvos.json` pela sessão dona desses arquivos ([relatório](lote-C.md) §5 e §8) | P2 |
| 🔴 | `tipo` das entidades cosmológicas (Iyami e Egungun como "ancestrais", orixás funfun como "conceito cosmológico") | classificação de trabalho, exibida como tal; revisor confirma ou propõe outra | P3 |
| 🔴 | Itãs espelhados: agrupamentos editoriais (exu-009 + exu-082; oxossi-023 + oxossi-026) e títulos escritos pelo projeto | revisor confere se as versões são do mesmo itã e se os títulos são adequados | P3 |
| 🟡 | iemanja-052 nomeia Obatalá: não foi ligado ao id `oxala` sem fonte que o diga | **lote A:** Bastide identifica Obatalá com Oxalá **na Bahia** (oxala-001, p. 98); o mito de ita-003 é iorubá (Ellis via Pitta), por isso o itã continua sem `oxala`. Revisor decide se a identificação baiana basta | P3 |
| 🔴 | Nenhum itã ligado a aresta do grafo (os 12 registros de itã não estão em `conexoes_alvos.json`) | ao fichar parentesco afirmado num itã, mapear o registro para que a aresta apareça na página do itã | P3 |
| 🔴 | Lote A: itã de Ifá e Oxum (ita-013) liga **Elegba → `exu`** (Bastide, p. 141, diz que é outro nome de Exu) e **Ifá → `orunmila`** (rótulo "Orunmilá / Ifá") | revisor confirma as identificações | P3 |
| 🔴 | Lote A: o site não tem estilo para arestas `rivalidade` (o build quebra); omolu-019 ("rival de Xangô") ficou só com o casamento com Obá no mapa | sessão do site inclui `rivalidade` em `site/src/lib/grafo.js` (`CORES_ARESTA`, rótulos) e então o mapa ganha a aresta | P3 |
| 🔴 | Lote A: alimentos e animais de Bastide (pp. 22, 198) e de S. Ferretti 2011 (pp. 256–264) para os cinco orixás **não foram fichados** (só as festas, com a nota "alimentos retidos") | conselho decide o que é público (§3c); depois uma sessão ficha | P3 |
| 🔴 | Fontes para a expansão: Prandi, *Mitologia dos Orixás* (2001), e Verger, *Lendas africanas dos orixás*, são a base dos itãs e só existem impressas | exemplar (ver §2) | P1 |

## 3b. Site (Fase 5): decisões do autor

O protótipo em `site/` (Astro) compila no CI. **Sessão pages (2026-11-01): publicado como rascunho público** em <https://aureliosaraiva.github.io/mapadosorixas/> (GitHub Pages, workflow `deploy-pages.yml`; ver [`docs/publicacao.md`](../publicacao.md)).

| Status | Item | O que decidir ou fazer | Prioridade |
|:-:|---|---|:-:|
| ✅ | Deploy (GitHub Pages) | **resolvido em 2026-11-01:** o autor tornou o repositório público e gravou Settings → Pages → Source: GitHub Actions; a execução nº 4 do `deploy-pages.yml` publicou o site, conferido com Playwright (screenshots em `docs/screenshots/pages/`). Observação: a integração desta sessão não pode disparar `workflow_dispatch` (403); deploys vêm de push na `main` ou do botão Run workflow | — |
| 🔴 | Domínio | registrar `.org`/`.com` (`.com.br` exige CPF/CNPJ). **Consulta RDAP em 2026-10-31: sem registro (provavelmente livres) — `mapadosorixas.org`, `mapadosorixas.com`, `atlasdosorixas.org`, `atlasdosorixas.com`, `enciclopediaorixas.org`, `enciclopediaorixas.com`, `orixas.wiki`, `orixas.info`, `panteaoorixa.com`. Já registrados: `orixas.com`, `orixa.org`.** Confirmar no registrador antes de comprar e apontar para o deploy | P2 |
| 🔴 | Licenças de código, textos e dados | sugestão do plano: MIT, CC BY-SA 4.0, CC BY 4.0 (ou NC), a confirmar com o conselho. O rodapé do site, a página Baixar dados e o `LEIAME.txt` de `/dados/` dizem "a definir pelo autor". **Com o rascunho público no Pages (sessão pages), a decisão ganha prioridade:** sem licença, ninguém tem permissão formal de reutilizar os dados baixáveis | **P1** |
| 🔴 | Indexação | o site sai com `<meta name="robots" content="noindex">` enquanto for rascunho. Retirar só depois da revisão das fichas | P1 (no lançamento) |
| 🟡 | Revisão de acessibilidade com leitor de tela real e Lighthouse | automatizado feito: axe-core (WCAG 2.1 A/AA + boas práticas) em todas as 14 páginas, 1280 e 390 px, sem violações (sessão modelo2: 26 páginas, incluindo Itãs e Cosmologia, sem violação grave) (`site/scripts/acessibilidade.cjs`; em 2026-10-31 corrigido o campo de busca sem rótulo visível). Falta auditoria humana (NVDA/VoiceOver), em especial do mini-grafo e do grafo (canvas: o leitor de tela recebe só o `aria-label` e a lista/tabela equivalente), e Lighthouse ≥ 90 | P2 |
| 🔴 | Dados publicados em "Baixar dados" (`/dados/`) | a página publica cópias de `data/orixas/*.json`, `conexoes.json`, `entidades_equivalentes.json`, `divergencias.json`, `glossario.json`, do catálogo de fontes e (sessão modelo2) `entidades.json` sem grupos não confirmados e `itans.json` só com versões lidas, com aviso "licença a definir pelo autor". Decidir: (a) a licença dos dados; (b) se o catálogo deve sair inteiro, incluindo fontes `pista` (nível D) e observações internas; (c) se as fichas JSON devem continuar listando os **ids** de registros retidos e em pré-fichamento em `pendencias` (só ids, sem conteúdo, como na seção Pendências das fichas HTML). O fichamento bruto **não** é publicado (tem registros retidos e em pré-fichamento) e `tradicoes.json` sai sem as descrições ainda sem fonte | P2 |
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
| 🟡 | Decisões da proposta de registro | `revisoes` por registro **implementado** em 2026-11-01 ([`como-registrar-revisao.md`](../conselho/como-registrar-revisao.md)); falta o autor: (a) confirmar o critério do selo "Rascunho" (implementado: sai só quando **todas** as versões da ficha têm revisão vigente; alternativa: por atributo); (b) aceitar ou não `comunicacao_pessoal` como fonte ([`proposta-registro-revisao.md`](../conselho/proposta-registro-revisao.md) §4); (c) confirmar que `nao_publicar` vale mesmo com o registro alterado depois (implementado assim, por ser a opção conservadora) | P1 |
| 🔴 | Primeiro revisor | cadastrar em `data/revisores.json` só depois do termo assinado; contatos e termo ficam fora do repo; seguir [`como-registrar-revisao.md`](../conselho/como-registrar-revisao.md) | P1 |
| 🔴 | Página Créditos | gerar de `data/revisores.json` (sem anônimos nem quem revogou) quando houver o primeiro revisor (proposta, passo 6) | P3 |
| 🔴 | Tombamentos não confirmados | Sítio de Pai Adão (Recife) e Tumba Junsara (Salvador): conferir no portal do IPHAN (junto com as datas do §3) | P3 |
| 🔴 | Lacunas de diversidade | sem caminho institucional verificado para Umbanda (federação nacional), sacerdotisas lucumís e casas lucumís na Espanha; pedir indicação aos primeiros conselheiros | P2 |

## 3d. Lote B (Ossaim, Obá, Ibeji, Iroko, Logunedé, Oxumarê, Ewá): o que falta

Sessão lote B, 2026-11-01 ([relatório](lote-B.md)). 176 registros com as fontes abertas; o que segue depende de exemplar, de decisão ou de outra sessão.

| Status | Item | O que falta | Prioridade |
|:-:|---|---|:-:|
| 🔴 | **Ewá**: só 8 registros, todos de casas específicas (Recife, Mina em São Paulo, Maranhão, angola-congo); nenhum sobre domínios, cores, dia, símbolos, itãs ou origem | Verger, *Orixás* (1981); Prandi, *Mitologia* (2001); obras da Coleção Orixás (Pallas). Nenhuma fonte acadêmica dedicada achada nas varreduras 3 e 4 | **P1 (expansão)** |
| 🔴 | **Oxumarê**: 33 registros, mas nenhum itã de Prandi/Verger, nem saudação; a qualidade/cobra Dã (Bessém) do jeje baiano não tem fonte aberta | Verger 1981; Prandi 2001; Santos 2019 (Casa de Oxumarê, OJS com 403); Parés, *A formação do candomblé* (2006), para Bessém/Dã | P1 |
| 🔴 | **Ossaim**: falta a monografia de Barros (2011, *A floresta sagrada de Ossaim*) e Verger 1967/1995 (*Ewé*); mitos de Ossaim em Prandi 2001 (pp. 152–161) e Verger 2000 (pp. 228–230) só conhecidos por citação de Sallum & Silva | exemplar | P2 |
| 🔴 | **Logunedé**: Lopes (*Logunedé: santo menino que velho respeita*) só via Santos 2023, que cita a ed. de 2019 (o catálogo tem a de 2006) | exemplar; a sessão do catálogo anota a reedição em `observacoes` de `lopes-2006-logunede` | P2 |
| 🔴 | **Ibeji**: Houlberg (1973), Mobolade (1971), Chappel (1974) e Renne (2001), citados por Ogunbunmi; Thompson (1971, "Sons of thunder") | exemplar ou JSTOR; Thompson 1983 (`thompson-1983-flash`) segue `a_verificar` e por isso entrou só como citação de Sallum & Silva (ossaim-030) | P2 |
| 🔴 | **Iroko/Tempo**: nenhum registro de Tempo como nome (o agrupamento Iroko/Tempo da lista-mestra só é sustentado por Botão, p. 42, para o inquice Kitembo); nada sobre cores, dia, festas | exemplar (Verger 1981; Barros); autor decide se mantém o agrupamento | P2 |
| 🔴 | **Obá**: Sandoval 2007 (cap. "Oshún, Oyá e Obba") e Verger 1981 | exemplar | P3 |
| 🔴 | "Yewá" em Santos 2023 (amiga de Logunedé, logunede-009) e "Euá ou Yewá" como nome de Iemanjá em Queiroga & Nascimento 2019 (p. 8, nota 5): não se sabe se é Ewá ou Iyewa | autor decide; ver [lote-B](lote-B.md) §5 | P2 |
| 🔴 | Arestas e itãs do lote B não integrados: os registros de parentesco, equivalência e sincretismo geram aviso `sem_mapa`, e os itãs não estão em `data/itans.json` (fora do escopo desta sessão) | sessão de integração usa [lote-B](lote-B.md) §6–§7 para `conexoes_alvos.json` e `itans.json` | P1 |
| 🔴 | Registros retidos (tabus e alimentos) do lote B: 9 (ibeji-004, -020, -029, -038; logunede-021, -025; oxumare-033; oba-018; ewa-008) | conselho decide o que é público | P3 |
| 🔴 | Bastide pp. 157–161 descreve a colheita ritual das ervas pelo babalosaim (cantos, horas, pagamento a Ossaim, número de folhas na iniciação): **não fichado**, por tocar em fundamento | conselho decide se algo entra | P3 |

## 4. Resolvidos

| Data | Item | Como |
|---|---|---|
| 2026-11-01 | Cópia achada na auditoria anti-cópia 01 (10 erros, 31 campos classe B) | reescritas conferidas no original e aplicadas; `scripts/anticopia.py` com hifenização, filtro de referência bibliográfica e aviso de 6–7 palavras iguais à fonte citada; `scripts/baixar_refs.py` monta `/tmp/refs` ([anticopia-02](anticopia-02.md)) |
| 2026-11-01 | Registro da revisão (proposta, passos 1–3) | campo `revisoes` no fichamento, `data/revisores.json` (vazio) e `schemas/revisor.schema.json`, regras em `scripts/revisao.py` usadas pelo validador, pelo gerador e pelo QA do site; testes em `tests/` ([`como-registrar-revisao.md`](../conselho/como-registrar-revisao.md)) |
| 2026-11-01 | `palo_monte` e `xango_sergipe` ganharam fonte; 7 tradições reforçadas; +7 termos no glossário (Regla de Ocha, Palo Monte, nfumbi, mpungu, cabildo, Xambá, abatá) | Halloy 2005, Pitta (1985), M. Ferretti (2001), S. Ferretti 2011, Oro 2012, Toutain 2019, Argyriadis 2005, Cerqueira 2015 ([tradicoes-02](tradicoes-02.md)) |
| 2026-10-31 | Ferretti 2011, "Comida ritual em festas de Tambor de Mina" (antes atrás do Dialnet) | texto aberto no site da PUC Minas, achado pela DOAJ na varredura 3 |
| 2026-10-31 | Coleta automatizada de metadados (antes impossível por bloqueio de API) | Crossref, Open Library, theses.fr, HAL e DOAJ respondem; `scripts/coleta/` ([relatório 3](relatorio-varredura-03.md)) |
| 2026-10-31 | Descrições de 13 tradições com fonte e página; glossário com 47 termos | Bastide 1961, Chiousse 1995, Prandi 2001 e 2005, Silva 2012, Oro 2008, Botão 2007, Tomba 2019 ([fichamento-05](fichamento-05.md)) |
| 2026-10-31 | Leitura de Nogueira 2017 (UFG), Pinheiro 2011 (UFPB) e Costa 2007 (*Afro-Ásia*): exu-034, ogum-006 e xango-005 passaram a `fichado` | PDFs nos repositórios UFG e UFPB e no portal de periódicos da UFBA ([fichamento-04](fichamento-04.md)) |
| 2026-10-31 | Metadados de Ortiz 1978 e Landes 1947, usados como fonte primária de registros de 2ª mão | Open Library → `conferido_web` |
| 2026-10-31 | Metadados das 17 fontes `a_verificar`/`pista` usadas no fichamento | Open Library, Internet Archive, Crossref, repositórios UFG/UFPB; autores das teses identificados (Nogueira 2017, Pinheiro 2011) e título de Costa 2007 (DOI 10.9771/aa.v0i36.21145) |
| 2026-10-31 | Acesso a USP, UFRJ, HAL, Crossref, BDTD, theses.fr, Open Library | domínios liberados pelo autor nas configurações do ambiente |
| 2026-10-31 | Divergência aparente entre Bastide e Chiousse sobre a espada-de-ogum | Bastide, p. 165: registra o uso diurético; p. 192: o vínculo religioso vem da forma. Sem contradição |
