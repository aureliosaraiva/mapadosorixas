"""Testes do registro da revisão do conselho (scripts/revisao.py, gerar_fichas.py).

Fixtures 100% sintéticas: revisores fictícios e registros inventados com ids
na faixa 9xx, que não existem em data/. Nada aqui é conteúdo sobre orixás.

Uso: python3 -m unittest discover -s tests -v
"""
import copy
import datetime as dt
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

import revisao  # noqa: E402
import gerar_fichas  # noqa: E402

HOJE = dt.date(2027, 6, 1)
TRADS = {"candomble_ketu", "candomble_angola", "umbanda"}


def revisor(id_, credito="nome_e_tradicao", nome="Pessoa Fictícia", desc="descrição fictícia de teste",
            tradicoes=("candomble_ketu",), data="2027-01-10", revogado=None, remover=None):
    cons = {"versao_termo": "1.0", "data": data, "revogado_em": revogado}
    if remover is not None:
        cons["remover_revisoes"] = remover
    return {"id": id_, "credito": credito, "nome_publico": nome, "descricao_publica": desc,
            "tipo": "praticante", "tradicoes": list(tradicoes), "consentimento": cons}


def registro(id_="exu-901", status="fichado", tradicoes=("candomble_ketu",), atributo="cores", valor="valor sintético"):
    return {"id": id_, "orixa": "exu", "atributo": atributo, "valor": valor, "tradicoes": list(tradicoes),
            "casa_ou_regiao": None, "source_id": "fonte-sintetica", "via_source_id": None,
            "localizacao": "p. 1", "parafrase": f"paráfrase sintética de {id_}", "nota": None, "status": status}


def rev(r, revisor_id="rev-901", tradicao="candomble_ketu", parecer="aprovado", data="2027-02-14", nota=None, hash_=None):
    return {"revisor_id": revisor_id, "data": data, "tradicao": tradicao, "parecer": parecer,
            "aspectos": ["parafrase", "tradicao"], "hash_registro": hash_ or revisao.hash_registro(r), "nota": nota}


def revisado(r, **kw):
    r = copy.deepcopy(r)
    r["status"] = "revisado"
    r["revisoes"] = [rev(r, **kw)]
    return r


class Base(unittest.TestCase):
    def setUp(self):
        self.revisores = [
            revisor("rev-901"),
            revisor("rev-902", credito="anonimo", nome=None, desc=None, tradicoes=("candomble_angola", "candomble_ketu")),
            revisor("rev-903", credito="so_nome", nome="Só O Nome", desc=None, tradicoes=("umbanda",)),
        ]
        self.rp = revisao.por_id(self.revisores)

    def validar(self, regs):
        return revisao.validar_revisoes(regs, self.revisores, TRADS, hoje=HOJE)


class TestHash(unittest.TestCase):
    def test_hash_estavel_e_sensivel(self):
        r = registro()
        h = revisao.hash_registro(r)
        self.assertRegex(h, r"^sha256:[0-9a-f]{64}$")
        self.assertEqual(h, revisao.hash_registro(copy.deepcopy(r)))
        r2 = dict(r, parafrase="outra paráfrase")
        self.assertNotEqual(h, revisao.hash_registro(r2))
        # campos fora do hash (nota, status, evidências) não desatualizam a revisão
        self.assertEqual(h, revisao.hash_registro(dict(r, nota="nota nova", status="revisado")))


