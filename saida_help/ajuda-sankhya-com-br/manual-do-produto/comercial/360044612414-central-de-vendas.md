---
id: "360044612414"
titulo: "Central de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-10-22T13:20:15Z"
rotulos: ["ORDITENS", "AGRUPADANFEBOL", "CALCCUSTOMEDCAF", "EXPEDSENHA", "IMPEXPSEMCONF", "MASCARAPERCDESC", "NOTAADICEMP", "QRYCONSPROD", "MODCALCPRECDIN", "NOMPROCCALCPRE", "ATUALCOMITE", "CALCCOMMARGMIN", "DISDESAUTANTIMP", "FILTCONTPARCV", "PERCDESCFOB", "PERCDESCFOBCAB", "PRESERQTDVOL", "SOMAQTDVOL", "EXCLIBFECSESALV", "AJUSTARBASEDIN", "USADTSAILIVSAI", "ACVENDIAFIXOVCT", "RECVALCONSPROD", "DECVLRDSMBRLOTE", "APLVLRUNITEDIT", "INIBIREVTSTIPI", "AJUSTACSDECMOE", "DISTDESCIMPEMB", "DTNEGSERVCPA", "DEFCAMDUPFINNOT", "FATSOMAPESOM3P", "RETCONTRECMP", "TRANSFDIGQTDVLR", "IGNORAVENDCOMP", "ACEITATEFVENC", "CALAUTOFRETEWMS", "PERDEVNOTACOMPL", "DISDESAUTIMPEMB", "SAIIPISEMDESC", "INCFACPROLIS", "MAXCENTRAIS", "TAXINCCUST", "DESTITGNREIMP", "COPIAOUTRIMPDEV", "ATUALVENDITEM", "VALLOCKITMP; PREVEDTITEPROC", "DECVLRLIQARR", "LIGCACHEMETA; INITNFEREMESSA", "FORCATPROVCONF; IGNORACESPARCF2", "CALINDDESICMSST;USAVLRCTBBASDIN"]
---

# Central de Vendas

```
 Módulo: Comercial > Rotinas
```

---

Na Central de Vendas, serão realizados todos os lançamentos das operações de saída de mercado ou prestação de serviços pela empresa. Será aberta uma tela por meio do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) ao realizar um duplo clique em um um Pedido de venda, Nota de venda, Devolução de venda ou Conhecimento de Transporte já lançado, ou ao solicitar a inclusão de algum destes documentos; notas de saída que foram canceladas, são detalhadamente visualizadas na tela [Notas Canceladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603254).

**Importante:** A Central de Vendas, assim como as demais centrais, poderá ser utilizada com base em um layout padrão do sistema, ou em um layout configurado manualmente de acordo com os tipos de movimento que forem trabalhados. Deve-se entender aqui, "layout" como a definição dos campos que irão compor o documento na tela, bem como sua disposição; por exemplo, alguns campos não são necessários no lançamento de Notas de Venda, em contrapartida, precisam ser apresentados em um Conhecimento de Transporte, ou seja, essa é diferenciação feita no layout dos respectivos documentos; tal modificação é feita através da tela [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

| [Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AJ3YQBYY22KJ8PDS0S) | [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AKAJ3EBF0FYGKJWK9M) |
| --- | --- |
| [Grade Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AM6144AE6J8XSS702P) | [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2APJDDNNZSAQFBDVVGS) |
| [Como lançar um documento na Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AQGNQ9093VMRZWHT3J) | [Cadastro Simplificado de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AQFD0N7771MBW8V8Z0) |
| [Parâmetros que atuam na Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KYJAE2AQM7D7X203K6V4X32K) |  |

![Imagem 1: Parâmetros que atuam na Central de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/12999683123735)

## Grade Cabeçalho

A grade Cabeçalho, agrupa os dados essenciais do documento; nela teremos a [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) que realiza a venda, o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) cliente para o qual a venda vai ser, está, ou foi realizada, o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) utilizado no processo, e o [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) compatível com a negociação, sendo esta última, uma informação essencial para que as devidas atualizações de estoque, financeiro, livros fiscais ocorram corretamente.

**Observação:** Caso a Empresa informada seja optante pelo Simples Nacional é necessário selecionar um código no campo\*\*"CSOSN"\*\*, localizado na aba [SIMPLES Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasimplesnacional), da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS). Do contrário, ao tentar emitir a nota será apresentada a mensagem:

**"CSOSN não configurado na alíquota utilizada na emissão da nota. Cód Alíquota"**

Além disso, temos dados particulares de cada documento, como o **"Número Único"**, **"Número da Nota"**, Datas de **"Entrada/Saída"**, **"Faturamento"** e **"Movimento"**; como informado inicialmente, outros campos podem ser incluídos no cabeçalho através da rotina [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634); alguns deles, devem ser inseridos para posterior preenchimento, de acordo com a legislação em que cada empresa se enquadra.

Nos **Pedidos de Vendas e Compras,** o campo **"Previsão de entrega"** têm o seguinte comportamento:

- Se a Data de Negociação do novo lançamento for igual à do pedido, o campo Previsão de entrega manterá a mesma data do pedido original.
- Caso a Data de Negociação seja diferente, o campo Previsão de entrega ficará em branco para que possa inserir a data correta. Isso evita que a data prevista seja anterior à data de negociação.

A tag `dPrevEntrega` é gerada no XML de Notas Fiscais Eletrônicas (NF-e) quando o campo "Previsão de Entrega" está preenchido no cabeçalho.

- **Formato de Saída:** A data é gerada no formato **AAAA-MM-DD**.
- **Restrições de Documento:**
  - Só é gerada para **NF-e (modelo 55)**.
  - **Não é criada** para CTe, NFC-e ou NFCom.

O sistema só gera a tag `dPrevEntrega` se **todas** as seguintes condições forem atendidas:

1. A data não seja **anterior à data de saída** (ou à data de emissão, caso a saída esteja vazia).
2. A data **não ultrapasse 3 meses** após a data de saída.
3. A finalidade da emissão seja **“1” (Normal)** ou **“4” (Devolução de mercadoria)**.
4. A modalidade do frete **não seja** **“1”, “4” ou “9”**.

Em caso de emissão de [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e) na venda, para que as tags de Características Adicionais sejam geradas no documento fiscal é necessário inserir os campos **"Característica adicional do transporte"** e **"Característica adicional do serviço"** por meio do Configurador de Layout da Nota no cabeçalho da nota. Desse modo, ao preenchê-los, as tags  e  serão geradas no XML dentro do grupo **"Compl"** com o conteúdo dos campos citados, respectivamente, e a tag  do mesmo grupo, apresentará o nome do usuário emissor do documento.

**Nota:** Após o lançamento da nota, poderá alterar as datas mencionadas acima, apenas se o parâmetro **"Obriga Dt. Negoc. igual a do servidor em COMPRAS? - DTNEGSERVCPA"** estiver desligado.

![Imagem 2: Nota: Após o lançamento da nota, poderá alterar as datas mencionadas acima, apenas se o parâmetro "Obriga Dt. Negoc.…](https://ajuda.sankhya.com.br/hc/article_attachments/12999749589783)

Assim como ocorre nas outras Centrais, ao iniciar o lançamento de um documento, note que apenas a grade Cabeçalho estará habilitada para edição. A grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) será liberada para inserção dos produtos quando o cabeçalho for salvo; a grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) terá alguns de seus dados carregados automaticamente com o lançamento dos itens, e outras informações poderão ser acrescentadas manualmente.

**Observações:**

- Quando o parâmetro **"Apresentar apenas contratos do Parceiro? - FILTCONTPARCV"** estiver ativado, no preenchimento do campo "Contrato", que é disponibilizado no Cabeçalho do documento por meio do Configurador de layout da nota, será possível pesquisar apenas os contratos vinculados à Empresa e ao Parceiro selecionados no pedido/nota; caso o parâmetro esteja desativado, serão apresentados para busca, todos os contratos independente da Empresa e Parceiro incluídos no documento.
- No Cabeçalho da Nota poderá ser inserido através da tela Configurador de Layout da Nota o campo **"Código GNRE Unidade Federativa"**, que permite informar qual o código utilizado na geração do GNRE. Caso este campo esteja vazio, será utilizada a regra com o menor código para a Unidade Federativa do Parceiro da Nota. Este campo tem relação com a tela [Estados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados), aba **"Geral"** e **"GNRE Unidade Federativa"**, marcação .
- Não havendo registros para a UF correspondente, a geração do GNRE não ocorrerá e será apresentada a seguinte mensagem:

**"Relação entre GNRE e Unidade Federativa não informada".**

- Será possível configurar vários códigos de receita para o mesmo Estado e, também, gerar os campos adicionais para todos os Estados nos quais o mesmo é obrigatório.
- Quando o campo **"Parceiro Descarregamento (MDF-e)"** estiver preenchido e o parceiro da nota for do exterior, ao gerar o XML do MDF-e as tags do

   e a tag

   serão preenchidas com os valores pertinentes a cidade do Parceiro Descarregamento (MDF-e).
- Na Central de Vendas, é possível alterar o vendedor mesmo quando a nota já foi aprovada, para tal ação, basta alterar o Vendedor atual para o de sua preferência e em seguida **"Confirmar todas as alterações"**.

No campo **"Vendedor"**, você poderá informar o vendedor que realizou a venda.

**Nota:** ao ligar o parâmetro **"Exibir apenas vendedores da empresa?"**, apenas os vendedores pertencentes à Empresa que realiza a venda serão apresentados.

\*\*Nota:\*\*quando houver a tentativa de alteração do Vendedor quando a Nota já foi Aprovada, ao salvar a alteração, o sistema exibirá a seguinte mensagem:

**"NF-e/NFS-e com status APROVADA não pode pode ter o vendedor alterado quando o parâmetro TIPTABPRECOS or 'Região do vendedor'ou Tipo de Negoc./Vendedor', ou quando houver cálculo de preço dinâmico.**

Você deve preencher o campo **"Indicador de Intermediador/Marketplace"** se o campo **"Indicador de Presença para NF-e/NFC-e"** estiver com uma das opções a seguir:

- **"2 = Operação não presencial, pela internet.";**
- **"3 = Operação não presencial, Teleatendimento.";**
- **"4 = NFC-e em operação com entrega a domicílio.";**
- **"9 = Operação não presencial, outros.".**

O campo **"Intermediador de Transação"** também deve ser preenchido, caso nos campos Indicador de Presença para NF-e/NFC-e e **"Indicador da Transação"** estiverem com as opções **"1 = Operação Presencial"** e **"1 = Operação com intermediador"**, respectivamente selecionadas.

**Importante:** Para que sejam exibidos, os campos Indicador de Intermediador/Marketplace, Intermediador da Transação e Indicador de Presença para NF-e/NFC-e deverão ser configurados da tela [Configurador de Layout de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

Na emissão de NFS-e, o campo **Intermediador da Transação** também controla o envio dos dados do intermediário do serviço. Ao preenchê-lo com um parceiro válido, o Sankhya Om inclui o bloco `intermediario` dentro do nó `metadados` do JSON, com os dados buscados no cadastro desse parceiro.

**Como funciona?**

Quando o Intermediador da Transação está preenchido, o sistema monta o bloco `intermediario` a partir do cadastro do parceiro informado:

- cpfCnpj — CNPJ / CPF
- inscricaoMunicipal — Inscrição Municipal (enviado como null quando vazio)
- issRetido — Retém ISS (aba Fiscal)
- email — E-mail específico p/ envio NFS-e

Quando o campo está vazio, a nota segue o fluxo padrão, sem o bloco `intermediario`.

Exemplo do bloco gerado no JSON:

```
"metadados": {
    "intermediario": [
        {
            "cpfCnpj": "60502242000105",
            "inscricaoMunicipal": "10643923",
            "issRetido": false,
            "email": "exemplo@empresa.com.br"
        }
    ]
}
```

**Relação com o bloco cliente**

O envio do intermediário é independente do bloco `cliente`. Quando o Tomador do serviço é o próprio Prestador (mesmo parceiro emitente), o bloco `cliente` não é gerado; nesse caso, apenas o bloco `intermediario` identifica a operação. Quando o Tomador é diferente do Prestador, o bloco `cliente` é gerado normalmente com os dados do Tomador, junto com o `intermediario`.

**ℹ️ Nota**

O bloco `intermediario` é enviado somente um por nota, não sendo possível em uma única emissão informar múltiplos .

O campo **Controle do Indicador de Destinatário** é exclusivo para a emissão de NFS-e e define se o serviço foi prestado para o tomador principal ou para um terceiro. Ele atua em conjunto com o campo **Parceiro Destinatário**.

Quando você seleciona a opção\*\*\*"1 - Destinatário não é o tomador"\*\*\*e preenche um parceiro válido, o sistema inclui automaticamente o grupo de tags de endereço desse destinatário no XML da prefeitura (suportando inclusive parceiros estrangeiros ou de outros municípios).

Caso utilize a opção **"0 - Destinatário próprio tomador"**, o sistema fatura a nota apenas com os dados do tomador padrão.

> **Nota:** para que os campos **Controle do Indicador de Destinatário** e **Parceiro Destinatário** fiquem visíveis e acessíveis para preenchimento no cabeçalho da nota, é estritamente necessário que eles tenham sido previamente adicionados à estrutura da tela por meio do [**Configurador de Layout da Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

Ao criar uma nota de devolução por meio do botão **"Cadastrar"**, para que o sistema realize a validação desta nota, ligue o parâmetro **"Valida NF de devolução sem documento referenciado - VALNFDEVDOCREF"**. Além de que, na TOP utilizada na referida nota, as seguintes configurações devem ser realizadas na aba [NF-e/NFC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP):

- Sendo esta TOP de Compra ou Venda, a opção **"Normal"** do campo **"NF-e"** deve estar selecionada;
- Defina o campo **"Modelo de Documento"**, com a opção **"55-Nota Fiscal Eletrônica"**;
- Realize a habilitação da marcação **"Buscar NF-e de origem p/ referenciar na NFe"**.

Dessa forma, ao salvar o cabeçalho na Central de Venda com a referida TOP definida, o sistema emitirá a seguinte mensagem:

**"Está sendo emitida uma nota de devolução sem vínculo com a nota de origem. Verifique, pois a SEFAZ exige esta informação para validação."**

Se todas as configurações acima forem realizadas e você tentar salvar a TOP de devolução na tela Tipos de Operação - TOP com a marcação Buscar NF-e de origem p/ referenciar na NFe desabilitada, a seguinte mensagem será exibida:

**"Este cadastro se refere a uma devolução de emissão própria, mas o campo "Buscar NF de origem p/ referenciar na NFe" está desmarcado. Se este campo ficar desmarcado, pode haver rejeição da nota, pois a SEFAZ exige esta informação".**

Informe no campo **"Indicador negociável Multimodal"** se o indicador será **"Não negociável"** ou **"Negociável"**.

**Observação:** Quando não for selecionada nenhuma das opções, o sistema entenderá como Não negociável.

Quando os modelos de nota 21 e 22 forem utilizados na TOP de venda, os campos abaixo serão utilizados no preenchimento das informações. Observe:

- Cód. Tipo de assinante;
- FISTEL;
- Nro. Característica Sv Tele/Comunicação;
- Quantidade de usuário / login;
- Nro. Identificação do Terminal Telefônico;
- MD5MODCOMTEL;
- Tipo Cliente de Serviços de Comunicação.

**Importante:** Para que os campos mencionados acima sejam exibidos na Central de Vendas, é necessário que estes sejam configurados na tela [Configurador de Layout de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

**Observação:** ao duplicar uma nota confirmada do modelo 21 - Nota Fiscal de Serviço de Comunicação ou modelo 22 - Nota Fiscal de Serviço de Telecomunicação, mesmo que os campos MD5MODCOMTEL e Nro. Identificação do Terminal Telefônico estejam preenchidos na nota modelo, eles serão duplicados em branco.

No campo **"Cód. Parceiro Retirada"**, você poderá informar um parceiro para retirada. Para isso, realize primeiramente as configurações abaixo:

1. Na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao), preencha as informações do estabelecimento como **"Razão social"**, **"Inscrição Estadual/ Identidade"** e na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo), o  **"CEP"** e o **"Cód. Cidade"**.
2. Depois, na tela [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas), aba [Local Retirada](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abalocalretirada), informe no campo **"Cód. do Parceiro Retirada"** o parceiro cadastrado anteriormente e acione a marcação **"Ativo"**.
3. Feito isso, na [Central de vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) realize o lançamento da nota fiscal com o campo **"Cód. Parceiro Retirada"** preenchido. Desse modo, a tag <\*\*retirada\*\*> do XML será gerada com as informações de identificação do estabelecimento e endereço do parceiro.

**Nota:** Ao realizar a inclusão de uma nota na Central de Vendas, se a **"Série da nota"** e o código da **"Empresa"** informados já estiverem em uso no Sankhya Checkout, o sistema apresentará a seguinte mensagem:

**"Não é possível inserir uma NFCe com série e cód-empresa que já estejam sendo utilizados por um Checkout".**

No campo **"Tipo Fretamento"** você poderá selecionar se o tipo de frete será **"1 - Eventual"** ou **"2 - Contínuo"** quando a operação for CT-e com o modal rodoviário para o transporte de pessoas.

Além desse campo, teremos também o campo **"Data e hora da viagem"** que deve ser preenchido com uma data e hora superior ao da data e hora da emissão do CT-e, de outro modo, a SEFAZ rejeitará a nota com a seguinte mensagem:

**"Rejeição: Data e hora da viagem deve ser superior à data de emissão do CT-e"**

É importante saber ainda que, quando o campo Tipo Fretamento for definido com a opção 1 - Eventual, o campo Data e hora da viagem precisa ser configurado, caso contrário, a SEFAZ irá rejeitar a nota com a mensagem:

**"Rejeição: Data e hora da viagem deve ser informada para tipo de fretamento eventual**

Para emitir Notas Fiscais de Serviço (NFS-e) corretamente, principalmente em operações com o exterior, utilize o campo **"Finalização do Serviço"**. Este campo determina como o sistema deve calcular o Imposto Sobre Serviços (ISS) e qual informação fiscal será registrada no arquivo XML da NFS-e.

O campo oferece as seguintes opções:

- **Campo em branco:** mantém o comportamento padrão do sistema;
- **No país:** para serviços prestados e concluídos dentro do Brasil; e
- **No exterior:** para serviços concluídos fora do Brasil.

A seleção que você fizer tem o seguinte impacto fiscal:

- Se você escolher a opção **"No país"**, o sistema calcula e insere o valor do ISS retido na nota fiscal, seguindo a alíquota aplicável. No arquivo XML, é gerada uma informação indicando que o ISS deve incidir.
- Se você escolher **"No exterior"**, o sistema insere o valor do ISS zerado (igual a 0) na nota fiscal. No XML, é gerada uma informação indicando que o ISS não deve incidir/é zero.

![Imagem 3: Escolher a opção correta é fundamental para garantir o cálculo fiscal exato e evitar a rejeição da sua NFS-e.](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) Escolher a opção correta é fundamental para garantir o cálculo fiscal exato e evitar a rejeição da sua NFS-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Grade de Itens

Uma vez que você salvou os dados na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho), a grade **Itens** estará disponível para preenchimento. Nela informe os produtos ou serviços que irão compor o documento que será gerado.

**Importante:** para garantir a exatidão no lançamento de notas de serviços tomados, o campo de alíquota e valor de ISS suporta até 5 casas decimais, respeitando a configuração realizada no cadastro de [Alíquotas.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS)

![Imagem 4: Importante: para garantir a exatidão no lançamento de notas de serviços tomados, o campo de alíquota e valor de ISS…](https://ajuda.sankhya.com.br/hc/article_attachments/12999845509399)

**Nota:** quando o parâmetro "Desabilita a paginação da grade de itens da central - DISABLEGRIDPAG" estiver ativado, o sistema deixará de realizar a paginação. Durante a inserção ou exclusão de itens, a grade será totalmente recarregada para apresentar as alterações. O parâmetro é utilizado para resolver problemas de congelamento de tela que podem ocorrer em notas com grande volume de produtos, evitando conflitos com a rotina de paginação da grade.

Localizado na parte superior da grade **Itens**, tem-se o botão ![Imagem 5: Localizado na parte superior da grade Itens , tem-se o botão "Configuração do Formulário" que ao ser acionado, temos a…](https://ajuda.sankhya.com.br/hc/article_attachments/360100060394) **"Configuração do Formulário"** que ao ser acionado, temos a abertura de um pop-up de mesmo nome, que permite dentre os campos disponíveis, a escolha de quais campos serão selecionados, bem como sua disposição na grade, quando esta se encontrar em Modo Formulário. Estas alterações podem ser realizadas seguindo o que foi previamente definido na tela [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634), ou seja, podemos nestas modificações, trabalhar com os campos que fazem parte do layout.

**Nota:** Ao clicar no botão **"Restaurar padrão"** localizado dentro do botão acima mencionado, o sistema deletará as configurações do usuário logado no momento, fazendo com que este utilize as mesmas configurações realizadas pelo usuário SUP. Desta forma, para que sejam utilizadas as configurações pretendidas, é necessário acessar os layout's com o usuário SUP e defini-los da maneira que deseja. Assim, quando acessar o sistema com outros usuários, basta clicar no botão Restaurar padrão para que, deste modo, busque as novas configurações do usuário SUP.

Ainda sobre a parte superior da grade **Itens**, podemos visualizar o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15422091601303) **"Configurar Grade"** que permite a seleção de duas formas de visualização, sendo: Modo Grade e Modo Formulário. Escolhendo o Modo Grade, é necessário considerar os seguintes pontos:

- Se o parâmetro **"Usar ENTER como TAB na grade de itens da central - ENTERTABGRADITE"** estiver ligado, a tecla Enter executará as mesmas funcionalidades da tecla Tab, permitindo o deslocamento do cursor nas colunas contidas na  grade **Itens**. Quando desligado, a tecla Enter funcionará como a tecla Tab apenas em colunas de pesquisas; nas demais colunas executará o comando **"Salvar"**.
- Para alguns campos de pesquisas como por exemplo Referência do Produto e Referência do Fornecedor, é necessário também configurar o parâmetro **"Código e/ou referência nos itens? - CODPROREF"** selecionando no campo **"Valor"** a opção **"Referência"**.
- Em relação ao campo de pesquisa Produto, no parâmetro de chave CODPROREF selecione a opção **"Código"** no campo **"Valor"**.
- Ainda neste contexto, se os campos de pesquisas mencionados anteriormente estiverem sem preenchimento, ao utilizar a tecla Enter o sistema abrirá a tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353).

**Observações:**

**(1)** Caso o parâmetro **"Aceitar valor total igual a zero? - ACEITARVLRZERO"** esteja habilitado, no lançamento de itens na Central, o sistema irá permitir que o valor total de um produto seja igual a zero; caso esteja desabilitado, não será permitido que o valor total do item esteja zerado.

**(1)** Na Configuração da grade é possível que você ajuste a ordenação dos itens conforme desejar, sendo ascendente ou descendente, através da aba **"Ordenação dos dados"**. Você também poderá ajustar conforme o lançamento; para isso, basta não marcar a caixa de seleção ao lado esquerdo dos nomes dos campos.

Sobre o botão **"Atualizar Itens"** no topo da grade **Itens**, você pode obter mais informações a respeito dele, através do link [Botão Atualizar Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600294-Bot%C3%A3o-Atualizar-Itens).

**Notas:**

**(1)** Ao realizar a inclusão de produtos controlados por Série, é aberto para pesquisa o pop-up **"Número de Série"**; neste, ao acionar a lupa para pesquisa das respectivas séries, é possível selecionar múltiplas séries e incluí-las de uma vez na nota; esta seleção é realizada mantendo pressionada a tecla **"Ctrl"** no teclado e clicando nas séries desejadas, onde em seguida, acione o botão **"OK"** para encerrar a inserção.

**(1)** Ao realizar o lançamento dos itens em sua grade correspondente, informando-se um percentual de desconto para este produto, neste campo de percentual é possível definir a sua quantidade de casas decimais; para esta definição, é necessário configurar-se o parâmetro **"Máscara p/ percentual de desconto. - MASCARAPERCDESC"**, onde define-se a máscara a ser utilizada para o campo mencionado. Por padrão, este parâmetro é definido com o valor **##0.00** que representa duas casas decimais. Para utilizar neste campo, quatro casas decimais por exemplo, informa-se a máscara **##0.0000**. Os descontos aqui informados, também serão apresentados na utilização da rotina de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).

**(1)** A configuração do parâmetro MASCARAPERCDESC impacta tanto a apresentação da quantidade de casas decimais na grade de Itens quanto o cálculo do percentual de desconto, uma vez que a quantidade de casas decimais definida afeta diretamente os valores calculados.

É fundamental configurar corretamente esse parâmetro quando for liberado ao usuário a possibilidade de digitar os valores nos campos **"Vlr. Desconto"** ou **"Preço Liq."**, pois a precisão nos cálculos dependerá dessa configuração.

Além disso, caso a informação do campo % Desconto seja inserida manualmente, o sistema arredondará o valor do campo Vlr. desconto, e a situação contrária também ocorre, ou seja, se o campo Vlr. desconto for digitado, o sistema arredondará o valor do campo % Desconto.

Para não ter que modificar a configuração do produto em casos que seja necessário que o valor unitário líquido tenha mais de três casas decimais no XML, deve-se ligar o parâmetro **"Desativ arred. val unit liq na tela. - DECVLRLIQARR"**, assim, o arredondamento será desativado e o XML será preenchido com o valor exato.

**(1)** Os preços apresentados na Central de Vendas, podem ser calculados com base na configuração de [Preço Dinâmico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110953); clique no referido link para obtenção de maiores informações.

**(1)**O parâmetro CALCPRECICMS “Cálculo de preço embutindo índice do Grupo ICMS por Empresa” habilita o campo **Percentual** na aba **Grupo ICMS/ISS por Empresa** do **Cadastro de Parceiros**. Este campo serve para definir um índice por estado conforme as exceções de ICMS. Com isso, o Sankya Om desconsidera o desconto padrão da redução de base de cálculo do ICMS no lançamento de uma nota fiscal na Central de Vendas.

Este parâmetro é válido somente para o tipo de movimento Venda: P-V-D:

- Pedido (P)
- Venda (V)
- Devolução de Vendas (D)

![Imagem 7: Atenção: CALCPRECICMS funciona com o parâmetro EDITVLRUNITLIQ ativo.](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887)Atenção: CALCPRECICMS funciona com o parâmetro EDITVLRUNITLIQ ativo.

**(1)**O campo **"Sequência Fiscal"** da grade **Itens**, vai identificar a posição em que o item está dentro do **XML**. Para que seja gerada a sequência fiscal, a marcação **"Agrupar produtos semelhantes na Nf-e"** do [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) aba **"Validações"** não pode estar selecionada.

