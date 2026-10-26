---
id: "360043421213"
titulo: "A quantidade entregue não pode ser maior que a quantidade negociada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043421213-A-quantidade-entregue-n%C3%A3o-pode-ser-maior-que-a-quantidade-negociada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-27T19:40:22Z"
rotulos: ["#PUBLIFER", "CORE_E01998", "Configuração", "Faturamento", "Nota Fiscal", "TOP", "Estoque", "Quantidade excedida", "Erro durante o faturamento", "Ajustar configurações de operação", "Erro"]
---

# A quantidade entregue não pode ser maior que a quantidade negociada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117613245207) MENSAGEM:**

[CORE\_E01998] A quantidade entregue não pode ser maior que a quantidade negociada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117613248535) SITUAÇÃO:**

Mensagem apresentada no faturamento de pedido/nota.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117613251223) SOLUÇÃO:**

Para solução seguir os passos:

![Imagem 4: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: comercial » Arquivo » Cadastros) , aba "Estoque" , opção…](https://ajuda.sankhya.com.br/hc/article_attachments/16117613253399) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: comercial » Arquivo » Cadastros), aba **"Estoque"**, opção **"Aceitar faturar quantidade maior que a origem?"**: marcado

![Imagem 5: Acesse a tela " Tipos de Operação - TOP " (Caminho de acesso: comercial » Arquivo » Cadastros) , aba "Estoque" , opção…](https://ajuda.sankhya.com.br/hc/article_attachments/14608557898391)

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17804167841815) IMPORTANTE:**

Além da marcação citada, é necessário que a opção **"Exigir Pedido"**, aba **"Geral"** esteja marcada como: **"Exige algum item"** ou **"Não Exigir".**

![Imagem 7: Além da marcação citada, é necessário que a opção "Exigir Pedido" , aba "Geral" esteja marcada como: "Exige algum item"…](https://ajuda.sankhya.com.br/hc/article_attachments/14608669268119)

![Imagem 8: Realizados os ajustes, exclua o lançamento da nota destino e refaça o faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16117620718231) Realizados os ajustes, exclua o lançamento da nota destino e refaça o faturamento.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16117613265431) CAUSA:**

Ao tentar realizar o faturamento no qual a quantidade de determinado item da nota/pedido de destino é maior que a quantidade da nota/pedido de origem, a mensagem será retornada.
