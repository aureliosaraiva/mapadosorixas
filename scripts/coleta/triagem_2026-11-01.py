#!/usr/bin/env python3
"""Decisões manuais da triagem da varredura nº 4 (coleta de 2026-11-01).

Alvo: expansão do MVP para o panteão completo — orixás além dos 5 (Oxalá,
Oxum, Iansã, Nanã, Omolu, Oxumarê, Ossaim, Logunedé, Obá, Ewá, Ibeji, Iroko,
Orunmilá/Ifá, Odudua, Olokun), cosmologia/hierarquia (Olodumare, Orum/Aiê,
Egungun, Iyami, Orí) e itãs/odu/oríkì. Consultas `v4-*` em `consultas.json`.

Mesmos critérios da varredura 3 (ver `triagem_2026-10-31.py`):
- **entra** (`conferido_web`): metadado de API idônea; tema central = orixá,
  cosmologia ou corpus oral; publicação acadêmica ou obra de praticante
  reconhecido. A/B/C como na varredura 3.
- **pista**: pertinente, mas com metadado incompleto (sem ano, edição ou
  autoria a conferir) ou editora sem revisão acadêmica clara.
- **descarta**: duplicata/edição/tradução/capítulo de obra já catalogada,
  resenha, literatura de ficção, autopublicação esotérica, fora do recorte
  (ex.: Olokun do Benim/Edo, Igala).

Uso: python3 scripts/coleta/triagem_2026-11-01.py
"""
import json
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = RAIZ / "data" / "fontes" / "coleta" / "2026-11-01"

ART, LIV, CAP, TES, DIS, DOC = "artigo", "livro", "capitulo", "tese", "dissertacao", "documento"
AC, TS, PR, DV, CO, EN, PA = "academica", "tese", "praticante", "divulgacao", "corpus_oral", "enciclopedia", "patrimonio"
J_ART = "artigo em periódico com revisão por pares; metadados e DOI conferidos na API"
J_OA = J_ART + "; acesso aberto"
J_UP = "monografia acadêmica em editora universitária/científica"
J_CAP = "capítulo em obra acadêmica (DOI Crossref)"
NG, LU, KE, BE, UM, MI, BA = "ioruba_nigeria", "lucumi", "candomble_ketu", "vodun_benim", "umbanda", "tambor_de_mina", "batuque_rs"

