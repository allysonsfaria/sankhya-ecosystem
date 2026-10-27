---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-double-list/"
titulo: "Double List"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-double-list/"
trilha: "Docs > Components > Components Doc > Ez Double List"
---

# Double List

O componente **ez-double-list** permite criar um mecanismo de transferências de items de uma lista **A**
para uma lista **B** e vice versa, de forma simples e rápida.

![Imagem 1: O componente ez-double-list permite criar um mecanismo de transferências de items de uma lista A para uma lista B e…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades

### slotsListBuilder

Com essa propriedade é possivel personalizar as listas( da esquerda ou da direita) adicionando elementos a esquerda ou a direita de cada item.

![Imagem 2: Com essa propriedade é possivel personalizar as listas( da esquerda ou da direita) adicionando elementos a esquerda ou…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### useOnlyRightList

Propriedade importante caso precise utilizar apenas uma lista e ter os recursos de navegação e totalizadores do ez-double-list.

![Imagem 3: Propriedade importante caso precise utilizar apenas uma lista e ter os recursos de navegação e totalizadores do…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### ezLeftListChanged

Emitido ao realizar uma alteração na **lista esquerda** do componente.

![Imagem 4: Emitido ao realizar uma alteração na lista esquerda do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezRightListChanged

Emitido ao realizar uma alteração na **lista direita** do componente.

![Imagem 5: Emitido ao realizar uma alteração na lista direita do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `emptyMessage` -- Objeto que define as mensagens a serem exibidas quando a lista está vazia Exemplo: { LEFT\_LIST?: "Lista lado esquerdo vazia.", RIGHT\_LIST?: "Lista lado direito vazia."; } `EmptyMessage` `undefined`| `entityLabel` `entity-label` Nome da entidade listada. Exemplo: "Campo", "Item", "Empresa". `string` `'item'`| `entityLabelPlural` `entity-label-plural` Variação plural do nome da entidade listada. Exemplo: "Campos", "Itens", "Empresas". `string` `'itens'`| `leftList` -- Define a lista origem. `ListItem[]` `[]`| `leftListLabel` `left-list-label` Rótulo da lista esquerda. `string` `'disponíveis'`| `leftTitle` `left-title` Define o título da lista origem. `string` `undefined`| `rightList` -- Define a lista destino. `ListItem[]` `[]`| `rightListLabel` `right-list-label` Rótulo da lista direita. `string` `'selecionados'`| `rightTitle` `right-title` Define o título da lista destino. `string` `undefined`| `slotsListBuilder` -- Objeto que define os métodos de construção dos elementos visuais para os itens de cada lista. Este objeto permite configurar dinamicamente os elementos HTML que serão exibidos ao lado esquerdo e direito dos itens em ambas as listas (`LEFT_LIST` e `RIGHT_LIST`). `DoubleListSlots` `undefined`| `useOnlyRightList` `use-only-right-list` Define se irá exibir apenas a lista da direita. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezLeftListChanged` Emitido ao realizar uma alteração na lista esquerda do componente. `CustomEvent<ListItem[]>`| `ezRightListChanged` Emitido ao realizar uma alteração na lista direita do componente. `CustomEvent<ListItem[]>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `resetSelectedLists() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-sortable-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sortable-list)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-double-list --> ez-sortable-list
  ez-double-list --> ez-button
  ez-sortable-list --> ez-filter-input
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-button --> ez-icon
  style ez-double-list fill:#f9f,stroke:#333,stroke-width:4px
```

---
