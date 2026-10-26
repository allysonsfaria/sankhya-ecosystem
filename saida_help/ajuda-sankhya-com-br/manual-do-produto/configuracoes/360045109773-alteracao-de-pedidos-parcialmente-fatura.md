---
id: "360045109773"
titulo: "Alteração de Pedidos Parcialmente Faturados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:01Z"
rotulos: ["Pedidos", "AJUDA DO SKW", "Configuração", "Alteração de Pedidos Parcialmente Faturados", "Pedido parcialmente faturado", "parcialmente", "Permitir Alteração após confirmar", "Permite alterar itens após faturar parcialmente", "Gravar Histórico de alteração do Pedido", "TGFHPE", "Histórico de Pedido", "QUEBRALINHAITE", "HABVINCPEDFINAN", "NUFIN", "Faturamento", "TOP", "Estoque", "Preferências"]
---

# Alteração de Pedidos Parcialmente Faturados

O mercado no segmento agrícola é um bom exemplo de usabilidade dessa função, pois exige negociações de longo prazo; por isso, uma hora ou outra, por motivos de variações dos preços do mercado, causas naturais, etc., o preço e quantidade negociada anteriormente poderá sofrer algumas alterações. A empresa lança um Pedido de Venda negociado, por exemplo, em 01/01 para ser entregue em até 31/12; durante esse prazo de negociação, ocorrem algumas variações do preço e quantidade dos itens, assim como itens excluídos e incluídos na negociação, por isso existe a necessidade de manter um Pedido de Venda faturado parcialmente e que poderá sofrer manutenção/alterações.

Para que você consiga efetuar esse procedimento, serão necessárias as seguintes configurações:

[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#tiposdeopera%C3%A7%C3%A3o-top)                                                   [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#dicion%C3%A1riodedados)

[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#prefer%C3%AAncias)                                                                          [Portais de Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#portaisdenotas)  

## Tipos de Operação - TOP

Para os tipos de movimento Pedido de Compra e Pedido de Venda, ao efetuar a marcação **"Permitir Alteração após confirmar"**(aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)), o sistema habilitará as marcações **"Permite alterar itens após faturar parcialmente"**(aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque)) e **"Gravar histórico de alterações do pedido"** (aba Geral), que possibilitarão a alteração do Pedido de Compra ou Pedido de Venda, faturado parcialmente.

