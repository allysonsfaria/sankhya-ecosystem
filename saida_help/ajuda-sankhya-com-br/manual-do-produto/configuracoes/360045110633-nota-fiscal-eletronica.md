---
id: "360045110633"
titulo: "Nota Fiscal Eletrônica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:56:56Z"
rotulos: ["AJUDA DO SKW", "Configuração", "NF-e Pronta Entrega - Integração Landix", "Nota Fiscal Eletrônica", "Console NFe", "NF-e", "Estorno", "Receita Federal", "RFB", "Secretaria da Fazenda", "Acompanhamentos da NFe", "ajuste", "Cancelar Nota", "Características da NFe", "Danfe do SankhyaW", "Envio de XML da NFe por e-mail", "Gerar lote", "Impressão do DANFE", "Layout do DANFE", "Lei da Transparência", "Logomarca no DANFE", "NFe Cancelada", "Nota Cancelada", "Nota de Ajuste", "SanNFe", "TIMEOUTSTNFE", "Nota Fiscal Eletrônica manual", "XML", "VALCHAVETERC", "SEFAZ", "DANFE", "Contingências", "Documentos Eletrônicos"]
---

# Nota Fiscal Eletrônica

Entende-se por Nota Fiscal Eletrônica um documento onde sua existência é exclusivamente digital, emitido e armazenado eletronicamente, com intuito de documentar uma operação de circulação de mercadoria ou prestação de serviço, ocorrida entre as partes, cuja validade jurídica é garantida pela assinatura digital do emitente e recepção, pelo fisco, antes da ocorrência do fato gerador.

