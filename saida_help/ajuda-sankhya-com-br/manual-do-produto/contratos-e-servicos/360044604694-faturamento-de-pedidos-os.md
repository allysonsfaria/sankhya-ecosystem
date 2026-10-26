---
id: "360044604694"
titulo: "Faturamento de Pedidos/OS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-09-25T16:55:08Z"
rotulos: ["Produtos", "Pedidos", "AJUDA DO SKW", "manual", "Faturamento", "Conclusão", "Conformidade", "Faturamento de Pedidos/OS", "Faturar", "Filtros Personalizados", "Medição", "Operação destino", "Serviços complementares", "br.com.sankhya.mgeos.faturamento.serv.avulsos", "Faturamento de Pedidos/OS manual", "Ordem de Serviço", "TOP", "Financeiro", "Faturamento de Pedidos/OS: Processo Flexível"]
---

# Faturamento de Pedidos/OS

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311225382039) Módulo: Comercial > Arquivo > Cadastros
```

---

Esta rotina está destinada ao Faturamento de Pedidos e Ordens de Serviço.

| [Filtros Personalizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#filtrospersonalizados) |  | [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#parmetros) |
| --- | --- | --- |
| [Tipos de Faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#tiposdefaturamento) |  | [Abas Conformidade e Serviços...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#abasconformidadeeservioscomplementares) |
| [Faturamento de Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#faturamentodepedidos) |  |  |

![Imagem 2: Faturamento de Pedidos](https://ajuda.sankhya.com.br/hc/article_attachments/360070947094)

## Filtros Personalizados

![Imagem 3: Filtros Personalizados](https://ajuda.sankhya.com.br/hc/article_attachments/360070947274)

Para faturar Pedidos nesta rotina, você deve, primeiramente, **"Filtrar"** os pedidos que deseja faturar. Assim como no [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654), o filtro poderá ser feito por **"Empresa"** e/ou **"Parceiro"**.

O campo **"Período"** trata-se de um filtro obrigatório, para que sejam apresentados na grade somente Pedidos/OS referentes à um determinado período.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#top)

## Parâmetros

![Imagem 4: Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/360072097013)

No campo **"Tipo de Operação** **destino"**, informe qual a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP) a ser utilizada para o faturamento.

Temos a possibilidade de escolher o Tipo de Negociação que será utilizado para faturamentos do tipo Parcelas do Financeiro, no campo **"Tipo de Negoc. p/ Faturamento 'Parcelas do Financeiro'"**.

**Observação:** caso não seja utilizado este tipo de Faturamento, o Tipo de Negociação utilizado será o mesmo do pedido de origem.

O campo **"Data para Faturamento"** é de preenchimento obrigatório e refere-se à data de Faturamento dos Pedidos.

**Importante:** não existe nenhuma tratativa ou parâmetro referente às datas retroativas que podem ser informadas neste campo. O sistema simplesmente fatura o pedido e seta a data de faturamento informada.

Informe no campo **"Série"** a Série que será utilizada referente à TOP de Faturamento, série esta, informada no **"Controle de Numeração"** da TOP.

Através da marcação **"Gerar 1 única Fatura** **(Medição)"**, você tem a possibilidade de faturar mais de um pedido, gerando uma única fatura.

**Nota:** este é o único tipo de faturamento em que é possível gerar uma única nota para todos os pedidos selecionados. Os outros tipos de faturamento, por terem ligação com o pedido de origem mais forte, por exemplo, pelas parcelas do financeiro, são necessários gerar uma nota para cada pedido faturado.

Caso você efetue a marcação Gerar 1 única Fatura (Medição) e selecione qualquer outro tipo de faturamento que não seja **"Horas de OS Executadas (Medição)"**, o sistema apresentará a seguinte mensagem:

**"'Gerar 1 única fatura (Medição)' só pode ser usado com 'Horas de OS Executadas (Medição)'".**

**Importante:** quando o parâmetro **"Usa processo de autorização de faturamento de OS? - UTILIZAAUTFATOS"** estiver ligado, o processo de Faturamento de OS e [Fechamento de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607034) passarão a necessitar de autorização para cada subitem que você desejar processar. Assim, os itens da OS para os quais forem autorizados o faturamento, serão exibidos aqui na tela Faturamento de Pedidos/OS para serem faturados; já os itens que não foram autorizados, não serão exibidos nesta rotina.

Caso a marcação **"Confirmar nota ao faturar"** seja realizada, a nota faturada será gerada já confirmada.

Quando o tipo de faturamento for **"Pelas parcelas do financeiro"** e a marcação **"Calcular Impostos Mensais ao faturar parcelas do Financeiro"** estiver efetuada, fará com que os impostos mensais sejam calculados durante a fatura e o valor será incluído na nota gerada, aso contrário, isto não será feito.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#top)

## Tipos de Faturamento

As **"OS Fechadas (Conclusão)"** são propostas com preço fechado, ou seja, independente de quantas horas forem utilizadas para executar o serviço, o preço para o cliente não irá mudar. Será apresentado para faturamento quando todos os itens da OS estiverem fechados.

O Tipo de Faturamento **"Horas de OS Executadas (Medição)"** é muito utilizado para venda de horas de serviço, onde fecha-se um pacote mas o faturamento ocorre de acordo com as horas que são gastas no fechamento de um período. Trouxemos um exemplo:

O cliente fecha um pacote de 500 horas. No primeiro mês de prestação de serviços (sendo neste exemplo fevereiro), são gastas 60 horas. No dia 05 do mês de março, o financeiro da empresa fatura às 60 horas executadas no mês anterior e encaminha a fatura para o cliente, de acordo com tempo que foi gasto no cliente dentro do mês.

Através do Tipo de Faturamento **"Pelas Parcelas do Financeiro"** um Pedido gera várias Notas no valor das parcelas negociadas, assim, será gerada uma nota de cada mês conforme valor negociado.

**Observação:** você deve se atentar para este caso pois, na tentativa de faturamento, não existindo estoque para o produto do Pedido de Venda, nenhuma mensagem será emitida, porém o faturamento não será realizado.

Em relação à **"Todas as parcelas do Financeiro (Total)"**, ela fara com que um Pedido gere apenas uma Nota, independente do número de parcelas negociadas. Neste caso, a Empresa poderá emitir vários boletos, totalizando o valor na Nota. Neste tipo de faturamento, o imposto é pago sobre o valor total.

**Nota:** utilizando os tipos de faturamento Pelas Parcelas do Financeiro e Todas as parcelas do Financeiro (Total), serão levados para a nota todos os produtos e serviços do pedido fechado. A diferença entre essas 2 opções é que, ao faturar por parcelas, o valor unitário de cada produto é proporcionalizado conforme o valor da parcela faturada, mantendo os mesmos produtos e sua quantidade original, não necessitando que haja vínculo com o apontamento de serviços na OS para que o faturamento seja realizado. 

O Tipo de Faturamento **"Horas de OS Executadas (Pedido a Pedido)"** é utilizado quando a TOP do pedido é por medição, ou seja, será faturado de acordo com a quantidade de horas executadas.

**Observação:** caso o Produto\Serviço esteja com o valor unitário zerado, ao efetuar o faturamento do Pedido\OS, com o Tipo de Faturamento igual à Horas de OS Executadas (Pedido a Pedido), o sistema emitirá a seguinte mensagem:

**"Não encontramos produtos. Cancelando a operação".**

Esta mensagem poderá ocorrer por outros motivos, além do citado acima:

- Produtos\Serviços sem preço de venda na tabela de preços;
- Produtos\Serviços vinculados à uma extensão de garantia;

**Nota:** em relação ao tipo Horas de OS Executadas (Medição), há um vínculo entre o serviço do Pedido e o serviço executado na OS, servindo de parâmetro para calcular as horas apontadas e aptas a serem faturadas. Nesse caso, o faturamento consumirá do pedido, o saldo referente aquele serviço apontado na OS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#top)

## Abas Conformidade e Serviços Complementares

Nestas abas serão apresentados os Pedidos/OS que estão dentro do que foi previsto; particularmente, na aba Serviços Complementares estarão as OS's que foram classificadas como **"Serviços Complementares"** em seu lançamento.

![Imagem 5: Nestas abas serão apresentados os Pedidos/OS que estão dentro do que foi previsto; particularmente, na aba Serviços…](https://ajuda.sankhya.com.br/hc/article_attachments/360070947574)

Temos também, as colunas a baixo que facilitam a análise da situação do cliente antes do faturamento. Utilizando estas colunas, você pode visualizar as pendências financeiras vencidas de um determinado parceiro, auxiliando na decisão de emissão de uma nota fiscal para ele ou não. As colunas são:

A **"Qtd. Fin. Vencidos"** apresenta a quantidade de títulos de receita, real e pendentes, com vencimento menor que a data atual que o Parceiro possui.

Na coluna **"Valor Fin. Vencidos"** será exibida a soma dos valores dos títulos que se encaixam no critério anterior. 

A coluna denominada **"Dias em Atraso"** mostrará a quantidade de dias em atraso do título de receita mais antigo e ainda não quitado do respectivo parceiro listado na grade. 

**Observação:** se não houver títulos vencidos do respectivo parceiro, a coluna Dias em Atraso exibirá o valor "0" (zero).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#top)

## Faturamento de Pedidos

Para realizar o Faturamento de Pedidos nesta rotina, você deve, primeiramente, **"Filtrar"** aqueles que deseja faturar. Assim como no [Faturamento de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604654), o filtro poderá ser feito por **"Empresa"** e/ou **"Parceiro"**.

As opções de **"Tipo de Faturamento"** complementam o filtro, permitindo a seleção dos pedidos que serão faturados:

![Imagem 6: As opções de "Tipo de Faturamento" complementam o filtro, permitindo a seleção dos pedidos que serão faturados:](https://ajuda.sankhya.com.br/hc/article_attachments/360070948574)

A seleção dos pedidos que serão faturados, ocorrerá segundo a classificação da TOP utilizada no lançamento do Pedido, ou seja, pode-se filtrar nesta tela os pedidos lançados com:

- TOP de Faturamento Total;
- TOP de Faturamento Parcelado;
- TOP de Conclusão do Serviço;
- TOP de Serviço Medição.

**Nota:** a funcionalidade do parâmetro **"Serviços complementares atualiza Qtd.Atendida? - SERCOMPLDEDQTA"** é fazer com que a coluna **"Quantidade Atendida"**, da tabela Compras e Vendas com vários Pedidos - TGFVAR fique com valor zerado quando a linha corresponder à itens de OS com classificação **"Conformidade"**. Tal parâmetro é do tipo lógico (ligado, desligado), e seu valor padrão é ligado. Caso o parâmetro esteja habilitado, a quantidade atendida receberá o valor correspondente ao tempo gasto no item da OS.

Se o parâmetro estiver desligado e na tela de Faturamento de Pedidos/OS existir um item de OS de Classificação Serviços Complementares, e o Tipo de Faturamento seja **"Horas de OS Executadas (Pedido a Pedido)"**, ao faturar, o sistema lançará na TGFVAR valores zerados para a coluna QTATENDIDA referente aos itens Serviços Complementares.

Após realizar os filtros necessários e clicar no botão ![Imagem 7: Após realizar os filtros necessários e clicar no botão , o sistema apresentará na grade inferior todos os Pedidos do…](https://ajuda.sankhya.com.br/hc/article_attachments/360070948834), o sistema apresentará na grade inferior todos os Pedidos do Parceiro ou Empresa lançados com a TOP selecionada no filtro, disponíveis para faturamento.

Neste momento, você poderá faturar todos os pedidos de uma só vez, segurando a tecla **"Ctrl"** do teclado e clicando no botão **"Faturar"**, ou pode selecionar os que deseja faturar, excluindo pelo botão ![Imagem 8: Neste momento, você poderá faturar todos os pedidos de uma só vez, segurando a tecla "Ctrl" do teclado e clicando no…](https://ajuda.sankhya.com.br/hc/article_attachments/360072099293) os que não serão faturados, ou ao contrário, selecionando os que não serão faturados e clicando no botão ![Imagem 9: Neste momento, você poderá faturar todos os pedidos de uma só vez, segurando a tecla "Ctrl" do teclado e clicando no…](https://ajuda.sankhya.com.br/hc/article_attachments/360072099233).

Esta tela apresenta na **"Grade Superior"** os Pedidos não faturados e na **"Grade inferior"** os itens das OS's ligadas ao pedido.

Com o(s) pedido(s) selecionado(s) e os filtros necessários realizados, clique no botão ![Imagem 10: Com o(s) pedido(s) selecionado(s) e os filtros necessários realizados, clique no botão .](https://ajuda.sankhya.com.br/hc/article_attachments/360072099333).

Feito isto, o sistema emitirá a seguinte mensagem:

**"Gerar faturas para CONFORMIDADE?".**

Ao clicar em **"Sim"**, será emitida uma nova mensagem de alerta, informando que o faturamento será realizado com a TOP de destino informada. Assim, clicando em **"OK"**, uma mensagem de confirmação do faturamento será emitida.

**![Imagem 11: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/20889961662359) Informações adicionais**

- O faturamento não poderá ser executado quando há valor de juros no cabeçalho da nota. Ao calcular a quantidade entregue, o valor adicional de juros no cabeçalho não é considerado nos itens, resultando em divergências nas quantidades no faturamento;
- As OS's marcadas como **"Não conformidade"** não serão Faturadas;
- Não se esqueça de efetuar as marcações **"Confirmar a nota ao faturar"** e **"Calcular impostos mensais ao faturar parcelas no financeiro"** se sua Empresa trabalhar com Outros Impostos;
- Há TOP's como as de **"Medição"** e **"OS Fechadas (conclusão)"** que dependem de OS para serem faturadas. Já o faturamento de serviço com as TOP's configuradas **"Pelas parcelas do financeiro"** ou **"Todas as parcelas do Financeiro (Total)"** independem de OS pois, o que é faturado é o pedido ou um financeiro do pedido.

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16036259255831) Acesse também:

[Usa processo de autorização de faturamento de OS?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602554)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604694-Faturamento-de-Pedidos-OS#top)
