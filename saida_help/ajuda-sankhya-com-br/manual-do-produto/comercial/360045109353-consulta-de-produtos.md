---
id: "360045109353"
titulo: "Consulta de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:29:11Z"
rotulos: ["Produtos", "manual", "Configuração", "Consulta", "Consulta de Produtos", "Alternativo", "DTPREVENTPEND", "Estoque disponível WMS", "IGNPRECARMOVIN", "LOTECARCOMP", "MOSTIMPCONSPROD", "PERCADPRODSUBST", "RESTACESSVENDRG", "Substituto", "br.com.sankhya.com.cons.consultaprodutos", "Consulta de Produtos manual", "Estoque", "USAPRECTOPPDV", "USAPRECPELATOP", "PREINDEXATERM", "EXPORDINDEX", "TIPDIRPROALT", "Consulta de produtos", "Preço e estoque", "Layout personalizado", "Comercial"]
---

# Consulta de Produtos

```
 Módulo: Comercial > Consulta
```

---

O principal objetivo dessa tela é apresentar os produtos de forma sintetizada, de modo que você consiga analisar o preço e o estoque dos produtos, entre outras informações. A Consulta de Produtos é exibida em seu layout padrão, sendo que o mesmo poderá ser personalizado de forma a melhor atender suas necessidades.

Essa rotina é preparada e apresentada, partindo de duas vertentes diferentes: uma é carregada com as configurações da Central - [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154) (quando aberta pela Central), e a outra é carregada diretamente quando aberta a tela Consulta de Produtos. A formação das grades é gravada na CFG tabela de configurações com chaves diferentes, e isso faz com que, ao abrir a tela pela Consulta de Produtos, tenha-se uma configuração e, abrindo-se pela Central, tenha-se outra. Portanto, caso seja necessário que em ambas as formas de abertura tenha-se grades iguais, configure as grades iguais para os dois locais através do menu da tela.

No lançamento de um pedido/nota, ao clicar em qualquer campo dos painéis e acionar as teclas de atalho **"Ctrl + Alt + P"**, será aberta a tela de Consulta de Produtos.

Para facilitar sua navegação nas funcionalidades dessa tela, acesse os links abaixo:

| Funcionalidades da tela | |
| --- | --- |
| [Modos de Exibição da Grade de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#modosdeexibiodagradedeprodutos) | [Config. a Ordenação dos Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configurandoaordenaodosprodutos) |
| [Configurações do Painel de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdopainelderesultado) | [Config. da Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos) |
| [Buscando os Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#buscandoosprodutos) | [Botão Outros Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#botooutrosfiltros) |
| [Botão Salvar em PDF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#salvarempdf) | [Carrinho de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#carrinhodecompras) |
| [Painel Buscar preço por](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#painelbuscarpreopor) | [Painel Classificadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#painelclassificadores) |
| [Painel Produção programada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#painelproduoprogramada) | [Como Simular um Desconto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#comosimularumdesconto) |
| [Desconto Promoc. por Quantidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#descontopromocionalporquantidade) | [Mesma Tab. de Preço p/ Todos os Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#utilizaodamesmatabeladepreoparatodososprodutos) |
| [Precificação de prod./serv. pela TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#usaraprecificaodeprodutosserviospelatop) | [Consulta de Produtos por Série](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#consultadeprodutosporsrie) |
| [Desc. Promoc. por Controle de Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#descontopromocionalporcontroledegrade) | [Parâmetros nos Detalhes do Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#parmetrosqueinfluenciamnosdetalhesdopreo) |
| [Campos Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#camposadicionais) |  |

## Modos de Exibição da Grade de Produtos

É possível configurar a forma que essa grade exibirá todos os produtos, seja em Modo Lista, Modo Coluna ou Modo Grade. Abaixo, trataremos sobre cada um deles:

#### Modo Lista

Nesse modo, os produtos serão listados na grade conforme a imagem abaixo:

![Imagem 1: Nesse modo, os produtos serão listados na grade conforme a imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4404799674007)

####

#### Modo Coluna

Para exibição no modo coluna, configure a quantidade de colunas que serão exibidas na aba [Layout da célula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abalayoutdaclula), botão ![Imagem 2: Para exibição no modo coluna, configure a quantidade de colunas que serão exibidas na aba Layout da célula , botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903395351) **"Configurar a quantidade de colunas"**. Tanto nesse modo quanto no Modo lista descrito no tópico acima,para expandir a imagem basta clicar sobre a miniatura.

![Imagem 3: Para exibição no modo coluna, configure a quantidade de colunas que serão exibidas na aba Layout da célula , botão…](https://ajuda.sankhya.com.br/hc/article_attachments/4404799812503)

####

#### Modo Grade

Os produtos serão exibidos nesse modo com o layout da grade:

![Imagem 4: Os produtos serão exibidos nesse modo com o layout da grade:](https://ajuda.sankhya.com.br/hc/article_attachments/4404799875479)

**Nota:** as configurações de grade realizadas no painel serão aplicadas somente na visualização do modo grade.

**Observação:** para que não ocorra erros ao finalizar o carrinho, será necessário incluir a coluna **"Preço"** na Consulta de Produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

**Configurando a Ordenação dos Produtos**

O botão ![Imagem 5: O botão "Configurar ordenação" abre um painel para que você possa configurar a ordenação de exibição dos produtos.](https://ajuda.sankhya.com.br/hc/article_attachments/16105903397015) **"Configurar ordenação"** abre um painel para que você possa configurar a ordenação de exibição dos produtos.

![Imagem 6: O botão "Configurar ordenação" abre um painel para que você possa configurar a ordenação de exibição dos produtos.](https://ajuda.sankhya.com.br/hc/article_attachments/4404784828567)

Nesse painel, em **"Ordenar por"**,  você deve escolher por qual campo deseja realizar a ordenação e depois informar se a ordenação será **"Crescente"** ou **"Decrescente"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Configurações do Painel de Resultado

Para efetuar as configurações relacionadas ao painel de resultado, é necessário clicar no botão ![Imagem 7: Para efetuar as configurações relacionadas ao painel de resultado, é necessário clicar no botão "Configurar Painel de…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903398167) **"Configurar Painel de Resultado"**. Ao acionar esse botão, o sistema exibirá a tela no modo de configurações. Essas configurações serão efetuadas através das abas **"Preços"**, **"Estoque"** e **"Layout da célula"**. Trataremos sobre cada uma delas logo abaixo:

| [Aba Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abapreos) |
| --- |
| [Aba Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaestoque) |
| [Aba Layout da célula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abalayoutdaclula) |

### Aba Preços

![Imagem 8: Aba Preços](https://ajuda.sankhya.com.br/hc/article_attachments/4407426631831)

A consulta irá exibir os preços dos produtos de acordo com as definições efetuadas nessa aba. Os preços poderão ser definidos informando os campos **"Descrição"**, **"Tabela específica"** e **"Multiplicador"**, sendo que, se a tabela específica não for informada, será utilizada a tabela padrão (0) do produto.

Após acionar o botão de pesquisa, a janela de consulta **"Pesquisando "Tabela de Preço""** é apresentada; nela, são exibidos em **"Código"** apenas os códigos das tabelas. Internamente, o sistema verifica o Cód. Único da Tabela (NUTAB) desse cód. da tabela (CODTAB), retornando para você, apenas a que possui data de vigor mais atual.

**Nota:** Caso você tenha inserido no sistema uma tabela de preço com data de vigor antiga, após a atualização da versão, o sistema automaticamente selecionará a mesma tabela, porém com a data de vigor mais atual.

O campo **"Multiplicador"** é o valor pelo qual será multiplicado o preço da tabela, seja ela uma tabela específica ou a tabela padrão do produto.

Poderão ser definidos vários preços nessa aba. Clicando sobre um produto no painel de resultados, serão exibidos todos os preços cadastrados no painel de **"Detalhes de preço"**.

**Observação:** A visualização do novo **"Preço"** cadastrado poderá ser configurada através da aba [Layout da célula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abalayoutdaclula) para ser visualizada em outros locais.

Se você efetuar a marcação **"Mostrar promoção na grade principal?"**, fará com que uma coluna seja apresentada na grade principal com o valor do produto em promoção. Se estiver desmarcada, a coluna não será apresentada.

**Nota:** Sempre terá a descrição **"Promoção"** juntamente com o nome da descrição do preço. Exemplo: Se no campo Descrição estiver **"Natal"**, a coluna se chamará **"Promoção Natal"**.

**Observação:** Quando o produto está em promoção por quantidade, ele somente será exibido através da Consulta de Produtos pela Central de Vendas pois, é necessário saber se o tipo de desconto para o tipo de negociação é por quantidade.

**Nota:** caso seja configurada alguma cor para produtos em promoção e/ou liquidação ([Configurações da consulta de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abageral)), para que as mesmas sejam aplicadas ao painel de produtos, é necessário que a marcação Mostrar promoção na grade principal? esteja marcada. Se estiver desmarcada, os produtos em promoção e liquidação não ficarão destacados nas cores definidas.

Trabalhando com Carrinho de Compras e efetuando a marcação Mostrar promoção na grade principal?, ao realizar a venda, elaa será feita considerando os descontos promocionais configurados; na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas), os campos Vlr. Unitário, Vlr. Unit. Liq. e % de Desconto, serão alimentados de acordo com esse comportamento.

#### Impacto do Preço Dinâmico na Consulta

Caso o parâmetro '**Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE**' esteja configurado, os preços apresentados na grade de resultados e nos detalhes de preço serão calculados em tempo real pela procedure definida. Se a consulta for aberta diretamente pelo menu, o sistema utilizará as definições do parâmetro '**Nota modelo para cálculo de preço dinâmico - MODCALCPRECDIN**' para simular os impostos necessários para o cálculo do preço. Você pode impedir que empresas específicas utilizem este cálculo através do parâmetro 'LISEMPSEMPREDIN'.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdopainelderesultado)

### Aba Estoque

Nessa aba você poderá cadastrar vários estoques, sendo que, cada um deles pode utilizar um filtro diferente.

![Imagem 9: Nessa aba você poderá cadastrar vários estoques, sendo que, cada um deles pode utilizar um filtro diferente.](https://ajuda.sankhya.com.br/hc/article_attachments/4407433834647)

Informe no campo **"Descrição"** o nome do estoque.

Se a marcação **"Subtrair reservas"** estiver selecionada, ao exibir o estoque, o sistema subtrairá a quantidade reservada do total em estoque produto.

A marcação **"Apenas estoque da empresa da nota"**, quando efetuada, alimentará o campo **"Estoque"** com o somatório do estoque da empresa da nota em questão. Como por exemplo:

O Produto X  tem 100 unidades no estoque da empresa 1 e para empresa 2 tem 200 unidades. A nota de venda selecionada e aberta a Consulta de Produtos pertence à empresa 1. Sendo assim, com a marcação realizada, o campo **"Estoque"** apresentará 100 unidades.

Sendo que:

- Se a Consulta de Produtos for aberta fora da Central de Notas, ou seja, diretamente pelo menu **"Comercial > Consulta > Consulta de Produtos"**, essa marcação não executará sua funcionalidade;
- Se houver configurada uma empresa no item **"Nome Empresa"** e essa marcação estiver selecionada, será utilizada a empresa discriminada na nota.

Nas abas **"Nome empresa"** e **"Local"** você poderá adicionar as empresas e locais a serem filtrados.

No grupo **"Filtro"**, poderá ser configurado um filtro personalizado com o auxílio do **"Facilitador"** que tem o funcionamento análogo ao componente Assistente de filtro.

Se você optar por digitar uma expressão de filtro na caixa de texto, localizada no grupo **"Filtro"**, será possível verificar se a expressão é válida através do botão **"Validar Filtro"**.

A visualização do novo filtro de Estoque cadastrado no painel de resultado pode ser configurada através da aba [Layout da célula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abalayoutdaclula).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdopainelderesultado)

### Aba Layout da célula

Nessa aba você configura a aparência do painel de resultado. Na grade de linhas, será possível inserir linhas para exibição das informações no layout. Na parte inferior esquerda da aba estão os campos disponíveis para serem utilizados no layout e ao lado direito, as colunas que serão apresentadas na linha selecionada.

![Imagem 10: Nessa aba você configura a aparência do painel de resultado. Na grade de linhas, será possível inserir linhas para…](https://ajuda.sankhya.com.br/hc/article_attachments/4407426697495)

**Nota:** No modo de visualização grade, cada produto ocupará apenas uma linha da grade. Se houver mais de uma linha configurada, o sistema apenas obedecerá a ordem de cada linha para exibição das colunas.

É possível alterar as configurações de exibição das colunas. Para isso, é necessário selecionar o campo no painel de colunas escolhidas. O sistema exibirá logo abaixo o painel **"Detalhes da coluna"**.

Nesse painel é possível configurar a fonte (letra), o tipo, cor, tamanho e a formatação (negrito, itálico e sublinhado).

Quando a marcação **"Exibir coluna?"** não estiver selecionada, a coluna não será exibida na tela.

Ao acionar a marcação **"Apresentar somente o valor"**, a descrição da coluna não será exibida na tela.

No exemplo abaixo, temos as alterações que estão sendo realizadas.

![Imagem 11: No exemplo abaixo, temos as alterações que estão sendo realizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/4407427059223)

Abaixo, temos na imagem como a coluna Preço será exibida na tela com as configurações realizadas:

![Imagem 12: Abaixo, temos na imagem como a coluna Preço será exibida na tela com as configurações realizadas:](https://ajuda.sankhya.com.br/hc/article_attachments/4404800165783)

Você também pode alterar a forma de visualização dos preços promocionais; sendo assim, teremos uma diferenciação entre o preço padrão e a promoção. Para isso, é necessário analisar os seguintes pontos:

- O produto deve estar previamente cadastrado e com uma promoção vigente cadastrada na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111833);
- Nas Configurações do painel de resultados, aba Preços, a marcação "Mostrar promoção na grade principal" necessita estar selecionada;
- Ainda nas Configurações do painel de resultados, aba Layout da célula, ao selecionar no quadrante Colunas escolhidas para a linha "Padrão" a linha relacionada ao **"Preço"** temos a aba Detalhes da coluna "Promoção" que permitirá as alterações de visualização:

![Imagem 13: Ainda nas Configurações do painel de resultados , aba Layout da célula , ao selecionar no quadrante Colunas escolhidas…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006186182)

Na imagem abaixo, observe como a coluna será apresentada após as devidas configurações:

![Imagem 14: Na imagem abaixo, observe como a coluna será apresentada após as devidas configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/1500006186242)

**Observação:** No exemplo apresentado acima, foi empregado um produto que não se encontra em promoção.

Através do botão ![Imagem 15: Através do botão "Dimensionar o tamanho das imagens" , você pode definir o tamanho das imagens que serão exibidas no…](https://ajuda.sankhya.com.br/hc/article_attachments/16105918240279) **"Dimensionar o tamanho das imagens"**, você pode definir o tamanho das imagens que serão exibidas no modo lista e coluna. Ao clicar no botão, será aberta uma janela para você utilizar as barras de dimensionamento horizontal e vertical ou digitar nas caixas **"Largura"** e **"Altura"** o tamanho desejado para as imagens em pixels.

![Imagem 16: Através do botão "Dimensionar o tamanho das imagens" , você pode definir o tamanho das imagens que serão exibidas no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006186322)

O botão ![Imagem 17: O botão "Configurar a quantidade de colunas" permite que você configure a quantidade de colunas a serem exibidas no…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903395351) **"Configurar a quantidade de colunas"** permite que você configure a quantidade de colunas a serem exibidas no modo de visualização Coluna. Seu acionamento exibe o seguinte pop-up:

![Imagem 18: O botão "Configurar a quantidade de colunas" permite que você configure a quantidade de colunas a serem exibidas no…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006186362)

Assim, indique no campo **"Quantidade de colunas"** a quantidade de colunas a serem apresentadas.

O sistema está preparado para trabalhar com a escolha de preços (nos casos em que se tenha mais de um preço) na inserção dos produtos no Carrinho de Compras. Para isso, ainda na aba Layout da célula, deve-se contextualizar os preços no Painel de Resultados. Caso seja informado apenas um preço, ao inserir o produto no Carrinho de Compras, o preço contextualizado será para ele levado. Caso sejam definidos mais de um preço, o sistema apresentará um pop-up para escolha de qual preço deverá ser utilizado. Para isso, realize a seguinte configuração:

Posicionado na aba Layout da Célula, escolha as tabelas disponíveis no painel **"Preços"** e mova as tabelas de preço para o painel **"Colunas escolhidas para a linha Padrão"**.

Assim, na Consulta de Produtos, quando o produto for incluído no Carrinho de Compras, será apresentado o pop-up de nome **"Detalhes da Venda"** para escolha do preço.

**Nota:** Na inserção de um ou mais produtos no Carrinho de Compras, para que se tenha o preço dos itens apresentado corretamente, na seção Colunas escolhidas para a linha "Padrão" você deve selecionar a coluna Preço; essa configuração também evitará que um produto em promoção tenha uma solicitação de liberação de desconto indevida ao ser incluso na nota.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdopainelderesultado) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Configurações da Consulta de Produtos

Através do botão ![Imagem 19: Através do botão "Configuração Consulta de Produto" você poderá configurar essa rotina. Ao clicar nesse botão, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903400855) **"Configuração Consulta de Produto"** você poderá configurar essa rotina. Ao clicar nesse botão, o sistema passará para o modo onde será possível realizar essas configurações.

| [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#bot%C3%B5esdotopodatela) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abageral) |
| --- | --- |
| [Aba Detalhes de estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abadetalhesdeestoque) | [Aba Características do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abacaractersticasdoproduto) |
| [Aba Outras informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaoutrasinformaes) | [Aba Configuração do Carrinho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaconfiguraodocarrinho) |
| [Aba Detalhes Adicionais de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abadetalhesadicionaisdepreo) | [Painéis Personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#h_01JFG019HCRT6PFCHRC33H4GR2) |
| [Cor de fundo da grade no Painel Personalizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#cordefundodagradenopainelpersonalizado) |  |
| [Enviar preço do Painel Personalizado para o carrinho de compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#Enviarpre%C3%A7odoPainelPersonalizadoparaocarrinhodecompras) |  |

### Botões do topo da tela

Quando você realizar um redimensionamento dos painéis na Consulta de Produtos, o sistema irá salvar as posições do layout automaticamente, assim que se realizar uma pesquisa. Sendo assim, ao acessar a tela, os painéis serão apresentados conforme a última configuração realizada. Teremos então os seguintes botões:

![Imagem 20: "Restaurar layout dos painéis" : Quando esse botão for utilizado, o layout original da tela será restaurado,…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903402263) **"Restaurar layout dos painéis"**: Quando esse botão for utilizado, o layout original da tela será restaurado, substituindo àquela realizada anteriormente.

**Importante:** ao acessar a tela de Consulta de Produtos pela primeira vez, o layout padrão será exibido, incluindo a grade de Consulta de Produtos com os campos **"Código"**, **"Descrição"**, **"Preço"** e **"Estoque"**. Após configurar a tela de acordo com suas preferências e salvá-la, o novo layout será associado ao seu ID de usuário e o sistema irá considerá-lo como padrão.

![Imagem 21: "Copiar personalização" : Ao utilizar esse botão, o pop up "Copiando configurações" será exibido. Nele você poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903403159) **"Copiar personalização"**: Ao utilizar esse botão, o pop up **"Copiando configurações"** será exibido. Nele você poderá copiar as configurações do layout de outros usuários, sendo um **"Usuário logado"** ou **"Outro Usuário"** do sistema.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

### Aba Geral

![Imagem 22: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/18694947149719)

Quando a marcação **"Usa carrinho de compras?**" estiver selecionada, no painel Detalhes de Estoque será exibido o carrinho de compras para que você possa acrescentar produtos ao carrinho utilizando o estoque disponível, bem como, irá habilitar a aba [Configuração do Carrinho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaconfiguraodocarrinho).

Caso a marcação **"Exibir painel de classificadores?"** esteja habilitada, será exibido o painel **"Classificadores"** com os produtos organizados de acordo com a sua classificação.

Por padrão, todos os produtos que estiverem em promoção, terão suas linhas destacadas na cor amarela mas, se você desejar alterá-la, faça através do campo **"Cor para produtos em promoção na grade principal"**.

- O produto deverá estar cadastrado na tela de [Descontos promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111833);
- Na tela de Consulta de Produtos, em Configurações do Painel de Resultados, aba Preços, efetue a marcação **"Mostrar Promoção na grade principal?"**. Assim, uma coluna será apresentada na grade principal com o valor do produto em promoção.

Uma observação importante com relação à descrição dessa coluna é que ela sempre terá a descrição **"Promoção"** juntamente com o nome da descrição do preço.

De acordo com a configuração do campo **"Cor para produtos em liquidação na grade principal"**, os produtos que estiverem em liquidação terão suas linhas destacadas na cor vermelha mas, se você desejar alterá-la, faça por esse campo.

Para que o produto em liquidação seja visualizado de forma destacada na tela de Consulta de Produtos, são necessárias as seguintes configurações:

- O produto deverá estar inserido em um Desconto promocional e, nessa configuração do desconto, com a marcação **"Liquidação"** efetuada;
- Na própria tela de Consulta de Produtos, é necessário que a coluna referente ao preço esteja selecionada na grade, e no botão **"Configuração Painel de Resultado"**, a marcação **"Mostrar promoção na grade principal"**, presente na aba **"Preços"**, esteja efetuada.

**Observação:** Essas configurações serão visualizadas somente se, na grade principal, estiver mostrando pelo menos uma coluna de valor de produto em promoção e o valor da promoção for diferente de zero. Se essas condições não forem satisfeitas, a linha na grade de produtos não será destacada de cor diferente.

Quando o produto está em promoção, é exibido um ícone marcador ![CONPROD18](https://ajuda.sankhya.com.br/hc/article_attachments/360060988134) para destacar o produto em promoção em relação aos demais.

Determine no campo **"Cor para produtos com estoque negativo ou sem estoque na grade principal"**, a cor da linha para destacar os produtos sem estoque ou com estoque negativo. É importante ressaltar que, sempre que a coluna Estoque (configurada na aba [Layout da célula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353#abalayoutdaclula) do botão Configuração Painel Resultado) estiver visível, as linhas exibidas com estoque negativo ou zerado serão coloridas conforme configurado. Caso essa coluna não esteja visível, somente as linhas do painel Detalhes de Estoque serão coloridas.
Considere ainda que, se já houver cores definidas para produtos em promoção ou liquidação e esses mesmos produtos não possuírem estoque, automaticamente a cor de destaque será alterada para a cor determinada no campo Cor para produtos com estoque negativo ou sem estoque na grade principal.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

### Aba Detalhes de estoque

![Imagem 24: Aba Detalhes de estoque](https://ajuda.sankhya.com.br/hc/article_attachments/1500006188162)

Nessa aba você configura a apresentação do painel **"Detalhes de estoque"**.

Caso a marcação **"Apresentar estoque por empresa"** esteja selecionada, a marcação **"Apresentar estoque por empresa soma"** será desabilitada.

Ao habilitar a marcação Apresentar estoque por empresa soma, o estoque será apresentado agrupando pela empresa da soma, ou seja, pode-se visualizar a soma do estoque de todas as empresas do grupo.

**Observação:** quando esta marcação estiver realizada, não será possível verificar nos campos **"Cód. empresa"** e **"Nome empresa"** todas as empresas que estão somando seus estoques. Essa marcação é exclusivamente para somar/agrupar o estoque das empresas. Porém, através do campo Grupo de estoque pode-se visualizar à qual grupo pertence aquele estoque que foi somado. Essa visualização se dará se o campo **"Empresa para agrupar estoque"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) estiver preenchido. Por exemplo:

Tem-se o seguinte estoque:
**Empresa 1**: 5.000
**Empresa 2**: 5.000
**Empresa 3**: sem estoque
**Empresa 4**: 5.000

Se a configuração do campo Empresa para agrupar estoque for realizada da forma abaixo:

Empresa 1 possui o campo Empresa para agrupar estoque preenchido com a empresa 1;
Empresa 2 possui o campo Empresa para agrupar estoque preenchido com a empresa 1;
Empresa 3 possui o campo Empresa para agrupar estoque preenchido com a empresa 1;
Empresa 4 possui o campo Empresa para agrupar estoque vazio;

E a marcação Apresentar estoque por empresa soma estiver habilitada, será possível visualizar o campo Grupo de estoque da Consulta de Produtos da seguinte forma:

**Estoque**: 5.000 com o Grupo de estoque vazio (referindo-se ao estoque da empresa 4, visto que o campo Empresa para agrupar estoque está vazio);
**Estoque**: 10.000 com o Grupo de estoque 1 (referindo-se ao estoque da empresa 1, agrupando as empresas 1 e 2 somente, visto que a empresa 3 não possui estoque).

Portanto, para saber quais empresas estão somando o estoque (quando a marcação está habilitada) basta visualizá-las através do campo Grupo de estoque.

Se a marcação **"Apresentar estoque por local"** estiver acionada, você poderá visualizar o estoque agrupado por cada local.

Com a marcação **'Apresentar estoque por local'** ativada, o sistema exibirá os locais de estoque ordenados pela menor quantidade disponível primeiro. Ao adicionar o produto ao carrinho, será utilizado sempre o primeiro local que aparece na lista, que, devido à ordenação, pode não ter saldo em estoque.

Caso não selecione nenhuma linha em **'Detalhes de estoque'** e adicione o produto pela grade principal, o sistema irá adicionar o 1º registro ao carrinho.

Se desejar que o sistema siga as Preferências da empresa, basta desativar essa marcação.

Quando a marcação **"Apresentar estoque por controle"** estiver ligada, você conseguirá visualizar o estoque agrupado por cada controle. Associado à esta marcação, utilizando o Carrinho de Compras, temos a possibilidade de configuração do parâmetro **"Lote no carrinho de compras? - LOTECARCOMP"** que, quando ativado, caso o produto inserido no carrinho possua controle, essa informação também irá para a Central de Notas. Para que esse comportamento ocorra quando o parâmetro for acionado, é necessário que a marcação Apresentar estoque por controle esteja efetuada.

Se desejar que o sistema siga as Preferências da empresa, basta desativar essa marcação.

**Observação:** para que a explosão de lotes seja feita na Central de Notas após carregar os produtos no carrinho é necessário que o parâmetro LOTECARCOMP esteja habilitado, a opção Apresentar estoque por controle deve estar necessariamente desmarcada e a opção Apresentar estoque por local, ativada. Desta forma, ao adicionar o número de itens desejados no carrinho e clicar em **"Terminar Seleção"** será efetuada a explosão de lote na Central. Caso a opção Apresentar estoque por controle esteja marcada e a opção Apresentar estoque por local desabilitada, será considerado o primeiro lote disponível e não será realizada a explosão, fazendo apenas a validação sem controle.

Se a marcação **"Apresentar estoque por parceiro"** estiver selecionada, você poderá visualizar o estoque agrupado por cada parceiro.

Se você habilitar a marcação **"Usar casas decimais do cadastro de produtos"**, poderá visualizar o estoque e o preço com as casas decimais definidas no cadastro do produto.

Caso a marcação **"Levar estoque p/quantidade"** esteja habilitada, todo o estoque disponível do produto será adicionado ao carrinho de compras, da mesma forma que se, na grade principal da Consulta de Produtos for dado um duplo clique para levar à Central de Notas, também levará a quantidade total para o item da nota.

Quando a marcação **"Apresentar somente estoque agrupado maior que zero"** estiver acionada, o sistema só trará no conteúdo da grade de detalhes do estoque as linhas cujo estoque agrupado (o calculo não inclui as reservas e quantidade bloqueada por WMS) é maior que zero.

Ao habilitar a marcação **"Apresentar somente estoque disponível agrupado maior que zero"**, o sistema só vai trazer no conteúdoda grade de detalhes do estoqueas linhas cujo estoque menos a reserva menos a quantidade bloqueada pelo WMS é maior que zero.

O parâmetro **"Desconsidera estoque em doca do WMS? - SUBESTDOCAWMS"** quando ligado, subtrai do estoque a quantidade que está na doca, o que se faz necessário nas situações de venda, para que o sistema não considere os produtos que não foram armazenados ainda. Na Consulta de Produtos é verificada a quantidade que está na doca e ela é subtraída das colunas **"Estoque"** e **"Disponível"** presentes na grade **"Detalhes de Estoque"**. Para que o estoque da Doca seja considerado, é necessário que a mesma seja do tipo Entrada/Saída ([Cadastro de Docas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612974), campo Tipo doca).

**Nota:** A tela de Consulta de Produtos não considera o critério do parâmetro **"Critério adicional para catálogo de produtos - QRYCONSPROD"**, sempre apresentando todos os Produtos/Serviços.

Ao selecionar o produto no painel **"Detalhes de estoque"**, será sugerido o valor do estoque menos reserva para o carrinho de compras. A sugestão varia de acordo com o local.

Essa quantidade poderá ser alterada para um número personalizado, não sendo necessariamente adicionada no carrinho a quantidade total de itens.

Ao inserir quantidade do produto para o carrinho e clicar no botão **"Terminar seleção"**, o campo **"Quantidade"** da central de notas é preenchido conforme a quantidade do carrinho de compras.

**Observação:** Esse processo ocorrerá quando a Consulta de Produtos for acessada através das Centrais.

Se a marcação **"Levar estoque p/ a quantidade"** estiver desfeita, na aba Detalhes de estoque será adicionado no carrinho apenas um item e não todos os itens disponíveis no estoque.

Também é possível fazer a inserção direta do produto na central de notas pela tela de Consulta de Produtos. Nesse caso, ao dar duplo clique no produto escolhido, com a condição de que o carrinho esteja vazio, o sistema irá carregar o produto na grade **"Itens"** da nota para que você informe a quantidade desejada.

Se o carrinho não estiver vazio, cada duplo clique no produto escolhido aumentará em 1 a sua quantidade no carrinho de compras e, será necessário utilizar o botão **"Terminar Seleção"** para que esse produto seja apresentado nos itens da nota.

**Nota:** Para que isso ocorra, o carrinho não poderá conter um produto diferente do selecionado.

Quando o carrinho possui produtos ou locais diferentes para o mesmo produto, ao terminar a seleção serão inseridos na central de notas itens de acordo com o carrinho de compras.

O comportamento do duplo clique é uma regra nativa e não pode ser desabilitado ou parametrizado. Quando o carrinho possui produtos ou locais diferentes para o mesmo produto, ao terminar a seleção serão inseridos na central de notas itens de acordo com o carrinho de compras.

**Observação:** Se os produtos a serem exibidos possuírem [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194), eles também serão exibidos na grade de produtos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

### Aba Características do produto

Nessa aba você define quais informações aparecerão no painel **"Características"**.

![Imagem 25: Nessa aba você define quais informações aparecerão no painel "Características" .](https://ajuda.sankhya.com.br/hc/article_attachments/1500006309281)

Quando a marcação **"Mostrar imagem do produto"** estiver selecionada, será exibida a imagem do produto no painel.

Os campos contidos na coluna **"Campos selecionados"** estarão visíveis no painel.

Ao visualizar as características do produto, os campos selecionados serão alimentados e apresentados na aba Detalhes, conforme imagem abaixo:

![Imagem 26: Ao visualizar as características do produto, os campos selecionados serão alimentados e apresentados na aba Detalhes ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4404842367127)

![Imagem 27: Ao consultar um produto com uma ou mais imagens cadastradas, é possível visualizá-las e ampliá-las. Para isso, basta…](https://ajuda.sankhya.com.br/hc/article_attachments/21484221964823) Ao consultar um produto com uma ou mais imagens cadastradas, é possível visualizá-las e ampliá-las. Para isso, basta clicar na imagem no painel Características e um pop-up será exibido com a qualidade correspondente, garantindo a visualização em sua resolução máxima. Se preferir, ao pressionar o botão **"Abrir original"**, a imagem será carregada em seu tamanho original em uma nova aba no navegador padrão.

[GIF animado: Imagem 28: Ao consultar um produto com uma ou mais imagens cadastradas, é possível visualizá-las e ampliá-las. Para isso, basta…](https://ajuda.sankhya.com.br/hc/article_attachments/18948960328343)

A aba **"Perfil"** é habilitada mediante liberação do opcional **"Telemarketing"**.

A aba **"Componentes"** possibilita consultar os componentes dos produtos similares na grade principal da tela de Consulta de Produtos assim como na grade de Produtos Alternativos, apresentando os componentes cadastrados na aba Componentes da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

Quando é selecionado um produto alternativo, os outros painéis são atualizados com base no produto alternativo selecionado. Para que você saiba exatamente de qual produto são as informações, a tela Consulta de Produtos mostra no rodapé qual o produto está selecionado; esse rodapé somente é apresentado quando o painel de produtos alternativos está sendo apresentado, ou se ele for um link, quando a tela correspondente está aberta. Quando você selecionar o produto principal, o sistema apresenta o rodapé exibindo o código, descrição e complemento do produto; quando você seleciona um produto alternativo, o sistema apresenta este rodapé na cor vermelha e ao lado direito, o texto **"Produto alternativo"** para te indicar que as informações apresentadas nos painéis são referentes ao produto alternativo e não do produto principal.

Quando se trabalhar também com produtos substitutos, o mesmo irá ocorrer, ou seja, sendo selecionado um produto substituto, no rodapé da tela será apresentada a informação na cor vermelha, constando a frase que o item é substituto.

Ainda na aba Características do Produto, quando se trabalha com **"Produtos Substitutos"** (parâmetro **"Permite cadastro de produtos substitutos? - PERCADPRODSUBST"** ativado), será possível que você escolha os campos **"Data da Substituição do Produto"** e **"Código do Produto Substituto"** para visualização, bastando incluí-los na coluna de **"Campos Selecionados"**.

**Nota:** na Central de Notas, ao tentar vender um produto que não possui estoque, mas possui um produto substituto vinculado a ele, será apresentado o seguinte questionamento na tela:

**"Estoque insuficiente para o Produto "X". Existem produtos substitutos, deseja visualizar?"**

Ao clicar em **"Sim"**, é aberta uma tela apresentando uma lista de produtos substitutos para o item sem estoque; com isso, pode-se selecionar um produto e este será posicionado na grade de inserção de itens.

**Observação:** somente os campos presentes na tabela de Produtos estarão disponíveis para preenchimento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

### Aba Outras informações

Nessa aba o sistema lista todos os painéis de informações sobre o produto. Cada painel pode ser definido como **"Link"**, **"Painel"** ou **"Não Exibir"**.

Quando um painel é definido como Link, será criado um link no painel **"Outras Informações"** através do qual você poderá abrir o painel correspondente.

Se for definido que o item deverá aparecer como Painel, o sistema criará um painel na tela.

Se for marcado **"Não exibir"**, você não visualizará o painel.

A imagem a seguir mostra a configuração para criar na tela de Consulta de Produtos, os painéis **"Detalhes de estoque"** e **"Detalhes de preço"**. Serão criados links para acessar os painéis **"Entradas Pendentes"**, **"Características"**, **"Extensões de Garantia"**, **"Produtos alternativos"**, **"Produtos sugeridos na venda"**, **"Reservas"** e **"Série"** no painel **"Outras informações"**, enquanto os demais itens não serão exibidos na tela.

![Imagem 29: A imagem a seguir mostra a configuração para criar na tela de Consulta de Produtos , os painéis "Detalhes de estoque" e…](https://ajuda.sankhya.com.br/hc/article_attachments/11003801839383)

**Observação:** as informações do painel Extensões de Garantia estão atreladas ao painel Detalhes de preço; portanto, serão exibidas de acordo com as configurações abaixo:

- Quando os dois (Detalhes de Preço e Extensão de Garantia) forem definidos como Painel, seus valores serão atualizados automaticamente.
- Quando o painel Detalhes de preço estiver configurado como Link, é necessário clicar no respectivo link para que os valores do painel Extensões de Garantia sejam atualizados.

Como dito, a tela de Consulta de Produtos possui vários recursos para visualizações de informações inerentes aos produtos. Essas informações podem ser exibidas através de painéis ou de links, conforme configuração realizada nas [Configurações da consulta de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos).

Existe um painel/link que possibilita uma visualização de maneira mais rápida em clientes que são concessionárias, referente à quais modelos de veículos utilizam e/ou estão vinculados ao produto (peça) selecionado na tela. Para que a marcação **"Aplicação do Produto"** seja apresentada, é necessário que o parâmetro **"Utiliza modelo veículos para concessionárias? -USAMODVEICONCES"** esteja habilitado. Esses modelos deverão ser previamente cadastrados na aba **"Aplicação"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

Após ser configurado como link ou como painel, o sistema passará a apresentar os modelos de veículos vinculados ao produto selecionado.

**Nota:** No topo do painel **"Produtos sugeridos na venda"** temos o botão **"Adicionar produto com o estoque selecionado ao carrinho"**, que permite adicionar o item ao Carrinho de Compras, de modo que serão feitas diversas validações bem como, se já existe o item adicionado no carrinho, ou se quantidade negociada corresponde ao agrupamento mínimo de acordo com definição do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

**Observação:** O sistema realizará a validação de produtos repetidos no momento de incluir os mesmos no carrinho, ou seja, imediatamente após clicar no botão **"Adicionar produto selecionado no carrinho"**. Assim, ao inserir produtos repetidos no carrinho, será emitida a seguinte mensagem:

**"Produto X - já existe no carrinho".**

**Nota:** Essa validação ocorrerá quando estiver incluindo produtos através dos painéis Produtos sugeridos na venda, Produtos alternativos e Painel de Produtos.

Ainda em relação aos painéis Produtos alternativos e Produtos sugeridos na venda, o sistema atualizará os painéis **"Detalhes de Estoque"** e **"Detalhes de Preço"** com as informações referente ao produto selecionado. Nos painéis acima informados, será possível visualizar diretamente na grade, alguns campos que facilitam o vendedor com informações corretas e mais rápidas referente ao produto, sem que seja necessário acessar outras telas do sistema.

**Observação:** Ao incluir um item no carrinho de compras por meio do painel Produto sugerido na venda ou pelo painel Produtos alternativos, o produto a ser incluído deverá ser o mesmo que estava selecionado em um desses painéis, e não o produto principal.

O parâmetro **"Contextualizar dados nota na consulta de produtos - BUSCONTXNOTAPRD"** influenciará na grade de Produtos alternativos e Produtos sugeridos para venda, sendo que, quando ele estiver habilitado, será possível realizar a contextualização de dados da nota. Este parâmetro será utilizado apenas em personalizações.

**Nota:** Primeiramente, o implantador deverá criar campos adicionais nas tabelas dos Produtos alternativos e/ou Produtos sugeridos na venda através da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294). Em seguida, deverá adicionar no campo **"Expressão"** dos campos adicionais que foram criados a seguinte expressão, por exemplo:

**#type.sql# SELECT ACT\_INT\_FIELD((SELECT SID FROM V$SESSION WHERE AUDSID = (SELECT USERENV('SESSIONID') FROM DUAL)), 0, 'CODVEND') FROM DUAL**

Os dados serão contextualizados através da tabela EXECPARAMS, onde a chave para coleta dessas informações será pelo SESSIONID da conexão.
**Importante:**  quando o parâmetro **"Tipo de direção para considerar na visualização de Produtos alternativos - TIPDIRPROALT"** estiver configurado com a opção **"Bidirecional"**, todos os produtos alternativos do produto selecionado e, os produtos alternativos desses produtos serão apresentados na grade de Produtos alternativos.

Ainda no painel Outras informações, na opção **"Reservas"**, são apresentados os dados originados do lançamento de um pedido de venda. Na opção **"Entradas Pendentes"**, é possível visualizar também o **"Número Pedido"**, informação esta originada de um pedido de compra.

Através da definição realizada no parâmetro **"Qual Dt.Previsão mostrar no painel Ent.Pendentes? - DTPREVENTPEND"**, determina-se qual campo de Dt. Previsão Entrega será exibido na grade Entradas Pendentes; pode-se fazê-lo dentre as opções Da Nota ou Do Item; a primeira opção indica que o sistema irá apresentar o campo "Dt. Previsão de Entrega" do pedido/nota; já na segunda opção, será exibido o campo **"Dt. Prev. Entrega"** correspondente aos itens.

**Importante:** O campo Data Previsão de Entrega, tanto em relação ao pedido/nota ou em relação aos itens, deve ser previamente inserido no layout do documento que está sendo lançado, através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) para que, consequentemente, sejam alimentados e assim exibidos na Consulta de Produtos.

**Nota:** Ao visualizar o quadrante Entradas Pendentes em modo grade, será possível notar ao final da coluna Quantidade um totalizador de seus valores.

Através do Painel de Cotação, será possível visualizar informações referente aos itens que estão sendo cotados, para isto, temos os campos **"Observação (Item Cotação)"** e **"Observação (Cotação)"**.

Por meio da opção **"Componente BI"** você pode adicionar paineis personalizados para, por exemplo, visualizar indicadores através de gráficos. Para isso, você deve configurar no **"Painel Personalizado"** o campo **"Tipo de entrada"**, com a opção **"Componente BI"** e selecionar no campo **"Componente"** o componente que será utilizado como painel.

Desse modo, quando você pesquisar pelo produto desejado por meio da tela de Consulta de Produtos ou quando estiver efetuando o lançamento de um Pedido de Venda/Compra na tela Central de Vendas/Compras, no painel Componente BI será apresentado as informações de acordo com as configurações realizadas.

**Observação:** o painel personalizado Componente BI não foi implementado para o layout Flex, dessa forma, quando utilizar a Consulta de Produtos em Flex, o painel será apresentado em branco. Porém, você poderá visualizá-lo normalmente no layout HTML5.

### Painéis Personalizados

É possível incluir painéis personalizados na Consulta de Produtos. Na borda direita da aba, temos o botão **![Imagem 30: É possível incluir painéis personalizados na Consulta de Produtos . Na borda direita da aba, temos o botão "Adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/16105918247575) "Adicionar Painel Personalizado"** que, ao ser acionado, exibe um pop-up que permite adicionar esses painéis:

![Imagem 31: É possível incluir painéis personalizados na Consulta de Produtos . Na borda direita da aba, temos o botão "Adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006310081)

Inicialmente, é necessário informar um **"Título"** para o painel que está sendo criado. Logo após, indique qual será o **"Tipo de Entrada"** que será aplicada. Temos as seguintes opções:

**Rotina de Banco de Dados:** Nessa rotina, a **"Expressão SQL"** trará os dados a serem exibidos. Você pode utilizar alguns parâmetros que serão injetados no momento da execução da consulta, como CODPROD, CODEMP, CODPARC, NUTAB. Esses parâmetros deverão ser inseridos com dois pontos antes dos seus nomes. O parâmetro CODPROD sempre estará disponível, os demais precisam estar contextualizados a partir de um filtro, de acordo com o tipo de tabela de preço ou se a Consulta de Produtos for aberta a partir das Centrais.

**Detalhes da Implementação do Módulo Java (Interface** `CustomPanel`**)**

A `Rotina Java` utiliza um `Módulo Java` (`.JAR`) que deve implementar a interface `CustomPanel` do sistema para interagir corretamente com a Consulta de Produtos. Esta interface define os métodos que o painel personalizado deve expor para que o sistema possa carregar, exibir e interagir com os dados retornados.

A `Classe Java` apontada deve ser a classe principal que implementa esta interface. É possível personalizar a consulta ou criar novos arquivos `.JAR`, desde que atendam às especificações necessárias da interface.

Essa rotina utiliza um **"Módulo Java"** que comporta um arquivo .JAR com uma consulta ao banco de dados que retorna as informações. É possível personalizar a consulta desse arquivo ou criar outro(s), desde que atenda às especificações necessárias. Além disso, deverá ser apontada a **"Classe Java"** para a ação.

**Observação:** Para que seja permitido que o painel personalizado adicione itens no carrinho, o campo **"Consulta (Expressão SQL)"** (para `Rotina de Banco de Dados`) ou o `Módulo Java` (para `Rotina Java`) deve retornar no mínimo as informações CODPROD, CODVOL, CODLOCAL, CONTROLE. Caso contrário, ao tentar incluir um item no carrinho o sistema irá notificar que é necessário indicar essas informações.

**Tratamento de Nomes de Colunas Padrão**

Quando o painel personalizado utiliza colunas com nomes padrão como CODPROD ou CODVOL, o sistema pode entender que deve exibir o painel lateral de seleção de unidades. Para evitar essa exibição automática, é recomendável usar nomes alternativos para essas colunas, como por exemplo: CODPROD = PRODUTO, CODVOL = CODUN.

**Componente BI:** Para inserir Componentes de BI como painéis da tela Consulta de Produtos, selecione no campo **"Tipo Entrada"** a opção **"Componente de BI"**, assim será apresentado o campo **"Componente de BI"**; nele, busque pelos componentes existentes e escolha qual será utilizado como painel. Lembrando que é necessário criar primeiramente, na tela [Construtor de Componentes de BI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044605354), os componentes de BI para que eles sejam apresentados no campo Componente.

Você também poderá ![Imagem 32: Você também poderá "Editar" e/ou "Remover" um painel personalizado já criado.](https://ajuda.sankhya.com.br/hc/article_attachments/16105903404695) **"Editar"** e/ou ![Imagem 33: Você também poderá "Editar" e/ou "Remover" um painel personalizado já criado.](https://ajuda.sankhya.com.br/hc/article_attachments/16105918249879) **"Remover"** um painel personalizado já criado.

Todas as ações possíveis de serem realizadas com os painéis do sistema podem ser realizadas nos painéis personalizados, como por exemplo, a ordenação, a exibição como link, entre outros.

**Observação:** ao habilitar o parâmetro **"Ignora desc. promocional qdo usando preço painel personalizado - IGNDESCPROCARR"**, o sistema não irá considerar as regras de desconto promocional de forma que, nenhum desconto nos itens será aplicado ao usar um painel personalizado que possua a coluna **"Preço"** na Consulta de Produtos. Assim, o valor da negociação será mantido conforme os valores selecionados no painel personalizado. Porém, quando desativado, haverá o ajuste do preço com base na aplicação de descontos promocionais vigentes, caso haja.

![Imagem 34: Esse parâmetro é válido somente para descontos promocionais, ou seja, qualquer outro desconto cadastrado será…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903413271) Esse parâmetro é válido somente para descontos promocionais, ou seja, qualquer outro desconto cadastrado será considerado soberano referente ao comportamento do IGNDESCPROCARR.

Informe no parâmetro **"Decimais para valor em painel personalizado - DECPAINELPERSON"**, no campo **"Inteiro"**, a quantidade de casas decimais que deseja visualizar nos campos numéricos do Painel personalizado. Por padrão, este campo é exibido com o valor 2. Vale destacar que esse parâmetro funcionará apenas no layout [HTML5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110733-HTML5).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

### Cor de fundo da grade no Painel Personalizado

Caso queira adicionar o recurso de cor de fundo da grade no Painel personalizado, é necessário que o implantador realize a configuração abaixo:

- Adicionar um novo Painel personalizado usando uma query no campo Consulta (Expressão SQL) como no exemplo abaixo. Desse modo, quando o vendedor consultar um produto, a cor da linha deste produto será exibida de acordo com a regra personalizada.

CASE WHEN A.PERCENTUAL < 0 AND ABS(A.PERCENTUAL) BETWEEN 0 AND 4 THEN '#E9967A'

![Imagem 35: CASE WHEN A.PERCENTUAL < 0 AND ABS(A.PERCENTUAL) BETWEEN 0 AND 4 THEN '#E9967A'](https://ajuda.sankhya.com.br/hc/article_attachments/11305059483671)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

**Enviar preço do Painel Personalizado para o carrinho de compras**

Por meio do Painel Personalizado, pode-se criar uma consulta que recupere informações de preço e, em seguida, esses dados podem ser enviados diretamente para o carrinho de compras. Para que esse processo ocorra de forma adequada, a consulta deve incluir obrigatoriamente as colunas 'PRECO' e 'NUTAB' (pertencentes à tabela de preços). Além disso, é fundamental garantir que o parâmetro **"Usar Preço de Painel Personalizado no Carrinho - USAPRECOCARR"** esteja ativado.

Existem outros parâmetros que podem ser utilizados juntos ao parâmetro USAPRECOCARR. São eles:

- **"Habilita desconto no carrinho de produtos - HABDESCCARRINHO"**: Com esse parâmetro ligado é possível configurar o campo **"Desc. Total"** para que seja exibido no carrinho.
- **"Decimais para custo - CUSTODEC"**: Neste parâmetro, você pode configurar a quantidade de casas decimais referente ao **"Preço"** do produto.
- **"Aplicar vlr editado da Consulta Prod. na Central? - APLVLRUNITEDIT"**: Com este parâmetro habilitado, ao selecionar o produto através da tela Consulta de Produtos para que seja inserido na nota, o sistema irá carregar o valor exibido no campo **"Vlr. Unit."**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

**Aba Configuração do Carrinho**

Essa aba será habilitada quando a marcação **"Usar carrinho de compras"** da aba Geral estiver selecionada.

![Imagem 36: Essa aba será habilitada quando a marcação "Usar carrinho de compras" da aba Geral estiver selecionada.](https://ajuda.sankhya.com.br/hc/article_attachments/1500006310281)

Quando a marcação **"Exibir último valor de venda dos produtos"** for efetuada, na realização de uma negociação com o cliente, utilizando o Carrinho de Compras, o valor do último valor negociado será demonstrado de modo a facilitar a negociação. Para que essa visualização ocorra, é necessário que na visualização do carrinho de compras, a coluna **"Últ. Vlr. Venda"** esteja entre as colunas selecionadas; nela, será apresentado o último valor de venda do **"Produto",** podendo considerar o "Parceiro" e/ou a "Empresa" informados na negociação.

**Importante:** Ao realizar o lançamento de um Pedido de Venda, Requisição ou uma Transferência, caso o parâmetro **"Ignorar preço do carrinho na movimentação interna? - IGNPRECARMOVIN"** esteja ativado, na inserção dos produtos no Carrinho de Compras, será utilizado como preço, o valor correspondente à configuração realizada no campo **"Usar como Preço"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado no lançamento.

![Imagem 37: Em casos de Transferência entre locais, o Carrinho de Compras não permitirá o lançamento, pois possui validações que…](https://ajuda.sankhya.com.br/hc/article_attachments/23027952819351) Em casos de Transferência entre locais, o Carrinho de Compras não permitirá o lançamento, pois possui validações que impedem a finalização da seleção.

**Observação:** Incluindo um produto através do carrinho de compras, em um Pedido de Compra ou Nota de Compra e habilitando o parâmetro **"Alterar o preço do item de acordo com o TOP? - CONFPRECACORTOP"**, será utilizado como preço, o valor correspondente à configuração realizada no campo Usar como Preço, localizado na aba Geral do Tipo de Operação - TOP utilizado no lançamento.

A marcação **"Exibir carrinho no painel"**, quando selecionada, fará com que o painel **"Produtos no Carrinho"** seja apresentado na parte principal da tela Consulta de Produtos, abaixo da grade de produtos.

Efetuando a marcação **"Agrupar itens semelhantes"**, os itens idênticos (mesmo código, mesmo local, mesma unidade, mesmo controle) serão agrupados em uma só linha no carrinho de compras. Essa marcação irá influenciar nos lançamentos realizados na Central de Compras, Vendas e Movimentações Internas, sendo que, na aplicação de uma promoção por produto, quando esse item possuir um desconto por quantidade, será efetuado o seu agrupamento e aplicação do desconto.

> **Observação:** Quando a base estiver configurada com **Preço Dinâmico** (parâmetro `NOMPROCCALCPRE` preenchido), o agrupamento de itens semelhantes ocorrerá independentemente da marcação "Agrupar itens semelhantes" estar selecionada ou não. Isso acontece porque, nesse cenário, a lógica de agrupamento é aplicada prioritariamente pelo processamento do preço dinâmico. Portanto, se a base utilizar preço dinâmico, os itens idênticos (mesmo código, mesmo local, mesma unidade, mesmo controle) serão agrupados no carrinho de compras mesmo com a opção desmarcada.

Com a marcação **"Alertar sobre item semelhante"** realizada, caso o carrinho de compras já possua um item similar ao que está sendo incluído, será exibida a seguinte mensagem:

**"O carrinho já possui um item semelhante. Deseja continuar e adicionar o item ?"**

A marcação **"Verificar o agrupamento mínimo"** irá validar o agrupamento mínimo do produto no momento da sua inclusão no carrinho de compras. O valor mínimo de agrupamento é configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque) no campo **"Agrupamento mínimo"**. Caso seja informado um valor menor que o configurado para o agrupamento mínimo, será exibido o seguinte alerta:

**"Produto x - Produto x deve ser negociado em múltiplos de Y."**

Onde Y é o valor mínimo de agrupamento configurado.

**Observação:** O carrinho de compras conta com dois campos internos, Origem Busca e Produto Pesquisado, que visam identificar por onde foi feita a seleção do produto, se pelo Painel de consulta direta (consulta de produtos), Painel de produtos alternativos ou pelo Painel de produtos sugeridos na venda.

Quando a marcação **"Redirecionar foco para o campo de busca após inclusão do produto no carrinho"** estiver acionada, ao final da inclusão de um produto no carrinho de compras, o sistema automaticamente se posicionará no campo **"Busca"** localizado no topo da tela; viabilizando assim o processo de inclusão dos produtos.

![Imagem 38: Ao utilizar a marcação Redirecionar foco para o campo de busca após inclusão do produto no carrinho , o…](https://ajuda.sankhya.com.br/hc/article_attachments/23027952819351) Ao utilizar a marcação Redirecionar foco para o campo de busca após inclusão do produto no carrinho, o redirecionamento do foco só ocorrerá quando a tecla de seta para baixo é pressionada no teclado após a inclusão dos itens no carrinho. A tecla enter não ativa o redirecionamento do foco nesse cenário.

Para que seja apresentado o recurso de faróis no carrinho de compras, é necessário que sejam realizadas algumas configurações:

- Primeiramente, deve ser criada uma procedure no banco de dados para a tabela TGFCAC, que determinará a regra dos campos adicionais da Grade de Itens; já para os totalizadores de Rodapé do carrinho de compras, deve-se criar a procedure no banco de dados para a tabela TGFTCA;

Trigger modelo:

```
CREATE TRIGGER TGFCAC_ALTER_COLUMN

ON TGFCAC

AFTER UPDATE, INSERT

AS

BEGIN

DECLARE

@SEQCAC INT,

@NUNOTA INT,

@QTDPRODTOT FLOAT

SELECT @SEQCAC = SEQCAC,

@NUNOTA = NUNOTA

FROM INSERTED

UPDATE TGFCAC

SET AD_CAMPO_FAROL = (CASE WHEN TGFCAC.QTDPRODUTO < 5 THEN '#ff0303'

WHEN TGFCAC.QTDPRODUTO < 11 THEN '#faea01'

ELSE '#53bf14' END),

AD_VLRRENTA = 10

WHERE

NUNOTA = @NUNOTA

AND SEQCAC = @SEQCAC

SELECT @QTDPRODTOT = SUM(QTDPRODUTO) FROM TGFCAC WHERE NUNOTA = @NUNOTA

UPDATE TGFTCA

SET AD_TOTAL_FAROL = (CASE WHEN @QTDPRODTOT < 5 THEN '#ff0303'

WHEN @QTDPRODTOT < 11 THEN '#faea01'

ELSE '#53bf14' END),

AD_QTDTOT = (SELECT SUM(QTDPRODUTO) FROM TGFCAC WHERE NUNOTA = @NUNOTA)

WHERE

NUNOTA = @NUNOTA

END
```

- Após isso, deve-se habilitar o parâmetro **"Utiliza campos adicionais no carrinho? - USACAMPOSADCCAR"**. Dessa forma, será possível configurar na Grade de Itens do carrinho de compras um campo que exibe o farol e, assim, determinar na consulta de produtos as cores a serem apresentadas conforme a definição criada no campo;

**Nota:** os campos adicionais criados do tipo farol deverão, obrigatoriamente, serem do **"Tipo"** igual a **"Texto"**; esses campos deverão ser criados na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

Logo em seguida, deve-se adicionar os campos adicionais determinados como **"Farol"** na configuração do parâmetro **"Campos do tipo farol no carrinho - CAMPOSFAROLCAR"**, sendo que, esses campos adicionais deverão possuir o mesmo nome do campo criado na tela Dicionário de Dados.

**Observação:** é necessário realizar a configuração da Grade de Itens do carrinho de compras para que os campos criados anteriormente possam ser visualizados.

**Nota:** também será possível a exibição de faróis e campos adicionais nos totalizadores localizados no Rodapé do carrinho de compras; para isso, após a criação dos campos adicionais, deve-se inseri-los na configuração do parâmetro **"Campos do tipo farol nos totalizadores adicionais - CAMPFAROLTOTCAR"**.

**Observação:** ao ligar o parâmetro **"Habilita desconto no carrinho de produtos - HABDESCCARRINHO"**, no Painel de Carrinho será disponibilizada a coluna **"Desc. Total"** e um totalizador de mesmo nome no cabeçalho com o valor total descontado do carrinho. O campo Desc. Total do carrinho de produtos traz os descontos aplicados automaticamente através do desconto promocional, do Tipo de Negociação com **"Taxa em %"** do tipo desconto e/ou desconto simulado na própria Consulta de Produtos. No caso do desconto simulado, ele será levado para o carrinho apenas quando o parâmetro **"Aplicar desconto simulado no carrinho aos itens? - SIMDESCCPITENS"** estiver ligado.

Com a marcação **"Alertar sobre item semelhante no documento de origem"** habilitada, ao consultar um produto por meio de um documento de origem qualquer e tentar adicioná-lo ao carrinho, será exibida a seguinte mensagem:

**"O documento nro único 999999 já contêm um item semelhante. Deseja continuar e adicionar o item?."**

Se responder **"Sim"**, o produto será adicionado ao carrinho. Caso contrário, mesmo que o carrinho esteja vazio, esse produto não será incluído nele. 

Para adicionar produtos no carrinho pressionando a tecla **"Enter"**, ative a marcação **"Incluir produto no carrinho usando tecla Enter"**. Após a inclusão do produto, o cursor será automaticamente direcionado para o primeiro campo editável no painel **"Produtos no carrinho"**, onde é possível modificar as informações conforme necessário. Se desejar editar o próximo campo, utilize a tecla **"Tab"** do seu teclado. Para retornar ao campo anterior, basta pressionar **"Shift+Tab"**. Após concluir a inclusão/edição, para retornar a Central, clique no botão **"Terminar Seleção"** ou pressione as teclas **"Alt+T"**.

> **Notas sobre o comportamento da tecla Enter:**
>
> - **Redirecionamento de foco:** Se a marcação **"Redirecionar foco para o campo de busca após inclusão do produto no carrinho"** estiver ativada, ao pressionar **Enter** no último produto da grade, o cursor retornará automaticamente para o campo **"Busca"**.
> - **Alteração de configuração durante o processo:** Se houver mais de um item sendo incluído consecutivamente pela tecla **Enter**, o sistema manterá o comportamento de adição contínua, mesmo que a configuração seja desmarcada após a primeira inclusão. Isso ocorre porque a lógica da aplicação não reavalia a configuração para itens já em processamento no carrinho naquele momento.

**Seção Filtro Para Buscar Última Negociação**

Ao criar um filtro nessa seção, o sistema irá utilizá-lo no momento da busca, pesquisando a última negociação realizada com o cliente. Notemos que o botão **"Adicionar filtro"** é um filtro personalizado do cabeçalho e nele estará a condição para buscar a última nota. Por exemplo, se no filtro não for informado o tipo do movimento, a consulta ficará limitada à ordenação interna que é por data de negociação descendente e número único da nota, ou seja, se estiver na central com um pedido de venda aberto e solicitar na consulta a busca pela última negociação e esta for uma nota de compra, serão apresentados os itens da nota de compra; porém, se nesse filtro for solicitado para trazer somente o cabeçalho da nota, cujo tipo de movimento é **"Venda"**, então aparecerão os itens da última negociação do tipo de movimento Venda.

####

**Seção Filtro para buscar histórico de consumo**

Criando um filtro nessa seção, o sistema irá utilizar o filtro definido no momento de busca do histórico de consumo do cliente. Nesse filtro é possível configurar o filtro personalizado para o item da nota. Por exemplo, é possível configurar para que só sejam adicionados ao carrinho de compras, os produtos comprados pelo cliente que sejam do grupo de produtos = 30, para isso basta criar o filtro **"Produto > CODGRUPOPROD = 30"**.

Informe no campo **"Quantidade de dias retroação"** a quantidade de dias passados que o sistema deverá considerar ao buscar o histórico de consumo; se por exemplo for informado "30" e hoje for dia "15/10/2014", o sistema irá buscar as últimas negociações com a data de negociação maior ou igual à "15/09/2014".

Configure no campo **"Quantidade a ser usada"** qual será a regra para cálculo da quantidade do produto a ser adicionada ao carrinho de compras quando utilizada a opção **"Histórico de consumo"**. Escolha dentre as seguintes opções:

- Nenhuma;
- Última negociação;
- Somatório;
- Média;
- Maior;
- Menor.

Mesmo trazendo as quantidades de acordo com os itens da nota, o sistema irá analisar o agrupamento mínimo. Abaixo temos um exemplo:

O agrupamento mínimo é 12 para o produto 100.

Nota 1: quantidade: 12 (Data 16/06/2014)

Nota 2: quantidade: 24 (Data 20/06/2014)

Nota 3: quantidade: 36 (Data 25/06/2014)

Quantidadea ser usada for Maior: Qtde: 36

Quantidadea ser usada for Menor: Qtde: 12

Quantidadea ser usada for Média: Qtde: 24

Quantidadea ser usada for Soma: Qtde: 72

Quantidadea ser usada for Nenhuma: Qtde: 0

Se trocar o agrupamento para 10, iremos arredondar para cima. Considerando os mesmos dados do exemplo anterior.

Quantidadea ser usada for Maior: Qtde: 40

Quantidadea ser usada for Menor: Qtde: 20

Quantidadea ser usada for Média: Qtde: 30

Quantidadea ser usada for Soma: Qtde: 80

Quantidadea ser usada for Nenhuma: Qtde: 0

Ao enviar itens para o carrinho a partir do histórico de consumo, dependendo da opção selecionada no campo **"Preço de Venda"** o sistema terá o seguinte comportamento:

- Selecionando a opção **"Última negociação"**, será apresentado no carrinho e na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) o preço da última compra realizada para o parceiro definido.
- Indicando a opção **"Regra de precificação"**, no carrinho e na Central de Vendas será exibido o preço de venda atualizado do produto, conforme sua regra atual de preço.

**Observações:**

- Produtos inativos não serão adicionados ao carrinho.
- O sistema só considera notas confirmadas para buscar os itens.
- O parâmetro **"Tabela de Preços por - TIPTABPRECOS"** irá influenciar na execução do botão **"Histórico de Consumo"**, caso o parâmetro seja diferente de **"Parceiro"** ou esteja no contexto do parceiro e o mesmo não tenha sido escolhido, ao clicar no botão será aberto um pop-up para escolha do parceiro e, logo em seguida, o sistema apresentará os produtos do Histórico de consumo conforme configuração na aba **"Configuração do Carrinho"**.

Ao clicar no botão **"Visualizar carrinho de compras"**, o sistema exibirá no painel **"Produtos no carrinho"** os detalhes do carrinho de compras.

![Imagem 39: Ao clicar no botão "Visualizar carrinho de compras" , o sistema exibirá no painel "Produtos no carrinho" os detalhes do…](https://ajuda.sankhya.com.br/hc/article_attachments/4404842210583)

Serão exibidos os produtos inseridos ao carrinho de compras na grade. A grade do carrinho de compras permite que sejam realizadas alterações na quantidade e no valor de cada produto.

**Importante:** Ao selecionar um produto no Carrinho de Compras, quando se trabalha com [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854) Única (parâmetro Tabela de Preços por - TIPTABPRECOS), ou seja, Tabela "0" (zero) e o produto não possui preço de venda para essa tabela, teremos dois comportamentos:

1. Se o produto possuir algum Desconto Promocional configurado, o sistema emitirá a mensagem:

**"Produto "X" sem preço de tabela, não pode ser vendido."** - Nessa situação a mensagem será de obstrução e o produto não será carregado na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

2. Se o produto não possuir Desconto Promocional configurado, o sistema emitirá a mensagem de aviso:

**"A tabela contextualizada foi a tabela 0. Produto "X" sem preço de tabela, não pode ser vendido."** - Nesse caso, a mensagem será de aviso e o produto será carregado na Central de Vendas.

Na visualização dos produtos do carrinho, você também pode **"Limpar os produtos do carrinho"** removendo todos os produtos do carrinho de compras, ou apenas **"Remover produtos selecionados do carrinho"**, respectivamente.

Por meio do campo de busca, você pode efetuar uma pesquisa dos produtos existentes no carrinho da **"Consulta de Produtos"**. A pesquisa pode ser realizada digitando o Código, Descrição, Complemento ou Referência do item, onde o sistema irá verificar a existência do mesmo e posicionar o foco sobre ele, caso seja informado um produto que não exista no carrinho a pesquisa não procederá.

Quando a Consulta de Produtos for aberta pela Central - Compras | Vendas | Mov. Internas, ao **"Visualizar carrinho de compras"** teremos a exibição do botão **"Terminar a seleção"**.Ao clicar nesse botão, o sistema insere todos os produtos que estão no carrinho de compras ao pedido ou nota através do qual foi inicializada a consulta.

**Observação:** Através dos totalizadores localizados no alto do painel Produtos no carrinho, você poderá consultar a **"Qtde. Itens"**, **"Qtde. Total"**, o **"Desc. Total"** (caso o(s) produto(s) tenha(m) descontos aplicados) e o **"Valor Total"** dos produtos que estão no carrinho.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos)

**Aba Detalhes Adicionais de Preço**

Quando define-se pela utilização da grade **"Detalhes de Preço"**, essa aba permite a adição de informações nessa grade. Tais informações se referem à uma consulta SQL cujos campos resultantes serão apresentados como colunas na grade do painel **"Detalhes de Preço"**.

![Imagem 40: Quando define-se pela utilização da grade "Detalhes de Preço" , essa aba permite a adição de informações nessa grade.…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006311141)

Ao acessar novamente a tela de Consulta de Produtos e visualizar a grade Detalhes de Preço, você pode observar as informações adicionadas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Buscando os Produtos

No campo **"Busca"** você pode pesquisar os produtos que deseja visualizar. Além disso, clicando no link **Busca**, é possível definir os critérios de localização dos produtos que serão considerados pelo sistema. Ao acioná-lo, será aberto o pop-up **"Configurar a caixa de busca"**:

![Imagem 41: No campo "Busca" você pode pesquisar os produtos que deseja visualizar. Além disso, clicando no link Busca , é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/4404841667479)

Como já informado, você poderá definir quais campos do produto serão considerados na busca. Os campos selecionados serão considerados toda vez que uma pesquisa por determinado produto for efetuada. Por exemplo, pesquisando-se os produtos pelo código, o critério de busca **"Código"** deverá estar selecionado.Temos os seguintes critérios de pesquisa:

- Código;
- Descrição;
- Características;
- Complemento;
- Referência;
- Grupo;
- Localização;
- Referência do Fornecedor;
- Marca;
- Código de Barras;
- Prod. Equivalente.

**Nota:** Caso o critério **"Código"** esteja selecionado, a busca inicial será feita através deste, desde que o valor seja um número inteiro. Caso o valor buscado não seja inteiro ou não tenha sido encontrado na busca, o processo utilizará os outros critérios que foram selecionados, ou seja, caso um dos critérios de busca esteja marcado com a opção **"Código"**, o sistema realizará primeiro uma busca exata pelo código; se o mesmo não for encontrado, será realizada outra pesquisa, agora uma pesquisa dinâmica usando o próximo critério. Se o critério Código não for selecionado, a busca inicial não será realizada através deste.

Se as marcações **"Marca"** e **"Referência do Fornecedor"** estiverem selecionadas, o dado informado na busca irá trazer os produtos cuja Marca e/ou Referência do Fornecedor possuem o que foi informado.

O campo **"Tipo de Busca"** permite que você alterne o tipo da busca entre **"Contendo..."** e **"Começando com..."** de forma que a primeira opção faz com que a busca inclua resultados que contenham o texto digitado. Por exemplo, utilizando a primeira opção, a busca com o texto **"Azul"** retornaria resultados como:

- Pasta Azul;
- Caderno Azul;
- Azul Marinho.

Já a busca com a segunda opção denominada Começando com... mostrará apenas os resultados que comecem com o texto digitado, ou seja, ainda nesse exemplo, a busca do texto **"Azul"** só retornaria o resultado:

- Azul Marinho.

**Observação:** As opções Contendo... e Começando com... não são aplicáveis em buscas efetuadas em campos do tipo numérico, como por exemplo, o campo código.

**Nota:** A opção padrão marcada e usada pelo sistema é configurada no parâmetro **"Busca de Produto feita usando 'contendo (palavra buscada)' - CONSPRODCONTEN"** cujo valor padrão é verdadeiro.

No campo **"Considerar termos digitados"** você define qual será a regra a ser utilizada na consulta indexada por termos, podendo ser **"Todos os termos"** ou **"Qualquer termo"**. Ou seja, quando você digitar mais de uma palavra chave, poderá decidir se a pesquisa deve retornar apenas os produtos que possui a descrição com todas as palavras chaves ou aqueles produtos que contem apenas uma delas.

**Importante:** Para que esse campo seja apresentado, é necessário que o produto esteja com o serviço ativo no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela#botooutrasopes...), opção **"Consulta indexada por termos"**.

Observe abaixo o processo utilizando primeiramente o Tipo de Busca Contendo... Todos os termos e depois, Contendo... Qualquer termo:

[GIF animado: Imagem 42: Observe abaixo o processo utilizando primeiramente o Tipo de Busca Contendo... Todos os termos e depois, Contendo...…](https://ajuda.sankhya.com.br/hc/article_attachments/4404841898007)

Com a marcação **"Utiliza na Consulta de Produtos"** realizada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) (botão **“Outras Opções…”**, opção **"Consulta indexada por termos"**) teremos a caixa de busca exibida conforme imagem abaixo:

![Imagem 43: Com a marcação "Utiliza na Consulta de Produtos" realizada no Cadastro de Produtos (botão “Outras Opções…” , opção…](https://ajuda.sankhya.com.br/hc/article_attachments/9167950395799)

---

**(1)** **Parâmetros que influenciam na consulta indexada por termos:**

**Expressão para Ordenação na consulta Indexada - EXPORDINDEX:** quando este parâmetro estiver preenchido, ao acessar a caixa de busca, poderá ser selecionada a opção **"Termos digitados"** no campo **"Ordenação"**. Assim, ao realizar a busca com essa opção, o sistema realizará uma busca por todos os termos digitados e irá ordenar conforme a definição configurada no parâmetro.

Se o campo Ordenação estiver com uma opção diferente de Termos digitados e você alterar para a configuração para essa opção e o parâmetro: **EXPORDINDEX** estiver vazio, será apresentada a mensagem: **"Para usar a opção 'Termos digitados', será necessário informar uma expressão de ordenação no parâmetro EXPORDINDEX. Entre em contato com o administrador do sistema”** e assim, o sistema não permitirá utilizar essa opção.

Além disso, o parâmetro EXPORDINDEX  deve ser configurado da seguinte forma:

1. termo\_01, termo\_02, termo\_03, termo\_04, termo\_05, termo\_06, termo\_07, termo\_08, termo\_09, termo\_10, tgfpro.descrprod;
2. termo\_01, termo\_02, termo\_03;
3. tgfpro.descrprod;
4. termo\_01 desc, termo\_02 desc,.

Sendo permitido utilizar no máximo 10 termos e no mínimo 1, para que a funcionalidade do parâmetro seja ativada. Também é possível utilizar qualquer campo da tabela TGFPRO para a ordenação da consulta.

**Preposições desconsideradas na Consulta Indexada por Termos - PREINDEXATERM:** este parâmetro contém todas as preposições usadas atualmente. No entanto, caso queira é possível remover ou adicionar novas preposições no campo Texto, na tela Preferências. Ao fazer isso o número de resultados será ampliado, pois o sistema passa a considerar a preposição como sendo um termo de pesquisa.

---

Caso estejam sendo exibidos na tela painéis com outras informações, por exemplo, **"Detalhes de preço"**, **"Detalhes de estoque"**, entre outros, ao clicar sobre um produto na tela, serão exibidas informações sobre o produto selecionado nesses painéis.

**Observação:** O parâmetro **"Exibe variação de custo na consulta de preços e estoque - EXIBEVARCUSTO"** uma vez habilitado, fará com que o sistema apresente a coluna **"Variação de custo(%)"** no painel de Entradas Pendentes. Nesse campo é realizado o seguinte cálculo: (1 - o valor da última compra dividido pelo valor unitário do produto) vezes 100.

A grade de **"Detalhes de estoque"** apresentará o campo **"Status Lote"** caso o parâmetro **"Utiliza Status do Lote? - UTILSTATUSLOTE"** esteja ligado.

O campo **"Grupo de Estoque"** da grade de Detalhes de estoque corresponde às informações configuradas nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo), campo **"Empresa para agrupar o estoque"**.

Nos painéis **"Detalhes de preço"** e **"Detalhes de estoque"**,caso o produto tenha volumes alternativos cadastrados, serão exibidos botões para que o usuário possa visualizar as informações na unidade desejada.

**Nota:** Na grade **"Detalhes de estoque"**, caso você possua em sua licença o opcional **"WMS/W - 80084"**, será disponibilizada para uso a coluna **"Estoque disponível WMS"**, onde serão apresentados os dados do estoque disponível no WMS do produto selecionado. Além disso, são respeitadas para apresentação dos dados, as configurações realizadas através do botão **"Configurar consulta de produtos"**, na aba **"Detalhes de estoque"** verificando a marcação da opção **"Apresentar estoque por empresa"**; se marcada, mostra o estoque disponível WMS para cada empresa.

O valor padrão será sempre exibido com um asterisco **(\*)** precedendo o nome.

Alguns painéis disponíveis nessa rotina possuem colunas que apresentam as informações em forma de links. Ao clicar no link, você será redirecionado para a tela correspondente à informação. Por exemplo, ao clicar em um link da coluna empresa, o sistema abrirá o [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913), exibindo as informações da empresa selecionada.

Com a finalidade de possibilitar o refinamento das informações obtidas no painel de **"Entradas Pendentes"** dessa tela, o sistema oferece opção para definir filtros de seleção. Você poderá, por exemplo, em um processo de venda para determinado item, consultar o saldo de estoque disponível e filtrar as movimentações de entradas pendentes que atualizem o estoque para verificar se a empresa conseguirá atender à demanda de venda para seu cliente.

![Imagem 44: Com a finalidade de possibilitar o refinamento das informações obtidas no painel de "Entradas Pendentes" dessa tela, o…](https://ajuda.sankhya.com.br/hc/article_attachments/4404842107287)

Ao clicar em Entradas Pendentes, serão exibidas entradas pendentes referentes a pedidos de compra com status da nota liberada e notas de compra com status não confirmada.

É necessário definir um filtro para TOP que Atualiza Estoque. O Pedido para o item configurado com TOP de Pedido de Compra que Atualiza Estoque será apresentado.

Expressão do filtro (CabecalhoNota > TipoOperacao > ATUALEST = 'E')

Ou

Definir filtro para TOP que não Atualiza Estoque. O Pedido para o item configurado com TOP de Pedido de Compra que não Atualiza Estoque será apresentado.

Expressão do filtro (CabecalhoNota > TipoOperacao > ATUALEST = 'N')

Deve ser observado que o filtro definido será acrescentado ao filtro já realizado pela tela, que leva em consideração as movimentações com cabeçalho e itens pendentes, tipo de movimentação de pedido de compra (O-Pedido de compra) e nota de compra (C-COMPRA), Status da Nota (Liberada e Não Confirmada), ou seja, o sistema permite realizar um filtro dentro de Entradas Pendentes respeitando primeiro o filtro default e depois o filtro inserido na tela.

O campo **"Data Previsão Entrega"** encontra-se disponível no painel **"Entradas Pendentes"**, assim como no Painel Reservas e no Cabeçalho da Nota na Central de Notas, possibilitando que você visualize na Consulta de Produtos em Entradas Pendentes e em Reservas, a data prevista para entrega dos produtos que foi informada no lançamento do Pedido ou Nota de Compra.

No campo **"Quantidade de produtos"** da grade principal e da grade **"Detalhes de Estoque"**, pressionando **"Enter"** no teclado, o sistema adiciona a quantidade no carrinho de compras. Quando for utilizado o campo **"Quantidade"** da grade principal, será considerado o local do item que está selecionado na grade Detalhes de Estoque.

Você pode também, através dos atalhos **"Ctrl+M"** ou **"Ctrl+Z"**, posicionar o cursor no campo **"Critério de busca"**, sendo este o campo de pesquisa de produtos da grade principal.

Quando o cursor estiver posicionado em qualquer campo da tela, ao pressionar no teclado as teclas de atalho **"Ctrl+Q"**, teremos o posicionamento do cursor no campo de preenchimento da Quantidade na grade Detalhes de Estoque, de modo que será possível informar a quantidade antes da inclusão no carrinho de compras.

**Observação:** caso queira, é possível definir uma quantidade máxima de registros retornados na Consulta de Produtos, basta inserir a quantidade desejada no parâmetro **"Qtd. máx. de reg. na consulta de produtos - MAXREGCONSPROD"**. E para limitar a consulta ainda mais, pode-se também adicionar detalhes como cor, tamanho e/ou marca na descrição dos produtos para que haja uma filtragem mais efetiva. Após o preenchimento do parâmetro, efetuando a abertura da consulta de produtos, a mensagem abaixo será exibida ao lado do botão **"Configuração da Grade"**:

**"A quantidade de produtos encontrados foi limitada por um parâmetro do sistema. Existem mais registros"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Botão Outros Filtros

Esse botão está localizado na parte superior da tela; nele você pode filtrar os produtos que encontram-se em promoção e/ou liquidação, a depender da marcação realizada.

Sendo que, para utilizar estas opções de filtro, é necessário que o campo **"Busca"** esteja vazio, pois caso ele esteja preenchido com o código ou a descrição do produto, o sistema irá carregar os registros de acordo com a busca definida neste campo, deixando de priorizar as marcações do botão Outros Filtros.

Ressaltamos ainda que, ao acionar a marcação **"Filtrar promoção"** o sistema irá considerar apenas os Produtos cadastrados com [Desconto Promocional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034), ou seja, a marcação **"Promoção"** localizada na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda), da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), não influência neste filtro.

![Imagem 45: Ressaltamos ainda que, ao acionar a marcação "Filtrar promoção" o sistema irá considerar apenas os Produtos cadastrados…](https://ajuda.sankhya.com.br/hc/article_attachments/4404842351639)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Botão Salvar em PDF

Quando você clicar no botão ![Imagem 46: Quando você clicar no botão Salvar em PDF , terá as opções " Salvar em PDF" , "Imprimir" e "Salvar modelo" .](https://ajuda.sankhya.com.br/hc/article_attachments/16105918251799)  Salvar em PDF, terá as opções "**Salvar em PDF"**, **"Imprimir"** e **"Salvar modelo"**.

Assim:

- Na opção Salvar em PDF, o sistema irá salvar ou imprimir a lâmina de um produto onde constam informações para a venda, tais como: características do produto, peso, medidas, entre outros;
- A opção Imprimir trará as impressoras disponíveis para que a impressão seja realizada;
- Já a opção Salvar modelo irá salvar um documento em **jrxml.** com as informações do produto no seu computador. Considere ainda que, essa opção ficará disponível apenas para o usuário SUP.

Além disso, você poderá imprimir ou salvar o documento conforme um modelo personalizado que deve ser criado através da tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados). Para isso, basta criar o modelo conforme as suas preferências na tela Relatórios Formatados e informar o código dele no campo **"Inteiro"** do parâmetro **"Lamina de produtos na consulta de produtos - LAMICONSPROD"**. Se este estiver vazio, o documento será salvo/impresso usando o modelo padrão do sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Carrinho de Compras

Com a finalidade de simular as compras, você pode utilizar o carrinho de compras adicionando ou retirando produtos do mesmo. Para que o carrinho de compras seja exibido na tela é necessário efetuar a marcação **"Usa carrinho de compras?"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abageral) do botão [Configurar consulta de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdaconsultadeprodutos).

Para adicionar um produto ao carrinho de compras, clique sobre o produto e arraste-o para dentro do painel do carrinho de compras. Assim, será possível incluir apenas uma unidade do produto ao carrinho.

![Imagem 47: Para adicionar um produto ao carrinho de compras, clique sobre o produto e arraste-o para dentro do painel do carrinho…](https://ajuda.sankhya.com.br/hc/article_attachments/4404850523287)

No campo ao lado esquerdo do botão destacado acima, informe a quantidade do produto que você deseja acrescentar ao carrinho e adicione o produto selecionado, respectivamente. É necessário selecionar o produto na grade, informar a quantidade desejada no campo citado e, em seguida, clicar no Carrinho.

**Observação:** com o parâmetro **"Alterar quant. produto para um após adicionar ao carrinho?-ALTQTDPRODUM"** ligado, ao adicionar um item no carrinho, o campo **"Quantidade de Produtos"** retornará para a quantidade 1 ou manterá a quantidade digitada anteriormente. Lembrando que, esse parâmetro não influencia na **"Quantidade"** do produto inserido no carrinho de compras.

[GIF animado: Imagem 48: Observação: com o parâmetro "Alterar quant. produto para um após adicionar ao carrinho?-ALTQTDPRODUM" ligado, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/26484431231383)

Se o produto adicionado ao carrinho possuir o controle adicional por grade, ao clicar no botão ![Imagem 49: Se o produto adicionado ao carrinho possuir o controle adicional por grade, ao clicar no botão Adicionar produto com o…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903408023) Adicionar produto com o estoque selecionado ao carrinho o sistema exibirá o pop-up  **"Grade"**, onde você poderá selecionar a variação do produto adicionado, sendo que ele será configurado na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba **"Medidas e Estoque"**, sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional).

[GIF animado: Imagem 50: Se o produto adicionado ao carrinho possuir o controle adicional por grade, ao clicar no botão Adicionar produto com o…](https://ajuda.sankhya.com.br/hc/article_attachments/4404842514967)

Na lateral direita do painel, o sistema exibe as informações sobre a quantidade de produtos que foram adicionados ao carrinho e o valor total dos produtos.

Para possibilitar a inicialização rápida do carrinho de compras de um pedido, existem as opções **"Última negociação"** e **"Histórico de consumo"** pois, algumas pessoas possuem um padrão de consumo, ou seja, sempre compram os mesmos produtos.

![Imagem 51: Para possibilitar a inicialização rápida do carrinho de compras de um pedido, existem as opções "Última negociação" e…](https://ajuda.sankhya.com.br/hc/article_attachments/4404850559767)

Através da opção **"Última negociação"**, o  sistema irá encontrar a última negociação do parceiro e irá adicionar os itens da negociação ao carrinho de compras. Os preços unitários serão reinicializados para o valor de tabela atual. É possível configurar um **"Filtro para buscar a última negociação"**, trataremos disso mais abaixo.

Pela opção **"Histórico de consumo"** teremos a busca das negociações do parceiro nos últimos X dias, podendo considerar um **"Filtro para buscar histórico de consumo"**, em que X e o filtro são definidos por você na configuração do carrinho que será tratada mais abaixo. Os produtos são agrupados através do Código do produto + Controle.

Ainda sobre o Histórico de consumo, habilitando o parâmetro **"Permite triagem de histórico de consumo? - PERTRIAGEMHISTC"**, será exibido o painel **"Histórico de consumo"**. Nesse painel você pode executar, previamente, uma apuração os itens que serão incluídos no carrinho de compras de determinado parceiro. Abaixo trouxemos a descrição de algumas funcionalidades:

- Define-se primeira e obrigatoriamente o **"Parceiro"**, o **"Período"** desejado e a situação dos **"Produtos"** a serem verificados; em relação aos produtos, pode-se definir dentre:
- **Próxima compra vencida:** Serão exibidos todos os registros cuja data da próxima compra esteja vencida;
- **Próxima compra a vencer:** Serão apresentados todos os registros em que a data da próxima compra não esteja vencida;
- **Todos:** Tem-se todos os registros que se enquadrem nos filtros apresentados na grade.
- O botão **"Enviar para carrinho"** confirma o envio dos itens que estão com a coluna **"Quantidade"** diferente de 0 (zero) para o carrinho de compra;
- Para cancelar a seleção utilize o botão **"Voltar"**;
- Acionando o botão **"Usar Qtd. Últ. Compra"**, os itens contidos na grade serão enviados para o carrinho de compras com sua quantidade conforme a quantidade da última compra efetuada. Você poderá verificar estes dados através das colunas **"Quantidade"** e **"Qtd. Últ. Compra"**;
- O campo **"Interv. Compra"** trará a diferença entre o campo **"Dt. Últ. Compra"** e **"Dt. Próx. Compra"**.
- As linhas em vermelho indicam que a data da próxima compra é menor que a data atual. Ou seja, um produto que tem média de x dias somados a última compra está com a data atrasada. Abaixo temos um exemplo:

19/04/2017 + 50 dias = 08/06/2017. A provável compra do produto era 08/06 e até a data atual (30/06/2017) não se realizou a compra;

As linhas em preto apontam que a data da próxima compra é maior que a data atual. Sendo assim, um produto que tem média de x dias somados a última compra não está em atraso. Exemplo:

22/05/2017 + 41 dias = 02/07/2017. A provável compra do produto era 02/07 e até a data atual (30/06/2017) não se efetuou a compra.

Efetuando a marcação **"Usar carrinho de compras"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abageral), além da realização das configurações descritas acima, será habilitada a aba [Configuração do Carrinho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaconfiguraodocarrinho).

Ao abrir a Consulta de Produtos por meio das centrais, você pode acessar a Ficha de Parceiros como uma forma de consulta, sendo que, é possível também abri-la por meio do atalho **"Ctrl + Alt + F"** no teclado, ou pelo botão ![Imagem 52: Ao abrir a Consulta de Produtos por meio das centrais, você pode acessar a Ficha de Parceiros como uma forma de…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903412503) **"Parceiros"**; para voltar para a grade de Produt![Imagem 53: Ao abrir a Consulta de Produtos por meio das centrais, você pode acessar a Ficha de Parceiros como uma forma de…](https://ajuda.sankhya.com.br/hc/article_attachments/16105903413271)os da Central, basta utilizar o atalho **"Ctrl + Shift + Backspace"** ou o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15585163872023):

[GIF animado: Imagem 55: Ao abrir a Consulta de Produtos por meio das centrais, você pode acessar a Ficha de Parceiros como uma forma de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006312741)

**Observação:** no layout Flex, não é possível adicionar um produto ao carrinho e, em seguida, alterar a quantidade do produto. Além disso, o sistema não consegue recalcular o valor caso haja um desconto aplicado no momento da adição do item ao carrinho.

---

#### Controle de Acesso à Ficha de Parceiros

O acesso à rotina **Ficha de Parceiros** depende das permissões configuradas na **tela de** [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos). O comportamento varia de acordo com a configuração do usuário:

- **Usuário listado na tela de Acessos, mas sem permissões**: não conseguirá acessar a **Ficha de Parceiros**, nem mesmo por meio do botão **Parceiros** disponível na **Consulta de Produtos via Centrais**.
- **Usuário não listado na tela de Acessos**: não poderá abrir a **Ficha de Parceiros** diretamente, mas ainda poderá acessá-la por meio do botão **Parceiros** na **Consulta de Produtos via Centrais**.

Isso ocorre porque, quando um usuário está explicitamente configurado na **Tela de Acessos**, o sistema exige permissões específicas para liberar a entrada. Caso contrário, ele impede a pesquisa e o acesso direto, mas ainda permite a navegação a partir de outras telas.

---

![Imagem 56: O parâmetro "Procedure para definição da unidade - NOMPROCDEFUNID" permite utilizar uma procedure para definir a…](https://ajuda.sankhya.com.br/hc/article_attachments/23027952819351) O parâmetro **"Procedure para definição da unidade - NOMPROCDEFUNID"** permite utilizar uma procedure para definir a unidade padrão do produto no processo de venda. Esta procedure deve seguir um padrão específico de assinatura, aceitando um único parâmetro de entrada (`p_IdSessao`) e um parâmetro de saída (`p_Result`) do tipo `VARCHAR2`.

> **Regras de execução da procedure:**
>
> - **Consulta de Produtos:** a procedure só entra em ação quando a inclusão do produto vem sem unidade, ou seja, a partir da **grade principal** da consulta. Caso o produto seja incluído via painel **Detalhes de Estoque**, a unidade já estará definida e a procedure não será aplicada.
> - **Inclusão Direta:** quando o produto é incluído diretamente na Central, a procedure só será utilizada se o campo **Unidade** estiver em branco.
> - **Limitação:** esta funcionalidade não está disponível na **Venda Assistida**.

Vale ressaltar que essa preferência não é aplicada durante a atualização dos itens ao incluir produtos no carrinho de compras.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Painel Buscar preço por

O parâmetro **"Tabela de preço por - TIPTABPRECO"** tem várias opções de valores; ao habilitar os valores **"Única"** ou **"Local"**, a Consulta de Produtos permanece inalterada. Sendo que, ao escolher qualquer um dos outros valores para o parâmetro, a tela apresentará um painel lateral direito chamado **"Buscar preço por"**, que atua como filtro nas buscas de preços.

![Imagem 57: O parâmetro "Tabela de preço por - TIPTABPRECO" tem várias opções de valores; ao habilitar os valores "Única" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/4404850652183)

Cada um dos valores escolhidos para o parâmetro TIPTABPRECO influenciam em quais campos de filtro o painel **"Buscar preço por"** irá disponibilizar para preenchimento. Por exemplo, ao se escolher o valor Tipo de Negociação/Vendedor o painel disponibiliza os campos Tipo de Negociação e Vendedor porém, só será possível que se preencha um desses campos; se um dos campos já estiver preenchido, ao preencher algum outro, o campo anteriormente informado fica limpo.

Através da ativação do parâmetro **"Restringir acesso a vendedores por região? - RESTACESSVENDRG"**, será permitido que os vendedores busquem os preços de tabela correspondentes apenas a outros vendedores que pertençam à sua região. Ou seja, trabalhando com Tabelas de Preço por Região do Vendedor (parâmetro de chave TIPTABPRECOS), ao efetuar a procura por um Vendedor no painel **"Buscar preço por"**, independente da Consulta de Produtos ter sido aberta pela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ou diretamente pelo menu, apenas vendedores pertencentes à mesma região que o vendedor vinculado ao usuário logado serão exibidos no campo de pesquisa. Não será possível realizar a consulta de produtos sem que um vendedor seja informado.

Caso você não possua vínculo com nenhum vendedor ([Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), campo **"Vendedor"**), ou o vendedor associado à você não possua a informação pertinente à região ([Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133#abageral), campo **"Região"**), essa restrição de acesso não irá acontecer.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Painel Classificadores

Este painel exibe os produtos de acordo com a classificação indicada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Classificação por Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaclassificaoporproduto). Essa classificação deve ser previamente cadastrada na tela [Classificadores de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598434).

Ao clicar sobre um dos itens do painel **"Classificadores"**, serão exibidos na grade da **"Consulta de Produtos"** todos os produtos daquela classificação.

Ao realizar uma pesquisa pelo campo **"Busca"**, o sistema considerará a classificação como um critério, ou seja, a busca vai trazer produtos que estejam dentro da classificação selecionada.

#### Busca através do Código de Barras

Essa tela disponibiliza uma opção de busca avançada para Código de Barras. Esta opção permite a busca na tabela TGFBAR pelo código de barras cadastrado para o produto.

Para o funcionamento da mesma, é necessário que o produto esteja cadastrado com seu respectivo código de barras, ter a busca de produtos configurada para ser realizada por código de barras. Posicionar o cursor de digitação no campo **"Busca"** e bipar o leitor sobre o código de barras do produto. Para ler outro código relacionado a outro produto, é necessário limpar o campo de leitura Busca.

Bipar o leitor novamente sobre os outros códigos que o produto possui.

Sendo assim, quando a consulta do produto for realizada, serão verificadas também as informações de estoque do produto para as variáveis do mesmo. Não sendo necessário utilizar outros critérios de busca ou ter que bipar especificamente o produto que possui o código de barras cadastrado no campo referência. Otimizando o tempo de consulta, que é muito importante para vendas ágeis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Painel Produção programada

```
                A partir da versão 4.17 este painel será renomeado para "Status da Produção".
```

Neste painel, você poderá acompanhar o status da produção das OPs abertas que estão em andamento ou que serão iniciadas para um determinado produto.

Aqui, constam as principais informações: Nº OP, Status Produção, Cód. Produto, Descrição, Quantidade, Saldo à Produzir, Produção p/Pedido e Nro. Nota.

**Nota:** As Ordens de Produção abertas para o produto com status **"Cancelada"** ou **"Finalizada"** não serão apresentadas neste painel.

![Imagem 58: Nota: As Ordens de Produção abertas para o produto com status "Cancelada" ou "Finalizada" não serão apresentadas neste…](https://ajuda.sankhya.com.br/hc/article_attachments/11004264112535)

Você pode configurar o modo de visualização deste painel na Consulta de Produtos, na aba **"Outras Informações"** escolhendo entre **"Link"**, **"Painel"** ou **"Não exibir"**.

**Nota:** O modo de visualização Link não está sendo apresentado em HTML.

Entre as colunas disponibilizadas no painel, os campos local e controle serão exibidos em branco caso o produto não esteja configurado para utilizá-los. Quando o produto possuir controle, a descrição dessa coluna será alterada para exibir o tipo de controle.

A data programada exibida no painel, é calculada pela **"Data do planejamento + duração do ciclo de produção do produto"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Como Simular um Desconto

Para simular nessa rotina um desconto para o preço do produto, é necessário habilitar o parâmetro **"Simular desconto na consulta de produto - SIMDESCCONPROD"** que permite visualizar o painel para informar o desconto extra.

Além disso, caso o parâmetro **"Aplicar desconto simulado no carrinho aos itens?-SIMDESCCPITENS"** esteja ligado, o desconto simulado será aplicado nos itens do Carrinho de Compras e na Central de Vendas.

[GIF animado: Imagem 59: Além disso, caso o parâmetro "Aplicar desconto simulado no carrinho aos itens?-SIMDESCCPITENS" esteja ligado, o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006315281)

Você poderá informar um percentual de desconto entre 0 e 100. Este percentual de desconto será aplicado em todos os produtos da grade e também no painel de Detalhes de Preço.

Pode existir nas Configurações do painel de resultados, tabelas de preços com um multiplicador diferente de 1 então, o percentual para simular o desconto será aplicado depois que for aplicado o multiplicador.

O desconto extra é apenas uma simulação, por isso, quando é feita a consulta de produtos através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) o sistema irá preencher no item da nota o valor integral do produto ou serviço.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Desconto Promocional por Quantidade

Os produtos que possuem faixas de desconto conforme sua quantidade vendida, poderão ser apresentados na grade com suas linhas coloridas da mesma forma que ocorre com os produtos com desconto promocional padrão. Para tanto é necessário realizar algumas configurações:

- Na tela de [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034) será criado o desconto por quantidade;
- O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) que será utilizado deve possuir em sua aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), o campo **"Desconto Promocional"** configurado com a opção **"Considerar por Qtde Somando"** ou a opção **"Considerar por Qtde/Desconto"**;
- Através da tela [Atualização de Preço de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612094) efetue a criação do preço do preço desse produto, bem como, sua vinculação à este preço;
- Na Consulta de Produtos, aba [Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abapreos), a marcação **"Mostrar promoção na grade principal"** deve estar acionada para que a promoção seja exibida.

Sendo assim, no lançamento de um pedido/nota, ao acessar a Consulta de Produtos teremos a exibição do produto em destaque na grade.

**Nota:** Essa funcionalidade só é válida quando se acessa a Consulta de Produtos através das Centrais.

Além disso, ao selecionar um produto que possua desconto promocional por unidade alternativa, nos Painéis **"Detalhes de Preço"**/ **"Detalhes de Estoque"** serão exibidos as unidades para que você possa escolher o item com **"Volume"** alternativo que apresente a promoção e assim, seja aplicado o desconto deste na venda, sendo que, a unidade que possuir a promoção será destacada  com uma tarja **amarela**.

**Nota:** Caso o produto que foi selecionado na venda tenha uma unidade alternativa e ela possua uma promoção configurada, o campo **"Multiplicador de valor"** (tela Cadastro de Produtos, aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas)) ficará nulo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Utilização da Mesma Tabela de Preço para Todos os Produtos

Ao efetuar a busca de qualquer produto e clicar no mesmo para adicionar ao carrinho, será exibida uma grade com informações dos preços cadastrados para o produto.

Quando a marcação **"Usar este tipo de preço nos próximos itens"** for habilitada, no momento de selecionar o preço o sistema utilizará aquele mesmo tipo de preço para os demais produtos.

**Observação:** Caso exista somente um tipo de preço cadastrado, a grade não será apresentada e o produto será adicionado automaticamente ao carrinho de acordo com esse tipo de preço.

**Nota:** Todas as vezes que você acessar a Consulta de Produtos através da **"Central - Compras | Vendas | Mov. Internas"**, caso você retorne na central e, em seguida acesse novamente a Consulta de Produtos, a grade com informações dos preços será apresentada. Ou seja, a rotina será mantida apenas naquele momento que ele está na tela.

**Observação:** Quando houver a entrada de uma nota em que a tabela de preço por empresa é utilizada e, algum produto esteja sem preço na Consulta ou inclusão de Produtos cadastrados, o sistema buscará os preços a partir da função SNK\_GET\_PRECO. Assim, ele terá o seguinte comportamento:

- O preço será procurado na maior tabela existente e caso o produto não exista, o preço a ser apresentado será 0;
- O sistema irá procurar o preço somente na última tabela existente, caso este não for encontrado na tabela em questão, os preços serão buscados nas tabelas seguintes e assim sucessivamente.

Uma vez que os comportamentos acima são alterados, o objeto padrão exibido abaixo deve ser inserido na tabela TSISNK, pois ela controla os objetos para que não sofram atualizações:

**/\*    SELECT NVL (MAX (M.NUTAB), -999999)**
**INTO TROCA**
**FROM TGFTAB M, TGFEXC E**
**WHERE M.DTVIGOR <= P\_DTVIGORAUX**
**AND M.CODTAB = P\_CODTAB**
**AND E.CODPROD = P\_CODPROD**
**AND E.CODLOCAL = P\_CODLOCAL**
**AND E.CONTROLE = P\_CONTROLEAUX**
**AND E.NUTAB = M.NUTAB;**

**IF TROCA = -999999 THEN \*/**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Usar a  precificação de produtos/serviços pela TOP

O sistema possibilita usar a precificação de produtos/serviços definida pela TOP. Para isso existe o parâmetro **"Usa precificação de produtos/serviços pela TOP -USAPRECPELATOP"** que, quando ligado, habilita a aba [Tabela por Empresa/Projeto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abatabelaporempresaprojeto) no [Cadastro de Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) e, nessa mesma rotina, a busca de tabela de preço na inicialização do produto no Portal de Vendas, bem como na consulta de produto.

Devido à esta configuração, quando o parâmetro USAPRECPELATOP está ligado, independente da tabela selecionada na Consulta de Produtos/Carrinho, a tabela a ser considerada é a tabela associada à TOP (se houver), pois a aplicação realizará uma busca para encontrar a tabela associada à TOP e, caso não encontre nenhuma, o sistema irá considerar a tabela selecionada na Consulta de Produtos/Carrinho.

E quando o parâmetro USAPRECPELATOP está desligado, o preço retornado para a Central será o da tabela selecionada na Consulta de Produtos/Carrinho.

**Observação:** Quando o parâmetro **"Usa precificação pela TOP no PDV Web - USAPRECTOPPDV"** estiver ligado, a configuração de precificação definida na TOP será considerada no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web), mesmo que o parâmetro **"Usa precificação de produtos/serviços pela TOP - USAPRECPELATOP"** esteja desligado.

**Importante:** Ao acessar a Consulta de Produtos através do menu e não através da Central, o sistema levará em consideração o parâmetro **"Tabela de Preços por - TIPTABPRECO"**.

**Observação:** Na [Configuração do Painel de Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#configuraesdopainelderesultado), em sua aba [Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abapreos), não pode haver uma **"Tabela específica"** informada.

**Nota:** Os preços apresentados na Consulta de Produtos podem ser calculados com base na configuração de [Preço Dinâmico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110953). Além de que, caso queira que uma ou mais empresas não sejam considerados no cálculo de preço dinâmico, basta informá-las no campo **"Texto"** do parâmetro **"Lista de empresas sem cálculo de preço dinâmico. - LISEMPSEMPREDIN"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Consulta de Produtos por Série

É possível consultar a quantidade de produtos em estoque por cada série cadastrada e movimentações efetuadas por produtos que possuem controle adicional por estoque por Série.

Essa opção é apresentada somente se no [Cadastro do Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), a marcação **"Inibe Consultar Série de Produtos"** estiver habilitada para o usuário logado.

Além disso, para visualizar a aba **"Série"**, é necessário ir na aba **"Outras Informações"** e marcar se a aba Série deve aparecer como **"Link"**, **"Painel"** ou **"Não exibir"**.

Se o parâmetro **"Usa Número de Série Global? - USACBGLOBAL"** estiver habilitado, serão apresentados a coluna **"Avariado"** e o botão **"Ver detalhes da avaria"**. Caso a série relacionada esteja avariada, será apresentada a linha em vermelho e o referido botão ficará habilitado.

![Imagem 60: Se o parâmetro "Usa Número de Série Global? - USACBGLOBAL" estiver habilitado, serão apresentados a coluna "Avariado" e…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006315601)

Ao acioná-lo, será apresentada uma tela com os detalhes da série avariada como o número de cadastro, o % de desconto que será aplicado sobre a venda, um campo para observações e imagens do produto.

Se clicar no botão **"Enviar série p/ pedido/nota"** será enviado o produto, a série específica, o percentual de desconto e o local caso o produto utilize local.

As avarias são previamente cadastradas na tela de [Registro de Avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333).

Acesse a documentação [Controle de Produtos com Número de Série Global](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597254) para obter mais informações.

Na grade inferior, são apresentadas todas as movimentações efetuadas das séries existentes do Produto selecionado.

Informe a **"Dt. Inicial"** da negociação para aplicar o filtro e o sistema apresentar as movimentações a partir desta.

#### Botão de Filtros

Uma vez informados os filtros desejados, o sistema apresentará as informações de acordo com os referidos filtros.

![Imagem 61: Uma vez informados os filtros desejados, o sistema apresentará as informações de acordo com os referidos filtros.](https://ajuda.sankhya.com.br/hc/article_attachments/1500006195982)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Desconto Promocional por Controle de Grade

Agora, na Consulta de Produtos, podemos identificar e aplicar o desconto promocional configurado para os itens do produto controlado por grade, lista ou lote.

Quando você selecionar um produto controlado por grade, lista ou lote e ele possuir desconto promocional, o sistema irá apresentar esse produto com a linha em cor destaque (conforme foi configurado na Consulta de Produtos), bem como o item (ou itens) nos painéis Detalhes de Estoque e Carrinho de Compras (conforme configuração realizada na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais)):

**Observação:** Independente do parâmetro **"Controle Preços por Controle ? - PRECOPORCONT"** estar ligado ou não, quando for selecionado um produto controlado por grade, lista ou lote e ele possuir desconto promocional configurado, o sistema apresentará no painel Detalhes de Preço o campo **"Controle"** e, ao selecionar a opção do controle, serão exibidas as informações já existentes no painel, de acordo com o desconto promocional cadastrado na tela Descontos Promocionais.

**Nota:** Após terminar a seleção dos itens, será aplicado o valor ou percentual de desconto para todos os itens selecionados, de acordo com a configuração feita previamente na tela Descontos Promocionais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Parâmetros que influenciam nos Detalhes do Preço

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), é possível definir o Tipo e o Título do controle. Feito esse cadastro, após ativar o parâmetro **"Controla Preços por Controle? - PRECOPORCONT"**, na tela de [Tabela de preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854) será exibido um campo com título e tipo indicado na tela de produtos. Com isso, poderão ser cadastrados diferentes valores para o mesmo produto.

Na Consulta de produtos, se o parâmetro de chave PRECOPORCONT estiver habilitado, será mostrado um campo com o título indicado na tela de produtos no painel **"Detalhes de Preço"** para que seja possível ver o preço para um determinado controle.

Se o parâmetro **"Preço por Local - PRECOPORLOC"** estiver habilitado, na tela de Tabelas de preços, aba **"Exceções"**, ao adicionar um registro aparecerá o campo Local para se preencher. Com isso, você poderá cadastrar diferentes Locais para o mesmo produto e, se combinado com o parâmetro de chave PRECOPORCONT, será possível cadastrar diferentes valores para diferentes Locais e diferentes Controles do mesmo produto.

Em seguida, na Consulta de produtos se o parâmetro **"Tabela de Preços por - TIPTABPRECO"** estiver como Local, será mostrado um campo de nomenclatura **"Locais"** no painel **"Detalhes de Preço"** para que seja possível ver o preço para um determinado Local, se estiver combinado com o Controle, ao selecionar o Local o sistema apresenta no campo dos controles apenas aqueles que tem cadastro nas tabelas de preços.

O parâmetro **'Mostrar impostos na Consulta de Produtos? - MOSTIMPCONSPROD'** é apresentado desativado por padrão. Quando ativado, ele habilita a exibição das colunas **'Vlr. IPI'**, **'Vlr. ICMS-ST'** e **'Vlr. c/ impostos'** em diversas grades da consulta.

Impacto importante**:** O funcionamento deste parâmetro é restrito exclusivamente às situações em que a **Consulta de Produtos é aberta através da Central de Vendas**. Ele influencia a visualização na grade de resultados, nos Detalhes de Preço, nos Detalhes de Venda e no Carrinho de Compras, onde também habilita totalizadores de impostos no canto superior direito.

- Grade de Desconto Promocional por quantidade, a qual é visualizada na seleção de uma linha na grade de Detalhes de Preço, é apresentada a coluna Preço c/ impostos;
- Detalhes de Venda, tem-se a coluna Preço c/ impostos;
- Grade de resultados da Consulta de Produtos, tem-se a coluna Preço c/ impostos para cada preço contextualizado;
- Grade do carrinho de compras, tem-se os campos Vlr. IPI, Vlr. Tot. IPI, Vlr. ICMS-ST, Vlr. Tot. ICMS-ST, Vlr. c/ impostos e Vlr. Tot. c/ impostos. Por fim, é apresentado um Totalizador com impostos no canto superior direito desta grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)

## Campos Adicionais

Com a possibilidade de descrição de expressões SQL em campos adicionais, de modo que eles sejam utilizados na Consulta de Produtos, podemos relatar um exemplo de como não se deve formular a expressão (dessa forma ao realizar uma consulta de produtos, será gerado um erro na tela):

```
String txt = "";

$sql.setParam("CODPROD", $col_CODPROD);

$sql.select(" CASE WHEN TIPSUBST = 'N' THEN 'TRIB' ELSE 'SBT' END", "TGFPRO",
" CODPROD = {CODPROD} ");

if($sql.next()) {

txt = $sql.getString(1);

}

return txt;

Para que não sejam apresentados erros, a expressão deve ser substituída pela seguinte:

#type.sql#

CASE WHEN TGFPRO.TIPSUBST = 'N' THEN 'TRIB' ELSE 'SBT' END
```

**Atenção Consultor Sankhya:** durante a criação de Campos Adicionais, o sistema assume que cada produto possui um único valor para cada campo adicional (relação 1:1). Portanto, se forem criados Campos Adicionais onde um produto pode ter múltiplos valores para um campo, isso resultará em erros, exibindo a seguinte mensagem de aviso na tela:

**"A subconsulta retornou mais de 1 valor. Isso não é permitido quando a subconsulta segue um =, !=, <, <=, >, >= ou quando ela é usada como uma expressão."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#top)
