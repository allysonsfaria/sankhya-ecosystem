---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/"
titulo: "Grid"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/"
trilha: "Docs > Components > Components Doc > Ez Grid"
---

# Grid

![Imagem 1: Grid](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

> **Observação**: A grade tem uma altura mínima de 300px

## Navegação via teclado

Esta funcionalide permite aos usuários editar e avançar para células da grade de forma eficiente, além de fornecer uma experiência de navegação simplificada.

Para navegar pela grade, utilize as seguintes teclas:

- **Seta para cima  `↑` :** Move para a célula acima.
- **Seta para baixo  `↓` :** Move para a célula abaixo.
- **Seta para a esquerda  `←` :** Move para a célula à esquerda.
- **Seta para a direita  `→` :** Move para a célula à direita.
- **Tecla  `ENTER` :** Além de ser utilizada na edição é possível usar para navegação também, ao pressionar a tecla a navegação move para a célula abaixo, ou quando a propriedade \*\*useEnterLikeTab \*\* está habilitada, moverá para o lado direito.
- **Tecla  `SHIFT`  +  `ENTER` :** Além de ser utilizada na edição é possível usar para navegação também, ao pressionar a tecla a navegação move para a célula acima, ou quando a propriedade \*\*useEnterLikeTab \*\* está habilitada, moverá para o lado esquerdo.

## Edição de Células

Quando a propriedade **canEdit** está habilitada siga as instruções abaixo:

1. **Seleção da Célula:**

   - Utilize as teclas de navegação para selecionar a célula desejada.
2. **Iniciar Edição:**

   - Pressione a tecla  `ENTER`  para iniciar a edição na célula selecionada.
3. **Cancelar Edição:**

   - A qualquer momento durante a edição, pressione a tecla  `ESC`  para cancelar as alterações e sair do modo de edição.
4. **Salvar Edição:**

   - Após fazer as alterações desejadas, pressione a tecla  `ENTER`  novamente para salvar as alterações e sair do modo de edição.

## Controle de paginação

![Imagem 2: Controle de paginação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Importante

Quando a grid é limitada horizontalmente, a informação de **Itens na página** e **Total de itens** será exibida por um tooltip nos **botões de navegação**.

![Imagem 3: Quando a grid é limitada horizontalmente, a informação de Itens na página e Total de itens será exibida por um tooltip…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Totalizador de colunas

É possível definir colunas que possuam totalizadores, como soma, média, contagem, valor máximo e valor mínimo.

Para isso, nas definições dos **fields** dos metadados do **DataUnit**, deve-se utilizar a propriedade **aggFunc** com o nome da função que será utilizada para calcular o totalizador.

![Imagem 4: Para isso, nas definições dos fields dos metadados do DataUnit , deve-se utilizar a propriedade aggFunc com o nome da…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Dica

As funções de agregação suportadas para totalizadores são:

- **sum**: Soma dos valores.
- **avg**: Média dos valores.
- **count**: Contagem dos valores.
- **max**: Valor máximo.
- **min**: Valor mínimo.

Importante

Caso não queira exibir o totalizador de uma coluna específica, basta que nenhum campo tenha a propriedade **aggFunc** definida.

## Seleção múltipla

![Imagem 5: Seleção múltipla](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Seleção múltipla com paginação

Importante

A barra de informações que indica a **quantidade de registros selecionados** será visível
somente quando a **Seleção múltipla** e a **Paginação** estiverem ativadas.

![Imagem 6: A barra de informações que indica a quantidade de registros selecionados será visível somente quando a Seleção múltipla…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Suprimir filtro de coluna

Dica

Em alguns cenários específicos, desejamos suprimir o filtro de coluna.
Para isso, podemos utilizar a propriedade **suppressFilterColumn**.

![Imagem 7: Em alguns cenários específicos, desejamos suprimir o filtro de coluna. Para isso, podemos utilizar a propriedade…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Validação de registros

> Propriedade utilizada: **recordsValidator**

Define um validador responsável pela integridade dos registros.

Reprodução

Para testar a demonstração abaixo altere alguma informação do primeiro registro da grade.

![Imagem 8: Para testar a demonstração abaixo altere alguma informação do primeiro registro da grade.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Edição na grade

> Propriedade utilizada: **canEdit**

Define se a edição está habilitada na grade.

![Imagem 9: Define se a edição está habilitada na grade.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Configuração

![Imagem 10: Configuração](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Parâmetro ENTER como TAB

> Propriedade utilizada: **useEnterLikeTab**

![Imagem 11: Propriedade utilizada: useEnterLikeTab](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Coluna de status

![Imagem 12: Coluna de status](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

###

A coluna de status também pode ser resolvida por uma função.

![Imagem 13: A coluna de status também pode ser resolvida por uma função.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Tamanho mínimo

Por padrão a grade possui a altura mínima de **300px**, porém existe alguns casos onde o desenvolvedor pode desejar que
a mesma possua uma altura mínima de **0px** para que o componente acompanhe o tamanho do container que o envolve.

Para isso, basta adicionar a classe css `grid_height-0`.

![Imagem 14: Para isso, basta adicionar a classe css grid_height-0 .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Foco automático

Por padrão, a grade possui foco automático, sendo importante para casos onde possui implementações de atalhos de teclado. Porém,
existe alguns casos onde o desenvolvedor pode desejar que a mesma não ocorra, para isso, existe a propriedade booleana `autoFocus` onde pode
ser definido seu comportamento.

## Inserção de item

> Propriedade utilizada: **enableGridInsert**
> Por padrão a inserção na grade vem desabilitada, porém quando ativada da ao usuário a possibilidade de inserir novos registros diretamente na grade.

![Imagem 15: Propriedade utilizada: enableGridInsert Por padrão a inserção na grade vem desabilitada, porém quando ativada da ao…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Inserção continua

> Propriedade utilizada: **enableContinuousInsert**

Essa propriedade somente é utilizada quando a inserção está ativada propriedade `enableGridInsert`.
Por padrão caso a inserção de item esteja ativada a inserção continua também vem ativada, fazendo com que após salvar um registro, seja por envento de um botão salvar ou por alterar a linha selecionada, uma vez o salve sendo bem sucedido automaticamente inicia a inserção de um novo registro. Quando desabilitada ao final da inserção de um registro finaliza a edição.

![Imagem 16: Essa propriedade somente é utilizada quando a inserção está ativada propriedade enableGridInsert . Por padrão caso a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Linhas zebradas

> Propriedade utilizada: **enableRowTableStriped**

Por padrão o zebrado na grade vem habilitado, porém sendo possivel desabilita-lo.

![Imagem 17: Por padrão o zebrado na grade vem habilitado, porém sendo possivel desabilita-lo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Modo simplificado

> Propriedade utilizada: **mode**

O modo simples do componente ez-grid é projetado para oferecer uma experiência de usuário simplificada, mantendo as funcionalidades essenciais. Quando a propriedade `mode` é definida como `"simple"`, o grid opera em modo somente leitura, desabilitando a edição de células e removendo elementos de interface como a barra de ações e o cabeçalho. A paginação não é exibida visualmente, e os checkboxes de seleção de linhas são ocultados. Funcionalidades como ordenação, filtro e ajuste de largura das colunas são mantidas.

![Imagem 18: O modo simples do componente ez-grid é projetado para oferecer uma experiência de usuário simplificada, mantendo as…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setColumnsDef

Cria a definição sem depender dos metadados do DataUnit.

![Imagem 19: Cria a definição sem depender dos metadados do DataUnit.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### addColumnMenuItem

Permite adicionar itens de menu em cada uma das colunas.

![Imagem 20: Permite adicionar itens de menu em cada uma das colunas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### setColumnsState

![Imagem 21: setColumnsState](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### getColumnsState

![Imagem 22: getColumnsState](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### getColumns

![Imagem 23: getColumns](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### getSelection

![Imagem 24: getSelection](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### setData

![Imagem 25: setData](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### addGridCustomRender

Com o método **addGridCustomRender** é possível alterar o elemento que é mostrado na coluna do Grid, podendo criar um elemento customizado dependendo ou não dos valores anteriores.

![Imagem 26: Com o método addGridCustomRender é possível alterar o elemento que é mostrado na coluna do Grid, podendo criar um…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### addCustomEditor

Com o método **addCustomEditor** é possível alterar o elemento que é mostrado na coluna daq Grid em modo de edição e no formulário.

Importante

Ao retornar o elemento como string ou utilizando o método `renderToString` provido pelo `react-dom/server`, não será aplicado **nenhum** código JavaScript, portanto, em casos de inputs ou similares é necessário que o elemento seja criado a partir do `document`, utilizando o método `createElement`.

![Imagem 27: Ao retornar o elemento como string ou utilizando o método renderToString provido pelo react-dom/server , não será…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### ezSelectionChange

![Imagem 28: ezSelectionChange](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezDoubleClick

![Imagem 29: ezDoubleClick](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezColumnStateChange

![Imagem 30: ezColumnStateChange](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Formatador personalizado

É possível adicionar formatadores personalizados (CustomValueFormatter) através do método **addCustomValueFormatter** do componente. Este formatador deve seguir a interface ICustomFormatter e, através do método **format**, retornar um valor formatado a ser apresentado na grade.

O método **removeCustomValueFormatter** remove um formatador personalizado previamente adicionado.

## API do componente

### Properties

| Property Attribute Description Type Default| `autoFocus` `auto-focus` Define se a grid será focada ao ser carregada. `boolean` `true`| `canEdit` `can-edit` Define se a edição está habilitada na grid. `boolean` `true`| `columnfilterDataSource` -- Define um `IMultiSelectionListDataSource` responsável por alimentar o filtro de colunas. `IMultiSelectionListDataSource` `undefined`| `compact` `compact` Define se a grade deve ser exibida em modo compacto `boolean` `false`| `config` -- Configuração de exibição da grade. `IGridConfig` `undefined`| `dataUnit` -- Unidade de dados. Responsável pelo controle de edição de registros e informações pertinentes aos campos. `DataUnit` `undefined`| `enableContinuousInsert` `enable-continuous-insert` Ativa/desativa a inserção continua na grade Só funciona quando a prop enableGridInsert está ativa `boolean` `true`| `enableGridInsert` `enable-grid-insert` Ativa inserção de registros no modo grade. `boolean` `false`| `enableLockManagerLoadingComp` `enable-lock-manager-loading-comp` Define se o componente deve usar o LockManager para controle de carregamento da aplicação `boolean` `false`| `enableLockManagerTaskbarClick` `enable-lock-manager-taskbar-click` Ativa inserção de registros no modo grade pela Taskbar. `boolean` `true`| `enableRowTableStriped` `enable-row-table-striped` Ativa modo de linhas com cores alternadas. `boolean` `true`| `mode` `mode` Define o modo de uso da grade `"complete" | "simple"` `"complete"`| `multipleSelection` `multiple-selection` Habilita a seleção de várias linhas. `boolean` `undefined`| `outlineMode` `outline-mode` Altera visualmente as sombras e bordas do componente Quando false, aplica o padrão de sombras ao componente (Utilizar quando for o elemento principal do layout) Quando true, aplica o padrão de outline ao componente (Utilizar quando estiver contido em outro elemento como um painel ou pop-up) `boolean` `false`| `paginationCounterMode` `pagination-counter-mode` Define se a grid será focada ao ser carregada. `"auto" | "hidden" | "show"` `'auto'`| `recordsValidator` -- Define um validador responsável pela integridade dos registros. `IRecordValidator` `undefined`| `selectionToastConfig` -- Configuração da seleção de grade no toast. `ISelectionToastConfig` `undefined`| `serverUrl` `server-url` Endereço do servidor para obtenção dos dados. `string` `undefined`| `statusResolver` -- Define um `IStatusResolver` responsável pelo estado da coluna de status. `((data: object) => string) | IStatusResolver` `undefined`| `suppressCheckboxColumn` `suppress-checkbox-column` Informa se a coluna de chechbox deve ser suprimida `boolean` `false`| `suppressFilterColumn` `suppress-filter-column` Informa se a grade deve suprimir o filtro de coluna. `boolean` `false`| `suppressHorizontalScroll` `suppress-horizontal-scroll` Define se a grade deve suprimir o scroll horizontal. `boolean` `false`| `useEnterLikeTab` `use-enter-like-tab` Quando verdadeiro, o ENTER fará a navegação como se fosse a tecla TAB na grade. `boolean` `false`| `useSearchColumn` `use-search-column` Define se a grade deve exibir um buscador de coluna com uso do Ctrl+F `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `componentReady` Emitido quando o componente estiver completamente carregado. `CustomEvent<void>`| `configChange` Emitido quando acontece a alteração de configuração do grade. `CustomEvent<IGridConfig>`| `ezColumnFilterChanged` Emitido quando acontece a alteração de filtro de colunas. `CustomEvent<Filter[]>`| `ezColumnStateChange` Emitido quando acontece a alteração de estado das colunas do grid: Ordenação, largura, etc. `CustomEvent<EzGridColumStateEvent>`| `ezDoubleClick` Emitido com o duplo clique de uma linha `CustomEvent<any>`| `ezPageChangedChanged` Emitido a página atual é alterada. `CustomEvent<void>`| `ezSelectionChange` Emitido quando acontece a alteração de seleção de linhas. `CustomEvent<ISelection>` | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addColumnMenuItem(label: string, name: string, action: Function, icon: HTMLElement | string) => Promise<void>`

Adiciona item de menu nas colunas.

##### Returns

Type: `Promise<void>`

---

#### `addCustomEditor(fieldName: string, customEditor: ICustomEditor, detailContext?: string) => Promise<void>`

Registra um editor customizado para campos da grade e formulário.

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

#### `checkStopEditOutsideClick(event: MouseEvent) => Promise<void>`

##### Returns

Type: `Promise<void>`

---

#### `filterColumns(search: string) => Promise<Array<EzGridColumn>>`

Usa um argumento para filtrar as colunas po label

##### Returns

Type: `Promise<EzGridColumn[]>`

---

#### `getAppliedColumnFilters() => Promise<Array<Filter>>`

Retorna os filtros aplicados.

##### Returns

Type: `Promise<Filter[]>`

---

#### `getColumns() => Promise<Array<EzGridColumn>>`

Obtém a lista de definição de colunas.

##### Returns

Type: `Promise<EzGridColumn[]>`

---

#### `getColumnsState() => Promise<Array<EzGridColumn>>`

Obtém o estado atual das colunas.

##### Returns

Type: `Promise<EzGridColumn[]>`

---

#### `getCustomValueFormatter(columnName: string) => Promise<ICustomFormatter | undefined>`

Retorna o formatador customizado da coluna caso exista.

##### Returns

Type: `Promise<ICustomFormatter>`

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

#### `refreshColumnFilterDataSource() => Promise<void>`

##### Returns

Type: `Promise<void>`

---

#### `refreshSelectedRows() => Promise<void>`

Atualiza linhas da grade.

##### Returns

Type: `Promise<void>`

---

#### `removeCustomValueFormatter(columnName: string) => Promise<void>`

Remove o formatador de valores de uma coluna da grid.

##### Returns

Type: `Promise<void>`

---

#### `setColumnsDef(cols: Array<EzGridColumn>) => Promise<void>`

Aplica a definição de colunas.

##### Returns

Type: `Promise<void>`

---

#### `setColumnsState(state: Array<EzGridColumnConfig>) => Promise<void>`

Aplica o estado das colunas.

##### Returns

Type: `Promise<void>`

---

#### `setData(data: Array<any>) => Promise<void>`

Insere os registros no ez-grid.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Atribui o foco para a grade.

##### Returns

Type: `Promise<void>`

---

#### `stopEdit() => Promise<void>`

Para a edição da grade.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-grid-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid-view)

#### Depends on

- [ez-popover](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [filter-column](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/subcomponents)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)

#### Graph

```
graph TD;
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
  ez-grid-view --> ez-grid
  style ez-grid fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-grid\_\_header--background-color Define a cor de fundo do header do componente.| --ez-grid\_\_selection-counter--z-index Define o z-index do componente selection counter.| --ez-grid\_\_container--shadow Define o sombreamento usado como borda.| --ez-grid--min-height Define altura mínima da grid| --ez-grid\_\_container--shadow--outline Define o outline usado como borda.| --ez-grid\_\_header--shadow Define a sombra do header.| --ez-grid\_\_header--shadow--outline Define o outline usado como borda do header.| --ez-grid\_\_header--outline Define o outline do header.| --ez-grid\_\_header--border Define a borda do header. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
