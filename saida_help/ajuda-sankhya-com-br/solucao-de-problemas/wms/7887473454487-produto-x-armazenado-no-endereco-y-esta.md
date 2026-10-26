---
id: "7887473454487"
titulo: "Produto: X armazenado no endereço: Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7887473454487-Produto-X-armazenado-no-endere%C3%A7o-Y-est%C3%A1-configurado-com-a-unidade-alternativa-a-quantidade-negociada-no-Pedido-Nota-n%C3%A3o-%C3%A9-multiplo-dessa-unidade"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:12:54Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "não apagar", "Resolução para Problemas com Unidade Alternativa e Quantidade no Pedido", "Erro"]
---

# Produto: X armazenado no endereço: Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16541730320791)MENSAGEM**:

"Produto: X armazenado no endereço: Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade.
O Envio não foi concluído para não fracionar o Estoque.
Pedido: X"

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16541730323095) SOLUÇÃO:**

![Imagem 3: Verifique na tela de "Produto" , na aba "WMS" , o endereço de picking vinculado ao produto.](https://ajuda.sankhya.com.br/hc/article_attachments/16541747089431) Verifique na tela de **"Produto"**, na aba **"WMS"**, o endereço de picking vinculado ao produto.

**(1)** Verifique na tela **"Estoque/endereçamento WMS"** se o endereço picking vinculado está com o produto correto.

**(1)** Caso não esteja, corrija  o endereço de picking vinculado no produto para o picking correto com o produto no estoque, ou faça o inventário dos endereços para ficarem corretos com o vinculo.

![Imagem 4: Verifique na tela tela "Estoque/endereçamento WMS" se tem mais de uma unidade armazenada no endereço picking. Caso…](https://ajuda.sankhya.com.br/hc/article_attachments/16541747091479) Verifique na tela tela **"Estoque/endereçamento WMS"** se tem mais de uma unidade armazenada no  endereço picking. Caso tenha, corrija para a unidade correta.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16541747094039)CAUSA:**

![Imagem 6: Produto com endereço X de picking vinculado no produto e o estoque está no endereço Y de picking sem vinculo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16541747089431)  Produto com endereço X de picking vinculado no produto e o estoque está no endereço Y de picking sem vinculo com o produto.

![Imagem 7: Produto com mais de uma unidade armazenada no mesmo endereço picking.](https://ajuda.sankhya.com.br/hc/article_attachments/16541747091479) Produto com mais de uma unidade armazenada no mesmo endereço picking.
