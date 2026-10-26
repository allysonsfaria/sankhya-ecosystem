---
id: "360044579974"
titulo: "Melhores práticas para Funções/expressões em relatórios iReport e Fórmulas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579974-Melhores-pr%C3%A1ticas-para-Fun%C3%A7%C3%B5es-express%C3%B5es-em-relat%C3%B3rios-iReport-e-F%C3%B3rmulas"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T15:51:22Z"
rotulos: ["#RevisadoWellington", "Configuração", "Relatórios", "Fórmulas", "iReport", "Funções Utilitárias para Relatórios no iReport", "Sankhya Util"]
---

# Melhores práticas para Funções/expressões em relatórios iReport e Fórmulas

Os relatórios formatados pelo iReport e depois executados no SankhyaW precisam de funções utilitárias que devem rodar tanto no ambiente de design quanto no próprio SankhyaW.

Uma das funções mais utilizadas é a PDES, que existe em pelo menos 3 classes mas que não estão no formato adequado para ser usada no iReport, pois em sua maioria dependem de recursos não disponíveis no ambiente de design.

Para resolver esse problema e criar um padrão de funções disponíveis para o iReport foi criada a classe **br.com.sankhya.jasperfuncs.Funcoes onde devemos disponibilizar métodos utilitários.**

**O primeiro método implementado é justamente o pdes, com a seguinte assinatura:**

**public static String pdes(Connection c , String sCol, String sTable, String sWhere)**

vejam que ele recebe a conexão como primeiro argumento, isso é necessário para torná-la independente de chamador.

**Segue um exemplo de uso em uma expressão de campo do iReport:**

**br.com.sankhya.jasperfuncs.Funcoes.pdes($P{REPORT\_CONNECTION},”NOMEPARC”,”TGFPAR”,”CODPARC=” + $F{CODPARC})**

Notem o uso do parâmetro **REPORT\_CONNECTION que é criado automaticamente pelo iReport e possui referencia para a conexão JDBC em uso pelo JasperReport.**

Essa classe faz parte do projeto SankhyaUtil, e portanto temos que atualizar nosso iReport para download.

**Função STP:**

Essa função permite chamar **StoredProcedures** ou **Functions** do banco de dados dentro de relatório formatados no iReport, segue a sintaxe:

**br.com.sankhya.jasperfuncs.Funcoes.stp( <CONEXAO\_BD>, <NOME\_PROCEDURE>, <PARAMETROS\_DE\_ENTRADA> , <TIPO\_DE\_RETORNO> })**

**Detalhe dos argumentos:**

- **<CONEXAO\_BD>**: conexão com o banco de dados usada pelo iReport.

o valor será sempre $P{REPORT\_CONNECTION}

- **<NOME\_PROCEDURE>** : nome da procedure, exatamente como está declarada no BD
- **<PARAMETROS\_DE\_ENTRADA>**: parâmetros que serão passados para a procedure. Na prática é uma lista de pares com tipo e valor (conforme exemplo)

new Object[]{ <TIPO\_P1>, <VALOR\_P1> , <TIPO\_P2>, <VALOR\_P2>, … , <TIPO\_Pn> , <VALOR\_Pn>}

onde <TIPO\_Px> pode ser “N” para numéricos, “S” para texto e “T” para datas

- **<TIPO\_DE\_RETORNO>**: Esse parâmetro é OPCIONAL, e só deve ser usado se a procedure retornar algum valor que o relatório vá usar.

Determina o tipo de retorno da procedure/function, e deve possuir um valor que seja equivalente ao tipo de retorno declarado para a procedure, por exemplo:

java.sql.Types.DOUBLE   (para tipos float no BD)

java.sql.Types.INTEGER   (para tipos int no BD)

java.sql.Types.NUMERIC   (para tipos NUMBER no BD)

a lista completa de tipos pode ser vista em <http://download.oracle.com/javase/6/docs/api/index.html>

**Exemplos:**

- Chamada para uma procedure com 1 parâmetro de entrada do tipo numérico:

br.com.sankhya.jasperfuncs.Funcoes.stp( $P{REPORT\_CONNECTION} ,”STP\_ATUALIZA\_CARTA\_COBRANCA”, new Object[]{ “N”, $F{NUFIN}  })

- Chamada para uma procedure com 2 parâmetros de entrada, o primeiro numérico e o segundo texto:

br.com.sankhya.jasperfuncs.Funcoes.stp( $P{REPORT\_CONNECTION}, “STP\_ATUALIZA\_CARTA\_COBRANCA”, new Object[]{ “N”, $F{NUFIN} , “S”, “TESTE”} )

- Chamada para uma procedure com 3 parâmetros de entrada, o primeiro numérico ,o segundo texto e o terceiro data:

br.com.sankhya.jasperfuncs.Funcoes.stp( $P{REPORT\_CONNECTION}, “STP\_ATUALIZA\_CARTA\_COBRANCA”, new Object[]{ “N”, $F{NUFIN} , “S”, “TESTE”, “T”,”01/01/2011″} )

**Expressões aceitas e usadas pela Aplicação em Fórmulas:**

**Val()**

Por padrão o resultado das variáveis/funções são do tipo 'string', sendo assim não consegue fazer cálculos com os mesmos.
A função '**Val()**' é utilizada para converter a string para um valor numérico, sendo assim possível fazer cálculos com o resultado.

**Exemplo:**
VAL(PDES('VLRDESCTOT','TGFCAB','NUNOTA='+NUNOTA))

**FormatNumeric(Utilizado na visualização de relatórios)**
FORMATNUMERIC('M', 'V') - Formata um valor, onde 'M' representa a mascara e 'V' o valor a ser formatado.

**Exemplo:**
VLRNOTA = 13900,66(sem formatação)
FORMATNUMERIC('###,###,##0.00', VLRNOTA)
Resultado com o Format: 13.900,66

Observação: Essa função foi utilizada da formatação de formulas. Logo qualquer outra função que esteja disponível também pode ser utilizado por esse formatador.

**Round('Campo','Casas decimais para considerar no round').**
Usado para arredondar as casas decimais do resultado da expressão/campo.

**Exemplo:**
PI = 3.14159265359
Round(PI,4)
Resultado do Round = 3.141**6**- Note que houve arrendondamento para cima.

**Trunc('Campo','Casas decimais para considerar no trunc')**
Usado para truncar as casas decimais do resultado da expressão/campo.
Trunc remove a parte fracionaria do numero.

**Exemplo:**
PI = 3.14159265359
Round(PI,4)
Resultado do Round = 3.141**5** - Note que não houve arredondamento de forma alguma.

**IF('Expressão booleana', 'Retorna aqui, se verdadeiro', 'Retornar aqui, se falso');**
A expressão de logica booleana é uma estrutura logica que pode ser verdadeira ou falsa. A logica booleana usa tabelas verdade (TRUE ou FALSE) para determinar o valor verdade (TRUE ou FALSE) das expressões.

**Exemplo:**
Idade = 15
IF(idade > 18, "Sou maior de idade","Sou menor de idade")
Resultado do IF "Sou maior de idade"

**Pdes('Campos','Tabelas','Condição');**
Semelhante a SELECT, busca informações de tabelas/view do sistema.

**Exemplo:** SELECT AD\_VLRVENDOR FROM TGFCAB WHERE NUNOTA = 1100
      PDES('AD\_VLRVENDOR','TGFCAB','NUNOTA='+:NUNOTA)
