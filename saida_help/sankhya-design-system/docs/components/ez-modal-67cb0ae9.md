---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal/"
titulo: "Modal"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal/"
trilha: "Docs > Components > Components Doc > Ez Modal"
---

# Modal

![Imagem 1: Modal](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Altura do Modal

A propriedade `heightMode` controla o comportamento de altura do Modal, permitindo definir o modo `regular` ou `full`. O modo `regular` possui altura padrão para conteúdo compacto, enquanto o modo `full` expande o Modal verticalmente, ocupando todo o espaço disponível na tela.

![Imagem 2: A propriedade heightMode controla o comportamento de altura do Modal, permitindo definir o modo regular ou full . O…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Tamanho ocupado

A prop `modalSize` define o tamanho do componente ez-modal, permitindo especificar o tamanho desejado seguindo o grid-layout. Desse modo, é possível utilizar classes de dimensionamento, como `col-sd-3`, para determinar o tamanho do modal.

![Imagem 3: A prop modalSize define o tamanho do componente ez-modal, permitindo especificar o tamanho desejado seguindo o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Scrim

A prop `scrim` define o tipo de overlay a ser aplicado no backdrop do modal, podendo alterar entre `medium` ou `light`.

![Imagem 4: A prop scrim define o tipo de overlay a ser aplicado no backdrop do modal, podendo alterar entre medium ou light .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Fechamento automático

Existem duas opções para fechar o modal automaticamente:

- closeEsc = true: Habilitando esta opção, a tecla "ESC" faz com que o modal seja fechado.
- closeOutsideClick = true: Se Habilitada, esta opção fecha o modal ao clicar fora do conteúdo.
  Podem ser habilitadas simultaneamente.

![Imagem 5: closeOutsideClick = true: Se Habilitada, esta opção fecha o modal ao clicar fora do conteúdo. Podem ser habilitadas…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

Sempre que o modal é exibido ou ocultado os eventos ezOpenModal e ezCloseModal são emitidos repectivamente.

![Imagem 6: Sempre que o modal é exibido ou ocultado os eventos ezOpenModal e ezCloseModal são emitidos repectivamente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `align` `align` Define o alinhamento do ez-modal. `"left" | "right"` `undefined`| `closeEsc` `close-esc` Define se o ez-modal será fechado ao clicar `ESC`. `boolean` `false`| `closeOutsideClick` `close-outside-click` Define se o modal será fechado ao clicar fora do conteúdo. `boolean` `false`| `closeOutsideLeave` `close-outside-leave` Define se o modal será fechado se o mouse sair para fora do conteúdo. `boolean` `false`| `heightMode` `height-mode` Ativa o modo Full, permitindo que o Modal expanda-se verticalmente e ocupe todo o espaço disponível. `"full" | "regular"` `"regular"`| `modalSize` `modal-size` Define o tamanho do ez-modal. Devem ser definidas seguindo grid-layout. Exemplo: `col-sd-3`. `string` `undefined`| `opened` `opened` Define se o ez-modal está aberto. `boolean` `true`| `scrim` `scrim` Define o tipo de scrim a ser aplicado no overlay do modal `"light" | "medium" | "none"` `"medium"` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezCloseModal` Emitido quando o modal é fechado. `CustomEvent<boolean>`| `ezModalAction` Representa a interação com o usuário. OK - Quando o botão é acionado CANCEL - Quando o botão de cancelar é acionado CLOSE - Quando o botão de fechar é acionado. LOAD - Quando o modal é carregado (eventualmente pode ser usado para dar foco a um elemento específico) `CustomEvent<string>`| `ezOpenModal` Emitido quando o modal é aberto. `CustomEvent<any>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

---

### CSS Variables

| Variable Description| --ez-modal-z-index Define a camada em que o componente será exibido.| --ez-modal-vertical-padding Define o espaçamento vertical do conteúdo do modal.| --ez-modal-content-padding Define o padding entre o conteúdo e o modal | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