| [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFC1RCNCM2FJ5RR56HVZX0) | [SanNFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFC9SAP3DY66KY3KRBYENY) |
| --- | --- |
| [Acessando a NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#acessandoanf-e) | [Atualizando a situação da nota conforme a SEFAZ](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFCPQEZ7CZ5MSBGX81X01D) |
| [Danfe do Sankhya OM](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFDTNSKZYYSR2T2YCWZY2Z) | [Armazenamento e Envio do XML da NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFE6J2B0JNBDG3PHGS1ZAA) |
| [Logomarca no Danfe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFEFMMM9M67DCRVKZX2WFT) | [Envio de XML da NF-e/CC-e e Danfe por e-mail](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFEX2TD87WD40HNWE2ZDX5) |
| [Acompanhamentos da NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFF784X1GJF6V3NDD3MKRK) | [Cancelamento da NF-e após o prazo de 7 dias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFFKS0SWKS6B8FEDYK41AC) |
| [Função getFaturasXml](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFG5769E9RVWCEZQ7XNN0R) | [Notas Marcadas como Pendente de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFGE92NZ06V0815NXXH75N) |
| [NF-e Pronta Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFGQBRD6J3QJWJXZGXSP0W) | [Parâmetros que influenciam na NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#h_01FAGFH1AWT05DN5XCZ86QZ4QE) |

## Características

A Nota Fiscal Eletrônica possui as seguintes características:

- Uma NF-e é um documento digital, que atende aos padrões definidos no formato **"XML"** (Extended Markup Language).
- Garantia de autoria, integridade e irrefutabilidade, certificadas através de assinatura digital do emitente, definido pela Infraestrutura de Chaves Públicas Brasileiras (ICP Brasil).
- O arquivo da NF-e deverá seguir o layout de campos definido em legislação específica.
- A NF-e deverá conter um **"código numérico"**, obtido por meio de algoritmo fornecido pela administração tributária, que irá compor a **"chave de acesso"** de identificação da NF-e, juntamente com o CNPJ/CPF do emitente e número da NF-e.
- Para ser válida, a NF-e deverá ser enviada eletronicamente e autorizada pelo fisco, da circunscrição do contribuinte emissor, antes de seu envio ao destinatário e antes da saída da mercadoria do estabelecimento.
- A transmissão da NF-e será efetivada, via Internet, por meio de protocolo de segurança ou criptografia.
- A NF-e transmitida para a SEFAZ não pode ser alterada, permitindo-se apenas, dentro de certas condições, seu cancelamento.
- As NF-e deverão ser emitidas em ordem consecutiva crescente e sem intervalos a partir do 1º número sequencial, sendo vedados a duplicidade ou reaproveitamento dos números inutilizados ou cancelados.
- A critério das administrações tributárias, a NF-e poderá ter o seu recebimento confirmado pelo destinatário.

![Imagem 1: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16533425609623)**Informações adicionais:**

1. Na geração do XML para o setor de Combustíveis, será apresentado os campos do grupo **"L1 - Detalhamento Específico de Combustíveis"** e as tags **<cProdANP>**, **<CODIF>**, **qTemp> <ICMSComb>**, **<vBCICMS>, <vICMS>**, **<vBCICMSST>**, **<vICMSST>**, **<ICMSInter>**,**<vBCICMSSTDest>** e **<vICMSSTDest>**;
2. Na geração do XML para os Distribuidores de Medicamentos, serão apresentados os campos do grupo **"K - Detalhamento Específico de Medicamento"** e as tags **<nLote>**; **<qLote>**; **<dFab>**;**<dVal>** e **<vPMC>**;
3. A tag **<qLote>** será gerada com valor zero.

Em relação as empresas que trabalham com medicamentos, no XML da nota, pode-se ter a necessidade de apresentação da tag **<med>**; para que ela seja gerada, é necessário realizar as seguintes configurações:

- Ative os  parâmetros **"Informações adicionais para Lotes? - LOTEINFO"** e **"Usar data de validade junto com Lote? - LOTEDTVAL"**;
- O parâmetro **"Tabela de Preço PMC - CODTABPMC"** deve ser preenchido com um valor diferente de zero;
- Preencha o campo **"Gênero"**, da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), tela Cadastro do Produto, com a opção **"30 - Produtos Farmacêuticos"**;
- Além disso, o produto configurado deve possuir um preço de venda cadastrado.

De maneira simplificada, a empresa emissora de NF-e gerará um arquivo eletrônico contendo as informações fiscais da operação comercial, o qual deverá ser assinado digitalmente, de maneira a garantir a integridade dos dados e a autoria do emissor. Este arquivo eletrônico, que corresponderá à Nota Fiscal Eletrônica (NF-e), será então transmitido pela Internet para a Secretaria da Fazenda de jurisdição do contribuinte que fará uma validação prévia do arquivo e devolverá um protocolo de recebimento (Autorização de Uso), sem o qual não poderá haver o trânsito da mercadoria.

A NF-e também será transmitida para a Receita Federal, que será repositório nacional de todas as NF-e emitidas (Ambiente Nacional) e, no caso de operação interestadual, para a Secretaria de Fazenda de destino da operação e Suframa, no caso de mercadorias destinadas às áreas incentivadas.

As Secretarias de Fazenda e a RFB (Ambiente Nacional), disponibilizarão consulta, através da Internet, para o destinatário e outros legítimos interessados, que detenham a chave de acesso do documento eletrônico.

Para acompanhar o trânsito da mercadoria será impressa uma representação gráfica simplificada da Nota Fiscal Eletrônica. Esta representação é intitulada como DANFE (Documento Auxiliar da Nota Fiscal Eletrônica), em papel comum, em única via, que conterá impressa, em destaque, a chave de acesso para consulta da NF-e na Internet e um código de barras que facilitará a captura e a confirmação de informações da NF-e pelas unidades fiscais.

O DANFE não substitui e não é uma nota fiscal, servindo apenas como instrumento auxiliar para consulta da NF-e, pois contém a chave de acesso da NF-e, que permite ao detentor desse documento confirmar a efetiva existência da NF-e através do Ambiente Nacional (RFB) ou site da SEFAZ na Internet.

Na imagem abaixo, você pode observar o processo de Emissão e Transmissão de uma NF-e.

![Imagem 2: Na imagem abaixo, você pode observar o processo de Emissão e Transmissão de uma NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/4403905403415)

**Observação:** as equipes envolvidas, Sankhya e cliente, devem ter pleno conhecimento dos Manuais de Integração e de Contingências publicados pelo governo. A execução de todas as rotinas da empresa em ambiente de homologação "testes de validação" devem ser efetuadas, para posterior implementação em ambiente de produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## SanNFe

O SanNFe deve estar instalado no servidor de aplicações que roda o Sankhya Om, na pasta de usuário do sistema operacional que executa a aplicação. Essa pasta irá variar dependendo da versão do sistema operacional, por exemplo, no Linux a pasta é **"home/mgeweb"**, já no Windows sugerimos utilizar a pasta **"X:\SanNFe"**, onde **"X"** será o drive a ser utilizado.

**Nota:** no Sankhya Om, o SanNFe não precisa estar em execução para poder se emitir notas.

Além disso, na tela [Console NFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734) você deve informar o certificado da empresa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Acessando a NF-e

Nos Portais de [Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603174-Portal-de-Compras-Atributos-da-Tela#grade-resultadodaseleo), [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo) e [Mov. Interna](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108493-Portal-de-Mov-Internas-Atributos-da-Tela#grade-resultadodaseleo), na Grade- Resultado Seleção, temos através do botão ![Imagem 3: Nos Portais de Compra , Venda e Mov. Interna , na Grade- Resultado Seleção , temos através do botão "Opções para Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/4403897553943) **"Opções para Nota Fiscal Eletrônica"**, todas as opções acerca das Notas Fiscais Eletrônicas. Trataremos a seguir sobre as opções apresentadas neste botão:

![Imagem 4: Nos Portais de Compra , Venda e Mov. Interna , na Grade- Resultado Seleção , temos através do botão "Opções para Nota…](https://ajuda.sankhya.com.br/hc/article_attachments/4747486309655)

A rotina **"Consulta do Status do Serviço"** estabelecerá comunicação com a web service do ambiente definido nas preferências da empresa, **"homologação"** ou **"produção"**, considerando a UF da empresa solicitante, empresa da nota, retornando com o **"Status"** da resposta. Ao clicar nessa opção, será aberto um pop-up com as informações do status do serviço ativo:

![Imagem 5: A rotina "Consulta do Status do Serviço" estabelecerá comunicação com a web service do ambiente definido nas…](https://ajuda.sankhya.com.br/hc/article_attachments/4404415210007)

**Observação:**para que o sistema impeça que o usuário consulte o status da NF-e, nos casos em que a emissão tiver sido realizada por terceiros, é necessário que na tela [Tipos de Operação- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), campo **"Base numeração"**, você configure a opção **"Manual"**. Além disso, na aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), campo **"NF-e"**, selecione a opção **"Terceiros"**. Caso o usuário tente visualizar, o sistema exibe a seguinte mensagem:

**"Uma das notas selecionadas é de emissão de terceiros, portanto esta opção não pode ser acessada."**

A opção **"Consulta Situação Atual da Nota"** é utilizada para verificar se a NF-e em processamento, (serviço assíncrono) já foi liberada ou simplesmente, consultar uma NF-e já autorizada. Ao clicar nessa opção, em notas que já foram enviadas, será apresentado informações importantes, como a **"Chave de Acesso"**, **"Data e hora de recebimento"**, dentre outras.

![Imagem 6: A opção "Consulta Situação Atual da Nota" é utilizada para verificar se a NF-e em processamento, (serviço assíncrono)…](https://ajuda.sankhya.com.br/hc/article_attachments/7267785382551)

Você pode verificar também notas que ainda não foram enviadas. Nesse caso será apresentado o número da nota, informando que esta não tem chave NF-e.

![Imagem 7: Você pode verificar também notas que ainda não foram enviadas. Nesse caso será apresentado o número da nota, informando…](https://ajuda.sankhya.com.br/hc/article_attachments/4404400775191)

**Nota:** no caso da realização do lançamento de notas de entrada avulsas, pode-se fazer uso do parâmetro **"Validação da chave de acesso da NF-e de terceiros - VALCHAVETERC"**, que quando ativado, valida a chave NF-e do parceiro, permitindo ou não a continuidade no lançamento, dependendo do que for configurado. Porém, se a nota que está sendo lançada possui sua série de 890 a 899, o CNPJ presente na chave da NF-e não será validado, pois o CNPJ deste caso pertence a Sefaz e portanto, a nota poderá ser confirmada mesmo com o referido parâmetro ativado.

**Observação:** o parâmetro **"Timeout de cache do status do serviço NFe - TIMEOUTSTNFE"** possui o valor **"5"** como padrão, que se refere ao tempo em minutos para realização do cache de retorno do status do serviço por UF; esse cache é utilizado em consultas futuras, de modo a evitar que o sistema tenha que efetuar novas consultas até o timeout do cache.

Ao clicar na opção **"Pendente de Retorno"** será apresentada a opção **"Marcar como Pendente de Retorno"**, que ao ser acionada, fará com que as informações da NF-e sejam encaminhadas para outro registro, e esta precisará ser Cancelada após sua aprovação. Dessa forma, uma nova NF-e poderá ser gerada para este lançamento.

Na opção **"DANFE de segurança"** a alternativa **"Marcar como DANFE de segurança"** deve ser utilizada apenas em contingência. Ao selecionar esta opção, o DANFE precisará ser impresso em Formulário de Segurança (FS-DA).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Atualizando a situação da nota conforme a SEFAZ

É necessário configurar o ambiente de homologação da SEFAZ, para a sincronização de status, dessa forma:

1. Com a nota confirmada, no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) consulte a situação atual da nota na SEFAZ, através do botão  **"NF-e"**  opção **"Consulta situação atual da nota"**;
2. Ao abrir o pop-up de consulta de situação de nota, caso a situação no sistema esteja diferente da situação atual da nota na SEFAZ, será exibida uma caixa de diálogo, informando que a situação da nota no sistema está diferente da situação atual na SEFAZ, possibilitando a sincronização dos dados da nota através de um botão de confirmação.
3. Ao confirmar a atualização da situação da nota, alguns serviços serão chamados como Impressão da Nota, Impressão de Boleto, Envio de E-mails, Compensação Financeira, sendo estes os mesmos serviços executados quando é utilizada a opção de **"Buscar autorização"**, seguindo a rotina normal de uma nota aprovada;

**Observação:** esta atualização contempla apenas notas que estejam com a situação **"Enviada"** ou **"Aguardando Aprovação"** . Vejamos a seguir, alguns exemplos de situações:

- **Notas Enviadas:** Se caso tenha sido gerado o lote de um nota e houver algum problema na comunicação com a SEFAZ, a nota não será processada pela SEFAZ, logo sua situação ficará com status Enviada, e posteriormente poderá ser consultada e processada pela SEFAZ.
- **Notas Aguardando Aprovação:** Ocorrerá quando uma nota for recebida pela SEFAZ mas ainda não foi processada, ficando marcada no sistema como Aguardando Aprovação.

**Observação:** quando realizada a consulta de situação de uma nota marcada no sistema como Enviada ou Aguardando Aprovação, o sistema tentará enviar a nota à SEFAZ. O comportamento esperado será o mesmo comportamento da opção Buscar Autorização.

- **Notas Rejeitadas:** São notas não validadas pela SEFAZ e consequentemente não registradas na base da SEFAZ. Exemplo de causas comuns, erros nas informações da nota, empresa não cadastrada, certificação corrompida.

**Nota:** uma nota Rejeitada poderá ser corrigida e submetida novamente à SEFAZ, utilizando-se a mesma numeração de nota ou com uma nova numeração, já que uma nota rejeitada não é registrada na base de NF-e’s.

- **Notas Denegadas:** Ocorre quando o emissor, e em alguns casos o destinatário também, apresentam pendências fiscais. Neste caso a empresa estará impedida de faturar até que ela regularize sua situação fiscal.

**Observação:** diferente da situação de rejeição, NF-e's denegadas são registradas na base da SEFAZ, impedindo a reutilização daquela numeração de NF-e posteriormente.

A opção **"Impressão do DANFE"** será apresentada no final desse artigo.

Através da opção **"Inutilização de Numeração"**, informe os campos **"Empresa"**, **"Data de Movimento"**, **"Modelo de doc. fiscal"**, **"Série da nota"** e **"Numeração"**, e o intervalo de numeração a ser inutilizado. Depois clique em **"OK"**.

**Observação:** no caso de inutilizar uma numeração, ao gerar o lote as notas não serão enviadas.

**Nota:** para maiores detalhes sobre o processo de Inutilização de Numeração, acesse o link [Inutilização de documentos fiscais eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052225474-Inutiliza%C3%A7%C3%A3o-de-documentos-fiscais-eletr%C3%B4nicos).

A opção **"Gerar XML da NFe em arquivo para conferência"**, gera o XML da nota para que você possa conferir as informações. Se o navegador impedir a abertura da janela, deve-se  liberá-la e clicar novamente na opção para gerar o XML.

Através da opção **"Gerar Lote"**, efetua o envio da NF-e para a web service. Mesmo processo do botão **"Confirmar"**. Lembrando que, a geração e envio de lote limita-se a 50 notas.

**Observação:** no Sankhya Om verifique o serviço ativo no momento, e ao enviar, se tiver algum problema, o lote será enviado para o próximo serviço. A ordem de execução dos serviços é SEFAZ, SCAN, EPEC.

**Nota:** esta opção não terá efeito se a NF-e já tiver sido enviada.

**Observação:** o modo síncrono para a UF de São Paulo está disponível apenas para a NFC-e de modelo 65. Desse modo, para a NF-e de modelo 55 é necessário desabilitar a marcação **"Usar modo Síncrono para envio do XML"**, localizada nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral).

**Observação:** ao selecionar uma nota que esteja com o **"Status NF-e" = "Aguardando Correção"** ao clicar na opção Gerar lote, caso a data e/ou hora estejam diferentes da data e/ou hora do servidor, o parâmetro **"Obriga Dt.Negoc. ser igual a do servidor? - DTNEGSERV"** terá o seguinte comportamento:

- Se estiver habilitado, será realizada a alteração da data e/ou hora do documento de forma automática.
- Caso esteja desabilitado, será apresentado um pop-up questionando se você deseja manter a data e/ou hora do documento ou se deseja ajustar estas informações para que estejam de acordo com as informações do servidor.

**Observação:** por meio do parâmetro **"Qtd Casas Desc. ao Valid Prop Pis/Cofins - DECPISDESP"** será definido o round utilizado na sumarização durante a comparação ao gerar o XML, assim, quando houver a diferença em casas decimais superiores a dez após a vírgula, a tag <**vOutro**> será gerada corretamente.

Desta forma, será possível alterar as datas de negociação, faturamento e entrada/saída de acordo com o mesmo comportamento da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ao realizar a confirmação de uma nota com data diferente do servidor.

**Importante:** realize a atualização destas datas e horas, pois, se um boleto estiver vinculado à estas datas e for efetuado a correção do cadastro dias depois, a nota e o boleto serão recebidos com datas de saídas incorretas, ocasionando a perda do prazo negociado.

A opção **"Buscar Autorização"** será utilizada no processo assíncrono, para identificar status de processo de notas, que estão **"Aguardando Autorização"**.

**Nota:** ainda sobre a Busca de Autorização, podem ocorrer casos em que a empresa gera várias Notas Fiscais Eletrônicas em um curto período de tempo; este processo pode dificultar a resposta da Sefaz quanto à autorização/aprovação das notas, bem como atrasar as impressões dos Danfes e de seus respectivos boletos. Considerando a autorização/aprovação das notas, tem-se três considerações importantes:

- No parâmetro **"Lista de UFs com autorização de NF-e assíncrona - LISTAUFNFEASYNC"** informe as siglas dos Estados para os quais ao emitir as notas (gerar o lote), o processamento dos lotes não será feito de imediato, ficarão com o status Aguardando Autorização; somando-se a isso, o sistema conta com um recurso interno (job) que dinamiza esta situação, verificando periodicamente (a cada 10 segundos) se existem notas para busca de autorização junto à Sefaz; o job fará um total de 30 tentativas de busca de autorização por nota; excedendo esse limite, a busca pela autorização deverá ser feita manualmente.
- Através do parâmetro **"Intervalo em minutos p/ buscar autorização de NF-e - INTBUSCAAUTNFE"** determina-se após quantos minutos o sistema deverá buscar a autorização novamente de uma nota que foi processada ao menos uma vez.
- Tem-se ainda, o parâmetro **"Imprime Danfe ao buscar autorização de NF-e? - IMPDANNFEBUSAUT"** que é o responsável por solicitar ou não a impressão do Danfe ao buscar a autorização das notas.

As opções **"Marcar as notas como EPEC"**, **"Retirar das notas a marcação de EPEC"** e **"Enviar como EPEC"**, representam a modalidade de contingência eletrônica para as Notas Fiscais Eletrônicas através da **"Declaração Prévia de Emissão em Contingência - EPEC"**, a saber:

- Constatando-se a impossibilidade do envio de uma Nota Fiscal Eletrônica por problemas de recepção da Sefaz (Secretaria da Fazenda), o você deverá selecionar a opção **"Marcar Notas como EPEC"** e em seguida a opção **"Enviar como EPEC"**.
- As notas enviadas como EPEC, são enviadas para um endereço de internet diferente do que é utilizado no envio normal das Notas Fiscais Eletrônicas de cada Estado, este endereço é específico para o recebimento de notas enviadas em contingência eletrônica. Por isso, logo após o reestabelecimento do serviço da Sefaz deve-se gerar o lote das notas enviadas como EPEC, para que estas notas constem na base de dados da Sefaz.
- O tipo de **"Emissão NF-e"** destas notas ficará como EPEC e seu **"Status NF-e"** como **"Aprovada"**, desde que não haja nenhum problema na validação das mesmas.
- No cabeçalho das Notas Fiscais Eletrônicas são apresentados os campos **"Nro.Registro EPEC"** e **"Dt. Registro EPEC"**, estes campos fornecerão mais informações sobre as Notas Fiscais Eletrônicas que foram enviadas como EPEC.

A opção **"Carta de Correção"** abrirá o pop-up **"Carta de Correção Eletrônica"** para que você possa entrar com a correção da nota fiscal, que é um texto livre conforme a nota técnica 2010/008 disponibilizada pela Receita Federal. Temos nesse pop-up os botões para envio ou cancelamento da **"CC-e"**. Lembrando que, será realizada uma nota por vez.

**Observação:** o envio de CC-e é um evento que só será aceito para Notas já autorizadas na SEFAZ.

Conforme a nota técnica 2010/008 uma correção substitui a anterior, por isso, quando o sistema identifica que já houve o envio de uma carta o texto referente a esse envio é apresentado no pop-up Carta de Correção Eletrônica para alteração.

Neste caso também é apresentado o texto, **"Carta de Correção já enviada"**, na cor **vermelha** informando que já houve o envio de carta de correção para a nota.

A Carta de Correção Eletrônica (CC-e) faz parte de um processo maior por parte da SEFAZ, sendo considerado um "evento".

Ao enviar a Sefaz o evento de Carta de Correção Eletrônica, caso este seja processado e vinculado (termo utilizado pela Receita Federal, o qual vincula o evento a uma NF-e), a janela será automaticamente fechada e apresentada a mensagem de carta enviada com sucesso.

Quando selecionada a opção **"Enviar XML da NF-e/CC-e e Danfe por e-mail"**, será enviado ao e-mail cadastrado, o XML da NF-e e CC-e, o PDF da NF-e (DANFe) e, também, o PDF da Carta de Correção, caso exista alguma gerada.

**Observação:** caso esta rotina seja utilizada sem um modelo de impressão de Carta de Correção inserido na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), sub-aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaCT-e) (aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)), campo **"Relatório Carta de Correção"**, o sistema não encaminhará o PDF no e-mail e não emitirá qualquer mensagem de aviso.

