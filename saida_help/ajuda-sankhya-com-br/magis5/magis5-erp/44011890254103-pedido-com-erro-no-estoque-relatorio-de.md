---
id: "44011890254103"
titulo: "Pedido com \"Erro no Estoque\" - Relatório de BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011890254103-Pedido-com-Erro-no-Estoque-Relat%C3%B3rio-de-BI"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:14Z"
rotulos: ["sync_hc", "magis5", "magis5_204048557333", "sync_hash_825340b67632"]
---

# Pedido com "Erro no Estoque" - Relatório de BI

## Este erro significa que ao tentar concluir o faturamento de uma venda e um dos itens adquiridos pelo cliente possui uma quantidade inferior àquela que foi originalmente solicitada.

Para resolver esse erro, além de visualizar os itens faltantes através da tela de vendas ([clique aqui e veja o processo](https://ajuda.artemis5.com.br/pedido-com-erro-no-estoque/)), é possível analisar através do relatório de Business Intelligence.

**VERIFIQUE OS ITENS QUE PRECISAM DE AJUSTE NO ESTOQUE**

Para acessar o relatório de BI, clique em: Gerenciamento→ Business Intelligence:

![Imagem 1: Para acessar o relatório de BI, clique em: Gerenciamento→ Business Intelligence:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-101-1024x164.png)

No canto lateral direito estão os filtros, sendo o primeiro campo “Visão”:

![Imagem 2: No canto lateral direito estão os filtros, sendo o primeiro campo “Visão”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-653-1024x345.png)

Em “Visão” selecione "Pedidos com Problema de Estoque". Os filtros à seguir complementam as informações do relatório:

![Imagem 3: Em “Visão” selecione "Pedidos com Problema de Estoque". Os filtros à seguir complementam as informações do relatório:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/10/image-1024x354.png)

Selecione "Organizado por Vendedor" para trazer qual o vendedor / marketplace responsável pela venda e também, para saber qual depósito deverá dar entrada nos itens necessários:

Informe um perído em "Data Inicial” e “Data Final”. Este campo é obrigatório.

Observação: Caso possua mais de um empreendimento, é possível selecioná-los, clicando em "(+) Incluir" e com isso, fazer a reposição do estoque de uma única vez.

Após selecionar os filtros desejados e clicar em “Aplicar Filtro”, para gerar o relatório:

![Imagem 4: Após selecionar os filtros desejados e clicar em “Aplicar Filtro”, para gerar o relatório:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/10/image-4-1024x320.png)

**ANALISANDO O RELATÓRIO**

Após gerar o relatório, analise as colunas "Vendedor", "ID Produto" e "Totais" para saber quais produtos deverão ser atualizados e suas respectivas quantidades:

![Imagem 5: Após gerar o relatório, analise as colunas "Vendedor", "ID Produto" e "Totais" para saber quais produtos deverão ser…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/10/image-12-1024x303.png)

**AJUSTANDO O ESTOQUE**

No menu, clique em Cadastros → Produtos, insira o ID do produto à ser pesquisado no campo “ID/SKU”, clique em: Aplicar Filtros e, ao exibir o produto, clique em: Editar:

![Imagem 6: No menu, clique em Cadastros → Produtos, insira o ID do produto à ser pesquisado no campo “ID/SKU”, clique em: Aplicar…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/10/image-13-1024x277.png)

No cadastro do produto, clique em: Estoque:

![Imagem 7: No cadastro do produto, clique em: Estoque:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/10/image-14-1024x242.png)

Observação: Caso seu empreendimento utilize apenas um estoque, o mesmo será identificado por "Depósito Padrão - nome do empreendimento", como é o caso acima.
Marketplaces que utilizam fulfillment são identificados pelo nome do marketplace + fulfillment na frente. Por exemplo: Amazon - Fulfillment.

Para atualizar este depósito, clique em "depósito" e selecione em qual depósito será realizado a entrada nos itens. Caso você possua mais de um empreendimento e não utilize depósito compartilhado entre eles, se atente ao nome do empreendimento e ao nome do depósito, como é o caso abaixo:

![Imagem 8: Para atualizar este depósito, clique em "depósito" e selecione em qual depósito será realizado a entrada nos itens.…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-124-1024x410.png)

Após selecionar o depósito, informe o tipo de movimentação:

![Imagem 9: Após selecionar o depósito, informe o tipo de movimentação:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-125-1024x169.png)

- **Inventário**: Substitui todos os itens do depósito. Caso você possua 10 itens em depósito e queira inserir mais 15, ao selecionar essa opção, o estoque ficará com 15 itens.

- **Entrada**: Soma a quantidade de itens à quantidade que o estoque possui. Caso você possua 10 itens em depósito e queira inserir mais 15, ao selecionar essa opção, o estoque ficará com 25 itens.

- **Saída**: Retira itens do depósito. Caso você possua 10 itens em depósito e queira remover 8, ao selecionar essa opção, o estoque ficará com 2 unidades.
  - Observação: Será necessário informar o motivo da retirada dos itens.

Na situação exemplificada, será necessário dar entrada de 4 itens para o pedido ser faturado, então, selecione entrada, em Qtd. insira o número 4 e clique em: Movimentar:

![Imagem 10: Na situação exemplificada, será necessário dar entrada de 4 itens para o pedido ser faturado, então, selecione entrada,…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-126-1024x167.png)

Ao clicar em movimentar o estoque será salvo e a entrada será realizada.

![Imagem 11: Ao clicar em movimentar o estoque será salvo e a entrada será realizada.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-127-1024x283.png)

Clique em: Salvar para finalizar a edição do produto.

Agora, basta aguardar um prazo de até cinco minutos para a venda ser reprocessada e faturada.

**IDENTIFICANDO UMA VENDA FULFILLMENT**

Os itens do depósito Fulfillment normalmente são separados do depósito padrão.

Para identificar quando uma venda é padrão e quando uma venda é fulfillment, basta analisar o vendedor responsável pelo pedido. O vendedor é o marketplace na qual foi realizado o pedido:

Na tela de vendas, ao identificar um pedido com problema no estoque, observe o vendedor:

![Imagem 12: Na tela de vendas, ao identificar um pedido com problema no estoque, observe o vendedor:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-129-1024x95.png)

Neste caso, ao realizar a entrada no produto, será necessário selecionar o depósito referente à este marketplace e prosseguir com os mesmos procedimento acima informado:

![Imagem 13: Neste caso, ao realizar a entrada no produto, será necessário selecionar o depósito referente à este marketplace e…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-130-1024x270.png)