**(1)**O campo **"Vlr. Tot.Líq. Desejado"** é utilizado para calcular ou recalcular o **"Vlr. desconto"** de um item, levando em conta certos requisitos tributários como **"Vlr. IPI"** e **"Vlr. substituição"**. Este valor não é salvo na tabela TGFITE, sendo usado apenas para o cálculo do Vlr. desconto.

**(1)**Caso o parâmetro **"ST e IPI embutido como desconto no item da nota - STIPIEMBDESC"** esteja habilitado, no lançamento de um pedido/nota na Central, o sistema irá permitir informar no campo Vlr. Tot.Líq. Desejado o valor final da nota. Deste modo, o sistema automaticamente irá determinar o desconto necessário para chegar a este valor. Para tanto, se faz necessário atentar-se para alguns detalhes:

- Após habilitar o referido parâmetro, acesse a tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) e no layout empregado acrescentar o campo Vlr. Tot.Líq. Desejado na grade Itens da nota;
- O cálculo somente será efetuado quando existir na nota um Valor de IPI e/ou Valor de substituição informado;
- O valor final poderá sofrer perdas devido aos cálculos e arredondamentos aplicados.

**Nota:** Se este parâmetro estiver ligado, o sistema buscará o valor unitário do produto para realizar o cálculo do IPI, logo será necessário sempre digitar o respectivo valor do campo Vlr. Tot. Líq. Desejado mesmo não tendo desconto.

\*\*Observação:\*\*quando o parâmetro **"Gera percentual Tag Aliquota IPI - GERPERCALIQIPI"** estiver ligado, o campo **"Alíq. IPI."** desta aba não será preenchido. No entanto, quando o parâmetro estiver desligado, o campo será automaticamente preenchido com a [Alíquota de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI) configurada.

Por outro lado, **quando esse parâmetro estiver desativado**, o sistema poderá **retirar automaticamente o valor do IPI embutido do custo do produto**, desde que todas as seguintes condições sejam atendidas:

- A operação tenha IPI embutido, ou seja: a TOP esteja marcada para IPI embutido, o tipo de movimento seja V, P ou D, o produto possua código de IPI cadastrado e o imposto esteja presente na venda;
- A operação **não** tenha ST embutido (o parceiro não pode estar com a opção **"Retirar ST"** marcada como Sim ou Sim e considerar no cálculo);
- O parâmetro STIPIEMBDESC esteja desligado;
- E, por fim, uma das seguintes condições deve ser **falsa**:
  - A TOP não está configurada para buscar custo;
  - Ou não há desconto promocional do tipo **"Considerar Sempre"**.

Se todas essas regras forem cumpridas, o sistema desconsidera o valor do IPI no custo do produto.

A marcação **"Não Compõe Total NF-e"** oferece um controle direto sobre o cálculo do **Valor Total da Nota Fiscal (vNF)**.

Você pode incluir este campo no layout da Central de Vendas por meio do [**Configurador de Layout da Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

Utilize esta opção em itens que, por determinação fiscal (como **bonificações**), não devem ter seu valor somado ao Total Geral da Nota. Quando ativada, o valor do item será **excluído** do cálculo do Total da NF-e, garantindo a conformidade do documento fiscal.

Para garantir a precisão e evitar erros, sempre que você tentar confirmar uma nota que contenha qualquer item com a marcação **"Não Compõe Total NF-e"** ativa, o sistema exibirá o seguinte alerta:

“**O item [número do item / código / descrição] está com a marcação “Não compõe total NF-e”. Dessa forma, ele não irá compor o valor total da nota. Deseja confirmar?”**

- **Para confirmar:** se a exclusão do valor estiver correta (exemplo: é uma bonificação), clique em **Sim** para prosseguir com a confirmação da nota.
- **Para revisar:** se a marcação foi feita por engano ou você precisa reverter, clique em **Não**. A confirmação será interrompida, permitindo que você **desmarque o campo** e revise os itens.

O campo **"Qtd. tributação para exportação"**, possibilita informar qual a quantia de tributação para exportação que será gerada no XML na tag . Para que este campo seja visualizado na grade itens, deve-se acessar a tela Configurador de Layout da Nota e acrescenta-lo no layout empregado. A quantidade de casas decimais que o mesmo irá comportar, é definida no campo **"Decimais para Quantidade"**, aba [Medidas e estoques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abamedidas), do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113). Sendo que, o referido campo será disponibilizado de acordo com as seguintes condições:

- Quando se tratar de uma NFS-e que contenha um dos CFOP´s informados no parâmetro **"CFOP's utilizados para tributário de exportao - CFOPTRIBEXPORT"**.
- Na geração da NF-e, a tag

   será alimentada com o valor descrito no campo Qtd. tributação para exportação. Caso o mesmo se encontre sem informações, a referida tag receberá o valor informado no campo **"Quantidade"** desta mesma grade.
- É importante ressaltar que a unidade de venda do produto tem que ser diferente da unidade de tributação, para que ocorra o correto preenchimento da tag

  .

![Imagem 8: Informe no parâmetro CFOPTRIBEXPORT os CFOP´s no qual deseja que sejam incluídos na geração da tag , sendo eles: 5504,…](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) Informe no parâmetro CFOPTRIBEXPORT os CFOP´s no qual deseja que sejam incluídos na geração da tag , sendo eles: 5504, 5505, 6504, 6505, 5501, 5502, 6501, 6502, 5949, 6949, 5101, 5102, 5105, 5106, 5118, 5119, 5155, 5156, 5663, 5666, 5905, 5923, 6101, 6102, 6105, 6106, 6118, 6119, 6155, 6156, 6663, 6666, 6923.

\*\*Observação:\*\*os CFOP´s devem ser separados por vírgulas e a coluna **"TGFITE.QTDTRIBEXPORT"** deverá possuir um valor maior que zero.

O campo **"Metro Cúbico"** da nota (TGFCAB) é preenchido automaticamente com o valor do campo **"M3"** da tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274). Sendo assim, ao salvar itens em um Pedido de Venda, por exemplo, o sistema não calcula automaticamente o metro cúbico total da nota. Esse cálculo é feito apenas na Formação de Carga.

Ainda nesta grade, teremos o painel **"Matéria-Prima"** quando o produto que compor os itens tratar de um kit (configuração realizada na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacomponentes)). Desta forma, quando o produto selecionado na grade tiver componentes, você poderá observar o painel Matéria-Prima. Por outro lado, caso o produto indicado não for um kit, este painel não será visualizado.

Este painel apenas será apresentado após o produto kit ser salvo na grade Itens das Centrais de Notas. Além disso, os seguintes parâmetros deverão encontrar habilitados:

- Tem aba Mat.Prima na Transferência? - TEMMPTRAN;
- Tem aba Mat.Prima na requisição? - TEMMPREQ;
- Tem aba mat.prima na central atend. ao Cliente? - TEMMPVENDA;
- Tem aba mat.prima na central atendimento ao Forn.? - TEMMPCOMPRA;
- Mostrar grid de mat. prima somente quando existir - SHOWGRIDMATPRI.

**Observação:** lembre-se que ao informar um produto tipo kit, ao preencher o campo Quantidade na grade de itens da Central de Vendas, o sistema registrará até no máximo 9 casas decimais.

\*\*Nota:\*\*atualmente, o sistema não realiza transferências de produtos Kit, pois esta se trata de uma operação que executa a explosão do Kit.

**Observação:** caso o parâmetro **"Configuração para Kit Independente - CONFKITIND"** esteja habilitado, ao lançar um produto tipo kit não será possível alterar o campo **"Quantidade Total"** do painel Matéria-Prima. Assim, para que este campo seja editável o parâmetro deve estar desabilitado.

Em relação ao campo **"Alíquota da ST de oper. ant."** tem-se que quando este estiver preenchido, ao realizar a confirmação de uma nota ou gerar seu lote, será informado no XML o valor especificado neste campo na tag . Por outro lado, ao confirmar uma nota sem informar o valor neste campo, a tag acima informada será preenchida com os valores inseridos nos campos **"Vlr. do ICMS da ST de oper. ant."**, **"Base de Cálc. da ST de oper. ant."** e **"Vlr ICMS destacado da oper. própria de oper. ant."** conforme fórmula abaixo:

```
 ((VLRSUBSTANT+ VLRICMSANT) / BASESUBSTITANT)* 100
```

**Observação:** se o campo Alíquota da ST de oper. ant. estiver vazio, em casos de ICMS com cobrança anterior de Substituição Tributária, o sistema usará o valor do campo **"Alíquota suportada pelo Consumidor Final"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#top), aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria), para preencher a tag .

A marcação **“Consumidor Final”** para definir o padrão para a operação, indicando se a destinação é para o Consumidor Final. As opções são **(Não)** ou  **(Sim)**. Essa marcação é herdada automaticamente da TOP configurada, mas permite **ajuste manual** no momento da emissão da nota pelo usuário

**Nota:** Em relação ao desconto no item da Nota, temos que, o sistema fará o cálculo deste apenas se utilizar os valores já trazidos na própria nota. Caso seja inserido um **"Vlr. unitário"** ou **"% desconto"** manualmente, não será considerado o desconto informado nos [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) e sim, no desconto no [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) da Nota.

Desta forma, quaisquer alterações realizadas nos campos de forma manual, farão com que o desconto vinculado aos Tipos de Negociação não seja considerado quando pré-configurado.

O sistema permite informar o valor do crédito presumido de ICMS diretamente na **Central de Vendas**, na grade de itens do CT-e.

Para que o campo esteja disponível:

1. Acesse o [**Configurador de Layout da Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota);
2. Localize o campo **"Vlr Crédito Presumido de ICMS no CT-e (vCred)"**;
3. Inclua-o no layout do CT-e, no quadrante correspondente aos itens.

Após a configuração, o campo passa a ser exibido na Central de Vendas e pode ser preenchido manualmente.

- Se houver valor informado, o sistema gera a tag

   no XML do CT-e com o valor correspondente.
- Se não houver valor informado, a tag não será gerada.
- A tag é aplicável apenas para CST **60** e **90**.

Ao clicar na lupa do campo **"Produto"** será aberta a tela de **"Consulta de Produtos"** ainda na Central de Vendas; nesta serão exibidos os preços por quantidades que foram cadastrados na rotina de [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111833). Ao selecionar o preço através da grade de consulta, o mesmo será carregado na grade Itens da Central. Para isto, clique no botão **"Configurar Painel de Resultado"** (localizado no topo da tela), aba **"Preços"** e realiza a marcação **"Mostrar promoção na grade principal"**. Realizada esta configuração, ao selecionar o preço do produto, será demonstrada a regra de desconto promocional criada.

**Observação:** ao incluir um item no campo acima e este possuir um outro produto cadastrado como sugestão no campo **"Produto/Serviço sugerido"** no [Cadastro de Produtos,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaprodutossugeridosparavenda) caso este possua controle adicional de estoque cadastrado no campo **"Controlar por"** da sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional) (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque)), quando uma venda for realizada com o referido item, o sistema exibirá a seguinte mensagem:

**"Campo CONTROLE do produto xx - 'descrição do produto' deve ser informado"**

De modo que, o produto sugerido controlado por estoque não poderá ser selecionado na venda ao clicar no botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15421797608599) **"Incluir itens"** do pop-up **"Produtos sugeridos para venda"**.

**Importante:** para que o desconto seja aplicado, os produtos lançados devem ser iguais e precisam possuir os mesmo grupos de desconto, bem como estarem incluídos na mesma regra promocional.

**Nota:** O sistema irá atualizar o custo do item da tabela TGFCUSITE considerando os seguintes Tipos de movimentos **"Pedido de Vendas", "Notas de Vendas"** e **"Devolução de Vendas"**. O custo utilizado será o último Custo de Reposição informado no campo **"Custo de Reposição"** da tela [Atualização de Custos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594174). Sendo que, o parâmetro **"Preenche custo do produto no item? - PREENCUSTPROD"** não influencia neste processo.

---

![Imagem 10: Informações adicionais referentes à aplicação de descontos:](https://ajuda.sankhya.com.br/hc/article_attachments/18920981226647) **Informações adicionais referentes à aplicação de descontos:**

Dado que as configurações abaixo sejam realizadas:

**(1)** Os Produtos a serem utilizados nas vendas com seus devidos descontos inseridos na sub-aba **"Regras"** da tela [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os);
**(1)** Na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034), o Produto seja informado no desconto a ser utilizado;
**(1)** Por fim, configurar o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) que será utilizado nas vendas com desconto.

Desse modo, teremos que:

**(1)** Quando o campo **"Tipo da taxa"** da aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas) da tela Tipos de Negociação for configurado com a opção **"Desconto"**, ao incluir um item o sistema irá atualizar o preço do produto e subtrair o valor do preço de tabela, além de aplicar o desconto.
**(1)** Porém, se a opção **"Juro taxa Única"** for definida no campo Tipo da taxa, na inclusão do item o sistema irá atualizar o preço do produto com o valor de preço de tabela aplicando os juros.
**(1)** Por fim, com o campo Tipo da taxa definido com a opção Desconto e na tela Descontos Promocionais possua um **"Percentual"** (aba Características) configurado para o registro do Produto a ser utilizado na venda, o preço do item será atualizado aplicando o desconto no valor de preço de tabela.

**Observação:** caso a opção **"Considerar Maior"** do campo Desconto Promocional seja selecionada, o sistema irá considerar o maior desconto entre o Desconto Promocional e aquele do Tipo de Negociação. Porém, lembre-se que se houver esse desconto, este será considerado apenas quando o parâmetro **"Usar o maior desconto promocional? - USAMAIDESCPROMO"** for habilitado.

![Imagem 11: Caso queira saber a funcionalidade de cada opção do campo Desconto Promocional, acesse o artigo Tipos de Negociação .](https://ajuda.sankhya.com.br/hc/article_attachments/18920988802967) Caso queira saber a funcionalidade de cada opção do campo Desconto Promocional, acesse o artigo [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas:~:text=O%20%22-,Desconto%20Promocional,-%22%20inserido%20neste).

---

No campo **"Cód. Tributação ISS"** pode-se definir o tipo de código de tributação de ISS por meio das seguintes opções:

- 07 - Não Tributado;
- 06 - Isento;
- 00 - Tributado;
- 01 - Tributado com ISS Retido.

Quando houver valor informado no campo **"Base Cálc.Reduzida"** desta grade, temos que, será preenchido o campo 8 do Registro C170 ao realizar a geração do [EFD -Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674).

No campo **"Produto"**, você adicionará produtos que deseja incluir na nota.

Ainda sobre este campo, quando um produto que possui controle adicional por grade é selecionado, o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15421885392791) **"Grade"** será exibido na tela, ao selecionar este, o pop-up de mesmo nome será aberto assim como ocorre na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), porém nas Centrais não haverão as seções para as Configurações dessa grade, sendo que estas serão realizadas na tela Cadastro de Produtos.

[GIF animado: Imagem 13: Ainda sobre este campo, quando um produto que possui controle adicional por grade é selecionado, o botão "Grade" será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019512902)

Clicando em **"Confirmar"**, o campo Controle será alterado com a informação definida no pop-up. Por exemplo, se você selecionar o Tamanho Médio e a Cor Azul, o campo Controleserá modificado para "TAM/COR = TM:M/CR:AZ".

Além disso, caso você tenha configurado mais de um item no pop-up, será gerado um registro para cada variação de produto. Para visualizá-los, basta mudar o formulário para o **"Modo grade"**.

**Observação:** Quando for informado um produto controlado por grade, o campo **"Quantidade"** ficará bloqueado, pois a quantidade deve ser informada no pop-up Grade.

**Observação:** Caso a definição padrão do campo [Grade Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostosinformaesporempresa) seja definida na aba **"Impostos / Informações por empresa"**, esta configuração será utilizada nas operações de compras e venda.

**Nota:** Quando você desejar excluir um item da grade nas Centrais, e este estiver cadastrado na grade padrão mínima, o sistema exibirá a mensagem para que você seja informado que a grade padrão é fechada para a quantidade mínima, porém ainda assim desejar realizar a exclusão, todos os itens também serão excluídos.

Se o produto selecionado possuir Desconto Promocional cadastrado, este será aplicado conforme configuração de valores e período de vigência definidos na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034) no momento em que você incluí-los na Central.

**Observações:**

- Quando você informar um valor no campo **"Quantidade"**, o campo **"% Desconto"** será preenchido de acordo com as configurações efetuadas na tela Descontos Promocionais. Por exemplo, se você inserir até 10 unidades no campo Quantidade o percentual de desconto será de 10%, de 11 até 15 unidades o percentual de desconto será de 15%, de 16 até 20 unidades o percentual de desconto será de 20%, e a partir de 20 unidades o sistema irá considerar o último desconto informado, no caso 20%.
- Para que o desconto não seja concedido a partir de uma determinada quantidade, na tela Descontos Promocionais, efetue o cadastro do desconto e informe o percentual **"0"** (zero) no campo **"%Desc./Vlr. Unit."**. Lembrando que este cadastro deverá ser o último apresentado na tela.
- Caso uma **"Empresa"** e/ou **"Parceiro"** sejam informados na tela Descontos Promocionais, a nota criada também deve possuir a mesma Empresa e/ou Parceiro cadastrados, além de que, a data da nota criada deve estar dentro do período de vigência do desconto.

Para o campo **"%Desc. Bonif"** funcionar corretamente, é necessário que o parâmetro **"Usa Desc. Bonificação? - DESCBONIF"** esteja habilitado, assim, o valor inserido neste campo será diretamente descontado do valor total do item a ser dado o desconto.

**Observação:** quando a TOP é de NF-e, não é possível que o desconto de bonificação seja 100%, pois, o valor unitário não pode ser zero. Do contrário, quando a TOP não está configurada como NF-e, você pode realizar uma venda 100% bonificada, para isso, é necessário emitir uma nota separada para o produto que esteja com a marcação **"Bonificação"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)) ativa.

**Importante:** caso o produto esteja configurado na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral), com o campo **"Usado como"** selecionado com a opção **"Brinde"**, é necessário preencher o campo %Desc. Bonif para garantir que o CFOP seja calculado corretamente.

---

### Conversão Automática de CFOP (Atos Cooperativos)

Para empresas que operam como cooperativas, o sistema possui uma inteligência que altera o CFOP do item automaticamente assim que você adiciona o produto na grade. Essa conversão adequa a emissão aos Ajustes SINIEF (Cartilha OCB), garantindo que a nota reflita se a mercadoria é de produção própria ou adquirida de terceiros.

> **Nota:** Este gatilho automático só é ativado se o cabeçalho da sua nota estiver utilizando uma TOP configurada com os CFOPs **5159, 5160, 6159 ou 6160**. Para qualquer outro CFOP (como 5102 ou 6102), o sistema ignorará a regra e manterá o CFOP padrão da operação.

**Como o sistema define o novo CFOP:** Ao inserir o item na nota, o sistema cruza o destino da operação com o campo **Usado como** (lá do Cadastro de Produtos) para aplicar a conversão:

- **Saídas dentro do estado (TOP com 5159 ou 5160):** \* Converte para **5160** se o produto for Revenda, Matéria Prima ou os códigos R, M, 4, B, C, D, E, F, I, T (Adquirida de terceiros).
  - Converte para **5159** se o produto for dos códigos 1, 2, O, P ou V (Produção própria).
- **Saídas interestaduais (TOP com 6159 ou 6160):**
  - Converte para **6160** se o produto for Revenda, Matéria Prima ou os códigos R, M, 4, B, C, D, E, F, I, T (Adquirida de terceiros).
  - Converte para **6159** se o produto for dos códigos 1, 2, O, P ou V (Produção própria).

> **Atenção:** Como o sistema toma essa decisão sozinho, é estritamente necessário que o campo Usado como esteja classificado corretamente no Cadastro do Produto. Caso note que o CFOP convertido na grade está incorreto para a operação, não force a alteração manual na nota; corrija o cadastro do produto para resolver o problema na raiz.

Para mais informações acesse o artigo [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP).

---

Em relação à funcionalidade do campo **"%Desc. Promoção"**, é preciso que o cadastro na tela Descontos Promocionais encontre-se corretamente efetuado, sendo assim, o desconto será aplicado no item em questão.

**Observação:** quando o desconto promocional por quantidade for aplicado e o campo **"Tipo Desconto"** estiver configurado como **"Percentual"** (definição realizada na tela [Desconto promocional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais)), o campo **"Vlr. unitário"** desta grade será alterado para o valor informado na tela de Desconto promocional. Os campos  %Desc. Promoção e Vlr. desconto desta grade permanecerão inalterados.

Para que o campo **"%Desc. Digitado"** seja habilitado, será necessário que os parâmetros **"Incluir desc. digitado p/ item c/ desc. promo? - INCDESCITEPROM"** e **"Usa Desc. Bonificação? - DESCBONIF"** estejam ligados pois, estes funcionam no sistema como complementos de descontos bonificados.

Referente ao campo **"Cód. Alíq. Icms"**, temos que, ao clicar duas vezes no código cadastrado neste, o sistema abrirá a tela **"Alíquota de ICMS"** no registro correspondente ao item selecionado. Porém, caso você não possua acesso à tela de Alíquotas de ICMS ou no campo não contenha um registro, um aviso será emitido.

O campo **"Indicador Repasse Desoneração"** permite definir, por meio das opções disponíveis, se o valor do ICMS desonerado será deduzido ou não do valor do item. As opções são:

- O valor do ICMS desonerado não deduz do valor do item/total da NF-e;
- O valor do ICMS desonerado deduz do valor do item/total da NF-e.

**Observação:** este campo deve ser preenchido conforme o campo **"Forma de Repasse Desoneração"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) da tela de [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), quando houver cálculo de desoneração.

O campo **"Vlr. Redução ST"** irá apresentar o valor calculado da desoneração do ICMS/ST.

Os campos **"Quantidade"**, **"Vlr. Unit. Moeda"** e **"Vlr. Tot. Moeda"** podem ser utilizados nas [Operações em Moeda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112833-Opera%C3%A7%C3%A3o-em-Moeda) realizadas no Sankhya Om, para isso, no cadastro da TOP que será utilizada nessa operação, habilite a marcação **"Operação em Moeda"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) da tela [Tipos de Operações- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP). Ainda sobre os campos mencionados anteriormente, temos as seguintes observações:

- **Quantidade:** Você pode inserir um valor neste, caso o campo **"Digitação na nota"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda) estiver definido com as opções **"Quantidade"**, **"Quant. e Valor Unitário"** ou **"Quant. e Valor Total"**. Assim como, se o movimento da operação for de transferência e o parâmetro **"Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR"** for ligado;
- **Vlr. Unit. Moeda:** Será possível configurar esse campo, se o campo Digitação na nota for definido com as opções **"Valor Unitário"** ou Quant. e Valor Unitário. Assim como, caso o movimento utilizado na operação for compra, Transferência ou se a nota for de Complemento;
- **Vlr. Tot. Moeda:** Será habilitado para edição se o campo Digitação na nota estiver definido com uma das opções **"Valor Total"** ou Quant. e Valor Total. Assim como, se a nota for de Transferência e o parâmetro Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR estiver ligado.

**Observação:** O campo Quantidade também ficará desabilitado se o parâmetro **"Tabela p/compra de serviço por CR - TABCRFORN"** for ligado, assim como as opções **"Usa Tabela p/ compra por CR?"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes) e **"Validar Tabela de compra por CR?"** da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

**Nota:** O valor da coluna **"Preço líq"** se dá pelo resultado entre o valor da coluna **"Total líq"** dividido pela **"Quantidade"**, e como a coluna Total líq possui apenas duas casas decimais, o valor da coluna Preço líq nem sempre irá bater com o valor da coluna **"Vlr Unitário"**.

**Observação:** ao ativar o parâmetro **"Editar o Vlr.Unit.Liq. e recalc.Desconto? - EDITVLRUNITLIQ"** e alterar o preço no campo Preço Líq., o sistema preencherá de maneira automática os campos % Desconto e Valor Desconto com a diferença entre o  Vlr. unitário e o Preço Líq.

Caso você queira excluir dois ou mais itens de uma vez de um lançamento, basta que você selecione todos esses itens e clique sobre o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15421576647191) **"Excluir"**; após isso, o sistema realizará toda a rotina de atualização e recálculos para os itens que foram excluídos.

**Observações:**

- Em operações envolvendo estoque de terceiros, o sistema só irá realizar a validação de estoque insuficiente se o parâmetro **"Ignora validação de baixa de estoque terceiros? - IGVALBXESTTERC"** estiver desligado, e se o produto informado estiver configurado como **"Terceiros"** (tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral), campo **"Usado como"**).
- Caso a operação envolva estoque de terceiros cujo o produto é seu, não será efetuada essa validação, pois, quando o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) está configurado para **"Subtrair do estoque próprio em poder de terceiros"** (aba [Estoque de Terceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoquedeterceiros), campo **"Estoque com/de Terceiros"**) o sistema procura estoque próprio em poder de terceiros. Se não for encontrado, não irá atualizar os campos **"TGFITE.TERCEIROS"** e **"TGFITE.ATUALESTTERC"**, ou seja, o estoque de terceiros.
- Quando o produto da nota possuir a opção **"Número do lote"** do campo **"Controlar por"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional) configurado, é preciso informar o número de lote do produto ao enviar para o [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias).

Referente ao campo **"Total produtos"**, destacamos que ao realizar uma devolução de venda parcial onde houve desconto aplicado na nota de venda, o dito campo não será considerado no cálculo do índice de juros, uma vez que este é calculado da seguinte maneira:

|  |
| --- |
| `Somatório da qtd. Produtos*(Qtd. neg. * Vlr. Unitário)` |

Para que seja informada a sequência do FCI referente ao item que esta sendo lançado, busque no campo **"Controle FCI"** o cadastro do FCI realizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Controle FCI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#AbaControleFCI).

O campo **"Cód. de Benefício Fiscal na UF"** será preenchido de forma automática quando a marcação **"Utiliza endereço de entrega do contato"** da aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaendereo) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) for habilitada. Porém, caso a marcação Utiliza endereço de entrega do contato seja desligada, o campo Cód. de Benefício Fiscal na UF será configurado conforme a UF do Parceiro informado no cabeçalho da nota.

O campo **"Série NFS-e"** será preenchido de forma automática com a informação do campo **"Prefixo Série NFS-e Padrão Nacional"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), sub-aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNFS-e) (aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)) junto ao dado do campo Série da nota da Grade de Itens.

É importante frisar que, caso o campo Série da nota dessa mesma grade estiver vazio, então o sistema irá inserir zeros à esquerda para completar os três dígitos, mais dois dígitos do campo Prefixo Série NFS-e Padrão Nacional, uma vez que o padrão nacional da NFS-e necessita ter cinco dígitos.

**Observação:** compensações financeiras realizadas nas Centrais não geram registros na tabela acerto de frete (TGFFRE).

---

