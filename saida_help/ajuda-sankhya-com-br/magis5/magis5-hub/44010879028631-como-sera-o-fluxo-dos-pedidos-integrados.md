---
id: "44010879028631"
titulo: "Como será o fluxo dos pedidos integrados com a Melhor Envio?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010879028631-Como-ser%C3%A1-o-fluxo-dos-pedidos-integrados-com-a-Melhor-Envio"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:49:14Z"
rotulos: ["sync_hc", "magis5", "magis5_204048155920", "sync_hash_3b6b2469f7d0"]
---

# Como será o fluxo dos pedidos integrados com a Melhor Envio?

## Veja como os pedidos sem logística própria do canal de venda serão processados automaticamente após a integração com a Melhor Envio.

---

⚠️ **Requisitos**

- Ter realizado as configurações iniciais de integração Melhor Envio com a Magis5, caso não tenha feito, [clique aqui](https://ajuda.magis5.com.br/como-integrar-a-melhor-envio-com-o-magis5-hub?hsLang=pt-br).

Alguns canais de venda oferecem soluções próprias de envio, como o Mercado Livre, com o Mercado Envios e o Mercado Coletas; o Magazine Luiza, com o Magalu Entregas; a Shopee, com o Shopee Express; e a Amazon, com o Amazon DBA.

Já em outros canais de venda, não há uma solução logística própria. Nesses casos, o vendedor precisa contratar uma transportadora ou uma solução de logística por conta própria.

⚠️ É importante destacar que, mesmo nos marketplaces que oferecem soluções logísticas próprias, produtos que ultrapassam os limites de dimensões estabelecidos podem perder essa opção de envio.

Nesses casos, os pedidos podem assumir status como **“Combine a Entrega com o seu comprador”**, **“Frete a combinar com o comprador”** ou **“Envio Próprio”**, entre outros. Quando isso acontece, o vendedor precisa contratar uma solução logística por conta própria.

Após realizar as configurações iniciais da integração com a Melhor Envio, os pedidos passarão a aparecer com o status **“Ag. Logística” (Aguardando Logística)**.

Esse status pode ser visualizado diretamente na **Dashboard**, conforme ilustrado na imagem abaixo.

![Imagem 1: Esse status pode ser visualizado diretamente na Dashboard , conforme ilustrado na imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/44010893048599)

Ao clicar no botão da Dashboard **"Ag. Logística"**conforme imagem anterior, ou seguindo em **"Pedidos"**no menu superior e depois clicando em**"Consultar Pedidos".**

![Imagem 2: Ao clicar no botão da Dashboard "Ag. Logística" conforme imagem anterior, ou seguindo em "Pedidos" no menu superior e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010899758231)

No filtro **“Canal de Venda”**, selecione o canal que foi integrado à Melhor Envio. Em seguida, no filtro **“Status”**, selecione **“Ag. Logística”** e clique no botão **“Buscar”**. 

![Imagem 3: No filtro “Canal de Venda” , selecione o canal que foi integrado à Melhor Envio. Em seguida, no filtro “Status” ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010884376855)

 Serão listados os pedidos que estão nesse status. Inicialmente, eles aparecerão com o **“Método de envio”** definido como **“Envio próprio - custom”**, conforme ilustrado na imagem abaixo. 

![Imagem 4: Serão listados os pedidos que estão nesse status. Inicialmente, eles aparecerão com o “Método de envio” definido como…](https://ajuda.sankhya.com.br/hc/article_attachments/44010893495959)

Nesse status, o HUB realizará automaticamente a validação das configurações iniciais e definirá o método de envio.

Se todas as condições estiverem corretas, o pedido terá seu status alterado para **“Ag. Separação”**, conforme ilustrado na imagem abaixo.

⚠️ Neste momento, o sistema realizará automaticamente a **cotação do frete, consulta de saldo, criação do envio e pagamento da etiqueta**.

Por isso, certifique-se de que sua conta da **Melhor Envio** esteja regularizada e com saldo disponível, para que o HUB possa realizar todas as operações necessárias por meio da API.

![Imagem 5: Por isso, certifique-se de que sua conta da Melhor Envio esteja regularizada e com saldo disponível, para que o HUB…](https://ajuda.sankhya.com.br/hc/article_attachments/44010900198807)

Caso o pedido permaneça no status anterior por mais de **15 minutos**, pode ter ocorrido algum erro durante a automação.

Nesse caso, clique em **“Editar”** no pedido para verificar e realizar os procedimentos necessários.

![Imagem 6: Nesse caso, clique em “Editar” no pedido para verificar e realizar os procedimentos necessários.](https://ajuda.sankhya.com.br/hc/article_attachments/44010872414359)

Em seguida, confira a mensagem de erro exibida no campo **“Informação”**. Com base no erro apresentado, realize os ajustes necessários no **Magis5 HUB** para corrigir a configuração e permitir que a automação prossiga normalmente. 

![Imagem 7: Em seguida, confira a mensagem de erro exibida no campo “Informação” . Com base no erro apresentado, realize os ajustes…](https://ajuda.sankhya.com.br/hc/article_attachments/44010880237335)

⚠️ Caso encontre alguma dificuldade para ajustar o erro, [entre em contato](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br) com o nosso suporte!

Após realizar os ajustes necessários, basta aguardar. O sistema tentará novamente atualizar o status do pedido automaticamente para **“Ag. Separação”**.

Com a atualização concluída, o pedido poderá seguir normalmente pelas próximas etapas do **processo de expedição**.

Durante o processo de expedição, o sistema realizará automaticamente a geração das etiquetas de envio por meio da API da Melhor Envio.

Em seguida, serão impressas a **etiqueta de envio** e a **NF ou Declaração de Conteúdo**, conforme as orientações apresentadas no manual de integração.
