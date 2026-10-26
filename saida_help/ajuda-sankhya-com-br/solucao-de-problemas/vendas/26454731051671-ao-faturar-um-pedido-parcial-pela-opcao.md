---
id: "26454731051671"
titulo: "Ao faturar um pedido parcial pela opção  faturar pelo estoque, o restante do pedido está ficando como não pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26454731051671-Ao-faturar-um-pedido-parcial-pela-op%C3%A7%C3%A3o-faturar-pelo-estoque-o-restante-do-pedido-est%C3%A1-ficando-como-n%C3%A3o-pendente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:42:06Z"
rotulos: ["Produtos", "Configuração", "Faturamento", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "restante do pedido está ficando como não pendente", "faturar um pedido parcial", "faturar pelo estoque"]
---

# Ao faturar um pedido parcial pela opção  faturar pelo estoque, o restante do pedido está ficando como não pendente

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26456188084503) **SITUAÇÃO:**

Ao faturar um pedido parcial pela opção faturar pelo estoque, o restante do pedido está ficando como não pendente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26454716743319)SOLUÇÃO:**

Isso é um comportamento do sistema. Para deixar o restante do pedido como pendente, use a opção de faturar pelo estoque deixando pendente.

![Imagem 3: Isso é um comportamento do sistema. Para deixar o restante do pedido como pendente, use a opção de faturar pelo estoque…](https://ajuda.sankhya.com.br/hc/article_attachments/26454716753431)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26454731048215)CAUSA:**

Essa particularidade é quando usa a opção de faturar pelo estoque, na qual tem casos que só serão faturados os itens que realmente tem no estoque. Essa opção não olha os parâmetros **FATCORTITNS** e **ZERARQTDCONF,** pois temos a opção de Faturar pelo estoque deixando pendente que resolve o problema.
