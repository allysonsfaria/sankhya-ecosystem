---
id: "4406903288855"
titulo: "Eventos de Processo e Eventos de Tarefa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:10:11Z"
rotulos: ["Configuração", "Eventos", "Processo", "sankhyaflow", "Eventos de Processo e Eventos de Tarefa", "Definição de onde e quando executar scripts", "Scripts automáticos em processos e tarefas", "Envio de e-mail e ajustes de parâmetros", "JavaScript", "Tarefa"]
---

# Eventos de Processo e Eventos de Tarefa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313294125463) Versão: a partir da 4.6
```

---

O Evento tem o poder de definir um script associado a um determinado cenário, ou seja, quando algo acontecer em uma Tarefa de Usuário ou no Processo, podemos definir que um script seja executado. Diferentemente da Tarefa de Serviço que é possível modelar de forma independente e em qualquer ponto do fluxo de processo, os Eventos são obrigatoriamente relacionados a acontecimentos na utilização do processo.

Quando os Eventos são configurados, poderão auxiliar desde automação até integrações com outros módulos Sankhya e outros sistemas ao longo do processo. Ele permite scripts em várias linguagens, definidos para executar em vários pontos ou contextos de Processo e de Tarefa de Usuário, como por exemplo, quando for inserido um apontamento em uma tarefa, um Evento poderá disparar uma notificação a um determinado grupo de usuários.

Um outro exemplo é o processo de **"Manutenção de Equipamentos"**, onde o modelador poderá definir que na finalização da tarefa **"Realizar Manutenção"**, um script execute e faça a baixa do produto utilizado na manutenção, sem a necessidade do usuário ter que sair do processo e acessar uma outra tela para fazer essa baixa manualmente.

Nessa documentação, trataremos sobre os seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#casodeuso)
2. [Configurando os Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#configurandooseventos)
3. [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#resultados)
4. [Demais Eventos disponíveis no contexto de Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#demaiseventosdispon%C3%ADveisnocontextodeprocesso)
5. [Demais Eventos disponíveis no contexto de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#demaiseventosdispon%C3%ADveisnocontextodetarefas)

---

#### Caso de Uso

O processo **"Solicitação de Compras"** exibido na imagem abaixo, foi modelado a fim de atender a proposta de simplificar uma solicitação de compra, tanto para o usuário quanto para automatização do lançamento da solicitação.

![Imagem 2: O processo "Solicitação de Compras" exibido na imagem abaixo, foi modelado a fim de atender a proposta de simplificar…](https://ajuda.sankhya.com.br/hc/article_attachments/4406994313239)

| **Solicitação de Compras** |
| --- |

O processo possui 3 Tarefas de Usuário: **"Analisar a Solicitação"**, **"Realizar cotação"** e **"Refazer Solicitação"**, possui 1 Tarefa de Serviço, que é a **"Geração de pedido de compras"** e por fim, possui também 2 Tarefas de E-mail para notificação dos cenários de reprovação ou status do pedido.

Na Tarefa de Usuário Realizar Cotação existe a necessidade de enviar um e-mail no exato momento em que o responsável por essa tarefa começa a trabalhar nela. O intuito é de avisar em tempo real o andamento da compra para o solicitante do processo.

A Tarefa de Serviço Geração de pedido de compras é responsável por gerar o pedido na Central de Compras; para isso, são obrigatórias algumas informações da empresa que está emitindo o pedido, como por exemplo: Tipo de Operação, Tipo de Negociação, Natureza e etc. A fim de facilitar o ajuste dessas informações para se adequar a qualquer empresa que queira utilizar o processo, esses parâmetros não são contemplados na implementação da Tarefa de Serviço pois, como são informações relacionadas a cada pedido de venda gerado, elas precisam constar no contexto de processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#top)

#### Configurando os Eventos

Para a necessidade de definição dos parâmetros para gerar o pedido de compras, utilizamos o recurso de Evento na inicialização do Processo.

Para acessar a aba Eventos no contexto de Processo, basta dar um duplo clique em qualquer área branca do fluxograma; com isso, o painel lateral à direita se abrirá na tela.

Nesse painel, temos a aba **"Eventos"**. Posicionada nela, clique no botão para abrir o pop-up **"Configuração de Evento"** para adicionar um novo Evento:

[GIF animado: Imagem 3: Nesse painel, temos a aba "Eventos" . Posicionada nela, clique no botão para abrir o pop-up "Configuração de Evento"…](https://ajuda.sankhya.com.br/hc/article_attachments/4407022480279)

| **Configuração de Evento** |
| --- |

Com o pop-up aberto, podemos adicionar um novo Evento e também podemos editar os que já estiverem cadastrados no processo. Primeiramente, iremos inserir o **"Nome do Evento"** que será Parâmetros da Empresa.

O campo **"Onde"** é de multisseleção e indica o momento em que o Evento vai acontecer. Nesse ponto, temos as opções de Processo, Formulário Embarcado e Formulário Formatado. Conforme as regras de negócio descritas no [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#casodeuso), utilizaremos a opção Processo.

Ao selecionar que o campo Onde será no contexto de Processo, precisamos definir a **"Ação"**. Nesse campo, temos as opções **"Iniciar"** e **"Finalização"**, ambas relacionadas ao Processo. Em nosso caso, iremos utilizar a opção Iniciar. Assim, com esses dois campos definimos o exato momento em que o script será executado.

Os scripts podem ser escritos em **"Java"**, **"JavaScript"** ou **"Procedure"**, bastando que você sinalize qual desses será o script dentro da Configuração de Evento. Para o nosso caso de uso iremos utilizar um script em JavaScript. Abaixo demonstramos como definir a linguagem a ser utilizada no script e, logo em seguida, o script do Evento:

[GIF animado: Imagem 4: Os scripts podem ser escritos em "Java" , "JavaScript" ou "Procedure" , bastando que você sinalize qual desses será o…](https://ajuda.sankhya.com.br/hc/article_attachments/4407022349079)

| **Definindo a linguagem do Script** |
| --- |

| ``` //Dados a serem alterados para adequar a realidade da empresa que utilizará  o processo de Solicitação de Compras no SankhyaFlow  var data = new Date();   setCampo("CODEMP", 1); //Código da empresa  setCampo("CODTIPOPER", 7); //Tipo de Operação  setCampo("CODTIPVENDA", 5);  //Tipo de Negociação  setCampo("CODNAT", 3020600); //Natureza  setCampo("CODCENCUS", 10300);  //Centro de Resultado  setCampo("DTNEG",'' + data.getDate() + '/' + data.getMonth() +'/' + data.getFullYear());  ``` |
| --- |

