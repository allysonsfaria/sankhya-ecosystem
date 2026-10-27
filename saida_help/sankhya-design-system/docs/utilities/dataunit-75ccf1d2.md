---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/"
titulo: "DataUnit"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/"
trilha: "Docs > Utilities > Components > Dataunit"
---

# DataUnit

Criar interfaces de usuário que manipulam dados é um grande desafio que envolve diversas etapas, desde a recuperação dos dados até a apresentação deles de forma amigável para o usuário. A manipulação de dados costuma ser a parte mais desafiadora desse processo, uma vez que envolve uma série de tarefas, como a criação de registros, recuperação de informações, associação de atributos a campos na interface, a persistência dos dados, entre outras.

Embora as tecnologias atuais de desenvolvimento ofereçam recursos para reduzir a complexidade na manipulação de dados no contexto front-end, essa ainda é uma das etapas mais desafiadoras na implementação de interfaces. Com base nesse pressuposto, foi criado o componente **DataUnit**, uma ferramenta intuitiva cujo objetivo é simplificar a manipulação de dados, abstraindo os detalhes técnicos desse processo. Com o **DataUnit**, é possível realizar as operações **CRUD** (Create, Read, Update, Delete) nos registros e gerenciar os eventos associados a essas ações. Isso significa que os desenvolvedores podem se concentrar na criação de uma interface amigável para o usuário, sem se preocupar com os detalhes de como os dados são gerenciados.

O **DataUnit** atua como uma camada de abstração entre o back-end e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados. Com essa abordagem, os desenvolvedores não precisam implementar essa funcionalidade de maneira detalhada, pois o **DataUnit** assume essa responsabilidade. Além disso, cabe destacar que o **DataUnit** possui forte desacoplamento com serviços de regra de negócio do back-end, o que significa que não há conexão ou relação estabelecida com as entidades presentes no banco de dados. Isso torna o processo de gerenciamento de dados mais flexível e escalável, permitindo independência entre o back-end e o front-end, pois as alterações no back-end não requerem mudanças no lado front-end. Desse modo, possibilitando mudanças futuras de forma ágil, sem comprometer o funcionamento do back-end.

> Em resumo, o DataUnit funciona como um intermediário entre os dados e a aplicação, atuando como uma espécie de API que conecta o estado com a View. Em outras palavras, funciona como um repositório de dados que contém metainformação para descrever cada um dos campos, o que o torna uma ferramenta poderosa para o gerenciamento e manipulação de dados de forma eficiente e intuitiva.

## Loaders do DataUnit

No contexto do `DataUnit`, um Loader é um ponteiro de **função que executa serviços externos** ao `DataUnit`. Em termos gerais, são uma abstração usada para manter o `DataUnit` isolado de qualquer caso de uso específico. A ideia é permitir um nível de abstração que gera uma despreocupação com o processo interno de obtenção dos dados.

O `DataUnit` passa as informações para o ponteiro de função e espera que ele retorne uma `Promise`. O objetivo é que o `DataUnit` não precise conhecer a implementação e não saiba como os dados serão obtidos, tornando o componente agnóstico. Sendo assim, basta invocar um Loader desejado e tratar a `Promise` retornada.

Em resumo, o conjunto de métodos responsáveis por carregar e manipular dados do `DataUnit` inclui os seguintes Loaders:

- [metadataLoader](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#metadataloader), que fornece metadados do `DataUnit`;
- [dataLoader](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#dataloader), que gerencia a solicitação de carregamento de dados;
- [saveLoader](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#saveloader), que salva as alterações no `DataUnit`;
- [removeLoader](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#removeloader), que exclui registros do `DataUnit`;
- [recordLoader](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#recordloader), que carrega registros especificados do `DataUnit`.

Nos tópicos a seguir, serão espeficados cada um dos Loaders, usando como exemplo uma simulação de uma carga de dados por um servidor.

### metadataLoader

O método `metadataLoader` é responsável por **definir os metadados** do DataUnit, recuperando as informações com base no parâmetro `DataUnit` passado como argumento e, em seguida, transforma essas informações em um objeto de metadados e o retorna a partir de uma `Promise`.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `metadataLoaderCountries`, implementação do `metadataLoader`.

![Imagem 1: É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método metadataLoaderCountries…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### dataLoader

O método `dataLoader` encarrega-se de gerenciar a solicitação de **carregamento de dados** retornando os dados do DataUnit. O método recebe como parâmetro os atributos `dataUnit` e `request`, o primeiro parâmetro é o `DataUnit` ser carregado enquanto o `request` trata-se de um objeto do tipo `LoadDataRequest` que contém informações adicionais sobre como os dados devem ser carregados, como os filtros a serem aplicados, a ordenação, etc. A função retorna uma `Promise` que é resolvida com um objeto contendo os dados carregados.

É importante ressaltar que, é de respondabilidade do desenvolvedor ao implementar o `dataLoader`, que o mesmo lide com as funcionalidades de **paginação**, **ordenação** e **filtragem**,
seja no backend, no serviço que retorna os dados solicitados, ou no frontend, na implementação do próprio `dataLoader`.

Informação

É esperado que todo registro possua uma propriedade chamada `__record__id__`, que é utilizada pelo `DataUnit` para indexação dos registros.

Dica

Para implementação das funcionalidades de **paginação**, **ordenação** e **filtragem** no frontend, podemos utilizar a classe **[DataUnitLoaderUtils](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitLoaderUtils)**,
que disponibiliza alguns utilitários que abstraem essa complexidade.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `dataLoaderCountries`, implementação do `dataLoader`.

![Imagem 2: É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método dataLoaderCountries ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### saveLoader

O `saveLoader` tem como atribuição **salvar as alterações** realizadas no `DataUnit`, e retorna uma `Promise` contendo os registros salvos. Para isso, a função recebe o `DataUnit` cujas mudanças serão salvas e um `Array` de objetos que representam as mudanças a serem feitas.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `saveLoaderCountries`, implementação do `saveLoader`.

![Imagem 3: É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método saveLoaderCountries ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### removeLoader

O método `removeLoader` é responsável por **excluir registros** do `DataUnit` e retornar uma `Promise` contendo os IDs dos registros que foram alvos da exclusão. O método recebe como parâmetro `dataUnit` e `recordIds`, onde `recordIds` é definido como um array contendo os identificadores dos registros que serão removidos do `DataUnit`.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `removeLoaderCountries`, implementação do `removeLoader`.

![Imagem 4: É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método removeLoaderCountries ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### recordLoader

O método `recordLoader` é usado para **carregar registros** do `DataUnit`. O método recebe como parâmetro `dataUnit` e `recordIds`, onde `recordIds` trata-se de um `Array` contendo os IDs que são passados automaticamente pela seleção dos registros. O método retorna uma `Promise` que, quando resolvida, fornece as informações dos registros carregados.

É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método `recordLoaderCountries`, que é a implementação do `recordLoader`, para atualizar a população de um país selecionado para um valor aleatório. Para executá-lo, basta clicar no botão "Recarregar Registro Selecionado".

![Imagem 5: É demostrado abaixo um exemplo prático da implementação deste método, onde foi criado o método recordLoaderCountries ,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Métodos públicos

O dataUnit expõe uma gama de métodos para permitir manipular seus dados, metadados, seleção de registros, controle de paginação, entre outros.

Seguem alguns exemplos:

### hideField / showField

Os métodos `hideField` e `showField` permitem que os metadados sejam manipulados, informando se um campo deve ser ocultado ou exibido.

![Imagem 6: Os métodos hideField e showField permitem que os metadados sejam manipulados, informando se um campo deve ser ocultado…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### setFieldValue

O método `setFieldValue` é utilizado para **inserir ou atualizar o valor de um campo** no registro atual do DataUnit. Este método possui um comportamento especial: **se não houver nenhum registro selecionado ou registro novo criado, ele automaticamente criará um novo registro** antes de atribuir o valor ao campo.

#### Parâmetros

- **`fieldName`** (string): Identificador do campo que será modificado.
- **`newValue`** (any): Valor a ser inserido no campo. Pode ser um valor direto ou uma `Promise` que será resolvida posteriormente.
- **`records`** (Array<string>, opcional): Array com os IDs dos registros que serão afetados pela alteração. Se não fornecido, a alteração será aplicada ao registro atual.
- **`options`** (DataUnitEventOptions, opcional): Objeto de configurações do evento, incluindo:
  - **`suppressCreateNewRecord`** (boolean): Quando `true`, impede a criação automática de um novo registro caso não haja registro selecionado. Neste caso, o método retornará `false` sem realizar alterações.

#### Retorno

Retorna uma `Promise<boolean>` que será resolvida quando o novo valor for persistido no state:

- **`true`**: Quando o valor foi alterado com sucesso.
- **`false`**: Quando o valor não foi alterado (valor igual ao atual, sem registro selecionado com `suppressCreateNewRecord` ativo, etc.).

#### Comportamento de criação de novo registro

Comportamento Importante

Se o método for chamado **sem nenhum registro selecionado** e **sem um registro novo em edição**, o DataUnit **automaticamente criará um novo registro** antes de atribuir o valor ao campo. Este comportamento pode ser suprimido utilizando a opção `suppressCreateNewRecord: true`.

![Imagem 7: Se o método for chamado sem nenhum registro selecionado e sem um registro novo em edição , o DataUnit automaticamente…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

---

# API do Componente

**[Clique aqui para acessar a API do DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/api/classes/DataUnit)**
