# Como registrar uma revisão do conselho (passo a passo)

> Implementação dos passos 1–3 da [proposta](proposta-registro-revisao.md), com o gerador e o site já preparados para exibir revisões. **Nenhum revisor existe ainda:** `data/revisores.json` está vazio e nenhum registro tem `revisoes`. O exemplo abaixo é fictício e fica **só nesta página**, nunca nos dados.

## Onde fica cada coisa

| O quê | Onde | Público? |
|---|---|---|
| Quem pode ser creditado e como | `data/revisores.json` (esquema [`schemas/revisor.schema.json`](../../schemas/revisor.schema.json)) | sim, no repositório. Não vai para `/dados/` do site |
| O parecer sobre cada afirmação | campo `revisoes` do registro em `data/fichamento/<orixa>.json` (esquema em [`schemas/fichamento.schema.json`](../../schemas/fichamento.schema.json), `$defs.revisao`) | sim |
| Contatos, termo assinado, quem é cada revisor anônimo | **fora do repositório**, com o autor | não |
| Resumo exibido (sem nome) | gerado em `data/orixas/<orixa>.json`: `revisoes` na versão e `revisao` na ficha | sim |

O cadastro ficou em `data/revisores.json`, e não em `data/conselho/revisores.json` como dizia a proposta, para não criar uma pasta com um arquivo só.

Regras comuns em [`scripts/revisao.py`](../../scripts/revisao.py), que o validador, o gerador e o QA do site usam.

## Passo a passo

### 1. Antes: termo de consentimento

A pessoa assina o termo de [`kit-revisao.md`](kit-revisao.md) §3. O autor guarda o termo **fora do repositório**. O que entra no repo é só a opção de crédito marcada.

### 2. Cadastrar o revisor em `data/revisores.json`

Escolha o próximo `rev-NNN` livre. Nunca reutilize um id, nem de quem saiu. Exemplo **fictício**:

```json
{
  "id": "rev-001",
  "credito": "nome_e_tradicao",
  "nome_publico": "Nome Como Autorizado",
  "descricao_publica": "iyalorixá, Candomblé Ketu, Salvador",
  "tipo": "praticante",
  "tradicoes": ["candomble_ketu"],
  "consentimento": { "versao_termo": "1.0", "data": "2027-02-01", "revogado_em": null }
}
```

| `credito` (opção do termo) | `nome_publico` | `descricao_publica` | O site mostra |
|---|---|---|---|
| `nome_e_tradicao` | obrigatório | obrigatório | "Nome Como Autorizado, iyalorixá, Candomblé Ketu, Salvador" |
| `so_nome` | obrigatório | `null` | "Nome Como Autorizado" |
| `generico` | `null` | obrigatório | "iyalorixá, Candomblé Ketu, Salvador" |
| `anonimo` | `null` | `null` | "revisor/a anônimo/a" |

- `tradicoes`: ids de [`data/tradicoes.json`](../../data/tradicoes.json) **em nome das quais** a pessoa revisa. A revisão só vale para essas tradições.
- O esquema recusa campos extras (e-mail, telefone etc.), e o validador recusa nome ou descrição que pareçam contato.

### 3. Registrar o parecer no registro de fichamento

Para cada registro revisado, gere a entrada com o hash atual:

```bash
python3 scripts/revisao.py hash ogum-012                     # só o hash
python3 scripts/revisao.py modelo ogum-012 rev-001 candomble_ketu aprovado
```

O segundo comando imprime a entrada pronta. Ajuste `data` (dia da revisão), `aspectos` (o que a pessoa de fato conferiu) e `nota`, e acrescente ao fim de `revisoes` do registro:

```json
"revisoes": [
  {
    "revisor_id": "rev-001",
    "data": "2027-02-14",
    "tradicao": "candomble_ketu",
    "parecer": "aprovado",
    "aspectos": ["parafrase", "fonte", "tradicao", "tom", "publicavel"],
    "hash_registro": "sha256:…",
    "nota": null
  }
]
```

| `parecer` | Efeito | Muda `status`? |
|---|---|---|
| `aprovado` | versão exibe "Revisado por … (tradição) em dd/mm/aaaa" | pode passar a `revisado` |
| `aprovado_com_ressalva` | "Revisado com ressalva por …: [nota]" | pode passar a `revisado` |
| `contestado` | "Contestado por … (tradição) em …: [nota]". A versão **continua** na ficha. `nota` obrigatória | não |
| `nao_publicar` | a versão sai da ficha pública e vai para `pendencias.retidos_ate_conselho` (também sai do grafo e das divergências). Vale mesmo que o registro mude depois; só o autor desfaz, depois de ouvir o conselho | não |

