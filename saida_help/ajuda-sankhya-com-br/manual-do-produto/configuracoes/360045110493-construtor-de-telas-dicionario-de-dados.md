---
id: "360045110493"
titulo: "Construtor de Telas/Dicionário de Dados - Aba Ações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-11T18:05:15Z"
rotulos: ["Configuração", "Rotina Java", "Dicionário de Dados", "Lançador", "Construtor de Telas/Dicionário de Dados - Aba Ações manual", "Construtor de Telas", "Ações Personalizadas no Construtor de Telas e Dicionário de Dados", "Script (JavaScript)"]
---

# Construtor de Telas/Dicionário de Dados - Aba Ações

A configuração desta aba, permite que no Sankhya-Om sejam executadas tarefas específicas de forma rápida e simples. Esta aba está presente nas configurações das telas [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas) e [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados).

Assim, inicialmente informe uma **"Descrição"** adequada a ação que está sendo cadastrada.

Pelo campo **"Tipo"**, será possível definir a execução de uma **"Rotina** **no Banco de Dados"**, a execução de uma **"Rotina Java"**, a execução de um **"Script (JavaScript)"** e a configuração de um **"Lançador"** para uma tela do sistema. Cada uma destas opções quando escolhida, disponibiliza configurações diferentes a serem efetuadas.

