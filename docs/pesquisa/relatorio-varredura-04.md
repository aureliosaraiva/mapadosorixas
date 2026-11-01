# Fase 1 — Relatório da varredura nº 4 (expansão para o panteão completo)

**Data:** 2026-11-01 · **Objetivo:** levantar fontes para a expansão de 5 para ~25 orixás, para a hierarquia e cosmologia (Olodumare, Orum/Aiê, funfun, Egungun, Iyami, Orí) e para os itãs, odù e oríkì. **Prioridade: texto integral acessível.** Só catálogo: nada foi fichado nesta rodada, e nenhum item passou por conferência humana.

## Resumo

| Indicador | Antes | Depois |
|---|---:|---:|
| Fontes no catálogo | 316 | **422** (+106) |
| `conferido_web` | 227 | **317** (+75 da coleta por API, +13 em domínio público, +2 promovidas) |
| `a_verificar` | 62 | 59 |
| `pista` | 27 | 46 (+19) |
| Fontes com `url` de texto integral ou página aberta | 49 | **106** |
| Idiomas | pt 159 · en 94 · fr 36 · es 18 · de 6 · it 2 · yo 1 | pt 189 · en 154 · fr 38 · es 23 · yo 8 · de 7 · it 2 · tr 1 |

Duas partes:

1. **Domínio público** (§2): 13 obras novas e 8 atualizadas, todas com URL de texto integral conferida. As de viajantes, missionários e administradores coloniais ficam com confiabilidade C e aviso de olhar colonial ou missionário em `observacoes`.
2. **Fontes modernas** (§3): coleta por API com 45 consultas novas (`v4-*`) em 5 bases, triagem manual registrada em script, 75 entradas e 19 pistas.

**Como reproduzir:**

```bash
python3 scripts/coleta/coletar.py --bases crossref,openlibrary,thesesfr,hal,doaj --data 2026-11-01 \
        --consultas $(python3 -c "import json;print(','.join(c['id'] for c in json.load(open('scripts/coleta/consultas.json'))['consultas'] if c['id'].startswith('v4-')))")
python3 scripts/coleta/triar.py --data 2026-11-01
python3 scripts/coleta/triagem_2026-11-01.py        # decisões manuais → triagem.json
python3 scripts/coleta/incorporar.py --data 2026-11-01
python3 scripts/coleta/dominio_publico_2026-11-01.py   # obras em domínio público + correções manuais (idempotente)
```

Mudanças nos coletores (não nos validadores):

- `pertinencia.py` ganhou termos para os orixás novos, a cosmologia e os itãs.
- "Osun" (estado nigeriano) e "Nana" (nome comum) contam como termos fracos, e "Osun State" e "Oyo State" entram na lista de exclusão.
- `incorporar.py` passou a rotular as observações pela data da coleta ("Varredura 4").

## 1. Acesso às bibliotecas digitais (testado em 2026-11-01)

