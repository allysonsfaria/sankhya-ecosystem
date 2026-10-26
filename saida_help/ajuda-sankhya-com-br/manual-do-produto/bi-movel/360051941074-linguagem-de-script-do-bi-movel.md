---
id: "360051941074"
titulo: "Linguagem de Script do BI MÓVEL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL"
trilha: "Manual do Produto > Inteligência e Análise > BI Móvel"
atualizado_em: "2026-07-29T13:40:09Z"
rotulos: ["BI Móvel", "Script", "Editor de Mensagens", "Iteradores", "Variáveis", "Linguagem de Script para BI Móvel: Facilitadores Variáveis e Iteradores", "Mensagens Linguagem de Script Variáveis."]
---

# Linguagem de Script do BI MÓVEL

Esse artigo refere-se ao [Editor de Mensagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353), assim, na definição do texto e da condição do envio dessas mensagens, será possível utilizar trechos de código em Java ou na linguagem de script desenvolvida para o BI Móvel, uma vez que ele contêm vários facilitadores. Para saber mais sobre, acesse os tópicos a seguir:

| Facilitadores da Linguagem de Script do BI MÓVEL | |
| --- | --- |
| [Variáveis e Seletores de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#variveiseseletoresdedados) | [Tabelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#tabelas) |
| [Iteradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#iteradores) | [Utilizadores de Iteradores em Mensagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#utilizaodeiteradoresemmensagens) |
| [Cursores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#cursores) | [Utilização de Iteradores na Construção...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#utilizaodeiteradoresnaconstruoevariveis) |
| [Condição de Disparo das Mensagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#condiodedisparodasmensagens) | [Utilização de Variáveis em Fórmulas SQL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#utilizaodevariveisemfrmulassql) |
| [Formatando Números](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#formatandonmeros) | [Funções Auxiliares](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#funesauxiliares) |
| [Editor Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#editoravanado) | [Fila de Mensagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#filademensagens) |
| [Configuração do Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#configuraodoservidorsmtp) |  |

### Variáveis e Seletores de Dados

São consideradas variáveis pelo interpretador todas as palavras iniciadas com o símbolo **$**, seguido de um ou mais caracteres alfanuméricos. Opcionalmente, a variável pode possuir um seletor de dados, sendo que, o seletor definirá qual das datas de referência existentes no histórico de valores da variável será considerada. Se o seletor for omitido, será considerado o valor da variável correspondente à última data de referência presente no histórico.

O seletor será escrito entre colchetes, logo após o nome da variável, ou seja:

```
$variavel[seletorDados]
```

A seguir, observe algumas funções que podem ser utilizadas como seletores de dados:

- **anual():** retornará a data de referência para o ano corrente (primeiro dia do ano);
- **mensal():** irá retornar a data de referência para o mês corrente (dia do mês);
- **quinzenal():** retornará a data de referência para a quinzena do mês;
- **semanal():** essa função retornará a data do primeiro dia da semana corrente (Domingo);
- **diaria():** retornará a data do dia corrente;
- **todoMes(mês):** essa função retornará o primeiro dia do mês indicado para o último ano em que o mês ocorreu. Por exemplo, se a data atual é 15/04/2008 e utiliza-se todoMes(3), a data retornada será 01/03/2008. Já a chamada todoMes(8), retornaria 01/08/2007, porque o mês 08 ainda não ocorreu em 2008;
- **todoDia(dia):** aqui, a informação referente ao dia indicado para o último mês em que o dia ocorreu será retornada;
- **todoDiaSemana(diaSemana):** retornará a data para a última ocorrência do dia da semana indicado. O Parâmetro diaSemana pode assumir uma das opções: **"DOM"** para Domingo, **"SEG"** para segunda-feira, **"TER"** para terça-feira, **"QUA"** para quarta-feira, **"QUI"** para quinta-feira, **"SEX"** para sexta-feira e **"SAB"** para sábado;
- **data(dia, mes, ano):** essa função, permite montar uma data fixa informando o dia, mês e ano. Por exemplo, data(15, 4, 2008) para retornar o dia 15 de abril de 2008.
- **modDia(data, n):** essa, modificará o dia da data informada adicionando n dias. Por exemplo, caso queira a data de referência para dois dias atrás, pode-se utilizar modDia(diaria(), -2);
- **modMes(data, n):** essa função irá alterar o mês da data informada, adicionando n meses. Como exemplo, a data de referência para o mês passado pode ser obtido com modMes(mensal(), -1);
- **modAno(data, n):** funciona da mesma forma que as duas funções anteriores, mas em relação ao ano. Por exemplo, modAno(anual(), -1) retorna a data de referência para o ano passado.

Observe a seguir, um exemplo da utilização de uma variável com seletor de dados em uma mensagem:

```
O total de vendas no mês passado foi de:        $total_vendas[modMes(mensal(), -1)]
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Tabelas

Existe uma notação que facilita a exibição de uma variável do tipo **"Tabela"** em uma mensagem, sendo que ela será exibida em HTML. Esse tipo de notação só é válida para mensagens cujo envio for por e-mail. Deve-se escrever o nome da variável do tipo Tabela, e opcionalmente, será seguido pelo seletor de colunas e o seletor de dados envolvidos pelo marcador **tab{ }**, ou seja:

```
 tab{$var(col1,col2,...)[dtref]}
```

O termo **[dtref]** é a data de referência que será utilizada para buscar os dados, e recebe o valor de outra variável do tipo data.

Esse termo pode ser omisso; nesse caso, serão considerados os dados que tiverem a maior data de referência, ou seja, os mais recentes. Se a escolha dos campos não for informada, todas as colunas da tabela serão selecionadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Iteradores

Os **"Iteradores"** são mecanismos que percorrem as listas, linha a linha e são utilizados no BI Móvel com a finalidade de imprimir tabelas, históricos de variáveis e para a geração de variáveis do tipo **"Calculado"**, cujo tipo de saída é Tabela. Permite também grande flexibilidade na composição das mensagens, possibilitando a formatação do texto da maneira que for mais conveniente. Eles serão escritos nos seguintes formatos:

```
         repita para $variavel {
                 ...
         }
```

ou

```
         repita para $variavel filtrando expressaoFiltro {
                 ...
             }
```

O conjunto das palavras reservadas **"repita para"** e os marcadores **"{ }"**, indicam ao interpretador que está sendo definido um novo Iterador.

A iteração é aplicada na variável definida em $variavel. Caso esteja utilizando o **"repita"** sem opção de filtro, o bloco de código entre { } será repetido para cada linha de $variavel. Se a palavra **"filtrando"** estiver sendo utilizada, o bloco de código só será repetido para as linhas cujo resultado da expressão do filtro for verdadeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Utilização de Iteradores em Mensagens

Em uma mensagem no bloco de código do Iterador, será possível inserir um texto e variáveis que terão seus valores alterados de acordo com a linha atual de cada uma, sobre a qual é feita a iteração. Para referenciar uma variável, utilize o seu nome, ou o termo **"$variavel.valor"**. Será possível tambem acessar a data de referência da variável corrente pela propriedade **"dt\_ref"** utilizando a **$variavel.dt\_ref**. Dessa forma, observe abaixo alguns exemplos de iteradores nas mensagens:

![Imagem 1: Considere a variável $emails do tipo tabela que contém duas colunas " NOMEUSU" , dado ela inclui o nome dos usuários do…](https://ajuda.sankhya.com.br/hc/article_attachments/20473426177047) Considere a variável **$emails** do tipo tabela que contém duas colunas **"NOMEUSU"**, dado ela inclui o nome dos usuários do sistema e o endereço de e-mail cadastrado para cada um, dessa forma:

```
Repita para $emails filtrando ano($emails.dt_ref) == anoCorrente() {
 Usuário: $emails.NOMEUSU                                                        
 Email: $emails.EMAIL.valor                                                                
}                                                                                                        
```

Assim, o iterador acima imprimirá as linhas **"Usuário"** e **"Email"** para cada linha da variável **$emails** cujo ano da data de referência seja igual ao ano atual. As expressões **$emails.NOMEUSU** e **$emails.EMAIL** serão substituídas pelos valores das respectivas colunas da linha atual representada por **$emails**.

---

![Imagem 2: Considere que $venda_mes seja uma variável do tipo tabela que contém os campos TOTAL e MES . Sua data de referência foi…](https://ajuda.sankhya.com.br/hc/article_attachments/20473426184855) Considere que **$venda\_mes** seja uma variável do tipo tabela que contém os campos TOTAL e MES. Sua data de referência foi gerada a partir da função de periodicidade **"mensal"**.

```
Repita para $venda_mes filtrando ano ($venda_mes.dt_ref) == anoCorrente() - 1 {              
      Mês: $venda_mes.MES  Total: $venda_mes.TOTAL                                              
}                                                                                                        
```

Nesse caso, para cada linha da variável cujo ano é o ano passado, será impressa uma linha com informação do mês e o valor do campo TOTAL para aquele mês.

---

![Imagem 3: Ao montar mensagens, será possível inserir textos normalmente antes e após o iterador e mesmo nos delimitadores { } ,…](https://ajuda.sankhya.com.br/hc/article_attachments/20473426191895) Ao montar mensagens, será possível inserir textos normalmente antes e após o iterador e mesmo nos delimitadores **{ }**, como nos exemplos acima. Esse recurso pode ser utilizado para formatar a mensagem gerada pelo iterador com a linguagem HTML em mensagens com o tipo de conteúdo configurado como **"HTML"**. O exemplo abaixo ilustra esse tipo de utilização:

```
<font size="2" face="Courier New">                                    
<b>Vendas Mensais por Vendedor:</b> <br>                                        
repita para $vendmes {                                                                              
Vendedor: $vendmes.VENDEDOR                                                                      
Mês: $vendmes.MES        Total: $vendmes.TOTAL_VENDA<br>                        
}                                                                                                      
<br>                                                                                                      
<b>Vendedores que ultrapassaram a meta de R$ 10.000,00:</b>        
<br>                                                                                                      
repita para $vendmes filtrando $vendmes.TOTAL_VENDA >= 10000 {        
Cód.Vendedor: $vendmes.CODVEND        Mês: $vendmes.MES<br>                  
}<br>                                                                                                      
<i>Obs.: Os vendedores sem vendas no mês não foram listados.</i>                      
</font>                                                                                                
```

No exemplo acima, foram utilizadas as tags da linguagem HTML a fim de conseguir a formatação desejada para a mensagem. Dessa forma, observe a função de cada uma das tags utilizadas:

- A tag <**font**> foi utilizada para definir uma fonte mono espaçada. Ela pode ser muito útil para conseguir um efeito de tabela com o texto;
- Posteriormente, existe a tag <**b**>, que foi aplicada aos títulos a fim de destacá-los;
- Utiliza-se a tag <**br**> para aplicar saltos de linhas na mensagem;
- E <**i**>, deixará o texto que está sendo delimitado em itálico.

Assim, a mensagem gerada por esta fórmula teria a seguinte aparência:

#### Vendas Mensais por Vendedor:

Vendedor: João         Mês: 10        Total: 5867                        

Vendedor: Maria        Mês: 10        Total: 11000                        

Vendedor: José          Mês: 10        Total: 8684                        

Vendedor: João          Mês: 11        Total: 10001                        

Vendedor: Maria         Mês: 11        Total: 2777                        

Vendedor: José           Mês: 11       Total: 9840                     

#### Vendedores que ultrapassaram a meta de R$ 10.000,00:

Vendedor: Maria        Mês: 10                                                

Vendedor: João         Mês: 11                                              

**Observação:** os vendedores sem vendas no mês não serão listados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Utilização de Iteradores na Construção e Variáveis

Os Iteradores possuem alguns recursos a mais quando utilizados na construção de variáveis. Entretanto, não é permitido a inserção de textos como visto em mensagens. A sua função neste contexto é a de geração de variáveis do tipo Calculado com saída Tabela linha a linha, a partir de outras variáveis já existentes.

Considere o exemplo abaixo:

```
Repita para $pedmes {                                                                              
 $est_vendedor.novaLinha();                                                              
         $est_vendedor.codvend = $pedmes.codvend;              
         $est_vendedor.criterio = "POSITIVACAO";                                      
         $est_vendedor.pontos = 6;                                                      
 $est_vendedor.salvar();                                                                      
}                                                                                                        
```

A fórmula acima gera a variável **$est\_vendedor** que está sendo cadastrada. Para cada linha da variável **$pedmes**, uma linha de **$est\_vendedor** foi criada, que contém os campos **"codvend"**, **"criterio"** e **"pontos"** previamente cadastrados, atribuindo os valores **"$pedmes.codven"**, **"POSITIVACAO"** e **"6"** respectivamente. Dessa forma, a variável **"$est\_vendedor"** gerada será representada por uma tabela com o mesmo número de linhas da tabela de **"$pedmes"**, onde o campo **"codvend"** de cada linha terá o mesmo valor do campo equivalente em **"$pedmes"**, enquanto os outros dois campos possuem valores constantes. Note que para cada linha incluida, deve-se utilizar os métodos **novaLinha()** e **salvar()** da variável, e todos os campos devem ser informados entre essas duas instruções.

Além da possibilidade da utilização de condições através da palavra **"filtrando"**, utilize os recursos da linguagem Java para criar regras para as variáveis. Algumas palavras reservadas do Java foram traduzidas e podem ser utilizadas tanto em sua forma original quanto em sua versão em português.

![Edimen6](https://ajuda.sankhya.com.br/hc/article_attachments/15443543449367)

Não será discutido aqui a utilização das palavras reservadas do Java. Entretanto, ao definir a palavra **"buscar"**, sua função será localizar uma determinada linha em uma variável com base em uma expressão que retorne **"verdadeiro"** ou **"falso"**; sendo que ela é uma das três adições da linguagem de script do BI móvel em relação à linguagem Java. Assim, observe:

```
buscar $variavel filtrando expressão;
```

Informe em **$variavel**, a variável que se está pesquisando, dado que a expressão deve ser uma que retorne verdadeiro para a linha procurada. Caso seja utilizada uma expressão que retorne verdadeiro para mais de um registro, apenas o primeiro será considerado. Após utilizado esse método, utilize os campos da variável normalmente. Considere o exemplo abaixo:

```
Repita para $vendcom {                                                                              
  $tabcalc.novaLinha();                                                                              
    buscar $emails filtrando igual($emails.email, "usu@sankhya.com.br");      
      $tabcalc.parc_ativos = $vendcom.QTD_PARC;                                              
      $tabcalc.apelido = $emails.nomeusu;                                                      
      $tabcalc.codvend = $vendcom.CODVEND;                                              
      $tabcalc.qtd_parc_novos = $vendcom.QTD_PARC_NOVOS;                              
 $tabcalc.qtd_parc = $vendcom.QTD_PARC;                                              
      $tabcalc.VLRVENDA = $vendcom.TOTAL_VENDA;                                              
      se ($vendcom.QTD_PARC_NOVOS / $vendcom.QTD_PARC > 0.1)                      
        $tabcalc.VLRCOM = ($vendcom.comvenda + 1)*$vendcom.TOTAL_VENDA/100;
      Senão                                                                                                
        $tabcalc.VLRCOM = $vendcom.comvenda * $vendcom.TOTAL_VENDA/100;      
    $tabcalc.salvar();                                                                              
}                                                                                                        
```

Nesse caso, o campo **$tabcalc.apelido** recebe seu valor com base no campo **$emails.nomeusu** para a linha em que o **$emails.email** vale "usu@sankhya.com.br".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Cursores

Na Linguagem de script do BI Móvel, um cursor serve para incluir um trecho de linguagem SQL para consultas em banco com a finalidade de criar variáveis do tipo tabela localmente, sem a necessidade de cadastro. Ele deve ser definido da seguinte forma:

```
     $nomeCursor = SQL
```

O SQL do cursor pode apresentar parâmetros inseridos por dois pontos. Como, por exemplo, :PARAMETRO

Para atribuir um valor a um parâmetro, deve-se utilizar o cursor:

```
      $nomeCursor.parametro = valor;
```

Após a definição da consulta em SQL e informar os valores de todos os parâmetros do cursor, caso haja algum, será necessário abri-lo para que ele possa ser utilizado através do método abrir():

```
     $nomeCursor.abrir();
```

A partir desse ponto, é possível utilizar o cursor como uma variável normal. Dessa forma, observe o exemplo completo de criação de variáveis com cursor:

```
$cursorCliente =        SELECT NOMEUSU,                                                              
                          CODUSU,                                                              
                          EMAIL                                                              
                          FROM TSIUSU                                                      
                 WHERE  NOMEUSU LIKE :nomeusu                                              
                   AND         CODGRUPO = :codgrupo;                                              
$cursorCliente.codgrupo = 99;                                                                      
$cursorCliente.nomeusu = "Z%";                                                              
$cursorCliente.abrir();                                                                              
repita para $cursorCliente {                                                                      
 $testecursor.novaLinha();                                                              
         $testecursor.nomeusu = $cursorCliente.nomeusu;                              
 $testecursor.salvar();                                                                      
}                                                                                                        
```

Como resultado da execução do script acima, será criada a variável **$testecursor** que possui uma coluna nomeada **"nomeusu"** cujo valor é o nome dos usuários que começam com "Z" e pertencem ao grupo 99.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Condição de Disparo das Mensagens

Sempre que a hora programada no campo período da mensagem é atingida, a condição de disparo da mensagem é testada.

A fórmula da condição deve sempre retornar um valor booleano, ou seja, verdadeiro ou falso. Na sua composição, pode-se utilizar todas as variáveis, com exceção das que possuem saída do tipo tabela. Por exemplo, considere a existência de uma variável **$naoconformidade** que retorna o número de horas gastas em ordens de serviço de não conformidade. Nesse caso, quem está cadastrando uma mensagem para exibição do valor da variável pode escolher que a mensagem não seja enviada caso não houverem horas gastas em não conformidade. Portanto, a fórmula da condição poderia ser montada da seguinte maneira:

```
 Se ($naoconformidade > 0) {
         retorne verdadeiro;
 } senao {
         retorne falso;
 }
```

É possível notar que, a fórmula possui uma cláusula de retorno para todas as possibilidades de avaliação. Se o valor da variável **$naoconformidade** for maior que zero, a expressão retornará o valor verdadeiro e a mensagem será enviada. Caso contrário, o resultado será falso e a mensagem não será disparada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Utilização de Variáveis em Fórmulas SQL

Para variáveis do tipo **"SQL"**, poderá utilizar outras variáveis com saída para o tipo tabela em sua fórmula, com regras parecidas com as da utilização de uma tabela SQL normal. Dessa forma, observe o exemplo a seguir:

A fórmula para a variável **$total\_vendas**, que calcula o valor total de vendas por mês, com base na variável **$vendmes** que contém os valores de vendas por vendedor:

```
SELECT SUM($vendmes.total_venda)
  FROM $vendmes
 WHERE $vendmes.dt_ref >= TRUNC(SYSDATE,'MONTH')
```

Na fórmula, utiliza a variável **$vendmes** como se fosse uma tabela SQL normal; ao usar seu nome seção **"FROM"** e acessar suas colunas nas outras partes do SQL através do nome da variável, seguido por ponto e do nome da coluna. Porém, há algumas diferenças em relação ao uso de uma tabela normal, são elas:

- Não atribuia apelidos às variáveis através da palavra reservada "AS";
- Utilize as propriedades internas da variável, como sua data de referência (dt\_ref) ou seu valor como se fossem colunas normais de uma tabela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Formatando Números

Nas mensagens do BI Móvel, poderá utilizar a função **masc** com a finalidade de formatar números. A função possui o seguinte protótipo:

```
  masc(valor, padrão)
```

Em que, o **"valor"** é o número que o usuário deseja formatar e **"padrão"** especifica como deve ser a apresentação do número.

O padrão é feito através do caractere **'#'** e de dígitos e deve estar entre aspas. Caso deseje informar um número que pode assumir qualquer valor, inclusive vazio, utiliza-se **'#'**. Caso o valor não possa assumir vazio, informe o número que será apresentado no caso. Por exemplo, para criar uma formatação para valores de moedas, utilize o seguinte padrão:

```
  "R$ ###.##0,00"
```

Nesse padrão, será possível obter as seguintes informações:

- O número tem duas casas decimais e, quando for inteiro, será utilizado 00;
- As casas decimais serão separadas por vírgula;
- A cada 3 dígitos, um ponto será utilizado;
- A sigla R$ será utilizada no início do número.

Sendo assim, observe os exemplos:

```
    masc(6, “R$ ###.##0,00”) retornará o valor R$ 6,00
    masc(1234567.89, “R$ ###.##0,00”) retornará R$ 1.234.567,89
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Funções Auxiliares

O BI Móvel possui algumas funções pré-definidas que podem ser utilizadas para a composição de variáveis, mensagens e condições. Visto que, é necessário observar bem o tipo de retorno para que essas funções sejam aplicadas de forma correta. Dessa forma, observe:

![Imagem 5: F unções booleanas, em que seu retorno deve ser Verdadeiro ou Falso:](https://ajuda.sankhya.com.br/hc/article_attachments/20473426177047) Funções booleanas, em que seu retorno deve ser Verdadeiro ou Falso:

- igual(objeto1, objeto2)

![Imagem 6: Funções matemáticas, sendo que elas terão um retorno numérico:](https://ajuda.sankhya.com.br/hc/article_attachments/20473426184855) Funções matemáticas, sendo que elas terão um retorno numérico:

- exp(double b, double e)
- log(double a)
- log10(double a)

![Imagem 7: Já as Funções gerais para data, terão retorno: igual à data:](https://ajuda.sankhya.com.br/hc/article_attachments/20473426191895) Já as Funções gerais para data, terão retorno: igual à data:

- getDate()
- getDateTime()
- toDate(String s)
- addDay(Timestamp t, int q)

![Imagem 8: Referente às funções para obter parte de determinada data, o retorno deve ser inteiro:](https://ajuda.sankhya.com.br/hc/article_attachments/20473446269207) Referente às funções para obter parte de determinada data, o retorno deve ser inteiro:

- ano(Timestamp dtRef)
- mes(Timestamp dtRef)
- dia(Timestamp dtRef)
- quinzena(Timestamp dtRef)

![Imagem 9: Funções para obter parte da data corrente, devem retornar um valor inteiro:](https://ajuda.sankhya.com.br/hc/article_attachments/20473446276375) Funções para obter parte da data corrente, devem retornar um valor inteiro:

- anoCorrente()
- mesCorrente()
- diaCorrente()
- semanaCorrente()
- diaSemanaCorrente()
- quinzenaCorrente()
- primeiroDiaMes()
- ultimoDiaMes()
- primeiroDiaSemana()
- ultimoDiaSemana()
- inicioQuinzena(int quinzena)
- fimQuinzena(int quinzena)

![Imagem 10: As funções simplificadas para serem utilizadas no seletor, deverão ter um retorno igual a data:](https://ajuda.sankhya.com.br/hc/article_attachments/20473446279575) As funções simplificadas para serem utilizadas no seletor, deverão ter um retorno igual a data:

- anual()
- mensal()
- quinzenal()
- semanal()
- diaria()
- porHora()
- porMinuto()
- todoMes(int mês)
- todoDia(int dia)
- todoDiaSemana(String diaSemana)

![Imagem 11: Por fim, as funções que retornam data e/ou hora já formatados, devem ter um retorno: igual a texto:](https://ajuda.sankhya.com.br/hc/article_attachments/20473446294807) Por fim, as funções que retornam data e/ou hora já formatados, devem ter um retorno: igual a texto:

- dataCorrenteFormatada()
- horaCorrenteFormatada()
- dataHoraCorrenteFormatada()

Tanto em Java quanto na linguagem de script do BI Móvel, quando o operador de comparação **==** (dois sinais de igual seguidos) for utilizado para comparar valores de variáveis, deverá ser utilizado apenas em tipos primitivos de dados. No nosso caso, é possível utilizá-lo para as funções que retornam valores inteiros ou decimais. Quando for comparar textos, datas, sendo elas, datas completas e não apenas o dia em separado, por exemplo; ou campos numéricos gerados a partir da leitura do banco de dados, utilize a função **igual(objeto1, objeto2)**, o que irá comparar seus dois parâmetros retornando verdadeiro caso sejam iguais ou falso, caso sejam diferentes. Sendo assim, considere os exemplos abaixo: 

- igual("BI Móvel", "BI Móvel") = retorna verdadeiro.
- 3 == 2 + 1  = retorna verdadeiro.
- igual($var1.dt\_ref, $var2.dt\_ref) = retorna verdadeiro se as datas de referência de $var1 e $var2 forem iguais.
- ano($var1.dt\_ref) == anoCorrente()  = retorna verdadeiro se o ano da data de  referência $var1 for igual ao ano corrente.

   [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Editor Avançado

Na tela de edição de variáveis e mensagens, a aba [Expressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593534-Editor-de-Vari%C3%A1veis#abaexpresso) possui alguns recursos para facilitar a edição de código, como:

- Colorização da sintaxe;
- Árvore de variáveis;
- Visualizador de propriedades;
- Execução de variável/mensagem para testes;
- Execução de SQL sem parâmetros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Fila de Mensagens

Todas as mensagens que foram processadas pelo sistema poderão ser visualizadas pela tela [Fila](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002573481-Fila), que possui uma lista onde cada linha representa uma mensagem na fila de envio. Dessa forma, tem-se as seguintes colunas:

Em **"Tipo** **de Envio"**, o sistema indicará se a mensagem deve ser enviada via e-mail e/ou SMS.

O **"Destinatário"** exibirá o nome do destinatário da mensagem, conforme cadastrado na tela [Destinatários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593394).

Na coluna **"Cód. Fila"**consulte o número único da mensagem na fila.

Em **"Cód. Msg."**, será exibido o código de cadastro da mensagem.

Na **"Data Entrada"** Data em que a mensagem entrou na fila de envio;

Consulte na coluna **"Status"**, a situação de envio da mensagem. Sendo que elas poderão estar como:

- **Pendente:** a mensagem entrou na fila para ser enviada e ainda não houve nenhuma tentativa;
- **Pendente: Erro:** a mensagem ainda não foi enviada, mas já houve pelo menos uma tentativa com falha. O número máximo de tentativas de envio ainda não foi atingido;
- **Pendente: Erro SMS:** houve sucesso no envio do e-mail e erro para a mensagem SMS. O número máximo de tentativas de envio ainda não foi atingido;
- **Pendente: Erro e-mail:** houve sucesso no envio do SMS e erro para o e-mail. O número máximo de tentativas de envio ainda não foi atingido;
- **Sucesso: Enviada:** a mensagem foi enviada com sucesso;
- **Erro: Não Enviada:** não houve o envio da mensagem. O número máximo de tentativas de envio foi atingido;
- **Erro: SMS \* Sucesso: email:** houve sucesso de envio para e-mail e erro para SMS. O número máximo de tentativas de envio foi atingido;
- **Erro: e-mail \* Sucesso: SMS:** houve sucesso de envio para SMS e erro para e-mail. O número máximo de tentativas de envio foi atingido.

A **"Tentativas de Envio"** indicará quantas vezes houve a tentativa de envio da mensagem. Quando o número máximo de tentativas cadastrado durante a criação da mensagem for atingido, será considerado um erro de envio.

Ao clicar em uma entrada na fila, no campo **"Mensagem"**, é possível visualizar a mensagem que será ou já foi enviada. Caso contenha tags html, utilize o botão **"Visualizar HTML"** para exibir a mensagem em sua forma formatada.

![Imagem 12: Ao clicar em uma entrada na fila, no campo "Mensagem" , é possível visualizar a mensagem que será ou já foi enviada .…](https://ajuda.sankhya.com.br/hc/article_attachments/4559656430615)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)

### Configuração do Servidor SMTP

Para enviar mensagens por e-mail, configure o servidor de SMTP, responsável por encaminhar as mensagens. Por meio da tela [Servidor SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593494), realize a seguinte configuração:

![Imagem 13: Para enviar mensagens por e-mail, configure o servidor de SMTP, responsável por encaminhar as mensagens. Por meio da…](https://ajuda.sankhya.com.br/hc/article_attachments/4559732651031)

Após o preenchimento dos campos, clique no botão ![Imagem 14: Após o preenchimento dos campos, clique no botão " Confirmar " para que as configurações possam ser salvas.](https://ajuda.sankhya.com.br/hc/article_attachments/20473426245015) **"Confirmar"** para que as configurações possam ser salvas.

Porém, antes do envio do e-mail, é possível testar se a configuração do servidor está correta por meio do botão ![Imagem 15: Porém, antes do envio do e-mail, é possível testar se a configuração do servidor está correta por meio do botão…](https://ajuda.sankhya.com.br/hc/article_attachments/20473426255511) **"Testar"**, após inserir o e-mail ao qual deseja enviar a mensagem no campo **"Destinatário"**; assim, uma mensagem validará a configuração e um texto de teste será enviado para o e-mail informado.

É possível ainda, enviar a OS por e-mail a partir da configuração da tela Servidor SMTP, independente da configuração do SMTP que fora definido. Para tal ação, o parâmetro **"Utilizar o BI Móvel para enviar OS por e-mail? - OSEMAILBIMOVEL"** deve estar habilitado.

Então, o sistema possui as seguintes possibilidades:

- Ao enviar uma OS por e-mail com o parâmetro OSEMAILBIMOVEL desligado, ele será enviado seguindo as configurações do SMTP do usuário de acordo com as definições cadastradas na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874). Se o referido parâmetro estiver ligado, o e-mail enviado seguirá as configurações da tela Servidor SMTP.
- Configure um modelo de e-mail em TXT ou HTML para o envio. Esse modelo deverá ser colocado no caminho indicado no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**. Caso  um modelo externo (configurado por ele) não seja utilizado, o sistema enviará um modelo padrão de e-mail.

**Observação:** mesmo com o parâmetro OSEMAILBIMOVEL ligado, se no caminho do parâmetro SERVDIRMOD estiver um modelo de TXT configurado com o nome **"email.txt"** ou **"email.html"** o e-mail enviado será com as configurações desse modelo.

![Imagem 16: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/20473426260503)Acesse também:

[Editor de Mensagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL#top)
