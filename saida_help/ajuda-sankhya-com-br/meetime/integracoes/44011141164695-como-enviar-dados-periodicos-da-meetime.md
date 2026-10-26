---
id: "44011141164695"
titulo: "Como enviar dados periódicos da Meetime para o Power BI utilizando o Make"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011141164695-Como-enviar-dados-peri%C3%B3dicos-da-Meetime-para-o-Power-BI-utilizando-o-Make"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:57:29Z"
rotulos: ["sync_hc", "meetime", "meetime_1090", "sync_hash_de3fafa36be3"]
---

# Como enviar dados periódicos da Meetime para o Power BI utilizando o Make

O **Make** é uma ferramenta de automação que conecta sistemas e executa fluxos automáticos. Para usar com a Meetime, é necessário:

• Conta no Make;
• Conta na Meetime com perfil de administrador ou gestor.

A forma mais simples é usar o Google Sheets como intermediário.

**Fluxo recomendado**

Meetime → Google Sheets → Power BI

**✅ Formas de envio**

Os dados podem ser enviados de duas maneiras:

• Em tempo real, via Webhook
• De forma periódica, via requisições HTTP usando a API

Neste artigo, explicaremos o envio periódico. Caso queira entender como enviar dados em tempo real, basta acessar esse artigo:

👉 [Como enviar dados em tempo real da Meetime para o Power BI utilizando o Make](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1772673041-como-enviar-dados-em-tempo-real-da-meetime-para-o-power-bi-utilizando-o-make)

## Envio periódico usando endpoints da API

1 - No primeiro módulo do cenário, você deve buscar por **HTTP > Make a request**. No primeiro campo **"Authentication Type"**, selecione **"No authentication":**