**![Imagem 15: Informações adicionais: Cálculo com Unidades Alternativas](https://ajuda.sankhya.com.br/hc/article_attachments/18920981226647) Informações adicionais: Cálculo com Unidades Alternativas**

Ao trabalhar com Unidades Alternativas, onde são cadastradas várias unidades alternativas iguais, porém com lotes e quantidades diferentes, o sistema realizará o cálculo com base no valor unitário da respectiva unidade alternativa, considerando seu lote e quantidade. Considere o seguinte exemplo:

(1)** Cadastro de Produto:** Produto 1

(1)** Unidades Alternativas**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Unidade** | **Quantidade** | **Lote** | **Vlr. Unitário** |
| LT | 0,97 | (vazio) | R$ 10,00 |
| LT | 0,98 | 123 | R$ 10,30 |
| LT | 0,99 | 1234 | R$ 10,60 |

**(1)** **Cenário:**

Na Central, ao inserir o item e preencher a Unidade Alternativa, o sistema utilizará primeiramente a quantidade e valor referente à unidade alternativa que não possui lote. Se o lote for preenchido, o sistema recalculará os valores com base na quantidade específica para aquele lote.

(2)** Lançamento:**

- **Produto:** Produto 1
- **Unidade:** LT
- **Lote:** (vazio)
- **Vlr. Unitário:** R$ 10,00

(2)** Antes de salvar:**

- **Produto:** Produto 1
- **Unidade:** LT
- **Lote:** 123
- **Vlr. Unitário:** R$ 10,30

(2)** Após salvar:**

Após salvar a inserção do item, se for realizada uma nova alteração do lote, o sistema não recalculará o campo **"Vlr. Unitário"**. Será necessário atualizar o valor desse campo manualmente para que os cálculos subsequentes sejam processados corretamente.

- **Produto:** Produto 1
- **Unidade:** LT
- **Lote:** 1234
- **Vlr. Unitário:** R$ 10,30

Após a alteração manual do campo Vlr. Unitário, o sistema recalculará os demais campos com base no valor inserido.

---

![Imagem 16: Informações adicionais sobre a GNRE DIFAL:](https://ajuda.sankhya.com.br/hc/article_attachments/18920981226647) **Informações adicionais sobre a GNRE DIFAL:**

Para que a [Fórmula para Parcelas Independentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733) seja considerada no Financeiro da nota é necessário que quando a opção **"GNRE DIFAL"** estiver selecionada no **"Tipo de Título"** da aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) da tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173), o campo **"Fórmula"**, também desta aba não seja preenchido. Considere ainda que:

- Quando o campo Fórmula estiver em branco na tela Tipos de Negociação e existir uma **"Fórmula"** na tela Fórmulas p/ Parcelas Independentes, a GNRE DIFAL é calculada corretamente no Financeiro da nota;
- Caso o campo Fórmula da tela Tipos de Negociação esteja com 0 (zero), o sistema não irá recalcular o valor no Financeiro da nota quando ocorrer qualquer alteração na Grade de Itens da Central de Vendas.

Exemplo:

Foi inserido o Produto com 1 quantidade na Grade de Itens (valor GNRE DIFAL: R$ 15,37);
Em seguida alterou-se para 2 quantidades (valor GNRE DIFAL deveria ser alterado para R$ 30,73).
O valor da GNRE DIFAL deveria ser recalculado, pois foi alterada a quantidade de itens, mas no Financeiro não é recalculado, é mantido o valor do imposto R$ 15,37.

Ressaltando que, este comportamento ocorre quando o 0 (zero) é utilizado no campo Fórmula da tela Tipos de Negociação do GNRE DIFAL.

Já, no caso da GNRE FCP o comportamento é o inverso. Quando se utiliza as fórmulas de parcelas independentes na tela Tipos de Negociação, aba Parcelas, o Tipo de Título **"GNRE FCP"** precisará ficar com 0 (zero) para que seja considerada a fórmula das parcelas independentes, pois este não possui a particularidade de cálculo e recálculo. Independente do valor e quantidade inseridos, o sistema recalcula conforme o esperado.

---

Acesse também:

[Inserção de Itens na Central por Referência (Cód. Barras do Produto)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602754-Inser%C3%A7%C3%A3o-de-Itens-nas-Centrais-por-Refer%C3%AAncia)

[Inclusão Facilitada de Itens nas Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599354-Inclus%C3%A3o-Facilitada-de-Itens-nas-Centrais)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Grade Rodapé

A grade Rodapé é completamente habilitada para utilização, logo após os dados na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) serem salvos. Algumas informações são geradas automaticamente e poderão ser modificadas caso necessário, enquanto que outros dados deverão ser inseridos manualmente. Ela é composta por 8 (oito) abas. Trataremos sobre cada uma delas a seguir:

|  |  |
| --- | --- |
| [Aba Totais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatotais) | [Aba Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatransporte) |
| [Aba Notas Conhecimento Transp.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abanotasconhecimentotransp.) | [Aba Coleta/Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abacoletaentrega) |
| [Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaimpostos) | [Aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro) |
| [Aba Referências e ajustes da NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01H98WJHP55M23JCKYM3AHPXWB) | [Aba NF-e/NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abanf-enfs-e) |
| [Aba Comissões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abacomisses) | [Aba Unidade de Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abaunidadedetransporte) |
| [Aba Multimodal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abamultimodal) | [Aba Retenção do ICMS do Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#AbaReten%C3%A7%C3%A3odoICMSdoTransporte) |
| [Aba Documentos Anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#AbaDocumentosAnteriores) | [Aba Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01KZXJG0HZ7Z6X2VFCVM1SXR33) |
| [Aba Comércio Exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#h_01M3KVWJSRXXEXMMJPHNTY2HV6) |  |

**Observação:** na realização do lançamento de um [Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834), são apresentadas para verificação e/ou preenchimento, algumas outras abas além das que serão exibidas abaixo; estas podem ser visualizadas por meio do link [Lançamento do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314).

#### Aba Totais

Nesta aba são agrupados os valores finais a respeito do documento lançado, tomando por base os valores e percentuais referentes aos preços e descontos aplicados nos itens, respectivamente.

![Imagem 17: Nesta aba são agrupados os valores finais a respeito do documento lançado, tomando por base os valores e percentuais…](https://ajuda.sankhya.com.br/hc/article_attachments/12999902828823)

O campo **"Vlr. Repasse a Terceiros (NFS-e)"** pode ser incluído na Central de Vendas por meio do [Configurador de layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634). Esse campo permite informar o valor que será registrado na tag . Importante destacar que:

- Não há incidência de impostos sobre o campo Vlr. Repasse a Terceiros (NFS-e).
- Descontos informados nos itens ou no rodapé da nota não influenciam o campo Vlr. Repasse a Terceiros (NFS-e) e vice-versa.
- O valor inserido no campo Vlr. Repasse a Terceiros (NFS-e) será agregado ao campo Vlr. Nota, sendo também enviado para a tag

  .

**Observação:** caso a empresa trabalhe com descontos no rodapé da nota, esta rotina pode ser influenciada pelo parâmetro **"Distribuir desconto autom. antes calc. impostos? - DISDESAUTANTIMP"** que se for ativado, os valores dos impostos IPI e ST serão desconsiderados na realização da distribuição de descontos. Caso o parâmetro mencionado esteja desligado (situação padrão), o sistema ajusta o desconto para compensar o novo IPI e ST após a distribuição do desconto, de modo a manter o valor da nota independente do IPI e ST.

![Imagem 18: Exemplo de como o sistema calcula e distribui o desconto no Rodapé da nota](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) **Exemplo de como o sistema calcula e distribui o desconto no Rodapé da nota**

O sistema Sankhya realiza a distribuição do desconto aplicado no rodapé da nota de maneira proporcional entre os itens. No entanto, quando o **valor unitário de um item é alterado manualmente e fica acima do preço de tabela (ou "valor custo")**, isso pode gerar uma discrepância na porcentagem de desconto final aplicada a cada produto, mesmo que o percentual de desconto no rodapé da nota seja único.

Isso ocorre porque o cálculo considera um valor "cobrado a mais" para itens com valor unitário alterado, impactando a base sobre a qual o desconto máximo é aplicado, antes da distribuição final do desconto do rodapé.

Para ilustrar esse comportamento, vamos detalhar o cálculo com base nos dados do pedido 2982:

- **Desconto Total (descTot):** R$ 0,50 (50 centavos)
- **Desconto Máximo configurado no cadastro de produtos:** 10% para ambos os produtos.
- **Parâmetro** `DISTJDCONF`**:** Configurado para permitir a distribuição do desconto.

**Parte 1: Cálculo do Total e Máximo a partir dos Itens**

Nesta etapa, o sistema calcula uma base para a distribuição, considerando o valor de custo, a quantidade negociada e o percentual de desconto máximo de cada item. Um ponto crucial é a identificação do **"valor cobrado a mais" (**`cobradoAMais`**)** quando o valor unitário do item é maior que o seu valor de custo.

**Produto 98:**

- **Valor Unitário Lançado (**`vlrTotItem`**):** R$ 2,00
- **Preço de Tabela / Valor Custo (**`valor custo`**):** R$ 1,50
- **Quantidade Negociada:** 1
- **Desconto Máximo (**`descMax`**):** 10%
- **Valor de Desconto do Item (**`vlrDesc` **- inicial):** R$ 0,00

1. **Cálculo do** `vlrTotDesc` **(valor total do desconto baseado no custo):** `vlrTotDesc = valor custo * quantidade negociada = 1,50 * 1 = R$ 1,50`
2. **Identificação do** `cobradoAMais`**:** Como `vlrTotItem` (R$ 2,00) é maior que `vlrTotDesc` (R$ 1,50), o sistema calcula o `cobradoAMais`. `cobradoAMais = vlrTotItem - vlrTotDesc = 2,00 - 1,50 = R$ 0,50`

   > **Observação:** É neste ponto que reside a principal diferença. Se o valor unitário não fosse alterado e fosse igual ao preço de tabela, o `cobradoAMais` seria zero, não impactando os cálculos seguintes.
3. **Cálculo da Parcela** `max` **inicial:** `max = vlrTotDesc * descMax / 100 = 1,50 * 10 / 100 = R$ 0,15`
4. **Atualização de** `total` **e** `max`**:**
   - `total = total (anterior) + max + cobradoAMais = 0 + 0,15 + 0,50 = R$ 0,65`
   - `max = max - (vlrTotDesc - vlrTotItem) - vlrDesc = 0,15 - (-0,50) - 0 = R$ 0,65`

**Produto 96:**

- **Valor Unitário Lançado (**`vlrTotItem`**):** R$ 3,00
- **Preço de Tabela / Valor Custo (**`valor custo`**):** R$ 3,00
- **Quantidade Negociada:** 1
- **Desconto Máximo (**`descMax`**):** 10%
- **Valor de Desconto do Item (**`vlrDesc` **- inicial):** R$ 0,00

1. **Cálculo do** `vlrTotDesc` **(valor total do desconto baseado no custo):** `vlrTotDesc = valor custo * quantidade negociada = 3,00 * 1 = R$ 3,00`
2. **Identificação do** `cobradoAMais`**:** Como `vlrTotItem` (R$ 3,00) é igual a `vlrTotDesc` (R$ 3,00). `cobradoAMais = 0`
3. **Cálculo da Parcela** `max` **inicial:** `max = vlrTotDesc * descMax / 100 = 3,00 * 10 / 100 = R$ 0,30`
4. **Atualização de** `total` **e** `max`**:**
   - `total = total (anterior) + max + cobradoAMais = 0,65 + 0,30 + 0 = R$ 0,95`
   - `max = max - (vlrTotDesc - vlrTotItem) - vlrDesc = 0,30 - (3,00 - 3,00) - 0 = R$ 0,30`

**Parte 2: Cálculo dos Coeficientes e Descontos Finais**

Com os valores totais calculados na primeira parte, o sistema determina um coeficiente de proporcionalidade para distribuir o `descTot` (desconto total do rodapé) entre os itens.

- `total` **(acumulado):** R$ 0,95
- `descTotSaldo` **(desconto total a ser distribuído):** R$ 0,50

1. **Cálculo do Coeficiente (**`coeficiente` **e** `coeficienteSemIpiSt`**):** `coeficiente = descTotSaldo / total = 0,50 / 0,95 = 0,5263 (arredondado)` `coeficienteSemIpiSt = descTotSaldo / total = 0,50 / 0,95 = 0,5263 (arredondado)` `indiceIpiStCoeficiente = coeficiente / coeficienteSemIpiSt = 1`
2. **Inicialização de** `totalDesc`**:** `totalDesc = 0`

**Novamente para cada Item:**

**Produto 98:**

1. **Recálculo de** `max` **(base para o desconto do item):** `max = cobradoAMais + ((vlrTotDesc * descMax) / 100) = 0,50 + ((1,50 * 10) / 100) = 0,50 + 0,15 = R$ 0,65`
2. **Cálculo do** `desc` **(desconto efetivo para o item):** `desc = max * coeficiente = 0,65 * 0,5263 = R$ 0,3421`
3. `VLRDESC DO ITEM`**:** `0,3421` `totalDesc = totalDesc + VLRDESC = 0 + 0,3421 = R$ 0,3421`
4. `PERCDESC DO ITEM` **(Porcentagem de Desconto Final):** `PERCDESC = VLRDESC / VLRTOT (Valor Unitário Lançado) * 100 = 0,3421 / 2,00 * 100 = 17,105% (aproximadamente 17,11%)`

**Produto 96:**

1. **Recálculo de** `max` **(base para o desconto do item):** `max = cobradoAMais + ((vlrTotDesc * descMax) / 100) = 0 + ((3,00 * 10) / 100) = 0,30`
2. **Cálculo do** `desc` **(desconto efetivo para o item):** `desc = max * coeficiente = 0,30 * 0,5263 = R$ 0,1579`
3. `VLRDESC DO ITEM`**:** `0,1579` `totalDesc = totalDesc + VLRDESC = 0,3421 + 0,1579 = R$ 0,50` (Note que a soma dos `VLRDESC` dos itens totaliza o `descTot` do rodapé)
4. `PERCDESC DO ITEM` **(Porcentagem de Desconto Final):** `PERCDESC = VLRDESC / VLRTOT (Valor Unitário Lançado) * 100 = 0,1579 / 3,00 * 100 = 5,263% (aproximadamente 5,26%)`

Como pode ser observado, a porcentagem de desconto por item (`PERCDESC DO ITEM`) difere entre o Produto 98 (17,11%) e o Produto 96 (5,26%), mesmo com o mesmo percentual de desconto no rodapé (10%). Essa diferença é causada pelo cálculo do `cobradoAMais` para o Produto 98, que teve seu valor unitário alterado acima do preço de tabela, alterando a base de cálculo para a distribuição proporcional do desconto.

A soma dos valores de desconto (`VLRDESC DO ITEM`) de ambos os produtos (0,3421 + 0,1579 = 0,50) corresponde exatamente ao `descTot` de R$ 0,50 aplicado no rodapé da nota, validando que o valor total do desconto está sendo distribuído corretamente, mas a proporção individual é influenciada pelo `cobradoAMais`.

### Recálculo do Repasse

Quando há necessidade de recalcular o repasse, o sistema executa automaticamente algumas etapas para garantir que o valor do repasse permaneça proporcional ao novo valor da nota.

**1**. Validação das condições para recálculo

O recálculo somente é realizado quando:

- O valor da nota é maior que zero;
- O valor total de \*\*Desconto de Redução de Base\*\* também é maior que zero.

Caso essas condições não sejam atendidas, o recálculo não é aplicado.

**2**. Apuração do total de repasse reduzido

O sistema identifica e soma o valor de repasse reduzido dos itens da nota, considerando apenas os itens que atendem aos critérios definidos para o cálculo.

**3.** Identificação do valor original da nota

Para encontrar o valor da nota antes da aplicação dos descontos, o sistema soma:

- O valor atual da nota;
- O total de repasse reduzido;
- O total de descontos aplicados.

Com isso, obtém-se o valor original da nota antes das reduções.

**4.** Ajuste proporcional do repasse

O valor do repasse é recalculado proporcionalmente ao novo valor da nota (já com os descontos aplicados).
Esse ajuste é realizado por meio de cálculo proporcional, garantindo que o repasse acompanhe a redução do valor total da nota.

**5.** Recalculo do percentual de desconto

Após o ajuste do repasse, o percentual de desconto da nota é recalculado com base no novo valor total.

**6.** Atualização das informações na nota

Por fim, o sistema atualiza automaticamente:

- O valor total da nota;
- O valor total de desconto;
- O percentual de desconto.

Dessa forma, todos os valores passam a refletir corretamente o novo cenário após o recálculo do repasse.

**Nota:** em relação ao produto que possui seu preço definido em moeda, ao inserir no Rodapé da Nota um desconto, o sistema realizará o rateio do valor deste desconto entre os itens da nota e manterá o valor total da NF-e considerando o desconto definido no Rodapé. Para isto, é necessário realizar as seguintes configurações:

- Habilitar a marcação **"Operação em Moeda"** localizada na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral);
- Verificar o valor da moeda atualizado na tela [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754);
- Certificar que o Produto permite desconto através da tela [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda), campo **"% Desconto Máximo"**;
- Configurar o parâmetro **"Valida desconto máximo - VALDESCMAX"** com qualquer opção diferente de **"Não valida"** e;
- Habilitar o parâmetro **"Distribuir desc. na confirmação da nota - DISTJDCONF?"**.

**Observação:** Ao confirmar a nota pela Central e esta possuir um valor informado no campo **"Vlr do Juro"** do rodapé da nota, os campos **"Base de Cálculo"** e **"Base Cálc.Reduzida"** da opção **"Consultar/Alterar Dados do Imposto do Item"** terão mesmo valor do campo Vlr do Juro.

**Observação:** Se houver uma compensação financeira no lançamento da Nota Fiscal feita com Difal, o sistema a reconhecerá como um título. Sendo assim o valor da referida Nota Fiscal será afetado, logo é necessário realizar esse lançamento através de um projeto adaptativo.

![Imagem 19: Atualmente, o sistema não está preparado para realizar o rateio de descontos que aparecem no rodapé da nota após a…](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) Atualmente, o sistema não está preparado para realizar o rateio de descontos que aparecem no rodapé da nota após a confirmação, especialmente quando o item é um serviço (CODUSOPROD = S). Isso resulta na não aplicação dos descontos nos valores desses itens.

#### Regra de recálculo para alteração de percentual de desconto no rodapé:

Quando for informado um percentual de desconto no rodapé da nota e este for alterado, o sistema seguirá a seguinte regra de recálculo:

- **Condições necessárias:**
  1. Existência de valor de redução nos itens da nota;
  2. O tipo de movimentação **não** ser Venda;
  3. Parâmetros **DISTJDCONF** e **DESCTOTVIAITENS** estarem desligados.
- **Comportamento:** O sistema realizará o recálculo do desconto utilizando como base o **valor da nota somado ao valor de redução total**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Transporte

Na aba Transporte temos, os dados a respeito do frete do documento que está sendo lançado, tais como, o **"Parceiro Transportador"**, a **"Quantidade de Volumes"** destinados à carga da nota, qual será o **"Tipo do frete"**, ou seja, se **"Incluso"** ou **"Extra nota"** , se será **"CIF"**  **\***  ou **"FOB"\*\*\*\*\*\***, entre outras informações.

CIF\*\*\*\*\* - O frete é pago por quem envia a mercadoria, ou seja, o Remetente.

FOB\*\*\*\*\*\* - O frete é pago por quem recebe a mercadoria, ou seja, o Destinatário.

**Observações:**

- a funcionalidade de sugestão preferencial para o **"Parceiro Transportadora"** é considerada apenas em novos lançamentos de documentos ou quando o referido campo estiver em branco. Após ser preenchido, mesmo que o Parceiro do cabeçalho seja alterado, esse campo não será atualizado automaticamente;
- quando uma NF-e for lançada sem frete e existir uma Ordem de Carga vinculada ao **"Parceiro Transportadora"**, o sistema irá gerar no XML o grupo

   com os dados do transportador da OC.

![Imagem 20: com os dados do transportador da OC.](https://ajuda.sankhya.com.br/hc/article_attachments/13000650567063)

**Observação:** Em Notas Fiscais Eletrônicas, nos itens na qual tem-se **"Campos Adicionais"** e **"Observações"** informadas, estas podem ser modificadas mesmo que o documento já esteja confirmado. Ainda se tratando de NF-e's, tendo este documento sido aprovado e sendo composto por frete **"Extra Nota"**, caso necessário, os campos **"Vlr. do Frete"** e **"Vencimento do Frete"** podem ser ajustados. Ao solicitar o salvamento das alterações realizadas no documento, será apresentado o pop-up de nome **"Salvar documento confirmado"** onde será definido quais informações serão salvas.

Em relação ao campo **"Qtd. volumes"**, este será atualizado apenas na confirmação do lançamento. Diante disto, havendo alterações posteriores na nota, estas não serão replicadas ao campo.

**Observação:** Ao habilitar o parâmetro **"Somar Quantidade de Volumes por - SOMAQTDVOL"**, o sistema mudará o cálculo da Quantidade de volumes da nota. Para entendermos a diferença entre as possíveis opções, considere o seguinte exemplo:

1 - Produto X:

- Unidade principal = UN,
- Unidade alternativa = CX multiplicada por 10.
- Grupo de produtos = A
- Qtd embalagens = 2

2 - Produto Y:

- Grupo de produtos = B
- Qtd embalagens = 1

3 - Produto Z:

- Grupo de produtos = B
- Qtd embalagens = 1

O cálculo da quantidade de volumes da nota pode ocorrer das seguintes maneiras:

**Qtd principal:** Soma as quantidades baseadas no volume principal do produto. Temos:

1. Tendo-se 4 CX do produto X, tem-se 40 volumes, pois cada caixa possui 10 UN (unidade principal).
2. Tendo-se 40 UN do produto X, tem-se 40 volumes.

**Qtd. da tela:** A quantidade de volumes será igual à quantidade da tela, ou seja:

1. Se temos 4 CX do produto X, tem-se 4 volumes.
2. Tendo-se 40 UN do produto X, tem-se 40 volumes.

**Qtd./Embalagens por Grupo:** Serão agrupadas unidades de produtos diferentes, mas pertencentes a um mesmo grupo; em seguida, temos a divisão pela Quantidade de Embalagem informada no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

Lançando os itens na nota da seguinte maneira:

Produto X | Grupo de Produtos A | Embalagem = 2 | Quantidade = 6

Produto Y | Grupo de Produtos B | Embalagem = 1 | Quantidade = 2

Produto Z | Grupo de Produtos B | Embalagem = 1 | Quantidade = 2

Temos a Quantidade dividida pelo Número de embalagens:

6 / 2 = 3

2 / 1 = 2

2 / 1 = 2

Ou seja, na soma, o sistema preencherá o campo Qtd. volumes com 7.

**Qtd./Embalagens por Produto:** Serão somadas as unidades de produtos e em seguida, temos a divisão pela Quantidade de Embalagens definida no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-).

Lançando os itens na nota da seguinte maneira:

Produto X | Embalagem = 2 | Quantidade = 2

Produto Y | Embalagem = 1 | Quantidade = 2

Produto Z | Embalagem = 1 | Quantidade = 2

Deste modo, tem-se a Quantidade dividida pelo número de embalagens:

2 / 2 = 1

2 / 1 = 2

2 / 1 = 2

Ou seja, na soma, o sistema preencherá o campo Qtd. volumes com 5.

\*\*Soma dos Volumes dos pedidos:\*\*Esta opção vai somar a Quantidade de Volumes dos pedidos, de forma que quando estes forem faturados, esta soma será a quantidade de volumes na nota, ou seja:

1. Pedido | Qtd. Volumes = 10
2. Pedido | Qtd. Volumes = 15
3. Pedido | Qtd. Volumes = 20

Na nota temos a Quantidade de Volumes = 45

**Observação sobre o Faturamento Parcial:** om o parâmetro **SOMAQTDVOL** marcado na opção **"Soma dos Volumes dos pedidos"**, o sistema não proporcionalizará a quantidade de volumes no faturamento, gerando o volume completo.

Isso significa que, se um pedido for dividido entre duas notas faturadas (por exemplo, uma sequência do pedido indo para uma nota e outra sequência para outra nota devido à configuração da TOP), ambas as notas apresentarão o volume total do pedido original.

**Exemplo:** Um pedido com quantidade de volume igual a **2** é faturado parcialmente. Mesmo que a nota contenha apenas parte dos itens, ela registrará **2** de volume. Atualmente, o sistema não possui uma maneira de realizar essa divisão proporcional corretamente no faturamento.

> **Nota:** todas as totalizações, exceto a primeira, serão arredondadas a cada produto para cima, nesse caso o sistema não trata embalagem fracionada.

**Observação:** Para que a quantidade de volumes dos pedidos seja somada na nota, o parâmetro **"Preserva a quantidade do Volume pedido? - PRESERQTDVOL"** deve estar desabilitado; caso esteja ligado, será mantida a quantidade de volumes do primeiro pedido.

Teremos ainda que, ao confirmar uma nota de venda o sistema irá recalcular os impostos e atualizar o valor da GNRE no financeiro, sendo que, esta condiz ao ICMS ST EXTRA NOTA.

**Nota:** É necessário que você siga as orientações do artigo [Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094153-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-ICMS-ST-Extra-Nota-GNRE-Venda-) para a geração da GNRE EXTRA NOTA.

**Observação:** Para a geração de um financeiro de GNRE para uma nota de venda, em que esta considere o frete incluso com cláusula CIF no cálculo do ICMS ST EXTRA NOTA, preencha os seguinte requisitos:

- Realize as configurações para geração de GNRE EXTRA NOTA de acordo com o exposto no artigo Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda);
- A TOP utilizada deve ser habilitada com a opção **"Frete/Seguro/Outras Despesas para ST extra nota"** localizada na aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias);
- E os campos **"Tipo do frete"** deverá marcado com a opção **"Inclusão"**, assim como o campo **"CIF / FOB"** que deve estar selecionado com a opção **"CIF"**, devem ser informados no lançamento da nota.
- Sendo necessário também realizar as configurações do **"Estado"**, **"Parceiro"** e da [Fórmula p/ parcelas independentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045912733-F%C3%B3rmula-p-Parcelas-Independentes).

**Desconto com Frete FOB**

O parâmetro **"Usa Perc. Desc. FOB no rodapé (Venda)? - PERCDESCFOBCAB"** quando ativado, permite a aplicação de forma dinâmica do desconto relacionado ao frete FOB. Com este parâmetro habilitado, será possível configurar um percentual de desconto por meio do campo **"Perc. desc. FOB"**; para utilização deste campo, o mesmo deve ser incluído no layout da nota através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634). Além disso, o documento em questão deve ser um Pedido, Nota ou Devolução de Venda, bem como o campo CIF/FOB deve estar definido como FOB - Contratação do Frete por conta do Destinatário. Com base nesta configuração, o recálculo de preço ocorre na seguinte situação:

- Ao serem configurados os campos CIF/FOB e Perc. desc. FOB, caso o campo CIF/FOB não esteja definido como FOB, o sistema zera o valor do campo de percentual de redução e recalcula o preço;
- Caso o percentual do desconto relacionado ao frete FOB seja maior que o valor do campo Perc. desc. FOB, será emitida uma mensagem não permitindo a aplicação do desconto;
- Se o parâmetro **"Usar % Desc.por região p/Frete FOB? - PERCDESCFOB"** estiver ativado e o parâmetro Usa Perc. Desc. FOB no rodapé (Venda)? - PERCDESCFOBCAB estiver desabilitado, no [Cadastro de Regiões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599074) será apresentado o campo **"Perc. desc. FOB"**; caso o parâmetro de chave PERCDESCFOBCAB esteja ativado, a descrição desse campo passa a ser **"% Limite desc. FOB"**.

Indique também o número de **"Lacres"** das unidades de transporte. Caso haja mais de um lacre por unidade, preencha os dados separados por ponto e vírgula (;).

Além disso, se nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abanf-enfc-e), a marcação **"Gerar múltiplas tags  no XML?"** estiver habilitada, serão geradas no XML da nota uma TAG para cada número de lacre informado.

**Nota:** o campo **"Vlr. do frete"** e **"Vlr. frete calc"** é alterado no faturamento com base na variação entre o total dos produtos da origem e o total dos produtos do destino. Sendo assim, tem-se a seguinte fórmula:

```
 (totalitensdest / totalitensorig)  * fretorigem
```

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Notas Conhecimento Transp.

Nesta aba, informe as notas que pertencem ao conhecimento de transporte. É importante ressaltar que, quando for informada mais de uma nota, estas devem possuir o mesmo emitente (remetente) e destinatário.

Você pode indicar nesta aba, notas fiscais que possuam o modelo de documento fiscal **"1"** (Nota Fiscal Convencional), ou o modelo de documento **"55"** (Nota Fiscal Eletrônica).

