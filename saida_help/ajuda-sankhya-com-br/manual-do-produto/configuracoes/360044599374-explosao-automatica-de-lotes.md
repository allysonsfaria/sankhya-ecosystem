---
id: "360044599374"
titulo: "Explosão Automática de Lotes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:51Z"
rotulos: ["Produtos", "Configuração", "WMS", "Explosão Automática de Lotes", "LOTAUTCENT", "LOTEDTVAL", "PRECOPORCONT", "PRECOPORCONTEXL", "Explosão Automática de Lotes manual", "Central de Vendas", "Lote", "Estoque", "CONSLOTEATIVO", "REPETECONTANT"]
---

# Explosão Automática de Lotes

A Explosão Automática de Lotes é uma funcionalidade disponível na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas),  em que, ao lançar um item em uma nota de venda ou pedido de venda, caso o produto seja controlado por lote e data de validade, você precisará informar o lote de cada item, porém, com essa funcionalidade, não será necessário informar o Lote (CONTROLE).

Caso o lote não seja informado, o sistema distribui a quantidade solicitada entre itens de cada um dos lotes do produto, automaticamente. A distribuição é feita na ordem das datas de validade, das mais próximas para as mais distantes.

Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:

---

| ![Imagem 1: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310676491927) |  | ![Imagem 2: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310676493591) |  | ![Imagem 3: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310706072087) |
| --- | --- | --- | --- | --- |
| [![Imagem 4: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310706072215)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#configura%C3%A7%C3%B5esiniciais) |  | [![Imagem 5: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310706072855)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#par%C3%A2metros) |  | [![Imagem 6: Dessa forma, pode clicar nas imagens abaixo para consultar as configurações e o processo a ser realizado:](https://ajuda.sankhya.com.br/hc/article_attachments/42310676495767)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#processo) |

---

### Configurações Iniciais

Primeiramente, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) configure o seu controle adicional de estoque para que este seja realizado por meio do controle de lote, para isso, na [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional) selecione a opção **"Número do lote"** do campo **"Controlar por"**.

![Imagem 7: Primeiramente, no Cadastro de Produtos configure o seu controle adicional de estoque para que este seja realizado por…](https://ajuda.sankhya.com.br/hc/article_attachments/4407268892183)

Lembre-se ainda que, o produto em questão deve pertencer a um Grupo de Produtos que valide estoque, ou seja, este não pode estar configurado com a opção **"Não valida"** no [Cadastro de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os), aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaestoque).

A TOP utilizada na nota de venda, deve estar configurada com a opção **"Baixar"** do campo **"Atualização do Estoque"**, aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque). Porém, a marcação **"Atualizar Estoq.a partir da Confirmação"** da mesma aba, não pode estar habilitada.

![Imagem 8: A TOP utilizada na nota de venda, deve estar configurada com a opção "Baixar" do campo "Atualização do Estoque" , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4407268898583)

**Importante:** o parâmetro **"Controla Preços por Controle - PRECOPORCONT"** deve ser desabilitado, pois, no caso em que o produto é controlado por lote, não é possível associar preços diferentes para cada lote, ou seja, na tabela de preços, o preço deve ser cadastrado sem informar o lote.

**Restrição de Estoque de Terceiros**: A funcionalidade de Explosão Automática de Lotes (incluindo o uso do parâmetro **LOTAUTCENT**) é restrita exclusivamente a operações com **estoque próprio**. O sistema possui um comportamento nativo e intencional de **não realizar a explosão automática** quando o estoque em questão é de **terceiros**, sendo necessário, nestes casos, a informação manual do lote/controle.

**Nota:**a explosão de lote para componente de Kit não funciona para **"Kit Independente"**.

