---
id: "360045109733"
titulo: "Bancos de Dados - Dashboards no Sankhya Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:57Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Dashboards", "Dashboard", "Firebird", "IBM DB2", "MySQL", "Oracle", "PostgreSQL", "SQL Server", "Bancos de Dados - Dashboards no Sankhya-W manual", "Banco", "Dashboards no Sankhya Om: Conectando com Bancos de Dados", "Conexão JDBC", "Sankhya Om", "DB2"]
---

# Bancos de Dados - Dashboards no Sankhya Om

Para a criação de dashboards você pode utilizar gerenciadores de bancos de dados externos ao sistema Sankhya Om, sendo eles o PostgreSQL, Firebird, DB2 e SQL Server. No entanto, é necessário que eles estejam em suas versões mais recentes.

Para conectar com os bancos de dados, o Sankhya Om necessita do driver de conexão JDBC, para isso antes de dar início, acesse a página oficial do fabricante responsável pelo banco de dados e na área de downloads baixe a versão mais recente do driver. Feito o download, copie o Jar do driver para o servidor, no caminho $jboss\server\default\lib, em seguida no caminho $jboss\server\default\deploy configure o **"arquivo mge-ds.xml"**.

[Arquivo mge-ds.xml](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#arquivomge-ds.xml)                                  [Datasourse Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourseoracle)

[Datasource MySQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourcemysql)                                    [Datasource PostgreSQL v9.4](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourcepostgresqlv9.4)

[Datasource Firebird v2.5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourcefirebirdv2.5)                           [Datasource IBM DB2 v10.5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourceibmdb2v10.5)

[Datasource SQL Server v10.0](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#datasourcesqlserverv10.0)

**Wildfly:**

[Wildfly - Configuração...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#wildfly-configuraodedatasource)                           [Driver JDBC para conexão com o banco de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#driverjdbcparaconexocomobancodedados)

[Criação do Datasource](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#criaododatasource)                             [Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#oracle)

[MySQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#mysql)                                                          [PosgreSQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#posgresql)

[MS SQL Server](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#mssqlserver)                                           [IBM DB2](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#ibmdb2)

[Firebird](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#firebird)

## Arquivo mge-ds.xml

<?xml version="1.0" encoding="UTF-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**MGEDS**</jndi-name>

<connection-url>**jdbc:oracle:thin:@SERVIDOR:PORTA:ORCL**</connection-url>

<driver-class>**oracle.jdbc.driver.OracleDriver**</driver-class>

<user-name>Usuário</user-name>

<password>senha</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql>**select 1 from dual**</new-connection-sql>

<min-pool-size>**5**<min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

<local-tx-datasource>

**Configuração da string de conexão**

A partir desta etapa, adicione ao Datasource a configuração para conexão com banco de dados; cada banco de dados possui seu próprio padrão de conexão; citaremos o que será necessário para realizar tal configuração, sendo que todas essas configurações são inseridas em um único arquivo mge-ds.xml criado pelo próprio Sankhya Om no diretório $jboss\server\default\deploy.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasourse Oracle - Dados para conexão - Oracle

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**MGEDS**</jndi-name>

<connection-url>**jdbc:oracle:thin:@192.168.0.210:1521:ORCL**</connection-url>

<driver-class>oracle.jdbc.driver.OracleDriver</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql>**select 1 from dual**</new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasource MySQL - Dados para conexão - MySQL

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**homologaMYSQL**</jndi-name>

<connection-url>**jdbc:mysql://localhost:3306/NOME-BANCO**</connection-url>

<driver-class>**com.mysql.jdbc.Driver**</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql></new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasource PostgreSQL v9.4 - Dados para conexão - PostgreSQL

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**homologaPostgresql**</jndi-name>

<connection-url>**jdbc:postgresql://localhost:5432/postgres**</connection-url>

<driver-class>**org.postgresql.Driver**</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql></new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasource Firebird v2.5 - Dados para conexão - Firebird v2.0/v2.5

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**homologaFirebird**</jndi-name>

<connection-url>**jdbc:firebirdsql://localhost:3050/C:\ProgramFiles\Firebird\Firebird\_2\_5\examples\empbuid\EMPLOYEE.FDB**</connection-url>

<driver-class>**org.firebirdsql.jdbc.FBDriver**</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql></new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasource IBM DB2 v10.5 - Dados para conexão - IBM DB2 v10.5

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**homologaDB2**</jndi-name>

<connection-url>**jdbc:db2://localhost:50000/SAMPLE**</connection-url>

<driver-class>**com.ibm.db2.jcc.DB2Driver**</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql></new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Datasource SQL Server v10.0 - Dados para conexão - SQL Server v10.0

<?xml version="1.0" encoding="UFT-8"?>

<datasources>

<local-tx-datasource>

<jndi-name>**homologaSQLSERVER**</jndi-name>

<connection-url>**jdbc:sqlserver://localhost\SQLEXPRESS:1433**</connection-url>

<driver-class>**com.microsoft.sqlserver.jdbc.SQLServerDriver**</driver-class>

<user-name>**Usuário**</user-name>

<password>**senha**</password>

<exception-sorter-class-name>**org.jboss.resource.adapter.jdbc.vendor.OracleExceptionSorter**</exception-sorter-class-name>

<new-connection-sql></new-connection-sql>

<min-pool-size>**5**</min-pool-size>

<max-pool-size>**5**</max-pool-size>

<transaction-isolation>**TRANSACTION\_READ\_COMMITTED**</transaction-isolation>

</local-tx-datasource>

Finalizada a configuração, salve o arquivo.

No Sankhya Om, ao utilizar a tela [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354-Construtor-de-Componentes-de-BI) para criação de um novo dashboard, na etapa destinada a **"Editar/consultar a expressão"**, realize a escolha do banco de dados externo que foi anteriormente inserido no Datasource, através do ícone em destaque na imagem abaixo:

![Imagem 1: No Sankhya Om , ao utilizar a tela Construtor de Componentes de BI para criação de um novo dashboard, na etapa…](https://ajuda.sankhya.com.br/hc/article_attachments/5877030693271)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Wildfly - Configuração de Datasource

A configuração de um novo datasource para o Wildfly consiste na configuração do driver de conexão com o banco de dados ([Driver JDBC para conexão com o banco de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#driverjdbcparaconexocomobancodedados) e [Criação do Datasource](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#criaododatasource), respectivamente) e na definição do datasource que na prática é um XML que define os dados de conexão com a base de dados.

O driver de conexão precisa ser definido uma única vez, portanto se já existir o driver no Wildfly, será necessário apenas seguir as instruções descritas no tópico [Criação do Datasource](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#criaododatasource).

Por padrão, o Wildfly que disponibilizamos já possui os drivers do Oracle, MS SQL e MySQL como módulos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Driver JDBC para conexão com o banco de dados

Existem duas opções para configurar o driver de conexão com o banco de dados, são elas:

**A.** Utilizar um driver JDBC versão 4.0

Para isto, basta copiar o **"arquivo.jar"** referente ao seu driver JDBC 4.0 para a pasta:

WILDFLY\_HOME/standalone/deployments

**Observação:** se o jar for de uma versão anterior a 4.0, o Wildfly exibirá um erro de deploy do arquivo.jar.

**B.** Definir o driver JDBC como módulo do Wildfly

Para os passos a seguir, iremos considerar que o termo "meuBanco" é o nome identificador do seu banco de dados, deste modo:

**1 –** Crie a pasta **WILDFLY\_HOME/modules/custom/meuBanco/main**

**2 –** Dentro da pasta **"main"** crie o arquivo module.xml que é o descritor do seu módulo.

**<?xml** version="1.0" encoding="UTF-8"?>

**<module** xmlns="urn:jboss:module:1.1" name="custom.meuBanco"**>**

 **<resources>**

         **<resource-root** path="meuBanco.jar"**/>**

 **</resources>**

 **<dependencies>**

         **<module** name="javax.api"**/>**

         **<module** name="javax.transaction.api"**/>**

 **</dependencies>**

#### </module>

**Observações:**

- O nome para seu módulo deve ser sugestivo e não pode conter caracteres especiais ou espaços;
- O jar do driver JDBC deve ficar na pasta main, juntamente ao module.xml; certifique-se que o nome do jar é o mesmo definido dentro do XML.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Criação do Datasource

O Datasource é um XML que descreve as configurações e os dados de conexão com a base de dados. O arquivo deve ter o nome terminado em **"-ds.xml"** (teste-ds.xml, treina-ds.xml, integracao-ds.xml) e deve ser salvo em:

WILDFLY\_HOME/standalone/deployments

**Observação:** destaca-se ainda que o Construtor de Dashboards pode ser utilizado em qualquer Banco de Dados. Para isso, basta criar um novo arquivo Data Source no Wildfly para o Banco escolhido, desse modo, no [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354) pode-se selecionar a Data-Base. 

A seguir estão disponibilizados os modelos conforme cada banco de dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Oracle

**<?xml** version="1.0" encoding="UTF-8"**?>**

**<datasources** xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.org/schema/

 datasources\_1\_0.xsd">

 **<datasource** jndi-name="java:/OracleDS" pool-name="OracleDS"**>**

         **<connection-url>**jdbc:oracle:thin:@IP\_OU\_HOST:1521:SID\_DA\_BASE**</connection-url>**

         **<connection-property** name="v$session.program">IronJacamar**</connection-property>**

         **<driver-class>**oracle.jdbc.driver.OracleDriver**</driver-class>**

         **<security>**

                 **<user-name>x</user-name>**

**<password>y</password>**

         **</security>**

**<validation>**

**<valid-connection-checker**

                 class-name="org.jboss.jca.adapters.jdbc.extensions.oracle.OracleValidConnectionChecker"**>**

         **</valid-connection-checker>**

                 **<stale-connection-checker**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.oracle.OracleStaleConnectionChecker">

                 **</stale-connection-checker>**

                         **<exception-sorter**

                                 class-name="org.jboss.jca.adapters.jdbc.extensions.oracle.OracleExceptionSorter">**</exception-sorter>**

                 **</validation>**

 **</datasource>**

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## MySQL

**<?xml** version="1.0" encoding="UTF-8"?>

**<datasources** xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.org/schema/

 datasources\_1\_0.xsd">

 **<datasource** jndi-name="java:/MySqlDS" pool-name="MySqlDS">

         **<connection-url>**jdbc:mysql://mysql-hostname:3306/nome\_bd**</connection-url>**

         **<driver-class>**com.mysql.jdbc.Driver**</driver-class>**

         **<security>**

                 **<user-name>**x**</user-name>**

                 **<password>**y**</password>**

         **</sec<datasource** jndi-name="java:jboss/datasources/SantaRosa" pool-name="SantaRosaDS" enabled="true" jta="true" use-java-context="true" use-ccm="true"**>**

                  **<connection-url>**jdbc:firebirdsql:localhost/3050:C:/SantaRosa/sicoi.gdb?charSet=ISO-8859-1**</connection-url>**

                  **<driver>**firebirdsql**</driver>**

                  **<security>**

                    **<user-name>**SYSDBA**</user-name>**

                    **<password>**masterkey**</password>**

                  **</security>**

                  **<statement>**

                      **<prepared-statement-cache-size>100</prepared-statement-cache-size>**

                      **<share-prepared-statements/>**

                  **</statement>**

              **</datasource>**

**<driver** name="firebirdsql" module="org.firebirdsql"**>**

                    **<xa-datasource-class>**org.firebirdsql.pool.FBConnectionPoolDataSource**</xa-datasource-class>**

                  **</driver>**urity>

         **<validation>**

                 **<valid-connection-checker**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.mysql.MySQLValidConnectionChecker">

                 **</valid-connection-checker>**

                 **<exception-sorter**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.mysql.MySQLExceptionSorter">

                 **</exception-sorter>**

**</validation>**

**</datasource>**

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## PosgreSQL

**<?xml** version="1.0" encoding="UTF-8"**?>**

**<datasources** xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.org/schema/

 datasources\_1\_0.xsd">

 **<datasource** jndi-name="java:/PostgresDS" pool-name="PostgresDS">

         **<connection-url>**jdbc:postgresql://[servername]:[port]/[database name]**</connection-url>**

        **<driver-class>**org.postgresql.Driver**</driver-class>**

         **<security>**

**<user-name>**x**</user-name>**

                **<password>**y**</password>**

         **</security>**

         **<validation>**

                 **<valid-connection-checker**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.postgres.PostgreSQLValidConnectionChecker">

                 **</valid-connection-checker>**

**<exception-sorter**

                                 class-name="org.jboss.jca.adapters.jdbc.extensions.postgres.PostgreSQLExceptionSorter">

                         **</exception-sorter>**

**</validation>**

 **</datasource>**

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## MS SQL Server

**<?xml** version="1.0" encoding="UTF-8"**?>**

**<datasources** xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.orgd/schema/atasources\_1\_0.xsd"**>**

 **<datasource** jndi-name="java:/MSSQLDS" pool-name="MSSQLDS"**>**

         **<connection-url>**

                 jdbc:microsoft:sqlserver://localhost:1433;DatabaseName=MyDatabase

        **</connection-url>**

         **<driver-class>**com.microsoft.sqlserver.jdbc.SQLServerDriver**</driver-class>**

         **<security>**

                 **<user-name>**x**</user-name>**

                 **<password>**y**</password>**

         **</security>**

**<validation>**

**<valid-connection-checker**

                                 class-name="org.jboss.jca.adapters.jdbc.extensions.mssql.MSSQLValidConnectionChecker">

                 </valid-connection-checker>

         **</validation>**

 **</datasource>**

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## IBM DB2

**<?xml** version="1.0" encoding="UTF-8"**?>**

#### <datasources

 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.org/schema/datasources\_1\_0.xsd"

 **>**

 **<datasource** jndi-name="java:/DB2DS" pool-name="DB2DS">

         **<connection-url>**jdbc:db2:SUA\_BASE\_DE\_DADOS**</connection-url>**

         **<driver-class>**COM.ibm.db2.jdbc.app.DB2Driver**</driver-class>**

         **<security>**

                 **<user-name>**USUARIO**</user-name>**

                 **<password>**SENHA**</password>**

         **</security>**

**<validation>**

**<valid-connection-checker**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.db2.DB2ValidConnectionChecker">

                 **</valid-connection-checker>**

**<stale-connection-checker**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.db2.DB2StaleConnectionChecker">

                 **</stale-class-connection-checker>**

**<exception-sorter**

                         class-name="org.jboss.jca.adapters.jdbc.extensions.db2.DB2ExceptionSorter">

                 </exception-sorter>

         </validation>

 </datasource>

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)

## Firebird

**<?xml** version="1.0" encoding="UTF-8"**?>**

#### <datasources

 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

 xsi:noNamespaceSchemaLocation="http://www.ironjacamar.org/schema/datasources\_1\_0.xsd"

 **>**

**<datasource** jta="false" jndi-name="java:jboss/NOME\_DATASROUCE" pool-name="NOME\_DATASROUCE" enabled="false" use-ccm="false">

  **<connection-url>**jdbc:FirebirdSQL:name.serverfirebird.com.br:/path/to/database/data.fdb**</connection-url>**  

    **<driver-class>**org.firebirdsql.jdbc.FBDriver**</driver-class>**  

    **<connection-property** name="charSet">ISO8859-1**</connection-property>**

    **<connection-property** name="roleName">ROLE\_APP**</connection-property>**

    **<driver>**jaybird-2.2.4.jar**</driver>**

    **<security>**  

            **<user-name>**userdb**</user-name>**  

            **<password>**passwddb**</password>**

    **</security>**

**<validation>**

**<validate-on-match>**false**</validate-on-match>**

            **<background-validation>**false**</background-validation>**  

    **</validation>**

**<timeout>**

**<idle-timeout-minutes>**1**</idle-timeout-minutes>**

    **</timeout>**

**<statement>**

**<share-prepared-statements>**false**</share-prepared-statements>**

    **</statement>**

**</datasource>**  

#### </datasources>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109733-Bancos-de-Dados-Dashboards-no-Sankhya-Om#top)
