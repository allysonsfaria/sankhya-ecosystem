---
id: "9904104558999"
titulo: "O Gênero do produto é \"XX - XXXXX\", para isso é necessário que a opção \"Tem Rastro do Lote\" esteja marcada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9904104558999-O-G%C3%AAnero-do-produto-%C3%A9-XX-XXXXX-para-isso-%C3%A9-necess%C3%A1rio-que-a-op%C3%A7%C3%A3o-Tem-Rastro-do-Lote-esteja-marcada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:05:30Z"
rotulos: ["Produtos", "Configuração", "Lote", "Estoque", "CORE_E03874", "Necessidade de Marcação “Tem Rastro do Lote” para Certos Produtos", "Regulamentação Sanitária"]
---

# O Gênero do produto é "XX - XXXXX", para isso é necessário que a opção "Tem Rastro do Lote" esteja marcada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19351379267223) MENSAGEM:**

[CORE\_E03874] O Gênero do produto é "XX - XXXXX", para isso é necessário que a opção "Tem Rastro do Lote" esteja marcada. Efetue a configuração na aba Geral.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351379268631) SITUAÇÃO:**

Ao tentar cadastrar um novo produto a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19351359232535) CAUSA:**

Ocorre quando o produto possui regulações sanitárias e a marcação **"Tem Rastro do Lote"** não está marcada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351379276567) SOLUÇÃO:**

Ao informar um gênero no cadastro do produto que possui regulações sanitárias, como medicamentos por exemplo, é necessário que haja um controle por lote, sendo assim, é necessário que a marcação **"Tem Rastro do Lote"**esteja marcada.

Foi elaborado um novo grupo destinado a permitir a rastreabilidade de qualquer produto submetido às regulações sanitárias, além de defensivos agrícolas, produtos veterinários, odontológicos, medicamentos, entre outros. Para isto, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), foi disponibilizado a marcação **"Tem Rastro do Lote"**.

![Imagem 5: Foi elaborado um novo grupo destinado a permitir a rastreabilidade de qualquer produto submetido às regulações…](https://ajuda.sankhya.com.br/hc/article_attachments/19351359243287)

Para realizar a marcação Tem Rastro do Lote, o produto em questão deve estar configurado na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), com o campo **"Controlar por"** indicando a opção **"Número do lote"**:

![Imagem 6: Para realizar a marcação Tem Rastro do Lote , o produto em questão deve estar configurado na aba Medidas e Estoque ,…](https://ajuda.sankhya.com.br/hc/article_attachments/19351379281303)

Além disso, os parâmetros **"Usar data de Fabricação junto com Lote? - LOTEDTFAB"** e **"Usar data de validade junto com Lote? - LOTEDTVAL"** devem estar habilitados.

Os campos **"nLote"**,**"qLote"**,**"dFab"**e**"dVal"** que faziam parte do grupo de Medicamentos (med) na versão anterior, agora passaram a fazer parte do grupo de Rastreamento do produto (rastro).

No grupo de Medicamentos foi incluído o campo **"Cód. ANVISA"**, que pode ser configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), na aba [Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedicamentos).

![Imagem 7: No grupo de Medicamentos foi incluído o campo "Cód. ANVISA" , que pode ser configurado no Cadastro de Produtos , na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/19351359254551)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9904104558999-O-G%C3%AAnero-do-produto-%C3%A9-XX-XXXXX-para-isso-%C3%A9-necess%C3%A1rio-que-a-op%C3%A7%C3%A3o-Tem-Rastro-do-Lote-esteja-marcada#top)
