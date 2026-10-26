---
id: "4410197622295"
titulo: "Configurações OAuth"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:56Z"
rotulos: ["Configuração", "Segurança", "br.com.sankhya.ConfigsOAuth", "envio de mensagens", "OAuth", "Gmail", "Configuração OAuth para Gmail: Simplificando a Autenticação", "Outlook"]
---

# Configurações OAuth

```
 Módulo: Configurações > Avançado > Envio de Mensagens 
```

---

Desde o dia 30 de maio de 2022 o Google atualizou os critérios de segurança e passou a utilizar o protocolo OAuth para a autenticação de aplicações, e com essa ação o Google deixou de oferecer suporte para o uso de aplicativos ou dispositivos de terceiros que solicitam login utilizando apenas seu nome de usuário e senha.
Fonte: <https://support.google.com/accounts/answer/6010255>

O protocolo OAuth permite que aplicações acessem dados de um usuário de forma segura, sem a necessidade de compartilhamento de senhas. Para a utilização deste protocolo no **Sankhya Om** é necessário o registro do aplicativo e obtenção das credenciais dele, e a inserção das credenciais na tela **"Configurações OAuth do Sankhya"**.

Para usar o protocolo OAuth no **Sankhya Om**, primeiro obtenha as credenciais no aplicativo [Google](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744604472983-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Google-para-o-protocolo-OAuth) ou [Outlook](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth). Depois, acesse a tela Configurações OAuth.

![Imagem 1: Para usar o protocolo OAuth no Sankhya Om , primeiro obtenha as credenciais no aplicativo Google ou Outlook . Depois,…](https://ajuda.sankhya.com.br/hc/article_attachments/25747918127639)

Insira um nome para a configuração. Depois, escolha o **"Provedor"** adequado entre as opções disponíveis, **"Gmail"** ou **"Outlook"**.

---

### Configuração para Gmail:

Informe o **"Nome da API"** conforme cadastrado no Google Cloud. Em seguida, insira o **"Client ID"** e **"Client Secret"** relacionado ao aplicativo criado.

Preencha os campos a seguir com as informações específicas para o Gmail:

**URL da API do Google:** https://accounts.google.com/signin/oauth/oauthchooseaccount

**URL para obter o Access Token:** https://oauth2.googleapis.com/token

**URL da API do Google People:** https://people.googleapis.com/v1/people/me/?access\_token

**Redirect URI:** /mge/genericOAuth.mge

**Scopes:** https://www.googleapis.com/auth/userinfo.profile%20https://www.googleapis.com/auth/userinfo.email%20https%3A%2F%2Fmail.google.com%2F%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.action.compose%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.action%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.metadata%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.insert%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.labels%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.metadata%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.modify%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.send%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.settings.basic%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.settings.sharing&access\_type=offline&o2v=2&as=EXe1pFcAZPvx5\_2\_7FHg3g&flowName=GeneralOAuthFlow

Com os campos preenchidos, clique em **"Salvar"**.

Para saber mais, acesse [Obtenção das credenciais do aplicativo Google para o protocolo OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744604472983-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Google-para-o-protocolo-OAuth).

---

### Configuração para Outlook:

Se você escolheu o Outlook, informe o **Nome da API** (conforme cadastrado no portal da Microsoft), o **Client ID** e o **Client Secret**. A partir deste ponto, você tem duas opções de configuração para a sua integração:

**1. Via Graph API (Novo Padrão Recomendado):**

- Ative a marcação **Usa Graph API para envio**.
- Preencha o **Redirect URI** com: /mge/genericOAuth.mge
- Preencha o campo **Scopes** com: offline\_access Mail.Send openid profile

**Para saber mais:** Acesse o artigo [Obtenção das credenciais do aplicativo Outlook para Graph API](https://ajuda.sankhya.com.br/hc/pt-br/articles/40377307749399-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-Graph-API) para conferir as permissões necessárias neste modelo.

**2. Via SMTP (Legado):**

- Deixe a marcação **Usa Graph API para envio** desativada.
- Preencha o **Redirect URI** com: /mge/genericOAuth.mge
- Preencha o campo **Scopes** com: offline\_access https://outlook.office.com/SMTP.Send

**Atenção:** a Microsoft deixará de oferecer suporte de segurança para o envio via SMTP a partir de **01/03/2026**. Recomendamos que você priorize a configuração via Graph API para evitar interrupções e garantir a segurança das suas operações.

**Para saber mais:** Acesse o artigo [Obtenção das credenciais do aplicativo Outlook para o protocolo OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth) para conferir as permissões do modelo legado.

Após preencher os dados do seu provedor, clique em **Salvar**.

#### Vinculação no Servidor SMTP

Com a configuração OAuth salva, você deve vinculá-la à sua conta de e-mail no sistema.

Acesse a tela [**Servidor SMTP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP), localize a conta desejada e ative a marcação **Autenticar com OAuth**. No campo **Configurações OAuth**, busque o registro que você acabou de criar. Em seguida, realize a autenticação na tela do provedor para confirmar o processo. Você pode garantir que a configuração ocorreu com sucesso enviando um e-mail de teste

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth#top)