Após a inserção do script, basta salvar; assim, o Evento já estará definido e contendo o script necessário para poder gerar o pedido de compras. Note que, depois de adicionado o Evento, é possível ler as definições dele, bastando abrir o painel lateral do Processo na aba Eventos:

![Imagem 5: Após a inserção do script, basta salvar; assim, o Evento já estará definido e contendo o script necessário para poder…](https://ajuda.sankhya.com.br/hc/article_attachments/4407013725463)

| **Painel de controle dos Eventos** |
| --- |

Para a necessidade de enviar um e-mail no instante em que for atribuída a tarefa de **"Realizar Cotação"**, utilizamos o recurso de Evento na Atribuição/Desatribuição da Tarefa. No campo Ação, temos as opções **"Atribuição/Desatribuição"**, **"Criação"** e **"Finalização"**, todas relacionadas à Tarefa em que o Evento está sendo definido.

Para acessar a aba Eventos no contexto de Tarefa, dê um duplo clique na atividade Realizar Cotação para que seja aberto o painel lateral. Clicando no botão , teremos acesso ao pop-up Configuração de Evento para adicionar um novo Evento.

Primeiramente, devemos inserir o Nome do Evento que será Envio de E-mail. O campo Onde indica onde o Evento vai acontecer; portanto, em nosso cenário, queremos que o Evento aconteça na Tarefa e a Ação seja de Atribuição/Desatribuição.

Com esses dois campos temos então definido o exato momento em que o script será executado. O Onde na tarefa Realizar Cotação em junção da Ação que será no ato de atribuir a tarefa.

Novamente, escrevemos o script do Evento em JavaScript:

| ``` var emailSolicitante = getEmailSolicitante; eMail("Cotação foi iniciada", "Sua cotação esta sendo realizada e logo mais teremos um resultado",  emailSolicitante); ``` |
| --- |

Após a inserção do script, basta salvar. Dessa forma, o Evento já está definido e contendo o script necessário para poder enviar o e-mail ao solicitante. Note que, depois de adicionado o Evento, será possível ler as definições acessando a tarefa a qual foi definido o Evento:

![Imagem 6: Após a inserção do script, basta salvar. Dessa forma, o Evento já está definido e contendo o script necessário para…](https://ajuda.sankhya.com.br/hc/article_attachments/4407023032215)

| **Painel de controle dos Eventos** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#top)

#### Resultados

O processo **"Pedido de Compras"** foi iniciado e para isso é necessário o preenchimento de 3 campos: **"Produto"**, **"Quantidade"** e **"Observação"**:

![Imagem 7: O processo "Pedido de Compras" foi iniciado e para isso é necessário o preenchimento de 3 campos: "Produto" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4407006592279)

| **Lançamento do Pedido** |
| --- |

Após o pedido lançado, o processo passa pela atividade **"Realizar Cotação"** e quando a cotação é finalizada, o pedido então é gerado na Central de Compras, contendo todas as informações necessárias para gerar o pedido e que foi escrito no script contido no Evento que descrevemos no tópico [Configurando os Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#configurandooseventos).

Quando o processo chega na tarefa Realizar Cotação e ela é atribuída, o Evento descrito no tópico [Configurando os Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#configurandooseventos) entra em ação e envia um e-mail ao solicitante que fez a abertura do processo. Podemos conferir na imagem abaixo o e-mail recebido:

![Imagem 8: Quando o processo chega na tarefa Realizar Cotação e ela é atribuída, o Evento descrito no tópico Configurando os…](https://ajuda.sankhya.com.br/hc/article_attachments/4407000131991)

| **E-mail do evento da tarefa "Realizar Cotação"** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#top)

#### Demais Eventos disponíveis no contexto de Processo

Os conceitos que definem um Evento são as junções de momentos e ações que indicam ou não a execução de um script escrito pelo modelador. O modelador pode definir vários Eventos, editar, excluir e incluir no contexto de Processo.

Para todo Evento adicionado, é necessário escrever o **"Nome do Evento"**. Além dele, existem de 3 a 5 campos obrigatórios e que, sequencialmente, devem ser preenchidos de acordo com a regra de negócio do Evento, são eles:

**1- Onde:**

- **Formulário Embarcado:** O momento será relacionado a qualquer campo do Formulário Formatado contido no processo e, para esse apontamento, existe a ação **"Salvar"** a ser definida; ao salvar um campo de qualquer Formulário Formatado, o Evento é disparado.
- **Formulário Formatado:** O momento será relacionado diretamente a um Formulário Formatado contido na Tarefa onde o Evento está sendo definido. Para o Formulário Formatado existem as seguintes ações:

**Excluir:** Na exclusão de um Formulário Formatado o Evento é disparado.

**Incluir:** Na inclusão de um Formulário Formatado o Evento é disparado.

**Alterar:** Na alteração de um Formulário Formatado o Evento é disparado.

**Observação:** é necessário definir o **"Quando"**, sendo **"Antes"** ou **"Depois"** da ação e por fim, selecionar qual Formulário Formatado está relacionado à essa configuração de Evento no campo **"Formulário"**.

**2- Tipo de Rotina:**

- **Java:** Para essa rotina é necessário vincular um arquivo .jar na tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java) e, posteriormente, associar o módulo java ao Evento. Assim, o modelador pode escrever scripts simples e até mais completos, como por exemplo, um que utiliza WebService, chamando um serviço externo qualquer.
- **Banco de Dados:** Também é possível criar uma rotina de banco de dados no padrão procedure do Sankhya Om. Então, dentro da rotina do banco de dados, teremos que retornar um resultado **'N'** caso a condição testada seja falsa, ou **'S'** se a condição for verdadeira.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#top)

#### Demais Eventos disponíveis no contexto de Tarefas

Os conceitos que definem um Evento são as junções de momentos e ações que indicam ou não a execução de um script escrito pelo modelador. O modelador pode definir vários Eventos, editar, excluir e incluir no contexto de Tarefa.

Para todo Evento adicionado, é necessário escrever o **"Nome do Evento"**. Além dele, existem de 3 a 5 campos obrigatórios e que, sequencialmente, devem ser preenchidos, são eles:

**1- Onde:**

- **Apontamento:** O momento será relacionado aos apontamentos na Tarefa onde o Evento está sendo definido e, para esse apontamento existem as seguintes ações a serem definidas:

**Excluir:** Na exclusão de um apontamento o Evento é disparado.

**Incluir:** Na inclusão de um apontamento o Evento é disparado.

**Pausar:** Na pausa de um apontamento o Evento é disparado.

**Iniciar:** Na inicialização de um apontamento o Evento é disparado.

**Alterar:** Na alteração de um apontamento o Evento é disparado.

**Nota:** é necessário definir também o **"Quando"**, sendo **"Antes"** ou **"Depois"** da ação.

- **Formulário Embarcado:** O momento será relacionado a qualquer campo do Formulário Embarcado contido no processo e, para esse apontamento, existe a ação **"Salvar"** a ser definida; assim, ao salvar um campo de qualquer Formulário Formatado o Evento é disparado.
- **Formulário Formatado:** O momento será relacionado diretamente a um Formulário Formatado contido na Tarefa onde o Evento está sendo definido. Para o Formulário Formatado existem as seguintes ações:

**Excluir:** Na exclusão de um Formulário Formatado o Evento é disparado.

**Incluir:** Na inclusão de um Formulário Formatado o Evento é disparado.

**Alterar:** Na alteração de um Formulário Formatado o Evento é disparado.

**Observação:** é necessário definir o **"Quando"**, sendo **"Antes"** ou **"Depois"** da ação e por fim, selecionar qual Formulário Formatado está relacionado à essa configuração de Evento no campo **"Formulário"**.

**2- Tipo de Rotina:**

- **Java:** Para essa rotina é necessário vincular um arquivo .jar na tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java) e, posteriormente, associar o módulo java ao Evento. Assim, o modelador pode escrever scripts simples e até mais completos, como por exemplo, um que utiliza WebService, chamando um serviço externo qualquer.
- **Banco de Dados:** Também é possível criar uma rotina de banco de dados no padrão procedure do Sankhya Om. Então, dentro da rotina do banco de dados, teremos que retornar um resultado **'N'** caso a condição testada seja falsa, ou **'S'** se a condição for verdadeira.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4406903288855-Eventos-de-Processo-e-Eventos-de-Tarefa#top)
