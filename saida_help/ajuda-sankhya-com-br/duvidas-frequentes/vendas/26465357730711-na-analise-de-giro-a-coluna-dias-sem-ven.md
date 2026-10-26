---
id: "26465357730711"
titulo: "Na análise de giro a coluna dias sem vendas apresenta uma quantidade de X dias, sendo que deveria ser X dias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26465357730711-Na-an%C3%A1lise-de-giro-a-coluna-dias-sem-vendas-apresenta-uma-quantidade-de-X-dias-sendo-que-deveria-ser-X-dias"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:42:04Z"
rotulos: ["Produtos", "Configuração", "análise de giro", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "coluna dias sem vendas apresenta uma quantidade de X dias", "sendo que deveria ser X dias"]
---

# Na análise de giro a coluna dias sem vendas apresenta uma quantidade de X dias, sendo que deveria ser X dias

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26465342097047) **MENSAGEM:**

Na análise de giro a coluna dias sem vendas apresenta uma quantidade de X dias , sendo que deveria ser X dias.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26465342098967)SOLUÇÃO:**

Acesse a tela **"Tipos de Operação - TOP",** na aba **"Geral",** configure corretamente o campo **"Atualizar Última Compra"**, da Top de compras e o campo **"Atualizar Última Venda"**, da Top de Venda.

![Imagem 3: Acesse a tela "Tipos de Operação - TOP", na aba "Geral", configure corretamente o campo "Atualizar Última Compra" , da…](https://ajuda.sankhya.com.br/hc/article_attachments/26505968193687)

**(1)** **Se houver vendas e compras para o produto:** conta os dias da última venda até a data atual;

**(1)** **Se não houver vendas, mas existir compras para o produto:** conta os dias da última compra até a data atual para popular o campo;

**(1)** **Se não houver nem compra nem venda:** conta os dias a partir da última data de alteração do cadastro do produto até a data atual para popular o campo.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26465342100631)CAUSA:**

Esse erro ocorre caso a top de vendas ou de compras não estejam com os campos Atualizar Última Venda ou Atualizar Última Compras configurados corretamente. Lembrando que esse campo é histórico e precisa ser feita a consolidação de giro para que a tabela 'TGFUVC' se atualizada corretamente.
