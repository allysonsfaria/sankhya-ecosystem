---
id: "4414199283735"
titulo: "Eventos Temporais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:11:14Z"
rotulos: ["Configuração", "Eventos", "Projeto", "Agendamento", "sankhyaflow", "Eventos Temporais", "Início Intermediário Borda (Interrupto/Ininterrupto)", "Defina tempo de início pausa ou ações de borda", "Processo inicia todo dia 12 pausa por 1 dia e alerta por e-mail se atraso"]
---

# Eventos Temporais

| ``` ![Imagem 1: Versão disponível: a partir da 3.2](https://ajuda.sankhya.com.br/hc/article_attachments/42313360086295) Versão disponível: a partir da 3.2 ``` |
| --- |

---

Evento temporal é um recurso que permite colocar no fluxo do processo situações relacionadas a tempo, tempo no sentido de determinadas datas, horários, minutos, etc.

Existem três tipos de Eventos Temporais disponíveis para ser utilizado no fluxo do processo. São eles:

- **Evento de Início Temporal:** O processo pode ser iniciado em função de um tempo definido.
- **Evento Intermediário:** Esse Evento pausa o fluxo do processo por determinado tempo definido.
- **Evento de borda:** Esse Evento é colocado na borda da Tarefa de Usuário para que caso a tarefa não for finalizada em um determinado tempo o fluxo do processo seguirá por um outro caminho, sendo ele de dois tipos:

**- Interrupto:** A tarefa que contém esse evento na borda é finalizada.

**- Ininterrupto:** A tarefa que contém esse evento na borda não é finalizada.

Esse processo pode ser utilizado quando o modelador identifica que o processo precisa sempre ser iniciado em uma data ou horário fixo. A título de exemplo, suponhamos que o modelador do processo definiu que um processo da área Contábil de geração de holerites, será iniciado todo dia 15 de todos os meses do ano, dessa forma o processo é iniciado automaticamente todo dia 15 do mês.

Quando é necessário interromper o processo por determinado tempo e só poder retomar o processo depois desse tempo decorrido. Por exemplo, no processo produtivo em uma indústria de químicos, o processo produtivo só deve continuar após 24 horas de pausa para descanso do produto, após esse período o processo produtivo é retomado.

Ainda é possível colocar um Evento na Borda de uma Tarefa de Usuário nos cenários em que caso a tarefa não seja finalizada em determinado tempo, o fluxo do processo pode seguir outro caminho. Como por exemplo, em um processo de atendimento de manutenção, quando o usuário que está atendendo e em 12 horas ele não consegue solucionar o atendimento ele é escalado, passa para um atendimento Nível 2.

