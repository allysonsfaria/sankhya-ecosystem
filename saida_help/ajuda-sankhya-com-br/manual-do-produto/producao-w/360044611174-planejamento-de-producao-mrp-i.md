---
id: "360044611174"
titulo: "Planejamento de Produção (MRP I)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-10-21T19:05:21Z"
rotulos: ["manual", "Configuração", "Planejamento", "Planejamento de Produção (MRP I)", "br.com.sankhya.producao.rotina.controledeproducao", "Planejamento de Produção (MRP I) manual", "Análise de Giro", "Estoque", "Produção", "MAXROWEXECQUERY", "Configuração do MPS e demanda", "MRP para gestão de estoque", "Filtros de demanda e cálculos de produção", "MRP", "MPS"]
---

# Planejamento de Produção (MRP I)

```
 Módulo: Produção > Rotinas
```

---

A gestão do estoque de uma empresa deve ser uma tarefa alinhada com todas as áreas do negócio, da produção à venda. Caso contrário, podem ser gerados atrasos e demora na entrega de produtos. Em tempos nos quais os consumidores têm acesso a inúmeras opções de produtos e serviços, construir uma reputação de atraso na entrega pode ser devastador para a empresa.

Para prevenir este tipo de problema e otimizar a gestão do estoque, muitas empresas adotam o MRP. Do inglês, MRP significa "Manufacturing Resource Planning", ou Planejamento das Necessidades Materiais.