# (trecho do título, ano|None, id, tipo, categoria, tradições, confiabilidade, justificativa, extras)
ENTRA = [
    # ---- Cosmologia / hierarquia
    ("Ará Òrun Kìn-ìn Kin-in", 2019, "akande-2019-egungun", ART, AC, [NG], "B", J_OA + " (Genealogy, MDPI, CC BY); Egúngún de Òyó e equilíbrio ontológico.", {}),
    ("A Comparative Study of Olodumare", 2021, "ogungbemi-2021-olodumare", ART, AC, [NG], "B", J_OA + " (Yoruba Studies Review, Univ. da Flórida).", {}),
    ("Proof of Olódùmarè", 2024, "akin-otiko-2024-olodumare", ART, AC, [NG], "B", J_OA + " (Nsukka Journal of Religion); filosofia da religião iorubá.", {}),
    ("How man makes God in West Africa", 1981, "barber-1981-how-man", ART, AC, [NG], "A", J_ART + " (Africa, CUP); texto clássico sobre a relação devotos × òrìṣà.", {}),
    ("IYÁ MI OXORONGÁ: OLHARES SAGRADOS", 2021, "monteiro-2021-iya-mi", ART, AC, [KE], "B", J_ART + " (Ethnoscientia). Nação a confirmar na leitura.", {"titulo": "Iyá Mi Oxorongá: olhares sagrados do feminino no candomblé"}),
    ("Is Olodumare, God In Yoruba Belief, God?", 2014, "igboin-2014-olodumare", ART, AC, [NG], "B", J_OA + " (Kanz Philosophia); debate filosófico com Layi 2016.", {}),
    ("A Response to Benson O. Igboin", 2016, "layi-2016-olodumare", ART, AC, [NG], "B", J_OA + " (Kanz Philosophia); réplica a Igboin 2014.", {}),
    ("Iá Mi Oxorongá: As Mães Ancestrais", 2008, "santos-2008-ia-mi", ART, AC, [KE], "B", J_ART + " (Sankofa, USP, acesso aberto). Nação a confirmar.", {}),
    ("Masquerading Politics", 2017, "willis-2017-masquerading", LIV, AC, [NG], "A", J_UP + " (Indiana University Press); história do Egúngún em Òyó.", {"tipo_base": "book"}),
    ("pesquisa colaborativa com sacerdotisas da Deusa Iyami", 2019, "carvalho-2019-iyami", ART, AC, [KE], "B", J_ART + " (Fractal, UFF). Tradição a confirmar (o título fala em sacerdotisas de Iyami).", {}),
    ("Olodumare: God In Yoruba Belief And The Theistic Problem", 1998, "bewaji-1998-olodumare", ART, AC, [NG], "B", J_OA + " (African Studies Quarterly).", {}),
    ("The god of smallpox: aspects of Yoruba religious knowledge", 1985, "buckley-1985-smallpox", ART, AC, [NG], "B", J_ART + " (Africa, CUP); Ṣọ̀pọ̀nnọ́ (Omolu).", {}),
    ("Visões sobre Eshu", 2012, "oliva-2012-eshu", ART, AC, [NG], "B", J_ART + " (Revista Brasileira de História, SciELO); historiografia da cosmologia iorubá.", {}),
    ("Egungun Costuming in Abeokuta", 1982, "wolff-1982-egungun", ART, AC, [NG], "B", J_ART + " (African Arts).", {}),
    ("Egungun Masquerades in Iganna", 1978, "schiltz-1978-egungun", ART, AC, [NG], "B", J_ART + " (African Arts).", {}),
    ("The Role of Sculptures in Yoruba Egungun", 1991, "kalilu-1991-egungun", ART, AC, [NG], "B", J_ART + " (Journal of Black Studies).", {}),
    ("Èdè Àyàn", 2021, "famule-2021-ayan", ART, AC, [NG], "B", J_OA + " (Yoruba Studies Review); Àyàn e Egúngún.", {}),
    ("Olori, o dono da cabeça", 2010, "zacharias-2010-olori", ART, AC, [KE], "B", J_OA + " (Esboços, UFSC); Orí e orixá de cabeça. Nação a confirmar.", {}),
    # ---- Oxalá / Odudua / Olokun
    ("Obatala", 2009, "asante-mazama-2009-obatala", DOC, EN, [NG], "B", "verbete da Encyclopedia of African Religion (SAGE, 2009); DOI Crossref.", {"tipo_base": "reference-entry", "autores": ["Molefi Kete Asante (org.)", "Ama Mazama (org.)"]}),
    ("Disability and Human Diversity", 2021, "adegbindin-2021-eni-oosa", ART, AC, [NG], "B", J_OA + " (Yoruba Studies Review); Ọbàtálá e o ẹni-òòṣà.", {}),
    ("Orí Apéré O", 2001, "rodrigue-2001-ori-apere", LIV, AC, [KE], "B", "livro (Selo Negro, 2001) sobre as Águas de Oxalá; registro na Open Library.", {}),
    ("The Obatala Factor in Yoruba History", 1992, "lawuyi-1992-obatala", ART, AC, [NG], "B", J_ART + " (History in Africa).", {}),
    ("Myth, Ritual, and Visible Expressions of", 2024, "raheem-2024-obatala-olokun", LIV, AC, [NG], "B", "monografia acadêmica (Lexington Books, 2024) sobre Ọbàtálá e Olókun em Ilé-Ifẹ̀; registro na Open Library.", {"tipo_base": "book", "titulo": "Myth, Ritual, and Visible Expressions of Ọbàtálá and Olókun in Ilé-Ifẹ̀"}),
    ("Samuel Johnson’s view about Oduduwa", 2020, "jock-2020-oduduwa", ART, AC, [NG], "B", J_OA + " (HTS Teologiese Studies).", {}),
    ("İle-İfe: Geleneksel Yoruba Dininde", 2019, "seyfeli-2019-ile-ife", ART, AC, [NG], "B", J_OA + " (Artuklu Akademi); em turco, sobre Ilé-Ifẹ̀ e a criação.", {"idioma": "tr"}),
    ("Olóòkun", 1996, "mason-1996-olookun", LIV, PR, [LU], "B", "obra de John Mason, sacerdote e pesquisador lucumí (Yorùbá Theological Archministry); visão de dentro, a cotejar.", {}),
    # ---- Oxum / Iansã / Obá
    ("Divining the self", 2012, "love-2012-divining", LIV, AC, [NG], "B", J_UP + " (Penn State UP); cap. 6 sobre Ọ̀ṣun, Yemọja e Ọya.", {"tipo_base": "book"}),
    ("Against Feminine Erasure in Yoruba Ritual Archives", 2026, "afolabi-2026-oya", ART, AC, [NG, LU, KE], "B", J_OA + " (Yoruba Studies Review); Ọya no Atlântico negro.", {}),
    ("Entre Oyá y Santa Teresa", 2005, "fernandez-cano-2005-oya", ART, AC, [LU], "B", J_OA + " (Gazeta de Antropología, Univ. de Granada); sincretismo de Oyá.", {}),
    ("Oya", 1987, "gleason-1987-oya", LIV, AC, [NG, LU, KE], "B", "monografia de Judith Gleason (Shambhala, 1987) sobre Ọya na Nigéria e nas Américas; editora não acadêmica, autora pesquisadora.", {"tipo_base": "book"}),
    ("O presente de Oxum e a construção da multiplicidade", 2015, "rabelo-2015-oxum", ART, AC, [KE], "B", J_OA + " (Religião e Sociedade, SciELO).", {}),
    ("Ochún en la regla de ocha-ifá", 2026, "carrillo-2026-ochun", ART, AC, [LU], "B", J_ART + " (Argumentos).", {}),
    ("Nomination to the World Heritage List, Osun-Osogbo", 2004, "joffroy-2004-osun-osogbo", DOC, PA, [NG], "B", "dossiê de candidatura do Bosque Sagrado de Ọ̀ṣun-Òṣogbo ao Patrimônio Mundial (CRAterre/NCMM, 2004), depositado no HAL.", {}),
    # ---- Omolu / Sakpata
    ("Could Sòpònná Originate as a Black Death Deity", 2026, "amherd-2026-soponna", ART, AC, [NG], "B", J_OA + " (Yoruba Studies Review); hipótese histórica, a ler com cautela.", {}),
    ("La terre de Sakpata", 2010, "henry-2010-sakpata", ART, AC, [BE], "B", J_ART + " (Journal des Africanistes, OpenEdition, acesso aberto).", {}),
    ("Long day's journey to Rincón", 2002, "hagedorn-2002-babalu", ART, AC, [LU], "B", J_ART + " (British Journal of Ethnomusicology); San Lázaro/Babalú Ayé.", {}),
    ("Médico ferido", 1998, "caprara-1998-omolu", CAP, AC, [KE], "B", J_CAP + ": em Antropologia da Saúde (Fiocruz/Relume-Dumará), acesso aberto no SciELO Livros.", {}),
    ("OMOLU, OBALUAÊ, SÃO LÁZARO", 2020, "leite-2020-omolu", ART, AC, [KE, UM], "B", J_ART + " (Fragmentos de Cultura, PUC Goiás). Tradições a confirmar.", {"titulo": "Omolu, Obaluaê, São Lázaro, São Roque, a fé, a medicina do pobre"}),
    ("Sakpata, ein Beitrag afrikanischer Medizinmänner", 1982, "stocklin-1982-sakpata", ART, AC, [BE], "B", J_ART + " (Gesnerus); história da medicina.", {}),
    ("Vodun Sakpata et épidémie de variole", 2013, "kakpo-2013-sakpata", ART, AC, [BE], "B", J_ART + " (Ponts-Ponti); literatura oral sacra do golfo do Benim.", {}),
    ("Omolu quer todo mundo no Olubaje", 2022, "mota-2022-olubaje", ART, AC, [KE], "B", J_OA + " (Equatorial, UFRN). Nação a confirmar.", {"titulo": "“Omolu quer todo mundo no Olubaje”"}),
    ("A Bembé for San Lázaro–Babalú Ayé", 2020, "ochoa-2020-lazarus", LIV, AC, [LU], "B", J_UP + " (University of California Press, 2020: A Party for Lazarus); capítulo 8 sobre Babalú Ayé.", {"tipo_base": "book-chapter", "doi_exato": "10.1525/9780520974111-010", "autores": ["Todd Ramón Ochoa"], "titulo": "A Party for Lazarus: Six Generations of Ancestral Devotion in a Cuban Town"}),
    # ---- Ossaim / Oxumarê / Logunedé / Ibeji
    ("A floresta sagrada de Ossaim", 2011, "barros-2011-ossaim", LIV, AC, [KE], "B", "livro de José Flávio Pessoa de Barros, antropólogo (UERJ), sobre as folhas no candomblé (Pallas).", {}),
    ("Awo̦n ewé o̦sanyin", 1967, "verger-1967-osanyin", LIV, CO, [NG], "A", "textos iorubás de Ọ̀sanyìn recolhidos por Verger (Institute of African Studies, Univ. de Ifẹ̀, 1967); registro na Open Library.", {}),
    ("Por que das hastes de ossaim brotam pássaros", 2006, "sallum-2006-ossaim", ART, AC, [KE, NG], "B", J_OA + " (Revista do Museu de Arqueologia e Etnologia, USP).", {}),
    ("A indumentária de Lógunède", 2023, "santos-2023-logunede", ART, AC, [KE], "B", J_OA + " (Revista Calundu, UnB).", {}),
    ("Ibeji Custom in Yorubaland", 1971, "mobolade-1971-ibeji", ART, AC, [NG], "B", J_ART + " (African Arts).", {}),
    ("Ibeji Images of the Yoruba", 1973, "houlberg-1973-ibeji", ART, AC, [NG], "B", J_ART + " (African Arts); estudo de referência sobre Ìbejì.", {}),
    ("Orin ìbejì", 1971, "olayemi-1971-ibeji", LIV, CO, [NG], "B", "cantos de louvor aos gêmeos (Institute of African Studies, Univ. de Ibadan, 1971); registro na Open Library.", {}),
    ("Yoruba Customs and Beliefs Pertaining to Twins", 2002, "leroy-2002-twins", ART, AC, [NG], "B", J_ART + " (Twin Research, CUP).", {}),
    ("Tracing the Origin of Twins’ Birth", 2026, "ogunbunmi-2026-twins", ART, AC, [NG], "B", J_OA + " (Yoruba Studies Review).", {}),
    ("94. Ibeji Statuettes from Yoruba", 1944, "meyerowitz-1944-ibeji", ART, AC, [NG], "C", J_ART + " (Man, RAI); olhar colonial de 1944, valor documental.", {"titulo": "Ibeji Statuettes from Yoruba, Nigeria"}),
    ("PROBLEMÁTICA DOS LUGARES DE MEMÓRIA – O CASO DO ILÉ", 2019, "sousa-2019-osumare", ART, AC, [KE], "B", J_ART + " (Macabéa); terreiro Ilê Axé Oxumarê (Salvador) e lugares de memória.", {"titulo": "Entre escritos e falados: terreiros de candomblé e a problemática dos lugares de memória – o caso do Ilé Òsùmàrè Aràká Àṣẹ Ògòdó (Casa de Oxumarê)"}),
    ("cromática dos Orixás", 2024, "jesus-2024-cromatica", ART, AC, [KE], "B", J_OA + " (Sacrilegens, UFJF); cores dos orixás no Ketu.", {"titulo": "Cromática dos orixás: uma análise da nomenclatura e atribuição das cores aos orixás do candomblé ketu"}),
    ("As representações sociais dos orixás para a comunidade do Candomblé Ketu", 2024, "tosoli-2024-cantigas", ART, AC, [KE], "B", J_OA + " (Reflexão); representações a partir das cantigas.", {}),
    ("Voduns e Orixás assentados na Casa da Mina Nagô", 2022, "silva-2022-mina-nago", CAP, AC, [MI], "B", "capítulo em obra acadêmica (Maringá de todos os santos?), DOI Crossref; panteão de uma casa de Mina Nagô.", {}),
    ("O livro dos Orixás: África e Brasil", 2020, "parizi-2020-livro-orixas", LIV, AC, [NG, KE], "B", "livro em acesso aberto (Editora Fi, DOI 10.22350/9786559170319) de pesquisador doutor; cobre o panteão. Conferir rigor na leitura.", {}),
    # ---- Orunmilá / Ifá / itãs / oríkì
    ("IMAGES OF WOMEN IN THE IFÁ LITERARY CORPUS", 1997, "abimbola-1997-women", ART, AC, [NG], "A", J_ART + " (Annals of the New York Academy of Sciences); autor é a referência do corpus de Ifá.", {"autores": ["Wande Abimbola"], "titulo": "Images of Women in the Ifá Literary Corpus"}),
    ("Ifá will mend our broken world", 1997, "abimbola-1997-mend", LIV, AC, [NG, LU], "B", "entrevistas de Wande Abimbola (Aim Books, 1997) sobre Ifá na África e na diáspora; registro na Open Library.", {}),
    ("Is There Any Evidence for Hell in the Ifá Literary Corpus", 2023, "ofuasia-2023-ifa-hell", ART, AC, [NG], "B", J_OA + " (Religions, MDPI).", {}),
    ("Oriki Orisa: The Yoruba Prayer of Praise", 1990, "lindon-1990-oriki", ART, AC, [NG], "B", J_ART + " (Journal of Religion in Africa).", {}),
    ("I Will Chant Homage to the Orisa", 2014, "adeniji-neill-2014-oriki", CAP, AC, [NG], "B", J_CAP + " (Palgrave Macmillan, Indigenous Concepts of Education).", {}),
    ("The problem of gerontocracy in Africa", 2011, "adegbindin-2011-ifa", ART, AC, [NG], "B", J_ART + " (Human Affairs); leitura filosófica do corpus de Ifá.", {}),
    ("Odù Ifá in Transition", 2022, "anoba-2022-odu", ART, AC, [NG], "B", J_ART + " (Journal of Religion in Africa).", {}),
    ("Two Studies of Ifa Divination", 1966, "morton-williams-1966-ifa", ART, AC, [NG], "B", J_ART + " (Africa, CUP).", {}),
    ("80. The Divination of Ifa (A Fragment)", 1919, "wyndham-1919-ifa", ART, AC, [NG], "C", J_ART + " (Man, RAI). Documento colonial de 1919 (domínio público): usar como documento histórico.", {"titulo": "The Divination of Ifa (A Fragment)"}),
    ("A QUESTÃO DO AUTOCONHECIMENTO NA FILOSOFIA DE ORUNMILÁ", 2018, "noguera-2018-orunmila", ART, AC, [NG], "B", J_ART + " (ODEERE, UESB).", {"titulo": "A questão do autoconhecimento na filosofia de Orunmilá"}),
    ("Commonalities and Disparities in the Iconography of Opón Ifá", 2020, "akande-2020-opon", ART, AC, [NG], "B", J_ART + " (African Arts).", {}),
    ("Ifa Divination Trays from Isale-Oyo", 2011, "pogoson-2011-ifa", ART, AC, [NG], "B", J_ART + " (Cadernos de Estudos Africanos, OpenEdition, acesso aberto).", {}),
    ("Ìyẹ̀rẹ̀ Ifá", 1999, "elebuibon-1999-iyere", LIV, PR, [NG], "B", "cantos de Ifá (ìyẹ̀rẹ̀) publicados por Ifayemi Elebuibon, babaláwo de Òṣogbo; visão de dentro.", {"autores": ["Ifayemi Elebuibon"]}),
    ("Owner of the Day and Regulator of the Universe", 2022, "olupona-2022-ifa-healing", CAP, AC, [NG], "B", J_CAP + " (University of Arizona Press, Divination and Healing).", {"autores": ["Jacob K. Olupona"]}),
    ("Religious Pluralism in Africa: Insights from Ifa Divination Poetry", 2010, "olupona-2010-pluralism", CAP, AC, [NG], "B", J_CAP + " (Fortress Press, Ethics That Matters).", {}),
    ("Socrates and Ọ̀rúnmìlà", 2014, "oluwole-2014-orunmila", LIV, AC, [NG], "B", "monografia da filósofa Sophie Oluwole (Ark Publishers, 2014).", {}),
    ("5 What Is Ifa", 2020, "ogunnaike-2020-deep", LIV, AC, [NG], "B", J_UP + " (Penn State UP, 2020: Deep Knowledge); caps. 5–6 e 9 sobre Ifá.", {"autores": ["Oludamini Ogunnaike"], "titulo": "Deep Knowledge: Ways of Knowing in Sufism and Ifa, Two West African Intellectual Traditions"}),
    ("The Yorùbá god of drumming", 2015, "villepastour-2015-ayan", LIV, AC, [NG, LU], "A", J_UP + " (University Press of Mississippi); Àyàn na Nigéria e em Cuba.", {}),
]

