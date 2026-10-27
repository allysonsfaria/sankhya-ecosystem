---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/grid-system/"
titulo: "Grid System"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/grid-system/"
trilha: "Docs > Components > Layout Doc > Grid System"
---

# Grid System

O sistema de grids do CSS3 visa permitir que o conteúdo dos elementos possam ser divididos em um conteúdo de grade.
Com o Grid System usa-se uma série de containers, linhas e colunas para
fazer o layout e alinhar o conteúdo. É construído com flexbox e é totalmente responsivo.

## Como funciona

O sistema de grid possui elementos que dividi-se em linhas e colunas, as linhas organizam os elementos
internos que podem ser colunas ou outro elemento desejado.

### Linhas

No sistema de grid é possível utilizar elementos de linha para organizar seus elementos internos,
basta utilizar a classe CSS `ez-row`, conforme o exemplo a seguir:

![Imagem 1: No sistema de grid é possível utilizar elementos de linha para organizar seus elementos internos, basta utilizar a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Colunas

Para utilizar elementos de colunas, basta utilizar a classe CSS `ez-col`. Cada linha do grid possui 12 colunas,
então para posicionar os elementos em seu interior são utilizadas classes com prefixos pré-definidos que irão ocupar a
quantidade desejada de colunas para uma determinada linha, segue um exemplo de como ocupar uma linha com
três elementos internos:

![Imagem 2: Para utilizar elementos de colunas, basta utilizar a classe CSS ez-col . Cada linha do grid possui 12 colunas, então…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Linhas e Colunas

Para entender melhor o uso de quantidade desejada de colunas, segue um exemplo com várias linhas,
e com quantidades específicas de colunas para cada linha:

![Imagem 3: Para entender melhor o uso de quantidade desejada de colunas, segue um exemplo com várias linhas, e com quantidades…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Prefixos de resoluções

Para que funcione corretamente o uso do grid para determinadas resoluções, o correto é usar a combinação
de classes com prefixos que determinam até qual resolução aquela quantidade de colunas irá obedecer para
aquele determinado elemento. Ou seja, com estes prefixos, o elemento irá ocupar a quantidade desejada de
colunas a partir de uma resolução mínima, e abaixo desta resolução, o elemento irá ocupar toda a largura da tela.

A seguir seguem alguns exemplos para cada prefixo:

### Small Devices

Prefixo para adaptar em resolução de dispositivos pequenos.

#### sd (min-width: 320px)

Para que a coluna respeite a resolução mínima de até **320px** de largura, utiliza-se o prefixo `--sd-`.

![Imagem 4: Para que a coluna respeite a resolução mínima de até 320px de largura, utiliza-se o prefixo --sd- .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Phones

Prefixo para adaptar em resolução de smartphones.

#### pn (min-width: 480px)

Para que a coluna respeite a resolução mínima de até **480px** de largura, utiliza-se o prefixo `--pn-`.

![Imagem 5: Para que a coluna respeite a resolução mínima de até 480px de largura, utiliza-se o prefixo --pn- .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tablets

Prefixo para adaptar em resolução de tablets.

#### tb (min-width: 768px)

Para que a coluna respeite a resolução mínima de até **768px** de largura, utiliza-se o prefixo `--tb-`.

![Imagem 6: Para que a coluna respeite a resolução mínima de até 768px de largura, utiliza-se o prefixo --tb- .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Medium Devices

Prefixo para adaptar em resolução de dispositivos médios.

#### md (min-width: 992px)

Para que a coluna respeite a resolução mínima de até **992px** de largura, utiliza-se o prefixo `--md-`.

![Imagem 7: Para que a coluna respeite a resolução mínima de até 992px de largura, utiliza-se o prefixo --md- .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Large Devices

Prefixo para adaptar em resolução de dispositivos grandes.

#### ld (min-width: 1200px)

Para que a coluna respeite a resolução mínima de até **1200px** de largura, utiliza-se o prefixo `--ld-`.

![Imagem 8: Para que a coluna respeite a resolução mínima de até 1200px de largura, utiliza-se o prefixo --ld- .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Combinação de prefixos

Para projetos que sejam totalmente responsivos, é possível utilizar a combinação dos prefixos apresentados
anteriormente, e evitar a quebra de layout em determinada resolução. A seguir, será apresentado um
exemplo de como utilizar essa combinação, na qual serão utilizados todos os prefixos,
e cada elemento interno da linha seguirá as seguintes regras:

| Prefixo Resolução Mínima Qtd. Colunas Ocupadas| ld >= 1200px 1| md >= 992px 2| tb >= 768px 3| pn >= 480px 4| sd >= 320px 6| -- < 320px 12 | | | | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

![Imagem 9: 12](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
