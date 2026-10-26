---
id: "27537922347287"
titulo: "Campo Pedido foi impresso não foi marcado depois de imprimir um pedido nos portais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27537922347287-Campo-Pedido-foi-impresso-n%C3%A3o-foi-marcado-depois-de-imprimir-um-pedido-nos-portais"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:39:33Z"
rotulos: ["Configuração", "Impressão", "Portal de Vendas", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Campo Pedido foi impresso não foi marcado depois de imprimir um pedido nos portais", "Venda Mais", "REGIMPPED"]
---

# Campo Pedido foi impresso não foi marcado depois de imprimir um pedido nos portais

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27545516020887) **SITUAÇÃO:**

O campo **"Pedido foi impresso"** não foi marcado depois de imprimir um pedido nos portais.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27537922326551)SOLUÇÃO:**

Para que o campo seja marcado como **'S',** ligue o parâmetro **"REGIMPPED"**

Depois de marcado e impresso o pedido, o sistema registra a informação na tabela TGFACT e a linha do pedido nos portais fica com a cor azul.

![Imagem 3: Depois de marcado e impresso o pedido, o sistema registra a informação na tabela TGFACT e a linha do pedido nos portais…](https://ajuda.sankhya.com.br/hc/article_attachments/27537892858263)

![Imagem 4: Depois de marcado e impresso o pedido, o sistema registra a informação na tabela TGFACT e a linha do pedido nos portais…](https://ajuda.sankhya.com.br/hc/article_attachments/27537922331415)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27537892862999)CAUSA:**

O campo só registra a informação do campo Pedido foi impresso quando o parâmetro REGIMPPED está ligado.
