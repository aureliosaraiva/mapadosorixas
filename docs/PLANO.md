# Plano do projeto — Enciclopédia interativa dos Orixás

> Documento vivo. Base: `CLAUDE.md`. Última revisão: 2026-10-31.

## 0. Visão, princípios e definição de pronto

**Visão.** Ser a referência aberta, organizada e com fontes citadas sobre orixás (e equivalentes: voduns, inquices, orishas lucumí, òrìṣà iorubás), que mostra as divergências entre tradições em vez de apagá-las.

**Princípios inegociáveis** (derivados das regras de conteúdo do `CLAUDE.md`):

1. **Fonte por afirmação.** Nenhum campo factual entra numa ficha sem pelo menos uma referência no catálogo de fontes (`source_id`).
2. **Paráfrase sempre.** Nunca transcrever trechos de livros. Citações literais só de domínio público, curtas e marcadas.
3. **Pluralidade explícita.** Divergências registradas lado a lado, com nação/casa/região/autor, sem eleger uma versão "correta".
4. **Respeito e sigilo.** Não publicar fundamentos iniciáticos (awo, segredos de feitura, ebós específicos, rezas restritas). Na dúvida, não publicar e perguntar ao conselho consultivo.
5. **Candomblé ≠ Umbanda ≠ Santería ≠ culto iorubá.** Toda informação é etiquetada com a tradição a que se refere.
6. **Revisão humana antes de publicar.** Praticantes (babalorixás/iyalorixás, tatas, doné/hunbonos, olorishas, babalawos) e/ou pesquisadores.
7. **Rastreabilidade.** Dados em JSON versionados no Git; toda mudança de conteúdo passa por PR com revisão.

**O MVP está pronto quando:** 5 fichas (Exu, Ogum, Oxóssi, Xangô, Iemanjá) revisadas por ≥1 praticante e ≥1 pesquisador; catálogo com filtros; grafo funcional; página de metodologia; deploy público em domínio próprio; 100% dos campos factuais com fonte.

---

## Fase 1 — Levantamento e catalogação de TODA a informação disponível (qualquer idioma)

Esta é a fase fundadora. O objetivo não é ainda escrever fichas, e sim **construir um catálogo bibliográfico e um fichamento estruturado** do que existe — livros, artigos, teses, acervos, sites, vídeos, registros de patrimônio — em português, espanhol, inglês, francês, iorubá, fon, alemão, italiano e outros idiomas onde houver material relevante.

### 1.1 Objetivos

| # | Objetivo | Entregável |
|---|----------|-----------|
| O1 | Inventariar fontes sobre orixás e equivalentes em todas as tradições e idiomas | `data/fontes/*.json` (catálogo de fontes) |
| O2 | Classificar cada fonte por tipo, tradição, idioma, confiabilidade e acesso | Campos padronizados no catálogo |
| O3 | Mapear autores, instituições, acervos e pesquisadores ativos | `data/fontes/autores.json`, `docs/pesquisa/acervos.md` |
| O4 | Extrair e fichar atributos por orixá com origem (fonte + página) | `data/fichamento/<orixa>.json` |
| O5 | Registrar divergências já na coleta | Campo `divergencias` no fichamento |
| O6 | Identificar lacunas (tradições/orixás pouco documentados) | `docs/pesquisa/lacunas.md` |
| O7 | Identificar potenciais revisores e parceiros | `docs/pesquisa/contatos.md` (privado se tiver dados pessoais) |

### 1.2 Escopo da coleta

**Tradições a cobrir (cada fonte é etiquetada com uma ou mais):**

- **África Ocidental**: culto iorubá aos òrìṣà (Nigéria, Benim, Togo) — incluindo o corpus de Ifá; culto fon/ewe aos vodun (Benim, Togo, Gana).
- **África Central**: religiosidade bakongo/ambundu (base dos inquices bantos).
- **Brasil — Candomblé**: Ketu/Nagô, Jeje (Mahi, Savalu, Mina-Jeje), Angola/Congo (Bantu), Ijexá, Efon; Xangô de Pernambuco (Nagô do Recife); Tambor de Mina (MA); Batuque (RS); Xambá.
- **Brasil — Umbanda** e Omolocô (etiquetadas separadamente).
- **Cuba e diáspora hispânica**: Regla de Ocha / Santería / Lucumí, Regla de Ifá, Palo Monte (equivalências bantas), Arará (equivalências jeje).
- **Outras Américas**: Orisha de Trinidad e Tobago (Shango Baptists), Vodou haitiano (lwa nagô/rada), Venezuela, Uruguai/Argentina (Batuque/Umbanda rio-platense), EUA (Oyotunji, Lucumí nos EUA).
- **Sincretismo católico** (por região: Bahia, Rio, Recife, RS, Cuba).

