---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chip/"
titulo: "Chip"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chip/"
trilha: "Docs > Components > Components Doc > Ez Chip"
---

# Chip

Documentação do componente EzChip.

![Imagem 1: Documentação do componente EzChip.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Tipo

A propriedade `type` define o estilo de cor do componente.
Valores possíveis:

- `primary` (padrão)
- `secondary`

![Imagem 2: secondary](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Largura máxima

A propriedade `maxWidth` define o tamanho máximo do componente.
Quando o texto não couber, será exibido um tooltip ao passar o mouse.

![Imagem 3: A propriedade maxWidth define o tamanho máximo do componente. Quando o texto não couber, será exibido um tooltip ao…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho

A propriedade `size` define a altura do chip.
Valores possíveis:

- `default` (32px de altura)
- `medium` (42px de altura)
- `large` (50px de altura)

![Imagem 4: large (50px de altura)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Icones

A propriedade `iconNameLeft` e `iconNameRight` adiciona ícones aos lados do chip, sem necessidade de slots.

![Imagem 5: A propriedade iconNameLeft e iconNameRight adiciona ícones aos lados do chip, sem necessidade de slots.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tooltip

A propriedade `showNativeTooltip` ativa o tooltip que é exibido ao colocar o ponteiro do mouse sobre o
componente. Este comportamento acontece de forma automática caso tenha definido largura máxima e espaço
interno não seja suficiente para apresentar o texto completamente.

![Imagem 6: A propriedade showNativeTooltip ativa o tooltip que é exibido ao colocar o ponteiro do mouse sobre o componente. Este…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado

Componente disponível para seleção.

![Imagem 7: Componente disponível para seleção.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Componente indisponível para seleção.

![Imagem 8: Componente indisponível para seleção.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Chip em modo ação

Componente com a propriedade "mode" alterada.

É possível determinar a propriedade "mode" com as seguintes opções:

- label: É a opção padrão do componente, possui o comportamento de seleção ativa;
- action: O chip terá o comportamento de um botão, não tendo mais o comportamento de seleção ativa.

Essa propriedade deve ser informada no formato string, exemplo:

```
<EzChip ... mode="action" ... />
```

![Imagem 9: Essa propriedade deve ser informada no formato string, exemplo: < EzChip ... mode = " action " ... />](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Chip com opção de remover

#### Com o ícone a esquerda

![Imagem 10: Com o ícone a esquerda](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Com o ícone a direita

![Imagem 11: Com o ícone a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com ícone de ação

Componente com ícone customizado e com ação de clique.

#### Com o ícone a esquerda

![Imagem 12: Com o ícone a esquerda](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Com o ícone a direita

![Imagem 13: Com o ícone a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Com ícone a esquerda e a direita

![Imagem 14: Com ícone a esquerda e a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com ícone de informação

![Imagem 15: Com ícone de informação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática
temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Chip**. Clicando nesse
botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

![Imagem 16: O exemplo abaixo demonstra isso através do botão Focar Chip . Clicando nesse botão o campo ganhará foco e após 2…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### valueChange()

Evento disparado quando o estado do componente mudar (onValueChange).

![Imagem 17: Evento disparado quando o estado do componente mudar (onValueChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### removeChip()

Evento disparado ao clicar no botão de remoção (onRemoveChip).

![Imagem 18: Evento disparado ao clicar no botão de remoção (onRemoveChip).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### actionClick()

Evento disparado ao clicar no chip usando o modo "action" (onActionClick).

![Imagem 19: Evento disparado ao clicar no chip usando o modo "action" (onActionClick).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### iconClick()

O evento `onIconClick` é disparado ao clicar em um ícone adicionado pelas propriedades `iconNameLeft` ou `iconNameRight`.
O evento recebe um objeto com a chave `icon`, que pode ser `'left'` ou `'right'`.

![Imagem 20: O evento onIconClick é disparado ao clicar em um ícone adicionado pelas propriedades iconNameLeft ou iconNameRight . O…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `disableAutoUpdateValue` `disable-auto-update-value` Desabilita a alteração da propriedade value ao clicar. `boolean` `false`| `enabled` `enabled` Se false o usuário não pode interagir com o ez-chip. `boolean` `true`| `iconNameLeft` `icon-name-left` Define o icone esquerdo. `string` `undefined`| `iconNameRight` `icon-name-right` Define o icone direito. `string` `undefined`| `label` `label` Texto a ser apresentado como título do ez-chip. `string` `undefined`| `maxWidth` `max-width` Define o tamanho máximo do chip. `string` `undefined`| `mode` `mode` Define o modo de uso do ez-chip. `"action" | "label"` `undefined`| `removePosition` `remove-position` Determina o posicionamento do botão de remover (não disponível no modo `action`). Se não informado, não exibe o botão. `"left" | "right"` `undefined`| `removeWithKeyboard` `remove-with-keyboard` Define se o chip deve ser removido ao pressionar a tecla Enter quando focado. `boolean` `false`| `showNativeTooltip` `show-native-tooltip` Exibe condicionalmente o tooltip nativo do navegador ao sobrepor o cursor acima do elemento. `boolean` `false`| `size` `size` Define o tamanho do chip. `"default" | "large" | "medium"` `'default'`| `tabIndex` `tab-index` Define o tabindex do chip. Por padrão é 0, permitindo que o chip seja focável. `number` `0`| `type` `type` Define o tipo de estilização do chip. `"error" | "error-light" | "primary" | "secondary" | "success" | "success-light" | "warning" | "warning-light"` `'primary'`| `value` `value` Define o valor do ez-chip. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `actionClick` Emitido no modo "action" quando o usuário clica no ez-chip. `CustomEvent<void>`| `iconClick` Emitido quando o icone é acionado. `CustomEvent<{ icon: "left" | "right"; }>`| `removeChip` Emitido quando o botão de remoção é acionado. `CustomEvent<void>`| `valueChange` Emitido quando acontece a alteração de valor do ez-chip. `CustomEvent<boolean>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do ez-chip.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Aplica o foco no ez-chip.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-tag-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tag-input)

#### Depends on

- [ez-tooltip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-chip --> ez-tooltip
  ez-chip --> ez-icon
  ez-tag-input --> ez-chip
  style ez-chip fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-label-chip--height Define a altura do chip.| --ez-label-chip\_\_label--font-size Define o tamanho do label.| --ez-label-chip\_\_label--font-family Define a família da fonte do label.| --ez-label-chip\_\_label--font-weight Define o peso da fonte do label.| --ez-label-chip\_\_horizontal-padding Define o espaçamento do label.| --ez-label-chip\_\_label--text--primary Define a cor do texto.| --ez-label-chip\_\_label--icon--primary Define a cor do ícone.| --ez-label-chip\_\_label\_\_container--border-radius Define o raio da borda do container do chip.| --ez-label-chip\_\_label\_\_container--border Define o estilo da borda do container.| --ez-label-chip\_\_label\_\_container--border-color-strokes Define a cor da borda do container.| --ez-label-chip\_\_label\_\_container-color--disabled Define a cor da borda e do fundo quando o chip está desativado.| --ez-label-chip\_\_label\_\_container--background-color Define a cor de fundo do container.| --ez-label-chip\_\_label\_\_container--border-color-active Define a cor da borda do container quando ativo.| --ez-label-chip\_\_label\_\_container--default--background-color--active Define a cor do fundo do container quando está ativo.| --ez-label-chip\_\_label\_\_container--default--color--active Define a cor do texto quando está ativo.| --ez-label-chip\_\_label\_\_container--text--disabled Define a cor do texto e do ícone quando o chip está desabilitado.| --ez-label-chip\_\_label\_\_container--default--border-color--active Define a cor da borda quando o componente está ativo.| --ez-label-chip\_\_label\_\_container--secondary--border-color--active Define a cor da borda quando o componente está ativo e na variação secundária.| --ez-label-chip\_\_label\_\_container--margin Define a margem do chip. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
