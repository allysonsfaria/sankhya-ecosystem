---
id: "360045108753"
titulo: "Configuração Arquivo Remessa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-21T18:50:43Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "CMC7", "Arquivo de Destino", "Configuração Arquivo Remessa", "Confirmação da Nota", "EDI Comercial", "EDI Comercial na Confirmação da Nota", "MASCEDI", "Query", "br.com.sankhya.edi.config.arquivo.remessa", "Configuração Arquivo Remessa manual", "EDI", "Financeiro", "Configuração Arquivo Remessas: Configuração Hierarquia Geração", "Comercial", "Arquivo Remessa"]
---

# Configuração Arquivo Remessa

| ``` ![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312006790423) Módulo: Comercial > EDI ``` |
| --- |

---

EDI - Eletronic Data Interchange (Intercâmbio Eletrônico de Dados) é a troca estruturada de informações entre a empresa e o banco através de arquivos. Esse recurso é composto por esta tela (Configuração Arquivo Remessa) e pela Geração Arquivo de Remessa. Através desta tela define-se a query e é feita a configuração das linhas do arquivo utilizado pela empresa.

[Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#abacampos)                                                              [Aba Query](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#abaquery)

[Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#abapropriedades)                                                    [Aba Geração em Lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#abageraoemlote)

[Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#botooutrasopes...)                                           [Arquivo de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#arquivodedestino)

[Ações Agendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#aesagendadas)

## Aba Campos

A aba Campos, somente estará habilitada caso esteja sendo configurada uma hierarquia inferior ao primeiro nível.

Primeiramente, através do parâmetro **"Máscara para Intercâmbio Eletrônico de Dados (EDI) - MASCEDI"** defina a máscara da hierarquia que será utilizada pela tela de configuração onde será formatado o layout do arquivo.

Feita a configuração do parâmetro, pode-se dar início a configuração do layout; para isso utilize a aba **"Campos"** para definir o conteúdo e o tamanho dos campos.

![Imagem 2: Feita a configuração do parâmetro, pode-se dar início a configuração do layout; para isso utilize a aba "Campos" para…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003544882)

Inicialmente nesta aba, determine a **"Sequência"** referente ao campo que está sendo cadastrado. Em seguida a esta informação, defina qual será o **"Tipo do Campo"**, dentre as seguintes opções:

- Decimal com zeros à esquerda;
- Decimal com brancos à esquerda;
- Inteiro com zeros à esquerda;
- Inteiro com brancos à esquerda;
- Alfanumérico;
- Alfanumérico com zeros à esquerda;
- Inicialização;
- Filtro.

É necessário atentar-se para a configuração do campo Tipo do Campo nos níveis de detalhe do EDI; deve-se definir adequadamente o tipo de cada campo a ser utilizado. Campos do tipo **"Filtro"** só devem ser usados em sequências negativas, geralmente empregadas fora do layout do arquivo.

A informação seguinte, diz respeito ao **"Conteúdo"** do campo; para isso, temos a opção de recorrer ao botão **"Assistente"**, posicionado logo à frente do campo. Este botão ao ser acionado, apresenta o assistente de [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213), onde serão listadas as categorias de funções, variáveis e banco de dados.

**Observação:** Na geração do arquivo de remessa, você poderá optar por gerar as tag's com letras minúsculas ou maiúsculas, na qual bastará informar as funções "Dados\_Disp.TESTE+LOWER" e "Dados\_Disp.TESTE+UPPER" respectivamente.

Uma vez determinado o conteúdo do campo, defina o **"Tamanho"** e a **"Quantidade de Decimais"** que ele irá possuir. O tamanho definido para o campo, irá determinar sua **"Posição Inicial"** e **"Posição Final"**, campos estes alimentados automaticamente.

**Nota:** Pode-se realizar a geração do EDI bancário de custódia de cheques, de modo que estes contenham os dígitos verificadores C1, C2 e C3. Estes dígitos se referem ao código da compensação, número do banco, agência, conta e números do cheque, além de serem utilizados na montagem do CMC7.

Para utilização desta funcionalidade, no Construtor de Expressões aberto através do botão Assistente, localize as funções GETC1, GETC2 e GETC3. Estas funções irão receber o CMC7 como parâmetro e retornar os dígitos C1, C2 e C3 do CMC7, respectivamente.

![Imagem 3: Para utilização desta funcionalidade, no Construtor de Expressões aberto através do botão Assistente , localize as…](https://ajuda.sankhya.com.br/hc/article_attachments/360102425134)

Ao acionar o botão ![Imagem 4: Ao acionar o botão "Ordenar Campos" , será aberta um pop-up com o nome "Ordenação dos Campos" , onde você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/360102364834) **"Ordenar Campos"**, será aberta um pop-up com o nome **"Ordenação dos Campos"**, onde você pode configurar a ordem dos campos definidos.

Já o botão ![Imagem 5: Já o botão "Copiar linhas de outro Layout" pode ser utilizado no início da configuração do Layout, onde tem-se a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003532541) **"Copiar linhas de outro Layout"** pode ser utilizado no início da configuração do Layout, onde tem-se a possibilidade de reproduzir as linhas de um layout já criado, no layout que está sendo criado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Aba Query

A aba Query, somente estará habilitada caso esteja sendo configurada uma hierarquia inferior ao primeiro nível. Nesta aba são configuradas as query's, que serão responsáveis por extrair as informações do banco de dados.

![Imagem 6: A aba Query , somente estará habilitada caso esteja sendo configurada uma hierarquia inferior ao primeiro nível. Nesta…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003549402)

Ao salvar um layout que esteja ativo, o sistema irá pegar as informações desta aba, e irá executar o comando SELECT, para verificar se a sintaxe está correta; caso esteja errada, não será permitido o salvamento do layout.

Para geração do EDI Comercial, na confirmação da nota nas Centrais é necessário que no campo **"Condições dos Campos"**, na parte mais analítica da árvore, tenha-se o filtro:

![Imagem 7: Para geração do EDI Comercial, na confirmação da nota nas Centrais é necessário que no campo "Condições dos Campos" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360104608313)

Este filtro será utilizado pelo sistema para gerar o arquivo mediante o número de notas selecionadas nos Portais, para geração do Arquivo EDI.

**Observação:** Na montagem do EDI, no filtro, será necessário informar [NUNOTA], exatamente desta forma, para que o sistema leia como chave.

Ex.: **( :NUNOTA: = ([NUNOTA]))**

Obtenha mais detalhes do EDI Comercial na **"Confirmação da Nota"** em [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

A função **"variavelPorNome(String nome)"** permite obter o valor de variáveis de filtro nomeadas a partir de qualquer nível. Por exemplo, é possível obter o valor de uma variável que foi definida em um detalhe no registro header.

Para adotar esta funcionalidade é necessário utilizar parâmetros nomeados. Para isso, basta operar o assistente de filtro no layout para gerar as condições de campo e ao colocar os campos variáveis e alterar a "?" (interrogação) da expressão pelo parâmetro nomeado seguindo os exemplos abaixo:

Para campos do tipo data, cria-se o parâmetro começando com 'DAT', exemplo:

**( :DTVENC: > [DATData Inicial] ) .E. ( :DTVENC: < [DATData Final] )**

Ao apresentar a tela de filtro, o sistema utiliza o 'DAT' para gerar um campo que aceita somente data e removê-lo da descrição (veja imagem abaixo).

![Imagem 8: Ao apresentar a tela de filtro, o sistema utiliza o 'DAT' para gerar um campo que aceita somente data e removê-lo da…](https://ajuda.sankhya.com.br/hc/article_attachments/360102430074)

Como apresentado na figura acima, o mesmo vale para campos do tipo inteiro, cria-se o parâmetro começando com 'INT', por exemplo:

**( CODPARC: = [INTParceiro] )**

Para campos do tipo número inteiro utiliza-se o prefixo 'INT'. Neste caso o sistema coloca um campo numérico que aceita somente números.

Para campo do tipo Decimal ou Moeda: cria-se um parâmetro começando com 'NUM', por exemplo:

**( :VLRNOTA: < [NUMValor máximo] )**

**Importante:** Apelidos de colunas não podem ser utilizados na composição das Condições dos campos. Caso um campo seja necessário para definição de filtros, não deve-se definir apelidos para o mesmo; o correto a ser feito, é a construção do filtro manualmente através da digitação do nome do campo no Banco de Dados.

**Observação:** A função variavelPorNome(), terá a sua funcionalidade na aba Campos desta tela, pois tem-se que as querys não interpretam variáveis desenvolvidas para os campos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Aba Propriedades

![Imagem 9: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/1500003545182)

As opções presentes na aba **"Propriedades"** somente são utilizadas para o layout que está sendo usado para gerar o arquivo, ou seja, se algum layout filho possuir estas marcações, elas não serão respeitadas:

**Ordenar o arquivo:** Caso esta opção esteja marcada, o sistema irá ordenar as linhas do arquivo em ordem alfabética.

**Primeira coluna somente p/ ordenação:** Esta opção deve ser assinalada juntamente à opção Ordenar o arquivo; esta marcação faz com que após a ordenação do arquivo em ordem alfabética, o primeiro campo definido na aba Campos seja removido do arquivo.

Esta marcação é efetuada, quando deseja-se utilizar o primeiro campo somente para ordenação e não tem-se a necessidade deste valor no arquivo. Ao utilizar esta opção, é necessário que o campo empregado para ordenação, tenha exatamente o mesmo tamanho em todos os registros.

**Gerar um arquivo p/ cada linha:** Esta marcação faz com que ao gerar o arquivo de remessa, cada linha seja gravada em um arquivo separado, porém se existir vários itens iguais em uma mesma nota e os arquivos ficarem com o mesmo nome, o sistema agrupará automaticamente todos os itens num mesmo arquivo.

**Nota:** Essa funcionalidade está disponível apenas para o EDI Comercial.

**Gerar um arquivo p/ cada detalhe do layout:** Selecionando esta marcação, será gerado um arquivo para cada item filho da árvore do layout, de forma compactada.

**Observação:** Esta marcação apenas estará disponível para o primeiro registro pai da árvore.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Aba Geração em Lote

Por meio desta aba temos a possibilidade de gerar os arquivos de remessa em lote através de uma query externa que irá definir o valor dos parâmetros em suas configurações. Em outras palavras, podemos realizar a inclusão de uma query, que a partir de seu resultado, obtêm-se o preenchimento dos parâmetros definidos anteriormente na aba Query de cada nível da configuração do arquivo, exceto em seu primeiro "Header"; neste é realizada a configuração na aba Geração em Lote.

#### O que é uma Query?

Structured Query Language, ou Linguagem de Consulta Estruturada ou SQL, é a linguagem de pesquisa declarativa padrão para banco de dados relacional (base de dados relacional). É o processo de extração de dados de um banco de dados e sua apresentação em uma forma adequada ao uso; são conjuntos de instruções que permitem extrair repetidamente determinado subconjunto de dados.

Pela aba Geração em Lote, realize a formulação de uma query que irá gerar um desmembramento do resultado dos filtros construídos, em alguns arquivos de remessa, seguindo obviamente as condições estabelecidas. Por exemplo, suponhamos que você deseja filtrar os títulos de uma única empresa, considerando um determinado período inicial e final, buscando os títulos por parceiro; imaginemos ainda que no período estabelecido, foram feitas negociações com três parceiros distintos. O resultado será a geração de três arquivos de remessa, em que tem-se o desmembramento por parceiros, ou seja, cada arquivo gerado corresponde a um parceiro diferente.

Para sucesso na configuração da geração em lote em um layout, é necessário que no cabeçalho da tela, o campo **"Arquivo de Destino"** tenha sido adequadamente preenchido. Para o preenchimento do arquivo de destino, pode-se utilizar a variável de nome **"Dados\_Disp.SEQ\_ARQ"** (sequência de arquivo); esta variável pode ser definida no nome do arquivo para que sejam gerados arquivos sequenciais; caso esta variável não seja definida, o arquivo gerado sempre será sobreposto pelo próximo.

Considere o exemplo abaixo de nome de arquivo, onde utilizou-se a variável de sequência:

**Dados\_Disp.SEQ\_ARQ+'\_REMGISS.TXT'**

Pode-se também definir no nome do arquivo, variáveis retornadas pela query de geração em lote. Por exemplo:

**'[CODPARC]\_REMGISS.TXT'**

**Observação:** Quando for utilizada a expressão 'Dados\_Disp' para o nome de arquivo, não será possível utilizar as variáveis literais ([CODPARC]) para resgatar os dados da query de geração em lote no nome de arquivo (mais informações sobre o campo Arquivo de Destino, poderão ser visualizadas mais abaixo nesta documentação).

![Imagem 10: Observação: Quando for utilizada a expressão 'Dados_Disp' para o nome de arquivo, não será possível utilizar as…](https://ajuda.sankhya.com.br/hc/article_attachments/1500003593161)

O botão **"Validar Consulta"** quando acionado, será realizada a validação da query configurada; sendo esta validação realizada com êxito, é apresentada a seguinte mensagem:

**"Consulta validada com sucesso!"**

Nos casos, em que esta validação não é bem sucedida, é exibida a seguinte mensagem:

**"ORA-00920: operador relacional inválido."**

Ao clicar no botão **"Gerar arquivo"** (acima do cabeçalho da tela), será exibido o pop-up para o preenchimento dos parâmetros configurados, onde serão apresentados apenas os parâmetros que não tiverem um respectivo campo como resultado da query da Geração em Lote.

Uma segunda utilização para a aba Geração em Lote, é o agrupamento dos filtros a serem utilizados nos demais layout's do EDI. No header do arquivo, informe o nome do arquivo a ser gerado, e nesta aba a query desejada.

No campo **"Condições dos Campos"** presente na aba **"Query"** nos detalhes do layout do EDI, informe os filtros contendo os campos variáveis, seguindo a nomenclatura definida na query da aba Geração em Lote. Considere o seguinte exemplo:

Query configurada na aba Geração em Lote do header do arquivo:

SELECT CODEMP AS COD\_EMPRESA

, INIPER AS INICIO\_PERIODO

, FIMPER AS FIM\_PERIODO

FROM VGF\_DIEFCEARA\_HOT

WHERE CODEMP = [INTCOD\_EMPRESA]

AND INIPER >= [DATINICIO\_PERIODO]

AND FIMPER <= [DATFIM\_PERIODO]

Filtros inseridos no campo Condições dos Campos na aba Query:

( :CODEMP: = [COD\_EMPRESA] ) .E.

( :INIPER: >= [INICIO\_PERIODO] ) .E.

( :FIMPER: <= [FIM\_PERIODO] )

Deste modo, no nosso exemplo, ao ser solicitado o preenchimento dos filtros (parâmetros variáveis), estes serão informados apenas uma vez, pois deste modo, o sistema entende que a parametrização realizada (filtros preenchidos) vale para o header e também para os detalhes nos layout's do EDI.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Botão Outras Opções...

O botão Outras Opções... conta com duas funcionalidades, **"Importar Layout"** e **"Exportar Layout"**; ambas tem por objetivo facilitar a configuração de layouts no sistema, uma vez que layouts já existentes em outras bases poderão ser importados e reutilizados, tem-se a geração de economia de tempo e trabalho na confecção destes arquivos.

![Imagem 11: O botão Outras Opções... conta com duas funcionalidades, "Importar Layout" e "Exportar Layout" ; ambas tem por objetivo…](https://ajuda.sankhya.com.br/hc/article_attachments/360102425454)

Ao acionar a opção Importar Layout, será aberto um pop-up para upload do arquivo desejado. De forma contrária, a opção Exportar Layout disponibiliza o layout "fora do sistema" para ser utilizado conforme a necessidade da empresa/usuário. É importante citar que os arquivos que poderão ser importados ou exportados, devem ser do formato **".xml"**.

**Importante:** O layout poderá ser importado em uma base, desde que esta base suporte a estrutura hierárquica deste layout. Portanto, é essencial se atentar para a configuração realizada no parâmetro **"Máscara para Intercâmbio Eletrônico de Dados (EDI) - MASCEDI"**. Por exemplo, se em uma base para a qual será feita a importação, a máscara definida no referido parâmetro é "99\.99\.99;0", não será possível importar um layout que possua "4" (quatro) níveis hierárquicos.

**Nota:** Quando você comprar uma solução pelo Place e esta for protegida, a opção Exportar Layout ficará indisponível. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Arquivo de Destino

Somente um layout com hierarquia pai e filhos, pode possuir o campo **"Arquivo de Destino"** informado, ou seja, se um layout filho estiver com este campo preenchido, ao preencher em um layout pai o sistema irá informar que já existe um nome de arquivo informado para layout's filhos; o mesmo irá acontecer se existir nome de arquivo em algum layout pai e for preenchido o nome em layout's filhos.

Além da tela [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914), é possível gerar o arquivo através do botão ![Gerar](https://ajuda.sankhya.com.br/hc/article_attachments/16081621835799) **"Gerar Arquivo"** presente na parte superior da tela.

O layout que for utilizado para gerar o arquivo deve estar Ativo e possuir o campo Arquivo de Destino preenchido com o nome desejado para o arquivo, caso contrário, no momento da geração o sistema irá lançar uma mensagem informando que os layout's não contêm este campo preenchido.

Ao gerar um arquivo, caso o layout possua uma Query com parâmetros variáveis, será exibida uma tela (ver imagem abaixo) com todos os parâmetros variáveis de todos os layout's utilizados para a geração deste arquivo.

![Imagem 13: Ao gerar um arquivo, caso o layout possua uma Query com parâmetros variáveis, será exibida uma tela (ver imagem abaixo)…](https://ajuda.sankhya.com.br/hc/article_attachments/360104609653)

**Nota:** O sistema realiza a geração do arquivo de remessa de forma progressiva, ou seja, criando-se o arquivo três vezes por exemplo, tem-se as seguintes nomenclaturas:

**NOME\_DO\_ARQUIVO - 1**.txt

**NOME\_DO\_ARQUIVO - 2**.txt

**NOME\_DO\_ARQUIVO - 3**.txt

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)

## Ações Agendadas

Trabalhando na Configuração do Arquivo de Remessa, é possível gerar o arquivo de configuração de forma automática, a partir de [Ações Agendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653). Isso é feito em um ambiente de desenvolvimento Java.

Depois de criada, deve-se enxergar a geração do arquivo como uma rotina que recebe algumas informações de entrada, executa um conjunto de transformações (relativamente desconhecidas) e devolve um resultado, nesse caso, um arquivo TXT de acordo com as regras do layout.

Nesse momento, entra o Platform Services, pois somente os desenvolvedores diretamente ligados ao projeto do Sankhya-Om tem acesso aos códigos fonte. O que seria necessário para interagir com este tipo de rotina. Além do mais, a rotina precisa estar suficientemente desacoplada do ambiente em que roda, para executar em ambientes diversos. É dada então uma forma padronizada, para obter o produto destas rotinas, a partir do seguinte comando:

PlatformService ps =  PlataformServiceFactory.getInstance().lookupService("@core:edi.comercial.service");

Existem diversos Platform Services, e a tendência que cada vez existam mais. Então a forma como identificamos qual serviço queremos usar é através do método **"lookupService"**. No caso do nosso serviço, deve-se usar o nome **"@core:edi.comercial.service"**, pois é assim que ele está registrado.

Com o serviço devidamente instanciado, observe como utilizá-lo. Primeiramente, deve-se fornecer todos os argumentos que ele necessita, que são:

- **codLayout** (Obrigatório) BigDecimal - Trata-se do layout de EDIComercial que será usado.
- **Parâmetros** (Opcional – de acordo com o layout) Collection<Map<String, Object>> - Esse é o mais complexo de todos; é através dele que passamos as informações que o usuário digitaria na janela de parâmetros.
- **emails** (Opcional) String – Esse parâmetro funciona semelhante ao campo E-mail da tela de Geração de arquivo EDI.
- **caminhoRepositorio** (Opcional) String – Se informado, salva o arquivo diretamente no repositório de arquivos.
- **caminhoFTP**, **enderecoFTP**, **usuarioFTP** e **senhaFTP** (Opcionais) String - Caso o arquivo deva ser disponibilizado via FTP, esses parâmetros devem ser informados.

Todos os argumentos devem ser informados utilizando o método set, que recebe dois argumentos – nome do parâmetro e valor, respectivamente, observe:

**ps.set(**"codLayout", new BigDecimal(10000));

O argumento "parâmetros" é o mais complexo pois trata-se de duas construções Java.

A primeira é uma Collection, que é literalmente uma coleção de qualquer tipo de objeto. No nosso caso, essa coleção deve ser composta de outra construção Java, a Map. Assim como a Collection, a Map também possui vários objetos, mas eles ficam mapeados e acessíveis através de uma chave. Isso é especialmente útil para o nosso exemplo, pois cada parâmetro que precisamos enviar ao serviço possui três características que devemos informar, código, nome e valor. Assim cada Map dentro da collection deverá ter esses 3 atributos.

Depois de todos os argumentos necessários, resta chamar a execução com o método ps.execute().

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#top)
