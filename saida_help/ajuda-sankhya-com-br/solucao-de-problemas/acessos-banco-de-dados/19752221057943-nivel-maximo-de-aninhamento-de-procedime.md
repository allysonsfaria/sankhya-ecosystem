---
id: "19752221057943"
titulo: "Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19752221057943-N%C3%ADvel-m%C3%A1ximo-de-aninhamento-de-procedimento-armazenado-fun%C3%A7%C3%A3o-gatilho-ou-exibi%C3%A7%C3%A3o-excedido-o-limite-%C3%A9-32"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T14:51:32Z"
rotulos: ["SQL Server", "Limite de Aninhamento Excedido (32)", "Recursividade em Triggers e Funções", "Ajuste de Objetos do Banco de Dados", "aninhamento recursividade triggers", "Erro", "Banco de Dados", "Trigger", "Recursividade"]
---

# Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32)

#### 'Artigo criado para apoio ao usuário técnico da empresa'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19752221042327) **MENSAGEM:**

Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19752176534935)SOLUÇÃO:**

Ajustar objetos de banco de dados personalizados a fim de evitar a recursividade nestes

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19752231652375)CAUSA:**

No SQL Server, devemos nos atentar durante o desenvolvimento de objetos quanto a possibilidade de recursividade (loop).

É comum em criação de triggers de UPDATE (exemplo mais clássico), a ocorrência de um comando de UPDATE que irá disparar novamente esta trigger, até que surja uma mensagem de erro:

Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).

Isto ocorre caso o banco de dados esteja com o parâmetro RECURSIVE\_TRIGGERS ativado. Para verificar esta condição, execute o comando:

select name, is\_recursive\_triggers\_on from sys.databases where name = db\_name()

Caso a segunda coluna retorne 1, este parâmetro está ligado. Caso esteja 0, é provável que mais objetos dentro do processo no banco de dados gerem o loop. Neste caso, é recomendado adicionar, então, um teste para verificar qual é o nível de recursão daquela entrada no objeto. Eis a expressão que pode fazer este controle:

IF @@NESTLEVEL > 1

RETURN

Para desativar o parâmetro RECURSIVE\_TRIGGERS, é preciso executar o seguinte comando:

ALTER DATABASE <dbname> SET RECURSIVE\_TRIGGERS OFF

Abaixo um exemplo de loop. Basta retirar o comentário do trecho do @@NESTLEVEL citado acima para ver o comportamento.

ALTER DATABASE <dbname> SET RECURSIVE\_TRIGGERS ON

CREATE TABLE TESTE\_LOOP

(

ID INT IDENTITY(1,1) PRIMARY KEY,

VALOR INT NOT NULL

)

GO

CREATE TRIGGER TRG\_TESTE\_LOOP ON TESTE\_LOOP

FOR UPDATE

AS

BEGIN

/\*  IF @@NESTLEVEL > 1

RETURN\*/

UPDATE TESTE\_LOOP SET TESTE\_LOOP.VALOR = TESTE\_LOOP.VALOR + 1 FROM INSERTED INS WHERE TESTE\_LOOP.ID = INS.ID

END

GO

INSERT INTO TESTE\_LOOP VALUES (1)

GO

UPDATE TESTE\_LOOP SET VALOR = 5 WHERE ID = 3

GO

Mensagem apresentada:

Nível máximo de aninhamento de procedimento armazenado, função, gatilho ou exibição excedido (o limite é 32).

Não se esqueça de desativar o parâmetro ao final do teste:

ALTER DATABASE <dbname> SET RECURSIVE\_TRIGGERS OFF
