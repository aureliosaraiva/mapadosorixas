# Ilustrações 01 — uma ilustração simbólica por orixá

**Sessão:** ilustra (trabalhadora, coordenada pela orquestradora), 2026-11-02.
**Pedido do autor:** uma ilustração de boa qualidade para cada orixá com ficha/capítulo e, se fizer sentido, para as entidades da cosmologia.
**Resultado:** 22 ilustrações (17 orixás + Orum, Aiê, Odudua, Olokun e Orí), no topo da página de cada um, no cartão do catálogo e na abertura do capítulo. Sem ilustração: Iyami (tema sensível), Ewá (sem símbolos fichados), Olodumare e Egungun (motivos em §4). `data/fichamento/`, capítulos, catálogo e itãs **não foram tocados**.

## 1. Critérios

1. **Emblema, não retrato.** Nenhum rosto ou corpo de divindade, nenhuma cena de culto, transe, dança ou ritual. Cada ilustração é uma composição de objetos, plantas, paisagens e sinais (ferramentas, emblemas, águas, árvores, céu).
2. **Só o que está fichado.** Todo elemento desenhado tem pelo menos um registro com status `fichado` em `data/fichamento/` (atributos `simbolos`, `elementos`, `dominios`, `iconografia`; em alguns casos `itans`, `hierarquia` ou `funcoes`, quando o elemento só aparece ali). `data/ilustracoes.json` lista, para cada elemento, os ids que o sustentam; o QA confere que existem e estão fichados. Detalhes que as fontes não dão ficaram de fora ou foram desenhados de modo genérico, sem afirmar nada (ex.: o número de varetas do chachará, de contas do opelê ou de búzios em Orí é só gráfico, e isso está anotado).
3. **Cores sem "cor oficial".** Base na paleta do site (papel quente, traço da página, tom claro de "metal"). **No máximo um acento**, e só quando a cor aparece em **mais de uma tradição** nos registros de `cores`: verde (Ogum, Oxóssi), vermelho (Exu, Xangô, Iansã), azul (Iemanjá), ouro (Oxum), violeta (Nanã). Nos demais, sem acento de cor do orixá: o ocre do site aparece só como cor de material (palha, barro, terra, folhas, nozes). A justificativa e os registros de cor estão em `data/ilustracoes.json`. Em Exu, o preto não entra para não reforçar a leitura demonizada que as fontes discutem.
4. **Evitar estereótipo.** Nada de exotismo, caricatura ou figuras "tribais". Em Exu ficaram fora o tridente, chifres e falo (imagens da leitura europeia e da associação ao diabo, que as fontes registram e criticam); em Omolu, a figura coberta de palha (só a palha como material); em Ibeji, as estatuetas (só motivos abstratos e os três pratinhos de barro).

## 2. Técnica

- **SVG vetorial desenhado em código**, sem imagens de terceiros, bancos de imagem ou obras de referência: `site/scripts/ilustracoes/desenhos.py` (uma função por entidade, coordenadas escritas à mão, com geometria calculada onde ajuda: leques, anéis, ondas) e `base.py` (medalhão comum). `gerar.py` grava `site/src/assets/ilustracoes/<id>.svg` usando o texto alternativo de `data/ilustracoes.json`.
- **Estilo coeso:** medalhão 200×200 com disco, dois anéis e uma coroa de pontos (o mesmo vocabulário de círculos concêntricos da capa), traço arredondado de espessura constante, tom claro para metais e objetos, um acento.
- **Claro e escuro:** o traço é `currentColor`; fundo, anéis, tom claro e acentos usam variáveis `--il-*` definidas em `global.css` para os dois temas (com valores de reserva no próprio SVG, para o arquivo solto).
- **Acessibilidade:** cada SVG tem `role="img"` e `<title>` com id único, ligado por `aria-labelledby`; o texto alternativo descreve o que se vê ("Ilustração simbólica de Ogum: emblema de ferro com sete pontas…"). Na página e no capítulo vai dentro de `<figure>` com a legenda "Ilustração simbólica inspirada nos elementos descritos nas fontes"; no catálogo, um parágrafo acima da grade explica que as imagens são ilustrações simbólicas, nunca retratos.
- **Peso:** 3–10 KB por SVG, inline (sem pedido extra). O svgo não estava instalado no ambiente; o gerador já escreve números com uma casa decimal e sem atributos redundantes. Fica como melhoria opcional.
- **Revisão de qualidade:** 3 pilotos (Ogum, Iemanjá, Xangô) renderizados em PNG (claro/escuro, 320 px e 72 px) por `site/scripts/ilustracoes/renderizar.cjs` e revistos antes da série; cada lote seguinte também foi renderizado e corrigido (ex.: em Ogum as folhas brigavam com o leque e o centro parecia um sol; em Xangô o raio era cortado pela borda; em Oxumarê as cabeças de serpente ficaram caricatas e viraram pontas estilizadas; em Exu o montículo parecia um cogumelo).