![Imagem 9: A marcação "Permitir reserva de estoque sem lote?" será habilitada para uso apenas quando a TOP for configurada para…](https://ajuda.sankhya.com.br/hc/article_attachments/16245204309527) A marcação **"Permitir reserva de estoque sem lote?"** será habilitada para uso apenas quando a TOP for configurada para reservar estoque (aba Estoque, campo Atualização do Estoque). Durante o lançamento e/ou faturamento de um Pedido de Venda, caso a TOP utilizada no procedimento esteja com esta marcação realizada, o sistema irá efetuar a reserva de estoque mesmo que o lote não seja informado; caso o lote seja inserido, será validado seu respectivo estoque; se o lote não for preenchido, será feita a validação com base no total de estoque de todos os lotes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#top)

---

### Parâmetros

Nesse tópico, exibiremos alguns parâmetros que podem influenciar no uso da rotina de explosão automática de lotes. Observe:

**Usar data de validade junto com Lote? - LOTEDTVAL:** habilita o uso da Data de Validade no controle de estoque. Assim, ao informar um item de produto controlado por número de lote, o sistema exige que seja informada a Data de Validade.

**Controle Automático por data de validade de lote? - LOTAUTCENT:** ao utilizar esse parâmetro, será habilitado o controle automático de lote. Caso contrário, você deve informar os lotes manualmente. É importante mencionar que, caso esse parâmetro esteja ativado, ao salvar um item presente em um pedido que reserve estoque, o sistema irá explodir o lote.

Além disso, mesmo que o parâmetro LOTAUTCENT esteja desabilitado, na Operação de Produção (que gera nota de produção), ao informar uma MP controlada por lote, mesmo que o lote não seja informado a explosão de lote ocorrerá normalmente, de forma que, o sistema utilizará o lote da MP que está mais próximo do vencimento.

Para habilitar a marcação **"Ignorar explosão automática de lotes nesta TOP"** da aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque) na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) é necessário que o campo **"Atualização do Estoque"** desta mesma aba esteja configurado como **"Baixar"** e o parâmetro LOTAUTCENT esteja ligado. Dessa forma, ao acionar essa marcação, o sistema não efetuará a explosão automática de lotes no lançamento de documentos que utilizarem a TOP.

| ![Imagem 10: Para habilitar a marcação "Ignorar explosão automática de lotes nesta TOP" da aba Estoque na tela Tipos de Operação -…](https://ajuda.sankhya.com.br/hc/article_attachments/42310706075159) | No parâmetro "Emp. que utilizam controle por data de validade lote - EMPLOTAUTCENT" deverão ser incluídas as empresas que serão impactadas pelo parâmetro de chave LOTAUCENT; assim, se o parâmetro LOTAUCENT estiver habilitado, todas as empresas serão impactadas.  Caso haja mais de uma empresa na configuração do parâmetro EMPLOTAUTCENT, as empresas devem ser separadas por vírgula, sem nenhum espaço em branco ou "enter". Por exemplo: 1, 3, 7. |
| --- | --- |

**Usa local do estoque na explosao lote inclusão? - USALOCESTEXPLOT:** quando este parâmetro estiver ligado, o sistema utilizará o Controle e o Local de estoque para explosão do lote. Do contrário, será carregado automaticamente apenas o Controle para explosão. Lembrando que, esse parâmetro não afetará a explosão do lote durante o faturamento, somente a inclusão do produto pela Central. Vale ressaltar que, a opção **"Agrupar local na validação de estoque"** presente na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaestoque) da tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294) deve estar habilitada para que ocorra a explosão entre locais que possuam estoque do produto para a empresa informada.

**Controla Preços por Controle? - PRECOPORCONT:** quando esse parâmetro for habilitado, o campo **"Controle"** será exibido na tela de **"Atualização de custos"** para que a atualização seja realizada por controle. Com o parâmetro desabilitado, ao atualizar os custos, o campo Controle não é apresentado, e esta é feita para todos os controles.

**Exclui Lote do "Controla Preços por Controle"? - PRECOPORCONTEXL:** esse parâmetro trabalha de forma conjunta ao parâmetro citado anteriormente. Com o parâmetro anterior ligado, os preços serão controlados por controle, porém, quando este segundo também é habilitado, o sistema reenquadra os produtos controlados por "lote" na regra de busca de preço utilizada habitualmente, ou seja, serão apresentados para estes seus preços específicos.

**Não mostra estoque inativo na explosão de lotes? - NMOSTRALOTINA:** quando esse parâmetro for habilitado, ao lançar no Pedido/Nota um produto que contenha diferentes lotes, será desconsiderado o lote que estiver com estoque vazio e utilizado o próximo lote a vencer que contenha estoque para compor a nota.

