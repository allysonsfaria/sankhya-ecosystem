---
id: "360045109173"
titulo: "Tipos de Negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:28:54Z"
rotulos: ["CORE_E02785", "AJUDA DO SKW", "manual", "Configuração", "Parceiro", "USACRPROJNATCAB", "TIPTABPRECOS", "Vencimento", "ORDENARABAS", "Parcelas", "Desconto máximo", "Boleta", "Desconto promocional", "DEVQTIPVENDA", "DIFCTIPNEGOC", "DIFVTIPNEGOC", "DTCALCVENC", "Função \"VALORIMPOSTO\"", "Lucro mínimo", "Prazo máximo", "Prazo médio", "Tabela financeira", "Taxa", "Tipo de Negociação", "USAPROCFORMPPG", "Valor Máximo e Mínimo", "br.com.sankhya.core.cad.tipo.negociacao", "Tipos de Negociação manual", "CORE_E04191", "Vendas", "Financeiro", "Tipos de Negociação", "RECPRECOTPV", "Cadastro Essencial", "Parametrização Importante", "FINARRPARCELAS", "Compras"]
---

# Tipos de Negociação

```
 Módulo: Comercial > Arquivo > Cadastros
```

---

Os Tipos de Negociação se referem às formas de pagamento utilizadas pela empresa, seja nas operações de Compra ou Venda. Nos Tipos de Negociação são realizadas diversas parametrizações que serão utilizadas nas negociações com os parceiros da empresa; portanto, tem-se aqui um cadastro de extrema importância.

