---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button/"
titulo: "Button"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button/"
trilha: "Docs > Components > Components Doc > Ez Button"
---

# Button

Botões são usados para inicializar uma ação. Os rótulos dos botões expressam qual ação ocorrerá quando o usuário interagir com eles.
Use botões para comunicar as ações que os usuários podem realizar e para permitir que os usuários interajam com a página.

![Imagem 1: Botões são usados para inicializar uma ação. Os rótulos dos botões expressam qual ação ocorrerá quando o usuário…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Variantes

Utilize o atributo class ou a prop variant para mudar o estado do botão

O estado dos botões podem ser alterados através da utilização das classes `ez-button--primary` e `ez-button--tertiary`. O estado secundário é o default, logo não precisa ser adicionado.

A prop variant também pode ser utilizada com a mesma finalidade, recebendo os valores `primary`, `secondary` ou `tertiary`

![Imagem 2: A prop variant também pode ser utilizada com a mesma finalidade, recebendo os valores primary , secondary ou tertiary](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Primário.

É o botão de maior destaque da tela. Ele orienta a ação principal onde está inserido. Por isso, deve ser usado apenas 1 por bloco.

![Imagem 3: É o botão de maior destaque da tela. Ele orienta a ação principal onde está inserido. Por isso, deve ser usado apenas 1…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Secundário.

É o botão mais comum e com mais opções de uso.

![Imagem 4: É o botão mais comum e com mais opções de uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Terciário.

Normalmente acompanhado de um botão primário e expressa uma ação mais incomum na jornada.

![Imagem 5: Normalmente acompanhado de um botão primário e expressa uma ação mais incomum na jornada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado.

Prop descontinuada

A prop `enabled` está sendo descontinuada, recomendamos a utilização da prop `isDisabled` com suporte a melhorias de acessibilidade.

![Imagem 6: A prop enabled está sendo descontinuada, recomendamos a utilização da prop isDisabled com suporte a melhorias de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado.

Existem 2 formas de se desabilitar um botão utilizando a prop `isDisabled`.

Quando passamos o valor `isDisabled={"full"}` temos o disable nativo do HTML, onde o botão fica inacessível, ou seja, não entra na navegação via teclado.

Quando passamos o valor `isDisabled={true}`(recomendado) temos um disable acessível, onde o usuário ainda pode acessar o botão via teclado, mesmo que a
interação com o mesmo esteja bloqueada.

![Imagem 7: Quando passamos o valor isDisabled={true} (recomendado) temos um disable acessível, onde o usuário ainda pode acessar o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Suprimir animação.

A animação de ripple do componente pode ser suprimida pela prop `suppressAnimation`

![Imagem 8: A animação de ripple do componente pode ser suprimida pela prop suppressAnimation](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Label.

![Imagem 9: Label.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modos.

#### Link.

![Imagem 10: Link.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícone.

![Imagem 11: Ícone.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícone e texto.

![Imagem 12: Ícone e texto.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícone na esquerda, direita e texto.

![Imagem 13: Ícone na esquerda, direita e texto.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanhos.

![Imagem 14: Tamanhos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

### Adicionar foco.

![Imagem 15: Adicionar foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remover foco.

![Imagem 16: Remover foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enabled` `enabled` ⚠️ [DEPRECATED] Use `isDisabled` prop instead.Se false o usuário não pode interagir com o botão. `boolean` `true`| `iconName` `icon-name` Define o ícone a ser usado da biblioteca de ícones: [ez-icons](https://sankhyalabs-storybook.herokuapp.com/themes/default/icons/fonts/index.html) `string` `undefined`| `image` `image` Define o caminho usado nos modos `icon` e `label-icon` para imagens não contempladas na biblioteca de ícones. `string` `undefined`| `isDisabled` `is-disabled` Se verdadeiro o clique no botão fica desabilitado mas a navegação continua funcional. Se full, o usuário não pode interagir com o botão. `"" | "full" | boolean` `false`| `label` `label` Texto a ser apresentado como título do botão. `string` `undefined`| `leftIconName` `left-icon-name` Define o ícone esquerdo do ez-button. Tem prioridade sobre o slot `leftIcon`. `string` `undefined`| `mode` `mode` Define o modo de uso do botão. `"icon" | "label-icon" | "link" | "regular"` `"regular"`| `rightIconName` `right-icon-name` Define o ícone direto do ez-button. Tem prioridade sobre o slot `rightIcon`. `string` `undefined`| `size` `size` Define o tamanho do ez-button. `"large" | "medium" | "small" | "x-small"` `"medium"`| `suppressAnimation` `suppress-animation` Se verdadeiro, desabilita a animação de ripple. `boolean` `false`| `type` `type` Define o tipo do botão. Pode ser `button`, `submit` ou `reset`. `string` `"button"`| `variant` `variant` Define a variante do ez-button. `"primary" | "secondary" | "tertiary"` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `setBlur() => Promise<void>`

Remove o foco do botão.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Aplica o foco no botão.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-actions-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-actions-button)
- [ez-alert-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert-list)
- [ez-dialog](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dialog)
- [ez-double-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-double-list)
- [ez-filter](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter)
- [ez-grid](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid)
- [ez-guide-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator)
- [ez-modal-container](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal-container)
- [ez-pagination](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-pagination)
- [ez-popup](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popup)
- [ez-sidebar-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator)
- [ez-split-item](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-panel/structure/item)
- [ez-text-edit](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit)
- [ez-tile-medium](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile-medium)
- [filter-column](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/subcomponents)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-button --> ez-icon
  ez-actions-button --> ez-button
  ez-alert-list --> ez-button
  ez-dialog --> ez-button
  ez-double-list --> ez-button
  ez-filter --> ez-button
  ez-grid --> ez-button
  ez-guide-navigator --> ez-button
  ez-modal-container --> ez-button
  ez-pagination --> ez-button
  ez-popup --> ez-button
  ez-sidebar-navigator --> ez-button
  ez-split-item --> ez-button
  ez-text-edit --> ez-button
  ez-tile-medium --> ez-button
  filter-column --> ez-button
  style ez-button fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-button--min-width Define a largura mínima do componente.| --ez-button--width Define a largura do componente.| --ez-button--height Define a altura do componente.| --ez-button--padding-top Define o espaçamento superior ao label.| --ez-button--padding-bottom Define o espaçamento inferior ao label.| --ez-button--padding-right Define o espaçamento à direita do label.| --ez-button--padding-left Define o espaçamento à esquerda do label.| --ez-button--icon--gap Define o gap entre o texto e ícone, quando existir.| --ez-button--color Define a cor do label.| --ez-button--label-icon--color Define a cor do label do botao tipo label-icon.| --ez-button--label-icon--hover-color Define a cor do label do botao tipo label-icon, quando o mouse sobre o botão.| --ez-button--label-icon--disabled-color Define a cor do label do botao tipo label-icon, quando desabilitado.| --ez-button--left-icon--color Define a cor do icone esquerdo.| --ez-button--right-icon--color Define a cor do icone direito, quando o mouse está sobre o botão.| --ez-button--left-icon--hover-color Define a cor do icone esquerdo.| --ez-button--right-icon--hover-color Define a cor do icone direito, quando o mouse está sobre o botão.| --ez-button--left-icon--disabled-color Define a cor do icone esquerdo, quando desabilitado.| --ez-button--right-icon--disabled-color Define a cor do icone direito, quando desabilitado.| --ez-button--font-size Define o tamanho do label.| --ez-button--font-family Define a família da fonte do label.| --ez-button--font-weight Define o peso da fonte do label.| --ez-button--background-color Define a cor de fundo do botão.| --ez-button--border-radius Define o raio da borda do botão.| --ez-button--border Define o estilo da borda do botão.| --ez-button--hover--border Define o estilo da borda do botão quando em hover.| --ez-button--justify-content Define o alinhamento horizontal do conteúdo do botão.| --ez-button--hover-color Define a cor do texto e do ícone quando o cursor está sobre o botão.| --ez-button--hover--background-color Define a cor de fundo quando o cursor está sobre o botão.| --ez-button--disabled-color Define a cor do texto quando o botão está desabilitado.| --ez-button--disabled--background-color Define a cor de fundo quando o botão está desabilitado.| --ez-button--disabled--border Define a cor da borda quando o botão está desabilitado.| --ez-button--disabled-icon-color Define a cor do icone quando o botão está desabilitado.| --ez-button--link-color Define a cor do texto do botão no modo link.| --ez-button--link--hover-color Define a cor do texto do botão no hover do modo link.| --ez-button--link-disabled-color Define a cor do texto do botão no hover do modo link, quando desabilitado.| --ez-button--link--small--font-size Define o tamanho small na fonte do texto do botão no modo link.| --ez-button--link--medium--font-size Define o tamanho medium na fonte do texto do botão no modo link.| --ez-button--link--large--font-size Define o tamanho large na fonte do texto do botão no modo link. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