![Imagem 21: Você pode indicar nesta aba, notas fiscais que possuam o modelo de documento fiscal "1" (Nota Fiscal Convencional), ou…](https://ajuda.sankhya.com.br/hc/article_attachments/13000668559127)

**Observação:** Para inserir campos nesta aba, acesse a tela [Configurador de Layout de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota#top), selecione o Tipo de Movimento em questão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Coleta/Entrega

Informe nesta aba as notas correspondentes a coleta ou entrega diferentes do endereço de origem e destino do [Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834), se assim a empresa desejar.

![Imagem 22: Informe nesta aba as notas correspondentes a coleta ou entrega diferentes do endereço de origem e destino do…](https://ajuda.sankhya.com.br/hc/article_attachments/13000671545879)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Impostos

Com base nas configurações de impostos anteriormente realizadas para cada [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), considerando ainda a localização da [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas) e [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), temos os dados da aba Impostos. Configurações como a geração de [ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), [ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014) e [IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013), e suas respectivas alíquotas por exemplo, são essenciais para alimentação desta aba.

Em relação a marcação **"ISS Retido na fonte"**, o sistema se comportará conforme às configurações realizadas nos cadastros de Cidades e Parceiros, observe:

- Quando a marcação **"Retém ISS"** da aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), do cadastro do Parceiro estiver habilitada e um **"Valor mínimo para retenção"** for configurado na aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913#abanfs-e) da tela Cidades, então a marcação ISS Retido na fonte será ativada. Além disso, se o **"Vlr do ISS"** for igual ou maior ao informado no campo Valor mínimo para retenção, o sistema irá subtrair o valor de ISS do total da nota. Porém, se o Vlr do ISS for menor, a marcação ISS Retido na fonte será desativada.
- Caso no cadastro do Parceiro, a marcação Retém ISS esteja habilitada, mas não seja informado nenhum Valor mínimo para retenção na tela Cidades, o sistema realizará o cálculo de retenção de ISS na nota normalmente.

O campo **"Tipo de Retenção do ISS"** no rodapé do documento fiscal é obrigatório apenas para documentos sujeitos à retenção de ISS. Ele permite a seleção de um dos seguintes valores:

- **Não Retido**
- **Retido pelo Tomador**
- **Retido pelo Intermediário**

Se o ISS não for aplicável, o campo é preenchido automaticamente com **"1 - Não Retido"**.

**Observação:** o campo **"tipoRetencao"** só será incluído no JSON quando a emissão do documento fiscal seguir o **padrão nacional** e o código do município estiver vinculado ao parâmetro **“Cód. IBGE Munic. utilizam NFSe Nacional via broker - CODIBGENFSENAC”**.

Se a emissão não for no padrão nacional ou o município não estiver configurado neste parâmetro, o campo **não será gerado** no JSON.

![Imagem 23: Se a emissão não for no padrão nacional ou o município não estiver configurado neste parâmetro, o campo não será gerado…](https://ajuda.sankhya.com.br/hc/article_attachments/13000692188183)

Quando você acessar o Configurador de Layout de Notas, entrar na grade **“Campos disponíveis”** e adicionar os campos **“BC de PIS ST”** e **“Vlr. de PIS ST”** ou **BC de COFINS ST e Vlr. de COFINS ST** ao layout, essas informações ficarão disponíveis para uso na nota fiscal.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Referências e ajustes da NFS-e

#### O que é e para que serve

A aba **Deduções da Base IBS/CBS** permite que você registre valores de dedução ou redução da base de cálculo do IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição Social sobre o Faturamento) em uma NFS-e. Esses valores — como tributos, emolumentos e condomínio inclusos no aluguel, ou ainda glosa de serviços médicos — não devem compor a base tributável conforme a NT 005 v1.1 da Reforma Tributária. A aba permite o registro estruturado dessas informações, garantindo que sejam enviadas corretamente ao Micro Serviço de NFS-e.

![Imagem 24: A aba Deduções da Base IBS/CBS permite que você registre valores de dedução ou redução da base de cálculo do IBS…](https://ajuda.sankhya.com.br/hc/article_attachments/40825017738135)

#### Como acessar a aba

A aba fica dentro da grade de rodapé **"Referências e ajustes da NFS-e"**. Siga este fluxo:

1. **Abra a Central de Vendas**(Comercial › Vendas › Central de Vendas)
2. **Localize uma NFS-e** para edição (crie uma nova ou abra uma existente)
3. **Acesse a grade de Rodapé e encontre a aba** "Referências e ajustes da NFS-e"
4. **Clique na aba** "Deduções da Base IBS/CBS"
5. **Clique no botão de inserção** (ou atalho apropriado) para adicionar um novo registro de dedução
6. **Preencha os campos** conforme descrito nas seções abaixo
7. **Salve** a NFS-e para persistir as deduções

A aba aceita múltiplos registros — você pode cadastrar quantas deduções forem necessárias, desde que respeitem as regras de negócio.

#### Campos de preenchimento

**Tipo de Dedução/Redução da Base IBS/CBS** — Seleção do tipo de dedução aplicável conforme layout nacional da NFS-e.

**Descrição da Dedução/Redução** — Descrição complementar da dedução (obrigatória apenas para tipo 99).

**Valor da Dedução/Redução da Base IBS/CBS** — Valor monetário da dedução aplicada na nota.

**Total das Deduções** — Campo de resumo automático que exibe a soma acumulada de todas as deduções cadastradas.

#### Tipo de Dedução/Redução da Base IBS/CBS

##### O que faz

Campo de seleção que apresenta os tipos de dedução permitidos conforme a NT 005 v1.1. Cada tipo tem restrições específicas de NBS (Nomenclatura Brasileira de Serviços) e comportamentos de validação distintos.

##### Quando usar

Use para indicar qual categoria de dedução você está registrando. O tipo determina se a descrição é obrigatória e se há compatibilidade com a NBS do item da nota.

##### Como funciona

Ao clicar no campo, o sistema apresenta uma lista com 6 opções:

| Código | Descrição | Restrição de NBS |
| --- | --- | --- |
| 01 | Tributos inclusos no aluguel ou equivalente (Ex.: IPTU, Contribuição de melhoria) | Permitido apenas para NBS 1.1002.10.00 ou 1.1002.20.00 |
| 02 | Emolumentos inclusos no aluguel ou equivalente | Permitido apenas para NBS 1.1002.10.00 ou 1.1002.20.00 |
| 03 | Condomínio incluso no aluguel ou equivalente | Permitido apenas para NBS 1.1002.10.00 ou 1.1002.20.00 |
| 04 | Redutor Social | Permitido apenas para NBS 1.1002.10.00 |
| 05 | Glosa de Serviços Médicos | Sem restrição de NBS |
| 99 | Outras parcelas inclusas no aluguel ou equivalente | Sem restrição de NBS (descrição obrigatória) |

Ao selecionar um tipo, o sistema valida automaticamente se a NBS do item da nota é compatível. Se não for, você receberá uma mensagem de erro ao tentar salvar.

#### Impacto no sistema

A seleção do tipo impacta:

- **Validação de NBS:** O sistema verifica se o tipo é permitido para a NBS do item
- **Obrigatoriedade de descrição:** Tipo 99 exige preenchimento do campo Descrição
- **Integração com Micro Serviço:** O tipo é enviado como parte do grupo gDedRedIBSCBS ao Micro Serviço de NFS-e

#### Configurações relacionadas

| Necessidade | Onde configurar |
| --- | --- |
| Verificar NBS permitida para seu serviço | Cadastro do serviço na Central de Notas › Aba Itens › Campo NBS |
| Consultar tipos de dedução permitidos por legislação | Documentação Técnica da NT 005 v1.1 |

> **Nota:** o campo "Tipo de Dedução/Redução da Base IBS/CBS" não aceita valores livres. Você só pode escolher entre as 6 opções listadas acima.

#### Descrição da Dedução/Redução

##### O que faz

Campo de texto livre para descrever os detalhes da dedução ou redução. É obrigatório apenas quando o tipo selecionado é 99 (Outras parcelas).

##### Quando usar

Use para fornecer contexto adicional sobre a dedução, especialmente quando se trata de "outras parcelas" (tipo 99) que não se enquadram nos tipos predefinidos.

##### Como funciona

- **Para tipos 01–05:** Campo opcional
- **Para tipo 99:** Campo obrigatório
- **Limite:** Máximo 150 caracteres para todos os tipos

Se você tentar preencher com mais de 150 caracteres, o sistema limitará a entrada ou exibirá mensagem de validação bloqueando o salvamento.

#### Impacto no sistema

A descrição é armazenada junto com a dedução e enviada ao Micro Serviço de NFS-e como informação complementar.

> **⚠️ Atenção:** se o tipo de dedução for 99 e você deixar este campo em branco, o sistema impedirá o salvamento da nota. Preencha sempre a descrição para tipo 99.

> **💡 Dica:** para tipo 99, seja descritivo. Use referências como "Lavanderia e manutenção de áreas comuns" ou "Serviço de limpeza mensal" para facilitar auditorias posteriores.

#### Valor da Dedução/Redução da Base IBS/CBS

##### O que faz

Campo monetário que recebe o valor numérico da dedução ou redução aplicada à base de cálculo.

##### Quando usar

Use para informar quanto será deduzido da base tributável. Este valor não pode ser zero ou negativo.

##### Como funciona

- **Formato:** campo monetário (duas casas decimais, separador vírgula ou ponto conforme configuração regional)
- **Validação:** o valor deve ser **maior que zero** (> 0)
- **Rejeição:** valores zerados (0.00) ou negativos (-10.00) serão bloqueados ao salvar

Se você tentar salvar com valor inválido, o sistema exibirá: "O valor da dedução deve ser maior que zero."

##### Impacto no sistema

- O valor é somado ao **Total das Deduções** automaticamente
- Se a soma de todas as deduções ultrapassar o valor total da NFS-e, o sistema bloqueará o salvamento da nota
- O valor é enviado ao Micro Serviço de NFS-e como parte da composição da base tributária

> **Atenção:** certifique-se de que o valor informado é correto. Deduções incorretas podem gerar inconsistências fiscais. Valores negativos não são aceitos em nenhuma circunstância.

#### Total das Deduções

##### O que faz

Campo de resumo automático (somente leitura) que exibe a soma de todas as deduções cadastradas na aba.

##### Quando usar

Use para validar visualmente se a soma das suas deduções está dentro dos limites esperados. Não é editável — atualiza-se automaticamente conforme você adiciona ou edita registros.

#### Como funciona

O sistema calcula em tempo real:

```
Total das Deduções = Valor_Dedução_1 + Valor_Dedução_2 + ... + Valor_Dedução_N
```

Se você tentar salvar a nota com um total de deduções que ultrapasse o valor total da NFS-e, o sistema exibirá mensagem de validação e impedirá o salvamento.

#### Impacto no sistema

Este total é validado contra o valor total da NFS-e como proteção contra registros inconsistentes.

> **Nota:** o campo "Total das Deduções" é apenas informativo. Ele não pode ser editado manualmente.

#### Pontos de atenção

**Validação de NBS incompatível:** se você selecionar um tipo de dedução (como 04 - Redutor Social) e a NBS do item não for compatível, o sistema impedirá o salvamento e exibirá: "O tipo de dedução '04 - Redutor Social' é permitido apenas para NBS 1.1002.10.00." Verifique a NBS do seu item antes de selecionar o tipo.

**Limite de soma de deduções:** o sistema não permite que a soma de todas as deduções ultrapasse o valor total da NFS-e. Se isso ocorrer, você verá uma mensagem de validação bloqueando a confirmação. Reduza o valor de algumas deduções ou remova registros desnecessários.

**Limite de 150 caracteres:** a descrição é limitada a 150 caracteres para todos os tipos de dedução (não apenas para tipo 99). Se tentar ultrapassar esse limite, o sistema bloqueará com: "O campo descrição não pode exceder 150 caracteres."

**Persistência em banco SQL/Oracle:** as deduções são armazenadas em banco de dados SQL ou Oracle vinculadas à NFS-e. Ao reabrir a nota para edição, todos os registros de dedução serão recuperados corretamente.

#### Repasses e reembolsos de terceiros (gReeRepRes — NT 004 v2.0)

A NT 004 v2.0 introduziu no layout nacional da NFS-e o grupo `gReeRepRes`, que identifica valores recebidos pelo prestador relacionados a operações de terceiros — como reembolsos, repasses ou ressarcimentos já tributados anteriormente. Esse cenário é comum em intermediação imobiliária, agências de turismo e agências de publicidade, nas quais o prestador recebe valores que não compõem sua receita própria.

Para registrar essas informações, acesse a grade **Referências e ajustes da NFS-e** na Central de Vendas e abra a aba **Repasses e reembolsos de terceiros**.

**Campos da aba Repasses e reembolsos de terceiros**

- **Tipo de repasse** — selecione uma das opções previstas no layout nacional:
  - 01 — Repasse de remuneração por intermediação de imóveis a demais corretores envolvidos na operação
  - 02 — Repasse de valores a fornecedor relativo a fornecimento intermediado por agência de turismo
  - 03 — Reembolso ou ressarcimento recebido por agência de propaganda e publicidade por valores pagos relativos a serviços de produção externa por conta e ordem de terceiro
  - 04 — Reembolso ou ressarcimento recebido por agência de propaganda e publicidade por valores pagos relativos a serviços de mídia por conta e ordem de terceiro
  - 99 — Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem de terceiro

|  |
| --- |
| ℹ️ Nota Ao selecionar o tipo 99, o campo **Descrição do reembolso ou ressarcimento** torna-se obrigatório. Limite de 150 caracteres. |

- **Fornecedor** — informe o CNPJ, CPF ou NIF. O sistema preenche automaticamente o fornecedor ao selecionar um documento da Central de Notas, e filtra os documentos disponíveis conforme o fornecedor informado.
- **Documento de origem** — documento ao qual o repasse ou reembolso está vinculado.
- **Valor do reembolso, repasse ou ressarcimento** — valor individual do registro. A aba exibe o total acumulado de todos os registros informados na nota.

**Validações aplicadas pelo sistema**

O sistema bloqueia a confirmação da nota quando:

- O valor informado em qualquer linha é zero ou negativo
- A soma dos valores registrados na aba ultrapassa o valor total da NFS-e
- Há mais de um registro com o mesmo CNPJ, CPF ou NIF para o mesmo fornecedor

Na emissão da NFS-e pelo Nota Gateway, os registros desta aba são enviados no JSON, no grupo `reembolsoRepasseRessarcimento`. Para saber mais, acesse [NFS-e e Reforma Tributária: Configuração e Uso do IBS/CBS via Nota Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567-NFS-e-e-Reforma-Tribut%C3%A1ria-Configura%C3%A7%C3%A3o-e-Uso-do-IBS-CBS-via-Nota-Gateway#repasses-reembolsos).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Financeiro

Esta aba permite que você ajuste o valor das parcelas, seus vencimentos bem como alguma outra anotação relevante no histórico. Além disso, ela exibe os dados do financeiro do documento, de acordo com as configurações definidas essencialmente na [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), nos [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494) e, consequentemente, no [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173).

![Imagem 25: Esta aba permite que você ajuste o valor das parcelas, seus vencimentos bem como alguma outra anotação relevante no…](https://ajuda.sankhya.com.br/hc/article_attachments/13000709699351)

Normalmente os Pedidos de Venda provisionam o financeiro para análise de fluxo de caixa e controle de metas.

A informação **"Nro.Único"** possibilita que você consulte o título na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e a informação **"Nro.Único Bancário"** permite que você o encontre na tela de [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653), lembrando que este último, só será preenchido quando o título for quitado.

Em processos de emissão de nota fiscal eletrônica de serviços o campo **"Nro NFS-e"** indicará o número da nota fiscal eletrônica de serviço. É um campo protegido e será alimentado em conformidade com o informado no campo Nro. NFS-e do cabeçalho da Nota.

**Observação:** o parâmetro **"Força atualização da provisão na confirmação da nota?? - FORCATPROVCONF"** quando ligado irá garantir que após o processo de confirmação da nota, o campo **"Provisão"** não tenha seu valor alterado por qualquer outra rotina de banco.

![Imagem 26: Os campos citados anteriormente podem ser incluídos na aba Financeiro, através da tela Configurador de Layout da Nota .](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) Os campos citados anteriormente podem ser incluídos na aba Financeiro, através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

**Importante:** No Sankhya Om, os financeiros serão gerados na seguinte ordem: PRAZO, TIPOEMP, CODEMP, TIPOPAR, CODPARC.

**Nota:** O Nro. NFS-e da nota também será exibido na tela [Cadastro Livro ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608394-Cadastro-Livro-ISS#dadosgerais) no campo **"Nro. NFS-e"** e assim, gerado no [Livro ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607514-Gera%C3%A7%C3%A3o-ISS).

O sistema seguirá a seguinte ordem para calcular a Data de Vencimento do pagamento, caso a empresa informada esteja configurada com prazo máximo para pagamento e dia fixo, e ainda, se os parâmetros **"Utiliza regra de venciomento para dias fixos - USARDIAFIXOVCT"**, **"Altera calculo de vencimento para dias fixos - CALDIAFIXOVCT"**, **"Data Base p/ Calculo do Vencimento no Faturamento - DTCALCVENC"**, **"Transfere vencimento quando fim de semana/feriado- TRANSFVENC"** e o **"Ajustar dia fixo após aplicação dos prazos?- AJUSDIAFIXOPRZO"**, estiverem ligados:

- 1° Data de faturamento
- 2° Prazo médio de pagamento
- 3° Tipo de Negociação
- 4° Dia Fixo

Sendo que, caso o dia fixo de pagamento do Parceiro seja no final de semana ou feriado, o sistema irá carregar a data do próximo dia útil.

A seguir, trataremos de alguns botões para realização de modificações no financeiro caso necessário.

Clique no link, para saber mais detalhes sobre os botões ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15422196128023) [Parcelar com Vários Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598674)  e ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15421941073047) [Alterar Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598874).

O botão ![clip7883](https://ajuda.sankhya.com.br/hc/article_attachments/360061025974) **"Confirmar Alterações"** é utilizado para efetivação de alguma modificação realizada no financeiro de notas já confirmadas.

Já o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15422162153367) **"Receber"** é empregado nos recebimentos feitos com cartão de crédito; será aberto o pop-up **"Recebimento com cartão"** para concretização do procedimento. Este botão é utilizado na rotina [Integração com TEF AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873).

**Observação:** A Central de Vendas não aceita o tipo de pagamento POS, apenas TEF.

O botão ![Imagem 31: O botão "Outras Opções..." é composto por duas funcionalidades:](https://ajuda.sankhya.com.br/hc/article_attachments/27465287904919) **"Outras Opções..."** é composto por duas funcionalidades:

- **Pref. de recebimento com cartão:** Neste, teremos as particularidades acerca do recebimento com cartão; são definições realizadas e salvas por usuário. No tópico Preferências de recebimento com cartão, explanamos melhor sobre esta opção.
- **Reimprimir comprovante:** Para imprimir os comprovantes, a impressora vinculada à máquina deve ter o nome cadastrado como IMPRESSORATEF. No caso da utilização do Windows, esta configuração é realizada no Painel de Controle > Dispositivos e Impressoras.

**Observação:** Os campos texto apresentados nesta aba, podem ter sua apresentação influenciada pelo parâmetro **"Usa text area grande no financeiro? - USABIGTEXTAREA"**, que ao ser ativado, exibe os campos em tamanho grande na aba; desligando o parâmetro, os campos são exibidos em tamanho pequeno. Qualquer campo adicional do tipo texto que possua a forma de apresentação igual a caixa de texto, será exibido de acordo com a definição feita no referido parâmetro.

**Nota:** Quando na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), a opção **"Proibir impressão boleto?"** estiver selecionada, o tipo de título da nota não irá gerar um boleto assim como não gerará a taxa de boleto, portanto ao confirmar a nota, você poderá observar que neste Tipo de Título em questão as linhas **"Cód. Barras Receb."** e **"Linha Dig. Receb."** estarão em branco.

Quando o parâmetro **"Pront. Ent. WMW recalcula fianceiro e icms? - PRONTENTWMWRFI"** estiver ligado, irá refazer o ICMS do item e recalculará o financeiro da nota e, quando estiver desligado e o cliente for WMW, não será refeito o ICMS do item e nem recalculado o financeiro da nota.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Comissões

A aba Comissões é empregada para inserção dos vendedores e suas respectivas comissões obtidas sobre as vendas realizadas. Além disso, você pode incluir alguma observação pertinente ao documento, a operação ou mesmo sobre o vendedor.

![Imagem 32: A aba Comissões é empregada para inserção dos vendedores e suas respectivas comissões obtidas sobre as vendas…](https://ajuda.sankhya.com.br/hc/article_attachments/13000885095191)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba NF-e/NFS-e

Esta aba é alimentada, em casos de lançamento de Notas Fiscais Eletrônicas ou Notas Fiscais de Serviço Eletrônicas; será possível visualizar informações como a **"Chave NF-e"**, **"Status NF-e"** ou **"Status NFS-e"**, **"Número"** e **"Data do Protocolo da NF-e"**, entre outros dados..

![Imagem 33: Esta aba é alimentada, em casos de lançamento de Notas Fiscais Eletrônicas ou Notas Fiscais de Serviço Eletrônicas;…](https://ajuda.sankhya.com.br/hc/article_attachments/13000887093783)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Multimodal

**Observação:** Você pode incluir essa aba, através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

Para o [CT-e Multimodal](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403013730327-CT-e-Multimodal-), realize as configurações iniciais de [Lançamento do CT-e.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599314) Depois, nessa aba informe os seguintes campos:

No campo **"Modal CT-e"** selecione o tipo de modal **"Rodoviário"** ou **"Aquaviário"**. Após isto, informe a transportadora responsável pelo percurso, através do campo **"Cód. Parceiro"**. Por último, preencha o **"Cód. Cidade Início"** e o **"Cód. Cidade Término"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Unidade de Transporte

Nessa aba, indique os tipo de transportes utilizados e as informações referentes ao containers.

Para isso, preencha o campo **"Tipo da Unidade de Transporte"**, conforme as seguintes opções:

- Rodoviário Tração
- Rodoviário Reboque
- Navio
- Balsa
- Aeronave
- Vagão
- Outros

Depois, informe o campo **"Identificação Unidade Transporte"** de acordo com o tipo da unidade de transporte. Por exemplo, para rodoviário tração ou reboque preencha com o número da Placa.

**Sub- aba Unidades de Carga**

Selecione o **"Tipo da Unidade de Carga"**, conforme as seguintes opções:

- Container
- ULD
- Pallet
- Outros

Depois informe a **"Identificação da Unidade da Carga"**, por exemplo, o número do container. Após isto, indique o **"Número Lacre"** das unidades de carga. Por fim, preencha a **"Quantidade Rateada"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Documentos Anteriores

Caso seja inserido um layout de venda na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) incluindo a aba Documentos Anteriores na grade de [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap), ao acessar a Central de Vendas utilizando este layout, a grade será apresentada da seguinte forma:

![Imagem 34: Caso seja inserido um layout de venda na tela Configurador de Layout da Nota incluindo a aba Documentos Anteriores na…](https://ajuda.sankhya.com.br/hc/article_attachments/27465233564823)

O campo **"Parceiro Emissor do Documento"** é o único apresentado no painel principal e é comum aos dois grupos de documentos, sendo utilizado para seleção do Parceiro. Além disso, é possível visualizar a sub-aba **"Documentos Eletronicos"**, que possui os campos **"Chave de Acesso (doc. anterior)"** com função de texto de até 44 caracteres e o **"CT-e Referenciado"** que pode ser habilitado para definir se a CT-e está referenciado por outro documento fiscal ou não.

Já a sub-aba **"Documentos em Papel"** possui o campo **"Tipo do documento de Transporte Anterior"** o qual terá as seguintes opções:

- Em branco;
- 07-ATRE;
- 08-DTA (Despacho de Trânsito Aduaneiro);
- 09-Conhecimento Aéreo Internacional;
- 10 – Conhecimento - Carta de Porte Internacional;
- 11 – Conhecimento Avulso;
- 12 - TIF (Transporte Internacional Ferroviário);
- 13 - BL (Bill of Lading).

Os campos **"Série da nota"**, **"Subsérie da nota"**, **"Número do Documento Fiscal"** são campos com a funcionalidade de preenchimento de texto e possuem os seguintes limites de caracteres:

- Série da nota: 3 caracteres;
- Subsérie da nota: 2 caracteres;
- Número do Documento Fiscal: 30 caracteres.

O campo **"Data de emissão"**, deve ser preenchido com uma data.

**Observação:** se preenchido um Parceiro Emissor do Documento, um dos documentos, eletrônico ou em papel, deverá ser informado, sendo que todos os campos são de cunho obrigatório. Logo, caso os campos não sejam preenchidos, ao clicar em ![Imagem 35: Observação: se preenchido um Parceiro Emissor do Documento, um dos documentos, eletrônico ou em papel, deverá ser…](https://ajuda.sankhya.com.br/hc/article_attachments/27465233567767) **“Salvar”**, a seguinte mensagem surgirá na tela:

**“Por favor, preencha os dados do documento anterior.”**

Caso seja informado os dois tipos de documentos para o mesmo Parceiro Emissor Documento, a mensagem abaixo será apresentada, impedindo que o cadastro seja salvo.

**"Só pode ser informado um único tipo de documento anterior por parceiro, impedindo que o cadastro seja salvo."**

Assim, cadastrando apenas um tipo de documento anterior para o parceiro, ao confirmar o lançamento, e visualizar o XML do CT-e, então será gerado o subgrupo referente a informação inserida,  ou , e suas respectivas tags com o conteúdo preenchido nos campos correspondentes a cada uma, e o documento deverá ser aprovado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Eventos

Além das abas padrão do Rodapé, a Central de Vendas conta com a aba **Eventos**, destinada ao preenchimento do grupo `detalhesEvento` exigido pelo **Padrão Nacional da NFS-e** quando o serviço prestado está vinculado a um evento — shows, congressos, feiras e exposições.

Essa aba **não é exibida por padrão**. Para evitar poluição visual em empresas que não atuam nesse setor, ela precisa ser habilitada pelo usuário/consultor por meio do **Configurador de Layout** da nota:

1. Acesse o **Configurador de Layout** da Central de Vendas.
2. Localize a grade **"Eventos"** na paleta de componentes disponíveis.
3. Adicione-a ao Rodapé e salve o layout.

Após configurada, a aba fica disponível no Rodapé para os perfis desejados. Com isso, o preenchimento dos dados do evento é feito diretamente na emissão, sem necessidade de cadastros prévios para eventos pontuais.

**Campos da aba** (os marcados com \* são obrigatórios):

| Campo | Obrigatório | Descrição |
| --- | --- | --- |
| Identificador do Evento | Sim | Código/identificador do evento (ex.: `EVT2025007254180`). |
| Nome do Evento | Sim | Nome do evento (ex.: `Festival de MPB`). |
| Data de Início | Sim | Data inicial do evento. |
| Data de Fim | Sim | Data final do evento. |
| Tipo de Endereço | Não | Define a origem dos dados de endereço (ver a seguir). |

**Tipo de Endereço**

O campo **Tipo de Endereço** agiliza o preenchimento reaproveitando endereços já existentes na nota:

- **Prestador** — copia automaticamente o endereço da empresa (unidade logada); os campos ficam preenchidos e bloqueados para edição.
- **Tomador** — copia automaticamente o endereço do parceiro destinatário; os campos ficam preenchidos e bloqueados para edição.
- **Informar** — libera a digitação manual do endereço (Logradouro, Número, Bairro, Complemento, CEP e Município/UF).

Observações:

- Ao selecionar **Prestador** ou **Tomador**, se a empresa ou o parceiro não tiver endereço disponível, o sistema assume automaticamente a opção **Informar** para digitação manual.
- O bloco de endereço só é enviado à prefeitura quando o campo **Logradouro** estiver preenchido. Estando vazio, o endereço não é enviado; os demais campos, quando vazios, são enviados como `null`.

**Regras de preenchimento**

- **Um evento por nota:** é permitido apenas um evento por nota. Ao tentar incluir um segundo, o sistema exibe: "Já existe um evento de NFS-e informado para esta nota. É permitido apenas um evento por nota."
- **Período válido:** a Data de Fim deve ser igual ou maior que a Data de Início. Caso contrário, a confirmação da nota é impedida com a mensagem: "Data fim deve ser maior ou igual a Data de Início."
- **Persistência:** ao confirmar a nota, os dados informados na aba são gravados e vinculados à própria nota, preservando a informação mesmo que o endereço do parceiro seja alterado futuramente.

**Como os dados são enviados**

Ao confirmar a nota com um evento informado, o sistema gera o grupo `detalhesEvento` no JSON enviado para emissão, com as datas no formato `AAAA-MM-DD`. O sub-bloco `endereco` só é incluído quando o Logradouro está preenchido; campos sem valor são enviados como `null`. Exemplo:

```
"detalhesEvento": {
  "identificador": "EVT2025007254180",
  "nome": "Festival de MPB",
  "dataInicio": "2025-10-12",
  "dataFim": "2025-10-20",
  "endereco": {
    "logradouro": "Rua dos Andradas",
    "numero": "450",
    "complemento": null,
    "bairro": "Centro",
    "cep": "38400018"
  }
}
```

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Retenção do ICMS do Transporte

Como emitente da nota, você poderá incluir no XML da NF-e um grupo de informações chamado **Retenção do ICMS do Transporte** (tag ). Ele serve para detalhar o valor do ICMS retido sobre o serviço de transporte. Isso é essencial para que sua nota esteja conforme a lei e para que você possa recolher o imposto em nome do transportador.

Para registrar essa retenção, você verá novas opções na tela do sistema. Veja como funciona:

#### 1. Ativando os Campos de Retenção

- **Onde encontrar:** Os novos campos estarão no [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).
- Adicione a **aba Retenção do ICMS do Transporte,** assim os campos específicos para a retenção do ICMS do transporte aparecerão na tela.

#### 2. Campos para Preencher

Uma vez que você configure a nova aba na tela, os seguintes campos estarão disponíveis para preenchimento, permitindo que o sistema gere o grupo  no XML da NF-e:

|  |  |
| --- | --- |
| **Valor do Serviço** | O valor total do serviço de transporte. |
| **Base de Cálculo da Retenção** | O valor sobre o qual o imposto de ICMS será calculado para a retenção. |
| **Alíquota da Retenção** | A porcentagem do ICMS que será retida. |
| **Valor do ICMS Retido** | O valor final do ICMS que será retido. **Atenção: Este campo é chave!** **Se você preenchê-lo, todos os outros campos desta seção se tornarão obrigatórios.** |
| **CFOP** | O Código Fiscal de Operações e Prestações específico para essa operação de transporte. Você poderá escolher um da sua lista de CFOPs. |
| **Código do Município do Fato Gerador** | O código do município onde o serviço de transporte foi de fato prestado. Você poderá escolher um da sua lista de cidades cadastradas. |

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)

#### Aba Comércio Exterior

**O que é e para que serve**

A aba Comércio Exterior reúne as informações exigidas pelo layout da NFS-e Padrão Nacional na prestação de serviços para tomadores no exterior. Os campos são preenchidos automaticamente a partir do [Contrato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774) e dos cadastros de [Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553), [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) e [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), e podem ser ajustados na própria nota.

**Como acessar a aba**

- Abra a Central de Vendas (Comercial › Vendas › Central de Vendas);
- Localize ou crie uma NFS-e para um parceiro estrangeiro;
- Acesse a grade de Rodapé e clique na aba Comércio Exterior.

**Campos de preenchimento**

- **Modalidade de Prestação:** 0 - Desconhecido, 1 - Transfronteiriço, 2 - Consumo no Brasil, 3 - Mov. Temp. Pessoas Físicas, 4 - Consumo no Exterior.
- **Vínculo Prestador:** 0 - Sem vínculo, 1 - Controlada, 2 - Controladora, 3 - Coligada, 4 - Matriz, 5 - Filial, 6 - Outro, 9 - Desconhecido.
- **Apoio/Fomento do Prestador** e **Apoio/Fomento do Tomador:** mecanismos de apoio e fomento previstos pela Receita Federal, conforme as listas apresentadas nos campos.
- **Envia para MDIC:** define se a NFS-e será compartilhada com o Ministério do Desenvolvimento, Indústria, Comércio e Serviços.
- **Mov. Temporária Bens:** 0 - Desconhecido, 1 - Não, 2 - Vinculada DI, 3 - Vinculada RE.
- **Nº Declaração Importação** e **Nº Registro Exportação:** informe quando a operação estiver vinculada a DI ou a RE.
- **Moeda** e **Valor em moeda:** correspondem à moeda e ao valor do serviço em moeda estrangeira informados no cabeçalho da nota, por meio do pop-up "Cotação de moedas".

**Pontos de atenção**

- Os campos são preenchidos respeitando a ordem de prioridade Nota › Contrato › Cadastros base (Serviço, Parceiro e Empresa). O valor informado nesta aba prevalece e não é sobrescrito pelo sistema.
- Mov. Temporária Bens, Nº Declaração Importação e Nº Registro Exportação não possuem herança e devem ser informados manualmente.
- Para tomadores nacionais, as informações desta aba não são enviadas no arquivo da NFS-e.

Para saber mais, acesse o link [Emissão de NFS-e no padrão nacional para tomadores no exterior](https://ajuda.sankhya.com.br/hc/pt-br/articles/43810824811799).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Botões no topo da tela

Os botões ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16035335861655), ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15421576647191), ![Imagem 38: Os botões , , , realizam a Inclusão, Exclusão, Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402430951191), ![Imagem 39: Os botões , , , realizam a Inclusão, Exclusão, Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402430962839) realizam a Inclusão, Exclusão, Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre os botões a seguir, para saber mais sobre o comportamento de cada um deles:

|  |  |
| --- | --- |
| [mceclip0.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#criardocumentoemnovapgina) | [botao-salvar-em-pdf.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#salvarempdf) |
| [mceclip25.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas) | [mceclip2.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#confirmar) |
| [mceclip18.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#ratear) | [mceclip24.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#recalcularcustos) |
| [mceclip5.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#aprovar) | [mceclip6.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#liberaes) |
| [mceclip16.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#produtos) | [mceclip8.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#parceiros) |
| [mceclip9.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#md-e) | [mceclip10.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#aes) |
| [mceclip11.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#outrasopes) | [mceclip12.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#visualizarmapacomrotaendereo) |
| [mceclip19.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#CancelarNota) | [mceclip20.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#NF-e) |
| [mceclip21.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#NFS-e) | [mceclip22.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#CT-e) |
| [mceclip23.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#NFC-e) | [mceclip13.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#alternarentreosdocumentos) |
| [mceclip14.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#exibirhistrico) | [mceclip15.png](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#mapadeatalhos) |
| [ListadePaineis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#mostrarlistadepaineis) |  |

#### Criar documento em nova página

Acionando este botão, será aberto um novo documento sem descartar o anterior. Sendo assim, possível alternar entre os documentos que estiverem abertos através do botão [Alternar entre os documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#alternarentreosdocumentos).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Salvar em PDF

```
        Esse botão estará disponível a partir da versão 4.18.
```

Esse botão permitirá que você realize o download direto do pedido em **PDF** para agilizar o processo de vendas e orçamentos. Para isso, o campo **"Modelo de Impressão de nota fiscal"** da aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce/cfe) da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada na venda/pedido deve ser cadastrado com um modelo de impressão criado na tela [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-).

Além disso, esse download só poderá ser realizado se a nota estiver confirmada, caso contrário, ao clicar no botão ![Imagem 40: Além disso, esse download só poderá ser realizado se a nota estiver confirmada, caso contrário, ao clicar no botão…](https://ajuda.sankhya.com.br/hc/article_attachments/12557242728983) Salvar em PDF o sistema exibirá uma mensagem informando que é preciso confirmar a nota antes de imprimir. Então, o documento será salvo com o nome **"número único do pedido + nome do parceiro"**, por exemplo, **"5689-Cliente XYZ "**, mas você poderá mudá-lo.

Você também tem a opção de fazer o download de mais de um pedido simultaneamente, desde que eles já estejam confirmados. Assim, quando pedidos/notas forem selecionados, o sistema irá salvá-los em um arquivo **.zip**.

**Nota:** A funcionalidade do botão Salvar em PDF estará disponível para o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e Central de Vendas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Impressão na Central de Vendas

O botão **"Imprimir"** apresenta algumas opções para impressão e tratamento dos dados presentes na tela. Trataremos sobre cada uma delas a seguir:

[Imprimir Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#imprimirnota)                                                                            [Imprimir Pix/Boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#imprimirpix/boleto)

[Imprimir Expedição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#imprimirexpedio)                                                                  [Imprimir Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#imprimirnotaadicional)

[Desvincular Impressoras Substitutas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#desvincularimpressorassubstitutas)                                  [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#relatriosformatados)

[Exportar Registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#exportarregistros)

**Imprimir Nota**

Através desta opção será possível imprimir as notas que tem por base o formato TXT. Para imprimir uma ou mais notas em modelo TXT, você deve selecionar as notas desejadas mantendo pressionado o botão "Ctrl" do teclado, e clicar na referida opção. Vale citar que cada modelo pode ter sua particularidade.

Para uso desta funcionalidade, você deve atentar para os seguintes aspectos:

- Na configuração do [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) utilizado na nota, aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), no campo **"Modelo de impressão de nota fiscal"** informe um modelo TXT previamente cadastrado; este cadastro é realizado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913).
- O modelo informado na TOP, deve ser inserido manualmente na pasta do servidor de aplicação do Sankhya-Om. Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) você pode verificar o caminho referente à esta pasta, através do parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**; o caminho está indicado no campo **"Texto"**. Salve os modelos de TXT na pasta informada no parâmetro mencionado. Um exemplo de caminho para a configuração deste parâmetro é /home/mgeweb/modelos/, onde os modelos estão salvos na pasta modelos.

Você também pode realizar impressões de notas obedecendo à ordem da tela de seleção; para isso, ative o parâmetro **"Respeitar a ordem da grade em selec.várias Notas? - MULTSELORD"**, que uma vez habilitado fará com que as notas sejam impressas de acordo com sua ordenação/apresentação na grade. Considere o seguinte exemplo:

As notas de número 5487, 6587, 5481 e 44 não estavam ordenadas por número nota na grade e estavam sendo apresentadas conforme esta sequência informada. Ao solicitar a impressão das mesmas, com o parâmetro ativado, o sistema obedecerá a sequência que está na grade e a impressão ocorrerá na mesma ordem (5487, 6587, 5481 e 44).

Caso o parâmetro Respeitar a ordem da grade em selec.várias Notas? - MULTSELORD esteja desligado, as notas serão impressas sempre obedecendo a sequência do número nota e não a sua apresentação na grade, ou seja, ainda no exemplo citado, ao solicitar a impressão das notas 5487, 6587, 5481 e 44, as mesmas serão impressas obedecendo à numeração crescente das notas, ou seja, primeiro será impresso a nota de número 44, em seguida a 5481, a 5487 e por último a 6587, mesmo que as mesmas não estejam ordenadas pelo número da nota de forma crescente na seleção de notas na grade.

**Observação:** Para que as notas sejam impressas conforme ordenação da grade, o parâmetro **"IMPDANFEBOL - Imprimir DANFE e depois boletos?"** deve estar desligado, pois este quando ligado tem prioridade sobre o parâmetro Respeitar a ordem da grade em selec.várias Notas? - MULTSELORD.

Na geração do XML de uma NF-e e na impressão de seu respectivo DANFE, os itens da nota serão ordenados mediante a configuração realizada no parâmetro **"Ordem dos itens para impressão nas notas - ORDITENS"**; você pode ordenar os itens de acordo com sua **"Sequência"**, **"Código"**, **"Descrição"**, **"CFOP"**, entre outras alternativas. Quando definida a ordenação pela opção **"Referência do Produto"**, esta irá ocorrer desde que no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), o campo **"Referência"** esteja devidamente preenchido.

**Importante:** Vale salientar que, o parâmetro **"Ordena Itens nas Centrais? - ORDITENSCENTR"** não influência na ordenação dos itens ao realizar o faturamento. No entanto, se um dos parâmetros **"Agrupar prod. repetido em qualquer faturamento? - AGRUPFATSEMP"** e **"Agrupa produtos em comum para um item - AGRUPAPROD"** estiver habilitado, o sistema irá ordenar os itens de acordo com o seu código. Deste modo, o sistema somente manterá a ordenação dos itens escolhida, se os dois parâmetros mencionados estiverem desligados.

Além disso, o parâmetro AGRUPFATSEMP funcionará como um 'espelho' da nota de origem nas devoluções.

Exemplo:

Se na data do lançamento da nota de origem, o parâmetro estiver ligado, os itens serão agrupados e, na devolução também ficará agrupado. Todavia, se estiver desligado no lançamento da nota de origem, os itens não ficarão agrupados na devolução, mesmo se nesse momento ele estiver ligado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Imprimir Pix/Boleto**

Um boleto é um documento largamente utilizado no Brasil como instrumento de pagamento de um produto ou serviço prestado. Através do boleto, seu emissor pode receber do pagador o valor referente àquele pagamento. Tal documento pode ou não ser emitido pelo sistema no faturamento de uma Nota como forma de pagamento ou recebimento. Você deve se atentar ao fato de não ser possível emitir boletos com data de vencimento anterior a sua emissão ou com [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) "à vista".

Dentre as medidas normais para impressão de boletos, está a existência de impressoras dedicadas a esta funcionalidade. O sistema irá imprimir o Boleto para a Conta cadastrada no financeiro da nota ou do lançamento financeiro, baseando-se no modelo informado no [Cadastro da Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), campo **"Modelo"**.

Para maiores informações sobre as configurações para impressão de boletos, acesse o link [Impressão de Boletos nos Portais e Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634-Impress%C3%A3o-de-boletos-nas-centrais-Compras-Vendas-Mov-Int-).

A impressão de boletos poderá ser realizada também através do menu [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094).

Relacionada a impressão de notas e boletos, temos o parâmetro **"Imprimir DANFE e boleto agrupados? - AGRUPADANFEBOL"**, que quando habilitado, faz com que o sistema agrupe o DANFE e o Boleto, se existirem, no momento da impressão de acordo com cada nota. Com o parâmetro desabilitado, o sistema irá imprimir todos os boletos e em seguida todos os DANFE's. Esse parâmetro possui tal funcionalidade quando é utilizado o [Faturamento direto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#faturamento) do sistema.

**Nota:** A medida que as impressões de boletos e notas vão sendo realizadas, arquivos de anexos de mensagens vão sendo gerados e armazenados internamente no sistema; estes arquivos são desnecessários a partir de um certo momento para o sistema e consomem espaço significativo em disco. No parâmetro **"Dias p/ vencimento de arquivos temporários - DIASVENCTFILE"** informe o tempo que o arquivo ficará armazenado internamente. Após este período, ele será excluído para não ocupar espaço desnecessariamente.

**Observação:** Ao selecionar a marcação **"Emite"** na aba [Boletos(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), do [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), o sistema irá permitir que a impressão de boletos seja realizada na conta utilizada na operação. Porém, caso esta não esteja acionada, ao tentar realizar a impressão do boleto com a referida conta, o sistema emitirá um alerta para que você execute a conferência da marcação Emite.

**Importante:** A impressão do Boleto Cobrança Pix só poderá ser realizada por meio da opção **"Imprimir Pix"** do botão [Outras Opções..](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es). da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Imprimir Expedição**

As notas de expedição são utilizadas para controle interno de estoque e separação do material vendido; normalmente é um espelho da Nota Fiscal. A configuração da impressão da expedição é feita da seguinte maneira:

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo), campo **"Impressora"** o caminho da impressora onde será impressa a expedição; no campo **"Modelo"** informe o modelo previamente configurado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913) (para impressão de expedições, o modelo configurado pode ser na extensão TXT ou [Relatório Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados)); por fim, determine o **"Tipo de Impressora"** que será utilizado para efetuar a impressão.

Dois parâmetros influenciam na impressão da expedição, são eles:

- **Pede senha p/imprimir Expedição p/Pedidos - EXPEDSENHA:** Se este parâmetro estiver habilitado, o sistema vai solicitar a digitação do usuário e senha para efetuar a impressão da expedição no tipo de movimento em que esta for solicitada.
- **Imprimir expedição sem confirmar a nota? - IMPEXPSEMCONF:** Caso este parâmetro esteja ativado, o sistema permitirá a impressão de expedição para pedidos/notas/devoluções sem que estas estejam confirmadas. Caso esteja desligado, e seja feita a tentativa de impressão da expedição, o sistema irá emitir a seguinte mensagem:

**"Documento XXX: Para imprimir expedição, confirme  a notas antes de imprimir."**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Imprimir Nota Adicional**

A Nota Adicional é uma possibilidade de impressão de informações complementares a respeito de uma determinada nota, caso a empresa opte por utilizar controles adicionais. Pode ser uma nota adicional referente ao cupom fiscal, ou mesmo a uma nota fiscal, nota de transporte de mercadorias, ordem de separação ou um espelho da nota para o cliente.

Para realização da impressão da Nota Adicional, temos três configurações principais, a saber:

- Caso o parâmetro **"Nota Adicional por Empresa? - NOTAADICEMP"** esteja habilitado, na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) será apresentada a aba **"Estoque/Nota Adicional"**, contendo os campos para configurar o modelo e impressora para notas adicionais. Com esta configuração realizada, o sistema passará a considerar essa opção, quando a opção **"Imprimir nota adicional"** for acionada. Caso o parâmetro não esteja habilitado, o sistema irá considerar a empresa "1", buscando as informações contidas na tela Modelo e Impressora Nota Adicional, que será citada a seguir.
- Na tela [Modelo e Impressora Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597534) devem ser informados os campos **"Impressora"**, na qual você deverá informar o caminho da impressora, onde será impressa a Nota Adicional; o **"Modelo**" a ser utilizado para impressão de Notas Adicionais, que deve ser previamente configurado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913) (o modelo configurado pode ser na extensão TXT ou [Relatório Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados)); determine o **"Tipo de Impressora"** que será utilizado para efetuar a impressão; por fim, definindo pela **"Numeração Automática"**, caso no Tipo de Operação - TOP tenha sido feita a marcação para impressão da nota adicional (configuração citada a seguir), ao efetuar a confirmação da nota, a nota adicional correspondente será impressa automaticamente.
- No cadastro de [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), na aba **"Impressão"**, temos as marcações **"Imprimir Nota Adicional"** e **"Imprimir nota adicional antes de confirmada"**; com a primeira marcação, sempre que a respectiva TOP for utilizada, será acionada a rotina de impressão de Nota Adicional; caso a segunda marcação citada esteja realizada, será impressa a Nota Adicional correspondente à Nota Fiscal que não estiver confirmada.

**Nota:** É possível imprimir Notas Adicionais para mais de uma nota ao mesmo tempo; para isso, selecione mais de uma nota na grade **"Resultado da Seleção"** mantendo pressionado o botão **"Ctrl"** do teclado, e em seguida clique na opção **"Imprimir Nota Adicional"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Desvincular Impressoras Substitutas**

A opção **"Desvincular Impressoras Substitutas**" desfaz o vínculo existente entre as impressoras substitutas e a impressora cadastrada nos Modelos de Impressão.

Se ao enviar uma nova impressão, seja esta de notas ou boletos, e o pop-up para selecionar a impressora não for aberto, significa que certamente a última impressão foi feita marcando-se a opção **"Salvar Seleção?"**, o que impede a escolha de uma nova impressora. Neste caso, acessa-se esta opção de Desvincular Impressoras Substitutas, para que a impressora possa ser novamente escolhida.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Relatórios Formatados**

No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) e na Central de Vendas, no botão de impressão, a opção **"Relatórios Formatados"** irá apresentar os Relatórios Formatados vinculados a instância Cabeçalho Nota. Desse modo, todos os usuários com acesso liberado aos Portais terão acesso a estes relatórios formatados.

Os Relatórios Formatados apenas serão exibidos, caso a expressão definida no vínculo seja satisfeita. Através do link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados), você pode verificar como definir tal vínculo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

**Exportar Registros**

Esta opção realiza a baixa do XML correspondente ao documento que está sendo exibido na tela. É uma funcionalidade mais utilizada pelo nosso setor de Service Desk.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#impressonacentraldevendas)

#### Confirmar

Através deste botão realize a confirmação do documento que está sendo lançado. Todas as configurações feitas no lançamento do documento serão executadas no momento de sua confirmação, ou seja, será feita a validação do que ficou definido entre [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas) e [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), com base no [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), etc., que foram inseridos no documento em questão. É a confirmação de um documento que irá "disparar", por exemplo, sua impressão, o envio de e-mail's, a baixa, a impressão de boleto, impressão de nota adicional, faturamento da confirmação, geração da cotação, etc.

**Nota:** após realizar a confirmação do pedido de venda, se a nota já possuir liberação dos eventos [3 - Limite de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#3-limitedecrdito) e/ou [8 - Atraso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#8-atraso) e houver a alteração do Parceiro após essa confirmação, o sistema irá solicitar novamente a liberação de limites.

Realizando a marcação **"Baixa na Confirmação"**, presente na aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) do cadastro de Tipos de Negociação, ao acionar o botão **"Confirmar"**, temos em seguida a baixa do documento em questão.

**Importante:** Na confirmação da nota/pedido, para que seja realizado o cálculo de comissão antes da execução da solicitação de liberação referente ao evento [48 - Margem de Contribuição Mínima](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#48-margemdecontribuiomnima), temos as seguintes configurações:

- O parâmetro **"Antecipa calc.comissão na margem mínima? - CALCCOMMARGMIN"** deve estar ativado;
- O parâmetro **"Atualizar comissão por item? - ATUALCOMITE"** deve estar desligado.

A premissa para que o cálculo de comissão seja antecipado, é a utilização do cálculo de comissão pelo cabeçalho da nota; se for utilizada a comissão no item, a antecipação não será realizada mesmo com o parâmetro Antecipa calc.comissão na margem mínima? - CALCCOMMARGMIN ligado.

**Observação - EDI Comercial:** Para geração do **EDI Comercial** na Confirmação da Nota nas Centrais, é necessário configurar o Tipo de Operação - TOP utilizado no lançamento da Nota (aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), campo **"Modelo p/geração de EDI na confirmação**"), e o arquivo utilizado na montagem do **EDI** ([Configuração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273)). Uma vez configurado o **Arquivo Remessa** e a **TOP**, ao confirmar um lançamento, será gerado o **Arquivo de EDI** conforme caminho e modelo configurados.

**Nota:** se uma nota for confirmada sem CTe vinculado, a aba frete ficará zerada. Caso um CTe esteja vinculado, a aba frete virá populada com o valor de acordo com o CTe. Em ambos os casos o pop-up **"Movimentação Financeira - Frete"** será apresentado. Além de ser exibido também quando tratar tipo de frete igual Extra Nota, valor de frete maior que zero, código do Parceiro Transportador diferente de zero e quando a marcação **"Simulação de frete automática"** da aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) estiver desabilitada.

Para que esse pop-up não seja exibido, pode-se realizar uma das configurações abaixo:

1. Habilitar a simulação automática de frete para a TOP, ou;
2. Não importar a transportadora nas [Preferências para importação de NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimporta%C3%A7%C3%A3odenf-e).

Assim, ao confirmar uma nota com CTe vinculado, o pop-up não será exibido e o valor do frete continuará a ser populado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Ratear

Ao acionar este botão, o pop-up **"Rateando"** será exibido. Com base nos [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio) preestabelecidos, será feita a distribuição das receitas e despesas pelas Naturezas, Centros de Resultado ou Projetos.

Após a confirmação do rateio, o botão na Central de Vendas será renomeado para **"Rateado"**. Além disso, na tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), o conteúdo da coluna **"Rateio"** será atualizado para **"Sim"**.

**Observação:** o rateio só é feito se a Natureza, Centro de Resultado ou Projeto do pedido for diferente do informado no produto/grupo e seja diferente de zero.

![Imagem 41: Observação: o rateio só é feito se a Natureza, Centro de Resultado ou Projeto do pedido for diferente do informado no…](https://ajuda.sankhya.com.br/hc/article_attachments/25945868304023)

Quando o parâmetro **"Usar rateio por veículo? - RATEIOPORVEICU"** estiver habilitado, o campo **"Veículo Obrigatório"** será exibido, permitindo que o rateio seja feito com base no **Centro de Resultado vinculado ao veículo informado**.

Nesses casos, ao abrir o pop-up **"Rateando"**:

- O campo **"Centro de Resultado"** será **bloqueado para edição** **somente** quando o parâmetro **RATEIOPORVEICU** estiver habilitado e o veículo informado possuir um Centro de Resultado previamente definido.
- Nessa situação, o sistema utilizará automaticamente o Centro de Resultado do veículo, impedindo alterações manuais — comportamento alinhado ao sistema Flex.

![Imagem 42: Para acessar essa funcionalidade na Central de Vendas do Portal de Pedidos , o usuário deve ter a permissão "Rateio" da…](https://ajuda.sankhya.com.br/hc/article_attachments/25834717844887) Para acessar essa funcionalidade na Central de Vendas do [Portal de Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609994), o usuário deve ter a permissão **"Rateio"** da tela Portal de Pedidos, configurada na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854).

**Nota:** quando o parâmetro **"Copiar Rateio no Faturamento/Devolução? - COPIARATCEN"** estiver ativado, ao faturar um Pedido de Venda no Portal de Pedidos, o rateio será transferido para o novo pedido gerado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Recalcular Custos

O acionamento deste botão, efetua o recálculo dos custos e/ou preços conforme definidos no Tipo de Operação - TOP. Esta é uma ferramenta que permite a realização do recálculo de custos de produtos, a partir de movimentações de entrada como, Notas de compra, Devolução de Venda, Transferência. Tal funcionalidade é útil em casos de alterações em fórmulas de precificação (fórmulas de custo/preço) necessárias devido a redefinições em políticas de custeio e precificação. Caso haja a necessidade de se refazer custos de produtos em consequência de erros de lançamento de uma Nota Fiscal, por exemplo, você pode utilizar esta ferramenta.

**Observação:** O parâmetro **"Calcula Custo Médio na C.A.Fornecedor na Confirmação? - CALCCUSTOMEDCAF"**, quando acionado, e for utilizada esta opção de Recalcular Custos, além de calcular o custo de entrada, também vai calcular o custo médio. Se desativado, o processo de confirmação ficará mais ágil, pois ao não calcular o custo médio, não é feita uma leitura de estoque, entradas e saídas, na confirmação da nota, processo este realizado na realização do referido cálculo.

**Importante:** Quando o parâmetro **"Recalcula preços quando altera Tipo de Negociação: - RECPRECOTPV"** estiver com a opção **"Nunca"** selecionada e o campo TIPLANCNOTA com a opção diferente de 'Q' na tabela TGFPRO do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), o valor do produto não será recalculado ao alterar o Parceiro na Central de Vendas.

\*\*Observação:\*\*Com o parâmetro RECPRECOTPV configurado com a opção **"Sempre"** e na tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#top), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), o campo **"Tipo da Taxa"**, estiver selecionado com a opção **"Juro taxa Única"**, ao realizar a troca do Tipo de Negociação em um lançamento em moeda, tanto no tipo de título anterior quanto no novo o sistema irá realizar o recálculo dos valores zerando o desconto da moeda.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Aprovar

O botão **"Aprovar"** é habilitado para uso, em Notas de Venda não confirmadas e não aprovadas, cujo Tipo de Operação - TOP utilizado em seu lançamento for do Tipo de Movimento "Venda" e em sua configuração na aba **"Geral"**, tem-se a marcação **"TOP de Cupom Fiscal"** realizada. Além disso, na opção **"Controle de Numeração"** localizada no botão **"Outras opções..."** desta mesma TOP, é necessário que tenha cadastrada uma série CF para a empresa que será utilizada no lançamento.

O acionamento deste botão, ativa no sistema as validações de confirmação de nota e a posiciona como **"Aprovada"**; a nota não é numerada. Sua numeração ocorre na confirmação do Cupom, procedimento este, realizado no Fast Service. O botão Aprovar está ligado às rotinas de lançamento de Pedido DAV e Pré-Venda.

Quando se tratar somente da emissão de NFC-e, o botão Aprovar será habilitado nos documentos não confirmados e não aprovados, cujo Tipo de operação - TOP empregado no seu lançamento seja do Tipo de Movimento **"Venda"**, em sua configuração na aba **"Livro Fiscal"**, o campo **"Modelo do Documento"** esteja assinalado como **"Nota Fiscal de Venda ao Consumidor"** e na aba **"Validações"**, o campo **"Nunca incluir Confirmada"** se encontre marcado. Além disso, deve existir um vínculo com um pedido de venda do qual seu Tipo de operação - TOP contenha na aba **"Impressão"**, o campo **"Base numeração"** indicado como **"DAV cupom fiscal"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Liberações

O Botão **"Liberações"** será apresentado habilitado e o atalho **"Ctrl+Shift+L"** também pode ser utilizado para acioná-lo, somente funcionarão quando o documento já estiver salvo e não estiver confirmado. Mesmo que o usuário não possua acesso a tela de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites), esse botão ficará habilitado, pois a tela exige a digitação de usuário e senha. Somente serão exibidas as liberações de limites correspondentes às liberações cadastradas para o usuário que digitou a senha.

Um exemplo de uso deste botão que acontece muito frequentemente, é no momento da confirmação de uma nota, tem-se a solicitação de alguma liberação de limite; o usuário aciona o gerente que pode liberar aquela solicitação e ele clicando no botão Liberações digita o usuário e senha, efetua a liberação e retorna para a Central de Compras para que o usuário proceda com a confirmação da nota.

**Observação:** Para evitar que a liberação de limites ocorra de forma indevida ao clicar duas vezes sobre o registro na tela de Liberação de Limites, ligue o parâmetro **"Na Liberação de Limites, avisar no duplo clique - AVISACLIQUELIB"**, assim, o sistema exibirá o pop-up Liberar Limites para que o evento solicitado seja analisado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Produtos

O acionamento deste botão, abre o Catálogo de Produtos, ou seja, tem a visualização da tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos). Este botão tem por objetivo, facilitar a busca e identificação de itens, para sua posterior inserção no documento que está sendo lançado. Clicando em qualquer campo de uma das três grades ([Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho), [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)) e utilizando as teclas de atalho **"Ctrl + Alt + P"**, também será aberta a tela de Consulta de Produtos.

Uma vez na tela Consulta de Produtos, quando o cursor estiver posicionado em algum campo, ao pressionar no teclado as teclas de atalho **"Ctrl + Q"**, temos o posicionamento do cursor no campo de preenchimento da Quantidade na grade Detalhes de estoque, de modo que será possível informar a quantidade antes da inclusão no carrinho de compras.

**Nota:** Na Consulta de Produtos, aberta ao pesquisar um produto na Central de Vendas, podemos acrescentar um critério adicional que permitirá que você filtre os produtos da consulta de acordo com a Nota/Pedido selecionados. Esta modificação requer um nível de conhecimento avançado.

Primeiramente, você deve configurar o parâmetro **"Critério adicional para catálogo de produtos - QRYCONSPROD"**. Nele, coloque o pedaço da cláusula **"WHERE"** que irá filtrar os produtos. Nesse WHERE estará disponível o parâmetro **"NUNOTA"** que representa a nota selecionada na Central.

Exemplo 1:

```
"AND ((TGFPRO.CODGRUPOPROD = 100 AND 'P' = (SELECT TIPMOV FROM TGFCAB WHERE NUNOTA
 = :NUNOTA)) OR ('P' != (SELECT TIPMOV FROM TGFCAB WHERE NUNOTA = :NUNOTA)))"
```

O critério adicional acima faz com que sejam apresentados na consulta de produtos de todos os PedidosdeVenda('P'), somente produtos que pertençam ao Grupo de Produtos de código 100.

Exemplo 2:

```
AND ((TGFPRO.CODVOL = ‘CX’ AND 102000 = (SELECT CODCENCUS FROM TGFCAB WHERE
NUNOTA= :NUNOTA)) OR ('102000'!= (SELECT CODCENCUS FROM TGFCAB WHERE NUNOTA
=:NUNOTA)))
```

O critério adicional acima faz com que sejam apresentados na consulta de produtos das Notas/Pedidos/Requisições que tenham Centro de Resultado=102000, somente produtos que tem Unidade Padrão=CX.

Após configuração do parâmetro de Critério adicional para catálogo de produtos - QRYCONSPROD, a Consulta de Produtos aberta pelas Centrais já irá considerá-lo no filtro.

**Importante:** A [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos), quando abertanão considera o critério definido nesse parâmetro, ela sempre apresenta todos os Produtos/Serviços.

Ainda sobre a Consulta de Produtos aberta partindo-se da Central de Vendas, ao realizar a inclusão de itens no carrinho de compras, caso ocorra alguma falha nos navegadores de internet ou falta de conexão inesperada, os dados inseridos no carrinho permanecerão guardados no navegador durante os 5 (cinco) dias seguintes; finalizado esse período, os dados são descartados automaticamente. O comportamento resultante desse armazenamento no navegador, ocorre ao acessar novamente a Central de Vendas e consequentemente o documento que estava sendo trabalhado; será exibida a seguinte mensagem:

**"Encontramos um carrinho não finalizado, deseja utilizá-lo?"**

Se você escolher por utilizar os dados já presentes no carrinho, será dada continuidade no processo, adicionando os produtos à grade de itens correspondente. Mas se decidir por não utilizar as informações já contidas no carrinho, estes serão apagados, e um novo carrinho de compras poderá ser elaborado. Este comportamento irá ocorrer, caso seja feito o acesso ao mesmo navegador que estava aberto anteriormente; abrindo um navegador diferente, as informações não serão mantidas no carrinho.

**Importante:** Para que seja realizada a Consulta de Produtos por meio da Central de Vendas, considerando que os parâmetros **"Mostrar impostos na Consulta de Produtos? - MOSTIMPCONSPROD"** e **"Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE"** estejam configurados, é preciso que o campo "NCM" tenha sido devidamente cadastrado no sistema, de acordo com as especificações contidas na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral).

Será possível registrar os itens adicionados no carrinho por termos consultados; para isto, o parâmetro **"Procedure para registrar consulta de produtos - NOMPROCREGPROD"** deve estar configurado com a procedure que foi criada pelo consultor ou implantador.

Neste contexto, após configurada a procedure, o sistema realizará a consulta e retornará esta. Neste retorno, temos o campo **"AD\_IDCONSULTA"** (estará localizado na tabela onde foi criada a procedure) que identificará a consulta realizada, apresentando seu resultado; a partir disto, toda inclusão de produtos no carrinho receberá o mesmo campo identificador, que foi gerado anteriormente. Caso uma nova consulta for realizada, será gerado um novo identificador e este estará vinculado à novas inclusões no carrinho.

**Observação:** Dentro do carrinho de compras, ocorrerão algumas validações do [Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603054) desde que as configurações abaixo tenham sido anteriormente realizadas:

- Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), a marcação **"Usar Créd. Flex?"** deve estar selecionada;
- O parâmetro **"Utiliza campos adicionais no carrinho? - USACAMPOSADCCAR"** deve estar habilitado;
- Na tela [Tabelas de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os), o campo **"Preço"** deverá possuir um valor configurado;
- No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito), a marcação **"Usar Créd. Flex?"** deve estar selecionada;
- E, por fim, a [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) deverá apresentar, em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), o campo **"Atualizar Acréscimos/Decréscimos"** igual a **"Saldo Disponível"** ou **"Provisão de Acréscimo"**.

Desta forma, você lançará um pedido/nota e, ao realizar a pesquisa do produto desejado na Consulta de Produtos, irá adicioná-lo ao carrinho de compras; você terá então, a possibilidade de aumentar ou reduzir o valor unitário do produto dentro do carrinho de compras e, de acordo com as regras do flex configuradas anteriormente, poderá gerar o saldo ou desconto no flex.

O campo **"Vlr Acresc/Desc"** apenas será exibido quando o parâmetro Utiliza campos adicionais no carrinho? **-** USACAMPOSADCCAR estiver ligado e for pela Central de Notas.

O campo **"Últ. Vlr. Venda"**, exibido na grade **Produtos no carrinho**, apresenta o valor bruto da última venda realizada para o produto, desconsiderando descontos e impostos aplicados na operação.

**Importante:** O campo Vlr Acresc/Desc não é atualizado na distribuição automática de descontos inseridos diretamente no rodapé da nota, independente dos parâmetros DISTJDCONF ou DISTDESCNFE estarem ligados ou não. O mesmo apenas é atualizado.

Abaixo, temos algumas validações disparadas:

- O Acréscimo Flex (X) excedeu o Limite (X) do Produto X;
- O Desconto Flex (X) excedeu o Limite (X) do Produto X;
- O valor do desconto excedeu o saldo disponível do Parceiro X;
- Ao excluir um item que deixará o Saldo Flex negativo, será exibida a mensagem: **"A exclusão deixará o saldo disponível do (vendedor/parceiro) X negativo"**;
- Ao alterar o valor de um item que deixará o Saldo Flex negativo, será apresentado a mensagem: **"O valor do desconto excedeu o saldo disponível do (vendedor/parceiro) X"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Parceiros

O acionamento deste botão, abre a tela [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934) já posicionada nas informações pertinentes ao [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) informado no documento. Note na Ficha de Parceiros que é aberta, o botão **"Usar parceiro"** que ao ser acionado, o Parceiro em questão será inserido no documento que está sendo lançado na Central de Vendas; esta inserção do Parceiro na Central também pode ser feita por meio do atalho **"Ctrl + Shift + U"**.

**Nota:** A referida tela quando aberta pela Central de Vendas, permite pesquisar somente parceiros condizentes com a definição do campo **"Tipo"** presente na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), ou seja, para os movimentos de Nota de Venda, Pedido de Venda e Conhecimento de Transporte será filtrado o parceiro do tipo Cliente e para o movimento de Devolução de Venda os parceiros do tipo Fornecedor e Cliente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### MD-e

O botão **"MD-e"**, é peça chave na utilização da rotina [Manifestação do Destinatário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112353); ele possui as seguintes opções:

- **Ciência da operação:** Registra o evento de ciência de operação para a nota fiscal lançada na Central;
- **Confirmo a operação:** Fixa o evento de Confirmação de Operação para a nota fiscal lançada na Central;
- **Desconheço a operação:** Registra o evento de Desconhecimento de Operação para a Nota Fiscal lançada na Central;
- **Operação não realizada:** Determina o evento de Operação não Realizada para a nota fiscal lançada na Central;
- **Prestação de Serviço em Desacordo:** A prestação de serviço em desacordo é uma funcionalidade destinada ao tomador de serviço, ou seja, o responsável pelo pagamento do serviço de frete. Essa ação será realizada caso o CT-e emitido possua informações indevidas ou conflitantes entre o serviço realizado e o descrito no documento XML.

Sendo que, para que os dados possam ser corrigidos e o documento substituído, as seguintes etapas do processo deverão ser seguidas:

1. O tomador de serviço deve manifestar o evento de Prestação de Serviço em Desacordo com uma justificativa válida;
2. A Transportadora tem que emitir um CT-e substituto referenciando o CT-e anulado.
3. O Prazo para registrar este evento é de até 45 dias a partir da data da autorização do CT-e original. A regularização através do CT-e substituto e CT-e de anulação deve se estender por no máximo 60 dias da autorização.

- **Visualizar manifestos:** Por meio desta opção, será aberto um pop-up, na qual é possível consultar os eventos relacionados à Manifestação do Destinatário.

**Importante:** Esta opção está disponível somente para as notas de Devolução de Venda.

- **Visualizar eventos DF-e:** Este serviço tem por finalidade à distribuição de informações resumidas e documentos fiscais eletrônicos de interesse do cliente, seja este uma pessoa física ou jurídica.

**Importante:** Para que estas opções sejam apresentadas no menu do botão MD-e, é necessário que o parâmetro **"Controla acessos dos eventos do MD-e? - ACESSOEVENTOMDE"** esteja ligado, além disso, na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), os usuários devem estar com os acessos especiais concedidos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Ações

Através deste botão, tem-se a escolha das ações configuradas previamente na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294). Estas ações são configuradas de acordo com a rotina e processo de cada empresa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Outras Opções

Podemos notar a presença deste botão no alto da tela e no topo da grade de Itens. As opções contidas em cada um dos botões, podem ser acessadas por meio dos link's [Central de Vendas | Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234-Central-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) e [Central de Vendas | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374), respectivamente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Visualizar mapa com rota/endereço

Através deste botão, você realiza a análise da localização do **"Endereço de entrega"** e do **"Endereço do parceiro"** (endereço principal), bem como as **"Rotas"** do endereço da empresa com base nos endereços de entrega principal do Parceiro. Ao acionar uma das duas opções deste botão, será aberta a tela **"Configurações > Consulta > Mapa Visualizador de Endereços"** onde será possível visualizar o ponto referente ao endereço escolhido (principal ou de entrega).

As informações necessárias para se efetuar as configurações de integração do botão **"Visualizar mapa com rota/endereço"** com a ferramenta Google Maps, podem ser visualizadas através do link [Como configurar o botão Mapas Integrado ao Google Maps](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#comoconfigurarobotomapasaogooglemaps).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Cancelar Nota

O acionamento deste botão invalida o documento. Você pode obter mais informações acerca deste processo nos link's [O que é Cancelar uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#oqueumanotafiscaldevenda) e [Como realizar o Cancelamento de uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#comorealizarocancelamentodeumanotafiscal).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Opções para Nota Fiscal Eletrônica

Temos através deste botão, todas as opções acerca das [Notas Fiscais Eletrônicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110633-Nota-Fiscal-Eletr%C3%B4nica). No uso do Tipo de Movimento **"Canceladas"**, este botão é habilitado caso algum documento seja selecionado na grade Resultado da seleção.

**Observação:** Ao selecionar uma nota que esteja com o **"Status NF-e" = "Aguardando Correção"** e clicando na opção **"Gerar lote"** disponível neste botão, caso a data e/ou hora estejam diferentes da data e/ou hora do servidor, o parâmetro **"Obriga Dt.Negoc. ser igual a do servidor? - DTNEGSERV"** terá o seguinte comportamento:

- Encontrando-se habilitado, será realizada a alteração da data e/ou hora do documento de forma automática.
- Caso encontre-se desabilitado, será apresentado um pop-up te questionando se você deseja manter a data e/ou hora do documento ou se deseja ajustar estas informações para que estejam de acordo com as informações do servidor.

Desta forma, será possível alterar as datas de negociação, faturamento e entrada/saída de acordo com o mesmo comportamento, ao realizar a confirmação de uma nota com data diferente do servidor na Central de Vendas.

**Importante:** Realize a atualização destas datas e horas pois, se um boleto estiver vinculado à estas datas e for efetuado a correção do cadastro dias depois, a nota e o boleto serão recebidos com datas de saídas incorretas, ocasionando a perda do prazo negociado.

Em relação à opção **"Enviar XML da NF-e/CC-e e Danfe por e-mail"** disponível neste botão, quando esta for selecionada, será enviado ao e-mail cadastrado o XML da NF-e e CC-e, o PDF da NF-e (DANFe) e, também, o PDF da **"Carta de Correção"**, caso exista alguma gerada.

**Nota:** Se você utilizar esta rotina sem um modelo de impressão de Carta de Correção inserido na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), campo **"Relatório Carta de Correção"**, o sistema não encaminhará o PDF no e-mail e não emitirá qualquer mensagem de aviso.

No Portal de Vendas, ao gerar uma nota em EPEC com o parâmetro **"Utiliza informação imposto da NFe para EPEC? - USAIMPNFEEPEC"** ligado, será utilizado para compor a tag  do EPEC, o mesmo valor do vICMS de uma NF-e normal.

**Observação:** Quando o parâmetro **"Imprimir os XMLs processados pelo SanNFe no log? - DEBUGXMLSANNFE"** estiver ligado, fará com que o sistema passe a imprimir os xmls completos de requisição e retorno no log.

**Nota:** Caso você tente realizar a impressão de um documento fiscal que esteja com status que não permite impressão, será apresentado um aviso, por exemplo:

**“Documento XXX: Nota com status DENEGADA não pode ser impressa, favor verificar o documento. NFe ignorada na impressão.”**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Opções para Nota Fiscal Eletrônica de Serviços

Por meio deste botão, temos acesso às opções que podem ser utilizadas quando realizado o lançamento de uma [Nota Fiscal Eletrônica de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Opções para Conhecimento de Transporte Eletrônico

Este botão exibe as alternativas relacionadas ao [CT-e - Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e).

**Observação:** Inserindo um CNPJ nas configurações do parâmetro **"CNPJ ANTT p/ autorização de download de XML. - CNPJANTT"**, ao **"Gerar o Arquivo XML de CT-e para conferência"** através deste botão, será possível visualizar na tag  deste arquivo o mesmo CNPJ inicialmente configurado no parâmetro.

**Nota:** Será possível realizar a impressão da Carta de Correção CT-e selecionando a opção **"Imprimir a Carta de Correção"** localizada neste botão; para isto, você deve, primeiramente, baixar o modelo de impressão através da tela [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-), botão **"Baixar Modelos Padrões"**, opção **"Carta de Correção CT-e"** e, após, inserir o mesmo no campo **"Relatório Carta de Correção"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abact-e).

Através da opção **"Comprovante Entrega CTe"** disponível neste botão, será possível indicar que a entrega da carga foi efetivada pelo transportador; assim, o sistema irá gerar e transmitir o evento que será vinculado ao CT-e e propagado nas notas fiscais eletrônicas relacionadas de forma automática.

Ainda neste botão, temos a opção **"Cancelar Comprovante Entrega CTe"**, que deverá ser selecionada caso haja necessidade de cancelar o evento de Comprovante de Entrega de CT-e anteriormente vinculado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Opções para Nota Fiscal Consumidor Eletrônica

Através deste botão, teremos acesso às opções utilizadas ao lançar uma [NFC-e Nota Fiscal de Consumidor Eletrônica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Alternar entre os documentos

Este botão é exibido quando forem abertos na tela mais de um documento; através dele será possível intercalar a visualização dos documentos que se encontram abertos.

Quando acionado, temos a exibição de um pop-up de mesma nomenclatura contendo os referidos documentos. Podemos verificar no lado superior esquerdo do pop-up o campo **"Buscar no histórico"**, quando existirem vários documentos abertos este botão permitirá efetuar a busca de um determinado documento através do seu Nro. Único.

Além disso, na parte superior direita do pop-up tem-se um contador de registros que irá auxiliar na identificação do número de documentos que se encontram abertos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Exibir Histórico

Este botão exibe o pop-up **"Histórico de documentos abertos"**, nele são apresentados os registros dos documentos que foram fechados recentemente até o último que deve estar em execução. Se trata de um histórico temporário que se inicia desde a abertura da central até o seu o último documento. Esta ferramenta só exibirá o histórico do usuário que está logado e permitirá assim o resgate destes registros que já foram fechados, possibilitando assim sua manutenção ou simples conferência. Para visualização do registro desejado basta um clique que o mesmo será carregado na central.

Podemos verificar no lado superior esquerdo do pop-up o campo **"Buscar no histórico"**, quando existirem vários documentos abertos este botão permitirá a busca de um determinado documento pelo seu Nro. Único.

Além disso, na parte superior direita do pop-up temos um contador de registros que vai auxiliar na identificação do número de documentos que se encontram abertos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Mostrar lista de painéis

Localizado no lado superior direito da tela, este botão exibe a listagem dos painéis que compõem a tela Central de Vendas. Ao clicar na opção desejada, o sistema direciona o foco para a mesma.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela)

#### Mapa de atalhos

Além das opções até aqui citadas, que podem ser acessadas via botões, você pode realizar  também através atalhos do teclado. Esta opção, assim como a anterior, se encontra no lado superior direito da Central de Vendas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#botesnotopodatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Como lançar um documento na Central de Vendas?

Tomaremos como exemplo neste tópico, o lançamento de uma Nota de Venda na Central de Vendas; os demais documentos trabalhados nesta tela (Pedido de Venda, Devolução de Venda e Conhecimento de Transporte Eletrônico), seguem o mesmo padrão de lançamento, diferenciando basicamente nas validações fiscais, de estoque e financeiro que podem realizar. Os dados fundamentais que deverão existir no sistema, são:

- É necessário que se tenha, o [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas); em seguida as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), onde definimos as particularidades de cada corporação no sistema, bem como, se a mesma estará ativa para uso nesta e nas demais rotinas, respectivamente;
- O [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494) na Nota de Venda, é o Cliente para o qual a empresa cadastrada inicialmente está concretizando a venda;
- O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) assim como em todas as operações, é um cadastro de extrema importância, pois determina o Tipo de Movimento (que em uma Nota de Venda, é V-Venda), as atualizações de Financeiro, Estoque, Matérias-Primas, Preços, entre outros aspectos;
- É essencial o cadastro do [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), ou seja, a forma de pagamento feita entre a empresa e o cliente;
- Por fim, efetue o cadastro dos [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) que serão ofertados ao Cliente.

Uma vez cadastradas essas informações, como citado inicialmente nesta documentação, a Central de Vendas não é aberta diretamente; é necessário que esteja posicionado no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) para que você o execute.

