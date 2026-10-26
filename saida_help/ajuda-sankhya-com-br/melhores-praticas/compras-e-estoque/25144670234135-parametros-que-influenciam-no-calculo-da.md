---
id: "25144670234135"
titulo: "Parâmetros que influenciam no cálculo da Data de Vencimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25144670234135-Par%C3%A2metros-que-influenciam-no-c%C3%A1lculo-da-Data-de-Vencimento"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-07-22T14:46:03Z"
rotulos: ["Configuração", "Movimentação Financeira", "Parâmetros", "Preferências", "Financeiro", "Parâmetros que influenciam no cálculo da Data de Vencimento"]
---

# Parâmetros que influenciam no cálculo da Data de Vencimento

Ao realizar algum lançamento na central que inclua financeiro e a data de vencimento calculada pelo sistema está errada, necessário revisar não só o cadastro do tipo de negociação e suas parcelas, mas também todos os parâmetros que influenciam seu cálculo.

Na tela **"Preferências"**(Caminho: Configurações » Avançado » Preferências), verifique os parâmetros abaixo:

(1)** TRANSFVENC** - Transfere vencimento quando fim de semana/feriado

Se estiver "Sim", fará com que títulos que tenham vencimento em feriados ou dias não úteis tenham seu vencimento alterado para o próximo dia útil.

**(1)** **DTCALCVENC** - Data Base p/ Calculo do Vencimento no Faturamento

Neste parâmetro o usuário deverá informar a data base que será utilizada para calcular o vencimento dos títulos gerados no financeiro da nota, se negociação ou faturamento. O sistema pega o prazo do tipo de negociação e acresce na data base para formar o vencimento. Se o parâmetro estiver igual a 'Faturamento' e a data de faturamento for informada no pedido de compra, ao faturar este pedido, aparecerá uma caixa de diálogo onde o usuário deverá informar a nova data de faturamento. Se a data for maior que a indicada no pedido ou vazia, o sistema irá recalcular o vencimento do financeiro de acordo com esta data, sendo que quando estiver vazia, o sistema usará para data de faturamento a data atual. Quando o parâmetro estiver pela data de faturamento, se a data informada estiver diferente da data do servidor, o sistema irá criticar e emitirá a mensagem "Existe Faturamento posterior a esta data".

Caso o parâmetro esteja configurado para "Data de Saída", o sistema irá calcular a data base de vencimento a partir da data informada no campo "Data de Ent./Saída", do cabeçalho da nota/pedido. E se estiver configurado como "Negociação" irá calcular a data base de vencimento a partir da data informada no campo Dt. Negociação do cabeçalho do lançamento.

(1)** HABTIPALTDTVENC** - Usa Tipo de alterao da Data de Vencimento(TOP)

Este parâmetro funciona em conjunto com a configuração da TOP **"Tipo de Alteração da Data de Vencimento"** presente na aba **"Financeiro"**. No caso de um Faturamento não ser na mesma data que o pedido, se configurar neste campo da TOP a opção "Manter", o sistema mantém a data de vencimento do pedido e acrescenta o número de dias entre a emissão do pedido e a emissão da nota. Além disso, no Faturamento só será respeitado o valor informado neste campo se o parâmetro "Usa Tipo de Alteração da Data de Vencimento (TOP) - **HABTIPALTDTVENC**" estiver ligado. Caso o parâmetro esteja desligado, independente do que for definido no campo, o sistema terá o comportamento equivalente à opção Manter.

**Observação:** a opção 'Manter', tem o objetivo de quando alterar no documento a data que corresponde ao configurado no parâmetro DTCALCVENC, não serão recalculados os vencimentos financeiros.

**(1)** **RECALVENCFAT** - Recalcular vencimento dos títulos no faturamento?

No processo de faturamento, caso este parâmetro esteja ativado, o vencimento dos financeiros dos títulos serão recalculado. Este comportamento ocorrerá nos seguintes casos:

Se o título possuir apenas uma parcela e a data de vencimento desta for menor que a data atual (data do faturamento), seu vencimento será recalculado;
Caso o título possua duas ou mais parcelas e a data destas parcelas seja menor que a data atual (data do faturamento), será feito a agrupamento em uma única parcela e seu correspondente vencimento recalculado.
**Observação:** se a data de vencimento calculada coincidir com a data de alguma parcela já existente, estas parcelas serão agrupadas. Além disso, os impostos da nota serão recalculados, exceto os que foram digitados, estes serão excluídos.

