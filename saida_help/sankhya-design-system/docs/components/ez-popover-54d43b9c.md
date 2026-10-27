---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover/"
titulo: "Popover"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover/"
trilha: "Docs > Components > Components Doc > Ez Popover"
---

# Popover

![Imagem 1: Popover](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Controle de exibição

O controle de exibição do componente é feito através de dois métodos e um atributo:

- show() faz com o que seja exibido.
- hide() oculta o elemento.
- Além disso, caso o usuário clique em algum lugar fora do conteúdo o faz ocultar automaticamente. Isso pode ser desligado pela flag "autoClose".

Observação

É necessário definir o parâmetro `overlayType` com valor **none**.
Uma vez que, tendo o `overlayType` ligado o `autoClose` por regra também será ligado.

![Imagem 2: É necessário definir o parâmetro overlayType com valor none . Uma vez que, tendo o overlayType ligado o autoClose por…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Controle de sobreposição

Por padrão, o popover é exibido acima de outros elementos com uma sobreposição/overlay, essa
sobreposição é controlada pela propriedade `overlayType`. Caso a propriedade `autoClose` esteja
desligada e a propriedade `overlayType` seja diferente de `none`, o componente irá desconsiderar o valor
de `autoClose` e sempre fechará o popover ao clicar fora do conteúdo.

![Imagem 3: Por padrão, o popover é exibido acima de outros elementos com uma sobreposição/overlay, essa sobreposição é controlada…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Demonstrando o valor de opened

Sempre que os métodos "show" e "hide" são chamados, um evento "ezVisibilityChange" é disparado.
Usando esse evento juntamente com a propriedade "opened", é possível reagir à abertura e fechamento do componente:

![Imagem 4: Sempre que os métodos "show" e "hide" são chamados, um evento "ezVisibilityChange" é disparado. Usando esse evento…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Usando largura total

![Imagem 5: Usando largura total](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Abrindo abaixo de um elemento

É possível determinar que o popover se posicione no canto inferior esquerdo de um elemento HTML, por exemplo um botão.
Para isso é necessário usar o método "showUnder" ao invés do "show", sendo necessário informar o elemento de referência.
Também é possível determinar o posicionamento a partir do canto direito ao invés do esquerdo.
Há ainda a opção de informar algum deslocamento horizontal e/ou vertical.

![Imagem 6: É possível determinar que o popover se posicione no canto inferior esquerdo de um elemento HTML, por exemplo um botão.…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Alterando a posição do popover

![Imagem 7: Alterando a posição do popover](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `autoClose` `auto-close` Define que será fechado automaticamente quando o usuário clicar fora do conteúdo. `boolean` `true`| `boxWidth` `box-width` Ajusta o comportamento da largura do popover. `"fit-content" | "full-width"` `"fit-content"`| `innerElement` `inner-element` Define as tags que serão consideradas conteúdo. `string | string[]` `undefined`| `opened` `opened` Define se o ez-popover está aberto. `boolean` `undefined`| `overlayType` `overlay-type` Define o tipo de overlay do popover. `"light" | "medium" | "none"` `"light"` | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezVisibilityChange` Emitido quando acontece a alteração de estado do componente. `CustomEvent<boolean>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `hide() => Promise<void>`

Oculta o ez-popover.

##### Returns

Type: `Promise<void>`

---

#### `show(top?: string, left?: string) => Promise<void>`

Exibe o ez-popover.

##### Returns

Type: `Promise<void>`

---

#### `showUnder(element: HTMLElement, options?: IEzPopoverAnchorOptions) => Promise<void>`

Ancora a exibição do popOver a um elemento HTML.

##### Returns

Type: `Promise<void>`

---

#### `updatePosition(top?: string, left?: string) => Promise<void>`

Atualiza a posição do popover.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form)
- [ez-grid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)

#### Graph

```
graph TD;
  ez-form --> ez-popover
  ez-grid --> ez-popover
  style ez-popover fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-popover\_\_box--border-radius Define o raio da borda do popover.| --ez-popover\_\_box--box-shadow Define a sombra do popover.| --ez-popover\_\_box--background-color Define a cor de fundo do popover.| --ez-popover\_\_box--z-index Define a camada de visibilidade do popover. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
