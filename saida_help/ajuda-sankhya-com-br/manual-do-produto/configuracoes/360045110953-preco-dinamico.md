---
id: "360045110953"
titulo: "Preço Dinâmico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110953-Pre%C3%A7o-Din%C3%A2mico"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:25Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Impostos", "TOP", "Preço", "Dinâmico", "MODCALCPRECDIN", "NOMPROCCALCPRE", "Preço Dinâmico manual", "CORE_E02294", "CORE_E02297", "Configuração de Preço Dinâmico em Vendas", "USAIMPPRECODIN"]
---

# Preço Dinâmico

No dia a dia de sua empresa pode ser necessário que o preço de venda utilizado nas negociações, tenha como base diversas particularidades. Dentre estas especificidades pode-se ter: forma de pagamento, impostos, usuários, contratos fechados com clientes, promoções, entre outras, onde será necessário levar todas elas em consideração para calcular o preço de venda. As informações abaixo, visam te orientar na construção do cálculo do preço de venda com base em todos os critérios desejados pela sua empresa.

Na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) o cálculo do preço dinâmico do produto será efetuado quando o [Tipo de operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), possuir no campo **"Usar como preço"** a opção **"Preço de Venda"** selecionada.

**Impacto na Consulta de Produtos:** ao preencher este parâmetro, o sistema altera o comportamento da tela de Consulta de Produtos. O preço exibido para o usuário deixará de ser apenas o valor estático da tabela de preços e passará a ser o valor retornado pela procedure personalizada, garantindo que o vendedor veja o preço exato (com todas as variáveis de negócio) antes mesmo de inserir o item na nota.

**Impacto no Cálculo e Performance:** o parâmetro **"Usa impostos no cálculo do preço dinâmico? - USAIMPPRECODIN"** define a ordem das operações. Se ligado (padrão), o sistema processa todos os impostos antes de enviar os dados para a sua procedure. Caso sua regra de preço dinâmico não utilize valores de impostos (como Base de ICMS ou Vlr IPI) para chegar ao preço final, recomenda-se desativar este parâmetro. Isso gera um ganho significativo de performance, pois evita cálculos tributários desnecessários antes da chamada da procedure.

**Observações:**

- Você só poderá utilizar o cálculo de preço dinâmico quando o Tipo de Operação - TOP for um Pedido de venda, Venda ou uma Devolução de venda.
- Com o parâmetro **"Usa impostos no cálculo do preço dinâmico? - USAIMPPRECODIN"** ligado, o cálculo de impostos será executado antes de chamar a procedure que faz o cálculo do Preço Dinâmico. Por padrão, este parâmetro é ligado. Caso não sejam utilizados valores de impostos no cálculo do Preço Dinâmico, desligando esse parâmetro haverá um ganho de performance no sistema.
- Quando o parâmetro **"Usa cache na inicialização do produto? - USACACHEINIPROD"** estiver desligado, não será feito o cache da inicialização do produto, trazendo então o valor do produto de forma correta quando for alterado o tipo de negociação do Pedido de Venda com itens duplicados utilizando a funcionalidade do preço dinâmico.
- É primordial que as configurações abaixo, sejam realizadas e validadas por um implantador Sankhya.

Tem-se dois parâmetros essenciais para funcionamento desta rotina. São eles:

**Nota modelo para cálculo de preço dinâmico - MODCALCPRECDIN:** Neste parâmetro, informe o modelo de nota/pedido que será utilizado para gerar um Cabeçalho transient. No caso, esse cabeçalho não será persistido, pois ele serve apenas para fins de cálculo de impostos. Em algumas situações, como por exemplo a Consulta de Produtos aberta diretamente, não tem-se o cabeçalho para calcular impostos.

![Imagem 1: A criação da nota modelo deve ser feita através da tela Modelo de Notas e Pedidos .](https://ajuda.sankhya.com.br/hc/article_attachments/24421715640599) A criação da nota modelo deve ser feita através da tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos).

**Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE:** Indique neste parâmetro, o nome da procedure para cálculo de preço dinâmico. Ao preenchê-lo, significa que o sistema irá utilizar as rotinas de preço dinâmico.

**Observação:** com os parâmetros de chave MODCALCPRECDIN e NOMPROCCALCPRE devidamente configurados, quando for lançada uma venda ou um pedido de venda informando o local do item, o valor unitário será calculado conforme a procedure cadastrada.

No entanto, caso a quantidade de um item seja aumentada durante a [Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia), o sistema refaz automaticamente o cálculo do custo do produto. Isso acontece porque algumas procedures de cálculo de custo dinâmico consideram a obtenção do preço com base na quantidade negociada. Portanto, qualquer alteração na quantidade exige que o sistema realize um novo cálculo para garantir que o valor do produto reflita a quantidade atualizada.

Na configuração do parâmetro **"Campos que afetam o cálculo do preço Dinâmico - LISCAMPPRECODIN"** deverão ser inseridos quais os campos da TGFCAB irão influenciar no Cálculo do Preço Dinâmico, inclusive campos adicionais, para que, caso algum deles seja alterado, seja recalculado o preço dos produtos. Importante ressaltar que, para isso o parâmetro **"Recalcula preços quando altera Tipo de Negociação: - RECPRECOTPV"** deve estar definido como **"Sempre"**.

**Observação:** os campos que já recalculam o preço quando são alterados não deverão ser incluídos neste parâmetro.

**Nota:** os nomes dos campos devem estar em letras maiúsculas e separados por vírgulas.

No momento do cálculo do preço de venda, será chamada uma procedure personalizada. Esta procedure será "chamada" pelo sistema na inicialização do produto na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) e na [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos) solicitada também pela Central de Vendas ou diretamente pela rotina de Consulta de Produtos.