Caso seja enviada uma Carta de Correção para uma determinada nota, você poderá enviar o e-mail através da opção Enviar Xml da NF-e/CC-e e Danfe por e-mail. Essa opção identificará que existe uma Carta de Correção Eletrônica (CC-e) e enviará o arquivo de distribuição da CC-e juntamente com o da Nota Fiscal Eletrônica e opcionalmente o Danfe, para os destinatários já configurados no sistema. Neste caso o assunto do e-mail será alterado para indicar que a mesma possui correção, por exemplo:

Envio da NF-e - N.Doc 000000008 - Série 1 + Carta de Correção (CC-e)

**Nota:** ao confirmar ou solicitar a geração de um lote de NF-e, o Sankhya Om possibilita o envio automático de e-mail com o XML de distribuição da nota, como nesse momento ainda não existe Carta de Correção, somente será enviado o XML da nota.

O sistema não enviará automaticamente o e-mail para o cliente/transportadora com o arquivo de distribuição da Carta de Correção Eletrônica (CC-e).

**Importante:** a rotina de envio de XML da NF-e para o e-mail do destinatário trará as informações do sistema em que está sendo enviado o e-mail. Os e-mails relacionados à NF-e além de conter a Assinatura Sankhya, irão possuir os seguintes dados:

| **Autorizado o uso    da NF-e** | **Dados da NF-e** | **Dados do Emitente** | **Dados do Destinatário** |
| --- | --- | --- | --- |
| - Chave de acesso. | - Número; - Série; - Data de Emissão; - Protocolo de Autorização; - Ambiente; - Tipo de Emissão; - Valor da NF-e. | - Razão Social; - CPF/CNPJ; - Endereço; - Município; - UF; - Telefone; - E-mail. | - Razão Social; - CPF/CNPJ; - Endereço; - Município; - UF. |

