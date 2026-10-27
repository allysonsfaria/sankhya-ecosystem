---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-upload/"
titulo: "Upload"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-upload/"
trilha: "Docs > Components > Components Doc > Ez Upload"
---

# Upload

O componente de upload é utilizado para selecionar arquivos, imagens, vídeo e etc do diretório do usuário, de acordo com o que a tela permitir.

![Imagem 1: O componente de upload é utilizado para selecionar arquivos, imagens, vídeo e etc do diretório do usuário, de acordo…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Habilitado.

![Imagem 2: Habilitado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitado.

![Imagem 3: Desabilitado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Label.

![Imagem 4: Label.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Subtitle.

![Imagem 5: Subtitle.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho limite do arquivo.

![Imagem 6: Tamanho limite do arquivo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Quantidade limite de arquivos.

![Imagem 7: Quantidade limite de arquivos.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Cabeçalhos da requisição.

![Imagem 8: Cabeçalhos da requisição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### URL de upload.

![Imagem 9: URL de upload.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### URL para remover arquivo.

![Imagem 10: URL para remover arquivo.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de métodos.

### Adiciona o foco.

![Imagem 11: Adiciona o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remove o foco.

![Imagem 12: Remove o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Adiciona arquivos para upload.

![Imagem 13: Adiciona arquivos para upload.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos.

### Ao mudar o estado do componente.

![Imagem 14: Ao mudar o estado do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ao iniciar a alteração.

![Imagem 15: Ao iniciar a alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ao interromper uma alteração.

![Imagem 16: Ao interromper uma alteração.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `enabled` `enabled` Se false o usuário não pode interagir com o campo. `boolean` `true`| `label` `label` Texto a ser apresentado como título do campo. `string` `undefined`| `maxFileSize` `max-file-size` Define o tamanho máximo (em bytes) de cada arquivo que pode ser transferido `number` `undefined`| `maxFiles` `max-files` Define um limite para a quantidade de arquivos `number` `undefined`| `requestHeaders` `request-headers` Headers para a requisição Http `any` `undefined`| `subtitle` `subtitle` Define o subtítulo utilizado no campo de upload `string` `undefined`| `urlDelete` `url-delete` Define a URL de deleção `string` `undefined`| `urlUpload` `url-upload` Define a URL de upload `string` `undefined`| `value` -- Define o valor do campo. `EzFile[]` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezCancelWaitingChange` Emitido quando não foi possível completar a alteração entre o evento ezStartChange e ezChange. `CustomEvent<void>`| `ezChange` Emitido quando acontece a alteração de valor do campo. `CustomEvent<EzFile[]>`| `ezStartChange` Emitido ao iniciar a alteração (remover ou adicionar um arquivo). `CustomEvent<WaitingChange>` | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addFiles(files: Array<File>) => Promise<void>`

Adiciona arquivos.

##### Returns

Type: `Promise<void>`

---

#### `setBlur() => Promise<void>`

Remove o foco do campo.

##### Returns

Type: `Promise<void>`

---

#### `setFocus() => Promise<void>`

Aplica o foco no campo.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Graph

```
graph TD;
  ez-form-view --> ez-upload
  style ez-upload fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-upload--height Define a altura do componente.| --ez-upload--width Define a largura do componente.| --ez-upload\_\_icon--width Define a largura do slot que contém o ícone.| --ez-upload\_\_container--background-color Define a cor de fundo do container.| --ez-upload\_\_color--primary Define a cor de fundo do container.| --ez-upload--padding--extra-small Define os espaçamentos extra pequenos no componente.| --ez-upload--padding--small Define os espaçamentos pequenos no componente.| --ez-upload--padding--medium Define os espaçamentos médios no componente.| --ez-upload--padding--large Define os espaçamentos grandes no componente.| --ez-upload\_\_border--color Define a cor das bordas no componente.| --ez-upload--text-shadow Define as sombras dos textos do componente.| --ez-upload--text--primary Define a cor dos textos do componente.| --ez-upload--font-size Define o tamanho dos textos do componente.| --ez-upload--font-family Define a família dos textos do componente.| --ez-upload--font-weight Define o peso dos textos do componente.| --ez-upload\_\_btn\_\_cancel-image Contém o ícone de cancelamento.| --ez-upload\_\_file-icon-image Contém o ícone de arquivo. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
