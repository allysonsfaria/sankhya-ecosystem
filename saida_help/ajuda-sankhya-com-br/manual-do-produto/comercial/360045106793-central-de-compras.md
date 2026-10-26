---
id: "360045106793"
titulo: "Central de Compras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-10-01T17:55:47Z"
rotulos: ["AJUDA DO SKW", "ORDITENS", "ACEITARVLRZERO", "AGRUPADANFEBOL", "CALCCUSTOMEDCAF", "EXPEDSENHA", "IMPEXPSEMCONF", "MASCARAPERCDESC", "NOTAADICEMP", "QRYCONSPROD", "Central de Compras manual", "Configuração", "Parceiro", "Central de Compras", "Estoque", "Financeiro", "br.com.sankhya.com.mov.CentralNotas", "DIASNOTANAOCONF", "Configuração de Layout", "Documentação de Entrada", "CFOPPEDIDOS", "DECVLRLIQARR", "FORCATPROVCONF", "LIGCACHEMETA", "NFEFINDIFNOTA", "DISABLEGRIDPAG", "CALINDDESICMSST", "LOCGRIDINITITEM", "QTDREGCCAPORJOB", "CALCCUSTOPORJOB", "VALCONTDTVAL", "SEGINCICMS", "Documentos Eletrônicos"]
---

# Central de Compras

```
 Módulo: Comercial > Rotinas
```

---

A Central de Compras é a tela responsável por receber todos os documentos referentes às operações de entrada de mercadoria ou aquisição de serviços pela empresa. É uma tela que será aberta através do [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) quando você solicitar a inclusão ou selecionar (duplo clique) um Pedido de compra, Nota de compra ou Devolução de compra já lançado; notas de entrada que foram canceladas são detalhadamente visualizadas na tela [Notas Canceladas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107913).

