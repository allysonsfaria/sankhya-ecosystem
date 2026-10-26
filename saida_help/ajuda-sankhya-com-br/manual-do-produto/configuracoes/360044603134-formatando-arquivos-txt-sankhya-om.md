---
id: "360044603134"
titulo: "Formatando arquivos TXT - Sankhya-Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:10Z"
rotulos: ["Configuração", "Impressão", "Relatórios Formatados", "Variáveis", "TXT", "SIADE", "Formatando arquivos TXT - Sankhya-W manual", "Formatação de Arquivos TXT: Funções e Variáveis", "Sankhya-Om"]
---

# Formatando arquivos TXT - Sankhya-Om

Na criação/formatação de arquivos no formato txt, diversas variáveis podem ser utilizadas e consultadas por meio do tópico [Variáveis de TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109013-Vari%C3%A1veis-de-txt). Além disso, várias funções podem ser aplicadas na formatação destes arquivos. A seguir trataremos sobre estas funções:

| [Abertura do Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Aberturadoarquivo) | [Fixar Posição de Conteúdo no Modelo TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Fixarposi%C3%A7%C3%A3odeconte%C3%BAdonomodelotxt) |
| --- | --- |
| [Ordenação de itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Ordena%C3%A7%C3%A3odeitens) | [Impressão de Outros Modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Impress%C3%A3odeoutrosmodelos) |
| [Aglutinação de itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Aglutina%C3%A7%C3%A3odeitens) | [Agrupamento de itens na Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Agrupamentodeitensnaimpress%C3%A3o) |
| [Impressão de itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Impress%C3%A3odeitens) | [Recortar Partes da Variáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Recortarpartesdavari%C3%A1veis) |
| [Impressão de Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Impress%C3%A3odemat%C3%A9rias-primas) | [Organização na Impressão de Grandes Textos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Organiza%C3%A7%C3%A3onaimpress%C3%A3odegrandestextos) |
| [Impressão de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Impress%C3%A3odeservi%C3%A7os) | [Impressão de Campos sem Variáveis Preexistentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Impress%C3%A3odecampossemvari%C3%A1veispreexistentes) |
| [Utilização de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Utiliza%C3%A7%C3%A3odefiltros) | [Transformar Texto em Número](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Transformartextoemn%C3%BAmero) |
| [Desprezar Linhas em Branco](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Desprezarlinhasembranco) | [Definir Tamanho Padrão para uma Variável](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Definirtamanhopadr%C3%A3oparaumavari%C3%A1vel) |
| [Flexível](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Flex%C3%ADvel) | [Utilização das Condições para Impressão das...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Utiliza%C3%A7%C3%A3odascondi%C3%A7%C3%B5esparaimpress%C3%A3odasvari%C3%A1veis) |
| [Atribuir Máscara Para um Valor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#Atribuirmascaraparaumvalor) |  |

---

#### Abertura do Arquivo

A função **"SIADE"** é utilizada, para que nossos sistemas possam reconhecer o modelo que está sendo configurado como um modelo de impressão válido, e deve estar presente em todos os modelos de impressão em formato TXT e HTML, lembrando que a linha Web não realiza a impressão de modelos em HTML.

Esta função deverá estar sempre na primeira linha, no primeiro bite do modelo, com a seguinte estrutura:

```
*** SIADE ***
```

Caso esta função não seja encontrada no local correto, o sistema emitirá a mensagem: 

**"Modelo não pertence ao MGE".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Ordenação de itens

Esta função é utilizada para ordenação dos itens nos documentos impressos. Deve estar na primeira linha do arquivo, ao lado da função SIADE (citada anteriormente), com a estrutura ORDEM=n, onde **"n"** varia de 0 a 7, representando:

**0** = TGFITE.SEQUENCIA    

**1** = TGFPRO.DESCRPROD

**2** = TGFPRO.LOCALIZACAO, TGFPRO.DESCRPROD

**3** = TGFITE.CODPROD

**4** = TGFPRO.CODGRUPOPROD, TGFITE.CODPROD

**5** = TGFITE.CODLOCALORIG, TGFITE.CODPROD

**6** = TGFITE.CODEXEC, TGFITE.SEQUENCIA

**7** = TGFITE.CODLOCALORIG, TGFITE.SEQUENCIA

Por exemplo:

```
*** SIADE *** ORDEM=1
```

Será feita ordenação pela descrição do produto.

Além da função ORDEM, existe a função **"ORDEMESPECIAL"**, que foi criada para permitir a ordenação dos itens do documento em função de quaisquer outros campos das tabelas de itens ou de produtos, inclusive em função de campos adicionais nestas tabelas.

Para isso, você deve inserir na primeira linha do modelo a chave ORDEMESPECIAL e no corpo do modelo inserir o bloco:

```
*** INICIO ORDEM ***

    P.<CAMPO> ou

    I.<CAMPO>

*** FIM ORDEM ***
```

Onde **"P"** refere-se a **"Tabela de Produtos"**, e **"I"** esta relacionada a **"Tabela de Itens"** da nota.

**Nota:** na linha gráfica, ao cadastrar o modelo na tela de [Modelos de Nota Fiscal/Duplicata/Boletas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913), deve-se lembrar de fazer sua compilação por meio do botão **"Compilar o modelo para acelerar a impressão"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Aglutinação de itens

A função **"AGRUPA"** é utilizada para agrupar múltiplos registros do mesmo item na impressão de documentos. A estrutura da função é AGRUPA=x, onde **"x"** pode ser **"S"** para produto, **"L"** para local, **"C"** para controle e **"N"** para não agrupar.

**Nota:** quando estiver utilizando a função AGRUPA=x, não será possível imprimir observações sobre o produto (campo **"Observações"**), a não ser que X seja igual a N (não agrupar).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Impressão de itens

Esta função é utilizada para separar, na impressão de documentos como notas e pedidos, a parte do documento onde serão impressos os itens da Nota/Pedido. Todas as variáveis que estiverem contidas entre as funções de início e fim, serão impressas tantas vezes quantos forem os itens da Nota/Pedido. Por exemplo:

```
*** INICIO ITENS ***

 &vcd601   &vnom01   &vqtd01   &vvlr01   &vtot01

         &PDES('COMPLDESC','TGFPRO','CODPROD='+&TGFITE.CODPROD)

*** FIM ITENS *** 51
```

Nesse exemplo, utilizado em formulários pré-impressos (onde se imprime apenas o conteúdo das colunas), serão impressos o código, descrição, quantidade, valor unitário e valor total de cada item da nota. Na linha abaixo, será impresso ainda o complemento da descrição do produto, cuja variável foi criada utilizando a função PDES, que será vista adiante.

Observe que ao final, foi utilizada a função \*\*\* FIM ITENS \*\*\* NN, na linha imediatamente posterior à das variáveis. O **"NN"** é a linha final de impressão dos itens. Para calcular a quantidade de itens, você deverá verificar em qual linha foi digitado o \*\*\* INICIO ITENS \*\*\*. Soma-se 1 ao número da linha, e no resultado soma-se a quantidade de itens que devem ser impressos. O valor obtido deve ser colocado no lugar do NN, em \*\*\* FIM ITENS \*\*\* NN.

A função **"ITEMAX"**, que deve ser informada ao lado da função de **"Início Itens"**, é utilizada para definir o número máximo de itens a serem impressos em cada página do documento. Caso o número de itens lançado para o pedido/nota seja superior ao definido nesta função, o formulário será quebrado no número de páginas necessários para impressão de todos os itens. Considere o seguinte exemplo:

```
*** INICIO ITENS *** ITEMAX=10
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Impressão de Matérias-Primas

Para incluir as matérias-primas relativas aos itens, coloque \*\*\* INICIO MP \*\*\* e nas próximas linhas indique as variáveis de matérias-primas. Ao terminar esta seção, informe \*\*\* FIM MP \*\*\*.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Impressão de Serviços

Para fazer a inclusão de serviços no modelo a ser impresso, escreva \*\*\* INICIO SERVICOS \*\*\* e na próxima linha, informe as variáveis dos itens. Para finalizar os serviços, coloque \*\*\* FIM SERVICOS \*\*\*.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Utilização de Filtros

Existe a possibilidade de se fazer filtros dentro dos modelos de impressão. O filtro deve ser colocado no final do TXT, com o uso dos indicadores \*\*\* INICIO FILTRO \*\*\* e \*\*\* FIM FILTRO \*\*\*.

De forma semelhante às outras seções, os filtros deverão estar entre estes dois indicadores. Os nomes das variáveis devem ser ITE.XXX, onde **"XXX"** é o nome de um campo da TGFITE. Por exemplo:

```
*** INICIO FILTRO ***

AND ITE.CODLOCALORIG <> 203

*** FIM FILTRO ***
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Desprezar Linhas em Branco

Esta função é utilizada para que as linhas em branco sejam desprezadas na impressão. Existem duas formas de utilização da variável **"DESPREZARLINHABRANCO"**. São elas:

**1)** Para respeitar o número de linha final, é necessário utilizar esta instrução somente no início do corpo de impressão do serviço ou produto.

