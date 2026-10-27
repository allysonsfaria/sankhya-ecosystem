---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-area/"
titulo: "Text Area"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-area/"
trilha: "Docs > Components > Components Doc > Ez Text Area"
---

# Text Area

Utilizado para entradas mais longas de várias linhas.

![Imagem 1: Utilizado para entradas mais longas de várias linhas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados.

### Deixa o campo disponível.

![Imagem 2: Deixa o campo disponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Deixa o campo indisponível.

![Imagem 3: Deixa o campo indisponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exibe mensagem de erro.

![Imagem 4: Exibe mensagem de erro.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Define número de linhas.

![Imagem 5: Define número de linhas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Permite exibir a mensagem de erro.

![Imagem 6: Permite exibir a mensagem de erro.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo regular.

![Imagem 7: Modo regular.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo slim.

![Imagem 8: Modo slim.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

### Faz o foco no componente de input.

![Imagem 9: Faz o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remove o foco no componente de input.

![Imagem 10: Remove o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Informa se o campo está inválido.

![Imagem 11: Informa se o campo está inválido.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adiciona ou substitui texto selecionado por um valor informado.

![Imagem 12: Adiciona ou substitui texto selecionado por um valor informado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Ao mudar o estado do componente.

![Imagem 13: Ao mudar o estado do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo a ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `autoRows` `auto-rows` Ativa a opção de fazer as linhas do componente serem baseados na altura máxima. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enableResize` `enable-resize` Ativa a opção de fazer resize do input. `boolean` `true`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `'regular'`| `rows` `rows` Define o número de linhas. `number` `4`| `value` `value` Define o valor do campo. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<string>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `appendTextToSelection(text: string) => Promise<void>`

Adiciona o argumento text no value do text area, seguindo as regras:

- Se o cursor do mouse está posicionado em algum local do texto, o argumento será adicionado nesse local.
- Se existir uma seleção no texto, o trecho selecionado deve ser substituído pelo argumento.
- Se não existir seleção nem posicionamento do cursor do mouse, o argumento será adicionado no final do texto.

##### Returns

Type: `Promise<void>`

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

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)
- [ez-rich-text](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text)

#### Depends on

- [ez-tooltip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-text-area --> ez-tooltip
  ez-text-area --> ez-icon
  ez-form-view --> ez-text-area
  ez-rich-text --> ez-text-area
  style ez-text-area fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --text-area--width Define a largura do componente.| --text-area--border-radius Define o raio da borda do input do componente.| --text-area--font-size Define o tamanho da fonte do input e label do componente.| --text-area--font-family Define a família da fonte do input, label e caixa de mensagem do componente.| --text-area--font-weight Define o peso da fonte do label do componente.| --text-area--color Define a cor da fonte do input e label do componente.| --text-area\_\_input--background-color Define a cor de fundo do input.| --text-area\_\_input--border Define o estilo da borda do input.| --text-area\_\_input--border-color Define a cor da borda do input.| --text-area\_\_input--focus--border-color Define a cor da borda do input quando focado.| --text-area\_\_input--disabled--background-color Define a cor de fundo do input quando desabilitado.| --text-area\_\_input--disabled--color Define a cor do texto do input.| --text-area\_\_input--disabled--border--color Define a borda do texto do input quando desabilitado.| --text-area\_\_input--error--border-color Define a cor da borda do input quando com erro.| --text-area\_\_message\_box--font-size Define o tamanho da fonte da mensagem abaixo do input.| --text-area\_\_message\_box--info--color Define a cor da fonte da mensagem quando info.| --text-area\_\_message\_box--error--color Define a cor da fonte da mensagem quando erro.| --text-area\_\_label--floating--top Define o posicionamento do label.| --text-area\_\_label--padding-top Define o espaçamento superior do label.| --text-area\_\_label--padding-left Define o espaçamento esquerdo do label.| --text-area\_\_label--padding-right Define o espaçamento direito do label.| --text-area\_\_scrollbar--color-default Define a cor da barra de rolagem do componente.| --text-area\_\_scrollbar--color-background Define a cor de fundo da barra de rolagem do componente.| --text-area\_\_scrollbar--color-hover Define a cor do hover na barra de rolagem do componente.| --text-area\_\_scrollbar--color-clicked Define a cor do active na barra de rolagem do componente.| --text-area\_\_scrollbar--border-radius Define o raio da borda da barra de rolagem do componente.| --text-area\_\_scrollbar--width Define a largura da barra de rolagem do componente.| --ez-text-area\_\_tooltip-icon--spacing Define o espaçamento lateral do icone de erro.| --ez-text-area\_\_tooltip-icon---width Define a largura do icone de erro.| --ez-text-area\_\_tooltip-icon---horizontal-margin Define a margem horizontal do icone de erro.| --ez-text-area\_\_tooltip-icon---vertical-margin Define a margem vertical do icone de erro.| --ez-text-area\_\_tooltip\_icon--error--color Define a cor da fonte da mensagem quando erro. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
