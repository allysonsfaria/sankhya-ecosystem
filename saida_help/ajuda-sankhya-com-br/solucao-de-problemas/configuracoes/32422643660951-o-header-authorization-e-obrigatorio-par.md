---
id: "32422643660951"
titulo: "O Header Authorization é obrigatório para esta requisição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32422643660951-O-Header-Authorization-%C3%A9-obrigat%C3%B3rio-para-esta-requisi%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:31:19Z"
rotulos: ["Configuração", "Autenticação", "Passos para resolver", "Razão do erro", "Detalhe do erro", "requisição", "header", "Header Authorization", "Authorization", "api", "login api", "Erro", "Case Sensitive"]
---

# O Header Authorization é obrigatório para esta requisição

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32422643642007) **MENSAGEM:**

O Header Authorization é obrigatório para esta requisição

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32422643642519)SOLUÇÃO:**

Verifique a URL de login utilizada no momento da autenticação.

A API da Sankhya é sensível a letras maiúsculas e minúsculas (case sensitive). Portanto, a palavra "**login**" no endpoint deve obrigatoriamente ser informada em letras minúsculas.
Exemplo correto:

```
https://api.sandbox.sankhya.com.br/login
```

O uso de "**Login**" (com "L" maiúsculo) resultará em falha de autenticação e erro no Header Authorization.

Após o ajuste da URL com a grafia correta, a autenticação ocorrerá normalmente.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32422643644439)CAUSA:**

A API da Sankhya diferencia maiúsculas de minúsculas na URL (case sensitive). O uso incorreto de letras maiúsculas na palavra "**login**" na URL de autenticação impede o correto processamento da requisição e ocasiona o erro de Header Authorization, mesmo quando AppKey e Token estão devidamente configurados.
