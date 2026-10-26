---
id: "44012252190999"
titulo: "Como gerar uma reposição de lojas manual?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012252190999-Como-gerar-uma-reposi%C3%A7%C3%A3o-de-lojas-manual"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:28Z"
rotulos: ["sync_hc", "magis5", "magis5_204056240160", "sync_hash_6e5a0124d2b7"]
---

# Como gerar uma reposição de lojas manual?

## O módulo "Reposição de Lojas" é utilizado para automatizar o processo de pedido de produtos.

O módulo "Reposição de Lojas" é utilizado para automatizar o processo de pedido de produtos. Com base no histórico de vendas, pedidos de venda e tempo médio de recebimento do produto dos fornecedores (leadtime), esse recurso oferece sugestões precisas de quantidades a serem compradas.

Ao utilizar este recurso, o sistema apresenta um conjunto de filtros que permite visualizar a movimentação dos produtos em um determinado período e quantas unidades desses produtos podem ser adquiridas para atender à demanda em um número específico de dias, conforme informado nos filtros. Essas informações são essenciais para tomar decisões embasadas sobre o pedido de reposição de estoque.

A utilização do módulo de “Reposição de Lojas” traz diversos benefícios para o empreendimento. Primeiramente, agiliza o processo de reposição de estoque, evitando a falta de produtos e garantindo que a demanda seja atendida de forma adequada. Além disso, ao utilizar os dados históricos de vendas e o tempo médio de recebimento dos produtos, o sistema ajuda a evitar o excesso de estoque e otimiza os investimentos em estoque.

---

Para realizar uma reposição de lojas manual, na barra de menus, clique em: Controle de Produção → Reposição de Lojas:

![Imagem 1: Para realizar uma reposição de lojas manual, na barra de menus, clique em: Controle de Produção → Reposição de Lojas:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image.png)

**UTILIZANDO OS FILTROS**

Os filtros permitem acessar informações sobre as vendas no período estimado. Para realizar uma pesquisa eficaz, é importante compreender os seguintes filtros:

![Imagem 2: Os filtros permitem acessar informações sobre as vendas no período estimado. Para realizar uma pesquisa eficaz, é…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-1.png)

- **Dias de Cobertura:** Indica o período desejado de cobertura do estoque.
- **Leadtime Fornecedor:** Indica o prazo de entrega do fornecedor.
- **Fornecedor:** É utilizado para informar em qual empreendimento será realizada a consulta de de estoque dos produtos. O fornecedor deverá ter o campo "ID Empreendimento Ref." preenchido (para mais informações, [clique aqui](https://ajuda.artemis5.com.br/como-cadastrar-um-novo-fornecedor/)).
- **Empreendimentos:** Indique qual empreendimento deve ser analisado para reposição. É possível inserir quantos empreendimentos desejar.
- **Marcas:** Selecione a marca desejada para um resultado mais específico.
- **Produtos:** Selecione os produtos que deseja consultar. Se nenhum produto for selecionado, o sistema trará todos os produtos com estoque no fornecedor.
- **Proporção de Estoque:** Quando ativada, esta opção garante que o estoque do fornecedor não seja ultrapassado.

Os campos "Dias de Cobertura", "Leadtime Fornecedor", "Fornecedor" e "Empreendimento" são obrigatórios.

Após preencher os campos desejados, clique em "Aplicar filtro" e aguarde o carregamento dos produtos:

![Imagem 3: Após preencher os campos desejados, clique em "Aplicar filtro" e aguarde o carregamento dos produtos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-2.png)

Embaixo do nome do produto, temos três campos:

![Imagem 4: Embaixo do nome do produto, temos três campos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-3.png)

- **Universal:** É a marca do produto.
- **Sem demanda:** Este campo é variável. Ao inserir os itens no campo à direita, o texto será alterado para "no carrinho" ou "falta de estoque".
- **994:** É a quantidade de itens em estoque no fornecedor informado.

Ao lado do nome do produto, temos os campos:

![Imagem 5: Ao lado do nome do produto, temos os campos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-4.png)

O primeiro campo (onde consta "12" e "509") indica a quantidade em estoque no empreendimento analisado. Os campos "25" e "10" indicam as movimentações dentro do período de cobertura.

Após inserir a quantidade desejada nos produtos, clique em "Finalizar Compra":

![Imagem 6: Após inserir a quantidade desejada nos produtos, clique em "Finalizar Compra":](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-5.png)

Um resumo com o detalhamento do pedido será exibido:

![Imagem 7: Um resumo com o detalhamento do pedido será exibido:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-6.png)

Ao clicar em "Continuar", será necessário informar a quantidade de parcelas e a periodicidade para pagamento, por exemplo:

![Imagem 8: Ao clicar em "Continuar", será necessário informar a quantidade de parcelas e a periodicidade para pagamento, por…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2024/06/image-7.png)

Após inserir essas informações, clique em "Gerar Pedido" e o pedido estará concluído.

Observação: O pedido deverá sair em nome de um cliente que deverá ser vinculado ao empreendimento analisado. Para informações sobre como realizar este procedimento, [clique aqui](https://ajuda.artemis5.com.br/como-vincular-um-empreendimento-a-um-cliente/)