PISTA = [
    ("Kò sí ewé, kò sí òrìsà", None, "silva-unb-ossaim", DIS, TS, [KE], "B", "dissertação (UnB) sobre folhas num terreiro; sem ano no registro.", {}),
    ("Àdanidá: homem, ambiente e orixá", 2020, "campelo-2020-adanida", ART, AC, [KE], "B", "Horizonte (PUC Minas); orixá tratado a confirmar.", {}),
    ("The Yorùbá high god", 2007, "verger-2007-high-god", LIV, AC, [NG], "B", "reedição (Black Madonna Enterprises, 2007) do artigo de Verger sobre o deus supremo iorubá; conferir a publicação original.", {}),
    ("Ifá divination corpus, the", None, "barber-rep-ifa", DOC, EN, [NG], "B", "verbete de Karin Barber na Routledge Encyclopedia of Philosophy; sem ano no registro.", {}),
    ("A prophet called Orunmila", 2010, "lijadu-2010-orunmila", LIV, PR, [NG], "C", "reedição/tradução (2010) da obra de E. M. Lijadu (Orunmila!, c. 1908); conferir edição original e tradutor.", {}),
    ("Iwe Ifa Orunmila", 1900, "sobanjo-iwe-ifa", LIV, CO, [NG], "C", "obra em iorubá de J. A. Ṣobanjo (Remo Syndicate Press); o ano 1900 no registro parece genérico; conferir data e direitos.", {}),
    ("Iwe ifa", 1951, "epega-1951-iwe-ifa", LIV, CO, [NG], "C", "obra em iorubá de D. Ọnadele Epega (Imọlẹ Oluwa Institute); conferir data, edição e direitos.", {}),
    ("Ìwé odù Ifá", 1995, "bogunmbe-1995-odu", LIV, PR, [NG], "C", "odù de Ifá por praticante (Ilé Ọ̀rúnmìlà Communications); editora de nicho.", {}),
    ("Sixteen mythological stories of Ifá", 1994, "fama-1994-sixteen", LIV, PR, [NG], "C", "narrativas de Ifá por praticante (Ilé Ọ̀rúnmìlà Communications); editora de nicho.", {}),
    ("Oduduwa Obatala", 1984, "pichardo-1984-oduduwa", LIV, PR, [LU], "C", "obra de Ernesto Pichardo, oriaté lucumí (Ediciones Universal); conferir conteúdo.", {}),
    ("Olókun", 1964, "akinjogbin-1964-olokun", LIV, AC, [NG], "C", "publicação do Yoruba Historical Research Scheme (I. A. Akinjogbin); conferir se é folheto ou monografia.", {}),
    ("Na fé de Vivaldo de Logunedé", 2006, "alexandre-2006-logunede", LIV, DV, [KE], "C", "publicação municipal (São Paulo, 2006) sobre um sacerdote de Logunedé.", {}),
    ("O presente de Oxum: bebês em candomblés", None, "rocha-unicamp-oxum", DIS, TS, [KE], "B", "dissertação (Unicamp) sobre bebês em candomblés Ketu; sem ano no registro.", {}),
    ("La venus lukumí", 2002, "feraudy-2002-venus", LIV, AC, [LU], "C", "Editorial de Ciencias Sociales (Havana); sobre Ochún, conferir conteúdo.", {}),
    ("Oro asa Òsányìn", 1999, "monteiro-1999-osanyin", LIV, PR, [KE], "C", "CETRAB; editora de nicho.", {}),
    ("A linguagem correta dos orixas", 1978, "durojaiye-1978-linguagem", LIV, PR, [KE], "C", "obra de praticante; editora e conteúdo a conferir.", {}),
    ("Oxalá, o criador dos homens e senhor de toda sabedoria", 2021, "machado-2021-oxala", CAP, DV, [KE], "C", "reconto educativo de itãs (Prosa de Nagô, Vanda Machado); útil como divulgação, não sustenta ficha.", {}),
    ("Pureza e confusão", 2018, "serra-2018-pureza", ART, AC, [KE], "B", "Anuário Antropológico (UnB, acesso aberto), de Ordep Serra; a DOAJ data 2018, possível digitalização de volume antigo; tema a confirmar.", {}),
    ("Osun Osogbo Sacred Grove", None, "probst-osun-osogbo", DOC, EN, [NG], "B", "verbete de Peter Probst (Routledge); sem ano no registro.", {}),
]