**Tipos de fonte:**

| Código | Tipo | Exemplos |
|--------|------|---------|
| `etno_classica` | Etnografia clássica (1890–1970) | Nina Rodrigues, Arthur Ramos, Edison Carneiro, Bastide, Verger, Lydia Cabrera, Fernando Ortiz |
| `academica` | Livros e artigos acadêmicos recentes | Parés, Matory, Prandi, Olupona, Brown |
| `tese` | Teses e dissertações | BDTD, Catálogo CAPES, ProQuest, theses.fr |
| `corpus_oral` | Registros de tradição oral e Ifá publicados | Abimbola, Bascom, Salami |
| `praticante` | Obras escritas por sacerdotes/as | Mãe Stella de Oxóssi, Mestre Didi, José Beniste |
| `enciclopedia` | Dicionários e enciclopédias | Cacciatore, Nei Lopes, Oxford Research Encyclopedia |
| `acervo` | Museus, arquivos, coleções digitais | Museu Afro Digital UFBA, Fundação Pierre Verger, Museu Afro Brasil |
| `patrimonio` | Registros oficiais | IPHAN (tombamentos de terreiros), UNESCO (Ifá; Bosque Sagrado de Osun-Osogbo) |
| `web_divulgacao` | Sites/blogs de divulgação | Wikipédia (todas as línguas), portais de terreiros |
| `audiovisual` | Documentários, cantigas gravadas, podcasts | Acervos sonoros, YouTube de casas tradicionais |
| `iconografia` | Arte e imagem | Carybé, Verger (fotos), arte iorubá em museus |

**Fora de escopo:** conteúdo comercial de "trabalhos", sites de venda de serviços espirituais, material que exponha fundamentos secretos.

### 1.3 Estratégia de busca

#### Bases e repositórios (por prioridade)

1. **Catálogos bibliográficos**: WorldCat, Biblioteca Nacional (BN Digital, Hemeroteca), Biblioteca Nacional de España, BnF/Gallica, Library of Congress, Open Library.
2. **Acadêmicas**: Google Scholar, SciELO, Redalyc, Dialnet (es), CAIRN/Persée/OpenEdition (fr), JSTOR, Project MUSE, Semantic Scholar, OpenAlex, CORE.
3. **Teses**: BDTD (IBICT), Catálogo de Teses CAPES, repositórios USP/UFBA/UNICAMP/UNESP/UFPE/UFRGS/UFMA, ProQuest Dissertations, theses.fr, EThOS (UK), repositórios da Universidade de Ibadan e Obafemi Awolowo (Ilé-Ifẹ̀).
4. **Periódicos-chave**: *Afro-Ásia* (UFBA), *Revista de Antropologia* (USP), *Religião & Sociedade*, *Debates do NER* (UFRGS), *Revista Brasileira de História das Religiões*, *Horizonte* (PUC Minas), *Journal of Religion in Africa*, *Research in African Literatures*, *African Arts*, *Journal de la Société des Africanistes*, *Cahiers d'Études Africaines*, *Catauro* e *Del Caribe* (Cuba), *Journal of Africana Religions*.
5. **Domínio público / livros digitalizados**: Internet Archive, HathiTrust, Google Books, Domínio Público (MEC), Biblioteca Brasiliana Guita e José Mindlin (USP).
6. **Acervos**: Museu Afro Digital UFBA, Fundação Pierre Verger, Museu Afro Brasil, CEAO/UFBA, Museu Nacional (perdas do incêndio de 2018 — checar coleções remanescentes), Smithsonian NMAfA, British Museum, Musée du quai Branly, Casa de África (Havana), Fundación Fernando Ortiz.
7. **Patrimônio**: IPHAN (processos de tombamento: Casa Branca do Engenho Velho, Gantois, Ilê Axé Opô Afonjá, Alaketu, Bate Folha, Casa das Minas etc.), UNESCO (Sistema de adivinhação Ifá — patrimônio imaterial; Bosque Sagrado de Osun-Osogbo — patrimônio mundial).
8. **Web aberta**: Wikipédia em pt/es/en/fr/yo/de/it (usar sobretudo as referências, não o texto), Wikidata (identificadores e equivalências), sites de terreiros tradicionais, portais acadêmicos de divulgação.

