---
id: "360044612514"
titulo: "Viagens de Transportes (MDF-e)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > MDF-e"
atualizado_em: "2026-09-15T16:56:11Z"
rotulos: ["MDF-e", "manual", "Configuração", "Transporte", "Viagens de Transportes (MDF-e)", "br.com.sankhya.viagensdetransporte", "Viagens de Transportes (MDF-e) manual", "UFCOLCOMPMDFE", "Documento digital vincula documentos fiscais agiliza registro", "Certificado digital ordem de carga configurações de cadastro.", "Processo de entrega múltiplos destinos emissão de MDF-e.", "UFCOLDESCMANUAL", "Documentos Eletrônicos", "Viagens"]
---

# Viagens de Transportes (MDF-e)

```
 Módulo: Comercial > Rotinas
```

---

[Manifesto de Documentos Fiscais Eletrônicos - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673) é o documento emitido e armazenado eletronicamente, de existência apenas digital, para vincular os documentos fiscais utilizados na operação e/ou prestação, à unidade de carga utilizada no transporte, cuja validade jurídica é garantida pela assinatura digital do emitente e autorização de uso pela administração tributária da unidade federada do contribuinte.

O MDF-e deverá ser emitido por empresas prestadoras de serviço de transporte, para prestações com mais de um conhecimento de transporte ou pelas demais empresas nas operações, cujo transporte seja realizado em veículos próprios, arrendados, ou mediante contratação de transportador autônomo de cargas, com mais de uma nota fiscal.

A finalidade do MDF-e é agilizar o registro em lote de documentos fiscais em trânsito e identificar a unidade de carga utilizada e demais características do transporte. A autorização de uso do MDF-e implicará em registro posterior dos eventos, nos documentos fiscais eletrônicos nele relacionados. O MDF-e dever ser emitido em operações de transporte interestaduais.

#### Legislação:

<https://www.confaz.fazenda.gov.br/legislacao/ajustes/2013/AJ_010_13>

#### Os requisitos para a rotina de emissão do MDF-e são:

- Possuir certificado digital para a empresa que vai emitir o MDF-e;
- Trabalhar com o processo de Ordem de Carga;
- Possuir todas as configurações de cadastro definidas corretamente e de forma completa.

#### Conceito de viagem:

Uma viagem se trata de um processo em que a empresa fará várias entregas em vários destinos de uma determinada rota. Em uma única viagem é possível ter mais de um MDF-e, devido ao fato de que cada MDF-e possui somente uma UF de carregamento e uma UF de descarregamento. Portanto, em uma viagem que a empresa deverá entregar de MG para GO, DF e BA, deverão ser emitidos três MDF-e's. Sendo que estes três MDF-e's estarão em uma mesma viagem. Considere o exemplo abaixo:

A empresa realiza a negociação de uma compra com seu fornecedor, localizado em outro estado, e a mesma combina de buscar as mercadorias, a emissão da nota fiscal de compra será executada pelo fornecedor, e em seguida, registrada pela empresa sem a sua devida confirmação; com o intuito de que posteriormente seja efetuado o lançamento de uma MDF-e para a coleta das mercadorias.

Com a chegada do veículo no fornecedor, deve-se proceder com o carregamento das mercadorias compradas e na sequência emitir o MDF-e; diante disto, será possível transitar do fornecedor até a empresa. Se tudo estiver em conformidade, a confirmação da nota de compra se dará após o retorno do veículo para a empresa com as mercadorias e as respectivas notas fiscais.

**Importante:** Ao vincular uma nota de compra em um MDF-e, é necessário atentar para os seguintes requisitos:

1. Não realizar a confirmação da nota;
2. Marcar a opção **"Contém documentos de terceiros?"** localizada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abageral).

**Observação:** É possível selecionar o município de carregamento do MDF-e pelo parceiro remetente da NF-e de compra presente na viagem de transporte. Deste modo, se o parceiro remetente for informado, o mesmo será utilizado no lugar do município da empresa. No entanto, quando o campo **"Parceiro Remetente"** não for informado e o parâmetro **"Considerar UF Coleta XML MDF-e Envolve Mov Compra? - UFCOLCOMPMDFE"** estiver ligado, o sistema considerará como UF inicial no XML a UF de Coleta da [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514#abageral) do MDF-e.

Considere ainda que, ao habilitar o parâmetro **"UF Coleta e UF Descarregamento manualmente - UFCOLDESCMANUAL"** será possível indicar manualmente a UF e o município de coleta, bem como, a UF e o município de descarregamento na sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral), da aba [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) dessa tela.

Este parâmetro será priorizado sempre que no MDF-e houver apenas documentos de emissão própria, ou seja, se a marcação Contém documentos de terceiros? estiver desativada. Do contrário, a funcionalidade do parâmetro UFCOLCOMPMDFE será executada prioritariamente. 

Trataremos neste artigo, sobre o comportamento da tela Viagens de Transportes (MDF-e):