Com base nessa informação, ao acessar o Portal de Vendas e acionar o botão ![clip5908](https://ajuda.sankhya.com.br/hc/article_attachments/360061943373), será aberta a Central de Vendas para início do lançamento.

Exceto os Produtos, os demais cadastros mencionados acima, deverão obrigatoriamente compor o [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) da nota. Os outros campos devem ser informados, de acordo com o processo escolhido por cada empresa. Ao finalizar esta etapa do lançamento e salvar as inclusões, será habilitada a grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) para inclusão dos produtos negociados entre Empresa e Cliente.

**Observação:** Os parâmetros **"Aceitar prod.repetido para Exec.diferente?-ACEITARPRODREPE"** e **"Aceitar produto repetido-ACEITARPRODREP"** quando habilitados, permitem que seja inserida mais de uma linha do mesmo produto no documento. Ainda nesse contexto, considerando que seja inserido o mesmo produto, porém com local de origem e/ou controles diferentes, a inclusão de forma repetida será permitida, independente dos parâmetros mencionados.

As abas apresentadas na grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) terão algumas informações alimentadas automaticamente (de acordo com os dados inseridos na grade Cabeçalho e na grade Itens da Nota) e outras deverão ser preenchidas de acordo com o processo de cada empresa.

Finalizadas as inserções, concluímos o lançamento por meio do botão[Confirmar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#confirmar) localizado no alto da tela.

Um lançamento também pode ser iniciado pela própria Central de Vendas; quando um documento já estiver aberto e este não será mais trabalhado, o botão de Inclusão prepara e habilita a tela para um novo lançamento.

**Observação:** O ato de duplicar um documento, também abre a Central de Vendas, porém todos os preenchimentos citados até aqui já se encontrarão realizados, bastando apenas (caso nenhuma modificação seja necessária) [Confirmar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#confirmar) o documento em questão.

Finalizado o lançamento da nota, formulando os filtros corretos, esta poderá ser visualizada na grade Resultado da Seleção no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) e com um duplo clique sobre o documento, você pode analisá-lo na própria Central de Vendas.

**Observação:** Caso você realize um pedido de venda DAV, sendo este finalizado no [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056765053-Processos-de-vendas) e algum dos itens desse pedido permanecer como pendente, carregue-o novamente no Checkout para que o seu faturamento seja finalizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Cadastro Simplificado de Parceiros

Os Parceiros são todas as pessoas físicas ou jurídicas que se relacionam de alguma forma com a empresa. Qualquer organização que comercialize bens e serviços com a empresa. A integração das informações de clientes, fornecedores, representantes etc, traduz a adoção de maior foco sobre os dados fundamentais destes clientes e fornecedores, no sentido de constituir todas as fontes de dados existentes na empresa.

Deste modo, no lançamento de um Pedido de venda, Nota de venda, Devolução de venda ou Conhecimento de Transporte o nosso sistema disponibiliza uma forma rápida e prática de se efetuar um cadastro simplificado de um novo parceiro. Para tanto, é necessário acionar a tecla **"F2"** no ato de preenchimento dos dados.

**Observação:** Ao acionar a tecla **"F2"** posicionado em um pedido, nota ou devolução que já esteja com a grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) preenchida, o pop-up **"Cadastro simplificado de parceiros"** será apresentado com os dados do parceiro já cadastrado.

