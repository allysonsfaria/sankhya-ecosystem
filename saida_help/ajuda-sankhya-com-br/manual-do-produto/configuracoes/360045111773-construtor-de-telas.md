---
id: "360045111773"
titulo: "Construtor de Telas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-26T12:36:00Z"
rotulos: ["manual", "Configuração", "Pesquisa", "Arquivos", "Anexos", "Telas", "MODGRADCONSTTEL", "Construtor de Telas", "CONFGRARESPTEL", "Manual", "Painel de Filtros", "Responder", "Telas Personalizadas", "br.com.sankhya.core.cfg.telaspersonalizadas", "Construtor de Telas manual", "Construção de Telas Personalizadas no Sankhya-Om", "Central de Projetos", "Customização", "Desenvolvimento"]
---

# Construtor de Telas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310984296343) Módulo: Configurações > Avançado
```

---

Nesta tela, temos uma ferramenta que permite a elaboração de novas telas do tipo formulário no Sankhya-Om, de modo a facilitar que os gestores coletem as mais variadas informações sobre os processos trabalhados.

| [Aba Campos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#abacampos) |  | [Aba Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#abaligaes) |
| --- | --- | --- |
| [Aba Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#abaaes) |  | [Aba Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#abaeventos) |
| [Criando uma Tela Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#criandoumatelaadicional) |  | [Campos como "Lista de Opções"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#camposcomolistadeopes) |
| [Importando um campo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#importandoumcampo) |  | [Configurando os Atributos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#configurandoosatributosdecamposadicionais) |
| [Tela Detalhe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#teladetalhe) |  | [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#botooutrasopes) |
| [Compreendendo o Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#comprendendoopaineldefiltros) |  | [Recursos da Tela Adicional Criada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#recursosdatelaadicionalcriada) |
| [Configurações da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#configuraesdatela) |  | [Criação de Filtros Personalizados...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#criaodefiltrospersonalizadosatravsdoassistentedefiltro) |
| [Relatórios Rápidos...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#relatriosrpidosatravsdobotoimpressodogrid) |  | [Criar um novo item no Menu do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#criarumnovoitemnomenudosistema) |
| [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#controledeacessos) |  | [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#parmetros) |

![Imagem 2: Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/360075374613)

**Observação:** é possível modificar o modo com que a tela é iniciada, ou seja, a forma que a tela será aberta; através da ativação do parâmetro **"Modo grade padrão no Constr. de Telas? - MODGRADCONSTTEL"** tem-se a apresentação inicial da tela em modo grade; com o referido parâmetro desligado, a tela em modo fomulário será aberta.

Pelo configurador você terá a liberdade de definir quantos campos julgue necessário com seus respectivos tipos, além de ser possível criar telas com nível de complexidade mais alta, como telas do tipo Mestre-detalhe.

As telas criadas por este recurso serão acessadas pelo menu padrão do sistema e irão se assemelhar no visual e comportamento às telas padrão do sistema, ou seja, elas possuem modo grade/formulário, botões de edição dos registros, impressão da grade, assistente para montagem de filtros, configuração de layout, controle de acesso por usuário etc.

O sistema cria a tabela no banco de dados para manter os dados inseridos nesta tela, desta forma, podem-se usar as informações onde se desejar, como por exemplo, em relatórios, cubos de decisão, dashboards, regras de validação etc.

**Nota:** para facilitar a identificação de telas adicionais no sistema, no menu à direita da tela (local onde se realiza o logout do sistema), na opção **"Configurar Tela"** é exibido o texto **"Tela adicional"**.

![Imagem 3: Nota: para facilitar a identificação de telas adicionais no sistema, no menu à direita da tela (local onde se realiza o…](https://ajuda.sankhya.com.br/hc/article_attachments/360075374693)

Além das possibilidades de navegação entre os registros, de inclusão, exclusão, confirmação, cancelamento e duplicação de informações, é possível também anexar arquivos relacionados a tela, ou a rotina que está sendo desenvolvida. Para maiores detalhes, acesse o tópico [Anexar Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603294-Anexar-Arquivos).

**Nota:** quando você comprar uma solução pelo Place e esta for protegida, você não poderá **"Duplicar"** o registro. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Criando uma tela adicional

Uma tela personalizada poderá ser inserida no conceito do Sankhya Place. Para isso, é necessário habilitar a marcação **"Permitir instalar Sankhya Place?"** da tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana), e, em seguida, ao clicar no botão para a inclusão de uma tela, será apresentado o pop-up **"Buscar soluções no Sankhya Store"** com as soluções disponíveis no Sankhya Place. 

Desse modo, defina o pacote que deseja efetuar o download e verifique se a solução é gratuita ou paga. A saber:

**Soluções gratuitas**

Caso você queira instalar uma solução gratuita, basta clicar em **"Instalar"** e aceitar os termos de uso da loja de soluções. 

[GIF animado: Imagem 4: Caso você queira instalar uma solução gratuita, basta clicar em "Instalar" e aceitar os termos de uso da loja de…](https://ajuda.sankhya.com.br/hc/article_attachments/8100424257303)

| ```  Imagem 5: Obtenha mais informações sobre o termo de uso, por meio do link Termos e Condições da Loja de Soluções . Obtenha mais informações sobre o termo de uso, por meio do link  Termos e Condições da Loja de Soluções. ``` |
| --- |

**Soluções pagas**

Antes de iniciarmos a instalação do pacote pago, é importante ressaltarmos que o usuário responsável pela aquisição do respectivo pacote deverá realizar o login com o Sankhya ID. Através desse usuário o sistema identificará quem é o parceiro/CNPJ responsável por essa aquisição.

Desse modo, é de extrema importância atentar-se aos usuários que terão permissão para executar o download de pacotes no Place. Para tal, acesse a tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), aba [Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abasegurana) e verifique a configuração da marcação**"Permite instalar pacote Sankhya Place?"**.

Agora, para realizar o download da solução, clique em **"Instalar"**, assim, será apresentado um pop-up com as informações do pedido. Para concluir a compra é necessário aceitar as seguintes condições:

**“Estou ciente que ao confirmar, o pacote será imediatamente instalado no sistema e será gerado uma fatura no valor de R$ XX,XX para minha empresa.”**

**“Estou ciente e de acordo com os termos de uso da loja de soluções.”**

[GIF animado: Imagem 6: “Estou ciente e de acordo com os termos de uso da loja de soluções.”](https://ajuda.sankhya.com.br/hc/article_attachments/8100571427607)

Clicando em **"Sim, confirmar"**, a aquisição/download é realizada e será disparado um BI para o mesmo e-mail cadastrado para recebimento de boletos de cobrança mensal de uso do sistema Sankhya. Nesse e-mail serão enviados o boleto e NFS-e referentes ao valor do pacote adquirido. O boleto, em sua maioria, é gerado com o vencimento até 7 dias após a data do download do pacote.

Caso você queira realizar a inserção de um novo registro fora deste contexto, clique no botão **"Cadastrar Tela Adicional"** do pop-up, assim, a janela **"Nova Tela"** será apresentada onde deve-se selecionar o tipo da tela.

[GIF animado: Imagem 7: Caso você queira realizar a inserção de um novo registro fora deste contexto, clique no botão "Cadastrar Tela…](https://ajuda.sankhya.com.br/hc/article_attachments/8100607366551)

Para entender os tipos de tela disponíveis devemos primeiramente entender o que é uma tela mestre e o que é uma tela detalhe.

A **"Tela Mestre"** é aquela que não possui dependência de nenhuma outra tela, e pode ser acessada diretamente pelo menu.

Enquanto uma **"Tela Detalhe"** é aquela que depende de outra para existir, como por exemplo, em um cadastro de clientes, a sub-tela de Contatos pode ser considerada uma tela detalhe e só pode ser acessada de dentro da tela de Clientes (o sistema monta uma aba para este caso).

As telas detalhe são criadas de forma independente, e a ligação entre a tela mestre e seus detalhes é realizada através do dicionário de dados de forma automática pelo sistema.

Para se ter uma tela detalhe, é necessário compreender que a cardinalidade entre a mestre e a detalhe é sempre de um para muitos (1 x N), no exemplo citado, um Cliente pode possuir vários Contatos, vários Produtos preferidos e vários Perfis.

Por padrão, as telas detalhe são montadas dentro da tela mestre como sendo uma aba, dentro desta aba tem-se uma grade onde poderemos realizar a inclusão de dados. Uma tela detalhe é semanticamente idêntica a uma tela mestre, a única diferença é que ela é dependente da mestra. Outra característica importante é que a tela detalhe sempre herda parte da chave-primária da tela mestre, isso significa que telas detalhe sempre possuem chave primária composta, onde a primeira parte é a chave mestre e a segunda parte é o campo da própria detalhe.

Uma tela detalhe pode ser mestre de outra (pode ter seus próprios detalhes), isso significa que no exemplo citado a sub-tela de Contatos pode possuir uma tela Telefones que mantém os dados de todos os telefones do contato.

Uma tela que não possui detalhes também é considerada mestre, pelo fato de que ela será disponibilizada para acesso direto pelo menu.

Relacionamentos um para um (1 x 1) não são mapeáveis por telas detalhe, e serão discutidos mais tarde neste documento quando falarmos sobre importação de campos.

Um **"Cadastro em estrutura hierárquica"** é uma tela onde seus registros possuem ligação hierárquica entre si; podendo-se citar como exemplo, telas do próprio sistema com essa característica:

- Naturezas;
- Centros de Resultados;
- Grupos de Produtos.

Uma característica comum entre estas telas é que o formato do código chave é definido por uma máscara hierárquica de níveis, por exemplo, 99.99.999. Neste caso a máscara impõe a estrutura do código considerando 3 grupos, onde o primeiro e segundo grupos terão 2 dígitos, e o terceiro terá 3 dígitos, portanto o código 1.01.00 é pai (na hierarquia) do código 1.01.55.

![Imagem 8: Uma característica comum entre estas telas é que o formato do código chave é definido por uma máscara hierárquica de…](https://ajuda.sankhya.com.br/hc/article_attachments/360075374813)

**Máscara:** Definiremos aqui a quantidade de dígitos que o código irá possuir, assim como a organização da estrutura, por exemplo:

- #.##.###

Esse código possuirá sempre 6 dígitos, sendo que no primeiro nível tem-se 1 dígito, 2 dígitos no segundo nível e 3 no terceiro nível. Com esta estrutura, tem-se os seguintes exemplos de códigos:

- 1.01.123
- 2.09.001

**Nome do parâmetro:** Por padrão no Sankhya-Om, todas as telas que utilizam estrutura de hierarquia guardam o valor da máscara em um parâmetro na tabela TSIPAR, como por exemplo MASC\_GRUPOPROD. No caso das telas adicionais o sistema gera esse nome como sendo MASC\_<nome.da.tabela.adicional>; porém, você poderá alterá-lo como quiser.

**Nome do Campo de Apresentação:** Nome do campo que será criado para receber a descrição de cada linha de registro, por exemplo, no cadastro de Centro de Resultados esse campo é o DESCRCENCUS; no caso da tela adicional, deve-se dar um nome sugestivo para o campo que terá essa característica.

**Descrição do Campo de Apresentação:** Idêntico ao anterior, porém aqui você irá colocar sua descrição. No exemplo mencionado do Centro de Resultados, o campo recebe o texto de **"Descrição Centro de resultado"**.

Vejamos um exemplo:

Suponhamos que um cliente queira controlar os orçamentos emitidos; para isso deseja-se criar uma Tela Mestre de Lançamento de Orçamentos.

Logo depois, clique no sinal de inserção de uma nova tela, e selecione a opção **"Tela Mestre"** e clique em **"Próximo"**, onde a tela para inclusão das informações sobre a nova tela será apresentada.

![Imagem 9: Logo depois, clique no sinal de inserção de uma nova tela, e selecione a opção "Tela Mestre" e clique em "Próximo" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360074214514)

**Descrição da Tela:** Neste campo informa-se a descrição da tela. Essa informação será utilizada em todas as situações onde uma descrição abreviada da tela for necessária, como em telas pesquisas por exemplo.

**Nome da tabela no banco de dados:** Informa-se aqui, o nome da tabela do banco de dados que mantém as informações da tela. Este nome será pré-fixado no banco de dados como AD\_Nome da Tabela, ou seja, se o valor digitado for CLIENTES, o nome da tabela será AD\_CLIENTES.

Preenchidas as duas informações, e ao clicar em **"Próximo"** a tela seguinte será exibida para cadastro da chave primária. De maneira sucinta, chave primária é o campo (ou conjunto de campos) da tabela que identificam um registro de maneira única, ou seja, nenhuma outra linha da tabela terá valores repetidos para este campo.

Um exemplo deste fato, é o cadastro de Parceiros que possui como chave primária o campo Código do Parceiro, pois não existirão outros iguais.

No caso de Cadastro de Orçamentos, a chave primária da tabela seria o número único do orçamento.

![Imagem 10: No caso de Cadastro de Orçamentos, a chave primária da tabela seria o número único do orçamento.](https://ajuda.sankhya.com.br/hc/article_attachments/360075374893)

Para inclusão de campos na chave primária, acione o botão incluir ![Imagem 11: Para inclusão de campos na chave primária, acione o botão incluir , e preencha os dados:](https://ajuda.sankhya.com.br/hc/article_attachments/16844709303959), e preencha os dados:

**Nome do campo:** Aqui será definido um nome para o campo, sendo que este nome, não deve possuir espaços em branco nem caracteres especiais; tem-se aqui um limite de 32 caracteres.

**Descrição do campo:** Neste campo informe a que se refere o campo criado. Este texto será empregado em todos os locais onde o campo é apresentado, ou seja, formulários, grades, consultas, relatórios rápidos etc.

**Tipo de dados:** Insira aqui, o tipo do campo; no nosso exemplo, é o tipo Número Inteiro. Vejamos mais detalhes sobre os tipos campos, na seção **"Aba Campos"**.

**Apresentação:** Aqui será selecionada a forma de apresentação do campo. Obteremos mais detalhes, também a apresentação dos campos na seção **"Aba Campos"**.

**Permite pesquisa?:** Esta marcação quando efetuada, permite que o campo seja utilizado como critério de pesquisa na tela padrão de pesquisas.

**Visível no grid de pesquisa?:** Esta opção quando marcada, o campo estará visível na grade de resultados da pesquisa.

Pode-se incluir quantos campos forem julgados necessários na chave-primária; quando finalizar, clique em **"Próximo"**.

![Imagem 12: Pode-se incluir quantos campos forem julgados necessários na chave-primária; quando finalizar, clique em "Próximo" .](https://ajuda.sankhya.com.br/hc/article_attachments/360075374913)

Neste passo, você poderá definir qual campo da chave-primária será auto-numerado, ou seja, o sistema irá gerar automaticamente um código numérico sequencial crescente, quando forem incluídos novos registros na tela.

Este recurso é bastante útil em telas onde a chave-primária é um campo numérico sequencial e deseja-se deixar o sistema controlar a numeração. Por exemplo, em um cadastro de Clientes, o código do cliente pode ser uma campo numérico auto-numerado. Isso vale também para telas detalhe, como por exemplo, a sub-tela de Contatos de um cadastro de Clientes; pode sequenciar o código do contato.

Feita a definição de relacionada a numeração, clica-se em **"Concluir"** para determinar o fim do procedimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Aba Campos

Nesta aba serão configurados os campos que serão apresentados/utilizados na tela que está sendo criada.

![Imagem 13: Nesta aba serão configurados os campos que serão apresentados/utilizados na tela que está sendo criada.](https://ajuda.sankhya.com.br/hc/article_attachments/360075374933)

Depois de criada pelo sistema a nova tabela no banco de dados com a chave primária, pode-se adicionar os outros campos que irão manter as informações importantes da tela. Para tal, será necessário incluir as seguintes informações:

**Nome do Campo:** Preencha aqui o nome interno do campo, ou seja, a nomenclatura que ele irá possuir na tabela do banco de dados.

**Descrição do campo:** Este espaço é destinado a descrição do campo que irá aparecer em todas as situações onde este for apresentado, como na própria tela (formulário), grades, telas de pesquisa, relatórios rápidos etc.

**Tipo de Dados:** Defina aqui o tipo do campo no banco de dados; neste caso, teremos as seguintes opções:

- **Conteúdo Binário:**Esse tipo de dados é utilizado para campos do tipo Imagem, Arquivo e Múltiplos Arquivos. Sendo que, quando o campo **"Apresentação"** estiver configurado com a opção **"Múltiplos Arquivos"**, será possível anexar ao campo, links que poderão ser copiados, ou então, o redirecionamento direto para a página pertencente ao link.
- **Data:** Representa as informações apenas de data.
- **Data e Hora:** Tem-se aqui a representação de data e hora. Ambos são criados no Banco de Dados como sendo tipo DATE Oracle e DATETIME SQLServer. A única diferença é na forma de apresentação, pois no caso de Data e Hora o campo permite a digitação da hora.
- **Hora:** Representa-se valores de hora. O campo será criado no banco de dados como sendo do tipo NUMBER(5) para Oracle e SMALLINT para SQLServer. O sistema irá apresentá-lo com a máscara 999:99
- **Número Decimal:** Serve para representar valores numéricos com decimais ou valores de moeda. O campo será criado no banco de dados como sendo do tipo FLOAT.
- **Número Inteiro:** Este tipo representa números sem a parte decimal (inteiros), ideal para códigos. Será criado no Banco de Dados como sendo do tipo NUMBER (10) Oracle e INT SQLServer.
- **Texto Longo (CLOB):** Ao definir pela utilização deste tipo de dado, será possível inserir uma grande quantidade de informações no campo. Além disso, será possível alterar algumas características da fonte do texto informado no campo, deixando este em Negrito, Itálico ou Sublinhado e ainda, inserir-se Marcadores.
- **Texto:** Este tipo é curinga, e dependendo do Tipo de Apresentação será exibido de maneiras diferentes pelo sistema, como segue:

1. Lista de opções: Será apresentado como sendo uma caixa de seleção (ComboBox). Os itens da caixa de seleção são informados no botão Opções que se localiza ao lado do campo Apresentação. Nela será definido a lista de valores usando pares Valor/Descrição. O valor é o que será gravado no Banco de Dados e a descrição é o que será apresentado ao usuário final, por exemplo: Valor = S, Descrição = Sim. Será criado no banco de dados como sendo do tipo VARCHAR(10), isso significa que os valores devem ter no máximo esse comprimento.
2. Padrão: Será apresentado como uma caixa de texto de apenas uma linha; o campo será criado no Banco de Dados como sendo do tipo VARCHAR(100).
3. Caixa de texto: Será apresentado como uma caixa de texto que comporta várias linhas de texto (também conhecido como campo memo). O campo será criado no Banco de Dados como sendo VARCHAR2(4000) Oracle ou TEXT no SQLServer.
4. Formatação HTML: Tem sua apresentação como uma caixa de texto que comporta várias linhas de texto. Ao utilizar está opção combinada com o campo **"Tipo de dados"** configurado com a opção **"Texto Longo (CLOB)"**, tem-se a possibilidade de realizar o upload de imagens para telas no formato HTML5. Pode-se adicionar quantas imagens forem necessárias, sendo que cada uma delas poderá conter somente 500kb.

**Apresentação:** Possibilita que o usuário configure o formato que o campo será apresentado para utilização. São disponibilizadas as seguintes opções:

- Formatação HTML;
- Imagem;
- Múltiplos Arquivos;
- Checkbox;
- Padrão;
- Caixa de Texto;
- Anexo;
- Lista de Opções (Combobox);
- Múltiplos arquivos.

**Nota:** a opção Anexo só poderá ser utilizada quando o campo Tipo de dados estiver configurado com a opção **"Conteúdo Binário"**.

**Permite pesquisa?:** Determina se o campo poderá ser utilizado como critério de pesquisa no componente. 

**Visível no grid de pesquisa:** Quando marcado, define que o campo irá aparecer na grade de resultados do componente de pesquisa.

**Campo calculado:** Determina que esse campo é calculado, e portanto não irá existir no banco de dados. Seu valor será resolvido através do campo de expressão.

**Expressão:** Este campo possui objetivos diferentes dependendo do tipo de campo. Se o campo for calculado, a expressão será utilizada para calcular seu valor final. Se o campo não for calculado, sendo a expressão informada ela será utilizada como expressão de UPDATE, ou seja, quando o registro for atualizado, essa expressão será avaliada para resolver o novo valor do campo, e esse valor será gravado no banco de dados.

A expressão é sempre escrita em Java, e todos os campos da tabela estão disponíveis para uso com o padrão $col\_NOMEDOCAMPO, ou seja, se na tela adicional houver um campo chamado CODPARC então este será referenciado no script como $col\_CODPARC (existe diferenciação entre letras maiúsculas e minúsculas).

Os tipos das variáveis referentes aos campos são equivalentes ao tipo da coluna no banco de dados, como segue:

- **Numéricas:** java.math.BigDecimal

Esta informação vale para qualquer coluna numérica, independente de ser inteiro ou ponto flutuante, não importando sua precisão.

- **Texto:** java.lang.String

Vale para qualquer tipo de coluna texto, independente da largura ou tipo primitivo do banco de dados.

**Nota:** caso a coluna seja do tipo CLOB ou TEXT, o tipo da coluna no script será char[] (array de caracteres).

**Importante:** ao criar uma tela adicional e adicionar um campo do tipo **"Texto"** com apresentação tipo **"Caixa de texto"**, o nome do campo (Texto de descrição) será um link, que ao ser acionado, abrirá uma tela de edição e/ou visualização do campo, respeitando os critérios do campo ser ou não somente leitura.

![Imagem 14: Importante: a o criar uma tela adicional e adicionar um campo do tipo "Texto" com apresentação tipo "Caixa de texto" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360075374973)

![Imagem 15: Importante: a o criar uma tela adicional e adicionar um campo do tipo "Texto" com apresentação tipo "Caixa de texto" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360074214714)

Nas telas principais, como por exemplo "Movimentação Financeira", os campos que forem do tipo "Texto", com modo de apresentação igual a "Caixa de texto", também apresentarão o link de acesso à tela de edição.

![Imagem 16: Nas telas principais , como por exemplo "Movimentação Financeira", os campos que forem do tipo "Texto", com modo de…](https://ajuda.sankhya.com.br/hc/article_attachments/360075375053)

Depois de editado, clique em **"OK"** a janela será fechada e o conteúdo digitado nela passará para o campo. Ao selecionar **"Cancelar"** a janela será fechada e o conteúdo nela digitado descartado. Este comportamento se repete nos **"Campos Adicionais"**.

Data: java.sql.Timestamp

Este tipo é independente do banco de dados, ou seja, podem ser SQL Server, Oracle ou qualquer outro.

Além das variáveis com os valores das colunas, tem-se outras variáveis interessantes:

$sql - É uma referencia a um objeto do tipo EasySQL. Esse tipo de objeto possui métodos que permitem a execução de consultas SQL de forma simples, no próprio banco de dados configurado da aplicação; vejamos um exemplo de uso:

$sql.setParam(“PARCEIRO”, $col\_CODPARC ); //a tabela local possui um campo chamado CODPARC

$sql.select(“P.NOMEPARC,C.NOMECID”,”TGFPAR P INNER JOIN TSICID C ON(C.CODCID = P.CODCID)”, “P.CODPARC = {PARCEIRO}”);

nomeParc = “”;

nomeCidade = “”;

if( $sql.next() ){ // verdadeiro se houver pelo menos uma linha de resultado nomeParc = $sql.getString(1);nomeCidade = $sql.getString(2);}

return nomeParc + “ ” + nomeCidade;

O exemplo acima faz uma consulta na tabela de parceiros e obtém o nome do parceiro e o nome da cidade; com isso, é montado um texto de retorno concatenando os dois campos.

**$usuario\_logado** - Código do usuário logado (o tipo é java.math.BigDecimal)

**$dh\_atual** - Data e hora atual (o tipo é java.sql.Timestamp)

**$d\_atual** - Data atual do sistema. Esse valor não contém horas (o tipo é java.sql.Timestamp)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Campos como "Lista de Opções"

Ao utilizar com campos do tipo **"Texto"**, podemos configurá-lo para que na sua utilização, tenha-se um campo com o formato **"Lista de Opções"** (Combobox). Para isso, defina o campo **"Apresentação"** como **"Lista de Opções"**:

![Imagem 17: Ao utilizar com campos do tipo "Texto" , podemos configurá-lo para que na sua utilização, tenha-se um campo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/360074214734)

A partir disso, no botão **"Opções"**, cadastra-se as possibilidades para o campo.

![Imagem 18: A partir disso, no botão "Opções" , cadastra-se as possibilidades para o campo.](https://ajuda.sankhya.com.br/hc/article_attachments/360074214794)

Por fim, no botão **"Atributos"**, na tela que é aberta, efetua-se a marcação **"Lista de opções"**.

![Imagem 19: Por fim, no botão "Atributos" , na tela que é aberta, efetua-se a marcação "Lista de opções" .](https://ajuda.sankhya.com.br/hc/article_attachments/360074214814)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Importando um campo

![Imagem 20: Importando um campo](https://ajuda.sankhya.com.br/hc/article_attachments/360075375193)

Através do botão **"Importar Campo"** é possível realizar a importação de um campo de outra tabela, para a tela adicional; podendo esta outra tabela ser adicional ou oficial do sistema.

Este procedimento é equivalente a criação de uma chave estrangeira para a outra tabela. Esta opção deve ser utilizada sempre que se deseja criar um campo que faça referência a outra tabela. Como exemplo de uma tabela que faz referência a outra, podemos citar uma tabela de Clientes que faz referência a tabela de Cidades, ou seja, na tabela de Clientes possui-se um campo com o código da cidade de domicílio do cliente; assim quando o sistema monta a tela, o formulário irá possui um campo com o código na esquerda e o nome da cidade à direita, além de um botão para pesquisar cidades.

Tomemos como exemplo, a importação para a tabela do campo Parceiro:

![Imagem 21: Tomemos como exemplo, a importação para a tabela do campo Parceiro:](https://ajuda.sankhya.com.br/hc/article_attachments/360075375233)

Selecionando-se através de um duplo clique o campo desejado, e clicando-se em **"Próximo"** serão apresentadas as **"Informações do Campo"**; ao importar-se um campo de uma tabela estrangeira, o sistema só poderá importar a chave primária desta tabela, logo a janela Informações do campo se apresentará preenchida:

![Imagem 22: Selecionando-se através de um duplo clique o campo desejado, e clicando-se em "Próximo" serão apresentadas as…](https://ajuda.sankhya.com.br/hc/article_attachments/360074227694)

As informações das colunas **"Campo Local"** e **"Descrição Local"** poderão ser modificadas, proporcionando a opção de criar-se mais de um relacionamento para a mesma tabela (mais de uma FK para a mesma tabela destino).

Por exemplo: Pode-se querer relacionar o orçamento ao parceiro do orçamento, ou com o parceiro atendido etc. Para isso, inclui-se mais de um campo "Cód. Parceiro" e atribui-se a cada um deles, um nome diferente.

**Observação:** nos casos em que forem criados campos adicionais para armazenamento do código do vendedor, é necessário que na tela **"Configurações > Controle de Acesso > Usuários > aba Identificação > campo Cód. Parceiro"**, informa-se o parceiro que será vinculado ao usuário; além disso, na tela **"Configurações > Cadastros > Vendedores/Compradores > campo Parceiro"**, informa-se o mesmo parceiro cadastrado na primeira tela mencionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Configurando os Atributos de Campos Adicionais

Na aba Campos, pode-se observar o botão **"Atributos"**, que ao ser acionado, abre a pequena tela **"Atributos de campo adicional"** para configuração de detalhes mais refinados relacionados aos campos.

![Imagem 23: Na aba Campos, pode-se observar o botão "Atributos" , que ao ser acionado, abre a pequena tela "Atributos de campo…](https://ajuda.sankhya.com.br/hc/article_attachments/360075384453)

Nesta tela, inicialmente é feita a definição se o campo será ou não **"Requerido"**; determina-se também se o campo será **"Visível"** ou não; pela marcação **"Somente Leitura"**, tem-se a representação que o campo será apenas de leitura (quando marcado), ou edição (se desmarcado).

A marcação **"Permite valor nulo"** quando assinalada, tem-se que o campo adicional que está sendo criado ou editado, aceitará em sua utilização, valores nulos (conceitualmente, um valor nulo ou NULL é diferente de zero (0), espaços em branco ou uma cadeia de caracteres de comprimento zero como ""; NULL significa que nenhuma entrada foi feita; a presença de valor NULL, normalmente implica que o valor é desconhecido ou indefinido). Por padrão, esta marcação é apresentada realizada. Quando um campo não permitir valor nulo (opção desmarcada) deve-se obrigatoriamente, marcar o campo como "Requerido", o que deve ocorrer na criação ou alteração do campo.

Se o campo deverá constar em uma aba específica, deve-se preencher o campo **"Nome da aba"**. Através do campo **"Nome do agrupamento"**, pode-se criar uma espécie de grupo dentro da Aba.

Sendo necessário que um conjunto de campos seja apresentado na mesma aba e/ou em mesmo um agrupamento, define-se os atributos **"Nome da aba"** e **"Nome do agrupamento"** com valor igual para todos os campos que deverão ser apresentados na aba e/ou agrupamento em questão.

**Nota:** referente ao recurso de Agrupamento de campos em uma aba, este encontra-se disponível apenas nas telas desenvolvidas linguagem [HTML5](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110733-HTML5).

Ainda com relação à configuração dos Campos Adicionais, quando um destes for composto de número inteiro ou número decimal existirá a possibilidade que o usuário tenha a soma dos mesmos no rodapé da coluna. Esta possibilidade somente estará disponível caso o campo seja composto de número inteiro ou decimal. Nos referimos aqui, à marcação **"Mostra soma no rodapé da grade"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Aba Ligações

![Imagem 24: Aba Ligações](https://ajuda.sankhya.com.br/hc/article_attachments/360075384473)

Após a importação de um campo (no exemplo, o campo "Parceiro") o sistema o relaciona à chave primária automaticamente na aba **"Ligações"**, isso significa que no momento da visualização da nova tela, este campo será apresentado para pesquisa de parceiros.

#### Botão Avançado

Ao acioná-lo será aberta a tela **"Atributos da ligação"**:

![Imagem 25: Ao acioná-lo será aberta a tela "Atributos da ligação" :](https://ajuda.sankhya.com.br/hc/article_attachments/360075384573)

**Campo para apresentação:** Define-se aqui, qual campo será utilizado no lado direito da pesquisa; por exemplo, imaginemos que não deseja-se apresentar o nome do parceiro no campo lateral da pesquisa nas pesquisas de parceiro, mas sim outro campo qualquer; utiliza-se então esta opção. É uma configuração bem específica, e na maioria das vezes o valor padrão é o mais indicado.

O campo selecionado para Apresentação, deverá possuir a marcação **"Permite pesquisa?"** selecionada para que sejam apresentados os nomes vinculados aos códigos.

Esta marcação poderá ser feita pela tela Dicionário de Dados, aba **"Campos"** ou, se for vinculado à uma tela mestre, será verificada a mesma marcação na tela Construtor de Telas, aba Campos.

**Expressão da ligação:** Este campo serve para filtrar a pesquisa, ou seja, sempre que a pesquisa for aberta (pois toda ligação é apresentada na tela como um componente de pesquisa), este filtro será aplicado. Imaginemos que seja criada uma ligação com Parceiro e que na pesquisa devam ser exibidos apenas os parceiros clientes, para isso, a expressão do filtro seria: this.CLIENTE = 'S'.

**Filtro de formulário:** Neste espaço é possível utilizar os valores digitados na própria tela como filtro de ligação. Exemplo: this.NOMEPARC lilke 'form.PRIMEIRONOME%' - Desta forma, suponhamos que 'PRIMEIRONOME' seja um campo da tela, seu valor será utilizado para filtrar a pesquisa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Aba Ações

![Imagem 26: Aba Ações](https://ajuda.sankhya.com.br/hc/article_attachments/360074227834)

A configuração desta aba, permite que no Sankhya-Om sejam executadas tarefas específicas de forma rápida e simples. Através desta aba pelo campo **"Tipo"**, será possível definir a execução de uma **"Rotina no Banco de Dados"**, a execução de uma **"Rotina Java"**, a execução de um **"Script (JavaScript)"** e a configuração de um **"Lançador"** para uma tela do sistema. Cada uma destas opções quando escolhida, disponibiliza configurações diferentes a serem efetuadas.

Vejamos separadamente o comportamento de cada uma destas opções, acessando o tópico [Construtor de Telas/Dicionário de Dados - Aba Ações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110493-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es).

A marcação **"Controla Acesso"** que é apresentada na escolha de um dos quatro tipos de ações, quando realizada, tem-se que somente usuários com permissão, poderão ter acesso aos botões de ação. Quando desmarcado, todos os usuários possuirão acesso aos botões de ação.

Uma vez definindo-se pelo Controle de Acesso, na tela **"Configurações > Controle de Acesso > Acessos"** localiza-se a tela adicional criada, e libera-se os acessos desejados. Ainda nesta tela, no lado direito tem-se o botão "Outros Acessos", que ao ser acionado, irá apresentar as ações que tiveram o campo "Controla Acesso" marcado.

No exemplo da tela adicional "Tarefas Exclusivas", marcaremos as tarefas **"Tarefa no Pedido de Venda"** e **"Tarefa no Pedido de Compra"** para terem seu acesso controlado.

![Imagem 27: No exemplo da tela adicional "Tarefas Exclusivas", marcaremos as tarefas "Tarefa no Pedido de Venda" e "Tarefa no…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228094)

Na tela de controle de acessos, acionando-se o botão **"Outros Acessos"** pode-se observar que são apresentadas as duas ações marcadas para terem seu acesso controlado.

![Imagem 28: Na tela de controle de acessos, acionando-se o botão "Outros Acessos" pode-se observar que são apresentadas as duas…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228174)

Caso nenhuma ação do Construtor de telas tenha ação controlada, e acessar-se o botão "Outros Acessos", da tela de controle de acessos do usuário, será apresentado um alerta com a seguinte mensagem:

**"Nenhuma ação do Construtor de Telas está marcada para controlar acesso para o item de menu selecionado".**

Além das permissões poderem ser fornecidas para determinados usuários, estas também poderão ser configuradas para um determinado grupo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Aba Eventos

Esta aba permite realizar as configurações de eventos considerando as entidades (telas nativas ou adicionais) do sistema.

![Imagem 29: Esta aba permite realizar as configurações de eventos considerando as entidades (telas nativas ou adicionais) do…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228234)

Os referidos eventos são mecanismos que podem executar ações utilizando a Rotina de Banco de dados (Stored Procedure) ou a Rotina (Java) de acordo com a regra de negócio utilizada e considerando os lançamentos nas respectivas entidades.

Diante disto, pode-se visualizar os seguintes exemplos:

![Imagem 30: Diante disto, pode-se visualizar os seguintes exemplos:](https://ajuda.sankhya.com.br/hc/article_attachments/360074228254)

**Observação:** para mais detalhes deve-se verificar as informações disponibilizadas no tópico [Construtor de Telas/Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025236714-Construtor-de-Telas-Dicion%C3%A1rio-de-Dados-Aba-A%C3%A7%C3%B5es) que dispõe de dados relacionados especificamente a aba **"Ações"**; sua utilização se assemelha a aba Eventos.

O botão **"Salvar ordem"** permite definir a ordem que os eventos ativos serão executados; após este procedimento, pode-se visualizar na coluna **"Ordem"** a ordenação configurada anteriormente.

![Imagem 31: O botão "Salvar ordem" permite definir a ordem que os eventos ativos serão executados; após este procedimento, pode-se…](https://ajuda.sankhya.com.br/hc/article_attachments/360075384953)

É relevante mencionar que o sistema não sobrescreve os eventos adicionados na instância, uma vez que sua execução se dará após as validações nativas do Enterprise Resource Planning (ERP).

Veja também as informações contidas nas telas [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor) e [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Tela Detalhe

Finalizado o cadastro da tela mestre, cadastra-se a tela detalhe, ou seja, a instância de ligação. Clique no botão de inclusão  para efetuar-se o cadastro de uma tela do tipo detalhe; o sistema exigirá a ligação com uma tela mestre.

![Imagem 32: Finalizado o cadastro da tela mestre, cadastra-se a tela detalhe, ou seja, a instância de ligação. Clique no botão de…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385013)

No relacionamento de tela mestre com uma tela detalhe, a chave primária da tela mestre migra automaticamente para a tela detalhe. Como estas ligações devem ser do tipo um para muitos casos, então deve-se adicionar mais um campo a chave primária da tela detalhe, geralmente faz-se isso com um campo numérico do tipo inteiro.

![Imagem 33: No relacionamento de tela mestre com uma tela detalhe, a chave primária da tela mestre migra automaticamente para a…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228314)

Na situação relatada nas imagens, o próximo passo é selecionar-se o campo Sequência para a auto-numeração.

![Imagem 34: Na situação relatada nas imagens, o próximo passo é selecionar-se o campo Sequência para a auto-numeração.](https://ajuda.sankhya.com.br/hc/article_attachments/360075385333)

Ao concluir o procedimento, tem-se:

![Imagem 35: Ao concluir o procedimento, tem-se:](https://ajuda.sankhya.com.br/hc/article_attachments/360075385353)

A partir daqui, pode-se realizar a inclusão dos campos necessários à completude da tela.

#### Utilizando campos da tela em filtros de pesquisa

A utilidade deste recurso consiste em permitir o uso de informações da tela, para contextualizar a busca feita pelo **"componente de pesquisa"**, filtrando os registros da "tabela de destino", a partir dessas informações, mesmo antes de salvar-se o registro. Deste modo, nas telas adicionais será possível efetuar filtros entre campos, ou seja, trazer informações de um campo, mediante inserção da informação de outro campo.

Exemplo: Trazer os parceiros cuja cidade informada no campo **"Cidade"** seja Uberlândia. Ao solicitar a tela de pesquisa do campo "Parceiro", serão apresentados todos que se encontram na cidade de Uberlândia.

#### Para efetuar a configuração do exemplo acima, será necessário:

Na Tela Adicional AD\_NFSENAT criada para o exemplo, os campos **"Cód. Cidade"** e **"Cód. Parceiro"** foram campos importados de outras telas. O objetivo do filtro a ser utilizado, é de quando o usuário informar a "Cidade" o sistema traga somente os parceiros, pertencentes a Cidade informada:

![Imagem 36: Na Tela Adicional AD_NFSENAT criada para o exemplo, os campos "Cód. Cidade" e "Cód. Parceiro" foram campos importados…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385413)

Para compor o filtro, foi selecionado na **"Aba Ligações"**, o campo **"Cód. Parceiro"** e através do botão **"Avançado"** foram estabelecidos os seguintes atributos para a ligação:

![Imagem 37: Para compor o filtro, foi selecionado na "Aba Ligações" , o campo "Cód. Parceiro" e através do botão "Avançado" foram…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228874)

**Campo para apresentação:** Essa configuração determina qual campo será utilizado do lado direito da pesquisa. Por exemplo, para apresentar a "Razão social", ao invés do nome do parceiro, bastará localizar este campo como "campo de apresentação". Essa troca só acontecerá na tela onde a alteração é feita, mas existem outras maneiras de realizar esta alteração para qualquer contexto do sistema. É algo bem específico, e na maioria dos casos, aconselha-se que o valor padrão seja mantido.

Por exemplo, na imagem acima o Campo para Apresentação é o **"Nome Parceiro"**; na tela adicional (AD\_NFSENAT), o campo de **"Descrição"** será o **"Nome Parceiro"**.

![Imagem 38: Por exemplo, na imagem acima o Campo para Apresentação é o "Nome Parceiro" ; na tela adicional ( AD_NFSENAT ), o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228914)

**Expressão da ligação:** Esta expressão será utilizada como filtro de ligação entre as duas tabelas. Por exemplo, this.CLIENTE = 'S'. Nesta situação, serão visíveis na tela somente os "Parceiros" do tipo "Cliente". A palavra especial "this", que precede o nome do campo, determina que o campo "CLIENTE" esteja na tabela pesquisada e que deva estar presente, com o objetivo de evitar ambiguidades na consulta. Sempre que houver uma busca partindo da tabela, onde a ligação foi feita para a tabela de parceiros, essa expressão estará presente.

#### Exemplo:

Expressão da ligação: this.CLIENTE='S'

Com este filtro, na tela adicional (AD\_NFSENAT), serão apresentados para escolha, somente os parceiros que são **"Clientes"**.

![Imagem 39: Com este filtro, na tela adicional ( AD_NFSENAT ), serão apresentados para escolha, somente os parceiros que são…](https://ajuda.sankhya.com.br/hc/article_attachments/360074228934)

**Filtro de formulário:** Este é um recurso semelhante à expressão de ligação, porém, aqui é possível utilizar-se campos da tabela principal, para compor os filtros. Diferentemente da expressão da ligação, esse filtro só terá efeito quando a busca partir da tela (deve-se ter em mente que existem outras formas, além do componente de pesquisa e da aba de detalhes, para se pesquisar uma tabela partindo de outra).

A forma de preenchimento neste campo, será um pouco mais elaborada, vejamos:

**this.CODCID = form.** – Novamente o termo "this" indica um campo na tabela pesquisada. Já a palavra "form" determina que o valor utilizado para a expressão deverá ser obtido pelo formulário de entrada da tela, através do campo **"CODCID"**.

Todas as ocorrências de "form." sucedidas do nome de algum campo, serão substituídas pelo valor desse campo, no momento da consulta; se não houver o campo mencionado ou ele não estiver preenchido, não será possível realizar a busca, pois os campos usados no filtro são considerados requeridos.

Para tornar um campo não requerido, ou seja, permitir a pesquisa mesmo que ele não exista no formulário ou não esteja preenchido, acrescente o caractere "@" antes do nome do campo. Assim, teríamos: this.CODCID = form.@CODCID.

#### Exemplo:

Filtro de formulário: form.@CODCID is null OR this.CODCID = form.@CODCID

A expressão form.@CODCID is null foi informada no filtro de formulário para que, caso não informe-se na tela adicional (AD\_NFSENAT) a cidade do parceiro, poderá a tela de pesquisa trazer os parceiros. Se não for informada esta expressão, o sistema não trará nenhuma informação na tela de pesquisa, se a cidade do parceiro não for informada.

Vejamos na imagem a seguir, que como na tela adicional (AD\_NFSENAT) **"não foi informando"** a cidade do parceiro, a **"Tela de Pesquisa do Parceiro"**, trouxe várias cidades:

![Imagem 40: Vejamos na imagem a seguir, que como na tela adicional ( AD_NFSENAT ) "não foi informando" a cidade do parceiro, a…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385573)

Se na tela adicional for informada a cidade do parceiro, a Tela de Pesquisa do Parceiro, irá apresentar apenas esta cidade:

![Imagem 41: Se na tela adicional for informada a cidade do parceiro, a Tela de Pesquisa do Parceiro , irá apresentar apenas esta…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385633)

Os **"Totalizadores"** das colunas das telas adicionais não serão apresentados com casas decimais, quando a coluna do grid for do tipo inteiro. Vejamos na imagem abaixo por exemplo, o campo Cód. Parceiro do tipo **"Número Inteiro"** e o campo **"Valor Final"** do tipo **"Número Decimal"**.

![Imagem 42: Os "Totalizadores" das colunas das telas adicionais não serão apresentados com casas decimais, quando a coluna do grid…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385673)

Na tela adicional, a somatória dos dois campos será apresentada da seguinte forma:

O campo de Número Decimal será apresentado com vírgula "ex: 20,00" e o campo do **"Número Inteiro"** será exibida a somatória sem vírgula, "ex: 20".

#### Importante: a documentação a seguir é destinada para usuários avançados, como implantadores, consultores e monitores. Entretanto, o que será descrito nesta documentação, deve ser considerado somente como exemplo de uma das funcionalidades.

Se você selecionar o botão **"Avançado"** presente na aba Ligações, será aberta a tela **"Atributos da ligação"**. Ao clicar no sinal de inclusão **"+"** à frente da descrição **"Parâmetros"**. Vejamos maiores detalhes:

**Parâmetros:** Esse recurso possui a funcionalidade de alterar alguns comportamentos das ligações. Na maioria das ligações isso não será necessário. Contudo, segue uma breve descrição de alguns desses parâmetros, seus possíveis valores e o efeito obtido:

**Nome:** Determine aqui, a descrição da tabela pesquisada no título do resultado da pesquisa, ou no título da aba, caso o relacionamento seja "um-para-muitos".

**Valor:** Para preenchimento deste campo, um texto para ser usado como título.

Sendo assim, consideraremos o exemplo a seguir:

![Imagem 43: Sendo assim, consideraremos o exemplo a seguir:](https://ajuda.sankhya.com.br/hc/article_attachments/360074229134)

Desta forma, foi criado o parâmetro **"description"** igual a **"PARCEIRO"**, onde na **"Tela Adicional"** será apresentado:

![Imagem 44: Desta forma, foi criado o parâmetro "description" igual a "PARCEIRO" , onde na "Tela Adicional" será apresentado:](https://ajuda.sankhya.com.br/hc/article_attachments/360074229194)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Botão Outras Opções

Através do botão **"Outras Opções"** teremos as seguintes alternativas:

**Processar campos MGE/Mitra:** Por meio desta opção, é feito o processamento dos campos adicionais que foram criados no MGE. Como o Sankhya-Om utiliza um dicionário de dados diferente do MGE, o fato de se criar um campo adicional no MGE, não faz com que ele esteja disponível automaticamente no Sankhya-Om.

**Checar integridade de campos adicionais:** Através desta opção, faz-se a verificação se todos os campos adicionais presentes no dicionário de dados para esta tabela, realmente existem no banco de dados e estão com o tipo correto.

**Reiniciar esta unidade de dados:** Esta alternativa faz com que o sistema descarte as "caches" internas e releia o dicionário de dados desta tela no banco de dados. Pode ser utilizada quando se faz alterações na estrutura da tela (como adicionar um campo ou realizar uma nova ligação, por exemplo) e esta alteração não aparece imediatamente na tela em execução. Feita a reinicialização, é apresentada a seguinte mensagem:

![Imagem 45: Reiniciar esta unidade de dados : Esta alternativa faz com que o sistema descarte as "caches" internas e releia o…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385773)

**Configuração de Pesquisa:** Através dessa opção, você poderá configurar a ordenação e o limite de resultados de uma determinada tabela. Assim, ao ordenar dados em uma tela, será respeitada a configuração feita nos campos **"Ordenação"** e **"Limite de Resultados"**.

**Definir ordem dos campos:** Ao acionar esta opção, pode-se definir a ordem em que os campos irão aparecer na tela por padrão. Esta ordem poderá ser alterada pelo usuário ou configurada através desta opção.

![Imagem 46: Definir ordem dos campos: Ao acionar esta opção, pode-se definir a ordem em que os campos irão aparecer na tela por…](https://ajuda.sankhya.com.br/hc/article_attachments/360075385793)

**Exportar Metadados e Importar Metadados:** Por meio destas opções, são realizadas a Exportação e Importação de telas adicionais, além dos menus/pastas adicionais necessários para abri-los. Essa funcionalidade flexibiliza e potencializa o uso desse recurso, permitindo o compartilhamento de verdadeiros **"Módulos Adicionais"** entre ambientes distintos. Para maiores detalhes, clique em [Exportação e Importação de Telas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597974-Exporta%C3%A7%C3%A3o-e-Importa%C3%A7%C3%A3o-de-Telas-Adicionais).

**Nota:** quando você comprar uma solução pelo Place e esta for protegida, não será possível efetuar a exportação dos metadados.

**Avançado:** Através desta opção, você terá alguns atributos para configuração fina da tela, tais como:

![Imagem 47: Avançado: Através desta opção, você terá alguns atributos para configuração fina da tela, tais como:](https://ajuda.sankhya.com.br/hc/article_attachments/360074229374)

- **Campo para apresentação:** Trata do campo da tabela que o sistema irá utilizar quando apresentar uma pesquisa para esta tela em outras telas. Por exemplo, em telas onde se tem o campo Código do Parceiro, geralmente se apresenta um controle onde o usuário pode pesquisar o parceiro, e sempre tem-se um campo lateral onde se apresenta o nome do parceiro selecionado, de forma similar a quando se tem um campo **"Cód. Cidades"** em formulários; geralmente tem-se uma pesquisa para a cidade, e o nome desta será exibido no campo lateral.
- **Critério da entidade:** É um filtro que será aplicado internamente em todas as consultas e pesquisas desta tela, independente do usuário. Um uso comum, é definir-se filtro que use o usuário logado como parte do critério. Por exemplo:

Imaginemos uma tela onde terá a informação de departamento; então deseja-se que os usuários do departamento A vejam apenas registros vinculados a este departamento, assim:

this.CODDEP IN(SELECT MAX(CODDEP) FROM TSIUSU WHERE CODUSU = ctx[usuario\_logado])

Neste exemplo, apenas linhas cujo departamento seja o mesmo do usuário logado serão apresentadas. A variável ctx[usuario\_logado] será substituída pelo código do usuário logado. Os campos da tabela devem ser referenciados através do alias this.

**Adicionar lançador:** Ao acionar esta opção, será aberta uma tela, onde você deverá informar a descrição e a pasta de destino. A **"Descrição"** é a identificação literal para o lançador; a pasta de destino, refere-se ao diretório do menu que abrigará o lançador de um determinado item. A operação estará concluída após a confirmação, pressionando o botão **"Concluir"**, e poderá também ser abortada, acionando o botão **"Cancelar"**.

![Imagem 48: Adicionar lançador: Ao acionar esta opção, será aberta uma tela, onde você deverá informar a descrição e a pasta de…](https://ajuda.sankhya.com.br/hc/article_attachments/360074229474)

**Localizar lançador:** Ao acionar esta opção, é apresentada a listagem de todos os lançadores que apontam para o item que corresponde ao item atual de navegação. Por exemplo, se determinado usuário estiver navegando entre relatórios personalizados, ao acionar esta opção, será aberta uma lista de todos os lançadores que correspondem ao item **"Relatório"** atual de navegação. Nesta tela, além de visualizar os lançadores para um item, pode-se excluir um lançador do item e/ou alterar sua descrição.

![Imagem 49: Localizar lançador: Ao acionar esta opção, é apresentada a listagem de todos os lançadores que apontam para o item que…](https://ajuda.sankhya.com.br/hc/article_attachments/360074229594)

Alterando a descrição de um lançador:

Para alterar a descrição de um lançador, primeiramente deve-se selecionar um lançador na grade.

A partir do momento em que o usuário começar a digitar no campo descrição, automaticamente serão habilitados os botões **"salvar"** e **"cancelar"** ativando assim o modo **"Alteração de Descrição"**;

Ao clicar em ![clip3113](https://ajuda.sankhya.com.br/hc/article_attachments/360061921573) **"Salvar"**, tem-se confirmadas as modificações da descrição.

No botão ![Imagem 51: No botão "Cancelar" , o modo "Alteração de descrição" será desabilitado, voltando para o estado normal da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/16845106030871) **"Cancelar"**, o modo **"Alteração de descrição"** será desabilitado, voltando para o estado normal da tela.

Através de um duplo clique em algum item da grade, este redirecionará para o determinado lançador, executando assim a função de lançador.

O botão **"Fechar"**, na parte inferior da tela, procede com seu fechamento.

**Observação:** sempre que selecionado um lançador na **"grade"**, o campo **"Descrição"** sofrerá modificações de modo a exibir qual a descrição daquele lançador selecionado;

O botão ![Imagem 52: O botão "Excluir" , estará disponível sempre que houver um lançador selecionado na grade. Ao clicar neste botão, será…](https://ajuda.sankhya.com.br/hc/article_attachments/16845092019991) **"Excluir"**, estará disponível sempre que houver um lançador selecionado na grade. Ao clicar neste botão, será apresentado uma mensagem de alerta para confirmação da exclusão

**Transformar Tabela em View:** Por meio desta opção, você realizará a transformação de uma tabela para uma view. Se a tela adicional em questão já possuir registros o sistema emitirá a seguinte mensagem:

**"Existem X registros na tabela. Ao converte-la TODOS OS DADOS SERÃO DEFINITIVAMENTE PERDIDOS. Deseja prosseguir?"**

Clicando-se em **"Sim"** o sistema deletará os registros e criará a View.

Se a tabela adicional já for uma View, o sistema emitirá a seguinte mensagem ao tentar transformar:

**"A tela atual já utiliza uma VIEW como unidade de dados!"**

Sendo feita a tentativa de criação de um novo campo para uma tela que já é View, o sistema emitirá a mensagem:

**"Para incluir o campo é necessário antes, criar o campo na view com um tipo que seja compatível"**

Sendo solicitada a exclusão de um campo, será emitida a seguinte mensagem:

**"Para excluir o campo é necessário antes, excluir o campo da view no banco de dados"**

Após a transformação da tabela em view o usuário poderá adicionar um lançador para esta tela. Se na view em questão não houver nenhum registro, por default os campos virão preenchidos com um registro padrão.

Quando a tela é transformada em view ela estará na base de dados da seguinte forma:

CREATE VIEW [sankhya].[AD\_PARAMETRO] (PARAMETRO,TIPO1,TIPO2,TIPO3,TIPO4,TIPO5,TIPO6,TIPO7) AS SELECT 0 AS PARAMETRO, CAST(NULL AS IMAGE) AS TIPO1, DATEADD(DAY, DATEDIFF(DAY, 0, '01/01/1970'), 0) AS TIPO2,1.0 AS TIPO3, DATEADD(DAY, DATEDIFF(DAY, 0, '01/01/1970'), 0) AS TIPO4,0 AS TIPO5,'' AS TIPO6,0 AS TIPO7 FROM DUAL

GO

**Definir chave primária para a unidade de dados:** Definir chave primária para a unidade de dados: Através desta opção, determine uma chave primária (PK) para as unidades de dados do tipo View. O sistema não permitirá que uma view fique sem PK; caso isso ocorra, será exibida a seguinte mensagem:

**"A unidade de dados dessa tela, requer no mínimo uma PK"**

**Painel de Filtros:** Por meio desta, será possível aprimorar ainda mais a personalização em Telas Adicionais. Ao acioná-la será aberta uma pequena tela **"Painel de Filtros"** onde serão disponibilizadas funcionalidades para configurar o Painel de Filtros conforme desejado. O objetivo desta configuração é disponibilizar um Painel de Filtros, localizado à esquerda, onde será possível realizar uma "busca rápida" informando os filtros configurados para a Tela Adicional em questão.

![Imagem 53: Painel de Filtros: Por meio desta, será possível aprimorar ainda mais a personalização em Telas Adicionais. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/360074230854)

Ao clicar no botão **"Adicionar filtro ao Painel de Filtros"**, serão apresentadas as configurações para geração do filtro fixo, de acordo com a Tabela e o seu respectivo campo selecionado.

![Imagem 54: Ao clicar no botão "Adicionar filtro ao Painel de Filtros" , serão apresentadas as configurações para geração do filtro…](https://ajuda.sankhya.com.br/hc/article_attachments/360075390553)

**Documento de ajuda:** Esta opção permite inserir na tela adicional uma documentação contendo informações que visam auxiliar o usuário na utilização e entendimento das funcionalidades pertinentes a mesma. Ao acessar esta opção, serão apresentadas as seguintes ações:

- **Upload documento:** Esta ação quando acionada, permite selecionar o documento que servirá de auxílio para o usuário. Sendo que, será possível selecionar  somente arquivos do tipo PDF. Caso já exista um documento inserido na tela, pode-se realizar a substituição do mesmo pelo documento atual.
- **Visualizar documento:** Através desta ação, teremos a visualização do documento de ajuda.
- **Remover documento:** Se utilizar esta ação, a eliminação do documento de auxílio inserido será feita.

Além disso, quando posicionado na tela ao acessar a Central de Ajuda, o help padrão será direcionado para a documentação de auxílio.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Compreendendo o Painel de Filtros

Para se entender o funcionamento do Painel de Filtros, é necessário compreender, ainda que de forma concisa, o funcionamento de uma consulta SQL. Este recurso se destina a usuários implantadores, responsáveis pela criação de Telas Adicionais.

Os filtros são criados a partir das informações dos próprios campos da tela, que passam a funcionar como uma espécie de argumento variável. O conjunto desses "argumentos" será apresentado em um painel lateral, onde se o usuário informar algum, o sistema irá incluir uma condição (where) na consulta SQL que é feita para obter os dados da tela. Vejamos que este é o fragmento de consulta que será inserido quando o usuário preencher, por exemplo, o campo "Idade" no Painel de Filtros:

this.IDADE = :IDADE

Imaginando que a consulta inteira fosse parecida com o trecho:

SELECT \* FROM AD\_PARTICIPANTES this

**Observação:** this é um apelido padrão que o sistema aplica à tabela principal da consulta.

O resultado seria:

SELECT \* FROM AD\_PARTICIPANTES this WHERE this.IDADE = :IDADE

Os campos no painel de filtros são do mesmo tipo de dados que cada campo representa. Assim, um campo numérico irá obter um argumento numérico, um campo de data irá obter uma data e um campo de texto consequentemente fornecerá argumento tipo texto.

#### Tipos de campos "especiais":

**Padrão:** Quando um campo é usado como filtro, utilizando este tipo, a interface empregada será muito semelhante à interface usada no formulário de edição. Deste modo, um campo que possui opções será exibido como um "Combo Box" (campo que abre uma lista ao ser clicado); representa uma ligação com outra tabela, será apresentado como uma Pesquisa; se for uma data, o componente de calendário será mostrado e assim por diante.

Porém, pode ser necessário utilizar outro tipo de interface, por exemplo, digamos que se queira ao invés de escolher especificamente uma data, usar um período, ou ainda, ao invés de escolher uma opção, seja necessário escolher várias opções. Para esses casos, existem tipos especiais que podem ser empregados:

**Multi-seleção:** Este tipo é destinado à campos que possuem lista de opções e para campos de Pesquisa. No caso de lista de opções, a lista é composta por todas as opções do campo. Quando o campo é do tipo Pesquisa, as opções devem ser inseridas através de uma busca.

**Período:** Campos do tipo "Data" possuem uma alternativa de representarem um Intervalo; neste caso, o usuário informará data inicial e final.

Caso seja informada apenas a data de início, o filtro será semelhante a:

this.DATAADMISSAO >= :DATAADMISSAO.INI

Quando somente a data final for fornecida, o filtro será equivalente a:

this.DATAADMISSAO <= :DATAADMISSAO.FIN

Se ambas as datas forem informadas, tem-se o seguinte filtro:

this.DATAADMISSAO BETWEEN :DATAADMISSAO.INI AND :DATAADMISSAO.FIN

#### Criando filtros:

Existem algumas opções para determinar como o filtro irá se comportar na tela, são elas:

**Nome da variável:** Nesse campo, determina-se o nome variável SQL. Por padrão, o sistema alimenta esse campo com o próprio nome do campo, porém isso pode ser alterado quando conveniente.

**Descrição:** Será utilizado no formulário para orientação do usuário. Como padrão, o sistema usa a própria descrição do campo mas caso necessário pode ser modificado.

**Obrigatório:** Esta marcação, determina que o filtro é obrigatório e portanto deve ser informado antes de se aplicar o filtro.

**Observação:** trabalhando-se com campos do tipo texto, cuja apresentação é **"Lista de Opções"**, ao marcar a opção **"Obrigatório"** serão exibidas as opções configuradas para o campo; caso a opção Obrigatório esteja desmarcada, serão acrescidas às opções do campo as alternativas **"Não informado"** e **"Informado"**.

**Salvar último valor:** Critérios marcados com esta opção, memorizam o último valor para a próxima vez que a tela for aberta.

**Considerar filtro de ligação:** Acionando-se esta marcação, quando se tratar de um campo pertencente ao tipo **"Pesquisa"** será considerado o filtro de ligação previamente configurado para a respectiva ligação.

**Valor padrão:** Quando a tela for aberta o critério será preenchido com esse valor.

**Intervalo de valores:** Esta é uma opção exclusiva para campos numéricos e determina valores máximos e mínimos permitidos no campo.

**Expressão (SQL):** Caso seja necessário personalizar o fragmento de SQL que será utilizado no filtro, deve-se usar esse campo. Por exemplo, digamos que se queira fazer um filtro do tipo "EXISTS" e que o nome do campo seja "DT" do tipo data, portanto teríamos:

EXISTS(

       SELECT 1

       FROM

             AD\_PARTICIPACAOEVENTOS EVENTO

       WHERE

             EVENTO.CODPARTICIPANTE = this.CODPARTICIPANTE AND

             EVENTO.DATA BETWEEN :DT.INI AND :DT.FIN

)

Lembrando que "this" refere-se ao apelido (ou 'alias') da tabela principal, esse filtro verifica a existência de registros em uma outra tabela tendo como base os registros da tabela principal e o critério informado no critério "DT".

**Expressão vazia:** Quando essa marcação estiver habilitada, o sistema não irá adicionar nenhum critério ao filtro, sendo portanto útil para se criar variáveis que podem ser utilizadas em outros critérios. No caso em que se personaliza uma expressão, é possível usar mais de um argumento. Usando o exemplo anterior é possível incluir o seguinte trecho:

EXISTS(

       SELECT 1

       FROM

             AD\_PARTICIPACAOEVENTOS EVENTO

       WHERE

             EVENTO.CODPARTICIPANTE = this.CODPARTICIPANTE AND

             EVENTO.DATA BETWEEN :DT.INI AND :DT.FIN AND

             EVENTO.LOCALEVENTO = :LOCAL

)

Nesse caso, a expressão acima está definida no campo 'Expressão SQL' do campo 'DT', e o campo LOCAL não possui expressão SQL, no entanto, ele pode ser utilizado aqui como variável. Esse recurso é muito útil para quando precisa-se de um filtro cujo campo não existe na tabela principal, mas sim em uma outra tabela que possui ligação com a tabela principal, como no exemplo acima.

**Observação:** para os filtros de telas adicionais, uma das regras utilizadas no sistema é que, quando as marcações dos filtros Não informado e o Informado estiverem selecionadas, o sistema irá trazer apenas os registros Informados, pois os mesmo possui precedência sobre os outros filtros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Recursos da Tela Adicional Criada

Com descrito anteriormente, as telas criadas serão acessadas pelo menu padrão do sistema e vão se parecer e comportar de maneira semelhante às telas padrão do sistema, ou seja, elas possuem modo grade/formulário, botões de edição dos registros, impressão da grade, assistente para montagem de filtros, configuração de layout, controle de acesso por usuário, etc. Vejamos abaixo demonstrações de alguns desses recursos:

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Configurações da Tela

![Imagem 55: Configurações da Tela](https://ajuda.sankhya.com.br/hc/article_attachments/360075390573)

Se você possuir acesso liberado para configurar telas, poderá efetuar modificações nas telas adicionais por meio do botão **"Configuração da Tela"** (em destaque na imagem acima); será possível por exemplo, buscar e mover os campos disponíveis para a coluna de campos selecionados, de modo que estes sejam apresentados na tela.

![Imagem 56: Se você possuir acesso liberado para configurar telas, poderá efetuar modificações nas telas adicionais por meio do…](https://ajuda.sankhya.com.br/hc/article_attachments/360075390613)

Feitas as modificações desejadas, acione o botão  salvar localizado no alto da tela. Mais informações sobre as Configurações da Tela, podem ser visualizados acessando o tópico [Conhecendo o SankhyaW/Recursos e Componentes/Configurações da Tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Criação de Filtros Personalizados através do "Assistente de Filtro"

![Imagem 57: Criação de Filtros Personalizados através do "Assistente de Filtro"](https://ajuda.sankhya.com.br/hc/article_attachments/360075390653)

**Importante:** nas telas adicionais, ao aplicar um filtro personalizado o sistema não exibirá os pais que não possuam filhos "Analíticos", mesmo que o filtro satisfaça registros filhos que sejam sintéticos.

Mais detalhes podem ser visualizados através do tópico [Conhecendo o Sankhya-W/Recursos e Componentes/Assistente de Filtro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Relatórios Rápidos através do botão "Impressão do Grid"

A medida que a tela é alimentada, pode-se através do botão **"Impressão do Grid"** (em destaque na imagem abaixo) exportar os dados como PDF, como Planilha ou ainda visualizá-los em Cubo.

![Imagem 58: A medida que a tela é alimentada, pode-se através do botão "Impressão do Grid" (em destaque na imagem abaixo) exportar…](https://ajuda.sankhya.com.br/hc/article_attachments/360075391033)

Na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025240174-Relat%C3%B3rios-Formatados) tem-se o campo **"Tela/Instância"** que permite a inserção de qual tela está relacionado o relatório:

![Imagem 59: Na tela Relatórios Formatados tem-se o campo "Tela/Instância" que permite a inserção de qual tela está relacionado o…](https://ajuda.sankhya.com.br/hc/article_attachments/360074231334)

**Importante:** quando o sistema preencher os relatórios vinculados às telas, ele irá preencher automaticamente os parâmetros cujos nomes sejam iguais aos nomes das colunas da chave primária da tabela prefixados com **PK\_**. Considerando o exemplo onde o nome da PK da tabela é NUMERO, então o parâmetro que deve ser criado no relatório é **PK\_NUMERO**, e este poderá ser usado em qualquer lugar do relatório, usando a notação padrão de parâmetro no iReport, ou seja, $P{PK\_NUMERO}. Isso significa que o relatório poderá filtrar em sua query apenas o registro que está atualmente posicionado na grade da tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Criar um novo item no Menu do Sistema

Deve-se disponibilizar no menu do sistema as telas criadas.

![Imagem 60: Deve-se disponibilizar no menu do sistema as telas criadas.](https://ajuda.sankhya.com.br/hc/article_attachments/360075391153)

Na tela [Menu do Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112053-Menu-do-Sistema-) depois de selecionado em qual item do menu será incluída a nova tela, deve-se acionar o botão ![clip4273](https://ajuda.sankhya.com.br/hc/article_attachments/360060998074) **"Criar Novo Item"**  para que a tela **"Criando novo item em (nome do item)"** seja apresentada:

![Imagem 62: Na tela Menu do Sistema depois de selecionado em qual item do menu será incluída a nova tela, deve-se acionar o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/360074231454)

Na **"Descrição"** será indicado o nome do item que corresponderá à tela adicional criada; no campo **"Tipo"** escolha entre as opções **"Lançador"** ou **"Pasta"**, no nosso exemplo o tipo do item é lançador; o **"Tipo Lançador"** no caso trata-se de uma Tela adicional.

![Imagem 63: Na "Descrição" será indicado o nome do item que corresponderá à tela adicional criada; no campo "Tipo" escolha entre as…](https://ajuda.sankhya.com.br/hc/article_attachments/360074231474)

Após a conclusão da criação do novo item, o mesmo será visualizado no respectivo menu.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Controle de Acessos

Vimos que o Sankhya-Om permite a criação de telas personalizadas, de forma que é possível criar tanto telas **"mestre"** quanto telas "detalhe" (também chamadas "filhas") e associá-las, fazendo com que a tela **"detalhe"** apareça dentro da tela "mestre", como uma aba. Além disso, vimos que para uma tela personalizada, seja ela mestre ou detalhe, é possível criar um item de menu para iniciá-la.

Para cada item de menu pode-se associar permissões de acesso para os usuários, assim, um mesmo usuário pode possuir permissões diferentes para a tela **"mestre"** e para a tela **"detalhe"**, quando isso acontece o sistema irá considerar os acessos individualmente, mesmo quando uma tela detalhe é acessada através da tela mestre a tela detalhe terá suas permissões por usuário respeitadas. Se a tela detalhe não possuir um item no Menu do Sistema, então os acessos são herdados da tela mestre. Se a tela detalhe existir no Menu do Sistema, mas o usuário não possuir nenhum acesso a ela, a aba não aparecerá na tela mestre; caso o usuário tenha qualquer acesso a aba aparecerá para consulta, pois qualquer acesso garante consulta.

Vejamos abaixo o exemplo de como o sistema irá se comportar:

Suponhamos que o cliente seja uma faculdade, e deseja criar uma tela para cadastrar cursos e suas respectivas disciplinas. Um caso de uso seria o seguinte:

- São dois usuários a serem criados: DIRETOR e COORDENADOR. Sendo que o DIRETOR pode incluir/alterar/excluir cursos, mas não pode incluir/alterar/excluir disciplinas. E o COORDENADOR por sua vez pode apenas visualizar cursos, mas pode incluir/alterar/excluir disciplinas;
- Cria-se também a tela adicional CURSOS, com código, descrição, etc. Com o item de menu Cursos e na configuração de acessos concede-se privilégio para consulta, inclusão, alteração e exclusão para DIRETOR, e para COORDENADOR concede-se se privilégio para consulta, inclusão, alteração e exclusão para DIRETOR, e para COORDENADOR concede-se apenas acesso de consulta;
- Cria-se a tela adicional DISCIPLINAS, de forma que esta seja uma tela DETALHE da tela CURSOS (ou seja, cria-se o relacionamento de Curso para Disciplina). Assim, ao acessar a tela Cursos, deve haver uma aba para as Disciplinas para cada curso. Neste momento, a aba Disciplinas deve respeitar os acessos da tela Cursos;
- Para a tela Disciplinas, cria-se um item de menu, de forma que possa ser acessado sem entrar na tela Cursos. Configura-se o controle de acesso conforme definido no início. Nesse momento, ao entrar na tela Cursos, a aba Disciplinas irá respeitar as configurações do seu próprio item de menu para o usuário que está acessando a tela.

**Conclusão:** Ao acessar a tela Cursos, o usuário DIRETOR poderá incluir/alterar/excluir cursos, mas na Aba Disciplinas ele poderá apenas fazer consultas. Por sua vez, o COORDENADOR pode acessar a tela Cursos e consultar, mas não poderá incluir/editar/excluir os registros de Cursos, porém, na aba Disciplinas ele terá acesso para incluir/editar/excluir, conforme configurado para o COORDENADOR no Controle de Acesso para o item de Menu da tela Disciplinas;

Pode-se visualizar mais informações sobre o Controle de Acessos, por meio do tópico [Conhecendo o Sankhya-W/Recursos e Componentes/Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598934-Conhecendo-o-Sankhya-W).

Acesse aqui o tópico [Configurando Ações Personalizadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111093-Configurando-A%C3%A7%C3%B5es-Personalizadas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)

### Parâmetros

Ao realizar-se a criação de uma tela adicional, através da ativação do parâmetro **"Configuração da grade respeita config. da tela - CONFGRARESPTEL"**, o usuário administrador pode realizar a organização dos campos (ocultá-los ou apresentá-los), de modo que os demais usuários não irão conseguir reconfigurar a tela no modo formulário ou no modo grade, ou seja, não poderão retornar ou remover os campos para a tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111773-Construtor-de-Telas#top)