#### Strings de busca por idioma (modelo; expandir por orixá)

| Idioma | Exemplos |
|--------|----------|
| pt | `orixá*`, `candomblé ketu`, `candomblé jeje vodum`, `candomblé angola inquice`, `itã`, `"<Ogum>" candomblé`, `sincretismo orixá santo` |
| es | `oricha*`, `orisha*`, `santería lucumí`, `regla de ocha`, `pataki*`, `"Changó"`, `"Yemayá"`, `regla de palo nkisi` |
| en | `orisha*`, `òrìṣà`, `Yoruba religion`, `Ifa divination corpus`, `Candomblé`, `Lucumí`, `"Ogun" Yoruba` |
| fr | `orisha`, `òrìṣà`, `vodun`, `culte des orisha`, `religion yoruba`, `candomblé` |
| yo | `òrìṣà`, `ẹsẹ Ifá`, `oríkì <òrìṣà>`, `ìtàn` (com e sem diacríticos) |
| de | `Orisha Religion`, `Yoruba Götter`, `Candomblé` |
| it | `orisha`, `religione yoruba`, `candomblé` |

Variantes de grafia por orixá entram no catálogo de nomes (ex.: Exu / Èṣù / Eshu / Elegguá / Elegbara / Legba; Xangô / Ṣàngó / Changó / Shango; Iemanjá / Yemọja / Yemayá / Yemoja).

### 1.4 Esquema do catálogo de fontes

Cada fonte é um objeto JSON (compatível com CSL-JSON para gerar citações automaticamente):

```json
{
  "id": "verger-1981-orixas",
  "tipo": "livro",
  "categoria": "etno_classica",
  "autores": [{ "familia": "Verger", "dado": "Pierre Fatumbi" }],
  "titulo": "Orixás: deuses iorubás na África e no Novo Mundo",
  "titulo_original": "Orisha: les dieux yorouba en Afrique et au Nouveau Monde",
  "ano": 1981,
  "ano_original": 1982,
  "editora": "Corrupio",
  "local": "Salvador",
  "idioma": "pt",
  "idiomas_traducoes": ["fr", "pt"],
  "isbn": null,
  "doi": null,
  "url": null,
  "acesso": "comercial",
  "dominio_publico": false,
  "tradicoes": ["ioruba_nigeria", "candomble_ketu", "benim"],
  "orixas": ["exu", "ogum", "oxossi", "xango", "iemanja"],
  "temas": ["itans", "simbolos", "culto", "fotografia"],
  "confiabilidade": "A",
  "perspectiva": "pesquisador-iniciado",
  "observacoes": "Autor foi iniciado (babalaô); combina pesquisa de campo na Bahia e no Benim/Nigéria.",
  "status_verificacao": "verificado",
  "verificado_em": "2026-11-05",
  "verificado_por": "nome"
}
```

**Campos obrigatórios:** `id`, `tipo`, `autores`, `titulo`, `ano`, `idioma`, `tradicoes`, `confiabilidade`, `status_verificacao`.

**Convenção de `id`:** `sobrenome-ano-palavrachave` (minúsculas, sem acentos).

### 1.5 Rubrica de confiabilidade

| Nível | Critério | Uso nas fichas |
|-------|----------|----------------|
| **A** | Pesquisa acadêmica revisada por pares, etnografia de campo documentada, corpus oral publicado com metodologia, obra de sacerdote/a reconhecido/a | Pode sustentar sozinha uma afirmação |
| **B** | Obra de divulgação séria com bibliografia; dicionários especializados; registros oficiais (IPHAN, UNESCO) | Sustenta afirmação, de preferência com outra fonte |
| **C** | Sites de terreiros, entrevistas, enciclopédias gerais, Wikipédia | Só como indicação de prática corrente; exige fonte A/B ou marcação "relato de casa" |
| **D** | Blogs sem autoria, conteúdo comercial | Não citar; serve só para descobrir pistas |

