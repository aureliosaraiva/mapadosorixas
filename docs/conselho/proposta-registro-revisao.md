# Proposta: como registrar a aprovação do conselho nos dados

> **Passos 1–3 implementados em 2026-11-01**, com o gerador e o site já preparados para exibir revisões (parte dos passos 4–6). Ver o passo a passo em [`como-registrar-revisao.md`](como-registrar-revisao.md). Diferença em relação ao texto abaixo: o cadastro ficou em `data/revisores.json`, não em `data/conselho/revisores.json`. Continuam pendentes a página Créditos e a decisão sobre `comunicacao_pessoal` (parte 4). O texto abaixo é a proposta original, mantida como registro.

## Situação atual

- `schemas/fichamento.schema.json`: o `status` já aceita `revisado`, mas não há onde dizer **quem** revisou, **quando** e **para qual tradição**.
- `schemas/orixa.schema.json`: a ficha tem `revisao: [{revisor, data, tradicao, nome_publico, observacoes}]`, no nível da ficha inteira. Hoje é sempre `[]` (`gerar_fichas.py`).
- `schemas/_versao.schema.json`: cada versão leva `status` (`fichado`/`revisado`), mas nenhum detalhe da revisão.

O problema: aprovação no nível da ficha é grossa demais. Um tata de Angola pode aprovar as versões Angola de Ogum e não ter nada a dizer sobre as versões Ketu ou de Umbanda. A regra do projeto (versões lado a lado) pede **aprovação por registro e por tradição**.

## Proposta em 4 partes

### 1. Revisões no registro de fichamento (fonte da verdade)

Novo campo opcional `revisoes` em cada registro de `data/fichamento/<orixa>.json`:

```json
{
  "id": "ogum-012",
  "status": "revisado",
  "revisoes": [
    {
      "revisor_id": "rev-003",
      "data": "2027-02-14",
      "tradicao": "candomble_ketu",
      "parecer": "aprovado",
      "aspectos": ["parafrase", "tradicao", "tom", "publicavel"],
      "hash_registro": "sha256:9f1c…",
      "nota": null
    }
  ]
}
```

| Campo | Valores | Para quê |
|---|---|---|
| `revisor_id` | `rev-NNN` | pseudônimo estável. O nome fica em outro arquivo (parte 2) |
| `data` | ISO 8601 | quando |
| `tradicao` | id de `data/tradicoes.json` | **em nome de qual tradição** a pessoa revisou |
| `parecer` | `aprovado` · `aprovado_com_ressalva` · `contestado` · `nao_publicar` | resultado |
| `aspectos` | subconjunto de `parafrase`, `fonte`, `tradicao`, `tom`, `publicavel` | o que foi de fato conferido. Uma revisão parcial fica explícita |
| `hash_registro` | sha256 de `valor + parafrase + tradicoes + casa_ou_regiao + source_id + localizacao` | se o registro mudar depois, a revisão fica **desatualizada** |
| `nota` | texto ou `null` | ressalva ou motivo da contestação (parafraseado; nunca fundamento) |

**Regras do validador** (`validar_fichamento.py`, a implementar):

1. `status: "revisado"` exige pelo menos uma revisão com `parecer` igual a `aprovado` ou `aprovado_com_ressalva`, **feita em nome de uma tradição que esteja em `tradicoes` do registro** e com `hash_registro` igual ao atual.
2. Se o hash não bater, o registro gera o aviso `revisao_desatualizada` e o `status` volta a ser tratado como `fichado` na geração, até nova revisão.
3. `contestado` **não remove** o registro e não impede `revisado` dado por outra pessoa. A ficha mostra que há contestação (parte 3). Divergência entre revisores fica registrada, sem arbitragem.
4. `nao_publicar`: `gerar_fichas.py` retira o registro da ficha pública e o lista em `pendencias.retidos_ate_conselho`, como já acontece com tabus e alimentos. Só o autor, depois de consultar o conselho, pode reverter.
5. `revisor_id` precisa existir em `data/conselho/revisores.json`.

Por que usar o registro como fonte da verdade: as fichas são **geradas**. Se a aprovação vivesse na ficha, seria apagada a cada regeneração, o que contraria a decisão "Fichas são geradas, não editadas" de `ESTADO.md`.

