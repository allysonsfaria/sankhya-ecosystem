---
id: "14011567179799"
titulo: "Análise de Giro: Não está trazendo as compras pendentes anteriores a 6 meses"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14011567179799-An%C3%A1lise-de-Giro-N%C3%A3o-est%C3%A1-trazendo-as-compras-pendentes-anteriores-a-6-meses"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:59:41Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "Análise de Giro", "Estoque", "layout antigo", "Problema de Compras Pendentes Anteriores a 6 Meses na Análise de Giro"]
---

# Análise de Giro: Não está trazendo as compras pendentes anteriores a 6 meses

**![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/16860137952151) SITUAÇÃO:**

Ao processar uma matriz de análise de giro, com determinados produtos na análise não estão sendo apresentadas as compras pendentes que estes produtos possuem. Se tratam de pedidos confirmados, que não reservam estoque.

**![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/16860137954199)SOLUÇÃO:**

**Nota:** Para clientes que utilizam o Layout Antigo (Flex):

Crie um filtro para buscar os pedidos, com data negociada acima de 6 meses.

Filtro: **CabecalhoNota->DTNEG >= sysdate -365**

![Imagem 3](https://ajuda.sankhya.com.br/hc/article_attachments/14011044066455)

**![Imagem 4](https://ajuda.sankhya.com.br/hc/article_attachments/16860137963799)CAUSA:**

No layout (flex), o sistema processa apenas os pedidos dos últimos 6 meses. Sendo assim, esta falha vai ocorrer sempre que os pedidos tiverem data de negociação superior a 6 meses da data atual.

Já diferente do layout HTML5 (novo), em que o mesmo busca as compras pendentes, independente da data de negociação.
