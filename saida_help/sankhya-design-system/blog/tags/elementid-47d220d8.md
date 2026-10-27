---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/elementid"
titulo: "Localizando o atributo data-element-id"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/elementid"
trilha: "Blog > Tags > Elementid"
---

## [Definindo bons data element id de testabilidade no design system](https://gilded-nasturtium-6b64dd.netlify.app/blog/definindo-bons-element-id)

16 de fevereiro de 2023 · 9 min para ler

![Matheus Willames](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/MatheusWillames.jpg)

Matheus Willames

Developer

## Entendendo o atributo data-element-id: Como é construído?

O ElementIDUtils é um utilitário responsável por criar e adicionar identificadores únicos aos componentes através do atributo `data-element-id`. A finalidade dele é otimizar a automação dos testes e melhorar a eficiência na manipulação dos componentes do Design System, além de permitir a mapeamento de jornada dos usuário utilizando ferramentas como [posthog](http://posthog.com) e [hotjar](https://www.hotjar.com/), garantindo seleções precisas e seguras.

A atribuição de identificadores únicos permite representar os componentes de forma estruturada. Isto é fundamental para que os desenvolvedores possam utilizar esses identificadores para localizar elementos na página através de XPath, em vez de tentar encontrá-los pela posição ou tag. Dessa maneira, os identificadores precisam refletir semanticamente o que aquele elemento faz, exercendo um papel importante para garantir a qualidade e segurança de acesso aos componentes.

Como exemplo, o identificador de um botão localizado na TaskBar na seção Financeira poderia ser nomeado como `insert_ezButton`, para acessar esse elemento de forma segura poderíamos utilizar o seguinte querySelector: `[data-element-id="financeiro_snkCrud"] [data-element-id="financeiro_gridTop_snkTaskbar"] [data-element-id="insert_ezButton"]`. Esse padrão possibilita a compreensão estruturada dos elementos dentro do sistema, sendo crucial para garantir a confiabilidade dos testes automatizados e evitar falhas devido a mudanças na estrutura da página. Desta forma, a utilização de identificadores unicos fornece uma representação precisa da estrutura, facilitando a implementação e manutenção dos testes.

O `data-element-id` é construído a partir da combinação de propriedades de três atributos: element, suffix e iDInfo:

`ElementIDUtils.addIDInfo(element, suffix, iDInfo)`

A função "addIDInfo" recebe três parâmetros como entrada:

- "element": Um elemento do tipo HTMLElement.
- "suffix": Uma string opcional que pode ser adicionada como sufixo no valor retornado.
- "iDInfo": Um objeto opcional do tipo IElementIDInfo.

A interface "IElementIDInfo" define as propriedades que o objeto deve ter. Nesse caso, temos definido duas propriedades:

- "id": Uma string opcional.
- "dataUnit": Um DataUnit opcional.

Existe uma propriedade adicional chamada "Prefixo". Sempre que o `dataUnit` estiver presente no `ElementIDInfo` e o valor do `data-element-id` ainda não conter o `dataUnit.name` no inicio da String, será adicionado `dataUnit.name` como prefixo do valor do atributo `data-element-id`.

> **Exemplo**: `${dataInfo?.dataUnit?.name}_${valor_element_id}_${suffix}`

A função `addIDInfo` tem a responsabilidade de criar e adicionar o atributo `data-element-id` no argumento `element` seguindo as seguintes regras:

- Se o `element` já possuir um atributo `data-element-id`, ele será preservado e somente o prefixo e sufixo serão adicionados.
- Caso exista `ElementIDInfo.id` o valor do `data-element-id` será o valor do `ElementIDInfo.id` adicionando prefixo e sufixo.
- Se o `element` possuir o atributo `data-field-name`, o valor do `data-element-id` será a combinação do valor do `data-field-name` com o prefixo e sufixo.
- Se o `element` possuir o atributo `id`, o valor do atributo `data-element-id` será a combinação do valor do atributo `id` com o prefixo e sufixo.
- Se o atributo `name` estiver presente no `element`, o valor de `data-element-id` deve ser igual ao valor do atributo `name` com adição de prefixo e sufixo
- Se o atributo `label` estiver presente no `element`, o valor de `data-element-id` deve ser igual ao valor do atributo `label` com adição de prefixo e sufixo
- Caso nenhuma das condições acima sejam satisfeitas e o argumento `suffix` existir, o valor de `data-element-id` deve ser composto apenas pelo prefixo seguido pelo sufixo.
- Caso o argumento `suffix` for `null`, o valor padrão será automaticamente atribuído como `element.tagName`, normalizado no formato `camelCase`.

Por fim, a função `addIDInfo` gera automaticamente o identificador único, aplica ao `element` e retorna o valor como string.

## Criando e atribuindo "data-element-id" aos componentes

Para criar e atribuir um `data-element-id` para algum componente, basta seguir os passos abaixo:

1. Importe o utilitário `ElementIDUtils` do projeto `@sankhyalabs/core`.
2. Invoque a função `addIDInfo` passando os atributos esperados `ElementIDUtils.addIDInfo(element, suffix, iDInfo)`

   Exemplo:

   ```
   componentDidLoad() {
   	const dataInfo: IElementIDInfo = {dataUnit: this._dataUnit};
   	ElementIDUtils.addIDInfo(this._element, null, dataInfo);
   }
   ```

   **Resultado**: Em um cenário em que o `element` não contém os atributos requeridos pelo `ElementIDUtils` como `id`, `name`, `label`, `data-field-name` ou `data-element-id`, o atributo considerado para o ID único será composto pelo prefixo `name` do `dataUnit` e o sufixo `element.tagName` normalizado em `camelCase`. Visto que, se o argumento `suffix` receber `null`, o sufixo será automaticamente atribuído como `element.tagName`. Desse modo, o resultado final será:

   ```
   <snk-component data-element-id="Financeiro_snkComponent"></snk-component>
   ```

Lembre-se que o `ElementIDUtils.addIDInfo` adiciona automaticamente o `data-element-id` ao `element` enviado como parâmetro. Para obter o ID gerado, basta capturar o retorno da função.

## Como melhorar o atributo "data-element-id"?

O utilitário `ElementIDUtils` automatiza a geração do atributo `data-element-id`. Para torná-lo mais preciso e confiável, é possível atribuir propriedades adicionais aos componentes, como `id` ou `name`. Afinal, se o `element` possuir algum desses atributos, o valor do atributo `data-element-id` será a combinação do valor do atributo com o prefixo e sufixo. Isto torna o ID ainda mais singular, evitando conflitos.

**Exemplo**:

```
<snk-component id="stack-item-one"></snk-component>
```

```
componentDidLoad() {
	const dataInfo: IElementIDInfo = {dataUnit: this._dataUnit};
	ElementIDUtils.addIDInfo(this._element, null, dataInfo);
}
```

**Resultado**:

```
<snk-component
	id="stack-item-one"
	data-element-id="Financeiro_stackItemOne_snkComponent"
/>
```

## Como utilizar o data-element-id (POs E QAs)

A atribuição de identificadores únicos aos componentes é vital para a eficácia de testes automatizados, pois permite a identificação precisa e confiável de elementos específicos do sistema. Isso facilita a direção dos testes nesses componentes tornando-os mais acessíveis para realização de ações.

Sem a presença de identificadores únicos, os testes automatizados podem ser comprometidos pela seleção inadequada de elementos, pois seria necessário buscar por informações menos precisas, como classes ou tags. Baseando-se nisso, o utilitário `ElementIDUtils` foi criado como uma solução para contribuir na automatização de testes, tornando mais eficiente a utilização dos componentes do Design System. A partir desse utilitário é gerado identificadores únicos para os componentes através do uso do atributo `data-element-id`, permitindo a identificação precisa e confiável dos elementos durante o processo de teste.

O `data-element-id` gerado reflete semanticamente o que aquele elemento representa, exercendo um papel importante para garantir a qualidade de acesso aos componentes. Assim, permitindo representá-los de forma estruturada, como uma árvore na qual suas ramificações é simbolizadas pelos componentes. Isto é fundamental para localizar estes componentes no sistema em vez de tentar encontrá-los, por exemplo, pela posição, pois garante seleções precisas e seguras. Além disso, a utilização de identificadores oferece uma representação clara da estrutura da página favorecendo a manutenção dos testes.

Os principais componentes do Design System possuem um identificador único representado pelo atributo `data-element-id`. Por exemplo, o botão "Cadastrar" dentro da Taskbar do Financeiro pode ser definido como `snkTaskBar_INSERT`. Por meio desses atributos, este padrão se torna ágil e acessível de seguir, permitindo que os desenvolvedores de testes automatizados compreendam rapidamente a estrutura dos elementos no sistema.

# Localizando o atributo `data-element-id`

1. Em seu navegador, abra o "Inspecionar" ou "Ferramentas de desenvolvedor" dentro da página do sistema. No Google Chrome é possível acessar de diversas formas: clicando com o botão direito na página e selecionando a opção "Inspecionar", clicando no ícone de três pontos no canto superior direito do navegador, ir em "Mais ferramentas" e selecionar "Ferramentas do desenvolvedor" ou pressionando F12.
   ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk01-58dcc355fe42711bb782d773eb664249.jpg "Image 01")
