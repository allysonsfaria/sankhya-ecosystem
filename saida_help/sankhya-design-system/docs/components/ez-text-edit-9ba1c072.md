---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit/"
titulo: "Text Edit"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit/"
trilha: "Docs > Components > Components Doc > Ez Text Edit"
---

# Text Edit

Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o cumprimento do conteúdo que você espera que o usuário insira. Esse input padrão é para conteúdo curto de uma linha.

![Imagem 1: Os inputs permitem que os usuários insiram dados de texto de formato livre. O tipo de campo utilizado deve refletir o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

![Imagem 2: Exemplos de métodos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Evento emitido ao salvar uma edição.

![Imagem 3: Evento emitido ao salvar uma edição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Disparado ao cancelar uma edição.

![Imagem 4: Disparado ao cancelar uma edição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `styled` -- Define atributos do estilo. `IStyled` `undefined`| `value` `value` Define o valor do campo. `string` `undefined` | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `cancelEdition` Emitido ao cancelar uma edição `CustomEvent<any>`| `saveEdition` Emitido ao salvar uma edição `CustomEvent<any>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `applyFocusSelect() => Promise<void>`

Aplica foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-collapsible-box](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-collapsible-box)

#### Depends on

- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)
- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-text-edit --> ez-text-input
  ez-text-edit --> ez-button
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-button --> ez-icon
  ez-collapsible-box --> ez-text-edit
  style ez-text-edit fill:#f9f,stroke:#333,stroke-width:4px
```

---
