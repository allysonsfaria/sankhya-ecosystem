---
id: "44011975557911"
titulo: "Como realizar um pedido utilizando o módulo Sugestão de Compras?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011975557911-Como-realizar-um-pedido-utilizando-o-m%C3%B3dulo-Sugest%C3%A3o-de-Compras"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:15:41Z"
rotulos: ["sync_hc", "magis5", "sync_hash_daf853262370", "magis5_204056240156"]
---

# Como realizar um pedido utilizando o módulo Sugestão de Compras?

## O módulo de "Sugestão de Compras" é utilizado para automatizar o processo de pedido de produtos.

O módulo de "Sugestão de Compras" é utilizado para automatizar o processo de pedido de produtos. Com base no histórico de vendas, estoque de venda e tempo médio de recebimento do produto dos fornecedores (Leadtime), esse recurso oferece sugestões precisas de quantidades a serem compradas.

Ao utilizar este recurso, o sistema apresenta um conjunto de filtros que permite visualizar a movimentação dos produtos em um determinado período e quantas unidades desses produtos podem ser adquiridas para atender à demanda em um número específico de dias, conforme informado nos filtros. Essas informações são essenciais para tomar decisões embasadas sobre o pedido de reposição de estoque.

Com base nessas sugestões, o lojista tem a opção de seguir ou não as recomendações do sistema ao realizar o pedido.

A utilização do módulo de "Sugestão de Compras" traz diversos benefícios para o empreendimento. Primeiramente, agiliza o processo de reposição de estoque, evitando a falta de produtos e garantindo que a demanda seja atendida de forma adequada. Além disso, ao utilizar os dados históricos de vendas e o tempo médio de recebimento dos produtos, o sistema ajuda a evitar o excesso de estoque e otimiza os investimentos em estoque.

Outra vantagem importante desse módulo é a redução de erros e retrabalhos, uma vez que as sugestões são baseadas em informações precisas e atualizadas. Isso contribui para uma gestão mais eficiente do estoque, evitando desperdícios e minimizando os riscos de produtos obsoletos ou vencidos.

---

Na barra de menus, clique em: Suprimentos → Sugestão de Compras.

![Imagem 1: Na barra de menus, clique em: Suprimentos → Sugestão de Compras.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-3-1024x203.png)

**UTILIZANDO OS FILTROS**

Os filtros são utilizados para ter acesso ao que foi vendido no tempo estimado. Para realizar uma pesquisa é necessário entender os filtros, sendo eles:

![Imagem 2: Os filtros são utilizados para ter acesso ao que foi vendido no tempo estimado. Para realizar uma pesquisa é necessário…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-1024x215.png)

- **Cobertura (Dias):** Gostaria de ter cobertura de estoque por quanto tempo?

- **LT Fornec. (Dias):** Qual será o prazo de entrega do Fornecedor?

- **Produtos:** Nome do Produto

- **Marca:** Marca do Produto (lembrando que o produto só é exibido neste campo se, no cadastro do produto, ele foi vinculado a alguma marca)

- **Empreendimentos:** Deseja consultar quais empreendimentos?

- **Categoria:** Categoria do Produto.

- **Depósito**: A sugestão de compras deve ser com base em quais depósitos?

- **Estoque**: Considerar produtos com estoque, sem estoque ou todos?

- **Somente produtos com movimentação de estoque**: Considerar apenas produtos que tiveram movimentação de estoque no período selecionado?

Atenção: Não é obrigatório preencher todos os campos, apenas “Cobertura (Dias)” e "Empreendimentos”.

**RESULTADO DA PESQUISA**

Para ter acesso ao provisionamento de compras, iremos utilizar os filtros:

- Cobertura: 500 dias
- LT Fornec.: 10 dias
- Fabricante: Universal
- Empreendimento: 1 - Artemis5 - Distribuição
- Depósitos: Depósito - Artemis5 Distribuidora
- Estoque: Todos
- Somente produto com movimentação de estoque? Não

![Imagem 3: Somente produto com movimentação de estoque? Não](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-1-1024x193.png)

Ao clicar em “Aplicar Filtros”, o **Artemis5** trará uma tabela com alguns dados importantes:

![Imagem 4: Ao clicar em “Aplicar Filtros”, o Artemis5 trará uma tabela com alguns dados importantes:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-2-1024x262.png)

O provisionamento é para os próximos 510 dias. Os dias utilizados para cálculo da tabela são a soma dos campos: **Cobertura (Dias) + LT Fornec. (Dias)**, que, segundo os filtros inseridos, resultaram em **510** **dias**.

- **Transferências:** Quantidade de itens foram transferidos entre unidades nesses 510 dias;
- **Vendas:** Quantidade de vendas que foram realizadas nesses 510 dias;
- **Qtd. Estoque:** Quantidade de produtos em estoque atualmente;
- **Orçamentos em Aberto:** Orçamentos abertos até a data atual;
- **Último Custo:** Último preço de custo do produto.

