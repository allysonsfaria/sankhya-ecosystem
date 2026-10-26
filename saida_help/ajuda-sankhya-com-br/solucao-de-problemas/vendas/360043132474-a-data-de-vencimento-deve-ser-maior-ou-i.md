---
id: "360043132474"
titulo: "A data de vencimento deve ser maior ou igual a data de negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043132474-A-data-de-vencimento-deve-ser-maior-ou-igual-a-data-de-negocia%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-30T12:25:49Z"
rotulos: ["#RevisadoJR", "CORE_E02204", "CORE_E02805", "CORE_E03476", "OS-1226918", "Configuração", "Movimentação Financeira", "Financeiro", "Vencimento Antecipado", "Correção de Configuração", "Vencimento Fixo", "Erro"]
---

# A data de vencimento deve ser maior ou igual a data de negociação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16145820257559) MENSAGEM:**

[CORE\_E02204] A data de vencimento deve ser maior ou igual a data de negociação.

[CORE\_E02805] A data de vencimento deve ser maior ou igual a data de negociação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145820259607) SITUAÇÃO:**

Ao tentar efetuar o faturamento de um pedido ou alterar um pedido já confirmado, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145843755927) SOLUÇÃO:**

![Imagem 4: Acesse a tela Tipos de Negociação ( Comercial » Arquivo » Cadastros » Tipos de Negociação), aba parcelas, Campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16145820275607) Acesse a tela **Tipos de Negociação** (Comercial » Arquivo » Cadastros » Tipos de Negociação), aba parcelas, Campo **"Vencto. Fixo"-** data de Vencimento Fixo. Aqui encontra-se uma data de vencimento fixo. Verifique com o setor financeiro e se for o caso, limpe o valor neste campo. Salve a alteração e, posteriormente, fature o pedido novamente.

**IMPORTANTE:**

A data informada no campo **"Vencto Fixo"** será usada como a data de vencimento em todas as notas que forem lançadas utilizando o tipo de negociação configurado, desconsiderando assim as configurações para cálculo do vencimento.

![Imagem 5: A data informada no campo "Vencto Fixo" será usada como a data de vencimento em todas as notas que forem lançadas…](https://ajuda.sankhya.com.br/hc/article_attachments/14691133367319)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16145843766807) CAUSA:**

Esta mensagem ocorre quando se define um vencimento fixo, através do Tipo de Negociação. E o vencimento dos títulos já tenha sido calculados na nota/pedido e caso ocorra alguma alteração ou faturamento, no qual o sistema irá refazer o financeiro.