## 3. Elementos por ilustração

| Entidade | Elementos (registros) | Acento | Observações / o que ficou de fora |
|---|---|---|---|
| **Ogum** | emblema de ferro com sete pontas (ogum-022, ogum-016); espada-de-ogum (Sansevieria) (ogum-023, ogum-027, ogum-042); mariô (ogum-041) | verde | — |
| **Iemanjá** | lua crescente com estrela (emblema; metal: prata) (iemanja-021); águas do mar (iemanja-014, iemanja-017, iemanja-010); otá: seixo marítimo (iemanja-024) | azul | — |
| **Xangô** | oxê (machado) (xango-025); raio (xango-018, xango-020, xango-023, xango-044); otá: pedra de raio; matéria: pedra (xango-033, xango-025) | vermelho | — |
| **Exu** | encruzilhada, caminhos (exu-033, exu-053, exu-058, exu-061); laterita (suporte do culto na África Ocidental) (exu-051); búzios (exu-051, exu-007) | vermelho | Tridente/garfo (exu-025) e figuras com chifres ou falo (exu-004, exu-017, exu-043, exu-051) ficaram de fora: são as imagens da leitura europeia e da associação ao diabo que as fontes registram e discutem (exu-002, exu-005, exu-016, exu-029, exu-077); o montículo é desenhado baixo, sem forma humana nem fálica. |
| **Oxóssi** | arco e flecha (oxossi-014); eruquerê (espanta-moscas de rabo de boi, atributo real) (oxossi-014); mata, floresta (oxossi-011, oxossi-012) | verde | — |
| **Oxum** | abebé (leque); metal ouro ou latão (oxum-007, oxum-036); águas doces: rios, cachoeiras, fontes (oxum-004, oxum-031, oxum-042, oxum-051); otá: seixo liso tirado do leito de um rio (oxum-008) | ouro | — |
| **Iansã** | ventos, ventania, tempestade (iansa-005, iansa-022, iansa-032, iansa-039); relâmpago / centelha (iansa-005, iansa-022, iansa-039); espada (com que imita o relâmpago); armas (iansa-005, iansa-027) | vermelho | Os mortos e o cemitério (iansa-006, iansa-022) não foram figurados, para não aproximar a imagem do culto aos mortos. |
| **Nanã** | chachará: feixe de varetas amarradas (nana-016); águas das chuvas e do dilúvio (nana-023) | violeta | A ligação com a morte e os ritos fúnebres (nana-013, nana-030) não foi figurada; o número de varetas é só gráfico (as fontes não o dão). |
| **Omolu / Obaluaê** | palha (matéria) (omolu-035, omolu-010); xaxará: feixe de varetas, vassoura (omolu-012, nana-016); otá cheio de buraquinhos (omolu-013); terra (Sakpata-Omolu como 'rei da terra') (omolu-006) | neutro (ocre do site) | A figura coberta de palha, o rosto marcado e a dança (omolu-010, omolu-011, omolu-029) não foram desenhados: são retrato e cena de culto. Doença e cemitério (omolu-005, omolu-007) não foram figurados. |
| **Oxalá** | cabaça dupla: duas metades encaixadas, céu e terra (oxala-011); céu, abóbada celeste (oxala-006, oxala-044); pomba no alto do emblema (oxala-046); paxorô (vara de metal) (oxala-012); algodão (oxala-046, oxala-032) | neutro (ocre do site) | A pomba fica acima da cabaça, sem afirmar que o emblema e o paxorô sejam o mesmo objeto (as fontes falam deles separadamente). |
| **Ossaim** | ferro de Ossaim: haste pontuda cravada no chão, pássaro no alto, ramos em leque (ossaim-020, ossaim-021, ossaim-023); ervas, folhas, mato selvagem (ossaim-001, ossaim-002, ossaim-003, ossaim-004) | neutro (ocre do site) | Seis ramos seguem Sallum & Silva ('muitas vezes seis', ossaim-023); Bastide fala em sete (ossaim-020). A figura de um olho e uma perna (ossaim-030, ossaim-032) não foi desenhada. |
| **Oxumarê** | arco-íris que liga céu e terra (oxumare-003, oxumare-011, oxumare-022); serpente; dois bastões de ferro que figuram cobras (oxumare-026, oxumare-011, oxumare-022) | neutro (ocre do site) | — |
| **Logunedé** | pena de ave de caça (sinal do pai) (logunede-006); ofá (logunede-018); abebé (logunede-018) | neutro (ocre do site) | — |
| **Obá** | as nuvens revoltas que se encontram (oba-016); o rio Oba (oba-011) | neutro (ocre do site) | A dança com a mão sobre a orelha e o itã da orelha cortada (oba-003, oba-004) não foram figurados: são cena de culto e corpo. |
| **Iroko / Tempo** | a gameleira, adorada como Iroko (iroko-001); entre as divindades que ligam céu e terra; reino da vegetação (iroko-005, iroko-006) | neutro (ocre do site) | A árvore como morada de antepassados (iroko-009) é depoimento único e não foi figurada; nenhum pano ou oferenda junto à árvore, por não estar fichado. |
| **Ibeji** | divindade tutelar dos gêmeos (ibeji-027, ibeji-036); um terceiro personagem menor entre os dois (Doú) (ibeji-010, ibeji-011, ibeji-016); assentamento em três pratinhos de barro (ibeji-023) | neutro (ocre do site) | As estatuetas e imagens esculpidas (ibeji-011, ibeji-030, ibeji-037) não foram desenhadas, por serem figuras humanas e objetos de culto; o caruru e o macaco (ibeji-004, ibeji-029) ficaram de fora. |
| **Orunmilá / Ifá** | opelê, colar de Ifá usado na adivinhação (orunmila-001); nozes de palmeira usadas na adivinhação (itã) (orunmila-004) | neutro (ocre do site) | A forma exata do opelê (número e tipo de peças) e os sinais dos odus não estão fichados e não foram desenhados; nada de cena de consulta. |
| **Orum** | òrun: o céu imaginado como abóbada sólida sobre a terra (orum-001); céu visível e morada da divindade suprema (orum-002, orum-006) | neutro (ocre do site) | Os 'dois céus' e a terra dos mortos (orum-003, orum-004) não foram figurados. |
| **Aiê** | Aiyê: o mundo físico, em contraponto ao Orum (aie-001, aie-002); aiye: 'o mundo', abrangendo a terra e os céus (aie-003) | neutro (ocre do site) | — |
| **Odudua** | terra lançada sobre a água (mito da criação) (odudua-017); coquinho de dendê que vira palmeira de 16 ramos laterais (odudua-017); a terra, metade inferior do casal primordial (odudua-011, odudua-001) | neutro (ocre do site) | O galo do mesmo mito (odudua-017) ficou de fora para não carregar a composição; as versões masculina e feminina (odudua-014) não são figuradas, já que não há figura. |
| **Olokun** | o mar (olokun-001, olokun-005); sete correntes de ferro (mito do dilúvio) (olokun-006) | neutro (ocre do site) | — |
| **Orí** | meia cabaça coberta de búzios (ori-002) | neutro (ocre do site) | A coroa de 41 búzios guardada no Ile Ori (ori-004) não foi desenhada: a contagem e a forma exigiriam detalhe que é melhor conferir com praticantes; o número de búzios no desenho é só gráfico. |

