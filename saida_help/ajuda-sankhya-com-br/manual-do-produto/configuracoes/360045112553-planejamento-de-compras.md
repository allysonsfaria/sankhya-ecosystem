---
id: "360045112553"
titulo: "Planejamento de Compras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112553-Planejamento-de-Compras"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:20Z"
rotulos: ["Produtos", "manual", "Configuração", "Planejamento", "CONTACESSCONSOL", "Estoque", "Planejamento de Compras", "USAPLANCPCONCES", "br.com.sankhya.planejamentodecompraskia", "Planejamento de Compras manual", "Otimização do Planejamento de Compras", "Comercial"]
---

# Planejamento de Compras

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311020485015) Módulo: Comercial > Rotinas
```

---

Um planejamento de compras é uma análise feita a partir dos produtos, onde a necessidade de  compra é calculada e sugerida pelo sistema com base no giro dos produtos, a posição atual do estoque e a previsão dos pedidos pendentes. Com o recurso da projeção de estoque é possível saber como o estoque irá se comportar até o momento do recebimento da mercadoria comprada, identificando possíveis rupturas (falta de estoque), podendo gerar pedidos complementares para o produto com diferentes meios de transporte, evitando excesso ou falta do produto em estoque e aproveitando o meio de transporte mais vantajoso.

![Imagem 2: No Sankhya Om , essa rotina refere-se a um parceiro especifico.](https://ajuda.sankhya.com.br/hc/article_attachments/16695634332439) No Sankhya Om, essa rotina refere-se a um parceiro especifico.

O parâmetro **"USAPLANCPCONCES - Utiliza planejamento compras para concessionárias?"**, habilita a rotina de planejamento de compras, que consiste na ativação da tela acessada em **"Comercial > Rotinas > Planejamento de Compras"**.

Com a ativação do parâmetro, é habilitada no [Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-), a aba [Plan. Compra de Peças](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-#abaplan.decompradepeas), onde serão informados dados, que irão complementar a rotina de Planejamento de Compras.

![clip0177](https://ajuda.sankhya.com.br/hc/article_attachments/360061003414)

**%Desvio Máximo:** Percentual máximo de desvio entre o giro médio diário normal e o giro médio diário recente.

**Compra Mínima:** Informa-se o mínimo da quantidade do produto que se deve adquirir.

**Estoque de Segurança:** Corresponde ao estoque de segurança do produto.

**Estoque de Segurança (dias úteis):** Informa-se o estoque de segurança em dias úteis para cálculo dinâmico em função do giro.  Define-se o prazo de consumo do estoque de segurança.

**Data de Alteração (Estoque de Segurança):** Este campo registra automaticamente a data e hora de alteração do Estoque de Segurança. Este campo não é editável.

**Lote de Compra (dias úteis):** Representa o período para o qual se pretende comprar.  Define-se o prazo ideal entre dois pedidos consecutivos, é a frequência de compras.

**Agrupamento Mínimo:** Múltiplo para um pedido de compra.  A sugestão final de compra deverá ser ajustada a um múltiplo do agrupamento mínimo.

**Arredondamento para Agrupamento:** Ao ajustar-se a quantidade de um pedido ao múltiplo do Agrupamento mínimo, a divisão poderá não ser exata.  No arredondamento simétrico o valor para arredondar para cima é 0,5 que deverá ser o default deste campo, que possibilita arredondamentos diferentes.

**Estoque Máximo:** Informa-se aqui o estoque máximo em quantidade; quando informado será estático, não sendo calculado pelo giro.

**Estoque Máximo (dias úteis):** Estoque máximo em dias úteis, utilizado para cálculo dinâmico em função do giro.

**Data de Alteração (Estoque Máximo):** Este campo registra automaticamente a data de alteração do Estoque Máximo. Este campo não é editável.

**Aplica Sazonalidade:** Quando marcado, a projeção de demanda futura será aplicada a sazonalidade prevista para este produto. Estando desmarcado, isso não irá ocorrer.

## Inserindo um novo planejamento de compras

Ao clicar no botão irá aparecer um painel para o cadastro do cabeçalho do planejamento que necessita das informações do modelo de planejamento, um título (Descrição) do planejamento e a empresa. Ao clicar em **"salvar"** será registrado o cabeçalho de planejamento com os parâmetros para cálculo do giro importados do modelo de planejamento informado. Não será gerado nenhum item no planejamento, pois poderão ser feitas quaisquer alterações nos parâmetros.

**Veja como incluir novos modelos abaixo neste documento:**

Para gerar os itens do planejamento deve-se clicar no botão processar, será aberto o popUp para alguma alteração nos parâmetros e ao clicar em **"ok"** caso algum filtro possua parâmetros variáveis será aberto um popUp para informar esses parâmetros, logo após será processado as informações dos itens.

Para visualizar algum planejamento já criado existe um botão de pesquisa abrirá um popUp com filtros para seleção do planejamento desejado.

Na opção **"Agendamento da geração da tabela de giro"** permite agendar a consolidação da tabela de giros como é feito na análise de giro ([ver documentação sobre análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554#agendamentodagera%C3%A7%C3%A3odatabeladegiro)).

**Nota:** para exclusão ou reprocessamento do planejamento não pode existir pedidos de compra gerados para este planejamento.

## Grade de Produtos (itens do planejamento)

Os produtos aqui apresentados podem possuir movimentações de giro ou não dependendo da configuração do planejamento. Os produtos com giro possuem consolidação (TGFGIR1) positiva e os produtos sem giro podem possuir consolidação negativa (devoluções) ou simplesmente não possuir informação de giro. Em ambos os casos é levado em consideração o fato de o produto estar ativo e a opção **"Permite comprar este produto?"** do cadastro de produtos estar ligada.

#### GMD (Giro Médio Diário)

Quantidade média de vendas dentro dos períodos de análise de giro. As vendas são analisadas a partir a partir de datas anteriores. Temos o exemplo:

Data da análise 29/10/2013; os períodos serão contados a partir do dia 28/10/2013.

A data da análise não entra, pois é considerada uma data futura e os períodos para análise fazem parte do passado. Dentro de cada período serão contabilizados a quantidade de dias úteis. Temos o exemplo:

Período 1; data inicial 22/10/2013; data final 28/10/2013; dias uteis 5.

Depende da configuração do planejamento de compra.

#### GMDR (Giro Médio Diário Recente)

Semelhante ao GMD. Aqui se olha o giro em períodos menores e esses períodos são sempre os mais recentes. Tem-se o exemplo:

Dentro de um período de GMD de 8, os 3 primeiros períodos a partir da data da analise serão analisados.

Depende da configuração do planejamento de compra.

#### Desvio

Com base no GMD e GMDR pode-se obter a variação do período mais recente em relação ao período normal. Temos o exemplo:

Em todos os períodos de analise foi obtido um giro de 5, mais recentemente o giro ficou em 10. A conclusão é que ultimamente o produto esta girando muito.

#### Desvio Máximo

Percentual máximo para o desvio configurado no produto. No caso de um desvio acima deste valor, o campo desvio será destacado com cor diferente.

#### LeadTime

Demanda ajustada de todos períodos de LeadTime. Somatório de todas as demandas de cada período de LeadTime, onde a demanda é obtida a partir do GMD de cinco dias uteis mais sazonalidades.

#### Lote de Compra

Semelhante ao LeadTime mais baseado nos períodos de Lote de Compra.

#### Estoque de Segurança

Semelhante ao LeadTime mais baseado nos períodos de Estoque de Segurança.

**Demanda**

Demanda total durante a análise

Somatório de LeadTime, Lote de Compra e Estoque de Segurança.

**Estoque Físico**

Estoque físico disponível na data da analise.

#### Pedidos de Compra Pendentes

Somatório das quantidades de pedidos de compra pendentes em cada período de LeadTime.

A analise dos pedidos de compra para cada período segue um padrão baseado na TOP e nos LeadTimes do meio de transporte do pedido.

TOP TOPKIAPO

 Quantidade = TGFCAB.DTNEG

 Data Prevista de entrega = TGFCAB.DTNEG + Lead Time Total do meio de transporte

TOP TOPKIACO

 Quantidade = TGFICO. BKORDERQTY

 Data prevista de entrega = TGFICO.DTSTATUS + Lead Time de confirmação do meio de                transporte

 Quantidade = TGFICO. PROCQTY

 Data prevista de entrega = TGFICO.DTSTATUS + Lead Time de processamento do meio de                transporte

 Quantidade = TGFICO. PACKQTY

 Data prevista de entrega = TGFICO.DTSTATUS + Lead Time de empacotamento do meio de                transporte

TOP TOPKIAINVOICE

 Quantidade = Quantidade Negociada - Quantidade Atendida

 Data prevista de Entrega = TGFCAB.DTNEG + Lead Time de despacho do meio de                        transporte

Outras TOPs de pedido de compra

 Quantidade = Quantidade Negociada - Quantidade Atendida

 Data prevista de entrega =  TGFCAB.DTNEG + Lead Time Total do meio de transporte

Com base na Data prevista de entrega os pedidos e suas respectivas quantidades são posicionados nos períodos de LeadTime.

#### Pedidos de Venda Pendentes

Quantidades de pedidos de venda pendentes em cada período de LeadTime. Os pedidos de venda sempre entram na semana da análise, pois não se trabalha com previsão de entrega.

#### Estoque Previsto

Estoque previsto baseado no estoque físico atual, pedidos de compra pendentes e pedidos de venda pendentes.

#### Estoque Futuro

Previsão de quanto será meu estoque final após o período de LeadTime.

A demanda do período de LeadTime menos o estoque previsto.

#### Estoque Futuro Ajustado

Estoque Futuro sem Estoque de Segurança. O estoque de segurança seria uma área reservada do estoque para uma demanda extra, sendo assim ele deve ser deduzido. Situação ideal seria zero.

#### Sugestão de Compra

A demanda para o período de Lote de Compra sem o Estoque Futuro Ajustado. Ex.: Tenho uma Demanda para o período de Lote de Compra de 27 e um Estoque Futuro Ajustado de 10. A sugestão deverá ser de 27-10. Deverá ser considerado também um percentual de acréscimo para prever possíveis erros. Segurança da segurança.

#### Pedido

- Quantidade para compra. Para o cálculo será levado em consideração o Agrupamento mínimo, Lote de Compra mínimo e Arredondamento para agrupamento do produto.
- Agrupamento mínimo indica, por exemplo, a capacidade de uma caixa de venda para determinado produto. Exemplo prático de um caixa com dez unidades de determinado produto.
- Lote de Compra mínima indica a quantidade mínima para compra.
- Arredondamento para agrupamento indica a fração para arredondamento do agrupamento mínimo. Tem-se o exemplo:

Sugestão de compra de 77.6; Agrupamento mínimo de 5 e Arredondamento para agrupamento de 0.5. Sugestão de compra é 75 ou 80. Cálculo = 77.6 / 5 + (1-0.5) = 16 caixas \* 5 = 80.

#### Ruptura Crítica

Primeira semana de ocorrência de um Estoque Final negativo. Útil para filtro na tela para análise de necessidade de pedidos complementares.

#### Ruptura Aceitável

Primeira semana de ocorrência de um Estoque Final – Estoque de Segurança negativo. Útil para filtro na tela para análise de necessidade de pedidos complementares.

#### Pedido Revisto

Pedido sem os pedidos Complementares. Os pedidos complementares já foram lançados para suprir uma demanda em algum período. É uma quantidade que não deve ser levada em consideração.

#### Pedido Efetivo

Campo editável sem valor inicial. Se digitado será a quantidade que servirá para geração do pedido de compra, se nulo a quantidade do pedido será a quantidade do Pedido Revisto.

Quando a grade de Itens do Planejamento for alimentada, serão apresentados também os produtos cuja compra para os mesmos não está permitida (aba Geral, campo Permite comprar este produto?); esta informação poderá ser visualizada nesta grade por meio da coluna Permite comprar este produto?. Somando-se a isso, o Meio de Transporte padrão é definido na configuração do planejamento (pop-up Parâmetros para Planejamento de Compra); esta informação também é encontrada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-) de forma que, caso esteja preenchido no produto, será desconsiderado o Meio de Transporte do planejamento e será considerado o do produto.

**Observação:** é possível realizar a Personalização do Planejamento, ou seja, tem-se a possibilidade de configurar-se ações com base na tabela de Itens do Planejamento (grade Produtos - tabela TGFIPC), de modo que se tenha a apresentação de campos adicionais pertinentes à esta tabela. Além disso, pode-se criar Abas Adicionais ligadas aos itens e filtros rápidos não obrigatórios baseados nos campos **"Aplicação"**, **"Linha"** e **"Código do Produto"**.

## Grade com a projeção de estoque

Define-se a evolução do estoque durante o período de lead time do meio de transporte da configuração do planejamento. Os períodos são divididos em Período de LeadTime, Período de Lote de Compra e Período de Estoque de Segurança.

- Período de LeadTime é baseado no Lead Time Total do meio de transporte da configuração do planejamento. Entende-se o período total para entrega do pedido;
- Período de Lote de Compra é baseado no Lote de Compra do produto. Entende-se um período para qual o estoque vai atender;
- Período de Estoque de Segurança é baseado no Estoque de Segurança do produto. Entende-se um período para qual o estoque vai garantir possíveis imprevistos como atraso na entrega, uma demanda acima do previsto.

Para todos esses períodos serão criados períodos semanais sequencialmente em LeadTime, Lote de Compra e Estoque de Segurança.

Para cada semana representada por um período temos as seguintes informações.

#### Data Final

Data final do período. Calculada a partir da data do planejamento.

#### Estoque Físico Inicial

Estoque físico na data do planejamento. Para o primeiro período é o estoque atual do produto. Ao final do cálculo de cada período, o estoque físico inicial do próximo período será o estoque final calculado no período atual.

#### Pedidos de Venda Pendente

Pedido de venda pendente reservando estoque.

#### Pedidos de Compra Pendente

Pedido de compra pendente previsto para o período.

#### Pedidos Complementares

Pedidos que foram lançados para suprir uma demanda e que estão posicionados no período de acordo com o leadtime do seu meio de transporte.

#### Estoque Disponível

Estoque disponível para venda. Estoque Físico Inicial - Pedidos de Venda Pendente + Pedidos de Compra Pendente + Pedidos Complementares.

#### Giro Médio Estendido

Giro médio do produto para um período de cinco dias úteis.

#### Sazonalidade Média

Sazonalidade futura. Observa-se o exemplo:

Na data do feriado de 7 de setembro, a demanda por determinado tipo de peça será maior devido as revisões que antecedem o feriado. Ex2.: No lançamento de modelo novo de um veículo, o modelo anterior terá uma queda nas vendas.

Uma maneira de prever futuramente se a demanda irá aumentar ou diminuir.

#### Sazonalidade

O Cálculo da Sazonalidade irá ocorrer com base em 25 períodos de 5 dias úteis; o sistema conta com um algorítmo que determina para cada sazonalidade quantos dias ela impacta em cada um dos 25 períodos. Tem-se então:

Sazonalidade Média do Período = Sazonalidade \* Dias de Impacto / 5

Pode ocorrer de duas sazonalidades impactarem em um mesmo período; neste caso, a Sazonalidade Média do Período será acumulativa e aplicada em cascata.

Vejamos um exemplo:

- Data Inicial = 01/05/2017 – segunda-feira
- Data Final = 07/05/2017
- Sazonalidade 1 = De 02/05/2017 a 15/05/2017 = 20% (4 dias úteis)
- Sazonalidade Média do Período = 20 \* 4 / 5 (Dentro do período houve impacto do dia 02 ao dia 05) = 16 %
- Sazonalidade 2 = De 05/05/2017 a 10/05/2017 = 10% (1 dia útil)
- Sazonalidade Média do Período = 10 \* 1 / 5 (Dentro do período houve impacto do dia 05 ao dia 05) = 2 %
- Sazonalidade Média do período = 16 % \* 2 % = 18,32 %

#### Demanda Ajustada

Demanda ajustada pela sazonalidade do período. Giro Médio Estendido + Sazonalidade.

#### Estoque Final

Estoque Disponível - Demanda ajustada.

#### Estoque de Segurança

Estoque de segurança. Margem para imprevistos. Quando no produto o Estoque de Segurança for informado em quantidade, o valor para todos os períodos será estático. Quando no produto o Estoque de Segurança for informado em dias úteis, o cálculo levará em consideração Demanda Ajustada. Então Estoque de Segurança = Demanda Ajustada \* (Estoque de Segurança Dias Úteis / 5 Dias Úteis).

#### Estoque Final – Segurança

Estoque final sem considerar a margem de segurança. Estoque previsto para semana de 10 – estoque de garantia 5 = estoque disponível.

#### Estoque Final – Segurança – Dias

Informativo. O estoque nesse período atenderá uma quantidade de dias. Em um lote de compra configurado para 5 dias e o Estoque Final – Segurança – Dias é de 7 dias, então o estoque nesse período está em um valor ideal.

#### Estoque Final – Segurança – Semana

Semelhante ao Estoque Final – Segurança – Dias mais transformado em semana.

#### Informações por período (Giro)

Com base na configuração e na data do planejamento serão criados períodos com datas que serão calculadas retroativamente. Ao analisar as vendas recentes, temos uma base para determinar o volume de venda de determinado produto, possibilitando uma previsão mais assertiva em relação à demanda atual e projeção da demanda dos períodos futuros.

#### Pedidos Complementares

Na análise dos períodos de projeção pode existir a possibilidade de suprir determinada quantidade devido a uma ruptura (estoque negativo). Com base nessa situação há a possibilidade de adicionar pedidos complementares informando o meio de transporte e a quantidade para o produto. Ao salvar, a grade de projeção de estoque será atualizada posicionando o pedido complementar cadastrado no período correspondente.

#### Pedidos de compra pendentes

Mostra quais pedidos de compra estão pendentes para entrar no período.

#### Pedidos de venda pendentes

Mostra quais pedidos de venda estão pendentes para entrar no período.

## Botão Processar

Ao acionar o botão **"Processar"** será aberto primeiramente, o pop-up **"Parâmetros para Planejamento de Compra"** para redefinição das parametrizações, se for o caso, e clicando-se em "OK" será aberto um outro pop-up denominado **"Processos"** onde tem-se o andamento do processamento.

Através do pop-up Processos é possível acompanhar o andamento do processamento, ver o histórico dos últimos processamentos e/ou parar o processamento atual; ao clicar em **"Parar processamento"**, todo o processamento será abortado. Mesmo que este pop-up seja fechado, o processamento irá continuar internamente; caso queira-se verificar o andamento do processamento novamente, basta clicar-se no botão **"Histórico"** na tela Planejamento de compra e selecionar-se o processamento Em execução com um duplo clique sobre a linha da grade, onde será apresentado seu andamento detalhado.

## Botão Gerar Pedidos

Esta opção irá gerar o pedido principal e os pedidos complementares, ambos agrupados por via de transporte. O pedido de compra gerado será com base no modelo de pedido/nota configurado para o meio de transporte.

**Nota:** este modelo deve estar bem configurado com a TOP correta.

Na geração do Pedido de Compra, não serão gerados pedidos para os itens que estiverem com a opção Permite comprar este produto? desmarcada.

A quebra dos pedidos será feita por Meio de Transporte, uma vez que um pedido não pode ter mais de um Meio de Transporte. Serão gerados N pedidos, sendo um pedido para cada Meio de Transporte, de acordo com o que for cadastrado no Produto. Todos os produtos de um mesmo Meio de Transporte ficarão no mesmo pedido. Os produtos que não possuem Meio de Transporte ficarão no pedido cujo o meio de transporte é o definido no pop-up Parâmetros para Planejamento de Compra.

## Botão "Outras Opções..."

#### Pedidos Gerados

Esta opção mostra os pedidos de compra gerados a partir do planejamento de compras posicionado. Será aberto um popUp contendo uma grade com os pedidos gerados com duplo clique em alguma linha será lançado a Central de Compras com o pedido selecionado.

#### Modelos de Planejamento

Os modelos de planejamento são criados de forma a se agrupar produtos que compartilharão parâmetros semelhantes para a análise e formação de pedidos.  Um modelo de planejamento é semelhante à configuração de uma **"Matriz"** da rotina **"Análise de Giro"**.

Um modelo de planejamento serve como uma configuração padrão para novos planejamentos.

O cadastro dos modelos de planejamento de compra está na tela de planejamento de compras no menu de **"Outras opções > Modelos de planejamento"**.

Para o cadastro do modelo deve-se informar a descrição do modelo.

![clip0178](https://ajuda.sankhya.com.br/hc/article_attachments/360061003434)

**Filtro de Pedido de compra pendente/Filtro de Pedido de venda pendente:** A base da sugestão de compras leva em consideração o estoque atual, os pedidos de compra/venda pendentes. Opcionalmente pode-se usar um critério de filtragem para determinar quais os pedidos serão de fato considerados nessa conta.

**Filtro de Quantidade em estoque:** Esse filtro atua exclusivamente sobre a quantidade a ser apresentada na Coluna Estoque. Caso o usuário crie um Filtro para analisar o Giro apenas da Empresa X e queira ver o Estoque apenas desta mesma empresa, terá que colocar o Filtro nessa Opção e na Opção "Filtro de Produtos com Giro".

**Filtro de Produtos com Giro:** Permite definir filtros para a apresentação dos produtos que tiveram giro no período selecionado. Independente do filtro, só serão analisados produtos com marcação 'Ativo' e 'Permite comprar este produto?'.

**Filtro de Produtos sem Giro:** Permite com que o usuário defina os filtros para a apresentação dos produtos que NÃO tiveram giro no período selecionado. Independente do filtro só serão analisados produtos com marcação 'Ativo' e 'Permite comprar este produto?'

Incluir produtos sem estoque: Se habilitado, simula o cálculo para todos os produtos, independente de ter giro ou estoque. Esta opção só fica disponível se a opção ‘Incluir produto sem giro estiver marcada

**Qtd. períodos para GMD:** Quantidade de períodos para o cálculo do giro médio diário.

**Qtd. períodos para GMD recente:** Quantidade de períodos para o cálculo do giro médio diário recente.(Esta informação deve ser menor que a quantidade para GMD).

**Tamanho dos períodos de Giro:** Tamanho dos períodos para analise do giro. Neste campo existem as opções: diário, mensal e semanal; quando o usuário informar diário ira aparecer uma caixa de texto para informar a quantidade de dias que será considerado como 1 período, mensal o tamanho do período será de 1 mês e semanal de 1 semana.

**% Acréscimo na Sugestão de Compras:** Percentual adicionado na sugestão de compras.

**Meio de Transporte:** Meio de transporte utilizado na projeção.

## Parâmetros Envolvidos

O parâmetro **"Controla acesso para consolidador de giro? - CONTACESSCONSOL"**, quando ativado, irá liberar na tela **"Configurações > Controle de Acesso"**, o acesso especial **"Consolidação do giro"**. O usuário que possuir esta marcação efetuada em seus acessos, terá permissão para realização do **"Agendamento da geração da tabela de giro"**.

![clip0450](https://ajuda.sankhya.com.br/hc/article_attachments/360061003454)

Caso seja feita a tentativa de utilização do botão de **"Agendamento da geração da tabela de giro"**, por um usuário que não possui esta liberação em seus acessos, será apresentada a mensagem descrita abaixo:

![clip0451](https://ajuda.sankhya.com.br/hc/article_attachments/360061927473)

Caso o parâmetro esteja desabilitado, o comportamento do sistema em relação ao Agendamento da geração da tabela de giro, não será alterado.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112553-Planejamento-de-Compras#top)
