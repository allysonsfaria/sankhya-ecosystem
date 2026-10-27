---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input/"
titulo: "FilterInput"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter-input/"
trilha: "Docs > Components > Components Doc > Ez Filter Input"
---

# FilterInput

Documentação do componente EzFilterInput.

![Imagem 1: Documentação do componente EzFilterInput.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Inverted

Em backgrounds escuros os inputs devem mudar de aparência para o modo `inverted` melhorando o contraste.

![Imagem 2: Em backgrounds escuros os inputs devem mudar de aparência para o modo inverted melhorando o contraste.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado

Campo disponível para uso.

![Imagem 3: Campo disponível para uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Campo indisponível para uso.

![Imagem 4: Campo indisponível para uso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com estado de erro

Quando há um problema de validação, serve como orientação ao usuário.

![Imagem 5: Quando há um problema de validação, serve como orientação ao usuário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com restrict

Restringe o que o usuário pode digitar. Cada caractere digitado será testado e deve estar contido nessa string ou será descartado.

![Imagem 6: Restringe o que o usuário pode digitar. Cada caractere digitado será testado e deve estar contido nessa string ou será…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

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

#### setValue()

Método responsável por setar um novo valor ao campo.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada.

![Imagem 11: O método endSearch funcionará apenas quando a propriedade asyncSearch estiver ativada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### endSearch()

Método responsável por resetar o valor do campo para o ultimo valor inputado.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada.

![Imagem 12: O método endSearch funcionará apenas quando a propriedade asyncSearch estiver ativada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange()

Evento disparado quando o estado do componente é alterado (onEzChange).

![Imagem 13: Evento disparado quando o estado do componente é alterado (onEzChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezSearching()

O evento ezSearching é acionado exclusivamente no modo assíncrono, quando uma pesquisa está sendo realizada.

Importante

O método **endSearch** funcionará apenas quando a propriedade asyncSearch estiver ativada.
É importante ressaltar que, quando a propriedade **asyncSearch** estiver ativada, o value não será mais atualizado.

![Imagem 14: O método endSearch funcionará apenas quando a propriedade asyncSearch estiver ativada. É importante ressaltar que,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezFocusin()

Evento disparado quando acontece o foco no componente (ezFocusin).

![Imagem 15: Evento disparado quando acontece o foco no componente (ezFocusin).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `asyncSearch` `async-search` Define se o campo irá funcionar de forma assíncrona. `boolean` `false`| `autoFocus` `auto-focus` Se true o campo de texto receberá o foco ao ser renderizado. `boolean` `false`| `canShowError` `can-show-error` Se false deixa de exibir a mensagem de erro dentro do campo. `boolean` `true`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `errorMessage` `error-message` Define uma mensagem de orientação ao usuário, colocando o campo em modo inválido. `string` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o tamanho do campo. `"regular" | "slim"` `"regular"`| `restrict` `restrict` Restringe o que o usuário pode digitar. `string` `undefined`| `value` `value` Define o valor do campo. `string` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<string>`| `ezFocusIn` Emitido quando acontece o foco no campo. `CustomEvent<void>`| `ezSearching` Emitido quando está sendo realizada uma pesquisa no modo asyncSearch. `CustomEvent<string>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `endSearch() => Promise<void>`

Método responsável por resetar o valor do campo para o ultimo valor inputado.

##### Returns

Type: `Promise<void>`

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

---

#### `setValue(newValue: string) => Promise<void>`

Método responsável por setar um novo valor ao campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-guide-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator)
- [ez-multi-selection-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list)
- [ez-sortable-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sortable-list)

#### Depends on

- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-guide-navigator --> ez-filter-input
  ez-multi-selection-list --> ez-filter-input
  ez-sortable-list --> ez-filter-input
  style ez-filter-input fill:#f9f,stroke:#333,stroke-width:4px
```

---
