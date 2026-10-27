---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-actions-button/"
titulo: "Actions Button"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-actions-button/"
trilha: "Docs > Components > Components Doc > Ez Actions Button"
---

# Actions Button

![Imagem 1: Actions Button](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Habilitado

Utilizado nos momentos em que o usuário pode interagir com os botões.
Se a propriedade `enabled` não for passada, será habilitado como comportamento padrão.

![Imagem 2: Utilizado nos momentos em que o usuário pode interagir com os botões. Se a propriedade enabled não for passada, será…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Utilizado nos momentos em que o usuário não pode interagir com os botões.

![Imagem 3: Utilizado nos momentos em que o usuário não pode interagir com os botões.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanhos

#### Small

![Imagem 4: Small](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Medium

![Imagem 5: Medium](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Large

![Imagem 6: Large](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Todos os tamanhos

Colocando todos os tamanhos lado a lado para comparação.

![Imagem 7: Colocando todos os tamanhos lado a lado para comparação.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com label

Define se o label do item selecionado será apresentado no display do componente.

![Imagem 8: Define se o label do item selecionado será apresentado no display do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com ícone

Quando for utilizar ícone, deve-se passar a informação de qual ícone será utilizado.

![Imagem 9: Quando for utilizar ícone, deve-se passar a informação de qual ícone será utilizado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com checkOption

Define se na opção selecionada apresentará um ícone de check.

![Imagem 10: Define se na opção selecionada apresentará um ícone de check.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Altura máxima

Definindo a altura máxima que a lista de actions pode atingir.

![Imagem 11: Definindo a altura máxima que a lista de actions pode atingir.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com lista de ações (actions)

Define um array com a lista de ações. Os elementos devem obedecer o formato: `{value: string, label: string}`

![Imagem 12: Define um array com a lista de ações. Os elementos devem obedecer o formato: {value: string, label: string}](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitar item de menu (actions)

Para desabilitar um item específico, basta definir o valor `false` para o atributo `enabled`.

![Imagem 13: Para desabilitar um item específico, basta definir o valor false para o atributo enabled .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### hideActions()

Oculta a lista de ações.

Observação

No exemplo abaixo, ao clicar no botão disponível,
a lista de ações será exibida, após 2 segundos será chamado o médodo **hideActions()**,
e então a lista será ocultada automaticamente.

![Imagem 14: No exemplo abaixo, ao clicar no botão disponível, a lista de ações será exibida, após 2 segundos será chamado o médodo…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### isOpened()

Verifica se a lista de ações está oculta.

![Imagem 15: Verifica se a lista de ações está oculta.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezAction()

Evento disparado ao acionar uma ação.

![Imagem 16: Evento disparado ao acionar uma ação.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `actions` -- Define a lista de ações. Os elementos devem obedecer o formato: `{value: string, label: string}`. `IAction[]` `undefined`| `arrowActive` `arrow-active` Se true a seta de ordenação será apresentada. `boolean` `false`| `checkOption` `check-option` Se true o check será apresentado para os itens. `boolean` `false`| `displayIcon` `display-icon` Define o ícone do componente. `string` `undefined`| `enabled` `enabled` Se false o usuário não pode interagir com o componente. `boolean` `true`| `isTransparent` `is-transparent` Se true o background será transparent. `boolean` `false`| `showLabel` `show-label` Se true o label será apresentado. `boolean` `false`| `size` `size` Determina o tamanho do ez-action-button. `"large" | "medium" | "small"` `"medium"`| `value` `value` Define o valor do componente. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezAction` Emitido ao acionar uma ação. `CustomEvent<IAction>`| `ezDisconnectedActionButtons` Emitido quando componente é desconectado da DOM `CustomEvent<void>`| `ezPopoverOpen` Emitido ao mostrar a lista de ações `CustomEvent<HTMLElement>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `hideActions() => Promise<void>`

Oculta a lista de ações.

##### Returns

Type: `Promise<void>`

---

#### `isOpened() => Promise<boolean>`

Verifica se a lista de ações está aberta.

##### Returns

Type: `Promise<boolean>`

---

#### `showActions() => Promise<void>`

Apresenta a lista de ações.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-actions-button --> ez-button
  ez-actions-button --> ez-icon
  ez-button --> ez-icon
  style ez-actions-button fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-actions-button\_\_actions-list--border-radius Define o raio da borda do popover.| --ez-actions-button\_\_actions-list--box-shadow Define a sombra do popover.| --ez-actions-button\_\_actions-list--background-color Define a cor de fundo do popover.| --ez-actions-button\_\_actions-list--padding Define o espaçamento interno do popover| --ez-actions-button\_\_actions-list--top-margin Define a distancia entre o botão e o popover| --ez-actions-button\_\_actions-list--z-index Define a elevação do popover.| --ez-actions-button\_\_actions-max-height Define a altura máxima do popover.| --ez-actions-button\_\_btn-action--min-width Define a largura mínima do popover| --ez-actions-button\_\_btn-action--background-color Define a cor de fundo do popover | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
