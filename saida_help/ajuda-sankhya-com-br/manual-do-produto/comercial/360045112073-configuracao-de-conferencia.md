---
id: "360045112073"
titulo: "Configuração de Conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:31:26Z"
rotulos: ["AJUDA DO SKW", "manual", "Conferência", "Configuração", "FREPBASEFOLDER", "Fila", "Faturamento", "Entrega", "Divergência", "TOP", "Estoque", "Corte", "Fila de Conferência", "CNFIGNCONTLOTE", "Conferência de Pedidos nas Docas", "Configuração de Conferência", "Confirmação", "CONFPARCIALVOL", "Corte de pedido (Conferência)", "Divergente", "Evento 64", "Exibe código de barras dos produtos do pedido", "Liberar para conferência", "Momento da conferência", "Notas Conferidas", "Recontagem", "Utiliza conferência parcial de volumes", "Utiliza conferência parcial de volumes?", "br.com.sankhya.com.cad.configuracao.conferencia", "Configuração de Conferência manual", "Configuração de Conferência: Detalhes e Funcionalidades", "Comercial"]
---

# Configuração de Conferência

```
 Módulo: Comercial > Configuração
```

---

Por meio desta tela você realizará a configuração para a conferência dos produtos, considerando as marcações realizadas para este procedimento em cada TOP. A tela objetiva também tornar mais simplificada, a configuração de Conferência de Produtos por Código de Barras.

Abaixo poderemos acessar as configurações acerca desta tela.

| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#PainelPrincipal) |  | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral) |
| --- | --- | --- |
| [Aba Corte/Divergência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abacortedivergncia) |  | [Aba Formação de volumes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abaformaodevolumes) |
| [Processo de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#processodeconferncia) |  | [Exclusão de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#exclusodeconferncia) |
| [Exclusão de Notas Conferidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#exclusodenotasconferidas) |  | [Parâmetros que influenciam nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#parmetrosqueinflunciamnestarotina) |

---

## Painel Principal

![Imagem 1: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/5541515153303)

Inicialmente, no campo **"Descrição"** determinará a nomenclatura da configuração de conferência que está sendo cadastrada.

Em seguida, teremos o **"Nro único"**, que corresponde à chave da configuração de conferência que está sendo realizada. Este campo pode ser alimentado de forma manual ou automática; esta definição é feita pelo botão ![Imagem 2: Em seguida, teremos o "Nro único" , que corresponde à chave da configuração de conferência que está sendo realizada.…](https://ajuda.sankhya.com.br/hc/article_attachments/16343257723415) **"Configuração da tela"** localizado no lado superior direito da tela.

**Botão Coletor**

Ao acionar o botão **![Imagem 3: Ao acionar o botão "Coletor" , você poderá consultar as configurações de conferência não suportadas pelo coletor. São…](https://ajuda.sankhya.com.br/hc/article_attachments/16082736065175) "Coletor"**, você poderá consultar as configurações de conferência não suportadas pelo coletor. São elas:

- Exibir imagem do produto;
- Exibe código de barras dos produtos do pedido;
- Abrir Fila de Conferência ao faturar;
- Abrir nota faturada na finalização da conferência;
- Inibir mensagem de confirmação ao finalizar conferência;
- Exige identificador do produto;
- Registrar peso;
- Sempre apresentar na fila de conferência;
- Conferência por série;
- Aceita múltiplas entregas;
- Formação de volumes. Apenas a opção Registro simplificado (no final) está disponível no coletor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Aba Geral

![Imagem 4: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/5541146460567)

**Importante:** ao realizar a conferência é necessário que você utilize a mesma unidade utilizada durante a negociação. Por exemplo, ao realizar uma negociação com a opção **"Unidade Alternativa"**, o processo de conferência deverá ser realizado nesta mesma unidade. Caso contrário o sistema ira emitir a mensagem:

**"Quantidade conferida maior do que quantidade negociada no pedido/nota."**

Por meio da opção **"Momento da Conferência:"** será definido quando será realizada a conferência; nesta temos duas possibilidades de escolha:

- **Antes de faturar:** Será exigida a conferência dos itens somente ao **"Faturar"** o Pedido, ou seja, o Pedido só poderá ser faturado, se a conferência dos itens estiver finalizada.
- **Antes da confirmação:** Se configurada será exigida a conferência dos itens ao **"Confirmar"** o pedido/nota. Isto é, a confirmação da nota ou pedido, somente poderá ser feita, se a conferência estiver finalizada.

Em **"Buscar código de barras por:"** ao fazer a conferência, o sistema irá utilizar esse campo para identificar onde procurar o **"Produto"** através do código de barras. Segue as opções:

- **Automático:** O Produto será localizado através da seguinte ordem:

1°- Pelo campo **"Cód. de Barras"** da aba **"Estoque"**.

2º- Pelo campo **"Código de Barras"** da aba **"Unidades Alternativas"** ou pelo campo Cód. Barras da aba Código de barras, desde que tenha-se o campo "Unidade de volume" informado.

3º- Pelo campo **"Referência"** do cadastro de produto ou pelo campo Cód. Barras da aba Código de barras, que **não tenha** Unidade de volume informada ou cuja Unidade de volume seja a mesma do produto.

- **Código do produto:** c**aso esta opção esteja configurada, ao realizar a conferência, será realizada a busca do** **"Código de barras"** **(bipado na fila de conferência) igual ao código do produto.**
- **Referência:** o sistema pesquisará pelo campo Referência, do Cadastro de Produtos ou pelo campo Cód. Barras da aba **"Código de barras"** (também no Cadastro de Produtos) que **não tenha** "Unidade de Volume" informada ou que a "Unidade de Volume", seja **a mesma do produto**.
- **Unidade alternativa:** a pesquisa será feita pelo campo **"Código de Barras"** da aba **"Unidades Alternativas"** ou pelo campo Cód. Barras da aba Código de barras, que tenha o campo **"Unidade de Volume"** informado e **que seja diferente** da Unidade de Volume do produto.
- **Estoque:** a busca será feita pelo campo Cód. de Barras da aba Estoque (Cadastro de Produtos).

No campo **"Tipo de contagem:"** existem três opções de escolha para a definição do tipo de contagem, que são:

- **Contagem única por produto:** Será apresentado na tela de **"Conferência"** o campo **"Quantidade"**, para que seja possível informar a quantidade que está sendo conferida.
- **Contagem cumulativa com quantidade:** Caso esta opção esteja selecionada o sistema deixará habilitado o campo Quantidade no painel de conferência (aberto através da [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)). Ao fazer uma conferência de um pedido ou nota que utilize essa opção e caso já exista um produto igual já conferido o sistema apenas irá somar as quantidades; por padrão é sugerida a quantidade 1 (um).
- **Contagem cumulativa:** Por esta opção, apenas informe o **"Código de Barras"** e o sistema considerará a quantidade como 1. Tem-se como exemplo, os caixas de supermercado que a cada bipe conta-se 1 produto.

**Nota:** o parâmetro **"Pode alterar Qtd. Conferida na Contagem Cumulativa - ALTQTDCONF"** quando habilitado, permitirá a alteração da quantidade de itens conferidos mesmo quando o campo Tipo de contagem se encontrar configurado com a opção **"Contagem cumulativa"**.

**Observação:** a configuração efetuada no campo Tipo de contagem será aplicada para todos os produtos. Para configurar o tipo de contagem de forma específica para um produto, deve-se configurar nos [Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba **"Geral"**, o campo Tipo de contagem.

A marcação **"Detalhar lote pela conferência"** permitirá que os lotes dos produtos sejam determinados pela conferência. Isso acontece no momento do faturamento do pedido. Essa opção não pode ser utilizada ao trabalhar-se com documentos de entrada (Pedidos e Notas de Compra). 

**Importante:** em sintonia com essa marcação, tem a configuração dos seguintes parâmetros:

- **Permite ignorar controle por lote na conferência - CNFIGNCONTLOTE:** Deverá estar desligado.
- **Utiliza a coluna Controle para controle o estoque - UTILIZACONTROLE:** Deverá estar ativado;
- **Controle Automático por data de validade de lote? - LOTAUTCENT:** Deve ser ativado.

#### Seção Regras Gerais

A marcação **"Conferência por série"**, quando selecionada, fará com que na rotina de [Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia) seja feita a captura da série. Desta forma, será possível que o conferente informe o número da série para os produtos que são controlados por série, podendo informar 1 ou **"N"** número de séries. Veja sobre a funcionalidade no link [Apontar Número de Série pela Conferência (entrada e saída)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047392914).

Ao efetuar a marcação **"Ignorar componentes de Kit:"** não serão exibidos os componentes do Kit na grade Itens do Pedido na tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia); além disso, nesta mesma tela, não serão exibidos os componentes do Kit, na grade Produtos divergentes na Conferência, do botão **"Produtos Divergentes"**. Pelo fato da conferência ser feita apenas pelo código de barras do Kit, pode-se melhor entender a interferência desta marcação.

Por meio do campo **"Exige identificador do produto:"**, é feita a definição se ao proceder com a Conferência será solicitada ou não a inclusão de identificadores. Tem-se as seguintes opções:

- **Exige todos (opcionalmente):** Através desta opção, caso no documento conferido exista ao menos um produto que possua identificadores de conferência, será apresentado o seguinte questionamento, **"Deseja informar os identificadores de produto?"**; caso afirmativo, realiza-se a inclusão do identificador.
- **Exige Todos:** Por esta opção, será necessário incluir todos os identificadores dos produtos para conclusão da Conferência.
- **Exige um:** Através desta opção, será exigida a inserção de apenas um dos identificadores dos produtos para seguimento no processo de Conferência.
- **Não exige:** Ao definir o campo com esta opção, não será exigida a inclusão de nenhum identificador para andamento no processo de conferência.

Referente à marcação **"Proibe alt. documento em conferência"**, uma vez que o pedido foi liberado para conferência e o status do mesmo consta **"Em andamento"** ou **"Recontagem em andamento"**, caso esta marcação esteja acionada o sistema não permitirá que sejam efetuadas alterações nos itens da nota, como por exemplo modificar a quantidade dos itens, excluir ou adicionar um item, mudança de local, entre outros.

O mesmo se aplica para as importações realizadas pelo [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML). Portanto, considerando um documento importado com status de conferencia igual a Em andamento ou Recontagem em andamento, ao clicar em excluir ou liberar para reprocessamento, a seguinte mensagem será apresentada:

**"O documento Nro. único XXX, não pode ser alterado, pois existe uma conferência em andamento. Código: CORE\_E01881"**

A marcação **"Abrir Fila de Conferência ao faturar:"** só estará habilitada quando o campo **"Momento da conferência"** estiver configurado com a opção **"Antes de faturar"**. Quando acionada, ao realizar o faturamento de um pedido de venda, tem-se a abertura automática da tela Fila de Conferência para que seja realizada a conferência do referido pedido.

Para tanto, o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado no lançamento do pedido de venda necessita estar configurado para realizar a conferência (aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), marcação **"Exige conferência"**).

Juntamente com estas configurações, temos as marcações **"Faturar ao concluir conferência"** e **"Abrir nota faturada na finalização da conferência"** que quando configuradas, na finalização da conferência caso o faturamento tenha ocorrido sem erros, automaticamente tem-se a exibição da Central de Vendas posicionada na nota que foi gerada.

#### Comportamento da interface

| ⚠️**Importante!** Com esta opção ligada, a paginação é desabilitada para que todos os produtos (incluindo os não conferidos) sejam listados. Em conferências com muitos itens, isso poderá causar lentidão no carregamento da tela. Nas **Preferências do Coletor**, a configuração de "Quantidade de produtos por página" ficará oculta enquanto esta marcação estiver ativa. |
| --- |

Tem-se que quando a marcação **"Exibir produtos do pedido"** esta mostrará na tela de Conferência um painel com uma grade, contendo os produtos negociados na Nota ou Pedido.

A marcação **"Exibir quantidade do pedido:"** é habilitada somente quando o campo **"Exibir produtos do pedido"** estiver marcada. Esta opção apresentará a coluna **"Quantidade Negociada"**, na grade dos **itens negociados**, na Nota ou Pedido.

O campo **"Exibe código de barras dos produtos do pedido"** apresenta as opções **"Não exibir"**, **"Automático"**, **"Aba Códigos de barra do cadastro"** e somente estará habilitado quando o campo **"Exibir produtos do pedido"** estiver marcado.

Quando o campo **"Exibe código de barras dos produtos do pedido"** estiver configurado como **"Automático"** ou **"Aba Códigos de barra do cadastro"**, no painel de conferência, que é aberto ao iniciar uma conferência através da tela de **"Fila de Conferência"**, é apresentada no painel de **"Itens do Pedido"** a coluna **"Cód. Barras"**.

De acordo com a opção definida no campo **"Exibe código de barras dos produtos do pedido"**, o código de barras será apresentado na grade, de acordo com a seguinte ordem:

Para a opção **"Automático"**:

1º: **Estoque:** Caso o produto esteja configurado para usar controle adicional de estoque, será apresentado o "Cód. Barra", informado na aba **"Estoque"** do Cadastro de Produtos, para o respectivo controle.

2º: **Unidade alternativa:** O sistema busca o **"Cód. Barras"** que está cadastrado na aba "Unidades Alternativas" do Cadastro de Produtos para a **unidade** informada no item do Pedido/Nota.

3º: **Código de Barras com Unidade:** O sistema busca o "Cód. Barras" que está informado na aba "Código de Barras" do Cadastro de Produtos utilizando a "Unidade" informada no item do Pedido/Nota.

4º: **Código de barras sem Unidade:** O sistema busca o "Cód. Barras" que está informado na aba **"Código de Barras"** do cadastro de Produtos **ignorando a unidade**.

5º: **Referência:** O sistema busca o "Cód. Barras", informado no campo **"Referência"** do cadastro de Produtos.

Para a opção **"Aba Códigos de barra do cadastro"**:

1º: **Código de barras com Unidade:** O sistema busca o **"Cód. Barras"** que está informado na aba Código de barras do Cadastro de Produtos, utilizando a **"Unidade"** informada no item do Pedido/Nota.

2º: **Código de barras sem Unidade:** O sistema busca o **"Cód. Barras"** que está informado na Aba Código de Barras do cadastro de Produtos ignorando a unidade.

3º: **Estoque:** Caso o produto esteja configurado para usar controle adicional de estoque, será apresentado o Cód. de Barras informado na **"Aba Estoque"** do cadastro de Produtos, para respectivo controle.

4º: **Unidade alternativa:** O sistema busca o "Cód. Barras" que está cadastrado na aba **"Unidades Alternativas"** do Cadastro de Produtos, para a unidade informada no item do Pedido/Nota.

5º: **Referência:** O sistema busca o "Cód. Barras" informado no campo **"Referência"** do cadastro de Produtos.

A opção **"Aba Códigos de barra do cadastro"** não indica que o sistema buscará o **"Cód. Barras"** apenas desta aba, mas sim que dará preferência a ela.

Observação sobre as preferências do coletor: caso a opção "Exibir os produtos do pedido" esteja ligada, a configuração de "Quantidade de produtos por página" nas Preferências do Coletor não será exibida, uma vez que a paginação é automaticamente desabilitada para assegurar a listagem completa dos itens.

Quando a marcação **"Exibir produtos conferidos"** estiver habilitada, será apresentado nesta tela um painel contendo os produtos que já foram conferidos.

**Nota:** quando se inicia uma conferência através da tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia) é apresentada a tela de **"Conferência"**.

Referente à marcação **"Exibir quantidade conferida"**, esta será habilitada somente quando o campo **"Exibir produtos conferidos"** estiver marcado. Quando realizada, será apresentada na tela Conferência, a coluna de **"Quantidade Conferida"** e a **"Quantidade Conferida em Unidade Padrão"**, na grade de itens conferidos.

Quando a marcação **"Exibir divergências ao conferir"** estiver acionada, tem-se a exibição das divergências ocorridas na tela Fila de Conferência no momento da conferência dos produtos.

**Importante:** ao acionar a opção Exibir divergências ao conferir, o sistema exige que as opções Exibir produtos conferidos, Exibir quantidade conferida, Exibir produtos do pedido e Exibir quantidade do pedido estejam marcadas, apresentando a seguintes mensagem:

**"As opções "Exibir produtos conferidos", "Exibir quantidade conferida", "Exibir produtos do pedido", "Exibir quantidade do pedido" também serão ligadas. Deseja continuar?"**

Deste modo, ao confirmar este processo tem-se a marcação automática desta opções. Caso uma das marcações seja desmarcada, o sistema desmarcará automaticamente o campo Exibir divergências ao conferir.

A marcação **"Exibir imagem do produto"** quando realizada, caso no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), tenha-se na Aba Geral uma imagem do referido item, esta imagem será apresentada na utilização da Fila de Conferência.

Marque a opção **"Emitir alerta sonoro em mensagens de divergência"**, para exigir um alerta sonoro através de um arquivo mp3, durante a Conferência e na Conclusão da Conferência, caso alguma mensagem de erro seja apresentada. Além disso, o alerta sonoro será emitido quando a empresa trabalhar com identificadores e informou-se um identificador inválido.

Para emissão do som de alerta na Conferência, é necessário configurar o parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"**. Neste parâmetro configura-se o endereço do arquivo de som, que será executado na conferência de pedidos, sempre que o sistema detectar uma incompatibilidade, como, quantidade conferida de produto incorreta e/ou código de barras incorreto.

**Observação:** os tipos de arquivo que são aceitos nesse parâmetro são: mp3, wma e wave.

Além disso, o arquivo deve ser hospedado em diretório do servidor, conforme exemplo:

1º: Parâmetro de chave FREPBASEFOLDER: **D:\Repositorio\**;

2º: Criado na pasta D:\Repositorio\: **system\sounds\conferencia**;

3º: Copiado e renomeado arquivo mp3: **error.mp3**.

No servidor Linux:

1º: Parâmetro de chave FREPBASEFOLDER: **/home/servicedesk/modelos/**;

2º: Criado na pasta /home/servicedesk/modelos/: **system/sounds/conferencia**;

3º: Copiado e renomeado arquivo mp3: **error.mp3**.

####

#### Seção Faturamento/Confirmação

A marcação **"Aceita múltiplas entregas"** é habilitada somente quando o campo **"Momento da conferência"** estiver definido como **"Antes de faturar"**. Quando esta marcação estiver ligada, pode-se finalizar a conferência como divergente, ou seja, poderá conferir apenas parte do pedido, fazer o corte e faturar o mesmo. Quando for necessário faturar o restante do pedido, bastará acessar o Portal ou o Pedido e utilizar a opção **"Liberar para conferência"**, fazer a conferência do restante ou de mais uma parte do restante, finalizar a conferência e proceder seu faturamento.

**Observação:**quando esta marcação estiver habilitada, o sistema irá ajustar automaticamente o status da conferência de acordo com essa configuração. Ou seja, se a nota estiver confirmada, a conferência finalizada corretamente e a marcação Aceita múltiplas entregas ativa, o status da conferência será alterado para **"Aguardando Conferência"**.

A marcação **"Ao faturar, considerar estoque conferido"** (por padrão desmarcada), ao ser efetuada, no processo de faturamento, será utilizada a quantidade conferida para este procedimento. Esta opção ao ser assinalada, deve-se atentar para as seguintes particularidades acerca das formas de faturamento:

Pela grade **"Resultado da seleção"** de documentos ([Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)):

- Em casos de múltiplos pedidos selecionados, apenas se todos possuírem conferência e estiverem configurados para faturamento por quantidade conferida, o sistema de fato irá utilizar o faturamento pela conferência, caso contrário o faturamento convencional será empregado.

Pela tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia):

- Com a referida opção marcada, o sistema sempre utilizará o faturamento pela conferência, caso contrário utilizará o faturamento convencional.

**⚠️ Riscos da marcação "Ao faturar, considerar estoque conferido":**

Ao utilizar esta opção, o sistema permitirá realizar o faturamento do documento **mesmo que o produto não possua estoque disponível**. Portanto, esta marcação deve ser utilizada com cautela, pois a ausência de estoque no momento do faturamento pode influenciar negativamente nas seguintes rotinas:

- **Geração do Custo:** Pode haver distorções no cálculo do custo médio ou contábil;
- **Kardex:** O extrato de movimentação de estoque apresentará saldos inconsistentes ou negativos;
- **Demais rotinas de estoque:** Qualquer processo que dependa da acuracidade do saldo físico será impactado.

**Importante:** produtos configurados com o campo **"Controlar por"** definido como **"Número de lote"** (localizado na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional)) não são compatíveis com pedidos que exigem conferência no faturamento. Isto é, pedidos configurados com a marcação Ao faturar, considerar estoque conferido ativada e o parâmetro **"Agrupar prod.repetido em qualquer faturamento? - AGRUPFATSEMP"** ligado.

Lembrando que, esse parâmetro funcionará como um 'espelho' da nota de origem nas devoluções.

Exemplo:

Se na data do lançamento da nota de origem, o parâmetro estiver ligado, os itens serão agrupados e, na devolução também ficará agrupado. Todavia, se estiver desligado no lançamento da nota de origem, os itens não ficarão agrupados na devolução, mesmo se nesse momento ele estiver ligado.

Quando a marcação **"Faturar ao concluir conferência"** estiver ligada, ao finalizar uma conferência corretamente, o sistema verificará se o campo **"TOP p/Faturamento"** da TOP da nota/pedido e a série para faturamento, definida no parâmetro **"Série Padrão para Faturamento/Venda - SERIEVNDPADRAO"**, estão informados. Se tudo estiver correto, o sistema tentará realizar o faturamento.

Além disso, quando essa marcação estiver ativada, será realizado o faturamento padrão, equivalente ao botão [Faturar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#faturamento-comofazer) do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) e também à opção **"Faturamento"** > [Faturar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturar) localizado no botão **"Outras opções"**. Ou seja, dentro do processo de conferência, não é possível realizar outros tipos de faturamento.

Ao final do processo de conferência, o sistema exibirá uma mensagem informando que a conferência foi concluída, indicando se o faturamento foi realizado ou não. Caso o faturamento seja bem-sucedido, a nota gerada será impressa conforme a configuração definida.

**Observação:** em alguns casos, o faturamento pode ser concluído com sucesso, mas a nota gerada não ser confirmada. Nesses casos, é necessário verificar se as configurações estão corretas, se há liberações de limites pendentes ou outras validações que possam impedir a confirmação da nota.

Referente à marcação **"Ao efetuar corte pela Central/Portal"**, tem-se que o sistema irá realizar a recontagem de forma automática sempre que houver corte no pedido e a situação de conferência estiver como **"Finalizada"** ou **"Recontagem"**.

Tem-se que uma vez que um item foi cortado, seja este parcial ou total, a conferência entrará em modo de recontagem, mesmo que este seja desfeito, a conferência continuará exigindo recontagem.

**Nota:** o campo Momento da conferência deverá estar marcado com a opção **"Antes de faturar"** e o pedido não poderá ter sido faturado.

Nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), o corte poderá ser efetuado por meio do campo **"Qtd. Corte"** ou por meio do botão **"Corte"** na [grade itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens).

#### Produtos controlados por lote

O campo **"Usar seq. lote no cód. barras"**, juntamente com a informação solicitada à frente dele (Separador), visam aperfeiçoar o código de barras gerado para um produto, especialmente quando se faz necessária a localização deste produto dentro de um determinado lote. Na fabricação do produto, é gerado um código de barras especial para ele, de modo que se obtenha a seguinte ordenação:

```
<CODBARRAS>+<SEPARADOR>+<SEQUENCIA>
```

Esta funcionalidade, tem como característica fazer com que na conferência de saída, quando este código de barras é utilizado, os caracteres referentes ao número sequencial de identificação do item sejam ignorados na busca de produtos, porém, seja registrado no item conferido. Deste modo, é possível saber exatamente quais os itens de um lote específico foram expedidos a partir de um determinado pedido/nota.

**Importante:** feita a configuração da conferência que é vinculada a TOP utilizada na nota, vale informar que esta TOP utilizada no documento a ser conferido deve em sua configuração, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) estar com a marcação **"A nota fica como pendente"** efetuada. Além disso, é necessário configurar o **"Código de Barras"** do produto na aba [Código de Barra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abacdigodebarras) da tela Cadastro de Produtos.

A marcação **"Validar lote conforme Estoque"** só pode ser ativada quando a marcação Detalhar lote pela conferência (presente nesta aba) estiver habilitada. Ao ativar a marcação Validar lote conforme Estoque, o sistema verificará se o lote informado está disponível no estoque durante o registro na [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia).

Se o lote não for encontrado no estoque, o sistema exibirá a seguinte mensagem:

**"Estoque insuficiente. Empresa: X Produto: YYYY Local: ZZZZZ Controle: XPTO."**

A opção **"Ignorar controle do tipo lote"** quando marcada, no momento da conferência, o controle do tipo lote será ignorado. Para que esta opção seja apresentada, é necessário que o parâmetro **"Permite ignorar controle por lote na conferência - CNFIGNCONTLOTE"** esteja habilitado.

#### Seção Peso/Balança

No campo **"Registrar peso"** defina como será o comportamento da conferência em relação ao peso dos produtos. Poderemos defini-lo dentre as seguintes opções:

- **Não Registrar:** Não será necessário registrar o peso dos itens ao proceder com a conferência;
- **Manualmente:** Tem-se por esta opção, a obtenção do peso dos produtos de forma manual, ou seja, o peso será digitado. Quando a obtenção de peso é feita de forma manual, ainda assim é possível usar a balança através do botão "Obter da balança", que será apresentado também no modo manual;
- **Balança/Manual:** Por esta opção, o peso dos itens será obtido através da balança, porém também será possível que o mesmo seja incluído manualmente;
- **Pela balança:** Através desta opção, o peso dos produtos na conferência será obtido exclusivamente com o uso da balança.

No campo **"Obter quantidade pela balança"** tem-se as seguintes opções:

- Não obter;
- Pela balança;
- Balança/manual.

**Seção** **Recontagem:**

Por meio da marcação **"Exibir produtos divergentes na recontagem"**, os produtos com divergência serão apresentados na recontagem.

Através do campo **"Recontagem"**, determine como será a recontagem; teremos as seguintes opções:

- **Automática:** Quando for finalizada a conferência e esta terminar com divergência, será apresentado o botão **"Realizar recontagem"**, para que seja iniciada uma nova recontagem.
- **Comandada:** Quando selecionada esta opção, não será apresentado o botão **"Realizar recontagem"** ao finalizar a conferência como divergente. Será necessário utilizar a opção **"Solicitar recontagem"**, localizada no menu do botão **"Outras opções..."** dos "Portais" e na "Central - Compras | Vendas | Mov. Internas".

Determine em **"Abrangência da recontagem"**, até que ponto deve-se proceder com a recontagem. Tem-se as seguintes opções:

- **Recontar todos os itens, mesmo aqueles sem divergência:** Se esta opção for selecionada, devemos proceder com toda a conferência.
- **Recontar seletivamente:** Deve-se refazer a conferência apenas dos itens que tiveram divergência; não será necessário conferir novamente os produtos que não apresentaram erro, contudo, caso necessário, ela poderá ser feita.

**Importante:** uma vez marcada a opção **"Excluir do processo de conferência"**, presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral) no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), este item não participará da Conferência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Aba Corte/Divergência

![Imagem 5: Aba Corte/Divergência](https://ajuda.sankhya.com.br/hc/article_attachments/5541136907415)

No campo **"Corte/Divergência"**, o sistema dispõe das opções:

- **Permitido:** Quando a conferência for finalizada, se esta estiver divergente, também será apresentado ao usuário, o botão **"Cortar itens divergentes"**. No entanto, se a divergência tiver sido causada por conferência de produtos não constantes no pedido ou por conferência de quantidades maiores do que as negociadas na nota ou pedido, o botão mencionado não será apresentado, pois não haverá nada a cortar da nota ou pedido, nesses casos.

Ao clicar no botão para cortar os itens, o sistema irá realizar o corte de acordo com a opção **"Procedimento de corte"** e se houver "liberações de limites", estas deverão ser realizadas.

- **Proibido:** Quando selecionado, o corte não será utilizado pelo sistema, logo o botão **"Cortar itens divergentes"** não será apresentado ao usuário ao finalizar a conferência como divergente. Se a conferência for finalizada com divergência, deve-se realizar o corte manualmente, diretamente na nota ou pedido, e acessar a opção **"Reprocessar conferência"** presente no menu do botão **"Outras opções..."**, presente nos "Portais" e na "Centra de Notas". Ao reprocessar, se a conferência for igual a negociada na nota ou no pedido, a conferência será finalizada como **"OK"**.

O campo **"Quantidade a maior",** refere-se ao momento da conferência, em que se a quantidade conferida for maior que a quantidade negociada, esta poderá ser tratada de duas formas:

- **Permitido:** O sistema permitirá que a conferência seja feita, contudo ao finalizá-la, esta ficará como divergente;
- **Proibido:** Ao fazer a Conferência do Produto, caso tenha excedido a quantidade negociada na Nota ou Pedido, o sistema exibirá uma mensagem de alerta e não fará a conferência desse item.

Caso no campo **"Recontagens p/ permitir corte/divergência"** seja informado um valor diferente de zero o sistema contará quantas recontagens ocorreram e caso a quantidade seja superior ao informado nesse campo, a recontagem é automática. O botão de corte é apresentado ao final das conferências com divergência, permitindo ao usuário clicar neste e cortar a nota ou pedido de acordo com as configurações.

####

#### Seção Divergência a maior

No campo **"Procedimento de divergência a maior"**, quando uma conferência for finalizada com divergência a maior (quantidade conferida maior que a quantidade do documento), aplica-se as seguintes opções:

- **Gerar ped. complementar:** Ocorre a aceitação da divergência gerando assim um pedido complementar;
- **Atualizar a quantidade negociada:** A divergência será permitida e finalizada ajustando-se a quantidade negociada dos itens no documento de origem;
- **Não ajustar:** A divergência não será ajustada.

Referente ao campo **"Modelo nota p/ pedido complementar"**, este campo será habilitado apenas se o campo **"Gerar ped. complementar"** estiver marcado. Informa-se neste campo o modelo de nota que será utilizado na geração de pedidos complementares nos casos de divergência.

Com a marcação **"Ped. complementar confirmado"** habilitada, quando o campo **"Procedimento de divergência a maior"** estiver configurado com a opção **"Gerar ped. complementar"**. Quando marcada, o pedido complementar gerado pela divergência a maior, seja gerado confirmado.

Tem-se que no **"Produtos não constantes no pedido"**, no momento da conferência existirem produtos que não constam no pedido ou nota, estes podem ser tratados de duas maneiras:

- **Permitido:** O sistema permitirá a conferência de um produto não constante na Nota ou Pedido, porém ao finalizar a conferência esta ficará como divergente, e não poderá ser confirmada ou faturada.
- **Proibido:** Ao fazer a Conferência do Produto, se ele não estiver na Nota ou Pedido, o sistema apresentará uma mensagem de alerta e não fará a conferência desse item.

Ao habilitar a opção **"Conferir produto não constante no pedido"**, será possível a conferência de um produto não constante na Nota ou Pedido. Esta opção ficará disponível quando o campo Produtos não constantes no pedido estiver configurado com a opção **"Permitido"**.

####

#### Seção Divergência a menor

**Observação:** esta seção ficará disponível quando o campo **"Corte/Divergência"** estiver configurado com a opção **"Permitido"**.

O campo **"Procedimento de corte"** possui três opções de escolha:

- **Atualizar a quantidade negociada:** Esta opção somente pode ser utilizada se o campo **"Momento da conferência"** estiver configurado como "Antes do confirmar". Quando for efetuado o corte, o sistema cortará a diferença direto na quantidade negociada no item da nota ou pedido e recalculará o total dos itens e da nota, refazendo o financeiro.
- **Atualizar a quantidade cortada:** O sistema apenas fará o corte, se o campo **"Momento da conferência"** estiver definido como **"Antes do confirmar"**. O sistema permitirá a confirmação da nota e não fará o corte na quantidade negociada. Quando o campo **"Momento da conferência"** for **"Antes de faturar"**, ao fazer o faturamento o sistema irá realizar o corte na nova nota gerada e no pedido não haverá alterações.
- **Gerar nota de devolução:** Ao realizar o corte, será gerada uma nota de devolução.
- **Corte parcial de itens:** São duas as opções de escolha:
- **Permitido:**O sistema deixará realizar o corte parcial. Por exemplo, se foi negociado a quantidade de 10 do produto XX, porém só existem 7 produtos XX no estoque, ao realizar o corte parcial, o sistema cortará os 3 que faltam, de acordo com o campo **"Procedimento de corte"**.
- **Proibido:** O sistema não autorizará o corte parcial. Esta opção será utilizada quando a empresa desejar somente, que seja entregue toda a mercadoria ou nenhuma. Vejamos um exemplo:

Foi negociada a quantidade de 10 unidades do produto XX, porém só havia 7 unidades no estoque, o sistema não autorizará o corte, a conferência não será finalizada como "OK", deverá ser feito o corte manual na nota ou pedido ou ser feita uma recontagem, sendo que na nova conferência, não seja conferido nenhum produto que não tenha o total negociado, fazendo com que o sistema corte todo o item da nota ou pedido.

O campo **"Modelo nota p/ devolução"** será habilitado, apenas se o campo **"Procedimento de corte"** estiver selecionado como **"Gerar nota de devolução"**. Informa-se neste campo o modelo de nota que será utilizado na geração da nota de devolução nos casos de divergência.

A opção **"Nota de devolução confirmada"** será habilitada, quando o campo **"Procedimento de corte"** estiver configurado com a opção **"Gerar nota de devolução"**. Quando acionada, o sistema irá tentar confirmar a nota que fora conferida e, caso haja sucesso, haverá a tentativa de confirmar a nota de devolução.

Caso esteja desmarcada, o sistema apenas confirmará a nota que fora conferida. A nota de devolução gerada, deverá ser confirmada então manualmente pelo usuário. O mesmo procedimento vale para o pedido complementar gerado.

**Observação sobre Agrupamento de Itens no Faturamento:** Ao realizar o faturamento de um pedido que possua quantidade de corte originada na conferência, o comportamento do sistema dependerá do parâmetro **"Agrupar prod.repetido em qualquer faturamento? - AGRUPFATSEMP"**:

- **Se o parâmetro estiver ligado:** ao faturar, o sistema levará a **quantidade conferida** para a nota fiscal, respeitando o que foi efetivamente apurado no processo.
- **Conflito com a quantidade de corte:** caso haja uma quantidade de corte registrada na conferência e o referido parâmetro esteja ativado, o sistema poderá desconsiderar a quantidade do corte obtida especificamente na conferência, mantendo a quantidade registrada ou negociada originalmente no pedido para fins de faturamento.

**Nota:** esse procedimento só irá funcionar se na aba **"Geral"** desta tela, o campo **"Momento da conferência"** estiver definido como **"Antes da Confirmação"**.

Para que o campo **"Liberação p/ corte/divergência"** seja habilitado, é necessário que o campo **"Corte/divergência"** esteja definido com a opção **"Permitido"**. Tem-se as seguintes opções:

- **Nunca exigir:** O sistema não solicitará liberação de Limites de Corte na conferência.
- **Exigir sempre:** Ao realizar o corte, será solicitada a liberação de limites para o evento **"64-Corte/divergência de pedido (Conferência)"**, de acordo com a configuração.

Referente ao campo **"Tipo de liberação"**, este estará disponível quando o campo Liberação p/ corte/divergência estiver definido com a opção **"Exigir sempre"**.

- **Uma liberação por item divergente:** Será solicitada uma liberação de limites para cada item da nota ou pedido, que estiver divergente, no momento de fazer o corte.
- **Uma liberação única por pedido:** Será solicitada apenas uma liberação para a nota ou pedido, no momento de fazer o corte.

O campo **"Ao liberar"** será habilitado se o campo Liberação p/ corte/divergência estiver configurado com a opção **"Exigir sempre"**. São apresentadas as seguintes opções:

- **Marcar para recontagem:** Após o usuário fazer a liberação da solicitação e não houver mais solicitações de liberação para essa conferência, o sistema marcará a conferência para uma recontagem.
- **Reprocessar conferência:** Após a liberação da solicitação pelo usuário e se não houver mais solicitações de liberação para essa conferência, selecionando-se esta opção, o sistema irá refazer o corte, e caso não haja itens com quantidade maior ou produtos não constantes no pedido, o sistema realizará o corte e finalizará a conferência como **"OK"**.

**Importante:** os campos Liberação p/ corte/divergência, Tipo de liberação e Ao liberar, só estarão visíveis na tela se o parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** estiver habilitado.

**Observação:** em casos onde o usuário deseja alterar a quantidade negociada em notas ou pedidos, inserir ou remover itens, após a nota ter sido conferida e finalizada como **"OK"**, o sistema irá marcar essa conferência como finalizada e divergente. Neste caso, será necessário reprocessar a conferência, ou então fazer uma nova conferência para continuar o processo. Se a conferência não estiver finalizada não haverá problemas, pois a quantidade conferida somente será comparada com a quantidade negociada, ao finalizar a conferência.

#### Manipulação de itens divergentes

Para habilitar a manipulação dos itens divergentes e/ou fora do documento, será necessário alterar a Configuração de Conferência desta aba:

O campo Produtos não constantes no pedido deverá estar com a opção Proibido selecionada.

- A marcação **"Conferir produto não constante no pedido"** terá de estar habilitada.

Desta forma, na tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia), quando acionado o botão **"Produtos Divergentes"** será aberto o popup **"Produtos divergentes na conferência"**, sendo que os produtos com divergência estarão destacados em vermelho.

O popup também pode ser visualizado se o usuário tentar finalizar a conferência com determinado produto divergente no documento. Neste caso, a finalização da conferência só será permitida caso não haja produtos com divergência não constante no documento.

**Importante:** o botão **"Remover"** estará disponível se a marcação Conferir produto não constante no pedido estiver acionada. Este botão estará habilitado para ação quando o produto selecionado na grade não estiver presente no documento em conferência.

Ao selecionar um produto divergente que não encontra-se no documento da grade, o botão de remover será habilitado e ao clicar neste, um pop up será exibido solicitando a confirmação de remoção do item.

Assim, quando o usuário registrar a conferência de um item do pedido, o sistema dará foco à sua respectiva linha na grade **"Itens do Pedido"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Aba Formação de Volumes

Por esta aba, determine as características da Formação de Volumes.

![Imagem 6: Por esta aba, determine as características da Formação de Volumes.](https://ajuda.sankhya.com.br/hc/article_attachments/5541314377367)

Em relação ao campo **"Formação de volumes"**, quando você selecionar a opção **"Registro simplificado (na tela)"**, ao realizar a conferência o campo **"Qtd. volumes"** será apresentado na tela. Além disso, ao optar pela opção **"Registro simplificado (no final)"**, no ato da conferência o sistema exibirá uma janela de mesmo nome solicitando o preenchimento dos volumes.

A opção **"Registro detalhado de volumes"** é melhor explicada por meio do link [Registro Detalhado de Volumes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602034-Registro-Detalhado-de-Volumes).

**Observação:** para que a etiqueta seja impressa, é necessário que nesta aba, no campo Formação de volumes esteja configurado com a opção Registro detalhado de volumes.

A marcação **"Imprimir etiquetas ao finalizar conferência"** indica que devem ser impressas as etiquetas ao finalizar a conferência.

No campo **"Modelo p/ etiqueta"**, teremos o modelo a ser utilizado na impressão das etiquetas será definido.

**Nota:** quando o sistema utilizar faturamento automático na finalização, as etiquetas somente serão impressas caso o faturamento seja bem sucedido.

Todos os pedidos/notas que utilizam a configuração **"Sempre apresentar na fila de conferência"** serão apresentados na fila de conferência mesmo que não possuam produtos conferíveis.

Quando a marcação **"Imprimir uma etiqueta por volume"** estiver efetuada, para as conferências que possuem dois ou mais volumes serão impressas duas ou mais etiquetas.

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral) tem-se o campo **"Imprime etiqueta de volumes na conferência"** (TGFPRO.IMPETIQCONF) que ao ser marcado, indique que o produto deve ter impressão de etiquetas. Por padrão esse campo já está habilitado, logo, sendo desejado que algum produto não tenha impressão de etiquetas deve desmarcá-lo e tratá-lo no modelo de relatório das etiquetas.

Em situações em que a formação de volumes é detalhada, somente o conferente poderá finalizar a conferência, pois pode haver impressão de etiquetas ou faturamento do pedido. Quando houver, por exemplo, uma solicitação de liberação de corte, ao liberar essa solicitação, o sistema não finalizará a conferência caso o campo **"Ao liberar/Aba Corte"** estiver com a opção **"Reprocessar conferência"** selecionada, o sistema marcará a conferência como **"Aguardando finalização"**, e então o conferente através da tela "Fila de Conferência" fará a finalização dessa conferência dando um duplo clique no pedido/nota que estiver aguardando finalização.

Veja também a documentação da tela [Impressão de Etiquetas Vol. Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601094-Impress%C3%A3o-de-Etiquetas-Vol-Confer%C3%AAncia).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Processo de Conferência

**1)** Lançando uma "Nota", e utilizando-se o campo **"Momento da conferência"** definido como **"Antes da confirmação"**:

![Imagem 7: 1) Lançando uma "Nota", e utilizando-se o campo "Momento da conferência" definido como "Antes da confirmação" :](https://ajuda.sankhya.com.br/hc/article_attachments/5541616911895)

**2)** No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), informe no campo **"Configuração p/ conferência"**, a configuração de conferência a ser utilizada para esta **"TOP"** (esta é a configuração que irá determinar como a conferência irá se comportar, em cada Nota ou Pedido).

![Imagem 8: 2) No cadastro de Tipos de Operação - TOP , aba Estoque , informe no campo "Configuração p/ conferência" , a…](https://ajuda.sankhya.com.br/hc/article_attachments/5541733280279)

**Observação:** no pedido de venda com conferência por série e faturamento, é necessário que na tela Tipos de Operação - TOP, o tipo de movimento de Faturamento seja configurado na aba Estoque, no campo **"Atualização do Estoque"**, com a opção **"Baixar"**, para que ocorra a baixa do estoque, desse modo o sistema ajustará o **"ATUALESTOQUE"** da TGFSER, após a confirmação do pedido, da nota faturada e conferência por série.

Ao lançar uma **"Nota de Venda"**, utilizando a TOP configurada para conferência e um Produto que faz parte do processo de conferência, o deve-se acessar o botão **"Outras opções..."** e utilizar a opção **"Liberar para conferência"** esta opção também pode ser acessada pelo [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454)).

![Imagem 9: Ao lançar uma "Nota de Venda" , utilizando a TOP configurada para conferência e um Produto que faz parte do processo de…](https://ajuda.sankhya.com.br/hc/article_attachments/5542554049815)

Assim, enquanto a **"Nota"** não for liberada para a conferência, ela não será apresentada na tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia), e não sendo conferida, não poderá ser confirmada.

Neste caso, deve-se acessar a tela Fila de Conferência, onde serão apresentados apenas os "Pedidos" e "Notas" que **fazem parte do processo de conferência**, e que já podem ser conferidos, ou seja:

- Notas e Pedidos que utilizam **"Momento da conferência"** como **"Antes da confirmação"** e foram liberadas para conferência;
- Notas e Pedidos que utilizam **"Momento da conferência"** como **"Antes de faturar"** e já foram confirmados;
- Notas em **processo de recontagem**, com a conferência em **andamento** e **aguardando liberação** de corte.

As Notas e Pedidos apresentados na tela Fila de Conferência são ordenados por Data e Hora do movimento, ou seja, as mais antigas são apresentadas em primeiro lugar. Conferências já finalizadas não são exibidas nesta tela.

**Observação:** através do parâmetro **"Tempo em minutos p/ atualizar Fila Conferência - TEMPOREFCONF"** o sistema fará, a atualização automática da [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia). Para isso, configure no campo **"Inteiro"**, na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), o valor em minutos, indicando de quantos em quantos minutos esta Fila será atualizada. Além disso, com este parâmetro habilitado, a função de Liberar para conferência é realizada automaticamente ao final do tempo estipulado no campo acima.

Para iniciar a "Conferência", basta dar um duplo clique na linha da Nota ou Pedido desejado; com isso, será apresentado um novo painel onde sua parte superior mostrará se está **"Conferindo"** ou **"Recontando"**, além do "Número da Nota", o "Parceiro" e o "Vendedor".

![Imagem 10: Para iniciar a "Conferência", basta dar um duplo clique na linha da Nota ou Pedido desejado; com isso, será apresentado…](https://ajuda.sankhya.com.br/hc/article_attachments/5542983987351)

Tem-se também o campo **"Cód. Barras"**, onde será informado o código de barras para a conferência. Caso a empresa utilize **"Controle"** este campo será apresentado, contudo, somente será habilitado após ser informado o código de barras e o produto vinculado a esse código de barras, utilizar Controle.

Caso a Conferência esteja configurada para utilizar **"Tipo de Contagem"** igual a **"Única por Produto"**, será também apresentado o campo **"Quantidade"**, onde informa-se a quantidade conferida.

Ao proceder com a conferência de todos os produtos, deve-se clicar no botão **"Finalizar conferência"**; com isso o sistema verificará se as quantidades de todos os **produtos conferidos** batem com as **quantidades negociadas dos produtos** da Nota ou Pedido, caso isso não ocorra, será apresentada uma janela informando que a conferência foi finalizada com divergência. De acordo com a configuração desta janela, será apresentado o botão **"Cortar itens divergentes"** e caso a recontagem seja automática, será apresentado o botão **"Realizar recontagem"**.

Para efetuar a recontagem, basta clicar no botão **"Realizar recontagem"**; o painel da tela "Fila de Conferência" é reaberto e uma nova conferência poderá ser feita.

Para **realizar o corte**, bastará utilizar o botão **"Cortar itens divergentes"**. Caso a **configuração de conferência** utilize "Liberação de Limites", será feita uma solicitação de liberação para o evento **"64 - Corte de pedido (Conferência)"**; caso contrário, será apresentada a mensagem de corte bem sucedido ou não.

Nos casos que ocorra **solicitação de liberação de limites**, no momento da liberação dessa solicitação, o sistema executará o que estiver determinado no campo **"Ao liberar"** desta tela, aba [Corte/Divergência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abacortedivergncia).

Uma vez finalizada a conferência, a nota poderá ser confirmada.

**3)** Lançando um "Pedido" ao utilizar o campo **"Momento da conferência"** definido como **"Antes de faturar"**:

![Imagem 11: 3) Lançando um "Pedido" ao utilizar o campo "Momento da conferência" definido como "Antes de faturar" :](https://ajuda.sankhya.com.br/hc/article_attachments/5543391308567)

Assim como no procedimento citado anteriormente, no cadastro de Tipos de Operação - TOP, informe no campo **"Configuração p/ conferência"**, a configuração de conferência a ser utilizada para esta **"TOP"**:

![Imagem 12: Assim como no procedimento citado anteriormente, no cadastro de Tipos de Operação - TOP , informe no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/5543674591767)

Com essa TOP o "Pedido" poderá ser lançado e confirmado normalmente, porém,  caso seja feita a tentativa de faturá-lo sem proceder com sua conferência, o sistema não irá concluir o faturamento e exibirá uma mensagem, informando que **não houve conferência** dos produtos deste "Pedido".

**"Conferência exigida pela TOP XX ainda não realizada. (Nro. único = XXX)".**

Feita a conferência, o pedido poderá ser faturado normalmente.

**Observação:** para que seja possível efetuar a conferência com uma Unidade Alternativa, faz-se necessário que a Configuração de Conferência encontre-se com o campo **"Buscar código de barras por"** igual a **"Unidade alternativa"** sendo que, também, deverá ser inserido um código no campo Referência ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#top), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral)) para a unidade principal e um código no campo **"Código de Barras"** (Cadastro de Produtos, aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaunidadesalternativas)).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Exclusão de Conferência

A opção **"Excluir Conferência"** localizada no botão **"Outras opções..."** presente nos Portais de [Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609994), [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953), [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593) ou na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973), remove todos os dados de conferências vinculadas ao pedido/nota, inclusive informações de volumes, histórico de corte, solicitações de liberação de corte, caso existam.

![Imagem 13: A opção "Excluir Conferência" localizada no botão "Outras opções..." presente nos Portais de Pedidos , Compras , Vendas…](https://ajuda.sankhya.com.br/hc/article_attachments/5543754004759)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Exclusão de Notas Conferidas

Podem ocorrer situações, onde um "Pedido" tenha sido conferido, gerando o corte de alguns itens e faturado normalmente, contudo por algum motivo a "Nota" que foi gerada no faturamento, foi excluída pelo usuário. Nesse caso o sistema perde o que tinha **sido cortado anteriormente**. Nessa situação será necessário utilizar a opção **"Reaplicar corte"** presente no Portal de Compras | Vendas | Mov. Internas ou na Central - Compras | Vendas | Mov. Internas; este procedimento, **reaplica o corte no "Pedido"** possibilitando que este seja **faturado novamente**.

Outra situação semelhante, ocorre quando a nota gerada pelo faturamento também for excluída e for solicitada uma recontagem. Quando o conferente iniciar a recontagem desse pedido, o sistema mostrará uma janela, informando que a **conferência possui um histórico de corte** e perguntará ao usuário se deseja **"Reaplicar corte"** e finalizar, ou **"Realizar a recontagem"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

## Parâmetros que influenciam nesta rotina

O parâmetro **"Procedure para definir empresa e local de destino - NOMPROCEMPLOCAL"** possibilita a inserção de uma procede que será responsável por permitir a seleção do Local e da Empresa destinatários em faturamento para transferência na conferência. Vejamos um exemplo contendo como parâmetros de entrada o Número da nota e o Número da Conferência. Deste modo, o retorno será o código da empresa de destino e o local de destino no atoa da conferência.

```
CREATE PROCEDURE STP_GET_EMP_LOCAL

AS

BEGIN

   SELECT

       @P_CODEMP = CODEMP,

       @P_CODLOCAL = CODLOCAL

   FROM

      TESTE

    WHERE NUNOTA = @P_NUNOTA

END

GO
```

**Nota:** é de cunho obrigatório que a procedure contenha os parâmetros P\_NUNOTA DECIMAL, P\_NUCONF DECIMAL, P\_CODEMP NUMERIC OUTPUT e P\_CODLOCAL NUMERIC OUTPUT.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#top)

![Imagem 14: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16343283356055) Acesse também:

[Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)
