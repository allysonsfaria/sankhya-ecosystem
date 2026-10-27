---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/review"
titulo: "2 publicações com a etiqueta \"review\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/review"
trilha: "Blog > Tags > Review"
---

# 2 publicações com a etiqueta "review"

## [Boas práticas de codificação e codereview](https://gilded-nasturtium-6b64dd.netlify.app/blog/boas-praticas-code-review-codificacao)

7 de abril de 2023 · 13 min para ler

![Helikson Rufino](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/HeliksonRufino.jpg)

Helikson Rufino

Software Architect

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

![Marcos Sobral](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/MarcosSobral.png)

Marcos Sobral

Software Architect

### Introdução

O desenvolvimento de software requer uma série de boas práticas e requisitos que visam garantir a qualidade do código produzido. O documento a seguir apresenta uma lista de recomendações para testes do desenvolvedor, código limpo, estilização em CSS e SASS e boas práticas em JSX e JS. Tais recomendações visam garantir a manutenibilidade do código, facilidade de leitura e entendimento, além de contribuir para a consistência e padronização do desenvolvimento.

### Testes de desenvolvimento

- Não é necessário realizar os testes exploratórios em todos os roteiros de testes.
- Devemos realizar os testes nos seguintes ambientes:

  - Navegadores

    - Chrome
    - Edge
    - Firefox
    - Safari (no macOS)
  - Resolução da tela

    - Devemos realizar os testes nas resoluções mais utilizadas pelos usuários. São elas:

      - 1366x768
      - 1920x1080
      - 1536x864
      - 1024x768
      - 1600x900

### Clean Code

Clean Code é um conjunto de práticas e princípios que visam melhorar a qualidade do código fonte, tornando-o mais legível, fácil de manter e de entender. Essas práticas são baseadas em anos de experiência e em estudos sobre como as pessoas leem e compreendem o código.
Uma das principais vantagens de se aplicar o Clean Code é a facilidade de manutenção do código. Um código bem escrito é mais fácil de entender, reduzindo a incidência de bugs e melhorando a produtividade da equipe de desenvolvimento. Além disso, um código limpo e bem organizado ajuda a evitar problemas de manutenção no futuro, tornando o processo de correção de bugs e de adição de novas funcionalidades mais rápido e eficiente.
Para aplicar as práticas de Clean Code, é importante seguir uma série de boas práticas. Algumas dessas práticas incluem:

- **Dar nomes significativos às variáveis, funções e classes**: é importante escolher nomes que reflitam a função de cada elemento do código, tornando-o mais fácil de entender. Nomes claros e descritivos ajudam a evitar erros de interpretação e a tornar o código mais legível.

> Defina nomes claros:

```
// ❌ Incorreto
const d = new Date();
// ✅ Correto
const currentDate = new Date();
```

> Evite redundância:

```
// ❌ Incorreto
const listGroup = [];
// ✅ Correto
/* Por ser um array já sabemos que é uma lista,
essa info não precisa estar no nome da variável */
const groups = [];
```

> Utilize nomes pronunciáveis:

```
// ❌ Incorreto
const ddmmyyyy = new Intl.DateTimeFormat("pt-BR").format(new Date());
// ✅ Correto
const currentFormattedDate = new Intl.DateTimeFormat("pt-BR").format(new Date());
```

> Utilize nomes pesquisáveis

```
// ❌ Incorreto
if (groups.length < 7) {
 // Do something
}
// ✅ Correto
if (groups.length < MAX_GROUPS) {
  // Do something
}
```

- **Manter as funções curtas e com uma única responsabilidade**: funções muito longas ou com múltiplas responsabilidades são difíceis de entender e de manter. É importante dividir as funções em partes menores, cada uma com uma única responsabilidade bem definida.

> A função deve ter uma única responsabilidade

```
// ❌ Incorreto
selectOption(newOption){
  this.selectedOption = newOption;
  this._visibleOptions = [];
}
// ✅ Correto
selectOptionAndClearVisible(newOption){
this.selectedOption = newOption;
this.clearVisibleOptions();
}
clearVisibleOptions(){
  this._visibleOptions = [];
}
```

