---
id: "360045118953"
titulo: "Planejamento de Produção e Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:55:10Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Planejamento", "Gerencial", "Planejamento de Produção e Compra", "br.com.sankhya.rotina.mgeprod.planejamentoproducao", "Planejamento de Produção e Compra manual", "Estoque", "Produção", "Algoritmos de cálculo e lead time", "Planejamento de produção e compras", "Filtros metas e cobertura de estoque"]
---

# Planejamento de Produção e Compra

| ``` ![Imagem 1: Módulo: Configurações > Cadastros > Gerencial](https://ajuda.sankhya.com.br/hc/article_attachments/42312795904023) Módulo:  Configurações > Cadastros > Gerencial ``` |
| --- |

---

Para prover o planejamento da produção, compras de matérias-primas e o acompanhamento destes, tendo como base previsões mensais de vendas e estoque mínimo em função do "lead time" do processo produtivo, o sistema conta com a tela Planejamento de Produção e Compras.

Essa tela contém apenas uma grade com os produtos selecionados, classificada inicialmente pelo código do produto. Nesta tela, tratamos apenas o processo do Planejamento de Produção e Compras. Em outras telas, serão tratadas a geração da produção e suas etapas.

O planejamento consiste na avaliação da situação atual de cada produto com informações relevantes para um possível início do processo produtivo que se iniciará com a compra dos insumos necessários.

É importante salientar que o planejamento de uma produção envolve todo o processo, desde a compra dos insumos até a entrada definitiva do PA (produto acabado) em estoque, sendo que, a geração efetiva da produção no ERP será efetuada manualmente no processo de acompanhamento acontecendo normalmente após a chegada de todos os insumos necessários para a produção.

**Nota:** para acessar o módulo Produção, é necessária uma licença específica, pois se trata de um opcional.

