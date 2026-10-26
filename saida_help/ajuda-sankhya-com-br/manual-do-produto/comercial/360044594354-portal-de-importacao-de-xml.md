---
id: "360044594354"
titulo: "Portal de importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-09-03T11:00:51Z"
rotulos: ["CT-e", "AJUDA DO SKW", "manual", "Configuração", "NF-e", "Processamento", "XML", "Divergência", "Importação", "IPI", "USACRPROJNATCAB", "VALCHAVETERC", "CALCCUSIMPCTE", "CONCNPJIEIMPXML", "DHSAIENTIMPXML", "IMPNEGDIVXMLCMP", "Nota Fiscal de Compra", "PEDLIGAPORLOTE", "Portal de importação de XML", "TOPIMPORTXML", "USALOCALPEDIMP", "VALBONIFPEDNOT", "br.com.sankhya.cac.importacaoxmlnota", "Portal de importação de XML manual", "Financeiro", "HABOPCFINMENNOT", "USALIBLIM", "TOPDIGIMPXMLCTE", "Notas de Compra", "Facilitando o Lançamento: Portal de Importação de XML", "NOMPROCCALDTVEN", "DFeReferenciado", "Documentos Eletrônicos", "DFe Referenciada"]
---

# Portal de importação de XML

```
 Módulo: Comercial > Rotinas 
```

---

Esta rotina visa facilitar e agilizar o processo de lançamento de Notas Fiscais de Compras no sistema, permitindo a importação dos XMLs das notas eletrônicas. Além das notas de compras, também é possível importar as notas de devoluções de vendas emitidas pelo parceiro.

É importante destacar que, para acessar esta funcionalidade, a empresa deve possuir o produto **"IMPORTAÇÃO DE DOCUMENTOS ELETRÔNICOS/W"** incluído na licença de uso. Para esclarecer qualquer dúvida, entre em contato com o departamento Comercial da Sankhya.

