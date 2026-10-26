---
id: "360045112353"
titulo: "MD-e - Manifestação do Destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112353-MD-e-Manifesta%C3%A7%C3%A3o-do-Destinat%C3%A1rio"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > Comum a todos os documentos"
atualizado_em: "2026-09-15T15:06:07Z"
rotulos: ["Configuração", "Eventos", "NF-e", "Configuração MD-e", "XML", "Importação", "SEFAZ", "Manifestação do Destinatário", "MD-e", "MD-e - Manifestação do Destinatário manual", "SERVERHOSTSCHED", "Manifestação do Destinatário: Configuração e Utilização", "Documentos Eletrônicos"]
---

# MD-e - Manifestação do Destinatário

Trataremos aqui, como proceder para realização correta da configuração do processo de Manifestação do Destinatário, bem como efetuar sua exata utilização.

#### O que é Manifestação do Destinatário?

Trata-se de um processo em que o destinatário de uma Nota Fiscal Eletrônica se manifesta para a SEFAZ, comunicando ao órgão qual a realidade em relação à nota fiscal emitida para ele. O destinatário poderá comunicar à SEFAZ quatro eventos de manifestação. São eles:

- **Ciência da Operação:** O destinatário declara ter ciência da operação destinada a seu CNPJ, mas ainda não possui elementos suficientes para apresentar uma manifestação conclusiva;
- **Confirmação da Operação:** O destinatário confirma a ocorrência da operação e o recebimento da mercadoria;
- **Desconhecimento da Operação:** Neste caso, o destinatário declara o desconhecimento da operação, não reconhecendo a emissão da Nota Fiscal Eletrônica destinada ao seu CNPJ;
- **Operação não Realizada:** Utiliza-se este evento, quando o destinatário declara que a operação não foi realizada (com recusa do recebimento da mercadoria e/ou outros) e a justificativa pela qual a operação não se realizou.

Além desses eventos que o destinatário poderá comunicar à SEFAZ, existem dois serviços que este também poderá utilizar, sendo os seguintes:

- **Consulta das Notas:** Este serviço, basicamente consulta na SEFAZ quais foram as Notas Fiscais Eletrônicas emitidas para o CNPJ do destinatário;
- **Download do XML das notas:** Por este serviço, realiza-se o download do XML das Notas Fiscais Eletrônicas que foram emitidas para o CNPJ do destinatário e que tiveram o evento de **"Ciência da Operação"** registrado.

De modo geral, a Manifestação do Destinatário tem o objetivo de evitar a emissão de notas fiscais fraudulentas, para destinatários que não possuem ciência ou confirmação tal operação.

Uma vez que o destinatário efetuou o evento de Ciência de Operação, este possui 180 dias para que seja feita a manifestação final do documento que é caracterizada por qualquer outro evento que não seja a Ciência da Operação. Este prazo poderá sofrer modificações ao longo do tempo pela SEFAZ.

Para obtenção de maiores informações sobre o conceito da Manifestação do Destinatário, pode-se acessar o Portal da NF-e a NT 2012.002:

<http://www.nfe.fazenda.gov.br/portal/perguntasFrequentes.aspx?tipoConteudo=yjOJMwFOkA0=> 

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bUBJ/PmtKQo=> 

Para utilização do MD-e, deve-se atender à alguns requisitos; sendo eles:

- Possuir um certificado digital do tipo **A1** credenciado juntamente a SEFAZ;
- Possuir o produto **NOTA FISCAL ELETRÔNICA/W**para Sankhya Om e produto JIVA-MD-e/W para Jiva Evo;
- Versão do Sankhya Om a partir da **3.11**, Jiva Evo a partir da 3.13 e versão do SanNFe a partir da [em definição].

Abaixo, temos as configurações que deverão ser realizadas no sistema para utilização da MD-e:

#### Configurações

Nas [Preferências de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), tem-se a opção **"Utiliza distribuição de DF-e"** para que sejam determinadas quais empresas utilizarão os serviços de Manifestação do Destinatário.

Além disso, para determinar se os serviços da Manifestação do Destinatário serão utilizados em ambiente de homologação ou produção, deve-se configurar o campo **"Ambiente NF-e/NFC-e"** (também em destaque na imagem abaixo).

