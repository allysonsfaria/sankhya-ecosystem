---
id: "360044601114"
titulo: "Campos para Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:23:20Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "análise de giro", "Parceiro", "br.com.sankhya.com.rotinas.analisegiro", "JUNVENDTROCA", "TOP", "Estoque", "Campos para Análise de Giro", "Campos para Análise de Giro manual", "SOMALEADTIME", "USAPRODGENERICO", "FOLGADOM", "CONSDIASUTEIS", "SUBSUGCOMPBLWMS", "FOLGAQUA", "FOLGAQUI", "FOLGASEX", "FOLGATER", "FOLGASEG", "Detalhes do Produto", "Grade Produtos"]
---

# Campos para Análise de Giro

```
 Módulo: Comercial > Rotinas
```

---

Na grade **"Produtos"** tem-se disponíveis colunas que representam totalizadores dos períodos analisados. Já na grade de **"Detalhes do Produto"**, são apresentadas colunas cujos valores são analisados individualmente por período, de acordo com os intervalos definidos. Isto permite a análise da evolução dos valores dessas variáveis em até 12 períodos distintos.

As informações visíveis na forma de **"Linhas"** na grade de Detalhes do Produto poderão também ser observadas como **"Colunas"**, na grade Produtos. Na grade de Produtos, a descrição dos campos de **"Detalhes"** será acompanhada do número do período. Por exemplo: "Curva Peso (N)", em que **"N"** é o número do período.

Para saber mais sobre as funcionalidades da tela Analise de Giro, acesse os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Grade Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradeprodutos) | [Grade Detalhes do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto) |

---

### Grade Produtos

![Imagem 1: Grade Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/23671696252439)

Nesta grade, são exibidas as seguintes informações:

**Produto** e **Descrição (Produto):** apresentam o código e o nome do produto, respectivamente.

**Grupo** e **Descrição (Grupo Produto):** representam o código e o nome do grupo de produtos ao qual o produto pertence.

**Unidade de Compra:** representa a forma de compra do produto, ou seja, se foi adquirido pela empresa em: quilos, litros, metros, etc.

**Observação:** um produto pode ser comprado em um tipo de volume e vendido em outro tipo.

**Marca:** corresponde a marca definida no cadastro do produto.

**Local** e **Descrição (Local):** representam o código e o nome do local do produto no estoque.

**Estoque:** corresponde a quantidade de estoque do produto, respeitando o filtro para **"Quantidade em estoque"**.

**% Estoque:** se refere a análise vertical da participação do Custo do Estoque deste produto sobre o Custo Total.

**Estoque \* Custo:** apresenta a multiplicação da coluna de Estoque pelo Custo selecionado no campo **"Considerar custo"** (localizado na [Configuração da Matriz de análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro), seção [Outras Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#outrasconfigura%C3%A7%C3%B5es)).

**Estoque Min.:** apresenta o estoque mínimo do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) ou da tabela de estoque, dependendo da seleção realizada no campo **"Apresentar resultado por"**(disponível na Configuração da Matriz de análise de giro, seção Outras Configurações).

**Estoque Máx:** nesta coluna é apresentado o estoque máximo conforme preenchido no campo **"Estoque Máximo (Produtos)"** (tela Cadastro de Produtos, aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque)).

**Observação:** caso no campo Apresentar resultado por as marcações **"Empresa"** e **"Matriz"** estiverem habilitadas, o sistema irá extrair a informação do campo **"Estoque Máximo"** da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque) na tela Cadastro de Produtos.

**Est.Min.Sug.:** refere-se à sugestão calculada pela Análise de Giro, sendo ela baseada no Giro por Dia Útil (Qt. Vnd/Dia útil) multiplicado pelo **"Lead Time"** do produto ou caso não tenha essa informação, multiplica-se pelo número de **"Dias úteis para Estocagem"** indicado na configuração da matriz. Observe:

```
 Est. Min. Sug. = Qtd. Vnd/Dia Útil x Lead Time (se houver)
```

- E caso não tenha, usa-se a fórmula:

```
 Est. Min. Sug. = Qtd. Vnd/Dia Útil x Dias úteis para Estocagem
```

- Além disso, quando o parâmetro **"Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME"** for ligado, o campo Est. Mín. Sug. será calculado pela Qtd. Vnd/Dia Útil multiplicado pela soma do Lead Time com os Dias Úteis para Estocagem, ou seja:

```
 Est. Mín. Sug. = Qtd. Vnd/Dia Útil x (Lead Time + Diaas úteis para Estocagem)
```

Assim, quando a matriz possuir mais de um período, o sistema irá utilizar um giro médio para calcular o estoque mínimo sugerido. 

**Observação:** desativando esse parâmetro, o sistema examinará o valor atual da coluna **"Leadtime"**, caso esse valor estiver zerado ou nulo, os dados da coluna **"Dias úteis para Estocagem"** serão utilizados.

---

