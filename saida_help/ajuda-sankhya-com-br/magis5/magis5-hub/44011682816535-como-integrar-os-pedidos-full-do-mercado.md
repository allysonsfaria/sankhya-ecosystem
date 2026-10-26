---
id: "44011682816535"
titulo: "Como integrar os Pedidos Full do Mercado Livre com o ERP Omie no Magis5 Hub?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011682816535-Como-integrar-os-Pedidos-Full-do-Mercado-Livre-com-o-ERP-Omie-no-Magis5-Hub"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T19:08:42Z"
rotulos: ["sync_hc", "magis5", "magis5_204055362111", "sync_hash_0cf297d53ade"]
---

# Como integrar os Pedidos Full do Mercado Livre com o ERP Omie no Magis5 Hub?

## Aprenda a configurar os pedidos Full do Mercado Livre junto com o ERP Omie.

---

### Configuração do ID do Armazém no canal

Para garantir que o processo de importação de NFE do Mercado Livre para o ERP Omie funcione corretamente, siga os seguintes passos:

1. Faça login em sua conta Magis5.
2. Vá para **"Configurações" > "Integrações"** e clique em **"Marketplaces"**.

   ![Imagem 1: Vá para "Configurações" > "Integrações" e clique em "Marketplaces" .](https://ajuda.sankhya.com.br/hc/article_attachments/44011697438231)
3. Encontre a integração Mercado Livre que tem o Fullfilment ativo e clique no botão **"Editar"** ao lado dela.

   ![Imagem 2: Encontre a integração Mercado Livre que tem o Fullfilment ativo e clique no botão "Editar" ao lado dela.](https://ajuda.sankhya.com.br/hc/article_attachments/44011659321751)
4. Vá para a aba **"Depósitos"** e insira o **ID do Armazém que criou para o Full no ERP Omie** no campo **"Código de depósito Fulfillment"**. 

   ![Imagem 3: Vá para a aba "Depósitos" e insira o ID do Armazém que criou para o Full no ERP Omie no campo "Código de depósito…](https://ajuda.sankhya.com.br/hc/article_attachments/44011697648407)
5. **Salve** as configurações.

Após configurar o ID do depósito, o processo de importação de NFE será automatizado. Ele funciona da seguinte forma:

- Quando um pedido full é recebido na conta do Mercado Livre que utiliza pedidos full, o Magis5 Hub não criará mais o pedido no ERP Omie. Em vez disso, o Magis5 Hub importará automaticamente a Nota Fiscal Eletrônica (NFE) associada a esse pedido dentro do ERP Omie.
- Dentro do ERP Omie, a NFE será usada para dar baixa no estoque dos produtos relacionados ao pedido.
- A partir disso, o ERP Omie irá gerar as informações de contas a receber com base nos pedidos importados.
