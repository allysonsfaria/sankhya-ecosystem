---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popup/"
titulo: "Popup"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-popup/"
trilha: "Docs > Components > Components Doc > Ez Popup"
---

# Popup

São janelas flutuantes usadas com pequenas frases de texto, normalmente como notificação
ou aviso, e esperam uma ação do usuário para serem fechadas. O componente oferece flexibilidade
para diferentes tipos de interação e personalização, por meio de suas propriedades.

![Imagem 1: São janelas flutuantes usadas com pequenas frases de texto, normalmente como notificação ou aviso, e esperam uma ação…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Controle de exibição do cabeçalho

É possível controlar a exibição do cabeçalho através da propriedade `useHeader`.
Quando desabilitado, o título e o botão de fechar não são exibidos.

![Imagem 2: É possível controlar a exibição do cabeçalho através da propriedade useHeader . Quando desabilitado, o título e o botão…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Botões do rodapé (footerButtons)

A propriedade `footerButtons` permite adicionar até 3 botões no rodapé do popup.
Aceita todas as propriedades do componente `ez-button`, incluindo variantes,
ícones e eventos personalizados.

### Propriedades padrão por posição

O componente aplica propriedades padrão baseadas na posição do botão, que podem ser sobrescritas:

- **1º botão (índice 0)**: `variant="primary"`, `size="small"`, `label="Confirmar"`, `onClick` que fecha o popup e emite evento "OK"
- **2º botão (índice 1)**: `variant="secondary"`, `size="small"`, `label="Cancelar"`, `onClick` que fecha o popup
- **3º botão (índice 2)**: `variant="tertiary"`, `size="small"`, `label="Fechar"`, `onClick` que fecha o popup

Qualquer propriedade informada no array `footerButtons` sobrescreve as propriedades padrão correspondentes.

![Imagem 3: Qualquer propriedade informada no array footerButtons sobrescreve as propriedades padrão correspondentes.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos práticos com múltiplos botões

![Imagem 4: Exemplos práticos com múltiplos botões](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Fechamento automático (autoClose)

Controla se o popup deve fechar automaticamente ao clicar fora dele. Por padrão,
esta propriedade está habilitada (`true`), mas pode ser desabilitada quando
for necessário forçar o usuário a utilizar os botões para fechar.

![Imagem 5: Controla se o popup deve fechar automaticamente ao clicar fora dele. Por padrão, esta propriedade está habilitada (…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações de largura

O popup oferece diferentes tamanhos predefinidos através da propriedade `size`:
x-small, small, medium, large, x-large e auto.

![Imagem 6: O popup oferece diferentes tamanhos predefinidos através da propriedade size : x-small, small, medium, large, x-large e…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações de altura

A propriedade `heightMode` controla como a altura do popup é calculada:
`auto` ajusta ao conteúdo ou `full` ocupa toda a altura da tela.

![Imagem 7: A propriedade heightMode controla como a altura do popup é calculada: auto ajusta ao conteúdo ou full ocupa toda a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Barra de rolagem vertical

Quando o conteúdo excede a altura disponível, é possível habilitar a barra
de rolagem vertical através da propriedade `enabledScroll`.

![Imagem 8: Quando o conteúdo excede a altura disponível, é possível habilitar a barra de rolagem vertical através da propriedade…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Eventos do componente

O popup emite eventos quando é fechado, permitindo que a aplicação responda
adequadamente às ações do usuário.

![Imagem 9: O popup emite eventos quando é fechado, permitindo que a aplicação responda adequadamente às ações do usuário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Considerações de usabilidade

- Use popups para confirmações rápidas ou informações que não interrompam o fluxo principal
- Prefira `autoClose={false}` quando a ação for crítica e requerer confirmação explícita
- Limite o uso de três botões no rodapé para manter a interface limpa
- Utilize variantes apropriadas nos botões: `primary` para ação principal, `secondary` para alternativas e `tertiary` para ações de cancelamento
- **Aproveite as propriedades padrão**: para casos simples, você pode usar arrays vazios `[{}, {}, {}]` no `footerButtons` para obter botões com configuração padrão
- **Override seletivo**: sobrescreva apenas as propriedades que precisam ser diferentes dos padrões (ex: apenas o `label` ou `onClick`)
- O primeiro botão sempre tem `variant="primary"` por padrão, seguindo convenções de UX para ação principal

## Slots

O **Popup** disponibiliza os seguintes slots para personalização:

- **footer**: Permite adicionar conteúdo personalizado adicional no rodapé do popup. O conteúdo
  do slot é posicionado à esquerda dos botões configurados pela propriedade `footerButtons`, permitindo
  adicionar informações extras ou elementos complementares sem substituir os botões existentes.

![Imagem 10: footer : Permite adicionar conteúdo personalizado adicional no rodapé do popup. O conteúdo do slot é posicionado à…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `autoClose` `auto-close` Define se o popup deve fechar automaticamente ao clicar fora dele. `boolean` `true`| `enabledScroll` `enabled-scroll` Possibilita scroll vertical no conteúdo interno do componente `boolean` `true`| `ezTitle` `ez-title` Texto a ser apresentado como título do componente. `string` `undefined`| `footerButtons` -- Botões do rodapé do popup. Aceita todas as propriedades do ez-button. Limitado a até 3 botões. `Partial<EzButtonProps>[]` `[]`| `heightMode` `height-mode` Define altura do componente. `"auto" | "full"` `"full"`| `opened` `opened` Define se o ez-popover está aberto. `boolean` `false`| `size` `size` Define a largura do ez-popup. `"auto" | "large" | "medium" | "small" | "x-large" | "x-small"` `"medium"`| `useHeader` `use-header` Define se o componente utilizará cabeçalho. `boolean` `true` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezClosePopup` Evento emitido ao clicar no botão de fechar (onEzClosePopup). `CustomEvent<any>`| `ezPopupAction` Evento emitido ao clicar no botão de fechar (ezPopupAction = OK) `CustomEvent<string>` | | | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-link-builder](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-link-builder)
- [ez-simple-image-uploader](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-rich-text/ez-simple-image-uploader)

#### Depends on

- [ez-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-button)

#### Graph

```
graph TD;
  ez-popup --> ez-button
  ez-button --> ez-icon
  ez-link-builder --> ez-popup
  ez-simple-image-uploader --> ez-popup
  style ez-popup fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-popup-z-index Define a camada em que o componente será exibido.| --ez-popup\_\_container--color Define a cor do texto do container do popup.| --ez-popup\_\_container--padding Define o espaçamento do container do popup.| --ez-popup\_\_title--font-family Define a família da fonte do título do popup.| --ez-popup\_\_title--font-size Define o tamanho da fonte do título do popup.| --ez-popup\_\_title--color Define a cor da fonte do título do popup.| --ez-popup\_\_title--font-weight Define o peso da fonte do título do popup. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
