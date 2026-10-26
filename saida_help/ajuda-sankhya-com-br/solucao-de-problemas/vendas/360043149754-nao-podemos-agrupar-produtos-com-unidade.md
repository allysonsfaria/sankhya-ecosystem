---
id: "360043149754"
titulo: "Não podemos agrupar produtos com unidades diferentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043149754-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:01Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Financeiro", "Unidades diferentes não podem ser agrupadas", "Unidades distintas para o mesmo produto", "Uniformize a unidade nos pedidos", "Erro"]
---

# Não podemos agrupar produtos com unidades diferentes

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16120986426647) MENSAGEM:**

Não podemos agrupar produtos com unidades diferentes.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120982448791) SOLUÇÃO:**

![Imagem 3: Identifique dentre os pedidos que irão originar o faturamento, quais os produtos encontram-se repetidos e possuem…](https://ajuda.sankhya.com.br/hc/article_attachments/16120986429463) Identifique dentre os pedidos que irão originar o faturamento, quais os produtos encontram-se repetidos e possuem Unidades diferentes.

(1)** Exemplo:**

**(2)**Pedido Número 10

**(3)** Produto A » Unidade CX (Caixa)

**(3)** Produto B » Unidade PT (Pacote)

**(3)** **Produto E » Unidade KG (Kilo)**

**(2)**Pedido Número 11

**(3)** Produto A » Unidade CX (Caixa)

**(3)** Produto B » Unidade PT (Pacote)

**(3)** **Produto E » Unidade CX (Caixa)**

![Imagem 4: Ao selecionar ambos os pedidos e realizar o faturamento, o erro será reportado, pois o Produto E foi lançado como…](https://ajuda.sankhya.com.br/hc/article_attachments/16120986436631) Ao selecionar ambos os pedidos e realizar o faturamento, o erro será reportado, pois o **Produto E** foi lançado como **Unidade KG** e em outro momento com **Unidade CX**.

**(2)**Para solucionar o caso, ajuste um dos pedidos igualando as informações de Unidade.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120986438551) CAUSA:**

Ocorre quando ao realizar faturamento agrupando mais de 1 pedido, onde exista para o mesmo Cód.Produto lançamentos com Unidades diferentes.
