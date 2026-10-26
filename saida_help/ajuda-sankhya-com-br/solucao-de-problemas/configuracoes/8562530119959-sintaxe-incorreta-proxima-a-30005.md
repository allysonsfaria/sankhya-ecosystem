---
id: "8562530119959"
titulo: "Sintaxe incorreta próxima a '30005'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8562530119959-Sintaxe-incorreta-pr%C3%B3xima-a-30005"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:11:54Z"
rotulos: ["Configuração", "Triggers", "SQL Server", "não apagar", "#validadoJoaoGomes", "Correção de Sintaxe de Erro em SQL Server", "Erro", "Procedures"]
---

# Sintaxe incorreta próxima a '30005'

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16596792446231) MENSAGEM**:

Sintaxe incorreta próxima a '30005'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16596846727063) SOLUÇÃO:**

Objetos padrão do sistema já utilizam um RAISERROR compatível com as versões recentes do SQL Server, porém em sua base pode existir objetos como triggers e procedures personalizadas que precisam de ajuste.

Para identificar quais objetos estão nesta situação, execute a query abaixo para buscar objetos que tenham o texto com a chamada de erro 30005:

SELECT DISTINCT OBJ.NAME AS OBJETO
,OBJ.XTYPE AS TIPO /\*TR = TRIGGER, P = PROCEDURE, F = FUNCTION\*/
,COM.TEXT AS TEXTO
FROM SYSOBJECTS OBJ
,SYSCOMMENTS COM
WHERE COM.ID = OBJ.ID
AND UPPER(COM.TEXT) LIKE '%30005%'

Onde está assim:
RAISERROR 30005 @ERRMSG

Deverá ficar assim:
RAISERROR (@ERRMSG, 16, 1)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16596792450967)CAUSA:**

Mensagem de erro apresentada pelo fato de haver triggers com o formato de exibição de mensagem de erro que não é mais válido nas versões mais recentes do SQL Server, especialmente a partir do SQL Server 2012.