No exemplo abaixo, a impressão irá parar na linha 50:

```
*** INICIO SERVICOS *** DESPREZARLINHABRANCO

 &vqtm01   &vnom01   &vvlr01   &vtot01

                    copy(&obs1,0,120)

*** FIM SERVICOS *** 50
```

**2)** Se for utilizada a variável conforme exemplo abaixo, o txt será impresso apagando a linha em branco, ou seja, irá subir tudo que estiver abaixo das linhas. Por exemplo:

```
*** INICIO SERVICOS ***

 &vqtm01   &vnom01   &vvlr01   &vtot01

                    copy(&obs1,0,120) DESPREZARLINHABRANCO

*** FIM SERVICOS ***
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Flexível

Quando o número de linhas dos itens for variável e usar a função DESPREZARLINHABRANCO, pode-se usar no início do TXT a opção **"FLEXIVEL"**. Quando for utilizado esta opção, ao informar no \*\*\* FIM ITENS \*\*\* a linha final de impressão de produtos, esta linha final será respeitada e o conteúdo entre \*\*\* INICIO ITENS \*\*\* e \*\*\* FIM ITENS \*\*\* só ficará na página se couberem todas as linhas. Por exemplo:

Apresentando um **"IF"** nos itens, fazendo com que a linha seja impressa só para alguns produtos, e utilizando a função DESPREZARLINHAEMBRANCO, esse item só será impresso na mesma página, se todas as linhas do item couberem na mesma página.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Agrupamento de itens na Impressão

É possível realizar AGRUPAMENTOS no modelo, similar aos agrupamentos do formatador de relatórios.

Para isso, é necessário criar uma sessão, delimitada por \*\*\* INICIO CAB GRUPO \*\*\* e \*\*\* FIM CAB GRUPO \*\*\*, podendo também ser utilizada uma sessão para rodapé, delimitadas por \*\*\* INICIO TOT GRUPO \*\*\* e \*\*\* FIM TOT GRUPO \*\*\*.

Diferente do formatador, aqui só é permitido uma quebra. Similar ao formatador, precisamos de uma coluna de ordenação, que funcionará para controlar o agrupamento. A ordenação é controlada pelo parâmetro **"ORDEM=n"**, utilizado na linha \*\*\* SIADE \*\*\* e pode ser:

- **"2"** para quebrar pelos campos LOCALIZACAO do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113);
- **"5"** ou **"7"** para quebrar por LOCAL DE ORIGEM digitado nos itens;
- **"6"** para quebrar pelo Executante informado nos itens;
- **"4"** para quebrar por Grupo de produto.

As variáveis a seguir, estão disponíveis para totalizarem no rodapé:

SetVar('gqtdneg', Pae(fmsc(gruQtdNeg,\_mqtd,6,'S'), 6,space01));

SetVar('gqtdent', Pae(fmsc(gruQtdEnt,\_mqtd,6,'S'), 6,space01));

SetVar('gqtd',    Pae(fmsc(gruQtdNeg-gruQtdEnt,\_mqtd,6,'S'), 6,space01));

SetVar('gvlrtot', pae(fmsc(gruVlrTot,\_mven,16,'S'),16,space01));

SetVar('gvlrtotdesc', pae(fmsc(gruVlrTotMenosDesc,\_mven,16,'S'),16,space01));

SetVar('gvlrliq', pae(fmsc(gruVlrLiq,\_mven,16,'S'),16,space01));

SetVar('gvlripi', pae(fmsc(gruVlrIPI,\_mven,16,'S'),16,space01));

SetVar('gcontad', pae(IntToStr(gruCont),3,space01)).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Fixar Posição de Conteúdo no Modelo TXT

A função **"POSICIONAL"** é utilizada para definir de forma fixa, a posição a ser respeitada na impressão de determinadas variáveis em modelos TXT. Utilizada normalmente para variáveis de rodapé, para que sejam respeitados os espaços destinados ao rodapé independentemente do número de itens impressos no documento. Para conhecer a estrutura da função, considere o seguinte exemplo:

```
*** INICIO POSICIONAL ***