| [Filtros iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#filtrosiniciais) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abageral) |
| --- | --- |
| [Aba MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) | [Aba Motorista](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamotorista) |
| [Aba Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abaordemdecarga) | [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#bot%C3%A3ooutrasop%C3%A7%C3%B5es) |
| [Demais botões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#demaisbot%C3%B5es) | [Inclusão do CT-e globalizados e não...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#Inclus%C3%A3odocteglobalizadosen%C3%A3oglobalizadosnomesmomdfe) |
| [Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Rodoviário CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/33529957876375-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-CT-e) | [Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Aquaviário NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530697647767-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Aquavi%C3%A1rio-NF-e) |
| [Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Rodoviário NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e) |  |

### Filtros iniciais

Você pode filtrar as viagens de acordo com a **"Empresa"**, o **"Número da Viagem"**, a **"Data de Emissão"** do MDF-e ou mesmo, pelo **"Status do Documento"**, este pode ser:

- Não transmitido;
- Enviado;
- Aguardando autorização;
- Autorizado;
- Aguardando correção;
- Cancelado;
- Encerrado;
- Denegado.

Logo abaixo dos filtros fixos da tela, temos o **"Nro. Viagem"**, que corresponde ao Número único gerado para cada viagem criada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Aba Geral

![Imagem 1: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/4406663639191)

**Empresa:** Empresa que vai emitir o(s) manifesto(s) da viagem em questão.

**Série:** Série do(s) manifesto(s) que será(ão) emitido(s) na viagem.

**Nota:** Quando no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#bot%C3%A3ooutrasop%C3%A7%C3%B5es), opção **"Controle de Numeração"**, houver somente uma empresa configurada, a série da mesma será inserida automaticamente pelo sistema no(s) manifesto(s) que será(ão) emitido(s) na viagem.

**Status Doc.:** Status da viagem, poderá ser **"Em edição"** quando a viagem ainda apresenta manifestos não transmitidos, e **"Confirmado"** quando os manifestos já foram transmitidos de alguma forma.

**Veículo de tração:** Veículo de tração do(s) manifesto(s) da viagem em questão.

**Reboque 1:** Em uma viagem poderão existir até três reboques no transporte, você poderá informar um reboque neste campo.

**Reboque 2:** Em uma viagem poderão existir até três reboques no transporte, você poderá informar um reboque neste campo.

**Reboque 3:** Em uma viagem poderão existir até três reboques no transporte, você poderá informar um reboque neste campo.

**Tip. Amb. MDF-e:** Ambiente de emissão do(s) manifesto(s) que a empresa está configurada.

Caso a marcação **"Usar CIOTs dos CT-e vinculados ao MDF-e?"** esteja realizada, ao incluir um CT-e no MDF-e, o CIOT correspondente ao CT-e será utilizado para o MDF-e.

Se a marcação **"Usar tomadores de serv. como contratantes?"** estiver realizada, ao incluir um CT-e no MDF-e, o parceiro correspondente ao CT-e será inserido como contratante no MDF-e.

A marcação **"Contém documentos de terceiros?"** quando realizada, indica que a viagem de transporte possuirá documentos de terceiros a ela vinculados. Esta marcação poderá ser realizada, caso a viagem não possua Ordens de Carga e/ou MDF-e's a ela vinculados; além disso, ao assinalar esta marcação, a aba [Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abaordemdecarga) será desabilitada para uso.

**Importante:** Para realizar a inserção de notas, quando a marcação Contém documentos de terceiros? estiver realizada, os  campos **"UF de Coleta"**, **"UF de Descarregamento"** e **"Unidade de Medida"**, todos presentes na sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral) deverão estar devidamente preenchidos, sendo que este último deve ser definido com a unidade KG (quilo).

**Tipo Modal MDF-e:** Este campo pode ser definido como **"Rodoviário"** ou **"Aquaviário"**; esta definição irá determinar o tipo de documento de CT-e aceito na viagem de transporte, ou seja Rodoviário ou Aquaviário, respectivamente; além disso, cada uma dessas opções, habilitará na aba [MFD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e), sub-abas distintas, as quais podem ser verificadas abaixo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Aba MDF-e

![Imagem 2: Aba MDF-e](https://ajuda.sankhya.com.br/hc/article_attachments/4406663641495)

Esta aba é dividida em outras sub-abas que aglomeram os dados correspondentes ao MDF-e. Primeiramente trataremos as abas apresentadas, ao definir o campo Tipo Modal MDF-e (aba Geral) como Rodoviário: 

| [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral) | [Produto Predominante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaprodutopredominante) |
| --- | --- |
| [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaeventos) - [Eventos do MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#eventosdomdf-e) | [Documentos MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abadocumentosmdf-e) |
| [UFs do percurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaufsdopercurso) | [Contratantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abacontratantes) |
| [Seguro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaseguro) | [Pagamento de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abapagamentodefrete) |
| [CIOT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaciot) | [Vale Pedágio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abavaleped%C3%A1gio) |
| [Lacres](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abalacres) |  |

Ao trabalhar com o campo **"Tipo Modal MDF-e"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#h_628cac3b-7676-41bd-8860-74913d31af68)) definido como **"Aquaviário"**, serão habilitadas as seguintes sub-abas:

| [Terminais Carregamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaterminaiscarregamento) | [Terminais Descarregamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaterminaisdescarregamento) |
| --- | --- |
| [Embarcações Comboio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaembarca%C3%A7%C3%B5escomboio) | [Unidades Carga Vazia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaunidadescargavazia) |
| [Unidades Transporte Vazia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abaunidadestransportevazia) |  |

 **Sub-aba Geral**

**Status MDF-e:** Este campo será gerado automaticamente de acordo com a confirmação do MDF-e, cancelamento ou encerramento. Os status serão: Enviado, Aguardando Autorização e Autorizado, Encerrado e Cancelado; estes serão gerados de acordo com as seguintes regras:

- **Enviado:** Será definido este status quando o sistema gerar somente a chave de acesso e o número aleatório do MDF-e, sem gerar o XML assinado;
- **Aguardando Autorização:** Este status será definido quando o sistema gerar somente a chave de acesso, o número aleatório do MDF-e, e o XML, contudo sem assinar;
- **Autorizado:** Será definido este status quando o sistema gerar a chave de acesso, o número aleatório do MDF-e, e o XML assinado.

**Observação:** O MDF-e que estiver com o status **"Encerrado"** poderá ser impresso da mesma maneira como o MDF-e com status **"Autorizado"** ou **"Enviado em contingência"** são impressos atualmente, seguindo portanto, as mesmas regras e validações.

**Nota:** A impressão deste MDF-e irá conter a frase **"MDF-e encerrado na data [data e hora do encerramento]"** como observação no rodapé do documento.

**Nro. Aleatório:** Número aleatório gerado pelo sistema para compor a chave de acesso e enviar a informação no MDF-e.

**Chave MDF-e:** Chave de acesso do MDF-e gerado pelo sistema.

**Nro. Recibo:** Número do recibo gerado pela receita quando a mesma responde a uma solicitação de serviço.

**Dt. e Hora do Recbto.:** Data e hora que o sistema recebe a resposta da receita a uma solicitação de serviço.

**Dt. e Hora da emissão:** Data e hora em que o MDF-e é confirmado.

**Tipo de emissão:** Tipo de emissão do MDF-e, pode ser Normal quando a aprovação do MDF-e ocorre de forma eficiente com comunicação plena com a receita, e Contingência quando a comunicação com a receita não existe a aprovação do MDF-e não ocorre de forma eficiente. Quando existir essa situação, o usuário poderá apenas imprimir o DAMDFE (com o destaque de um texto demonstrando a contingência) e assim que possível autorizar o MDF-e, quando o serviço voltar ao normal. Temos o prazo de no máximo 168 horas (7 dias) para a aprovação do MDF-e emitido em contingência.

**UF de Coleta:** este campo é automaticamente calculado como sugestão na criação da Viagem de Transporte, ou na inserção de uma Ordem de Carga em uma Viagem já existente. É um campo calculado conforme a UF da origem dos documentos do MDF-e criado. Nessas ocasiões, são verificados os documentos da Ordem de Carga, suas UF's de origem e UF's de destino; para cada UF de destino será criado um MDF-e. Se para a mesma UF de destino houver UF's de origens diferentes, então você será questionado sobre qual UF de coleta utilizar no MDF-e a ser criado.

Assim que for feita a escolha de qual será a UF de coleta para o MDF-e a ser criado, o campo UF de coleta é gerado conforme a escolha feita. Caso você modifique o campo UF de coleta manualmente, a UF alterada será gerada como UF de carregamento do MDF-e.

Caso você altere a UF de coleta para uma UF que não possui qualquer cidade de origem de algum documento vinculado ao MDF-e, ao gerar seu lote será apresentada a seguinte rejeição da SEFAZ:

**"Rejeição: Código de Município diverge da UF de carregamento do MDF-e"**

Ou seja, para que o MDF-e possa ser aprovado, é preciso informar o campo UF de coleta com uma UF que possua alguma cidade de origem de algum documento vinculado ao MDF-e. Caso o campo UF de coleta seja informado com uma UF que possua mais de uma cidade de origem dos documentos vinculados ao MDF-e, a primeira cidade encontrada será utilizada para gerar o campo de município de carregamento.

**Município de Coleta:** este campo será apresentado quando o parâmetro UFCOLDESCMANUAL estiver ligado e, será preenchido automaticamente com o município da empresa de coleta dos itens da nota vinculada à viagem. Porém, caso seja necessário, pode-se alterar esse município manualmente. 

**UF de Descarregamento:** este campo poderá ser preenchido manual ou automaticamente. Ele será carregado automaticamente quando forem informadas as ordens de carga na viagem; o sistema irá buscar a UF de descarregamento de acordo com os parceiros destinatários das notas das ordens de carga, se existirem; se não houver parceiros destinatários nas notas, o sistema buscará pelos parceiros da própria nota, sempre priorizando o endereço de entrega do cadastro de parceiro, se existir; caso não exista, buscará o endereço principal.

Este campo poderá ser informado manualmente, quando precisar lançar uma manifesto manualmente, mesmo que a ordem de carga já esteja informada na viagem. Essa situação poderá ocorrer em função de um encerramento do MDF-e que não deu certo, possuindo a necessidade de lançar outro na mesma viagem (inclusão de um novo motorista, por exemplo). Você pode lançar somente a UF que esteja disponível de acordo com as notas das ordens de carga vinculadas na viagem.

O único campo que poderá ser editado nessa aba, será o campo UF de Descarregamento.

**Município de Descarregamento:** este campo será exibido após a ativação do parâmetro UFCOLDESCMANUAL e será preenchido automaticamente com o município do parceiro para descarregamento dos itens da nota vinculada à viagem. Porém, caso seja necessário, pode-se alterar esse município manualmente. 

**Nota:** os campos Município de Coleta e Município de Descarregamento são de preechimento obrigatório, caso tente salvar o cadastro vinculado ao MDF-e sem informar esses municípios, a seguinte mensagem será exibida:

**"Para lançamento manual do MDF-e, é obrigatório informar a 'Município de Coleta' e a 'Município de Descarregamento'."**

**Considerar Peso Bruto Total para NF-e:** Quando esta marcação estiver acionada, a tag <**qCarga**> será gerada com o valor informado no campo **"Peso Bruto Total"**, dispensando assim a soma do Peso Bruto armazenado no lançamento das NF-e's relacionadas no MDF-e. Além disso, a unidade de medida irá gerar a tag <**cUnid**> com o valor informado no campo **"Unidade de Medida"**.

A seguir trataremos da rotina de inclusão de documentos fiscais no MDF-e com indicação de carregamento posterior:

Primeiramente, habilite a marcação **"Indicativo de Carregamento Posterior"**, para indicar que poderão ser incluídos novos documentos fiscais eletrônicos ao MDF-e com data posterior ao início da viagem, caracterizando assim, o evento Inclusão DF-e. Ressaltamos que, só poderão ser incluídos novos documentos ao MDF-e se o transporte for intermunicipal, ou seja, dentro do mesmo estado (UF origem = UF destino) e se os documentos fiscais estiverem aprovados e não tiverem participado de outro MDF-e.

Feito isso, quando você incluir novos DF-e, estes alimentarão a sub-aba [Documentos MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514#sub-abadocumentosmdf-e) com o campo **"Status de Envio"** igual a **"Não enviado"**, sendo que estes registros poderão ser enviados por meio do botão **"Enviar Evento"** localizado na parte superior desta aba. Este botão, enviará todos os documentos que estiverem com o campo Status de Envio igual a Não enviado de uma única vez alterando-o automaticamente para **"Por evento"**.

Por fim, você poderá acompanhar o evento Inclusão DF-e por meio da sub-aba [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514#sub-abaeventos).

**Importante:** A exclusão do documento incluído posteriormente na situação de carregamento posterior só será permitida se o campo Status de Envio for igual a Não enviado.

#### Seção MDF-e Aquaviário

**Cód. Porto Embarque:** Informe o código do porto de embarque da carga a ser transportada.

**Cód. Porto Destino:** Semelhante ao campo anterior, preencha o código do porto de destino da carga.

**Cód. Porto Transbordo:** Preencha aqui o porto de transbordo da carga, ou seja, o porto onde ocorreu a passagem de carga de um meio de transporte para outro.

**Tipo Navegação:** Defina aqui o tipo de navegação em questão. Podendo ser:

- **Interior:** Corresponde ao espaço compreendido entre os limites de um país;
- **Cabotagem:** Navegação mercante ao longo da costa e, especialmente, entre portos do mesmo país, por oposição a navegação de longo curso.

**Nº IRIN:** Temos neste campo uma identificação relativa ao registro do navio, por isso um mesmo MDF-e aquaviário que contenha mais de um CT-e aquaviário, estes vinculados ao MDF-e, terão o mesmo IRIN do navio, pois, não é correto documentos de CT-e aquaviário diferentes com o IRIN do navio diferentes entre si, vinculados ao mesmo MDF-e.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Produto Predominante**

Complete nesta aba as seções correspondentes com as informações do produto transportado, seu local de carregamento e o de descarregamento.

[A partir da NT 2025.001 v1.02](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503) as informações do campo "**Tipo de Carga**" incluem a nova opção de carga **Granel Pressurizada**.

![Imagem 3: O campo EAN é de preenchimento opcional.](https://ajuda.sankhya.com.br/hc/article_attachments/35474818881303)O campo EAN é de preenchimento opcional.

![Imagem 4: O campo EAN é de preenchimento opcional.](https://ajuda.sankhya.com.br/hc/article_attachments/35474863183895)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Eventos**

![Imagem 5: Sub-aba Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/4406648429463)

**Cód. Evento:** Este campo será gerado automaticamente quando o usuário executar determinadas ações. Ao cancelar um manifesto, o sistema irá gerar o evento de código 110111 - cancelamento. No encerramento de um manifesto, será gerado o evento de código 110112 - encerramento.

**Descrição do Evento:** Este campo será gerado de acordo com o código do evento, sendo 110111 - Cancelamento e 110112 - Encerramento.

**Dt. e Hora do Evento:** Data e hora que o usuário executou a ação de cancelar ou encerrar o manifesto.

**Nro. Recibo:** Número do recibo que receita gera, quando responde a solicitação do serviço de algum evento.

**Justificativa do Evento:** Quando você efetuar o evento de cancelamento do MDF-e, deverá ser informado uma justificativa pela empresa do porque está cancelando, essa justificativa será grava neste campo.

**UF de encerramento:** Quando houver o evento de encerramento do MDF-e, você deverá informar qual a UF que o mesmo foi encerrado, e essa informação será grava neste campo.

**Cidade de encerramento:** Quando houver o evento de encerramento do MDF-e, você deverá informar qual a cidade que o mesmo foi encerrado, e essa informação será gravada neste campo.

**Observação:** Nenhum campo na sub-aba Eventos poderá ser editado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Eventos do MDF-e**

**Cancelamento:** Este evento é realizado quando houver qualquer erro de emissão do manifesto; efetue seu cancelamento, e emita outro, se for o caso. O prazo para que um manifesto seja cancelado é de 24 horas.

**Encerramento:** Este evento possui duas situações em que deve ser executado:

- A empresa emitente deverá encerrar o MDF-e no final do percurso. Enquanto houver MDF-e pendente de encerramento não será possível autorizar novo MDF-e, para o mesmo par UF de carregamento e UF de descarregamento, ou para o mesmo veículo.
- Se no decorrer do transporte, for feita qualquer alteração nas informações do MDF-e (veículos, carga, documentação, motorista etc.), este deverá ser encerrado, tendo-se a emissão de um novo MDF-e com a nova configuração.

Entende-se como encerramento do MDF-e, o ato de informar ao fisco o fim da vigência do documento, que poderá ocorrer pelo término do trajeto acobertado ou pela alteração das informações do MDF-e através da emissão de um novo.

**Entrega da mercadoria:** Quando a mercadoria é entregue com sucesso para o destinatário, a empresa emitente do MDF-e deve encerrá-lo, informando à receita que o transporte em questão foi finalizado, assim será possível emitir outros manifestos para o veículo que transportou a mercadoria. É importante lembrar que, quando se emite um MDF-e contendo determinado veículo, não será possível emitir outro MDF-e para o mesmo veículo com a mesma UF de carregamento e descarregamento. Para que isso seja possível, é necessário encerrar o MDF-e que foi emitido anteriormente.

**Alteração do MDF-e durante o percurso:** Se no decorrer do transporte houver qualquer alteração nas informações do MDF-e (veículos, carga, documentação, motorista, etc.) este deverá ser encerrado e ser emitido um novo MDF-e contendo as novas informações.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Documentos MDF-e**

Inicialmente nesta sub-aba, temos o Nro. Único da Nota, que corresponde ao Número único dos documentos que estão disponíveis na viagem de acordo com ordem de carga utilizada e a UF de descarregamento. Esse campo poderá ser carregado automaticamente ou ser editado manualmente:

- Será carregado automaticamente quando forem lançadas as ordens de carga na viagem, onde o sistema irá inserir as notas que possuem o parceiro destinatário, ou parceiro da nota com o endereço igual a UF de descarregamento do manifesto; nessa aba irão conter as notas do manifesto.
- Será manualmente informado, caso seja excluída alguma nota manualmente do manifesto e seja necessário incluí-la novamente; ao incluir, você pode pesquisar as notas de acordo com as ordens de carga da viagem e a UF de descarregamento do manifesto. Ou seja, só estarão disponíveis para incluir, as notas que participem das ordens de carga da viagem e que possuam o destino de acordo com a UF de descarregamento do manifesto. Caso queira incluir uma nota que não satisfaça essas condições, será necessário incluir primeiramente a nota na tela de [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274) e depois atualizar a viagem para que a nota fique disponível.

Esta sub-aba é dividida em outras duas abas, **"Geral"** e **"Produtos Perigosos"**.

A aba Geral, terá seus dados carregados de acordo com o Número único anteriormente informado.

Também temos nesta aba, a marcação **"Id. Reentrega"** que se realizada, indica que o documento em questão corresponde a uma reentrega de notas fiscais que retornaram à empresa e foram vinculadas no novo MDF-e emitido. Essa situação é comum, por exemplo, quando clientes encerram suas atividades às 18:00hs e após esse horário não recebem a mercadoria; com isso, o caminhão retorna para a empresa emitente do MDF-e, que por sua vez encerra esse MDF-e e emite outro no dia seguinte contendo as notas a serem entregues juntamente com as notas que não foram entregues no dia anterior.

**Observação:** Caso o documento MDF-e tenha a marcação Id. Reentrega realizada, a tag <**indReentrega**> será gerada em seu XML.

Já a aba Produtos Perigosos, para cada documento transportado no MDF-e, seja NF-e ou CT-e, é preciso informar o **"Número ONU"** do produto transportado e a **"Quantidade total do produto"**. Cada documento pode ter vários produtos classificados pela ONU como perigosos, por isso, ambas as informações precisam ser preenchidas conforme a legislação de transporte de produtos perigosos aplicada ao modal.

Entende-se por CT-e globalizado o lançamento cuja marcação **"CT-e globalizado"** localizada no [Cabeçalho da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) se encontre acionada. Ao realizar a inserção de um CT-e globalizado diretamente por esta aba, caso haja algum documento para o MDF-e em questão que não seja um CT-e globalizado a seguinte mensagem será exibida:

**"Não é possível vincular conhecimentos de transporte globalizados com conhecimentos de transporte não globalizados para o mesmo MDF-e. Verifique!"**

Além disso, se o MDF-e for composto por CT-e globalizado, ao invés de enviar as chaves do CT-e o sistema irá enviar as chaves da NF-e que compõem o CT-e. Neste caso, se alguma das notas tiver sido enviada em contingência (Danfe Segurança), temos o seguinte procedimento:

- Se a nota existir no sistema, o cálculo do segundo código de barras será efetuado;
- Caso contrário, se faz necessário o preenchimento do campo **"Segundo Código de Barras"** contido no [Rodapé da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba UFs do Percurso**

Nesta aba, informe quais estados o veículo irá percorrer desde seu ponto de origem até seu destino. Por exemplo, se a origem do trajeto for MG - Minas Gerais e o destino do manifesto for MT - Mato Grosso, o veículo deverá passar pelo estado de GO - Goiás, portanto, neste caso, a UF Goiás deverá ser informada nessa aba.

![Imagem 6: Nesta aba, informe quais estados o veículo irá percorrer desde seu ponto de origem até seu destino. Por exemplo, se a…](https://ajuda.sankhya.com.br/hc/article_attachments/4406663702807)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Contratantes**

Nesta sub-aba, determine os Parceiros tomadores do serviço de transporte feito no MDF-e. Para tal, preencha o campo Cód. Parceiro Contratante. Os dados aqui inseridos, irão preencher a tag <infContratante> do XML do MDF-e.

![Imagem 7: Nesta sub-aba, determine os Parceiros tomadores do serviço de transporte feito no MDF-e . Para tal, preencha o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/4406648478743)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Seguro**

![Imagem 8: Sub-aba Seguro](https://ajuda.sankhya.com.br/hc/article_attachments/4406648499607)

Nesta sub-aba, defina os dados pertinentes ao seguro da carga transportada na emissão do MDF-e. O emitente precisará informar:

- Número da apólice;
- Seguradora;
- Responsável do seguro - Caso este campo não seja preenchido, indica-se que o responsável pelo seguro é o emitente do MDF-e; ao ser informado, tem-se que o responsável pelo seguro será o contratante;

**Observação:** Somente parceiros que forem definidos como Contratantes podem ser informados neste campo (aba Contratantes).

Na sub-aba Averbações, informe o Número da Averbação correspondente ao seguro/apólice; este pode conter várias averbações.

As informações referentes ao seguro, irão preencher a tag <**seg**> do XML do MDF-e.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Pagamento de Frete**

![Imagem 9: Sub-aba Pagamento de Frete](https://ajuda.sankhya.com.br/hc/article_attachments/4406648510103)

Temos aqui as informações referentes aos dados bancários e a forma de pagamento do frete.

A aba **"Componentes do Pagamento do Frete"**, está relacionada as informações de pagamento do frete como Vale Pedágio, Impostos, Taxas e Contribuições, Despesas (bancárias, meios de pagamento, etc), Frete (adequações à NT 2025.001 v1.02) e Outros.

A aba **"Informações do pagamento a prazo"** esta vinculada ao detalhamento do pagamento à prazo como Número de parcelas, Data de vencimento e Valor da parcela.

A tag `<CNPJIPEF>` no XML do Manifesto Eletrônico de Documentos Fiscais (MDF-e), que representa o CNPJ da Instituição de Pagamento Eletrônico de Frete (IPEF) garante a conformidade fiscal.

O sistema preenche a tag `<CNPJIPEF>` exclusivamente com o CPF/CNPJ do parceiro informado no campo **"Parceiro de Pag. do Frete" nesta aba, na sub aba Geral > Informações bancárias.**

**Observação:** para que o MDF-e seja emitido corretamente, é essencial que você verifique e confirme se o campo **"Parceiro de Pag. do Frete"** está populado com o cadastro da **Instituição Financeira (ou IPEF)** responsável pela operação de pagamento do frete.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba CIOT**

![Imagem 10: Sub-aba CIOT](https://ajuda.sankhya.com.br/hc/article_attachments/4406663746711)

Preencha os campos **CIOT** e **Emitente do CIOT** para definir o uso do CIOT (Código Identificador da Operação de Transporte) referente aos documentos vinculados ao MDF-e em cada viagem. Estas informações vão compor a tag <**infCIOT**> do XML do MDF-e.

![Imagem 11: A partir das alterações trazidas pela NT 2025.001 v1.02 , o campo CIOT passou a ser opcional.](https://ajuda.sankhya.com.br/hc/article_attachments/35474818881303)[A partir das alterações trazidas pela NT 2025.001 v1.02](https://ajuda.sankhya.com.br/hc/pt-br/articles/35309948500503), o campo CIOT passou a ser opcional.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Vale Pedágio**

Através desta sub-aba, são definidas as informações correspondentes ao vale-pedágio no MDF-e, quando existir.
Informe o **"Nro. Compra"**, **"Cód. Parceiro Pagante"**, **"Tipo do vale pedágio"**, **"Cód. Parceiro Fornecedor"**, **"Categoria de combinação veicular"** e **"Vlr. do Pedágio"**.

![Imagem 12: Através desta sub-aba, são definidas as informações correspondentes ao vale-pedágio no MDF-e, quando existir. Informe o…](https://ajuda.sankhya.com.br/hc/article_attachments/4406663756183)

Os dados referentes a esta aba irão alimentar a tag <valePed> no XML do MDF-e.

- O campo **Nro. Compra** representa o Identificador do Vale-Pedágio Obrigatório.
- O campo **Tipo do vale pedágio** aceita as opções:
  - Não específico;
  - 01 - Tag;
  - 04 - Leitura de placa.

**Observações legais:**

- Quando a mercadoria e o veículo estiverem no mesmo **CNPJ da empresa emissora do MDF-e**, o tipo do emitente deve ser **Transportador de Carga Própria**.
- Nesta situação, se o transporte for realizado por colaborador registrado, **não será exigido o grupo de informações de pagamento**.
- Porém, se o tipo de transportador for informado e o MDF-e possuir apenas um documento fiscal, o grupo de pagamento passa a ser obrigatório.
- Quando o veículo pertencer a uma empresa com **CNPJ diferente da emissora**, ainda que do mesmo grupo econômico, será considerado como **veículo de terceiros**.
- As informações desta aba foram adequadas à **NT 2025.001 v1.02**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Lacres**

Informe nesta sub-aba, por meio do campo **"Nro Lacre"** as informações pertinentes aos lacres no MDF-e, quando existirem.

![Imagem 13: Informe nesta sub-aba, por meio do campo " Nro Lacre" as informações pertinentes aos lacres no MDF-e , quando existirem.](https://ajuda.sankhya.com.br/hc/article_attachments/4406648550423)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

---

**Sub-aba Terminais Carregamento**

Informe nesta aba o **"Código"** e o **"Nome"** dos Terminais de Carregamento correspondentes à Viagem aquaviária.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) 

**Sub-aba Terminais Descarregamento**

Complementando a aba anterior, informe nesta aba o **"Código"** e o **"Nome"** dos Terminais de Descarregamento correspondentes à Viagem aquaviária.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#aotrabalharcomocampo) 

**Sub-aba Embarcações Comboio**

Devem ser inseridas nesta aba as embarcações correspondentes ao transporte aquaviário. Serão apresentados para escolha aqui, as embarcações previamente incluídas no [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-), cujo campo **"Tipo Veículo"** tenha sido definido como **"Aquaviário"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#aotrabalharcomocampo) 

**Sub-aba Unidades Carga Vazia**

Determine nesta aba a **"Identificação das Unidades"** utilizadas no transporte aquaviário em casos de Carga Vazia. Defina também o **"Tipo Unidade Carga Vazia"**, que pode ser:

- Pallet;
- ULD;
- Container;
- Outros.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#aotrabalharcomocampo) 

**Sub-aba Unidades Transporte Vazia**

Defina nesta aba a Identificação das Unidades utilizadas no transporte aquaviário em casos de Transporte Vazio. Determine também o **"Tipo Unidade Transporte Vazia"**, que pode ser:

- Rodoviário Reboque;
- Rodoviário Tração.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#aotrabalharcomocampo) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Aba Motorista

Nesta aba, você informe os parceiros cadastrados no sistema como motoristas e que estão ativos. Existe um limite de até dez motoristas por viagem. Estes motoristas serão informados no(s) manifesto(s) da viagem.

![Imagem 14: Nesta aba, você informe os parceiros cadastrados no sistema como motoristas e que estão ativos. Existe um limite de até…](https://ajuda.sankhya.com.br/hc/article_attachments/4406648569111)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Aba Ordem de Carga

Indique nesta aba, a empresa da ordem de carga e qual a ordem de carga que participará da viagem. Poderão ser informadas várias ordens de carga, mesmo que a empresa destas seja diferente da empresa da viagem.

![Imagem 15: Indique nesta aba, a empresa da ordem de carga e qual a ordem de carga que participará da viagem. Poderão ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4406648573591)

Se a marcação **"Usa UF da empresa da viagem como origem da MDF-e das Preferências"** (localizada no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-#bot%C3%A3ooutrasop%C3%A7%C3%B5es), opção **"Preferências"**) estiver desligada, ao registrar nessa aba uma Ordem de Carga associada a um documento fiscal de saída com origens em UF's diferentes, o pop-up **"Escolha UF Coleta dos MDF-e"** será exibido. Nesse pop-up, pode-se escolher a UF de origem desejada com base nas UF's identificadas nos documentos vinculados.

Com o parâmetro **"Manter ordem de carga vinculada ao MDF-e encerrado - ORDCARGMDFENC"** ligado, a ordem de carga permanecerá vinculada ao MDF-e mesmo depois do seu encerramento, com isso não será possível vincular a OC em outro MDF-e. Do contrário, quando o MDF-e estiver encerrado, a OC será automaticamente removida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Botão Outras Opções

Através do botão Outras Opções... presente no alto da tela, deverão ser realizadas as configurações de numeração e impressão dos manifestos, para sua posterior emissão.

Por meio da opção **"Controle de Numeração"**, será aberto o pop-up Controle numeração do MDF-e , nele defina a empresa emitente, a série empregada na numeração dos manifestos, o modelo de documento (no uso desta funcionalidade, o modelo deve ser 58), a numeração como automática (definição feita automaticamente), qual o último número de MDF-e emitido pela empresa e o limite de numeração dos manifestos.

![Imagem 16: Por meio da opção " Controle de Numeração" , será aberto o pop-up Controle numeração do MDF-e , nele defina a empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/4406663790999)

Ao acionar a opção **"Preferências"**, um pop-up de mesmo nome que será aberto, você pode estabelecer nele as seguintes particularidades:

- **Tipo de impressora:** O tipo da impressora na qual os manifestos serão impressos;
- **Caminho/impressora:** Determine aqui, qual o caminho ou nome da impressora em que os manifestos serão impressos;
- **Imprimir ao confirmar?:** Caso esta opção esteja marcada, quando os manifestos forem transmitidos e autorizados, sua respectiva impressão irá ocorrer automaticamente;
- **Usa UF da empresa da viagem como origem da MDF-e:** Marcando esta opção, indica-se que se o MDF-e possuir documentos com UF origem diferentes, será utilizada a UF da empresa emitente do MDF-e como origem;
- **Modelo DAMDFE:** Defina aqui, qual o modelo formatado para impressão do DAMDFE;
- **Número de cópias DAMDFE:** Informe quantas cópias deverão ser impressas do DAMDFE;
- **Modelo DAMDFE Contingência:** Determine qual o modelo formatado para impressão do DAMDFE em contingência;
- **Número de cópias DAMDFE Contingência:** Indique quantas cópias deverão ser impressas do DAMDFE em contingência.

![Imagem 17: Número de cópias DAMDFE Contingência : Indique quantas cópias deverão ser impressas do DAMDFE em contingência.](https://ajuda.sankhya.com.br/hc/article_attachments/4406663805847)

Através da opção **"Preferências do agendador de MDF-e em contingência"**, é possível determinar a periodicidade em que o sistema deverá executar a tarefa de verificação da existência de manifestos emitidos em contingência e automaticamente gerá-los no ambiente de autorização normal.

No pop-up que é aberto por esta opção, temos o botão **"Forçar execução"**, que executa a tarefa no momento em que é acionado. A marcação **"Ativo"** determina se o agendador está ou não operante. Na aba **"Frequência Agendamento"** determine em que horário do dia o sistema irá executar a tarefa; além disso, estabeleça se a frequência de execução dessa tarefa será Diária ou Semanal. Na aba **"Horários"**, o campo **"Próxima execução em"** será utilizado pelo sistema automaticamente; já no campo **"Data Final de Execução"** determine qual a data e hora para o agendador paralisar sua execução.

![Imagem 18: No pop-up que é aberto por esta opção, temos o botão "Forçar execução" , que executa a tarefa no momento em que é…](https://ajuda.sankhya.com.br/hc/article_attachments/4406663811223)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Demais botões

O botão **"Confirmar"**, transmite todos os manifestos gerados da viagem para a SEFAZ, um por vez. Todos podem ser autorizados, ou ainda um ou todos também podem ser rejeitados; para cada manifesto, seu status poderá ser visualizado. A grande vantagem da utilização deste botão, é a transmissão de todos os manifestos automaticamente.

Note também nesta tela, o botão **"Cancelar"**, que deve ser utilizado para cancelar todos os manifestos de viagem de uma vez. Vale citar que a justificativa informada para o cancelamento, será a mesma para todos os manifestos.

Além disso, na aba MDF-e, tem-se também o botão **"Confirmar"**, que é utilizado para transmitir somente o manifesto selecionado na aba. Seguindo o mesmo raciocínio, o botão **"Cancelar"** dessa aba também só realiza o cancelamento do manifesto selecionado.

Da mesma maneira, o botão **"Encerrar"** só o faz, no manifesto em questão. Ao encerrar o MDF-e, será aberto um pop-up denominado **"Encerrar MDF-e"** para que seja definida a cidade de encerramento do manifesto. Este procedimento, segue algumas regras:

- Ao confirmar a nota na tela Viagens de Transportes (MDF-e), o sistema irá utilizar o Código Município Fiscal presente no arquivo XML correspondente a cidade, de modo que ao encerrar o MDF-e, o pop-up mencionado será aberto com esta sugestão de cidade;
- Em situações onde existem duas notas MDF-e selecionadas com estados diferentes, o sistema irá apresentar a cidade e UF de cada documento em separado;
- Caso tenha mais de um Código Município Fiscal, ou existam códigos divergentes, ao encerrar o MDF-e, o pop-up será aberto com o campo da cidade em branco, para preenchimento manual;
- Se for selecionado duas notas juntas e estas correspondam a cidades diferentes, o pop-up Encerrar MDF-e será aberto em branco, para preenchimento manual.

Esta aba conta também com o botão para impressão do DAMDFE do manifesto selecionado, conforme Preferências de Impressão mencionadas no tópico Botão Outras Opções.

Dentro da aba MDF-e, temos o botão **"MDF-e"**:

![Imagem 19: Dentro da aba MDF-e , temos o botão "MDF-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/4406648619159)

As opções existentes no botão MDF-e, são:

- **Consultar status do serviço:** Verifica se o serviço de transmissão do MDF-e está em operação;
- **Consulta situação atual do manifesto:** Consulta a situação do manifesto em questão junto à SEFAZ;
- **Gerar arquivo XML de MDF-e:** Esta opção gera o arquivo XML do MDF-e autorizado;
- **Gerar arquivo XML de MDF-e para conferência:** Gera o arquivo XML do MDF-e sem informações de autorização, apenas para conferência (análise) de dados;

**Observação:** Inserindo um CNPJ nas configurações do parâmetro **"CNPJ ANTT p/ autorização de download de XML. - CNPJANTT"**, temos que, ao **"Gerar Arquivo XML de MDF-e para conferência"** através do botão **"MDF-e"**, será possível visualizar na tag **<autXML>** deste arquivo o mesmo CNPJ inicialmente configurado no parâmetro.

- **Gerar MDF-e em contingência:** Esta opção deve ser empregada quando o serviço de transmissão normal está fora do ar; ao acioná-la, o sistema gera a chave de acesso do MDF-e em contingência e imprime o DAMDFE em contingência;
- **Gerar lote:** Através desta opção, a geração do lote do manifesto;
- **Buscar autorização:** Em casos em que o manifesto está com o status Aguardando Autorização, esta opção busca esta autorização junto à SEFAZ;
- **Incluir condutor:** Esta opção inclui um condutor no manifesto - evento de inclusão de condutor;
- **Ver acompanhamentos:** Temos aqui, a consulta de todas as ocorrências registradas para o manifesto.
  ![Imagem 20: Ver acompanhamentos: Temos aqui, a consulta de todas as ocorrências registradas para o manifesto.](https://ajuda.sankhya.com.br/hc/article_attachments/4406663824279)

**Importante:** Após a transmissão do MDF-e com êxito, sua impressão poderá ser feita para que o veículo siga viagem. Posteriormente o MDF-e precisa ser encerrado para que não haja bloqueio da placa e percurso.  

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

### Inclusão do CT-e globalizados e não globalizados no mesmo MDF-e

Você pode vincular o [CT-e globalizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599654) e não globalizado no mesmo MDF-e, desde que ambos os CT-e's sejam lançados para uma mesma Ordem de Carga e com a mesma cidade de inicio e fim. Há duas formas para que os dois CT-e's sejam informados no mesmo MDF-e, são elas:

1. Primeiramente no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) realize o lançamento de dois CT-e's, um do tipo globalizado e o outro não globalizado, lembrando que para o CT-e globalizado é necessário informar o campo **"CT-e Globalizado"** do cabeçalho da nota. Depois, na tela Ordens de carga, informe o número da **"Ordem de Carga"** no painel principal e clique no botão **"Criar Viagem"**. Dessa forma, o sistema irá preencher automaticamente a tela [Viagens de transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514) com os dois tipos de CT-e's.
2. Na tela Viagens de transporte (MDF-e), inclua um novo registro por meio do botão ![Imagem 21: Na tela Viagens de transporte (MDF-e) , inclua um novo registro por meio do botão , informe os CT-e's na aba MDF-e ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16747424063767), informe os CT-e's na aba [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-#abamdf-e), sub-aba [Documentos MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e-#sub-abadocumentosmdf-e) e clique em confirmar. Feito isso, o sistema irá incluir os dois tipos de CT-e's.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#top)

Acesse também:

[Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-)

[Manifesto de Documentos Fiscais Eletrônicos - MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110673)
