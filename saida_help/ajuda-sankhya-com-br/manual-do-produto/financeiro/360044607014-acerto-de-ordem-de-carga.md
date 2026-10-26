---
id: "360044607014"
titulo: "Acerto de Ordem de Carga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:41:24Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Parceiro", "Transportadora", "Acerto de Ordem de Carga", "Abrir caixa", "Baixar em lote", "CODLANCBAIXA", "EXIGECONFCAIXA", "Fechar caixa", "GERDIFACOC", "GERMOVBANACER", "OCULVLRRETACER", "TIPTITDINHEIRO", "br.com.sankhya.fin.mov.acertoordemcarga", "Acerto de Ordem de Carga manual", "Transporte", "Preferências", "Financeiro", "OFEROPCBAIXTIT", "Transportadora Ordem de Carga Acerto"]
---

# Acerto de Ordem de Carga

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312356621719) Módulo: Financeiro> Rotinas> Acertos
```

---

Esta rotina é empregada na realização do controle de cargas entregues por uma determinada transportadora.

Quando uma nota é lançada para uma determinada empresa, ela pode ser vinculada a uma ordem de carga, posteriormente essa nota será entregue para o seu respectivo parceiro juntamente com a carga. Esse transportador pode levar várias notas numa só Ordem de Carga e além disso, pode levar também alguns títulos que estejam pendentes para aquele parceiro da entrega.

Assim, o controle de notas e títulos que o transportador está levando juntamente com a carga é feito através desta tela; quando o transportador retornar da viagem, serão ponderadas as suas despesas, o valor que ele trouxe dos títulos recebidos, além de serem relatados os títulos que retornaram, que por algum motivo não puderam ser recebidos.

![Imagem 2: Assim, o controle de notas e títulos que o transportador está levando juntamente com a carga é feito através desta…](https://ajuda.sankhya.com.br/hc/article_attachments/8453667261207)

No lado esquerdo da tela temos o painel **"Filtro"**, que deve ser obrigatoriamente preenchido com a **"Empresa"** e **"Ordem de Carga"** correspondentes ao acerto a ser realizado; logo abaixo dos filtros tem-se o painel **"Opções"** contendo algumas funcionalidades a serem utilizadas, as quais podem ser visualizadas acionando-se os link's abaixo.

| [Abrir caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abrircaixa) | [Fechar caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#fecharcaixa) |
| --- | --- |
| [Relatório resumo acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#rel.resumoacerto) | [Relatório fechamento caixa/acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#rel.fechamentocaixaacerto) |
| [Baixar em lote](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#baixaremlote) | [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#preferncias) |
| [Aba Resumo do Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abaresumodoacerto) | [Aba Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abanotas) |
| [Aba Outros Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abaoutrosttulos) | [Aba Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abadespesas) |
| [Baixa agrupada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#baixaagrupada) | [Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#parmetrosqueinfluenciamestarotina) |

Esta tela depende de algumas configurações que são realizadas partindo-se de outras telas do sistema, são elas:

Transferência de Títulos p/ Ordem de Carga: Os títulos que são entregues para o Motorista da Transportadora receber dos clientes, são vinculados a Ordem de Carga através desta tela;

[Configuração de Tipos de Títulos p/ Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606974): Configuram-se os Tipos de Títulos que serão utilizados no Acerto da Ordem de Carga;

[Histórico p/Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392553-Hist%C3%B3rico-p-Acerto-de-Ordem-de-Carga): Deve-se aqui cadastrar os Históricos que serão utilizados no Acerto da Ordem de Carga;

[Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaacertodeordemdecarga), destacando-se as seguintes opções:

- Valor baixado deve ser igual ao Retornado?;
- Transferir a diferença entre o valor retornado e o baixado?.

## Abrir caixa

O procedimento de abertura de Caixa é feito para uma Conta Bancária vinculada ao parceiro Transportador, pois é com ele que estará o dinheiro do acerto da ordem de carga, ou seja, as notas e os títulos que foram encaminhados para serem recebidos, serão pagos ao transportador. Abre-se um caixa para a conta bancária deste parceiro, para que possa ser feito balanço dos recebimentos realizados. Ao dar início a um acerto, o caixa deve ser aberto clicando-se em **"Abrir caixa"**.

É importante mencionar que a Conta Bancária vinculada ao **"Parceiro Transportador"**, deve ser do tipo **"Caixa (PDV)"**, configuração esta, realizada no cadastro de Contas Bancárias, aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros), campo **"Tipo de conta"**. Além disso, seu vínculo ao parceiro é feito no cadastro de Parceiros, aba [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontabancria); por sua vez, a aba **"Conta Bancária"** é habilitada, caso o parceiro seja também apontado na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), campo **"Tipo"**, como **"Conta Adiantamento"**.

Ao clicar na opção **"Abrir caixa"**, é aberto um pop-up contendo as **"Informações do caixa"**; nele, tem-se o **"Número do caixa"**, o **"Usuário"**, a **"Conta"** e seu respectivo **"Saldo inicial"**; o Saldo inicial será considerado um Adiantamento.

Depois de aberto o caixa, a opção **"Fechar caixa"** é habilitada, e consequentemente o link Abrir caixa ficará desabilitado.

**Importante:** Se já existir um caixa aberto para um determinado transportador, o sistema não permitirá que se abra outro caixa de outra ordem de carga para aquele mesmo transportador. É necessário que se inicie o processo de Acerto de Ordem de Carga e o finalize (fechando o caixa) para que se possa iniciar outro processo para esse transportador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Fechar caixa

Esta opção é utilizada para fechar o caixa que foi aberto ao se iniciar a rotina de Acerto de ordem de carga, ou seja, finalizar os lançamentos das despesas de viagem e dos títulos recebidos.

![Imagem 3: Esta opção é utilizada para fechar o caixa que foi aberto ao se iniciar a rotina de Acerto de ordem de carga, ou seja,…](https://ajuda.sankhya.com.br/hc/article_attachments/8453994768023)

O fechamento de caixa é um procedimento que aconselhamos ser realizado sem que exista nenhuma diferença entre o valor utilizado como **"Adiantamento"** e o **"Valor Total retornado"**. Será permitido o fechamento com divergência entre estes valores, apenas se o parâmetro **"Gerar Diferença do Acerto de OC p/ Financeiro - GERDIFACOC"** estiver desativado; se este parâmetro estiver habilitado, será preciso Gerar a diferença para financeiro; a configuração para esta geração é realizada nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#preferncias) de Acerto de Ordem de Carga.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Rel. resumo acerto

Ao acionar esta opção será gerada a visualização de um Relatório de resumo do acerto, ou seja, os procedimentos realizados até então e que estão presentes na aba [Resumo do Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abaresumodoacerto). Ao acioná-la, será solicitado o preenchimento da **"Data do acerto"** para que esta seja inserida no relatório.

![Imagem 4: Ao acionar esta opção será gerada a visualização de um Relatório de resumo do acerto, ou seja, os procedimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/8454845283991)

Tem-se no relatório além dos dados da Aba Resumo do Acerto, a numeração da **"Ordem de Carga"**, a **"Empresa"**, a **"Transportadora"**, bem como seu respectivo Motorista, o Conferente responsável pelo acerto e sua correspondente Data:

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Rel. fechamento caixa/acerto

Por essa opção, realiza-se a geração de um relatório que lista os caixas que foram abertos e/ou fechados. Caso a visualização/impressão deste relatório seja necessária, determina-se na seção **"Critérios de Impressão"** as particularidades acerca dos Créditos/Débitos, Vendas e Produtos relacionados ao acerto.

![Imagem 5: Por essa opção, realiza-se a geração de um relatório que lista os caixas que foram abertos e/ou fechados. Caso a…](https://ajuda.sankhya.com.br/hc/article_attachments/8454119728407)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Baixar em lote

Por meio da opção **"Baixar em lote"** pode-se realizar a baixa em lote (em conjunto) dos títulos correspondentes à todas as notas pertencentes a Ordem de Carga.

Ao clicar em Baixar em lote será aberto o pop-up com esta mesma nomenclatura:

![Imagem 6: Ao clicar em Baixar em lote será aberto o pop-up com esta mesma nomenclatura:](https://ajuda.sankhya.com.br/hc/article_attachments/8454198240791)

Serão exibidos aqui todos os títulos vinculados às notas que forem apresentadas na grade de notas. Pode-se selecionar um ou vários títulos a serem baixados, utilizando-se dos botões **"Remover Selecionados"** e/ou **"Remover Não Selec."**; uma vez selecionados os títulos desejados, por meio do botão **"Baixar"** localizado na parte inferior do pop-up, inicia-se o processo de baixa, em que será aberto um segundo pop-up denominado **"Preferências de baixa"**, para preenchimento de alguns dados pertinentes a este processo. É importante informar que serão apresentados para baixa em lote, apenas títulos nas seguintes condições:

- Títulos reais, ou seja, que não são provisões;
- Apenas títulos não baixados;
- Somente títulos que não foram renegociados;
- Exclusivamente títulos em que utilizou-se em seu lançamento, um tipo de título que permita baixa no acerto (tela [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaacertodeordemdecarga), marcação **"Pode Baixar?"**).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Preferências

Nesta opção serão definidas algumas singularidades que serão utilizadas pela rotina de Acerto de Ordem de Carga.

![Imagem 7: Nesta opção serão definidas algumas singularidades que serão utilizadas pela rotina de Acerto de Ordem de Carga .](https://ajuda.sankhya.com.br/hc/article_attachments/8454264361367)

Na seção **"Ao fechar o caixa"** tem-se configurações que serão empregadas pelo sistema no fechamento do caixa do acerto. Nesta seção, destacamos a opção **"Mudar todos os títulos para a Conta Padrão"** que ao ser acionada, ao fechar o caixa, os títulos do acerto terão sua conta alterada para a "Conta Padrão" informada no parâmetro **"Conta padrão para financeiro - CONTAPADRAO"**. A marcação **"Permitir despesas no Acerto?"** quando realizada, tem-se a aba [Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abadespesas) habilitada na tela para seu correspondente preenchimento.

A seção **"Ao gerar financeiro da diferença"** conta com configurações utilizadas pelo sistema para geração de títulos a fim de compensar a diferença no caixa caso o valor retornado pelo transportador seja menor que o esperado; pode-se ter este caso, quando algum título vinculado à Ordem de Carga não foi recebido por determinado motivo; essa diferença deve ser gerada, pois o sistema não permite o fechamento do caixa caso exista diferença de valores, exceto se o parâmetro de chave GERDIFACOC estiver desabilitado, como mencionado no tópico [Fechar caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#fecharcaixa).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Aba Resumo do Acerto

Nesta aba são apresentados os títulos conforme definição prévia na tela [Configuração de Tipos de Títulos p/ Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606974). Nessa aba, pode-se analisar as informações do acerto, uma vez que, na grade predominante na aba, são exibidos os títulos e seus respectivos valores esperados e retornados.

![Imagem 8: Nesta aba são apresentados os títulos conforme definição prévia na tela Configuração de Tipos de Títulos p/ Acerto .…](https://ajuda.sankhya.com.br/hc/article_attachments/8454361221399)

No rodapé da aba tem-se alguns valores informativos:

- **Adiantamento:** A quantia de adiantamento feita ao transportador, será apresentada nesse campo.
- **Vlr. total esperado:** Soma dos valores esperados.
- **Total despesas:** Total das despesas cadastradas na aba Despesas.
- **Vlr. da diferença:** Valor calculado da diferença entre o **"Adiantamento"** e o **"Total retornado"**.
- **Qtd. notas a conferir:** A medida que são conferidas as notas pela aba [Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abanotas), o sistema atualiza este campo.
- **Total retornado:** Valor Total retornado com o transportador.

Não é possível realizar nenhuma alteração no acerto enquanto o caixa não for aberto; feita sua abertura, qualquer informação inserida na grade desta aba, deverá ser salva e em seguida confirmada ou rejeitada pelos botões **"Confirmar"** e **"Rejeitar"**, respectivamente, que se encontram na parte superior da grade. Além disso, ao lado destes botões, pode-se digitar a descrição de algum título específico de modo que, ao teclar-se **"Enter"** o sistema posiciona no título informado.

O botão **"Gerar diferença p/ financeiro"** é utilizado para gerar um título para compensar o **"Valor da Diferença"**, que pode estar no caixa por diversos motivos, como por exemplo, o parceiro não pôde receber alguma mercadoria, assim o transportador não retornará com o valor esperado, e o caixa ficará com diferença. Porém, para fechar o caixa será preciso que essa diferença seja igual a "0" (zero). Deste modo, ao clicar neste botão, o sistema irá gerar um financeiro para compensar essa divergência para que o caixa possa ser fechado.

**Importante:** Utilizando o botão **"Gerar diferença p/ financeiro"**, o título de despesa não será apresentado na aba [Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abadespesas). Além disso, o título gerado será apresentado com o campo Origem preenchido como **"Estoque"** mesmo não sendo um financeiro originado diretamente de uma nota; este comportamento impede que o financeiro seja modificado através da [Central de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154).

O botão Gerar diferença p/ financeiro irá gerar 2 (dois) títulos, sendo um de Despesa, que permitirá [Fechar o caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#fecharcaixa) e será apresentado somente no relatório [Resumo do Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abaresumodoacerto), e outro título de Receita "contra" o parceiro Motorista. Este comportamento ocorre pelo fato desta diferença não possuir uma **"Nota/Recibo"** que justifique a diferença entre o **"Valor Esperado"** e o **"Valor Retornado"**. Assim, teremos o exemplo:

Um motorista saiu para realizar as entregas de 2 notas, com "Tipo de Título" = Dinheiro, no valor total de R$ 2.000,00; realizou as entregas e recebeu os valores correspondentes. Durante o retorno, este motorista utilizou parte deste dinheiro para uma despesa pessoal, no valor de R$ 50,00. Ao realizar o acerto desta **"Ordem de Carga"**, o **"Valor Esperado"** será de R$ 2.000,00 (valor total), porém o **"Valor Retornado"** será de R$ 1.950,00. Se você clicar em Gerar diferença p/ financeiro, o sistema irá gerar o título de despesa, eliminando assim a diferença no fechamento. Irá gerar também uma receita contra o parceiro motorista para que este "restitua" o valor gasto por ele.

Quando existir um documento (nota, recibo etc.) que "justifique" a existência dessa despesa, deve-se utilizar a aba[Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abadespesas), para lançar o documento. Tem-se o exemplo:

Durante o retorno da entrega foi necessário pagar um "pedágio". O motorista utilizou o dinheiro recebido das entregas para pagar esta despesa. Ao proceder com o acerto desta Ordem de Carga, este "gasto" será registradona aba Despesasatravés de seu comprovante (recibo, nota).

**Observação:** Depois que uma Ordem de Carga é apresentada na tela Acerto de Ordem de Carga, a nota integrante da Formação de Carga não poderá ser modificada, pois os valores podem ficar divergentes. Se uma Ordem de Carga foi formada com uma nota, acessou-se a tela Acerto de Ordem de Carga e essa nota foi exibida, caso esta mesma nota seja retirada da formação de carga, ela não será retirada do acerto.

Após a geração da diferença para o financeiro, o botão **"Gerar diferença p/ financeiro"** passará a apresentar a nomenclatura **"Visualizar diferença p/ financeiro"**, para que o título de despesa anteriormente gerado possa ser visualizado, caso necessário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Aba Notas

Nesta aba são disponibilizadas todas as notas pertencentes à Ordem de Carga. Pode-se notar:

- A grade superior contendo as Notas da Ordem de Carga, contendo opção para marcar as notas, o que possibilita a identificação de quais notas não foram conferidas;
- A grade **"Financeiro(s) da nota"** possui a opção para marcar os financeiros, possibilitando também a identificação de quais não foram conferidos (marcações **"Todas as notas"** ou **"Notas não conferidas"**).

O botão **"Acompanhamento"** é utilizado para lançar os acompanhamentos de nota. Esses acompanhamentos se referem aos recebimentos dessas notas pelo parceiro, onde é possível informar a Data e Hora do acompanhamento, a Sequência relacionada ao item da nota, bem como a Referênciado documento, e dar às notas Qualidade e Pontualidade.

Já o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16080124459031) **"Outras Opções..."** dispõe de duas alternativas, que são:

- **Marcar todas como entregues:** Acionando-se esta opção, todas as notas exibidas na grade terão o campo **"Entregue"** modificado para a opção **"Entregue"**.
- **Marcar todas como não entregues:** De forma inversa à opção anterior, clicando-se nesta alternativa, as notas apresentadas na grade terão o campo Entregue definido como **"Não entregue"**.

![Imagem 10: Marcar todas como não entregues : De forma inversa à opção anterior, clicando-se nesta alternativa, as notas…](https://ajuda.sankhya.com.br/hc/article_attachments/8454389032983)

#### Grade de Notas

Além de alterar os registros pela grade das Notas, é possível modificar para o modo de edição, de modo a visualizar melhor os dados de uma única nota.

O campo Entregue deve ser alterado; ele inicialmente é exibido com a opção **"Não Entregue"** e quando estiver com esse valor, a nota será considerada como **"Não Conferida"** e com isso, o sistema não permitirá fechar o caixa até que todas as notas sejam conferidas, ou seja, até que todas as notas tenham o campo Entregue modificado para algum valor diferente de **"Não Entregue"**.

**Observação:** Ao realizar o fechamento de uma Ordem de Carga, todo documento vinculado a esta Ordem que não for um Pedido de Venda, ou ainda se for um Pedido de Venda que não esteja faturado para uma Nota que também faça parte da carga, e cujo campo Entregue esteja indicado como Devolvido ou Reentregar, terão a informação pertinente ao campo Ordem de Carga do cabeçalho da Nota, anulada.

#### Grade Financeiro(s) da nota

O botão **"Baixar"** realiza a baixa do financeiro. Sempre que o campo **"Retornado"** permanecer como **"Não"**, o financeiro deverá ser baixado, pois se o título não retornou, significa que ele foi recebido, sendo necessário portanto, efetuar sua baixa. Se o campo Retornado estiver com a opção **"Sim"**, este botão ficará desabilitado, pois se o título retornou, significa que ele não foi recebido, e assim não deverá ser baixado. A coluna Retornado nesta grade, deverá ser marcada como **"Sim"** sempre que o responsável pelo transporte retornar com o Boleto.

Já o botão **"Estornar"** efetua o estorno do financeiro.

O botão **"Ver financeiro"** irá abrir a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), posicionada no financeiro da nota em questão, que está sendo conferida. Não será possível baixar o título pela tela aberta por este botão; para fazê-lo, deve-se utilizar o botão **"Baixar"**, mencionado acima.

**Importante:** As baixas realizadas na tela Acerto de Ordem de Carga, poderão ser executadas apenas se o usuário logado for o usuário que fez a abertura do caixa. Caso seja feita a tentativa de baixa por um usuário diferente do logado, será exibida a seguinte mensagem:

**"A baixa dos títulos vinculados a Ordem de Carga deve ser feita pelo usuário que abriu o caixa."**

O parâmetro **"Baixa de múltiplos títulos - OFEROPCBAIXTIT"** pode influenciar na rotina de baixa de três maneiras:

- Se definido como **"Baixa com Renegociação"**, será possível nas rotinas de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) e Acerto de Ordem de Carga, efetuar a seleção e posterior baixa de múltiplos títulos de uma única vez; este procedimento implica na realização de uma baixa agrupada, de modo que os títulos selecionados serão incorporados em um único documento;
- Uma vez que o parâmetro citado esteja determinado com a opção **"Não permitir"**, não será possível proceder com a baixa de múltiplos títulos ao utilizar-se da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) e do Acerto de Ordem de Carga; persistindo a tentativa de baixa, o sistema irá proceder com esta ação apenas para o primeiro título selecionado, mesmo que vários títulos tenham sido assinalados.
- Optando-se pela opção **"Baixa Automática"**, pode-se efetuar nas rotinas de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) e Acerto de Ordem de Carga a seleção e baixa de múltiplos títulos de uma única vez; sem gerar a renegociação dos mesmos. Deste modo, tem-se a baixa individual de cada título.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Aba Outros Títulos

São apresentados nesta aba, os títulos que foram escolhidos na tela [Transferência de Títulos p/ Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606634).

![Imagem 11: São apresentados nesta aba, os títulos que foram escolhidos na tela Transferência de Títulos p/ Ordem de Carga .](https://ajuda.sankhya.com.br/hc/article_attachments/8454602720279)

Esta aba disponibiliza os títulos que foram enviados juntamente à Ordem de Carga. Tem-se também os seguintes botões:

- **Baixar:**Para realização da baixa do financeiro. Neste procedimento, as datas de pagamento dos cheques devem ser menores ou iguais ao vencimento. O sistema permite que o tipo de título seja modificado.
- **Estornar:** Utilizado para execução do estorno do financeiro.
- **Ver financeiro:** Para visualizar a tela de Movimentação Financeira posicionada no título em questão.

**Observação:** Essa aba é semelhante a grade Financeiro(s) da nota da aba [Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abanotas); apresentam as mesma funcionalidade e obedecem as mesmas regras.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Aba Despesas

Essa aba é habilitada para uso, caso a marcação **"Permitir despesas no acerto?"**, localizada nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#preferncias)da tela esteja realizada.

![Imagem 12: Essa aba é habilitada para uso, caso a marcação "Permitir despesas no acerto?" , localizada nas Preferências da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/8454772105751)

São incluídas nesta aba as despesas obtidas pelo motorista. Esta é uma aba similar à tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), inclusive com botões de **"Baixar"**, **"Estornar"** e **"Ratear"**.

A baixa das despesas incluídas nesta aba, será feita na **"Conta do Motorista"**. As despesas a prazo continuarão pendentes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Baixa agrupada

Por meio da aba [Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abanotas), será possível realizar a baixa agrupada das notas referentes ao Acerto de Ordem de Carga; este procedimento consiste em incorporar os títulos selecionados em um único documento por meio de uma renegociação. Deste modo, um título baixado na realidade será um título renegociado, uma vez que este representa a junção dos financeiros originais. Essencialmente, o sistema soma os valores relevantes dos títulos e um único documento e posteriormente vincula o título resultante aos títulos originais através da renegociação.

Particularidades da Baixa agrupada:

- Na aba Notas, selecione na grade superior a nota e, em seguida, na grade Financeiro(s) da nota, escolhe-se os títulos que serão reunidos para realização da baixa agrupada;
- Todos os títulos selecionados devem ser do mesmo Parceiro e Empresa;
- Não é possível realizar a baixa agrupada para títulos de Receita/Despesa diferentes;
- Esta rotina não está apta a lidar com solicitações de liberação. Caso ocorra a solicitação de liberação para o título resultante, a baixa agrupada não será realizada;
- A data de vencimento do título resultante, será a menor data de vencimento dos títulos originais, de forma que, esta data será a base para o cálculo de juros e multas no momento da baixa;
- O cálculo de juros e multas será efetuado apenas para o título resultante;
- Quando possível, a origem do título resultante será a mesma dos títulos originais; caso contrário, será preenchido como Financeiro.
- Sempre que possível, os outros impostos pertinentes às notas também serão agrupados, porém, não será permitida a edição de outros impostos na baixa agrupada;
- O procedimento de Estorno não elimina a baixa agrupada (renegociação) que foi realizada. Caso seja necessário desfazer a renegociação, deve-se fazê-lo manualmente através da tela [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)

## Parâmetros que influenciam esta rotina

**Código do lançamento bancário para baixa - CODLANCBAIXA:** O campo **"Lançamento"** na tela de Baixa no caso do Acerto, é apresentado em consequência do preenchimento deste parâmetro.

**Gerar Diferença do Acerto de OC p/ Financeiro - GERDIFACOC:** Se estiver Desligado, o botão **"Gerar Diferença p/ o Financeiro"** não será habilitado e será possível fechar o caixa com diferença.

**Gerar Movimentação Bancária do Acerto de OC - GERMOVBANACER:** Se estiver Desligado o sistema não gerará a movimentação bancária quando clicar-se em [Fechar caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#fecharcaixa).

**Tipo de título dinheiro - TIPTITDINHEIRO:** Neste parâmetro, informe qual o código do Tipo de Título que representa Dinheiro, pois nos Acertos que tiverem esse tipo de título, o sistema totaliza o "Troco" dos títulos com uma fórmula (total em Cheque – total em Dinheiro), e o valor obtido é adicionado ao campo **"Valor Retornado"**.

**Ocultar Valor Retornado no Acerto - OCULVLRRETACER:** Quando acionado, a coluna **"Valor Retornado"** presente na aba [Resumo do Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#abaresumodoacerto) será ocultada.

**Exige conferência antes de fechar? - EXIGECONFCAIXA:** Se Ligado, força a conferência do caixa ao clicar em [Fechar caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#fecharcaixa).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607014-Acerto-de-Ordem-de-Carga#top)