O MRP é um sistema de cálculo dos materiais necessários para produção dos Produtos Acabados (PA's) de um determinado MPS**\***. O MRP realiza a explosão de materiais considerando a BOM**\*\*** para cada um dos itens do MPS e apresenta as necessidades de compra conforme estado atual do estoque (estoque atual e pedidos de compra).

**\*MPS - Master Production Schedule** ou **Plano Mestre de Produção:** É um registro/documento que apresenta quais produtos devem ser produzidos assim como suas respectivas necessidades, em determinado período.

**\*\*BOM - Bill Of Materials** ou **Estrutura de Produtos:** O BOM é a lista de materiais brutos, pré-montados, subcomponentes, componentes ou partes, e a quantidade necessária de cada um para fabricar um produto por completo.

Para que a rotina de Planejamento de Produção (MRP I) tenha um funcionamento adequado, é necessário a configuração do MPS; Esta configuração será utilizada pela rotina no cálculo de demanda do MPS assim como base para o cálculo do MRP.

![Imagem 1: O sistema não leva em conta campos adicionais no cálculo do Planejamento de Produção .](https://ajuda.sankhya.com.br/hc/article_attachments/16841108041623) O sistema não leva em conta campos adicionais no cálculo do Planejamento de Produção.

| [Configurando o MPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#configurandoomps) |  | [Aba Demanda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademanda) |
| --- | --- | --- |
| [Aba Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abaprodutos) |  | [Aba Filtros de Estoque (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#filtrosdeestoque(pa)) |
| [**Aba Filtros de Estoque (MP)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#filtrosdeestoque(mp)) |  | [Aba MRP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#mps-abamrp) |
| [Plano Mestre de Produção | Novo Plano](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#planomestredeproduonovoplano) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#h_01G3YBZ8G9083FNV4RH1JMYN95) |
| [Aba Plano Mestre de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abaplanomestredeproduo) |  | [Aba Plano Mestre de Produção - Botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abaplanomestredeproduo-botes) |
| [Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#botesdotopodatela) |  |  |

## Configurando o MPS

Para configurar o MPS clique no botão ![Imagem 2: Para configurar o MPS clique no botão "Configuração" localizado no alto da tela. Assim, a visão desta tela será…](https://ajuda.sankhya.com.br/hc/article_attachments/16841108047895) **"Configuração"** localizado no alto da tela. Assim, a visão desta tela será alterada para uma grade onde serão apresentadas todas as configurações já existentes. Diversas configurações de MPS podem ser utilizadas em momentos diferentes de acordo com a necessidade da empresa (um exemplo são indústrias onde alguns produtos são planejados com base em metas comerciais de vendas e outros por projeção de giro).

Clique no botão de inclusão para criar uma nova configuração; considere que esta deve possuir uma descrição de fácil identificação.

O sistema irá dispor também os botões ![Imagem 3: O sistema irá dispor também os botões "Cancelar" , "Anterior" , "Próximo" e "Concluir" , onde você poderá avançar entre…](https://ajuda.sankhya.com.br/hc/article_attachments/16841108051351) **"Cancelar"**, ![Imagem 4: O sistema irá dispor também os botões "Cancelar" , "Anterior" , "Próximo" e "Concluir" , onde você poderá avançar entre…](https://ajuda.sankhya.com.br/hc/article_attachments/6935890989463) **"Anterior"**, ![Imagem 5: O sistema irá dispor também os botões "Cancelar" , "Anterior" , "Próximo" e "Concluir" , onde você poderá avançar entre…](https://ajuda.sankhya.com.br/hc/article_attachments/6935961970583) **"Próximo"** e ![Imagem 6: O sistema irá dispor também os botões "Cancelar" , "Anterior" , "Próximo" e "Concluir" , onde você poderá avançar entre…](https://ajuda.sankhya.com.br/hc/article_attachments/6935964414743) **"Concluir"**, onde você poderá avançar entre as etapas ao realizar as configurações. Lembre-se ainda que, o botão Concluir será exibido apenas na última etapa. 

O detalhamento da Configuração de um MPS, pode ser visualizado nos tópicos que seguem. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Demanda

Na aba Demanda você define inicialmente, qual o tipo de demanda o MPS irá considerar para gerar a necessidade de produção para os produtos. O campo **"Tipo Demanda"**, que pode ser definido dentre as opções Projeção de Giro, Pedidos Firmes, Metas e Personalizada, habilita logo abaixo, diferentes opções referentes a cada uma das configurações em questão. Observe:

| [Projeção de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademandasub-abaprojeodegiro) |  | [Pedidos Firmes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademandasub-abapedidosfirmes) |  | [Metas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademandasub-abametas) |  | [Personalizada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademandasub-abapersonalizada) |
| --- | --- | --- | --- | --- | --- | --- |

## Projeção de Giro

Uma vez o campo Tipo Demanda configurado como Projeção de Giro (aba Demanda), tem-se a liberação dos campos para configuração desta.

Além dos filtros que serão demonstrados mais abaixo, os documentos (pedidos/notas) que serão considerados pela rotina são aqueles que atualizam o giro (campo **"Análise de Giro"** do Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)).

![Imagem 7: Além dos filtros que serão demonstrados mais abaixo, os documentos (pedidos/notas) que serão considerados pela rotina…](https://ajuda.sankhya.com.br/hc/article_attachments/6933184578327)

**Estoque Mínimo:** este campo define como o MPS irá considerar o estoque mínimo dos Produtos Acabados nos cálculos. Temos as seguintes opções:

- **Ignora Estoque Mínimo:** não será considerado estoque mínimo no resultado da necessidade de produção;
- **Até Atingir o Estoque Mínimo:** por meio desta opção, será adicionada a quantidade necessária para se chegar ao estoque mínimo (quando maior que zero) ao resultado da necessidade de produção calculada;
- **Adicionar a Qtd de Estoque Mínimo:** será acrescentada a quantidade do estoque mínimo ao resultado da necessidade de produção.

**Tamanho:** é preciso definir o tamanho dos períodos considerados no cálculo de giro. As opções disponíveis são:

- Semana;
- Quinzena;
- Mês;
- Bimestre;
- Trimestre;
- Quadrimestre;
- Semestre;
- Ano;
- Livre.

**Exibir Produtos Intermediários:** nesse campo, defina a exibição dos produtos intermediários no MPS. Esse é apenas um filtro de registros da tela.

- **Nunca:** nessa opção, nunca serão apresentados Produtos Intermediários (PI's) na grade de itens, mesmo estando presentes no MPS;
- **Sempre:** sempre serão apresentados PI's na grade itens, mesmo se não existir demanda direta (pedidos de venda, meta, giro etc) para o PI em questão;
- **Apenas c/ demanda direta:** será apresentado o PI na grade de itens apenas quando existir demanda direta para o PI (pedidos de venda, meta, giro, etc).

**Tamanho de Lote da OP igual ao Lote Padrão:** com essa marcação acionada, a quebra do tamanho do lote da Ordem de Produção será equivalente ao Tamanho do Lote Padrão, conforme as condições abaixo:

- É necessário possuir as licenças **"5332 - Indústria - Pack 3 / Programação de O.P.”** e **“5331 - Industria - Pack 2 / Planejamento MRP I"**;
- A configuração da marcação Tamanho de Lote da OP igual ao Lote Padrão só é aplicada no lançamento de OPs pela **"Programação Plano Mestre de Produção"**, isto é, não é utilizada em lançamento manual;
- Essa configuração não trabalha em conjunto com as marcações **"Detalhar itens agrupando pela previsão de entrega"** e/ou **"Detalhar itens por pedido ativas"**;
- Essa marcação não funciona quando as sub-ordens dos PIs não se agrupam (opções **"Sempre iniciar uma nova"** e **"Sempre usar uma em aberto"**, localizadas na tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top), aba [Matérias-primas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#abamat%C3%A9rias-primas), botão **"Outras Opções"**, opção **"Configurações do PI"**, campo **"Tipo de sub-ordem"**.

**Importante:** ao utilizar essa configuração, é necessário se atentar ao **"Tamanho de Lote Padrão"** configurado para os produtos na tela [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto#top). Sendo que, o Tamanho de Lote Padrão não pode ser pequeno para grandes volumes produzidos, pois para esses casos quanto menor o tamanho de lote, maior o número de OPs gerados, o que pode comprometer o processamento da rotina.

**Tipo de Período:** no cálculo de demanda baseada em projeção de giro, o MPS trabalha com pedidos/notas que atualizaram estoque. Sendo assim, neste campo deve ser definida qual data utilizar, ou seja, data de Negociação ou de Movimento do documento em questão.

**Qtd. Período:** a projeção de giro pode considerar vários períodos e o resultado final será uma média simples do valor obtido de cada período. Então nesse campo deve ser inserida a quantidade de períodos que serão considerados.

**Qtd. Dias:** quando o campo Tamanho do período for definido como Livre, tem-se a possibilidade de informar a quantidade de dias nesse campo.

**Retroagir Mesmo Período em Anos Anteriores:** ao efetuar esta marcação, os períodos montados para o cálculo irão corresponder à anos anteriores. 

```
                                                                          Exemplo 1:
```

Qtd. Período = 2

Tamanho = Mês

Retroagir Mesmo Período em Anos Anteriores = Sim

Período do Planejamento = 01/06/2018 à 30/06/2018

Períodos giro:

P1 = 01/06/2017 à 30/06/2017 = 500 UN

P2 = 01/06/2016 à 30/06/2016 = 400 UN

O giro considerado no cálculo de demanda do produto será 500 + 400 / 2 = 450 UN.

```
                                   Exemplo 2:
```

Qtd. Período = 2

Tamanho = Mês

Retroagir Mesmo Período em Anos Anteriores = Não

Período do Planejamento = 01/06/2018 à 30/06/2018

Períodos giro:

P1 = 01/04/2018 à 30/04/2018 = 700 UN

P2 = 01/05/2018 à 31/05/2018 = 500 UN

O giro do considerado no cálculo de demanda do produto será 700 + 500 / 2 = 600.

**Nota:** o parâmetro **" Incluir TOPs de Produção no calculador de giro MPS - INCPRODGIROMPS"** permite a inclusão de movimentos gerados por TOPs de produção (F - Produção) do calculador de demanda por giro do MPS.

**Filtro de Empresas:** A demanda dos produtos do plano mestre de produção serão apresentadas de acordo com as empresas selecionadas neste filtro. A saber:

- Se você marcar todas as empresas do filtro, na aba [Plano mestre de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-#abaplanomestredeproduo), serão exibidos todos os produtos de todas as empresas cadastradas, conforme o tipo de demanda gerada para a **"Planta de Manufatura"** cadastrada no MPS.
- Caso você selecione apenas algumas empresas do filtro, serão apresentadas na aba Plano mestre de Produção, somente os produtos da(s) empresa(s) selecionada(s).
- Se não for marcada nenhuma empresa, na aba Plano mestre de Produção, serão apresentados os produtos de todas as empresas cadastradas, conforme tipo de demanda gerada para a Planta de Manufatura, cadastrada no MPS.

Ainda sobre considerar a projeção de giro, caso o produto não retorne giro para o período em questão, no MPS é possível buscar em metas. Observe:

#### Seção Metas

**Utilizar Meta Simplificada de Produtos:** ao realizar esta marcação, se o produto em questão não retornar giro, será considerada a [Meta Simplificada de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117773) do mesmo (apenas metas simplificadas para Produtos do tipo Quantidade). Caso não seja feita a opção por utilizar meta simplificada, pode-se então utilizar Metas Comerciais (Controle Orçamentário e Metas).

Se você não assinalar a marcação Utilizar Meta Simplificada de Produtos, serão habilitados os seguintes filtros:

**Filtro de Metas:** o campo permite filtrar as configurações de metas existentes e que serão consideradas no cálculo de demanda.

**Filtro Personalizado (Configurações de Metas):** você pode elaborar um filtro personalizado partindo da configuração de metas que serão consideradas no cálculo de demanda.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademanda)

## Pedidos Firmes

Uma vez que o campo Tipo Demanda foi configurado como Pedidos Firmes (aba Demanda), teremos a exibição dos campos para configuração. Neles, serão configuradas as regras para a obtenção dos pedidos que serão considerados no cálculo de demanda do MPS.

Além dos filtros que serão descritos mais abaixo, os pedidos que serão considerados neste ponto da rotina são aqueles Confirmados , Pendentes e cujo [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado em seu lançamento possua marcada a opção **"Gerar demanda para MPS"** (aba [Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaproduo)).

![Imagem 8: Além dos filtros que serão descritos mais abaixo, os pedidos que serão considerados neste ponto da rotina são aqueles…](https://ajuda.sankhya.com.br/hc/article_attachments/6933142017687)

**Estoque Mínimo:** aqui, será definido como o MPS irá considerar o estoque mínimo dos Produtos Acabados nos cálculos. Este terá as opções:

- **Ignora Estoque Mínimo:** não será considerado estoque mínimo no resultado da necessidade de produção;
- **Até Atingir o Estoque Mínimo:** por meio desta opção, será adicionada a quantidade necessária para se chegar ao estoque mínimo (quando maior que zero) ao resultado da necessidade de produção calculada;
- **Adicionar a Qtd de Estoque Mínimo:** será acrescentada a quantidade do estoque mínimo ao resultado da necessidade de produção.

**Exibir Produtos Intermediários:** nesse campo, defina a exibição dos produtos intermediários no MPS. Esse é apenas um filtro de registros da tela.

- **Nunca:** nessa opção, nunca serão apresentados Produtos Intermediários (PI's) na grade de itens, mesmo estando presentes no MPS;
- **Sempre:** sempre serão apresentados PI's na grade itens, mesmo se não existir demanda direta (pedidos de venda, meta, giro etc) para o PI em questão;
- **Apenas c/ demanda direta:** será apresentado o PI na grade de itens apenas quando existir demanda direta para o PI (pedidos de venda, meta, giro, etc).

**Tipo de Período:** como essa configuração faz o sistema considerar pedidos, então o MPS terá um período para pedidos que será definido por você, assim como o período de planejamento. Por meio deste campo, determine a data dos documentos dentro desse período a serem considerados:

- **Negociação:** serão considerados todos os pedidos cuja data de negociação esteja dentro do período de pedidos do MPS;
- **Previsão de Entrega (Nota):** serão considerados todos os pedidos cuja Previsão de Entrega (cabeçalho do documento) esteja dentro do período de pedidos do MPS;
- **Previsão de Entrega (Itens):** serão considerados todos os pedidos em que a Previsão de Entrega esteja dentro do período de pedidos do MPS. Essa previsão é por item e quantidade, com isso, pode ser que a quantidade total de um determinado produto não seja considerada no cálculo;
- **Movimento:** serão considerados todos os pedidos cuja Data do Movimento esteja dentro do período de pedidos do MPS.

**Filtro Personalizado (Itens Pedido):** através deste campo, você pode criar um filtro personalizado partindo dos itens de um pedido que deve ser considerado no cálculo de demanda.

**Filtro de Empresas:** a demanda dos produtos do plano mestre de produção serão apresentadas de acordo com as empresas selecionadas neste filtro. A saber:

- Se você marcar todas as empresas do filtro, na aba [Plano mestre de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-#abaplanomestredeproduo), serão exibidos todos os produtos de todas as empresas cadastradas, conforme o tipo de demanda gerada para a **"Planta de Manufatura"** cadastrada no MPS.
- Caso você selecione apenas algumas empresas do filtro, serão apresentadas na aba Plano mestre de Produção, somente os produtos da(s) empresa(s) selecionada(s).
- Se não for marcada nenhuma empresa, na aba Plano mestre de Produção, serão apresentados os produtos de todas as empresas cadastradas, conforme tipo de demanda gerada para a Planta de Manufatura, cadastrada no MPS.

**Detalhar itens agrupando pela previsão de entrega:** com esta marcação acionada, os itens do MPS exibirão a previsão de entrega baseada nos pedidos de venda. Sendo que, está marcação só será apresentada se o campo **"Tipo de Período"** estiver configurado com a opção **"Previsão de Entrega (Nota)"** ou **"Previsão de Entrega (Itens)"**.

**Observação:** a coluna **"Ponto de Pedido"** irá exibir a data sugerida para a compra de MP considerando o primeiro dia do planejamento quando o campo Tipo de Demanda for definido com a opção Pedidos Firmes ou Metas quando os campos [Tempo de Atravessamento (min)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abaplanomestredeproduo) e **"Lead Time de Compra"** da aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) forem preenchidos.

Além disso, ao sugerir a data da compra de MP, o valor a ser considerado no campo Lead Time de Compra ocorrerá da seguinte maneira:

![Imagem 9: Caso o campo Lead Time de Compra da sub-aba "Geral" da aba Imposto / Informações por empresa do Cadastro de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/21130850420119) Caso o campo Lead Time de Compra da sub-aba **"Geral"** da aba Imposto / Informações por empresa do Cadastro de Produtos não tenha sido configurado;
![Imagem 10: Caso o campo Lead Time de Compra da sub-aba "Geral" da aba Imposto / Informações por empresa do Cadastro de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/21130850431127) O sistema irá procurar por essa configuração no campo Lead Time de Compra na sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque) da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) também do Cadastro de Produtos.

Sabendo disso, o cálculo será realizado da seguinte maneira:

```
 (Primeiro dia do planejamento) - (tempo de processamento de produção) - (Lead
      time de compra da MPS)
```

Assim, teremos, por exemplo:

= (01/01/24) - (5760 min = 4 dias) - (5 dias)

= 23/12/23

Lembre-se ainda que, a carga horária não será considerada para realizar o cálculo, somente os dias corridos no Tempo de Atravessamento (min) e Lead Time de Compra.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademanda)

## Metas

Nos casos em que o campo Tipo Demanda for configurado como Metas (aba Demanda), tem-se a liberação dos campos para configuração. Configure aqui, a regra para a obtenção das metas a serem consideradas no cálculo de demanda do MPS.

![Imagem 11: Nos casos em que o campo Tipo Demanda for configurado como Metas (aba Demanda ), tem-se a liberação dos campos para…](https://ajuda.sankhya.com.br/hc/article_attachments/6933241944983)

**Estoque Mínimo:** aqui, será definido como o MPS irá considerar o estoque mínimo dos Produtos Acabados nos cálculos. Este terá as opções:

- **Ignora Estoque Mínimo:** não será considerado estoque mínimo no resultado da necessidade de produção;
- **Até Atingir o Estoque Mínimo:** por meio desta opção, será adicionada a quantidade necessária para se chegar ao estoque mínimo (quando maior que zero) ao resultado da necessidade de produção calculada;
- **Adicionar a Qtd de Estoque Mínimo:** será acrescentada a quantidade do estoque mínimo ao resultado da necessidade de produção.

**Exibir Produtos Intermediários:** nesse campo, defina a exibição dos produtos intermediários no MPS. Esse é apenas um filtro de registros da tela.

- **Nunca:** nessa opção, nunca serão apresentados Produtos Intermediários (PI's) na grade de itens, mesmo estando presentes no MPS;
- **Sempre:** sempre serão apresentados PI's na grade itens, mesmo se não existir demanda direta (pedidos de venda, meta, giro etc) para o PI em questão;
- **Apenas c/ demanda direta:** será apresentado o PI na grade de itens apenas quando existir demanda direta para o PI (pedidos de venda, meta, giro, etc).

**Tamanho de Lote da OP igual ao Lote Padrão:** com essa marcação assinalada, o tamanho do lote da Ordem de Produção será equivalente ao tamanho do Lote Padrão. Lembre-se ainda que, essa configuração só é utilizada na rotina de lançamento de ordens de produção pela **"Programação Plano Mestre de Produção"**, não é utilizada pelo lançamento manual.

**Utilizar Meta Simplificada de Produtos:** ao realizar esta marcação, se o produto em questão não retornar giro, será considerada a Meta Simplificada de Venda do mesmo (apenas metas simplificadas para Produtos do tipo Quantidade). Caso não seja feita a opção por utilizar meta simplificada, pode-se então utilizar Metas Comerciais (Controle Orçamentário e Metas).

Se não for realizada a marcação Utilizar Meta Simplificada de Produtos, serão habilitados os seguintes filtros:

**Filtro de Metas:** o campo permite filtrar as configurações de metas existentes e que serão consideradas no cálculo de demanda.

**Filtro Personalizado (Configurações de Metas):** você pode elaborar um filtro personalizado partindo da configuração de metas que serão consideradas no cálculo de demanda.

Para ambos os casos de metas (Meta Simplificada e Metas do módulo de Controle Orçamentário e Metas) o período é fechado, mensal, por exemplo. Como o período do planejamento é livre, é feito o cálculo proporcional à meta para o período do planejamento. Assim a quantidade calculada para o produto poderá ser afetada por metas de diversos meses, caso o planejamento contenha dias de mais de um mês.

#### Exemplo:

Se o período do planejamento for 31/08/2018 a 05/09/2018, serão consideradas as metas de agosto e setembro, em suas devidas proporções: 1º dia da meta de agosto (1/31 da meta) + 5 dias da meta de setembro (5/30 da meta).

**Observação:** a coluna **"Ponto de Pedido"** irá exibir a data sugerida para a compra de MP considerando o primeiro dia do planejamento quando o campo Tipo de Demanda for definido com a opção Pedidos Firmes ou Metas quando os campos [Tempo de Atravessamento (min)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abaplanomestredeproduo) e **"Lead Time de Compra"** da aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) forem preenchidos.

Além disso, ao sugerir a data da compra de MP, o valor a ser considerado no campo Lead Time de Compra ocorrerá da seguinte maneira:

![Imagem 12: Caso o campo Lead Time de Compra da sub-aba "Geral" da aba Imposto / Informações por empresa do Cadastro de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/21130850420119) Caso o campo Lead Time de Compra da sub-aba **"Geral"** da aba Imposto / Informações por empresa do Cadastro de Produtos não tenha sido configurado;
![Imagem 13: Caso o campo Lead Time de Compra da sub-aba "Geral" da aba Imposto / Informações por empresa do Cadastro de Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/21130850431127) O sistema irá procurar por essa configuração no campo Lead Time de Compra na sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque) da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) também do Cadastro de Produtos.

Sabendo disso, o cálculo será realizado da seguinte maneira:

```
 (Primeiro dia do planejamento) - (tempo de processamento de produção) - (Lead
      time de compra da MPS)
```

Assim, teremos, por exemplo:

= (01/01/24) - (5760 min = 4 dias) - (5 dias)

= 23/12/23

Lembre-se ainda que, a carga horária não será considerada para realizar o cálculo, somente os dias corridos no Tempo de Atravessamento (min) e Lead Time de Compra.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademanda)

## Personalizada

Ao configurar o campo Tipo Demanda com a opção Personalizada (aba Demanda), ocorrerá a liberação desta aba para configuração. Aqui, será definida uma rotina (Stored Procedure) que permite personalizar a demanda bruta para todos os itens de um determinado MPS.

![Imagem 14: Ao configurar o campo Tipo Demanda com a opção Personalizada (aba Demanda ), ocorrerá a liberação desta aba para…](https://ajuda.sankhya.com.br/hc/article_attachments/6933304277783)

Para tanto, é necessário informar o **"Nome da rotina"** e acionar o botão ![Imagem 15: Para tanto, é necessário informar o "Nome da rotina" e acionar o botão "Criar template da rotina" , feito isso, um…](https://ajuda.sankhya.com.br/hc/article_attachments/16841116081559) **"Criar template da rotina"**, feito isso, um template da rotina será criado no banco de dados. Esse template revelará como deve ser o esqueleto da rotina, ou seja, quais são os parâmetros necessários (de entrada e saída). Em contrapartida, o botão ![Imagem 16: Para tanto, é necessário informar o "Nome da rotina" e acionar o botão "Criar template da rotina" , feito isso, um…](https://ajuda.sankhya.com.br/hc/article_attachments/16841116083991) **"Remover template da rotina"** possibilita remover a rotina criada do banco de dados.

**Nota:** uma vez que a rotina foi inserida no banco de dados, para que seja possível alterar o nome da rotina, é necessário que esta seja primeiramente removida.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#abademanda) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Produtos

Nessa aba é possível restringir os produtos que serão considerados no MPS que utilizarem essa configuração.

![Imagem 17: Nessa aba é possível restringir os produtos que serão considerados no MPS que utilizarem essa configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/6933670616471)

**Exibir Apenas PAs c/ Demanda:** efetuando essa marcação, no MPS serão apresentados apenas os Produtos PAs com necessidade de produção (demanda) e, ao executar MRP, serão apresentadas apenas as matérias-primas desses Produtos PAs; Ao gerar OP pelo MPS, apenas serão apresentados esses Produtos PAs para lançamento de OP.

**Planejamento por Controle:** quando marcado, significa que o cálculo de demanda do MPS irá considerar o controle do produto (controle adicional do tipo lista). Dessa forma, será gerado um registro de necessidade de produção para cada produto/controle. Essa configuração faz sentido apenas para produtos com controle adicional do tipo Lista.

**Classificação:** por meio deste campo, você pode restringir o MPS aos produtos pertencentes a classificação em questão (classificadores de produtos). Caso uma classificação pai seja selecionada, então todos os produtos também vinculados às classificações filhas serão considerados.

**Filtro de Marcas:** a partir desse filtro é possível restringir o MPS apenas aos produtos pertencentes às marcas selecionadas.

**Filtro Personalizado (Produto):** esse filtro, permite ainda a criação de um filtro personalizado partindo da entidade Produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Filtros de Estoque (PA)

Nessa aba, serão definidos todos os filtros de estoque para os Produtos Acabados (PAs). Os filtros aqui construídos impactam diretamente no cálculo da necessidade de produção do PA.

![Imagem 18: Nessa aba, serão definidos todos os filtros de estoque para os Produtos Acabados (PAs) . Os filtros aqui construídos…](https://ajuda.sankhya.com.br/hc/article_attachments/6933722764695)

**Considerar estoque de outros planos:** quando essa opção estiver marcada, o MPS irá considerar o estoque do produto em outros planos já confirmados (campo Qtd. Outros Planos) reduzindo assim a necessidade de produção do item em questão.

**OPs pendentes:** esta opção quando acionada, permite considerar o saldo de outras OPs pendentes no saldo a produzir do MPS. Tem-se as seguintes opções:

- **Não Considera**;
- **Tamanho de Lote:** será considerado o tamanho total de lote das OPs pendentes no saldo a produzir do MPS;
- **Saldo a Produzir:** a quantidade que ainda falta para ser produzida das OPs pendentes será considerada no saldo a produzir do MPS.

**Nota:** é necessário se atentar para a utilização desta opção, pelo fato de que as OPs Pendentes reduzem o saldo a produzir do produto, entretanto, ao serem finalizadas, deixam de ser OPs Pendentes e, por consequência, deixam de impactar o saldo a produzir. Sendo assim, essa opção deve ser empregada apenas para identificação de OPs ainda pendentes para a fabricação do produto que podem ser canceladas ou incorporadas ao planejamento em questão.

**Observações:** a respeito do planejamento de produção para produtos que utilizam PI com geração de subordens e consideram OP's pendentes, temos as seguintes considerações: 

- Se não possuírem sobra, não deverão ser consideradas;
- Se existirem subordens abertas para o PI e a quantidade de dependência for inferior ao Tamanho de Lote da subordem, o sistema irá considerar como OPs pendentes apenas a quantidade do PI que não possuir dependência;
- Quando existirem Ordens de Produção principais abertas para o PI (lançado como PA), ao gerar a necessidade de produção do PI, serão consideradas as OPs como OPs pendentes;
- Se existirem subordens abertas para o PI e a quantidade de dependência for inferior ao Tamanho de Lote da subordem e houver produção parcial para o PI, serão consideradas como OPs pendentes somente a quantidade do PI que não possuir dependência, sendo que a quantidade produzida será abatida da quantidade de dependência.

**Estoque Atual:** nesse campo, você define se o MPS deverá ou não considerar o estoque dos produtos acabados no cálculo de necessidade de produção. As opções disponíveis são:

- **Não considera:** com essa opção selecionada, não será considerado o estoque dos produtos;
- **Considera** **(Filtro Estoque):** por meio desta opção, será considerado o estoque dos produtos. Você pode então criar um filtro de estoque a partir dos campos Empresa, Filtro Locais e Filtro Estoque que serão habilitados.
- **Considera** **(Procedimento Personalizado):** através desta opção, será considerado o estoque dos produtos gerados a partir do procedimento personalizado desenvolvido e especificado no campo Procedimento Personalizado.

**Considerar Reserva:** através desta marcação, tem-se a possibilidade de definir se a quantidade reservada do produto será ou não considerada no cálculo de estoque dos Itens do Plano Mestre de Produção. Uma vez considerada, o estoque calculado será igual à quantidade em estoque subtraído a quantidade reservada, ou seja, quantidade disponível.

**Nota:** quando o campo Estoque Atual estiver configurado com a opção **"Não considera"**, a marcação Considerar Reserva ficará desabilitada.

**Empresa:** filtro de empresa para o estoque dos produtos. Quando vazio, o filtro não restringe a consulta de estoque à Empresa.

**Procedimento Personalizado:** este campo, será habilitado quando o campo Estoque Atual for definido como Considera (Procedimento Personalizado), de modo que, deve-se inserir aqui o nome do objeto em questão (Procedure) a ser utilizado para obter o estoque do produto.

O campo acima é composto por dois botões:

- ![Imagem 19: "Criar um template da rotina": Este cria no banco de dados uma rotina modelo (procedure modelo) com o nome igual ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16841116081559) **"Criar um template da rotina":** Este cria no banco de dados uma rotina modelo (procedure modelo) com o nome igual ao valor inserido no campo Procedimento Personalizado.
- ![Imagem 20: "Remover a rotina do Banco de dados": Acionando este botão, será removida a rotina (procedure) do banco de dados.](https://ajuda.sankhya.com.br/hc/article_attachments/16841116083991) **"Remover a rotina do Banco de dados":** Acionando este botão, será removida a rotina (procedure) do banco de dados.

**Importante:** a procedure aqui utilizada deve possuir, obrigatoriamente, os parâmetros P\_CODPROD (IN), P\_CONTROLE (IN), P\_CODEMP (IN), P\_CODLOCAL (IN) e P\_QTDESTOQUE (OUT).

P\_CODPROD NUMBER: Código do Produto.

P\_CONTROLE VARCHAR2: Controle adicional do Produto.

P\_CODEMP NUMBER: Código da Empresa.

P\_CODLOCAL VARCHAR2: Lista de Locais.

P\_QTDESTOQUE OUT FLOAT: Valor da quantidade de estoque que será calculada pela procedure.

**Filtro Locais:** filtro de locais para o estoque dos produtos. Quando vazio, o filtro não restringe a consulta de estoque à locais.

**Nota:** para definir a quantidade de registros de locais apresentados na tela é necessário configurar o número desejado no campo **"Texto"** do parâmetro **"Máximo de linhas para o serviço ExecQuerySP - MAXROWEXECQUERY"**.

**Filtro Estoque:** pode-se neste espaço construir um filtro personalizado para a consulta de estoque dos produtos partindo do Estoque.

#### Seção Pedidos de Compras

Podem ser considerados também os pedidos de compra pendentes de entrega como estoque dos Produtos Acabados (PA's), assim a necessidade de produção calculada será subtraída pelo valor encontrado.

**Considerar Pedidos de Compra:** esta marcação determina, se serão ou não considerados os pedidos de compra. Se assinalada, os campos abaixo serão habilitados.

**Filtro Grupos TOPs:** temos aqui, um filtro para os grupos de [TOP's](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) que devem ser considerados na consulta de pedidos de compras para os PA's do MPS.

**Filtro Personalizado (Itens de Pedido):** configure neste ponto, um filtro personalizado partindo da entidade Itens de Pedido que será considerado na consulta de pedidos de compra apara os PA's do MPS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Filtros de Estoque (MP)

Nos campos aqui expostos, serão definidos todos os filtros de estoque para as Matérias Primas (MP's) que serão consideradas na execução do MRP. Os filtros aqui construídos impactam diretamente no cálculo da necessidade de compra de materiais.

![Imagem 21: Nos campos aqui expostos, serão definidos todos os filtros de estoque para as Matérias Primas (MP's) que serão…](https://ajuda.sankhya.com.br/hc/article_attachments/6933986479127)

**Estoque Atual:** neste campo defina se o MRP deve ou não considerar o estoque de produto no cálculo da necessidade de materiais. As opções disponíveis são:

- **Não considera:** por meio desta opção, não será considerado o estoque dos produtos.
- **Considera (Filtro Estoque):** com esta opção selecionada, será considerado o estoque dos produtos, de modo que você pode criar um filtro de estoque a partir dos campos Empresa, Filtro Locais e Filtro Estoque que serão habilitados.
- **Considera (Procedimento Personalizado):** se for selecionada esta opção, será considerado o estoque dos produtos gerados a partir do procedimento personalizado que você possa ter desenvolvido e especificado no campo Procedimento Personalizado.

**Empresa:** filtro de empresa para o estoque dos produtos. Quando estiver vazio, o filtro não restringe a consulta de estoque à empresa.

**Procedimento Personalizado:** esse campo é habilitado quando o campo Estoque Atual for definido com a opção Procedimento Personalizado, onde deve-se inserir o nome do objeto em questão (PROCEDURE). Os parâmetros de entrada são, CODPROD (código do PA) e CONTROLE (controle adicional da MP).

**Filtros Locais:** filtro de locais para o estoque dos produtos. Se estiver vazio, o filtro não restringe a consulta de estoque à locais.

**Nota:** para definir a quantidade de registros de locais apresentados na tela é necessário configurar o número desejado no campo **"Texto"** do parâmetro **"Máximo de linhas para o serviço ExecQuerySP - MAXROWEXECQUERY"**.

**Filtro Estoque:** a partir deste campo, você pode construir um filtro personalizado para a consulta de estoque dos produtos partindo da entidade Estoque.

#### Seção Pedidos de Compras

Podem ser considerados também os pedidos de compra pendentes de entrega como estoque dos produtos, assim a necessidade de materiais calculada irá subtrair o valor encontrado.

**Considerar Pedidos de Compras:** esta marcação determina se serão ou não considerados os pedidos de compra. Se assinalado, os campos abaixo serão habilitados.

**Filtro Grupo TOPs:** este filtro, é direcionado para os grupos de TOP's que devem ser considerados na consulta de pedidos de compras para os MP's do MPS.

**Filtro Personalizado (Itens de Pedido):** filtro personalizado partindo da entidade Itens de Pedido que será considerado na consulta de pedidos de compra apara os MP's do MPS.

#### Seção Cotação

Esta seção permite realizar a definição de quais cotações serão consideradas na execução do MRP (necessidade de compras do material). De modo que, você pode filtra-las de acordo com a sua situação (filtro Situações).

Sendo que, além do filtro rápido (Situações) é possível realizar a formulação de filtros avançados (Filtro Personalizado) para exibição das mesmas. Sendo que, estes filtros só estarão disponíveis quando a marcação **"Considerar cotação"** estiver acionada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## MRP

Você irá configurar as regras básicas para a execução do MRP nos campos aqui expostos.

![Imagem 22: Você irá configurar as regras básicas para a execução do MRP nos campos aqui expostos.](https://ajuda.sankhya.com.br/hc/article_attachments/6934082775447)

**Executar MRP para dois períodos:** existem cenários onde o MRP deve ser executado considerando o período de planejamento e o próximo período, com o objetivo de adiantar a compra de alguns materiais que possuem lead time (tempo entre o momento de entrada do material até à sua saída do inventário) de fornecimento alto. Com essa opção marcada o MPS será gerado para dois períodos onde a demanda do segundo período será a mesma do primeiro. Assim, você pode realizar pequenos ajustes antes da execução do MRP. Caso esta marcação não esteja realizada.

**Matriz de Giro Período 1:** o resultado da execução do MRP é a lista de necessidade de materiais necessários para a produção de todos os PA's contidos no MPS. Para todos os materiais cujo saldo seja negativo (existe necessidade de compra dado MPS em questão), tem-se a possibilidade de informar ao departamento de compras sua necessidade a partir da geração de uma Matriz de Analise de Giro. A geração da matriz é apenas a apresentação de sugestão de compras baseado no resultado do MPS, e não um cálculo de giro desses produtos. Deste modo, o departamento de compras será capaz de executar a compra dos materiais utilizando a ferramenta de compras já existente no sistema. Logo, esse campo determina qual configuração de matriz será utilizada na geração da matriz que representa a necessidade de materiais. Quando não preenchida, o sistema gera uma configuração de matriz automaticamente e associa a configuração do MPS.

**Matriz de Giro Período 2:** informe aqui, a matriz de giro para gerar necessidade de compras dos materiais referentes ao segundo período. Quando não preenchida, o sistema gera uma configuração automaticamente e associa a configuração do MPS.

**Considerar qtd. adicional:** quando a execução do MRP está configurada para dois períodos, tem-se a possibilidade de considerar a Qtd. Adicional do primeiro período no segundo período. Dessa forma, se for indicado um valor adicional no primeiro período, este valor será inserido automaticamente no segundo período.

**Considerar '% Ajuste Demanda':** quando marcado, o segundo período do MPS receberá o percentual de ajuste de demanda definido no cabeçalho do MPS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Plano Mestre de Produção | Novo Plano

Uma vez que a Configuração de MPS foi realizada, é possível iniciar o lançamento de um novo MPS. Ao clicar no botão de inclusão, será aberto o pop-up **"Cadastrar Plano Mestre de Produção"** para definição dos dados globais do MPS.

![Imagem 23: Uma vez que a Configuração de MPS foi realizada, é possível iniciar o lançamento de um novo MPS . Ao clicar no botão de…](https://ajuda.sankhya.com.br/hc/article_attachments/6934087730071)

**Configuração:** aqui serão apresentadas todas as configurações de MPS já existentes, para que seja definida qual será utilizada no plano criado. Pode-se ainda iniciar a criação de uma nova configuração por meio do botão de inclusão localizado à frente do campo.

**Planta de Manufatura:** informe nesse campo, a planta de manufatura correspondente ao Plano Mestre. Os processos produtivos considerados para os itens do MPS serão apenas os referentes a planta em questão ou àqueles sem definição de planta (processos compartilhados por todas as plantas).

**% Ajuste Demanda:** nesse campo, determine um percentual de ajuste sobre o valor de demanda calculado pelo MPS para todos os itens (pode ser um valor positivo ou negativo). Esse recurso é útil quando se sabe que a demanda do período do MPS será aquela determinada na configuração já existente, acrescida de uma sazonalidade do período causada por alguma ação da empresa (campanha publicitária que irá representar um ganho de venda em X% do esperado para o período, por exemplo) . Esse percentual de ajuste pode ser editado a qualquer momento após o lançamento do plano, mas exige o reprocessamento do MPS. Por exemplo, se a demanda do produto calculada foi de 100 Unidades com um percentual de ajuste de 25%, a demanda ajustada do produto será 125 Unidades.

**Período MPS:** defina o período (data inicial e data final) do plano, ou seja, o MPS representa esse período de produção da indústria. O período de planejamento pode ser modificado a qualquer momento após o lançamento do plano, mas exige o reprocessamento do MPS.

**Período dos Pedidos:** aqui, será determinado o período (data inicial e data final) dos pedidos firmes a serem considerados no cálculo da necessidade de produção. Esse valor pode ser diferente do período do MPS e apenas estará habilitado para edição, caso a configuração selecionada possua como Tipo de Demanda a opção Pedidos Firmes (aba [Demanda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#mps-abademanda)). Depois de criado, o plano não permite a edição desse campo. Assim, feito o lançamento do MPS, você poderá visualizaré possível visualizar seus dados no cabeçalho do plano e também na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#h_01G3YBZ8G9083FNV4RH1JMYN95).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Geral

Por meio desta aba, você realizará a configuração do comportamento geral que diz respeito a demanda dos produtos do MPS.

![Imagem 24: Por meio desta aba, você realizará a configuração do comportamento geral que diz respeito a demanda dos produtos do MPS…](https://ajuda.sankhya.com.br/hc/article_attachments/6934239860375)

Dessa forma, além dos dados gerais até aqui descritos no lançamento de um Novo Plano Mestre de Produção no tópico acima, um MPS possui as seguintes informações (Cabeçalho e aba Geral):

**Situação:** nesse campo, você pode confirmar o planejamento com o objetivo de fazer com que o seu cálculo da necessidade de produção influencie em outros planos (a configuração dos planos que devem ser influenciados, precisa estar assinalada para considerar outros planos); um Plano pode estar Pendente ou Confirmado.

**Dh. Geração MRP:** esse campo armazena a Data e Hora em que o MRP foi executado. Caso o MRP já tenha sido gerado anteriormente e alguma alteração nos itens do MPS seja realizada, esse campo será apagado, permitindo assim novamente a execução  do MRP.

**Usuário:** defina neste, o Usuário responsável pela criação do plano.

**Dh. Alteração:** data e hora da última alteração no plano.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Plano Mestre de Produção

Após a definição dos dados globais do plano, o sistema calcula os itens para o plano em questão. O resultado é apresentado na aba Plano Mestre de Produção. Temos as seguintes informações:

**Nota:** o Plano Mestre de Produção não considera itens configurados em processos produtivos de produção para terceiros. A rotina trabalha com planejamento por metas de vendas, pedidos firmes ou giro de produtos, porém para o caso de produção para terceiros, é vendido o serviço de industrialização e apesar de existir necessidade de produção para esses itens, não existe demanda, visto que esses itens produzidos não são comercializados pela empresa.

> **Importante:** dado o filtro de produtos da configuração do MPS, apenas os produtos vinculados a algum Processo Produtivo definido como Padrão serão inseridos no plano. Além dos resultados gerados pela configuração de MPS selecionada para o plano, a qualquer momento você poderá inserir um novo PA na lista de itens do plano.

**Produto:** código e Descrição do Produto.

Quando o produto possuir a configuração de tempo de processamento, o sistema apresentará o resultado no campo "Tempo de Atravessamento (min)" para todos os produtos do MPS (PA's e PI's). Para isso, o Sankhya Om valida algumas regras:

- Possuir um Processo Produtivo configurado como "Padrão" para os produtos do MPS;
- Na tela Composição do Produto devem ser cadastrados os PA's e PI's que serão utilizados no MPS vinculados ao processo produtivo configurado acima;
- Os produtos cadastrados na tela Composição do Produto devem ter o Tempo de Atravessamento maior do que zero (tanto os PA's quanto PI's);
- Na tela de Planejamento de Produção (MRP I) tem que existir um MPS com configuração de "Tipo Demanda" igual à "Pedidos Firmes" e com a marcação "Detalhar itens agrupando pela previsão de entrega" realizada;
- O MPS deve estar configurado para apresentar os PI's;
- Por fim, deve-se ter um pedido de venda que gera demanda para o PA no MPS.

O valor apresentado no campo "Tempo de Atravessamento (min)" dos produtos no MPS deve estar de acordo com o Tempo de Atravessamento da Composição do Produto, em razão do "Tamanho de Lote Padrão" e do "Saldo à Produzir" do produto no MPS.

**Controle:** controle adicional do produto, quando este possuir controle do tipo Lista (respeita o parâmetro "Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE").

**Processo Produtivo:** tem-se aqui o Processo Produtivo que está sendo considerado no MPS para o produto em questão. Inicialmente o sistema utiliza o processo Padrão do produto, priorizando o processo produtivo "Padrão por Produto". Caso não exista, utilizará o processo produtivo Padrão. No entanto, é possível realizar alterações nesse processo, caso seja necessário.

> **Importante:** ao realizar a pesquisa pelos Processos Produtivos, caso o parâmetro "Lançar OPs utilizando versões anteriores à última - LANCOPVERSANT" esteja ativado, as versões antecedentes à última também serão apresentadas para escolha.

**Un.:** unidade de volume do produto considerado no MPS.

**Qtd. Giro Médio Calc.:** giro médio calculado dada a configuração do MPS para o produto. Faz sentido quando o tipo de demanda da configuração é projeção de giro. Quando na Configuração do MPS a marcação "Executa MRP para dois períodos" (aba MRP) estiver realizada, o valor desse campo será igual para os dois períodos.

**Giro Médio:** tem-se aqui o Giro Médio considerado pelo MPS para o produto. Inicialmente esse campo é preenchido com o mesmo valor do campo Qtd. Giro Médio Calc., porém pode-se editar a demanda do produto. Esta informação faz sentido quando o Tipo de Demanda da configuração for definida como Projeção de Giro (aba Demanda). Quando na Configuração do MPS a marcação Executa MRP para dois períodos (aba MRP) estiver realizada, o valor desse campo será igual para os dois períodos, porém a edição realizada por você influenciará apenas no período posicionado.

**Demanda Bruta:** trata-se da Demanda Bruta calculada para o produto dada a configuração do MPS. Quando o Tipo de Demanda da configuração for definida como Projeção de Giro (aba Demanda), esse campo tem o mesmo valor do campo Giro Médio, já para os outros tipos de demanda será o valor calculado pelo sistema.

**Demanda Indireta:** essa informação representa a demanda deste produto vinda de outro PA, ou seja, a quantidade necessária do produto para atender ordens de PA's. Apenas os PI's possuem demanda indireta.

**Demanda Ajustada:** a demanda ajustada do produto, corresponde ao valor da demanda bruta aplicando o percentual de ajuste definido no cabeçalho do plano somado a demanda indireta. Quando na Configuração do MPS as marcações Executa MRP para dois períodos e "Considera '% Ajuste Demanda'" estejam efetuadas (aba MRP), os registros dos dois períodos serão influenciados pelo % de ajuste do cabeçalho. Tem-se portanto:

Demanda Ajustada = Demanda Bruta \* (1 + % Ajuste Demanda) + Demanda Indireta

**Estoque:** esta informação corresponde ao Estoque do produto no momento em que o MPS foi gerado, considerando a configuração de estoque utilizada no plano. Quando na Configuração do MPS a marcação Executa MRP para dois períodos (aba MRP) estiver realizada e o estoque tenha sido suficiente para atender a demanda do primeiro período, o valor restante será apresentado como estoque no segundo período.

**À Produzir Calc.:** a quantidade a produzir calculada, reduz da demanda ajustada o valor em estoque, e ajusta esse valor ao estoque mínimo de acordo com a configuração do MPS, ou seja:

À Produzir Calc. = (Demanda Ajustada - Estoque) + Estoque Mínimo

**À Produzir Ad.:** dada quantidade a produzir calculada pelo sistema, pode-se ainda manipular o valor inserindo uma quantidade adicional neste campo. Esse valor pode ser positivo para aumentar a necessidade de produção ou negativo para diminuir a necessidade de produção do item. Quando na Configuração do MPS as marcações Executa MRP para dois períodos e "Considera qtd. adicional" estejam efetuadas (aba MRP), a edição desse campo no primeiro período será espelhada para o segundo período.

**Pedido de Compra:** caso a configuração do MPS considere pedidos de compra, será apresentado nesse campo a quantidade do item em pedidos de compra. Serão considerados os pedidos pertinentes à configuração realizada (Filtros) que estejam confirmados e pendentes; a quantidade exibida é a Quantidade Pendente (Quantidade negociada - Quantidade entregue).

A data de pedido de compra (DPC) para cada item do BOM é calculada a partir da previsão de entrega, do lead time de compra e do lead time de produção, considerando as [Configurações do MPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I-#configurandomps) como o "Tipo Demanda", "Tipo de Período" e o detalhamento de itens pela previsão de entregas. Para que esse cálculo seja realizado, a configuração do MPS deve ter Tipo Demanda = Pedidos Firmes, Tipo de Período = Previsão de Entrega, e a marcação "Detalhar itens agrupando pela previsão de entrega" habilitada. Os parâmetros considerados são:

- Previsão de Entrega: através dos MPS, no campo "Previsão de Entrega" da aba Plano Mestre de Produção.
- Lead time de compra: preferencialmente, o lead time de compra deve ser obtido através do campo "Lead time de compra" do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba Medidas e Estoque; porém, existem situações em que o lead time pode variar por Empresa e/ou Unidade e, nesse caso, será buscado o valor do campo Lead time de compra através da aba Impostos / Informações por empresa, referente à cada empresa.
- Lead time de produção: no MPS, é possível obter o lead time de produção através do campo "Tempo de Atravessamento (min)" da aba Plano Mestre de Produção. Esse tempo é definido como o tempo decorrido a partir do momento em que uma matéria-prima chega na empresa, e o momento em que ela chega ao armazém incorporada em um produto acabado.

Fórmula: DPC = Previsão de Entrega - Lead Time (Compra) - Tempo de Atravessamento (Produção)

**Observação:** na tela de Necessidade de Materiais (botão MRP), teremos o campo "Data Pedido de Compra" com o cálculo já realizado. Você também poderá filtrar, na tela de Necessidade de Materiais, pelo "Nro. Material" e pelo "Período Data Pedido de Compra".

**À Produzir Liq.:** a quantidade a produzir líquida é o valor a produzir calculado, subtraído aos pedidos de compra, somado à quantidade a produzir adicional. Esse valor sofre arredondamento referente ao tamanho mínimo e múltiplo do lote, ou seja:

À Produzir Liq. = À Produzir Calc. - Pedido de Compra + À Produzir Ad.

**Qtd. em OPs:** este campo apresenta a quantidade do produto que já está em ordens de produção a partir desse planejamento.

Qtd. em OPs = Soma (Qtd. a produzir por OP desse MPS)

Ou seja, pode-se considerar, por exemplo, que duas OPs foram geradas no MPS 10, cada uma com um saldo de 30 a produzir, no campo Qtd. em OPs serão exibidas a quantidade de 60 para o MPS 10.

**Outras OPs Pendentes:** através deste campo, pode-se visualizar as outras OPs pendentes para o produto no MPS. Sendo que, este campo só ficará visível quando a marcação "Considerar outras OPs pendentes" localizada na aba Filtros de Estoque, sub-aba Produtos Acabados (PA) estiver acionada.

**Saldo a Produzir:** este campo apresenta a diferença entre À produzir Liq. e Qtd. em OPs, de forma a demonstrar o que de fato está custando.

Saldo a Produzir = À produzir Liq. - Qtd. em OPs

**Demanda Líquida:** a quantidade de Demanda Líquida é a soma da Demanda Ajustada e quantidade À Produzir Ad. arredondado ao lote mínimo do produto (conforme configuração do MPS).

**% Estoque x Demanda:** a percentual de estoque por demanda líquida é um indicador muito utilizado nas indústrias com o objetivo de identificar quais itens devem ter sua produção priorizada com base na necessidade de atendimento. Logo quanto menor esse valor, mais urgência se tem em produzir. É considerado como estoque, a quantidade do produto em estoque somada a quantidade em pedidos de compra, ou seja:

% Estoque x Demanda = (Estoque + Pedidos de Compra) / Demanda Líquida

**Qtd. Base MRP:** esta informação faz sentido apenas quando na Configuração do MPS a marcação Executa MRP para dois períodos (aba MRP) estiver realizada. O valor apresentado será o mesmo valor do campo À Produzir Liq. de ambos os períodos como uma forma de produzir o total do item. Logo, quando o planejamento for apenas para um período, esse campo terá o mesmo valor que o campo À Produzir Liq..

**Qtd. Outros Planos:** tem-se aqui, a Quantidade À Produzir Liq. do produto em outros planos confirmados, cujo período esteja contido no período do plano. Apenas será calculado, quando na Configuração do MPS a marcação "Considerar estoque de outros planos" (aba MRP) estiver realizada.

**Fixado:** Esta marcação é utilizada para não recalcular a demanda do produto em um reprocessamento do MRP; ele sinaliza se o produto foi ou não fixado.

**Observação:** após inserir manualmente um produto nos itens do planejamento, o sistema sempre executará e reprocessará, internamente, todos os produtos.

**Produto Intermediário:** esta marcação sinaliza que o produto é um Produto Intermediário (PI).

**Prioridade:** identifica a prioridade do item para o momento de lançamento de ordem do produto. Quando são selecionados vários produtos e tem-se o comando do lançamento de ordem, esse valor será utilizado para identificar qual produto será primeiramente lançado (ordem crescente).

**Dh. Inicialização (máx):** refere-se a data em que o produto precisa começar a ser produzido para que a produção seja finalizada na data e hora esperada. Esse campo considera o "Tempo de atravessamento" calculado para o produto e a "Carga Horária" configurada na Planta de Manufatura.

**Observação:** nesse momento (geração do Plano Mestre de Produção), a Carga Horária do Centro de Trabalho não é considerada, visto que as OPs não foram geradas e as atividades não foram alocadas.

**Nro. Nota** e **Sequência**: esses campos exibem o número da nota do pedido de venda e a sequência do item que originaram a demanda no Plano Mestre de Produção. Eles aparecem quando, na Configuração do MPS (aba Demanda, sub-aba Pedidos Firmes), a marcação **Detalhar itens por pedido** está ativada. Nessa condição, a demanda é agrupada pelo número do pedido de venda — cada pedido gera uma linha própria no MPS — permitindo rastrear a origem de cada item específico do pedido.

Para que essa marcação funcione corretamente, é necessário que o Tipo de Demanda esteja configurado como **Pedidos Firmes**, o Tipo de Período como **Previsão de Entrega (Nota)** ou **Previsão de Entrega (Itens)**, e que os pedidos de venda considerados tenham a previsão de entrega informada — na nota ou no item, conforme a opção escolhida em Tipo de Período.

Essa configuração também permite filtrar as Ordens de Produção pelo número do pedido de venda na tela **Ordens de Produção - Nova**. Quando as OPs são geradas pelo MRP com essa configuração ativa, o sistema também exibe as Sub-Ordens dos Produtos Intermediários (PI's) vinculadas ao número do pedido.

> **Atenção:** a marcação **Detalhar itens por pedido** não funciona em conjunto com a configuração **Tamanho de Lote da OP igual ao Lote Padrão**.
>
> Não confunda com a marcação **Detalhar itens agrupando pela previsão de entrega** (aba Demanda) — nela, o agrupamento é feito exclusivamente pela data de previsão de entrega, e a demanda de pedidos diferentes com a mesma data é somada em uma única linha, sem preservar a identificação do pedido de origem.

![Imagem 25: Não confunda com a marcação Detalhar itens agrupando pela previsão de entrega (aba Demanda) — nela, o agrupamento é…](https://ajuda.sankhya.com.br/hc/article_attachments/42834969824919)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611174-Planejamento-de-Produ%C3%A7%C3%A3o-MRP-I#top)

## Aba Plano Mestre de Produção - Botões

**Botão Outras Opções...**

Através deste botão tem-se acesso as seguintes funcionalidades:

**Visualizar OPs**

Esta opção quando acionada exibe um pop-up de mesma nomenclatura contendo as informações a respeito de todas as OPs abertas para a fabricação do produto dado aquele MPS. Caso o MPS esteja configurado para Considerar outras OPs pendentes, tem-se a exibição das informações pertinentes as outras OPs pendentes neste pop-up.

![Imagem 26: Esta opção quando acionada exibe um pop-up de mesma nomenclatura contendo as informações a respeito de todas as OPs…](https://ajuda.sankhya.com.br/hc/article_attachments/6934283283223)

Você pode ampliar ou limitar a exibição das OPs de acordo com o seu status utilizando o campo **"Status da OP"**, onde temos a possibilidade de optar por apenas um status ou por todos os status.

O filtro **"Tipo de OP"** será apresentado para facilitar a identificação das OPs. São apresentadas as seguintes opções:

- **OPs do MPS:** irá restringir a visualização para as OPs pertencentes ao MPS para o produto;
- **Outras OPs pendentes:** são exibidas somente as outras OPs pendentes para o produto;
- **Ambas:** tem-se a exibição de ambas as opções.

Através do botão **"Visualizar OP"**, tem-se a abertura da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) posicionada na OP selecionada.

**Importante:** para que essas informações sobre as outras OPs pendentes sejam apresentadas, é necessário que a marcação **"Considerar outras OPs pendentes"** localizada na aba Filtros de Estoque, sub-aba Produtos Acabados (PA) esteja acionada.

**Observação:** ao gerar o Plano Mestre de Produção, quando for consultadas as OPs pendentes do PI através da opção Visualizar OP, não serão apresentadas ordens de PI que possuírem dependência com OPs de PAs e que foram lançadas como subordem. 

---

**Fixar/Desfixar registro selecionado**

O recurso Fixar registro, impede que o item sofra alterações durante o reprocessamento do MPS. Assim, pode-se executar todos os ajustes que forem necessários no item e fixá-lo, com o objetivo de não perder esses ajustes durante o reprocessamento do MPS. Para fixar ou desfixar o item, basta selecionar o registro e clicar sobre a referida opção.

---

**Detalhamento (Giro) produto selecionado**

Quando a Configuração do MPS possuir o Tipo de Demanda definido como Projeção de Giro, faz sentido visualizar o giro do produto em cada um dos períodos considerados pelo plano visto que o resultado final é o valor médio dos períodos. Para esse detalhamento, clique nesta opção, para que seja apresentado o pop-up **"Detalhes de Giro"**.

![Imagem 27: Quando a Configuração do MPS possuir o Tipo de Demanda definido como Projeção de Giro , faz sentido visualizar o giro…](https://ajuda.sankhya.com.br/hc/article_attachments/6934348970007)

Esse pop-up não bloqueia a possibilidade de alternar entre os registros do MPS facilitando assim uma possível análise de vários itens de um plano.

**Observação:** o resultado apresentado no pop-up Detalhes de Giro desta tela não deve ser comparado ao resultado calculado na tela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro), já que cada uma dessas rotinas considera diferentes variáveis para o cálculo dos detalhes de giro. Neste caso, a tela Planejamento de Produção realiza os cálculos baseando-se nas quantidades negociadas nos períodos apresentados, desde que exista relacionamento com processos produtivos da **"Planta de Manufatura do Planejamento"**. Enquanto a tela Análise de Giro realiza o cálculo baseado em todas as negociações daquele período, considerando ainda estoque e custos, dentre outras variáveis, para gerar seus valores.

---

**Detalhes Matérias Primas para PA selecionado**

Quando essa opção é acionada, apresenta na tela o pop-up **"Lista de Materiais (B.O.M.)"** que exibe de fato, a lista de materiais correspondente ao produto selecionado na grade de itens, com base no processo produtivo do PA.

![Imagem 28: Quando essa opção é acionada, apresenta na tela o pop-up "Lista de Materiais (B.O.M.)" que exibe de fato, a lista de…](https://ajuda.sankhya.com.br/hc/article_attachments/8214328361879)

---

**Seleção de Período**

Na Configuração do MPS quando a marcação Executa MRP para dois períodos (aba MRP) estiver realizada, esta opção será exibida e através dela, você pode alternar entre os registros de itens do plano referentes ao primeiro e segundo períodos.

---

**Gerar OP**

Uma vez que o MPS esteja concluído, ou seja, o cálculo de demanda tenha sido realizado e os ajustes executados se tornarem necessários (edição de giro e demanda ajustada), é possível gerar ordens de produção para os itens. Para isso, clica-se neste botão. Antes de modificar a visão da interface para **"Lançamento de Ordens de Produção"**, o sistema o questionará se deseja gerar rascunho de OP's considerando Todos os produtos do MPS ou Apenas produtos selecionados, além da opção **"Deseja agrupar produtos semelhantes?"** que quando selecionada, irá agrupar na mesma OP os produtos PA, data de entrega iguais e números das notas de pedidos diferentes.

Após o rascunho do lançamento de OP ser lançado, os produtos iguais serão agrupados em uma linha com o tamanho do lote somado, e caso os PA's tenham o mesmo PI estes serão agrupados e o tamanho do lote será somado dos PIs. Uma vez gerado, não será possível alterar o rascunho.

> ℹ️**Observação**: ao gerar OPs utilizando a opção "apenas selecionados" e escolhendo somente produtos intermediários, o sistema irá gerar as OPs apenas se os PIs possuírem Demanda Bruta. Nesse caso, o tamanho do lote da OP será definido com base nessa demanda bruta. Isso ocorre porque, como o produto acabado (responsável por gerar a demanda indireta) não será produzido, a demanda indireta não é considerada na geração das OPs.

O ajuste da OP no rascunho do seu lançamento será realizado se o campo **"Fórmula p/ Ajuste Tamanho de Lote"** presente nas telas [Composição do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050836154-Composi%C3%A7%C3%A3o-do-Produto) e [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova), estiver preenchido, sendo estas configurações para produtos ou processos, conforme às telas configuradas. Considere também que, o tamanho dos Produtos Intermediários será calculado conforme o tamanho de lote ajustado.

Quando a configuração estiver marcada para Detalhar itens por pedido, clique no botão **"Lançar Ordens"** para que estas sejam geradas.

---

**Pesquisar MPS**

Por meio da barra de pesquisa, você poderá efetuar a busca de um produto pertinente a um determinado MPS, através do seu código ou da sua descrição.

---
