---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid-view/"
titulo: "Grid View"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid-view/"
trilha: "Docs > Components > Components Doc > Ez Grid View"
---

# Grid View

O **EzGridView** é um componente que permite a **visualização** de dados em modo de grade de forma simples e dinâmica.

Diferente do **[EzGrid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)**, ele oferece uma abordagem de implementação mais direta e prática,
eliminando a necessidade do desenvolvedor configurar `dataLoaders`, lidar com **filtros**, **paginação**,
entre outras configurações que apesar de poderosas, aumentam consideravelmente a complexidade de sua implementação.

Para usar o **EzGridView**, basta informar os **metadados das colunas** e o array com os registros, que o componente cuidará do resto.

Importante

É importante ressaltar que o **EzGridView** é um meio apenas de **visualização** dos dados em modo de grade.
Ou seja, ele não possui funcionalidades de edição ou inserção de registros, como no **[EzGrid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)**.

![Imagem 1: É importante ressaltar que o EzGridView é um meio apenas de visualização dos dados em modo de grade. Ou seja, ele não…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades

O **EzGridView** possui algumas propriedades que permitem personalizar seu comportamento e aparência.

### Tamanho das colunas

É possível configurar as colunas do **EzGridView** através da propriedade `columnsConfig`.
Com isso, é possível definir a largura inicial, alinhamento e outras características de cada coluna.

informação

A Propriedade `columnsConfig` deve ser um array de objetos da interface `ColumnConfig`.

```
interface ColumnConfig {
  /**
   * ID da coluna. Em cada linha do array de dados, esse ID deve coincidir com
   * o nome do atributo que a coluna representa.
   */
  name: string,

  /**
   * Largura padrão da coluna em pixels absolutos.
   */
  width: number,
}
```

![Imagem 2: A Propriedade columnsConfig deve ser um array de objetos da interface ColumnConfig . interface ColumnConfig { /** * ID…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Suprimir coluna de checkbox

Por padrão, o **EzGridView** exibe uma coluna de checkbox para seleção de linhas.
Para que a mesma não seja exibida, basta definir a propriedade `suppressCheckboxColumn` como `true`.

![Imagem 3: Por padrão, o EzGridView exibe uma coluna de checkbox para seleção de linhas. Para que a mesma não seja exibida, basta…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Definir tamanho da página

A propriedade `pageSize` permite definir o número de registros exibidos por página.

> Por padrão, o valor do `pageSize` é `150`.

![Imagem 4: Por padrão, o valor do pageSize é 150 .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Seleção de múltiplos registros

Para habilitar a seleção de múltiplos registros, basta definir a propriedade `multipleSelection` como `true`.

![Imagem 5: Para habilitar a seleção de múltiplos registros, basta definir a propriedade multipleSelection como true .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo de exibição do contador da paginação

A propriedade `paginationCounterMode` permite definir o modo de exibição do contador da paginação.

Informação

Opções disponíveis: `show`, `hidden` e `auto`.

Valor padrão: `auto`.

![Imagem 6: Valor padrão: auto .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Suprimindo filtro de colunas

Para suprimir o filtro de colunas, basta definir a propriedade `suppressFilterColumn` como `true`.
Dessa forma, ao clicar no menu de contexto de uma coluna, a opção de filtro não será exibida.

![Imagem 7: Para suprimir o filtro de colunas, basta definir a propriedade suppressFilterColumn como true . Dessa forma, ao clicar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo outilne

Altera visualmente as sombras e bordas do componente. Quando `false`, aplica o padrão de sombras ao componente
(Utilizar quando for o elemento principal do layout).
Quando `true`, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up).

![Imagem 8: Altera visualmente as sombras e bordas do componente. Quando false , aplica o padrão de sombras ao componente (Utilizar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Linhas listradas

A propriedade `enableRowTableStriped` permite definir se as linhas do grid serão exibidas com um estilo listrado.

![Imagem 9: A propriedade enableRowTableStriped permite definir se as linhas do grid serão exibidas com um estilo listrado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Formato das datas

É possível definir o formato das datas exibidas no grid através da propriedade `recordDateFormat`.

Dica

A Propriedade `recordDateFormat` aceita as opções `DD_MM_YYYY` e `ISO` ou o enum `RECORD_DATE_FORMAT` da biblioteca `@sankhyalabs/core`.

![Imagem 10: A Propriedade recordDateFormat aceita as opções DD_MM_YYYY e ISO ou o enum RECORD_DATE_FORMAT da biblioteca…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

Uma série de métodos são disponibilizados pelo **EzGridView** para manipulação e interação com o componente.

### Obter DataUnit

O método `getDataUnit` retorna o `DataUnit` associado ao componente, que contém os dados exibidos no grid.

![Imagem 11: O método getDataUnit retorna o DataUnit associado ao componente, que contém os dados exibidos no grid.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Recarregar os registros

Em alguns casos é necessário recarregar os registros exibidos na grade para que seja visível alterações realizadas,
como por exemplo a adição de um formatador personalizado.

Para isso, o método `refresh` deve ser utilizado.

![Imagem 12: Para isso, o método refresh deve ser utilizado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Obter registros selecionados

O método `getSelectedRecords` retorna um array com os registros selecionados na grade.

![Imagem 13: O método getSelectedRecords retorna um array com os registros selecionados na grade.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adicionar um formatador de coluna customizado

O método `addCustomValueFormatter` permite adicionar um formatador customizado para uma coluna específica.
Para isso, é necessário informar o nome da coluna e a função formatadora que será aplicada aos valores dessa coluna.

Dica

A função formatadora deverá implementar a interface `ICustomFormatter`, que define o método `format` e o método `refreshSelectedRows`.:

```
interface ICustomFormatter {
    format: (currentValue: any, column: EzGridColumn, recordId: string) => any;
    refreshSelectedRows: () => void;
}
```

Essa interface está disponível em `@sankhyalabs/ezui/dist/types/components/ez-grid/interfaces`

Atenção

O método `addCustomValueFormatter` por si só não recarrega os registros da grade, sendo necessário chamar o método `refresh`
para que as alterações possam ser visualizadas.

![Imagem 14: O método addCustomValueFormatter por si só não recarrega os registros da grade, sendo necessário chamar o método…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remover um formatador de coluna customizado

O método `removeCustomValueFormatter` permite remover um formatador customizado previamente adicionado a uma coluna.

Atenção

Assim como o `addCustomValueFormatter`, o método `removeCustomValueFormatter` não recarrega os registros da grade automaticamente.
Sendo asism, é necessário chamar o método `refresh` para que as alterações sejam visíveis.

![Imagem 15: Assim como o addCustomValueFormatter , o método removeCustomValueFormatter não recarrega os registros da grade…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adicionando um renderizador customizado

Com o método `addGridCustomRender` é possível alterar o elemento que é mostrado na coluna da grade,
podendo criar um elemento customizado dependendo ou não dos valores anteriores.

![Imagem 16: Com o método addGridCustomRender é possível alterar o elemento que é mostrado na coluna da grade, podendo criar um…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adicionando item no menu de coluna

Utilize o método `addColumnMenuItem` para adicionar itens de menu em cada uma das colunas.

![Imagem 17: Utilize o método addColumnMenuItem para adicionar itens de menu em cada uma das colunas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Localizar coluna

O método `locateColumn` permite localizar uma coluna, tornando-a visível, mesmo que haja scroll na grade.

![Imagem 18: O método locateColumn permite localizar uma coluna, tornando-a visível, mesmo que haja scroll na grade.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

Seguem abaixo alguns exemplos de eventos que permitem interagir com o componente.

Dica

O **EzGridView** utiliza o **[EzGrid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)**, portanto, todos os eventos disponíveis no **EzGrid** também estão
disponíveis no **EzGridView**.

### Evento de seleção

O evento `ezSelectionChange` é disparado sempre que a seleção de registros na grade é alterada.

![Imagem 19: O evento ezSelectionChange é disparado sempre que a seleção de registros na grade é alterada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento de duplo clique em uma linha

O evento `ezDoubleClick` é disparado quando uma linha da grade é clicada duas vezes.

![Imagem 20: O evento ezDoubleClick é disparado quando uma linha da grade é clicada duas vezes.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento de mudança de estado das colunas

O evento `ezColumnStateChange` é disparado quando o estado de uma coluna é alterado, como por exemplo, quando uma coluna é ordenada ou filtrada.

![Imagem 21: O evento ezColumnStateChange é disparado quando o estado de uma coluna é alterado, como por exemplo, quando uma coluna…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Slots para elementos personalizados

O **EzGridView** permite a utilização de slots para adicionar elementos personalizados ao componente.

### Slot de rodapé

![Imagem 22: Slot de rodapé](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Slot de cabeçalho

Utilize o slot `leftButtons` para adicionar elementos personalizados ao cabeçalho do grade.

Dica

Pode ser utilizado para adicionar uma barra de ferramentas contendo botões de ação, como exportação de dados,
filtros avançados, entre outros.

![Imagem 23: Pode ser utilizado para adicionar uma barra de ferramentas contendo botões de ação, como exportação de dados, filtros…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `autoFocus` `auto-focus` Define se a grid será focada ao ser carregada. `boolean` `true`| `columnsConfig` -- Configuração de exibição da grade. `ColumnConfig[]` `undefined`| `compact` `compact` Define se a grade deve ser exibida em modo compacto `boolean` `false`| `enableRowTableStriped` `enable-row-table-striped` Ativa modo de linhas com cores alternadas. `boolean` `true`| `metadata` -- Metadados que definem a estrutura da grade. `UnitMetadata` `undefined`| `multipleSelection` `multiple-selection` Habilita a seleção de várias linhas. `boolean` `false`| `outlineMode` `outline-mode` Altera visualmente as sombras e bordas do componente Quando false, aplica o padrão de sombras ao componente (Utilizar quando for o elemento principal do layout) Quando true, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up) `boolean` `false`| `pageSize` `page-size` Quantidade de registros por página. `number` `150`| `paginationCounterMode` `pagination-counter-mode` Define a forma como a paginação irá se comportar. `"auto" | "hidden" | "show"` `'auto'`| `recordDateFormat` `record-date-format` Formato dos campos data dos registros. `RECORD_DATE_FORMAT.DD_MM_YYYY | RECORD_DATE_FORMAT.ISO` `RECORD_DATE_FORMAT.DD_MM_YYYY`| `records` -- Registros a serem exibidos na grade. `Record[]` `undefined`| `suppressCheckboxColumn` `suppress-checkbox-column` Informa se a coluna de chechbox deve ser suprimida `boolean` `false`| `suppressFilterColumn` `suppress-filter-column` Informa se a grade deve suprimir o filtro de coluna. `boolean` `false`| `suppressHorizontalScroll` `suppress-horizontal-scroll` Define se a grade deve suprimir o scroll horizontal. `boolean` `false`| `useSearchColumn` `use-search-column` Define se a grade deve exibir um buscador de coluna com uso do Ctrl+F `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addColumnMenuItem(label: string, name: string, action: Function, icon: HTMLElement | string) => Promise<void>`

Adiciona item de menu nas colunas.

##### Returns

Type: `Promise<void>`

---

#### `addCustomValueFormatter(columnName: string, customFormatter: ICustomFormatter) => Promise<void>`

Registra um formatador de valores para uma coluna da grid.

##### Returns

Type: `Promise<void>`

---

#### `addGridCustomRender(fieldName: string, customRender: ICustomRender, detailContext?: string) => Promise<void>`

Registra um render customizado para colunas da grid.

##### Returns

Type: `Promise<void>`

---

#### `filterColumns(search: string) => Promise<Array<EzGridColumn>>`

Usa um argumento para filtrar as colunas por label

##### Returns

Type: `Promise<EzGridColumn[]>`

---

#### `getDataUnit() => Promise<DataUnit>`

Obtém o DataUnit da grade.

##### Returns

Type: `Promise<DataUnit>`

---

#### `getSelection() => Promise<Array<any>>`

Obtém as linhas selecionadas.

##### Returns

Type: `Promise<any[]>`

---

#### `locateColumn(columnName: string) => Promise<void>`

Localiza determinada coluna tornando-a visível.

##### Returns

Type: `Promise<void>`

---

#### `quickFilter(term: string) => Promise<void>`

Aplica um filtro rápido.

##### Returns

Type: `Promise<void>`

---

#### `refresh() => Promise<void>`

Recarrega os registros da grade.

##### Returns

Type: `Promise<void>`

---

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove o formatador de valores de uma coluna da grid.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Atribui o foco para a grade.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-grid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)

#### Graph

```
graph TD;
  ez-grid-view --> ez-grid
  ez-grid --> ez-popover
  ez-grid --> ez-icon
  ez-grid --> ez-button
  ez-grid --> filter-column
  ez-grid --> ez-search
  ez-button --> ez-icon
  filter-column --> ez-popover-plus
  filter-column --> ez-button
  filter-column --> ez-multi-selection-list
  ez-popover-plus --> ez-popover-core
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
  search-list --> ez-card-item
  style ez-grid-view fill:#f9f,stroke:#333,stroke-width:4px
```

---
