---
id: "360045108893"
titulo: "Configuração de Transições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:53:57Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Expressão", "Operações de Estoque", "Atividade Base", "Configuração de Transições", "Execução", "Filtros de Transições", "Matéria-Prima", "Configuração de Transições manual", "Estoque", "Produção", "br.com.sankhya.mgeprod.cad.composicao.produto", "Aba Estoque: operações momentos impressora", "Configuração transições: duplo clique \"Editar\"", "Aba Geral: transições expressões status", "Transições", "Fluxo de Processo"]
---

# Configuração de Transições

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312760427287) Módulo: Produção > Cadastros > Produtivo - Botão Roteiro
```

---

Outro ponto de extrema importância na construção do Fluxo do Processo Produtivo, derivado das formatações realizadas através do [Botão Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793), é a configuração das transições do fluxo, onde o sistema permite a realização de tal configuração a partir de um duplo clique sobre as mesmas ou acionando a opção **"Editar"** por meio de um clique com o botão esquerdo (as transições são as setas contínuas que ligam os elementos do fluxo). Utilizando qualquer uma das duas ações será exibido o pop-up **"Configuração de Transição"**.

Acesse os links abaixo para facilitar sua navegação:

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abageral) |  | [Aba Filtros de Transições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abafiltrosdetransies) |
| --- | --- | --- |
| [Aba Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abaoperaesdeestoque) |  |  |

![Imagem 2: Aba Operações de Estoque](https://ajuda.sankhya.com.br/hc/article_attachments/8892629805719)

## Aba Geral

Esta aba, tem por objetivo a determinação das configurações gerais das transições entre as atividades, que irão de fato estabelecer o fluxo que o processo deverá seguir em tempo de execução.

A marcação **"Padrão"** determina que a transição em questão é a referência no caso de todas as condições falharem.

O espaço do campo **"Expressão"** é destinado a determinar uma condição que torne a transição executável. Este deverá ser utilizado somente quando a transição for condicional. Utilize uma expressão escrita em "Java Script".

**Nota:** é importante lembrar que durante a execução de OPs do Processo, essa expressão será executada assim que o Gateway (ponto de decisão) a qual ela esteja ligada seja atingido. O resultado da execução esperado é verdadeiro (true = 1) ou falso (false = 0). A expressão da transição será utilizada em conjunto com os filtros de transições utilizando o operador de adição AND:

(Expressão javaScript aba Geral) && Filtros de Transição (transição 1511)

Através do campo **"Status da Execução"**, selecione o "status" de execução do processo, quando a transição em questão for atravessada. Você pode definir dentre as seguintes opções:

- Reprocesso;
- Mantém Status Atual;
- Normal.

Aponte por meio do campo **"Ordem"** a sequência de avaliação da transição. Sendo que o mesmo deverá ser utilizado somente quando a transição participar de um Gateway do tipo **"Exclusivo"**, na qual a primeira transição verdadeira faz com que siga o fluxo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#top)

## Aba Filtros de Transições

Nesta aba, são definidos os filtros que serão avaliados na transição. Estes filtros deverão ser utilizados somente em situações em que transições condicionais são aceitas. Determine no campo **"Tipo"**, a espécie de filtro de transição a ser utilizado. Sendo que cada possibilidade quando acionada, apresentará seus respectivos campos de acompanhamento. Abaixo teremos a descrição de cada uma delas:

| [Produto Acabado em Processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#produtoacabadoemprocessamento) |  | [Estoque Disponível de MP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#estoquedisponveldemp) |
| --- | --- | --- |
| [Necessidade de Setup para Centro de Trabalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#necessidadedesetupparacentrodetrabalho) |  | [Condição Personalizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#condiopersonalizada) |

![Imagem 3: Condição Personalizada](https://ajuda.sankhya.com.br/hc/article_attachments/8892630677783)

**Produto Acabado em Processamento**

Será conveniente o uso desta opção, quando o Produto Acabado estiver em processamento na instância do processo. Nesse caso é obrigatória a seleção de um produto no campo **"Produto (PA)"**.

**Produto (PA):** utilize este campo para determinar qual Produto Acabado deve estar em processamento na instância do processo para execução do filtro. Quando se deseja que o filtro seja avaliado para qualquer Produto Acabado que esteja sendo processado, este campo não deve ser utilizado.

**Controle (PA):** neste campo informe o controle do produto selecionado. Apenas será exibido quando o Produto Acabado possuir controle adicional por lista.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abafiltrosdetransies)

**Estoque Disponível de MP**

Esta opção será apropriada, quando a matéria-prima possuir estoque disponível conforme necessidade listada na atividade base. Caso necessário, é possível definir uma expressão que busca a quantidade de estoque no campo **"Expressão"**. Essa matéria-prima pode ser também um Produto Intermediário, e nestes casos, a atividade base é um subprocesso de produção.

**Atividade Base:** este campo, deve ser utilizado para especificar a atividade que será empregada como base da operação. Seu preenchimento se torna obrigatório, apenas quando o tipo do filtro for **"Estoque disponível de MP"** ou **"Necessidade de Setup para Centro de Trabalho"**.

**Matéria-Prima:** utilize este campo, para especificar-se qual matéria-prima deve ter o estoque avaliado. Se este campo não for preenchido, todas as matérias-primas necessárias na atividade base serão avaliadas, conforme marcação **"Valida estoque em transições condicionais"** na lista de materiais. Deve ser utilizado somente quando o tipo do filtro for **"Estoque disponível de MP"**.

**Controle (MP):** este campo será exibido para preenchimento, quando a matéria-prima selecionada possuir controle adicional por lista. É um campo a ser utilizado para especificar o controle da matéria-prima que deve ter o estoque avaliado.

**Empresa:** informe aqui a empresa que será utilizada para busca do estoque. Não sendo informada uma empresa neste campo, será utilizada a mesma do processo de produção.

**Local:** determine neste campo, o local onde será checado o estoque.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abafiltrosdetransies)

**Necessidade de Setup para Centro de Trabalho**

O uso desta opção se justifica, se o Centro de Trabalho em uso na atividade base sempre exigir setup, ou quando condicional, o setup atual for incompatível com o Produto Acabado em processamento.

**Atividade Base:** este campo deve ser utilizado para especificar a atividade que será empregada como base da operação. Seu preenchimento se torna obrigatório, apenas quando o tipo do filtro for **"Estoque disponível de MP"** ou **"Necessidade de Setup para Centro de Trabalho"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abafiltrosdetransies)

**Condição Personalizada**

A utilização desta opção será válida, se a expressão especificada no campo **"Expressão"** retornar linha onde a primeira coluna seja numérica com valor maior que zero.

**Expressão:** neste campo, defina uma expressão em SQL que deve retornar uma linha com uma coluna numérica. Caso o valor seja igual a **"0"** (zero), a expressão será considerada falsa, caso contrário será verdadeira. O sistema vai injetar os seguintes parâmetros na consulta:

- CODPRODPA
- CONTROLEPA
- CODPRODMP
- CONTROLEMP
- CODEMP
- CODLOCAL
- IDPROC

![Imagem 4: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16646706154519) **Informações adicionais:**

Os filtros de transições são avaliados de forma agrupada ao tipo do filtro (Produto Acabado, Estoque Disponível de MP, Necessidade de Setup para o Centro de Trabalho e Condição personalizada) considerando OR para cada filtro do mesmo grupo, ou seja, se qualquer uma das expressões do grupo retornar verdadeiro (true = 1), então o grupo resulta em verdade.

Os grupos são avaliados considerando AND, ou seja, o resultado da Transição será verdadeiro, apenas se todos os grupos existentes resultarem em verdadeiro (true = 1). Segue um exemplo:

P - Produto Acabado = { true , false , false } -> resultado do grupo P = 'true';

S - Expressão Personalizada = { false, false } -> resultado do grupo S = 'false';

Resultado da transição, neste exemplo será 'false', pois o grupo S é false.

Para as expressões personalizadas do filtro de transição estão disponíveis alguns parâmetro para uso, são eles:

:IDPROC - Código de identificação do Processo Produtivo.

:IDIPROC - Nro da Ordem de Produção.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#abafiltrosdetransies) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#top)

## Aba Operações de Estoque

Nesta aba, são configuradas as operações com estoque que irão ocorrer automaticamente no decorrer da atividade do Processo Produtivo.

Essas operações podem ser de qualquer tipo (pedidos, notas, requisições, transferências etc). Cada atividade pode possuir um número infinito de operações, que podem ocorrer em vários momentos diferentes do ciclo de vida da atividade. A coerência entre as diversas operações que ocorrem em uma atividade, é de responsabilidade do configurador do processo.

Você pode selecionar diversos tipos diferentes de itens que irão compor estas operações com estoque, por exemplo, as matérias-primas necessárias na atividade, produtos acabados apontados na atividade, subprodutos gerados na atividade etc.

![Imagem 5: Você pode selecionar diversos tipos diferentes de itens que irão compor estas operações com estoque, por exemplo, as…](https://ajuda.sankhya.com.br/hc/article_attachments/8892610333207)

O campo **"Código"** é alimentado automaticamente com a chave de identificação da operação de estoque configurada.

Utilize o campo **"Ordem"** para determinar a sequência em que as operações serão executadas.

Determine o momento em que a operação de estoque deve ser gerada por meio do campo **"Quando"**. Você pode escolher dentre as seguintes opções:

- **Saída:** define que a operação de estoque irá acontecer quando a atividade for encerrada.
- **Ao preencher um formulário:** determina que a operação de estoque deve acontecer quando for finalizado o preenchimento de um formulário.

**Nota:** não implementada.

- **Ao apontar PA:** esta opção representa que a operação de estoque irá acontecer quando o Produto Acabado for apontado.
- **Quando o usuário iniciar a atividade:** estabelece que a operação deve acontecer quando a atividade for iniciada pelo usuário.
- **Entrada:** define que a operação de estoque irá acontecer quando a atividade for criada.
- **Aceite da atividade:** determina que a operação de estoque deve acontecer no aceite da atividade pelo usuário.
- **Ao apontar materiais de ajustes:** esta opção representa que a operação de estoque deve acontecer quando forem apontados os materiais de ajuste pelo usuário.

No campo **"Modelo de Nota"** indique um modelo de pedido/nota a ser utilizado na operação de estoque. Os modelos aqui apresentados para escolha, devem ser previamente cadastrados na rotina [Modelo de Notas e Pedidos.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514)

O campo **"Atividade Base"** propicia a determinação da atividade que será utilizada como base da operação, ou seja, de onde virá a lista de materiais ou o apontamento de Produtos Acabados que serão utilizados como itens das notas.

O parceiro para ser utilizado na operação de estoque será indicado por meio do campo **"Parceiro"**. Caso este campo não seja alimentado, o sistema irá utilizar o parceiro da nota modelo.

O campo **"Centro de Resultado"** é utilizado para selecionar o Centro de Resultado que será utilizado na operação de estoque. Se o mesmo for mantido sem preenchimento, o sistema irá utilizar o Centro de Resultado da nota modelo.

Indique um projeto a ser utilizado na operação de estoque através do campo **"Projeto"**. Ocorrendo do mesmo não ser preenchido, o sistema irá utilizar o projeto da nota modelo.

Através do campo **"Natureza"** defina uma natureza a ser utilizada na operação de estoque. Na hipótese do mesmo estar sem informações, o sistema irá empregar a natureza da nota modelo.

Temos no campo **"Tipo de Negociação"** a funcionalidade de selecionar um Tipo de Negociação para ser utilizada na operação de estoque, caso esse campo não seja preenchido o sistema usará o tipo de negociação da nota modelo.

Defina no campo **"Tipo de Operação"**, uma TOP a ser utilizada na operação de estoque. Sendo que, caso este campo seja mantido em branco, o sistema irá utilizar a TOP da nota modelo.

O campo **"Local de Origem"** é destinado a determinar o local de princípio para os itens da operação de estoque. Caso esse valor não seja informado, ele receberá **"0"** (zero) por padrão, e o material sendo controlado por local, o sistema irá aplicar como local o Local de origem do Processo Produtivo.

Utilize o campo **"Local de Destino"** para designar o local de destinação para os itens para a operação de estoque. Caso esse valor não seja informado, ele receberá **"0"** (zero) por padrão, e o material sendo controlado por local, o sistema irá utilizar como local o Local de destino do Processo Produtivo.

Empregue o campo **"Local para baixa de MPs"**, para apontar o local de baixa de Matérias-Primas sempre que a operação de estoque corresponder a uma nota de produção. Quando este campo não for alimentado (valor = "0"), o sistema irá buscar o local com a seguinte regra: **1º** - Local do Centro de Trabalho, **2º** - Local de Manufatura, definido no cabeçalho do processo.

Indique no campo **"Empresa Origem"** a instituição de princípio que será utilizada para a operação de estoque.

Diferente do campo anterior, informe no campo **"Empresa Destino"** a corporação de paradeiro da operação de estoque. Seu preenchimento é necessário, apenas quando a operação de estoque seja uma transferência. Caso o mesmo não seja preenchido, será utilizada a empresa de origem da operação de estoque.

Por meio do campo **"Tipo dos Itens"** determine o que será utilizado como itens no movimento. Você poderá definir dentre as seguintes opções:

- **Subproduto da Atividade:** será utilizada a quantidade de subproduto apontada, menos à quantidade que já tenha sido movimentada.
- **Produto acabado apontado na atividade:** a lista de materiais será a soma de todos os apontamentos feitos até o momento, independente da atividade onde tenham sido apontados. Esta marcação é útil em situações onde se aponta Produtos Acabados em diversas atividades, mas deseja-se gerar a nota de produção apenas no final do processo.
- **Lista de materiais de todas as atividades:** quando utilizada esta opção, o sistema irá considerar apenas atividades do fluxo principal. Geralmente se utiliza essa opção em atividades no início do processo. Selecionando esta opção, todas as matérias-primas serão multiplicadas pela quantidade de Produto Acabado presentes na lista de Produtos Acabados a produzir na instância do processo, sempre subtraindo a quantidade já utilizada em um registro de operação com estoque do processo.
- **Materiais de ajuste:** o sistema irá utilizar materiais de ajuste presentes no apontamento de materiais deste tipo. Somente deve ser utilizado em conjunto com o campo **"Quando"** marcado como **"Ao apontar materiais de ajustes"**.
- **Lista de materiais da atividade base:** a quantidade de cada matéria-prima será multiplicada pela quantidade de Produto Acabado presente atualmente no repositório de entrada, subtraindo a quantidade utilizada em operações anteriores. Caso o repositório não possua Produto Acabado, será utilizada a quantidade a ser produzida.

A impressora que será selecionada nas operações de estoque, será apontada no campo **"Selecionar Impressora"**. As opções disponíveis são:

- Conforme a TOP;
- Específica;
- Usar impressora Padrão do Centro de Trabalho.

O campo **"Impressora"**, é utilizado para informar o nome ou apelido de uma impressora a qual deseja imprimir documentos da atividade.

Determine no campo **"Status da Execução"**, em qual "status" de execução a operação será concretizada. As opções disponíveis para escolha são:

- **Todos:** ao selecionar esta opção, a operação será executada em todas as situações.
- **Normal:** essa opção faz com que a operação seja executada apenas quando a atividade estiver sendo efetivada em situações normais.
- **Reprocesso:** através desta opção, a operação será executada apenas quando a atividade estiver sendo efetuada em situações de reprocesso.

O campo **"Formulário"** será habilitado apenas quando o momento da operação de estoque for ao preencher formulário. O sistema irá utilizar o valor dos campos do formulário sempre que encontrados. Os campos que serão considerados serão:

- CODPARC;
- CODCENCUS;
- CODPROJ;
- CODNAT;
- CODTIPVENDA;
- CODTIPOPER;
- CODLOCALORIG;
- CODLOCALDEST;
- CODEMPORIG;
- CODEMPDEST.

Se um campo não for encontrado no formulário, então este será ignorado e o valor utilizado será o da operação, ou o obtido através da nota modelo.

Utilize a marcação **"Confirmar Operação"** para determinar se a operação (nota, requisição, entre outros) deverá ser confirmada no momento da geração. Essa marcação é predominante sobre qualquer outra configuração.

A marcação **"Baixar reserva na nota de produção"** deve ser utilizada nas operações de pedidos que reservam estoque. Ao gerar operações de produção, o sistema irá baixar essas reservas, vinculando o item de matéria-prima à nota de produção com o item do pedido.

Defina no campo **"Tipo de Execução"** quando a operação de estoque deverá ser executada, em relação a terceirização da atividade. Serão apresentadas as seguintes opções:

- **Terceiros:** esta opção representa que a referida operação de estoque será executada se a atividade estiver sendo executada por terceiros.
- **Própria:** por meio desta opção, indica-se que esta operação de estoque será efetivada se a atividade estiver sendo executada internamente, ou seja, não terceirizada.
- **Todos:** através desta opção, temos que esta operação de estoque será realizada independente se a atividade for terceirizada ou não.

A opção **"Usar o Parceiro Terceiro"** quando acionada, determinará que o parceiro terceiro da Ordem de Produção/Operação será o parceiro do documento gerado por essa operação de estoque.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108893-Configura%C3%A7%C3%A3o-de-Transi%C3%A7%C3%B5es#top)
