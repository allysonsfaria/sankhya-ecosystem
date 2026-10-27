---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile-medium/"
titulo: "Tile Medium"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile-medium/"
trilha: "Docs > Components > Components Doc > Ez Tile Medium"
---

# Tile Medium

O **Tile Medium** é um componente que pode ser utilizado para somente leitura ou acompanhado de um botão que pode enviar para uma página específica, contém tags para mostrar status, título e parágrafo configuráveis para atender a necessidade do time que for usar.

![Imagem 1: O Tile Medium é um componente que pode ser utilizado para somente leitura ou acompanhado de um botão que pode enviar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Tamanhos

O Tile Medium tem por padrão as dimensões fixas de `446px * 257px`
O Tile Medium suporta altura e largura customizadas por padrão, que podem ser definidas por meio das propriedades `height` e `width`.

![Imagem 2: O Tile Medium tem por padrão as dimensões fixas de 446px * 257px O Tile Medium suporta altura e largura customizadas…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Cores

O Tile Medium possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por meio
da propriedade `color`.

![Imagem 3: O Tile Medium possui 5 variações de cores nativas dentro da paleta de cores Design System, que podem ser definidas por…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações - Header

O header do Tile Medium pode ser construído de forma dinâmica. Do lado esquerdo podendo ser apresentado um ícone ou avatar. Do lado esquerdo podendo apresentar até 3 tags de cores diferentes.

### Ícone

O ícone, quando presente, fica do canto superior esquerdo do componente.

- O ícone é definido pela propriedade `iconName`;
- Uma cor customizada pode ser passada para o ícone pela propriedade `iconColor`, dentre as cores da paleta do Design System.
  [Veja a paleta de cores...](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/acorde/cores/)

![Imagem 4: Uma cor customizada pode ser passada para o ícone pela propriedade iconColor , dentre as cores da paleta do Design…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Avatar

O avatar, quando presente, fica do canto superior esquerdo do componente, substituindo o ícone quando este também for definido

- O avatar é definido pela propriedade `avatarProps`, que é um objeto que define as propriedades do avatar, sendo elas:
  - `name?: string;` (Define a letra que será apresentada no avatar)
  - `shape?: 'circle' | 'square';` (Define o formato do avatar)
  - `imageSrc?: string;` (Define uma imagem a ser apresentada no avatar)

![Imagem 5: imageSrc?: string; (Define uma imagem a ser apresentada no avatar)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tags

As tag, quando presentes, ficam do canto superior direito do componente. O componente suporte de até 3 tags simultâneas.

- A tags são definidos pela propriedade `tags`, que é array de objetos que define as propriedades do grupo de tags, sendo elas:
  - `label: string;` (Define a letra que será apresentada no avatar)
  - `color?: string;` (Define o formato do avatar)

![Imagem 6: color?: string; (Define o formato do avatar)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações - Content

A seção de conteúdo do Tile Medium pode apresentar dinamicamente 3 níveis de texto (Título pequeno, Título principal e descrição) e um botão.

Caso algumas das propriedades que definem cada sub-seção não tenha valor, a mesma não será apresentada

### Textos

- O Título Pequeno, pode ser passado por meio da variável `smallTitleText`
- O Título Principal, pode ser passado por meio da variável `titleText`
- A descrição, pode ser passado por meio da variável `descriptionText`

![Imagem 7: A descrição, pode ser passado por meio da variável descriptionText](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Quantidade máxima de linhas

A quantidade máxima de linhas de texto apresentadas em cada seção pode ser definida através das propriedades:

- Quantidade máxima de linhas do Título Pequeno, pode ser definida por meio da variável `smallTitleMaximumLines` (Padrão 1)
- Quantidade máxima de linhas do Título Principal, pode ser definida por meio da variável `titleMaximumLines` (Padrão 1)
- Quantidade máxima de linhas da descrição, pode ser definida por meio da variável `descriptionMaximumLines` (Padrão 3)

![Imagem 8: Quantidade máxima de linhas da descrição, pode ser definida por meio da variável descriptionMaximumLines (Padrão 3)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Botão

O botão, quando presente, fica do canto inferior esquerdo do componente.

- O botão é definido pela propriedade `buttonProps`, que é um objeto que define as propriedades do ez-button, sendo elas:

  ```
  label: string;
  enabled?: boolean;
  mode?: 'regular' | 'icon' | 'link' | 'label-icon';
  iconName?: string;
  size?: 'x-small' | 'small' | 'medium' | 'large';
  onClick: () => void;
  colors?:{
    background?: string;
    backgroundHover?: string;
    backgroundActive?: string;
    text?: string;
    textHover?: string;
    textActive?: string;
  }
  ```

![Imagem 9: O botão é definido pela propriedade buttonProps , que é um objeto que define as propriedades do ez-button, sendo elas:…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setFocus e setBlur

O Tile Medium pode receber ou remover foco de forma imperativa através dos métodos `setFocus` e `setBlur`.

![Imagem 10: O Tile Medium pode receber ou remover foco de forma imperativa através dos métodos setFocus e setBlur .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `avatarProps` -- Propriedade utilizada para configurar o avatar, se definida substitui o ícone por um ez-avatar `{ name?: string; imageSrc?: string; shape?: "circle" | "square"; }` `undefined`| `buttonProps` -- Define as props que serão passadas para o botão, caso o objeto seja passado, o botão será renderizado. `{ label: string; enabled?: boolean; mode?: "link" | "regular" | "icon" | "label-icon"; iconName?: string; size?: "small" | "medium" | "large" | "x-small"; onClick: () => void; colors?: { background?: string; backgroundHover?: string; backgroundActive?: string; text?: string; textHover?: string; textActive?: string; }; }` `undefined`| `color` `color` Define a cor tema do componente. `"default" | "gray" | "green" | "red" | "yellow"` `"default"`| `descriptionMaximumLines` `description-maximum-lines` Define a quantidade máxima de linhas de texto a serem apresentadas na descrição. Quando a propriedade não é passada, limita a 3 linhas. `number` `undefined`| `descriptionText` `description-text` Texto a ser apresentado como descrição do componente `string` `undefined`| `height` `height` Define a altura do componente, sobrescrevendo o padrão de 257px. `string` `undefined`| `iconColor` `icon-color` Define uma cor customizada para o ícone, dentro da paleta de cores do Design System. Exemplo: "--color--yellow-600" `string` `undefined`| `iconName` `icon-name` Define o ícone a ser usado da biblioteca de ícones: [ez-icons](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/) `string` `undefined`| `smallTitleMaximumLines` `small-title-maximum-lines` Define a quantidade máxima de linhas de texto a serem apresentadas no título pequeno. Quando a propriedade não é passada, limita a 1 linha. `number` `undefined`| `smallTitleText` `small-title-text` Texto a ser apresentado como um título pequeno do componente. `string` `undefined`| `tags` -- Define as props que serão passadas para as tags, caso um objeto seja passado, a(s) tag(s) será renderizada(s), se limitando a 3 tags. `{ label: string; color?: string; }[]` `undefined`| `titleMaximumLines` `title-maximum-lines` Define a quantidade máxima de linhas de texto a serem apresentadas no título. Quando a propriedade não é passada, limita a 1 linha. `number` `undefined`| `titleText` `title-text` Texto a ser apresentado como título do componente. `string` `undefined`| `width` `width` Define a largura do componente, sobrescrevendo o padrão de 446px. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `setButtonBlur() => Promise<void>`

Remove o foco do botão.

##### Returns

Type: `Promise<void>`

---

#### `setButtonFocus() => Promise<void>`

Aplica o foco no botão.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-badge](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-badge)
- [ez-avatar](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-avatar)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-tile-medium --> ez-badge
  ez-tile-medium --> ez-avatar
  ez-tile-medium --> ez-icon
  ez-tile-medium --> ez-button
  ez-badge --> ez-icon
  ez-avatar --> ez-icon
  ez-button --> ez-icon
  style ez-tile-medium fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-tile-medium--width Define a largura do componente.| --ez-tile-medium--height Define a altura do componente.| --ez-tile-medium--padding Define a margem do componente.| --ez-tile-medium--border-radius Define o raio da borda do componente.| --ez-tile-medium--background-color Define a cor do fundo.| --ez-tile-medium--color Define a cor do title.| --ez-tile-medium--icon-color Define a cor do ícone.| --ez-tile-medium--font-family Define a família da fonte do title.| --ez-tile-medium--header-gap Define o gap entre a seção de imagem e tags.| --ez-tile-medium--icon-line-height Define a altura da linha do ícone.| --ez-tile-medium--tag-group-gap Define o gap entre uma tag e outra.| --ez-tile-medium\_button--background-color Define a cor de fundo do botão.| --ez-tile-medium\_button--color Define a cor do label do botão.| --ez-tile-medium\_button--hover--background-color Define a cor de fundo quando o cursor está sobre o botão.| --ez-tile-medium\_button--hover-color Define a cor do texto e do ícone quando o cursor está sobre o botão.| --ez-tile-medium\_button--active--background-color Define a cor do fundo ao ativar o botão.| --ez-tile-medium\_button--active-color Define a cor do texto e do ícone ao ativar o botão. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