(1)** TIPALTDTVENCCEN** - Tipo alterao da Data Vencimento(TOP) na Central.

Se o parâmetro estiver habilitado, o sistema irá manter a data de vencimento após sua alteração. Caso desligado, o recálculo será realizado conforme a data definida no parâmetro **DTCALCVENC**.

**(1)USARDIAFIXOVCT** - Utiliza regra de vencimento para dias fixos?

Quando ligado, habilitará na aba "**Crédito"** do cadastro de parceiros o quadrante de informações complementares **'Dias Fixos para Pagamento'**, contendo seis campos onde o usuário poderá cadastrar números inteiros.

**Observação:** no help '[Seção Dias fixos para pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#Se%C3%A7%C3%A3oDiasfixosparapagamento)' temos um exemplo do funcionamento dos campos deste quadrante caso configurado.

(1)** CALDIAFIXOVCT**  - Altera cálculo de vencimento para dias fixos?

Este parâmetro possibilita que o cálculo do vencimento seja alterado para dias fixos conforme cadastrado no parceiro. Ele trabalha em conjunto com o parâmetro "**USARDIAFIXOVCT**", então para que o sistema valide a Seção de Dias Fixos para pagamento é necessário que ambos estejam ligados.

**(1)POSVENCDIAFIX** - Posterga vencimento com dia fixo (CALDIAFIXOVCT)?

Quando o parâmetro "Utiliza regra de vencimento para dias fixos? - **USARDIAFIXOVCT**" está ligado, ele tenta passar o vencimento para um dia útil quando ele cair em um dia não útil; assim, quando o parâmetro **POSVENCDIAFIX** também estiver ligado, ao tentar passar o vencimento fixo para um dia útil, o sistema irá observar um período menor que 30 dias entre as parcelas, passando o vencimento para o próximo mês subsequente. Já com o parâmetro de chave **POSVENCDIAFIX** desligado, o vencimento não será postergado, mesmo que o período entre as parcelas seja menor que 30 dias, ou seja, para que o sistema mantenha o vencimento fixo e só altere o vencimento para um dia útil quando o dia fixo cair em um dia não útil, o parâmetro **POSVENCDIAFIX** deve estar desligado.

(1)** MTDTVENAPRZO** - Manter venc. na cópia financeiros do faturamento?

Quando ligado o sistema mantém a data de vencimento ao realizar a cópia de financeiros no faturamento. Quando desligado o vencimento será recalculado.

**Observação:** para tratar o vencimento do novo financeiro de acordo com o pedido, é necessário que o sistema esteja tratando uma nota por pedido, seja uma nota a ser faturada de cada parceiro ou que a opção de **"Uma nota para cada"** esteja marcada.

**(1)** **FORCDTFATCOMPRA** - Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra?

Quando habilitado, o sistema irá considerar a data de faturamento como base para calcular o vencimento nas compras. Deste modo, o parâmetro "Data Base p/ Cálculo do Vencimento no Faturamento - **DTCALCVENC**" não será aplicado.

(1)** DIASMAXPRAZEXTR** - Dias máximo prazo extra dia fixo para vencimento

Este parâmetro tem a função de informar o número máximo de dias extras permitido para chegar ao dia de vencimento. Caso esse número de dias seja extrapolado, o vencimento deverá ser retroagido par o mês anterior.

Segue abaixo um exemplo:

![Imagem 1: Segue abaixo um exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/25159122952599)

**(1)ACVENDIAFIXOVCT** - Acumula vencimento para dias fixos?

Quando ativado, o sistema não permitirá que haja o acúmulo de vencimentos. Dessa forma, caso queira que o sistema realize esse acúmulo, basta desativá-lo.
**Observação:** é importante saber que, quando ambos os parâmetros "Utiliza regra de vencimento para dias fixos? - **USARDIAFIXOVCT"** e "Acumula vencimento para dias fixos? - **ACVENDIAFIXOVCT**" estiverem ligados quando há mais de uma parcela definida com a mesma "Base do Prazo" (Tipos de Negociação, aba Parcelas), a base do vencimento será o valor do campo DTPRAZO do financeiro gerado. Mas se o **USARDIAFIXOVCT** for habilitado, e o parâmetro **ACVENDIAFIXOVCT** desligado, a base do vencimento será a mesma para todas as parcelas configuradas.

(1)** FP\_FOLGADOM e FOLGADOM** - Folga no Domingo?
Utilizado para o cálculo de dias úteis. Se estiver "Sim", o domingo será considerado um dia não útil, se estiver "Não", o domingo será considerado útil no cálculo.
