---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-card-item/"
titulo: "CardItem"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-card-item/"
trilha: "Docs > Components > Components Doc > Ez Card Item"
---

# CardItem

Documentação do componente EzCardItem.

![Imagem 1: Documentação do componente EzCardItem.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezClick()

Evento disparado ao clicar no componente.

![Imagem 2: Evento disparado ao clicar no componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `compacted` `compacted` Determina se o componente será apresentado no modo compacto. `boolean` `false`| `enableKey` `enable-key` Determina se a chave do item deve ser exibida. `boolean` `true`| `item` -- Determina o conteúdo do card. Deve conter um objeto no formato: `{title: string, key: string, details: any}`. `CardItem` `undefined` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezClick` Emitido sempre que o ez-card é clicado. `CustomEvent<CardItem>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-search-result-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search-plus/subcomponent/ez-search-result-list)
- [search-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-search/subcomponent/search-list)

#### Graph

```
graph TD;
  ez-search-result-list --> ez-card-item
  search-list --> ez-card-item
  style ez-card-item fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-card-item--font-size Define o tamanho da fonte do componente.| --ez-card-item--font-size-compacted Define o tamanho da fonte do componente no modo compacto.| --ez-card-item--font-family Define a família da fonte do componente.| --ez-card-item--font-weight Define o peso da fonte do componente.| --ez-card-item--font-weight-large Define o peso da fonte do title do componente.| --ez-card-item--color Define a cor da fonte do componente.| --ez-card-item\_\_key--color Define a cor da fonte da key do componente.| --ez-card-item\_\_detail-label--color Define a cor da fonte do label do detalhe do componente.| --ez-card-item\_\_detail-value--color Define a cor da fonte do valor do detalhe do componente.| --ez-card-item\_\_detail--padding-bottom Define o espaçamento inferior dos detalhes do componente.| --ez-card-item\_\_title--padding-bottom Define o espaçamento inferior do title do componente.| --ez-card-item\_\_highlight--color Define a cor do highlight / marcação nos textos do componente.| --ez-card-item--detail-label--font-weight Define o peso da fonte do componente. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
