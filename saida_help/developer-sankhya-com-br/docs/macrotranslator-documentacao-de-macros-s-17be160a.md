---
id: "https://developer.sankhya.com.br/docs/macrotranslator-documentação-de-macros-sankhya"
titulo: "🔄 MacroTranslator: Documentação de Macros Sankhya"
url: "https://developer.sankhya.com.br/docs/macrotranslator-documentação-de-macros-sankhya"
atualizado_em: "2026-02-24T18:48:54.000Z"
---

# 🔄 MacroTranslator: Documentação de Macros Sankhya

<br />

# 🔄 MacroTranslator: Documentação de Macros Sankhya

Esta documentação descreve todas as macros suportadas pelo framework de persistência da Sankhya, explicando propósito,
sintaxe, diferenças entre Oracle e MSSQL, e exemplos práticos.

***

## 🤔 Por que usar macros?

O uso do Macros Sankhya traz diversas vantagens, especialmente quando se busca portabilidade e manutenção de consultas SQL entre Oracle e MSSQL:

* ✅ **Unificação de Sintaxe:** Permite escrever consultas SQL de forma unificada, abstraindo diferenças de sintaxe e funções entre Oracle e MSSQL. Isso reduz a necessidade de duplicar código ou criar ramificações específicas para cada banco.
* ✅ **Redução de Erros:** Ao centralizar as diferenças em macros bem definidas, diminui-se o risco de erros causados por adaptações manuais ou esquecimentos de detalhes específicos da sintaxe de cada banco.
* ✅ **Facilidade de Manutenção:** Alterações em regras de negócio ou ajustes de queries podem ser feitas em um único ponto, sem a necessidade de revisar múltiplas versões da mesma consulta.
* ✅ **Melhoria na Legibilidade:** As macros tornam as consultas mais legíveis e expressivas, permitindo que o foco esteja na lógica de negócio em vez de detalhes técnicos de cada banco.

## Índice