| Acervo | Situação | Uso nesta rodada |
|---|---|---|
| Internet Archive (`advancedsearch`, `metadata`, `download`) | ✅ busca, metadados e `_djvu.txt` (texto OCR) funcionam. 🟡 HTTP 500 intermitente em alguns `_djvu.txt` (*Os africanos no Brasil*; Bowen 1857 baixou na 2ª tentativa) | 16 textos integrais baixados para `/tmp/v4txt` (fora do repo) para levantar sumário e cobertura |
| HathiTrust, API de catálogo (`catalog.hathitrust.org/api/volumes/brief/oclc/…`) | ✅ devolve `rightsCode` (pd/pdus/ic) | prova de domínio público (Full view) por OCLC |
| HathiTrust, leitor (`babel.hathitrust.org`) e site | 🔴 desafio anti-robô (Cloudflare "Just a moment") | Nina Rodrigues 1900 (pd) só pela URL, sem leitura |
| Gallica (BnF) | 🔴 403 "Sorry, you have been blocked" (Cloudflare), de novo | Baudin 1884 (original francês) não conferido |
| Biblioteca Brasiliana Guita e José Mindlin (`digital.bbm.usp.br`) | 🟡 a página do registro (`/handle/bbm/…`) responde; a busca (`/discover`) dá 404 | João do Rio, *As religiões no Rio* (1904, 1906) |
| Wikimedia Commons | ✅ (`action=raw`) | espelho do João do Rio de 1904 (da BBM) |
| Wikisource (API) | 🔴 429 (limite de requisições do IP compartilhado) | — |
| Project Gutenberg | 🟡 a página de busca proíbe raspagem; `gutendex.com` dá *timeout*. Nenhuma das obras-alvo está no Gutenberg, pelo que se sabe | — |
| Domínio Público (MEC, `dominiopublico.gov.br`) | 🔴 403 (Cloudflare) | — |
| Open Library (`search.json`) | ✅ | OCLC, edições e `ebook_access` |
| Crossref, Open Library, HAL, DOAJ (coleta) | ✅ (theses.fr respondeu, mas sem resultados para as consultas novas) | §3 |
| `books.scielo.org`, `www.mdpi.com`, `periodicos.urca.br`, `www.periodicos.unimontes.br` | 🔴 403 | Caprara 1998, Silva 2022, Ofuasia 2023, Akande 2019, Santos 2019 e Carrillo 2026: URL registrada, texto não baixado |
| `periodicos2.uesb.br` (ODEERE) | 🔴 503 | Noguera 2018 |
| `periodicos.ufpa.br` | 🔴 bloqueio do servidor (página de erro) | Monteiro & Azevedo 2021 (Iyá Mi Oxorongá) |
| `digibug.ugr.es` | 🟡 erro de protocolo HTTP/2 no curl | Fernández Cano 2005 (Oyá) |
| `hal.science` / `halshs` | 🔴 Anubis (como na sessão anticopia2) | Chiousse 1995 e o dossiê Ọ̀ṣun-Òṣogbo (Joffroy 2004) não baixam |

## 2. Domínio público: obras, URL e cobertura

Critério de domínio público: Internet Archive com item livre e `possible-copyright-status: NOT_IN_COPYRIGHT` quando informado, HathiTrust `pd`/`pdus` e data de morte do autor. O prazo é de 70 anos *post mortem* no Brasil e na Nigéria e de 80 anos na Espanha, onde mora o autor, para quem morreu antes de 1987. Para paráfrase com citação, que é o uso do projeto, o direito autoral da fonte não impede nada. A data de domínio público importa para distribuir trechos ou cópias.

A cobertura veio de **sumários e cabeçalhos de seção lidos nos textos OCR** e da contagem de menções por nome, com grafias da época (`/tmp/v4scripts/cobertura.py`, fora do repo). Isso **não é fichamento**: as páginas são as do sumário impresso, a conferir na leitura.

