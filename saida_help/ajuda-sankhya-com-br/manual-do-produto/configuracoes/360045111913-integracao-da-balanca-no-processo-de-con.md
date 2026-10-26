---
id: "360045111913"
titulo: "Integração da balança no Processo de Conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:30Z"
rotulos: ["Produtos", "Conferência", "Configuração", "WMS", "NF-e", "SPS", "Integração", "Estoque", "Balança", "IMEI", "Número Serial", "Web Connection", "Integração da balança no Processo de Conferência manual", "Processo de Conferência e Recebimento: Detalhes e Configurações"]
---

# Integração da balança no Processo de Conferência

Em um processo de conferência, existem várias etapas antes de faturar a nota para entrega. Tem-se a etapa de conferência dos produtos através do código de barras, IMEI ou número de série, em seguida, a etapa em que é feita a pesagem dos produtos conferidos e, por fim, a impressão da etiqueta seguida da geração e impressão do DANFE.

Tratando-se do recebimento, quando o fornecedor efetua a entrega na empresa existem dois processos de conferência, são eles:

- O processo de conferência da quantidade real entregue, visa a entrada no estoque da quantidade real recebida do item. Como a unidade de medida do produto é peso, utiliza-se uma balança para aferir o peso líquido do item que está sendo recebido.
- O segundo detalhe do processo de conferência consiste em como o peso líquido é obtido, visto que os produtos podem contar com pelo menos 2 embalagens e o elemento utilizado para movimentação que possui um peso variável. Analisemos melhor no exemplo prático descrito abaixo:

**Elemento de movimentação:** A empresa utiliza paletes para acondicionar os produtos internamente na empresa assim como para efetuar a movimentação deste. Cerca de 40% dos paletes possuem peso variável em função de diversas variáveis (molhado, parte A quebrada, parte B quebrada, etc);

**Primeira embalagem:** Alguns fornecedores entregam os produtos em caixas plásticas ou grandes sacos (big bags);

**Segunda embalagem:** Os fornecedores utilizam também uma segunda embalagem. Cada uma destas embalagem (saquinhos) contém uma pesagem e são acondicionados dentro da primeira embalagem.

Deste modo, torna-se necessário discriminar as taras pertinentes ao peso do elemento de movimentação, bem como, o peso de cada embalagem para chegar ao peso líquido do produto.

As informações abaixo, visam aprimorar a conferência do sistema a fim de atender a estas etapas na empresa. Vejamos:

#### Peso do Volume