A opção **"Imprimir a Carta de Correção"** permite a impressão da Carta de Correção Eletrônica, para isso você deve possuir permissão para imprimir notas de venda. Você pode selecionar uma ou várias notas para imprimir a carta de correção, porém, para que uma nota tenha sua carta de correção impressa ela já deve estar aprovada na SEFAZ e a carta de correção já deve ter sido enviada. Ao solicitar a impressão da carta de correção, o sistema imprimirá a carta de cada uma das notas selecionadas. Caso uma ou mais notas não possuam carta de correção, o sistema exibirá numa janela o número único das notas e um texto informativo.

Para configurar a carta de correção, você deverá seguir os seguintes passos:

- Primeiramente, acesse a tela [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034) e selecione no botão **"Baixar Modelos Padrões"** a opção **"Carta de Correção"**. Assim, você pode personalizar o modelo da carta de correção através do iReport.
- Com o modelo da carta de correção pronto, acesse a tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694) e cadastre o modelo de carta de correção.
- Uma vez que o relatório formatado com o modelo de carta está configurado, você deve associar esse modelo nas preferências da empresa que emite NF-e. Para isso, acesse a tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) e informe o código do relatório de carta de correção no campo **"Relatório Carta de Correção"**, da sub-aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaCT-e) da aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos).

A opção **"Acompanhamento de Eventos"** é semelhante ao acompanhamento de envio da NF-e, contudo, é específica para eventos. Em caso de ocorrer algum erro de validação de schemas, assim como o envio da NF-e, será apresentada a tela de Acompanhamento de eventos. O usuário poderá ainda consultar todos os eventos ligados a NF-e através desta opção.

**Nota:** quando for utilizada a contingência EPEC, o acompanhamento da nota é feito por esta opção Acompanhamento de Eventos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Danfe do Sankhya OM

O Danfe do Sankhya Om funciona de uma forma diferente do Danfe do MGE que é interno no sistema. No Sankhya Om, a impressão é configurada através da definição do Relatório Formatado Danfe, cujos modelos padrões estão disponíveis para download na tela de [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034).

Para se imprimir um Danfe, deve-se primeiro informar os modelos de **"Danfe paisagem"** e **"Danfe retrato"** na tela de [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694). Para cada modelo temos três arquivos que devem ser informados. Vejamos 3 exemplos para cada um deles:

**Danfe paisagem:** danfe\_paisagem.jrxml, danfe\_paisagem\_itens.jrxml, danfe\_paisagem\_sub.jrxml.

**Danfe retrato:** danfe\_retrato.jrxml, danfe\_retrato\_itens.jrxml, danfe\_retrato\_sub.jrxml.

**Observação:** para a impressão do DANFE pelo sistema, é necessário possuir o Plugin Java devidamente instalado no navegador.

**Nota:** na impressão do Danfe serão impressas a data e hora da entrada e saída da NF-e.

Nas Preferências da Empresa, aba [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e) da sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e) (aba Documentos Fiscais Eletrônicos), o campo **"Relatório Formatado do DANFE"** deve se informar qual modelo de Danfe a empresa usará, **"Paisagem"** ou **"Retrato"**.

