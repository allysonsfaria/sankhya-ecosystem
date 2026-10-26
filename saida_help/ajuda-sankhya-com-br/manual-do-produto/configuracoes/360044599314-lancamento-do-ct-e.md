---
id: "360044599314"
titulo: "Lançamento do CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:44Z"
rotulos: ["CT-e", "Lançamento", "Veículo", "Configuração", "Portal de Vendas", "Destinatário", "Remetente", "XML", "Redespacho", "Transporte", "Consignatário", "Expedidor", "Lotação", "Reboque", "Recebedor", "Tração", "Lançamento do CT-e manual", "Documentos Eletrônicos"]
---

# Lançamento do CT-e

Este tópico destina-se à apresentação das informações acerca do lançamento de um Conhecimento de Transporte Eletrônico - CT-e.

| Funcionalidades |
| --- |
| [Considerações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#consideraesiniciais) |
| [Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#gradecabealho) |
| [Grade Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#gradeitens) |
| [Grade Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#graderodap) |
| [Portal de Vendas - CT-e em Desacordo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#portaldevendas-ct-eemdesacordo) |
| [Observações importantes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#observaesimportantes) |

## Considerações iniciais

O procedimento de lançamento do CT-e, possui algumas particularidades se comparado ao lançamento de uma NF-e comum. Ele se desenvolve no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), onde você deverá selecionar no lado esquerdo da tela, o Tipo de Movimento **"Conhecimento de transporte"**.

![Imagem 1: O procedimento de lançamento do CT-e, possui algumas particularidades se comparado ao lançamento de uma NF-e comum. Ele…](https://ajuda.sankhya.com.br/hc/article_attachments/9449805841943)

Escolhendo-se o Tipo de Movimento Conhecimento de transporte, e acionando o botão **"+Novo"** para inserção de um novo documento, será realizado o direcionamento para a tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas) carregando-se o layout já configurado, de acordo com a orientação no tópico [Configuração do Layout da Nota - DACTE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599454-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE).

![Imagem 2: Escolhendo-se o Tipo de Movimento Conhecimento de transporte , e acionando o botão "+Novo" para inserção de um novo…](https://ajuda.sankhya.com.br/hc/article_attachments/9449906595351)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Grade Cabeçalho

![Imagem 3: Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/article_attachments/9449988373783)

Ao dar início ao lançamento de um CT-e, você deverá preencher os dados do cabeçalho do documento, nos quais pode-se destacar os seguintes:

No campo **"Empresa"** você informará a empresa cadastrada no sistema como **"Transportadora"**.

Preencha no campo **"Parceiro"** com o parceiro que será o tomador do serviço de transporte.

No campo **"Parceiro Remetente"** informe o parceiro remetente do CT-e, ou seja, o parceiro que emitiu as notas fiscais referentes aos produtos que a transportadora está deslocando.

Você irá inserir no campo **"Parceiro Destinatário"** o parceiro destinatário do CT-e, ou seja, o parceiro que receberá as mercadorias remetidas pelo parceiro remetente.

**Observação:** pode-se definir as cidades de Origem e Destino do CT-e no ato de sua emissão; para tal, por meio dos campos **"Cód. Cid. Início CT-e"** e **"Cód. Cid. Fim CT-e"**, acrescenta-se estes dados no documento que está sendo emitido, de modo que não será necessário informar o Parceiro de Coleta. Estes campos devem ser incluídos no layout da nota, através da configuração feita previamente na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota). No caso de lançamento de CT-e de Terceiros, estas informações devem ser obrigatoriamente preenchidas.

**Importante:** caso o CT-e seja de terceiros (em que o [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de Compra tenha o campo CT-e definido como Terceiros ([aba Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso)) e o Modelo do Documento seja de Conhecimento de Transporte ([aba Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal))), o sistema irá validar o preenchimento de ambos os campos Cód. Cid. Início CT-e e/ou Cód. Cid. Fim CT-e. Porém, caso seja um CT-e de terceiros, mas o campo CT-e mencionado esteja definido com um valor diferente de Terceiros, o sistema irá validar somente o preenchimento do Cód. Cid. Início CT-e e/ou Cód. Cid. Fim CT-e. Essa exigência é necessária somente para documentos que possuem sua data igual ou maior à 01/01/2018.

Insira no campo **"Consignatário (Expedidor)"** o expedidor da mercadoria do CT-e anterior. Você deverá preencher este campo apenas quando o CT-e possuir o Tipo de Serviço **"Redespacho"** ou **"Redespacho intermediário"**.

Preencha o campo **"Redespacho (Recebedor)"** com o recebedor da mercadoria do CT-e anterior. Este campo deverá ser preenchido apenas quando o CT-e possuir o Tipo de Serviço Redespacho intermediário.

Informe no campo **"Tipo Operação"** o Tipo de Operação que caracteriza a emissão do documento, considerando o tipo de CT-e e o Tipo do Serviço do mesmo.

Você informará no campo **"Tipo Negociação"** o Tipo de Negociação que irá gerar a(s) parcela(s) do financeiro; isto apenas quando a TOP informada no campo anterior estiver configurada para atualizar o financeiro.

Preencha o campo **"Série da nota"** com a série do documento.

No campo **"Produto predominante"** informe o produto predominante no CT-e, ou seja, a descrição que identifique a mercadoria que está sendo transportada.

Você deverá selecionar a marcação **"Lotação"** somente quando o CT-e caracterizar uma lotação; esta pode ser caracterizada pelo fato de que a mercadoria transportada ocupa todo o espaço do veículo, ou seja, a entrega será realizada somente para um destinatário; caso o transporte não possua essa condição, este campo deverá permanecer desmarcado.

**Observação:** quando a marcação Lotação estiver habilitada, obrigatoriamente você deverá informar o motorista e o veículo, caso contrário, será apresentada a seguinte mensagem:

**"Para CT-e de lotação, ao menos um motorista e o veículo e seus reboques (caso haja) devem ser informados".**

Informe no campo **"Veículo de Tração"** o veículo de tração que realizará o transporte da mercadoria.

Caso o veículo possua reboque, você deverá informá-lo nos campos **"Reboque 1"**, **"Reboque 2"** e **"Reboque 3"**.

Preencha no campo **"Previsão de entrega"** a data prevista da entrega da mercadoria ao destinatário.

Os campos relacionados ao veículo e seus reboques determinarão, automaticamente, se o veículo é de tração ou reboque, isso a partir do campo em que for lançado o dado do veículo.

No lançamento de um CT-e, será possível determinar através do campo **"Forma de Pagamento do CT-e"** como se dará a quitação do documento, dentre as seguintes opções:

- A pagar;
- Pago;
- Outros.

A informação contida neste campo, alimentará a tag **<forPag>** do XML do CT-e. Caso este campo esteja em branco, será considerada a informação presente no campo **"CIF / FOB"** localizado também no cabeçalho da nota, para o preenchimento da referida tag. Para que ambos os campos, Forma de Pagamento do CT-e e CIF / FOB sejam apresentados no cabeçalho da nota, é necessário que eles sejam previamente incluídos no layout da nota, por meio da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

**Importante:** na emissão do CT-e existem alguns casos em que a transportadora precisa gerar determinadas informações nos campos **<ObsCont xCampo=>** e **<xTexto>**; no parâmetro **"Consulta para informação adicional no XML do CTe - QUEINFADCXMLCTE"** pode-se informar uma query para preenchimento destes campos. Consideremos um exemplo de query:

**SELECT OBSERVACAO as XCAMPO, PLACA as XTEXTO FROM TGFCAB WHERE NUNOTA = :NUNOTA**

Quando você lançar um CT-e e preencher os campos Observação e Placa, essas informações serão carregadas no XML e no DACTE do CT-e. O XML será construído com a seguinte configuração:

**<**compl>

  <xObs>CTe importante</xObs>

  <ObsCont> xCampo="CTe importante">

    <xTexto>HEO2144</xTexto>

  </ObsCont>

</compl**>**

**Observação:** na emissão do CT-e, a respeito da tag **<indIEToma>** tem-se as seguintes considerações:

- No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), [aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal), caso você defina o campo Classificação ICMS como **"Consumidor Final Não Contribuinte"** e/ou o parceiro seja do exterior (o que caracteriza um parceiro do exterior é na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo) de seu cadastro constar um endereço do exterior e na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), o CNPJ 00000000000000), no XML do CT-e, a tag **<indIEToma>** será alimentada com o valor **"9"**. No caso do Parceiro ser estrangeiro, no XML não tem-se a sua Inscrição Estadual;
- Para um tomador do serviço Consumidor Final, seu indicador será igual a 9 (tag **<indIEToma>**) e sua Inscrição Estadual será gerada, caso esteja preenchida;
- Se tratando de um tomador Pessoa Física, cuja configuração do campo Classificação ICMS esteja definido como Consumidor Final Não Contribuinte, no XML do CT-e, a tag **<indIEToma>** não será gerada;
- Quando o parceiro tomador não é do exterior, não está configurado como Consumidor Final Não Contribuinte, a sua Inscrição Estadual está definida como Isento e a UF do parceiro está configurada no parâmetro **"UF que não aceita tomador isento no CT-e emitido - UFTOMAISENTOCTE"**, a tag **<indIEToma>** será alimentada com o valor **"2"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Grade Itens

![Imagem 4: Grade Itens](https://ajuda.sankhya.com.br/hc/article_attachments/9450030358295)

Na parte destinada aos itens da nota, você informará quais os serviços prestados, sendo que, cada serviço deve possuir um componente de serviços. Neste caso, ao gerar o lote do CT-e, o sistema agrupará o valor dos serviços que possuem o mesmo componente e no CT-e será feito o destaque por componente.

Caso você informe algum serviço sem componente cadastrado, será apresentada a seguinte mensagem de validação:

**"O serviço (xxx) lançado não possui componente cadastrado. Favor definir algum componente para este serviço".**

Quando você informar serviços que possuem CST, Alíquotas de ICMS, Percentual de Redução de Base ou CFOP diferentes entre si, também será apresentada uma mensagem de validação, sendo esta apresentada no momento da geração do lote do documento:

**"Verifique a tributação dos componentes do serviço (serviços) do CT-e! Para confirmação do CT-e é necessário que a tributação (CST), a alíquota de ICMS, percentual de redução de base e CFOP, sejam os mesmos."**

Estas informações deverão ser as mesmas de todos os serviços lançados; por mais que exista a divisão de componentes de serviço, a prestação de serviço de transporte é apenas uma.

**Validação Reforma Tributária (IBS/CBS):** com as adequações da Reforma Tributária, o leiaute do CT-e passou a permitir apenas um único grupo de tributação de IBS e CBS por Componente do Valor da Prestação. Portanto, no momento da confirmação do CT-e, o sistema validará se todos os itens associados a um mesmo componente possuem tributação estritamente homogênea. Caso exista divergência de **CST, Classificação Tributária (cClassTrib), Alíquota de IBS, Alíquota de CBS ou Percentual de redução de base** entre itens do mesmo componente, o sistema bloqueará a emissão exibindo o erro **CORE\_E04421**.

Ressaltamos que o sistema não está preparado para gerar o lote do CT-e que possua na nota itens com a tributação igual a:

- 010 – Tributada e c/ cobrança por substituição;
- 030 – Isenta e não tribut. e c/ cobrança por subst.;
- 050 – Suspensão;
- 060 – ICMS cobrado anteriormente por substituição;
- 070 – Com redução de base e c/ cobrança por subst.;
- 090 – Outros.

Caso os itens (serviços/componentes de serviço) possuam alguma das tributações acima mencionadas, a Receita irá rejeitar o lote do CT-e com a mensagem informando que o conteúdo do campo "ICMS" não é válido.

Nota: se na emissão do CT-e a prestadora do serviço não for situada no local de origem do transporte, ocorrerá a conversão da CFOP que se dará de acordo com a seguinte regra: Quando o tipo do CT-e for Normal, [Complementar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596894-Aprova%C3%A7%C3%A3o-do-CT-e) ou [Substituição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596894-Aprova%C3%A7%C3%A3o-do-CT-e#ct-edesubstituio), se a UF emitente for diferente da UF de início da prestação, e se a UF de início e fim da prestação não forem estrangeiras (EX - Exterior):

- Se a UF de início e fim da prestação forem iguais, o CFOP será convertido automaticamente para **"5932 - Prestação de** **serviço de transporte iniciada em unidade da Federação diversa daquela onde inscrito o prestador"**.
- Se a UF de início e fim da prestação forem diferentes, o CFOP será automaticamente convertido para **"6932 - Prestação de serviço de transporte iniciada em unidade da Federação diversa daquela onde inscrito o prestador"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Grade Rodapé

A grade Rodapé é completamente habilitada para utilização, logo após o salvamento dos dados na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#gradeitens). Algumas informações serão geradas automaticamente e poderão ser modificadas, caso necessário; enquanto que outros dados deverão ser manualmente informados. Ela é composta por 10 (dez) abas. Analisemos sobre cada uma delas:

| [Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abaimpostos) |
| --- |
| [Aba Unidades de Medida](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abaunidadesdemedida) |
| [Aba Notas do Conhecimento de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abanotasdoconhecimentodetransporte) |
| [Aba Seguros de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abasegurosdetransporte) |
| [Aba Motorista](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abamotorista) |
| [Aba Documentos Anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abadocumentosanteriores) |
| [Aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abafinanceiro) |
| [Aba Coleta/Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abacoletaentrega) |
| [Aba Vale Pedágio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abavalepedgio) |
| [Aba Lacres](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abalacre) |
| [Aba Informações da GTV-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#AbaInforma%C3%A7%C3%B5esdaGTV-e) |

## Aba Impostos

Com base nas configurações de impostos anteriormente realizadas para cada [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389093-Produtos-), considerando ainda a localização da [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025387933-Empresas) e [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232674-Parceiros), tem-se os dados da aba Impostos. Configurações como a geração de [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596434-Al%C3%ADquotas-de-ICMS), [ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS) e [IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601134-Al%C3%ADquotas-de-IPI), e suas respectivas alíquotas por exemplo, são essenciais para alimentação desta aba. Além disso, tem-se os dados a respeito do CT-e lançado, bem como sua Chave, seu Tipo de emissão, o Ambiente de lançamento etc.

![Imagem 5: Com base nas configurações de impostos anteriormente realizadas para cada Produto , considerando ainda a localização da…](https://ajuda.sankhya.com.br/hc/article_attachments/9450087756439)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Unidades de Medida

![Imagem 6: Aba Unidades de Medida](https://ajuda.sankhya.com.br/hc/article_attachments/9450091930263)

Nesta aba, obrigatoriamente, você deverá informar quais as unidades de medida das mercadorias em transporte. Um mesmo documento pode possuir mais de uma unidade de medida.

No campo **"Tipo da Medida"** realiza-se o preenchimento do tipo da medida, que não necessariamente trata-se da unidade de medida propriamente dita. Por exemplo, no caso da Unidade de Medida ser **"KG"** o Tipo da Medida pode ser **"Peso Bruto"**.

Informe no campo **"Quantidade na medida"** a quantidade de mercadoria que possui a unidade de medida selecionada.

Selecione no campo **"Unidade de Medida"** a unidade de medida das mercadorias. Neste, você poderá definir uma das seguintes opções:

- M3;
- KG;
- TON;
- UNIDADE;
- LITROS;
- MMBTU.

As informações referentes à unidade de medida são obrigatórias para emissão do CT-e. Caso estes dados não sejam informados, será apresentada a seguinte mensagem no momento da confirmação do documento:

**"É necessário informar a(s) unidade(s) de carga na aba Unidades de Medida."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Notas do Conhecimento de Transporte

![Imagem 7: Aba Notas do Conhecimento de Transporte](https://ajuda.sankhya.com.br/hc/article_attachments/9450146081303)

Nesta aba, obrigatoriamente, você deverá informar as notas que pertencem ao conhecimento de transporte. É importante ressaltar que, quando informada mais de uma nota, estas devem possuir o mesmo emitente (remetente) e destinatário.

Pode-se informar nesta aba, as notas fiscais que possuam o modelo de documento fiscal **"1"** **(Nota Fiscal Convencional)**, ou o modelo de documento **"55"** **(Nota Fiscal Eletrônica)**. Existem ainda, casos em que a mercadoria transportada não exige nota fiscal, como é o caso, por exemplo, do transporte de materiais biológicos, transporte de móveis em uma mudança de residência etc. Por este motivo, é possível que sejam vinculados ao CT-e outros documentos, como um Documento de Declaração (00), ou um documento caracterizado como Outros (99); no [DACTE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599454-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE), estas informações são impressas no campo TP DOC.

Para cada modelo de documento, são considerados um conjunto de campos, os quais devem ser preenchidos.

- Para o modelo de documento fiscal **"1"**, os seguintes campos devem ser informados:

**Número:** Informa-se o número da nota fiscal.

**Dh. emissão:** Preenche-se a data e hora da emissão da nota fiscal.

**Série:** Informa-se a série da nota fiscal.

**Valor da nota:** Este campo destina-se ao preenchimento do valor da nota fiscal.

**Modelo Documento:** Se tratando de notas no modelo convencional, informa-se neste caso o modelo de documento igual a **"1"**.

**Base ICMS:** Informa-se aqui, o valor da base de cálculo do ICMS da nota fiscal. Caso não exista, informa-se o valor 0,00.

**Valor ICMS:** Preenche-se aqui, o valor do ICMS da nota fiscal. Caso não exista, informa-se o valor 0,00.

**Base Substit.:** Informa-se aqui, o valor da base de cálculo do ICMS ST da nota fiscal. Caso não exista, informa-se o valor 0,00.

**Valor Substit.:** Preenche-se este campo com o valor do ICMS ST da nota fiscal. Caso não exista, informa-se o valor 0,00.

**Valor Total dos Produtos:** Este campo deve ser preenchido com o valor total dos produtos da nota fiscal.

**CFOP:** Informa-se neste campo, qual a CFOP predominante da nota fiscal.

- No caso do modelo de documento fiscal **"55"**, deve-se preencher os seguintes campos:

**Número:** Informa-se o número da NF-e.

**Dh. emissão:** Preenche-se a data e hora da emissão da NF-e.

**Série:** Informa-se a série da NF-e.

**Valor da nota:** Este campo destina-se ao preenchimento do valor da NF-e.

**Modelo Documento:** Como se tratam de Notas Fiscais Eletrônicas, informa-se neste campo, o modelo de documento fiscal **"55"**.

**Chave NF-e:** Informa-se neste campo, a chave de acesso da NF-e.

**Observação:** não se deve inserir em um mesmo CT-e notas fiscais de modelos de documento diferentes, ou seja, um CT-e não pode conter uma **"Nota Fiscal Convencional"** e outra **"Nota Fiscal Eletrônica"**.

Caso os dados nesta aba não sejam preenchidos, o sistema irá apresentar a seguinte mensagem na confirmação:

**"É necessário informar ao menos um tipo de documento a ser transportado na aba Notas de Conhecimento de Transporte".**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Seguros de Transporte

![Imagem 8: Aba Seguros de Transporte](https://ajuda.sankhya.com.br/hc/article_attachments/9450188113687)

Nesta aba você fará o registro das informações relacionadas ao Seguro de Transporte. Em um único CT-e, pode-se ter mais de um responsável pelo seguro da carga. Para esta configuração, tem-se os seguintes campos:

No campo **"Responsável pelo Seguro"** você definirá quem é o responsável pelo seguro da carga, com as seguintes opções de escolha:

- Emitente do CT-e;
- Remetente;
- Tomador de Serviço;
- Destinatário.

Informe o nome da seguradora que irá acobertar o seguro da carga transportada no campo **"Nome da Seguradora"**.

O campo **"Nro. Apólice"** é destinado ao número da apólice de seguro feita pela seguradora que está acobertando o seguro da carga.

Você informará no campo **"Nro. Aberbação"** o valor da carga; este deve ser preenchido apenas se o valor da carga acobertada for diferente do somatório do valor total das notas fiscais informadas na aba **"Notas do Conhecimento de Transporte"**. Caso não seja necessário preenchê-lo, o sistema irá considerar o valor da carga como sendo o somatório do valor total das notas fiscais transportadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Motorista

![Imagem 9: Aba Motorista](https://ajuda.sankhya.com.br/hc/article_attachments/9450206596759)

Nesta aba, você poderá informar o motorista que realizará o transporte da carga. Em um mesmo CT-e pode-se ter mais de um motorista, podendo-se com isso, nesta aba, informar um ou mais motoristas.

Informe aqui qual é o parceiro correspondente ao motorista. Serão aceitos somente lançamentos de parceiros que estão identificados como **"Motorista"** em seu cadastro ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), campo Tipo).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Documentos Anteriores

![Imagem 10: Aba Documentos Anteriores](https://ajuda.sankhya.com.br/hc/article_attachments/9450232932759)

Você preencherá esta aba com os documentos anteriores, quando o CT-e emitido possuir o tipo de serviço **"Redespacho"**, **"Redespacho Intermediário"** ou **"Subcontratação"**.

O documento anterior consiste em informar qual ou quais CT-e's foram emitidos antes do que está sendo gerado no momento. No caso dos tipos de serviço acima citados, obrigatoriamente, deve-se possuir ao menos um documento anterior informado. Para completo preenchimento desta aba, informa-se os seguintes campos:

**Parceiro Emissor do Documento:** Informa-se aqui, o parceiro que emitiu o documento anterior ao que está sendo inserido.

**Chave de acesso (doc. anterior):** Preenche-se este campo com a chave de acesso do documento anteriormente emitido pelo parceiro informado no campo **"Parceiro Emissor do Documento"**.

Caso esteja-se utilizando um Tipo de Operação caracterizado com o serviço Redespacho, Redespacho Intermediário ou Subcontratação, e no mínimo um documento anterior não tiver sido informado nesta aba, o sistema irá exibir um alerta com as seguintes informações:

**"Para CT-e de Redespacho, Redespacho Intermediário ou Subcontratação, o(s) documento(s) anterior(es) deve(m) ser informado(s)."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Financeiro

Nesta aba, são apresentados os dados do financeiro do documento, de acordo com as configurações definidas essencialmente nos [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) e consequentemente no [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113513-Tipo-de-Negocia%C3%A7%C3%A3o).

![Imagem 11: Nesta aba, são apresentados os dados do financeiro do documento, de acordo com as configurações definidas…](https://ajuda.sankhya.com.br/hc/article_attachments/9450236619159)

Esta aba possui também dois botões para realização de algumas modificações, caso necessário. São eles:

![Imagem 12: Parcelar com Vários Tipos de Títulos e Alterar Parcelas](https://ajuda.sankhya.com.br/hc/article_attachments/9450308570391)[Parcelar com Vários Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025393853-Parcelar-com-V%C3%A1rios-Tipos-de-T%C3%ADtulos)        e         ![Imagem 13: Parcelar com Vários Tipos de Títulos e Alterar Parcelas](https://ajuda.sankhya.com.br/hc/article_attachments/9450346407959)[Alterar Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238194-Alterar-Parcelas)

**Observação:** os campos texto apresentados nesta aba podem ter sua apresentação influenciada pelo parâmetro **"Usa text area grande no financeiro?- USABIGTEXTAREA"** que, ao ser ativado, exibirá os campos em tamanho grande na aba; desligando-se o parâmetro, os campos serão exibidos em tamanho pequeno. Qualquer campo adicional do tipo texto que possua a forma de apresentação igual a caixa de texto, será exibido de acordo com a definição feita no referido parâmetro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Coleta/Entrega

![Imagem 14: Aba Coleta/Entrega](https://ajuda.sankhya.com.br/hc/article_attachments/9450554297111)

Informe nesta aba os dados referentes à coleta ou entrega diferentes do endereço de origem e destino do CT-e, se assim a empresa desejar.

Para cada tipo de CT-e, existe uma origem e destino a serem considerados para os cálculos de impostos e CFOP:

#### Tipo do CT-e normal ou subcontratação:

- **Origem:** Parceiro Remetente
- **Destino:** Parceiro Destinatário

#### Tipo do CT-e redespacho:

- **Origem:** Parceiro Expedidor
- **Destino:** Parceiro Destinatário

#### Tipo do CT-e redespacho intermediário:

- **Origem:** Parceiro Expedidor
- **Destino:** Parceiro Recebedor

Além disso, nesta aba, você poderá realizar o preenchimento dos seguintes dados:

**Tipo:** Informe aqui se o tipo será destinado a caracterizar uma **"Coleta"** ou **"Entrega"**.

**Tipo transporte:** Defina qual o tipo de transporte que será realizada a coleta ou entrega. O sistema atualmente atende apenas o modal **"Rodoviário"**.

**Cód. Parceiro:** Neste campo você informará o parceiro a ser considerado para realizar a coleta ou entrega. Nesta situação, o endereço de coleta ou entrega será o endereço do parceiro informado.

Caso nenhuma informação seja inserida neste campo relacionada à coleta ou entrega, para a emissão do CT-e o sistema irá considerar o endereço do **"Parceiro Remetente"** como **"Coleta"** e o endereço do **"Parceiro Destinatário"** como **"Entrega"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Vale Pedágio

![Imagem 15: Aba Vale Pedágio](https://ajuda.sankhya.com.br/hc/article_attachments/9450580360599)

Cada transportadora possui uma forma de calcular o pedágio da rota a ser seguida, que pode ser optando por calcular seu valor e adquirindo o mesmo junto à fornecedora, destacando o vale-pedágio no CT-e. Normalmente, a transportadora possui um cadastro junto à fornecedora do pedágio, e o cadastro de rotas e veículos, para que a partir dessas informações a fornecedora indique qual o valor do pedágio por eixo, considerando a rota e o veículo.

Assim, a transportadora compra o pedágio, a fornecedora passa a ela o número da aquisição do pedágio e o valor. Com posse desses dados, a transportadora aponta as mesmas na emissão do CT-e. Estas informações são inseridas nesta aba. A saber:

No campo **"Pagante do Pedágio"** você determinará quem é o pagante do pedágio, dentre as seguintes opções:

- Emitente do CT-e;
- Remetente;
- Destinatário;
- Expedidor;
- Recebedor;
- Outro.

Informe no campo **"Nro. Compra"** a numeração do comprovante da compra do vale pedágio.

Você deverá preencher o campo **"Parceiro Pagante"** com o parceiro pagante do pedágio, quando o campo anterior estiver definido com a opção Outro.

No campo **"Parceiro Fornecedor"** informe o parceiro fornecedor do pedágio.

**Nota:** quando o Parceiro Pagante do Pedágio for definido como **"Outro"**, será feita a validação pelo sistema se o pagante está devidamente informado. Caso não esteja, será apresentada uma mensagem alertando sobre o ocorrido:

**"Parceiro Pagante do Vale Pedágio não informado."**

O mesmo vale para os outros atores do CT-e, ou seja, caso você defina o referido campo como Destinatário, Emitente ou Remetente e não informe este código do Parceiro no cabeçalho do CT-e, será apresentada uma mensagem semelhante à retratada acima.

O campo **"Valor do Pedágio"** é destinado ao preenchimento do valor correspondente ao vale pedágio.

As informações pertinentes à esta aba, serão geradas no XML do CT-e da seguinte maneira:

**<**valePed>

  <CNPJForn>81777325000104</CNPJForn>

  <nCompra>3557</nCompra>

  <CNPJPg>02245571000107</CNPJPg>

  <vValePed>0.00</vValePed>

</valePed**>**

Além das informações geradas no XML, estas serão impressas no [DACTE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237274-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE) somente se existir lotação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Lacres

![Imagem 16: Aba Lacres](https://ajuda.sankhya.com.br/hc/article_attachments/9450633878551)

Nos casos de transporte de combustível, é preciso que se tenha o lacre destacado no CT-e. Normalmente, o remetente aponta o Número do Lacre na nota fiscal. De posse da Nota Fiscal, o operador aponta o número do lacre no momento da emissão do CT-e; poderão ser informados apenas os lacres correspondentes às mercadorias presentes no transporte daquele CT-e a ser emitido.

Com os dados desta aba preenchidos, estas serão geradas no XML do CT-e da seguinte maneira:

**<**lacRodo>

  <nLacre>1997</nLacre>

</lacRodo**>**

Essa informação é impressa no [DACTE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237274-Configura%C3%A7%C3%A3o-do-Layout-da-Nota-DACTE) somente quando existe lotação. Além disso, quando tem-se mais de um lacre no CT-e, os mesmos serão separados pelo caractere barra invertida **"\"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Aba Informações da GTV-e

```
             As implementações apresentadas aqui, estarão disponíveis a partir da versão 4.17.
```

Na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), você pode incluir no layout da nota de Conhecimento de Transporte (CT-e), a grade **"Informações da GTV-e"** que considera os campos previstos na NT 2020.002.

![Imagem 17: Na tela Configurador de Layout da Nota , você pode incluir no layout da nota de Conhecimento de Transporte (CT-e), a…](https://ajuda.sankhya.com.br/hc/article_attachments/15605356379671)

Realizada a inclusão da grade, ao acessar a [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e) e emitir um CT-e, a aba estará disponível na grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314#graderodap) para que as informações do GTV-e sejam inseridas manualmente e geradas no XML do CT-e OS.

![Imagem 18: Realizada a inclusão da grade, ao acessar a Central de Vendas e emitir um CT-e, a aba estará disponível na grade Rodapé…](https://ajuda.sankhya.com.br/hc/article_attachments/15605356381335)

Após aprovação do documento fiscal, você poderá conferir no XML as tags correspondentes ao grupo Informações da GTV-e, conforme exemplo abaixo: 

```
<infGTVe>
        <chCTe>52220800914803000151640010000842291849055652</chCTe>
        <Comp>
          <tpComp>1</tpComp>
          <vComp>3000.00</vComp>
        </Comp>
      </infGTVe>
```

**Observação:** selecionando no campo **"Componentes do Valor da GTV-e"** a opção **"6- Outros"**, o campo **"Complemento"** passa a ser de preenchimento obrigatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Portal de Vendas - CT-e em Desacordo

Considere os dados abaixo na utilização da Versão 3.00 do CT-e ([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba CT-e, campo Versão CT-e).

Uma vez lançado o CT-e, no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) tem-se no botão NF-e a opção **"Prestação de serviço de CT-e em desacordo"** que é utilizada em casos de divergências ou contestações a respeito das NF-e's que compõem o CT-e.

![Imagem 19: Uma vez lançado o CT-e, no Portal de Vendas tem-se no botão NF-e a opção "Prestação de serviço de CT-e em desacordo"…](https://ajuda.sankhya.com.br/hc/article_attachments/9450658330775)

A prestação de serviço em desacordo tem como autor o tomador do serviço do CT-e. Ao acionar esta opção, será aberto o pop-up também denominado **"Prestação de serviço de CT-e em desacordo"**, onde você informará a Empresa tomadora do serviço, a Chave do CT-e gerador da aquisição do serviço, a Sequência do evento e, caso necessário, alguma Observação pertinente ao caso. Uma vez preenchidas as devidas informações, proceda com a transmissão do evento.

![Imagem 20: A prestação de serviço em desacordo tem como autor o tomador do serviço do CT-e. Ao acionar esta opção, será aberto o…](https://ajuda.sankhya.com.br/hc/article_attachments/9450663254039)

**Observação:** o campo Sequência por padrão é apresentado preenchido com o número **"1"**; porém, nos casos em que já existir a sequência 1 de evento gerado para a chave de CT-e informada, será possível modificar a sequência de 1 para 2; feito isto, realiza-se a transmissão do evento novamente.

![Imagem 21: Para que esta opção possa ser utilizada, é necessário que a empresa possua em sua licença o produto "30610 - NOTA…](https://ajuda.sankhya.com.br/hc/article_attachments/16636873651095) Para que esta opção possa ser utilizada, é necessário que a empresa possua em sua licença o produto **"30610 - NOTA FISCAL ELETRÔNICA/W"**, pois como mencionado acima, o autor desta demanda é o tomador do serviço do CT-e.

**Atenção Implantantador Sankhya:** A tabela alimentada no banco de dados, caso a transmissão do evento ocorra com sucesso, tem o nome de TGFEPSD.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)

## Observações importantes

Ao faturar um ou mais Pedidos de Venda de modo a ser elaborado um único CT-e, as informações que constituem às abas abaixo serão copiadas do Pedido de Venda para o CT-e gerado:

- [Aba Unidades de medida](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abaunidadesdemedida);
- [Aba Notas do Conhecimento de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abanotasdoconhecimentodetransporte);
- [Aba Seguros do Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abasegurosdetransporte);
- [Aba Motorista](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abamotorista);
- [Aba Documentos Anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abadocumentosanteriores);
- [Aba Vale Pedágio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abavalepedgio);
- [Aba Lacres](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#abalacre).

Considere as informações abaixo, quando na utilização da Versão 3.00 do CT-e ([Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba CT-e, campo Versão CT-e).

- Informe no parâmetro **"UFs que não aceitam tomador contribuinte isento de I.E. - UFNACTOMCONISE"** os estados que não aceitam o lançamento de CT-e, cujo tomador seja contribuinte isento de Inscrição Estadual. Por padrão, este parâmetro já possui as seguintes Unidades Federativas informadas:

**AM, BA, CE, GO, MG, MS, MT, PE, RN, SE, SP.**

- Caso a operação de emissão do CT-e envolva cálculo de substituição tributária (CST 60), e tenha-se nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) emitente (aba [Insc. Estadual Contribuinte ST no Estado Dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abainsc.estadualcontribuintestnoestadodest.)) alguma Inscrição Estadual informada para o estado de destino do CT-e, o campo IEST será gerado com tal Inscrição Estadual no XML do CT-e.
- Na emissão do CT-e é possível informar valor da carga para efeito de averbação, caso haja qualquer acidente que exija averbação de alguma seguradora; esta informação é incluída no campo **"Valor da Carga Para Averbação"** ([Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)), campo este padrão do layout do CT-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314-Lan%C3%A7amento-do-CT-e#top)
