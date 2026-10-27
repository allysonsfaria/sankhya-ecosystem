---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-number-input/"
titulo: "Number input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-number-input/"
trilha: "Docs > Components > Components Doc > Ez Number Input"
---

# Number input

![Imagem 1: Number input](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo "inverted" melhorando o contraste.

![Imagem 2: Em backgrounds escuros os inputs devem mudar de aparência para o modo "inverted" melhorando o contraste.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Campo indisponível para uso.

![Imagem 3: Campo indisponível para uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

![Imagem 4: Quando há um problema de validação, serve como orientação ao usuário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo slim

Modo reduzido do tamanho do campo.

![Imagem 5: Modo reduzido do tamanho do campo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Precision e Pretty Precision

Existem duas propriedades para influenciar a precisão dos campos numéricos.
"precision" determina o arredondamento do valor.
"prettyPrecision" influencia a apresentação do campo, dando preferência ao menor número de casas decimais.

![Imagem 6: Existem duas propriedades para influenciar a precisão dos campos numéricos. "precision" determina o arredondamento do…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### Controle de foco

Para possibilitar dar foco e remover foco do componente de forma programática
temos os métodos "setFocus()" e "setBlur()".

O exemplo abaixo demonstra isso através do botão **Focar campo**. Clicando nesse
botão o campo ganhará foco e após 2 segundos perderá foco automaticamente.

![Imagem 7: O exemplo abaixo demonstra isso através do botão Focar campo . Clicando nesse botão o campo ganhará foco e após 2…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### isInvalid()

Retorna informando se o campo está inválido (true | false).

![Imagem 8: Retorna informando se o campo está inválido (true | false).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange

Evento disparado ao mudar o estado do componente (onEzChange).

![Imagem 9: Evento disparado ao mudar o estado do componente (onEzChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezStartChange

Evento emitido ao iniciar a alteração.

![Imagem 10: Evento emitido ao iniciar a alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezCancelWaitingChange

Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é disparado.

![Imagem 11: Entre o evento ezStartChange e ezChange, se por algum motivo não foi possível completar a alteração, esse evento é…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `allowNegative` `allow-negative` Se false, o input não aceitará números negativos. `boolean` `true`| `alternativePlaceholder` `alternative-placeholder` Texto alternativo a ser apresentado como título do campo. `string` `undefined`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enabled` `enabled` Se false, o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `precision` `precision` Define quantas casas decimais serão exibidas. Caso haja mais casas haverá arredondamento. `number` `undefined`| `prettyPrecision` `pretty-precision` Define qual é o mínimo de casas depois da vírgula. Exemplo: 1,1 será exibido como 1,1000 quando `prettyPrecision = 4`. `number` `undefined`| `value` `value` Define o valor do campo. `number` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezCancelWaitingChange` Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. `CustomEvent<void>`| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<number>`| `ezInput` Emitido quando o usuário digita no campo. `CustomEvent<number>`| `ezStartChange` Emitido ao iniciar a alteração (digitação incompleta). `CustomEvent<WaitingChange>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `getValueAsync() => Promise<number>`

##### Returns

Type: `Promise<number>`

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

#### Graph

```
graph TD;
  ez-number-input --> ez-text-input
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-form-view --> ez-number-input
  style ez-number-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-number-input\_\_min-width Define a largura maxima do componente.| --ez-number-input\_\_max-width Define a largura minima do componente. | | | --- | --- | | | | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- |