[64,105] &numnot

*** FIM POSICIONAL ***
```

Onde:

- &numnot = Variável a ser impressa;
- 64 = Linha onde será impressa;
- 105 = Coluna onde será impressa.

Esta função é colocada no final do TXT, geralmente na linha abaixo das variáveis &oitrel &dcprel.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Impressão de Outros Modelos

Existe também a funcionalidade de se indicar outro modelo de nota a ser impresso imediatamente após a conclusão da impressão do primeiro, viabilizando que mais relatórios possam ser feitos durante a impressão da nota. As diretrizes para este procedimento são:

```
*** OUTRO MODELO *** nome_do_arquivo

*** OUTRA IMPRESSORA *** nome_da_impressora
```

Se não for informada **"Outra Impressora"**, será usada a mesma impressora.

Se no primeiro for informado um nome repetido no encadeamento de modelos, o computador irá travar.

**Observação:** se o TXT possuir POSICIONAL, você deve fechá-lo com \*\*\* FIM POSICIONAL \*\*\*.

**Impressão de Holletit**

Para impressão de documentos relacionados à folha de pagamento, existem funções semelhantes à Início Itens, citada anteriormente.

Para impressão de Hollerit's, por exemplo, utilize a função \*\*\* INICIO EVENTOS \*\*\* para delimitar a parte dos detalhes do hollerit, podendo aplicar a variável **"EVEMAX=xx"** ao lado, para se definir a quantidade máxima de eventos a serem impressos em cada página.

---

**Impressão de Múltiplas Cópias**

O parâmetro COPIA=N é o responsável pela definição da quantidade de cópias do arquivo TXT, a serem impressas, e quando utilizada, deverá ser inserida logo à frente da função \*\*\* SIADE \*\*\*. Por exemplo:

```
 *** SIADE *** COPIAS=2
