---
id: "360045094173"
titulo: "Melhores Práticas para processo 'Venda Entrega Futura'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094173-Melhores-Pr%C3%A1ticas-para-processo-Venda-Entrega-Futura"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:29Z"
rotulos: ["DUVIDANF", "#PUBLIFER", "#revisadohugo", "Configuração", "Nota Fiscal Eletrônica", "Vendas", "CFOP", "Estoque", "Financeiro", "Venda sem entrega imediata", "Financeiro atualizado estoque reserva", "Simples remessa finaliza entrega"]
---

# Melhores Práticas para processo 'Venda Entrega Futura'

O processo de “Venda Entrega Futura”, de forma padrão, será acionado quando a venda é efetuada sem que a entrega do produto seja concretizada de imediato. Considere a emissão de uma nota fiscal eletrônica no ato dessa venda - Venda para entrega futura, onde apenas a atualização do financeiro será gerada, possibilitando que o cliente realize os respectivos pagamentos para efetivação dessa negociação.

A etapa final do processo consiste na entrega e/ou envio da mercadoria para o respectivo parceiro, essa acontecerá quando o estoque desse for disponibilizado, gerando assim a necessidade de emissão de uma nota fiscal de 'Simples Remessa Entrega Futura', que será responsável pela baixa desse estoque, justificando a saída do produto.

**Considere o processo abaixo:**

![Imagem 1: Lançamento de um “ Pedido de venda ” através de uma TOP de pedido com as configurações padrão desse tipo de movimento.…](https://ajuda.sankhya.com.br/hc/article_attachments/19257379488535) Lançamento de um “**Pedido de venda**” através de uma TOP de pedido com as configurações padrão desse tipo de movimento.

![Imagem 2: Lançamento de um “ Pedido de venda ” através de uma TOP de pedido com as configurações padrão desse tipo de movimento.…](https://ajuda.sankhya.com.br/hc/article_attachments/19257368898071) Transformação do “Pedido” em “Nota”: Selecionar o pedido no 'Portal de Vendas', através do botão 'Faturar' selecionar a “**TOP- Z - Venda para entrega futura**”, TOP essa que deverá ter sido previamente configurada considerando a atualização do financeiro.

| - Como se trata de uma das modalidades de venda da empresa, o tipo de movimento para esta TOP é "Nota de Venda". - Deve atualizar o financeiro com uma receita real, pois se trata de um direito real registrado através de uma nota fiscal; - Pode (ou não) reservar estoque, de acordo com o processo da empresa. Se optar por reservar estoque, o estoque deste produto ficará negativo no ato da reserva. Neste caso, a opção **"Validar Estoque p/ Reservar?"**, na aba **"validações"**, deve estar desmarcada para que o sistema não impeça o lançamento desta nota. Além disso, o Tipo de Movimento da operação de Simples Faturamento deve ser **"P - Pedido de Venda"** para permitir a utilização da opção **"Faturar pelo Estoque"** na geração da nota de Simples Remessa; - Não deve permitir alteração após a confirmação, evitando que a Nota Fiscal registrada no sistema seja diferente daquela emitida e entregue ao cliente; - Configurar o campo "Usar como Preço" com a opção "Preço de Venda", pois o valor unitário a ser praticado nas vendas é o Preço de Venda calculado pelo sistema; - Deve atualizar os livros fiscais de saída com as CFOps 5922 e 6922 - Lançamento efetuado a título de simples faturamento decorrente de venda para entrega futura; - Deve calcular impostos incidentes sobre os produtos (ICMS, PIS, COFINS) para que a empresa realize a emissão da nota com todos os impostos incidentes na movimentação; - Como a Nota Fiscal será emitida pela empresa, suas configurações para a impressão devem ser idênticas às indicadas para a TOP de "venda", com Base de Numeração igual a "venda" e Tipo de Numeração igual a "Empresa/série"; - Após a emissão da Nota de Simples Faturamento é realizada a aquisição da mercadoria e será necessário encaminhar a mercadoria para o cliente através da Simples Remessa. Para isto é necessário realizar a configuração de uma restrição para que a única TOP de destino permitida seja a TOP de " Simples Remessa". |
| --- |

![Imagem 3: Lançamento da Simples Remessa, envio da mercadoria vendida anteriormente ao cliente:](https://ajuda.sankhya.com.br/hc/article_attachments/19257379503511) Lançamento da **Simples Remessa,** envio da mercadoria vendida anteriormente ao cliente:

3.1- Deverá ser feita a seleção da nota de venda para entrega futura através do 'Portal de Vendas'.
3.2- Uma vez selecionada a nota de venda, deverá ser utilizado o botão **'Dev./Est.'.**

3.3- O sistema irá solicitar alguns dados, tais como data, série e TOP.

3.4- No campo TOP, deverá ser utilizada uma TOP de remessa: “**TOP - W - Simples Remessa Entrega Futura**”, atualizando somente o estoque.

| - Como se trata de uma das modalidades de venda da empresa, o tipo de movimento para esta TOP é "Nota de Venda", representando a última parte do processo de Venda para entrega futura. - Não deve atualizar o financeiro, pois esta atualização já foi realizada no movimento de simples faturamento. - Deve atualizar estoque como uma saída, pois o produto será enviado ao cliente; - Não deve permitir alteração após a confirmação, evitando que a Nota Fiscal registrada no sistema seja diferente daquela emitida e entregue ao cliente; - Configurar o campo "Usar Preço" com a opção "Preço de Venda", pois o valor unitário a ser praticado nas vendas é o Preço de Venda calculado pelo sistema, da mesma forma que para as demais operações do processo de Vendas (vide Obs.); - Deve atualizar livros fiscais de saída com as CFOPs 5117 e 6117 - Venda de mercadoria adquirida ou recebida de terceiros, originada de encomenda para entrega futura; - Deve calcular impostos incidentes sobre os produtos (ICSM, PIS E COFINS) para que a empresa realize a emissão da nota com todos os impostos incidentes na movimentação; - Como a Nota Fiscal será emitida pela empresa, suas configurações para a impressão devem ser idênticas às indicadas para a TOP de "venda", com Base de Numeração igual a "venda" e Tipo de Numeração igual a "Empresa/série"; |
| --- |

**Importante:**

1. Informações fiscais e CFOP'S referentes aos três 'Tipos de Operação' mencionados, deverão ser validados junto ao Contador da empresa.
2. Ressaltamos que as configurações citadas acima são de um processo padrão, que podem não atender ao processo da sua empresa. Por isso é importante que diante necessidade de validações e parametrizações de um novo processo, um consultor de serviços  de sua Unidade seja acionado.
