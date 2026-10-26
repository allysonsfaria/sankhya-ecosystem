---
id: "14437003887127"
titulo: "Data de Entrada/Saída deve ser maior ou igual a data de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14437003887127-Data-de-Entrada-Sa%C3%ADda-deve-ser-maior-ou-igual-a-data-de-Negocia%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:47Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Financeiro", "CORE_E05555", "Data Entrada/Saída menor que Negociação", "Parâmetro habilitado exige data correta", "Preencher Data Entrada/Saída corretamente", "Erro"]
---

# Data de Entrada/Saída deve ser maior ou igual a data de Negociação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16276810626711) MENSAGEM:**

[CORE\_E05555]: Data de Entrada/Saída deve ser maior ou igual a data de Negociação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16276767592855) SOLUÇÃO:**

![Imagem 3: Quando o parâmetro "Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI" estiver habilitado, os lançamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/16970193893783) Quando o parâmetro **"Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI"** estiver habilitado, os lançamentos realizados na Movimentação Financeira e nas Centrais de Nota terão como obrigatório o preenchimento do campo **"Dt. Entrada/Saída"**.

![Imagem 4: Quando o parâmetro "Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI" estiver habilitado, os lançamentos…](https://ajuda.sankhya.com.br/hc/article_attachments/14437007062551)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16276810646167)OBSERVAÇÃO:**

Ao tentar confirmar um registro em que a Data de Entrada/Saída seja menor do que a Data de Negociação, o sistema emitirá a seguinte mensagem citada anteriormente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16276810635799) CAUSA:**

Ocorre sempre que o parâmetro **"Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI"** estiver habilitado e a Data de Entrada/Saída seja menor do que a Data de Negociação.
