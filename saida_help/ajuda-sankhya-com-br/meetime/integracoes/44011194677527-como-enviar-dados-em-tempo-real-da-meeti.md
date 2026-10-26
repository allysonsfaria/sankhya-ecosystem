---
id: "44011194677527"
titulo: "Como enviar dados em tempo real da Meetime para o Power BI utilizando o Make"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011194677527-Como-enviar-dados-em-tempo-real-da-Meetime-para-o-Power-BI-utilizando-o-Make"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:58:07Z"
rotulos: ["sync_hc", "meetime", "meetime_1189", "sync_hash_c23572e15d07"]
---

# Como enviar dados em tempo real da Meetime para o Power BI utilizando o Make

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

Neste artigo, explicaremos o envio em tempo real. Caso queira entender como fazer envios periódicos, basta acessar esse artigo:

👉 [Como enviar dados periódicos da Meetime para o Power BI utilizando o Make](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1771463047-como-enviar-dados-da-meetime-para-o-power-bi-utilizando-o-make)

## Envio em tempo real (Webhook)

1 - Antes de tudo, será necessário que você possua uma conta no [Make](https://www.make.com/en). Já no sistema, você deverá clicar no menu **“Scenarios” > Create a new scenario** (nome dado para o ambiente onde integrações são construídas por lá):

![Imagem 1: 1 - Antes de tudo, será necessário que você possua uma conta no Make . Já no sistema, você deverá clicar no menu…](https://ajuda.sankhya.com.br/hc/article_attachments/44011157055895)

2 - Na etapa inicial, você deverá pesquisar por **“Webhook”** (sem aspas) e escolher a opção **“Custom webhook”:**

![Imagem 2: 2 - Na etapa inicial, você deverá pesquisar por “Webhook” (sem aspas) e escolher a opção “Custom webhook”:](https://ajuda.sankhya.com.br/hc/article_attachments/44011203410711)

3 - Após isso, clique para **criar um webhook**, escolha um nome e salve:

![Imagem 3: 3 - Após isso, clique para criar um webhook , escolha um nome e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/44011195380887)

4 - O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão **"copy adddres to clipboard"** e inseri-lo na Meetime:

![Imagem 4: 4 - O Make gerará um endereço para recebimento dos dados disparados pela Meetime, você pode copiá-lo clicando no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/44011220482455)

**Na Meetime**

Na sua conta da Meetime, através de um usuário **Gestor** ou **Administrador**, siga os seguintes passos:

1 - Clique [aqui](https://meetime.com.br/dashboard/integrations/webhooks) > botão verde de “+” para **adicionar um Webhook**

![Imagem 5: 1 - Clique aqui > botão verde de “+” para adicionar um Webhook](https://ajuda.sankhya.com.br/hc/article_attachments/44011171905815)

2 - Selecione o “**Evento**” conforme a integração que você deseja construir no Make (quais dados o outro sistema deve receber)

3 - Em “URL Destino”, coloque o **endereço trazido do Make** (atenção para que o início “https://” não fique duplicado)

4 - Salvar

![Imagem 6: 4 - Salvar](https://ajuda.sankhya.com.br/hc/article_attachments/44011196109079)

Na sequência, **volte ao Make** para finalizar a integração com o **Google Sheets:**

1 - Para integrar, passe o mouse sobre o cenário de webhook que você criou e **clique no símbolo de mais para adicionar outro módulo**:

![Imagem 7: 1 - Para integrar, passe o mouse sobre o cenário de webhook que você criou e clique no símbolo de mais para adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44011158423063)

2 - Clique em **"Add"** para iniciar a integração. Em seguida, clique em Fazer login com o Google, s**elecione a conta desejada, revise as permissões com atenção e clique em Continuar:**

![Imagem 8: 2 - Clique em "Add" para iniciar a integração. Em seguida, clique em Fazer login com o Google, s elecione a conta…](https://ajuda.sankhya.com.br/hc/article_attachments/44011221492631)

3 - **Preenchimento dos campos seguintes:**

- **Search Method:** selecione search by path;
- **Drive:** selecione my drive;
- **Spreadsheet ID:** pesquise pelo nome da planilha para qual esses dados serão enviados e clique em selecionar;
- **Unformatted:** esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos exatamente como chegam, sem que o Google Sheets aplique formatação automática. Ao selecionar Não, o Sheets aplica o formato padrão. Escolha conforme a sua necessidade.

![Imagem 9: Unformatted: esse campo define se a linha será inserida sem formatação. Ao selecionar Sim, os dados são inseridos…](https://ajuda.sankhya.com.br/hc/article_attachments/44011196810903)

4 - Para finalizar, **associe os campos dos leads às colunas da planilha**. Em Sheet Name, selecione a aba que vai receber os dados, clique sobre o nome de cada coluna e arraste o campo correspondente da Meetime até ela:

![Imagem 10: 4 - Para finalizar, associe os campos dos leads às colunas da planilha . Em Sheet Name, selecione a aba que vai receber…](https://ajuda.sankhya.com.br/hc/article_attachments/44011187929879)

Para testar, clique em **"Executar"** e verifique se os dados foram retornados com sucesso. Em seguida, abra a planilha e confirme se as informações foram enviadas corretamente:

![Imagem 11: Para testar, clique em "Executar" e verifique se os dados foram retornados com sucesso. Em seguida, abra a planilha e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011209390999)

**❗Dica:** Para definir o período de execução da automação, clique em Immediately as data arrives, na parte inferior, e selecione quando ela será executada e o intervalo em minutos entre cada execução.

![Imagem 12: ❗Dica: Para definir o período de execução da automação, clique em Immediately as data arrives, na parte inferior, e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011173702551)

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

![Imagem 13: Copie o link gerado](https://ajuda.sankhya.com.br/hc/article_attachments/44011174096663)

Esse link será utilizado no Power BI Desktop para realizar a conexão via Web.

Importante destacar que o link utilizado deve ser o link de publicação em CSV. O link padrão de compartilhamento da planilha não funcionará para esse tipo de integração.

### 2 - Conectando a planilha ao Power BI Desktop

Com o link da planilha publicado no formato CSV, o próximo passo é realizar a conexão dentro do Power BI Desktop.

1. Abra o Power BI Desktop
2. Clique em Obter Dados
3. Selecione a opção Web

![Imagem 14: Selecione a opção Web](https://ajuda.sankhya.com.br/hc/article_attachments/44011222844311)

1. Cole o link CSV gerado no Google Sheets
2. Clique em OK

![Imagem 15: Clique em OK](https://cloudchat2.cloudhumans.com/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBNlg1Q2c9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--ea0d6e42b1b97825dd69c59e89c266bdc7725f28/image.png)

O Power BI irá reconhecer automaticamente o conteúdo como um arquivo CSV.

## Após a pré visualização dos dados

Assim que o Power BI exibir a pré visualização da planilha, você terá duas opções:

### Opção 1 - Transformar Dados

✅ Indicado quando há necessidade de validação ou tratamento prévio das informações.

Utilize essa opção para verificar e ajustar tipos de dados, renomear colunas, remover colunas desnecessárias, tratar valores nulos e aplicar regras no Power Query.

Após realizar os ajustes, clique em **Fechar e Aplicar** para carregar os dados no modelo.

### Opção 2 - Fechar e Aplicar

✅Indicado quando a planilha já está estruturada corretamente.

Ao selecionar essa opção, os dados serão carregados diretamente no modelo do Power BI, ficando imediatamente disponíveis para criação de medidas, modelagem, construção de relatórios e dashboards.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
