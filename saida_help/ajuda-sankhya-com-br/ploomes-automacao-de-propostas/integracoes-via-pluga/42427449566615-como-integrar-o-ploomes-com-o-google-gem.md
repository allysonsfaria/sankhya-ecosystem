---
id: "42427449566615"
titulo: "Como integrar o Ploomes com o Google Gemini (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427449566615-Como-integrar-o-Ploomes-com-o-Google-Gemini-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:01:35Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12414653", "sync_hash_fc74d18049f0"]
---

# Como integrar o Ploomes com o Google Gemini (via Pluga)

Observação:

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

Com a integração entre o Ploomes e o Google Gemini via Pluga, você adiciona uma camada de inteligência artificial diretamente no seu fluxo de vendas — seja para qualificar leads antes de criá-los no CRM, para enriquecer dados de negócios ou para disparar tarefas automáticas no time de operações assim que um negócio é fechado.

O Google Gemini atua sempre como etapa intermediária, processando as informações recebidas de uma ferramenta de origem e gerando um resultado pronto para ser usado na ferramenta de destino. Alguns exemplos do que é possível fazer:

- A cada nova resposta em um formulário do Google Forms, usar o Gemini para qualificar e estruturar os dados do lead e criar automaticamente um card no Ploomes com as informações organizadas;
- Quando um card for marcado como ganho no Ploomes, acionar o Gemini para redigir automaticamente um briefing de passagem de bastão para a operação e criar uma tarefa no Trello com as instruções prontas;
- A cada proposta criada no Ploomes, enviar os dados ao Gemini para gerar um rascunho de e-mail personalizado e salvá-lo como rascunho no Gmail;
- Quando um card chegar a uma etapa específica do funil, usar o Gemini para classificar o lead como quente, morno ou frio e atualizar um campo personalizado no próprio Ploomes;
- A cada novo cliente criado no Ploomes, acionar o Gemini com pesquisa na web habilitada para enriquecer o perfil com informações públicas da empresa e registrar o resumo no CRM.

Essa flexibilidade é possível porque o Google Gemini suporta ações como **"Enviar mensagem"**, **"Extrair dados estruturados"** e **"Buscar na web"**, que podem ser combinadas com qualquer gatilho disponível no Ploomes or em outras ferramentas de origem integradas à Pluga.

---

## Requisitos

