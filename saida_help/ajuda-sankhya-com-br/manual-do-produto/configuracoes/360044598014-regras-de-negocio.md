---
id: "360044598014"
titulo: "Regras de Negócio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-30T12:57:26Z"
rotulos: ["manual", "Configuração", "Eventos", "Componentes de BI", "Central de Notas", "Eventos de Liberação", "Liberador", "Portais", "Regras de Negócio", "Stored Procedures", "Tipo de Operação", "Usuário Liberador", "br.com.sankhya.cfg.regranegocio", "Regras de Negócio manual", "Central de Vendas", "Liberação de Limites", "Expressão", "TOP", "Configuração e Execução de Regras de Negócios", "Regra de validação"]
---

# Regras de Negócio

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310663293463) Módulo: Configurações > Avançado
```

---

Trata-se de um mecanismo para exigir liberações para notas, onde as regras sejam flexíveis. Temos aqui uma rotina destinada à operações realizadas exclusivamente nas Centrais; [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) e [Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154). Para que seja possível aplicar regras onde os lançamentos sejam inseridos de forma correta e que atendam aos requisitos específicos para uma regra de negócios, o sistema conta com as seguintes funcionalidades:

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#abageral) |  | [Aba Tipo Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#abatipoopera%C3%A7%C3%A3o) |
| --- | --- | --- |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) |  | [Procedimentos armazenados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#procedimentosarmazenados) |
| [Execução das Regras Dinâmicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#execu%C3%A7%C3%A3odasregrasdin%C3%A2micas) |  | [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#par%C3%A2metrosqueinfluenciamestarotina) |

![Imagem 2: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/6168200580887)

**Num. Regra:** Informe o código da regra a ser criada. Esta numeração pode ser manual ou automática.

**Descrição:** Informe a descrição da regra de forma que possa ser objetiva e de fácil identificação. 

## Aba Geral

**Ativa:** Efetue esta marcação se a regra criada está ativa ou não.

**Tipo de Expressão:** Pode ser Stored Procedure ou Scripts. A opção de Stored Procedure já foi implementada, mas a de Scripts não.

**Onde:** Você deve informar o local onde será aplicada a regra, de acordo com as opções abaixo:

- Portais
- Venda Assistida

**Observação:** apesar de existir esta opção no cadastro, a funcionalidade ainda não foi implementada no Sankhya Om. Caso seja necessário, entre em contato com a Sankhya para negociar a implementação desta funcionalidade.

**Quando:** Informe o momento que será aplicada a regra. Pode ser:

- Confirmação;
- Inclusão/Alteração Itens;
- Inclusão/Alteração Cabeçalho.

**Observação:** quando uma inserção/alteração for realizada manualmente no cabeçalho da nota, ao copiá-las no faturamento, selecione no campo Quando, a opção Confirmação. Assim, não será solicitada nenhuma liberação adicional e os valores referentes à nota serão gerados na confirmação da mesma.

**Observação:** a opção Confirmação não pode ser utilizada quando a opção Venda Assistida estiver selecionada no campo Onde. 

**Evento de Liberação:** Caso a regra deva solicitar uma liberação de limites por alçada, será necessário preencher este campo, podendo ser **"Liberação Comercial"** ou **"Liberação Financeiro"**.

**Importante:** para regras que incluem uma liberação, caso a rotina retorne SUCESSO = N, ou seja, a regra não foi respeitada. Somente os eventos Liberação Financeiro e Liberação Comercial são permitidos aqui. Além disso, e o campo Evento de Liberação for preenchido, na ocasião em que a regra falhar, será inserida uma Solicitação de liberação, e o Item ou Cabeçalho serão gravados normalmente (exceto se a regra for para a confirmação da nota).

Essa solicitação de liberação terá o campo **"Observação"** preenchido com a mensagem tornada pela procedure e, se não for retornada nenhuma mensagem, a observação recebe a descrição da regra para efeito informativo. Se o campo **"Cód. Usuário Liberador"** for informado, será repassado para a solicitação, caso contrário, qualquer pessoa que tenha poder de liberação, poderá fazê-lo. Não há, atualmente, como parametrizar o restante da liberação (como por exemplo, valores outros campos da TSILIB).

Regras que não tem Evento de Liberação vinculado, cancelam a operação, mostrando a mensagem à você, ou seja, nesse caso, o Cabeçalho ou o Item não serão gravados.

**Cód. Usuário Liberador:** Deverá ser informado somente quando o Evento de Liberação tiver informado. Se não for informado na regra, ao solicitar a liberação de limites, o sistema solicitará que o usuário tenha alçada configurada em seu Cadastro de Usuário, Limites para Liberação. Parâmetro usado em regras que incluem solicitação de liberação. Há duas formas de se definir o usuário liberador, a primeira é através deste campo. A segunda, é informando o parâmetro P\_CODUSULIB dentro da própria Stored Procedure; se existir conflito, vale a definição realizada na Stored Procedure.

**Expressão:** Aqui, deve ser informado somente o nome da Stored Procedure que deve ser executada pela regra.

**Nota:** quando a opção de Script for implementada, conterá a própria rotina, por isso o campo tem um tamanho maior.

**Inibe alteração do liberador:** Caso esta marcação esteja realizada, somente a regra de negócios pode alterar o liberador, ficando esta escolha proibida ao usuário. Além disso, é importante que o mecanismo sempre determine um liberador, caso contrário, será permitido a qualquer pessoa escolher o liberador apenas uma vez, pois, na verificação das próximas alterações, não será possível determinar se quem escolheu o liberador foi o usuário ou o mecanismo de regra de negócios.

Quando duas regras vinculam o mesmo evento de liberação, acontece o seguinte:

Se a primeira regra falhar, uma solicitação de liberação será incluída. As demais regras não resultarão em novas solicitações, pois já existe uma liberação pendente. Esse comportamento está previsto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#top)

## Aba Tipo Operação

## Imagem 3: Aba Tipo Operação

A aba Tipo de Operação é uma opção que permite configurar as TOP's que serão consideradas para aplicar as regras de negócios configuradas. Essas TOP's devem ser criadas previamente em [Cadastro de Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

**Tipo de Operação:** Informe o Tipo de Operação que deverá ter considerada a regra configurada.

**Seq. de execução:** Serve para informar a sequência que o sistema deverá seguir para quando houver para a mesma top várias regras.

**Nota:** no Cadastro de Tipos de Operação - TOP existe a aba Regras de negócio, para que você possa visualizar e verificar as regras que estão vinculadas à esta, como também, a sua sequência. Outra possibilidade, é permitir incluir/excluir regras como também a sua sequência.

![Imagem 4: A Regra de Negócios não contempla a funcionalidade disponibilizada pela Liberação em Cascata , uma vez que este recurso…](https://ajuda.sankhya.com.br/hc/article_attachments/16746112233751) A Regra de Negócios não contempla a funcionalidade disponibilizada pela [Liberação em Cascata](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaliberaoemcascata), uma vez que este recurso permite trabalhar com um usuário liberador diretamente pela procedure (podendo nesta, existir mais de um usuário). Além disso, no cadastro da Regra de Negócio, pode-se também informar um Usuário Liberador.

Acesse também o help da [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#top)

## Botão Outras Opções...

![Imagem 5: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/6169292634647)

Através do botão Outras Opções..., opção **"Eventos"**, criam-se novos eventos de liberação de limite.

Para utilização destes novos eventos, são necessários os seguintes passos:

O parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** deve estar habilitado, pois estes eventos novos como também os já existentes, precisam que este esteja habilitado para abrir a tela de Liberação de Limites.

Ao clicar na opção Eventos, o pop-up Eventos p/ liberação de Regras de negócio será exibido. Observe:

![Imagem 6: Ao clicar na opção Eventos , o pop-up Eventos p/ liberação de Regras de negócio será exibido. Observe:](https://ajuda.sankhya.com.br/hc/article_attachments/6169579174551)

**Evento:** É o código do Evento. Pode ter numeração automática ou manual.

**Importante:** a numeração está condicionada a iniciar sua numeração a partir de 1000, ou seja, os respectivos eventos abaixo disso são os já padronizados do sistema, e este validará se você informar uma numeração menor que 1000.

**Descrição:** É a descrição de identificação do evento novo a ser criado, ficando à seu critério. É possível configurar um evento até 60 caracteres.

As outras funcionalidades da tela já são padrão do sistema, Exportar Registros, Exportar para Excel, PDF e Visualizar o Cubo de Decisão, como também, o Painel de Controle.

Acesse maiores detalhes no help [Conhecendo o Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934).

Após a criação dos eventos, estes deverão ser vinculados na aba Geral da Regra de Negócio, conforme demonstramos abaixo:

[GIF animado: Imagem 7: Após a criação dos eventos, estes deverão ser vinculados na aba Geral da Regra de Negócio , conforme demonstramos…](https://ajuda.sankhya.com.br/hc/article_attachments/6169658672919)

No [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para Liberação"**:

O usuário que tiver alçada para liberação do evento novo criado, obrigatoriamente deverá ser configurado nesta opção, da mesma forma que os eventos padrões do sistema.

Na tela de Liberação de Limites da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414):

Lançado um Pedido de Venda, cuja TOP foi configurada na Regra de Negócios, tanto para alteração/inclusão de itens, como confirmação do cabeçalho da nota.

A liberação destes eventos pode ser feitas através:

- Do sistema, na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites);
- Do e-mail;
- Via Android:

Exemplo abaixo efetuado em um celular Samsung Galaxy S3, Android versão 4.2.1:

![Imagem 8: Exemplo abaixo efetuado em um celular Samsung Galaxy S3 , Android versão 4.2.1 :](https://ajuda.sankhya.com.br/hc/article_attachments/6169753018647)

![Imagem 9: Exemplo abaixo efetuado em um celular Samsung Galaxy S3 , Android versão 4.2.1 :](https://ajuda.sankhya.com.br/hc/article_attachments/6169804115095)

Da grade [Resultado da seleção (Portal de Vendas)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Validar os Pedidos Selecionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#validarospedidosselecionados).

**Nota:** para esta opção, também poderá ter liberações das regras de negócios vinculados a eventos criados neste menu.

## Procedimentos armazenados

Para o sistema identificar as regras e como tratá-las, é necessário criar, inicialmente, as Stored Procedures (rotina utilizada no Banco de Dados e criada neste).

Importante salientar que, a Stored Procedure, por regra, deve ter os parâmetros de entrada(P\_NUNOTA INT, P\_SUCESSO OUT VARCHAR, P\_MENSAGEM OUT VARCHAR2, P\_CODUSULIB OUT NUMBER);

Como exemplo, peguemos uma base de dados Oracle e SQL Server:

**1) Modelo da Stored Procedure para o cabeçalho:**

- Oracle:

```
CREATE OR REPLACE PROCEDURE STP_INC_CAB_NOTA (
          P_NUNOTA NUMBER,
          P_SUCESSO OUT VARCHAR,
          P_MENSAGEM OUT VARCHAR2,
          P_CODUSULIB OUT NUMBER)
