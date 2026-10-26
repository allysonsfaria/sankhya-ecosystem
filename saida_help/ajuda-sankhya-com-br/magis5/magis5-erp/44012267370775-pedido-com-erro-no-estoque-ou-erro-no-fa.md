---
id: "44012267370775"
titulo: "Pedido com \"Erro no Estoque\" ou \"Erro no faturamento\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012267370775-Pedido-com-Erro-no-Estoque-ou-Erro-no-faturamento"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:25Z"
rotulos: ["sync_hc", "magis5", "magis5_204056235649", "sync_hash_f64f4e8cc10a"]
---

# Pedido com "Erro no Estoque" ou "Erro no faturamento"

## Verique os itens que fazem parte da Venda

## Na tela de vendas, clique em Visualizar Pedido/Venda:

![Imagem 1: Na tela de vendas, clique em Visualizar Pedido/Venda :](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-9.png)

Nos detalhes do pedido, copie o ID do produto e verifique a quantidade adquirida de cada um deles:

![Imagem 2: Nos detalhes do pedido, copie o ID do produto e verifique a quantidade adquirida de cada um deles:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-11.png)

Volte para o Artemis5. No menu superior, vá para **Cadastros → Produtos**. Insira o ID do primeiro produto à ser pesquisado no campo **“ID/SKU”** e clique no botão **Aplicar Filtro**.

![Imagem 3: Volte para o Artemis5. No menu superior, vá para Cadastros → Produtos . Insira o ID do primeiro produto à ser…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-12.png)

Ao exibir o produto, clique em **Editar** na coluna de Opções:

![Imagem 4: Ao exibir o produto, clique em Editar na coluna de Opções:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-14.png)

No cadastro do produto, clique na aba **Estoque**. Verifique a quantidade exibida.

![Imagem 5: No cadastro do produto, clique na aba Estoque . Verifique a quantidade exibida.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/estoque.png)

Caso seu empreendimento utilize apenas um estoque, o mesmo será identificado por "Depósito Padrão", como é o caso acima.

No canto direito, **verifique se a quantidade de itens em estoque está igual ou superior à quantidade adquirida pelo cliente**. Neste exemplo, a quantidade está superior:

![Imagem 6: No canto direito, verifique se a quantidade de itens em estoque está igual ou superior à quantidade adquirida pelo…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-15.png)

Como o primeiro produto possui quantidade suficiente em estoque para faturar o pedido, será necessário analisar o outro produto. Para isso, repita o procedimento:

1. Copie o ID do produto na página de detalhes do pedido;
2. Em consulta de produtos, informe o ID em ID/SKU, clique em aplicar filtro e, em seguida, editar;
3. Verifique se a quantidade de itens disponíveis em estoque é maior do que a quantidade de unidades solicitadas no pedido.

![Imagem 7: Verifique se a quantidade de itens disponíveis em estoque é maior do que a quantidade de unidades solicitadas no pedido.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-16.png)

Quando a quantidade em estoque no sistema é menor do que a quantidade comprada no pedido, temos os seguintes casos:

**Caso 1:** A tabela exibirá o texto **"Produto sem estoque nos depósitos"**:

![Imagem 8: Caso 1: A tabela exibirá o texto "Produto sem estoque nos depósitos" :](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/case1deposito.png)

**Caso 2:** a tabela exibirá **Quantidade 0**.

![Imagem 9: Caso 2: a tabela exibirá Quantidade 0 .](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/case2deposito.png)

Como é necessário que todos os itens da venda tenham estoque disponível para o faturamento, será necessário corrigir este depósito.

Para isso, clique no ícone rosa do campo **"Depósito"** e selecione em qual depósito será dado entrada nos itens. Caso você possua mais de um empreendimento e não utilize depósito compartilhado entre eles, **se atente ao nome do seu empreendimento e ao nome do depósito**.

![Imagem 10: Para isso, clique no ícone rosa do campo "Depósito" e selecione em qual depósito será dado entrada nos itens. Caso você…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-17.png)

Após selecionar o depósito, informe o tipo de movimentação:

![Imagem 11: Após selecionar o depósito, informe o tipo de movimentação:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-18.png)

- **Inventário**: Substitui todos os itens do depósito. Caso você possua 10 itens em depósito e queira inserir mais 15, ao selecionar essa opção, o estoque ficará com 15 itens.

- **Entrada**: Soma a quantidade de itens à quantidade que o estoque possui. Caso você possua 10 itens em depósito e queira inserir mais 15, ao selecionar essa opção, o estoque ficará com 25 itens.

- **Saída**: Retira itens do depósito. Caso você possua 10 itens em depósito e queira remover 8, ao selecionar essa opção, o estoque ficará com 2 unidades. S**erá necessário informar o motivo da retirada dos itens**.

Na situação exemplificada, será necessário dar entrada de 01 unidade do item para o pedido ser faturado. Então, selecione **Entrada**, e em Qtd. insira o número 1. Clique em **"Movimentar"**.

![Imagem 12: Na situação exemplificada, será necessário dar entrada de 01 unidade do item para o pedido ser faturado. Então,…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-19.png)

Ao clicar em movimentar o estoque será salvo e a entrada será realizada.

![Imagem 13: Ao clicar em movimentar o estoque será salvo e a entrada será realizada.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/confirm.png)

Clique em **Salvar** para finalizar a edição do produto.

Agora, basta aguardar um prazo de até cinco minutos para a venda ser reprocessada e faturada.

---

## Identificando uma venda Fullfilment.

Para identificar quando uma venda é padrão e quando uma venda é fulfillment, basta analisar o vendedor responsável pelo pedido. O vendedor é o marketplace no qual foi realizado o pedido. Na **tela de vendas**, ao identificar um pedido com problema no estoque, observe o vendedor:

![Imagem 14: Para identificar quando uma venda é padrão e quando uma venda é fulfillment, basta analisar o vendedor responsável pelo…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-20.png)

Neste caso, **ao realizar a entrada no estoque produto**, será necessário **selecionar o depósito fulfillment** referente a este marketplace e prosseguir com os mesmos procedimentos informados acima.

![Imagem 15: Neste caso, ao realizar a entrada no estoque produto , será necessário selecionar o depósito fulfillment referente a…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/05/image-21.png)