![Imagem 1: O Controle de Produtos por Grade não é permitido nesta rotina.](https://ajuda.sankhya.com.br/hc/article_attachments/16364732359831) O [Controle de Produtos por Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045269813) não é permitido nesta rotina.

| Funcionalidades da Tela |
| --- |
| [Configurações necessárias nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#configuraesnecessriasnestarotina) |
| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#filtros) |
| [Inclusão dos arquivos no Portal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#inclusodosarquivosnoportal) |
| [Processamento dos arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#processamentodosarquivos) |
| [Cancelando o processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#cancelandooprocessamento) |
| [Aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#Financeiro) |
| [Tratando divergências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#tratandodivergncias) |
| [Divergências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#Diverg%C3%AAncias) |
| [Outras validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_322985bf-9305-4ebe-b749-bff396e76d09) |
| [Validação do valor unitário dos itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#validaodovalorunitriodositens) |
| [Validação do IPI no XML dos itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#validaodoipinoxmldositens) |
| [Regras de Negócio na Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#regrasdenegcionaimportaodexml) |
| [Exclusão de documentos importados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#exclus%C3%A3odedocumentosimportados) |
| [Abrir Documento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#abrirdocumento) |
| [Local para inserção das notas via importação do XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#localparainserodasnotasviaimportaodoxml) |
| [Botão MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#botomd-e) |
| [Referenciamento de item de outro Documento Fiscal Eletrônico (DFeReferenciado) em notas de devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_01M00Q4G2S7382SZ7PGYM3GGWV) |
| [Validação de IBS e CBS durante a transição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_01M00Q4G35JEMG0AF0JYQECDWC) |
| [Notas de Débito e Crédito (Reforma Tributária)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_01M00Q4G3DN5NJH398GQD1ZFG2) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) |
| [Particularidades do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#particularidadesdoct-e) |
| [Importação do XML do CT-e como emissão própria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#importaodoxmldoct-ecomoemissoprpria) |
| [Importação de cancelamento feito por terceiros de um CT-e de emissão própria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#importaodecancelamentofeitoporterceirosdeumct-edeemissoprpria) |
| [CT-e importado com Pedido de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#ct-eimportadocompedidodefrete) |
| [Rateio do Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#rateiodofrete) |
| [Calcular vencimento do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#calcularvencimentodoct-e) |
| [Cancelar CT-e importado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#cancelarct-eimportado) |
| [Importação de Notas contendo Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#importaodenotascontendomedicamentos) |
| [Importação dos dados do FCP e Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#importaodosdadosdofcpeimpostos) |
| [Importação de XML com Desmembramento de Itens em Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#Importa%C3%A7%C3%A3odeXMLcomDesmembramentodeItensemLotes) |
| [Importação de Notas ICMS Monofásico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#Importa%C3%A7%C3%A3odeNotasICMSMonof%C3%A1sico) |
| [Controle de Documentos Cancelados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_72cbdbf7-e277-4655-9daf-58671cee4f7d) |
| [Seleção de notas de venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#Sele%C3%A7%C3%A3odenotasdevenda) |
| [Parâmetros - Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051315453-Par%C3%A2metros-Portal-de-importa%C3%A7%C3%A3o-de-XML) |
| [Importação de NF-e com a Nota Técnica 2025.002 - (Reforma Tributária)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35135179341463-Importa%C3%A7%C3%A3o-de-NF-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC) |
| [Importação de CT-e com a Nota Técnica 2025.002 - (Reforma Tributária)](https://ajuda.sankhya.com.br/hc/pt-br/articles/35134864204311-Importa%C3%A7%C3%A3o-de-CT-e-com-a-Nota-T%C3%A9cnica-2025-002-RTC) |

---

## Configurações necessárias nesta rotina

![Imagem 2: Modelo de Notas (tela Modelo de Notas e Pedidos ):](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) Modelo de Notas (tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514)):

Cadastre um modelo que será associado à empresa, que servirá de base para a Nota de Compra. Este modelo conterá informações que não estão contidas no XML como: [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (**"Tipo de Movimento"** igual á **"Compra"**), **"Natureza"**, [Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado), entre outras. O [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) informado no modelo poderá ser utilizado na importação em algumas situações.

![Imagem 3: Modelo de importação de XML (tela Preferências da Empresa ):](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) Modelo de importação de XML (tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)):

Na aba [Modelo de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abamodelodeimportaodexml), adicione um ou mais modelos de importação ao cadastro da empresa. Além do modelo de notas e pedidos, informe a **"Natureza da operação"**. É possível cadastrar vários modelos, mas deve haver um modelo padrão por empresa.

Durante a importação do XML, o sistema verifica o campo **<natOp>** do XML e o campo Natureza da Operação, que devem estar em maiúsculas e sem acento ou cedilha. Em seguida, com base na configuração do campo **"Pesquisa da nat. de operação"** (Preferências da Empresa, aba Modelo de Importação de XML), o comportamento será:

- **Igual:** o modelo de importação é usado apenas se os valores dos campos **<natOp>** e Natureza da Operação forem iguais;
- **Contendo:** o modelo é utilizado se o valor de Natureza da Operação estiver contido em **<natOp>**;
- **Começando com:** o modelo é aplicado se <**natOp**> iniciar com o valor do campo Natureza da Operação;
- **Terminando com:** o modelo é usado se **<natOp>** terminar com o valor do campo Natureza da Operação.

![Imagem 4: Considerações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/25753358813463) **Considerações adicionais**

Na importação do XML, considerando notas de compras que possuam produtos configurados com rastro de estoque, deve-se analisar as seguintes informações:

1. São considerados os produtos que utilizam a marcação **"Tem Rastro do Lote"** ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abageral));
2. O sistema registra como quantidades negociadas os valores inseridos nas tags **<qLote>** e **<qCom>**, que compõem o grupo de rastreamento do produto (rastro);
3. Quando o item lançado possuir a tag **<qLote>** com uma quantidade superior aos valores registrados na tag **<qCom>**, o sistema considerará como quantidade do item as informações existentes na tag **<qCom>**.

**Observações:**

Para que o sistema preencha a TOP ao importar o XML de Devolução de Venda é necessário informar na tela Preferências da Empresa, aba Modelo de Importação de XML, campo **"Modelo de notas e pedido"** o modelo de nota/ pedido cadastrado na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514) e, na tela Tipo de Operação- TOP, aba [NF-e/CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce) efetue a marcação **"Desconsidera Nfe de orig. referenciada? (Importação de XML)"**. Porém lembre-se que a importação não ocorrerá caso a quantidade devolvida seja maior que a quantidade registrada na nota. 

Para a importação do XML do CT-e, o sistema não considera o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) informado na aba [Modelo de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abamodelodeimportaodexml) que foi vinculado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893). O sistema buscará a TOP definida no campo **"Tipo Operação"** localizado no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Preferências de Importação do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e), seção**"Movimentação Financeira"**.

**Observação:** na importação de uma devolução de NF-e emitida por terceiros que referencia uma nota de emissão própria, o sistema não utiliza o Modelo de Importação de XML para definir a TOP. A TOP é obtida a partir do campo TOP p/Devolução configurado na TOP de venda da nota referenciada (a nota de origem citada no XML).

Ou seja, para esse cenário, mesmo que exista um Modelo de Importação de XML configurado para a natureza da operação, ele é ignorado. O preenchimento automático da TOP depende exclusivamente de a TOP de venda da nota original ter o campo TOP p/Devolução informado.

| ⚠️ Atenção Ao definir a TOP p/Devolução na TOP de venda, verifique o campo NF-e da TOP apontada. Se ela estiver com NF-e configurado como Terceiros, uma devolução própria que utilize essa mesma TOP de venda como referência poderá ser emitida de forma incorreta. |
| --- |

No entanto, quando o parâmetro **"Preferir TOP digitada na importao de CT-e?- TOPDIGIMPXMLCTE"** estiver ligado, na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) o sistema informará a TOP definida na grade do Portal de Importação.

Já quando o parâmetro TOPDIGIMPXMLCTE estiver desligado e a marcação **"Importar CT-e com Cabeçalho"** da seção **"Nota de Compra"** estiver habilitada, o sistema informará no XML do Portal de Importação o Tipo Operação informado na seção Movimentação Financeira. E na Central de Compras, será apresentada a TOP informada na seção Nota de Compra.

Pode-se alterar a coluna **"Tipo de Negociação"** antes de processar o arquivo. Para isso, clique sobre a lupa ![Imagem 5: Pode-se alterar a coluna "Tipo de Negociação" antes de processar o arquivo. Para isso, clique sobre a lupa e selecione…](https://ajuda.sankhya.com.br/hc/article_attachments/4439251394071) e selecione o Tipo de Negociação desejado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Filtros

![Imagem 6: Filtros](https://ajuda.sankhya.com.br/hc/article_attachments/27080761995159)

Na lateral esquerda da tela, encontra-se o Painel de Filtros, que permite filtrar os registros por diversos critérios, como:

- Usuário Importador;
- Período de Importação;
- Período de Emissão;
- Número Único.

Além disso, há o campo **"Status"** com as seguintes opções:

- **Todos:** exibe todos os arquivos;
- **Pendentes:** mostra arquivos incluídos no Portal de Importação, mas não processados;
- **Importados:** exibe arquivos importados com sucesso e sem divergências;
- **Cancelados:** mostra arquivos cancelados manualmente;
- **Com divergências:** exibe arquivos processados com divergências;
- **Confirmados:** exibe arquivos importados e confirmados.

O filtro **"Apresentar importações"** permite selecionar entre as opções:

- Todas;
- Manuais;
- Baixados pelo MD-e.

No filtro **"Status WMS"**, as opções disponíveis são:

- Todas;
- Enviado parcialmente;
- Enviado Totalmente;
- Não Controlado pelo WMS;
- Não enviado;
- Pedido parcialmente cortado;
- Pedido totalmente cortado.

A seção de **"Divergências"** exibe as inconsistências encontradas no arquivo selecionado. Alguns exemplos de divergências:

- Quantidade do produto devolvido é superior ao total disponível para devolução nas notas de venda;
- Produto da nota de devolução não corresponde aos produtos vinculados às notas de venda referenciadas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Inclusão dos arquivos no Portal

A importação de arquivos pode ser feita individualmente, com um arquivo XML ou um arquivo compactado (ZIP) contendo vários XMLs.

![Imagem 7: Não é possível importar arquivos de outras extensões.](https://ajuda.sankhya.com.br/hc/article_attachments/16364732359831) Não é possível importar arquivos de outras extensões.

Para incluir o arquivo no portal, clique em ![Imagem 8: Para incluir o arquivo no portal, clique em "Cadastrar Importação de XML de Notas" no menu padrão do sistema, escolha o…](https://ajuda.sankhya.com.br/hc/article_attachments/27082299846423) **"Cadastrar Importação de XML de Notas"** no menu padrão do sistema, escolha o arquivo e clique em **"Enviar"**. Ao fim deste processo o status na grade de resultados será **"Pendente"**.

![Imagem 9: Para incluir o arquivo no portal, clique em "Cadastrar Importação de XML de Notas" no menu padrão do sistema, escolha o…](https://ajuda.sankhya.com.br/hc/article_attachments/27082325025943)

Ao incluir um arquivo compactado, o sistema cria uma linha para cada arquivo na grade. O nome do arquivo será o mesmo para todos, mas cada um terá um código único.

Após a importação de um arquivo ZIP, o sistema informa quantos XMLs foram selecionados, quantos tiveram erros, quantos foram processados e quantos ainda faltam para terminar. Em caso de falha, consulte o log de erros na tela [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos).

Para facilitar a identificação dos documentos importados, pode-se inserir na grade principal da tela a coluna **"Tipo NF-e"** que exibe a categoria da nota que está sendo trabalhada. Tem-se as seguintes opções:

- NF-e Normal Compra;
- NF-e Complementar;
- NF-e Ajuste;
- Devolução de mercadoria.

**Nota:** quando se tratar de notas sem o devido lançamento/saída não será possível digitar mais de uma chave de devolução. Recomenda-se utilizar o Portal de Importação de XML para lançar as notas e processar as devoluções.

A coluna **"Tipo"** é apenas informativa e será alimentada com as opções **"NF-e"** ou **"CT-e"**.

Com o parâmetro **"Considerar CNPJ/CPF e IE na importação do XML? - CONCNPJIEIMPXML"** ligado, ao realizar a importação do XML, o sistema irá considerar o CPF/CNPJ e Inscrição Estadual do destinatário do XML para localizar a Empresa. Caso o XML não possua a informação pertinente à Inscrição Estadual, será considerado apenas o CNPJ/CPF para identificação da Empresa e será exibida a seguinte mensagem:

**"Não encontramos empresas com CNPJ e IE iguais ao do XML, no entanto, foram encontradas múltiplas empresas com o mesmo CNPJ. Na importação, será considerada a empresa com o menor código de cadastro"**.

Ao tentar processar, o sistema faz novamente a validação do parâmetro CONCNPJIEIMPXML e exibe a seguinte mensagem ao usuário:

**"Não foi encontrado empresas com dados de destinatário CPF e IE ou emitente CPF e IE"**.

Se o parâmetro estiver desligado, o sistema considera apenas o CPF/CNPJ na validação da importação do XML. Isso significa que uma nota será importada para a empresa com o menor número de cadastro, mesmo que a Inscrição Estadual não corresponda ao XML, pois, com o parâmetro desativado, a Inscrição Estadual não é validada.

É importante destacar que, com o parâmetro CONCNPJIEIMPXML ativado, o sistema compara a Inscrição Estadual (IE) registrada no [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas) com a tag **<IE>** do grupo **<Dest>** no XML da NFe. Caso a tag contenha zeros à esquerda, esses serão desconsiderados, permitindo a importação do XML mesmo que haja diferença na formatação da IE.

Por outro lado, se o parâmetro estiver desativado, o sistema seguirá o comportamento padrão, validando apenas o CNPJ/CPF e desconsiderando a IE. Nesse caso, a NFe será importada para o cadastro que apresentar o menor número associado ao mesmo CNPJ/CPF do XML.

O comportamento do parâmetro CONCNPJIEIMPXML ocorre apenas na rotina do Portal de Importação de XML.

**Observação:** será possível fazer a importação de arquivos de CT-e de Anulação com a tag **<tpCTe>2</tpCTe>**, alimentando o lançamento na Central.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Processamento dos arquivos

Para processar um arquivo, iniciando a importação, basta selecioná-lo na grade e clicar no botão ![Imagem 10: Para processar um arquivo, iniciando a importação, basta selecioná-lo na grade e clicar no botão "Processar Arquivo(s)"…](https://ajuda.sankhya.com.br/hc/article_attachments/27082685089687) **"Processar Arquivo(s)"**, na parte superior da tela. Para processar vários arquivos, segure a tecla **"Ctrl"** e clique nos arquivos desejados, depois repita o processo.

Se houver divergências durante a importação, o sistema exibirá mensagens indicando os problemas. Ao processar múltiplos arquivos, as divergências de cada um serão tratadas individualmente.

Mesmo com divergências, o sistema gerará uma nota de compra no [Portal de Compras,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) caso o sistema consiga identificar as informações básicas do cabeçalho da nota. As informações da nota podem ser visualizadas na grade do Portal de Importação de XML.

Quando as divergências forem solucionadas, as informações serão adicionadas na nota até que a importação seja feita por completo.

Após a importação da Nota de Compra, o sistema enviará um e-mail para o Parceiro da nota autorizando a entrega da mercadoria, desde que as configurações para envio de e-mail estejam corretamente realizadas.

Se o status do arquivo for diferente de **"Importado"** e a opção de remoção for selecionada, a nota correspondente no Portal de Compras também será excluída.

Além disso, para arquivos com status Importado, o botão Processar Arquivo(s) mudará para **"Liberar para reprocessamento"**. Ao ser acionado, o documento e o financeiro associados serão excluídos, o status do registro será alterado para **"Pendente"**, permitindo o reprocessamento.

**Observação:** o sistema não processa nota complementar de terceiros. Contudo, o processamento só é realizado quando a nota complementar for de emissão própria.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Cancelando o processamento

Quando um arquivo possui o status **"Pendente"** ou **"Com divergência"**, tem-se a opção de cancelar a importação, clicando no botão ![Imagem 11: Quando um arquivo possui o status "Pendente" ou "Com divergência" , tem-se a opção de cancelar a importação, clicando…](https://ajuda.sankhya.com.br/hc/article_attachments/27082786608151) **"Cancelar"** localizado na parte superior da tela. Assim, o status será alterado para **"Cancelado"**.

Se o cancelamento for feito por engano, exclua o arquivo no Portal de Importação de XML e importe-o novamente. Essa ação fará com que o arquivo seja importado com status diferente de Cancelado, sendo possível dar continuidade no processo habitual.

**Importante:** antes de proceder com a exclusão do lançamento, certifique que o arquivo XML esteja salvo em uma pasta local. O download pode ser realizado por meio do botão [MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354#botomd-e), opção **"Exportar Documentos Fiscais"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Aba Financeiro

Nesta aba, visualize e configure o financeiro de acordo com o XML importado ou o **"Tipo de Negociação"** definido para o respectivo documento. 

![Imagem 12: Nesta aba, visualize e configure o financeiro de acordo com o XML importado ou o "Tipo de Negociação" definido para o…](https://ajuda.sankhya.com.br/hc/article_attachments/25480844506007)

O campo Tipo de Negociação é preenchido de acordo com a configuração do campo de mesmo nome encontrado em cada opção dentro do botão **"Outras Opções"** desta tela.

No entanto, caso selecione um Tipo de Negociação diferente ao configurado anteriormente, será possível visualizar a simulação através do botão ![Imagem 13: No entanto, caso selecione um Tipo de Negociação diferente ao configurado anteriormente, será possível visualizar a…](https://ajuda.sankhya.com.br/hc/article_attachments/25480824210071) **"Simular"**, sendo possível saber como seria o Financeiro escolhido. Entretanto, ao concluir e processar, o documento será gerado com o financeiro configurado no botão Outras Opções. 

O campo **"Usar financeiro"** determina qual financeiro será gerado ao processar o documento, sendo possível escolher entre as seguintes opções:

- Usar Financeiro do Sistema;
- Usar Financeiro do Arquivo.

Quando este campo estiver como **"Não informado"** significa que existem inconsistências entre o financeiro do sistema e o financeiro do arquivo, não sendo possível prosseguir, já que para processar um XML é necessário informar qual financeiro deseja usar, do Sistema ou do Arquivo.

**Observação:** ao realizar a conferência, os valores dos impostos da nota serão recalculados conforme as configurações do [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) para Explosão de Lote, independentemente da forma de importação, o que pode resultar em alteração no valor financeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Tratando divergências

Durante o processamento podem ocorrer divergências entre o conteúdo do XML e o do sistema. Para essas divergências, decida qual será a informação correta, se a do sistema ou a informação do XML. Após o processamento do(s) arquivo(s), caso algum possua divergência de importação, o sistema exibirá a seguinte mensagem:

**"Divergências na importação. Arquivo: X - XML de Compra.xml"**

Para solucionar a divergência, selecione o registro na grade e clique duas vezes na linha para abrir a seção de tratamento de divergências. Nessa seção, visualize as divergências nas abas **"Cabeçalho"**, **"Produtos por parceiro"**, **"Pedidos"**, **"Impostos"** e **"Financeiro"**.

![Imagem 14: Para solucionar a divergência, selecione o registro na grade e clique duas vezes na linha para abrir a seção de…](https://ajuda.sankhya.com.br/hc/article_attachments/27546843926167)

**Importante:** tratando-se de arquivos com o status Importado, o botão **"Validar importação"** passará a se chamar **"Liberar para reprocessamento"** e, ao ser acionado, realizará a exclusão do documento e financeiro associados ao arquivo selecionado. Deste modo, o status do registro passará para Pendente e o mesmo poderá ser processado novamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Divergências

| [Divergências de Parceiro/Empresa/Transportadora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciadeparceiroempresaetransportadora) | [Divergências de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciasdeprodutos) |
| --- | --- |
| [Divergências de Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciasdepedidos) | [Divergências de financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_94b53eaa-3fbe-4543-be6c-2cc10c93298e) |
| [Divergências de Data do Vencimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_926d8ff8-21ac-458f-a75f-d8672f5dd086) | [Divergências de impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#h_5cbef30c-c40c-45b9-86cc-bce908be438c) |

### Divergências de Parceiro, Empresa e Transportadora

Na aba **"Cabeçalho"** visualize informações sobre o registro do Parceiro, Empresa, Transportadora e Chave Referenciada encontrados no sistema e no XML. Essas informações são apenas para identificar a existência de alguma diferença entre estes cadastros e não podem ser editadas.

O **"Parceiro"** da nota de compra é localizado no sistema pelo **"CPF/CNPJ"**; caso o sistema não encontre nenhum parceiro com o CNPJ, será registrada uma divergência na importação; se encontrado mais de um parceiro com o mesmo CNPJ, também será registrada uma divergência. A mesma validação é feita para **"Empresa"** e **"Transportadora"**.

A aba “Chave Referenciada” ajuda você a visualizar e tratar as chaves encontradas no XML, mas que **não foram vinculadas automaticamente** durante a importação, ao contrário das abas de Impostos ou Financeiro que mostram dados processados.

A aba é dividida em dois quadrantes, "Sistema" e "Arquivo", que possuem totalizadores e grades de visualização:

##### Visão Geral dos Quadrantes

- No quadrante **Arquivo**, o campo **"Total Chaves do Arquivo"** representa o total de chaves referenciadas existentes no arquivo XML.
- No quadrante **Sistema**, o campo **"Total Chaves Vinculadas"** apresenta as chaves referenciadas que foram devidamente vinculadas ao documento no sistema.
- Observação: Esses campos de totalização não podem ser preenchidos manualmente.

##### Visualização Detalhada (Grades)

- **Grade Arquivo:** **Sempre lista todas as chaves referenciadas** que estão presentes no arquivo XML. O papel dela é mostrar o que o arquivo contém.
- **Grade Sistema:** **Só lista as chaves** que estão no XML (Grade Arquivo) **e que NÃO foram referenciadas na importação**. Se a importação não conseguir vincular alguma chave, ela aparecerá nesta grade.

##### Como Integrar os Dados (SPED Fiscal)

Quando há chaves listadas na grade "Sistema" (chaves não referenciadas), o usuário tem a opção de usar o botão **"Integrar Dados"**.

- **Ação e Resultado:** Ao clicar, o sistema junta as informações dessa chave não referenciada (número, data do documento fiscal e tipo de operação) e grava no campo **CHVNFEINEREF** (Chave NFe Referenciada Inexistente) do cabeçalho da nota.
- **Finalidade Fiscal:** Essa informação gravada é essencial e será consumida (usada) pelo **registro C113 do SPED Fiscal**.

Os campos **"Tipo de operação"** e **"Data do Documento Fiscal"** apresentados no quadrante Sistema deverão ser preenchidos com base na chave vinculada. 

**Observação:** quando o **"Cód. Parceiro"** não estiver preenchido corretamente mesmo que este já esteja cadastrado, realize a importação do XML novamente. Esse campo só poderá ficar em branco caso a importação não tenha sido concluída.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

### Divergências de produtos

A aba **"Produtos por Parceiro"** apresenta os itens da nota do XML importado com suas respectivas ligações com os produtos no sistema; caso existam divergências para produtos, informe a qual produto do sistema aquele item é equivalente. Para editar, clique duas vezes na linha correspondente às colunas Produto, Unidade e Controle. Caso o produto informado tenha controle adicional, a coluna terá sua descrição alterada automaticamente para o nome definido como título na configuração do controle adicional de cada produto.

![Imagem 15: A aba "Produtos por Parceiro" apresenta os itens da nota do XML importado com suas respectivas ligações com os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/27546911404567)

Esse registro é a base para a validação dos Pedidos, Financeiro e Impostos. Após vincular todos os produtos, clique no botão **"Validar importação"** para que o sistema refaça a análise com base nos produtos informados. As regras para seleção do produto são:

**(1)** **Sem divergência:** produto localizado pelo código prod. equivalente e unidade (aba [Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaprodutosequivalentes) no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos)).

**(1)** **Com divergência:**

- Produto localizado apenas pelo código prod. equivalente (aba Produtos Equivalentes no Cadastro de Produtos);
- Produto localizado apenas pela referência (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral));
- Produto localizado apenas pela referência do fornecedor (aba Geral);
- Produto localizado apenas pela descrição do produto (aba Produtos Equivalentes);
- Produto não localizado.

No segundo caso, onde o produto é localizado, uma divergência é lançada para que seja confirmada a relação dos produtos.

Após a importação com sucesso, caso o produto localizado esteja sinalizado com divergência, será incluído um item na aba Produtos Equivalentes do Cadastro de Produtos registrando a ligação.

Ao realizar a importação de um XML por meio das funcionalidades desta tela ou por meio da Central de Compras, fará com que o sistema permita que sejam realizados registros considerando produtos que não estejam previamente cadastrados no sistema. Diante disso, serão validados os lançamentos e, em sequência, será apresentada na coluna **"Divergência"** a mensagem: **"Produto não localizado"**.

Assim, quando o sistema não localiza os mesmos produtos contidos no arquivo XML, será disponibilizado um pop-up denominado **"Cadastre os produtos equivalentes"** para que sejam inseridos neste, o produto e a unidade correspondentes aos dados do arquivo.

Para proceder com a equivalência dos produtos mencionados anteriormente, é necessário acessar a tela Cadastro de Produtos, aba Produtos Equivalentes, para que assim, o processo de importação de XML ocorra tanto na Central de Compras quanto no Portal de importação de XML.

---

![Imagem 16: Informações adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/25753358813463) **Informações adicionais**

- Caso o parâmetro **"Ligar pedidos considerando lote na importação/XML? - PEDLIGAPORLOTE"** esteja ativado, será feita a busca no sistema por pedidos ligados tomando-se por base o lote do produto informado nessa aba (Produtos por Parceiro).
- Se o parâmetro **"Recalcular custos na importação do CT-e? - CALCCUSIMPCTE"** estiver ativado, ao concretizar a importação do XML, os custos pertinentes aos itens da nota serão automaticamente recalculados. Caso o parâmetro esteja desativado e seja necessário recalcular os custos dos produtos, localize as notas no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), efetuar sua abertura e, na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), proceder com o recálculo de forma manual (botão Recalcular Custos).
- Ao realizar a marcação da opção **"Priorizar descrição para vinculação de produtos"** (**"Botão Outras Opções"**, [Preferências para Importação de NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimporta%C3%A7%C3%A3odenf-e)), quando o processamento de arquivos for realizado, uma das linhas do produto conterá o valor da tag <**cProd**> e a outra a descrição e o valor da tag <**xProd**>. Sendo assim, se houverem produtos com o mesmo Código, NCM e EAN, a descrição do produto será o critério que irá diferenciá-los. Se esta opção estiver desmarcada, o sistema não fará a divergência das informações referente às tags, e incluirá uma nova linha.
- Utilize o botão  ![clip9401](https://ajuda.sankhya.com.br/hc/article_attachments/360061908933) **"Impressão do Grid"** localizado no canto superior esquerdo da aba Produtos por Parceiro, para imprimir a lista que consta os produtos sem equivalência, para que assim, seja otimizado o processo. Esse procedimento de impressão poderá ser realizado também na Central de Compras.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

### Divergências de Pedidos

Quando um [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) de Nota de Compra estiver com o campo **"Exigir Pedido"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) estiver configurado com a opção **"Não exigir"**, não será feita a validação de Pedido de Compra ao importar o arquivo. Se estiver diferente de Não exigir, o sistema irá analisar para cada item da nota, se existe algum Pedido de Compra no sistema com o mesmo **"Número da Nota"**, que pode ou não ter sido informado no arquivo XML. Serão considerados somente os Pedidos de Compra que estiverem confirmados.

Para que isso ocorra nos Pedidos de Vendas, o pedido deve atender a alguns requisitos específicos: 

![Imagem 18: O pedido deve ser lançado para o mesmo Parceiro e Empresa da importação;](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) O pedido deve ser lançado para o mesmo Parceiro e Empresa da importação;

![Imagem 19: O item do pedido deve ser o mesmo item vinculado na aba Produtos por Parceiro ;](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) O item do pedido deve ser o mesmo item vinculado na aba [Produtos por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciasdeprodutos);

![Imagem 20: O campo Exigir Pedido na TOP da importação deve estar diferente de Não Exigir , podendo ser:](https://ajuda.sankhya.com.br/hc/article_attachments/27539664299159) O campo Exigir Pedido na TOP da importação deve estar diferente de Não Exigir, podendo ser:

- **Exigir Completo:** todos os itens da nota devem ser compatíveis com os itens do pedido;
- **Exigir algum item:** ao menos um item da nota deve ser compatível com o pedido.

**Observação:** o pedido deve ser lançado, confirmado e com o status **"Pendente"**.

Com esses requisitos atendidos, será possível vincular o pedido à nota e gerar o registro correspondente na tabela específica por meio do botão ![Imagem 21: Com esses requisitos atendidos, será possível vincular o pedido à nota e gerar o registro correspondente na tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/27539664302615) **"Ligar pedidos mais antigos"**.

O sistema fará a ligação automática do número do Pedido Compra com o XML da nota importada, quando no XML da Nota de compra a tag **<xPed>** estiver preenchida com o Nro. Nota (NUMNOTA) dos pedidos de compra e o pedido com essa numeração existir no sistema. Caso essa informação não venha preenchida no arquivo, ou o pedido não exista no sistema, serão apresentados na aba **"Pedidos"** todos os Pedidos de Compra que contenham o produto selecionado na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603174-Portal-de-Compras-Atributos-da-Tela#grade-itens).

![Imagem 22: O vínculo de pedidos ocorre somente para Pedidos de Compras .](https://ajuda.sankhya.com.br/hc/article_attachments/16364732359831) O vínculo de pedidos ocorre somente para Pedidos de Compras.

Se forem identificados os pedidos informados no XML, o sistema irá verificar os [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) dos pedidos. Se for encontrado apenas um tipo de negociação entre os pedidos, este será utilizado na validação do financeiro e na importação da nota, caso contrário será utilizado o tipo de negociação do modelo de notas e pedidos, do [Cadastro da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas).

**Observação:** o parâmetro **"Importa negociação divergente do xml da compra? - IMPNEGDIVXMLCMP"** por padrão é apresentado ativado; sendo mantido com esse status, será possível realizar a importação de notas de compra mesmo que o Tipo de Negociação do XML esteja divergente. Para que as importações com divergência no Tipo de Negociação não sejam permitidas, desative o referido parâmetro.

Quando o número do Pedido de Compra não tiver sido informado no XML da nota importada ou não existir no sistema, os produtos poderão ser ligados aos pedidos de duas formas: **"Manual"** (um a um), ou pelo botão Ligar pedidos mais antigos.

#### Manual:

Na grade superior são apresentados os produtos importados, e na grade inferior os pedidos que contêm os produtos apresentados da grade superior. A coluna **"Vinculado"** na grade **"Pedidos disponíveis"** é editável e sua modificação está relacionada à informação apresentada na coluna **"Vinculado"** da grade **"Itens importados"**, ou seja, a soma total da coluna Vinculado da grade inferior é o valor apresentado na coluna Vinculado da grade superior.

![Imagem 23: Na grade superior são apresentados os produtos importados, e na grade inferior os pedidos que contêm os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/27548564009111)

**Importante:** a ordenação da grade Pedidos disponíveis seguirá a configuração realizada no campo **"Opção para Data de Previsão de Entrega"** localizado no botão **"Outras opções"**, opção **"Preferências para importação de NF-e"**.

#### Botão Ligar pedidos mais antigos:

O sistema fica responsável por selecionar quais pedidos serão ligados, e exibe as ligações feitas utilizando este critério (data de entrega mais antiga); antes de executar este procedimento, é apresentado na tela um questionamento para confirmação da operação.

Na seleção, se o sistema identificar mais de um pedido para o produto, será verificado qual pedido tem a data de entrega mais antiga para ligá-lo ao produto. Caso a quantidade não seja suficiente, os pedidos mais recentes serão associados, respeitando sempre a ordem da grade.

Se, no Pedido de Venda, a quantidade atendida for igual a quantidade disponível, o pedido deixa de estar pendente e não será vinculado novamente a outra nota no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), e indicada na informação da nota no pop-up **"Documentos relacionados à Nota"** pela opção [Documentos relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014-Portal-de-Vendas-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#documentosrelacionados), no botão ![Imagem 24: Se, no Pedido de Venda , a quantidade atendida for igual a quantidade disponível, o pedido deixa de estar pendente e…](https://ajuda.sankhya.com.br/hc/article_attachments/24344649125911) **"Outras Opções"**. 

No entanto, caso a quantidade atendida seja menor ou parcialmente igual a quantidade disponível, o pedido continuará pendente e poderá ser vinculado em outra nota.

Caso exista alguma divergência entre os campos **"Valor Unitário"** das grades inferior e superior, o sistema irá analisar as configurações realizadas no cadastro de Tipos de Operação - TOP, aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes), seção **"Conf. Evento de Liberação 68"** e, a partir disso, se for o caso, aciona-se o botão **"Liberações"** para que seja escolhido o usuário liberador, ou seja, aquele que possui o evento **"68 - Variação do vlr. unit. orig./dest."** para ele configurado.

Se a grade inferior não apresentar nenhum registro ao selecionar um item na grade superior, será porque o sistema não encontrou nenhum pedido que possa ser ligado, deve-se então fazer o lançamento do(s) pedido(s) e utilizar o botão **"Buscar novos pedidos"**. Importate destacar que este botão refaz a busca de pedidos e descarta a distribuição já feita dos itens.

**Importante:** quando houverem pedidos de compras com unidades alternativas de medidas diferentes daquelas que constam no XML, é necessário alterar a quantidade no campo **"Quantidade"** da grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) do pedido de compra na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras). Após isso, deve-se retornar ao arquivo importado no Portal de Importação de XML e acionar o botão Buscar novos pedidos, para que o sistema informe o valor correto do pedido de compra, pois não é possível atribuir um valor de produtos vinculados maior que a quantidade solicitada no pedido de compra. 

**Observação:** quando utilizada a rotina de importação de notas para uma empresa filial vinculando um pedido de compra do parceiro Matriz com a nota de compra do parceiro filial, para aparecer os pedidos da empresa Matriz é necessário clicar no botão Buscar novos pedidos onde será aberto um pop-up para informar **"Qual parceiro será utilizado para ligar a nota ao pedido?"**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

### Divergências de impostos

Nessa aba serão exibidos apenas os produtos na qual o imposto do XML estiver divergente dos impostos do sistema. Deste modo, suas informações servirão somente para fins comparativos.

Os impostos da nota serão considerados de acordo com a opção do campo **"Cálculo de ICMS, IPI e ISS"** da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) (TOP de Compra), conforme abaixo:

- **Calcula e digita:** o sistema irá calcular os impostos dos itens e comparar com os impostos vindos do XML, caso possua alguma divergência o sistema irá apresentá-lo na grade, e pode-se escolher entre utilizar os impostos do sistema ou os impostos do XML;
- **Não calcula e não digita:** os impostos não são considerados nem do sistema, nem do XML na nota; as informações ficam em branco;
- **Não calcula e digita:** são considerados os impostos vindos do XML;
- **Calcula e Não digita:** são considerados os impostos calculados pelo sistema.

Ao realizar a importação de um arquivo XML onde a TOP utilizada encontra-se com o campo acima mencionado configurado com uma das opções Calcula e Digita ou Calcula e Não Digita, fará com que o sistema verifique qual será a data de negociação da nota e buscar na tabela de preços o valor informado para o produto lançado nesta nota, se esta possui data igual ou anterior que esteja mais próxima à data de negociação.

Quando a opção Não calcula e digita estiver selecionada, os impostos provenientes do XML serão considerados. Para que a importação dos valores constantes no XML do IPI sejam realizadas, é necessário que os seguintes campos estejam marcados:

- Campo **"Tem IPI na compra"** na tela Cadastro de Produtos, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos);
- **"Tem IPI"** tela Cadastro de Parceiros, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal);
- e o campo **"Tem IPI"** na tela TOP, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos).

Ainda considerando a opção Não calcula e digita mencionado acima, para que no total do lançamento os valores do IPI e ICMS-ST sejam somados, é preciso que na TOP as opções **"Somar ST no total da nota"** e **"Somar IPI no Total da Nota"** estejam marcadas.

![Imagem 25: Ainda considerando a opção Não calcula e digita mencionado acima, para que no total do lançamento os valores do IPI e…](https://ajuda.sankhya.com.br/hc/article_attachments/27547334882583)

Existindo divergências de impostos, através do campo **"Usar impostos"** pode-se definir como o sistema deverá tratar essas inconsistências. Essa configuração ficará disponível sempre que a importação alertar sobre alguma diferença de impostos. Tem-se as seguintes opções:

- **Usar Impostos do Sistema:** os dados de tributação serão aqueles calculados pelo sistema. Quando você simula o cálculo de impostos, lembre-se: o sistema **não inclui as despesas extras** nessa conta. Ele calcula o imposto só com base nos valores principais.
- **Usar Impostos do Arquivo:** a busca das informações será diretamente do XML; posteriormente o sistema realiza algumas validações antes de definitivamente inseri-las na nota.
- **Não informado:** esta opção corresponde à não existência de divergências de impostos entre o sistema e o XML, ou ainda, a inexistência de impostos no documento.

Ao ativar o parâmetro **"Valida cálculo de impostos ao explodir lotes" (VALCALCIMPLOXML)"**, a validação dos impostos dos lotes segue o critério aplicado aos demais itens. Com essa alteração, se houver diferença nos valores, os impostos do item serão classificados como divergentes.

Caso esse parâmetro esteja desativado, durante a importação, alguns itens podem não aparecer na aba de impostos quando há divisão em múltiplos lotes. Com a ativação, o sistema passa a identificar e considerar corretamente essas divergências.

**Importante:** no Portal de importação de XML, quando a empresa for optante pelo Simples Nacional, ao inserir o item da nota na Central de Compras, o campo CST da importação será sempre preenchido com as informações correspondentes à CSOSN calculada pelo sistema. Esse comportamento leva em consideração apenas a empresa, portanto, independe do regime do fornecedor, ou se existem ou não divergências entre os impostos calculados pelo sistema e o XML importado.

**Observação:** caso a BC do ICMS tenha incidência de frete, o sistema irá indicar uma divergência de impostos, pois o valor da incidência do frete é considerado apenas após a validação da importação. Lembre-se ainda que, caso opte por utilizar o cálculo do sistema, a marcação **"ICMS proporcional para Frete"** da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias)) deve ser habilitada.

Na validação das divergências de impostos, o sistema possui uma tolerância de R$ 0,01 (um centavo) para o valor do imposto; ao realizar a importação do XML, se existirem discrepâncias nos valores dos impostos ICMS, IPI e ST de até R$0,01, não será exibida a mensagem de divergência de impostos. Esta tolerância é válida apenas para o valor do imposto; as respectivas bases e alíquotas não se encaixam nessa flexibilização.

**Nota:** ao realizar a importação de XML, o sistema está apto a importar o valor do imposto da nota de compra nos casos em que a empresa se enquadra no Regime Normal (Cadastro de Empresas, aba [Naturezas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas#abanaturezas), campo **"Cód. Regime Tribut."** definido como **"Regime Normal"**) e seu fornecedor emitente da nota é Optante pelo Simples Nacional (Cadastro de Parceiros, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal), marcação **"Optante pelo Simples Nacional"** realizada).

**Observação:** no processo de importação, além de importar o valor da substituição tributária do produto, o sistema irá considerar o valor da substituição tributária referente ao Fundo de Combate a Pobreza, ou seja, o valor da Subst. Tributária será a soma do **<vICMSST>** com o **<vFCPST>**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

### Divergências de financeiro

Se o sistema encontrar apenas um [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173) ao analisar os pedidos, ele será usado para validar o financeiro. Caso haja mais de um Tipo de Negociação nos pedidos relacionados à nota de compra, o sistema utilizará o Tipo de Negociação do modelo de nota.

O sistema verifica se há divergências nas parcelas do financeiro, como quantidade de parcelas, datas de vencimento e valores. Se alguma diferença for identificada, o sistema gerará uma divergência onde será possível escolher entre usar o financeiro calculado pelo sistema ou o financeiro do XML, além de selecionar outros tipos de negociação para simular o financeiro.

Ao configurar o campo **"Usar financeiro"** com a opção **"Usar financeiro do arquivo"**, o sistema aplicará o Tipo de Negociação do modelo de importação do XML.

A data do vencimento do sistema utiliza como base a data da negociação informada no XML.

![Imagem 26: A data do vencimento do sistema utiliza como base a data da negociação informada no XML.](https://ajuda.sankhya.com.br/hc/article_attachments/27547334887447)

Os parâmetros **"Data Base p/ Calculo do Vencimento no Faturamento - DTCALCVENC"** e **"Força Dt. Fat. c/ Base p/ Cálculo Venc. na compra? - FORCDTFATCOMPRA"** definem qual data será utilizada no cálculo da data de vencimento. As verificações são as seguintes:

1. Se o parâmetro DTCALCVENC estiver configurado com a opção **"Data de Saída"** e a data de entrada/saída existir, essa data será utilizada;
2. Caso o parâmetro FORCDTFATCOMPRA esteja ligado, e o tipo de movimento for Compra ou Pedido de Compra, a data de faturamento será aplicada;
3. Quando o parâmetro DTCALCVENC for diferente de **"Negociação"** e a data de faturamento estiver preenchida, essa data será usada;
4. Se as condições acima não forem atendidas, utiliza-se a data de negociação.

Após definir o financeiro a ser usado, clique em **"Validar importação"** novamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

### Divergências de Data do Vencimento

O sistema permite selecionar o tipo de data a ser usada na importação do CT-e, conforme as preferências para importação do CT-e no campo **"Usar Vencimento"**.

No caso de processamento de CT-e de Terceiros, se o campo Usar Vencimento estiver configurado com a opção **"Data de Vencimento"**, caso o XML não possua data de vencimento, será apresentada a seguinte divergência:

**"Preferências CT-e: Data de vencimento não informado"**

O sistema disponibiliza o preenchimento manual da referida data clicando no campo **"Dt. Vencimento"**.

Após informar a data de vencimento, clique em **"Validar importação"** para resolver a divergência.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Outras validações

### Modelo

Se não for encontrado nenhum **"Modelo de Importação de XML"** correspondente à Empresa e Natureza de operação ou o Modelo de Notas configurado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) não existir, o processamento será interrompido para ajuste. As mensagens exibidas serão:

**"Modelo padrão não encontrado no sistema"**

**"XML mal formado ou inválido!"**

Após corrigir todas as divergências, ao clicar em **"Validar importação"**, o processamento será concluído com sucesso.

### Configurações pra importação de NF-e de terceiros mista (Venda e Bonificação)

Com as devidas configurações para permitir o valor do financeiro menor que o total da nota, é necessário habilitar o parâmetro **"Hab. opç. que perm. fin. menor que o vlr. da nota - HABOPCFINMENNOT"** e acionar a marcação **"Permite financeiro menor que o valor total da nota"** localizada na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abafinanceiro) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114).

Deste modo, ao importar uma nota fiscal mista será possível a correta conversão do CFOP referente aos produtos bonificados constantes no XML, sendo 5910/6910 para 1910/2910 respectivamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Validação do valor unitário dos itens

Com as configurações abaixo, será possível validar o valor unitário dos itens entre o pedido de compra e o XML importado. A partir dessa validação, o usuário poderá decidir pela aceitação ou não do XML da nota de compra negociada.

No Portal de Importação de XML, o sistema irá realizar as seguintes validações:

- O evento [68 - Variação do vlr. unit. orig./dest.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#68-variaodovlr.unit.orig.dest.) deve estar configurado para um usuário liberador (tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para Liberação"**.
- O Tipo de Operação utilizado deve estar com o campo **"Exigir pedido"** diferente de **"Não exigir"**; (tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalida%C3%A7%C3%B5es)).
- As configurações do evento 68 devem estar corretamente configuradas na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), seção **"Conf. do evento 68 (Variação do valor unitário entre origem e destino)"**.
- O parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** deve estar ativado.

Se o XML importado tiver algum item com valor unitário diferente do valor unitário no pedido de compra vinculado à nota, será registrada uma divergência de importação, e a seguinte mensagem será exibida:

**"Aguardando liberação para variação do vlr.unitário acima do permitido. Divergência de valor unitário entre pedido e nota."**

A divergência será considerada apenas se a diferença entre os valores unitários do pedido e da nota for superior à tolerância configurada no Tipo de Operação - TOP. Caso contrário, não haverá a divergência.

### Resolução da Divergência

Para resolver a divergência, pode-se:

- Alterar o valor unitário do pedido de compra para que corresponda ao valor do XML.
- Solicitar a liberação de limites.

Ao optar por solicitar a liberação, no pop-up onde o usuário liberador é definido, os dados referentes ao pedido e à divergência serão exibidos no campo **"Observações"**, com a seguinte mensagem:

**"Houve divergência no valor unitário do produto: Ped. orig. XXX Prod. YYY - Descrição do Produto, Variação de R$ #,## (Nota: R$ #,## / Pedido: R$ #,##)"**

Onde:

- **XXX** = Pedido de Origem
- **YYY** = Produto que está apresentando a divergência
- **#,##** = Diferença entre o valor do pedido e o valor da nota (valor da nota / valor do pedido)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Validação do IPI no XML dos itens

![Imagem 27: Atenção Consultor Sankhya!](https://ajuda.sankhya.com.br/hc/article_attachments/16364732359831) **Atenção Consultor Sankhya!**

O cálculo do IPI foi ajustado para atender empresas que possuem particularidades no cálculo desse imposto, como produtos com mais de uma alíquota de IPI. Nesses casos, o sistema pode adaptar-se mediante a criação de uma função específica no banco de dados.

No momento em que o sistema realiza o cálculo do IPI em qualquer operação, ele atualmente verifica o produto da operação para identificar qual o código de alíquota de IPI do mesmo.

O sistema irá verificar se existe alguma função no banco de dados com o nome **"OBTEM\_ALIQ\_IPI"** e que retorne algum código de alíquota de IPI; se essa condição for satisfeita, será utilizado o código de alíquota de IPI obtido a partir da função em questão e utilizá-la no cálculo do imposto.

As informações que o sistema poderá utilizar para obter o código de alíquota de IPI serão as seguintes:

- **CODEMP:** Código da empresa da nota;
- **CODPARC:** Código do parceiro da nota;
- **CODPROD:** Código do produto da nota;
- **NUNOTA:** Número único da nota;
- **SEQUENCIA:** Sequência do produto na nota.

Abaixo está um exemplo da função mencionada:

```
CREATE OR REPLACE FUNCTION OBTEM_ALIQ_IPI (P_CODEMP IN NUMBER,
P_CODPARC IN NUMBER, P_CODPROD IN NUMBER, P_NUNOTA IN NUMBER,
P_SEQUENCIA IN NUMBER)

RETURN NUMBER IS CODALIQ NUMBER;

BEGIN

   SELECT CAB.AD_CODALIQ INTO CODALIQ

   FROM TGFCAB CAB

   WHERE CAB.CODEMP=P_CODEMP

   AND CAB.CODPARC=P_CODPARC

   AND CAB.NUNOTA=P_NUNOTA;

   RETURN (CODALIQ);

END;

/
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Regras de Negócio na Importação de XML

No processo de importação de XML, seja pelo Portal de importação de XML ou pela [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), as [Regras de Negócio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598014) configuradas na empresa podem ser aplicadas durante a inclusão ou alteração do cabeçalho e itens da nota de compra.

As regras de negócio vinculadas ao [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) utilizado na nota, serão acionadas. Caso seja determinado um usuário liberador para algum evento oriundo de uma regra de negócio, a solicitação de liberação será realizada normalmente, tanto na importação do arquivo XML da NF-e pela Central de Compras, quanto pelo Portal de importação de XML.

**Importação de XML de CT-e modelo 57 de terceiros**

Ao importar um **XML de CT-e modelo 57** de terceiros que contenha o grupo de tags **ICMS60**, o sistema identifica automaticamente as informações do ICMS retido por substituição tributária (ICMS-ST).

Se as tags **vBCSTRet** (Base de Cálculo do ICMS-ST Retido), **vICMSSTRet** (Valor do ICMS-ST Retido) e **pICMSTSTRet** (Alíquota do ICMS-ST Retido) estiverem presentes e possuírem valores iguais ou maiores que zero, o sistema realiza os seguintes registros:

[Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)

- O campo **“Base Substituição”** recebe o valor da tag **<vBCSTRet>**.
- O campo **“Vlr. Substituição”** recebe o valor da tag **<vICMSSTRet>**.

Aba de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abaimpostos) na [Grade de Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) da Central de Compras

O sistema cria automaticamente uma nova linha para o **ICMS-ST**, preenchendo os campos correspondentes com os valores extraídos do XML:

- **Base de Cálculo**: valor da tag **vBCSTRet**.
- **Alíquota do Imposto**: valor da tag **pICMSTSTRet**.
- **Valor do Imposto**: valor da tag **vICMSSTRet**.

Dessa forma, as informações do **ICMS-ST retido** são registradas corretamente no sistema a partir da importação do XML.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Exclusão de documentos importados

No processo de exclusão de documentos no Portal de Importação de XML ou em documentos associados a essa rotina, as seguintes regras são aplicadas:

- Ao excluir uma nota ou um título financeiro vinculado a um registro do Portal de Importação de XML, o registro correspondente também será excluído, independentemente de seu status.

**Observação:** a partir da versão **4.20** do sistema, a exclusão das notas de importação do XML poderá ser realizada apenas se esta não for confirmada.

- No Portal de importação de XML, ao tentar excluir um registro que tenha preenchido o Nro. Único da Nota (NF-e) ou Nro. Financeiro (CT-e), a seguinte mensagem será exibida:

**"Existe documento vinculado ao XML selecionado que também será excluído. Deseja continuar?"**

- Ao proceder com a exclusão de um registro no Portal de importação de XML, se este registro possuir o Nro. Único da Nota informado, será apresentado o questionamento se deseja-se excluir a nota vinculada; optando-se por continuar e a nota não estiver confirmada, a mesma será excluída, caso contrário a seguinte mensagem será exibida:

**"A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML."**

- Na exclusão de um registro no Portal de importação de XML, se este possuir Nro. Financeiro informado, ou seja, for um CT-e, será apresentado o questionamento se deseja-se excluir o financeiro vinculado; continuando com a exclusão, caso o financeiro não esteja baixado o mesmo será excluído, caso contrário, será exibida a seguinte mensagem:

**"O financeiro de Nro. Único XXX já foi baixado e não pode ser excluído pelo Portal de importação de XML."**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Abrir Documento

O botão ![Imagem 28: O botão "Abrir Documento" , localizado na parte superior da tela, será habilitado apenas nas seguintes condições:](https://ajuda.sankhya.com.br/hc/article_attachments/27547273821335) **"Abrir Documento"**, localizado na parte superior da tela, será habilitado apenas nas seguintes condições:

- Quando o documento selecionado for uma NF-e e o campo **"Nro. Único da Nota"** estiver preenchido.
- Quando o registro for um CT-e e o campo **"Nro. Financeiro"** estiver preenchido.

Ao clicar no botão se estiver posicionado em uma linha de NF-e, a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) será aberta exibindo a nota correspondente. Se o registro for um CT-e, a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) será aberta, com o título financeiro já selecionado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Local para inserção das notas via importação do XML

No momento da inserção da nota fiscal de compra através do Portal de importação de XML, caso o produto utilize local, é preciso inserir o local adequado na nota. Para isso, no momento da inserção dos itens, serão analisadas as seguintes prioridades:

![Imagem 29: O sistema irá verificar se o parâmetro "Usa local Ped. compra c/menor Dt na importação XML-USALOCALPEDIMP" está ligado;…](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) O sistema irá verificar se o parâmetro **"Usa local Ped. compra c/menor Dt na importação XML-USALOCALPEDIMP"** está ligado; se estiver, será feita a busca do local referente ao pedido de origem mais antigo;

![Imagem 30: Se mesmo assim não for encontrado um local, o sistema utilizará a regra padrão para localização do local padrão, que…](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) Se mesmo assim não for encontrado um local, o sistema utilizará a regra padrão para localização do local padrão, que consiste em se basear no parâmetro global, empresa, usuário e produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Botão MD-e

![Imagem 31: Informações mais detalhadas sobre MD-e podem ser acessadas por meio do link MD-e - Manifestação do Destinatário .](https://ajuda.sankhya.com.br/hc/article_attachments/26330615640471) Informações mais detalhadas sobre MD-e podem ser acessadas por meio do link [MD-e - Manifestação do Destinatário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112353-MD-e-Manifesta%C3%A7%C3%A3o-do-Destinat%C3%A1rio).

O botão ![Imagem 32: O botão "MD-e" , localizado no canto superior direito da tela, oferece as seguintes opções de uso:](https://ajuda.sankhya.com.br/hc/article_attachments/27547273826327) **"MD-e"**, localizado no canto superior direito da tela, oferece as seguintes opções de uso:

- Ciência da operação;
- Confirmo a operação;
- Desconheço a operação;
- Operação não realizada;
- Prestação Serviço Desacordo;
- Cancelar Prestação Serviço Desacordo;
- Manifestar Docs. selecionados;
- Visualizar manifestos;
- Visualizar eventos DF-e;
- Documentos Referenciados;
- Visualizar NF-e/CT-e;
- Download NF-e;
- Exportar Documentos Fiscais;
- Preferências DF-e.

Essas opções estão vinculadas a permissões configuradas na tela de [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos), com acessos especiais dedicados a essa rotina. O funcionamento dessas opções no Portal de Importação de XML depende do parâmetro **"Controla acessos dos eventos do MD-e? - ACESSOEVENTOMDE"**, que deve estar ativado para que as opções relacionadas sejam exibidas no menu do botão MD-e.

Em relação à rotina de Compras, quando uma Nota de Compra estiver confirmada e a opção selecionada neste botão for **"Ciência da operação"**, **"Confirmo a operação"**, **"Desconheço a operação"**, **"Operação não realizada"** ou **"Prestação Serviço Desacordo"**, o sistema emitirá a mensagem:

**"Esta operação de manifesto não pode ser realizada em uma nota confirmada"**.

Dessa forma, o sistema impedirá a manifestação destes eventos. Por outro lado, se a nota não estiver confirmada, o comportamento do sistema seguirá conforme descrito na Central de Compras, botão MD-e.

No caso de manifestação do evento Prestação de Serviço Desacordo para um tomador de serviço Pessoa Física, o sistema exibirá a mensagem:

**"Evento Manifestação Serviço Desacordo para CT-e não é previsto para Tomador do Serviço Pessoa Física (CPF)."**

A opção Cancelar Prestação de Serviço em Desacordo permite que você, como tomador do serviço, desfaça uma manifestação de desacordo registrada indevidamente ou cuja divergência já foi solucionada. Ao acioná-la, o sistema gera e transmite o XML do evento de cancelamento para autorização da SEFAZ.

Para realizar o cancelamento, selecione o CT-e na grade, clique no botão **MD-e** e selecione **Cancelar Prestação de Serviço em Desacordo**. Confirme a operação quando o sistema solicitar.

> ⚠️ **Atenção**
>
> O cancelamento só é permitido se o CT-e possuir um Evento de Prestação de Serviço em Desacordo previamente autorizado pela SEFAZ. Caso contrário, o sistema exibe a mensagem "Não é possível realizar o cancelamento. O CT-e selecionado não possui Evento de Prestação de Serviço em Desacordo autorizado." Além disso, não é possível cancelar uma manifestação que já foi cancelada anteriormente.

Após a autorização do cancelamento pela SEFAZ, o evento é registrado no histórico do CT-e. Para consultar e garantir a rastreabilidade, selecione o CT-e, clique em **MD-e** e acesse **Visualizar eventos DF-e**. O sistema manterá o evento original e exibirá a nova linha de cancelamento.

Neste caso, a manifestação não será concluída.

Para a recusa de notas, é possível utilizar relatórios formatados para inserir e imprimir justificativas. As seguintes etapas devem ser seguidas:

1. Selecione a nota com operação recusada no Portal de Importação de XML;
2. Acione o botão MD-e, e selecione a opção **"Operação não realizada"**;
3. Em seguida, será aberto o pop-up **"Motivo operação não realizada"** para que sejam inseridas as informações de recusa;
4. Feito isso, selecione a opção **"Visualizar eventos DF-e"** localizada ainda no botão MD-e;
5. No pop-up **"Eventos DF-e"**, insira no campo **"Justificativa da manifestação"** o motivo da recusa.

Após a configuração, é possível exportar os registros com informações como número de protocolo, data, hora e justificativa da manifestação, utilizando a opção **"Exportar Registros"** no botão  ![clip9878](https://ajuda.sankhya.com.br/hc/article_attachments/360060978454) **"Impressão do Grid"** .

A justificativa será exibida na tag **<justificativamanifestacao>**do arquivo XML.

Para utilizar a funcionalidade de **Download de NF-e**, é necessário seguir os passos abaixo:

1. **Desmarcar a opção** “Baixar o XML ao dar a ciência da operação” na tela [Configuração MD-e/DF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234-Configura%C3%A7%C3%A3o-MD-e-DF-e). Isso garante que o XML não seja baixado automaticamente no momento da ciência, permitindo o uso do processo manual de download.
2. **Realizar a ciência da operação ou confirmação do destinatário** para os documentos desejados. Essa etapa é obrigatória para habilitar o download do XML junto à SEFAZ.
3. **Executar o download da NF-e** utilizando a funcionalidade específica no módulo **MD-e**.

**Importante**: o download só será possível após a ciência ou confirmação, e desde que o XML não tenha sido baixado anteriormente por outro processo automatizado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Referenciamento de item de outro Documento Fiscal Eletrônico (DFeReferenciado) em notas de devolução

| **Versão** | **Release** |
| --- | --- |
| 4.35 | Sankhya Om 4.35b826 |
| 4.36 | ERP Core 5.14.0 |

Documentos de devolução emitidos no novo layout da Reforma Tributária utilizam o grupo **DFe Referenciada** para identificar a nota fiscal de origem, em substituição ao grupo anteriormente utilizado. O portal reconhece esse grupo e grava a chave da nota referenciada em todos os controles internos do processo de importação, garantindo rastreabilidade completa da nota de origem.

O sistema processa XMLs em quatro cenários:

- **Apenas grupo antigo de referência de NF-e** — comportamento preservado sem alteração.
- **Apenas grupo DFe Referenciada** — chave gravada automaticamente nos controles internos.
- **Ambos os grupos simultaneamente** — o portal aplica regra de decduplicação para evitar duplicidade de referência.
- **Múltiplas referências em um único documento de devolução** — todas as referências são processadas e gravadas.

> **Nota:** o reconhecimento do grupo DFe Referenciada é automático após a atualização. Nenhuma ação adicional é necessária para ativar esse comportamento — basta importar o XML normalmente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Validação de IBS e CBS durante a transição

| **Versão** | **Release** |
| --- | --- |
| 4.36 | ERP Core 5.14.0 |

Durante o período de transição da Reforma Tributária 2026, o portal assume os valores de IBS e CBS destacados no XML pelo fornecedor como referência oficial para o processamento do documento. O sistema não realiza recálculo tributário interno para esses tributos na etapa de importação.

Esse comportamento implica que:

- Diferenças entre o cálculo interno do Sankhya Om e os valores de IBS/CBS do XML não geram bloqueio na importação.
- Os valores recebidos são armazenados integralmente e ficam disponíveis para apuração, consultas e obrigações acessórias da Reforma Tributária.
- As validações tributárias para tributos fora do contexto da Reforma — ICMS, IPI, PIS e COFINS — permanecem inalteradas.

#### Ativação do comportamento transitório

O comportamento é controlado por uma marcação nas Preferências do portal:

1. No **Portal de Importação de XML**, abra as **Preferências**.
2. Localize a seção **Configurações para Liberação Divergências**.
3. Marque **Ignorar validações de IBS/CBS (transição)** para ativar o comportamento transitório.
4. Salve a configuração.

> **Aviso:** quando a marcação **Ignorar validações de IBS/CBS (transição)** não estiver ativa, o portal pode gerar bloqueios por divergência de cálculo em documentos com esses tributos. Valide com a equipe fiscal antes de ativar ou desativar essa configuração em produção.

## Notas de Débito e Crédito (Reforma Tributária)

| **Versão** | **Release** |
| --- | --- |
| 4.35 | Sankhya Om 4.35b804 |
| 4.36 | ERP Core 5.12.0 |

> **Atenção:** esta configuração se aplica exclusivamente a NF-e de Débito (`finNFe=6`) e Crédito (`finNFe=5`) de **emissão própria** — documentos emitidos pelo próprio parceiro fora do Sankhya Om, como em marketplace ou solução fiscal operada em nome do parceiro. NF-e de Débito e Crédito recebidas de fornecedores ou clientes na relação comercial padrão continuam sendo tratadas como emissão de terceiros: não há distinção de subtipo e nenhuma configuração adicional é necessária nesta seção.

A Reforma Tributária (LC 214/2025) introduziu dois novos tipos de finalidade no layout NF-e:

- **Nota de Crédito** (`finNFe=5`) — 6 subtipos identificados pela tag `tpNFCredito`.
- **Nota de Débito** (`finNFe=6`) — 8 subtipos identificados pela tag `tpNFDebito`.

Para importar XMLs com essas finalidades, crie Tipos de Operação específicos e configure os vínculos nas Preferências desta tela. A sequência obrigatória é: primeiro cadastre as TOPs, depois configure as Preferências.

#### Cadastro de [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

Crie uma TOP para cada subtipo utilizado na operação:

1. Acesse o cadastro de **Tipo de Operação**.
2. No campo de finalidade, selecione **Import. Doc. Crédito (Emissão Própria)** ou **Import. Doc. Débito (Emissão Própria)**.
3. Preencha o campo condicional exibido:

   - Para crédito: **Tipo de Nota Fiscal de Crédito** — selecione o subtipo correspondente entre os 6 disponíveis de `tpNFCredito`.
   - Para débito: **Tipo de Nota Fiscal de Débito** — selecione o subtipo correspondente entre os 8 disponíveis de `tpNFDebito`.
4. Conclua o cadastro normalmente.

> **Nota:** os campos **Tipo de Nota Fiscal de Crédito** e **Tipo de Nota Fiscal de Débito** são condicionais: aparecem apenas quando a finalidade correspondente é selecionada. Para qualquer outra finalidade, esses campos não são exibidos.

#### Preferências de importação

Após cadastrar as TOPs, vincule cada subtipo à sua TOP nas Preferências do portal:

1. No **Portal de Importação de XML**, abra as **Preferências** para importação de NF-e de emissão própria.
2. Localize a seção **Notas de Débito e Crédito (Reforma Tributária)**.
3. Na grade exibida, vincule cada linha ao Tipo de Operação correspondente. A grade possui três colunas: **Finalidade**, **Tipo de Nota** e **Tipo de Operação**.
4. Salve a configuração.

> **Dica:** a grade carrega automaticamente os subtipos das TOPs já cadastradas com as novas finalidades. Se um subtipo não aparece, cadastre a TOP correspondente no cadastro de Tipo de Operação e volte para configurar as Preferências.

Após salvar, o comportamento na importação é:

- XML com `finNFe=5` ou `finNFe=6` e subtipo parametrizado na grade — importação concluída normalmente com a TOP configurada.
- XML com `finNFe=5` ou `finNFe=6` e subtipo não parametrizado — importação bloqueada com mensagem indicando o subtipo e o caminho de configuração nas Preferências.

## Particularidades do CT-e

![Imagem 34: O sistema está preparado para realizar a importação de CT-e nos layouts 2.00 e 3.00.](https://ajuda.sankhya.com.br/hc/article_attachments/16364732359831) O sistema está preparado para realizar a importação de CT-e nos layouts 2.00 e 3.00.

Para esse processo, é necessário preencher o pop-up [Preferências para importação do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e) (do botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)), onde também se define o vínculo do CT-e com as notas.

O sistema realiza algumas validações para vincular corretamente as notas. Caso ocorram divergências, o processo não será finalizado e as respectivas mensagens serão apresentadas. As principais divergências que podem surgir são:

- **Notas não encontradas:** ocorre quando nenhuma chave NF-e do arquivo XML do CT-e é encontrado no sistema. Para resolver este caso, é preciso verificar se todas as notas foram devidamente lançadas;
- **Nota(s) faltante(s):** quando pelo menos uma chave NF-e foi encontrada, mas outras não. Para solucionar, é preciso verificar se todas as notas foram devidamente lançadas;
- **Nota(s) de venda com modalidade de frete FOB:** quando forem encontradas notas de venda e que estejam com a modalidade de frete igual a FOB, essa divergência não poderá ser resolvida porque a NF-e não pode ser alterada depois de aprovada; o ideal é verificar se a nota foi emitida corretamente e se é preciso realizar seu cancelamento;
- **Nota(s) com frete Incluso:** sendo encontradas notas de venda e que estejam com o tipo do frete igual a Incluso, essa divergência não poderá ser resolvida porque a NF-e não pode ser alterada depois de aprovada; o ideal é verificar se a nota foi emitida corretamente e se é preciso realizar seu cancelamento;
- **Divergências de mais de uma nota encontrada:** quando o sistema localiza mais de uma nota (compra e venda) para a chave NF-e encontrada no arquivo XML; nesta situação, a divergência é resolvida escolhendo qual nota será vinculada ao CT-e.

Ao importar um CT-e, assim como na importação de uma NF-e, as divergências podem ser tratadas na aba **"Cabeçalho"**, que contém algumas informações sobre o Parceiro, Empresa e Transportadora encontrados no sistema e no XML. Essas informações não são editáveis e servem para identificar possíveis diferenças.

O Parceiro da nota de compra é localizado no sistema pelo **"CPF/CNPJ"**. Caso o sistema não encontre nenhum parceiro com o CNPJ, será registrada uma divergência na importação; se encontrado mais de um parceiro com o mesmo CNPJ, também será registrada uma divergência. A mesma validação é feita para Empresa e Transportadora.

Na aba **"Ligações"**, é possível selecionar qual nota do sistema será vinculada ao CT-e. 

![Imagem 35: Na aba "Ligações" , é possível selecionar qual nota do sistema será vinculada ao CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/27083616755095)

A seção **"Chave Referenciada"** será preenchida quando o XML conter uma tag **<ChaveNFeRef>**, que vincula as notas de devolução às suas notas de origem (compra/venda).

A grade superior traz as chaves NF-e e a inferior exibe as notas que possuem aquela chave. Selecione a nota na grade inferior e dê dois cliques na mesma ou então clique no botão **"Selecionar nota"**; deste modo, o campo Nota Selecionada na grade das chaves será preenchido. Escolha todas as notas para proceder com a validação; caso alguma chave não possua uma nota selecionada, não será possível continuar com a validação.

É possível também, limpar a nota selecionada caso tenha-se escolhido alguma nota errada; além disso, pode-se abrir a nota na Central de Vendas para visualizar alguma informação, a fim de tomar a decisão de qual nota escolher.

**Nota:** na realização de uma consulta de CT-e, desde que a empresa solicitante do serviço seja também a tomadora do serviço, o documento será inserido no Portal de importação de XML. A situação e a participação da empresa em questão no documento, poderão ser visualizadas nas colunas **"Situação CT-e"** e **"Papel no CT-e"**, respectivamente, de modo que estes podem ser alimentados da seguinte forma:

| **Situação CT-e:** | **Papel no CT-e:** |
| --- | --- |
| - Uso autorizado; - CT-e cancelado; - Uso EPEC. | - Remetente; - Destinatário; - Expedidor; - Recebedor; - Tomador; - Indefinido. |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Substituição de CT-e

Ao importar um XML de CT-e de Substituição pelo Portal de Importações, o sistema identifica automaticamente se o documento contém o grupo <infCteSub> com a tag <chCTe>. Caso essa informação esteja presente e preenchida com uma chave válida de 44 dígitos, o campo **Chave CT-e Referenciada** do cabeçalho da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) é preenchido de forma automática, eliminando a necessidade de inserção manual.

A mesma chave também passa a ser exibida no [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI) → [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abageral), no campo **Chave CT-e de Referência**, e é levada para o [EFD Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI) → Aba D001 → Sub-aba D100 → Geral, no campo **Chave do Bilhete de Passagem Eletrônico substituído**.

Quando o XML não contiver substituição, o sistema simplesmente ignora o preenchimento, mantendo o fluxo normal da importação.

Para que o processo funcione corretamente, é importante que o XML esteja configurado com a tag tpCTe = 3. Além disso, a TOP deve estar parametrizada com o tipo de emissão CT-e igual a 3, na aba **“CT-e/MD-e”**, e, no **Portal de Importações**, o campo **“Tipo de Importação CT-e”** deve ser definido como **Terceiros**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação do XML do CT-e como emissão própria

Ainda tratando as peculiaridades acerca do CT-e, no processo de sua emissão própria feita por terceiros, podem ocorrer casos em que o tomador de serviço tem posse do certificado digital da transportadora, e além dele emitir o CT-e, pode-se ocorrer o cancelamento do documento. Visando suprir estas situações, a transportadora será capaz de importar o cancelamento feito pelo seu tomador de serviço.

Diante destas situações, o sistema irá proceder com as seguintes validações:

(1)**Origem e Destino do CT-e de emissão própria a ser importado:**

No momento da importação do arquivo XML de um CT-e de emissão própria, o sistema irá validar sua origem e destino com o remetente e destinatário. Internamente, o sistema irá comparar o campo **<cMunIni>** com o campo **<cMun>** filho do campo **<rem>**, além de comparar o campo **<cMunFim>** com o campo **<cMun>** do campo **<dest>**. Além disso, os parceiros deverão ser informados antes do processamento da importação, tendo-se para tal, as colunas Parceiro Coleta CT-e e Parceiro Entrega CT-e, ou seja:

- **Parceiro Coleta CT-e:** esse parceiro será preenchido somente em casos que o CT-e a ser importado for classificado como emissão própria, e o campo <cMunIni> for diferente do campo **<cMun>** filho do campo **<rem>**; obrigatoriamente este parceiro precisa ter a mesma cidade com mesmo Cód. Município Dom. Fiscal do campo **<cMunIni>**;
- **Parceiro Entrega CT-e:** esta informação será alimentada apenas em casos que o CT-e a ser importado seja classificado como emissão própria, e o campo <cMunFim> seja diferente do campo **<cMun>** filho do campo **<dest>**; obrigatoriamente este parceiro precisa ter a mesma cidade com mesmo Cód. Município Dom. Fiscal do campo **<cMunFim>**.

Ao ativar a marcação **"Preencher o campo Parceiro Entrega CT-e"** no Portal de Importação de XML, botão ![Imagem 36: Ao ativar a marcação "Preencher o campo Parceiro Entrega CT-e" no Portal de Importação de XML , botão Outras Opções ,…](https://ajuda.sankhya.com.br/hc/article_attachments/24344649125911) [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Preferências para Importar CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e), aba **"CT-e de Emissão Própria"**, o sistema não valida a origem e destino com o remetente e destinatário, preenchendo automaticamente com o parceiro destinatário do XML a coluna Parceiro Entrega CT-e e buscando no XML o município inicio (**<cMunIni>**) e o município fim (**<cMunFim>**) para preencher o **"Cód. Cid. Inicio CT-e"** e **"Cód. Cid. Fim CT-e"** do [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas). 

(1)** Informações de lacre do CT-e de emissão própria:**

Ao processar e inserir um CT-e de emissão própria, serão importados também informações pertinentes ao lacre do CT-e.

(1)** Dados de vale-pedágio do CT-e de emissão própria:**

Feito o processamento e inserção de um CT-e, serão importados dados referentes ao vale-pedágio, sendo apresentada a correspondente divergência de parceiro, caso o parceiro fornecedor de pedágio não seja encontrado.

**(1)** Tributação 060 do CT-e de emissão própria:

Quando houver, ao processar e inserir um CT-e de emissão própria, serão importados os dados correspondentes a Tributação 060 - ICMS cobrado anteriormente por substituição.

(1)** Importação de CT-e Substituição como Emissão Própria**

O sistema permite a importação de CT-e de Substituição como emissão própria através do Portal de Importação de XML. Ao importar um XML de CT-e que contenha a tag `<infCteSub>` com a chave de referência (`<chCTe>`), o sistema identifica automaticamente o documento como CT-e de Substituição.

**Preenchimento automático**

Durante o processamento da importação, o campo "Chave CT-e Referenciada", localizado no cabeçalho da Central de Compras, é preenchido automaticamente com o valor da chave informada no XML, eliminando a necessidade de preenchimento manual.

**Renegociação do financeiro (evita duplicidade)**

Para que os lançamentos financeiros não fiquem duplicados, é necessário habilitar a preferência "Utilizar renegociação em CT-e de Substituição". Com essa opção marcada, o sistema realiza automaticamente a renegociação do financeiro do CT-e substituído durante a importação do CT-e de Substituição como Emissão Própria.

> **Atenção:** caso essa preferência não esteja habilitada, o financeiro do CT-e original e o do CT-e de Substituição poderão coexistir, gerando duplicidade de lançamentos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação de cancelamento feito por terceiros de um CT-e de emissão própria

Através do Portal de Importação de XML, pode-se realizar a importação de um XML correspondente à um Cancelamento de CT-e. Quando este tipo de arquivo for importado, a coluna **"Tipo de Importação CT-e"** será definida com a opção Cancelamento, não sendo possível sua modificação. O sistema irá validar se o XML de cancelamento importado é válido quanto a sua estrutura e sua autorização junto à SEFAZ.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## CT-e importado com Pedido de Frete

O sistema realizará algumas validações para identificar o pedido de frete. Caso existam divergências, o processo não será finalizado e as respectivas mensagens serão apresentadas. Neste procedimento, pode-se ter as seguintes divergências:

- **Pedido de frete ausente para nota:** esta situação ocorrerá quando as configurações estiverem pra exigir pedido e as notas de venda encontradas não possuírem o pedido de frete vinculado à elas;
- **Mais de um pedido de frete encontrado:** este caso ocorrerá quando as configurações estiverem pra exigir pedido e as notas de venda encontradas possuírem juntas mais de um pedido de frete vinculado à elas;
- **Diferença entre o pedido de frete e o CT-e importado:** quando o valor do CT-e importado estiver diferente do valor do pedido de frete superando o percentual de tolerância configurado nas **"Preferências para importação do CT-e"**.

Estas divergências são tratadas através da aba **"Frete x Pedido Frete"**.

![Imagem 37: Estas divergências são tratadas através da aba "Frete x Pedido Frete" .](https://ajuda.sankhya.com.br/hc/article_attachments/27083512740503)

### Aba Frete x Pedido Frete

Nesta aba, pode-se definir se as divergências serão ou não aceitas; divergências estas de valores entre frete e o pedido de frete (haverá divergência somente se a diferença entre pedido de frete e valor do CT-e for maior que a tolerância configurada).

Essa validação será feita apenas quando a marcação **"Exige pedido de frete"** estiver realizada.

O sistema traz nesta aba algumas informações para que seja decidido se aceita a divergência ou não:

- **Vlr. Pedido de Frete:** valor do campo **"Valor da Nota"** do pedido de frete;
- **Vlr. Desdobramento CT-e:** valor real do CT-e;
- **Vlr. Limite pela Tolerância:** esse é o valor limite que a diferença entre o pedido de frete e o valor do CT-e pode chegar, ou seja, é o resultado da multiplicação do percentual de tolerância pelo valor do pedido de frete;
- **Vlr. Diferença:** tem-se aqui o resultado do valor do CT-e subtraído do valor do pedido de frete.

Na grade **"Sistema"** serão apresentados os itens referentes ao pedido de frete, caso existam. Já Na grade **"Arquivo"** serão apresentados os componentes de serviço do CT-e, caso estejam presentes.

Assim, caso a divergência seja aceita, basta marcar **"Aceitar Divergências"** e acionar o botão **"Validar importação"** novamente para que o problema seja solucionado.

---

#### Como Vincular CT-e a um Pedido de Frete com Valores Divergentes

Para vincular o CT-e ao Pedido de frete cujos valores estejam divergentes, siga os passos abaixo:

![Imagem 38: Após realizar a importação e processamento do arquivo, selecione o Parceiro desejado e confirme.](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) Após realizar a importação e processamento do arquivo, selecione o Parceiro desejado e confirme.

![Imagem 39: Verifique os pedidos de frete disponíveis para ligação na aba "Pedido de Frete" .](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) Verifique os pedidos de frete disponíveis para ligação na aba **"Pedido de Frete"**.

![Imagem 40: Acione o botão "Liberar para reprocessamento" , em seguida, selecione o pedido de frete que deseja vincular a nota,…](https://ajuda.sankhya.com.br/hc/article_attachments/27539664299159) Acione o botão **"Liberar para reprocessamento"**, em seguida, selecione o pedido de frete que deseja vincular a nota, clique em **"Ligar Pedido de Frete ao CT-e"** e confirme.

![Imagem 41: Após a execução do reprocessamento, serão exibidas duas mensagens informando as "Divergências" e solicitando a…](https://ajuda.sankhya.com.br/hc/article_attachments/27547895482391) Após a execução do reprocessamento, serão exibidas duas mensagens informando as **"Divergências"** e solicitando a confirmação da exclusão do documento relacionado ao registro. Clique em **"Ok"** e **"Sim"**, respectivamente.

![Imagem 42: Por fim, ative a marcação Aceitar Divergências na aba Frete x Pedido Frete e clique no botão "Processar" .](https://ajuda.sankhya.com.br/hc/article_attachments/27547851219607) Por fim, ative a marcação Aceitar Divergências na aba Frete x Pedido Frete e clique no botão **"Processar"**.

Pode-se confirmar se o pedido foi vinculado à nota, acionando o botão **"Abrir Documento"**. Assim, ao ser redirecionado para a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), pressione o botão **"Outras opções"** e selecione a opção **"Documentos relacionados"**, onde será aberto um pop-up apresentando o documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Rateio do Frete

Assim que todas as divergências forem resolvidas o sistema irá proceder com a inclusão do financeiro e fará o rateio do valor do frete para as notas encontradas.

Esse rateio será feito conforme a configuração da seção **"Critério para rateio do valor do frete"** presente na opção [Preferências para Importar CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e), do botão [Outras opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es):

![Imagem 43: Esse rateio será feito conforme a configuração da seção "Critério para rateio do valor do frete" presente na opção…](https://ajuda.sankhya.com.br/hc/article_attachments/27733692241687)

Sendo que, quando o campo **"Tipo"** for configurado com a opção:

- **Valor:** é somado o valor do campo **"Valor da Nota"** de todas as notas. Pega-se o valor de cada nota, divide-se pelo valor total das notas e o multiplica pelo valor do frete. O resultado será o valor do frete para cada nota.

**Atenção Implantadores!** Este registro será salvo na tabela TGFFNF.

- **Peso:** é somado o valor do campo **"Peso Total"** de todas as notas. Pega-se o peso de cada nota, divide-se pelo peso total das notas e o multiplica pelo valor do frete. O resultado será o valor do frete para cada nota.

**Atenção Implantadores!** Este registro será salvo na tabela TGFFNF.

Se o valor total do peso for igual a zero, automaticamente o sistema fará o rateio pelo valor, mesmo que esteja configurado para realizar o rateio por peso.

**(1)** Quando o parâmetro **"Vlr total da nota e peso p/ calc. do rateio de frete -** **VLRTOTNOTAPESO"** estiver ativado, o sistema distribui o valor total da carga entre as notas fiscais. Caso esteja desativado, utiliza diretamente o valor da nota fiscal (**VLRNOTA**) da tabela **TGFCAB**, sem rateio.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Calcular vencimento do CT-e

Através do parâmetro **"Procedure para cálculo da data vencimento do CT-e - NOMPROCCALDTVEN"** informa-se o nome da procedure que será utilizada para fazer o cálculo da data de vencimento do CT-e.

Essa procedure pode possuir cinco parâmetros de entrada e um de saída:

- **Entrada:** Código da Transportadora, Data de Negociação do CT-e, Valor de Desdobramento do CT-e, Código do Parceiro Remetente e Código do Parceiro Destinatário;
- **Saída:** Data de vencimento calculada.

Considerando que o parâmetro tenha sido informado, o sistema buscará a data de vencimento na seguinte ordem:

![Imagem 44: Irá buscar a data de vencimento no arquivo CT-e;](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) Irá buscar a data de vencimento no arquivo CT-e;

![Imagem 45: Caso não encontre, buscará a data pela procedure;](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) Caso não encontre, buscará a data pela procedure;

![Imagem 46: Se não encontrar, o sistema irá buscar conforme configurado nas preferências (como é feito normalmente).](https://ajuda.sankhya.com.br/hc/article_attachments/27539664299159) Se não encontrar, o sistema irá buscar conforme configurado nas preferências (como é feito normalmente).

Se o parâmetro não for informado, o sistema buscará a data de vencimento com base nas preferências configuradas, seguindo o procedimento padrão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Cancelar CT-e importado

No alto da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), tem-se o botão **"Cancelar CT-e"**, que estará disponível para uso apenas se o financeiro possuir a Chave CT-e informada.

O botão Cancelar CT-e executará o mesmo procedimento de excluir o CT-e, ou seja, a ação executada será a mesma que o botão excluir financeiro realiza, contudo, para que o sistema realize tal procedimento pelo referido botão, o financeiro deve atender aos seguintes critérios:

- Não pode ter sido baixado;
- Chave CT-e informada;
- Deve ser uma despesa;
- A TOP deve possuir modelo de documento igual a **"57 - Conhecimento Transporte Rodoviário Eletrônico"**;
- Deve existir registro no Portal de importação de XML para o financeiro a ser cancelado.

Esse cancelamento excluirá o financeiro atualizando os dados necessários (valores de frete das notas envolvidas e atualização de pedido de frete para Pendente/Não Pendente, se existir).

No cancelamento do CT-e os seguintes dados a respeito do frete são atualizados:

- O campo **"Valor do Frete"** das notas presentes na tabela TGFFNF terão seus valores atualizados (será feita uma soma na TGFFNF por nota);
- Se o pedido de frete das notas que estão vinculadas ao financeiro cancelado não estiver ligado a outras notas, o mesmo será atualizado para pendente, ou seja, o campo **"Pendente"** ficará igual a **"Sim"**, caso contrário continuará como Pendente igual a **"Não"**.

Pode-se também excluir financeiros pela Movimentação Financeira. Logo, o sistema verificará da mesma forma a questão da atualização dos dados de frete.

- Se as notas presentes na tabela TGFFNF para o financeiro excluído estiverem vinculadas também a outros financeiros, o campo Valor do Frete das notas será atualizado (será feita uma soma na TGFFNF por nota);
- Se o pedido de frete das notas que estão vinculadas ao financeiro excluído não estiver ligado a outras notas, o mesmo será atualizado para pendente, ou seja, o campo Pendente ficará igual a Sim, caso contrário continuará como Pendente igual a Não.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação de Notas contendo Medicamentos

Através do Portal de importação de XML é possível realizar a importação de uma nota que contenha medicamentos com Lote, Data de Fabricação e Validade, de modo que, os medicamentos contidos na nota, podem ser ligados aos pedidos de compra pendentes destes medicamentos.

As informações referentes a lote, data de validade e data de fabricação são identificadas através do campo **<rastro>**. Os campos identificados são:

- <nLote>
- <qLote>
- <dFab>
- <dVal>

**Importante:** essas informações somente poderão ser importadas, caso o produto em questão possua o rastreamento ativo ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral) ou aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa), marcação **"Tem Rastro do Lote"**).

Caso o produto tenha rastreamento ativo e o XML não possua as informações citadas acima (lote, data de validade e data de fabricação), o sistema irá exibir um aviso informando que o produto importado possui rastreamento de estoque e controle adicional por lote, e o XML não possui tais dados, de modo que será necessário digita-las na nota de compra. De maneira contrária, caso o produto não tenha o rastreamento ativo e o XML possua os campos citados acima informados (lote, data de validade e data de fabricação), o sistema também irá apresentar um aviso alertando sobre tal fato.

Os medicamentos são inseridos na nota de compra da mesma maneira que se a nota de compra fosse importada na Central de Compras pelo importador de XML convencional (Botão Outras Opções, opção **"Importar Xml de nota fiscal eletrônica"**).

Os pedidos de compra podem ser ligados de forma automática ou manual. Isso dependerá do XML, pois, se ele possuir o campo **<xPed>** preenchido e tal pedido existir, será feita a ligação automaticamente, caso contrário precisará ser feito manualmente.

Ao importar o XML das operações de Medicamentos contendo produtos que possuem controle adicional por lote e rastro de lote, para que o sistema faça a conversão da quantidade que será considerada no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) é necessário realizar as seguintes configurações:

- No cadastro do Produto, as opções **"Tem Rastro do Lote"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral)) e **"Controle Adicional"**(aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional)) devem estar configuradas.
- O parâmetro **"Usar unidade do lote para conversão do qLote - USARUNIDLOTE"** deve ser ligado para que a coluna **"Unidade do lote"** seja exibido na aba Produtos por Parceiro, onde a unidade alternativa deverá ser obrigatoriamente informada. Porém, caso o lote não seja informado nesse campo, o parâmetro USARUNIDLOTE deve ser desligado.

**Observação:** se o Produto informado tiver controle adicional por Número do lote e a opção Tem Rastro do Lote estiver habilitada, mas campo Unidade do Lote estiver vazio, o sistema apresentará a mensagem de erro abaixo:

**"Quando o produto tiver controle adicional por “Número do lote” e opção “Tem Rastro do Lote” marcado, o campo Unidade do Lote é obrigatório."**

Caso o produto não tiver controle adicional por Número do lote e/ou a opção Tem Rastro do Lote não estiver efetuada, então a coluna Unidade do Lote será apresentado em branco e sem edição.

![Imagem 47: Caso o produto não tiver controle adicional por Número do lote e/ou a opção Tem Rastro do Lote não estiver efetuada,…](https://ajuda.sankhya.com.br/hc/article_attachments/27548383662359)

A importação de produtos que não são medicamentos na nota de compra, mas que possuem qualquer controle adicional de estoque no sistema, não sofre modificações, inclusive a respeito da ligação com os pedidos de compra.

**Importante:** a ligação dos medicamentos da nota com os pedidos de compra não exige que os pedidos de compra tenham a informação do Lote, Data de Fabricação ou Validade.

Ao trabalhar com um produto que possua controle adicional de estoque por número de lote, os parâmetros **"Usar data de validade junto com Lote? - LOTEDTVAL"** e **"Usar data de Fabricação junto com Lote? - LOTEDTFAB"** estiverem ativados e no XML existirem lote nos produtos, ao utilizar o Portal de importação do XML, o Lote será importado juntamente com sua respectiva Dt. Fabricação e Dt.Validade. Partindo deste comportamento, as seguintes situações podem ocorrer:

- **O XML importado e o produto contém informações de Controle por lote:** neste caso, os produtos serão importados com sua correspondente numeração de lote, bem como suas datas de fabricação e validade;
- **O XML não possui informações sobre o controle por lote, porém tem-se um produto que tem a configuração de Controle por lote:** nesta situação, o lote e os dados pertinentes à Data de Validade e Data de Fabricação podem ser incluídos através da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), utilizando-se o **"Botão Outras Opções"** presente na grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens), opção **"Informações de Controle Adicional"**, onde será aberto um pop-up com esta mesma nomenclatura para inserção destes dados;
- **O XML e o produto não possuem configurações de Controle por lote:** neste caso, não será possível utilizar o botão Outras Opções, opção Informações de Controle Adicional, pois este não estará habilitado.

De forma semelhante ao terceiro caso, ao realizar a importação de um XML composto por itens controlados por lote, caso tenha-se um mesmo produto que possua mais de um lote, os dados pertinentes a Data de Validade e Data de Fabricação também podem ser incluídos através da Central de Compras, utilizando-se do Botão Outras Opções, opção Informações de Controle Adicional.

**Observação:** vale salientar que para funcionamento deste processo de importação de produtos controlados por lote, é indispensável que os parâmetros LOTEDTVAL e LOTEDTFAB estejam ativados. Além disso, para que as informações pertinentes ao lote dos produtos sejam importadas, é necessário que a marcação **"Atualizar Estoq. a partir da Confirmação"** presente no cadastro de [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), esteja realizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação dos dados do FCP e Impostos

Na importação do XML, para que os dados referentes ao Fundo de Combate à Pobreza (FCP) sejam importados, é necessário que a marcação **"Calcular FCP (ICMS/ST) Interno?"** presente no cadastro de Tipos de Operação-TOP, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), esteja realizada.

Além disso, a importação irá ocorrer de acordo com a definição realizada no campo **"Cálculo de ICMS, IPI e ISS"** também presente na aba Impostos, ou seja:

- **Não calcula e não digita:** as informações citadas não serão importadas, nem calculadas pelo sistema;
- **Calcula e não digita:** os dados citados não serão importados, porém são calculados pelo sistema;
- **Calcula e digita:** as informações citadas serão importadas e não serão consideradas para comparação de impostos entre o XML e sistema;
- **Não calcula e digita:** por esta opção, tem-se o mesmo comportamento citado em relação a opção Calcula e digita;
- **Calcular na confirmação:** os dados citados não são importados, porém calculados pelo sistema no momento da confirmação da nota de compra importada.

**Nota:** no momento em que o Portal de Notas estiver efetuando a leitura do XML para importação de seus valores, caso tenha alguma informação na tag <**vFCP**>, o valor será importado mesmo que as outras tags do arquivo não encontrem-se preenchidas.

**Observação:** ao realizar a importação do XML, caso esteja faltando alguma informação referente ao cálculo do imposto, o sistema deverá complementá-lo; desta forma, considere o seguinte exemplo:

No XML tem-se os valores nas tags <**pFCP**> e <**vFCP**>; como o valor referente à **<vBCFCP>** é o mesmo que a Base ICMS, o sistema poderá utilizar a informação deste para preencher o campo **"Base para Fundo Comb. Pobreza"** da Central de Notas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação de XML com Desmembramento de Itens em Lotes

Para realizar o desmembramento de itens por lote durante a importação de arquivos XML contendo produtos com mais de um grupo de rastreabilidade, é necessário que as seguintes configurações sejam previamente efetuadas:

![Imagem 48: Na tela Preferências , ligue os parâmetros:](https://ajuda.sankhya.com.br/hc/article_attachments/25750103226775) Na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), ligue os parâmetros:

- Usar data de validade junto com Lote? - LOTEDTVAL;
- Usar data de Fabricação junto com Lote? - LOTEDTFAB.

![Imagem 49: No Cadastro de Produtos , aba Geral , acione as marcações:](https://ajuda.sankhya.com.br/hc/article_attachments/25750061669015) No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), acione as marcações:

- Utiliza data de Fabricação;
- Utiliza data de Validade;
- Tem Rastro do Lote.

![Imagem 50: Ainda nessa tela, na aba Medidas e Estoque , sub-aba Controle Adicional defina o campo "Controlar por" com a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/27539664299159) Ainda nessa tela, na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) defina o campo **"Controlar por"**com a opção **"Número de lote"**.

Com essas configurações feitas, ao importar o XML que contenha o desmembramento de itens por lote e processar o arquivo, o sistema registrará o item na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) considerando o desmembramento e aplicará o rateio aos campos de valores com base na quantidade de cada lote.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Importação de Notas contendo ICMS Monofásico

Para que o Portal de importação de XML processe os XMLs de produtos monofásicos para os tipos de documentos: NF-e Compra, NF-e Compra Emissão Própria, Dev. de Venda Emissão Própria e Dev. de Compra Emissão Própria, é necessário considerar as regras da [Nota Técnica 2023.001 - v.1.10](https://ajuda.sankhya.com.br/hc/pt-br/articles/22268069589399).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Controle de Documentos Cancelados

Para identificar os documentos que foram atualizados com status Cancelado, basta realizar os seguintes filtros no Portal de importação de XML:

**(1)** **Para CT-e:**

ImportacaoXMLNotas.SITUACAOCTE = 'C' AND
ImportacaoXMLNotas.TIPO = 'C' AND
ImportacaoXMLNotas.STATUS = 2

**(1)** **Para NF-e:**

ImportacaoXMLNotas.SITUACAONFE = 3 AND
ImportacaoXMLNotas.TIPO = 'N' AND
ImportacaoXMLNotas.STATUS = 2

Deste modo, após localizar os documentos que foram cancelados pelo emissor, deve-se analisar e realizar as tratativas necessárias (verificar se deverá ser excluído no sistema, se o financeiro já foi baixado, se já foi escriturado no livro, entre outros).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)

## Seleção de notas de venda

O botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Preferências para importação de NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimporta%C3%A7%C3%A3odenf-e), possui a marcação **"Permitir vinculo Manual para NFe Devolução para NFe Venda"** que quando efetuada, determina se o Portal de Importação de XML permitirá o vínculo manualmente das referências entre as NFe de Devolução e NFe de Venda.

**Observação:** o vínculo manual não se aplica para devolução de compra ou venda de emissão própria.

**Nota:** durante o processamento do arquivo importado, caso o XML da nota de devolução apresente alguma inconsistência com relação à nota de origem, será exibida a mensagem abaixo:

**"Devolução sem Nota de Venda, efetuar o Ref. Manual."**

Assim, a aba **"Seleção de notas de venda"** será habilitada na tela Portal de importação de XML, contendo as notas de venda do mesmo parceiro da nota de devolução para serem vinculadas:

![Imagem 51: Assim, a aba "Seleção de notas de venda" será habilitada na tela Portal de importação de XML , contendo as notas de…](https://ajuda.sankhya.com.br/hc/article_attachments/10056300776471)

Na grade **"Itens disponíveis"**, caso queira editar a quantidade de produtos disponíveis, clique duas vezes sobre a coluna **"Disponível"** e informe o valor desejado. Depois, acione o botão **"Adicionar itens"** e, em seguida, clique em **"Associar itens"**.

Feito isso, na grade **"Produtos do XML"**, coluna **"Divergência"**, confira o valor restante a ser associado ao item.

Caso seja necessário remover a quantidade informada, basta acionar o botão **"Remover itens"**.

Na grade **"Notas disponíveis"** serão exibidas apenas as notas da empresa do XML de devolução. As notas com status **"Aguardando Correção"** não serão apresentadas nesta grade.

Quando a marcação **"Permitir vinculo Manual para NFe Devolução para NFe Venda"** (botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Preferências para importação de NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimporta%C3%A7%C3%A3odenf-e)) estiver desabilitada ao importar notas de **devolução de emissão própria**, o sistema Sankhya fará o vínculo automático da **nota referenciada** apenas nos casos em que o XML possuir **apenas um item**.

Se a nota de devolução tiver **mais de um item**, o vínculo com a nota de origem deverá ser feito **manualmente**.

Ao importar notas de **devolução de emissão própria**, o sistema Sankhya fará o vínculo automático da **nota referenciada** apenas nos casos em que o XML possuir **apenas um item**.

Se a nota de devolução tiver **mais de um item**, o vínculo com a nota de origem deverá ser feito **manualmente**. Para isso:

1. Acesse **Central de Vendas**.
2. Vá para a **Grade de Itens** da nota de devolução.
3. Clique em **Outras Opções > Documentos Referenciados**.

Durante o processo de vinculação:

- Ao abrir o pop-up de Documentos Referenciados em um item específico, o vínculo deve ser feito com a **sequência correspondente da nota de origem**.

  - Exemplo: Se você abriu o pop-up no item de sequência 1, vincule a sequência 1 da nota de origem.
  - Se abriu no item de sequência 2, vincule a sequência 2 da origem, e assim por diante.

**Atenção:**
No pop-up, existe uma opção no canto superior chamada **"Apenas este item"** ou **"Todos os itens"**.
Essa opção é apenas **visual**: ela serve para apresentar os documentos já lançados e **não interfere** no vínculo do item selecionado.

Para saber mais sobre isso acesse a opção **Documentos Relacionados** na **Grade de Itens** no botão **Outras Opções** da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#documentosrelacionados) e [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)
