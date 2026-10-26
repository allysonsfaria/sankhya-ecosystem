---
id: "360045110673"
titulo: "MDF-e - Manifesto de Documentos Fiscais Eletrônicos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:03Z"
rotulos: ["MDF-e", "Veículo", "Configuração", "XML", "SEFAZ", "Transporte", "DAMDFE", "Documentos", "Eletrônicos", "Fiscais", "Manifesto", "Viagem", "MDF-e - Manifesto de Documentos Fiscais Eletrônicos manual", "Documentação do MDF-e: Emissão e Configuração", "Documentos Eletrônicos"]
---

# MDF-e - Manifesto de Documentos Fiscais Eletrônicos

Trataremos nesta documentação, do MDF-e - Manifesto Eletrônico de Documentos Fiscais, que é um documento emitido e armazenado eletronicamente de existência apenas digital que visa vincular os documentos fiscais utilizados na operação e/ou prestação à unidade de carga utilizada no transporte, cuja validade jurídica é garantida pela assinatura digital do emitente e autorização de uso, pela administração tributária da UF (Unidade Federativa) do contribuinte.

O MDF-e deverá ser emitido por empresas prestadoras de serviço de transporte em casos de prestações com mais de um conhecimento de transporte, ou pelas demais empresas nas operações cujo transporte seja realizado em veículos próprios, arrendados, ou mediante contratação de transportador autônomo de cargas, com mais de uma nota fiscal.

O objetivo do MDF-e, é agilizar o registro em lote de documentos fiscais em trânsito, identificar a unidade de carga utilizada e demais características do transporte. A autorização de uso do MDF-e implicará em registro posterior dos eventos, nos documentos fiscais eletrônicos nele relacionados. O MDF-e deve ser emitido obrigatoriamente em todo território brasileiro.

Um segundo conceito importante a ser compreendido, é o de Viagem de Transporte. Uma viagem de transporte se trata de um processo em que a empresa fará várias entregas em vários destinos com base em uma determinada rota. Em uma única viagem é possível apresentar mais de um MDF-e, devido ao fato de que cada MDF-e possui somente uma UF de carregamento e uma UF de descarregamento. Por exemplo, em uma viagem que a empresa deverá entregar do estado de MG para GO, DF e BA, deverão ser emitidos três MDF-e's, sendo que estes três MDF-e's estarão em uma mesma viagem. Da mesma forma que, uma transportadora poderá apanhar a mercadoria nos estados de MG e SP e entregar no estado de GO, deverão ser emitidos dois MDF-e.

Alguns requisitos deverão ser atendidos para utilização deste recurso. São eles:

- Possuir o Sankhya OM/Jiva Evo na versão 3.14.4b6 ou superior;
- Possuir o Sankhya OM/Jiva Evo na versão 3.16.2b10 ou superior para contribuintes emitentes de CT-e;
- Possuir os produtos MANIFESTO DE DOC. FISCAIS ELETRÔNICO/W, COMERCIAL/W e NOTA FISCAL ELETRÔNICA/W/ JIVA MDFe/W, JIVA/W e JIVA NFe/W na licença de uso;
- Possuir os produtos MANIFESTO DE DOC. FISCAIS ELETRÔNICO/W, COMERCIAL/W e CONHECIMENTO DE TRANSPORTE ELETRÔNICO/W/ JIVA MDFe/W, JIVA/W e JIVA NFe/W na licença de uso, para contribuintes emitentes de CT-e;
- Possuir o SanNFe na versão 2.24b4 ou superior;
- Possuir o SanNFe na versão 2.26b4 ou superior, para contribuintes emitentes de CT-e;
- Possuir o certificado digital da empresa credenciada para emissão da NF-e e/ou CT-e.

A seguir, trataremos dos detalhes sobre as configurações a serem executadas no sistema, bem como seu consequente comportamento:

[Configurações no Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema)                                    [Geração da Viagem de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#geraodaviagemdetransporte)

[Transmissão dos manifestos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#transmissodosmanifestos)                                [Parâmetros que atuam sobre este recurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#parmetrosqueatuamsobreesterecurso)

## Configurações no Sistema

Abaixo, temos as configurações a serem realizadas no Sankhya-Om para posterior geração/impressão do MDF-e:

[Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#cadastrodeempresas)                                           [Preferências de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#prefernciasdeempresa)

[Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#cadastrodeveculos)                                              [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#ordensdecarga)

[Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#viagensdetransportemdf-e)                            [Modelos de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#modelosdeimpresso)

- **Cadastro de Empresas**

No [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas), presente na aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas#abanaturezas), tem-se o campo **"RNTRC"**; para utilização do MDF-e é essencial o preenchimento desta informação. Informe aqui a inscrição do transportador no Registro Nacional de Transportadores Rodoviários de Carga.

![Imagem 1: No Cadastro de Empresas , presente na aba Naturezas , tem-se o campo "RNTRC" ; para utilização do MDF-e é essencial o…](https://ajuda.sankhya.com.br/hc/article_attachments/9457540126615)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema)

- **Preferências de Empresa**

Uma vez posicionado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), na aba MDF-e, é necessário a definição do ambiente em que o MDF-e será emitido, a versão do MDF-e e a condição da empresa quanto ao transporte de cargas:

![Imagem 2: Uma vez posicionado nas Preferências da Empresa , na aba MDF-e , é necessário a definição do ambiente em que o MDF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/9457684267287)

Determine no **"Ambiente MDF-e"** qual o âmbito de emissão de MDF-e que a empresa se encaixa; tem-se as seguintes opções:

- **Não usa** **-** A empresa não faz uso de MDF-e;
- **Homologação** **-** Os MDF-e's emitidos pela empresa em questão, são válidos apenas para testes e simulações;
- **Produção** **-** Por esta opção, tem-se que a empresa gera efetivamente MDF-e's e estes serão devidamente validados pelos órgãos competentes.

A versão do layout de emissão do MDF-e é determinada no campo **"Versão MDF-e"**; temos as seguintes alternativas:

- Versão MDFe 1.00 - Através desta opção, o XML do MDF-e é gerado como é atualmente, mesmo com as configurações mencionadas neste tópico, ou seja, a tag **<versão>** filha da tag **<infMDFe>** será alimentada com 1.00;
- Versão MDFe 3.00 - Por meio desta alternativa, além do XML ser gerado considerando todas as configurações citadas neste tópico, a tag **<versão>** filha da tag **<infMDFe>** será preenchida com 3.00.

Quando a empresa for uma transportadora, por meio do campo **"Transportadora de cargas"** é preciso indicar se ela é uma ETC ou CTC. Esta informação é útil na geração da tag **<tpTransp>** presente no XML do MDF-e. Tem-se as seguintes opções:

- Empresa transportadora de cargas (ETC);
- Cooperativa transportadora de cargas (CTC).

Caso a empresa tenha participação no canal verde, a marcação **"Participa do canal verde?"** deverá ser acionada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema) 

- **Cadastro de Veículos**

As informações a respeito do [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-), devem ser definidas para os veículos de tração e para os reboques, caso existam. A saber:

**Aba Geral**

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/9457892129175)

No campo **"Tipo de rodado"** temos a opção **"00–Não Aplicável"**; o MDF-e não aceita esta opção como válida, portanto ao configurar os veículos do manifesto, você deve se atentar a este detalhe. Essa é uma opção empregada apenas para emissão de CT-e.

No campo **"Tipo de Carroceria"** determine qual é o tipo de carroceria do veículo em questão.

**Aba Propriedades**

![Imagem 4: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/9457895169047)

Nesta aba, é essencial o preenchimento dos seguintes dados:

- **Placa**;
- **Cidade Emplacamento:** Cidade em que o veículo foi emplacado; o estado (UF - unidade federativa) deve estar vinculado à cidade informada;
- **RENAVAM**;
- **Tara:** Corresponde ao peso próprio do veículo, acrescido dos pesos da carroçaria e equipamento, do combustível, das ferramentas e dos acessórios, da roda sobressalente, do extintor de incêndio e do fluído de arrefecimento, expressa em quilos;
- **Peso Máximo:** Capacidade máxima do veículo em quilos;
- **Metros Cúbicos Máximo**: Capacidade máxima do veículo em metros cúbicos;

Quando o veículo de tração ou reboque for de propriedade da empresa emitente do MDF-e, a marcação Veículo da empresa deve ser realizada, e no campo Parceiro ou Empresa insira a empresa emitente do MDF-e.

Caso o veículo de tração ou reboque seja de propriedade de terceiros, a opção Veículo da empresa deve ser desmarcada, e no campo Parceiro ou Empresa deve ser inserido o parceiro que é proprietário do veículo. Além disso, os campos Tipo de proprietário e RNTRC devem ser corretamente definidos.

Caso o veículo seja de propriedade de uma empresa cadastrada no sistema, porém essa empresa não é emissora do MDF-e, é preciso desmarcar a opção Veículo da empresa e vincular o parceiro correspondente dessa outra empresa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema) 

- **Ordens de carga**

Os processos de Cadastro de Ordens de Carga e Formação de Carga da empresa emitente do MDF-e, devem existir para fins de agilizar a geração dos manifestos na Viagem do Transporte. Casos referidos processos ainda não estejam definido na empresa, para maiores informações você pode consultar suas respectivas documentações por meio dos link's [Ordens de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga) e/ou [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga).

**Observação:** por se tratar de um documento eletrônico, informações de endereço, cadastro da empresa, veículos e parceiros (motoristas ou proprietários de veículos) devem ser clara e corretamente informados.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema) 

- **Viagens de Transporte (MDF-e)**

Através da tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-), deverão ser realizadas as configurações de numeração e impressão dos manifestos, para sua posterior emissão. Neste momento, direcionaremos o foco para o botão **"Outras Opções..."** presente na referida tela.