**Usar (Estoque - Reserva) ao Faturar pelo Estoque? - FATEST-RESERV:** na realização do faturamento de um pedido, considerando a nota gerada, cuja TOP utilizada esteja configurada para reservar estoque, esse parâmetro deve ser ligado para que a Explosão de Lote aconteça. Além disso, quando habilitado, permitirá que o sistema considere como estoque somente a quantidade disponível do produto.

**Ignorar validação estoque quando lote automático? - IGNORAVALESTLT:** quando este parâmetro está habilitado o sistema não realiza a validação de estoque corresponde ao produto relacionado à explosão automática de lotes. Diante disto, desconsidera o produto que seja controlado por lote retirando-o do faturamento.

**Custo por controle? - CUSTOPORCONT:** quando esse parâmetro estiver habilitado, o sistema irá preencher o campo **"Custo"** do item da Nota, bem como preencherá o campo**"Controle"** do item desta, nos seguintes itens:

- Explosão automática de lote na inserção de item;
- Explosão automática de lote no faturamento;
- Explosão automática de lote na expedição (WMS).

**Corte Automático de Lote WMS - CORTEAUTLOTEWMS:** quando este parâmetro for ligado, o sistema irá automaticamente realizar o corte de produtos com base no estoque físico disponível. Assim, observe o exemplo:

Foi solicitada uma quantidade de 200 unidades do Produto X, sendo assim, temos:

- Possuímos 50 unidades do lote Y e;
- 50 unidades do lote Z.

Portanto, o sistema irá gerar um corte automático de 100 unidades do produto X.

| ``` Para o correto funcionamento desse processo, o parâmetro "Zerar Corte após  faturamento? - ZERARQTDCONF" deve ser desligado. ``` |
| --- |

**Considera lote ativo na explosao de lote? - CONSLOTEATIVO:** quando este parâmetro estiver ligado, o sistema irá considerar apenas o lote ativo para o faturamento da nota.

**Repete último controle digitado? - REPETECONTANT:** se estiver ligado, quando for incluido um produto que tenha [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), ao incluir um novo item que também tenha controle, o sistema já irá sugerir o controle do anterior.

**Priorizar saldo pickings na expl. lote WMS? - WMSPRIPICKEXPLT:** com este parâmetro habilitado, no momento da explosão de lotes de um produto que possua duas ou mais notas e conste em estoque de dois ou mais pulmões com diferentes lotes, será priorizado o saldo existente no picking.

**Calcular qtde. mínima para o lote no faturamento? - QTDMINLOTEAUT:** quando o parâmetro estiver ligado, o valor mínimo de estoque para que um lote seja selecionado em uma explosão de lotes deve ser maior ou igual ao resultado do cálculo:

```
  1/(10^Decimais para quantidade)
```

Lembre-se que o campo **Decimais para quantidade** é configurado na sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abamedidas) da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque) (tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#top)

---

### Processo

Sabendo que o início desse processo ocorre ao realizar uma compra, na inserção de cada item, por meio da opção **"Desmembrar item por lote"** do botão **"Outras Opções..."** da Central, informe a **"Data de validade"**, **"Data de fabricação"** e o número do **"Lote"** no pop-up **"Desmembrar lote"**.

**Importante:** para utilizar a opção Desmembrar item por lote, é necessário primeiro salvar o item desejado. Após isso, selecione a opção Desmembrar item por lote e insira os dados necessários para realizar o desmembramento do lote.

[GIF animado: Imagem 11: Importante: para utilizar a opção Desmembrar item por lote , é necessário primeiro salvar o item desejado. Após isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/4407268996503)

Com os produtos em estoque separados por Lote e Data de Validade, você tem a possibilidade de realizar o faturamento do pedido ou lançar uma nota de venda para os produtos.

Dessa forma, caso uma dessas ações seja realizada sem informar o Lote (CONTROLE), o sistema irá distribuir a quantidade informada conforme a Data de Validade do Lote, ou seja, os lotes com as datas de validade mais próximas são esgotados primeiros, e se o estoque total não for suficiente, um erro será lançado.

Quando você preencher os campos acima com as informações requeridas, os produtos serão separados em estoque segundo o Lote e Data de Validade. Assim, poderá optar por faturar o referido pedido, ou lançar uma nota de venda para o produto.

![Imagem 12: Em caso de lançamentos de Pedidos e Notas de Vendas, o sistema utiliza apenas a Data de Validade como critério para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16245204309527) Em caso de lançamentos de Pedidos e Notas de Vendas, o sistema utiliza apenas a Data de Validade como critério para a explosão de lotes. Contudo, quando existir mais de um lote com a mesma Data de Validade, o sistema escolherá aleatoriamente quais lotes serão utilizados.

#### Pedido de Venda

Dado que um pedido foi lançado na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), e este possuir um item controlado por número de lote e quantidade do produto, ao lançar um pedido e incluir um item controlado por número de lote, quantidade do produto, valor unitário, etc., o campo **"Controle"** não deve ser informado, e o item será salvo.