Detalhes sobre a configuração das ações personalizadas desta tela, também podem ser visualizados acessando o link [Não sabe o que é isso? Comece lendo esse Tutorial](http://code.sankhya.com.br/configurando-acoes-personalizadas-para-telas/) localizado na parte superior da aba Ações.

Trataremos a seguir, sobre o comportamento de cada uma destas opções apresentadas no campo Tipo:

| [Rotina no Banco de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#rotinanobancodedados) | [Script (JavaScript)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#scriptjavascript) |
| --- | --- |
| [Lançador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#lanador) | [Rotina Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#rotinajava) |

![Imagem 1: Rotina Java](https://ajuda.sankhya.com.br/hc/article_attachments/1500009239262)

### Rotina no Banco de Dados

A base deste tipo de ação é uma **"Stored Procedure"** que será contextualizada e executada pelo sistema. Como existem vários recursos de programação e diferenças significativas entre os Bancos de Dados (Oracle e SqlServer) suportados pelo Sankhya-OM, a melhor maneira de criar a stored procedure (adotemos o nome de **"proc"** para simplificar), é fazê-lo diretamente no banco. Assim, a interface de configuração das ações deste tipo, efetua a coleta das informações necessárias para criação o "corpo" da "proc".

![Imagem 2: A base deste tipo de ação é uma "Stored Procedure" que será contextualizada e executada pelo sistema. Como existem…](https://ajuda.sankhya.com.br/hc/article_attachments/1500009507861)

Inicialmente, localize na tela a tabela a ser utilizada para inclusão da ação; tomemos como exemplo a tabela **"AD\_TAREFA"**.

O passo seguinte é o preenchimento de uma **"Descrição"** e a escolha do tipo **"Rotina no Banco de Dados"**.

O campo **"Nome da rotina"** está destinado ao preenchimento do nome da "proc" propriamente dita. Em seguida, escolha uma das opções disponíveis no campo **"Depois de executar, recarregar"**, sendo elas:

- **Não recarrega nada:** Através desta definição, nenhum registro será recarregado.
- **Toda a grade:** Por esta opção, serão recarregados todos os registros da grade principal da tela, independente dos itens selecionados.
- **Os registros selecionados:** Serão recarregados apenas os registros selecionados para a ação.
- **O registro pai (Quando existir):**  No caso em que a ação é registrada para uma tela Detalhe, recarrega-se o registro da tela Mestre. Se selecionado para uma tela não Detalhe, recarrega-se toda a grade.
- **O registro principal (Quando existir):** A diferença para a opção anterior é sutil, mas entendamos que uma tela Mestre, pode ser Detalhe de outra. Por exemplo, quando executa-se uma ação para a tela "Participantes", o registro pai seria a "Etapa" e o registro principal a "Tarefa", pois Participante é Detalhe de Etapa, que por sua vez, é Detalhe de Tarefa.

A marcação **"Controle de transação manual"** por padrão, é apresentada desmarcada; caso esteja assinalada, o controle de transação com o banco de dados deve ser feito no seu respectivo script, de acordo com a necessidade. Caso esteja desmarcada, o sistema automaticamente controla a transação e realiza o commit no final da execução do script e faz o rollback caso existam erros na execução do script.

Ao salvar a ação criada, clique no botão ![Imagem 3: Ao salvar a ação criada, clique no botão para que um template da rotina (proc) seja criado. Quando a proc está…](https://ajuda.sankhya.com.br/hc/article_attachments/1500009249442) para que um template da rotina (proc) seja criado. Quando a proc está compilada no Banco de Dados, o campo "Nome da rotina" ficará desabilitado a fim de se evitar modificações indevidas.

O template criado revela como deve ser o "esqueleto" da proc, ou seja, quais são os parâmetros de entrada e saída que ela deve possuir.

Na seção **"Parâmetros"**, configure os fatores a serem utilizados na ação; informe a **"Descrição"**, bem como o **"Nome"** do parâmetro.

No campo **"Tipo de parâmetro"**, você deve defirnir a categoria do parâmetro dentre as seguintes opções:

- Texto;
- Número inteiro;
- Número decimal;
- Data;
- Data e hora;
- Verdadeiro/Falso;
- Pesquisa;
- Opções.

A marcação **"Obrigatório"** quando realizada determina que o parâmetro em questão será indispensável.

Com a marcação **"Sugerir último valor"** realizada, o último valor passado no parâmetro será sugerido quando este for novamente solicitado.

**Observação:** trabalhando-se na tela [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas), para exibir a descrição do campo ao utilizar a consulta por meio do botão **"Visualizar formulário"** é necessário primeiramente acessar o Botão Outras Opções, opção Avançado, e definir adequadamente o Campo para apresentação, campo este caracterizado como tipo texto. Esta medida é necessária para tabelas criadas pelo usuário; para tabelas do sistema não é necessário efetuar tal procedimento.

A pequena grade localizada na parte lateral direita da tela, apresenta todos os parâmetros que foram configurados para esta ação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#top)

### Script (JavaScript)

Uma opção dentre as ações de Banco de dados, são as ações do tipo Script, que através da linguagem JavaScript abrem um novo arsenal de programação, além de suportar as mesmas funcionalidades básicas apresentadas na Rotina no Banco de Dados. Apesar da semelhança do nome, JavaScript não possui relação com Java.

JavaScript é uma linguagem poderosa e bastante difundida em aplicações Web, sendo fácil obter exemplos e tutoriais de como utilizá-la. Se você já conhece JavaScript com certeza vai preferir escrever suas ações dessa forma. Se ainda não conhece, vale a pena estudá-la pois com pouquíssimo esforço já estará apto a fazer tudo o que precisa, de forma mais simples do que em StoredProcedure, ou mesmo em Java.

![Imagem 4: JavaScript é uma linguagem poderosa e bastante difundida em aplicações Web, sendo fácil obter exemplos e tutoriais de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500009255062)

Inicialmente, localize na tela a tabela a ser utilizada para inclusão da ação; tomemos como exemplo a tabela **"AD\_TADCKM"**.

O passo seguinte é o preenchimento de uma **"Descrição"** e a escolha do tipo **"Script (JavaScript)"**.

Em seguida, escolha uma das opções disponíveis no campo **"Depois de executar, recarregar"**, sendo elas:

- **Não recarrega nada:** Através desta definição, nenhum registro será recarregado.
- **Toda a grade:** Por esta opção, serão recarregados todos os registros da grade principal da tela, independente dos itens selecionados.
- **Os registros selecionados:** Serão recarregados apenas os registros selecionados para a ação.
- **O registro pai (Quando existir):** No caso em que a ação é registrada para uma tela Detalhe, recarrega-se o registro da tela Mestre. Se selecionado para uma tela não Detalhe, recarrega-se toda a grade.
- **O registro principal (Quando existir):** A diferença para a opção anterior é sutil, mas entendamos que uma tela Mestre, pode ser Detalhe de outra. Por exemplo, quando executa-se uma ação para a tela "Participantes", o registro pai seria a "Etapa" e o registro principal a "Tarefa", pois Participante é Detalhe de Etapa, que por sua vez, é Detalhe de Tarefa.

A marcação **"Controle de transação manual"** por padrão, é apresentada desmarcada; caso esteja assinalada, o controle de transação com o banco de dados deve ser feito no seu respectivo script, de acordo com a necessidade. Caso esteja desmarcada, o sistema automaticamente controla a transação e realiza o commit no final da execução do script e faz o rollback caso existam erros na execução do script.

**Sub-aba Script**

Você pode realizar nesta sub-aba, a configuração do script a ser utilizado pela tela que está sendo construída. Além da sintaxe básica da linguagem JavaScript, pode-se fazer uso de alguns recursos especiais, são eles:

- **Função novaLinha: novaLinha([nomeDaTabela])** – Função utilizada para inserir um registro novo. Se for informado o nome da tabela, o registro será criado nessa tabela. Caso contrário será criado na tabela à qual pertence a ação. Essa função, retorna um objeto do tipo Registro, que será detalhado adiante.
- **Função getParam: getParam(nomeDoParametro)** – Função responsável por retornar o valor dos parâmetros informados pelo usuário. Seu único argumento é o nome do parâmetro.
- **Função confirmar: confirmar(titulo, texto, indice)** – Esta função mostra um diálogo ao usuário, dando a opção de prosseguir com a ação ou cancelar. É muito útil em situações onde o resultado da ação pode trazer consequências imprevistas ao usuário.
- **Função confirmarSimNao: confirmarSimNao(título, texto, índice)** – Aqui o funcionamento é semelhante a função confirmar, porém nesta, além de cancelar a execução, o usuário pode optar por **"Sim"** ou **"Não"**. Ela pode retornar true ou false.
- **Função email: email (título, mensagem, destinatários)** – Adiciona uma mensagem a ser enviada por e-mail. A lista de destinatários deve ser separada por vírgula.
- **Função mostraErro: mostraErro(mensagem)** – Interrompe a execução da ação, mostrando uma mensagem de erro.
- **Função getQuery: getQuery()** – Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados. O objeto retornado é um QueryExecutor.
- **Função newJava: newJava(classname)** – Para quem está familiarizado com programação em Java, é possível criar instâncias de objetos java para suprir uma eventual demanda não atendida pela estrutura JavaScript.
- **Função javaClass: javaClass(classname)** – Esta é semelhante a função anterior, porém, o retorno é uma Classe java e não uma instância desta classe. Serve para utilizar métodos e atributos estáticos das classes Java.

Trataremos agora, sobre algumas variáveis de ambiente:

- **linhas (tipo Array):** Esse array representa as linhas selecionadas na grade. Os itens desse array são objetos do tipo Registro.
- **linhaPai (tipo Registro):** Linha pai é um objeto do tipo Registro que representa a linha da tela master, quando a ação estiver vinculada a uma tela detalhe.
- **mensagem (tipo String):** Se algum valor for atribuído a essa variável, será apresentado ao usuário como uma informação (somente ao final da execução).

Tem-se também, alguns tipos especiais de objetos específicos para ações:

- **Registro** **-** Este objeto representa a linha de uma tabela. Seus métodos são:
- **remove()** – Determina que o registro seja excluído. Este método não possui retorno.
- **save()** – Normalmente o registro será salvo de forma automática ao final da ação. Eventualmente, pode-se antecipar esse procedimento manualmente através desse método.
- **setCampo(nomeDoCampo, valorDoCampo)** – Altera o valor de um campo. Esse método não possui retorno.
- **getCampo(nomeDoCampo)** **–** Retorna o valor de um campo.
- **QueryExecutor** **-** Objeto responsável por interagir com o Banco de dados. Ele é obtido através da função getQuery descrita acima.

Os métodos do QueryExecutor, são:

- **nativeSelect(consultaSql)** – Executa a consulta. Podem ser utilizados parâmetros na consulta envolvendo o nome do parâmetro por chaves ("{MEU\_PARAMETRO}"). Não há retorno para esse método.
- **update(consultaSql)** – Usado para fazer UPDATE ou INSERT no banco. Não há retorno para esse método.
- **setParam(nomeDoParametro, valor)** – Atribui valor aos parâmetros da consulta/alteração. Não há retorno.
- **next()** – Navega no resultado da consulta. Quando não há mais registros retorna false.
- **getDouble(coluna)** – Retorna o valor da coluna solicitada. Pode ser o índice (1 para a 1ª coluna, 2 para a 2ª etc) ou o nome da coluna no banco de dados. O retorno é um número decimal.
- **getInt(coluna)** – Para colunas com conteúdo Inteiro.
- **getString(coluna)** – Para colunas de texto.
- **getDate(coluna)** – Retorna como uma data.

**Sub-aba Parâmetros**

![Imagem 5: Sub-aba Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/1500009256862)

Configure nesta sub-aba, os fatores a serem utilizados na ação; informe a **"Descrição"**, bem como o **"Nome"** do parâmetro.

No campo **"Tipo de parâmetro"**, defina a categoria do parâmetro dentre as seguintes opções:

- Texto;
- Número inteiro;
- Número decimal;
- Data;
- Data e hora;
- Verdadeiro/Falso;
- Pesquisa;
- Opções.

A marcação **"Obrigatório"** quando realizada determina que o parâmetro em questão será indispensável.

Com a marcação **"Sugerir último valor"** realizada, o último valor passado no parâmetro será sugerido quando este for novamente solicitado.

**Observação:** trabalhando-se na tela [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas), para exibir a descrição do campo ao utilizar a consulta por meio do botão **"Visualizar formulário"** é necessário primeiramente acessar o Botão Outras Opções, opção Avançado, e definir adequadamente o Campo para apresentação, campo este caracterizado como tipo texto. Esta medida é necessária para tabelas criadas pelo usuário; para tabelas do sistema não é necessário efetuar tal procedimento.

A pequena grade localizada na parte lateral direita da tela, apresenta todos os parâmetros que foram configurados para esta ação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#top)

### Lançador

Assim como para configuração das outras ações, primeiramente define-se a tabela na qual serão realizadas as configurações. Tomemos como exemplo a tabela **"TGFPAR"**.

![Imagem 6: Assim como para configuração das outras ações, primeiramente define-se a tabela na qual serão realizadas as…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010675581)

Definida a tabela, informe a **"Descrição"** desejada e determine o tipo **"Lançador"**. O próximo passo, é selecionar uma tela relacionada ao processo que será aberta quando o lançador que está sendo configurado for acionado. No nosso exemplo, utilizaremos o **"Inserir SAC"**.

![Imagem 7: Definida a tabela, informe a "Descrição" desejada e determine o tipo "Lançador" . O próximo passo, é selecionar uma…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010390182)

Feito isso, a ação está ligada a tabela TGFPAR; ao abrir a tela relacionada a esta tabela, você pode visualizar no botão **"Ações"** a ação criada:

![Imagem 8: Feito isso, a ação está ligada a tabela TGFPAR ; ao abrir a tela relacionada a esta tabela, você pode visualizar no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010675641)

A ação configurada **"Listar SACs"** quando acionada, abre a tela **"Inserir SAC"** conforme configuração realizada inicialmente no nosso exemplo ao selecionar a tela.

Além disso, deve-se realizar a configuração de um detalhe importante; para contextualizar a tela, deve-se incluir um argumento na ação configurada; esta inclusão é feita por meio da grade de **"Parâmetros"**; estes parâmetros relacionam os campos da tela "que faz a chamada" com os campos da tela "que recebe a chamada".

![Imagem 9: Além disso, deve-se realizar a configuração de um detalhe importante; para contextualizar a tela, deve-se incluir um…](https://ajuda.sankhya.com.br/hc/article_attachments/1500010390262)

Tem-se algumas considerações sobre estes parâmetros:

- Qualquer campo pode ser referenciado, independente de ser PK tanto na tela de origem quanto no destino.
- Caso não existam registros que atendam aos critérios estabelecidos, a tela entra automaticamente em modo de inclusão, preenchendo os campos referenciados com os respectivos valores. Isso adianta o processo de inclusão.
- Se existirem parâmetros para esta ação, ela só poderá ser executada quando todos os campos referenciados não estiverem vazios.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#top)

### Rotina Java

Java é uma linguagem bastante poderosa que conta com excelentes ferramentas de desenvolvimento de software. Para definir ações do tipo Rotina Java, é necessário que se tenha os conhecimentos básicos sobre a plataforma Java, além de contar com um ambiente de desenvolvimento, o Eclipse por exemplo.

Uma ação do tipo **"Rotina Java"**, diz respeito a uma classe java que deve ser implementada e disponibilizada em um JAR (do inglês, Java Archive ou Arquivo java, comumente denominado ".jar"), o qual será inserido no Sankhya-OM através do cadastro de [Módulos Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java).

Este cadastro foi criado para incluir classes personalizadas dentro do Sankhya-OM, tornando possível usar essas classes em conjunto com as do próprio sistema em pontos específicos. Na funcionalidade aqui discutida, cada ação será representada por uma classe, e um arquivo .jar pode conter várias classes; assim, pode-se ter dezenas de ações em um único jar. Além disso, cada módulo pode conter vários jar's, possibilitando, por exemplo, o uso de bibliotecas/utilitários de terceiros.

Uma classe só é considerada uma ação se for implementada a interface AcaoRotinaJava. Essa interface é bastante simples e só exige que o método doAction seja implementado. Este é o método que será executado quando a ação for disparada pelo usuário.

Essa interface está disponível na biblioteca **"Sankhya-W-extensions.jar"**, que pode ser baixada diretamente das telas [Construtor de telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773) ou [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

![Imagem 10: Essa interface está disponível na biblioteca "Sankhya-W-extensions.jar" , que pode ser baixada diretamente das telas…](https://ajuda.sankhya.com.br/hc/article_attachments/1500009270922)

Inicialmente, localize na tela a tabela a ser utilizada para inclusão da ação.

O passo seguinte é o preenchimento de uma **"Descrição"** e a escolha do tipo **"Rotina Java"**.

Defina o **"Módulo"** na qual a ação estará relacionada; o módulo aqui informado, deve ser cadastrado previamente na tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java); através do campo **"Classe Java"** efetue a seleção da classe que será executada nesta ação.

Em seguida, escolha uma das opções disponíveis no campo **"Depois de executar, recarregar"**, sendo elas:

- **Não recarrega nada:** Através desta definição, nenhum registro será recarregado.
- **Toda a grade:** Por esta opção, serão recarregados todos os registros da grade principal da tela, independente dos itens selecionados.
- **Os registros selecionados:** Serão recarregados apenas os registros selecionados para a ação.
- **O registro pai (Quando existir):**  No caso em que a ação é registrada para uma tela Detalhe, recarrega-se o registro da tela Mestre. Se selecionado para uma tela não Detalhe, recarrega-se toda a grade.
- **O registro principal (Quando existir):** A diferença para a opção anterior é sutil, mas entendamos que uma tela Mestre, pode ser Detalhe de outra. Por exemplo, quando executa-se uma ação para a tela "Participantes", o registro pai seria a "Etapa" e o registro principal a "Tarefa", pois Participante é Detalhe de Etapa, que por sua vez, é Detalhe de Tarefa.

A marcação **"Controle de transação manual"** por padrão, é apresentada desmarcada; caso esteja assinalada, o controle de transação com o banco de dados deve ser feito no seu respectivo script, de acordo com a necessidade. Caso esteja desmarcada, o sistema automaticamente controla a transação e realiza o commit no final da execução do script e faz o rollback caso existam erros na execução do script.

Na seção **"Parâmetros"**, você pode configurar os fatores a serem utilizados na ação; informe a **"Descrição"**, bem como o **"Nome"** do parâmetro.

No campo **"Tipo de parâmetro"**, informe a categoria do parâmetro dentre as seguintes opções:

- Texto;
- Número inteiro;
- Número decimal;
- Data;
- Data e hora;
- Verdadeiro/Falso;
- Pesquisa;
- Opções.

A marcação **"Obrigatório"** quando realizada determina que o parâmetro em questão será indispensável.

Com a marcação **"Sugerir último valor"** realizada, o último valor passado no parâmetro será sugerido quando este for novamente solicitado.

**Observação:** trabalhando-se na tela [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas), para exibir a descrição do campo ao utilizar a consulta por meio do botão **"Visualizar formulário"** é necessário primeiramente acessar o Botão Outras Opções, opção Avançado, e definir adequadamente o Campo para apresentação, campo este caracterizado como tipo texto. Esta medida é necessária para tabelas criadas pelo usuário; para tabelas do sistema não é necessário efetuar tal procedimento.

A pequena grade localizada na parte lateral direita da tela, apresenta todos os parâmetros que foram configurados para esta ação.

#### Inserção de avisos no sistema

O sistema permite por meio de uma procedure interna (nativa) chamada **"STP\_NOTIFICA\_SISTEMA"**, adicionar avisos ao usuário sobre qualquer alteração realizada no sistema. Estes avisos serão apresentados por meio do botão de Notificações do Sistema, localizado na parte superior direita da tela.

A utilização da referida procedure pode ser realizada através da criação de uma **Rotina Java** que permite a sua aplicação através de um botão de ação, bem como criar uma trigger diretamente no banco de dados para consumo da mesma.

Na chamada da procedure, devem ser informados os seguintes parâmetros:

- titulo - Título do aviso;
- Descricao - Descrição do link do aviso;
- codUsu - Código usuário destinatário;
- codGrupo - Código grupo destinatário;
- codUsuRemetente - Código usuário remetente.

Dentre os parâmetros acima, tem-se como obrigatório o parâmetro Descrição e codUsuRemetente. O parâmetro Descrição deve ser criado através da função **"GET\_LINK\_TELA"**, na chamada desta função devem ser informados os seguintes parâmetros:

- ResourceID - ResourceID da tela;
- textoLink - Texto do link;
- JsonPk - Json da PK.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es#top)
