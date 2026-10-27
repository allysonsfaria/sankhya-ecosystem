---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip/"
titulo: "Tooltip"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tooltip/"
trilha: "Docs > Components > Components Doc > Ez Tooltip"
---

# Tooltip

Tooltip é um componente flutuante que exibe uma mensagem de texto quando o usuário passa o mouse sobre um elemento.

O tooltip é um componente inerte, ou seja, ele não possui eventos de foco, seleção ou clique.

![Imagem 1: O tooltip é um componente inerte, ou seja, ele não possui eventos de foco, seleção ou clique.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Tipos de Tooltip

> Propriedade utilizada: `type`

Atualmente o tooltip pode assumir um dos seguintes tipos: `default`, `success`, `warning` e `error`.

![Imagem 2: Atualmente o tooltip pode assumir um dos seguintes tipos: default , success , warning e error .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Posicionamento

> Propriedade utilizada: `placement`

O tooltip pode assumir diferentes posicionamentos, conforme necessidade.

![Imagem 3: O tooltip pode assumir diferentes posicionamentos, conforme necessidade.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Espaçamento entre o elemento âncora

> Propriedade utilizada: `gapOptions`

É possível definir o espaçamento entre o tooltip e seu elemento âncora de forma simples.

![Imagem 4: É possível definir o espaçamento entre o tooltip e seu elemento âncora de forma simples.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Debounce

> Propriedade utilizada: `debouncingTime`

Podemos definir um delay para o tempo de exibição do tooltip.

![Imagem 5: Podemos definir um delay para o tempo de exibição do tooltip.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Largura máxima

> Propriedades utilizadas: `maxWidth` e `useAnchorSize`

Podemos ajustar a largura máxima do tooltip conforme necessidade, ou mesmo definir que o tooltip terá a largura do elemento âncora.

![Imagem 6: Podemos ajustar a largura máxima do tooltip conforme necessidade, ou mesmo definir que o tooltip terá a largura do…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `active` `active` Define se o tooltip está ativo. `boolean` `true`| `anchoringElement` -- Elemento HTML que será utilizado como ancoragem do tooltip. `HTMLElement` `undefined`| `debouncingTime` `debouncing-time` Tempo de espera para exibir o tooltip após o evento de mouseenter. `number` `500`| `gapOptions` -- Define o espaçamento entre o tooltip e o elemento de ancoragem. `{ horizontalGap: number; verticalGap: number; }` `{ horizontalGap: 0, verticalGap: 0 }`| `maxWidth` `max-width` Define a largura máxima do elemento. `number` `200`| `message` `message` Mensagem que será apresentada no tooltip. `string` `undefined`| `placement` `placement` Define a posição do tooltip em relação ao elemento de ancoragem. `"bottom" | "bottom-end" | "bottom-start" | "left" | "left-end" | "left-start" | "right" | "right-end" | "right-start" | "top" | "top-end" | "top-start"` `'bottom'`| `strategy` `strategy` Define a estratégia de posicionamento do tooltip. Use 'fixed' quando o elemento estiver dentro de containers com position: relative. `"absolute" | "fixed"` `'absolute'`| `type` `type` Define o tipo de tooltip a ser exibido. `"default" | "error" | "success" | "warning"` `'default'`| `useAnchorSize` `use-anchor-size` Define se o elemento manterá o mesmo tamanho do componente de ancora. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-chip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chip)
- [ez-multi-select-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-multi-select-input)
- [ez-simple-image-uploader](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-simple-image-uploader)
- [ez-text-area](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-area)
- [ez-text-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-input)

#### Graph

```
graph TD;
  ez-chip --> ez-tooltip
  ez-multi-select-input --> ez-tooltip
  ez-simple-image-uploader --> ez-tooltip
  ez-text-area --> ez-tooltip
  ez-text-input --> ez-tooltip
  style ez-tooltip fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-tooltip--triangle-size Define o tamanho do triângulo da seta do tooltip.| --ez-tooltip--z-index Define o z-index do tooltip.| --ez-tooltip--padding Define o padding interno do tooltip.| --ez-tooltip--border-radius Define o border-radius do tooltip.| --ez-tooltip--font-family Define a família da fonte do tooltip.| --ez-tooltip--font-size Define o tamanho da fonte do tooltip.| --ez-tooltip--font-weight Define o peso da fonte do tooltip. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
