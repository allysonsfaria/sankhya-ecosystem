---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-radio-button/"
titulo: "Radio Button"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-radio-button/"
trilha: "Docs > Components > Components Doc > Ez Radio Button"
---

# Radio Button

Use os Radio button quando tiver um grupo de opções e apenas uma seleção da lista for permitida.

![Imagem 1: Use os Radio button quando tiver um grupo de opções e apenas uma seleção da lista for permitida.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Adicionar as opções por array

![Imagem 2: Adicionar as opções por array](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Desabilitado

![Imagem 3: Desabilitado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Orientação horizontal

![Imagem 4: Orientação horizontal](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Evento

Sempre que uma opção é selecionada, um evento ezChange é emitido com o valor selecionado.

![Imagem 5: Sempre que uma opção é selecionada, um evento ezChange é emitido com o valor selecionado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `direction` `direction` Define a direção dos itens. `"horizontal" | "vertical"` `"vertical"`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `options` -- Define as opções que serão apresentadas `Radio[]` `[]`| `value` `value` Define o valor do campo. `any` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<any>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

---

### CSS Variables

| Variable Description| --ez-radio-button--font-family Define a família da fonte do label.| --ez-radio-button--font-size Define o tamanho do label.| --ez-radio-button--font-weight Define o peso da fonte do label.| --ez-radio-button--font-color Define a cor do texto.| --ez-radio-button--padding-vertical Define o espaço superior e inferior da lista de opções.| --ez-radio-button--padding-horizontal Define o espaço lateral da lista de opções.| --ez-radio-button\_\_form-label--font-family Define a família da fonte do label.| --ez-radio-button\_\_form-label--font-weight Define o peso da fonte do label.| --ez-radio-button\_\_form-label--title-primary Define a cor do texto.| --ez-radio-button\_\_form-label--font-size Define o tamanho do label.| --ez-radio-button\_\_form-label--padding-horizontal Define o espaço lateral da lista de opções.| --ez-radio-button\_\_form-radio--border-color cor da borda do radio sem seleção (sem seleção / sem foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--checked--color cor do radio selecionado (com seleção / sem foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--disabled--border-color cor da borda do radio quando está desativado (sem seleção / sem foco / sem hover / disabled)| --ez-radio-button\_\_form-radio--disabled--background-color cor do background do radio quando está desativado (sem seleção / sem foco / sem hover / disabled)| --ez-radio-button\_\_form-radio--disabled--color cor da label quando o radio está desativado (sem seleção / sem foco / sem hover / disabled)| --ez-radio-button\_\_form-radio--disabled--before--background-color cor do centro do radio quando o radio está desativado (com seleção / sem foco / sem hover / disabled)| --ez-radio-button\_\_form-radio--focus--background-color cor do background quando o radio está ativado e sem seleção (sem seleção / com foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--checked--box-shadow-color cor do box-shadow quando o radio está ativado e sem seleção (sem seleção / com foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--checked--focus--background-color cor do background quando o radio está marcado e com foco (com seleção / com foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--checked--focus--box-shadow-color cor do background quando o radio está marcado e com foco (com seleção / com foco / sem hover / enabled)| --ez-radio-button\_\_form-radio--checked--hover--background-color cor do background quando o radio está marcado, com foco e com hover (com seleção / com foco / com hover / enabled)| --ez-radio-button\_\_form-radio--checked--hover--box-shadow-color cor do box-shadow quando o radio está marcado, com foco e com hover (com seleção / com foco / com hover / enabled)| --ez-radio-button\_\_form-radio--hover--box-shadow-color cor do hover quando o radio está desmarcado (sem seleção / sem foco / com hover / enabled)| --ez-radio-button\_\_form-radio--checked--disabled--hover--background-color cor do fundo quando o radio está marcado e desativado (com seleção / sem foco / com hover / disabled) | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