AS
BEGIN

--AQUI SERIA A EXECUÇÃO DA ROTINA

P_SUCESSO := 'N';
P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
--SE FOR NECESSÁRIO DETERMINAR O LIBERADOR BASTA ATRIBUIR:
P_CODUSULIB := 10;

END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE STP_INC_CAB_NOTA (
          @P_NUNOTA INT,
          @P_SUCESSO VARCHAR OUTPUT,
          @P_MENSAGEM VARCHAR OUTPUT,
          @P_CODUSULIB INT OUTPUT)
AS
BEGIN

--AQUI SERIA A EXECUÇÃO DA ROTINA

P_SUCESSO := 'N'
P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.'
--SE FOR NECESSÁRIO DETERMINAR O LIBERADOR BASTA ATRIBUIR:
P_CODUSULIB := 10

END
GO
```

Exemplo da criação de uma Stored Procedure utilizando o Modelo:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Cab_Nota (
         P_NUNOTA NUMBER,
         P_SUCESSO OUT VARCHAR,
         P_MENSAGEM OUT VARCHAR2,
         P_CODUSULIB OUT NUMBER)
AS
         P_COUNT NUMBER := 0;
BEGIN
         P_SUCESSO := 'S';

        SELECT COUNT(1) INTO P_COUNT
        FROM TGFCAB CAB
        WHERE CAB.NUNOTA = P_NUNOTA
        AND CAB.CODCENCUS IN (10200, 10300);

       IF P_COUNT = 0 THEN
         P_SUCESSO := 'N';
         P_MENSAGEM := 'PARA ESTA INSERÇÃO É NECESSÁRIO INSERIR O CR 10200 OU 10300.';
       END IF;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE Stp_Inc_Cab_Nota(
          @P_NUNOTA INT,
          @P_SUCESSO VARCHAR OUTPUT,
          @P_MENSAGEM VARCHAR OUTPUT,
          @P_CODUSULIB INT OUTPUT)
AS
BEGIN

          DECLARE @P_COUNT INT;

          SET @P_SUCESSO = 'S';

          SELECT @P_COUNT = COUNT(1)
          FROM TGFCAB CAB
          WHERE CAB.NUNOTA = @P_NUNOTA
          AND CAB.CODCENCUS IN (10200, 10300);

   IF @P_COUNT = 0
   BEGIN

     SET @P_SUCESSO = 'N';
     SET @P_MENSAGEM = 'PARA ESTA INSERÇÃO É NECESSÁRIO INSERIR O CR 10200 OU 10300.';
   END
END;
GO
```