> As condições quando, muito grandes, devem ser encapsuladas em funções

```
// ❌ Incorreto
if( this.value.getDate() == currentDate.getDate() &&
  this.value.getMonth() == currentDate.getMonth() &&
  this.value.getFullYear() == currentDate.getFullYear()){
// Do something
}
// ✅ Correto
if(isSelectedDate(currentDate)){
// Do something
}
isSelectedDate(currentDate) {
  return  this.value.getDate() == currentDate.getDate() &&
          this.value.getMonth() == currentDate.getMonth() &&
          this.value.getFullYear() == currentDate.getFullYear()
}
```

> Utilize poucos argumentos, o recomendado é no máximo 3

```
// ❌ Incorreto
setSelection(selection, before, after){
  // Do something
}
// ✅ Correto
setSelection(executionCtx: ExecutionContext){
  // Do something
}
ExecutionContext{
  selection: Array<string>,
  before?: () => { /*Do something*/ };
  afte?: () => { /*Do something*/ };
}
```

> Não use argumentos para alterar o comportamento da função

```
// ❌ Incorreto
getToday(withTime){
  const today = new Date();
  if (withTime) {
     return today;
   } else {
     return clearTime(today);
   }
}
// ✅ Correto
getToday(){
  const today = new Date();
  return today;
}
getTodayWithoutTime(){
  const today = getToday();
  return clearTime(today);
}
```

> Previna efeitos colaterais

```
// ❌ Incorreto
checkPassword(String userName, String password) {
if(isValidPassWord(userName, password)){
    Session.initialize();
      return true;
  }
  return false;
}
// ✅ Correto
checkPassword(String userName, String password) {
if(isValidPassWord(userName, password)){
      return true;
  }
  return false;
}
checkPasswordAnInitializeSession(String userName, String password) {
if(checkPassword(userName, assword)){
      Session.initialize();
      return true;
  }
  return false;
}
```

- **Evitar repetições desnecessárias de código**: repetições desnecessárias tornam o código mais difícil de manter e de entender.
  É importante usar funções e métodos genéricos quando possível, para evitar a repetição do mesmo código em múltiplos lugares.
- **Manter a formatação consistente**: a formatação do código deve ser consistente em todo o projeto, usando espaços e indentação de forma padronizada.
  Isso torna o código mais fácil de ler e compreender.
- **Comentar apenas o necessário**: comentários devem ser usados apenas quando necessário, para explicar o "porquê" do código e não o "como".
  Comentários em excesso podem tornar o código mais difícil de ler e de manter.
- **Fazer testes unitários**: testes unitários são essenciais para garantir que o código funcione corretamente e para evitar regressões no futuro.
  É importante escrever testes para todas as partes do código que possam ser testadas.
- **Refatorar o código constantemente**: Refatorar o código é uma prática essencial para manter a qualidade do código ao longo do tempo. Ao refatorar,
  é possível identificar problemas e melhorias no código, tornando-o mais fácil de entender e de manter.

### Estilização (CSS e SASS)

- Utilizar os [tokens criados no ez-design](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/tokens/)

Atenção