Para se utilizar o relatório de dados adicionais no Sankhya Om é necessário observar o seguinte:

A TOP de NF-e utilizada no MGE, que é a mesma que o Sankhya Om utiliza, possui um relatório de dados adicionais que foi cadastrado na tela [Modelos de Nota Fiscal/Duplicata/Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913) e informado na TOP no campo **"Modelo para Dados Adicionais de NF-e"**.

Com a configuração dessa forma, na tela Modelos de Nota Fiscal\Duplicatas\Boletos do Sankhya Om, deve se cadastrar o arquivo de dados adicionais do Danfe do Sankhya Om e informar o correspondente dele no MGE. Isso será feito no campo **"Número do relatório modelo"**.

![Imagem 8: Com a configuração dessa forma, na tela Modelos de Nota Fiscal\Duplicatas\Boletos do Sankhya Om , deve se cadastrar o…](https://ajuda.sankhya.com.br/hc/article_attachments/7647703698199)

**Importante:** o campo **"Layout do DANFE"** da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), sub-aba [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e) (sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e) da aba Documentos Fiscais Eletrônicos) não tem influência no layout do Danfe.

Diferente do MGE, o Danfe do Sankhya Om mostrará sempre todas as colunas na grade de produtos.

O parâmetro **"Tenta imprimir nota no servidor?' - IMPRNOTASERV"** por padrão vem ligado. Este habilita a impressão de nota fiscal no servidor. Ou seja, estando ligado, a impressão do DANFE é realizada na máquina servidora, e estando desligado a impressão é enviada para o cliente (máquina do usuário).

**Nota:** quando ocorrer a mensagem: **"Não foi possível carregar a fonte de dados XML"** ao solicitar impressão de notas\pedidos, significa que o modelo configurado na TOP para impressão possui um relatório formatado equivalente ao DANFE e o movimento do qual foi solicitado impressão não é NF-e.

Para impressão de DANFE de NF-e com [Desoneração de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025394913-Desonera%C3%A7%C3%A3o-do-ICMS) acesse o link.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Armazenamento e Envio do XML da NF-e

Empresas que trabalham com Notas Fiscais Eletrônicas (emitentes e destinatários), deverão manter as Notas em arquivo digital pelo prazo estabelecido na legislação tributária para a guarda dos documentos fiscais, devendo estas serem apresentadas à administração tributária, quando solicitado.

Através da tela [Gerar Arquivo XML de NFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596034) o usuário do sistema fará a geração e download do arquivo XML de NF-e já aprovadas e com chave NF-e para um diretório em sua máquina, possibilitando a visualização destes arquivos no visualizador do governo.

![Imagem 9: Através da tela Gerar Arquivo XML de NFe o usuário do sistema fará a geração e download do arquivo XML de NF-e já…](https://ajuda.sankhya.com.br/hc/article_attachments/7647596983319)

Todos os campos desta tela são filtros para que o usuário possa selecionar a NF-e que deseja **"Fazer Download"**, sendo que o **"Período"** é obrigatório. Contudo, se o usuário informar a **"Chave Nfe"**, as demais opções de filtro serão desabilitadas:

O filtro trará apenas notas Aprovadas ou Denegadas. Qualquer outro tipo de status NF-e não será filtrado.

**Empresa:** Informa-se neste campo a Empresa do Lote que se deseja fazer download, podendo esta ser pesquisada pela opção de **"Pesquisa"**. É necessário informar o período de emissão deste lote, por isto a opção Período é de preenchimento obrigatório.

**Período:** Informa-se neste campo as datas **"iniciais"** e **"finais"** da emissão do lote, para compor o filtro.

**Observação:** ao informar Empresa e Período os campos de pesquisa pela Chave NF-e e **"Número da Nota"**, ficam desabilitados.

Isto porque o sistema permite que seja feito dois tipos de filtro pra Download:

- Se desejar fazer download de um **"Lote de Notas"** deverá informar a Empresa e o Período de emissão dos mesmos (Período), e neste caso o sistema gerará um arquivo compactado com todos os XML.
- Se desejar fazer download de uma única Nota Fiscal Eletrônica, bastará informar apenas a Chave NF-e ou o próprio Número e Série da Nota.

**Chave NFe:** Informa-se neste campo a chave NF-e, para compor o filtro. Bastará esta informação pra que o sistema selecione a Nota a ser exportada, uma vez que cada nota possui apenas uma única chave, logo como foi dito anteriormente, os demais campos de filtro são desabilitados, quando a Chave NF-e é informada.

**Número da nota\Série:** Informa-se nestes campos o número e a série da nota desejada. Uma vez que cada nota possui apenas um número, os demais campos de filtro serão desabilitados.

Se o usuário informar apenas o Número da Nota, o sistema exibirá a seguinte mensagem:

**"Erro**

**Não foi encontrado NFe para esta nota: xxxxx e série:xx"**

Caso seja informado apenas a Série, o sistema exibirá a seguinte mensagem:

**"Atenção**

**Ao informar a série a nota deve ser informada."**

Ao clicar no botão **"Fazer Download"**, o arquivo XML será exportado para visualização no programa SPED-Visualizador de Documentos Fiscais Eletrônicos.

Se o navegador utilizado pelo usuário bloquear o pop-up impedindo o download, será necessário desbloqueá-lo.

O arquivo XML é exportado compactado, o usuário deverá descompactá-lo e no **"Visualizador de Documentos Fiscais Eletrônicos"** importá-lo para o **"Repositório"**, para então clicar no arquivo e visualizá-lo.

![Imagem 10: O arquivo XML é exportado compactado , o usuário deverá descompactá-lo e no "Visualizador de Documentos Fiscais…](https://ajuda.sankhya.com.br/hc/article_attachments/7267828712855)

Visualizador de Documentos Fiscais Eletrônicos.

![Imagem 11: Visualizador de Documentos Fiscais Eletrônicos.](https://ajuda.sankhya.com.br/hc/article_attachments/7267830141975)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Logomarca no Danfe

O arquivo com a logomarca é indicado no campo **"Arquivo Logomarca"** da Aba [NFe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e)/tela Empresa. Nesse campo determina-se o caminho onde será encontrado o arquivo de imagem com a logomarca da empresa, para que seja impressa no DANFE.

Este caminho pode ser definido de duas formas diferentes:

1) O arquivo será obtido a partir da pasta no servidor definida pelo parâmetro SERVDIRMOD. Exemplo:

Considerando que o parâmetro SERVDIRMOD seja /home/mgeweb/modelos e que o nome do arquivo seja logoemp1.jpg, então o valor do campo **"Arquivo Logomarca"** deve ser logoemp1.jpg. Naturalmente, o arquivo deve ter sido copiado para dentro da pasta /home/mgeweb/modelos para que tudo funcione.

**Observação:** deve ser observado que em servidores UNIX os nomes de arquivos são sensitive-case, portanto, se houver diferença de maiúsculas e minúsculas o logotipo não será mostrado.

2) Usar uma path relativa ao repositórios de arquivos do Sankhya Om, assim:

```
    Repo://imagens/logoemp1.jpg
```

Note o prefixo 'Repo://', isso determina que o caminho seja relativo ao repositório de arquivos e neste caso sistema irá buscar o arquivo logemp1.jpg no repositório de arquivos dentro da pasta imagens.

**Nota:** o layout do DANFE definido pela Secretaria da Fazenda possui um lugar onde opcionalmente pode-se colocar uma logomarca, desde que a mesma não comprometa as informações de **"Identificação do emitente"**, que estão posicionadas ao lado da logomarca. O componente usado no DANFE possui largura = 65 pixels, altura = 72 pixels e está configurado para centralizar a imagem. Esse componente não possui a função de redimensionar a imagem, ajustando-a ao seu tamanho.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Envio de XML da NF-e/CC-e e Danfe por e-mail

Para o correto funcionamento desta rotina é necessário realizar algumas configurações:

Na tela Cadastro do Parceiro\[aba NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e) onde:

- No campo **"Tipo do anexo"** o usuário poderá escolher se o e-mail será mandado como arquivo compactado (extensão zip) ou arquivo normal (extensão xml).
- No campo **"E-mail p/ envio de NF-e"** deve ser informado o e-mail para onde será enviado o XML da Nota, caso o campo **"Ambiente NF-e"**, da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), esteja configurado como **"Produção"**.

