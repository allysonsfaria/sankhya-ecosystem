---
id: "44011104444055"
titulo: "Como efetuar a integração do Magento 2 (Adobe Commerce) com o Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011104444055-Como-efetuar-a-integra%C3%A7%C3%A3o-do-Magento-2-Adobe-Commerce-com-o-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:55:18Z"
rotulos: ["sync_hc", "magis5", "sync_hash_277116e7fc02", "magis5_204051622057"]
---

# Como efetuar a integração do Magento 2 (Adobe Commerce) com o Magis5 Hub?

## Confira o passo a passo de como integrar o Magento 2 ao Magis5 Hub com este guia.

---

### 1) Habilitando integrações externas

Para habilitar, **acesse o painel** do Magento 2 - Adobe Commerce. No menu da lateral esquerda, vá para **"STORES"** e depois clique em "**Configuration".**

![adobecommerce1](https://ajuda.sankhya.com.br/hc/article_attachments/44011104579735)

Na listagem à esquerda, clique na opção **"SERVICES"** e depois em **"OAuth".**

![oauth](https://ajuda.sankhya.com.br/hc/article_attachments/44011093699223)

Na seção de **"Consumer Settings"**localize a opção **"Allow OAuth Access Tokens to be used as standalone Bearer tokens"**e nela escolha a opção **"Yes".**

![Imagem 3: Na seção de "Consumer Settings" localize a opção "Allow OAuth Access Tokens to be used as standalone Bearer tokens" e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011093809687)

Feita esta verificação, finalize clicando no botão **"Save Config"**.

### 2) Gerando o token API

Novamente dentro do painel do Magento 2 / Adobe Commerce, vá para **"SYSTEM"** no menu da lateral esquerda e depois clique em **"Integrations"**.

![integrations](https://ajuda.sankhya.com.br/hc/article_attachments/44011072472727)

Em seguida, clique no botão **"Add New Integration"**, localizado na parte direita.

![Imagem 5: Em seguida, clique no botão "Add New Integration" , localizado na parte direita.](https://ajuda.sankhya.com.br/hc/article_attachments/44011089178007)

Na aba **"Integration Info"** preencha somente os campos citados abaixo:

**Name:** Defina **Magis5** como o nome da integração.
**Your Password:** Insira a sua senha utilizada para acessar o painel do Magento.

![info](https://ajuda.sankhya.com.br/hc/article_attachments/44011089309335)

Clique agora na aba **"API"**. No campo **"Resource Access",** selecione a opção **"All"**para que o Magis5 não tenha restrições via API. Finalize clicando no botão **"Save".**

![access](https://ajuda.sankhya.com.br/hc/article_attachments/44011089388439)

Após salvo, você será direcionado para a lista com as integrações criadas. **Edite** a integração indicada por Magis5 que você acabou de criar clicando no ícone de **lápis**.

![w](https://ajuda.sankhya.com.br/hc/article_attachments/44011094379927)

**Copie** o código gerado do campo **"Access Token"**que estará no final da página e guarde-o em um bloco de notas.

![Imagem 9: Copie o código gerado do campo "Access Token" que estará no final da página e guarde-o em um bloco de notas.](https://ajuda.sankhya.com.br/hc/article_attachments/44011105638807)

Por fim, retorne para a **"DASHBOARD"**do painel do Magento e **selecione a url** exibida na barra de endereço. **Selecione apenas a URL base** que termina em .com, como demonstrado abaixo, destacado em azul. Copie a seleção e guarde-a no bloco de notas.

![Imagem 10: Por fim, retorne para a "DASHBOARD" do painel do Magento e selecione a url exibida na barra de endereço. Selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/44011094524311)

Tendo concluído o processo anterior, prossiga para o seu painel do Magis5 Hub.

### 3) Integrando o Magento 2/Adobe Commerce ao Magis5 Hub

No Magis5 Hub, vá para**"Configurações" > "Integrações"**e clique em **"Lojas Virtuais"**.

![Imagem 11: No Magis5 Hub, vá para "Configurações" > "Integrações" e clique em "Lojas Virtuais" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011120914199)

Na tela que será aberta, clique no botão **"Adicionar nova integração"**.

![Imagem 12: Na tela que será aberta, clique no botão "Adicionar nova integração" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011094686359)

Selecione **Magento 2** no campo Marketplace e preencha os campos conforme indicado abaixo:

![image-png-Jun-06-2024-05-53-49-9417-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44011106005527)

**Nome da sua loja:** O nome da sua preferência (Ex: Magis5 Store);
**Token de acesso:** O token copiado no item [Access Token](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011104444055-Como-efetuar-a-integra%C3%A7%C3%A3o-do-Magento-2-Adobe-Commerce-com-o-Magis5-Hub#token) da Magento;
**Url da Loja:**A [URL da sua loja](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011104444055-Como-efetuar-a-integra%C3%A7%C3%A3o-do-Magento-2-Adobe-Commerce-com-o-Magis5-Hub#url) Magento 2 copiada anteriormente.

O campo **"Código da sua loja no ERP"**é necessário para quem utiliza **ERPs externos. Atente-se se este for seu caso!**

O preenchimento deste campo não é nesessário para vendedores que utilizam o faturador do Magis5 Hub.

Para o **ERP Bling!**, siga nosso tutorial de [como preencher o campo "Código da sua loja no ERP" utilizando o Bling!](https://ajuda.magis5.com.br/para-que-serve-o-campo-c%C3%B3digo-da-sua-loja-no-erp-e-como-utiliza-lo?hsLang=pt-br)

A seguir, clique em **"Notas fiscais"** e **selecione um ERP** para a emissão de Notas Fiscais. **Verifique também as outras abas e os demais campos**, preenchendo-os se necessário.

![Imagem 14: A seguir, clique em "Notas fiscais" e selecione um ERP para a emissão de Notas Fiscais. Verifique também as outras abas…](https://ajuda.sankhya.com.br/hc/article_attachments/44011090270359)

Finalize clicando em **"Realizar Integração"**.

![Imagem 15: Finalize clicando em "Realizar Integração" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011113356567)

Após isto, sua integração com o Magento 2 será concluída. Caso encontrar quaisquer problemas, não hesite em [entrar em contato com nosso suporte](https://ajuda.magis5.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br).