![Imagem 5: Através da tela Viagens de Transporte (MDF-e) , deverão ser realizadas as configurações de numeração e impressão dos…](https://ajuda.sankhya.com.br/hc/article_attachments/9457994358295)

**Controle de Numeração**

![Imagem 6: Controle de Numeração](https://ajuda.sankhya.com.br/hc/article_attachments/9458535495191)

Por meio desta opção, no pop-up Controle numeração do MDF-e que será aberto, defina a empresa emitente, a série empregada na numeração dos manifestos, o modelo de documento (no uso desta funcionalidade, o modelo deve ser 58), a numeração como automática (definição feita automaticamente), qual o último número de MDF-e emitido pela empresa e o limite de numeração dos manifestos.

**Preferências**

![Imagem 7: Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/9458639317655)

Ao acionar a opção Preferências, no pop-up de mesmo nome que será aberto, você pode estabelecer as seguintes particularidades:

- **Tipo de impressora:** O tipo da impressora na qual os manifestos serão impressos;
- **Caminho/impressora:** Determine qual o caminho ou nome da impressora em que os manifestos serão impressos;
- **Imprimir ao confirmar?:** Caso esta opção esteja marcada, quando os manifestos forem transmitidos e autorizados, sua respectiva impressão irá ocorrer automaticamente;
- **Modelo DAMDFE:** Defina aqui, qual o modelo formatado para impressão do DAMDFE;
- **Número de cópias DAMDFE:** Informe quantas cópias deverão ser impressas do DAMDFE;
- **Modelo DAMDFE Contingência:** Determine qual o modelo formatado para impressão do DAMDFE em contingência;
- **Número de cópias DAMDFE Contingência:** Informe quantas cópias deverão ser impressas do DAMDFE em contingência.

**Preferências do agendador de MDF-e em contingência**

![Imagem 8: Preferências do agendador de MDF-e em contingência](https://ajuda.sankhya.com.br/hc/article_attachments/9458711213463)

Através desta opção, é possível determinar a periodicidade em que o sistema deverá executar a tarefa de verificação da existência de manifestos emitidos em contingência e automaticamente gerá-los no ambiente de autorização normal.

No pop-up que é aberto por esta opção, temos o botão **"Forçar execução"**, que executa a tarefa no momento em que é acionado. A marcação **"Ativo"** determina se o agendador está ou não operante. Na aba **"Frequência Agendamento"** determine em que horário do dia o sistema irá executar a tarefa; além disso, estabeleça se a frequência de execução dessa tarefa será Diária ou Semanal. Na aba **"Horários"**, o campo Próxima execução em será utilizado pelo sistema automaticamente; já no campo Data Final de Execução determine qual a data e hora para o agendador paralisar sua execução.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema) 

- **Modelos de Impressão**

Na tela [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-) temos o botão **"Baixar Modelos Padrões"**; dentro dele, temos as seguintes opções de baixa de modelos:

- DAMDFE retrato;
- DAMDFE paisagem;
- DAMDFE em contingência retrato;
- DAMDFE em contingência paisagem.

![Imagem 9: DAMDFE em contingência paisagem.](https://ajuda.sankhya.com.br/hc/article_attachments/9458683740439)

A partir disto, será possível criar o modelo de impressão utilizando os modelos previamente cadastrados no sistema, e vinculá-los nas Preferências de impressão na tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-#bot%C3%A3ooutrasop%C3%A7%C3%B5es), opção **"Preferências"** mencionadas no tópico anterior.

**Observação:** para esses modelos de DAMDFE tem-se a possibilidade de impressão do MDF-e que esteja com status **"Encerrado"** na tela acima mencionada, aba [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-#abamdf-e), sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025390913-Viagens-de-Transportes-MDF-e-#sub-abageral), campo **"Status MDF-e"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#configuraesnosistema)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#top)

## Geração da Viagem de Transporte

Nessa seção, abordaremos os seguintes tópicos:

[Criação da Viagem de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#criaodaviagemdetransporte)                                     [Geração dos manifestos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#geraodosmanifestos)

**Criação da Viagem de Transporte**

Para geração de uma Viagem de Transporte, é necessário que uma Ordem de Carga esteja cadastrada e seja composta pelas devidas Notas ou Conhecimentos vinculados. Para vincular tais documentos à Ordem de Carga, a rotina de Formação de Carga pode ser empregada.

Na tela Ordem de Carga, temos o botão **"Criar Viagem"**, que ao ser acionado, o sistema verifica se existem Notas Fiscais ou Conhecimentos de Transporte que podem ser inseridos na geração dos Manifestos; caso nenhum documento seja localizado, será exibida a seguinte mensagem:

**"Não foram encontrados documentos de venda, devolução de compra, devolução de venda, transferência ou conhecimento de transporte na(s) ordem(ns) de carga com o modelo de documento 1, 1B, 4, 8, 55 ou 57."**

Caso o sistema encontre normalmente os documentos a serem gerados nos manifestos, a viagem será gerada com sucesso, e a tela Viagens de Transporte (MDF-e) já será aberta posicionada na viagem recentemente criada.

Quando em uma mesma ordem de carga existirem documentos que são Notas Fiscais e Conhecimentos de Transporte, ao criar a viagem, a seguinte mensagem será apresentada:

**"Não é permitido que a ordem de carga geradora da viagem tenha documentos de nota e conhecimento de transporte."**

As duas validações mencionadas acima, estão presentes também no momento da inserção de uma Ordem de Carga de forma manual diretamente na tela Viagens de Transporte (MDF-e).

Caso a empresa emitente do MDF-e seja prestadora de serviço de transporte, e tenha-se na mesma Ordem de Carga Notas Fiscais e Conhecimento de Transporte vinculados, você pode ativar o parâmetro **"Extrair somente CT-e de OC contendo NF-e/CT-e? - GERASOCTEMDFE"**; caso o referido parâmetro esteja ligado, ao criar a viagem, somente os Conhecimentos de Transporte serão considerados na criação da viagem.

Além disso, na tela Ordens de Carga, você pode localizar qualquer ordem de carga e em seguida abrir a viagem a ela vinculada através do botão **"Abrir Viagem"**, assim como fazer o procedimento inverso, ou seja, desvincular a ordem de carga da viagem por meio do botão **"Desvincular Viagem"**.

**Observação:** será possível desvincular a ordem de carga de uma viagem, somente se os manifestos dessa viagem não forem transmitidos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#geraodaviagemdetransporte)

**Geração dos manifestos**

Na tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-) você pode lançar todas as informações pertinentes ao manifesto manualmente ou agilizar a inserção destes dados criando a viagem por meio da [Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga).

Na aba **"Geral"**, as informações pertinentes à Empresa e Veículo de tração são carregadas de acordo com o definido na Ordem de Carga; Série e Reboques podem ser determinados manualmente. O **"Tip. Amb. MDF-e"** é indicado de acordo com o que foi previamente configurado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#prefernciasdeempresa).

![Imagem 10: Na aba " Geral" , as informações pertinentes à Empresa e Veículo de tração são carregadas de acordo com o definido na…](https://ajuda.sankhya.com.br/hc/article_attachments/9458706358039)

Na aba MDF-e visualize inicialmente a **"Sequência do manifesto"** na viagem; dentro desta aba, temos também a aba **"Geral"** que apresenta todas as informações dos manifestos daquela viagem por estado de descarregamento.

O campo **"Nro. do MDF-e"** se refere ao número do manifesto gerado a partir do controle de numeração;

Os **"Status do MDF-e"** podem ser:

- **Não transmitido:** O manifesto ainda não foi enviado à SEFAZ;
- **Enviado:** O manifesto foi enviado à SEFAZ mas não obteve uma resposta;
- **Aguardando autorização:** O manifesto foi enviado à SEFAZ, mas não foi autorizado nem rejeitado;
- **Autorizado:** O manifesto foi enviado para a SEFAZ e autorizado;
- **Aguardando correção:** O manifesto foi enviado à SEFAZ mas foi rejeitado, e após ser devidamente ajustado, poderá ser reenviado;
- **Cancelado:** O manifesto foi cancelado pelo emitente;
- **Encerrado:** O manifesto foi encerrado pelo emitente;
- **Denegado:** O manifesto foi enviado à SEFAZ, mas foi denegado, ou seja, recusado por conter algum dado improcedente;
- **Com erro de validação:** O manifesto não foi enviado para a SEFAZ por problemas de formação no XML;
- **Enviado em contingência:** O manifesto não foi enviado para a SEFAZ por falta de comunicação, mas foi impresso em contingência.

**Observação:** o MDF-e que esteja com o status **"Encerrado"** poderá ser impresso da mesma maneira que o MDF-e com status **"Autorizado"** ou **"Enviado em contingência"** são impressos atualmente, seguindo portanto, as mesmas regras e validações.

O campo **"Nro. aleatório"** representa o número aleatório gerado para calcular a chave de acesso;

Em relação ao campo **"Chave do MDF-e"**, este se refere a chave de acesso do manifesto;

Preencha o campo **"Nro. do recibo"** com o número do recibo de autorização;

Informe no campo **"Dt. e hora do recebimento"** a data e hora do recebimento e autorização e no campo **"Dt. e hora da emissão"** a data e hora da emissão do manifesto;

Em **"Tipo da emissão"**, temos as seguintes alternativas:

- **Normal:** O manifesto foi ou será enviado à SEFAZ;
- **Contingência:** O manifesto foi impresso em contingência.

Informe em **"UF de Coleta"** o Estado em que a mercadoria das notas do manifesto foram coletadas;

No campo **"UF de Descarregamento"** informe o Estado em que toda a mercadoria das notas do manifesto serão descarregadas;

Preencha o campo **"Nro. lote"** com o número do lote de emissão;

Determine em **"Unidade de medida"**, a unidade de medida que a mercadoria transportada no MDF-e possui.

A respeito do campo Unidade de medida, no caso de notas fiscais, sempre será considerado o peso bruto de seu cabeçalho e este campo será preenchido com a informação KG. Já no caso de CT-e será considerada sua unidade de medida definida na aba Unidades de Medida do CT-e. Caso os conhecimentos possuam mais de uma unidade de medida definida, este campo ficará em branco para preenchimento manual. Caso os conhecimentos possuam somente uma unidade de KG ou TON o campo será preenchido automaticamente com KG ou TON conforme conhecimentos.

O campo **"Peso Bruto Total"** corresponde à quantidade total de medida definida nos documentos.

No caso de Notas Fiscais, o Peso Bruto Total será a soma do peso bruto das notas. Já nos conhecimentos, será a soma das quantidades de medida dos conhecimentos do manifesto. Vale mencionar que o campo somente será preenchido automaticamente, se todos os conhecimentos possuírem a mesma unidade de medida, "KG" ou "TON".

**Observação:** mesmo que os campos Unidade de Medida e Peso Bruto Total sejam definidos automaticamente, para as notas, o valor real considerado no XML é o campo correspondente ao peso bruto da nota e não do manifesto, ou seja, no caso de notas, esses campos são utilizados apenas para demonstrar a soma do peso bruto das notas, no momento da criação da viagem.

Também dentro da aba MDF-e, a aba **"Eventos"** possui informações de quais eventos foram transmitidos para o manifesto, tais como a **"Sequência do Evento"**, **"Código do Evento"**, **"Data e hora do recebimento"** e o **"Status de Retorno do Evento"**. Além disso, contém as informações pertinentes a cada evento, por exemplo, se o evento for cancelamento é possível visualizar sua justificativa, se for o evento de encerramento é possível visualizar em qual cidade e estado o manifesto foi encerrado, se for o evento de inclusão de condutor, é possível visualizar qual motorista foi incluído, e assim sucessivamente. O arquivo XML transmitido para o evento também poderá ser consultado.

Na aba **"Documentos MDF-e"** podem ser visualizados dados básicos do documento, como seu **"Número"**, **"Empresa"**, **"Ordem de Carga"**, **"Parceiro"**, **"Valor da nota"** etc. É possível ainda incluir documentos manualmente nessa aba, desde que o documento em questão esteja vinculado à ordem de carga que está vinculada na viagem e que possui destino igual ao estado de descarregamento do manifesto.

Por fim, dentro da aba MDF-e, a aba **"UFs do percurso"** é utilizada pra informar quais são os estados que o veículo irá percorrer desde sua origem até seu destino. Por exemplo, se a origem for de MG - Minas Gerais e o destino do manifesto for DF - Distrito Federal, o veículo deverá passar pelo estado de GO - Goiás, portanto, GO - Goiás deverá ser informado nessa aba.

Na aba **"Motorista"**, o motorista é sugerido de acordo com a Ordem de Carga; mas ainda assim, sendo o caso, você pode determinar mais motoristas, chegando ao máximo de 10 (dez).

![Imagem 11: Na aba " Motorista" , o motorista é sugerido de acordo com a Ordem de Carga ; mas ainda assim, sendo o caso, você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/9459195779223)

Na aba **"Ordem de Carga"** você pode adicionar ordens de carga que possuem documentos a serem acrescentados nos manifestos já formados mas que não foram emitidos. Ao acrescentar as ordens de carga, o sistema irá localizar em qual manifesto cada documento precisa ser adicionado.

![Imagem 12: Na aba " Ordem de Carga" você pode adicionar ordens de carga que possuem documentos a serem acrescentados nos…](https://ajuda.sankhya.com.br/hc/article_attachments/9459199252631)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#geraodaviagemdetransporte)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#top)

## Transmissão dos manifestos

Na tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-) tem-se o botão **"Confirmar"**, que sobretudo transmite todos os manifestos gerados da viagem para a SEFAZ, um por vez. Todos podem ser autorizados, ou ainda um ou todos também podem ser rejeitados; para cada manifesto, seu status poderá ser visualizado. A grande vantagem da utilização deste botão, é a transmissão de todos os manifestos automaticamente.

Note nesta tela também, o botão **"Cancelar"**, que deve ser utilizado para cancelar todos os manifestos de viagem de uma vez. Vale citar que a justificativa informada para o cancelamento, será a mesma para todos os manifestos.

Além disso, na aba MDF-e, temos também o botão **"Confirmar"**, que é utilizado para transmitir somente o manifesto selecionado na aba. Seguindo o mesmo raciocínio, o botão **"Cancelar"** dessa aba também só realiza o cancelamento do manifesto selecionado. Da mesma maneira, o botão **"Encerrar"** só o faz, no manifesto em questão. Esta aba conta também com o botão para impressão do DAMDFE do manifesto selecionado, conforme Preferências de Impressão já mencionadas.

Dentro da aba MDF-e, tem-se o botão **"MDF-e"**:

![Imagem 13: Dentro da aba MDF-e , tem-se o botão "MDF-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/9459226375191)

As opções existentes no botão MDF-e, são:

**Consultar status do serviço:** verifica se o serviço de transmissão do MDF-e está em operação;

**Consulta situação atual do manifesto:** consulta a situação do manifesto em questão junto à SEFAZ;

**Gerar arquivo XML de MDF-e:** esta opção gera o arquivo XML do MDF-e autorizado;

**Gerar arquivo XML de MDF-e para conferência:** gera o arquivo XML do MDF-e sem informações de autorização, apenas para conferência (análise) de dados;

**Gerar MDF-e em contingência:** esta opção deve ser empregada quando o serviço de transmissão normal está fora do ar; ao acioná-la, o sistema gera a chave de acesso do MDF-e em contingência e imprime o DAMDFE em contingência;

**Gerar lote:** tem-se por esta opção, a geração do lote do manifesto;

**Buscar autorização:** em casos em que o manifesto está com o status Aguardando Autorização, esta opção busca esta autorização junto à SEFAZ;

**Incluir condutor:** esta opção inclui um condutor no manifesto - evento de inclusão de condutor;

**Ver acompanhamentos:** tem-se aqui, a consulta de todas as ocorrências registradas para o manifesto.

**Importante:** após a transmissão do MDF-e com êxito, sua impressão poderá ser feita para que o veículo siga viagem. Posteriormente o MDF-e precisa ser encerrado para que não haja bloqueio da placa e percurso.  

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#top)

## Parâmetros que atuam sobre este recurso

**Gerar tpTransp p/ propr. de veículo pessoa física? - GERATPTRANSPPF:** quando desligado, não será gerada a tag **<tpTransp>** se o emitente não for prestador de serviço de transporte e o proprietário do veículo for pessoa física.

**Validar Confirmação Op. DF-e em Nota Confirmada? - VALCONFOPDFE:** ao ligar esse parâmetro, o sistema irá verificar se a nota já foi confirmada, se sim, não será possível utilizar a opção **"Confirmo a operação"** do botão **"MD-e"** da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) quando houver operações com MD-e. Porém, quando desativado, essa opção poderá ser utilizada mesmo que a nota já tenha sido confirmada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673-MDF-e-Manifesto-de-Documentos-Fiscais-Eletr%C3%B4nicos#top)

![Imagem 14: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16646377936279) Acesse também:

[Nota Técnica 2018.002 - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599734-Nota-T%C3%A9cnica-2018-002-MDF-e)
