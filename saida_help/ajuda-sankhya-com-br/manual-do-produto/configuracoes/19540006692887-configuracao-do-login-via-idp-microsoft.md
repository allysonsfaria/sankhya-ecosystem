---
id: "19540006692887"
titulo: "Configuração do login via IDP Microsoft Azure no Sankhya Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:41:14Z"
rotulos: ["Configuração", "Segurança", "Integração", "IDP", "Configuração do login via IDP Microsoft Azure no Sankhya Om", "Configuração do Login via Microsoft Azure no Sankhya Om", "SAML", "Sankhya Om", "Microsoft Azure"]
---

# Configuração do login via IDP Microsoft Azure no Sankhya Om

Neste artigo, abordaremos as etapas para configurar, utilizando o padrão SAML, a integração do login via IDP Microsoft Azure nas versões 4.21 e posteriores do **Sankhya Om**.

Esta configuração visa estabelecer a conexão entre ambas as aplicações, permitindo que o login no **Sankhya Om** seja realizado por meio do Microsoft Azure.

| **Configurações** |
| --- |
| [Configuração no portal da aplicação Azure](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#Configura%C3%A7%C3%A3onoportaldaaplica%C3%A7%C3%A3oAzure) |
| [Como gerar o metadado SP usando o Samltool?](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#ComogerarometadadoSPusandooSamltool?) |
| [Como gerar os metadados no Sankhya Om?](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#ComogerarosmetadadosnoSankhyaOm?) |

---

### Configuração no portal da aplicação Azure

**Importante:** apenas o usuário **"Administrador Global"** possui permissão para realizar essa configuração.

![Imagem 1: Acesse o site https://azure.microsoft.com/en-ca/get-started/azure-portal/ e clique em "Microsoft Entra ID" na página…](https://ajuda.sankhya.com.br/hc/article_attachments/19580796038679) Acesse o site <https://azure.microsoft.com/en-ca/get-started/azure-portal/> e clique em **"Microsoft Entra ID"** na página principal do portal.

![Imagem 2: Acesse o site https://azure.microsoft.com/en-ca/get-started/azure-portal/ e clique em "Microsoft Entra ID" na página…](https://ajuda.sankhya.com.br/hc/article_attachments/19540652366871)

![Imagem 3: Na parte superior da tela, acesse o menu "+Add" e selecione a opção "Enterprise application" .](https://ajuda.sankhya.com.br/hc/article_attachments/19580825676695) Na parte superior da tela, acesse o menu **"+Add"** e selecione a opção **"Enterprise application"**.

![Imagem 4: Na parte superior da tela, acesse o menu "+Add" e selecione a opção "Enterprise application" .](https://ajuda.sankhya.com.br/hc/article_attachments/19540746537495)

![Imagem 5: Na página seguinte, escolha a opção "Create your own application" . Assim, será apresentado um formulário à direita da…](https://ajuda.sankhya.com.br/hc/article_attachments/19580796055063) Na página seguinte, escolha a opção **"Create your own application"**. Assim, será apresentado um formulário à direita da tela. Nele, preencha os seguintes dados:

- No campo **"What’s the name of your app?"** defina o nome da aplicação utilizando, por exemplo, o nome do seu domínio **Sankhya**, como skwinovacao.sankhya.com.br (use skwinovacao).
- Marque a opção **"Integrate any other application you don't find in the gallery (Non-gallerry)"**.
- Após o preenchimento, clique em **"Create"**.

![Imagem 6: Após o preenchimento, clique em "Create" .](https://ajuda.sankhya.com.br/hc/article_attachments/19541286705687)

![Imagem 7: Com a aplicação criada, a página abaixo será aberta. Selecione a opção "2. Set up single sign on" .](https://ajuda.sankhya.com.br/hc/article_attachments/19580825709335) Com a aplicação criada, a página abaixo será aberta. Selecione a opção **"2. Set up single sign on"**.

![Imagem 8: Com a aplicação criada, a página abaixo será aberta. Selecione a opção "2. Set up single sign on" .](https://ajuda.sankhya.com.br/hc/article_attachments/19541507301527)

Em seguida, clique em **"SAML"**.

![Imagem 9: Em seguida, clique em "SAML" .](https://ajuda.sankhya.com.br/hc/article_attachments/19541892170903)

![Imagem 10: Depois, acione o botão Edit" para editar a "Basic SAML Configuration" .](https://ajuda.sankhya.com.br/hc/article_attachments/19580796074391) Depois, acione o botão **Edit"** para editar a **"Basic SAML Configuration"**.

![Imagem 11: Depois, acione o botão Edit" para editar a "Basic SAML Configuration" .](https://ajuda.sankhya.com.br/hc/article_attachments/19541892180375)

No pop-up apresentado, informe os seguintes campos:

- Informe no campo **"Identifier (Entity ID)"** o nome da aplicação, como, por exemplo, skwinovacao.
- Insira no campo **"Reply URL (Assertion Consumer Service URL)"** o link da aplicação **Sankhya Om**, como, por exemplo, skwinovacao.sankhya.com.br/mge/acs. Certifique-se de que "/mge/acs" esteja no final da URL.
- Preencha o campo **"Sign on URL"** com o link da aplicação **Sankhya Om**, por exemplo, skwinovacao.sankhya.com.br/mge/sso. É obrigatório que o "/mge/sso" esteja no final da URL.

Clique em salvar.

![Imagem 12: Agora, em "User Attributes & Claims" clique no botão de edição.](https://ajuda.sankhya.com.br/hc/article_attachments/19580796082455) Agora, em **"User Attributes & Claims"** clique no botão de edição. 

![Imagem 13: Agora, em "User Attributes & Claims" clique no botão de edição.](https://ajuda.sankhya.com.br/hc/article_attachments/19543791685527)

Depois, clique no botão ![Imagem 14: Depois, clique no botão "Edit" para editar a linha de "Emailaddress" .](https://ajuda.sankhya.com.br/hc/article_attachments/19573504939159) **"Edit"** para editar a linha de **"Emailaddress"**.

![Imagem 15: Depois, clique no botão "Edit" para editar a linha de "Emailaddress" .](https://ajuda.sankhya.com.br/hc/article_attachments/19543563899799)

Informe o campo **"Name"** com a nomenclatura **"EmailAddress"** e mantenha o campo **"Namespace"** vazio. Clique em salvar. 

![Imagem 16: Informe o campo "Name" com a nomenclatura "EmailAddress" e mantenha o campo "Namespace" vazio. Clique em salvar.](https://ajuda.sankhya.com.br/hc/article_attachments/19549717069591)

![Imagem 17: Agora, no menu esquerdo da tela clique na opção "Single sign-on" para que a tela abaixo seja apresentada novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/19580796088215) Agora, no menu esquerdo da tela clique na opção **"Single sign-on"** para que a tela abaixo seja apresentada novamente.

![Imagem 18: Agora, no menu esquerdo da tela clique na opção "Single sign-on" para que a tela abaixo seja apresentada novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/19549690051863)

![Imagem 19: Em "SAML Certificates" clique no botão "Edit" . No pop-up que será apresentado à direita da tela, selecione no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19580796095383) Em **"SAML Certificates"** clique no botão **"Edit"**. No pop-up que será apresentado à direita da tela, selecione no campo **"Signing Option"** a opção **"Sign SAML response and assertion"**.

![Imagem 20: Em "SAML Certificates" clique no botão "Edit" . No pop-up que será apresentado à direita da tela, selecione no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/19573815083671)

![Imagem 21: Na seção "Verification certificates" , clique no botão "Edit" e certifique-se de que as opções "Require verification…](https://ajuda.sankhya.com.br/hc/article_attachments/19580819492375) Na seção **"Verification certificates"**, clique no botão **"Edit"** e certifique-se de que as opções **"Require verification certificates"** e **"Allow requests signed with RSA-SHA1"** estejam desmarcadas.

![Imagem 22: Na seção "Verification certificates" , clique no botão "Edit" e certifique-se de que as opções "Require verification…](https://ajuda.sankhya.com.br/hc/article_attachments/19574365030551)

![Imagem 23: No menu "Users and group" , clique na opção "+Add user/group" para adicionar os usuários que irão utilizar a solução.…](https://ajuda.sankhya.com.br/hc/article_attachments/19580819505943) No menu **"Users and group"**, clique na opção **"+Add user/group"** para adicionar os usuários que irão utilizar a solução. Feito isso, clique em salvar.

![Imagem 24: No menu "Users and group" , clique na opção "+Add user/group" para adicionar os usuários que irão utilizar a solução.…](https://ajuda.sankhya.com.br/hc/article_attachments/19574820597143)

![Imagem 25: Por fim, retorne ao menu "Single sign-on" , na seção "SAML Certifiques" e faça o download do arquivo "Fedration…](https://ajuda.sankhya.com.br/hc/article_attachments/19580866176663) Por fim, retorne ao menu **"Single sign-on"**, na seção **"SAML Certifiques"** e faça o download do arquivo **"Fedration Metadata XML"**. Armazene-o em um local de fácil acesso em sua máquina com o nome **"IDP\_metadados.xml"**. Este arquivo será utilizado posteriormente.

![Imagem 26: Por fim, retorne ao menu "Single sign-on" , na seção "SAML Certifiques" e faça o download do arquivo "Fedration…](https://ajuda.sankhya.com.br/hc/article_attachments/19575215936407)

![Imagem 27: O navegador Sankhya não tem suporte para login via SSO. Portanto, é necessário utilizar navegadores externos.](https://ajuda.sankhya.com.br/hc/article_attachments/26133385844887) O navegador Sankhya não tem suporte para login via SSO. Portanto, é necessário utilizar navegadores externos.

 [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#top)

### Como gerar o metadado SP usando o Samltool?

Acesse o site <https://www.samltool.com/online_tools.php> e no menu **"BUILD METADATA"** clique em **"SP"**:

![Imagem 28: Acesse o site https://www.samltool.com/online_tools.php e no menu "BUILD METADATA" clique em "SP" :](https://ajuda.sankhya.com.br/hc/article_attachments/19581346361367)

Assim, será apresentada a página **"Build SP Metadata"**. Nela, preencha os seguintes dados:

- Preencha o campo **"EntityID"** com o nome da aplicação que foi inserida na etapa 7, do tópico [Configuração no portal da aplicação Azure](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887#Configura%C3%A7%C3%A3onoportaldaaplica%C3%A7%C3%A3oAzure).
- Informe o campo **"Attribute Consume Service Endpoint"** com a url da base + **/mge/acs**, exemplo: skwinovacao.sankhya.com.br/mge/acs.
- Utilize no campo **"Single Logout Service Endpint"** a URL da base + /mge/sso, como, por exemplo: skwinovacao.sankhya.com.br/mge/sso.
- No campo **"Nameid Format"** selecione a opção **"urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"**.
- Indique no campo **"AuthnResquestsSigned"** a opção **"False"**.
- Por fim, no campo **"Want AssertionsSigned"** escolha a opção **"True"**.

![Imagem 29: Por fim, no campo " Want AssertionsSigned" escolha a opção "True" .](https://ajuda.sankhya.com.br/hc/article_attachments/19581514039319)

No final dessa página, clique no botão **"Build SP Metadata"**. Assim, será gerado um arquivo, salve-o com o nome **"SP\_metadados.xml"** e armazeno-o em um local de fácil acesso em sua máquina para uso posterior.

 [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#top)

### Como gerar os metadados no Sankhya Om?

Acesse o sistema **Sankhya Om** utilizando o usuário **"SUP"** e abra a tela **"Repositório de arquivos"**. Em seguida, clique no botão  **"Criar nova pasta"** e crie uma pasta com a nomenclatura **"sso"**, utilizando todas as letras minúsculas.

![Imagem 30: Acesse o sistema Sankhya Om utilizando o usuário "SUP" e abra a tela "Repositório de arquivos" . Em seguida, clique no…](https://ajuda.sankhya.com.br/hc/article_attachments/19582346435479)

Selecione a pasta SSO e adicione os dois metadados realizados anteriormente, o **"SP\_metadados"** gerado pela ferramenta Samltool e o **"IDP\_metadados"** criado no passo 11 do tópico [Configuração no portal da aplicação Azure](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887#Configura%C3%A7%C3%A3onoportaldaaplica%C3%A7%C3%A3oAzure).

Para que o login no **Sankhya Om** seja bem-sucedido, o e-mail cadastrado para o usuário da plataforma Microsoft Azure deve ser o mesmo configurado na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874).

**Observação:** para o uso do SSO deve existir apenas um usuário com o mesmo email.

![Imagem 31: Observação: para o uso do SSO deve existir apenas um usuário com o mesmo email.](https://ajuda.sankhya.com.br/hc/article_attachments/19583366446487)

Com essas configurações realizadas para efetuar o login via Microsoft Azure, basta acessar o **Sankhya Om** a partir da URL de login acrescida de “/sso” (por exemplo: [https://nomedaaplicacao.com.br/mge/sso](https://nomedabase.com.br/mge/sso)).

![Imagem 32: Com essas configurações realizadas para efetuar o login via Microsoft Azure, basta acessar o Sankhya Om a partir da URL…](https://ajuda.sankhya.com.br/hc/article_attachments/19583193376663)

 [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/19540006692887-Configura%C3%A7%C3%A3o-do-login-via-IDP-Microsoft-Azure-no-Sankhya-Om#top)