## 4. Sem ilustração

| Entidade | Motivo |
|---|---|
| Iyami | Tema sensível (data/entidades.json, sensivel=true), à espera da decisão do conselho consultivo; o site nunca mostra ilustração de entidade sensível. |
| Ewá | Sem símbolos, elementos, domínios ou iconografia fichados (só parentesco e alimento: ewa-005, ewa-008). Fica para quando houver obra lida (Verger 1981, Prandi 2001; ver PENDENCIAS). |
| Olodumare / Olorum / Olofin | As fontes registram que Olodumare não tem imagens, templos nem culto direto (olodumare-001, olodumare-006, olodumare-019); uma ilustração contrariaria o que está fichado. |
| Egungun | Os únicos elementos visuais fichados são os mascarados do culto (egungun-006, egungun-009), que é reservado; desenhá-los seria figurar cena de culto. Decisão a confirmar com praticantes. |
| cosmologia | Capítulo-panorama, não entidade; as ilustrações de Orum, Aiê, Odudua, Olokun e Orí aparecem nas páginas deles. |

## 5. Site, QA e acessibilidade

- `site/src/components/Ilustracao.astro` + `site/src/lib/ilustracoes.js`: entidade sensível nunca recebe ilustração, mesmo que exista o arquivo (defesa em profundidade).
- Página do orixá: ilustração à direita do título (abaixo no celular), com legenda. Catálogo: medalhão de 72 px ao lado do nome. Capítulo: medalhão de 104 px com a legenda ao lado, acima do sobretítulo.
- **`scripts/qa_site.py` §14:** toda ilustração tem `<title>` igual ao texto alternativo do JSON, `role="img"` e `aria-labelledby`; nenhuma para entidade sensível ou listada em `sem_ilustracao`; todo registro citado existe e está fichado (ou revisado); SVG sem imagens externas; a página, o cartão e o capítulo de cada entidade ilustrada mostram a ilustração (com legenda na página e no capítulo); ids de título únicos por página. **Testado por adulteração** (ilustração para Iyami, registro inexistente, título trocado): 10 erros acusados.
- axe, testes e e2e: ver §7.

