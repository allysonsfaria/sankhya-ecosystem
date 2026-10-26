---
id: "360045111093"
titulo: "Configurando Ações Personalizadas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:29Z"
rotulos: ["Configuração", "FAP", "Dicionário de Dados", "Lançador", "Botões de ação na FAP", "Configurando Ações Personalizadas", "ORDENARACOES", "Outras opções", "ProjetoServico", "Configurando Ações Personalizadas manual", "Sankhya-Om", "Ações Personalizadas", "Script (JavaScript)"]
---

# Configurando Ações Personalizadas

Os botões de ação são uma ótima ferramenta de customização que permite que você, como usuário do Sankhya-Om, execute tarefas específicas de maneira simples e rápida. No [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas) e no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) por meio da aba **"Ações"**, é possível definir a execução de uma **"Rotina no Banco de dados"** (Stored Procedure), execução de uma **"Rotina Java"**, execução de um **"Script (JavaScript)"** e o Lançamento de uma tela do sistema.

A seguir, iremos auxiliá-lo a dar os primeiros passos nesse recurso e para ser mais objetivo, apresentaremos alguns conceitos básicos do Sankhya-Om, como cadastros Mestre/Detalhe, Dicionário de dados e Menus adicionais. 

Partindo de um exemplo didático, considere as seguintes tabelas adicionais:

- **Tarefa (TADTAR):**Um cadastro básico de tarefas.
- **CODTAREFA(PK):** Campo que identifica uma tarefa. Esse campo é a PK da tabela e é auto numerado.
- **DESCRTAR:** Descrição da tarefa.
- **NUNOTA:** Campo importado da TGFCAB.
- **Etapa (TADETA):** Cadastro do tipo **"Tela detalhe"** que vincula diversas etapas a uma tarefa. Como já é sabido, em relacionamentos Tela mestre/Tela detalhe, a Tela mestre é aberta por um menu adicional e a Tela detalhe aparece como uma aba onde são incluídos os registros filhos.
- **CODTAREFA(PK):** Campo que vincula uma etapa a uma tarefa e, por isso, faz parte da PK.
- **CODETAPA(PK):** Campo identifica uma etapa. Sendo ele, auto numerado.
- **DESCRICAO:** Descrição da tarefa.
- **Participante (TADPTA):** Cadastro do tipo Tela detalhe que vincula diversos participantes a uma etapa.
- **CODTAREFA(PK) e CODETAPA(PK):** Campos que vinculam um participante a uma etapa.
- **CODPARTICIPANTE(PK):** Campo identifica um participante. Esse campo é auto numerado.
- **NOME:** Nome do participante.

Assim, poderemos criar ações que poderão ser executadas em outras telas. Em seguida,  você pode consultar essas ações por meio dos links:

[Lançador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#lan%C3%A7ador)                                    [Rotina no Banco de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#rotinanobancodedados)                                     [Rotina Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#rotinajava)

[Script(Java Script)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#Script(javascript))                    [Botões de ação na FAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#bot%C3%B5esdea%C3%A7%C3%A3onafap)

### Lançador

Digamos que no processo de faturamento exista uma lista de tarefas a serem executadas por pedido e que ao ser criado o pedido, seja necessário definir essas tarefas. Seria interessante lançar o cadastro de tarefas diretamente da Central, filtrando as tarefas do pedido selecionado.

Dessa forma, localize a TGFCAB na tela Dicionário de Dados e na aba **"Ações"** criaremos um lançador para a tela, assim, teremos:

- Clique no botão **"Incluir"**;
- Informe a **"Descrição"** da ação e selecione o tipo **"Lançador"**. Assim, uma cópia do menu do sistema será exibida para determinar qual item abre a tela desejada;
- Em seguida, selecione o menu **"Tarefas"**.

[GIF animado: Imagem 1: Em seguida, s elecione o menu " Tarefas" .](https://ajuda.sankhya.com.br/hc/article_attachments/1500008276621)

```
           ![Imagem 2: GIF animado: Imagem 1: Em seguida, s elecione o menu " Tarefas" .](https://ajuda.sankhya.com.br/hc/article_attachments/42310938012695) Quando uma tabela adicional for utilizada, faça o uso da tela Construtor de telas.
```

Pelo fato de a ação estar ligada à **TGFCAB**, ao abrir a Central, a ação estará sob o Menu **"Ações"** na barra superior:

![Imagem 3: Pelo fato de a ação estar ligada à TGFCAB , ao abrir a Central, a ação estará sob o Menu "Ações" na barra superior:](https://ajuda.sankhya.com.br/hc/article_attachments/1500008098482)

Quando selecionado, o menu abrirá a tela **"Lista de Tarefas"**.

Para contextualizar a tela nas tarefas do pedido selecionado na Central, devemos incluir um argumento na ação que envia para tela requerida, o NUNOTA da TGFCAB. Para isso serve a grade de **"Parâmetros"** (não confunda com os parâmetros da TSIPAR). Esses parâmetros relacionam os campos da tela chamadora (Central) com os campos da tela chamada **"Tarefas"**. Assim, adicione um parâmetro ligando NUNOTA da origem com NUNOTA do destino. Assim, referente a esses parâmetros podemos destacar:

- Qualquer campo pode ser referenciado, independente de ser PK tanto na tela de origem quanto no destino.
- Caso não existam registros que atendam aos critérios estabelecidos, a tela entra automaticamente em modo de inclusão, preenchendo os campos referenciados com os respectivos valores. Isso adianta o processo de inclusão.
- Se existirem parâmetros para essa ação, ela só poderá ser executada quando todos os campos referenciados estiverem preenchidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)

### Rotina no Banco de Dados

Aqui, especificaremos o tipo de Ação Rotina no Banco de Dados:

**Observação:** os exemplos a serem exibidos são para Oracle, mas também é aplicável para SQLServer.

A base desse tipo de ação é uma Stored Procedure que será contextualizada e executada pelo sistema. Como existem vários recursos de programação e diferenças significativas entre os SGDB (Oracle e SqlServer) suportados pelo Sankhya-Om, a melhor maneira de criar a stored procedure é fazê-lo diretamente no banco. Assim, a interface de configuração das ações desse tipo coleta as informações necessárias para criar o corpo da procedure. Dessa forma, siga as orientações a seguir:

- Abra o Construtor de telas e nele localize a tabela de exemplo **"Tarefa"**;
- Na aba Ações, crie uma ação do tipo **"Rotina no Banco de Dados"** e informe a **"Descrição"**;
- No campo **"Nome da rotina"**, informe o nome da procedure propriamente dito.

![Imagem 4: No campo "Nome da rotina" , informe o nome da procedure propriamente dito.](https://ajuda.sankhya.com.br/hc/article_attachments/1500008105422)

No campo **"Depois de executar, recarregar"**, selecione uma dentre as seguintes opções:

- **Toda a grade:** Recarrega todos os registros da grade principal da tela, independente dos itens selecionados.
- **Os registros selecionados:** Recarrega somente os registros selecionados para a ação.
- **O registro pai (Quando existir):** No caso em que a ação é registrada para uma tela Detalhe, recarrega o registro da tela Mestre. Caso seja selecionado para uma tela não Detalhe, toda a grade será recarregada.
- **O registro principal (Quando existir):** A diferença é sutil, mas entenda que uma tela Mestre, pode ser Detalhe de outra. Por exemplo, quando estamos executando uma ação para a tela **"Participantes"**, o registro pai seria a **"Etapa"** e o registro principal seria a **"Tarefa"**, pois Participante é Detalhe de Etapa que por sua vez, é Detalhe de Tarefa.

Em seguida, salve a ação e clique no botão **"Criar uma template da rotina"** para gerar um template da procedure. Destacamos ainda que, se a procedure está compilada no Banco, o campo **"Nome da rotina"** ficará desabilitado.

O template criado revela como deve ser o "esqueleto" da procedure, ou seja, quais são os parâmetros e entrada e saida que ela deve ter. Dessa forma, considere:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
      P_CODUSU NUMBER,
      P_IDSESSAO VARCHAR2,
      P_QTDLINHAS NUMBER,
      P_MENSAGEM OUT VARCHAR2
) AS
BEGIN
END;

/
```

Referente aos parâmetros, teremos:

- **P\_CODUSU:** O código do usuário logado pode ser útil em alguns casos;
- **P\_IDSESSAO:** Esse identificador serve para separar o ambiente da execução;
- **P\_QTDLINHAS:** Determina quantas linhas estavam selecionadas no grid, no momento da execução.
- **P\_MENSAGEM** (parâmetro de saída)**:** Se houver atribuição de um valor para esse parâmetro, ao final da execução uma mensagem será exibida a você.

Em seguida, recompile a procedure da seguinte forma:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
      P_CODUSU NUMBER,
      P_IDSESSAO VARCHAR2,
      P_QTDLINHAS NUMBER,
      P_MENSAGEM OUTVARCHAR2
) AS
BEGIN
      INSERT INTO AD_TADTAR(CODTAREFA, DESCRTAR) VALUES(1,'Logística');
      INSERT INTO AD_TADETA(CODTAREFA, CODETAPA, DESCRICAO) VALUES(1, 1,
'Ligar para transportadora e agendar carregamento');

             INSERT INTO AD_TADPTA(CODTAREFA, CODETAPA, CODPARTICIPANTE
, NOME) VALUES(1, 1, 1,'Antônio');

END;

/
```

Ao executar a ação, podemos comprovar a inclusão dos registros.

Até aqui, já é possível fazer uma infinidade de ações, afinal, todo arsenal de programação do banco de dados pode usado para incluir/alterar/remover registros de qualquer tabela, efetuar desde os mais simples aos mais elaborados cálculos. Além disso, antes de executar a procedure, o Sankhya-Om prepara o ambiente de execução, passando alguns parâmetros. Esses parâmetros podem ser obtidos da seguinte forma:

Ao retornar à aba Ações, adicione um parâmetro do tipo texto chamado **NOMEPARTICIPANTE** e recompile a procedure assim:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
      P_CODUSU NUMBER,
      P_IDSESSAO VARCHAR2,
      P_QTDLINHAS NUMBER,
      P_MENSAGEM OUT VARCHAR2
) AS
     V_PROXIMO_ID_PARTICIPANTE NUMBER;
BEGIN
       -- Para descobrir o próximo codparticipante...
SELECT
      MAX(CODPARTICIPANTE)+ 1
INTO
      V_PROXIMO_ID_PARTICIPANTE
FROM
       AD_TADPTA
WHERE
CODTAREFA = 1 AND CODETAPA = 1;
       -- No primeiro participante, o valor da variável estará nulo.
IF V_PROXIMO_ID_PARTICIPANTE IS NULL THEN
             V_PROXIMO_ID_PARTICIPANTE := 1;
END IF;
      INSERT
            INTO AD_TADPTA (
                CODTAREFA,
                CODETAPA,
CODPARTICIPANTE,
NOME
) VALUES (
     1,
     1,
    V_PROXIMO_ID_PARTICIPANTE,
    ACT_TXT_PARAM(P_IDESESSAO, 'NOMEPARTICIPANTE')
);
END;
/
```

O resultado é que ao executar novamente, será mostrada uma janelinha solicitando o valor do parâmetro.

Posteriormente, a procedure irá obter o valor informado através da função **ACT\_TXT\_PARAM**. Isso é possível porque o Sankhya-Om injeta esses parâmetros no banco, antes de executar a procedure, por isso existe o parâmetro **P\_IDSESSAO** mencionado acima, sendo que ele é necessário para isolar o ambiente dessa execução.

Além da função **ACT\_TXT\_PARAM** mencionada acima, existem outras três funções, uma para cada tipo de dado, observe:

- **ACT\_TXT\_PARAM:** Retorna um valor VARCHAR, usada para parâmetro do tipo texto;
- **ACT\_INT\_PARAM:** Retorna um valor NUMBER, usada para parâmetro do tipo numero inteiro;
- **ACT\_DEC\_PARAM:** Retorna um valor NUMBER, usada para parâmetro do tipo numero decimal;
- **ACT\_DTA\_PARAM:** Retorna um valor DATE, usada para parâmetro do tipo data.

Todas essas funções têm a mesma estrutura. Recebem o ID da sessão como primeiro argumento e o Nome do parâmetro como segundo.

Também estão disponíveis a PK de todos os registros selecionados na grade no momento da execução. Para obter essas informações, existem quatro funções semelhantes, observe:

- **ACT\_TXT\_FIELD:** Retorna um valor VARCHAR, usada para campos do tipo texto;
- **ACT\_INT\_FIELD:** Retorna um valor NUMBER, usada para campos do tipo numero inteiro;
- **ACT\_DEC\_FIELD:** Retorna um valor NUMBER, usada para campos do tipo numero decimal;
- **ACT\_DTA\_FIELD:** Retorna um valor DATE, usada para campos do tipo data.

A diferença no uso dessas funções, é que além do ID da sessão e o Nome do campo, é necessário também informar um Índice que determina a sequencia das linhas selecionadas. Assim, considere o exemplo:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
      P_CODUSU NUMBER,
      P_IDSESSAO VARCHAR2,
      P_QTDLINHAS NUMBER,
      P_MENSAGEM OUT CARCHAR2
) AS
      V_PROXIMO_ID_PARTICIPANTE NUMBER;
      V_CODTAREFA NUMBER;
      V_NOMEPARTICIPANTE VARCHAR2(4000);
BEGIN
      -- Pegamos o valor digitado pelo usuário e guardamos nessa variável.
                           V_NOMEPARTICIPANTE      :=     ACT_TXT_PARAM(P_IDSESSAO,
'NOMEPARTICIPANTE');
     -- Como visto, P_QTDLINHAS determina quantas linhas estão selecionadas
      FOR I IN 1..P_QTDLINHAS
      LOOP
         -- Aqui, "I" representa a qual linha estamos nos referindo.
         V_CODTAREFA := ACT_INT_FIELD(P_IDSESSAO, I, 'CODTAREFA');
         SELECT
               MAX(CODPARTICIPANTE) + 1
         INTO
              V_PROXIMO_ID_PARTICIPANTE
         FROM
             AD_TADPTA
         WHERE
              CODTAREFA = V_CODTAREFA AND CODETAPA = 1;
         -- No primeiro participante, o valor da variáve estará nulo.
         IF V_PROXIMO_ID_PARTICIPANTE IS NULL THEN
              V_PROXIMO_ID_PARTICIPANTE := 1;
         END IF;
         -- Com todos os valores necessários, fazemos a inclusão
         INSERT
              INTO AD_TADPTA (
                  CODTAREFA,
                  CODTAPA,
                  CODPARTICIPANTE,
                  NOME
              ) VALUES (
                  V_CODTAREFA,
                  1,
                 V_PROXIMO_ID_PARTICIPANTE,
                 ACT_TXT_PARAM(P_IDSESSAO, 'NOMEPARTICIPANTE')
              );
         END LOOP;

END;

 /
```

Com duas Tarefas selecionadas, execute novamente a ação.

De acordo com a procedure, o nome do participante informado, será incluído na etapa 1 das duas tarefas. 

Em algumas situações, pode ser necessário solicitar  uma confirmação durante a execução da ação. Por exemplo, digamos que uma etapa normalmente tenha no máximo dois participantes e se estiver sendo solicitada a inclusão de um terceiro participante, você deve ser consultado antes de proceder a inclusão. Dessa forma, deve-se recompilar a procedure da seguinte maneira:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
   P_CODUSU NUMBER,
   P_IDSESSAO VARCHAR2,
   P_QTDLINHAS NUMBER,
   P_MENSAGEM OUT VARCHAR2
) AS
   V_PROXIMO_ID_PARTICIPANTE NUMBER;
   V_CODTAREFA NUMBER;
   V_NOMEPARTICIPANTE VARCHAR2(4000);
   V_TOTAL_PARTICIPANTES NUMBER;
   V_DESCRTAREFA VARCHAR(4000);
   V_DESCRETAPA VARCHAR(4000);
   V_TITULO VARCHAR(4000);
   V_MENSAGGEM VARCHAR(4000);
   V_INCLUIR BOOLEAN;
BEGIN

  -- Pegamos o valor digitado pelo usuário e guardamos nesta variável.
                V_NOMEPARTICIPANTE          :=   ACT_TXT_PARAM(P_IDSESSAO,
'NOMEPARTICIPANTE');
  -- Como visto,, P_QTDLINHAS determina quantas linhas estão selecionadas
   FOR I IN 1..P_QTDLINHAS
   LOOP
     -- Aqui, "I" representa a qual linha estamos nos referindo.
     V_CODTAREFA := ACT_INT_FIELD(P_IDSESSAO, I, 'CODTAREFA');
     SELECT
        TAR.DESCRTAR,
        ETA.DESCRICAO,
        MAX(CODPARTICIPANTE) + 1,
        COUNT(1)
     INTO
        V_DESCRTAREFA,
        V_DESCRETAPA,
        V_PROXIMO_ID_PARTICIPANTE,
        V_TOTAL_PARTICIPANTES
       FROM
        AD_TADTAR TAR
        INNER JOIN AD_TADETA ETA ON ETA.CODTAREFA = TAR.CODTAREFA
          INNER JOIN AD_TADPTA ETA ON ETA.CODTAREFA = ETA.CODTAREFA
AND PTA.CODTAPA = ETA.CODETAPA
     WHERE
       TAR.DESCRTAR = V_CODTAREFA AND ETA.CODETAPA = 1
     GROUP BY
        TAR.DESCRTAR, ETA.DESCRICAO;

     -- No primeiro participante, o valor da variável estará nulo.
     IF V_PROXIMO_ID_PARTICIPANTE IS NULL THEN
         V_PROXIMO_ID_PARTICIPANTE := 1;
     END IF;
      --Se o total de participantes ainda não chegou ao limite, a inclusão está liberada
     IF V_TOTAL_PARTICIPANTES < 2 THEN
        V_INCLUIR := TRUE;
     ELSE -- Senão, faz uma pergunta ao usuário.
       V_TITULO := 'Máximo de participantes atingido';

            V_MENSAGEM := 'A etapa "' || V_DESCRETAPA || '"(Tarefa "' ||
V_DESCRTAREFA   || '") já possui   '  ||  V_TOTAL_PARTICIPANTES    ||  '
participantes.\n\nDeseja continuar?';
              V_INCLUIR := ACT_ESCOLHER_SIMNAO(V_TITULO, V_MENSAGEM,
P_IDSESSAO, I) = 'S';
     END IF;
     IF V_INCLUIR THEN
       -- Com todos os valores necessários, fazemos a inclusão
       INSERT
          INTO AD_TADPTA (
            CODTAREFA,
            CODETAPA,
            CODPARTICIPANTE,
            NOME
         ) VALUES (
            V_CODTAREFA,
            1,
            V_PROXIMO_ID_PARTICIPANTE,
           ACT_TXT_PARAM(P_IDSESSAO, 'NOMEPARTICIPANTE')
         );
    END IF;
  END LOOP;
END;

/
```

Com duas Tarefas selecionadas execute novamente a ação, informe o nome do participante e clique em **"OK"**.

Será exibida uma mensagem de confirmação em que o sistema irá informá-lo que há mais de dois participantes.

Isso é feito através da função **ACT\_ESCOLHER\_SIMNAO** e durante a execução da rotina. Quando essa função é chamada, o sistema interrompe a ação, exibe o pop-up de confirmação na tela e espera a sua decisão. Se o botão **"Cancelar"** for pressionado, a ação é cancelada. Se o botão **"Sim"** for o escolhido, a ação é retomada e o retorno da função será **"S"**. Caso você selecione **"Não"**, o retorno da função será **"N"**. Essa função recebe 4 argumentos, sendo eles:

- **P\_TITULO:** O título da janela de confirmação;
- **P\_TEXTO:** A mensagem de confirmação que será exibida;
- **P\_CHAVE:** Como dito anteriormente, serve para isolar o ambiente de execução da ação e é recebido como argumento na procedure;
- **P\_SEQUENCIA:** Trata-se de um número inteiro, que serve para identificar a pergunta. Digamos que exista mais de uma chamada à **ACT\_ESCOLHER\_SIMNAO**, cada uma delas deverá ter um valor diferente para esse parâmetro. Assim, poderemos identificar corretamente as suas respostas.

---

![Imagem 5: P_SEQUENCIA: Trata-se de um número inteiro, que serve para identificar a pergunta. Digamos que exista mais de uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16118136679959)

Se existirem duas perguntas **ACT\_ESCOLHER\_SIMNAO** com mesma **P\_SEQUENCIA**, a resposta da primeira pergunta será repassada para a segunda, e ela ficará sem efeito. A chamada está dentro do loop de registros, usamos a variável I como sequência, a fim da pergunta se repetir a cada registro.

---

Além da confirmação **ACT\_ESCOLHER\_SIMNAO**, existe outra função chamada **ACT\_CONFIRMAR**, que recebe os mesmos argumentos e fará basicamente a mesma coisa. A diferença entre elas, é que não existe uma resposta, em que você pode escolher entre **"OK"**, que nesse caso retoma a execução, ou **"Cancelar"**, que faz a ação ser cancelada, portanto **ACT\_CONFIRMAR** não terá retorno.

Referente ao **"PK do registro mestre"**, quando uma ação é executada em uma tela detalhe, os campos PK da tela pai estarão disponíveis como se fossem parâmetros, podendo ser obtidos através de uma das funções **ACT\_TXT\_PARAM**, **ACT\_INT\_PARAM**, **ACT\_DEC\_PARAM** ou **ACT\_DTA\_PARAM** mencionadas acima. É possível utilizar o próprio nome do campo precedido de **"**MASTER\_", assim, ações da aba **"Participantes"** podem usar, por exemplo, ACT\_INT\_PARAM(P\_IDSESSAO, ‘MASTER\_CODTAREFA’) e ACT\_INT\_PARAM(P\_IDSESSAO, ‘MASTER\_CODETAPA’).

**Nota:** a procedure pode retornar uma mensagem a ser exibida por meio do parâmetro de saída **"P\_MENSAGEM"**. Quando existir um valor para esse parâmetro, o Sankhya-Om o exibirá como uma informação:

```
CREATE OR REPLACE PROCEDURE "STP_CHECK_LIST" (
       P_CODUSU NUMBER,
       P_IDSESSAO VARCHAR2,
       P_QTDLINHAS NUMBER,
       P_MENSAGEM OUT VARCHAR2
) AS
BEGIN
      P_MENSAGEM := 'A ação foi executada com sucesso!';
END;

/
```

Dessa forma, a ação será executada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)

### Rotina Java

Java é uma linguagem muito poderosa, robusta e possui excelentes ferramentas de desenvolvimento de software. Para definir ações do tipo rotina Java, você precisa ter os conhecimentos básicos sobre a plataforma Java e contar com um ambiente de desenvolvimento, como por exemplo, o Eclipse.

Uma ação do tipo Rotina Java, nada mais é que uma classe java que deve ser implementada e disponibilizada em um JAR (do inglês, Java Archive ou Arquivo java, comumente denominado ".jar"), em que, será inserido no Sankhya-Om através do Cadastro de Módulos Java. Esse cadastro foi criado para incluir classes personalizadas dentro do Sankhya-Om, tornando possível usar essas classes em conjunto com as do próprio sistema em pontos específicos. Na funcionalidade aqui discutida, cada ação será representada por uma classe e um arquivo .jar, que pode conter várias classes, assim, podemos ter dezenas de ações em um único JAR. Além disso, cada módulo poderá possuir vários JARs, possibilitando, por exemplo, o uso de bibliotecas/utilitários de terceiros.

A seguir, exibiremos como as classes escritas em Java estarão no Sankhya-Om.

Uma classe só é considerada uma ação se implementar a interface AcaoRotinaJava. Essa interface é bastante simples e só exige que o método doAction seja implementado. Esse é o método que será executado quando você disparar uma ação.

Vamos refazer em Java, o exemplo **"Gerar financeiro"** aplicado à ação JavaScript:

**Nota:** aqui, trataremos apenas do Eclipse, mas você pode utilizar Netbeans ou qualquer outra IDE. Dependendo da versão do Eclipse, as telas podem ter aparência ligeiramente diferente, porém, essa mudança não afetará as ações a serem realizadas.

Obtenha uma versão do Eclipse pelo site http://www.eclipse.org/downloads, sendo que, você deve optar pela versão **"Eclipse IDE for Java EE Developers"**, pois caso precise "debugar" sua ação, essa versão permite rodar um servidor de aplicações diretamente dentro do Eclipse. Se ainda não estiver familiarizado com a ferramenta, existe uma extensa documentação, incluindo tutoriais no mesmo site disponibilizado acima.

Crie um projeto Java através de **"File > New > Java Project"**. No passo seguinte informe um nome para o projeto e clique em **"Finish"**.

[GIF animado: Imagem 6: Crie um projeto Java através de "File > New > Java Project" . No passo seguinte informe um nome para o projeto e clique…](https://ajuda.sankhya.com.br/hc/article_attachments/8498350442647)

Em seguida, baixe a biblioteca de extensão do Sankhya-Om, clicando no botão **"Baixar biblioteca de extensões"** e salve o arquivo em um local conhecido, por exemplo: **"C:\Bibliotecas Java"**. Considere ainda que, o botão Baixar biblioteca de extensões ficará disponível quando o tipo de ação escolhido for **"Rotina Java"**.

Em seguida, adicione a biblioteca ao projeto e clique com o botão direito sobre o projeto e escolha a opção **"Build Path"** e em seguida selecione a opção **"Add External Archives"**.

Selecione o arquivo que acabamos de baixar, e finalize. O resultado deve ser algo parecido com:

![Imagem 7: Selecione o arquivo que acabamos de baixar, e finalize. O resultado deve ser algo parecido com:](https://ajuda.sankhya.com.br/hc/article_attachments/8498458051607)

Crie a classe que irá representar a ação da seguinte maneira:

Clique no menu **"File > New > Class"**.

Defina o pacote em que a classe deverá ser criada.

---

![Imagem 8: Defina o pacote em que a classe deverá ser criada.](https://ajuda.sankhya.com.br/hc/article_attachments/16118136679959)

Você deve atentar-se ao último ponto, pois evita conflitos entre a sua classe e uma outra classe que coincidentemente tenha o mesmo nome. Existe uma convenção para a definição do pacote que inverte os fragmentos do domínio, sendo ele o endereço pelo qual acessamos as páginas na Web. Por exemplo, classes da Sankhya sempre estarão abaixo do pacote br.com.sankhya que é justamente o domínio da Sankhya invertido.

---

Depois, informe o nome da classe; pode ser algo como AcaoGerarFinanceiro.

Clique no botão **"Add"** ao lado do campo Interfaces.

Em **"Choose interfaces"** defina a interface AcaoRotinaJava para ser implementada e clique em **"OK"**.

Ao clicar em **"Finish"** e deve obter um resultado semelhante a:

![Imagem 9: Ao clicar em " Finish" e deve obter um resultado semelhante a:](https://ajuda.sankhya.com.br/hc/article_attachments/8498572931223)

Observe que o método doAction recebe um parâmetro do tipo ContextoAcao. Esse objeto é responsável por todas as funcionalidades que descrevemos anteriormente, como obter o valor de um parâmetro, agendar o envio de um email, criar uma nova linha, etc.

Em seguida, mude a implementação do método doAction assim:

```
public void doAction(ContextoAcao contexto) throws Exception {

           //Obtemos uma consulta para buscar os lançamentos

           QueryExecutor query = contexto.getQuery();

           //preparamos a execução da query, incluindo o parâmetro CODVEICULO.

            query.setParam("CODVEICULO", contexto.getParam("CODVEICULO"));

                query.nativeSelect("SELECT * FROM AD_TADCKM WHERE CODVEICULO =
{CODVEICULO}");

           double vlrDesdob = 0;

           while(query.next()){

                 double reembolso = query.getDouble("REEMBOLSO");

                 //Só permitimos gerar o título quando todos
                 //os lançamentos estiverem com reembolso calculado.

                 if(reembolso &gt; 0){

                       vlrDesdob += reembolso;

                 } else {
                                            contexto.mostraErro("O reembolso do lançamento " +
query.getInt("SEQUENCIA") + " não foi calculado ainda.");
             }

      }
      if(vlrDesdob == 0){
             contexto.confirmar("Valor do título zerado", "O veículo informado não
possui lançamentos para reembolso, o título terá valor de desdobramento igual a
zero. Deseja continuar?", 1);

            }

            //por questões de desempenho é aconselhavel
            //fechar a consulta sempre que ela não for mais necessária.

            query.close();

            //Solicitamos a inclusão de uma linha no financeiro

            Registro financeiro = contexto.novaLinha("TGFFIN");

            //Informamos os campos desejados para incluir o financeiro

            financeiro.setCampo("VLRDESDOB", vlrDesdob);

            financeiro.setCampo("RECDESP", -1);

            financeiro.setCampo("CODEMP", 11);

            financeiro.setCampo("NUMNOTA", 0);

            financeiro.setCampo("DTNEG", "04/10/2012");

            financeiro.setCampo("CODPARC", 0);

            financeiro.setCampo("CODNAT", 3050200);

            financeiro.setCampo("CODBCO", 0);

            financeiro.setCampo("CODTIPTIT",2);

            financeiro.setCampo("DTVENC", "04/10/2012");

            financeiro.setCampo("HISTORICO", "REEMBOLSO DE KM PARA O VEÍCULO"
+ contexto.getParam("CODVEICULO"));

           //Quando o "save" do registro é acionado,
           //a alteração é feita no Banco de dados.
           //Portanto aqui estamos incluindo um registro na TGFFIN.
           financeiro.save();

                  //Finalmente configuramos uma mensagem para ser exibida após a
execução da ação.

           StringBuffer mensagem = new StringBuffer();

           mensagem.append("Foi gerado o título ");

           mensagem.append(financeiro.getCampo("NUFIN"));

           mensagem.append(" no valor de ");

           mensagem.append(financeiro.getCampo("VLRDESDOB"));

           mensagem.append(" como reembolso de KM para o veículo ");

           mensagem.append(contexto.getParam("CODVEICULO"));

           contexto.setMensagemRetorno(mensagem.toString());
     }
```

Para o próximo passo, exporte o projeto para um arquivo JAR:

- Clique em **"File > Export"**.
- No diálogo **"Destino"** selecione a opção **"Java > JAR file"** na árvore e clique em **"Next"**.
- No passo seguinte, selecione a sua classe como conteúdo do arquivo, defina o nome do arquivo e clique em Finish (os passos seguintes podem ser ignorados).

![Imagem 10: No passo seguinte, selecione a sua classe como conteúdo do arquivo, defina o nome do arquivo e clique em Finish (os…](https://ajuda.sankhya.com.br/hc/article_attachments/8498661037335)

Em seguida, acesse a tela [Configurações > Avançado > Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java) e crie um módulo.

---

![Imagem 11: Em seguida, acesse a tela Configurações > Avançado > Módulo Java e crie um módulo.](https://ajuda.sankhya.com.br/hc/article_attachments/16118136679959)

Para evitar conflitos entre os módulos, fique muito atento ao campo Identificador, pois o objetivo dele é identificar unicamente o seu módulo para efeito de exportação/Importação de módulos. Esse campo será usado como identificador de recursos. É extremamente aconselhável usar o mesmo padrão de domínio reverso mencionado para a criação de pacotes.

---

![Imagem 12: Para evitar conflitos entre os módulos, fique muito atento ao campo Identificador , pois o objetivo dele é identificar…](https://ajuda.sankhya.com.br/hc/article_attachments/1500008322461)

Na aba **"Arquivo Módulo (Jar)"**, Ao clicar no botão ![Imagem 13: Na aba "Arquivo Módulo (Jar)" , Ao clicar no botão "Cadastrar Arquivo Módulo (Jar) (F8)" , adicione o JAR que você…](https://ajuda.sankhya.com.br/hc/article_attachments/16118136684695) **"Cadastrar Arquivo Módulo (Jar) [F8]"**, adicione o JAR que você criou.

Na aba de Ações, altere a ação **"Gerar financeiro"** selecionando no campo **"Tipo"**, a opção **"Rotina Java"**, selecione o módulo e clique no botão **"Seleção da classe que será executada nesta ação"** ao lado do campo **"Classe Java"**, e escolha a ação que criamos. 

**Nota:** o comportamento dessa ação é exatamente a que será descrita no tópico **"Java Script"** desse artigo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)

### Script (Java Script)

Com as ações do tipo Rotina no Banco de Dados vimos como estender as funcionalidades das telas do Sankhya-Om com StoredProcedure, maximizando as possibilidades de customização.

Uma opção às ações de Banco de dados são as ações do tipo Script, que através da linguagem JavaScript abrem um novo arsenal de programação, além de suportar as mesmas funcionalidades básicas apresentadas anteriormente. Apesar da semelhança do nome, JavaScript não possui relação com Java.

JavaScript é uma linguagem poderosa e bastante difundida em aplicações Web, sendo fácil obter exemplos e tutoriais de como utilizá-la. 

É importante destacar que o JavaScript que usaremos será executado no servidor e não no browser, como é mais comumente usado. Essa diferença faz com que alguns recursos do navegador, como a função alert() e o objeto window não estejam disponíveis para uso em nossos scripts, sendo que esses recursos são de fato do navegador e não da linguagem. No entanto, ao lado do servidor, é possível fazer outras coisas que o JavaScript do browser não consegue, como consultas e alterações no Banco de dados.

Ao utilizar o JavaScript, alguns recursos usados no JavaScript de páginas HTML, como aqueles que rodam no ambiente do navegador, não estão disponíveis para serem utilizados em ações. Dessa forma, como na maioria das linguagens, é possível criar variáveis, usar estruturas como laços de repetição, operadores de comparação, operadores aritméticos, etc. Também estão disponíveis a maioria das funções globais, como parseInt, isNaN, etc. Além disso, você também pode declarar suas próprias funções e invocá-las livremente.

**Observação:** a maioria das fontes de estudos misturam os conceitos da linguagem JavaScript e do mecanismo que o navegador usa para interpretar o script das paginas HTML. Tente não se confundir, pois o objetivo dos nossos scripts não é tratar HTML.

Portanto, teremos disponível além do JavaScript, a sintaxe básica da linguagem com alguns recursos especiais. Assim, teremos:

- **Função novaLinha -** **novaLinha([nomeDaTabela]):** Função utilizada para inserir um registro novo. Se for informado o nome da tabela, o registro será criado nessa tabela. Caso contrário, será criado na tabela da qual pertence a ação. Essa função, retorna um objeto do tipo Registro, que será detalhado adiante.

**Nota:** quando essa função é chamada, o registro ainda não existe no banco de dados e não estará disponível em consultas até o fim da ação. Mas se durante a execução for necessário antecipar a inclusão, o método save() do registro pode ser acionado. Assim, teremos:

```
var financeiro = novaLinha("TGFFIN");

//Aqui temos um registro virtual pronto para receber todos os campos do financeiro

//mas ele é criado vazio e não existe no banco de dados.

...

//Depois de informar todos os campos obrigatórios, podemos efetuar a inclusão
financeiro.save();
```

- **Função getParam -** **getParam(nomeDoParametro):** Função responsável por retornar o valor dos parâmetros que você informar. Segue o mesmo principio discutido no exemplo da StoredProcedure, porém, mais simples, pois seu único argumento é o nome do parâmetro, sendo ele:

| ``` var codigoDoVeiculo = getParam("CODVEICULO") ``` |
| --- |

- **Função confirmar -** **confirmar(titulo, texto, indice):** Essa função exibe um diálogo, em que você terá a opção de prosseguir ou cancelar a ação. É muito útil em situações onde o resultado da ação pode trazer consequências imprevistas. Dessa forma, temos o referido diálogo:

| ``` confirmar("Valor do título zerado","Desdobramento igual a zero. Deseja continuar?", 1). ``` |
| --- |

- Função confirmarSimNao - **confirmarSimNao(titulo, texto, indice):** Funcionamento semelhante à ação anterior, porém, na ação tratada aqui, além de cancelar a execução, você pode optar por **"Sim"** ou **"Não"**, em que o retorno poderá ser true ou false. Assim, teremos:

```
if(confirmarSimNao("Registro inconsistente", "Localizado um registro inconsistente.
Deseja corrigi-lo?', 1)){

...

} else {
...

}
```

- **Função email -** **email (título, mensagem, destinatários):** Essa função adiciona uma mensagem a ser enviada por email, uma vez que a lista de destinatários deve ser separada por vírgula.
- **Função mostraErro -** **mostraErro(mensagem):** Esta irá interromper a execução da ação, mostrando uma mensagem de erro.
- **Função getQuery -** **getQuery():** Cria um objeto capaz de executar consultas ou mesmo alterar o estado do banco de dados. O objeto retornado é um QueryExecutor. Observe detalhes desse objeto abaixo:

| ``` var query = getQuery();  //Os parâmetros DEVEM ser incluídos antes de executar a consulta.  query.setParam("CODVEICULO", getParam("CODVEICULO"));  query.nativeSelect("SELECT * FROM TGFVEI WHERE CODVEICULO =     {CODVEICULO}");   while(query.next()){     var placa = query.getString("PLACA"); ...  } ``` |
| --- |

- **Função newJava -** **newJava(classname):** Por meio deste, é possível criar instâncias de objetos java para suprir uma eventual demanda não atendida pela estrutura JavaScript. Por exemplo, veja como formatar uma data:

| ``` //Instanciamos um objeto SimpleDateFormat do java         var simpleDateFormat = newJava("java.text.SimpleDateFormat");  //determinamos o padrão de formatação pelo método applyPattern. Mais detalhes podem ser  //vistos em http://http://docs.oracle.com/javase/6/docs/api/java /text/SimpleDateFormat.html        simpleDateFormat.applyPattern("dd/MM/yyyy");  //utilizando o método format, convertemos uma data em string, formatando  de acordo com o padrão determinado acima.  var dataFormatada = simpleDateFormat.format(new Date()); //pra finalizar exibimos uma mensagem para ver o resultado da formatação mensagem = "A data formatada é " + dataFormatada; ``` |
| --- |

- **Função javaClass -** **javaClass(classname):** Essa função se assemelha à anterior, porém, o retorno é uma Classe java e não uma instância dessa classe. Serve para usar métodos e atributos estáticos das classes Java.

Teremos também, algumas variáveis de ambiente. São elas:

- **linhas** (tipo Array)**:** Esse array representa as linhas selecionadas na grade. Os itens desse array são objetos do tipo Registro.
- **linhaPai** (tipo Registro)**:** Linha pai é um objeto do tipo Registro que representa a linha da tela master quando a ação estiver vinculada a uma tela detalhe.
- **mensagem** (tipo String)**:** Se algum valor for atribuído a essa variável, será exibido como uma informação ao final da execução.

Posteriormente, temos alguns tipos especiais de objetos específicos para ações, observe:

- **Registro:** Esse objeto representa a linha de uma tabela. Nele, temos dois métodos, sendo o primeiro deles o **"remove()"**, que não possui retorno e determina que o registro seja excluído. Em seguida, temos o **"save()"**, em que nele, usualmente o registro será salvo de forma automática ao final da ação. Eventualmente, pode-se antecipar esse procedimento manualmente através desse método.
- **setCampo(nomeDoCampo, valorDoCampo):** Altera o valor de um campo. Esse método não tem retorno.
- **getCampo(nomeDoCampo):** Retorna o valor de um campo.
- **QueryExecutor:** Esse objeto será responsável por interagir com o Banco de dados. Ele é obtido através da função getQuery descrita acima. A seguir, temos um exemplo básico de consulta ao banco de dados usando esse objeto:

| ``` //Obtemos uma instância do QueryExecutor através da função getQuery     var query = getQuery();  //Se a consulta utiliza parâmetros, devemos informá-los antes de executar      query.setParam("DATAINICIO", "01/09/2013");   query.setParam("DATAFIM", "03/10/2013");  //Executamos a consulta (o nome dos parâmetros deve ser delimitado por {})    query.nativeSelect("SELECT * FROM TGFFIN WHERE DHMOV >    {DATAINICIO} AND DHMOV < {DATAFIM}");  //E criamos um laço para percorrer o resultado, adicionando o número dos títulos  em um array //para exibir uma mensagem no final.    var titulos = new Array();   while(query.next()){  //esse método push, adiciona um elemento ao final do array.    titulos.push(query.getString("NUFIN"));  }  if(titulos.length > 0){             //o método join do array, concatena os elementos, colocando um separador entre eles.       mensagem = 'Foram localizados os títulos "' + titulos.join(",") + '" no período pesquisado.';  } else {       mensagem = "Não existem títulos para o períodos pesquisado";  } ``` |
| --- |

Temos a seguir, os métodos do QueryExecutor:

- **nativeSelect(consultaSql):** Executa a consulta. Sendo que, podem ser usados parâmetros na consulta envolvendo o nome do parâmetro por chaves (“{MEU\_PARAMETRO}”). Esse metódo não possui retorno.
- **update(consultaSql):** Usado para fazer UPDATE ou INSERT no banco. Não há retorno para esse método.
- **setParam(nomeDoParametro, valor):** Atribui valor aos parâmetros da consulta/alteração. Não possui retorno.
- **next():** Navega no resultado da consulta. Quando não há mais registros retorna false.
- **getDouble(coluna):** Retorna o valor da coluna solicitada. Pode ser o índice (1 para a 1ª coluna, 2 para a 2ª, etc.), ou o nome da coluna no banco de dados. O retorno é um número decimal.
- **getInt(coluna):** Para colunas com conteúdo Inteiro.
- **getString(coluna):** Para colunas de texto.
- **getDate(coluna):** Retorna como uma data.

A seguir, exibiremos um exemplo Prático. Assim, faremos um controle de quilometragem de frota, utilizando uma tela adicional, observe:

- **Controle de quilometragem (TADCKM):** Tela para lançamento de movimentação de veículos;
- **SEQUENCIA(PK):** Esse campo é a PK da tabela e é auto numerado;
- **CODVEICULO:** Campo importado da TGFVEI;
- **SAIDA:** Data e hora de saída do veículo;
- **CHEGADA:** Data e hora de chegada do veículo;
- **KMINICIAL:** Quilometragem do veículo na saída;
- **KMFINAL:** Quilometragem do veículo na chegada;
- **DISTÂNCIA:** Diferença entre a quilometragem de chegada e de saída. Esse campo é do tipo calculado e deve ter a seguinte expressão:

| ``` if($col_KMINICIAL == null || $col_KMFINAL == null){         return null;  } else {      return $col_KMFINAL.subtract($col_KMINICIAL);  } ``` |
| --- |

- **REEMBOLSO:** O valor desse campo será calculado com base na distância percorrida multiplicado pelo preço do Km.

Para fazer o cálculo do reembolso, criaremos uma ação do tipo Script com a rotina abaixo:

| ``` for(var i = 0; i < linhas.length; i++){    var linha = linhas[i];               linha.setCampo("REEMBOLSO", linha.getCampo("DISTANCIA") * getParam("PRECOKM"));  } ``` |
| --- |

E criamos um parâmetro numérico para representar o preço do KM.

Depois de alguns lançamentos na tela de **"Controle de quilometragem"**, ao executar a ação **"Calcular reembolso"**, nossa ação usa o preço do Km informado por parâmetro e o campo calculado DISTANCIA para determinar o valor do campo REEMBOLSO.

Perceba que utilizamos um campo que não existe no banco de dados, sendo ele o campo calculado DISTANCIA. Isso não seria possível em uma ação do tipo StoredProcedure.

Outra vantagem de ações Script em relação a StoredProcedure, é que não é necessário informar a PK auto-numerada o que não acontece quando inserimos registros diretamente no banco de dados, uma vez que a chave automática é gerada no servidor de aplicação (como foi visto no exemplo da StoredProcedure precisamos fazer um SELECT MAX para determinar a próxima PK disponível). Dessa forma, teremos:

```
var linha = novaLinha();

O campo SEQUENCIA que é a PK, não precisa ser informado, pois esse campo é
auto-numerado

linha.setCampo("CODVEICULO", 6);

linha.setCampo("SAIDA", "11/09/2012");

linha.setCampo("CHEGADA", "12/09/2012");

linha.setCampo("KMINICIAL", 33250);

linha.setCampo("KMFINAL", 33300);

Uma outra ação para essa tela, seria lançar um Título financeiro para o reembolso
das despesas com combustível, para tal:

Crie uma nova ação do tipo script contendo o seguinte código:

Obtemos uma consulta para buscar os lançamentos

var query = getQuery();

preparamos a execução da query, incluindo o parâmetro CODVEICULO.

query.setParam("CODVEICULO", getParam("CODVEICULO"));

query.nativeSelect("SELECT * FROM AD_TADCKM WHERE CODVEICULO = {CODVEICULO}");

var vlrDesdob = 0;

while(query.next()){

      var reembolso = query.getDouble("REEMBOLSO");

Só permitimos gerar o título quando todos os lançamentos estiverem com reembolso
calculado.

   if(reembolso > 0){

       vlrDesdob += reembolso;

    } else {

        mostraErro("O reembolso do lançamento " + query.getInt("SEQUENCIA") + " não foi
calculado ainda.");

    }

}

if(vlrDesdob == 0){

confirmar("Valor do título zerado", 'O veículo informado não possui lançamentos para
reembolso, o título terá valor de desdobramento igual a zero. Deseja continuar?', 1);

}

//por questões de desempenho é aconselhavel

//fechar a consulta sempre que ela não for mais necessária.

query.close();

Solicitamos a inclusão de uma linha no financeiro

var financeiro = novaLinha("TGFFIN");

Informamos os campos desejados para incluir o financeiro

financeiro.setCampo("VLRDESDOB", vlrDesdob);

financeiro.setCampo("RECDESP", -1);

financeiro.setCampo("CODEMP", 11);

financeiro.setCampo("NUMNOTA", 0);

financeiro.setCampo("DTNEG", "04/10/2012");

financeiro.setCampo("CODPARC", 0);

financeiro.setCampo("CODNAT", 3050200);

financeiro.setCampo("CODBCO", 0);

financeiro.setCampo("CODTIPTIT", 2);

financeiro.setCampo("DTVENC", "04/10/2012");

financeiro.setCampo("HISTORICO", "REEMBOLSO DE KM PARA O VEÍCULO " +
 getParam("CODVEICULO"));
```

Quando o **"save"** do registro é acionado, a alteração no Banco de dados é realizada. Portanto aqui estamos incluindo um registro na TGFFIN. Observe:

```
financeiro.save();

Finalmente configuramos uma mensagem para ser exibida após a execução da ação.

mensagem = "Foi gerado o título ";

mensagem += financeiro.getCampo("NUFIN");

mensagem += " no valor de ";

mensagem += financeiro.getCampo("VLRDESDOB")

mensagem += " como reembolso de KM para o veículo ";

mensagem += getParam("CODVEICULO");
```

Crie um parâmetro do tipo Pesquisa apontando para a tabela de veículos, em que você possa determinar para qual veículo será lançado o reembolso.

Assim, ao ser acionada, nossa rotina irá criar um título financeiro com o somatório de todos os lançamentos para o veículo informado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)

### Transação Manual para Ações

Ao cadastrar uma ação do tipo **"Rotina no Banco de Dados"**, **"Rotina Java"** ou **"Script (Java Script)"** é possível marcar a opção **"Controle de transação manual"**. Essa opção vem desmarcada por padrão.

Caso esteja marcada, o controle de transação com o banco de dados deve ser feito no seu respectivo script, de acordo com sua necessidade.

Se estiver desmarcada, o funcionamento continua da mesma forma que antes, ou seja, o sistema automaticamente controla a transação e faz o commit no final da execução do script e o rollback, caso haja erro na execução do script.

É necessário incluir o **"jape.jar"** no buildpath para importar o JapeSession e SessionHandle. A seguir, temos um exemplo de script Java para controlar transação manual:

```
import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;

import br.com.sankhya.extensions.actionbutton.ContextoAcao;

import br.com.sankhya.extensions.actionbutton.QueryExecutor;

import br.com.sankhya.extensions.actionbutton.Registro;

import br.com.sankhya.jape.core.JapeSession;

import br.com.sankhya.jape.core.JapeSession.SessionHandle;

public class TesteBotaoAcaoGustavo implements AcaoRotinaJava {

 public void doAction(final ContextoAcao ctx) throws Exception {

         SessionHandle hnd = null;

         final Registro[] linhas = ctx.getLinhas();

         try {

                 hnd = JapeSession.open();

                 hnd.execWithTX(new JapeSession.TXBlock() {

                         public void doWithTx() throws Exception {

                                 int i = 0;

                                 while (i < linhas.length) {

                                         linhas[i].setCampo("TESTE", 1);

                                         linhas[i].save();

                                         i++;

                                 }

                         }

                 });

                 hnd.execWithTX(new JapeSession.TXBlock() {

                         public void doWithTx() throws Exception {

                                 int i2 = 0;

                                 while (i2 < linhas.length) {

                                         linhas[i2].setCampo("TESTE", 2);

                                         linhas[i2].save();

ctx.mostraErro("Cancelando alterações, os TESTE devem estar 1.");

                                         i2++;

                                 }

                         }

                 });

         } finally {

                 JapeSession.close(hnd);

         }

 }

}
```

O código acima utilizará várias linhas de uma tabela adicional que tem um campo TESTE, e coloca todos os TESTE=1, e depois insere 2, daí cancelamos a segunda transação e os campos TESTE são alterados com sucesso para 1, ou seja, mesmo havendo um erro que fará o rollback na segunda transação, a primeira transação que muda o TESTE para 1 é executada e feito commit com sucesso.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)

### Botões de ação na FAP

Quando houverem um ou mais botões de ações criados na instância **"ProjetoServico"** da tela de Dicionário de Dados a qual a FAP está ligada, os mesmos serão apresentados na FAP por meio do botão **"Outras opções"**. 

O acesso ao botão de Ação, poderá ser feito através do menu Outras opções da FAP.

Na configuração de ações,  há a opção de utilizar o parâmetro **"Ordenar ações por ordem alfabética? - ORDENARACOES"** que quando ativado, ordena a visualização das ações criadas por ele em seu correspondente botão de ações de forma alfabética.

Caso não exista nenhum botão de ação criado para esta instância, o menu Outras opções será apresentado desabilitado na FAP.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas#top)
