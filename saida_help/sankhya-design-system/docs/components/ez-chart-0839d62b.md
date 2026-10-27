---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chart/"
titulo: "Chart"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chart/"
trilha: "Docs > Components > Components Doc > Ez Chart"
---

# Chart

O componente `ez-chart` é utilizado para renderizar gráficos com base em séries de dados fornecidas. Ele permite a personalização dos gráficos através de várias propriedades, proporcionando flexibilidade para atender diferentes necessidades.

![Imagem 1: O componente ez-chart é utilizado para renderizar gráficos com base em séries de dados fornecidas. Ele permite a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alteração de largura e altura

Utilize as propriedade `width` e `height` sempre passando os valores em pixel somente números

## Como adicionar Título e Subtítulo

Utilize a propriedade `chartTitle` para definir o título que aparecerá no gráfico.

Utilize a propriedade `chartSubTitle` para definir o subtítulo que aparecerá no gráfico.

## Como Desativar as Legendas

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` não possui legenda

## Como Definir as Séries

É possível definir as `series` como um `ChartSerie` ou um `Array<ChartSerie>`.

- Utilize a propriedade `name` para definir o nome da sua série.
- Utilize a propriedade `color` para definir a cor da sua série.
- Por padrão, os rótulos dos valores não são exibidos no gráfico. Use a propriedade `showDataLabel` com valor `true` para exibi-los.
- Utilize a propriedade `type` para definir o tipo individual da série.

Importante

A propriedade **type** definida na série sobrepõe a propriedade `type` do gráfico de forma individual para cada série. Pode ser definida como `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

## Personalizar `data` de uma Série

Os dados (`data`) de uma série podem ser definidos como um array de números ou um array de objetos `ChartSerieData`.

Para detalhes específicos em cada valor da série, utilize `ChartSerieData`, definindo as propriedades `y`, `name`, e `color` (opcional).

- A propriedade `y` é do tipo `number` e define o valor no eixo y.
- A propriedade `name` é do tipo `string` e define um nome para o valor da série.
- A propriedade `color` (opcional) é do tipo `string` e define uma cor para o ponto da série.

Ao visualizar o tooltip padrão, verá que ele exibe a propriedade `name` definida em cada ponto da série, com cores distintas.

## Formatar Tooltip da Série

É possível definir um tooltip personalizado para cada série através de uma função de formatação.

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

Importante

- É necessário definir um **name** para a série, pois ele é usado para identificar o tooltip.
- O tooltip deve ser definido individualmente para cada série que deseja personalizar.

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` possui outros parametros para formatar o tooltip, vejo com detalhe na sua propria sessão

## Personalização dos Eixos

Importante

Gráficos ou series do `type` definido como `'pie'` ou `'donut'` não tuiliza a propriedade `xAxis` e `yAxis` e não possuí personalização dos eixos

É possível personalizar os eixos dos gráficos, alterando a descrição, a cor, e definindo categorias que podem ser personalizadas usando um formatter.

### Personalização da Descrição

- Utilize a propriedade `text` para adicionar uma descrição no eixo do gráfico.
- Utilize a propriedade `color` para alterar a cor da descrição adicionada no eixo.

### Personalização das Categorias

- Utilize a propriedade `categories` para inserir um `Array<string>` que substitui os números por texto no eixo.
- Utilize a propriedade `formatter` para personalizar o estilo dos valores no eixo.

### Múltiplos Eixos

Você pode criar um eixo secundário ou múltiplos eixos.

- Passe um `Array<ChartAxis>` e defina quais séries devem usar diferentes eixos.
- Na série, defina a propriedade `yAxis` com o índice do eixo definido.
- Também é possível usar a propriedade `invertedPosition` para inverter a posição do eixo.

## Interação com gráfico

- Utilize a propriedade `onEzSerieClick` chamar uma função de callback com informações da serie clicada

![Imagem 2: Utilize a propriedade onEzSerieClick chamar uma função de callback com informações da serie clicada](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Linha

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

![Imagem 3: Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade type para definir outros…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Coluna

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de coluna utilize o `type`: `'column'`

![Imagem 4: Para um gráfico de coluna utilize o type : 'column'](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Linha e Coluna

Utilizando um Array de `series`, você pode criar um gráfico combinando linha e coluna, onde o `type` de uma serie deve ser `'column'` e o `type` da outra serie deve ser `'line'`

![Imagem 5: Utilizando um Array de series , você pode criar um gráfico combinando linha e coluna, onde o type de uma serie deve ser…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Barra

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de barra utilize o `type`: `'bar'`

Importante

- Quando definimos o tipo do gráfico como barra (`'bar'` ) os eixos são invertidos, sendo que o eixo Y fica na horizontal e o eixo X na vertical, mesmo uma serie do tipo coluna, ficaria na horizontal

![Imagem 6: Quando definimos o tipo do gráfico como barra ( 'bar' ) os eixos são invertidos, sendo que o eixo Y fica na horizontal…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Pizza

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de pizza utilize o `type`: `'pie'`

Importante

- Quando definimos o tipo do gráfico como (`'pie'` ou `'donut'` ) não é utilizado as propriedades `'xAxis'` e `'yAxis'`

Importante

Não é recomendado utilizar varias series com o `type` definido como `'pie'` pois pode haver sobreposição

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` não possui legenda

Importante

- É interessante definir a propriedade `name` para o `data` as `series` para que seja exibido um nome para as fatias

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

![Imagem 7: Na série, defina a propriedade toolTipFormatter , que deve ser uma função que recebe os seguintes parâmetros:…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Gráfico de Donut

Por padrão, o gráfico renderizado é do tipo linha. No entanto, é possível passar a propriedade `type` para definir outros tipos de gráficos, como: `'column'`, `'bar'`, `'line'`, `'pie'` ou `'donut'`.

Para um gráfico de Donut utilize o `type`: `'donut'`

Importante

- Quando definimos o tipo do gráfico como (`'pie'` ou `'donut'` ) não é utilizado as propriedades `'xAxis'` e `'yAxis'`

Importante

Não é recomendado utilizar varias series com o `type` definido como `'pie'` pois pode haver sobreposição

A propriedade `legendEnabled` permite ocultar ou exibir a legenda do gráfico, que por padrão é exibida.

Importante

Gráficos ou series do `type` definido como `'pie'` não possui legenda

Importante

- É interessante definir a propriedade `name` para o `data` as `series` para que seja exibido um nome para as fatias

Na série, defina a propriedade `toolTipFormatter`, que deve ser uma função que recebe os seguintes parâmetros: `(serieName: string, xAxis: string | number, yAxis: number, dataName: string, percentage: number)` e retorna uma string HTML com a formatação desejada.

![Imagem 8: Na série, defina a propriedade toolTipFormatter , que deve ser uma função que recebe os seguintes parâmetros:…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
