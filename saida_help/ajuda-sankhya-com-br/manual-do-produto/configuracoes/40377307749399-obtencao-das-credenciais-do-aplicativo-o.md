---
id: "40377307749399"
titulo: "Obtenção das credenciais do aplicativo Outlook para Graph API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40377307749399-Obten%C3%A7%C3%A3o-das-credenciais-do-aplicativo-Outlook-para-Graph-API"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T16:32:07Z"
rotulos: ["Configuração", "Segurança", "#API", "Outlook", "GRAPH", "Graph API", "Microsoft Entra"]
---

# Obtenção das credenciais do aplicativo Outlook para Graph API

Este guia orienta você no passo a passo para registrar um aplicativo no portal da Microsoft e obter as credenciais necessárias para utilizar a **Microsoft Graph API**. Este é o método mais moderno e seguro para o envio de e-mails pelo Sankhya Om, substituindo o protocolo SMTP legado.

### 1. Registro do aplicativo no Microsoft Entra

Para começar, acesse o portal **Microsoft Entra**. No menu lateral, clique em **Aplicativos** e selecione a opção **Registros de aplicativo**.

Clique em **+ Novo registro** e preencha os detalhes do seu novo aplicativo:

- **Nome:** Defina um nome que facilite a identificação (ex: Envio de E-mail Sankhya).
- **Tipos de conta com suporte:** Selecione a opção “Contas somente neste diretório organizacional (somente Diretório Padrão - único locatário)”.
- **URI de redirecionamento:** No campo de seleção, escolha **Web** e, ao lado, insira o endereço do seu servidor seguido de /mge/genericOauth.mge.

| **Importante**  Por questões de segurança, a Microsoft exige que o seu servidor utilize um certificado HTTPS válido para estabelecer a comunicação. |
| --- |

Após preencher os campos, clique em **Registrar**. Na tela de **Visão geral** que será exibida, copie e guarde os valores de **ID do aplicativo (cliente)** e **ID do diretório (locatário)**.

### 2. Geração do Segredo do Cliente

Agora, você precisa gerar uma chave de segurança para o seu aplicativo. No menu lateral, acesse **Certificados e segredos** e clique na aba **Segredos do cliente**.

Clique em **+ Novo segredo do cliente**, dê uma descrição para a chave e selecione o prazo de validade desejado. Ao clicar em **Adicionar**, o sistema gerará um código na coluna **Valor**.

| **Atenção**  Copie este código (Secret ID) imediatamente e guarde-o em um local seguro. Por segurança, a Microsoft oculta esse valor assim que você sai da tela ou atualiza a página. |
| --- |

### 3. Configuração de Permissões da Graph API

Para que o sistema consiga enviar os e-mails, você deve liberar os acessos corretos. No menu lateral, acesse **Permissões de APIs** e clique em **Adicionar uma permissão**.

Selecione a opção **Microsoft Graph** e, em seguida, **Permissões delegadas**. Busque e marque exatamente estas quatro permissões:

1. Mail.Send
2. offline\_access
3. openid
4. profile

Clique em **Adicionar permissões** para confirmar. Para finalizar esta etapa, clique no botão **"Conceder consentimento do administrador para o Diretório padrão"** que aparece logo abaixo da lista de permissões. Sem esse consentimento, a integração não será validada.

### 4. Configuração no Sankhya Om

Com todos os dados em mãos, acesse a tela **Configurações OAuth** no Sankhya Om para ativar a nova rotina:

1. Clique em **Novo** e defina um nome para a configuração.
2. No campo **Provedor**, selecione a opção **Outlook**.
3. Ative a marcação **Usa Graph API para envio**.
4. Insira o **Nome da API**, o **Client ID** e o **Client Secret** que você obteve no portal da Microsoft.
5. No campo **Redirect URI**, informe: /mge/genericOAuth.mge.
6. No campo **Scopes**, digite exatamente: offline\_access Mail.Send openid profile.
7. Clique em **Salvar**.

Após concluir estes passos, você deve realizar a vinculação da conta na tela **Servidor SMTP**, ativando a opção **Autenticar com OAuth** e selecionando o perfil que você acabou de criar. Finalize realizando a autenticação no provedor e enviando um e-mail de teste para validar a operação.
