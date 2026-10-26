---
id: "30261767501079"
titulo: "Processo de autenticação falhou! Por favor contate o administrador do sistema (Outlook)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30261767501079-Processo-de-autentica%C3%A7%C3%A3o-falhou-Por-favor-contate-o-administrador-do-sistema-Outlook"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:36:23Z"
rotulos: ["Configuração", "Segurança", "Autenticação", "outlook", "Processo de Autenticação falhou!", "falhou", "processo de autenticacao", "Erro", "Microsoft Entra"]
---

# Processo de autenticação falhou! Por favor contate o administrador do sistema (Outlook)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30261767489303) MENSAGEM:**

Processo de Autenticação falhou! Por favor contacte o administrador do sistema.

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30261777186583) **SITUAÇÃO:**

Ao acessar a tela "Servidor SMTP" ou "Contas SMTP" e realizar as configurações para autenticação OAuth e/ou selecionar uma configuração e tentar autenticar com um usuário (e-mail) que não é **"Administrador"** do Outlook corporativo, retorna o erro de autenticação.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30261777188631)SOLUÇÃO:**

![Imagem 4: Acesse o Microsoft Entra com o usuário "Administrador" e realize a configuração de permissão do usuário que vai…](https://ajuda.sankhya.com.br/hc/article_attachments/30261777190295) Acesse o [Microsoft Entra](https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?redirect_uri=https%3A%2F%2Fentra.microsoft.com%2Fsignin%2Findex%2F&response_type=code%20id_token&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2Fuser_impersonation%20openid%20email%20profile&state=OpenIdConnect.AuthenticationProperties%3D81ZtVtoHs_guMhSBt0eUgF6X3cYbwzU6_epHgggbPw1hwpAqJv53FukYfjeeEeA9lTYMp22H7LDAALmvBft1rAHEFn2Q2bAGYt6JiElRfpl1Mi_Ykta8a_9Vy5X39mC4mpfw9BLLjt6to4Iyk8ZDKO0N1J95CPmM_j10_F2NGZp1TXD7mZAByo_D_YItEFFLNF12ISJN7fN5gUalZOfqut_RFLGCuAGO_Zbyde-XbOglAlxgNoQM4NWByEwusewrKy5wapPmOWxbDJLRMHdj2W5iZkh3VOPy00d2rjHZ7To0EMSgjXEIwka-Kbn84zK66pFIAfdMELrh83vOTN5Wn9d9IGjs6XzKG7GYAriSwPVayrcHYhw2KiMemJl3uEhGPH4PzNYZLKJ5hEUXuNuFChDV-ynKSX_UinzoWtpgQ7eVRkbfdenr9cYw4sF-Gppu&response_mode=form_post&nonce=638592325777495352.ZWQ3ODM5M2EtYzgyYy00NDcyLWI5NmUtOWJlNWNjMDJiMzc3MTQ3NzhlOTctMzQ3YS00OGU0LWI2NzAtNDFkZWFjMzdmNDNi&client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&site_id=501430&cobrandid=106b89c7-ab4e-4963-afb3-004cd2f15cac&client-request-id=ae9f5def-276f-4c7d-833d-012e1b92faaf&x-client-SKU=ID_NET472&x-client-ver=7.5.0.0&sso_reload=true) com o usuário **"Administrador"**  e realize a configuração de permissão do usuário que vai autenticar conforme abaixo.

![Imagem 5: No menu lateral esquerdo, clique em "Aplicativos" e, em seguida, selecione "Aplicativos Empresariais".](https://ajuda.sankhya.com.br/hc/article_attachments/30261777191703) No menu lateral esquerdo, clique em **"Aplicativos"** e, em seguida, selecione **"Aplicativos Empresariais".**

![Imagem 6: No submenu "Gerenciar" , clique em "Configuração de consentimento do usuário". Adicione o endereço de e-mail do usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/30261777192727) No submenu **"Gerenciar"**, clique em "Configuração de consentimento do usuário". Adicione o endereço de e-mail do usuário que será autenticado.

![Imagem 7: No submenu "Gerenciar" , clique em "Classificações de permissão" . Adicione as seguintes permissões do Microsoft Graph:](https://ajuda.sankhya.com.br/hc/article_attachments/30261767494039) No submenu **"Gerenciar"**, clique em **"Classificações de permissão"**. Adicione as seguintes permissões do Microsoft Graph:

- email
- offline\_access
- openid
- profile
- Mail.Send
- SMTP.Send
- User.Read

**OBSERVAÇÃO:**

Caso ainda não tenha adicionado as permissões acima é necessario primeiro seguir as configurações do artigo [Obtenção das credenciais do aplicativo Outlook para o protocolo OAuth](https://ajuda.sankhya.com.br/hc/pt-br/articles/25744837815959-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-o-protocolo-OAuth)

![Imagem 8: No SankhyaOM cesse a tela Servidor SMTP (Configurações >Avançado > Envio de Mensagens > Servidor SMTP) ou Contas SMTP…](https://ajuda.sankhya.com.br/hc/article_attachments/30261777194775)  No SankhyaOM cesse a tela **Servidor SMTP** (Configurações >Avançado > Envio de Mensagens > Servidor SMTP) ou **Contas SMTP** (Configurações > Avançado > Envio de Mensagens > Contas SMTP), desmarque a opção **"Autenticar com OAuth"** e marque-a novamente. Isso iniciará o processo de autenticação com as novas permissões.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30261777187223) CAUSA:**

O erro é retornado quando o usuário(e-mail) que não é administrador, não tem permissão para autenticar em aplicativos empresariais.