**Nota:** se o campo Ambiente NF-e estiver configurado como **"Homologação"**, enquanto a NF-e estiver em implantação, o e-mail será enviado para o e-mail da própria empresa, cadastrado na tela [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293), na aba Endereço, campo **"Email"**. Uma vez que o Ambiente NF-e tenha sido alterado para Produção, o e-mail será enviado para o e-mail do parceiro da nota, que deverá ser cadastrado no cadastro do Parceiro, campo **"E-mail p/ envio de NF-e"**.

É importante informar que, para que o Danfe seja enviado, na TOP o campo **"Imprimir"** da Aba Impressão deve estar informado como **"Na confirmação"**. Dessa forma, ao gerar o Lote da NF-e, o Danfe será impresso e o e-mail será enviado com o XML e o Danfe.

Tem-se ainda a possibilidade de enviar o e-mail de forma manual, pelo botão **"Outras opções"** escolhendo a opção **"Nota Fiscal Eletrônica"** e respectivamente,**"Enviar XML da nota por e-mail"**.

Na TOP se o campo Imprimir estiver como Manual e você desejar enviar o Danfe junto com o XML no e-mail, deverá imprimir o Danfe antes de enviar Manual. Ou seja, para que o Danfe seja enviado, ele deve ter sido impresso anteriormente, caso contrário o Danfe não será enviado.

**Observação:** o arquivo XML da nota será enviado para a lista de e-mails tanto do parceiro Destinatário, quanto do parceiro Transportador, se o campo **"E-mail p/ envio NF-e/NFS-e/CT-e"** do cadastro de Parceiros, aba [NF-e/NFS-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abanf-enfs-ect-e) estiver preenchido. Lembrando que, o parceiro Transportador receberá o e-mail mesmo que o parceiro Destinatário não tenha e-mail cadastrado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Acompanhamentos da NF-e

A opção **"Ver acompanhamento"** será muito útil quando ocorrer um problema na geração e envio de Lotes de Notas. Através desta opção, você poderá verificar qual problema ocorreu no envio do Lote e providenciar a correção.

![Imagem 12: A opção " Ver acompanhamento" será muito útil quando ocorrer um problema na geração e envio de Lotes de Notas. Através…](https://ajuda.sankhya.com.br/hc/article_attachments/7647583732247)

Quando selecionar uma nota que não possui ocorrência, ou seja, não apresenta nenhum problema, e clicar em Ver acompanhamentos, o sistema emitirá a mensagem:

**"Lista de acompanhamentos vazia!"**

Nesse caso a Nota não possui nenhuma informação para mostrar ao usuário.

Ao selecionar, por exemplo, uma Nota de NF-e que esteja com o Status **"Aguardando correção"** e clicar na opção Ver acompanhamentos, o sistema abrirá uma pequena tela de [Ocorrência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604834), apenas informativa.

Na grade superior desta tela serão visualizadas as notas recusadas.

Logo abaixo será mostrado o acompanhamento da nota com a Data e Descrição da ocorrência.

O botão **"Ver observação"** mostra detalhes da observação do Lote ampliando a informação, facilitando a visualização. O mesmo ocorre com o botão Ver ocorrência que mostra detalhes da ocorrência selecionada.

Para visualizar os detalhes pode-se utilizar também o duplo clique do mouse e não somente os botões.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Cancelamento de NF-e após o prazo de 7 dias

O Ato COTEPE/ICMS nº 33/08 prevê um prazo máximo de 168 horas para o cancelamento de uma NF-e, todavia, em alguns estados como na SEFAZ-MG permite-se através do Decreto nº 44.747/08 o cancelamento após este prazo desde que seja protocolada Denúncia Espontânea na Administração Fazendária relatando o fato e demonstrando que a operação não tenha ocorrido.

Importante ressaltar que um documento fiscal somente pode ser cancelado antes da sua escrituração no livro próprio caso não tenha ocorrido à saída da mercadoria ou o início de prestação do serviço.

Maiores esclarecimentos vide CONSULTA INTERNA Nº 085/2009 – 05/06/2009.

Por isso, foi disponibilizado no sistema a permissão de efetuar cancelamentos de NF-e para notas que possuam sua emissão acima de 7 dias permitidos.

Neste momento, este comportamento somente será válido para Minas Gerais; e é de total responsabilidade da empresa usuária o encaminhamento e protocolização da denúncia espontânea. A Sankhya não se responsabiliza por cancelamentos efetuados sem o devido respaldo legal.

Para esta configuração, foi criado o parâmetro **"Estados que podem cancelar NFe após 168 hs - UFORIGCANM168"**, que deverá ser preenchido com o(s) Estado(s) que permita(m) esta situação.

Após a configuração do parâmetro, ao solicitar o cancelamento da nota no Portal (Venda, Compra, Interna, ou seja, os tipos de movimento que permite emissão da NF-e), será aberto uma tela solicitando a justificativa do cancelamento e posteriormente será solicitado a inserção do número do protocolo e a Dt. Protocolo Canc.

![Imagem 13: Após a configuração do parâmetro, ao solicitar o cancelamento da nota no Portal ( Venda , Compra , Interna , ou seja,…](https://ajuda.sankhya.com.br/hc/article_attachments/7267889150871)

Depois de preenchidos os campos e clicado em ok o sistema emite a mensagem:

**"Nota cancelada com sucesso!"**

Para visualização da nota cancelada deve-se acessar a tela [Notas Canceladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913):

![Imagem 14: Para visualização da nota cancelada deve-se acessar a tela Notas Canceladas :](https://ajuda.sankhya.com.br/hc/article_attachments/7647457284375)

Importante: não é possível o cancelamento das Notas Fiscais Eletrônicas aprovadas a mais de 24 horas, portanto, nesse caso será feito o "Estorno" e envio da Nota  como ajuste da nota aprovada, para assim poder ser validado o cancelamento destas notas.

Para que isso seja possível ao clicar em **"Cancelar Nota"** será necessário informar uma TOP de Devolução, e então o sistema duplicará a Nota aprovada e realizará o estorno, lançando uma Nota de Devolução para realização dos devidos ajustes (Nota de Ajuste), visto que esse tipo de cancelamento só ocorrerá quando a Nota de Origem estiver aprovada a mais de 24 horas e o estado não estiver nas preferências dos estados, que podem cancelar até 7 dias (Parâmetro - UFORIGCANM168).

A utilização de Estorno da NF-e depende da regulamentação de cada UF. As principais características da NF-e de estorno são:

**a)** Finalidade de emissão da NF-e (campo FinNFe) = '3' - NF-e de ajuste;

**b)** Descrição da Natureza da Operação (campo natOp) = Estorno de NF-e não cancelada no prazo legal?;

**c)** Referenciar a chave de acesso da NF-e que está sendo estornada (campo refNFe);

**d)** Dados de produtos/serviços e valores equivalentes aos da NF-e estornada;

