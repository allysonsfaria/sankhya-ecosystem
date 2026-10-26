---
id: "360045118893"
titulo: "Formulários de Processo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:04Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Formulários", "Processo Produtivo", "Produção", "br.com.sankhya.formularioprocessoinstancia", "Formulários de Processo manual", "Cadastro", "Formulários de Processo", "Eliminando papel", "Atributos e tipos"]
---

# Formulários de Processo

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312795432215) Módulo: Produção > Cadastros
```

---

Na execução de Ordens de Produção existe a necessidade de se transmitir informações entre os envolvidos pela execução da Ordem (Chefe de Produção, Operador de Reator, Técnicos Laboratório, Farmacêutico). Dentre essas informações podemos citar como exemplo:

- Procedimento para execução da atividade;
- Informações técnicas para consulta do operador;
- Resultados das avaliações de regulagem de máquina periódicos;
- Detalhamento para execução da atividade;
- Entre outros.

Deste modo, esta tela tem por finalidade a criação de formulários digitais que servirão para coletar os dados de um apontamento no Processo Produtivo, substituindo assim o papel no "chão de fábrica".

Trataremos neste artigo sobre os seguintes tópicos:

| [Criando um Formulário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#criandoumformulrio) |  | [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#abacampos) |
| --- | --- | --- |
| [Campos como "Lista de Opções"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#camposcomolistadeopes) |  | [Aba Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#abaligaes) |
| [Botão Importar Campo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#botoimportarcampo) |  | [Botão Atributos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#botoatributos) |

                                                                                                           

![Imagem 2: Botão Atributos](https://ajuda.sankhya.com.br/hc/article_attachments/4416795752343)

## Criando um Formulário

Para adicionar um formulário, clique no botão **"Novo"** localizado no Painel de Controle na parte superior da tela. Deste modo, será apresentado o pop-up **"Novo Formulário"**.

![Imagem 3: Para adicionar um formulário, clique no botão "Novo" localizado no Painel de Controle na parte superior da tela. Deste…](https://ajuda.sankhya.com.br/hc/article_attachments/4416795791895)

Inicialmente, você deve informar se o formulário será do tipo **"Processo"** ou **"Atividade"**. Após este passo, serão solicitadas algumas informações a respeito do novo formulário:

![Imagem 4: Inicialmente, você deve informar se o formulário será do tipo "Processo" ou "Atividade" . Após este passo, serão…](https://ajuda.sankhya.com.br/hc/article_attachments/4416795835543)

Informe a **"Descrição do Formulário"** para localiza-lo em todas as rotinas que ele for empregado.

Preencha o **"Nome da tabela no banco de dados"** que mantém as informações do formulário. Este nome será pré-fixado no banco de dados como AD Nome da Tabela, ou seja, se o valor digitado for Definições Embalagem, o nome da tabela será AD\_DEFEMB.

Desta forma, ao clicar no botão ![Imagem 5: Desta forma, ao clicar no botão "Próximo" é necessário informar a chave primária da tabela.](https://ajuda.sankhya.com.br/hc/article_attachments/4416782560919) **"Próximo"** é necessário informar a chave primária da tabela.

![Imagem 6: Desta forma, ao clicar no botão "Próximo" é necessário informar a chave primária da tabela.](https://ajuda.sankhya.com.br/hc/article_attachments/4416782466071)

Para inclusão de campos na chave primária, acione o botão **"Novo"**, e preencha os seguintes dados:

Defina o **"Nome do campo"**, sendo que este nome, não deve possuir espaços em branco nem caracteres especiais; temos aqui um limite de 32 caracteres.

Informe na **"Descrição do Campo"**, o que se refere o campo criado. Este texto será empregado em todos os locais na qual o campo é apresentado, ou seja, formulários, grades, consultas, relatórios rápidos, entre outros.

Determine em **"Tipo de dados"**, o tipo do campo; no nosso exemplo, é o tipo **"Número Inteiro"**. Teremos mais detalhes sobre os tipos campos, na aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#abacampos).

Selecione em **"Apresentação"**, a forma de apresentação do campo. Iremos obter mais detalhes também, na aba Campos.

A marcação **"Permite pesquisa?"**, quando efetuada, permite que o campo seja utilizado como critério de pesquisa.

Se for assinalado a marcação **"Visível no grid de pesquisa?"**, o campo estará visível na grade de resultados da pesquisa.

Ao finalizar a inclusão dos campos, acione o próximo passo do processo.

![Imagem 7: Ao finalizar a inclusão dos campos, acione o próximo passo do processo.](https://ajuda.sankhya.com.br/hc/article_attachments/4416782656919)

Neste passo, você pode definir qual campo da chave-primária será preenchido sequencialmente, de forma automática pelo sistema.

Feita a definição de numeração, clique em ![Imagem 8: Feita a definição de numeração, clique em "Concluir" para determinar o fim do procedimento.](https://ajuda.sankhya.com.br/hc/article_attachments/4416787999767) **"Concluir"** para determinar o fim do procedimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)

## Aba Campos

Nesta aba, configure os campos que serão apresentados/utilizados no formulário que está sendo criado.

![Imagem 9: Nesta aba, configure os campos que serão apresentados/utilizados no formulário que está sendo criado.](https://ajuda.sankhya.com.br/hc/article_attachments/4416788061079)

Após realizar a criação do novo formulário, você pode adicionar os outros campos que irão conter as informações relevantes ao mesmo. Para tal, temos o preenchimento das seguintes informações:

Preencha em  **"Nome do campo"**, a nomenclatura da tabela do banco de dados.

Em **"Descrição do campo"** informe a descrição que irá aparecer em todas as situações na qual o campo for apresentado.

Defina em **"Tipo de Dados"**, o tipo do campo no banco de dados; de acordo com as seguintes opções:

- **Conteúdo Binário:** Este tipo é empregado apenas para imagens e portanto, deve ser utilizado sempre com o tipo Apresentação definido como Imagem.
- **Data:** Representa as informações apenas de data.
- **Data e Hora:** Ambos são criados no Banco de Dados como sendo tipo DATE Oracle e DATETIME SQLServer. A única diferença é na forma de apresentação, pois no caso de Data e Hora o campo permite a digitação da hora.
- **Hora:** Representa-se valores de hora, o campo será criado no banco de dados como sendo do tipo NUMBER(5) para Oracle e SMALLINT para SQLServer. O sistema irá apresentá-lo com a máscara 999:99
- **Número Decimal:** Serve para representar valores numéricos com decimais ou valores de moeda. O campo será criado no banco de dados como sendo do tipo FLOAT.
- **Número Inteiro:** Este tipo representa números sem a parte decimal (inteiros), ideal para códigos. Será criado no banco de dados como sendo do tipo NUMBER (10) Oracle e INT SQLServer.
- **Texto Longo (CLOB):** Definindo a utilização deste tipo de dado, será possível inserir uma grande quantidade de informações no campo. Além disso, será possível alterar algumas características da fonte do texto informado no campo, deixando este em **Negrito**, Itálico ou Sublinhado e ainda, inserir Marcadores.
- **Texto:** Este tipo é curinga, e dependendo da configuração realizada no campo Apresentação será exibido de formas diferentes pelo sistema.

A opção **"Apresentação"**, contém as seguintes alternativas:

- **Caixa de texto:** Será apresentado como uma caixa de texto que comporta várias linhas de texto (também conhecido como campo memo). O campo será criado no banco de dados como sendo VARCHAR2(4000) Oracle ou TEXT no SQLServer.
- **Padrão:** Esta opção, será exibida como uma caixa de texto de apenas uma linha; o campo será criado no banco de dados como sendo do tipo VARCHAR(100).
- **Lista de opções:** Será demostrado como uma caixa de seleção (ComboBox). Os itens da caixa de seleção são informados no botão ![Imagem 10: Lista de opções: Será demostrado como uma caixa de seleção (ComboBox). Os itens da caixa de seleção são informados no…](https://ajuda.sankhya.com.br/hc/article_attachments/4416788186903) **"Opções"** que será apresentado ao lado do campo Apresentação. Nele defina a lista de valores usando pares Valor/Descrição. O valor é o que será gravado no banco de dados e a descrição é o que será apresentado ao usuário final, por exemplo: Valor = S, Descrição = Sim. Será criado no banco de dados como sendo do tipo VARCHAR(10), isso significa que os valores devem ter no máximo esse comprimento.
- **Formatação HTML:** Tem sua apresentação como uma caixa de texto que comporta várias linhas de texto. Ao utilizar esta opção combinada com o campo Tipo de dados configurado com a opção Texto Longo (CLOB), temos a possibilidade de realizar o upload de imagens para telas no formato HTML5. Pode ser adicionado quantas imagens forem necessárias, sendo que cada uma delas poderá conter somente 500kb.

A marcação **"Permite pesquisa?"**, determina se o campo poderá ser utilizado como critério de pesquisa no componente.

Se for assinalado a marcação **"Visível no grid de pesquisa?"**, indica que o campo irá aparecer na grade de resultados do componente de pesquisa.

Ao assinalar essa marcação **"Campo calculado"**, determina que esse campo é calculado, e portanto, não irá existir no banco de dados. Seu valor será resolvido através do campo de expressão.

O campo **"Expressão"**, possui objetivos diferentes dependendo do tipo de campo. Se o campo for Calculado, a Expressão será utilizada para calcular seu valor final. Se o campo não for Calculado, sendo a expressão informada ela será utilizada como expressão de UPDATE, ou seja, quando o registro for atualizado, essa expressão será avaliada para resolver o novo valor do campo, e esse valor será gravado no banco de dados.

Os tipos das variáveis referentes aos campos são equivalentes ao tipo da coluna no banco de dados, conforme abaixo:

- **Numéricas:** java.math.BigDecimal. Esta informação vale para qualquer coluna numérica, independentemente de ser inteiro ou ponto flutuante, não importando sua precisão.
- **Texto:** java.lang.String. Vale para qualquer tipo de coluna texto, independente da largura ou tipo primitivo do banco de dados.

**Nota:** caso a coluna seja do tipo CLOB ou TEXT, o tipo da coluna no script será char[] (array de caracteres).

- **Data:** java.sql.Timestamp. Este tipo é independente do banco de dados, ou seja, podem ser SQL Server, Oracle ou qualquer outro.

Além das variáveis com os valores das colunas, temos outras variáveis interessantes:

- **$sql -** É uma referência a um objeto do tipo EasySQL. Esse tipo de objeto possui métodos que permitem a execução de consultas SQL de forma simples, no próprio banco de dados configurado da aplicação; a seguir temos um exemplo de uso:

```
$sql.setParam(“PARCEIRO”, $col_CODPARC ); //a tabela local possui um campo chamado CODPARC

