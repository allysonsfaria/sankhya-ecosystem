---
id: "31299212340375"
titulo: "Erro toFixed() digits argument must be between 0 and 100"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31299212340375-Erro-toFixed-digits-argument-must-be-between-0-and-100"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:33:20Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "must be between 0 and 100", "toFixed() digits argument", "Erro", "Decimais"]
---

# Erro toFixed() digits argument must be between 0 and 100

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31299212326295) **MENSAGEM:**

toFixed() digits argument must be between 0 and 100

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31940145752215) SITUAÇÃO:**

Ao acessar a tela **"Consulta de produtos"** é apresentada a mensagem de erro citada acima.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31299212332567)SOLUÇÃO:**

Quando a tela  Consulta de produtos é acionada e essa mensagem é apresentada, significa que  um dos produtos da base possui o campo **"Decimais para quantidade"** (Aba Medidas e Estoque) com valor **superior a 100.** 
Assim, analise e ajuste o campo de todos os produtos que estejam com esta configuração.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31299212333079)CAUSA:**

O erro acontece quando um dos produtos da base possui um valor superior a 100 no campo Decimais para quantidade.
