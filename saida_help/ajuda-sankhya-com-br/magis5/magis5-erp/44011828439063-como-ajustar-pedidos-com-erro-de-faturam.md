---
id: "44011828439063"
titulo: "Como ajustar pedidos com erro de faturamento relacionados à Inscrição Estadual (IE)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011828439063-Como-ajustar-pedidos-com-erro-de-faturamento-relacionados-%C3%A0-Inscri%C3%A7%C3%A3o-Estadual-IE"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:12:45Z"
rotulos: ["sync_hc", "magis5", "magis5_204055193459", "sync_hash_6ad1401a790d"]
---

# Como ajustar pedidos com erro de faturamento relacionados à Inscrição Estadual (IE)

## Entenda neste artigo como corrigir pedidos com erro de faturamento quando o comprador possui Inscrição Estadual (IE) ou for não contribuinte

---

Alguns pedidos para compradores que possuem CNPJ podem cair em **"erro no faturamento"** devido à configuração dos dados fiscais do cadastro do comprador.

### Como identificar um pedido com erro de faturamento dentro no Magis5 ERP

Após fazer login no Magis5 ERP, vá até a aba **"Vendas"** e selecione **"Consulta de Vendas"**. No campo **"Status**", escolha a opção **"Erro no faturamento"** e aplique o filtro de data desejado. Esse filtro exibirá todos os pedidos que apresentaram erro no faturamento dentro do período selecionado.

![Imagem 1: Após fazer login no Magis5 ERP, vá até a aba "Vendas" e selecione "Consulta de Vendas" . No campo "Status ", escolha a…](https://ajuda.sankhya.com.br/hc/article_attachments/44011851608855)

É possível identificar o motivo do erro de faturamento do pedido clicando sobre o ícone na coluna **"Observações Adicionais".**

![Imagem 2: Possíveis erros de faturamento relacionados à Inscrição Estadual (IE) do comprador: "Rejeição: A SEFAZ do destinatário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011840054807)

Possíveis erros de faturamento relacionados à **Inscrição Estadual (IE)** do comprador:

**"Rejeição: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual"

![Imagem 3: Possíveis erros de faturamento relacionados à Inscrição Estadual (IE) do comprador: "Rejeição: A SEFAZ do destinatário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011837145239)**
**"Rejeição: IE do destinatário não está ativa na UF"**

![Imagem 4: Possíveis erros de faturamento relacionados à Inscrição Estadual (IE) do comprador: "Rejeição: A SEFAZ do destinatário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011829040535)

Para ajustar o cadastro do comprador e permitir a emissão da nota fiscal do pedido, é necessário localizar o cadastro do cliente. Para isso, acesse a aba **"Cadastro"** e, em seguida, clique em **"Clientes."

![Imagem 5: Possíveis erros de faturamento relacionados à Inscrição Estadual (IE) do comprador: "Rejeição: A SEFAZ do destinatário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011820812439)**

Você pode localizar o cliente utilizando o **CNPJ**, o **nome** ou qualquer outro filtro disponível no sistema.

![Imagem 6: Após localizar o cliente que deseja ajustar, clique em "Editar" para abrir o cadastro e realizar as alterações…](https://ajuda.sankhya.com.br/hc/article_attachments/44011837543959)

Após localizar o cliente que deseja ajustar, clique em **"Editar"** para abrir o cadastro e realizar as alterações necessárias.

![Imagem 7: Após localizar o cliente que deseja ajustar, clique em "Editar" para abrir o cadastro e realizar as alterações…](https://ajuda.sankhya.com.br/hc/article_attachments/44011821031831)

![Imagem 8: Após localizar o cliente que deseja ajustar, clique em "Editar" para abrir o cadastro e realizar as alterações…](https://ajuda.sankhya.com.br/hc/article_attachments/44011829472279)

Antes de ajustarmos as opções **"Contribuinte ICMS"** e **"Isento da I.E."** no perfil do cliente, é necessário verificar se o CNPJ do comprador possui uma Inscrição Estadual (IE) ativa.

Para isso, acesse o site do [Portal da Nota Fiscal Eletrônica – SVRS.](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)
No portal, selecione a **UF** do comprador, clique na opção **"Dados do Contribuinte"**, insira o **CNPJ** no campo correspondente e clique em **"Pesquisar por CNPJ"**.

![Imagem 9: Se o cliente não possuir Inscrição Estadual (IE), será exibida a seguinte mensagem: "Contribuinte não localizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011829584407)

Se o cliente não possuir Inscrição Estadual (IE), será exibida a seguinte mensagem: **"Contribuinte não localizado no Cadastro Centralizado de Contribuintes."

![Imagem 10: Se o cliente não possuir Inscrição Estadual (IE), será exibida a seguinte mensagem: "Contribuinte não localizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011810978327)**Com essa informação, volte ao Magis5 ERP, acesse a aba **"Dados Fiscais"** e marque as opções **"Isento da I.E."** como **SIM** e **"Contribuinte ICMS"** como **NÃO**. Em seguida, clique em **"Salvar"**.

![Imagem 11: Se o cliente não possuir Inscrição Estadual (IE), será exibida a seguinte mensagem: "Contribuinte não localizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011852716823)

Se o cenário for o inverso, ou seja, se o cliente possuir IE ativa, conforme mostrado na imagem abaixo.

![Imagem 12: Terá que ajustar o inverso as informações. Acesse a aba "Dados Fiscais" , marque "Isento da I.E." como NÃO e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011841036311)

Terá que ajustar o inverso as informações. Acesse a aba **"Dados Fiscais"**, marque **"Isento da I.E."** como **NÃO** e **"Contribuinte ICMS"** como **SIM**. Em seguida, vá até a aba **"Informações Básicas"**, preencha o campo com a **Inscrição Estadual (IE)** do comprador e clique em **"Salvar"**.

![Imagem 13: Terá que ajustar o inverso as informações. Acesse a aba "Dados Fiscais" , marque "Isento da I.E." como NÃO e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011821644695)

![Imagem 14: Terá que ajustar o inverso as informações. Acesse a aba "Dados Fiscais" , marque "Isento da I.E." como NÃO e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011811379351)

Após finalizar o processo, aguarde o sistema processar o pedido e emitir a **Nota Fiscal** ou emita manualmente a **Nota Fiscal** no pedido de venda.

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011841384727)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
