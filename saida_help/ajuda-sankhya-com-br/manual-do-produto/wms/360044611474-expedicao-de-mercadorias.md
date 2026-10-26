---
id: "360044611474"
titulo: "Expedição de Mercadorias"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:13:34Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios Formatados", "WMS", "Expedição", "AGRAREASEPPROD", "Expedição de Mercadorias", "MODETIQSEPWMS", "WMSINSEPBALPRES", "WMSVALCODVOLUSU", "br.com.sankhya.expedicao", "Expedição de Mercadorias manual", "Estoque", "Preferências", "PROIBDIGCONFPED", "USARECAGRUPADA", "ESTPICKSEP", "Configuração de parâmetros", "Separação de pulmão", "Botões na tela"]
---

# Expedição de Mercadorias

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311526843415) Módulo: WMS> Rotinas
```

---

Neste artigo, trataremos sobre os seguintes tópicos:

[Separação Direto do Pulmão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#separaodiretodopulmo)                                             [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

[Parâmetros ligados à rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#parmetrosligadosrotina)

![Imagem 2: Parâmetros ligados à rotina](https://ajuda.sankhya.com.br/hc/article_attachments/4406649432215)

**Observação:** esta tela está apta a receber notas de Transferência (baixa) e Pedidos de Requisição originados do [Portal de Movimentações Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas) (botão **"Outras Opções"**, **"Enviar para WMS (Expedição)"**).

**Nota:** caso seja necessário realizar o cancelamento de uma separação que se encontre com o status de **"Conferência validada"**, cancelamento este, efetuado pelas opções **"Cancelar Separação"** ou **"Cancelar Separações dessa OC"**, deve-se após tal procedimento, executar no Coletor a função de **"Armazenagem"**, onde será solicitado o **"Endereço de Estorno"** (este endereço é previamente configurado na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313) e inserido na tela **"Preferências da Empresa"**, aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms) campo **"Endereço para retorno de expedição"**; uma vez informado o endereço de estorno no coletor, informe o produto a ser movimentado e em seguida o endereço de origem do item, ou seja, o local onde ele estava acondicionado inicialmente. Confirmando este procedimento no coletor, pode-se verificar que a separação em questão na tela de Expedição será exibida com o status de **"Cancelada"**.

**Observação:** por meio do filtro **"Parceiro"**, serão filtrados na tela, os parceiros ligados á expedições, incluindo aqueles que possuem [Controle de Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360060958194-Controle-de-Estoque-de-Terceiros).

**Nota:** quando o endereço de picking for configurado em unidade maior do que a padrão, se a quantidade negociada no Pedido/OC não for múltipla da unidade do estoque, ao tentar enviar o pedido para expedição o sistema apresentará a mensagem abaixo:

**"Produto: X armazenado no endereço Y está configurado com a unidade alternativa, a quantidade negociada no Pedido/Nota não é multiplo dessa unidade.**

**O Envio não foi concluído para não fracionar o Estoque.**
**Pedido: Z, seq: null**

**Verifique a configuração de endereços.**

**Pickings disponíveis:**

**Endereço: XX**
**Estoque: YY**

**Pulmões Disponíveis:**

**Pegas registradas:**

**Código: WMS\_E00770"**

**Observação:** no envio da Ordem de Carga, caso um produto esteja sem vínculo com um endereço de picking, o sistema apresentará a imagem abaixo:

**"O Produto X não possui endereço de Picking configurado. Verifique com o Gerente do WMS**
**Pedido: Y**

**O produto deve estar vinculado em um endereço do Tipo: Picking e que 'Permite Expedição'. Esse cadastro é feito na Rotina:**

**WMS >> Cadastros >> Endereço de Armazenamento**

**Código: WMS\_E00770"**

Caso mais de um produto não tenha a configuração, a mensagem apresentará todos os produtos, pedido e sequência do produto no Pedido de Venda/Nota.

## Separação Direto do Pulmão

O sistema irá gerar as separações diretamente dos pulmões quando a quantidade solicitada no pedido for superior a um palete fechado (lastro x camada) e/ou igual a quantidade estocada no endereço de pulmão. Deste modo, será evitado o reabastecimento e acumulo de mercadorias nos pickings, nos casos de expedição de grandes volumes. Considere o exemplo:

- Produto Lâmpada 12v (lastro 10 x camada 10 = 100 CX)
- Pedido: 110 caixas
- Picking = 80 caixas
- Pulmão = 1 palete com 100 caixas

Desta forma, o sistema gerará duas separações onde a primeira irá pegar 10 caixas do Picking e a segunda pegará 1 palete ou 100 caixas no pulmão.

A utilização desta forma de separação está condicionada a marcação da opção **"Utiliza separação pulmão"**, localizada na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), nas Preferências da Empresa.

Será possível gerar uma onda com mais de dois pedidos, que deverão ser supridos com um mesmo produto e será pego do pulmão. Para isto, realize as seguintes configurações:

- Nas Preferências da Empresa, aba WMS, a marcação Utiliza separação pulmão deverá estar selecionada;
- O parâmetro **"Usa área separação do pulmão diferente do picking - USAARSEPDIFPIC"** também influência neste processo; por padrão, ele é apresentado desligado e, somente deverá ser habilitado, caso os endereços de picking estiverem em área de separação diferente do pulmão.
- A Área de Separação deverá ser **"Por Produto"**;

**Observações:**

- A soma da quantidade dos produtos de todos os pedidos deverá ser maior ou igual à quantidade que existe atualmente no pulmão, pois, não pode ser realizado o fracionamento no pulmão, sempre será retirado tudo e o restante faltante será pego no picking;
- Desta forma, será possível que a separação pulmão seja tanto para separação por pedido quanto por produto, de forma que aumente a produtividade nas Tarefas de Expedição;
- O remanejamento não irá considerar o lastro x camada do produto, mas sim a capacidade do endereço do destino;
- Não é possível realizar a separação de itens pendentes, ou que não tenha necessidade de reabastecimento corretivo, logo, será imprescindível realizar o reabastecimento destes itens antes de proceder com a tarefa de separação dos itens.

**Nota:** quando os produtos forem enviados para a separação no Coletor, você poderá visualizar quem é o reponsável por essa separação; dessa forma, será possível tratar as possíveis divergências encontradas de maneira mais fluída e rápida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#top)

## Botões no topo da tela

No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre o comportamento de cada um:

| [![Imagem 3: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311526844567)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botooutrasopes) |  | [![Imagem 4: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311510654743)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#tarefas) |
| --- | --- | --- |
| [![Imagem 5: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/16920797285271)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#divergncia) |  | [![Imagem 6: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/16920793071639)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botoaes) |
| [![Imagem 7: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311510655127)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#conferncias) |  | [![Imagem 8: No alto da tela, temos alguns botões essenciais para a rotina de Recebimento. Clique sobre eles, para saber mais sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/16920793076631)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#atualiza%C3%A7%C3%A3oautom%C3%A1tica) |

**Botão Outras Opções**

No botão Outras Opções... está presente a opção **"Etiquetas para Separação"**. A rotina irá realizar a impressão das etiquetas de separação de acordo com as seguintes configurações:

- O modelo de etiqueta deve ser criado na rotina de Relatórios Formatados;
- O parâmetro **"Modelo de etiqueta para separação - MODETIQSEPWMS"** alimentado com o modelo de etiqueta criado ou o campo **"Modelo de etiqueta para separação"** no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) estiver configurado da seguinte forma:

O produto contendo no campo **"Imprime etiqueta para separação"** a marcação **"Sim (Por unidade)"**, irá imprimir uma etiqueta para cada unidade daquele produto no pedido. Caso indique a opção **"Sim (Por Produto)"**, irá imprimir uma etiqueta por produto.

- O nome da impressora deve ser configurado nas Preferências da Empresa aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), no campo **"Impressora padrão da etiqueta de separação"**.

**Observação:** a impressão de etiquetas de separação também é realizada ao iniciar a separação por esteira, puxando a primeira tarefa na posição inicial da esteira.

Será possível realizar a impressão de etiquetas de volumes manualmente ao utilizar o volume contínuo através da opção **"Gerar etiquetas de volumes..."**, localizada no botão Outras Opções desta tela, desde que o parâmetro **"Detalhar volumes em conferências p/pedido no WMS? - DETALHAVOLWMS"** esteja habilitado e a marcação **"Volume Contínuo"** na rotina de [Área de Separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054) esteja assinalada. Caso o parâmetro encontre-se ligado, mas a Área de Separação não utiliza o Volume Contínuo, será exibida a seguinte mensagem:

**"A geração de etiquetas não pode ser utilizada pois o parâmetro 'Detalhar volumes em conferências p/ pedidos no WMS' está habilitado".**

**Nota:** essa opção realiza somente a impressão de etiquetas em separação por pedido, ou seja, não imprime etiquetas em que a separação seja agrupada por produto.

**Observação:** quando a etiqueta é gerada a mais, tem-se que estas serão removidas sempre a partir da última etiqueta gerada, da maior para a menor.

**(1)** **Preferência de Cores**

Ao acionar essa opção, será aberto um pop-up de mesmo nome, para que você possa personalizar as cores do texto e fundo das linhas na grade de Expedição, de acordo com a Situação de cada um, ou seja, linhas referentes a Expedições Enviado para armazenagem, podem receber uma cor, Concluído outra colocação e assim sucessivamente. Essa personalização pode ser feita por usuário, ou seja, cada usuário do sistema poderá realizar da forma que preferir.

[GIF animado: Imagem 9: Ao acionar essa opção, será aberto um pop-up de mesmo nome, para que você possa personalizar as cores do texto e fundo…](https://ajuda.sankhya.com.br/hc/article_attachments/4404768790679)

**Nota:** a configuração de cores de fundo das linhas poderão ser realizadas somente em HTML5. Caso esta seja feita e em seguida, você acessar a tela em flex, ao retornar para o novo layout as configurações de cores retornarão para as cores padrão.

**(1)** **Retirar Pedidos Sep. por OC** 

Por meio da opção Retirar Pedido Sep.por OC, o sistema irá cancelar um pedido de venda que possua a separação **"Por Produto"** e quando a coluna Situação constar como **"Enviado para Separação"**. Dessa forma, você poderá utilizar os botões ![Imagem 10: Por meio da opção Retirar Pedido Sep.por OC, o sistema irá cancelar um pedido de venda que possua a separação "Por…](https://ajuda.sankhya.com.br/hc/article_attachments/16921026374039) **"Remover selecionados"** ou ![Imagem 11: Por meio da opção Retirar Pedido Sep.por OC, o sistema irá cancelar um pedido de venda que possua a separação "Por…](https://ajuda.sankhya.com.br/hc/article_attachments/16921010520727) **"Remover NÃO selecionados"** para escolher os pedidos que serão cancelados.

**Observação:** será possível cancelar separações de Pedido que estejam com a Situação igual a Enviado para Separação.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

**Tarefas**

Ao clicar neste botão, será exibido o pop-up **"Tarefas de Expedição"** na qual serão apresentadas todas as tarefas que estão relacionadas à expedição que foi selecionada na grade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

**Divergência**

O botão ![Imagem 12: O botão "Divergência" será habilitado quando houverem divergências na conferência da separação de mercadorias.](https://ajuda.sankhya.com.br/hc/article_attachments/16920797285271) **"Divergência"** será habilitado quando houverem divergências na conferência da separação de mercadorias.

Através do pop-up de divergência da expedição, será possível que você visualize as informações de **"Qtde Unidade de Venda"** e **"Unidade Venda"**.

Ao acionar o botão acima, será aberto o pop-up **"Divergências na Separação de Mercadorias"**:

![Imagem 13: Ao acionar o botão acima, será aberto o pop-up "Divergências na Separação de Mercadorias" :](https://ajuda.sankhya.com.br/hc/article_attachments/4404768648343)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

**Botão Ações**

Através do botão ![Imagem 14: Através do botão "Ações" , pode-se realizar a escolha das ações configuradas previamente na tela Dicionário de Dados .…](https://ajuda.sankhya.com.br/hc/article_attachments/16920793071639) **"Ações"**, pode-se realizar a escolha das ações configuradas previamente na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados). Estas ações são configuradas de acordo com a rotina e processo de cada empresa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

**Conferências**

Este botão será habilitado apenas quando existir uma conferência para a separação selecionada.

Acionando este botão, será aberto o pop-up **"Detalhes Itens Conferências"**:

![Imagem 15: Acionando este botão, será aberto o pop-up "Detalhes Itens Conferências" :](https://ajuda.sankhya.com.br/hc/article_attachments/4404775978519)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela)

---

#### Atualização Automática

Através do botão ![Imagem 16: Através do botão "Atualização Automática" você poderá configurar o tempo em segundos para atualização da tela Expedição…](https://ajuda.sankhya.com.br/hc/article_attachments/16920793076631) **"Atualização Automática"** você poderá configurar o tempo em segundos para atualização da tela Expedição de Mercadorias.

![Imagem 17: Através do botão "Atualização Automática" você poderá configurar o tempo em segundos para atualização da tela Expedição…](https://ajuda.sankhya.com.br/hc/article_attachments/4406649474967)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#top)

---

#### ![Imagem 18: Atalho para Gerência do WMS](https://ajuda.sankhya.com.br/hc/article_attachments/42311510655383) Atalho para Gerência do WMS

O botão **Atalho para Gerência do WMS** foi adicionado para agilizar a gestão de tarefas e usuários na rotina de expedição. Ele permite acessar a tela **Gerência de WMS** diretamente da tela de expedição, sem a necessidade de sair e refiltrar os dados manualmente.

Ao clicar nesse botão, a tela de Gerência de WMS será aberta automaticamente, já filtrada para a expedição selecionada. Nela, é possível:

- Definir a **prioridade** da tarefa de separação.
- Associar **usuários** para executarem a tarefa.

**Importante:** A **prioridade** da tarefa só pode ser definida na tela de Gerência de WMS, pois é lá que o código da tarefa é gerado.

---

## Parâmetros ligados à rotina

O sistema irá gerar as separações:

O parâmetro por padrão "**Exigir cadastro de volume por usuário no WMS? - WMSVALCODVOLUSU"** é apresentado ativado, de modo que é necessário que sejam cadastradas as unidades dos produtos nas configurações por usuário no WMS. Se o parâmetro em questão for desativado, não será necessário efetuar o cadastro, sendo possível que o usuário tenha acesso a qualquer unidade no WMS.

Em relação ao parâmetro **"Iniciar separação balcão pendente de ressuprimento. - WMSINSEPBALPRES"**, por padrão é apresentado ativado; este comportamento faz com que na busca de uma tarefa de separação de balcão por meio do [Coletor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112173-Coletores), esta tarefa poderá ser iniciada independente dela possuir uma ou mais tarefas dependentes de reabastecimento. Ao ser desligado, não será possível que separações balcão pendentes de ressuprimento sejam enviadas para o Coletor de Dados. Apenas separações que possam ser iniciadas e finalizadas sem interrupções, ou seja, sem a necessidade de reabastecimento, serão apresentadas para o operador.

Quando o parâmetro **"Val.Est.Picking agrup. por controle no Reabast.? - WMSVALESTAGRURE"** estiver ligado, o sistema irá considerar o estoque total do picking, somando todos os controles. Contudo, com este desligado, o sistema manterá o comportamento padrão, utilizando o estoque por Produto/Controle.

Com o parâmetro **"Agrupar área de separação por produto? - AGRAREASEPPROD"** ativado, ao realizar a geração de um pedido que possua mais de um produto e para estes exista a configuração de Áreas de Separação por produto diferentes, ao enviar a Ordem de Carga para expedição, será gerada apenas uma separação agrupando todas as áreas em questão por produto. O referido parâmetro, por padrão, é apresentado acionado. O envio para expedição é realizado através da tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274), por meio das opções denominadas **"Enviar para expedição"** e **"Enviar para expedição por OC"**, localizadas no botão Outras Opções, na qual a primeira envia todas as separações feitas por pedido e a segunda, encaminha todas as separações executadas por produto e por pedido e efetua o fechamento da Ordem de Carga.

Ainda sobre as opções Enviar para expedição e Enviar para expedição por OC, quando o parâmetro **"Encerrar ordem de carga manualmente? - ENCERRAOCMANUAL"** estiver habilitado, ao utilizar a segunda opção o fechamento da Ordem de Carga deixará de ser automático e passará a ser manual. Assim, será possível a inclusão de novos pedidos na ordem de carga e o envio da expedição dentro da mesma OC.

Quando o parâmetro **"Permite continuidade na conferência por pedido? - PERMCONTCONFPED"** estiver habilitado, poderá iniciar e finalizar a conferência em momentos diferentes, ou seja, começar na parte da manhã e terminar na parte da tarde.

**Observação:** nos casos em que a Conferência por Pedido for finalizada em outro momento, o usuário que a iniciou deverá terminá-la. Deste modo, outro usuário não poderá continuar a execução.

Ao habilitar o parâmetro **"Nova busca tarefas - UTILNEWBUSCATAR"**, o sistema permite que vários operadores executem a mesma tarefa no coletor superwaba, cada um em uma sequência.

Ao ligar o parâmetro **"Usa end. de checkout adicional na separação - WMSUSACKADIC"**, o botão **"Checkout Adicional"** ficará disponível e ao clicar neste, o sistema exibirá os checkouts adicionais utilizados.

O parâmetro **"Valida faturamento na Liberação de Doca? - VALFATLIBDOCA"** tem o objetivo de validar os pedidos de venda não faturados, na liberação da doca. Sendo assim, teremos os seguintes comportamentos conforme as opções selecionadas:

- **Não valida:** segue o comportamento atual, ou seja, não validará os pedidos não faturados.
- **Valida e avisa:** com essa opção selecionada, o sistema irá apresentar a mensagem abaixo :

**"Existem Pedidos PENDENTES (ou não faturados) nessa Doca, deseja continuar com a liberação da Doca? Pedidos não faturados?".**

**Nota:** no cenário dessa opção, a doca poderá ser liberada.

- **Valida e Bloqueia:** se o parâmetro estiver com essa opção selecionada e houverem pedidos pendentes, será exibida a seguinte mensagem:

**"Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes."**

**Observação:** nesse caso a doca não poderá ser liberada até que os pedidos sejam faturados ou marcados como não pendente.

Observe abaixo o comportamento referente às 2 últimas opções:

[GIF animado: Imagem 19: Observe abaixo o comportamento referente às 2 últimas opções:](https://ajuda.sankhya.com.br/hc/article_attachments/11144471444887)

**Importante:** o parâmetro VALFATLIBDOCA não atende o mesmo processo configurado com a marcação **"Permite mais de OC na mesma Doca"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms).

Quando você realizar uma Conferência por Pedido ou uma Conferência de Saída, o parâmetro **"Informar avaria na Conferência de Expedição?"- AVARIACONFSAIDA"** pode ser ligado para que o campo **"Quantidade Avariada"** seja exibido no coletor e a quantidade do item avariado, informada. Com o parâmetro desligado, o campo não será exibido.

Quando o parâmetro **"Cons. somente est.Picking na sep.? - ESTPICKSEP"** estiver ligado, o sistema buscará somente o estoque disponível no picking, assim, será gerado um corte no momento do envio da separação. Caso o estoque não seja suficiente para atender a demanda, será apresentado um pop-up para que o corte seja efetuado conforme escolha do usuário.

Os parâmetros **"Quantidade padrão na conferência por pedidos. - QTDCONFPEDWMS"** e **"Proibir digitação de qtd. na conferência por pedid - PROIBDIGCONFPED"** influenciam na rotina de conferência de pedidos no coletor de dados com estes ligados e desligados juntos ou não. Desse modo, considere a funcionalidade de cada um deles:

- **QTDCONFPEDWMS:** quando ligado, esse parâmetro irá definir se o sistema deve preencher automaticamente o campo **"Quantidade"** no coletor de dados durante a conferência de pedido;
- **PROIBDIGCONFPED:** ao habilitá-lo, irá determinar se o valor do campo Quantidade poderá ser alterado durante a conferência de pedido.

**Nota:** os parâmetros QTDCONFPEDWMS e PROIBDIGCONFPED podem ser utilizados junto ao parâmetro DETALHAVOLWMS na [Conferência de Pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050705273-Confer%C3%AAncia-por-Coletor).

Abaixo, detalha-se o comportamento do sistema com o uso dos parâmetros especificados acima:

**(1)** Na situação a seguir, o campo Quantidade do coletor não será preenchido automaticamente e poderá ser alterado durante a conferência. Sabendo disso, observe abaixo a definição dos parâmetros envolvidos:

- **QTDCONFPEDWMS:** valor 0 ou nulo;
- **PROIBDIGCONFPED:** desligado.

**(1)** No caso abaixo, o campo Quantidade não será preenchido de forma automática e poderá ser alterado também durante a conferência, assim como a formação de volumes. Observe:

- **QTDCONFPEDWMS:** valor 0 ou nulo;
- **PROIBDIGCONFPED:** ligado ou desligado.

**(1)** No cenário abaixo, o campo Quantidade será preenchido conforme o valor definido no parâmetro QTDCONFPEDWMS, porém não poderá ser alterado. Assim, tem-se:

- **QTDCONFPEDWMS:** igual ou maior que 1;
- **PROIBDIGCONFPED:** ligado.

**(1)** Nessa situação, o campo Quantidade estará configurado com o valor inserido no parâmetro QTDCONFPEDWMS, porém, nesse caso, esse valor poderá ser alterado durante a conferência. Observe:

- **QTDCONFPEDWMS:** igual ou maior que 1;
- **PROIBDIGCONFPED:** desligado.

Além disso, na recontagem, se o parâmetro **"Utiliza recontagem agrupada na separação? - USARECAGRUPADA"** for ligado, irá definir se a recontagem pode ser realizada ao acumular valores ou se informada a quantidade conferida de uma única vez.

![Imagem 20: Neste caso, os parâmetros USARECAGRUPADA e DETALHAVOLWMS não podem ser utilizados juntos.](https://ajuda.sankhya.com.br/hc/article_attachments/17972894564759) Neste caso, os parâmetros USARECAGRUPADA e DETALHAVOLWMS não podem ser utilizados juntos.

Este também poderá interferir no processo quando utilizado junto aos parâmetros QTDCONFPEDWMS e PROIBDIGCONFPED. Observe:

**(1)** No caso abaixo, o sistema não irá acumular a quantidade conferida no campo Quantidade do coletor de dados na recontagem de uma única vez. Além disso, os parâmetros QTDCONFPEDWMS e PROIBDIGCONFPED serão desconsiderados. Desse modo, teremos:

- **USARECAGRUPADA:** desligado;
- **QTDCONFPEDWMS:** configurado ou não;
- **PROIBDIGCONFPED:** ligado ou desligado.

**(1)** Aqui, o sistema irá acumular as quantidades informadas no campo Quantidade durante a recontagem. E esse mesmo campo será preenchido automaticamente com o mesmo valor do parâmetro QTDCONFPEDWMS. Considere também que, independente da configuração do parâmetro PROIBDIGCONFPED conforme mostrado acima, o campo Quantidade não poderá ser alterado. Observe:

- **USARECAGRUPADA:** ligado;
- **QTDCONFPEDWMS:** valor igual ou maior que 1;
- **PROIBDIGCONFPED:** ligado.

**(1)** Nessa situação, o campo Quantidade será preenchido de forma automática e essas quantidades serão acumuladas. Porém, o campo poderá ser alterado durante a recontagem.

- **USARECAGRUPADA:** ligado;
- **QTDCONFPEDWMS:** valor igual ou maior que 1;
- **PROIBDIGCONFPED:** desligado.

**(1)** Nesse caso, o sistema acumula as quantidades informadas no campo Quantidade durante a recontagem, mas não irá preenchê-lo, pois o parâmetro QTDCONFPEDWMS estará com um valor 0 ou nulo. Nessa situação, o parâmetro PROIBDIGCONFPED é desconsiderado.

- **USARECAGRUPADA:** ligado;
- **QTDCONFPEDWMS:** valor 0 ou nulo;
- **PROIBDIGCONFPED:** ligado ou desligado.

**(1)** Aqui, as quantidades definidas no campo Quantidade durante a recontagem serão acumuladas, além de que, esse campo será preenchido automaticamente pelo valor informado no parâmetro QTDCONFPEDWMS. O parâmetro PROIBDIGCONFPED será desconsiderado. Desse modo, observe abaixo:

- **USARECAGRUPADA:** ligado;
- **QTDCONFPEDWMS:** valor 0 ou nulo;
- **PROIBDIGCONFPED:** ligado ou desligado.

Com o parâmetro **"Ordena sequência de gravação das tarefas. - ORDSEQTAREFA"** ligado, ao gerar uma tarefa de separação, a sequência dos itens será ordenada de acordo com o endereço.

**Priorizar NUTAREFA na ord. da busca tar. de sep.? - WMSPRIORITARSEP:** com este parâmetro desligado, ao lançar uma tarefa de separação, o sistema irá desconsiderar a sequência gravada nas tarefas e utilizará a ordem dos endereços de armazenamento envolvidos. Caso esteja ligado, a separação será realizada priorizando a sequência dos endereços indicados nas tarefas de separação.

**Observação:** esse parâmetro não é utilizado nas rotinas de envio para expedição dos pedidos. Contudo, o mesmo interfere diretamente na ordenação de apresentação dos endereços de separação para atividades exclusivas de separação do tipo balcão.

No término da conferência dos pedidos, ao habilitar o parâmetro **"Permite faturar antes da conferência de volumes? - FATANTESCONFVOL"** é possível realizar o processo de faturamento da nota antes da conferência de volumes do [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602114). Com o parâmetro desligado haverá o bloqueio do faturamento logo após a conferência por pedido na expedição de mercadorias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#top)
