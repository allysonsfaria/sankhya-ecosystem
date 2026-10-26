---
id: "360044612074"
titulo: "Fila de Conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:26:13Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Conferência", "Configuração", "Fila", "Central de Vendas", "TAXBOLNOT", "CODBARDECOMP2", "CONFCODBARRA2", "Finalizar conferência", "Produtos Divergentes", "br.com.sankhya.fila.de.conferencia", "Fila de Conferência manual", "Estoque", "Fila de Conferência", "Limite", "Liberação", "Gestão da Fila de Conferência", "Conferência Pedido Nota Estoque", "RECALCVALITEM"]
---

# Fila de Conferência

```
 Módulo: Comercial > Rotinas > Fila de Conferência
```

---

Entende-se como **"Conferência"**, o momento em que os itens presentes em um pedido/nota são confrontados com o que de fato existe fisicamente no estoque da empresa. Este procedimento é realizado com o auxílio desta tela.

**Observações:**

- Esta rotina não suporta o [Controle de Pedidos por Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045269813-Controle-de-Produtos-por-Grade).
- A [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053) não trabalha em conjunto com a Fila de Conferência.
- Para que um usuário possa realizar a conferência, é necessário ter permissão para **"Incluir"** na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854).

Vale salientar que nosso sistema permite que você realize a [Conferência por Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050705273).

![Imagem 1: Vale salientar que nosso sistema permite que você realize a Conferência por Coletor .](https://ajuda.sankhya.com.br/hc/article_attachments/360082817353)

São apresentados aqui, todos os Pedidos/Notas que estão em Conferência; o status destes documentos poderão ser:

- Aguardando conferência;
- Em andamento;
- Aguardando liberação de corte;
- Aguardando Recontagem;
- Recontagem em andamento;
- Aguardando liberação de Corte.

**Importante:** ao realizar a conferência, é necessário que você utilize a mesma unidade utilizada durante a negociação. Por exemplo, ao realizar uma negociação com a opção **"Unidade Alternativa"**, o processo de conferência deverá ser realizado nesta mesma unidade. Caso contrário o sistema ira emitir a mensagem:

**"Quantidade conferida maior do que quantidade negociada no pedido/nota."**

Ao iniciar uma **"Conferência"**, será exibida a tela abaixo:

![Imagem 2: Ao iniciar uma "Conferência" , será exibida a tela abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360082817593)

Esta tela é composta por grades que apresentam:

- Itens em conferência;
- Itens Conferidos;
- Itens do Pedido;
- Imagem do produto.

Na grade Itens do Pedido, temos a marcação **"Ocultar itens já conferidos"** que, ao ser realizada, fará com que os itens que foram conferidos sejam ocultados na grade, restando apenas aqueles que não passaram por tal procedimento. Também nesta grade, as linhas que apresentarem a coloração **amarela**, demonstram que a quantidade conferida ainda encontra-se menor que o pedido; já as linhas em **vermelho**, representam que a quantidade conferida encontra-se maior que a quantidade no pedido.

A apresentação da Imagem do produto vem da realização da marcação **"Exibir imagem do produto"** disponível na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral) da tela [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073), e da imagem do [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) ter sido previamente salva em seu cadastro (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abageral), campo **"Imagem"**).

Na parte superior esquerda da tela, existe o botão ![Imagem 3: Na parte superior esquerda da tela, existe o botão denominado "Configura o modo de visualização dos painéis" que, ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16244697272855) denominado **"Configura o modo de visualização dos painéis"** que, ao ser acionado, exibirá o pop-up **"Configuração dos painéis"**, onde você pode realizar as seguintes definições:

As marcações disponíveis em **"Visualizar em"** definem como será a disposição dos painéis presentes na tela. Temos três possibilidades:

- Em abas;
- Em painel vertical;
- Em painel horizontal.

Caso a marcação **"Digita qtd. antes do cód. barras"** seja realizada, ao proceder com a conferência, a disposição dos campos Cód. Barras e Quantidade será alterada, ficando o campo Quantidade em primeiro lugar, seguido do Cód. Barras. Ao acessar a tela para realização da Conferência, o foco inicial será no campo Quantidade.

Além disto, ao inserir o Código de Barras, a informação incluída primeiramente na Quantidade, será mantida; ao informar a Quantidade, se o Código de Barras não for incluído, o sistema coloca o foco no campo Cód. Barras e, mesmo pressionando **"Enter"** no teclado, não ocorre o direcionamento para o campo seguinte.

