---
id: "28819466067095"
titulo: "Configurações para evitar quedas esporádicas e aleatórias do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28819466067095-Configura%C3%A7%C3%B5es-para-evitar-quedas-espor%C3%A1dicas-e-aleat%C3%B3rias-do-sistema"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:37:34Z"
rotulos: ["Configuração", "Atualização", "Banco de dados", "\"%T.Nat\" (contribuição) \"%T.Rec\" (receitas) \"%T.Desp\" (despesas)", "Configurações para evitar quedas esporádicas e aleatórias do sistema", "WildFly", "standalone.xml", "JDK", "desconexão", "desconenctando", "Infraestrutura"]
---

# Configurações para evitar quedas esporádicas e aleatórias do sistema

**SITUAÇÃO**

Os passos a seguir servem como forma de evitar as quedas de sessões de usuários que ocorrem durante o uso do sistema, tendo como premissa que essas quedas não são causadas pelas configurações de time out.

**SOLUÇÃO**

Os passos a seguir são atividades de infraestrutura que devem ser executadas por um profissional com conhecimento técnico em banco de dados e servidores de aplicação. O Service Desk não realiza este procedimento.

#### **(1)** Atualização do WildFly:

Em primeiro lugar, verifique a versão do WildFly e caso não esteja na última versão (observar o mod além da versão), atualize através da [Central de Downloads:](https://downloads.sankhya.com.br/downloads?app=WildFly&c=1)

![Imagem 1: Em primeiro lugar, verifique a versão do WildFly e caso não esteja na última versão (observar o mod além da versão),…](https://ajuda.sankhya.com.br/hc/article_attachments/40077239480983)

#### **(1)** Configuração do Banco de Dados

Após a atualização do WildFly, configure o banco de dados utilizando a seguinte documentação:

**Para ambientes Linux:**
**-** [Como atualizar o Wildfly - Linux?](https://ajuda.sankhya.com.br/hc/pt-br/articles/35196444326423-Como-atualizar-o-Wildfly-Linux)

[- Configuração para Banco de Dados Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3oparaBancodeDadosOracle)

- [Configuração para Banco de Dados SQL Server](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux#Configura%C3%A7%C3%A3oparaBancodeDadosSQLServer)

**Para ambientes Windows:**

**-** [Como atualizar o Wildfly - Windows?](https://ajuda.sankhya.com.br/hc/pt-br/articles/38109965528087-Como-atualizar-o-Wildfly-em-sistema-operacional-Windows)

[- Configuração para Banco de Dados Oracle](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Windows#Configura%C3%A7%C3%A3oparaBancodeDadosOracle)

[- Configuração para Banco de Dados SQL Server](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Windows#Configura%C3%A7%C3%A3oparaBancodeDadosSQLServer)

#### **(1)** Atualização do JDK

Após a atualização do WildFly é necessário verificar se o JDK está compartivel com a versão do Wildfly, essas versões do JDK são 8u421 à 11

- [Como efetuar a atualização da JDK em servidor LINUX?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056845294-Como-efetuar-a-atualiza%C3%A7%C3%A3o-da-JDK-em-servidor-LINUX)

[- Como efetuar a atualização da JDK em servidor Windows?](https://ajuda.sankhya.com.br/hc/pt-br/articles/39011143271447-Como-efetuar-a-atualiza%C3%A7%C3%A3o-da-JDK-em-servidor-Windows)

####
