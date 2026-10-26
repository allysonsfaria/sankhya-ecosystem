---
id: "360050819554"
titulo: "Análise de Giro - Botões do topo da tela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:34:12Z"
rotulos: ["Produtos", "Configuração", "análise de giro", "br.com.sankhya.com.rotinas.analisegiro", "TOP", "Estoque", "USAPRODGENERICO", "Análise de Giro - Botões do topo da tela", "Botões Importantes", "Configuração da Matriz"]
---

# Análise de Giro - Botões do topo da tela

```
 Módulo: Comercial > Rotinas
```

---

Na parte superior da tela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673), são exibidos alguns botões relevantes para a geração da análise. Neste artigo tem-se as funcionalidades de cada um deles:

| Botões do topo da tela |
| --- |
| [Configuração da Matriz de Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro) |
| [Botão Processar Matriz](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3oprocessarmatriz) |
| [Botão Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3oseguran%C3%A7a) |
| [Botão Relatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3orelat%C3%B3rios) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) |

---

**Configuração da Matriz de Análise de Giro**

Para criar uma nova matriz, clique no botão  **"Criar nova configuração"**. Em seguida, será apresentada uma tela para inserir um título para o agendamento que está sendo criado.

![Imagem 1: Para criar uma nova matriz, clique no botão "Criar nova configuração" . Em seguida, será apresentada uma tela para…](https://ajuda.sankhya.com.br/hc/article_attachments/24826831971863)

Depois de informado o título desejado para a matriz, defina quais são períodos em que os giros serão calculados, sendo que essa definição pode ser realizada de dois modos:

(1)** Modo Avançado:** todas as configurações disponíveis da Análise de Giro estarão acessíveis.

(1)** Modo Guiado:** o sistema exibirá cada configuração com sua descrição e os impactos que ela pode causar. Este modo, possui 7 etapas e 3 seções. Ao clicar nas seções, será direcionado para a 1ª etapa correspondente a cada uma delas:

[GIF animado: Imagem 2: (1) Modo Guiado: o sistema exibirá cada configuração com sua descrição e os impactos que ela pode causar. Este modo,…](https://ajuda.sankhya.com.br/hc/article_attachments/4409676763799)

Para compor uma matriz de análise de giro, alguns critérios devem ser informados, configurando os cálculos e determinando quais informações serão importantes para o processo de compra. Esses critérios são estabelecidos pela interface de configuração e podem ser criadas várias combinações para se fazer análises distintas.

Como podem existir várias configurações, é necessário identificá-las informando o nome da matriz.

No pop-up de **"Configuração da Matriz de análise de giro"**, estão disponíveis as seguintes seções:

| [Períodos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#Per%C3%ADodos) |
| --- |
| [Estoque Mínimo e Sugestão de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#estoquem%C3%ADnimoesugest%C3%A3odecompra) |
| [Outras Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#outrasconfigura%C3%A7%C3%B5es) |

---

### Períodos

Informações referentes aos períodos determinam os ciclos de análise aos quais os produtos serão submetidos. Podem ser criados até doze períodos e eles podem ser dinâmicos, onde as datas serão calculadas durante o processamento da matriz. Assim, ao utilizar dois períodos de uma semana, por exemplo, o sistema determina automaticamente as datas de início e fim de cada semana retroativamente.

#### Tipo

Definindo os períodos como **"Dinâmicos"**, é possível estabelecer a quantidade e o intervalo de tempo que o sistema irá considerar para a busca retroativa das movimentações dos produtos. Considere o seguinte exemplo:

Ao configurar uma quantidade de três e um período de **"Mês/Meses"**, o sistema analisará, a partir da data atual (no momento em que clicar em [Processar Matriz](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3oprocessarmatriz)), os três últimos meses. Por exemplo, se a data atual for 01/03/2016, o sistema considerará os seguintes períodos para análise das movimentações:

- **1º Período:** 01/12/2015 a 31/12/2015
- **2º Período:** 01/01/2016 a 31/01/2016
- **3º Período:** 01/02/2016 a 29/02/2016

Os períodos também podem ser **"Fixos"**, definidos manualmente ou sugeridos pelo sistema. Para configurar períodos fixos, marque **"Adicionar"**, para definir a quantidade de períodos a serem acrescentadas, logo à frente, determine o **"Período"** desejado e clique em **"OK"** para carregar a quantidade de períodos solicitada. 

![Imagem 3: Os períodos também podem ser "Fixos" , definidos manualmente ou sugeridos pelo sistema. Para configurar períodos fixos,…](https://ajuda.sankhya.com.br/hc/article_attachments/4409676514199)

![Imagem 4: É importante entender como funciona o cálculo de períodos como "Bimestre" , "Trimestre" e "Semestre" . Independente da…](https://ajuda.sankhya.com.br/hc/article_attachments/31226454996887) É importante entender como funciona o cálculo de períodos como **"Bimestre"**, **"Trimestre"** e **"Semestre"**. Independente da configuração da opção **"Utiliza Períodos Fechados"** (marcada ou desmarcada), o sistema considera o dia anterior para calcular o giro (D-1). Isso significa que as movimentações feitas hoje só aparecem na tabela de giro a partir de amanhã.

Sobre o número de dias nos períodos, ao escolher períodos como bimestre, trimestre ou semestre, o sistema não usa um número fixo de dias. Isso acontece porque os meses têm durações diferentes. Observe alguns exemplos de bimestres:

- janeiro e fevereiro: 59 dias (ou 60 em anos bissextos);
- março e abril: 61 dias;
- julho e agosto: 62 dias.

Ou seja, um bimestre pode ter entre 59 e 62 dias, dependendo dos meses escolhidos.

A marcação **"Utilizar períodos fechados"** é utilizada quando se deseja que o cálculo do Giro seja feito considerando da primeira até a última data do período selecionado. Considere o exemplo abaixo para melhor entendimento:

**(1)** **Configurações:**

- Utilizar períodos fechados - marcada;
- Adicionar 3 Semana(s);
- Data Atual: 28/06/2017;

**(1)** **Serão sugeridos os seguintes períodos:**

- **1º Período:** 11/06/2017 a 17/06/2017
- **2º Período:** 18/06/2017 a 24/06/2017
- **3º Período:** 25/06/2017 a 27/06/2017

Ou seja, considera-se uma semana completa (de domingo à sábado); caso a semana ainda não tenha terminado, a data final será o dia anterior à data atual.

**(1)** **Configurações:**

- Utilizar períodos fechados - desmarcada;
- Adicionar 3 Semana(s);
- Data Atual: 28/06/2017;

**(1)Serão sugeridos os seguintes períodos:**

- **1º Período:** 07/06/2017 a 13/06/2017
- **2º Período:** 14/06/2017 a 20/06/2017
- **3º Período:** 21/06/2017 a 27/06/2017

Neste caso, a data atual menos um dia é utilizada para calcular retroativamente os períodos de sete dias (uma semana).

Ao uitlizar períodos Fixos, eles podem ser sugeridos pelo sistema (campo Adicionar, Período desejado, e clicando em OK) ou informados manualmente. Caso esses períodos não sejam preenchidos, ao processar a matriz, o sistema exibirá a mensagem de alerta:

**"Informe pelo menos um período"**

O campo **"Atualizar Última Venda"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) da tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), determina se um pedido ou venda refletirá nos dados **"Últ. Vnd"** e **"Qtd Venda"**. Quando esse campos está configurado, o pedido ou venda será utilizado para atualizar esses dados. Por exemplo, ao marcar essa opção para duas TOPs quaisquer e lançar alguns documentos, ao processar a matriz após a consolidação, ambos os documentos serão considerados para atualização dos dados Últ. Vnd e Qtd Venda.

Assim, é necessário configurar o campo Atualizar Última Venda nas TOP's. Vale ressaltar que a TOP é histórica; assim, para pedidos ou notas que já foram lançados, a alteração não terá efeito, a menos que haja alteração via banco e uma nova consolidação da matriz.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro)

### Estoque Mínimo e Sugestão de Compra

![Imagem 5: Estoque Mínimo e Sugestão de Compra](https://ajuda.sankhya.com.br/hc/article_attachments/4409676474519)

Se a marcação **"Período sem vendas influencia a média para estoque mínimo"** for efetuada, mesmo um período em que não houve vendas será considerado para a média de estoque mínimo. Por exemplo, ao definir três períodos semanais e não houver vendas na segunda semana, essa configuração determina se o volume de vendas das três semanas será dividido por dois ou por três para obter a média de estoque mínimo para esse produto.

A informação contida no campo **"Dias ÚTEIS para Estocagem"** influencia a sugestão de compra, determinando quantos dias tem o ciclo planejado. Por exemplo, se o giro médio de determinado produto é 10 unidades por dia e o planejamento é comprar o estoque para a semana (cinco dias úteis), então a sugestão será de 50 unidades (considerando que o estoque atual esteja zerado).

Além disso, há o parâmetro **"Somar o Lead Time aos dias Úteis para Estocagem - SOMALEADTIME"** que, quando acionado, o sistema soma o Lead Time cadastrado na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top) aos dias úteis para estocagem definidos neste campo. O cálculo da sugestão de compra será feito com base nessa soma.

Ainda sobre o parâmetro SOMALEADTIME, quando ligado, o sistema irá somar a coluna LEADTIME da tabela TGFGIR (cálculo apresentado abaixo) com o campo Dias ÚTEIS para Estocagem. Quando desligado, o sistema verificará se a coluna LEADTIME da tabela TGFGIR contém um valor maior que zero. Se sim, utilizará este valor desconsiderando os Dias ÚTEIS para estocagem. Se não, o valor do campo é utilizado no cálculo da sugestão de compra.

O cálculo para Lead Time na tabela TGFGIR ocorre da seguinte forma:

**(1)** **Produtos com Giro:** ao calcular o giro dos produtos, a TGFGIR recebe na coluna LEADTIME ("Lead Time"), de acordo com a opção configurada no campo **"Apresentar resultado por"** da seção [Outras configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#outrasconfigura%C3%A7%C3%B5es). Isto é:

- **Empresa:** se o campo **"Lead time de compra"** da TGFPEM estiver preenchido (aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) do Cadastro de Produtos), utiliza essa informação; caso não exista, utiliza Lead time de compra do produto (aba Medidas e estoque, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque)).
- **Matriz:** mesmo comportamento da opção Empresa, porém utiliza a empresa matriz.
- **Produto:** busca a informação diretamente do campo Lead time de compra do Cadastro de Produtos (aba Medidas e estoque, sub-aba Estoque).

**(1)** **Produtos sem Giro:** a informação é selecionada diretamente do campo Lead time de compra do Cadastro de Produtos (aba Medidas e estoque, sub-aba Estoque).

O campo **"% Acréscimo na sugestão de compras"** é utilizado como uma margem de acréscimo na Sugestão. Levando em consideração o exemplo do campo Dias ÚTEIS para estocagem, caso o valor seja 10%, a sugestão será de 55 unidades.

Quando a marcação **"Não atualizar estoque mínimo quando a sugestão for zero"** estiver realizada, ao clicar em [Alterar Estoque Mínimo nos Cadastro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#alterarestoquem%C3%ADnimonoscadastros) do botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), caso o valor da coluna Est.Mín.Sug for zero o sistema não atualizará o campo **"Estoque Mínimo"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Medidas e Estoque sub-aba Estoque.

Com a marcação **"Desconsiderar período de ruptura do cálculo de Giro Médio Diário?"** efetuada, os dias úteis em que o produto esteve sem saldo no período avaliado não serão considerados no cálculo de giro médio diário. Desse modo, esse cálculo refletirá nos campos Estoque Mínimo Sugerido, Sugestão de Compra Giro, Duração do Estoque e Duração do Estoque Após compra que, apresentarão resultados condizentes com a real necessidade de reposição do produto.

#### Desprezar período de giro

Por meio das marcações **"Desprezar o período de maior giro?"** e **"Desprezar o período de menor giro?"** é possível retirar, respectivamente, o maior e o menor período de giro. Deste modo, após o processamento da análise de giro será apresentada a sugestão de compra desprezando o período conforme as marcações realizadas.

#### Filtros

A marcação **"Desconsiderar pedidos pendentes na sugestão de compra?"** quando realizada, bloqueia os filtros **"Pedido de compra pendente"** e **"Pedido de venda pendente"** (campos a seguir). Ao processar a matriz, serão considerados os pedidos de compra e venda confirmados, exceto os que o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top) estiver com a opção **"Orçamento"** marcada, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

A base da sugestão de compras leva em consideração o estoque atual, os pedidos de compra/venda pendentes. Opcionalmente, pode-se usar um critério de filtragem por meio dos filtros **"Pedido de compra pendente"** e **"Pedido de venda pendente"** para determinar quais os pedidos serão de fato considerados nessa conta.

O filtro **"Quantidade em estoque"** atua exclusivamente sobre a quantidade a ser apresentada na coluna Estoque. Caso seja necessário analisar o Giro da Empresa X e visualizar o Estoque dessa mesma empresa, é necessário aplicar o filtro tanto na opção Quantidade em estoque quanto na opção **"Filtro de Produtos com Giro"**.

Para que o filtro Quantidade em estoque seja considerado na Análise de Giro, os produtos precisam ter giro no período.

---

**![Imagem 6: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/24845522057495) Informações adicionais:**

- Caso não seja informado nenhum dos filtros acima, o sistema irá considerar os pedidos de compra e vendas pendentes;
- Nos casos em que é necessário que o sistema considere as notas de entrega futura, utilize o filtro CabecalhoNota->TIPMOV = 'V';
- Para que as notas de venda sejam consideradas como pendentes, é necessário que, no ato do lançamento, as mesmas não sejam confirmadas e que o Tipo de Operação - TOP utilizado esteja configurado para Atualizar Estoq. a partir da Confirmação (aba Geral). Diante disto, em um lançamento de uma nota utilizando o movimento de venda (TIPMOV = 'V') ao proceder com sua confirmação, este não será considerado como pendente;
- Uma vez que as notas de venda futuras não possuem provisão, estas não são consideradas como pendentes, mas sim, como confirmadas.
- É necessário definir nos filtros desta aba o período desejado para observar os pedidos de venda ou compras pendentes. Caso estes filtros não sejam configurados, o sistema considerará um período inferior a 180 dias.

---

![Imagem 7: Acesse também: Campos para Análise de Giro .](https://ajuda.sankhya.com.br/hc/article_attachments/20410321679255) Acesse também: [Campos para Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro)

### Outras configurações

![Imagem 8: Outras configurações](https://ajuda.sankhya.com.br/hc/article_attachments/6217762072599)

Quando a marcação **"Incluir produtos sem giro"**estiver habilitada, o sistema irá simular o cálculo também para os produtos em estoque que não têm giro.

Ao ativar a marcação **"Incluir produtos sem estoque"**, o cálculo é simulado para todos os produtos, independente de terem giro ou estoque. Esta marcação só fica disponível se a marcação Incluir produto sem giro estiver marcada.

Com a marcação **"Usar Unidade de Compra?"** ativada, será utilizada a Unidade de Compra na Matriz. Importante ressaltar que, ao acionar esta marcação, as unidades adicionais devem estar com o campo **"Decimais para quantidade"** preenchido na aba **"Geral"** do cadastro de [Unidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597094-Unidades).

Quando a marcação **"Agrupar movimentação produto alternativo"** estiver ligada, a movimentação dos produtos relacionados como **"alternativos"** será agrupada para o produto com código numérico menor. Para isso, cadastre previamente os produtos alternativos através do Cadastro de Produtos, aba **"Produtos Alternativos"**. Considere o exemplo abaixo: 

- Produto 001 tem alternativos 010 e 015;
- Produto 002 tem alternativos 020 e 001;
- Produto 030 tem alternativos 025 e 001;

Neste caso, uma movimentação para um dos produtos: 001, 010, 015, 002 ou 030, será agrupada no produto 001.

![Imagem 9: Se os leadtimes do produto alternativo e do principal (o agrupador) forem diferentes, o sistema utilizará o do…](https://ajuda.sankhya.com.br/hc/article_attachments/35775300707863)Se os leadtimes do produto alternativo e do principal (o agrupador) forem diferentes, o sistema utilizará o do principal.

**(2)**O campo **"Tipo de Agrupamento"** apresenta as seguintes opções para configurar a consolidação (agrupamento) dos produtos a serem exibidos na análise de giro:

- **Nenhum:** não haverá nenhuma consolidação (agrupamento) na análise de giro;
- **Produto alternativo:** essa opção corresponde as informações relatadas na marcação Agrupar movimentação produto alternativo descrita anteriormente;
- **Produto genérico:** a análise de giro considerará o produto genérico e consolidará os produtos reais (específicos) vinculados a ele. É necessário cadastrar os produtos específicos no Cadastro de Produtos, aba [Produtos Específicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosespecficos).

**Observação:** o campo Tipo agrupamento será exibido quando o parâmetro **"Usa produtos genéricos?-USAPRODGENERICO"** estiver ligado. Sendo que, ao habilitar o referido parâmetro, a marcação Agrupar movimentação produto alternativo não será apresentada.

**(2)**O campo **"Tabela de preço"** permite buscar o preço com base na última atualização da tabela informada.

**(2)**Por meio do campo **"Considerar custo"** é possível determinar o Custo da Mercadoria Vendida (CMV) para análises que utilizam esse indicador. O custo variável é o mais indicado, pois ele está livre dos gastos variáveis das vendas e da participação no gasto fixo. Este campo possui as seguintes opções:

- Reposição;
- Gerencial;
- Variável;
- Médio com ICMS;
- Médio sem ICMS;
- Sem ICMS;
- Com ICMS.

**Observação:** na grade de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradeprodutos), a coluna de Custo será nomeada de acordo com a opção selecionada no campo Considerar custo. Por exemplo, se a opção Variável for escolhida, a coluna será nomeada como **"Custo Variável"**. Se a opção Reposição for selecionada, a coluna será nomeada como **"Custo Reposição"**.

**(2)**O campo **"Detalhar de acordo com"** define a forma de agrupamento na análise, conforme as opções:

- Produto;
- Grupo de produto;
- Marca;
- Empresa.

Esta totalização é uma forma de quebra ou agrupamento para as análises verticais. Ao selecionar por Marca, por exemplo, serão apresentados todos os produtos da Marca A, depois os da Marca B, e assim por diante. Os percentuais de análise vertical mostrarão a representatividade daquele produto dentro da movimentação daquela marca.

Ao selecionar por Produto, será feita a análise global do Cadastro de Produtos sem nenhum tipo de agrupamento ou quebra, ou seja, serão apresentados todos os produtos da empresa (respeitando os Filtros) e os percentuais de análise vertical mostrarão a representatividade daquele produto dentro da movimentação total da(s) empresa(s). A ordenação por produto não é recomendada para empresas que trabalham com produtos muito distintos, pois a comparação se tornará inviável.

A marcação **"Listar pedidos na aba Compras/Vendas Pendentes"** quando habilitada, faz com que o sistema guarde analiticamente os lançamentos que compõem os valores de Compras e Vendas Pendentes, permitindo desse modo, a consulta detalhada desta informação na aba [Compras/Vendas Pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abacomprasvendaspendentes). 

**(2)**O campo **"Apresentar resultado por"** define a forma de apresentação dos produtos, conforme as opções:

- Empresa;
- Matriz;
- Local;
- Controle.

Entenda o comportamento do Sankhya OM ao usar a opção "**Apresentar resultado por: Empresa**":

- **Produto sem movimentação:** se um produto ainda não teve giro, o sistema exibe o valor '0' na coluna **Empresa**.
- **Produto com movimentação:** a partir da primeira movimentação você visualiza a empresa que realizou o giro e o sistema omite as demais.
- **Movimentação em múltiplas empresas:** se o mesmo produto tiver movimentação em duas empresas distintas, você verá duas linhas para ele no resultado, uma para cada empresa.

Para otimizar sua consulta, crie uma matriz para cada empresa e aplique filtros específicos para produtos com e sem giro:

- **Para produtos sem giro:** usar (EST1.CODEMP = X)
- **Para produtos sem giro e sem estoque:** usar (NVL(ITE.CODEMP, X) = X)

Se houver movimentação para duas empresas distintas, serão apresentadas duas linhas para o mesmo produto, uma para cada empresa. Da mesma forma ocorrerá com **Local** e **Controle**.

Se além da opção **Empresa**, estiver marcada também a opção **Matriz**, o código da matriz será usado e todas as empresas que tem aquela empresa como matriz, serão agrupadas em apenas uma linha cuja empresa será a matriz.

As opções **Local** e **Controle** são habilitadas e desabilitadas pelos parâmetros **"Utiliza a coluna Local para controlar o estoque-UTILIZALOCAL"** e **"Utiliza a coluna Controle para controlar o estoque-UTILIZACONTROLE"**, e o parâmetro **"Descrição para Local-DESCRLOCAL"** definirá a descrição do campo **"Local"**.

**Observação:** para processar uma Matriz de Análise de Giro obtendo o resultado por **Empresa**, habilite o parâmetro **"Considerar os dias úteis (Lead Time) da Anál. Giro. - CONSDIASUTEIS"** e marque somente a opção **Empresa**, no campo **Apresentar resultado por**.

#### Filtros

Nesta seção, é possível refinar a visibilidade dos produtos na grade de análise através dos seguintes filtros:

- **Produtos com Giro:** permite definir filtros para a apresentação dos produtos que tiveram giro no período selecionado.
- **Produtos sem Giro:** permite definir filtros para a apresentação dos produtos que não tiveram giro no período selecionado, independentemente de possuírem estoque.
- **Produtos sem Giro e sem estoque:** permite definir filtros para a apresentação dos produtos que não tiveram giro no período selecionado e que também não possuem estoque.

> **Informações Técnicas sobre a Filtragem:**
>
> - **Hierarquia de Processamento:** o sistema processa inicialmente os produtos sem giro e, posteriormente, os produtos sem giro e sem estoque. Dessa forma, itens já contemplados no primeiro filtro não são reavaliados no segundo, o que pode impactar a exibição dos resultados se os filtros forem utilizados de forma independente.
> - **Independência da Coluna de Estoque:** a existência de um filtro para trazer movimentações de uma empresa específica nestas opções não obriga a coluna **Estoque** a respeitá-lo. O cálculo da referida coluna depende exclusivamente dos filtros aplicados no campo **Quantidade em Estoque**.
> - **Filtragem por Empresa específica:** caso seja necessário apresentar resultados de apenas uma determinada empresa, utilize a sintaxe abaixo nos filtros correspondentes:
>
>   - ![Marcador 1] **Produtos sem Giro** = `EST1.CODEMP = "X"`
>   - ![Marcador 1] **Produtos sem Giro e sem estoque** = `PEM.CODEMP = "X"`
>   - ![Marcador 2] Onde **"X"** representa o código da empresa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

## Botão Processar Matriz

O botão ![Imagem 10: O botão "Processar Matriz" é responsável por iniciar o encadeamento dos dados seguindo os filtros formulados,…](https://ajuda.sankhya.com.br/hc/article_attachments/10266681541399) **"Processar Matriz"** é responsável por iniciar o encadeamento dos dados seguindo os filtros formulados, apresentando-os na grade principal. Este botão está presente no canto superior direito da tela, e também no pop-up [Configuração da Matriz de análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro).

Ao acioná-lo, será aberto o pop-up **"Processos"** onde será apresentado o andamento da geração da matriz:

[GIF animado: Imagem 11: Ao acioná-lo, será aberto o pop-up "Processos" onde será apresentado o andamento da geração da matriz:](https://ajuda.sankhya.com.br/hc/article_attachments/4409676708759)

Além disso, anexado ao botão Processar Matriz, há a seta ![Imagem 12: Além disso, anexado ao botão Processar Matriz , há a seta em que, ao clicá-la, será exibida a opção "Exibir o histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/10266717623959) em que, ao clicá-la, será exibida a opção **"Exibir o histórico do processamento"** e, logo em seguida, o pop-up **"Processos"**, onde é possível consultar as informações referentes às datas e horários dos últimos processamentos da matriz.

Dessa forma, pode-se verificar se os dados exibidos na tela estão atualizados, evitando o reprocessamento desnecessário.

[GIF animado: Imagem 13: Dessa forma, pode-se verificar se os dados exibidos na tela estão atualizados, evitando o reprocessamento desnecessário.](https://ajuda.sankhya.com.br/hc/article_attachments/10267390666519)

Por meio do botão  **"Ver histórico"**, consulte a relação de todos os processos já executados e as informações pertinentes ao mesmos, bem como, os processos que estiverem em execução no momento da consulta.

Na parte superior do referido pop-up, são disponibilizados alguns botões que executam funções relevantes para as informações aqui apresentadas. Abaixo, falaremos sobre cada um deles:

**Atualizar:** possibilita renovar as informações apresentadas no pop-up.

**Excluir processo antigo:** pode-se eliminar o processo que está selecionado.

**Excluir todos os processos:** executa-se a eliminação de todos os processos antigos (finalizados) permanecendo apenas aqueles que se encontrem em execução.

**Observação:** o parâmetro **"Processar matriz antes de aplicar? - PROCMATRIZAPL"** por padrão é desligado. Quando ligado, caso você clique no botão **"Aplicar"** do filtro personalizado, fará com que o sistema processe a matriz selecionada antes de efetivamente aplicar o filtro. Consideramos ainda que, ao abrir a tela, os produtos são carregados automaticamente, nesse primeiro carregamento, a matriz não é executada antes da apresentação dos dados, são apresentados os produtos do processamento anterior.

**Nota:** Referente ao processamento da Matriz da análise de giro, nós temos o parâmetro **"Log na consolidação do giro? - LOGCONSOLIDACAO"** que, ao ligá-lo, ao realizar download do log do sistema na Administração do Servidor, informações sobre o tempo de execução e filtros utilizados em cada procedure do processamento da matriz de giro serão exibidos no log gerado.

Uma vez configurada a Matriz temos:

### Visão "Produtos" Imagem 14: Visão "Produtos"

![Imagem 15: Visão "Produtos"](https://ajuda.sankhya.com.br/hc/article_attachments/4409681816983)

A configuração da grade de produtos da matriz de análise de giro funcionará da mesma forma que as outras grades do sistema, basta utilizar o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15665244482967) **"Configurar Grade"**  para selecionar quais colunas deverão aparecer na grade, a ordem das colunas e sua ordenação.

**Nota:** Ao adicionar determinados campos na grade, por meio da opção **"Configuração da Grade"** em **"Informações por Período"**, estes campos serão exibidos também na grade **"Produtos"**, além dos campos configurados como visíveis. Se você não quiser que alguns campos não sejam exibidos na exportação para .xls, estes deverão ser ocultados na Configuração de Grade da grade Informações por período. Sendo assim, pode-se destacar o exemplo:

Caso você não queira que a coluna **"Acumulador Margem"** seja exportada para .xls ou fique indisponível para visualização, oculte-o na Configuração de Grade em Informações por Período.

Tem-se ainda a coluna **"Ruptura Estoque (Qtd. dias)"** do painel superior que irá apresentar a soma da quantidade de dias de indisponibilidade de todos os períodos.

**Observação:** quando a marcação **"Calcular Ruptura de Estoque?"** da aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo) for acionada, o sistema irá registrar diariamente se o produto da empresa finalizou o dia com o saldo zerado.

**Observação:** com o parâmetro **"Deduzir reserva do estoque na Análise de Giro - DEDUZIRRESESTAN"** ligado, se o produto selecionado possuir no campo **"Reservado"** da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaestoque) do [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), uma quantidade maior ou igual ao saldo atual do campo **"Estoque"** (aba Estoque, tela Cadastro de Produtos), o sistema irá considerar que esse produto está em ruptura e apresentará a quantidade de dias de indisponibilidade na coluna **"Dias sem Saldo"**. Porém, com o parâmetro desligado e o produto com estoque maior que zero, além do campo Reservado maior ou igual ao saldo atual do campo Estoque, o sistema não irá considerar a reserva e a coluna Dias sem saldo ficará vazio.

**Importante:** o parâmetro DEDUZIRRESESTAN quando ativado, fará a subtração da reserva do estoque na coluna Estoque na Análise de Giro. Ao ser desativado, a coluna Estoque será composta apenas pelo saldo atual de estoque, sem subtrair a reserva.

Além disso, na coluna **"Dias sem saldo"** da aba **"Informações por período"** do painel inferior, será exibida a quantidade de dias de indisponibilidade a cada período.

**Grade de Produtos**: Énesta grade que as informações geradas pela Análise de Giro estarão disponíveis, esta grade apresenta campos que são indicadores para a análise dos Gestores, como: Código e Descrição do Produto, o Estoque, Custo de Venda Unitário, Custo de Venda Total, Sugestão De Compra, Sugestão Compra Giro e etc.

No campo ![Imagem 17: No campo "Buscar" você localizará o produto em que deseja que a seleção seja contextualizada. Além disso, ao clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/4402883206807) **"Buscar"** você localizará o produto em que deseja que a seleção seja contextualizada. Além disso, ao clicar no link Buscar será possível definir os critérios de localização dos produtos que serão considerados pelo sistema.

Ao acioná-lo o pop-up **"Configurar a caixa de busca"** será exibido, e assim, os campos selecionados serão considerados sempre que uma pesquisa por produto for efetuada. Dessa forma, consideraremos o exemplo:

Ao pesquisar um Produto, o critério de busca **"Produto"** deverá ser selecionado, logo, teremos:

![Imagem 18: Ao pesquisar um Produto, o critério de busca "Produto" deverá ser selecionado, logo, teremos:](https://ajuda.sankhya.com.br/hc/article_attachments/4409676676759)

Além da marcação **"Agrupar por família"**, que quando selecionada, fará um filtro na tela para os produtos que fazem parte de uma família, apenas na relação Pai e Filho, de acordo com o que for cadastrado na tela Cadastro de Produtos, aba [Família](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abafamlia).

Ao lado marcação mencionada acima, temos a marcação **"Esconder informações de período"** presente no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15665291856023) **"Outras opções..."** em que, quando você habilitá-la, o sistema ocultará as colunas referentes às informações por período.

#### Modificação na Sugestão de Compras

Depois que a análise de giro é gerada, analisada e seus pedidos de compra são sugeridos, há a possibilidade de escolha e/ou remoção de itens a serem gerados nos Pedidos de compra.Vejamos um exemplo:

Quando se trabalha com um determinado produto e sua compra é encerrada, o mesmo continua a ser vendido até finalizar seu estoque. Sendo assim, no Cadastro do Produto é efetuada a marcação da opção **"Permite Comprar este produto?"** em sua aba **"Geral"**. Deste modo, caracteriza-se que é proibido comprar o produto e só depois de finalizar o estoque do mesmo que este será efetivamente inativado.

A matriz de giro não reconhece a informação de "proibido comprar" dos produtos e os mesmos são demonstrados na análise de giro, pelo fato de se tratar de uma informação válida para a análise do comprador que pode estar analisando informações passadas para decidir como, por exemplo, sobre um produto substituto. Deste modo, os produtos configurados com a referida marcação não poderão ser comprados. Na hipótese de se tentar gerar o pedido será exibida a mensagem abaixo:

**"Produto: X - Xxxxxx não está permitido para compra."**

É necessário a utilização do **"Assistente de Filtros"** para criação de filtros específicos que serão utilizados na identificação e assim retirada desses produtos da análise de giro, para evitar o bloqueio do pedido de compra.

Após as alterações, basta gerar o pedido de compra e conferi-lo no Portal de Compras, assim, na aba **"Pedidos"** da Análise de Giro, clique no botão **"Preferências"**. Pode-se observar que os fornecedores estarão indicados na tela, preencha os campos obrigatórios e efetuar a marcação **"Lista única de produtos"**. Após esses procedimentos, clique em **"OK"**; assim, a tela será reposicionada para a lista de produtos e fornecedores.

A marcação **"Usar empresa de negociação no cabeçalho da nota?:"** será habilitada quando, nas configurações da matriz, o campo Apresentar resultado por: Empresa estiver desmarcado. Assim, você poderá informar a empresa à qual deseja que o Pedido de Compras seja criado.

Ainda na aba Pedidos, acione o botão **"Gerar Pedido"**, assim somente os itens da lista serão gerados nos pedidos de compra de acordo com seus respectivos fornecedores.

Os campos **"Fornecedor Preferencial"**, **"Sugestão Compra"** e **"Custo Gerencial"**, desta grade, poderão ser alterados, mesmo após a geração dos dados, bastando dar um duplo-clique na linha do produto que se deseja alterar e uma tela trará os campos para que possam ser inseridos/modificados.

O campo **"Sug.Compra Giro Ajustado"** será calculado quando as grades da tela forem carregadas, ou o campo **"Sug. Compra Giro"** for alterado. Este campo (Sug.Compra Giro Ajustado) será calculado da seguinte forma:

- Inicialmente, a Sug.Compra Giro Ajustado é igual a Sug.Compra Giro;
- Obtêm-se o Estoque Final após a Sugestão de Compra:

Estoque Final = Estoque Atual + Pedidos Compra Pendentes - Pedidos de Venda Pendente + Sug.Compra Giro

- Avalia-se o Estoque Final em relação ao Estoque Mínimo e Estoque Máximo do Produto de forma a evitar que o Estoque Final seja menor que o Estoque Mínimo ou maior que o Estoque Máximo.

Se Estoque Final < Estoque Mínimo: Sug.Compra Giro Ajustado = Sug.Compra Giro + (Estoque Minimo - Estoque Final)

Se Estoque Final > Estoque Máximo: Sug.Compra Giro Ajustado = Sug.Compra Giro - (Estoque Final - Estoque Máximo), se negativo zerar.

Caso o valor no campo Sug. Compra Giro seja diferente do valor do campo Sug.Compra Giro Ajustado, o campo **"Sugestão de giro ajustado?"** terá o valor Sim; do contrário, terá valor Não.

Ao carregar a matriz de Análise de Giro, serão apresentadas várias linhas para os produtos. Nessas linhas, serão exibidos os produtos que você poderá interpretar a partir das cores exibidas, sendo que, você pode consultar a legenda das cores no botão **"Legenda de Cores"**. Observe:

- **Vermelho:** Produto sem giro
- **Preto:** Produto com giro
- **Azul:** Produto com sugestão de compra ajustada

O giro do produto é calculado pelo sistema e apresentado nos campos **"Qtd Venda"** (VLRVENDA). O ajuste da sugestão de compras pode ser percebido a partir do campo **"Sugestão de giro ajustado?"** (TEMSUGGIROAJUSTADO) que recebe valor Sim e o campo **"Sug.Compra Giro Ajustado"** (SUGCOMPRAGIRAJUSTADO) recebe o valor calculado de forma ajustada. Para maiores detalhes do ajuste consultar a documentação do campo descrita acima.

### Visão "Pedidos" Imagem 20: Visão "Pedidos"

![Imagem 21: Visão "Pedidos"](https://ajuda.sankhya.com.br/hc/article_attachments/4402868863255)

**Grade de Resumo por Fornecedor/Pedido:** Nesta grade, cada linha representará [fornecedor x pedido]\*, estes fornecedores que aparecerão aqui são os que foram escolhidos através da tela descrita na visão de produtos (ao dar duplo-clique na linha do produto). Esta grade também trará informações como o Número único do pedido (se ele já tiver sido gerado) e seu valor total.

**Nota:** Caso tenhamos mais de um pedido para um mesmo fornecedor, então teremos 2 linhas nesta grade, diferenciando apenas a coluna Pedido.

**Painel de detalhes do pedido:** Após gerar um pedido, o sistema mostrará alguns detalhes sobre o pedido gerado, como o Fornecedor, Valor do Pedido, Transportadora, Valor do frete, Vencimento do frete e Previsão de entrega. Além disso, tem-se três botões, e uma caixa com três opções de escolha:

![Imagem 22: Painel de detalhes do pedido: Após gerar um pedido, o sistema mostrará alguns detalhes sobre o pedido gerado, como o…](https://ajuda.sankhya.com.br/hc/article_attachments/4402883233303)

Para compor o pedido, o sistema irá utilizar o valor dos campos conforme a opção escolhida. Por exemplo, sendo escolhida a opção Sug. Compra Giro, os valores contidos neste campo, irão compor a quantidade solicitada no pedido.

Então, caso o produto deste possua o valor **"Multipl. Compra"** preenchido, os campos de compra sugeridos serão substituídos pelos seus equivalentes, sendo eles:

- **"Sug. Compra"** = **"Sug. Compra Mult. Cpa"**;
- **"Sug. Compra Giro"** = **"Sug. Compra Giro Mult. Cpa"**;
- **"Sug. Compra Giro Ajustado"** = **"Sug. Compra Giro Ajustado Mult. Cpa"**.

![Imagem 23: Para mais informações referente ao Multipl. Compra , acesse o artigo Campos para Análise de Giro .](https://ajuda.sankhya.com.br/hc/article_attachments/20410321679255) Para mais informações referente ao Multipl. Compra, acesse o artigo [Campos para Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradeprodutos).

Depois de escolhida a opção Sug. Compra Giro e solicitar a geração do pedido, a quantidade pode ser visualizada no pedido gerado.

#### Gerar pedido e Preferências

Por meio do botão ![Gerar](https://ajuda.sankhya.com.br/hc/article_attachments/15665347090199) **"Gerar Pedido"**, realize o lançamento dos Pedidos de Compra com os produtos da grade **"Itens"** para o parceiro informado na grade **"Resumo por Fornecedor/Pedido"**. Sendo que, os demais dados do pedido serão configurados no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15665288918807) **"Preferências"**.

Ao clicar no botão Preferências, o pop-up **"Preferências do Lançamento de Pedidos"** será exibido. Nele, serão informados os campos que irão compor os pedidos de compra a serem gerados. Ao configurar o [Tipo de operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), atente-se à necessidade de existir uma TOP de Pedido de Compra. Na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), a **"Base numeração"** não poderá ser do tipo **"Manual (Informada pelo usuário)"**, geralmente, utiliza-se Pedido de Compra.

![Imagem 26: Ao clicar no botão Preferências , o pop-up "Preferências do Lançamento de Pedidos" será exibido. Nele, serão informados…](https://ajuda.sankhya.com.br/hc/article_attachments/4402883277975)

Quando a marcação **"Definir preferências na geração do pedido"** for habilitada, todos os demais campos disponíveis no pop-up, com exceção da marcação **"Lista Única de Produtos"**, ficarão indisponíveis para preenchimento, uma vez que a definição deles será realizada na geração do pedido, ao clicar no botão Gerar Pedido.

[GIF animado: Imagem 27: Quando a marcação "Definir preferências na geração do pedido" for habilitada, todos os demais campos disponíveis no…](https://ajuda.sankhya.com.br/hc/article_attachments/4402883271831)

Com a marcação **"Usar custo da TOP"** efetuada, o custo do pedido será calculado conforme a opção selecionada no campo **"Usar como preço"** do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral). Mas, quando desativada, o custo será baseado no valor do **"Custo de Reposição"** da [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673).

Caso seja habilitada a marcação **"Confirmar pedido"**, o pedido realizado na Análise de Giro já será lançado como confirmado na Central de Notas.

Quando o Pedido de Compras for lançado, o sistema guardará as informações o pop-up Preferências do lançamento de pedidos para as próximas transações, com exceção dos campos **"Valor do frete"**, **"Vencimento do Frete"**, **"Previsão de entrega"** e **"Observação do pedido"**.

Assim, o Pedido de Compra será gerado com base do campo **"Sugestão de Compra"**. Para utilização deste botão é necessário que o usuário logado tenha acesso à inclusão de pedidos de compra.

**(1)** **Cotação**

Além disso, estando no modo de visão Cotação, ao acionar o botão Preferências teremos a exibição do pop-up **"Preferências do lançamento de cotações"**, onde serão informados os campos que irão compor a cotação.

[GIF animado: Imagem 28: Além disso, estando no modo de visão Cotação , ao acionar o botão Preferências teremos a exibição do pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/4402886769303)

Teremos a possibilidade de gerar a cotação com o preço de compra já preenchido de acordo com a tabela de preço do fornecedor do produto, para tanto se faz necessário analisar os seguintes pontos:

**1)** **Configurar os parâmetros:**

**Meses p/ 'Já cotou' Análise giro->Gerar Cotação – QTDMESESJACOTOU:** Esse parâmetro limita a busca das cotações para um número "X" de meses anteriores ao momento da pesquisa. O seu valor padrão é 12 meses e o dia inicial sempre será o primeiro dia do mês, então se a geração da cotação for efetuada no dia 21/06/2018 a data inicial da busca será 01/06/2018;

**Meses p/ 'Já forneceu' Análise giro->Gerar Cotação – QTDMESESJAFORNE:** O comportamento deste parâmetro é semelhante ao do parâmetro anterior, porém ele efetua a busca por notas de compra;

**Precificação automática Cotação tab. Fornecedor? - PRECCOTINCLUSAO:** Este parâmetro quando habilitado, determinará que a cotação será incluída já com o preço especificado pela tabela de preço do fornecedor.

**2)** Após configurar os respectivos parâmetros, no pop-up Preferências do lançamento de pedidos apresentado na imagem acima, utilize as seguintes marcações para determinar o preço de compra do produto que será aplicado na cotação:

- **Fornecedor preferencial:** Através desta marcação, será gerada a cotação para os parceiros configurados como fornecedor preferencial no Cadastro do Produto, aba **"Geral"**, campo **"Parceiro Fornecedor preferencial"**;
- **Fornecedor com perfil de consumo:** Com esta marcação tem-se a geração da cotação para os fornecedores que contenham um perfil de consumo principal definido para o produto ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), campo **"Perfil Principal"**) ou um perfil secundário (Cadastro de Parceiros, aba [Perfil do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaperfildoparceiro), campo **"Perfil"**);
- **Quem já cotou antes:** Utilizando esta marcação, a cotação será gerada para os fornecedores que já efetuaram cotações deste produto dentro do período configurado no parâmetro de chave QTDMESESJACOTOU;
- **Quem já forneceu antes:** Quando acionada esta opção, gera-se a cotação para os fornecedores que já forneceram o produto dentro do período configurado no parâmetro de chave QTDMESESJAFORNE.

Assim, ao realizar as configurações descritas acima, a cotação será gerada com o preço de compra preenchido automaticamente de acordo com o fornecedor do produto.

#### Visualizar pedido

Após a geração do pedido, basta selecionar a linha na grade de Fornecedor/Pedido e clicar no botão ![Imagem 29: Após a geração do pedido, basta selecionar a linha na grade de Fornecedor/Pedido e clicar no botão para que o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/360097388493) para que o sistema abra a Central de Compras do pedido gerado, sendo possível dar andamento no pedido. É necessário que o usuário logado tenha acesso à consulta de pedidos de compra para que possa visualizar os pedidos gerados pela Matriz de Análise de Giro.

#### Excluir pedido

O botão ![Imagem 30: O botão será disponibilizado quando o pedido em questão já foi gerado, desta forma, você poderá realizar a exclusão do…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001327521) será disponibilizado quando o pedido em questão já foi gerado, desta forma, você poderá realizar a exclusão do pedido de compra. caso possua a opção **"Excluir"** na tela de Acessos para Pedidos habilitado para o seu usuário.

**Observação:** Para que seja possível um usuário realizar a exclusão de um pedido, este deverá possuir a opção **"Excluir"** da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854) do **"Pedido"** habilitada para si.

#### Grade de Itens

Nesta grade estarão todos os produtos da grade Produtos da visão de produtos exceto os produtos que já tiveram pedidos gerados, é possível também visualizar os itens de um pedido já gerado (selecionando o pedido na grade Fornecedor/Pedido), além disso, antes da geração do pedido é possível modificar a Transportadora, Sugestão de Compra e Custo Gerencial por esta grade, basta dar duplo-clique na linha, funcionará da mesma forma como explicado anteriormente na grade Produtos da visão de produtos.

**Observação:** Na edição de itens e produtos, o campo Sug.Compra Giro pode ser editado por você, porém, caso seja alterado, o sistema marcará em um novo campo **"Sug. Compra Giro Alterado"** que o valor foi alterado manualmente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

**Botão Segurança**

```
 Esta rotina estará disponível a partir da versão 4.12 do sistema.
```

O botão ![Imagem 31: O botão "Segurança" será apresentado quando o parâmetro "Controla acesso por matriz de análise de giro? - CONTACESSMAT"…](https://ajuda.sankhya.com.br/hc/article_attachments/5320188844311) **"Segurança"** será apresentado quando o parâmetro **"Controla acesso por matriz de análise de giro? - CONTACESSMAT"** estiver ligado, ao aciona-lo, o sistema abrirá o pop-up **"Controle de Acessos da Matriz de Análise de Giro - xxxx"** onde você irá observar os Grupos de Usuário, e abaixo, os Usuários que fazem parte desse grupo, para que possa controlar aqueles que terão acesso e definir as permissões de cada usuário.

![Imagem 32: O botão "Segurança" será apresentado quando o parâmetro "Controla acesso por matriz de análise de giro? - CONTACESSMAT"…](https://ajuda.sankhya.com.br/hc/article_attachments/5320726216727)

Observe a seguir, como funciona o processo descrito:

- Os usuários SUP não terão restrições de visualização, edição ou remoção de qualquer matriz cadastrada;
- Para aqueles usuários que são donos da matriz, será dado total acesso à sua própria matriz, ou seja, também poderão conceder acessos a ela para outros grupos e/ou usuários para executar as mesmas ações, ou conforme autorizações concedidas;
- Se o grupo possuir os acessos para a matriz, sem que o dono dela realize alguma restrição ao grupo ou a determinado usuário pertencente ao grupo, os membros deste, terão total acesso, ou acesso às permissões definidas;
- Você poderá ainda, restringir os acessos a certo usuário mesmo que o grupo em que este esteja inserido também o tenha.

**Importante:** ao ligar o parâmetro CONTACESSMAT, será apresentada a seguinte mensagem:

**"Ao ligar essa funcionalidade, o acesso às matrizes criadas até momento será concedido, automaticamente, para todos os usuários que já trabalham na tela Analise de Giro. Para novas matrizes, será necessário configurar manualmente o acesso para cada usuário. Deseja aplicar essa modificação?"**

- Se você confirmar, o botão **"Segurança"** será habilitado para que possa realizar as configurações de segurança das matrizes de análise de giro. Além disso, será exibido no pop-up Configuração da Matriz, o horário e o usuário que executou a criação da matriz de análise de giro em questão.
- Ao clicar em **"Não"**, o parâmetro será Desligado e você não conseguirá configurar a segurança das matrizes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

## Botão Outras Opções...

Por meio deste botão, teremos as seguintes opções:

| [Alterar Estoque Mínimo nos Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#alterarestoquem%C3%ADnimonoscadastros) |  | [Modo cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#modocota%C3%A7%C3%A3o) |
| --- | --- | --- |
| [Lead Time de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#leadtimedecompra) |  | [Agendamento da geração da tabela de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#agendamentodagera%C3%A7%C3%A3odatabeladegiro) |
| [Uso do parâmetro "UTIFILPDCONGIR"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#usodopar%C3%A2metroUTIFILPDCONGIR) |  | [Iniciar Tour](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#iniciartour) |

### Alterar Estoque Mínimo nos Cadastros

A opção Alterar Estoque Mínimo nos Cadastros quando acionada, fará com que o sistema atualize o campo **"Estoque Mínimo"** do Cadastro do Produto, de acordo com o valor da coluna **"Est.Min.Sug"**. Para tal, teremos as seguintes regras:

![Imagem 33: A opção Alterar Estoque Mínimo nos Cadastros quando acionada, fará com que o sistema atualize o campo "Estoque Mínimo"…](https://ajuda.sankhya.com.br/hc/article_attachments/4404242768023)

No pop-up **"Configurações da Matriz de Análise de Giro"** aba **"Outras Configurações"**, teremos as opções **"Empresa"**, **"Matriz"**, **"Local"** e **"Controle"** (campo **"Apresentar resultado por:"**), dessa forma, o sistema atualizará o campo **"Estoque Mínimo"** da tela Cadastro de Produtos de acordo com os seguintes pontos:

- O campo Estoque Mínimo (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque))  será atualizado caso todas as opções ditas acima estiverem **desmarcadas**.
- Se você **marcar** todas essas opções, o sistema atualizará o referido campo localizado na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaestoque).
- No entanto, se apenas duas destas forem marcadas, como por exemplo, Empresa e Local, ou Empresa e Controle, quando a opção Alterar estoque mínimo nos cadastros for acionada o sistema exibirá as seguintes mensagens:

**"Atualização do Estoque Mínimo só é permitida quando Apresentar por Empresa estiver escolhido."**

**"Atualização do Estoque Mínimo só é permitida quando Apresentar por Local estiver escolhido."**

**"Atualização do Estoque Mínimo só é permitida quando Apresentar por Controle estiver escolhido."**

- Caso apenas a marcação Empresa for selecionada, o Estoque Mínimo da aba Impostos/Informações por empresa que será atualizado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

### Modo Cotação

Por meio da opção **"Modo Cotação"**, teremos a alteração do modo de visão **"Pedidos"** para o modo de visão **"Cotação"**.

O **"Modo de visão Cotação"** permite que sejam realizadas cotações de produtos junto aos fornecedores antes da geração do pedido de compra. Sendo que, também poderão ser aplicados aqui os produtos alternativos bem como os produtos específicos. As funcionalidades aqui apresentadas são similares ao modo de visão "Pedidos", sendo apresentadas algumas particularidades nas configurações:

- Caso o produto a ser gerado na cotação contenha controle adicional de estoque e na análise de giro não esteja sendo considerado controle, a cotação não poderá ser efetuada;
- A unidade do produto necessita ser a mesma unidade configurada na análise de giro;
- Os fornecedores gerados na cotação variam conforme o produto. Se o produto a ser gerado for genérico, os fornecedores da cotação serão iguais aos fornecedores preferenciais dos produtos reais (específicos) vinculados ao produto genérico. Vejamos um exemplo:

**Produto genérico:** Frango Congelado

| **Produtos reais** | **Forn. preferencial** |
| --- | --- |
| Frango Congelado Seara | Seara |
| Frango Congelado Superfrango | Superfrango |
| Frango Congelado Sadia | Sadia |
| Frango Congelado Perdigão | Perdigão |

Então, ao gerar o produto Frango Congelado na cotação, os fornecedores serão os seguintes:

- Seara
- Superfrango
- Sadia
- Perdigão

Sendo que, se o produto a ser gerado na cotação não for genérico o único fornecedor da cotação será o preferencial definido na análise de giro. Caso não haja um fornecedor preferencial definido na análise de giro, a cotação será gerada sem fornecedor;

**Nota:** Através do parâmetro **"Código p/ produto genérico na cotação - CODPRODGENCOT"**, o comprador permite ou não o lançamento de produtos repetidos na cotação. O parâmetro pode ser configurado com três valores:

- **1 (menos um):** Caso seja informado este valor, todo e qualquer produto poderá se repetir no lançamento da cotação;
- **0 (zero):** Informando este valor, nenhum produto poderá se repetir no lançamento da cotação;
- **Valor maior que 0:** Neste caso, informe o código do produto que poderá se repetir, sendo permitida repetição somente para este produto no lançamento da cotação.

Sendo que, caso o produto a ser inserido seja repetido na mesma cotação e o parâmetro esteja configurado para não permitir a inserção; tem-se a exibição da seguinte mensagem:

**"Os seguintes produtos já existem em alguma cotação para a empresa X com o situação igual a "Aberta", portanto não é possível incluí-los. Produtos:**

**Y - "NOMEDOPRODUTO"**

**Retire esse(s) produto(s) dentre os selecionados para gerar cotação."**

**Associação de Ações à Tela de Análise de Giro**

Este recurso do sistema permite, por exemplo, a visualização de dashboards.

Quando você precisar associar seus dashboards à tela de Análise de Giro, basta criar as ações na tela de dicionário de dados (tabela TGFGIR).

Exemplo prático:

Na tela [Dicionário de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025241574-An%C3%A1lise-de-Giro), foi criada a ação **"Leidiane"** do tipo Lançador na tabela TGFGIR.

![Imagem 34: Na tela Dicionário de dados , foi criada a ação "Leidiane" do tipo Lançador na tabela TGFGIR.](https://ajuda.sankhya.com.br/hc/article_attachments/1500003734642)

Ao acessar a tela de Análise de Giro no botão **"Outras Opções"**:

Ao clicar neste botão, serão apresentadas as ações criadas anteriormente. Se selecionarmos a ação Leidiane, o sistema executará a ação programada para o mesmo, que neste caso é abrir um dashboard.

O sistema sempre guardará a última ação executada pelo usuário. Como, por exemplo:

Existem 5 ações, sendo uma delas de nome Leidiane, ao executá-la, o sistema chamará a ação, levando a outra tela (no exemplo acima a Dashboard), em seguida se o usuário voltar a acessar a tela Análise de Giro, esta mesma ação estará selecionada no botão Outras Opções.

**Observação:** Ao sair e acessar novamente a tela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro), o botão Outras Opções será apresentado normalmente, ou seja, com o nome Outras Opções sem salvar a informação da última ação executada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

### Lead Time de Compra

Ao selecionar esta opção, o sistema o redirecionará para a tela [Lead Time de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594134):

[GIF animado: Imagem 35: Ao selecionar esta opção, o sistema o redirecionará para a tela Lead Time de Compra :](https://ajuda.sankhya.com.br/hc/article_attachments/4404242796439)

Destaca-se ainda que, caso possua algum produto focado ao selecionar esta opção, a tela filtrará esse produto.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

### Agendamento da geração da tabela de giro

Para utilização da Matriz de Analise de Giro, é necessário criar e configurar um agendamento; esse agendamento serve para extrair os dados sobre os giros dos produtos e consolidá-los em uma única tabela, tabela esta que será usada para geração da Matriz de Análise de Giro.

Depois da execução bem sucedida de um agendamento, o ícone ![Imagem 36: Depois da execução bem sucedida de um agendamento, o ícone será apresentado na cor verde . Ao clicar sobre ele, você…](https://ajuda.sankhya.com.br/hc/article_attachments/4439885795351) será apresentado na cor **verde**. Ao clicar sobre ele, você poderá verificar os dados da última execução por meio dos seguintes campos:

- **Data Exec.:** este campo exibirá a data da última execução realizada com sucesso.
- **Tempo de Processamento:** aqui será apresentado o tempo de processamento da execução da consolidação.
- **Qtd. de Novos Registros:** informará a quantidade total dos novos registros incluídos.
- **Reprocessando giro a partir de:** este campo demonstrará a data a partir da qual o reprocessamento está sendo efetuado (de acordo com os filtros do agendador). Caso seja a primeira consolidação, que naturalmente irá desconsiderar esse filtro, então apresentará a informação da data a partir da qual a consolidação foi feita.
- **Qtd. de Produtos com Movimento:** tem-se aqui a quantidade total de novos produtos a partir da última consolidação.

Neste pop-up, você também pode acompanhar por meio da aba **"TOP’s elegíveis"**, os [Tipos de Operação- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), que possuam na sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), o campo **"Análise de Giro"** configurado com uma opção diferente de **"Desconsiderar"**.

Além disso, na aba **"Produtos elegíveis"** serão apresentados os produtos que possuem a marcação **"Calcula giro pelo agendador"** habilitada ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque)), e que tenham custos gravados na respectiva tabela.

![Imagem 37: Além disso, na aba "Produtos elegíveis" serão apresentados os produtos que possuem a marcação "Calcula giro pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/4440009825431)

Do contrário, quando houver falha de execução do agendador o ícone será apresentado na cor **vermelha**. Clicando sobre ele, você poderá obter informações da última execução realizada com sucesso, bem como, com erro e os detalhes que o ocasionaram.

Caso o agendamento não seja concretizado, o sistema exibirá o ícone ![Imagem 38: Caso o agendamento não seja concretizado, o sistema exibirá o ícone .](https://ajuda.sankhya.com.br/hc/article_attachments/360102502813).

Destaca-se ainda que o cabeçalho das **"Configurações de agendamento"** permitirá apenas um agendamento.

Para tal ação, basta você clicar no botão ![Imagem 39: Para tal ação, basta você clicar no botão e selecionar a opção "Agendamento da geração da tabela de giro" . Ao clicar…](https://ajuda.sankhya.com.br/hc/article_attachments/4402883458327) e selecionar a opção **"Agendamento da geração da tabela de giro"**. Ao clicar nesta, um pop up de configurações será exibido. Teremos as abas:

#### Frequência

![Imagem 40: Frequência](https://ajuda.sankhya.com.br/hc/article_attachments/4402886860183)

O campo **"Última execução em"** mostrará a data na qual a tarefa foi executada pela última vez.

A **"Próxima execução"** exibirá quando será a próxima execução da tarefa.

Na opção **"Horários"** serão definidos quais horários a tarefa será executada. 

O botão adicionará mais horários de execução, sendo que você também poderá utilizará o botão ![Imagem 41: O botão adicionará mais horários de execução, sendo que você também poderá utilizará o botão para limpar todos os…](https://ajuda.sankhya.com.br/hc/article_attachments/360095095054) para limpar todos os horários. Sendo que:

- Quando você utilizar **"** **Diário** **"** significa que a tarefa será executada todos os dias;
- Em **"Semanal"** será possível definir quais dias na semana a tarefa será executada;
- Quando a opção **"Mensal"** será possível definir quais dias no mês a tarefa será executada.

#### Configurações

O **"Agrupamento de período"** definirá o agrupamento da data de negociação da tabela de giro:

![Imagem 42: O "Agrupamento de período" definirá o agrupamento da data de negociação da tabela de giro:](https://ajuda.sankhya.com.br/hc/article_attachments/4402883481239)

O algarismo inserido em **"Qtd. de períodos (cálculo da curva)"** será utilizado para o cálculo da curva. Assim, teremos o exemplo:

Se você definiu o **"Tipo de Período"** como **"Mensal"** e no campo **"Quantidade de Períodos para Cálculo da Curva"** informou o valor **"3"**, o **"Agendador"** considerará os três últimos meses para cálculo da Curva ABC.

Desta forma, o sistema realizará a consolidação sempre ocorrerá por Empresa, Local e Controle, portanto as marcações **"Considerar Empresa:"**, **"Considerar Local:"** e **"Considerar Controle:"** serão desabilitadas para seleção.

**Seção Parâmetros**

Nesta seção da aba Configurações teremos alguns parâmetros que você poderá utilizar de acordo com sua preferência, sendo estes:

- Qtd. meses p/ refazer consolidação compra/venda;
- Qtd. meses p/ refazer consolidação matriz giro;
- Limite em % para curva B;
- Limite em % para curva C;
- Ignora última compra/venda na matriz?;
- Log na consolidação de giro?;
- Tipo consolidação última compra/venda;
- Filtro adicional para a consolidação de giro.

#### Filtros

Para definir o filtro para gerar a tabela de giro, teremos as opções:

![Imagem 43: Para definir o filtro para gerar a tabela de giro, teremos as opções:](https://ajuda.sankhya.com.br/hc/article_attachments/4402883492247)

Os campos **"Dt. Entrada/Saída"**, **"Dt. Faturamento"**, **"Dt. Movimento"** e **"Dt. Negociação"** podem ser configurados por:

- Início do mês corrente;
- Final do mês corrente;
- Data da execução;
- Início do mês anterior;
- Final do mês anterior.

Após preenchimento desses dados, basta você clicar no botão **"OK"** e, na data da próxima execução, o sistema irá gerar a tabela de giro.

Por meio do botão **"Limpar Consolidação"**, localizado na parte superior da tela de configurações de agendamento, o sistema irá reagendar o agendamento selecionado para a data/hora atual, assim ele será rodado na próxima execução do Job.

**Nota:** Quando configurado um Agendamento de Consolidação de Giro, no horário em que foi agendado, o sistema começará limpando através do botão acima informado, a tabela TGFGIR1 (Limpar Consolidação), caso haja uma consolidação do período e, após, limpará a TGFUVC (Limpar Ult.Compra/Venda) para depois preenchê-la novamente e consolidar o período desejado. Assim, estas opções foram criadas para serem utilizadas em casos pontuais, por exemplo, em bases onde as tabelas encontrem-se extremamente populadas e gerando timeout. Assim, em condições normais estas duas opções não serão usadas.

Na primeira execução dos agendamentos (quando ainda não há nenhuma consolidação de giro), se houver algum filtro criado, ele será ignorado. Então, a seguinte mensagem será apresentada:

**"Este filtro não será considerado na consolidação inicial. "Não existe linhas em TGFGIR1)".**

A cada consolidação, novas linhas são criadas. A partir da segunda consolidação, o filtro será considerado incluindo novas linhas e permitindo assim, análises atualizadas ou antigas do giro.

O filtro padrão **" :Dt. Negociação: > #DtInicioMesAnterior# "** apresentado quando você configurar um novo agendamento, poderá ser editado conforme sua necessidade.

**Importante:** Caso necessário, configure no parâmetro **"Filtro adicional para a consolidação do giro - FILTROADCGIRO"** uma query que irá complementar o filtro criado no que tange a consolidação do giro das empresas. Esta é uma configuração bastante delicada e indicamos sua realização apenas no ato de implantação do sistema e logicamente por um consultor Sankhya.

#### Uso do parâmetro "UTIFILPDCONGIR"

```
 Esta rotina estará disponível a partir da versão 4.12 do sistema.
```

Ao habilitar o parâmetro Usa filtro padrão p/ reproc. consolidação de giro - UTIFILPDCONGIR, no pop-up Configurações de agendamento, o sistema exibirá somente as abas Frequência e Configurações, sendo que, esta última apresentará as seções **"Curva ABC"**, **"Últimas Compras e Vendas"** e **"Giro"**.

![Imagem 44: Ao habilitar o parâmetro Usa filtro padrão p/ reproc. consolidação de giro - UTIFILPDCONGIR , no pop-up Configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/5319102605975)

Na seção Giro, o campo **"Período para reprocessar a consolidação"** permite que você selecione as opções **"Início do mês anterior"** ou **"Especificar qtd. dias para retroação"**, sendo que, caso escolha a opção Especificar qtd. dias para retroação, um campo para digitalização será habilitado para que a quantidade de dias seja informada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)

**Iniciar Tour**

Por meio da opção Iniciar Tour, você terá acesso ao tour do sistema para conferir as novidades da tela.

[GIF animado: Imagem 45: Por meio da opção Iniciar Tour , você terá acesso ao tour do sistema para conferir as novidades da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/4440075709335)

Quando você habilitar a marcação **"Não mostrar novamente"**, seja no primeiro ou no último pop-up do tour, ao abrir a tela, o Tour não será mais exibido.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#bot%C3%A3ooutrasop%C3%A7%C3%B5es...) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

## Botão Relatórios

Na parte superior da tela, teremos o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15665431654423), que a princípio é apresentado desabilitado.

Para que esta opção seja habilitada, é necessário primeiramente que seja feita a criação de um relatório formatado na tela de Relatórios Formatados; na criação deste relatório, teremos o campo **"Id da Tela"**:

![Imagem 47: Para que esta opção seja habilitada, é necessário primeiramente que seja feita a criação de um relatório formatado na…](https://ajuda.sankhya.com.br/hc/article_attachments/360097389593)

Este campo deve ser preenchido com a Id da tela **"Análise de Giro"**, que é localizada no canto superior direito da tela, em **"Configurar Tela"**.

Preenchido o campo Id da Tela na tela de Relatórios Formatados, novamente na tela Análise de Giro, pode-se observar o campo **"Relatórios"** habilitado, onde as opções de escolha serão os relatórios que receberam esta configuração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#top)

Acesse também:

[Análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673)

[Campos para Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro)
