---
id: "42427668735895"
titulo: "Como integrar o Ploomes com o WhatsApp Business API (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427668735895-Como-integrar-o-Ploomes-com-o-WhatsApp-Business-API-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:06:27Z"
rotulos: ["sync_hc", "ploomes", "ploomes_12461518", "sync_hash_61b7ace72d06"]
---

# Como integrar o Ploomes com o WhatsApp Business API (via Pluga)

**Observação**:

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

---

## O que esta integração faz?

A cada **atualização de status em um card** do Ploomes, **enviar mensagem** a partir de um modelo no WhatsApp Business API.

Ou então, quando um **card** chegar a uma **etapa de um funil** no Ploomes, enviar mensagem a partir de um modelo no WhatsApp Business API.

## Requisitos

- Uma conta no Ploomes;
- Uma conta na [Pluga](https://pluga.co/);
- Acesso ao WhatsApp Business API.

---

## Criando uma integração entre Ploomes (origem) e WhatsApp Business API (destino)

Acesse a [Pluga](https://pluga.co/) e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753408892/bed7c9a6bbb7e371b2fafa091798/a62ad9ad-7a75-4d09-86d6-6d666d9a9530?expires=1786536000&signature=0f5cae87ca1cd6a251a633f765da3eafb6e4ee7daf90545398430a40d188085f&req=dSciFc1%2BlYlWW%2FMW3nq%2Bgcy%2BB7UesGGhnxf4lLevuCq7tgnkFZ3rnb89O%2Fap%0AkN4G1xE%2B2jTr5Fa8DpJ86yVHLCY%3D%0A)

Na área de usuário da Pluga, clique em “**Criar Automatização**”;

![Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753409512/0538a037d36303cd272d72360faf/64fb166d-99e8-4f8a-a353-3d0b7ac08aec?expires=1786536000&signature=038d63ffa8424fd69356b7e44d08cc06aeaef7c0015569ce8c7a83edbc89c5ba&req=dSciFc1%2BlIReW%2FMW3nq%2BgaIvbit8srnnsg3dl0%2BCvgN2GLyAjhdm0G88pz1K%0ArYAJ0NibsR%2BBfDjr1DBtBIfJ4ME%3D%0A)

Dê um título para a sua automatização. Isso vai ser útil caso você queira editá-la no futuro;

![Imagem 3: Dê um título para a sua automatização. Isso vai ser útil caso você queira editá-la no futuro;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753409800/629250c0c3df285810997e1d18cb/4c5c8cf2-af63-42a0-aa37-0f7da604eac3?expires=1786536000&signature=313f61a200c3b6ede69a7565a8e374054b96f2cb1f36a77bd88390f18213cab5&req=dSciFc1%2BlIlfWfMW3nq%2BgSzwyM4Q38uM9Q4rYgxtxMd4JKPClnc7TIuOgdnl%0AOxN1yivJngSOoF2XFpS8T9dLGKQ%3D%0A)

Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o gatilho, ou seja, o acontecimento na ferramenta que dará início à sua automatização. Neste caso de uso vamos selecionar “**Card alcança etapa no funil**”, e clicar em “**Continuar**”;

![Imagem 4: Selecione a ferramenta que dará início a automatização. Neste caso de uso, selecionaremos o Ploomes. Escolha também o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753410061/b8af25c6fcba0f9207353c540d37/10def24d-199f-434e-bd36-e2d4314dcee8?expires=1786536000&signature=25a867c6413c92e91fb1fd3fb8f440291b0be3d60fe4edc8183284203bcd2be5&req=dSciFc1%2FnYFZWPMW3nq%2BgViq5QzwKHYqHNP2%2FMIQWNEada578tLv3cP%2FgIbk%0A%2Bfr46FFVrX112crs6S8P8DLWYzk%3D%0A)

Conecte sua conta no Ploomes. Basta clicar em “**Conectar Nova Conta**” e realizar a autenticação. Esse processo só precisa ser realizado uma única vez. Ao criar outras automatizações com o Ploomes, sua conta já aparecerá listada entre as contas conectadas Caso seja a sua primeira vez conectando a sua conta do Ploomes, clique em **"Veja o passo a passo para encontrar suas chaves de acesso"** e siga o breve tutorial;

![Imagem 5: Conecte sua conta no Ploomes. Basta clicar em “ Conectar Nova Conta ” e realizar a autenticação. Esse processo só…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753410286/4075ce1d83b205363f5e5a16d9ae/ef72d9e2-1c00-478b-84f7-f6ed10dde0aa?expires=1786536000&signature=c2d08ae640b9d12bb810427173609b9483122bf21fd2d648b02de4a34f6712ca&req=dSciFc1%2FnYNXX%2FMW3nq%2Bgbm%2BVhIiRP5QyBHZ%2BGPoWmLmAPMkIhDshABahZxz%0AZO4R6P6QeyP8qXQkA6j%2BWAEtLF0%3D%0A)

Defina o **funil** e a **etapa do funil** que deverão acionar a automatização assim que o card os alcançar. Em seguida, clique em “Salvar e Continuar”;

![Imagem 6: Defina o funil e a etapa do funil que deverão acionar a automatização assim que o card os alcançar. Em seguida, clique…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753410518/c1e602a1e92ef77f38a3f540c220/c5af1ad8-f73c-410b-96a2-3d2e60ad06dc?expires=1786536000&signature=f35d826524bd85714527031675c93c4485b702e4d434876080368168a29f2bf8&req=dSciFc1%2FnYReUfMW3nq%2BgRVD%2FlEV5alRP%2BlsE7W4cm3Clg4Z%2BU3ZEJz8PT91%0AC%2BZZXhwr4D3SBPrQqCLz%2FGgAEsg%3D%0A)

Caso queira, você também pode criar filtros para a automatização usando como critério qualquer um dos campos da Ploomes. Você pode adicionar múltiplos critérios a um filtro, e a forma como eles se relacionam determina o comportamento da sua automatização. Para adicionar mais de um critério, utilize os botões **“E”** ou **"OU”**.

Para nosso exemplo, iremos considerar apenas negócios que estejam sob a responsabilidade de um usuário específico da Ploomes **(“Dono do Card = Vendedor Pluga”)** e que o telefone não esteja vazio **(“Cliente: Números de Telefone = Não está vazio”)**. Em seguida, clicar em “Salvar e Continuar”;

![Imagem 7: Para nosso exemplo, iremos considerar apenas negócios que estejam sob a responsabilidade de um usuário específico da…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753410826/3da8dfd601a776b1eebb6d0a2003/822868f3-8da7-4107-8fdf-fba8fcbd5434?expires=1786536000&signature=babdb1efa336d8e22fe93ecebe1a033f4834b0589aa3c1b17153fa7053ef69c2&req=dSciFc1%2FnYldX%2FMW3nq%2BgXMH%2BLpHknAFnydS8LCON1hkELhKojPDRZCN7t1I%0AWIsyzCwGIUtgUmDK5OMVr%2BozeMc%3D%0A)

Com a sua conta da Ploomes configurada, clique em **“Conectar Nova Ferramenta”**;

![Imagem 8: Com a sua conta da Ploomes configurada, clique em “Conectar Nova Ferramenta” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753411123/448cfd1979b75a1a8820da4fa2db/7336bfe0-3471-4987-8c60-974687e52fe4?expires=1786536000&signature=8855e8e71b295f2f1450291750554dbe56c6413ce91a8b837e47386448afb8be&req=dSciFc1%2FnIBdWvMW3nq%2BgYlPxpSwGq0LSvpVMq7fhfBQCAzDpAuz9WXx8w47%0A%2B4LVr7J71FDepxWfS6eVBPfpRJI%3D%0A)

Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “**WhatsApp Business API**” e uma ação, ou seja, a tarefa que será executada na ferramenta de destino. Neste caso, selecione **“Enviar mensagem a partir de um modelo”** e clique em **“Salvar e Continuar”**;

![Imagem 9: Em seguida, você precisa conectar a ferramenta de destino da sua automatização. Basta selecionar “ WhatsApp Business…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753411382/2a1f82baeadf9ba60d00b510b3ba/0c56aec4-f8d6-4199-ab37-ffcba9739cdb?expires=1786536000&signature=b70b082a73201a8e0c98993f781d6ff2f50a54c5c89311447756b6c281bf96d9&req=dSciFc1%2FnIJXW%2FMW3nq%2Bgapb1AMpqBf6lxYS34OpOJmf7anrywjQSsM0Adbk%0A5BVaE3%2BoxyrV%2BWy3rjOrLK2ACsI%3D%0A)

Assim como fez com a Ploomes, você irá autenticar sua conta do Facebook, conectando-a na Pluga. Clique em **“Conectar Nova Conta”** e faça o login. Nas próximas vezes, a conta já estará entre as listadas;

![Imagem 10: Assim como fez com a Ploomes, você irá autenticar sua conta do Facebook, conectando-a na Pluga. Clique em “Conectar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753411634/f1d79af4b43693f50d5c71851329/84075aad-958c-4640-9703-506309043c2d?expires=1786536000&signature=652fe4e9c1b1fa81da3f2d59f796bff4aa080dcbbc318af2dc722c9d760d7970&req=dSciFc1%2FnIdcXfMW3nq%2BgWPd3vYcX7raQL5kW2%2BCuUs7Kphp%2BISRq4oEHvI7%0Ah9%2FN%2FqHZacWLLx07%2B64GivpJ%2By8%3D%0A)

Atente-se aos pré requisitos para que a sua automatização com o **WhatsApp** funcione corretamente:

- É necessária uma versão do Whatsapp Business no smartphone superior à 2.24.17;
- Que tenha, também, um número que nunca tenha sido usado no WhatsApp Business API anteriormente em quaisquer outros provedores terceiros;
- Um cartão de débito ou crédito disponível, pois diferentemente dos outros serviços, as mensagens do Whatsapp Business API são cobradas pela Meta.

Após verificar se atende aos pré-requisitos, siga para a conexão de sua conta com a **Pluga**. Durante a autenticação, você realizará o login em sua conta do **Facebook**, selecionando ou criando um portfólio comercial que será associado a um número de telefone. Assim, você poderá conectar a uma conta de **WhatsApp Business** existente, ou então criar uma nova conta;

![Imagem 11: Após verificar se atende aos pré-requisitos, siga para a conexão de sua conta com a Pluga . Durante a autenticação,…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753412206/bea4b717c27d346119544419eee1/6fde277d-dbe3-480c-bc21-5269d259cf9a?expires=1786536000&signature=4f17582cf9372046d4912aa54478be52f04534b73402ed3748e27abe2a1fb019&req=dSciFc1%2Fn4NfX%2FMW3nq%2BgSXeZjfD7xKB%2BQMWtFrR0R0PgEcX6zm0Xbwivg6y%0AMYmn31kgEPhXzONhJDzEQIgTvmE%3D%0A)

Após inserir o seu número de telefone, você confirmará os acessos da Pluga e receberá um **código de verificação**. Com sua conta conectada, ajuste as opções, selecionando o **número de remetente** e um **modelo de mensagem do WhatsApp**, que pode ser criado [aqui](https://business.facebook.com/latest/whatsapp_manager/message_templates). Os modelos de mensagem do WhatsApp permitem que as empresas usem modelos existentes aprovados previamente para enviar mensagens estruturadas a clientes que concordaram em receber notificações. Para ter mais detalhes sobre como criar o seu modelo, confira este [guia](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) da própria Meta.

Com tudo configurado, clique em **“Salvar e Continuar”**;

![Imagem 12: Com tudo configurado, clique em “Salvar e Continuar” ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753412574/20a3a86c60a48693a07000c867eb/b03c7499-47ef-402f-8a6b-8fcff8fb612c?expires=1786536000&signature=c561f473970aed954b436021f62e7e11f8a131f478aac089c382afcfa9c10b17&req=dSciFc1%2Fn4RYXfMW3nq%2BgQMK8EdiqLXg5F1gJhS6%2Fiq3Kr7symRHToYYnvIP%0AISOWpprCFaRswlCGK5aCiGL0350%3D%0A)

Em seguida, selecione o campo da Ploomes que trará telefones de destinatários para a sua automatização;

![Imagem 13: Em seguida, selecione o campo da Ploomes que trará telefones de destinatários para a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753412894/b9d1b949e43652baf33f6ba4204a/a1e395be-0851-49c7-af49-4773fad3ba6d?expires=1786536000&signature=5db3cf1473d54138c75bce934d38480f2057e00502b7c505ed282f8109167c2f&req=dSciFc1%2Fn4lWXfMW3nq%2BgV%2F7Z%2FnakAl3V52yC%2BoztySxjenik%2FyIoQ%2Bs%2BS8Z%0AEkzGP8ZvXTlFi9oO%2BfvWTuQyO1A%3D%0A)

Através do botão **“Inserir infos”**, você seleciona as informações da Ploomes que serão inseridas em cada variável de template de mensagem do WhatsApp Business API. Em nosso exemplo, criamos duas variáveis: **#{{name}}** e **#{{empresa}}**. Após as configurações, clique em “Salvar e Continuar”;

![Imagem 14: Através do botão “Inserir infos” , você seleciona as informações da Ploomes que serão inseridas em cada variável de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753413182/2539e9716076303a26cb4cd356a6/005b5e38-e37d-4757-8817-a715a1dace88?expires=1786536000&signature=5ecd252b79ff66fc482a1af15a7f0c5f9c8c575613d5a6a14b1cc7dbc57fe82a&req=dSciFc1%2FnoBXW%2FMW3nq%2BgfIkoscPp4eHorfSjwbq6F%2B4XHwVsKU3nJXMn1wR%0AIxD3Ud5NiJFURfBvr1vwJVXT144%3D%0A)

Depois de preencher todas as informações necessárias, é só clicar em **“Finalizar automatização”** e prontinho! Agora, sempre que um negócio chegar em uma determinada etapa na Ploomes, uma mensagem será enviada pelo WhatsApp Business API.

Depois de enviada essa primeira mensagem, você pode continuar a conversa diretamente pelo seu aplicativo WhatsApp Business;

![Imagem 15: Depois de enviada essa primeira mensagem, você pode continuar a conversa diretamente pelo seu aplicativo WhatsApp…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1753413516/b617ae9e50b6c1a06001ecd8686f/b8507a43-308c-4f28-a48c-b16216b23da8?expires=1786536000&signature=7041b685db028cb97a5d81aca89ef71dc5bbfeb6e1d14f3a2f23122e80cce48d&req=dSciFc1%2FnoReX%2FMW3nq%2BgUuNUH%2FqnJx5OYgLORk7%2FfCIzeRGGjGy3W72oMPM%0Aq%2BUJmPdWM5ePOjzZEVeUNyKx54o%3D%0A)

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
