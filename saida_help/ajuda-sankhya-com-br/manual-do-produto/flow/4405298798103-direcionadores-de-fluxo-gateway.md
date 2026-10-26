---
id: "4405298798103"
titulo: "Direcionadores de fluxo (Gateway)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:49Z"
rotulos: ["Configuração", "Fluxo", "Processo", "Gateways", "sankhyaflow", "Direcionadores de fluxo (Gateway)", "Gateways determinam caminhos", "Paralelo Exclusivo Inclusivo", "Configuração e uso", "Gateway"]
---

# Direcionadores de fluxo (Gateway)

Os Gateways são elementos que determinam o caminho que o processo seguirá, definindo ramificações, bifurcações e união de caminhos, por meio dos Gateways Paralelo, Exclusivo e Inclusivo.

Nessa documentação, trataremos sobre os seguintes tópicos:

---

1. [Gateways](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gateways)
2. [Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#casosdeuso)
3. [Configurando Gateways no Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#Configurandogatewaysnoprocesso)

---

#### Gateways

Nesse tópico falaremos sobre cada um dos Gateways: [Paralelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#paralelo), [Exclusivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#exclusivo) e [Inclusivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#inclusivo).

**Paralelo**

Esse gateway representa a divisão de um fluxo em 2 ou mais caminhos que serão executados paralelamente, ou seja, todos os caminhos de saída são executados simultaneamente.

Ele é utilizado também como junção; nesse caso, o fluxo de execução será percorrido apenas quando todos os seus fluxos de entrada forem percorridos.

![Imagem 1: Ele é utilizado também como junção ; nesse caso, o fluxo de execução será percorrido apenas quando todos os seus fluxos…](https://ajuda.sankhya.com.br/hc/article_attachments/4405304270615)

| **Ícone Gateway Paralelo** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gateways) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

---

**Exclusivo**

O gateway exclusivo é utilizado em um processo onde vários caminhos são possíveis porém, de acordo com as condições, apenas um deles será percorrido. Assim, deverá existir sempre 2 ou mais fluxos de saídas, sendo que um desses fluxos pode ser um caminho padrão, que será executado apenas se todos os outros fluxos não forem verdadeiros no tempo de execução. Ele é representado por um fluxo sequencial com uma barra diagonal:

![Imagem 2: O gateway exclusivo é utilizado em um processo onde vários caminhos são possíveis porém, de acordo com as condições,…](https://ajuda.sankhya.com.br/hc/article_attachments/4405299425943)

| **Fluxo de sequência padrão** |
| --- |

Ou seja, a primeira condição (script) que for avaliada como verdadeira (true) irá determinar o fluxo a ser seguido, e se por acaso todas as condições dos fluxos retornarem falso (false), o fluxo padrão terá sequência.

Esse gateway também pode unificar fluxos distintos em uma única sequência de atividades, sendo que a primeira sequência que chegar dará continuidade no fluxo do processo.

![Imagem 3: Esse gateway também pode unificar fluxos distintos em uma única sequência de atividades, sendo que a primeira sequência…](https://ajuda.sankhya.com.br/hc/article_attachments/4405299484183)

| **Ícone Gateway Exclusivo** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gateways) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

---

**Inclusivo**

Esse gateway será utilizado em pontos do processo onde vários caminhos de continuidade são possíveis, desde que sua condição seja verdadeira. Sendo assim, sempre deverá ter 2 ou mais fluxos de saídas.

A execução do processo pode ser dividida em inúmeros fluxos paralelos e todos os fluxos que retornarem com a condição (script) verdadeira serão executados. Também pode ser definido um caminho padrão que será percorrido caso nenhuma das condições forem verdadeiras.

O gateway inclusivo permite também unificar o fluxo de execução, ou seja, a continuidade do processo acontecerá apenas quando todos os fluxos de saída de um gateway inclusivo tiver sido percorrido.

![Imagem 4: O gateway inclusivo permite também unificar o fluxo de execução, ou seja, a continuidade do processo acontecerá apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/4405299585175)

| **Ícone Gateway Inclusivo** |
| --- |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gateways) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

#### Casos de Uso

Nesse tópico, trouxemos um caso de uso para cada tipo de Gateway. Para verificar sobre, clique nos link's abaixo:

[Gateway Paralelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gatewayparalelo)                              [Gateway Exclusivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gatewayexclusivo)                              [Gateway Inclusivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#gatewayinclusivo)

---

**Gateway Paralelo**

![Imagem 5: Gateway Paralelo](https://ajuda.sankhya.com.br/hc/article_attachments/4405304951063)

| **Processo utilizando Gateway Paralelo** |
| --- |

Nesse exemplo, serão executados paralelamente 2 fluxos (representado pelo primeiro gateway). Enquanto a **"Tarefa 2"** é realizada, a **"Tarefa 3"** também poderá ser executada. O segundo gateway faz a junção dos fluxos, garantindo que a **"Tarefa 4"** só seja realizada depois que as Tarefas 2 e 3 tiverem sido finalizadas.

**Observação:** os gateways são utilizados de maneira independente, ou seja, não precisa utilizar um gateway de junção ou os dois juntos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#casosdeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

---

**Gateway Exclusivo**

O processo abaixo permite que um colaborador realize uma solicitação de Adiantamento de viagens para seu líder:

![Imagem 6: O processo abaixo permite que um colaborador realize uma solicitação de Adiantamento de viagens para seu líder:](https://ajuda.sankhya.com.br/hc/article_attachments/4405305033239)

| **Processo utilizando Gateway Exclusivo** |
| --- |

No exemplo acima, o primeiro gateway verifica o resultado da tarefa **"Aprovar adiantamento de viagem"**; se na execução dessa tarefa o líder aprovar o adiantamento, o fluxo seguirá pela sequência de saída padrão **"Registrar títulos de adiantamento"** e se o adiantamento for reprovado, o fluxo seguirá pelo caminho **"Notificar o solicitante"**.

**(2)** Uma boa prática no SankhyaFlow é utilizar o Gateway Exclusivo também quando uma determinada tarefa tiver várias entradas, pois na tarefa é possível ter apenas um evento de entrada.

Nesse mesmo exemplo, utilizamos o Gateway Exclusivo para dar sequência nos 2 fluxos criados, onde ambos serão direcionados para a mesma tarefa Notificar solicitante, conforme a execução do fluxo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#casosdeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

---

**Gateway Inclusivo**

No caso abaixo, o primeiro gateway verifica o resultado da atividade **"Avaliar documentação"**; se na execução dessa atividade for identificada a necessidade de ter que digitalizar a documentação e/ou validar a autenticidade desses documentos, cada fluxo será executado. Caso esteja tudo certo com a documentação, o fluxo seguirá o caminho padrão.

![Imagem 7: No caso abaixo, o primeiro gateway verifica o resultado da atividade "Avaliar documentação" ; se na execução dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/4405305272343)

| **Processo utilizando Gateway Inclusivo** |
| --- |

Aqui, o Gateway Inclusivo foi utilizado para unir os fluxos criados. Isso garante que a atividade **"Notificar partes envolvidas"** só seja iniciada depois que todos os fluxos que forem iniciados pelo gateway anterior sejam executados.

**(2)** Os gateways são utilizados de maneira independente, ou seja, não precisa utilizar um gateway de junção ou então os dois juntos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#casosdeuso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)

#### Configurando Gateways no Processo

Ao selecionar uma tarefa do processo na tela Processos de Negócio, será exibida uma caixa com várias opções. Dentre elas, selecione o ícone **"Adicionar Gateway"** ou busque esse elemento dentro da paleta localizada ao lado esquerdo:

[GIF animado: Imagem 8: Ao selecionar uma tarefa do processo na tela Processos de Negócio, será exibida uma caixa com várias opções. Dentre…](https://ajuda.sankhya.com.br/hc/article_attachments/4405312002711)

| **Adicionando Gateways** |
| --- |

Por padrão, é apresentado o Gateway Exclusivo; para alterar o tipo, basta clicar no ícone **"Alterar tipo"** e selecionar o que você desejar:

[GIF animado: Imagem 9: Por padrão, é apresentado o Gateway Exclusivo ; para alterar o tipo, basta clicar no ícone "Alterar tipo" e selecionar…](https://ajuda.sankhya.com.br/hc/article_attachments/4405306343959)

| **Alteração do tipo de Gateways** |
| --- |

Para configurar um Gateway Paralelo, basta inseri-lo no processo e dar sequência na modelagem de cada caminho que deverá ser percorrido. Para configurar esse elemento como junção, o gateway deve receber as entradas dos caminhos do Gateway Paralelo anterior:

![Imagem 10: Para configurar um Gateway Paralelo , basta inseri-lo no processo e dar sequência na modelagem de cada caminho que…](https://ajuda.sankhya.com.br/hc/article_attachments/4405312065175)

| **Modelagem do Processo com Gateway Paralelo** |
| --- |

Na configuração do Gateway Exclusivo, é necessário inserir uma condição no fluxo sequencial para que o caminho seja executado conforme os dados inseridos na tarefa anterior. Quando o caminho for definido como fluxo padrão, não é necessário inserir um script.

Você pode realizar a configuração de um gateway exclusivo, de duas formas: Modo assistente e Modo avançado.

---

**Modo assistente**

Essa opção é viável para auxiliar o usuário que está realizando a modelagem do processo e não possui conhecimento em criação de script (Groovy ou JavaScript).

Para definir uma condição, utilizando o Modo Assistente, no caminho que não é padrão, é necessário clicar sobre o fluxo sequencial, onde será apresentado na aba Geral o botão **"Abrir configurador de condições"**. 

![Imagem 11: Para definir uma condição, utilizando o Modo Assistente , no caminho que não é padrão, é necessário clicar sobre o…](https://ajuda.sankhya.com.br/hc/article_attachments/5567336333207)

| **Configurador de condições** |
| --- |

Ao abrir o configurador de condições, o usuário deverá selecionar no **"Modo de construção"** a opção **"Assistente"**.

![Imagem 12: Ao abrir o configurador de condições, o usuário deverá selecionar no " Modo de construção" a opção "Assistente" .](https://ajuda.sankhya.com.br/hc/article_attachments/5575163794967)

| **Modo de construção - Assistente** |
| --- |

Nesse exemplo, iremos realizar uma configuração utilizando o Modo assistente para buscar os dados de um campo do formulário formatado, na situação em que a solicitação do adiantamento seja reprovada. Para que este cenário ocorra é necessário seguir os passos abaixo:

**(2)** O exemplo abaixo é referente ao processo de Adiantamento de viagens, no gateway Aprovação de adiantamento. Para realizar um teste, procure na base utilizada um processo correspondente.

**Campo**: SITUACAO

**Formulário**: AD\_SOLICITACAOADIANTAMENTO

Com o campo Modo de construção indicado com a opção Assistente, clique em **"Formulários"**, opção **"Formatado"** e selecione o formulário formatado **"AD\_SOLICITACAOADIANTAMENTO"**. Feito isso, selecione a opção **"SITUACAO"**, em seguida escolha o operador lógico **"Igual(=)"** e indique a opção **"Reprovado"** . Para finalizar clique em **"OK"**.

[GIF animado: Imagem 13: Com o campo Modo de construção indicado com a opção Assistente , clique em "Formulário s" , opção " Formatado" e…](https://ajuda.sankhya.com.br/hc/article_attachments/5576907772055)

| **Configurando uma condição no modo assistente** |
| --- |

---

**Modo avançado**

Essa opção é viável para o usuário que está realizando a modelagem do processo e possui conhecimento em criação de script (Groovy ou JavaScript).

Para definir uma condição script - Modo Avançado no caminho que não é padrão, é necessário clicar sobre o fluxo sequencial, onde será apresentado na aba Geral o botão **"Abrir configurador de condições"**.

![Imagem 14: Para definir uma condição script - Modo Avançado no caminho que não é padrão, é necessário clicar sobre o fluxo…](https://ajuda.sankhya.com.br/hc/article_attachments/5567336333207)

| **Configurador de condições** |
| --- |

Ao abrir o configurador de condições, o usuário deverá selecionar no **"Modo de construção"** a opção **"Avançado"**.

![Imagem 15: Ao abrir o configurador de condições, o usuário deverá selecionar no "Modo de construção" a opção "Avançado" .](https://ajuda.sankhya.com.br/hc/article_attachments/5569988416023)

| **Modo de construção - Avançado** |
| --- |

Neste exemplo, iremos configurar um script para buscar os dados de um campo do formulário formatado, para o caso onde a solicitação de adiantamento for reprovada. Então para que este cenário ocorra é necessário definir o script abaixo:

**(2)** O exemplo abaixo é referente ao processo de Adiantamento de viagens, no gateway Aprovação de adiantamento. Para realizar um teste, utilizando esse script, procure na base utilizada um processo correspondente.

**Campo**: SITUACAO

**Formulário**: AD\_SOLICITACAOADIANTAMENTO

| ``` //Obter dados do formulário var formulario = getLinhasFormulario("AD_SOLICITACAOADIANTAMENTO"); //Se o campo SITUACAO for igual a RP (REPROVADO) a condição será verdadeira if(formulario[0].getCampo("SITUACAO") == 'RP'){     return true; }else{     return false; } ``` |
| --- |

No script deve ser informada sempre a chave que resulta na opção de um determinado campo; por exemplo a lista de opções para o campo SITUACAO são:

**RP=REPROVADO**
**AP=APROVADO**

Ou seja, a chave corresponde à **"RP"** e **"AP"**.

Para buscar os dados de um campo do formulário formatado para um único registro, utilizamos a função **getLinhasFormulario**, conforme demonstrado no exemplo acima. Quando usado o formulário nativo, utilizamos a função **getLinhasFormularioNativo**, e para buscar um campo de um formulário embarcado, é utilizada a função **getCampo**, de acordo com o exemplo abaixo:

**Linguagem Groovy:** getCampo("DOCUMENTACAO") == "S"

**Linguagem JavaScript:** return getCampo("DOCUMENTACAO") == "S"

![Imagem 16: É possível utilizar apenas as funções de consulta para os scripts de gateways. Elas estão disponíveis no botão "Ajuda"…](https://ajuda.sankhya.com.br/hc/article_attachments/16092447987991) É possível utilizar apenas as funções de consulta para os scripts de gateways. Elas estão disponíveis no botão **"Ajuda"** do script.

---

Por fim, a configuração do Gateway Inclusivo segue conforme apresentado no exemplo anterior do Gateway Exclusivo, ou seja, é necessário inserir uma condição para que o caminho seja executado conforme os dados inseridos na tarefa anterior. Quando o caminho for definido como fluxo padrão, não é necessário inserir uma condição.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298798103-Direcionadores-de-fluxo-Gateway#top)
