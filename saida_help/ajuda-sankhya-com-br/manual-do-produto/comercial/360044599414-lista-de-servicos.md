---
id: "360044599414"
titulo: "Lista de Serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599414-Lista-de-Servi%C3%A7os"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:22:00Z"
rotulos: ["manual", "Configuração", "Alíquota de ISS", "Serviços", "Impostos", "Lista de Serviços", "Lista", "SINTEGRA", "br.com.sankhya.com.cad.listaservicos", "Lista de Serviços manual", "Prefeituras", "NFS-e", "Configuração de Layout", "Validação de NFS-e", "Campos Obrigatórios"]
---

# Lista de Serviços

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311771936535) Módulo: Comercial > Arquivo > Cadastros
```

---

A tela Lista de Serviços permite a realização do cadastro da listagem dos Serviços, de modo a permitir o agrupamento destes serviços nas rotinas em que estes forem utilizados; é uma tela de cadastro de forma hierárquica, onde você pode inserir as listas de serviço do nível mais abrangente para o mais específico.

![Imagem 2: A tela Lista de Serviços permite a realização do cadastro da listagem dos Serviços, de modo a permitir o agrupamento…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002516321)

Informe inicialmente, o **"Código"** da Lista de Serviço que está sendo inserido. Este código deverá ser cadastrado obedecendo à hierarquia definida no parâmetro **"Máscara para Lista de Serviços - MASCTGFLST"**.

No campo **"Descrição"**, insira a descrição da Lista de Serviços, visando uma nomenclatura que melhor a identifique nas rotinas em que for utilizada.

Para que o cadastro da Lista de Serviço esteja disponível para inserção em outros cadastros, a marcação **"Ativo"** deverá estar realizada.

A marcação **"Analítico"** quando realizada, define se a lista em questão é analítica ou sintética; sendo sintética, serão aceitos cadastros de subníveis posteriores à este; quando analítica, teremos o cadastro como último nível na árvore hierárquica.

No ato da emissão da nota, ao preencher o campo **"Código (Auxiliar)"**, o código auxiliar  enviado no XML terá preferência em relação ao código cadastrado na tela Lista de Serviços.

**Observação:** A lista de serviços a ser cadastrada nesta tela é definida pela [Lei complementar 116](http://www.planalto.gov.br/ccivil_03/leis/LCP/Lcp116.htm), podendo haver variações por município.

Para a configuração do Código da Obra, você deve se atentar para os seguintes detalhes:

1. Cadastre na tela Lista de Serviços as listas que utilizarão o código da obra, efetuando a marcação **"Exige Cód. da Obra"**. Esta opção só poderá ser utilizada para Lista de Serviços analíticos.
2. Vincule a Lista de Serviços configurada anteriormente aos Serviços que deverão utilizar o código da obra. Este vínculo é realizado no [Cadastro do Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), aba [Alíquotas de ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abaalquotasdeiss), no campo **"Tipo de Serviço"**; informe neste campo, a Lista de Serviços cadastrada.
3. Na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), localize o modelo a ser utilizado para emissão de NFS-e, selecione os campos **"Cód. da Obra"** e **"Cód. Art"** e os insira no quadrante correspondente à aba Cabeçalho.

Feitas as devidas configurações, na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) ([Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)), informe os dados necessários para emissão da Nota Fiscal de Serviço, tais como Empresa, TOP, Parceiro, Tipo de Negociação, Serviço prestado (configurado conforme citado acima), Valores etc.

No lançamento de serviços cujo Tipo de Serviço foi configurado para exigir o Código da Obra, os campos Cód. da Obra e Cód. Art estarão disponíveis para preenchimento no cabeçalho da nota. Caso o Código da Obra não seja informado ao confirmar a nota, será apresentada a seguinte mensagem:

**"Existem serviços relativos à construção civil que foram lançados na nota e que obrigam o preenchimento dos campos: 'Cód. da Obra' e 'Cód. Art'."**

Ao efetuar a marcação **"A tag "Valor Total Recebido" é obrigatória para NFSe SP?"** será gerada a tag **<ValorTotalRecebido>** no XML RPS das [Notas Fiscais de Serviço Eletrônicas (NFSes)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras#sopaulosp) emitidas na cidade de São Paulo.

**Nota:** A NFS-e não será confirmada até que você informe os devidos campos. Caso os dados da nota estejam corretos, ao ser confirmada, esta será transmitida e autorizada na prefeitura.

O botão ![Imagem 3: O botão "Outras Opções..." é composto pelas opções "Marcar Todos (Exige Cód. da Obra)" e "Desmarcar Todos (Exige Cód.…](https://ajuda.sankhya.com.br/hc/article_attachments/16278858385047)**"Outras Opções..."** é composto pelas opções **"Marcar Todos (Exige Cód. da Obra)"** e **"Desmarcar Todos (Exige Cód. da Obra)"**, que assinalam ou desmarcam todos os registros analíticos de uma só vez, respectivamente. Para utilizar estas opções, você deve posicionar em um registro sintético que possua registros analíticos filhos; serão marcados e/ou desmarcados apenas os registros filhos correspondentes ao registro sintético selecionado.