| id | Obra | Texto integral | Direitos | Orixás, cosmologia e itãs cobertos |
|---|---|---|---|---|
| `ellis-1894-yoruba` (C) | Ellis, *The Yoruba-Speaking Peoples* (1894) | [IA](https://archive.org/details/yorubaspeakingp00elligoog) · HathiTrust hvd.32044020314415 | ✅ autor m. 1894 | cap. II "Chief gods" (pp. 34–69): Olorun, Obatala, Odudua, Orungan/Yemaja, Shango, Ifa (com os 16 odù *meji*), Elegba. Cap. III "Minor gods" (pp. 70–84): Olokun, Olosa, Shigidi, Dada, Oshun, Oya, Orisha Oko, Osanyin, Aroni, Aja, Ibeji, Oshumare. Cap. VI Egungun e Oro; VII almas; XIV contos |
| `johnson-1921-history` (B) | S. Johnson, *The History of the Yorubas* (1921) | [IA](https://archive.org/details/historyofyorubas00john) · HathiTrust inu.39000005818294 | ✅ autor m. 1901, editor m. 1920 | parte I, cap. III "Religion" (pp. 26–39); parte II, cap. I (pp. 143–152): Oduduwa, Oranyan, Sango como alafin. Leitura histórica de Oyó |
| `frobenius-1913-voice` (C), nova | Frobenius, *The Voice of Africa* (1913, trad. R. Blind) | [IA vol. I](https://archive.org/details/voiceofafricabei01frobuoft) · [vol. II](https://archive.org/details/voiceofafricabei02frobuoft) | ✅ autor m. 1938 | vol. I, caps. X–XIV: base da religião iorubá (p. 186), Xangô (p. 204), Ifá e odù (p. 228), Ifẹ̀ (p. 265), cabeça de Olokun (p. 292). A tese da "Atlântida" é especulação descartada |
| `frobenius-1912-afrika` (C) | *Und Afrika sprach* (original alemão) | [IA](https://archive.org/details/undafrikasprachb00frob) | ✅ | o mesmo, em alemão |
| `farrow-1926-faith` (C), nova | Farrow, *Faith, Fancies and Fetich* (1926) | [IA](https://archive.org/details/faithfanciesfeti00farr) · HathiTrust (pd) | 🟡 domínio público nos EUA; data de morte do autor a conferir para a Europa | Ser Supremo (Olorun); 2 caps. "The Orishas": Obatala, Odudua, Shango, Oya, Ogun, Eshu, Ifa/Orunmila, Yemaja, Olokun, Oshun, Sopono, Osanyin, Ibeji; mortos (Egungun, Oro); hino iorubá. Tese que declara querer justificar a missão |
| `dennett-1910-nigerian` (C), nova | Dennett, *Nigerian Studies* (1910) | [IA](https://archive.org/details/nigerianstudieso00dennuoft) · HathiTrust (pd) | ✅ autor m. 1921 | criação e Ifẹ̀ (p. 17); Oro e Egungun (p. 28); Jakuta (p. 65); Odudua (p. 73); Obatala (p. 81); Ifá (p. 86); Eshu (p. 94); Aganju e Yemoja com os filhos (p. 97); Olokun e Olosa (p. 106); Ogun e Oshowsi (p. 116); odù de Ifá (p. 147); Shango, Oya, Oba e Oshun (p. 156). Esquema próprio de quaternidades |
| `dennett-1906-back` (C), nova | Dennett, *At the Back of the Black Man's Mind* (1906) | [IA](https://archive.org/details/atbackofblackman00dennuoft) | ✅ | **Kongo** (Bavili: nkisi, Nzambi) e Bini/Edo. Quase nada de orixás; serve para inquices e cosmologia banta |
| `baudin-1885-fetichism` (C), nova | Baudin, *Fetichism and Fetich Worshipers* (trad. 1885 de *Fétichisme et féticheurs*, 1884) | [IA](https://archive.org/details/fetichismfetichw00baud) · HathiTrust (pd) | ✅ | deuses "superiores" (Obatala, Odudua, Ifa), "semideuses" e "gênios"; menciona Shango, Oya, Elegba, Olokun, Ibeji, Oro e Egungun. Demoniza Exu. O original francês (`baudin-1884-fetichisme`) não foi achado aberto (Gallica 403) |
| `nina-rodrigues-1935-animismo` (C), nova | Nina Rodrigues, *O animismo fetichista dos negros baianos* (ed. 1935, notas de A. Ramos) | [IA](https://archive.org/details/animismofetichista) | ✅ no Brasil; 🟡 na Espanha as notas de Ramos só em 2030; HathiTrust marca "ic" | Salvador na década de 1890: Olorun, Obatalá, Xangô, Ogum, Oxóssi (Odé), Iemanjá ("Yê-man-já"), Exu/Elegbá, Ifá, Dadá, iniciação e possessão. Viés racialista |
| `nina-rodrigues-1900-animisme` (B) | idem, ed. francesa de 1900 | [HathiTrust coo.31924020011759](https://babel.hathitrust.org/cgi/pt?id=coo.31924020011759) (pd; leitor bloqueado aqui) | ✅ | idem |
| `nina-rodrigues-1932-africanos` (B) | *Os africanos no Brasil* (1932) | [IA](https://archive.org/details/osafricanosnobrasil) (`_djvu.txt` com HTTP 500 em 2026-11-01) | 🟡 texto de NR livre; revisão de Homero Pires (m. 1962) protegida | sobrevivências religiosas: orixás, voduns, culto malê |
| `querino-1955-raca` (B), nova | Querino, *A raça africana e os seus costumes* (textos de 1916–17; ed. 1955) | [IA](https://archive.org/details/aracaafricana) | ✅ autor m. 1923 | candomblés de Salvador no começo do séc. XX, por um intelectual negro baiano |
| `joao-do-rio-1904-religioes` (C), nova | João do Rio, *As religiões no Rio* (1904) | [Commons/BBM](https://commons.wikimedia.org/wiki/File:As_religi%C3%B5es_no_Rio_(1904).pdf) · [BBM 1906](https://digital.bbm.usp.br/handle/bbm/2680) | ✅ autor m. 1921 | "No mundo dos feitiços": casas de orixás e alufás no Rio de 1904. Jornalismo sensacionalista |
| `ortiz-1906-brujos` (C), nova | Ortiz, *Los negros brujos* (1906) | [IA (ed. digital Fund. Larramendi, 2020)](https://archive.org/details/hampa-afro-cubana-los-negros-brujos) | 🟡 livre nos EUA e em Cuba; **na Espanha só em 2050** | primeira etnografia dos orixás lucumís (Changó, Obatalá, Yemayá, Elegguá, Ochún), em chave criminológica |
| `ellis-1890-ewe` (C), nova | Ellis, *The Ewe-Speaking Peoples* (1890) | [IA](https://archive.org/details/ewespeakingpeopl0000abel) · HathiTrust (pd) | ✅ | voduns fon e ewe (Legba, Sapata, Khebioso etc.): base para as equivalências jeje |
| `bouche-1885-cote` (C), nova | Bouche, *La Côte des Esclaves et le Dahomey* (1885) | [IA](https://archive.org/details/lactedesesclav00bouc) | ✅ | "État religieux" (p. 101), contos nagôs (p. 221), provérbios (p. 239), Daomé (p. 365) |
| `ajisafe-1924-laws` (B), nova | Ajisafe Moore, *The Laws and Customs of the Yoruba People* (1924) | [IA](https://archive.org/details/lawscustomsofyor00moorrich) (reimpressão sem data) | ✅ autor m. 1940 | direito e costumes; Egungun, Oro, Ifá e Ọ̀sanyìn de passagem |
| `bowen-1857-adventures` (C) | Bowen, *Central Africa* (1857) | [IA](https://archive.org/details/centralafricaadv00bowe_0) | ✅ | pouco: Ifá, Xangô, Ogum, Oro, Egungun |
| `bowen-1858-grammar` (C), nova | Bowen, *Grammar and Dictionary of the Yoruba Language* (1858) | [IA](https://archive.org/details/grammardictionar00bowerich) · HathiTrust (pd) | ✅ | verbetes de orixás e termos religiosos em grafia do séc. XIX |
| `burton-1863-abeokuta` (C) | Burton, *Abeokuta and the Camaroons Mountains* (1863) | [IA vol. I](https://archive.org/details/abeokutaandcama00burtgoog) · [vol. II](https://archive.org/details/abeokutaandcama02burtgoog) | ✅ | menções esparsas (muitos "Ogun" são o rio) |
| `wyndham-1919-ifa` (C), nova (coleta) | Wyndham, "The Divination of Ifa (a fragment)", *Man* (1919) | JSTOR (DOI 10.2307/2839981) | ✅ (1919) | fragmento de Ifá |

**Não localizados ou com direitos incertos** (→ [PENDENCIAS](PENDENCIAS.md)):

- **E. M. Lijadu**, *Ifá* (1897/1923) e *Orunmila!* (1908), em iorubá: não aparecem no IA nem na Open Library. Só a reedição em tradução *A prophet called Orunmila* (2010), que entrou como pista.
- **D. O. Epega**, *The Mystery of Yoruba Gods* (1931): consta na Open Library, sem *e-book*. *Iwe Ifa* (1951) entrou como pista. A data de morte do autor é desconhecida e os direitos estão indefinidos.
- **J. O. Lucas**, *The Religion of the Yorubas* (1948): no IA só por empréstimo; não está em domínio público.
- **Talbot**, *The Peoples of Southern Nigeria* (1926): no IA, só a reedição de 1969, por empréstimo.
- **Frobenius**, *Atlantis*, vol. X (*Die atlantische Götterlehre*, 1926): não achado no IA, embora outros volumes de *Atlantis* estejam lá. Pista para itãs em alemão.
- **J. A. Ṣobanjo**, *Iwe Ifa Orunmila*: entrou como pista, com ano a conferir.
- Lachatañeré, *¡¡Oh, mío Yemayá!!* (1938): HathiTrust "ic"; na Espanha, só em 2033.
- **Cópias de terceiros sem licença clara**: Abimbola, *Sixteen Great Poems of Ifá* (item de usuário no IA) e *Ifá: An Exposition…* (PDF em thinkyorubafirst.org). **Não usar** sem confirmar a autorização; ficam fora do catálogo como URL.

## 3. Fontes modernas: coleta por API e triagem

**1.181 itens baixados** (Crossref 788, Open Library 245, HAL 31, DOAJ 117, theses.fr 0) → 795 grupos → 18 já no catálogo · 288 sem termo de pertinência · **489 candidatos**. Triagem: **75 entram**, **19 pistas**, 38 descartes manuais e 357 sem incorporação automática. Destes, 282 são periféricos (literatura, artes, educação, saúde), 36 são autopublicação ou editora esotérica (Original Publications, Panapo, Lulu, CreateSpace, Madras), 31 não são bibliográficos, 5 são capítulos de obra já catalogada e 3 são resenhas. Decisões legíveis em [`scripts/coleta/triagem_2026-11-01.py`](../../scripts/coleta/triagem_2026-11-01.py) e resumo em `data/fontes/coleta/2026-11-01/triagem_resumo.json`.

**Descartes de recorte:**

- **Olokun do reino do Benim (Edo)**: Rosen 1989, Ben-Amos 1973, Imasogie 1980 e Izevbigie 1978. Há literatura sólida; decidir se entra (decisão para o autor ou o conselho).
- Igala (Boston 1974).
- Capítulos de Sandoval 2007 e de Barber 1991, obras já catalogadas.

Sandoval 2007 (`sandoval-2007-worldview`, já no catálogo) tem **capítulo por orixá** com DOI:

- Obatalá e Oduduwa
- Changó
- Oshún, Oyá e Obba
- Ochosi, Orisha Oko, Ibeyi e Agayú
- Olokun e Yemayá
- Babalú Ayé
- Osain

**Promovidas a `conferido_web`:** `abimbola-1976-ifa` (Open Library, OUP Nigéria 1976) e `abimbola-1968-ijinle` (a Open Library registra a ed. de 2006; ano citado mantido).

## 4. Por entidade: o que há de texto aberto e o que só existe impresso

"Aberto" = URL registrada no catálogo (domínio público ou acesso aberto). Já lidas no projeto: Bastide 1961 e Chiousse 1995 (ver §5). Fontes centrais impressas → [PENDENCIAS](PENDENCIAS.md) §2.

| Entidade | Texto aberto (catálogo) | Só impresso, pago ou bloqueado (centrais) |
|---|---|---|
| **Oxalá / Obatalá** (funfun) | Ellis 1894 cap. II; Dennett 1910 cap. VII; Farrow 1926; Baudin 1885; Nina Rodrigues 1935; **Bastide 1961** (já lido: pp. 28, 32, 90, 95–98, 106–127, 182–192); Adegbindin 2021 ([YSR](https://journals.flvc.org/ysr/article/view/129917)) | Verger 1981 *Orixás*, Verger *Lendas*, Prandi *Mitologia*; Rodrigué 2001 (*Orí Àpéré Ó*, Águas de Oxalá); Lawuyi 1992; Raheem & Elugbaju 2024; Sandoval 2007 |
| **Oxum** | Ellis cap. III; Dennett cap. XVI; Farrow; **Bastide** (pp. 28–32, 89–92, 101–127, 187); Rabelo 2015 ([SciELO](http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-85872015000100237&lng=en&tlng=en)); dossiê Ọ̀ṣun-Òṣogbo (Joffroy 2004, HAL, bloqueado aqui) | Murphy & Sanford 2001 (*Ọ̀ṣun across the Waters*); Cabrera 1974; Love 2012; Carrillo 2026 (OJS 403) |
| **Iansã / Oyá** | Ellis cap. III; Dennett cap. XVI; Farrow; Baudin; **Bastide** ("Yansan": pp. 101–126, 183–189); Afolabi 2026 ([YSR](https://doi.org/10.32473/ysr.11.1.141483)); Fernández Cano 2005 (Digibug, erro HTTP/2 aqui) | Gleason 1987; Theodoro 2010; Sandoval 2007 |
| **Nanã** | **Bastide** (pp. 32, 103–104, 119–126); Ellis 1890 (vodum, de passagem) | nenhuma monografia aberta achada; Verger 1981; Prandi *Mitologia*. **Lacuna**: as consultas "Nanã orixá" e "Nana Buruku" não trouxeram fonte acadêmica dedicada |
| **Omolu / Obaluaiê / Sakpata / Babalú Ayé** | **Bastide** (pp. 28–30, 89, 101–127, 185, 192); Farrow ("Sopono"); Ellis 1890 (Sapata); Henry 2010 ([OpenEdition](https://journals.openedition.org/africanistes/2572)); Mota 2022 ([Equatorial](https://periodicos.ufrn.br/equatorial/article/view/26154)); Leite 2020 ([Fragmentos](https://seer.pucgoias.edu.br/index.php/fragmentos/article/view/7748)); Caprara 1998 (SciELO Livros, 403 aqui); Amherd 2026 ([YSR](https://journals.flvc.org/ysr/article/view/143210)) | Buckley 1985; Hagedorn 2002; Ochoa 2020; Kakpo 2013; Stöcklin 1982 |
| **Oxumarê** | Ellis cap. III (Oshumare); Bastide p. 121 (uma página); Santos 2019 (Casa de Oxumarê, OJS 403) | Verger 1981; Prandi. **Lacuna**: quase nada acadêmico dedicado; Vieira 2006 (Madras) descartado |
| **Ossaim / Ọ̀sanyìn** | Ellis cap. III; Farrow; **Bastide** (pp. 118, 183–190); Sallum & Silva 2006 ([Rev. MAE-USP](https://revistas.usp.br/revmae/pt_BR/article/view/89723)) | Barros 2011 (*A floresta sagrada de Ossaim*); Verger 1967 (*Awọn ewé Ọ̀sanyìn*) e 1995 (*Ewé*); Athayde 2025 |
| **Logunedé** | Santos 2023 ([Calundu](https://periodicos.unb.br/index.php/revistacalundu/article/view/47629)); Bastide cita Logun em 11 páginas fora das já lidas | Lopes 2006 (Pallas; Open Library registra eds. de 2000 e 2002) |
| **Obá** | Ellis (lista); Dennett cap. XVI; **Bastide** (pp. 116, 121–122) | Sandoval 2007; Verger 1981. **Lacuna** |
| **Ewá** | nada (Bastide: 0 menções) | Verger 1981; Prandi. **Lacuna total** nas bases; fica para exemplar |
| **Ibeji** | Ellis cap. III; Farrow (frontispício); Bastide p. 103; Ogunbunmi 2026 ([YSR](https://doi.org/10.32473/ysr.11.1.141497)) | Houlberg 1973; Mobolade 1971; Leroy et al. 2002; Ọlayẹmi 1971 (*Orin ìbejì*) |
| **Iroko** (Loko) | **Bastide** (pp. 94–96) | nenhum acadêmico dedicado achado (os resultados de "iroko" são madeira e botânica). **Lacuna** |
| **Orunmilá / Ifá / odù** | Ellis cap. II (16 odù *meji*); Dennett caps. VIII e XV; Frobenius 1913 cap. XII; Farrow; Baudin; Pogoson 2011 ([OpenEdition](https://journals.openedition.org/cea/196)); UNESCO (Ifá); Noguera 2018 (ODEERE, 503 aqui); Ofuasia 2023 (MDPI, 403) | **Abimbola 1975, 1976 e 1977** (corpus); Bascom 1969 e 1980; Olupona & Abiodun 2016; Ogunnaike 2020; Morton-Williams 1966; Elebuibon 1999 |
| **Odudua / Ifẹ̀** | Ellis cap. II; Dennett cap. VI; Johnson parte II; Frobenius cap. XIII; Jock 2020 ([HTS](https://hts.org.za/index.php/hts/article/view/6013)); Seyfeli 2019 (turco, [DergiPark](https://dergipark.org.tr/tr/download/article-file/909860)) | Raheem & Elugbaju 2024 |
| **Olokun** | Ellis cap. III; Dennett cap. XI; Frobenius (cabeça de Olokun) | Mason 1996 (lucumí); Raheem & Elugbaju 2024; a literatura edo ficou fora do recorte |
| **Olodumare / Olorun** (hierarquia) | Ellis; Farrow; Dennett; Ogungbemi 2021, Igboin 2014, Layi 2016, Bewaji 1998, Akin-Otiko 2024 (todos abertos) | **Idowu 1962**; Verger, "The Yoruba High God" (pista: ed. 2007); Beniste 1997 (*Òrun-Àiyé*) |
| **Egungun / Egum** | Ellis cap. VI; Dennett cap. III; Farrow; Akande 2019 (MDPI, 403); Fámúlẹ̀ 2021 ([YSR](https://journals.flvc.org/ysr/article/view/129886)); Bastide (pp. 98, 103, 165, 183, 188) | **Santos 1976** (*Os Nàgô e a morte*); Willis 2017; Wolff 1982; Schiltz 1978; Kalilu 1991 |
| **Iyami / Ìyá Mi** (abordagem acadêmica) | Santos 2008 ([Sankofa](https://revistas.usp.br/sankofa/pt_BR/article/view/88730)); Carvalho & Costa 2019 ([Fractal](https://periodicos.uff.br/fractal/article/view/29003)); Monteiro & Azevedo 2021 (Ethnoscientia, bloqueado aqui) | Augras 1989; Verger, "Grandeur et décadence du culte de Ìyámi Ọ̀ṣọ̀rọ̀ngà" (1965), **não está no catálogo**: pista para a próxima sessão do catálogo |
| **Orí** | Zacharias 2010 ([Esboços](https://periodicos.ufsc.br/index.php/esbocos/article/view/14762)); Ellis cap. VII | Rodrigué 2001; Abimbola 1976 |
| **Itãs e oríkì** (corpus) | Ellis cap. XIV (contos); Bouche cap. XII (contos nagôs); Lindon 1990 (JSTOR); Jesus 2024 (cores, [Sacrilegens](https://periodicos.ufjf.br/index.php/sacrilegens/article/view/43378)); Tosoli & Peixoto 2024 (cantigas, [Reflexão](https://periodicos.puc-campinas.edu.br/reflexao/article/view/8580)); Parizi 2020 ([Editora Fi](https://www.editorafi.org/031orixas), panteão inteiro, acesso aberto) | **Prandi 2001 *Mitologia***; **Verger 1985 *Lendas***; Beier 1980; Barber 1991; Cabrera 1954; Bolívar 1990; Beniste 2006 (*Mitos yorubás*) |

## 5. O que já foi lido e cobre os orixás novos

- **Bastide 1961** (`bastide-1958-candomble`; texto da UFRJ baixado de novo nesta sessão para `/tmp/refs`). As páginas **já lidas** (26–32, 89–128, 165, 182–192) mencionam:
  - Oxalá (27 pp.), Oxum (20), Iansã ("Yansan", 13), Omolu (16), Nanã (8), Ossaim (4), Obá (3), Iroko (3), Odudua (3), Olorum (4), Egum (5), Ibeji (1) e Oxumarê (1, p. 121);
  - Logunedé só fora delas (11 pp.); Ewá em nenhuma.
  - O cap. sobre o tempo sagrado (pp. 105–128) dá **dias da semana** e festas por cidade para quase todos; pp. 26–32 dão **cores dos colares**; pp. 182–192 dão **plantas**.
  - **Pode ser fichado já, sem nova leitura de fonte**: basta reabrir as mesmas páginas para os orixás novos.
- **Chiousse 1995**, parte III, pp. 225–291 (perfis de orixás com cores, datas, emblemas e plantas, segundo pais e mães de santo):
  - os 5 do MVP ocupam pp. 236–241 (Iemanjá, Xangô), 259–260 (Oxóssi), 266–267 (Ogum) e 289–291 (Exu);
  - as **páginas intermediárias (227–235, 242–258, 261–265, 268–288) trazem os demais perfis**.
  - A lista exata não pôde ser conferida nesta sessão porque o HAL está com desafio anti-robô também no PDF ([PENDENCIAS](PENDENCIAS.md) §1). Quando o autor salvar o PDF em `/tmp/refs-pdf/chiousse-1995-divins.pdf`, o lote A pode usar as mesmas páginas.

## 6. Plano de leitura em lotes

| Lote | Entidades | Fontes abertas já disponíveis | Pode começar? | Depende de |
|---|---|---|---|---|
| **A** | Oxalá, Oxum, Iansã, Nanã, Omolu | **Bastide 1961** (já lido, só reabrir), **Chiousse 1995** (PDF salvo à mão), Ellis 1894, Dennett 1910, Farrow 1926, Nina Rodrigues 1935, Baudin 1885 (documentos históricos, C), Rabelo 2015, Henry 2010, Mota 2022, Leite 2020, Afolabi 2026, Amherd 2026 | ✅ **sim**, com Bastide e os artigos abertos; Chiousse quando o PDF estiver em `/tmp/refs-pdf/` | Verger 1981, Prandi 2001, Murphy & Sanford 2001 e Cabrera 1974 para origem africana e itãs |
| **B** | Oxumarê, Ossaim, Logunedé, Obá, Ewá, Ibeji (e Iroko) | Bastide (Ossaim, Obá, Iroko, Ibeji; Logunedé em páginas não lidas), Ellis cap. III (Oshumare, Osanyin, Ibeji), Dennett cap. XVI (Oba), Sallum 2006, Santos 2023, Ogunbunmi 2026 | 🟡 **parcial**: Ossaim, Obá, Ibeji e Iroko têm base aberta; **Oxumarê e Ewá quase não têm** | Verger 1981 e 1967, Barros 2011, Lopes 2006, Houlberg 1973; Ewá e Oxumarê dependem de exemplar |
| **C** | Cosmologia e hierarquia: Olodumare/Olorum, Orum/Aiê, funfun, Orí, Odudua, Olokun, Egungun, Iyami | Ellis caps. II, VI e VII; Dennett caps. II, III, VI e XI; Farrow; Johnson parte II; Ogungbemi 2021; Igboin 2014; Layi 2016; Bewaji 1998; Akin-Otiko 2024; Jock 2020; Fámúlẹ̀ 2021; Santos 2008; Carvalho 2019; Zacharias 2010 | ✅ **sim**, com a ressalva de que a hierarquia africana fica sustentada sobretudo por fontes coloniais (C) e por filosofia da religião (B). Para o Brasil faltam Santos 1976 e Beniste 1997 | Idowu 1962, Santos 1976, Beniste 1997, Augras 1989, Willis 2017 |
| **D** | Itãs, odù e oríkì | Ellis caps. II (16 *meji*) e XIV; Dennett cap. XV; Bouche cap. XII; Pogoson 2011; Parizi 2020; Lindon 1990 (JSTOR); Bastide p. 123 (já usado: roubo do fogo) | 🔴 **não, para itãs no Brasil**: o corpus central (Prandi *Mitologia*, Verger *Lendas*, Abimbola) é impresso ou protegido; cópias online de Abimbola não têm licença. Dá para preparar só a estrutura (odù, oríkì) com Ellis, Dennett e artigos | Prandi 2001, Verger 1985, Abimbola 1975/1976/1977, Barber 1991, Beier 1980, Cabrera 1954, Bolívar 1990, Beniste 2006 |

**Ordem sugerida:** A (Bastide e artigos) → C → B (parcial) → D quando chegarem os exemplares. Em todos os lotes:

- Fontes C (Ellis, Dennett, Farrow, Baudin, Frobenius, Nina Rodrigues, Ortiz, João do Rio) entram só como **documento histórico** de uma época e de um lugar, com a casa ou região dita pela fonte, e **nunca sozinhas** para um atributo. A sessão deve anotar o viés no registro.
- O anti-cópia com texto integral (regra do `CLAUDE.md`) vale para os textos do IA: `baixar_refs.py` precisa de `url` (já preenchida) ou do `_djvu.txt` salvo em `/tmp/refs/<id>.txt`.

## 7. Observações e sugestões

- **Lacunas reais** (nada acadêmico aberto ou dedicado nas bases): **Ewá, Oxumarê, Nanã, Obá e Iroko**. São orixás cultuados sobretudo no Brasil (Ewá, Logunedé) ou com culto africano pouco estudado; dependem de Verger, Prandi e literatura de praticantes da Pallas (Coleção Orixás, PENDENCIAS §3).
- **BDTD e OpenAlex** continuam sem resposta. Teses brasileiras sobre esses orixás (por exemplo, dissertações sobre Logunedé e Oxumarê) provavelmente existem e não apareceram. Repetir `coletar.py --bases bdtd,openalex --consultas <v4-*>` quando voltarem.
- **Pistas para a próxima sessão do catálogo:**
  - Verger, "Grandeur et décadence du culte de Ìyámi Ọ̀ṣọ̀rọ̀ngà" (*Journal de la Société des Africanistes*, 1965; possivelmente aberto no Persée);
  - Verger, "The Yoruba High God" (*Odu*, 1966);
  - Abimbola, *Sixteen Great Poems of Ifá* (UNESCO, 1975), checando se a UNESCO tem PDF oficial (UNESDOC).
- A categoria `etno_classica` agora tem 41 fontes; quase todas as novas são C. O site deve deixar claro, quando citar essas fontes, que se trata de **documento histórico**.
