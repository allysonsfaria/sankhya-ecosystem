---
id: "44011891382039"
titulo: "Como cadastrar produto normal sem variação?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011891382039-Como-cadastrar-produto-normal-sem-varia%C3%A7%C3%A3o"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:48Z"
rotulos: ["sync_hc", "magis5", "sync_hash_34d8f2dbd776", "magis5_204055239683"]
---

# Como cadastrar produto normal sem variação?

Para criar um produto normal, “Sem Variação”, siga os passos abaixo:

No menu superior, clique em **Cadastros → Produtos**:

![d1-2](https://ajuda.sankhya.com.br/hc/article_attachments/44011845644695)

No módulo de produtos, clique em **“Novo Produto”**.

![d2-1](https://ajuda.sankhya.com.br/hc/article_attachments/44011891740951)

Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e automática, cujo código é **único e não editável**.

O módulo de produtos é separado por abas, sendo cada uma delas responsável por uma área específica.

---

## INFORMAÇÕES BÁSICAS

![d3-1](https://ajuda.sankhya.com.br/hc/article_attachments/44011860819351)

- **Tipo de Produto:** Selecione **“Normal”**;

- **Subtipo do Produto:**
  - **Matéria Prima**: Se o produto que está cadastrando for um item utilizado na composição de outro produto, ou seja, a matéria prima, selecione essa opção;
  - **Material de Embalagem**: Caso seja a embalagem de um produto, selecione essa opção.

Para produtos finais, não selecione nenhuma das opções.

No cadastro de uma pizza, por exemplo:

- Os ingredientes utilizados na produção da pizza são matéria prima (queijo, tomate, farinha, ovo, etc);
- A caixa utilizada para embalar a pizza é o material de embalagem;
- O produto “Pizza” é o produto final, ou seja, neste caso, não é selecionada nenhuma das duas opções.

- **Peso Líquido (Un. Com.):** É o peso líquido do produto (desconsiderando o peso da embalagem);

- **Possui Variações:** Selecione “não”. Para cadastrar um produto normal com variações, [clique aqui](https://ajuda.artemis5.com.br/como-cadastrar-produto-normal-com-variacao/);

- **Código de Barras:** Insira o código de barras do produto;

Obs: Em casos em que o  estabelecimento recebe a caixa mas a  venda é realizada na unidade, é possível realizar a conversão da caixa para a unidade, vinculando o produto unitário à caixa.

Neste caso, é preciso cadastrar o produto unitário antes de cadastrar a caixa do produto.

Feito isso, ao cadastrar a caixa do produto, em “**Produto Unitário**”, clicar na lupa, **buscar pelo produto unitário**, selecioná-lo e em “**Qtd Unidades”**, informar a quantidade de itens que a caixa possuirá.

![d4-2](https://ajuda.sankhya.com.br/hc/article_attachments/44011892003095)

- **Descrição do Produto:** É o nome do produto utilizado para identificação interna. Este campo é obrigatório;

- **Tamanho:** Caso o produto **tenha um tamanho, clique em “Select an Option”** e selecione-o. Se não localizar a opção desejada, é porque ainda não foi cadastrada no **Artemis5**, então, será necessário cadastrá-la. Para isso, **clique em (+) ao lado de “Tamanho”**, preencha o campo “**Tamanho”** e clique em **“Salvar”**;

Observação: Antes de cadastrar um novo tamanho, verifique se já não consta o tamanho cadastrado, por exemplo: **'60 Caps'** é diferente de **'60Caps'**.

![d5](https://ajuda.sankhya.com.br/hc/article_attachments/44011883442711)

- **Sabor/Cor:** Caso o produto tenha um sabor ou uma cor, clique em **“Select an Option”** e selecione-o. Se não localizar a opção desejada, é porque ainda não foi cadastrada no **Artemis5**, então, será necessário cadastrá-la. Para isso, **clique em (+) ao lado de “Tamanho”**, preencha o campo “**Tamanho”** e clique em **“Salvar”**;

![d6](https://ajuda.sankhya.com.br/hc/article_attachments/44011869784343)

- **Código GTIN:** É o código de barras universal do produto. Para que o código GTIN conste na Nota Fiscal Eletrônica, deverá obedecer o padrão brasileiro, iniciando em 7898 ou 7896. Qualquer código iniciado com números diferentes não será exibido no XML da Nota Fiscal. Caso coloque um código iniciando em 7898 ou 7896 mas o restante do código esteja incorreto, acarretará em um erro de transmissão da Nota Fiscal. É recomendável que o código de barras seja o mesmo do código GTIN.

**Se o código não for preenchido, o campo sairá em branco.**

- **Nome de Exibição (PDV):** É o nome do produto que será exibido no módulo de frente de caixa (PDV) ao cliente;

## EMPREENDIMENTOS

O empreendimento que o usuário está logado vem selecionado por padrão. Caso o lojista possua mais de um empreendimento, é possível compartilhar o cadastro do produto entre eles, evitando a necessidade de refazer o cadastro e agilizando o processo.

Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em **“(+) Incluir”** e selecione os empreendimentos desejados:

![d7](https://ajuda.sankhya.com.br/hc/article_attachments/44011869929367)

- **Categoria:** Cada produto poderá ser inserido em apenas uma categoria por empreendimento. Porém, é possível inserir esse produto em categorias diferentes em cada empreendimento;

- **Ativo:** Informa se este produto estará habilitado ou não no empreendimento. O produto pode estar ativo em um empreendimento e desativado em outro;

- **ID Externo:** Utilizado em clientes que possuem uma base de dados já existente (seja em marketplaces ou na migração de outro ERP) e inicie a utilização do **Artemis5**. Esse ID Externo servirá para que o produto não perca a referência do produto antigo e não perca a relevância dos anúncios. Cada empreendimento pode ter um código distinto;

- **Estoque Mínimo:** O preenchimento deste campo reflete no “Relatório de Produtos c/ Estoque Mínimo”, onde é exibido um alerta no momento que o estoque atinge o mínimo preenchido no cadastro do produto informando que o produto está abaixo do necessário para a operação do estabelecimento. Caso não queira ter esse controle neste produto, basta não preencher o campo. É possível definir uma quantidade mínima para cada estabelecimento;

![d8](https://ajuda.sankhya.com.br/hc/article_attachments/44011870055319)

## PREÇO

Cada empreendimento pode ter sua tabela de preços, sendo possível que cada empreendimento tenha até quatro tabelas de preços diferentes, sendo elas: “Atacado”, “Intermediário 1”, ”Intermediário 2” e “Varejo”. A definição de quais tabelas o empreendimento irá utilizar é definida na implantação do **Artemis5**, podendo ser alterado nas configurações de cada empreendimento.

![d9](https://ajuda.sankhya.com.br/hc/article_attachments/44011870158487)

A aplicação do preço final ao cliente é definida no cadastro do cliente ou pelo vendedor na hora da venda (caso o vendedor possua a permissão necessária);

- **%:** É a porcentagem de lucro sobre o preço de custo do produto. O preenchimento deste campo calcula automaticamente o valor de venda do produto com base na porcentagem informada e preenche a coluna (R$);

- **R$**: É o valor de venda do produto que será cobrado do cliente final. O preenchimento deste campo calcula automaticamente a porcentagem de lucro que este produto terá com base no preço informado e preenche a coluna (%);

- **% Desc. Máx:** Sobrepõe qualquer outro desconto que o produto possa ter. É a porcentagem de desconto máximo a ser disponibilizado para o produto. O valor inserido neste campo implica na liberação de desconto para o produto no ato da compra. Por exemplo:
  - Situação 1: O produto tem um desconto máximo de 20%, porém, um vendedor deseja aplicar um desconto superior.  A venda é travada e o desconto só é aplicado após alteração no cadastro do produto ou a correção do desconto;
  - Situação 2: O campo “Desc. Máx” não está preenchido, consequentemente o produto não possui um limite de desconto. Porém, o vendedor que está realizando a venda só tem permissão para aplicar uma porcentagem fixa de desconto. Caso  ele queira aplicar um desconto maior, será necessário que alguém com uma permissão superior libere o desconto.

## ESTOQUE

É possível controlar o estoque dos produtos ao adicionar, remover ou até mesmo corrigi-los através de um inventário.

![d10](https://ajuda.sankhya.com.br/hc/article_attachments/44011870247959)

- **Controlar Estoque:** Selecione “Sim” caso haja controle de estoque do produto;

- **Unidade de Medida:**Selecione a unidade de medida correspondente;

- **Unidade:** É utilizado para produtos unitários;

- **Fração:** É utilizado em casos que são vendidas partes de um produto (unidades fracionadas).

- **Qtd. Múltipla:** É utilizado em situações onde há mais de um empreendimento e esses empreendimentos realizam transferências entre si. As solicitações de transferência deverão respeitar este campo, uma vez que o número informado será utilizado como parâmetro: se estiver marcado 10, não será possível pedir 15 unidades, já que 15 não é múltiplo de 10.

- **Depósito:** Utilizado para realizar movimentações no estoque, sendo entrada ou saída de produtos além de ajustes de estoque (através do inventário, baixa manual ou entrada de estoque). Para habilitar este campo, é necessário salvar o produto e depois, acessar o cadastro do produto novamente.

É possível ajustar o estoque de vários depósitos na mesma tela desde que os depósitos estejam compartilhados com o empreendimento que você está logado.

Ao selecionar o depósito, informe qual será o tipo de movimentação, quantidade de itens e clique em “Movimentar”. Após clicar em “Movimentar”, o estoque anterior será ajustado.

Para efetuar este procedimento, selecione a opção abaixo e informe em qual será o depósito que irá realizar a alteração:

![d11](https://ajuda.sankhya.com.br/hc/article_attachments/44011861793175)

A movimentação de estoque só poderá ser realizada por usuários com a devida permissão.

- **Tipo de movimentação:** Informa qual será a movimentação a ser realizada, sendo elas:

- **Inventário:** É a substituição do produto do depósito selecionado.

- **Entrada:** É a adição de produtos ao depósito selecionado. Ele é somado a quantidade atual de produtos.

- **Saída:** É a retirada de produtos ao depósito selecionado. O valor informado é removido da quantidade atual de produtos. É possível informar os motivos pelo qual está removendo os produtos, desde que esses motivos sejam cadastrados anteriormente. Para realizar este procedimento, clique aqui (tutorial de criação de motivos de saída)

- **Data de Validade:** Caso o estabelecimento controle os produtos por data de validade, a data de validade do produto deverá ser informada neste campo.

- **Qtd.:** Quantidade de produtos que serão adicionados ao depósito selecionado.

Obs: Após movimentar o primeiro depósito, pode-se selecionar outro depósito e realizar o mesmo procedimento.

## FORNECEDORES

Utilizado na elaboração da lista de cotação. Um produto pode possuir mais de um fornecedor com conversões diferentes, por exemplo: O fornecedor A vende o pack de água com 12 unidades e o fornecedor B vende o pack da mesma água com 6 unidades.

 É necessário preencher este campo para informar quais são os fornecedores deste produto.

Para informar os fornecedores do produto, basta clicar em “Incluir” e selecioná-los. A seguir, preencha as seguintes informações:

- **Un. Medida de Compra:** É a maneira que esse produto é vendido, seja em peso (quilograma, grama), unidade, dezena, peça, pacote, etc. É necessário o preenchimento deste campo para habilitar o “Fator de Conversão” (explicado abaixo);

- **Qtd. Min. Compra:** Neste campo é informado o mínimo de unidades que o fornecedor vende deste produto;

Além desses campos, há também a possibilidade de cadastrar as conversões deste produto. Para isso, clique em **"Conversões"** e preencha os campos seguintes:

![d12](https://ajuda.sankhya.com.br/hc/article_attachments/44011892936727)

- **Código Interno do Fornecedor:** É o código de identificação do produto descrito na Nota Fiscal de Compra (normalmente chamado de SKU) utilizado para alimentar o estoque ao realizar a leitura da Nota Fiscal no processo de Entrada de Estoque (amarrar link).

- **Unidade Comercial:** É o modo que é vendido esse produto (seja em lote, quilo, litros, etc);

- **Unidade Tributável:** Não é possível editar este campo nesta tela. Para editá-lo, selecione a aba **“Fiscal”** e altere o campo **“Uni Comercial”**.

- **Fator de Conversão:**
  - **Divisão:** É utilizado quando o empreendimento adquire um produto e divide esse produto em dois ou mais produtos para comercializá-lo. 
    Exemplo: O lojista adquiriu uma caixa com 30 unidades de um produto e dividiu essa caixa em 3 pacotes com 10 unidades para venda. Em **Qtd. de Conversão** deve ser informado o número 10, visto que, ao realizar a entrada da Nota Fiscal, o estoque será alimentado em 3 unidades deste produto.
  - **Multiplicação:** Utilizado em situações onde o empreendimento adquire um produto em caixa e vende o produto unitário. Ao realizar a leitura da Nota Fiscal, o **Artemis5** irá identificar que entrou uma caixa no estoque, porém, apenas a quantidade de produtos que compõem a caixa será acrescida ao estoque. 
    Exemplo: O lojista adquiriu uma caixa com 30 unidades de um produto. Em **Qtd. de Conversão** deve ser informado o número 30, visto que, ao realizar a entrada da Nota Fiscal, o estoque será alimentado em 30 unidades deste produto.

Obs: É possível ter mais de uma unidade de conversão por produto, visto que pode-se comprar tamanhos diferentes de caixa do mesmo fornecedor.

## INFORMAÇÕES COMPLEMENTARES

![d13](https://ajuda.sankhya.com.br/hc/article_attachments/44011862055447)

- **Fabricante:** Informe qual a marca do produto;

- **Peso Bruto (Kg):** Informe o peso do produto (considere o peso da embalagem exibida no rótulo do produto);

- **Largura do Pacote:** Informe a largura do produto (em centímetros);

- **Altura do Pacote:** Informe a altura do produto (em centímetros);

- **Profundidade do Pacote:** Informe a profundidade do produto (em centímetros);

- **Natureza:** Informe a classificação do produto dentro do plano de contas;

- **Garantia (Meses):** Caso seja oferecida uma garantia pelo produto, informe o tempo de cobertura (em meses);

- **Nome do Produto para Integrações:** Informe qual será o nome do produto a ser exibido nas integrações. Caso esse campo não seja preenchido, o nome preenchido em “Descrição do Produto” na aba “Informações Básicas” será utilizado;

- **Nome do Produto para NF-e:** Informe qual será o nome do produto que será utilizado para emissão de Nota Fiscal Eletrônica;

- **Descrição:** É a descrição do produto. Neste campo é possível estilizar a fonte utilizada (seja a cor, tamanho, etc). Limite de 4.000 caracteres;

- **Descrição Curta:** É a descrição curta do produto. Diferente da “Descrição”, neste campo não é possível estilizar a fonte. Limite de 4.000 caracteres;

- **Meta Title:** É o título da sua página que é exibido no resultado das buscas do Google. Limite de 255 caracteres;

- **Meta Description:** É um pequeno texto que é exibido abaixo do Meta Title no resultado das buscas do Google. Limite de 255 caracteres;

![d14](https://ajuda.sankhya.com.br/hc/article_attachments/44011862138263)

- **Miniatura do Produto:** É a foto do produto otimizada, utilizada no PDV, App 's, sites, etc. O **Artemis5** é compatível com os formatos .png e .jpg;

- **Vetor do Produto:** É a foto do produto vetorizada. Neste campo, pode-se enviar fotos nos formatos .svg, .png ou .jpg;

## FISCAL

![d15](https://ajuda.sankhya.com.br/hc/article_attachments/44011897538711)

- **NCM:** É um código de oito dígitos utilizado para identificar a natureza das mercadorias. Essa categorização tem como objetivo melhorar e facilitar o comércio internacional e seu controle estatístico. Qualquer mercadoria, importada ou comprada no Brasil, deve ter o código NCM na Nota Fiscal;

- **EX TIPI** (Exceção da Tabela do IPI): É um número utilizado para identificar se há diferença sobre a alíquota do IPI ou da regra da NCM em relação à tributação deste produto. Produtos acompanhados do “Ex” pertencem a uma categoria de classificação fiscal, porém, com a alíquota diferente (maior ou menor) da que está estabelecida na tabela para a classificação fiscal dos demais produtos;

- **Especialização NCM:** É um código NCM utilizado em produtos raros, cujo objetivo é um especificação diferenciada em relação à tributação;

- **Forma de Aquisição:** Informe qual foi a forma de aquisição deste produto, sendo “Produzida/Importada” ou “Adquirida de Terceiros”;

- **Origem da Mercadoria:** Informe qual a origem da mercadoria, sendo ela “Nacional” ou “Importada”;

- **Tipo de Tributação IPI:** É uma configuração utilizada para determinar o modelo de cálculo do IPI, seja por “Quantidade” ou por ‘“Valor da Operação”;

- **Regra Tributos:** Informe em qual a regra de tributos este produto irá fazer parte.

- **Número CEST:** O CEST é um código cuja finalidade é identificar categorias de produtos passíveis à substituição tributária. A partir dele, o recolhimento do ICMS será antecipado e sua cobrança permitirá que um único contribuinte pague o imposto;

- **Uni Comercial:** Informe qual o tipo do produto a ser cadastrado. A opção selecionada neste local será exibida no campo **“Unidade Tributável”** ao cadastrar uma conversão na seleção de fornecedores.

![d16](https://ajuda.sankhya.com.br/hc/article_attachments/44011879473815)

- **Tipo de Tributação:** Informe o tipo de tributação que esse produto faz parte;

Após finalizar o preenchimento de todos os campos necessários, **clique em “Salvar”.**

---

Para habilitar as abas **“Imagens” e "Movimentação de Estoque"** você deverá **editar o produto** na listagem de produtos. Utilize os filtros para encontrar o produto correto e clique no **ícone em amarelo** na coluna de Opções, a ultima à direita da tabela.

![d17](https://ajuda.sankhya.com.br/hc/article_attachments/44011884703383)

## IMAGENS

Utilizado para inserir mais imagens no cadastro do produto para serem usadas em integrações, vitrines e marketplaces. É possível inserir imagens por plataforma, como no exemplo abaixo:

![d18](https://ajuda.sankhya.com.br/hc/article_attachments/44011862598807)

## MOVIMENTAÇÃO DE ESTOQUE

Utilizado para analisar todas as movimentações de estoque que já houve com o produto, exibindo: data, horário, responsável pela movimentação e qual o tipo de movimentação realizada. Para isso, selecione o Depósito, clicando no ícone ao lado direito e depois, em buscar. A relação com a movimentação de estoque do depósito selecionado será exibida.

![d19](https://ajuda.sankhya.com.br/hc/article_attachments/44011862699287)
