---
id: "42427413919511"
titulo: "Como integrar o Ploomes com o Omie?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427413919511-Como-integrar-o-Ploomes-com-o-Omie"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:10Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452455", "sync_hash_0bdace860f32"]
---

# Como integrar o Ploomes com o Omie?

Omie é um ERP (Enterprise Resource Planning), que integramos com o nosso CRM da Ploomes por meio de uma integração Plug-and-Play. Por meio dessa integração é possível unir os dois sistemas através das entidades: Cliente, Produto, Venda, Produto da Venda, Serviço e Ordem de Serviço, e também os usuários no Ploomes, que são os vendedores no Omie.

## Como ativar a integração?

Após a criação do seu aplicativo Omie, acesse a seguinte URL: <https://developer.omie.com.br/my-apps/> e entre com seu login e senha

![Imagem 1: Após a criação do seu aplicativo Omie, acesse a seguinte URL: https://developer.omie.com.br/my-apps/ e entre com seu…](https://downloads.intercomcdn.com/i/o/754642662/f09b20dffda7c87dce897647/image.png?expires=1786536000&signature=54247d5bade3bd7b93e4177e5b9a0e02927cedc309f25d32abadc02bd7324e66&req=cyUjEM18m4ddFb4V1XW4gQLF344l%2BXVtSpXhU9sOWsLNoxh47jIfjSAy00P%2B%0A02LZjgS5pXAnPiZJXGlpNqnNeA%3D%3D%0A)

Na tela inicial estão as informações necessárias para realizar a integração. Vamos utilizar o App Key e App Secret para dar continuidade pelo Ploomes.

![Imagem 2: Na tela inicial estão as informações necessárias para realizar a integração. Vamos utilizar o App Key e App Secret para…](https://downloads.intercomcdn.com/i/o/754642955/6e118b66d8ade02e9066f7cf/image.png?expires=1786536000&signature=e3df70a99f8b72de4ee0562e64acf0ed4da461f26540188bf25b3a787c25c163&req=cyUjEM18lIRaFb4V1XW4gWmMvhhKEAohSm1U%2BD1XSb%2B%2FJE7o1jdzB6MuFCrS%0Agn7SDQnUCB0wojxj%2FedmZ2Pn3g%3D%3D%0A)

Após copiar as informações, basta acessar o Ploomes e navegar para a tela de Integrações Plug & Play pela opção Administração no menu lateral.

![Imagem 3: Após copiar as informações, basta acessar o Ploomes e navegar para a tela de Integrações Plug & Play pela opção…](https://downloads.intercomcdn.com/i/o/754647276/6d62101bab983d6a2121e6e5/image.png?expires=1786536000&signature=5bf8ca795982aab2762fcb8ea6761f661f51143720adb2ec170a75311091945d&req=cyUjEM15n4ZZFb4V1XW4gXoY6jfmx1zYmU2YYTNzRIpXD6rmwJx1ZtF4P43o%0A6njJUTmK%2Be8ACpoktfb%2B3AdKyg%3D%3D%0A)

Basta clicar na integração do Omie na lista e habilitar a integração.

![Imagem 4: Basta clicar na integração do Omie na lista e habilitar a integração.](https://downloads.intercomcdn.com/i/o/754648478/07c24bdc2f1753eb1ff3df7c/image.png?expires=1786536000&signature=196e686111a4cfc10e7e00b544d6e2ed97ff5e2619a27fa30f1965ca0d6f81cc&req=cyUjEM12mYZXFb4V1XW4gYPS2VY9X0Can2Zukhv%2FtqCs6QjsWLy64WoOUi16%0Amr9CtUN17%2F%2FNrEJPBzbgDzFwLw%3D%3D%0A)

Clique em “Autorizar integração”, isso abrira uma nova guia do navegador, nela você deve colar as informações de App Key e App Secret que copiamos anteriormente no Omie, após isso clique em “Confirmar” e em seguida “Ativar integração”.

![Imagem 5: Clique em “Autorizar integração”, isso abrira uma nova guia do navegador, nela você deve colar as informações de App…](https://downloads.intercomcdn.com/i/o/754649488/6da2e4c4781ae4830ee490b3/image.png?expires=1786536000&signature=9a3674792f9ad24d1aba1cbf9bb7b3547dd3dcec03881b90e3569835ed6cb556&req=cyUjEM13mYlXFb4V1XW4gbiz8hG%2FTrTHaWtD79B6PbgcU6fp9PU31Hd3PtnD%0AeIGQ1SFtICoYubyqRtU3MJXwaw%3D%3D%0A)

Após a ativação da integração, copie a URL gerada para criar os webhooks dentro do Omie.

![Imagem 6: Após a ativação da integração, copie a URL gerada para criar os webhooks dentro do Omie.](https://downloads.intercomcdn.com/i/o/754649778/7b5631bb4dd9dfa0d71f2e1d/image.png?expires=1786536000&signature=a543c22830e59525fae8b0fb1c540456f2f336e10e6e62f8d48f1fa00515da9a&req=cyUjEM13moZXFb4V1XW4gS39lrYs%2Bb%2BnfMYzejRME9C6ey5QJ2nXR4PGH%2Bkf%0AnMFtFSb8DKSCeZ87UcCFBhEoTA%3D%3D%0A)

Retorne ao painel do Omie e na barra inferior de opções do mesmo aplicativo que foi configurado no Ploomes (App Key) e clique em “Adicionar novo webhook”.

![Imagem 7: Retorne ao painel do Omie e na barra inferior de opções do mesmo aplicativo que foi configurado no Ploomes (App Key) e…](https://downloads.intercomcdn.com/i/o/754651943/2a8e9bd84b8c1d0d52095687/image.png?expires=1786536000&signature=79200320f210aa5383e0e5763da1dd98efc82b1f4b93db6cb75cc749c7e8a290&req=cyUjEMx%2FlIVcFb4V1XW4gdLgbggo1cyevDpjIFOV6Ym2scoPFeGayC2NLqnr%0AhZqXP85c4qqXJDF8wE%2FEKk3Dww%3D%3D%0A)

Cole a URL gerada pelo Ploomes no campo “Endpoint”.

![Imagem 8: Cole a URL gerada pelo Ploomes no campo “Endpoint”.](https://downloads.intercomcdn.com/i/o/754655442/ca65d6d4002f17fce9c60852/image.png?expires=1786536000&signature=ea3138e089b3a376cf4863ed3525565f9612e65044f027c8ab2455b39cf87f32&req=cyUjEMx7mYVdFb4V1XW4gbnrZS%2Flc0Vn%2FTHa2KTXytcb98nU01vjQINyF1oH%0AaJhqyVVMnIqztHp2dPko1s%2FWqA%3D%3D%0A)

## Adicionando entidades no mapeamento

Marque as seguintes entidades e clique em “SALVAR” ao final.

- ## Cliente Fornecedor

  ![Imagem 9: Cliente Fornecedor](https://downloads.intercomcdn.com/i/o/754655895/7056f6a3ea8cb5a0f87172d1/image.png?expires=1786536000&signature=2d74271b13356422ae9c7fda7abf78220ebbc8f6de56ab6ae7a0f2dda6753506&req=cyUjEMx7lYhaFb4V1XW4gZ2hK1dnoY6FKYcvAHkWNaxVlq6NqxXbxPO2Y1d8%0A%2FapWp9J%2BCXmz697%2F1WYUnM6MQg%3D%3D%0A)
- ## Produto (Caso utilize marktplace ou pdv marcar as opções referentes a elas também)

  ![Imagem 10: Produto (Caso utilize marktplace ou pdv marcar as opções referentes a elas também)](https://downloads.intercomcdn.com/i/o/754659735/17e1795276ac55a17dfb31c2/image.png?expires=1786536000&signature=56b44ba55a9f347a398b75e55b853e649d35f64f4eca9360cdfb3511a4a492fa&req=cyUjEMx3moJaFb4V1XW4gYWRk5h4o1b37VBfSuDj47oPuCx64KR8xxuRDUP8%0AEoJhI6GcieLRC6zyD3dYQ%2Ftg7A%3D%3D%0A)
- ## Serviço

  ![Imagem 11: Serviço](https://downloads.intercomcdn.com/i/o/754660131/f909172c014fa21791f7c68c/image.png?expires=1786536000&signature=2979ed6602c2a46aa624e1be0f2fb321b1b4469daf82f4d76c3881f04e6af87b&req=cyUjEM9%2BnIJeFb4V1XW4gZgNgMijupCpbcuA20du49jbb3BgCnMsQEtGfnOx%0AGUVJqZwrKXayDwz0huIZRxNUww%3D%3D%0A)
- ## Venda Produto

![Imagem 12: Venda Produto](https://downloads.intercomcdn.com/i/o/754660379/15b1673222079e67ba4b4627/image.png?expires=1786536000&signature=aacb72f9d57b588726c2478f5ec41468f2e555d11f383e0ab39df00f26d47b7d&req=cyUjEM9%2BnoZWFb4V1XW4gSl5U84X03bG9zM5L4Dsqko0m2K7VW%2BbGwCMpFcw%0AdBeIX8%2B2pY2yu%2FmuUcR7b9dVVg%3D%3D%0A)

- ## Vendedor

![Imagem 13: Vendedor](https://downloads.intercomcdn.com/i/o/754660632/1425788b02a1bb22bf6d03c6/image.png?expires=1786536000&signature=3adafeeb1c76689e6a6e29ccdd6f0fa0f7d5cddea01914aaf9c263f2ad1ac53a&req=cyUjEM9%2Bm4JdFb4V1XW4geweV%2Fi0Y%2BQ7gQc8E8G%2FUJMUJzBgF9IdEnjSVc0G%0AOh2hg5z%2Bm5R4zpe0uTF%2F34aeAg%3D%3D%0A)

Escolha se há a necessidade de sincronização dos históricos de pedidos e de vendas criados antes da ativação da integração. Se essas opções estiverem desligadas, serão sincronizados somente os pedidos criados após a ativação da integração.

![Imagem 14: Escolha se há a necessidade de sincronização dos históricos de pedidos e de vendas criados antes da ativação da…](https://downloads.intercomcdn.com/i/o/754660973/7fc7d5ba4b95e82b49eb4046/image.png?expires=1786536000&signature=df930fc7459465f25da3481c8b1ce34a1bd5bc7d8e75cb1781db7d61dbe01ee6&req=cyUjEM9%2BlIZcFb4V1XW4gaB4gOO%2F71DsxNEKdmxeJFf8VmfhnCuEX2egMNRe%0A4uKAdHmldaHlcxFGmnTD9FpIVw%3D%3D%0A)

Mapeie os campos que vão ter uma comunicação entre o Ploomes e o Omie. Se atente à tabela de correspondência entre os campos Omie e o tipo de campo no Ploomes. Quando acabar, finalize a ativação da integração clicando em “Atualizar integração”.

![Imagem 15: Mapeie os campos que vão ter uma comunicação entre o Ploomes e o Omie. Se atente à tabela de correspondência entre os…](https://downloads.intercomcdn.com/i/o/754661480/91a9251cd460cc17f96d648b/image.png?expires=1786536000&signature=740fea3c9818651b890a405fb3f1512f8fbdcbb6dcc9999a767ea83b5baf79e8&req=cyUjEM9%2FmYlfFb4V1XW4gTuPKgS40T%2BCmMsRX1eHvuQLrkKJDKz%2BK1j4uykP%0A%2FbzvY909Nz6ZYrlkNfYUwOJYeQ%3D%3D%0A)

## Limites da API Omie:

- Limite de até 240 requisições por minuto;
- Limite de até 4 requisições simultâneas por segundo para consultas;
- Requisições redundantes liberadas a cada 60 segundos (\*);

## Limites da API Ploomes:

- Nossa API atualmente está apta a processar até 120 requisições por minuto, considerando todos os usuários de integração da conta em conjunto, portanto, em caso de a sua solução precisar executar muitas requisições simultâneas, esteja preparado para processar respostas HTTP 429 - Too Many Requests.
- Algumas entidades possuem um limite de recursos que pode ser obtido em uma solicitação GET. Esse limite é de 300 itens para as entidades: Contacts, Deals, Cities, Tasks, Orders e Quotes.
- O máximo payload aceito pela API é de 10MB.

Os limites e recomendações de uso estão presentes na documentação oficial: <https://developers.ploomes.com/>

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
