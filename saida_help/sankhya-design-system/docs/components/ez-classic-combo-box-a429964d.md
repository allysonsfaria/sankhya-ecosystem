---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-combo-box/"
titulo: "Classic Combo Box"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-combo-box/"
trilha: "Docs > Components > Components Doc > Ez Classic Combo Box"
---

# Classic Combo Box

O **Classic Combo Box** é um componente de seleção que permite aos usuários escolher uma ou mais opções de uma lista suspensa. Oferece funcionalidades como busca, ícones personalizáveis, diferentes estados visuais e slots customizáveis para renderização personalizada das opções.

![Imagem 1: O Classic Combo Box é um componente de seleção que permite aos usuários escolher uma ou mais opções de uma lista…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Estados Visuais

O Classic Combo Box suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

![Imagem 2: O Classic Combo Box suporta diferentes estados visuais que podem ser definidos pela propriedade state .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones

É possível adicionar ícones ao combo box para melhorar a experiência visual e funcional.

![Imagem 3: É possível adicionar ícones ao combo box para melhorar a experiência visual e funcional.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Funcionalidade de Busca

O componente oferece suporte à funcionalidade de busca para filtrar opções dinamicamente.

![Imagem 4: O componente oferece suporte à funcionalidade de busca para filtrar opções dinamicamente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Estados de Interação

Controle sobre estados desabilitado e somente leitura.

![Imagem 5: Controle sobre estados desabilitado e somente leitura.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Slots Customizados

O Classic Combo Box permite personalizar completamente a renderização das opções através de slots.
Isso possibilita criar listas ricas com informações adicionais, imagens, ícones coloridos e layouts complexos.

Os slots customizados permitem:

- **Informações do usuário**: Avatar, status online, função e contato
- **Detalhes do produto**: Imagem, preço, categoria, avaliação e disponibilidade
- **Status coloridos**: Ícones, descrições e cores específicas para cada estado
- **Layouts complexos**: Múltiplas linhas de informação e elementos visuais

Atenção

Quando utilizar slots customizados, as funcionalidades de busca e navegação por teclado não estarão disponíveis.
Para manter a usabilidade, é recomendado implementar uma lógica de busca personalizada se necessário, para isto
explore o evento `ezType` para capturar as mudanças no input. Para navegação por teclado,
poderá ser utilizado o utilitário `KeyboardManager` para gerenciar os eventos de teclado.

![Imagem 6: Quando utilizar slots customizados, as funcionalidades de busca e navegação por teclado não estarão disponíveis. Para…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Evento ezChange

Disparado sempre que uma opção é selecionada ou desselecionada.

![Imagem 7: Disparado sempre que uma opção é selecionada ou desselecionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento ezBlur

Disparado quando o combo box perde o foco.

![Imagem 8: Disparado quando o combo box perde o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

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

### open e close

Métodos para abrir e fechar programaticamente a lista de opções.

Dica

Os métodos `showPopover()` e `hidePopover()`
permitem controlar programaticamente a visibilidade da lista de opções do combo box.
Isso é útil para criar interações personalizadas ou automações específicas.

![Imagem 11: Os métodos showPopover() e hidePopover() permitem controlar programaticamente a visibilidade da lista de opções do…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enabled` `enabled` Define se o combo box está habilitado. `boolean` `true`| `helpText` `help-text` Texto de ajuda exibido abaixo do combo box. `string` `undefined`| `iconClickable` `icon-clickable` Define se o ícone é clicável `boolean` `false`| `iconName` `icon-name` Nome do ícone. `string` `undefined`| `label` `label` Texto do label exibido acima do combo box. `string` `undefined`| `name` `name` Nome do combo box. `string` `undefined`| `options` -- Array com as opções do ez-classic-combo-box. Os elementos devem obedecer o formato: `{value: string, label: string}`. `IOption[]` `undefined`| `placeholder` `placeholder` Placeholder do combo box `string` `undefined`| `readonly` `readonly` Define se o combo box é somente leitura. `boolean` `false`| `state` `state` Estado visual do combo box: default, error, success ou warning. `"default" | "error" | "success" | "warning"` `"default"`| `suppressEmptyOption` `suppress-empty-option` Se true remove a opção vazia da lista. `boolean` `false`| `suppressSearch` `suppress-search` Se true desabilita a digitação dentro do componente. `boolean` `false`| `textEmptyOption` `text-empty-option` Texto a ser apresentado na opção de valor nulo. `string` `undefined`| `titleIcon` `title-icon` Título do ícone (tooltip). `string` `undefined`| `value` -- Valor do combo box. `IOption` `null` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezBlur` Evento disparado quando o combo box perde o foco. `CustomEvent<IOption>`| `ezChange` Evento disparado quando o valor do combo box muda. `CustomEvent<IOption>`| `ezType` Emitido quando é digitado no campo de entrada. `CustomEvent<string>`| `ezVisibilityChange` Emitido quando acontece a alteração de estado do popover. `CustomEvent<boolean>`| `iconClick` Evento disparado quando o ícone é clicado. `CustomEvent<void>` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `hidePopover() => Promise<void>`

Oculta o popover.

##### Returns

Type: `Promise<void>`

---

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

---

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

---

#### `setValue(option: IOption) => Promise<void>`

##### Returns

Type: `Promise<void>`

---

#### `showPopover() => Promise<void>`

Exibe o popover abaixo do input.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-classic-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-classic-input)
- [ez-popover-core](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/subcomponent)

#### Graph

```
graph TD;
  ez-classic-combo-box --> ez-classic-input
  ez-classic-combo-box --> ez-popover-core
  ez-classic-input --> ez-icon
  style ez-classic-combo-box fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-classic-combo-box-highlighted-bg-color Define a cor da seleção do item.| --ez-classic-combo-box-max-height Define a altura máxima do container da lista de opções.| --ez-classic-combo-box-list-bg-color Define a cor de fundo da lista de opções.| --ez-classic-combo-box-item-hover-bg-color Define a cor de fundo do item em hover.| --ez-classic-combo-box-selected-bg-color Define a cor de fundo do item selecionado.| --ez-classic-combo-box-selected-text-color Define a cor do texto do item selecionado.| --ez-classic-combo-box-selected-font-weight Define o peso da fonte do item selecionado.| --ez-classic-combo-box-item-padding Define o padding interno dos itens da lista.| --ez-classic-combo-box-item-border-radius Define o border-radius dos itens da lista.| --ez-classic-combo-box-list-margin Define a margem da lista de opções.| --ez-classic-combo-box-transition-duration Define a duração da transição dos itens.| --ez-classic-combo-box-scrollbar-color Define a cor da scrollbar.| --ez-classic-combo-box-no-results-margin Define a margem do texto "sem resultados".| --ez-classic-combo-box-item-text-color Define a cor do texto dos itens.| --ez-classic-combo-box-item-min-height Define a altura mínima dos itens da lista. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
