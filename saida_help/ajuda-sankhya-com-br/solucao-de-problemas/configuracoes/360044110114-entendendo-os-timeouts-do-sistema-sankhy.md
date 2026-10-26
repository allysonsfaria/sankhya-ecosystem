---
id: "360044110114"
titulo: "Entendendo os timeouts do sistema- Sankhya-W/ Jiva-W"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110114-Entendendo-os-timeouts-do-sistema-Sankhya-W-Jiva-W"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:53:51Z"
rotulos: ["Configuração", "Timeouts do Sistema: Uma Visão GeralConfigurações Comportamento", "SankhyaW", "Desempenho", "Timeout", "JivaW"]
---

# Entendendo os timeouts do sistema- Sankhya-W/ Jiva-W

(1)** Timeout** é um termo em inglês utilizado para determinar um limite de tempo, e na computação isso é muito utilizado para limitar o tempo máximo que um procedimento ou rotina pode executar ininterruptamente.
A plataforma **SankhyaOm** possui alguns tipos de timeouts e cada um deles determina limites diferentes, como segue:

**![Imagem 1: Timeout de query](https://ajuda.sankhya.com.br/hc/article_attachments/16311042467735) Timeout de query**

Esse timeout determina o limite de tempo que o sistema espera pela resposta em consultas e outros comandos no banco de dados (select, update, insert, delete).
Ao atingir o limite de tempo, o banco de dados será notificado pela aplicação para que ele “desista” da operação e retorne um erro.

**(2)** No caso do Oracle esse erro é: **"ORA-01013 user requested cancel of current operation"** ou em português: **"ORA-01013 o usuário solicitou o cancelamento da operação atual".**

**(2)** Para o SQLServer, as mensagens a ser apresentadas são: Em inglês: "**The query has timed"** out ou em português: **"O tempo limite da consulta foi atingido".** Esse timeout é definido pelo atributo -Djape.global.query.timeout (em segundos) e deve ser configurado em &lt;WILDFLY&gt;/bin/standalone.conf (Linux) ou &lt;WILDFLY&gt;/bin/standalone.conf.bat (Windows), o valor padrão para este atributo é de 600 segundos equivalendo a 10 minutos.

![Imagem 2: Timeout de sessão](https://ajuda.sankhya.com.br/hc/article_attachments/16311010047639) **Timeout de sessão**

Esse tempo determina quanto tempo uma operação completa pode durar. Em uma operação completa podemos ter diversas transações e milhares de interações com o banco de dados (select/updates/inserts/deletes), portanto ela determina a janela total de tempo em uma operação. Em termos práticos, seria o tempo total decorrido entre o usuário clicar em um botão na tela, a requisição chegar ao servidor, ser totalmente processada e a resposta gerada.
Esse timeout é definido pelo atributo -Djape.session.timeout (em milisegundos) no arquivo &lt;WILDFLY&gt;/bin/standalone.conf (Linux) ou &lt;WILDFLY&gt;/bin/standalone.conf.bat (Windows). Ao atingir o limite de tempo, será apresentado ao usuário a mensagem **“JapeSession timeout”** Na ausência de configuração o valor padrão é de 1800000 ms, ou seja, 30 minutos.

![Imagem 3: Timeout de transação](https://ajuda.sankhya.com.br/hc/article_attachments/16311042475799) **Timeout de transação**

Esse é o tempo máximo de uma transação com o banco de dados (TRANSACTION\_TIME\_OUT). Uma operação no sistema pode compreender diversas transações e esse timeout determina o tempo limite de cada uma delas, não a somatória. Ao acontecer esse tipo de timeout a transação é automaticamente desfeita (rollback) e para o usuário é apresentada uma mensagem do tipo **“Transaction is not active”** ou &quot;Could not commit transaction&quot;
Se uma determinada operação compreende diversas transações e uma delas teve o limite de tempo excedido, então apenas ela vai sofrer rollback, ficando as anteriores com o status “COMMITED”. Atualmente, é possível configurar este timeout pelo sistema a partir da tela **“Administração do Servidor”**, aba **“Avançado”**, conforme imagem abaixo:

![Imagem 4: Esse é o tempo máximo de uma transação com o banco de dados (TRANSACTION_TIME_OUT). Uma operação no sistema pode…](https://ajuda.sankhya.com.br/hc/article_attachments/12463588527511)
