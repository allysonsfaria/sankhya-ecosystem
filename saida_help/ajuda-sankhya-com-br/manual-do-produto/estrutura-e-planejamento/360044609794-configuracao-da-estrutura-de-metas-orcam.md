---
id: "360044609794"
titulo: "Configuração da Estrutura de Metas/Orçamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos"
trilha: "Manual do Produto > Inteligência e Análise > Metas e Orçamentos > Estrutura e planejamento"
atualizado_em: "2026-09-23T18:07:34Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "br.com.sankhya.cfg.config.estrutura.meta.orcamento", "Configuração da Estrutura de Metas/Orçamentos manual", "TOP", "Financeiro", "VALCOMPORCAPR", "Configuração e propriedades", "Aprovação e liberação", "Metas e orçamentos comerciais", "Comercial", "Metas e Orçamentos"]
---

# Configuração da Estrutura de Metas/Orçamentos

```
 Módulo: Metas e Orçamentos
```

---

Esta rotina permite que você controle e acompanhe as Metas Comerciais e Orçamentos Financeiros através da análise e comparação entre o valor previsto e o realizado. Esse planejamento pode ser feito por diversos critérios de acordo com as necessidades de cada empresa.

O campo **"Código"** será alimentado de forma automática.

No campo **"Descrição da Meta"** informe o nome que identificará a meta.

![Imagem 1: Essa tela será apresentada para utilização no Sankhya-Om, apenas se a empresa possuir em sua licença o produto 30742 -…](https://ajuda.sankhya.com.br/hc/article_attachments/16347346335511) Essa tela será apresentada para utilização no Sankhya-Om, apenas se a empresa possuir em sua licença o produto 30742 - CONTROLE ORÇAMENTÁRIO E METAS/W e no Jiva Evo, o produto 20422 - JIVA - CONTROLE ORÇAMENTÁRIO E METAS.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abageral) |  | [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades) |
| --- | --- | --- |
| [Aba TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abatop) |  | [Aba Liberação Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abaliberaoplanejamento) |
| [Aba Restrições por natureza](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abarestriespornatureza) |  | [Aba Campos Substitutos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abacampossubstitutos) |
| [Aba Limitações (Intervalo Único)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abalimitaesintervalonico) |  |  |

![Imagem 2: Aba Limitações (Intervalo Único)](https://ajuda.sankhya.com.br/hc/article_attachments/1500000217301)

## Aba Geral

Você irá configurar aqui os campos responsáveis por iniciar o cadastro da estrutura de cada meta ou orçamento.

No campo **"Tipo de Meta"** defina qual será a categoria de meta a ser criada, sendo elas:

- Comercial;
- Financeira.

Quando o Tipo de Meta for Comercial, será exibida na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades) a marcação **"Meta por quantidade"**.

**Observação:** para metas do tipo Financeira, é possível cadastrar TOP's que não geram impacto financeiro. Nesses casos, é necessário configurar o campo **"Receita/Despesa"** localizado na aba [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abatop), informando a equivalência do Tipo de Operação - TOP no contexto da meta.

Além disso, como as notas que não envolvem fluxo financeiro não têm vínculo direto com o financeiro, caso o campo **"Tipo de Data"** na aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades) esteja configurado como **"Baixa"**, **"Vencimento"** ou **"Movimento"**, será utilizada a data de **"Negociação"**.

Por meio da opção **"Ativo"** você indicará se a meta está habilitada ou não.

A data em que foi feita a aprovação da meta/orçamento será descrita no campo **"Data da Aprovação"**.

Por meio do campo **"Cód. Usuário Aprovação"** teremos o apontamento do usuário que validou a meta/orçamento.

O campo **"Cód. Meta anterior"** tem seu preenchimento automático, a numeração da meta anterior é exibida aqui.

**Nota:** os campos Data da Aprovação, Cód. Usuário Aprovação e Cód. Meta anterior não possuem funcionalidade no Sankhya-Om, somente para o MGE.

A opção **"Considerar componentes"** permite definir se na atualização do realizado o sistema irá considerar ou não os **"Componentes do produto"** (KIT) no cálculo do realizado.

Com a marcação **"Valida alteração do período em vigor"** acionada, não será permitida a alteração das metas para o mês atual e meses anteriores. Ou seja, mesmo que não haja dados registrados para a meta, o sistema não realizará a importação de dados para esses meses, pois as informações passadas não podem ser modificadas.