## 6. Screenshots

Em [`docs/screenshots/ilustracoes/`](../screenshots/ilustracoes/): `galeria-grande-{claro,escuro}.jpg` e `galeria-pequeno-{claro,escuro}.png` (todas as 22, em 320 e 72 px); topo do catálogo e das páginas e capítulos de Ogum, Iemanjá, Xangô, Oxalá e Odudua em desktop/celular, claro/escuro (`site/scripts/screenshots-ilustracoes.cjs`; com `BASE=<url>` tira da URL publicada).

## 7. Validadores e testes

Rodados no fim da sessão: `validar_fontes`, `validar_fichamento`, `divergencias`, `gerar_fichas` (sem diferença em `data/`), `validar_fichas`, `anticopia` (0 erros; só avisos antigos), `validar_capitulos`, `python3 -m unittest discover -s tests` (ok), build com `SITE_BASE=/mapadosorixas`, `qa_site.py` (ok, 44 ilustrações exibidas entre páginas, cartões e capítulos), e2e de capítulos, modelo 2 e revisão (ok; o e2e de revisão pegou um erro do próprio QA §14, que só aceitava `fichado` e não `revisado`, corrigido) e **axe** (`site/scripts/acessibilidade.cjs`: 198 verificações, 94 páginas × 1280/390 px + 10 no escuro, **0 violações**). A sessão não usou o acervo nem fichou fontes, por isso o anti-cópia com texto integral não se aplica.