**Observação:** caso os produtos possuam identificadores (grade Itens Conferidos), estes podem ser do tipo Número Serial ou IMEI ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abageral), sessão **"Identificadores da conferência"**); trabalhando-se com identificadores do tipo IMEI, caso este tenha um tamanho diferente de 15 caracteres, será exibido um "balão" ao lado do campo, com a informação "IMEI inválido: XXXXXXXXXXX". Este comportamento previne que um Código de Barras seja lido equivocadamente no lugar de um IMEI. Caso um identificador seja lido pela segunda vez, também teremos a apresentação de um "balão" com os dizeres, "Identificador já informado: YYYYYYYYYYYYYYY".

Além disto, caso seja feita inserção de um identificador que já tenha sido informado para o produto/conferência em questão, o sistema irá emitir um alerta sobre o ocorrido.

**Nota:** quando um produto que exige identificadores é conferido utilizando o campo Quantidade, caso esta quantidade seja maior que 1 (um), o pop-up onde são incluídos os identificadores passa a apresentar uma grade para inclusão de todos os identificadores. Por exemplo, se um produto usa 2 (dois) identificadores e foi conferido 4 (quatro) unidades, a medida que os **"conjuntos de identificadores"** vão se formando, as linhas são inseridas na grade. É importante salientar que todos os identificadores de um produto devem ser lidos em sequência, para formação correta dos conjuntos. Ainda neste exemplo, assim que 4 (quatro) conjuntos forem informados, o pop-up é fechado, possibilitando a conferência do próximo produto.

**Observação:** o parâmetro **"Recalcular Valor ao Alterar a Quantidade na Conferência? - RECALCVALITEM"** define se o **"Vlr. Unitário"** do item na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) será recalculado ao alterar a Quantidade de itens na Fila de Conferência. Por padrão, este parâmetro se encontra habilitado, o que faz com que o sistema ajuste o valor unitário quando há mudança na quantidade. Caso esteja desligado, o valor unitário permanecerá inalterado, mesmo que a quantidade seja alterada.

Ao **"Finalizar a Conferência"** o sistema solicitará confirmação.

Caso haja divergência o sistema exibirá as opções abaixo:

![Imagem 4: Caso haja divergência o sistema exibirá as opções abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360082817633)

Ao clicar sobre o botão **"Gerar ped. compl./nota de dev. ou corte"**, o sistema realizará a geração dos documentos auxiliares (pedido complementar e nota de devolução). O sistema verificará qual é o procedimento de corte definido na Configuração da Conferência cadastrada na TOP da nota. Se o procedimento de corte definido for **"Gerar Nota de Devolução"** e, no momento da conferência algum item for conferido com quantidade menor do que consta na nota, será gerada uma nota de devolução da seguinte forma:

1. O cabeçalho da nota será gerado baseado no modelo cadastrado no campo **"Modelo nota p/ devolução"** na tela [Configuração da Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073). Os dados que não estiverem preenchidos no modelo serão retirados da nota que está sendo confirmada.
2. Os itens gerados para a nota de devolução serão aqueles que tiverem sua quantidade conferida menor que a quantidade presente na nota que está sendo conferida. A quantidade dos itens na nota de devolução é a diferença entre a quantidade na nota que está sendo conferida e a quantidade conferida.

O procedimento de geração do pedido complementar acontece da mesma maneira que a nota de devolução, com a diferença de ser gerado quando um item é conferido com uma quantidade maior do que constava na nota.

Após a geração do pedido complementar e/ou nota de devolução, o sistema apresentará um pop-up informando quais foram os documentos gerados.

**Observação:** caso a marcação **"Nota de devolução confirmada"** esteja efetuada na tela Configuração da Conferência, o sistema tentará confirmar a nota que foi conferida e, caso haja sucesso ao confirmá-la, haverá a tentativa de confirmar a nota de devolução. Por outro lado, estando desmarcada, o sistema apenas confirmará a nota que fora conferida. A nota de devolução gerada deverá ser confirmada manualmente. O mesmo procedimento vale para o pedido complementar gerado.

**Importante:** esse procedimento apenas funcionará se, na tela Configuração da Conferência, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral), o campo **"Momento da conferência"** estiver definido como **"Antes da Confirmação"**.

**Nota:** será permitido gerar apenas o **"Pedido Complementar"** ou a **"Nota de Devolução"** quando o documento que estiver sendo conferido for de **"Compra"**, caso contrário, será emitida uma mensagem informando que não é possível gerar uma Nota de Devolução ou Pedido complementar para um documento de **"Venda"** e o processo será abortado e a conferência não será concluída.

**Observação:** o sistema não realiza nenhum tipo de validação/verificação quanto à atualização de estoque que os **"Tipos de Operação - TOP"** informados para o modelo de Pedido Complementar ou Nota de Devolução realizam (entrada ou baixa de estoque). Com isto, é necessário que você tenha muita atenção neste ponto para que o estoque não fique incoerente.

