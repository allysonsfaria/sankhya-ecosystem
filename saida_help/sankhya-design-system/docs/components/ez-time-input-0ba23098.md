---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-time-input/"
titulo: "Time Input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-time-input/"
trilha: "Docs > Components > Components Doc > Ez Time Input"
---

# Time Input

![Imagem 1: Time Input](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Deixa o campo disponível.

![Imagem 2: Deixa o campo disponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Deixa o campo indisponível.

![Imagem 3: Deixa o campo indisponível.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Label.

![Imagem 4: Label.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com estado de erro.

![Imagem 5: Com estado de erro.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo regular.

![Imagem 6: Modo regular.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo slim.

![Imagem 7: Modo slim.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exibe ou não os segundos no calendário.

![Imagem 8: Exibe ou não os segundos no calendário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

### Faz o foco no componente de input.

![Imagem 9: Faz o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remove o foco no componente de input.

![Imagem 10: Remove o foco no componente de input.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Informa se o campo está inválido.

![Imagem 11: Informa se o campo está inválido.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Ao mudar o estado do componente.

![Imagem 12: Ao mudar o estado do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ao iniciar a alteração.

![Imagem 13: Ao iniciar a alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ao interromper alteração.

![Imagem 14: Ao interromper alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `showSeconds` `show-seconds` Se true considera segundos. `boolean` `false`| `value` `value` Define o valor do campo. `number` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezCancelWaitingChange` Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. `CustomEvent<void>`| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<number>`| `ezStartChange` Emitido ao iniciar a alteração (digitação incompleta). `CustomEvent<WaitingChange>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `isInvalid() => Promise<boolean>`

Retorna se o conteúdo é inválido.

##### Returns

Type: `Promise<boolean>`

---

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

---

#### `setFocus({ selectText }: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Depends on

- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-time-input --> ez-text-input
  ez-time-input --> ez-icon
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-form-view --> ez-time-input
  style ez-time-input fill:#f9f,stroke:#333,stroke-width:4px
```

---