[GIF animado: Imagem 1: Para os tipos de movimento Pedido de Compra e Pedido de Venda , ao efetuar a marcação " Permitir Alteração após…](https://ajuda.sankhya.com.br/hc/article_attachments/360103301893)

Se o tipo de movimento não for Pedido de Compra ou Pedido de Venda, mesmo que a marcação Permitir Alteração após confirmar seja efetuada, o sistema não possibilita que as outras duas marcações sejam habilitadas:

[GIF animado: Imagem 2: Se o tipo de movimento não for Pedido de Compra ou Pedido de Venda , mesmo que a marcação Permitir Alteração após…](https://ajuda.sankhya.com.br/hc/article_attachments/360103302053)

Se a marcação Permite alterar itens após faturar parcialmente for feita, possibilitará para a movimentação alterar pedidos já confirmados e faturados parcialmente, ou seja, o pedido não foi entregue totalmente e continua com os itens pendentes.

A marcação Gravar histórico de alterações do pedido, quando realizada, gravará as alterações dos itens que forem efetuadas mediante o faturamento parcial do pedido de compra/venda. Veja [Como habilitar e gravar os históricos de alterações realizadas nos itens de Pedidos de Compra/Venda faturados parcialmente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044462213-Como-habilitar-e-gravar-os-hist%C3%B3ricos-de-altera%C3%A7%C3%B5es-realizadas-nos-itens-de-Pedidos-de-Compra-Venda-faturados-parcialmente) e utilize esta marcação juntamente com a marcação acima.

**Importante:** na aba Estoque da TOP, você deve configurar o campo **"Aceitar Produto Repetido"** com a opção **"Sim"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#top)

## Dicionário de Dados

Quando a TOP estiver configurada para Gravar histórico de alterações do pedido, no caso de haver campos adicionais criados na tabela de Itens, e for necessário gravar histórico, estes terão que ser criados na tabela TGFHPE - Histórico de Pedido. Por exemplo:

**Tabela:** TGFITE

**Campos Adicionais:** AD\_VLRTS, AD\_VLRFRETE, AD\_VLRUNITSEMEN

Todos os campos do tipo **"Número Decimal"** e **"Permite visualizar na Grade"**:

![Imagem 3: Todos os campos do tipo "Número Decimal" e "Permite visualizar na Grade" :](https://ajuda.sankhya.com.br/hc/article_attachments/360101136254)

**Tabela:** TGFHPE

**Campos Adicionais:** AD\_VLRTS, AD\_VLRFRETE, AD\_VLRUNITSEMEN

#### Todos os campos do tipo Número Decimal e Permite visualizar na Grade:

![Imagem 4: Todos os campos do tipo Número Decimal e Permite visualizar na Grade :](https://ajuda.sankhya.com.br/hc/article_attachments/1500002306701)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#top)

## Preferências

O parâmetro **"Campos duplicam item nota(pedido parc. faturado) -** **QUEBRALINHAITE"** determinará quais serão os campos da tabela TGFITE, inclusive campos adicionais, que irão disparar no sistema o mecanismo de desmembrar a linha do item, quando o campo for alterado.

Você deve preencher a lista com o nome do campo igual ao da tabela, por exemplo, o campo **"Local"**, no parâmetro deverá ser preenchido como **"CODLOCALORIG"**; **"Vendedor"** como **"CODVEND"**. Os campos adicionais também deverão ser preenchidos conforme constam na tabela TGFITE, por exemplo, **"Valor Frete"** deverá ser inserido no parâmetro como **"AD\_VLRFRETE"**.

Somente os campos que estiverem nesse parâmetro irão disparar o mecanismo de desmembrar a linha do item quando o campo for alterado, ou seja, quando você alterar algum campo que esteja determinado no parâmetro, o sistema desmembrará a linha do item em duas, caso o item esteja parcialmente faturado.

Os campos informados no parâmetro QUEBRALINHAITE deverão ser separados por **","**(vírgula). Lembrando que, esse parâmetro apenas determinará quais campos que, quando alterados e com item parcialmente faturado, desmembrarão a linha do item em duas. Ao definir os campos nesse parâmetro, você deve se atentar para o fato de que na tela de Histórico de pedido, não necessariamente, haverão todos os campos da tabela TGFITE. Por exemplo, se você determinar que o campo Local deve disparar o mecanismo de desmembramento da linha do item em duas, o sistema irá desmembrar, mas não fará a gravação da informação no histórico.

Além disso, você não poderá incluir os campos que se referem à CODPROD e CONTROLE pois, esses campos não poderão ser alterados em itens parcialmente faturados; caso você os inclua no parâmetro, o sistema não os considerará.

Conforme exemplo que dei, o parâmetro foi configurado:

![Imagem 5: Conforme exemplo que dei, o parâmetro foi configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/1500002307321)

Os campos informados no parâmetro foram os campos adicionais criados na tabela TGFITE.

**Importante:** não tem necessidade de informar no parâmetro o campo Valor Unitário do Item pois, internamente, ele já será considerado ao duplicar o item no Pedido de Venda, se ele estiver faturado parcialmente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#top)

## Portais de Notas

Depois que você efetuar as configurações que informei acima, as validações serão feitas nos Portais de Notas:

**1)Bloquear alteração do item já faturado parcialmente:**

O sistema bloqueará a alteração do item caso a quantidade negociada a ser alterada, seja menor que a quantidade entregue, ou seja, quantidade faturada. Por exemplo:

Item: 179

Qtd. Negociada: 100

Qtd. Entregue: 30

Qtd. Pendente: 70

Ao alterar a **"Qtd Negociada"** para 10, o sistema emite a mensagem:

**"Qtd. Negociada" não pode ser menor que Qtd. Entregue".**

**2)Bloquear alteração do item já faturado totalmente:**

Se o item já tiver sido faturado totalmente, ou seja, a quantidade negociada for igual à quantidade entregue, ao tentar alterar o item, será exibida a mensagem:

**"Item já foi totalmente faturado e não pode ser alterado".**

**3)Vínculo com o financeiro:**

Com o parâmetro **"Utiliza vínculos de ped. a títulos no financeiro -** **HABVINCPEDFINAN"** habilitado, será feito o [Adiantamento/Empréstimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598534-Adiantamento-Empr%C3%A9stimo) com o Parceiro que foi lançado no Pedido de Venda e vinculado à despesa com a receita do Pedido de Venda.

Depois do Adiantamento/Empréstimo selecionado, o financeiro de despesa do Adiantamento será vinculado com a receita do Pedido de Venda. Ao alterar o Pedido que foi vinculado, de forma que o valor seja menor que o valor vinculado, o sistema emitida a seguinte mensagem:

**"Valor do pedido não pode ser menor que o valor vinculado".**

**4)Produtos com controle, se faturados parcialmente, não podem ser alterados.**

