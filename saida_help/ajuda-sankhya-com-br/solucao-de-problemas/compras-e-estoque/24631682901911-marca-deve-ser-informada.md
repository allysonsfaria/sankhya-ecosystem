---
id: "24631682901911"
titulo: "Marca deve ser informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24631682901911-Marca-deve-ser-informada"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-20T22:31:00Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Preferências", "CORE_E03853", "Preencher campo \"Marca\" em \"Produtos\"", "Parâmetro CFPSMARCAREFREP desligado", "Marca não informada", "Erro"]
---

# Marca deve ser informada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24631666334871) **MENSAGEM:**

[CORE\_E03853] Marca deve ser informada

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24631666338199) **SOLUÇÃO:**

![Imagem 3: Acesse a tela "Produtos" (Caminho: Configurações » Cadastros » Produtos » Produtos) , vá até a aba "Geral" e preencha o…](https://ajuda.sankhya.com.br/hc/article_attachments/24631682886551) Acesse a tela **"Produtos"**(Caminho: Configurações » Cadastros » Produtos » Produtos), vá até a aba **"Geral"**e preencha o campo **"Marca".**

Na tela **"Preferências"**(Caminho: Configurações » Avançado » Preferências) verifique o parâmetro **"CFPSMARCAREFREP - Uso interno tela Produto/Serviço".** Caso o parâmetro esteja desligado o preenchimento será obrigatório.

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24631682892183)**CAUSA:**

O erro é apresentado ao tentar cadastrar um produto, não tendo preenchido o campo Marca e com o parâmetro CFPSMARCAREFREP desligado.
