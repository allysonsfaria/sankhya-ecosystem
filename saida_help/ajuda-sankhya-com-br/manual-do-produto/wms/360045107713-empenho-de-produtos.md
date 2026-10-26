---
id: "360045107713"
titulo: "Empenho de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-10-19T20:28:33Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "br.com.sankhya.wms.rot.empenhoproduto", "Empenho de Produtos manual", "Recebimento", "Estoque", "Separação rápida via Crossdocking", "Marcar endereço Crossdocking", "Filtros grade principal emprenho de produtos", "Crossdocking"]
---

# Empenho de Produtos

```
![Módulo 36x36 FINAL.png](https://ajuda.sankhya.com.br/hc/article_attachments/16842160838295) Módulo: WMS > Rotinas
```

---

Esta tela permite que sejam separados os produtos comprados sem que estes sejam armazenados em endereços de pulmão ou picking, mas sim em endereço de crossdocking, ou seja, a mercadoria é recebida e, logo em seguida, é preparada para o carregamento e distribuição/expedição, a fim de ser entregue ao cliente de forma imediata ou o mais rápida possível.

![Imagem 1: Esta tela permite que sejam separados os produtos comprados sem que estes sejam armazenados em endereços de pulmão ou…](https://ajuda.sankhya.com.br/hc/article_attachments/8895621760663)

|  |  |
| --- | --- |
| [Configurações necessárias...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#configuraesnecessriasparautilizarestarotina) | [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#filtros) |
| [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#gradeprincipal) | [Incluir Empenho de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#incluirempenhodeproduto) |
| [Passo a Passo para utilização desta Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#passoapassoparautilizaodestarotina) | [Parâmetros que influenciam esta Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#parmetrosqueinfluenciamestarotina) |

## Configurações necessárias para utilizar esta Rotina

Para que esta rotina desempenhe seu procedimento de forma correta, faz-se necessário realizar algumas configurações em outras telas do sistema, conforme exposto a seguir:

Primeiramente, na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral), a marcação **"End. de Crossdocking"** deverá ser selecionada, considerando que esta ficará disponível para seleção apenas se você realizar a marcação **"Picking"**:

![Imagem 2: Primeiramente, na tela Endereço de Armazenamento , aba Geral , a marcação "End. de Crossdocking" deverá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/360086334093)

Após realizar a configuração acima, configure na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms), o campo **"Endereço CrossDocking"** com o endereço marcado como Crossdocking na tela acima mencionada:

![Imagem 3: Após realizar a configuração acima, configure na tela Preferências da Empresa , aba WMS , o campo "Endereço…](https://ajuda.sankhya.com.br/hc/article_attachments/360085159334)

Por fim, na tela [Docas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612974-Docas), o campo Endereço Crossdocking também deverá ser marcado como Crossdocking:

![Imagem 4: Por fim, na tela Docas , o campo Endereço Crossdocking também deverá ser marcado como Crossdocking:](https://ajuda.sankhya.com.br/hc/article_attachments/360086334553)

**Nota:** caso não haja uma configuração de endereço na tela Docas, o sistema considerará o endereço configurado nas Preferências da Empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)

## Filtros

![Imagem 5: Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/360085159494)

No canto esquerdo da tela, temos os seguintes campos nos Filtros Rápidos:

- Empresa;
- Transportadora;
- Nro. Recebimento;
- Dt. Recebimento;
- Chave NF-e;
- Dt. Negociação;
- Produto;
- Nro. Único (Compra);
- Nota/Pedido(Compra).

**Observação:** o campo **"Empresa"** é o único de preenchimento obrigatório, enquanto os outros são de preenchimento opcional; pode-se preencher qualquer um destes outros campos para facilitar a busca.

Além da opção de Filtros Rápidos, tem-se também a possibilidade de criar um **"Filtro personalizado"** através do ícone ![Imagem 6: Além da opção de Filtros Rápidos, tem-se também a possibilidade de criar um "Filtro personalizado" através do ícone…](https://ajuda.sankhya.com.br/hc/article_attachments/16842138418455)**"Cadastrar Filtro"**.

Depois de definidos os filtros desejados e adequados à rotina, clica-se no botão ![Imagem 7: Depois de definidos os filtros desejados e adequados à rotina, clica-se no botão "Aplicar" para apresentação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16842151177239) **"Aplicar"** para apresentação dos produtos e suas demais informações na [Grade Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#gradeprincipal).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)

## Grade Principal

Neste painel será possível visualizar os detalhes dos itens que foram exibidos após a aplicação do filtro de busca.

![Imagem 8: Neste painel será possível visualizar os detalhes dos itens que foram exibidos após a aplicação do filtro de busca.](https://ajuda.sankhya.com.br/hc/article_attachments/8900036277527)

Pode-se observar os seguintes campos após dar um duplo clique sobre qualquer item:

- Cód. do Produto;
- Controle;
- Nro. Único Compra;
- Nro. Único Venda;
- Situação (Recebimento);
- Qtd. Empenhada;
- Unidade;
- Nro. Recebimento;
- Chave NFe;
- Data de Alteração;
- Cód. do Usuário;
- Tipo de Empenho;
- Pendente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)

## Incluir Empenho de Produto

Na parte superior da tela, tem-se o botão ![Imagem 9: Na parte superior da tela, tem-se o botão "Incluir Empenho de Produto" . Ao acioná-lo, o usuário será encaminhado para…](https://ajuda.sankhya.com.br/hc/article_attachments/16842184093719) **"Incluir Empenho de Produto"**. Ao acioná-lo, o usuário será encaminhado para outro painel, ainda dentro da tela principal Empenho de Produtos:

![Imagem 10: Na parte superior da tela, tem-se o botão "Incluir Empenho de Produto" . Ao acioná-lo, o usuário será encaminhado para…](https://ajuda.sankhya.com.br/hc/article_attachments/8901897549079)

No canto esquerdo desta tela, tem-se o campo **"Empresa"** e as abas **"Compra"** e **"Venda"**; nestas possuem alguns campos que, quando configurados, filtrarão os itens para Empenho dos Produtos.

Ao aplicar o filtro, a grade **"Itens de compra"** será carregada com as informações referente aos produtos, conforme demonstrado acima.

A coluna **"Qtd. Empenhar Compra"** da grade Itens de compra é editável para que seja inserida a quantidade a ser empenhada. Já na grade **"Itens de venda"**, a coluna **"Qtd. Empenhar Venda"** será preenchida com um valor máximo sugerido que poderá ser empenhado.

**Nota:** este valor será calculado sempre com o menor valor entre o pedido (coluna Qtd. Pedidos de Vendas) e o valor de compra (coluna Qtd. em Compras); caso o usuário insira um valor maior, ao tentar confirmar o empenho por meio do botão ![Imagem 11: Nota: este valor será calculado sempre com o menor valor entre o pedido (coluna Qtd. Pedidos de Vendas) e o valor de…](https://ajuda.sankhya.com.br/hc/article_attachments/16843079099031) **"Empenhar"**, o sistema apresentará a seguinte mensagem:

**"A quantidade requerida do produto X, (nro único: X) para realizar o Empenho não pode ser maior que a quantidade existente desse produto".**

Por outro lado, caso não haja divergência nos valores, ao acionar o botão acima, será exibida uma mensagem informando que o empenho foi gerado com sucesso.

**Observação:** as notas não empenhadas serão conferidas normalmente e os produtos não serão enviados para o Picking Crossdocking.

#### Botão Agendamento de Tarefa

Ainda nesta tela, na parte superior, teremos o botão ![Imagem 12: Ainda nesta tela, na parte superior, teremos o botão "Agendamento de Tarefa" ; este botão tem a finalidade de realizar…](https://ajuda.sankhya.com.br/hc/article_attachments/16843129999639) **"Agendamento de Tarefa"**; este botão tem a finalidade de realizar o empenho de forma automática.

Ao acioná-lo, uma sub-tela será aberta mostrando as tarefas que encontram-se agendadas:

![Imagem 13: Ao acioná-lo, uma sub-tela será aberta mostrando as tarefas que encontram-se agendadas:](https://ajuda.sankhya.com.br/hc/article_attachments/8902135834263)

O botão ![Imagem 14: O botão "Modo formulário" quando acionado, permitirá realizar a navegação entre as tarefas de agendamento, bem como…](https://ajuda.sankhya.com.br/hc/article_attachments/16842913481367) **"Modo formulário"** quando acionado, permitirá realizar a navegação entre as tarefas de agendamento, bem como editá-las, conforme demonstrado abaixo:

![Imagem 15: O botão "Modo formulário" quando acionado, permitirá realizar a navegação entre as tarefas de agendamento, bem como…](https://ajuda.sankhya.com.br/hc/article_attachments/8902195732119)

Os campos **"Cód. Config."** e **"Data de alteração"** serão preenchidos automaticamente.

São de preenchimento obrigatório os campos **"Empresa"** e **"Tipo de Gatilho"**, tanto para criação quanto para edição de uma tarefa agendada.

O campo Tipo de Gatilho possui duas opções:

- Expressão CRON;
- Intervalo de Tempo.

Quando selecionada a opção **"Expressão CRON"**, será exibido o campo **"Expressão de Gatilho"**, que é de preenchimento obrigatório pelo fato de ter a função de complementar o Tipo de Gatilho.

**Nota:** ao lado deste campo possui o botão ![Imagem 16: Nota: ao lado deste campo possui o botão "Help" que, quando acionado, abrirá o pop-up "Ajuda Expressão Cron" para que…](https://ajuda.sankhya.com.br/hc/article_attachments/16843455911703) **"Help"** que, quando acionado, abrirá o pop-up **"Ajuda Expressão Cron"** para que seja escolhido o exemplo disponível para preenchimento do campo.

Ao selecionar uma opção e clicar em **"Ok"**, o campo Expressão de Gatilho será alimentado.

Caso seja escolhida a opção **"Intervalo de Tempo"** surgirá os campos **"Tipos de Intervalo"** e **"Valor"**, conforme pode-se notar na imagem acima.

No campo Tipos de Intervalo teremos as seguintes opções:

- Por Hora;
- Por Minuto;
- Por Segundo.

Desta forma, os dois campos possuem vínculos. Vejamos um exemplo:

Se no campo Valor for informado o valor 2 e o campo Tipo de Intervalo estiver com a opção **"Por Minuto"** selecionada, tem-se que, a cada 2 minutos será realizada uma "limpeza" para gerar novos empenhos.

Ainda tratando-se da sub-tela, tem-se o botão ![Imagem 17: Ainda tratando-se da sub-tela, tem-se o botão "Agendamentos ativos" que ao acioná-lo, serão carregados os registros…](https://ajuda.sankhya.com.br/hc/article_attachments/16843205958679) **"Agendamentos ativos"** que ao acioná-lo, serão carregados os registros marcados como ativos.

**Observação:** com a configuração de Agendamento de Tarefa ativa, o sistema fará a leitura desta configuração conforme o tempo de Tipo de Gatilho informado; caso ocorra o empenho automático através desta configuração, será lançado na tela Configurações > Avançado > Envio de Mensagens > Fila os dados que serão enviados ao e-mail cadastrado no pop-up acima.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)

## Passo a Passo para utilização desta Rotina

Primeiramente, deve-se lançar na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) um [Pedido de Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#oqueumpedidodevenda) que contenha os produtos solicitados pelo cliente.

**Nota:** será necessário que a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de Pedido de Venda não atualize estoque.

Após isto, realize o lançamento de uma [Nota de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras#comolanarumpedidodecompra) na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) com os produtos que serão vendidos e foram lançados no Pedido de Venda.

Em seguida, na tela Empenho de Produtos filtre o documento de compras e acione o botão Aplicar; automaticamente o documento de compra será apresentado na grade "Itens de compras" e o documento de venda na grade **"Itens de vendas"**. Após, utilize o botão Empenhar e, caso os dados estejam corretos, será apresentada a mensagem de Empenho gerado com sucesso.

Neste contexto, no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) selecione a Nota de Compra anteriormente lançada e clique sobre o botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Enviar para o WMS (Recebimento)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#enviarparaowmsrecebimento); em seguida, faça o preenchimento dos campos do pop-up **"Dados para Recebimento"** e, ao clicar em confirmar, uma mensagem de que o recebimento foi gerado será exibida.

Deve-se verificar na tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias) o recebimento gerado, sendo que, a **"Situação"** da tarefa, neste momento, deverá ser **"Aguardando Conferência"**.

Realizados os procedimentos acima, deve-se acessar o Coletor de Dados com o usuário responsável pela tarefa de **"Conferência"** e efetuar as seguintes configurações:

- Selecionar a função Conferência;
- Informar a Doca de entrada;
- Inserir a quantidade do produto que consta na nota;
- Informar o código de barras do produto;
- Repetir o procedimento de informar a doca, quantidade do produto e código de barras para todos os produtos do recebimento;
- Ao finalizar, clicar no botão **"Enviar"**; com isto, será apresentada uma mensagem de Conferência finalizada com sucesso.

Após realizar a configuração no Coletor, na tela Recebimento de Mercadorias, a Situação da tarefa será alterada para **"Aguardando Armazenagem"**.

Ainda na tela acima mencionada, acione o botão **"Gerar Tarefas"** (localizado no topo da tela); assim, será aberta a tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento) e nela realiza-se os procedimentos a seguir:

- Clique no botão **"Pré-visualizar"** e confirma se nas tarefas de armazenagem que serão geradas, algum dos endereços de destino é o Endereço Crossdocking criado inicialmente nas [Configurações necessárias para utilizar esta Rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#configuraesnecessriasparautilizarestarotina).
- Após, clicar no botão Gerar Tarefas.

Assim, na tela Recebimento de Mercadorias, a Situação da tarefa será ajustada para **"Enviado para Armazenagem"**.

Realizados os procedimentos acima, deve-se acessar o Coletor de Dados com o usuário responsável pela tarefa de **"Armazenagem"** e efetuar as seguintes configurações:

- Escolher o equipamento para armazenagem e clicar no botão **"Tarefa"**;
- Informar no campo **"Origem"** o endereço referente a Doca de entrada já exibido no Coletor;
- Inserir o código de barras do produto;
- Após isto, a tela do Coletor será direcionada para informar-se o endereço de destino de Crossdocking (já exibido no Coletor); assim, informe o endereço de armazenamento;
- Repetir o procedimento para os produtos restantes.

Após realizar a configuração no Coletor, na tela Recebimento de Mercadorias a Situação da tarefa será modificada para **"Armazenado"** e deve-se realizar os seguintes procedimentos:

- Acionar o botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#botesnotopodatela) e selecionar a opção **"Liberação da Doca"** para conclusão do recebimento e a liberação da Doca de entrada;
- Em seguida, verificar se a Situação foi alterada para **"Concluído"**;

Realizadas todas as configurações acima, deve-se realizar a criação de uma nova Ordem de Carga na tela [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga).

Logo após, faz-se necessário acessar a tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga), filtrar pelo número do Pedido de Venda lançado inicialmente e vinculá-lo à Ordem de Carga cadastrada; em seguida, clicar no botão **"Outras Opções..."** localizado no topo desta tela e selecionar a opção **"Enviar para Expedição por OC"**; realizar o preenchimento dos campos do pop-up **"Dados para Separação"**.

Ainda na tela acima mencionada, será possível verificar as colunas **"Situação WMS"** e **"Status WMS"**, que serão atualizadas para **"Enviado para separação"** e **"Enviado totalmente"**, respectivamente.

Neste contexto, deve-se acessar a tela [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias) para verificar a separação gerada; neste momento, a Situação da tarefa deverá ser **"Enviado para separação"**.

Realizados os procedimentos acima, deve-se acessar o Coletor de Dados, escolher a função **"Separação"**, definir o equipamento e acionar o botão Tarefa; após isto, efetuar as seguintes configurações:

- Informar no campo Origem o **"Endereço de Crossdocking"** e o **"Produto"**;
- Clicar no botão **"Destino"** e inserir o endereço de Checkout ou Doca de saída, quando for o caso; assim, apresenta-se uma mensagem informando que não há tarefas em aberto ou adequadas para o usuário.

Feito isto, na tela Expedição de Mercadorias a Situação da tarefa deverá ser **"Aguardando conferência"**.

Ao se encontrar com a situação acima mencionada, no Coletor de Dados deve-se escolher a função "Conferência por Pedido" e realizar o procedimento seguinte:

- Informar o Checkout ou a Doca de Saída onde encontram-se localizados os produtos, a quantidade e o código de barras;
- Repetir o procedimento caso existam mais produtos a serem conferidos;
- Ao finalizar a conferência, clicar no botão **"Enviar"** e, desta forma, será exibida a mensagem de conferência finalizada com sucesso.

Realizado o procedimento acima, na tela Expedição de Mercadorias a Situação da Tarefa será **"Conferência Validada"**; nesta tela ainda, clique no botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botesnotopodatela), opção **"Liberar Doca"** e, assim, estará caracterizado o fim do processo de Separação por produto.

Para finalizar, no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), realiza-se o Faturamento do Pedido de Venda, para que a saída dos produtos do estoque seja concretizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)

## Parâmetros que influenciam esta Rotina

Quando o parâmetro **"Armazenamento atômico picking crossdocking - ARMATOMPICKDOC"** está ativado, a movimentação de estoque ocorre automaticamente do endereço da doca de origem para o endereço de Crossdocking, sem a necessidade de intervenção manual via coletor de dados. O sistema cria automaticamente um registro de estoque no endereço de Crossdocking por meio da movimentação atômica, eliminando a necessidade de uma transação adicional.

**Observação:** durante a geração de [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento), o sistema identifica o parâmetro habilitado e gera automaticamente a tarefa atômica para o Crossdocking, já finalizada. Caso existam outros endereços para armazenamento, esses seguirão o fluxo padrão de geração de tarefas.

Quando o parâmetro **Libera separação de empenho com receb. parcial? (WMSLIBSEPRECPAR)** está ativado, a onda de um pedido empenhado é liberada assim que a quantidade empenhada do produto estiver armazenada no endereço de Crossdocking, sem esperar a situação **Concluído** do recebimento. Com ele ativado, o estoque do Crossdocking coberto por empenhos pendentes também fica reservado e não é oferecido a outros pedidos. O parâmetro está disponível a partir da versão 5.16.0 do módulo WMS.

Para saber mais, acesse [Processo Crossdocking Contínuo e Respeito ao Empenho](https://ajuda.sankhya.com.br/hc/pt-br/articles/43674876567831).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107713-Empenho-de-Produtos#top)
