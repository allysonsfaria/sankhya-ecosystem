---
id: "26509445115287"
titulo: "Pedidos de Compra/Venda pendentes não estão sendo considerado na Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26509445115287-Pedidos-de-Compra-Venda-pendentes-n%C3%A3o-est%C3%A3o-sendo-considerado-na-An%C3%A1lise-de-Giro"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-08-11T01:19:31Z"
rotulos: ["Configuração", "Análise de Giro", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Pedido de venda pendente:", "Pedido de Compra pendente", "Pedidos de Compra/Venda pendentes", "não estão sendo considerado na Análise de Giro", "Pedidos de Compra", "Artigo atualizado KCS", "CVE - KCS", "Plataforma - KCS", "Pedidos de Venda"]
---

# Pedidos de Compra/Venda pendentes não estão sendo considerado na Análise de Giro

**(1)** Ao processar matriz, pedidos de compra e pedidos de venda não são levados para análise de giro, impactando no calculo de vários campos, inclusive nas sugestões de compra.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26509445087767)SOLUÇÃO:**

**(2)** **Pedido de venda pendente:**

Para que um pedido de venda seja considerado, ele deve atender as seguintes regras:

![Imagem 2: Deve estar confirmado;](https://ajuda.sankhya.com.br/hc/article_attachments/26509429416855) Deve estar confirmado;

![Imagem 3: Deve estar pendente (ainda não foi faturado);](https://ajuda.sankhya.com.br/hc/article_attachments/26509445092375) Deve estar pendente (ainda não foi faturado);

![Imagem 4: A TOP usada seja do tipo de movimento 'P - Pedido de Venda';](https://ajuda.sankhya.com.br/hc/article_attachments/26509429419543) A TOP usada seja do tipo de movimento 'P - Pedido de Venda';

![Imagem 5: A TOP usada não pode reservar estoque. Isso ocorre pois os cálculo da sugestão de compra consideram o estoque…](https://ajuda.sankhya.com.br/hc/article_attachments/26509429420695) A TOP usada **não** pode **reservar** estoque. Isso ocorre pois os cálculo da sugestão de compra consideram o estoque disponível, ou seja, já abatendo a reserva. Então, se o sistema considerasse também pedidos que reserva, levaria de forma duplicada para a sugestão;

![Imagem 6: Dentro das configurações da Matriz, na análise de giro, deve estar desmarcada a configuração "Desconsiderar pedidos…](https://ajuda.sankhya.com.br/hc/article_attachments/26509445098903) Dentro das configurações da Matriz, na análise de giro, deve estar desmarcada a configuração **"Desconsiderar pedidos pendentes na sugestão de Compra**".

**(2)** **Pedido de Compra pendente:**

Para que um pedido de compra seja considerado, ele deve atender as seguintes regras:

![Imagem 7: Deve estar confirmado;](https://ajuda.sankhya.com.br/hc/article_attachments/26509429416855) Deve estar confirmado;

![Imagem 8: Deve estar pendente (ainda não foi faturado);](https://ajuda.sankhya.com.br/hc/article_attachments/26509445092375) Deve estar pendente (ainda não foi faturado);

![Imagem 9: A TOP usada seja do tipo de movimento 'O - Pedido de Compra';](https://ajuda.sankhya.com.br/hc/article_attachments/26509429419543) A TOP usada seja do tipo de movimento 'O - Pedido de Compra';

![Imagem 10: Dentro das configurações da Matriz, na análise de giro, deve estar desmarcada a configuração "Desconsiderar pedidos…](https://ajuda.sankhya.com.br/hc/article_attachments/26509429420695) Dentro das configurações da Matriz, na análise de giro, deve estar desmarcada a configuração **"Desconsiderar pedidos pendentes na sugestão de Compra**".

![Imagem 11: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/26509445101591)**Importante:**

**(1)** De forma nativa, o sistema considera apenas pedidos com data de negociação anteriores a 6 meses, por questão de performance. Caso seja necessário aumentar esse período, inclua os filtros abaixo nas configurações da matriz de giro.

![Imagem 12: (1) De forma nativa, o sistema considera apenas pedidos com data de negociação anteriores a 6 meses, por questão de…](https://ajuda.sankhya.com.br/hc/article_attachments/26617015641111)

Filtro Pedido de venda pendente:

```
CabecalhoNota->TIPMOV = 'P' AND CabecalhoNota->DTNEG >= (GETDATE() - 365)
```

Filtro Pedido de compra pendente:

```
CabecalhoNota->TIPMOV = 'O' AND CabecalhoNota->DTNEG >= (GETDATE() - 365)
```

**(1)** Se mesmo assim os pedidos não forem levados, verifique os filtros da análise de giro e processe a matriz após qualquer alteração.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26509445107607)CAUSA:**

Alguns requisitos são necessários para que o sistema leve pedidos pendentes para análise de giro, impactando diretamente no cálculo da sugestão de compra.