**Observação:** quando a marcação Valida alteração do período em vigor estiver ligada e o campo **"Periodicidade"** na aba [Prioridades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades) estiver configurado como **"Mensal"**, ao realizar a importação na tela [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814-Planejamento-de-Metas-Or%C3%A7amentos), o sistema limpará os valores que estão sendo importados. Para permitir a importação, a marcação Valida alteração do período em vigor deve estar desligada. Nesse caso, se houver dados existentes, o sistema substituirá todas as informações do mês atual e dos meses passados.

A marcação **"Ignora orçamento não previsto"** quando realizada, permitirá definir se o aviso de não planejamento orçamentário será ou não apresentado nas Centrais.

**Observação:** quando essa marcação for efetuada, e existir campos significativos, apenas existirá validação destes campos que tiveram planejamento, caso não haja planejamento, não será emitido alerta de falta de previsão orçamentária ou solicitação de liberação de orçamento.

**Nota:** para que o sistema não apresente o pop-up de **"Solicitação de Liberação de Orçamento"** ao realizar o cadastro de títulos por meio da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), você deverá ligar o parâmetro **"Considera orçamento zerado como não previsto?- METZERONAOPREV"**. Assim, com este parâmetro ligado, ao criar uma movimentação financeira, os itens referentes ao Planejamento de Metas/Orçamento serão desconsiderados caso não tenham sido preenchidos.

**Importante:** quando a soma dos campos (PREVDESP + SUPLEMENTODESP + ANTECIPDESP + TRANSFDESP + TRANSFSALDODESP - REDUCAODESP) da tabela Metas/Orçamentos (TGMMET) for igual a zero, o parâmetro Considera orçamento zerado como não previsto? - METZERONAOPREV não irá validar a liberação de Orçamentos. Você pode verificar se será validada com a seguinte query:

```
SELECT PREVDESP + SUPLEMENTODESP + ANTECIPDESP + TRANSFDESP + TRANSFSALDODESP
 - REDUCAODESP TOTPREV
FROM TGMMET MET
WHERE MET.CODMETA = 32
AND MET.DTREF = '01/01/2022'
AND MET.CODEMP = 0
AND MET.CODGER = 0
AND MET.CODVEND = 0
AND MET.CODCENCUS = 0
AND MET.CODNAT = 0
AND MET.CODREG = 0
AND MET.CODPROJ in (20000605) --10001602,
AND MET.CODPARC = 0
AND MET.CODCID = 0
AND MET.CODUF = 0
AND MET.CODPAIS = 0
AND MET.CODTIPPARC = 0
AND MET.CODGRUPONAT = 0
```

**Observação:** caso exista na lista de campos significativos o campo **"Empresa"**, o alerta será disparado apenas para a empresa que houver o planejamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba Propriedades

Nessa aba, são configuradas as propriedades de um orçamento ou meta.

