---
id: "360044599094"
titulo: "Extrato de Materiais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:51:31Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Produto", "Materiais", "Acabado", "Matérias", "MPs", "Primas", "Extrato de Materiais manual", "Extrato", "Ordens de Produção", "Estoque", "Produção", "br.com.sankhya.producao.rotina.OrdemProducao", "Verifica estoque e substituições no lançamento de OP", "Ajuste de MP e PI por alternativas com controle e estoque", "Matérias Primas Produtos Acabados e Materiais Alternativos"]
---

# Extrato de Materiais

Localizado no cabeçalho da grade **"Ordens de Produção (OP)"** no [Lançamento de Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599554-Lan%C3%A7amento-de-uma-Ordem-de-Produ%C3%A7%C3%A3o-OP-), o botão ![Imagem 1: Localizado no cabeçalho da grade "Ordens de Produção (OP)" no Lançamento de Ordem de Produção , o botão disponibiliza o…](https://ajuda.sankhya.com.br/hc/article_attachments/4416748947735) disponibiliza o Extrato de Materiais, que é um excelente recurso disponibilizado aos Gestores de Produção, em um cenário onde o Lançamento de Ordens de Produção ocorre de forma manual, uma vez que apresenta a informação de estoque atual da fábrica no instante, com base nas OP's e tamanhos de lote que você deseja lançar. Desta maneira, é possível evitar problemas durante a execução da Ordem de Produção, quanto ao estoque de materiais.

Os problemas de estoque apresentados, podem facilmente serem resolvidos a partir da substituição da matéria-prima por um material alternativo, ou seja, a Ordem de Produção em questão deixará de utilizar a MP prevista em sua composição, e utilizará uma alternativa selecionada por você no lançamento da referida Ordem.

[Grade Matérias Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#gradematriasprimas)                                               [Grade Produtos Acabados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#gradeprodutosacabados)

[Grade Materiais Alternativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#grademateriaisalternativos)

Ao acionar o botão **"Extrato MPs"** será apresentado a seguinte tela:

![Imagem 2: Ao acionar o botão "Extrato MPs" será apresentado a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/4416756620311)

### Grade Matérias Primas

A grade Matérias Primas, exibe todas as matérias-primas necessárias para a produção dos Produtos Acabados (PA's) associados às Ordens do lançamento.

**Importante:** apenas as matérias-primas ligadas as atividades definidas como **"Lista de matéria-prima padrão"** ([Botão Roteiro - Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abageral)).

Ao habilitar a marcação **"Apresentar PIs"**, teremos a exibição de todas as MPs sendo estes Produtos Intermediários (PI) ou não. Quando desmarcada, somente as MPs que não são Produtos Intermediários (PI) são apresentadas.

A exibição dos dados nesta aba é global, ou seja, caso existam duas ou mais [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o), ou dois, ou mais PA's no lançamento, serão exibidas todas as matérias-primas necessárias para a produção dos mesmos de forma agrupada (por matéria-prima). Temos na grade, as seguintes informações:

**Matéria Prima:** código da matéria-prima.

**Descrição:** descrição da matéria-prima.

**Controle:** esta informação é alimentada, quando a matéria-prima possui controle adicional por **"Lista"** ou **"Livre"**.

**Referência:** referência do produto.

**Estoque:** esta coluna exibe o estoque atual da matéria-prima. Seu resultado é influenciado pelo filtro de estoque da tela que pode ser configurado a partir do botão **"Configurações de estoque"** localizado na parte superior direita da tela.

**Necessidade:** temos nesta coluna, a quantidade necessária da matéria-prima em questão para este lançamento, ou seja, a soma da necessidade do material para todos os PA's presentes no lançamento.

**Qtd. Substituída:** aqui é apresentada a quantidade da matéria-prima que foi substituída por algum material alternativo. De acordo com a alteração realizada, o material que irá substituir a MP ou então a quantidade, essa coluna é recalculada.

**Qtd. Usar:** essa coluna exibe a quantidade que será utilizada desta matéria-prima no lançamento. Inicialmente, esse valor é igual à Necessidade; a medida que é feita a substituição da matéria-prima por algum material alternativo, esse valor vai sendo reduzido.

**Qtd. em OPs:** aqui é apresentada a quantidade de PI's que estão em Ordens de Produção e que não possuem dependência com nenhuma OP. 

**Saldo:** temos aqui, uma coluna calculada que apresenta o saldo atual da matéria-prima em questão, dado todo estoque da matéria-prima e também o arranjo de substituição que pode ter sido realizado no lançamento:

| ``` ![Imagem 3: Saldo = Estoque - Qtd. Usar * - Qtd. Usar **](https://ajuda.sankhya.com.br/hc/article_attachments/42312727408279) Saldo = Estoque - Qtd. Usar* - Qtd. Usar** ``` |
| --- |

Onde:

**Qtd. Usar**\*: é a quantidade que será utilizada da matéria-prima (campo **"Qtd. Usar"** da grade Matérias Primas).

**Qtd. Usar**\*\*:é a quantidade que será utilizada da matéria-prima, caso a mesma seja utilizada como Matéria-Prima Alternativa de outra matéria-prima no lançamento (somatório do campo Qtd. Usar da grade Materiais Alternativos para essa matéria-prima).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#top)

### Grade Produtos Acabados

Nesta grade, temos os Produtos Acabados que utilizam a matéria-prima selecionada na grade Matérias Primas.

![Imagem 4: Nesta grade, temos os Produtos Acabados que utilizam a matéria-prima selecionada na grade Matérias Primas .](https://ajuda.sankhya.com.br/hc/article_attachments/4416781541783)

As colunas apresentam as seguintes informações:

**Sequência:** nessa coluna, é exibida a sequência da Ordem de Produção para o PA. Essa sequência representa a OP que será gerada.

**Produto Acabado:** código do produto acabado.

**Descrição:** descrição do produto acabado.

**Controle:** esta informação é alimentada, quando o produto acabado possui controle adicional por "Lista" ou "Livre".

**Tam. Lote:** tem-se nesta coluna, o tamanho de lote da Ordem de Produção que será lançada para a produção do produto acabado.

**Referência:** referência do produto acabado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#top)

### Grade Materiais Alternativos

Essa grade apresenta os Materiais Alternativos pelos quais a matéria-prima selecionada na grade superior poderá ser substituída. A seleção do PA na grade Produtos Acabados serve como um filtro, ou seja, a substituição acontecerá para a OP do produto selecionado na referida grade.

![Imagem 5: Essa grade apresenta os Materiais Alternativos pelos quais a matéria-prima selecionada na grade superior poderá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4416781589655)

Para os Materiais Alternativos serem apresentados nesta grade, é necessário, realizar o vínculo dos mesmos ao PA e matéria-prima em questão. Este vínculo, na verdade, é uma possibilidade de mudança de formulação do produto, portanto, deve acontecer em algum momento antes da equipe responsável pela composição do produto utilizar esta funcionalidade.

Será possível realizar também nesta grade, a substituição parcial ou total de um Produto Intermediário por um outro PI alternativo no Lançamento de OP.

**Observação:** se o PI for fabricado a partir de uma sub-ordem ligada à ordem de fabricação do PA, será ajustado esta sub-ordem para o PI alternativo. Neste contexto, considere para o PI alternativo as mesmas configurações do produto substituído, como o Tipo do PI, a Quantidade em estoque, o Tipo de sub-ordem e o Tipo de Numeração de Lote (tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), aba [Produtos(PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaprodutospa), sub-aba [Produtos(PI)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#pa-abaprodutospi)).

Vale salientar que os produtos exibidos na grade, são influenciados pela seleção primeiramente realizada nas grades Matérias-primas e Produtos Acabados, que servem como filtro para esta terceira grade.

Inicialmente temos na grade Materiais Alternativos, um check box (marcação) que permite a seleção do material em questão, para substituir a matéria-prima e produtos acabados selecionados, grades Matérias Primas e Produtos Acabados, respectivamente.

Temos nesta grade as seguintes informações: 

**MP. Alternativa:** código do material alternativo.

**Descrição:** descrição do material alternativo.

**Referência:** referência do material.

**Controle:** esta informação é alimentada, quando o material alternativo possui controle adicional por **"Lista"** ou **"Livre"**.

**Estoque:** essa coluna exibe o estoque atual do material alternativo. Seu resultado é influenciado pelo filtro de estoque da tela que pode ser configurado a partir do botão **"Configurações de estoque"** localizado na parte superior direita da tela.

**Necessidade:** temos nesta coluna, a quantidade necessária do material alternativo caso o mesmo seja utilizado para substituir a matéria-prima.

**Qtd. Usar:** esse campo é livre para digitação, pois nele será especificado a quantidade do material que será utilizado para substituir a matéria-prima.

**Conjunto:** essa coluna apresenta o número do conjunto, ao qual o material alternativo em questão pertence. Caso este campo não esteja preenchido, significa que o material não pertence a nenhum conjunto.

**Qtd. Lanç.:** temos nesta coluna, a quantidade do material em uso neste lançamento, ou seja, a quantidade do mesmo utilizado na substituição de alguma matéria-prima, e a quantidade do mesmo utilizado como matéria-prima no lançamento.

**Saldo:** campo calculado que apresenta saldo atual do material alternativo. O objetivo desse campo, é apresentar no momento do lançamento, qual o saldo atual do produto dado todo o arranjo de substituição já realizado:

| ``` ![Imagem 6: Saldo = Estoque - Qtd. Usar * - Qtd. Usar **](https://ajuda.sankhya.com.br/hc/article_attachments/42312727408279) Saldo = Estoque - Qtd. Usar*- Qtd. Usar** ``` |
| --- |

Onde:

**Qtd. Usar\***: é a quantidade que será utilizada da matéria-prima (campo Qtd. Usar da grade Matérias Primas).

**Qtd. Usar\*\***: é a quantidade que será utilizada da matéria-prima caso a mesma seja utilizada como MP Alternativa de outra matéria-prima no lançamento (somatório do campo Qtd. Usar da grade Materiais Alternativos para essa matéria-prima).

Para executar a substituição por Materiais Alternativos propriamente dita, é necessário marcar o check box da linha correspondente ao material, especificar a quantidade que se deseja utilizar (coluna Qtd. Usar) e salvar o registro.

Esta grade conta com algumas funcionalidades que auxiliam no momento da seleção dos materiais alternativos. A saber:

- Ao selecionar um material pertencente a um conjunto, todos os materiais do mesmo conjunto são selecionados.
- Ao selecionar um material, o sistema pressupõe que a substituição da matéria-prima irá acontecer de forma completa. Então ajusta a coluna **"Qtd. Usar"** com a quantidade necessária do material para essa substituição, ou seja, ajusta o valor de Qtd. Usar de modo que este recebe o mesmo valor do campo **"Necessidade"**.
- Ao editar a Qtd. Usar de um material pertencente a um conjunto, a Qtd. Usar de todos os materiais do mesmo conjunto sofrem ajuste de forma proporcional.
- Caso um material alternativo seja selecionado e o saldo para o mesmo seja menor que zero, a linha em questão receberá a coloração **vermelha**, sinalizando um problema. Caso o saldo não seja menor que zero, a linha receberá a coloração **azul**, demostrando a normalidade na substituição.

**Botões da grade**

No cabeçalho da grade temos alguns botões que possuem o seguinte comportamento:

**![Imagem 7: Salvar: este botão, salva a edição de substituição realizada na grade.](https://ajuda.sankhya.com.br/hc/article_attachments/4416769669655) Salvar:** este botão, salva a edição de substituição realizada na grade.

![Imagem 8: Cancelar: por meio deste botão, você cancela a edição de substituição realizada na grade.](https://ajuda.sankhya.com.br/hc/article_attachments/4416781712919) **Cancelar:** por meio deste botão, você cancela a edição de substituição realizada na grade.

**![Imagem 9: Mover para cima e Mover para baixo: permitem alterações na ordem de uso dos materiais alternativos (ordem crescente). A…](https://ajuda.sankhya.com.br/hc/article_attachments/4416786765335) Mover para cima e Mover para baixo:** permitem alterações na ordem de uso dos materiais alternativos (ordem crescente). A ordem de uso de materiais utilizada pelo sistema sempre será, primeiro a Matéria Prima (caso utilizada), em seguida os Materiais Alternativos seguindo a ordem definida na grade Materiais Alternativos no lançamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599094-Extrato-de-Materiais#top)