**![Imagem 2: Informações adicionais sobre a Qt. Vnd/Dia útil](https://ajuda.sankhya.com.br/hc/article_attachments/21294912035479) Informações adicionais sobre a Qt. Vnd/Dia útil**

**(1)** A memória de cálculo que a aplicação utiliza para calcular a **Qt. Vnd/Dia Útil** pode ser obtida na procedure responsável por realizar esse cálculo "SNK\_MATGIRCALCGIRO2":

VLRVENDIAUTIL\_1 = CASE WHEN p\_UsarRuptura = 'S' AND ( p\_DiasUteis - intDIASRUPTURA) = 0 THEN 0 ELSE (
dobQtde / CASE WHEN p\_DiasUteis = 0 THEN 1 ELSE (
CASE WHEN p\_UsarRuptura = 'S' THEN (p\_DiasUteis - intDIASRUPTURA) ELSE p\_DiasUteis END
) END
) END

Traduzindo a fórmula acima, a expressão fica da seguinte forma:

- se a opção **"Desconsiderar período de ruptura do cálculo de Giro Médio Diário"** das [configurações da matriz](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro) estiver desmarcada;

```
Quantidade Vendida (Período) / Dias úteis (Considerando feriados e folgas)
```

- se estiver marcada.

```
Quantidade Vendida (Período) / Dias úteis (Considerando feriados e folgas) - Dias de Ruptura
de Estoque (TGFRUP)
```

**(1)** A grade da aba [Informações por período](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abainforma%C3%A7%C3%B5esporper%C3%ADodo) contém a coluna Qt. Vnd/Dia útil utilizada para os campos da Sugestão de Compra Giro, esta pode ser alterada quando o **"Período dinâmico"** ou o **"Período fixo"** for usado. Observe o exemplo a seguir:

Suponha que foi definido para usar o Período dinâmico em 5 períodos; a Qt. Vnd/Dia útil será calculada por linha, dividindo a quantidade de venda pelos dias úteis, ou seja:

| **Período** | **Qtd Venda** | **Dias úteis** | **Qt. vnd dia útil** |
| --- | --- | --- | --- |
| 1 (2024-02-25 2024-03-24) | 0 | 20 | 0 |
| 2 (2024-01-25 2024-02-24) | 0 | 21 | 0 |
| 3 (2023-12-25 2023-01-24) | 0 | 21 | 0 |
| 4 (2023-11-25 2023-10-24) | 10 | 20 | 0,5 |
| 5 (2023-10-25 2023-11-24) | 0 | 21 | 0 |

Com 5 períodos mensais, como exemplificado acima, o cálculo é realizado conforme a Quantidade de vendas / Dias úteis (10/20 = 0,5). No entanto, caso escolha trabalhar com Período fixo, na grade será apresentada apenas uma linha.

| **Período** | **Qtd Venda** | **Dias úteis** | **Qt. vnd dia útil** |
| --- | --- | --- | --- |
| 1 (2023-10-25 2024-03-24) | 10 | 103 | 0,1 |

Neste segundo caso, com data fixa no mesmo período, o sistema divide a quantidade de vendas por dias úteis (10/103 = 0,097808737) arredondando o resultado para 0,1.

**Observação:** quando é inserido o Período fixo com 5 períodos definidos através da aba [Períodos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#per%C3%ADodos) do botão ![Imagem 3: Observação: quando é inserido o Período fixo com 5 períodos definidos através da aba Períodos do botão "Alterar a…](https://ajuda.sankhya.com.br/hc/article_attachments/22644738455575) **"Alterar a matriz selecionada"**, referenciando as mesmas datas do primeiro exemplo, o sistema chega no mesmo valor dinâmico, porém se usado a mesma data dinâmica em um único Período fixo, o resultado não será o mesmo.

---

**Estoq.<Média:** esta coluna indica se o estoque atual do produto é menor do que a média vendida no período selecionado.

**Fornec.Preferencial:** esta coluna se refere ao parceiro que tem preferência em fornecer determinado produto. A informação deste campo é buscada do Cadastro de Produtos, e será usada para geração de pedidos. Pode-se editar esta coluna, para geração de Pedidos.

> **Restrição para Geração de Pedidos:** A **Análise de Giro** não deve ser utilizada para gerar pedidos quando a TOP estiver configurada com operação em moeda (`OPERCOMMOEDA = S`). Nestes casos, a geração de pedidos com moeda deve ser realizada exclusivamente pela **Central**, garantindo que:
>
> - O campo **CODMOEDA** seja preenchido obrigatoriamente;
> - O valor da moeda seja corretamente tratado;
> - Os itens sejam recalculados de forma consistente.

**Geração de Pedidos:** este campo é um filtro. Depois de obtidos os produtos por meio da execução da matriz, é possível filtrar produtos para os quais já foram gerados pedidos, não foram gerados ou todas as ocorrências.

**Últ. Vnd:** se refere a data da última venda do produto. Para que a informação deste campo seja alimentada, é necessário que na tela Tipos de Operação - TOP, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), o campo **"Atualizar Última Venda"** esteja definido diferente de **"Não Atualizar"**, ou seja, ele deve estar assinalado com uma das três datas disponíveis.

**Atenção Consultor Sankhya:** este campo é histórico no sistema.

**Dias Sem Venda:** este campo tem o seguinte comportamento:

- Se houver vendas e compras para o produto: conta os dias da última venda até a data atual;
- Se não houver vendas, mas existir compras para o produto: conta os dias da última compra até a data atual para popular o campo;
- Se não houver nem compra nem venda: conta os dias a partir da última data de alteração do cadastro do produto até a data atual para popular o campo.

**Nota:** para que os campos Últ. Cpa e Qtd. Últ. Cpa sejam preenchidos na Análise de Giro, o Tipo de Operação - TOP deverá estar previamente configurado em sua aba Geral com campo **"Atualizar Última Compra"** indicando uma opção diferente de **"Não Atualizar"**. Essa marcação é histórica, por isso, a referida configuração somente surtirá efeito para os lançamentos futuros. Ressaltando ainda que o referido campo só deverá ser configurado para os Tipos de Operação - TOP de Compra.

**Últ. Cpa:** representa a data da última compra do produto.

**Ult Vlr de Cpa:** neste campo, pode-se consultar a informação referente ao último valor da compra realizada.

**Ref.Fornecedor:** este campo se refere ao código de referência do produto no fornecedor.

**% Desconto Máximo:** se refere ao percentual de desconto máximo informado no Cadastro de Produtos.

**Vr.Tab.Preço:** representa o último preço de venda do produto, na tabela de preços que foi colocada no campo **"Tabela de Preço"** das configurações da Matriz.

**% Markup:** este campo mostra o percentual do preço de venda em relação ao custo usado como filtro da matriz. O preço de venda usado será o informado no campo Tabela de Preço das configurações da Matriz.

**Compra Pendente:** apresenta a quantidade de Entradas Pendentes para o produto, de acordo com o filtro para **"Pedido de compra pendente"** definido. Caso não sejam definidos filtros serão considerados os lançamentos pendentes do Tipo de Movimento **"O - Pedido de Compra".**

**Venda Pendente:** este campo apresenta a quantidade de Saídas Pendentes para o produto, de acordo com o filtro para **"Pedido de venda pendente"** definido. Caso não sejam definidos filtros serão considerados os lançamentos pendentes do Tipo de Movimento **"P - Pedido de Venda"**.

**Importante:** além de considerar os Pedidos de Compra/Venda pendentes na composição dos campos Compra Pendente e Venda Pendente, também entram na conta os lançamentos de Compras/Vendas que ainda não foram confirmados e o Tipo de Operação esteja configurado para Atualizar Estoq. a partir da Confirmação.

**Nota:** naturalmente o cálculo filtra somente pedidos (tipmov "P" ou "O"). Para que sejam considerados outros tipos de movimento, é necessário explicitar no filtro de pedidos de venda (ou compra) pendentes quais são os tipos. Exemplo:

**CabecalhoNota->TIPMOV IN ('P','V')** (observe que foi necessário informar também pedido de venda, pois como o filtro determina o tipmov, se não o considerássemos ele não entraria no cálculo).

Pedidos que reservam ou atualizam estoque não serão considerados mesmo depois de faturados, pois como o estoque exibido pela matriz não é o estoque total, mas sim o estoque disponível (Estoque - Reservas), considerar esses lançamentos implicaria em considerá-los duas vezes no cálculo da sugestão de compra.

**Observação:** o sistema não permite que o movimento de Venda (TIPMOV = 'V') confirmado, seja considerado como pendente; uma vez sendo necessário.

**Duração do Estoque:** representa a duração, em dias, do estoque atual do produto, com base no giro diário do produto, considerando também as entradas e saídas pendentes.

```
 Duração do Estoque = (Estoque + Compra Pendente – Venda Pendente) / Qt. Vnd/Dia útil.
```

Exemplo:

Qtd. Vnd/Dia Útil (0,05) / 3 períodos = 0,0166666666666667

**Nota:** caso esse resultado não seja exato, o sistema irá arredondá-lo.

Neste caso foi arredondado para 0.017.

Após esse cálculo, divide-se o Estoque (299) pelo resultado arredondado acima (0,017), onde chega-se no valor de 17.588 da Duração do Estoque.

**Duração Pós Compra:** mostra a duração, em dias, do estoque atual do produto somado à sugestão de compra, considerando entradas e saídas pendentes, com base no giro diário do produto, ou seja:

```
  Duração Pós Compra = (Estoque + Sug.Compra + Compra Pendente – Venda Pendente)/
Qt. Vnd/Dia útil.
```

**Nota:** quando o giro diário for 0 (zero), os campos de duração de estoque ficarão com valor 0 (zero).

**Duração Pós Compra Giro:**  aqui será exibida a duração, em dias, do estoque vigente do produto adicionado à proposta de compra pelo giro, levando em consideração as entradas e saídas pendentes com base no giro diário do produto.

```
 Duração Pós Compra Giro = (Estoque + Sug. Compra Giro) / Giro Diário.
```

**Observação:** quando o campo **"Sug.Compra Giro"** é alterado manualmente, o campo Duração Pós Compra Giro não é afetado e seu valor permanece inalterado mesmo após a aplicação do filtro.

**Lead Time:** se refere a quantidade de dias entre o lançamento do pedido de compra e a entrega do produto pelo fornecedor, ou seja, a entrada do produto no estoque. Esse valor é utilizado pela Análise de Giro para calcular a Sug.Compra Giro. O valor para esse campo pode ser calculado automaticamente através da tela [Lead Time de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594134-Lead-Time-de-Compra).

**Sug.Compra:** apresenta a sugestão de compra baseada no Estoque Mínimo do produto, ou seja:

```
 Sug.Compra = (Estoque Min.* % Acréscimo na Sugestão de Compras)
        –Estoque–Compra Pendente+Venda Pendente
```

**Sug.Compra Giro:** apresenta a sugestão de compra baseada no Giro do Produto, ou seja:

- Quando o parâmetro **"Somar o Lead Time aos dias úteis de estocagem -** **SOMALEADTIME"** estiver desabilitado tem-se o seguinte:

```
 Sug.Compra Giro = (Qt.Vnd/Dia útil* Dias ÚTEIS pra Estocagem + % Acréscimo na Sugestão
          de Compras) - Estoque - Compra Pendente + Venda Pendente
```

---

![Imagem 4: Informações adicionais sobre a fórmula acima:](https://ajuda.sankhya.com.br/hc/article_attachments/21294912035479) **Informações adicionais sobre a fórmula acima:**

A Sugestão de Compra Giro é calculada usando a função ROUND() sem casas decimais, arredondando para cima se for maior ou igual a 0,5 e truncando para zero se for menor que 0,5.

Na fórmula mencionada, há um arredondamento no cálculo de **"Qt.Vnd/Dia útil"**. Nesse momento, a quantidade já será igual a zero, pois esse cálculo é idêntico ao de **"Est. Min. Sug."**.

Atualmente, não há um parâmetro para quebrar a quantidade da Sugestão de Compra Giro; o cálculo sempre é realizado arredondando para zero casas decimais.

---

- Por outro lado, quando o parâmetro estiver habilitado, será considerado a seguinte fórmula:

```
  Sug.Compra Giro = (Qt. Vnd/Dia útil*(Dias ÚTEIS pra Estocagem + Lead Time)) * %
          Acréscimo na Sugestão de Compras) - Estoque - Compra Pendente + Venda Pendente
```

**Observação:** o cálculo da Sug. Compra Giro poderá, também, sofrer influência do parâmetro **"Considerar os dias úteis (Lead Time) da Anál. Giro. - CONSDIASUTEIS"** que, sendo habilitado, irá considerar a seguinte fórmula:

- Com o parâmetro SOMALEADTIME desabilitado, tem-se o seguinte:

```
 Sug.Compra Giro = (Qt. Vnd/Dia útil" * SNK_QTD_DIAS_UTEIS (Data de
        hoje, Dias ÚTEIS pra Estocagem) * % Acréscimo na Sugestão de Compras)
        - Estoque - Compra Pendente + Venda Pendente
```

- Já com o parâmetro habilitado:

```
 Sug.Compra Giro = (Qt. Vnd/Dia útil * SNK_QTD_DIAS_UTEIS(Data de
        hoje, Dias ÚTEIS pra Estocagem + Leadtime) * % Acréscimo na Sugestão
        de Compras) - Estoque - Compra Pendente + Venda Pendente.
```

**Nota:** a função SNK\_QTD\_DIAS\_UTEIS é a que retorna os dias úteis de um período.

**Observação:** se o campo **"Lead time de compra"** da aba [Impostos/Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa) ou o campo Lead time de compra da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque) não estiverem preenchidos, o sistema utilizará a configuração da matriz para completar a informação dos Dias ÚTEIS para estocagem.

Possuindo mais de um período na matriz, o sistema considerará a média entre a Qt. Vnd/Dia Útil de cada período para sugerir a compra giro. O cálculo da **"Sug. Compra Giro"** utilizará também o campo **"Lead Time de Compra"** do Cadastro do Produtos, para encontrar o estoque mínimo a partir do giro. Se o campo Lead Time de Compra não estiver preenchido no Produto, o sistema utilizará o campo **"Dias ÚTEIS para estocagem"**, que é usado de forma geral para todos os produtos.

**Popularidade Total:** este campo apresenta o número de notas que contêm o produto em todos os períodos.

**Freq.Qtd Vnd:** representa o número de períodos que tiveram quantidade negociada maior que zero para o produto.

**Total Qtd Vnd:** se refere a soma do giro de todos os períodos selecionados para análise.

**Maior Qtd.Vnd:** este campo representa a Quantidade Vendida no período com maior volume de vendas, dentre os períodos selecionados.

**Menor Qtd Vnd:** representa a Quantidade Vendida no período com menor volume de vendas, dentre os períodos selecionados.

**Média qtd Vnd:** mostra a quantidade média vendida para o produto nos períodos selecionados. É calculada dividindo o **"Total Qtd Vnd"** pela quantidade de períodos selecionados para análise.

**Importante:** para que sejam considerados todos os períodos para o cálculo da Média qtd vnd, é necessário que a marcação **"Período sem vendas influencia a média para estoque mínimo"** esteja realizada; esta marcação está presente na [Configuração da Matriz de análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro), aba [Estoque Mínimo e Sugestão de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554#estoquem%C3%ADnimoesugest%C3%A3odecompra).

**Alíq.Créd.ICMS:** este campo apresenta a alíquota de ICMS da última nota do produto.

**Créd.ICMS:** este campo se refere ao Valor de crédito do ICMS, calculado pelo custo usado na matriz multiplicado pela **"Alíq.Créd.ICMS"**, será apresentado neste campo.

**Giro Médio Diário:** tem-se neste campo, a quantidade vendida dividida pelos dias úteis do período informado. Desta forma, obtém-se neste caso um valor médio.

**Observação:** neste campo o sistema sempre procederá com o arredondamento dos valores registrados, apresentando apenas números inteiros. Diante disto, deve-se considerar o seguinte exemplo: quando o giro médio for de 0,5052 o sistema arredondará para 1.

**Duração do Estoque de Segurança:** este campo representa a quantidade de dias úteis previstos para duração do estoque de segurança. Dessa forma, tem-se que a fórmula utilizada no cálculo deste campo será:

```
 Duração do Estoque de Segurança = Estoque Mínimo / Dia útil / Qtd Vnd
```

Para que este campo seja calculado, é necessário que o campo **"Estoque Mínimo"** localizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abaestoque), seja atualizado de acordo com o valor presente na coluna **"Est.Min.Sug"**; esta modificação é feita na tela Análise de Giro, por meio do botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#alterarestoquem%C3%ADnimonoscadastros), marcação **"Alterar Estoque Mínimo nos Cadastros"**.

**Ponto de Pedido:** este campo exibe a data prevista em que deverá ser inserido um novo de pedido de compra, considerando o que existe em estoque, o Lead Time da nova entrega e o estoque de segurança para se evitar ruptura.

**Observação:** quando o parâmetro **"Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME"** estiver ligado, a fórmula utilizada no cálculo do campo Ponto de Pedido será:

```
 Ponto de Pedido = Data atual - 1 + (Duração de Estoque
       - Duração do Estoque de Segurança - Lead Time - Dias Úteis de Estocagem).
```

Se o parâmetro for desligado, e se tiver informações do Lead Time para o Produto selecionado, teremos:

```
 Ponto de Pedido = Data Atual - 1 + (Duração de Estoque
       - Duração do Estoque de Segurança - Lead Time).
```

E se for desligado o parâmetro Somar o Lead Time aos dias úteis de estocagem - SOMALEADTIME, e não tiver informações referente ao Lead Time para o produto selecionado:

```
 Ponto de Pedido = Data Atual - 1 + (Duração de Estoque
       - Duração do Estoque de Segurança - Dias Úteis de Estocagem).
```

**Pedido:** esse campo refere-se ao número único do pedido de compra.

**Previsão de Entrega:** tem-se neste campo a data prevista para que os produtos sejam recebidos. 

**Observação:** o valor obtido no campo acima será obtido por meio do seguinte cálculo:

```
 "Data Atual" - 1 + ("Duração do Estoque" - "Duração do Estoque de Segurança")
```

**Nota:** os campos **"Qtde Venda (1 até 12)"**, **"Média Qtd Vnd"**, **"Estoque"**, **"Sug.Compra"**, **"Qtd. Últ. Cpa"**, **"Compra pendente"**, **"Venda pendente"**, **"Custo Rep x Sug. Compra"** e **"Estoque x Cus. Ger."**, apresentarão totalizadores na grade **"Produtos"**, para que os compradores possam fazer suas análises com base em informações totalizadas.

**Multipl. Compra:** neste campo é apresentado o múltiplo de compra para o produto dado ao fornecedor preferencial. Seu valor é alimentado com base em definição feita no Cadastro de Produtos, aba [Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaprodutosequivalentes), campo **"Multipl. Compra"**.  Além disso, para que o sistema utilize este valor definido é necessário que seja informado o campo **"Fornec. Preferencial"** localizado na [Grade Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradeprodutos) da tela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro). Caso este campo não seja preenchido será utilizado o valor definido no campo **"Qtd. multiplicador Compra"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-). 