```

![Imagem 1: É permitida uma quantidade máxima de 9 cópias.](https://ajuda.sankhya.com.br/hc/article_attachments/16425098041879) É permitida uma quantidade máxima de 9 cópias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Utilização das Condições para Impressão das Variáveis

**"IF"** é uma forma de aplicar condições em layout's/modelos para a impressão de notas, com o objetivo de retornar uma ou outra informação, de acordo com o atendimento da condição estabelecida. Com um IF, tem-se a possibilidade de testar o valor de uma determinada variável antes de fazer sua impressão.

Na tradução do inglês para o português, **"IF"** quer dizer "se", ou seja, "no caso de", "dado a circunstância de".

Portanto, é utilizada para que seja avaliada uma situação. Caso a condição seja verdadeira, a função retornará uma informação, e caso seja falsa, retornará outra informação. 

O IF possui a seguinte sintaxe:

```
IF(<CONDIÇÃO>,<IMPRIME_SE_VERDADEIRO>,<IMPRIME_SE_FALSO>)
```

Considere o seguinte exemplo:

```
IF(&cidcli='UBERLANDIA          ','UDIA',&cidcli)
```

Com esta expressão, se a cidade do parceiro for Uberlândia, será impresso **'UDIA'**; senão, será impresso a cidade do parceiro da nota.

Notemos que os valores fixos foram inseridos na expressão delimitados por apóstrofos (aspas simples). Vejamos também que foram adicionados 10 espaços após a palavra "UBERLANDIA". Isto porque a variável "&cidcli" retorna sempre 20 caracteres, completando com espaços à direita caso o conteúdo possua menos de 20 caracteres.

![Imagem 2: Para conhecer o tamanho de uma variável, configure sua impressão de forma isolada, delimitando a variável com dois…](https://ajuda.sankhya.com.br/hc/article_attachments/16425098044823) Para conhecer o tamanho de uma variável, configure sua impressão de forma isolada, delimitando a variável com dois caracteres constantes (|, !, etc.), desta forma:

```
| &cidcli |
```

Utilizando a variável desta forma, será impresso:

```
| UBERLANDIA           |
```

Assim, você pode contar a quantidade de espaços acrescentados pela variável ao intervalo definido.

Se o IF for utilizado em um modelo TXT, é interessante que os dois valores (verdadeiro ou falso) possuam o mesmo tamanho, para que os outros valores impressos à direita não fiquem desalinhados.

Ainda no exemplo anterior, pode-se definir o IF desta forma, para padronização do tamanho:

```
IF(&cidcli='UBERLANDIA          ','UDIA                ',&cidcli)
```

Outra observação importante na construção de um IF, é que a função não pode ser posicionada "colada" à margem esquerda do arquivo. Deve haver ao menos um espaço separando a função da margem esquerda do arquivo de layout. Vejamos outros exemplos:

```
IF(&nropag=&pagatu,&totnot,'        ')
```

A condição acima valida se a página atual é a última página da nota, comparando o número de páginas do documento, com o número da página atual. Se for a última página, será impresso o total da nota. Se não for, serão impressos quatro asteriscos. Esta condição é utilizada quando existe a possibilidade da impressão utilizar mais de uma página, fazendo com que os totalizadores sejam impressos apenas na última página.

```
IF(&endrec='                                    ',&endcli,&endrec)
```

O objetivo desta condição, é verificar se deve ser impresso o endereço de recebimento do parceiro, ou o endereço principal do mesmo. A função valida se a variável correspondente ao endereço de recebimento retorna 36 espaços, ou seja, verifica se o endereço do recebimento está preenchido. Se o endereço do recebimento não estiver preenchido, a condição será verdadeira, e com isso, será impresso o endereço principal do parceiro. Caso a variável retorne conteúdo diferente de 36 espaços, significa que o endereço de recebimento do parceiro está preenchido, e este será impresso.

```
IF('&tipmov'='V','X'+'        ','         '+'X')
```

A condição acima é normalmente utilizada na impressão de Notas Fiscais em formulário contínuo, para preenchimento do campo que define se esta é uma operação de entrada ou de saída. Este campo normalmente é marcado com um **"X"**, de acordo com o tipo de movimento da operação. Na condição acima, está sendo validado se o tipo de movimento é "Venda". Se for, será impresso o X alinhado a esquerda, completando com oito espaços. Caso não seja "Venda", primeiramente serão impressos os mesmos oito espaços, e depois a letra "X", de modo que seja marcado o campo **"Entrada"** da Nota Fiscal.

```
IF(&vvoa01=&vvol01,&vqtd01,&vqta01)
```

Esta expressão verifica se a **"Unidade"** utilizada no lançamento do item é igual à **"Unidade Principal"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Se não for, conclui que está sendo lançado no item da nota um volume definido como unidade alternativa do Cadastro de Produtos e por isso, retornará a quantidade negociada convertida para unidade alternativa. Se as unidades forem iguais, a função retornará a quantidade de acordo com a unidade principal. Desta forma, a impressão será realizada sempre da mesma forma que visualiza-se os itens nas centrais de notas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Recortar Partes da Variáveis

- **COPY**

O COPY é um comando para extrair uma parte de uma variável; extrair apenas o "DDD" do número de telefone, a raiz do CEP, parte do CNPJ, etc.

A estrutura utilizada na construção do COPY é a seguinte:

```
&COPY(<VARIÁVEL>,<CARACTERE_INIC>,<NRO_DE_CARACTERES>)
```

Por exemplo:

A variável **"&cepcli"** retorna no CEP do parceiro, com a seguinte máscara: "99.999-999". Se por algum motivo, não seja necessário imprimir os separadores da máscara, pode-se utilizar:

```
&COPY(&cepcli,1,2)+&COPY(&cepcli,4,3)+&COPY(&cepcli,8,3)
```

Vejamos que primeiramente pegou-se partindo do primeiro, dois caracteres, e estes foram ligados; a partir do quarto, com mais três caracteres; e novamente com os últimos três caracteres, a partir do oitavo.

Notemos também que foi utilizado o sinal de **"+"** para unir as diferentes partes do CEP, para que sejam impressas sequencialmente e sem espaços.

- **LEFT/RIGHT**

Estas funções são empregadas de forma semelhante ao COPY. A diferença, é que nestas não se aponta o caractere inicial. O corte será sempre realizado a partir do primeiro caractere à esquerda (LEFT) ou à direita (RIGHT).

A estrutura das funções é a seguinte:

```
&LEFT(<VARIÁVEL>,<NÚMERO_DE_CARACTERES>)

