#!/usr/bin/env python3
"""Decisões manuais da triagem da varredura nº 3 (coleta de 2026-10-31).

Cada decisão localiza o candidato em `candidatos.json` por trecho do título
(+ ano/base quando preciso) e grava `triagem.json` com a chave estável do
grupo. Assim, a triagem é legível aqui e reproduzível. Critérios:

- **entra** (`conferido_web`): metadados vindos de API idônea (Crossref,
  Open Library, theses.fr, HAL, DOAJ); tema central = orixás do MVP ou
  tradições com poucas fontes; publicação acadêmica (periódico revisado,
  tese, editora universitária) ou obra de praticante reconhecido.
  Confiabilidade: A = monografia/obra de referência de pesquisador
  consolidado ou clássico; B = artigo revisado por pares, tese, capítulo
  acadêmico, obra de sacerdote(isa) publicada; C = divulgação qualificada.
- **pista**: pertinente, mas com metadado incompleto (sem ano, título
  truncado), possível resenha ou autoria/venue a conferir.
- **descarta**: duplicata de fonte já catalogada (outra edição, tradução,
  capítulo de obra já no catálogo), resenha, item que não é sobre o tema.

Os demais candidatos sem decisão manual recebem motivo automático em
`incorporar.py` (autopublicação/esotérico, resenha, tipo não bibliográfico,
periférico ao recorte).

Uso: python3 scripts/coleta/triagem_2026-10-31.py
"""
import json
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = RAIZ / "data" / "fontes" / "coleta" / "2026-10-31"

ART, LIV, CAP, TES, DIS, DOC = "artigo", "livro", "capitulo", "tese", "dissertacao", "documento"
AC, TS, PR, DV = "academica", "tese", "praticante", "divulgacao"
J_ART = "artigo em periódico com revisão por pares; metadados e DOI conferidos na API"
J_TES = "tese de doutorado registrada em base nacional de teses (theses.fr/HAL)"
J_UP = "monografia acadêmica em editora universitária/científica"
J_CAP = "capítulo em obra acadêmica de editora universitária (DOI Crossref)"