Depois de uma aprovação, troque o `status` do registro para `"revisado"`.

A `nota` é parafraseada e nunca traz fundamento ([`kit-revisao.md`](kit-revisao.md) §2).

### 4. Regenerar e validar

```bash
python3 scripts/validar_fichamento.py     # revisores, revisões e histórico (contra HEAD)
python3 scripts/gerar_fichas.py
python3 scripts/divergencias.py
python3 scripts/validar_fichas.py
python3 -m unittest discover -s tests
cd site && npm run build && python3 ../scripts/qa_site.py
```

### 5. Commit

Uma revisão por commit, com mensagem do tipo `Revisão rev-001 (candomble_ketu): ogum-012, ogum-015`. O histórico do git é o registro de quem mudou o quê.

## O que o validador confere

`scripts/validar_fichamento.py`, com as regras em `scripts/revisao.py`:

1. **`revisado` exige aprovação vigente:** pelo menos uma revisão `aprovado` ou `aprovado_com_ressalva` de revisor cadastrado, em nome de uma tradição que esteja em `tradicoes` do registro **e** nas do revisor, com `hash_registro` igual ao atual. Sem nenhuma aprovação, é erro.
2. **Revisão desatualizada:** se o registro mudou depois da revisão (`valor`, `parafrase`, `tradicoes`, `casa_ou_regiao`, `source_id` ou `localizacao`), aparece o aviso `revisao_desatualizada`. A versão volta a `fichado` na ficha e a linha da revisão some do site, até nova revisão. `nota`, `status` e `evidencias` não entram no hash.
3. **Revisão não apaga versões:** `contestado` mantém a versão; `nao_publicar` a move para `retidos_ate_conselho`, onde ela continua listada. `validar_fichas.py` acusa se algum registro fichado sumir da ficha sem estar retido.
4. **Revisões só se acrescentam:** comparando com `--base REF` (padrão `HEAD`; no CI, o commit anterior ao push ou a base do PR), é erro remover um registro que tinha revisão, ou remover ou alterar uma revisão já registrada.
5. **Consentimento:** `credito` coerente com `nome_publico` e `descricao_publica` (tabela do passo 2). A revisão precisa ser posterior ao termo e anterior a uma eventual revogação. Também são erro: data no futuro, revisão repetida e revisão em registro `pre_fichamento`.

Avisos que não bloqueiam: registro `fichado` com aprovação vigente (pode passar a `revisado`) e registros retirados por `nao_publicar`.

## Revogação do consentimento

1. Em `data/revisores.json`, preencha `consentimento.revogado_em` e troque `nome_publico` e `descricao_publica` por `null`. As revisões continuam valendo e o site passa a mostrar "revisor/a anônimo/a".
2. Se a pessoa pedir também a **remoção** das revisões, acrescente `"remover_revisoes": true` ao `consentimento`. Só então o validador aceita apagar as entradas dela em `revisoes`. Registros que dependiam só dela voltam a `"fichado"`.

## O que o site mostra

- **Em cada versão revisada:** uma linha por revisão vigente, por exemplo "Revisado por Nome Como Autorizado, iyalorixá, Candomblé Ketu, Salvador (Candomblé Ketu) em 14/02/2027". Contestação e aprovação aparecem lado a lado, sem arbitragem.
- **Selo "Rascunho — aguardando revisão de praticantes e pesquisadores":** continua enquanto houver **alguma** versão da ficha sem revisão vigente. Quando todas estão revisadas, dá lugar ao aviso de ficha revisada. O critério (ficha inteira, e não por atributo) ainda precisa ser confirmado pelo autor ([`PENDENCIAS.md`](../pesquisa/PENDENCIAS.md) §3c).
- **Pendências da ficha:** "N de M versões com revisão vigente".
- **Metodologia e Sobre:** número de versões revisadas, calculado dos dados.
- O `noindex` continua em todas as páginas: publicar para buscadores é decisão do autor.

`scripts/qa_site.py` confere tudo isso no site gerado: linhas de revisão idênticas às esperadas, presença ou ausência do selo, estado em Pendências, crédito não autorizado ausente de todas as páginas e `revisores.json` fora de `/dados/`. `tests/e2e_revisao_site.py` monta numa cópia temporária um cenário sintético (ficha inteira revisada, contestação, `nao_publicar`, revogação, revisão desatualizada), compila o site, roda o QA e confere que o QA acusa adulterações.

## Ainda não implementado (proposta, passos 4–7)

- Página **Créditos** gerada de `revisores.json`, sem os anônimos e sem quem revogou.
- Tipo de fonte `comunicacao_pessoal` (proposta, parte 4), que depende de decisão do autor e mexe no catálogo.
