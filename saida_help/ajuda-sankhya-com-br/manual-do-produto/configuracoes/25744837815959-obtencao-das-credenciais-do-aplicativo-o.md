---
id: "25744837815959"
titulo: "Obtenção das credenciais do aplicativo Outlook para o protocolo OAuth"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-17T13:28:16Z"
rotulos: ["Configuração", "Segurança", "br.com.sankhya.ConfigsOAuth", "OAuth", "Outlook", "Microsoft Graph API"]
---

# Obtenção das credenciais do aplicativo Outlook para o protocolo OAuth

**Atenção: Este método de envio será descontinuado** A Microsoft deixará de oferecer suporte de segurança para o envio de e-mails via **SMTP (SMTP AUTH)** a partir de **01/03/2026**.

Para garantir que as suas comunicações e faturamentos não sejam interrompidos, recomendamos fortemente que utilize a nova integração via **Microsoft Graph API**. Ela é mais segura, moderna e o novo padrão recomendado pelo sistema.

[**Clique aqui para acessar o novo guia: Obtenção das credenciais do aplicativo Outlook para Graph API**](https://ajuda.sankhya.com.br/hc/pt-br/articles/40377307749399-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-Graph-API)

### Sobre este manual

Este guia descreve o processo de obtenção de credenciais para o modelo de envio **SMTP via OAuth2 (Legado)**. Utilize estas instruções apenas se a sua operação ainda depender estritamente do protocolo SMTP e se estiver ciente do prazo de desativação mencionado acima.

Para criar o seu aplicativo no provedor da Microsoft, siga os passos abaixo:

### Obtenção das credenciais do aplicativo Outlook

Para criar um novo aplicativo utilizando o provedor da Microsoft, siga os passos abaixo:

Acesse o portal [Microsoft Entra](https://entra.microsoft.com/signin/index/). No menu lateral, clique em **"Aplicativos"** e em seguida selecione **"Registros de aplicativo"**. Clique na opção **"+Novo registro"**. Feito isso, preencha os detalhes do aplicativo:

- **Nome:** defina o nome do aplicativo;
- **Tipos de conta com suporte:** selecione um tipo de conta. Recomenda-se utilizar a opção **“Contas somente neste diretório organizacional (somente Diretório Padrão - único locatário)”**;
- **URI de redirecionamento:** escolha a opção **"Web"** e, no campo ao lado, insira a URI de redirecionamento, que deve ser o endereço do servidor seguido de /mge/genericOauth.mge.

Após preencher os campos, clique em **"Registrar"**.

**Importante:** certifique-se de que a aplicação utiliza um certificado HTTPS válido.

[GIF animado: Imagem 1: Importante: certifique-se de que a aplicação utiliza um certificado HTTPS válido.](https://ajuda.sankhya.com.br/hc/article_attachments/25744979704343)

Na tela que será apresentada, clique no menu **"Visão geral"**. Copie os valores de **"ID do aplicativo (cliente)"** e **"ID do diretório (locatário)"**. Essas informações serão inseridas posteriormente no **Sankhya Om**, na tela [Configuração Oauth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth).

![Imagem 2: Na tela que será apresentada, clique no menu "Visão geral" . Copie os valores de "ID do aplicativo (cliente)" e "ID do…](https://ajuda.sankhya.com.br/hc/article_attachments/25745314637463)

Agora, acesse no menu **"Certificados e segredos"** a aba **"Segredos do cliente"** e clique em **"+Novo segredo do cliente"**. Defina uma descrição e selecione o prazo de validade para o segredo. Clique em **"Adicionar"**.

![Imagem 3: Agora, acesse no menu "Certificados e segredos" a aba "Segredos do cliente" e clique em "+Novo segredo do cliente" .…](https://ajuda.sankhya.com.br/hc/article_attachments/25745314641815)

Depois, no campo **"Valor"** copie a chave gerada (Secret ID). Essa informação também será utilizada na tela Configuração Oauth.

Acesse o menu **"Permissões de APIs"** e clique em **"Adicionar uma permissão"** e em **"Permissões delegadas"**. No campo **"Selecionar permissões"** busque as permissões necessárias. Sugestão de permissões:

- email;
- offline\_access;
- openid;
- profile;
- Mail.Send;
- SMTP.Send;
- User.Read.

Clique em **"Adicionar permissões"** após selecionar as permissões desejadas.

![Imagem 4: Clique em "Adicionar permissões" após selecionar as permissões desejadas.](https://ajuda.sankhya.com.br/hc/article_attachments/25745314645399)

Por fim, marque a opção **"Conceder consentimento do administrador para o Diretório padrão"**.

### Configurações do protocolo OAuth no Sankhya Om

Acesse agora a tela [Configurações OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth) para a utilização do protocolo OAuth no **Sankhya Om**.

![Imagem 5: Acesse agora a tela Configurações OAuth para a utilização do protocolo OAuth no Sankhya Om .](https://ajuda.sankhya.com.br/hc/article_attachments/25747498870551)

Insira um nome para a configuração. Depois, em **"Provedor"** selecione **"Outlook"**.

Informe o **"Nome da API"** cadastrado no Microsoft. Em seguida, insira o **"Client ID"** e o **"Client Secret"** relacionado ao aplicativo criado.

Preencha os campos a seguir com as informações específicas para o Outlook:

**Redirect URI:** /mge/genericOAuth.mge

**Scopes:** offline\_access https://outlook.office.com/SMTP.Send

Com os campos preenchidos, clique em **"Salvar"**.

Após realizar a configuração OAuth, deve-se vincular as configurações do servidor SMTP. Para isso, na conta SMTP cadastrada na tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP), acione a marcação **"Autenticar com OAuth"** e no campo **"Configurações OAuth"** busque o registro cadastrado na etapa anterior:

[GIF animado: Imagem 6: Após realizar a configuração OAuth, deve-se vincular as configurações do servidor SMTP. Para isso, na conta SMTP…](https://ajuda.sankhya.com.br/hc/article_attachments/25747184201239)

Após selecionar a configuração OAuth, realize a autenticação e confirme o processo. 

Pode-se certificar de que a configuração foi realizada com sucesso a partir do envio de um e-mail de teste.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth#top)
