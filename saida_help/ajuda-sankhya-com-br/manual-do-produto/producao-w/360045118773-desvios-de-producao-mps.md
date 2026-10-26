---
id: "360045118773"
titulo: "Desvios de Produção (MPs)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:47Z"
rotulos: ["AJUDA DO SKW", "manual", "Custos", "Configuração", "Relatórios Gerenciais", "Desvios de Produção", "br.com.sankhya.prod.desvioproducaomp", "Desvios de Produção (MPs) manual", "Estoque", "Produção", "Conceitos Iniciais: Desvio desvio superior desvio inferior", "Painel de Filtros: Configurações e filtros disponíveis", "Visões: MPs PAs Ordens de Produção"]
---

# Desvios de Produção (MPs)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312811255831)Módulo: Produção > Consultas
```

---

Essa tela compõe uma rotina gerencial que visa o acompanhamento/análise dos desvios de produção referentes ao consumo de matérias-primas em um determinado período.

| [Conceitos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#conceitosiniciais) |  | [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#paineldefiltros) |
| --- | --- | --- |
| [Botão Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#botoopes) |  | [Visão de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#visodemps) |
| [Visão por PAs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#visoporpas) |  | [Visão por Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#visoporordensdeproduo) |

                                                          

![Imagem 2: Visão por Ordens de Produção](https://ajuda.sankhya.com.br/hc/article_attachments/1500000294342)

## Conceitos Iniciais

**Desvio:** corresponde à diferença entre a quantidade prevista e a quantidade realizada. No caso de uma análise voltada para materiais, o desvio será a diferença entre a quantidade prevista para ser consumida da matéria-prima (fórmula, lista de MPs) subtraída da quantidade consumida da mesma (qtd. apontada). Por exemplo:

Qtd. Prevista = 15UN

Qtd. Consumida = 20UN

Desvio = Qtd. Consumida – Qtd. Prevista

Desvio = 20UN – 15UN

Desvio = 5UN

**Desvio Superior:** este se refere a um desvio de valor positivo, ou seja, a quantidade consumida do material subtraída da quantidade prevista para seu consumo é maior que zero. Por exemplo:

Qtd. Prevista = 15UN

Qtd. Consumida = 20UN

Desvio = Qtd. Consumida – Qtd. Prevista

Desvio = 20UN – 15UN

Desvio = 5UN

**Desvio Inferior:** de forma contrária ao desvio anterior, o desvio inferior é um desvio de valor negativo, ou seja, a quantidade consumida do material subtraída da quantidade prevista para o consumo do mesmo, é menor que zero. Por exemplo:

Qtd. Prevista = 25UN

Qtd. Consumida = 20UN

Desvio = Qtd. Consumida – Qtd. Prevista

Desvio = 20UN – 25UN

Desvio = -5UN

**Desvio Total:** o desvio total representa o somatório dos desvios de produção, independente de serem desvios superiores ou inferiores. Logo, este indicador pode ser calculado apenas em uma análise macro onde existem várias Ordens de Produção. Por exemplo:

Ordem de Produção 1, desvio igual à 25UN

Ordem de Produção 2, desvio igual à 15UN

Ordem de Produção 3, desvio igual à -10UN

25 + 15 - 10 = 30UN

Com isso, o desvio total é igual à 30UN

**Desvio Médio:** o desvio médio corresponde ao valor médio do desvio entre várias Ordens de Produção, logo, este indicador, assim como o anterior, pode ser calculado apenas em uma análise macro contendo várias Ordens de Produção. Por exemplo:

Ordem de Produção 1, desvio igual à 25UN

Ordem de Produção 2, desvio igual à 15UN

Ordem de Produção 3, desvio igual à -10UN

(25 + 15 - 10)/3 = 10UN

Deste modo, o desvio médio é igual à 10UN

**Custo Desvio:** este custo corresponde ao custo financeiro para o desvio em questão, logo, todo indicador de desvio possui também o indicador de custo lhe acompanhando, ou seja, Custo Desvio Total, Custo Desvio Inferior, Custo Desvio Superior e Custo Desvio Médio. O valor de custo considerado no indicador, é o custo da matéria-prima na data de negociação da Nota de Produção.

**% Desvio:** o percentual de desvio se refere ao percentual ao qual a quantidade do desvio corresponde sobre a quantidade prevista para consumo do material, logo, todo indicador de desvio possui também o indicador de percentual lhe acompanhando, ou seja, % Desvio Total, % Desvio Inferior, %Desvio Superior e % Desvio Médio.

**Importante:** a rotina de Desvios de Produção (MPs) considera apenas Ordens de Produção finalizadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)

## Painel de Filtros

![Imagem 3: Painel de Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/8823762352791)

Atente-se para os dados pertinentes ao Painel de Filtros pois, alguns dos campos são alimentados por configurações prévias que, consequentemente, implicam diretamente no resultado exibido pela rotina.

**Planta de Manufatura:** a [Planta de Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119293) é uma informação obrigatória para realizar uma análise de desvio de produção com base nas matérias-primas.

**Período:** o período especificado neste campo corresponde ao período da geração das notas de produção originadas pelas Ordens de Produção as quais deseja-se analisar os desvios (movimentação de estoque dos produtos).

**Agrupar Gráficos por:** esta rotina conta com alguns gráficos auxiliares que visam enriquecer a análise dos desvios de produção. Sendo assim, é possível definir qual o tipo de agrupamento dos mesmos dentre as seguintes possibilidades:

- Dia;
- Semana;
- Mês;
- Bimestre;
- Trimestre;
- Semestre.

**Matéria Prima:** este filtro deve ser utilizado caso você queira restringir o universo da análise de desvio a uma matéria-prima específica.

**Grupo (MP):** utilize este filtro caso seja necessário restringir o universo de análise de desvio a apenas matérias-primas pertencentes a um grupo de produtos específico.

**Produto Acabado:** este filtro deve ser empregado caso você deseje delimitar o universo de análise de desvios a apenas matérias-primas consumidas por um determinado produto acabado.

**Nro. da OP:** empregue este filtro quando for necessário restringir o universo de análise de desvios a uma Ordem de Produção específica.

**Apenas MPs com desvio:** esta marcação, quando realizada, faz com que o resultado apresentado em matérias-primas seja apenas aquele referente a materiais que sofreram variação (desvio) dado o período, diminuindo assim o universo de dados apresentados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)

## Botão Opções

No alto da tela, ao lado do botão Aplicar, temos o botão **"Opções"**:

O acionamento deste botão disponibiliza alguns filtros avançados, que tem por objetivo refinar ainda mais os resultados a serem obtidos na rotina:

**Considerar Controle:** efetuando esta marcação, a análise de desvios de produção passa a considerar o controle do produto, ou seja, passa a ser por produto (matéria-prima) e controle. Quando esta marcação não estiver realizada, a análise será agrupada para todos os controles do produto (matéria prima).

**MPs. fora da Composição:** por meio desta opção, você especifica o comportamento do sistema para as matérias-primas que não pertencem a composição do Produto Acabado. São duas as possíveis definições:

- Não Considerar: as matérias-primas que não fazem parte da composição do produto acabado, mas que foram consumidas na produção do mesmo, não serão consideradas um desvio de produção;
- Considerar como Desvio: as matérias-primas que não fazem parte da composição do produto acabado, mas que foram consumidas na produção do mesmo, serão consideradas como desvio de produção.

**Custo para Análise:** defina dentre as opções abaixo, qual será o custo considerado na análise:

- **Reposição:** o custo utilizado para formar os indicadores de custo (Custo Desvio Inferior, Custo Desvio Superior etc), será o custo de Reposição da matéria-prima em questão na data correspondente a nota de produção analisada;
- **Gerencial:** o custo empregado para formar os indicadores de custo (Custo Desvio Inferior, Custo Desvio Superior etc), será o custo Gerencial da matéria-prima em questão na data correspondente a nota de produção analisada.

**Cálculo de Médias:** esta opção define quais Ordens de Produção devem ser consideradas para o cálculo dos indicadores de média. Temos as seguintes opções:

- **Todas as OPs:** por esta opção, todas as OPs incluindo aquelas cuja a matéria-prima não possui desvio, serão consideradas no cálculo dos indicadores de média;
- **Apenas OPs com Desvios:** Ao utilizar esta opção, apenas as OPs cuja matéria-prima sofreu desvio, serão consideradas no cálculo dos indicadores de média.

**Considerar MPs Alternativas:** ao realizar esta marcação, serão considerados os materiais alternativos das matérias-primas, ou seja, os produtos e quantidades previstos deixam de ser a Lista de MPs do produto e passam a ser referentes ao arranjo realizado no Extrato de Materiais no momento de lançamento da Ordem de Produção; com isso, se for utilizada uma MP alternativa no lugar da MP principal, aquela será considerada assim como será calculado seu desvio, uma vez consumindo uma quantidade maior que a definida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)

## Visão de MPs

A grade principal da tela corresponde à primeira análise pertinente aos desvios de produção que se pode realizar, diz respeito a um contexto global dada a Planta de Manufatura inserida no filtro, ou seja, na grade de desvios, são apresentados os cálculos de desvios para as matérias-primas, considerando todos os Produtos Acabados responsáveis pelo seu consumo, assim como todas as Ordens de Produção.

Temos ainda, gráficos na parte inferior da tela que permitem uma visão mais detalhada dos desvios de quantidade e de custos de matéria-prima selecionada na grade superior.

Localizado no lado superior direito da tela, o botão **"Visão Gráfica"** é responsável por apresentar um gráfico que facilita a análise dos custos dos desvios de produção:

![Imagem 4: Localizado no lado superior direito da tela, o botão "Visão Gráfica" é responsável por apresentar um gráfico que…](https://ajuda.sankhya.com.br/hc/article_attachments/8823850118807)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)

## Visão por PAs

Uma outra visão que você pode ter para realização das análises quanto aos desvios de produção dos materiais na rotina, diz respeito aos produtos acabados que consumiram uma determinada matéria-prima que sofreu desvio.

Para acessar esta visão, selecione uma matéria-prima na grade principal da tela e clique sobre o botão **"Visualizar PAs"** em destaque na imagem acima; um duplo clique sobre a linha desejada na grade principal surte o mesmo efeito.

![Imagem 5: Para acessar esta visão, selecione uma matéria-prima na grade principal da tela e clique sobre o botão "Visualizar PAs"…](https://ajuda.sankhya.com.br/hc/article_attachments/8824008801431)

Nesta visão, temos o indicador % Desvio Total PA que demonstra o percentual do desvio da matéria-prima correspondente ao desvio total da mesma, de forma que é possível ter uma visão de quais são os PAs com maior incidência de desvio do material.

Ainda nesta visão, existem indicadores da quantidade de Ordens de Produção (OPs) sendo consideradas na análise, ou seja, Qtd. OPs Total (todas as OPs), Qtd. OPs Inf. (apenas OPs cujo desvio foi inferior) e Qtd. OPs Sup. (apenas OPs cujo desvio foi superior).

A parte inferior da tela conta também com gráficos que permitem uma visualização de maiores detalhes sobre os desvios de quantidade, de custos da matéria-prima e produto acabado selecionados na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)

## Visão por Ordens de Produção

Uma terceira e última visualização possível de ser realizada quanto aos desvios de produção dos materiais na rotina, corresponde às Ordens de Produção, dada a seleção de uma matéria-prima e um produto acabado nas visões apresentadas anteriormente ([Visão de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#visodemps) e [Visão por PAs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#visoporpas)). Esta visão ocorre através do botão **"Visualizar OPs"**:

![Imagem 6: Uma terceira e última visualização possível de ser realizada quanto aos desvios de produção dos materiais na rotina,…](https://ajuda.sankhya.com.br/hc/article_attachments/8824067460759)

Além de analisar o desvio da matéria-prima do produto acabado selecionado em cada uma das Ordens de Produção para o período em questão, podemos abrir a ordem de produção na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) por meio do botão **"Abrir OP"**; um duplo clique sobre o registro desejado, executa este mesmo comportamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118773-Desvios-de-Produ%C3%A7%C3%A3o-MPs#top)
