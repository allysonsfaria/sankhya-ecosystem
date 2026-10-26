---
id: "18863018746263"
titulo: "O valor do campo orig (origem da mercadoria: 0 - Nacional 1 - Estrangeira - Importação direta 2 - Estrangeira - Adquirida no mercado interno) informado não é valido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18863018746263-O-valor-do-campo-orig-origem-da-mercadoria-0-Nacional-1-Estrangeira-Importa%C3%A7%C3%A3o-direta-2-Estrangeira-Adquirida-no-mercado-interno-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:52:02Z"
rotulos: ["CORE_E04895", "Produtos", "Configuração", "Fiscal", "NF-e", "XML", "Erro de Classificação da Origem do Produto"]
---

# O valor do campo orig (origem da mercadoria: 0 - Nacional 1 - Estrangeira - Importação direta 2 - Estrangeira - Adquirida no mercado interno) informado não é valido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18863010271255) **MENSAGEM:**

[CORE\_E04895] O valor do campo orig (origem da mercadoria: 0 - Nacional
1 - Estrangeira - Importação direta
2 - Estrangeira - Adquirida no mercado interno) informado não é
valido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18863018720663)SOLUÇÃO:**

Pegue o XML para conferência no botão "NF-e" opção "Gerar XML da NF-e em arquivo para conferência" no portal e após baixado precisa localizar o produto que conta com a Tag <orig> vazia.

Após localizar o produto, basta entrar no cadastro do mesmo (Tela de Produtos) e classificar o campo "Origem do Produto", localizado na aba "Geral" conforme desejado.

![Imagem 3: Após localizar o produto, basta entrar no cadastro do mesmo (Tela de Produtos) e classificar o campo "Origem do…](https://ajuda.sankhya.com.br/hc/article_attachments/19142036381975)

Após a alteração, redigite algo na nota e gere o lote novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18863002208407)CAUSA:**

Ocorre quando não é classificado a origem do produto no cadastro, pois no XML a tag <orig> fica vazia e apresenta a mensagem de erro.

![Imagem 5: Ocorre quando não é classificado a origem do produto no cadastro, pois no XML a tag <orig> fica vazia e apresenta a…](https://ajuda.sankhya.com.br/hc/article_attachments/19142057235735)