* [ignorecase](#ignorecase)
* [normalizeText](#normalizetext)
* [nullValue](#nullvalue)
* [convertToNumber](#converttonumber)
* [maxLines](#maxlines)
* [yearMonth](#yearmonth)
* [dbDate](#dbdate)
* [stringIndex](#stringindex)
* [trim](#trim)
* [length](#length)
* [diffdays](#diffdays)
* [diffhour](#diffhour)
* [concatstr](#concatstr)
* [quebraLinha](#quebralinha)
* [convertPtBrDate](#convertptbrdate)
* [onlydate](#onlydate)
* [truncWeek](#truncweek)
* [truncMonth](#truncmonth)
* [truncQarter](#truncqarter)
* [truncYear](#truncyear)
* [truncDate](#truncdate)
* [convertToFloat](#converttofloat)
* [convertToVarchar](#converttovarchar)
* [user.name](#username)
* [sqldatabase](#sqldatabase)
* [leftPad](#leftpad)
* [subString](#substring)
* [upperText](#uppertext)
* [getMonth](#getmonth)
* [getYear](#getyear)
* [getDay](#getday)
* [monYear](#monyear)
* [addMonths](#addmonths)
* [endOfCurrentMonth](#endofcurrentmonth)
* [convertToTimestamp](#converttotimestamp)
* [convertToMilliseconds](#converttomilliseconds)

***

## ignorecase

**Propósito:** Normaliza texto para comparação sem considerar maiúsculas/minúsculas e acentuação.

**Sintaxe:**

```sql
ignorecase(<expressão>)
```

**Oracle:**

```sql
TRANSLATE(UPPER(<expressão>),'ÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÇ','AEIOUAOAEIOUAEIOUC')
```

**MSSQL:**

```sql
REPLACE(UPPER(<expressão>),'ÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÇ','AEIOUAOAEIOUAEIOUC')
```

**Exemplo:**

```sql
ignorecase(NOME)
```

**Exemplo de consulta:**

```sql
SELECT * FROM CLIENTES WHERE ignorecase(NOME) = ignorecase('José');
```

***

## normalizeText

**Propósito:** Remove acentuação e normaliza texto para comparação.

**Sintaxe:**

```sql
normalizeText(<expressão>)
```

**Oracle:**

```sql
CONVERT(UPPER(<expressão>), 'US7ASCII')
```

**MSSQL:**

```sql
REPLACE(UPPER(<expressão>),'ÁÉÍÓÚÃÕÂÊÎÔÛÀÈÌÒÙÇ','AEIOUAOAEIOUAEIOUC')
```

**Exemplo:**

```sql
normalizeText(NOME)
```

**Exemplo de consulta:**

```sql
SELECT * FROM CLIENTES WHERE normalizeText(NOME) LIKE normalizeText('%silva%');
```

***

## nullValue

**Propósito:** Substitui valores nulos por um valor padrão.

**Sintaxe:**

```sql
nullValue(<expressão>, <valor padrão>)
```

**Oracle:**

```sql
NVL(<expressão>, <valor padrão>)
```

**MSSQL:**

```sql
ISNULL(<expressão>, <valor padrão>)
```

**Exemplo:**

```sql
nullValue(SALARIO, 0)
```

**Exemplo de consulta:**

```sql
SELECT nullValue(SALARIO, 0) AS SALARIO_CORRIGIDO FROM FUNCIONARIOS;
```

***

## convertToNumber

**Propósito:** Converte expressão para número.

**Sintaxe:**

```sql
convertToNumber(<expressão>)
```

**Oracle:**

```sql
TO_NUMBER(<expressão>)
```

**MSSQL:**

```sql
CONVERT(NUMERIC, <expressão>)
```

**Exemplo:**

```sql
convertToNumber(VALOR)
```

**Exemplo de consulta:**

```sql
SELECT convertToNumber(PRECO) FROM PRODUTOS WHERE convertToNumber(PRECO) > 100;
```

***

## maxLines

**Propósito:** Limita o número de linhas retornadas.

**Sintaxe:**

```sql
maxLines(<quantidade>)
```

**Oracle:**

```sql
AND ROWNUM <= <quantidade>
```

**MSSQL:**

```sql
TOP <quantidade>
```

**Exemplo:**

```sql
maxLines(10)
```

**Exemplo de consulta:**

```sql
SELECT maxLines(10) * FROM VENDAS ORDER BY DATA DESC;
```

***

## yearMonth

**Propósito:** Retorna o ano e mês de uma data no formato YYYYMM.

**Sintaxe:**

```sql
yearMonth(<campo>)
```

**Oracle:**

```sql
(TO_NUMBER(TO_CHAR(<campo>,'YYYYMM')))
```

**MSSQL:**

```sql
(YEAR(<campo>) * 100) + MONTH(<campo>)
```

**Exemplo:**

```sql
yearMonth(DATA)
```

**Exemplo de consulta:**

```sql
SELECT yearMonth(DATA_VENDA) AS ANO_MES FROM VENDAS;
```

***

## dbDate

**Propósito:** Retorna a data atual do banco.

**Sintaxe:**

```sql
dbDate()
```

**Oracle:**

```sql
SYSDATE
```

**MSSQL:**

```sql
GETDATE()
```

**Exemplo:**

```sql
dbDate()
```

**Exemplo de consulta:**

```sql
SELECT dbDate() AS DATA_ATUAL;
```

***

## stringIndex

**Propósito:** Retorna a posição de uma substring dentro de uma string.

**Sintaxe:**

```sql
stringIndex(<src>, <trg>)
```

**Oracle:**

```sql
INSTR(<src>, <trg>)
```

**MSSQL:**

```sql
CHARINDEX(<trg>, <src>)
```

**Exemplo:**

```sql
stringIndex('abcde', 'cd')
```

**Exemplo de consulta:**

```sql
SELECT stringIndex(NOME, 'A') AS POSICAO FROM CLIENTES;
```

***

## trim

**Propósito:** Remove espaços em branco das extremidades.

**Sintaxe:**

```sql
trim(<expressão>)
```

**Oracle:**

```sql
TRIM(<expressão>)
```

**MSSQL:**

```sql
LTRIM(RTRIM(<expressão>))
```

**Exemplo:**

```sql
trim(NOME)
```

**Exemplo de consulta:**

```sql
SELECT trim(NOME) FROM CLIENTES;
```

***

## length

**Propósito:** Retorna o tamanho de uma string.

**Sintaxe:**

```sql
length(<expressão>)
```

**Oracle:**

```sql
LENGTH(<expressão>)
```

**MSSQL:**

```sql
DATALENGTH(<expressão>)
```

**Exemplo:**

```sql
length(NOME)
```

**Exemplo de consulta:**

```sql
SELECT length(NOME) AS TAMANHO FROM CLIENTES;
```

***

## diffdays

**Propósito:** Calcula a diferença em dias entre duas datas.

**Sintaxe:**

```sql
diffdays(<data1>, <data2>)
```

**Oracle:**

```sql
TRUNC(<data1> - <data2>)
```

**MSSQL:**

```sql
DATEDIFF(DAY, <data2>, <data1>)
```

**Exemplo:**

```sql
diffdays(DATA_FIM, DATA_INICIO)
```

**Exemplo de consulta:**

```sql
SELECT diffdays(DATA_FIM, DATA_INICIO) AS DIAS FROM PROJETOS;
```

***

## diffhour

**Propósito:** Calcula a diferença em horas entre duas datas.

**Sintaxe:**

```sql
diffhour(<data1>, <data2>)
```

**Oracle:**

```sql
((<data1> - <data2>) * 24)
```

**MSSQL:**

```sql
DATEDIFF(HOUR, <data2>, <data1>)
```

**Exemplo:**

```sql
diffhour(DATA_FIM, DATA_INICIO)
```

**Exemplo de consulta:**

```sql
SELECT diffhour(DATA_FIM, DATA_INICIO) AS HORAS FROM TAREFAS;
```

***

## concatstr

**Propósito:** Concatena duas strings.

**Sintaxe:**

```sql
concatstr(<str1>, <str2>)
```

**Oracle:**

```sql
<str1> || <str2>
```

**MSSQL:**

```sql
<str1> + <str2>
```

**Exemplo:**

```sql
concatstr('A', 'B')
```

**Exemplo de consulta:**

```sql
SELECT concatstr(NOME, SOBRENOME) AS NOME_COMPLETO FROM CLIENTES;
```

***

## quebraLinha

**Propósito:** Insere uma quebra de linha.

**Sintaxe:**

```sql
quebraLinha()
```

**Oracle:**

```sql
CHR(13)||CHR(10)
```

**MSSQL:**

```sql
CHAR(13)+CHAR(10)
```

**Exemplo:**

```sql
quebraLinha()
```

**Exemplo de consulta:**

```sql
SELECT NOME || quebraLinha() || ENDERECO AS DADOS FROM CLIENTES;
```

***

## convertPtBrDate

**Propósito:** Converte data para formato brasileiro (DD/MM/YYYY).

**Sintaxe:**

```sql
convertPtBrDate(<data>)
```

**Oracle:**

```sql
TO_CHAR(<data>, 'DD/MM/YYYY')
```

**MSSQL:**

```sql
CONVERT(VARCHAR, <data>, 103)
```

**Exemplo:**

```sql
convertPtBrDate(DATA)
```

**Exemplo de consulta:**

```sql
SELECT convertPtBrDate(DATA_NASCIMENTO) AS DATA_BR FROM CLIENTES;
```

***

## onlydate

**Propósito:** Retorna apenas a parte da data (sem hora).

**Sintaxe:**

```sql
onlydate(<data>)
```

**Oracle:**

```sql
TRUNC(<data>)
```

**MSSQL:**

```sql
DATEADD(DAY, DATEDIFF(DAY, 0, <data>), 0)
```

**Exemplo:**

```sql
onlydate(DATA)
```

**Exemplo de consulta:**

```sql
SELECT onlydate(DATA_VENDA) AS DATA_SEM_HORA FROM VENDAS;
```

***

## truncWeek

**Propósito:** Retorna o início da semana da data.

**Sintaxe:**

```sql
truncWeek(<data>)
```

**Oracle:**

```sql
TRUNC(<data>, 'IW')
```

**MSSQL:**

```sql
CONVERT(DATE, DATEADD(DAY, -1, DATEADD(WK, DATEDIFF(WK, 0, <data> ), 0)), 103)
```

**Exemplo:**

```sql
truncWeek(DATA)
```

**Exemplo de consulta:**

```sql
SELECT truncWeek(DATA) AS INICIO_SEMANA FROM CALENDARIO;
```

***

## truncMonth

**Propósito:** Retorna o início do mês da data.

**Sintaxe:**

```sql
truncMonth(<data>)
```

**Oracle:**

```sql
TRUNC(<data>, 'MM')
```

**MSSQL:**

```sql
CONVERT(DATE, DATEADD(DAY, (DATEPART(DAY, <data>) * -1) + 1, <data>), 103)
```

**Exemplo:**

```sql
truncMonth(DATA)
```

**Exemplo de consulta:**

```sql
SELECT truncMonth(DATA) AS INICIO_MES FROM CALENDARIO;
```

***

## truncQarter

**Propósito:** Retorna o início do trimestre da data.

**Sintaxe:**

```sql
truncQarter(<data>)
```

**Oracle:**

```sql
TRUNC(<data>, 'Q')
```

**MSSQL:**

```sql
CONVERT(DATE, DATEADD(QQ, DATEDIFF(QQ, 0, <data>), 0), 103)
```

**Exemplo:**

```sql
truncQarter(DATA)
```

**Exemplo de consulta:**

```sql
SELECT truncQarter(DATA) AS INICIO_TRIMESTRE FROM CALENDARIO;
```

***

## truncYear

**Propósito:** Retorna o início do ano da data.

**Sintaxe:**

```sql
truncYear(<data>)
```

**Oracle:**

```sql
TRUNC(<data>, 'YY')
```

**MSSQL:**

```sql
CONVERT(DATE, DATEADD(YY, DATEDIFF(YY, 0, <data>), 0), 103)
```

**Exemplo:**

```sql
truncYear(DATA)
```

**Exemplo de consulta:**

```sql
SELECT truncYear(DATA) AS INICIO_ANO FROM CALENDARIO;
```

***

## truncDate

**Propósito:** Retorna apenas a parte da data (sem hora).

**Sintaxe:**

```sql
truncDate(<data>)
```

**Oracle:**

```sql
TRUNC(<data>)
```

**MSSQL:**

```sql
CONVERT(date, <data>)
```

**Exemplo:**

```sql
truncDate(DATA)
```

**Exemplo de consulta:**

```sql
SELECT truncDate(DATA) AS DATA_SEM_HORA FROM CALENDARIO;
```

***

## convertToFloat

**Propósito:** Converte expressão para float.

**Sintaxe:**

```sql
convertToFloat(<expressão>)
```

**Oracle:**

```sql
<expressão>
```

**MSSQL:**

```sql
CONVERT(FLOAT, <expressão>)
```

**Exemplo:**

```sql
convertToFloat(VALOR)
```

**Exemplo de consulta:**

```sql
SELECT convertToFloat(PRECO) FROM PRODUTOS;
```

***

## convertToVarchar

**Propósito:** Converte expressão para varchar.

**Sintaxe:**

```sql
convertToVarchar(<expressão>)
```

**Oracle:**

```sql
TO_CHAR(<expressão>)
```

**MSSQL:**

```sql
CONVERT(VARCHAR, <expressão>)
```

**Exemplo:**

```sql
convertToVarchar(VALOR)
```

**Exemplo de consulta:**

```sql
SELECT convertToVarchar(CODIGO) FROM PRODUTOS;
```

***

## user.name

**Propósito:** Insere o nome do usuário/banco.

**Sintaxe:**

```sql
${user.name}
```

**Oracle:**

```sql
<usuário>
```

**MSSQL:**

```sql
<usuário>.
```

**Exemplo:**

```sql
SELECT * FROM ${user.name}TABELA
```

**Exemplo de consulta:**

```sql
SELECT * FROM ${user.name}CLIENTES;
```

***

## sqldatabase

**Propósito:** Insere o nome do banco.

**Sintaxe:**

```sql
sqldatabase.<tabela>
```

**Oracle:**

```sql
<tabela>
```

**MSSQL:**

```sql
<usuário>.<tabela>
```

**Exemplo:**

```sql
SELECT * FROM sqldatabase.TABELA
```

**Exemplo de consulta:**

```sql
SELECT * FROM sqldatabase.CLIENTES;
```

***

## leftPad

**Propósito:** Preenche à esquerda até o tamanho desejado.

**Sintaxe:**

```sql
leftPad(<coluna>, <caractere>, <tamanho>)
```

**Oracle:**

```sql
LPAD(<coluna>, <tamanho>, <caractere>)
```

**MSSQL:**

```sql
RIGHT(REPLICATE(<caractere>, <tamanho>) + <coluna>, <tamanho>)
```

**Exemplo:**

```sql
leftPad('123', '0', 5)
```

**Exemplo de consulta:**

```sql
SELECT leftPad(CODIGO, '0', 8) AS CODIGO_PAD FROM PRODUTOS;
```

***

## subString

**Propósito:** Retorna parte de uma string.

**Sintaxe:**

```sql
subString(<coluna>, <início>, <fim>)
```

**Oracle:**

```sql
SUBSTR(<coluna>, <início>, <fim>)
```

**MSSQL:**

```sql
SUBSTRING(<coluna>, <início>, <fim>)
```

**Exemplo:**

```sql
subString('abcdef', 2, 3)
```

**Exemplo de consulta:**

```sql
SELECT subString(NOME, 1, 5) AS PRIMEIRAS_LETRAS FROM CLIENTES;
```

***

## upperText

**Propósito:** Converte texto para maiúsculas.

**Sintaxe:**

```sql
upperText(<expressão>)
```

**Oracle:**

```sql
UPPER(<expressão>)
```

**MSSQL:**

```sql
UPPER(RTRIM(CONVERT(VARCHAR(4000),<expressão>)))
```

**Exemplo:**

```sql
upperText(NOME)
```

**Exemplo de consulta:**

```sql
SELECT upperText(NOME) AS NOME_MAIUSCULO FROM CLIENTES;
```

***

## getMonth

**Propósito:** Retorna o mês de uma data.

**Sintaxe:**

```sql
getMonth(<data>)
```

**Oracle:**

```sql
TO_CHAR(<data>, 'MM')
```

**MSSQL:**

```sql
MONTH(<data>)
```

**Exemplo:**

```sql
getMonth(DATA)
```

**Exemplo de consulta:**

```sql
SELECT getMonth(DATA_NASCIMENTO) AS MES_NASC FROM CLIENTES;
```

***

## getYear

**Propósito:** Retorna o ano de uma data.

**Sintaxe:**

```sql
getYear(<data>)
```

**Oracle:**

```sql
TO_CHAR(<data>, 'YYYY')
```

**MSSQL:**

```sql
YEAR(<data>)
```

**Exemplo:**

```sql
getYear(DATA)
```

**Exemplo de consulta:**

```sql
SELECT getYear(DATA_NASCIMENTO) AS ANO_NASC FROM CLIENTES;
```

***

## getDay

**Propósito:** Retorna o dia de uma data.

**Sintaxe:**

```sql
getDay(<data>)
```

**Oracle:**

```sql
TO_CHAR(<data>, 'DD')
```

**MSSQL:**

```sql
DAY(<data>)
```

**Exemplo:**

```sql
getDay(DATA)
```

**Exemplo de consulta:**

```sql
SELECT getDay(DATA_NASCIMENTO) AS DIA_NASC FROM CLIENTES;
```

***

## monYear

**Propósito:** Retorna mês e ano de uma data.

**Sintaxe:**

```sql
monYear(<data>)
```

**Oracle:**

```sql
TO_CHAR(<data>, 'MM/YYYY')
```

**MSSQL:**

```sql
FORMAT(<data>, 'MM/yyyy')
```

**Exemplo:**

```sql
monYear(DATA)
```

**Exemplo de consulta:**

```sql
SELECT monYear(DATA_NASCIMENTO) AS MES_ANO FROM CLIENTES;
```

***

## addMonths

**Propósito:** Soma meses a uma data.

**Sintaxe:**

```sql
addMonths(<data>, <quantidade>)
```

**Oracle:**

```sql
ADD_MONTHS(<data>, <quantidade>)
```

**MSSQL:**

```sql
DATEADD(MONTH, <quantidade>, <data>)
```

**Exemplo:**

```sql
addMonths(DATA, 2)
```

**Exemplo de consulta:**

```sql
SELECT addMonths(DATA_VENDA, 3) AS DATA_FUTURA FROM VENDAS;
```

***

## endOfCurrentMonth

**Propósito:** Retorna o último dia do mês atual.

**Sintaxe:**

```sql
endOfCurrentMonth()
```

**Oracle:**

```sql
LAST_DAY(SYSDATE)
```

**MSSQL:**

```sql
EOMONTH(GETDATE())
```

**Exemplo:**

```sql
endOfCurrentMonth()
```

**Exemplo de consulta:**

```sql
SELECT endOfCurrentMonth() AS FIM_MES_ATUAL;
```

***

## convertToTimestamp

**Propósito:** Converte expressão para timestamp.

**Sintaxe:**

```sql
convertToTimestamp(<expressão>)
```

**Oracle:**

```sql
TO_TIMESTAMP(<expressão>)
```

**MSSQL:**

```sql
CONVERT(DATETIME, <expressão>)
```

**Exemplo:**

```sql
convertToTimestamp(DATA)
```

**Exemplo de consulta:**

```sql
SELECT convertToTimestamp(DATA) AS DATA_TIMESTAMP FROM LOGS;
```

***

## convertToMilliseconds

**Propósito:** Converte expressão para milissegundos.

**Sintaxe:**

```sql
convertToMilliseconds(<expressão>)
```

**Oracle:**

```sql
EXTRACT(MILLISECOND FROM <expressão>)
```

**MSSQL:**

```sql
DATEPART(MILLISECOND, <expressão>)
```

**Exemplo:**

```sql
convertToMilliseconds(DATA)
```

**Exemplo de consulta:**

```sql
SELECT convertToMilliseconds(DATA) AS MILIS FROM LOGS;
```
