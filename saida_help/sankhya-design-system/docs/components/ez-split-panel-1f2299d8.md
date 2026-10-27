---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-panel/"
titulo: "Split Panel"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-panel/"
trilha: "Docs > Components > Components Doc > Ez Split Panel"
---

# Split Panel

## Painel

O componente `SplitPanel` é um painel com múltiplas divisões internas, onde cada divisão pode ser redimensionada individualmente pelo usuário.
O objetivo desse painel é receber outros componentes e permitir um layout mais dinâmico.

![Imagem 1: O componente SplitPanel é um painel com múltiplas divisões internas, onde cada divisão pode ser redimensionada…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Direção de itens

A propriedade `direction` define qual será o sentido que o painel será divido.

#### Column

![Imagem 2: Column](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Row

![Imagem 3: Row](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Definir âncora para expandir item

Por padrão, cada divisão pode ser expandida. A propriedade
`anchorToExpand` no `EzSplitPanel` irá definir que esse elemento é o limite para o item filho expandir,
caso não seja passada nenhuma âncora, o item será expandido para a primeira posição relativa que encontrar

![Imagem 4: Por padrão, cada divisão pode ser expandida. A propriedade anchorToExpand no EzSplitPanel irá definir que esse elemento…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `anchorToExpand` `anchor-to-expand` Responsável por definir o painel que limita o tamanho do item expandido. `boolean` `false`| `direction` `direction` `"column" | "row"` `'column'`| `structural` `structural` Define se o painel está sendo utilizado como estrutura para apresentação de outro item `boolean` `false` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `resizeEnd` `CustomEvent<IPanelSizeInfo>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `rebuildLayout() => Promise<void>`

##### Returns

Type: `Promise<void>`

---

## Item

Cada `EzSplitItem` representa uma divisão do painel e pode ter seu tamanho ajustado pelo usuário através de um controle visual intuitivo.

![Imagem 5: Cada EzSplitItem representa uma divisão do painel e pode ter seu tamanho ajustado pelo usuário através de um controle…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Título

Os items podem receber títulos através da propriedade `label`.

![Imagem 6: Os items podem receber títulos através da propriedade label .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Slot à esquerda do título

Podemos adicionar um conteudo dinâmico à esquerda do título, passando o slot `leftButtons`.

observação

À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.

![Imagem 7: À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Slot à direita do título

Podemos adicionar um conteudo dinâmico à esquerda do título, passando o slot `rightButtons`.

observação

À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.

![Imagem 8: À medida que largura da tela for diminuindo e e o titulo for muito grande, é adicionado "..." ao título.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitar expansão

A propriedade `enableExpand` define se o componente pode ser expandido

![Imagem 9: A propriedade enableExpand define se o componente pode ser expandido](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho inicial

A propriedade `size` define o espaço que o item irá ocupar no painel.
Ela pode ser definida através das medidas `fr` e `%`

#### Usando `fr`

![Imagem 10: Usando fr](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Usando `%`

![Imagem 11: Usando %](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos.

#### Evento emitido ao redimensionar o painel.

![Imagem 12: Evento emitido ao redimensionar o painel.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enableExpand` `enable-expand` Define se o item pode ser expandido `boolean` `true`| `label` `label` Define um título para o painel. `string` `undefined`| `size` `size` Define o tamanho inicial do painel. `string` `undefined`| `structural` `structural` Define se o painel está sendo utilizado como estrutura para apresentação de outro item `boolean` `false` | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/ez-button)

#### Graph

```
graph TD;
  ez-split-item --> ez-button
  ez-button --> ez-icon
  style ez-split-item fill:#f9f,stroke:#333,stroke-width:4px
```

---