**2)Modelo da Stored Procedure para o item:**

- Oracle:

```
CREATE OR REPLACE PROCEDURE Ad_Stp_Inc_Item_Nota(
        P_NUNOTA NUMBER,
        P_SEQUENCIA NUMBER,
        P_SUCESSO OUT VARCHAR,
        P_MENSAGEM OUT VARCHAR2,
        P_CODUSULIB OUT NUMBER)
AS
        P_COUNT NUMBER := 0;
BEGIN
        SELECT COUNT(1) INTO P_COUNT
        FROM TGFITE ITE
        WHERE ITE.NUNOTA = P_NUNOTA
        AND ITE.SEQUENCIA = P_SEQUENCIA
        AND ITE.QTDNEG >= 10;

        IF P_COUNT = 0 THEN
                 P_SUCESSO := 'N';
                 P_MENSAGEM := 'A QTDNEG só pode ser acima de 10';
                 P_CODUSULIB := 0;
        ELSE
                 P_SUCESSO := 'S';
        END IF;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE Ad_Stp_Inc_Item_Nota(
       @P_NUNOTA INT,
       @P_SEQUENCIA INT,
       @P_SUCESSO VARCHAR OUTPUT,
       @P_MENSAGEM VARCHAR OUTPUT,
       @P_CODUSULIB INT OUTPUT)
AS
BEGIN
       DECLARE @P_COUNT INT;

       SELECT @P_COUNT = COUNT(1)
       FROM TGFITE ITE
       WHERE ITE.NUNOTA = @P_NUNOTA
       AND ITE.SEQUENCIA = @P_SEQUENCIA
       AND ITE.QTDNEG >= 10;

       IF @P_COUNT = 0
       BEGIN
                 SET @P_SUCESSO = 'N';
                 SET @P_MENSAGEM = 'A QTDNEG só pode ser acima de 10';
                 SET @P_CODUSULIB = 0;
       END
       ELSE
       BEGIN
                 SET @P_SUCESSO = 'S';
       END
END;
GO
```

