---
id: "44011905738135"
titulo: "Como cadastrar um produto kit sem variações?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011905738135-Como-cadastrar-um-produto-kit-sem-varia%C3%A7%C3%B5es"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:13:56Z"
rotulos: ["sync_hc", "magis5", "sync_hash_aae3aa8d3a50", "magis5_204048483629"]
---

# Como cadastrar um produto kit sem variações?

## No Magis5 Hub, os produtos do tipo “Composto” podem ser utilizados para a criação de kits, que são produtos agrupados e vendidos juntos, ou para elaborar um produto de fabricação própria, que são produtos produzidos pela própria rede varejista.

Um produto kit é definido como “um conjunto de mercadorias que agregam valor entre si, geralmente composto de dois ou mais itens”. Quando não há variações dos produtos que compõem um kit, ou seja, quando um produto Kit é simples, é possível criá-lo selecionando a opção: “Produto Composto”.

Para facilitar o entendimento,  vamos utilizar o exemplo da criação de um Kit contendo um mouse e um teclado.

Cenário Utilizado:

1. Estes produtos (mouse e teclado) são vendidos individualmente no empreendimento;
2. Ambos não possuem variação de modelo.

Para iniciar o cadastro deste tipo de produto é necessário que todas as composições estejam previamente cadastradas. Caso não estejam, [clique aqui](https://ajuda.artemis5.com.br/como-cadastrar-produto-normal-sem-variacao/).

---

Para criar um produto de kit, “Sem Variações”, siga os passos abaixo:

Na barra de menus, clique em: Cadastro → Produtos:

![Imagem 1: Na barra de menus, clique em: Cadastro → Produtos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/07/image-127-1024x144.png)

No módulo de produtos, clique em “Novo Produto”.

Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e automática, cujo código é único e não editável.

![Imagem 2: Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-119-1024x208.png)

O módulo de produtos é separado por abas, sendo cada uma delas responsável por uma área específica.

1. **Informações Básicas**

- **Tipo de Produto:** Selecione “Composto”;

- **Fabricação Própria:** Selecione “Não”.

- **Peso Líquido (Un. Com.):** É o peso líquido do produto (desconsiderando o peso da embalagem);

- **Bloquear Transf. Produção:** Utilizado para transferência de produtos entre fábricas. Selecione “Não” caso o produto seja 100% produzido na mesma fábrica e seus insumos não possam ser transferidos para outra fábrica. Caso selecione “sim”, será permitido transferir parte dos insumos.

No exemplo de uma pizza, haverão insumos que serão utilizados para a produção da massa, que depois, será utilizada para a composição da pizza. Neste caso, as matérias primas não poderão ser transferidas, visto que serão utilizadas para a produção da massa.

- **Possui Variações:** Selecione “não”.

- **Código de Barras:** Insira o código de barras do produto.

Obs: Em casos em que o  estabelecimento recebe a caixa mas a  venda é realizada na unidade, é possível realizar a conversão da caixa para a unidade, vinculando o produto unitário à caixa.

Neste caso, é preciso cadastrar o produto unitário antes de cadastrar a caixa do produto.

Feito isso, ao cadastrar a caixa do produto, em “**Produto Unitário**”, clicar na lupa, buscar pelo produto unitário, selecioná-lo e em “**Qtd Unidades”**, informar a quantidade de itens que a caixa possuirá.

![Imagem 3: Feito isso, ao cadastrar a caixa do produto, em “ Produto Unitário ”, clicar na lupa, buscar pelo produto unitário,…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-121.png)

- **Descrição do Produto:** É o nome do produto utilizado para identificação interna. Este campo é obrigatório;

- **Código GTIN:** É o código de barras universal do produto. Para que o código GTIN conste na Nota Fiscal Eletrônica, deverá obedecer o padrão Brasil, iniciando em 7898 ou 7896. Qualquer código iniciado com números diferentes não será exibido no XML da Nota Fiscal. Caso coloque um código iniciando em 7898 ou 7896 mas o restante do código esteja incorreto, acarretará um erro de transmissão da Nota Fiscal. É recomendável que o código de barras seja o mesmo do código GTIN.

Caso não preencha o código, o campo sairá em branco.

- **Nome de Exibição (PDV):** É o nome do produto que será exibido no módulo de frente de caixa (PDV) ao cliente;

- **Insumos:** Informe neste campo quais serão os itens que irão compor o produto.

Clique no (+) localizado a direita, busque pelo produto, informe a quantidade de itens que irá utilizar e clique em “Selecionar”. Faça esse procedimento com todos os insumos do produto.

![Imagem 4: Clique no (+) localizado a direita, busque pelo produto, informe a quantidade de itens que irá utilizar e clique em…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-122-1024x201.png)

Após finalizar a seleção de insumos, clique no (x) para fechar a tela de seleção e verifique todos os insumos selecionados.

![Imagem 5: Após finalizar a seleção de insumos, clique no (x) para fechar a tela de seleção e verifique todos os insumos…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-123-1024x216.png)

No campo “% s/ Venda” informe a porcentagem correspondente a cada item deste produto para que o **Artemis5** saiba qual será o valor que cada item custará no final de uma venda. Por exemplo: é criado um KIT contendo um Whey e uma coqueteleira onde o Whey custa R$ 100,00 e a coqueteleira custa R$ 0,10. O Kit está sendo vendido a R$ 500,00. Se este campo não tiver preenchido, no pedido, o Whey custará R$ 250,00 e a coqueteleira, R$ 250,00 sendo que, proporcionalmente, nesta venda, o Whey custará R$ 499,50 e a coqueteleira, R$ 0,50).

