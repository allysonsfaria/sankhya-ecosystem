---
id: "44011898853399"
titulo: "Como cadastrar um produto kit com variações?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011898853399-Como-cadastrar-um-produto-kit-com-varia%C3%A7%C3%B5es"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:14:09Z"
rotulos: ["sync_hc", "magis5", "sync_hash_415b16ba6dac", "magis5_204055206969"]
---

# Como cadastrar um produto kit com variações?

## No Magis5 ERP, os produtos compostos desempenham um papel importante na criação de kits e na montagem de produtos de fabricação própria, que possuem variações.

Um kit é definido como um conjunto de mercadorias que possuem um valor agregado quando vendidas em conjunto, normalmente composto por dois ou mais itens.

Para facilitar a compreensão deste tutorial, vamos utilizar o exemplo da criação de um kit contendo um mouse e um teclado.

Cenário Utilizado:

1. Estes produtos (mouse e teclado) são vendidos de forma unitária no empreendimento;
2. O teclado não possui variação de modelo;
3. O mouse possui variação de cor, sendo preto e branco.

Considerando as informações acima, deduz-se que os produtos citados já estão cadastrados (visto que eles são vendidos de forma unitária).

---

Para criar um produto Kit, “Com Variações”, siga os passos abaixo:

Na barra de menus, clique em: Cadastro → Produtos:

![Imagem 1: Na barra de menus, clique em: Cadastro → Produtos:](https://ajuda.sankhya.com.br/hc/article_attachments/44011894760087)

No módulo de produtos, clique em “Novo Produto”.

Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e automática, cujo código é único e não editável.

![Imagem 2: Para cada novo cadastro é gerado um novo ID (identificação interna do produto dentro do sistema) de forma aleatória e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011899098903)

O módulo de produtos é separado por abas, sendo cada uma delas responsável por uma área específica.

**INFORMAÇÕES BÁSICAS**

- **Tipo de Produto:** Selecione “Normal”;

- **Possui Variações:** Selecione “sim”.

- **Descrição do Produto:** É o nome do produto utilizado para identificação interna. Este campo é obrigatório;

- **Nome de Exibição (PDV):** É o nome do produto que será exibido no módulo de frente de caixa (PDV) ao cliente;

**EMPREENDIMENTOS**

O empreendimento que o usuário está logado vem selecionado por padrão, caso o lojista possua mais de um empreendimento, é possível compartilhar o cadastro do produto entre eles, evitando ter que refazer o cadastro e agilizando o processo.

Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e selecione os empreendimentos desejados:

![Imagem 3: Nesta aba é exibido em quais empreendimentos este produto será compartilhado. Para isso, clique em “(+) Incluir” e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011931549463)

- **Categoria:** Cada produto poderá ser inserido em apenas uma categoria por empreendimento. Porém, é possível inserir esse produto em categorias diferentes em cada empreendimento;

- **Ativo:** Informa se este produto estará habilitado ou não no empreendimento. O produto pode estar ativo em um empreendimento e desativado em outro;

- **ID Externo:** Utilizado em clientes que possuem uma base de dados já existente (seja em marketplaces ou na migração de outro ERP) e inicie a utilização do **Artemis5**. Esse ID Externo servirá para que o produto não perca a referência do produto antigo e não perca a relevância dos anúncios. Cada empreendimento pode ter um código distinto;

**ESTOQUE**

É possível controlar o estoque dos produtos ao adicionar, remover ou mesmo, corrigi-los através de um inventário.

- **Controlar Estoque:** Selecione sim caso haja controle de estoque do produto.

- **Unidade de Medida:**

- **Unidade:** É utilizado para produtos unitários;

- **Fração:** É utilizado em casos que são vendidas partes de um produto (unidades fracionadas).

- **Qtd. Múltipla:** É utilizado em situações onde há mais de um empreendimento e esses empreendimentos realizam transferências entre si. As solicitações de transferência deverão respeitar este campo, uma vez que o número informado será utilizado como parâmetro: se estiver marcado 10, não será possível pedir 15 unidades, já que 15 não é múltiplo de 10.

- **Depósito:** Utilizado para realizar movimentações no estoque, sendo entrada ou saída de produtos além de ajustes de estoque (através do inventário, baixa manual ou entrada de estoque). Para habilitar este campo, é necessário salvar o produto e depois, acessar o cadastro do produto novamente.

É possível ajustar o estoque de vários depósitos na mesma tela desde que os depósitos estejam compartilhados com o empreendimento que você está logado.

Ao selecionar o depósito, informe qual será o tipo de movimentação, quantidade de itens e clique em “Movimentar”. Após clicar em “Movimentar”, o estoque anterior será ajustado.

Para efetuar este procedimento, selecione a opção abaixo e informe em qual será o depósito que irá realizar a alteração:

![Imagem 4: Para efetuar este procedimento, selecione a opção abaixo e informe em qual será o depósito que irá realizar a alteração:](https://ajuda.sankhya.com.br/hc/article_attachments/44011906531607)

A movimentação de estoque só poderá ser realizada por usuários com a devida permissão.

Observação: Só será possível realizar a venda do produto KIT se todos os itens que compõem o KIT tiverem estoque. A falta de um item acarretará na indisponibilidade da venda.

- **Combinação:** Selecione a combinação que deseja realizar a movimentação de estoque;

- **Tipo de movimentação:** Informa qual será a movimentação a ser realizada, sendo elas:

- **Inventário:** É a substituição do produto do depósito selecionado.

- **Entrada:** É a adição de produtos ao depósito selecionado. Ele é somado a quantidade atual de produtos.

- **Saída:** É a retirada de produtos ao depósito selecionado. O valor informado é removido da quantidade atual de produtos. É possível informar os motivos pelo qual está removendo os produtos, desde que esses motivos sejam cadastrados anteriormente. Para realizar este procedimento, clique aqui (tutorial de criação de motivos de saída)

- **Data de Validade:** Caso o estabelecimento controle os produtos por data de validade, a data de validade do produto deverá ser informada neste campo.

- **Qtd.:** Quantidade de produtos que serão adicionados ao depósito selecionado.

Observação: Após movimentar o primeiro depósito, pode-se selecionar outro depósito e realizar o mesmo procedimento.

**FORNECEDORES**

Utilizado na elaboração da lista de cotação. Um produto pode possuir mais de um fornecedor com conversões diferentes, por exemplo: O fornecedor A vende o pack de água com 12 unidades e o fornecedor B vende o pack da mesma água com 6 unidades.

 É necessário preencher este campo para informar quais são os fornecedores deste produto.

Para informar os fornecedores do produto, basta clicar em “Incluir” e selecioná-los. A seguir, preencha as seguintes informações:

→ **Un. Medida de Compra:** É a maneira que esse produto é vendido, seja em peso (quilograma, grama), unidade, dezena, peça, pacote, etc.

→ **Qtd. Min. Compra:** Neste campo é informado o mínimo de unidades que o fornecedor vende deste produto;

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

![Imagem 5: Meta Description: É um pequeno texto que é exibido abaixo do Meta Title no resultado das buscas do Google. Limite de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011895179927)

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

![Imagem 6: Uni Comercial: Informe qual o tipo do produto a ser cadastrado. A opção selecionada neste local será exibida no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011914684439)

- **Tipo de Tributação:** Informe o tipo de tributação que esse produto faz parte;

**COMBINAÇÕES**

Nesta aba serão adicionadas as variações dos produtos. É possível inserir a variação de um produto de duas maneiras: Criando um novo produto ou selecionando um produto existente.

- **Criando um novo produto:** Para inserir a variação através de um novo cadastro, clique na aba “Combinações” e depois, em (+) incluir, localizado à direita.  Feito isso, preencha todas as informações em todas as abas do produto filho e, em ‘tipo de produto’, selecione “Composto”, visto que será através dele que serão inseridas as composições do produto.

![Imagem 7: Criando um novo produto: Para inserir a variação através de um novo cadastro, clique na aba “Combinações” e depois, em…](https://ajuda.sankhya.com.br/hc/article_attachments/44011895358615)

Dica:  Para facilitar a identificação nos menus e consultas de produtos posteriormente, sempre identifique o tipo de variação do produto através dos campos: Tamanho ou Sabor/Cor.

Em “Insumos”, clique no (+) à direita e selecione os insumos deste produto:

![Imagem 8: Em “Insumos”, clique no (+) à direita e selecione os insumos deste produto:](https://ajuda.sankhya.com.br/hc/article_attachments/44011914879895)

O próximo passo é selecionar o primeiro item que irá compor o produto, neste caso, o teclado. Clique em “Selecionar” e, ao aparecer “Selecionado”, verifique se o produto já está sendo exibido na composição do produto (identificado pelo retângulo vermelho).

![Imagem 9: O próximo passo é selecionar o primeiro item que irá compor o produto, neste caso, o teclado. Clique em “Selecionar” e,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011914968983)

Em seguida, clique novamente no (+) para selecionar a primeira variação do mouse (que no caso, será o branco) e clique em “Salvar”:

![Imagem 10: Em seguida, clique novamente no (+) para selecionar a primeira variação do mouse (que no caso, será o branco) e clique…](https://ajuda.sankhya.com.br/hc/article_attachments/44011886810519)

O primeiro item deste produto composto já está incluso:

Para inserir a combinação com o mouse preto, repita o procedimento, selecionando o mouse preto invés do branco. Após inserir todos os itens do Kit, clique em “Adicionar”.

- **Selecionar Produto Existente**: Caso o produto composto já esteja criado, com as devidas variações relacionadas, basta

clicar na aba “combinações” e depois, em (+) incluir, localizado à direita. Na tela “Nova Combinação”, clique em “Selecionar Produto Existente”

A tela fará o carregamento de todas as informações do produto. Basta conferir se as variações estão selecionadas e clicar em salvar. 

No campo “% s/ Venda” informe a porcentagem correspondente a cada item deste produto para que o **Artemis5** saiba qual será o valor que cada item custará no final de uma venda. Por exemplo: é criado um KIT contendo um Whey e uma coqueteleira onde o Whey custa R$ 100,00 e a coqueteleira custa R$ 0,10. O Kit está sendo vendido a R$ 500,00. Se este campo não tiver preenchido, no pedido, o Whey custará R$ 250,00 e a coqueteleira, R$ 250,00 sendo que, proporcionalmente, nesta venda, o Whey custará R$ 499,50 e a coqueteleira, R$ 0,50).

Após informar todos os dados do produto e vincular os produtos “filho”, clique em “Salvar” para salvar o produto.

Para habilitar a aba “Movimentação de Estoque”, clique em editar, na “Listagem de Produtos”:

**MOVIMENTAÇÃO DE ESTOQUE**

Utilizado para analisar todas as movimentações de estoque que já houve com o produto, exibindo: data, horário, responsável pela movimentação e qual o tipo de movimentação realizada. Para isso, selecione o Depósito, clicando no ícone ao lado direito e depois, em buscar. A relação com a movimentação de estoque do depósito selecionado será exibida.

[![Universidade Magis5](https://ajuda.sankhya.com.br/hc/article_attachments/44011895832855)](https://download.magis5.com.br/universidade-magis5?utm_source=central_de_ajuda&utm_medium=link&utm_campaign=central_de_ajuda&hsLang=pt-br)