![Imagem 1: 1 - No primeiro módulo do cenário, você deve buscar por HTTP > Make a request . No primeiro campo "Authentication Type"…](https://ajuda.sankhya.com.br/hc/article_attachments/44011141380119)

2 - No campo URL, você precisa **adicionar a URL do endpoint que deseja utilizar**. Essa informação pode ser tirada na [nossa documentação](https://meetime.readme.io/reference/introdu%C3%A7%C3%A3o). Nesse caso, estamos utilizando o endpoint de Listar Prospecções. A URL está disponível logo no início da página:

![Imagem 2: 2 - No campo URL, você precisa adicionar a URL do endpoint que deseja utilizar . Essa informação pode ser tirada na…](https://ajuda.sankhya.com.br/hc/article_attachments/44011132983447)

3 - Em **"Method"** selecione **"GET"**. A próxima etapa são adicionar os dois Headers necessários para a requisição funcionar corretamente. Para adicionar, basta clicar em **"Add a header":**

![Imagem 3: 3 - Em "Method" selecione "GET" . A próxima etapa são adicionar os dois Headers necessários para a requisição funcionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44011154667031)

**4 - Preenchimento dos Headers:**

Preenchimento do **"Header 1":**

**Name:** "Authorization"

**Value:** Preencher com o seu token de API da Meetime. Esse artigo te mostra [Como encontrar seu token de API na Meetime](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768839869-como-encontrar-seu-token-de-api-na-meetime).

![Imagem 4: Value: Preencher com o seu token de API da Meetime. Esse artigo te mostra Como encontrar seu token de API na Meetime .](https://ajuda.sankhya.com.br/hc/article_attachments/44011183781655)

Preenchimento do **"Header 2":**

**Name:** "Accept"

**Value:** "application/json"

![Imagem 5: Value: "application/json"](https://ajuda.sankhya.com.br/hc/article_attachments/44011155114007)

Na sequência, **volte ao Make** para finalizar a integração com o **Google Sheets:**

1 - Para integrar, passe o mouse sobre o cenário de HTTP que você criou e **clique no símbolo de mais para adicionar outro módulo**:

![Imagem 6: 1 - Para integrar, passe o mouse sobre o cenário de HTTP que você criou e clique no símbolo de mais para adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44011217907479)

2 - Clique em **"Add"** para iniciar a integração. Em seguida, clique em Fazer login com o Google, **selecione a conta desejada, revise as permissões com atenção e clique em Continuar:**

![Imagem 7: 2 - Clique em "Add" para iniciar a integração. Em seguida, clique em Fazer login com o Google, selecione a conta…](https://ajuda.sankhya.com.br/hc/article_attachments/44011155574295)

3 - Preenchimento dos campos seguintes:

- **Search Method:** selecione search by path;
- **Drive:** selecione my drive;
- **Spreadsheet ID:** pesquise pelo nome da planilha para qual esses dados serão enviados e clique em selecionar;
- **Unformatted:** esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos exatamente como chegam, sem que o Google Sheets aplique formatação automática. Ao selecionar Não, o Sheets aplica o formato padrão. Escolha conforme a sua necessidade.

![Imagem 8: Unformatted: esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/44011184648087)

4 - Para finalizar, **associe os campos dos leads às colunas da planilha**. Em Sheet Name, selecione a aba que vai receber os dados, clique sobre o nome de cada coluna e arraste o campo correspondente da Meetime até ela:

![Imagem 9: 4 - Para finalizar, associe os campos dos leads às colunas da planilha . Em Sheet Name, selecione a aba que vai receber…](https://ajuda.sankhya.com.br/hc/article_attachments/44011155901975)

## Conectando o Google Sheets ao Power BI

### 1 - Publicando a planilha no Google Sheets

Para que o Power BI consiga consumir os dados corretamente, é necessário gerar um link público no formato CSV. Seguindo o procedimento abaixo:

1. Abra a planilha no Google Sheets
2. No menu superior, clique em Arquivo
3. Selecione Compartilhar
4. Clique em Publicar na web
5. Escolha a aba correta que contém os dados
6. Selecione o formato CSV
7. Clique em Publicar
8. Copie o link gerado

![Imagem 10: Copie o link gerado](https://ajuda.sankhya.com.br/hc/article_attachments/44011169947927)

Esse link será utilizado no Power BI Desktop para realizar a conexão via Web.

Importante destacar que o link utilizado deve ser o link de publicação em CSV. O link padrão de compartilhamento da planilha não funcionará para esse tipo de integração.

### 2 - Conectando a planilha ao Power BI Desktop

Com o link da planilha publicado no formato CSV, o próximo passo é realizar a conexão dentro do Power BI Desktop.

Siga o procedimento abaixo:

1. Abra o Power BI Desktop
2. Clique em Obter Dados
3. Selecione a opção Web

![Imagem 11: Selecione a opção Web](https://ajuda.sankhya.com.br/hc/article_attachments/44011194380439)

1. Cole o link CSV gerado no Google Sheets
2. Clique em OK

![Imagem 12: Clique em OK](https://ajuda.sankhya.com.br/hc/article_attachments/44011194551703)

O Power BI irá reconhecer automaticamente o conteúdo como um arquivo CSV.

## Após a pré visualização dos dados

Assim que o Power BI exibir a pré visualização da planilha, você terá duas opções:

### Opção 1 - Transformar Dados

✅ Indicado quando há necessidade de validação ou tratamento prévio das informações.

Utilize essa opção para verificar e ajustar tipos de dados, renomear colunas, remover colunas desnecessárias, tratar valores nulos e aplicar regras no Power Query.

Após realizar os ajustes, clique em **Fechar e Aplicar** para carregar os dados no modelo.

### Opção 2 - Fechar e Aplicar

✅ Indicado quando a planilha já está estruturada corretamente.

Ao selecionar essa opção, os dados serão carregados diretamente no modelo do Power BI, ficando imediatamente disponíveis para criação de medidas, modelagem, construção de relatórios e dashboards.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
