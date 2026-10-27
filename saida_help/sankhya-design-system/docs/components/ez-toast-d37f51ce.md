---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-toast/"
titulo: "Toast"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-toast/"
trilha: "Docs > Components > Components Doc > Ez Toast"
---

# Toast

Toasts são elementos de notificação não-modais, baseados em tempo de duração, usados para exibir mensagens curtas. Eles, geralmente, aparecem em algum lugar da tela sobrepondo todos os elementos (flutuantes) e desaparecem após alguns segundos.

![Imagem 1: Toasts são elementos de notificação não-modais, baseados em tempo de duração, usados para exibir mensagens curtas.…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados.

### Mensagem exibida.

![Imagem 2: Mensagem exibida.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tempo de exibição.

![Imagem 3: Tempo de exibição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adiciona ícone de check.

![Imagem 4: Adiciona ícone de check.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Uso do ícone de fechar.

![Imagem 5: Uso do ícone de fechar.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `canClose` `can-close` Se false, o usuário não consegue fechar. `boolean` `true`| `fadeTime` `fade-time` Define o tempo de exibição em milissegundos. `number` `5000`| `message` `message` Mensagem a ser exibida no componente. `string` `undefined`| `useIcon` `use-icon` Se true permite a utilização do slot de ícone. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `show(message: string, fadeTime: number, useIcon: boolean, canClose?: boolean) => Promise<void>`

Exibe o ez-toast.

##### Returns

Type: `Promise<void>`

---

### CSS Variables

| Variable Description| --ez-toast\_\_btn\_\_close\_\_image Contém o ícone de fechamento do toast.| --ez-toast\_\_container--z-index Define a camada em que o container será exibido.| --ez-toast\_\_container--background-color Define a cor de fundo do container.| --ez-toast\_\_container--left Define a posição esquerda do container.| --ez-toast\_\_container--bottom Define a posição inferior do container.| --ez-toast\_\_container--width Define a largura do container.| --ez-toast\_\_icon--padding-left Define o espaçamento à esquerda do ícone. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