**Importante:** quando o sistema apresenta o erro: **"Top exige conferência"**, significa que esta validação está relacionada com a marcação **"Exige Conferência"**, que não é utilizada pelo Sankhya Om. Assim, para a Fila de Conferência do Sankhya Om, entendemos que, apenas o fato de haver uma configuração de conferência no campo **"Configuração p/ conferência"**, é necessária para realizar a conferência.

**Importante:** no processo de faturamento, para que o corte seja aplicado corretamente tanto ao produto principal quanto aos componentes do kit na conferência, realize as configurações abaixo na tela [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia):

1. Ative a marcação **"Ignorar componentes de Kit"**, localizada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral), seção **"Regras Gerais"**.
2. Desmarque a opção [Exclusão de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#exclusodeconferncia) no kit.
3. Certifique-se de desmarcar completamente a Exclusão de Conferência.

**Observação:** caso o parâmetro "**Taxa de boleto no total da nota? - TAXBOLNOT"** esteja ligado, ao faturar um pedido de venda (que possua juros calculados) pela Fila de Conferência, o valor dos juros não será levado para a nota de venda. Caso você queira que os juros sejam levados para a nota após o faturamento, é necessário desligar o parâmetro.

Através do parâmetro **"Tempo em minutos p/ atualizar Fila Conferência - TEMPOREFCONF"** o sistema fará, a atualização automática, da Fila de Conferência. Para isso, configure no campo **"Inteiro"**, na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834), o valor em minutos, indicando de quantos em quantos minutos esta Fila será atualizada. Além disso, com este parâmetro habilitado, a função de **"Liberar para conferência"** encontrada no botão ![Imagem 5: Através do parâmetro "Tempo em minutos p/ atualizar Fila Conferência - TEMPOREFCONF" o sistema fará, a atualização…](https://ajuda.sankhya.com.br/hc/article_attachments/22592018447255) **"Outras opções..."** da tela [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia), é realizada automaticamente ao final do tempo estipulado no campo acima.

#### Manipulação de itens divergentes

Para habilitar a manipulação dos itens divergentes e/ou fora do documento, é necessário que você altere a Configuração de Conferência desta aba:

- O campo **"Produtos não contantes no pedido"** localizado na aba [Corte / Divergência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abacortedivergncia) da tela acima deverá estar com a opção **"Proibido"** selecionada.
- A marcação **"Conferir produto não constante no pedido"** deve estar habilitada.

Assim, quando acionado o botão **"Produtos Divergentes"**, será aberto o pop-up **"Produtos divergentes na conferência"**, sendo que os produtos com divergência estarão destacados em vermelho.

O pop-up também poderá ser visualizado caso você tente finalizar a conferência com determinado produto divergente no documento. Neste caso, a finalização da conferência só será permitida caso não haja produtos com divergência não constante no documento.

**Importante:** o botão **"Remover"** estará disponível se a marcação Conferir produto não constante no pedido estiver acionada. Este botão estará habilitado para ação quando o produto selecionado na grade não estiver presente no documento em conferência.

Ao selecionar um produto divergente que não encontra-se no documento da grade, o botão de remover será habilitado e ao clicar neste, um pop up será exibido solicitando a confirmação de remoção do item.

Assim, quando registrarmos a conferência de um item do pedido, o sistema dará foco à sua respectiva linha na grade **"Itens do Pedido"**.

Em caso de **"Recontagem"** o sistema exibirá a tela abaixo:

![Imagem 6: Em caso de "Recontagem" o sistema exibirá a tela abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360081674414)

**Nota:** para que seja possível facilitar a análise no momento da conferência, existe na grade a coluna **"Cód. Barras"**, para quando houver divergências, você saiba qual é o código de barras e unidade já conferida.

![Imagem 7: Nota: para que seja possível facilitar a análise no momento da conferência, existe na grade a coluna "Cód. Barras" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360082817913)

A tela de Recontagem difere da tela de conferência pela opção de visualizar os **"Produtos divergentes"**:

![Imagem 8: A tela de Recontagem difere da tela de conferência pela opção de visualizar os "Produtos divergentes" :](https://ajuda.sankhya.com.br/hc/article_attachments/360081674594)

A Recontagem será influenciada pela configuração do campo **"Qtd. mínima de recontagens p/ permitir corte"**, que se encontra na rotina Configuração de Conferência.

Quando a conferência está **"Aguardando liberação de corte"**, é preciso acessar a tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites) liberar o corte.

Pelo botão **"Detalhes Conferência"** será possível que você visualize os detalhes dos itens conferidos.

**Observação:** quando um produto aparecer destacado na cor **vermelha** é porque houve diferença entre a Quantidade do Pedido e a Quantidade Conferida.

**Observação:** ao realizar qualquer alteração referente a quantidade de produtos na Conferência, todo o financeiro será refeito, com base nas configurações da TOP, incluindo as parcelas geradas.

Caso a quantidade de um item seja aumentada durante a Conferência, o sistema refaz automaticamente o cálculo do custo do produto. Isso acontece porque algumas procedures de cálculo de custo dinâmico consideram a obtenção do preço com base na quantidade negociada. Portanto, qualquer alteração na quantidade exige que o sistema realize um novo cálculo para garantir que o valor do produto reflita a quantidade atualizada.

#### Código de Barras iniciado com "2"

No processo de conferência, existem produtos que possuem código de barras iniciando com o número **"2"** e com tamanho de 14 caracteres (informação esta, inserida no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), no campo **"Referência"**); nesta situação, a interpretação feita pelo sistema é que, este item trata-se de um produto que é pesado em balança e vendido de acordo com seu peso, ou seja, todo o código de barras representa, "código de barras do produto (identificação) + preço + peso (quantidade)". Este comportamento é ativado através do acionamento do parâmetro **"Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2"**.

