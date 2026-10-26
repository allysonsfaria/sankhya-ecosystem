---
id: "8896725681943"
titulo: "Configuração de argumentos para Wildfly"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:11:41Z"
rotulos: ["Configuração", "Parâmetros", "configurações servidor Java", "WildFly", "Servidor de Aplicações", "Java"]
---

# Configuração de argumentos para Wildfly

Algumas vezes são necessárias algumas configurações específicas para a máquina virtual do Java, a JDK, a fim de mudar alguns comportamentos do sistema. Tais configurações são determinadas por argumentos que podem ter efeito no funcionamento geral do servidor de aplicações ou até mesmo mudar uma tratativa específica do sistema. 

Tais configurações são feitas no arquivo de inicialização do Wildfly e só entram em vigor após a reinicialização do serviço, a partir do próprio sistema operacional. 

Para fazer esta configuração num servidor Windows, acesse a pasta do Wildfly > bin > arquivo standalone.conf.bat e adicione uma nova configuração com esta sintaxe: 

set "JAVA\_OPTS=%JAVA\_OPTS% -Djava.io.tmpdir=C:\Sankhya\TEMP"

![Configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15822526310807)

No exemplo em questão, o argumento -Djava.io.tmpdir está direcionando a geração de arquivos temporários para a pasta: C:\Sankhya\TEMP 

Para servidores de aplicação no ambiente linux, o caminho do arquivo é o mesmo: Pasta do Wildfly > bin, porém o arquivo a ser editado é o standalone.conf. A sintaxe também é diferente ficando desta forma: 

![Configuração](https://ajuda.sankhya.com.br/hc/article_attachments/15822526316439)

JAVA\_OPTS="$JAVA\_OPTS -Djava.io.tmpdir=/home/mgeweb/TEMP"

Feita a edição, salve o arquivo e reinicie o sistema a partir do servidor. 

Dentre os argumentos mais comuns utilizados pelo sistemas estão estes abaixo. Lembrando que sempre que for alterar ou adicionar algum além destes, tenha completa ciência dos impactos que podem gerar na operação do sistema: 

(1)** -Djape.global.query.timeout**: Tempo de timeout de query. Ajustando quando ocorre o erro de "ORA-01013". Valor deve ser em segundos.

Exemplo: -Djape.global.query.timeout=600

(1)** -Djape.session.timeout**: Tempo de timeout de sessão JAPE. Ajustado quando ocorre o erro "JapeSession timeout". Valor deve ser em milissegudos.

Exemplo: -Djape.session.timeout=600000

(1)** -Djape.jdbc.check.select**: Validar/não validar a expressão select de relatórios e dashboards.

Exemplo: -Djape.jdbc.check.select=false

(1)** -#GMT\_BRASIL**

(1)** -JAVA\_OPTS="$JAVA\_OPTS -Duser.timezone=GMT-3"** : ajustar timezone

(1)** -Djboss.socket.binding.port-offset**: Offset da porta padrão do Wildfly. Soma-se o valor a 8080.

Exemplo: -Djboss.socket.binding.port-offset=100, dessa forma, a porta de conexão ao sistema será a 8180.

(1)** -Djboss.bind.address.management**: Bind de acesso ao JMX Console do Wildfly. É necessário para utilizar o JConsole e Visual VM.

Exemplo: -Djboss.bind.address.management=0.0.0.0

(1)** -Duser.language**: Força a linguagem do usuário. Exemplo: -Duser.language=pt

(1)** -Duser.country**: Força a região do usuário.

Exemplo: -Duser.country=BR 

(1)** -Dfile.encoding**: Força o encoding do sistema para o padrão ISO pt\_br 

Exemplo: -Dfile.encoding=ISO8859-1

(1)** -Dskw.use.procedure.tgfnum**: Ativa/Desativa a numeração por procedure no sistema.

Exemplo: -Dskw.use.procedure.tgfnum=true

(1)** -Dskw.use.procedure.tgfnum.rule**: Lista de tabelas que serão numeradas por procedures.

Exemplo: -Dskw.use.procedure.tgfnum.rule=TGFCAB,TGFFIN,TGFMBC,TMDFMG,TMDAMG,TGFLNF

(1)** -Djape.experimental.lock.strategy**: Estratégia diferencial de Lock.

Exemplo: -Djape.experimental.lock.strategy=1

(1)** -Djape.experimental.always.reuse.jdbc.conn**: Ativar o reuso de conexões JDBC

Exemplo: -Djape.experimental.always.reuse.jdbc.conn=true

(1)** -Djape.experimental.commit-type**: Tipo de commit

Exemplo: -Djape.experimental.commit-type=B

(1)** -Djape.use.write.history**: Desligar a gravação de histórico do jape

Exemplo: -Djape.use.write.history=false

(1)** -Dsankhyaw.schedule.disable:** Desabilita a execução de jobs no sistema

Exemplo:  -Dsankhyaw.schedule.disable=false

(1)** -Dlogin.unico.ativo:** false : Ignora checagens do login unico ( [LoginUnico] Informações incompletas, o token não será gerado. Usuario....])

(1)** -Djape.check.is.valid.connection=false:** Ignora checagens de conexão feitas pelo wildfly (SELECT FROM DUAL)

(1)** -Djape.sqlserver.use.native.query.getpk=true:** -- SQL Server para carga dos metadados mais rápida 

(1)**-Dskw.use.procedure.tgfnum.numnota=false:** Desabilita a utilização da procedure STP\_NUMERAR\_NOTA2

(1)** -Djava.io.tmpdir=**: Determina o diretório de arquivos temporários do sistema

**(1)** **Dsnk.authorization.layer.enable =** true

**(1)** **Dskw.cluster.nodes=** 'IP 1,IP 2' declarar quais IPs estarão no modo cluster.

(1)** Dskw.cluster.pref.run.job=** true declarar qual nó será o executor de jobs.
