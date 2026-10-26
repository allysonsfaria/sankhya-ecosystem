---
id: "360045094273"
titulo: "Melhores práticas para configuração de conexão JDBC no iReport"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094273-Melhores-pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-de-conex%C3%A3o-JDBC-no-iReport"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T15:51:21Z"
rotulos: ["Configuração", "Relatórios", "iReport", "Conexão JDBC no iReport", "Banco de Dados", "JDBC"]
---

# Melhores práticas para configuração de conexão JDBC no iReport

O iReport é uma ferramenta open source para desenvolvimento de relatórios, para conecta-lo a um banco de dados utilizamos uma conexão JDBC. Java Database Connectivity ou JDBC é um conjunto de classes e interfaces (API) escritas em Java que fazem o envio de instruções SQL para qualquer banco de dados relacional.

Para cada banco de dados há um driver JDBC, normalmente utilizamos **com.microsoft.sqlserver.jdbc.SQLServerDriver**para **MS SQL Server** e e**oracle.jdbc.driver.OracleDriver** para **ORACLE**, que respectivamente são disponibilizados nos arquivos **sqljdbc.jar**e **ojdbc14.jar** no <http://downloads.sankhya.com.br>

**Adicionando um .jar no classpath do iReport**

O primeiro passo antes de criar uma conexão é inserir no **classpath**do **iReport** o jar que contem o Driver que iremos utilizar. Na barra (superior) de menu: **Opções >> Classpath**, clique em “Adicionar Jar” e navegue até o local onde está o arquivo (sqljdbc.jar e/ou ojdbc14.jar ) e adcione-o. Clique em **“Salvar Classpath”**

**Criando uma nova conexão**

Na barra (superior) de menu: **Data >> Conexões / Banco de Dados,** em seguida clique em **“Novo”, “Conexão de Banco de  Dados JDBC”.**

**Em “Propriedades de Conexão”**:

1. Insira um nome (à sua escolha) em “Nome”
2. Selecione a Driver utilizado.
3. Insira a String de conexão em “Caminho do JDBC”
4. Preencha usuário e senha.

**String de Conexão para MS SQL Server utilizando o driver com.microsoft.sqlserver.jdbc.SQLServerDriver**

**jdbc:sqlserver://HOST\_OU\_IP\_DO\_BANCO:PORTA;instanceName=NOME\_DA\_INSTANCIA;
databaseName=NOMSE\_BD;lastUpdateCount=true**

**Observação:** Caso não exista instancia nomeada retire o **instanceName=NOME\_DA\_INSTANCIA**. Se a porta for a porta padrão 1433 não coloque  **:PORTA**. retire-o também. Não esqueça de preencher o usuário e senha.

**String de Conexão para Oracle utilizando o driver oracle.jdbc.driver.OracleDriver**

**jdbc:oracle:thin:@HOST\_OU\_IP\_DO\_BANCO:PORTA:SID**

Observação: Todas os dados  (host, porta e SID) devem ser informados. SID  (Service ID) é o que chamamos de serviço,  por padrão é ORCL ou XE, mas confirme se a base não está num serviço que não um destes.

**Clique em “Teste” para testar a conexão, antes de sava-la.**

**Um erro comum:**

O teste de conexão permite que tenhamos a certeza que a conexão salva está funcionando, se durante o teste ocorrer o erro a cima significa que não existe o driver JDBC escolhido não está no classpath do iReport. Isso porque:

![Imagem 1: O driver escolhido (Figura “Propriedade de Conexão” item 2) não é um dos dois driver citados (…](https://ajuda.sankhya.com.br/hc/article_attachments/19196198463255) O driver escolhido (Figura “Propriedade de Conexão” item 2) não é um dos dois driver citados (com.microsoft.sqlserver.jdbc.SQLServerDriver ou oracle.jdbc.driver.OracleDriver) 

![Imagem 2: O driver escolhido (Figura “Propriedade de Conexão” item 2) não é um dos dois driver citados (…](https://ajuda.sankhya.com.br/hc/article_attachments/19196198469399) O jar que contém o Driver não foi colocado no classpath do iReport conforme o tópico “Adicionando um .jar no classpath do iReport”

Vale ressaltar que o tanto do iReport quanto os Drivers (.jar) podem ser baixados no [**http://downloads.sankhya.com.br**](http://downloads.sankhya.com.br)
