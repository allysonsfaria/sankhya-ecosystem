---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-input/"
titulo: "Classic Input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-input/"
trilha: "Docs > Components > Components Doc > Ez Classic Input"
---

# Classic Input

O **Classic Input** é um componente de entrada de texto versátil que oferece diversas opções de customização, incluindo ícones, máscaras e estados visuais.

![Imagem 1: O Classic Input é um componente de entrada de texto versátil que oferece diversas opções de customização, incluindo…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Estados Visuais

O Classic Input suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

![Imagem 2: O Classic Input suporta diferentes estados visuais que podem ser definidos pela propriedade state .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones

É possível adicionar ícones à esquerda e/ou direita do input, com opção de torná-los clicáveis.

![Imagem 3: É possível adicionar ícones à esquerda e/ou direita do input, com opção de torná-los clicáveis.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Máscaras

O componente oferece suporte a máscaras para formatação automática dos dados inseridos.

![Imagem 4: O componente oferece suporte a máscaras para formatação automática dos dados inseridos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tipos de Input

Suporte a diferentes tipos de input HTML para validação e comportamento específicos. A propriedade `type`
aceita todos os tipos nativos do elemento HTML `<input>` (text, email, password, number, tel, url, search, etc.).

![Imagem 5: Suporte a diferentes tipos de input HTML para validação e comportamento específicos. A propriedade type aceita todos os…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

![Imagem 6: Controle sobre estados desabilitado e somente leitura.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Evento ezChange

Disparado sempre que o valor do input é alterado.

![Imagem 7: Disparado sempre que o valor do input é alterado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento ezBlur

Disparado quando o input perde o foco.

![Imagem 8: Disparado quando o input perde o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento iconClick

Disparado quando um ícone clicável é clicado.

![Imagem 9: Disparado quando um ícone clicável é clicado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

![Imagem 10: Métodos para controlar programaticamente o foco do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `emitMaskedValue` `emit-masked-value` Define se o valor emitido pelo evento ezChange deve conter a máscara aplicada (padrão: false) `boolean` `false`| `enabled` `enabled` Define se o input está habilitado `boolean` `true`| `helpText` `help-text` Texto de ajuda exibido abaixo do input `string` `undefined`| `label` `label` Texto do label exibido acima do input `string` `undefined`| `leftIconClickable` `left-icon-clickable` Define se o ícone da esquerda é clicável `boolean` `false`| `leftIconName` `left-icon-name` Nome do ícone à esquerda `string` `undefined`| `leftIconTooltip` `left-icon-tooltip` Título do ícone à esquerda (tooltip) `string` `undefined`| `mask` `mask` Aplica uma máscara no conteúdo conforme o padrão estabelecido. Para mais informações acesse: <https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/maskformatter/> `string` `undefined`| `maxlength` `maxlength` Tamanho máximo do valor `number` `undefined`| `minlength` `minlength` Tamanho mínimo do valor `number` `undefined`| `name` `name` Nome do input `string` `undefined`| `placeholder` `placeholder` Placeholder do input `string` `undefined`| `readonly` `readonly` Define se o input é somente leitura `boolean` `false`| `rightIconClickable` `right-icon-clickable` Define se o ícone da direita é clicável `boolean` `false`| `rightIconName` `right-icon-name` Nome do ícone à direita `string` `undefined`| `rightIconTooltip` `right-icon-tooltip` Título do ícone à direita (tooltip) `string` `undefined`| `state` `state` Estado visual do input: default, error, success ou warning `"default" | "error" | "success" | "warning"` `"default"`| `type` `type` Tipo do input (ex: text, password, email, etc) `string` `'text'`| `value` `value` Valor do input `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezBlur` Evento disparado quando o input perde o foco. `CustomEvent<string>`| `ezChange` Evento disparado quando o valor do input muda. `CustomEvent<string>`| `ezFocus` Evento disparado quando o input ganha o foco. `CustomEvent<string>`| `iconClick` Evento disparado quando um ícone é clicado. Payload: { icon: "left" | "right" } `CustomEvent<{ icon: "left" | "right"; }>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

---

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-classic-combo-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-combo-box)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-classic-input --> ez-icon
  ez-classic-combo-box --> ez-classic-input
  style ez-classic-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-classic-input--label-color Define a cor do texto do input.| --ez-classic-input--border-color-default Define a cor da borda do input quando está no estado padrão.| --ez-classic-input--border-color-focus Define a cor da borda do input quando está no estado de foco.| --ez-classic-input--border-color-success Define a cor da borda do input quando está no estado de sucesso.| --ez-classic-input--border-color-error Define a cor da borda do input quando está no estado de erro.| --ez-classic-input--border-color-warning Define a cor da borda do input quando está no estado de aviso.| --ez-classic-input--background-color Define a cor de fundo do input.| --ez-classic-input--background-color-disabled Define a cor de fundo do input quando está desabilitado.| --ez-classic-input--text-color Define a cor do texto do input.| --ez-classic-input--placeholder-color Define a cor do texto do placeholder do input.| --ez-classic-input--icon-color Define a cor do ícone do input.| --ez-classic-input--helptext-color Define a cor do texto de ajuda do input.| --ez-classic-input--height Define a altura do input. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
