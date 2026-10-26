---
id: "33606598418327"
titulo: "Como configurar e gerar o EDI DOCCOB e CONEMB?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33606598418327-Como-configurar-e-gerar-o-EDI-DOCCOB-e-CONEMB"
trilha: "Sankhya Official Pack - SOP > TMS"
atualizado_em: "2026-07-22T14:28:46Z"
rotulos: ["CT-e", "Configuração", "EDI", "TOP", "Financeiro", "Documentos Eletrônicos"]
---

# Como configurar e gerar o EDI DOCCOB e CONEMB?

### Configurações para utilização do EDI CONEMB

#### Objetivo:

Gerar EDI no “Padrão Proceda” considerando o Layout do Manual de Layout PROCEDA. Qualquer informação adicional fora do Layout padrão é considerada a necessidade de Personalização.

#### Menu de acesso

Foi criada a pasta EDI Proceda, dentro dela a tela **"CONEMB"**.

![Imagem 1: Foi criada a pasta EDI Proceda, dentro dela a tela "CONEMB" .](https://ajuda.sankhya.com.br/hc/article_attachments/33606631336087)

Acesse o painel lateral, no qual o usuário seleciona a versão e pode preencher o filtro por período de emissão, Empresa e Parceiro Tomador e também incluir algum filtro personalizado.

![Imagem 2: Acesse o painel lateral, no qual o usuário seleciona a versão e pode preencher o filtro por período de emissão, Empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/33606598400151)

Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira incluir algum CT-e no arquivo e, após isto, clicar em **"Gerar Arquivo"**.

![Imagem 3: Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira…](https://ajuda.sankhya.com.br/hc/article_attachments/33606598401943)

Depois que o arquivo é gerado, escolha o local no qual irá salvá-lo.

#### Configurações na TOP de CTE

Alguns campos do layout receberam configuração adicional, como **"Classificação do tipo de CT-e"**. Assim, foi criado o campo **"Tipo documento proceda",** na tela **"Tipos de Operação - TOP",** para indicar  se a TOP é utilizada para uma das opções disponíveis no arquivo.

![Imagem 4: Alguns campos do layout receberam configuração adicional, como "Classificação do tipo de CT-e" . Assim, foi criado o…](https://ajuda.sankhya.com.br/hc/article_attachments/33606598403607)

Para o tipo do Veículo também foi criado o campo **"Tipo Meio de Transporte Proceda",** na tela **"Composição de Veículos",** a fim de classificar o veículo conforme parâmetros do layout do CONEMB.

![Imagem 5: Para o tipo do Veículo também foi criado o campo "Tipo Meio de Transporte Proceda", na tela "Composição de Veículos", a…](https://ajuda.sankhya.com.br/hc/article_attachments/33606631342103)

#### Agendamento de geração do EDI CONEMB

Foi incluído o botão para agendar a geração automática de arquivos na tela CONEMB.

![Imagem 6: Foi incluído o botão para agendar a geração automática de arquivos na tela CONEMB .](https://ajuda.sankhya.com.br/hc/article_attachments/33608397409559)

Ao clicar neste botão, é apresentado um popup para criar os agendadores.

![Imagem 7: Ao clicar neste botão, é apresentado um popup para criar os agendadores.](https://ajuda.sankhya.com.br/hc/article_attachments/33606598406551)

É possível incluir vários agendadores e cada com com suas configurações separadas:

![Imagem 8: É possível incluir vários agendadores e cada com com suas configurações separadas:](https://ajuda.sankhya.com.br/hc/article_attachments/33606598408215)

#### Passo a passo para geração do Arquivo EDI DOCCOB

Foi incluído no diretório EDI Proceda, a tela **"DOCCOB"**

![Imagem 9: Foi incluído no diretório EDI Proceda, a tela "DOCCOB"](https://ajuda.sankhya.com.br/hc/article_attachments/33608397415703)

Nesta tela há um painel lateral, no qual é possível selecionar a versão, preencher o filtro por período de Negociação, Empresa e Parceiro e também incluir algum filtro personalizado.

Na tela serão apresentados apenas financeiros que possuem Nro de Duplicata e sejam de receita e não estejam baixados.

![Imagem 10: Na tela serão apresentados apenas financeiros que possuem Nro de Duplicata e sejam de receita e não estejam baixados.](https://ajuda.sankhya.com.br/hc/article_attachments/33606598410263)

Nos resultados retornados do filtro, é possível  remover os selecionados ou remover os não selecionados, caso não queira incluir algum Financeiro no arquivo e, após isto, clicar em **"Gerar Arquivo"**.

![Imagem 11: Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira…](https://ajuda.sankhya.com.br/hc/article_attachments/33606598411031)

![Imagem 12: Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira…](https://ajuda.sankhya.com.br/hc/article_attachments/33606631353623)

Foi incluído o botão para agendar a geração automática de arquivos na tela DOCCOB.

![Imagem 13: Foi incluído o botão para agendar a geração automática de arquivos na tela DOCCOB .](https://ajuda.sankhya.com.br/hc/article_attachments/33606631344023)

Ao clicar neste botão, é apresentado um popup para criar os agendadores.

![Imagem 14: Ao clicar neste botão, é apresentado um popup para criar os agendadores.](https://ajuda.sankhya.com.br/hc/article_attachments/33608384122519)

É possível incluir vários agendadores e cada com com suas configurações separadas:

![Imagem 15: É possível incluir vários agendadores e cada com com suas configurações separadas:](https://ajuda.sankhya.com.br/hc/article_attachments/33608384124055)

#### Aba Geral:

- **Cód. Agendador:** identificador do agendador;
- **Descrição:** campo para inserir uma descrição que facilite a identificação deste agendador;
- **Ativo:** indica se esta ativo ou inativo o agendador;
- **Filtro Agendador:** neste campo inclua filtros para buscar os documentos que deverão ser incluídos no arquivo. A tabela base é a TGFCAB, então, todos os campos dela estão disponíveis neste filtro. Por padrão será incluído um filtro que traga apenas os CT-es, NFS-es vinculados às viagens e cuja a data Dt Movimento seja superior a data da última geração. Desse modo, a rotina controla para sempre pegar os documentos não enviados desde a última consulta. Exemplo, se estiver configurado para ser gerado todas as segundas, a rotina vai executar na segunda pegando todos os documentos que possuam Dt Movimento maior do que a segunda-feira anterior até a segunda-feira atual.
- **Versão Proceda:** campo para informar qual versão o arquivo será gerado;
- **Usuário:** usuário que incluiu ou alterou o agendador;
- **Data Alteração:** data e hora da última alteração do agendador;
- **Diretório Destino do Arquivo:** campo para apontar em qual diretório serão criados os arquivados gerados pela execução do agendador;
- **Expressão CRON da Geração:** expressão para indicar quando deve ser gerado o arquivo.

#### Aba Processamento:

- **Status Geração:** indica se a rotina executou ou se gerou falha;
- **Data Última Geração:** data da última geração;
- **Data Próxima Execução:** considerando a expressão CRON, esta será a próxima data e horário que será executada a próxima execução;
- **Tempo Processamento:** tempo em segundos que durou o processamento e geração do arquivo;
- **Log Processamento:** caso tenhamos alguma falha, a mensagem será apresentada neste campo.

Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e segundo:

![Imagem 16: Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e…](https://ajuda.sankhya.com.br/hc/article_attachments/33608384125079)

![Imagem 17: Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e…](https://ajuda.sankhya.com.br/hc/article_attachments/33606631344023)

![Imagem 18: Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e…](https://ajuda.sankhya.com.br/hc/article_attachments/33608384122519)

![Imagem 19: Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e…](https://ajuda.sankhya.com.br/hc/article_attachments/33608384124055)![Imagem 20: Após executado o agendador, o arquivo foi gerado no diretório configurado com o nome contendo a data, hora, minuto e…](https://ajuda.sankhya.com.br/hc/article_attachments/33608384125079)

Foi criada dentro da pasta EDI Proceda a nova tela **"OCOREN"**

![Imagem 21: Foi criada dentro da pasta EDI Proceda a nova tela "OCOREN"](https://ajuda.sankhya.com.br/hc/article_attachments/33606598409239)

Ao abrir a tela é apresentada uma grade contendo as ocorrências lançadas no call center que possuam o campo **"Cód. Ocorrência Proceda"** informado.

![Imagem 22: Ao abrir a tela é apresentada uma grade contendo as ocorrências lançadas no call center que possuam o campo "Cód.…](https://ajuda.sankhya.com.br/hc/article_attachments/33608397423767)

Nesta tela há um painel lateral contendo os filtros no quais é possível selecionar a versão, período de emissão do CT-e, Empresa e Parceiro Tomador. Além de ser possível incluir uma lista de ocorrências e filtro personalizado.

Nos resultados retornados do filtro, é possível  remover os selecionados ou remover os não selecionados, caso não queira incluir alguma ocorrência no arquivo e, após isto, clicar em **"Gerar Arquivo"**.

![Imagem 23: Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira…](https://ajuda.sankhya.com.br/hc/article_attachments/33608384130967)![Imagem 24: Nos resultados retornados do filtro, é possível remover os selecionados ou remover os não selecionados, caso não queira…](https://ajuda.sankhya.com.br/hc/article_attachments/33608397425303)

Para configurar o código da ocorrência no padrão Proceda, foi incluído o novo campo na tela de "**Ocorrências do CT-e"**.

![Imagem 25: Para configurar o código da ocorrência no padrão Proceda, foi incluído o novo campo na tela de " Ocorrências do CT-e" .](https://ajuda.sankhya.com.br/hc/article_attachments/33608384132631)

Também foi incluído o agendador que vai gerar o arquivo de forma automática, considerando a data de emissão do CT-e.

![Imagem 26: Também foi incluído o agendador que vai gerar o arquivo de forma automática, considerando a data de emissão do CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/33608384135191)

![Imagem 27: Também foi incluído o agendador que vai gerar o arquivo de forma automática, considerando a data de emissão do CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/33608397423767)![Imagem 28: Também foi incluído o agendador que vai gerar o arquivo de forma automática, considerando a data de emissão do CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/33608384130967)![Imagem 29: Também foi incluído o agendador que vai gerar o arquivo de forma automática, considerando a data de emissão do CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/33608397425303)
