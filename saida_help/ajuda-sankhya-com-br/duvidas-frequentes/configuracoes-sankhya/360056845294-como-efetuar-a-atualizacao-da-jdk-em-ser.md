---
id: "360056845294"
titulo: "Como efetuar a atualização da JDK em servidor LINUX?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056845294-Como-efetuar-a-atualiza%C3%A7%C3%A3o-da-JDK-em-servidor-LINUX"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:27:04Z"
rotulos: ["#criadoRoger", "Configuração", "Atualização", "jdk", "fuso", "atualizaçao jdk", "horario servidor", "Linux", "Atualização da JDK no Linux", "Sankhya Om", "JivaEvo"]
---

# Como efetuar a atualização da JDK em servidor LINUX?

JDK e um pacote de software que você pode usar para desenvolver aplicativos baseados em **Java**. Este pacote é imprescindível para o uso das aplicações Sankhya Web(Sankhya OM e JivaEvo).

| Recomendamos que solicite a equipe de TI da Empresa, que execute o procedimento abaixo. Também, deve-se programar um horário que não irá interromper a operação da empresa, ou avisar aos usuários sobre a manutenção e que o sistema ficará fora do ar, por alguns instantes. |
| --- |

**Neste artigo trataremos o seguinte incidente:** Versão do servidor de aplicação com fuso horário conforme print abaixo

![Imagem 1: Neste artigo trataremos o seguinte incidente: Versão do servidor de aplicação com fuso horário conforme print abaixo](https://ajuda.sankhya.com.br/hc/article_attachments/360098814793)

Confira o passo a passo para a manutenção da JDK:

![Imagem 2: Faça login no Terminal Server do Linux, via Putty ou via Prompt de Comando. Pare o serviço do WildFly Comando: ps -ef |…](https://ajuda.sankhya.com.br/hc/article_attachments/16250484473239) Faça login no Terminal Server do Linux, via Putty ou via Prompt de Comando. Pare o serviço do WildFly
Comando: **ps -ef | grep wildfly\_producao**Encontre o número do processo (PID), anote:

![Imagem 3: Faça login no Terminal Server do Linux, via Putty ou via Prompt de Comando. Pare o serviço do WildFly Comando: ps -ef |…](https://ajuda.sankhya.com.br/hc/article_attachments/360096500034)

Execute o comando de parar o serviço
Comando: **kill -9 [numero do processo]**

![Imagem 4: Execute o comando de parar o serviço Comando: kill -9 (numero do processo)](https://ajuda.sankhya.com.br/hc/article_attachments/360098814833)

![Imagem 5: Verifique a versão da distribuição do Linux, versão da JDK e arquitetura (32 ou 64bits)](https://ajuda.sankhya.com.br/hc/article_attachments/16250508428823) Verifique a versão da distribuição do Linux, versão da JDK e arquitetura (32 ou 64bits)

Comando: **cat /etc/redhat-release**
Versão do Linux: CentOS Linux....
Comando: **java -version
Java version '1.8.0\_271'**Comando:**uname –m**x86\_64 = 64 Bits
i386 = 32 Bits

![Imagem 6: Comando: cat /etc/redhat-release Versão do Linux: CentOS Linux.... Comando: java -version Java version '1.8.0_271'…](https://ajuda.sankhya.com.br/hc/article_attachments/360098814813)

![Imagem 7: Baixe a JDK de acordo com a arquitetura informada acima: http://downloads.sankhya.com.br/ Em (Ferramentas>>Java JDK) ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16250484478743) Baixe a JDK de acordo com a arquitetura informada acima:
<http://downloads.sankhya.com.br/> Em (Ferramentas>>Java JDK)
ou
https://www.oracle.com/br/java/technologies/javase/javase-jdk8-downloads.html (necessario cadastro)

Exemplo: **JDK 8u231** (Linux 64 bits) ou **jdk-8u271-linux-x64.tar.gz**

Transfira para a pasta /home/mgeweb via [WinSCP](https://winscp.net/eng/download.php)

![Imagem 8: Transfira para a pasta /home/mgeweb via WinSCP](https://ajuda.sankhya.com.br/hc/article_attachments/360098814873)

Extraia com o comando abaixo:

Comando: **tar -xzvf jdk-xxxx-linux-x64.tar.gz**

![Imagem 9: Comando: tar -xzvf jdk-xxxx-linux-x64.tar.gz](https://ajuda.sankhya.com.br/hc/article_attachments/360098814893)

![Imagem 10: Remova JDK Antiga e link simbólico.](https://ajuda.sankhya.com.br/hc/article_attachments/16250484480791) Remova JDK Antiga e link simbólico.

Comandos: **rm -rf jdk.jdkx.x.x\_156 (exemplo)**
**rm -rf jdk8**

![Imagem 11: Crie link simbólico:](https://ajuda.sankhya.com.br/hc/article_attachments/16250484482455) Crie link simbólico:

Comandos: **cd jdkx.x.x\_xx**
**pwd**
**/home/mgeweb/jdkx.x.x\_xx**
**ln -s /home/mgeweb/jdk1.8.0\_231/ /home/mgeweb/jdk8**

![Imagem 12: Consulte a versão atual novamente](https://ajuda.sankhya.com.br/hc/article_attachments/360096500074)

![Imagem 13: Consulte a versão atual novamente](https://ajuda.sankhya.com.br/hc/article_attachments/16250484484759) Consulte a versão atual novamente

Comando: **java -version**

![Imagem 14: Remova pastas temporárias do WildFly](https://ajuda.sankhya.com.br/hc/article_attachments/16250508442263) Remova pastas temporárias do WildFly

Comandos: **cd /wildfly\_producao/standalone/**
**ls (confira as pastas) e execute o comando abaixo.**
**rm -rf tmp log sysmon**

![Imagem 15: Comandos: cd /wildfly_producao/standalone/ ls (confira as pastas) e execute o comando abaixo. rm -rf tmp log sysmon](https://ajuda.sankhya.com.br/hc/article_attachments/360096500094)

![Imagem 16: Inicie o WildFly](https://ajuda.sankhya.com.br/hc/article_attachments/16250484489879) Inicie o WildFly

8.1: Executando o atalho: **jb\_startprod**

ou

8.2: Executando o comando: **nohup ./standalone.sh > /dev/null &**

![Imagem 17: Aguarde alguns minutos, até que a aplicação seja iniciada, solicite aos usuários da aplicação que acessem novamente o…](https://ajuda.sankhya.com.br/hc/article_attachments/16250484490775) Aguarde alguns minutos, até que a aplicação seja iniciada, solicite aos usuários da aplicação que acessem novamente o SankhyaW/JivaEvo.

**![Imagem 18: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16250508455575) OBSERVAÇÃO:**

Recomendável limpar o cache dos navegadores, após o procedimento.