As informações referentes as abas apresentadas e o botão **"Outras opções"**, devem ser verificadas no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).

**Nota:** se o parâmetro **"Parceiro F2 ignora controle de acesso do cad. parceiro? - IGNORACESPARCF2"** estiver desligado, só será possível acessar o pop-up Cadastro simplificado de parceiros quando o usuário tiver os devidos [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) de edição da tela de [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros). Caso contrário, com o parâmetro habilitado, será possível editar o pop-up de parceiro simplificado sem qualquer permissão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

## Parâmetros que atuam na Central de Vendas

**Financeiro Nota fiscal diferente da nota - NFEFINDIFNOTA:** este parâmetro realiza uma tratativa no caso onde o valor do financeiro é diferente da nota na geração do XML. Sendo assim, ele pode ser configurado com os seguintes valores:

1. Considerar como desconto e sem pagamento: a diferença entra como valor de desconto sem afetar o valor total da nota;
2. Distribuir diferença entre financeiros: se parcela única, é definido o valor da nota como valor da duplicata; caso tenha mais de um financeiro, o seu valor será retirado do valor da nota;
3. Considerar como desconto: a diferença entra como valor de desconto sem afetar o valor total da nota.

**Integridade casas decimais XML Portal Import - INTEGRDECIMXML:** com este parâmetro ligado, o arredondamento de casas decimais do índice é desabilitado automaticamente, carregando assim toda a dizima periódica para o cálculo. Sendo que, esse processo só ocorrerá quando se tratar de uma nota importada pelo [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) e houver explosão de lote na importação. Por padrão, este parâmetro está ligado. Para habilitar a funcionalidade mencionada, é necessário desligá-lo.

**Aceitar desconto negativo na geracao Xml? - VLDSCNEGGERXML:** este parâmetro permite que sejam considerados valores negativos ao calcular os descontos na geração do XML.

**Inclusão facilitada de produtos controlados por lista? - INCFACPROLIS:** este parâmetro habilita uma segunda aba na grade de Itens, denominada **"Facilitado"**; ela visa facilitar o lançamento de produtos controlados por Lista.

**Qtd. máx. de Centrais abertas - MAXCENTRAIS:** nesse parâmetro, definimos uma quantidade máxima de documentos que poderão ser abertos simultaneamente na Central. Ao exceder este limite será exibido o pop-up **"Quantidade máxima de documentos atingidos"** com a mensagem:

**"A quantidade máxima de X documento(s) aberto(s) simultaneamente foi atingida. Selecione um documento para ser substituído."**

Quando a quantidade definida for 1 (um) registro o sistema irá substituir automaticamente o registro atual pelo registro anterior. Sendo que, se o registro atual possuir alterações, a seguinte mensagem será apresentada:

**"O registro atual foi alterado, deseja salvar as alterações?"**

Após a seleção, o novo documento será carregado na Central.

**Taxa do Tipo Negociação afeta TOP c/ultimo custo? - TAXINCCUST:** o funcionamento deste parâmetro depende das seguintes configurações:

- No Cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), o campo **"Usar como preço"** selecionado com a opção **"Último custo de reposição"**;
- O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) em sua aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), o campo **"Taxa em %"** deve estar preenchido e o campo **"Apresentação da taxa"** marcado como **"Incluir no preço do produto"**.

Estando habilitado o referido parâmetro e as configurações acima efetuadas, o sistema incluirá o valor da taxa informada no valor do produto (último custo de reposição).

**Validar executante ativo no item da nota? - VALEXECITEM:** Habilitando este parâmetro, o sistema irá verificar se o código do Vend./Executante informado no campo **"Executante"** da grade **"Itens"** está ativo. Caso o mesmo se encontre inativo, a seguinte mensagem será exibida:

**"Vendedor não existe ou não pode ser usado aqui: PK[11]."**

**Permitir Dt. Faturamento anterior Dt. Negociação? - PERDTFATANDTNEG:** podem ocorrer situações em que no lançamento de notas, a data de faturamento tenha que ser anterior à data de negociação. Para estes casos, temos o referido parâmetro que por padrão é apresentado desligado; ao ser acionado, ele irá efetuar o lançamento de notas em que sua data de faturamento é anterior a data de negociação.

**Alterar rateio nota confirmada sem validar metas? - ALTRATSEMVALMET:** este parâmetro permite alterar o rateio de notas confirmadas sem que ocorra a validação de metas.

**Bloquear rateio negativo - BLOQRATNEG:** quando este parâmetro estiver ligado, o sistema irá bloquear o rateio acima de 100% ou abaixo de 0%.

**Procedure para definição da unidade - NOMPROCDEFUNID:** este parâmetro permite a utilização de uma procedure para definição da unidade padrão do produto no processo de venda. A procedure deve obedecer um padrão de assinatura, recebendo um único parâmetro de entrada (p\_IdSessao) e de saída (p\_Result) do tipo VARCHAR2. O parâmetro de entrada é o ID da sessão com o qual você pode obter outros parâmetros, que são injetados no momento da inicialização do produto.

O parâmetro de saída é o próprio código do volume que será utilizado pelo sistema. Caso a procedure retorne NULL, o sistema continuará utilizando a inicialização padrão. Se retornar um código de volume inapropriado para o produto, a seguinte mensagem será apresentada:

**"O volume X informado não é válido para este produto Y e controle Z."**

Esta funcionalidade atende os seguintes processos de venda:

- Pedido Web;
- Pedido de Venda;
- Venda;
- Devolução de Venda.

**Importante:** Aconselhamos que a configuração deste parâmetro seja efetuada por usuários avançados do sistema Sankhya Om.

**Transferir valor do desconto para o campo destaque - TRANSFDESCDEST:** este parâmetro por padrão se encontra habilitado, tendo como funcionalidade retirar o valor negativo contido no campo **"Desconto total por item"** deixando-o zerado e assim transferi-lo positivamente para o campo **"Vlr. Destaque"**; ambos localizados no [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) da nota. Caso esteja desligado, não ocorrerá a transferência dos valores. Sendo que, este parâmetro é aplicado em notas de devolução.

**Valida acesso alterações em notas não confirmadas - VALACESSONOTA:** define se o sistema verifica o acesso **Alterar** da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos#parametrosqueinfluenciamosacessos) antes de permitir alterações em notas não confirmadas.

- **Ligado:** o usuário só consegue alterar a nota se tiver o acesso **Alterar** liberado. Sem esse acesso, o sistema bloqueia a alteração e exibe a mensagem "O usuário logado não possui permissão para alterar o documento 'Nota de venda'".
- **Desligado:** o sistema não verifica o acesso **Alterar**. O usuário consegue alterar a nota mesmo sem essa permissão.

**Importante:** com o parâmetro ligado, incluir um item na nota também conta como alteração, porque o sistema recalcula os valores do cabeçalho. Por isso, o usuário que precisa incluir itens deve ter os acessos **Incluir** e **Alterar** liberados.

**Arredondar desconto p/2 casas decimais? - DECDESC2:** este parâmetro quando habilitado, força o arredondamento dos valores para duas casas decimais, desconsiderando o número de casas do produto e do volume alternativo. Em casos de utilização de desconto com mais de duas casas decimais nos itens, poderá ocorrer uma diferença de valores entre a base do ICMS e o valor total da nota devido ao arredondamento. Portanto, nesta situação, é necessário habilitar este parâmetro para que os valores sejam ajustados.

**Nota:** Mesmo com este parâmetro habilitado, o arredondamento não funcionará quando houver a duplicação de nota.

Tem-se ainda, o parâmetro **"Arredonda o valor do desconto unitário do item - ARREDDESCITE"** que, estando ligado, também arredonda para duas casas decimais o valor do desconto unitário do item da nota. Porém, realizando o cálculo de forma diferente; primeiramente divide o desconto pela quantidade, arredondando pelo método normal e, em seguida, multiplica novamente pela quantidade, arredondando para duas casas decimais.

|  |
| --- |
| `curVlrDesc=getRounded(getRounded(curVlrDesc / QTDNEG, getCasasDecimais) * QTDNEG,2)` |

**Importante:** Quando o parâmetro **ARREDDESCITE** estiver ligado, será alterado o comportamento do cálculo de descontos, causando um arredondamento antes da aplicação do percentual, o que pode influenciar no Valor do Desconto aplicado e, estando desligado, o arredondamento não é realizado, o que contribui para que o Valor do Desconto aplicado seja resultado do percentual inserido.

**Arredonda % de desconto do rodapé nos itens - ARREDPERCDESCIT:** neste parâmetro, defina a quantidade de casas decimais utilizadas no cálculo do percentual de desconto rateado do rodapé para os itens. Com isso, o sistema realiza os cálculos considerando mais casas decimais antes de aplicar o arredondamento, evitando pequenas diferenças no somatório dos itens em relação ao valor total do rodapé da nota.
Caso ainda ocorra perda de precisão, recomenda-se aumentar a quantidade de casas definidas no parâmetro para que o cálculo fique mais preciso e evite divergências.

**Ajustar os centavos da NF-e na TGFDIN - AJUCENNFENADIN:** em relação ao lançamento de notas de vendas que possuam despesas acessórias (Tipos de Operação - TOP, aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias)), temos que ao proceder com a confirmação da nota, o sistema realizará uma conferência, e em seguida, o ajuste na proporção dos impostos. Diante disto, poderão ocorrer diferenças nos arredondamentos das casas decimais.

Para estes casos, o sistema considerará o Valor Total da NF e o valor da soma (Vlr Produtos + ICMS ST + Desp.Acessórias). Deste modo, ao habilitar o parâmetro de chave AJUCENNFENADIN, tem-se que os valores serão devidamente ajustados para que não ocorram divergências.

**Busca parceiro pelo veículo? - BUSPARCVEICULO:** quando este parâmetro estiver habilitado, ao inserir um registro no campo **"Veículo"** (localizado nesta tela, na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho)), o sistema preencherá automaticamente o campo **"Parceiro"** (grade Cabeçalho) utilizando parceiro que estiver configurado no [Cadastro de Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-).

**Importante:** Este parâmetro só funcionará se caso o veículo selecionado não estiver vinculado à empresa, ou seja, o veículo deverá ser necessariamente de algum parceiro.

**Usa endereço de entrega dos contatos - USENDENTREGA:** habilitando esse parâmetro, nessa rotina o sistema tornará obrigatório o preenchimento do campo **"Contato"** (na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho)). Além disso, na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), apresentará na aba [Endereço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaendereo) o campo **"Utiliza endereço de entrega do contato"**.

**Nota:** Ao realizar um lançamento na Central de Notas considerando que esse parâmetro esteja habilitado, o sistema emitirá o seguinte aviso:

**"É obrigatório informar o contato do parceiro para entrega."**

**Calcular 'Desconto no total' pelos itens? - DESCTOTVIAITENS:** quando este parâmetro encontrar-se habilitado, se for informado um percentual de desconto, o sistema calculará o Desconto do Total no Rodapé da Nota com base nos preços de tabelas dos itens e não baseado no valor total da nota. Já quando for informado um valor de desconto, o percentual do desconto da nota, será calculado com base no total da nota.

Desse modo, temos abaixo o comportamento do **Sankhya Om** quando o parâmetro DESCTOTVIAITENS for habilitado. Observe:

- Ao preencher o campo "**% desc. bonif."** com um valor igual a 100 em algum produto da grade de itens junto ao parâmetro ligado, junto à configuração do campo **"Percentual de desconto"** no rodapé da nota, o valor do desconto do rodapé será distribuído com base no **"Vlr. Unitário"** da tabela de preços para os itens que não possuem o campo % desc. bonif. preenchido.
- Quando um Percentual de Desconto for informado, haverá uma distribuição desse desconto no campo **"% Desconto"**, então este terá o percentual atual somado ao rateio do desconto do rodapé. Caso o item que já possua o % Desconto configurado não seja suficiente para abater o desconto do rodapé, o desconto residual será lançado no primeiro item.
- Poderão ocorrer inconsistências ao realizar um rateio do desconto do rodapé da nota ao preencher o campo % desc. bonif. e, posteriormente, inserir um desconto no rodapé.

**Custo por controle? - CUSTOPORCONT:** quando este parâmetro estiver habilitado, o sistema irá preencher o campo **"Custo"** do item da Nota bem como preencherá o campo **"Controle"** do item desta na:

- Explosão automática de lote na inserção de item;
- Explosão automática de lote no faturamento;
- Explosão automática de lote na expedição (WMS).

**Pré-visualizar nota e boleto nos Portais - PREVIEWNOTABOL:** este parâmetro quando ativado, habilitará o botão ![clip9560](https://ajuda.sankhya.com.br/hc/article_attachments/360061943393) **"Pré-visualizar"** nas Centrais e Portais de Notas, para que seja possível realizar a pré-visualização de notas e/ou boletos. Neste botão tem-se as quatro opções de pré-visualização seguintes:

- Pré-Visualizar Nota;
- Pré-Visualizar Boleto;
- Pré-Visualizar Danfe Simplificado;
- Pré-Visualizar Nota Expedição;
- Pré-Visualizar Nota Adicional.

**Nota:** Para pré-visualizar os documentos, é necessário que os pedidos/notas estejam confirmados.

**Reservar numero de serie em um Pedido de Venda? - RESNROSERPEDVEN:** ao habilitar este parâmetro, o sistema irá reservar o número de série utilizado no pedido de venda, ou seja, ao efetuar o lançamento de um pedido contendo um número de série, o sistema não irá permitir que outro pedido de venda seja lançado com este número de série. Sendo que, ao realizar a exclusão do pedido de venda este número de série poderá ser empregado em outro pedido.

**Observação:** quando se trata de produtos com série, não é possível faturar de maneira lateral, ou seja, pedido reservado sendo faturado para outro pedido já reservado, isso ocorre porque o sistema faz a validação do estoque com a série informada e como já existe uma reserva para aquele produto com aquela série e naquele local, quando é feito o faturamento para outra TOP de pedido que também reserva, o sistema tenta reservar novamente aquele produto com a mesma série e local, emitindo um aviso de que não há estoque disponível. Mas, se faturar o pedido para outra TOP que baixa o estoque não haverá erro.

**Atualiza vendedor dos itens automaticamente? - ATUALVENDITEM:** quando este parâmetro estiver desativado e havendo no cabeçalho de um pedido/nota um vendedor X, na grade de Itens terá inicialmente este mesmo vendedor X; porém, caso o vendedor no cabeçalho do documento for alterado para o vendedor Y, na grade de Itens o vendedor X será mantido.

Por outro lado, habilitando o parâmetro acima e tendo no cabeçalho de um pedido/nota um vendedor Z, na grade de Itens terá este mesmo vendedor Z; se no cabeçalho do documento o vendedor for modificado para o vendedor Y, na grade de Itens o vendedor também será alterado para o vendedor Y.

**Observação:** Mesmo com o referido parâmetro ligado, caso seja feita a modificação do vendedor diretamente nos itens para um vendedor diferente do vendedor da nota, o sistema respeitará a mudança realizada, pois pode ser um caso de comissão para o vendedor do item.

**Observação:** Quando o parâmetro Atualiza vendedor dos itens automaticamente? - ATUALVENDITEM estiver ligado ou o parâmetro **"Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE"** estiver preenchido, e ainda, na tela [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), o campo **"Cálculo de ICMS, IPI e ISS"**, da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), estiver configurado com a opção **"Não calcula e digita"**, quando o valor do IPI for informado manualmente e o código do **"Comprador"** ou **"Vendedor"** (localizado na grade [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho)) for alterado, o sistema irá verificar se é necessário refazer os cálculos dos impostos.

**Não consumir limite de crédito por Tipo Título? - VALLIMCRETIT:** neste parâmetro você pode definir a maneira em que o limite de crédito e/ou débito do cliente será consumido nas operações de vendas de acordo com os [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo). Desta forma, nas configurações deste parâmetro temos as seguintes opções:

- \*\*Nenhum:\*\*Selecionando esta opção, será consumido o limite de crédito na utilização de ambos os cartões.
- **Apenas crédito:** Quando esta opção estiver configurada, não será consumido o limite de crédito quando o cartão de crédito for utilizado;
- **Apenas débito:** Optando por esta alternativa, o sistema não consumirá o limite de débito caso utilize o cartão de débito nas operações de vendas;
- **Ambos:** Com esta opção, não será consumido o limite de crédito em ambos os casos, tanto para utilização de cartão de crédito quanto para cartão de débito;

**Nota:** Este parâmetro quando configurado, consumirá o limite de crédito apenas do [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654).

**Não consumir limite de crédito por Tipo de Negociação? - VALLIMCRETPV:** este parâmetro vai definir a forma em que o limite de crédito e/ou débito será consumido de acordo com os [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o); neste sentido, nas configurações deste parâmetro, temos as seguintes alternativas para seleção:

- **Nenhum:** Selecionando esta opção, será consumido o limite de crédito na utilização de ambos os cartões.
- **Apenas crédito:** Com esta opção selecionada, não será consumido o limite de crédito quando houver utilização de cartão de crédito nas operações;
- **Apenas débito:** Indicando esta opção, não será consumido o limite de débito quando utilizado cartão de débito;
- **Ambos:** Não será consumido o limite de crédito na utilização de ambos os cartões quando selecionar esta opção.

**Observação:** Na utilização deste parâmetro, temos que o limite de crédito será consumido apenas na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela).

**Nota:** No Tipo de Negociação, além de configurar o **"Tipo"** como cartão de crédito ou débito, você deve também configurar o campo **"Sub-tipo"** como cartão de crédito ou débito, visto que, o parâmetro observará este último para definir a maneira de consumo do limite.

**Validar regras de negócios de itens no faturamento? - VALREGNEGFAT:** habilitando este parâmetro temos que, ao criar uma [Regra de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014) com validação pela inclusão/alteração dos itens, caso o pedido tenha se originado de um faturamento e não ocorra nenhuma alteração neste item, será exibido um aviso de que a regra X não permitiu tal operação.

**Base para impostos retidos do financeiro - TPBASEIMPRETFIN:** este parâmetro deverá ser configurado de forma a definir o comportamento do financeiro em relação aos impostos retidos, ou seja, se a base para os mesmos serão de acordo com o **"Valor do Pagamento"** ou conforme o **"Valor da Nota"**.

**Usar saldo FLEX do Pedido? - SALDOFLEXPEDIDO:** através da habilitação deste parâmetro, será possível utilizar o [Saldo Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603054) no próprio pedido que está sendo negociado, ou seja, o valor poupado em um produto poderá ser utilizado no próprio pedido, em outro produto e, assim, os valores de acréscimo serão somados ao saldo do pedido e não ao saldo do cliente.

**Importação, tag vOutro da nota sem valor do ICMS e - VOUTNOTASEMICMS:** ao habilitar este parâmetro, os valores do ICMS e do FCP interno serão retirados da tag  da nota durante a geração do XML.

**Distribuir desconto p/ produtos s/ valor máximo? - DISTDESCPRODSM:** quando este parâmetro estiver habilitado e o desconto máximo do produto for igual a zero ou vazio tem-se que, o desconto no Rodapé da Nota será distribuído normalmente, considerando como desconto máximo do Produto, o valor inserido no campo **"% Desconto máximo"** do Tipo de Negociação vinculado à esta Nota.

**Observação:** Quando o parâmetro **"Ñ valida Desc.Max na Dist. Desc.Jur. (DISTJDCONF) - NVALIDARDESCMAX"** estiver ligado, o parâmetro DISTDESCPRODSM não terá aplicabilidade independente da sua configuração.

Se o parâmetro NVALIDARDESCMAX estiver ligado juntamente com o parâmetro DISTJDCONF, distribui-se o desconto do rodapé da nota nos itens, sem validar o desconto máximo, possibilitando que os itens recebam mais desconto do que o permitido em seu cadastro.

Quando o parâmetro DISTDESCPRODSM se encontrar habilitado juntamente com o parâmetro DISTJDCONF e o parâmetro NVALIDARDESCMAX estiver desligado, distribui-se o desconto do rodapé da nota nos itens sem validar o desconto máximo pelo Cadastro de Produtos (apenas em produtos com Desconto Maximo **"0"** ou **"nulo"**), e validará o desconto máximo cadastrado no Tipo de Negociação. Ou seja, caso o produto tenha um desconto máximo > 0, irá validar usando o desconto máximo do produto, caso não tenha, validará usando o desconto máximo do tipo de negociação.

Recomenda-se usar o parâmetro DISTJDCONF ligado e manter o DISTDESCNFE desligado.

**Campo para agrupar produtos na Central - CAMPAGRUPPROD:** quando este parâmetro  estiver configurado, será utilizado na rotina de validação do produto repetido no pedido, fazendo com que possa ser lançado o mesmo produto no pedido, desde que o campo esteja com o valor diferente.

**Habilita configuração de redução de IPI? - IPINFEREDVALOR:** com este parâmetro habilitado, e o campo **"% Redução de Vlr. IPI"** (tela [Alíquota IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abageral)) devidamente preenchido, você poderá digitar o % de redução do IPI, desta forma, possibilitará a redução do imposto conforme sua necessidade.

**Considerar desconto financeiro p/ tag vLiq NF-e? - VDESCFINVLIQNFE:** ao habilitar este parâmetro, o valor do desconto financeiro irá subtrair o valor do desdobramento e irá gerar o valor líquido do financeiro, não alterando o valor da nota.

**Permite digitar valor unitário em devoluções (PERMITEVLRDEV):** quando esse parâmetro for habilitado, ao digitar o **"Valor Unitário"** mesmo quando este permitir apenas quantidade ([Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abavenda), o campo **"Digitação na nota"** configurado com a opção **"Quantidade"**). Esse processo irá acontecer quando a Nota de Devolução for proveniente de uma Nota de Venda, caso tente devolvê-la diretamente na Central, não será permitida à alteração do campo Valor Unitário.

**Importante:** Este parâmetro só funcionará para Devoluções de Venda.

**TOP s/frete sem TAG infor volume transportado - TOPSFRETESVOL:** este parâmetro vai definir o comportamento do conjuntos de tags de volumes de transporte em uma NF-e; se no [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414#graderodap) da Nota, aba [Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414#abatransporte), o campo CIF / FOB estiver como **"Sem frete"** e este parâmetro estiver ligado, o XML gerado não vai possuir as tags de volume transportado.

**Valid. Restriç./Exces. alterar Financ. na central - VALRESTFINCENTR:** caso este parâmetro esteja ligado, o sistema validará restrições e exceções da TOP, ao alterar os campos CODTIPOPER, CODEMP, CODPARC, CODVEND, CODCENCUS e CODNAT do financeiro via Central de Notas.

**Usa controle de acesso para aba comissões multipla - CTRLACESSCOMIS:** se você ligar este parâmetro, poderá controlar os acessos de usuários ao painel Comissões nas centrais. Para isto, depois de ligar o parâmetro, acesse a tela Acessos e localize o módulo **"Notas"** (Comercial> Rotinas> Portal de Vendas), selecione um usuário e em seguida limite os acessos que deseja, sendo que estes podem ser **"Editar"**, **"Incluir"**, **"Alterar"**, **"Excluir"** e etc. Desta forma, se algum dos usuário a quem você limitou os acessos tentar realizar alguma das ações, o sistema não o permitirá.

**Aplicar Total desc. serviços p/ impostos federais? - DESCSERVIMPFED:** caso este esteja habilitado, fará com que seja possível realizar a proporção do desconto da nota sobre os serviços e impostos da NFS-e, quando esse desconto for informado no Rodapé da Nota, no campo **"Total desc. serviços"**.

**Distribuir desconto autom. com impostos embutidos - DISDESAUTIMPEMB:** se esse parâmetro estiver habilitado, será aplicado um desconto total bruto sobre o valor da nota, considerando a incidência dos impostos IPI e ICMS-ST.

**Observação:** Para que a distribuição de descontos com os impostos embutidos seja feita corretamente, é necessário que o campo **"Cálculo de ICMS, IPI E ISS"** no [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), esteja com a opção **"Calcula e não digita"** selecionada.

**Nota:** Também é necessário que os parâmetros abaixo estejam configurados da seguinte forma:

- **Opção para distribuir Juros entre os Produtos? - DISTJUR:** Desligado;
- **Distribuir desconto autom. antes calc. impostos? - DISDESAUTANTIMP:** Desligado;
- **Saída c/Base IPI sem Desconto? -SAIIPISEMDESC:** Desligado;
- **Distribuir desconto autom. com impostos embutidos - DISDESAUTIMPEMB:** Ligado.

Após o lançamento da nota, você deve acessar o botão **"Outras Opções..."** da Central de Vendas e selecionar a opção **"Distribuir desconto entre produtos"** para que sejam distribuídos os devidos descontos aos itens da nota (campo **"Desconto no total"**, aba [Totais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatotais) do [Rodapé da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap)).

**Permite devolver nota de complemento c/ qtd zerada - PERDEVNOTACOMPL:** ao ligar este parâmetro, o sistema permitirá que uma nota de estorno seja gerada com a quantidade zero, uma vez que a esta nota já tenha passado do prazo de cancelamento.

**Aceita recebimento TEF vencido? - ACEITATEFVENC:** quando estiver ligado, ao receber um pagamento via TEF com a data de vencimento do título anterior ao dia do pagamento, o sistema irá considerá-la. Caso contrário, será utilizada a data do dia atual como vencimento do título.

**Cálculo Automático de Frete no WMS? - CALAUTOFRETEWMS:** ao habilitá-lo, será realizado o cálculo automático do frete, considerando a cidade de destino dos campos **"Redespacho (Recebedor)"** e **"Contato de Entrega"**. Sendo assim, esses campos deverão vim preenchidos; caso contrário, será emitida a mensagem abaixo:

**"Para uso de cálculo automático de frete, o código do Contato de Entrega ou Redespacho (Recebedor) devem ser preenchidos no cabeçalho da nota."**

**Observação:** Na [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada, a marcação **"Simulação de frete automática"** da aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) deve estar realizada também.

**Nota:** Após habilitar o parâmetro e a marcação informada acima, lance um pedido de venda, informe os dados do cabeçalho, se atentando para o Parceiro e para os campos Redespacho (Recebedor) e Contato de Entrega; preencha a grade de itens e, na aba [Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatransporte) da grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap), escolha no campo **"CIF/FOB"** a opção **"CIF - Contratação do Frete por conta do Remetente"**.

