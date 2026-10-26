---
id: "42427459277591"
titulo: "Login via SSO com Microsoft"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427459277591-Login-via-SSO-com-Microsoft"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:03:43Z"
rotulos: ["sync_hc", "ploomes", "ploomes_11787364", "sync_hash_99c85ff2df47"]
---

# Login via SSO com Microsoft

## 1) Sobre o Login via Microsoft SSO

O login via Microsoft SSO permite que usuários corporativos acessem o Ploomes utilizando suas credenciais da Microsoft, como aquelas utilizadas no Entra ID (antigo Azure AD). Essa integração simplifica o fluxo de login, aumenta a segurança da plataforma e elimina a necessidade de gerenciamento manual de senhas no Ploomes.

É uma solução especialmente útil para empresas, em especial de grande porte, que já utilizam o ecossistema Microsoft em suas operações de TI, garantindo controle centralizado e sincronização de dados entre os sistemas.

## 2) Pré-requisitos

- Ter o módulo habilitado no Ploomes
- É necessário que o administrador da conta tenha permissões no ambiente Microsoft Entra ID
- Os usuários devem estar previamente cadastrados na Microsoft com os dados corretos (nome, e-mail e telefone)
- Nas propriedades do Aplicativo Empresarial, deve ser marcado a opção “Atribuição Necessária” como SIM. Caso não seja marcada essa opção, não será possível localizar o usuário no fluxo de login do Ploomes

[GIF animado: Imagem 1: Nas propriedades do Aplicativo Empresarial, deve ser marcado a opção “Atribuição Necessária” como SIM. Caso não seja…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1626066757/8a993a95d6c79872ed026520ea1e/opera_XT2K3iMqWi.gif?expires=1786536000&signature=8074beacbb68489256142c0527034280249fad5979095b145347045961133c6a&req=dSYlEMl4m4ZaXvMW3nq%2BgUelAkMvxn8J4UFGY%2Bmdykw8B7AYjcQy6BdSK8lN%0ApWi4nGrz20d0K3wU7aBv3ou2SqI%3D%0A)

**Observação:** pode ser necessário realizar a autorização da integração no Ploomes (através do menu Integrações plug and play) para que a aplicação seja exibida na aba "Aplicativos Empresariais" dentro da plataforma da Microsoft.

## 3) Configurando/Ativando a Integração de Login via Microsoft SSO

### Ativando a Integração via Plug and Play

1. Acesse o menu **Administração > Integrações Plug and Play**
2. Acesse a integração Microsoft
3. Clique em **Habilitar Integração**
4. Clique em **Autorizar Integração**
5. Faça login com sua conta de administrador na Microsoft e conceda as permissões necessárias (serão solicitadas duas vezes, em sequência)
6. Para finalizar, clique em **Ativar Integração**

[GIF animado: Imagem 2: Para finalizar, clique em Ativar Integração](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1626178891/514e07a10325b0599d656f7f3d45/SSO-ativando-_online-video-cutter_com_-_1_.gif?expires=1786536000&signature=774d19eb430ae42328b66442a1239a58e85223e1897852e48768a7934b5f3d90&req=dSYlEMh5lYlWWPMW3nq%2BgbEKe%2Bi6twA6pwOkfEFMrNBcGc9hz6A5vCQMqGJQ%0A8U4v9KVRAuo5gtALc4e8VfiSoCQ%3D%0A)

A integração estará ativa e os dados dos usuários começarão a ser sincronizados automaticamente. A partir desse momento, os usuários não conseguirão mais utilizar as senhas de acesso ao Ploomes, devendo utilizar as credenciais da Microsoft.

**Observação 1:** Só será possível ativar a integração desde que o módulo esteja habilitado no Ploomes. Caso seja necessário, solicite um contato do nosso time de vendas

**Observação 2:** Caso o e-mail de um usuário já possua vinculo a outra conta, ele não será criado e um alerta será retornado

![Imagem 3: Observação 2: Caso o e-mail de um usuário já possua vinculo a outra conta, ele não será criado e um alerta será…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1624200335/3ca906fd22c6c0f2d8b9cb1de416/image.png?expires=1786536000&signature=65680bae7b0747dfd2cc87d81f71b3b0b5d0784f70ef05ae8d5787564df58812&req=dSYlEst%2BnYJcXPMW3nq%2BgXUAHa2I8xQklXmyeyb7oy%2FYJ6HnNwJ%2FwnavGjTU%0A8BwX3DkpV5b4cKTLrGRvUdOuFVA%3D%0A)

## 4) Utilizando o Login via Microsoft

## 4.1.) Login com Microsoft

Após a integração ativa:

1. Acesse a tela de login do Ploomes.
2. Clique em **Entrar com Microsoft**.
3. Faça a autenticação com suas credenciais Microsoft.
4. Se tudo estiver correto, você será redirecionado à sua conta no Ploomes.

[GIF animado: Imagem 4: Se tudo estiver correto, você será redirecionado à sua conta no Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1627656638/843c8dc1c0f4971e66c1bc960c51/SSO_Login-_online-video-cutter_com_.gif?expires=1786536000&signature=725c70c2f9eb7edf74edf88cf8b680174a37cb7d972cd06b04289dfce136d0ee&req=dSYlEc97m4dcUfMW3nq%2BgWit34REATq8xR0lHfmJsIu9tHLCv6Lic97Fwsff%0AmhX9T1c92rQjE9yyX%2Fm9OybpT5c%3D%0A)

