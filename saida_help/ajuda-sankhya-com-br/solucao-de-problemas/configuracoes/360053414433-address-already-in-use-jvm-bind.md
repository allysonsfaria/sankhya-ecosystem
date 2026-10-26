---
id: "360053414433"
titulo: "Address already in use: JVM_Bind"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053414433-Address-already-in-use-JVM-Bind"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:29:01Z"
rotulos: ["Porta", "Configuração", "#AGUARDANDOVALIDAÇÃO", "#formatadoroger", "Conflito de Porta", "Identificação de Aplicação", "Alteração de Porta", "Erro", "SAS", "JVM_Bind"]
---

# Address already in use: JVM_Bind

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18524322451095) MENSAGEM**:

Address already in use: JVM\_Bind

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18524322459159) CAUSA**:

Ocorre quando outra aplicação já está utilizando a porta 10050 (porta padrão utilizada pelo SAS), sendo necessário alterar a porta de comunicação do SAS, ou encerrar a aplicação que está utilizando a porta 10050.

**![Imagem 3: SOLUÇÃO : Identificar se a porta 10050 está em uso por outro aplicativo, via prompt de comando(CMD).](https://ajuda.sankhya.com.br/hc/article_attachments/18524334895895) SOLUÇÃO**:
![Imagem 4: SOLUÇÃO : Identificar se a porta 10050 está em uso por outro aplicativo, via prompt de comando(CMD).](https://ajuda.sankhya.com.br/hc/article_attachments/18524334897559) Identificar se a porta 10050 está em uso por outro aplicativo, via prompt de comando(CMD).

1.1- Abra o prompt de comando clicando em Iniciar / Executar e Digite CMD e pressione Enter;

1.2-Digite o comando: **netstat -o -n –a**

Será apresentado o Endereço de IP, seguido da porta (0.0.0.0:10050) e o processo(PID)

![Imagem 5: 1.2-Digite o comando: netstat -o -n –a Será apresentado o Endereço de IP, seguido da porta (0.0.0.0:10050) e o…](https://ajuda.sankhya.com.br/hc/article_attachments/360088733454)

1.3-Agora será preciso, encontrar qual é a aplicação que está trabalhando na porta 10050. Uma dica de comando, pode ser usado, conforme exemplo abaixo.

Descobrir quais aplicações estão trabalhando na porta  10050.
**netstat -o -n -a | findstr  0.0:10050**
**0.0  são os dois números finais do IP 0.0.0.0 e 10050 é a porta**

![Imagem 6: Descobrir quais aplicações estão trabalhando na porta 10050. netstat -o -n -a | findstr 0.0:10050 0.0 são os dois…](https://ajuda.sankhya.com.br/hc/article_attachments/360089886813)

No exemplo, foi encontrado apenas uma aplicação utilizando a porta consultada, e também o número do processo(PID) que é 12148

![Imagem 7: Abra o Gerenciador de Tarefas clicando em Iniciar / Executar e digite taskmgr e pressione Enter;](https://ajuda.sankhya.com.br/hc/article_attachments/18524322481943) Abra o Gerenciador de Tarefas clicando em Iniciar / Executar e digite taskmgr e pressione Enter;

![Imagem 8: Selecione a Aba Detalhes,](https://ajuda.sankhya.com.br/hc/article_attachments/18524334909847) Selecione a Aba Detalhes,

![Imagem 9: Consulte pela coluna PID qual o processo que esta executando na porta consultada no passo 1](https://ajuda.sankhya.com.br/hc/article_attachments/18524334912023) Consulte pela coluna PID qual o processo que esta executando na porta consultada no passo 1

![Imagem 10: Se a aplicação que esta usando a porta 10050 não for o SAS, é possível alterar a configuração do SAS para rodar em…](https://ajuda.sankhya.com.br/hc/article_attachments/18524334921367) Se a aplicação que esta usando a porta 10050 não for o SAS, é possível alterar a configuração do SAS para rodar em outra porta, para isso

5.1-Acesse o diretório onde esta instalada o SAS [<SAS\_HOME>/conf/sas.cfg]
Na pasta CONF, abra o arquivo SAS.cfg em um bloco de nota e edite o ultimo trecho
server.port=**10051**ou para outra porta acima de 10050

![Imagem 11: 5.1-Acesse o diretório onde esta instalada o SAS (<SAS_HOME>/conf/sas.cfg) Na pasta CONF, abra o arquivo SAS.cfg em um…](https://ajuda.sankhya.com.br/hc/article_attachments/18524322505367) Configurações » Avançado » Preferências
Altere a porta do parâmetro **IP do servidor de acessos - IPSERVACESS**, para a nova porta configurada no item 5
Exemplo: **IPDOSERVIDOR:10051**

![Imagem 12: Execute a inicialização novamente do SAS, reinicie a aplicação do Sistema(WildFly).](https://ajuda.sankhya.com.br/hc/article_attachments/18524322511127) Execute a inicialização novamente do SAS, reinicie a aplicação do Sistema(WildFly).