2. Clique no ícone representado por um símbolo de cursor no canto superior esquerdo da janela do DevTools, denominado "Selecionar um elemento na página".
   ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk02-cf31fe28e7894ed5a47bc992b1defb30.jpg "Image 02")
3. Com a opção anterior selecionada, clique no elemento que você deseja capturar o `data-element-id`. Observe que, ao clicar, o código correspondente ao elemento será destacado no DevTools.

   [GIF animado: alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk03-bbf0de98b83a6327542b66f8bb7dc165.gif)
4. Alguns componentes possuem um elemento pai com o mesmo nome do elemento filho mas com o prefixo "ez-". Esse é o componente que nos interessa, pois é ele que possui o atributo `data-element-id` correspondente ao elemento selecionado.

   **Exemplo**: Um botão representado pelo elemento `button`, tem como elemento pai o `ez-button`.

   [GIF animado: alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk04-9e726a7b391cad6ab430a3206e2d7bd2.gif)
5. Efetue dois cliques no atributo "data-element-id" e copie o conteúdo.

   [GIF animado: alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk05-4bc2d40e0d08a8f41a420fb09e1effc7.gif)

### Mapeamento com PostHog

1. Acesse a página inicial do PostHog.
   ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk-posthog-01-acd76ff81eec7aa32d4beede1b338322.jpg "Image 01")