### 2. Cadastro de revisores com consentimento

Novo arquivo `data/conselho/revisores.json` (público), contendo **apenas** o que o termo de consentimento autoriza ([`kit-revisao.md`](kit-revisao.md) §3):

```json
{
  "id": "rev-003",
  "credito": "nome_e_tradicao",
  "nome_publico": "Nome Como Autorizado",
  "descricao_publica": "iyalorixá, Candomblé Ketu, Salvador",
  "tipo": "praticante",
  "tradicoes": ["candomble_ketu"],
  "consentimento": { "versao_termo": "1.0", "data": "2027-02-01", "revogado_em": null }
}
```

- `credito`: `nome_e_tradicao` · `so_nome` · `generico` · `anonimo`. Com `anonimo`, `nome_publico` e `descricao_publica` ficam `null`, e o site mostra só "revisor/a de [tradição]".
- `tipo`: `praticante` · `pesquisador` · `ambos`.
- **Não guardar** e-mail, telefone, endereço nem o termo assinado. Isso fica **fora do repositório**, com o autor. A ligação entre `rev-NNN` e a pessoa real, no caso dos anônimos, também fica fora do repo.
- **Revogação:** preencher `revogado_em` e zerar `nome_publico`/`descricao_publica`. As revisões continuam válidas como anônimas, salvo pedido contrário. Se a pessoa pedir, as revisões dela são removidas, e os registros que dependiam só dela voltam a `fichado`.

### 3. O que é gerado na ficha e na versão

`gerar_fichas.py` passaria a copiar para cada versão um resumo sem dados pessoais:

```json
"revisoes": [
  { "tradicao": "candomble_ketu", "data": "2027-02-14", "parecer": "aprovado", "revisor": "rev-003" }
]
```

E o campo `revisao` da ficha (`orixa.schema.json`), que já existe, seria **gerado** como agregado: uma entrada por revisor e tradição, com a data mais recente. A sugestão é trocar `revisor` (texto livre) por `revisor_id` e remover `nome_publico` desse ponto, porque o nome vem de `revisores.json`. Essa é a única mudança incompatível com o esquema atual.

O site mostraria:
- na versão: selo "revisado por [crédito] ([tradição], [data])" ou "contestado por revisor/a de [tradição]: [nota]";
- na ficha: o selo "Rascunho" só sai quando **todas** as versões publicadas tiverem pelo menos uma revisão válida. Critério a confirmar com o autor; a alternativa é tirar o selo por atributo.
- página **Créditos**: lista gerada de `revisores.json`, sem os anônimos e sem quem revogou.

### 4. Versões vindas do próprio revisor

Quando o revisor traz uma versão da sua casa sem fonte publicada ([`kit-revisao.md`](kit-revisao.md) §1.5, item 3), há duas opções. Fica para decisão do autor:

- **(a)** Criar o tipo `comunicacao_pessoal` em `fonte.schema.json`. Seria uma entrada no catálogo do tipo `pc-rev-003-2027`, com `confiabilidade_preliminar` própria e o crédito controlado por `revisores.json`. Isso mexe em `catalogo.json`, que só uma sessão por vez pode editar.
- **(b)** Não aceitar comunicação pessoal como fonte e registrar a informação só como `nota` no registro contestado.

A recomendação é **(a)**, com um limite: comunicação pessoal sustenta apenas a versão **daquela casa** (`casa_ou_regiao` obrigatório) e nunca uma afirmação geral sobre a nação.

## Impacto e ordem de implementação

1. `schemas/fichamento.schema.json`: adicionar `revisoes` (opcional; não quebra nada).
2. Novo `schemas/revisor.schema.json` e `data/conselho/revisores.json` (vazio).
3. `validar_fichamento.py`: regras 1 a 5.
4. `gerar_fichas.py`: copiar o resumo para as versões, gerar `revisao` da ficha e tratar `nao_publicar`.
5. `orixa.schema.json` e `_versao.schema.json`: ajustar `revisao` e incluir `revisoes`.
6. Site: selos e página de Créditos.
7. Se for adotada a opção 4(a): tipo `comunicacao_pessoal` no catálogo.

Os passos 1 a 3 podem ser feitos antes do primeiro revisor aceitar. Os passos 4 a 6, quando houver a primeira revisão real.
