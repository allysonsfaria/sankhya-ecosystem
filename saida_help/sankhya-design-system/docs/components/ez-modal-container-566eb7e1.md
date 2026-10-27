---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal-container/"
titulo: "Modal Container"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-modal-container/"
trilha: "Docs > Components > Components Doc > Ez Modal Container"
---

# Modal Container

## Visão Geral

O componente `ez-modal-container` fornece uma estrutura padronizada para exibir conteúdo em modais e popups. Ele inclui cabeçalho com título e subtítulo, área de conteúdo personalizável e rodapé com botões de ação (OK e Cancelar), além de suporte completo a navegação por teclado.

É especialmente útil quando você precisa de uma interface consistente para diálogos de confirmação, formulários modais ou qualquer conteúdo que exija interação do usuário em uma camada sobreposta.

## Exemplo Básico

![Imagem 1: Exemplo Básico](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Sem barra de títulos

Útil quando você precisa de um container simples sem cabeçalho. Utilize a propriedade `showTitleBar={false}` para ocultar o cabeçalho completo.

![Imagem 2: Útil quando você precisa de um container simples sem cabeçalho. Utilize a propriedade showTitleBar={false} para ocultar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Personalização dos botões

O modal container oferece controle total sobre os botões de ação através das propriedades de label e status.

#### Texto dos botões

Use `okButtonLabel` e `cancelButtonLabel` para definir textos personalizados nos botões.

![Imagem 3: Use okButtonLabel e cancelButtonLabel para definir textos personalizados nos botões.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Botão desabilitado

Use `okButtonStatus="DISABLED"` ou `cancelButtonStatus="DISABLED"` para desabilitar os botões.

![Imagem 4: Use okButtonStatus="DISABLED" ou cancelButtonStatus="DISABLED" para desabilitar os botões.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Botão oculto

Use `okButtonStatus="HIDDEN"` ou `cancelButtonStatus="HIDDEN"` para ocultar os botões.

Dica

Para ocultar um botão, você também pode omitir o `label` correspondente. Ambas as abordagens funcionam.

![Imagem 5: Para ocultar um botão, você também pode omitir o label correspondente. Ambas as abordagens funcionam.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Botão de fechar

Por padrão, o botão de fechar (X) é exibido no canto superior direito. Use `showCloseButton={false}` para ocultá-lo.

![Imagem 6: Por padrão, o botão de fechar (X) é exibido no canto superior direito. Use showCloseButton={false} para ocultá-lo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de uso

### Validação de formulário

Exemplo de como desabilitar o botão OK dinamicamente até que todos os campos obrigatórios sejam preenchidos corretamente.

![Imagem 7: Exemplo de como desabilitar o botão OK dinamicamente até que todos os campos obrigatórios sejam preenchidos…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Gerenciamento de eventos

Demonstração de como capturar e tratar as ações do modal. O evento `ezModalAction` pode emitir 4 valores diferentes:

- **"OK"** - Quando o usuário clica no botão OK ou pressiona Enter
- **"CANCEL"** - Quando o usuário clica no botão Cancelar
- **"CLOSE"** - Quando o usuário clica no botão fechar (X) ou pressiona Esc
- **"LOAD"** - Disparado após o componente ser montado no DOM

![Imagem 8: "LOAD" - Disparado após o componente ser montado no DOM](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modal informativo

Modal simples com apenas um botão de confirmação, ideal para exibir mensagens informativas ou alertas.

![Imagem 9: Modal simples com apenas um botão de confirmação, ideal para exibir mensagens informativas ou alertas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ações customizadas

Exemplo de como criar sua própria interface de ações dentro do modal, ocultando os botões padrão através de `okButtonStatus="HIDDEN"` e `cancelButtonStatus="HIDDEN"`.

![Imagem 10: Exemplo de como criar sua própria interface de ações dentro do modal, ocultando os botões padrão através de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Atalhos de teclado

O componente possui suporte nativo para navegação por teclado:

- **Enter** - Dispara o evento com ação `"OK"`
- **Esc** - Dispara o evento com ação `"CLOSE"`

Importante

Os atalhos de teclado funcionam apenas quando o componente possui foco. O componente só será focado automaticamente caso a propriedade `autoFocus` seja verdadeira. Se você precisar restaurar o foco após interações específicas (como abrir um popup ou executar uma ação), será necessário implementar essa lógica manualmente.

## API do componente

### Properties

| Property Attribute Description Type Default| `autoFocus` `auto-focus` Se true o modal container receberá o foco ao ser renderizado. `boolean` `false`| `cancelButtonLabel` `cancel-button-label` Define o texto do botão de cancelamento. `string` `undefined`| `cancelButtonStatus` `cancel-button-status` Define o estado do botão de cancelamento. `"DISABLED" | "ENABLED" | "HIDDEN"` `undefined`| `modalSubTitle` `modal-sub-title` Texto do subtítulo, geralmente usado para orientação do usuário. `string` `undefined`| `modalTitle` `modal-title` Texto a ser apresentado como título do modal. `string` `undefined`| `okButtonLabel` `ok-button-label` Determina o texto do botão de confirmação. `string` `undefined`| `okButtonStatus` `ok-button-status` Define o estado do botão de confirmação. `"DISABLED" | "ENABLED" | "HIDDEN"` `undefined`| `showCloseButton` `show-close-button` Define a visibilidade do botão de fechar. `boolean` `true`| `showTitleBar` `show-title-bar` Define se o cabeçalho será mostrado. `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezModalAction` Representa a interação com o usuário. OK - Quando o botão é acionado CANCEL - Quando o botão de cancelar é acionado CLOSE - Quando o botão de fechar é acionado. LOAD - Quando o modal é carregado (eventualmente pode ser usado para dar foco a um elemento específico) `CustomEvent<string>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-link-builder](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-link-builder)
- [ez-simple-image-uploader](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-simple-image-uploader)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-modal-container --> ez-icon
  ez-modal-container --> ez-button
  ez-button --> ez-icon
  ez-link-builder --> ez-modal-container
  ez-simple-image-uploader --> ez-modal-container
  style ez-modal-container fill:#f9f,stroke:#333,stroke-width:4px
```

---
