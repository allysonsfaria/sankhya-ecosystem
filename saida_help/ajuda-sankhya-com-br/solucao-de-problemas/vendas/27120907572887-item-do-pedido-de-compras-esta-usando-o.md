---
id: "27120907572887"
titulo: "Item do Pedido de compras está usando o multiplicador de valor da unidade alternativa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27120907572887-Item-do-Pedido-de-compras-est%C3%A1-usando-o-multiplicador-de-valor-da-unidade-alternativa"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-27T16:12:06Z"
rotulos: ["Produtos", "Configuração", "Pedido de Compra", "Unidade Alternativa", "Parâmetro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Item do Pedido de compras está usando o multiplicador de valor da unidade alternativa"]
---

# Item do Pedido de compras está usando o multiplicador de valor da unidade alternativa

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/27120905264663) **MENSAGEM:**

Item do Pedido de compras está usando o multiplicador de valor da unidade alternativa.

![Imagem 2: Item do Pedido de compras está usando o multiplicador de valor da unidade alternativa.](https://ajuda.sankhya.com.br/hc/article_attachments/27120905266071)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27120905267479)SOLUÇÃO:**

Para que não considere Multiplicador de valor para pedido/nota e devoluções de compras é necessário habilitar o parâmetro **"MULTVLRSOVENDAS"**, esse parâmetro determina que só será usado o multiplicador para notas de vendas.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27120905269527)CAUSA:**

Quando o parâmetro MULTVLRSOVENDAS está desligado, o sistema utiliza o multiplicador para valor da aba **"Unidade alternativa"** do cadastro do produto para pedidos/notas/devolução de compras.
