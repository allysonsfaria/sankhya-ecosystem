---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown/"
titulo: "Dropdown"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown/"
trilha: "Docs > Components > Components Doc > Ez Dropdown"
---

# Dropdown

Documentação do componente EzDropdown.

Importante

O componente **EzDropdown** não possui a capacidade de gerenciar a visibilidade do nível principal.
Sua função é controlar somente os subníveis, portanto, é o componente pai ou o programador que é responsável
por determinar se o dropdown será exibido na tela ou não. Para realizar esse controle de visibilidade,
nos exemplos a seguir será utilizado o componente **EzButton**.

![Imagem 1: O componente EzDropdown não possui a capacidade de gerenciar a visibilidade do nível principal. Sua função é controlar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Variações e estados

### Manipulação dos itens

> Propriedade utilizada: **items**

Os itens do componente são renderizados por um objeto JSON,
nele possui as definições necessárias para configurar cada um destes itens.

Observação

Para adicionar uma sublista com itens filhos a um determinado item,
é necessário inserir o atributo **children** com uma lista de itens,
utilizando as mesmas configurações do atributo da lista principal.

As configurações de itens disponíveis são:

#### Tipo de item

> Atributo utilizado: **type**

O valor padrão do atributo type é **item**. No entanto, é possível modificar
para **divider** e **loading** para que um divisor seja apresentado entre os itens do menu
na posição correspondente do JSON. O exemplo a seguir ilustra essa possibilidade:

![Imagem 2: O valor padrão do atributo type é item . No entanto, é possível modificar para divider e loading para que um divisor…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ícones nos itens

> Atributo utilizado: **iconName**

Com o atributo iconName é possível atribuir um ícone no item desejado.
Conforme o exemplo a seguir:

![Imagem 3: Com o atributo iconName é possível atribuir um ícone no item desejado. Conforme o exemplo a seguir:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ação secundária

> Atributo utilizado: **subAction**

Com o atributo subAction é possível definir uma ação secundária no item desejado.

Informação

O texto de ação secundária terá duas variações de cores:

- **primary**: utilizada como padrão para ações secundárias.
- **critical**: utilizada para ações destrutivas como um excluir.

Importante

Caso o item da lista possua uma sublista com itens filhos,
a ação secundária não será exibida.
Isso significa que o atributo **subAction** será ignorado quando o
item tiver o atributo **children** preenchido.

Em **[exemplos de eventos](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-dropdown/#exemplos-de-eventos)**,
será demonstrado como utilizar o evento **ezSubActionClick**
para explorar a ação secundária e obter mais informações sobre ela.

A seguir será apresentado um exemplo com as duas variações de cores
e um item com os atributos subAction e children preenchidos.

![Imagem 4: A seguir será apresentado um exemplo com as duas variações de cores e um item com os atributos subAction e children…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Nome do grupo

> Atributo utilizado: **group**

O atributo group permite especificar o nome do grupo ao qual um determinado item pertencerá.
É necessário informar o nome desejado no formato de string, como ilustrado no exemplo a seguir:

![Imagem 5: O atributo group permite especificar o nome do grupo ao qual um determinado item pertencerá. É necessário informar o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### Ordenação do grupo

> Atributo utilizado: **group**

Além de permitir definir o nome do grupo ao qual um item pertencerá,
o atributo group também possibilita determinar a ordem em que o grupo será apresentado na lista.
Para isso, é necessário fornecer um objeto contendo os atributos **order** e **label**,
conforme exemplificado abaixo:

![Imagem 6: Além de permitir definir o nome do grupo ao qual um item pertencerá, o atributo group também possibilita determinar a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Capturar o valor do item

> Propriedade utilizada: **value**

A propriedade value armazena o item clicado, com ela é possível capturar os dados deste item.
Conforme o exemplo a seguir:

![Imagem 7: A propriedade value armazena o item clicado, com ela é possível capturar os dados deste item. Conforme o exemplo a…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Alterar aparência do item

> Propriedade utilizada: **itemBuilder**

A propriedade itemBuilder é uma função que possibilita alterar como o item da lista será apresentado.
Conforme o exemplo a seguir:

![Imagem 8: A propriedade itemBuilder é uma função que possibilita alterar como o item da lista será apresentado. Conforme o…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Altura máxima

> Variável CSS utilizada: **--ez-dropdown--max-height**

A variável --ez-dropdown--max-height define a altura máxima que a lista de itens pode atingir:

![Imagem 9: A variável --ez-dropdown--max-height define a altura máxima que a lista de itens pode atingir:](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Exemplos de eventos

#### ezClick()

Esse evento é emitido quando ocorre um clique em um item da lista.
A seguir será apresentado um exemplo de uso deste evento.

![Imagem 10: Esse evento é emitido quando ocorre um clique em um item da lista. A seguir será apresentado um exemplo de uso deste…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezSubActionClick()

Esse evento é emitido quando ocorrer um clique em uma ação secundária do item.
A seguir será apresentado um exemplo de uso deste evento.

![Imagem 11: Esse evento é emitido quando ocorrer um clique em uma ação secundária do item. A seguir será apresentado um exemplo de…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

#### ezHover()

Esse evento é emitido quando o ponteiro do mouse é colocado sobre um item.
A seguir será apresentado um exemplo de uso deste evento.

![Imagem 12: Esse evento é emitido quando o ponteiro do mouse é colocado sobre um item. A seguir será apresentado um exemplo de uso…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## API do componente

### Properties

| Property Attribute Description Type Default| `itemBuilder` -- Função builder que possibilita alterar como o item da lista vai ser apresentado. Observação: No react ele se transforma em VNode e não como HTMLElement. `(item: IDropdownItem, level: number) => string | HTMLElement` `undefined`| `items` -- Lista de itens que vão ser apresentados no dropdown. `IDropdownItem[]` `[]`| `value` -- Último item que recebeu o click. `IDropdownItem` `undefined` | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Events

| Event Description Type| `ezClick` Emitido quando ocorrer um click em um item da lista, o IDropdownItem que recebeu o click deve ser enviado como data do evento. `CustomEvent<IDropdownItem>`| `ezHover` Emitido quando ocorrer o ponteiro do mouse é colocado sobre um item. `CustomEvent<IDropdownItem>`| `ezOutsideClick` Emitido quando ocorrer um click fora do componente. `CustomEvent<void>`| `ezSubActionClick` Emitido quando ocorrer um click em uma ação secundaria do item, o IDropdownSubAction deve ser enviado como data do evento. `CustomEvent<IDropdownSubAction>` | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Dependencies

#### Used by

- [ez-breadcrumb](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-breadcrumb)
- [ez-split-button](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-split-button)

#### Depends on

- [ez-skeleton](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-skeleton)
- [ez-icon](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/components-doc/ez-icon)

#### Graph

```
graph TD;
  ez-dropdown --> ez-skeleton
  ez-dropdown --> ez-icon
  ez-breadcrumb --> ez-dropdown
  ez-split-button --> ez-dropdown
  style ez-dropdown fill:#f9f,stroke:#333,stroke-width:4px
```

---

### CSS Variables

| Variable Description| --ez-dropdown--z-index Define a posição do componente.| --ez-dropdown--padding Define o espaçamento interno do componente.| --ez-dropdown--box-shadow Define a sombra externa do componente.| --ez-dropdown--border-radius Define o raio da borda do componente.| --ez-dropdown--background-color Define cor de fundo do componente.| --ez-dropdown--font-family Define a fonte do componente.| --ez-dropdown--max-height Define a altura máxima do componente.| --ez-dropdown\_\_item--padding Define o espaçamento interno de cada item do componente.| --ez-dropdown\_\_item--gap Define o espaçamento entre os elementos internos do item do componente.| --ez-dropdown\_\_item--border-radius Define o raio da borda de cada item do componente.| --ez-dropdown\_\_item--color Define a cor do texto de cada item do componente.| --ez-dropdown\_\_item--font-weight Define o peso do texto de cada item do componente.| --ez-dropdown\_\_item--font-size Define o tamanho da fonte de cada item do componente.| --ez-dropdown\_\_item--line-height Define a altura do texto de cada item do componente.| --ez-dropdown\_\_item--background-color Define a cor de fundo no hover de cada item do componente.| --ez-dropdown\_\_item--transition Define o efeito de transição do hover de cada item do componente.| --ez-dropdown\_\_item-label--margin-right Define o espaçamento direito externo de cada label do componente.| --ez-dropdown\_\_icon--size Define o tamanho da área de cada ícone do componente.| --ez-dropdown\_\_divider--background-color Define a cor de fundo do divider do componente.| --ez-dropdown\_\_divider--margin Define o espaçamento externo do divider do componente.| --ez-dropdown\_\_group-label--color Define a cor do título de cada grupo do componente.| --ez-dropdown\_\_group-label--font-weight Define o peso do texto do título de cada grupo do componente.| --ez-dropdown\_\_group-label--font-size Define o tamanho da fonte do título de cada grupo do componente.| --ez-dropdown\_\_group-label--line-height Define a altura do texto do título de cada grupo do componente.| --ez-dropdown\_\_group-label--padding Define o espaçamento interno do título de cada grupo do componente.| --ez-dropdown\_\_submenu--z-index Define a posição do submenu do componente.| --ez-dropdown\_\_link--font-weight Define o peso do texto de cada link do componente.| --ez-dropdown\_\_link--primary--color Define a cor utilizada como padrão para ações secundárias.| --ez-dropdown\_\_link--critical--color Define a cor utilizada para ações destrutivas como um excluir.| --ez-dropdown\_\_scrollbar--color-default Define a cor da barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--color-background Define a cor de fundo da barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--color-hover Define a cor do hover na barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--color-clicked Define a cor do active na barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--border-radius Define o raio da borda da barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--width Define a largura da barra de rolagem do componente.| --ez-dropdown\_\_scrollbar--padding-right Define o espaçamento interno direito quando houver barra de rolagem. | | | --- | --- | | | | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
