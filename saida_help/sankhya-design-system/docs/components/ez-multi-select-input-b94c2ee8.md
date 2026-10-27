---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input/"
titulo: "Multi Select Input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input/"
trilha: "Docs > Components > Components Doc > Ez Multi Select Input"
---

# Multi Select Input

O **Multi Select Input** é um campo de formulário de múltipla seleção com o mesmo layout visual do [Text Input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input/) (label flutuante, estados de foco/erro/desabilitado e modos regular/slim). Ao ser acionado por clique ou teclado, abre um [Popover Plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/) ancorado ao campo, contendo um [Multi Selection List](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list/). O gatilho exibe a contagem de itens marcados ("N selecionado(s)") e um chevron que alterna entre fechado e aberto.

![Imagem 1: O Multi Select Input é um campo de formulário de múltipla seleção com o mesmo layout visual do Text Input (label…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Lista estática (`options`)

A propriedade `options` recebe um catálogo do tipo `IMultiSelectionOption[]` (com `label`, `value` e `check`) que é renderizado com checkboxes. O gatilho contabiliza os itens com `check: true`.

Importante

Para utilizar a lista estática, defina `useOptions={true}`.

![Imagem 2: Para utilizar a lista estática, defina useOptions={true} .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Carregamento dinâmico (`dataSource`)

Quando os itens vêm do backend, utilize a propriedade `dataSource` (um `IMultiSelectionListDataSource`) em conjunto com `columnName`. O `dataSource` oferece busca em tempo real através do `fetchData` e ordenação através do `sortItems`. A propriedade `isTextSearch` informa se a pesquisa é do tipo texto (`true`) ou numérica (`false`).

Importante

Para a utilização de `dataSource`, defina `useOptions={false}` e informe a propriedade `columnName`.

![Imagem 3: Para a utilização de dataSource , defina useOptions={false} e informe a propriedade columnName .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modos regular e slim

A propriedade `mode` controla a altura do campo: `regular` (42px) ou `slim` (32px).

![Imagem 4: A propriedade mode controla a altura do campo: regular (42px) ou slim (32px).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Estados de interação

O campo acompanha os estados visuais do Text Input: inválido (`errorMessage`/`hasInvalid`), desabilitado (`enabled={false}`) e sem bordas (`noBorder`).

![Imagem 5: O campo acompanha os estados visuais do Text Input: inválido ( errorMessage / hasInvalid ), desabilitado (…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Evento ezChange

Disparado a cada mudança real do conjunto de itens marcados. O payload é o array completo de opções (`IMultiSelectionOption[]`) com o estado de `check` atual.

Observação

As propriedades `options` e `dataSource` não refletem como atributo HTML (arrays e objetos não serializam bem). Atribua-as sempre via propriedade/JSX.

![Imagem 6: As propriedades options e dataSource não refletem como atributo HTML (arrays e objetos não serializam bem). Atribua-as…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### getSelectedOptions e clearSelection

- **`getSelectedOptions()`**: retorna apenas as opções com `check: true`.
- **`clearSelection()`**: limpa todas as seleções (delega ao Multi Selection List) e zera a contagem.

![Imagem 7: clearSelection() : limpa todas as seleções (delega ao Multi Selection List) e zera a contagem.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Integração com formulários

O componente integra-se ao [Form View](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view/) quando o metadata informa `userInterface: "MULTISELECTOR"`. As opções e o modo de carregamento são informados em `props` (`options` + `useOptions`, ou `dataSource` + `columnName`), e o `DataBinder` injeta a seleção armazenada em `value` no carregamento do registro, gravando-a de volta a cada `ezChange`.

```
{
  "name": "DEPARTAMENTOS",
  "userInterface": "MULTISELECTOR",
  "label": "Departamentos",
  "readOnly": false,
  "properties": {
    "options": [
      { "value": "1", "label": "Financeiro", "check": false },
      { "value": "2", "label": "Comercial",  "check": false }
    ],
    "useOptions": true,
    "isTextSearch": false
  }
}
```

Observação

`props.options` também aceita o formato JSON `{"chave":"rótulo"}` (igual ao `OPTIONSELECTOR`), convertido para `IMultiSelectionOption[]` com `check: false`. O `columnName` assume o `name` do campo quando omitido, e `useOptions` é inferido (lista estática quando não há `dataSource`).

## API do componente

### Overview

Campo de formulário de múltipla seleção. Possui o mesmo layout visual do
`ez-text-input` (label flutuante, estados de foco/erro/desabilitado) e, ao ser
acionado, abre um `ez-popover-plus` ancorado ao campo contendo um
`ez-multi-selection-list`. O campo exibe o texto "N selecionado(s)" com a
contagem de itens marcados.

Suporta tanto lista estática (`options`) quanto carregamento dinâmico via
`dataSource`/`columnName`. O valor selecionado é exposto pela prop `value` e
pelo evento `ezChange` (ambos no formato `IMultiSelectionOption[]`), o que
permite a vinculação automática a formulários através do `DataBinder` quando o
metadata informa `userInterface: "MULTISELECTOR"`.

### Properties

| Property Attribute Description Type Default| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `columnName` `column-name` Nome da coluna para o datasource. `string` `undefined`| `dataSource` -- Datasource dinâmico passado para o ez-multi-selection-list. `IMultiSelectionListDataSource` `undefined`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `hasInvalid` `has-invalid` Define se o campo está em estado inválido (bordas vermelhas). `boolean` `false`| `isTextSearch` `is-text-search` Informa se a pesquisa é do tipo texto ou numérico. `boolean` `false`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `'regular'`| `noBorder` `no-border` Se true o campo não terá bordas. `boolean` `false`| `options` -- Opções estáticas passadas para o ez-multi-selection-list. `IMultiSelectionOption[]` `undefined`| `orderSelectedFirst` `order-selected-first` Define se as opções marcadas devem ser reordenadas para o topo da lista. Quando `false` (padrão), a ordem original das opções é preservada — os itens não "pulam" para o topo ao serem selecionados. Defina `true` para manter os selecionados no topo (ordenados). `boolean` `false`| `useOptions` `use-options` Alterna entre lista estática (true) e datasource (false). `boolean` `false`| `value` -- Valor do campo: as opções com o estado de check atual (mesmo formato do payload de `ezChange`). Usado para a vinculação com formulários (read-back do DataBinder). Não reflete como atributo pois arrays não serializam bem em HTML. `IMultiSelectionOption[]` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando a seleção de itens na lista é alterada. O payload é o array completo das opções com seu estado de check. `CustomEvent<IMultiSelectionOption[]>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `clearSelection() => Promise<void>`

Limpa todas as seleções. Delega ao ez-multi-selection-list.

##### Returns

Type: `Promise<void>`

---

#### `getSelectedOptions() => Promise<IMultiSelectionOption[]>`

Retorna as opções com o estado de check atual.

##### Returns

Type: `Promise<IMultiSelectionOption[]>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-tooltip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip)
- [ez-popover-core](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/subcomponent)
- [ez-multi-selection-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list)

#### Graph

```
graph TD;
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
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-search --> ez-text-input
  ez-search --> ez-icon
  ez-search --> ez-popover-plus
  ez-search --> search-list
  ez-popover-plus --> ez-popover-core
  search-list --> ez-card-item
  ez-form-view --> ez-multi-select-input
  style ez-multi-select-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-multi-select-input--height Define a altura do componente.| --ez-multi-select-input--height--slim Define a altura do componente em modo "slim".| --ez-multi-select-input--width Define a largura do componente.| --ez-multi-select-input\_\_min-width Define a largura mínima do componente.| --ez-multi-select-input\_\_max-width Define a largura máxima do componente.| --ez-multi-select-input\_\_icon--width Define a largura reservada para o ícone à direita.| --ez-multi-select-input--font-size Define o tamanho da fonte do componente.| --ez-multi-select-input--font-family Define a família da fonte do componente.| --ez-multi-select-input--font-weight Define o peso da fonte do componente.| --ez-multi-select-input--color Define a cor da fonte do componente.| --ez-multi-select-input--border-radius Define o raio da borda do componente.| --ez-multi-select-input\_\_input--border Define o estilo da borda.| --ez-multi-select-input\_\_input--border-color Define a cor da borda.| --ez-multi-select-input\_\_input--focus--border-color Define a cor da borda quando focado.| --ez-multi-select-input\_\_input--error--border-color Define a cor da borda quando com erro.| --ez-multi-select-input\_\_input--background-color Define a cor de fundo do campo.| --ez-multi-select-input\_\_input--disabled--background-color Define a cor de fundo quando desabilitado.| --ez-multi-select-input\_\_input--disabled--color Define a cor do texto quando desabilitado.| --ez-multi-select-input\_\_label--floating--top Define o posicionamento do label flutuante.| --ez-multi-select-input\_\_label--padding-top Define o espaçamento superior do label.| --ez-multi-select-input\_\_label--padding-left Define o espaçamento esquerdo do label.| --ez-multi-select-input\_\_placeholder--color Define a cor do placeholder.| --ez-multi-select-input\_\_tooltip\_icon--error--color Define a cor do ícone de erro.| --ez-multi-select-input\_\_tooltip-icon---width Define a largura do ícone de erro.| --ez-multi-select-input\_\_tooltip-icon---horizontal-margin Define a margem horizontal do ícone de erro.| --ez-multi-select-input\_\_tooltip-icon---vertical-margin Define a margem vertical do ícone de erro. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