**EMPREENDIMENTOS**

O empreendimento que o usuário está logado vem selecionado por padrão, caso o lojista possua mais de um empreendimento, é possível compartilhar o cadastro do produto entre eles, evitando ter que refazer o cadastro e agilizando o processo.

Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e selecione os empreendimentos desejados:

![Imagem 6: Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-124-1024x274.png)

- **Categoria:** Cada produto poderá ser inserido em apenas uma categoria por empreendimento. Porém, é possível inserir esse produto em categorias diferentes em cada empreendimento;

- **Ativo:** Informa se este produto estará habilitado ou não no empreendimento. O produto pode estar ativo em um empreendimento e desativado em outro;

- **ID Externo:** Utilizado em clientes que possuem uma base de dados já existente (seja em marketplaces ou na migração de outro ERP) e inicie a utilização do **Artemis5**. Esse ID Externo servirá para que o produto não perca a referência do produto antigo e não perca a relevância dos anúncios. Cada empreendimento pode ter um código distinto;

- **Estoque Mínimo:** O preenchimento deste campo reflete no “Relatório de Produtos c/ Estoque Mínimo”, onde é exibido um alerta no momento que o estoque atinge o mínimo preenchido no cadastro do produto informando que o produto está abaixo do necessário para a operação do estabelecimento. Caso não queira ter esse controle neste produto, basta não preencher o campo. É possível definir uma quantidade mínima para cada estabelecimento;

![Imagem 7: Estoque Mínimo: O preenchimento deste campo reflete no “Relatório de Produtos c/ Estoque Mínimo”, onde é exibido um…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-125-1024x135.png)

**PREÇO**

Cada empreendimento pode ter sua tabela de preços, sendo possível que cada empreendimento tenha até quatro tabelas de preços diferentes, sendo elas: “Atacado”, “Intermediário 1”, ”Intermediário 2” e “Varejo”. A definição de quais tabelas o empreendimento irá utilizar é definida na implantação do **Artemis5**, podendo ser alterado nas configurações de cada empreendimento.

A aplicação do preço final ao cliente é definida no cadastro do cliente ou pelo vendedor na hora da venda (caso o vendedor possua a permissão necessária);

- **%:** É a porcentagem de lucro sobre o preço de custo do produto. O preenchimento deste campo calcula automaticamente o valor de venda do produto com base na porcentagem informada e preenche a coluna (R$);

- **R$**: É o valor de venda do produto que será cobrado do cliente final. O preenchimento deste campo calcula automaticamente a porcentagem de lucro que este produto terá com base no preço informado e preenche a coluna (%);