A rotina de cálculo dinâmico é executada em pontos específicos do sistema. São eles:

- Na inicialização do produto;
- Ao consultar o produto pela Consulta de Produtos (Central de Vendas e diretamente pela Consulta de Produtos);
- Na alteração do campo de quantidade (pela Central de Vendas ou pelo Carrinho de Compras);
- Ao salvar o item pela Central de Vendas ou na inclusão direta pelo carrinho. Uma informação importante é que apenas nesse ponto é que o sistema injeta os demais campos calculados pela procedure.

No parâmetro **"Campos do item para cálculo do preço Dinâmico - CAMITEMPRECODIN"**, deverão ser informados os campos da **TGFITE** (itens da nota) que serão levados em consideração no cálculo do preço dinâmico.

- **Limitação:** o tipo do campo configurado neste parâmetro não pode ser do tipo "Checkbox".

Quando for utilizada a Consulta de Produtos aberta diretamente (sem acessar primeiramente a Central de Vendas), o sistema irá gerar um Cabeçalho transient, o qual é necessário para cálculo de impostos. Para gerar esse cabeçalho será utilizado o modelo definido no parâmetro MODCALCPRECDIN, caso o parâmetro não esteja configurado será corretamente apresentada a seguinte mensagem:

**"Falha no cálculo de preço dinâmico: O modelo de nota/pedido informado no parâmetro MODCALCPRECDIN não existe."**

No caso da empresa, a primazia é utilizar a empresa do usuário logado; caso este não tenha empresa vinculada, será utilizada a empresa do modelo. Se nenhuma empresa foi definida, será exibida a seguinte mensagem no cálculo:

**"Falha no cálculo de preço dinâmico: Nenhuma empresa foi defina no modelo de nota/pedido e o usuário logado não está vinculado a uma empresa."**

Caso ocorra alguma falha na execução da procedure, será apresentada a seguinte mensagem:

**"Falha no cálculo de preço dinâmico: Erro ao executar a procedure 'nome\_precedure'."**

Sobre a procedure:

Dados disponíveis na procedure:

**SEQUENCIA**

**NUNOTA**

**IDALIQ**

**CODPROD**

**CONTROLE**

**CODLOCAL**

**CODVOL**

**QTD**

**CODPARC**

**CODVEND**

**CODTIPVENDA**

**CODTIPOPER**

**CODEMP**

**CODUSULOGADO**

**VLRUNIT**

**BASEICMS**

**BASESUBST**

**VLRSUBST**

**VLRICMS**

**VLRIPI**

**ICMSPRO\_VLRDIFALDEST**

**ICMSPRO\_VLRDIFALREM**

**ICMSPRO\_VLRFCP**

**IPIPRO\_PERCIPI**

Esses dados são disponibilizados através da tabela **EXECPARAMS**. Além disso, existem funções específicas para se obter esses dados (Opcional):

**ACT\_DEC\_FIELD**

**ACT\_INT\_FIELD**

**ACT\_DTA\_FIELD**

**ACT\_TXT\_FIELD**

A procedure para cálculo de preço dinâmico deve receber apenas um parâmetro de entrada e como resultado deve retornar um Json do tipo chave-valor. O campo "PRECO" é o preço dinâmico e esse dado é obrigatório no retorno, mesmo que seja zero. Por exemplo:

**{**

**"PRECO" : "50.0",**

**"PRECOBASE" : "50.0"**

**"AD\_TIPOPRECO" : "T"**

**}**

**Observação:** para que uma ou mais empresas não sejam incluídas no cálculo de preço dinâmico, basta informá-las no campo **"Texto"** do parâmetro **"Lista de empresas sem cálculo de preço dinâmico. - LISEMPSEMPREDIN"**.

Caso utilize a opção **"Nunca"** no parâmetro RECPRECOTPV, porém ocorram algumas dessas condições acima, o recálculo será efetuado se:

- Na tela [Cadastro do Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abavenda), o campo **"Digitação na nota"** estiver definido com a opção **"Quantidade"**;
- Se tratar de uma Venda e um dos parâmetros abaixo estiver ligado:

  - Usa desconto FOB - DESCFOB;
  - Usar % Desc.por região p/Frete FOB? - PERCDESCFOB;
  - Simula formas de pagamento na Central? - USASIMFORMAPGTO;
  - Usa Perc. Desc. FOB no rodapé (Venda)? - PERCDESCFOBCAB;
  - Usa precificação de produtos/serviços pela TOP - USAPRECPELATOP;
  - Usa precificação pela TOP no PDV Web - USAPRECTOPPDV (para [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047)).

**Observação:**quando o parâmetro **"Recalcular preço dinâmico ao alterar valor de desconto - RECALCPRECODINA"**estiver ligado, o preço dinâmico será recalculado sempre que ocorrer a inclusão, alteração de itens ou de suas informações.