**Alertas de viés a anotar no campo `observacoes`:** olhar colonial/evolucionista (ex.: Ellis 1894, Nina Rodrigues), "nagocentrismo" (crítica de Beatriz Góis Dantas e outros à ideia de pureza nagô), apropriação, recorte de uma única casa generalizado como regra.

### 1.6 Fichamento estruturado (extração de informação)

Além do catálogo, cada leitura gera registros atômicos:

```json
{
  "orixa": "ogum",
  "atributo": "dia_da_semana",
  "valor": "terça-feira",
  "tradicao": "candomble_ketu",
  "casa_ou_regiao": "Bahia (genérico)",
  "source_id": "verger-1981-orixas",
  "localizacao": "p. 86",
  "parafrase": "Resumo com palavras próprias...",
  "nota": null
}
```

Atributos-padrão: nomes/grafias, origem geográfica (cidade/região na África), domínios, elementos, cores, dia da semana, saudação, símbolos/ferramentas, alimentos (genérico, sem receita ritual), animais associados (genérico), qualidades/caminhos, parentesco nos itãs, equivalências (vodun/inquice/orisha lucumí/lwa), sincretismo católico, itãs (resumo parafraseado + fonte), tabus públicos conhecidos.

A partir dos registros, gera-se automaticamente a **matriz de divergências** (mesmo orixá + mesmo atributo + valores diferentes).

### 1.7 Processo e ferramentas

1. **Zotero (biblioteca de grupo)** como ferramenta de coleta e anexos privados (PDFs não vão para o repo).
2. Exportação periódica Zotero → CSL-JSON → script que normaliza para `data/fontes/`.
3. **Validação automática** (JSON Schema + CI): campos obrigatórios, ids únicos, todo `source_id` do fichamento existe no catálogo.
4. **Planilha de triagem** (opcional) para pistas ainda não verificadas.
5. **Pesquisa assistida por IA**: agentes podem varrer bases e propor entradas, mas **toda entrada nasce com `status_verificacao: "a_verificar"`** e só muda após conferência humana em catálogo (WorldCat/ISBN/DOI) ou no próprio documento.

**Fluxo de uma fonte:** `pista` → `a_verificar` → `verificado` (metadados conferidos) → `fichado` (atributos extraídos) → `revisado` (segunda pessoa conferiu o fichamento).

### 1.8 Direitos autorais e ética na coleta

- PDFs de obras protegidas ficam fora do repositório (só metadados e paráfrase).
- Imagens: só domínio público, licença aberta (CC) ou autorização escrita; registrar licença por imagem.
- Material de terreiros: pedir autorização antes de citar conteúdo de sites ou redes de casas específicas.
- Entrevistas com praticantes: termo de consentimento; anonimizar se pedido.

### 1.9 Sub-etapas e cronograma sugerido (Fase 1)

| Semana | Atividade | Saída |
|--------|-----------|-------|
| 1 | Configurar Zotero, JSON Schema, script de validação; carregar catálogo-semente (`data/fontes/catalogo-semente.json`) | Infra de catalogação |
| 2–3 | Verificar o catálogo-semente; varrer catálogos (WorldCat, BN, BnF, BNE) e Wikipédia multilíngue (referências) | ~150 fontes `a_verificar` |
| 3–4 | Varredura acadêmica (Scholar, SciELO, Redalyc, Dialnet, JSTOR, CAIRN) e teses (BDTD, CAPES, ProQuest, theses.fr) | ~300 fontes; lista de periódicos |
| 4–5 | Acervos, patrimônio, audiovisual; Cuba/Trinidad/Haiti/Nigéria/Benim | `acervos.md`, cobertura por tradição |
| 5–7 | Fichamento dos 5 orixás do MVP em ≥8 fontes A/B cada, cobrindo ≥3 tradições | `data/fichamento/*.json` |
| 7–8 | Matriz de divergências, relatório de lacunas, lista de revisores | Relatório da Fase 1 |

**Critérios de aceite da Fase 1:**
- ≥ 200 fontes verificadas, em ≥ 4 idiomas, cobrindo todas as tradições listadas em 1.2.
- Para cada orixá do MVP: ≥ 8 fontes A/B, ≥ 3 tradições, todos os atributos-padrão com ao menos uma fonte ou marcados como lacuna.
- Relatório `docs/pesquisa/relatorio-fase1.md` com estatísticas, lacunas e vieses identificados.