DESCARTA = [
    ("Olódùmarè", 1994, "reedição de idowu-1962-olodumare"),
    ("Orixás", 1981, "edição francesa (Métailié) de verger-1981-orixas"),
    ("Iemanjá & Oxum", 2004, "tradução brasileira de cabrera-1974-yemaya"),
    ("Yemoja", 2013, "duplicata de otero-falola-2013-yemoja"),
    ("Ifa Divination: Communication between Gods and Men", 1991, "reedição de bascom-1969-ifa"),
    ("Ifa divination poetry (Traditional African literature)", 1977, "duplicata de abimbola-1977-poetry"),
    ("Obatala", 2019, "capítulo de Dennett 1910 (domínio público, catalogado à parte)"),
    ("From Calundu to Candomblé", 2013, "capítulo da tradução inglesa de pares-2006-formacao"),
    ("Logunedé", 2000, "edição de lopes-2006-logunede (já no catálogo)"),
    ("Logunedé", 2002, "edição de lopes-2006-logunede (já no catálogo)"),
]
# capítulos de Sandoval 2007 (sandoval-2007-worldview, já no catálogo): registrar a cobertura no relatório
SANDOVAL = "Worldview, the Orichas, and"
BARBER91 = "I Could Speak Until Tomorrow"
DEEP = "Deep Knowledge"
EDO = ["Chalk Iconography in Olokun Worship", "Symbolism in Olokun Mud Art", "Olokun, the divinity of fortune"]

