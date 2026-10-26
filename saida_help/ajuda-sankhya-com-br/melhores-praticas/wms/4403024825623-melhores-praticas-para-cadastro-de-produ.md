---
id: "4403024825623"
titulo: "Melhores práticas para cadastro de produto que trabalha com WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403024825623-Melhores-pr%C3%A1ticas-para-cadastro-de-produto-que-trabalha-com-WMS"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:24:03Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "#validadoRonald", "Configurações de Controle WMS no Cadastro de Produtos"]
---

# Melhores práticas para cadastro de produto que trabalha com WMS

A marcação **“Controlado pelo WMS?"**, somente estará visível se o opcional WMS estiver habilitado na base de dados para os módulos COMERCIAL. Para o WMS esta opção é padrão do módulo, esta marcação indica se o produto será separado ou armazenado no WMS. Uma vez marcada a opção, só será possível desmarcá-la se não existir estoque deste produto no WMS. Quando esta opção estiver marcada na aba **“WMS”** será habilitada no cadastro de produtos.

Na aba WMS, o campo **“Usa controle adicional no WMS?"**, somente ficará habilitado quando o produto tiver controle adicional de estoque e estiver marcado como **"Controlado pelo WMS"**. Esta marcação permitirá que o WMS faça controle adicional de estoque

**![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16343296782743) OBSERVAÇÃO:**

Fique atento, pois  o WMS não trabalha com controle adicional de estoque por "Série".

Para utilizar o controle por "Data de Validade" juntamente como a opção **"Número de Lote"** ligue o parâmetro: **"Usar data de validade junto com o Lote?- (LOTEDTVAL)".** Nesta opção o sistema trabalhará com o algoritmo **FEFO – First Expire First out** (primeiro a expirar é o primeiro a sair). Quando o produto tiver controle adicional de estoque e for controlado pelo WMS, ao marcar a opção Usa controle adicional no WMS? será utilizado o controle de lote do WMS e para controlar data de validade no WMS basta informar o Shelflife na aba WMS do cadastro do produto.

Podendo utilizar nas tarefas do WMS, o código de barras da **Unidade padrão**. O código de barras, informado na lista de opções, também será apresentado na aba de **"Unidades Alternativas"**. Na aba Unidades Alternativas o código de barras não será  importado automaticamente da aba **“Medidas e Estoque”**, portanto deverá ser informado manualmente pelo usuário. De tal modo, cada controle deverá ter **obrigatoriamente** um código de barras diferente. As configurações que serão utilizadas devem estar de acordo com as melhores práticas, como podemos ver no artigo : [Unidade alternativa com WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4402883089687)