Caso não exista uma class que será necessária na implementação e reutilizada em outros locais, [abra uma nova issue](https://gitlab.sankhya.com.br/dti/design-system/design-system-issues/-/issues/new?issue%5Bassignee_id%5D=&issue%5Bmilestone_id%5D=) solicitando para que seja adicionada.

- Defina seletores específicos para que sejam utilizados apenas nos locais que fazem sentido para a implementação.

```
// ❌ Incorreto
grid__label--beautiful
// ✅ Correto
financial-accounts-grid__label--beautiful
```

- **Não** utilize o !important nas adições de estilos.
- **Não** sobrescreva as variáveis do Design System, utilize-as na sua forma padrão.
- Utilize Flexbox ou Grid System para deixar a aplicação responsiva

  - [Flexbox System](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/flexbox-system/)
  - [Grid System](https://gilded-nasturtium-6b64dd.netlify.app/docs/components/layout-doc/grid-system/)
- Utilize a [metodologia BEM](https://getbem.com/introduction/) para criar sua estrutura de classes

### React, JSX e JS

- Para desenvolvimento de telas sankhya sempre utilizar os blocos de construção já disponíveis no sankhya-bocks.

Informação

Caso seja necessário a construção de um novo bloco de construção ou a manutenção do comportamento em um bloco já existente,
podemos [abrir uma issue](https://gitlab.sankhya.com.br/dti/design-system/design-system-issues/-/issues/new?issuable_template=new_feature).

- Toda e qualquer regra de negócio deve ser construída no back-end. Em nenhum momento devemos criar regras de negócio no front-end.
- Em hipótese alguma, devemos alterar a DOM ou Virtual DOM para atender casos específicos de tela.
- Sempre estar atento aos hooks do react, se perguntar:

  - São seguros?
  - Estão sendo disparados apenas quando necessário?
- Não deixe comentários, consoles, linhas ou espaços desnecessários.
- Remova todo código não utilizado, inclusive os códigos comentados.
- Ao criar um componente ReactJs, sempre optar por criar um function component.
- Todos os códigos fonte devem estar em UTF-8.
- Sempre estar atento se o reject de promises estão sendo tratadas. Como no exemplo a seguir:

```
DataFetcher.get().callServiceBroker(
SERVICE_MONTA_DADOS_BAIXA,
      JSON.stringify(requestBody)
)
.catch(reason => console.log(reason));
/* No exemplo, caso algo dê errado na montagem dos dados de baixa,
a reject da promise irá informar o que ocorreu.*/
```

- Verificar se as propriedades com useRef estão sendo utilizadas com a propriedade current? Como no exemplo a seguir:

```
application.current?.info("Mensagem informativa!");
```

- Chamadas de serviço devem ser feitas utilizando o DataFetcher. Como no exemplo a seguir:

```
DataFetcher.get().callServiceBroker(
SERVICE_MONTA_DADOS_BAIXA,
JSON.stringify(requestBody)
).then((resolve) => {
console.log(resolve)
}).catch(reason => console.log(reason));
```

- Funções callback de listeners, devemos sempre usar arrow functions. Como no exemplo a seguir:

```
element.addEventListener("ezChange", () => console.log("Elemento alterado!"));
```

- Sempre fazer unsubscribe de listeners registrados no DataUnit.

Dica

O `unsubscribe` é usado para remover um Observer registrado no DataUnit. Sem o `unsubscribe`, o ouvinte de evento continuaria registrado,
mesmo quando o componente não estivesse mais em uso, causando possíveis problemas de desempenho e vazamento de memória. Portanto, é importante realizar
o `unsubscribe` ao desconectar o componente do DOM para garantir que os recursos sejam utilizados de forma eficiente.

- Sempre utilize React Fragment para encapsular um JSX e não usar div’s para essa responsabilidade. Como mostra o exemplo a seguir:

```
// ❌ Incorreto
return (
<div>
<div>Container 1</div>
  <div>Container 2</div>
  <div>Container 3</div>
</div>
)
// ✅ Correto
return (
<>
  <div>Container 1</div>
  <div>Container 2</div>
  <div>Container 3</div>
</>
)
```

- Use aspas duplas para strings

```
const fruits = ["Abacaxi", "Manga", "Banana"];
```

- Use undefined, não null

```
// ❌ Incorreto
const fruits = null;
// ✅ Correto
const fruits = undefined;
```

- Quando necessitar validar usando undefined utilizar apenas “==” ou “!=” e não “===”, “!==”. Como no exemplo a seguir:

```
const fruits = null;
// ❌ Incorreto
const allFruits = () => fruits === undefined ? "Não há frutas": fruits;
console.log(allFruits()) //retorna:  null
// ✅ Correto
const allFruits = () => fruits == undefined ? "Não há frutas": fruits;
console.log(allFruits()) //retorna: "Não há frutas"
```

- Use arrow functions no lugar de funções anônimas.

```
// ❌ Incorreto
setTimeout(function(){
  console.log("Execultou após 1 segundo")
}, 1000);
// ✅ Correto
setTimeout(() => {
  console.log("Execultou após 1 segundo")
}, 1000);
```

- Use surround parâmetros de arrow functions somente quando necessário. Como no exemplo a seguir:

```
// ❌ Incorreto
(x) => x + x
// ✅ Correto
x => x + x
// ✅ Correto
(x,y) => x + y
// ✅ Correto
<T>(x: T, y: T) => x === y
```

- Sempre coloque o loop e os corpos condicionais entre as chaves. Como no exemplo a seguir:

```
// ❌ Incorreto
for (var i = 0, n = str.length; i < 10; i++) // Do something
if (x < 10) // Do something
// ✅ Correto
for (var i = 0, n = str.length; i < 10; i++) { // Do something }
if (x < 10) {// Do something }
```

- Códigos entre parênteses não devem ter espaços em branco ao redor

```
for (var i = 0, n = str.length; i < 10; i++) { }
if (x < 10) { }
function f(x: number, y: string): void { }
```

- Use else na mesma linha da chave de fechamento do if. Como no exemplo a seguir:

```
const fruits = ["Abacaxi"];
if(fruits.length > 0){
  console.log(fruts)
}else{
  console.log("Não há frutas!")
}
```

- Use 4 espaços por indentação. Como no exemplo a seguir:

```
const fruits= ["Abacaxi"];
if(fruits.length > 0){
  console.log(fruts)
}
// O console.log dentro do escopo da condição possui 4 espaços
```

- Sempre dê preferência pelo uso do const e let ao invés de var:

```
// ❌ Incorreto
var fruits = ["Abacaxi"];
// ✅ Correto
let fruits = ["Abacaxi"];
const fruits = ["Abacaxi"];
```

- Sempre dê preferência por utilizar arrow functions

```
// ❌ Incorreto
[1, 2, 3].map(function(number, index) {
  return ({ [index]: number });
})
// ✅ Correto
[1, 2, 3].map((number, index) => ({ [index]: number }))
```

- Funções ou componentes simples, que possuem apenas um retorno, não é necessário o uso de chaves e return.

```
// ❌ Incorreto
const getUserInfo = id => {
  return new Promise((resolve, reject) => {
      return callSomeFunction()
      .then(result => {
          return resolve(result)
      })
      .catch(error => {
          return reject(error)
      })
})
// ✅ Correto
const getUserInfo = id => (
  new Promise((resolve, reject) => (
      callSomeFunction()
          .then(result => resolve(result))
          .catch(error => reject(error))
      )
)
// ❌ Incorreto
const DemoComponent = () => {
  return (
      <span>
          Return only it
      </span>
  )
}
// ✅ Correto
const DemoComponent = () => (
  <span>
      Return only it
  </span>
)
```

- Utilize o destructuring ao receber algum valor ao invés de pegar elemento por elemento

```
// ❌ Incorreto
const name = objectInfo.name;
const email = objectInfo.email;
const name = arrayInfo[0];
const email = arrayInfo[1];
// ✅ Correto
const { name, email } = objectInfo;
const [ name, email ] = arrayInfo;
// ❌ Incorreto
const getInfo = info => "Mensagem"
// ✅ Correto
const getInfo = ({ name, email }) => "Mensagem"
// ❌ Incorreto
const getInfo = (allInfo) => ({
  Name: "Mensagem",
  "E-mail": allInfo.email,
  Address: getAddress(allInfo),
})
// ✅ Correto
const getInfo = ({ name, lastName, email, ...rest }) => ({
  Name: "Mensagem",
  "E-mail": email,
  Address: getAddress(rest),
})
```

- O uso do else não é necessário em 90% dos casos. Basta apenas dar um return finalizando a função ou o componente:

```
// ❌ Incorreto
const getInfo = (data) => {
  ...
  if (negativeValidade) {
      return undefined;
  } else {
      ...
      return data;
  }
}
// ✅ Correto
const getInfo = (data) => {
  ...
  if (negativeValidade) {
      return undefined;
  }
  ...
  return data;
}
// ❌ Incorreto
const DemoComponent = () => {
  ...
  if (negativeValidate) {
      return null;
  } else {
      ...
      return (
          <span>
              Returned value
          </span>
      )
  }
}
// ✅ Correto
const DemoComponent = () => {
  ...
  if (negativeValidate) {
      return null;
  }
  ...
  return (
      <span>
          Returned value
      </span>
  )
}
```

- Ao passar valores para um object, não repita o nome da variável caso seja o mesmo da key.

```
const name = "Sankhya"
const url = "sankhya.com.br"
// ❌ Incorreto
const newObj = {
  name: name,
  url: url,
}
// ✅ Correto
const newObj = {
  name,
  url,
}
```

- Caso queira alterar ou adicionar algum valor no object ou array, utilize o **Spread Operator**

```
const myObject = {
name: "Sankhya",
url: "sankhya.com.br"
}
const anotherObject = {
  name: "Sankhya Gestão de negócios",
  email: "sankhya@sankhya.com.br",
}
// ❌ Incorreto
const myConditionalObject = condition ? { a: "value a" } : { a: "value b" }
let myNewObject = {}
myNewObject = Object.assign({}, myNewObject, myObject)
myNewObject = Object.assign({}, myNewObject, anotherObject)
myNewObject = Object.assign({}, myNewObject, myConditionalObject)
// ✅ Correto
const myNewObject = {
...myObject,
...anotherObject,
...(condition ? { a: "value a" } : { a: "value b" })
}
```

- Caso não saiba se aquele object ou o array sempre possui aquela propriedade, utilize o **Optional Chaining**

```
const user = { name: "Sankhya" }
const userArray = []
// ❌ Incorreto
const userEmail = user && user.email ? user.email : undefined
const values = userArray && userArray[0] ? userArray[0] : undefined
// ✅ Correto
const userEmail = user?.email
const values = userArray?.[0]
```

- Caso o operador ternário valide alguma condição e a retorne em caso de verdade, utilize o **Nullish Coalescing**

```
const user = { name: "Sankhya" }
const userArray = []
// ❌ Incorreto
const value = myValue ? myValue : defaultValue;
// ✅ Correto
const value = myValue ?? defaultValue;
```

- Sempre que uma função, variável ou componente fique muito grande, quebre em mais linhas

```
const user = { name: "Sankhya" }
const userArray = []
// ❌ Incorreto
const myExtensiveObject = { name: "Sankhya", email: "sankhya@sankhya.com.br", url: "sankhya.com.br" }
// ✅ Correto
const myExtensiveObject = {
  name: "Sankhya",
  email: "sankhya@sankhya.com.br",
  url: "sankhya.com.br"
}
// ❌ Incorreto
const myFunction = () => (
  new Promise((resolve, reject) => {
      callAnotherServiceWithLongName().then(result => resolve(result)).catch(error => reject(error)).finally(() => alert("finish"))
})
)
// ✅ Correto
const myFunction = () => (
  new Promise((resolve, reject) => {
      callAnotherServiceWithLongName()
          .then(result => resolve(result))
          .catch(error => reject(error))
          .finally(() => alert("finish"))
      })
)
// ❌ Incorreto
const DemoComponent = () => {
  const values = {};
  return (
      <MyComponent value={values} label="Sankhya" onClick={() => {}} onChange={() => {}} />
  )
}
// ✅ Correto
const DemoComponent = () => {
  const values = {};
  return (
      <MyComponent
          value={values}
          label="Sankhya"
          onClick={() => {}}
          onChange={() => {}}
      />
  )
}
```

- Ao criar uma função com muitos parâmetros, utilize um object ao invés de várias variáveis

```
const user = { name: "Sankhya" }
const userArray = []
// ❌ Incorreto
const myFunction = (name, email, url, address) => { ... }
myFunction(name, email, url, address)
// ✅ Correto
const myFunction = ({ name, email, url, address }) => {... }
myFunction(myObjectValues)
```

- Um laço de algum elemento JSX precisa ter uma key única

```
return (
<>
this.items.map( item => <li
 key={"item_" + item.label}>
  {{item.label}}
</li>                           )
<>
)
```

- Para strings dinâmicas, utilize template literals

```
const itemKey = `item_${item.label}`;
```
