---
id: "44011768653335"
titulo: "Como funciona o FBA Onsite - Logística da Amazon dentro do Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:11:34Z"
rotulos: ["sync_hc", "magis5", "sync_hash_3c49bdb6c18c", "magis5_204056235147"]
---

# Como funciona o FBA Onsite - Logística da Amazon dentro do Magis5 Hub?

## O FBA Onsite é um dos serviços de logística disponibilizados pela Amazon, onde o anúncio possui selo Prime. Você vende, embala e a Amazon coleta e cuida do pós-vendas.

---

Este manual é direcionado a clientes que utilizam a Amazon, estão devidamente integrados e já participam do programa FBA Onsite. Caso você queira efetuar a integração com a Amazon, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44011406798615) e veja nosso manual sobre o assunto.

Entenda como funciona, preços e tarifas, benefícios e procedimentos para registrar-se no FBA Onsite acessando o link: [venda.amazon.com.br/cresca/fba-onsite](https://venda.amazon.com.br/cresca/fba-onsite)

Se você já participa do programa FBA Onsite da Amazon, vamos te mostrar como funciona no Magis5 Hub a mudança de logística no anúncio, a baixa dos pedidos FBA Onsite, controle de estoque, consulta de pedidos, envio da nota fiscal e impressão de etiquetas.

Sumário:

[1) Como converter anúncios para FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#um)

[2) Como ativar a importação de pedidos FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#dois)

[3) Funcionamento do controle de estoque do FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#tres)

[4) Como consultar os pedidos do FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#quatro)

[5) Como emitir nota fiscal na FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#cinco)

[6) Como imprimir etiquetas da Amazon FBA Onsite](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011768653335-Como-funciona-o-FBA-Onsite-Log%C3%ADstica-da-Amazon-dentro-do-Magis5-Hub#seis)

### 1) Como converter anúncios para FBA Onsite no Magis5 Hub

Os anúncios FBA Onsite devem passar pelo processo de indicar para a Amazon que estão nesse programa para aparecerem corretamente no site e não serem considerados Logística Própria do Vendedor.

Existe uma funcionalidade para essa conversão no Magis5 Hub. Para isso, no menu da parte superior, vá para **"Produtos e anúncios"**, depois **"Produtos e anúncios"** e por último clique em **"Anúncios publicados"**.

![Imagem 1: Existe uma funcionalidade para essa conversão no Magis5 Hub. Para isso, no menu da parte superior, vá para "Produtos e…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-39-40-0376-PM.png?width=681&height=443&name=image-png-Mar-06-2024-12-39-40-0376-PM.png)

**Localize e selecione** o anúncio da Amazon que deseja realizar a conversão.

![Imagem 2: Localize e selecione o anúncio da Amazon que deseja realizar a conversão.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-32-48-8856-PM.png?width=660&height=326&name=image-png-Mar-06-2024-12-32-48-8856-PM.png)

Com o anúncio selecionado, clique em "Opções" na parte direita da tela e depois **"Alterar Fullfilment"**.

![Imagem 3: Com o anúncio selecionado, clique em "Opções" na parte direita da tela e depois "Alterar Fullfilment" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-34-26-7277-PM.png?width=522&height=341&name=image-png-Mar-06-2024-12-34-26-7277-PM.png)

Uma nova janela trará a listagem dos anúncios selecionados. Confira se selecionou corretamente e então no**"Tipo de programa"** selecione qual logística deseja utilizar no anúncio. Finalize clicando no botão **"Salvar alterações"**.

![Imagem 4: Uma nova janela trará a listagem dos anúncios selecionados. Confira se selecionou corretamente e então no "Tipo de…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-42-52-0733-PM.png?width=688&height=461&name=image-png-Mar-06-2024-12-42-52-0733-PM.png)

💡 Alguns produtos podem acabar classificados para oferta híbrida dentro da Amazon, ou seja, o mesmo produto estando disponível tanto para logística própria do vendedor quanto para logística da Amazon Onsite.
A Amazon orienta que os produtos possuam **apenas uma** logística.

É muito importante que o vendedor realize essa conversão, pois é através dela que sabemos que quando cair um pedido para aquele anúncio com a logística FBA (Onsite e/ou Classic), o sistema não deve realizar a atualização de estoque via API, e caso isso ocorra (esquecer de realizar a conversão), o produto passa a ser logística própria do seller novamente.

**⚠️ A gestão de estoque de anúncios com logística FBA Onsite é feita apenas pelo seller via Painel da Amazon.**

### 2) Como ativar a importação de pedidos FBA Onsite para o Magis5 Hub

No Magis5 Hub, vá até **"Configurações"**, depois até **"Integrações"** e por último clique em **"Marketplaces"**.

![Imagem 5: No Magis5 Hub, vá até "Configurações" , depois até "Integrações" e por último clique em "Marketplaces" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Feb-06-2024-02-02-29-2745-PM.png?width=620&height=479&name=image-png-Feb-06-2024-02-02-29-2745-PM.png)

Localize a integração da conta Amazon desejada e clique no botão **"Editar"**.

![Imagem 6: Localize a integração da conta Amazon desejada e clique no botão "Editar" .](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-52-55-7872-PM.png?width=688&height=107&name=image-png-Mar-06-2024-12-52-55-7872-PM.png)

Em seguida, vá até a aba de **'Logística'** e ative a flag **"Baixar pedidos FBA Onsite - Logística da Amazon"**

![Imagem 7: Em seguida, vá até a aba de 'Logística' e ative a flag "Baixar pedidos FBA Onsite - Logística da Amazon"](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-03-43-25-8372-PM.png?width=688&height=333&name=image-png-Mar-06-2024-03-43-25-8372-PM.png)

Pronto, agora a Amazon passa a enviar novos pedidos FBA Onsite para a sua conta Magis5 Hub!

**Somente os pedidos feitos após a integração ficarão disponíveis na Magis5. Pedidos antigos não irão aparecer.**

### 3) Funcionamento do controle de estoque do FBA Onsite no Magis5 Hub

Mesmo que os produtos estejam no centro de distribuição do vendedor, **o controle de estoque precisa ser feito pelo painel da Amazon**, ou seja, não é possível realizar alterações de estoque via API quando o anúncio está com a logística FBA Onsite.

### 4) Como consultar os pedidos do FBA Onsite no Magis5 Hub

Para identificar os pedidos do FBA Onsite, acesse os pedidos indo até **"Pedidos"** no menu superior e depois clique em **"Consultar Pedidos"**.

![Imagem 8: Para identificar os pedidos do FBA Onsite, acesse os pedidos indo até "Pedidos" no menu superior e depois clique em…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-12-58-49-8117-PM.png?width=660&height=317&name=image-png-Mar-06-2024-12-58-49-8117-PM.png)

**Selecione sua loja Amazon** no filtro 'Canal de Venda'.

![Imagem 9: Selecione sua loja Amazon no filtro 'Canal de Venda'.](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-01-01-05-4760-PM.png?width=560&height=219&name=image-png-Mar-06-2024-01-01-05-4760-PM.png)

Na lista de pedidos, é possível diferenciar os pedidos FBA Onsite dos demais através do campo **“Tipo de Logística”, onde é apresentado o logo do serviço.**

![Imagem 10: Na lista de pedidos, é possível diferenciar os pedidos FBA Onsite dos demais através do campo “Tipo de Logística”, onde…](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Mar-06-2024-03-59-56-8204-PM.png?width=592&height=309&name=image-png-Mar-06-2024-03-59-56-8204-PM.png)

### 5) Como emitir nota fiscal na FBA Onsite no Magis5 Hub

O fluxo de emissão da nota fiscal é obrigatório para todos os pedidos FBA Onsite, então precisam estar ativadas na integração da Amazon a **geração e emissão de Nota Fiscal**. Para mais informações sobre a ativação, [clique aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44011406798615).

O envio da nota fiscal segue o fluxo padrão Magis5 Hub para os demais Marketplaces, ocorrendo de forma automática após ser gerada no ERP ou Faturador Magis5 Hub e vinculada ao pedido no Magis5 Hub.

### 6) Como imprimir etiquetas da Amazon FBA Onsite no Magis5 Hub.

Não há disponibilização de API para download de etiquetas de pedidos FBA Onsite. Por conta disso, durante a expedição, será impressa apenas a Nota Fiscal e **o vendedor deve imprimir as etiquetas pelo painel da Amazon.**
