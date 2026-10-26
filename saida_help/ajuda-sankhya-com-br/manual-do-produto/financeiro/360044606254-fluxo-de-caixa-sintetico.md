---
id: "360044606254"
titulo: "Fluxo de Caixa Sintético"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:38:55Z"
rotulos: ["AJUDA DO SKW", "manual", "Relatórios", "Contas", "Parceiro", "Moeda", "Movimentação Financeira", "Relatórios Gerenciais", "Caixa", "Cubo", "Fluxo", "Financeiro", "EMAILGESFIN", "Float", "DIASNTFFLUCAIXA", "Fluxo de Caixa Sintético", "FREQUSOFLUCAIXA", "PERCINADANT", "PERCINADATU", "PERCINADPOS", "Saldos", "Saldos Bancários", "br.com.sankhya.fin.fluxo.caixa.sintetico", "Fluxo de Caixa Sintético  manual", "Resumo diário planejamento financeiro", "Conciliação e lançamentos corretos", "Filtros contas moeda e impressão"]
---

# Fluxo de Caixa Sintético

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312315679383) Módulo: Financeiro > Relatórios > Gerenciais
```

---

O Fluxo de Caixa Sintético é um demonstrativo que resume todas as entradas e saídas de recursos financeiros da empresa dia a dia. Ele funciona como um simulador do futuro, permitindo avaliar antecipadamente a necessidade de captação de recursos ou de investimento dos excedentes de caixa em aplicações, por isso é uma importante ferramenta de planejamento que busca sempre o perfeito equilíbrio financeiro da empresa.

Pode ser utilizado também para análises passadas, retratando como foi a movimentação financeira diária da empresa na última semana, mês ou período desejado de títulos já recebidos ou pagos, ou comparando o realizado com o que ainda está pendente.

Pré-requisitos para análise de Fluxo de Caixa:

1. Conciliação Bancária em dia e saldos bancários corretos.
2. Receitas e Despesas Reais e Provisões lançadas no sistema.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK51KMN8SZWVDTCT2YP5KR)                                                                [Aba Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK57X81WW1NCYBAV1HKZ75)
[Aba Cubo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK5M2S1R9ZD0TFRZA6QMNS)                                                                [Parâmetros que influenciam este relatório](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK61P17E87ZGMK4YF5P5FJ)
[Modelos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK68872N03MTTSKKQFK903)                                                                  [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#h_01ENXK6F57VJDT095D4S1ACVKZ)

## Aba Geral

![Imagem 2: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/360082518014)

Informe em **"Data de Negociação no Período"** o período no qual os títulos foram negociados; aqui também serão considerados os títulos Pendentes.

Defina na **"Data de Movimento no Período"**, o período de movimentação financeira, ou seja, os títulos movimentados no período; analise aqui, baixa efetiva.

Preencha em **"Vencendo no Período"**, o período de vencimento dos títulos.

Referente à marcação **"Considerar Float"**, o float é definido no cadastro de **"Tipos de Títulos"**. É necessário configurar os Tipos de Títulos de recebíveis da empresa e marcar esta opção na visualização do relatório de Fluxo de Caixa, de modo que não se conte com dinheiro na conta antes dele realmente estar disponível. Assim, teremos o exemplo:

Uma boleta com vencimento no dia 25/11, cujo Tipo de Título consta um Float = 2, aparecerá nos relatórios de fluxo de caixa na data do dia 27/11.

**Observação:** quando a marcação **"Considerar dias úteis"** da tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) estiver habilitada, o sistema irá ponderar a data de vencimento + marcação Considerar float para exibir os títulos para análises. **{disponível na versão ≥ 4.12}**

**Importante:** se o parâmetro **"Transfere vencimento quando fim de semana/feriado - TRANSFVENC"** esteja ligado e a opção "Considerar dias úteis" da tela Tipos de Títulos, for desmarcada, o valor apresentado no relatório será sempre em dia útil.

Selecione na seção **"Baixados no Período"**, o período de baixa dos títulos.

Por fim, determine quais os títulos serão visualizados entre **"Receitas"** e/ou **"Despesas"**, **"Real"** e/ou **"Provisão"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)

## Aba Avançado

![Imagem 3: Aba Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/360083694593)

#### Seleção das Contas

**Nota:** você poderá selecionar contas para apresentar seus saldos no início do relatório, considerando desta forma o saldo atual das contas além das movimentações futuras.

**Apenas Contas Ativas:** Ao marcar a opção **"Apenas Contas Ativas"**, o sistema irá avaliar apenas as operações realizadas com as contas ativas. Esta é uma marcação apenas para apresentação das contas na tela de seleção; para que estas contas sejam impressas, deve-se marcar a opção **"Imprime Saldos"**.

Ao efetuar a marcação **"Imprime Saldos"**, serão impressos os saldos das contas no início do Relatório.

Por meio da opção **"Saldos referentes à data"**, serão apurados os saldos na data aqui informada.

Referente à **"Considera o saldo das contas no acumulado dos pendentes"**,  quando a seleção desta é realizada, a coluna **"Acumulado"** do relatório será apresentada somando ou subtraindo o saldo das contas do acumulado que for resultado do cruzamento entre receita e despesa. Se desmarcada, o relatório só apresentará o saldo; o acumulado será apenas a diferença entre receitas e despesas.

Através da marcação **"Imprime somente totais"**, serão impressos no relatório apenas os totais dos dados.

Os botões **"Marcar Todas"** e **"Desmarcar Todas"** auxiliam na seleção das contas a serem exibidas na grade.

#### Ordenar por data de:

Através da escolha de uma destas opções, determine como se dará a ordenação das informações apresentadas no relatório. Teremos as seguintes opções:

- Negociação;
- Vencimento;
- Baixa.

#### Conversão de moeda

Primeiramente, preencha o campo **"Moeda"** quando existirem transações financeiras em moedas estrangeira. Selecione em seguida, a **"Data para converter a moeda"**, onde apresentam-se as seguintes opções:

- **Negociação:** Converte pela data de negociação do Título. Utilizada quando o valor de conversão for fixada na data de negociação.
- **Vencimento:** Converte através da data de vencimento do Título. Utilizada quando a conversão ocorrer na data de vencimento.
- **Baixa:** Aqui a conversão é feita pela data da baixa. Usada quando o valor for convertido na data da baixa do Título.
- **Fixa:** A conversão é feita de acordo com um valor fixo informado no cadastro de moedas. Normalmente utilizado em negociações contratuais que estipulam um valor fixo de conversão durante a vigência do contrato.

O tipo do **"Período"** definirá a forma de agrupamento do relatório, que poderá ser **"Diário"** ou **"Mensal"**.

#### A conversão da moeda será da seguinte forma:

Os títulos que possuem moeda diferente da "moeda corrente" serão convertidos para a moeda corrente considerando a data para conversão. Para valores que vêm da tabela TGFSBC (cadastro de Contas Bancárias, aba Saldo > Saldo Banco e Saldo Real), a conversão será pela data de referência; na tabela TGFMBC (tela de Conciliação Bancária) a conversão será pela data de lançamento.

Se a data para converter a moeda for **"Fixa"**, será disponibilizado um campo de data para a digitação da mesma. Uma linha no cabeçalho do relatório trará qual moeda foi escolhida e qual a data para conversão da mesma.

#### Saldo Anterior Pendente:

Com a opção **"Imprime o saldo anterior de receitas pendentes"** marcada, o relatório irá apresentar o saldo de **"receitas"** anteriores a data informada em **"Saldo anterior a partir de:"**. Assim, pode-se visualizar no relatório os valores a receber que já estão vencidos, ou seja, estes valores não estarão presentes no fluxo de caixa, mas pode-se considerar o recebimento deles nos próximos dias, uma vez que estão vencidos.

Se marcada, a opção **"Imprime o saldo anterior de despesas pendentes"** o relatório irá exibir o saldo de **"despesas"** anteriores a data informada em **"Saldo anterior a partir de:"**. Desta forma, pode-se visualizar no relatório os valores a pagar que já estejam vencidos, ou seja, estes valores não estarão presentes no fluxo de caixa, mas pode-se considerar o pagamento deles.

#### Outras Opções de Impressão

Com a opção **"Imprime o valor líquido pendente"** marcada, o sistema irá analisar as marcações efetuadas na tela **"Financeiro > Preferências > Componentes do Valor Líquido"**, para realização desta impressão.

Caso a marcação **"Imprime Filtros"** for realizada, os filtros realizados, **"Data de Negociação no Período"**, **"Data do Movimento no Período"**, **"Vencendo no Período"**, e **"Baixados no Período"** serão apresentados na impressão do relatório.

Quando você marcar a opção **"Considerar baixa futura como títulos a pagar/a receber"**, o sistema irá considerar os títulos baixados, com data de baixa maior que a data atual, como títulos **"a receber"** / **"a pagar"**. Se desmarcada, o sistema considerará os títulos com baixa futura como **"recebidos"** ou **"pagos"**.

Se opção **"Usar Antecipação/Atraso habitual do pagto do Cad.Parceiro?"** for selecionada, serão considerados os dias informados de atraso ou antecipação, que habitualmente o parceiro tenha, na formação do fluxo de caixa. Assim não pode-se contar com o valor antes do dia que o parceiro costuma pagar. A Antecipação/Atraso é configurada no **"Cadastro de Parceiros"**, aba **"Crédito"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)

## Aba Cubo

Nesta aba o sistema apresenta o Fluxo de Caixa em forma de Cubo.

Este Cubo é uma ferramenta flexível, que permite a escolha dos campos ou critérios desejados para realização das análises; além de prover um grande número de recursos para permitir a visualização dos resultados por diferentes aspectos, acrescentando ainda diversos indicadores sobre os dados selecionados, comparando-os em suas **"Linhas"** ou **"Colunas"**.

Para indicar os campos que o cubo irá possuir, selecione os mesmos a lista **"Campos Disponíveis"** e faz-se o seu transporte para a área desejada no cubo, ao utilizar o botão **"Adicionar na"**. Pode-se arrastá-los também através do mouse.

![Imagem 4: Para indicar os campos que o cubo irá possuir, selecione os mesmos a lista "Campos Disponíveis" e faz-se o seu…](https://ajuda.sankhya.com.br/hc/article_attachments/360083695633)

Os dados serão analisados de acordo com os campos filtrados e os resultados visualizados por diferentes aspectos. Tudo dependerá da forma como o usuário combinar os campos de filtros e os dados.

Em cada uma das colunas é possível filtrar os dados que deverão ser apresentados no Cubo. Assim é possível personalizar o filtro da forma mais conveniente ao usuário e à situação.

![Imagem 5: Em cada uma das colunas é possível filtrar os dados que deverão ser apresentados no Cubo. Assim é possível personalizar…](https://ajuda.sankhya.com.br/hc/article_attachments/360083695673)

Pode-se também visualizar os dados em forma de grade; para isso pressione o ícone **"Grade"** localizado no canto superior esquerdo da tela.

![Imagem 6: Pode-se também visualizar os dados em forma de grade; para isso pressione o ícone "Grade" localizado no canto superior…](https://ajuda.sankhya.com.br/hc/article_attachments/360083695773)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)

## Parâmetros que influenciam este relatório

- **Percentual de Inad. da data atual em diante - PERCINADATU;**
- **Percentual de Inad. com atraso de até 2 meses - PERCINADANT;**
- **Percentual de Inad. com atraso de mais de 2 meses - PERCINADPOS.**

Estes três parâmetros impactam diretamente no resultado da coluna **"A Receber"** do relatório, na visualização dos títulos pendentes. Os valores apresentados nesta coluna do relatório são valores estimados de recebimentos livres da inadimplência esperada para o período. Ou seja, baseado em movimentações passadas, a empresa deve estabelecer "percentuais esperados de inadimplência" para que a análise de Fluxo de Caixa tenha uma visão realista sobre os valores a receber da empresa, de forma a não fazer-se compromissos com as receitas previstas além daquele montante cujo recebimento seja certo.

Um dos percentuais definidos nestes três parâmetros será aplicado ao valor **"A Receber"**, de acordo com a data de vencimento apresentada pelo relatório, tomando a data da emissão do relatório como data base para o cálculo.

Vejamos um exemplo:

- Data da Emissão: 01/01/2015
- Percentual de Inad. da data atual em diante: 5
- Percentual de Inad. com atraso de até 2 meses: 10
- Percentual de Inad. com atraso de mais de 2 meses:  20

1) O valor a receber com vencimento a partir do dia 02/01/2015 será apresentado no relatório com uma redução de 5%, se comparado com o valor nominal dos títulos;

2) O valor a receber com vencimento entre os dias 03/11/2014 e 01/01/2015 será apresentado no relatório com uma redução de 10%;

3) O valor a receber com vencimento até o dia 02/11/2014 será apresentado no relatório com uma redução de 20%.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)

## Modelos que irão facilitar a utilização do "Fluxo de Caixa Sintético"

**Modelo 1: Fluxo de Caixa Simples**

A forma mais simples de utilizar o Fluxo de Caixa é selecionando os seguintes filtros:

- Pendentes;
- Vencendo no período (de hoje até o fim da semana, mês ou mais);
- Receitas;
- Despesas;
- Real;
- Provisão.

Desta forma, você visualizará um relatório contendo um resumo dia a dia do que a empresa tem a receber, a pagar, a diferença e o acumulado.

**Modelo 2: Fluxo de Caixa visualizando saldos bancários**

Neste caso, deve-se incluir na análise acima os seguintes filtros:

- Seleção das contas para compor o saldo bancário;
- Imprime Saldos;
- Saldos referentes à data (normalmente a data do início do filtro de **"Vencendo no período"**).

Será acrescentada a análise do tópico anterior, um resumo de todas as contas bancárias selecionadas, **"Saldo Real"** e **"Saldo Bancário"** com totalizadores.

**Modelo 3: Fluxo de Caixa considerando Saldos Bancários no Acumulado**

Para esta análise, deve-se incluir na análise do Modelo 2 acima, a seguinte opção:

- Considera o Saldo das contas no acumulado dos Pendentes

O sistema considerará a soma de todos os **"Saldos Reais"** das contas selecionadas como saldo inicial na coluna de "Acumulado" dos títulos que ainda estão pendentes. Esta é uma análise muito interessante, pois normalmente a empresa conta com o saldo que possui em contas correntes, em caixa para pagar as contas e não só o que será recebido no período.

**Observação:** esta opção não é utilizada em análises de títulos baixados, pois títulos nesta situação já entraram na composição do saldo bancário por isso esta opção tem o nome de: **"Considera o Saldo das contas no acumulado dos Pendentes"**.

Na seleção das contas, normalmente seleciona-se apenas contas correntes, caixa ou ainda conta aplicação quando os saldos das contas estão baixos e a empresa precisa realizar resgates de aplicações. Mas contas Adiantamento, Empréstimo, Cartão e outras nunca devem entrar na análise de fluxo de caixa.

**Modelo 4: Fluxo de Caixa considerando Float**

O Float é definido no cadastro de "Tipos de Títulos" é necessário configurar os "Tipos de Títulos" de recebíveis da empresa e marcar esta opção na visualização do relatório de Fluxo de Caixa, de modo que não sejam considerados valores em conta antes deles realmente estarem disponíveis. Assim, tem-se um exemplo de float:

Um boleto com vencimento no dia 25/11, cujo "Tipo de Título" consta um Float = 2, aparecerá nos relatórios de fluxo de caixa na data do dia 27/11.

Para analisar Fluxo de Caixa considerando o Float, marca-se a opção:

- Considerar Float

**Modelo 5: Fluxo de Caixa considerando inadimplência**

Configure os seguintes parâmetros:

- Percentual de Inad. da data atual em diante - PERCINADATU;
- Percentual de Inad. com atraso de até 2 meses - PERCINADANT;
- Percentual de Inad. com atraso de mais de 2 meses - PERCINADPOS.

O Relatório de Fluxo de Caixa desconta do valor a receber, valores vencidos ou a vencer, os percentuais definidos nos parâmetros, visando simular uma possível "inadimplência" que costuma ocorrer na empresa. Os dados informados nestes parâmetros ficam visíveis no cabeçalho do relatório na opção **"Percentual esperado de Inadimplência"**.

**Modelo 6: Fluxo de Caixa considerando baixas futuras como títulos a pagar e a receber**

Para esta análise você irá acrescentar ao Modelo 1 ou 3, a seguinte configuração:

- Considerar baixa futura como títulos a pagar ou a receber;
- Baixados;
- Baixados no período (o mesmo período do campo vencendo no período)

Desta forma o sistema irá gerar um Fluxo de Caixa onde todos os títulos baixados com data futura serão considerados como títulos "Pendentes" na visualização do relatório.

**Modelo 7: Fluxo de Caixa considerando Antecipação ou Atraso habitual do Parceiro**

Configure na tela **"Configurações > Cadastros > Parceiros > aba Crédito"**, o campo **"Antecipação/Atraso recebimento (em dias)"**, onde números negativos serão considerados como antecipação e números positivos como atraso.

Por exemplo:

- - 2 O cliente costuma antecipar 2 dias.
- 2 O cliente costuma atrasar o pagamento em 2 dias.

Acrescente a análise do Modelo 1 ou 3 à seguinte configuração:

- Usar antecipação ou atraso habitual de pagamentos do cadastro de Parceiros

O sistema irá gerar um Fluxo de Caixa onde todos os títulos dos parceiros configurados serão apresentados com vencimentos **"Adiantados"** ou **"Atrasados"**.

**Modelo 8: Fluxo de Caixa considerando cotação de moedas**

As moedas devem ser cadastradas de acordo com a periodicidade de cada uma para todo período analisado.

Por exemplo, se a análise do mês 09/2015 for feita em dólar que é uma moeda de cotação diária é necessário que todos os dias que tiverem lançamentos tenham moeda cadastrada para que o sistema consiga realizar a devida conversão.

Deve-se acrescentar na análise do Modelo 1 ou 3, o código da moeda e os relatórios terão os valores convertidos de acordo com a moeda analisada.

**Modelo 9: Fluxo de Caixa imprimindo Saldo anterior pendente**

Para esta análise, seleciona-se as seguintes opções:

- Imprime o saldo anterior de Receitas Pendentes
- Imprime o saldo anterior de Despesas Pendentes

O relatório irá apresentar um resumo dos valores pendentes.

**Modelo 10: Fluxo de Caixa considerando saldo anterior pendente no acumulado**

Configura-se a opção:

- Saldo anterior a partir de: (informando uma data)

O sistema inclui na primeira linha do Fluxo o **"Valor Pendente do Período"** da data informada neste campo e a primeira data do período informado no campo, **"Vencendo no Período"**. Tem-se:

Se estiver sendo analisado o fluxo de caixa de 21/09 até 30/09 e deseja-se que o sistema considere no fluxo os valores "Pendentes" desde 01/09, na visualização do relatório todos os valores "Pendentes" de 01/09 à 20/09 serão somados e incluídos no acumulado do fluxo de caixa.

**Modelo 11: Fluxo de Caixa análise via Cubo de Decisão**

É possível visualizar o Fluxo de Caixa via "Relatório" ou "Cubo de Decisão" bastando para isto selecionar a aba "Cubo".

**Modelo 12: Fluxo de Caixa imprimindo valor líquido pendente**

Seleciona-se a opção:

- Imprime valor líquido pendente

O sistema não irá considerar apenas o valor do desdobramento na análise dos valores pendentes e sim o valor configurado no menu **"Financeiro > Preferências > Componentes do Valor Líquido"**.

Quando a análise for de títulos baixados sempre será necessário considerar o **"Valor líquido"**, caso contrário, o sistema irá considerar o valor do desdobramento e surgirão diferenças na análise.

Para consultar o Help de Relatórios Formatados, acione o link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)

## Parâmetros

**E-mail(s) do(s) gestor(es) financeiro(s) - EMAILGESFIN:** Neste parâmetro devem ser inserido(s) o(s) e-mail(s) do(s) gestor(es) que serão comunicados sobre o não acesso às telas de Agenda Financeira, Fluxo de Caixa e Conciliação Bancária.

**Frequência de uso esperada Rel. fluxo de caixa - FREQUSOFLUCAIXA:** Neste parâmetro informe a frequência aguardada de uso da tela de Fluxo de Caixa Sintético; por exemplo, de 05 em 05 dias.

**Dias notificação de não uso Rel. fluxo de caixa - DIASNTFFLUCAIXA:** Indique neste parâmetro os dias de notificação em que o gerente receberá e-mail caso a tela Fluxo de Caixa Sintético não seja acessada conforme definição do parâmetro **"FREQUSOFLUCAIXA"**. Por exemplo, caso a tela de Agenda Financeira não seja acessada em 10 dias, será enviado um e-mail ao gestor sobre o não acesso dos usuários à tela.

Os três parâmetros mencionados acima, trabalham em conjunto e afetam o sistema da seguinte maneira:

Quando algum funcionário que possua acesso a tela Fluxo de Caixa Sintético efetuar o login no sistema, será exibido um pop-up de alerta sobre o período que a referida tela não está sendo acessada, de acordo com os parâmetros **"FREQUSOFLUCAIXA"** e **"DIASNTFFLUCAIXA"**. Caso os dias definidos em ambos os parâmetros sejam ultrapassados, será encaminhado um e-mail ao(s) endereço(s) de e-mail(s) inserido(s) no parâmetro **"EMAILGESFIN"**.

Uma vez posicionado no pop-up citado, clicando em **"Próximo"** na mensagem apresentada, tem-se a marcação **"Não quero receber mais este alerta"**; sendo esta efetuada, o pop-up não será mais apresentado. Com esta medida, nas **"Opções de contexto"** (localizado no lado superior direito da tela) será apresentada a opção **"Receber notificações Gaps gestão"** para que o(s) usuário(s) volte(m) a receber o alerta.

**Observações:**

- Quando o usuário ler o aviso, ele somente será notificado quando atingir o prazo estipulado no parâmetro **"FREQUSOFLUCAIXA"** com base no último envio, mesmo que ele ainda não tenha acessado a rotina;
- Ao deixar os parâmetros **"FREQUSOFLUCAIXA"** e **"DIASNTFFLUCAIXA"** marcados com "0" (zero), as mensagens não serão exibidas aos usuários. O preenchimento padrão deste parâmetro é "0" (zero);
- As mensagens são exibidas tendo em vista o grupo de funcionários que possuam acesso a tela mencionada. Por exemplo, se existem os funcionários A, B e C que possuem acesso a tela, a mensagem será exibida à todos eles. Quando qualquer um desses usuários acessar a tela, a mensagem não será mais emitida para os demais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico#top)
