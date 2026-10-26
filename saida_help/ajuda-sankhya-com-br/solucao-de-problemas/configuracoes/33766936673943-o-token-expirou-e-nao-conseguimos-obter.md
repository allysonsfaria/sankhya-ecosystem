---
id: "33766936673943"
titulo: "O token expirou e não conseguimos obter um novo, talvez a API tenha sido revogada. Sugerimos que faça uma nova autenticação. Código: 400"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33766936673943-O-token-expirou-e-n%C3%A3o-conseguimos-obter-um-novo-talvez-a-API-tenha-sido-revogada-Sugerimos-que-fa%C3%A7a-uma-nova-autentica%C3%A7%C3%A3o-C%C3%B3digo-400"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:28:21Z"
rotulos: ["Configuração", "Autenticação", "Office365", "Oauth", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "oauth", "400", "token", "Contas SMTP", "Servidor SMTP", "token expirou", "expirou", "API revogada", "Erro", "O token expirou e não conseguimos obter um novo", "talvez a API tenha sido revogada", "Sugerimos que faça uma nova autenticação", "Código: 400", "Outlook", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# O token expirou e não conseguimos obter um novo, talvez a API tenha sido revogada. Sugerimos que faça uma nova autenticação. Código: 400

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33766950114839) **MENSAGEM:**

O token expirou e não conseguimos obter um novo, talvez a API tenha sido revogada. Sugerimos que faça uma nova autenticação. Código: 400

**SITUAÇÃO:**

Durante testes ou tentativas de envio de e-mails pelas telas **Servidor SMTP** ou **Contas SMTP**, o sistema exibe a mensagem de erro acima, impedindo o disparo de mensagens por contas configuradas com autenticação OAuth, como Outlook ou Office365.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33766950115735) SOLUÇÃO:**

**(1)** Pela tela **Contas SMTP:**

- Acesse a tela **''Contas SMTP''** (Configurações> Avançado > Envio de Mensagens > Contas SMTP);
- Selecione a conta de e-mail configurada com OAuth;
- Clique no botão **''Autenticação OAuth'';**
- Realize o login com a conta Microsoft autorizada;
- Após autenticar, o novo token será salvo automaticamente;
- Realize um teste de envio de e-mail para validar.

**(2)** Pela tela **Servidor SMTP:**

- Acesse a tela **''Servidor SMTP''** (Configurações> Avançado > Envio de Mensagens > Servidor SMTP);
- Clique no botão **''Autenticação OAuth''**;
- Realize a revalidação da conta Microsoft conforme instruções na tela.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33766950116247) CAUSA:**

Esse erro está relacionado à expiração do token de autenticação OAuth, utilizado pelo sistema Sankhya para se comunicar com os servidores da Microsoft (Outlook/Office365).

O token expirado refere-se a um token temporário de sessão, gerado durante a autenticação inicial, com validade limitada conforme as regras da Microsoft.

A falha ocorre quando o Sankhya não consegue renovar automaticamente esse token, devido a um dos seguintes motivos:

- Expiração sem renovação permitida;
- Revogação de permissões pelo administrador da conta Microsoft;
- Alterações na política de segurança da Microsoft;
- Mudanças no escopo ou configurações da aplicação no portal Azure.
