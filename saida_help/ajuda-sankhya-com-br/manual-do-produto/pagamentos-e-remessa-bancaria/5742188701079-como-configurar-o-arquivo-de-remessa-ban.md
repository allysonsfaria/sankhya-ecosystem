---
id: "5742188701079"
titulo: "Como configurar o arquivo de remessa bancária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Pagamentos e Remessa Bancária"
atualizado_em: "2026-10-02T17:51:58Z"
rotulos: ["Configuração", "Arquivo de Destino", "MASCEDI", "Layout", "Construtor de Expressões", "Financeiro", "Arquivo de Remessa", "Arquivo de Retorno", "Geração Arquivo de Remessa", "Sankhya Place", "ID: br.com.sankhya.rh.configuracao.arquivo.de.remessa", "Configuração de Arquivo Remessa", "Instalação Pacotes Sankhya Place", "Importação e exportação de layouts em XML", "EDI Bancários"]
---

# Como configurar o arquivo de remessa bancária

```
 Módulo: Pessoal+ > EDI Bancários         Versão disponível: A partir da 4.12
```

---

Nesta tela será efetuada a construção do layout do Arquivo de Remessa que será gerado pelo sistema. 

O Arquivo de Remessa se trata de um documento contendo um conjunto de contas a receber que serão interpretadas pelos computadores do banco responsável; e como resultado do processamento, todo Arquivo de Remessa gera um arquivo de retorno. Dessa forma, por meio dos links a seguir, poderá saber mais sobre os campos e funcionalidades disponíveis nessa tela:

