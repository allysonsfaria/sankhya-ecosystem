---
id: "44010300677015"
titulo: "Como receber dados da Meetime em outros sistemas utilizando o Make"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010300677015-Como-receber-dados-da-Meetime-em-outros-sistemas-utilizando-o-Make"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:35:15Z"
rotulos: ["sync_hc", "meetime", "meetime_334", "sync_hash_4a2cc0fa7f35"]
---

# Como receber dados da Meetime em outros sistemas utilizando o Make

Make é uma ferramenta de automação que conecta sistemas e executa fluxos automáticos. Para usar essa ação, basta ter uma conta no Make e uma conta na Meetime com perfil de administrador ou gestor. Com isso configurado, o Make consegue receber ou enviar dados e executar o fluxo conforme os eventos definidos.

### Como criar a automação

1. Antes de tudo, será necessário que você possua uma conta no [Make](https://www.make.com/en). Já no sistema, você deverá clicar no menu “**Scenarios” > Create a new scenario** (nome dado para o ambiente onde integrações são construídas por lá):

![Imagem 1: Antes de tudo, será necessário que você possua uma conta no Make . Já no sistema, você deverá clicar no menu “…](https://ajuda.sankhya.com.br/hc/article_attachments/44010333203863)

1. Na etapa inicial, você deverá pesquisar por “**Webhook**” (sem aspas) e escolher a opção “**Custom webhook**”:

![Imagem 2: Na etapa inicial, você deverá pesquisar por “ Webhook ” (sem aspas) e escolher a opção “ Custom webhook ”:](https://ajuda.sankhya.com.br/hc/article_attachments/44010283858583)

1. Após isso, clique para **criar um webhook**, escolha um nome e salve:

![Imagem 3: Após isso, clique para criar um webhook , escolha um nome e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/44010284149911)

1. O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão "**copy adddres to clipboard**" e inseri-lo na Meetime:

![Imagem 4: O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão "…](https://ajuda.sankhya.com.br/hc/article_attachments/44010321980567)

## Na Meetime

Na sua conta da Meetime, através de um usuário **Gestor** ou **Administrador**, siga os seguintes passos:

1. Clique [aqui](https://meetime.com.br/dashboard/integrations/webhooks) > botão verde de “+” para **adicionar um Webhook**

![Imagem 5: Clique aqui > botão verde de “+” para adicionar um Webhook](https://ajuda.sankhya.com.br/hc/article_attachments/44010302084119)

1. Selecione o “**Evento**” conforme a integração que você deseja construir no Make (quais dados o outro sistema deve receber)
2. Em “URL Destino”, coloque o **endereço trazido do Make** (atenção para que o início “https://” não fique duplicado)
3. Salvar

![Imagem 6: Salvar](https://ajuda.sankhya.com.br/hc/article_attachments/44010302317591)

É **importante** que você utilize um lead teste da conta e realize o evento que você escolheu no passo 2, como por exemplo fazer uma atividade do flow (caso você tenha escolhido o evento “Atividade Flow Feita”).

## Teste de funcionalidade

Depois desses passos, de volta no Make, clique em “Run once” no rodapé da página para testar o recebimento dos dados:

![Imagem 7: Depois desses passos, de volta no Make, clique em “Run once” no rodapé da página para testar o recebimento dos dados:](https://ajuda.sankhya.com.br/hc/article_attachments/44010318669207)

Por fim, clique para sair do modal que apresenta os dados recebidos e depois no ícone de “+” para criar o próximo módulo, onde você selecionará a ferramenta para onde os dados devem ir e seguir com as configurações da integração como desejado.

![Imagem 8: Por fim, clique para sair do modal que apresenta os dados recebidos e depois no ícone de “+” para criar o próximo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010285249047)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