**5)Pedidos totalmente faturados não permite alteração da quantidade negociada:**

Em Pedidos que já foram totalmente faturados, se você tenta alterar a quantidade negociada, o sistema emitirá a mensagem abaixo:

**"Item já foi totalmente faturado e não pode ser alterado."**

**6)Exclusão de itens para pedidos faturados**

Ao solicitar a exclusão de um item que já tenha sido parcialmente/totalmente faturado, será exibida a mensagem abaixo:

**"Item X do pedido/nota Y já foi faturado. Não pode ser excluído".**

**7)Exclusão da Nota**

Quando você cancelar ou excluir uma Nota que tenha sido faturada de um Pedido, que permitia alteração dos itens, após o faturamento parcial, o sistema não realizará a recomposição do mesmo produto, em uma linha de item, se o mesmo estiver desmembrado (quando altera o **"Vlr.Unitário"**), por exemplo.

Uma vez o Pedido parcialmente faturado, se a Nota Faturada for excluída, os valores das quantidades entregues do Pedido serão zerados.

**8)Alteração no Cabeçalho do Pedido de Venda**

Caso o Pedido de Venda seja faturado parcialmente/totalmente, o sistema validará se você alterar a Empresa, o Tipo Negociação, o Tipo de Operação e o Parceiro, emitindo uma mensagem que estes não poderão ser alterados.

####

**Duplicação do Item:**

Quando um Pedido de Venda é faturado parcialmente e os valores que estão configurados no parâmetro **"Campos duplicam item nota(pedido parc. faturado) - QUEBRALINHAITE"** e os campos de **"Valor Unitário"** sofrem alterações no Pedido faturado, o sistema duplica a linha:

- **Alterando valor unitário:**

Exemplo:

**Pedido de Venda Nro Único: 4432**

| **Sequência** | **Produto** | **Qtd. Neg** | **Qtd. Entregue** | **Valor Unitário** | **Pendente** |
| --- | --- | --- | --- | --- | --- |
| 1 | 179 | 100 | 30 | 152,00 | Sim |

Solicitado alterar o Valor Unitário para 162,35:

| **Sequência** | **Produto** | **Qtd. Neg** | **Qtd. Entregue** | **Valor Unitário** | **Pendente** |
| --- | --- | --- | --- | --- | --- |
| 1 | 179 | 30 | 30 | 152,00 | Sim |
| 4 | 179 | 70 | 0 | 162,35 | Sim |

- **Alterando campos adicionais:**

Exemplo:

**Pedido de venda nro único: 4432**

| **Sequência** | **Produto** | **Qtd. Neg** | **Qtd. Entregue** | **Valor Unitário** | **Pendente** | **AD\_VLRFRETE** |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 180 | 50 | 20 | 138,00 | Sim | 5,00 |

####

Solicitado alterar o campo adicional AD\_VLRFRETE para 10,00:

| **Sequência** | **Produto** | **Qtd. Neg** | **Qtd. Entregue** | **Valor Unitário** | **Pendente** | **AD\_VLRFRETE** |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 180 | 20 | 20 | 138,00 | Não | 5,00 |
| 5 | 180 | 30 | 0 | 138,00 | Sim | 10,00 |

**Importante:** caso o item esteja com a quantidade entregue zerada, se for alterado os campos que solicitem a duplicação do item, esta não será efetuada, pois será considerado que o item ainda não foi faturado.

**Financeiro do Pedido:**

Pedido que provisiona o financeiro poderá ser alterado parcialmente, mediante alterações dos itens, que foram faturados parcialmente, duplicando o item na Nota e também os valores.

Por isso, o Total do Pedido irá alterar, tendo que alterar também o financeiro.

Provisões com **"Número Único do Financeiro"** (NUFIN) negativo, servem apenas para representar a parte da Provisão do Pedido que já foi transformada em um financeiro efetivo no faturamento. Relembrando, contudo, que um valor faturado não sofre alteração, sendo sempre o mesmo. Então, o financeiro com NUFIN negativo, mesmo refeito, terá sempre o mesmo valor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109773-Altera%C3%A7%C3%A3o-de-Pedidos-Parcialmente-Faturados#top)
