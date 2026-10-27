---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input/"
titulo: "Text Input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input/"
trilha: "Docs > Components > Components Doc > Ez Text Input"
---

# Text Input

Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o cumprimento do conteúdo que você espera que o usuário insira. Esse input padrão é para conteúdo curto de uma linha.

![Imagem 1: Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados.

### Deixa o campo disponível.

![Imagem 2: Deixa o campo disponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Deixa o campo indisponível.

![Imagem 3: Deixa o campo indisponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Label.

![Imagem 4: Label.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com estado de erro.

![Imagem 5: Com estado de erro.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo regular.

![Imagem 6: Modo regular.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo slim.

![Imagem 7: Modo slim.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo Password.

![Imagem 8: Modo Password.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Aplica uma máscara no campo.

![Imagem 9: Aplica uma máscara no campo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exibe mensagem de erro.

![Imagem 10: Exibe mensagem de erro.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Restringe o que o usuário pode digitar.

![Imagem 11: Restringe o que o usuário pode digitar.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Define se o campo contará com bordas.

![Imagem 12: Define se o campo contará com bordas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

### Faz o foco no componente de input.

![Imagem 13: Faz o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remove o foco no componente de input.

![Imagem 14: Remove o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Informand se o campo está inválido.

![Imagem 15: Informand se o campo está inválido.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Ao mudar o estado do componente.

![Imagem 16: Ao mudar o estado do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo a ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `cleanValueMask` `clean-value-mask` Para remover a máscara quando fizer um apply no formulário. `boolean` `false`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `hasInvalid` `has-invalid` Define se o campo está em estado inválido (bordas vermelhas). `boolean` `false`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mask` `mask` Aplica uma máscara no conteúdo conforme o padrão estabelecido `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `noBorder` `no-border` Se true o campo não terá bordas. `boolean` `false`| `password` `password` Se true o campo não terá bordas. `boolean` `false`| `restrict` `restrict` Restringe o que o usuário pode digitar. `string` `undefined`| `value` `value` Define o valor do campo. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<string>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

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

- [ez-combo-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box)
- [ez-date-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input)
- [ez-date-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-time-input)
- [ez-filter-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input)
- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)
- [ez-link-builder](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-link-builder)
- [ez-number-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-number-input)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)
- [ez-search-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus)
- [ez-simple-image-uploader](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-simple-image-uploader)
- [ez-text-edit](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit)
- [ez-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-time-input)

#### Depends on

- [ez-tooltip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-combo-box --> ez-text-input
  ez-date-input --> ez-text-input
  ez-date-time-input --> ez-text-input
  ez-filter-input --> ez-text-input
  ez-form-view --> ez-text-input
  ez-link-builder --> ez-text-input
  ez-number-input --> ez-text-input
  ez-search --> ez-text-input
  ez-search-plus --> ez-text-input
  ez-simple-image-uploader --> ez-text-input
  ez-text-edit --> ez-text-input
  ez-time-input --> ez-text-input
  style ez-text-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-text-input--height Define a altura do componente.| --ez-text-input--width Define a largura do componente.| --ez-text-input\_\_icon--width Define a largura do slot que contém o ícone.| --ez-text-input--height--slim Define a altura do componente em modo "slim".| --ez-text-input\_\_min-width Define a largura maxima do componente.| --ez-text-input\_\_max-width Define a largura minima do componente.| --ez-text-input--border-radius Define o raio da borda do input do componente.| --ez-text-input--border-top-left-radius Define o raio da borda no top esquerdo do componente.| --ez-text-input--border-bottom-left-radius Define o raio da borda inferior esquerda do componente.| --ez-text-input--border-top-right-radius Define o raio da borda no top direito do componente.| --ez-text-input--border-bottom-right-radius Define o raio da borda inferior direita do componente.| --ez-text-input--font-size Define o tamanho da fonte do input e label do componente.| --ez-text-input--font-family Define a família da fonte do input, label e caixa de mensagem do componente.| --ez-text-input--font-weight Define o peso da fonte do label do componente.| --ez-text-input--color Define a cor da fonte do input e label do componente.| --ez-text-input\_\_margin-bottom Define a margem abaixo do componente.| --ez-text-input\_\_input--background-color Define a cor de fundo do input.| --ez-text-input\_\_input--border Define o estilo da borda do input.| --ez-text-input\_\_input--border-color Define a cor da borda do input.| --ez-text-input\_\_input--focus--border-color Define a cor da borda do input quando focado.| --ez-text-input\_\_input--disabled--background-color Define a cor de fundo do input quando desabilitado.| --ez-text-input\_\_input--disabled--color Define a cor do texto do input.| --ez-text-input\_\_input--error--border-color Define a cor da borda do input quando com erro.| --ez-text-input\_\_input--noborder-color Define a cor do input quando não possuir borda| --ez-text-input\_\_input--padding Define o padding do input| --ez-text-input\_\_placeholder--color Define a cor do placeholder do input.| --ez-text-input\_\_tooltip\_icon--error--color Define a cor da fonte da mensagem quando erro.| --ez-text-input\_\_label--floating--top Define o posicionamento do label.| --ez-text-input\_\_label--padding-top Define o posicionamento do label.| --ez-text-input\_\_label--padding-left Define o espaçamento esquerdo do label.| --ez-text-input\_\_label--padding-right Define o espaçamento direito do label.| --ez-text-input\_\_input--focus--icon-color Define a cor do ícone do slot.| --ez-text-input\_\_input--disabled--focus--icon-color Define a cor do ícone do slot quando disabled.| --ez-text-input\_\_tooltip-icon--spacing Define o espaçamento lateral do icone de erro.| --ez-text-input\_\_tooltip-icon---width Define a largura do icone de erro.| --ez-text-input\_\_tooltip-icon---horizontal-margin Define a margem horizontal do icone de erro.| --ez-text-input\_\_tooltip-icon---vertical-margin Define a margem vertical do icone de erro. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
