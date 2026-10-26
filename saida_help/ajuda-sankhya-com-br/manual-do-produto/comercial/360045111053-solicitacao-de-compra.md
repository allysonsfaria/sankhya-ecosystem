---
id: "360045111053"
titulo: "Solicitação de Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111053-Solicita%C3%A7%C3%A3o-de-Compra"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:30:48Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Requisições", "Portal de Vendas", "Liberação de Limites", "RESPCOTCOMPR", "TOP", "Confirmação do Pedido", "Previsão de Entrega do Produto", "Solicitação de Compra", "Solicitação de Compra manual", "Estoque", "Geração Automatizada", "Configurações de Sistema"]
---

# Solicitação de Compra

A solicitação de compra está disponível para os tipos de movimento Pedido de Venda, Pedido de Requisição, Venda e Requisição.

Como a Solicitação de Compra é uma ponte para o módulo de **"Cotação"**, é necessário que você possua o módulo.

Ao efetuar a confirmação de um pedido/nota, o sistema gerará uma solicitação de compra.

#### **(1)** Configurações para Gerar a Solicitação de Compra na confirmação

Na tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), a marcação **"Participa da opção "Gerar Solicitação de Compra na Confirmação" do cadastro da top?"** deve estar realizada.

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral), a marcação **"Solicita Compra?"** deve estar realizada.

No [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), a marcação **"Gera Solicitação de Compra na Confirmação"** deve estar efetuada.

Caso o parâmetro **"O responsável pela cotação tem que ser comprador?** **RESPCOTCOMPR"** esteja ligado, ao confirmar o lançamento, o sistema exibirá uma tela de pesquisa para que você indique qual comprador será utilizado na geração da solicitação de compra. Para o comprador aparecer nesta tela de pesquisa, é necessário que, no cadastro de Vendedores/Compradores o tipo seja Comprador e o Código do Funcionário tem que ser igual ao Código do Funcionário do Usuário.

#### **(1)** Gerar Solicitação de Compra através do botão "Outras Opções" nos Portais

Será possível a geração da Solicitação de Compra, no Portal de Vendas e Portal de Mov. Internas através do botão **"Outras Opções"**. Ao selecionar o título na grade **"Resultado da seleção"**, o sistema habilitará as opções **"Gerar solicitação de compra p/ produtos sem estoque"** e **"Gerar solicitação de compra"**.

Através da opção **"Gerar Solicitação de Compra p/ produtos sem estoque"**, o sistema gerará solicitação de compra para os produtos que não possuem estoque suficiente. A quantidade gerada, será a quantidade do pedido selecionado. O sistema não calcula a diferença solicitada menos a quantidade em estoque.

**Nota:** para que a validação do estoque seja feita é necessário que na tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaestoque), o campo **"Valida estoque"** esteja configurado com uma opção diferente de **"Não Valida"**.

A opção **"Gerar Solicitação de Compra"** criará uma solicitação de compras para os itens do lançamento, de acordo com a quantidade necessária (quantidade negociada - quantidade entregue - quantidade corte).

Caso o produto tenha estoque e mesmo assim você deseje gerar uma solicitação de compra utilizando a opção de Gerar Solicitação de Compra p/ produto sem estoque, o sistema emitirá a mensagem: **"Não será gerada solicitação de compra, pois os produtos originais já foram todos entregues ou cortados"**.

**Observação:** essa solicitação de compra é gerada no módulo de cotação da Sankhya.

- #### Para a geração de Solicitação de Compra Automática quando o produto possui estoque disponível:

  | **Configuração:** É necessário que as configurações de **Liberação de Limites** para o **evento 40** ("Solicitação de compra p/ produto em estoque") estejam devidamente ativadas.  **Comportamento do Sistema:** Neste cenário, o sistema adota um fluxo de controle. Em vez de criar a solicitação de compra de forma direta e automática, o sistema primeiro gerará uma **pendência de aprovação** para o usuário ou grupo de aprovadores configurado." |
  | --- |

#### **(1)**Previsão de Entrega do Produto

Na configuração do layout da nota o campo **"Dt. Prev. Entrega"** dos itens, permite que você possa informar a Data de Previsão de Entrega do Produto. Este campo estará disponível para os tipos de movimento **"Pedido de Compra"**, **"Compra"**, **"Pedido de Venda"**, **"Pedido de Requisição"**, **"Requisição"**.

Caso você utilize o Layout Padrão do sistema para estes tipos de movimentos, este campo será visualizado como padrão.

Uma vez preenchido, ao solicitar a compra, seja pelo Pedido de Venda ou Pedido de Requisição ou Requisição, seja na confirmação seja em Outras Opções, o sistema levará esta informação a Solicitação de Compra, no campo Data Entrega.

Configurações necessárias:

- O campo Dt. Prev. Entrega tem que estar disponível na Grade de Itens da Central de Compras. Para isto, acesse a tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota) e inclua este campo no Tipo movimento Compra.

**Nota:** se o tipo de movimento não permitir a visualização do campo, não será disponibilizado na Grade de Itens.

- **Evento 40 (Liberação de Limites):** Para que o sistema trate solicitações de produtos que ainda possuem estoque, o evento **"40 - Solicitação de compra p/ produto em estoque"** deve estar ativado e configurado na tela Tipos de Liberação de Limites.

  **Nota** : isso garantirá que, em vez da geração automática, o sistema crie uma pendência de aprovação.
- No Portal de Vendas, após o preenchimento do campo e confirmação da nota foi gerado a solicitação de compra.

A tela de Solicitação de Compra ainda não foi convertida para o Sankhya Om, portanto, será visualizada a Data Entrega pelo MGE.

**Importante:**

- Quando efetua-se a Entrega de um Pedido de Requisição para uma Requisição, a solicitação de compra será a mesma.
- A opção de Gerar solicitação de compra ou Gerar Solicitação de Compra para produtos sem estoque estará habilitada somente se o lançamento estiver confirmado e não houver solicitação já vinculada.
- Se no lançamento não for informada a Dt.Prev.Entrega, esta irá vazia para o campo Data Entrega na Solicitação de Compra.
