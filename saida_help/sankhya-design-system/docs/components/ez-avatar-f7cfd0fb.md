---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-avatar/"
titulo: "Avatar"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-avatar/"
trilha: "Docs > Components > Components Doc > Ez Avatar"
---

# Avatar

O componente **Avatar** tem a função de representar visualmente um usuário, exibindo uma imagem, letra inicial de seu nome ou
um ícone, de acordo com a configuração realizada.

![Imagem 1: O componente Avatar tem a função de representar visualmente um usuário, exibindo uma imagem, letra inicial de seu nome…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

dica

A exibição do conteúdo respeitará a seguinte ordem de prioridade:

1. **URL da imagem** (`imageSrc`) - se uma imagem for fornecida, ela será exibida.
2. **Nome** (`name`) - caso não haja imagem, a letra inicial do nome será exibida.
3. **Ícone padrão** - se nenhuma imagem ou nome for fornecido, o ícone padrão será utilizado.

## Variações

### Tamanhos

O componente Avatar suporta diferentes tamanhos, que podem ser definidos por meio da propriedade `size`.

![Imagem 2: O componente Avatar suporta diferentes tamanhos, que podem ser definidos por meio da propriedade size .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Formatos

O componente Avatar pode ser exibido em dois formatos (quadrado ou redondo), controlados pela propriedade `shape`.

![Imagem 3: O componente Avatar pode ser exibido em dois formatos (quadrado ou redondo), controlados pela propriedade shape .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Interatividade

A propriedade `isInteractive` adiciona interatividade ao componente Avatar, exibindo um feedback visual quando o mouse passa por cima.

![Imagem 4: A propriedade isInteractive adiciona interatividade ao componente Avatar, exibindo um feedback visual quando o mouse…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícone a ser exibido

Por padrão, quando é exibido o avatar com ícone, é renderizado o ícone `account-outline`.
Podemos personalizar isso através da propriedade `iconName`, informando o valor de um dos ícones disponíveis em nossa biblioteca.

[Veja a lista completa de ícones.](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/icons/)

![Imagem 5: Veja a lista completa de ícones.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `iconName` `icon-name` Nome do ícone que deve ser exibido no avatar. `string` `undefined`| `imageSrc` `image-src` URL da imagem do Avatar. `string` `undefined`| `isInteractive` `is-interactive` Se true, o Avatar será interativo. Caso contrário, será estático. `boolean` `false`| `name` `name` Nome do usuário para exibição da inicial. `string` `undefined`| `shape` `shape` Define o formato do Avatar: 'circle' ou 'square'. `"circle" | "square"` `'circle'`| `size` `size` Tamanho do Avatar (valores permitidos): '320x320', '300x300', '280x280', '260x260', '240x240', '220x220', '200x200', '180x180', '160x160', '140x140', '120x120', '100x100', '80x80', '60x60'. `"100" | "120" | "140" | "160" | "180" | "200" | "220" | "240" | "260" | "280" | "300" | "320" | "60" | "80"` `'100'` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-tile-medium](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tile-medium)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-avatar --> ez-icon
  ez-tile-medium --> ez-avatar
  style ez-avatar fill:#f9f,stroke:#333,stroke-width:4px
```

---
