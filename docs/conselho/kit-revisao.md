# Kit do revisor

> Material para enviar a quem aceitar revisar (Fase 4 do [`PLANO.md`](../PLANO.md)). **Rascunho preparado sem contato com ninguém.** O autor adapta o texto e envia.
> Partes: (1) guia do revisor · (2) sigilo · (3) termo de consentimento para crédito público · (4) convite em pt-BR · (5) convite em espanhol para olorishas.

---

## 1. Guia do revisor

### 1.1 O que é o projeto

Uma enciclopédia aberta sobre orixás que cita a fonte de cada afirmação e mostra **lado a lado** as versões de nações, casas e regiões diferentes, sem escolher uma "correta". Começa com 5 orixás (Exu, Ogum, Oxóssi, Xangô e Iemanjá) e tem catálogo, fichas e um grafo de conexões (parentesco nos itãs, equivalências com voduns e inquices, sincretismo). O projeto separa o Candomblé, com suas nações, da Umbanda.

### 1.2 Como as fichas são feitas

1. **Fichamento:** cada afirmação vira um *registro* em `data/fichamento/<orixa>.json`, com a fonte (`source_id`), a página, as tradições a que se aplica, a casa ou região quando a fonte informa, e uma **paráfrase**. Nunca há cópia de trecho de livro.
2. **Geração:** um script (`scripts/gerar_fichas.py`) monta a ficha em `data/orixas/<orixa>.json` usando só registros com status `fichado` ou `revisado`. Ninguém edita a ficha à mão.
3. **Versões:** se duas fontes dizem coisas diferentes, a ficha mostra as duas, cada uma com tradição, casa e fonte.
4. **Site:** o site lê esses dados e não traz texto próprio sobre os orixás. Todas as páginas exibem o selo "Rascunho — aguardando revisão de praticantes e pesquisadores" e estão fora dos buscadores (`noindex`).

Consequência prática: **o revisor comenta o registro, não a página.** Toda versão exibida no site traz o id do registro de origem (ex.: `ogum-012`).

### 1.3 O que pedimos que você revise

O revisor escolhe o que revisar: um orixá, um atributo ou só os registros da sua tradição. Para cada registro:

| Pergunta | Resposta possível |
|---|---|
| A paráfrase está fiel ao que a fonte diz? | sim / não / não sei |
| A afirmação vale para a tradição indicada? (ex.: está marcada `candomble_ketu`, mas é prática de Umbanda) | correta / trocar a tradição / ampliar / restringir |
| O tom é respeitoso? Há termo pejorativo ou exotizante? | ok / sugerir redação |
| O conteúdo pode ser publicado? (ver §2) | publicável / **não publicar** / em dúvida |
| Na sua casa ou nação é diferente? | descrever (vira **nova versão**, ver §1.5) |
| Falta algo importante e público? | indicar, de preferência com fonte |

Não precisa revisar tudo. Uma revisão parcial e bem delimitada vale mais que uma aprovação geral.

### 1.4 O que significa o status `revisado`

- Um registro só passa de `fichado` para `revisado` quando **pelo menos um revisor da tradição indicada** no registro o aprova.
- A aprovação vale **para aquela tradição**. Um registro de Ketu aprovado por um tata de Angola fica anotado, mas não passa a `revisado` na marcação Ketu.
- **Aprovar não é escolher a versão correta.** Significa: "esta versão está bem documentada e corretamente atribuída".
- A aprovação é registrada com quem aprovou, quando e qual tradição. O nome só aparece em público se você assinar o termo (§3). Detalhes técnicos em [`proposta-registro-revisao.md`](proposta-registro-revisao.md).

### 1.5 Como registrar uma divergência sem apagar a outra versão

O projeto **não apaga versões** porque um revisor discorda. Se o seu axé faz diferente:

1. Diga qual é a sua versão e **de onde ela vem**: sua casa ou nação, e se há livro ou artigo que a registre.
2. Se houver fonte publicada, ela entra como novo registro `fichado`, citando a fonte.
3. Se for conhecimento oral da casa, sem fonte escrita, e você **autorizar**, ela entra como versão de comunicação pessoal, com a casa ou nação indicada e só com o crédito que você permitir. Esse tipo de fonte ainda não existe nos dados: precisa de decisão do autor antes de ser usado.
4. A versão anterior continua lá, com a fonte original. Você pode pedir uma **nota** dizendo que ela não vale para a sua tradição.

