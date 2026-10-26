---
id: "360044530153"
titulo: "Ao processar a matriz de Análise de Giro o campo Sugestão de Compra não é atualizado levando em consideração as compras pendentes. "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044530153-Ao-processar-a-matriz-de-An%C3%A1lise-de-Giro-o-campo-Sugest%C3%A3o-de-Compra-n%C3%A3o-%C3%A9-atualizado-levando-em-considera%C3%A7%C3%A3o-as-compras-pendentes"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T15:55:35Z"
rotulos: ["Produtos", "Configuração", "análise de giro", "Sugestão de Compra", "Estoque", "Atualização da Sugestão de Compra"]
---

# Ao processar a matriz de Análise de Giro o campo Sugestão de Compra não é atualizado levando em consideração as compras pendentes. 

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18796205361943) SOLUÇÃO:**

Considere as seguintes regras aplicadas para que o campo "Sugestão de Compra" seja preenchido:

**Sug.Compra:** Apresenta a sugestão de compra baseada no Estoque Mínimo do produto, ou seja:

"Sug.Compra" = ("Estoque Min." \* "% Acréscimo na Sugestão de Compras") – "Estoque" – "Compra Pendente" + "Venda Pendente".

Caso esse cálculo não esteja sendo realizado com os valores esperados, considere avaliar os filtros inseridos para "Compras Pendentes" e "Vendas Pendentes":

![Imagem 2: Caso esse cálculo não esteja sendo realizado com os valores esperados, considere avaliar os filtros inseridos para…](https://ajuda.sankhya.com.br/hc/article_attachments/18796166531223)

**Observação:** Quando não houver nenhum filtro para compras e vendas pendentes, por uma questão de melhoria de performance, o sistema só irá considerar as compras e vendas pendentes dos últimos 180 dias.
