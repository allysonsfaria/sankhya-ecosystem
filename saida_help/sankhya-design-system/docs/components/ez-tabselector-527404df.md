---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tabselector/"
titulo: "Tabselector"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tabselector/"
trilha: "Docs > Components > Components Doc > Ez Tabselector"
---

# Tabselector

Selecionador de abas.

![Imagem 1: Selecionador de abas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados.

### Define o index da aba selecionada.

![Imagem 2: Define o index da aba selecionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Define a aba selecionada.

![Imagem 3: Define a aba selecionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Define as abas do componente.

Abas separadas por vírgula ",".

![Imagem 4: Abas separadas por vírgula ",".](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Ao mudar o estado do componente.

![Imagem 5: Ao mudar o estado do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `selectedIndex` `selected-index` Define o index da aba selecionada. `number` `undefined`| `selectedTab` `selected-tab` Define a aba selecionada. `string` `undefined`| `tabs` `tabs` Define o nome das abas do componente. Podendo serem separadas por vírgula "," ou em um Array de configuração. `Tab[] | string` `undefined` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do componente. `CustomEvent<Tab>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `goToTab(tabIndex: number, silent?: boolean) => Promise<void>`

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-tabselector --> ez-icon
  ez-form --> ez-tabselector
  style ez-tabselector fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --tabselector--backward-icon Contém o ícone de voltar para a aba anterior.| --tabselector--forward-icon Contém o ícone de avançar para a aba posterior. | | | --- | --- | | | | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- |
