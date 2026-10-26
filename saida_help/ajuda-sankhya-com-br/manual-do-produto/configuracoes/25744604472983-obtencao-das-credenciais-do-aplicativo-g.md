---
id: "25744604472983"
titulo: "Obtenção das credenciais do aplicativo Google para o protocolo OAuth"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25744604472983-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Google-para-o-protocolo-OAuth"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:49Z"
rotulos: ["Configuração", "br.com.sankhya.ConfigsOAuth", "OAuth", "Gmail", "API", "Credenciais", "Google Cloud"]
---

# Obtenção das credenciais do aplicativo Google para o protocolo OAuth

### Obtenção das credenciais do aplicativo Google

Primeiramente, realize o login no [Google Cloud Platform](https://console.cloud.google.com/), clique em **"Selecionar um projeto"** e opte pela criação de um **"Novo projeto"**, com o nome e local de armazenamento de acordo com os padrões da sua empresa:

[GIF animado: Imagem 1: Primeiramente, realize o login no Google Cloud Platform , clique em "Selecionar um projeto" e opte pela criação de um…](https://ajuda.sankhya.com.br/hc/article_attachments/25744604419223)

Depois, selecione o projeto criado e na **"Tela de permissão OAuth"** indique que o aplicativo é de uso **"Externo"**, ou seja, está disponível para qualquer usuário de teste que tenha uma conta do Google. Feito isso, clique em **"Criar"**:

[GIF animado: Imagem 2: Depois, selecione o projeto criado e na "Tela de permissão OAuth" indique que o aplicativo é de uso "Externo" , ou…](https://ajuda.sankhya.com.br/hc/article_attachments/25744541127063)

Será apresentada a tela para as configurações do aplicativo criado. Na etapa de permissões, informe o nome do app, e-mail para suporte do usuário, o domínio autorizado, por exemplo, sankhya.com.br, e na seção **"Dados de contato do desenvolvedor"** preencha o **"Endereço de e-mail"** do responsável que está realizando a configuração. Clique em **"Salvar e Continuar"** para passar para a próxima etapa:

[GIF animado: Imagem 3: Será apresentada a tela para as configurações do aplicativo criado. Na etapa de permissões, informe o nome do app,…](https://ajuda.sankhya.com.br/hc/article_attachments/25744604428567)

Pressione o botão **"Adicionar ou remover escopos"** e selecione todas as APIs disponíveis. Em seguida, clique em **"Salvar e Continuar"** para passar para a próxima etapa:

[GIF animado: Imagem 4: Pressione o botão " Adicionar ou remover escopos " e selecione todas as APIs disponíveis. Em seguida, clique em "Salvar…](https://ajuda.sankhya.com.br/hc/article_attachments/25744541133335)

Na terceira etapa, informe um e-mail para a realização de testes da configuração. Para isso, pressione o botão **"+Add Users"** ou clique em **"Salvar e Continuar"** para seguir para a próxima etapa onde será exibido o resumo das informações inseridas. Para concluir essa configuração, clique em **"Salvar e Continuar".**

[GIF animado: Imagem 5: Na terceira etapa, informe um e-mail para a realização de testes da configuração. Para isso, pressione o botão "+Add…](https://ajuda.sankhya.com.br/hc/article_attachments/25744541137431)

Após realizar as configurações de permissão OAuth, é necessário gerar as credenciais que serão inseridas no **Sankhya Om**. Para isso, selecione o projeto criado anteriormente, clique em **"+ Criar Credenciais"** e selecione a opção **"ID do cliente OAuth"**. 

Com está opção selecionada, será exibida a tela **"Criar ID do cliente OAuth"**. Em **"Tipo de aplicativo"** indique a opção **"Aplicativo Web"** e no campo **"Nome"** informe um nome para o aplicativo.

Na seção **"URIs de redirecionamento autorizados"**, clique no botão **"Adicionar URL"** para preencher o endereço do local do servidor da aplicação e adicione no final do caminho a informação mge/genericOAuth.mge, como, por exemplo:

[https:/exemplo.sankhya.com.br/mge/genericOAuth.mge](https://localhost:8080/mge/genericOAuth.mge).

[GIF animado: Imagem 6: https:/exemplo.sankhya.com.br/mge/genericOAuth.mge .](https://ajuda.sankhya.com.br/hc/article_attachments/25744541152279)

![Imagem 7: O Google exige que o servidor utilize protocolo HTTPS para estabelecer uma comunicação segura para transmissão de…](https://ajuda.sankhya.com.br/hc/article_attachments/25744541156375) O Google exige que o servidor utilize protocolo HTTPS para estabelecer uma comunicação segura para transmissão de informações.

Ao clicar em **"Criar"** será disponibilizado as credenciais **"Client ID"** e **"Client Secret"**, que serão utilizadas pelo **Sankhya Om**.

### Configurações do protocolo OAuth no Sankhya Om

Acesse agora a tela [Configurações OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth) para a utilização do protocolo OAuth no **Sankhya Om**.

![Imagem 8: Acesse agora a tela Configurações OAuth para a utilização do protocolo OAuth no Sankhya Om .](https://ajuda.sankhya.com.br/hc/article_attachments/25747596787351)

Insira um nome para a configuração. Depois, em **"Provedor"** selecione **"Gmail"**.

Informe o **"Nome da API"** conforme cadastrado no Google Cloud. Em seguida, insira o **"Client ID"** e **"Client Secret"** relacionado ao aplicativo criado.

Preencha os campos a seguir com as informações específicas para o Gmail:

**URL da API do Google:** https://accounts.google.com/signin/oauth/oauthchooseaccount

**URL para obter o Access Token:** https://oauth2.googleapis.com/token

**URL da API do Google People:** https://people.googleapis.com/v1/people/me/?access\_token

**Redirect URI:** /mge/genericOAuth.mge

**Scopes:** https://www.googleapis.com/auth/userinfo.profile%20https://www.googleapis.com/auth/userinfo.email%20https%3A%2F%2Fmail.google.com%2F%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.action.compose%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.action%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.metadata%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.addons.current.message.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.insert%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.labels%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.metadata%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.modify%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.send%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.settings.basic%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.settings.sharing&access\_type=offline&o2v=2&as=EXe1pFcAZPvx5\_2\_7FHg3g&flowName=GeneralOAuthFlow

Com os campos preenchidos, clique em **"Salvar"**.

Após realizar a configuração OAuth, deve-se vincular as configurações do servidor SMTP. Para isso, na conta SMTP cadastrada na tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP), acione a marcação **"Autenticar com OAuth"** e no campo **"Configurações OAuth"** busque o registro cadastrado na etapa anterior:

[GIF animado: Imagem 9: Após realizar a configuração OAuth, deve-se vincular as configurações do servidor SMTP. Para isso, na conta SMTP…](https://ajuda.sankhya.com.br/hc/article_attachments/25745355317527)

Após selecionar a configuração OAuth, realize a autenticação e confirme o processo. 

Pode-se certificar de que a configuração foi realizada com sucesso a partir do envio de um e-mail de teste.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744604472983-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Google-para-o-protocolo-OAuth#top)