Se dois revisores discordarem entre si, as duas posições ficam registradas. O projeto não arbitra.

**Exceção:** se você apontar que o registro **expõe fundamento** (§2) ou **atribui mal a fonte** (a fonte não diz aquilo), ele é retirado da ficha pública. A retirada fica anotada no histórico do repositório; o conteúdo não é apagado sem registro.

### 1.6 Como enviar a revisão

Por ordem de preferência para o revisor:

1. **Planilha ou documento** enviado pelo autor, com uma linha por registro (id, valor, paráfrase, tradição, fonte) e colunas para as respostas do §1.3;
2. **Comentários no pull request** da ficha no GitHub, para quem já usa a plataforma;
3. **Conversa** (chamada ou áudio) que o autor transcreve e devolve para você conferir antes de registrar.

Prazo sugerido: livre. Pedimos só que você avise se desistir.

---

## 2. Sigilo: o que NÃO deve ser publicado

Princípio 4 do [`PLANO.md`](../PLANO.md): não publicar fundamentos iniciáticos. **Na dúvida, não publicar.**

**Nunca publicar:**
- segredos de feitura (iniciação), *awo* e etapas reservadas de obrigação;
- rezas, cantigas e oríkìs de uso restrito (só os de domínio público e já editados, com fonte);
- ebós específicos, receitas de assentamento e de "trabalhos";
- composição exata de comidas e sacrifícios rituais;
- nome de pessoa iniciada, oruko (nome de iniciação) ou orixá de cabeça de alguém, sem consentimento explícito;
- localização de assentamentos ou de espaços restritos dos terreiros;
- qualquer coisa que a sua casa considere fundamento, mesmo que já esteja em livro.

**Retido até decisão do conselho:** tabus (*ewós*) e alimentos rituais. Já existem registros fichados que estão **fora** da ficha pública (`pendencias.retidos_ate_conselho`). Pedimos ao conselho uma regra sobre quais desses temas, e em que nível de generalidade, podem aparecer.

**Pode ser publicado (com fonte):** nomes, domínios, cores, dia da semana, saudação de uso público, símbolos e ferramentas que aparecem em festas públicas, sincretismo, itãs **parafraseados** de obras publicadas, história do culto, interpretação acadêmica.

Uma informação estar num livro **não basta** para ser publicada: o critério final é o do conselho.

---

## 3. Termo de consentimento para crédito público (modelo)

> **Termo de consentimento — Revisão e crédito no projeto [nome do projeto]**
>
> Eu, ______________________________ (nome como deseja ser identificado/a), declaro que:
>
> 1. Participei voluntariamente e sem remuneração da revisão de conteúdos do projeto [nome], enciclopédia aberta sobre orixás mantida por [nome do autor].
> 2. Revisei: ☐ todo o conteúdo indicado · ☐ apenas os registros: ____________ · ☐ apenas a tradição: ____________.
> 3. Quanto ao crédito público, **escolho** (marcar uma opção):
>    ☐ ser citado/a pelo **nome completo**, com tradição/casa: ____________ e/ou instituição: ____________;
>    ☐ ser citado/a **só pelo nome**, sem casa nem instituição;
>    ☐ ser citado/a de forma **genérica** (ex.: "iyalorixá de nação Ketu, Salvador");
>    ☐ **não** ser citado/a publicamente (o registro interno da revisão continua existindo, sem nome).
> 4. Entendo que:
>    - minha aprovação **não** significa que a versão revisada seja a única correta, e que outras versões continuarão publicadas lado a lado;
>    - o nome escolhido aparecerá nas fichas revisadas, na página de créditos e nos dados abertos do projeto (arquivos JSON públicos no GitHub, sob licença aberta);
>    - os dados abertos podem ser copiados por terceiros e, depois de publicados, não é possível garantir que desapareçam de todas as cópias;
>    - posso **retirar este consentimento** a qualquer momento, por mensagem a [contato do autor]. Meu nome sai das versões futuras do site e dos dados em até 30 dias.
> 5. Nenhum conteúdo que eu tenha indicado como fundamento ou sigiloso será publicado.
>
> Local e data: ____________  Assinatura (ou aceite por mensagem escrita): ____________

