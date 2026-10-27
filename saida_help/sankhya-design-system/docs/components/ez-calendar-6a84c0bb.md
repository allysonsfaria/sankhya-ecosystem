---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-calendar/"
titulo: "Calendar"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-calendar/"
trilha: "Docs > Components > Components Doc > Ez Calendar"
---

# Calendar

Documentação do componente EzCalendar.

![Imagem 1: Documentação do componente EzCalendar.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Com horas e minutos

Exibe as horas e minutos no calendário.

![Imagem 2: Exibe as horas e minutos no calendário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Com segundos

Exibe os segundos no calendário.

![Imagem 3: Exibe os segundos no calendário.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Modo floating

No modo floating o calendário só se tornará visível quando o método show() for acionado.

![Imagem 4: No modo floating o calendário só se tornará visível quando o método show() for acionado.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Principais métodos

#### show()

Faz com que o componente seja exibido quando utilizado no modo floating.

É possível determinar ajustes de posicionamento através dos parâmetros:

- top;
- left;
- bottom;
- right.

Esses parâmetros devem ser informados como strings no formato css.

![Imagem 5: Esses parâmetros devem ser informados como strings no formato css.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### fitVertical()

Usado no modo floating. Método necessário para ajustar o posicionamento do calendar acima ou abaixo do elemento pai conforme a disponibilidade de espaço.

É possível determinar ajustes de posicionamento através dos parâmetros:

- topOffset;
- bottomOffset.

Esses parâmetros devem ser informados como number.

![Imagem 6: Esses parâmetros devem ser informados como number.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### hide()

Faz com que o componente seja ocultado quando utilizado no modo floating.

Observação

No exemplo abaixo, ao clicar no botão **Mostrar Calendário**,
o calendário será exibido, após 2 segundos será chamado o médodo **hide()**,
e então ele será ocultado automaticamente.

![Imagem 7: No exemplo abaixo, ao clicar no botão Mostrar Calendário , o calendário será exibido, após 2 segundos será chamado o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Exemplos de eventos

#### ezChange()

Quando o usuário escolhe uma data, esse evento é emitido.

![Imagem 8: Quando o usuário escolhe uma data, esse evento é emitido.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `floating` `floating` Define se a exibição do ez-calendar será feita pelos métodos `show()` e `hide()`. `boolean` `false`| `showSeconds` `show-seconds` Se true a data considera segundos. Deve ser usado em conjunto com a propriedade `time`. `boolean` `false`| `time` `time` Se true a data considera horas e minutos. `boolean` `false`| `value` -- Define o valor do calendário. `Date` `new Date()` | | | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezChange` Emitido quando acontece a alteração de valor do calendário. `CustomEvent<Date>` | | | | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- |

### Methods

#### `fitHorizontal(rightOffset: number) => Promise<void>`

Ajusta o posicionamento horizontal do ez-calendar conforme a disponibilidade de espaço.

##### Returns

Type: `Promise<void>`

---

#### `fitVertical(topOffset: number, bottomOffset: number) => Promise<void>`

Ajusta o posicionamento vertical do ez-calendar conforme a disponibilidade de espaço.

##### Returns

Type: `Promise<void>`

---

#### `hide() => Promise<void>`

Oculta o ez-calendar.

##### Returns

Type: `Promise<void>`

---

#### `show(top?: string, left?: string, bottom?: string, right?: string) => Promise<void>`

Exibe o ez-calendar em uma posição determinada.
É possível determinar o posicionamento através dos parâmetros, no formato css.

##### Returns

Type: `Promise<void>`

### Dependencies

#### Used by

- [ez-date-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-input)
- [ez-date-time-input](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-date-time-input)

#### Graph

```
graph TD;
  ez-date-input --> ez-calendar
  ez-date-time-input --> ez-calendar
  style ez-calendar fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-calendar--font-family Define a família da fonte do componente.| --ez-calendar--color Define a cor dos textos dentro do componente.| --ez-calendar--text-shadow Define a sombra dos textos dentro do componente.| --ez-calendar\_\_body--background-color Define a cor de fundo do corpo do calendário.| --ez-calendar\_\_time--background-color Define a cor de fundo do corpo da hora do calendário.| --ez-calendar\_\_body--padding Define o espaçamento do corpo do calendário.| --ez-calendar\_\_body--border-radius Define o raio da borda do corpo do calendário.| --ez-calendar\_\_body--shadow Define a sombra do corpo do calendário.| --ez-container--z-index Define a posição do container de calendario nas camadas da página .| --ez-calendar\_\_header-line--stroke Define a espessura da borda inferior do header.| --ez-calendar\_\_header-line--color Define a cor da borda inferior do header.| --ez-calendar\_\_nav-btn--fill Define a cor do ícone de navegação.| --ez-calendar\_\_nav-btn--hover--fill Define a cor do ícone de navegação quando o cursor está sobre ele.| --ez-calendar\_\_nav-btn--width Define a largura do ícone de navegação.| --ez-calendar\_\_nav-btn--height Define a altura do ícone de navegação.| --ez-calendar\_\_nav-btn--previous-image Contém a imagem do ícone de navegação à esquerda.| --ez-calendar\_\_nav-btn--next-image Contém a imagem do ícone de navegação à direita.| --ez-calendar\_\_cell--margin Define o espaçamento vertical entre as células.| --ez-calendar\_\_cell--width Define a largura das células.| --ez-calendar\_\_cell--padding Define o espaçamento horizontal entre as células.| --ez-calendar\_\_cell--border-radius Define o raio da borda das células.| --ez-calendar\_\_cell--over--background-color Define a cor de fundo das células.| --ez-calendar\_\_cell--over--color Define a cor de do texto das células.| --ez-calendar\_\_cell--outset--color Define a cor do texto para células secundárias (fora do mês selecionado).| --ez-calendar\_\_cell--selected--background-color Define a cor de fundo das células selecionadas.| --ez-calendar\_\_cell--selected--color Define a cor do texto da célula selecionada.| --ez-calendar\_\_btn-today--color Define a cor do texto do botão "Hoje".| --ez-calendar\_\_btn-today--hover--background-color Define a cor de fundo do botão "Hoje" quando o cursor está sobre ele.| --ez-calendar\_\_btn-today--border-radius Define o raio da borda do botão "Hoje". | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