**Sug. Compra Mult. Cpa:** este campo exibe o valor da Sug.Compra calculado em função do múltiplo de compra, ou seja, se a sugestão de compra calculada não for um número múltiplo do Múltiplo de Compra, a sugestão de compra em função do múltiplo de compra passa ser o próximo valor múltiplo de Múltiplo de Compra.

**Sug. Compra Giro Mult. Cpa:** neste campo, tem-se o valor da Sug. Compra Giro calculado em função do múltiplo de compra, ou seja, se a sugestão de compra giro calculada não for um número múltiplo do Múltiplo de Compra a sugestão de compra giro em função do múltiplo de compra passa ser o próximo valor múltiplo de Múltiplo de Compra.

**Sug. Compra Giro Ajustado Mult. Cpa:** este campo apresenta o valor da Sug. Compra Giro Ajustado calculado em função do múltiplo de compra, ou seja, se a sugestão de compra giro ajustado calculada não for um número múltiplo do Múltiplo de compra a sugestão de compra giro ajustada em função do múltiplo de compra será o próximo valor múltiplo de Múltiplo de compra.

Considere o seguinte exemplo, suponhamos um produto que possua Multipl. Compra igual a 10.

1. Se a sugestão de compra calculada é 5, será necessário comprar 10, então a sugestão de compra baseada no múltiplo de compra será 10.
2. Se a sugestão de compra calculada é 12, será necessário comprar 20, então a sugestão de compra baseada no múltiplo de compra será 20.

