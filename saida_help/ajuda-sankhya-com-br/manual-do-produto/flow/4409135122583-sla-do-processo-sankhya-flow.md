---
id: "4409135122583"
titulo: "SLA do Processo - Sankhya Flow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:10:39Z"
rotulos: ["Configuração", "Contrato", "Processo", "SLA", "Sankhyaflow", "SLA do Processo", "Define prazos e alertas para o cumprimento de tarefas", "\"Solicitação de Compras\" com SLAs diferenciados por tipo de produto", "Adicione e ajuste SLAs definindo prazos em dias ou horas", "Sankhya Flow"]
---

# SLA do Processo - Sankhya Flow

Um contrato estabelecido entre duas partes pode envolver uma série de itens, acordos e também prazos de atendimento. Com os prazos estabelecidos no processo, temos então a necessidade de acompanhar em dias ou horas se os prazos estão sendo cumpridos.

Para esse acompanhamento, baseado nas regras estabelecidas em contrato, existe o recurso do SLA (Acordo de Nível de Serviço) do processo.

O SLA do Processo possibilita estabelecer regras para contagem do prazo. Em uma determinada ação no processo iniciará uma contagem de tempo, como também será possível estabelecer regras para a suspensão da contagem. Assim, uma vez tendo regras acordadas entre fornecedor e cliente, o SLA do Processo fará esse acompanhamento.

Além das regras de contagem e suspensão de prazo, será possível criar alertas de notificações e e-mails em função dos prazos decorridos portanto, se determinado prazo for atingido, os usuários do sistema podem ser alertados.