$sql.select(“P.NOMEPARC,C.NOMECID”,”TGFPAR P INNER JOIN TSICID

C ON(C.CODCID = P.CODCID)”, “P.CODPARC = {PARCEIRO}”);

nomeParc = “”;

nomeCidade = “”;

if( $sql.next() ){ // verdadeiro se houver pelo menos uma linha de resultado nomeParc = $sql.getString(1);
nomeCidade = $sql.getString(2);}

return nomeParc + “ ” + nomeCidade;
```

O exemplo acima faz uma consulta na tabela de Parceiros e obtém o nome do parceiro e o nome da cidade; com isso, é montado um texto de retorno unindo os dois campos.

- **$usuario\_logado -** Código do usuário logado (o tipo é java.math.BigDecimal)
- **$dh\_atual -** Data e hora atual (o tipo é java.sql.Timestamp)
- **$d\_atual -** Data atual do sistema. Esse valor não contém horas (o tipo é java.sql.Timestamp)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)

## Campos como "Lista de Opções"

Quando indicado o campo do tipo **"Texto"**, você pode configurá-lo para que na sua utilização, tenha um campo com o formato Lista de Opções (Combobox). Para isso, defina o campo **"Apresentação"** com a opção **"Lista de Opções"**:

![Imagem 11: Quando indicado o campo do tipo "Texto" , você pode configurá-lo para que na sua utilização, tenha um campo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/4416788860823)

Desta maneira, através do botão ![Imagem 12: Desta maneira, através do botão Opções será aberto um pop-up onde serão cadastradas as possibilidades para o campo.](https://ajuda.sankhya.com.br/hc/article_attachments/4416788186903) Opções será aberto um pop-up onde serão cadastradas as possibilidades para o campo.

![Imagem 13: Desta maneira, através do botão Opções será aberto um pop-up onde serão cadastradas as possibilidades para o campo.](https://ajuda.sankhya.com.br/hc/article_attachments/4416783251863)

Acione o botão ![Imagem 14: Acione o botão "Atributos" , assim será exibido o pop-up "Atributos de campo adicional" no qual é efetuado a marcação…](https://ajuda.sankhya.com.br/hc/article_attachments/4416783291799) **"Atributos"**, assim será exibido o pop-up **"Atributos de campo adicional"** no qual é efetuado a marcação **"Lista de opções"**.

![Imagem 15: Acione o botão "Atributos" , assim será exibido o pop-up "Atributos de campo adicional" no qual é efetuado a marcação…](https://ajuda.sankhya.com.br/hc/article_attachments/4416789028887)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)

## Aba Ligações

Nesta aba são apresentadas as Ligações geradas ao realizar a importação de um campo através do botão [Importar Campo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#botoimportarcampo).

![Imagem 16: Nesta aba são apresentadas as Ligações geradas ao realizar a importação de um campo através do botão Importar Campo .](https://ajuda.sankhya.com.br/hc/article_attachments/4416789174807)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)

## Botão Importar Campo

Através deste botão, é possível realizar a importação de um campo pertencente a outro formulário.

![Imagem 17: Através deste botão, é possível realizar a importação de um campo pertencente a outro formulário.](https://ajuda.sankhya.com.br/hc/article_attachments/4416789233303)

Ao acioná-lo, será solicitado que você indique a origem do campo, ou seja, qual formulário fornecerá o campo.

![Imagem 18: Ao acioná-lo, será solicitado que você indique a origem do campo, ou seja, qual formulário fornecerá o campo.](https://ajuda.sankhya.com.br/hc/article_attachments/4416797182103)

Após selecionar e realizar a importação de um campo através do botão Importar Campo, o sistema irá gerar automaticamente na aba [Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#abaligaes) uma ligação para o mesmo, considerando o seu formulário de origem. Isso significa, que no momento da visualização do campo no novo formulário, ele será apresentado de modo a permitir pesquisa no formulário de origem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)

## Botão Atributos

Na aba [Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#abacampos), temos o botão Atributos, que ao ser acionado, abre o pop-up **"Atributos de campo adicional"** para configuração de detalhes mais refinados relacionados aos campos.

![Imagem 19: Na aba Campos , temos o botão Atributos , que ao ser acionado, abre o pop-up "Atributos de campo adicional" para…](https://ajuda.sankhya.com.br/hc/article_attachments/4416797373079)

Inicialmente, defina se o campo será ou não **"Requerido"**; determine também se o campo será **"Visível"** ou não; a marcação **"Somente Leitura"**, indica que o campo será apenas de leitura (quando marcado), ou edição (se desmarcado).

A marcação **"Permite valor nulo"** quando assinalada, determina se o campo adicional que está sendo criado ou editado, aceitará em sua utilização, valores nulos (conceitualmente, um valor nulo ou NULL é diferente de zero (0), espaços em branco ou uma cadeia de caracteres de comprimento zero como ""; NULL significa que nenhuma entrada foi feita; a presença de valor NULL, normalmente implica que o valor é desconhecido ou indefinido). Quando um campo não permitir valor nulo (opção desmarcada) deve-se obrigatoriamente, marcar o campo como **"Requerido"**, o que deve ocorrer na criação ou alteração do campo.

Através do campo **"Nome do agrupamento"**, você pode criar uma espécie de grupo dentro da aba. Sendo necessário que um conjunto de campos seja apresentado em um mesmo agrupamento, defina o atributo Nome do agrupamento com valor igual para todos os campos.

Ainda com relação à configuração dos Campos Adicionais, quando um destes for composto de número inteiro ou número decimal existirá a possibilidade que o usuário tenha a soma dos mesmos no rodapé da grade. Esta possibilidade somente estará disponível caso o campo seja composto de número inteiro ou decimal. Nos referimos aqui, à marcação **"Mostra soma no rodapé da grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118893-Formul%C3%A1rios-de-Processo#top)