**Bloqueado no WMS:** este campo exibe a somatória dos estoques que estão bloqueados no WMS.

**Importante:** quando o parâmetro **"Subtrair da Sug de Compra qtde bloqueada no WMS - SUBSUGCOMPBLWMS"** estiver habilitado, tem-se que este irá subtrair da Sugestão de Compra a quantidade que constar no campo acima mencionado.

**Observação:** alguns campos aqui expostos estarão visíveis na grade como padrão, porém  pode-se alterá-los para campos invisíveis no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15479858220695) **"Configurar grade"**.

**Ruptura de Estoque (Qtd. dias):** fornece informações sobre os períodos de indisponibilidade de estoque, considerando apenas o estoque próprio da empresa.

#### Botões do topo da grade

No topo da grade de produtos tem-se alguns botões, são eles:

No botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16032920105367) **"Outras Opções..."** da grade de Produtos, ao utilizar a marcação **"Esconder informações de período"**, o sistema ocultará as colunas referentes às seguintes informações por período: **"% G.Variável/Fat"**, **"% Lucro"**, **"% M.Contrib./Fat"**, **"% M.Contribuição"**, **"% Peso"**, **"% Qtd"**, **"% T.Lucro"**, **"% Total"**, **"Acumulador Margem"**, **"Acumulador Qtde, Acumulador Total"**, **"Acumulador Peso"**, **"Curva Marg"**, **"Curva Peso"**, **"Curva Qtd"**, **"Curva Tot"**, **"Custo Vnd Total"**, **"Custo Vnd Unitário"**, **"Dias sem saldo"**, **"Gasto Variável"**, **"M.Contribuição"**, **"Período1"**, **"Periodo2"**, **"Períodos"**, **"Popularidade"**, **"Peso"**, **"Qt. Vnd/Dia útil"**, **"Qtd Venda"**, **"Vr. Total"**, **"Vr. Unit."** e **"Vlr Lucro"**.

