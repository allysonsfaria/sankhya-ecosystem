---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-check/"
titulo: "Check"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-check/"
trilha: "Docs > Components > Components Doc > Ez Check"
---

# Check

Os CheckBox são usados para permitir ao usuário selecionar uma ou mais opções de uma lista de opções.
Utilize os checkbox quando o usuário possui múltipla escolha em uma grade, por exemplo.

Através da propriedade `mode`, existem dois modos de visualização: **regular** e **switch**.

- Se esta propriedade for omitida, o componente assume o formato "regular".
- No modo **regular** a visualização é a tradicional de uma caixinha marcada/desmarcada.
- No modo **switch** o campo tem uma interface em formato de um pino liga/desliga.

![Imagem 1: No modo switch o campo tem uma interface em formato de um pino liga/desliga.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Habilitado

Utilizado nos momentos em que o usuário pode interagir com o checkbox. É permitido marcar e desmarcar ele.

![Imagem 2: Utilizado nos momentos em que o usuário pode interagir com o checkbox. É permitido marcar e desmarcar ele.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado

Utilizado quando seu conteúdo não pode ser modificado. Podendo ser por questões como permissão ou regra da própria tela. Por exemplo:

![Imagem 3: Utilizado quando seu conteúdo não pode ser modificado. Podendo ser por questões como permissão ou regra da própria…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Marcado

O checkbox estará nesse estado quando estiver marcado e seu valor será considerado para as operações que serão feitas no sistema.

![Imagem 4: O checkbox estará nesse estado quando estiver marcado e seu valor será considerado para as operações que serão feitas…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desmarcado

O checkbox estará nesse estado quando estiver desmarcado e seu valor será considerado para as operações que serão feitas no sistema.

![Imagem 5: O checkbox estará nesse estado quando estiver desmarcado e seu valor será considerado para as operações que serão…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Indeterminado

Deixa o campo em um estado indeterminado, nem marcado nem desmarcado. (não disponível em modo "switch")

![Imagem 6: Deixa o campo em um estado indeterminado, nem marcado nem desmarcado. (não disponível em modo "switch")](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Versão alternativa (Switch)

#### Marcado

![Imagem 7: Marcado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Desmarcado

![Imagem 8: Desmarcado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Compacto

![Imagem 9: Compacto](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### getMode()

Utilizado para obter o modo atual do checkbox (regular ou switch).

![Imagem 10: Utilizado para obter o modo atual do checkbox (regular ou switch).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### setFocus()

Utilizado para setar o foco no checkbox.

![Imagem 11: Utilizado para setar o foco no checkbox.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do check (onEzChange).

![Imagem 12: Evento disparado ao mudar o estado do check (onEzChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alternativePlaceholder` `alternative-placeholder` Texto alternativo a ser apresentado como título do campo. `string` `undefined`| `compact` `compact` Define o modo compacto com espaçamento menor entre label e o input `boolean` `false`| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `indeterminate` `indeterminate` Se true ativa o estado indeterminado, nem marcado nem desmarcado (não disponível em modo `switch`). `boolean` `undefined`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `mode` `mode` Define o modo de visualização do ez-check. `CheckMode.REGULAR | CheckMode.SWITCH` `CheckMode.REGULAR`| `value` `value` Define o valor do campo. `boolean` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<any>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `getMode() => Promise<CheckMode>`

Obtém o modo escolhido.

##### Returns

Type: `Promise<CheckMode>`

---

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)
- [ez-link-builder](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-link-builder)
- [ez-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-list)
- [ez-multi-selection-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-selection-list)

#### Graph

```
graph TD;
  ez-form-view --> ez-check
  ez-link-builder --> ez-check
  ez-list --> ez-check
  ez-multi-selection-list --> ez-check
  style ez-check fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-check--box--width Define a largura do box do checkbox.| --ez-check--box--height Define a altura do box do checkbox.| --ez-check--width Define a largura do input do checkbox.| --ez-check--height Define a altura do input do checkbox| --ez-check--border-radius Define o raio da borda do input do checkbox.| --ez-check--checked--background-color Define a cor de fundo do input do checkbox quando marcado.| --ez-check--focus--background-color Define a cor de fundo do input do checkbox quando focado.| --ez-check--hover--background-color Define a cor de fundo do input do checkbox quando o cursor está sobre ele.| --ez-check--checked--disabled--background-color Define a cor de fundo do input do checkbox quando marcado e desabilitado.| --ez-check--border Define o estilo da borda do input do checkbox.| --ez-check--disabled--border Define o estilo da borda do input do checkbox quando desabilitado.| --ez-check--checked--border Define o estilo da borda do input do checkbox quando marcado.| --ez-check--checked--hover--background-color Define a cor de fundo do input do checkbox quando ativo e com o cursor sobre ele.| --ez-check--checked--focus--background-color Define a cor de fundo do input do checkbox quando ativo e focado.| --ez-check--check--image Contém o ícone do input marcado.| --ez-check--indeterminate--image Ícone usado para o estado "indeterminado" do componente.| --ez-check--check--background-color Define a cor de fundo do slot do ícone quando marcado.| --ez-check--check--disabled--background-color Define a cor de fundo do slot do ícone quando marcado e desabilitado.| --ez-switch--slider--width Define a largura do slider do checkbox.| --ez-switch--slider--height Define a altura do slider do checkbox.| --ez-switch--pin--width Define a largura do pino do slider do checkbox.| --ez-switch--pin--height Define a altura do pino do slider do checkbox.| --ez-switch--focus--width Define a largura do slider quando focado.| --ez-switch--focus--height Define a altura do slider quando focado.| --ez-switch--background-color Define a cor de fundo do checkbox no modo switch.| --ez-switch--disabled--background-color Define a cor de fundo do checkbox desabilitado no modo switch.| --ez-switch--disabled--checked--background-color Define a cor de fundo do checkbox marcado no modo switch.| --ez-switch--checked--background-color Define a cor de fundo do checkbox marcado no modo switch.| --ez-switch--pin--background-color Define a cor de fundo do pino do slider.| --ez-switch--pin--disabled--background-color Define a cor de fundo do pino do slider quando desabilitado.| --ez-switch--pin--checked--background-color Define a cor de fundo do pino do slider quando marcado.| --ez-switch--pin--checked--disabled--background-color Define a cor de fundo do pino do slider quando marcado e desabilitado1.| --ez-switch--pin--focus--background-color Define a cor de fundo do pino do slider quando focado.| --ez-switch--pin--checked--focus--background-color Define a cor de fundo do pino do slider quando marcado e focado.| --ez-switch--pin--border-color Define a cor da borda do pino do slider.| --ez-switch--pin--disabled--border-color Define a cor da borda do pino do slider quando desabilitado.| --ez-check--label--font-size Define o tamanho da fonte do label.| --ez-check--label--font-family Define a família da fonte do label.| --ez-check--label--color Define a cor da fonte do label.| --ez-check--label--disabled--color Define a cor da fonte do label quando desabilitado. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
