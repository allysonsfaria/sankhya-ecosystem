---
id: "1500002572921"
titulo: "O Windows não pôde interromper o serviço Sankhya-W wildfly em Computador local"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002572921-O-Windows-n%C3%A3o-p%C3%B4de-interromper-o-servi%C3%A7o-Sankhya-W-wildfly-em-Computador-local"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:32Z"
rotulos: ["#criadoRoger", "Configuração", "Sankhya-W", "Serviços", "#solicitadoBraga", "Erro 1053", "Falha na Interrupção do Serviço Sankhya-W Wildfly", "WildFly", "Erro"]
---

# O Windows não pôde interromper o serviço Sankhya-W wildfly em Computador local

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16302703116951) MENSAGEM**:

O Windows não pôde interromper o serviço Sankhya-W wildfly em Computador local.

[Erro 1053]: O serviço não respondeu à requisição de inicio ou controle em tempo hábil.

**![Imagem 2: S OLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302703118871) SOLUÇÃO:**

Para resolver o problema, aumente o timeout (tempo limite) seguindo os passos abaixo:

![Imagem 3: Abra o Regedit](https://ajuda.sankhya.com.br/hc/article_attachments/16302703121943) Abra o [Regedit](https://support.microsoft.com/pt-br/help/4027573/windows-open-registry-editor-in-windows-10)

![Imagem 4: Navegue até: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control](https://ajuda.sankhya.com.br/hc/article_attachments/16302703122839) Navegue até: **HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control**

![Imagem 5: Altere o valor da chave WaitToKillServiceTimeout para 600000 (10 minutos)](https://ajuda.sankhya.com.br/hc/article_attachments/16302703131159) Altere o valor da chave **WaitToKillServiceTimeout** para 600000 (10 minutos)

Caso não tenha a chave em questão, crie um novo “Valor da Cadeia de Caracteres” clicando com o botão direito do mouse na pasta “Control”, conforme a imagem a seguir.

![Imagem 6: Caso não tenha a chave em questão, crie um novo “Valor da Cadeia de Caracteres” clicando com o botão direito do mouse…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002536421)

**(1)** O Wildfly/JBoss é um servidor de aplicações Java Web sobre o qual é executado o Sankhya-W.

**![Imagem 7: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16302695997207) CAUSA**:

O Wildfly possui um comportamento na execução da finalização, ele aguarda algumas tarefas concluírem para então dar início ao processo de stop. Isto pode ser observado aqui:
(I) Nós inicializamos o Wildfly, (II) aguardamos o início do deploy do Sankhya-W e (III) neste momento nós acessamos a tela de serviços do Windows e finalizamos o Wildfly. O Wildfly aguarda então todo o processo de deploy do Sankhya-W para só então iniciar o processo de finalização. Veja o ocorrido conforme trechos dos dois arquivos de log:

![Imagem 8: O Wildfly possui um comportamento na execução da finalização, ele aguarda algumas tarefas concluírem para então dar…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002536521)

Neste caso com o timeout padrão de 20 segundos não haveria tempo suficiente para todo o processo de finalização, o erro seria inevitável (e foi – nós simulamos). Em alguns servidores o processo de inicialização pode gastar algo próximo a 10 minutos e isso estoura o timeout de finalização do serviço. Claro que é raro uma situação destas, parar um serviço que acabara de ser inicializado, mas o que evidenciamos aqui é o fato de que o Wildfly aguarda algumas rotinas se concluírem antes de ter disparar o processo de shutdown.
