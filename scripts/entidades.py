"""Lista-mestra de entidades (data/entidades.json) e leitura genérica do fichamento.

Usado por validar_fichamento.py, gerar_fichas.py, validar_fichas.py,
divergencias.py, anticopia.py e qa_site.py. O fichamento tem um arquivo por
entidade: data/fichamento/<id>.json, com <id> da lista-mestra; os registros
desse arquivo têm `orixa` = <id> e ids <id>-NNN. (O campo continua se chamando
`orixa` por compatibilidade com os registros e hashes de revisão existentes.)
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GERADOS_NO_FICHAMENTO = {"divergencias.json"}
STATUS_CONTEUDO = ("sem_fichamento", "pre", "fichado")


def ler(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def carregar(raiz=RAIZ):
    return ler(Path(raiz) / "data" / "entidades.json")


def lista(raiz=RAIZ):
    return carregar(raiz)["entidades"]


def por_id(raiz=RAIZ):
    return {e["id"]: e for e in lista(raiz)}


def ids(raiz=RAIZ):
    return [e["id"] for e in lista(raiz)]


def arquivos_fichamento(raiz=RAIZ):
    """Arquivos data/fichamento/<id>.json (sem os gerados), em ordem alfabética."""
    return sorted(p for p in (Path(raiz) / "data" / "fichamento").glob("*.json")
                  if p.name not in GERADOS_NO_FICHAMENTO)


def registros_por_entidade(raiz=RAIZ):
    """{id da entidade: [registros]} na ordem da lista-mestra (só quem tem arquivo)."""
    arqs = {p.stem: p for p in arquivos_fichamento(raiz)}
    ordem = ids(raiz)
    chaves = [i for i in ordem if i in arqs] + sorted(set(arqs) - set(ordem))
    return {i: ler(arqs[i])["registros"] for i in chaves}


def todos_registros(raiz=RAIZ):
    return [r for regs in registros_por_entidade(raiz).values() for r in regs]


def status_conteudo(regs):
    """sem_fichamento (nenhum registro), pre (só pré-fichamento) ou fichado."""
    if not regs:
        return "sem_fichamento"
    if any(r["status"] in ("fichado", "revisado") for r in regs):
        return "fichado"
    return "pre"