Nessa documentação trataremos sobre os seguintes temas:

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#casodeuso),
2. [Configurações do SLA do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#configura%C3%A7%C3%B5esdosladoprocesso),
3. [Demais informações do SLA do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#demaisinforma%C3%A7%C3%B5esdosladoprocesso),
4. [Inicialização/Continuação e Suspensão - Configurações de Script e Rotina de Banco de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#inicializa%C3%A7%C3%A3o/continua%C3%A7%C3%A3oesuspens%C3%A3o-configura%C3%A7%C3%B5esdescripterotinadebancodedados), e
5. seus [Status](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#status).

---

#### Caso de Uso

O processo **"Solicitação de compras"**, exibido na imagem abaixo, foi modelado a fim de atender a proposta de simplificar uma solicitação de compra, tanto para o usuário quanto para automatização do lançamento da solicitação.

![Imagem 1: O processo "Solicitação de compras" , exibido na imagem abaixo, foi modelado a fim de atender a proposta de simplificar…](https://ajuda.sankhya.com.br/hc/article_attachments/4409140270359)

| **Solicitação de Compras** |
| --- |

O processo possui 3 Tarefas de Usuário: **"Analisar solicitação de compra"**, **"Realizar cotação"** ou **"Refazer Solicitação"**, possui também 2 Tarefas de Serviço para Atualizar e Gerar o pedido e por fim, 2 Tarefas de E-mail para notificação nos cenários de reprovação ou status do pedido.

A partir do momento em que a solicitação é lançada, ou seja, um processo é aberto, o SLA começa a contar. A primeira Tarefa de Usuário é a de Analisar solicitação de compra; nela o gestor responsável analisa a solicitação feita e decide se ela é válida para prosseguir ou se é inválida para ser diretamente cancelada ou refeita na atividade de Refazer Solicitação, na qual o solicitante edita e refaz a solicitação de compra.

**Observação:** quando o processo é direcionado para essa atividade, o SLA é suspenso e somente volta a ser contado quando retorna a atividade de Analisar solicitação de compra.

A Souza Empreendimentos executa uma série de solicitações de compras dos mais variados produtos e para alguns produtos existem fornecedores acordados com prazos de atendimento estabelecidos. Hoje, existem 2 SLA's configurados, sendo um para grupo de produtos de consumo alimentício e o outro produtos de consumo de escritório.

Os itens do grupo alimentício são comprados em eventos para o coffee break e como são perecíveis, o prazo de SLA é mais curto.

Já itens do grupo de escritório são itens de consumo do dia a dia da Empresa, como canetas, borrachas, cadernos, etc. Como são itens comprados em volumes maiores e não possuem data de validade, têm um SLA mais longo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#top)

#### Configurações do SLA do Processo

Podemos adicionar vários SLA's no mesmo processo (conforme demonstramos abaixo), sendo que, cada um deve seguir regras e alertas diferentes. Para acessar o painel lateral de configurações do processo, basta dar um duplo clique fora do mapeamento do processo e clicar na aba **"SLA"**. Nessa aba podemos adicionar um novo SLA e configurá-lo, editá-lo e também excluí-lo do processo:

[GIF animado: Imagem 2: Podemos adicionar vários SLA's no mesmo processo (conforme demonstramos abaixo), sendo que, cada um deve seguir regras…](https://ajuda.sankhya.com.br/hc/article_attachments/4409190621847)

| **Acessando a configuração do SLA** |
| --- |

Para todo SLA adicionado no processo, será necessário dar um **"Nome"** a ele, informar se seu **"Prazo de solução"** será em **"Dias"** ou **"Horas"** e informar a quantidade de **"Dias ou Horas"**. Também podemos informar qual **"Carga horária"** poderá ser levada em consideração na contagem desse SLA:

![Imagem 3: Para todo SLA adicionado no processo, será necessário dar um "Nome" a ele, informar se seu "Prazo de solução" será em…](https://ajuda.sankhya.com.br/hc/article_attachments/4409190682647)

| **Configurando SLA detalhes** |
| --- |

Se o solicitante lançar um produto que esteja no grupo de produtos alimentícios, isso indica que será vigente um SLA de 3 dias para o processo. O modelador do processo deve selecionar o **"Contexto de Processo"**, conforme demonstramos no gif acima, e na configuração do contexto, selecionar a opção por campo de formulário. Nesse caso de uso existem 2 formulários; no caso, o modelador pode selecionar o formulário que contém o campo relacionado ao grupo de produto.

Assim, quando o processo for iniciado com um produto selecionado do grupo alimentício, a contagem de um SLA de 3 dias para o processo passará a contar.

[GIF animado: Imagem 4: Assim, quando o processo for iniciado com um produto selecionado do grupo alimentício, a contagem de um SLA de 3 dias…](https://ajuda.sankhya.com.br/hc/article_attachments/4409195741975)

| **Configurando SLA Contexto de Processo** |
| --- |

Na Tarefa de Usuário Analisar solicitação de compra, o gestor poderá devolver a demanda para o solicitante refazer o pedido, devolvendo os pedidos que forem lançados com algum erro, por exemplo. Então, para esse cenário, o SLA é suspenso já que a solicitação será refeita.

A configuração da Suspensão é semelhante à configuração da Inicialização/Continuação. O modelador acessa a configuração Contexto de Tarefa (conforme abaixo) e seleciona a tarefa onde será analisada a solicitação, e o **"Quando"** será na finalização da tarefa.

[GIF animado: Imagem 5: A configuração da Suspensão é semelhante à configuração da Inicialização/Continuação . O modelador acessa a…](https://ajuda.sankhya.com.br/hc/article_attachments/4409190864663)

| **Configurando Suspensão SLA Contexto de Tarefa** |
| --- |

**Nota:** a informação de suspensão está contida em um campo de formulário; dessa forma, o modelador terá que fazer essa relação. Assim, quando a atividade Analisar solicitação de compra for finalizada e o campo **"Refazer Solicitação"** for igual a **"Sim"**, será suspensa a contagem do SLA.

---

**Alertas no SLA do Processo**

Para o acompanhamento do SLA, existe a configuração dos **"Alertas"**; nesse caso, os alertas **"No Prazo"** e **"A Vencer"**.

Configurando o status No Prazo, o tipo de **"Contagem"** será mantido em **"Dias"**, a marcação **"Status"** será habilitada pois assim será possível acompanhar a contagem do SLA no card do processo na Lista de Tarefas. Para cada alerta existe um tempo **"Decorrido"** padrão e, nesse caso, manteremos o valor padrão para o alerta No Prazo que é de 50 (relacionado à dias).

Quanto às notificações, elas serão do **"Tipo"** de **"Notificações do Sistema"**, não sendo necessário relacionar uma **"Conta SMTP"**. O **"Destinatário"** deve ter a marcação **"Notificar o dono/candidatos da tarefas"** selecionada, sendo possível também colocar mais destinatários de **"Scripts SQL"**.

Para o status A Vencer, o tipo de Contagem será mantido em Dias e a marcação Status também será mantida ligada para que seja possível acompanhar a contagem do SLA no card da tarefa. No caso do tempo Decorrido, manteremos o valor padrão para o alerta A Vencer que é de 75 (relacionado à dias).

As notificações serão do Tipo **"Ambas"**, sendo necessário relacionar uma Conta SMTP. A marcação Notificar o dono/candidatos de tarefa também deverá ser habilitada e você poderá inserir mais destinatários através de Scripts SQL.

---

**Cards na Lista de Tarefas**

Quando configurados os Alertas, na Lista de Tarefas será apresentado um novo campo, trazendo o **"Prazo do SLA"** no card e também no cabeçalho do formulário da tarefa. As cores que constam na configuração dos Alertas também serão representadas no card.

A imagem abaixo representa um card com o SLA **"Muito Vencido"**:

![Imagem 6: A imagem abaixo representa um card com o SLA "Muito Vencido" :](https://ajuda.sankhya.com.br/hc/article_attachments/4409195902871)

| **Lista de Tarefas** |
| --- |

Outra funcionalidade com o SLA no card é utilizar ele como critério na ordenação na Lista de Tarefas de acordo com o seu **"Vencimento"**, que poderá ser **"Mais próximos primeiro"** ou **"Mais distantes primeiro"**:

[GIF animado: Imagem 7: Outra funcionalidade com o SLA no card é utilizar ele como critério na ordenação na Lista de Tarefas de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/4409196090263)

| **Configurando ordenação dos cards** |
| --- |

---

**Notificações dos Alertas**

Podemos configurar o Alerta de SLA para enviar tanto uma notificação quanto um e-mail para o dono da atividade. As notificações aparecem no ícone de notificação geral do sistema conforme imagem abaixo:

![Imagem 8: Podemos configurar o Alerta de SLA para enviar tanto uma notificação quanto um e-mail para o dono da atividade. As…](https://ajuda.sankhya.com.br/hc/article_attachments/4409196195095)

| **Notificação no sistema** |
| --- |

E também no texto do e-mail:

![Imagem 9: E também no texto do e-mail:](https://ajuda.sankhya.com.br/hc/article_attachments/4409191633047)

| **Notificação por e-mail** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#top)

#### Demais informações do SLA do Processo

**Inicialização / Continuação - Alteração de Formulário**

Nessa configuração, você pode estabelecer que uma alteração em um campo qualquer de um formulário qualquer que esteja no processo (independente do ponto em que ele esteja), seja iniciada ou continuada uma contagem do SLA.

---

**Inicialização / Continuação - Contexto de Tarefa**

Aqui você pode estabelecer que uma Tarefa de Usuário inicie ou continue a contagem do SLA. Os momentos disponíveis para esse contexto são: **"Ao atribuir dono"**, **"Ao desatribuir dono"**, **"Ao criar tarefa"** e **"Ao finalizar tarefa"**.

---

**Suspensão - Alteração de Formulário**

Por fim, nessa configuração você estabelece que uma alteração em um campo qualquer de um formulário que esteja no processo (independente do ponto em que ele esteja) possa ser suspensa uma contagem do SLA que está sendo executada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#top)

#### Inicialização/Continuação e Suspensão - Configurações de Script e Rotina de Banco de Dados

No [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#casodeuso) vimos a configuração do SLA do Processo através de campos do formulário, mas existem outras 2 possibilidades de configuração para Inicialização/Continuação do SLA do Processo e Suspensão.

Também é possível combinar scripts, rotinas de banco e campos de formulários com os operadores lógicos **"E"** e/ou **"OU"**, para que essa combinação retorne ao final um valor verdadeiro para iniciar/continuar o SLA do Processo ou realizar sua suspensão.

Através de scripts na linguagem JavaScript ou Groovy estabelecemos regras para a Inicialização/Continuação ou Suspensão; o script deverá retornar verdadeiro ou falso. As funções disponíveis para uso podem ser consultadas no help.

No gif abaixo temos a demonstração de utilização de script na configuração de um SLA do Contexto de Processo:

[GIF animado: Imagem 10: No gif abaixo temos a demonstração de utilização de script na configuração de um SLA do Contexto de Processo :](https://ajuda.sankhya.com.br/hc/article_attachments/4409190577303)

| **Configurando SLA do Contexto de Processo por Script** |
| --- |

| ``` var grupo = getLinhasFormulario("AD_SOLICITACAOCOMPRA"); if (grupo.length > 0){ var Codgrupo = grupo[0].getCampo("CODGRUPOPROD"); if (Codgrupo == 1000000) { return true; } }  return false; ``` |
| --- |

**Observação:** também é possível criar uma rotina de banco de dados no padrão procedure do Sankhya Om. Então, dentro da rotina do banco de dados, você deve retornar um resultado **"N"**, caso a condição testada seja falsa ou **"S"** se a condição for verdadeira.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#top)

#### Status

Para todo SLA do Processo é possível estabelecer Alertas diferentes, em diferentes níveis te tempo. Eles estão segmentados da seguinte forma:

- **Início do Prazo:** Tempo decorrido 0, cor **azul**;
- **No Prazo:** Tempo decorrido 50, cor **verde**;
- **A Vencer:** Tempo decorrido 75, cor **amarela**;
- **Vencido:** Tempo decorrido 100, cor **vermelha**;
- **Muito Vencido:** Tempo decorrido 110, cor **preta**.

O tempo Decorrido pode ser ajustado para outros valores caso o modelador queira. Os Alertas possuem os seguintes campos:

No campo **"Contagem"** é informado se a contagem será em **"Percentual"**, **"Dias"** ou **"Horas"**.

Se a marcação **"Status"** estiver ligada, as informações de tempo consumido do SLA estarão no card do processo na Lista de Tarefas e no cabeçalho do formulário.

O campo **"Tipo"** refere-se aos tipos de notificações que o sistema irá emitir, sendo eles: **"E-mail"**, **"Notificações do Sistema"**, **"Ambas"** ou **"Nenhuma"**.

Caso seja selecionado o Tipo de Notificação de E-mail ou Ambas, será necessário informar a **"Conta SMTP"** para o disparo do e-mail.

Se a marcação **"Notificar o dono/candidato da tarefa"** estiver selecionada, fará com que os usuários candidatos/dono da tarefa sejam notificados.

Por fim, será possível escrever uma consulta no campo **"Script SQL"** que retorne o e-mail do usuário para ele receber a notificação de alerta do SLA.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4409135122583-SLA-do-Processo-Sankhya-Flow#top)
