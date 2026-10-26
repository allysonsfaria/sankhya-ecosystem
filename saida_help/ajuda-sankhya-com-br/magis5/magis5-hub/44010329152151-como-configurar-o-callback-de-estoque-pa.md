---
id: "44010329152151"
titulo: "Como configurar o callback de estoque para integração com o ERP Bling"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010329152151-Como-configurar-o-callback-de-estoque-para-integra%C3%A7%C3%A3o-com-o-ERP-Bling"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:34:33Z"
rotulos: ["sync_hc", "magis5", "magis5_204055239680", "sync_hash_02661c3e6977"]
---

# Como configurar o callback de estoque para integração com o ERP Bling

## Entenda, neste guia, como configurar o callback de estoque para integrar a comunicação entre o Bling e o Magis5 HUB.

---

O Magis se comunica com o Bling por meio de um link de **Callback**, que centraliza todo o fluxo de produtos, como criação, atualização de estoque e sincronização de informações. Para garantir o funcionamento correto desses processos, é fundamental que o **Callback esteja devidamente configurado.**

### Onde encontrar o link de Callback no Magis?

Feito o login no Magis5, vá para **"Configurações"**, depois até **"Integrações"** e por último clique em **"Marketplaces".

![Imagem 1: Feito o login no Magis5, vá para "Configurações" , depois até "Integrações" e por último clique em "Marketplaces".](https://ajuda.sankhya.com.br/hc/article_attachments/44010313653655)**

Cada integração de canal de venda do Magis possui um link de **Callback**, porém, para a configuração, é necessário utilizar apenas **um único link**.
Para localizá-lo, basta editar qualquer canal de venda desejado.

![Imagem 2: Cada integração de canal de venda do Magis possui um link de Callback , porém, para a configuração, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44010329470487)

![Imagem 3: Cada integração de canal de venda do Magis possui um link de Callback , porém, para a configuração, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44010280809879)

![Imagem 4: Cada integração de canal de venda do Magis possui um link de Callback , porém, para a configuração, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44010251380631)

Copie o **link de Callback** referente ao estoque para utilizar na configuração da integração no BLING.

A configuração do **Callback** deve ser realizada no **Bling Principal**, ou seja, aquele que controla o estoque. Para identificar qual é o Bling Principal no Magis, acesse: **Configurações > Integrações > ERPs & Faturador**. O Bling que estiver marcado com a **estrela** é o principal.

![Imagem 5: A configuração do Callback deve ser realizada no Bling Principal , ou seja, aquele que controla o estoque. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/44010304382359)
Caso não exista um **Bling Principal** em seu painel, será necessário configurar um **Callback** para cada Bling, conforme as lojas integradas em cada um.

Após identificar o seu Bling Principal, faça login na sua conta, clique em **“Central de Extensões”** e depois em **“Minhas Instalações”**. Nessa tela, localize a integração da loja na qual você [editou e copiou o link de Callback no Magis.](https://ajuda.sankhya.com.br/hc/pt-br/articles/44010329152151-Como-configurar-o-callback-de-estoque-para-integra%C3%A7%C3%A3o-com-o-ERP-Bling#Callback)

![Imagem 6: Após identificar o seu Bling Principal, faça login na sua conta, clique em “Central de Extensões” e depois em “Minhas…](https://ajuda.sankhya.com.br/hc/article_attachments/44010304512151)

![Imagem 7: Após identificar o seu Bling Principal, faça login na sua conta, clique em “Central de Extensões” e depois em “Minhas…](https://ajuda.sankhya.com.br/hc/article_attachments/44010314412055)

Após localizar a loja, clique sobre a integração e, no campo **“Callbacks”, em “Tipo de retorno no Callback”,** selecione a opção **“JSON (urlencoded)”.** Em seguida, ative a opção **"Callback de estoque"** logo abaixo**.

![Imagem 8: Após localizar a loja, clique sobre a integração e, no campo “Callbacks”, em “Tipo de retorno no Callback”, selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010314542359)**

Ao ativar a opção **“Callback de estoque”**, será exibida uma caixa de texto onde você deve colar o [link de Callback](https://ajuda.sankhya.com.br/hc/pt-br/articles/44010329152151-Como-configurar-o-callback-de-estoque-para-integra%C3%A7%C3%A3o-com-o-ERP-Bling#Callback) que foi copiado da integração no Magis.

![Imagem 9: Após localizar a loja, clique sobre a integração e, no campo “Callbacks”, em “Tipo de retorno no Callback”, selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010330325783)

Após concluir todo o processo, clique em **“Salvar”** ao final da página.

![Imagem 10: Após localizar a loja, clique sobre a integração e, no campo “Callbacks”, em “Tipo de retorno no Callback”, selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010298610583)

Pronto! O **Callback de estoque** foi configurado corretamente e está ativo.

**Importante:** Apenas **um link de Callback** deve ser configurado no Bling. Caso mais de um **Callback** esteja ativo, o funcionamento correto será comprometido e os estoques, assim como as atualizações, não serão enviados ao Magis.

Caso queira identificar, no Bling, qual integração de loja está configurada o callback, acesse **“Minhas Instalações”** e localize a loja que possui a palavra **CALL** em sua descrição.

![Imagem 11: Caso queira identificar, no Bling, qual integração de loja está configurada o callback, acesse “Minhas Instalações” e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010252070935)
