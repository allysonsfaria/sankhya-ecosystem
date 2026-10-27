---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-collapsible-box/"
titulo: "CollapsibleBox"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-collapsible-box/"
trilha: "Docs > Components > Components Doc > Ez Collapsible Box"
---

# CollapsibleBox

Documentação do componente EzCollapsibleBox.

![Imagem 1: Documentação do componente EzCollapsibleBox.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Tamanho x-small

![Imagem 2: Tamanho x-small](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho small (default)

![Imagem 3: Tamanho small (default)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho medium

![Imagem 4: Tamanho medium](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho large

![Imagem 5: Tamanho large](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Slot para posiconamento de itens a direita

![Imagem 6: Slot para posiconamento de itens a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Tamanho x-large

![Imagem 7: Tamanho x-large](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícone a esquerda (default)

![Imagem 8: Ícone a esquerda (default)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Ícone a direita

![Imagem 9: Ícone a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Conteúdo do cabeçalho alinhado a esquerda (default)

![Imagem 10: Conteúdo do cabeçalho alinhado a esquerda (default)](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Título do conteúdo

![Imagem 11: Título do conteúdo](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Conteúdo do cabeçalho alinhado a direita

![Imagem 12: Conteúdo do cabeçalho alinhado a direita](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Conteúdo do cabeçalho alinhado ao centro

![Imagem 13: Conteúdo do cabeçalho alinhado ao centro](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Conteúdo do cabeçalho ocupando todo espaço disponível

![Imagem 14: Conteúdo do cabeçalho ocupando todo espaço disponível](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Componente com borda

![Imagem 15: Componente com borda](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### showHide()

Esconde ou revela o conteúdo do componente.

![Imagem 16: Esconde ou revela o conteúdo do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange()

Evento disparado ao mudar o estado do componente (onEzChange).

![Imagem 17: Evento disparado ao mudar o estado do componente (onEzChange).](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `boxBordered` `box-bordered` Define seu o componente deve ter borda `boolean` `false`| `conditionalSave` -- Define uma condição para salvar ou não uma alteração. `Function` `undefined`| `editable` `editable` Se true mostra o ícone para edição do componente. `boolean` `false`| `headerAlign` `header-align` Define a posição do conteúdo do cabeçalho do componente. `"center" | "left" | "right" | "stretch"` `"left"`| `headerSize` `header-size` Define o tamanho do texto e do ícone. `"large" | "medium" | "small" | "x-large" | "x-small"` `"small"`| `iconPlacement` `icon-placement` Define o posicionamento do ícone. `"left" | "right"` `"left"`| `label` `label` Texto a ser apresentado como título do componente. `string` `undefined`| `removable` `removable` Se true mostra o ícone para remoção do componente. `boolean` `false`| `subtitle` `subtitle` Texto a ser apresentado como subtítulo do componente. `string` `undefined`| `value` `value` Define o valor do componente. `boolean` `false` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do componente. `CustomEvent<boolean>`| `ezEditLabelMode` Emitido quando o modo de edição da label for aberto e fechado (onEzEditLabelMode). `CustomEvent<boolean>`| `ezRemove` Emitido ao remover o componente (onEzRemove). `CustomEvent<EzCollapsibleBox>`| `ezSaveEditLabel` Emitido ao concluir edição da label (onEzSaveEditLabel). `CustomEvent<CustomEvent<any>>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `applyFocusTextEdit() => Promise<void>`

Aplica o foco no campo de edição de título.

##### Returns

Type: `Promise<void>`

---

#### `cancelEdition() => Promise<void>`

Cancela a edição de título.

##### Returns

Type: `Promise<void>`

---

#### `showHide() => Promise<void>`

Oculta/mostra o conteúdo do ez-collapsible-box.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Depends on

- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)
- [ez-text-edit](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-text-edit)

#### Graph

```
graph TD;
  ez-collapsible-box --> ez-icon
  ez-collapsible-box --> ez-text-edit
  ez-text-edit --> ez-text-input
  ez-text-edit --> ez-button
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-button --> ez-icon
  ez-form-view --> ez-collapsible-box
  style ez-collapsible-box fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-collapsible-box--font-size Define o tamanho da fonte do header.| --ez-collapsible-box--font-family Define a família da fonte do header.| --ez-collapsible-box--font-weight Define o peso da fonte do header.| --ez-collapsible-box--color Define a cor da fonte do header.| --ez-collapsible-box--subtitle--font-size Define o tamanho da fonte do header.| --ez-collapsible-box--subtitle--font-family Define a família da fonte do header.| --ez-collapsible-box--subtitle--font-weight Define o peso da fonte do header.| --ez-collapsible-box--subtitle--color Define a cor da fonte do header.| --ez-collapsible-box--subtitle--margin-bottom Define a cor da fonte do header.| --ez-collapsible-box--focus--color Define a cor do texto e do ícone quando o componente está focado.| --ez-collapsible-box\_\_icon--color Define a cor do chevron.| --ez-collapsible-box\_\_header--padding-top Define o espaçamento superior ao header.| --ez-collapsible-box\_\_header--padding-bottom Define o espaçamento inferior ao header.| --ez-collapsible-box\_\_header--padding-right Define o espaçamento à direita do header.| --ez-collapsible-box\_\_header--padding-left Define o espaçamento à esquerda do header. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
