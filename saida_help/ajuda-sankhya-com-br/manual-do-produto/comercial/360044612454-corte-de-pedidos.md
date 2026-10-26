---
id: "360044612454"
titulo: "Corte de Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:27:05Z"
rotulos: ["Produtos", "Pedidos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Faturamento", "Central de Vendas", "Corte de Pedidos", "VALAGRUMINCORTE", "br.com.sankhya.mgecom.mov.cortedepedidos", "Corte de Pedidos manual", "Execução", "Estoque", "Corte"]
---

# Corte de Pedidos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311980125847) Módulo: Comercial > Rotinas > Ordem de Carga
```

---

O Corte de Pedidos é uma opção que você tem de eliminar itens ou determinada quantidade de itens de notas no faturamento, quando for feito um pedido de quantidade superior ao que realmente será entregue ou vendido. Assim, teremos o exemplo:

Foi lançado um pedido na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) com 50 unidades do produto X. O faturamento será de apenas 20 unidades. Assim, você **"corta"** 30 unidades no pedido, para que ao faturar o sistema já traga apenas a quantidade restante, 20 unidades.

![Imagem 2: Importante: notas enviadas ao WMS não poderão receber corte de produtos.](https://ajuda.sankhya.com.br/hc/article_attachments/16106738276759) **Importante:** notas enviadas ao WMS não poderão receber corte de produtos.

Esta tela está dividida em três partes, são essas:

[Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#filtros)                                                                                                [Botão Configurar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#bot%C3%A3oconfigurar)

[Botão Cortar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#bot%C3%A3ocortar)

![Imagem 3: Botão Cortar](https://ajuda.sankhya.com.br/hc/article_attachments/360084427493)

## Filtros

Na parte lateral esquerda da tela existem os filtros. Você pode utilizar os filtros rápidos por **"Período de Negociação"**, **"Empresa"** e **"Ordem de Carga"** e poderá também, configurar filtros através do botão de filtros personalizados.

No campo **"Período de Negociação"** informe o intervalo de data de negociação dos itens que serão cortados.

Informe o código da **"Ordem de Carga"**da nota que contém os itens para corte.

Insira a **"Empresa"** dos pedidos.

Depois de preencher os campos e formular os filtros necessários, clique em **"Aplicar"**.

![Imagem 4: Depois de preencher os campos e formular os filtros necessários, clique em "Aplicar" .](https://ajuda.sankhya.com.br/hc/article_attachments/360084427613)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#top)

## Botão Configurar

O botão **"Configurar"** possui opções de apresentação de dados na tela. São estas:

![Imagem 5: O botão " Configurar" possui opções de apresentação de dados na tela. São estas:](https://ajuda.sankhya.com.br/hc/article_attachments/360084428133)

- **Não exibir estoque?:** Não apresenta o campo **"Estoque"** na grade superior da tela de corte.
- **Exibir estoque por empresa?:** O sistema apresenta na grade superior da tela de corte, uma linha para cada empresa que tenha estoque dos produtos.
- **Exibir estoque total?:** Mostra o estoque total do produto no campo Estoque.
- **Exibir estoque do produto?:** O sistema apresenta em outra grade, todo o estoque de cada produto selecionado, como quantidade reservada etc. Observe a figura abaixo.

![Imagem 6: Exibir estoque do produto? : O sistema apresenta em outra grade, todo o estoque de cada produto selecionado, como…](https://ajuda.sankhya.com.br/hc/article_attachments/360083268634)

Existem ainda as caixas de seleção com as seguintes opções:

- **Exibir apenas produtos com estoque insuficiente?:** Mostra apenas produtos que não possuem estoque suficiente para atender aos pedidos.
- **Exibir estoque - reserva?:** Mostra no campo Estoque o estoque do produto, menos a quantidade reservada nos pedidos.
- **Exibir quantidade em unidade de compra?:** Quando estiver marcada, serão apresentados na grade os campos **"Volume Compra"** e **"Qtd.Compra"**.
- **Exibir quantidade em unidade do pedido na grade de corte:** Com esta marcação efetuada e caso o item da nota tiver volume alternativo, os valores dos campos **"Qtd. Negociação"**, **"Qtd. Entregue"**, **"Qtd. Corte"**, serão apresentados conforme o volume alternativo. Com ela marcada, o campo Qtd. Corte, ao ser editado respeitará a unidade alternativa. O campo **"Qtd. Nota"** apresenta a quantidade no pedido, este campo será útil quando estiver sendo exibida a quantidade em unidade padrão, e neste é apresentado o valor que está no item da nota.
- **Exibir painel de itens do pedido?:** Apresenta ao lado da grade inferior outra grade contendo todos os itens do pedido selecionado. Observe a figura abaixo.

![Imagem 7: Exibir painel de itens do pedido? : Apresenta ao lado da grade inferior outra grade contendo todos os itens do pedido…](https://ajuda.sankhya.com.br/hc/article_attachments/360083269194)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#top)

## Botão Cortar

O botão Cortar fará o corte no produto selecionado na primeira grade.

A tela aberta através desse botão, apresenta a quantidade pendente do produto e o campo para informar a quantidade de corte e ainda opções de **"Estratégia de Corte"**.

![Imagem 8: A tela aberta através desse botão, apresenta a quantidade pendente do produto e o campo para informar a quantidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/360083269394)

A opção **"Distribuir corte"** faz a distribuição da quantidade cortada nos pedidos da segunda grade, de forma proporcional à quantidade de cada pedido. A distribuição do corte considerará o número de **"Decimais para Quantidade"** definido no Cadastro de Produtos, como critério de arredondamento.

A opção **"Não distribuir corte"** faz o corte de acordo com a ordenação da segunda grade dos pedidos, cortando a partir do primeiro pedido até completar a quantidade de corte.

**Grade de Produtos**

Nesta grade, localizada logo abaixo dos filtros, serão apresentados os produtos que fazem parte do pedido filtrado.

A coluna **"Produções Programadas"** apresentará a quantidade de produções programadas através do somatório do tamanho do lote das Ordens de Produção, que possuam o status da ordem de produção igual à **"Criado e Programado (P2 - Programado, R - Criado)"**.

Já a coluna **"Produções Pendentes"** exibirá a quantidade de produções pendentes e serão consideradas as produções em andamento, com o cálculo através do somatório do tamanho do lote das Ordens de Produção que possuam o status da ordem igual à **"Em andamento (A - Andamento)"**.

Por fim, a coluna **"Produções Adiadas"** apresentará a quantidade de produções adiadas através do somatório do lote das Ordens de Produção que possuam o status igual à **"Suspenso (S - Suspendido)"**.

**Importante**: O parâmetro **"Atualiza campos produçao programada, pendente e ad - ATUALIZAPROD"** irá interferir nas colunas acima mencionadas, ou seja, quando você habilitá-lo, fará com que as colunas tenham seu cálculo atualizado e, de forma contrária, se você desabilitá-lo, não terá as colunas atualizadas.

**Grade de Pedidos**

Localizada logo abaixo da grade de produtos, esta segunda grade apresenta os pedidos que possuem o produto selecionado na grade de produtos.

Acima desta grade, existem os botões **"Cortar tudo"**, **"Limpar corte"** e **"Detalhes do pedido"**.

Ao clicar em Cortar tudo, será efetuado o corte do produto selecionado em todos os pedidos apresentados.

Caso deseje desfazer o corte, você deverá utilizar o botão Limpar corte.

**Nota:** Após clicar em **"Salvar"**, mesmo que seja alterada a coluna **"Faturamento"** para a opção **"Encerrar pedido"**, o pedido continuará a ser exibido no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232294-Portal-de-Vendas) como pendente.

A coluna **"Diferença"** trata da diferença da quantidade negociada do pedido, e a quantidade entregue referente ao corte. Exemplo: Pedido de Venda com 10 UN do produto A, corta-se 5 UN e fatura somente as 5 UN restantes. O valor da coluna Diferença passa a ser 5 UN.

Para efetuar cortes parciais ou diferentes em cada pedido, preencha na grade dos pedidos a coluna Qtd.Corte e salve para definir a quantidade a ser cortada.

![Imagem 9: Para efetuar cortes parciais ou diferentes em cada pedido, preencha na grade dos pedidos a coluna Qtd.Corte e salve…](https://ajuda.sankhya.com.br/hc/article_attachments/360083269694)

**Observação:** Caso sejam necessários para o processo de cada empresa, a Grade de Pedidos conta com as colunas **"Prev. Ent. Pedido"** e **"Prev. Ent. Item"**, que se referem à Previsão de Entrega nos Pedidos e dos Itens, respectivamente.

Além disso, à medida que os cortes forem realizados, você terá no final da coluna Qtd. Corte, um somatório correspondente aos cortes efetuados, facilitando a percepção da quantidade de itens que ainda podem ser cortados.

A coluna Faturamento pode ser alterada deixando o Faturamento pendente ou Encerrar pedido.

A opção Faturamento pendente, se marcada, fará com que a quantidade fique pendente para faturamento posterior, se desmarcada a opção, o pedido é faturado e a quantidade cortada não é faturada, ou seja, deixando como **"Faturamento Pendente"**, é mantido o pedido pendente naquela quantidade.

Ou seja, se não tiver estoque suficiente para atender todo o pedido, ao marcar Faturamento Pendente, o sistema deixará a quantidade que cortou para que ao ter estoque, possa faturar esse mesmo pedido. Se colocar como Encerrar Pedido, será encerrado o pedido sem que nada fique pendente.

Quando se encerra o pedido, é possível consultar os pedidos que tiveram corte e quais produtos foram cortados; basta fazer o filtro pela data de negociação, pela empresa ou pela Ordem de Carga, irá aparecer a quantidade, o corte e a quantidade líquida.

**Nota:** O procedimento de corte, pode sofrer a influência do parâmetro **"Valida agrupamento mínimo no corte? - VALAGRUMINCORTE"** que, quando ativado, será feita a validação do agrupamento mínimo dos produtos, nas telas de Corte, Portal de Vendas e Central de Vendas.

Para que isso ocorra, é necessário que no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque), o campo **"Agrupamento mínimo"** esteja devidamente preenchido. Ao lançar uma nota de venda, sendo necessário realizar o corte do produto, ou mesmo na tela de Corte de Pedidos, este deve ser feito em valores múltiplos do Agrupamento mínimo informado para o produto. Caso seja feita a tentativa de corte fora deste padrão, será exibida a seguinte mensagem:

**"Corte não está de acordo com o agrupamento mínimo do produto."**

O botão **"Detalhes do pedido"** alterna a tela para uma exibição detalhada do pedido selecionado e tem as mesmas opções de corte da grade de pedidos.

![Imagem 10: O botão "Detalhes do pedido" alterna a tela para uma exibição detalhada do pedido selecionado e tem as mesmas opções de…](https://ajuda.sankhya.com.br/hc/article_attachments/360084429213)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612454-Corte-de-Pedidos#top)
