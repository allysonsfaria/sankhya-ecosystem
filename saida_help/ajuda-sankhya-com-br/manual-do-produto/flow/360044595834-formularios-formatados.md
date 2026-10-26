---
id: "360044595834"
titulo: "Formulários Formatados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-10-08T11:24:26Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.workflow.cad.formularioformatado", "Formulários Formatados manual", "Configuração", "Relatórios", "Formulários", "sankhyaflow", "Campos e atributos", "Coletam dados", "Vínculos e eventos", "Estrutura Reutilizável", "Persistência de dados"]
---

# Formulários Formatados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313259781527) Módulo: Flow
```

---

Os Formulários Formatados são estruturas utilizadas para coleta e/ou apresentação de dados aos usuários do sistema, considerando a execução de tarefas vinculadas a um determinado processo. Sendo que, estes formulários possuem duas grandes diferenças em relação aos campos do formulário principal de um processo, são elas:

1. Considerando a **"Estrutura Reutilizável"**, você pode construir formulários com diversos campos e utilizá-los em processos diferentes;
2. Em relação a **"Persistência de dados"**, esta refere-se as tabelas adicionais do sistema que possuem registros acessíveis considerando a personalização de telas adicionais, dashboards e relatórios após a conclusão do processo.

| [Construindo um formulário formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#construindoumformulrioformatado) |  | [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abacampos) |
| --- | --- | --- |
| [Aba Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abaligaes) |  | [Aba Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abaeventos) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#botooutrasopes) |  | [Considerações Finais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#consideraesfinais) |

![Imagem 2: Considerações Finais](https://ajuda.sankhya.com.br/hc/article_attachments/4407919786135)

## Construindo um formulário formatado

Para realizar a criação de um Formulário Formatado acione o botão  **"Novo"** localizado na parte superior central da tela. Assim será apresentado um pop-up **"Novo Formulário"** onde você poderá definir o tipo de formulário que será utilizado. Sendo eles:

![Imagem 3: Para realizar a criação de um Formulário Formatado acione o botão "Novo" localizado na parte superior central da tela.…](https://ajuda.sankhya.com.br/hc/article_attachments/4407919890455)

**Formulário mestre**

Este formulário é geralmente denominado como Formulário Pai, podendo ser vinculado ao processo ou a uma tarefa de usuário.

![Imagem 4: Este formulário é geralmente denominado como Formulário Pai , podendo ser vinculado ao processo ou a uma tarefa de…](https://ajuda.sankhya.com.br/hc/article_attachments/4407923127959)

No campo **"Descrição do formulário"**, informe o nome do formulário que está sendo cadastrado.

Depois, descreva no campo **"Nome da tabela no banco de dados"** a nomenclatura da tabela no banco de dados.

Feito isso, clique no botão **"Concluir"**, dessa forma o sistema irá recarregar a tela de acordo com as configurações efetuadas.

![Imagem 5: Feito isso, clique no botão "Concluir" , dessa forma o sistema irá recarregar a tela de acordo com as configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/4407928534551)

**Observação:** os campos mencionados acima serão utilizados para representar unicamente os registros inseridos na estrutura em seu uso por processos.

**Formulário detalhe**

Neste tipo de formulário, é necessário informar no campo **"Selecione um formulário mestre"** um formulário mestre previamente configurado, para que o mesmo seja vinculado ao cadastro.

![Imagem 6: Neste tipo de formulário, é necessário informar no campo "Selecione um formulário mestre" um formulário mestre…](https://ajuda.sankhya.com.br/hc/article_attachments/4407923300631)

Em seguida, preencha os campos **"Descrição do formulário"** e **"Nome da tabela no banco de dados"**, que possuem as mesmas funcionalidades descritas no formulário anterior.

![Imagem 7: Em seguida, preencha os campos "Descrição do formulário" e "Nome da tabela no banco de dados" , que possuem as mesmas…](https://ajuda.sankhya.com.br/hc/article_attachments/4407923127959)

Após estes passos, realize as devidas configurações em relação a **"chave-primária"** da tabela:

![Imagem 8: Após estes passos, realize as devidas configurações em relação a " chave-primária" da tabela:](https://ajuda.sankhya.com.br/hc/article_attachments/4407928733207)

**Importante:** após concluir os devidos registros, independente do tipo de formulário selecionado, o sistema procederá automaticamente com as seguintes configurações:

1. Acrescentará o prefixo **"AD\_"** nos registros inseridos nos campos do Cabeçalho da tela.
2. Disponibilizará quatro campos principais que compõem a chave primária da tabela criada, sendo estes **"Inst. processo"**, **"Inst. tarefa"**, **"Código"** e **"Tarefa"** (aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abacampos)).

Ainda sobre o Formulário detalhe, deverão ser criados campos para compor a chave primária da estrutura em conjunto com os campos que já fazem parte da chave-primária do Formulário mestre. Ao concluir a criação do formulário, o sistema irá inserir automaticamente os campos que fazem parte da chave-primária do formulário mestre, assim como os campos que fazem parte da chave-primária do formulário em referência.

**Nota:** o sistema permitirá que sejam utilizados outros campos além daqueles que compõem a chave-primária, sendo possível incluí-los de forma manual por meio das funcionalidades da aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abacampos). Além disso, é possível editar os atributos dos campos através do botão **"Atributos"** e os campos poderão ser importados utilizando o botão **"Importar Campos"**, ambos localizados na mesma aba.

**Observação:** para maiores detalhes em relação a cada um dos tipos de campos do formulário,  acesse o link do artigo [Construtor de telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas), ambos possuem a mesma estrutura e contexto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)

## Aba Campos

Por meio desta aba, é possível proceder com as configurações dos campos que serão visualizados nesta tela.

| [Botão Importar Campo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#bot%C3%A3oimportarcampo) |  | [Botão Atributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#bot%C3%A3oatributos) |
| --- | --- | --- |

![Imagem 9: Botão Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/4408071770647)

Considerando que tenha sido criada uma nova tabela no banco de dados com a chave primária, é possível adicionar campos mantendo as informações relevantes da tela por meio desta aba.

No campo **"Nome do Campo"**, informe a nomenclatura que o campo deverá possuir na tabela do banco de dados.

A descrição informada no campo **"Descrição do campo"**, constará em todas as situações onde for apresentada, considerando a presente tela, assim como, grades, telas de pesquisas, relatórios rápidos, dentre outros.

No campo **"Tipo de Dados"** será definido o tipo de campo que corresponde ao banco de dados. São apresentadas as seguinte opções:

- **Conteúdo Binário:** Esse tipo de dados é utilizado para campos do tipo Imagem, Arquivo e Múltiplos Arquivos. Sendo que, quando o campo **"Apresentação"** estiver configurado com a opção **"Múltiplos Arquivos"**, será possível anexar ao campo, links que poderão ser copiados, ou então, o redirecionamento direto para a página pertencente ao link.
- **Texto Longo (CLOB):** Esta opção permite inserir uma grande quantidade de informações. Além disto, será possível alterar algumas características da fonte do texto informado deixando este negrito, itálico ou sublinhado, sendo possível também inserir marcadores.
- **Data:** Neste caso as informações serão representadas considerando apenas a data inserida.
- **Número Decimal:** Este tem a finalidade de representar os valores numéricos com decimais ou valores de moeda. Desse modo, o campo será criado no banco de dados como sendo do tipo FLOAT.
- **Data e Hora:** Por meio desta opção, tem a representação de data e hora; os campos serão criados no Banco de Dados como DATE Oracle e DATETIME SQLServer.
- **Número Inteiro:** Este tipo representa números sem a parte decimal (inteiros), ideal para códigos. Ele será criado no Banco de Dados como sendo do tipo NUMBER (10) Oracle e INT SQLServer.
- **Texto:** Este tipo é curinga, e dependendo do tipo de **"Apresentação"** sua exibição ocorrerá de maneiras diferentes pelo sistema, como segue:

**a) Lista de opções:** Será apresentado como sendo uma caixa de seleção (ComboBox). Os itens da caixa de seleção são informados no botão **"Opções"** que se localiza ao lado do campo Apresentação. Nela define-se a lista de valores utilizando pares valor/descrição.

**Observação:** o valor é o que será armazenado no Banco de Dados e a descrição é o que será apresentado ao usuário final, Valor = S e Descrição = Sim. Deste modo, será criado no banco de dados como sendo do tipo VARCHAR (10), isso significa que os valores devem ter no máximo esse comprimento.

**b) Padrão:** Será apresentado como uma caixa de texto de apenas uma linha. O campo será criado no Banco de Dados como sendo do tipo VARCHAR (100).

**c) Caixa de texto:** Será apresentado como uma caixa de texto que comporta várias linhas (também conhecido como campo memo). O campo será criado no Banco de Dados como sendo VARCHAR2 (4000) Oracle ou TEXT no SQLServer.

**d) Formatação HTML:** Tem sua apresentação como uma caixa de texto que comporta várias linhas. Ao utilizar esta opção combinada com o campo **"Tipo de dados"** configurado com a opção **"Texto Longo (CLOB)"**, tem-se a possibilidade de realizar o upload de imagens para telas no formato HTML5. Este campo será criado no Banco de Dados como sendo VARCHAR2 (4000) Oracle ou TEXT no SQLServer. Desse modo, pode-se adicionar quantas imagens forem necessárias, sendo que cada uma delas poderá conter somente 500kb.

- **Hora:** Esta opção representa os valores de hora. O campo será criado no banco de dados como sendo do tipo NUMBER (5) Oracle e SMALLINT SQLServer. Diante dessas informações, o sistema irá apresentá-lo com a máscara 999:99.

A marcação **"Permite pesquisa?"** define se o campo poderá ser utilizado como critério de pesquisa no componente.

Ao habilitar a marcação **"Visível no grid de pesquisa?"**, o campo será exibido na grade de resultados do componente de pesquisa.

Quando a marcação **"Campo calculado"** estiver acionada, indica que este campo não existirá no banco de dados. Deste modo, o seu valor será resolvido por meio do campo Expressão.

O campo **"Expressão"** possui objetivos diferentes dependendo do tipo de campo. Se o campo for calculado, a expressão será utilizada para calcular seu valor final. Já se o campo não for calculado, sendo a expressão informada, ela será utilizada como expressão de UPDATE, ou seja, quando o registro for atualizado, esta expressão será avaliada para resolver o novo valor do campo, e esse valor será gravado no banco de dados.

**Importante:** a expressão utilizará a linguagem em Java em que todos os campos da tabela estão disponíveis para uso com o padrão **"$col\_NOMEDOCAMPO"**, ou seja, se na tela adicional houver um campo denominado CODPARC, então este será referenciado no script como **"$col\_CODPARC"**.

**Nota:** é necessário observar que neste caso existe uma diferenciação entre letras maiúsculas e minúsculas.

Ainda nesse contexto, os tipos das variáveis referentes aos campos são equivalentes ao tipo da coluna no banco de dados. Vejamos sobre cada uma delas:

- **Numéricas: java.math.BigDecimal** - Esta informação vale para qualquer coluna numérica, independente de ser inteiro ou ponto flutuante, não importando sua precisão.
- **Texto: java.lang.String** - Esse caso, aplica-se a qualquer tipo de coluna texto, independente da largura ou tipo primitivo do banco de dados.
- **Data: java.sql.Timestamp** - Estes tipos são independentes do banco de dados, ou seja, não importa se é SQL Server ou Oracle.

#### Botão Importar Campo

Este botão permite importar para a tela do sistema um campo de outra tabela (seja ela adicional ou nativa do sistema).

**Observação:** esta opção deverá ser utilizada quando houver a necessidade de se criar um campo que faça referência a outra tabela.

![Imagem 10: Observação: esta opção deverá ser utilizada quando houver a necessidade de se criar um campo que faça referência a…](https://ajuda.sankhya.com.br/hc/article_attachments/4408065756439)

Esta ação é semelhante a criação de uma chave estrangeira para a outra tabela. Desse modo, ao acioná-lo será apresentado o pop-up **"Importar campo"** que permite selecionar a origem do campo.

![Imagem 11: Esta ação é semelhante a criação de uma chave estrangeira para a outra tabela. Desse modo, ao acioná-lo será…](https://ajuda.sankhya.com.br/hc/article_attachments/4408065860631)

**Importante:** após a importação de um campo, o sistema irá automaticamente relaciona-lo à chave primária na aba [Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abaligaes) .

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abacampos) 

#### Botão Atributos

Por meio das funcionalidades deste botão, os atributos dos campos poderão ser editados. Além disso, você pode realizar configurações em relação aos campos adicionais.

![Imagem 12: Por meio das funcionalidades deste botão, os atributos dos campos poderão ser editados. Além disso, você pode realizar…](https://ajuda.sankhya.com.br/hc/article_attachments/4408065911575)

Ao acionar o referido botão, o sistema irá apresentar o pop-up **"Atributos de campo adicional"**:

![Imagem 13: Ao acionar o referido botão, o sistema irá apresentar o pop-up "Atributos de campo adicional" :](https://ajuda.sankhya.com.br/hc/article_attachments/4408072987287)

Inicialmente, você pode definir se o campo será **"Requerido"** (campo indispensável). Além disso, se o campo adicional será **"Visível"** ou não, se possuirá características de **"Somente Leitura"** ou leitura e edição (se desmarcado) ou ainda se o campo deverá constar em uma aba específica, para esse último caso você deve preencher o campo com o **"Nome da aba"**.

Quando acionada a marcação **"Permite valor nulo"**, o campo adicional que está sendo criado ou editado aceitará em sua utilização valores nulos.

**Observação:** conceitualmente, um valor nulo ou NULL é diferente de zero (0), espaços em branco ou uma cadeia de caracteres de comprimento zero como ""; NULL significa que nenhuma entrada foi feita. Diante disso, quando um campo não permitir valor nulo (opção desmarcada) deve-se obrigatoriamente, selecionar a marcação Requerido, o que deverá ocorrer na criação ou alteração do campo.

Temos também o campo **"Nome do agrupamento"**, que permite criar uma espécie de grupo dentro da aba.

**Nota:** caso seja necessário que um conjunto de campos seja apresentado na mesma aba e/ou mesmo agrupamento necessariamente deverão ser preenchidos os campos Nome da aba e Nome do agrupamento com valores iguais para todos os campos que ficarão na aba e/ou agrupamento em referência.

Ainda com relação à configuração dos campos adicionais, ao acionar a marcação **"Mostra soma no rodapé da grade"** considerando que os campos tratem de Número inteiro ou Número decimal, o procedimento será devidamente realizado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#abacampos)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)

## Aba Ligações

Por meio meio desta aba, você pode realizar configurações específicas relacionadas aos campos.

![Imagem 14: Por meio meio desta aba, você pode realizar configurações específicas relacionadas aos campos.](https://ajuda.sankhya.com.br/hc/article_attachments/4408073325975)

Para efetuar um lançamento, é necessário acionar o botão **"Novo"** destacado na imagem acima. Deste modo, será disponibilizado o pop-up **"Criar Ligação"** sendo necessário proceder com seus devidos registros selecionando o destino da ligação, e posteriormente, os campos da ligação.

![Imagem 15: Para efetuar um lançamento, é necessário acionar o botão "Novo" destacado na imagem acima. Deste modo, será…](https://ajuda.sankhya.com.br/hc/article_attachments/4408066349847)

Após realizar os procedimentos mencionados, o sistema efetuará os devidos registros, conforme abaixo:

![Imagem 16: Após realizar os procedimentos mencionados, o sistema efetuará os devidos registros, conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/4408066381335)

Assim, o sistema preencherá automaticamente os campos **"Origem dos Dados"**, **"Adicional"** e **"Nome Interno"**. Além disso, serão inseridos registros também na grade **"Campos"**, considerando **"Campo Local"** e **"Campo na Origem"**.

**Observação:** as ligações podem ser realizadas entre os campos do formulário formatado e outras instâncias.

#### Botão Avançado

O botão ![Imagem 17: O botão está localizado na parte superior da grade, ao acioná-lo será aberto o pop-up "Atributos da ligação" para que…](https://ajuda.sankhya.com.br/hc/article_attachments/4408073459223) está localizado na parte superior da grade, ao acioná-lo será aberto o pop-up **"Atributos da ligação"** para que sejam realizadas as configurações necessárias.

![Imagem 18: O botão está localizado na parte superior da grade, ao acioná-lo será aberto o pop-up "Atributos da ligação" para que…](https://ajuda.sankhya.com.br/hc/article_attachments/4408073473047)

No **"Campo para apresentação"** defina qual campo será utilizado no lado direito da pesquisa. Quando se tratar de uma configuração específica, o mais indicado é utilizar o valor padrão.

Utilize o campo **"Expressão da ligação"** para filtrar a pesquisa, ou seja, sempre que a pesquisa for aberta, uma vez que toda ligação é apresentada na tela como um componente de pesquisa, o filtro será aplicado.

Por meio do campo **"Filtro de formulário"**, tem-se os valores digitados na própria tela como filtro de ligação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)

## Aba Eventos

Esta aba permite realizar as configurações de eventos considerando as entidades. Os eventos são mecanismos que podem executar ações utilizando a Rotina de Banco de dados (Stored Procedure) ou a Rotina Java de acordo com a regra de negócio utilizada e considerando os lançamentos nas respectivas entidades.

![Imagem 19: Esta aba permite realizar as configurações de eventos considerando as entidades. Os eventos são mecanismos que podem…](https://ajuda.sankhya.com.br/hc/article_attachments/4408073781527)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)

## Botão Outras Opções

Em relação ao botão ![Imagem 20: Em relação ao botão l ocalizado no Cabeçalho desta tela, o sistema dispõe das seguintes funcionalidades:](https://ajuda.sankhya.com.br/hc/article_attachments/4408066808599) localizado no Cabeçalho desta tela, o sistema dispõe das seguintes funcionalidades:

**Checar integridade de campos acionais:** Por meio desta opção você pode verificar se todos os campos adicionais de acordo com a tabela realmente existem no banco de dados e estão com seu tipo em conformidade.

**Reiniciar esta unidade de dados:** Utilizando esta opção, o sistema descartará as caches internas e procederá com a releitura do dicionário de dados desta tela no banco de dados.

**Observação:** esta opção poderá ser utilizada quando ocorrem alterações na estrutura da tela, por exemplo, a adição de um campo, ou a realização de uma nova ligação e estas alterações não aparecem imediatamente na tela em execução.

Diante desse contexto, considerando que tenha sido efetuada a reinicialização, o sistema apresentará a seguinte mensagem:

**"Unidade de dados reiniciada com sucesso!"**.

**Definir ordem dos campos:** Acionando esta opção, você pode definir a ordem em que os campos irão aparecer na tela por padrão.

**Nota:** esta ordem poderá ser alterada pelo usuário ou configurada através desta opção.

**Metadados:** Por meio desta opção, tem-se as funcionalidades **"Exportar Metadados"** e **"Importar Metadados"** que permitem o compartilhamento de Módulos Adicionais entre ambientes distintos.

![Imagem 21: Para mais detalhes sobre esse conteúdo, acesse a documentação Exportação e Importação de Telas Adicionais .](https://ajuda.sankhya.com.br/hc/article_attachments/16109771818903) Para mais detalhes sobre esse conteúdo, acesse a documentação [Exportação e Importação de Telas Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)

## Considerações Finais

Os formulários formatados são utilizados no processo considerando o conteúdo exibido aos usuários na execução.

**Vinculação do formulário formatado**

Para realizar a vinculação de um formulário formato a um determinado processo, é indispensável que sejam considerados os seguintes pontos:

1. Inicialmente, você deve acessar a tela [Processos de Negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio);

2. Depois acione o botão ![Imagem 22: 2. Depois acione o botão "Visualizar Diagrama BPMN" localizado no topo da tela mencionada, para visualizar o diagrama…](https://ajuda.sankhya.com.br/hc/article_attachments/4408074193943) **"Visualizar Diagrama BPMN"** localizado no topo da tela mencionada, para visualizar o diagrama do processo;

3. Na sequência clique duas vezes sobre o elemento **"Tarefa de Usuário"** contido no diagrama para realizar as devidas configurações;

![Imagem 23: Para mais detalhes sobre esse conteúdo, acesse a documentação Tarefas .](https://ajuda.sankhya.com.br/hc/article_attachments/16109771818903) Para mais detalhes sobre esse conteúdo, acesse a documentação [Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360034481774-Processos-de-Neg%C3%B3cio#tarefas).

4. Após este passo, no diagrama deve-se proceder com a vinculação do formulário formatado criado nesta tela, adicionando-o na aba **"Formulário Formatado"** localizada no [Painel de Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107733-Processos-de-Neg%C3%B3cio#paineldepropriedades).

Ao relacionar um formulário formatado à um processo, é necessário definir a quantidade de registros permitidos para a execução do processo. Deste modo, preenchendo o campo **"Quantidade de registros"** contido na aba mencionada, consideram-se os seguintes pontos:

- Ao selecionar a opção **"Único"**, o sistema permitirá que seja inserido apenas um registro no formulário formatado.
- Considerando a opção **"Vários"** podem ser inseridos inúmeros registros no formulário formatado, sendo estes apresentados em forma de grade.

**Visualização do formulário formatado**

É relevante mencionar que os formulários formatados criados na presente tela e posteriormente configurados de acordo com os pontos mencionados acima, estarão disponíveis para sua respectiva visualização por meio da tela [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360037149534-Lista-de-Tarefas).

**Observação:** os formulários mencionados, relacionam-se a uma tarefa/atividade que está vinculada a um processo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595834-Formul%C3%A1rios-Formatados#top)
