---
id: "360044601774"
titulo: "Controle de Veículos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:53Z"
rotulos: ["Controle de Veículos manual", "Configuração", "Veículos", "Parceiro", "RATEIOPORVEICU", "Transporte", "Financeiro", "FILTRAVEICCTRL", "VINPRODVEINFE", "Gestão Eficiente de Frota de Veículos", "Gestão de Frota"]
---

# Controle de Veículos

O objetivo desta documentação é demostrar através da funcionalidade de controle de veículos como se realiza a gestão da frota de veículos da empresa. Pode-se controlar entradas e saídas, ordem de carga, despesas diversas com os veículos, manutenção com peças, consumo e custo com combustível, entre outras.

Estes recursos são destinados para empresas que trabalham com transporte de carga própria e entrega de mercadorias, empresas que utilizam veículos próprios, normalmente com um motorista, para prestação de serviços ou outras atividades que controlem apenas os quilômetros rodados, ou esse recurso que pode ser utilizado no Controle de Veículos ou isoladamente, ou seja, todas as empresas que precisam controlar débitos e créditos que ocorrem durante uma viagem.

Para conferir as funcionalidades dessa tela, basta acessar os links abaixo:

| Funcionalidades da tela | |
| --- | --- |
| [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#cadastrodeveculos) | [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#cadastrodeparceiros) |
| [Cadastro de Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#cadastrodegruposdeprodutosservios) | [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#critriosderateio) |
| [Realizando o Controle de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#realizandoocontroledeveculos) | [Controle de Saída/Chegada de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#controledesadachegadadeveculos) |
| [Gerência de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#gernciadeveculos) |  |

### Cadastro de Veículos

O [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-) é primordial para o funcionamento da rotina de Controle de Veículos. A respeito deste cadastro, pode-se destacar:

- É imprescindível que o parâmetro **"Usar rateio por veículo? - RATEIOPORVEICU"** esteja habilitado para realização dos lançamentos e controles dos veículos; sua ativação irá habilitar na aba [Informações Complementares](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos#h_6e9b6c3a-7f9e-4d3e-91a4-99bb9e15fa15) os campos **"Centro de Resultado"**, **"Aferição"**, e **"Tipo Aferição"**;
- O campo Aferição deve ser preenchido para ser exigida a quilometragem do veículo nos respectivos lançamentos e seja possível realizar controle de quilometragem.
- Também na aba Informações Complementares, os campos **"Produto"** e **"Código do bem"** serão exibidos apenas se o parâmetro **"Vincular produto a um veículo p/ Geração da NFE? - VINPRODVEINFE"** estiver ligado. Esses campos visam atender as exigências fiscais da Nota Fiscal Eletrônica para empresas importadoras/exportadoras, que comercializam veículos novos.
- Com o parâmetro **"Filtrar veículos com Chassi igual ao Controle? -** **FILTRAVEICCTRL"** ligado, o sistema usará o controle adicional do item para buscar o veículo cadastrado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

### Cadastro de Parceiros

No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), deve-se cadastrar o Motorista como parceiro para controle das despesas de viagem e selecionar na [aba Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), campo **"Tipo"**, a opção **"Transportadora"** para ser informado na nota fiscal como o responsável pelo transporte e entrega da mercadoria;

Ainda na aba Identificação, campo Tipo, marca-se também a opção **"Conta adiantamento"**; esta medida irá apresentar a aba [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontabancria), onde se inclui uma conta bancária para o lançamento dos movimentos financeiros referentes ao próprio motorista e seu veículo. Este cadastro controlará todos os créditos e débitos que serão lançados para o motorista durante a viagem, por exemplo, adiantamentos de viagem, gastos com alimentação, combustível, peças, pedágios e demais.

**Importante:** no [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-), aba Propriedades, realiza-se no campo Motorista o vínculo entre o mesmo e o respectivo veículo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

### Cadastro de Grupos de Produtos/Serviços

Para uma melhor análise, no [Cadastro de Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os) determina-se de forma bem definida os grupos e produtos que serão utilizados na manutenção dos veículos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

### Critérios de Rateio

Os Veículos que possuírem em seu cadastro a **"Aferição"** definida como **"Obrigatória"** no [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos), aba [Informações Complementares](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos#h_6e9b6c3a-7f9e-4d3e-91a4-99bb9e15fa15) deverão ter nos [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio) o campo Aferição cadastrado com um valor coringa, 1, por exemplo; quando o critério for utilizado em um rateio, o usuário editará o campo com o valor de aferição correspondente ao lançamento empregado.

O campo **"Aferição Veic."** habilita a inserção automática do último registro no campo **"Km Inicial"** na tela de [Gerência de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

### Realizando o Controle de Veículos

Após efetuar os cadastros corretamente e realizar os lançamentos dos devidos registros. Como, por exemplo, nota de compra, despesas ou requisições referentes ao veículo, utiliza-se o botão **"Ratear"** presente na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) no caso de aquisição de peças ou serviços para controle de estoque.

O campo **"Aferição Veic."** do rateio é utilizado para ser informada a quilometragem do veículo.

![Imagem 1: O campo "Aferição Veic." do rateio é utilizado para ser informada a quilometragem do veículo.](https://ajuda.sankhya.com.br/hc/article_attachments/8535113023255)

Na [Central de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas) para controle de combustível, a quilometragem rodada é também empregada para controle de estoque.

![Imagem 2: Na Central de Movimentações Internas para controle de combustível, a quilometragem rodada é também empregada para…](https://ajuda.sankhya.com.br/hc/article_attachments/8535538076951)

Na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), são lançados os gastos que não precisam de controle de estoque com sua respectiva natureza; além disso, informa-se o número da Ordem de Carga para que seja feita a ligação do financeiro a um motorista e sua respectiva conta bancária para controle de despesas de viagem.

![Imagem 3: Na Movimentação Financeira , são lançados os gastos que não precisam de controle de estoque com sua respectiva…](https://ajuda.sankhya.com.br/hc/article_attachments/8535534393495)

O controle da quilometragem poderá ser realizado também por meio da tela [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025242234-Ordens-de-Carga), onde são informadas as quilometragens inicial e final de uma determinada Ordem de Carga.

![Imagem 4: O controle da quilometragem poderá ser realizado também por meio da tela Ordens de Carga , onde são informadas as…](https://ajuda.sankhya.com.br/hc/article_attachments/8535646077591)

**Nota:** o controle de quilometragem, realizado na [Central de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas) é a rotina responsável pelo controle da média de quilômetros rodados por litro de combustível entre um momento de abastecimento e outro. Já o controle feito por meio de [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga) faz uso desta mesma média considerando apenas os quilômetros rodados naquele traslado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

**Controle de Saída/Chegada de Veículos**

A tela [Controle de Saída/Chegada de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603074-Controle-de-Sa%C3%ADda-Chegada-de-Ve%C3%ADculos) é utilizada para controle de saída e entrada dos veículos na empresa, podendo controlar quilometragem, usuário do veículo, destino ou atividade realizada com o veículo, entre outras.

![Imagem 5: A tela Controle de Saída/Chegada de Veículos é utilizada para controle de saída e entrada dos veículos na empresa,…](https://ajuda.sankhya.com.br/hc/article_attachments/8536076946711)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)

**Gerência de Veículos**

A análise correspondente à rotina Controle de Veículos é a [Gerência de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110293-Ger%C3%AAncia-de-Ve%C3%ADculos), onde as informações estão disponíveis somente para consulta. Utiliza-se então os filtros disponíveis na tela para concretização da análise.

![Imagem 6: A análise correspondente à rotina Controle de Veículos é a Gerência de Veículos , onde as informações estão disponíveis…](https://ajuda.sankhya.com.br/hc/article_attachments/8536357107607)

A respeito da Gerência de Veículos, pode-se destacar os seguintes aspectos:

- A aba Consumo Peças/Combustível conta com um resumo completo do consumo de peças, combustível e produtos. É pautado um consumo por quilometragem em relação à última nota, pedido ou requisição lançada com uma quilometragem informada;

**Importante:** na grade inferior presente nesta aba a coluna **"Km Rodados"** é calculada considerando a compra de cada produto separadamente. Apenas a partir da segunda compra de um item, tem-se informações suficientes para que a diferença entre o Km Final e o Km Inicial seja calculada, pois será possível identificar o quanto se percorreu utilizando o produto partindo a primeira compra até sua segunda aquisição.

- Na aba [Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110293-Ger%C3%AAncia-de-Ve%C3%ADculos#abaordemdecarga) é feita uma análise financeira, quantitativa e qualitativa de cada Ordem de Carga;
- A aba [Saída/Chegada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110293-Ger%C3%AAncia-de-Ve%C3%ADculos#abasa%C3%ADda/chegada) é atualizada pela rotina [Controle de Saída/Chegada de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603074-Controle-de-Sa%C3%ADda-Chegada-de-Ve%C3%ADculos). Esse controle é apenas um demonstrativo dos veículos que saíram e retornaram à empresa, informando data e hora de saída e retorno, assim como sua quilometragem;
- Na aba [Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110293-Ger%C3%AAncia-de-Ve%C3%ADculos#abadespesas), é possível visualizar todos os lançamentos através da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) vinculada a uma Ordem de Carga.

Além da possibilidade de análise oriunda da [Gerência de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110293-Ger%C3%AAncia-de-Ve%C3%ADculos), pode-se fazê-lo também através da tela [Controle de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596334-Controle-de-Ve%C3%ADculos). Nesta tela, ao solicitar a visualização do relatório, tem-se o documento de nome **"Demonstrativo de Despesas para Veículo"**, que é basicamente composto pelos mesmos dados da Gerência de Veículos, podendo este ser exibido no formato sintético ou analítico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601774-Controle-de-Ve%C3%ADculos#top)
