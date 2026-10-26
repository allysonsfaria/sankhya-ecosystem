---
id: "360045111693"
titulo: "Processo de Desmonte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:54:36Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Operações de Estoque", "Matéria-Prima", "Estoque", "Subprodutos", "Desmonte", "Ordens", "Reaproveitamento", "Processo de Desmonte manual", "Produção", "Desmonte: processo inverso à produção", "Reaproveitamento de matérias-primas e subprodutos", "Configurações para desmonte no sistema e ordens de produção"]
---

# Processo de Desmonte

Inicialmente, podemos definir o **"Desmonte"** como o ato de separar as partes que formavam um conjunto. Estendendo este conceito, no nosso caso, Desmonte é o processo contrário à produção normal, em que o Produto Acabado (PA) é decomposto em produtos reaproveitados e/ou subprodutos.

Trouxemos um exemplo:

Temos a fabricação de um Produto através do processo principal Shampoo Cabellu's - Caixa c/ 12 Unidades. Para a produção deste produto, foram utilizados os seguintes materiais: Envasado Shampoo Cabellu's, Caixa para 12 Unidades do produto, Fita e Etiqueta. Assim, ao realizar o processo de desmonte do produto Shampoo Cabellu's, devemos obter o seguinte resultado:

- **Shampoo Cabellu's - Caixa com 12 Unidades (Produto Acabado):** este item deverá sair do estoque, pois trata-se do Produto que está se processando o desmonte.
- **Envasado Shampoo Cabellu's (Matéria-Prima):** este produto deverá entrar em estoque, por ser uma Matéria-Prima utilizada na fabricação do produto principal.
- **Caixa c/ 12 Unidades do produto:** não será aproveitada, pois foi danificada e possui fita e etiqueta coladas; sendo assim, será encaminhada à reciclagem.
- **Fita (Matéria-Prima):** este material não será aproveitado, pois não será possível removê-lo da caixa sem danificá-lo.
- **Etiqueta (Matéria-Prima):** assim como o material anterior, este também não será aproveitado, pois não será possível removê-lo da caixa sem danificá-lo.
- **Caixa Shampoo reciclagem (Subproduto):** este item deverá entrar em estoque, caracterizado como um subproduto gerado pela Operação de Desmonte do Produto Acabado; assim, esta caixa não poderá ser aproveitada em outra Operação de Produção, porém, poderá ser comercializada para reciclagem.

Acesse os links abaixo para facilitar sua compreensão neste processo:

| [Configurando um Processo de Desmonte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#configurandoumprocessodedesmonte) |  | [Vínculo de Matérias-Primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#v%C3%ADnculodemat%C3%A9rias-primas) |
| --- | --- | --- |
| [Vínculo de Subprodutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#v%C3%ADnculodesubprodutos) |  | [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#opera%C3%A7%C3%B5esdeestoque) |
| [Lançamento de Ordem de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#lan%C3%A7amentodeordemdeprodu%C3%A7%C3%A3o) |  |  |

### Configurando um Processo de Desmonte

Na criação de um novo [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), é necessário que as Operações de Desmonte sejam representadas. Na tela Processo Produtivo, seção Tipo de processo, é necessário que a marcação **"Desmonte"** seja efetuada e informado no campo **"Processo de Produção Relacionado"**, o processo de fabricação a ele vinculado.

![Imagem 1: Na criação de um novo Processo Produtivo , é necessário que as Operações de Desmonte sejam representadas. Na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/4416303141271)

**Observação:** os processos de Desmonte deverão possuir a configuração de **"Tipo do Nro. Lote"** igual a **"Manual"**, para que, no momento do lançamento de uma Ordem de Produção relacionada a este lote, especifique-se qual o lote do produto que de fato está passando pela desmontagem. 

![Imagem 2: Observação: os processos de Desmonte deverão possuir a configuração de "Tipo do Nro. Lote" igual a "Manual" , para que,…](https://ajuda.sankhya.com.br/hc/article_attachments/4416293983639)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#top)

### Vínculo de Matérias Primas

Nas Operações de Produção, você deve configurar a lista de Matérias-Primas da mesma. Para este fim, na tela Processo Produtivo, dentro do botão ![Imagem 3: Nas Operações de Produção , você deve configurar a lista de Matérias-Primas da mesma. Para este fim, na tela Processo…](https://ajuda.sankhya.com.br/hc/article_attachments/16841729562263) [Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro), acessando uma [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades), aba [Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa), sub-aba [Lista de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistademps), utilize o campo **"Tipo de Uso do Material"**, onde você deve especificar a característica da Matéria-Prima que está sendo vinculada à operação. Temos as seguintes opções:

- **Reaproveitamento em Desmonte:** através desta opção, definimos que a Matéria-Prima vinculada à operação/produto será reaproveitada na execução do processo, ou seja, será dada entrada no estoque deste produto.
- **Usada na Operação Normal:** por esta opção, determinamos que a Matéria-Prima vinculada à operação/produto será utilizada no processo, ou seja, o estoque deste produto será baixado (em alguns Processos de Desmonte, é necessário o consumo de outras Matérias-Primas para se chegar ao resultado esperado).
- **Usada em Ajustes:** esta opção impacta em Processos de Desmonte quando a atividade estiver sendo executada pela segunda vez (reprocesso).

**Importante:** não implementada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#top)

### Vínculo de Subprodutos

Você deve também, configurar a lista de subprodutos que serão gerados a partir do Processo de Desmonte do produto, ou seja, os produtos gerados a partir do Desmonte. Em muitos casos, são aquelas Matérias-Primas que por algum motivo não foram possíveis de se aproveitar. Trouxemos um exemplo:

No Processo de Produção normal, é consumida a Matéria-Prima **"Caixa de Papelão"** para se embalar o Produto. No Processo de Desmonte, o produto é retirado dessa embalagem e agora o produto Caixa de Papelão está danificado, pois foi rasgada ou possui fita e etiquetas já coladas. Como consequência, não pode utilizar esta Caixa de Papelão novamente na fabricação de outro produto, porém, podemos vendê-la como **"Papelão"** para reciclagem.

Desta forma, você deve realizar a configuração da lista de subprodutos que serão gerados no processo, lembrando de informar o local de estoque das movimentações que existirem para o mesmo. Assim, esta configuração é realizada na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), botão [Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro), [Configuração de Atividades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades), aba [Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa), sub-aba [Lista de Subprodutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistadesubprodutos).

**Importante:** não implementada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#top)

### Operações de Estoque

Para os Processos de Desmonte, temos as seguintes Operações de Produção:

- **Nota de Produção Inversa:** esta Operação de Estoque refere-se à uma nota de produção cuja [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada realizará o procedimento inverso de atualização de estoque, ou seja, baixa-se estoque de Produto Acabado e é dada entrada no estoque de Matérias-Primas.
- **Movimentação do Subproduto:** já esta Operação de Estoque, diz respeito à movimentação de estoque dos subprodutos apontados que estão entrando no estoque. Para isto, configure uma operação que utilize uma TOP que atualize estoque de Matérias-Primas.

![Imagem 4: Movimentação do Subproduto: já esta Operação de Estoque , diz respeito à movimentação de estoque dos subprodutos…](https://ajuda.sankhya.com.br/hc/article_attachments/4416508377367)

A TOP de Produção para o Processo de Desmonte realizará o procedimento inverso de atualização de estoque (como mencionado acima) porém, os campos de locais para atualização dos mesmos permanecem inalterados, ou seja:

- **Local de Origem:** é o local onde buscamos o Produto Acabado.
- **Local para baixa de MPs:** trata-se do local de onde serão efetuadas as baixas dos materiais de consumo quando for o caso, ou então será dada a entrada dos materiais reaproveitáveis.

**Observação:** na tela Processo Produtivo, no botão Roteiro, acessando uma Configuração de Atividade, aba Produtos (PA), sub-aba Lista de Subprodutos, temos o campo **"Cód. Local"**, onde informamos o local que será dada entrada dos subprodutos gerados na operação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#top)

### Lançamento de Ordem de Produção

Ao lançar uma Ordem de Produção referente a um Processo de Desmonte, é necessário definir que essas ordens geradas correspondem a tal operação. Para isto, ao clicar no botão ![Imagem 5: Ao lançar uma Ordem de Produção referente a um Processo de Desmonte , é necessário definir que essas ordens geradas…](https://ajuda.sankhya.com.br/hc/article_attachments/16841729564823) **"Nova OP"** será aberto um pop-up, onde você deve selecionar no campo **"Tipo de Ordem"**, a opção **"Desmonte"**, para que o sistema possa considerar todos os Processos Produtivos correspondentes ao desmonte.

**Observação:** é importante especificar o número de lote do produto que se deseja realizar o processo de desmonte.

![Imagem 6: Nota: no lançamento de um Ordem de Produção referente à um Processo de Desmonte , caso a rotina não encontre notas de…](https://ajuda.sankhya.com.br/hc/article_attachments/4416288395031)**Nota:** no lançamento de um Ordem de Produção referente à um Processo de Desmonte, caso a rotina não encontre notas de produção para o produto e lote informados na ordem, teremos o parâmetro **"OP de Desmonte s/ nota de Produção - OPDESMONTESNOTA"** (por padrão é apresentado desligado) que, ao ser ativado, fará com que o sistema busque na tabela TGFEST se existe estoque para o produto, lote e empresa da planta de manufatura.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111693-Processo-de-Desmonte#top)
