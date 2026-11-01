"""Termos de pertinência para a triagem automática da coleta.

Normaliza (sem acento, minúsculas) e procura termos por radical. Termos
"fortes" indicam religião afro-diaspórica por si sós; termos "fracos" (nomes
de orixá que também são topônimos ou palavras comuns: Ogun State, Exu,
Sango/Congo etc.) só contam junto com um termo forte ou em contexto.
"""
import re
import unicodedata

FORTES = {
    "orixa": r"orix[aá]", "orisha": r"orisha|orisa\b|orisas\b|orishas", "oricha": r"oricha",
    "candomble": r"candombl", "umbanda": r"umband", "quimbanda": r"quimband",
    "santeria": r"santer[ií]a", "lucumi": r"lucum[ií]", "regla de ocha": r"regla de ocha|\bocha\b",
    "ifa": r"\bif[aá]\b", "vodou": r"vodou|vodun|vodum|voudou|voodoo|vaudou|vodu\b",
    "inquice": r"inquice|nkisi|minkisi", "batuque": r"batuque", "tambor de mina": r"tambor de mina|casa das minas",
    "terreiro": r"terreiro", "afro-brasileiro": r"afro[- ]?brasil|afro[- ]?brazil|afrobrasil|afro-bresil",
    "afro-cubano": r"afro[- ]?cuban|afrocuban", "afro-diasporico": r"afro[- ]?diasp|african diaspora religion",
    "axe": r"\bax[eé]\b", "babalorixa": r"babalorix|iyalorix|ialorix|babalawo|babalao|babalaô",
    "yoruba religion": r"yoruba religio|religion yoruba|religiao ioruba|religion des yoruba|yoruba relig",
    "spiritual baptist": r"spiritual baptist|shouter",
    "legba": r"legba", "elegua": r"elegg?u[aá]", "eshu": r"\beshu\b|elegbara",
    "ochosi": r"ochosi|oshosi|oxossi|oxoss|osoosi|ososi", "yemoja": r"yemoja|yemaya|iemanj|yemanja|yemonja",
    "shango": r"shango|chang[oó]\b|xang[oô]", "ogou": r"\bogou\b", "orunmila": r"orunmila|orula",
    # varredura nº 4: orixás além dos 5, cosmologia e itãs
    "oxala": r"oxal[aá]|obatal[aá]|orisanla|orishanla|oshala", "oxum": r"\boxum\b|\boshun\b|\bochun\b",
    "iansa": r"ians[aã]|\boya\b|\boy[aá]\b", "nana": r"nan[aã] buruku|nana buluku|\bnan[aã]\b (?:orix|buruk)",
    "omolu": r"omolu|obaluai|obaluay|babal[uú] ay|sakpata|sapata|xapan[aã]|sopona|shopona",
    "oxumare": r"oxumar|osumare|oshumare|\bdan\b ayido", "ossaim": r"ossaim|ossain|osanyin|osain\b",
    "logunede": r"logun ?ed[eé]|logun ?ede", "ewa": r"\bew[aá]\b|\byew[aá]\b", "ibeji": r"ibeji|ibej[ií]",
    "iroko": r"iroko|irok[oô]", "oduduwa": r"oduduwa|odudua", "olokun": r"olokun", "obaluaye": r"obaluaye",
    "olodumare": r"olodumar|olorun|olofin|eledumare", "egungun": r"egungun|egun\b|\beguns?\b|babaegum",
    "iyami": r"iyami|iy[aá]mi|\baje\b witch|oxorong", "itan": r"\bit[aã]s\b|\bit[aã]\b|patak[ií]", "odu": r"\bodu\b|\bodus\b|merindilogun|dilogun|diloggun",
    "oriki": r"or[ií]k[ií]",
}
FRACOS = {"ogum": r"\bogum\b|\bogun\b|\bogu\b", "exu": r"\bexu\b|\besu\b", "sango": r"\bsango\b",
          "yoruba": r"yoruba|ioruba|yorùbá|iorubá", "oyo": r"\boyo\b", "dahomey": r"dahom|daome|\bfon\b",
          "osun": r"\bosun\b", "nana": r"\bnan[aã]\b"}
EXCLUI = [r"osun state", r"oyo state", r"ogun state", r"estado de ogun", r"exu\b.*\bexus? (?:de|da) ", r"sango (?:river|town)"]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"<[^>]+>", " ", s).lower()


def termos_encontrados(texto):
    t = norm(texto)
    achou = [k for k, rx in FORTES.items() if re.search(rx, t)]
    achou += [f"~{k}" for k, rx in FRACOS.items() if re.search(rx, t)]
    if any(re.search(rx, t) for rx in EXCLUI):
        achou.append("!excluir")
    return achou


def pontuacao(termos_titulo, termos_resumo):
    """2 = pertinente no título; 1 = só no resumo ou só termos fracos combinados; 0 = não."""
    fortes_t = [x for x in termos_titulo if not x.startswith(("~", "!"))]
    fracos_t = [x for x in termos_titulo if x.startswith("~")]
    fortes_r = [x for x in termos_resumo if not x.startswith(("~", "!"))]
    if "!excluir" in termos_titulo and not fortes_t:
        return 0
    if fortes_t:
        return 2
    if fracos_t and (fortes_r or len(fracos_t) >= 2):
        return 1
    if len(fortes_r) >= 2:
        return 1
    return 0
