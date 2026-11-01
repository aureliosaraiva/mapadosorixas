"""Testes do modelo 2: lista-mestra (data/entidades.json), fichamento genérico e itãs."""
import json
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import entidades  # noqa: E402
import gerar_fichas  # noqa: E402

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


def ler(p):
    return json.loads((RAIZ / p).read_text(encoding="utf-8"))


EXIGIDAS = ["exu", "ogum", "oxossi", "ossaim", "oxumare", "omolu", "nana", "xango", "iansa", "oba", "ewa", "oxum",
            "logunede", "iemanja", "oxala", "oxalufa", "oxaguia", "ibeji", "iroko", "orunmila", "odudua", "orixa_oko",
            "olokun", "aganju", "erinle", "aje_xaluga", "iyewa", "olodumare", "orum", "aie", "orixas_funfun", "egungun", "iyami"]


class ListaMestra(unittest.TestCase):
    def test_entidades_exigidas(self):
        ids = entidades.ids()
        for i in EXIGIDAS:
            self.assertIn(i, ids)
        self.assertEqual(len(ids), len(set(ids)))

    def test_iyami_sensivel_e_qualidades(self):
        e = entidades.por_id()
        self.assertTrue(e["iyami"]["sensivel"])
        self.assertEqual(e["oxalufa"]["qualidade_de"], "oxala")
        self.assertEqual(e["oxaguia"]["tipo"], "qualidade")

    def test_nenhum_grupo_confirmado_sem_registro(self):
        for e in entidades.lista():
            if e["grupo"]:
                self.assertEqual(e["grupo"]["confirmado_por"], [], e["id"])  # até haver fonte

    def test_status_conteudo(self):
        self.assertEqual(entidades.status_conteudo([]), "sem_fichamento")
        self.assertEqual(entidades.status_conteudo([{"status": "pre_fichamento"}]), "pre")
        self.assertEqual(entidades.status_conteudo([{"status": "pre_fichamento"}, {"status": "fichado"}]), "fichado")

    @unittest.skipIf(jsonschema is None, "jsonschema ausente")
    def test_esquema(self):
        s = ler("schemas/entidades.schema.json")
        jsonschema.validate(ler("data/entidades.json"), s)
        ruim = ler("data/entidades.json")
        ruim["entidades"][0]["grupo"] = {"rotulo": "inventado", "confirmado_por": []}
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(ruim, s)

    def test_fichas_so_de_entidades_da_lista(self):
        ids = set(entidades.ids())
        for p in (RAIZ / "data/orixas").glob("*.json"):
            self.assertIn(p.stem, ids)


class Fichamento(unittest.TestCase):
    def test_esquema_aceita_qualquer_id_e_hierarquia(self):
        s = ler("schemas/fichamento.schema.json")
        self.assertIn("hierarquia", s["properties"]["atributo"]["enum"])
        self.assertNotIn("enum", s["properties"]["orixa"])

    def test_registros_no_arquivo_da_entidade(self):
        for eid, regs in entidades.registros_por_entidade().items():
            for r in regs:
                self.assertEqual(r["orixa"], eid)
                self.assertTrue(r["id"].startswith(eid + "-"))


class Itans(unittest.TestCase):
    def test_espelho(self):
        r = {"valor": "v", "parafrase": "p", "tradicoes": ["candomble_ketu"], "casa_ou_regiao": None,
             "source_id": "s", "localizacao": "p. 1", "via_source_id": None, "nota": None, "status": "fichado"}
        e = gerar_fichas.espelho(r)
        self.assertEqual(e["resumo"], "p")
        self.assertEqual(e["sources"], [{"id": "s", "loc": "p. 1", "via": None}])

    def test_espelhos_em_dia(self):
        regs = {r["id"]: r for r in entidades.todos_registros()}
        for it in ler("data/itans.json")["itans"]:
            for v in it["versoes"]:
                if v["registro"]:
                    esperado = gerar_fichas.espelho(regs[v["registro"]])
                    self.assertEqual({k: v[k] for k in esperado}, esperado, v["registro"])

    @unittest.skipIf(jsonschema is None, "jsonschema ausente")
    def test_esquema_ita(self):
        s = ler("schemas/ita.schema.json")
        for it in ler("data/itans.json")["itans"]:
            jsonschema.validate(it, s)
        ruim = ler("data/itans.json")["itans"][0]
        ruim["versoes"][0]["sources"] = []
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(ruim, s)


if __name__ == "__main__":
    unittest.main()
