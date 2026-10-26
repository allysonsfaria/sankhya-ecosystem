---
id: "360044595954"
titulo: "Desvios de Produção (PAs)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:51:00Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "br.com.sankhya.prod.desvioproducaopa", "Desvios de Produção (PAs) manual", "Configuração", "Relatórios Gerenciais", "Estoque", "Produção", "Filtros: Configurações período", "Visões: PAs MPs OPs", "Conceitos: Desvio superior inferior"]
---

# Desvios de Produção (PAs)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312677973655) Módulo: Produção > Consultas
```

---

Esta é uma rotina gerencial para o acompanhamento/análise dos desvios de produção, no que diz respeito a quantidade produzida de produtos em um determinado período.

![Imagem 2: Esta é uma rotina gerencial para o acompanhamento/análise dos desvios de produção, no que diz respeito a quantidade…](https://ajuda.sankhya.com.br/hc/article_attachments/4407586759319)

| [Conceitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#conceitos) |  | [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#filtros) |
| --- | --- | --- |
| [Análise 1 - Visão por PAs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#anlise1-visoporpas) |  | [Análise 2 - Visão de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#anlise2-visodemps) |
| [Análise 3 - Visão por Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#anlise3-visoporordensdeproduo) |  |  |

## Conceitos

Antes de utilizar esta rotina, é necessário compreender alguns conceitos, são eles:

**Desvio**

O desvio é a diferença entre a quantidade prevista e quantidade realizada. No caso de uma análise voltada para produto acabado, o desvio será a diferença entre a quantidade do produto que esta prevista para ser fabricada (tamanho de lote) subtraída à quantidade fabricada do mesmo (qtd. apontada e que consequentemente saiu em notas de produção). Considere o seguinte exemplo:

Qtd. Prevista = 15UN

Qtd. Produzida = 20UN

Desvio = Qtd. Produzida – Qtd. Prevista

Desvio = 20UN – 15UN

Desvio = 5UN

**Desvio Superior**

Entende-se como desvio superior, um desvio de valor positivo, ou seja, a quantidade produzida do produto subtraída da quantidade prevista para fabricação é maior que zero. Analisemos o exemplo abaixo:

Qtd. Prevista = 15UN

Qtd. Produzida = 20UN

Desvio = Qtd. Produzida – Qtd. Prevista

Desvio = 20UN – 15UN

Desvio = 5UN

**Desvio Inferior**

Trata-se de um desvio de valor negativo, ou seja, a quantidade produzida do produto subtraída da quantidade prevista para fabricação é menor que zero. Por exemplo: 

Qtd. Prevista = 25UN

Qtd. Produzida = 20UN

Desvio = Qtd. Produzida – Qtd. Prevista

Desvio = 20UN – 25UN

Desvio = -5UN

**Desvio Total**

Este desvio representa o somatório dos desvios de produção independente de ser um desvio superior ou inferior. Logo, este indicador pode ser calculado apenas em uma análise macro onde existem várias ordens de produção. Considere o seguinte exemplo:

OP 1, desvio igual à 25UN

OP 2, desvio igual à 15UN

OP 3, desvio igual à -10UN

Então desvio total é igual à 30UN

**Desvio Médio**

O desvio médio representa o valor médio do desvio entre várias Ordens de Produção. Deste modo, este indicador pode ser calculado apenas em uma análise macro contendo várias OPs. Exemplo:

OP 1, desvio igual à 25UN

OP 2, desvio igual à 15UN

OP 3, desvio igual à -10UN

Então desvio médio é igual à 10UN

**Custo Desvio**

Este custo corresponde ao custo financeiro para o desvio em questão. Desta forma, todo indicador de desvio vem acompanhado também do indicador de custo. Tem-se o Custo Desvio Total, Custo Desvio Inf., Custo Desvio Sup. e Custo Desvio Méd.

O valor de custo considerado no indicador é o custo do produto na data de negociação da nota de Produção.

**% Desvio**

Este percentual equivale a porcentagem pela qual a quantidade do desvio corresponde sobre a quantidade prevista para fabricação do produto. Desta forma, todo indicador de desvio vem acompanhado do indicador de percentual. Sendo eles, o % Desvio Total, % Desvio Inf., %Desvio Sup. e % Desvio Méd.

**Importante:** esta rotina considera apenas Ordens de Produção finalizadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#top)

## Filtros

Detalharemos aqui algumas informações a respeito do painel de Filtros, visto que algumas opções na verdade são configurações que vão impactar no resultado apresentado pela rotina.

![Imagem 3: Detalharemos aqui algumas informações a respeito do painel de Filtros, visto que algumas opções na verdade são…](https://ajuda.sankhya.com.br/hc/article_attachments/4407580360599)

Inicialmente, temos o campo **"Planta de Manufatura"** que é um requisito obrigatório para realizar uma análise de desvio de produção baseada em produto acabado.

O intervalo de tempo especificado no campo **"Período"** deverá ser o período correspondente a geração das notas de produção geradas pelas OPs, as quais deseja-se analisar os desvios (movimentação de estoque dos produtos).

Por meio do campo **"Agrupar Gráficos por"** você pode determinar o tipo de agrupamento de alguns gráficos auxiliares existentes na análise dos desvios de produção.

Utilize o filtro **"Produto Acabado"** quando se desejar restringir o universo da análise de desvio à um produto (PA) específico.

Para apresentar no universo de análise de desvio apenas produtos (PAs) pertencentes a um grupo de produtos específico, basta preencher o campo **"Grupo (PA)"**.

O filtro **"Matéria-prima"** é empregado para delimitar o universo de análise de desvios para apenas matérias-primas consumidas por um determinado produto acabado. Utilize apenas se o tipo de desvio envolver consumo de MP.

É possível ainda utilizar o filtro **"Nro. da OP"** para restringir o universo de análise de desvios à uma ordem de produção específica.

Quando a marcação **"Apenas PAs com desvio"** for acionada, o sistema permitirá que o resultado apresentado seja apenas aqueles produtos que sofreram variação (desvio) dado o período, diminuindo assim o universo de dados apresentados.

Existem ainda os filtros avançados, que você pode acessar por meio o botão **"Opções"**:

![Imagem 4: Existem ainda os filtros avançados, que você pode acessar por meio o botão "Opções" :](https://ajuda.sankhya.com.br/hc/article_attachments/4407580862999)

Ao acionar a marcação **"Considerar Controle"**, a análise dos desvios de produção passa a ser por produto e controle (para controle do tipo **"Lista"**). Quando a marcação estiver desligada, a análise será agrupada para todos os controles do produto.

No filtro **"MPs. fora da Composição"** selecione qual o comportamento do sistema para as matérias-primas que não pertencem a composição do PA. Ou seja, se o sistema irá **"Considerar como Desvio"** de produção ou **"Não Considerar"** as matérias-primas que não fazem parte da composição do produto acabado, mas que foram consumidas na produção do mesmo.

**Nota:** este filtro faz sentido somente em análise cujo tipo de desvio corresponda a quantidade consumida de MP (Ambos ou Consumo de MP).

Por meio do filtro **"Custo para Análise"**, indique se o custo utilizado para formar os indicadores de custo (Custo Desvio Inferior, Custo Desvio Superior, etc) será o custo de **"Reposição"** ou o custo **"Gerencial"** do produto em questão; na data correspondente a nota de produção analisada.

Defina no campo **"Cálculo de Médias"** quais OPs devem ser consideradas para o cálculo dos indicadores de média. Tem-se as seguintes opções:

- **Todas as OPs:** Ao utilizar esta opção, todas as OPs incluindo aquelas cujo produto não desviou serão consideradas no cálculo dos indicadores de média.
- **Apenas OPs com Desvios:** Ao selecionar esta opção, apenas as OPs cujo produto desviou serão consideradas no cálculo dos indicadores de média.

Indique no campo **"Tipo de Desvio"** o tipo de análise global da rotina, por meio das seguintes opções:

- **Qtd. Produzida:** Quando selecionada, a análise será efetuada de acordo com a variação da quantidade fabricada de produtos (Produto Acabado);
- **Consumo de MP:** Ao indicar essa opção, a análise será realizada conforme a variação do consumo de MP, independente da variação da quantidade fabricada de PA;
- **Ambos:** Por meio dessa opção, temos uma análise mista em função da quantidade final fabricada de produtos e consumida de materiais.

**Observação:** a opção selecionada neste campo implica nas colunas de análise que serão apresentadas na análise da primeira visão, assim como nas análise secundárias a partir da seleção de um determinado produto acabado.

Ao acionar a marcação **"Considerar MPs Alternativas"**, serão considerados os materiais alternativos das matérias-primas, ou seja, os produtos e quantidades previstas deixam de ser a Lista de MPs do produto e passam a ser o arranjo realizado no Extrato de materiais no momento de lançamento da OP, então se foi utilizado uma MP alternativa no lugar da MP principal, aquela será considerada assim como calculado seu desvio uma vez consumido uma quantidade maior que aquela definida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#top)

## Análise 1 - Visão por PAs

A primeira análise sobre os desvios de produção, diz respeito a um contexto global dado a Planta de Manufatura inserida no filtro. Ou seja, na grade de desvios são apresentados os cálculos de desvios considerando todos os Produtos Acabados fabricados na planta no período em questão, assim como todas as OPs.

![Imagem 5: A primeira análise sobre os desvios de produção, diz respeito a um contexto global dado a Planta de Manufatura inserida…](https://ajuda.sankhya.com.br/hc/article_attachments/4407581877271)

É importante ressaltar que os campos apresentados nesta visão são dinâmicos conforme o tipo de desvio selecionado no painel de filtros. Sendo que, os campos referentes a matérias-primas serão apresentados somente quando o tipo de desvio de analise corresponder a matérias-primas (Tipo de Desvio igual à **"Consumo de MP"** ou **"Ambos"**).

Existem gráficos na parte inferior da tela que permitem visualizar os desvios de quantidade e de custos do produto acabado selecionados na grade, bem como os desvios de custos dos materiais.

![Imagem 6: Existem gráficos na parte inferior da tela que permitem visualizar os desvios de quantidade e de custos do produto…](https://ajuda.sankhya.com.br/hc/article_attachments/4407589066903)

Por meio do botão **"Visão Gráfica"** localizado no topo da tela, você poderá visualizar o gráfico Custo Desvio (Todos), que disponibiliza uma visão gráfica macro dos custos de desvio do período em questão para todos os produtos. 

![Imagem 7: Por meio do botão "Visão Gráfica" localizado no topo da tela, você poderá visualizar o gráfico Custo Desvio (Todos) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4407589249175)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#top)

## Análise 2 - Visão de MPs

Tem-se na segunda análise um contexto de consumo de MPs. Ou seja, em relação ao desvio de consumo de matérias-primas. Para acessar esta visão, basta selecionar um produto (PA) na grade de Produtos Acabados e clicar sobre o botão **"Visualizar MPs"** ou efetuar um duplo clique sobre a linha do mesmo.

![Imagem 8: Tem-se na segunda análise um contexto de consumo de MPs. Ou seja, em relação ao desvio de consumo de matérias-primas.…](https://ajuda.sankhya.com.br/hc/article_attachments/4407582335511)

Nesta visão existem indicadores da quantidade de OPs sendo consideradas na análise de desvio do consumo de MP. São eles a Qtd. OPs Total (todas as OPs), Qtd. OPs Inf. (apenas OPs cujo desvio foi inferior) e Qtd. OPs Sup (apenas OPs cujo desvio foi superior).

Além disso, você pode visualizar na parte inferior da tela os gráficos que permitem analisar de forma mais ampla os detalhes sobres os desvios de quantidade e de custos da matéria-prima e produto acabado; selecionados na grade.

![Imagem 9: Além disso, você pode visualizar na parte inferior da tela os gráficos que permitem analisar de forma mais ampla os…](https://ajuda.sankhya.com.br/hc/article_attachments/4407647922967)

**Nota:** este nível de análise fica disponível apenas se o tipo de desvio de análise corresponda a consumo de MPs (Tipo de Desvio igual à **"Consumo de MP"** ou **"Ambos"**).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#top)

## Análise 3 - Visão por Ordens de Produção

Na terceira visão é possível análisar o contexto de OPs de acordo com a seleção de um produto acabado e uma matéria-prima nas visões apresentadas anteriormente.

![Imagem 10: Na terceira visão é possível análisar o contexto de OPs de acordo com a seleção de um produto acabado e uma…](https://ajuda.sankhya.com.br/hc/article_attachments/4407647943319)

Esta visão também é influenciada pelo Tipo de Desvio definido no painel de Filtros, sendo que os campos referentes a desvio de consumo de MP apenas serão apesentados caso o tipo de análise selecionada seja referente à consumo de MP (Tipo de Desvio igual à **"Consumo de MP"** ou **"Ambos"**).

O botão **"Abrir OP"** localizado no topo da tela, possibilita visualizar a ordem de produção cuja análise de desvios está sendo realizada. Bem como, um duplo clique sobre o registro.

**Nota:** esta visão pode ser o segundo nível de análise quando o **"Tipo de Desvio"** definido no painel de Filtros, estiver configurado com a opção **"Qtd. Produzida"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595954-Desvios-de-Produ%C3%A7%C3%A3o-PAs#top)
