---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert/"
titulo: "Alert"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-alert/"
trilha: "Docs > Components > Components Doc > Ez Alert"
---

# Alert

O componente Alert tem o papel de apresentar mensagens de feedback contextuais no padrão de alerta, erro ou sucesso.

![Imagem 1: O componente Alert tem o papel de apresentar mensagens de feedback contextuais no padrão de alerta, erro ou sucesso.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Alerta

![Imagem 2: Alerta](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Erro

![Imagem 3: Erro](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Sucesso

![Imagem 4: Sucesso](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho

A largura do componente é definida livremente de acordo com o espaço disponível na tela ou o tamanho fixo do componente pai. Já a altura é determinada pelo conteúdo interno.

![Imagem 5: A largura do componente é definida livremente de acordo com o espaço disponível na tela ou o tamanho fixo do componente…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Quebra de linha

O componente conta com a funcionalidade de quebra automática de palavras (hyphenation) para evitar espaços excessivos em branco e melhorar a legibilidade do texto.

![Imagem 6: O componente conta com a funcionalidade de quebra automática de palavras (hyphenation) para evitar espaços excessivos…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `alertType` `alert-type` Define a cor e o ícone a serem exibidos no componente. `"critical" | "success" | "warn"` `'success'` | | | | | | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-alert --> ez-icon
  style ez-alert fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-alert-alert-container--padding-up-down Define o raio do padding interno para cima e para baixo.| --ez-alert-alert-container--padding-right-left Define o raio do padding interno para a esquerda e para a direita.| --ez-alert-alert-container--gap Define o espaçamento entre os elementos internos| --ez-alert-alert-container--border-radius Define o raio da borda do corpo do Alert.| --ez-alert-alert-container--font-color-warn Define a cor da fonte no estilo Warn.| --ez-alert-alert-container--icon-warn Define a cor do ícone no estilo Warn.| --ez-alert-alert-container--background-color-warn Define a cor do background no estilo Warn.| --ez-alert-alert-container--font-color-critical Define a cor da fonte no estilo Critical.| --ez-alert-alert-container--icon-critical Define a cor do ícone no estilo Critical.| --ez-alert-alert-container--background-color-critical Define a cor do background no estilo Critical.| --ez-alert-alert-container--font-color-success Define a cor da fonte no estilo Success.| --ez-alert-alert-container--icon-success Define a cor do ícone no estilo Success.| --ez-alert-alert-container--background-color-success Define a cor do background no estilo Success. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