- **% Desc. Máx:** Sobrepõe qualquer outro desconto que o produto possa ter. É a porcentagem de desconto máximo a ser disponibilizado para o produto. O valor inserido neste campo implica na liberação de desconto para o produto no ato da compra. Por exemplo:
  - Situação 1: O produto tem um desconto máximo de 20%, porém, um vendedor deseja aplicar um desconto superior.  A venda é travada e o desconto só é aplicado após alteração no cadastro do produto ou a correção do desconto.
  - Situação 2: O campo “Desc. Máx” não está preenchido, consequentemente o produto não possui um limite de desconto. Porém, o vendedor que está realizando a venda só tem permissão para aplicar uma porcentagem fixa de desconto. Caso  ele queira aplicar um desconto maior, será necessário que alguém com uma permissão superior libere o desconto.

**ESTOQUE**

É possível controlar o estoque dos produtos ao adicionar, remover ou mesmo, corrigi-los através de um inventário.

- **Controlar Estoque:** Selecione sim caso haja controle de estoque do produto.

- **Unidade de Medida:**

- **Unidade:** É utilizado para produtos unitários;

- **Fração:** É utilizado em casos que são vendidas partes de um produto (unidades fracionadas).

- **Qt. Múltipla:** É utilizado em situações onde há mais de um empreendimento e esses empreendimentos realizam transferências entre si. As solicitações de transferência deverão respeitar este campo, uma vez que o número informado será utilizado como parâmetro: se estiver marcado 10, não será possível pedir 15 unidades, já que 15 não é múltiplo de 10.

- **Depósito:** Utilizado para realizar movimentações no estoque, sendo entrada ou saída de produtos além de ajustes de estoque (através do inventário, baixa manual ou entrada de estoque). Para habilitar este campo, é necessário salvar o produto e depois, acessar o cadastro do produto novamente.

É possível ajustar o estoque de vários depósitos na mesma tela desde que os depósitos estejam compartilhados com o empreendimento que você está logado.

Ao selecionar o depósito, informe qual será o tipo de movimentação, quantidade de itens e clique em “Movimentar”. Após clicar em “Movimentar”, o estoque anterior será ajustado.

Para efetuar este procedimento, selecione a opção abaixo e informe em qual será o depósito que irá realizar a alteração:

![Imagem 8: Para efetuar este procedimento, selecione a opção abaixo e informe em qual será o depósito que irá realizar a alteração:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-126-1024x335.png)

A movimentação de estoque só poderá ser realizada por usuários com a devida permissão.

Observação: Só será possível realizar a venda do produto KIT se todos os itens que compõem o KIT tiverem estoque. A falta de um item acarretará na indisponibilidade da venda.

- **Tipo de movimentação:** Informa qual será a movimentação a ser realizada, sendo elas:

- **Inventário:** É a substituição do produto do depósito selecionado.

- **Entrada:** É a adição de produtos ao depósito selecionado. Ele é somado a quantidade atual de produtos.

- **Saída:** É a retirada de produtos ao depósito selecionado. O valor informado é removido da quantidade atual de produtos. É possível informar os motivos pelo qual está removendo os produtos, desde que esses motivos sejam cadastrados anteriormente. Para realizar este procedimento, clique aqui (tutorial de criação de motivos de saída)

- **Data de Validade:** Caso o estabelecimento controle os produtos por data de validade, a data de validade do produto deverá ser informada neste campo.

- **Qtd.:** Quantidade de produtos que serão adicionados ao depósito selecionado.

Obs: Após movimentar o primeiro depósito, pode-se selecionar outro depósito e realizar o mesmo procedimento.

**FORNECEDORES**

Utilizado na elaboração da lista de cotação. Um produto pode possuir mais de um fornecedor com conversões diferentes, por exemplo: O fornecedor A vende o pack de água com 12 unidades e o fornecedor B vende o pack da mesma água com 6 unidades.

 É necessário preencher este campo para informar quais são os fornecedores deste produto.

Para informar os fornecedores do produto, basta clicar em “Incluir” e selecioná-los. A seguir, preencha as seguintes informações:

- **Un. Medida de Compra:** É a maneira que esse produto é vendido, seja em peso (quilograma, grama), unidade, dezena, peça, pacote, etc.

- **Qtd. Min. Compra:** Neste campo é informado o mínimo de unidades que o fornecedor vende deste produto;

Além desses campos, há também a possibilidade de cadastrar as conversões deste produto. Para isso, clique em conversões e preencha os campos seguintes:

![Imagem 9: Além desses campos, há também a possibilidade de cadastrar as conversões deste produto. Para isso, clique em conversões…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-127-1024x396.png)

- **Código Interno do Fornecedor:** É o código de identificação do produto descrito na Nota Fiscal de Compra (normalmente chamado de SKU) utilizado para alimentar o estoque ao realizar a leitura da Nota Fiscal no processo de Entrada de Estoque (amarrar link).

- **Unidade Comercial:** É o modo que é vendido esse produto (seja em lote, quilo, litros, etc);

- **Unidade Tributável:** Não é possível editar este campo nesta tela. Para editá-lo, selecione a aba “Fiscal” e altere o campo “Uni Comercial”:

![Imagem 10: Unidade Tributável: Não é possível editar este campo nesta tela. Para editá-lo, selecione a aba “Fiscal” e altere o…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-128-1024x285.png)

- **Fator de Conversão:**
  - **Divisão:** É utilizado quando o empreendimento adquire um produto e divide esse produto em dois ou mais produtos para comercializá-lo. 
    Exemplo: O lojista adquiriu uma caixa com 30 unidades de um produto e dividiu essa caixa em 3 pacotes com 10 unidades para venda. Em **Qtd. de Conversão** deve ser informado o número 10, visto que, ao realizar a entrada da Nota Fiscal, o estoque será alimentado em 3 unidades deste produto.
  - **Multiplicação:** Utilizado em situações onde o empreendimento adquire um produto em caixa e vende o produto unitário. Ao realizar a leitura da Nota Fiscal, o **Artemis5** irá identificar que entrou uma caixa no estoque, porém, apenas a quantidade de produtos que compõem a caixa será acrescida ao estoque. 
    Exemplo: O lojista adquiriu uma caixa com 30 unidades de um produto. Em **Qtd. de Conversão** deve ser informado o número 30, visto que, ao realizar a entrada da Nota Fiscal, o estoque será alimentado em 30 unidades deste produto.

Obs: É possível ter mais de uma unidade de conversão por produto, visto que pode-se comprar tamanhos diferentes de caixa do mesmo fornecedor.

**INFORMAÇÕES COMPLEMENTARES**

- **Fabricante:** Informe qual a marca do produto;

- **Peso Bruto (Kg):** Informe o peso do produto (considere o peso da embalagem exibida no rótulo do produto);

- **Largura do Pacote:** Informe a largura do produto (em centímetros);

- **Altura do Pacote:** Informe a altura do produto (em centímetros);

- **Profundidade do Pacote:** Informe a profundidade do produto (em centímetros).

- **Natureza:** Informe a classificação do produto dentro do plano de contas (Para saber mais sobre o plano de contas, clique aqui)

- **Garantia (Meses):** Caso seja oferecida uma garantia pelo produto, informe o tempo de cobertura (em meses);

- **Nome do Produto para Integrações:** Informe qual será o nome do produto a ser exibido nas integrações. Caso esse campo não seja preenchido, o nome preenchido em “Descrição do Produto” na aba “Informações Básicas” será utilizado;

- **Nome do Produto para NF-e:** Informe qual será o nome do produto que será utilizado para emissão de Nota Fiscal Eletrônica;

- **Descrição:** É a descrição do produto. Neste campo é possível estilizar a fonte utilizada (seja a cor, tamanho, etc). Limite de 4.000 caracteres;

- **Descrição Curta:** É a descrição curta do produto. Diferente da “Descrição”, neste campo não é possível estilizar a fonte. Limite de 4.000 caracteres;

- **Meta Title:** É o título da sua página que é exibido no resultado das buscas do Google. Limite de 255 caracteres;

