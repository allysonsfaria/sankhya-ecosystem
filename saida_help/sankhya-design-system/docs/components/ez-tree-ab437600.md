---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tree/"
titulo: "Tree"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tree/"
trilha: "Docs > Components > Components Doc > Ez Tree"
---

# Tree

Uma árvore ou **Tree** é um componente usado para exibir dados hierárquicos de forma organizada.
É possível expandir e contrair informações, auxiliando a navegação entre os registros.

![Imagem 1: Uma árvore ou Tree é um componente usado para exibir dados hierárquicos de forma organizada. É possível expandir e…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Carregamento sob demanda

Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica.
Para isso basta atribuir ao atributo "children" do item, uma função. Veja:

![Imagem 2: Em algumas situações pode ser necessário fazer a carga dos filhos de um item de forma dinâmica. Para isso basta…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades

### Item selecionado

> Propriedade utilizada: **value**

![Imagem 3: Propriedade utilizada: value](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ID selecionado

> Propriedade utilizada: **selectedId**

Também podemos determinar a seleção pelo id

![Imagem 4: Também podemos determinar a seleção pelo id](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Itens selecionáveis

> Propriedade utilizada: **selectable**

Através do atributo selectable é possível determinar se os itens serão ou não selecionáveis.

Quando o selectable for verdadeiro, os itens da lista se comportam de forma diferente. Com
`selectable={true}`, ao clicar no item o mesmo é selecionado e os itens filhos não são abertos
automaticamente, apenas serão abertos quando clicado na seta de expansão. Já quando o selectable
for falso, tanto o ícone quanto o próprio item, quando clicados, expandem os filhos.

![Imagem 5: Quando o selectable for verdadeiro, os itens da lista se comportam de forma diferente. Com selectable={true} , ao…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Personalização de ícones

> Propriedade utilizada: **iconResolver**

Através do atributo iconResolver é possível interferir na criação do ícone de expandir/contrair.

![Imagem 6: Através do atributo iconResolver é possível interferir na criação do ícone de expandir/contrair.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Icones por item

Além disso, o próprio item consegue determinar qual ícone deve ser usado para representar seu estado (aberto/fechado).

![Imagem 7: Além disso, o próprio item consegue determinar qual ícone deve ser usado para representar seu estado (aberto/fechado).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Personalização de tooltip

> Propriedade utilizada: **tooltipResolver**

Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.

![Imagem 8: Através do atributo tooltipResolver é possível personalizar o tooltip dos itens.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Tooltip por item

A exemplo dos ícones, o próprio item consegue determinar seu tooltip.

![Imagem 9: A exemplo dos ícones, o próprio item consegue determinar seu tooltip.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Principais métodos

### applyFilter

O método `applyFilter` permite filtrar os itens da árvore utilizando uma string como parâmetro.
É possível realizar buscas simples ou buscas hierárquicas utilizando o caractere ponto (`.`) para separar os níveis da hierarquia.

Exemplos de uso:

- `applyFilter("Geral")` irá buscar todos os itens que contenham "Geral".
- `applyFilter("Endereço")` irá buscar todos os itens que contenham "Endereço".
- `applyFilter("Geral.Endereço")` irá buscar o caminho hierárquico "Geral" > "Endereço".
- `applyFilter("Geral.Endereço.Entrega.CEP")` irá buscar o caminho completo até "CEP".
- `applyFilter("Fiscal.NF-e/NFS-e/CT-e.Canceladas.Por erro")` irá buscar o caminho até "Por erro" dentro de "Canceladas".

Dessa forma, é possível refinar a busca por caminhos específicos dentro da árvore, facilitando a localização de itens em estruturas complexas.

![Imagem 10: Dessa forma, é possível refinar a busca por caminhos específicos dentro da árvore, facilitando a localização de itens…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### addChild

![Imagem 11: addChild](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### disableItem e enableItem

![Imagem 12: disableItem e enableItem](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### expandAll e collapseAll

![Imagem 13: expandAll e collapseAll](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### openItem

![Imagem 14: openItem](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### selectItem

![Imagem 15: selectItem](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### updateItem

O método `updateItem` permite atualizar as propriedades de um ou mais itens existentes na árvore. Pode receber como parâmetro um item individual ou um array de itens, juntamente com opções de configuração.

**Parâmetros:**

- `item` - Um objeto `ITreeItem` ou array de objetos `ITreeItem` com as novas informações
- `config` (opcional) - Objeto de configuração com as seguintes propriedades:
  - `updatedBySelectedId`: Se `true`, utiliza o `selectedId` atual como ID do item a ser atualizado
  - `forceDefaultValues`: Se `true`, aplica valores padrão para propriedades não definidas (disabled: false, expanded: false)

**Funcionalidades:**

- Atualiza propriedades como título/label, estado disabled/enabled, filhos, etc.
- Suporte para atualização em lote (múltiplos itens)
- Atualização baseada no item selecionado atual
- Aplicação automática de valores padrão quando necessário
- Emite evento `ezChange` se o item atualizado estiver selecionado

![Imagem 16: Emite evento ezChange se o item atualizado estiver selecionado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### removeItem

O método `removeItem` permite remover um item específico da árvore. Pode receber como parâmetro o ID do item que será removido. Caso nenhum ID seja passado, o item atualmente selecionado será removido.

Formas de uso:

- `removeItem()` - Remove o item selecionado
- `removeItem(id)` - Remove o item com o ID especificado

Ao remover um item que possui filhos, todos os seus descendentes também serão removidos da árvore.

![Imagem 17: Ao remover um item que possui filhos, todos os seus descendentes também serão removidos da árvore.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos

### ezChange

![Imagem 18: ezChange](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezOpenItem

![Imagem 19: ezOpenItem](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezRemoveItem

![Imagem 20: ezRemoveItem](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enableHierarchicalFilter` `enable-hierarchical-filter` Define se a árvore deve permitir a filtragem hierárquica. `boolean` `true`| `iconResolver` -- Define uma função que vai resolver o ícone daquele item. Retorna o nome do ícone da lib de icones do DS. `(item: ITreeItem, expanded: boolean, level: number) => string` `defaultIconResolver`| `items` -- Define os itens apresentados na árvore. `ITreeItem[]` `[]`| `selectable` `selectable` Define se os itens da árvore são selecionáveis. `boolean` `true`| `selectedId` `selected-id` Forma alternativa para atribuir o item selecionado por seu ID. `string` `undefined`| `tooltipResolver` -- Define uma função que vai resolver o `tooltip` ou `title` daquele item. `(item: ITreeItem, enabled: boolean, level: number) => string` `undefined`| `value` -- Define o item selecionado na árvore. `ITreeItem` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando um item é selecionado na árvore. `CustomEvent<ITreeItem>`| `ezDbClickItem` Emitido ao dar clique duplo em um item da árvore. `CustomEvent<ITreeItem>`| `ezOpenItem` Emitido quando um item é aberto na árvore. `CustomEvent<ITreeItem>`| `ezRemoveItem` Emitido ao remover um item da árvore. `CustomEvent<string>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addChild(item: ITreeItem, parentId?: string) => Promise<void>`

Adiciona um ou mais itens. Opcionalmente pode-se determinar a qual
item da árvore será anexado o item. Caso não informado parentId,
adiciona no item selecionado.
Observação para carga dinâmica (Lazyload): O parentId deve ser
um item carregado atualmente na árvore.

##### Returns

Type: `Promise<void>`

---

#### `applyFilter(pattern: string) => Promise<void>`

Efetua a seleção de um item.

##### Returns

Type: `Promise<void>`

---

#### `collapseAll() => Promise<void>`

Recolhe todos os itens da árvore.

##### Returns

Type: `Promise<void>`

---

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

#### `expandAll() => Promise<void>`

Expande todos os itens da árvore.

##### Returns

Type: `Promise<void>`

---

#### `getCurrentPath() => Promise<Array<ITreeItem>>`

Obtem um array do caminho de itens da seleção atual.

##### Returns

Type: `Promise<ITreeItem[]>`

Retorna um array do caminho de itens da seleção atual.

---

#### `getItem(id: string) => Promise<ITreeItem>`

Obtem um item pelo id

##### Returns

Type: `Promise<ITreeItem>`

---

#### `getParent(id: string) => Promise<ITreeItem>`

Obtem o item pai a partir de um id

##### Returns

Type: `Promise<ITreeItem>`

---

#### `openItem(id: string) => Promise<void>`

Realiza a abertura de um item, incluindo a hieraquia acima.
Observação para carga dinâmica (Lazyload): O item solicitado já deve
estar carregado na lista. Nos casos onde o item ainda não esteja
carregado o id pode ser uma string no formato "id1>>id2>>id3",
tornando possível a carga a partir de um ponto já carregado.

##### Returns

Type: `Promise<void>`

---

#### `removeItem(id?: string) => Promise<void>`

Remove um item da árvore pelo seu ID.
Se o item removido estiver selecionado, a seleção será limpa.

##### Returns

Type: `Promise<void>`

---

#### `selectItem(id: string) => Promise<void>`

Efetua a seleção de um item.

##### Returns

Type: `Promise<void>`

---

#### `updateItem(item: ITreeItem | ITreeItem[], config?: Partial<UpdateItemConfig>) => Promise<void>`

Atualiza um item

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-guide-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-tree --> ez-icon
  ez-guide-navigator --> ez-tree
  style ez-tree fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-tree--border-radius Define o arredondamento dos retangulos.| --ez-tree--padding-inline-start Define a largura da identação de cada nível.| --ez-tree--margin Define a margem do componente.| --ez-tree--margin-right Define a margem da direita do componente.| --ez-tree--user-select Define se o texto dos itens pode ser selecionado pelo usuário.| --ez-tree--font-family Define a família da fonte.| --ez-tree--font-size Define o tamanho da fonte.| --ez-tree--selected--font-weight Define o peso da fonte.| --ez-tree--font-weight Define o peso da fonte.| --ez-tree--color Define a cor da fonte e do ícone.| --ez-tree--selected--color Define a cor da fonte e do ícone quando selecionado.| --ez-tree--disabled--color Define a cor da fonte e do ícone quando desabilitado.| --ez-tree--font-weight--bold Usado em fontes com peso maior (bold)| --ez-tree\_\_tree-item--height Define a altura de cada item.| --ez-tree\_\_tree-item--padding Define o espaçamento interno do item.| --ez-tree\_\_tree-item--background-color Define a cor de background.| --ez-tree\_\_tree-item--selected--background-color Define a cor de background quando selecionado.| --ez-tree\_\_tree-item--hover--background-color Define a cor de background com o mouse sobre o item.| --ez-tree\_\_tree-item--disabled--background-color Define a cor de background quando deabilitado.| --ez-tree\_\_item-icon-box--height Define a altura do box do ícone.| --ez-tree\_\_item-icon-box--width Define a largura do box do ícone.| --ez-tree\_\_item-icon-box--padding Define o espaçamento interno do ícone.| --ez-tree\_\_badge--icon-color--default Cor de ícone de badge padrão.| --ez-tree\_\_badge--icon-color--error Cor de ícone de badge de erro.| --ez-tree\_\_badge--icon-color--success Cor de ícone de badge sucesso.| --ez-tree\_\_badge--icon-color--warning Cor de ícone de badge de aviso.| --ez-tree\_\_badge--icon-color--disabled Cor de ícone de badge desabilitado. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
