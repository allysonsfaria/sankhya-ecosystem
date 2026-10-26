---
id: "360045110273"
titulo: "Configuração Arquivo de Remessa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-10-13T15:30:05Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Layout", "Configuração Arquivo de Remessa", "PERCJURO", "br.com.sankhya.configuracao.arquivo.remessa", "Configuração Arquivo de Remessa manual", "Financeiro", "Arquivo de Remessa", "APLFANACRUDHIER", "Montagem do layout para geração bancária", "Campos e passos essenciais", "Importação exportação e opções extras", "EDI Bancário"]
---

# Configuração Arquivo de Remessa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312410968343) Módulo: Financeiro > EDI Bancário
```

---

Nessa tela, você efetuará a construção do layout do Arquivo de Remessa que será gerado pelo sistema. 

Visto que, o Arquivo de Remessa se trata de um arquivo contendo um conjunto de contas a receber que serão interpretadas pelos computadores do banco responsável; e como resultado do processamento, todo Arquivo de Remessa gera um arquivo de retorno. Dessa forma, por meio dos links a seguir, você poderá saber mais sobre os campos e funcionalidades disponíveis nessa tela:

| [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#preenchimentosiniciais) |
| --- |
| [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abacampos) |
| [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abapropriedades) |
| [Aba Detalhes para geração de arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abadetalhesparagera%C3%A7%C3%A3odearquivo) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#botooutrasopes...) |
| [Variáveis para configuração de layout de remessa bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#Vari%C3%A1veisparaconfigura%C3%A7%C3%A3odelayoutderemessabanc%C3%A1ria) |

                                                

![Imagem 2: Variáveis para configuração de layout de remessa bancária](https://ajuda.sankhya.com.br/hc/article_attachments/1500007320741)

## Preenchimentos Iniciais

Antes de iniciar a Configuração do Arquivo de Remessa, tenha em mãos o manual do banco contendo as especificações para configuração do layout. Dentro desse manual, existe uma tabela explicativa com todos os campos que deverão compor cada registro dentro do Arquivo de Remessa, essa tabela possui informações semelhantes à tela exibida acima, com a Posição Inicial e Posição Final, além do Conteúdo do campo, Tipo do Campo, Sequência, etc.

**Nota:** ao ligar o parâmetro **"Apl. filtro ana. HTML5 listener CRUD hierrquico? - APLFANACRUDHIER"** junto a um filtro personalizado nessa tela, o sistema irá buscar apenas os layouts analíticos, desse modo, não encontrará os arquivos pais na hierarquia para a exibição.

Sendo assim, no Painel Principal da tela temos os seguintes campos:

No campo **"Código"**, insira o código interno do layout que é gerado pelo sistema.

Informe o **"Título"** do layout criado.

A marcação **"Ativo"**, identificará se o registro está ou não ativo.

Efetuando a marcação **"Detalhe"**, será indicado se o registro é ou não um registro de Detalhe.

No campo **"Tamanho"**, informe o tamanho final considerando todos os campos que foram configurados no registro. O tamanho do registro identificará se o tipo de conexão será CNAB ou FEBRABAN.

Informe no campo **"Arquivo de Destino"**, a descrição do Arquivo de Remessa que será gerado pelo sistema.

O botão  ![Imagem 3: O botão "Edição" localizado ao lado direito, permite incluir variáveis na construção do nome pertinente ao Arquivo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16202774108567) **"Edição"** localizado ao lado direito, permite incluir variáveis na construção do nome pertinente ao Arquivo de Remessa, sendo que, é necessário utilizar **"{}"** para delimitar o nome da variável. Assim, considere o exemplo abaixo:

```
&{CODCTABCO}_TEXTO_&{NUMREMESSA}.txt
```

**Nota:** As informações contidas no campo Arquivo de Destino serão sobrepostas pelos dados configurados no campo **"Nome do arquivo"** presente na rotina [Geração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa).

**Observação:** Na construção de filtros, para imprimir no .txt o que for digitado no filtro (data) do EDI, é necessário colocar apenas **"Variavel(0)"**, onde (0) é a sequência da variável que você deseja imprimir no filtro informado, por exemplo:

```
( FIN.DTNEG >= [DATData Inicial]) .E.
( FIN.DTNEG <= [DATData Final] )
```

Nesse caso, esse filtro possui apenas estas duas linhas, então por isso utilizamos a Variavel(0); se fosse a segunda condição do filtro, seria **"Variavel(1)"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)

## Aba Campos

A aba Campos estará disponível somente quando um dos registros filhos do layout escolhido, estiver selecionado.

No campo **"Sequência"**, informe o código sequencial dos campos que irão compor o registro que está sendo configurado, no caso do exemplo acima, é o código sequencial dos campos do Registro Header.

Selecione em **"Tipo do campo"**, o tipo do campo que está sendo configurado conforme lista de campos disponíveis. Logo, temos as seguintes opções de definição:

- Decimal com zeros à esquerda;
- Decimal com brancos à esquerda;
- Inteiro com zeros à esquerda;
- Inteiro com brancos à esquerda;
- Alfanumérico;
- Alfanumérico com zeros à esquerda;
- Inicialização;
- Filtro.

Escolha no campo **"Conteúdo"**, a variável que preencherá o valor quando gerado o Arquivo de Remessa. Por exemplo: **Dados\_Gerais.RAZAOSOCIAL\_EMPRESA**.

No modo formulário, selecione a variável que será utilizada no campo por meio do [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213-Construtor-de-Express%C3%B5es).

Através do botão **"Assistente"**, será aberto o componente [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213-Construtor-de-Express%C3%B5es).

[GIF animado: Imagem 4: Através do botão "Assistente" , será aberto o componente Construtor de Expressões .](https://ajuda.sankhya.com.br/hc/article_attachments/4406189000599)

A função CTOF (<Texto>, <decimais>) converte texto para número real, com casas <decimais>; é utilizada no campo Conteúdo, presente na aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abacampos) e pode ser encontrada no Construtor de Expressões (Assistente); observe a sintaxe abaixo:

```
CTOF('String',QtdDecimais)
```

A String sempre deverá ser construída entre aspas simples, a QtdDecimais pode ser positiva (para arredondar casas decimais) e negativa (para arredondar o valor não decimal do número). Abaixo, temos alguns exemplos:

CTOF('123,456',1), em que 123,456 é um número com 3 casas decimais e usaremos 1 para fazer o arredondamento. Logo, o resultado após a geração do arquivo de remessa será: 123500.

CTOF('123,456',-1), em que 123,456 é um numero com 3 casas decimais e usaremos -1 para fazer o arredondamento. Assim, o resultado após a geração do arquivo de remessa será: 120000, se a QtdDecimais fosse -2, o resultado seria 100000.

O **"Conteúdo"** também pode obter uma informação **"Fixa"**, por exemplo, **"REMESSA"**. Nesse caso, o Construtor de Expressão não é utilizado, basta digitar a informação diretamente no campo Conteúdo. 

Informe o **"Tamanho"** do campo, uma vez que esse preenchimento calculará automaticamente os campos **"Posição inicial"** e **"Posição Final"**.

Em **"Quantidade de Decimais"**, informe a quantidade de decimais do campo, caso possua algum.

A Posição Inicial do campo, é calculada automaticamente quando preenchemos o campo Tamanho.

Posteriormente, temos a Posição Final do campo, que é calculada automaticamente quando o campo Tamanho é preenchido.

**Observação:** O sistema possui a variável PERCJURO, que retorna o percentual de juros de acordo com os campos Tamanho e **"Quant. Decimais"**. Ao utilizar um exemplo em que o Tamanho é **"15"** e a Quant.Decimais é igual a **"2"**, temos:

Para **0.2** > retornará **000000000000020**;

Para **0.02** > retornará **000000000000002**;

Para **5.2** > retornará **000000000000520**;

Para **8.25** > retornará **000000000000825**.

Caso seja necessário somar um ou mais dias à data de vencimento calculada na configuração do arquivo de remessa, teremos a seguinte função:

```
somaData(Object data, int nº dias)
```

Abaixo, temos o exemplo:

Utilizando a função "somaData(DATA\_VENCIMENTO\_DDMMAA,1)", o sistema buscará a data de vencimento do título e acrescentar um dia, ficando da seguinte forma:

Dt. Vencimento: 28/12/2017

No arquivo de remessa ficará: 29/12/17

**Nota:** Em relação à Data de Vencimento, você pode trabalhar com as variáveis DATA\_VENCIMENTO, DATA\_VENCIMENTO\_DDMMAA ou DATA\_VENCIMENTO\_PADRAO.

O botão ![Imagem 5: O botão "Copiar linhas de outro Layout" poderá ser acionado apenas no início da Configuração do Arquivo de Remessa .…](https://ajuda.sankhya.com.br/hc/article_attachments/16202621498903)**"Copiar linhas de outro Layout"** poderá ser acionado apenas no início da Configuração do Arquivo de Remessa. Assim, ao utilizá-lo,, será aberto o pop-up **"Copiar Layout"** para escolha do layout que terá seus dados (linhas) copiados para o novo layout em construção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)

## Aba Propriedades

Os campos e marcações dessa aba serão exibidos de acordo com a seleção dos registros na árvore hierárquica.

![Imagem 6: Os campos e marcações dessa aba serão exibidos de acordo com a seleção dos registros na árvore hierárquica.](https://ajuda.sankhya.com.br/hc/article_attachments/1500007207122)

**Observação:** Os campos abaixo só serão apresentados para o arquivo pai. São eles:

- **"Utilizar Sequência Alternativa"**;
- **"Utilizar Sequência Informada"**;
- **"Sequência Informada"**;
- **"Iniciais do arquivo para nome automático"**.

Quando a marcação **"Utiliza Sequência Alternativa"** for efetuada, fará com que o sistema utilize a **"Sequência Remessa Alternativa"** do [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) para a geração da sequência de numeração da remessa, o que possibilita o controle do número de remessa daquelas com duas sequências por conta.

A marcação **"Utiliza Sequência Informada"** trabalha em conjunto com o campo **"Sequência Informada"**, de forma que, quando estiver efetuada, você deve informar um valor numérico no campo Sequência Informada para que esse valor seja o número da próxima remessa gerada, sendo que, a cada Geração do Arquivo de Remessa ele será aumentado em um. Assim, a cada remessa gerada, o sistema gravará os dados históricos da remessa na tabela **"TGFRCI"**. Dessa forma, com a tabela populada, será possível [Desvincular uma Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#desvincularremessa) com a qual o financeiro do título possua ligação.

Ao habilitar a marcação **"Ordenar o arquivo"**, ao concluir o processamento dos registros, o sistema ordenará as linhas processadas de acordo com o conteúdo definido no campo de sequência igual a "1".

A marcação **"Primeira coluna somente p/ ordenação"** deverá ser utilizada em conjunto com a marcação Ordenar o arquivo, onde o campo definido como ordenador deve sempre ocupar a sequência 1 do arquivo e possuir o mesmo tamanho em todas as linhas do layout.

**Importante:** As funcionalidades pertinentes às marcações Ordenar o arquivo e Primeira coluna somente p/ ordenação estão disponíveis para o EDI Comercial e Financeiro.

Por padrão, o campo **"Iniciais do arquivo para nome automático"** apresenta os dizeres **"COB"** e permite um máximo de "5" (cinco) caracteres. Os dados aqui inseridos irão compor o início do nome do arquivo gerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)

## Aba Detalhes para geração de arquivo

Essa aba será apresentada somente quando a marcação Detalhe, localizada no cabeçalho da tela, estiver desligada. Seu objetivo é evitar que o EDI Bancário seja gerado utilizando o layout de uma determinada conta que não tenha sido configurada nessa aba. Acesse os links abaixo para verificar sobre cada uma das sub-aba existentes.

[Sub-aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#par%C3%A2metros)                               [Sub-aba Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#conta)                         [Sub-aba Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#empresas)

[Sub-aba Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#tiposdet%C3%ADtulo)

---

**Sub-aba Parâmetros**

![Imagem 7: Sub-aba Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/1500007208182)

Por padrão, a marcação **"Usar parâmetros informados na tela de geração"** virá habilitada e por esse motivo, estarão desabilitados todos os outros campos e as outras três Sub-abas.

**Nota:** Quando a marcação acima estiver desabilitada, será possível realizar configurações com as mesmas opções existentes na tela [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa) e vincular Conta, Empresa e Tipo de Título.

Os demais campos e marcações da sub-aba Parâmetros também serão encontrados na tela Geração Arquivo de Remessa; assim sendo, quando escolhido um layout que não possua a marcação Usar parâmetros informados na tela de geração, a Geração Arquivo de Remessa será carregada com os dados definidos na Configuração Arquivo de Remessa e terá os respectivos campos bloqueados.

Logo, quando informado um Layout que tenha a aba **"Detalhes para geração de arquivo"** configurada na Geração Arquivo de Remessa, serão desabilitadas as opções da tela de Geração e utilizadas as configurações detalhadas aqui no layout Configuração Arquivo de Remessa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

**Sub–aba Conta**

Se uma [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) for definida nessa sub-aba, no ato da Geração de Remessa, o sistema verificará se a Conta utilizada consta ou não na lista de contas; caso não esteja listada, você será avisado e o processo de [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa) não será executado. Essa validação será feita apenas se existir, no mínimo, uma conta definida na sub-aba Conta.

![Imagem 8: Se uma Conta for definida nessa sub-aba, no ato da Geração de Remessa , o sistema verificará se a Conta utilizada…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007209282)

**Observação:** Na Geração Arquivo de Remessa, após informar a Conta, o Período e o Layout, se o layout estiver com a marcação Usar parâmetros informados na tela de geração desabilitada, o sistema exibirá na grade registros em conformidade com as configurações, incluindo a Empresa e o Tipo de Título inserido no mesmo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

**Sub-aba Empresas**

A(s) Empresa(s) informada(s) nessa sub-aba serão gerados/filtrados na tela Geração Arquivo de Remessa. Caso você informe nenhuma Empresa aqui, na Geração Arquivo de Remessa serão aceitos os títulos de todas as Empresas.

![Imagem 9: A(s) Empresa(s) informada(s) nessa sub-aba serão gerados/filtrados na tela Geração Arquivo de Remessa . Caso você…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007210062)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

**Sub-aba Tipos de título**

Nessa sub-aba, você pode informar os Tipos de título que serão gerados/filtrados na Geração Arquivo de Remessa; se nenhum título for informado, na Geração Arquivo de Remessa serão aceitos os títulos correspondentes a todos os Tipos de Título.

![Imagem 10: Nessa sub-aba, você pode informar os Tipos de título que serão gerados/filtrados na Geração Arquivo de Remessa; se…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007368221)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#abadetalhesparagera%C3%A7%C3%A3odearquivo)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)

## Botão Outras Opções...

O botão Outras Opções... contém duas funcionalidades, sendo elas **"Importar Layout"** e **"Exportar Layout"**; ambas têm por objetivo facilitar a configuração dos layouts no sistema. Dado que, layouts já existentes em outras bases poderão ser importados e reutilizados, tendo a geração de economia de tempo e trabalho na confecção desses arquivos.

![Imagem 11: O botão Outras Opções... contém duas funcionalidades, sendo elas "Importar Layout" e "Exportar Layout" ; ambas têm por…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007368461)

Ao acionar a opção Importar Layout, será aberto um pop-up para upload do arquivo desejado.

De forma contrária, a opção Exportar Layout disponibiliza o layout fora do sistema para ser utilizado conforme a necessidade da Empresa. É importante citar que os arquivos que poderão ser importados ou exportados, devem ser do formato **".xml"**.

**Importante:** O layout poderá ser importado em uma base, desde que ela suporte a estrutura hierárquica desse layout. Portanto, é essencial se atentar para a configuração realizada no parâmetro **"Máscara para Intercâmbio Eletrônico de Dados (EDI) - MASCEDI"**. Por exemplo, se em uma base para a qual será feita a importação, a máscara definida no referido parâmetro é **"99\.99\.99;0"**, não será possível importar um layout que possua **"4"** (quatro) níveis hierárquicos.

**Nota:** Quando você comprar uma solução pelo Place e esta for protegida, a opção Exportar Layout ficará indisponível. 

**Observação:** Os EDI's baixados do Sankhya Place estarão criptografados por questão de segurança.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)

## Variáveis para configuração de layout de remessa bancária

As variáveis descritas abaixo podem ser utilizadas na configuração de layouts de remessa de cobrança para o banco. Confira a seguir a função de cada variável e exemplos práticos de sua aplicação:

**(1)** **NROSEQUENCIAL**: contador geral de linhas no arquivo gerado, excluindo sequências negativas (usado com frequência para ordenação). Exemplo:

```
HEADER
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 1|

