---
id: "44010204073111"
titulo: "Como enviar dados da Meetime para o Google Sheets utilizando o Make"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010204073111-Como-enviar-dados-da-Meetime-para-o-Google-Sheets-utilizando-o-Make"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:33:12Z"
rotulos: ["sync_hc", "meetime", "meetime_333", "sync_hash_16abc5ec0292"]
---

# Como enviar dados da Meetime para o Google Sheets utilizando o Make

Make é uma ferramenta de automação que conecta sistemas e executa fluxos automáticos. Para usar essa ação, basta ter uma conta no Make e uma conta na Meetime com perfil de administrador ou gestor. Com isso configurado, o Make consegue receber ou enviar dados e executar o fluxo conforme os eventos definidos.

Existem duas maneiras de receber esses dados: **enviando em tempo real via Webhook** ou **buscando de forma periódica usando o módulo HTTP com os endpoints da API**. A seguir, detalharemos cada uma dessas opções:

## Envio em tempo real (Webhook)

1. Antes de tudo, será necessário que você possua uma conta no [Make](https://www.make.com/en). Já no sistema, você deverá clicar no menu “**Scenarios” > Create a new scenario** (nome dado para o ambiente onde integrações são construídas por lá):

![Imagem 1: Antes de tudo, será necessário que você possua uma conta no Make . Já no sistema, você deverá clicar no menu “…](https://cloudchat2.cloudhumans.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBL2dwQ3c9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--dde7668ac4e3505cfaa012565a8b352c38b8a144/image.png)

1. Na etapa inicial, você deverá pesquisar por “**Webhook**” (sem aspas) e escolher a opção “**Custom webhook**”:

![Imagem 2: Na etapa inicial, você deverá pesquisar por “ Webhook ” (sem aspas) e escolher a opção “ Custom webhook ”:](https://ajuda.sankhya.com.br/hc/article_attachments/44010215781911)

1. Após isso, clique para **criar um webhook**, escolha um nome e salve:

![Imagem 3: Após isso, clique para criar um webhook , escolha um nome e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/44010216112151)

1. O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão "**copy adddres to clipboard**" e inseri-lo na Meetime:

![Imagem 4: O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão "…](https://ajuda.sankhya.com.br/hc/article_attachments/44010216467095)

Na Meetime

Na sua conta da Meetime, através de um usuário **Gestor** ou **Administrador**, siga os seguintes passos:

1. Clique [aqui](https://meetime.com.br/dashboard/integrations/webhooks) > botão verde de “+” para **adicionar um Webhook**

![Imagem 5: Clique aqui > botão verde de “+” para adicionar um Webhook](https://ajuda.sankhya.com.br/hc/article_attachments/44010231504279)

1. Selecione o “**Evento**” conforme a integração que você deseja construir no Make (quais dados o outro sistema deve receber)
2. Em “URL Destino”, coloque o **endereço trazido do Make** (atenção para que o início “https://” não fique duplicado)
3. Salvar

![Imagem 6: Salvar](https://ajuda.sankhya.com.br/hc/article_attachments/44010217174039)

Na sequência, **volte ao Make** para finalizar a integração com o **Google Sheets:**

1. Para integrar, passe o mouse sobre o cenário de webhook que você criou e **clique no símbolo de mais para adicionar outro módulo**:

![Imagem 7: Para integrar, passe o mouse sobre o cenário de webhook que você criou e clique no símbolo de mais para adicionar outro…](https://ajuda.sankhya.com.br/hc/article_attachments/44010232194327)

1. Clique em **"Add"** para iniciar a integração. Em seguida, clique em Fazer login com o Google, **selecione a conta desejada, revise as permissões com atenção e clique em Continuar:**

![Imagem 8: Clique em "Add" para iniciar a integração. Em seguida, clique em Fazer login com o Google, selecione a conta desejada,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010232553751)

**3. Preenchimento dos campos seguintes:**

- **Search Method:** selecione search by path;
- **Drive:** selecione my drive;
- **Spreadsheet ID:** pesquise pelo nome da planilha para qual esses dados serão enviados e clique em selecionar;
- **Unformatted:** esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos exatamente como chegam, sem que o Google Sheets aplique formatação automática. Ao selecionar Não, o Sheets aplica o formato padrão. Escolha conforme a sua necessidade.

![Imagem 9: Unformatted: esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010201682711)

1. Para finalizar, **associe os campos dos leads às colunas da planilha**. Em Sheet Name, selecione a aba que vai receber os dados, clique sobre o nome de cada coluna e arraste o campo correspondente da Meetime até ela:

![Imagem 10: Para finalizar, associe os campos dos leads às colunas da planilha . Em Sheet Name, selecione a aba que vai receber os…](https://ajuda.sankhya.com.br/hc/article_attachments/44010236445847)

Para testar, clique em "**Executar"** e verifique se os dados foram retornados com sucesso. Em seguida, abra a planilha e confirme se as informações foram enviadas corretamente:

![Imagem 11: Para testar, clique em " Executar" e verifique se os dados foram retornados com sucesso. Em seguida, abra a planilha e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010233604375)

**❗Dica:** Para definir o período de execução da automação, clique em Immediately as data arrives, na parte inferior, e selecione quando ela será executada e o intervalo em minutos entre cada execução.

![Imagem 12: ❗Dica: Para definir o período de execução da automação, clique em Immediately as data arrives, na parte inferior, e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010253074327)

## Envio periódico usando endpoints da API

Na nossa documentação da API temos diversos endpoints que podem ser utilizados para extrair informações da Meetime para outras ferramentas, como: listar prospecções, atividades, cadências. Você pode conferir a documentação completa acessando esse link: [Documentação API](https://meetime.readme.io/reference/introdu%C3%A7%C3%A3o). Para exemplificar o uso, estaremos utilizando o endpoint de [Listar Prospecções.](https://meetime.readme.io/reference/listarprospeces)

O primeiro passo é semelhante ao processo de enviar informações via Webhook. Você irá criar um novo cenário clicando no menu “**Scenarios” > Create a new scenario.**

1. No primeiro módulo do cenário, você deve buscar por **HTTP > Make a request**. No primeiro campo **"Authentication Type"**, selecione **"No authentication":**

![Imagem 13: No primeiro módulo do cenário, você deve buscar por HTTP > Make a request . No primeiro campo "Authentication Type" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010207917719)

1. No campo URL, você precisa **adicionar a URL do endpoint que deseja utilizar**. Essa informação pode ser tirada na [nossa documentação](https://meetime.readme.io/reference/introdu%C3%A7%C3%A3o). Nesse caso, estamos utilizando o endpoint de Listar Prospecções. A URL está disponível logo no início da página:

![Imagem 14: No campo URL, você precisa adicionar a URL do endpoint que deseja utilizar . Essa informação pode ser tirada na nossa…](https://ajuda.sankhya.com.br/hc/article_attachments/44010253744535)

1. Em **"Method"** selecione **"GET"**. A próxima etapa são adicionar os dois Headers necessários para a requisição funcionar corretamente. Para adicionar, basta clicar em **"Add a header":**

![Imagem 15: Em "Method" selecione "GET" . A próxima etapa são adicionar os dois Headers necessários para a requisição funcionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010238072599)

Preenchimento do **"Header 1":**

**Name:** "Authorization"

**Value:** Preencher com o seu token de API da Meetime. Esse artigo te mostra [Como encontrar seu token de API na Meetime](https://suporte.meetime.com.br/hc/pt-br/articles/meetime.zendesk.com/hc/pt-br/articles/26604018404505/live_preview/01KC530E17BXWJH3JRD7NPQ2YS).

![Imagem 16: Value: Preencher com o seu token de API da Meetime. Esse artigo te mostra Como encontrar seu token de API na Meetime .](https://ajuda.sankhya.com.br/hc/article_attachments/44010235444503)

Preenchimento do **"Header 2":**

**Name:** "Accept"

**Value:** "application/json"

![Imagem 17: Value: "application/json"](https://ajuda.sankhya.com.br/hc/article_attachments/44010227128087)

Na sequência, **volte ao Make** para finalizar a integração com o **Google Sheets:**

1. Para integrar, passe o mouse sobre o cenário de webhook que você criou e **clique no símbolo de mais para adicionar outro módulo**:

![Imagem 18: Para integrar, passe o mouse sobre o cenário de webhook que você criou e clique no símbolo de mais para adicionar outro…](https://ajuda.sankhya.com.br/hc/article_attachments/44010271488407)

1. Clique em **"Add"** para iniciar a integração. Em seguida, clique em Fazer login com o Google, **selecione a conta desejada, revise as permissões com atenção e clique em Continuar:**

![Imagem 19: Clique em "Add" para iniciar a integração. Em seguida, clique em Fazer login com o Google, selecione a conta desejada,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010261451031)

**3. Preenchimento dos campos seguintes:**

- **Search Method:** selecione search by path;
- **Drive:** selecione my drive;
- **Spreadsheet ID:** pesquise pelo nome da planilha para qual esses dados serão enviados e clique em selecionar;
- **Unformatted:** esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos exatamente como chegam, sem que o Google Sheets aplique formatação automática. Ao selecionar Não, o Sheets aplica o formato padrão. Escolha conforme a sua necessidade.

![Imagem 20: Unformatted: esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010210011415)

1. Para finalizar, **associe os campos dos leads às colunas da planilha**. Em Sheet Name, selecione a aba que vai receber os dados, clique sobre o nome de cada coluna e arraste o campo correspondente da Meetime até ela:

![Imagem 21: Para finalizar, associe os campos dos leads às colunas da planilha . Em Sheet Name, selecione a aba que vai receber os…](https://ajuda.sankhya.com.br/hc/article_attachments/44010210316567)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
