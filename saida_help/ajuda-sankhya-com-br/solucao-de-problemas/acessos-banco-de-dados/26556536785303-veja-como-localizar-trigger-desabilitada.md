---
id: "26556536785303"
titulo: "Veja como localizar TRIGGER  desabilitadas em banco  ORACLE  ou SQL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26556536785303-Veja-como-localizar-TRIGGER-desabilitadas-em-banco-ORACLE-ou-SQL"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T14:41:26Z"
rotulos: ["SQL", "Configuração", "Atualização", "Oracle", "Trigger Desabilitada", "Passos para resolver", "Razão do erro", "Detalhe do erro", "localizar TRIGGER  desabilitadas em banco  ORACLE  ou SQL", "Banco de Dados"]
---

# Veja como localizar TRIGGER  desabilitadas em banco  ORACLE  ou SQL

Durante a atualização do sistema ou atuações diretamente no **Banco de dados**, podem  ocorrer situações em que triggers (nativas ou personalizadas) fiquem desabilitadas, impedindo o correto fluxo de atualização dos dados no sistema.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26556536782487)SOLUÇÃO:**

Para localizar essas situações, pode-se utilizar os comandos abaixo para cada **Banco de dados,** através do **DBEXPLORER**:

(1)** COMANDO ORACLE:**

SELECT trigger\_name,
table\_owner,
table\_name,
status
FROM all\_triggers
WHERE status = 'DISABLED'

(1)** COMANDO SQL:**

SELECT
TAB.name as Table\_Name
, TRIG.name as Trigger\_Name
, TRIG.is\_disabled --or objectproperty(object\_id('TriggerName'), 'ExecIsTriggerEnabled')
FROM [sys].[triggers] as TRIG
inner join sys.tables as TAB
on TRIG.parent\_id = TAB.object\_id
where TRIG.is\_disabled = 1