class TestStatusRevisado(Base):
    def test_revisado_sem_revisao_e_erro(self):
        erros, _ = self.validar([registro(status="revisado")])
        self.assertTrue(any("exige ao menos uma revisão aprovada" in e for e in erros), erros)

    def test_revisado_com_aprovacao_valida(self):
        r = revisado(registro())
        erros, avisos = self.validar([r])
        self.assertEqual(erros, [])
        self.assertEqual(revisao.status_efetivo(r, self.rp), "revisado")

    def test_aprovado_com_ressalva_tambem_vale(self):
        r = revisado(registro(), parecer="aprovado_com_ressalva", nota="ressalva sintética")
        self.assertEqual(self.validar([r])[0], [])
        self.assertEqual(revisao.status_efetivo(r, self.rp), "revisado")

    def test_so_contestacao_nao_basta(self):
        r = revisado(registro(), parecer="contestado", nota="motivo sintético")
        erros, _ = self.validar([r])
        self.assertTrue(any("exige ao menos uma revisão aprovada" in e for e in erros), erros)

    def test_revisor_inexistente(self):
        r = revisado(registro(), revisor_id="rev-999")
        erros, _ = self.validar([r])
        self.assertTrue(any("não existe em data/revisores.json" in e for e in erros), erros)
        self.assertEqual(revisao.status_efetivo(r, self.rp), "fichado")

    def test_tradicao_fora_do_registro(self):
        r = revisado(registro(tradicoes=("umbanda",)), tradicao="candomble_ketu")
        erros, _ = self.validar([r])
        self.assertTrue(any("não está nas tradições do registro" in e for e in erros), erros)

    def test_tradicao_fora_do_revisor(self):
        # rev-901 só revisa Ketu; o registro é Ketu + Angola e a revisão diz Angola
        r = revisado(registro(tradicoes=("candomble_ketu", "candomble_angola")), tradicao="candomble_angola")
        erros, _ = self.validar([r])
        self.assertTrue(any("não está nas tradições do revisor rev-901" in e for e in erros), erros)

    def test_hash_desatualizado_volta_a_fichado(self):
        r = revisado(registro())
        r["parafrase"] = "paráfrase alterada depois da revisão"
        erros, avisos = self.validar([r])
        self.assertEqual(erros, [])
        self.assertTrue(any("revisao_desatualizada" in a for a in avisos), avisos)
        self.assertEqual(revisao.status_efetivo(r, self.rp), "fichado")
        self.assertEqual(revisao.resumo_publico(r, self.rp), [])

    def test_fichado_com_aprovacao_gera_aviso(self):
        r = registro()
        r["revisoes"] = [rev(r)]
        erros, avisos = self.validar([r])
        self.assertEqual(erros, [])
        self.assertTrue(any("pode passar a 'revisado'" in a for a in avisos))
        self.assertEqual(revisao.status_efetivo(r, self.rp), "fichado")

    def test_pre_fichamento_nao_pode_ser_revisado(self):
        r = registro(status="pre_fichamento")
        r["revisoes"] = [rev(r)]
        erros, _ = self.validar([r])
        self.assertTrue(any("só registros fichados" in e for e in erros), erros)

    def test_datas(self):
        futura = revisado(registro("exu-902"), data="2027-12-01")
        antes = revisado(registro("exu-903"), data="2026-12-31")
        erros, _ = self.validar([futura, antes])
        self.assertTrue(any("data no futuro" in e for e in erros), erros)
        self.assertTrue(any("anterior ao termo de consentimento" in e for e in erros), erros)

    def test_revisao_depois_da_revogacao(self):
        self.revisores[0] = revisor("rev-901", nome=None, desc=None, revogado="2027-02-01")
        r = revisado(registro(), data="2027-03-01")
        erros, _ = self.validar([r])
        self.assertTrue(any("posterior à revogação" in e for e in erros), erros)

    def test_contestado_exige_nota(self):
        r = registro()
        r["revisoes"] = [rev(r, parecer="contestado")]
        erros, _ = self.validar([r])
        self.assertTrue(any("contestado exige nota" in e for e in erros), erros)

    def test_revisao_repetida(self):
        r = revisado(registro())
        r["revisoes"].append(copy.deepcopy(r["revisoes"][0]))
        erros, _ = self.validar([r])
        self.assertTrue(any("revisão repetida" in e for e in erros), erros)


