---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-file-item/"
titulo: "File item"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-file-item/"
trilha: "Docs > Components > Components Doc > Ez File Item"
---

# File item

Componente que representa um arquivo. É possível representar o progresso de upload, expressar a necessidade
de download ou remoção. Também fornece informações como tamanho, tipo e nome do arquivo.

![Imagem 1: Componente que representa um arquivo. É possível representar o progresso de upload, expressar a necessidade de download…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Características

### Tamanho do arquivo

![Imagem 2: Tamanho do arquivo](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Progresso

![Imagem 3: Progresso](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Sem remoção

![Imagem 4: Sem remoção](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícones por extensão

![Imagem 5: Ícones por extensão](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícone personalizado

![Imagem 6: Ícone personalizado](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

![Imagem 7: Exemplos de eventos](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `canRemove` `can-remove` Define se o usuário pode remover o arquivo que está sendo apresentado. `boolean` `true`| `fileName` `file-name` Define o nome do arquivo, com extensão. `string` `undefined`| `fileSize` `file-size` Tamanho do arquivo (em bytes). `number` `undefined`| `iconName` `icon-name` Define qual ícone que representa o arquivo. `string` `undefined`| `progress` `progress` Percentual de carregamento do arquivo para o servidor. `number` `100` | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezClick` Emitido ao clicar no ez-file-input (exceto no botão de remover). `CustomEvent<string>`| `ezRemove` Emitido ao clicar no botão de remover. `CustomEvent<string>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-file-item --> ez-icon
  style ez-file-item fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-file-item--height Define a altura do componente.| --ez-file-item--padding Define espaçamento interno do componente.| --ez-file-item--border-radius Define o arredondamento dos retangulos.| --ez-file-item--border-color Define a cor da borda.| --ez-file-item--border-style Define largura e estilo da borda.| --ez-file-item--font-family Define a família da fonte.| --ez-file-item--font-size Define o tamanho da fonte.| --ez-file-item--font-weight Define o peso da fonte.| --ez-file-item--color Define a cor da fonte.| --ez-file-item\_\_file-size--font-weight Define o peso da fonte do tamanho do arquivo.| --ez-file-item\_\_file-size--color Define o peso da fonte do tamanho do arquivo.| --ez-file-item--icon-color Define a cor do ícone. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