*Observação para o autor:* o autor mora na Espanha e o projeto terá revisores no Brasil e em outros países. Nome e tradição religiosa são dados pessoais sensíveis tanto no RGPD europeu (art. 9) quanto na LGPD (art. 11). Por isso o consentimento precisa ser explícito, específico e revogável, como neste modelo. Antes de usar, vale uma revisão jurídica rápida.

---

## 4. Convite em português (modelo)

**Para pesquisador/a:**

> Assunto: Convite para revisar fichas de uma enciclopédia aberta sobre orixás
>
> Prezado/a Prof./Profa. [sobrenome],
>
> Meu nome é [nome]. Coordeno um projeto sem fins lucrativos de enciclopédia aberta sobre orixás. Cada afirmação traz fonte e página, e as versões de nações e casas diferentes aparecem lado a lado, sem eleger uma correta. Seu trabalho, em especial [obra(s)], está entre as fontes que usamos.
>
> Antes de publicar, queremos que pesquisadores/as e sacerdotes/as de várias tradições revisem as fichas. Gostaria de saber se teria interesse em revisar **[um recorte pequeno: ex. os registros sobre equivalências entre orixás e voduns]**, no tempo e no formato que preferir (planilha, comentários ou conversa).
>
> A participação é voluntária, e o crédito público é opcional, com termo de consentimento. Envio em anexo um guia de duas páginas sobre como as fichas são feitas e o que pedimos.
>
> O projeto e os dados estão em [link do repositório/prévia].
>
> Agradeço desde já a atenção, mesmo que não seja possível participar.
>
> Atenciosamente,
> [nome] · [contato]

**Para casa de santo / instituição (por meio do terreiro, federação ou núcleo):**

> Assunto: Pedido de orientação para um projeto educativo sobre orixás
>
> Prezada comunidade do [nome da casa/instituição],
>
> Meu nome é [nome]. Estou organizando uma enciclopédia aberta e gratuita sobre os orixás, feita a partir de livros e pesquisas publicadas, com a fonte de cada informação. Nela, Candomblé (Ketu, Jeje, Angola), Umbanda, Batuque e outras tradições aparecem separados e com respeito às diferenças entre as casas.
>
> Sabemos que livros não substituem a palavra de quem vive a religião. Por isso pedimos, com todo respeito, que a casa indique, se achar adequado, alguém que possa ler as fichas da sua tradição e apontar erros, faltas de respeito e, principalmente, **o que não deve ser publicado**. Nenhum fundamento será divulgado, e a pessoa decide se quer ou não aparecer com seu nome.
>
> Se for de seu interesse, envio o material e me coloco à disposição para conversar no formato e no momento que a casa preferir.
>
> Com respeito e agradecimento,
> [nome] · [contato]

---

## 5. Convocatoria en español para olorishas (modelo)

> Asunto: Invitación a revisar fichas de una enciclopedia abierta sobre los orishas
>
> Estimado/a [tratamiento: olorisha / iyalocha / babalocha / babalawo] [nombre]:
>
> Me llamo [nombre] y coordino un proyecto sin ánimo de lucro: una enciclopedia abierta sobre los orishas. Cada afirmación cita su fuente, y las versiones de distintas tradiciones (Candomblé en Brasil, Regla de Ocha/Lucumí en Cuba y en la diáspora, culto yoruba en Nigeria) aparecen una al lado de la otra, sin elegir una como "la correcta".
>
> Estamos preparando la versión en español y queremos que la revisen personas que viven la Regla de Ocha. Nos gustaría saber si estaría dispuesto/a a revisar **[un recorte pequeño: p. ej. lo referente a Yemayá y Changó en la tradición lucumí]**, cuando y como le resulte más cómodo (hoja de cálculo, comentarios o una conversación).
>
> Le aseguramos que:
> - no se publicará ningún fundamento ni secreto de santo, y usted podrá indicar lo que no debe divulgarse;
> - su participación es voluntaria y el crédito público es opcional (con un documento de consentimiento que puede revocar cuando quiera);
> - si en su casa se hace de otro modo, su versión se registrará junto a las demás, sin borrar ninguna.
>
> Le adjunto una guía breve sobre cómo se elaboran las fichas. El proyecto puede consultarse en [enlace].
>
> Con todo respeto y agradecimiento, aunque no le sea posible participar,
> [nombre] · [contacto]

*Nota para o autor:* a guia (§1–2) e o termo (§3) ainda precisam de tradução para o espanhol antes de serem enviados a olorishas. Isso fica para a Fase 7, ou para quando houver o primeiro aceite.