---

## Fase 2 — Modelo de dados

Arquivos em `data/` (JSON, validados por JSON Schema em `schemas/`):

| Arquivo | Conteúdo |
|---------|----------|
| `orixas/<id>.json` | Ficha: nomes por tradição, origem, domínios, elementos, cores, dia, saudação, símbolos, sincretismo, itãs (resumos), divergências, `sources` |
| `tradicoes.json` | Nações/tradições: Ketu, Jeje, Angola, Ijexá, Efon, Xangô-PE, Mina, Batuque, Umbanda, Lucumí, Arará, Palo, Ioruba-NG, Vodun-BJ, Vodou-HT, Orisha-TT |
| `entidades_equivalentes.json` | Voduns, inquices, orishas lucumí, lwa — cada um com ficha leve |
| `conexoes.json` | Arestas tipadas: `parentesco` (pai/mãe/filho/irmão/cônjuge, por itã), `equivalencia`, `sincretismo`, `rivalidade`, `companheiro_de_culto`; cada aresta com `tradicao` e `sources` |
| `fontes/*.json` | Catálogo da Fase 1 |
| `glossario.json` | Termos (axé, itã, odu, orí, ebó...) com fonte |
| `i18n/` | Textos traduzidos (pt-BR base; es; en) |

**Regra estrutural:** qualquer valor factual é `{ "valor": ..., "tradicao": [...], "sources": [{ "id": ..., "loc": ... }] }`. Um atributo pode ter vários valores (é assim que divergências aparecem).

**Validações no CI:** schema; `source_id` existente; toda aresta com fonte; nenhum campo factual sem fonte; detector de trechos longos idênticos a textos de referência (anti-cópia simples, ex.: n-gramas comparados com citações registradas).

---

## Fase 3 — Curadoria de conteúdo do MVP (5 orixás)

Para cada um de Exu, Ogum, Oxóssi, Xangô e Iemanjá:

1. Consolidar o fichamento em ficha (`data/orixas/<id>.json`).
2. Redigir resumos de itãs parafraseados (2–5 por orixá), cada um com fonte e tradição.
3. Preencher a seção de divergências (ex.: Iemanjá — rio Ògùn na Nigéria vs. mar no Brasil; Exu — orixá vs. "exus" da Umbanda; sincretismos diferentes por estado).
4. Tabela de equivalências (ex.: Exu ↔ Legba (fon) ↔ Aluvaiá/Pambu Njila (banto) ↔ Elegguá/Eshu (lucumí)), sempre com fonte e com a ressalva de que equivalência ≠ identidade.
5. Checklist editorial: tom, sigilo, paráfrase, etiqueta Candomblé/Umbanda.

---

## Fase 4 — Revisão por praticantes e pesquisadores

- **Conselho consultivo** (meta: 3–6 pessoas): ≥2 sacerdotes/as de nações diferentes (ex.: Ketu e Angola/Jeje), ≥1 pesquisador/a acadêmico/a, idealmente ≥1 olorisha lucumí para a versão em espanhol.
- **Fluxo**: ficha em PR → link de pré-visualização → comentários → ajustes → aprovação registrada no campo `revisao` da ficha (quem, quando, tradição; com consentimento para nome público).
- Política para divergência de revisores: registrar ambas as versões, não escolher.
- Canal público de correção ("sugerir correção" em cada ficha → issue no GitHub ou formulário).

---

## Fase 5 — Site estático

**Recomendação de stack:** **Astro** (geração estática, conteúdo em JSON, i18n nativo, ótimo SEO) + **Cytoscape.js** para o grafo (layouts prontos, filtros por tipo de aresta, melhor para redes do que D3 puro) + **Pagefind** para busca estática + deploy em **Cloudflare Pages** (ou GitHub Pages) a partir do `main`.

**Páginas:**
1. **Início** — proposta, acesso a catálogo/grafo/metodologia.
2. **Catálogo** — cards com filtros (tradição, elemento, domínio, região de origem, dia, cor) e busca.
3. **Ficha** — seções do `CLAUDE.md`, cada afirmação com nota de rodapé clicável para a fonte; bloco "Divergências" com tabela por tradição; mini-grafo local.
4. **Grafo** — rede completa; filtros por tipo de conexão e tradição; clique abre ficha; legenda acessível.
5. **Fontes** — bibliografia completa com filtros (idioma, tipo, ano, confiabilidade).
6. **Metodologia e limitações** — tradição oral, variação entre casas, ausência de panteão único, critérios de fonte, sigilo, conselho, como contribuir.
7. **Glossário** e **Sobre/Créditos**.

