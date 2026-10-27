---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator/"
titulo: "Sidebar Navigator"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator/"
trilha: "Docs > Components > Components Doc > Ez Sidebar Navigator"
---

# Sidebar Navigator

O **Sidebar Navigator** é um componente de navegação lateral que pode funcionar de três maneiras: flutuante, fixo ou dinâmico.

O comportamento do menu pode ser configurado para abrir ao passar o mouse sobre o **SidebarButton** (modo flutuante) ou ao clicar nele (modo fixo). No modo dinâmico (padrão), o menu começa como flutuante, mas pode ser fixado conforme o desejo do usuário.

![Imagem 1: O comportamento do menu pode ser configurado para abrir ao passar o mouse sobre o SidebarButton (modo flutuante) ou ao…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Propriedades (Props)

### `type`

- Tipo: `TypeMenuEnum`
- Padrão: `'dynamic'`
  Define o comportamento do menu:
- **`float`**: O menu é aberto ao passar o mouse sobre o **SidebarButton**.
- **`fixed`**: O menu é fixo e precisa ser aberto/fechado manualmente ao clicar no **SidebarButton**.
- **`dynamic`** (padrão): Inicia no modo flutuante, mas pode ser fixado pelo usuário.

### `mode`

- Tipo: `ModeMenuEnum`
- Padrão: `'float'`

Define o modo inicial do menu: `'float'` ou `'fixed'`.

### `size`

- Tipo: `SizeMenuEnum`
- Padrão: `'small'`

Controla a largura do menu, com três opções:

- **`small`**: 240px de largura.
- **`medium`**: 280px de largura.
- **`large`**: 320px de largura.

Por padrão o componente utiliza a altura total da tela, mas é possível definir uma altura fixa utilizando a variavel de estilo `--ez-sidebar-navigator--height`

### `isResponsive`

- Tipo: `boolean`
- Padrão: `false`

Define se a largura do menu é ajustada automaticamente com base no tamanho da tela:

- **Até 768px**: utiliza o tamanho `small`.
- **Até 992px**: utiliza o tamanho `medium`.
- **Acima de 1200px**: utiliza o tamanho `large`.

### `titleMenu`

- Tipo: `string`

Define o título do **Sidebar Navigator**. Se não for especificado, o conteúdo ocupará o espaço do título.

### `showCollapseMenu`

- Tipo: `boolean`
- Padrão: `true`

Permite ocultar o botão de recolher o menu.

### `showFixedButton`

- Tipo: `boolean`
- Padrão: `true`

Permite ocultar o botão que fixa o menu no modo dinâmico.

![Imagem 2: Permite ocultar o botão que fixa o menu no modo dinâmico.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Slots

O **Sidebar Navigator** disponibiliza os seguintes slots para personalização:

- **start**: Conteúdo no início do cabeçalho.
- **content**: Espaço principal no cabeçalho. Se o `titleMenu` for definido, o conteúdo desse slot será posicionado abaixo do título.
- **end**: Conteúdo no final do cabeçalho.
- **footer**: Conteúdo do rodapé do menu.

![Imagem 3: footer : Conteúdo do rodapé do menu.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

Quando há uma mudança de modo entre `fixed` e `float`, é emitido um evento contendo o novo modo selecionado.

![Imagem 4: Quando há uma mudança de modo entre fixed e float , é emitido um evento contendo o novo modo selecionado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### `openSidebar()`

Abre o menu programaticamente.

### `closeSidebar()`

Fecha o menu programaticamente.

### `changeModeMenu()`

Alterna entre os modos fixo e flutuante. Este método só funciona quando o `type` do componente for `dynamic`.

![Imagem 5: Alterna entre os modos fixo e flutuante. Este método só funciona quando o type do componente for dynamic .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Tipos de Comportamento

### Fixo

O menu já começa aberto e ocupa um espaço fixo na tela. Ao ser fechado, é necessário clicar no **SidebarButton** para reabri-lo.

Para usar esse comportamento, defina a propriedade `type` como `'fixed'`.

![Imagem 6: Para usar esse comportamento, defina a propriedade type como 'fixed' .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Flutuante

O menu inicia fechado e é exibido ao passar o mouse sobre o **SidebarButton**. Quando o mouse sai do componente, o menu é ocultado novamente. O menu não ocupa espaço na tela enquanto está oculto.

Para usar esse comportamento, defina a propriedade `type` como `'float'`.

![Imagem 7: Para usar esse comportamento, defina a propriedade type como 'float' .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Dinâmico

Esse é o comportamento padrão, onde o menu começa no modo flutuante, mas pode ser fixado pelo usuário clicando em um botão no cabeçalho.

Para usar o modo dinâmico explicitamente, defina a propriedade `type` como `'dynamic'`.

![Imagem 8: Para usar o modo dinâmico explicitamente, defina a propriedade type como 'dynamic' .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `isResponsive` `is-responsive` Define se terá responsividade, Controle deverá ser pelo CSS. `boolean` `false`| `mode` `mode` Define se o menu será do tipo FIXED ou FLOAT. `ModeMenuEnum.FIXED | ModeMenuEnum.FLOAT` `ModeMenuEnum.FLOAT`| `showCollapseMenu` `show-collapse-menu` Define se o botão de "Recolher Menu" será exibido `boolean` `true`| `showFixedButton` `show-fixed-button` Define se o botão de "Fixar Menu" será exibido `boolean` `true`| `size` `size` Define o tamanho do menu (small, medium, large). `SizeMenuEnum.LARGE | SizeMenuEnum.MEDIUM | SizeMenuEnum.SMALL` `SizeMenuEnum.SMALL`| `titleMenu` `title-menu` Define o título do Sidebar Navigator `string` `""`| `type` `type` Define o tipo do menu (float, fixed ou dynamic (livre)). `TypeMenuEnum.DYNAMIC | TypeMenuEnum.FIXED | TypeMenuEnum.FLOAT` `TypeMenuEnum.DYNAMIC` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChangeMode` Evento emitido sempre que o modo (FLOAT ou FIXED) do menu for alterado.. `CustomEvent<ModeMenuEnum.FIXED | ModeMenuEnum.FLOAT>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `changeModeMenu() => Promise<void>`

Método para fixar/desafixar o menu, emitindo o evento ezChangeMode.

##### Returns

Type: `Promise<void>`

---

#### `closeSidebar() => Promise<void>`

Método para fechar o menu automaticamente após uma ação, fluxo, etc.

##### Returns

Type: `Promise<void>`

---

#### `openSidebar() => Promise<void>`

Método para abrir o menu automaticamente após uma ação, fluxo, etc.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-sidebar-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-button)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [ez-scroller](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scroller)

#### Graph

```
graph TD;
  ez-sidebar-navigator --> ez-sidebar-button
  ez-sidebar-navigator --> ez-button
  ez-sidebar-navigator --> ez-scroller
  ez-sidebar-button --> ez-icon
  ez-button --> ez-icon
  style ez-sidebar-navigator fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-sidebar-navigator--padding-left Define o espaçamento da esquerda do container| --ez-sidebar-navigator--padding-right Define o espaçamento da direita do container| --ez-sidebar-navigator--gap Define o espaçamento entre o cabeçalho conteúdo e rodapé| --ez-sidebar-navigator--box-shadow Define a cor de shadow box do container de label| --ez-sidebar-navigator--background-color Define a cor de fundo do container de label| --ez-sidebar-navigator--border-radius Define o border radius do container de label| --ez-sidebar-navigator--height Força uma altura especifica para o sidebar, o padrão é 100% da tela| --ez-sidebar-navigator--z-index Define a camada em que o componente será exibido.| --ez-sidebar-navigator--header-gap Define o espaçamento entre os componente do cabeçalho| --ez-sidebar-navigator--footer-gap Define o espaçamento entre os componente do rodadé| --ez-ez-sidebar-navigator\_\_title--font-family Define a fonte do título do componente| --ez-ez-sidebar-navigator\_\_title--font-size Define o tamanho da fonte do título do componente.| --ez-ez-sidebar-navigator\_\_title--color Define a cor da fonte do título do componente.| --ez-ez-sidebar-navigator\_\_title--font-weight Define o peso da fonte do título do componente. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
