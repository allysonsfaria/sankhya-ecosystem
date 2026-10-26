---
id: "31592968028055"
titulo: "Ação agendada não é executada, o que deve ser verificado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31592968028055-A%C3%A7%C3%A3o-agendada-n%C3%A3o-%C3%A9-executada-o-que-deve-ser-verificado"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:32:34Z"
rotulos: ["Configuração", "Ações Agendadas", "Servidor", "Controle de Jobs", "Ação agendada não é executada o que deve ser verificado?", "Configurar Expressão", "Expressão CRON", "Intervalo de Tempo", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Ação agendada não é executada, o que deve ser verificado?

**(1)** Este artigo tem o objetivo de apoiar na solução de problemas em ações agendadas que não são executadas, sejam elas novas ou que já funcionavam e pararam de funcionar. Abaixo seguem alguns passos que podem ser verificados.

### Verificação do argumento de VM

A primeira verificação a ser realizada é identificar se o argumento de VM **"-Dsankhyaw.schedule.disable"** está ativo no sistema. Quando este argumento está configurado como **"true"** (na administração do servidor ou via arquivo standalone.conf), todas as ações agendadas ficam desabilitadas.

Para resolver este problema, siga os passos abaixo:

**(1)** Acesse as configurações de VM ou o arquivo de configuração do servidor (standalone.conf/bat).

**(2)** Localize o argumento **"Dsankhyaw.schedule.disable"**.

**(3)** Remova o argumento ou altere seu valor para **"false"**.

**(4)** Reinicie o servidor de aplicação para aplicar as alterações.

### Verificação na tela Ações Agendadas

Primeiramente, verifique se a ação está ativa na tela **"Ações Agendadas"** (Configurações >> Avançado >> Ações Agendadas). Estando ativa, ainda nesta mesma tela, verifique na aba **"Configurar Expressão"** se o tipo de gatilho é **"Intervalo de tempo"** ou **"Expressão CRON"**.

**(2)Intervalo de Tempo:** configure de quanto em quanto tempo a ação será executada (segundos, minutos ou horas).

**(2)Expressão CRON:** certifique-se de que a expressão está correta. **Importante:** Ao usar valores fixos para hora e minuto, é obrigatório marcar um valor para o segundo (ex: 0), caso contrário, a ação poderá ser executada 60 vezes por minuto.

### Verificação no Controle de Jobs

**(2)** Acesse a tela **"Controle de Jobs"** (Configurações >> Avançado >> Controle de Jobs) e filtre pela descrição da ação. Nela é possível verificar se o Job existe e se apresenta erros de execução no horário da tentativa.

![Ação agendada não é executada](https://ajuda.sankhya.com.br/hc/article_attachments/31966078495511)

Caso encontre erros como "Esta ação agendada exige autorização pelo administrador do sistema!", acesse a tela **"Autorização de Customização"** (Configurações >> Avançado >> Autorização de Customização) para liberar a execução. Se o Job não for apresentado mesmo com a ação ativa, verifique o parâmetro **SERVERHOSTSCHED** (**SERVERHOSTSCHED**) nas **"Preferências"** (Configurações >> Avançado >> Preferências), que pode estar apontando para um IP de servidor de Jobs inexistente ou incorreto.

**OBS**:. O parâmetro **SERVERHOSTSCHED e**le é responsável por apontar o IP de um servidor exclusivo para execução de schedules (Jobs), ou seja, se tiver um servidor a parte para execução dos Jobs, o ideal é não existir.

Caso ele existe e contenha um caminho incorreto informado, os Jobs não serão executados.**É muito importante que tenha certeza da informação citada antes de realizar qualquer alteração no parâmetro.**

**Importante:** tanto o argumento quanto o parâmetro podem existir intencionalmente na base de testes. Isso evita que Jobs sejam executados de forma incorreta e enviem informações indevidas aos clientes (por exemplo, em Jobs de envio de e-mail). **Portanto, antes de remover qualquer um deles, avalie cuidadosamente os possíveis impactos!**

### Histórico de Execuções

**(3)** Para validar o histórico, utilize o **"Ações Ativas"** na tela de ações. Um pop-up será exibido informando o total de execuções e eventuais motivos de falhas.

![Ação agendada não é executada](https://ajuda.sankhya.com.br/hc/article_attachments/31966078498839)

**Nota:** Se após estas verificações o problema persistir, aconselhamos a abertura de um ticket para o Service Desk.