def n(s):
    return unicodedata.normalize("NFC", s or "").casefold()


def achar(cands, trecho, ano, tipo_base=None, doi=None):
    m = [c for c in cands if n(trecho) in n(c["titulo"])
         and (ano is None or c["ano"] == ano) and (tipo_base is None or c["tipo_base"] == tipo_base)
         and (doi is None or c.get("doi") == doi)]
    return m



def main():
    cand = json.loads((PASTA / "candidatos.json").read_text(encoding="utf-8"))
    cs = cand["candidatos"]
    dec, conf, erros = {}, {}, []
    for decisao, lista in (("entra", ENTRA), ("pista", PISTA)):
        for trecho, ano, fid, tipo, cat, trad, nivel, just, extra in lista:
            m = achar(cs, trecho, ano, extra.get("tipo_base"), extra.get("doi_exato"))
            if len(m) != 1:
                m = sorted(m, key=lambda c: (not c.get("doi"), -len(c["bases"])))
                if not m:
                    erros.append(f"{fid}: '{trecho}' ({ano}) não encontrado")
                    continue
            fonte = {"id": fid, "tipo": tipo, "categoria": cat, "tradicoes": trad, "confiabilidade_preliminar": nivel}
            for k in ("titulo", "autores", "ano", "idioma", "url"):
                if k in extra:
                    fonte[k] = extra[k]
            if fonte["tipo"] == "livro" and extra.get("tipo_base") == "book-chapter":
                fonte.setdefault("url", None)
            dec[m[0]["chave"]] = {"decisao": decisao, "motivo": None, "fonte": fonte, "justificativa": just}
    for trecho, ano, motivo in DESCARTA:
        for c in achar(cs, trecho, ano):
            if c["chave"] not in dec and (trecho != "Obatala" or c["tipo_base"] == "book-chapter"):
                dec[c["chave"]] = {"decisao": "descarta", "motivo": motivo}
    for c in cs:
        per = c.get("periodico") or ""
        if c["chave"] in dec:
            continue
        if SANDOVAL in per:
            dec[c["chave"]] = {"decisao": "descarta", "motivo": "capítulo de sandoval-2007-worldview (já no catálogo); cobertura anotada no relatório da varredura 4"}
        elif BARBER91 in per:
            dec[c["chave"]] = {"decisao": "descarta", "motivo": "capítulo de barber-1991-oriki (já no catálogo)"}
        elif DEEP in per:
            dec[c["chave"]] = {"decisao": "descarta", "motivo": "capítulo de ogunnaike-2020-deep (incorporado como livro)"}
        elif any(n(e) in n(c["titulo"]) for e in EDO):
            dec[c["chave"]] = {"decisao": "descarta", "motivo": "Olokun do reino do Benim (Edo), fora do recorte iorubá/afro-americano desta rodada"}

    # Conferência de fontes já catalogadas (a_verificar) com registro na coleta
    CONF_CAND = {
        "abimbola-1976-ifa": ("Ifá", 1976, "Open Library registra Oxford University Press Nigeria, 1976.", True),
        "abimbola-1968-ijinle": ("Ìjìnlè Ohùn Enu Ifá", 2006, "Open Library registra a edição de 2006 (University Press PLC); a 1ª edição (1968) não aparece no registro; ano citado mantido.", False),
    }
    for fid, (trecho, ano, nota, isbn) in CONF_CAND.items():
        m = [c for c in achar(cs, trecho, ano) if n(c["titulo"]).strip(" .") == n(trecho) or fid != "abimbola-1976-ifa"]
        if not m:
            erros.append(f"conferência {fid}: não encontrado")
            continue
        conf[fid] = {"chave": m[0]["chave"], "nota": nota, "isbn": isbn}
        dec[m[0]["chave"]] = {"decisao": "descarta", "motivo": f"já no catálogo como {fid} (usado para conferência)"}

    saida = {"_meta": {"descricao": "Decisões da triagem da varredura nº 4, geradas por scripts/coleta/triagem_2026-11-01.py. Aplicar com scripts/coleta/incorporar.py.",
                       "data": "2026-11-01"},
             "decisoes": dec, "conferencias": conf}
    (PASTA / "triagem.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    print(Counter(d["decisao"] for d in dec.values()), "conferências:", len(conf))
    for e in erros:
        print("ERRO", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