**e)** Códigos de CFOP inversos aos constantes na NF-e estornada;

**f)** Informar a justificativa do estorno nas Informações Adicionais de Interesse do Fisco (campo infAdFisco).

### Cancelamento Extemporâneo

A SEFAZ do estado de Mato Grosso/MT prevê o prazo máximo de 2 horas para cancelamento da NF-e. Deste modo, todas as notas que forem canceladas fora do referido prazo deverão ser escrituradas como um Cancelamento Extemporâneo.

### Emissão de NF-e para Parceiro Estrangeiro em Operação dentro do Estado

Na emissão de uma NF-e para Parceiro estrangeiro Consumidor Final Não Contribuinte em operação dentro do Estado, deverão estar com as qualificações cadastrais do Parceiro Estrangeiro adequadas (endereço, país, idEstrangeiro), a **"Classificação do ICMS"** ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal)) marcada como **"Consumidor Final Não Contribuinte"**, de forma que no XML, a tag **<idDest>** encontre-se com índice **"1"**, representando operação interna (dentro do estado) e a tag **<idEstrangeiro>** esteja preenchida corretamente.

**Nota:** deste modo, estas configurações evitarão a rejeição do XML pelo webservice da SEFAZ com a mensagem **"721 - Rejeição: Operação interestadual deve informar CNPJ ou CPF"**.

### Processo de contingência da Nota Fiscal Eletrônica referente à Pendência de Retorno

O processo de contingência da Nota Fiscal Eletrônica referente a Pendente de Retorno para o Sankhya Om possui o mesmo comportamento que o MGE.

#### Notas Denegadas

Ao receber o resultado do processamento de um NF-e, a nota pode ter sido DENEGADA. Neste caso, o status da nota é atualizado para DENEGADA e a TOP da nota deve ser trocada pela seguinte regra:

A nova TOP passa a ser a TOP do campo **"Tipo Operação NFe Denegada"**, Aba NF-e/NFC-e/CF-e. Caso o valor desse campo seja **"0"**, então será usado o valor do parâmetro **"TOP para Nota Fiscal Eletrônica Denegada -** **TOPNFEDENEG"**.

