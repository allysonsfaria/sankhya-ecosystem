---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/"
titulo: "Rich Text"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/"
trilha: "Docs > Components > Components Doc > Ez Rich Text"
---

# Rich Text

O `ez-rich-text` possibilita ao usuário, criar um conteúdo HTML permitindo não apenas sua edição, mas também sua pré-visualização.

![Imagem 1: O ez-rich-text possibilita ao usuário, criar um conteúdo HTML permitindo não apenas sua edição, mas também sua…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Dica

Disponibilizamos alguns atalhos de teclado para deixar a navegação e usabilidade do componente mais fluida:

- **Pré visualizar**: `Ctrl` + `P`
- **Desfazer**: `Ctrl` + `Z`
- **Refazer**: `Ctrl` + `X`
- **Negrito**: `Ctrl` + `B`
- **Itálico**: `Ctrl` + `I`
- **Sublinhado**: `Ctrl` + `U`
- **Lista**: `Ctrl` + `L`
- **Inserir imagem**: `Ctrl` + `O`
- **Inserir link**: `Ctrl` + `K`
- **Quebra de linha**: `Ctrl` + `ENTER`

## Desabilitando Funcionalidades

Por padrão, todas as funcionalidades estão disponíveis no componente. Porém, para permitir uma maior customização e
flexibilidade de uso, permitimos que grupos de funcionalidades possam ser desabilitadas programaticamente, conforme a necessidade,
através de suas propriedades.

### Modo de pré-visualização

> Propriedade utilizada: `showPreview = false`.

Desabilita a funcionalidade de modo de pré-visualização.

![Imagem 2: Desabilita a funcionalidade de modo de pré-visualização.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desfazer e refazer

> Propriedade utilizada: `showUndoRedo = false`.

Desabilita da taskbar, as funcionalidades de desfazer e refazer.

![Imagem 3: Desabilita da taskbar, as funcionalidades de desfazer e refazer .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Formatação de texto

> Propriedade utilizada: `showTextFormat = false`.

Desabilita as funcionalidades de formatação em negrito, sublinhado e itálico.

![Imagem 4: Desabilita as funcionalidades de formatação em negrito , sublinhado e itálico .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Opções diversas

> Propriedade utilizada: `showConfigs = false`.

Desabilita as funcionalidades de formatar lista, inserir imagem e inserir link.

![Imagem 5: Desabilita as funcionalidades de formatar lista , inserir imagem e inserir link .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Desabilitando edição

> Propriedade utilizada: `enabled = false`.

Desabilita a edição do elemento, por padrão, todas as funcionalidades são desabilitadas, exceto o modo de **pré-visualização**.

![Imagem 6: Desabilita a edição do elemento, por padrão, todas as funcionalidades são desabilitadas, exceto o modo de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### ezChange

Emitido sempre que há uma mudança na propriedade `value` do componente.

![Imagem 7: Emitido sempre que há uma mudança na propriedade value do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### Aplicar foco e blur

> Métodos usados: `setFocus` e `setBlur`.

![Imagem 8: Métodos usados: setFocus e setBlur .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

Dica

O método `setFocus` sempre irá definir o `rich-text` para o modo de **edição**, para que consiga focar no `text-area`.

### Verificar se campo está inválido

> Método usado: `isInvalid`.

Este método retorna `true` caso haja uma mensagem de erro atribuída ao componente.

É bastante útil para validações em formulários, onde são necessários alguns pré-requisitos para validar uma informação.

![Imagem 9: É bastante útil para validações em formulários, onde são necessários alguns pré-requisitos para validar uma informação.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
