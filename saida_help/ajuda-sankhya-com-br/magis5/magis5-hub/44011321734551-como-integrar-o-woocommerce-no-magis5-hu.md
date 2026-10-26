---
id: "44011321734551"
titulo: "Como integrar o WooCommerce no Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011321734551-Como-integrar-o-WooCommerce-no-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:01:12Z"
rotulos: ["sync_hc", "magis5", "magis5_204048109125", "sync_hash_b6b6fed4d983"]
---

# Como integrar o WooCommerce no Magis5 Hub?

## Aprenda a efetuar a integração com a loja virtual WooCommerce

### [![Imagem 1: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.magis5.com.br/hs-fs/hubfs/image-png-Jun-16-2023-06-01-40-2757-PM.png?width=77&height=56&name=image-png-Jun-16-2023-06-01-40-2757-PM.png)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#dashboard)[![Imagem 2: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.sankhya.com.br/hc/article_attachments/44011300967063)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#produtos-e-an%C3%BAncios)[![Imagem 3: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.sankhya.com.br/hc/article_attachments/44011291547671)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#estoque)[![Imagem 4: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.sankhya.com.br/hc/article_attachments/44011301155991)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#pedidos)[![https://ajuda.magis5.com.br/magis5-hub#expedi%C3%A7%C3%A3o](https://ajuda.sankhya.com.br/hc/article_attachments/44011291809047)](https://ajuda.magis5.com.br/expedi%C3%A7%C3%A3o?hsLang=pt-br)[![Imagem 6: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.sankhya.com.br/hc/article_attachments/44011291943447)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#financeiro)[![Imagem 7: Aprenda a efetuar a integração com a loja virtual WooCommerce](https://ajuda.sankhya.com.br/hc/article_attachments/44011310082967)](https://ajuda.magis5.com.br/magis5-hub?hsLang=pt-br#configura%C3%A7%C3%B5es)

---

Antes de realizarmos a integração da WooCommerce, vamos aprender algumas regrinhas básicas para o bom funcionamento da plataforma:

- Recomendamos que a versão do plugin WooCommerce instalado seja igual ou superior a **8.0.**
- No caso de utilização de hospedagem própria, certifique-se de possuir certificação SSL para que possamos utilizar os métodos GET, POST, e PUT da API do WooCommerce.
- É obrigatório que o plugin **Brazilian Market on WooCommerce** esteja instalado na sua loja WooCommerce, pois desta forma conseguiremos capturar os campos referentes a contato e endereço de entrega.
- É obrigatório que a unidade de medidas dentro do WooCommerce esteja configurada no padrão **cm** e **kg**.
- A emissão de etiquetas para a WooCommerce só irá ocorrer para clientes que utilizam a integração com os Correios ou Intelipost, pois a WooCommerce não faz a emissão de etiquetas.

### Como gerar o token na WooCommerce

No painel da WooCommerce localizado na lateral esquerda, acesse o menu **Painel > WooCommerce > Configurações.**

![Imagem 8: No painel da WooCommerce localizado na lateral esquerda, acesse o menu Painel > WooCommerce > Configurações.](https://ajuda.sankhya.com.br/hc/article_attachments/44011335264279)

No painel que abrir, clique em **Avançado > API Rest > Adicionar Chave:**

![Imagem 9: No painel que abrir, clique em Avançado > API Rest > Adicionar Chave:](https://ajuda.sankhya.com.br/hc/article_attachments/44011335391639)

Em seguida, preencha os campos conforme abaixo e confirme no botão **'Gerar uma chave de API'**:

**- Descrição:** Magis5
**- Usuário:** selecione o e-mail administrador da sua conta
**- Permissões:**selecione a opção Ler/Escrever

Após isso, as chaves de acesso (**Consumer key**e **Consumer secret**) serão exibidas.

⚠️ **IMPORTANTE:**

Ao clicar no botão, os tokens serão exibidos apenas uma única vez, então certifique-se de copiar eles. Caso contrário, você terá que repetir o processo para gerar novos tokens.

![Imagem 10: Ao clicar no botão, os tokens serão exibidos apenas uma única vez, então certifique-se de copiar eles. Caso contrário,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011335521943)

Para a integração, também será utilizada a **URL da loja.** Para isso, entre no site da sua loja e **copie o endereço na barra superior**.

![Imagem 11: Para a integração, também será utilizada a URL da loja. Para isso, entre no site da sua loja e copie o endereço na…](https://ajuda.sankhya.com.br/hc/article_attachments/44011327662359)

**OBS:** a URL deve ser copiada de forma completa, incluindo o começo em "https://". Exemplo: **https://www.exemplo.com.br**

### Integrando o WooCommerce com o Magis5 Hub

No Magis5 Hub, vá em **"Configurações"**, em seguida **"Integrações"** e por último clique em**"Lojas Virtuais".**

![Imagem 12: No Magis5 Hub, vá em "Configurações" , em seguida "Integrações" e por último clique em "Lojas Virtuais".](https://ajuda.sankhya.com.br/hc/article_attachments/44011343964695)

Na tela que será aberta, clique no botão **"Adicionar nova integração"**.

![Imagem 13: Na tela que será aberta, clique no botão "Adicionar nova integração" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011310728087)

Selecione "WooCommerce" no campo marketplace e preencha os campos conforme abaixo:

![Imagem 14: Selecione "WooCommerce" no campo marketplace e preencha os campos conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011310881047)

**Nome da sua loja:** O nome da sua preferência (Ex: Magis5 Store).
**E-mail/Código da loja:** Cole o **Consumer key** que foi copiado pelo painel da WooCommerce.
**Token de acesso:** Cole o **Consumer secret** que foi copiado pelo painel da WooCommerce.
**URL da loja:** A URL copiada pelo painel da WooCommerce.

O campo **"Código da sua loja no ERP"**é necessário para quem utiliza **ERPs externos. Atente-se se este for seu caso!**

Esta configuração não é necessária quando o seller utiliza o faturador do Magis5 Hub.

Para o **ERP Bling!**, siga nosso tutorial de [como preencher o campo "Código da sua loja no ERP" utilizando o Bling!](https://ajuda.magis5.com.br/para-que-serve-o-campo-c%C3%B3digo-da-sua-loja-no-erp-e-como-utiliza-lo?hsLang=pt-br)

Após isso, clique em **"Notas fiscais"** e selecione um ERP para a emissão de Notas fiscais. Preencha as demais opções e campos de acordo com o que desejar.

![Imagem 15: Após isso, clique em "Notas fiscais" e selecione um ERP para a emissão de Notas fiscais. Preencha as demais opções e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011293099543)

**Verifique também e preencha as opções e campos das outras abas, se necessário.** Finalize clicando em **"Realizar integração"** quando todos os campos necessários estiverem preenchidos.
