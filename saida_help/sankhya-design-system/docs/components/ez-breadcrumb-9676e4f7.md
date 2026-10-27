---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-breadcrumb/"
titulo: "Breadcrumb"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-breadcrumb/"
trilha: "Docs > Components > Components Doc > Ez Breadcrumb"
---

# Breadcrumb

O Breadcrumb é um componente responsável por apresentar uma sequência de links hierárquicos, proporcionando ao usuário uma clara orientação em relação à página principal, ao mesmo tempo em que permite uma navegação intuitiva entre as páginas anteriores.

![Imagem 1: O Breadcrumb é um componente responsável por apresentar uma sequência de links hierárquicos, proporcionando ao usuário…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Sem ícone

Variação do componente sem a presença de ícones.

![Imagem 2: Variação do componente sem a presença de ícones.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com ícone

Variação do componente com ícone à esquerda.

![Imagem 3: Variação do componente com ícone à esquerda.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Modos de apresentação `fillMode`

A propriedade `fillMode` permite personalização do modo de apresentação proporcionando flexibilidade ao componente. Sendo assim, é possível escolher entre dois modos: `auto` e `regular`, sendo `auto` o valor padrão.

### Auto

No modo `auto`, o componente se adapta de forma responsiva, ajustando-se dinamicamente ao espaço disponível na tela. Quando o Breadcrumb excede o espaço disponível, é acionado um mecanismo de ellipsis que oculta os itens excedentes, garantindo uma apresentação limpa e organizada.

Importante

Para garantir o correto funcionamento da funcionalidade `auto` do Breadcrumb, é necessário **sempre utilizar o Breadcrumb dentro de um container (HTMLElement) que não contenha outros elementos filhos**.

![Imagem 4: Para garantir o correto funcionamento da funcionalidade auto do Breadcrumb, é necessário sempre utilizar o Breadcrumb…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Regular

Já no modo regular, é concedido controle total sobre as configurações. Por meio desse modo, é possível definir manualmente a quantidade máxima de itens exibidos (`maxItems`) e até mesmo a posição do ellipsis (`positionEllipsis`), permitindo ajustes personalizados de acordo com especificações desejadas.

![Imagem 5: Já no modo regular, é concedido controle total sobre as configurações. Por meio desse modo, é possível definir…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos

#### onSelectedItem()

Quando o usuário escolhe um link, esse evento é emitido.

![Imagem 6: Quando o usuário escolhe um link, esse evento é emitido.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `fillMode` `fill-mode` Define o modo de uso do Breadcrumb. `"auto" | "regular"` `"auto"`| `items` -- Lista de itens do breadcrumb. `IBreadcrumbItem[]` `[]`| `maxItems` `max-items` Define o limite máximo de itens a serem renderizados. `number` `4`| `positionEllipsis` `position-ellipsis` Define a posição do Ellipsis nos itens visíveis do Breadcrumb. `number` `1` | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `selectedItem` Emitido quando um item do breadcrumb é selecionado. `CustomEvent<IBreadcrumbItem>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-dropdown](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown)

#### Graph

```
graph TD;
  ez-breadcrumb --> ez-icon
  ez-breadcrumb --> ez-dropdown
  ez-dropdown --> ez-skeleton
  ez-dropdown --> ez-icon
  style ez-breadcrumb fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --breadcrumb\_\_item--label--color--title-primary Define a cor da fonte do link, com exceção do último.| --breadcrumb\_\_item--label--color--active Define a cor da fonte do último link| --breadcrumb\_\_item--label--font-weight Define o peso da fonte. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
