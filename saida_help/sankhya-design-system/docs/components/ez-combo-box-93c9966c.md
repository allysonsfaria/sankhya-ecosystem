---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box/"
titulo: "Combo box"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box/"
trilha: "Docs > Components > Components Doc > Ez Combo Box"
---

# Combo box

Um combobox é um menu suspenso que apresenta uma lista de opções, ele pode ser usado em conjuntos com checkbox, entradas de textos e outros elementos.
Campos deste tipo permitem aos usuários escolher um valor a partir de uma lista opções filtrável.

![Imagem 1: Um combobox é um menu suspenso que apresenta uma lista de opções, ele pode ser usado em conjuntos com checkbox,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitar interação

![Imagem 2: Desabilitar interação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Mostra o valor da opção

#### Mostrar na opção selecionada.

![Imagem 3: Mostrar na opção selecionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Mostrar em todas as opções da lista.

![Imagem 4: Mostrar em todas as opções da lista.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo "slim"

![Imagem 5: Modo "slim"](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento `ezChange`

![Imagem 6: Evento ezChange](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Controle programático de foco: `setFocus()` e `setBlur()`

![Imagem 7: Controle programático de foco: setFocus() e setBlur()](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Posicionamento da lista

Em algumas situações pode ser necessário arbitrar o posicionamento da lista de opções. Isso é possível através da propriedade
`listOptionsPosition`. Essa propriedade permite definir o deslocamento horizontal e vertical da lista, além de determinar
a referência do deslocamento.

#### Horizontal

Naturalmente o deslocamento horizontal é aplicado da esquerda para a direita, mas isso pode
ser invertido passando o atributo `fromRight: true`.

![Imagem 8: Naturalmente o deslocamento horizontal é aplicado da esquerda para a direita, mas isso pode ser invertido passando o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Vertical

O mesmo acontece com o deslocamento vertical que por padrão posiciona a lista tendo o topo como referência, mas podemos
mostrá-la a partir da base - `fromBottom: true`. Caso a base seja a referência, a lista será exibida acima do seletor.

![Imagem 9: O mesmo acontece com o deslocamento vertical que por padrão posiciona a lista tendo o topo como referência, mas podemos…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo a ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `hideErrorOnFocusOut` `hide-error-on-focus-out` Quando verdadeiro deixa de exibir a mensagem de erro (se existente) quando focar em um elemento diferente. `boolean` `true`| `isTextSearch` `is-text-search` Informa se a pesquisa é do tipo texto. `boolean` `false`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `limitCharsToSearch` `limit-chars-to-search` Define o limite de caracteres mínimo para realizar uma pesquisa `number` `3`| `listOptionsPosition` -- Define um posicionamento fixo para a lista de opções do CheckBox. `IEzCheckBoxListPosition` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `optionLoader` -- Carrega as opções dinamicamente. `(argument: ISearchArgument) => IOption | IOption[] | Promise<IOption[]>` `undefined`| `options` -- Array com as opções do ez-combo-box. Os elementos devem obedecer o formato: `{value: string, label: string}`. `IOption[]` `undefined`| `preventAutoFocus` `prevent-auto-focus` Se true, impede que o campo de texto receba foco automaticamente ao abrir as opções. `boolean` `false`| `showOptionValue` `show-option-value` Se true cada opção na lista exibe o `value` junto com `label`. `boolean` `false`| `showSelectedValue` `show-selected-value` Se true a opção selecionada exibe o `value` junto com `label`. `boolean` `false`| `stopPropagateEnterKeyEvent` `stop-propagate-enter-key-event` Se true, ineterrompe a propagação do evento de KeyDown da tecla enter `boolean` `true`| `suppressEmptyOption` `suppress-empty-option` Se true remove a opção vazia da lista. `boolean` `false`| `suppressSearch` `suppress-search` Se true desabilita a digitação dentro do componente. `boolean` `false`| `textEmptyOption` `text-empty-option` Texto a ser apresentado na opção de valor nulo. `string` `undefined`| `value` `value` Define o valor do campo. `IOption | string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<IOption>`| `ezVisibilityChange` Emitido quando acontece a alteração de visibilidade do popover. `CustomEvent<boolean>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `clearValue() => Promise<void>`

Limpa o valor do campo de pesquisa

##### Returns

Type: `Promise<void>`

---

#### `getValueAsync() => Promise<unknown>`

##### Returns

Type: `Promise<unknown>`

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

- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-popover-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus)
- [ez-combo-box-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box/ez-combo-box-list)

#### Graph

```
graph TD;
  ez-combo-box --> ez-text-input
  ez-combo-box --> ez-icon
  ez-combo-box --> ez-popover-plus
  ez-combo-box --> ez-combo-box-list
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-popover-plus --> ez-popover-core
  ez-form-view --> ez-combo-box
  style ez-combo-box fill:#f9f,stroke:#333,stroke-width:4px
```

---
