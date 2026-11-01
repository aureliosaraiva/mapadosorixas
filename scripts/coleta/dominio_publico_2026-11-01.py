#!/usr/bin/env python3
"""Varredura nº 4 (2026-11-01): obras em domínio público com texto integral e
correções manuais dos registros incorporados da coleta por API.

Domínio público conferido em 2026-11-01 por: (a) metadados do Internet Archive
(`archive.org/metadata/<id>`: item livre, sem `access-restricted-item`, com
`_djvu.txt` baixável; `possible-copyright-status`); (b) API de catálogo do
HathiTrust (`catalog.hathitrust.org/api/volumes/brief/oclc/<n>.json`:
`rightsCode` pd/pdus = Full view); (c) data de morte do autor (Brasil: 70 anos
após a morte; Espanha: 80 anos para autores mortos antes de 1987).
As obras de viajantes, missionários e administradores coloniais ficam com
confiabilidade C e aviso de olhar colonial/missionário: valem como documento
histórico, não como descrição neutra.

Idempotente. Uso: python3 scripts/coleta/dominio_publico_2026-11-01.py
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CATALOGO = RAIZ / "data" / "fontes" / "catalogo.json"
ORDEM = ["id", "tipo", "categoria", "autores", "titulo", "ano", "idioma", "tradicoes",
         "confiabilidade_preliminar", "observacoes", "status_verificacao", "evidencias", "url",
         "identificadores", "periodico", "editora", "local"]
IA = "https://archive.org/details/"
HT = "https://catalog.hathitrust.org/api/volumes/brief/oclc/"
COL = "Olhar colonial/missionário: documento histórico (confiabilidade C), não descrição neutra; usar só com crítica e cotejo com fontes atuais."
TAG = "Varredura 4 (2026-11-01)"

# Atualizações de fontes já catalogadas: (id, url do texto integral, evidências novas, nota)
ATUALIZA = [
    ("ellis-1894-yoruba", IA + "yorubaspeakingp00elligoog", [HT + "4848837.json"],
     "Texto integral no Internet Archive (NOT_IN_COPYRIGHT) e HathiTrust (hvd.32044020314415, pd). Cobre: cap. II 'Chief gods' (pp. 34–69, seções numeradas: Olorun, Obatala, Odudua, Orungan/Yemaja, Shango, Ifa com os 16 odù 'meji', Elegba); cap. III 'Minor gods' (pp. 70–84: Olokun, Olosa, Shigidi, Dada, Oshun, Oya, Orisha Oko, Osanyin, Aroni, Aja, Ibeji, Oshumare etc.); cap. VI Egungun e Oro (p. 107); cap. VII almas (p. 125); cap. XIV contos (p. 243)."),
    ("johnson-1921-history", IA + "historyofyorubas00john", [HT + "3499148.json"],
     "Texto integral no Internet Archive e HathiTrust (inu.39000005818294, pd). Autor morto em 1901, editor (Obadiah Johnson) em 1920: domínio público. Cobre: parte I, cap. III 'Religion' (pp. 26–39); parte II, cap. I (pp. 143–152: Oduduwa, Oranyan, Sango como rei de Oyó) — leitura histórica de Oyó, não teologia."),
    ("frobenius-1912-afrika", IA + "undafrikasprachb00frob", [],
     "Texto integral (alemão) no Internet Archive (Univ. de Toronto). Autor morto em 1938: domínio público na UE (inclusive Espanha, desde 2019). Tradução inglesa catalogada à parte (frobenius-1913-voice). " + COL),
    ("bowen-1857-adventures", IA + "centralafricaadv00bowe_0", [],
     "Texto integral no Internet Archive (ed. 1857, Getty). Pouco sobre orixás (menções a Ifá, Xangô, Ogum, Oro, Egungun); a reedição de 1969 (Cass) no IA é só empréstimo. " + COL),
    ("burton-1863-abeokuta", IA + "abeokutaandcama00burtgoog", [HT + "2054549.json", IA + "abeokutaandcama02burtgoog"],
     "Texto integral dos 2 volumes no Internet Archive (NOT_IN_COPYRIGHT) e HathiTrust (mdp.39015048914579, pd). Menções esparsas a Ifá, Xangô, Obatalá, Oro e ao rio Ogum (muitas ocorrências de 'Ogun' são o rio). " + COL),
    ("baudin-1884-fetichisme", None, ["https://openlibrary.org/works/OL6848551W"],
     "Original francês sem cópia acessível neste ambiente (Gallica 403; não achado no Internet Archive). A tradução inglesa de 1885 tem texto integral aberto: baudin-1885-fetichism."),
    ("nina-rodrigues-1900-animisme", "https://babel.hathitrust.org/cgi/pt?id=coo.31924020011759", [HT + "14780382.json"],
     "Texto integral no HathiTrust (coo.31924020011759, pd, Full view); o leitor do HathiTrust tem desafio anti-robô neste ambiente. Edição portuguesa de 1935 com texto aberto no Internet Archive: nina-rodrigues-1935-animismo."),
    ("nina-rodrigues-1932-africanos", IA + "osafricanosnobrasil", [],
     "Texto integral no Internet Archive (o _djvu.txt deu HTTP 500 em 2026-11-01; tentar de novo ou baixar o PDF). Texto de Nina Rodrigues (m. 1906) em domínio público; revisão e prefácio de Homero Pires (m. 1962) ainda protegidos. Cobre o cap. sobre sobrevivências religiosas (orixás iorubás, voduns jejes, culto malê)."),
]

NOVAS = [
    {"id": "frobenius-1913-voice", "tipo": "livro", "categoria": "etno_classica", "autores": ["Leo Frobenius"],
     "titulo": "The Voice of Africa: Being an Account of the Travels of the German Inner African Exploration Expedition in the Years 1910–1912",
     "ano": 1913, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Tradução inglesa (Rudolf Blind) de frobenius-1912-afrika; 2 vols., Londres, Hutchinson, 1913. Texto integral no Internet Archive (Univ. de Toronto, NOT_IN_COPYRIGHT). Cobre, no vol. I: cap. X 'The Foundations of the Yorubans' Religious Life' (p. 186), XI 'The Kingly Thunder-God' (Xangô, p. 204), XII 'The Idea of the World' (p. 228: Ifá, odù), XIII 'The Holy City' (Ifẹ̀, p. 265), XIV achados arqueológicos (cabeça de Olokun, p. 292); a tese da 'Atlântida' iorubá é especulação descartada. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "voiceofafricabei01frobuoft", IA + "voiceofafricabei02frobuoft", "https://openlibrary.org/works/OL10610669W"],
     "url": IA + "voiceofafricabei01frobuoft", "identificadores": {}, "editora": "Hutchinson", "local": "Londres"},
    {"id": "farrow-1926-faith", "tipo": "livro", "categoria": "etno_classica", "autores": ["Stephen Septimus Farrow"],
     "titulo": "Faith, Fancies and Fetich, or Yoruba Paganism: Being Some Account of the Religious Beliefs of the West African Negroes, Particularly of the Yoruba Tribes of Southern Nigeria",
     "ano": 1926, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Tese de doutorado (Edimburgo, 1924) de missionário anglicano; declara o objetivo de justificar a missão cristã. Texto integral no Internet Archive e HathiTrust (pd, Full view; domínio público nos EUA desde 2022; data de morte do autor a conferir para a Europa). Cobre: o Ser Supremo (Olorun), 'The Orishas' (2 caps.: Obatala, Odudua, Shango, Oya, Ogun, Eshu, Ifa/Orunmila, Yemaja, Olokun, Oshun, Sopono, Osanyin, Ibeji), espíritos dos mortos (Egungun, Oro), hino religioso iorubá (apêndice A). " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "faithfanciesfeti00farr", HT + "374675.json", "https://openlibrary.org/works/OL6922169W"],
     "url": IA + "faithfanciesfeti00farr", "identificadores": {"oclc": "374675"}, "editora": "Society for Promoting Christian Knowledge", "local": "Londres"},
    {"id": "dennett-1910-nigerian", "tipo": "livro", "categoria": "etno_classica", "autores": ["Richard Edward Dennett"],
     "titulo": "Nigerian Studies; or, The Religious and Political System of the Yoruba",
     "ano": 1910, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Administrador colonial (m. 1921): domínio público. Texto integral no Internet Archive (Toronto e Cornell) e HathiTrust (mdp.39015019369126, pd). Sumário: II criação e pedras sagradas de Ifẹ̀ (p. 17); III morte, Oro, Egungun (p. 28); V Jakuta (p. 65); VI Odudua (p. 73); VII Obatala (p. 81); VIII Ifá (p. 86); IX Eshu (p. 94); X Aganju, Yemoja e seus filhos (p. 97); XI Olokun, Olosa (p. 106); XII Ogun, Oshowsi e o caçador (p. 116); XIV Oke, Ojo, Ajeshaluga e a agricultura (p. 140); XV odù de Ifá (p. 147); XVI Shango, Oya, Oba, Oshun (p. 156). Esquema interpretativo próprio (quaternidades) sem base nas fontes atuais. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "nigerianstudieso00dennuoft", IA + "cu31924028648776", HT + "1321239.json"],
     "url": IA + "nigerianstudieso00dennuoft", "identificadores": {"oclc": "1321239"}, "editora": "Macmillan", "local": "Londres"},
    {"id": "dennett-1906-back", "tipo": "livro", "categoria": "etno_classica", "autores": ["Richard Edward Dennett"],
     "titulo": "At the Back of the Black Man's Mind; or, Notes on the Kingly Office in West Africa",
     "ano": 1906, "idioma": "en", "tradicoes": ["kongo"], "confiabilidade_preliminar": "C",
     "observacoes": "Domínio público (autor m. 1921). Texto integral no Internet Archive (Toronto, Cornell). Trata sobretudo dos Bavili de Loango (Kongo: nkisi, Nzambi, caps. I–XVI) e dos Bini/Edo (caps. XVII–XXI); quase nada sobre orixás iorubás. Útil para inquices/cosmologia banta, não para os orixás. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "atbackofblackman00dennuoft", IA + "cu31924029887472"],
     "url": IA + "atbackofblackman00dennuoft", "identificadores": {}, "editora": "Macmillan", "local": "Londres"},
    {"id": "baudin-1885-fetichism", "tipo": "livro", "categoria": "etno_classica", "autores": ["R. P. Baudin"],
     "titulo": "Fetichism and Fetich Worshipers",
     "ano": 1885, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Tradução inglesa (Nova York, Benziger, 1885) de baudin-1884-fetichisme. Texto integral no Internet Archive (NYPL, NOT_IN_COPYRIGHT) e HathiTrust (pd). Parte I: deuses 'superiores' (1. Obatala, 2. Odudua, 3. Ifa), 'semideuses' e 'gênios'; menciona Shango, Oya, Elegba, Olokun, Ibeji, Oro e Egungun. Interpretação cristã que demoniza Exu (ver Prandi 2001). " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "fetichismfetichw00baud", HT + "2768472.json", "https://openlibrary.org/works/OL6848551W"],
     "url": IA + "fetichismfetichw00baud", "identificadores": {"oclc": "2768472"}, "editora": "Benziger Brothers", "local": "Nova York"},
    {"id": "nina-rodrigues-1935-animismo", "tipo": "livro", "categoria": "etno_classica", "autores": ["Raimundo Nina Rodrigues"],
     "titulo": "O animismo fetichista dos negros baianos",
     "ano": 1935, "idioma": "pt", "tradicoes": ["candomble_ketu"], "confiabilidade_preliminar": "C",
     "observacoes": "1ª edição em livro em português (Civilização Brasileira, Biblioteca de Divulgação Científica, v. 2), com prefácio e notas de Arthur Ramos. Texto integral no Internet Archive. Domínio público no Brasil (Nina Rodrigues m. 1906; Ramos m. 1949, 70 anos); na Espanha as notas de Ramos só caem em 2030 (80 anos). HathiTrust marca a edição como 'ic' nos EUA. Cobre terreiros de Salvador na década de 1890: Olorun, Obatalá/Oxalá, Xangô, Ogum, Oxóssi (Odé), Iemanjá ('Yê-man-já'), Exu/Elegbá, Ifá, Dadá, possessão e iniciação. Viés racialista/evolucionista do autor. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "animismofetichista", HT + "2923361.json", "https://openlibrary.org/works/OL22815561W"],
     "url": IA + "animismofetichista", "identificadores": {"oclc": "2923361"}, "editora": "Civilização Brasileira", "local": "Rio de Janeiro"},
    {"id": "ellis-1890-ewe", "tipo": "livro", "categoria": "etno_classica", "autores": ["A. B. Ellis"],
     "titulo": "The Ewe-Speaking Peoples of the Slave Coast of West Africa: Their Religion, Manners, Customs, Laws, Languages, etc.",
     "ano": 1890, "idioma": "en", "tradicoes": ["vodun_benim"], "confiabilidade_preliminar": "C",
     "observacoes": "Domínio público (autor m. 1894). Texto integral no Internet Archive e HathiTrust (hvd.32044043302934, pd). Caps. III–V: divindades gerais, tribais e locais dos ewe/fon (Legba, Sapata, Khebioso/So etc.): base para voduns equivalentes. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "ewespeakingpeopl0000abel", HT + "25946296.json", "https://openlibrary.org/works/OL6254631W"],
     "url": IA + "ewespeakingpeopl0000abel", "identificadores": {}, "editora": "Chapman and Hall", "local": "Londres"},
    {"id": "bouche-1885-cote", "tipo": "livro", "categoria": "etno_classica", "autores": ["Pierre Bouche"],
     "titulo": "La Côte des Esclaves et le Dahomey",
     "ano": 1885, "idioma": "fr", "tradicoes": ["vodun_benim", "ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Padre da Sociedade das Missões Africanas de Lyon; Paris, Plon, 1885. Domínio público. Texto integral no Internet Archive (Univ. de Toronto/Ottawa). Cap. VII 'État religieux' (p. 101), XII contos nagôs (p. 221), XIII provérbios (p. 239), XXIII particularidades religiosas do Daomé (p. 365); menciona Xangô, Ifá, Ogum. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "lactedesesclav00bouc", "https://openlibrary.org/works/OL18095922W"],
     "url": IA + "lactedesesclav00bouc", "identificadores": {}, "editora": "Plon", "local": "Paris"},
    {"id": "ajisafe-1924-laws", "tipo": "livro", "categoria": "etno_classica", "autores": ["A. K. Ajisafe Moore"],
     "titulo": "The Laws and Customs of the Yoruba People",
     "ano": 1924, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "B",
     "observacoes": "Autor iorubá de Abeokuta (m. 1940): domínio público na Nigéria e na Espanha. 1ª ed. Londres, Routledge, 1924; o exemplar do Internet Archive é reimpressão sem data (Abeokuta, Fola Bookshops, 87 p.). Direito e costumes; trata de Egungun, Oro, Ifá e Ọ̀sanyìn de passagem. Visão de elite cristã iorubá do período colonial.",
     "status_verificacao": "conferido_web", "evidencias": [IA + "lawscustomsofyor00moorrich", "https://openlibrary.org/works/OL6709470W"],
     "url": IA + "lawscustomsofyor00moorrich", "identificadores": {}},
    {"id": "querino-1955-raca", "tipo": "livro", "categoria": "etno_classica", "autores": ["Manuel Querino"],
     "titulo": "A raça africana e os seus costumes",
     "ano": 1955, "idioma": "pt", "tradicoes": ["candomble_ketu"], "confiabilidade_preliminar": "B",
     "observacoes": "Edição póstuma (Salvador, Progresso, 1955, Coleção de Estudos Brasileiros, série Cruzeiro, v. 9) de textos de 1916–1917 do intelectual negro baiano Manuel Querino (m. 1923, domínio público). Texto integral no Internet Archive. Descreve candomblés de Salvador no início do séc. XX. Confiabilidade B como testemunho de época; ano citado = edição lida.",
     "status_verificacao": "conferido_web", "evidencias": [IA + "aracaafricana", "https://openlibrary.org/works/OL13005073W"],
     "url": IA + "aracaafricana", "identificadores": {"oclc": "1292905"}, "editora": "Progresso", "local": "Salvador"},
    {"id": "ortiz-1906-brujos", "tipo": "livro", "categoria": "etno_classica", "autores": ["Fernando Ortiz"],
     "titulo": "Hampa afro-cubana: los negros brujos (apuntes para un estudio de etnología criminal)",
     "ano": 1906, "idioma": "es", "tradicoes": ["lucumi"], "confiabilidade_preliminar": "C",
     "observacoes": "Madri, Librería de Fernando Fé, 1906, com carta-prólogo de Lombroso. Edição digital (Fundación Ignacio Larramendi, 2020) com texto integral no Internet Archive. Direitos: domínio público nos EUA (1906) e em Cuba (autor m. 1969, 50 anos); na Espanha (80 anos) só em 2050 — conferir antes de reproduzir trechos (paráfrase e citação são permitidas). Primeira descrição etnográfica dos orixás lucumís (Changó, Obatalá, Yemayá, Elegguá, Ochún etc.) sob o enquadramento da criminologia positivista. " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "hampa-afro-cubana-los-negros-brujos"],
     "url": IA + "hampa-afro-cubana-los-negros-brujos", "identificadores": {}, "editora": "Librería de Fernando Fé", "local": "Madri"},
    {"id": "bowen-1858-grammar", "tipo": "livro", "categoria": "etno_classica", "autores": ["Thomas Jefferson Bowen"],
     "titulo": "Grammar and Dictionary of the Yoruba Language, with an Introductory Description of the Country and People of Yoruba",
     "ano": 1858, "idioma": "en", "tradicoes": ["ioruba_nigeria"], "confiabilidade_preliminar": "C",
     "observacoes": "Smithsonian Contributions to Knowledge, v. 10 (Washington, 1858). Domínio público. Texto integral no Internet Archive (NOT_IN_COPYRIGHT) e HathiTrust (hvd.hx6h4d, pd). Verbetes de nomes de orixás e termos religiosos do séc. XIX (grafias antigas). " + COL,
     "status_verificacao": "conferido_web", "evidencias": [IA + "grammardictionar00bowerich", HT + "1875976.json"],
     "url": IA + "grammardictionar00bowerich", "identificadores": {"oclc": "1875976"}, "editora": "Smithsonian Institution", "local": "Washington"},
    {"id": "joao-do-rio-1904-religioes", "tipo": "livro", "categoria": "etno_classica", "autores": ["João do Rio"],
     "titulo": "As religiões no Rio",
     "ano": 1904, "idioma": "pt", "tradicoes": ["candomble_ketu"], "confiabilidade_preliminar": "C",
     "observacoes": "Reportagens de Paulo Barreto (João do Rio, m. 1921: domínio público) na Gazeta de Notícias, reunidas em livro (Rio de Janeiro, 1904; ed. Garnier, 1906). Digitalização da Biblioteca Brasiliana (USP) espelhada no Wikimedia Commons (faltam as pp. 9–12). Abre com 'No mundo dos feitiços': casas de orixás e alufás no Rio de 1904. Jornalismo sensacionalista de época; tradição 'candomble_ketu' é aproximação a confirmar (a obra fala de cultos africanos no Rio sem nação).",
     "status_verificacao": "conferido_web", "evidencias": ["https://digital.bbm.usp.br/handle/bbm/976", "https://digital.bbm.usp.br/handle/bbm/2680", "https://commons.wikimedia.org/wiki/File:As_religi%C3%B5es_no_Rio_(1904).pdf"],
     "url": "https://commons.wikimedia.org/wiki/File:As_religi%C3%B5es_no_Rio_(1904).pdf", "identificadores": {}, "editora": "Gazeta de Notícias", "local": "Rio de Janeiro"},
]

# Correções manuais dos registros incorporados pela coleta de 2026-11-01
CORRIGE = {
    "akin-otiko-2024-olodumare": {"idioma": "en"},
    "amherd-2026-soponna": {"idioma": "en"},
    "henry-2010-sakpata": {"idioma": "fr"},
    "mason-1996-olookun": {"idioma": "en"},
    "probst-osun-osogbo": {"idioma": "en"},
    "elebuibon-1999-iyere": {"idioma": "yo"},
    "olayemi-1971-ibeji": {"idioma": "yo", "autores": ["Val Ọlayẹmi"]},
    "asante-mazama-2009-obatala": {"idioma": "en", "evidencias": ["https://api.crossref.org/works/10.4135/9781412964623.n294", "https://doi.org/10.4135/9781412964623.n294"]},
    "abimbola-1997-mend": {"autores": ["Wande Abimbola"]},
    "durojaiye-1978-linguagem": {"autores": ["Benjy Ainde Kayode Durojaiye"]},
    "villepastour-2015-ayan": {"autores": ["Amanda Villepastour (org.)"], "titulo": "The Yorùbá God of Drumming: Transatlantic Perspectives on the Wood That Talks"},
    "love-2012-divining": {"titulo": "Divining the Self: A Study in Yoruba Myth and Human Consciousness"},
    "gleason-1987-oya": {"titulo": "Oya: In Praise of the Goddess"},
    "willis-2017-masquerading": {"titulo": "Masquerading Politics: Kinship, Gender, and Ethnicity in a Yoruba Town"},
    "ochoa-2020-lazarus": {"observacoes_extra": "O DOI registrado é o do cap. 8 ('A Bembé for San Lázaro–Babalú Ayé')."},
}
# Acesso aberto conferido pelo DOI em 2026-11-01 (página do artigo; status HTTP no relatório da varredura 4)
URL_OA = {
    "santos-2008-ia-mi": "https://revistas.usp.br/sankofa/pt_BR/article/view/88730",
    "henry-2010-sakpata": "https://journals.openedition.org/africanistes/2572",
    "pogoson-2011-ifa": "https://journals.openedition.org/cea/196",
    "caprara-1998-omolu": "https://books.scielo.org/id/by55h",
    "mota-2022-olubaje": "https://periodicos.ufrn.br/equatorial/article/view/26154",
    "leite-2020-omolu": "https://seer.pucgoias.edu.br/index.php/fragmentos/article/view/7748",
    "oliva-2012-eshu": "https://periodicos.furg.br/rbhcs/article/view/10501",
    "jesus-2024-cromatica": "https://periodicos.ufjf.br/index.php/sacrilegens/article/view/43378",
    "monteiro-2021-iya-mi": "https://periodicos.ufpa.br/index.php/ethnoscientia/article/view/10369",
    "sallum-2006-ossaim": "https://revistas.usp.br/revmae/pt_BR/article/view/89723",
    "noguera-2018-orunmila": "http://periodicos2.uesb.br/index.php/odeere/article/view/4328",
    "carvalho-2019-iyami": "https://periodicos.uff.br/fractal/article/view/29003",
    "fernandez-cano-2005-oya": "https://digibug.ugr.es/handle/10481/7188",
    "ofuasia-2023-ifa-hell": "https://www.mdpi.com/2077-1444/14/11/1416",
    "silva-2022-mina-nago": "https://books.scielo.org/id/zz9yp",
    "parizi-2020-livro-orixas": "https://www.editorafi.org/031orixas",
    "santos-h-2019-osumare": "https://periodicos.urca.br/ojs/index.php/MacREN/article/view/2204",
    "carrillo-2026-ochun": "https://www.periodicos.unimontes.br/index.php/argumentos/article/view/10395",
}
TROCA_OBS = {"oliva-2012-eshu": ("(Revista Brasileira de História, SciELO)", "(Revista Brasileira de História & Ciências Sociais, FURG)")}
RENOMEIA = {"sousa-2019-osumare": ("santos-h-2019-osumare", {"autores": ["Hyago Átilla Sousa dos Santos"]}),
            "rocha-unicamp-oxum": ("roquete-unicamp-oxum", {})}


def main():
    doc = json.loads(CATALOGO.read_text(encoding="utf-8"))
    fontes = doc["fontes"]
    por_id = {f["id"]: f for f in fontes}
    for velho, (novo, campos) in RENOMEIA.items():
        if velho in por_id and novo not in por_id:
            f = por_id.pop(velho)
            f["id"] = novo
            f.update(campos)
            por_id[novo] = f
    for fid, c in CORRIGE.items():
        f = por_id[fid]
        extra = c.get("observacoes_extra")
        for k, v in c.items():
            if k != "observacoes_extra":
                f[k] = v
        if extra and extra not in f["observacoes"]:
            f["observacoes"] += " " + extra
    for fid, url in URL_OA.items():
        por_id[fid]["url"] = url
    for fid, (a, b) in TROCA_OBS.items():
        por_id[fid]["observacoes"] = por_id[fid]["observacoes"].replace(a, b)
    for fid, url, evs, nota in ATUALIZA:
        f = por_id[fid]
        if url and not f.get("url"):
            f["url"] = url
        f["evidencias"] = list(dict.fromkeys((f.get("evidencias") or []) + ([url] if url and "archive.org" in url else []) + evs))
        marca = f"{TAG}: {nota}"
        obs = (f.get("observacoes") or "").split(f" | {TAG}:")[0]
        f["observacoes"] = (obs + " | " + marca).lstrip(" |")
        if "Olhar colonial" not in f["observacoes"] and f["confiabilidade_preliminar"] == "C":
            f["observacoes"] += " " + COL
    for n in NOVAS:  # registros desta rodada: o script é a fonte da verdade e os regrava
        n = dict(n, observacoes=f"{TAG}. " + n["observacoes"])
        por_id[n["id"]] = {k: n[k] for k in ORDEM if k in n}
    fontes = sorted(por_id.values(), key=lambda f: f["id"])
    doc["fontes"] = fontes
    doc["_meta"]["total"] = len(fontes)
    doc["_meta"]["atualizado_em"] = "2026-11-01"
    CATALOGO.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(fontes)} fontes; novas DP: {sum(1 for n in NOVAS)}; atualizadas: {len(ATUALIZA)}")


if __name__ == "__main__":
    main()
