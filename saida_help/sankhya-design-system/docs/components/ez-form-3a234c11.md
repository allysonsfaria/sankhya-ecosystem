---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/"
titulo: "Form"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form/"
trilha: "Docs > Components > Components Doc > Ez Form"
---

# Form

Documentação do componente EzForm.

![Imagem 1: Documentação do componente EzForm.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Com config

Com configuração do formulário.

Observação

Os atributos `readOnly` e `required` dos campos vindos no metadata do dataUnit, com valor `true`,
terão prioridade sobre os mesmos atributos inseridos na config.
Por exemplo, se o campo `Nome do cliente` vier com `required: true` no metadata do dataUnit,
este mesmo atributo do campo na config, não será considerado.

![Imagem 2: Os atributos readOnly e required dos campos vindos no metadata do dataUnit, com valor true , terão prioridade sobre os…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Conteúdo estático

É possível criar conteúdo específico sem o uso de quaisquer tipos de metainformações.
Neste contexto, o formulário fará o vínculo entre os campos (EzTextInput, EzDateInput, etc...)
e o DataUnit, além de validar os registros. Para isso, é preciso fornecer o atributo
**data-field-name** para cada campo.

![Imagem 3: É possível criar conteúdo específico sem o uso de quaisquer tipos de metainformações. Neste contexto, o formulário fará…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com abas e grupos

Às vezes é necessário organizar os campos em abas e grupos, assim a interface fica mais objetiva
e específica, permitindo que o usuário se concentre em um ponto por vez.

![Imagem 4: Às vezes é necessário organizar os campos em abas e grupos, assim a interface fica mais objetiva e específica,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Validate

Exemplo de como validar o formulário.

![Imagem 5: Exemplo de como validar o formulário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com recordsValidator

Define um validador responsável pela integridade dos registros.

Observação

No exemplo a seguir, está sendo validado o valor do campo Desconto, que não pode ser valor zero (R$ 0,00).

![Imagem 6: No exemplo a seguir, está sendo validado o valor do campo Desconto, que não pode ser valor zero (R$ 0,00).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com elementos nas extremidades

Permite a adição de elementos nas extremidades do formulário,
incluindo botões, ícones, badges ou qualquer outro elemento desejado.

Observação

Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.

![Imagem 7: Esses elementos podem ser clicáveis e permitir o redirecionamento para telas externas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Submit

Exemplo de como utilizar o submit.

![Imagem 8: Exemplo de como utilizar o submit.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Cancel

Exemplo de como cancelar edição no formulário.

![Imagem 9: Exemplo de como cancelar edição no formulário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais componentes

A seguir temos a arquitetura do ez-form, apresentando seus principais componentes e como eles interagem ente si.

[![Imagem 10: A seguir temos a arquitetura do ez-form, apresentando seus principais componentes e como eles interagem ente si.](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/ez-form/diagram.jpg)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/ez-form/diagram.jpg)

#### Processo de updateValue

Arquitetura apresentando o processo de updateValue dos campos do formulário.

[![Imagem 11: Arquitetura apresentando o processo de updateValue dos campos do formulário.](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/ez-form/diagram-update.jpg)](https://gilded-nasturtium-6b64dd.netlify.app/img/demos/ez-form/diagram-update.jpg)

#### DataBinder

Realiza o processo de construção dos campos de acordo com o DataUnit, cria os eventos de controle de ações
(`DATA_SAVED`, `DATA_CHANGED`, `RECORDS_ADDED`, etc.) e atualiza os campos do formulário de acordo com esses eventos.

#### form.slice

Reducer utilizado para controlar os estados de uso do formulário, como no carregamento do metadata (`METADATA_LOADED`),
na alteração realizada nas abas de navegação (`CHANGE_TAB`) e para capturar o metadata do estado atual do formulário (`selectFormMetadata`).

#### FormSheet

Este componente é utilizado para realizar a renderização total do formulário de acordo com as configurações tratadas pelo `form.slice`,
este componente consiste na construção de um componente funcional do tipo `FormSheetProps` e possui os seguintes atributos:

FormSheetProps| Atributo Tipo| source FormSheetMetadata| store Store| dataElementId string | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### FormMetadata

Realiza o carregamento e tratamento do metadata de cada campo do formulário,
ele controla uma lista de campos do tipo `FormSheetMetadata` que consiste nos seguintes atributos:

FormSheetMetadata| Atributo Tipo| name string| label string| items Array<FieldMetadata | FieldSetMetadata>| requiredFields Array<string>| cleanOnCopyFields Array<string>| defaultValues any | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

FieldSetMetadata| Atributo Tipo| label string| items Array<FieldMetadata> | | | --- | --- | | | | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- |

FieldMetadata| Atributo Tipo| descriptor FieldDescriptor| config IFieldConfig | | | --- | --- | | | | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- |

#### FormItem

É utilizado para realizar a renderização de cada campo do formulário de acordo com o metadata carregado,
este componente consiste na construção de um componente funcional do tipo `FormItemProps` e possui os seguintes atributos:

FormItemProps| Atributo Tipo| source FieldMetadata | FieldSetMetadata| store Store | | | --- | --- | | | | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- |

#### FieldBuilder

Realiza a renderização do campo de acordo com o seu tipo específico.
Podem ser carregados nos seguintes formatos de `UserInterface`:

UserInterface| Tipo Descrição| LONGTEXT Campo com caixa de texto maior| CHECKBOX Campo de marcação| SWITCH Campo de marcação| OPTIONSELECTOR Campo com lista de seleção| SEARCH Campo de busca| FILE Campo de anexo| DATE Campo de data| TIME Campo de tempo| DATETIME Campo de data e hora| DECIMALNUMBER Campo com casas decimais| INTEGERNUMBER Campo com número inteiro | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

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
O ideal para estes casos é utilizar o **document.createElement** e retornar diretamente o elemento HTML.

![Imagem 12: O método renderToString não aceita nenhum código javascript. Para um botão, por exemplo, um onClick não irá funcionar.…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `config` -- Configuração do formulário. `IFormConfig` `undefined`| `dataUnit` -- Unidade de dados. Responsável pelo controle de edição de registros e informações pertinentes aos campos. `DataUnit` `undefined`| `elementFocusSearchField` -- Define uma ancoragem `HTMLElement` `undefined`| `fieldToFocus` `field-to-focus` Determina o campo que deve ficar em evidência. `string` `undefined`| `onlyStaticFields` `only-static-fields` Define se os campos que serão apresentados são todos estáticos. Quando verdadeira, ocorrerá no DataBinder o bind dos campos com o DataUnit. `boolean` `false`| `recordsValidator` -- Define um validador responsável pela integridade dos registros. `IRecordValidator` `undefined`| `useSearchField` `use-search-field` Define se o formulario deve exibir um buscador de coluna com uso do Ctrl+F `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezFormRequestClearFieldToFocus` Emitido quando o campo recebe foco `CustomEvent<void>`| `ezFormSetFields` Emitido quando o campo recebe foco `CustomEvent<IFieldConfig[]>`| `ezReady` Evento disparado quando o formulário está disponível na DOM. `CustomEvent<void>`| `formItemsReady` Responsável por notificar quando ocorrer a renderização de itens do formulário. `CustomEvent<FormItems>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

##### Returns

Type: `Promise<void>`

---

#### `setFieldProp(fieldName: string, propName: string, value: any) => Promise<void>`

Altera/adiciona uma propriedade nos metadados do campo.

##### Returns

Type: `Promise<void>`

---

#### `validate() => Promise<void>`

Realiza validação no conteúdo de todos os campos.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-tabselector](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tabselector)
- [ez-popover](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover)
- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)

#### Graph

```
graph TD;
  ez-form --> ez-tabselector
  ez-form --> ez-popover
  ez-form --> ez-form-view
  ez-form --> ez-search
  ez-tabselector --> ez-icon
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
  style ez-form fill:#f9f,stroke:#333,stroke-width:4px
```

---
