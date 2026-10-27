---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dialog/"
titulo: "Dialog"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dialog/"
trilha: "Docs > Components > Components Doc > Ez Dialog"
---

# Dialog

Dialogs são janelas "pop-up" usadas para apresentar informações que precisam de atenção imediata do usuário.

![Imagem 1: Dialogs são janelas "pop-up" usadas para apresentar informações que precisam de atenção imediata do usuário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Variações

![Imagem 2: Variações](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Confirmação

![Imagem 3: Confirmação](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones personalizados

![Imagem 4: Ícones personalizados](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Trabalhando com eventos

![Imagem 5: Trabalhando com eventos](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Propriedade beforeClose

![Imagem 6: Propriedade beforeClose](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `beforeClose` -- Define função a ser executada antes de fechar o modal `Function` `undefined`| `confirm` `confirm` Define se o ez-dialog será utilizado no modo de confirmação. `boolean` `false`| `dialogType` `dialog-type` Define aparência do ez-dialog. `DialogType.CRITICAL | DialogType.DEFAULT | DialogType.SUCCESS | DialogType.WARN` `undefined`| `ezTitle` `ez-title` Texto a ser apresentado como título do campo. `string` `undefined`| `message` `message` Define a menssagem exibida no ez-dialog. `string` `undefined`| `opened` `opened` Define se o ez-dialog está aberto. `boolean` `false`| `personalizedIconPath` `personalized-icon-path` Define o ícone a ser exibido. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezAccept` Emitido ao confirmar o ez-dialog. `CustomEvent<boolean>`| `ezCancel` Emitido ao cancelar o ez-dialog. `CustomEvent<boolean>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `show(title: string, message: string, dialogType: DialogType, confirm: boolean, icon: string, labelCancel: string, labelConfirm: string, btnConfirmDanger: boolean, beforeClose: Function) => Promise<boolean>`

Exibe o ez-dialog.

##### Returns

Type: `Promise<boolean>`

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-dialog --> ez-icon
  ez-dialog --> ez-button
  ez-button --> ez-icon
  style ez-dialog fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --dialog\_\_container-padding Define o espaçamento do container.| --dialog\_\_btn\_\_close--background-color Define a cor de fundo do botão de fechar.| --dialog\_\_btn\_\_no--padding-right Define o espaçamento direito do botão de negação.| --dialog\_\_btn\_\_close\_\_image Contém a imagem do ícone de fechamento.| --dialog\_\_btn\_\_min-width Define a largura mínima dos botões.| --dialog\_\_title--font-pattern Define o estilo da mensagem exibida no título.| --dialog\_\_title--padding-left Define o espaçamento a esquerda do título.| --dialog\_\_title\_\_container--padding-bottom Define o espaçamento abaixo do container do título.| --dialog\_\_title--weight--large Define o peso do título.| --dialog\_\_body--font-pattern Define o estilo do texto da mensagem.| --dialog\_\_body--text-shadow Define a sombra do texto da mensagem.| --dialog\_\_body--text-weight--medium Define o peso do texto da mensagem.| --dialog\_\_body--padding-bottom Define o espaçamento inferior do texto da mensagem.| --dialog\_\_body--font-size Define o tamanho do texto da mensagem.| --dialog\_\_body--color Define a cor do texto da mensagem.| --dialog\_\_icon--color Define a cor dos ícones dos indicadores de modo.| --dialog\_\_critical--background-color Define a cor do indicador do dialog de erro.| --dialog\_\_warning--background-color Define a cor do indicador do dialog de alert.| --dialog\_\_success--background-color Define a cor do indicador do dialog de sucesso.| --dialog-z-index Define a camada que o dialog será exibido.| --dialog--warning\_\_image Contém a imagem do ícone de alerta.| --dialog--critical\_\_image Contém a imagem do ícone crítico. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