**Importante:** A Central de Compras, assim como as demais centrais, poderá ser utilizada com base em um layout padrão do sistema, ou em um layout configurado manualmente de acordo com os tipos de movimento que forem trabalhados. Entenda por "layout" como a definição dos campos que irão compor o documento na tela, bem como sua disposição; por exemplo, alguns campos não são necessários no lançamento de Pedidos de Compra, em contrapartida, precisam ser apresentados em uma Devolução de Compra, ou seja, essa é diferenciação feita no layout dos respectivos documentos e tal modificação é feita através da tela [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

| [Grade Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradecabealho) | [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) |
| --- | --- |
| [Grade Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) | [Botões no topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela) |
| [Lançar um documento na Central...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#comolanarumdocumentonacentraldecompras) | [Cadastro Simplificado de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#cadastrosimplificadodeparceiros) |
| [Parâmetros que atuam na Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#parmetrosqueatuamnacentraldecompras) |  |

![Imagem 1: Parâmetros que atuam na Central de Compras](https://ajuda.sankhya.com.br/hc/article_attachments/4408230617495)

## Grade Cabeçalho

A grade Cabeçalho armazena os dados referentes ao "cérebro" do documento; nela você tem a [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas) que está realizando a compra, o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) fornecedor do qual a aquisição vai ser, está, ou foi realizada, o [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113513-Tipo-de-Negocia%C3%A7%C3%A3o) utilizado no processo, o [Tipo de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) compatível com a negociação, sendo esta última, uma informação essencial para as devidas atualizações de estoque, financeiro, livros fiscais ocorram corretamente.

Além disso, terá os dados particulares de cada documento, como o Número Único, Número da Nota, Datas de Entrada/Saída, Faturamento e Movimento; como informado inicialmente, outros campos podem ser incluídos no cabeçalho através da rotina [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634); alguns deles, devem ser inseridos para posterior preenchimento, de acordo com a legislação em que cada empresa se enquadra.

Para o registro de notas de serviços tomados, o campo **"Série NFS-e"** está habilitado para edição e permite a digitação livre de até 5 caracteres. Essa flexibilização atende às prefeituras que já utilizam a **NFS-e no Padrão Nacional**, eliminando bloqueios de limite de tamanho e garantindo que a série informada seja armazenada e escriturada integralmente nas obrigações acessórias (como o Registro A100 do SPED - EFD Contribuições, ECD e ECF). O sistema mantém total compatibilidade com notas que utilizam séries menores (de 1 a 3 posições).

**Observação:** o sistema não permitirá salvar o cabeçalho caso seja lançada uma nota de compras para um contrato de Comercialização do tipo **"Compra a Fixar"**, utilizando uma TOP que esteja configurada com a opção **"Nenhum"** no campo Atualização do Financeiro e Fixação no campo Movimento Armazém. .

Após o lançamento da nota, você poderá alterar as datas mencionadas acima, apenas se o parâmetro **"Obriga Dt.Negoc. igual a do servidor em COMPRAS? - DTNEGSERVCPA"** estiver desligado.

![Imagem 2: Após o lançamento da nota, você poderá alterar as datas mencionadas acima, apenas se o parâmetro "Obriga Dt.Negoc.…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225484183)

Quando você iniciar o lançamento de um documento, será possível observar que apenas a grade Cabeçalho estará habilitada para edição. A grade **"Itens"** será liberada para inserção dos produtos quando o cabeçalho for salvo; a grade **"Rodapé"** terá alguns de seus dados carregados automaticamente com o lançamento dos itens, e outras informações poderão ser inseridas manualmente.

**Observação:** no parâmetro **"Limite Superior para consultas (em anos) - LIMSUPANO"** defina o tempo (em anos) que o sistema aceitará lançamentos futuros na [Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) e na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Como por exemplo, quando você inserir o valor 1 (um) no parâmetro e na data 20/06/2016 inicia-se um lançamento futuro com uma data de negociação maior que 21/06/2017, o sistema emitirá uma mensagem e não permitirá este lançamento.

No campo **"Vendedor"**, você poderá informar o vendedor que realizou a venda.

**Nota:** quando houver a tentativa de alteração do Vendedor quando a Nota já foi Aprovada, ao salvar a alteração, o sistema exibirá a seguinte mensagem:

> **"NF-e/NFS-e com status APROVADA não pode pode ter o vendedor alterado quando o parâmetro TIPTABPRECOS or 'Região do vendedor'ou Tipo de Negoc./Vendedor', ou quando houver cálculo de preço dinâmico."**

A funcionalidade do campo **"%Desc. Promoção"** está diretamente ligada ao cadastro realizado na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais) que, se efetuado corretamente, o desconto será aplicado no item.

**Nota:** Quando você preencher o campo **"Parceiro Descarregamento (MDF-e)"** e o parceiro da nota for do exterior, ao gerar o XML do MDF-e as tags do `<infMunDescarga>` e a tag `<UFFim>` serão preenchidas com os valores pertinentes a cidade do Parceiro Descarregamento (MDF-e).

Você deve preencher o campo **"Indicador de Intermediador/Marketplace"** se o campo "Indicador de Presença para NF-e/NFC-e" estiver com uma das opções a seguir:

- "2 = Operação não presencial, pela internet.";
- "3 = Operação não presencial, Teleatendimento.";
- "4 = NFC-e em operação com entrega a domicílio.";
- "9 = Operação não presencial, outros.".

O campo **"Intermediador de Transação"** também deve ser preenchido, caso nos campos Indicador de Presença para NF-e/NFC-e e **"Indicador da Transação"** estiverem com as opções **"1 = Operação Presencial"** e **"1 = Operação com intermediador"**, respectivamente selecionadas.

**Importante:** Para que sejam exibidos, os campos Indicador de Intermediador/Marketplace, Intermediador da Transação e Indicador de Presença para NF-e/NFC-e deverão ser configurados da tela [Configurador de Layout de Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

Ao criar uma nota de devolução por meio do botão **"Novo documento"**, para que o sistema realize a validação desta nota, ligue o parâmetro **"Valida NF de devolução sem documento referenciado - VALNFDEVDOCREF"**. Além de que, na TOP utilizada na referida nota, as seguintes configurações devem ser realizadas na aba  [NF-e/NFC](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP):

- Sendo esta TOP de Compra ou Venda, a opção **"Normal"** do campo **"NF-e"** deve estar selecionada;
- Defina o campo **"Modelo de Documento"**, com a opção **"55-Nota Fiscal Eletrônica"**;
- Realize a habilitação da marcação **"Buscar NF-e de origem p/ referenciar na NFe"**.

Dessa forma, ao salvar o cabeçalho na Central de Compra com a referida TOP definida, o sistema emitirá a seguinte mensagem:

> **"Está sendo emitida uma nota de devolução sem vínculo com a nota de origem. Verifique, pois a SEFAZ exige esta informação para validação."**

Se todas as configurações acima forem realizadas e você tentar salvar a TOP de devolução na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) com a marcação **"Buscar NF-e de origem p/ referenciar na NFe"** desabilitada, a seguinte mensagem será exibida:

> **"Este cadastro se refere a uma devolução de emissão própria, mas o campo 'Buscar NF de origem p/ referenciar na NFe' está desmarcado. Se este campo ficr desmarcado, pode haver rejeição da nota, pois a SEFAZ exige esta informação".**

No campo **"Chave CT-e referenciado"**, pode-se informar chave do ct-e quando ocorrer Devolução de compra ou venda, com os respectivos **"Tipo de Movimento"**, **"E- Devolução de Compra"** ou **"D- Devolução de Venda"**. Desse modo, a tag `<refCTe>` do XML será preenchida.

Será possível visualizar o campo **"Chave NFe Referenciada Inexistente"** após a integração do Portal de Importação de XML para as Centrais, neste campo é apresentado a informação da Chave, Tipo de Operação e Data Documento separados por vírgula.

**Observação:** ao importar um XML no [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) para as [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) e este possuir Chave Referenciada Inexistente no Sistema, este valor será visualizado no campo informado acima.

O campo **Controle do Indicador de Destinatário** é exclusivo para a emissão de NFS-e e define se o serviço foi prestado para o tomador principal ou para um terceiro. Ele atua em conjunto com o campo **Parceiro Destinatário**.

Quando você seleciona a opção **"1 - Destinatário não é o tomador"** e preenche um parceiro válido, o sistema inclui automaticamente o grupo de tags de endereço desse destinatário no XML da prefeitura (suportando inclusive parceiros estrangeiros ou de outros municípios).

Caso utilize a opção **"0 - Destinatário próprio tomador"**, o sistema fatura a nota apenas com os dados do tomador padrão.

> **Nota:** para que os campos **Controle do Indicador de Destinatário** e **Parceiro Destinatário** fiquem visíveis e acessíveis para preenchimento no cabeçalho da nota, é estritamente necessário que eles tenham sido previamente adicionados à estrutura da tela por meio do [**Configurador de Layout da Nota**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Grade de Itens

Uma vez salvos os dados na grade Cabeçalho, a grade Itens será habilitada pra preenchimento. Nela, informe os produtos ou serviços que irão compor o documento que está sendo lançado.

![Imagem 3: Uma vez salvos os dados na grade Cabeçalho , a grade Itens será habilitada pra preenchimento. Nela, informe os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225523607)

**Nota:** quando o parâmetro "Desabilita a paginação da grade de itens da central - DISABLEGRIDPAG" estiver ativado, o sistema deixará de realizar a paginação. Durante a inserção ou exclusão de itens, a grade será totalmente recarregada para apresentar as alterações. O parâmetro é utilizado para resolver problemas de congelamento de tela que podem ocorrer em notas com grande volume de produtos, evitando conflitos com a rotina de paginação da grade.

Localizado na parte superior da Grade Itens, temos o botão **"Configuração do Formulário"** que, ao ser acionado, abrirá um pop-up com esta mesma nomenclatura, que permite dentre os campos disponíveis, a escolha de quais campos serão selecionados, bem como sua disposição na grade, quando esta se encontrar em Modo Formulário. Estas alterações podem ser realizadas seguindo o que foi previamente definido na tela Configurador de layout da nota, ou seja, nestas modificações, você pode trabalhar com os campos que fazem parte do layout.

**Observação:** Quando você clicar no botão **"Restaurar padrão"** localizado dentro do botão acima mencionado, o sistema deletará as configurações de seu usuário (se este for o logado no momento), fazendo com que este utilize as mesmas configurações realizadas pelo usuário SUP. Assim, para que sejam utilizadas as configurações pretendidas, é necessário que você acesse os layout's com o usuário SUP e defina-os da maneira que deseja. Desta forma, quando acessar o sistema com outro usuário, basta clicar no botão Restaurar padrão para que busque as novas configurações do usuário SUP.

Na parte superior da Grade Itens, temos o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496683634583) **"Configurar Grade"** que permite a seleção de duas formas de visualização, sendo: Modo Grade e Modo Formulário. Caso você opte pelo Modo Grade é necessário considerar os seguintes pontos:

1. Se o parâmetro **"Usar ENTER como TAB na grade de itens da central - ENTERTABGRADITE"** estiver ligado, a tecla Enter executará as mesmas funcionalidades da tecla Tab, permitindo o deslocamento do cursor nas colunas contidas na Grade Itens. Quando desligado, a tecla Enter funcionará como a tecla Tab apenas em colunas de pesquisas; nas demais colunas executará o comando **"Salvar"**.
2. Para alguns campos de pesquisas como por exemplo Referência do Produto e Referência do Fornecedor, é necessário também que você configure o parâmetro **"Código e/ou referência nos ítens? - CODPROREF"** selecionando no campo **"Valor"** a opção **"Referência"**.

   **Observação:** O campo **"Referência do Fornecedor"** possui disponibilidade permanente na grade de itens da Central, independentemente da configuração de layout utilizada. Mesmo que o campo não esteja selecionado entre os campos do layout no Configurador de Layout da Nota, ele continuará disponível para uso. Este comportamento é padrão do sistema e não constitui uma falha ou inconsistência.
3. Em relação ao campo de pesquisa Produto, no parâmetro de chave CODPROREF selecione a opção **"Código"** no campo **"Valor"**.
4. Se os campos de pesquisas mencionados anteriormente estiverem sem preenchimento, ao utilizar a tecla Enter o sistema abrirá a tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos).

Além disso, os registros de importação do XML podem ser configurados na Grade Itens de acordo com a sequência fiscal. Para isso, habilite na seção Ordenação de Dados as colunas desejadas e clique no ícone à direita para determinar se essa ordenação será **"Ascendente"** ou **"Descendente"**.

![Imagem 5: Além disso, os registros de importação do XML podem ser configurados na Grade Itens de acordo com a sequência fiscal.…](https://ajuda.sankhya.com.br/hc/article_attachments/8373028148503)

**Nota:** Caso você habilite o parâmetro **"Aceitar valor total igual a zero? - ACEITARVLRZERO"**, no lançamento de itens na Central será permitido que o valor total de um produto seja igual a zero; caso esteja desabilitado, não será permitido que o valor total do item esteja zerado.

Note a presença do botão **"Atualizar Itens"** no topo da Grade de Itens; as informações sobre o referido botão podem ser acessadas por meio do link [Botão Atualizar Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600294-Bot%C3%A3o-Atualizar-Itens).

**Observação:** Quando o parâmetro **"Calc.Preço embutindo índice do Grupo ICMS por Emp. - CALCPRECICMS"** for ligado, o sistema não irá considerar o desconto para a redução da base de cálculo do ICMS no lançamento de uma nota na Central de Compras.

**Nota:** Ao realizar a inclusão de produtos controlados por Série, é aberto para pesquisa o pop-up **"Número de Série"**; neste, se você acionar a lupa para pesquisa das respectivas séries, será possível selecionar múltiplas séries e incluí-las de uma vez na nota; esta seleção é realizada mantendo pressionada a tecla **"Ctrl"** no teclado e clicando nas séries desejadas, onde, em seguida, é acionado o botão **"OK"** para encerrar a inserção.

**Observação:** caso seja inserido um produto controlado por Série cujo número já conste no estoque, o sistema informará que não é possível prosseguir com a confirmação da nota de compra. Para que o processo continue, é necessário informar uma série não existente em estoque.

**Observação:** Ao realizar o lançamento dos itens em sua grade correspondente, se você informar um percentual de desconto para este produto, neste campo de percentual é possível definir a sua quantidade de casas decimais; para esta definição, é necessário configurar o parâmetro **"Máscara p/ percentual de desconto. - MASCARAPERCDESC"**, onde você define a máscara a ser utilizada para o campo mencionado. Por padrão, este parâmetro é definido com o valor **##0.00** que representa duas casas decimais. Para utilizar neste campo quatro casas decimais por exemplo, informe a máscara **##0.0000**. Os descontos aqui informados também serão apresentados na utilização da rotina de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).

A configuração do parâmetro MASCARAPERCDESC impacta tanto a apresentação da quantidade de casas decimais na grade de Itens quanto o cálculo do percentual de desconto, uma vez que a quantidade de casas decimais definida afeta diretamente os valores calculados.

É fundamental configurar corretamente esse parâmetro quando for liberado ao usuário a possibilidade de digitar os valores nos campos **"Vlr. Desconto"** ou **"Preço Liq."**, pois a precisão nos cálculos dependerá dessa configuração.

Além disso, caso a informação do campo % Desconto seja inserida manualmente, o sistema arredondará o valor do campo Vlr. desconto, e a situação contrária também ocorre, ou seja, se o campo Vlr. desconto for digitado, o sistema arredondará o valor do campo % Desconto.

Para não ter que modificar a configuração do produto em casos que seja necessário que o valor unitário líquido tenha mais de três casas decimais no XML, deve-se ligar o parâmetro **"Desativ arred. val unit liq na tela. - DECVLRLIQARR"**, assim, o arredondamento será desativado e o XML será preenchido com o valor exato.

**Observação:** Após realizar as configurações necessárias para o correto cálculo de diferenciação de alíquota de ICMS, e lançar uma nota, nos itens da nota você poderá inserir o **"Cód. Alíq.Dif. ICMS"**. 

Ao finalizar a inclusão dos itens e salvá-los, você terá a grade **"Rodapé"** alimentada.

Ainda nesta grade, será apresentado o painel **"Matéria-Prima"** quando o produto que compor os itens tratar-se de um kit. Desta forma, quando o produto selecionado na grade tiver componentes, você poderá observar o painel Matéria-Prima. Por outro lado, caso o produto indicado não seja um kit, este painel não será visualizado.

**Observação:** Este painel apenas será observado após o produto kit ser salvo na grade Itens das Centrais de Notas.

**Atenção:** Atualmente, o sistema não realiza transferências de produtos Kit, pois esta se trata de uma operação que executa a explosão do Kit.

**Nota:** Para que este painel seja apresentado nas Centrais de Notas, grade Itens, você deve habilitar os seguintes parâmetros:

- Tem aba Mat.Prima na Transferência? - TEMMPTRAN
- Tem aba Mat.Prima na requisição? - TEMMPREQ
- Tem aba mat.prima na central atend. ao Cliente? - TEMMPVENDA
- Tem aba mat.prima na central atendimento ao Forn.? - TEMMPCOMPRA
- Mostrar grid de mat. prima somente quando existir - SHOWGRIDMATPRI

No campo **"Produto"**, você adicionará produtos que deseja incluir na nota.

Ainda sobre este campo, quando um produto que possui controle adicional por grade é selecionado, o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496679285015) **"Grade"** será exibido na tela, ao selecionar este, o pop-up **"Grade"** será aberto assim como ocorre na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), porém nas Centrais não haverão as seções para as Configurações dessa grade, sendo que estas serão realizadas na tela Cadastro de Produtos.

[GIF animado: Imagem 7: Ainda sobre este campo, quando um produto que possui controle adicional por grade é selecionado, o botão "Grade" será…](https://ajuda.sankhya.com.br/hc/article_attachments/1500019512742)

Clicando em **"Confirmar"**, o campo Controle será alterado com a informação definida no pop-up. Por exemplo, se você selecionar o Tamanho Médio e a Cor Azul, o campo Controle será modificado para “TAM/COR = TM:M/CR:AZ”. 

No campo **"Cód. Tributação ISS"** pode-se definir o tipo de código de tributação de ISS por meio das seguintes opções:

- 07 - Não Tributado;
- 06 - Isento;
- 00 - Tributado;
- 01 - Tributado com ISS Retido.

Além disso, caso você tenha configurado mais de um item no pop-up, será gerado um registro para cada variação de produto. Para visualizá-los, basta mudar o formulário para o **"Modo grade"**. 

**Observação:** Quando for informado um produto controlado por grade, o campo **"Quantidade"** ficará bloqueado, pois a quantidade deve ser informada no pop-up Grade. 

**Observação:** Caso a definição padrão do campo [Grade Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostosinformaesporempresa) seja definida na aba **"Impostos / Informações por empresa"**, esta configuração será utilizada nas operações de compras e venda.

**Nota:** Quando você desejar excluir um item da grade nas Centrais, e este estiver cadastrado na grade padrão mínima, o sistema exibirá a mensagem para que você seja informado que a grade padrão é fechada para a quantidade mínima, porém ainda assim desejar realizar a exclusão, todos os itens também serão excluídos.

**Observação:** Para o lançamento de produtos bonificados com a redução do custo médio do produto utilizando a fórmula interna do sistema ou uma personalizada, é necessário que as seguintes configurações sejam realizadas na [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizada:

- O campo **"Precifica"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) precisa ter a opção **"Atualiza somente custo"** selecionada;
- Além da marcação **"Bonificação"** da mesma aba habilitada.

Dessa forma, se a nota de compra for lançada com uma fórmula interna, o campo **"Fórmula de Custo/Preço"** da aba [Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaformaodecustopreo) do [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) utilizado deve permanecer sem configuração, para que assim, o sistema utilize o custo do produto ao copiar o valor dos custos da última entrada, o que irá reduzir o valor do custo médio, uma vez que o custo de bonificação é zero.

Porém, se o campo Fórmula de Custo/Preço possuir uma fórmula configurada, o sistema atualizará o custo do produto de forma que irá copiar o valor dos custos da última entrada e calcular o custo médio conforme a fórmula.

Em relação ao campo **"Alíquota da ST de oper. ant."**, quando você preenchê-lo, ao realizar a confirmação de uma nota ou gerar seu lote, será informado no XML o valor especificado neste campo na tag **<pST>**. Por outro lado, ao confirmar uma nota sem informar o valor neste campo, a tag acima informada será preenchida com os valores inseridos nos campos **"Vlr. do ICMS da ST de oper. ant.",** **"Base de Cálc. da ST de oper. ant."** e **"Vlr ICMS destacado da oper. própria de oper. ant."** conforme a fórmula abaixo:

((VLRSUBSTANT+ VLRICMSANT) / BASESUBSTITANT) \* 100

Em relação à funcionalidade do campo **"%Desc. Promoção"**, é preciso que o cadastro na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034) esteja corretamente efetuado, sendo assim, o desconto será aplicado no item em questão.

**Observação:** quando o desconto promocional por quantidade for aplicado e o campo **"Tipo Desconto"** estiver configurado como **"Percentual"** (definição realizada na tela [Desconto promocional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais)), o campo **"Vlr. unitário"** desta grade será alterado para o valor informado na tela de Desconto promocional. Os campos  %Desc. Promoção e Vlr. desconto desta grade permanecerão inalterados.

Referente ao campo **"Cód. Alíq. Icms"**, temos que, ao clicar duas vezes no código cadastrado neste, o sistema abrirá a tela **"Alíquota de ICMS"** no registro correspondente ao item selecionado. Porém, caso você não possua acesso à tela de Alíquotas de ICMS ou no campo não contenha um registro, um aviso será emitido.

No campo **"Vlr. ICMS Diferido"** informe o valor para a Emissão de Nota de Importação com ICMS Diferido.

**Importante:** para que o valor inserido no campo acima seja somado ao Total da Nota, você deve, obrigatoriamente, informar no campo **"CFOP"** o código iniciado com 3 e selecionar no campo **"Tributação"** a opção **"51-Diferimento"**, caso contrário, o valor não será acrescentado ao Total.

Através do campo **"Indicador Repasse Desoneração"** se define, por meio das opções disponíveis, se o valor do ICMS desonerado será deduzido ou não do valor do item. As opções são:

- O valor do ICMS desonerado não deduz do valor do item/total da NF-e;
- O valor do ICMS desonerado deduz do valor do item/total da NF-e.

**Observação:** este campo deve ser preenchido conforme o campo **"Forma de Repasse Desoneração"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral) da tela de [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), quando houver cálculo de desoneração.