![Imagem 3: Nessa aba, são configuradas as propriedades de um orçamento ou meta.](https://ajuda.sankhya.com.br/hc/article_attachments/1500000218841)

Indique no campo **"% p/avisar antes de exceder a Despesa"** a porcentagem a ser considerada para que seja avisado antes que se exceda a Despesa.

A marcação **"Usar valor Bruto"** pode ser utilizada somente em metas financeiras. De forma que, as metas comerciais usam o valor da nota e não irá atualizar o realizado por meio do valor bruto.

![Imagem 4: Para o cálculo do compromisso orçamentário , a marcação Usar valor Bruto não é considerada.](https://ajuda.sankhya.com.br/hc/article_attachments/16347346335511) Para o cálculo do compromisso orçamentário, a marcação Usar valor Bruto não é considerada.

Desse modo, as metas financeiras utilizam os valores de desdobramento do financeiro e está preparado para somar os valores de outros impostos do cabeçalho da nota e do financeiro. Porém, se o parâmetro **"Considerar impostos retidos no valor da nota? - CONSIMPRETNOTA"** estiver ligado, o sistema irá aplicar os valores de ISS e INSS, quando retidos, além do IRF.

O campo **"Quando exceder a Despesa Prevista"** é utilizado para controlar os lançamentos que excedem a previsão no orçamento. São disponibilizadas as seguintes opções:

- **Avisar e Não aceitar o lançamento:** Por esta opção, não será permitido efetuar um lançamento de despesas acima do valor previsto;
- **Avisar e Aceitar o lançamento:** Quando essa opção for selecionada, teremos a autorização de se efetuar o lançamento mesmo quando o previsto for excedido. Sendo que, nesse caso é emitida uma mensagem informando que as previsões estão sendo ultrapassadas.
- **Não Avisar e Aceitar:** Esta opção tem a mesma funcionalidade da anterior, diferenciando apenas que, nesta situação a mensagem não será emitida, impedindo assim que se visualize quando as previsões forem excedidas.
- **Exigir Liberação SEMPRE, mesmo que não exceda o orçamento:** Caso está opção seja selecionada, sempre que for lançado um movimento com Tipo de Operação - TOP configurado no orçamento será solicita a liberação deste, independente de ultrapassar o orçado.

**Nota:** este campo será empregado somente para orçamentos.

No campo **"Periodicidade"** é configurado o intervalo de tempo em que os dados serão agrupados para análise da meta. Teremos as seguintes opções:

- Diário;
- Semanal;
- Intervalo Único;
- Anual;
- Semestral;
- Quadrimestral;
- Mensal;
- Bimestral;
- Trimestral.

**Importante:** ao utilizar a opção Diário do campo Periodicidade, não será possível fazer o uso das opções **"Cenários"** do botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#botaooutrasopes) e do botão **"Comparar Cenários"** localizado no pop-up Cenários da tela [Planejamento Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814), devido ao grande volume de dados.

**Observação:** não é possível utilizar as opções **"Copiar planejamento anterior"** e **"Importar Planilha"** se as opções Diário e Semanal do campo Periodicidade forem utilizadas.

Por meio do campo **"Tipo de Data"** informe em qual evento os dados que compõe a meta/orçamento serão filtrados, agrupados e atualizados.

**Nota**: A opção "Intervalo Único" no campo Periodicidade não está funcional no Sankhya Om (W). Esta configuração é um remanescente da versão MGE e, ao ser utilizada com Metas do tipo Financeiro, o sistema retornará o erro: “**Sistema não preparado para utilizar tipo de meta Financeiro e Periodicidade Intervalo Único (CORE\_E00978)**”.

**Observação:** quando o parâmetro **"Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI"** estiver habilitado e for criado um orçamento/meta nessa tela, considerando que o campo acima esteja com a opção **"Entrada/Saída"** selecionada, ao lançar um registro nas Centrais de Notas ou na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), o sistema obrigará que a Data de Entrada/Saída seja maior ou igual a Data de Negociação, após de planejadas e executadas as operações, será realizada a [Atualização do Realizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609774), assim, será feita a atualização deste, considerando também, a Data de Entrada/Saída dos documentos.

O campo **"Produtos por"** é utilizado somente para metas do tipo Comercial e caso o campo Produto seja significativo para a meta, pode-se definir dentre a opção **"Quantidade"** ou **"Peso bruto"**.

O campo **"Tipo de Valor"** não possui funcionalidade no Sankhya-Om, somente para o MGE.

O campo **"Data início"** permite a flexibilização do ciclo de orçamento, ou seja, você poderá escolher quando o ciclo irá se iniciar, de janeiro à dezembro. Considere o exemplo:

caso você deseje começar o ciclo em Março, o período considerado no [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814) será de Março à Fevereiro do ano seguinte porém, a apresentação dos dados relativos à meta continua anual na tela Planejamento de Metas/Orçamentos; sendo assim, para configurar o ciclo é necessário navegar entre os anos.

**Nota:** o campo Data início ficará indisponível para utilização caso o campo Periodicidade seja diferente de **"Mensal"**.

**Observação:** esta flexibilização do ciclo de orçamento apenas atenderá as metas comerciais; as metas contábeis ([Config. do Controle Orçam. Contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607754)) ainda não estão preparadas para esta flexibilização.

Quando a marcação **"Ver código com a descrição no Planejamento"** for acionada, indicará que os Campos Disponíveis que forem indicados como Significativos, terão seu código e sua descrição apresentados juntamente no [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814). Caso esteja desligada, somente a descrição será apresentada.

Além disso, teremos também as colunas **"Campos Disponíveis"** e **"Campos Significativos"** que permitem selecionar quais campos farão parte da estrutura de detalhamento da Árvore de Planejamento.

**Configuração para Metas por Executante** 

Caso a meta utilize apenas o campo significativo Executante, para que o sistema consiga montar a estrutura da grade no Planejamento, é necessário que na tela Vendedores/Compradores exista pelo menos um registro ativo configurado com o Tipo "Executante". Sem registros válidos nesta condição, o sistema retornará erro de estrutura de grade ([CORE\_E02491]).

**![Imagem 5: Configuração para Metas por Gerente](https://ajuda.sankhya.com.br/hc/article_attachments/34108059600791) Configuração para Metas por Gerente**

Para que o sistema consiga apurar o realizado corretamente quando a meta é detalhada por gerente, é **obrigatório** que o campo `Vendedor` também seja selecionado na lista de **Campos Significativos**. O sistema utiliza a estrutura de vendedores para vincular cada valor ao gerente correspondente. A configuração de uma meta **exclusivamente por gerente** (sem `Vendedor` ou `Executante`) não irá funcionar, e os valores serão consolidados em um único registro.

A marcação **"Meta por quantidade"** será exibida quando na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abageral), o campo Tipo de Meta estiver com a opção Comercial selecionada, assim será possível definir se a meta será por valor ou por quantidade.

**Nota:** caso a marcação seja efetuada, será demonstrada na tela [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814) as quantidades previstas e realizadas, sendo que, o número de casas decimais visualizadas é o número definido no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

**Observação:** caso você adicione os campos **"Parceiro"** e **"Nome Parceiro"** na grade Campos Substitutos, as informações destes campos serão levados para as referidas colunas na tela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba TOP

Nessa aba são definidos os Tipos de Operações - TOP que serão considerados para atualizar o realizado das metas ou orçamentos. Sendo que você poderá utilizar somente aqueles que se encontrarem ativos.

![Imagem 6: Nessa aba são definidos os Tipos de Operações - TOP que serão considerados para atualizar o realizado das metas ou…](https://ajuda.sankhya.com.br/hc/article_attachments/360101316493)

No campo **"Cód.Tipo Operação"** indique o Tipo de Operação - TOP que será utilizado.

Por meio do campo **"Receita/Despesa"** aponte se a operação atualizará Receitas, Despesas ou se serão empregadas as atualizações do Tipo de Operação - TOP (Usar da TOP) nas metas que a utilizam. Quando a opção **"Usar da TOP"** for selecionada, o sistema verificará no [Cadastro de Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba **"Geral"**, os campos **"Atualização do Estoque"** e **"Atualização estoque MP"**, conforme a configuração destes executará os seguintes procedimentos:

- Tipo de Operação - TOP de Venda e Pedido de Venda: A opção **"Baixar"** selecionada, a Receita será atualizada.
- Tipo de Operação - TOP de Compra e Pedido Compra: Com a opção **"Entrar"** indicada, tem-se a atualização da Despesa.
- Tipo de Operação - TOP de Devolução de Compra: Quando a opção **"Baixar"** for apontada, o sistema atualizará Receita.
- Tipo de Operação - TOP de Devolução de Venda: Se a opção **"Entrar"** estiver configurada, a Despesa será atualizada.

**Observação:** quando for indicada uma TOP de Requisição no campo Cód.Tipo Operação, o campo Receita/Despesa só terá influência na estrutura de metas quando houver financeiro e forem selecionadas as opções **"Receita"** ou **"Despesa"**.

**Observação:** TOP's do tipo **"J - Pedido de requisição"** sempre deverão ser marcadas como **"Sim"**, porque devem ser consideradas como compromisso.

Caso a meta seja do tipo **"Financeiro"**, o sistema irá analisar no Cadastro de Tipos de Operação -TOP, aba **"Geral"**, os campos **"Financeiro"** e **"Atualização do Financeiro"** e executará o mesmo procedimento citado acima levando em consideração o financeiro.

A marcação **"Compromisso"** tem a função de gerar uma obrigação no orçamento para movimentações que geram provisões. Este valor é equivalente a uma **"Reserva"** do **"valor previsto"**, dessa forma se uma requisição não puder ser totalmente atendida dentro do orçamento, ela não será confirmada. Portanto, compromissos são valores de orçamento já aprovados de **"Compras"** e **"Requisições"**, aguardando a entrega de Notas Fiscais.

**Observação:** quando habilitado, o parâmetro **"Valida Somente Compromissos Aprovados? - VALCOMPORCAPR"** irá considerar somente os pedidos confirmados para a composição do compromisso.

Além disso, no Cadastro de Tipos de Operações - TOP, botão **"Outras Opções"**, a opção **"Metas/Orçamentos"** quando acionada apresentará um pop-up que possibilitará a vinculação da TOP em uma Meta/Orçamento de maneira rápida e facilitada.

**Observação:** metas ativas que possuem a marcação **"Compromisso"** habilitada e ainda com o campo **"Produtos por"** (aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abapropriedades)) definido como **"Peso Bruto**" não podem ser utilizadas em um **"Pedido de Requisição"** com o [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) configurado com o **"Tipo de Movimento"** igual a **"J-Pedido de Requisição"**, ou para um **"Pedido de Compra"** ou **"Nota de Compra"** que possua o Tipo de movimento como **"O-Pedido de Compra"** e/ou **"C-Compra"**, com as seguintes definições:

- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), possua o campo **"Financeiro"** preenchido como **"Despesas"** e a marcação **"A nota fica como pendente"** esteja habilitada;
- Na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) o campo **"Atualização do financeiro"**  selecionado com a opção **"Provisionar"**.

