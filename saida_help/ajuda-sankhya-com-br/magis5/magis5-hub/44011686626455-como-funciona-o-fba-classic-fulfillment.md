---
id: "44011686626455"
titulo: "Como funciona o FBA Classic - Fulfillment by Amazon dentro do Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011686626455-Como-funciona-o-FBA-Classic-Fulfillment-by-Amazon-dentro-do-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:09:24Z"
rotulos: ["sync_hc", "magis5", "sync_hash_18a60ad33b07", "magis5_204055206965"]
---

# Como funciona o FBA Classic - Fulfillment by Amazon dentro do Magis5 Hub?

## O FBA Classic é um dos serviços de logística oferecidos pela Amazon, onde o seller envia seus produtos para o Centro de Distribuição da Amazon e eles cuidam do empacotamento, logística e pós venda dos pedidos.

---

Este manual é direcionado a clientes que utilizam a Amazon, estão devidamente integrados e já participam do programa FBA Classic. Caso você queira efetuar a integração com a Amazon, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44011406798615) e veja nosso manual sobre o assunto.

Entenda como funciona, preços e tarifas, benefícios e procedimentos para registrar-se no FBA Classic acessando o link: [venda.amazon.com.br/cresca/fba](https://venda.amazon.com.br/cresca/fba)

Se você já participa do programa FBA Classic da Amazon, vamos te mostrar como funciona no Magis5 Hub a mudança de logística no anúncio.

✅ **Para pedidos com logística FBA Classic**, o Magis5 HUB realiza a importação com um intervalo de **três a um dia antes da data atual (D-3 a D-1).**

Por exemplo, se hoje é dia 20, o sistema importará os pedidos processados entre os dias 17 e 19. Os pedidos do próprio dia 20 serão importados apenas no dia 23, respeitando o intervalo definido.

Sumário:

[1) Como converter anúncios para FBA Classic](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011686626455-Como-funciona-o-FBA-Classic-Fulfillment-by-Amazon-dentro-do-Magis5-Hub#um)

[2) Como ativar a importação de pedidos FBA Classic](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011686626455-Como-funciona-o-FBA-Classic-Fulfillment-by-Amazon-dentro-do-Magis5-Hub#dois)

[3) Como consultar os pedidos do FBA Classic](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011686626455-Como-funciona-o-FBA-Classic-Fulfillment-by-Amazon-dentro-do-Magis5-Hub#tres)

[4) Como fazer o download das NFes do FBA Classic](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011686626455-Como-funciona-o-FBA-Classic-Fulfillment-by-Amazon-dentro-do-Magis5-Hub#quatro)

### 1) Como converter anúncios para FBA Classic no Magis5 Hub

Os anúncios FBA Classic devem passar pelo processo de indicar para a Amazon que estão nesse programa para aparecerem corretamente no site e não serem considerados Logística Própria do Vendedor.

Existe uma funcionalidade para essa conversão no Magis5 Hub. Para isso, no menu da parte superior, vá para **"Produtos e anúncios"**, depois **"Produtos e anúncios"** e por último clique em **"Anúncios publicados"**.

![Imagem 1: Existe uma funcionalidade para essa conversão no Magis5 Hub. Para isso, no menu da parte superior, vá para "Produtos e…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-39-40-0376-PM.png?width=681&height=443&name=image-png-Mar-06-2024-12-39-40-0376-PM.png)

**Localize e selecione** o anúncio da Amazon que deseja realizar a conversão.

![Imagem 2: Localize e selecione o anúncio da Amazon que deseja realizar a conversão.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-32-48-8856-PM.png?width=660&height=326&name=image-png-Mar-06-2024-12-32-48-8856-PM.png)

Com o anúncio selecionado, clique em "Opções" na parte direita da tela e depois **"Alterar Fullfilment"**.

![Imagem 3: Com o anúncio selecionado, clique em "Opções" na parte direita da tela e depois "Alterar Fullfilment" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-34-26-7277-PM.png?width=522&height=341&name=image-png-Mar-06-2024-12-34-26-7277-PM.png)

Uma nova janela trará a listagem dos anúncios selecionados. Confira se selecionou corretamente e então no **"Tipo de programa"** selecione qual logística deseja utilizar no anúncio. Finalize clicando no botão **"Salvar alterações"**.

![Imagem 4: Uma nova janela trará a listagem dos anúncios selecionados. Confira se selecionou corretamente e então no "Tipo de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-42-52-0733-PM.png?width=688&height=649&name=image-png-Mar-06-2024-12-42-52-0733-PM.png)

É muito importante que o seller realize essa conversão, pois é através dela que sabemos que quando cair um pedido para aquele anúncio com a logística FBA (Onsite e/ou Classic), o sistema não deve realizar a atualização de estoque via API, e caso isso ocorra (esquecer de realizar a conversão), o produto passa a ser logística própria do seller novamente.

**⚠️ A gestão de estoque de anúncios FBA Classic é feita pela própria Amazon.**

### 2) Como ativar a importação de pedidos FBA Classic para a Magis5 Hub

No Magis5 Hub, vá até **"Configurações"**, depois até **"Integrações"** e por último clique em **"Marketplaces"**.

![Imagem 5: No Magis5 Hub, vá até "Configurações" , depois até "Integrações" e por último clique em "Marketplaces" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-06-2024-02-02-29-2745-PM.png?width=620&height=479&name=image-png-Feb-06-2024-02-02-29-2745-PM.png)

Localize a integração da conta Amazon desejada e clique no botão **"Editar"**.

![Imagem 6: Localize a integração da conta Amazon desejada e clique no botão "Editar" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-52-55-7872-PM.png?width=688&height=141&name=image-png-Mar-06-2024-12-52-55-7872-PM.png)

Em seguida, vá até a aba de **'Logística'** e ative a flag **"Baixar pedidos FBA Classic - Logística da Amazon"**

![Imagem 7: Em seguida, vá até a aba de 'Logística' e ative a flag " Baixar pedidos FBA Classic - Logística da Amazon"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-54-41-5261-PM.png?width=688&height=464&name=image-png-Mar-06-2024-12-54-41-5261-PM.png)

Pronto, agora a Amazon passa a enviar novos pedidos FBA Classic para a sua conta Magis5 Hub!

### 3) Como consultar os pedidos do FBA Classic no Magis5 Hub

Para identificar os pedidos do FBA Classic, acesse os pedidos indo até **"Pedidos"** no menu superior e depois clique em **"Consultar Pedidos"**.

![Imagem 8: Para identificar os pedidos do FBA Classic, acesse os pedidos indo até "Pedidos" no menu superior e depois clique em…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-58-49-8117-PM.png?width=660&height=317&name=image-png-Mar-06-2024-12-58-49-8117-PM.png)

**Selecione sua loja Amazon** no filtro 'Canal de Venda'.

![Imagem 9: Selecione sua loja Amazon no filtro 'Canal de Venda'.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-01-01-05-4760-PM.png?width=560&height=219&name=image-png-Mar-06-2024-01-01-05-4760-PM.png)

Na lista de pedidos, é possível diferenciar os pedidos  FBA Classic dos demais através do campo **“Tipo de Logística”, onde é apresentado o logo do serviço.**

![Imagem 10: Na lista de pedidos, é possível diferenciar os pedidos FBA Classic dos demais através do campo “Tipo de Logística”,…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-01-07-16-2692-PM.png?width=597&height=278&name=image-png-Mar-06-2024-01-07-16-2692-PM.png)

### 4) Como fazer o download das NFes do FBA Classic no Magis5 Hub

Semelhante ao item 3 deste manual, acesse os pedidos indo até **"Pedidos"** no menu superior e depois clique em **"Consultar Pedidos"**.

![Imagem 11: Semelhante ao item 3 deste manual, acesse os pedidos indo até "Pedidos" no menu superior e depois clique em "Consultar…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-58-49-8117-PM-webp.webp?width=660&height=317&name=image-png-Mar-06-2024-12-58-49-8117-PM-webp.webp)

**Selecione sua loja Amazon** no filtro 'Canal de Venda' e a **Fulfillment**no filtro 'Tipo de logística'.

![Imagem 12: Semelhante ao item 3 deste manual, acesse os pedidos indo até "Pedidos" no menu superior e depois clique em "Consultar…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2025-06-46-00-0411-PM.png?width=448&height=216&name=image-png-Jul-31-2025-06-46-00-0411-PM.png)

Na lista de pedidos, é possível conferir os pedidos FBA Classic e baixar o XML das NF-es de venda de mercadoria dos pedidos que já possuírem o número da NF-e e a Chave de acesso de forma massiva ou individual.

**1) Massivo:**Selecione os pedidos desejados e então no começo da listagem dos pedidos, clique em **"Baixar notas fiscais".**

**2) Individual:** Em cada pedido, clique nos 3 pontinhos, **"Baixar nota fiscal".**

![Imagem 13: Semelhante ao item 3 deste manual, acesse os pedidos indo até "Pedidos" no menu superior e depois clique em "Consultar…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jul-31-2025-06-41-59-4616-PM.png?width=688&height=414&name=image-png-Jul-31-2025-06-41-59-4616-PM.png)

**⚠️ Para pedidos feitos com logística FBA Classic**, o Magis5 Hub baixará/importará para dentro do hub o XML dos pedidos processados até o prazo de **dois dias anteriores**(D-2). **Por exemplo:**se estamos no dia 20, estará disponível para download do XML os pedidos feitos até o dia 18, e os pedidos do dia atual serão importados apenas no dia 22.

**⚠️ Para pedidos FBA Classic que os XMLs são diferentes de venda de mercadoria,** deverão ser baixados diretamente pelo Seller Central da Amazon.