O campo **"Vlr. Tot.Líq. Desejado"** é utilizado para calcular ou recalcular o **"Vlr. desconto"** de um item, levando em conta certos requisitos tributários como **"Vlr. IPI"** e **"Vlr. substituição"**. Este valor não é salvo na tabela TGFITE, sendo usado apenas para o cálculo do Vlr. desconto.

O somatório dos campos **"Base do ICMS/ST do Frete"** e **"Vlr. ICMS/ST sobre o frete"** será calculado separadamente do total da nota, caso a marcação **"Calc.ICMS extra nota p/ frete extra nota proporcional aos itens"** localizada no [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias) se encontre habilitada.

Ao utilizar o parâmetro **"Calcula diferença para itens repetidos? - CALCDIFITEREPTD"**, ao incluir, alterar ou excluir um item, o sistema irá verificar se não há outros produtos com o mesmo código na nota, e posteriormente calculará se será necessário ajustar o valor do ICMS do item inserido alterado, ou àquele que possui o item de menor sequência com aquele código de produto.

O cálculo que o sistema realiza será feito a partir da soma de todas as bases de ICMS dos produtos, multiplicado pela alíquota e subtraído pela soma do valor do ICMS.

Os campos **"Quantidade"**, **"Vlr. Unit. Moeda"** e **"Vlr. Tot. Moeda"** podem ser utilizados nas [Operações em Moeda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112833-Opera%C3%A7%C3%A3o-em-Moeda) realizadas no Sankhya Om, para isso, no cadastro da TOP que será utilizada nessa operação, habilite a marcação **"Operação em Moeda"** na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) da tela [Tipos de Operações- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP). Ainda sobre os campos mencionados anteriormente, temos as seguintes observações:

- **Quantidade:** Você pode inserir um valor neste, caso o campo **"Digitação na nota"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abavenda) estiver definido com as opções **"Quantidade"**, **"Quant. e Valor Unitário"** ou **"Quant. e Valor Total"**. Assim como, se o movimento da operação for de transferência e o parâmetro **"Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR"** for ligado;
- **Vlr. Unit. Moeda:** Será possível configurar esse campo, se o campo Digitação na nota for definido com as opções **"Valor Unitário"** ou Quant. e Valor Unitário. Assim como, caso o movimento utilizado na operação for compra, Transferência ou se a nota for de Complemento;
- **Vlr. Tot. Moeda:** Será habilitado para edição se o campo Digitação na nota estiver definido com uma das opções **"Valor Total"** ou Quant. e Valor Total. Assim como, se a nota for de Transferência e o parâmetro Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR estiver ligado.

**Observação:** O campo Quantidade também ficará desabilitado se o parâmetro **"Tabela p/compra de serviço por CR - TABCRFORN"** for ligado, assim como as opções **"Usa Tabela p/ compra por CR?"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abainformaes) e **"Validar Tabela de compra por CR?"** da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

**Nota:** Caso você queira excluir dois ou mais itens de uma vez de um lançamento, basta que você selecione todos esses itens e clique sobre o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496732303767) **"Excluir"** ; após isso, o sistema realizará toda a rotina de atualização e recálculos para os itens que foram excluídos.

Para que seja informada a sequência do FCI referente ao item que esta sendo lançado, busque no campo **"Controle FCI"** o cadastro do FCI realizado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Controle FCI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#AbaControleFCI).

**Observação:** compensações financeiras realizadas nas Centrais não geram registros na tabela acerto de frete (TGFFRE).

---