| Funcionalidades da tela | |
| --- | --- |
| [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#preenchimentosiniciais) | [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abacampos) |
| [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abapropriedades) | [Aba Detalhes para geração de arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abadetalhesparagera%C3%A7%C3%A3odearquivo) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#botooutrasopes...) |  |

---

![Imagem 1: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/16832634306071)

### Preenchimentos Iniciais

![Imagem 2: Antes de iniciar a Configuração de Arquivo de Remessa , tenha em mãos o manual do banco contendo as especificações para…](https://ajuda.sankhya.com.br/hc/article_attachments/16540353204119) Antes de iniciar a Configuração de Arquivo de Remessa, tenha em mãos o manual do banco contendo as especificações para configuração do layout. Dentro desse manual, existe uma tabela explicativa com todos os campos que deverão compor cada registro dentro do Arquivo de Remessa, essa tabela possui informações semelhantes à tela exibida acima, com a Posição Inicial e Posição Final, além do Conteúdo do campo, Tipo do Campo, Sequência, entre outros.

Ao incluir um novo EDI nesta tela, este poderá ser inserido no conceito do [Sankhya Place](https://ajuda.sankhya.com.br/hc/pt-br/articles/4422517129623). Para isso, é necessário habilitar a marcação **"Permite instalar pacote Sankhya Place?"** da tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana) e, em seguida, ao clicar no botão ![Imagem 3: Ao incluir um novo EDI nesta tela, este poderá ser inserido no conceito do Sankhya Place . Para isso, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/16832738775063) **"Cadastrar Formatador de Remessa"** para a inclusão de um EDI, será apresentado o pop-up **"Buscar soluções no Sankhya Place"** com as soluções disponíveis no Sankhya Place. 

Desse modo, defina o pacote que deseja efetuar o download e verifique se a solução é gratuita ou paga.

A saber:

#### Soluções gratuitas

Caso queira instalar uma solução gratuita, basta clicar em **"Instalar"** e aceitar os termos de uso da loja de soluções. 

[GIF animado: Imagem 4: Caso queira instalar uma solução gratuita, basta clicar em "Instalar" e aceitar os termos de uso da loja de soluções.](https://ajuda.sankhya.com.br/hc/article_attachments/16832815373975)

![Imagem 5: Obtenha mais informações sobre o termo de uso, por meio do link Termos e Condições da Loja de Soluções .](https://ajuda.sankhya.com.br/hc/article_attachments/16832859242135) Obtenha mais informações sobre o termo de uso, por meio do link [Termos e Condições da Loja de Soluções](https://docs.google.com/document/d/1K8BsOODBj7rxvUf-x10ktNmBRptHbOcr-9t2KAOwxaY/edit).

#### Soluções pagas

Antes de iniciar a instalação do pacote pago, é importante ressaltar que o usuário responsável pela aquisição do respectivo pacote deverá realizar o login com o Sankhya ID. Através desse usuário o sistema identificará quem é o parceiro/CNPJ responsável por essa aquisição.

Desse modo, é de extrema importância atentar-se aos usuários que terão permissão para executar o download de pacotes no Place. Para tal, acesse a tela Usuários, aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana) e verifique a configuração da marcação Permite instalar pacote Sankhya Place?.

Agora, para realizar o download da solução, clique em **"Instalar"**, assim, será apresentado um pop-up com as informações do pedido. Para concluir a compra é necessário aceitar as seguintes condições:

**“Estou ciente que ao confirmar, o pacote será imediatamente instalado no sistema e será gerado uma fatura no valor de R$ XX,XX para minha empresa.”**

**“Estou ciente e de acordo com os termos de uso da loja de soluções.”**

[GIF animado: Imagem 6: “Estou ciente e de acordo com os termos de uso da loja de soluções.”](https://ajuda.sankhya.com.br/hc/article_attachments/8101359650455)

Ao clicar em **"Sim, confirmar"**, a aquisição/download é realizada e será disparado um BI para o mesmo e-mail cadastrado para recebimento de boletos de cobrança mensal de uso do sistema **Sankhya**. Nesse e-mail serão enviados o boleto e NFS-e referentes ao valor do pacote adquirido. O boleto, em sua maioria, é gerado com o vencimento até sete dias após a data do download do pacote.

Caso queira inserir de um novo registro fora deste contexto, clique no botão **"Cadastrar EDI"** do pop-up. 

![Imagem 7: Caso queira inserir de um novo registro fora deste contexto, clique no botão "Cadastrar EDI" do pop-up.](https://ajuda.sankhya.com.br/hc/article_attachments/16833253827735)

No Painel Principal da tela tem-se os seguintes campos:

No campo **"Código"**, insira o código interno do layout que é gerado pelo sistema.

Informe o **"Título"** do layout criado.

A marcação **"Ativo"**, identificará se o registro está ou não ativo.

Efetuando a marcação **"Detalhe"**, será indicado se o registro é ou não um registro de Detalhe.

No campo **"Tamanho"**, informe o tamanho final considerando todos os campos que foram configurados no registro. O tamanho do registro identificará se o tipo de conexão será CNAB ou FEBRABAN.

As informações contidas no campo **"Arquivo de Destino"** serão sobrepostas pelos dados configurados no campo **"Nome do arquivo"** presente na rotina [Geração Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa).

O botão ![Imagem 8: O botão "Construtor nome arquivo" localizado ao lado direito do campo acima, permite incluir variáveis na construção do…](https://ajuda.sankhya.com.br/hc/article_attachments/16833380503831) **"Construtor nome arquivo"** localizado ao lado direito do campo acima, permite incluir variáveis na construção do nome pertinente ao Arquivo de Remessa, sendo que, é necessário utilizar **"{}"** para delimitar o nome da variável. Assim, considere o exemplo abaixo:

```
&{CODCTABCO}_TEXTO_&{NUMREMESSA}.txt
```

**Observação:** na construção de filtros, para imprimir no .txt o que for digitado no filtro (data) do EDI, é necessário colocar apenas **"Variavel(0)"**, onde (0) é a sequência da variável que deseja imprimir no filtro informado, por exemplo:

```
( FIN.DTNEG >= [DATData Inicial]) .E.
( FIN.DTNEG <= [DATData Final] )
```

Nesse caso, esse filtro possui apenas estas duas linhas, então por isso utiliza-se a Variavel(0); se fosse a segunda condição do filtro, seria **"Variavel(1)"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#top)

### Aba Campos

Esta aba estará disponível somente quando um dos registros filhos do layout escolhido, estiver selecionado.

No campo **"Sequência"**, informe o código dos campos que irão compor o registro que está sendo configurado, no caso do exemplo acima, é o código sequencial dos campos do Registro Header.

Selecione o **"Tipo do Campo"** que está sendo configurado conforme lista de campos disponíveis dentre as seguintes opções:

- Inicialização;
- Filtro;
- Inteiro com brancos à esquerda;
- Inteiro com zeros à esquerda;
- Alfanumérico;
- Alfanumérico com zeros à esquerda;
- Decimal com brancos à esquerda;
- Decimal com zeros à esquerda.

Escolha a variável que preencherá o valor no campo **"Conteúdo"**, quando gerado o Arquivo de Remessa. Por exemplo: **Dados\_Gerais.RAZAOSOCIAL\_EMPRESA**.

No modo formulário, selecione a variável que será utilizada no campo por meio do botão**"Assistente"**, através do componente [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213-Construtor-de-Express%C3%B5es).

[GIF animado: Imagem 9: No modo formulário, selecione a variável que será utilizada no campo por meio do botão "Assistente" , através do…](https://ajuda.sankhya.com.br/hc/article_attachments/15450408385431)

A função CTOF (<Texto>, <decimais>) converte texto para número real, com casas <decimais>; é utilizada no campo Conteúdo, presente na aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abacampos) e pode ser encontrada no Construtor de Expressões (Assistente); observe a sintaxe abaixo:

```
CTOF('String',QtdDecimais)
```

A String sempre deverá ser construída entre aspas simples, a QtdDecimais pode ser positiva (para arredondar casas decimais) e negativa (para arredondar o valor não decimal do número). Abaixo, tem-se alguns exemplos:

**1** - CTOF('123,456',1), em que 123,456 é um número com 3 casas decimais e usaremos 1 para fazer o arredondamento. Logo, o resultado após a geração do arquivo de remessa será: 123500.

**2** - CTOF('123,456',-1), em que 123,456 é um numero com 3 casas decimais e usaremos -1 para fazer o arredondamento. Assim, o resultado após a geração do arquivo de remessa será: 120000, se a QtdDecimais fosse -2, o resultado seria 100000.

O Conteúdo também pode obter uma informação **"Fixa"**, por exemplo, **"REMESSA"**. Nesse caso, o Construtor de Expressão não é utilizado, basta digitar a informação diretamente no referido campo. 

Informe o **"Tamanho"** do campo, uma vez que esse preenchimento calculará automaticamente os campos **"Posição inicial"** e **"Posição Final"**.

Em **"Quant. Decimais"**, informe a quantidade de decimais do campo, caso possua algum.

**Observação:** o sistema possui a variável PERCJURO, que retorna o percentual de juros de acordo com os campos Tamanho e Quant. Decimais. Ao utilizar um exemplo em que o Tamanho é **"15"** e a Quant. Decimais é igual a **"2"**, tem-se:

Para **0.2** > retornará **000000000000020**;

Para **0.02** > retornará **000000000000002**;

Para **5.2** > retornará **000000000000520**;

Para **8.25** > retornará **000000000000825**.

Caso seja necessário somar um ou mais dias à data de vencimento calculada na configuração do arquivo de remessa, tem-se a seguinte função:

```
somaData(Object data, int nº dias)
```

Abaixo, segue o exemplo:

Utilizando a função "somaData(DATA\_VENCIMENTO\_DDMMAA,1)", o sistema buscará a data de vencimento do título e acrescentar um dia, ficando da seguinte forma:

Dt. Vencimento: 28/12/2017

No arquivo de remessa ficará: 29/12/17

**Nota:** em relação à Data de Vencimento, poderá trabalhar com as variáveis DATA\_VENCIMENTO, DATA\_VENCIMENTO\_DDMMAA ou DATA\_VENCIMENTO\_PADRAO.

O botão**"Copiar linhas de outro Layout"** poderá ser acionado apenas no início da Configuração do Arquivo de Remessa. Assim, ao utilizá-lo, será aberto o pop-up **"Copiar Layout"** para escolha do layout que terá seus dados (linhas) copiados para o novo layout em construção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#top)

### Aba Propriedades

Os campos e marcações desta aba serão exibidos de acordo com a seleção dos registros na árvore hierárquica.

![Imagem 10: Os campos e marcações desta aba serão exibidos de acordo com a seleção dos registros na árvore hierárquica.](https://ajuda.sankhya.com.br/hc/article_attachments/16832634306071)

Os campos e marcações abaixo só serão apresentados para o arquivo pai. São eles:

- Utilizar Sequência Alternativa;
- Utilizar Sequência Informada;
- Sequência Informada;
- Iniciais do arquivo para nome automático.

Quando a marcação Utilizar Sequência Alternativa for efetuada, fará com que o sistema utilize a **"Sequência Remessa Alternativa"** do [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) para a geração da sequência de numeração da remessa, o que possibilita o controle do número de remessa daquelas com duas sequências por conta.

A marcação Utilizar Sequência Informada trabalha em conjunto com o campo Sequência Informada, de forma que, quando estiver realizada, deverá informar um valor numérico no campo Sequência Informada para que esse valor seja o número da próxima remessa gerada, sendo que, a cada Geração do Arquivo de Remessa ele será aumentado em um. Assim, a cada remessa gerada, o sistema gravará os dados históricos da remessa na tabela **"TGFRC"**.

Lembre-se ainda que a numeração do campo acima será sequencial conforme o valor máximo informado no campo **"Nro máx. p/ seq. remessa"**da aba [Intercâmbio Eletrônico de Dados (EDI)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113#abaintercmbioeletrnicodedadosedi) da tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113), ou seja, ao atingir esse limite o próximo valor será 1001, 1002, e assim por diante, desde que sejam limitados a 9 caracteres.

Ao habilitar a marcação **"Ordenar o arquivo"**, ao concluir o processamento dos registros, o sistema ordenará as linhas processadas de acordo com o conteúdo definido no campo de sequência igual a "1".

A marcação **"Primeira coluna somente p/ ordenação"** deverá ser utilizada em conjunto com a marcação Ordenar o arquivo, onde o campo definido como ordenador deve sempre ocupar a sequência 1 do arquivo e possuir o mesmo tamanho em todas as linhas do layout.

**Importante:** as funcionalidades pertinentes às marcações Ordenar o arquivo e Primeira coluna somente p/ ordenação estão disponíveis para o EDI Comercial e Financeiro.

Quando efetuar a marcação **"Gerar um arquivo p/cada linha"**, terá a obtenção de cada linha. Se a geração do arquivo for realizada com a referida marcação feita, se existirem vários itens em uma mesma nota e os arquivos ficarem com o mesmo nome, o sistema os agrupará automaticamente, e gerará todos os itens da nota em um mesmo arquivo.

**Nota:** essa funcionalidade só agrupará os arquivos caso os registros estejam no mesmo nível; em níveis diferentes, o sistema sobrescreve o conteúdo dos arquivos.

Por padrão, o campo Iniciais do arquivo para nome automático apresenta os dizeres **"COB"** e permite um máximo de cinco caracteres. Os dados aqui inseridos irão compor o início do nome do arquivo gerado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#top)

### Aba Detalhes para geração de arquivo

Esta aba será apresentada somente quando a marcação Detalhe, localizada no cabeçalho da tela, estiver desligada. Seu objetivo é evitar que o EDI Bancário seja gerado utilizando o layout de uma determinada conta que não tenha sido configurada nessa aba. Acesse os links abaixo para verificar sobre cada uma das sub-abas existentes.

| [Sub-aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#par%C3%A2metros) | [Sub-aba Contas para geração](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#contasparageracao) |
| --- | --- |
| [Sub-aba Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#tiposdet%C3%ADtulo) | [Sub-aba Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#empresas) |

---

#### Sub-aba Parâmetros

![Imagem 11: Sub-aba Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/16834027961111)

Por padrão, a marcação **"Usar parâmetros informados na tela de geração"** virá habilitada e por esse motivo, estarão desabilitados todos os outros campos e as outras três sub-abas.

**Nota:** quando a marcação acima estiver desabilitada, será possível realizar configurações com as mesmas opções existentes na tela [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa) e vincular Conta, Empresa e Tipo de Título.

A **Situação** determina quais títulos participarão da remessa:

- **Pendentes** - títulos em aberto, ainda não vencidos ou vencidos mas não liquidados;
- **Baixados** - títulos já pagos/recebidos;
- **Ambos** - inclui tanto pendentes quanto baixados.

O campo **Tipo** diferencia qual tipo de remessa será gerada entre **Títulos a Receber** (Receita) e **Títulos a Pagar** (Despesa).

A opção **Remessa vazia** permite gerar remessa mesmo sem títulos (arquivo vazio). Útil para confirmação de layouts e fluxos.

A opção **Nosso Número preenchido** indica se os títulos já possuem número de nosso número (identificação do título no banco).

- quando **marcada**:
  - desabilita opção **Gerar Nosso Número**;
  - assume que títulos já têm identificação.
- quando **desmarcada**:
  - permite habilitação de geração automática de nosso número;
  - permite que o sistema crie novos identificadores.

A opção **Nosso Número:**

- quando **marcada:** gera automaticamente números de **Nosso Número** para títulos que não possuem utilizando a sequência do banco.
- quando **desmarcada**: utiliza números já existentes nos títulos e assume que títulos já foram identificados.

A opção **Registrar Banco da Conta** associa títulos ao banco e conta utilizados na geração da remessa.

A opção **Gerar Linha Digitável** gera a linha digitável do boleto (sequência numérica lida por leitora óptica) em formato padrão: dígitos separados em grupos específicos.

A opção **Agrupar pagamentos**:

- quando marcada:

  - agrupa múltiplos pagamentos do mesmo parceiro/conta;
  - reduz quantidade de registros no arquivo;
  - consolida valores;
  - exibe mensagem: "Vamos agrupar pagtos do mesmo parceiro!"
- quando desmarcada:

  - cada título gera um registro separado no arquivo;
  - aumenta tamanho do arquivo.

Os campos e marcações desta sub-aba também serão encontrados na tela Geração Arquivo de Remessa; assim sendo, quando escolhido um layout que não possua a marcação Usar parâmetros informados na tela de geração, a Geração Arquivo de Remessa será carregada com os dados definidos na Configuração Arquivo de Remessa e terá os respectivos campos bloqueados.

Logo, quando informado um Layout que tenha a aba **"Detalhes para geração de arquivo"** configurada na Geração Arquivo de Remessa, serão desabilitadas as opções da tela de Geração e utilizadas as configurações detalhadas aqui no layout Configuração Arquivo de Remessa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

#### Sub–aba Contas para geração

Se uma [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) for definida nesta sub-aba, no ato da Geração de Remessa, o sistema verificará se a Conta utilizada consta ou não na lista de contas; caso não esteja listada, você será avisado e o processo de [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115613-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa) não será executado. Essa validação será feita apenas se existir, no mínimo, uma conta definida nesta sub-aba.

![Imagem 12: Se uma Conta for definida nesta sub-aba, no ato da Geração de Remessa , o sistema verificará se a Conta utilizada…](https://ajuda.sankhya.com.br/hc/article_attachments/16834272187671)

**Observação:** na Geração Arquivo de Remessa, após informar a Conta, o Período e o Layout, se o layout estiver com a marcação Usar parâmetros informados na tela de geração desabilitada, o sistema exibirá na grade registros em conformidade com as configurações, incluindo a Empresa e o Tipo de Título inserido no mesmo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

#### Sub-aba Empresas

A(s) **"Empresa"**(s) informada(s) nesta sub-aba serão geradas/filtradas na tela Geração Arquivo de Remessa. Caso não seja informada nenhuma Empresa aqui, na Geração Arquivo de Remessa serão aceitos os títulos de todas as Empresas.

![Imagem 13: A(s) "Empresa" (s) informada(s) nesta sub-aba serão geradas/filtradas na tela Geração Arquivo de Remessa . Caso não…](https://ajuda.sankhya.com.br/hc/article_attachments/16834387581847)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abadetalhesparagera%C3%A7%C3%A3odearquivo)

---

#### Sub-aba Tipos de título

Nesta sub-aba, pode-se informar os **"Tipos de título"** que serão gerados/filtrados na Geração Arquivo de Remessa; se nenhum título for informado, na Geração Arquivo de Remessa serão aceitos os títulos correspondentes a todos os Tipos de Título.

![Imagem 14: Nesta sub-aba, pode-se informar os "Tipos de título" que serão gerados/filtrados na Geração Arquivo de Remessa ; se…](https://ajuda.sankhya.com.br/hc/article_attachments/16834454007447)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#abadetalhesparagera%C3%A7%C3%A3odearquivo) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#top)

### Botão Outras Opções...

O botão ![Imagem 15: O botão "Outras Opções..." contém duas funcionalidades, sendo elas "Importar Layout" e "Exportar Layout" ; ambas têm…](https://ajuda.sankhya.com.br/hc/article_attachments/16834473548055) **"Outras Opções..."** contém duas funcionalidades, sendo elas **"Importar Layout"** e **"Exportar Layout"**; ambas têm por objetivo facilitar a configuração dos layouts no sistema. Dado que, layouts já existentes em outras bases poderão ser importados e reutilizados, tendo a geração de economia de tempo e trabalho na confecção desses arquivos.

![Imagem 16: O botão "Outras Opções..." contém duas funcionalidades, sendo elas "Importar Layout" e "Exportar Layout" ; ambas têm…](https://ajuda.sankhya.com.br/hc/article_attachments/16834554629143)

Ao acionar a opção Importar Layout, será aberto um pop-up para upload do arquivo desejado.

De forma contrária, a opção Exportar Layout disponibiliza o layout fora do sistema para ser utilizado conforme a necessidade da Empresa. É importante citar que os arquivos que poderão ser importados ou exportados, devem ser do formato **".xml"**.

**Importante:** o layout poderá ser importado em uma base, desde que ela suporte a estrutura hierárquica desse layout. Portanto, é essencial se atentar para a configuração realizada no parâmetro **"Máscara para Intercâmbio Eletrônico de Dados (EDI) - MASCEDI"**. Por exemplo, se em uma base para a qual será feita a importação, a máscara definida no referido parâmetro é **"99\.99\.99\.9;0"**, não será possível importar um layout que possua quatro níveis hierárquicos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079-Como-configurar-o-arquivo-de-remessa-banc%C3%A1ria#top)