## 8. Limitações e próximos passos

- **Revisão por praticantes (P1):** a série é um rascunho do projeto. Símbolos podem ter sentidos ou restrições que as obras não registram; o conselho deve poder vetar qualquer elemento. Remover um elemento é simples (apagar o trecho em `desenhos.py` e rodar `gerar.py`).
- **Oxê de uma lâmina:** desenhado assim porque o fichamento só diz "uma espécie de machado"; ver PENDENCIAS §3b.
- **Cores:** o acento escolhido é sempre uma cor que aparece em mais de uma tradição, mas nunca substitui a variação: as páginas continuam mostrando todas as cores, por tradição.
- **Encomenda a artistas afro-brasileiros:** sugestão ao autor substituir ou complementar esta série por ilustrações encomendadas e pagas a artistas ligados às tradições, com licença clara; `data/ilustracoes.json` serve como briefing (elementos, registros, o que evitar).
- **Leitor de tela real:** conferir com NVDA/VoiceOver como o texto alternativo é lido no cartão do catálogo (hoje ele é lido antes do nome).

## 9. Publicação

Push direto na `main`. O deploy (`deploy-pages.yml`, execução nº 36, com as 22 ilustrações) terminou com sucesso. **Conferência da URL publicada** (<https://aureliosaraiva.github.io/mapadosorixas/>, Playwright, 2026-11-02): o catálogo mostra 22 ilustrações, todas com texto alternativo; Ogum, Odudua e o capítulo de Iemanjá mostram a sua; Iyami e Ewá não mostram nenhuma; **nenhum erro de rede ou de JavaScript**. Screenshot: `docs/screenshots/ilustracoes/publicado-xango-desktop.jpg`.

## 10. Piloto figurativo de Oxóssi (pedido do autor, em avaliação)

O autor pediu imagens figurativas das entidades, mostrando como exemplo duas pinturas de Oxóssi tiradas da internet. Essas obras têm autor (uma é assinada, a outra traz marca d'água do deviantART), por isso não foram copiadas, decalcadas nem usadas como modelo. Por decisão do autor, foi feito **um piloto de figura estilizada original** que segue **só o que está fichado**:

- arco e flecha e eruquerê (oxossi-014); mata (oxossi-011, oxossi-012); colar de contas verdes e acento verde (oxossi-013, oxossi-025, oxossi-029);
- **silhueta sem traços de rosto**, num tom escuro fixo (`--il-figura`) que não muda com o tema. Se seguisse a cor do texto, a figura ficaria branca no modo escuro, ou seja, o tema trocaria a cor de pele. No escuro ganha um contorno claro, só por fora da silhueta;
- a roupa (pano na cintura) é genérica e sem cor, porque não há registro fichado de vestimenta fora do transe ("vestido de peles", oxossi-029, descreve a manifestação). O azul das pinturas de referência não tem fonte para Oxóssi.

Arquivos: `site/scripts/ilustracoes/pilotos_figura.py` → `site/src/assets/ilustracoes/pilotos/oxossi-figura.svg` (**fora do site**: o componente só lê a pasta principal); PNGs em `docs/screenshots/ilustracoes/piloto-figura-oxossi-*.jpg`.

**Limites e riscos:** desenho vetorial feito em código não chega à qualidade de uma pintura, e figura humana estilizada corre risco de parecer pictograma. Algumas casas de Candomblé não aceitam a figuração dos orixás, mais comum na Umbanda e na arte popular: a decisão de publicar figuras deve passar pelo conselho. Para retratos de qualidade, o caminho recomendado continua sendo encomendar ou licenciar obras de artistas, com autorização.
