---
id: "44011088033303"
titulo: "Como enviar as atividades realizadas para seu CRM via Zapier"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011088033303-Como-enviar-as-atividades-realizadas-para-seu-CRM-via-Zapier"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:54:54Z"
rotulos: ["sync_hc", "meetime", "meetime_358", "sync_hash_fcdbccf90bea"]
---

# Como enviar as atividades realizadas para seu CRM via Zapier

Antes de tudo, será necessário que você possua uma conta no Zapier.
Já no sistema, você deverá clicar para criar um “Zap”, nome dado para as integrações construídas por lá.

1. Na etapa inicial, chamada de “Trigger”, você deverá selecionar a Meetime e “Activity Finished” (feita) ou “Activity Ignored” (ignorada)
2. Na sequência, será necessário integrar a conta da Meetime que você desejará utilizar (menu “Account”) através da API Key. O próprio Zapier redirecionará para a tela do nosso sistema (basta clicar em “detalhes da API” conforme print abaixo) para que você possa pegar essa chave.

   Obs.: lembrando que apenas usuários com perfil de Administrador ou Gestor na Meetime conseguem acessá-la. Caso a chave/token não apareça na sua tela, basta solicitar a habilitação ao nosso Suporte através do e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br)
3. Na etapa seguinte, “Test”, importante seguir o procedimento abaixo antes de clicar para testar:

   - Na sua conta da Meetime, com um usuário de Administrador ou Gestor, acesse este menu e clique no botão verde de “+” para adicionar um Webhook.
   - Selecione o “Evento” conforme a integração que você está construindo no Zapier (Atividade Flow Feita ou Atividade Flow Ignorada)
   - Em “URL Destino”, você pode colocar uma URL fictícia, como <https://teste.teste.br>
   - Salvar
   - Utilizar um lead teste da conta e realizar ou ignorar uma atividade com ele (dependendo do evento selecionado no passo 2)

   Esse procedimento serve para que o webhook possa ser criado na Meetime e um lead tenha o evento em questão após isso. Dessa forma, o Zapier conseguirá puxar uma atividade exemplo assim que você clicar para testar.
4. Por fim, você deverá selecionar a ferramenta para a qual deseja enviar as atividades feita ou ignoradas em “Action” e seguir com as configurações/integrações desejadas.

   Após o Zap estar pronto e ativo, você pode deletar o Webhook que havia sido criado na tela da Meetime com a URL Destino fictícia.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
