---
id: "26354593831703"
titulo: "Vendas por vendedor no gerente online não apresenta as vendas para uma determinada TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26354593831703-Vendas-por-vendedor-no-gerente-online-n%C3%A3o-apresenta-as-vendas-para-uma-determinada-TOP"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:42:30Z"
rotulos: ["Configuração", "Relatórios", "Portal de Vendas", "TOP", "Vendas", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Vendas por vendedor no gerente online", "não apresenta as vendas para uma determinada TOP."]
---

# Vendas por vendedor no gerente online não apresenta as vendas para uma determinada TOP

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26429477770007)  **SITUAÇÃO:**

Mesmo a top de vendas estando configurada como apoio a decisão 'Vendas', não estão sendo apresentados os registros das vendas no Dash **"Vendas por vendedor"**.

![Imagem 2: Mesmo a top de vendas estando configurada como apoio a decisão 'Vendas', não estão sendo apresentados os registros das…](https://ajuda.sankhya.com.br/hc/article_attachments/26354593825303)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26354593826199)SOLUÇÃO:**

Esse problema ocorre quando a top de vendas está marcada como bonificação.

Nesse caso, desmarque a opção **"Bonificação"**.

![Imagem 4: Nesse caso, desmarque a opção "Bonificação" .](https://ajuda.sankhya.com.br/hc/article_attachments/26354572613015)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26354572614551)CAUSA:**

Na query de Vendas por vendedor no gerente online tem uma condição para o campo de 'TOTAL',  'CASE WHEN TGFTOP.BONIFICACAO = 'S' THEN 0 ELSE 1 END \* TGFTOP.GOLDEV). Esse campo na TOP é histórico, quando é alterado só surgirá efeito para os novos lançamentos.
