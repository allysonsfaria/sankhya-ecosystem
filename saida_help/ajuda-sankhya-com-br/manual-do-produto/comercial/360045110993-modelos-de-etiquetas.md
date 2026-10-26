---
id: "360045110993"
titulo: "Modelos de Etiquetas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:30:43Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios", "Portais", "Parceiro", "Volume", "Modelos de Etiquetas", "br.com.sankhya.mgecom.relatorios.modelosetiquetas", "Modelos de Etiquetas manual", "Parceiros", "SPS", "Botão Outras Opções", "Comercial"]
---

# Modelos de Etiquetas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312058273943) Módulo: Comercial > Relatórios
```

---

A impressão de etiquetas no sistema, se baseia nos templates (modelos de documento) obtidos por meio da tela Modelos de Etiquetas. Assim, neste artigo trataremos das configurações necessárias para cadastrar um modelo de etiqueta, bem como, das telas que realizam a impressão de etiquetas:

[Trabalhando na tela Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#trabalhandonatelamodelosdeetiquetas)       

[Impressão das Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#impressodasetiquetas)                       

[Impressão de Etiquetas através da tela de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#impressodeetiquetasatravsdateladeparceiros)            

[Impressão de Etiquetas através do Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#impressodeetiquetasatravsdocadastrodeprodutos)    

[Impressão de Etiquetas Vol. Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#impressodeetiquetasvol.conferncia)

## Trabalhando na tela Modelos de Etiquetas

![Imagem 2: Trabalhando na tela Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/article_attachments/4403852843671)

Temos no lado esquerdo da tela, os filtros **"Código"**, **"Nome contendo"**, **"Nome do arquivo contendo"**, para realizar a busca dos Modelos de Etiquetas já cadastrados.

No Painel Principal ao iniciar o cadastro de um modelo de etiqueta, o campo **"Código"** será alimentado automaticamente.

A **"Descrição"** do modelo é uma informação obrigatória e deve ser preenchida de modo a melhor identificar o cadastro em suas posteriores utilizações.

O campo **"Categoria"** pode ser utilizado como uma forma de agrupamento dos modelos; é uma informação que não necessita de cadastro prévio e pode ser inserida aleatoriamente de acordo com cada processo.

Automaticamente, o sistema grava a **"Última alteração"** feita no modelo de etiqueta selecionado e o respectivo **"Usuário"** que a realizou.

O campo **"Id da tela"** pode ser utilizado para relacionar o atual modelo de etiqueta com sua respectiva tela, onde será aplicado para impressão.

Caso seja necessário, realize o vinculo de outro modelo de Relatório Formatado ao modelo de etiqueta em questão, por meio do campo **"Relatório dependente"**.

Através do campo **"Fonte de Dados"**, defina qual o banco de dados que será acessado para execução dos modelos de etiqueta.

No campo **"Nome do anexo no envio de e-mail"** informe o texto que irá substituir o prefixo "Nota\_fiscal\_" no envio de notas por meio da tela [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-), por exemplo:

Na tela Impressão de Boleto(s), quando a opção **"Anexar Nota Fiscal"** estiver habilitada, será realizado o envio deste documento por e-mail com o nome "Nota\_fiscal\_2781.pdf", onde "2781" se refere ao número da nota; caso o campo Nome do anexo no envio de e-mail esteja informado, este texto substituirá o prefixo "Nota\_fiscal\_".

Informe o nome **"Impressora"**, sendo que, para utilização da impressora definida como padrão é necessário preencher neste campo a descrição **"padrão"** ou **"PADRAO"**; quando o sistema identifica que o nome da impressora está com a referida descrição, será enviada a impressão para a impressora definida como padrão.

---

**Aba Arquivos**

Nesta aba deverão ser adicionados os modelos de etiquetas. Através dos botões da barra de ferramentas da grade, pode-se adicionar, remover e realizar o download dos arquivos adicionados. Depois que um modelo é adicionado, este será apresentado na grade.

**Nota:** Será permitida a adição apenas de arquivos no formato **".jrxml"** e **"zpl"**.

---

**Botão Layouts**

No alto desta tela, temos a opção de baixar um dos templates disponibilizados através do botão **"Layouts"**, e utilizá-los nas telas que oferecem esta impressão, tais como [Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), [Portais de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e [Movimentação Interna](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas) e [Impressão de Etiquetas por Volume](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601094-Impress%C3%A3o-de-Etiquetas-Vol-Confer%C3%AAncia). Caso seja constatado que um dos modelos disponíveis não atende às necessidades da empresa, o Consultor Sankhya deverá baixar o modelo desejado, formatá-lo através do iReport e incluí-lo nesta mesma tela.

O botão Layouts, apresenta as seguintes opções de layout para baixa:

- **Parceiro** - Impressão acessada através do Cadastro de Parceiros > botão Outras Opções > Impressão de Etiquetas;
- **Produto** - Impressão acessada através do Cadastro de Produtos >  aba Estoque > botão Outras Opções > Imprimir Etiquetas;
- **Parceiro (Portais)** - Impressão acessada nos Portais (Compras, Vendas e Mov. Internas) > botão Outras Opções > Imprimir etiquetas > Etiquetas por Parceiro;
- **Produto (Portais)** - Impressão acessada nos Portais (Compras, Vendas e Mov. Internas) > botão Outras Opções > Imprimir etiquetas > Etiquetas por Produto;
- **Volume (Conferência)** - Impressão acessada através da tela Impressão de Etiquetas Vol. Conferência.

---

**Botão Outras Opções**

O botão Outras Opções apresenta as seguintes funcionalidades:

![Imagem 3: O botão Outras Opções apresenta as seguintes funcionalidades:](https://ajuda.sankhya.com.br/hc/article_attachments/4403852872599)

Ao acionar a opção **"**Adicionar lançador", será aberta uma tela, onde deve-se informar a descrição e a pasta de destino. A **"Descrição"** é a identificação literal para o lançador; a **"Pasta de destino"**, refere-se ao diretório do menu que abrigará o lançador de um determinado item. A operação estará concluída após a confirmação, pressionando o botão **"Concluir"**, e poderá também ser abortada, acionando o botão **"Cancelar"**.

Ao selecionar a opção **"Localizar lançador"**, é apresentada a listagem de todos os lançadores que apontam para o item que corresponde ao item atual de navegação. Por exemplo, se determinado usuário estiver navegando entre relatórios personalizados, ao acionar esta opção, será aberta uma lista de todos os lançadores que correspondem ao item "Relatório" atual de navegação. Nesta tela, além de visualizar os lançadores para um item, você pode excluir um lançador do item e/ou alterar sua descrição.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)

## Impressão das Etiquetas

As etiquetas podem ser impressas utilizando-se de três mecanismos diferentes:

- Applet (utilização de Plugin's - em alguns browser's não são suportados);
- Sankhya WebConnection;
- SPS - Sankhya Print Service;

Para essas três formas de impressão, o comportamento descrito abaixo será o mesmo:

**1** - Não sendo informado um nome no campo Impressora no Modelo de Etiquetas, ao solicitar a impressão, será aberto um pop-up de Impressora Substituta para seleção da impressora desejada;

**2** – Sendo informado o nome da impressora igual a "PADRAO", a etiqueta será impressa na impressora definida como padrão;

**3** – Se for definido um nome de impressora válido, ou seja, que está instalada, a etiqueta será impressa nessa impressora;

**4** – Sendo informado um nome de impressora inválido, ou seja, uma impressora não instalada, será apresentado o pop-up de Impressora Substituta para que seja selecionada uma impressora válida.

**Observação:** Na montagem dos dados para a impressão de etiquetas no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) (botão [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), [Imprimir etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#imprimiretiquetas), **"Etiquetas por Parceiro"**), o sistema não considera a query personalizada, ele busca os dados diretamente da nota, filtrando pelo NUNOTA e trazendo alguns campos específicos, como por exemplo **"CODPARC"**, **"NOMEPARC"**, **"NUNOTA"**, entre outros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)

## Impressão de Etiquetas através da tela de Parceiros

Na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), clique no botão **"Outras opções"** e selecione a opção **"Impressão de Etiquetas"**:

![Imagem 4: Na tela Cadastro de Parceiros , clique no botão "Outras opções" e selecione a opção "Impressão de Etiquetas" :](https://ajuda.sankhya.com.br/hc/article_attachments/4403845171607)

Após isto, no pop-up informe o **"Modelo de Etiqueta"** a ser utilizado, a **"Quantidade"** de etiquetas por parceiro a serem impressas e se serão impressas etiquetas apenas para o parceiro selecionado (filtrado na tela) ou para todos os parceiros presentes na grade. Se desejar imprimir etiquetas para todos os usuários apresentados/filtrados na grade, assinale a marcação **"Imprimir etiquetas para todos os parceiros da grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)

## Impressão de Etiquetas através do Cadastro de Produtos

Na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque), aba **"Estoque"**, selecione no botão **"Outras opções"** a opção **"Imprimir etiquetas"**.

![Imagem 5: Na tela Cadastro de Produtos , aba "Estoque" , selecione no botão "Outras opções" a opção "Imprimir etiquetas" .](https://ajuda.sankhya.com.br/hc/article_attachments/4403845192727)

Após selecionar o **"Modelo de Etiqueta"**, você pode informar caso necessário, a tabela de preço, a unidade alternativa, o complemento, entre outras; e solicitar a impressão através do botão **"OK"**. Vejamos sobre cada um desses campos a seguir:

No campo **"Quantidade"** indique a quantidade de etiquetas que serão impressas.

**Nota:** Caso seja informado **"0"** (zero), nenhuma etiqueta será impressa.

Quando você habilita a marcação **"Imprimir de acordo com a quantidade em estoque"**, o sistema irá utilizar a quantidade do produto em estoque como quantidade de etiquetas a serem impressas.

O preço do produto impresso na etiqueta será o valor informado na tabela de preço preenchida no campo **"Tabela de preço"**. Não sendo informada nenhuma tabela, o produto na etiqueta será impresso sem valor.

A **"Unidade alternativa"** informada, será a unidade impressa na etiqueta para o(s) produto(s) selecionado(s).

Você pode inserir um **"Complemento"** e uma informação para **"Controle"** que será impresso na etiqueta.

Se a marcação **"Imprimir para todos os produtos selecionados"** estiver habilitada, o sistema irá imprimir etiquetas para todos os estoques de todos os produtos.

Cada produto pode ter 1 ou mais estoques. Se você marcar a opção **"Imprimir para todos os itens de estoque selecionados"**, o sistema irá imprimir etiquetas para todos os estoques daquele produto, ou seja, todos os estoques que estão carregados na aba Estoque.

Quando o campo Imprimir para todos os produtos selecionados estiver assinalado, o sistema habilita o campo **"Empresa estoque"** para que seja informada uma empresa, se necessário. Caso você realize a marcação desse campo, o sistema irá imprimir as etiquetas referentes a empresa filtrada. Não informando nada, será impresso de todas as empresas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)

## Impressão de Etiquetas através dos Portais

Nos [Portais de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e [Movimentação Interna](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas), selecione um documento, e clique no botão **"Outras opções"**, opção **"Imprimir Etiquetas"**, você poderá solicitar a impressão por Parceiro ou por Produto. Vejamos sobre cada uma dessas alternativas a seguir:

**Etiquetas por Parceiro**

[GIF animado: Imagem 6: Etiquetas por Parceiro](https://ajuda.sankhya.com.br/hc/article_attachments/4403845252375)

No pop-up apresentado ao acionar a opção **"Etiquetas por Parceiro"**, informe primeiramente o **"Modelo de Etiqueta"** a ser utilizado e a **"Quantidade"** que se deseja imprimir.

Com a marcação **"Qtd. de acordo com o volume por nota"** efetuada, o número de etiquetas para cada item será igual ao campo quantidade de volumes.

Ao habilitar a marcação **"Atualizar quantidade de volume na nota"** o campo **"Quantidade de Volume"** dos itens da nota será atualizado com o valor do campo **"Qtd. Etiqueta"**, informado na grade inferior.

Você pode utilizar o botão **"Carregar Volumes"** para trazer os volumes das notas para a grade do pop-up.

**Nota:** No modelo padrão de etiquetas por parceiro tem-se a variável "SEQUENCIA", sua aplicabilidade está relacionada a impressão de mais de uma nota. Por consequência, o campo **"Sequência"** do modelo padrão seguirá a continuidade dos volumes e efetuará a quebra por nota. Este valor é sequencial da quantidade de volumes por nota. Deste modo, para cada volume a sequência terá o valor inicial 1 até o volume total da nota. Considere o seguinte exemplo:

Uma nota contendo 6 volumes, sua sequência terá os valores 1/6, 2/6, 3/6, 4/6, 5/6 e 6/6.

Para tanto, os modelos personalizados necessitam ser alterados manualmente. Esse procedimento é realizado através do iReport, modificando-se no XML a variável $V{PAGE\_NUMBER} / $F{QTDVOL} para $F{SEQUENCIA} / $F{QTDVOL}.

---

**Etiquetas por Produto**

![Imagem 7: Etiquetas por Produto](https://ajuda.sankhya.com.br/hc/article_attachments/4403845289239)

No pop-up apresentado ao acionar a opção **"Etiquetas por Produto"**, informe primeiramente o **"Modelo de Etiqueta"** a ser utilizado e a **"Tabela de Preços"** que deseja-se considerar para apresentação dos valores dos produtos.

Ao habilitar a marcação **"Qtd. de acordo com o volume por item"**, o número de etiquetas para cada item será igual ao campo quantidade de volumes.

**Nota:** A impressão de etiquetas por Parceiro ou por Produto impressos pela central não executa query. O sistema injeta os valores de acordo com a nota em questão e apenas para os campos que estão no modelo padrão (baixado através da tela de Modelo de etiquetas > botão **"Layout"**), além disso, somente os campos disponíveis no modelo padrão poderão ser utilizados para personalização de etiquetas.

Caso seja necessário obter outras informações de outras tabelas, pode se utilizar o PDES. Considere o seguinte exemplo de um PDES com a variável VLRNOTA que não é um campo disponível no modelo padrão:

br.com.sankhya.jasperfuncs.Funcoes.pdes($P{REPORT\_CONNECTION},"VLRNOTA", "TGFCAB", "NUNOTA = " + $F{NUNOTA})"

**Observação:** Não existem restrições quanto aos tipos de impressora; o sistema está adaptado para adotar vários tipos de impressora; com isso basta criar a configuração tanto na impressora quanto no sistema. A configuração do modelo de etiqueta em Ireport no formato jrxml, é perfeitamente flexível para atender seja a necessidade da empresa ou da impressora.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)

## Impressão de Etiquetas Vol. Conferência

A impressão de etiquetas por volume de conferência, é realizada por meio da tela [Impressão de Etiquetas Vol. Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601094-Impress%C3%A3o-de-Etiquetas-Vol-Confer%C3%AAncia).

![Imagem 8: A impressão de etiquetas por volume de conferência, é realizada por meio da tela Impressão de Etiquetas Vol.…](https://ajuda.sankhya.com.br/hc/article_attachments/4403853047319)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas#top)
