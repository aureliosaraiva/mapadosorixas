"""Testes do validador de capítulos narrativos (scripts/validar_capitulos.py).

Cada teste copia data/, schemas/ e docs/pesquisa/PENDENCIAS.md para uma pasta
temporária, altera o capítulo de Ogum de um jeito proibido e confere que o
validador acusa o problema (e que o capítulo real passa)."""
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import capitulos  # noqa: E402
import validar_capitulos as vc  # noqa: E402

PARAGRAFO_OK = "O ferro é o ponto de partida."


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(RAIZ / "data", self.tmp / "data")
        shutil.copytree(RAIZ / "schemas", self.tmp / "schemas")
        (self.tmp / "docs" / "pesquisa").mkdir(parents=True)
        shutil.copy(RAIZ / "docs" / "pesquisa" / "PENDENCIAS.md", self.tmp / "docs" / "pesquisa" / "PENDENCIAS.md")
        for p in (self.tmp / "data" / "capitulos").glob("*"):
            if p.stem != "ogum":
                p.unlink()
        self.md = self.tmp / "data" / "capitulos" / "ogum.md"
        self.texto = self.md.read_text(encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def validar(self, texto=None, gerar=True):
        if texto is not None:
            self.md.write_text(texto, encoding="utf-8")
        erros, avisos = vc.validar(self.tmp, gerar=gerar, saida=lambda *_: None)
        return erros

    def com_paragrafo(self, par, secao="historia-do-culto"):
        """Insere um parágrafo logo depois do título da seção."""
        alvo = re.search(rf"^## .*\{{#{secao}\}}\n", self.texto, re.M)
        return self.texto[:alvo.end()] + "\n" + par + "\n" + self.texto[alvo.end():]

    def assertErro(self, erros, trecho):
        self.assertTrue(any(trecho in e for e in erros), f"esperava erro com “{trecho}”, veio: {erros[:5]}")


class Capitulos(Base):
    def test_capitulo_real_passa(self):
        self.assertEqual(self.validar(), [])

    def test_paragrafo_sem_referencia(self):
        self.assertErro(self.validar(self.com_paragrafo("Ogum é muito antigo e respeitado.")), "sem nenhuma referência")

    def test_trecho_final_sem_referencia(self):
        self.assertErro(self.validar(self.com_paragrafo("Ogum é o patrono dos ferreiros {{ref:ogum-012}}. E é muito antigo.")),
                        "trecho final sem referência")

    def test_referencia_pre_fichamento(self):
        self.assertErro(self.validar(self.com_paragrafo("Ogum na Bahia {{ref:ogum-003}}.")), "pre_fichamento")

    def test_referencia_inexistente(self):
        self.assertErro(self.validar(self.com_paragrafo("Ogum na Bahia {{ref:ogum-999}}.")), "registro inexistente")

    def test_referencia_retida(self):
        self.assertErro(self.validar(self.com_paragrafo("Exu e Ogum {{ref:exu-012}}.")), "retido")

    def test_lacuna_falsa(self):
        self.assertErro(self.validar(self.com_paragrafo("Não há cor de Ogum {{lacuna:cores}}.")), "lacuna falsa")

    def test_pendencia_inexistente(self):
        self.assertErro(self.validar(self.com_paragrafo("Falta ler um livro {{pendencia:Livro Inventado de Ninguém}}.")),
                        "não está em docs/pesquisa/PENDENCIAS.md")

    def test_heuristica_entidade_ausente(self):
        erros = self.validar(self.com_paragrafo("Ogum é patrono dos ferreiros desde 1777, em Ijebu {{ref:ogum-012}}."))
        self.assertErro(erros, "heurística")

    def test_copia_da_parafrase(self):
        r = next(r for r in vc.ent.todos_registros(self.tmp) if r["id"] == "ogum-034")
        erros = self.validar(self.com_paragrafo(r["parafrase"] + " {{ref:ogum-034}}"))
        self.assertErro(erros, "8+ palavras iguais")

    def test_expressao_que_elege_versao(self):
        self.assertErro(self.validar(self.com_paragrafo("Na verdade, Ogum é patrono dos ferreiros na Bahia {{ref:ogum-012}}.")),
                        "elege versão")

    def test_autor_no_corpo(self):
        self.assertErro(self.validar(self.com_paragrafo("Segundo Bastide, Ogum é patrono dos ferreiros na Bahia {{ref:ogum-012}}.")),
                        "autor citado no corpo")

    def test_umbanda_sem_dizer(self):
        self.assertErro(self.validar(self.com_paragrafo("Em João Pessoa, Ogum é São Jorge {{ref:ogum-006}}.")),
                        "sem dizer 'Umbanda'")

    def test_divergencia_sem_tradicao(self):
        self.assertErro(self.validar(self.com_paragrafo("A cor de Ogum é verde e vermelho {{ref:ogum-054}}.")),
                        "versão divergente")

    def test_documento_colonial_sem_marca(self):
        self.assertErro(self.validar(self.com_paragrafo("Odudua e Obatala tiveram Aganju e Yemaja, e Ogun nasceu dela {{ref:iemanja-060}}.",
                                                        "mitos")),
                        "documento histórico")

    def test_secao_obrigatoria(self):
        sem = re.sub(r"## Sincretismo \{#sincretismo\}\n.*?(?=## Leituras)", "", self.texto, flags=re.S)
        self.assertErro(self.validar(sem), "falta a seção obrigatória")

    def test_json_desatualizado(self):
        self.validar()
        self.md.write_text(self.texto.replace(PARAGRAFO_OK, "O ferro é, de fato, o começo."), encoding="utf-8")
        self.assertErro(self.validar(gerar=False), "desatualizado")


class Formato(unittest.TestCase):
    def test_segmentos_e_notas_agrupadas(self):
        tks = capitulos.tokens("A {{ref:a-001}} B {{ref:a-002,a-003}}{{lacuna:cores}} C [x](ita:ita-001) {{pendencia:Algo longo}}")
        segs = capitulos.segmentos(tks)
        self.assertEqual(len(segs), 3)
        est = {"front": {"orixa": "a"}, "secoes": [{"slug": "abertura", "titulo": None,
                                                    "blocos": [{"tipo": "paragrafo", "linha": 1, "tokens": tks}]}]}
        js = capitulos.gerar_json(est)
        self.assertEqual([len(n["itens"]) for n in js["notas"]], [1, 3, 1])
        self.assertEqual([t["n"] for t in js["secoes"][0]["blocos"][0]["tokens"] if t["t"] == "nota"], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
