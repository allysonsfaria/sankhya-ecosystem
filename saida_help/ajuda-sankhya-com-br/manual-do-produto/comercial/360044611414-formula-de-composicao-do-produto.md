---
id: "360044611414"
titulo: "Fórmula de Composição do Produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:25:58Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Custos", "Configuração", "Fórmulas", "COPITEMCOMPPRO", "Etapas", "Ciclo de Produção", "Fórmula de Composição do Produto", "Fórmula Principal", "Múltiplo Ideal", "Produção Mínima", "Produto Final", "Tamanho dos lotes", "br.com.sankhya.formula.composicao.produto", "Fórmula de Composição do Produto manual", "Controle", "Local", "Estoque", "Produção", "Produto Acabado", "Composição Produção Matéria Prima"]
---

# Fórmula de Composição do Produto

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311900519703) Módulo: Comercial > Arquivo > Cadastros
```

---

Esta tela permite que você configure os componentes a serem utilizados na fabricação de um determinado produto, sendo que, esta tela pertence ao Módulo de Produção/G.

O campo **"Produto"** compreende o Nome e o Código do produto final que será produzido.

A fórmula de composição e rotina de produção podem ser feitas utilizando os controles adicionais de estoque **"Local"** e **"Controle"**. Isso facilita a fabricação de produtos que têm uma grade diferenciada. Como por exemplo, camisetas (P, M, G), cores branca, azul e verde. Nesse caso, o campo **"Local"** poderá ser renomeado para Cor.

**Observação:** O campo Local só estará habilitado no modo de inserção, quando o parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** estiver habilitado. Este campo é obrigatório, pois não é possível modificá-lo após salvar.

O campo Controle é um componente especial que considera algumas preferências do produto. Ele só estará habilitado no modo de inserção após informar um produto e o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** estiver habilitado, este componente segue o padrão dos outros campos relacionados a controle do sistema (na tela [Cadastro de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba **"Estoque"**). Dependendo do produto, o tipo do componente será alterado conforme sua configuração de Controle Adicional de Estoque.

O campo **"Variação"** indicará quantas alterações existem para uma mesma fórmula. Temos como exemplo, a formulação de um bolo que utiliza como matéria prima a farinha de trigo. Uma possível variação desta fórmula, seria trocar a farinha de trigo por maizena. O sistema só permite uma fórmula para cada produto, com a mesma variação.

**Nota:** Ao duplicar um produto, teremos a opção de configurar o sistema para que a Fórmula de Composição do Produto seja ou não copiada para o novo produto que será gerado; esta definição é feita através do parâmetro **"Copiar item de composição do produto? -  COPITEMCOMPPRO"** que, por padrão, é apresentado ativado, ou seja, na duplicação a Fórmula de Composição do Produto é passada de um produto ao outro; para que este fato não ocorra, você deve desativar o referido parâmetro.

[Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#abageral)                                                                      [Aba Tamanho do lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#abatamanhodoslotes)

[Aba Etapas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#abaetapas)                                                                    [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#botooutrasopes)

## Aba Geral

![Forcom1](https://ajuda.sankhya.com.br/hc/article_attachments/360061940673)

O campo **"Ciclo de produção"** comporta o tempo a ser gasto para efetuar a produção, segundo a unidade indicada no campo abaixo.

Por meio do campo **"Unidade do Ciclo"**, informe se a unidade digitada no ciclo de produção será representada por segundos, minutos, horas, dias ou meses.

No campo **"Múltiplo Ideal"**, aponte a quantidade ideal para fabricação do produto a cada produção, o sistema somente permitirá produções com quantidades múltiplas deste valor.

**Observação:** Em uma produção, cuja fórmula tenha o valor do campo Múltiplo Ideal igual a -1, o sistema multiplica a quantidade que será produzida, pela **"Produção mínima"**. Isto somente ocorrerá nas inclusões.

A quantidade mínima a ser fabricada do produto, é indicada através do campo Produção Mínima. O sistema não aceitará uma produção com valor inferior ao informado neste campo.

O campo **"Fórmula principal"** indicará qual é a formulação base do produto, uma vez que o mesmo pode possuir muitas variações na sua fórmula de composição. Esta fórmula principal é utilizada para o cálculo dos custos na rotina de Cálculo de Custo pela Fórmula de Composição e no Planejamento e Controle da Produção.

**Nota:** O sistema bloqueia a marcação de duas variações como Fórmula principal, mas aceita a inexistência de pelo menos uma marcada como tal.

Através da marcação **"Ativo"**, você disponibiliza ou bloqueia a Fórmula de Composição do Produto para a produção, ou seja, caso esta marcação esteja desmarcado, ao tentar efetuar a inserção da fórmula na **"Produção"**, o sistema irá barrar essa inserção e comunicará que se trata de uma fórmula **"Inativa"**.

Os campos **"Desvio Sup. (%)"** e **"Desvio Inf. (%)"** estarão visíveis somente quando o opcional de WMS estiver na licença.

A marcação **"Considerar Menor Dt. Validade?"** quando acionada, ao confirmar a produção e esta der entrada no produto acabado, o sistema buscará a menor data de validade dentre as MPs e a informará no campo **"Data de Validade"** (DTVAL) da Tabela de Estoque (TGFEST), não mais considerando o prazo de validade do Cadastro de Produto.

Por meio da marcação **"Registrada no M.A.P.A?"**, você indica se a fórmula possui registro no Ministério da Agricultura, Pecuária e Abastecimento.

O campo **"Variação Relacionada"** relaciona uma fórmula de composição com outra pela variação.

No campo **"Estrutura de Produção"** temos a estrutura de produção associada ao produto. Uma estrutura só pode ser associada quando o produto for fórmula principal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Tamanho dos lotes

Esta aba tem a funcionalidade de comportar o tamanho do lote que será produzido, uma vez que determinados processos produtivos limitam o tamanho destes.

![Forcom2](https://ajuda.sankhya.com.br/hc/article_attachments/360061940693)

Ao executar uma produção, se as quantidades não baterem com a informada na grade, o sistema apresentará a seguinte mensagem:

**"Quantidade informada não tem correspondência com os tamanhos de lotes!".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#top)

## Aba Etapas

Nesta aba, temos a apresentação da grade superior Etapa do produto que possui detalhes da tela principal e define as etapas para a produção do produto, como também, a grade inferior Matéria prima, que define quais MP's o produto precisa para ser produzido.

![Forcom3](https://ajuda.sankhya.com.br/hc/article_attachments/360061940713)

O botão **"Visualizar resumo das Mps"** faz com que as estas duas grades sejam trocadas por outra aba que irá exibir o resumo de todas as matérias primas do produto.

![Forcom4](https://ajuda.sankhya.com.br/hc/article_attachments/360061940733)

**Inclusão de Etapas**

O campo **"Etapa"** definirá a fase pré-cadastrada na rotina [Etapas de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118913).

A ordem em que cada etapa ocorrerá dentro da fórmula será apontada no campo **"Sequência"**.

Por meio do campo **"Ciclo de Produção"**, você define o ciclo da etapa, o tempo gasto para sua execução.

O tipo de unidade do tempo gasto que foi informado no campo acima será indicada no campo **"Unidade do Ciclo de Produção"**.

A marcação **"Obrigatória"** definirá se a etapa é obrigatória ou opcional no processo de transferência entre etapas.

A opção **"Final"** definirá qual a etapa final do processo.

**Observação:** Para utilizar o controle de etapas no processo de produção, a fórmula de produção deverá ter, obrigatoriamente, uma etapa final, senão, no momento do fechamento da produção, será exibida a seguinte mensagem:

**"Não encontrou a etapa final do item".**

**Inclusão de Matérias Primas na Fórmula**

Por meio do campo **"Matéria Prima"**, você seleciona o produto desejado, que necessita estar pré–cadastrado na rotina [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Quando a fórmula possuir Etapas, as matérias primas deverão ser cadastradas por etapas. Abaixo trouxemos um exemplo:

- **Sequência – 1/etapa – 1/preparo da massa:** matérias primas, farinha, ovos, leite, margarina, mão de obra, etc.
- **Sequência – 2/etapa – 2/tempo de forno:** matérias primas, assadeiras, forno e mão de obra.

No campo Local, informe a localização da matéria prima.

O campo Controle é um componente especial que considera algumas preferências do produto e ele só estará habilitado no modo de inserção, após informar um produto e o parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"** estiver habilitado. Este componente segue o padrão dos outros campos relacionados à controle do sistema (aba de Estoque da tela de Cadastro de Produtos), dependendo do produto, o tipo do componente irá ser alterado conforme sua configuração de Controle Adicional de Estoque.

Os campos **"Qtd. Mistura"** e **"Unidade"** serão preenchidos com a quantidade gasta do produto informado, na composição do produto acabado.

O percentual aceitável para a variação na quantidade de matéria prima no decorrer da Produção será indicado através do campo **"Desvio Padrão"**. Como por exemplo, para fabricar um bolo, se gasta 1 copo de farinha de trigo, mas no momento da produção pode-se precisar de até ½ copo, a mais ou a menos, desta matéria prima. Neste caso, o desvio padrão seria de 50%.

O lançamento das matérias-primas poderá ser realizado pela **"Referência"** ou Código, conforme o parâmetro **"Código e/ou referência nos itens - CODPROREF"**. A referência da matéria-prima deve estar previamente cadastrada no Cadastro de Produtos.

O campo **"Sequencia"** permite que você informe a sequência em que as matérias-primas são utilizadas na produção do produto.

As informações relevantes a respeito da matéria prima devem ser apontadas no campo **"Observação"**.

Você poderá reservar matéria prima para produção através de um Tipo de Operação - TOP de Requisição que reserve matéria prima e da marcação do campo **"Atualiza Estoque"**. Isto facilitará a gestão de estoque de matéria primas para produção e, consequentemente, a reposição desta.

A marcação **"Quantidade Fixa"** quando acionada, indicará quais elementos da fórmula são fixos, ou seja, não sofrerão variação em função da quantidade produzida. Os processados somente uma vez, independente do tamanho do lote produzido. Na produção, a matéria-prima que for fixa não será multiplicada pela quantidade a ser produzida.

Por meio da marcação **"Ativo"**, você informa que a matéria prima está ativa na composição do Produto Acabado.

A marcação **"Opcional"** identifica a Matéria Prima como opcional na composição do Produto Acabado.

No lançamento da produção, as MP's que estejam marcadas como **"Terceiros"** terão seus estoques atualizados, levando em consideração a marcação **"Estoque com/de Terceiros"** contida na aba **"Estoque de Terceiros"** do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP). Estas MP's não serão somadas no custo do Produto Acabado.

Na tela de produção, estará disponível para digitar o código do parceiro se o campo **"Estoque com/de Terceiros"** for diferente de 'N'. Este parceiro será usado para atualizar os estoques de terceiros.

A marcação **"Manter quantidade"** permite aumentar a quantidade de produto acabado sem aumentar a quantidade de matérias primas. Quando marcada, ao fazer a atualização de quantidade de produto acabado, na tela de produção, o sistema não atualizará a quantidade das matérias primas que estiverem marcadas.

**Nota:** A marcação Manter quantidade é habilitada pelo parâmetro **"Manter quantidade de Matéria Prima quando alterar quantidade de Produto Acabado? - MPNAORECALC"**.

Os campos de percentuais de custo contidos nesta grade permitirão visualizar as colunas de custo e porcentagem de custo, possibilitando análises verticais dos custos de composição.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#top)

## Botão Outras Opções

O botão **"Outras Opções..."** é representado pelo ícone ![Forcom5](https://ajuda.sankhya.com.br/hc/article_attachments/360061021874) e está localizado na parte superior direita da tela. Por meio dele, temos acesso às seguintes opções:

**Visualizar Custos**

Esta opção exibe uma janela onde são apresentados os custos do produto.

![Forcom6](https://ajuda.sankhya.com.br/hc/article_attachments/360061940753)

**Propriedades**

Aqui, você configura o campo **"Empresa p/ calcular custos"** que define a empresa que o sistema irá calcular os custos.

![Forcom7](https://ajuda.sankhya.com.br/hc/article_attachments/360061021894)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611414-F%C3%B3rmula-de-Composi%C3%A7%C3%A3o-do-Produto#top)