# (trecho do título, ano|None, id, tipo, categoria, tradições, confiabilidade, justificativa, extras)
ENTRA = [
    # ---- Batuque (RS)
    ("“A cozinha é a base da religião”: a culinária ritual no batuque", 1996, "correa-1996-cozinha", ART, AC, ["batuque_rs"], "B", J_ART + " (Horizontes Antropológicos).", {}),
    ("antropologia visual em uma casa de batuque", 1995, "polvora-1995-batuque", ART, AC, ["batuque_rs"], "B", J_ART + ".", {}),
    ("REAFRICANIZAÇÃO EM TERREIROS DE BATUQUE", 2010, "bem-2010-reafricanizacao", ART, AC, ["batuque_rs"], "B", J_ART + " (Debates do NER).", {"titulo": "Apontamentos sobre formas alternativas de reafricanização em terreiros de batuque no Rio Grande do Sul, Argentina e Uruguai"}),
    ("AS RELIGIÕES AFRICANAS NO RIO GRANDE DO SUL (BATUQUE)", 2019, "pernambuco-2019-batuque", ART, PR, ["batuque_rs"], "B", "texto de sacerdote do batuque publicado em periódico acadêmico (Debates do NER); visão de dentro, a cotejar com etnografias.", {"titulo": "As religiões africanas no Rio Grande do Sul (batuque)"}),
    ("Batuque jêje-ijexá em Porto Alegre", 1998, "braga-1998-batuque", LIV, AC, ["batuque_rs"], "B", "etnomusicologia do batuque; registro na Open Library e resenha em Horizontes Antropológicos (1999, DOI 10.1590/s0104-71831999000200014) confirmam a obra.", {"subtitulo": ": a música no culto aos orixás"}),
    ("NOTAS HISTÓRICAS E ANTROPOLÓGICAS SOBRE O BATUQUE", 2016, "tadvald-2016-batuque", ART, AC, ["batuque_rs"], "B", J_ART + ".", {"titulo": "Notas históricas e antropológicas sobre o batuque no Rio Grande do Sul"}),
    ("O atual campo afro-religioso gaúcho", 2012, "oro-2012-campo", ART, AC, ["batuque_rs", "umbanda"], "B", J_ART + " (Civitas); autor é referência no tema.", {}),
    ("Le tango des Orixàs", 2006, "muchnik-2006-tango", LIV, AC, ["batuque_rs", "umbanda"], "B", "livro derivado de tese de doutorado (theses.fr, 2004) sobre religiões afro-brasileiras em Buenos Aires.", {}),
    ("Expressões da devoção na Festa de Ogum em Bagé", 2019, "moura-2019-ogum-bage", ART, AC, ["umbanda"], "B", J_ART + " (PROA, Unicamp); tradição tirada do resumo (umbanda).", {}),
    # ---- Candomblé Angola / banto
    ("CANDOMBLÉ ANGOLA E O CULTO A CABOCLO", 2014, "mendes-2014-angola-caboclo", ART, AC, ["candomble_angola"], "B", J_ART + ".", {"titulo": "Candomblé angola e o culto a caboclo: de como João da Pedra Preta se tornou o rei nagô"}),
    ("Etude comparative de différentes nations de candomblé", 2001, "vatin-2001-nations", TES, TS, ["candomble_angola", "candomble_ketu", "candomble_jeje"], "B", J_TES + "; comparação explícita entre nações.", {}),
    ("o apagamento do candomblé angola nas políticas", 2019, "hass-2019-angola", ART, AC, ["candomble_angola"], "B", J_ART + " (Mouseion).", {}),
    ("Sobre sincretismo e pureza.  Uma perspectiva do candomblé angola", 2020, "lima-2020-angola", ART, AC, ["candomble_angola"], "B", J_ART + ".", {"titulo": "Sobre sincretismo e pureza: uma perspectiva do candomblé angola"}),
    ("Umbanda, Reinado e Candomblé de Angola: uma tríade Bantu", 2015, "santos-2015-triade-bantu", ART, AC, ["candomble_angola", "umbanda"], "B", J_ART + " (Horizonte, PUC Minas).", {}),
    # ---- Jeje / vodum
    ("Nascer vodunsi", 2026, "ferreira-2026-vodunsi", ART, AC, ["candomble_jeje"], "B", J_ART + " (ouvirOUver, UFU).", {}),
    ("The Jeje in the Tambor de Mina of Maranhão", 2001, "pares-2001-jeje", ART, AC, ["candomble_jeje", "tambor_de_mina"], "B", J_ART + " (Slavery & Abolition); autor é referência sobre a nação jeje.", {}),
    ("“Candomblé é a África”", 2016, "dias-2016-candomble-africa", ART, AC, ["candomble_jeje", "candomble_ketu"], "B", J_ART + " (Cadernos de História, PUC Minas).", {"titulo": "“Candomblé é a África”: esquecimento e utopia no candomblé jeje-nagô"}),
    ("Esclavage et inventions spirituelles afro-brésiliennes", 2015, "cerqueira-2015-lebabimibome", TES, TS, ["candomble_jeje"], "B", J_TES + ".", {}),
    ("Cohabitations et concurrences religieuses dans le Golfe de Guinée", 2002, "barbier-2002-golfe", ART, AC, ["vodun_benim"], "B", J_ART + ".", {}),
    ("Imaginaire national et mise en patrimoine dans l'Atlantique Sud", 2009, "tall-2009-patrimoine", ART, AC, ["candomble_ketu", "vodun_benim"], "B", J_ART + " (Lusotopie).", {}),
    ("Pierre Fatumbi Verger and the Study of", 2013, "brivio-2013-verger", ART, AC, ["vodun_benim", "ioruba_nigeria"], "B", J_ART + " (History in Africa); estudo sobre a obra de Verger.", {}),
    # ---- Exu / Legba / Elegguá
    ("Searching for Africa in Brazil: power and tradition in candomblé", 2010, "capone-2010-searching", LIV, AC, ["candomble_ketu", "umbanda"], "A", J_UP + " (Duke University Press); trata Exu no candomblé e na umbanda.", {}),
    ("A Carved Stone Figure of Eshu from Igbajo", 1964, "allison-1964-eshu", ART, AC, ["ioruba_nigeria"], "B", J_ART + " (Man, RAI).", {"titulo": "A Carved Stone Figure of Eshu from Igbajo, Western Nigeria"}),
    ("Alguns marcos na evolução histórica e situação atual de Exu na Umbanda", 1980, "costa-1980-exu-umbanda", ART, AC, ["umbanda"], "B", J_ART + " (Afro-Ásia).", {}),
    ("Worldview, the Orichas, and Santeria", 2007, "sandoval-2007-worldview", LIV, AC, ["lucumi", "ioruba_nigeria"], "B", J_UP + " (University Press of Florida); capítulos por orixá com DOI no Crossref.", {}),
    ("Eshu, ein Numen in der Vorstellungswelt der Yoruba", 1981, "zander-1981-eshu", LIV, AC, ["ioruba_nigeria"], "B", "monografia acadêmica (tese impressa) registrada na Open Library.", {}),
    ("Èșù Elegbára", 2012, "ogundipe-2012-esu", LIV, AC, ["ioruba_nigeria"], "B", "edição universitária (Kwara State University Press) da tese do autor sobre Èṣù (Indiana, 1978).", {}),
    ("Esu ma se mi o", 1997, "capone-1997-esu", TES, TS, ["candomble_ketu"], "B", J_TES + ".", {}),
    ("Exu, símbolo e função", 1985, "trindade-1985-simbolo", LIV, AC, ["umbanda"], "B", "publicação do Centro de Estudos da Religião (USP) por pesquisadora do tema.", {}),
    ("Exus e Pombas-Giras: o masculino e o feminino nos pontos cantados", 2001, "nascimento-2001-exus", ART, AC, ["umbanda"], "B", J_ART + " (Psicologia em Estudo); útil para a distinção Exu orixá × exus da umbanda.", {"titulo": "Exus e Pombas-Giras: o masculino e o feminino nos pontos cantados da umbanda"}),
    ("Frontières et altérités : Exu.", 2019, "pitta-2019-exu-recife", ART, AC, ["xango_pernambuco"], "B", J_ART + ". O título diz 'Candomblé de Recife'; a tradição xango_pernambuco é aproximação a conferir na leitura.", {}),
    ("III. Legba: Master of the Fon Dialectic", 1980, "pelton-1980-legba", CAP, AC, ["vodun_benim"], "B", J_CAP + ": cap. 3 de Robert D. Pelton, The Trickster in West Africa (University of California Press).", {"autores": ["Robert D. Pelton"], "titulo": "Legba: Master of the Fon Dialectic"}),
    ("Ifa and Eṣu", 1984, "witte-1984-ifa-esu", LIV, AC, ["ioruba_nigeria"], "B", "catálogo iconográfico de Hans Witte; registro na Open Library.", {}),
    ("Les Compagnons invisibles", 1991, "boyer-1991-compagnons", TES, TS, ["umbanda", "tambor_de_mina"], "B", J_TES + " (Umbanda e Mina em Belém).", {}),
    ("Na rua, no meio do redemoinho", 2022, "queiroz-2022-exu", ART, AC, ["candomble_ketu", "batuque_rs"], "B", J_ART + " (Religião e Sociedade); tradições tiradas do resumo, nação do candomblé não especificada.", {}),
    ("O enigma da quimbanda", 2021, "giumbelli-2021-quimbanda", ART, AC, ["umbanda"], "B", J_ART + " (Revista de Antropologia, USP).", {}),
    ("O self-service do proibido: a festa de exu", 2016, "campos-2016-exu-umbanda", ART, AC, ["umbanda"], "B", J_ART + " (Debates do NER).", {}),
    ("Orixá ou Diabo: a construção imagética de exu", 2021, "veiga-2021-exu", ART, AC, ["candomble_ketu", "umbanda"], "B", J_ART + " (Revista Calundu, UnB); tradições a confirmar na leitura.", {}),
    ("The Sculpture and Myths of Eshu-Elegba", 1962, "wescott-1962-eshu", ART, AC, ["ioruba_nigeria"], "A", J_ART + " (Africa, IAI); estudo clássico citado na literatura sobre Èṣù.", {}),
    ("Èṣù", 2014, "santos-2014-esu", LIV, AC, ["candomble_ketu", "ioruba_nigeria"], "A", "monografia de Juana Elbein dos Santos e Deoscóredes M. dos Santos (Corrupio), autores de referência sobre Exu.", {"tipo_base": "book", "autores": ["Juana Elbein dos Santos", "Deoscóredes Maximiliano dos Santos"]}),
    ("Le concept du héros imprévisible", 2011, "vallier-2011-esu", ART, AC, ["ioruba_nigeria", "vodun_benim"], "B", J_ART + " (Cahiers d'études africaines).", {}),
    ("Santos parados", 2019, "toutain-2019-santos", TES, TS, ["lucumi"], "B", J_TES + ".", {}),
    ("Eshu-Elegba: The Yoruba Trickster God", 1975, "pemberton-1975-eshu", ART, AC, ["ioruba_nigeria"], "A", J_ART + " (African Arts); estudo clássico.", {}),
    ("Èṣù and ethics in the Yorùbá world view", 2020, "oyelaran-2020-esu", ART, AC, ["ioruba_nigeria"], "B", J_ART + " (Africa, Cambridge).", {}),
    # ---- geral / orixás
    ("women and the proliferation and merging of", 1990, "barber-1990-proliferation", ART, AC, ["ioruba_nigeria"], "A", J_ART + " (Africa); sustenta a variação local do panteão iorubá.", {"titulo": "Oríkì, women and the proliferation and merging of òrìṣà"}),
    ("primeira ialorixá do Terreiro da Nação Xambá", 2023, "santana-2023-xamba", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Educação & Formação, UECE).", {}),
    ("Deuses africanos no Brasil contemporâneo", None, "prandi-1995-deuses", ART, AC, ["candomble_ketu", "umbanda"], "A", J_ART + " (Horizontes Antropológicos); autor de referência. A DOAJ data o registro em 2026, mas o identificador SciELO (S0104-71831995…) indica 1995.", {"ano": 1995}),
    ("Fazendo orixás", 2018, "marques-2018-fazendo", ART, AC, ["candomble_ketu"], "B", J_ART + " (Religião & Sociedade). Nação do candomblé não especificada nos metadados (aproximação).", {}),
    ("La Force et la douceur de la force", 1986, "silveira-1986-force", TES, TS, ["candomble_ketu"], "B", J_TES + ".", {}),
    ("Orisha Religion", 2024, "houk-2024-orisha", CAP, AC, ["orisha_trinidad"], "B", J_CAP + " (The Oxford Handbook of Caribbean Religions).", {"autores": ["James Houk"]}),
    ("Sacred Leaves of Candomblé", 1997, "voeks-1997-sacred", LIV, AC, ["candomble_ketu"], "A", J_UP + " (University of Texas Press).", {"autores": ["Robert A. Voeks"], "titulo": "Sacred Leaves of Candomblé: African Magic, Medicine, and Religion in Brazil"}),
    ("Yorùbá Beadwork in the Americas", 1998, "mason-1998-beadwork", ART, AC, ["lucumi", "ioruba_nigeria"], "B", J_ART + " (African Arts); trata cores de contas por orixá.", {"titulo": "Yorùbá Beadwork in the Americas: Òrìṣà and Bead Color"}),
    ("La Religion des orisha", 2011, "capone-2011-religion", LIV, AC, ["lucumi"], "B", J_UP + " (Hermann).", {}),
    ("Dans l'intimité des orixás", 2005, "halloy-2005-intimite", TES, TS, ["xango_pernambuco"], "B", J_TES + "; etnografia de uma família de santo do Xangô do Recife.", {}),
    # ---- Iemanjá
    ("A vida privada de Iemanjá e seus filhos", 1988, "segato-1988-iemanja", DOC, AC, ["xango_pernambuco"], "B", "texto da Série Antropologia (UnB) de pesquisadora do Xangô do Recife; registro na Open Library.", {}),
    ("Cristo, Bíblia e Iemanjá", 2024, "giumbelli-2024-monumentos", ART, AC, ["umbanda", "candomble_ketu"], "B", J_ART + " (Religião e Sociedade). Tradições a confirmar na leitura.", {}),
    ("an appraisal of Yemoja among the Yoruba in Nigeria", 2015, "ogunleye-2015-yemoja", ART, AC, ["ioruba_nigeria"], "B", J_ART + " (Inkanyiso).", {}),
    ("Encruzilhadas do Mercosul", 2025, "noleto-2025-montevideu", ART, AC, ["umbanda"], "B", J_ART + " (Religião & Sociedade). Tradição a confirmar na leitura.", {}),
    ("Festa de Iemanjá", 2011, "pordeus-2011-festa", LIV, AC, ["umbanda"], "B", "publicação do Museu do Ceará por antropólogo da UFC; tradição a confirmar.", {"tipo_base": "book"}),
    ("Sacred Pathway, Devotional Praxis", 2023, "niell-2023-regla", ART, AC, ["lucumi"], "B", J_ART + " (Religions, MDPI).", {}),
    ("New Lucumí from Ọ̀yọ́", 2019, "lovejoy-2019-lucumi", CAP, AC, ["lucumi", "ioruba_nigeria"], "B", J_CAP + ": cap. de Henry B. Lovejoy, Prieto: Yorùbá Kingship in Colonial Cuba (University of North Carolina Press).", {}),
    ("Trinidad Orisha Opens the Road", 2013, "castor-2013-trinidad", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Cultural Anthropology).", {"titulo": "Shifting Multicultural Citizenship: Trinidad Orisha Opens the Road"}),
    ("Nas águas de Ọ̀ṣun e Yemọja", 2026, "carneiro-2026-osun-yemoja", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Revista de Antropologia da UFSCar); o subtítulo no Crossref indica Xangô do Recife.", {}),
    # ---- Lucumí / Santería
    ("The artistry of Afro-Cuban batá drumming", 2013, "schweitzer-2013-bata", LIV, AC, ["lucumi"], "B", J_UP + " (University Press of Mississippi).", {}),
    ("2 The Orisha Tradition in Cuba: Santería/Regla de Ocha", 2022, "fernandez-olmos-2022-orisha-cuba", CAP, AC, ["lucumi"], "B", J_CAP + ": cap. 2 de Margarite Fernández Olmos e Lizabeth Paravisini-Gebert, Creole Religions of the Caribbean, 3ª ed. (New York University Press).", {"autores": ["Margarite Fernández Olmos", "Lizabeth Paravisini-Gebert"], "titulo": "The Orisha Tradition in Cuba: Santería/Regla de Ocha", "doi_exato": "10.18574/nyu/9781479803538.003.0009"}),
    ("Bamboxê Obitikô e a expansão do culto aos orixás", 2016, "castillo-2016-bamboxe", ART, AC, ["candomble_ketu", "ioruba_nigeria"], "B", J_ART + " (Tempo, UFF).", {}),
    ("Cooking for the gods", 2011, "perez-2011-cooking", ART, AC, ["lucumi"], "B", J_ART + " (Religion).", {}),
    ("Des dieux et des signes", 2000, "dianteill-2000-dieux", LIV, AC, ["lucumi"], "A", J_UP + " (Éditions de l'EHESS).", {}),
    ("Les Trois visages de l'Oricha", 1997, "dianteill-1997-oricha", ART, AC, ["lucumi"], "B", J_ART + " (Archives de sciences sociales des religions).", {}),
    ("Ifa divination, knowledge, power, and performance", 2016, "olupona-abiodun-2016-ifa", LIV, AC, ["ioruba_nigeria"], "A", J_UP + " (Indiana University Press).", {"autores": ["Jacob K. Olupona", "Rowland O. Abiodun"]}),
    ("La conquête de l’est", 2006, "testa-2006-santeria", TES, TS, ["lucumi"], "B", J_TES + ".", {}),
    ("Ramas, familles, réseaux", 2005, "argyriadis-2005-ramas", ART, AC, ["lucumi"], "B", J_ART + " (Journal de la Société des américanistes).", {}),
    ("La santería en Cuba", 1993, "linares-1993-santeria", ART, AC, ["lucumi"], "B", J_ART + " (Gazeta de Antropología); autora é etnomusicóloga cubana.", {}),
    ("Las celebraciones rituales festivas en la regla de Ocha", 2003, "balbuena-2003-celebraciones", LIV, AC, ["lucumi"], "B", "publicação do CIDMUC (Havana), centro de pesquisa musical cubano.", {}),
    ("Los sistemas adivinatorios de la Regla Ocha", 1997, "arguelles-1997-sistemas", LIV, AC, ["lucumi"], "B", "Editorial Academia (Havana); autor pesquisador cubano.", {}),
    ("Necklaces Used in the Santería of Cuba", 2005, "dominguez-2005-necklaces", ART, AC, ["lucumi"], "B", J_ART + " (BEADS); cores de colares por oricha.", {}),
    ("Opolopo owó", 1994, "bolivar-1994-opolopo", LIV, AC, ["lucumi"], "B", "Editorial de Ciencias Sociales (Havana); autora de referência (Bolívar, Los orishas en Cuba).", {}),
    ("Sacred possessions", 1997, "fernandez-olmos-1997-sacred", LIV, AC, ["lucumi", "vodou_haiti"], "A", J_UP + " (Rutgers University Press).", {"autores": ["Margarite Fernández Olmos", "Lizabeth Paravisini-Gebert"]}),
    ("Santería und ihre Globalisierung in Kuba", 2012, "rauhut-2012-santeria", LIV, AC, ["lucumi"], "B", J_UP + " (Ergon); tese publicada.", {}),
    ("Un complexe sacerdotal cubain", 2012, "gobin-2012-complexe", TES, TS, ["lucumi"], "B", J_TES + ".", {}),
    # ---- Ogum
    ("Domingo 23 é Dia de Jorge", 2019, "campos-2019-jorge", ART, AC, ["umbanda"], "B", J_ART + " (PROA, Unicamp).", {}),
    ("Foi lá no Candeal que plantei a minha mata", 2022, "castillo-2022-ogum", ART, AC, ["candomble_ketu"], "B", J_ART + " (Revista de História, USP); história de um culto familiar a Ogum em Salvador.", {}),
    ("O sacrifício do boi para Ogum", 2010, "ramos-2010-boi", ART, AC, ["candomble_ketu"], "B", J_ART + " (Resgate, Unicamp). Nação não especificada nos metadados.", {}),
    ("orixá desaparecido:", 2021, "fontes-2021-orixa-desaparecido", ART, AC, ["candomble_ketu"], "B", J_ART + " (Afro-Ásia). Nação a confirmar.", {"titulo": "Orixá desaparecido: descobertas através de um museu silencioso"}),
    ("The Many and Changing Faces of Ògún", 2012, "poynor-2012-ogun", ART, AC, ["ioruba_nigeria"], "B", J_ART + " (Nova Religio).", {}),
    # ---- Orisha de Trinidad
    ("African \"Powers\" in Trinidad: The Shango Cult", 1957, "mischel-1957-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Anthropological Quarterly).", {}),
    ("Ethnic Distance and Religious Convergence", 1998, "vertovec-1998-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Social Compass).", {}),
    ("He had the power", 2008, "henry-2008-power", LIV, AC, ["orisha_trinidad"], "B", "biografia de um líder do Orisha de Trinidad por antropóloga de referência (Frances Henry).", {}),
    ("Obeah, Orisa, and Religious Identity in Trinidad", 2022, "stewart-2022-orisa", LIV, AC, ["orisha_trinidad"], "A", J_UP + " (Duke University Press).", {}),
    ("Orisa (Orisha) Tradition in Trinidad", 1999, "aiyejina-1999-orisa", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Caribbean Quarterly).", {}),
    ("Praising his name in the dance", 2000, "lum-2000-praising", LIV, AC, ["orisha_trinidad"], "B", J_UP + " (Harwood/Taylor & Francis).", {}),
    ("Reflections on the Children of Shango", 2007, "trotman-2007-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Slavery & Abolition).", {}),
    ("Religion and Ideology in Trinidad", 1983, "henry-1983-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Caribbean Quarterly).", {}),
    ("Spiritual Citizenship", 2017, "castor-2017-spiritual", LIV, AC, ["orisha_trinidad"], "B", J_UP + " (Duke University Press).", {}),
    ("The Shango Cult and Other African Rituals in Trinidad", 1993, "pollak-eltz-1993-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Caribbean Quarterly).", {}),
    ("The Shango Cult in Nigeria and in Trinidad", 1962, "simpson-1962-shango", ART, AC, ["orisha_trinidad", "ioruba_nigeria"], "B", J_ART + " (American Anthropologist).", {"titulo": "The Shango Cult in Nigeria and in Trinidad"}),
    ("The Yoruba and Orisha Worship in Trinidad and British Guinea", 1976, "trotman-1976-yoruba", ART, AC, ["orisha_trinidad"], "B", J_ART + " (African Studies Review).", {}),
    ("The shango cult in Trinidad", 1965, "simpson-1965-shango", LIV, AC, ["orisha_trinidad"], "A", "monografia clássica (Institute of Caribbean Studies, Universidade de Porto Rico); registro na Open Library.", {}),
    ("When Field Recordings Meet Field Research", 2017, "bazinet-2017-shango", ART, AC, ["orisha_trinidad"], "B", J_ART + " (Ethnomusicology).", {}),
    # ---- Oxóssi
    ("“IMPRESSÕES” DE MÃE STELLA DE OXÓSSI", 2016, "santos-ms-2016-impressoes", ART, PR, ["candomble_ketu"], "B", "texto da iyalorixá do Ilê Axé Opô Afonjá em periódico da UnB; voz de praticante.", {"autores": ["Maria Stella de Azevedo Santos (Mãe Stella de Oxóssi)"], "titulo": "“Impressões” de Mãe Stella de Oxóssi, Iya Odé Kayode, 5ª iyalorixá do Ilê Axé Opô Afonjá, sobre o Atlas Geográfico África-Brasil de autoria do geógrafo Rafael Sanzio dos Anjos"}),
    ("Òsósi: o caçador de alegrias", 2006, "santos-ms-2006-ososi", LIV, PR, ["candomble_ketu"], "B", "livro da iyalorixá do Ilê Axé Opô Afonjá sobre Oxóssi; obra de praticante.", {"autores": ["Maria Stella de Azevedo Santos (Mãe Stella de Oxóssi)"]}),
    ("Oxossi, o caçador", 1981, "verger-1981-oxossi", LIV, AC, ["candomble_ketu", "ioruba_nigeria"], "A", "obra de Pierre Verger (Corrupio); registro na Open Library.", {}),
    # ---- Tambor de Mina
    ("A CASA DAS MINAS DE SÃO LUÍS DO MARANHÃO E A SAGA DE NÃ AGONTIMÉ", 2019, "cavalcanti-2019-casa-minas", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Sociologia & Antropologia).", {"titulo": "A Casa das Minas de São Luís do Maranhão e a saga de Nã Agontimé"}),
    ("TAMBOR DE MINA E PAJELANÇA NO MARANHÃO", 2019, "almeida-2019-mina", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Projeto História, PUC-SP).", {"titulo": "Ao ritmo de tambores e maracás: tambor de mina e pajelança no Maranhão de meados do século XX"}),
    ("Brinquedo de Cura em terreiro de Mina", 2014, "ferretti-m-2014-brinquedo", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Revista do IEB, USP); autora é referência no tema.", {}),
    ("Comida ritual em festas de Tambor de Mina", 2011, "ferretti-2011-comida", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Horizonte, PUC Minas); acesso aberto pelo DOAJ, contornando o bloqueio do Dialnet.", {"titulo": "Comida ritual em festas de Tambor de Mina no Maranhão"}),
    ("De vodum a caboclo: Trajetória de legbá", 2017, "ferreira-2017-legba", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Revista Calundu, UnB); Legba na Mina e no Terecô.", {}),
    ("Desceu na guma", 1993, "ferretti-m-1993-guma", LIV, AC, ["tambor_de_mina"], "A", "monografia de Mundicarmo Ferretti (SIOGE, São Luís), referência sobre o caboclo no Tambor de Mina.", {}),
    ("Festa de Acossi e o arrambã", 1996, "ferretti-1996-acossi", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Horizontes Antropológicos).", {}),
    ("Pureza nagô e nações africanas no tambor de Mina", 2020, "ferretti-m-2020-pureza", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Ciencias Sociales y Religión).", {}),
    ("Repensando o sincretismo", 1995, "ferretti-1995-sincretismo", LIV, AC, ["tambor_de_mina"], "A", J_UP + " (Edusp/FAPEMA); estudo da Casa das Minas.", {}),
    ("Repensando o turco no tambor de mina", 1992, "ferretti-m-1992-turco", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Afro-Ásia).", {}),
    ("Sincretismo afro-brasileiro e resistência cultural", 1998, "ferretti-1998-sincretismo", ART, AC, ["tambor_de_mina"], "B", J_ART + " (Horizontes Antropológicos).", {}),
    # ---- Xangô / Xangô de Pernambuco
    ("A fogueira de Xangô", 1999, "barros-1999-fogueira", LIV, AC, ["candomble_ketu"], "B", "publicação acadêmica (Intercon/UERJ) de José Flávio Pessoa de Barros, pesquisador do candomblé.", {"titulo": "A fogueira de Xangô, o orixá do fogo"}),
    ("De Xangô a Candomblé: transformações no mundo afro-pernambucano", 2013, "pereira-2013-xango-candomble", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Horizonte, PUC Minas).", {"titulo": "De Xangô a Candomblé: transformações no mundo afro-pernambucano"}),
    ("Gods in the Flesh", 2012, "halloy-2012-gods", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Ethnos).", {}),
    ("On the Etymology of the Yoruba Theonym Shango", 2025, "capo-chichi-2025-shango", ART, AC, ["ioruba_nigeria"], "B", J_ART + " (Yoruba Studies Review); etimologia do nome.", {}),
    ("Os Obás de Xangô", 1966, "costa-lima-1966-obas", ART, AC, ["candomble_ketu"], "A", J_ART + " (Afro-Ásia); estudo clássico do Opô Afonjá.", {}),
    ("Sexo, Culpa, Sacrifício e Expiação no Xangô de Pernambuco", 2011, "motta-2011-sexo", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Esboços, UFSC).", {"titulo": "Sexo, culpa, sacrifício e expiação no Xangô de Pernambuco"}),
    ("Cantos sagrados do xangô do Recife", 1993, "carvalho-1993-cantos", LIV, AC, ["xango_pernambuco"], "A", "edição de cantos pelo etnomusicólogo José Jorge de Carvalho (Fundação Cultural Palmares).", {}),
    ("Família de santo em alguns terreiros de Xangô em Pernambuco", 2016, "mendonca-2016-familia", LIV, AC, ["xango_pernambuco"], "B", "editora universitária (EDUA, UFAM); registro na Open Library.", {}),
    ("Le Sacrifice Xangô à Recife", 2003, "motta-2003-sacrifice", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Social Compass).", {}),
    ("Marcas muçulmanas nos xangôs de Pernambuco", 1954, "valente-1954-marcas", LIV, AC, ["xango_pernambuco"], "A", "estudo clássico (Universidade do Recife); registro na Open Library.", {}),
    ("Mitos e símbolos nos xangôs de Pernambuco", 2011, "pitta-2011-mitos", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Cadernos de Estudos Sociais, Fundaj).", {}),
    ("O útil, o sagrado e o mais-que-sagrado no Xangô de Pernambuco", 1998, "motta-1998-util", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Horizontes Antropológicos).", {}),
    ("Si la tradition nagô m'était contée", 1997, "lacourse-1997-nago", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Anthropologie et Sociétés).", {}),
    ("Transe, sacrifício, comunhão e poder no Xangô de Pernambuco", 1991, "motta-1991-transe", ART, AC, ["xango_pernambuco"], "B", J_ART + " (Revista de Antropologia, USP).", {}),
    ("Xangô rezado baixo. Xambá tocando alto", 2013, "guerra-2013-xamba", LIV, AC, ["xango_pernambuco"], "B", "editora universitária (UFPE); registro na Open Library.", {"autores": ["Lucia Helena Barbosa Guerra"]}),
    ("Xangôs do Nordeste", 1937, "fernandes-1937-xangos", LIV, AC, ["xango_pernambuco"], "A", "estudo clássico (Civilização Brasileira, Biblioteca de Divulgação Científica); registro na Open Library.", {}),
]