**Importante:** A ordem de precedência que o sistema respeitará é a seguinte:

- Quando um dos campos estiverem preenchidos: Qualquer um deverá ser utilizado como referência para o cálculo.
- Quando os dois campos estiverem preenchidos:

1. Campo Redespacho (campo será considerado para o cálculo de frete);
2. Contato para Entrega (campo não ignorado para o cálculo de frete).

**Usar o maior desconto promocional?-USAMAIDESCPROMO:** estando ligado, o sistema sempre irá considerar o maior desconto promocional cadastrado para produtos/parceiros. Quando desligado, será utilizado o desconto mais recente.

**Observação:** Caso o parâmetro acima esteja ligado e no lançamento do item da nota, você alterar o campo **"% de desconto"** para um valor menor, ao salvar o item, o sistema solicitará que haja a liberação do Evento **"66 - Desconto do item abaixo do calculado"**.

**Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP:** quando estiver ligado e for realizado o faturamento de uma nota ou duplicação de um pedido/nota nos Portais, caso o vendedor/comprador esteja inativo, o sistema irá completar o processo de faturamento ou duplicação, zerando o campo vendedor e apresentando a mensagem abaixo no Painel de Avisos do documento gerado:

**"O parâmetro IGNORAVENDCOMP - Ignorar Vend. ao duplicar/faturar doc. nos portais" está ligado, e o campo vendedor/comprador foi zerado ao duplicar ou faturar. Lembre-se de preencher o campo vendedor ou comprador caso seja necessário".**

Por outro lado, se o parâmetro estiver desligado e existir um documento já confirmado com um vendedor ou comprador inativo informado, quando for duplicado ou faturado esse documento, o sistema impedirá o procedimento.

**Valida Local da MP no KIT? - VALLOCKITMP:** estando ligado, o sistema não permitirá  o lançamento de Kit's com produtos que estejam com Local 0 quando a marcação **"Usa local"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba **"Medidas e estoque"**, sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abaestoque) for habilitada.

**Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR:** Quando for ligado, os campos **"Quantidade"** e **"Vlr. Tot. Moeda"** serão habilitados na grade de itens das centrais se o Tipo de Movimento for Transferência.

Com os parâmetros **"Nota modelo para cálculo de preço dinâmico - MODCALCPRECDIN"** e **"Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE"** devidamente configurados, quando for lançada uma venda ou um pedido de venda informando o local do item, o valor unitário será calculado de acordo com a procedure cadastrada.

Após realizar o lançamento de um pedido com um produto Kit e **"Confirmar"**, caso seja necessário efetuar outra **"Cotação de Moeda"**, a informação do lote do produto componente ficará salva apenas se o parâmetro **"Retorna controle ao recalcular MPs?- RETCONTRECMP"** estiver ligado.

**No faturamento, somar na nota o Peso e M3 dos pedi - FATSOMAPESOM3P:** quando estiver ligado, após realizar o corte de um item no pedido de venda e faturar o mesmo, o sistema irá atualizar o peso da nota conforme o peso do pedido de origem.

**Limpar campos Fin. ao duplicar registro na Central - DEFCAMDUPFINNOT:** você pode informar os campos cujo os dados não devem ser copiados no financeiro ao duplicar registros na Central de Vendas. Dessa forma, a seguir, você poderá observar os campos que poderão ser informados no parâmetro, uma vez que, estes devem ser separados por vírgulas:

- CODNAT;
- CODCENCUS;
- CODPROJ;
- CODBCO;
- CODCTABCOINT;
- HISTORICO.

Após o lançamento da nota, você poderá alterar as datas de Entrada/Saída, Faturamento, Movimento e Negociação, apenas se o parâmetro **"Obriga Dt.Negoc. igual a do servidor em COMPRAS? - DTNEGSERVCPA "** estiver desligado.

**Distrib. desc autom imp. embut. somando desc item - DISTDESCIMPEMB:** quando for ligado, o sistema irá somar o desconto dado em cada item da nota à aquele concedido no rodapé ao utilizar a opção **"Distribuir Desconto entre os Produtos"**. Porém, para tal ação, é necessário que as seguintes configurações sejam realizadas:

**1.** Na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), habilite os parâmetros da maneira como exibido abaixo:

- **Opção para distribuir Juros entre os Produtos? - DISTJURO:** Desligado;
- **Distribuir desconto autom. com impostos embutidos - DISDESAUTIMPEMB:** Ligado;
- **Distribuir desconto autom. antes calc. impostos? - DISDESAUTANTIMP:** Desligado;
- **Saída c/Base IPI sem Desconto? - SAIIPISEMDESC:** Desligado;
- **Calcular 'Desconto no total' pelos itens? - DESCTOTVIAITENS:** Ligado;
- **Distribuir desc. na confirmação da nota? - DISTJDCONF:** Ligado;
- **Distribuir desc.na confirmação da NFE ? - DISTDESCNFE:** Ligado.

2. Posteriormente, na aba Impostos da tela [Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), o campo **"Cálculo de ICMS, IPI e ISS"** deve estar com a opção **"Calcula e não digita"**, na TOP a ser utilizada na venda.

Do contrário, com o parâmetro Distrib. desc autom imp. embut. somando desc item - DISTDESCIMPEMB desligado, os valores dos descontos do itens serão substituídos pelo valor dado no rodapé da nota.

**Inibir eventos na subtrao de ST e IPI - INIBIREVTSTIPI:** você define se a solicitação de liberação dos eventos [1 - Desconto Tipo Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#1-descontotiponegociao), [25 - Desconto por Item da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota) e [27 - Fórmula Desc.Máx.Tipo Negoc.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#27frmuladesc.mx.tiponegoc.poritem) por Item serão inibidos quando houver alteração em valores relacionados à subtração dos impostos de ST e IPI. Para ficar mais claro, observe o caso de uso abaixo:

O sistema foi configurado para que o IPI e ST fosse descontado do valor do produto, ou seja, um pedido de venda (com a TOP não calculando nenhum imposto) que tem um produto vendido a R$10,00, ao ser faturado, o sistema automaticamente já subtrai o valor de ST e IPI do produto, sendo assim, teríamos por exemplo, R$2,00 de ST e R$1,00 de IPI, fazendo com que o valor unitário do produto fique em R$7,00.

Então, com o parâmetro INIBIREVTSTIPI ligado, o valor final da nota permanece os mesmos R$10,00, com o mesmo valor do pedido que não possui cálculo de impostos. Assim, apenas serão solicitados os eventos de liberação 1, 25 e 27, se realmente houver desconto na nota ou pedido.

**Aplicar vlr editado da Consulta Prod. na Central?- APLVLRUNITEDIT:** quando ligado, será considerado na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), o valor unitário da coluna **"Vlr. Unit"** localizada na grade **"Produtos no carrinho"**, mesmo que este valor tenha sido editado manualmente. Do contrário, quando este parâmetro estiver desligado, o sistema irá considerar o valor unitário da tabela, independentemente se a edição deste valor tiver sido realizada manualmente.

**Dec. p/valor ao desmembrar lotes no faturamento? - DECVLRDSMBRLOTE:** definirá se será recalculado o valor unitário para redefinir as casas decimais no faturamento de um documento. Sendo assim, se o parâmetro tiver ligado, o recálculo será feito e, estando desligado, não será executado.

**Observação:** O parâmetro acima corrige a divergência no valor da nota e no valor total de produtos entre o documento original e o gerado no faturamento do documento, que é causado pela quantidade de casas decimais de alguns itens.

**Ajusta decimais para cálculo com moeda - AJUSTACSDECMOE:** estando ligado, o cálculo dos itens da nota serão realizados conforme o campo **"Vlr. Moeda"** configurado no cabeçalho da nota de faturamento, ainda que estes valores sejam divergentes da nota de origem.

**Recalcula valores Cons. Prod. qdo prod. iguais? - RECVALCONSPROD:** quando estiver ligado e um item for editado através da consulta de produtos e seu **"CODPROD"** não for alterado, não serão recalculados os campos **"QTDNEG"** e **"VLRUNIT"**.

**Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT:** por padrão, estará ligado para que não haja o acúmulo de vencimentos. Sendo assim, caso você queira que o sistema realize esse acúmulo, basta desativar o parâmetro. Porém, é importante saber que, quando os parâmetros **"Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT"** e Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT estiverem ligados quando há mais de uma parcela definida com a mesma **"Base do Prazo"** (tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)), a base do vencimento será o valor do campo **"DTPRAZO"** do financeiro gerado. Mas se o Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT for habilitado, e o parâmetro Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT desligado, a base do vencimento será a mesma para todas as parcelas configuradas.

**Exclui liberações ao fechar sem salvar na central? - EXCLIBFECSESALV:** estando ligado, ao fechar a tela de solicitações de liberação na central sem clicar em salvar, o sistema irá apagar as liberações da nota que não possuam data de liberação na TSILIB. Caso esteja desligado, as liberações ficam salvas na tabela mencionada.

**Usar Dt. Ent/Saída na Ger. do Liv. Fis. de Saída - USADTSAILIVSAI:** caso esteja ligado e o cabeçalho da nota de saída esteja com o campo **"Dt. Neg."** com uma data diferente do campo **"Dt. Entrada e Saída"**, ao realizar a geração do livro fiscal das notas, o sistema irá gerar o campo **"Dt do movimento"** do [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI) com a mesma data do campo **"Dt Entrada/Saída"** do cabeçalho da nota.

Por outro lado, se o parâmetro estiver desligado e for realizada a geração do livro fiscal das notas de saída, o sistema manterá o comportamento atual, ou seja, irá gerar o campo Dt. do movimento com a mesma data do campo Dt. Neg.

\*\*Ajust. a base igual ao Ajust. da BaseRed(TGFDIN)? - AJUSTARBASEDIN:\*\*quando esse parâmetro estiver ligado, será feito o ajuste da diferença referente à base TGFDIN da mesma maneira que é feito o ajuste da BASERED, ou seja, distribuída entre os itens.

**Usa cotação da nota de origem - USACOTNOTAORIG:** com esse parâmetro ligado, o sistema irá manter a cotação das notas conforme as opções **"Preço em Moeda"** e **"Preço de Venda"** do campo **"Usar como preço"** definidas nas respectivas [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)'s das notas de origem e destino.

**Dias p/ notificação notas não confirmadas - DIASNOTANAOCONF:** quando esse parâmetro for configurado com um valor maior que zero, na tela [Notas Não Confirmadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10847777335319) o sistema exibirá um painel com as notas não confirmadas conforme a quantidade de dias a partir da **"Data de Negociação"**. Porém, se o parâmetro for configurado com o valor '0', a tela exibirá somente um painel com todas as notas não confirmadas existentes nas Centrais independente da quantidade dos dias.

\*\*Refazer financeiro ao editar Outros Imp. de itens? - REFAZFINIMPPROD:\*\*quando esse parâmetro estiver desligado, o financeiro não será refeito após a edição de Outros Impostos dos itens da nota. Caso esteja ligado, sempre será recalculado o financeiro após editar os Outros Impostos dos itens.

**Decimais para custo desimb. imposto - DECDESIMIMP:** utilize o parâmetro para que, ao realizar o faturamento de um Pedido de Venda, os impostos sejam desembutidos, de acordo com o número informado de decimais.

**Manter PIS e COFINS do XML importado. - MANPISCOFXMLIMP:** para que os impostos PIS e COFINS sejam importados conforme o XML, deve-se utilizar esse parâmetro ligado, considerando também as seguintes observações:

- Se for emissão própria ou a TOP estiver marcada para a importação manter despesas acessórias;
- O tipo de cálculo do ICMS deve ser igual à **"Não calcula e digita"**;
- O tipo da NF-e deve ser **"Terceiros"**;
- Portar qualquer imposto ICMS/ST/IPI/PIS/COFINS.

**Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT:** para que as tags dos impostos retidos (**retTrib**, **vRetPIS**, **vRetCOFINS**, **vRedCSLL**, **vBCIRRF** e **vNF**) sejam geradas no XML, é necessário que esse parâmetro esteja ligado e os parâmetros **"Destaca imp. federais na NF-e mista qdo.não retido? - DESTIMPNRETNFEM"** e **"Considerar desconto financeiro p/ tag vLiq NF-e? - VDESCFINVLIQNFE"** desligados.

**Remove ST embutido em desconto?-REMOVSTEMBDESC:** por padrão, é apresentado ligado e fará com que não seja exibido o pop-up de liberação de limites em casos de ST Desembutido. Caso você queira que haja a liberação de um supervisor, desligue o parâmetro para que o pop-up seja exibido.

**Separa por layout as conf. dos form. na Central - SELAYCONFFORM:** quando este parâmetro estiver habilitado, as configurações dos formulários da tela serão gravadas separadamente de acordo com o layout da nota.

**Copiar outros impostos na devolução? - COPIAOUTRIMPDEV:** quando o referido parâmetro for habilitado, o sistema incluirá os outros impostos já existentes na nota de origem na nota de devolução.

**Desconsidera Título GNRE no financ. na import. XML - DESTITGNREIMP:** quando o parâmetro estiver habilitado, o usuário poderá desconsiderar, se desejar, o tipo de título da GNRE. Ressaltamos que, o referido parâmetro não influenciará na tratativa de parcelas referente ao DIFAL.

**Forçar geração do financeiro quando GNRE apenas na nota? - GERFINGNRENOTA:** com o parâmetro ativado, ao realizar o faturamento de um pedido de venda, caso a marcação **"Gerar GNRE"** da aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais) (tela [Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)) esteja habilitada, os financeiros serão gerados conforme configurado nos [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o). Logo, se no tipo de negociação da nota possuir um financeiro GNRE, este será gerado.

**Salva Data Padrão para Faturamento/Venda-DATAVNDPADRAO:** se estiver ligado, será utilizada a última data informada para todos os faturamentos do dia.

**Recalcula preços quando altera Tipo de Negociação - RECPRECOTP:** ao selecionar a opção **"Nunca"** e preenchendo o campo TIPLANCNOTA com a opção diferente de **'Q'** na tabela TGFPRO do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/Cadastro%20de%20Produtos%20), o valor do produto não será recalculado ao alterar o Parceiro na Central de Vendas.

**Considerar reserva global para reserva específica - VALESTUSARESERV:** quando este parâmetro estiver ligado, o sistema vai considerar a quantidade na reserva de estoque com o controle vazio, dessa forma, mesmo lançando o item com o lote informado, o sistema verificará todo o estoque do produto verificando se será possível efetuar a reserva ou não do produto escolhido.

\*\*Permite editar/excluir tít. receb. administrativo? - PERMEDITRECADM:\*\*caso queira realizar determinada alteração em recebimentos com cartão na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), basta ligar esse parâmetro. Porém, é importante ressaltar que se não houver a conferência de lançamentos do cartão e baixa manual na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), poderão ocorrer inconsistências nos lançamentos e/ou recebimentos.

**Utilizar nova estratégia de corte no faturamento? - CONTSLDCORTEFAT:** esse parâmetro foi criado para cenários onde se realiza o corte em itens de um pedido por meio dos Portais. Posteriormente, ao faturar este pedido ocorre a explosão de lote e caso o parâmetro esteja desligado o corte será realizado em cada item daquele produto que sofreu a explosão de lote. Para melhor compreensão, considere o seguinte exemplo:

- O produto CODPROD 1 dispõe de um estoque válido nos lotes A e B, onde o lote A possui quantidade 30 e o lote B possui 70;
- Foi gerado um pedido de venda deste produto, com quantidade igual a 100, mas sem informar o lote;
- No [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) foi realizado o corte de 10 produtos;
- Ao faturar este pedido, na nota será apresentada a quantidade final igual a 80, sendo 30 unidades para o lote A e 50 para o lote B, pois em cada uma das linhas do item (lote A e lote B) sofreram o corte de 10, ou seja, o corte foi replicado para cada linha daquele produto na nota.

Assim, para que o corte não seja replicado, ligue o parâmetro CONTSLDCORTEFAT. Dessa forma, o corte ocorrerá em apenas uma linha da nota faturada.

Vale ressaltar que, essa regra ocorre quando se utiliza o WMS e o faturamento é realizado pelo Portal.

Se for utilizado o WMS e o corte for efetuado por meio da tela [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274) e, ainda, o parâmetro CONTSLDCORTEFAT esteja ligado, o item cortado será enviado para a nota faturada. Desse modo, para que não seja levado em consideração na nota o item cortado, o parâmetro deve estar desligado.

**Valida calc. ICMS durante a geração da NFe? - VICMSDIFNFE:** ao ligar esse parâmetro, o valor dos impostos da nota serão arredondados.

**UF que permite deduzir vlr repasse ICMS da BC IRRF - UFDEDREPICMSIRF:** preencha este parâmetro com a UF desejada. Desta forma, ao selecionar essa mesma UF na Central de Vendas durante a emissão da nota com desoneração de ICMS e retenção de IR, o valor do repasse será deduzido da base de cálculo do IRRF.

**Prevenir a edição de itens em processamento? - PREVEDTITEPROC:** quando este parâmetro estiver ativado, na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), na grade de **"Itens"** é necessário inserir entre o campo **"Produto"** e os campos não editáveis, algum campo editável que seja diferente dos campos **"Quantidade"**, **"Vlr Unitário"** e **"Valor Total"**.

**Destaca imp.federais na NF-e mista qdo.não retido? - DESTIMPNRETNFEM:** ao ligar esse parâmetro, a tag  será calculada pelo valor bruto dos produtos/serviços e, ao gerar o XML e destacar os impostos retidos na nota mesmo se os impostos estão inclusos na nota e configurados para subtrair no financeiro. Porém, esse comportamento só irá ocorrer quando a NF-e for mista, sendo esta de produtos e serviços para Brasília/DF.

**UFs que somam os impostos retidos na NFe - UFSSOMAIMPRET:** informe nesse parâmetro as UF's que gostaria que os parâmetros **"Somar valor de imposto retido no valor total da no - SOMIMPRETVLRNOT"** e DESTIMPNRETNFEM destaquem os impostos retidos no XML da nota. Porém, se não houver UF's no campo **"Texto"** do parâmetro UFSSOMAIMPRET, todas as UF's serão consideradas na geração do XML.

**Proporc. desc. total na desoneração de impostos - PROPDESCDESOIMP:** com esse parâmetro ligado, ao aplicar o desconto no total de um pedido de venda que possua a configuração para aplicação dos valores do desconto do ICMS, PIS e COFINS desonerado no total da nota, o sistema irá manter esses valores no lançamento do desconto e na confirmação do pedido de venda.

**Nota:** o parâmetro acima terá o comportamento descrito independente da definição do parâmetro DISTJDCONF.

**Utilizar cache para validar metas de notas com rateio ? - LIGCACHEMETA:** este parâmetro, quando ligado, tem-se uma melhora de performance para calcular o valor do realizado para quem usa a rotina de [Planejamento de Metas e Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814).

**Inicializar lista de remessa de nfe ao gerar lote - INITNFEREMESSA:** quando este parâmetro for ligado, o sistema não reinicializa a lista de notas de remessas da NFe, garantindo que todas as notas de um lote sejam transmitidas. No entanto, caso ele esteja desligado, se gerado lote com múltiplas notas de remessa de diferentes clientes, apenas a última nota será transmitida.

**Parceiro F2 ignora controle de acesso do cad. parceiro? - IGNORACESPARCF2:** com esse parâmetro desligado, só será possível acessar o pop-up Cadastro simplificado de parceiros quando o usuário tiver os devidos [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) de edição da tela de [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros). Caso contrário, com o parâmetro habilitado, será possível editar o pop-up de parceiro simplificado sem qualquer permissão.

**Considerar o vlr. líquido da operação ENOTAS - CONSIDVLLIQOPER:** caso este parâmetro esteja desligado, ao emitir uma NFS-e via eNotas, o sistema enviará no grupo de serviço, o valor total com a dedução do desconto, ou seja, o valor líquido. Assim, no entanto, caso ele esteja ligado e na cidade da empresa emissora da NFS-e a opção **"Enviar tag descontoCondicionado nos metadados do JSON?"** (tela [Cidades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), aba [NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades#abanfs-e)) esteja desmarcada, nenhum valor de desconto será enviado à prefeitura.

Observe o exemplo abaixo:

Uma venda com valor total de R$ 160,00 e um desconto de R$ 10,00.

Com o CONSIDVLLIQOPER ativado, o sistema enviará:
ValorTotal = R$ 150,00
ValorDesconto = R$ 0,00

Com o CONSIDVLLIQOPER desativado, o sistema enviará:
ValorTotal = R$ 160,00
ValorDesconto = R$ 10,00

**Calc Desc. ICMS no Calc ST sem IPI - CALINDDESICMSST**: quando o parâmetro estiver ligado, deve ser utilizado para que ao confirmar uma nota onde existem mais de um item e somente alguns dos itens tem incidência de ST, junto também da utilização de tipo de cálculo específico nas configurações da alíquota e proporcionalização de ICMS ST do Frete, o sistema realize os cálculos corretamente e não apresenta a divergência.

**Bloqueia a grade de itens durante a inicialização do produto - LOCGRIDINITITEM:** quando ativado, este parâmetro impede qualquer edição ou alteração na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) antes que todas as informações do produto sejam totalmente carregadas, evitando assim problemas nos cálculos de valores (como o valor unitário).

**Simula formas de pagamento na Central? - USASIMFORMAPGTO:** quando ativado, caso a informação do Parceiro seja alterada no [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) e o parâmetro **"Tabela de Preços por: - TIPTABPRECOS"** esteja com a opção **"Parceiro"** selecionada, o parâmetro garantirá que o campo **"Vlr. Unitário"** na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) seja recalculado com base no preço de tabela. Além disso, o valor atualizado será utilizado para preencher o campo **"Preço Base"** também localizado na grade de Itens.

Se o parâmetro estiver desativado, o sistema não atualizará o Vlr. Unitário, mantendo o valor atual no campo Preço Base, mesmo que este não corresponda ao preço de tabela.

Considere o exemplo abaixo:

- **Produto:** Água Sanitária QBoa 12x1LT
- **Preço de Tabela:** R$ 1,80

(1)** Cenário 01:** Parâmetro desativado

- **Quantidade:** 1
- **Valor Unitário Inicial:** R$ 2,50
- **Preço Base Antes da Alteração:** R$ 2,00

Ao alterar o parceiro para "Parceiro 2":

- **Vlr. Unitário:** R$ 2,50
- **Preço Base:** R$ 2,50

(1)** Cenário 2:** Parâmetro ativado

Ao alterar o parceiro para "Parceiro 2":

- **Vlr. Unitário:** R$ 1,80
- **Preço Base:** R$ 1,80

**Recalcular Valor ao Alterar a Quantidade na Conferência? - RECALCVALITEM:** este parâmetro define se o **"Vlr. Unitário"** do item será recalculado ao alterar a quantidade de itens na [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia). Por padrão, este parâmetro se encontra habilitado, o que faz com que o sistema ajuste o valor unitário quando há mudança na quantidade. Caso esteja desligado, o valor unitário permanecerá inalterado, mesmo que a quantidade seja alterada.

**Usa VLRCTB baseado na TGFDIN p/ NFe Emis. Prpria. - USAVLRCTBBASDIN:** se este parâmetro estiver ativado, o sistema altera o cálculo do valor contábil dos itens na [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI). Confira como funciona:

1. **Operações de saída ou entrada (empresa não optante pelo Simples Nacional):**
   - Se o item não tiver base com diferimento, será usada a base de ICMS normal como valor base, em vez da base reduzida.
2. **Compras, importações ou nacionalizações (CFOP 3000-3999):**
   - O valor contábil do item será calculado de forma diferente. O sistema soma:
     - Valor total (VLRTOT);
     - IPI (VLRIPI);
     - PIS (VLRPIS);
     - Cofins da importação (VLRCOFINSIMP);
     - Despesas aduaneiras (VLRDESPADUA).
3. **Notas com complementos de ICMS (CST20 ou CST51):**
   - Assim como no item 1, será usada a base de ICMS normal como valor base, e não a base reduzida.

**Valida preench dt val contr.adicional por dt val? - VALCONTDTVAL:** quando este parâmetro estiver ativado, o sistema impedirá que o item seja salvo sem o preenchimento do campo **"Data de Validade"** na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens). Para que essa validação seja aplicada, é necessário atender às seguintes condições no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos):

- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), a marcação **"Utiliza data de Validade"** deve estar habilitada;
- Na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), o campo **"Controlar Por"** deve estar configurado como **"Data da Validade"**.

Se ambas as configurações estiverem efetuadas, quando o usuário tentar salvar o item sem informar a Data de Validade, será exibida a seguinte mensagem:

**"O produto X é controlado por Data de Validade e nenhum controle foi informado."**

Se você precisar que o valor do seguro componha o cálculo dos impostos da nota, basta manter o parâmetro **SEGINCICMS** (Seguro incide ICMS) ligado. Com essa configuração ativada, o sistema passa a somar automaticamente o valor do seguro junto ao valor do ICMS. Vale destacar que essa regra de incidência é válida e tem o mesmo comportamento tanto para os documentos de entrada (Central de Compras) quanto para as operações de saída (Central de Vendas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#top)

Acesse também:

[Central de Vendas | Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612234)

[Central de Vendas | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374)

[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)

[Como realizar pagamentos via PIX na Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/27105600713879-Como-realizar-pagamentos-via-PIX-na-Central-de-Vendas)
