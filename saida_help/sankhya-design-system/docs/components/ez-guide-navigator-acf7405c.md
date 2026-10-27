---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator/"
titulo: "Guide Navigator"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator/"
trilha: "Docs > Components > Components Doc > Ez Guide Navigator"
---

# Guide Navigator

Componente responsável por exibir uma navegação baseando em guias.

![Imagem 1: Componente responsável por exibir uma navegação baseando em guias.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Carregamento sob demanda

Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica.
Para isso basta atribuir ao atributo "children" do item, uma função. Veja:

![Imagem 2: Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica. Para isso basta…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades

### Atribuição de dados

> Propriedade utilizada **items**

A exemplo do componente [EzTree](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tree), os dados desse componente são atribuídos no formato de um array. Cada elemento pode ter uma lista de elementos filhos, formando assim uma estrutura hierárquica.

![Imagem 3: A exemplo do componente EzTree , os dados desse componente são atribuídos no formato de um array. Cada elemento pode…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Visibilidade do componente

> Propriedade utilizada **open**

Para definir por padrão o componente fechado, basta atribui o valor **false** à propriedade `open`.

![Imagem 4: Para definir por padrão o componente fechado, basta atribui o valor false à propriedade open .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Personalização de tooltip

> Propriedade utilizada: **tooltipResolver**

Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.

![Imagem 5: Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Tooltip por item

A exemplo dos ícones, o próprio item consegue determinar seu tooltip.

![Imagem 6: A exemplo dos ícones, o próprio item consegue determinar seu tooltip.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Principais métodos

#### enableItem

Para habilitar itens, use um único id ou uma lista para habilitar vários de uma vez.

![Imagem 7: Para habilitar itens, use um único id ou uma lista para habilitar vários de uma vez.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### disableItem

Usado para desabilitar itens. Pode receber um único id ou uma lista.

![Imagem 8: Usado para desabilitar itens. Pode receber um único id ou uma lista.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `items` -- Lista de itens do menu de navegação. `IGuideItem[]` `[]`| `open` `open` Define se o menu de navegação está aberto. `boolean` `true`| `selectedId` `selected-id` Define o id do item selecionado. `string` `undefined`| `tooltipResolver` -- Define uma função que vai resolver o `tooltip` ou `title` daquele item. `(item: IGuideItem, enabled: boolean, level: number) => string` `undefined` | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezSelectionChange` Evento emitido quando o item selecionado no navigator é alterado. `CustomEvent<IGuideItem>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `disableItem(id: string | Array<string>) => Promise<void>`

Desabilita um ou mais itens.

##### Returns

Type: `Promise<void>`

---

#### `enableItem(id: string | Array<string>) => Promise<void>`

Habilita um ou mais itens.

##### Returns

Type: `Promise<void>`

---

#### `getCurrentPath() => Promise<Array<IGuideItem>>`

Obtem um array do caminho de itens da seleção atual.

##### Returns

Type: `Promise<IGuideItem[]>`

Retorna um array do caminho de itens da seleção atual.

---

#### `getItem(id: string) => Promise<IGuideItem>`

Obtem um item pelo id

##### Returns

Type: `Promise<IGuideItem>`

---

#### `getParent(id: string) => Promise<IGuideItem>`

Obtem o item pai a partir de um id

##### Returns

Type: `Promise<IGuideItem>`

---

#### `openGuideNavidator() => Promise<void>`

Abre o navegador de Guia

##### Returns

Type: `Promise<void>`

---

#### `selectGuide(id: string) => Promise<void>`

Seleciona o item desejado pelo ID.

##### Returns

Type: `Promise<void>`

---

#### `updateItem(item: IGuideItem | Array<IGuideItem>) => Promise<void>`

Atualiza um ou mais items

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-sidebar-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-button)
- [ez-filter-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [ez-scroller](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scroller)
- [ez-tree](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tree)

#### Graph

```
graph TD;
  ez-guide-navigator --> ez-sidebar-button
  ez-guide-navigator --> ez-filter-input
  ez-guide-navigator --> ez-button
  ez-guide-navigator --> ez-scroller
  ez-guide-navigator --> ez-tree
  ez-sidebar-button --> ez-icon
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-button --> ez-icon
  ez-tree --> ez-icon
  style ez-guide-navigator fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-guide-navigator--padding-left Define o espaçamento da esquerda do container| --ez-guide-navigator--padding-right Define o espaçamento da direita do container| --ez-guide-navigator--box-shadow Define a cor de shadow box do container de label| --ez-guide-navigator--background-color Define a cor de fundo do container de label| --ez-guide-navigator--border-radius Define o border radius do container de label| --ez-guide-navigator--actions-gap Define o espaçamento entre as ações| --ez-guide-navigator--actions-margin Define a margem vertical do elemento| --ez-guide-navigator--actions-padding-right Define o espaçamento da direita do elemento | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