PISTA = [
    ("\"Orixás, guardiões da ecologia\"", None, "silva-mb-orixas-ecologia", DIS, TS, ["batuque_rs"], "B", "dissertação USP sem ano no registro Crossref; ano e orientador a conferir.", {}),
    ("Nzo ia Nkis", None, "ferreira-ta-nzo-ia-nkisi", DIS, TS, ["candomble_angola"], "B", "dissertação UnB sem ano no registro; conferir no repositório.", {}),
    ("O cajado de Lemba", None, "machado-vs-cajado-lemba", DIS, TS, ["candomble_angola"], "B", "dissertação USP sobre o tempo no candomblé angola; ano a conferir.", {}),
    ("Candomblé de Angola", 1989, "costa-1989-angola", LIV, DV, ["candomble_angola"], "C", "livro de divulgação (Pallas); autoria e conteúdo a avaliar.", {"idioma": "pt"}),
    ("Dois de Fevereiro no Rio Vermelho", 2009, "porto-filho-2009-dois-fevereiro", LIV, DV, ["candomble_ketu"], "C", "memória local (Acirv); pode ajudar na divergência sobre a origem da festa (1923 ou c. 1910).", {}),
    ("Lucumí (Yoruba) Culture in Cuba", None, "ramos-m-lucumi-reevaluation", DIS, TS, ["lucumi"], "B", "dissertação (FIU) sem ano no registro; conferir.", {}),
    ("Ogum, o rei de muitas faces", 2000, "prandi-2000-ogum-faces", LIV, DV, ["candomble_ketu"], "C", "livro infantojuvenil de Reginaldo Prandi (Cia. das Letras); autor ausente no registro.", {"autores": ["Reginaldo Prandi"]}),
    ("O cabloco no \"Tambor de Mina\"", None, "ferretti-m-caboclo-dissertacao", DIS, TS, ["tambor_de_mina"], "B", "dissertação de Mundicarmo Ferretti (USP) sem ano no registro.", {}),
    ("Tambor de crioula et tambor de mina", None, "cousin-tambor-mina-these", TES, TS, ["tambor_de_mina"], "B", "tese (etnomusicologia) sem ano no registro; conferir em theses.fr.", {}),
    ("Xangô de Pernambuco", 2004, "lins-2004-xango-pe", LIV, DV, ["xango_pernambuco"], "C", "livro de divulgação (Pallas) sobre a tradição; autoria a avaliar.", {}),
    ("Nagô é lento!", None, "donatien-nago-lento", TES, TS, ["xango_pernambuco"], "B", "tese (etnomusicologia) sobre o xangô; ano a conferir.", {}),
    ("Echu-Elegguá", 1998, "souza-hernandez-1998-echu", LIV, DV, ["lucumi"], "C", "Ediciones Unión (Havana); obra de autor ligado à prática, a avaliar.", {}),
    ("História de Vida, Saberes e Apredizagens da Tradição de Candomblé de Angola", 2026, "nangetu-2026-angola", ART, PR, ["candomble_angola"], "C", "texto de mam'etu (sacerdotisa) em periódico; venue a avaliar.", {}),
    ("Candomblé", 1957, "medeiros-1957-candomble", LIV, DV, ["candomble_ketu"], "C", "fotorreportagem (O Cruzeiro) de valor histórico; não é fonte para atributos.", {"tipo_base": "book"}),
    ("A formação do candomblé e a Nação Jeje", 2007, "nascimento-2007-jeje", ART, AC, ["candomble_jeje"], "B", "Afro-Ásia; possivelmente resenha de Parés 2006 (DOI não respondeu na conferência).", {}),
    ("Representações sociais de voduns", 2025, "pereira-2025-voduns", ART, AC, ["candomble_jeje"], "C", "periódico pouco conhecido; avaliar antes de usar.", {}),
    ("Iemanjá em família", 2018, "segato-iemanja-familia", ART, AC, ["xango_pernambuco"], "B", "Anuário Antropológico (UnB); a DOAJ data 2018, provável digitalização de volume antigo; ano original a conferir.", {}),
]

