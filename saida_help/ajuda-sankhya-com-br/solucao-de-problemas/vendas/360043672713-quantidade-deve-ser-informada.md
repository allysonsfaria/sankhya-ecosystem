---
id: "360043672713"
titulo: "Quantidade deve ser informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043672713-Quantidade-deve-ser-informada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:48Z"
rotulos: ["ERRONF", "Configuração", "TOP", "Estoque", "Preferências", "Quantidade deve ser informada", "Ajustar parâmetro \"TOPQTDZERO\" para aceitar zero", "Sem ajuste mensagem é apresentada para quantidade = 0", "Erro"]
---

# Quantidade deve ser informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16118693294743) MENSAGEM:**

Quantidade deve ser informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16118693297303) SOLUÇÃO:**

![Imagem 3: Para lançamentos onde o campo quantidade deverá ser lançado zerado, por exemplo, notas de complemento de imposto,…](https://ajuda.sankhya.com.br/hc/article_attachments/16118706275607) Para lançamentos onde o campo quantidade deverá ser lançado zerado, por exemplo, notas de complemento de imposto, necessário ajustar o parâmetro abaixo:

**(2)** Tela **"Preferências"** (Caminho de acesso: Configurações » Avançado)

**(2)** Chave **"TOPQTDZERO - TOP para aceitar Qtd. igual a zero"**, informe no campo **"Texto"** o código do Tipo de Operação utilizado no lançamento.

![Imagem 4: (2) Chave "TOPQTDZERO - TOP para aceitar Qtd. igual a zero" , informe no campo "Texto" o código do Tipo de Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/14627826818199)

![Imagem 5: Ajustado o parâmetro acima será possível incluir itens com quantidade = 0.](https://ajuda.sankhya.com.br/hc/article_attachments/16118693314711) Ajustado o parâmetro acima será possível incluir itens com quantidade = 0.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16118693317399) CAUSA:**

Ao realizar lançamentos informando itens com o campo quantidade = 0, sem a devida parametrização do parâmetro TOPQTDZERO, será apresentada a mensagem.
