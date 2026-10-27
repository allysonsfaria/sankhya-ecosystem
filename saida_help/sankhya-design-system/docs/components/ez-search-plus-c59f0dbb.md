---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus/"
titulo: "Search Plus"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus/"
trilha: "Docs > Components > Components Doc > Ez Search Plus"
---

# Search Plus

O Search input permite ao usuário buscar um conteúdo por meio de uma palavra chave. A pesquisa oferece aos usuários uma maneira de explorar um conteúdo ou informação utilizando palavras chaves, podendo ser utilizada como o principal meio de descoberta de conteúdo ou como um filtro para ajudar o usuário a encontrar o conteúdo desejado.

![Imagem 1: O Search input permite ao usuário buscar um conteúdo por meio de uma palavra chave. A pesquisa oferece aos usuários uma…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades

### value

A propriedade `value` define o valor atual do campo de busca.
Pode ser uma string simples ou um objeto que contém value e label.
Quando é passado apenas o código, a label será buscada a partir
do `optionLoader`.

- Tipo: `string | IOption`.
- Valor inicial: `undefined`.

![Imagem 2: Valor inicial: undefined .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### enabled

A propriedade `enabled` controla se o campo de busca está habilitado ou não.
Quando habilitado, o usuário pode interagir com o campo de busca.
Caso contrário, o campo estará desabilitado e não permitirá interações.

- Tipo: `boolean`.
- Valor inicial: `true`.

![Imagem 3: Valor inicial: true .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### disableCodeInput

A propriedade `disableCodeInput` desabilita a entrada de código no campo de busca.
Quando habilitado, o usuário não poderá digitar ou selecionar um código.

- Tipo: `boolean`.
- Valor inicial: `false`.

![Imagem 4: Valor inicial: false .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### disableDescriptionInput

A propriedade `disableDescriptionInput` desabilita a entrada de descrição no campo de busca.
Quando habilitado, o usuário não poderá digitar ou selecionar uma descrição.

- Tipo: `boolean`.
- Valor inicial: `false`.

![Imagem 5: Valor inicial: false .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### label

A propriedade `label` define o rótulo exibido acima do campo de busca.
Este rótulo ajuda a identificar o propósito do campo para o usuário.

- Tipo: `string`.
- Valor inicial: `""` (string vazia).

![Imagem 6: Valor inicial: "" (string vazia).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### codeLabel

A propriedade `codeLabel` define o rótulo exibido no código no campo de busca.
Este rótulo ajuda a identificar o código exibido para o usuário.

- Tipo: `string`.
- Valor inicial: `"Cód."`.

![Imagem 7: Valor inicial: "Cód." .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### errorMessage

A propriedade `errorMessage` define a mensagem de erro exibida no ícone a direita do campo de busca.
Esta mensagem é exibida quando o campo de busca está em um estado de erro.

- Tipo: `string`.
- Valor inicial: `""` (string vazia).

![Imagem 8: Valor inicial: "" (string vazia).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### canShowError

A propriedade `canShowError` controla se a mensagem de erro deve ser exibida.
Quando habilitado, a mensagem de erro será exibida no ícone a direita do componente.

- Tipo: `boolean`.
- Valor inicial: `true`.

![Imagem 9: Valor inicial: true .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### optionLoader

A propriedade `optionLoader` define a função responsável por carregar as opções disponíveis no campo de busca.
Esta função pode ser utilizada para carregar opções dinamicamente com base em uma entrada do usuário.

- Tipo: `OptionLoaderFunction`.
- Valor inicial: `undefined`.

#### Tipos relacionados:

- `ISearchArgument`: Interface que define os argumentos passados para a função `optionLoader`.

  ```
  export interface ISearchArgument {
    mode: SearchMode;
    argument: string;
  }
  ```

  - `mode`: Define o modo de busca (por exemplo, busca por código ou por descrição).
  - `argument`: O argumento de busca fornecido pelo usuário.
- `OptionLoaderFunction`: Tipo da função `optionLoader`.

  ```
  export type OptionLoaderFunction = (
    argument: ISearchArgument,
    ctxProperties?: any
  ) =>
    Promise<Array<IOption | ISearchOption> | IOption | ISearchOption> |
    Array<ISearchOption | IOption> |
    IOption |
    ISearchOption;
  ```

  - A função recebe um argumento do tipo `ISearchArgument` e um objeto opcional `ctxProperties`.
  - Retorna uma promessa que resolve para um array de opções (`IOption` ou `ISearchOption`), uma única
    opção (`IOption` ou `ISearchOption`), ou diretamente um array de opções ou uma única opção.

Atenção

Quando é feita uma busca pelo campo código, o componente irá selecionar o primeiro item retornado pela função
`optionLoader`.

![Imagem 10: Quando é feita uma busca pelo campo código, o componente irá selecionar o primeiro item retornado pela função…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### showOptionValue

A propriedade `showOptionValue` controla se o valor das opções deve ser exibido junto com a label no campo de busca.
Quando desabilitado, apenas será exibido a label nas opções.

- Tipo: `boolean`.
- Valor inicial: `true`.

![Imagem 11: Valor inicial: true .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### mode

A propriedade `mode` define o modo de exibição do campo de busca.
Pode ser utilizada para alternar entre diferentes estilos de exibição, como regular ou slim.

- Tipo: `string`.
- Valores possíveis: `"regular" | "slim"`.
- Valor inicial: `"regular"`.

![Imagem 12: Valor inicial: "regular" .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ensureClearButtonVisible

A propriedade `ensureClearButtonVisible` garante que o botão de limpar pesquisa esteja visível.
Quando habilitado, o botão de limpar pesquisa será exibido mesmo quando o campo de busca estiver vazio.

- Tipo: `boolean`.
- Valor inicial: `false`.

![Imagem 13: Valor inicial: false .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### hideDescriptionInput

A propriedade `hideDescriptionInput` oculta a entrada de descrição no campo de busca.
Quando habilitado, a entrada de descrição não será exibida.

- Tipo: `boolean`.
- Valor inicial: `false`.

![Imagem 14: Valor inicial: false .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### stopPropagateEnterKeyEvent

A propriedade `stopPropagateEnterKeyEvent` controla se o evento de pressionar a tecla Enter deve ser propagado.
Quando habilitado, o evento de pressionar a tecla Enter não será propagado para outros elementos.

- Tipo: `boolean`.
- Valor inicial: `false`.

### autoFocus

A propriedade `autoFocus` define se o campo de busca deve receber foco automaticamente ao ser renderizado.
Quando habilitado, o campo de busca receberá foco automaticamente.

- Tipo: `boolean`.
- Valor inicial: `false`.

### contextProperties

A propriedade `contextProperties` permite passar propriedades de contexto adicionais para a função `optionLoader`.
Estas propriedades podem ser utilizadas para personalizar o comportamento da função `optionLoader`.

- Tipo: `any`.
- Valor inicial: `undefined`.

## Métodos

### setFocus

O método `setFocus` aplica o foco no campo de busca.

- Parâmetros: Nenhum.
- Retorno: `void`.

![Imagem 15: Retorno: void .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### setBlur

O método `setBlur` remove o foco do campo de busca.

- Parâmetros: Nenhum.
- Retorno: `void`.

![Imagem 16: Retorno: void .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### isInvalid

O método `isInvalid` retorna se o conteúdo do campo de busca é inválido.

- Parâmetros: Nenhum.
- Retorno: `boolean`.

![Imagem 17: Retorno: boolean .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### getValueAsync

O método `getValueAsync` retorna uma promise do valor atual do campo de busca,
aguardando o carregamente dos dados, caso esteja em progresso.

- Parâmetros: Nenhum.
- Retorno: `Promise<IOption>`.

![Imagem 18: Retorno: Promise<IOption> .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### clearValue

O método `clearValue` limpa o valor atual do campo de busca.

- Parâmetros: Nenhum.
- Retorno: `void`.

![Imagem 19: Retorno: void .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### ezChange

O evento `ezChange` é disparado quando o estado do componente é alterado.

- Parâmetros: `CustomEvent`.
- Retorno: `void`.

![Imagem 20: Retorno: void .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `codLabel` `cod-label` Texto a ser apresentado no input de código. `string` `undefined`| `contextProperties` `context-properties` Propriedades de contexto da aplicação. `any` `undefined`| `disableCodeInput` `disable-code-input` Se true o campo de código ficara desabilitado. `boolean` `false`| `disableDescriptionInput` `disable-description-input` Se true o campo de de apresentação ficara desabilitado. `boolean` `false`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `ensureClearButtonVisible` `ensure-clear-button-visible` Garante que o botão de limpar pesquisa está sempre visível `boolean` `false`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `hideDescriptionInput` `hide-description-input` Se true o campo de de apresentação não será exibido. `boolean` `false`| `hideErrorOnFocusOut` `hide-error-on-focus-out` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `true`| `ignoreLimitCharsToSearch` `ignore-limit-chars-to-search` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `false`| `isTextSearch` `is-text-search` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `false`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `listOptionsPosition` -- Propriedade depreciada na nova versão do componente de pesquisa. `IEzCheckBoxListPosition` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `optionLoader` -- Carrega as opções dinamicamente. `(argument: ISearchArgument, ctxProperties?: any) => ISearchOption | IOption | (ISearchOption | IOption)[] | Promise<ISearchOption | IOption | (ISearchOption | IOption)[]>` `undefined`| `showOptionValue` `show-option-value` Se false cada opção na lista deve exibir somente o `label`. `boolean` `true`| `showSelectedValue` `show-selected-value` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `true`| `stopPropagateEnterKeyEvent` `stop-propagate-enter-key-event` Se true, interrompe a propagação do evento de KeyDown da tecla enter `boolean` `false`| `suppressEmptyOption` `suppress-empty-option` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `false`| `suppressPreLoad` `suppress-pre-load` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `true`| `suppressSearch` `suppress-search` Propriedade depreciada na nova versão do componente de pesquisa. `boolean` `false`| `value` `value` Define o valor do campo. `IOption | string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<IOption>`| `ezEmptySearch` Emitido quando a pesquisa retorna um resultado inválido. `CustomEvent<string>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `clearValue() => Promise<void>`

Limpa o valor do campo de pesquisa

##### Returns

Type: `Promise<void>`

---

#### `getValueAsync() => Promise<IOption>`

Obtém o valor do componente só após a compo de apresentação
ter sido resolvido pelo option loader quando necessário

##### Returns

Type: `Promise<IOption>`

---

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

---

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

---

#### `setFocus(options?: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-popover-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus)
- [ez-search-result-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus/subcomponent/ez-search-result-list)

#### Graph

```
graph TD;
  ez-search-plus --> ez-icon
  ez-search-plus --> ez-text-input
  ez-search-plus --> ez-popover-plus
  ez-search-plus --> ez-search-result-list
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-popover-plus --> ez-popover-core
  ez-search-result-list --> ez-card-item
  ez-search-result-list --> ez-skeleton
  ez-form-view --> ez-search-plus
  style ez-search-plus fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-search--height Define altura do input.| --ez-search--width Define largura do input.| --ez-search\_\_icon--width Define largura do slot do ícone do input.| --ez-search--border-radius Define o raio da borda do input.| --ez-search--border-radius-small Define o raio da borda do input quando pequeno.| --ez-search--font-size Define o tamanho da fonte dentro do input.| --ez-search--font-family Define a família da fonte dentro do input.| --ez-search--font-weight--large Define o peso da fonte dentro do input quando pesada.| --ez-search--font-weight--medium Define o peso da fonte dentro do input quando média.| --ez-search--background-color--xlight Define a cor de fundo da lista de opções.| --ez-search--background-medium Define a cor de fundo dos itens da lista de opções.| --ez-search--line-height Define a altura da linha do texto dentro do input.| --ez-search\_\_input--background-color Define a cor de fundo do input.| --ez-search\_\_input--border Define o estilo da borda do input.| --ez-search\_\_input--border-color Define a cor da borda do input.| --ez-search\_\_input--focus--border-color Define a cor da borda do input quando focado.| --ez-search\_\_input--disabled--background-color Define a cor de fundo do input quando desabilitado.| --ez-search\_\_input--disabled--color Define a cor do texto dentro do input quando desabilitado.| --ez-search\_\_input--error--border-color Define a cor da borda do input quando com erro.| --ez-search\_\_btn--color Define a cor do botão de pesquisa do componente.| --ez-search\_\_btn-disabled--color Define a cor do botão de pesquisa do componente quando desabilitado.| --ez-search\_\_btn-hover--color Define a cor do botão de pesquisa do componente quando o mouse está sobre ele.| --ez-search\_\_label--color Define a cor do label.| --ez-search\_\_list-title--primary Define a cor do texto da lista de opções.| --ez-search\_\_list-text--primary Define a cor do texto do value da lista de opções.| --ez-search\_\_list-height Define a altura do box da lista de opções.| --ez-search\_\_list-min-width Define a largura mínima da lista de opções.| --ez-search--space--medium Define um espaçamento mediano entre elementos do componente.| --ez-search--space--small Define um espaçamento pequeno entre elementos do componente.| --ez-search\_\_scrollbar--color-default Define a cor da barra de rolagem do componente.| --ez-search\_\_scrollbar--color-background Define a cor de fundo da barra de rolagem do componente.| --ez-search\_\_scrollbar--color-hover Define a cor do hover na barra de rolagem do componente.| --ez-search\_\_scrollbar--color-clicked Define a cor do active na barra de rolagem do componente.| --ez-search\_\_scrollbar--border-radius Define o raio da borda da barra de rolagem do componente.| --ez-search\_\_scrollbar--width Define a largura da barra de rolagem do componente. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