- Uma conta no [Ploomes](https://app10.ploomes.com/login);
- Uma conta no [Google Gemini](https://aistudio.google.com/prompts/new_chat) (via Google AI Studio);
- Uma conta na [Pluga](https://pluga.co/).

**Nota:** automatizações com IA exigem pelo menos três ferramentas, com o Google Gemini como intermediário, e utilizam o recurso de integrações multi-actions — disponível nos [planos pagos](https://pluga.co/precos/) da Pluga.

## Passo a passo

Neste artigo você encontra dois casos de uso prontos para implementar com o Google Gemini e o Ploomes via Pluga. Os primeiros passos — acesso à Pluga e criação da automatização — são comuns a ambos. Faça-os uma única vez e siga direto para o caso que faz mais sentido para o seu contexto:

- **1. Como qualificar leads do Google Forms com o Gemini e criar cards no Ploomes** — ideal para times comerciais que recebem leads por formulário e querem que cada oportunidade chegue ao CRM já qualificada e com dados estruturados, sem digitação manual.
- **2. Como automatizar a passagem de bastão no fechamento: do Ploomes para o Trello via Gemini** — ideal para times que precisam que a operação receba automaticamente um briefing completo do negócio assim que ele é ganho no CRM.

Acesse a [Pluga](https://pluga.co/) e clique em **"Entrar"** ou em **"Cadastrar"** se este for o seu primeiro acesso;

![Tela de login da Pluga](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2423577437/8b78210ecc53cf92e76395b39832/d2e0bf3c-1a4c-44e6-a494-190d93fbba80?expires=1786536000&signature=4fc195a7157d907ba826c55519bf1012f7b83f7547d6f6969ee01c2f49b925c5&req=diQlFcx5moVcXvMW3nq%2BgXPkDFHLr4IbdSRzH%2FngzsECSGmNmXy%2Bkb3DwF0O%0AJYAN86F8ZEtxEHXZGIsBmXloGTg%3D%0A)

Na área de usuário da Pluga, clique em **"Criar Automatização"**;

![Botão Criar Automatização na área de usuário da Pluga](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2423577802/4d129be714c890fba7a3d7c90ad5/1736c0a6-b4b0-4585-bf9c-a940fa04e6db?expires=1786536000&signature=44ca3ba4fa5a45f51a9a5cb7b17dabda018b3062b2bcc055c878a9f7ceeac1cd&req=diQlFcx5molfW%2FMW3nq%2BgQHVt1x4Bo30F42jhQ%2BiOMw5u7SP87zBi2bhgEh%2B%0AqU6y52crCGZ7S2l8C2eywrVRtgo%3D%0A)

Dê um título para a sua automatização — isso vai ser útil caso você queira editá-la no futuro — e siga para o caso de uso desejado abaixo.

![Campo de título da automatização](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2423609210/329f521a6cf9b3ea371a4948114c/e03f4588-a8e4-4f7d-acc8-7c7d0824ee19?expires=1786536000&signature=1e96c7de4001c212eab402d4c4de8c0244d8b189731be982f783df5af0f3c7b2&req=diQlFc9%2BlINeWfMW3nq%2BgbTkgrQFx4NNHDKjrgMNmIKb7XEjTyI0xIhkuzQ2%0AsMJs2s68Qi2NOHqtANYjDv6AvDk%3D%0A)

---

## 1. Como qualificar leads do Google Forms com o Gemini e criar cards no Ploomes

Quando um lead preencher um formulário no Google Forms, os dados são enviados ao Gemini, que interpreta as respostas e extrai automaticamente as informações mais relevantes para a qualificação — como empresa, cargo, produto de interesse, porte e urgência. Em seguida, um card é criado no Ploomes com esses dados já estruturados, eliminando a necessidade de cadastro manual e garantindo que o time comercial receba oportunidades com contexto pronto para abordagem.

**Requisitos adicionais:** uma conta no [Google Forms](https://www.google.com/forms/about) com um formulário de captura de leads configurado.

## Conectando-se ao Google Forms

Selecione o **Google Forms** como ferramenta de origem e o gatilho **"Nova resposta em um formulário"**. Em seguida, clique em **"Salvar e Continuar"**;

![Seleção do Google Forms como ferramenta de origem](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426845479/cf0a6fcca5bb30192f3639b96d72/53a2221f-cd14-4f7f-90f1-6d142aa3dde4?expires=1786536000&signature=c8b7d38fd671a89b445302a45d69ea6e6b9d218d486c03d61d162c4cc1b10060&req=diQlEMF6mIVYUPMW3nq%2BgQ9VJ2NdcdF2Qh6Pp1PB2bxdQRowH5JsiCyYGXO8%0ACzHiLdrlrKpPEpL4UTMgFv4PAOs%3D%0A)

Conecte sua conta do Google clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Ao criar outras automatizações com o Google Forms, sua conta já aparecerá listada entre as contas conectadas;

![Conectar conta Google Forms](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426846404/827ef62ed95ec98146a577e127db/6f41b298-c966-4f1e-a9a7-a124820077aa?expires=1786536000&signature=dfca7a13917890c06ad778e70cc593e5850679bae859a25b033a4090a4f74f3a&req=diQlEMF6m4VfXfMW3nq%2BgTIVDL9PkpE1Gj36iHGvKjdXD9Ap6jjHxZV6966W%0AM1nx3OzidJ5oNHgLGpnWOAGYD%2FE%3D%0A)

Selecione a planilha que será usada para recuperar as informações do formulário, além da página em que as respostas serão computadas. Em seguida, clique em **"Salvar e Continuar"**;

![Seleção da planilha e página do formulário](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426847581/8804a29d2c36ee874f50f72fade0/69dec39a-af8b-48b8-b934-2441ae359848?expires=1786536000&signature=09d3478892e8cc0a161d20ec6169429acbc2f1c910c69b7e3ffbd3306310a893&req=diQlEMF6moRXWPMW3nq%2BgVCq2ifQCPusGR1s45wqe5ZV2H0hzyGSZAFzUIti%0ACuy3iJAh5aIiahr%2Ba0zhMt5LlAc%3D%0A)

Se quiser, configure filtros para acionar a automatização apenas para respostas com critérios específicos — por exemplo, um campo de segmento ou porte da empresa. Em seguida, clique em **"Conectar Nova Ferramenta"**.

## Transformando dados com Google Gemini

Selecione a ferramenta **Google Gemini** e a ação **"Extrair dados estruturados"**. Essa ação interpreta as respostas do formulário e retorna os dados organizados em campos definidos por você, prontos para preencher o card no Ploomes. Em seguida, clique em **"Salvar e Continuar"**;

![Seleção da ação Extrair dados estruturados no Google Gemini](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426850478/13498310318636c1c1cee975b3c3/3127acbe-2615-4156-8cad-6fb6d608c9d3?expires=1786536000&signature=4eb10f8b562a77e93cffd0525e5e5d4a290499cb39f3babc01dc331a8718efd2&req=diQlEMF7nYVYUfMW3nq%2BgZo%2BFCLTZJ%2BKv4MtMrs4MQdKgJTgjRhljtfr9nt1%0ASAYNXNgzRmKtI0DmFE0aSoM79mk%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua conta do Google AI Studio. Esse processo só precisa ser feito uma única vez. Caso não saiba como encontrar sua API Key, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga os passos indicados;

![Conectar conta do Google AI Studio](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426851183/bdb155a8cd3b9c60dd8f7bfd0ef1/69d8296f-f1b1-4dde-a4d1-75a8397e9bfb?expires=1786536000&signature=0c7ba78095d42fbd69dc954617158ecb9d0dff9d5e71e4cedba6952df85dd799&req=diQlEMF7nIBXWvMW3nq%2Bgdw%2Fa8f4AYD0kkIJWmBE8n%2Bp4TXhuVVpsSV2MPuC%0AEJjM7FZ%2BgLfqozm1Wk7F7KpbqMQ%3D%0A)

No campo **"Texto a ser transformado em dados estruturados"**, use o botão **"Inserir infos"** para mapear as respostas recebidas do Google Forms — nome, empresa, cargo, produto de interesse e qualquer outro campo relevante do seu formulário;

![Campo de texto para extração de dados estruturados](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426851742/3cc9dc8490e6ce3b0cc0f153e5eb/1758f85a-13de-4b24-9127-121774f0b488?expires=1786536000&signature=fde2880313e954076121b48be4ba8a01b7832e02b958bc6decae5f1672f85ae1&req=diQlEMF7nIZbW%2FMW3nq%2BgQ4ocq4dxI8XqN9qwEwG6gnnVB0HIm%2BjPp0sl6l2%0AqK8mVFXGxqEAxRzFWZGslo60Gh0%3D%0A)

Selecione o **modelo** do Gemini que será utilizado. Por padrão, a integração da Pluga utiliza o modelo **2.5 Flash**, que já está habilitado para buscas na web. Tenha em mente que, para que a sua automatização com o Gemini utilize URL de contexto e buscas na web, é preciso utilizar alguns dos modelos que sejam capazes de realizar este tipo de ação. São eles:

- 2.0 Flash
- 2.5 Flash
- 2.5 Flash-Lite
- 2.5 Pro (preview)

No campo **"Instruções de Sistema"**, cole o modelo abaixo e ajuste conforme a estrutura do seu formulário e o perfil dos leads do seu negócio.

Você é um especialista em qualificação de leads para times comerciais B2B. Sua função é interpretar as respostas de um formulário de captura e transformá-las em um perfil objetivo e acionável para o time de vendas. Trabalhe exclusivamente com as informações fornecidas — nunca invente dados. Mantenha a linguagem clara, direta e útil para quem vai abordar o lead. Se algum campo não tiver informação suficiente, deixe-o em branco em vez de preencher com suposições.

![Imagem 10: Você é um especialista em qualificação de leads para times comerciais B2B. Sua função é interpretar as respostas de um…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426855039/1e04c54df5725bafe90ea9d4159f/c6f6cfcf-4606-4cae-a351-964b636ecdf3?expires=1786536000&signature=50c1e4e26fa353f8bd954d4208ecfeb807d7425ce46903e14fc733f72de6001b&req=diQlEMF7mIFcUPMW3nq%2BgTk9KS1UPeHNvIvtaMOlP4S7jvjrEEBXOMDE2z77%0A9qcUGuJQs1z8UyrMmVhZ7mFoCVk%3D%0A)

Indique a **quantidade de campos** que deseja extrair e defina o nome e o tipo de cada parâmetro. Como ponto de partida, você pode utilizar a seguinte estrutura:

- **nome:** nome completo do lead;
- **empresa:** nome da empresa;
- **cargo:** cargo ou função do lead;
- **produto\_interesse:** produto ou solução de interesse mencionada;
- **porte\_empresa:** porte estimado da empresa, se mencionado;
- **urgencia:** nível de urgência ou prazo mencionado;
- **resumo\_qualificacao:** parágrafo curto com a síntese do perfil do lead, voltado para a primeira abordagem do vendedor.

![Imagem 11: resumo_qualificacao: parágrafo curto com a síntese do perfil do lead, voltado para a primeira abordagem do vendedor.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426856069/1443453878a4ec916b39e2062ed5/bbd04ac1-4324-4122-8ff5-b0385679d80f?expires=1786536000&signature=79cc6a224ad2d4ad898c7f86cacf669a2ad73293ca9339aa011eab31c28549b5&req=diQlEMF7m4FZUPMW3nq%2Bgc6GjXf%2BsnOddNxWKkMdgO4SgCLh5KvGZq9QG9oc%0ALLlqlgEc2ZjYPfhbeYZulsDlUzA%3D%0A)

Selecione o **modelo** do Gemini que será utilizado. Por padrão, a integração da Pluga utiliza o modelo **2.5 Flash**, que já está habilitado para buscas na web. Tenha em mente que, para que a sua automatização com o Gemini utilize URL de contexto e buscas na web, é preciso utilizar alguns dos modelos que sejam capazes de realizar este tipo de ação. São eles:

- 2.0 Flash
- 2.5 Flash
- 2.5 Flash-Lite
- 2.5 Pro (preview)

Se preferir, você pode acessar a lista completa de modelos compatíveis com essa funcionalidade clicando [aqui](https://ai.google.dev/gemini-api/docs/models?hl=pt-br).

Se quiser que o Gemini complemente as informações do lead com dados públicos da empresa, habilite a opção **Pesquisa na web** antes de salvar.

**Atenção:** o segredo desta automatização está na personalização e no controle. Antes de finalizar, teste o prompt diretamente na interface do Google Gemini com um exemplo real de resposta do seu formulário. Assim, você consegue ajustar a estrutura dos campos e o tom das instruções antes de colocar a automatização em produção.

Ao finalizar, clique em **"Salvar e Continuar"** e, em seguida, em **"Conectar Nova Ferramenta"**.

![Imagem 12: Ao finalizar, clique em "Salvar e Continuar" e, em seguida, em "Conectar Nova Ferramenta" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426858148/2cf3b01aaa0ae43661701d64e1ac/3a803380-1b5b-4c76-8393-194c27be5d80?expires=1786536000&signature=07166e984697fa00645e54ae65cf1850cb9ab5a357a3a6ae14093d57527ca735&req=diQlEMF7lYBbUfMW3nq%2BgeSlm7ARjZVR2Ko21cvN1YwZH%2Fu1e2Jy2Cil%2Bi9v%0AeALEOx9ptCzgbF06V%2Fvfqd%2FZ8VQ%3D%0A)

## Enviando os dados para o Ploomes

Selecione o **Ploomes** e a ação **"Criar ou atualizar card"**. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 13: Selecione o Ploomes e a ação "Criar ou atualizar card" . Em seguida, clique em "Salvar e Continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426859750/2089718cb8d24d6d9f2b830dbb01/21c0a836-5f22-4866-92fe-b2f620ec9ba8?expires=1786536000&signature=c85911f3d66a7655606379cb7d78691c01487e33906150a72d29b508f8ccb977&req=diQlEMF7lIZaWfMW3nq%2BgaM%2BFiTK28PuoRUkLTvSkdWy0fOGNwBbEkWcA1U5%0ABKoX17vxI5P8%2Bqt%2BNEkTnNtWsaI%3D%0A)

Conecte sua conta do Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Caso seja sua primeira vez, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 14: Conecte sua conta do Ploomes clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426860639/82aeea2f2691b311efcdde54791b/65e42b5c-2087-45a0-a83d-9ddd234c5f56?expires=1786536000&signature=c892de26931974a436bf9031f4a8d5c6a1f5caa32ce613374882ba321618beec&req=diQlEMF4nYdcUPMW3nq%2BgQMvEJ161UWi%2FUV2rlRV%2F4874E2I1P8kOQh7gf3A%0APUajqT3aF4TTFlXAibt1JO%2F3eUE%3D%0A)

Selecione em qual **funil** e **etapa** o card será criado;

![Imagem 15: Selecione em qual funil e etapa o card será criado;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426861458/35b3451ed402e1da39bd28fecf43/16ea6557-0570-4fd8-b112-19a47eca6760?expires=1786536000&signature=136be914a64247805c34f354a8065b3819bbb242078413be3269d39926c9570d&req=diQlEMF4nIVaUfMW3nq%2BgRpvxbd8T8IrrJbH3ro%2FhY3lE8vbzmOXJTbz2dQU%0AVZ53v5WabcuWLYCc%2BbKc4D%2FLCec%3D%0A)

Use o botão **"Inserir infos"** para mapear os campos extraídos pelo Gemini nos campos correspondentes do Ploomes — como **título do card** (com nome e empresa do lead), **nome do contato**, **empresa** e campos personalizados como **produto de interesse** ou **resumo de qualificação**. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 16: Use o botão "Inserir infos" para mapear os campos extraídos pelo Gemini nos campos correspondentes do Ploomes — como…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426862122/1bbfe86a36d0c6c812dcc392c6b4/220926d2-eac2-471e-9eff-8f85c224841a?expires=1786536000&signature=fd2c0c6b94c96786628fbf260e1b1001d81b2e0affda335bb39af2c22321b280&req=diQlEMF4n4BdW%2FMW3nq%2BgUG0ZqepNyyzKtp77exs9lLlanHb2AcYX5JuDCiN%0A7jj%2BUFVM3rG4OXQ%2BTht%2FLIDIlNQ%3D%0A)

Clique em **"Finalizar Automatização"**. Prontinho. Agora, sempre que uma nova resposta chegar no Google Forms, o Gemini qualificará o lead automaticamente e um card será criado no Ploomes com os dados estruturados — sem nenhuma digitação manual.

![Imagem 17: Clique em "Finalizar Automatização" . Prontinho. Agora, sempre que uma nova resposta chegar no Google Forms, o Gemini…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426862847/19f73e0d2500e179737ed4dc160f/1dff2c64-0674-4e8e-923b-bd59a8ea5d97?expires=1786536000&signature=976d2d123b106489e9e2d868a008ee0d827ed351872bea309e9cf985cce97027&req=diQlEMF4n4lbXvMW3nq%2BgXkmvEzindG6OYNdIQrXgXyL8N7TbxZan2tTjAJ0%0AKxy1%2BFxsaf2heiR%2BAxOFVFsrQIY%3D%0A)

---

## 2. Como automatizar a passagem de bastão no fechamento: do Ploomes para o Trello via Gemini

Quando um card for marcado como ganho no Ploomes, os dados do negócio são enviados ao Gemini, que gera automaticamente um briefing de passagem de bastão para a equipe de operações. Esse briefing — com contexto do cliente, produto contratado, valor, prazos e principais pontos de atenção — é então usado para criar uma tarefa detalhada no Trello, garantindo que a operação receba todas as informações necessárias para começar o trabalho sem precisar procurar nada no CRM.

**Requisitos adicionais:** uma conta no [Trello](https://trello.com/) com ao menos um espaço e uma lista configurados para receber as tarefas de operação.

## Conectando-se ao Ploomes

Selecione o **Ploomes** como ferramenta de origem e o gatilho **"Card ganho"**. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 18: Selecione o Ploomes como ferramenta de origem e o gatilho "Card ganho" . Em seguida, clique em "Salvar e Continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426865694/9eca3a4857b564abb1412a8c160d/76c8500f-6679-4239-911f-9d2efc77a624?expires=1786536000&signature=b0a54b8d96ae5896e0e4039ef2d114ef26c016f200e33a3e72c5ff98c1182e05&req=diQlEMF4mIdWXfMW3nq%2BgbZvWOp1YkTVdXrGhqsCrhChx%2FBaumD%2FepRVoEEW%0AJIaxkv0iPCWRLU4Tk51Bi2KHlSg%3D%0A)

Selecione o **Ploomes** como ferramenta de origem e o gatilho **"Card ganho"**. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 19: Selecione o Ploomes como ferramenta de origem e o gatilho "Card ganho" . Em seguida, clique em "Salvar e Continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426866346/c5c5a7cf1e304d56c97ab03d3768/b88a6851-fc71-490f-930e-2fb531560975?expires=1786536000&signature=9e9831be87698d0a38cfce8fcff56493cfa1a3bf065e111c1a8a8424907e1e42&req=diQlEMF4m4JbX%2FMW3nq%2BgT987Q1kkC8qnnRodyZLaAYj0KT%2B36eDR6k2xBak%0AsymvjYFKzjth9nF7ZBU9V5qldmw%3D%0A)

Conecte sua conta do Ploomes clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez. Caso seja a sua primeira vez, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 20: Conecte sua conta do Ploomes clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426867130/22b258d33d398f1f3396068feabf/c16fa74d-8526-414f-9038-6c8a71ed3e07?expires=1786536000&signature=476e18f9000e9a3ea0c20125a4d35719d864abfc46b3b9f620993513736c0a90&req=diQlEMF4moBcWfMW3nq%2BgQlP51wbUQveZq6TzOY%2BlrvlRoWMYL5Wykjl%2B0Bd%0ATDhwPtEcvVIrJyJeQf429CHyexs%3D%0A)

Se quiser, configure filtros para acionar a automatização apenas para cards de funis ou valores específicos — por exemplo, apenas negócios acima de determinado valor ou de um produto específico. Em seguida, clique em **"Conectar Nova Ferramenta"**.

## Transformando dados com Google Gemini

Selecione a ferramenta **Google Gemini** e a ação **"Enviar mensagem"**. Essa ação envia os dados do negócio para o Gemini e retorna um texto gerado pela IA, que será usado como descrição da tarefa no Trello. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 21: Selecione a ferramenta Google Gemini e a ação "Enviar mensagem" . Essa ação envia os dados do negócio para o Gemini e…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426877385/140b9b870b53f958e391ca666855/4ad20489-b34e-4aec-b3ac-ff42ca77aadd?expires=1786536000&signature=0c0014bb5d66a2dff3344fe03aba21e4c64b31ed367cc2c21a52d8be91b374b0&req=diQlEMF5moJXXPMW3nq%2BgdZktuw47shp%2B5JHmaupcWMwANNfkJl80xiGfjlm%0AIRQM%2FRJMbLjSNMCEP0mZUViOsPc%3D%0A)

Conecte sua conta clicando em **"Conectar Nova Conta"** e realize a autenticação com a sua conta do Google AI Studio. Esse processo só precisa ser feito uma única vez. Caso não saiba como encontrar sua API Key, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga os passos indicados;

![Imagem 22: Conecte sua conta clicando em "Conectar Nova Conta" e realize a autenticação com a sua conta do Google AI Studio. Esse…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426878004/1170bb0ad28c934a13f7b0e74ed9/55ed4aa5-de50-4c6e-8e76-4e570f9dbf16?expires=1786536000&signature=97f1a24ba9c5c1830861199fb8820611c5454c2a3fb49148e95b99657ca24d0a&req=diQlEMF5lYFfXfMW3nq%2BgbsnCYjztmgpQDQsl0eoeLLSr9Ph%2Bpc9IiPteuPV%0AHudof%2BX3p8pkAVCdfHb1J%2ByU4nI%3D%0A)

No campo **"Mensagem (prompt de comando)"**, cole o modelo abaixo e use o botão **"Inserir infos"** para mapear as variáveis com os dados recebidos do Ploomes.

Você é um assistente de operações B2B. Um negócio foi fechado no CRM e você precisa gerar um briefing de passagem de bastão para o time de operações, com todas as informações necessárias para iniciar a entrega sem precisar consultar outros sistemas.

Dados do negócio fechado:

Título do card: [[título do card]]

Cliente: [[pessoa.nome]]

Empresa: [[empresa.nome]]

Valor total: [[valor da proposta]]

Produtos contratados: [[nome dos produtos]]

Vendedor responsável: [[dono do card]]

Data de fechamento: [[data de fechamento]]

Com base nessas informações, gere um briefing estruturado contendo:

1. Resumo do negócio (2-3 linhas)

2. Produto(s) contratado(s) e escopo esperado

3. Principais pontos de atenção para a operação

4. Próximos passos sugeridos para o início da entrega

Regras: utilize apenas as informações fornecidas, sem inventar dados. Seja direto e útil para quem vai executar a entrega. O texto deve ter no máximo 300 palavras e usar parágrafos curtos para facilitar a leitura.

![Imagem 23: Regras: utilize apenas as informações fornecidas, sem inventar dados. Seja direto e útil para quem vai executar a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426879731/f5cee9782edeaa0855150ee9e1e1/85004a6d-3328-4582-8d00-e398e8041883?expires=1786536000&signature=065af63af330893f4756f1138cefd18b7733517fce09b42a4153efb084cc1c1f&req=diQlEMF5lIZcWPMW3nq%2BgeQycrmhv57MnKNKxtsRWccM9KXj8NOiNvbFPmcP%0ATyREK6Hp%2B3isAPyN%2B9b4QSxMTIc%3D%0A)

No campo **"Instruções de Sistema"**, defina o comportamento do modelo. Por exemplo:

Você é um assistente especializado em operações B2B. Seu papel é transformar dados de negócios fechados em briefings claros e acionáveis para o time de entrega. Seja direto, objetivo e organize as informações de forma que o leitor entenda o contexto sem precisar consultar outros sistemas. Mantenha a ortografia impecável e a linguagem profissional.

Selecione o **modelo** do Gemini que será utilizado. Por padrão, a integração da Pluga utiliza o modelo **2.5 Flash**, que já está habilitado para buscas na web. Habilite a **Pesquisa na web** caso deseje complementar o briefing com informações públicas sobre o cliente — por exemplo, notícias recentes ou contexto de mercado.

![Imagem 24: Selecione o modelo do Gemini que será utilizado. Por padrão, a integração da Pluga utiliza o modelo 2.5 Flash , que já…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426881353/9b551556738e375cfa2729d77adb/8f558faa-b23b-413e-92e7-3c8ff96e566f?expires=1786536000&signature=f070cf8f93df2e4296083868b53f1cb89d34bb4246f7018806a6ed198467299b&req=diQlEMF2nIJaWvMW3nq%2BgT3eCwAUQ4xJMXXDV5ocKic%2FrgbqwovAisnyN0L1%0A9R%2BnYiMBB3MpMibKHbLapuuL8iI%3D%0A)

**Atenção:** antes de ativar a automatização, teste o prompt diretamente na interface do Google Gemini. Cole um exemplo real de dados de um card ganho no Ploomes e verifique se o briefing gerado está como esperado. Só ative depois que o resultado estiver consistente.

Ao finalizar, clique em **"Salvar e Continuar"** e, em seguida, em **"Conectar Nova Ferramenta"**.

![Imagem 25: Ao finalizar, clique em "Salvar e Continuar" e, em seguida, em "Conectar Nova Ferramenta" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426882365/51a03f2baa358b13af7490ee069f/e0794d24-ebd1-4369-8519-2c396d134cca?expires=1786536000&signature=f19a8952aea0392f507bd1173ea26cfec51f568c0696e617204a6375e770aa01&req=diQlEMF2n4JZXPMW3nq%2BgdZeAbuJODy3pI7B60YCg6FLOBhheEEUVtw6yZD7%0AEAX2uFC3Ltm2K1q9LUM6Cp%2F1k4Y%3D%0A)

## Criando a tarefa no Trello

Selecione o **Trello** e a ação **"Criar/Atualizar um card no Trello"**. Em seguida, clique em **"Salvar e Continuar"**;

![Imagem 26: Selecione o Trello e a ação "Criar/Atualizar um card no Trello" . Em seguida, clique em "Salvar e Continuar" ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426883529/739465e2419d32583cca53dc5cdc/3735d8bf-e357-4d95-8a90-8ebee2713bf5?expires=1786536000&signature=d700bc0f1ed56c42afb7675a334c1fef698c0a9dd79a1c086d6ef83aa1122ac0&req=diQlEMF2noRdUPMW3nq%2BgeharWeNs8BovAWW3iuSDjpSajVh7xxL0HAas61O%0AuG4jn71yBq2Lec5H96TaEPOnzX8%3D%0A)

Conecte sua conta do Trello clicando em **"Conectar Nova Conta"** e realize a autenticação. Esse processo só precisa ser realizado uma única vez;

![Imagem 27: Conecte sua conta do Trello clicando em "Conectar Nova Conta" e realize a autenticação. Esse processo só precisa ser…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426883974/a75902cbabd0017ee0529b5b4c60/2cb2540f-fdc1-4a96-8567-66d0741cae96?expires=1786536000&signature=9037c06358d300bb6025ad1261a89118a38a5d63f1bfa5b0cadb5c22d683772b&req=diQlEMF2nohYXfMW3nq%2BgdFkYqrrjlZHmzY5iqouJku8aBnXsrlhq%2BeyMaOT%0A876jhJaGVJVdf6PmXUVZVoiylm4%3D%0A)

Selecione a **área de trabalho**, o **espaço**, a **pasta** e a **lista** onde a tarefa de operação será criada;

![Imagem 28: Selecione a área de trabalho , o espaço , a pasta e a lista onde a tarefa de operação será criada;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426884489/8f5417f99d2628ea6fae6f34d499/71f0bef4-70b2-4cd5-96f9-1a005d5b3551?expires=1786536000&signature=af56d627264b2fce4b65b88140acda3028bafc92948cdca68f09e2edf0b2e74a&req=diQlEMF2mYVXUPMW3nq%2BgX8K7Zf%2B44I8YkbA8as4HB6vgdEKKwnV1cdntejF%0AXKcs6AeUZ6U4%2BPytOyWbYm1X17I%3D%0A)

Use o botão **"Inserir infos"** para mapear os dados no Trello:

- **Título da tarefa:** combine o nome do cliente e o produto contratado, por exemplo: [Onboarding] [[pessoa.nome]];
- **Descrição:** insira o briefing gerado pelo Gemini;
- **Responsável:** se desejar, atribua a tarefa ao responsável pela operação;
- **Data de vencimento:** se houver prazo definido no card do Ploomes, mapeie aqui.

![Imagem 29: Data de vencimento: se houver prazo definido no card do Ploomes, mapeie aqui.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426884975/12998fba645720eca7ab90cad635/7fc33733-f299-45e2-91c0-400f8db16020?expires=1786536000&signature=cd93be93f7677e41a4bf9d3dd3d6b7103995c091e34f44d1d65762acea34bc99&req=diQlEMF2mYhYXPMW3nq%2BgToZMQV8lZSXkd1pkUAwwEVxWgq%2BcUcNE8fOQCaH%0AgAYhiMPD1O5C8yve1KpQoCHk%2BUI%3D%0A)

Clique em **"Finalizar Automatização"**. Prontinho. Agora, sempre que um card for marcado como ganho no Ploomes, o Gemini gerará automaticamente o briefing de passagem de bastão e uma tarefa detalhada será criada no Trello para o time de operações.

![Imagem 30: Clique em "Finalizar Automatização" . Prontinho. Agora, sempre que um card for marcado como ganho no Ploomes, o Gemini…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2426885944/63f2e8c32e889c3d09553f6b259e/1261074b-9fbb-4a3d-92aa-f34241275251?expires=1786536000&signature=722ab85a1a531c7859d474563f28a9ba649bb2fe2d45ff3d6aa65cc387870c94&req=diQlEMF2mIhbXfMW3nq%2Bge8fE7DHkghwi6XvlwrSpvxJ0kRVj3Jkp2%2Fx6ABy%0AS3J%2BcUZFodAOANyPwOURf8WQiRI%3D%0A)

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização multi action. Para isso, é só clicar em **"Conectar Nova Ferramenta"**;

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar;

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar <https://pluga.zendesk.com/hc/pt-br/requests/new>.