2. Para acessar os eventos, clique em `Live Events` na barra lateral esquerda.
   ![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk-posthog-02-2883540467ecb3e688e18e3a55e91604.jpg "Image 02")
3. Será exibida uma tabela com eventos executados nas páginas. É possível criar uma `Action` a partir desse evento clicando nos três pontos localizado após a coluna `Time` no final da linha e selecionar por `Create action from event`.

   [GIF animado: alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk-posthog-03-06c77cd15a6d676f61edcd52ac340414.gif)
4. Em seguida, navegue até a opção `HTML selector matches`, aqui você pode definir seus seletores. Para o `data-element-id`, o seletor terá a seguinte estrutura: `[data-element-id="id_component"] > nameElementHTML`. Uma vez conhecido o `data-element-id` do componente, adicione dessa forma juntamente com o nome do elemento desejado.

   **Exemplo**: `[data-element-id="Financeiro_snkCrud_insertBtn"] > button`

   O Gif abaixo demonstra como será o resultado no campo `HTML selector matches`:

   [GIF animado: alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/snk-posthog-04-2f3c553a7baf72dea033ea5a937f3a4d.gif)

### Mapeamento com métodos na DOM

Para encontrar um elemento na DOM com o atributo `data-element-id`, é necessário utilizar métodos de acesso ao DOM que permitem a seleção destes.

Os métodos a seguir são exemplos de como capturar o elemento a partir de um atributo, nesse caso, o `data-element-id`

- Buscar por um `data-element-id` específico:

```
const element = document.querySelector('[data-element-id="snkteste_snkCrud_crud_grid"]');
```

- Selecionar todos os elementos com o atributo `data-element-id`:

```
const elements = document.querySelectorAll('[data-element-id]');
```