Através do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15479866671383) **"Legenda de Cores"** pode-se interpretar os registros apresentados na grade, sendo estes: M.Contribuição, Período1, Periodo2, Períodos, % G.Variável/Fat, % Lucro, % M.Contrib./Fat, % M.Contribuição, % Peso, % Qtd, % T.Lucro, % Total, Acumulador Margem, Acumulador Qtde, Acumulador Total, Acumulador Peso, Curva Marg, Curva Peso, Curva Qtd, Curva Tot, Custo Vnd Total, Custo Vnd Unitário, Dias sem saldo, Gasto Variável, Popularidade, Peso, Qt. Vnd/Dia útil, Qtd Venda, Vr. Total, Vr. Unit. e Vlr Lucro.

- **Vermelho**: Sem giro;
- **Preto**: Com Giro;
- **Azul**: Sug. Compra ajustada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#top)

### Grade Detalhes do Produto

Esse painel trará informações mais detalhadas do produto selecionado na grade superior, nele, tem-se informações importantes como Venda e Compra Pendente e a Sugestão de Compra informada. além disso, ainda mostrará a quantidade e data da última compra do produto selecionado. O objetivo dessa apresentação é a visualização rápida da evolução destas informações ao longo dos períodos observados.

Considere ainda que, o campo **"Venda Pendente"** deste painel, leva em conta o seguinte:

- A fórmula para cálculo de vendas pendentes é: Qtd. negociada - Qtd. entregue;
- Serão considerados todos os pedidos pendentes, independente de sua data de negociação, desde que siga as regras;
- A TOP do Pedido deve ser do tipo **"P -Pedido"**, **"O - Orçamento"** ou **"J - Pedido de requisição"** e, o status da nota, deve ser **"Confirmada"**;
- Quando a TOP do Pedido estiver marcada para reservar estoque, fará com que esse pedido não seja considerado no processamento da matriz; considera-se também, os dados históricos dessa TOP, ou seja, mesmo alterando a mesma após o lançamento do registro, não surtirá efeito.

![Imagem 8: Quando a TOP do Pedido estiver marcada para reservar estoque, fará com que esse pedido não seja considerado no…](https://ajuda.sankhya.com.br/hc/article_attachments/22015407066519)

Para conhecer as funcionalidades de cada aba, clique nos links abaixo:

| [Aba Informações por período](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abainforma%C3%A7%C3%B5esporper%C3%ADodo) | [Aba Fornecedores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abafornecedores) |
| --- | --- |
| [Aba Detalhes da Sug. de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abadetalhesdasug.decompra) | [Aba Compras/Vendas Pendentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#abacomprasvendaspendentes) |
| [Aba Produtos Alternativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#AbaProdutosAlternativos) |  |

#### Aba Informações por período

Nessa aba, tem-se uma grade que fará a transposição das informações por período que são mostradas na grade superior, ou seja, cada coluna representa um período; já nesta grade transposta, as informações se dividem de forma diferente, nela aparecerão apenas as informações por período do produto selecionado na grade superior e cada linha representará um período, facilitando assim a análise do Gestor a respeito das informações sobre um determinado produto ao longo do tempo.

![Imagem 9: Nessa aba, tem-se uma grade que fará a transposição das informações por período que são mostradas na grade superior, ou…](https://ajuda.sankhya.com.br/hc/article_attachments/22015512549527)

**Observação:** ao adicionar algum campo na grade **"Informações por período"**, esse campo também será apresentado na grade de **"Produtos"**, além dos campos configurados como visíveis.

**Observação:** todos os campos de **"Análises Verticais (%)"** serão baseados no critério de Ordenação definido em **"Detalhar de acordo com"**.

Desse modo, podemos destacar as seguintes informações dispostas nessa aba:

**Qtd. Venda:** este campo apresenta a quantidade vendida no Período N.

**Nota:** trabalhando com um Tipo de Operação que não atualiza estoque (Tipo de Operação - TOP, aba Geral, campo **"Atualização do Estoque"** definido como Nenhuma), as vendas realizadas utilizando-se esta TOP serão consideradas na Matriz de Análise de Giro (alimentarão o campo Qtd. Venda), caso o parâmetro **"Junção de pedidos de Venda e Troca - JUNVENDTROCA"** esteja habilitado. Quando este parâmetro estiver habilitado, os componentes do KIT não serão apresentados.

**% Qtd:** se refere a análise vertical da participação da Quantidade Vendida deste produto no Período N, sobre a Quantidade Total Vendida (dependendo da opção **"Detalhar de acordo com"**, total da Marca, Grupo, Empresa ou Produto).

**Vr. Unit.:** representa o valor médio unitário praticado nas vendas do Período N. Corresponde à soma do valor total vendido do produto, dividida pela quantidade total vendida.

**Vr. Total:** se refere ao Valor total vendido desse produto no Período N, resultado da multiplicação de todas as quantidades vendidas pelos valores unitários praticados em cada uma das vendas.

**% Total:** este campo apresenta a análise vertical da participação do Valor Total Vendido deste produto no Período N, sobre o Valor Total Vendido (dependendo da opção Detalhar de acordo com, total da Marca, Grupo, Empresa ou Produto).

**Custo Vnd Total:** apresenta o Custo da Mercadoria Vendida no Período N, resultado da multiplicação do custo selecionado em **"Considerar Custo"** pela quantidade vendida.

**Qt. Vnd/Dia útil:** se refere a quantidade vendida do produto por dia útil no período N, resultado do Giro total do Período N dividido pelo Número de Dias Úteis no período. O sistema considera como sendo um dia útil os dias da semana nos quais a empresa trabalha. Esta definição é realizada através dos seguintes parâmetros:

- Folga no Domingo ? - FOLGADOM
- Folga na Segunda? - FOLGASEG
- Folga na Terça? - FOLGATER
- Folga na Quarta ? - FOLGAQUA
- Folga na quinta? - FOLGAQUI
- Folga na Sexta? - FOLGASEX
- Folga no Sábado? - FOLGASAB

**Observação:** é relevante mencionar que o sistema considera os feriados cadastrados como dias não úteis.

**Nota:** somando o resultado de cada período referente a este campo, tem-se que não chegará ao valor do Giro Médio Diário, uma vez que trata-se de um valor médio.

**Vlr Lucro:** tem-se aqui o Valor do lucro obtido pelo Produto no Período N, pelo algoritmo de Margem de Contribuição:

```
 Vlr Lucro = (Vr. Total – CMV – Gastos Variáveis – Part.Gasto Fixo)
```

**% Lucro:** este campo mostra o Percentual de lucro obtido pelo Produto no Período N. Calculado sobre o Vr. Total da venda do Produto:

```
 % Lucro = (Vlr Lucro * 100 / Vr. Total)
```

**% T.Lucro:** se refere a análise vertical da participação do Lucro deste produto no Período N, sobre o Lucro Total (dependendo da opção Detalhar de acordo com, total da Marca, Grupo, Empresa ou Produto).

**Gasto Variável:** representa o Valor do Gasto Variável gerado pela Venda do Produto no Período N (Impostos + Comissões +...), este campo não compõe o CMV do produto.

**% Gasto Variável:** este campo se refere a análise vertical da participação do Gasto Variável deste produto no Período N, sobre o Gasto Variável Total (dependendo da opção Detalhar de acordo com, total da Marca, Grupo, Empresa ou Produto).

**% G.Variável/Fat:** mostra o Percentual de Gasto Variável gerado pela Venda do Produto no Período N. Calculado sobre o Vr. Total da venda do Produto:

```
 % G.Variável/Fat = (Gasto Variável * 100 / Vr. Total)
```

**M.Contribuição:** se refere ao Valor da Margem de Contribuição gerada pela Venda do Produto no Período N:

```
 M.Contribuição = (Vr. Total – Custo Vnd Total – Gasto Variável)
```

**% M.Contribuição:** este campo corresponde a análise vertical da participação da Margem de Contribuição deste produto no Período N, sobre a Margem de Contribuição Total (dependendo da opção Detalhar de acordo com, total da Marca, Grupo, Empresa ou Produto).

**% M.Contrib./Fat:** Tem-se aqui, o percentual de Margem de Contribuição gerada pela Venda do Produto no Período N. Calculado sobre o Vr. Total da venda do Produto:

```
 % M.Contrib./Fat = (M.Contribuição * 100 / Vr. Total)
```

**Curva Qtd:** apresenta a classificação segundo o critério de Curva ABC, da quantidade vendida desse Produto no Período N calculada sobre a Quantidade Total Vendida. Os Percentuais que determinam se o Produto pertence à Curva A, B ou C são definidos no Cadastro de Grupo de Produtos.

**Curva Peso:** mostra a classificação segundo o critério de Curva ABC. A análise é feita observando o **"Peso"**, da mesma forma como é feito com a **"Quantidade"**. O Peso será calculado com base no campo **"Peso Bruto"** do Cadastro do Produto.

**Curva Tot:** indica a classificação segundo o critério de Curva ABC, do Valor Vendido desse Produto no Período N calculado sobre o Valor Total Vendido. Os Percentuais que determinam se o Produto pertence à Curva A, B ou C são definidos no cadastro de Grupo de Produtos.

**Curva Marg:** apresenta a classificação segundo o critério de Curva ABC, da Margem de Contribuição desse Produto no Período N, calculada sobre a Margem de Contribuição Total. Os Percentuais que determinam se o Produto pertence à Curva A, B ou C são definidos no cadastro de Grupo de Produtos.

**Popularidade:** representa o número de notas que contêm o produto no período.

**Acumulador Margem:** este campo se refere a análise vertical da participação da Margem de Contribuição deste produto no Período N, sobre a Margem de Contribuição Total, acumulado com as margens das linhas anteriores (só será calculado se a opção **"Detalhar resultado por"** for igual a Produto. Para visualizar os valores acumulados corretamente deve-se ordenar a grade por **"M. Contribuição"** de forma decrescente).

**Acumulador Qtde:** representa a análise vertical da participação da Quantidade Vendida deste produto no Período N, sobre a Quantidade Total Vendida, acumulado com as quantidades vendidas das linhas anteriores (só será calculado se a opção Detalhar resultado por for igual a Produto. Para visualizar os valores acumulados corretamente deve-se ordenar a grade por **"Qtd.Vnd"** de forma decrescente).

**Acumulador Total:** este campo corresponde a análise vertical da participação do Valor Total deste produto no Período N, sobre o Valor Total, acumulado com os valores das linhas anteriores (só será calculado se a opção Detalhar resultado por for igual a Produto. Para visualizar os valores acumulados corretamente deve-se ordenar a grade por **"Vr. Total"** de forma decrescente).

**Observação:** o sistema não considera as devoluções.

Através do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15480142737815) **"Visão Gráfica"** pode-se visualizar as informações de desempenho do produto, conforme a configuração da matriz na visão gráfica, exibindo todos os períodos. Aqui serão exibidas as mesmas informações de **"Qtd Venda"** por período:

[GIF animado: Imagem 11: Através do botão "Visão Gráfica" pode-se visualizar as informações de desempenho do produto, conforme a configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/22016656977047)

O botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15480174374679) **"Detalhes por Período"**, quando acionado, exibirá a visão analítica das informações que compuseram o período consolidado, contemplando os totalizadores de quantidade e valor total.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto)

#### Aba Fornecedores

Aqui, o sistema mostrará um gráfico de pizza dos fornecedores envolvidos nas compras do produto selecionado, dividindo e mostrando ao gestor de qual fornecedor a empresa mais compra o produto. Dessa forma, ao clicar sobre o gráfico, o sistema mostrará informações mais detalhadas sobre o fornecedor, além disso, mostrará uma grade com os contatos do mesmo.

[GIF animado: Imagem 13: Aqui, o sistema mostrará um gráfico de pizza dos fornecedores envolvidos nas compras do produto selecionado, dividindo…](https://ajuda.sankhya.com.br/hc/article_attachments/22016802962071)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto)

#### Aba Detalhes da Sug. de Compra

Por meio dessa aba, pode-se visualizar o detalhamento da composição de suas sugestões de compras para que, assim, a decisão dessas compras seja mais ágil e assertiva. 

![Imagem 14: Por meio dessa aba, pode-se visualizar o detalhamento da composição de suas sugestões de compras para que, assim, a…](https://ajuda.sankhya.com.br/hc/article_attachments/22016905943447)

Aqui, pode-se observar as seguintes linhas de sugestões de compra calculadas pelo sistema:

- Sug. Compra;
- Sug. Compra Giro;
- Sug. Compra Giro Ajustado.

Assim, serão apresentados os valores das variáveis que influenciam nos cálculos conforme cada tipo de sugestão. Observe: 

- Estoque Mín.;
- Estoque Máx.;
- Est. Mín Sug.;
- Estoque;
- Compra Pend.;
- Venda Pend.

Além disso, quando passar o mouse sobre cada uma das linhas e/ou colunas apresentadas, é possível consultar os detalhes destes:

[GIF animado: Imagem 15: Além disso, quando passar o mouse sobre cada uma das linhas e/ou colunas apresentadas, é possível consultar os detalhes…](https://ajuda.sankhya.com.br/hc/article_attachments/22017449716631)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto) 

#### Aba Compras/Vendas Pendentes

Ao efetuar a marcação **"Listar pedidos na aba Compras/Vendas Pendentes"** na [Configuração da Matriz de análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro), você visualizará nesta aba, todas as notas/pedidos que compõem as compras e vendas pendentes do respectivo produto selecionado, após o processamento da matriz.

![Imagem 16: Ao efetuar a marcação "Listar pedidos na aba Compras/Vendas Pendentes" na Configuração da Matriz de análise de giro ,…](https://ajuda.sankhya.com.br/hc/article_attachments/22017588304407)

Por meio do filtro **"Mostrar"**, pode-se optar por analisar os lançamentos que compõem as **"Compras"** ou **"Vendas"** que ainda estão pendentes.

Na parte inferior da aba, os totalizadores referentes a quantidades e valores totais serão iguais à soma dos respectivos campos dos lançamentos apresentados na grade.

Quando a marcação Listar pedidos na aba Compras/Vendas Pendentes não for realizada, será exibida uma mensagem sinalizando o motivo das notas não serem apresentadas, conforme a imagem abaixo:

![Imagem 17: Quando a marcação Listar pedidos na aba Compras/Vendas Pendentes não for realizada, será exibida uma mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/22018170364823)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto) 

#### Aba Produtos Alternativos

Pode-se visualizar nesta aba as informações de estoque, custo e preço de venda dos produtos alternativos vinculados ao item posicionado na grade superior, conforme configuração realizada no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).

**Observação:** esta aba é exibida quando a matriz não está configurada para agrupar Produtos Alternativos, ou seja:

- Caso o parâmetro **"Usa produtos genéricos?-USAPRODGENERICO"** esteja ligado, a aba só será exibida se o campo **"Tipo agrupamento"**, apresentado na [Configuração da Matriz de análise de giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554#configura%C3%A7%C3%A3odamatrizdean%C3%A1lisedegiro), esteja configurado com a opção **"Nenhum"**;
- Se o parâmetro mencionado anteriormente estiver desligado, a aba só será exibida se a opção **"Agrupar movimentação produto alternativo"** (Configuração da Matriz de análise de giro, seção [Outras Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554#outrasconfigura%C3%A7%C3%B5es)) estiver desmarcada.

![Imagem 18: Se o parâmetro mencionado anteriormente estiver desligado, a aba só será exibida se a opção "Agrupar movimentação…](https://ajuda.sankhya.com.br/hc/article_attachments/6278085335319)

Além disso, se no parâmetro **"Tipo de direção para considerar na visualização de Produtos alternativos-TIPDIRPROALT"** for selecionada a opção **"Unidirecional"**, serão apresentadas nesta aba, todos os produtos alternativos do produto selecionado na grade principal. Já se for indicada a opção **"Bidirecional"**, serão exibidos todos os produtos alternativos do produto selecionado na grade principal e os produtos aos quais ele também é alternativo. 

A respeito das informações apresentadas nas colunas, temos que:

- Os valores das colunas **"Estoque Mínimo"** e **"Estoque Máximo"** respeitam a mesma lógica das informações exibidas na grade principal, ou seja, podem apresentar informações originadas da aba **"Estoques"**, **"Impostos e Informações por Empresa"** ou **"Medidas e Estoque"**, dependendo do quão analítica for a definição realizada na configuração de **"Apresentar resultado por"** (Configuração da Matriz de análise de giro, seção Outras Configurações);
- A coluna **"Vlr. Tab. Preço"** exibirá o preço cadastrado de acordo com a tabela informada no campo **"Tabela de preço"**, localizado na Configuração da Matriz de análise de giro, seção Outras Configurações.

A aba permite filtrar as informações por **"Empresa"** e/ou **"Local"**, quando estas opções de apresentação são selecionadas nas configurações da Matriz. Por exemplo, caso seja acionado o filtro Empresa, ao selecionar um registro na grade principal, nesta aba serão exibidos apenas as informações de estoque dos alternativos para a mesma empresa.

![Imagem 19: A aba permite filtrar as informações por "Empresa" e/ou "Local" , quando estas opções de apresentação são selecionadas…](https://ajuda.sankhya.com.br/hc/article_attachments/6278281181207)

Para que não sejam exibidos os registros cujo Estoque seja igual a **"0"** (zero), acione a marcação **"Ocultar estoque zerado"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#Gradedetalhesdoproduto) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601114-Campos-para-An%C3%A1lise-de-Giro#top)

![Imagem 20: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/23765228655767) Acesse também:

[Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro)

[Análise de Giro - Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050819554-An%C3%A1lise-de-Giro-Bot%C3%B5es-do-topo-da-tela)