⚠️ Atenção: se o usuário estiver com o acesso desativado ou não for encontrado na Microsoft, será exibida uma mensagem de erro no login.

## 4.2) Sincronização de Dados

- Alterações em nome, e-mail telefone devem ser feitas na Microsoft e serão sincronizadas no Ploomes de forma automática, podendo levar até 5 minutos para a atualização dos dados.

- Novos usuários criados na Microsoft e vinculados ao Entra ID serão importados e atribuídos a um novo perfil nomeado como “**MicrosoftSSO”**, com permissões equivalentes ao perfil padrão **Funcionário**.

- Se um e-mail já existir no Ploomes vinculado a um usuário, ele será atualizado. Caso esteja vinculado a outra conta, será exibido um alerta e o usuário não será criado.
- A sincronização ocorre via webhooks de forma automática, e o tempo para que a atualização dos dados ocorra no Ploomes pode levar até 5 minutos
- A sincronização também pode ser acionada manualmente pelo usuário de perfil administrador através do botão “Atualizar integração”, e o tempo para que a atualização dos dados ocorra no Ploomes pode levar até 5 minutos

  [GIF animado: Imagem 5: A sincronização também pode ser acionada manualmente pelo usuário de perfil administrador através do botão “Atualizar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1624142324/bb52bdcdbaa5d35beda0c9b77179/Ploomes-_-Administra-C3-A7-C3-A3o-Google-Chrome-2025-07-16-15-01-49-_online-video-cutter_com_-_1_.gif?expires=1786536000&signature=8a75df8a4ab0cf8a3fd0e4cef1da7ad766a148bc64ac9efb95b4d0223e77e75a&req=dSYlEsh6n4JdXfMW3nq%2BgfwjJlRhiTd7ONeE1itWG0zCkUmSVUd6tNs8JbEK%0ArhLznt7Wt88JhyyQYJ2DSByJBAc%3D%0A)
- A alteração do status de um usuário (habilitar/desabilitar acesso) deve ser feito pela Microsoft, e o tempo para a atualização refletir no Ploomes pode levar até 5 minutos

## 4.3) Ocultação de Fluxos Padrão

Com o **SSO** **ativo**:

- Os fluxos **“Recuperar Acesso”** e **“Alterar Senha”** são ocultados.
- Edição de dados cadastrais do usuário e desativação de acesso ao Ploomes só podem ser feitos via Microsoft.
- Ao desativar o SSO, os fluxos mencionados serão reexibidos no Ploomes.

## 4.4) Desativando a Integração

1. Acesse **Administração > Integrações Plug and Play**
2. Clique em **Desligar Integração**
3. O sistema retornará ao fluxo tradicional de login por e-mail e senha
4. Todos os usuários receberão um e-mail com link para criação de nova senha

⚠️ Atenção: usuários que não criarem uma nova senha não conseguirão acessar o sistema até completar esse processo

[GIF animado: Imagem 6: ⚠️ Atenção: usuários que não criarem uma nova senha não conseguirão acessar o sistema até completar esse processo](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1624159150/b31c0e39b93bc0b7caf8e71c2082/Ploomes-_-Administra%C3%A7%C3%A3o-Google-Chrome-2025-07-16-17-38-19-_online-video-cutter_com_.gif?expires=1786536000&signature=b24afea8e529dc6c3dcb76dada97f64ef538884a8e6819c22065dcdf705b815b&req=dSYlEsh7lIBaWfMW3nq%2BgWNrpUbRbpkzJ7o%2B8X3hUtUz8EGnMNhhChst8ffm%0A2jz6e8EJoXTZZUEpAsJJDFKAWCA%3D%0A)

## 5) Limitações da Integração Microsoft SSO

- ### Conflito de contas

  Contas com o mesmo e-mail vinculadas a diferentes organizações não poderão ser integradas simultaneamente. O sistema exibirá uma mensagem listando as contas não integradas.

- ### Desativação de um usuário

  Ao desativar um usuário na Microsoft, o sistema levará cerca de 5 minutos para bloquear o acesso do usuário no Ploomes.

- ### Atualizações de dados de um usuário

  Ao atualizar um usuário na Microsoft, o sistema pode levar cerca de 15 minutos para atualizar as informações no Ploomes.

---

## 6) Glossário

- **SSO (Single Sign-On):**

  Mecanismo de autenticação que permite acesso a múltiplos sistemas com uma única credencial.

- **Entra ID (antigo Azure AD):**

  Plataforma de gerenciamento de identidade da Microsoft, utilizada para autenticação corporativa.

- **Integração Plug and Play:**

  Interface do Ploomes onde os administradores podem ativar/desativar integrações com outras plataformas.

---

## 7) F.A.Q.

- #### Consigo utilizar a senha comum de acesso ao Ploomes após ativar o SSO?

  Não. As senhas do Ploomes serão desativadas e os usuários utilizarão apenas suas credenciais Microsoft.
- #### O que acontece se um usuário for desativado na Microsoft?

  O acesso ao Ploomes será automaticamente bloqueado para esse usuário.
- #### Posso editar os dados dos usuários pelo Ploomes?

  Apenas permissões e vinculação a equipes podem ser editadas. Dados cadastrais como telefone, nome e e-mail só podem ser alterados via Microsoft.
- #### O que acontece se desativar o SSO?

  Quando o SSO for desativado, o login passará a ser realizado com as credenciais Ploomes (e-mail e senha). O sistema enviará um e-mail para todos os usuários com um link para criar uma nova senha de acesso.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com)
