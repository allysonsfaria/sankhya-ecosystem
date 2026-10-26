---
id: "360043178154"
titulo: "Data de Faturamento deve ser maior ou igual a data de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178154-Data-de-Faturamento-deve-ser-maior-ou-igual-a-data-de-Negocia%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-08T14:38:13Z"
rotulos: ["#criadoRoger", "#criadoUeder", "Configuração", "NF-e", "Movimentação Financeira", "Financeiro", "CORE_E01846", "Faturamento menor que Negociação", "Ajustar datas ou habilitar parâmetro", "Data de Faturamento inadequada", "Erro"]
---

# Data de Faturamento deve ser maior ou igual a data de Negociação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16165048400407) MENSAGEM:**

[CORE\_E01846] Data de Faturamento deve ser maior ou igual a data de Negociação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165066956183) SITUAÇÃO:**

Ao tentar efetuar o faturamento de uma Nota, a seguinte mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165048410263) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Verifique a data de Faturamento e se estiver menor que a data de Negociação, deverá ser ajustada.](https://ajuda.sankhya.com.br/hc/article_attachments/16165066965783) Verifique a data de Faturamento e se estiver menor que a data de Negociação, deverá ser ajustada.

Caso realmente se faz necessário que o Faturamento seja menor que a data de Negociação, considere ligar o parâmetro "**PERDTFATANDTNEG - Permitir Dt. Faturamento anterior Dt. Negociação?"**

![Imagem 5: Caso realmente se faz necessário que o Faturamento seja menor que a data de Negociação, considere ligar o parâmetro "…](https://ajuda.sankhya.com.br/hc/article_attachments/14712981951127)

![Imagem 6: Após os ajustes, tente faturar novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16165048417431) Após os ajustes, tente faturar novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16165048420375) CAUSA:**

Ocorre quando a data de Faturamento é menor que a data de negociação, caso o parâmetro esteja desligado, será apresentada a mensagem impeditiva.