Na tela de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites), é possível a vinculação deste evento juntamente a um Componente de BI. Para isso, acesse o botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites#botooutrasopes...):

![Imagem 10: Na tela de Liberação de Limites , é possível a vinculação deste evento juntamente a um Componente de BI . Para isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/6170272292247)

Ao clicar nesta opção abrirá a tela:

![Imagem 11: Ao clicar nesta opção abrirá a tela:](https://ajuda.sankhya.com.br/hc/article_attachments/6170342743319)

Ao clicar em **"Novo"** será aberta a tela para ser informado o Evento e o Componente de BI.

Clique em Salvar, e será habilitada a opção de Análises, podendo gerar o Componente de BI para a liberação em questão.

Caso o vínculo não esteja correto, você pode utilizar a opção de **"Remover Selecionado"**.

Se o vínculo estiver correto, habilitará a opção de Análises e poderá ser gerado o Componente de BI selecionado para o evento.

#### Criação de Usuário Liberador na Stored Procedure

Existe a possibilidade de criar o Usuário Liberador na Stored Procedure. O sistema olhará primeiro se existe algum Usuário Liberador na Stored Procedure, caso haja, este será utilizado na solicitação de liberação. Caso não tenha, será analisado dentro do cadastro da regra de negócios. Se na regra de negócios não tiver um Usuário Liberador informado, o sistema buscará usuário que tenha configurado no botão de Limites para Liberação do Cadastro do Usuário.

- **Regras:**

Quando efetuar a solicitação de liberação de limites, o valor da liberação será em conformidade ao que foi solicitado liberar, ou seja, se for uma solicitação da liberação do item, virá o valor total do item que foi alterado, caso seja da nota, virá o valor total da nota.

Para eventos que serão solicitados no Cabeçalho da Nota, a Stored Procedure terá um novo argumento P\_CODUSULIB:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Cab_Nota (
          P_NUNOTA NUMBER,
          P_SUCESSO OUT VARCHAR,
          P_MENSAGEM OUT VARCHAR2,
          P_CODUSULIB OUT NUMBER)
AS
BEGIN
-- AQUI SERIA A EXECUÇÃO DA ROTINA

P_SUCESSO := 'N';
P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
P_CODUSULIB := 0;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE Stp_Inc_Cab_Nota(
         @P_NUNOTA INT,
         @P_SUCESSO VARCHAR OUTPUT,
         @P_MENSAGEM VARCHAR OUTPUT,
         @P_CODUSULIB INT OUTPUT)
AS
BEGIN

         -- AQUI SERIA A EXECUÇÃO DA ROTINA

         SET @P_SUCESSO = 'N';
         SET @P_MENSAGEM = 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
         SET @P_CODUSULIB = 0;
END;
GO
```

Este mesmo argumento poderá ser utilizado também para os itens da nota:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Item_Nota(
       P_NUNOTA NUMBER,
       P_SEQUENCIA NUMBER,
       P_SUCESSO OUT VARCHAR,
       P_MENSAGEM OUT VARCHAR2,
       P_CODUSULIB OUT NUMBER)
AS
BEGIN
       -- AQUI SERIA A EXECUÇÃO DA ROTINA

       P_SUCESSO := 'N';
       P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
       P_CODUSULIB := 0;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE Stp_Inc_Item_Nota(
       @P_NUNOTA INT,
    @P_SEQUENCIA INT,
    @P_SUCESSO VARCHAR OUTPUT,
    @P_MENSAGEM VARCHAR OUTPUT,
    @P_CODUSULIB INT OUTPUT)
AS
BEGIN
       -- AQUI SERIA A EXECUÇÃO DA ROTINA

       SET @P_SUCESSO = 'N';
       SET @P_MENSAGEM = N'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
       SET @P_CODUSULIB = 0;
END;
GO
```

**Importante:** o código do usuário deve ser informado nesta variável P\_CODUSULIB;

Exemplo 01:

Regra não possui usuário, mas a Stored Procedure possui; neste caso, virá para a tela de solicitação de liberação, o usuário que está configurado na Stored Procedure.

Procedimento armazenado:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Cab_Nota(
        P_NUNOTA NUMBER,
        P_SUCESSO OUT VARCHAR,
        P_MENSAGEM OUT VARCHAR2,
        P_CODUSULIB OUT NUMBER)
AS
BEGIN

        -- AQUI SERIA A EXECUÇÃO DA ROTINA

        P_SUCESSO := 'N';
        P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
        P_CODUSULIB := 286;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE Stp_Inc_Cab_Nota(
       @P_NUNOTA INT,
       @P_SUCESSOOUT VARCHAR OUTPUT,
       @P_MENSAGEM VARCHAR OUTPUT,
       @P_CODUSULIB INT OUTPUT)
AS
BEGIN

       -- AQUI SERIA A EXECUÇÃO DA ROTINA

       SET @P_SUCESSOOUT = 'N';
       SET @P_MENSAGEM = 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
       SET @P_CODUSULIB = 286;
END;
GO
```

Na tela Regras de Negócio não foi informado um usuário liberador e a solicitação de liberação de limites será na confirmação da nota e com o evento de liberação 62 – Liberação Comercial.

Lançada a nota de venda e ao confirmar a nota, o sistema solicitou a liberação de limites do evento 62 – Liberação Comercial e trouxe automaticamente o Usuário Liberador em conformidade ao que está configurado na Stored Procedure.

Se tentar alterar o usuário, o sistema emite a mensagem:

**"Não é possível alterar o liberador quando a solicitação foi lançada por regra dinâmica".**

Exemplo 02:

Regra possui usuário e a Stored Procedure também possui; neste caso, virá para a tela de solicitação de liberação, o usuário que está configurado na Stored Procedure.

A Regra possui Usuário Liberador informado e na Stored Procedure também:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Cab_Nota(
         P_NUNOTA NUMBER,
         P_SUCESSO OUT VARCHAR,
         P_MENSAGEM OUT VARCHAR2,
         P_CODUSULIB OUT NUMBER)
AS
BEGIN

         -- AQUI SERIA A EXECUÇÃO DA ROTINA

         P_SUCESSO := 'N';
         P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
         P_CODUSULIB := 286;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE dbo.Stp_Inc_Cab_Nota(
         @P_NUNOTA INT,
         @P_SUCESSO VARCHAR OUTPUT,
         @P_MENSAGEM VARCHAR OUTPUT,
         @P_CODUSULIB INT OUTPUT)
AS
BEGIN

         -- AQUI SERIA A EXECUÇÃO DA ROTINA

         SET @P_SUCESSO = 'N';
         SET @P_MENSAGEM = 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
         SET @P_CODUSULIB = 286;
END;
```

No Portal de Vendas será trazido como liberador, o usuário configurado na Stored Procedure.

Exemplo 03:

Regra não possui usuário e a Stored Procedure também não possui; neste caso, virá para a tela de solicitação de liberação, o usuário zero para buscar o usuário que possui alçada para o evento.

Procedimento armazenado:

- Oracle:

```
CREATE OR REPLACE PROCEDURE Stp_Inc_Cab_Nota(
         P_NUNOTA NUMBER,
         P_SUCESSO OUT VARCHAR,
         P_MENSAGEM OUT VARCHAR2,
         P_CODUSULIB OUT NUMBER)
AS
BEGIN

         -- AQUI SERIA A EXECUÇÃO DA ROTINA

         P_SUCESSO := 'N';
         P_MENSAGEM := 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
         P_CODUSULIB := 0;
END;
/
```

- SQL Server:

```
CREATE OR ALTER PROCEDURE dbo.Stp_Inc_Cab_Nota(
        @P_NUNOTA INT,
        @P_SUCESSO VARCHAR OUTPUT,
        @P_MENSAGEM VARCHAR OUTPUT,
        @P_CODUSULIB INT OUTPUT)
AS
BEGIN

        -- AQUI SERIA A EXECUÇÃO DA ROTINA

        SET @P_SUCESSO = 'N';
        SET @P_MENSAGEM = 'A REGRA FALHOU DE PROPÓSITO, SÓ PARA TESTAR.';
        SET @P_CODUSULIB = 0;
END;
GO
```

No Portal de Vendas, virá como Usuário Liberador o usuário zero, para que seja informado o usuário liberador que possui alçada para este evento.

## Execução das Regras Dinâmicas

Caso a empresa opte por trabalhar com Regras de Negócio Dinâmicas (personalizadas), deve-se atentar para a criação/remoção dos eventos de liberação que, nesta situação, ficam sob a responsabilidade da própria regra. Aconselhamos que estas regras sejam criadas com o acompanhamento de um Consultor Sankhya. Na imagem abaixo temos um fluxo de execução das regras dinâmicas:

![Imagem 12: Caso a empresa opte por trabalhar com Regras de Negócio Dinâmicas (personalizadas), deve-se atentar para a…](https://ajuda.sankhya.com.br/hc/article_attachments/6175031927959)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#top)

## Parâmetros que influenciam esta rotina

Habilitando o parâmetro **"Validar regras de negócios de itens no faturamento? - VALREGNEGFAT"**, ao criar uma Regra de Negócios com validação pela inclusão/alteração dos itens na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), caso o pedido tenha se originado de um faturamento e não ocorra nenhuma alteração neste item, será exibido um aviso de que a regra X não permitiu tal operação.

Com o parâmetro **"Validar regras negócios cabeçalho no faturamento? - VALREGNEGFATCAB"** ligado, ao faturar um documento ou gerar uma remessa, serão utilizadas na confirmação, as regras personalizadas que estiverem com a opção **"Inclusão/Alteração Cabeçalho"** configurada no campo **"Quando"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#abageral).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014-Regras-de-Neg%C3%B3cio#top)
