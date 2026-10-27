---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-button/"
titulo: "Split Button"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-button/"
trilha: "Docs > Components > Components Doc > Ez Split Button"
---

# Split Button

O componente Split Button tem o papel de permitir que o usuário execute uma ação principal ao clicar no botão principal, enquanto também oferece acesso a opções secundárias ou um menu suspenso quando a seta para baixo é clicada. Isso é útil para agrupar funcionalidades relacionadas em um espaço limitado e oferecer uma experiência de usuário mais eficiente.

![Imagem 1: O componente Split Button tem o papel de permitir que o usuário execute uma ação principal ao clicar no botão…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

Utilize o atributo class ou a prop variant para alterar o estado do botão

Os estados dos botões podem ser alterados através da utilização das classes `ez-split-button--primary`, `ez-split-button--secondary` e `ez-split-button--tertiary` ou através da prop `variant` com os valores `primary`, `secondary` e `tertiary`. O estado secundário é o padrão, portanto não precisa ser adicionado.

### Primário

É o botão de maior destaque da tela. Ele orienta a ação principal onde está inserido. Por isso, deve ser usado apenas 1 por bloco.

**Usando a prop variant e classe CSS:**

![Imagem 2: Usando a prop variant e classe CSS:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Secundário

É o botão mais comum e com mais opções de uso.

**Usando a prop variant e classe CSS:**

![Imagem 3: Usando a prop variant e classe CSS:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Terciário

Normalmente acompanha um botão primário e expressa uma ação mais incomum na jornada.

**Usando a prop variant e classe CSS:**

![Imagem 4: Usando a prop variant e classe CSS:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado

![Imagem 5: Habilitado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Existem 2 formas de desabilitar um split button utilizando a prop `isDisabled`.

Quando passamos o valor `isDisabled={"full"}`, temos o disable nativo do HTML, onde o botão fica inacessível, ou seja, não entra na navegação via teclado.

Quando passamos o valor `isDisabled={true}` (recomendado), temos um disable acessível, onde o usuário ainda pode acessar o botão via teclado, mesmo que a interação com ele esteja bloqueada.

![Imagem 6: Quando passamos o valor isDisabled={true} (recomendado), temos um disable acessível, onde o usuário ainda pode acessar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Label

![Imagem 7: Label](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tooltips

No hover, os botões esquerdo e direito apresentam, respectivamente, os valores da própria label e 'Mais opções' como padrão.

![Imagem 8: No hover, os botões esquerdo e direito apresentam, respectivamente, os valores da própria label e 'Mais opções' como…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tooltip personalizado do botão esquerdo

![Imagem 9: Tooltip personalizado do botão esquerdo](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tooltip personalizado do botão direito

![Imagem 10: Tooltip personalizado do botão direito](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Suprimir animação

A animação de ripple do componente pode ser suprimida pela prop `suppressAnimation`.

![Imagem 11: A animação de ripple do componente pode ser suprimida pela prop suppressAnimation .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modos

#### Ícone (icon-only)

![Imagem 12: Ícone (icon-only)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Somente texto (default)

![Imagem 13: Somente texto (default)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícone e texto (icon-left)

![Imagem 14: Ícone e texto (icon-left)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanhos

![Imagem 15: Tamanhos](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones personalizados

#### Ícone esquerdo personalizado

![Imagem 16: Ícone esquerdo personalizado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícone direito personalizado

![Imagem 17: Ícone direito personalizado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Imagens personalizadas

#### Imagem personalizada

![Imagem 18: Imagem personalizada](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Clique no botão principal

![Imagem 19: Clique no botão principal](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Clique em item do dropdown

![Imagem 20: Clique em item do dropdown](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Clique em subação do dropdown

![Imagem 21: Clique em subação do dropdown](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos

### Adicionar foco no botão esquerdo

![Imagem 22: Adicionar foco no botão esquerdo](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adicionar foco no botão direito

![Imagem 23: Adicionar foco no botão direito](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remover foco

![Imagem 24: Remover foco](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alternar dropdown

![Imagem 25: Alternar dropdown](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Verificar se o dropdown está aberto

![Imagem 26: Verificar se o dropdown está aberto](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Overview

Split Button Component

### Properties

| Property Attribute Description Type Default| `enabled` `enabled` ⚠️ [DEPRECATED] Use `isDisabled` prop instead.Se false o usuário não pode interagir com o botão. `boolean` `true`| `iconName` `icon-name` ⚠️ [DEPRECATED] Use `leftIconName` prop instead.Define o ícone a ser usado da biblioteca de ícones: [ez-icons](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/) `string` `undefined`| `image` `image` Define o caminho usado nos modos `icon-only` e `icon-left` para imagens não contempladas na biblioteca de ícones. `string` `undefined`| `isDisabled` `is-disabled` Se verdadeiro o clique no botão fica desabilitado mas a navegação continua funcional. Se full, o usuário não pode interagir com o botão. `"" | "full" | boolean` `false`| `itemBuilder` -- Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. `(item: IDropdownItem, level: number) => string | HTMLElement` `undefined`| `items` -- Define o conteúdo do dropdown. `IDropdownItem[]` `undefined`| `label` `label` Texto a ser apresentado como label do botão. `string` `undefined`| `leftIconName` `left-icon-name` Define o ícone esquerdo a ser usado da biblioteca de ícones: [ez-icons](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/) `string` `undefined`| `leftTitle` `left-title` Texto a ser apresentado como title do botão principal `string` `undefined`| `mode` `mode` Define o modo de uso do botão. `"default" | "icon-left" | "icon-only"` `'default'`| `rightIconName` `right-icon-name` Define o ícone direito a ser usado da biblioteca de ícones: [ez-icons](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/) `string` `undefined`| `rightTitle` `right-title` Texto a ser apresentado como title do botão dropdown `string` `undefined`| `show` `show` Se true, o dropdown do botão é exibido. `boolean` `false`| `size` `size` Define o tamanho do ez-split-button. `"large" | "medium" | "small"` `'medium'`| `suppressAnimation` `suppress-animation` Se verdadeiro, desabilita a animação de ripple. `boolean` `false`| `variant` `variant` Define a variante do ez-split-button. `"primary" | "secondary" | "tertiary"` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `buttonClick` Emitido quando o botão principal é clicado `CustomEvent<void>`| `dropdownItemClick` Emitido quando um item do dropdown é clicado `CustomEvent<IDropdownItem>`| `dropdownSubActionClick` Emitido quando uma subAction de um item do dropdown é clicada `CustomEvent<IDropdownSubAction>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `isOpenedDropdown() => Promise<boolean>`

Informa se a lista de ações está aberta.

##### Returns

Type: `Promise<boolean>`

---

#### `setBlur() => Promise<void>`

Remove o foco de ambos os botões.

##### Returns

Type: `Promise<void>`

---

#### `setLeftButtonFocus() => Promise<void>`

Aplica o foco no botão principal.

##### Returns

Type: `Promise<void>`

---

#### `setRightButtonFocus() => Promise<void>`

Aplica o foco no botão do dropdown.

##### Returns

Type: `Promise<void>`

---

#### `toggleDropdown() => Promise<void>`

Abre ou Fecha o dropdown do Split Button.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-dropdown](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown)

#### Graph

```
graph TD;
  ez-split-button --> ez-icon
  ez-split-button --> ez-dropdown
  ez-dropdown --> ez-skeleton
  ez-dropdown --> ez-icon
  style ez-split-button fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-split-button--min-width Define a largura mínima do componente.| --ez-split-button--width Define a largura do componente.| --ez-split-button--height Define a altura do componente, quando size medium.| --ez-split-button\_\_medium-icon--width Define a largura do slot que contém o ícone.| --ez-split-button\_\_large-icon--width Define a largura do slot que contém o ícone.| --ez-split-button\_\_label--padding-top Define o espaçamento superior ao label.| --ez-split-button\_\_label--padding-bottom Define o espaçamento inferior ao label.| --ez-split-button\_\_right-button--padding-left Define o espaçamento esquerdo ao ícone.| --ez-split-button\_\_right-button--padding-right Define o espaçamento direito ao ícone.| --ez-split-button--color Define a cor do label.| --ez-split-button\_\_left-icon--color Define a cor do ícone esquerdo.| --ez-split-button\_\_right-icon--color Define a cor do ícone direito.| --ez-split-button--background-color Define a cor de fundo do botão.| --ez-split-button--border Define o estilo da borda do botão.| --ez-split-button--font-size Define o tamanho do label.| --ez-split-button--line-height Define a altura da linha do label.| --ez-split-button--font-family Define a família da fonte do label.| --ez-split-button--font-weight Define o peso da fonte do label.| --ez-split-button--border-radius Define o raio da borda do botão.| --ez-split-button--hover-color Define a cor do texto e do ícone quando o cursor está sobre o botão.| --ez-split-button--hover--background-color Define a cor de fundo quando o cursor está sobre o botão.| --ez-split-button--disabled-color Define a cor do texto quando o botão está desabilitado.| --ez-split-button--disabled--background-color Define a cor de fundo quando o botão está desabilitado.| --ez-split-button--focus--border Define o estido da borda quando o botão está selecionado.| --ez-split-button--focus--box-shadow Define a sombra do botão quando selecionado. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
