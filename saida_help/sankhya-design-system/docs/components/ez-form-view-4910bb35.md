---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view/"
titulo: "Form View"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view/"
trilha: "Docs > Components > Components Doc > Ez Form View"
---

# Form View

Esse componente é responsável por criar os campos e distribuí-los responsivamente no espaço disponível. Ele é usado pelo [EzForm](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/) para diagramar o conteúdo interno

IMPORTANTE

##### [EzForm](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/) vs. EzFormView

Ao contrário [EzForm](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/) que cuida de todo o fluxo de dados, o EzFormView somente cria a estrutura dos campos.

![Imagem 1: Ao contrário EzForm que cuida de todo o fluxo de dados, o EzFormView somente cria a estrutura dos campos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Atribuindo metadados

> Propriedade utilizada: **fields**

Atribuindo um array com objetos tipo `IFormViewField`, para cada elemento será criado um campo, respeitando
o `UserInterface`. Os campos serão envolvidos em uma estrutura responsiva (ajustável de acordo com o espaço disponível),
automatizando o trabalho de diagramá-los.

![Imagem 2: Atribuindo um array com objetos tipo IFormViewField , para cada elemento será criado um campo, respeitando o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Observação

Os campos serão apenas adicionados ao DOM, sem qualquer tipo de bind ou tratamento de eventos específicos. Todos os campos
terão o atributo `data-field-name` preenchido, sendo possível acessá-los através de queryString.

### Grupos

> Propriedade utilizada: **IFormViewField.group**

Usado para organizar os campos em grupos, além de permitir que o usuário se concentre em um grupo por vez, contraindo os outros.

![Imagem 3: Usado para organizar os campos em grupos, além de permitir que o usuário se concentre em um grupo por vez, contraindo…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Campos sinalizados como requerido

> Propriedade utilizada: **IFormViewField.required**

Campos requeridos são sinalizados visualmente.

![Imagem 4: Campos requeridos são sinalizados visualmente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Observação

Não há validação de preenchimento, apenas a sinalização.

### Campos com edição desabilitada

> Propriedade utilizada: **IFormViewField.readOnly**

Em várias situações, pode ser necessário exibir o valor do campo, mas mantendo-o inativo para edição.

![Imagem 5: Em várias situações, pode ser necessário exibir o valor do campo, mas mantendo-o inativo para edição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Campos com elementos nas extremidades

Permite a adição de elementos nas extremidades do formulário,
incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

![Imagem 6: Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alterção dinâmica de props

É possível alterar dinamicamente propriedades de campos através do método **setFieldProp** do componente.

## Editores customizados

Através do método **addCustomEditor**, é possível adicionar editores customizados (**ICustomEditor**) no lugar de campos do formulário.
Quando nenhum editor customizado é adicionado à coluna, seu campo padrão é renderizado.

Existem quatro retornos possíveis para o métodoo **getEditorElement** do **ICustomEditor**, sendo eles:

- **Nulo/indefinido**: renderiza o elemento padrão para aquele campo;
- **O elemento padrão**: renderiza o elemento padrão para aquele campo;
- **Uma string**: faz o parse da string e renderiza o elemento passado;
- **Um elemento HTML**: renderiza o elemento.

Importante

O método **renderToString** não aceita **nenhum** código javascript.
Para um botão, por exemplo, um onClick não irá funcionar.
O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTMLAllCollection.

![Imagem 7: O método renderToString não aceita nenhum código javascript. Para um botão, por exemplo, um onClick não irá funcionar.…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `fields` -- Define a lista de metadados usada para criar os campos de user interface. `IFormViewField[]` `undefined`| `selectedRecord` -- Define os registros da linha selecionada. `Record` `undefined`| `singleColumn` `single-column` Define se o formulario deve possuir apenas 1 coluna. `boolean` `false` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezContentReady` Evento emitido quando o componente foi totalmente carregado na DOM. `CustomEvent<HTMLElement[]>`| `formItemsReady` Responsável por notificar quando ocorrer a renderização de itens do formulário. `CustomEvent<FormItems>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

---

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metados do campo.

##### Returns

Type: `Promise<void>`

---

#### `showUp() => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-filter](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter)
- [ez-form](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form)

#### Depends on

- [ez-custom-form-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view/custom-input)
- [ez-collapsible-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-collapsible-box)
- [ez-check](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-check)
- [ez-combo-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box)
- [ez-date-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input)
- [ez-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-time-input)
- [ez-date-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-time-input)
- [ez-upload](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-upload)
- [ez-number-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-number-input)
- [ez-text-area](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-area)
- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-search-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)
- [ez-rich-text](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text)
- [ez-multi-select-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input)

#### Graph

```
graph TD;
  ez-form-view --> ez-custom-form-input
  ez-form-view --> ez-collapsible-box
  ez-form-view --> ez-check
  ez-form-view --> ez-combo-box
  ez-form-view --> ez-date-input
  ez-form-view --> ez-time-input
  ez-form-view --> ez-date-time-input
  ez-form-view --> ez-upload
  ez-form-view --> ez-number-input
  ez-form-view --> ez-text-area
  ez-form-view --> ez-text-input
  ez-form-view --> ez-search-plus
  ez-form-view --> ez-search
  ez-form-view --> ez-rich-text
  ez-form-view --> ez-multi-select-input
  ez-collapsible-box --> ez-icon
  ez-collapsible-box --> ez-text-edit
  ez-text-edit --> ez-text-input
  ez-text-edit --> ez-button
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-button --> ez-icon
  ez-combo-box --> ez-text-input
  ez-combo-box --> ez-icon
  ez-combo-box --> ez-popover-plus
  ez-combo-box --> ez-combo-box-list
  ez-popover-plus --> ez-popover-core
  ez-date-input --> ez-text-input
  ez-date-input --> ez-popover-plus
  ez-date-input --> ez-calendar
  ez-time-input --> ez-text-input
  ez-time-input --> ez-icon
  ez-date-time-input --> ez-text-input
  ez-date-time-input --> ez-popover-plus
  ez-date-time-input --> ez-calendar
  ez-number-input --> ez-text-input
  ez-text-area --> ez-tooltip
  ez-text-area --> ez-icon
  ez-search-plus --> ez-icon
  ez-search-plus --> ez-text-input
  ez-search-plus --> ez-popover-plus
  ez-search-plus --> ez-search-result-list
  ez-search-result-list --> ez-card-item
  ez-search-result-list --> ez-skeleton
  ez-search --> ez-text-input
  ez-search --> ez-icon
  ez-search --> ez-popover-plus
  ez-search --> search-list
  search-list --> ez-card-item
  ez-rich-text --> ez-text-area
  ez-rich-text --> ez-rich-toolbar
  ez-rich-text --> ez-link-builder
  ez-rich-text --> ez-simple-image-uploader
  ez-rich-toolbar --> ez-rich-toolbar-arrows
  ez-rich-toolbar --> ez-rich-toolbar-letters
  ez-rich-toolbar --> ez-rich-toolbar-configs
  ez-rich-toolbar-arrows --> ez-rich-toolbar-item
  ez-rich-toolbar-item --> ez-icon
  ez-rich-toolbar-letters --> ez-rich-toolbar-item
  ez-rich-toolbar-configs --> ez-rich-toolbar-item
  ez-link-builder --> ez-popup
  ez-link-builder --> ez-modal-container
  ez-link-builder --> ez-text-input
  ez-link-builder --> ez-check
  ez-popup --> ez-button
  ez-modal-container --> ez-icon
  ez-modal-container --> ez-button
  ez-simple-image-uploader --> ez-popup
  ez-simple-image-uploader --> ez-modal-container
  ez-simple-image-uploader --> ez-tooltip
  ez-simple-image-uploader --> ez-text-input
  ez-simple-image-uploader --> ez-icon
  ez-multi-select-input --> ez-icon
  ez-multi-select-input --> ez-tooltip
  ez-multi-select-input --> ez-popover-core
  ez-multi-select-input --> ez-multi-selection-list
  ez-multi-selection-list --> ez-check
  ez-multi-selection-list --> ez-list
  ez-multi-selection-list --> ez-icon
  ez-multi-selection-list --> multi-selection-box-message
  ez-multi-selection-list --> ez-filter-input
  ez-multi-selection-list --> ez-search
  ez-list --> ez-check
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  ez-filter --> ez-form-view
  ez-form --> ez-form-view
  style ez-form-view fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-form-view\_\_item--min-width Define o tamanho mínimo dos itens do formulário.| --ez-form-view\_\_item--max-width Define o tamanho máximo dos itens do formulário.| --ez-form-view\_\_item--width Define o espaçamento entre itens do formulário.| --ez-form-view\_\_item--padding Define o padding do formulário. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
