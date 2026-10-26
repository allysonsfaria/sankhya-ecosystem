---
id: "4410701941911"
titulo: "Quantidade conferida maior do que quantidade negociada no pedido/nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701941911-Quantidade-conferida-maior-do-que-quantidade-negociada-no-pedido-nota"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:21:15Z"
rotulos: ["Produtos", "Conferência", "Estoque", "#validadoHugo", "CORE_E01284", "CORE_E01285", "Quantidade conferida", "Erro CORE_E01284", "Unidade de negociação", "Erro"]
---

# Quantidade conferida maior do que quantidade negociada no pedido/nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/15993307074199) MENSAGEM:**

[CORE\_E01284] Quantidade conferida maior do que quantidade negociada no pedido/nota.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16121320010391) CAUSA:**

O erro ocorre quando existe uma divergência, na qual a quantidade que foi conferida é maior que o pedido/nota. Outra causa para o erro em questão é quando o cód. de barras da unidade padrão do produto está igual ao da unidade alternativa. Deste modo, quando o sistema tenta buscar na fila de conferência o produto, não consegue identificar qual das unidades é a correta. Portanto, ao colocar cod. de barras diferentes nos casos, é possível realizar a conferência pela unidade desejada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15993188371735) SOLUÇÃO:**

Ao realizar a conferência, use a mesma unidade utilizada durante a negociação. Por exemplo, ao realizar uma negociação com a opção **"Unidade Alternativa"**, o processo de conferência deverá ser realizado nesta mesma unidade. Caso contrário o sistema emitirá a mensagem:

**"Quantidade conferida maior do que quantidade negociada no pedido/nota."**

![Imagem 4: "Quantidade conferida maior do que quantidade negociada no pedido/nota."](https://ajuda.sankhya.com.br/hc/article_attachments/4416686868375)
