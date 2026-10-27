---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input/"
titulo: "DateInput"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input/"
trilha: "Docs > Components > Components Doc > Ez Date Input"
---

# DateInput

Popup de seleção de data, date time e intervalos de data.

Documentação do componente EzDateInput.

![Imagem 1: Documentação do componente EzDateInput.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo `inverted` melhorando o contraste.

![Imagem 2: Em backgrounds escuros os inputs devem mudar de aparência para o modo inverted melhorando o contraste.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Valor inicial

Exemplo de data inicial inserida no componente.

![Imagem 3: Exemplo de data inicial inserida no componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado

Campo disponível para uso.

![Imagem 4: Campo disponível para uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Campo indisponível para uso.

![Imagem 5: Campo indisponível para uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

![Imagem 6: Quando há um problema de validação, serve como orientação ao usuário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo slim

Modo reduzido do tamanho do campo.

![Imagem 7: Modo reduzido do tamanho do campo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo regular (default)

Modo padrão do tamanho do campo.

![Imagem 8: Modo padrão do tamanho do campo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática
temos os métodos `setFocus()` e `setBlur()`.

O exemplo abaixo demonstra isso através do botão **Focar Campo**. Clicando nesse
botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

![Imagem 9: O exemplo abaixo demonstra isso através do botão Focar Campo . Clicando nesse botão o campo ganhará foco e após 2…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

![Imagem 10: Retorna informando se o campo está inválido (true | false).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do componente (onEzChange).

![Imagem 11: Evento disparado ao mudar o estado do componente (onEzChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezStartChange()

Evento emitido ao iniciar a alteração.

![Imagem 12: Evento emitido ao iniciar a alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezCancelWaitingChange()

Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é disparado.

![Imagem 13: Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `value` -- Define o valor do campo. `Date` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezCancelWaitingChange` Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. `CustomEvent<void>`| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<Date>`| `ezInput` Emitido quando o usuário digita uma data válida no campo. `CustomEvent<Date>`| `ezStartChange` Emitido ao iniciar a alteração (digitação incompleta). `CustomEvent<WaitingChange>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `getValueAsync() => Promise<Date>`

##### Returns

Type: `Promise<Date>`

---

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

#### `setFocus(options?: TFocusOptions) => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Depends on

- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-popover-plus](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popover-plus)
- [ez-calendar](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-calendar)

#### Graph

```
graph TD;
  ez-date-input --> ez-text-input
  ez-date-input --> ez-popover-plus
  ez-date-input --> ez-calendar
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-popover-plus --> ez-popover-core
  ez-form-view --> ez-date-input
  style ez-date-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-date-input\_\_input--background-color Define a cor de fundo do input.| --ez-date-input\_\_input--border-color Define a cor da borda do input.| --ez-date-input\_\_calendar-image Contém a imagem do calendário. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