Nessa documentação trataremos sobre nosso [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#casodeuso), [Como configurar os Eventos Temporais do processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#Comoconfiguraroseventostemporaisdoprocesso) e os [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#resultados).

---

#### Caso de Uso

A empresa Beta Ltda., utiliza o SankhyaFlow em seu processo de **"Manutenção Preventiva de Equipamentos"** que está representado na imagem abaixo:

![Imagem 2: A empresa Beta Ltda. , utiliza o SankhyaFlow em seu processo de "Manutenção Preventiva de Equipamentos" que está…](https://ajuda.sankhya.com.br/hc/article_attachments/4414185320855)

**Processo de Manutenção Preventiva de Equipamentos**

Este processo contempla as etapas: **"Analisar equipamento"**, **"Separar peças"** e **"Realizar manutenção"**. Sendo a tarefa Separar peças um subprocesso onde o setor de almoxarifado executa a separação das peças.

Se tratando de manutenção preventiva de equipamentos o processo tem data fixa de iniciar, sendo ela todo dia 12 independente do mês, todo dia 12 às 5 impressoras a Laser precisam ser revisadas e eventualmente reparadas. Para cada impressora é gerada uma única tarefa em multiplicidade paralela de Analisar equipamento totalizando então 5 tarefas.

Para mais informações sobre multiplicidade consulte a documentação [Multiplicidade na Tarefa de Usuário](https://drive.google.com/drive/folders/1C3Pg-aMJC5HHlxrI3uFzqWCHu0emuO4I?usp=sharing).

O processo Separar peças contém as Tarefas de Usuário: **"Analisar separação de peças"** e **"Entrega das peças"**, além da tarefa de email **"Email ao gestor"**.

![Imagem 3: O processo Separar peças contém as Tarefas de Usuário : "Analisar separação de peças" e "Entrega das peças" , além da…](https://ajuda.sankhya.com.br/hc/article_attachments/4414185436951)

**Processo de Solicitação de peças**

Neste processo a tarefa Analisar separação de peças possui uma regra, onde ela precisa ser finalizada em até 2 dias.  Caso isso não aconteça, um e-mail será enviado ao gestor da área. Além disso, existe um prazo de espera pela separação depois que ela passa pela atividade de Analisar separação de peças, portanto, o processo é pausado por 1 dia ao chegar neste ponto do fluxo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#top)

#### Como configurar os Eventos Temporais do processo

Como descrito no caso de uso do processo Manutenção Preventiva de Equipamentos é necessário que ele se inicie automaticamente todo dia 12 do mês, para isto vamos configurar um Evento de Início Temporal. Desse modo, no primeiro elemento do fluxo do processo, clique em **"Alterar tipo"** e selecione a opção **"Evento de Início de Tempo"**, conforme abaixo:

[GIF animado: Imagem 4: Como descrito no caso de uso do processo Manutenção Preventiva de Equipamentos é necessário que ele se inicie…](https://ajuda.sankhya.com.br/hc/article_attachments/4414185820439)

**Selecionando o Evento de Início de Tempo**

Agora, é necessário configurar quando esse evento vai iniciar, o modelador tem a possibilidade de definir qualquer tempo seja minutos, dias, horas, etc. Neste caso de uso vamos configurar para iniciar todo dia 12.

Para realizar esta configuração, o modelador deve clicar no botão , assim será aberto um pop-up, onde pode-se determinar e validar a definição de tempo configurada:

[GIF animado: Imagem 5: Para realizar esta configuração, o modelador deve clicar no botão , assim será aberto um pop-up, onde pode-se…](https://ajuda.sankhya.com.br/hc/article_attachments/4414383234327)

**Pop-up de configuração do Evento de Início Temporal**

Ao clicar em **"Validar Expressão"**, será apresentada a mensagem abaixo, na qual podemos conferir se a configuração está correta e que o processo será iniciado no próximo dia 12:

**"Próxima execução em: 12/11/2021 00:00:00"**

Dado as regras de negócio deste processo é necessário que o fluxo contenha dois Eventos Temporais, como descrito no caso de uso será necessário interromper o fluxo do processo como também disparar um e-mail ao gestor em caso de atraso em uma das tarefas, portanto vamos colocar no fluxo o **"Evento Intermediário de Tempo"** e o **"Evento de borda temporal (não interrupto)"**. Trataremos a seguir destes dois tipos de eventos: 

**Evento Intermediário de Tempo**  

A primeira tarefa de usuário do processo é **"Analisar separação de peças"**, o almoxarifado informou que só poderia entregar as peças no dia seguinte, pedindo então 1 dia de espera para despachar as peças, assim, para interromper o processo por 1 dia utilizaremos o Evento Intermediário de Tempo.

Para definir esse evento no processo é necessário selecionar na palheta de eventos que fica à esquerda da tela, a opção de **"Criar Eventos Intermediário"** e posicionar ele entre as tarefas Analisar solicitação de peças e Entrega das peças:

[GIF animado: Imagem 6: Para definir esse evento no processo é necessário selecionar na palheta de eventos que fica à esquerda da tela, a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/4414200262935)

**Configurando o Evento Intermediário**

Após colocar o evento entre as Tarefas de Usuário é necessário configurar definindo ele para ser um Evento Intermediário de Tempo. Feito isso, na parte direita da tela existe um campo para definirmos quantos minutos o fluxo será interrompido, por regra é 1 dia de pausa, ou seja, 1440 minutos:

![Imagem 7: Após colocar o evento entre as Tarefas de Usuário é necessário configurar definindo ele para ser um Evento…](https://ajuda.sankhya.com.br/hc/article_attachments/4414200280343)

**Configurando os minutos do Evento Intermediário de Tempo**

**Evento de borda temporal (não interrupto)**

Neste caso de uso não existe a necessidade de cancelar a tarefa caso ela estoure o tempo acordado, apenas de enviar o email ao gestor para avisá-lo que o tempo foi excedido. Dado esse cenário, vamos utilizar na borda da tarefa Analisar separação de peças o Evento de Borda temporal Ininterrupto. Para isto, arraste um Evento Intermediário para a borda da tarefa e altere o tipo dele para o evento que precisamos:

![Imagem 8: Neste caso de uso não existe a necessidade de cancelar a tarefa caso ela estoure o tempo acordado, apenas de enviar o…](https://ajuda.sankhya.com.br/hc/article_attachments/4414383560215)

**Selecionando o Evento de Tempo de Borda Não Ininterrupto**

Agora, precisamos definir o tempo neste evento, a regra acordada no processo é que se em 2 dias ela não for finalizada o gestor do time de separação deve ser avisado, portanto, o evento deve ser definido para 2880 minutos:

![Imagem 9: Definindo o tempo do Evento](https://ajuda.sankhya.com.br/hc/article_attachments/4414374059543)**Definindo o tempo do Evento**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#top)

#### Resultados

Dia 12 chegou e foi automaticamente aberto o processo de **"Manutenção Preventiva de Equipamentos"** para as impressoras. O usuário ALEX.SILVA é quem executa a primeira tarefa de analisar os equipamentos, para cada impressora ele vai descrevendo as observações e se é necessário ou não requisitar um Kit Reparador de Impressora.

![Imagem 10: Dia 12 chegou e foi automaticamente aberto o processo de "Manutenção Preventiva de Equipamentos" para as impressoras. O…](https://ajuda.sankhya.com.br/hc/article_attachments/4414383739671)

**Analisando equipamento**

Após a finalização da atividade, o fluxo do processo segue para o Subprocesso **"Separar peças"**, sendo que a usuária ANA.ARAUJO é responsável por esta atividade e tem acesso às informações que levaram ao pedido da peça de manutenção da impressora.

Ela acabou estourando o tempo acordado para finalização da atividade, isto é, 3 dias depois do seu início, e isso fez com que o Evento de Borda fosse utilizado, disparando um e-mail ao gestor do setor de almoxarifado, conforme imagem abaixo:

![Imagem 11: Ela acabou estourando o tempo acordado para finalização da atividade, isto é, 3 dias depois do seu início, e isso fez…](https://ajuda.sankhya.com.br/hc/article_attachments/4414220147607)

**E-mail sinalizando o atraso na atividade.**

Após tarefa de Analisar separação de peças finalizada conforme a regra de negócio do caso de uso o processo é pausado por 1 dia aguardando o setor de almoxarifado fazer a separação da peça e só após o tempo decorrido o processo inicia a tarefa **"Entrega das peças"**.

Para os cenários em que a regra de negócio diz que é necessário finalizar a Tarefa de Usuário que contém o evento de borda, podemos utilizar a variação do evento de borda que é o interrupto.

Neste evento, quando o tempo decorrido é atingido, a Tarefa de Usuário é finalizada automaticamente e o fluxo do processo segue pelo caminho definido através do Evento de borda temporal Interrupto. Podemos conferir na imagem abaixo um exemplo de configuração deste evento.

![Imagem 12: Neste evento, quando o tempo decorrido é atingido, a Tarefa de Usuário é finalizada automaticamente e o fluxo do…](https://ajuda.sankhya.com.br/hc/article_attachments/4414383925271)

**Configuração de um Evento de borda temporal (interrupto)**

Ao finalizar uma tarefa manualmente, usando o botão **"Finalizar Tarefa"**, o sistema executa uma rotina que salva automaticamente as informações do formulário em uma tabela do sistema (quando o formulário estiver ligado a um processo com tabela nativa).

No entanto, se a tarefa for finalizada automaticamente por um temporizador, o sistema apenas encerra a tarefa e passa para a próxima etapa, sem salvar os dados do formulário no banco de dados. Ou seja, nenhuma informação será registrada se o processo usar uma tabela nativa e for finalizado dessa forma.

Se você quiser garantir que os dados sejam salvos mesmo com o uso de temporizador, é possível criar um módulo Java personalizado e configurá-lo no evento de finalização da tarefa, na aba **"Eventos"** do BPMN.
![Imagem 13: Se você quiser garantir que os dados sejam salvos mesmo com o uso de temporizador, é possível criar um módulo Java…](https://ajuda.sankhya.com.br/hc/article_attachments/32153685501591) Ao optar por essa abordagem manual, o processo não passará pelas validações automáticas do sistema; por isso, é importante ter muito cuidado ao implementá-la.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414199283735-Eventos-Temporais#top)
