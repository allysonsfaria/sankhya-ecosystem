---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list/"
titulo: "Multi Selection List"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list/"
trilha: "Docs > Components > Components Doc > Ez Multi Selection List"
---

# Multi Selection List

`<EzMultiSelectionList />` é um componente versátil que permite aos usuários selecionar múltiplos itens de uma lista. O componente oferece duas formas principais de renderização: através de uma lista estática de opções (`options`) ou através de um callback dinâmico (`dataSource`) que permite busca no backend.

![Imagem 1: <EzMultiSelectionList /> é um componente versátil que permite aos usuários selecionar múltiplos itens de uma lista. O…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Renderização com `options`

A propriedade `options` recebe uma lista do tipo `IMultiSelectionOption` e renderiza essa lista com checkboxes. Cada opção possui:

- `label`: Texto exibido para o usuário
- `value`: Valor único para identificação
- `check`: Estado inicial (selecionado ou não)

Importante

Para que o filtro funcione corretamente com `options`, você deve definir `useOptions={true}`.

![Imagem 2: Para que o filtro funcione corretamente com options , você deve definir useOptions={true} .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Renderização com `dataSource`

A propriedade `dataSource` permite integração dinâmica com backends, oferecendo busca em tempo real e carregamento sob demanda.

O `IMultiSelectionListDataSource` deve implementar:

- `fetchData(filterTerm, fieldName)`: Callback que retorna uma Promise com os dados filtrados
- `sortItems(column, items)`: Função para ordenação dos resultados

Importante

Para a utilização de `dataSource`, é necessário definir a propriedade `columnName`.

![Imagem 3: Para a utilização de dataSource , é necessário definir a propriedade columnName .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

O componente oferece o evento `onChangeFilteredOptions` para capturar alterações na seleção. Este
evento é disparado sempre que a seleção é alterada, permitindo que você reaja a essas mudanças.

Observação

Ao selecionar ou desmarcar itens, o objeto passado para a propriedade `options` é atualizado automaticamente.

![Imagem 4: Ao selecionar ou desmarcar itens, o objeto passado para a propriedade options é atualizado automaticamente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos:

O componente `EzMultiSelectionList` oferece um método para a limpeza dos itens adicionados:

- **`clearFilteredOptions()`**: Limpa a seleção atual

![Imagem 5: clearFilteredOptions() : Limpa a seleção atual](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `columnName` `column-name` Nome da coluna onde serão aplicadas as opções selecionadas. `string` `undefined`| `dataSource` -- Classe que implementa o método fetchData, responsável por realizar a pesquisa dos dados, com base no termo informado pelo usuário. `IMultiSelectionListDataSource` `undefined`| `isTextSearch` `is-text-search` Informa se a pesquisa é do tipo texto ou numérico. `boolean` `false`| `options` -- Opções de filtros a serem exibidas na listagem. `IMultiSelectionOption[]` `undefined`| `orderSelectedFirst` `order-selected-first` Define se as opções marcadas devem ser reordenadas para o topo da lista (e ordenadas alfabeticamente/pelo datasource). Quando `false`, a ordem original das opções é preservada — inclusive ao marcar/desmarcar itens. Padrão: `true` (mantém o comportamento histórico). `boolean` `true`| `useOptions` `use-options` Indica se deve ser exibida lista de opções do atributo options (true), ou se deve utilizar o datasource (false) `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `changeFilteredOptions` Evento que informa que a lista de opções selecionadas sofreu alteração. `CustomEvent<IMultiSelectionOption[]>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `clearFilteredOptions() => Promise<void>`

##### Returns

Type: `Promise<void>`

---

#### `clearSelection() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-multi-select-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input)
- [filter-column](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/subcomponents)

#### Depends on

- [ez-check](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-check)
- [ez-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-list)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [multi-selection-box-message](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list/subcomponents)
- [ez-filter-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)

#### Graph

```
graph TD;
  ez-multi-selection-list --> ez-check
  ez-multi-selection-list --> ez-list
  ez-multi-selection-list --> ez-icon
  ez-multi-selection-list --> multi-selection-box-message
  ez-multi-selection-list --> ez-filter-input
  ez-multi-selection-list --> ez-search
  ez-list --> ez-check
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-search --> ez-text-input
  ez-search --> ez-icon
  ez-search --> ez-popover-plus
  ez-search --> search-list
  ez-popover-plus --> ez-popover-core
  search-list --> ez-card-item
  ez-multi-select-input --> ez-multi-selection-list
  filter-column --> ez-multi-selection-list
  style ez-multi-selection-list fill:#f9f,stroke:#333,stroke-width:4px
```

---