DETALHE
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 2|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 3|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 4|

DETALHE 2
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 5|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 6|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 7|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 8|
```

(1)** NROSEQLOTE:** contador de linhas referente a um bloco gerado no detalhe. Exemplo:

```
HEADER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 0|

DETALHE 1
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 1|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 2|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 3|

DETALHE 2
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 1|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 2|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 3|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQLOTE = 0|
```

(1)** SEQUENCIALOTE:** contador de blocos gerados nos detalhes do arquivo. Exemplo:

```
HEADER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 0|

DETALHE 1
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 1|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 1|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 1|

DETALHE 2
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 2|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 2|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 2|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |SEQUENCIALOTE = 0|
```

**(1)** **TOTAL135:** essa variável realiza a soma das linhas geradas no detalhe e adiciona 2 ao valor total. Exemplo:

```
HEADER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE + 2)|

DETALHE 1
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE  + 2)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE  + 2)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE  + 2)|

DETALHE 2
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE + 2)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE + 2)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE + 2)|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL135 = 8 (6 LINHAS
 DE DETALHE + 2)|
```

(1)** TOTAL01359:** soma todas as linhas geradas no DETALHE, adicionando um valor fixo de 4 ao total. Exemplo:

```
HEADER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|

DETALHE 1
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|

DETALHE 2
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |TOTAL01359 = 10 (6
LINHAS DE DETALHE + 4)|
```

(1)** TOTALGERAL:** contador de todas as linhas geradas no arquivo. Exemplo:

```
HEADER
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 1|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 2|

DETALHE
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 3|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 4|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 5|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 6|

DETALHE 2
-123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 7|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 8|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 9|
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 10|

TRAILLER
123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC123ABC |NROSEQUENCIAL = 11|
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa#top)