**Requisitos não funcionais:** acessibilidade WCAG 2.1 AA (alternativa em lista/tabela ao grafo), funciona sem JS para conteúdo textual, mobile-first, Lighthouse ≥ 90, dados abertos para download (JSON + licença).

**Licenças sugeridas:** código MIT; textos próprios CC BY-SA 4.0; dados CC BY 4.0 — a confirmar com o conselho (há quem prefira restringir uso comercial: CC BY-NC-SA).

---

## Fase 6 — Lançamento do MVP

- Registro de domínio: preferir `.org` ou `.com` (autor mora na Espanha; `.com.br` exige CPF/CNPJ). Verificar disponibilidade de `atlasdosorixas.org`, `enciclopediaorixas.org`, `orixas.wiki`, `orixas.info`.
- Checklist: todas as fichas revisadas, página de metodologia publicada, links de fonte funcionando, analytics respeitoso (Plausible/Cloudflare, sem cookies), página de contato/correção.
- Divulgação: universidades (CEAO/UFBA, NER/UFRGS, CERU/USP), terreiros parceiros, comunidades lucumí, redes acadêmicas.

---

## Fase 7 — Expansão

1. **~15 orixás** cultuados no Brasil: + Oxum, Iansã/Oyá, Obaluaê/Omolu, Nanã, Oxumarê, Ossaim, Logun Edé, Obá, Ewá, Oxalá (Oxalufã/Oxaguiã), Ibeji, Iroko/Tempo (escolha final com o conselho).
2. **Voduns e inquices** como fichas próprias (não só como equivalências).
3. **Espanhol** (prioridade: público da Santería/Lucumí, com terminologia lucumí revisada por olorishas) e depois **inglês**.
4. Linha do tempo histórica (tráfico, fundação das casas, perseguição, tombamentos).
5. Mapa geográfico (origem na África ↔ difusão nas Américas).

---

## Governança, riscos e métricas

### Riscos

| Risco | Mitigação |
|-------|-----------|
| Exposição de conteúdo sigiloso | Princípio 4; revisão pelo conselho; lista de temas proibidos |
| Cópia involuntária de livros | Paráfrase obrigatória, revisão em par, verificação de n-gramas |
| Tomar uma casa como regra geral | Etiqueta de tradição/casa obrigatória em cada valor |
| Erros de metadados gerados por IA | `status_verificacao`; nenhuma fonte "a_verificar" pode sustentar ficha publicada |
| Intolerância religiosa / ataques | Moderação, sem comentários abertos, contato por formulário |
| Baixa adesão de revisores | Começar com rede próxima; crédito público; respeitar o tempo e, se possível, remunerar |
| Escopo excessivo | MVP fechado em 5 orixás; expansão só após lançamento |

### Métricas

- Cobertura: % de campos com ≥2 fontes A/B; nº de tradições por ficha.
- Qualidade: nº de correções aceitas; tempo de resposta a correções.
- Uso: visitas, tempo em ficha, uso do grafo, downloads dos dados.

### Estrutura de repositório proposta

```
/data
  /fontes          catálogo de fontes (Fase 1)
  /fichamento      registros atômicos por orixá (Fase 1)
  /orixas          fichas consolidadas (Fase 3)
  tradicoes.json  conexoes.json  glossario.json
/schemas           JSON Schemas
/scripts           validação, importação Zotero, matriz de divergências
/docs
  PLANO.md
  /pesquisa        protocolo, acervos, lacunas, relatórios
/site              projeto Astro
```

## Próximos passos imediatos

1. Aprovar este plano (ou ajustar escopo/cronograma).
2. Criar `schemas/fonte.schema.json` e `schemas/fichamento.schema.json` + script de validação.
3. Verificar o catálogo-semente (`data/fontes/catalogo-semente.json`) — todas as entradas estão marcadas como `a_verificar`.
4. Iniciar a varredura sistemática da seção 1.3, começando por WorldCat + Google Scholar + Wikipédia multilíngue.
5. Começar a montar a lista de potenciais revisores.