Então, considerando essas colunas acima, é feito um sugestionamento nas colunas a seguir, que são divididas em: “Sem Pedidos em Trânsito” e “Com Pedidos em Trânsito”.

A coluna “Sem Pedidos em Trânsito” considera apenas os produtos com venda concretizada (não considerando orçamentos abertos até a data da consulta) e a coluna “Com Pedidos em Trânsito” considera os produtos com venda concretizada e os orçamentos que estão abertos até a data da consulta.

Ambas colunas possuem subcolunas em comum: “VMD”, “Qtd Comprar” e “Custo Compra”.

- **VMD:** É o valor médio diário com base nos 510 dias versus a quantidade de produtos sugeridos;

- **Qtd. Comprar:** É a quantidade de itens que deverão ser comprados com base na coluna principal (“Sem Pedidos em Trânsito” ou “Com Pedidos em Trânsito”);

- **Custo Compra:** Se for pedido a quantidade sugerida, o “Custo Compra” informa qual será o valor do pedido.

![Imagem 5: Custo Compra: Se for pedido a quantidade sugerida, o “Custo Compra” informa qual será o valor do pedido.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-3-1024x293.png)

Analisando a primeira linha desta coluna, temos as seguintes informações:

![Imagem 6: Analisando a primeira linha desta coluna, temos as seguintes informações:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-4-1024x166.png)

1. O estabelecimento teve 496 vendas nos últimos 510 dias;
2. 3 orçamentos estão abertos até a data da consulta;
3. Tiveram 137 transferências deste produto em 510 dias;
4. O último custo do produto foi R$61,43.

Com base nessas informações, o **Artemis5** sugeriu duas opções:

- A primeira opção é realizar a compra de 305 itens (onde o custo desse pedido daria R$18.736,15, com um valor médio diário de R$1,24) ou,
- A segunda opção é realizar a compra de 308 itens (onde o custo desse pedido daria R$18.920,44, com um valor médio diário de R$1,25).

Para realizar o pedido deste item, informe, na coluna “Pedido Real” quantos itens irá pedir e se houve alguma alteração no preço de custo do produto. Por exemplo:

Incluímos 450 unidades deste item e alteramos o preço de custo para R$58,63. O **Artemis5** realizou o cálculo de quanto ficará esse pedido:

![Imagem 7: Incluímos 450 unidades deste item e alteramos o preço de custo para R$58,63. O Artemis5 realizou o cálculo de quanto…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-5-1024x112.png)

Descendo a tela, vemos um bloco chamado “Pedidos”. Ao inserir as 150 unidades do item acima, automaticamente, o **Artemis5** pressupõe que este item será pedido. Então, ele acrescenta o item à lista de pedidos:

![Imagem 8: Descendo a tela, vemos um bloco chamado “Pedidos”. Ao inserir as 150 unidades do item acima, automaticamente, o…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-6-1024x113.png)

Caso queira realizar outro conjunto de filtros para buscar por outro item, em outro prazo ou outro fornecedor, este item acima inserido não será excluído, a menos que clique no botão “Excluir”, à direita.

Como exemplo, inseri mais alguns itens ao pedido:

![Imagem 9: Como exemplo, inseri mais alguns itens ao pedido:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-356.png)

Após finalizar o pedido, é necessário informar o acordo comercial para então, gerar o pedido:

![Imagem 10: Após finalizar o pedido, é necessário informar o acordo comercial para então, gerar o pedido:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-7-1024x232.png)

- **Qtd. Parcelas**, informe em quantas parcelas esse pedido será pago;

- **Periodicidade** informe qual será o prazo entre elas (por exemplo, a cada 15 dias);

- **Fornecedor**, informe qual o fornecedor dos itens.

No exemplo a seguir, inserimos 3 parcelas a cada 15 dias. O Fornecedor selecionado foi o “Acqua Marine”:

![Imagem 11: No exemplo a seguir, inserimos 3 parcelas a cada 15 dias. O Fornecedor selecionado foi o “Acqua Marine”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-8-1024x347.png)

Como visto, o valor total é dividido na quantidade de parcelas informadas e o prazo também é estabelecido de acordo com os dias informados em “Periodicidade”.

Após finalizar o preenchimento das informações, clique em “Gerar Pedido”, localizado no canto inferior direito:

![Imagem 12: Após finalizar o preenchimento das informações, clique em “Gerar Pedido”, localizado no canto inferior direito:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/11/image-9-1024x347.png)

O pedido está gerado!

Para visualizar o pedido gerado, acesse o módulo: Compras → Pedidos de Compras.

Atenção: Além das linhas exibidas por padrão, é possível inserir outras linhas clicando em “Colunas”, selecionando a coluna desejada e clicando em “Salvar”. Como é possível ver, foi inserido nos exemplos, a coluna “Sug. de Compra c/ Pedidos em Trânsito”:

![Imagem 13: Atenção: Além das linhas exibidas por padrão, é possível inserir outras linhas clicando em “Colunas”, selecionando a…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-359.png)

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011942478871)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
