---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter/"
titulo: "Filter"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-filter/"
trilha: "Docs > Components > Components Doc > Ez Filter"
---

# Filter

O **Filter** (`ez-filter`) é um painel lateral de filtros agnóstico ao contexto de negócio.
Ele gera os campos automaticamente a partir da metadata do core (via `DataUnit`), coleta e
valida os valores preenchidos e emite eventos de aplicação, limpeza e remoção — deixando a
aplicação efetiva do filtro (ex.: `dataUnit.loadData(...)`) por conta do consumidor.

![Imagem 1: O Filter ( ez-filter ) é um painel lateral de filtros agnóstico ao contexto de negócio. Ele gera os campos…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações

### Modo de interação

A propriedade `interactionMode` define como o painel se relaciona com o conteúdo principal.

- `overlay` (padrão): o painel é fixo e sobrepõe o conteúdo, sem alterar o layout da página.
- `push`: o painel ocupa espaço no fluxo, deslocando (empurrando) o conteúdo irmão.

![Imagem 2: push : o painel ocupa espaço no fluxo, deslocando (empurrando) o conteúdo irmão.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Seleção e ordem dos campos

A propriedade `fields` permite escolher quais campos exibir e em que ordem, além de sobrescrever
`label` e `required`. Quando ausente, todos os campos visíveis da metadata são apresentados.

![Imagem 3: A propriedade fields permite escolher quais campos exibir e em que ordem, além de sobrescrever label e required .…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Valores iniciais

Utilize `initialValues` para pré-preencher os filtros no formato `{ nomeDoCampo: valor }`.

![Imagem 4: Utilize initialValues para pré-preencher os filtros no formato { nomeDoCampo: valor } .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Título e rótulos dos botões

Personalize o cabeçalho e os botões do rodapé com `panelTitle`, `applyButtonLabel` e
`clearButtonLabel`. Quando omitidos, os textos padrão do componente são utilizados.

![Imagem 5: Personalize o cabeçalho e os botões do rodapé com panelTitle , applyButtonLabel e clearButtonLabel . Quando omitidos,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Backdrop (scrim)

No modo `overlay`, `showScrim` controla a exibição do fundo escurecido e `closeOnScrimClick`
define se o clique nele fecha o painel.

![Imagem 6: No modo overlay , showScrim controla a exibição do fundo escurecido e closeOnScrimClick define se o clique nele fecha o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos

### Evento ezApplyFilter

Emitido ao aplicar os filtros (após a validação). O detalhe contém `values`, um mapa
`nomeDoCampo` → `valor` apenas com os filtros preenchidos.

![Imagem 7: Emitido ao aplicar os filtros (após a validação). O detalhe contém values , um mapa nomeDoCampo → valor apenas com os…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Evento ezChange

Emitido a cada alteração de valor de um campo, **uma única vez por mudança** e sempre com o detalhe
`{ fieldName, value }` preenchido. O contador do exemplo evidencia que não há disparos duplicados
nem eventos vazios.

![Imagem 8: Emitido a cada alteração de valor de um campo, uma única vez por mudança e sempre com o detalhe { fieldName, value }…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Eventos ezClearFilter e ezRemoveFilter

`ezClearFilter` é disparado ao limpar todos os filtros. `ezRemoveFilter` é disparado ao remover
um filtro específico, trazendo `{ fieldName }` no detalhe.

![Imagem 9: ezClearFilter é disparado ao limpar todos os filtros. ezRemoveFilter é disparado ao remover um filtro específico,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Eventos ezOpen e ezClose

Disparados quando o painel é aberto e fechado, respectivamente.

![Imagem 10: Disparados quando o painel é aberto e fechado, respectivamente.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos

### open, close e toggle

Controlam a abertura do painel de forma programática.

![Imagem 11: Controlam a abertura do painel de forma programática.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### apply e validate

`validate()` verifica os campos obrigatórios e o validador customizado. `apply()` valida e,
quando válido, emite `ezApplyFilter`. Ambos retornam `Promise<boolean>`.

Importante

`apply()` só emite `ezApplyFilter` quando a validação passa. Campos obrigatórios não preenchidos
bloqueiam a aplicação e o método resolve para `false`.

![Imagem 12: apply() só emite ezApplyFilter quando a validação passa. Campos obrigatórios não preenchidos bloqueiam a aplicação e o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### getValues

Retorna os valores atuais dos filtros preenchidos no formato `Promise<{ [fieldName]: valor }>`.

![Imagem 13: Retorna os valores atuais dos filtros preenchidos no formato Promise<{ (fieldName): valor }> .](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### setFieldValue, removeFilter e clear

`setFieldValue(nome, valor)` altera o valor de um filtro; `removeFilter(nome)` limpa um campo e
emite `ezRemoveFilter`; `clear()` esvazia o valor de cada campo e emite `ezClearFilter`.

Observação

`clear()` **esvazia** os campos: mesmo com `initialValues` definidos, `getValues()` passa a retornar
um objeto vazio após a limpeza — os valores iniciais não são restaurados.

![Imagem 14: clear() esvazia os campos: mesmo com initialValues definidos, getValues() passa a retornar um objeto vazio após a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### registerCustomField

Adiciona ao painel um campo que não existe na metadata padrão do core. O campo é registrado como
`standAlone` no `DataUnit` e participa normalmente da coleta, limpeza e validação dos filtros.
Cada campo registrado aparece **imediatamente** no painel — inclusive quando apenas um é registrado.

![Imagem 15: Adiciona ao painel um campo que não existe na metadata padrão do core. O campo é registrado como standAlone no DataUnit…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

Painel lateral de filtros, **agnóstico ao contexto de negócio**. Oferece uma estrutura flexível e
reutilizável para montar filtros, gerando os campos automaticamente a partir da **metadata do core**
(`UnitMetadata` via `DataUnit`) — o mesmo motor usado pelo `ez-form` (`buildFormMetadata` +
`ez-form-view` + `DataBinder`).

O componente cuida de **estrutura, comportamento e coleta/validação de valores**. Ele **emite eventos**
de aplicação/remoção/limpeza; a tradução dos valores para `Filter`/`QuickFilter` e a aplicação efetiva
(ex.: `dataUnit.loadData(...)`) ficam por conta do consumidor, mantendo a biblioteca sem regra de negócio.

### Modos de interação

- **`overlay`** (padrão): o painel é fixo e sobrepõe o conteúdo da página (com backdrop/scrim opcional),
  sem alterar o layout.
- **`push`**: o painel ocupa espaço no fluxo, deslocando (empurrando) o conteúdo irmão. Nesse modo,
  posicione o `ez-filter` num container flex/grid ao lado do conteúdo principal.

### Uso

```
// React (@sankhyalabs/react-ezui)
<EzFilter
  ref={filterRef}
  interactionMode="push"
  metadata={unitMetadata}                 // metadata do core
  fields={[{ name: "NOMEPARC" }, { name: "DATANEG", required: true }]}
  initialValues={{ ATIVO: "S" }}
  onEzApplyFilter={(e) => aplicarFiltros(e.detail.values)}
  onEzClearFilter={() => limparFiltros()}
/>;

// Abrir/fechar e alterar valores por método
await filterRef.current.open();
await filterRef.current.setFieldValue("NOMEPARC", "Sankhya");
const valores = await filterRef.current.getValues();
```

```
<!-- HTML puro: DataUnit já carregado é passado via propriedade -->
<ez-filter id="meuFiltro" interaction-mode="overlay"></ez-filter>
<script>
  const el = document.querySelector("#meuFiltro");
  el.dataUnit = meuDataUnit;               // com metadata do core já carregada
  el.addEventListener("ezApplyFilter", (e) => console.log(e.detail.values));
  el.open();
</script>
```

### Campos customizados

Campos que não existem na metadata padrão podem ser adicionados como campos `standAlone`, participando
normalmente da coleta de valores, limpeza e validação:

```
await filterRef.current.registerCustomField({
  name: "FAIXA_PRECO",
  label: "Faixa de preço",
  userInterface: UserInterface.DECIMALNUMBER,
  required: false,
});
```

Para conteúdo totalmente livre (fora do fluxo de valores/validação), há o slot `custom-fields` como
escape hatch.

### Overview

Painel lateral de filtros, agnóstico ao contexto de negócio.

Gera os campos automaticamente a partir da metadata do core (`UnitMetadata` via `DataUnit`),
reutilizando o mesmo motor de dados do formulário (`buildFormMetadata` + `ez-form-view` + `DataBinder`).

O componente é responsável apenas por estrutura, comportamento e coleta/validação de valores:
ele **emite eventos** de aplicação/remoção/limpeza, deixando a tradução para `Filter`/`QuickFilter`
e a aplicação efetiva (ex.: `dataUnit.loadData(...)`) por conta do consumidor.

### Properties

| Property Attribute Description Type Default| `applyButtonLabel` `apply-button-label` Rótulo do botão de aplicar filtros. `string` `undefined`| `applyOnEnter` `apply-on-enter` Aplica os filtros ao pressionar `Enter` com o painel aberto. `boolean` `true`| `clearButtonLabel` `clear-button-label` Rótulo do botão de limpar filtros. `string` `undefined`| `closeOnEsc` `close-on-esc` Fecha o painel ao pressionar `Esc`. `boolean` `true`| `closeOnScrimClick` `close-on-scrim-click` Fecha o painel ao clicar no backdrop (modo `overlay`). `boolean` `true`| `dataUnit` -- Unidade de dados que controla os valores e a metadata dos filtros. Quando ausente, o componente cria uma instância interna. `DataUnit` `undefined`| `fields` -- Seleção, ordem e sobrescrita (label, obrigatoriedade, valor padrão) dos campos. Quando ausente, todos os campos visíveis da metadata são apresentados. `IFieldConfig[]` `undefined`| `initialValues` -- Valores iniciais dos filtros, no formato `{ nomeDoCampo: valor }`. `{ [fieldName: string]: any; }` `undefined`| `interactionMode` `interaction-mode` Define como o painel interage com o conteúdo principal. - `overlay`: sobrepõe o conteúdo, sem alterar o layout da página. - `push`: ocupa espaço no fluxo, deslocando (empurrando) o conteúdo irmão. `"overlay" | "push"` `"overlay"`| `metadata` -- Metadata do core usada para gerar os campos. Alternativa a fornecer um `dataUnit` já carregado. `UnitMetadata` `undefined`| `opened` `opened` Define se o painel está aberto. `boolean` `false`| `panelTitle` `panel-title` Título exibido no cabeçalho do painel. `string` `undefined`| `recordValidator` -- Validador customizado responsável pela integridade dos filtros. `IRecordValidator` `undefined`| `showScrim` `show-scrim` Exibe o backdrop (scrim) no modo `overlay`. `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezApplyFilter` Emitido ao aplicar os filtros (após a validação). `CustomEvent<IFilterChange>`| `ezChange` Emitido quando o valor de um campo do filtro é alterado. `CustomEvent<{ fieldName: string; value: any; }>`| `ezClearFilter` Emitido ao limpar todos os filtros. `CustomEvent<void>`| `ezClose` Emitido quando o painel é fechado. `CustomEvent<void>`| `ezOpen` Emitido quando o painel é aberto. `CustomEvent<void>`| `ezRemoveFilter` Emitido ao remover um filtro específico. `CustomEvent<{ fieldName: string; }>` | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Methods

#### `addCustomEditor(fieldName: string, editor: ICustomEditor) => Promise<void>`

Registra um editor customizado para um campo já existente na metadata.

##### Returns

Type: `Promise<void>`

---

#### `apply() => Promise<boolean>`

Valida e, quando válido, emite `ezApplyFilter` com os valores atuais.

##### Returns

Type: `Promise<boolean>`

`true` quando aplicado; `false` quando bloqueado pela validação.

---

#### `clear() => Promise<void>`

Limpa todos os filtros (esvazia o valor de cada campo) e emite `ezClearFilter`.

##### Returns

Type: `Promise<void>`

---

#### `close() => Promise<void>`

Fecha o painel de filtros.

##### Returns

Type: `Promise<void>`

---

#### `getValues() => Promise<{ [fieldName: string]: any; }>`

Retorna os valores atuais dos filtros preenchidos.

##### Returns

Type: `Promise<{ [fieldName: string]: any; }>`

Mapa `nomeDoCampo` → `valor`.

---

#### `open() => Promise<void>`

Abre o painel de filtros.

##### Returns

Type: `Promise<void>`

---

#### `registerCustomField(field: IFilterCustomField) => Promise<void>`

Adiciona um campo customizado que não existe na metadata padrão do core.

##### Returns

Type: `Promise<void>`

---

#### `removeFilter(fieldName: string) => Promise<void>`

Remove um filtro específico (limpa seu valor) e emite `ezRemoveFilter`.

##### Returns

Type: `Promise<void>`

---

#### `setFieldValue(fieldName: string, value: any) => Promise<void>`

Altera o valor de um filtro.

##### Returns

Type: `Promise<void>`

---

#### `toggle() => Promise<void>`

Alterna o estado de abertura do painel.

##### Returns

Type: `Promise<void>`

---

#### `validate() => Promise<boolean>`

Valida os filtros (campos obrigatórios e validador customizado).

##### Returns

Type: `Promise<boolean>`

`true` quando válido; `false` caso contrário.

### Shadow Parts

| Part Description| `"body"` | `"footer"` | `"header"` | `"panel"` | `"scrim"` | `"title"`  | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Depends on

- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)
- [ez-form-view](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-form-view)

#### Graph

```
graph TD;
  ez-filter --> ez-button
  ez-filter --> ez-form-view
  ez-button --> ez-icon
  ez-form-view --> ez-custom-form-input
  ez-form-view --> ez-collapsible-box
  ez-form-view --> ez-check
  ez-form-view --> ez-combo-box
  ez-form-view --> ez-date-input
  ez-form-view --> ez-time-input
  ez-form-view --> ez-date-time-input
  ez-form-view --> ez-upload
  ez-form-view --> ez-number-input
  ez-form-view --> ez-text-area
  ez-form-view --> ez-text-input
  ez-form-view --> ez-search-plus
  ez-form-view --> ez-search
  ez-form-view --> ez-rich-text
  ez-form-view --> ez-multi-select-input
  ez-collapsible-box --> ez-icon
  ez-collapsible-box --> ez-text-edit
  ez-text-edit --> ez-text-input
  ez-text-edit --> ez-button
  ez-text-input --> ez-tooltip
  ez-text-input --> ez-icon
  ez-combo-box --> ez-text-input
  ez-combo-box --> ez-icon
  ez-combo-box --> ez-popover-plus
  ez-combo-box --> ez-combo-box-list
  ez-popover-plus --> ez-popover-core
  ez-date-input --> ez-text-input
  ez-date-input --> ez-popover-plus
  ez-date-input --> ez-calendar
  ez-time-input --> ez-text-input
  ez-time-input --> ez-icon
  ez-date-time-input --> ez-text-input
  ez-date-time-input --> ez-popover-plus
  ez-date-time-input --> ez-calendar
  ez-number-input --> ez-text-input
  ez-text-area --> ez-tooltip
  ez-text-area --> ez-icon
  ez-search-plus --> ez-icon
  ez-search-plus --> ez-text-input
  ez-search-plus --> ez-popover-plus
  ez-search-plus --> ez-search-result-list
  ez-search-result-list --> ez-card-item
  ez-search-result-list --> ez-skeleton
  ez-search --> ez-text-input
  ez-search --> ez-icon
  ez-search --> ez-popover-plus
  ez-search --> search-list
  search-list --> ez-card-item
  ez-rich-text --> ez-text-area
  ez-rich-text --> ez-rich-toolbar
  ez-rich-text --> ez-link-builder
  ez-rich-text --> ez-simple-image-uploader
  ez-rich-toolbar --> ez-rich-toolbar-arrows
  ez-rich-toolbar --> ez-rich-toolbar-letters
  ez-rich-toolbar --> ez-rich-toolbar-configs
  ez-rich-toolbar-arrows --> ez-rich-toolbar-item
  ez-rich-toolbar-item --> ez-icon
  ez-rich-toolbar-letters --> ez-rich-toolbar-item
  ez-rich-toolbar-configs --> ez-rich-toolbar-item
  ez-link-builder --> ez-popup
  ez-link-builder --> ez-modal-container
  ez-link-builder --> ez-text-input
  ez-link-builder --> ez-check
  ez-popup --> ez-button
  ez-modal-container --> ez-icon
  ez-modal-container --> ez-button
  ez-simple-image-uploader --> ez-popup
  ez-simple-image-uploader --> ez-modal-container
  ez-simple-image-uploader --> ez-tooltip
  ez-simple-image-uploader --> ez-text-input
  ez-simple-image-uploader --> ez-icon
  ez-multi-select-input --> ez-icon
  ez-multi-select-input --> ez-tooltip
  ez-multi-select-input --> ez-popover-core
  ez-multi-select-input --> ez-multi-selection-list
  ez-multi-selection-list --> ez-check
  ez-multi-selection-list --> ez-list
  ez-multi-selection-list --> ez-icon
  ez-multi-selection-list --> multi-selection-box-message
  ez-multi-selection-list --> ez-filter-input
  ez-multi-selection-list --> ez-search
  ez-list --> ez-check
  ez-filter-input --> ez-text-input
  ez-filter-input --> ez-icon
  style ez-filter fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-filter--width Define a largura do painel de filtros.| --ez-filter--background-color Define a cor de fundo do painel.| --ez-filter--padding Define o espaçamento interno do cabeçalho, corpo e rodapé.| --ez-filter--border-radius Define o raio da borda do painel (aplicado aos cantos direitos).| --ez-filter--z-index Define a camada de exibição do painel no modo overlay.| --ez-filter--transition-duration Define a duração da transição de abertura/fechamento.| --ez-filter--transition-timing Define a curva de aceleração da transição de abertura/fechamento.| --ez-filter--scrim-color Define a cor do backdrop (scrim) no modo overlay.| --ez-filter--scrim-blur Define o desfoque do backdrop (scrim) no modo overlay.| --ez-filter--box-shadow Define a sombra do painel no modo overlay.| --ez-filter--title-color Define a cor do título do painel.| --ez-filter--title-font-size Define o tamanho da fonte do título do painel.| --ez-filter--divider-color Define a cor da borda que separa cabeçalho e rodapé do corpo.| --ez-filter--header-gap Define o espaçamento entre os itens do cabeçalho.| --ez-filter--footer-gap Define o espaçamento entre os botões do rodapé. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
