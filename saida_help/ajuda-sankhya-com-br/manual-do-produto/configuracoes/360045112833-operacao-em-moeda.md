---
id: "360045112833"
titulo: "Operação em Moeda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112833-Opera%C3%A7%C3%A3o-em-Moeda"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:27Z"
rotulos: ["Configuração", "Cotação", "Moeda", "TOP", "Financeiro", "Dolar", "Operação em Moeda", "Reais", "Operação em Moeda manual", "Configurações de Operações em Moeda Estrangeira", "Tabela de Preços"]
---

# Operação em Moeda

Nosso sistema está apto a trabalhar com operações em moeda estrangeira, onde para fazê-lo, temos que realizar configurações em algumas telas, que irão gerar embasamento suficiente para o sucesso destas operações. Dentre estas configurações, pode-se destacar, o registro de preços em tabela, e o faturamento com atualização de valores conforme variação de cotação.

Consideremos o comportamento do sistema envolvido nestas operações:

- Na tela [Tabelas de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os), temos o campo **"Moeda (Tabela de Preço)"**, onde você informará a moeda estrangeira da tabela em questão. As moedas apresentadas para escolha neste campo deverão ter sido previamente cadastradas na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas) e serão as do tipo **"Valor"**.

![Imagem 1: Na tela Tabelas de Preços , temos o campo "Moeda (Tabela de Preço)" , onde você informará a moeda estrangeira da tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/7544355590807)

Os valores informados para cada produto na grade, irão respeitar a moeda informada no campo **"Moeda (Tabela de Preço)"**. Este campo sendo mantido com o valor **"0"** (zero), a moeda corrente continuará sendo a moeda da tabela.

- Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro), você deverá efetuar a marcação **"Operação em Moeda"**, pois desta forma, o sistema irá entender que nos lançamentos realizados com esta TOP, será considerada a moeda estrangeira.

![Imagem 2: Na tela Tipos de Operação - TOP , aba Financeiro , você deverá efetuar a marcação "Operação em Moeda" , pois desta…](https://ajuda.sankhya.com.br/hc/article_attachments/7544462061079)

- No lançamento de pedidos ou notas, onde estejam sendo utilizadas TOP's que possuam a marcação **"Operação em Moeda"** (mencionada acima) realizada, e o campo **"Usar como Preço"** definido como **"Preço de Venda"**, o sistema irá buscar a tabela de preço mais recente do item, ou seja, aquela que possuir a maior **"Data de Vigor"**, e irá inserir o preço encontrado no valor em moeda do item.

**Observação:** ao realizar a marcação Operação em Moeda mencionada acima, os campos **"Total Líq. Itens em Moeda"** e **"Desc.Total dos itens em Moeda"** podem ser acrescidos no cabeçalho da nota após configurá-los na tela [Configuração de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), assim como os campos **"Vlr. Unit. Moeda"**, **"Vlr. Desc. Moeda"**, **"Vlr. Tot. Moeda"**, **"Preço Liq. Moeda"** e **"Total líq. Moeda"** dos itens.

**Nota:** quando necessário que o campo **"Vlr total"** da grade Itens da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) seja editável, insira o número da TOP utilizada na operação no campo **"Texto"** do parâmetro **"TOP para aceitar Qtd. igual a zero - TOPQTDZERO"**. Porém, se houver uma conversão com moeda, essa referida TOP **não** deve ser informada no parâmetro.

Caso a moeda informada no cabeçalho da nota seja diferente da moeda informada na tabela de preços do item que está sendo inserido, o sistema irá exibir alguns alertas, informando que as configurações estão incoerentes. Estes alertas, serão apresentados nos seguintes casos:

**1-** O pedido/nota estar configurado através de sua TOP, para trabalhar com moedas estrangeiras, o campo **"Usar como Preço"** também na TOP, está definido como **"Preço de Venda"**, porém a Tabela de Preços do item está configurada para a moeda corrente. Será apresentada a seguinte mensagem:

**"Configurações incoerentes: A TOP XX possui a marcação 'Operação em Moeda' mas fora encontrada a moeda YY neste cabeçalho. É necessário informar uma moeda diferente da moeda 0 neste cabeçalho ou a TOP não deve ser uma operação em moeda".**

**2-** O pedido/nota não estar configurado através de sua TOP, para trabalhar com moedas estrangeiras, o campo Usar como Preço também na TOP, está definido como Preço de Venda, e a Tabela de Preços do item estar configurada para a moeda estrangeira. Será apresentada a seguinte mensagem:

**"Configurações incoerentes: A TOP XX não possui a marcação 'Operação em Moeda' mas fora encontrada  a moeda YY na tabela de preço ZZ. Neste caso, a moeda informada na tabela de preço deve ser moeda 0 ou a TOP deve possuir a marcação 'Operação em Moeda'. Alternadamente, a opção 'Preço de Venda' não deve estar selecionada no campo 'Usar como Preço' na TOP".**

**3-** O pedido/nota estar configurado através de sua TOP, para trabalhar com a moeda estrangeira **"X"**, o campo Usar como Preço também na TOP, está definido como Preço de Venda, mas a Tabela de Preços do item, está configurada para uma moeda estrangeira **"Y"**. Será apresentada a seguinte mensagem:

**"Configurações incoerentes: Encontrado um valor unitário para o item especificado na moeda XX através da tabela de preço YY, mas a moeda ZZ foi encontrada neste cabeçalho. As moedas devem ser as mesmas".**

**Descontos Promocionais**

Em relação à utilização dos descontos promocionais para itens inseridos em um pedido/nota, onde a TOP esteja configurada para operar com moedas estrangeiras, os descontos poderão ser fornecidos em percentual. Com isso, na inserção de um item em um pedido/nota que se enquadre nas operações em moeda estrangeira, a consulta de promoções será realizada ignorando àquelas promoções que não sejam por **"Percentual"**.

Deste modo, os descontos configurados na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais) por **"Valor de Desconto"**, **"Valor de Venda"** e **"% Desc. Bonificação"** não serão utilizados para compor os descontos promocionais dos itens em operações com moeda estrangeira.

![Imagem 3: Deste modo, os descontos configurados na tela Descontos Promocionais por "Valor de Desconto" , "Valor de Venda" e "%…](https://ajuda.sankhya.com.br/hc/article_attachments/7544615546519)

Para que os descontos promocionais funcionem, são necessárias algumas configurações:

- Na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), o Tipo de Negociação que será utilizado nos pedidos/notas, o campo **"Desconto Promocional"**, deve estar selecionado com a opção **"Considerar Sempre"**.
- Na tela Descontos Promocionais o campo **"Atua sobre a tabela de preço"** deve ter a tabela de preço corretamente informada.
- O produto, parceiro e empresa configurados também na tela Descontos Promocionais, devem ser os mesmos que os lançados no pedido/nota.

Na tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos)[,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos) quando esta estiver contextualizada com uma TOP configurada para trabalhar com **"Operações em Moeda"**, as promoções diferentes de **"Percentual"** não serão consideradas para demostração dos preços em promoção e aplicação no item.

**Importante:** as Operações em Moeda não correspondem a processos realizados pelo [Portal de Importação do XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), e, portanto, não terão suas informações consideradas nesta tela.

**Faturamento de Pedidos**

Na realização do faturamento de um pedido, será apresentado um pop-up que traz a moeda selecionada no cabeçalho do documento (apenas para visualização), o campo **"Vlr. Moeda"** que apresenta a cotação da moeda do dia (ou da última data anterior ao dia atual), e um botão para selecionar-se outra cotação para a moeda, se for o caso.

![Imagem 4: Na realização do faturamento de um pedido, será apresentado um pop-up que traz a moeda selecionada no cabeçalho do…](https://ajuda.sankhya.com.br/hc/article_attachments/7546756240279)

Ao concluir o faturamento, a nota destino será gerada com os valores em reais condizentes com os valores em moeda e a cotação informada, incluindo descontos.

Esta nota destino, pode ou não ser também uma operação em moeda; de qualquer forma, os valores em moeda não se alteram neste faturamento, eles serão mantidos iguais a nota de origem.

No faturamento de um pedido em moeda para uma nota que não é uma operação em moeda, os campos de valores em moedas ficarão preenchidos para demonstrar a origem dos valores e manter seu histórico.

Na Central de Vendas, em pedidos/notas que não sejam operações em moeda estrangeira, os campos referentes aos valores em moeda, ficarão impedidos de serem alterados manualmente. São eles:

- Vlr. Unit. Moeda;
- Vlr. Desc. Moeda;
- Vlr. Tot. Moeda;
- Preço Líq. Moeda;
- Total líq. Moeda.

Os campos **"Total líq. Itens em Moeda"** e **"Desc. Total dos itens em Moeda"** disponíveis no cabeçalho da nota, estarão protegidos contra edição, independente do pedido/nota ser uma operação em moeda estrangeira ou não.

**Nota:** no lançamento de um pedido ou nota em que a TOP utilizada não possua a marcação **"Operação em moeda"**, e nem a marcação **"Utiliza Indexação"** presente na aba **"Validações"** efetuada, ao informar uma moeda no cabeçalho da nota, o sistema não irá abrir automaticamente a tela para seleção da cotação, porém será permitido que o valor da moeda seja informado manualmente.

Porém, quando clicar-se no ícone ![Imagem 5: Porém, quando clicar-se no ícone para seleção da moeda, a tela para escolha da cotação será aberta normalmente;…](https://ajuda.sankhya.com.br/hc/article_attachments/7547042088215) para seleção da moeda, a tela para escolha da cotação será aberta normalmente; definindo-se a cotação e escolhendo-se a opção **"Usar esta cotação"**, o valor selecionado será apresentado no campo **"Vlr. Moeda"** no cabeçalho da nota.

**Observações**

**(2)** Quando for selecionado um produto, e este trouxer de forma automática da tabela de preços o valor unitário, se for realizada uma modificação no campo de valor unitário da moeda, o valor em R$ que foi adquirido da tabela de preços será desconsiderado, ou seja, sempre irá prevalecer o valor informado pelo usuário em moeda.

**(2)** Com o parâmetro **"Ajusta decimais para cálculo com moeda - AJUSTACSDECMOE"** ligado, o cálculo dos itens da nota serão realizados conforme o campo **"Vlr. Moeda"** configurado no cabeçalho da nota de faturamento, ainda que estes valores sejam divergentes da nota de origem.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112833-Opera%C3%A7%C3%A3o-em-Moeda#top)