| [Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#cadastrosdeprodutos) |
| --- |
| [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#configuraodeconferncia) |
| [Comportamento da tela "Fila de Conferência"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#comportamentodatelafiladeconferncia) |
| [Gerar XML da NF-e contendo o IMEI ou Número Serial dos produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#gerarxmldanf-econtendooimeiounmeroserialdosprodutos) |
| [Integração da balança - Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#integraodabalana-webconnection) |
| [Integração da balança - Sankhya Print Service (SPS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#integraodabalana-sankhyaprintservicesps) |

#### Obter Quantidade pela Balança

| [Cadastro de Unidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#cadastrodeunidades) |
| --- |
| [Unidades de Movimentação e Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#unidadesdemovimentaoearmazenagem) |
| [Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#cadastrosdeprodutos) |
| [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#configuraodeconferncia) |
| [Comportamento da tela "Fila de Conferência"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#comportamentodatelafiladeconferncia) |

## Cadastros de Produtos

![Imagem 1: Cadastros de Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/4852391120663)

Na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) tem-se na aba Geral os campos **"Qtd. Identificadores"**, onde deve-se informar a quantidade de identificadores exigidos pelo produto, e o campo **"Tipo Identificador"**, onde determina-se qual o identificador a ser considerado para o produto em questão; este último campo pode ser definido dentre as seguintes opções:

- Número Serial;
- IMEI.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Configuração de Conferência

![Imagem 2: Configuração de Conferência](https://ajuda.sankhya.com.br/hc/article_attachments/4852497214743)

Na tela de [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia) deve-se atentar às definições feitas nos campos abaixo, de modo que estas influenciarão no Processo de Conferência, desde que o pedido/nota a ser conferido possuam no [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) a eles vinculados, a configuração de conferência devidamente estruturada. São elas:

#### Aba Geral

Através do campo **"Registrar peso"** determina-se qual o mecanismo de pesagem utilizado na conferência. Este campo possui as seguintes opções:

- **Não registrar:** Através desta opção, o processo de conferência não exigirá pesagem de qualquer mercadoria;
- **Pela balança:** Quando marcada esta opção, ao finalizar a conferência, o sistema abrirá um pop-up com um campo de peso que somente poderá ser preenchido pela pesagem da balança;
- **Balança/Manual:** Esta opção é semelhante à anterior, porém, caso a balança não consiga obter o peso automaticamente, será habilitado um campo a para que o usuário digite o peso da mercadoria manualmente; esta digitação somente será permitida para números positivos e com vírgula, caso necessário;
- **Manualmente:** Marcando-se esta opção, ao finalizar a conferência, o sistema abrirá um pop-up com somente com um campo de peso para digitação do peso da mercadoria.

**Observações:**

Para as opções em que se obtém o peso da mercadoria através da balança ou este é informado manualmente, o sistema irá gravar o mesmo no peso bruto do pedido que está sendo conferido.

Ao obter o peso via balança complemente, a finalização da conferência será efetivada automaticamente. Considera-se que o peso via balança foi obtido, quando a balança estiver com um valor de peso maior que zero e estável.

Ao obter o peso manualmente, depois que este é informado, tem-se a conclusão da operação, finalizando a conferência efetivamente.

Em qualquer uma das situações, caso a obtenção do peso via balança ou manualmente não seja efetivada, a conferência não poderá ser finalizada.

Quando o mecanismo de pesagem estiver diferente da opção **"Não registrar"**, caso a conferência esteja configurada para faturar o pedido conferido em nota, o sistema irá preservar o peso bruto do pedido na nota faturada.

Define-se no campo **"Exige identificador do produto"** como se dará a exigência do identificador dos produtos. Tem-se as seguintes opções:

- **Exige um:** Por esta opção, ao informar o produto, o sistema irá exigir a informação de apenas um IMEI ou Número Serial, independente da quantidade de identificadores definida no Cadastro de Produtos;
- **Exige todos:** Quando marcada esta opção, ao informar o produto, o sistema irá exigir a informação do IMEI ou Número Serial de acordo com a quantidade de identificadores definida no Cadastro de Produtos;
- **Não exige:** Através desta opção, ao informar o produto, não será exigida qualquer informação de IMEI ou Número Serial.

Quando informado o produto, e a configuração da conferência exigir o identificador, o sistema irá apresentar um pop-up para que seja informado o IMEI ou Número Serial.

Se forem adicionados mais ou menos identificadores do que o exigido pelo produto, o sistema irá emitir uma mensagem de confirmação informando que a quantidade de identificadores está diferente da quantidade conferida e se o usuário deseja ajustar; caso seja selecionado **"Sim"**, o sistema irá remover ou adicionar uma ou mais à quantidade conferida do produto.

Na tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia), grade **"Itens Conferidos"**, tem-se o botão **"Identificador"** para que nos casos em que a conferência exige esta informação, seja possível consultar ou remover os identificadores do produto. Ao clicar no referido botão, o sistema apresenta o pop-up contendo os identificadores inseridos. Caso algum identificador seja removido, a tela somente poderá ser fechada caso todos os identificadores do produto sejam informados conforme exigência da conferência.

Mantendo a marcação **"Inibir mensagem de confirmação ao finalizar conferência"** não realizada (situação padrão), no momento em que o usuário clicar no botão **"Finalizar conferência"** na tela de Fila de Conferência, o sistema exibirá uma mensagem questionando se o usuário deseja realmente finalizar a conferência; caso o campo esteja marcado, essa mensagem não será apresentada e a conferência será finalizada.

#### Aba Formação de volumes

No campo **"Formação de volumes"** quando a opção **"Registro simplificado (na tela)"** estiver selecionada, ao lado do botão de "Finalizar Conferência" será apresentado um botão de adição e remoção juntamente ao campo para quantidade; este campo para quantidade não aceita valores negativos. Além disso, quando o usuário clicar no botão de "Finalizar Conferência", o sistema não irá exibir o pop-up para que seja informada a quantidade de volumes.

O campo **"Imprimir etiquetas ao finalizar a conferência"** estará habilitado quando o campo "Formação de volumes" estiver definido com uma opção diferente de "Não usa formação de volumes". Na finalização da conferência, caso o campo citado esteja marcado, e o campo "Formação de volumes" esteja definido como "Registro simplificado (no final)" ou "Registro simplificado (na tela)" a impressão da etiqueta irá ocorrer como se fosse para apenas um volume, e com o número de cópias de acordo com a quantidade de volumes definida na Conferência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Comportamento da tela "Fila de Conferência"

Ao abrir a tela **"Fila de Conferência"**, o sistema irá posicionar o cursor automaticamente no campo de **"Nro. único"**. Além disso, o usuário pode bipar um código de barras que identifica o número único de uma nota ou pedido; nesse momento, o sistema irá abrir a fila de conferência já posicionando o código de barras dos produtos a serem conferidos.

Da mesma forma, se for digitado o número único do pedido ou nota e sendo pressionada a tecla **"Enter"** no teclado, o sistema irá abrir também a fila de conferência já posicionando o código de barras dos produtos.

Caso o sistema não encontre o pedido ou nota a ser conferido pelo número único bipado ou informado, a tela permanece em seu status inicial.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Gerar XML da NF-e contendo o IMEI ou Número Serial dos produtos

Na finalização da conferência, caso haja o faturamento do pedido em NF-e, o sistema gera o XML e transmite para a SEFAZ. Nesse momento da geração do XML, o sistema valida se a mercadoria referente a nota que foi conferida possui IMEI ou Número Serial.

Caso possua essas informações, o XML será gerado contendo as informações do IMEI ou Número Serial de modo que os campos do XML abaixo sejam gerados:

- **<obsCont xCampo="IDENTIFICADOR">** onde IDENTIFICADOR é igual ao IMEI ou Número Serial. Esta definição ocorre de acordo com o Cadastro do Produto.
- **<xTexto>\*IMEI1\*IMEI2</xTexto>** onde IMEI1 se refere ao valor do primeiro IMEI do produto e IMEI2 do segundo. Nesse exemplo, o produto possui o IMEI como identificador e a quantidade de identificador igual a dois. Quando o produto possui mais de um identificador, esses devem ser separados por um asterisco.

**Observação:** para que o IMEI/Serial sejam gerados na tag **<xTexto>** do XML, deve-se inserir uma query para buscar os valores no parâmetro **"Consulta para informação adcional no XML da nota - QUEINFADCXMLNFE"**.

Desta forma, na emissão do XML, o sistema irá gerar um grupo **<obsCont>** para cada linha retornada desta consulta, contendo as informações dentro das tags **<xCampo>** e **<xTexto>**.

**Nota:** se a consulta retornar valores vazios, a tag será gerada no XML com o valor vazio e a NF-e será rejeitada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Integração da balança - Web Connection

Uma das aplicações ligadas à esta integração da balança na Conferência, é o Sankhya Web Connection. Com esta aplicação uma vez instalada, a mesma será a ponte de comunicação entre a balança e o Sankhya- W, por meio da porta serial COM. A configuração da aba **"Integração balança"** é primordial para o obtenção do peso junto à balança e direcionamento desta informação para o Sankhya-W.

![Imagem 3: Uma das aplicações ligadas à esta integração da balança na Conferência, é o Sankhya Web Connection . Com esta aplicação…](https://ajuda.sankhya.com.br/hc/article_attachments/4852704567319)

Na opção **"Integração com a balança"** define-se qual a balança a ser utilizada, tem-se as seguintes opções:

- Não usa;
- DIGITRON;
- Filizola (IDM);
- Toledo (P3);
- Outra - Serial.

**Observação:** as configurações necessárias para utilização de cada uma destas opções, podem ser visualizadas na documentação [Sankhya Web Connection - Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection#sankhyawebconnection-configuraes).

Na **"Porta de comunicação"** configura-se a porta que a balança está instalada; nesta deve ser configurada exatamente a porta a qual a balança está instalada, pois caso seja informada outra porta, a comunicação não será realizada impossibilitando buscar o preço retornado pela mesma.

No campo **"Quantidade de dígitos do display"** define-se a quantidade de dígitos que foi determinada no display da balança; geralmente as balanças são de 5 dígitos; esta informação é utilizada para formatar o retorno da balança para o sistema.

A balança e o software que realiza a leitura devem estar na mesma frequência, pois ambos precisam se comunicar corretamente. Esta informação é inserida no campo **"Frequência de transmissão"**. Se um estiver com uma frequência mais alta que o outro, pode-se ter erros de leitura do peso. O padrão é **"9600"** que é o valor geralmente utilizado pelas balanças.

Na opção **"Tempo de espera de estabilização"**, define-se o tempo de timeout, ou seja, um tempo que o sistema deverá aguardar para que a balança retorne o peso estabilizado de acordo com o esperado. Caso este tempo exceda, será apresentada uma mensagem informando que não foi possível estabilizar a balança a tempo. Este tempo é fornecido em segundos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Integração da balança - Sankhya Print Service (SPS)

Além do Sankhya Web Connection mencionado acima, a aplicação [Sankhya Print Service - SPS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025395073-Sankhya-Print-Service) realiza a intermediação das impressões de etiquetas e Notas Fiscais acerca do processo de integração da balança na Conferência. Em linhas gerais, o SPS irá realizar o direcionamento de quais impressões (etiquetas e notas fiscais) devem ser encaminhadas para quais impressoras.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Cadastro de Unidades

No [Cadastro de Unidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597094-Unidades) é necessário acionar a marcação **"Utiliza Conferência por peso"** para indicar que a unidade irá utilizar o processo de conferência por peso.

![Imagem 4: No Cadastro de Unidades é necessário acionar a marcação "Utiliza Conferência por peso" para indicar que a unidade irá…](https://ajuda.sankhya.com.br/hc/article_attachments/4852792231575)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Unidades de Movimentação e Armazenagem

Na tela [Unidades de Movimentação e Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595714-Unidades-de-Movimenta%C3%A7%C3%A3o-e-Armazenagem) efetua-se o cadastro das unidades de movimentação e armazenagem do produto que serão utilizadas no ato da conferência.

![Imagem 5: Na tela Unidades de Movimentação e Armazenagem efetua-se o cadastro das unidades de movimentação e armazenagem do…](https://ajuda.sankhya.com.br/hc/article_attachments/4852842242199)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Cadastros de Produtos

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) tem-se a aba [Unidade de Mov./Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#unidadedemov.armazenagem) que será responsável pela ligação entre o produto e a(s) unidade(s) de movimentação e armazenagem cadastrada(s).

![Imagem 6: No Cadastro de Produtos tem-se a aba Unidade de Mov./Armazenagem que será responsável pela ligação entre o produto e…](https://ajuda.sankhya.com.br/hc/article_attachments/4853054462487)

No campo **"U.M.A"** será(ão) indicada(s) a unidade(s) de movimentação e armazenagem configurada(s) anteriormente.

O campo **"Código de Barras"** permite realizar a busca do produto e unidade de movimentação através do seu código de barras no ato da Conferência. Sendo que, para tanto é necessário que na [Configuração da Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia) em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral), o campo **"Buscar código de barras por"** esteja configurado com a opção **"Referência"**.

Informa-se no campo **"Volume"** a unidade previamente configurada como Unidade Padrão ou Unidade Alternativa do produto.

Caso o campo **"Padrão"** esteja habilitado, tem-se que esta unidade de mov./armazenagem será utilizada como padrão no ato da conferência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Configuração de Conferência

Além das configurações padrão, na seção **"Peso/Balança"** configura-se o campo **"Obter quantidade pela balança"** e caso seja necessário realizar a impressão de etiquetas define-se no campo **"Modelo p/ etiqueta"** um modelo de etiqueta.

![Imagem 7: Além das configurações padrão, na seção "Peso/Balança" configura-se o campo "Obter quantidade pela balança" e caso seja…](https://ajuda.sankhya.com.br/hc/article_attachments/4853124931991)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

## Comportamento da tela "Fila de Conferência"

Na Fila de Conferência ao inserir o produto tem-se a exibição do pop-up **"Seleção da U.M.A"** contendo o peso bruto (peso obtido na balança) e a unidade de movimentação padrão.

![Imagem 8: Na Fila de Conferência ao inserir o produto tem-se a exibição do pop-up "Seleção da U.M.A" contendo o peso bruto (peso…](https://ajuda.sankhya.com.br/hc/article_attachments/5009262881559)

Deste modo, efetua-se o registro das taras variáveis para chegar ao peso líquido do produto. Para tanto, clica-se no botão **"Tarar"** para que o peso obtido seja inserido no campo **"Tara 1 (variável)"**. Neste caso, foi utilizado um palete de 45kg:

![Imagem 9: Deste modo, efetua-se o registro das taras variáveis para chegar ao peso líquido do produto. Para tanto, clica-se no…](https://ajuda.sankhya.com.br/hc/article_attachments/5009276271767)

Após este passo, informa-se a quantidade da U.M.A padrão utilizada na pesagem. Como por exemplo 50 sacos plásticos de 1kg cada:

![Imagem 10: Após este passo, informa-se a quantidade da U.M.A padrão utilizada na pesagem. Como por exemplo 50 sacos plásticos de…](https://ajuda.sankhya.com.br/hc/article_attachments/5009248384663)

Caso seja necessário realizar a inclusão de outras U.M.A, basta acionar o botão ![Imagem 11: Caso seja necessário realizar a inclusão de outras U.M.A, basta acionar o botão . Ao clicar no botão "Confirmar" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/5009317817367). Ao clicar no botão **"Confirmar"**, ocorre a finalização da conferência e caso tenha sido configurado tem-se o processo de impressão das etiquetas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia#top)

![Imagem 12: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16637234999319) Acesse também:

[Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia)

[Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)
