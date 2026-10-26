---
id: "360044237413"
titulo: "O produto XXX não pertence ao pedido/nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044237413-O-produto-XXX-n%C3%A3o-pertence-ao-pedido-nota"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:16Z"
rotulos: ["#RevisadoWellington", "Produtos", "Configuração", "Cadastro", "Erro ocorre por produtos com referências duplicadas", "Produto não pertence ao pedido/nota", "Verifique e ajuste referências ou códigos de barras", "Erro"]
---

# O produto XXX não pertence ao pedido/nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16422030478999) MENSAGEM:**

O produto XXX não pertence ao pedido/nota.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16422030482967) SITUAÇÃO:**

Ao tentar executar uma tarefa no coletor a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16422030485271) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 4: Acesse Configurações » Cadastros » Produtos » Produtos , aba Geral , campo "Referência"](https://ajuda.sankhya.com.br/hc/article_attachments/16422054443671) Acesse Configurações » Cadastros » Produtos » Produtos, aba **Geral**, campo **"Referência"**

ou

Configurações » Cadastros » Produtos » Produtos, aba **Unidade Alternativa**, campo **"Código de Barras da Unidade Alternativa".**

Identifique se existe mais de um produto que possui a mesma referência ou código de barras e faça o ajuste para que a referência entre ambos seja diferente.

![Imagem 5: Após os ajustes, execute a chamada da tarefa novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16422054446103) Após os ajustes, execute a chamada da tarefa novamente.

**![Imagem 6: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/16422054448023) CAUSA**

Ocorre quando dois ou mais produtos possuem o mesmo código de referência ou código de barras, o sistema busca pelo produto de menor código de cadastro no sistema e se no lançamento for o outro produto, ocorre a mensagem.

Exemplo:

Produtos:
Código: 10 - Referencia: AN13911
Código: 33 - Referencia: AN13911

Se o produto 33 estiver no lançamento da execução da tarefa, apresentará a mensagem, pois o sistema tentará buscar o produto de código 10 (dez).