Do contrário será exibido o aviso:

**"Existe(m) Meta(s) ativa(s) configurada(s) para controle do produto pelo 'PESO BRUTO', e não pode(m) ser utilizada(s) em Pedido de Requisição ou em Pedido/Nota que esteja PENDENTE e PROVISIONE uma despesa no financeiro."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba Liberação Planejamento

Por meio dessa aba, informe o(s) responsável(is) pela aprovação e liberação de metas e/ou orçamentos.

![Imagem 7: Por meio dessa aba, informe o(s) responsável(is) pela aprovação e liberação de metas e/ou orçamentos.](https://ajuda.sankhya.com.br/hc/article_attachments/360101317733)

**Importante:** apenas um único usuário liberador realizará a liberação, ou seja, não existe a possibilidade de uma **"liberação dupla"**, a partir do momento em que um dos responsáveis aprovar o orçamento, o mesmo já estará válido.

Quando tivermos um usuário cadastrado nesta aba, na tela [Planejamento de Metas/Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814), o botão **"Confirmar planejamento"** terá seu nome alterado para **"Solicitar aprovação"**, e a meta apenas será efetivada se o usuário vinculado acessar a tela [Aprovação Planejamento Orçamentário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107353) e liberar a meta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba Restrições por natureza

Por meio dessa aba, configure as exceções por **"Natureza"** que visam permitir ou proibir a **"Suplementação"**, **"Transferência"** ou **"Antecipação"** de metas.

**Observação:** esta aba será exibida para as metas e orçamentos que tiverem na aba **"Propriedades"**, o campo **"Natureza"** selecionado como **"Campos Significativos"** e se um dos parâmetros abaixo estiverem configurados:

**NIVAPROVSUPL - Nível p/Aprov. Suplementação de Orçamento**;

**NIVAPROVANTECIP - Nível p/Aprov. Antecipação de Orçamento**;

**NIVAPROVTRANSF - Nível p/Aprov. Transferência de Orçamento**.

![Imagem 8: NIVAPROVTRANSF - Nível p/Aprov. Transferência de Orçamento .](https://ajuda.sankhya.com.br/hc/article_attachments/1500000205602)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba Campos Substitutos

Esta aba é empregada para configurar os lançamentos que serão empregados em registros analíticos e resumidos nos registros sintéticos.

![Imagem 9: Esta aba é empregada para configurar os lançamentos que serão empregados em registros analíticos e resumidos nos…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000218361)

Os **"Campos Disponíveis"** serão configurados através da aba **"Propriedades"** desta tela.

Ao clicar no botão **"Cadastrar Campo Substituto"**, o campo acima mencionado será disponibilizado com as opções configuradas anteriormente.

No campo **"Campos Substitutos"** informe a **"Função"** que fará a ligação à tabela desejada. Para isto, utilize as seguintes regras:

- Quando o campo **"Tipo de Meta"**, localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#abageral) dessa tela, encontrar-se com a opção **"Comercial"** selecionada, os Campos Disponíveis e Campos Substitutos devem ser registrados, respectivamente, da seguinte forma:

Centro de resultado = TGFCAB.CODCENCUS

Natureza = TGFCAB.CODNAT

Projeto = TGFCAB.CODPROJ

Vendedor = TGFCAB.CODVEND

Parceiro = TGFCAB.CODPARC

Empresa = ITE.CODEMP

Controle = ITE.CONTROLE

Local = ITE.CODLOCALORIG

Produto = ITE.CODPROD

Vendedor Item = ITE.CODVEND

Executante = ITE.CODEXEC

Grupo de Produtos = PRO.CODGRUPOPROD

Marca = PRO.MARCA

- Quando o campo Tipo de Meta, localizado na aba Geral desta tela, encontrar-se com a opção **"Financeira"** selecionada, os Campos Disponíveis e Campos Substitutos devem ser registrados, respectivamente, da seguinte forma:

Empresa = FIN.CODEMP

Centro de resultado = FIN.CODCENCUS

Natureza = FIN.CODNAT

Projeto = FIN.CODPROJ

Vendedor = FIN.CODVEND

Parceiro = FIN.CODPARC

Grupo Natureza = TGFNAT.CODGRUPONAT

- Em ambas as metas, os campos desta aba deverão ser registrados conforme a seguir:

Gerente = TGFVEN.CODGER

Região = PAR.CODREG

Cidade = PAR.CODCID

Estado (UF) = CID.UF

País = UFS.CODPAIS

Perfil principal = PAR.CODTIPPARC

**Nota:** ao lançar uma natureza analítica, o sistema fará o cálculo de validações, o campo Campos Substitutos fará o cálculo por meio do campo **"Grau"** para tornar o Centro de Resultado sintético. Baseando-se nesta consideração, teremos o seguinte exemplo:

Ao utilizar o Campo Substituto = (ROUND(CAB.CODCENCUS/100000,2)\*100000) e Grau 5 temos o resultado:
**Centro Resultado:** 3 1 02 3 01 00
**CR CALCULADO PELO CAMPO Subst:** 3 1 02 0 00 00
**CR CALCULADO PELO GRAU** = 5 : 3 1 02 3 00 00

**Importante:** o Grau informado nesta aba deve ser sempre o resultado do campo substituto, para melhor compreensão considere o seguinte exemplo:

Para utilizar o Grau 3, o campo substituto deverá ser:

```
TRUNC(FIN.CODNAT/100)*100
```

Já para utilizar um Grau 1, o campo substituto deverá ser:

```
TRUNC(FIN.CODNAT/100000)*100000
```

E assim sucessivamente.

Utilizando a máscara 99\.99\.999;0, por exemplo, temos que:

- Grau 2 = 5 zeros
- Grau 1 = 7 zeros

Ou seja, se tivessemos uma máscara com 4 Graus, teriamos que:

**(1)** 99.\99\.99\.99;0

- Grau 2 = 4 zeros
- Grau 3 = 6 zeros
- Grau 4 = 8 zeros

![Imagem 10: Temos uma função nativa para truncar valores em bancos SQL Server , sendo a "SNK_TRUNC" . Utilize ela dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/16347346335511) Temos uma função nativa para truncar valores em bancos SQL Server, sendo a **"SNK\_TRUNC"**. Utilize ela dessa forma:

```
(SANKHYA.SNK_TRUNC(TGFCAB.CODCENCUS/1000000,2)*1000000)
```

**![Imagem 11: Regras de Ligação para Campos de Metas](https://ajuda.sankhya.com.br/hc/article_attachments/34108059600791) Regras de Ligação para Campos de Metas**

Em ambas as metas (Comercial ou Financeira), os campos desta aba deverão ser registrados conforme a seguir:

- `Gerente = TGFVEN.CODGER`

**Observação:** Para que a apuração por gerente funcione corretamente, o campo `Vendedor` (ou `Executante`) deve estar configurado como um **Campo Significativo** na aba `Propriedades`. Isso garante que o sistema possa inferir o código do gerente a partir da tabela de vendedores (`TGFVEN.CODGER`).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)

## Aba Limitações (Intervalo Único)

Utilize essa aba para controlar os gastos geralmente de uma determinada obra, utilizando uma meta financeira, como por exemplo a compra de materiais utilizados na obra e despesa prevista de produtos, tendo a opção período personalizada, com flexibilidade de prorrogação desse período.

![Imagem 12: Utilize essa aba para controlar os gastos geralmente de uma determinada obra, utilizando uma meta financeira, como por…](https://ajuda.sankhya.com.br/hc/article_attachments/360066073414)

**Observação:** essa funcionalidade foi criada para trabalhar unicamente com TOPs de Compra, Pedido de Compra, Devolução de Compra e Financeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609794-Configura%C3%A7%C3%A3o-da-Estrutura-de-Metas-Or%C3%A7amentos#top)