&RIGHT(<VARIÁVEL>,<NÚMERO_DE_CARACTERES>)
```

Utilizemos como exemplo novamente a variável "&cepcli". Imaginemos que em um determinado formulário, é preciso informar os cinco primeiros números do CEP em um campo, e os três últimos, em um campo diferente. Se o "ponto" (.) da máscara puder ser mantido, pode-se utilizar para os cinco primeiro números do CEP:

```
&LEFT(&cepcli,6)
```

Reforçando que no exemplo foi informado "6" para o número de caracteres, pois a variável "&cepcli" traz um ponto em sua máscara. Assim, será impresso "99.999", caso o CEP seja "99.999-999".

Para imprimir os três últimos números do CEP, ao invés de usar a variável "&COPY(&cepcli,8,3)" apresentada anteriormente pode-se, alternativamente utilizar:

```
&RIGHT(&cepcli,3)
```

Na formatação de TXT, a função **"LOTEINFO"** (chave, tamanho) buscará na tabela TGFLOT as informações complementares da chave, e apresentará com o tamanho especificado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Organização na Impressão de Grandes Textos

A função **"LINHA"** fraciona a impressão de campos de acordo com os parâmetros utilizados, e permite a impressão de até 400 caracteres, para campos tipo "Memo". A sintaxe dessa função é a seguinte:

```
LINHA(&campo,TAMANHO,LINHA,'SEPARADOR')
```

Por exemplo:

```
LINHA(&PDES('PRO.CARACTERISTICAS','TGFPRO
PRO','CODPROD='+&TGFITE.CODPROD),46,1,';')
```

Neste exemplo serão impressos os 46 primeiros caracteres do campo **"Características"** do cadastro de produtos.

Para continuar a impressão da linha seguinte, basta acrescentar a mesma expressão na linha abaixo, alterando apenas o **"Número da Linha"**, para que sejam impressos os caracteres seguintes, desta forma:

```
LINHA(&PDES('PRO.CARACTERISTICAS','TGFPRO
PRO','CODPROD='+&TGFITE.CODPROD),46,1,';')

LINHA(&PDES('PRO.CARACTERISTICAS','TGFPRO
PRO','CODPROD='+&TGFITE.CODPROD),46,2,';')
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Impressão de Campos sem Variáveis Preexistentes

O **"PDES"** é uma função de pesquisa, ou de consulta, utilizada para impressão de valores que não podem ser obtidos através das variáveis preexistentes. Com o PDES, pode ser impresso qualquer valor, de qualquer tabela do sistema, desde que a consulta realizada por meio do comando retorne um único valor. E isto é possível realizando ligações entre o PDES e variáveis existentes que retornem campos chaves das tabelas envolvidas.

A estrutura utilizada na construção de um PDES, é a seguinte:

```
&PDES('<COLUNA>','<TABELA(S)>',<CONDIÇÃO(ÕES)>)
```

Notemos que a estrutura da função é semelhante à estrutura do **"SELECT"**, utilizado para consultar informações no banco de dados. Para o uso do PDES, é necessário ter noções sobre banco de sados, e a estrutura das tabelas utilizadas pelo sistema.

Quanto às condições, normalmente são realizadas ligações entre as tabelas que estão sendo consultadas e as variáveis pré-existentes.

Deve ficar claro que a união entre uma parte fixa do comando, e uma parte variável deve ser realizada por meio do sinal **"+"**, sendo que as partes fixas do comando devem estar entre aspas simples, desta forma:

```
&PDES('<COLUNA>','<TABELA(S)>',<'<CONDIÇÃO_FIXA>'+<VARIAVEL>)
```

Por meio dos exemplos descritos a seguir, podemos entender melhor suas aplicações:

```
&PDES('P.NOMEPARC','TGFPAR P, TGFC C','P.CODPARC = C.CODPARC AND C.NUNOTA=
'+&TGFCAB.NUNOTA)
```

O PDES acima retornará o Nome do Parceiro do Pedido/Nota que está sendo impresso.

Notemos que a variável **"&TGFCAB.NUNOTA"**, foi utilizada como ligação para que o PDES retornasse um único resultado.

```
&PDES('CID.NOMECID','TSICID CID, TGFPAR PAR, TGFCAB CAB','CID.CODCID = PAR.CODCID
 AND PAR.CODPARC = CAB.CODPARC AND CAB.NUNOTA ='+&TGFCAB.NUNOTA)
```

Neste segundo exemplo foi acrescentada mais uma tabela (Cidades), para que a seleção retornasse o Nome da Cidade do parceiro do Pedido/Nota. Este exemplo reforça que o PDES pode fazer consultas utilizando ligações entre múltiplas tabelas.

A variável &TGFCAB.NUNOTA também foi utilizada como ligação para que o PDES retornasse um único resultado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Transformar Texto em Número

A função **"Val"** é utilizada para transformar em valor, um conjunto de caracteres que originalmente foram armazenados como texto.

A estrutura desta função é a seguinte:

```
&VAL(<VARIÁVEL>)
```

Esta função normalmente é utilizada em conjunto com as funções PDES e FORMATNUMERIC.

Enquanto a função PDES retorna um texto, a função VAL transforma este resultado em valor, para que a função FORMATNUMERIC consiga formatar este número no padrão desejado, como pode-se ver abaixo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Atribuir Máscara Para um Valor

A função **"FORMATNUMERIC"**é utilizada para realizar a formatação de números, para que a impressão respeite um padrão. É muito utilizada na impressão de valores, quando deseja-se que os decimais (centavos) sejam sempre impressos, mesmo quando estes decimais forem zero. Como esta função só funciona com "números", normalmente é empregada para formatar os valores obtidos por meio de um PDES, como vimos anteriormente, pois o PDES retorna os valores da mesma forma que armazenados no banco de dados, ou seja, sem formatação.

A estrutura desta função é a seguinte:

```
FORMATNUMERIC(<MÁSCARA>,<VARIÁVEL>)
```

Considere os seguintes exemplos:

```
1) FORMATNUMERIC('000000','&tgfcab.numnota')
```

Neste exemplo será impresso o número da nota, respeitando a regra: se o número for menor que 100.000, será completado com zeros à esquerda até chegar em seis dígitos. Por exemplo: se o número da nota for "150", será impresso "000150". Se o número for 150.000, será impresso "150000".

```
2) FORMATNUMERIC('000,000','&tgfcab.numnota')
```

Já neste caso, também será realizada a impressão do número da nota. Porém, acrescenta-se um separador de milhares, mantendo-se o mínimo de 6 dígitos para o número. Esta composição não é suportada corretamente na linha Web.

```
3) FORMATNUMERIC('###,###,###,##0','&tgfcab.numnota')
```

Este exemplo também será utilizado para impressão do número da nota com separador de milhares, mas sem completar o número da nota com zeros à esquerda.

**Observações:**

- Na linha Web você deve prever o tamanho possível do número a ser recebido com o símbolo **"#"**, caso o número seja menor, a impressão será completada com espaços.
- Na linha gráfica para realizar o terceiro exemplo, basta apenas a função FORMATNUMERIC('#,##0','&tgfcab.numnota'), que até mesmo os maiores números seriam impressos com novos separadores (milhar, milhão, bilhão etc). Outra diferença é que não são acrescentados espaços à esquerda para números menores que mil.

```
4)FORMATNUMERIC('###,##0.00',&Val(&Pdes('AD_QTDEPARC','TGFITE','NUNOTA=
' + &TGFCAB.NUNOTA)))
```

Neste exemplo, está sendo feita a formatação com decimais e separador de milhares, o conteúdo do campo adicional "AD\_QTDEPARC". Vejamos que o "PDES" foi utilizado para buscar o valor do Banco de Dados, a função "VAL" foi utilizada pra transformar este valor em número, e só então foi utilizada a função "FORMATNUMERIC" para aplicar-se a máscara.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)

#### Definir Tamanho Padrão para uma Variável

As funções **"PAD"** e **"PADL"** são utilizadas para atribuir tamanho padrão ao resultado de uma variável construída. O resultado da variável será acrescido de espaços à direita (PAD) ou à esquerda (PADL), até completar o tamanho definido na função.

A função PAD normalmente é utilizada para textos, e a função PADL é utilizada para números.

Estas são utilizadas principalmente em arquivos TXT, onde o alinhamento de textos em colunas é realizado por meio de espaços. Se esta função não for utilizada nestes casos, as colunas ficarão desalinhadas em função do tamanho do conteúdo impresso em cada linha.

A estrutura destas funções é a seguinte:

```
&PAD(<VARIÁVEL>,<TAMANHO_TOTAL>)

&PADL(<VARIÁVEL>,<TAMANHO_TOTAL>)
```

Por exemplo:

```
&PAD(&PDES('CID.NOMECID','TSICID CID, TGFPAR PAR, TGFCAB CAB','CID.CODCID=PAR.
CODCID AND PAR.CODPARC=CAB.CODPARC AND CAB.NUNOTA='+&TGFCAB.NUNOTA),30)
```

Utilizamos o exemplo de PDES apresentado anteriormente, que retorna o nome da cidade do parceiro, para demonstrar a função PAD, acrescentando tantos espaços à direita quantos forem necessários até que o nome da cidade impresso complete 30 caracteres.

Se a cidade do parceiro for "Uberlândia", será impresso "UBERLANDIA\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_" (onde "\_" está aqui representando um espaço em branco, para permitir a leitura). Se a função utilizada fosse PADL, o resultado seria "\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_UBERLANDIA".

**Observação:** deve-se ter cuidado ao configurar a impressão compactada em impressoras matriciais. Ao colocar a variável de compactação no início do arquivo "&cptrel", lembre-se de colocar a variável de descompactação no final do arquivo "&dcprel". Sem isso, a impressora fica configurada para impressão compactada e qualquer outro documento enviado para a mesma, será impresso compactado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-Om#top)
