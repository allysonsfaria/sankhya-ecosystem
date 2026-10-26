---
id: "360044597294"
titulo: "Dicionário de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:15Z"
rotulos: ["manual", "Configuração", "Relatórios", "Avançado", "Expressão", "Atributos", "Campo Adicional", "Dicionário de Dados", "MODGRADCONSTTEL", "Texto Longo (CLOB)", "br.com.sankhya.core.cfg.dicionariodados", "Dicionário de Dados manual", "Campos Adicionais", "customização", "Banco de Dados"]
---

# Dicionário de Dados

| ```  Módulo:  Configurações > avançado ``` |
| --- |

---

O Dicionário de Dados é uma ferramenta avançada que permite a customização de telas já existentes no sistema através das tabelas que as formam. Aqui, você terá a liberdade de definir novos campos, com seus respectivos tipos, além de ser possível a criação de novas abas para colocar esses novos campos.

Os campos e abas criadas por esse recurso serão acessados pela tela que utiliza a tabela modificada e vão se parecer e comportar de maneira semelhante aos campos e abas padrões do sistema.

Pode-se modificar o modo com que a tela é iniciada, ou seja, a forma que a tela será aberta; através da ativação do parâmetro **"Modo grade padrão no Constr. de Telas? - MODGRADCONSTTEL"** tem-se a apresentação inicial da tela em modo grade; com o referido parâmetro desligado, teremos a abertura da tela em modo formulário.

O sistema cria as colunas na tabela no banco de dados para manter os dados inseridos em campos, dessa forma, é possível utilizar as informações onde desejar, como, por exemplo, em relatórios, cubos de decisão, dashboards, regras de validação, entre outros. Assim, você pode utilizar os links a seguir para saber mais:

| [Criação de um Campo Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#criandoumcampoadicional) |  | [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abacampos) |
| --- | --- | --- |
| [Aba Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaligaes) |  | [Aba Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaaes) |
| [Aba Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaeventos) |  | [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#botooutrasopes) |
| [Campos que permitem alteração de tamanho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#camposquepermitemalteraodetamanho) |  |  |

![Imagem 1: Campos que permitem alteração de tamanho](https://ajuda.sankhya.com.br/hc/article_attachments/4421251678615)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Criação de um Campo Adicional

Para adicionar um campo personalizado, selecione uma tabela através da grade principal da tela, mostrada na figura acima. Assim, é possível utilizar o filtro rápido para encontrar a tabela facilmente, e na sequência, clique no botão ![Imagem 2: Para adicionar um campo personalizado, selecione uma tabela através da grade principal da tela, mostrada na figura…](https://ajuda.sankhya.com.br/hc/article_attachments/16242640187159) **"Novo"** no painel de controle da parte central da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

Aba Campos

Nessa aba, será configurado o campo adicional. Além de botões que o permitirão realizar configurações dos campos, serão estes:

| [Botão Importar Campo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#bot%C3%A3oimportarcampo) |  | [Botão Atributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#bot%C3%A3oatributos) |  | [Botão Proteção de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#bot%C3%A3oprote%C3%A7%C3%A3odedados) |
| --- | --- | --- | --- | --- |

Observe a seguir, os campos disponíveis na aba:

**Nota:** quando comprar uma solução pelo Place e esta for protegida, alguns campos não ficarão disponíveis para visualização nesta aba. 

Em **"Nome do campo"**, você informará o nome interno do campo, ou seja, o nome que ele terá na tabela do banco de dados.

Informe em **"Descrição do Campo"**, a descrição do campo que será apresentada em todas as situações onde ele apareça como na própria tela, grades, telas de pesquisa, relatórios rápidos, entre outros.

Defina no campo **"Tipo de Dados"**, o tipo do campo no banco de dados. Aqui, você poderá escolher dentre as seguintes opções:

- **Texto Longo (CLOB):** Definindo-se pela utilização deste tipo de dado, será possível inserir uma grande quantidade de informações no campo. Além disso, pode-se também alterar algumas características da fonte do texto informado no campo, deixando este em Negrito, Itálico ou Sublinhado e ainda, inserir Marcadores.
- **Conteúdo Binário:** Esse tipo de dados é utilizado para campos do tipo Imagem, Arquivo e Múltiplos Arquivos. Sendo que, quando o campo **"Apresentação"** estiver configurado com a opção **"Múltiplos Arquivos"**, será possível anexar ao campo, links que poderão ser copiados, ou então, o redirecionamento direto para a página pertencente ao link.
- **Data e Hora:** Estes, servirão para representar a data e hora respectivamente. Esse campo é criado no BD como sendo tipo DATETIME sqlserver. Esse campo permite que seja feita a digitação da hora.
- **Número Decimal:** Serve para representar valores numéricos com decimais, ou valores de moeda. O campo será criado no banco de dados como sendo do tipo FLOAT.
- **Hora:** Será utilizado para representar valores de hora. O campo será criado no BD como sendo do tipo NUMBER(5) para Oracle e SMALLINT para sqlserver. O sistema vai apresentá-lo com a máscara 999:99
- **Número Inteiro:** Serve para representar números sem a parte decimal (inteiros), ideal para códigos. Será criado no banco de dados como o tipo NUMBER (10) Oracle e INT sqlserver.
- **Texto:** Este tipo de campo é curinga, e dependendo do Tipo de **"Apresentação"** será apresentado de maneiras diferentes pelo sistema. Observe:

**Lista de opções:** Será apresentado como caixa de seleção. Os itens da caixa de seleção são informados no botão Opções que fica disponível ao lado do campo Tipo de Apresentação. Nela, você definirá a lista de valores usando pares Valor/Descrição. O valor é o que será gravado no banco de dados e a descrição é o que será apresentado ao usuário final, por exemplo: Valor = **S**, Descrição = **Sim**. Será criado no banco de dados como sendo do tipo VARCHAR(10), isso significa que os valores devem ter no máximo esse comprimento.

**Padrão:** Exibirá uma caixa de texto de apenas uma linha, e o campo será criado no banco de dados como o tipo VARCHAR(100).

**Caixa de texto:** Mostrado como caixa de texto que comporta várias linhas de texto (também conhecido como campo memo). O campo será criado no banco de dados como VARCHAR2(4000) Oracle, ou TEXT no sqlserver.

**Formatação HTML:** Tem sua apresentação como uma caixa de texto que comporta várias linhas de texto. Ao utilizar está opção combinada com o campo **"Tipo de dados"** configurado com a opção **"Texto Longo (CLOB)"**, teremos a possibilidade de realizar o upload de imagens para telas no formato HTML5. Será possível adicionar quantas imagens forem necessárias, sendo que cada uma delas poderá conter somente 500kb.

O campo **"Apresentação"** possibilita que você configure o formato que o campo será apresentado para utilização. São disponibilizadas as seguintes opções:

- Formatação HTML;
- Imagem;
- Múltiplos Arquivos;
- Checkbox;
- Padrão;
- Caixa de Texto;
- Anexo;
- Lista de Opções (Combobox);
- Múltiplos arquivos.

**Nota:** a opção Anexo só poderá ser utilizada quando o camp**o** Tipo de dados**estiver configurado com a opção** **"Conteúdo Binário".**

Em **"Permite pesquisa?"**, determine se o campo poderá ser usado como critério de busca no componente de pesquisa.

No campo **"Vísivel no grid de pesquisa?"**, será definido o campo a ser exibido na grade de resultado do componente de pesquisa.

O **"Campo calculado?"** determinará que o campo em questão será calculado, portanto, ele não vai existir no banco de dados. Seu valor será resolvido através do campo de expressão.

Referente ao campo **"Expressão"**, destacamos as seguintes considerações:

Ao criar um campo adicional e definir uma expressão, é essencial assegurar que o tipo de dado retornado por ela seja compatível com o tipo definido para o campo criado. Por exemplo:

Caso seja configurado um campo do tipo **"Inteiro"** e seja fornecido uma expressão que retorna um valor do tipo **"Data"**, o sistema enfrentará problemas na conversão dos valores, gerando o seguinte erro:

**"Valor não conversível para campo numérico."**

Este problema ocorre porque a expressão não atende ao formato esperado pelo campo, levando a falhas no processamento. Portanto, é necessário garantir que a expressão e o campo compartilhem o mesmo tipo de dado para evitar incompatibilidades.

Além disso, a expressão terá objetivos calculados, sendo necessário utilizar um padrão para que a consulta funcione corretamente. A expressão deve ser precedida de **'#type.sql#'** e a consulta deve retornar apenas uma linha. Observe a seguir, um exemplo de uma expressão correta em um campo:

**'#type.sql#** **SELECT NUBCO FROM TGFFIN WHERE NUFIN = 1450'**.

Note que no WHERE temos apenas um registro. Caso tivéssemos **'WHERE NUFIN > 1450'** a consulta não iria funcionar.

A expressão é sempre escrita em **Java**, e todos os campos da tabela estão disponíveis para uso com o padrão **"$col\_NOMEDOCAMPO"**, ou seja, se na tabela houver um campo chamado CODPARC então este será referenciado no script como $col\_CODPARC (maiúsculas e minúsculas são consideradas). Os tipos das variáveis referentes aos campos são equivalentes ao tipo da coluna no banco de dados, como exposto:

|  | ![Imagem 3: A expressão é sempre escrita em Java , e todos os campos da tabela estão disponíveis para uso com o padrão…](https://ajuda.sankhya.com.br/hc/article_attachments/42310594603799) |  |
| --- | --- | --- |

|  | Equivale para qualquer coluna numérica, independente de ser inteiro ou ponto flutuante e também não importa a precisão. |  |
| --- | --- | --- |

---

|  | ![Imagem 4: Equivale para qualquer coluna numérica, independente de ser inteiro ou ponto flutuante e também não importa a precisão.](https://ajuda.sankhya.com.br/hc/article_attachments/42310655487255) |  |
| --- | --- | --- |

|  | Este, corresponde para qualquer tipo de coluna texto, independente da largura ou tipo primitivo do banco de dados. |  |
| --- | --- | --- |

```
    Se a coluna do tipo CLOB ou TEXT o tipo da coluna no script será char[] (array de
                  caracteres).
```

---

|  | ![Imagem 5: Este, corresponde para qualquer tipo de coluna texto, independente da largura ou tipo primitivo do banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/42310655487895) |  |
| --- | --- | --- |

|  | Esses tipos são independentes do banco de dados, ou seja, não importa se é SQL Server ou Oracle ou qualquer outro. |  |
| --- | --- | --- |

Além das variáveis com os valores das colunas temos outras variáveis interessantes:

**$sql**

É uma referencia a um objeto do tipo easysql. Esse tipo de objeto possui métodos que permitem a execução de consultas SQL de forma simples, no próprio banco de dados configurado da aplicação. Segue exemplo de uso:

```
$sql.setParam(“PARCEIRO”, $col_CODPARC );   // a tabela local possui um campo chamado
 CODPARC

$sql.select (“P.NOMEPARC,C.NOMECID”,”TGFPAR P INNER JOIN TSICID C ON(C.CODCID = P
.CODCID)”, “P.CODPARC = {PARCEIRO}”)

Nomeparc = “”;

Nomecidade = “”;

If( $sql.next() ){  //  verdadeiro se houver pelo menos uma linha de resultado nomeparc =
$sql.getstring(1);nomecidade = $sql.getstring(2);}

return nomeparc + “ ” + nomecidade;
```

E exemplo acima faz uma consulta na tabela de parceiros e obtém o nome do parceiro e o nome da cidade, então monta um texto de retorno em que associa os dois campos.

```
 $usuario_logado
```

Acima, é exposto o código do usuário logado (tipo java.math.bigdecimal);

```
 $dh_atual
```

Aqui, foi apresentado a data e hora atual (tipo java.sql.Timestamp);

```
 $d_atual
```

Expõe-se neste, a data atual do sistema. Considere ainda, que esse valor não contém horas (tipo java.sql.Timestamp).

**Nota:** no campo Tipo de dados, na escolha do tipo Texto Longo (CLOB), é necessário que no campo Apresentação, escolha a opção Formatação HTML, onde o armazenamento do campo criado será na forma HTML permitindo sua utilização em outras aplicações fazendo com que este receba as formatações definidas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abacampos)

# Botão Importar Campo

Por meio do botão Importar Campo localizado no alto da aba Campos, é possível importar para a tela do sistema um campo de outra tabela, sendo ela adicional ou oficial do sistema. Isso é equivalente a criar uma chave estrangeira para a outra tabela.

Essa opção deve ser usada sempre que desejar criar um campo que faça referência a outra tabela. Como, por exemplo, de uma tabela que faz referência a outra, podemos citar uma tabela de Parceiros que faz referência a tabela de Cidades, ou seja, na tabela de Parceiros possuímos um campo com o código da cidade de domicílio do parceiro, assim quando o sistema monta a tela o formulário possuirá um campo com o código na esquerda e o nome da cidade à direita e um botão para pesquisar cidades.

[GIF animado: Imagem 6: Essa opção deve ser usada sempre que desejar criar um campo que faça referência a outra tabela. Como, por exemplo, de…](https://ajuda.sankhya.com.br/hc/article_attachments/4421134018199)

Ao importar um campo de uma tabela estrangeira, o sistema só poderá importar a chave primária dessa tabela, logo a tela **"Informações do campo"** se apresentará preenchida.

As informações das colunas **"Campo Local"** e **"Descrição Local"** poderão ser alteradas, permitindo a opção de criar mais de um relacionamento para a mesma tabela, ou seja, mais de uma FK para a mesma tabela destino. Dessa forma, considere o exemplo:

Poderá ocorrer a relação de um contrato com o parceiro do contrato e com o parceiro atendido, entre outros. Para isso, bastará incluir mais de um campo **"Cód. Parceiro"** e dar a cada um, um nome diferente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abacampos)

# Botão Atributos

![Imagem 7: Botão Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/4421254192663)

As configurações dos campos adicionais poderão ser feitas através do botão **"Atributos"**. Assim, ao clicá-lo o pop-up **"Atributos de campo adicional"** será exibido:

![Imagem 8: As configurações dos campos adicionais poderão ser feitas através do botão "Atributos" . Assim, ao clicá-lo o pop-up…](https://ajuda.sankhya.com.br/hc/article_attachments/4421239240471)

Primeiramente, defina se o campo será **"Requerido"** ou não.

Quando a marcação **"Permite valor nulo"** for habilitada, irá viabilizar que o campo adicional que está sendo criado ou editado, aceitará em sua utilização, valores nulos (conceitualmente, um valor nulo ou NULL é diferente de zero (0), espaços em branco ou uma cadeia de caracteres de comprimento zero como ""; NULL significa que nenhuma entrada foi feita; a presença de valor NULL, normalmente implica que o valor é desconhecido ou indefinido). Por padrão, essa marcação é apresentada realizada. Quando um campo não permitir valor nulo (opção desmarcada), deve-se obrigatoriamente, marcar o campo como **"Requerido"**, o que deve ocorrer na criação ou alteração do campo.

Defina também, se o campo será **"Visível"** ou não, e será **"Somente Leitura"** ou leitura e edição, caso este não seja habilitado. Além de, se o campo deverá constar em uma aba específica, para isso basta preencher o campo com o **"Nome da aba"**.

Teremos também o campo **"Nome do agrupamento"**, que permite criar uma espécie de grupo dentro da Aba.

Se for necessário que um conjunto de campos seja apresentado na mesma aba e/ou mesmo um agrupamento então basta definir o Nome da aba e Nome do agrupamento com valor igual para todos os campos que deverão ficar na aba e/ou agrupamento em questão.

**Nota:** ao deixar o campo Nome da aba sem preenchimento, na maioria das vezes, o sistema colocará o campo na Aba Geral, mas podem haver exceções, em alguns casos aparecerá uma nova aba nomeada **"Informações Adicionais"**.

Ainda na aba Campos, pode-se configurar a funcionalidade de alterar a apresentação de dados (campos de apresentação), que podem ser, Descrição do Produto, Nome da empresa entre outros. Dessa forma, você poderá alterar o conteúdo do campo que será apresentado. Por exemplo, para buscar a empresa, pode-se utilizar a **"Razão Social"** e não seu **"Nome Fantasia"**; e para buscar o produto, é possível utilizar o **"Complemento"** e não a **"Descrição"**.

Para realizar esta configuração, siga os seguintes passos:

Acesse a tela Dicionário de Dados, em seguida, busque a tabela na qual será realizada a alteração, e cadastre um campo adicional, para esses exemplo, considere a tabela TCBANA, sendo:

|  | ![Imagem 9: Acesse a tela Dicionário de Dados , em seguida, busque a tabela na qual será realizada a alteração, e cadastre um campo…](https://ajuda.sankhya.com.br/hc/article_attachments/42310594605463) |  |
| --- | --- | --- |

No campo **"Expressão"**, confgure uma função que possui a seguinte sintaxe:

```
  return $col_NOMECAMPO1 + " " + $col_NOMECAMPO2;
```

O registro ficará da seguinte forma:

![Imagem 10: O registro ficará da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/4421283129623)

Em seguida, acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834), e realize o cadastro de um parâmetro para vincular o novo campo criado no item anterior. Esse parâmetro servirá para o sistema substituir o valor do campo (apresentação), pelo valor da expressão configurada no campo adicional criado. O parâmetro deve possuir a seguinte configuração:

|  | ![Imagem 11: Em seguida, acesse a tela Preferências , e realize o cadastro de um parâmetro para vincular o novo campo criado no item…](https://ajuda.sankhya.com.br/hc/article_attachments/42310655489559) |  |
| --- | --- | --- |

Assim, o registro ficará da seguinte forma:

![Imagem 12: Assim, o registro ficará da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/4421271570199)

Portanto, o sistema irá substituir pelo valor da expressão configurada no campo adicional.

Ainda referente à configuração dos Campos Adicionais, quando o campo Tipo de Dados, estiver com as opções **"Número Decimal"** ou **"Número Inteiro"** selecionados, será possível de executar a soma dos mesmo no rodapé da coluna. Para isso, realize a marcação **"Mostra no rodapé da grade"**.

![Imagem 13: Ainda referente à configuração dos Campos Adicionais, quando o campo Tipo de Dados , estiver com as opções "Número…](https://ajuda.sankhya.com.br/hc/article_attachments/4421375071767)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abacampos)

# Botão Proteção de Dados

Para que você possa editar os campos que abrangem o botão Proteção de Dados ligue o parâmetro **"Habilitar Proteção Avançada de Dados - PROTDADOSAVANC"**, desta forma, quando você acessar telas que podem conter dados pessoais ou sensíveis, os dados estarão anonimizados.

Ainda com com o parâmetro ligado a anonimização desses dados, eles não serão realizados se você estiver logado com um usuário SUP.

Após clicar no botão, o sistema exibirá o pop-up Proteção de Dados onde você poderá realizar suas definições:

[GIF animado: Imagem 14: Após clicar no botão, o sistema exibirá o pop-up Proteção de Dados onde você poderá realizar suas definições:](https://ajuda.sankhya.com.br/hc/article_attachments/360093362914)

**Observação:** para anonimizar o CPF de Parceiros Pessoa Física, não é necessário que você realize nenhuma alteração no Dicionário de Dados, essa informação já vira anonimizada automaticamente.

Referente aos campos exibidos na imagem acima, teremos:

Por meio do campo **"Classificação do Campo"**, você definirá qual tipo de dados serão anonimizados, ou seja, se para uma determinada tela você utilizar a opção **"Sensível"**, não será possível visualizar os dados. Você também poderá criar mais tipos de dados a serem anonimizados, para tal basta utilizar a tela [Classificação de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057136673) e posteriormente vincular esta classificação na tela [Grupo de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596134), aba **"Exceções para Proteção de Dados"**.

O campo **"Classificação"** irá associar as regras e as exceções aos campos.

Em **"Tipo de anonimização"** será definido o tipo de anonimização que ocorrerá na tela em que as configurações que serão realizadas.

Na **"Regra"** defina a forma que os dados do campo serão exibidos.

Ao selecionar a marcação **"Identificar titular"**, você poderá identificar diretamente o usuário por meio de seus seus dados, como seu nome completo.

**Nota:** as opções selecionadas nessa tela para Proteção de Dados, não poderão ser editadas ou excluídas. Porém, você poderá alterar as classificações inseridas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abacampos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Aba Ligações

Após a importação de um campo, o sistema o relaciona a chave primária automaticamente na aba **"Ligações"**, isso significa que no momento da visualização da nova tela, este campo será apresentado para pesquisa de parceiros.

Além disso, a aba também dispõe de dois botões, sendo eles:

| [Botão Avançado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#bot%C3%A3oavan%C3%A7ado) |  | [Botão Filtro de Formulário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#bot%C3%A3ofiltrodeformul%C3%A1rio) |
| --- | --- | --- |

![Imagem 15: Botão Filtro de Formulário](https://ajuda.sankhya.com.br/hc/article_attachments/4421286435351)

# Botão Avançado

Ao acioná-lo, o pop-up **"Atributos da ligação"** será exibido:

![Imagem 16: Ao acioná-lo, o pop-up "Atributos da ligação" será exibido:](https://ajuda.sankhya.com.br/hc/article_attachments/4421286937623)

Em **"Campo para apresentação"**, será definido qual campo será utilizado no lado direito da pesquisa; assim, observe o exemplo abaixo:

Suponhamos que você não queira que o nome do parceiro seja apresentado no campo lateral da pesquisa nas pesquisas de parceiro, mas sim outro campo qualquer. Nessa situação, essa opção pode ser marcada.

É uma configuração bem específica, e na maioria das vezes o valor padrão é o mais indicado.

No campo **"Expressão da ligação"**, será utilizado para filtrar a pesquisa, ou seja, sempre que a pesquisa for aberta o filtro será aplicado; considerando que, toda ligação é apresentada na tela como um componente de pesquisa. Dessa forma, supondo a criação de uma ligação com Parceiro e que na pesquisa devam ser exibidos apenas os parceiros clientes, para isso, a expressão do filtro seria: **this.CLIENTE = 'S'**.

### Restrição no uso de filtros de formulário em ligações com valor padrão

Ao configurar filtros na aba Ligações do Dicionário de Dados, é importante observar que, quando o campo possui **valor padrão em layouts utilizados nas centrais (Venda, Compra , etc)** o sistema tenta aplicar esse valor automaticamente na inclusão de um novo registro.

Se o filtro da ligação depender de um campo que ainda não foi preenchido na tela, o sistema não conseguirá aplicar o filtro corretamente, podendo ocorrer erro na inclusão. Para evitar esse comportamento, recomenda-se:

- Remover o filtro da ligação, ou;
- Remover o valor padrão do campo.

Referente ao campo **"Filtro de formulário"**, é possível utilizar os valores digitados na própria tela como filtro de ligação. Por exemplo:

**this.NOMEPARC lilke 'form.PRIMEIRONOME%'** - Dessa forma, teremos o **'PRIMEIRONOME'**, que neste exemplo, será um campo da tela, e seu valor será utilizado para filtrar a pesquisa.

**Nota:** os Campos para apresentação, são os campos afetados pela configuração realizada no parâmetro **"Padrão para DESCRIÇÃO dos cadastros - PADRAOENTRDADOS"**; esse parâmetro define a padronização na forma como os dados serão inseridos nos cadastros. Este indicará como a informação do campo de descrição dos cadastros será salva no banco de dados, se em letra maiúscula, minúscula, ou da forma que for efetuada a digitação. 

[[Voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaligaes)

# Botão Filtro de Formulário

Por meio do botão Filtro de formulário, o sistema apresentará o pop-up **"Filtro de formulário"**, onde você poderá criar filtros de formulário nos campos que são originais do sistema, de modo que será possível definir regras de pesquisa para os campos:

![Imagem 17: Por meio do botão Filtro de formulário , o sistema apresentará o pop-up "Filtro de formulário" , onde você poderá criar…](https://ajuda.sankhya.com.br/hc/article_attachments/4421299977111)

[[Voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaligaes) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Aba Ações

A configuração dessa aba, permite que no Sankhya Om sejam executadas tarefas específicas de forma rápida e simples.

![Imagem 18: A configuração dessa aba, permite que no Sankhya Om sejam executadas tarefas específicas de forma rápida e simples.](https://ajuda.sankhya.com.br/hc/article_attachments/32050767800087)

No campo **"Tipo"** será possível definir a execução de uma **"Rotina** **no Banco de Dados"**,  **"Rotina Java"**, ou **"Script (JavaScript)"**, além da configuração de um **"Lançador"** para uma tela do sistema. Cada uma dessas opções quando escolhida, disponibiliza configurações diferentes a serem efetuadas. 

Para saber mais sobre o comportamento de cada uma dessas opções, acesse o artigo [Construtor de Telas/Dicionário de Dados - Aba Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es).

Na lupa do campo **"Filtro de Telas"** você realiza a seleção de telas para os filtros. Essa seleção é feita pelo **"ID"** da tela.

**Observação:** para as Centrais de Notas, devem ser utilizados os ID's conforme cada tipo de movimento. Abaixo trouxemos os tipos de movimento com os respectivos ID's:

- **Tipo de Movimento V:** br.com.sankhya.com.cac.Notas
- **Tipo de Movimento P:** br.com.sankhya.com.cac.Pedidos
- **Tipo de Movimento D:** br.com.sankhya.com.cac.Devolucoes
- **Tipo de Movimento A:** br.com.sankhya.com.cac.ConhecimentoTransporte
- **Tipo de Movimento O:** br.com.sankhya.com.caf.Pedidos
- **Tipo de Movimento C:** br.com.sankhya.com.caf.Notas
- **Tipo de Movimento E:** br.com.sankhya.com.caf.Devolucoes
- **Tipo de Movimento H:** br.com.sankhya.com.caf.ConhecimentoTransporte
- **Tipo de Movimento T:** br.com.sankhya.com.cai.Transferencia
- **Tipo de Movimento J:** br.com.sankhya.com.cai.PedidosRequisicao
- **Tipo de Movimento Q:** br.com.sankhya.com.cai.Requisicao
- **Tipo de Movimento L:** br.com.sankhya.com.cai.DevolucaoRequisicao
- **Tipo de Movimento F:** br.com.sankhya.prod.cac.NotaDeProducao

Ao realizar a marcação "Controla Acesso", será definido que somente usuários com permissão poderão ter acesso às ações configuradas, sendo elas telas próprias do sistema ou telas adicionais. Dessa forma, por meio da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), você poderá controlar a utilização e repasse de uso das ações elaboradas.

**Importante:** para que a ação apareça na tela de Acessos e possa ter sua permissão controlada por usuário, é obrigatório preencher o campo **"Filtro de Telas"** com a tela na qual o botão deverá ser liberado. Sem esse vínculo, a ação não será listada na tela de Acessos.

Quando a marcação acima for desabilitada, todos os usuários possuirão acesso às ações, pois o controle não será aplicado.

Ações criadas para uso com Notas Canceladas nos Portais de Compras, Vendas e Movimentações Internas (instância de nome NotaCancelada) não controlam acesso — qualquer usuário com acesso aos portais conseguirá visualizar notas canceladas e executar as ações disponíveis.

> **Diferença entre "Filtro de Telas" e "Id da Tela":** o **Filtro de Telas** define em quais telas a ação ficará disponível para controle de permissão na tela de Acessos. Já o **Id da Tela** restringe a exibição do botão de ação no sistema: se preenchido, o botão aparecerá apenas na tela com aquele resourceID; se não preenchido, o botão seguirá o comportamento padrão por entidade.

No campo "Id da Tela" informe o ID da tela à qual a ação estará vinculada. Essa informação é obtida pelo botão com a imagem do perfil no canto superior direito da tela, na opção "Configurar tela".

[GIF animado: Imagem 19: No campo "Id da Tela" informe o ID da tela à qual a ação estará vinculada. Essa informação é obtida pelo botão com a…](https://ajuda.sankhya.com.br/hc/article_attachments/32050878087063)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Aba Eventos

Ao utilizar essa aba, você poderá realizar as configurações de eventos considerando as entidades, sendo elas telas nativas, ou adicionais do sistema.

![Imagem 20: Ao utilizar essa aba, você poderá realizar as configurações de eventos considerando as entidades, sendo elas telas…](https://ajuda.sankhya.com.br/hc/article_attachments/4421373731991)

Os eventos são mecanismos que podem executar ações utilizando a Rotina de Banco de dados (Stored Procedure) ou a Rotina (Java) de acordo com a regra de negócio utilizada e considerando os lançamentos nas respectivas entidades.

Diante disso, observe os seguintes exemplos:

![Imagem 21: Diante disso, observe os seguintes exemplos:](https://ajuda.sankhya.com.br/hc/article_attachments/4421373903895)

![Imagem 22: Para mais detalhes, verifique as informações disponibilizadas no artigo Construtor de Telas/Dicionário de Dados - aba…](https://ajuda.sankhya.com.br/hc/article_attachments/16243057844247) Para mais detalhes, verifique as informações disponibilizadas no artigo [Construtor de Telas/Dicionário de Dados - aba Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es) que dispõe de dados relacionados especificamente a aba Ações; sua utilização se assemelha a aba Eventos.

O botão ![Imagem 23: O botão "Salvar ordem" , permite definir a ordem que os eventos ativos serão executados. Após esse procedimento, você…](https://ajuda.sankhya.com.br/hc/article_attachments/16243057845527) **"Salvar ordem"**, permite definir a ordem que os eventos ativos serão executados. Após esse procedimento, você poderá visualizar na coluna **"Ordem"** a ordenação configurada anteriormente.

![Imagem 24: O botão "Salvar ordem" , permite definir a ordem que os eventos ativos serão executados. Após esse procedimento, você…](https://ajuda.sankhya.com.br/hc/article_attachments/4421374144663)

![Imagem 25: O sistema não sobrescreve os eventos adicionados na instância , uma vez que sua execução se dará após as validações…](https://ajuda.sankhya.com.br/hc/article_attachments/16242932800023) O sistema não sobrescreve os eventos adicionados na instância, uma vez que sua execução se dará após as validações nativas do Enterprise Resource Planning (ERP).

Veja também as informações contidas nas telas [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833) e [Construtor de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Botão Outras Opções

Através do botão Outras Opções, localizado na parte superior da tela, temos as seguintes opções:

- **Processar campos MGE/Mitra:** Essa opção importa os campos adicionais que foram criados no MGE. Como o Sankhya Om usa um dicionário de dados diferente do MGE, o fato de se criar um campo adicional no MGE não faz com que ele esteja disponível no Sankhya Om automaticamente.
- **Processar campos Jiva G1:** Importa os campos adicionais que foram criados no Jiva G1. Como o Jiva Om usa um dicionário de dados diferente do Jiva G1 então o fato de se criar um campo adicional no Jiva G1 não faz com que ele esteja disponível no Jiva Om automaticamente.
- **Checar integridade de campos adicionais:** Verifica se todos os campos adicionais presentes no dicionário de dados para esta tabela realmente existem no banco de dados, e se estão com o tipo correto.
- **Reiniciar esta unidade de dados:** Essa opção faz com que o sistema descarte os cachês internos, e releia o dicionário de dados dessa tela no banco de dados. Pode ser utilizada quando se faz alterações na estrutura da tela, ou seja, pode adicionar um campo, ou uma nova ligação; e essa alteração não aparece imediatamente na tela em execução.
- **Configuração de Pesquisa:** Através dessa opção, você poderá configurar a ordenação e o limite de resultados de uma determinada tabela. Assim, ao ordenar dados em uma tela, será respeitada a configuração feita nos campos **"Ordenação"** e **"Limite de Resultados"**.

![Imagem 26: Consulte também o artigo Configurando Ações Personalizadas .](https://ajuda.sankhya.com.br/hc/article_attachments/16243057844247) Consulte também o artigo [Configurando Ações Personalizadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)

## Campos que permitem alteração de tamanho

Alguns campos terão o seu tamanho definido de acordo com o tamanho do campo criado no banco de dados. Caso ocorra a necessidade de aumentar o tamanho de algum desses campos, você poderá executar o comando diretamente no banco de dados. Abaixo, você pode consultar os campos:

- Nome do Parceiro e Razão Social (TGFPAR.NOMEPARC E TGFPAR,RAZAOSOCIAL) apresentam-se juntos;
- Nome da Cidade (TSICID.NOMECID);
- Nome do Bairro (TSIBAI.NOMEBAI);
- Controle (TGFITE.CONTROLE);
- Nome do Usuário (TSIUSU.NOMEUSU);
- Descrição Padrão do Laudo (TGACLT.DESCRCLT);
- Características Analisáveis (TGACLC.NOMECLC);
- Descrição Abreviada do Bem (TCIBEM.DESCRABREV);
- Descrição do Produto (TGFPRO.DESCRPROD);
- Complemento do Produto (TGFPRO.COMPLDESC);
- Marca do Produto (TGFPRO.MARCA);
- Nome do Vendedor (TGFVEN.APELIDO);
- Histórico (TGFMBC.HISTORICO);
- Expressão (TSIRHI.EXPRESSAO);
- Descrição da TOP (TGFTOP.DESCROPER);
- Descrição da CFOP (TGFCFO.DESCRCFO).

**Nota:** para aumentar o tamanho dos campos citados acima, solicite o DBA da sua Unidade que realize a criação de um script que percorra todas as tabelas que possuam o determinado campo e assim, realizar a devida alteração. Você também possui a alternativa de solicitar para a Indústria Sankhya tal procedimento, uma vez que, esta orçará a criação deste SCRIPT.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#top)