Assim, ao Confirmar o pedido e faturar, a nota lançada pelo faturamento utilizará a mesma quantidade do item do pedido, porém distribuída em itens de acordo com os lotes.

**Observação:** o sistema não permite a duplicação de itens nos orçamentos/pedidos e não efetua a explosão de lotes durante o faturamento.

#### Nota de Venda

Na Central de Vendas, efetue o lançamento de uma nota e inclua um item controlado por número de lote. Lembre-se ainda que, o campo Controle não deve ser preenchido.

Ao salvar o item, o sistema automaticamente distribuirá a quantidade informada em itens, conforme os lotes e suas respectivas datas de validade.

| ![Imagem 13: Ao salvar o item, o sistema automaticamente distribuirá a quantidade informada em itens, conforme os lotes e suas…](https://ajuda.sankhya.com.br/hc/article_attachments/42310706075159) | **O parâmetro Controla Preços por Controle - PRECOPORCONT deverá estar desabilitado, pois, no caso em que o produto é controlado por lote, não é possível associa preços diferentes para cada lote, ou seja na tabela de preço, este dever ser cadastrado sem informar o lote (Controle).** |
| --- | --- |

**Nota:** caso nas operações de entrada do sistema, sendo elas, Compras e Devoluções de Vendas, a empresa utilizada no processo esteja com a marcação **"Utiliza explosão de lote no recebimento"** da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) habilitada, o sistema realizará a explosão de lote em determinados momentos da operação. Observe:

- Quando não houverem divergências, o sistema realizará a inserção ou atualização no controle de lote dos itens da nota ao processar o recebimento;
- Se houver um mesmo produto que se encontra em UMA's diferentes, o sistema irá somá-los, o que atualizará os itens da grade;
- Porém, caso esse mesmo produto possuir controles de lotes diferentes, estes serão inseridos na grade de itens com uma sequência para cada controle cadastrado ou quantidade menor que a inicial, de forma que, o sistema irá realizar o recálculo dos valores da grade e de seus impostos.

**Observações:**

Para que o lote dos pedidos sejam corretamente fragmentados, habilite a marcação **"Fragmenta lote no envio para separação"**, localizada na aba WMS do Cadastro de Produtos.

Além disso, é importante também que a marcação **"Utiliza explosão de lote na separação"** ([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms)) esteja ligada, pois, assim, durante o lançamento do pedido de venda, o produto não terá uma validação de estoque e na separação, ele poderá ser separado independente do seu lote.

Porém, **atenção**! Para que as funcionalidades das marcações acima realizem as suas funções, o parâmetro **"Lote automático no envio para o WMS? - LOTEENVIOWMS"** precisar estar desligado.

Ao lançar um desconto em um item controlado por lote, pode acontecer de ser necessário utilizar mais de um lote para atender a quantidade desejada, alterando assim a quantidade de cada item, isso faria com que fosse preciso recalcular o desconto por quantidade, nesse caso, indica-se que o desconto somente seja alterado após a confirmação do item, pois assim os lotes já estarão definidos e o desconto por quantidade terá sido recalculado.

**Observação:** quando um desconto promocional por quantidade for aplicado e ocorrer a divisão de lote, o sistema irá considerar a regra do desconto por linha do desmembramento, e não por valor total somado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes#top)
