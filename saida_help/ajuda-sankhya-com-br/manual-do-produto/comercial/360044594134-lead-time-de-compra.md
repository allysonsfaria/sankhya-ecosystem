---
id: "360044594134"
titulo: "Lead Time de Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594134-Lead-Time-de-Compra"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:19:16Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Análise de Giro", "Lead Time de Compra", "tempo de compra", "tempo", "Medidas e Estoque", "Pedido de Compra", "br.com.sankhya.mgecom.cons.leadtimecompra", "Lead Time de Compra manual", "Estoque", "Atualização Automática", "Gerenciamento de Estoque", "Atualização de Informações", "Comercial"]
---

# Lead Time de Compra

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311674128407) Módulo: Comercial > Gerente
```

---

Esta tela é um complemento a matriz de análise de giro, e deverá ser utilizada para calcular o Lead Time de Compra e atualizar o [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), facilitando a gestão de estoque. Nesta tela serão calculados os Lead Times: menor, médio e o maior.

O Lead Time de Compra é a quantidade de dias entre o lançamento do Pedido de Compra e a entrega do produto pelo fornecedor, ou seja, a entrada do produto no estoque. O Lead Time é calculado pelo sistema por meio da diferença entre a Data de Negociação do Pedido de Compra e a Data da Entrada/Saída da Nota de Compra gerada através do faturamento do pedido.

![Imagem 2: O Lead Time de Compra é a quantidade de dias entre o lançamento do Pedido de Compra e a entrega do produto pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/4408512452887)

A esquerda da tela tem as opções de filtro, e logo abaixo as configurações com as formas de atualização.

![Imagem 3: A esquerda da tela tem as opções de filtro, e logo abaixo as configurações com as formas de atualização.](https://ajuda.sankhya.com.br/hc/article_attachments/4408511745943)

A marcação **"Quebra por Empresa"** definirá se a visão será geral por Produto ou por Produto/Empresa. Quando marcado preencherá a coluna **"Empresa"** e neste caso o sistema irá compor a grade agrupando as informações por empresa, e buscará o Lead time registrado da aba [Impostos/Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa) do Cadastro de Produtos. Quando desmarcado as informações da grade virão agrupadas por Produto, o Lead time registrado será o da aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque) e a coluna Empresa ficará vazia.

A opção escolhida em **"Atualizar Lead Time de Compra quando"** definirá a condição para que seja atualizado o Lead Time dos produtos e o quadro **"Atualizar Lead Time de Compra com"**, definirá com qual valor ele será atualizado.

Após definição dos filtros, ao clicar em **"Aplicar"** o sistema irá apresentar na grade principal os produtos comprados, que tiveram o lançamento de um Pedido de Compra e o Faturamento para uma Nota de Compra. Assim, será medido o tempo entre a colocação do pedido e a entrada da nota.

A grade mostrará o **"Fornecedor Preferencial"** do produto, a Empresa se a marcação Quebra por Empresa estiver assinalada, a **"Quantidade"** de fornecedores do produto no período selecionado e os **"Tempos"** (Lead Times): **"Menor"**, **"Médio"** e **"Maior"** de entrega.

O gestor visualizará também o campo **"Lead Time de Compra registrado"** que mostra o valor registrado para o Lead Time no Cadastro de Produtos, aba Impostos/Informações por Empresa. Este campo ficará aberto para digitação e se for alterado, atualizará a informação diretamente no Cadastro de Produtos.

É possível visualizar os produtos da grade em modo formulário, além disso, o sistema mostra num painel a direita os **"Detalhes da entrega"**. Caso este painel seja fechado, não será possível abri-lo novamente, a não ser fechando e abrindo a tela.

Ao selecionar um produto na grade superior, é possível visualizar na grade inferior as informações sobre **"Tempos de entrega"** de cada fornecedor para o Produto selecionado.

A esquerda da tela existe o botão ![Imagem 4: A esquerda da tela existe o botão "Atualizar Lead Time" que, ao ser clicado fará a atualização do Lead Time de compra…](https://ajuda.sankhya.com.br/hc/article_attachments/16278779383063) **"Atualizar Lead Time"** que, ao ser clicado fará a atualização do Lead Time de compra do produto. A atualização será feita conforme as preferências selecionadas nos campos acima do botão, de forma a colocar o menor, o médio ou maior tempo de entrega calculado, conforme regra: colocar **"Sempre atualizar"**, ou **"Novo valor maior que o atual"** ou então **"Novo valor menor que o atual"**.

Ao acionar o botão ![Imagem 5: Ao acionar o botão "Agendar Lead Time" , será aberta a tela Agendador de Lead Time de Compra .](https://ajuda.sankhya.com.br/hc/article_attachments/16278779396887) **"Agendar Lead Time"**, será aberta a tela [Agendador de Lead Time de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051307174).

Caso esteja marcado para Quebra por Empresa, então o sistema atualizará o Lead Time de Compra da aba [Impostos/Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa) do Cadastro de Produtos. Se não estiver marcado para Quebra por Empresa, o campo a ser atualizado será o Lead Time de Compra da aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque).