![Imagem 15: A nova TOP passa a ser a TOP do campo "Tipo Operação NFe Denegada" , Aba NF-e/NFC-e/CF-e. Caso o valor desse campo seja…](https://ajuda.sankhya.com.br/hc/article_attachments/7647426672151)

Além disso, os itens da nota passam a não atualizar estoque e os financeiros relacionados à nota são removidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Função getFaturasXml

A função **getFaturasXml** serve para configurações do relatório formatado utilizado na impressão do DANFE. Esta é muito útil, pois os dados do financeiro podem ser alterados/atualizados, e se a mesma não for utilizada esses dados modificados são impressos novamente. Com a utilização desta função as informações do financeiro que são buscadas no arquivo.xml que é gerado para o envio e aprovação da SEFAZ e impressas no DANFE, serão sempre estáticas.

**Exemplo sem a variável:** Lançada a nota de venda número 997, com o tipo de negociação parcelado, gerando assim três financeiros com datas de vencimentos distintas. Ao final da transação, o usuário imprime a DANFE para o cliente. Caso sejam alteradas as datas de vencimento das movimentações financeiras, ao imprimir a nota novamente, as informações do financeiro serão impressas com os dados atualizados.

Considerando um DANFE configurado com a nova função **getFaturasXml** para impressão das informações do financeiro, caso o usuário altere as movimentações financeiras geradas pela venda, essas atualizações não refletirão novamente no DANFE, quando impresso.

![Imagem 16: Considerando um DANFE configurado com a nova função getFaturasXml para impressão das informações do financeiro, caso o…](https://ajuda.sankhya.com.br/hc/article_attachments/7267928762775)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Notas Marcadas como Pendente de Retorno

![Imagem 17: Notas Marcadas como Pendente de Retorno](https://ajuda.sankhya.com.br/hc/article_attachments/7647291175063)

Uma nota pode ser marcada com pendente de retorno por meio do botão **"NF-e"** nos Portais. Para ser marcada, a nota deve ter o status **"Aguardando autorização"**. Ao ser marcada, a nota é duplicada com todas as suas informações. A nota original é marcada como **"Não Enviada"** tem seus campos de NF-e anulados. A nova nota é marcada como **"Pendente de Retorno"**.

A sua TOP é trocada pela seguinte regra:

A nova TOP é buscada pelo campo Top para NFe Pendente de Retorno, Aba Impressão da TOP original. Se o valor desse campo é zero, então é usado o valor do parâmetro TOP para NFe pendente de retorno - TOPNFEPENRET.

#### Processo

- Ambas as TOPs configuradas nos parâmetros ou na TOP de origem não devem atualizar nem financeiro e nem estoque, porém com relação as CFOP'S e atualização dos livros, devem ser analisados pelo contador da empresa.
- Este processo serve para casos de contingência, quando a SEFAZ Web service está sem serviço (NF-e já foi encaminhada para a SEFAZ e estava aguardando a autorização).

#### Solução Processual

- Aguardar restabelecer a comunicação ou passar as NFes já encaminhadas para pendente de retorno.
- Selecionar a(s) NF-e e clicar no Botão Outras opções->Nota Fiscal Eletrônica->Marcar Nota como Pendente de Retorno.
- O sistema irá gerar uma nova NF-e com o Status NF-e igual a Pendente de Retorno idêntica a NF-e que estava Aguardando Autorização;
- O sistema passará a nota que estava Aguardando Autorização para o Status NF-e igual a Não Enviada;
- Após restabelecer a comunicação com a SEFAZ, realizar a tratativa das NF-e Pendente de Retorno, conforme Manual de Contingência do Governo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## NF-e Pronta Entrega

Automatização do envio e consulta do resultado das NF-e à SEFAZ, cálculo de PIS/COFINS e geração da Chave NF-e das notas originadas do LMMS (Landix).

**Observação:** para o funcionamento da NF-e, o NF-e Pronta Entrega necessita da correta configuração para emissão de NF-e (Empresa, TOP, Produto... etc.).

Como premissa, para o funcionamento da rotina de cálculo de impostos acontecer as alíquotas de PIS e COFINS deverão estar configuradas.

Veja documentação completa das configurações necessárias para a emissão da Nota Fiscal Eletrônica, no Manual da NF-e disponível na área restrita do site Sankhya e\ou no Help On Line do sistema Sankhya.

![Imagem 18: Veja documentação completa das configurações necessárias para a emissão da Nota Fiscal Eletrônica, no Manual da NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/7267931613591)

1. O PDA (Assistente Pessoal Digital (Palm, Pocket)) descarrega a negociação e junto envia uma solicitação de autorização de NF-e.
2. A descarga é feita através da internet e é recebida pelo LMMS (Landix Mobile Middleware Server).
3. O LMMS aciona o Middleware para processar a negociação e a solicitação de autorização de NF-e.
4. O Middleware grava a negociação com o estado "confirmada" nas tabelas do Mitra e grava um registro na tabela de integração para enfileirar as solicitações de autorização de NF-e.
5. O Mitra indica para o Middleware o NUNOTA referente à negociação gravada.
6. O Middleware devolve ao LMMS o NUNOTA referente à negociação gravada no Mitra.
7. O LMMS envia através da internet o NUNOTA referente à negociação descarregada.
8. O PDA recebe NUNOTA para futuramente verificar se a NF-e foi autorizada e assim concretizar a venda.
9. De tempo em tempo um agendador da Sankhya (integrado com o web service da Sankhya que se comunica com o web service da Sefaz) verifica na tabela de integração se há solicitações de NF-e e monta um pacote com todas as solicitações de NF-e, que ainda não foram enviadas à SEFAZ.
10. O agendador envia através da internet o pacote com notas que necessitam de autorização da SEFAZ.
11. A SEFAZ recebe as solicitações de autorização de NF-e.
12. A SEFAZ devolve o protocolo de recebimento de solicitação.
13. O agendador recebe o protocolo de recebimento da SEFAZ.
14. O agendador grava no banco de dados do Mitra o protocolo de recebimento das solicitações que foram recebidas.
15. De tempo em tempo o agendador verifica no banco de dados e monta um pacote com as solicitações que já foram enviadas para a SEFAZ e estão aguardando a resposta sobre a autorização.
16. O agendador envia o pacote à SEFAZ para verificar se as notas foram autorizadas.
17. A SEFAZ recebe o pacote e verifica se as solicitações de NF-e indicadas no pacote foram autorizadas.
18. A SEFAZ monta um pacote indicando as solicitações de NF-e que foram aprovadas e indicando o código de autorização de cada NF-e.
19. O agendador recebe o pacote com as solicitações autorizadas e os códigos de autorização da NF-e.
20. O agendador grava no banco de dados do Mitra a marcação das notas que foram autorizadas e os códigos das NF-e autorizadas.
21. O PDA descarrega as notas que estão aguardando autorização da SEFAZ e junto envia a solicitação de verificação de NF-e aprovada.
22. A descarga é feita através da internet e é recebida pelo LMMS (Landix Mobile Middleware Server).
23. O LMMS aciona o Middleware para verificar se as notas descarregadas foram autorizadas.
24. O Middleware conecta ao banco de dados do Mitra e verifica quais notas já foram autorizadas pela SEFAZ.
25. O Middleware copia do banco do Mitra os XML das notas que foram autorizadas.
26. O Middleware monta um envelope onde são armazenados todos os XML copiados do banco do Mitra e disponibiliza o envelope para o LMMS.
27. O LMMS envia através da internet, o envelope com as XML das NF-e.
28. O PDA recebe o envelope, identifica através dos XML as notas que foram autorizadas.
29. O PDA interpreta o XML, monta o arquivo de DANFE simplificado e envia para impressora.
30. A impressora imprime o DANFE simplificado.

O NFE pronta entrega visa automatização do envio e consulta do resultado das NF-e à SEFAZ, cálculo de PIS/COFINS e geração da Chave NF-e das notas originadas do LMMS (Landix).

Ao entrar no sistema, o mesmo solicita o **"Intervalo de Execução"** para processamento (segundos entre as execuções) e a base que será executada a rotina.

A Sankhya recomenda que o usuário estipule um intervalo mínimo de 15 segundos.

As rotinas abrangentes nesse executável são:

- Cálculo de impostos;
- Montar Chave NF-e (Notas Modelo 1 ou 1A, a responsabilidade da Chave NF-e é do LMMS ( Landix ));
- Enviar solicitação à SEFAZ;
- Consultar resultado na SEFAZ.

Todo o funcionamento do módulo é baseado na tabela TGFPEL, onde serão inseridos os registros: Nota Fiscal (Modelo 1 ou 1A), Nota Fiscal Eletrônica, Cancelamento de NF-e e FS-DA (Contingência).

Como se trata de Pronta Entrega, o recolhimento do ST é sempre na entrada do item.

Processos para cada movimentação:

- **Nota Fiscal (Modelo 1 ou 1A):** Nesta modalidade, as notas não tem obrigatoriedade de envio à SEFAZ. Então o sistema verifica os registros modelo 1 ou 1A, realiza apenas o cálculo de PIS/COFINS e avisa ao PDA que a nota está pronta para ser impressa.
- **Nota Fiscal Eletrônica:** Essas notas têm obrigatoriedade de envio à SEFAZ. O sistema verifica os registros cujo modelo seja NF-e e realiza o cálculo de PIS/COFINS. Após os cálculos de PIS/COFINS, o sistema envia as notas à SEFAZ em busca de autorização das mesmas. Na próxima etapa, o sistema realiza a consulta para verificar se a NF-e foi Aprovada, Rejeitada ou Denegada. Ao receber o resultado da consulta, o sistema avisa ao PDA se a nota está pronta para ser impressa (DANFE), se a NF-e precisa de alguma correção (Rejeição) ou se a NF-e foi inutilizada (Denegada).
- **Cancelamento de NF-e:** Para o cancelamento de NF-e. A solicitação de cancelamento tem a obrigatoriedade de envio à SEFAZ. O sistema solicita o cancelamento de determinada NF-e e após o retorno da SEFAZ, o sistema desfaz o financeiro e o estoque envolvido, na NF-e cancelada.
- **Emissão FS-DA:** tipEmiss = 5 (Contingência) Formulário de Segurança – Documento Auxiliar. Esta contingência é específica para usuários de Pronta Entrega, que por algum motivo (seja por falta de Internet, SEFAZ fora do ar, etc.) não conseguiram emitir a NF-e. Neste caso, é emitida a contingência FS-DA, com impressão do DANFE em formulário de segurança. O FS-DA é emitido e o PALM preenche a tabela de integração com os dados referente ao FS-DA emitido. No momento em que a situação for regularizada (conexão à Internet ou SEFAZ volte a funcionar), o FS-DA será enviado para a SEFAZ.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

## Parâmetros que influenciam na NF-e

**Enviar tags CSRT de NF-e em homologação - ENVTAGCSRTHOM:** Quando este parâmetro estiver habilitado e o ambiente da NF-e for Homologação, as tags idCSRT e hashCSRT do grupo infRespTec serão geradas com os valores fixos para que a nota não seja rejeitada com **"975 - Rejeicao: Obrigatoria a informacao do identificador do CSRT e do Hash do CSRT"**.

**Importante:** este parâmetro só deve ser utilizado no ambiente de homolagação do Mato Grosso, caso seja exigido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica#top)

![Imagem 19: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16533477369751) Acesse também:

[Configurações para Nota Fiscal Eletrônica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601734-Configura%C3%A7%C3%B5es-para-Nota-Fiscal-Eletr%C3%B4nica)
