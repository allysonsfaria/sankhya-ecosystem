---
id: "360045547894"
titulo: "Manual de Instalação Sankhya Om em Ambiente  Linux"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux"
trilha: "Manual do Produto > Comece por aqui > Guia de Primeiros Passos"
atualizado_em: "2026-09-28T13:52:22Z"
rotulos: ["Configuração", "Oracle", "SQL Server", "Linux", "Instalação: Oracle/SQL Server Wildfly Sankhya Om", "Configurações: Ports memória inicialização backup", "Notas: Homologação parâmetros arquivos comandos", "WildFly", "Sankhya Om", "Instalação"]
---

# Manual de Instalação Sankhya Om em Ambiente  Linux

O manual a seguir contém as instruções para a instalação do **Sankhya Om** para Banco de Dados Oracle e SQL Server em Ambiente Linux.

| Etapas para instalação |
| --- |
| [Introdução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#introdu%C3%A7%C3%A3o) |
| [Procedimento para Banco de Dados Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#ProcedimentoparaBancodeDadosOracle) |
| [Configuração do Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3odoWildfly) |
| [Configuração para Banco de Dados Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3oparaBancodeDadosOracle) |
| [Configuração para Banco de Dados SQL Server](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3oparaBancodeDadosSQLServer) |
| [Instalação do pacote Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Instala%C3%A7%C3%A3odoPacoteSankhyaOM) |
| [Configuração da Porta Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3odaPortaWildfly) |
| [Configuração de memória do Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3odemem%C3%B3riadoWildfly) |
| [Inicialização do Wildfly para Produção, Teste e Treina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Inicializa%C3%A7%C3%A3odoWildflyparaProdu%C3%A7%C3%A3o,TesteeTreina) |
| [Acompanhamento da inicialização do Wildfly Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Acompanhamentodainicializa%C3%A7%C3%A3odoWildflyProdu%C3%A7%C3%A3o) |
| [Suspensão do Wildfly para Produção, Teste e Treina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Suspens%C3%A3odoWildflyparaProdu%C3%A7%C3%A3o,TesteeTreina) |
| [Configuração para inicialização automática Wildfly Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3oparainicializa%C3%A7%C3%A3oautom%C3%A1ticaWildflyProdu%C3%A7%C3%A3o) |
| [Configuração de backup Aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3odebackupAplica%C3%A7%C3%A3o) |

## Introdução

O **Sankhya Om** é uma aplicação JEE (Java Enterprise Edition) e, por isso, utiliza o Wildfly como servidor de aplicação JEE. O Wildfly, por sua vez, é uma aplicação Java que requer uma instalação prévia do Java na máquina servidora.

A configuração do Wildfly é facilitada pelo [Gerenciador de Pacotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580034-Melhores-pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-via-Gerenciador-de-Pacotes), que simplifica tarefas como configuração de memória, arranjo de portas, diretório de extensões, aplicação de patches de segurança, entre outras.

![Imagem 1: O Gerenciador de Pacotes não suporta mais o processo de atualização e instalação de pacotes do Sankhya Om (pkgs); essa…](https://ajuda.sankhya.com.br/hc/article_attachments/17096730163735) O Gerenciador de Pacotes não suporta mais o processo de atualização e instalação de pacotes do **Sankhya Om** (pkgs); essa responsabilidade agora é exclusiva do [WPM](https://ajuda.sankhya.com.br/hc/pt-br/articles/21238784689943-Atualiza%C3%A7%C3%A3o-do-sistema-Sankhya-W-via-WPM) que é uma aplicação Web, um painel de instalação do **Sankhya Om**, que é acessado dentro do ambiente do Wildfly.

![Imagem 2: O Gerenciador de Pacotes não suporta mais o processo de atualização e instalação de pacotes do Sankhya Om (pkgs); essa…](https://ajuda.sankhya.com.br/hc/article_attachments/22894728221719)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Procedimento para Banco de Dados Oracle

Para a instalação, deve-se conectar no servidor Oracle via putty ou diretamente no servidor e executar o procedimento descrito abaixo para verificar o parâmetro **open\_cursors**.

```
[oracle@oracletestes ~]$ sqlplus "/as sysdba"
```

Conferir valor do parâmetro open\_cursors:

```
SQL> show parameter open_cursors
NAME TYPE VALUE
-----------------------------------
open_cursors integer 300

Ajustar parâmetros do Oracle:
SQL> alter system set open_cursors=2000;
System altered.
SQL> exit
```

**Observação:** caso o retorno do parâmetro apresente **valor <2000** efetue o procedimento de **"Ajustar parâmetros do Oracle"** para correção.

### 1 - Mudar Padrão Lang

Conectar com root via putty ou direto no servidor, siga os passos abaixo:

Verificar a versão do Linux:

- Se o sistema for baseado em **Red Hat**:

```
cat /etc/redhat-release
```

- Se o sistema for baseado em **systemd**:

```
/etc/os-release
```

**Ajustar a configuração de localização:**

Para **CentOS 6** execute o bloco de comandos abaixo:

```
echo 'LANG="pt_BR.ISO-8859-1"
SUPPORTED="pt_BR.ISO-8859-1:pt_BR:pt"
SYSFONT="latarcyrheb-sun16"' > /etc/sysconfig/i18n
```

Para **CentOS 7** deve-se executar o bloco de comando exibido a seguir:

```
echo 'LANG="pt_BR.ISO-8859-1"
SUPPORTED="pt_BR.ISO-8859-1:pt_BR:pt"
SYSFONT="latarcyrheb-sun16"' > /etc/locale.conf
```

![Imagem 3: Caso o sistema operacional seja Red Hat Enterprise (RHEL) , execute o comando abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17096730163735) Caso o sistema operacional seja **Red Hat Enterprise (RHEL)**, execute o comando abaixo:

```
localectl set-locale LANG=pt_BR.UTF-8
```

### 2 - Criar usuário Mgeweb

Após isso, é necessário criar um usuário mgeweb:

```
[root@localhost ~]# useradd mgeweb
```

Utilize este comando para trocar a senha do usuário:

```
[root@localhost ~]# passwd mgeweb
```

### 3 - Adicionar limits

Para a adição de limits do usuário, deve-se executar o bloco como root:

```
echo "mgeweb soft nofile 1024
mgeweb hard nofile 65536
mgeweb soft nproc 2047
mgeweb hard nproc 16384
mgeweb soft stack 10240
mgeweb hard stack 32768" >> /etc/security/limits.conf
```

### 4 - Alterar hostname

Este deverá ser alterado conforme exemplo exibido abaixo:

```
127.0.0.1 localhost localhost.localdomain localhost4 localhost4.localdomain4
::1 localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.1.21 <novo nome do servidor>
```

### 5 - Desabilitar Firewall e Selinux

Caso este seja CentOS 6, como root:

```
service iptables save
service iptables stop
chkconfig iptables off

sed -i s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config
setenforce Permissive
```

Se este for CentOS 7:

```
[root@teste ~]# firewall-cmd --permanent --add-port=8180/tcp ;
firewall-cmd --permanent --add-port=8280/tcp ;
firewall-cmd --permanent --add-port=8380/tcp ;
firewall-cmd --permanent --add-port=10050/tcp ;
firewall-cmd --permanent --add-port=10051/tcp ;
firewall-cmd --permanent --add-port=1433/tcp ;
firewall-cmd --permanent --add-port=1521/tcp ;

firewall-cmd --reload

sed -i s/SELINUX=enforcing/SELINUX=disabled/g /etc/selinux/config
setenforce Permissive
```

### 6 - Baixar arquivos da aplicação Sankhya Om

Agora, envie os arquivos baixados nos passos anteriores para o servidor conectado com usuário mgeweb para a pasta **/home/mgeweb**.

- Para efetuar o download do Wildfly, acesse o [Sankhya Downloads](http://downloads.sankhya.com.br/), clique no menu **"Aplicações"** e escolha a opção **WildFly.** Importante ressaltar que para baixar os arquivos é necessário estar logado com o seu Sankhya ID.
- Além disso, para realizar o download do arquivo JDK 8, do Pacotes Sankhya e o Pacote Sankhya junto à documentação **sankhya\_x.xx.xxxxx.pkg**, acesse este link do [Sankhya Downloads](http://downloads.sankhya.com.br/).

**Nota:** deve-se fazer o download do arquivo JDK 8 conforme a versão do seu Sistema Operacional.

### 7 - Instalar Sannfe

![Imagem 4: Nesta etapa, conecte-se com o usuário mgeweb via putty2 ou direto no servidor;](https://ajuda.sankhya.com.br/hc/article_attachments/17096715440791) Nesta etapa, conecte-se com o usuário **mgeweb via putty2** ou direto no servidor;

![Imagem 5: Em seguida, é preciso descompactar o arquivo do Sannfe como exibido abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17096730168343) Em seguida, é preciso descompactar o arquivo do Sannfe como exibido abaixo:

```
[mgeweb@localhost ~]$ tar -xzvf SanNFe_unixx64_Sankhya_XXXXXXX.tar.gz
```

### 8 - Instalação do JDK

Para tal, conecte com o usuário **mgeweb via putty2** ou direto no servidor, deve-se descompactação com os procedimentos abaixo:

```
[mgeweb@localhost ~]$ tar -xzvf jdk-xxxx-linux-x64.tar.gz
```

### 9 - Criação do link simbólico

Com o caminho do diretório do JDK 8, crie o link simbólico:

```
[mgeweb@localhost ~]$ cd jdkx.x.x_xx
[mgeweb@localhost jdk1.x.x_XX]$ pwd
/home/mgeweb/jdkx.x.x_xx

[mgeweb@localhost ~]$ ln -s /home/mgeweb/jdk1.8.0_231/ /home/mgeweb/jdk8
```

### 10 - Adição do alias no .bash\_profile

Segue o exemplo:

```
[mgeweb@localhost jdkx.x.x_XX]$ vi /home/mgeweb/.bash_profile
```

Inclua as linhas abaixo no final do arquivo .bash\_profile, após procedimento tecle **ESC:wq**

#### Configurações para exclusão de pastas temporárias antes da inicialização do Wildfly

```
alias rmltwprod='rm -rf
/home/mgeweb/wildfly_producao/standalone/log
home/mgeweb/wildfly_producao/standalone/tmp
/home/mgeweb/wildfly_producao/standalone/work'
alias rmltwteste='rm -rf
/home/mgeweb/wildfly_teste/standalone/log
/home/mgeweb/wildfly_teste/standalone/tmp
/home/mgeweb/wildfly_teste/standalone/work'
alias rmltwtreina='rm -rf
/home/mgeweb/wildfly_treina/standalone/log
/home/mgeweb/wildfly_treina/standalone/tmp
/home/mgeweb/wildfly_treina/standalone/work'
```

#### Configuração para inicialização do Wildfly

```
alias jb_startprod='killprod;rmltwprod;nohup
/home/mgeweb/wildfly_producao/bin/standalone.sh
-bmanagement 0.0.0.0 >& /dev/null &'
alias jb_starttreina='killtreina;rmltwtreina;nohup
/home/mgeweb/wildfly_treina/bin/standalone.sh
-bmanagement 0.0.0.0 >& /dev/null &'
alias jb_startteste='killteste;rmltwteste;nohup
/home/mgeweb/wildfly_teste/bin/standalone.sh
-bmanagement 0.0.0.0 >& /dev/null &'
```

#### Configuração para ver log

```
alias jb_logprod='tail -f
/home/mgeweb/wildfly_producao/standalone/log/server.log'
alias jb_logtreina='tail -f
/home/mgeweb/wildfly_treina/standalone/log/server.log'
alias jb_logteste='tail -f
/home/mgeweb/wildfly_teste/standalone/log/server.log'
```

#### Configuração para execução do Wildfly

```
alias jb_psprod='ps ax | grep wildfly_producao'
alias jb_psteste='ps ax | grep wildfly_teste'
alias jb_pstreina='ps ax | grep wildfly_treina'
```

#### Configuração para fechar execução Wildfly

```
alias killprod='ps -ef | awk "/wildfly_producao/
&& !/awk/ {print \$2}" | xargs kill -9 2>> /dev/null'
alias killteste='ps -ef | awk "/wildfly_teste/
&& !/awk/ {print \$2}" | xargs kill -9 2>> /dev/null'
alias killtreina='ps -ef | awk "/wildfly_treina/
&& !/awk/ {print \$2}" | xargs kill -9 2>> /dev/null'
```

#### Para consulta de processos SAS

```
alias sas='ps aux | grep SAS'
#Parar o SAS
alias stopsas='/opt/SAS3.0b105/protstop.sh'
#iniciar o SAS
alias startsas='/opt/SAS3.0b105/protstart.sh'
```

#### Atalho para o Gerenciador de Pacotes

```
alias pkg='
/home/mgeweb/sankhyaw_gerenciador_de_pacotes/bin/./sankhyaw-package-manager'
```

### 11 - Descompactação do Gerenciador de Pacotes

```
[mgeweb@localhost jdkx.x.x_XX]$ cd
[mgeweb@localhost ~]$ tar -xzvf pkg-man_unix_1_xxx.tar.gz
```

**Observação:** o nome do arquivo poderá mudar, nesse caso, deve-se substituir o XXX pelo nome correspondente.

### 12 - Copiar o arquivo PKG

```
[mgeweb@localhost ~]$ cp sankhya-w_XXXXXX.pkg sankhyaw_gerenciador_de_pacotes/pkgs/
```

**Nota:** caso o nome do arquivo mude, substitua o  XXX pelo nome correspondente.

Posteriormente, confira se o pacote de instalação/atualização está na pasta correta:

```
[mgeweb@localhost ~]$ ls sankhya-w_gerenciador_de_pacotes/pkgs/sankhyaw_xxxx.pkg
```

**Observação:** caso não haja o retorno de nenhum arquivo ao executar o comando acima, deve-se repetir o passo 8.

Para descompactar o Wildfly, utilize o comando:

```
[mgeweb@localhost ~]$ unzip Wildfly_11.0.0_Sankhya_mod_XXX.zip
```

### 13 - Instalação do Wildfly Teste e Treina

Para a execução deste, segue:

```
[mgeweb@localhost ~]$ cp -r wildfly_producao/ wildfly_teste
[mgeweb@localhost ~]$ cp -r wildfly_producao/ wildfly_treina
```

### 14 - Permissão de Execução nos Arquivos

```
chmod +x /home/mgeweb/wildfly_producao/bin/*.sh
chmod +x /home/mgeweb/wildfly_teste/bin/*.sh
chmod +x /home/mgeweb/wildfly_treina/bin/*.sh
```

### 15 - Registro do servidor do Wildfly

Para tal, deve-se conectar com o usuário **mgeweb via putty2** ou direto no servidor, e descompactar o JDK com os procedimentos e registrar servidor de produção, teste e treina executar o bloco a seguir:

```
echo "<server>
<name>wildfly_producao</name>
<home>/home/mgeweb/wildfly_producao</home>
<appServer>WildFly 11.0.0.Final</appServer>
</server>" >
/home/mgeweb/sankhyaw_gerenciador_de_pacotes/conf/WILDFLY_PRODUCAO.xml

echo "<server>
<name>wildfly_teste</name>
<home>/home/mgeweb/wildfly_teste</home>
<appServer>WildFly 11.0.0.Final</appServer>
</server>" > /home/mgeweb/sankhyaw_gerenciador_de_pacotes/conf/WILDFLY_TESTE.xml

echo "<server>
<name>wildfly_treina</name>
<home>/home/mgeweb/wildfly_treina</home>
<appServer>WildFly 11.0.0.Final</appServer>
</server>" > /home/mgeweb/sankhya-w_gerenciador_de_pacotes/conf/WILDFLY_TREINA.xml

Para mudar a porta, utilize:

sed -i 's/port-offset=0/port-offset=100/g' /home/$USER/wildfly_producao/bin/standalone.conf
sed -i 's/port-offset=0/port-offset=200/g' /home/$USER/wildfly_teste/bin/standalone.conf
sed -i 's/port-offset=0/port-offset=300/g' /home/$USER/wildfly_treina/bin/standalone.conf
```

### 16 - Inicialização do Gerenciador de Pacotes

Insira os comandos:

```
[mgeweb@localhost ~]$ pkg
```

ou

```
[mgeweb@localhost ~]$
/home/mgeweb/sankhyaw_gerenciador_de_pacotes/bin/./sankhyaw-package-manager
Preparing JRE ...
testing JVM in /home/mgeweb/sankhyaw_gerenciador_de_pacotes/jre
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração do Wildfly

Deve-se realizar o procedimento a ser descrito abaixo nas bases de Produção, Teste e Treina.

No início das configurações, temos as opções:

- [1] Instalação/atualização expressa ao sistema;
- [2] Selecionar Servidor;
- [3] Listar Servidores Registrados;
- [4] Registrar Servidor;
- [5] Sair.

Para esta etapa, digite a opção 4;

No Registro de Servidor de Aplicações, o servidor **wildfly\_prod** deverá ser inserido;

![Imagem 6: No Registro de Servidor de Aplicações, o servidor wildfly_prod deverá ser inserido;](https://ajuda.sankhya.com.br/hc/article_attachments/360096090893)

Em seguida, insira o comando **/home/mgeweb/wildfly\_prod**  

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração para Banco de Dados Oracle

Para realizar os passos no seu Banco de Dados Oracle, será necessário realizar o procedimento descrito abaixo para bases de produção, teste e treina.

Para a configuração do Banco de Dados, tem-se as opções:

- [1] Instalação/atualização expressa do Sistema;
- [2] Selecionar Servidor;
- [3] Listar Servidores registrados;
- [4] Registrar Servidor;
- [5] Sair.

![Imagem 7: (5) Sair.](https://ajuda.sankhya.com.br/hc/article_attachments/360096091133)

Para esta configuração, digite a opção 2;

Posteriormente, as opções a seguir serão exibidas:

- [1] wildfly\_producao;
- [2] wildfly\_teste;
- [3] wildfly\_treina;
- [4] Retornar ao menu anterior.

![Imagem 8: (4) Retornar ao menu anterior.](https://ajuda.sankhya.com.br/hc/article_attachments/360064693793)

Digite a opção 1;

Em seguida, o início da Configuração de Banco de Dados será apresentado:

- [1] Oracle;
- [2] Ms SQL Server (Server JTDS);
- [3] Ms SQL Server (Driver Ms);
- [4] Para saber mais sobre JTDS e Ms.

![Imagem 9: (4) Para saber mais sobre JTDS e Ms.](https://ajuda.sankhya.com.br/hc/article_attachments/360093837414)

Neste, digite a opção 1;

Tem-se que deverá ser inserido o IP do servidor do Banco de Dados. Para este temos o exemplo para inserção:

**192.168.0.148** ou **localhost**, caso o servidor de aplicação estiver junto com o servidor de banco de dados;

Depois, digite o número da porta;

Para o nome do serviço digite **xe**, neste as letras deverão ser maiúsculas;

Posteriormente, digite o usuário do banco de dados. O usuário **SANKHYA** poderá ser digitado com letras maiúsculas ou minúsculas;

Em seguida, digite a senha do Bando de Dados, e será retornado a pergunta:

**"Deseja testar as configurações de Banco de Dados antes de salvá-las?"**

Para esta pergunta, digite **"S"**;

**Nota:** caso aconteça algum erro no teste de conexão, revise as configurações. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração para Banco de Dados SQL Server

Realiza-se o procedimento a ser descrito abaixo nas bases de Produção, teste e treina.

No início das configurações, temos as opções:

- [1] Instalação/atualização expressa do sistema;
- [2] Selecionar Servidor;
- [3] Listar Servidores Registrados;
- [4] Registrar Servidor;
- [5] Sair.

Exibidas estas opções, digite a opção 2, referente à seleção do servidor;

Depois, será possível ver o Início da Configuração do Banco de Dados:

- [1] Oracle;
- [2] Ms SQL Server (Driver JTDS);
- [3] Ms SQL Server (Driver Ms);
- [4] Para saber mais sobre JTDS e Ms.

![Imagem 10: (4) Para saber mais sobre JTDS e Ms.](https://ajuda.sankhya.com.br/hc/article_attachments/360093837414)

Para este, digite as opções 2 ou 3;

**Nota:** para a opção 2, utiliza-se drivers do Java. Esta deverá ser uma preferência de uso. Já na opção 3, será utilizado drivers da Microsoft.

Logo depois, Insira o IP ou localhost se o servidor de aplicação estiver junto com o servidor de Banco de Dados; 

Deve-se digitar o nome da porta e da instância do SQL Server, tem-se que esta deverá ser inserida apenas se estiver nomeada;

Digite o nome da base de dados, como, por exemplo: SANKHYA\_PROD;

Para o usuário de dados, digite **SANKHYA**, este poderá ser digitado em letras minúsculas ou maiúsculas.

Posteriormente, insira a senha.

Para a pergunta:

**"Deseja testar as configurações de Banco de Dados antes de salvá-las?"**

Para esta, digite "**S"**;

Caso ocorra algum erro no teste de conexão, revise as suas configurações. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Instalação do Pacote Sankhya Om

O procedimento abaixo será necessário para as bases de Produção, Teste e Treina.

Para o inicio do procedimento de instalação, teremos as opções:

- [1] Instalação/atualização expressa do Sistema;
- [2] Selecionar servidor;
- [3] Listar servidores registrados;
- [4] Registrar servidor;
- [5] Sair.

Digite 1 referente à Instalação/Atualização Expressa do Sistema, digite S para realizar a atualização deste.

Para os servidores registrados, será disponibilizado as opções:

- [1] wildfly\_producao;
- [2] wildfly\_teste;
- [3] wildfly\_treina;
- [4] Retornar ao menu anterior.

Digite a opção 1 para o servidor de aplicação;

Em seguida, insira a opção 1 para o Pacote de Atualização;

Depois veja que o Gerenciador exibirá mensagens o informando que o processo de atualização foi inicializado.

**Observação:** caso ocorra algum erro na instalação do pacote, efetue a verificação abaixo nos logs do Gerenciador de Pacotes:

```
 /home/mgeweb/sankhyaw_gerenciador_de_pacotes/log/package-manager.log
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração da porta Wildfly

Será necessário realizar o procedimento abaixo para as bases de Produção, Teste e Treina com as opções:

- [1] Instalação/atualização expressa do Sistema;
- [2] Selecionar Servidor;
- [3] Listar Servidores registrados;
- [4] Registrar Servidor;
- [5] Sair.

![Imagem 11: (5) Sair.](https://ajuda.sankhya.com.br/hc/article_attachments/360096091333)

Das opções a serem disponibilizadas acima, digite a opção 2;

![Imagem 12: Das opções a serem disponibilizadas acima, digite a opção 2 ;](https://ajuda.sankhya.com.br/hc/article_attachments/360064704753)

Neste, digite a opção 1;

Na etapa abaixo, digite o número 4 para selecionar esta opção;

![Imagem 13: Na etapa abaixo, digite o número 4 para selecionar esta opção;](https://ajuda.sankhya.com.br/hc/article_attachments/360063692494)

**Importante:** não utilize a porta 8080.

Por padrão do Sankhya, utilize as portas:

- PORTA 8180 para Base Produção;
- PORTA 8280 para Base Teste;
- PORTA 8380 para Base Treina.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração de memória do Wildfly

O procedimento a seguir, deverá ser realizado para as bases de Produção, Teste e Treina. Neste, tem-se as opções:

- [1] Configurar Banco de Dados;
- [2] Configurar Arranjo de Portas;
- [3] Deletar pasta temporária do Wildfly;
- [4] Visualizar dados da instalação corrente;
- [5] Diagnóstico do Dicionário de Dados;
- [6] Cancelar registro do servidor;
- [7] Configurações de memória;
- [8] Atualizar controle de acesso do sistema;
- [9] Instalar Wildfly como servico do Wndows;
- [10] Desinstalar Wildfly como servico do Windows;
- [13] Instalar extensões;
- [14] Voltar.

Primeiramente, deve-se selecionar o servidor, para tal ação, digite 2 para a seleção da opção a que refere-se este número;

Em seguida, selecione um servidor de aplicação, portanto digite o número 1 da opção **"wildfly\_produção"**;

![Imagem 14: Em seguida, selecione um servidor de aplicação, portanto digite o número 1 da opção "wildfly_produção" ;](https://ajuda.sankhya.com.br/hc/article_attachments/360096091473)

Nesta etapa digite o número 7, a que refere-se à opção de Configuração de Memória;

Referente ao Ambiente de Execução desta configuração, digite o número 1, a que corresponde ao da opção **"[1] Editar configurações de memória (XMX e XMS)"**.

Em seguida, tem-se:

![Imagem 15: Em seguida, tem-se:](https://ajuda.sankhya.com.br/hc/article_attachments/360096091853)

Referente a esta etapa, destacamos que a quantidade memória inicial e máxima do **Wildfly** deverão ser menores que a disponível no sistema operacional. É recomendável que considere a quantidade de memória utilizada por outros processos na máquina, inclusive na sistema operacional. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Inicialização do Wildfly para Produção, Teste e Treina

Em conexão com o usuário **mgeweb**, deve-se executar o comando para iniciar seu respectivo serviço. Observe:

- Produção - jb\_startprod;
- Teste - jb\_startteste;
- Treina - jb\_starttreina.

Confira o exemplo:

```
[mgeweb@localhost bin]$ su -l mgeweb

[mgeweb@localhost ~]$ jb_startprod

[mgeweb@localhost ~]$ nohup: ignorando entrada e anexando saída a nohup.out
/home/mgeweb/wildfly_producao/bin/standalone.sh
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Acompanhamento da inicialização do Wildfly Produção

Em conexão com o usuário **mgeweb**, execute o comando para iniciar seu respectivo serviço:

- Produção - jb\_logprod;
- Teste - jb\_logteste;
- Treina - jb\_logtreina.

Assim, considere o exemplo:

```
[mgeweb@localhost bin ~]$ jb_logprod
```

Ao finalizar a inicialização, será apresentado as últimas linhas.

```
2011-03-16 09:52:00,118 INFO [org.wildfly.system.server.Server]
Wildfly (MX MicroKernel) [4.0.5.GA (build: CVSTag=Branch_4_0 date=200610162339)]
Started in 39s:722ms
2011-03-16 09:52:00,320 INFO [STDOUT] [ConfigEmailUtil]
Não foi possível ler o parâmetro MSDSMTPPROP da TSIPAR.
Este parâmetro define informações da conta de e-mail.
2011-03-16 09:52:00,322 INFO [STDOUT] [EnviadorMsgJob]
ERRO Modem SMS: Não foi possível ler a configuração do modem pelo parâmetro MSDSMSPROP
da TSIPAR.
```

**Observação:** pressione as teclas **"Ctrl + C"** para Cancelar.

Para a conexão com a Aplicação **Sankhya Om** Produção, Teste e Treina, assim, deve-se abrir seu navegador, nós sugerimos o Google Chrome como navegador padrão para a solução Java, pois este terá um melhor desempenho nestas circunstâncias.

Em seguida, faça a alteração da porta configurada para o ambiente a que deseja conectar-se, sendo estes, Produção, Teste e Treina. Sendo assim, vejamos os exemplos:

Produção: <http://ipdoservidor:8080/mge> 
Teste: <http://ipdoservidor:8180/mge> 
Treina: <http://ipdoservidor:8280/mge>

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Suspensão do Wildfly para Produção, Teste e Treina

Conectado com o usuário **mgeweb** executar o comando para iniciar seu respectivo serviço:

- **Produção:** killprod
- **Teste:** killteste
- **Treina:** killtreina

**Nota:** ao executar o comando, o serviço do Wildfly referente ao ambiente selecionado, será encerrado.

Observe o exemplo:

```
[mgeweb@localhost bin ~]$ killprod
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração para inicialização automática Wildfly Produção

Para a Liberação de acesso ao arquivo, teremos o comando:

```
[root@localhost bin ~]$ chmod +x /home/mgeweb/wildfly_producao/bin/startServer.sh
chmod +x /home/mgeweb/wildfly_teste/bin/startServer.sh
chmod +x /home/mgeweb/wildfly_treina/bin/startServer.sh
```

### Para configurar a inicialização do wildfly

[root@localhost bin ~]$ vi /etc/init.d/wildfly

- Para adicionar conteúdo ao arquivo:

```
#!/bin/bash
# chkconfig: 35 99 10
# description: startup SAS
```

### Inicialização do SAS

```
su -l mgeweb /opt/SAS3.0b105/./protstart.sh
```

### Inicialização Produção

```
su -l mgeweb /home/mgeweb/wildfly_producao/bin/./startServer.sh
```

### Inicialização Teste

```
sleep 120s
su -l mgeweb /home/mgeweb/wildfly_teste/bin/./startServer.sh
```

### Inicialização Treina

```
sleep 120s
su -l mgeweb /home/mgeweb/wildfly_treina/bin/./startServer.sh
```

**Liberação do acesso ao arquivo**

Para executar a liberação do acesso ao arquivo, segue o comando:

```
[root@localhost bin ~]$ chmod 755 /etc/init.d/wildfly
[root@localhost bin ~]$ chkconfig --add wildfly

chmod -R 775 /opt
chown mgeweb /opt
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

## Configuração de backup Aplicação

**Importante:** caso o servidor do Banco de Dados seja o mesmo do server de aplicação, configure para que todos sejam executados com o usuário Oracle. Desse modo, insira os comandos:

```
[root@teste ~]# su -l
[root@teste ~]# mkdir -p /backupW/scripts /backupW/exports /backupW/logs
[root@teste ~]# chown -R mgeweb.mgeweb /backupW
[root@teste ~]# echo "30 20 * * * /backupW/scripts/./exportsW.sh" > /var/spool/cron/mgeweb

[mgeweb@localhost ~]$ su -l mgeweb
[mgeweb@localhost ~]$ mkdir modelos

[root@localhost ~]

echo '
pkg# Rotina de Backup Pasta modelos

####################################
####### "Carrega variáveis" ########
####################################

export NLS_LANG=AMERICAN_AMERICA.WE8ISO8859P1
export DATA_ATUAL=$(date "+%Y-%m-%d-%H")
source /home/mgeweb/.bash_profile

###########################
####### "Grava Log"########
###########################

echo `date`"====== Iniciando Backup ["$DATA_ATUAL"] ========"
>> /backupW/logs/Modelos_$DATA_ATUAL.log

# "Deleta arquivos MODELOS dos Ultimos 5 dias"

echo -e "\nDeletado arquivos de backup na pasta /backupW/exports! \n"
find /home/mgeweb/ -name 'server.log.20*' -ctime +15 -exec /bin/rm {} \;
find /backupW/exports/ -maxdepth 2 -type f -ctime +5 -exec rm -vf \{\} \;

###################################
##### "Compacta arquivo "##########
###################################

cd /backup/exports/

tar -czvf Modelos_$DATA_ATUAL.tar.gz /home/mgeweb/modelos
/home/mgeweb/.sw_file_repository

echo `date`"====== Fim Backup ["$DATA_ATUAL"] ======== "
>> /backupW/logs/Modelos_$DATA_ATUAL.log' > /backupW/scripts/./exportsW.sh

[mgeweb@localhost ~]$ chmod +x /backupW/scripts/./exportsW.sh

Confira a Rotina abaixo:

[mgeweb@localhost ~]$ crontab -l

E confira também o Script:

cat /backup/scripts/exportsW.sh
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#top)

![Imagem 16: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/17125324162839) Acesse também:

[Premissas e Pré requisitos para implantação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045373654-Premissas-e-Pr%C3%A9-requisitos-para-implanta%C3%A7%C3%A3o)

[Manual de Instalação Sankhya Om em Ambiente Windows](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-SankhyaW-em-Ambiente-Windows)