class TestConsentimento(Base):
    def erros(self, *revs):
        return revisao.validar_revisores(list(revs), TRADS)

    def test_validos(self):
        self.assertEqual(self.erros(*self.revisores), [])
        self.assertEqual(self.erros(revisor("rev-904", credito="generico", nome=None)), [])

    def test_anonimo_com_nome(self):
        self.assertTrue(self.erros(revisor("rev-904", credito="anonimo", nome="Vazou", desc=None)))

    def test_so_nome_com_descricao(self):
        self.assertTrue(self.erros(revisor("rev-904", credito="so_nome")))

    def test_generico_com_nome(self):
        self.assertTrue(self.erros(revisor("rev-904", credito="generico")))

    def test_nome_e_tradicao_incompleto(self):
        self.assertTrue(self.erros(revisor("rev-904", desc=None)))

    def test_revogado_precisa_zerar_nome(self):
        self.assertTrue(self.erros(revisor("rev-904", revogado="2027-02-01")))
        self.assertEqual(self.erros(revisor("rev-904", nome=None, desc=None, revogado="2027-02-01")), [])

    def test_remover_revisoes_so_com_revogacao(self):
        self.assertTrue(self.erros(revisor("rev-904", remover=True)))

    def test_contato_nao_entra(self):
        self.assertTrue(self.erros(revisor("rev-904", desc="fale comigo em pessoa@exemplo.org")))
        self.assertTrue(self.erros(revisor("rev-905", desc="telefone +55 (71) 99999-0000")))

    def test_id_repetido_e_tradicao_desconhecida(self):
        e = self.erros(revisor("rev-904"), revisor("rev-904", tradicoes=("nacao_inventada",)))
        self.assertTrue(any("id repetido" in x for x in e))
        self.assertTrue(any("tradição desconhecida" in x for x in e))

    def test_esquema_recusa_campo_de_contato(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest("jsonschema ausente")
        import json
        s = json.loads((RAIZ / "schemas" / "revisor.schema.json").read_text(encoding="utf-8"))
        r = revisor("rev-904")
        r["email"] = "x@y.z"
        self.assertTrue(list(jsonschema.Draft202012Validator(s).iter_errors(r)))
        self.assertFalse(list(jsonschema.Draft202012Validator(s).iter_errors(revisor("rev-904"))))

    def test_credito_exibido(self):
        rp = revisao.por_id(self.revisores + [revisor("rev-904", credito="generico", nome=None, desc="iyalorixá fictícia"),
                                              revisor("rev-905", nome=None, desc=None, revogado="2027-03-01")])
        self.assertEqual(revisao.quem(rp["rev-901"]), "Pessoa Fictícia, descrição fictícia de teste")
        self.assertEqual(revisao.quem(rp["rev-902"]), revisao.ANONIMO)
        self.assertEqual(revisao.quem(rp["rev-903"]), "Só O Nome")
        self.assertEqual(revisao.quem(rp["rev-904"]), "iyalorixá fictícia")
        self.assertEqual(revisao.quem(rp["rev-905"]), revisao.ANONIMO)
        linha = revisao.linha_credito({"revisor": "rev-902", "tradicao": "candomble_angola", "data": "2027-02-14",
                                       "parecer": "contestado", "nota": "motivo"}, rp, lambda t: "Angola")
        self.assertEqual(linha, "Contestado por revisor/a anônimo/a (Angola) em 14/02/2027: motivo")


class TestHistorico(Base):
    def test_remover_revisao_e_erro(self):
        base = revisado(registro())
        atual = copy.deepcopy(base)
        atual["revisoes"] = []
        self.assertTrue(revisao.comparar_historico([base], [atual], self.revisores))

    def test_alterar_revisao_e_erro(self):
        base = revisado(registro())
        atual = copy.deepcopy(base)
        atual["revisoes"][0]["parecer"] = "aprovado_com_ressalva"
        self.assertTrue(revisao.comparar_historico([base], [atual], self.revisores))

    def test_acrescentar_e_ok(self):
        base = revisado(registro(tradicoes=("candomble_ketu", "candomble_angola")))
        atual = copy.deepcopy(base)
        atual["revisoes"].append(rev(atual, revisor_id="rev-902", tradicao="candomble_angola", parecer="contestado", nota="m"))
        self.assertEqual(revisao.comparar_historico([base], [atual], self.revisores), [])

    def test_remover_registro_revisado_e_erro(self):
        base = revisado(registro())
        e = revisao.comparar_historico([base], [], self.revisores)
        self.assertTrue(any("registro com revisão foi removido" in x for x in e), e)

    def test_remocao_pedida_na_revogacao(self):
        self.revisores[0] = revisor("rev-901", nome=None, desc=None, revogado="2027-03-01", remover=True)
        base = revisado(registro())
        atual = copy.deepcopy(base)
        atual["revisoes"], atual["status"] = [], "fichado"
        self.assertEqual(revisao.comparar_historico([base], [atual], self.revisores), [])


class TestGerador(Base):
    def test_sem_revisao_saida_inalterada(self):
        f = gerar_fichas.gerar_ficha("exu", [registro()], revisores={})
        v = f["atributos"]["cores"][0]
        self.assertNotIn("revisoes", v)
        self.assertEqual(v["status"], "fichado")
        self.assertEqual(f["revisao"], [])

    def test_revisao_copiada_sem_dados_pessoais(self):
        r = revisado(registro())
        f = gerar_fichas.gerar_ficha("exu", [r], revisores=self.rp)
        v = f["atributos"]["cores"][0]
        self.assertEqual(v["status"], "revisado")
        self.assertEqual(v["revisoes"], [{"revisor": "rev-901", "tradicao": "candomble_ketu", "data": "2027-02-14",
                                          "parecer": "aprovado", "nota": None}])
        self.assertNotIn("Pessoa Fictícia", str(f))
        self.assertEqual(f["revisao"], [{"revisor_id": "rev-901", "tradicao": "candomble_ketu", "data": "2027-02-14", "versoes": 1}])

    def test_contestado_nao_apaga_versao(self):
        r = registro(tradicoes=("candomble_ketu", "candomble_angola"))
        r["status"] = "revisado"
        r["revisoes"] = [rev(r), rev(r, revisor_id="rev-902", tradicao="candomble_angola", parecer="contestado", nota="na Angola é diferente")]
        self.assertEqual(self.validar([r])[0], [])
        f = gerar_fichas.gerar_ficha("exu", [r], revisores=self.rp)
        v = f["atributos"]["cores"][0]
        self.assertEqual(v["status"], "revisado")
        self.assertEqual([x["parecer"] for x in v["revisoes"]], ["aprovado", "contestado"])

    def test_nao_publicar_retira_mas_lista(self):
        a, b = registro("exu-901"), registro("exu-902", valor="outro valor")
        b["revisoes"] = [rev(b, parecer="nao_publicar", nota=None)]
        self.assertEqual(self.validar([a, b])[0], [])
        f = gerar_fichas.gerar_ficha("exu", [a, b], revisores=self.rp)
        self.assertEqual([v["registro"] for v in f["atributos"]["cores"]], ["exu-901"])
        self.assertEqual(f["pendencias"]["retidos_ate_conselho"], {"cores": ["exu-902"]})

    def test_nao_publicar_vale_mesmo_desatualizado(self):
        b = registro("exu-902")
        b["revisoes"] = [rev(b, parecer="nao_publicar", hash_="sha256:" + "0" * 64)]
        self.assertFalse(revisao.publicavel(b, self.rp))

    def test_revisao_desatualizada_nao_aparece(self):
        r = revisado(registro())
        r["valor"] = "valor mudou"
        f = gerar_fichas.gerar_ficha("exu", [r], revisores=self.rp)
        v = f["atributos"]["cores"][0]
        self.assertEqual(v["status"], "fichado")
        self.assertNotIn("revisoes", v)


if __name__ == "__main__":
    unittest.main()