DESCARTA = [
    ("Traços do Kimbundu numa casa de candomblé angola", None, "duplicata de barros-2000-kimbundu (dissertação já no catálogo)"),
    ("Exu do Brasil: tropos de uma identidade", 2013, "duplicata de silva-2012-exu-brasil"),
    ("Oh, mío Yemayá!!", 1938, "duplicata de lachatanere-1938-yemaya"),
    ("Yemoja", 2013, "duplicata de otero-falola-2013-yemoja"),
    ("OXÓSSI: O HERÓI DE UMA FLECHA SÓ", 2020, "duplicata de mosaico-2020-oxossi"),
    ("Querebentam de Zomadonu", 1985, "duplicata de ferretti-1985-querebenta"),
    ("Querebentan de zomandonu", 1986, "duplicata (reedição) de ferretti-1985-querebenta"),
    ("Spirits, Blood and Drums- The Orisha Religion", 2010, "reedição de houk-1995-spirits"),
    ("The Formation of Candomblé", 2013, "tradução inglesa de pares-2006-formacao (já no catálogo)"),
    ("Orixás", 1981, "edição francesa (Métailié) de verger-1981-orixas"),
    ("Afrokubanische Kulte", 2000, "tradução alemã de barnet-1995-cultos"),
    ("Iemanjá & Oxum", 2004, "tradução brasileira de cabrera-1974-yemaya"),
    ("Brésil: candomblé de Angola. Musique rituelle", 2000, "provável resenha de disco (Cahiers de musiques traditionnelles)"),
    ("Le tango des Orixás : sociologie", 2004, "tese já representada pelo livro muchnik-2006-tango"),
]


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
                # vários registros do mesmo trabalho: prefere o que tem DOI, depois o de mais bases
                m = sorted(m, key=lambda c: (not c.get("doi"), -len(c["bases"])))
                if not m:
                    erros.append(f"{fid}: '{trecho}' ({ano}) não encontrado")
                    continue
            fonte = {"id": fid, "tipo": tipo, "categoria": cat, "tradicoes": trad, "confiabilidade_preliminar": nivel}
            for k in ("titulo", "autores", "ano", "idioma"):
                if k in extra:
                    fonte[k] = extra[k]
            if "subtitulo" in extra:
                fonte["titulo"] = m[0]["titulo"] + extra["subtitulo"]
            dec[m[0]["chave"]] = {"decisao": decisao, "motivo": None, "fonte": fonte, "justificativa": just}
    # idioma corrigido à mão quando a detecção pelo título erra (ex.: "de"/"em" pt × es)
    IDIOMA_FIX = {"ferretti-m-2014-brinquedo": "pt", "ferreira-2017-legba": "pt", "campos-2019-jorge": "pt",
                  "santos-2014-esu": "pt", "houk-2024-orisha": "en", "cousin-tambor-mina-these": "fr"}
    for d in dec.values():
        if d["fonte"]["id"] in IDIOMA_FIX:
            d["fonte"]["idioma"] = IDIOMA_FIX[d["fonte"]["id"]]
    for trecho, ano, motivo in DESCARTA:
        if motivo is None:
            continue
        for c in achar(cs, trecho, ano):
            dec.setdefault(c["chave"], {"decisao": "descarta", "motivo": motivo})

    # Conferência de fontes já catalogadas (a_verificar/pista) com registro forte na coleta
    ja = cand["ja_no_catalogo"]
    CONF = {
        "carybe-1980-iconografia": ("Iconografia dos deuses africanos", 1980, None),
        "prandi-2005-segredos": ("Segredos guardados", 2005, None),
        "silva-1994-candomble-umbanda": ("Candomblé e umbanda", 1994, None),
        "matory-2005-black": ("Black Atlantic religion", 2005, None),
        "brown-dh-2003-santeria": ("Santería enthroned", 2003, None),
        "henry-2003-reclaiming": ("Reclaiming African religions in Trinidad", 2003, None),
        "houk-1995-spirits": ("Spirits, blood, and drums", 1995, None),
        "seyfeli-kul-2020-orisha": ("GELENEKSEL YORUBA", 2020, "Título no Crossref em turco e inglês."),
    }
    for fid, (trecho, ano, nota) in CONF.items():
        m = [c for c in ja if n(trecho) in n(c["titulo"]) and c["ano"] == ano and fid in c["catalogo"]]
        if not m:
            erros.append(f"conferência {fid}: não encontrado")
            continue
        conf[fid] = {"chave": m[0]["chave"], "nota": nota}
    CONF_CAND = {
        "falola-genova-2005-orisa": ("ORISA: Yoruba Gods and Spiritual Identity", 2005, None, True),
        "cabrera-1954-monte": ("El monte, igbo, finda, ewe orisha, vititi nfinda: notas", 1954, "Open Library registra Ediciones C. R., Havana, 1954; reedições de 1971 e 1975 (Ediciones Universal).", True),
        "cabrera-1974-yemaya": ("Yemayá y Ochún", 1980, "Open Library registra a edição de 1980 (Ediciones Universal); a 1ª edição (1974) não aparece no registro; ano citado mantido.", False),
    }
    for fid, (trecho, ano, nota, isbn) in CONF_CAND.items():
        m = achar(cs, trecho, ano)
        if not m:
            erros.append(f"conferência {fid}: não encontrado")
            continue
        conf[fid] = {"chave": m[0]["chave"], "nota": nota, "isbn": isbn}
        dec[m[0]["chave"]] = {"decisao": "descarta", "motivo": f"já no catálogo como {fid} (usado para conferência)"}

    saida = {"_meta": {"descricao": "Decisões da triagem da varredura nº 3, geradas por scripts/coleta/triagem_2026-10-31.py. Aplicar com scripts/coleta/incorporar.py.",
                       "data": "2026-10-31"},
             "decisoes": dec, "conferencias": conf}
    (PASTA / "triagem.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    print(Counter(d["decisao"] for d in dec.values()), "conferências:", len(conf))
    for e in erros:
        print("ERRO", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
