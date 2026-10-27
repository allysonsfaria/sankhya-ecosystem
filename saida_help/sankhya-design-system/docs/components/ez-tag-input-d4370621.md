---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tag-input/"
titulo: "Tag Input"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-tag-input/"
trilha: "Docs > Components > Components Doc > Ez Tag Input"
---

# Tag Input

O **Tag Input** é um componente de entrada que permite aos usuários inserir e gerenciar múltiplas
opções de forma interativa. Ele é ideal para cenários onde é necessário coletar informações em forma
de tags, como categorias, palavras-chave ou outras entradas discretas.

![Imagem 1: O Tag Input é um componente de entrada que permite aos usuários inserir e gerenciar múltiplas opções de forma…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Estados Visuais

O Tag Input suporta diferentes estados visuais que podem ser definidos pela propriedade `state`.

![Imagem 2: O Tag Input suporta diferentes estados visuais que podem ser definidos pela propriedade state .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo Somente Leitura

O componente pode ser configurado para exibir apenas as tags sem permitir edição.

![Imagem 3: O componente pode ser configurado para exibir apenas as tags sem permitir edição.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Estados de Interação

Controle sobre estados desabilitados e múltiplos modos de interação.

![Imagem 4: Controle sobre estados desabilitados e múltiplos modos de interação.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Limite de Tags

É possível definir um limite máximo de tags que podem ser adicionadas.

![Imagem 5: É possível definir um limite máximo de tags que podem ser adicionadas.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Validação Customizada

O componente permite validação personalizada antes de adicionar novas tags através da propriedade `validator`.

Esta funcionalidade oferece controle total sobre quais tags são aceitas, permitindo implementar regras de
negócio específicas como:

- **Validação de formato**: Garantir que tags sigam um padrão específico (ex: emails, números, códigos)
- **Validação de conteúdo**: Bloquear palavras inadequadas ou termos específicos
- **Validação de tamanho**: Controlar o comprimento mínimo e máximo das tags
- **Validação contextual**: Usar as tags existentes para validar novas entradas

A função `validator` recebe dois parâmetros:

- `tag`: A tag que está sendo validada
- `existingTags`: Array com as tags já existentes no componente

E pode retornar:

- `true`: Tag válida, será adicionada
- `false`: Tag inválida, será rejeitada silenciosamente
- `string`: Tag inválida, será rejeitada e emitirá o evento `onEzValidationError` com a mensagem de erro

Dica

No evento onEzValidationError, você pode exibir uma mensagem de erro personalizada para o usuário. Utilizando
o próprio target passado, é possível acessar suas propriedades e métodos.

![Imagem 6: No evento onEzValidationError, você pode exibir uma mensagem de erro personalizada para o usuário. Utilizando o próprio…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Remoção de Tags

O componente oferece múltiplas formas de remover tags, garantindo uma experiência de usuário flexível e acessível:

#### Remoção com Mouse

- **Clique no ícone X**: Cada tag possui um ícone X que pode ser clicado para remoção

#### Remoção com Teclado

- **Navegação**: Use `Tab`, `Shift+Tab`, `Seta Esquerda` e `Seta Direita` para navegar entre as tags
- **Remoção**: Com uma tag selecionada, pressione `Enter`, `Backspace` ou `Delete` para removê-la
- **Remoção rápida**: Com o input vazio, pressione `Backspace` para remover a última tag

#### Controle de Comportamento

Você pode personalizar o comportamento de remoção através das seguintes propriedades:

- **`suppressBackspaceToRemove` (false por padrão)**: Define se a tecla `Backspace` deve remover a última tag quando o input está vazio
- **`suppressTagsKeyboardNavigation` (false por padrão)**: Define se a navegação por teclado pelas tags deve ser suprimida

![Imagem 7: suppressTagsKeyboardNavigation (false por padrão) : Define se a navegação por teclado pelas tags deve ser suprimida](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### ezChange

Disparado sempre que a lista de tags é alterada.

![Imagem 8: Disparado sempre que a lista de tags é alterada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezTagAdded

Disparado quando uma nova tag é adicionada.

![Imagem 9: Disparado quando uma nova tag é adicionada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezTagRemoved

Disparado quando uma tag é removida.

![Imagem 10: Disparado quando uma tag é removida.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### ezBlur e ezFocus

Disparado quando o componente perde ou ganha o foco.

![Imagem 11: Disparado quando o componente perde ou ganha o foco.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### setFocus e setBlur

Métodos para controlar programaticamente o foco do componente.

![Imagem 12: Métodos para controlar programaticamente o foco do componente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### addTag

Método para adicionar uma tag programaticamente.

![Imagem 13: Método para adicionar uma tag programaticamente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### removeTag

Método para remover uma tag específica.

![Imagem 14: Método para remover uma tag específica.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### clearTags

Método para limpar todas as tags.

![Imagem 15: Método para limpar todas as tags.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `allowDuplicates` `allow-duplicates` Define se tags duplicadas são permitidas `boolean` `false`| `enabled` `enabled` Define se o input está habilitado `boolean` `true`| `helpText` `help-text` Texto de ajuda exibido abaixo do input `string` `undefined`| `label` `label` Texto do label exibido acima do input `string` `''`| `maxTagLength` `max-tag-length` Tamanho máximo de uma tag `number` `undefined`| `maxTags` `max-tags` Número máximo de tags permitidas `number` `undefined`| `name` `name` Nome do input `string` `undefined`| `placeholder` `placeholder` Placeholder do input `string` `''`| `readonly` `readonly` Define se o input é somente leitura `boolean` `false`| `state` `state` Estado visual do componente `"default" | "error" | "success" | "warning"` `"default"`| `suppressBackspaceToRemove` `suppress-backspace-to-remove` Define se a tecla Backspace deve remover a última tag quando o input está vazio `boolean` `false`| `suppressTagsKeyboardNavigation` `suppress-tags-keyboard-navigation` Define se a navegação por teclado pelas tags deve ser suprimida `boolean` `false`| `tags` -- Array de tags iniciais `string[]` `[]`| `validator` -- Função de validação customizada para tags `(tag: string, existingTags: string[]) => string | boolean` `undefined` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezBlur` Evento disparado quando o input perde foco `CustomEvent<string[]>`| `ezChange` Evento disparado quando as tags mudam `CustomEvent<string[]>`| `ezFocus` Evento disparado quando o input recebe foco `CustomEvent<string[]>`| `ezTagAdded` Evento disparado quando uma tag é adicionada `CustomEvent<string>`| `ezTagRemoved` Evento disparado quando uma tag é removida `CustomEvent<string>`| `ezType` Emitido quando é digitado no campo de entrada `CustomEvent<string>`| `ezValidationError` Evento disparado quando uma validação falha `CustomEvent<{ tag: string; error?: string; }>` | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addTag(tag: string) => Promise<boolean>`

Adiciona uma tag programaticamente

##### Returns

Type: `Promise<boolean>`

---

#### `clearTags() => Promise<void>`

Limpa todas as tags

##### Returns

Type: `Promise<void>`

---

#### `removeTag(tag: string) => Promise<boolean>`

Remove uma tag programaticamente

##### Returns

Type: `Promise<boolean>`

---

#### `setBlur() => Promise<void>`

Remove o foco do campo

##### Returns

Type: `Promise<void>`

---

#### `setFocus(option?: OptionsSetFocus) => Promise<void>`

Aplica o foco no campo

##### Returns

Type: `Promise<void>`

### Dependencies

#### Depends on

- [ez-chip](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-chip)

#### Graph

```
graph TD;
  ez-tag-input --> ez-chip
  ez-chip --> ez-tooltip
  ez-chip --> ez-icon
  style ez-tag-input fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-tag-input--background-color Define a cor de fundo do container do input.| --ez-tag-input--border-color-default Define a cor da borda no estado padrão.| --ez-tag-input--border-color-focused Define a cor da borda no estado focado.| --ez-tag-input--border-color-error Define a cor da borda no estado de erro.| --ez-tag-input--border-color-success Define a cor da borda no estado de sucesso.| --ez-tag-input--border-color-warning Define a cor da borda no estado de aviso.| --ez-tag-input--border-radius Define o raio da borda do container.| --ez-tag-input--padding Define o espaçamento interno do container.| --ez-tag-input--gap Define o espaçamento entre tags e input.| --ez-tag-input--label-color Define a cor do texto do label.| --ez-tag-input--label-font-weight Define o peso da fonte do label.| --ez-tag-input--input-color Define a cor do texto do input.| --ez-tag-input--input-font-size Define o tamanho da fonte do input.| --ez-tag-input--placeholder-color Define a cor do placeholder.| --ez-tag-input--background-color-disabled Define a cor de fundo do input quando está desabilitado.| --ez-tag-input--helptext-color Define a cor do texto de ajuda do input. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
