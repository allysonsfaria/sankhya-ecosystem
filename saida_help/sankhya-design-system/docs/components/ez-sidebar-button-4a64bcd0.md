---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-button/"
titulo: "Sidebar Button"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-button/"
trilha: "Docs > Components > Components Doc > Ez Sidebar Button"
---

# Sidebar Button

O componente se trata de uma ação para expandir menu laterais que estejam recolhidos/ocultos.

![Imagem 1: O componente se trata de uma ação para expandir menu laterais que estejam recolhidos/ocultos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezClick()

Evento disparado ao clicar no componente.

![Imagem 2: Evento disparado ao clicar no componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Events

| Event Description Type| `ezClick` Emitido sempre que o ez-sidebar-button é clicado. `CustomEvent<void>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-guide-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-guide-navigator)
- [ez-sidebar-navigator](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-sidebar-navigator)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-sidebar-button --> ez-icon
  ez-guide-navigator --> ez-sidebar-button
  ez-sidebar-navigator --> ez-sidebar-button
  style ez-sidebar-button fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-sidebar-button--width Define a largura do span do botão.| --ez-sidebar-button--hover--width Define a largura do span do botão quando passar o mouse em cima.| --ez-sidebar-button--height Define a altura do span do botão.| --ez-sidebar-navigator-button--z-index Define a camada em que o componente será exibido.| --ez-sidebar-button--background-color--xlight Define a cor de fundo do botão.| --ez-sidebar-button--background-color--primary Define a cor de fundo do span do botão.| --ez-sidebar-button--space--small Define um espaçamento pequeno entre elementos do componente.| --ez-sidebar-button--space--medium Define um espaçamento mediano entre elementos do componente.| --ez-sidebar-button--box-shadow Define a sombra default do botão.| --ez-sidebar-button--hover--box-shadow Define a sombra do botão quando passar o mouse em cima.| --ez-sidebar-button--border--radius-small Define a borda arrendondada no valor de 6px.| --ez-sidebar-button--border--radius-medium Define a borda arrendondada no valor de 12px. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
