---
id: "30365835486103"
titulo: "Ao configurar um e-mail outlook e realizar a autenticação OAuth retorna o erro: the redirect URI specified in the request does not match"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30365835486103-Ao-configurar-um-e-mail-outlook-e-realizar-a-autentica%C3%A7%C3%A3o-OAuth-retorna-o-erro-the-redirect-URI-specified-in-the-request-does-not-match"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:03Z"
rotulos: ["Configuração", "email", "Autenticação", "outlook", "oauth", "the redirect URI", "microsofot", "confugração OAuth", "does not match", "configuracao oauth", "redirect URI", "erro oauth", "e-mail microsoft", "oauth microsoft", "Erro", "Artigo atualizado KCS", "Plataforma - KCS", "WMS - KCS", "Microsoft Entra"]
---

# Ao configurar um e-mail outlook e realizar a autenticação OAuth retorna o erro: the redirect URI specified in the request does not match

**MENSAGEM:**

AADSTS50011: The redirect URI
'https://arthuracrani.sde.sankhya.com.br/mge/genericOauth.mge' specified in
the request does not match the redirect URIs configured for the application 'd7372234-e37a-4118-838a-10278b96b230'. Make sure the redirect URI sent in the request matches one added to your application in the Azure portal. Navigate to https://aka.ms/redirectUriMismatchError to learn more about how to fix this.

**SITUAÇÃO:**

Ao realizar um cadastro de e-mail na tela "Conta SMTP" ou "Servidor SMTP" e realizar a autenticação OAuth de acordo com a [configuração de OAuth,](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410197622295-Configura%C3%A7%C3%B5es-OAuth) após obter as [credenciais da microsoft](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth) e realizar a autenticação na janela de login do outlook, retorna o erro informado a cima.

**CAUSA:**

O erro refere a uma divergência na URL da base SankhyaOm que está sendo feito em relação a URL inserida no microsoftentra. A causa pode ser a própria URL informada errada (tanto na tela "Configurações OAuth, campo "Redirect URI" quanto na microsoft), a base não possuir certificação SSL e não ser " httpS:// " ou estar usando outro cliente ID

**SOLUÇÃO:**

(1)** Acesse novamente o**[**Microsoft Entra.**](https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fentra.microsoft.com%2Fsignin%2Findex%2F&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3D81ZtVtoHs_guMhSBt0eUgF6X3cYbwzU6_epHgggbPw1hwpAqJv53FukYfjeeEeA9lTYMp22H7LDAALmvBft1rAHEFn2Q2bAGYt6JiElRfpl1Mi_Ykta8a_9Vy5X39mC4mpfw9BLLjt6to4Iyk8ZDKO0N1J95CPmM_j10_F2NGZp1TXD7mZAByo_D_YItEFFLNF12ISJN7fN5gUalZOfqut_RFLGCuAGO_Zbyde-XbOglAlxgNoQM4NWByEwusewrKy5wapPmOWxbDJLRMHdj2W5iZkh3VOPy00d2rjHZ7To0EMSgjXEIwka-Kbn84zK66pFIAfdMELrh83vOTN5Wn9d9IGjs6XzKG7GYAriSwPVayrcHYhw2KiMemJl3uEhGPH4PzNYZLKJ5hEUXuNuFChDV-ynKSX_UinzoWtpgQ7eVRkbfdenr9cYw4sF-Gppu&response_mode=form_post&nonce=638592325777495352.ZWQ3ODM5M2EtYzgyYy00NDcyLWI5NmUtOWJlNWNjMDJiMzc3MTQ3NzhlOTctMzQ3YS00OGU0LWI2NzAtNDFkZWFjMzdmNDNi&client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&site_id=501430&cobrandid=106b89c7-ab4e-4963-afb3-004cd2f15cac&client-request-id=ae9f5def-276f-4c7d-833d-012e1b92faaf&x-client-SKU=ID_NET472&x-client-ver=7.5.0.0&sso_reload=true)

**(2)** Selecione a API que está sendo usada para a autenticação.

**(3)** No menu lateral selecione o campo **"Autenticação"** e na opção **"URI de redirecionamento"** verifique se a URL informada é a mesma da base SankhyaOm que a configuração está sendo feita. Para isso, no **SankhyaOM**, acesse: outras opções > configurações > selecione a base usada > clique em **"editar"** e copie a URL. Em seguida, **adicione /mge/genericOAuth.mge no final da URL**.

**Exemplo:**

- link de acesso para a base: sankhya.com.br/mge
- link de redirecionamento (é fixo, sempre será o: /mge/genericOAuth.mge)

**Observação:** importante verificar que ao copiar e colar o '/mge' ficará duplicado, exclua um deles de modo que fique dessa forma:

- **https://sankhya.com.br/mge/genericOAuth.mge**

Depois, insira esta URL no campo **"URI de redirecionamento"** da microsoft entra

**(4)** Verifique se a base é " httpS:// " pois a microsoft insere automaticamente na URI, obrigando a base a também ser.

Caso o erro esteja: The redirect URI  'HTTP://arthuracrani.sde.sankhya.com.br/mge/genericOauth.mge' specified in....' **sem o "S"** é necessário incluir o certificado SSL no link de acesso à base

**(5)** No Sankhya, tela **"Configurações OAuth"**, campo **"redirect URI"** verifique se está inserido "/mge/genericOAuth.mge".

**Atenção:** verificar se o **"A"** do **OAuth** também está em maiúsculo, pois em alguns casos é inserido **"Oauth"** que também pode gerar o erro.

**(6)**Verifique se o campo Client Id na tela configurações OAuth é o mesmo informado no site da microsoftentra, clicando em **"visão geral"** e verificando o campo **"id do aplicativo (cliente)"**

(7)** Após essas verificações autentique novamente.**
