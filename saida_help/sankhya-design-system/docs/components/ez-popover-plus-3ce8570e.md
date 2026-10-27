---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/"
titulo: "Popover Plus"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/"
trilha: "Docs > Components > Components Doc > Ez Popover Plus"
---

# Popover Plus

O Popover é um componente utilizado para exibir informações contextuais em uma sobreposição leve e discreta em relação
ao conteúdo principal. Ele pode conter texto, botões ou outros elementos interativos e geralmente é ativado por ações
do usuário, como clique ou foco.

Atenção

Caso o conteúdo do componente tenha arquivos de estilização próprios, é necessário que o conteúdo seja separado em um
componente individual antes de ser utilizado.

![Imagem 1: Caso o conteúdo do componente tenha arquivos de estilização próprios, é necessário que o conteúdo seja separado em um…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Controle de exibição

O componente possui três métodos principais:

- `show()`: Exibe o popover.
- `showUnder(elemento)`: Exibe o popover abaixo do elemento especificado.
- `hide()`: Oculta o popover.

E uma propriedade de controle:

- `opened`: Controla o estado de visibilidade do componente.

Além disso, caso o usuário clique em algum lugar fora do conteúdo o faz ocultar automaticamente. Isso pode ser
desligado pela flag "autoClose".

Observação

É necessário definir o parâmetro `overlayType` com valor **none**.
Uma vez que, tendo o `overlayType` ligado o `autoClose` por regra também será ligado.

![Imagem 2: É necessário definir o parâmetro overlayType com valor none . Uma vez que, tendo o overlayType ligado o autoClose por…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Ancoragem de elementos

Para um bom funcionamento do componente, é necessário termos definido um elemento de ancoragem. Para isso, temos
algumas estratégias.

### Método showUnder

Este método simplifica o processo de abertura ao permitir a passagem do elemento de ancoragem no momento da
exibição do Popover. Isso elimina a necessidade de configurar previamente o componente. Como o elemento de
ancoragem só é utilizado no momento da abertura, essa abordagem resolve problemas relacionados à falta de
referência durante a renderização inicial e é a **estratégia recomendada**.

[Exemplo](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/#showunder)

### Propriedade anchorElement

Esta propriedade permite especificar o elemento que serve como ponto de referência para o posicionamento do Popover.
Ela pode ser configurada com uma referência ao elemento (HTMLElement), com seu identificador único (string) ou com
um array contendo múltiplos elementos ou IDs. Quando um array é usado, o Popover será posicionado em relação ao primeiro
elemento válido encontrado na lista. Isso é útil para cenários onde múltiplos pontos de ancoragem são possíveis.

### Método setAnchorElement

Este método permite configurar o elemento de referência para o posicionamento do Popover. Sendo necessário ser feito antes
do momento de abertura do componente, se tornando uma estratégia para casos onde o elemento de ancoragem são renderizados de
forma condicional por exemplo.

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

## Métodos

### show()

- Exibe o Popover.
- **Parâmetros:**
  - `x` (número | string | undefined): Valor de deslocamento horizontal.
  - `y` (número | string | undefined): Valor de deslocamento vertical.
- Exemplo de uso:

  ```
  popover.show();
  popover.show(10, 10);
  popover.show("10px", "10px");
  ```

### showUnder()

- Exibe o Popover abaixo de um elemento de ancoragem.
- **Parâmetros:**
  - `element` (HTMLElement | string): Elemento de referência para o posicionamento no popover, podendo ser o elemento diretamente ou um id.
  - `options` (IEzPopoverAnchorOptions): Objeto de configurações:
    - `horizontalGap` (number | undefined): Valor de deslocamento horizontal.
    - `verticalGap` (number | undefined): Valor de deslocamento vertical.
    - `fromRight` (boolean | undefined): Caso verdadeiro, o componente será mostrado da direito para esquerda.
- Exemplo de uso:

  ```
  popover.showUnder(button);
  popover.showUnder(button, { horizontalGap: 10, verticalGap: 10 });
  popover.showUnder(button, { fromRight: true });
  ```

### hide()

- Fecha o Popover.
- Exemplo de uso:

  ```
  popover.hide();
  ```

### setOptions()

- Altera as configurações de deslocamento e ponto de partida.
- **Parâmetros:**
  - `options` (IEzPopoverAnchorOptions): Objeto de configurações:
    - `horizontalGap` (number | undefined): Valor de deslocamento horizontal.
    - `verticalGap` (number | undefined): Valor de deslocamento vertical.
    - `fromRight` (boolean | undefined): Caso verdadeiro, o componente será mostrado da direito para esquerda.
- Exemplo de uso:

  ```
  popover.setOptions({ verticalGap: 5 });
  popover.setOptions({ horizontalGap: 10, verticalGap: 10 });
  popover.setOptions({ fromRight: true });
  ```

### setAnchorElement()

- Altera o elemento de ancoragem.
- **Parâmetros:**
  - `element` (HTMLElement | string): Elemento de referência para o posicionamento no popover, podendo ser o elemento diretamente ou um id.
- Exemplo de uso:

  ```
  popover.setAnchorElement(button);
  popover.setAnchorElement("text_input_id");
  ```

### updatePosition()

- Altera o deslocamento do componente.
- **Parâmetros:**
  - `x` (número | string | undefined): Valor de deslocamento horizontal.
  - `y` (número | string | undefined): Valor de deslocamento vertical.
- Exemplo de uso:

  ```
  popover.updatePosition(5, 5);
  popover.updatePosition("10px", "10px");
  ```

## Propriedades

### autoClose

- Define se será fechado automaticamente quando o usuário clicar fora do conteúdo.
- Tipo: boolean.
- Valor padrão: true.

### boxWidth

- Ajusta o comportamento da largura do popover.
- Tipo: string.
- Valores possíveis: fit-content (ajusta ao conteúdo) ou full-width (largura máxima).
- Valor padrão: fit-content.

### opened

- Define se o popover está visível ou oculto.
- Tipo: boolean.
- Valores possíveis: true (visível) ou false (oculto).
- Valor padrão: false.

### overlayType

- Define o tipo de overlay do popover.
- Tipo: string.
- Valores possíveis: medium, light ou none (desabilitado).
- Valor padrão: light.

### anchorElement

- Define o elemento de ancoragem. O elemento de ancoragem pode ser passado por uma
  lista de elementos ou ids, neste caso, será priorizado os elementos de indices menores.
- Tipo: Array<HTMLElement | string> | HTMLElement | string.
- Valor padrão: undefined.

### options

- Define as opções do elemento.
- Tipo (objeto com as seguintes propriedades):
  - horizontalGap: number (deslocamento horizontal).
  - verticalGap: number (deslocamento vertical).
  - fromRight: boolean (Caso verdadeiro, o componente será mostrado da direito para esquerda).
- Valor padrão: **`{ horizontalGap: 0, verticalGap: 0, fromRight: false }`**.

### useAnchorSize

- Define se o elemento manterá o mesmo tamanho do componente de ancora.
- Tipo: boolean.
- Valor padrão: false.

### minWidth

- Define a largura mínima do elemento (apenas será considerada caso a propriedade useAnchorSize seja verdadeira).
- Tipo: number.
- Valor padrão: 150.

## API do componente

### Properties

| Property Attribute Description Type Default| `anchorElement` `anchor-element` Define o elemento de ancoragem. `(string | HTMLElement)[] | HTMLElement | string` `undefined`| `autoClose` `auto-close` Define que será fechado automaticamente quando o usuário clicar fora do conteúdo. `boolean` `true`| `boxWidth` `box-width` Ajusta o comportamento da largura do popover. `"fit-content" | "full-width"` `"fit-content"`| `fitInViewport` `fit-in-viewport` Define se o popover deve se ajustar ao espaço visível disponível para não ser cortado pelas bordas da tela (ou por containers com rolagem). Quando verdadeiro, o conteúdo passa a rolar internamente em vez de ficar com parte oculta. Padrão: true. `boolean` `true`| `minWidth` `min-width` Define a largura mínima do elemento (apenas será considerada caso a propriedade useAnchorSize seja verdadeira). `number` `150`| `opened` `opened` Define se o ez-popover está aberto. `boolean` `false`| `options` -- Define as opções do elemento. `IEzPopoverAnchorOptions` `{ horizontalGap: 0, verticalGap: 0, fromRight: false }`| `overlayType` `overlay-type` Define o tipo de overlay do popover. `"light" | "medium" | "none"` `"light"`| `useAnchorSize` `use-anchor-size` Define se o elemento manterá o mesmo tamanho do componente de ancora. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezVisibilityChange` Emitido quando acontece a alteração de estado do componente. `CustomEvent<boolean>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `hide() => Promise<void>`

Oculta o ez-popover.

##### Returns

Type: `Promise<void>`

---

#### `setAnchorElement(anchor: HTMLElement | string) => Promise<void>`

Altera o elemento de ancoragem.

##### Returns

Type: `Promise<void>`

---

#### `setOptions(options: IEzPopoverAnchorOptions) => Promise<void>`

Altera as opções.

##### Returns

Type: `Promise<void>`

---

#### `show(top?: string | number, left?: string | number) => Promise<void>`

Exibe o ez-popover.

##### Returns

Type: `Promise<void>`

---

#### `showUnder(element: HTMLElement | string, options?: IEzPopoverAnchorOptions) => Promise<void>`

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

- [ez-combo-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-combo-box)
- [ez-date-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input)
- [ez-date-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-time-input)
- [ez-search](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search)
- [ez-search-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus)
- [filter-column](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-grid/subcomponents)

#### Depends on

- [ez-popover-core](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus/subcomponent)

#### Graph

```
graph TD;
  ez-popover-plus --> ez-popover-core
  ez-combo-box --> ez-popover-plus
  ez-date-input --> ez-popover-plus
  ez-date-time-input --> ez-popover-plus
  ez-search --> ez-popover-plus
  ez-search-plus --> ez-popover-plus
  filter-column --> ez-popover-plus
  style ez-popover-plus fill:#f9f,stroke:#333,stroke-width:4px
```

---