![Imagem 1: Além disso, para determinar se os serviços da Manifestação do Destinatário serão utilizados em ambiente de homologação…](https://ajuda.sankhya.com.br/hc/article_attachments/4942422534935)

Através da tela [Configuração MD-e/DF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234) configura-se algumas preferências para que o sistema execute os serviços da Manifestação do Destinatário de forma automática. Todas as alterações feitas na tela deverão ser gravadas por meio do botão **"Salvar"**.

![Imagem 2: Esta tela somente estará disponível, caso a empresa atenda aos requisitos mencionados na parte inicial desta…](https://ajuda.sankhya.com.br/hc/article_attachments/16646230794519) Esta tela somente estará disponível, caso a empresa atenda aos requisitos mencionados na parte inicial desta documentação, e possua também o produto **IMPORTAÇÃO DE DOCUMENTOS ELETRÔNICOS/W**e **JIVA-MD-e/W**.

![Imagem 3: Esta tela somente estará disponível, caso a empresa atenda aos requisitos mencionados na parte inicial desta…](https://ajuda.sankhya.com.br/hc/article_attachments/4942381316887)

A tela possui a opção **"Baixar o XML ao dar ciência da operação"** que é utilizada para efetuar o download do XML da NF-e quando realizar-se o evento de Ciência de Operação na tela do [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389613-Portal-de-importa%C3%A7%C3%A3o-de-XML).

Através da marcação **"Realizar ciência automatizada"**, sempre que for feita uma consulta de notas, automaticamente também será realizada a ciência do documento. Realizando-se esta marcação, a opção Baixar o XML ao dar ciência da operação será automaticamente assinalada.

No processo de consulta das notas fiscais emitidas para a empresa, as marcações Realizar ciência automatizada e Baixar o XML ao dar ciência da operação, caracterizam a automação existente no sistema que realiza a ciência da operação juntamente com o download do XML. Este procedimento, tem por objetivo agilizar o processo de conferência das notas de compra, sem a necessidade da empresa dar ciência e depois fazer o download do XML em momentos distintos; o download será realizado sempre ao final do processo de consulta da ciência automatizada.

Por meio do campo **"Versão de consulta do MD-e"**, define-se a versão de consulta do MD-e que deseja-se utilizar. Tem-se duas alternativas:

- Consulta de NF-e (NT 2012);
- Distribuição de DF-e (NT 2014).

**Atenção Implantadores:** optando-se pela opção Distribuição de DF-e (NT 2014), a Consulta é feita via webservice NFeDistribuicaoDFe, que visa disponibilizar os documentos para os autores interessados da NF-e, como emitentes, destinatários e transportadoras. Além da consulta dos documentos, a correspondente Baixa do XML da NF-e, será realizada por este webservice.

Informa-se no campo **"Qtd. dias para consulta de NSU faltantes"**, a quantidade de dias em que será possível proceder com a busca dos NSU's (Número Sequencial Único) faltantes, ou seja, números que não não foram retornados pela SEFAZ até o momento que foram realizadas as buscas de dados sobre notas fiscais emitidas para a empresa.

Na realização da consulta dos documentos, a SEFAZ retorna uma resposta que possui o campo maxNSU, que se refere ao último e maior NSU existente para o destinatário. Esta informação é gravada internamente pelo sistema, e será utilizada na próxima consulta de modo a evitar-se o consumo indevido do serviço de consulta de documentos.

Os campos **"Horário das consultas por novas notas"** e **"Intervalo consulta em horas"** são utilizados para que o sistema automaticamente busque as Notas Fiscais Eletrônicas emitidas para o destinatário em um intervalo de tempo determinado. Nele informa-se o horário do dia em que as notas deverão ser buscadas.

No campo **"Intervalo consulta em horas"**, determina-se o intervalo em horas para que o sistema busque as notas no dia. O valor do campo deverá ser entre 1 (um) e 23 (vinte e três), caso contrário será apresentada a seguinte mensagem:

**O intervalo do download deve ser maior ou igual a 1 e menor ou igual a 23.**

Os campos **"Horário de Download do XML"** e **"Intervalo de Download em horas"** possuem a mesma função dos campos Horário das consultas por novas notas e Intervalo consulta em horas mencionados acima, só que ao invés do serviço de consulta, fazem o serviço de download do XML automaticamente.

Vale ressaltar que, o download do XML somente ocorrerá caso a Nota Fiscal Eletrônica já possua o evento de Ciência de Operação registrado.

O campo **"Gravar log de consultas"** tem a finalidade que o sistema grave todos os serviços que você executar manualmente ou, serviços executados automaticamente que estão relacionados com a manifestação do destinatário.

Quando o campo está sinalizados, todos os serviços feitos relacionados a manifestação do destinatário serão gravadas; quando desmarcado, somente serviços que retornarem rejeição serão gravados.

O campo **"Modelo de relatório Danfe"** é utilizado para determinar-se qual modelo de impressão (relatório formatado) o sistema irá se basear para que o DANFE da Nota Fiscal importada seja visualizado.

O botão **"Consultar Notas"** quando acionado, realiza a consulta junto a SEFAZ das notas fiscais emitidas pela empresa.

**Observação:** no parâmetro **"Intervalo de consulta de notas MDe - INTCONSULTAMDE"** informa-se o tempo (em milisegundos)**\*** que o sistema irá aguardar para consultar as notas MD-e junto a SEFAZ; é o intervalo de tempo respeitado pelo sistema para uma nova tentativa de obtenção de resposta (retorno das notas emitidas) junto a SEFAZ a respeito das notas MD-e emitidas por um mesmo CNPJ.

**\*** 1000 (mil) milissegundos é equivalente a 1 (um) segundo.

Na parte inferior da tela, tem-se a sessão **"Mensagens MD-e"** que tem a finalidade de visualização de todos os serviços realizados relacionados à manifestação do destinatário (pode-se visualizar a sessão em modo grade ou modo formulário), conforme marcação do campo **"Gravar log de consultas"** citado anteriormente.

Para que o sistema possa consultar as notas e/ou baixar o XML das notas, é necessário configurar o parâmetro **"Servidor para executar schedule - SERVERHOSTSCHED"** com o IP do servidor da base (por exemplo, 192.168.1.1), seguido de dois pontos (:) e da lista dos jobs específicos que deseja executar. Apenas os jobs informados nesse parâmetro serão executados. Exemplo de configuração:

192.168.1.1:ColetorDadosJob,ConstrutorMsgJob,EnviadorMsgJob,GerenciadorFilaJob,VerificaRupturaEstoqueJob

Se o parâmetro não for preenchido, todos os jobs serão executados automaticamente.

#### SanNFe

Para que o sistema execute os serviços relacionados à Manifestação do Destinatário, o SanNFe deverá estar devidamente configurado com o certificado digital do destinatário do tipo A1 credenciado juntamente a SEFAZ.

O sistema poderá validar a confirmação da Nota Fiscal de compra no sistema, exigindo que o evento de confirmação da operação seja registrado, para que se consiga confirmar a nota.

Para isso, na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde), deve-se marcar o campo **"Exigir confirmação do MD-e antes da confirmação"**. Este campo, estará habilitado apenas para o Tipo de Movimento igual a **"Compra"**. Além disso, o campo **"NF-e"** localizado na aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), deverá estar definido com a opção **"Terceiros"**.

[GIF animado: Imagem 4: Para isso, na tela Tipos de Operação - TOP , aba CT-e/MD-e , deve-se marcar o campo "Exigir confirmação do MD-e antes…](https://ajuda.sankhya.com.br/hc/article_attachments/4942537077655)

#### Utilização da MD-e

Na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), no alto da tela, tem-se o botão **"MD-e"**, que tem a finalidade de possibilitar a realização dos devidos serviços relacionados à Manifestação do Destinatário.

![Imagem 5: Na Central de Compras , no alto da tela, tem-se o botão "MD-e" , que tem a finalidade de possibilitar a realização dos…](https://ajuda.sankhya.com.br/hc/article_attachments/4942788318359)

O botão MD-e possui as seguintes opções:

- **Ciência da operação:** Registra-se o evento de ciência de operação para a nota fiscal lançada na Central;
- **Confirmo a operação:** Fixa-se o evento de Confirmação de Operação para a nota fiscal lançada na Central;
- **Desconheço a operação:** Registra-se o evento de Desconhecimento de Operação para a Nota Fiscal lançada na Central;
- **Operação não realizada:** Determina-se o evento de Operação não Realizada para a nota fiscal lançada na Central;
- **Visualizar manifestos:** Através desta opção, abre-se uma pequena janela, para que se possa consultar os eventos relacionados à Manifestação do Destinatário.

![Imagem 6: Visualizar manifestos: Através desta opção, abre-se uma pequena janela, para que se possa consultar os eventos…](https://ajuda.sankhya.com.br/hc/article_attachments/4942747046295)

Pode-se observar nesta pequena janela, os seguintes campos:

- **Chave Acesso:** Exibe a chave de acesso do documento que registrou o evento de manifestação;
- **Sequência:** Mostra em qual sequência o evento de manifestação foi registrado para determinada chave de acesso;
- **Situação MD-e:** Apresenta a situação do evento de manifestação que foi registrado;
- **Situação NF-e:** Exibe se a nota fiscal eletrônica filtrada está autorizada, cancelada ou denegada;
- **Status:** Mostra se o evento foi referente ao algum manifesto, ou se foi relacionado a um download do XML da nota;
- **Dh. Alteração:** Apresenta a data e hora em que o evento em questão foi registrado;
- **Usuário:** Exibe o código de usuário que efetuou o registro do evento em questão.

Para que o sistema seja capaz de realizar os eventos de Manifestação de Destinatário, deve-se lançar a Nota Fiscal Eletrônica na Central de Compras aberta a partir do Portal de Compras.

A empresa informada deverá estar devidamente configurada para utilizar os serviços de MD-e, assim como seu certificado digital configurado no SanNFe; além disso, a nota de compra lançada, deverá possuir o campo **"Chave de acesso"** preenchido para que os serviços possam ser enviados.

Pode-se também optar por realizar a importação do XML através da opção **"Importar XML de nota fiscal eletrônica"** presente no botão de **"Outras Opções..."** e posteriormente realizar os serviços de MD-e.

Feito o registro de qualquer evento através do botão **"MD-e"**, será apresentada a seguinte mensagem:

**"Ação registrada".**

Além disso, será feito o registro do evento no histórico de movimentações do MD-e que pode ser acessado através da opção **"Visualizar manifestos"**.

Caso no momento de registrar algum manifesto, a SEFAZ rejeite o evento por algum motivo, o erro de rejeição será apresentado na tela, para que sejam tomadas as devidas providências.

Na tela [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), somente para empresas que possuem o produto **"IMPORTAÇÃO DE DOCUMENTOS ELETRÔNICOS/W"**e **JIVA-MD-e/W**, tem-se alguns campos referentes a MD-e, que podem ser visualizados quando a tela se encontra em modo grade; são eles:

**Importado pelo MD-e:** Este campo será igual a **"S"** (Sim), quando o sistema automaticamente consultar as Notas Fiscais Eletrônicas para o destinatário e inserir automaticamente no Portal de Importação de XML;

**Possui XML:** Este campo será preenchido com **"Sim"** quando o documento do Portal de Importação possuir XML, e será igual a **"Não"** quando o documento não possui o XML. O campo será igual a "Não", somente quando o documento for inserido pelo serviço de consultas de notas do MD-e;

**Situação MD-e:** Este campo possui várias opções, que caracterizam qual a situação de manifestação do documento. São elas:

- **Sem manifestação do destinatário:** O documento possui esse status, quando ainda não houve manifestação de forma alguma em relação ao documento;
- **Ciência:** O documento assume este status, quando registrou-se o evento de ciência de operação;
- **Operação confirmada:** Este status é apresentado, quando registrou-se o evento de confirmação da operação;
- **Desconhecida:** O documento possui este status, quando ocorreu o registro do evento de desconhecimento da operação;
- **Operação não realizada:** O documento irá assumir este status, quando o registrar-se o evento de que a operação não foi realizada.

**Situação NF-e:** Este campo possui algumas opções que caracterizam qual a situação da NF-e. São elas:

- **Uso autorizado:** Tem-se esta informação, quando a NF-e inserida no Portal de Importação estiver autorizada;
- **Uso denegado:** Será apresentado, quando a NF-e inserida no Portal de Importação estiver denegada;
- **NF-e cancelada:** Tem-se este preenchimento, quando a NF-e inserida no Portal de Importação estiver cancelada.

As situações da NF-e são obtidas através do serviço de consulta do MD-e, portanto poderão ser atualizadas automaticamente na tela do Portal de Importação de XML.

Pode-se notar no lado esquerdo da tela, nos filtros que podem ser utilizados, o campo **"Apresentar importações"** (em destaque na imagem abaixo) conta com as seguintes opções:

- **Todas:** Serão apresentadas todas as importações, independente do modo que elas foram realizadas;
- **Manuais:** Serão exibidas na tela, apenas as importações realizadas manualmente;
- **Baixados pelo MD-e:** Tem-se somente os documentos que foram importados no Portal de Importação através do serviço de consulta/download do MD-e.

![Imagem 7: Baixados pelo MD-e: Tem-se somente os documentos que foram importados no Portal de Importação através do serviço de…](https://ajuda.sankhya.com.br/hc/article_attachments/4942922249623)

No alto da tela, tem-se o botão **"MD-e"** (em destaque na imagem acima) que possui as seguintes funcionalidades:

- **Ciência da operação:** Registra-se o evento de ciência de operação para a nota fiscal lançada na Central;
- **Confirmo a operação:** Fixa-se o evento de Confirmação de Operação para a nota fiscal lançada na Central;
- **Desconheço a operação:** Registra-se o evento de Desconhecimento de Operação para a Nota Fiscal lançada na Central;
- **Operação não realizada:** Determina-se o evento de Operação não Realizada para a nota fiscal lançada na Central;
- **Visualizar manifestos:** Através desta opção, abre-se uma pequena janela, para que se possa consultar os eventos relacionados à Manifestação do Destinatário.
- **Visualizar NF-e:** Acionando-se esta opção, pode-se visualizar o Danfe impresso em formato PDF, de acordo com o modelo de impressão (relatório formatado) mencionado nas instruções sobre a tela **"Configuração MD-e"**.

Essa opção de Visualizar NF-e somente irá funcionar, caso o documento a ser visualizado possua o XML, ou seja, o campo **"Possui XML"** deverá estar igual a **"Sim"**; caso contrário ao clicar na opção, a seguinte mensagem será exibida:

**"Esta importação não possui o XML da nota."**

O processamento dos documentos poderá acontecer normalmente no Portal de Importação, desde que o mesmo possua XML para que o sistema seja capaz de processar as informações.

O processo de importação não foi afetado pelos procedimentos ligados ao MD-e; ocorrendo divergências, deve-se resolvê-las para conclusão da importação da nota.

- **Download NF-e:** Por meio deste campo, tem-se a funcionalidade de transferência da nota selecionada. Para realizar este procedimento serão necessárias algumas premissas conforme imagem abaixo:

**"Para que seja possível realizar download da NF-e e os seguintes critérios devem ser atendidos:**

**Ser NF-e**

**Possuir empresa**

**Não possuir XML**

**Possuir chave de acesso**

**Situação NF-e = 'uso autorizado'**

**Situação MD-e = 'Ciência' ou 'Operação confirmada'."**

#### Validação na confirmação da Nota de Compra

Como já mencionado no decorrer desta documentação, pode-se optar em não permitir a confirmação da nota de compra, caso o evento de confirmação da operação não tenha sido registrado na nota.

Caso seja feita a tentativa de confirmação de uma nota de compra que não possua esse evento, a seguinte mensagem será exibida:

**"Não foi localizado registro da confirmação da operação no MD-e para esta chave da NFe."**

Caso seja feita a escolha por não realizar esta validação, mesmo que a nota tenha sido confirmada, pode-se realizar os eventos de MD-e.

O processo de compra poderá ser concluído, quando a nota de compra for confirmada e o destinatário realizar a manifestação final do documento, que poderá ser a "confirmação da operação", "operação não realizada" ou "desconhecimento da operação".