**![Imagem 9: Informações adicionais: Cálculo com Unidades Alternativas](https://ajuda.sankhya.com.br/hc/article_attachments/28806588076439) Informações adicionais: Cálculo com Unidades Alternativas**

Ao trabalhar com Unidades Alternativas, onde são cadastradas várias unidades alternativas iguais, porém com lotes e quantidades diferentes, o sistema realizará o cálculo com base no valor unitário da respectiva unidade alternativa, considerando seu lote e quantidade. Considere o seguinte exemplo:

(1)**Cadastro de Produto:** Produto 1

(1)** Unidades Alternativas**:

| **Unidade** | **Quantidade** | **Lote** | **Vlr. Unitário** |
| --- | --- | --- | --- |
| LT | 0,97 | (vazio) | R$ 10,00 |
| LT | 0,98 | 123 | R$ 10,30 |
| LT | 0,99 | 1234 | R$ 10,60 |

(1)** Cenário:**

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

Acesse também:

[Inserção de Itens na Central por Referência (Cód. Barras do Produto)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602754-Inser%C3%A7%C3%A3o-de-Itens-nas-Centrais-por-Refer%C3%AAncia)

[Inclusão Facilitada de Itens nas Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599354-Inclus%C3%A3o-Facilitada-de-Itens-nas-Centrais)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Grade Rodapé

A grade **"Rodapé"** é completamente habilitada para utilização logo após o salvamento dos dados na grade de **"Itens"**. Algumas informações serão geradas automaticamente e poderão ser modificadas caso necessário, enquanto que outros dados deverão ser manualmente informados. Ela é composta por 8 (oito) abas. Trataremos abaixo sobre cada uma delas:

[Totais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abatotais)                                                                                      [Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abatransporte)

[Notas Conhecimento Transp.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abanotasconhecimentotransp.)                                            [Coleta/Entrega](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abacoletaentrega)

[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abaimpostos)                                                                                [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abafinanceiro)

[Comissões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abacomisses)                                                                             [NF-e/NFS-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abanf-enfs-e)

**Aba Totais**

Nesta aba são agrupados os valores finais a respeito do documento lançado, tomando-se por base os valores e percentuais referentes aos preços e descontos aplicados nos itens, respectivamente.

![Imagem 10: Nesta aba são agrupados os valores finais a respeito do documento lançado, tomando-se por base os valores e percentuais…](https://ajuda.sankhya.com.br/hc/article_attachments/31087844464151)

Atualmente, ao faturar um pedido de compra com a TOP configurada com **"Uso de Separação"**, o sistema não considera o valor informado no campo **"Total desc. serviços"** (aba Totais, grade Rodapé) da tela Central de Compras. Esse desconto é aplicado apenas para notas de serviço ao faturar o pedido pelo [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953).

**Observação:** o sistema não realiza o rateio de descontos que aparecem no rodapé da nota após a confirmação, especialmente quando o item é um serviço (CODUSOPROD = S). Isso resulta na não aplicação dos descontos nos valores desses itens.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Transporte**

Você terá na aba Transporte os dados a respeito do frete do documento que está sendo lançado, tais como, o **"Parceiro Transportadora"**, a **"Quantidade de Volumes"** destinados à carga da nota, qual será o **"Tipo do frete"**, ou seja, se **"Incluso"** ou **"Extra nota"**, se será CIF**\*** ou FOB**\*\***, entre outras informações.

CIF**\*** - O frete é pago por quem envia a mercadoria, ou seja, o Remetente.

FOB**\*\*** - O frete é pago por quem recebe a mercadoria, ou seja, o Destinatário.

**Importante:** a funcionalidade de sugestão preferencial para o **"Parceiro Transportadora"** é considerada apenas em novos lançamentos de documentos ou quando o referido campo estiver em branco. Após ser preenchido, mesmo que o Parceiro do cabeçalho seja alterado, esse campo não será atualizado automaticamente.

![Imagem 11: Importante: a funcionalidade de sugestão preferencial para o "Parceiro Transportadora" é considerada apenas em novos…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225833623)

**Importante:** em Notas Fiscais Eletrônicas, nos itens onde existam **"Campos Adicionais"** e **"Observações"** informadas, estas podem ser modificadas mesmo que o documento já esteja confirmado. Ainda em se tratando de NF-e's, tendo este documento sido aprovado e sendo composto por frete **"Extra Nota"**, caso necessário, os campos **"Vlr. do Frete"** e **"Vencimento do Frete"** podem ser ajustados. Ao solicitar o salvamento das alterações realizadas no documento, será apresentado o pop-up de nome **"Salvar documento confirmado"** onde você define quais informações serão salvas.

Teremos ainda que, ao confirmar uma nota de compra o sistema irá recalcular os impostos e atualizar o valor da GNRE no financeiro, sendo que, esta condiz ao ICMS ST EXTRA NOTA.

**Nota:** É necessário que você siga as orientações do artigo [Melhores Práticas para Configuração e Cálculo do ICMS-ST Extra Nota (GNRE - Venda)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094153-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-C%C3%A1lculo-do-ICMS-ST-Extra-Nota-GNRE-Venda-) para a geração da GNRE EXTRA NOTA.

O somatório dos campos **"Base do ICMS/ST do Frete"** e **"Vlr. ICMS/ST sobre o frete"** será calculado separadamente do total da nota, caso a marcação **"Calc.ICMS extra nota p/ frete extra nota proporcional aos itens"** localizada no [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias), se encontre habilitada.

**Observação:** Para ter os campos Base ICMS e Valor ICMS populados ao importar um XML de CTe, é necessário seguir primeiramente ligar o parâmetro **"Ratear ICMS de frete nas notas associadas ao CT-e - RATICMSFRETCTE"**. O tipo do ICMS no CTe determinará se as tags base de ICMS e valor de ICMS serão consideradas; ICMS00, ICMS20, ICMS60, e ICMS90 irão portar ambos valores.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Notas Conhecimento Transp.**

Nesta aba, informe a ou as notas que pertencem ao conhecimento de transporte. É importante ressaltar que, quando informada mais de uma nota, estas devem possuir o mesmo emitente (remetente) e destinatário.

Você pode informar nesta aba as notas fiscais que possuam o modelo de documento fiscal **"1"** (Nota Fiscal Convencional), ou o modelo de documento **"55"** (Nota Fiscal Eletrônica).

![Imagem 12: Você pode informar nesta aba as notas fiscais que possuam o modelo de documento fiscal " 1 " (Nota Fiscal…](https://ajuda.sankhya.com.br/hc/article_attachments/4408230813847)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Coleta/Entrega**

Informe nesta aba as notas correspondentes à coleta ou entrega diferentes do endereço de origem e destino do [Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e), se assim a empresa desejar.

![Imagem 13: Informe nesta aba as notas correspondentes à coleta ou entrega diferentes do endereço de origem e destino do…](https://ajuda.sankhya.com.br/hc/article_attachments/4408230817687)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Impostos**

Com base nas configurações de impostos anteriormente realizadas para cada Produto, considerando ainda a localização da Empresa e Parceiro, tem-se os dados da aba Impostos. Configurações como ICMS, ISS e IPI por exemplo, são essenciais para alimentação desta aba.

![Imagem 14: Com base nas configurações de impostos anteriormente realizadas para cada Produto , considerando ainda a localização da…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225856791)

Quando o parâmetro **"Seguro incide ICMS - SEGINCICMS"** estiver ligado, o valor do seguro é somado juntamente com o valor do ICMS.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Financeiro**

Esta aba permite que você ajuste o valor das parcelas, seus vencimentos bem como alguma outra anotação relevante no histórico. Além disso, ela exibe os dados do financeiro do documento, de acordo com as configurações definidas essencialmente na [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), nos [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494) e, consequentemente, no [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173).

![Imagem 15: Esta aba permite que você ajuste o valor das parcelas, seus vencimentos bem como alguma outra anotação relevante no…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225868183)

A informação **"Nro.Único"** possibilita que você consulte o título na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) e a informação **"Nro.Único Bancário"** permite que você o encontre na tela de [Movimentação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653), lembrando que este último, só será preenchido quando o título for quitado.

Em processos de emissão de nota fiscal eletrônica de serviços o campo **"Nro NFS-e"** indicará o número da nota fiscal eletrônica de serviço. É um campo protegido e será alimentado em conformidade com o informado no campo Nro. NFS-e do cabeçalho da Nota.

**Observação:** o parâmetro **"Força atualização da provisão na confirmação da nota?? - FORCATPROVCONF"** quando ligado irá garantir que após o processo de confirmação da nota, o campo **"Provisão"** não tenha seu valor alterado por qualquer outra rotina de banco.

![Imagem 16: Os campos citados anteriormente podem ser incluídos na aba Financeiro , através da tela Configurador de Layout da Nota .](https://ajuda.sankhya.com.br/hc/article_attachments/25834621612311) Os campos citados anteriormente podem ser incluídos na aba Financeiro, através da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634).

Esta aba possui também dois botões para realização de algumas modificações caso necessário. São eles:

[![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496773929751)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598674-Parcelar-com-V%C3%A1rios-Tipos-de-T%C3%ADtulos) [Parcelar com Vários Tipos de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598674-Parcelar-com-V%C3%A1rios-Tipos-de-T%C3%ADtulos)        e         ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496776110231) [Alterar Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598874-Alterar-Parcelas)

**Observação:** Os campos texto apresentados nesta aba podem ter sua apresentação influenciada pelo parâmetro **"Usa text area grande no financeiro?- USABIGTEXTAREA"** que, ao ser ativado, exibe os campos em tamanho grande na aba; quando você desabilitar o parâmetro, os campos são exibidos em tamanho pequeno. Qualquer campo adicional do tipo texto que possua a forma de apresentação igual a caixa de texto, será exibido de acordo com a definição feita no referido parâmetro.

**Nota:** Quando na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) a opção **"Proibir impressão boleto?"** estiver selecionada, o tipo de título da nota não irá gerar um boleto assim como não gerará a taxa de boleto, portanto, ao confirmar a nota, você poderá observar que neste Tipo de Título em questão, as linhas **"Cód. Barras Receb."** e **"Linha Dig. Receb."** estarão em branco.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba Comissões**

A aba Comissões pode ser utilizada nos casos em que a empresa queira gerar algum tipo de gratificação aos seus compradores, em consequência da realização de boas aquisições junto aos fornecedores; compras efetuadas a custos reduzidos, por exemplo.

![Imagem 19: A aba Comissões pode ser utilizada nos casos em que a empresa queira gerar algum tipo de gratificação aos seus…](https://ajuda.sankhya.com.br/hc/article_attachments/4408230855959)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap)

**Aba NF-e/NFS-e**

Esta aba é alimentada em casos de lançamento de NF-e normal de emissão própria. Além disso, quando se tratar do lançamento de uma NF-e de Terceiros, o campo **"Chave NF-e"** estará habilitado para digitação.

![Imagem 20: Esta aba é alimentada em casos de lançamento de NF-e normal de emissão própria. Além disso, quando se tratar do…](https://ajuda.sankhya.com.br/hc/article_attachments/4408225943063)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Botões no topo da tela

Os botões ![Imagem 21: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402438980247), ![Imagem 22: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402438988055), ![Imagem 23: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402438994711), ![Imagem 24: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/4402439008663) realizam a Inclusão, Exclusão, Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre os botões a seguir, para saber mais sobre o comportamento de cada um deles:

| [![Imagem 25: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983346455)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#criardocumentoemnovapgina) |  | [![Imagem 26: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983347735)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras) |
| --- | --- | --- |
| [![Imagem 27: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983349143)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#confirmar) |  | [![Imagem 28: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919913495)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#ratear) |
| [![Imagem 29: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983353367)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#recalcularcustos) |  | [![Imagem 30: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983353751)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#liberaes) |
| [![Imagem 31: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919916055)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#produtos) |  | [![Imagem 32: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919916695)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#parceiros) |
| [![Imagem 33: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919917591)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#md-e) |  | [![Imagem 34: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919919255)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#aes) |
| [![Imagem 35: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983360919)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#outrasopes) |  | [![Imagem 36: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919920663)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#visualizarmapacomrotaendereo) |
| [![Imagem 37: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919921943)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#CancelarNota) |  | [![Imagem 38: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919922711)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#NF-e) |
| [![Imagem 39: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/guide-media/01GW9SJAXA60D4XCD0GKTS3P7G)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#NFS-e) |  | [![Imagem 40: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983368087)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#CT-e) |
| [![Imagem 41: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983368983)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#NFC-e) |  | [![Imagem 42: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919924887)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#alternarentreosdocumentos) |
| [![Imagem 43: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983372823)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#exibirhistrico) |  | [![Imagem 44: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311919926039)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#mostrarlistadepaineis) |
| [![Imagem 45: Os botões , , , realizam a Inclusão , Exclusão , Salvamento e Descarte dos dados na tela, respectivamente. Clique sobre…](https://ajuda.sankhya.com.br/hc/article_attachments/42311983375127)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#mapadeatalhos) |  |  |

---

**Criar documento em nova página**

Acionando este botão, será aberto um novo documento sem descartar o anterior. Sendo possível alternar entre os documentos que estiverem abertos através do botão **"Alternar entre os documentos"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Impressão na Central de Compras**

O botão **"Imprimir"** apresenta algumas opções para impressão e tratamento dos dados presentes na tela; explicaremos sobre cada uma destas opções logo abaixo:

[Imprimir Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#imprimirnota)                                                                                [Imprimir Boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#imprimirboleto)

[Imprimir Expedição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#imprimirexpedio)                                                                      [Imprimir Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#imprimirnotaadicional)

[Desvincular Impressoras Substitutas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#desvincularimpressorassubstitutas)                                      [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#relatriosformatados)

[Exportar Registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#exportarregistros)

**Imprimir Nota**

Através desta opção, você poderá imprimir as notas que tem por base o formato TXT. Para imprimir uma ou mais notas em modelo TXT, selecione as notas desejadas mantendo pressionado o botão **"Ctrl"** do teclado, e clicar na referida opção. Vale citar que, cada modelo pode ter sua particularidade.

Para uso desta funcionalidade, atente-se para os seguintes aspectos:

- Na configuração do Tipo de Operação - TOP utilizado na nota, aba **"Impressão"**, no campo **"Modelo de impressão de nota fiscal"** informe um modelo TXT previamente cadastrado; este cadastro é realizado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-).
- O modelo informado na TOP deve ser inserido manualmente na pasta do servidor de aplicação do Sankhya-OM. Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) você poderá verificar o caminho referente à esta pasta, através do parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**; o caminho está indicado no campo **"Texto"**. Salve os modelos de TXT na pasta informada no parâmetro mencionado. Um exemplo de caminho para a configuração deste parâmetro é /home/mgeweb/modelos/, onde os modelos estão salvos na pasta modelos.

É possível também realizar impressões de notas obedecendo à ordem da tela de seleção; para isso, ative o parâmetro **"Respeitar a ordem da grade em selec.várias Notas? - MULTSELORD"** que, uma vez habilitado, fará com que as notas sejam impressas de acordo com sua ordenação/apresentação na grade. Abaixo temos um exemplo:

As notas de número 5487, 6587, 5481 e 44 não estavam ordenadas por número nota na grade e estavam sendo apresentadas conforme esta sequência informada. Ao solicitar a impressão das mesmas, com o parâmetro ativado, o sistema obedecerá a sequência que está na grade e a impressão ocorrerá na mesma ordem (5487, 6587, 5481 e 44).

Caso o parâmetro MULTSELORD esteja desligado, as notas serão impressas sempre obedecendo a sequência do número nota e não a sua apresentação na grade, ou seja, ainda no exemplo citado, ao solicitar a impressão das notas 5487, 6587, 5481 e 44, as mesmas serão impressas obedecendo à numeração crescente das notas, ou seja, primeiro será impresso a nota de número 44, em seguida a 5481, a 5487 e por último a 6587, mesmo que as mesmas não estejam ordenadas pelo número da nota de forma crescente na seleção de notas na grade.

**Observação:** Para que as notas sejam impressas conforme ordenação da grade, o parâmetro **"IMPDANFEBOL - Imprimir DANFE e depois boletos?"** deve estar desligado, pois este quando ligado tem prioridade sobre o parâmetro MULTSELORD.

Na geração do XML de uma NF-e e na impressão de seu respectivo DANFE, os itens da nota serão ordenados mediante a configuração realizada no parâmetro **"Ordem dos itens para impressão nas notas - ORDITENS"**; você pode ordenar os itens de acordo com sua **"Sequência"**, **"Código"**, **"Descrição"**, **"CFOP"**, entre outras alternativas. Quando definida a ordenação pela opção **"Referência do Produto"**, esta irá ocorrer desde que no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba Geral, o campo **"Referência"** esteja devidamente preenchido.

**Importante:** Vale salientar que, o parâmetro **"Ordena Itens nas Centrais? - ORDITENSCENTR"** não influência na ordenação dos itens ao realizar o faturamento. No entanto, se um dos parâmetros **"Agrupar prod. repetido em qualquer faturamento? - AGRUPFATSEMP"** e **"Agrupa produtos em comum para um item - AGRUPAPROD"** estiver habilitado, o sistema irá ordenar os itens de acordo com o seu código. Deste modo, o sistema somente manterá a ordenação dos itens escolhida, se os dois parâmetros mencionados estiverem desligados.

Além disso, o parâmetro AGRUPFATSEMP funcionará como um 'espelho' da nota de origem nas devoluções.

Exemplo:

Se na data do lançamento da nota de origem, o parâmetro estiver ligado, os itens serão agrupados e, na devolução também ficará agrupado. Todavia, se estiver desligado no lançamento da nota de origem, os itens não ficarão agrupados na devolução, mesmo se nesse momento ele estiver ligado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Imprimir Boleto**

Um boleto é um documento utilizado no Brasil como instrumento de pagamento de um produto ou serviço prestado. Através do boleto, seu emissor pode receber do pagador o valor referente àquele pagamento. Tal documento pode ou não ser emitido pelo sistema no faturamento de uma Nota como forma de pagamento ou recebimento. Você deve se atentar ao fato de não ser possível emitir boletos com data de vencimento anterior a sua emissão ou com **"Tipo de Negociação"** à vista.

Dentre as medidas normais para impressão de boletos, está a existência de impressoras dedicadas a esta funcionalidade. O sistema irá imprimir o Boleto para a **"Conta"** cadastrada no financeiro da nota ou do lançamento financeiro, baseando-se no modelo informado no **"Cadastro da Conta"**, aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas), campo **"Modelo"**.

Você pode acessar mais informações sobre as configurações para impressão de boletos através do link [Impressão de Boletos nos Portais e Central - Compras | Vendas | Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599634-Impress%C3%A3o-de-boletos-nas-centrais-Compras-Vendas-Mov-Int-).

A impressão de boletos poderá ser realizada também através do menu [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-).

Relacionada à impressão de notas e boletos, temos o parâmetro **"Imprimir DANFE e boleto agrupados? - AGRUPADANFEBOL"** que, quando habilitado, faz com que o sistema agrupe o DANFE e o Boleto, se existirem, no momento da impressão de acordo com cada nota. Com o parâmetro desabilitado, serão impressos todos os boletos e, em seguida, todos os DANFE's. Esse parâmetro possui tal funcionalidade quando é utilizado o Faturamento direto do sistema.

**Observação:** A medida em que as impressões de boletos e notas vão sendo realizadas, arquivos de anexos de mensagens vão sendo gerados e armazenados internamente no sistema; estes arquivos são desnecessários a partir de um certo momento para o sistema e consomem espaço significativo em disco. No parâmetro **"Dias p/ vencimento de arquivos temporários - DIASVENCTFILE"** informe o tempo que o arquivo ficará armazenado internamente. Após este período, ele será excluído para não ocupar espaço desnecessariamente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Imprimir Expedição**

As notas de expedição são utilizadas para controle interno de estoque e separação do material vendido; normalmente é um espelho da Nota Fiscal. A configuração da impressão da expedição é feita da seguinte maneira:

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abaestoquepreo) informe no campo **"Impressora"** o caminho da impressora onde será impressa a expedição; no campo **"Modelo"** informe o modelo previamente configurado na tela Modelos de Nota Fiscal/Duplicatas/Boleto(s) (para impressão de expedições, o modelo configurado pode ser na extensão TXT ou [Relatório Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados-)); por fim, determine o **"Tipo de Impressora"** que será utilizado para efetuar a impressão.

Dois parâmetros influenciam na impressão da expedição, são eles:

- **Pede senha p/imprimir Expedição p/Pedidos - EXPEDSENHA:** Se você habilitar este parâmetro, o sistema solicitará a digitação de usuário e senha para efetuar a impressão da expedição no tipo de movimento em que esta for solicitada.
- **Imprimir expedição sem confirmar a nota? - IMPEXPSEMCONF:** Caso este parâmetro esteja ativado, será permitida a impressão de expedição para pedidos/notas/devoluções sem que estas estejam confirmadas. Caso esteja desligado, e seja feita a tentativa de impressão da expedição, será emitida a seguinte mensagem:

**"Documento XXX: Para imprimir expedição, confirme  a notas antes de imprimir."**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Imprimir Nota Adicional**

A Nota Adicional é uma possibilidade de impressão de informações complementares a respeito de uma determinada nota, caso a empresa opte por utilizar controles adicionais. Pode ser uma nota adicional referente ao cupom fiscal, ou mesmo à uma nota fiscal, nota de transporte de mercadorias, ordem de separação ou um espelho da nota para o cliente.

Para realização da impressão da Nota Adicional, temos três configurações principais:

- Caso o parâmetro **"Nota Adicional por Empresa? - NOTAADICEMP"** esteja habilitado, na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893) será apresentada a aba [Estoque/Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893#abaestoquenotaadicional), contendo os campos para configurar o modelo e impressora para notas adicionais. Com esta configuração realizada, o sistema passará a considerar essa opção quando a opção **"Imprimir nota adicional"** for acionada. Caso o parâmetro não esteja habilitado, será considerada a empresa **"1"**, buscando as informações contidas na tela [Modelo e Impressora Nota Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597534-Modelo-e-Impressora-Nota-Adicional) que será citada a seguir.
- Na tela Modelo e Impressora Nota Adicional você deve informar os campos **"Impressora"**, onde insere-se o caminho da impressora onde será impressa a Nota Adicional; o **"Modelo"** a ser utilizado para impressão de Notas Adicionais, que deve ser previamente configurado na tela Modelos de Nota Fiscal/Duplicatas/Boleto(s) (o modelo configurado pode ser na extensão TXT ou Relatório Formatado); determine o **"Tipo de Impressora"** que será utilizado para efetuar a impressão; por fim, definindo pela **"Numeração Automática"**, caso no **"Tipo de Operação - TOP"** tenha sido feita a marcação para impressão da nota adicional (configuração citada a seguir), ao efetuar a confirmação da nota, a nota adicional correspondente será impressa automaticamente.
- No cadastro de Tipo de Operação - TOP, na aba **"Impressão"**, temos as marcações **"Imprimir Nota Adicional"** e **"Imprimir nota adicional antes de confirmada"**; com a primeira marcação, sempre que a respectiva TOP for utilizada, será acionada a rotina de impressão de Nota Adicional; caso a segunda marcação citada esteja realizada, será impressa a Nota Adicional correspondente à Nota Fiscal que não estiver confirmada.

**Nota:** É possível imprimir Notas Adicionais para mais de uma nota ao mesmo tempo; para isso, selecione mais de uma nota na grade **"Resultado da Seleção"** mantenha pressionado o botão **"Ctrl"** do teclado, e em seguida clique na opção **"Imprimir Nota Adicional"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Desvincular Impressoras Substitutas**

A opção Desvincular Impressoras Substitutas desfaz o vínculo existente entre as impressoras substitutas e a impressora cadastrada nos Modelos de Impressão.

Se ao enviar uma nova impressão, seja esta de notas ou boletos, e o pop-up para selecionar a impressora não for aberto, significa que certamente a última impressão foi feita selecionando a opção **"Salvar Seleção?"**, o que impede a escolha de uma nova impressora. Neste caso, acesse a opção de Desvincular Impressoras Substitutas, para que a impressora possa ser novamente escolhida.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Relatórios Formatados**

No [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) e na Central de Compras, no botão de impressão, a opção **"Relatórios Formatados"** irá apresentar os Relatórios Formatados vinculados a instância **"CabeçalhoNota"**.

Os Relatórios Formatados apenas serão exibidos caso a expressão definida no vínculo seja satisfeita. Através do link [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados-), você pode verificar como definir tal vínculo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#impressonacentraldecompras)

**Exportar Registros**

Esta opção quando acionada, realizará a baixa do XML correspondente ao documento que está sendo exibido na tela. É uma funcionalidade mais utilizada pelo nosso setor de Service Desk.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

---

**Confirmar**

Através deste botão você realiza a confirmação do documento que está sendo lançado. Todas as configurações feitas no lançamento do documento serão executadas no momento de sua confirmação, ou seja, será feita a validação do que ficou definido entre Empresa e Parceiro, com base no Tipo de Operação - TOP, Tipo de Negociação, Produtos, etc., que foram inseridos no documento em questão. É a confirmação de um documento que irá disparar, por exemplo, sua impressão, o envio de e-mail's, a baixa, a impressão de boleto, impressão de nota adicional, faturamento da confirmação, geração da cotação, etc.]

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Ratear**

O acionamento deste botão abre o pop-up **"Rateando"** para que, com base nos [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio) preestabelecidos, seja feita a distribuição das receitas e despesas pelas Naturezas, Centros de Resultado ou Projetos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Recalcular Custos**

O acionamento deste botão efetua o recálculo dos custos e/ou preços conforme definidos no Tipo de Operação - TOP. Esta é uma ferramenta que permite a realização do recálculo de custos de produtos, a partir de movimentações de entrada como, Notas de compra, Transferência, etc. Tal funcionalidade é útil em casos de alterações em fórmulas de precificação (fórmulas de custo/preço) necessárias devido à redefinições em políticas de custeio e precificação. Caso haja a necessidade de se refazer custos de produtos em consequência de erros de lançamento de uma Nota Fiscal, por exemplo, pode-se fazer uso desta ferramenta.

**Observação:** Se você habilitar o parâmetro **"Calcula Custo Médio na C.A.Fornecedor na Confirmação? - CALCCUSTOMEDCAF"** e utilizar a opção de **"Recalcular Custos"**, além de calcular o custo de entrada, irá calcular também o custo médio. Se desativado, o processo de confirmação ficará mais ágil, pois, ao não calcular o custo médio, não é feita uma leitura de estoque, entradas e saídas, na confirmação da nota, processo este realizado na realização do referido cálculo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Liberações**

O botão Liberações será apresentado habilitado e o atalho **"Ctrl+Shift+L"** também utilizado para acioná-lo, somente funcionarão quando o documento já estiver salvo e não estiver confirmado. Mesmo que você não possua acesso à tela de [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites), esse botão ficará habilitado, pois a tela exige a digitação de usuário e senha. Somente serão exibidas as liberações de limites correspondentes às liberações cadastradas para o usuário que digitou a senha.

Um exemplo de uso deste botão que acontece muito frequentemente, é no momento da confirmação de uma nota, tendo a solicitação de alguma liberação de limite; você aciona o gerente que pode liberar aquela solicitação e ele clicando no botão Liberações digita o usuário e senha, efetua a liberação e retorna para a Central de Compras para que você proceda com a confirmação da nota.

**Observação:** Para evitar que a liberação de limites ocorra de forma indevida ao clicar duas vezes sobre o registro na tela de Liberação de Limites, ligue o parâmetro **"Na Liberação de Limites, avisar no duplo clique - AVISACLIQUELIB"**, assim, o sistema exibirá o pop-up Liberar Limites para que seja analisado o evento solicitado. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Produtos**

O acionamento deste botão, abre o Catálogo de Produtos, ou seja, tem a visualização da tela Consulta de Produtos. Este botão tem por objetivo facilitar a busca e identificação de itens, para sua posterior inserção no documento que está sendo lançado. Quando você clicar em qualquer campo de qualquer uma das três grades (Cabeçalho, Itens, Rodapé) e utilizar as teclas de atalho **"Ctrl + Alt + P"**, também será aberta a tela de [Consulta de Produtos.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353)

**Nota:** Na Consulta de Produtos aberta ao pesquisar um produto na Central de Compras, você pode acrescentar um critério adicional que permitirá filtrar os produtos da consulta de acordo com a Nota/Pedido selecionados. Esta modificação requer que você tenha um nível de conhecimento avançado.

Primeiramente, configure o parâmetro **"Critério adicional para catálogo de produtos** **-** **QRYCONSPROD"**. Nele, coloque o pedaço da cláusula **"WHERE"** que irá filtrar os produtos. Nesse **"WHERE"** estará disponível o parâmetro **":NUNOTA"** que representa a nota selecionada na Central.

#### Exemplo 1:

"AND ((TGFPRO.CODGRUPOPROD = 100 AND 'P' = (SELECT TIPMOV FROM TGFCAB WHERE NUNOTA = **:NUNOTA**)) OR ('P' != (SELECT TIPMOV FROM TGFCAB WHERE NUNOTA = :NUNOTA)))"

O critério adicional acima faz com que sejam apresentados na consulta de produtos de todos os Pedidos de Venda ('P'), somente produtos que pertençam ao Grupo de Produtos de código 100.

#### Exemplo 2:

"AND ((TGFPRO.CODVOL = ‘CX’ AND 102000 = (SELECT CODCENCUS FROM TGFCAB WHERE NUNOTA = **:NUNOTA**)) OR ('102000' != (SELECT CODCENCUS FROM TGFCAB WHERE NUNOTA = :NUNOTA)))"

O critério adicional acima faz com que sejam apresentados na consulta de produtos das Notas/Pedidos/Requisições que tenham Centro de Resultado=102000, somente produtos que tem Unidade Padrão=CX.

Após configuração do parâmetro QRYCONSPROD, a Consulta de Produtos aberta pelas Centrais já irá considerá-lo no filtro.

**Importante:** A Consulta de Produtos, quando aberta através do menu **"Comercial > Consulta > Consulta de Produtos"** não considera o critério definido nesse parâmetro, ela sempre apresenta todos os Produtos/Serviços.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Parceiros**

O acionamento deste botão, abre a tela [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601934-Ficha-de-Parceiros) já posicionada nas informações pertinentes ao Parceiro informado no documento. Nota-se na Ficha de Parceiros que é aberta, o botão **"Usar parceiro"** que ao ser acionado, o Parceiro em questão será inserido no documento que está sendo lançado na Central de Compras; esta inserção do Parceiro na Central também pode ser feita por meio do atalho **"Ctrl + Shift + U"**.

**Nota:** A referida tela quando aberta pela Central de Compras, permite pesquisar somente parceiros condizentes com a definição do campo **"Tipo"** presente na aba **"Identificação"** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao), ou seja, para os movimentos de Nota de Compra e Pedido de Compra será filtrado o parceiro do tipo Fornecedor e para o movimento de Devolução de Compra os parceiros do tipo Fornecedor e Cliente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**MD-e**

O botão MD-e, é peça chave na utilização da rotina [Manifestação do Destinatário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112353-MD-e-Manifesta%C3%A7%C3%A3o-do-Destinat%C3%A1rio), possuindo as seguintes opções:

- **Ciência da operação:** Através desta opção será registrado o evento de ciência de operação para a nota fiscal lançada na Central;
- **Confirmo a operação:** Aqui, fixa-se o evento de Confirmação de Operação para a nota fiscal lançada na Central;
- **Desconheço a operação:** Esta opção registra o evento de Desconhecimento de Operação para a Nota Fiscal lançada na Central;
- **Operação não realizada:** Através desta, determina-se o evento de Operação não Realizada para a nota fiscal lançada na Central;
- **Visualizar manifestos:** Através desta opção, abre-se uma pequena janela, para que se possa consultar os eventos relacionados à Manifestação do Destinatário.

**Importante:** Para que estas opções sejam apresentadas no menu do botão MD-e, é necessário que o parâmetro **"Controla acessos dos eventos do MD-e? - ACESSOEVENTOMDE"** esteja ligado, além disso, na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854), os usuários devem estar com os acessos especiais concedidos.

**Observação:** Caso a nota de compra esteja confirmada e a opção selecionada de manifestação de operação na tela [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) seja Ciência da operação, Confirmo a operação, Desconheço a operação, Operação não realizada ou Prestação Serviço Desacordo, será emitida a seguinte mensagem:

**"Esta operação de manifesto não pode ser realizada em uma nota confirmada".**

Assim, o sistema impedirá a manifestação destes eventos. Por outro lado, caso a nota não esteja confirmada, o comportamento do sistema seguirá conforme descrito anteriormente para cada uma destas opções.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Ações**

Através deste botão, você pode escolher as ações configuradas previamente na tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294). Estas ações são configuradas de acordo com a rotina e processo de cada empresa.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Outras Opções**

Note a presença deste botão no alto da tela e no topo da grade Itens. As opções contidas em cada um dos botões podem ser acessadas por meio da [Central de Compras | Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593994) e [Central de Compras | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974), respectivamente.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Visualizar mapa com rota/endereço**

Através deste botão você realiza a análise da localização do **"Endereço de entrega"** e do **"Endereço do parceiro"** (endereço principal), bem como as **"Rotas"** do endereço da empresa com base nos endereços de entrega e principal do Parceiro. Ao acionar uma das duas opções deste botão, será aberta a tela **"Configurações > Consulta > Mapa Visualizador de Endereços"** onde será possível visualizar o ponto referente ao endereço escolhido (principal ou de entrega).

As informações necessárias para que você efetue as configurações de integração do botão **"Visualizar mapa com rota/endereço"** com a ferramenta Google Maps podem ser acessadas através do link [Como configurar o botão Mapas Integrado ao Google Maps](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602714-Bot%C3%A3o-Mapas-nos-portais#comoconfigurarobotomapasaogooglemaps).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Cancelar Nota**

O acionamento deste botão invalida o documento. Você pode obter mais informações acerca deste processo nos link's [O que é Cancelar uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#oqueumanotafiscaldevenda) e [Como realizar o Cancelamento de uma Nota Fiscal?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas#comorealizarocancelamentodeumanotafiscal).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Opções para Nota Fiscal Eletrônica**

Tem-se através deste botão, todas as opções acerca das Notas Fiscais Eletrônicas. No uso do Tipo de Movimento **"Canceladas"**, este botão é habilitado caso algum documento seja selecionado na grade Resultado da seleção.

**Nota:** Ao selecionar uma nota que esteja com o **"Status NF-e" = "Aguardando Correção"** e clicando na opção **"Gerar lote"** disponível neste botão, caso a data e/ou hora estejam diferentes da data e/ou hora do servidor, o parâmetro **"Obriga Dt.Negoc. ser igual a do servidor? - DTNEGSERV"** terá o seguinte comportamento:

- Encontrando-se habilitado, será realizada a alteração da data e/ou hora do documento de forma automática.
- Caso encontre-se desabilitado, será apresentado um pop-up questionando se você deseja manter a data e/ou hora do documento ou se deseja ajustar estas informações para que estejam de acordo com as informações do servidor.

Desta forma, será possível alterar as datas de negociação, faturamento e entrada/saída de acordo com o mesmo comportamento da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) ao realizar a confirmação de uma nota com data diferente do servidor.

**Importante:** Deve-se realizar a atualização destas datas e horas pois, se um boleto estiver vinculado à estas datas e for efetuado a correção do cadastro dias depois, a nota e o boleto serão recebidos com datas de saídas incorretas, ocasionando a perda do prazo negociado.

Quando a opção **"Enviar XML da NF-e/CC-e e Danfe por e-mail"** for selecionada, será enviado ao e-mail cadastrado o XML da NF-e e CC-e, o PDF da NF-e (DANFe) e, também, o PDF da **"Carta de Correção"**, caso exista alguma gerada.

**Observação:** Caso utilize esta rotina sem um modelo de impressão de Carta de Correção inserido na tela **"Preferências da Empresa"**, aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), campo **"Relatório Carta de Correção"**, o sistema não encaminhará o PDF no e-mail e não emitirá qualquer mensagem de aviso.

**Nota:** Caso você tente realizar a impressão de um documento fiscal que esteja com status que não permite impressão, será apresentado um aviso, por exemplo:

**“Documento XXX: Nota com status DENEGADA não pode ser impressa, favor verificar o documento. NFe ignorada na impressão.”**

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Opções para Nota Fiscal Eletrônica de Serviços**

Por meio deste botão, temos acesso às opções que podem ser utilizadas quando realizado o lançamento de uma [Nota Fiscal Eletrônica de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Opções para Conhecimento de Transporte Eletrônico**

Este botão exibe as alternativas relacionadas ao [CT-e - Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e).

**Observação:** Inserindo um CNPJ nas configurações do parâmetro **"CNPJ ANTT p/ autorização de download de XML. - CNPJANTT"**, ao **"Gerar o Arquivo XML de CT-e para conferência"** através deste botão, será possível visualizar na tag **<autXML>** deste arquivo o mesmo CNPJ inicialmente configurado no parâmetro.

**Nota:** Será possível realizar a impressão da Carta de Correção CT-e selecionando a opção **"Imprimir a Carta de Correção"** localizada neste botão; para isto, você deve, primeiramente, baixar o modelo de impressão através da tela [Modelo de Impressão (Nota/Pedido)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-), botão **"Baixar Modelos Padrões"**, opção **"Carta de Correção CT-e"** e, após, inserir o mesmo no campo **"Relatório Carta de Correção"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abact-e).

Através da opção **"Comprovante Entrega CTe"** disponível neste botão, será possível indicar que a entrega da carga foi efetivada pelo transportador; assim, o sistema irá gerar e transmitir o evento que será vinculado ao CT-e e propagado nas notas fiscais eletrônicas relacionadas de forma automática.

Ainda neste botão, temos a opção **"Cancelar Comprovante Entrega CTe"**, que deverá ser selecionada caso haja necessidade de cancelar o evento de Comprovante de Entrega de CT-e anteriormente vinculado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Opções para Nota Fiscal Consumidor Eletrônica**

Através deste botão, teremos acesso às opções utilizadas ao lançar uma [NFC-e Nota Fiscal de Consumidor Eletrônica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido-).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Alternar entre os documentos**

O botão Alternar entre os documentos é exibido quando forem abertos na tela mais de um documento; através dele será possível intercalar a visualização dos documentos que se encontram abertos.

Quando acionado, você terá a exibição de um pop-up de mesma nomenclatura contendo os referidos documentos. No lado superior esquerdo do pop-up, você pode observar o campo **"Buscar no histórico"**, quando existirem vários documentos abertos este botão permitirá efetuar a busca de um determinado documento através do seu Nro. Único.

Além disso, na parte superior direita do pop-up existe um contador de registros que irá auxiliar na identificação do número de documentos que se encontram abertos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Exibir histórico**

Este botão exibe o pop-up **"Histórico de documentos abertos"**, nele são apresentados os registros dos documentos que foram fechados recentemente até o último que deve estar em execução. Se trata de um histórico temporário que se inicia desde a abertura da central até o seu o último documento. Esta ferramenta só exibirá o histórico do usuário que está logado e permitirá assim o resgate destes registros que já foram fechados, possibilitando assim sua manutenção ou simples conferência. Para visualização do registro desejado basta um clique que o mesmo será carregado na central.

Você pode verificar no lado superior esquerdo do pop-up o campo **"Buscar no histórico"**, quando existirem vários documentos abertos este botão permitirá efetuar a busca de um determinado documento através do seu Nro. Único.

Além disso, na parte superior direita do pop-up tem-se um contador de registros que irá auxiliar na identificação do número de documentos que se encontram abertos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Mostrar lista de painéis**

Localizado no lado superior direito da tela, o botão Mostrar lista de painéis exibe a listagem dos painéis que compõem a tela Central de Compras. Quando você clicar na opção desejada, o sistema direciona o foco para a mesma.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela)

**Mapa de atalhos**

Além das opções até aqui citadas, que podem ser acessadas via botões, você também poderá fazê-las via atalhos do teclado. Esta opção, assim como a anterior, se encontra no lado superior direito da Central de Compras.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#botesnotopodatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Como lançar um documento na Central de Compras?

Tomaremos como exemplo neste tópico, o lançamento de uma Nota de Compra na Central de Compras; os demais documentos trabalhados nesta tela (Pedido de Compra e Devolução de Compra), seguem o mesmo padrão de lançamento, diferenciando-se basicamente nas validações de estoque e financeiro que podem realizar. Trataremos abaixo, os dados fundamentais que deverão existir no sistema:

- Inicialmente é necessário que se tenha o Cadastro de Empresas; em seguida, as Preferências da Empresa onde são definidas as particularidades de cada corporação no sistema, bem como, se a mesma estará ativa para uso nesta e nas demais rotinas, respectivamente;
- O Parceiro na Nota de Compra, é o Fornecedor do qual a empresa cadastrada inicialmente está concretizando a compra;
- O Tipo de Operação - TOP assim como em todas as operações, é um cadastro de extrema importância, pois determina o **"Tipo de Movimento"** (que em uma Nota de Compra, é C-Compra), as atualizações de Financeiro, Estoque, Matérias-Primas, Preços, entre outros aspectos;
- É essencial o cadastro do Tipo de Negociação, ou seja, a forma de pagamento acordada entre a empresa e o fornecedor;
- Por fim, efetue o cadastro dos Produtos que serão adquiridos junto ao Fornecedor.

Uma vez cadastradas essas informações, como citado inicialmente nesta documentação, a Central de Compras não é aberta diretamente; é necessário que você posicione no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) para abri-la.

Com base nessa informação, ao acessar o Portal de Compras e acionar o botão ![Novo](https://ajuda.sankhya.com.br/hc/article_attachments/15481546011927), **"Novo documento"** será aberta a Central de Compras para início do lançamento.

Exceto os Produtos, os demais cadastros mencionados acima deverão, obrigatoriamente, compor o Cabeçalho da nota. Os demais campos devem ser informados de acordo com o processo adotado por cada empresa. Ao finalizar esta etapa do lançamento e salvar as inclusões, será habilitada a grade Itens para inclusão dos produtos negociados entre Empresa e Fornecedor.

**Observação:** Os parâmetros **"Aceitar prod.repetido para Exec.diferente?-ACEITARPRODREPE"** e **"Aceitar produto repetido-ACEITARPRODREP"** quando habilitados, permitem que seja inserida mais de uma linha do mesmo produto no documento. Ainda nesse contexto, considerando que seja inserido o mesmo produto, porém com local de origem e/ou controles diferentes, a inclusão de forma repetida será permitida, independente dos parâmetros mencionados.

As abas apresentadas na grade Rodapé terão algumas informações alimentadas automaticamente (de acordo com os dados inseridos na grade Cabeçalho e na grade Itens da Nota) e outras deverão ser preenchidas de acordo com o processo de cada empresa.

Finalizadas as inserções, você conclui o lançamento por meio do botão Confirmar localizado no alto da tela.

Um lançamento também pode ser iniciado através da própria Central de Compras; quando um documento já se encontra aberto e este não será mais trabalhado, o botão de Inclusão prepara e habilita a tela para um novo lançamento.

**Nota:** O ato de duplicar um documento, também abre a Central de Compras, porém todos os preenchimentos citados até aqui já se encontrarão realizados, bastando apenas (caso nenhuma modificação seja necessária) Confirmar o documento em questão.

Finalizado o lançamento da nota, formulando-se os filtros corretos, esta poderá ser visualizada na grade Resultado da Seleção no Portal de Compras e com um duplo clique sobre o documento, você poderá analisá-lo na própria Central de Compras.

**Observação:** Referente à NF-e de Entrada, ao realizar uma importação de XML por meio da tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), tem-se que se o valor destacado na tag <**vICMSDif**> do grupo de tags <**ICMS**> do item da nota irá compor o mesmo valor contido na tag <**vICMSDeson**> do grupo <**ICMSTot**>, portanto o valor da tag <**vICMSDif**> deverá ser subtraído da <**vNF**> do qual representa o valor total da nota.

Porém, se o valor contido na tag <**vICMSDif**> do item da nota não compor o valor contido em <**vCIMSDeson**>, o valor da <**vICMSDif**> não será subtraído da tag <**vNF**>.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Cadastro Simplificado de Parceiros

Os Parceiros são todas as pessoas físicas ou jurídicas que se relacionam de alguma forma com a empresa. Qualquer organização que comercialize bens e serviços com a empresa. A integração das informações de clientes, fornecedores, representantes etc, traduz a adoção de maior foco sobre os dados fundamentais destes clientes e fornecedores, no sentido de constituir todas as fontes de dados existentes na empresa.

Deste modo, no lançamento de um Pedido de compra, Nota de compra ou Devolução de compra o Sankhya-OM disponibiliza uma forma rápida e prática de se efetuar um cadastro simplificado de um novo Parceiro. Para tanto, é necessário que você acione a tecla **"F2"** no ato de preenchimento dos dados.

**Observação:** Quando você acionar a tecla **"F2"** e posicionar um pedido, nota ou devolução que já esteja com a grade Cabeçalho preenchida, o pop-up **"Cadastro simplificado de parceiros"** será apresentado com os dados do Parceiro já cadastrado.

As informações referentes às abas apresentadas neste cadastro devem ser verificadas no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

## Parâmetros que atuam na Central de Compras

**Data Base p/ Calculo do Vencimento no Faturamento - DTCALCVENC:** este parâmetro determina a data base p/ cálculo do vencimento no faturamento.

**Fora Dt. Fat. c/ Base p/ Cálculo Venc. na compra? - FORCDTFATCOMPRA:** com este parâmetro habilitado, a data de faturamento na compra será forçada.

Quando o parâmetro FORCDTFATCOMPRA estiver habilitado e o parâmetro DTCALCVENC estiver configurado com o valor **"Faturamento"**, se as datas informadas forem retroativas e a data de faturamento não for informada, o sistema considerará a data atual para faturamento na confirmação. Além disso, ao confirmar uma nota cuja data de faturamento seja posterior à data base, o sistema irá refazer o financeiro, excluindo o registro anterior e gerando um novo. Como o sistema não armazena informações do financeiro anterior, quaisquer alterações realizadas serão perdidas. O mesmo comportamento se aplica quando o parâmetro DTCALCVENC estiver configurado como **"Negociação"**.

**Financeiro Nota fiscal diferente da nota - NFEFINDIFNOTA:** este parâmetro realiza uma tratativa no caso onde o valor do financeiro é diferente da nota na geração do XML. Sendo assim, ele pode ser configurado com os seguintes valores:

1. Considerar como desconto e sem pagamento: a diferença entra como valor de desconto sem afetar o valor total da nota;
2. Distribuir diferença entre financeiros: se parcela única, é definido o valor da nota como valor da duplicata; caso tenha mais de um financeiro, o seu valor será retirado do valor da nota;
3. Considerar como desconto: a diferença entra como valor de desconto sem afetar o valor total da nota.

**Integridade casas decimais XML Portal Import - INTEGRDECIMXML:** quando ligado, o arredondamento de casas decimais do índice é desabilitado, carregando assim toda a dizima periódica para o cálculo. Sendo que, esse processo só ocorrerá quando se tratar de uma nota importada pelo [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) e houver explosão de lote na importação. Por padrão, este parâmetro está ligado. Para habilitar a funcionalidade mencionada, é necessário desligá-lo.

**Inclusão facilitada de produtos controlados por lista? - INCFACPROLIS:** quando ligado, uma segunda aba na grade de Itens, denominada **"Facilitado"** será exibida, com o objetivo de facilitar o lançamento de produtos controlados por Lista.

**Apresentação parceiro - APRES.TGFPAR:** por meio deste parâmetro pode-se alterar a apresentação do **"Nome do Parceiro"** na Central; informe em sua configuração, o nome da coluna existente no banco de dados correspondente ao campo desejado. Por exemplo, caso você informe no parâmetro RAZAOSOCIAL, a Razão Social do Parceiro será apresentada. Esta modificação é válida tanto na Central, quanto na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753).

**Qtd. máx. de Centrais abertas - MAXCENTRAIS:** pode-se definir uma quantidade máxima de documentos que poderão ser abertos simultaneamente na Central. Ao exceder este limite, será exibido o pop-up **"Quantidade máxima de documentos atingidos"** com a seguinte mensagem:

**"A quantidade máxima de X documento(s) aberto(s) simultaneamente foi atingida. Selecione um documento para ser substituído."**

Quando a quantidade definida for 1 (um) registro, o sistema irá substituir automaticamente o registro atual pelo registro anterior, sendo que, se o registro atual possuir alterações, a seguinte mensagem será apresentada:

**"O registro atual foi alterado, deseja salvar as alterações?"**

Após a seleção, o novo documento será carregado na Central.

**Validar executante ativo no item da nota? - VALEXECITEM:** quando ligado fará com que o sistema verifique se o código do Vend./Executante informado no campo **"Executante"** da grade **"Itens"** está ativo. Caso o mesmo esteja inativo, a seguinte mensagem será exibida:

**"Vendedor não existe ou não pode ser usado aqui: PK[11]."**

**Manter financeiro de frete na alteração da nota? - MANTFINFRENOTA:** quando acionado, será possível quando em uma nota de entrada, alterar seu tipo de negociação, mesmo que esta possua um financeiro de frete (despesa) já baixado. Caso nesta mesma situação o referido parâmetro esteja desligado, na tentativa de alteração do tipo de negociação, será apresentada a seguinte mensagem:

**"Este lançamento já foi baixado.Não pode ser excluído!"**

**Alterar rateio nota confirmada sem validar metas? - ALTRATSEMVALMET:** este parâmetro permite que seja alterado o rateio de notas confirmadas sem que ocorra a validação de metas.

**Valida acesso alterações em notas não confirmadas - VALACESSONOTA:** define se o sistema verifica o acesso **Alterar** da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) antes de permitir alterações em notas não confirmadas.

- **Ligado:** o usuário só consegue alterar a nota se tiver o acesso **Alterar** liberado. Sem esse acesso, o sistema bloqueia a alteração e exibe a mensagem "O usuário logado não possui permissão para alterar o documento 'Nota de compra'".
- **Desligado:** o sistema não verifica o acesso **Alterar**. O usuário consegue alterar a nota mesmo sem essa permissão.

**Importante:** com o parâmetro ligado, incluir um item na nota também conta como alteração, porque o sistema recalcula os valores do cabeçalho. Por isso, o usuário que precisa incluir itens deve ter os acessos **Incluir** e **Alterar** liberados.

**Pré-visualizar nota e boleto nos Portais - PREVIEWNOTABOL:** quando ligado, habilitará o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15496913916183) **"Pré-visualizar"** nas Centrais e Portais de Notas, para que seja possível realizar a pré-visualização de notas e/ou boletos. Neste botão temos as quatro opções de pré-visualização seguintes:

- Pré-Visualizar Nota;
- Pré-Visualizar Boleto;
- Pré-Visualizar Danfe Simplificado;
- Pré-Visualizar Nota Expedição;
- Pré-Visualizar Nota Adicional.

Para pré-visualizar os documentos, é necessário que o pedido/nota estejam confirmados.

**Utilizar BASERED no rastreamento de estoque? - UTILBASEREDRAST:** quando estiver habilitado, fará com que o rastreamento de estoque considere a Base de Cálculo Reduzida do imposto do item da nota para realizar o rateio do valor da compra com as Notas de Vendas.

**Atualiza Calculo do ISS ao Modificar Item - ITEATUCALISS:** quando ligado permitirá que o valores de ISS (**"Base do ISS"**, **"Alíq. ISS"** e **"Vlr. ISS"**) sejam inseridos de forma manual nos Itens da Nota.

**Importação, tag vOutro do item sem valor do ICMS ligado - VOUTITEMSEMICMS:** quando ligado, o MGE Importação irá gerar a nota na central sem inserir os valores de ICMS e FCP no destaque da nota e, no momento de enviar o XML da NFe, não irá adicionar estes valores a tag **<vOutro>** do item para manter a compatibilidade com a tag **<vOutro>** da nota que não contenha estes valores.

**Observação:** se você não desejar que os valores ICMS e FCP sejam inseridos no destaque e na tag **<vOutro>**, não inclua-os no destaque e mantenha este parâmetro ligado.

**Imposto só em tag exclusiva em nota nacionalização - IMPTAGEXCNOTNAC:** caso esteja habilitado, o  MGE Importação gerará a nota na central sem acrescentar nenhum dos impostos que possuem tag própria no destaque, assim, os valores de PIS, COFINS, ICMS e FCP não serão destacados na nota, sendo assim, não estarão na tag **<vOutro>** dos itens ou da nota.

**Nota:** se você não deseja que os impostos PIS, COFINS, ICMS e FCP sejam incluídos no destaque e na tag **<vOutro>**, não insira estes valores no destaque e habilite o parâmetro IMPTAGEXCNOTNAC.

Caso você efetue o lançamento da nota de nacionalização manualmente na Central, você deverá inserir no destaque o valor de FCP da mesma forma que insere o ICMS.

**Habilita configuração de redução de IPI? - IPINFEREDVALOR:** quando habilitado, e o campo **"% Redução de Vlr. IPI:"** (tela [Alíquota IPI](https://jivasd.zendesk.com/hc/pt-br/articles/360025167513-Al%C3%ADquotas-de-IPI#abageral), aba "Geral") devidamente preenchido, o usuário poderá digitar o % de redução do IPI, desta forma, possibilitará a redução do imposto conforme sua necessidade.

**Permite edição de lote em compra de MPs? - EDITLOTEMPCPA:**Tratando-se de Notas de Compra cuja TOP estiver marcada para **"Numerar lote automaticamente"** e o produto for uma Matéria Prima (MP), só será permitido editar o controle do produto se este parâmetro estiver ligado.

**Força Base/Vlr ISS nulo no fatur. quando zerado - FORISSNULOFAT:** com o parâmetro ligado, se a Base e o Vlr ISS do Item estiverem zerados, será setado nulo nestes campos na hora de faturar. Assim, o cálculo ocorrerá normalmente.

**Considera desoneração no cálculo de custo? - DESONERACUSTO:** se estiver ligado, caso seu cálculo de custo seja feito por fórmula padrão, o sistema irá considerar o campo TGFCAB.VLRREPREDTOT para o cálculo do custo, ou seja, caso na nota em questão haja desoneração que incidiu no Valor Total da Nota, este valor de desoneração será levado em consideração no cálculo do custo do produto, levando seu custo para um valor menor.

**Utiliza domicílio empresa na transf. de vencimento na compra? - UTDOEMPTVENCOMP** em conjunto com o parâmetro **Transfere vencimento quando fim de semana/feriado - TRANSFVENC**, nos casos de realização de compras, quando o primeiro estiver habilitado, fará com que o sistema realize a transferência de vencimento, baseada no domicílio de Empresa, ao invés do domicílio do Parceiro.

**Usa controle de acesso para aba comissões multipla - CTRLACESSCOMIS:** quando ligado poderá controlar os acessos de usuários ao painel Comissões nas centrais. Para fazê-lo, depois de ligar o parâmetro acesse a tela Acessos e localize o módulo **"Notas"** (Comercial> Rotinas> Portal de Compras), selecione um usuário e em seguida limite os acessos que deseja, sendo que estes podem ser **"Editar"**, **"Incluir"**, **"Alterar"**, **"Excluir"** e etc. desta forma, se um dos usuário a quem você limitou o(s) acesso(s) tentar realizar alguma das ações, o sistema não o permitirá.

**Calc. Vlr. Desc. Mov. Compra com 2 casas decimais. - CVLRDISCTWODEC:** quando ligado o percentual de desconto para lançamentos manuais de compra será arredondado em duas casas decimais.

**Aplicar Total desc. serviços p/ impostos federais? - DESCSERVIMPFED:** caso esteja habilitado, fará com que seja possível realizar a proporção do desconto da nota sobre os serviços e impostos da NFS-e, quando esse desconto for informado no Rodapé da Nota, no campo **"Total desc. serviços"**.

Quando o parâmetro **"Ignorar Vend. ao duplicar/faturar doc. nos portais - IGNORAVENDCOMP"** estiver ligado e for realizado o faturamento de uma nota ou duplicação de um pedido/nota nos Portais, caso o vendedor/comprador esteja inativo, o sistema irá completar o processo de faturamento ou duplicação, zerando o campo vendedor e apresentando a mensagem abaixo no Painel de Avisos do documento gerado:

**"O parâmetro IGNORAVENDCOMP - Ignorar Vend. ao duplicar/faturar doc. nos portais" está ligado, e o campo vendedor/comprador foi zerado ao duplicar ou faturar. Lembre-se de preencher o campo vendedor ou comprador caso seja necessário".**

Por outro lado, se o parâmetro estiver desligado e existir um documento já confirmado com um vendedor ou comprador inativo informado, quando for duplicado ou faturado esse documento, o sistema impedirá o procedimento.

**Permite digitar Qtd X Vlr nas trasnferências? - TRANSFDIGQTDVLR:** quando for ligado, os campos **"Quantidade"** e **"Vlr. Tot. Moeda"** serão habilitados na grade de itens das centrais se o Tipo de Movimento for Transferência.

**Limpar campos Fin. ao duplicar registro na Central - DEFCAMDUPFINNOT:** neste parâmetro você pode informar os campos cujo os dados não devem ser copiados no financeiro ao duplicar registros na Central de Compras. Dessa forma, a seguir, você poderá observar os campos que poderão ser informados no parâmetro, uma vez que, estes devem ser separados por vírgulas:

- CODNAT;
- CODCENCUS;
- CODPROJ;
- CODBCO;
- CODCTABCOINT;
- HISTORICO.

Após o lançamento da nota, você poderá alterar as datas de Entrada/Saída, Faturamento, Movimento e Negociação, apenas se o parâmetro **"DTNEGSERVCPA - Obriga Dt.Negoc. igual a do servidor em COMPRAS?"** estiver desligado.

**Considera TOP criada posterior à data de neg no custo médio? - CONSTOPDTPOSTCM:** este parâmetro é utilizado para adequar o cálculo de custos quando há a necessidade de criar um novo Tipo de Operação para uma nota já existente. Quando o parâmetro é ligado, ao confirmar o lançamento de uma nota marcada para atualizar custos, cuja data seja anterior à data de criação da TOP utilizada, será apresentada a mensagem abaixo:

**"A TOP XX, marcada para atualizar custos, possui data de criação posterior à data deste documento. Ao confirmar a operação, o sistema ajustará a data da TOP para correta apuração dos custos. Deseja prosseguir?"**

Assim, caso você prossiga com a confirmação da nota, o sistema irá adequar a data da TOP no banco de dados, para que seja compatível com o respectivo lançamento. Se você optar por não prosseguir com a confirmação, a nota fica pendente para alteração da TOP utilizada.

**Cálculo de Custo assncrono - CALCCUSTOASSINC:** este parâmetro define como o sistema realizará o cálculo de custos. Ele pode ser configurado conforme as seguintes opções:

- **Transação por Nota**: O cálculo de custos será processado por transação, considerando cada nota fiscal individualmente.
- **Transação por Item**: O sistema calculará os custos item por item dentro de cada nota fiscal.
- **Desabilitado**: O cálculo de custo não será realizado de forma assíncrona.

#### Importante

Esse parâmetro impacta diretamente a confirmação de notas e o Agendador de Recálculo de Custos. No entanto, **as rotinas de Recálculo de Custo e Atualização de Custo não são afetadas por essa configuração**.

Quando o parâmetro **CALCCUSTOASSINC** estiver definido como "**Transação por Nota**" ou "**Transação por Item**", o cálculo de custo não ocorrerá imediatamente, sendo realizado de forma assíncrona (fora da transação de confirmação da nota). Devido a esse comportamento, o pop-up de variação de preço não será exibido para o usuário, independentemente de o parâmetro "**Apresenta variação de preço na NF de compra? - APRVARPNFCOMPRA**" estar ligado. O processo ocorre em duas etapas:

1. Inicialmente, o Cálculo de Custo Assíncrono é preenchido com as informações da nota.
2. O cálculo de custo é realizado posteriormente por um **JOB específico**, acionado somente após a confirmação de uma segunda nota.

**Força recálculo financeiro qdo há imposto mensal? - RECALCFINIMPMEN:** quando estiver ligado e houver imposto mensal, será forçado o recálculo do financeiro na confirmação da nota e, caso esteja desligado, o recálculo do financeiro não será forçado, sendo assim, se você não refizer o financeiro, o cálculo será com base no valor total sem o imposto.

**Recalcula valores Cons. Prod. qdo prod. iguais? - RECVALCONSPROD:** quando estiver ligado e um item for editado através da consulta de produtos e seu **"CODPROD"** não for alterado, não serão recalculados os campos **"QTDNEG"** e **"VLRUNIT"**.

**Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT:** por padrão, o parâmetro estará ligado para que não haja o acúmulo de vencimentos. Sendo assim, caso você queira que o sistema realize esse acúmulo, basta desativar o parâmetro. Porém, é importante saber que, quando os parâmetros **"Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT"** e Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT estiverem ligados quando há mais de uma parcela definida com a mesma **"Base do Prazo"** (tela [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas)), a base do vencimento será o valor do campo **"DTPRAZO"** do financeiro gerado. Mas se o Utiliza regra de vencimento para dias fixos? - USARDIAFIXOVCT for habilitado, e o parâmetro Acumula vencimento para dias fixos? - ACVENDIAFIXOVCT desligado, a base do vencimento será a mesma para todas as parcelas configuradas.

**Não calcular ST na compra quando só tem MVA - NCALSTSOMVA:** quando estiver ligado, o sistema não irá calcular o valor de ICMS ST na nota de compra, não buscando uma alíquota de ICMS ST para o cálculo. Dessa forma, será verificado se não existe alíquota de ST e não tem Modalidade de BC ST informada, não gerando o cálculo de ST na Nota de Compra. Caso o parâmetro esteja desligado, será mantido o comportamento atual, calculando BC e valor de ST na nota de compra.

**Observações:**

- A funcionalidade do parâmetro acima não será aplicada para o Pedido de Compra;
- A TOP de compra deve estar com o campo **"Cálculo de ICMS, IPI e ISS"** com a opção **"Calcula e digita"** selecionada.

**Usa cotação da nota de origem - USACOTNOTAORIG:** quando ligado, o sistema irá manter a cotação das notas conforme as opções **"Preço em Moeda"** e **"Preço de Venda"** do campo **"Usar como preço"** definidas nas respectivas [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)'s das notas de origem e destino.

**Dias p/ notificação notas não confirmadas - DIASNOTANAOCONF:** quando for configurado com um valor maior que zero, na tela [Notas Não Confirmadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/10847777335319) o sistema exibirá um painel com as notas não confirmadas conforme a quantidade de dias a partir da **"Data de Negociação"**. Porém, se o parâmetro for configurado com o valor '0', a tela exibirá somente um painel com todas as notas não confirmadas existentes nas Centrais independente da quantidade dos dias.

**Separa por layout as conf. dos form. na Central - SELAYCONFFORM:** ao habilitar este parâmetro, as configurações dos formulários da tela serão gravadas separadamente de acordo com o layout da nota.

**Reter impostos (ISS,INSS,IRF) p/ Parc. da nota? - RETIMPPARCNOTA:** quando estiver ativado, o sistema não efetuará o cálculo dos impostos nos registros financeiros das notas em que o parceiro não seja o mesmo da nota. Se desativado, o cálculo será realizado para todas as parcelas do financeiro. Ressaltamos que, a configuração desse parâmetro deve ser realizada antes de efetuar o lançamento da nota.

**Usar CFOP em pedidos de compra e venda? - CFOPPEDIDOS:** configurar uma TOP de P-Pedido de Venda ou O-Pedido de Compra incluindo os CFOP's em seus campos próprios e selecionar a opção **"Não atualiza"** no campo **"Atualização de Livro ICMS"**, na aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) em [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#top), ao lançar um documento com a TOP configurada, lançar um item e salvar, o sistema preencherá o campo **"CFOP"**.

**Utilizar cache para validar metas de notas com rateio ? - LIGCACHEMETA:** quando este parâmetro estiver ligado, tem-se uma melhora de performance para calcular o valor do realizado para quem usa a rotina de [Planejamento de Metas e Orçamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609814).

**Arredonda parcelas do financeiro na alteração do item? - FINARRPARCELAS:** quando ligado, garantirá o arredondamento das parcelas financeiras da nota quando houver modificação na quantidade do item.

**Calc Desc. ICMS no Calc ST sem IPI - CALINDDESICMSST**: quando o parâmetro estiver ligado, deve ser utilizado para que ao confirmar uma nota onde existem mais de um item e somente alguns dos itens tem incidência de ST, junto também da utilização de tipo de cálculo específico nas configurações da alíquota e proporcionalização de ICMS ST do Frete, o sistema realize os cálculos corretamente e não apresenta a divergência.

**Bloqueia a grade de itens durante a inicialização do produto - LOCGRIDINITITEM:** quando ativado, este parâmetro impede qualquer edição ou alteração na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) antes que todas as informações do produto sejam totalmente carregadas, evitando assim problemas nos cálculos de valores (como o valor unitário).

**Cálculo de custo executado por Job? - CALCCUSTOPORJOB:** quando este parâmetro está ativado, o cálculo do custo não acontece de forma imediata (síncrona). O cálculo será realizado por um JOB, que executa o processo quando chega a vez da nota lançada, considerando que podem existir outras notas aguardando na fila. Ao confirmar uma nota, um registro é gerado na tabela TGFCCA e, durante a execução do JOB, essa tabela será consultada. Se houver registros, o sistema realiza a atualização do custo e insere os dados na tabela TGFCUS. É importante destacar que, com o parâmetro ativado, o cálculo de custo assíncrono é desativado.

Em relação à execução do JOB, ele verifica a cada minuto se há registros na tabela TGFCCA. Caso existam, ele processa as notas considerando o limite informado no parâmetro **"Qtd. de registros da TGFCCA executados por Job - QTDREGCCAPORJOB"**, que define a quantidade de registros por JOB. O limite máximo de notas processadas simultaneamente é 10. Se o valor informado for maior que 10, o JOB processará notas adicionais à medida que o cálculo de uma nota for concluído, até atingir o limite informado no parâmetro. Quando atinge a quantidade definida, o JOB finaliza a execução e reinicia o processamento no minuto seguinte.

Se o parâmetro CALCCUSTOPORJOB estiver desativado, o cálculo de custo assíncrono volta a ser executado. No entanto, caso existam notas pendentes na tabela TGFCCA, elas só serão processadas quando uma nova nota for incluída nesta tabela pelo sistema. Por exemplo, se houver 10 notas na tabela e o parâmetro QTDREGCCAPORJOB estiver configurado como "3", o cálculo assíncrono processará 3 notas e aguardará a inclusão de uma nova nota na tabela para continuar o processamento.

Independente de o cálculo ser assíncrono ou por JOB, as notas serão processadas sempre começando pelas de data mais antiga.

**Valida preench dt val contr.adicional por dt val? - VALCONTDTVAL:** quando este parâmetro estiver ativado, o sistema impedirá que o item seja salvo sem o preenchimento do campo **"Data de Validade"** na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens). Para que essa validação seja aplicada, é necessário atender às seguintes condições no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos):

- Na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), a marcação **"Utiliza data de Validade"** deve estar habilitada;
- Na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), o campo **"Controlar Por"** deve estar configurado como **"Data da Validade"**.

Se ambas as configurações estiverem efetuadas, quando o usuário tentar salvar o item sem informar a Data de Validade, será exibida a seguinte mensagem:

**"O produto X é controlado por Data de Validade e nenhum controle foi informado."**

Se você precisar que o valor do seguro componha o cálculo dos impostos da nota, basta manter o parâmetro **SEGINCICMS** (Seguro incide ICMS) ligado. Com essa configuração ativada, o sistema passa a somar automaticamente o valor do seguro junto ao valor do ICMS. Vale destacar que essa regra de incidência é válida e tem o mesmo comportamento tanto para os documentos de entrada (Central de Compras) quanto para as operações de saída (Central de Vendas).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#top)

![Imagem 48: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/17880910702231) Acesse também:

[Central de Compras | Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593994-Central-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)

[Central de Compras | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)

[Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)