| [Configurações envolvidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#configura%C3%A7%C3%B5esenvolvidas) |  | [Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#Paineldefiltros) |
| --- | --- | --- |
| [Grade com os Planejamentos Calculados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#Gradecomosplanejamentoscalculados) |  | [Gerar Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#gerarplanejamento) |
| [Previsões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#previs%C3%B5es) |  | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#vendas) |
| [Acompanhamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#acompanhamento) |  | [Botão de Ação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#bot%C3%A3odea%C3%A7%C3%A3o) |
| [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#controledeacessos) |  |  |

---

## Configurações envolvidas

O parâmetro **"Consulta personalizada para quantidade em estoque -  QUERYESTQPLP"**, serve para configurar a query utilizada para a apuração do estoque atual da empresa. Para utilizar acesse a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834) e preencha com a query que será utilizada para a apuração.

Caso o parâmetro não seja preenchido, o sistema irá filtrar o estoque atual do produto na unidade padrão com "status lote aprovado" em qualquer local de estoque subtraindo a quantidade reservada.

O parâmetro **"Grupo de Produtos das embalagens - PCPGREMBAL"** refere-se à pesquisa de estoque personalizada do tipo texto, onde você poderá informar uma query para busca do estoque atual.

Na tela [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034), são criadas as etapas de produção.

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Planejamento de Produção e Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abaplanejamentodeproduoecompra), você deve configurar os campos:

- **Margem de segurança para PCP:** margem de Segurança para a tela de Planejamento de Produção e Compras que será utilizada no cálculo do campo **"Planejamento/Janela"**;
- **Meta Padrão para PCP:** meta padrão para a tela de Planejamento de Produção e Compras que, quando utilizada, permite a geração dos planejamentos pelo filtro **"Código da Meta (Simulação)"**.

Em [Metas Simplificadas de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117773) são criadas as metas mensais simplificadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Painel de Filtros

No Painel de Filtros, localizado no lado esquerdo da tela, você poderá realizar a filtragem de resultados por meio dos seguintes campos:

![Imagem 2: No Painel de Filtros , localizado no lado esquerdo da tela, você poderá realizar a filtragem de resultados por meio dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4416508354583)

Primeiro, informe para qual **"Empresa"** o planejamento está sendo efetuado.

Depois, busque pelo **"Grupo de Produtos"** para seleção dos produtos que aparecerão na tela. No caso de um grupo sintético, todos os produtos pertencentes a grupos abaixo na hierarquia deverão ser selecionados.

Em **"Filtro Genérico"** busque pelos dados do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Grade com os Planejamentos Calculados

Nesta tela são apresentadas as colunas abaixo com as seguintes informações:

![Imagem 3: Nesta tela são apresentadas as colunas abaixo com as seguintes informações:](https://ajuda.sankhya.com.br/hc/article_attachments/4416674500759)

**Produto**

Na grade Produto temos as colunas **"Código"**, **"Referência"**, **"Descrição"** e **"Unidade"** padrão do produto.

**Disponibilidade**

- **Estoque Atual:** estoque atual do produto. Estoque do Produto na unidade padrão com "status lote aprovado" em qualquer local de estoque subtraindo a quantidade reservada.  Se marcada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), a opção de pesquisa de estoque personalizada, utilizar query de busca configurada.
- **Em Produção:** quantidade do produto (Quantidade a ser produzida) já presente em planejamento de produção não concluído. Verifique se o lote de cada planejamento já não possui estoque com "status lote aprovado"; se existir, esta quantidade deve ser subtraída de quantidade planejada, pois esta já está presente no Estoque Atual.

**Previsão Corrente**

- **Quantidade:** quantidade prevista para o mês da **"Data atual"** de acordo com a Meta.
- **Dias Dif. Previsão:** apurar por meio das notas de venda (Notas confirmadas com TOP de venda) a quantidade que foi vendida (**"Venda"**) do produto até o dia imediatamente anterior à Data do Servidor. Com base na **"Previsão Corrente/Quantidade"**, calcular qual a quantidade deveria ter sido vendida até o dia imediatamente anterior à Data do Servidor ("Venda Prevista" = [Meta / Dias do Mês] \* "Dias até o dia Anterior").  Teremos então a fórmula final: Dias de Dif. de Previsão" = (["Venda" - "Venda Prevista"]/[Meta / Dias do Mês]).

Este resultado poderia automaticamente impactar nas coberturas calculadas em seguida, porém, isto não será feito visto que as causas destas diferenças podem variar de produto a produto.  Por exemplo, uma venda acima do previsto poderia ser causada tanto por uma demanda não prevista como por uma antecipação das vendas prevista no próprio mês. No caso de resultado positivo, o número obtido representa o equivalente em dias de venda da quantidade que foi vendida a mais do que o previsto, enquanto que o resultado negativo tem o mesmo significado porém, a menos do que previsto (será apresentado em **vermelho** quando negativo).  

Para Facilitar a análise, foi criado o botão **"Vendas"** que mostrará as vendas realizadas no período.

**Cobertura**

- **Estoque:** número de dias de estoque a partir do **"Estoque Atual"** levando em conta o consumo mensal definido na meta.

O algoritmo parte do Estoque Atual e mensalmente deduz as quantidades de acordo com a meta prevista para o mês até zerar o estoque, somando os dias do mês em totalizador. É considerado no mês da **"Data Atual"** o número de dias faltantes para o fim do mês (Quantidade = [Meta / Dias do Mês] \* Dias faltantes). Sendo que, é  considerado como faltante o dia da Data Atual.  

No mês em que o saldo não for suficiente para a atender a previsão é calculado o números de dias que a quantidade vai atender (Dias = Quantidade / [Meta / Dias do Mês]) e deve ser calculada a data de término deste para uso na coluna **"Cobertura/Fim de Estoque"** e também no cálculo da **"Cobertura/Janela"**.

- **Fim de Estoque:** data em que o estoque atual estará totalmente consumido de acordo com a previsão determinada na meta. Calculada no algoritmo da Cobertura/Estoque.
- **Produção:** número de dias de estoque das produções já planejadas e não concluídas, com base na quantidade planejada em cada uma delas. Da mesma forma que no campo **"Disponibilidades/Em Produção"** subtrair os estoques já existente para o lote.

O algoritmo é o mesmo da Cobertura/Estoque, utilizando como quantidade a quantidade planejada (subtrair os estoque já existentes para o lote) e no lugar da data atual, a data **"Cobertura/Fim de Estoque"**.

Em um processo recursivo, deverão ser processadas as produções planejadas de forma que a data inicial para a próxima iteração será a data final obtida na iteração anterior. A ordenação será de acordo com a data de  geração do planejamento.

Em cada uma das interações, deverá ser comparada data inicial do cálculo com a data prevista de entrada da produção planejada e, caso esta seja maior que a data inicial, acumular a diferença entre elas para uso na coluna **"Cobertura/Janela"**. A data prevista de produção planejada vai depender da etapa em que ela se encontra (Etapa), partindo-se da data de inicio da etapa e somando os lead times das etapas a partir dela. Por exemplo:

Se o planejamento se encontra na primeira, deve-se somar à data de inicio desta etapa os lead times das etapas seguintes, porém a etapa em andamento pode estar com atraso e este deverá ser somado para efeito do cálculo da data prevista (Atraso = "Data Atual" - ["Data de Inicio da Etapa" + "Lead Time da Etapa], considerando somente se for Positivo)".

A data de término, conforme previsto no algoritmo, será a última obtida e será utilizada na coluna **"Cobertura/Fim de Produção"**.

- **Fim de Produção:** data em que o estoque atual somado às produções já planejadas estará totalmente consumido de acordo com a previsão determinada na meta. Calculado no algoritmo da **"Cobertura/Produção"**.
- **Total:** número total de dias suprido pelo estoque atual e as produções já planejadas (**"Cobertura/Estoque"** + **"Cobertura/Produção"**).
- **Janela:** número de dias em que faltou estoque a partir da data atual e o fim de produção. Total calculado na rotina Cobertura/Produção).

**Planejamento**

- **Quantidade:** quantidade padrão de produção (Múltiplo Ideal da Fórmula principal do produto – TGFFCP.FORMPRINCIPAL = S de menor variação).
- **Lead Time:** número total de dias de todo o processo produtivo desde o pedido dos insumos até a entrada definitiva do PA em estoque. É a soma de todos os lead times de acordo com a estrutura de produção do produto. Sobre o Lead Time, é calculado o percentual cadastrado no campo **"Margem de Segurança"** das Preferências da Empresa e somado ao Lead Time.
- **Janela:** é a diferença do **"Lead Time"** e a **"Cobertura Total"**, quando esta diferença for positiva. Será exibida em branco se for negativa ou zero. Isto significa que o estoque atual, somado às produções já planejadas, não é suficiente para suprir o estoque mínimo necessário até que uma nova produção iniciada na data atual esteja disponível no estoque.
- **Tolerância:** idem do item anterior quando a diferença for negativa, mostrado em branco se positiva ou zero.
- **Início:** sugestão para início do planejamento. Data atual se existir Janela ou se a diferença apurada nos itens acima for 0. Se existir tolerância acrescentar a tolerância à Data Atual.
- **Fim:** é a data de término da produção se o planejamento for feito na Data indicada no campo Início. (Data de Planejamento/Início + dias do Planejamento/Lead Time).
- **Cobertura:** número de dias de estoque da nova produção com base na quantidade que deverá ser produzida (**"Planejamento/Quantidade"**).

O algoritmo é o mesmo da **"Cobertura/Estoque"**, utilizando como quantidade a quantidade que será produzida e acrescendo-se à data atual a **"Cobertura/Total"**.

Apresentar em vermelho quando for menor que o **"Planejamento/Lead Time"**, pois significa que a produção não vai ser suficiente para atender a demanda até uma próxima produção.

**Etapa**

- **Etapa:** campo do tipo texto, que será construído com base no campo Abreviação dos planejamentos pendentes do produto, de acordo com a etapa em que se encontram, separando cada planejamento com uma mudança de linha.

Texto: Lote 9999 - Etapa: XXXXXXXXXX - Obs: XX...XX, onde:

9999 = Número do Lote

XXX = Etapa do Planejamento

XX...XX = Observações do Planejamento

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Gerar Planejamento

Ao clicar no botão **"Planejamento"**, será gerado o planejamento de compras (visível na tela acompanhamento de Produção) e gerada a requisição de compra para todas as matérias-primas necessárias para a produção do produto (visível no portal de compras). Após a geração do Planejamento, o grid deverá ser reprocessado considerando o planejamento gerado.

**Nota:** quando o produto pertence a um  grupo de produção, o processo de geração de lotes será feito por grupo de produção e empresa, possibilitando gerar produção por grupo de produtos. Além disso, a estrutura de produção será obtida do preenchimento previamente efetuado do campo **"Estrutura de Produção"** informado na tela [Grupo de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611234).

Quando você clica em **"Gerar Planejamento"**, o sistema verifica se o produto está associado a um grupo de produção; caso esteja, trará todos os lotes do grupo que ainda não estejam com a primeira etapa concluída e dará a opção de você gerar o planejamento usando um lote existente ou gerar um novo lote. Não é permitido que você gere dois planejamentos para o mesmo produto no mesmo lote.

Caso não existam lotes, a tela não aparece e é gerado um novo lote para o grupo. Se o produto não pertencer a um grupo de produção, a tela não aparece e a numeração do lote é gerada a partir do produto. O que significa lote gerado a partir do produto ou do grupo? Será gerada uma sequencia de números exclusiva para o produto ou grupo.

**Planejamento:**

Sempre é gerado para o produto fórmula principal de menor variação. A Geração do Planejamento será feito baseado nas Etapas previstas na Estrutura de Produção.

Para cada Etapa, serão gerados um ou dois registros, o primeiro com CQL = 0 referente à um registro de produção ou registro que não gera produção.

Caso a etapa gere produção e tenha CQL, será gerado o segundo com CQL = 1 referente ao controle de qualidade da produção que será apontado pela aprovação do laudo de produção. Na geração, é gravada a data de geração na data de início da primeira etapa.

**Pedidos de Compra:**

Serão gerados pedidos de compra de todas as matérias-primas necessárias para a produção, de acordo com a fórmula principal do produto com o pedido modelo cadastrado na estrutura seguindo as regras:

A geração parte do produto principal e localiza as matérias-primas que não possuem fórmula, para que se faça o pedido destas.  No caso de matérias-primas que possuem fórmula (produtos intermediários), o processo é recursivo analisando as fórmulas destes.

Os produtos serão agrupados por seus fornecedores preferenciais. No caso de produtos com o campo zerado, utiliza o parceiro da nota modelo cadastrado na estrutura de produção.

A quantidade do pedido será a quantidade necessária para a produção independente do estoque atual. O Número da nota dos pedidos gerados (NUMNOTA) será o número do lote. Estes pedidos, na verdade, são requisições de compra que serão depois agrupados no ERP para geração do pedido efetivo de compra.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Previsões

Ao clicar neste botão, será aberto um pop-up mostrando em grade as Metas para o produto, de acordo com código da meta utilizada no planejamento a partir do mês da data do servidor.

Caso você tenha permissão de acesso para alteração na tela de lançamento de metas, é possível alterar as Metas neste pop-up, devendo, após seu fechamento, ser feito um recálculo na grade. Isto acontece mesmo quando estiver em simulação ou consulta porém, neste caso, não se pode alterar a meta cadastrada nas preferências da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Vendas

Ao clicar neste botão, será apresentado um pop-up mostrando em grade, as Vendas realizadas no mês, até o dia imediatamente anterior à data do servidor (Notas de Venda Confirmadas) exibindo as seguintes informações:

- Número da Nota
- Código do Parceiro
- Nome do Parceiro
- Quantidade Negociada
- Preço Unitário
- Desconto

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Acompanhamento

Ao clicar no botão **"Acompanhamento"**, será aberta a tela de **"Acompanhamento de Produção"**, tendo como filtro, a empresa da tela e o produto da linha selecionada.

Ao dar um duplo clique em um registro da grade, o sistema abre um pop-up para digitação da quantidade. Ao digitar a quantidade e confirmar, o sistema irá alterar a coluna **"Planejamento/Quantidade"** e recalcular o campo **"Planejamento/Cobertura"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Botão de Ação

Ao lado do botão Acompanhamento, temos um ![Imagem 4: Ao lado do botão Acompanhamento , temos um Botão de Ação , que é exibido apenas se uma ação for cadastrada na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16841490007703) Botão de Ação, que é exibido apenas se uma ação for cadastrada na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)

## Controle de Acessos

O controle de acesso permite configurar um usuário apenas para consulta e simulação ou com todos os acessos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#top)