Por outro lado, podem ocorrer situações em que os produtos não se encaixem completamente neste caso, ou seja, todo o código de barra identifica o produto, ele não é quebrado em identificação, preço e peso.

**Observação:** hoje, o sistema conta com um recurso que busca todo o código do produto e, caso não encontre nenhum item, executa a verificação citada inicialmente (identificação, preço e peso). Para que esta forma de conferência funcione, além do parâmetro CODBARDECOMP2 estar ativado, o parâmetro **"Conferir pelo código de barras iniciado c/2 - CONFCODBARRA2"** deve estar habilitado. Quando estes parâmetros estiverem ligados, o sistema buscará o produto pelo código de barras, informado no campo Referência do Cadastro de Produtos; caso não encontre o Produto, será feita a quebra do código de barras para que seja pego o código do produto.

#### Conferência por Código de Barras Composto

A Conferência por Código de Barras Composto é integrante de um procedimento específico de um Parceiro Sankhya.

Para esta rotina funcionar corretamente, é necessário que, na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), as configurações a seguir sejam realizadas:

- Na aba [Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedicamentos), o campo **"Cód. ANVISA"** deverá ser preenchido.
- Na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaestoque), preencha o campo **"Cód. Barras"**, assim como os campos **"Data de Validade"** e **"Controle"**.
- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), selecione a marcação **"Conferência por Código de Barras Composto"**.

A funcionalidade será habilitada pelo parâmetro **"Conferência por Código Composto - CONFCBCOMPOSTO"**; uma vez ligado, realizará conferências a partir de um código de barras seguindo o layout **"AAAAAAAAAAASSSSSDDDDDDLLLLLLCCCCCCCCCCCCC"**, sendo este:

- **A** **-** O Número do Registro do Medicamento junto à ANVISA, informado no campo Cód. ANVISA localizado no Cadastro de Produtos, dado que este, deverá conter até 11 caracteres.
- **S** **-** O Número Serial do produto, deve ser informando no momento da Conferência do Pedido de Venda com a captura via leitor de QR Code da informação gerada pela impressora do usuário, considerando que este deverá ter até 5 caracteres.
- **D** **-** Este terá até 6 caracteres, sendo que, este representará a Data de Validade do produto.
- **L** **-** No Lote do produto terá até 6 caracteres, e poderá ser acrescido zeros à esquerda caso necessário.
- **C** **-** Este representará o Código de Barras EAN 13, possuindo até 13 caracteres.

**Nota:** para o correto funcionamento da rotina, as informações acima devem ser preenchidas apenas com números.

**Observação:** neste processo, a conferência é efetuada item a item, pois a leitura do QR Code alimenta o Número Serial, que é único para cada produto.

**Parâmetros que influenciam nesta rotina**

**Processa Cód. barras composto - TAMCODCARCOMP:** neste parâmetro você definirá o tamanho do código de barras composto utilizado na rotina.

**Procedure para decompor cód. barras composto - PROCCODBARCOMP:** insira neste parâmetro a procedure que realizará a composição do código de barras composto.

**Procedure p/ tratar cód. barras comp. já conferido - PROCTRATBARCOMP:** este parâmetro tratará do processo de conferência de produtos com código de barras composto, envolvidos em devoluções e/ou transferências entre empresas, ou seja, permitirá que estes sejam conferidos em um novo lançamento.

Acesse também:

[Conferência por coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050705273)

[Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073)

[Integração da balança no Processo de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913)