- **Meta Description:** É um pequeno texto que é exibido abaixo do Meta Title no resultado das buscas do Google. Limite de 255 caracteres;

![Imagem 11: Meta Description: É um pequeno texto que é exibido abaixo do Meta Title no resultado das buscas do Google. Limite de…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-129.png)

- **Miniatura do Produto:** É a foto do produto otimizada, utilizada no PDV, App 's, sites, etc. O **Artemis5** é compatível com os formatos .png e .jpg;

- **Vetor do Produto:** É a foto do produto vetorizada. Neste campo, pode-se enviar fotos nos formatos .svg, .png ou .jpg;

**FISCAL**

- **NCM:** É um código de oito dígitos utilizado para identificar a natureza das mercadorias. Essa categorização tem como objetivo melhorar e facilitar o comércio internacional e seu controle estatístico. Qualquer mercadoria, importada ou comprada no Brasil, deve ter o código NCM na Nota Fiscal;

- **EX TIPI** (Exceção da Tabela do IPI): É um número utilizado para identificar se há diferença sobre a alíquota do IPI ou da regra da NCM em relação à tributação deste produto. Produtos acompanhados do “Ex” pertencem a uma categoria de classificação fiscal, porém, com a alíquota diferente (maior ou menor) da que está estabelecida na tabela para a classificação fiscal dos demais produtos;

- **Especialização NCM:** É um código NCM utilizado em produtos raros, cujo objetivo é um especificação diferenciada em relação à tributação;

- **Forma de Aquisição:** Informe qual foi a forma de aquisição deste produto, sendo “Produzida/Importada” ou “Adquirida de Terceiros”;

- **Origem da Mercadoria:** Informe qual a origem da mercadoria, sendo ela “Nacional” ou “Importada”;

- **Tipo de Tributação IPI:** É uma configuração utilizada para determinar o modelo de cálculo do IPI, seja por “Quantidade” ou por ‘“Valor da Operação”;

- **Regra Tributos:** Informe em qual a regra de tributos este produto irá fazer parte. Para criar novas regras de Tributos, clique aqui

- **Número CEST:** O CEST é um código cuja finalidade é identificar categorias de produtos passíveis à substituição tributária. A partir dele, o recolhimento do ICMS será antecipado e sua cobrança permitirá que um único contribuinte pague o imposto;

- **Uni Comercial:** Informe qual o tipo do produto a ser cadastrado. A opção selecionada neste local será exibida no campo “Unidade Tributável” ao cadastrar uma conversão na seleção de fornecedores.

![Imagem 12: Uni Comercial: Informe qual o tipo do produto a ser cadastrado. A opção selecionada neste local será exibida no campo…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-130-1024x381.png)

- **Tipo de Tributação:** Informe o tipo de tributação que esse produto faz parte;

Após informar todos os dados do produto, clique em “Salvar” para salvar o produto.

Para habilitar a aba “Imagens” e “Movimentação de Estoque”, clique em editar, na “Listagem de Produtos”:

![Imagem 13: Para habilitar a aba “Imagens” e “Movimentação de Estoque”, clique em editar, na “Listagem de Produtos”:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-131-1024x201.png)

**IMAGENS**

Utilizado para inserir mais imagens no cadastro do produto para serem usadas em integrações, vitrines e marketplaces. É possível inserir imagens por plataforma, como no exemplo abaixo:

![Imagem 14: Utilizado para inserir mais imagens no cadastro do produto para serem usadas em integrações, vitrines e marketplaces. É…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-133-1024x558.png)

**MOVIMENTAÇÃO DE ESTOQUE**

Utilizado para analisar todas as movimentações de estoque que já houve com o produto, exibindo: data, horário, responsável pela movimentação e qual o tipo de movimentação realizada. Para isso, selecione o Depósito, clicando no ícone ao lado direito e depois, em buscar. A relação com a movimentação de estoque do depósito selecionado será exibida.

![Imagem 15: Utilizado para analisar todas as movimentações de estoque que já houve com o produto, exibindo: data, horário,…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/05/image-132-1024x496.png)

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011894525463)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
