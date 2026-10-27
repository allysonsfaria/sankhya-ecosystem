---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-text-area/"
titulo: "Classic Text Area"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-text-area/"
trilha: "Docs > Components > Components Doc > Ez Classic Text Area"
---

# Classic Text Area

O **Classic Text Area** é um componente de entrada de texto multilinha versátil que oferece diversas opções de customização, incluindo ícones, redimensionamento automático e estados visuais.

![Imagem 1: O Classic Text Area é um componente de entrada de texto multilinha versátil que oferece diversas opções de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Estados Visuais

O Classic Text Area suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

![Imagem 2: O Classic Text Area suporta diferentes estados visuais que podem ser definidos pela propriedade state .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones

É possível adicionar ícones à esquerda e/ou direita do textarea, com opção de torná-los clicáveis.

![Imagem 3: É possível adicionar ícones à esquerda e/ou direita do textarea, com opção de torná-los clicáveis.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Redimensionamento

O componente oferece suporte a diferentes modos de redimensionamento (vertical, horizontal, ambos ou nenhum).

![Imagem 4: O componente oferece suporte a diferentes modos de redimensionamento (vertical, horizontal, ambos ou nenhum).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

![Imagem 5: Controle sobre estados desabilitado e somente leitura.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Evento ezChange

Disparado sempre que o valor do textarea é alterado.

![Imagem 6: Disparado sempre que o valor do textarea é alterado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento ezBlur

Disparado quando o textarea perde o foco.

![Imagem 7: Disparado quando o textarea perde o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento iconClick

Disparado quando um ícone clicável é clicado.

![Imagem 8: Disparado quando um ícone clicável é clicado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

![Imagem 9: Métodos para controlar programaticamente o foco do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enabled` `enabled` Define se a textarea está habilitada `boolean` `true`| `helpText` `help-text` Texto de ajuda exibido abaixo da textarea `string` `undefined`| `label` `label` Texto do rótulo exibido acima da área de texto `string` `''`| `leftIconClickable` `left-icon-clickable` Define se o ícone da esquerda é clicável `boolean` `false`| `leftIconName` `left-icon-name` Nome do ícone à esquerda `string` `undefined`| `leftIconTooltip` `left-icon-tooltip` Título do ícone à esquerda (tooltip) `string` `undefined`| `maxlength` `maxlength` Número máximo de caracteres permitidos `number` `undefined`| `name` `name` Nome da textarea `string` `StringUtils.generateUUID()`| `placeholder` `placeholder` Texto de placeholder exibido quando a área de texto está vazia `string` `''`| `readonly` `readonly` Se a área de texto é somente leitura `boolean` `false`| `resize` `resize` Comportamento de redimensionamento da área de texto `"both" | "horizontal" | "none" | "vertical"` `'vertical'`| `rightIconClickable` `right-icon-clickable` Define se o ícone da direita é clicável `boolean` `false`| `rightIconName` `right-icon-name` Nome do ícone à direita `string` `undefined`| `rightIconTooltip` `right-icon-tooltip` Título do ícone à direita (tooltip) `string` `undefined`| `rows` `rows` Define o número de linhas da área de texto `number` `5`| `state` `state` Estado visual da textarea: default, error, success ou warning `"default" | "error" | "success" | "warning"` `"default"`| `value` `value` Valor atual da área de texto `string` `''` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezBlur` Evento emitido quando a área de texto perde foco `CustomEvent<string>`| `ezChange` Evento emitido quando o valor da área de texto muda `CustomEvent<string>`| `iconClick` Evento disparado quando um ícone é clicado. Payload: { icon: "left" | "right" } `CustomEvent<{ icon: "left" | "right"; }>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

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

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-classic-text-area --> ez-icon
  style ez-classic-text-area fill:#f9f,stroke:#333,stroke-width:4px
```

---
