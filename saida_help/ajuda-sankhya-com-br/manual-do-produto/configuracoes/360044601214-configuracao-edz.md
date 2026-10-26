---
id: "360044601214"
titulo: "Configuração EDZ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:10Z"
rotulos: ["manual", "Configuração", "Fiscal", "Parceiro", "Consultar EDZ", "Stored Pocedure", "br.com.sankhya.configuracao.edz", "Configuração EDZ manual", "Crédito", "Integração", "Aba Crédito", "Análise de Crédito EDZ", "Cadastro de Emitentes de Cheques sem Fundos", "Cadastro de Parceiros", "CCF", "Configuração EDZ", "EDZ Consultoria", "FTP", "Ocorrências EDZ", "Parâmetros", "Receita Federal CNPJ", "Receita Federal CPF", "Sintegra", "Configuração EDZ no Sankhya Om"]
---

# Configuração EDZ

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310752980119) Módulo: Configurações > Avançado
```

---

Esta rotina trata exclusivamente da integração do Sankhya-OM com a EDZ Consultoria. A EDZ oferece as empresas informações que apoiam a comercialização de seus produtos, fornecendo maior segurança e agilidade no relacionamento com o fisco. Através desta integração, tem-se uma ferramenta de tomada de decisões automatizadas quanto a situação de crédito de um determinado parceiro. Para mais informações sobre a EDZ Consultoria acesse <http://www.dez.com.br/edz/index.htm>.

Serão feitos os seguintes tipos de análises:

- Receita Federal CNPJ;
- Receita Federal CPF;
- Sintegra;
- CCF (Cadastro de Emitentes de Cheques sem Fundos).

Quando um determinado parceiro estiver com qualquer pendência em uma destas análises, o sistema executará as ações definidas nos [Cadastros de Ocorrências EDZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599574-Ocorr%C3%AAncias-EDZ). Uma ocorrência poderá:

- Bloquear o crédito;
- Zerar o limite de crédito;
- Alterar o grupo de autorização de crédito;
- Disparar um script de banco de dados (Stored Pocedure) que realizará tarefas mais complexas.

**Importante:** as funcionalidades desta integração não estão disponíveis para o formato HTML5.

Vejamos os detalhes acerca das configurações a serem realizadas no sistema, bem como seu consequente comportamento:

[Configuração EDZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#configuraoedz)                                                               [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#cadastrodeparceiros) 

[Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#parmetrosqueinfluenciamnestarotina)

## Configuração EDZ

Aqui são inseridos os dados referentes à conexão com o servidor FTP da empresa de consultoria, e também as preferências referentes ao comportamento desta funcionalidade.

![Imagem 2: Aqui são inseridos os dados referentes à conexão com o servidor FTP da empresa de consultoria, e também as preferências…](https://ajuda.sankhya.com.br/hc/article_attachments/4405783952919)

Preencha o campo **"Endereço de FTP"**, com o endereço e porta referentes ao servidor FTP. Depois, informe o **"Usuário FTP"** e a **"Senha FTP"**, para conectar ao servidor FTP.

No campo **"Pasta no FTP para buscar arquivos"**, indique apenas o nome da pasta disponibilizada no servidor FTP, na qual estarão contidos os arquivos abrangendo as respostas das consultas.

O campo **"Pasta no FTP para enviar arquivos"**, deve conter o nome da pasta disponibilizada no servidor FTP, a qual serão inseridos os arquivos para a consulta.

Você pode verificar o status da conexão com o servidor FTP, através do botão **"Testar FTP"**. O resultado deste teste será apresentado em uma mensagem logo a frente do botão.

O sistema é configurado para automaticamente, acessar a pasta **"buscar"** no servidor FTP e verificar o resultado das consultas solicitadas. Assim, informe no campo **"Periodicidade de busca de arquivos"**, a quantidade em minutos com que esta busca será realizada.

Tem-se também o envio das consultas pendentes de forma automática. A quantidade de minutos com que o sistema realizará o envio dos arquivos para consulta é informado no campo **"Periodicidade de envio de arquivos"**.

No campo **"Máximo de parceiros em arquivos de consulta"**, será limitada a quantidade de parceiros que estarão contidos em cada arquivo de consulta a ser enviado ao servidor FTP.

O sistema é configurado para enviar um e-mail no momento em que a consulta certifica-se de que a situação pendente foi regularizada. Para isso, informe no campo **"E-mail para notificação de crédito"**, um e-mail para notificação, e clique no botão **"Adicionar o E-mail na lista"**. Caso seja necessário o cancelar o envio de notificações para esse e-mail, selecione o e-mail  na lista, e clique no botão **"Remover os E-mails selecionados"**. Observe os dois processos, no gif abaixo:

[GIF animado: Imagem 3: O sistema é configurado para enviar um e-mail no momento em que a consulta certifica-se de que a situação pendente foi…](https://ajuda.sankhya.com.br/hc/article_attachments/4405784075671)

**Nota:** é importante configurar o envio de e-mail pelo Sankhya-Om, através da tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494-Servidor-SMTP).

As alterações efetuadas serão gravadas por meio do botão **"Salvar Configurações"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#top)

## Cadastro de Parceiros

![Imagem 4: Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/4405783939735)

No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito), temos a **"Seção EDZ"** que permite visualizar o status do envio EDZ e as diversas situações fiscais do parceiro através dos campos **"Situação na Receita Federal"**, **"Situação no CCF"**, **"Situação no Sintegra"** e **"Status envio EDZ"**. A situação fiscal do parceiro poderá ser:

- **Indefinida:** Informa que a situação fiscal não sofreu nenhuma alteração influenciada pela execução da consulta EDZ;
- **Irregular:** Indica que alguma ocorrência foi executada devido à existência de pendências retornadas pelas consultas EDZ;
- **Regular:** Aponta que as ocorrências executadas não correspondem à existência de pendências retornadas pelas consultas EDZ.

**Nota:** estes campos não permitem alterações, sendo assim, apenas para visualização de suas informações.

O campo **"Status envio EDZ"** apresentará os seguintes valores:

- **Pendente:** O envio da solicitação de consulta está aguardando para ser realizada;
- **Enviada:** O envio da solicitação de consulta já foi realizado;
- **Recebido:** O sistema já recebeu a resposta da solicitação de consulta.

Além disso, no botão Outras Opções... serão disponibilizadas as opções relacionadas à integração EDZ:

![Imagem 5: Além disso, no botão Outras Opções... serão disponibilizadas as opções relacionadas à integração EDZ :](https://ajuda.sankhya.com.br/hc/article_attachments/4405783899159)

**Ocorrências EDZ**

Esta opção quando acionada, exibe o pop-up **"Ocorrências EDZ"**, que apresenta quais ocorrências foram executadas ao longo das últimas solicitações de consultas. Ao selecionar um registro, o botão **"Visualizar registro EDZ"** apresentará os dados retornados pela consulta. Caso o registro selecionado seja referente a um CNPJ, serão apresentadas caixas de marcações para que se possa selecionar informações úteis, incrementando ou atualizando o Cadastro do Parceiro.

Ao selecionar as caixas de marcações que correspondam às informações que se deseja copiar para o Cadastro do Parceiro, acione o botão **"Transferir Campos"**. Assim, será possível executar as devidas alterações e realizar a conclusão por meio do botão **"Confirmar dados"**.

Essa funcionalidade mantém os dados dos Parceiros (Pessoa Jurídica) sempre atualizados, evitando assim, problemas referentes à fiscalização, entre outros.

**Consultar EDZ agora**

Ao acioná-la, será apresentada as opções **"Consultar todos os parceiros da grade"** e **"Consultar apenas o parceiro selecionado"**. A primeira envia uma solicitação para o servidor FTP realizar uma consulta de todos os parceiros que estão sendo apresentados na grade, a segunda apenas ao parceiro selecionado.

Ao solicitar uma destas opções, o sistema irá alterar o valor do campo **"Status envio EDZ"** para **"Pendente"**. Assim que o sistema realizar o envio da solicitação de consulta, o valor será modificado para **"Enviado"**. Ao final, a resposta da consulta é apresentada, e o campo **"Status envio EDZ"** passará a conter o valor **"Recebido"**. Deste modo, o sistema se encarregará de executar as devidas Ocorrências EDZ.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#top)

## Parâmetros que influenciam nesta rotina

No parâmetro **"Configuração de conexão com FTP EDZ - CONFFTPEDZ"**, são apresentadas as informações necessárias para conexão com o servidor FTP, sendo elas o endereço IP, a porta, o usuário e a senha.

Através do parâmetro **"Tempo em minutos para envio de arquivo EDZ - TEMPOENVEDZ"**, indique a periodização em que a rotina que envia os dados para o servidor FTP será executada.

Por meio do parâmetro "**Tempo em minutos para busca de arquivo EDZ - TEMPOBUSCAEDZ"**, determine a periodização em que a rotina de busca dos resultados da consulta no servidor FTP será executada.

No parâmetro **"Pasta no FTP EDZ para enviar arquivos - PASTAENVARQEDZ"**, indique o local no servidor FTP onde são alocados os arquivos enviados para realização da consulta.

Através do parâmetro **"Pasta no FTP EDZ para buscar arquivos - PASTAPROCARQEDZ"**, informe o local no servidor FTP onde são reservados os arquivos contendo o resultado da consulta realizada.

Indique no parâmetro **"Máximo de parceiros em arquivo de consulta EDZ - MAXLINARQEDZ"**, a quantidade de Parceiros que cada arquivo a ser enviado para a consulta EDZ deverá conter.

Por meio do parâmetro **"E-mails para notificação de crédito EDZ - EMAILNOTFEDZ"**, determine o e-mail ao qual serão enviadas as notificações dos Parceiros que regularizaram sua situação fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601214-Configura%C3%A7%C3%A3o-EDZ#top)