| [Iniciando o cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#iniciandoocadastrodeumtipodenegociao) | [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) |
| --- | --- |
| [Aba Simulações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abasimulaes) | [Aba Bases para vencimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#ababasesparavencimento) |
| [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) | [Aba Taxas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais) |
| [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#parmetrosqueinfluenciamnestarotina) | [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#usodeprocedurenoclculodeparcelas) |
| [Observações sobre descontos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#observaessobredescontosdotipodenegociao) | [Regras para vinculo de Conta Bancária...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#regrasparavinculodecontabancriaoubanco) |
| [Uso de procedure no cálculo...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#usodeprocedurenoclculodeparcelas) |  |

![Imagem 1: Uso de procedure no cálculo...](https://ajuda.sankhya.com.br/hc/article_attachments/1500001442141)

## Iniciando o cadastro de um Tipo de Negociação

Para cadastrar um novo Tipo de Negociação, depois de clicar no botão de Inclusão de um novo registro ![Imagem 2: Para cadastrar um novo Tipo de Negociação , depois de clicar no botão de Inclusão de um novo registro "Cadastrar Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771570711) **"Cadastrar Tipo de Negociação"** ou utilizar a tecla **"F8"** do teclado, informe no campo **"Tipo de Negociação"** a numeração do cadastro em questão; através do botão **"Configuração da Tela"** localizado no lado superior direito da tela, pode-se determinar que a geração desta numeração se dará de maneira automática.

Feito isso, determine a **"Descrição"** do Tipo de Negociação, ou seja, a nomenclatura que melhor identificará a negociação nas rotinas em que ela for utilizada.

O campo **"Data e hora alteração"** será preenchido automaticamente pelo sistema e armazenará o dia e hora que o registro for cadastrado e/ou editado.

- **Observações sobre a atualização de "Data e hora alteração":**

  - A atualização deste campo (coluna `DHALTER`) segue regras específicas para garantir a integridade dos dados e evitar registros redundantes no banco de dados:
  - **Campos Históricos:** Ao alterar um campo histórico mais de uma vez no mesmo dia, o sistema só gerará uma nova linha com novo `DHALTER` se a linha atual já tiver sido utilizada em alguma operação (tabela `TGFCAB`). Caso contrário, o sistema manterá a linha existente, atualizando apenas o valor do campo, para evitar o acúmulo desnecessário de registros, considerando sempre a última alteração feita.
  - **Campos Não Históricos:** Nestes casos, o `DHALTER` não é alterado. Por se tratar de um campo chave, a mudança de data/hora de alteração poderia causar problemas de restrição de integridade em registros já relacionados em outras partes do sistema (como na `TGFCAB`).

**Nota:** Ao visualizar a lista de abas disponíveis desta tela através do ícone ![Tipneg3](https://ajuda.sankhya.com.br/hc/article_attachments/360061915033) localizado na lateral superior direita, pode-se fazê-lo de forma ordenada alfabeticamente; este comportamento é atribuído a ativação do parâmetro **"Ordenar abas por ordem alfabética? - ORDENARABAS"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Aba Características

Na Aba Características deverão ser determinadas as particularidades acerca de cada Tipo de Negociação. Veremos a seguir configurações essenciais para o perfeito funcionamento do Tipo de Negociação.

Quando a marcação **"Ativo"** está realizada, o Tipo de Negociação poderá ser utilizado nas novas inclusões nas Centrais; o oposto ocorre caso esteja desmarcado.

Um **"Subtipo"** é utilizado para definir a forma de pagamento que está sendo utilizada na operação realizada; é uma informação que depois de salva, não poderá ser modificada. Teremos as seguintes opções:

- Cartão de Débito;
- A vista;
- A prazo;
- Parcelada;
- Cheque pré-datado;
- Crediário;
- Financeira;
- Cartão de Crédito.

**Nota:** O subtipo Cartão de Crédito criticará um cliente em atraso, mas não impedirá a confirmação da Nota, pois considerará como uma venda garantida. O sistema se comportará da mesma forma com o subtipo A vista, contudo, para esse subtipo pode-se do utilizar o parâmetro **"Bloquear vendas a vista p/clientes em atraso? - BLOQVENDAVIST"** para impedir a confirmação da Nota para clientes que estejam em atraso.

**Observação:** A solicitação de liberação de limites a respeito do evento [3 - Limite de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#3-limitedecrdito) não ocorrerá quando:

- For utilizado um Tipo de Negociação com os subtipos A vista, Cartão de Crédito e Financeira;
- Parceiro utilizado no lançamento classificado como Consumidor Final ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), [Aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal), campo Classificação ICMS).

Através do campo **"Base de Prazo"** defina qual o prazo de carência para início da contagem do prazo para o vencimento no Tipo de Negociação em questão. Pode-se determiná-lo dentre as seguintes opções:

- **A partir do dia:** A partir do dia: O prazo começará a contar do próximo dia a venda. Vejamos um exemplo:

Se a venda foi dia 04/06/2019 e temos o prazo de 3 dias, logo, teremos vencimento dia 07/06/2019.

- **Fora a semana:** O prazo será contado a partir do primeiro dia da semana seguinte da data que foi efetuada a venda. Para que esta opção funcione, o prazo definido na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) deve ser diferente de zero.
- **Fora a dezena:** O prazo será contado a partir do primeiro dia da dezena seguinte da data que foi efetuada a venda. Este prazo é contado, fora a dezena em que o lançamento foi emitido.

Lançamentos do dia 1º ao dia 10 > Inicia-se o prazo no dia 11;

Lançamentos do dia 11 ao dia 20 > Inicia-se o prazo no dia 21.

- **Fora a quinzena:** O prazo será contado a partir do primeiro dia da quinzena seguinte da data que foi efetuada a venda. Este prazo é contado, fora a quinzena em que o lançamento foi emitido.

Lançamentos do dia 1º ao dia 15 > Inicia-se o prazo no dia 16;

Lançamentos do dia 16 ao dia 30 > Inicia-se o prazo no dia 01

- **Fora o mês:** O prazo será contado a partir do primeiro dia do mês seguinte à data que foi efetuada a venda. Este prazo é contado, fora o mês de emissão da nota. Dessa forma, todos os lançamentos realizados em Janeiro, (1º a 31), terão o vencimento do financeiro calculados a partir de 01/02, por exemplo.

Informe no campo **"Valor mínimo p/ venda"** o valor mínimo da negociação que será permitida na utilização deste Tipo de Negociação. A utilização deste campo pode ser vinculada ao evento [13 - Valor mínimo Tipo Negoc.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#13-valormnimotiponegoc.), ou seja, cadastre um Usuário Liberador e caso o valor determinado no campo não seja respeitado, tem-se a solicitação de liberação.

De forma inversa ao campo anterior, em **"Valor máximo p/ venda"** determina-se o valor máximo da venda que será permitida na utilização deste Tipo de Negociação. A utilização deste campo pode ser vinculada ao evento [14 - Valor máximo Tipo Negoc.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#14-valormximotiponegoc.), ou seja, cadastre um Usuário Liberador e caso o valor determinado no campo não seja respeitado, tem-se a solicitação de liberação.

De maneira análoga ao campo anterior, em **"Valor máximo p/ compra"** informe o valor máximo da compra que será permitida na utilização deste Tipo de Negociação. A utilização deste campo pode ser vinculada ao evento 14 - Valor máximo Tipo Negoc., ou seja, cadastra-se um Usuário Liberador e caso o valor determinado no campo não seja respeitado nas operações de compra, tem-se a solicitação de liberação.

Define-se o valor da **"Comissão"** a ser paga quando o Tipo de Negociação em questão for utilizado.

O campo **"Grupo de autorização"** permite que um Tipo de Negociação pertencente a um determinado grupo de autorização, possa ser utilizado apenas por parceiros que possuam o mesmo grupo de autorização. Um tipo de negociação só poderá pertencer a um grupo de autorização, enquanto que o mesmo parceiro pode pertencer a vários grupos de autorização. Poderão ser cadastrados até 10 (dez) grupos de autorização por parceiros. Por exemplo, se um tipo de negociação com 60 dias de prazo possui grupo de autorização A, esse tipo de negociação só pode ser utilizado por parceiros que também possuam o Grupo A. No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), esta informação é inserida no campo Grupo de autorização presente na [Aba Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacrdito).

**Nota:** Não possui validade no sistema, definir/informar um Grupo de autorização para os Tipos de Negociação utilizados nas operações de Compra, pois esta 'regra' será definida pelos próprios fornecedores e não pela empresa. Já no processo de Venda, é a Empresa que detém o poder de definir quem pode ou não utilizar o Tipo de Negociação. Por isso, este tipo de validação será feito pelo sistema apenas na Venda.

Efetuando-se a marcação **"Soma prazo de cliente"**, o sistema somará o prazo médio de pagamento em vendas, que é calculado no campo **"Prazo médio máximo"** também presente na aba Características, o Prazo médio pagamento definido na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abageral) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) e a **"Base de Prazo"** definida nesta aba.

A marcação **"Valida prazo de cliente"** quando realizada, bloqueia as vendas para o Parceiro quando o prazo médio calculado nos tipos de operação forem superiores aos valores definidos no Cadastro de Parceiros, aba Crédito, campo **"Prazo médio pagamento"**.

Ao efetuar a marcação **"Fixa vencimento"**, a Data de Vencimento inicial deverá ser digitada a cada nota para que os vencimentos posteriores sejam calculados considerando-se o mesmo dia. Exemplo: Uma venda no dia 1º com 30/60 dias de prazo resultará em dois títulos, um para dia 1º do mês seguinte e outro para o dia 1º do segundo mês. Com esta opção marcada, pode-se informar o dia 20 do mês seguinte para o primeiro pagamento, o segundo pagamento será calculado para o dia 20 do mês subsequente.

**Importante:** Caso você tenha realizado na aba Parcelas a configuração da coluna **"Fórmula"** considerando-se cálculos e valores de impostos, não será possível trabalhar com a funcionalidade da marcação Fixa Vencimento.

Caso uma nota seja duplicada ou tenha-se solicitado a opção de [Refazer o Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#refazerofinanceiro), e o Tipo de Negociação estiver marcado com a opção de Fixa Vencimento, será apresentado o pop-up também de nome Fixa Vencimento para inserção da nova data de vencimento. Na Central de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) ou de [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) será solicitada a data para compor o primeiro e os vencimentos das parcelas do financeiro.

**Importante:** Para apresentação do pop-up mencionado, é necessário que o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) esteja configurado para gerar financeiro (aba Geral, campo Financeiro), o Tipo de Negociação marcado para Fixar Vencimento e o parâmetro **"Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC"** esteja devidamente configurado.

Algumas considerações sobre o Tipo de Negociação que Fixa o Vencimento:

Nos Pedidos de Venda em que o Tipo de Operação-TOP esteja configurado com o campo **"Financeiro"** indicado com a opção **"Receitas"** e o campo **"Atualização do Financeiro"** marcado com a opção **"Provisionar"**, o faturamento ocorrerá normalmente, ou seja, será gerada a nota de venda e composto o vencimento que terá como base o pedido.

Se tratando de Pedidos de Venda que não atualizam o financeiro, ou seja, não provisionam, no ato do faturamento será visualizado no pop-up de faturamento um novo passo, onde trará o campo data de primeiro vencimento já preenchido de acordo com as configurações do Tipo de Negociação/Parceiro e esta data será utilizada para compor o vencimento da nota de venda.

Ao selecionar mais de um pedido para faturamento com parceiros diferentes, o sistema calculará as datas de vencimento e a data apresentada no pop-up de faturamento será a menor data de vencimento. Esta data pode ser modificada e todos os pedidos serão faturados com essa mesma data de vencimento fixa, sendo exibida a mensagem abaixo. Caso se necessite de datas fixas de vencimento diferentes para cada pedido, se faz necessário faturar pedido a pedido.

**"Foram selecionados para faturamento mais que um pedido que exige data fixa de vencimento. A menor data para primeiro vencimento entre os pedidos é a data sugerida neste passo. A Data Fixa para vencimento informada acima será utilizada para TODOS os pedidos selecionados para faturamento."**

Selecionando mais de um pedido para faturamento e o Tipo de Operação-TOP de venda selecionada não atualize o financeiro, será exibida a seguinte mensagem:

**"Há um ou mais pedidos em faturamento que não provisionam financeiro e cujo tipo de negociação possui configuração para data de vencimento fixa. Contudo a TOP escolhida para faturamento não gera financeiros."**

Ainda sobre o Cálculo do Vencimento, este é obtido pela **"Data Base"** associado ao **"Prazo da Parcela"**. Se Pedido de Compra ou Pedido de Venda e/ou Nota de Compra e Nota de Venda, e o parâmetro DTCALCVENC configurado como **"Dt. Faturamento"**, será utilizada a Data do Faturamento para cálculo do vencimento. Se este mesmo parâmetro estiver configurado como **"Dt. Negociação"**, o sistema utilizará a Data de Negociação para cálculo do vencimento.

**Observação:** O parâmetro **"Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra? - FORCDTFATCOMPRA"** quando habilitado, o sistema irá considerar a data de faturamento como base para calcular o vencimento nas compras. Deste modo, o parâmetro **"Data Base p/ Cálculo do Vencimento no Faturamento - DTCALCVENC"** não será aplicado.

Com a opção **"Pode ser usado por consumidor"** marcada, o Tipo de Negociação poderá ser utilizado nos lançamentos para Parceiros classificados como Consumidor Final ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) > [Aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal) > campo Classificação ICMS). Ao lançar uma Nota de venda com um Tipo de Negociação que esteja com esta opção desmarcada, se o Parceiro da nota estiver configurado como Consumidor Final, será apresentada uma mensagem de alerta na confirmação da nota alertando que Tipo de Negociação não pode ser usado por Consumidor Final.

A **"Tabela de preço"** poderá ser informada, se o parâmetro **"Tabela de Preços por - TIPTABPRECOS"** estiver definido com a opção Tipo de Negociação. Informa-se uma [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854) neste campo, de modo que ao utilize o Tipo de Negociação em questão, os produtos inseridos na nota, irão obter os preços cadastrados nesta tabela.

Configura-se o campo **"Imprimir Pix/Boleto/Duplicata?"** de acordo com a necessidade de impressão deste tipo de documento, quando o Tipo de Negociação correspondente for utilizado. Teremos as seguintes opções de definição deste campo:

- Manual;
- Na confirmação;
- Proibido.

**Observação:** O sistema não gera boletos para títulos com Data de Vencimento igual a Data de Negociação, por esta ser uma característica de vendas A vista.

Informe no campo **"Tabela financeira"** a Tabela de Financiamento que será utilizada durante a simulação e/ou efetivação de um financiamento.

Para inserir uma **"Observação padrão"**, é fundamental cadastrá-la previamente na tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474). Esta funcionalidade permite a criação de observações que podem ser impressas nas Notas Fiscais. No entanto, para que essas observações sejam exibidas no documento, é necessário que o [modelo de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido) esteja customizado para incluir esse campo. Exemplo de Observação Padrão: **"Não aceitamos devolução de mercadorias"**.

Vale ressaltar que não há um mecanismo padrão que replique a Observação padrão do Tipo de Negociação para a observação do cabeçalho da nota, ou seja, essa informação não será automaticamente transferida para o cabeçalho da nota.

O prazo inserido no campo **"Prazo médio máximo"** é a definição do prazo médio máximo para o Tipo de Negociação, de modo que nas vendas não seja permitido alterar os vencimentos resultando em um prazo médio maior que o estipulado. Exemplo: Tendo-se um Tipo de Negociação 30/60/90 dias, seu prazo médio será 60 (30+60+90/3); informando um prazo médio máximo de 60, ao tentar aumentar o prazo nas Centrais o sistema não permitirá e será aberta a tela de solicitação de liberação para o evento [5 - Prazo Médio Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#5-prazomdiomximo).

No campo **"Prazo máximo"** determina-se um prazo máximo em dias para realização de vendas utilizando o Tipo de Negociação. Caso o prazo seja ultrapassado, o sistema barra a venda e solicita liberação para o evento [6 - Prazo Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#6-prazomximo).

Informe no campo **"% Lucro mínimo"** um percentual de lucro mínimo a ser obtido para que a venda possa ser feita. Se na realização da venda, o lucro for inferior ao definido nesse campo, será solicitada a liberação de limites para o evento [19 - Lucro mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#19-lucromnimo).

O campo **"% MC Mínima"** indica o percentual mínimo permitido de margem de contribuição que a negociação deve contemplar. Esta configuração está relacionada à liberação de limites do evento [48 - Margem de Contribuição Mínima](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#48-margemdecontribuiomnima); este evento será solicitado na confirmação da nota/pedido quando a negociação não atender o percentual mínimo configurado no Tipo de Negociação utilizado.

Determine no campo **"Fórmula desc. máximo"** o código da fórmula para validação de desconto máximo nas vendas no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas). A informação aqui inserida, deve ser previamente cadastrada na tela [Fórmulas para Desconto Máximo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600314).

De forma similar ao campo anterior, tem-se em **"Fórmula desc. máximo itens"** o código da fórmula para validação de desconto máximo, por itens dentro da nota, nas vendas realizadas no Portal de Vendas. A informação aqui inserida, também deve ser previamente cadastrada através da tela Fórmulas para Desconto Máximo.

O **"Desconto Promocional"** inserido neste campo será utilizado no lançamento de descontos promocionais nas vendas feitas pelo Portal de Vendas; o desconto aqui inserido é primeiramente cadastrado na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034). O campo pode ser definido dentre sete opções, a saber:

- **Considerar Maior:** Por meio desta opção, o sistema irá considerar o maior desconto entre o Desconto Promocional e o Desconto no Tipo de Negociação. Lembrando que, caso exista desconto promocional eles só serão considerados quando o parâmetro **"Usar o maior desconto promocional? - USAMAIDESCPROMO"** estiver ligado.
- **Não considerar:** Por esta opção, não será considerado o Desconto promocional.
- **Considerar sempre:** Através desta opção, sempre será considerado o Desconto Promocional; caso o mesmo não esteja configurado será levado em consideração o Desconto no Tipo de Negociação.
- **Somar os dois:** Por esta opção, tem-se um desconto somando o valor do Desconto Promocional ao valor do Tipo de negociação.
- **Limitante:** Esta opção é utilizada para que o sistema considere o desconto promocional quando se tratar de uma bonificação.
- **Considerar por Qtde Somando:** Através desta opção, o sistema irá considerar o desconto dado no desconto promocional por quantidade, para produtos que tenham promoção configurada por quantidade. Para os produtos que não tenham desconto por quantidade, será considerado o desconto inserido no campo % desconto Máximo do Tipo de Negociação.
- **Considerar por Qtde/Desconto:** Por meio desta opção, tem-se o seguinte comportamento:

Produtos com desconto promocional por quantidade, usarão o desconto por quantidade;

Produtos com desconto promocional normal, utilizarão o desconto promocional normal;

Produtos com Desconto Máximo igual a 0 (zero), sempre irão utilizar o **"% Desconto Máximo"** do Tipo de Negociação.

![Imagem 4: Sobre Descontos Promocionais por Quantidade : quando o campo "Tipo da taxa" é configurado como Juro taxa única ou…](https://ajuda.sankhya.com.br/hc/article_attachments/34431940193303) Sobre **Descontos Promocionais por Quantidade**: quando o campo **"Tipo da taxa"** é configurado como **Juro taxa única** ou **Desconto** e o campo **"Desconto Promocional"** como **Considerar por Qtde Somando** ou **Considerar por Qtde/Desconto**, o sistema não aplica o desconto promocional sobre o valor já acrescido da taxa de negociação. Nesse cenário, o valor promocional do produto será o que foi registrado no cadastro do desconto promocional, sem a soma da taxa.

#### Observações Importantes:

- A regra para o cálculo de Desconto no Tipo de Negociação, seguirá a seguinte ordem:

1º - Desconto da Taxa Especial por produto;

2º - Desconto da Taxa Especial por grupo de produto;

3º - Desconto do tipo de negociação no campo Taxa em %.

- A validação de desconto do Tipo de Negociação é feita com base na nota inteira e não por item a item. Além disso, definindo o campo por esta opção, o sistema levará o desconto para a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), destacado na nota. Quando o Desconto Promocional for destacado na nota, dependendo do preço do produto, poderá existir diferença no valor calculado. Isso ocorre porque o percentual utiliza duas casas decimais e o cálculo pode não resultar em um valor exato.
- O sistema analisa o percentual de desconto do Tipo de Negociação, e caso ele seja maior do que o **"% Desconto máximo"** do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), ele irá substituir pelo que está configurado no produto. Se o campo referente ao **"% Desconto máximo"** do produto não possuir informações, o sistema considerará como "0" (zero), levando então, somente o % de desconto correspondente ao desconto promocional.

Deve-se inserir no campo **"% Desconto máximo"** o percentual de desconto máximo para este Tipo de Negociação. Se o percentual informado na central for maior que o deste campo, o sistema validará de acordo com o parâmetro **"Valida desconto máximo - VALDESCMAX"**, podendo ou não avisar e aceitar a venda, sendo necessária sua liberação por meio do evento [25 - Desconto por item da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota).

**Nota:** O parâmetro **"Valida desconto máx do tipo de negoc.? - DESCMAXTPN"** se ligado, faz com que o sistema solicite a liberação do evento 1 – Desconto tipo negociação caso o valor de desconto do produto seja maior que o configurado no Tipo de Negociação utilizado na venda. Se desligado não deve solicitar a liberação desse evento.

**Importante:** Os Percentuais de Desconto são lançados nas Centrais respeitando os percentuais máximos de desconto dos produtos. Isso significa que se um produto tiver um desconto promocional superior ao máximo, informado em seu cadastro, o sistema lançará o percentual até o limite.

No campo **"Taxa em %"** informe o percentual da taxa (juros ou desconto) que será utilizado para este Tipo de Negociação. Esta taxa será utilizada quando não existirem lançamentos na aba [Taxas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais).

Determina-se no campo **"Tipo da taxa"**, qual será a forma de aplicação da taxa (juros ou desconto) sobre o valor informado no campo Taxa em %. Pode-se defini-lo dentre as seguintes opções:

- **Juro taxa Única:** A taxa será cobrada como juros quando utilizado este Tipo de Negociação;
- **Desconto:** A taxa será dada como desconto na utilização deste Tipo de Negociação.

**Observação:** Quando o parâmetro **"Aplicar taxa de juros após desconto promocional? - JURPOSDESCPROMO"** estiver habilitado, o desconto promocional será aplicado e posteriormente o sistema calculará a taxa de juros do tipo de negociação. Caso esteja desabilitado, o sistema irá calcular a taxa de juros do tipo de negociação e em seguida efetuar o desconto promocional.

Seguindo a definição do campo anterior, no campo **"Apresentação da taxa"** defina-se como a taxa será exibida na nota. Teremos as seguintes alternativas:

- **Incluir no preço do produto:** A taxa será incluída no preço do produto;
- **Destacar na nota fiscal (valor sugerido):** A taxa será destacada na nota fiscal.

**Observação:** Não será possível realizar esta operação quando o parâmetro **"Taxa de boleto no total da nota? - TAXBOLNOT"** estiver ligado.

O sistema permite a combinação da opção Incluir no preço do produto, com a opção Somar os dois referente ao campo **"Desconto Promocional"**.

Quando o campo Apresentação da taxa for definido com a opção Incluir no preço do produto, o campo Desconto Promocional for definido como Somar os dois e na tela [Cadastro de Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034) for dado um desconto em valor, o sistema irá embutir o Desconto Promocional no preço do produto, levando-o para a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), reduzido.

**Nota:** Quando o Tipo de Negociação estiver com o campo **"Desconto Promocional"** configurado com a opção **"Considerar por Qtde Somando"**, o campo **"Tipo da taxa"** selecionado com a opção **"Juro taxa única"** e a **"Apresentação da taxa"** com a opção **"Incluir no preço do produto"**, ao lançar os itens nas Centrais, será aplicada a taxa configurada no valor unitário dos produtos configurados no [Desconto Promocional por Quantidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025241874).

Além das configurações acima, os parâmetros abaixo deverão encontrar-se da seguinte forma:

**Tabela de preço c/base no desconto por quantidade - CONSTABDESCQTD** = desligado
**Aplicar taxa de juros após desconto promocional? - JURPOSDESCPROMO** = ligado
**Desc. promo. 'Considerar Sempre' com preço cheio?** - **DESCPROMCSPRECO** = desligado

Através dos campos **"Conta contábil 1"** e **"Conta contábil 2"** pode-se vincular o Tipo de Negociação às contas contábeis desejadas.

**Observação:** Ao pesquisar as contas contábeis 1 e 2 para preenchimento, sendo esta pesquisa feita pelo campo Conta contábil,será necessário a digitação do ponto (.) entre os números da conta para realizar a pesquisa. Exemplo: 1.2.3. Esta medida é necessária pois podem existir planos de contas de várias empresas e cada um com uma máscara.

O campo **"% Mín. entrada"** é utilizado para inserção de um percentual mínimo de entrada que deverá ser dado sobre a nota.

No campo **"Prazo máx. 1ª parcela"** deve-se inserir a quantidade máxima de dias para o pagamento da primeira parcela.

O campo **"Número de parcelas"** é destinado a inclusão do número de parcelas da correspondentes à negociação.

**Observação:** quando o campo Número de Parcelas está preenchido com um valor maior que zero o sistema não processa devoluções para lançamentos de vendas. Caso haja tentativa, será apresentada a seguinte mensagem de aviso:

**"O Sistema não está preparado para gerar financeiro para o tipo de negociação que possui o campo número de parcelas diferente de zero e tipo de movimento (TIPMOV) diferente de "P" ou "V'"."**

A marcação **"Usar Créd.Flex"** quando realizada, indica que o Tipo de Negociação em questão será utilizado no processo de [Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603054).

O campo **"Prazo mínimo"** é aplicado a todas as negociações, exceto para a negociação do tipo A vista. Neste campo, deve-se inserir um valor numérico que corresponde à quantidade mínima de dias que poderão ser concedidos para prazo de pagamento. O prazo de pagamento da(s) parcela(s) é especificado na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas), através do campo **"Prazo"**.

**Observação:** A tela de cadastro de Tipos de Negociação em si, não faz a validação se o prazo de vencimento da(s) parcela(s) é inferior ao prazo mínimo estipulado através do campo Prazo mínimo. Essa validação ocorre no lançamento de pedidos ou notas de Compra. Sendo assim, na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), no lançamento de um pedido/nota, utilizando-se um Tipo de Negociação que contenha a configuração descrita, o sistema exige a liberação para o evento [4 - Prazo Mínimo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#4-prazomnimo) correspondente ao prazo.

O campo **"Taxa Mensal da Administradora"** é de uso específico de um Parceiro Sankhya.

Ao efetuar a marcação **"Vencimento pré-fixado no pedido"**, os vencimentos das parcelas correspondentes aos pedidos de Compra ou Venda, serão copiados para as parcelas das notas geradas pelo faturamento. Se o procedimento de [Refazer o Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#refazerofinanceiro) for executado em um documento que já foi faturado, os vencimentos serão recalculados com base nas configurações das parcelas, no Tipo de Negociação e nos dados do documento selecionado.

**Observação:** dado que uma nota tenha sido gerada a partir de um pedido com o Tipo de Negociação configurado com a marcação acima, a data de vencimento da nota será a mesma do pedido que a originou.

Caso o parâmetro **"Recalcular venc. títulos na aprovação (Sefaz)? - RECALVENCAPROV"** esteja ativado, será possível recalcular o vencimento dos financeiros de títulos que possuam o tipo de movimento Venda, antes que estes tenham seu lote enviado para aprovação na SEFAZ; o Tipo de Negociação utilizado no lançamento do título em questão, deve estar com opção Vencimento pré-fixado no pedido desmarcada.

Quando se tratar do lançamento de um pedido/nota de venda que contenha parcelamento, caso a divisão das parcelas apresente uma sobra, a pratica normal do mercado é sempre jogar o arredondamento para a última parcela. Sendo que, algumas administradoras de crédito não trabalham desta forma, jogando assim o arredondamento para a primeira parcela. Deste modo, ao utilizar a marcação **"Ajusta arredondamento na 1ª parcela"** que quando acionada efetuará o arredondamento desta sobra na 1ª parcela. Caso a marcação esteja desabilitada, o arredondamento será efetuado na última parcela.

**Nota:** Esta marcação propicia uma maior precisão na conciliação das transações, pelo fato de realizar a eliminação das diferenças de centavos.

**Truncar valores no parcelamento:** Esta marcação quando habilitada, faz com que o sistema realize uma operação de **"Truncate"** (corte) no valor da parcela após realizar a divisão. Se estiver desligada, o sistema efetuará um **"Round"** (arredondamento) no valor da parcela. Vejamos um exemplo:

O valor de R$ 8.77 em 8x é igual 8.77 / 8 = 1.09625;

Com a marcação acionada, a parcela será 1.10 e o parcelamento ficará 1.10, 1.10, 1.10, 1.10, 1.10, 1.10, 1.10, 1.07;

Se estiver desligada, a parcela ficará em 1.09 e o parcelamento será 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.14.

**Observação:** Esta marcação trabalhará juntamente com a marcação Ajusta arredondamento na 1ª parcela. Desta forma, será possível escolher 4 tipos diferentes de configurações:

1.Arredondar jogando a diferença na última parcela;

2.Arredondar jogando a diferença na primeira parcela;

3.Cortar jogando a diferença na última parcela;

4.Cortar jogando a diferença na primeira parcela.

#### Seção Integrar EConect

Marcando-se a opção **"Integrar com Econect"**, tem-se que o Tipo de Negociação em questão realizará integração com o EConect.

A **"Forma Recebto"** é uma informação de preenchimento obrigatório, e realizará o DE-PARA das formas de recebimento existentes no sistema da SOCIN com o Sankhya-Om.

**Observações:**

- Para cupons que existem mais uma forma de pagamento, deve-se cadastrar o tipo de negociação **"MISTO"** e no campo Forma Recebto informe **"-1"** para que o sistema reconheça esta situação no momento da importação.
- Para os tipos de negociação utilizados em cliente e convênio, o campo **"Subtipo"** deverá ser diferente de **"Cartão de Crédito"**. Como sugestão, deverá ser cadastrado como **"A prazo"** ou **"Parcelado"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Aba Simulações

Esta aba é apresentada para utilização, caso o parâmetro **"Simula formas de pagamento na Central? - USASIMFORMAPGTO"** esteja habilitado.

![Imagem 5: Esta aba é apresentada para utilização, caso o parâmetro "Simula formas de pagamento na Central? - USASIMFORMAPGTO"…](https://ajuda.sankhya.com.br/hc/article_attachments/360073688894)

Efetuando a marcação **"Disponível para simulação?"**, tem-se o Tipo de Negociação em questão, disponível para uso na opção [Formas de Pagamento <Ctrl+Shift+F4>](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#formasdepagamentoctrlshiftf4) presente no [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) da Central de Vendas.

Tem-se no campo **"Taxa de Juros em simulações"** o percentual de juros cobrados nas parcelas de uma negociação do tipo Parcelada.

No campo **"Tipo de juros em simulações"** será determinado a forma com que os juros serão calculados; teremos duas opções para definição deste campo:

- Composto;
- Simples.

Ao marcar a opção **"Permite edição simulação pgto"** será possível editar as formas de pagamento, quando na utilização da opção Formas de Pagamento <Ctrl+Shift+F4>, acessada pelo Botão Outras Opções da Central de Vendas.

Na simulação do cálculo, o sistema irá calcular a taxa e os dias de atraso entre a data da negociação e a data inserida no vencimento. Acerca desse cálculo, observe os exemplos abaixo:

- Se você não utilizar a taxa de juro mensal o cálculo a ser realizado será:

```
 ValorJuros = valor * taxa / 100
```

- Caso a taxa de juro mensal for utilizada junto aos juros compostos, o sistema efetuará o cálculo:

```
 ValorJuros = (Math.pow(1 + (txDiaria * 30 / 100), diasDeAtraso / 30) * valor) - valor
```

- Porém, no caso de utilizar a taxa de juro mensal e juros simples, o cálculo a ser feito será:

```
 ValorJuros = valor * txDiaria * diasDeAtraso / 100
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Aba Bases para vencimento

Através da aba Bases para vencimento, efetue as configurações para que o cálculo das Datas de vencimento dos títulos, seja feito considerando períodos e datas previamente definidos. Serão geradas automaticamente as parcelas no financeiro dos títulos, em função dos períodos e datas aqui configurados.

![Imagem 6: Através da aba Bases para vencimento , efetue as configurações para que o cálculo das Datas de vencimento dos títulos,…](https://ajuda.sankhya.com.br/hc/article_attachments/360073689974)

**Sequência:** Corresponde ao encadeamento das datas de venda e vencimento a serem inseridas.

**Dia inicial da venda:** Dia inicial do período em que a venda acontece.

**Dia final da venda:** Dia final do período em que a venda acontece.

**Dia do vencimento:** Este será o dia gerado como base do vencimento.

**Mês de vencimento:** Corresponde ao mês da data a ser gerada como base do vencimento. Neste campo tem-se as seguintes opções:

- Mês atual;
- 1º mês subsequente;
- 2º mês subsequente;
- 3º mês subsequente;
- 4º mês subsequente;
- 5º mês subsequente;
- 6º mês subsequente.

Para utilização das Bases de Vencimento no Tipo de Negociação, tem-se algumas regras (os campos citados abaixo se encontram na aba Características). A saber:

**Subtipo:** Quando o Subtipo é **"A vista"** esta funcionalidade não tem efeito. Não é possível criar base de vencimento para Tipos de negociação A vista.

**Base de prazo:** Quando houver Base para vencimento vigente, será desconsiderado.

**Soma prazo de cliente:** Existindo Base para vencimento vigente, será desconsiderado.

**Fixa vencimento:** Quando houver Base para vencimento vigente, será desconsiderado. Além disso, o pop-up correspondente a Data Base não será apresentado.

**Prazo (PPG):** Quando existir Base para vencimento vigente, os prazos serão sempre mensais, deste modo, haverá uma conta para determinar o intervalo de meses.

**Base de prazo (PPG):** Havendo Base para vencimento vigente, será desconsiderado.

**Vencimento fixo (PPG):** Se existir Base para vencimento vigente, será desconsiderado.

**Soma prazo cliente (PPG):** Quando houver Base para vencimento vigente, será desconsiderado

**Observações:**

- Ao cadastrar um sequenciamento de bases de vencimento, o Dia final de venda de uma linha não pode ser igual ao Dia inicial de venda da linha seguinte. Caso seja feita a tentativa de confirmação de um cadastro nessas condições, será apresentada a seguinte mensagem de aviso:

**"A data inicial já está em um intervalo cadastrado."**

- Na tentativa de cadastro do Mês de vencimento definido como Mês atual e o Dia de vencimento anterior ao Dia final de venda, será exibida a seguinte mensagem de aviso:

**"Para vencimentos dentro do próprio mês o dia de vencimento deve ser posterior ao dia final de venda."**

Este cadastro será possível (Dia de vencimento anterior ao Dia final de venda) caso o Mês de vencimento seja definido com uma opção diferente de Mês atual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Aba Parcelas

A aba Parcelas é responsável por agrupar as particularidades acerca do parcelamento que será realizado quando na utilização do Tipo de Negociação. A configuração realizada nesta aba, irá refletir diretamente no Financeiro dos documentos lançados nas Centrais.

![Imagem 7: A aba Parcelas é responsável por agrupar as particularidades acerca do parcelamento que será realizado quando na…](https://ajuda.sankhya.com.br/hc/article_attachments/360073690034)

Inicialmente, para geração das parcelas, são necessários três preenchimentos. A saber:

- Determine no campo **"Prazo para entrada"**, o número de dias para o cálculo da 1ª parcela;
- Em **"Prazo entre as Parcelas"**, informe o número de dias entre as parcelas;
- No campo **"Quantidade de parcelas"** determina-se o número de parcelas que deverão ser geradas.

Feito isso, clique no botão ![Imagem 8: Feito isso, clique no botão "Calcular Parcelas" para que o sistema construa as parcelas segundo os dados digitados nos…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771580311) **"Calcular Parcelas"** para que o sistema construa as parcelas segundo os dados digitados nos campos acima.

**Observação:** caso o parâmetro **"Arredondar percentual parcela p/7 casas decimais - DECPERCPARC7"** esteja habilitado, e o usuário clique em Calcular Parcelas o cálculo do percentual de cada parcela será feito considerando 7 casas decimais. Dessa forma, o percentual é melhor distribuido quando se tem muitas parcelas e consequentemente o residuo será um valor menor.

![Imagem 9: O botão Calcular Parcelas não é compatível com os tipos de negociação que tenham os subtipos "A vista" e "A prazo" . O…](https://ajuda.sankhya.com.br/hc/article_attachments/26098486496919) O botão Calcular Parcelas não é compatível com os tipos de negociação que tenham os subtipos **"A vista"** e **"A prazo"**. O sistema considera esses subtipos como pagamentos únicos, desativando a função de cálculo automático de parcelas (mesmo que seja possível realizar a inclusão de parcelas nos subtipos citados).

Além dessa maneira, pode-se utilizar dos botões ![Imagem 10: Além dessa maneira, pode-se utilizar dos botões Incluir , "Duplicar" e "Excluir" para realização dos ajustes desejados…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771570711) Incluir, ![Imagem 11: Além dessa maneira, pode-se utilizar dos botões Incluir , "Duplicar" e "Excluir" para realização dos ajustes desejados…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771584023) **"Duplicar"** e ![Imagem 12: Além dessa maneira, pode-se utilizar dos botões Incluir , "Duplicar" e "Excluir" para realização dos ajustes desejados…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771586199) **"Excluir"** para realização dos ajustes desejados nas parcelas.

Vejamos sobre as demais configurações presentes na aba:

De acordo com o determinado no campo **"Opção de digitação"**, será possível digitar os campos do financeiro da nota. Tem-se as seguintes opções:

- Digitar Somente Valor;
- Digitar Prazo e Valor;
- Digitar Somente Data;
- Digitar Data e Valor;
- Não Digita;
- Digitar Somente Prazo.

Determina-se no campo **"Prazo"** o período em dias entre a Data de Negociação e o Vencimento. Exemplo, 30 dias na primeira parcela e 60 dias na segunda parcela.

Será informado o **"Percentual"** correspondente à parcela que será paga no prazo. O somatório deste campo nas diversas parcelas deve resultar em 100 (cem).

Selecione o **"Banco"** para o lançamento das parcelas. Esta informação deve ter relação com a Conta Bancária a ser preenchida posteriormente nesta mesma aba.

No campo **"Centro Resultado Padrão"** informa-se o Centro de Resultado para análises gerenciais; a informação aqui vinculada, será apresentada  no campo Centro de Resultado da aba Financeiro na Central - Compras | Vendas | Mov. Internas, quando um lançamento for realizado utilizando-se este Tipo de Negociação.

Na **"Natureza Padrão"** seleciona-se a natureza a ser utilizada nas futuras análises gerenciais; a opção aqui escolhida, será apresentada no campo Natureza na aba Financeiro na Central - Compras | Vendas | Mov. Internas, quando um lançamento for realizado utilizando este Tipo de Negociação.

---

![Imagem 13: Informações adicionais sobre os campos Centro Resultado Padrão , Natureza Padrão e Projeto :](https://ajuda.sankhya.com.br/hc/article_attachments/20168207679511) **Informações adicionais sobre os campos Centro Resultado Padrão, Natureza Padrão e Projeto**:

- Se houver Centro Resultado Padrão, Natureza Padrão  e/ou **"Projeto"** informados na parcela, estes serão utilizados; caso contrário, o sistema irá utilizar o **"Centro Resultado**", **"Natureza"** e **"Projeto"** da nota, porém, quando o parâmetro **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"** estiver ativado, os campos Centro Resultado, Projeto e Natureza do cabeçalho da nota que serão considerados na geração do movimento financeiro.
- Além disso, pode-se ainda, informar no parâmetro **"Considerar CR/Proj/Nat da parcela p/tipo de título - CRPRONATPARCTIT"** o Tipo de Título configurado na aba Parcela do Tipo de Negociação do título para a geração e, caso não tenha essa informação, o sistema irá verificar a definição do parâmetro USACRPROJNATCAB.

---

Determine o **"Tipo de Título"** que será utilizado no Tipo de Negociação (cheque, duplicata, boleto, etc); é importante que esta informação tenha relação com Tipo de Negociação, por exemplo, um Tipo de Título Dinheiro é apropriado que seja utilizado juntamente a um Tipo de Negociação A vista.

Informe a **"Conta bancária"** que será apresentada no Financeiro das Centrais, e que consequentemente estará vinculada ao lançamento.

**Observação:** No cadastro de Tipos de Negociação, mesmo que o [Banco](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894-Bancos) não seja informado na configuração das parcelas, e a respectiva [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) esteja com as marcações Ativa, Exclusiva da empresa e Emite realizadas (abas [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros) e [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), respectivamente), quando for feita a busca do banco para geração do financeiro de um pedido, o sistema irá analisar se dentre as contas exclusivas da empresa, existe ao menos uma com a marcação Conta padrão para emissão efetuada (aba Boleto(s)/Duplicatas); caso exista, esta será utilizada no financeiro, caso contrário, dentre as contas exclusivas, será utilizada a de menor código.

O campo **"Tipo de Empresa"** é utilizado para informar ao sistema de que campo ele deverá buscar o código da empresa a ser gerado no Financeiro. Tem-se as seguintes opções:

- **C - Constante -** Informada no campo Empresa presente nesta aba;
- **E - Empresa -** Código da Empresa informado no cabeçalho da Nota;
- **N - Negociação -** Código da Empresa de Negociação informado no cabeçalho da Nota;
- **X - Constante exclusiva -** Código da Empresa informado no cabeçalho da Nota.

Determina-se a **"Empresa"** que será apresentada no Financeiro da nota de acordo com a configuração realizada no campo anterior.

No campo **"Tipo Parceiro"** informe qual o campo o sistema deverá se basear para apresentar o Parceiro no Financeiro da nota. Assim, teremos as seguintes alternativas:

- **T - Transportadora** - O parceiro gerado no Financeiro, será o Parceiro Transportadora da nota;
- **V - Vendedor** - O Vendedor da nota será inserido como Parceiro no Financeiro do documento;
- **X - Constante Exclusiva** - Código do Parceiro informado na aba Parcelas. Caso não seja informado um parceiro será apresentado a seguinte mensagem: 
  **"Ao escolher o Tipo de Parceiro X - Constante Exclusiva, é necessário definir um parceiro diferente de 0 - Sem Parceiro."**
- **D - Digita** - Esta opção permite lançar uma nota e indicar o financeiro para um Parceiro diferente, informando-o manualmente;
- **N - Nota** - O parceiro do Financeiro gerado será o mesmo informado no cabeçalho da nota;
- **C - Constante** - Será o parceiro informado no campo Parceiro presente nesta aba, porém caso não seja informado considera o parceiro da nota.

Informe o Parceiro que será apresentado no Financeiro da nota de acordo com a configuração realizada no campo anterior.

O campo **"Fórmula"** é destinado a alguma configuração detalhada a respeito das parcelas no financeiro; trabalha-se aqui, com variáveis e expressões que irão gerar valores específicos no financeiro. Vejamos alguns exemplos de expressões que podem ser utilizadas:

CHEQUE (VLRNOTA + VLROUTROS);

TROCO (VLROUTROS \* -1);

VLRFRETEEXTRA (valor do frete quando este é extra nota);

VLREMBEXTRA (valor da embalagem quando o tipo é extra nota);

BRANCO (VLRNOTA);

VLRNOTA, VLRFRETE, VLRDESC, VLROUTROS, VLRDESTAQUE, VLRJURO, VLRISS, VLRSEG, VLRIRF, VLRVENDOR, VLREMB (qualquer um dos campos de valor do cabeçalho da nota).

**Observação:** deverá ser utilizado, para fórmula no Tipo de Negociação, um valor diferente de 0 (zero) para que a movimentação seja atualizada antes de confirmar a nota.

A função VALORIMPOSTO é utilizada para buscar informações da tela de outros impostos, caso o produto esteja configurado para tal. Esta função acrescentará ao valor do financeiro mais uma parcela com a informação do imposto. A função possui a seguinte sintaxe:

Valorimposto (X,'Y'),

em que X é o código do imposto utilizado na nota; Y pode ser 'A', para alíquota do imposto, ou 'B', para base do valor do imposto, ou ainda 'V' para valor do imposto.

Vejamos um exemplo abaixo de um Tipo de Negociação contendo 06 parcelas, sendo que uma parcela é para um Parceiro da Nota e o restante para o Parceiro Constante, como uma administradora do cartão de crédito. Usando apenas percentuais, devido aos financeiros serem de parceiros diferentes, esta configuração não é possível. Com isso, foram realizadas configurações do campo Fórmula das parcelas. A aba Parcelas ficou da seguinte forma:

![Tipneg9](https://ajuda.sankhya.com.br/hc/article_attachments/360061915053)

Com isso, gerando uma nota de R$130,00, o financeiro irá ficar no seguinte formato:

![Tipneg10](https://ajuda.sankhya.com.br/hc/article_attachments/360060987254)

Neste caso, utilizando apenas percentuais, o sistema gera um financeiro com o total da nota para o parceiro da nota e 5 parcelas para a administradora do cartão totalizando o valor da nota.

**Importante:** Ao faturar um Pedido de Venda, sendo utilizado neste um Tipo de Negociação com fórmula, as parcelas uma vez calculadas pela fórmula não devem ser alteradas para respeitar sua integridade, pois mesmo que a soma do total das parcelas fique equivalente ao realizado pela fórmula, as parcelas perdem sua real origem; caso seja feita a utilização do Tipo de Negociação após este tipo de modificação, será apresentada a seguinte mensagem:

**"Parcela calculada pela fórmula não pode ter seu valor alterado."**

Neste caso, se for necessário modificar as parcelas, o Tipo de Negociação utilizado não deve possuir Fórmula configurada.

Marcando a opção **"Baixa na Confirmação"** será aberta a tela de Baixa no ato da Confirmação da Nota; é uma configuração utilizada para Tipo de Negociação A Vista. Tem-se a opção de na realização da baixa na confirmação da nota, configure o sistema de modo que o questionamento sobre o desejo de realizar ou não a baixa, não seja efetuado; para isso, teremos o parâmetro **"Baixar título na central sem perguntar? - BXARTITSEMPERG"**, que ao ser ativado, e a marcação **"Baixa na Confirmação"** estiver realizada, nenhuma tela para confirmação da baixa será apresentada, a baixa do título é diretamente realizada na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

**Nota:** Para que a tela de baixa seja apresentada, se faz necessário configurar na rotina de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) a liberação das opção de **"Baixa"** para a tela de Movimentação Financeira.

**Importante:** A baixa realizada pelo sistema quando efetuada a marcação Baixa na Confirmação, acontece apenas quando é feita a confirmação manual dos documentos, ou seja, através do botão [Confirmar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#confirmar) presente na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

**Observações:**

- Ao utilizar esta forma de baixa, não será solicitado nenhum tipo de impressão pelo sistema;
- Caso na tentativa de aprovação de uma NF-e (com baixa automática do respectivo título), ocorram falhas de comunicação por questões de timeout ou mesmo de configurações equivocadas, será exibida a seguinte mensagem e não ocorrerá a baixa do título:

**"Ocorreu um erro na baixa automática: O financeiro está vinculado a uma NF-e não autorizada pela Sefaz, portanto não é possível baixá-lo. Aprove a nota e realize a baixa manualmente."**

A aba Parcelas conta também com um recurso que possibilita o cálculo do vencimento de cada uma das parcelas separadamente; em casos onde tem-se a programação de impostos e retenções, estas parcelas poderão possuir bases de vencimento diferenciadas das bases comuns para os títulos ligados diretamente às notas, sendo viável e favorável a realização deste tipo de configuração. Para realização deste procedimento, tem-se os seguintes campos:

Defina no campo **"Base do prazo"** qual o prazo de carência para início da contagem do prazo para o vencimento nesta parcela. São apresentadas as seguintes opções de escolha:

- **Usar do Tipo de Negociação:** Ao realizar esta marcação, serão utilizadas as informações de base do prazo e soma prazo de cliente, realizadas na aba Características para o cálculo das parcelas;
- **A partir do dia:** O prazo será contado a partir do dia da negociação;
- **Fora a semana:** O prazo será calculado a partir do primeiro dia da semana seguinte da data da negociação. O campo "Prazo" apresentado mais acima na tela, deve ser definido diferente de zero;
- **Fora a dezena:** O prazo será calculado a partir do primeiro dia da dezena seguinte da data da negociação;
- **Fora a quinzena:** O prazo será calculado a partir do primeiro dia da quinzena seguinte da data da negociação;
- **Fora o mês:** O prazo será calculado a partir do primeiro dia do mês seguinte da data da negociação;
- **Quinzena/Fim mês:** Quando o vencimento da parcela for entre o primeiro dia do mês e o dia 15, ajusta-se o vencimento para o último dia do mês. Quando for posterior ao dia 15, transfere-se para o dia 15 do mês seguinte. Por exemplo:

Vencimento        >        Vencimento ajustado

15/02/2017        >        28/02/2017 (fim do mês)

16/08/2017        >        15/09/2017 (dia 15 do mês seguinte)

A data informada no campo **"Vencto Fixo"**, será usada como a data de vencimento em todas as notas que forem lançadas utilizando o tipo de negociação configurado, desconsiderando assim as configurações para cálculo do vencimento.

É importante destacar que a data informada no campo Vencto Fixo não será considerada quando o **"Subtipo"** configurado na aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) for **"A vista"**, pois, nesse caso, o vencimento será definido conforme a natureza da negociação.

---

**![Imagem 16: Informações adicionais sobre o campo Vencto Fixo](https://ajuda.sankhya.com.br/hc/article_attachments/20168207679511) Informações adicionais sobre o campo Vencto Fixo**

Em Notas de Complemento, ao utilizar um tipo de negociação com vencimento fixo, o sistema recalculará todos os financeiros com base na data configurada, mesmo que o vencimento gerado seja anterior à data atual. Garantindo, desse modo, que todos os valores sejam ajustados corretamente.

Já em Notas de Devolução, caso o tipo de negociação utilize vencimento fixo e os financeiros copiados estejam vencidos, o sistema ajustará o vencimento somando a diferença em dias entre a data de emissão da nota de origem e a data atual ao vencimento original. Considere o seguinte exemplo:

**Nota de Venda:**

- Data de emissão: 01/12
- Tipo de negociação com vencimento fixo: 02/12

**Nota de Devolução:**

- Data de emissão: 10/12
- Diferença entre a data atual e a nota de origem: 9 dias
- Novo vencimento calculado: **02/12 + 9 dias = 11/12**

---

Em relação ao campo **"Vencimento não útil"**, ele define o "destino" da data de vencimento em casos onde esta tenha sido calculada para dias não úteis. São possíveis as seguintes marcações:

- **Vencimento Original:** Mantém o vencimento atual e só irá postergá-lo para o próximo dia útil, caso o parâmetro **"Transfere vencimento quando fim de semana/feriado - TRANSFVENC"** esteja habilitado;
- **Antecipa vencimento se dia não útil:** Caso o vencimento caia em um dia não útil (sábado, domingo ou feriado), este deverá ser antecipado para o primeiro dia útil anterior ao vencimento;
- **Posterga vencimento se dia não útil:** Caso o vencimento cair em um dia não útil (sábado, domingo ou feriado), este deverá ser postergado para o primeiro dia útil posterior ao vencimento.

Ao efetuar a marcação **"Usar Dt. Entrada/Saída para vencimento da GNRE?"**, o vencimento utilizado na parcela correspondente à GNRE ST no financeiro será o mesmo informado no campo **"Dt. Entrada/Saída"** localizado no cabeçalho da nota Central de Venda.

**Importante:** essa marcação é especificamente para GNRE ST. Para maiores informações acesse o artigo [Melhores Práticas para Configuração e Cálculo do Garantido Integral (GNRE - Compra)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580314-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-Garantido-Integral-GNRE-Compra).

Caso a marcação **"Soma Prazo de Cliente"** esteja realizada, o sistema irá somar o prazo médio de pagamento em vendas, que é calculado no campo Prazo desta aba, o campo Prazo médio pagamento definido na [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abageral) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) e a Base do Prazo definida nesta aba.

**Observação:** ao **"Duplicar"** um cadastro, o registro copiado deve ser confirmado para que seja possível acrescentar as parcelas, que também são copiadas do registro original.

O parâmetro **"Manter dia útil na data de vcto em título avista? - MTDIADTITLAVI"** que por padrão é apresentado ativado, tem como função manter a data de vencimento dos títulos á vista para o próximo dia útil quando se tratar de finais de semana ou feirados. A partir do momento em que o parâmetro é desligado, as próximas notas de vendas lançadas com tipo de negociação á vista e baixa automática, terão a sua data de vencimento alterada para a data do dia em que forem faturadas.

Efetuando-se a marcação **"Parcela exclusiva FCP-ST"** serão geradas duas guias de GNRE, uma para ICMS-ST e outra para FCP-ST, desde que na tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados), aba **"Geral"**, os campos **"Código da Receita (GNRE) p/ FCP ST" e "Tipo de Título p/ indicar GNRE p/ FCP S.T."** também encontrem-se devidamente preenchidos.

**Observação:** Caso os campos não estejam preenchidos, será gerada apenas uma guia de GNRE com o ICMS ST e FCP ST somados.

No campo **"Tipo de Financeiro (REC/DESP)"** temos as opções **"T - Usar da TOP"** e **"N - Usar da Natureza Padrão"**.

**Nota:** Este campo possibilitará que você adicione financeiros oriundos da Central de Notas, com o tipo de receita/despesa diferente da configurada na TOP.

Para isto, na tela [Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774), defina em uma natureza o campo **"Tipo de Natureza"**; após, na tela Tipos de Negociação, aba Parcelas, defina no campo **"Natureza Padrão"** a natureza configurada e selecione uma das opções no campo Tipo de Financeiro.

**Observação:** Caso não seja definida uma opção, o sistema utilizará o financeiro configurado na TOP.

**Nota:** Quando o Tipo de Negociação é parcelado, todas as parcelas poderão utilizar o campo Tipo de Financeiro (REC/DESP) com a opção N - Usar da Natureza Padrão e o mesmo será apresentado na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Aba Taxas Especiais

Para usar as taxas especiais, o campo Apresentação da taxa deve estar configurado com a opção **"Incluir no preço do produto"** e o Tipo da taxa deve ser **"Juro taxa única"** ou **"Desconto"**; ambos os campos se encontram na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas).

![Imagem 17: Para usar as taxas especiais, o campo Apresentação da taxa deve estar configurado com a opção "Incluir no preço do…](https://ajuda.sankhya.com.br/hc/article_attachments/360074855733)

Pode-se criar Taxas Especiais para [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) e/ou [Grupos de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os) específicos que irão seguir as configurações adotadas, sendo que o produto terá prioridade sobre o grupo, ou seja, existindo a taxa no produto, esta será utilizada; se não existir, usará a taxa do grupo de produtos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Botões do topo da tela

Na parte superior da tela, teremos o botão ![Imagem 18: Na parte superior da tela, teremos o botão "Sankhya Place" , em que, ao clicar neste, o sistema o redirecionará para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16694798742679) **"Sankhya Place"**, em que, ao clicar neste, o sistema o redirecionará para a tela Sankhya Place, em que exibirá conteúdos e soluções referentes ao conteúdo em que a tela estará inserido.

Tem-se também o botão  ![Imagem 19: Tem-se também o botão "Edição múltipla" que permite a edição simultânea de vários registros a partir do modo grade. Ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16694771593751) **"Edição múltipla"** que permite a edição simultânea de vários registros a partir do modo grade. Ou seja, ao selecionar um conjunto de registros e clicar no botão, será possível editar os campos correspondentes de todos os registros de uma só vez. 

Por exemplo, com os cadastros em modo grade na tela Tipos de Negociação selecione-os e em seguida clique no botão Edição múltipla, assim os campos de todas as abas poderão ser editados simultaneamente para os tipos de negociação selecionados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Parâmetros que influenciam nesta rotina

O parâmetro **"Tabela de Preços por - TIPTABPRECOS"**, quando configurado como Tipo de Negoc./Vendedor ou Parceiro/Tipo de Negoc./Vendedor, habilitará nesta rotina a aba **"Vendedor/Tabela"**, através da qual vincula-se o vendedor à Tabela de Preço.

**Observação:** Caso não sejam feitas estas configurações na aba Vendedor/Tabela, ao tentar inserir um produto na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), o sistema mostrará o mesmo com o valor zero e, quando houver a confirmação da nota, a seguinte mensagem será exibida:

**"Preço não encontrado para este Vendedor/Tipo de Negociação."**

**Nota:** Quando um vendedor está inativo, ele não aparece na pesquisa.

Se o parâmetro **"Tabela de Preços por: - TIPTABPRECOS"** estiver definido com a opção **"Tipo de Negociação"** ou **"Tipo de Negoc./Vendedor"**, o sistema irá recalcular os valores do lançamento em relação a taxa do tipo de negociação, independente da configuração realizada no parâmetro **"Recalcula preços quando altera Tipo de Negociação: - RECPRECOTPV"**.

**Observação:** O parâmetro RECPRECOTPV não é considerado quando um dos dois Tipos de negociação (antigo ou o novo) contém taxa, pois é necessário considerar a taxa para compor o valor.

Durante os processos de faturamento e devolução, pode ser necessário que a empresa agrupe as notas independente do Tipo de Negociação utilizado nestes documentos. Para definição deste processo, tem-se a influência de três parâmetros. A saber:

- **Em Devoluções Aceitar Qualquer Tipo de Negociação? - DEVQTIPVENDA:** Utilizado para Devoluções de Compra e Devoluções de Venda.
- **Agrupar Tipo Negoc.diferentes na Central Clientes? - DIFVTIPNEGOC:** Usa-se este parâmetro para Pedidos e Notas de Venda.
- **Agrupar Tipo Negoc.diferentes na Central Fornec.? - DIFCTIPNEGOC:** A ativação deste parâmetro, irá impactar nos Pedidos e Notas de Compra.

**Observação:** Com o parâmetro RECPRECOTPV configurado com a opção **"Sempre"** e o campo **"Tipo da Taxa"** selecionado com a opção **"Juro taxa Única"**, ao realizar a troca do Tipo de Negociação em um lançamento em moeda, tanto no tipo de título anterior quanto no novo o sistema irá realizar o recálculo dos valores zerando o desconto da moeda.

**Importante:** Em um faturamento agrupado de notas, o sistema gera uma única nota assumindo o Tipo de Negociação da nota com menor nunota (número único).

Quando o parâmetro **"Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT"** está ligado, ele tenta passar o vencimento para um dia útil quando ele cair em um dia não útil; assim, quando o parâmetro **"Posterga vencimento com dia fixo (CALDIAFIXOVCT)? - POSVENCDIAFIX"** também estiver ligado, ao tentar passar o vencimento fixo para um dia útil, o sistema irá observar um período menor que 30 dias entre as parcelas, passando o vencimento para o próximo mês subsequente. Já com o parâmetro de chave POSVENCDIAFIX desligado, o vencimento não será postergado, mesmo que o período entre as parcelas seja menor que 30 dias, ou seja, para que o sistema mantenha o vencimento fixo e só altere o vencimento para um dia útil quando o dia fixo cair em um dia não útil, o parâmetro POSVENCDIAFIX deve estar desligado.

Por padrão, o parâmetro **"Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT"**estará ligado para que não haja o acúmulo de vencimentos. Sendo assim, caso você queira que o sistema realize esse acúmulo, basta desativar o parâmetro. Porém, é importante saber que, quando os parâmetros **"Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT"** e Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT estiverem ligados e houver mais de uma parcela com a mesma **"Base do Prazo"**, a base do vencimento será o valor do campo **"DTPRAZO"** (tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)) do financeiro gerado anteriormente.
E se o parâmetro USARDIAFIXOVCT estiver ligado e o ACVENDIAFIXOVCT desligado, a base do vencimento será a mesma para todas as parcelas.

O parâmetro **Arredonda parcelas do financeiro na alteração do item? - FINARRPARCELAS**, quando ligado, garantirá o arredondamento das parcelas financeiras da nota quando houver modificação na quantidade do item.

O parâmetro **Manter o desconto ao mudar tipo de negociação ? - FSMANTERDESCPOM** não tem funcionalidade no **Sankhya Om**.

Quando o parâmetro **"Utilizar conta bancária do pedido? - USACONTAPEDIDO"** estiver ativado, e todas as informações financeiras do pedido forem da mesma conta bancária, essa conta será copiada automaticamente para a nota na hora do faturamento.

Já, o parâmetro **TAXBOLNOT** usa os dados financeiros com conta para incluir o valor da **taxa de boleto** no total da nota, respeitando a configuração do campo **"Proibir impressão boleto?"** no [tipo de título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494).

Por isso, **não é recomendado usar os dois parâmetros ao mesmo tempo**. Mas, se for necessário, certifique-se de marcar o campo **"Proibir impressão boleto?"** nos tipos de título que não geram boleto, assim a taxa será incluída apenas quando realmente for necessário

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Observações sobre descontos do Tipo de Negociação

- Se todos os prazos forem iguais a zero (0), o prazo será determinado na venda. Se apenas o primeiro for igual a zero, a primeira parcela será considerada como entrada.
- Se na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) o campo Apresentação da Taxa estiver definido como **"Incluir no preço do produto"**, o campo Tipo da taxa estiver determinado como **"Desconto"** e na [Aba Taxas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais)constar o registro de alguma taxa, ao incluir o item na nota, o preço deste já é apresentado considerando o desconto desta aba. A taxa de desconto não é apresentada na Nota.
- Caso na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) o campo Apresentação da Taxa esteja definido como **"Destacar na nota fiscal"**, o campo Tipo da taxa esteja determinado como **"Desconto"**, na [Aba Taxas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais) exista alguma taxa e o parâmetro **"Aceita desconto por Produto/Serviço - DESCPRO"** esteja **"Ligado"**, ao incluir o Item na Nota, o preço do produto é apresentado sem alterações e o campo **"% desc"** do item virá preenchido com percentual de desconto da Aba Taxas Especiais, considerando que o [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-) tenha o campo Digitação na nota presente na aba Venda, não definido como Valor.
- Se na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) o campo Apresentação da Taxa estiver definido como **"Destacar na nota fiscal"**, o no campo Tipo da taxa estiver definido como **"Desconto"**, o parâmetro **"Aceita desconto por Produto/Serviço - DESCPRO"** estiver **"Desligado"**, o sistema pegará o desconto informado no campo **"Taxa em %"** também presente na Aba Características e apresentará no pé da nota.
- Se na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), o campo % Desconto Máximo estiver preenchido, na [Aba Taxas Especiais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abataxasespeciais) também possuir uma taxa informada, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Vendas, o campo % Desconto Máximo também possuir um valor, o sistema dará prioridade à taxa inserida na Aba Taxas Especiais.
- Se o campo Tipo da taxa presente na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) estiver definido como **"Desconto"**, e o campo Apresentação da Taxa também presente nesta aba, estiver determinado como **"Incluir no preço do produto"**, será embutida a taxa no preço.
- Caso o campo Apresentação da Taxa presente na [Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) esteja marcado como **"Destacar na nota fiscal"** e o parâmetro **"Aceita desconto por Produto/Serviço - DESCPRO"** esteja **"Ligado"**, o desconto será destacado no item; se o campo Apresentação da Taxa estiver determinado como **"Incluir no preço do produto"** e o campo Tipo da taxa estiver definido como **"Juro taxa única"**, o preço será embutido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Regras para vínculo de Conta Bancária ou Banco

É possível vincular um [Banco](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598894-Bancos) ou [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas):

- À Parceiros;
- Ao Tipo de Negociação;
- À conta padrão para emissão de boletos;
- À Empresa.

Esta configuração influencia na geração do financeiro da nota e na emissão de boletos. Tem-se a seguinte regra:

- Se for informada Conta Bancária na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) do Tipo de Negociação, será utilizada a Conta e o Banco das parcelas;
- Caso o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) tenha conta bancária informada em seu cadastro ([Aba Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao)), esta juntamente com o Banco serão utilizados;
- Caso seja informado apenas o Banco na Aba Parcelas do Tipo de Negociação, é utilizada a Conta Padrão para emissão de boletos (Cadastro de Contas Bancárias, aba Boleto(s)/Duplicatas);
- Caso a situação no item anterior não ocorra, será utilizada a Conta assinalada como Exclusiva da empresa (Cadastro de Contas Bancárias, aba Cadastros). A conta definida como exclusiva, deve possuir a mesma marcação de emissão de boletos que o Tipo de Negociação ([Aba Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), campo Imprimir Pix/Boleto/Duplicata?), ou seja, se o Tipo de Negociação emite boleto, a conta deve emitir; se o Tipo de Negociação não emite boleto, a conta não deve emitir;
- O sistema sempre considerará a Empresa do financeiro, ou seja, a que está configurada na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) do Tipo de Negociação;
- Quando é encontrada mais de uma conta para o mesmo banco, porém esta não foi encontrada pelos meios convencionais (marcação Exclusiva da empresa etc), o sistema priorizará uma conta da empresa utilizada na nota, ou seja, que esteja configurada no Tipo de Negociação, utilizando a mesma. Exemplo, no Tipo de Negociação, o campo Tipo de Empresa presente na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) está configurado como **"E - Empresa"**, deste modo, o sistema pegará a empresa da nota e a busca da conta levará essa configuração em consideração.

**Observação:** Na impressão das boletos o sistema busca o tipo de impressora que inserido no [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025236514-Contas); na aba Boleto(s)/Duplicatas informa-se o **"Tipo impressora"**, e no campo **"Modelo"** informa-se o modelo TXT que será utilizado na impressão.

Observação: caso houver uma renegociação, será utilizada a **"Conta"** informada no parâmetro **"Conta Padrão para Financeiro - CONTAPADRAOFIN"**. Se não houver conta informada neste parâmetro, será usada a conta referente ao primeiro financeiro escolhido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

## Uso de procedure no cálculo de parcelas

##### Nota: Para que a procedure seja acionada no cálculo das parcelas, é necessário informar ''PROCEDURE'' na aba ''Parcelas'' do Tipo de Negociação. Caso contrário, o sistema não executará a `STP_AVALIA_FORM_PPG`, mesmo com o parâmetro ativado.

O parâmetro **"Usar procedure como fórmula para parcelas do Tip. Negociação - USAPROCFORMPPG"** quando ativado, faz com que o sistema trabalhe com as fórmulas de parcela financeira utilizando a stored procedure STP\_AVALIA\_FORM\_PPG, ou seja, de acordo com a quantidade de parcelas definidas na [Aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) do Tipo de Negociação, o sistema calcula o valor de cada parcela com base nas fórmula definidas na procedure.

Vejamos um exemplo:

CREATE OR REPLACE PROCEDURE STP\_AVALIA\_FORM\_PPG ( P\_NUNOTA IN INT, P\_CODTIPVENDA IN INT, P\_SEQPPG IN INT, P\_RESULT OUT FLOAT)

AS

BEGIN

     P\_RESULT := NULL;

     BEGIN

           IF P\_CODTIPVENDA = 23 THEN

               SELECT VLRNOTA + VLROUTROS INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

           ELSIF P\_CODTIPVENDA IN(26,30,41,56,313) THEN

               IF P\_SEQPPG IN(2,3) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/3)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/3) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA IN(36,45) THEN

               IF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/2) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 2 THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/2)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA IN(38,57) THEN

               IF P\_SEQPPG IN(2,3,4) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/4)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/4) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA = 40 THEN

               IF P\_SEQPPG IN(2,3,4,5) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/5)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/5) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA = 42 THEN

               IF P\_SEQPPG IN(2,3,4,5,6,7) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/7)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/7) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA = 47 THEN

               IF P\_SEQPPG IN(2,3,4,5) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/5)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/5) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           ELSIF P\_CODTIPVENDA = 64 THEN

               IF P\_SEQPPG IN(2,3,4,5,6,7,8,9,10) THEN

                   SELECT (VLRNOTA - VLRSUBST - ((VLRNOTA - VLRSUBST)/10)) INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               ELSIF P\_SEQPPG = 1 THEN

                   SELECT ((VLRNOTA - VLRSUBST)/10) + VLRSUBST INTO P\_RESULT FROM TGFCAB WHERE NUNOTA = P\_NUNOTA;

               END IF;

           END IF;

     EXCEPTION

           WHEN NO\_DATA\_FOUND THEN

                P\_RESULT := NULL;

           WHEN OTHERS THEN

                P\_RESULT := NULL;

     END;

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top)

Acesse também:

[Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494)

[Contas Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)

[Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites)

[Contabilização de Financeiros com Ajuste ao Valor Presente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734)
