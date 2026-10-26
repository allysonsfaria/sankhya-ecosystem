---
id: "29900464543639"
titulo: "Houve falha de autenticação. Verifique o usuário e senha ao cadastrar e-mail Gmail (google) ou Outlook (microsoft)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29900464543639-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-ao-cadastrar-e-mail-Gmail-google-ou-Outlook-microsoft"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:47Z"
rotulos: ["Configuração", "Segurança", "email", "Financeiro", "e-mail", "Houve falha de autenticacao", "outlook", "google", "gmail", "senha incorreta", "senha", "Houve falha de autenticação", "Verifique o usuário e senha ao cadastrar e-mail", "smtp", "contas smtp", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Houve falha de autenticação. Verifique o usuário e senha ao cadastrar e-mail Gmail (google) ou Outlook (microsoft)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/29902040307351) MENSAGEM:**

Houve falha de autenticação. Verifique o usuário e senha ao cadastrar e-mail Gmail (google) ou Outlook (microsoft).

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29900436641047) **SITUAÇÃO:**

Ao acessar a tela "Servidor SMTP" ou "Contas SMTP" e cadastrar um e-mail ao clicar em "Confirmar" retorna "Dados confirmados com sucesso" mas ao fazer o envio do e-mail teste retorna falha de autenticação.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/29900464536599) CAUSA:**

O erro é causado ao inserir a senha errada do e-mail ou usar a senha padrão (usada para acessar a caixa de entrada do e-mail) quando o provedor exige outro tipo de autenticação, como OAuth ou senha de aplicativo.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29900436643223)SOLUÇÃO:**

![Imagem 5: Confirme qual o "Servidor SMTP" informado no cadastro do e-mail(nas telas "Contas SMTP" e "Servidor SMTP") e se está de…](https://ajuda.sankhya.com.br/hc/article_attachments/29900436643863)  Confirme qual o "Servidor SMTP" informado no cadastro do e-mail(nas telas "Contas SMTP" e "Servidor SMTP") e se está de acordo com o e-mail informado (Em casos onde há troca de e-mail é preciso confirmar se é o mesmo provedor ou se teve alteração);

![Imagem 6: Acesse o e-mail direto do provedor fora do Sankhya para confirmar a autenticação(por exemplo: logar no e-mail Gmail…](https://ajuda.sankhya.com.br/hc/article_attachments/29900464540567)  Acesse o e-mail direto do provedor fora do Sankhya para confirmar a autenticação(por exemplo: logar no e-mail Gmail direto pelo google);

![Imagem 7: Verifique se o provedor é do Google ou da Microsoft (Caso estejam informando no sankhya a mesma senha padrão usada para…](https://ajuda.sankhya.com.br/hc/article_attachments/29900436645527)  Verifique se o provedor é do Google ou da Microsoft (Caso estejam informando no sankhya a mesma senha padrão usada para logar diretamente no e-mail irá retornar o erro de autenticação pois é necessário usar senha de conexão com API - cada provedor usa uma forma específica);

![Imagem 8: Se for Gmail é necessário realizar a autenticação de 2 fatores com senha de aplicativo, seguindo os passos do artigo…](https://ajuda.sankhya.com.br/hc/article_attachments/29900464541463)  Se for Gmail é necessário realizar a autenticação de 2 fatores com senha de aplicativo, seguindo os passos do artigo [Usar Gmail no sistema Sankhya com ativação em duas etapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10018281372951--Usar-Gmail-no-sistema-Sankhya-com-ativa%C3%A7%C3%A3o-em-duas-etapas)ou  [Configurações OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth).

![Imagem 9: Se for Outlook é necessário realizar as Configurações OAuth se após essas configurações o erro permanecer, realize o…](https://ajuda.sankhya.com.br/hc/article_attachments/29900464542103)  Se for Outlook é necessário realizar as [Configurações OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth) se após essas configurações o erro permanecer, realize o passo a passo do artigo: [Houve falha de autenticação. Verifique o usuário e senha - Office365](https://ajuda.sankhya.com.br/hc/pt-br/articles/4805688673175-Houve-falha-de-autentica%C3%A7%C3%A3o-Verifique-o-usu%C3%A1rio-e-senha-Office365)
