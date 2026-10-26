---
id: "44010581091095"
titulo: "Configuração de Whitelist no Google Workspace"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010581091095-Configura%C3%A7%C3%A3o-de-Whitelist-no-Google-Workspace"
trilha: "Meetime > Configurações"
atualizado_em: "2026-10-05T18:41:27Z"
rotulos: ["sync_hc", "meetime", "meetime_369", "sync_hash_cd390ddd07b9"]
---

# Configuração de Whitelist no Google Workspace

Devido às [atualizações nas políticas de privacidade do Google](https://www.cnet.com/news/google-fined-57-million-under-european-privacy-law/), aplicações que acessam dados de contas Google precisarão de uma nova autorização para obter e manuseá-los.

Em função disso, para integrar sua conta de e-mail e calendar do google é necessário configurar um whitelist para a aplicação da Meetime. O processo é simples e as instruções estão descritas abaixo.

A Meetime faz a integração com a sua conta Google para enviar os e-mails pelo Flow (lembretes e link da sala).

Instruções para autenticar o whitelist:

## Atenção: Somente um usuário "SuperAdmin" poderá fazer a configuração

1. Acesse o admin do Google Workplace em [https://admin.google. com/](https://admin.google.com/)
2. Entre no menu **Security** **(Segurança) >** **Access and data controls (Controle de dados e acesso)** > **API Controls (Controle de API).**

   ![Imagem 1: Entre no menu Security (Segurança) > Access and data controls (Controle de dados e acesso) > API Controls (Controle de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010592411287)
3. Na tela de API Controls clique em **Manage Third-Party App Access (Gerenciar o acesso dos apps).**

   ![Imagem 2: Na tela de API Controls clique em Manage Third-Party App Access (Gerenciar o acesso dos apps).](https://ajuda.sankhya.com.br/hc/article_attachments/44010581683351)
4. No cabeçalho da tabela, clique em **Add app (Configurar novo app)**

   ![Imagem 3: No cabeçalho da tabela, clique em Add app (Configurar novo app)](https://ajuda.sankhya.com.br/hc/article_attachments/44010581939223)
5. No campo de texto digite o ID (sem espaços)
   `680613858090-ss0at3srqupf6dt8khsrmk9d4e07nm70.apps.googleusercontent.com`
   e clique em **Search (Pesquisar) .**

   ![Imagem 4: No campo de texto digite o ID (sem espaços) 680613858090-ss0at3srqupf6dt8khsrmk9d4e07nm70.apps.googleusercontent.com e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010597189783)
6. Nos resultados, passe o mouse na opção com o logo da Meetime e clique em **Select**. Se a busca não apresentar resultados verifique se você copiou o ID do passo 5 corretamente e tente novamente.
7. Selecione a opção correspondente ao ID da Meetime e clique no nome da Meetime (imagem abaixo).

   ![Imagem 5: Selecione a opção correspondente ao ID da Meetime e clique no nome da Meetime (imagem abaixo).](https://ajuda.sankhya.com.br/hc/article_attachments/44010597413527)
8. Em **Scope (Escopo)** selecione a primeira opção All users (Todos em Meetime)

   ![Imagem 6: Em Scope (Escopo) selecione a primeira opção All users (Todos em Meetime)](https://ajuda.sankhya.com.br/hc/article_attachments/44010597681175)
9. Em Acesso aos dados do Google, escolha a opção **Trusted: Can access all Google services** e clique em **Configure** (imagem abaixo).

   ![Imagem 7: Em Acesso aos dados do Google, escolha a opção Trusted: Can access all Google services e clique em Configure (imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/44010583006103)

Essa opção é uma exigência do **Nylas** e do **Google**, pois o Google só permite acesso às informações necessárias para que o Nylas possa operar e metrificar os e-mails nesse módulo de acesso completo.

Pronto! A whitelist está configurada e a integração com o Google já pode ser utilizada normalmente.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
