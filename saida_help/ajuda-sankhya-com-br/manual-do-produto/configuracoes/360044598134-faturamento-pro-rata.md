---
id: "360044598134"
titulo: "Faturamento Pro Rata"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598134-Faturamento-Pro-Rata"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:10Z"
rotulos: ["Produtos", "Configuração", "Faturamento", "Contrato", "CONTSOFT", "Faturamento Pro Rata", "Qtd. Prevista", "Faturamento Pro Rata manual", "Financeiro", "Faturamento Pró-Rata: Detalhes e Configurações"]
---

# Faturamento Pro Rata

Disponibilizado para o Sankhya Om a funcionalidade do Faturamento Pró-Rata. Este faturamento consiste em efetuar o faturamento do contrato através da análise das ocorrências dos produtos/serviços do contrato.

Para que seja efetuado este tipo de Faturamento é necessário:

Parâmetros:

"Utiliza faturamento de contratos pro rata? - FATCONTPRORATA" - Se ligado, disponibiliza a opção "Faturamento pro rata?" no [Cadastro de Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos) em sua aba "Geral", que poderá ser marcado apenas se a "Periodicidade do Faturamento" for Anual ou Mensal.

![Imagem 1: "Utiliza faturamento de contratos pro rata? - FATCONTPRORATA" - Se ligado, disponibiliza a opção "Faturamento pro…](https://ajuda.sankhya.com.br/hc/article_attachments/8768544069271)

Se marcada uma Periodicidade diferente de Mensal ou Anual o sistema emite a mensagem:

**"Só é possível utilizar contratos 'Faturamentos pro rata' com Periodicidade do Faturamento 'Mensal' ou 'Anual'."**

"Utiliza grupos de faturamento de contratos? - GRUPFATCONT" - Se ligado o sistema considerará que haverá agrupamento de contratos, além disso, serão mostrados os campos ‘“TOP para faturamento em contratos” e “Série para faturamento em contratos” para que o usuário informe TOP e Série padrão daquele produto em questão. Estes campos serão apresentados também no serviço.

Tela: Configurações » Cadastros » Produtos » Produtos.

![Imagem 2: Tela: Configurações » Cadastros » Produtos » Produtos.](https://ajuda.sankhya.com.br/hc/article_attachments/8768643870743)

Tela: Configurações » Cadastros » Produtos » Serviços.

![Imagem 3: Tela: Configurações » Cadastros » Produtos » Serviços.](https://ajuda.sankhya.com.br/hc/article_attachments/8768685261079)

Tela: Contratos e Serviços » Arquivos » Contratos.

Disponível na Aba Geral e na Aba de Produtos e Serviços.

Aba Geral:

![Imagem 4: Aba Geral:](https://ajuda.sankhya.com.br/hc/article_attachments/8768743669527)

Aba Produtos/Serviços:

![Imagem 5: Aba Produtos/Serviços:](https://ajuda.sankhya.com.br/hc/article_attachments/8768771218839)

Ignorar dia 31 no faturamento de contratos pro rata? IG31FATPRORATA - Faz com que em períodos abertos (não é a referencia inteira), o dia 31 não seja contado no calculo de preço.

Exemplo: Ativa um produto no dia 27/01, então o faturamento pro-rata vai faturar 5 dias referente a 27, 28, 29, 30 e 31 de janeiro em que o produto ficou ativo no contrato. Com o parâmetro ligado, vai faturar apenas 4 dias porque o dia 31 será ignorado.

Obs.: No faturamento em que é cobrada toda a referência fechada este parâmetro não faz diferença.

Tela: Contratos e Serviços » Rotinas » Faturamento de Contratos

Importante: Se na top informada tiver configurada para calcular ISS e no contrato não houver serviços ou o cálculo de ISS o sistema emitirá a mensagem: Tributação para cálculo de ISS não encontrada para o serviço. Para isso será necessário utilizar uma top não configurada para o cálculo de ISS.

Processo 1: Criar crédito\débito na próxima fatura

Contrato: 27

Data do Contrato: 01/01/2014

Produto: 141

Ativação do Produto: 01/01/2014

Valor do Produto: 1000,00

Gerado a fatura do mês de abril e posteriormente foi criada para o produto a ocorrência de cancelamento.

![Imagem 6: Gerado a fatura do mês de abril e posteriormente foi criada para o produto a ocorrência de cancelamento.](https://ajuda.sankhya.com.br/hc/article_attachments/8768849362711)

#### Aba Pendências para a próxima fatura

Este quadro mostrará uma pendência de crédito ou débito que foi gerada em função da ocorrência selecionada acima.

Serão mostrados os seguintes campos:

Pendência: Pode ser “Crédito” ou “Débito”. Será crédito se já foi faturado o produto e cancelado posteriormente. Será débito se informado produtos posterior ao faturamento do contrato.

Valor: É o valor (R$) da pendência. Será o valor do produto dividido por 30 e multiplicado pelo número de dias. Se for crédito irá diminuir do valor do produto.

Valor acertado: É o valor (R$) desta pendência que já foi acertado. Será atualizado no faturamento de contratos.

![Imagem 7: Valor acertado: É o valor (R$) desta pendência que já foi acertado. Será atualizado no faturamento de contratos.](https://ajuda.sankhya.com.br/hc/article_attachments/8768907263127)

O sistema fez o cálculo:

01 a 15: 14 dias com preço de 1000 reais. O sistema não considera o dia de cancelamento.

Para compor o crédito o preço diário é R$ 1000, divido por 30 dias, que resulta R$ 33,33.

Se multiplicar pela quantidade dará: 14\*33,33 = 466,66, se pegar 1000-466,66 = 533,33.

Inserido o produto 142 com o valor de 1500,00.

15 a 30: 16 dias com o preço de 1500,00

Para compor o débito o preço diário é R$ 1500, divido por 30 dias, que resulta R$ 33,33.

Se multiplicar pela quantidade dará: 16\*50 = 800,00

![Imagem 8: Se multiplicar pela quantidade dará: 16*50 = 800,00](https://ajuda.sankhya.com.br/hc/article_attachments/8768990491927)

#### Acerto de Pendências:

Conforme visto para que seja geradas pendências é necessário que o contrato tenha faturado já e houver após o faturamento o cancelamento do produto e inserção de um novo.

Portanto, para o primeiro faturamento o sistema trará como valor unitário o valor do produto\serviço:

![Imagem 9: Portanto, para o primeiro faturamento o sistema trará como valor unitário o valor do produto\serviço:](https://ajuda.sankhya.com.br/hc/article_attachments/8768992879895)

Contrato: 38

Observação: 01/05/2014 a 31/05/2014 – Equivale ao mês inteiro

Vlr. Unitário: 1000,00

Depois deste primeiro faturamento é cancelado e inserido um novo produto e efetuado o faturamento novamente:

![Imagem 10: Depois deste primeiro faturamento é cancelado e inserido um novo produto e efetuado o faturamento novamente:](https://ajuda.sankhya.com.br/hc/article_attachments/8769056191767)

Contrato: 38

Produto: 142 - 01/05/2014 – 1500,00 - 01/06 a 30/06 - 1500,00

Observação: 01/06/2014 a 30/06/2014 – Equivale ao mês inteiro

Pendências: 800 – 533,33 = 266,67

Total + Pendência: 1500 + 266,67 = 1766,67

No contrato fica:

![Imagem 11: No contrato fica:](https://ajuda.sankhya.com.br/hc/article_attachments/8769080318231)

Produto 141:

![Imagem 12: Produto 141:](https://ajuda.sankhya.com.br/hc/article_attachments/8769149050775)

#### Agrupamento de Contratos:

O agrupamento se dará com base na seguinte chave:

a.Empresa

b.Parceiro

c.Grupo de Faturamento

d.TOP para faturamento em contratos

e.Série para faturamento em contratos

f.Contrato de órgão público

g.Caso seja, adiciona-se o ano também.

h.Dia do pagamento

i.Periodicidade do Faturamento

j.Critério de Rateio

k.Considera dia do pagamento como dia útil

l.Prazo de vencimento

Assim, durante o faturamento todos os itens que resultarem na mesma configuração acima serão agrupados em uma mesma fatura.

Exemplo:

Algumas informações, assim como no faturamento convencional são obtidas a partir do contrato de menor numero, isso, pois como é um faturamento agrupado, não temos como unir todas as informações de todos. Sendo os campos:

•Centro de Resultado

•Natureza

•Projeto

•Tipo de Negociação (Respeita marcação nas configurações da tela de faturamento)

•Vendedor (do parceiro do contrato)

•Contrato dos financeiros

•Critério de Rateio (para rateio do financeiro)

Quando o parâmetro de agrupamento estiver ligado e possuir contratos pro rata e convencionais na tela faturamento o sistema realiza a separação destes em dois grupos, onde os pro rata passa pela nova rotina enquanto os que não são passam pela rotina convencional. Quando o parâmetro está desligado, o pro rata segue o basicamente o mesmo fluxo do convencional.

**Observação:** para que Contratos com faturamento pró-rata apresentem o valor do contrato na tela "Contratos e Serviços > Rotinas > Faturamento de Contratos", a marcação "Faturamento pro rata" presente na aba Geral da tela "Contratos e Serviços > Arquivos > Contratos" precisa estar efetuada. Além disso, ainda na tela "Contratos e Serviços > Arquivos > Contratos > Aba Produtos/Serviços > Aba Geral", o campo "Qtd. Prevista" precisa ser preenchido com um valor maior que zero.

O parâmetro "Contrato para software? - CONTSOFT" quando ativado, altera a descrição do campo "Quantidade" presente na tela "Contratos e Serviços > Arquivos > Contratos > Aba Produtos/Serviços > Aba Geral" para a descrição "Número de usuários".

#### Faturamento de Grupo de Contratos

Existem contratos do tipo "Faturamento pró rata" que utilizam o faturamento com agrupamento de contratos por grupo. Contudo, tem-se alguns contratos que não utilizam essa modalidade de agrupamento. Atualmente, o sistema gera as provisões no faturamento de contrato com as parcelas igual ao valor do contrato.

Caso seja necessário que as provisões sejam geradas conforme o valor da nota, ou seja, gerando parcelas de provisão com o valor líquido, deve-se habilitar os parâmetros "Utiliza grupos de faturamento de contratos? - GRUPFATCONT" e "Faturar contratos pro rata sem grupo isoladamente - FATCONPRSGISOL".
