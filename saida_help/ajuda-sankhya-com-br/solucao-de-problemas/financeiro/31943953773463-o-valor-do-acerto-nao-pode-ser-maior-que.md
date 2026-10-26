---
id: "31943953773463"
titulo: "O valor do acerto não pode ser maior que o total das Despesas ou Receitas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31943953773463-O-valor-do-acerto-n%C3%A3o-pode-ser-maior-que-o-total-das-Despesas-ou-Receitas"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:32:12Z"
rotulos: ["Configuração", "Moeda", "Movimentação Financeira", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "valor do acerto não pode ser maior", "que o total das Despesas ou Receitas", "Vlr. Moeda Atual", "Erro"]
---

# O valor do acerto não pode ser maior que o total das Despesas ou Receitas

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31943953760535) **MENSAGEM:**

O valor do acerto não pode ser maior que o total das Despesas ou Receitas

![Imagem 2: O valor do acerto não pode ser maior que o total das Despesas ou Receitas](https://ajuda.sankhya.com.br/hc/article_attachments/32640025701783)

**![Imagem 3: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32640011402263) SITUAÇÃO:**

Na tela **"Compensação Financeira"** (Caminho: Financeiro » Rotinas » Compensação Financeira) ao realizar uma compensação de lançamentos que possuem valor de moeda, no pop-up **"Acertar"** é apresentado a mensagem acima.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31943953761687)SOLUÇÃO:**

Essa mensagem é exibida ao informar, no campo **"Vlr. Moeda Atual"** do pop-up Acertar, da tela Compensação Financeira, um valor de moeda que não corresponde à moeda configurada no campo **"Data Cotação"**.

Para corrigir, verifique qual é a data correta correspondente ao valor de moeda inserido e informe essa data no campo **"Data Cotação"**.

Para consultar a data e o valor corretos da moeda, acesse a tela **"Valores de Moeda"** (Caminho: Configurações » Cadastros » Valores de Moedas) e localize a moeda correspondente aos lançamentos envolvidos.

![Imagem 5: Para consultar a data e o valor corretos da moeda, acesse a tela "Valores de Moeda" (Caminho: Configurações » Cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/32640025707287)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31943931619863)CAUSA:**

O sistema valida a **data informada** no campo **"Data de Cotação"** juntamente com o valor inserido no campo **"Vlr. Moeda Atual"**, conforme o cadastro existente na tela **"Valores de Moeda"**.

Caso seja informado um **valor divergente** do registrado para a data selecionada, a **mensagem de alerta será exibida**.
