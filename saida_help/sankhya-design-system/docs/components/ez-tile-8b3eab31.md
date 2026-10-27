---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile/"
titulo: "Tile"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile/"
trilha: "Docs > Components > Components Doc > Ez Tile"
---

# Tile

O **Tile** é um componente versátil que pode ser utilizado para criação de um botão grande, item de menu ou elemento de navegação destacado.

![Imagem 1: O Tile é um componente versátil que pode ser utilizado para criação de um botão grande, item de menu ou elemento de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Tamanhos

O Tile suporta diferentes tamanhos, que podem ser definidos por meio da propriedade `size`.

![Imagem 2: O Tile suporta diferentes tamanhos, que podem ser definidos por meio da propriedade size .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Além disso o Tile suporta altura e largura customizadas por padrão, que podem ser definidas por meio das propriedades `height` e `width`.

![Imagem 3: Além disso o Tile suporta altura e largura customizadas por padrão, que podem ser definidas por meio das propriedades…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Cores

O Tile possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio
da propriedade `color`.

![Imagem 4: O Tile possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio da…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícone

O ícone utilizado no Tile pode ser definido pelo propriedade `iconName`, dentre os ícones disponíveis na biblioteca.

[Veja a lista completa de ícones.](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/)

![Imagem 5: Veja a lista completa de ícones.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Quantidade de linhas

O Tile por padrão apresenta somente 1 linha de texto, podemos mudar a quantidade máxima de linhas com a propriedade `maximumLines`.

![Imagem 6: O Tile por padrão apresenta somente 1 linha de texto, podemos mudar a quantidade máxima de linhas com a propriedade…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Interatividade

A propriedade `isInteractive` adiciona interatividade ao Tile, exibindo um feedback visual quando o mouse passa por cima
e permitindo gerenciar o evento de clique.

![Imagem 7: A propriedade isInteractive adiciona interatividade ao Tile, exibindo um feedback visual quando o mouse passa por cima…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setFocus e setBlur

O Tile pode receber ou remover foco de forma imperativa através dos métodos `setFocus` e `setBlur`.

![Imagem 8: O Tile pode receber ou remover foco de forma imperativa através dos métodos setFocus e setBlur .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `color` `color` Define a cor tema do componente. `"default" | "gray" | "green" | "red" | "yellow"` `"default"`| `height` `height` Define o tamanho do componente, sobrescrevendo o padrão da propriedade size. `number` `undefined`| `iconName` `icon-name` Define o ícone a ser usado da biblioteca de ícones: [ez-icons](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/) `string` `"home"`| `isInteractive` `is-interactive` Define se o componente será interativo. Caso contrário, será estático. Se true, permite permite clique. Se false, não permite clique `boolean` `false`| `maximumLines` `maximum-lines` Define a quantidade máxima de linhas de texto a serem apresentadas. Quando a propriedade não é passada, limita a 1 linha. `number` `undefined`| `size` `size` Define qual o tamanho do componente. - `"default"`: 120x80px - `"medium"`: 120x170px `"medium" | "small"` `"small"`| `text` `text` Texto a ser apresentado como título do componente. `string` `undefined`| `width` `width` Define a largura do componente, sobrescrevendo o padrão da propriedade size. `number` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `tileClick` Emitido quando o elemento principal é clicado `CustomEvent<void>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do componente.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Aplica o foco no componente.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-tile --> ez-icon
  style ez-tile fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-tile--width Define a largura do componente.| --ez-tile--height Define a altura do componente.| --ez-tile--padding Define a margem do componente.| --ez-tile--icon--margin-bottom Define o espaçamento entre o ícone e o title.| --ez-tile--border-radius Define o raio da borda do componente.| --ez-tile--background-color Define a cor de fundo do componente.| --ez-tile--color Define a cor do title.| --ez-tile--icon-color Define a cor do ícone.| --ez-tile--hover-background-color Define a cor de fundo do componente no hover.| --ez-tile--hover-color Define a cor do title no hover.| --ez-tile--hover-icon-color Define a cor do ícone no hover.| --ez-tile--focus-visible-border Define a cor do ícone no hover.| --ez-tile--font-family Define a família da fonte do title.| --ez-tile--font-weight Define o peso da fonte do title.| --ez-tile--font-size Define o tamanho do title.| --ez-tile--title-line-height Define a altura da linha do title.| --ez-tile--icon-line-height Define a altura da linha do ícone. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
