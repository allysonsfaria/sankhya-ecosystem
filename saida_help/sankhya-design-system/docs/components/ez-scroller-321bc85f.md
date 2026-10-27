---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scroller/"
titulo: "Scroller"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-scroller/"
trilha: "Docs > Components > Components Doc > Ez Scroller"
---

# Scroller

As barras de rolagem servem para navegar em uma série de elementos ou uma lista dentro de um determinado espaço e podem ser utilizadas na horizontal ou vertical.

![Imagem 1: As barras de rolagem servem para navegar em uma série de elementos ou uma lista dentro de um determinado espaço e podem…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Scroll na direção Vertical

![Imagem 2: Scroll na direção Vertical](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Scroll na direção Horizontal

![Imagem 3: Scroll na direção Horizontal](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Scroll em ambas direções

(Vertical e Horizontal)

![Imagem 4: (Vertical e Horizontal)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Scroll com efeito de sombreamento

> Propriedade utilizada: **activeShadow**

#### Scroll na direção Vertical

![Imagem 5: Scroll na direção Vertical](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Scroll na direção Horizontal

![Imagem 6: Scroll na direção Horizontal](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Scroll em ambas direções

(Vertical e Horizontal)

Importante

Somente na vertical e na horizontal conseguimos utilizar o efeito de sombreamento.

## API do componente

### Properties

| Property Attribute Description Type Default| `activeShadow` `active-shadow` Define se haverá efeito de sombreado. `boolean` `false`| `direction` `direction` Define a direção em que haverá scroll. `EzScrollDirection.BOTH | EzScrollDirection.HORIZONTAL | EzScrollDirection.VERTICAL` `undefined`| `locked` `locked` Define se o `scroll` estará bloqueado. `boolean` `false` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-guide-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator)
- [ez-sidebar-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator)

#### Graph

```
graph TD;
  ez-guide-navigator --> ez-scroller
  ez-sidebar-navigator --> ez-scroller
  style ez-scroller fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-scroller--box-shadow-color Define a cor de efeito de sombreado com componente.| --ez-scroller\_\_scrollbar--color-default Define a cor da barra de rolagem do componente.| --ez-scroller\_\_scrollbar--color-background Define a cor de fundo da barra de rolagem do componente.| --ez-scroller\_\_scrollbar--color-hover Define a cor do hover na barra de rolagem do componente.| --ez-scroller\_\_scrollbar--color-clicked Define a cor do active na barra de rolagem do componente.| --ez-scroller\_\_scrollbar--border-radius Define o raio da borda da barra de rolagem do componente.| --ez-scroller\_\_scrollbar--width Define a largura da barra de rolagem do componente.| --ez-scroller\_\_max-height Define o a altura máxima do componente.| --ez-scroller\_\_scrollbar--padding-right Define o espaçamento interno direito da barra de rolagem do componente. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
