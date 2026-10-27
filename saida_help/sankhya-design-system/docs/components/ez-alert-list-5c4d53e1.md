---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert-list/"
titulo: "AlertList"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert-list/"
trilha: "Docs > Components > Components Doc > Ez Alert List"
---

# AlertList

O componente AlertList tem a função de exibir uma lista de alertas em formato de popup, garantindo que não interfira na usabilidade do conteúdo abaixo dele.

![Imagem 1: O componente AlertList tem a função de exibir uma lista de alertas em formato de popup, garantindo que não interfira na…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Habilitar expansão

![Imagem 2: Habilitar expansão](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Título com callback

![Imagem 3: Título com callback](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alerts` -- Lista de alertas que devem ser apresentados no componente. `AlertItem[]` `[]`| `enableDragAndDrop` `enable-drag-and-drop` Define se o componente pode ser arrastado na tela. `boolean` `undefined`| `enableExpand` `enable-expand` Define se o componente pode ser expandido. `boolean` `true`| `expanded` `expanded` Define se o componente está expandido. `boolean` `false`| `itemRightSlotBuilder` -- Define builder para elementos a direita do componente `(item: ListItem, group?: ListGroup) => string | HTMLElement` `undefined`| `opened` `opened` Define se o componente está aberto. `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [ez-list](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-list)

#### Graph

```
graph TD;
  ez-alert-list --> ez-button
  ez-alert-list --> ez-list
  ez-button --> ez-icon
  ez-list --> ez-check
  style ez-alert-list fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-alert-list\_\_container--width Define a largura da lista minimizado| --ez-alert-list\_\_container--height Define a altura da lista minimizado| --ez-alert-list\_\_container--width--expanded Define a largura da lista maximizada| --ez-alert-list\_\_container--height--expanded Define a altura da lista maximizada| --ez-alert-list\_\_title--font-family Define a fonte do título do componente| --ez-alert-list\_\_title--font-size Define o tamanho da fonte do título do popup.| --ez-alert-list\_\_title--color Define a cor da fonte do título do popup.| --ez-alert-list\_\_title--font-weight Define o peso da fonte do título do popup.| --ez-list\_\_item--border-bottom Define a borda inferior do item da lista.| --ez-list\_\_item--border-bottom-color Define a cor da borda inferior do item da lista.| --ez-list\_\_item--white-space Define o tipo da quebra de linha do item da lista. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
