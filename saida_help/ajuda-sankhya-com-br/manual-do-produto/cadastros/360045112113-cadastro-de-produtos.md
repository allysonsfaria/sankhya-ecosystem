---
id: "360045112113"
titulo: "Cadastro de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos"
trilha: "Manual do Produto > Configurações e Cadastros > Cadastros"
atualizado_em: "2026-09-15T12:18:56Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Consignação", "Configuração", "Complemento", "Parceiro", "PARCIMPFICI", "COPITEMCOMPPRO", "Amostra", "CONFMODGRDPESQ", "ORDENAFILTROS", "Anexo", "Apresentar nas tarefas do WMS", "Código da Empresa", "Consignante", "DESCONSMARCPROD", "DESCRCOMPL", "Descrição complemento", "DESCRLOCAL", "DESCRLOCALIZ", "DESCRMARCA", "DESCRPESOLIQ", "DESCRREF", "EAN13", "EAN14", "FATCONTLOCBEM", "Grupo de ICMS 2", "Imprimir Etiquetas", "Itens da nota", "Origem do Produto", "Peso Líquido", "br.com.sankhya.core.cad.produtos", "Produtos  manual", "ORDENARABAS", "Impostos", "Componentes", "Documentos", "Estoque", "CONTROLEADEMP", "LOTAUTKIT", "LIMITIMGPROD", "PRIDVCEN", "Cadastro", "UTILGRUPPF", "criando produtos"]
---

# Cadastro de Produtos

```
 Módulo: Configurações > Cadastros
```

---

Atualmente, em uma empresa de comercialização de itens palpáveis, o produto é considerado a ferramenta de cunho fundamental para os processos de [Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras) e [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas). A instituição adquire o(s) produto(s) para revenda ou a(s) matéria(s) prima(s) para produção de itens próprios. Além disso, tem-se em meio ao processo de Compras, as solicitações internas, que tem por objetivo sanar as deficiências de materiais nos vários setores da empresa.

Esta documentação permitirá ter uma visão completa de como efetuar o cadastro de um produto. Servirá também de apoio à consultas futuras para esclarecimentos de dúvidas, quanto à parametrização, principais tipos de erros e as possíveis maneiras de corrigi-los.

| Funcionalidades da tela | |
| --- | --- |
| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#painelprincipal) | [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) |
| [Aba Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedicamentos) | [Aba Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abavenda) |
| [Aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) | [Aba Plan. de Compra de Peças](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaplan.decompradepeas) |
| [Aba Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaapontamentos) | [Aba Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas) |
| [Aba Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacdigodebarras) | [Aba Perfil de Consumo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaperfildeconsumo) |
| [Aba Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) | [Aba Família](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abafamlia) |
| [Aba Classificação por Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaclassificaoporproduto) | [Aba Produtos Alternativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosalternativos) |
| [Aba Produtos Específicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosespecficos) | [Aba Outros Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaoutrosimpostos) |
| [Aba Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaalquotainternadedestino) | [Aba Funções que utilizam E.P.I](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abafunesqueutilizame.p.i) |
| [Aba Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosequivalentes) | [Aba Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abatiposdeamostra) |
| [Aba Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) | [Aba Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacomponentes) |
| [Aba Disponibilidade diária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abadisponibilidadediria) | [Aba Combustível](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacombustvel) |
| [Aba WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abawms) | [Aba Flex](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaflex) |
| [Aba Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaformaodecustopreo) | [Aba Produtos sugeridos para venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutossugeridosparavenda) |
| [Aba Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaestoque) | [Aba Imagem Alternativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimagemalternativa) |
| [Aba Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens) | [Aba Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamanufatura) |
| [Aba 0200 do EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#0200doEFD) | [Aba Anexos/Documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaanexosdocumentos) |
| [Aba IPI por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaipiporparceiro) | [Unidade de Mov./Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#unidadedemov.armazenagem) |
| [Aba Rastreamento Por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abarastreamentoporempresa) | [Aba Controle FCI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaControleFCI) |
| [Botões da tela Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela) | [Parâmetros utilizados nesta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#par%C3%A2metrosutilizadosnestarotina) |

---

## Painel Principal

Localizado no alto da tela, o Painel Principal reúne os dados que servirão de base para todo o restante do cadastro dos Produtos.

![Imagem 1: Localizado no alto da tela, o Painel Principal reúne os dados que servirão de base para todo o restante do cadastro dos…](https://ajuda.sankhya.com.br/hc/article_attachments/24177813438615)

O campo **"Código"** pode ser preenchido de forma manual ou automática; esta definição é feita pelo botão ![Imagem 2: O campo "Código" pode ser preenchido de forma manual ou automática; esta definição é feita pelo botão "Configuração da…](https://ajuda.sankhya.com.br/hc/article_attachments/16343426954903) **"Configuração da tela"** localizado na parte superior da tela. Informe neste campo, a numeração responsável por identificá-lo em todas as rotinas em que ele estiver presente.

No campo **"Descrição"** aponte o nome do produto que está sendo cadastrado.

Assim, ao habilitar a marcação **"Ativo"**, possibilitará movimentações com o produto. Caso contrário, torna-o inativo, impossibilitando a sua utilização.

A data e horário da última alteração realizada no cadastro do produto são registrados no campo **"Data da Alteração"**. Sendo que, o seu preenchimento é efetuado de forma automática pelo sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Geral

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/4402109896087)

Para que o campo **"Descrição para NFE"** seja apresentado é necessário que o parâmetro **"Utiliza descrição do produto para NFE? - USADESCRPRODNFE"** se encontre habilitado. Este campo permite que informar qual será a descrição para NF-e impressa no relatório de registro de controle da produção e do estoque que é gerado através da tela [Registro da Produção e do Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607894).

O campo **"Complemento"** tem a finalidade de comportar as informações complementares do produto, ou seja, os dados adicionais pertinentes ao mesmo. Como por exemplo, para o produto Extrato de tomate o complemento poderia ser lata de 100g, extrato peneirado, entre outros.

No campo **"Grupo"**, informe a qual grupo pertence o produto em questão. Sendo que, é necessário realizar previamente o cadastro dos grupos através da tela [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os).

A unidade de venda do produto, ou seja, a forma como o produto está sendo vendido é indicada no campo **"Unidade padrão"**. Tem-se como exemplo de unidade de venda o Quilo, Metro, Litro, Peças, entre outros. 

**Observação:** recomenda-se a configuração o campo Unidade padrão com a menor unidade do produto. Desta forma, nesta mesma rotina na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas) configure as demais unidades do produto. Abaixo tem-se um exemplo:

O produto X pode ser comercializado em **"Unidade"**, **"Pacotes com 5 unidades"** e **"Caixas de 20 unidades"**. Assim, o campo Unidade padrão é configurado com a **"UN - Unidade"** e na aba Unidades Alternativas configura-se as unidades **"CX - Caixa"** e **"PC - Pacote"**.

O campo **"Parceiro Fornecedor preferencial"** é disponibilizado para que seja informado o parceiro ao qual se tem preferência em fornecer o produto. A informação deste campo será usada para geração de pedidos.

Através do campo **"Referência do Fornecedor"**, indique o código do produto no fornecedor.

A empresa que executa a fabricação do produto será indicada no campo **"Fabricante"**.

Utilize o campo **"Referência"** para informar o código de barras do produto, sendo que, é possível preencher de forma automática os dados deste campo, através do botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela), opção **"Calcular Cód. Barra EAN13 p/ este Produto (Referência)..."**.

O local onde o produto se encontra armazenado, como por exemplo uma Prateleira, o Almoxarifado, o Depósito, será apontado no campo **"Localização"**. Este campo permite uma pesquisa dos locais já cadastrados anteriormente para outros produtos. Caso nenhuma localização tenha sido salva, a busca retornará em branco. Assim sendo, ao informar e salvar uma localização para o produto, a mesma estará disponível para seleção nas próximas pesquisas.

O campo **"Seleção"** é mais uma forma de diferenciar um produto. Como por exemplo, sendo necessário classificar os produtos em A, B, C. Para realizar este cadastro, basta informar a letra pertinente ao produto no campo Seleção.

A marca que efetua a representação da empresa no mercado é indicada através do campo **"Marca"**.

Informe no campo **"Home Page"** o site do produto ou site da marca do produto.

No campo **"Origem do produto"** informe se a mercadoria é Nacional ou Estrangeira, de acordo com as seguintes opções:

- 0-Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;
- 1-Estrangeira, importação direta, exceto a indicada no código 6;
- 2-Estrangeira, adquirida no mercado interno, exceto a indicada no código 7;
- 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%;
- 4-Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos;
- 5-Nacional, mercadoria ou bem com conteúdo de importação inferior ou igual a 40%;
- 6-Estrangeira, importação direta, sem similar nacional, constante em lista da CAMEX;
- 7-Estrangeira, adquirida no mercado interno, sem similar nacional, constante em lista da CAMEX;
- 8-Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.

Quando o código da Origem do Produto for 1, 2, 3 ou 8, informe a alíquota de 4,00% na tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), campo **"Alíquota"**. Já, quando o código for 0, 4, 5, 6 ou 7, informe a alíquota de 7.00% ou 12.00%, conforme a UF de destino.

![Imagem 4: Atenção Consultor Sankhya: a busca pela informação do campo "Origem do Produto" na Central de Vendas é feita por meio…](https://ajuda.sankhya.com.br/hc/article_attachments/16082119232151) **Atenção Consultor Sankhya:** a busca pela informação do campo **"Origem do Produto"** na Central de Vendas é feita por meio de uma função que pesquisa as informações por empresa; não existindo, busca-se do próprio cadastro de Produtos (Origem do Produto).

Esta busca é passível de personalização, onde individualiza-se a função **"SNK\_GET\_ORIGEM\_PRODUTO\_ALT"**. Esta função originalmente retorna nulo, fazendo com que a pesquisa busque de forma padrão, retornando qualquer valor que este campo tenha assumido.

Este recurso visa resolver casos em que a empresa compra produtos de origens diferentes (geralmente nacional e importado), não sendo viável criar dois códigos de produtos. Com esta personalização, poderão ser criados meios de se identificar a origem do produto, como por exemplo pelo controle ou local.

No campo **"Endereço da Imagem"** informe o diretório (pasta) na máquina onde encontra-se salvo o arquivo referente a imagem do produto, para que esta imagem seja utilizada tanto no Lojista OnLine, quanto para realizar o upload das imagens disponíveis no endereço local da máquina através da opção [Importar Imagens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela#botooutrasopes...) do botão Outras Opções....

O campo **"Usado como"** tem a finalidade de identificar qual é a funcionalidade do produto para a empresa. Um produto pode ser aplicado de acordo com as seguintes opções:

| - Embalagem; - Subproduto; - Prod.Intermediário; - Demonstração; - Brinde; - Consumo, - Venda (fabricação própria); - Revenda; | - Brinde (NF); - Imobilizado; - Matéria-prima; - Outros insumos; - Em processo; - Revenda (por fórmula); - Terceiros. |
| --- | --- |

---

**![Imagem 5: Informações adicionais sobre o campo Usado como :](https://ajuda.sankhya.com.br/hc/article_attachments/16090015459095) Informações adicionais sobre o campo Usado como:**

Para que a Numeração de Lote das Matérias-Primas no processo de compra seja gerada automaticamente, o campo Usado como necessita estar configurado com a opção **"Matéria-Prima"** e na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), o campo **"Controlar por"** deve indicar a opção **"Número do lote"**.

Para definir um produto como imobilizado, selecione no campo Usado como a opção Imobilizado. Ao escolher esta opção, os campos **"Identificação do Imobilizado"** e **"Utilização do Imobilizado"** localizados na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos), também deverão ser preenchidos. A aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens) será habilitada, na qual serão cadastradas a estrutura, a taxa de depreciação, as contas contábeis e a especificação do bem.

Caso queira que um, ou mais tipos de Usado como não sejam considerados na validação de NCM se o produto fizer o uso deste, basta informar a primeira leras destes no campo do parâmetro **"Não validar NCM para produtos 'Usados como' - VALUSOPRODNCM"**.

Quando o parâmetro **"Faz cálculo de CFOP em transferência? - CALCCFOPTRANSF"** estiver ligado, o sistema irá considerar o campo Usado como desta tela para o cálculo da CFOP do item de sequência negativa. Quando este parâmetro for desligado a CFOP será convertida para entrada, não considerando as configurações realizadas neste campo.

Quando a opção Brinde estiver selecionada no campo Usado como, é necessário preencher o campo **"%Desc. Bonif"** na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da tela [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), para garantir que o CFOP seja calculado corretamente.

![Imagem 6: O sistema não irá aplicar o percentual de desconto no Vlr. Total e Vlr. Unitário para produtos configurados como Brinde…](https://ajuda.sankhya.com.br/hc/article_attachments/34819938997399) O sistema não irá aplicar o percentual de desconto no **Vlr. Total** e **Vlr. Unitário** para produtos configurados como **Brinde** ou **Brinde (NF)**. Esse é o comportamento padrão, pois, para a emissão de uma nota fiscal de brinde, o produto deve ser 100% bonificado, e a legislação da NF-e não permite produtos sem preço.

Para emitir corretamente uma nota de brinde, você deve usar um **Tipo de Operação - TOP** com as seguintes configurações:

- Marcação **Bonificação** ligada.
- **CFOP** (Código Fiscal de Operações e Prestações) de bonificação.
- A configuração deve **Não gerar Financeiro**.

Caso o parâmetro **"Gerar notas com CFOP de Aquisição de Energ. Elétrica no C500 - GERNFENERC500"** esteja ligado, ao gerar o EFD Contribuições com a nota modelo 55 de emissão de terceiros, e este possuir algum item configurado como Consumo, e algum dos CFOP's:

| - 1251; - 1252; - 1254; - 1255; - 1256; - 1257; - 2251; | - 2252; - 2253; - 2254; - 2255; - 2256; - 2257. |
| --- | --- |

O Registro C500 será preenchido, se não possui nenhum dos CFOP's mencionados acima, este sairá no Registro C100, pois este em questão ocorre por nota, e não por item. Portanto no Registro C500 será gerado todos os itens independente da CFOP, pois este será gerado por item.

---

Com a Reforma Tributária, a informação do campo Usado como é usada na emissão da NF-e e da NFC-e para preencher o campo **indBemMovelUsado** no XML, conforme a **NT 2025.002-RTC**.

Para isso, é necessário que:

- O campo **“Identificação do Imobilizado”** esteja configurado como **“Veículos”**.
- O parceiro do documento seja:
  - **Pessoa Física** (Cadastro de Parceiros → campo **“Tipo de Pessoa”** = Física); ou
  - **Microempreendedor Individual (MEI)** ([Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) → campo **“Tipo de Pessoa”** = Física e opção **“Microempreendedor Individual”** marcada na aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal)).

Ao atender a esses dois requisitos, você garante que a tag <indBemMovelUsado> será incluída corretamente no XML.

![Imagem 7: Para mais informações acesse a categoria da Reforma Tributária ou o Guia da Reforma .](https://ajuda.sankhya.com.br/hc/article_attachments/16089265951767) Para mais informações acesse a categoria da [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) ou o [Guia da Reforma](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao).

---

Referente ao campo **"Tipo do item p/ SPED"**, a opção selecionada para este campo será utilizada na geração do SPED, sendo assim, tem-se as opções:

- Utilizar do "Usado como";
- Mercadoria para revenda;
- Matéria -Prima;
- Embalagem;
- Produtos em Processo;
- Produto Acabado;
- Subproduto;
- Produto Intermediário;
- Material de Uso e Consumo;
- Ativo Imobilizado;
- Serviços;
- Outros Insumos;
- Outras.

**Nota:** caso selecione a opção Utilizar do "Usado como", o sistema utilizará a informação preenchida no campo Usado como para realizar a geração do SPED.

O campo **"Unid. Compra"** representa a forma de compra do produto, se este foi adquirido pela empresa em quilos, litros, metros, peças, entre outros. Lembrando que, a unidade informada neste campo será sugerida no lançamento de um pedido/nota de compra do produto. Caso não seja configurada uma unidade de compra, será sugerida a Unidade padrão.

Além disso, se a unidade de compra informada for diferente da Unidade padrão e a mesma não estiver cadastrada como Unidade Alternativa, o sistema levará a unidade padrão para o lançamento do pedido/nota. Por fim, se a Unidade de Compra for uma Unidade Alternativa e houver um multiplicador para valor configurado, o sistema efetuará os cálculos necessários para atualização do Vlr unitário ao incluir o item no pedido/nota de compra.

![Imagem 8: Um produto pode ser comprado de uma forma e vendido de outra, ou seja, uma empresa pode comprar um produto em caixas e…](https://ajuda.sankhya.com.br/hc/article_attachments/27540392620439) Um produto pode ser comprado de uma forma e vendido de outra, ou seja, uma empresa pode comprar um produto em caixas e vendê-lo em unidades.

Descreva no campo **"Características"** as particularidades que representem relevância a respeito do produto.

Utilizando o campo **"Imagem"**, existirá a possibilidade de incluir ou alterar uma imagem para o produto. Para tal, passe o cursor do mouse sobre a imagem padrão ou imagem inserida anteriormente e clique no botão ![Imagem 9: Utilizando o campo "Imagem" , existirá a possibilidade de incluir ou alterar uma imagem para o produto. Para tal, passe…](https://ajuda.sankhya.com.br/hc/article_attachments/16083532793495) **"Enviar Imagem"**, uma janela é exibida para a seleção de um arquivo de imagem válido.

**Observações**

- Para ampliar o tamanho da imagem inserida, basta clicar sobre a mesma. Recomenda-se a utilização de imagens que contenham um tamanho reduzido, evitando assim, a limitação do desempenho do sistema.
- Para garantir a compatibilidade e o desempenho no processamento de imagens com resoluções mais altas (acima de 2000px de largura ou altura), é obrigatório atualizar o Java 8 para a build mais recente da série 8 (Java 8u451).

Para excluir a imagem, é necessário clicar no botão ![Imagem 10: Para excluir a imagem, é necessário clicar no botão "Excluir Imagem" .](https://ajuda.sankhya.com.br/hc/article_attachments/16083750103063) **"Excluir Imagem"**.

O campo **"Ordem Medida"** tem como funcionalidade organizar em ordem crescente na [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos), os produtos que apresentem semelhança em sua descrição. Assim, preencha o referido campo com a sequência que se deseja apresentar os produtos. Tem-se abaixo um exemplo desta funcionalidade:

| **Produto** | | | |
| --- | --- | --- | --- |
| **Código** | **Descrição** | **Compl.   Descrição** | **Ordem   Medida** |
| 41408 | Abraçadeira de nylon foxlux PT | 280X 3,5 | 1 |
| 41409 | Abraçadeira de nylon foxlux PT | 200 x 4,8 | 2 |
| 41411 | Abraçadeira de nylon foxlux PT | 280 x 4,8 | 3 |
| 43223 | Abraçadeira de nylon foxlux Tigre | 3/4 | 1 |
| 43743 | Abraçadeira de nylon foxlux Tigre | 1/2 | 2 |
| 43224 | Abraçadeira de nylon foxlux Tigre | 1 | 3 |

Existem quatro opções de escolha para se definir o **"Tipo de contagem"** do produto, sendo elas:

- **Considerar configuração:** através desta opção, o sistema acatará a configuração efetuada na tela [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral), campo **"Tipo de contagem"**.
- **Contagem única por produto:** será apresentado na tela de Conferência o campo **"Quantidade"**, para que seja possível informar a quantidade que está sendo conferida.
- **Contagem cumulativa com quantidade:** caso esta opção esteja selecionada, o sistema deixará habilitado o campo Quantidade no painel de conferência (aberto através da Fila de Conferência). Ao fazer uma conferência de um pedido ou nota que utilize essa opção e caso já exista um produto igual já conferido o sistema apenas irá somar as quantidades; por padrão é sugerida a quantidade 1 (um).
- **Contagem cumulativa:** por esta opção, apenas informe o **"Código de Barras"** e o sistema considerará a quantidade como 1. Tem-se como exemplo, os caixas de supermercado que a cada bipe conta-se 1 produto.

A marcação **"Comercialização Agrícola"** quando acionada, indicará que o produto será comercializado pelo segmento agrícola.

Na separação dos produtos serão empregadas etiquetas para identificação e correta alocação dos mesmos. Dessa forma, indique no campo **"Modelo de etiqueta para separação"** os modelos das referidas etiquetas.

O produto contendo no campo **"Imprime etiqueta para separação"** a opção **"Sim (Por unidade)"**, irá imprimir uma etiqueta para cada unidade daquele produto no pedido. Caso indique a opção **"Sim (Por Produto)"**, irá imprimir uma etiqueta por produto. Além disso, quando não houver a impressão de etiquetas será indicada a opção **"Não"**.

As informações pertinentes ao campo **"Utiliza endereço flutuante"** podem ser acessadas no link [Armazenando Produtos Recebidos em Endereço Flutuante](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112233-Armazenando-Produtos-Recebidos-em-Endere%C3%A7o-Flutuante).

Quando acionada a marcação **"Comercialização Agrícola?"**, está indicando que o produto é decorrente da produção/comercialização rural.

A marcação **"Realiza controle por medição"** somente estará visível quando o parâmetro **"Usa faturamento de contrato de locação de bens? - FATCONTLOCBEM"** estiver ativado. O seu acionamento determina se o produto irá fazer parte ou não do controle de medição.

Ao efetuar a marcação **"Desconsiderar nos result. venda consultiva"**, fará com que o produto selecionado não seja considerado nos resultados apresentados na tela [Dashboard de resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604794-Dashboard-de-Resultados).

O campo **"Local padrão"** faz parte da configuração acerca do controle de estoque por local. Maiores detalhes podem ser acessados no link [Sugestão de Local por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111993-Sugest%C3%A3o-de-Local-por-Empresa).

Os campos **"Utiliza data de Fabricação"** e **"Utiliza data de Validade"** estão relacionados ao controle de estoque de produtos; posto isto, se aplicam à produtos que utilizam controle adicional por número de lote e/ou data de validade (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional)[)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional).

**Observação:** para que os produtos sejam controlados por data de fabricação e/ou data de validade, habilite os parâmetros **"Usar data de Fabricação junto com Lote? - LOTEDTFAB"**, **"Usar data de validade junto com Lote? - LOTEDTVAL"** e **"Informações adicionais para Lotes? - LOTEINFO"**. Assim, o sistema procederá com as devidas validações.

**Nota:** quando o parâmetro **"Usar data val. fab. junto com Lote, por produto? - LOTEDTVALFABPRO"** estiver ligado, o sistema exigirá o acionamento das marcações Utiliza data de Fabricação e Utiliza data de Validade presentes nessa aba. Se estiver desligado, essa validação ocorrerá exclusivamente de acordo ao parâmetro LOTEDTVAL.

Informe no campo **"Parceiro Consignante"**, o parceiro proprietário do produto para recebimento em consignação. Sendo que, o seu preenchimento é obrigatório para o recebimento do produto em consignação.

A marcação **"Apresenta em fórmulas de composição"** refere-se às rotinas de Produção, pois é possível cadastrar um produto como Matéria-Prima de uma Fórmula de Composição, e definir através deste campo se a matéria-prima deve ou não aparecer na pesquisa de Variação do Produto, isso porque nessa visualização não é necessário, por exemplo, visualizar as tarifas de composição.

Outro exemplo é que, se a Fórmula de Composição do produto possuir o gasto de Energia Elétrica não será interessante que o vendedor visualize isso na hora de vender o produto.

**Nota:** ao duplicar um produto, existe a opção de configurar o sistema para que a Fórmula de Composição do produto seja ou não copiada para o novo produto que será gerado; esta definição é feita através do parâmetro **"Copiar item de composição do produto? - COPITEMCOMPPRO"** que, por padrão é apresentado ativado, ou seja, na duplicação, a Fórmula de Composição do produto é passada de um produto ao outro; para que este fato não ocorra, desative o referido parâmetro.

O campo **"Registro no M.A.P.A"** se refere ao código do registro do produto junto ao Ministério da Agricultura, Pecuária e Abastecimento (utilizado para fertilizantes, inoculantes, corretivos). Este campo deve ser preenchido se a empresa possuir algum controle ou alguma legislação que exija a apresentação do código na NF-e ou afins.

O campo **"Conversão de Volume"** será utilizado no faturamento do pedido para gerar a informação da quantidade no Relatório de Volumes. Tem-se abaixo um exemplo:

Produto na nota com quantidade = 10;

Conversão de volume = 2;

Será impresso no relatório **(10/2) = 5** no campo Quantidade.

**Observação:** o campo Conversão de Volume substituirá o campo **"Agrupamento mínimo"**, que será utilizado para geração do Relatório de Volumes.

Além disso, no campo Conversão de Volume informe o valor a ser utilizado para o cálculo da quantidade de etiquetas para o produto; em sintonia com a configuração realizada nos campos **"Impressão de etiqueta de volumes"** (definido com a alternativa Ao colocar o produto na doca) e **"Imprime etiquetas de separação por OC"** (assinalado), tem-se a impressão de etiquetas ao final da separação por produto; estes dois últimos campos citados, estão presentes nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms).

Este campo, no processo de Impressão de etiquetas, funciona da seguinte forma: imagine a quantidade solicitada no pedido de 10 unidades para um produto; informou-se a quantidade 2 na Conversão de Volume para este item; deste modo, será realizada a divisão de 10 por 2, resultando na quantidade 5, ou seja, ao invés de serem impressas 10 etiquetas (quantidade de itens do pedido) serão impressas 5 etiquetas, agrupando-as de 2 a 2.

Quando habilitada a marcação **"Excluir do processo de conferência"**, o item do registro não irá participar da conferência.

Acione a marcação **"Imprime etiqueta de volumes na conferência"** para os produtos que necessitam possuir a impressão de etiquetas de volumes na [Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia). Caso seja necessário que algum produto não tenha impressão de etiquetas, desative essa marcação e trate-a no modelo de relatório das etiquetas.

A marcação **"Informa % Pureza e % Germinação"** é utilizada em integração com o MGE Certificação de Sementes.

No campo **"Observação"** pode-se inserir qualquer informação relevante do produto cadastrado, mas evite caracteres especiais como, por exemplo: **-**, **:**, **ç**, **^** e/ou espaços excessivos.

A marcação **"Permite comprar este produto?"** tem como funcionalidade bloquear ou não a compra de um determinado produto que esteja no estoque para venda e que não será mais comprado pela empresa. Quando desativada, no lançamento de um pedido/nota de compra, é barrada a confirmação do item e posteriormente exibida a seguinte mensagem:

**"O produto XXX não está permitido para compra."**

**Importante:** associado à esta marcação, tem-se o parâmetro **"Desconsiderar proibição de compra do produto? - DESCONSMARCPROD"**; nele informe as TOP's (separadas por vírgula, caso exista mais de uma) que, ao serem utilizadas no lançamento de um pedido/nota de compra, irão desconsiderar a validação de Permite comprar este produto? (quando desativada) para os produtos adquiridos. 

Ao acionar a marcação **"Solicita Compra?"**, estará informando que o produto faz parte do processo de Solicitação de Compra. Para isso, no cadastro de [Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalida%C3%A7%C3%B5es), as marcações **"Faturar Produtos com Estoque na Confirmação?"** e **"Gera Solicitação de Compra na Confirmação?"** devem estar acionadas;

O campo **"Tem Rastro do Lote"** faz parte do processo de [Rastreabilidade do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#rastreabilidadedoproduto).

Em **"Tipo de Utilização"**, será possível selecionar uma das seguintes opções:

- 1 - Telefonia;
- 2 - Comunicação de dados;
- 3 - TV por Assinatura;
- 4 - Provimento de acesso à Internet;
- 5 - Multimídia;
- 6 - Outros.

#### Seção Identificadores da Conferência

Nesta seção são apresentados os campos **"Qtd. Identificadores"**, onde será preciso informar a quantidade de identificadores exigidos pelo produto, e o campo **"Tipo Identificador"**, determinando qual o identificador a ser considerado para o produto em questão; este último campo pode ser definido dentre as seguintes opções:

- Número Serial;
- IMEI.

Ambos os campos, fazem parte do processo [Integração da balança no Processo de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111913-Integra%C3%A7%C3%A3o-da-balan%C3%A7a-no-Processo-de-Confer%C3%AAncia).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) 

#### Seção NFCom

Preencha o campo **“Cód. Item NFCom”**,  conforme o produto ou serviço configurado.

![Imagem 11: Para saber mais, acesse também o artigo: Procedimentos e configurações para a emissão da NFCom (Nota Fiscal Fatura de…](https://ajuda.sankhya.com.br/hc/article_attachments/16089265951767) Para saber mais, acesse também o artigo: [Procedimentos e configurações para a emissão da NFCom (Nota Fiscal Fatura de Serviços de Comunicação Eletrônica)](https://ajuda.sankhya.com.br/hc/pt-br/articles/29711263175063-Procedimentos-e-configura%C3%A7%C3%B5es-para-a-emiss%C3%A3o-da-NFCom-Nota-Fiscal-Fatura-de-Servi%C3%A7os-de-Comunica%C3%A7%C3%A3o-Eletr%C3%B4nica).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Medicamentos

Esta aba estará disponível para configuração quando o parâmetro **"Habilitar Aba de Medicamentos no Cad Produto? - MEDICAMENTOS"** estiver habilitado. Nela são realizados os cadastros dos produtos identificados como medicamentos, sendo que estes cadastros são necessários para a gestão comercial e fiscal dos mesmos.

Essa aba possui as seguintes seções:

| [Seção Termolábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oTermol%C3%A1bil) | [Seção Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oClassifica%C3%A7%C3%A3o) |
| --- | --- |
| [Seção Categoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oCategoria) | [Seção Classe terapêutica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oClasseterap%C3%AAutica) |

---

![Imagem 12: Seção Classe terapêutica](https://ajuda.sankhya.com.br/hc/article_attachments/4402109948695)

A marcação **"Oneroso"** indicará que o medicamento em questão possui um valor elevado de comercialização.

Por meio do campo **"Cód. Fabricante"** é possível apontar a empresa responsável pela produção do medicamento.

Os medicamentos sujeitos a um controle especial, serão apontados pela marcação **"Controlado"**.

Através da marcação **"Identificação de Cosmecêutico"**, determine que este medicamento é indicado para o tratamento e a profilaxia de doenças superficiais ou sistêmicas.

A marcação **"Identificação de Correlato"** estabelece que o produto está relacionado ao ramo de medicamentos, entre os quais tem-se os aparelhos de medição de temperatura corporal, termômetros, medidores de glicose e pressão arterial, entre outros.

No campo **"Princ. Ativo Medicamento"** será descrito o princípio ativo do medicamento. Sendo que, estas informações devem estar previamente cadastradas na tela [Princípio ativo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112933-Princ%C3%ADpio-ativo).

Caso o medicamento esteja em falta no estoque, a marcação **"Produto em falta"** deverá ser acionada.

Efetue a marcação **"Referência no Mercado de Medicamento"** quando se tratar de um produto de marca que possui referência no mercado, ou seja, que não é genérico ou similar.

A marcação **"Identificação de OTC"** deve ser acionada para os medicamentos que podem ser comercializados sem receita médica.

O campo **"Identificação de Portaria"** comportará a identificação da norma reguladora do medicamento.

Quando o produto é configurado como Inativo, é necessário informar o motivo pelo qual o mesmo está sendo desativado. No campo **"Status do produto"** aponte a justificativa para o fato em questão, dentre as seguintes opções:

- Não classificado;
- Retirado do Mercado;
- Descontinuado;
- Não Faz Mais Parte do Mix.

O código do registro que identifica que o medicamento está regularizado junto à ANVISA - Agência Nacional de Vigilância Sanitária, será apontado por meio do campo **"Cód. ANVISA"**.

O campo **"Motivo Isenção Anvisa"** permite discriminar as informações adicionais referentes ao produto que corresponde a um medicamento, conforme detalhes da ANVISA.

O campo **"Indicador de Tipo de Referência da BC do ICMS ST"** apenas será apresentado se o parâmetro **"Habilitar Aba de Medicamentos no Cad Produto? - MEDICAMENTOS"** estiver ligado. Ele é destinado exclusivamente para a geração do campo 6 - IND\_MED do [Registro C173](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI-#registroc173) do [EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI-), não tendo impacto em outro registro ou cálculos relacionados à operações com medicamentos.
Nesse campo tem-se as seguintes opções: 

- 0 - Base de cálculo referente ao preço tabelado ou preço máximo sugerido;
- 1 - Base cálculo - Margem de valor agregado;
- 2 - Base de cálculo referente à Lista Negativa;
- 3 - Base de cálculo referente à Lista Positiva;
- 4 - Base de cálculo referente à Lista Neutra.

**Observação:** mesmo se o campo acima estiver com alguma opção configurada e o parâmetro MEDICAMENTOS estiver desligado, o sistema manterá essa opção configurada na tabela do banco de dados, porém não irá apresentar o campo na tela e, ao gerar o [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI), no campo 6 - IND\_MED do Registro C173 será levado o código 0 - Base de cálculo referente ao preço tabelado ou preço máximo sugerido.

#### Seção Termolábil

Esta seção é designada para os medicamentos sensíveis à temperatura, ou seja, que necessitam ser armazenados de acordo com a faixa de temperatura informada pela indústria farmacêutica.

Ao selecionar a marcação **"Termolábil"**, estará indicando que o medicamento se enquadra nas condições estabelecidas por esta seção.

Os campos **"Temperatura Mínima em ºC"** e **"Temperatura Máxima em ºC"** são responsáveis por estabelecer em graus Celsius, quais serão os valores limites da temperatura ambiente do local de armazenamento deste medicamento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedicamentos)

#### Seção Classificação

Nesta seção, os campos **"Classificação"** e **"SubClassificação"** têm a função de apontar o grau de toxidade do medicamento e a necessidade de receitas especiais para o seu controle. Sendo que, estas classificações devem estar previamente cadastradas na tela [Classificação/Sub-Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597414-Classifica%C3%A7%C3%A3o-Sub-Classifica%C3%A7%C3%A3o).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedicamentos)

#### Seção Categoria

O medicamento pode ser identificado como um produto que possui Marca, um produto Genérico ou um produto Similar. Assim, indique nesta seção a **"Categoria"** e **"SubCategoria"** de cada medicamento. Uma vez que, primeiramente, será necessário cadastrar cada opção na tela [Categoria/Sub-Categoria](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602234-Categoria-Sub-Categoria).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedicamentos)

#### Seção Classe terapêutica

Cada medicamento é prescrito ao paciente de acordo com sua finalidade terapêutica, ou seja, aqui será assinalada de acordo com uma classe e subclasse a função de cada medicamento. As classes em questão necessitam estar previamente configuradas na tela [Classe terapêutica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597674-Classe-terap%C3%AAutica).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedicamentos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Venda

![Imagem 13: Aba Venda](https://ajuda.sankhya.com.br/hc/article_attachments/7444733234071)

O acionamento da marcação **"Promoção"**, define se o produto está ou não em promoção (suspende a validação de desconto máximo).

Através do campo **"% Desconto Máximo"** é apontado o percentual máximo de desconto permitido para o produto, no ato de sua venda.

Quando o campo % Desconto máximo estiver preenchido, ao efetuar uma venda, caso informe um percentual de desconto maior do que o cadastrado no campo, o comportamento dependerá do parâmetro **"Valida Desconto Máximo - VALDESCMAX"**, que pode ser definido dentre as seguintes opções:

- **Não Valida:** o sistema não fará a validação, permitindo lançar a nota de venda com um **"% Desconto"** maior do que o % Desconto máximo cadastrado na aba [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abavenda).
- **Valida e Aceita:** o sistema validará, e se o % Desconto informado for maior do que o % Desconto máximo o sistema gerará um alerta para o usuário, porém permitirá lançar a nota sem liberação de limites.
- **Valida e Não Aceita:** o sistema validará, e se o % Desconto informada for maior do que o % Desconto máximo o sistema gerará **"Liberação de Limites"**, não interessando se está em promoção ou não.
- **Valida e Não Aceita (Exceto Prod. Promoção):** o sistema validará, e se o % Desconto informada for maior do que o % Desconto máximo, será verificado se o serviço está em promoção; se estiver, aceitará lançar a nota sem liberação de limites, se não estiver em Promoção gerará liberação de limites.
- **Valida e Não Aceita (Exceto Prod. Promoção):** o sistema validará, e se o **% Desconto** informada for maior do que o **% Desconto máximo**, será verificado se o serviço está em promoção; se estiver, aceitará lançar a nota sem liberação de limites, se não estiver em Promoção gerará liberação de limites.
  Nesse cenário, a validação poderá ocorrer também no cabeçalho da nota, por meio do **Evento 2 – Desconto Produto**. O sistema calcula o valor máximo de desconto permitido para o pedido, considerando a soma do desconto máximo permitido de cada item:

  - Para produtos em promoção, o valor máximo de desconto considerado será o valor unitário calculado do item, podendo chegar até 100% do valor do produto;

  - Para produtos que não estão em promoção, o cálculo respeita o percentual informado no campo **% Desconto Máximo**, multiplicado pelo valor total do item (considerando a quantidade).

  O sistema então realiza a seguinte validação no cabeçalho:

  **Soma do desconto máximo permitido de todos os itens** vs **Valor total de desconto informado no cabeçalho**

  Se o desconto informado no cabeçalho ultrapassar a soma do limite calculado para os itens, será acionado o **Evento 2**, exigindo liberação de limites.

> **Importante:** ao alterar a quantidade ou o valor total de um item que não esteja em promoção, o valor máximo de desconto permitido para o pedido também será alterado, pois o cálculo considera o total do item.

- **Valida e Não Aceita (Somente na Confirmação):** se definir o parâmetro com esta opção, será feita a validação do % Desconto máximo somente no momento da confirmação. Além disso, o sistema trabalha apenas com evento [2 - Desconto Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#2-descontoproduto); esse evento valida se a médias dos descontos excedem a médias dos descontos máximos.

Para as quatro primeiras opções citadas do parâmetro VALDESCMAX, o sistema trabalha com evento [25 - Desconto por item na nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#25-descontoporitemdanota); esse evento valida se o desconto do item excedeu o desconto máximo daquele produto, sem realizar médias, a validação é por item.

> **Importante:** caso exista além do percentual máximo de desconto, a configuração de um [Desconto Promocional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais) que envolva o produto em questão, o sistema realiza a seguinte análise:

- Se o lançamento for realizado entre a **"Data Inicial"** e a **"Data Final"** do Desconto promocional, será considerado este percentual;
- Caso o lançamento esteja fora do intervalo da Data Inicial e a Data Final do Desconto Promocional, o sistema considera o percentual máximo de desconto cadastrado para o produto.

**Observação:** em nenhuma das hipóteses será realizada a soma destes percentuais.

Ainda sobre o campo % Desconto Máximo, caso ele esteja **"vazio"** ou com **"0"** (zero) informado, significa que o produto não pode ter nenhum percentual de desconto informado; caso contrário, será solicitada a liberação para o evento 25 - Desconto por item na nota. Para estas situações, tem-se a seguinte regra:

Se o parâmetro VALDESCMAX estiver definido como Valida e Não Aceita e o produto estiver cadastrado com o campo % Desconto Máximo igual a "0" ou "vazio" o comportamento será:

- Existindo desconto promocional cadastrado e o valor de venda seja o valor da promoção, não será solicitada liberação de limites para o evento 25 - Desconto por item da nota;
- Se houver desconto promocional cadastrado e o valor de venda seja menor que o valor da promoção, será solicitada liberação de limites para o evento 25 - Desconto por item da nota;
- Caso não exista desconto promocional cadastrado e o valor de venda seja menor que o preço de tabela, será solicitada liberação de limites para o evento 25 - Desconto por item da nota.

Portanto, caso queira que o evento 25 não seja solicitado para o produto, é necessário informar **"100%"** no campo % Desconto Máximo e, no Cadastro de Produtos, aba Venda, a marcação **"Promoção"** não esteja acionada para o produto.

No campo **"Grupo Desconto"**, efetue o agrupamento de diversos produtos em um mesmo grupo de desconto; grupo este, que será utilizado na tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais).

**Nota:** ao trabalhar com Grupo de Desconto, há no sistema um recurso complementar a esta rotina, que permitirá nesta tela a inserção mais rápida e dinâmica dos agrupamentos de descontos nos produtos desejados; no [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela) tem-se a funcionalidade **"Definir grupo de desconto para produtos Filtrados"**. Antes de utilizar esta opção, crie um filtro selecionando os produtos que farão parte do mesmo grupo de desconto; ao acioná-la, será aberto o pop-up **"Alteração do Grupo Desconto"** onde é possível selecionar o Grupo Desconto ao qual os produtos filtrados serão inseridos; clicando-se em Alterar, exibe-se uma mensagem de confirmação do procedimento, que sendo aceita, o novo Grupo de Desconto é incluído nos produtos inicialmente filtrados.

Quando a marcação **"Calcular comissão"** estiver ligada e os campos **"% Comissão vendedor"** e **"% Comissão gerente"** forem preenchidos, o cálculo de comissão será habilitado. Isso significa que o sistema calculará o valor da comissão para o vendedor e o gerente com base nas porcentagens definidas para cada um, de acordo com o produto cadastrado. Esta é uma das formas de calcular a comissão para vendedores.

É importante destacar que a marcação Calcular comissão não é um fator que, por si só, determina se a comissão será calculada ou não. No entanto, ele deve ser considerado na fórmula de cálculo da comissão. Ou seja, se essa marcação estiver ligada, o cálculo será feito conforme as porcentagens informadas nos campos % Comissão vendedor e % Comissão gerente. Caso contrário, o valor da comissão será zero, pois a fórmula deve levar essa marcação em conta ao determinar o valor final.

Existe a possibilidade de informar a moeda a ser utilizada na venda do produto (Real, Dólar, Libra). Esta funcionalidade é empregada pela campo **"Moeda p/ preço"**, por exemplo, se o produto estiver cadastrado em dólar, no momento da venda, o sistema buscará a cotação do dia para o dólar e fará a conversão para o real.

O campo **"Digitação na nota"** permite configurar quais informações do produto serão aceitas, no ato da digitação do mesmo no lançamento do pedido/nota. Tem-se as seguintes opções:

- **Quantidade**: apenas a quantidade poderá ser digitada;
- **Valor Unitário**: será permitido que seja digitado apenas o preço do produto;
- **Valor Total**: esta opção indica que somente o valor total do item poderá ser digitado. Por exemplo, se foram vendidos dois sabonetes ao preço de R$ 1,00 cada, o total do item será R$ 2,00;
- **Quantidade e Valor Unitário**: poderá utilizar a quantidade ou o preço do produto;
- **Quantidade e Valor Total**: tem-se a aplicação da quantidade, bem como, do valor total do item.

> **Observação:** se configurado para digitar somente o campo quantidade, o campo valor unitário não será bloqueado caso esteja lançando uma compra, uma transferência ou uma nota de complemento, ou se for uma devolução e o parâmetro **"Permitir informar valor na devolução de compra? - PERMITEVLRDEV"** estiver ligado e houver uma nota de origem.

Através do campo **"Múltiplo p/ Preço"**, será executado o arredondamento do valor na visualização do preço do produto. Abaixo um exemplo:

Ao informar no referido campo o valor de 0,05 e o valor de venda do produto é R$ 2,93, o sistema arredondará este valor para R$ 2,95. Se o valor de venda do produto for R$ 2,92, o sistema arredondará este valor para R$ 2,90.

**Observação:** a funcionalidade do campo Múltiplo p/ Preço não é aplicada nas Centrais; servindo apenas para visualização do preço na tabela "0", as demais tabelas não serão afetadas.

Ao acionar a marcação **"Bloquear venda fracionada?"**, a venda de quantidades fracionadas será bloqueada.

As informações inseridas nos campos **"Natureza"**, **"Projeto"** e **"Centro de Resultado"** servem para apoiar o rateio por produto informado na TOP, ou seja, na hora de ratear o produto, eles servem como apoio para o campo **"Ratear automaticamente por produto?"**, localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), do cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

**Nota:** para utilizar o rateio automático é necessário cadastrar a Natureza, o Centro de Resultado e o Projeto, para os quais deseja-se ratear os valores nas movimentações de entrada, saída e devolução, efetuadas na empresa.

O campo **"Extensão de garantia"** é habilitado pelo parâmetro **"Tem Extensão de Garantias? - TEMEXTGAR"**. Através deste campo, é possível vincular uma garantia ao produto. Assim, quando este produto for inserido na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), se houver apenas um plano para a faixa de preços da mercadoria, o serviço vinculado (garantia) será incluído automaticamente na aba Serviços. Se houver mais de um plano para a faixa de preços da mercadoria, o sistema solicitará a escolha do plano de garantia, incluindo-o na aba de Serviços, após a confirmação. Estas informações fazem parte do processo [Extensões de Garantia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596314-Extens%C3%B5es-de-Garantia).

Nos campos **"Data da Substituição do Produto"** e **"Código do Produto Substituto"**, informe o período ao qual ocorrerá a substituição e o código do produto que irá substituir o produto que está selecionado. Sendo que, ambos os campos são apresentados na tela com a ativação do parâmetro **"Permite cadastro de produtos substitutos? - PERCADPRODSUBST"**.

Ao realizar o preenchimento destes dois campos, ao visualizar o produto em questão na tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos), o produto substituto será exibido com uma faixa na cor **azul**, como mostra a imagem abaixo:

![Imagem 14: Ao realizar o preenchimento destes dois campos, ao visualizar o produto em questão na tela Consulta de Produtos , o…](https://ajuda.sankhya.com.br/hc/article_attachments/4402116453655)

**Importante:** caso o parâmetro **"Permite cadastro de produtos substitutos? - PERCADPRODSUBST"** esteja ativado e o parâmetro **"Tipo de direção para considerar na visualização de Produtos alternativos - TIPDIRPROALT"** esteja definido como Bidirecional, no Cadastro de Produtos, os produtos que forem inseridos como Substitutos ou Alternativos não poderão ser inversamente cadastrados no produto principal. Suponha a seguinte situação:

**1º Produto substituto:**

- No cadastro do produto 10, o produto 20 está como substituto;
- No cadastro do produto 20, o produto 10 está como substituto.

**2º Produto Alternativo:**

- No cadastro do produto 10, o produto 20 está como alternativo;
- No cadastro do produto 20, o produto 10 está como alternativo.

Nestes casos, ao verificar um destes produtos por meio da tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos), na aba Produtos Alternativos será exibido o mesmo item mais de uma vez, o que é um equívoco neste tipo de análise.

A marcação **"Aceitar venda fora do kit"** quando acionada, no lançamento de um pedido ou uma nota de venda que contenha um produto que seja componente de outro e o mesmo esteja sendo vendido separadamente, o sistema permitirá o lançamento.

Vale ressaltar que, para efetuar vendas de produtos fora do kit, o parâmetro **"Agrupar prod.repetido em qualquer faturamento? - AGRUPFATSEMP"** deve estar desligado. Lembrando que, esse parâmetro funcionará como um 'espelho' da nota de origem nas devoluções.

Exemplo:

Se na data do lançamento da nota de origem, o parâmetro estiver ligado, os itens serão agrupados e, na devolução também ficará agrupado. Todavia, se estiver desligado no lançamento da nota de origem, os itens não ficarão agrupados na devolução, mesmo se nesse momento ele estiver ligado.

Caso a marcação Aceitar venda fora do kit esteja desabilitada, ao realizar este procedimento o sistema irá verificar se a TOP utilizada neste lançamento está relacionada no parâmetro **"Tops para venda individual de componentes - TOPVENCOMPINDIV"**. Se sim, a venda separada do produto será efetuada. Se não estiver acionada a marcação e nem a TOP relacionada, esta venda não será permitida e a seguinte mensagem será apresentada:

**"Componente não pode ser vendido separadamente."**

Nesse processo, também poderá ser realizada a venda de uma série avariada, sendo preenchido o campo % Desconto (conforme configuração do mesmo na tela de [Registro de avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333-Registro-de-Avarias)). Se o produto utilizar local, o sistema irá carregar o local correto e irá bloquear o campo **"Local origem"** na nota. Lembrando que, os produtos avariados não respeitam a marcação em questão e podem ser vendidos separadamente, independentemente da configuração do produto ou do parâmetro.

As informações abordadas englobam o [Suporte a Venda de Kits de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos).

#### Seção Integrar EConect

Caso habilite a marcação **"Integração Econect"** estará definindo que o produto realizará integração com o EConect.

No campo **"Máx. Multiplicador"**, informe a quantidade máxima que o produto selecionado pode ser vendido.

Com a marcação **"Integrar com EConect"** realizada, alguns campos no sistema passam a ser de preenchimento obrigatório, sendo eles:

(1)** Aba Geral**

- Grupo;
- Referência (na integração não serão aceitos Códigos de Barras repetidos);
- Origem do produto;
- Usado como (produtos utilizados como **"Matéria-Prima"** e **"Revenda (por Fórmula)** não podem ser utilizados na integração).

(1)** Aba Impostos**

- Alíquota ICMS do Econect;
- NCM;
- % Carga Média Trib. Federal;
- % Carga Média Trib. Estadual.

Caso as abas [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacdigodebarras) ou [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas) contenham informações, o campo **"Código de Barras"** nelas presente, será também de preenchimento obrigatório.

O código de barras do produto pode também ser preenchido na aba Código de Barras como dito anteriormente, porém, a prioridade para importação será caso esteja preenchido no campo **"Referência"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral). O objetivo desta tabela é identificar o código de barras para venda do produto.

No caso da Unidade Principal, basta estar cadastrado com a marcação **"Integrar com Econect"** e possuir o **"Cód. Barras"** preenchido. Já, para as Unidades Alternativas do produto, para que o código de barras seja importado para o Econect, é necessário que a marcação **"Ativo"** esteja habilitada, o **"Cód. Barras"** esteja preenchido e a **"Quantidade"** seja maior que **"0"** (zero).

Para a montagem de Kit's (cesta básica), siga os seguintes passos:

![Imagem 15: Habilite o parâmetro "Informar Preço p/Componente no cad.Produto? - PRECOKIT" ;](https://ajuda.sankhya.com.br/hc/article_attachments/24595215060759) Habilite o parâmetro **"Informar Preço p/Componente no cad.Produto? - PRECOKIT"**;

![Imagem 16: Na alteração/inclusão dos Componentes, o produto Cesta Básica deverá estar com a marcação "Integrar com Econect"…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215069975) Na alteração/inclusão dos Componentes, o produto Cesta Básica deverá estar com a marcação **"Integrar com Econect"** efetivada;

![Imagem 17: Selecione os produtos que farão parte da Cesta Básica . Todos os produtos selecionados como componentes da Cesta Básica…](https://ajuda.sankhya.com.br/hc/article_attachments/25993945648663) Selecione os produtos que farão parte da Cesta Básica. Todos os produtos selecionados como componentes da Cesta Básica deverão estar marcados como **"Ativos"** e Integrar com Econect. Os produtos também deverão possuir tabela de preços cadastrada, onde a mesma também deverá estar marcada Integrar com Econect. Todos os produtos da Cesta deverão dispor das mesmas configurações de um produto normal que é integrado com SOCIN;

![Imagem 18: Caso o produto na Cesta tenha um preço diferenciado do preço de venda unitário, deve-se preencher os campos "Preço" ou…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215084311) Caso o produto na Cesta tenha um preço diferenciado do preço de venda unitário, deve-se preencher os campos **"Preço"** ou **"Desconto"** da aba [Componentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abacomponentes);

![Imagem 19: Após finalizar a montagem da Cesta, a mesma deverá ter a marcação Integrar com Econect realizada. Caso exista algum…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215090071) Após finalizar a montagem da Cesta, a mesma deverá ter a marcação Integrar com Econect realizada. Caso exista algum erro de configuração em algum componente da Cesta, o sistema emitirá uma mensagem de alerta, para que seja feita a devida correção para a importação do produto;

![Imagem 20: Para que a Cesta seja enviada para o PDV , a integração deverá ser executada.](https://ajuda.sankhya.com.br/hc/article_attachments/24959949531287) Para que a Cesta seja enviada para o PDV, a integração deverá ser executada.

É importante mencionar que, para produtos que utilizam balança (horti-fruti por exemplo), a marcação **"Utilizar Balança"** deverá ser habilitada na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), na sub-aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque).

Para produtos fracionáveis, a marcação **"Decimais para quantidade"** contida na aba Medidas e Estoque, na sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abamedidas), deverá ser maior que **"0"** (zero).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Impostos

Nesta aba, possuem as seguintes seções:

| [Seção FETHAB](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oFETHAB) |
| --- |
| [Seção Imobilizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oImobilizado) |
| [Seção Contabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oContabilidade) |
| [Seção Prodepe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oProdepe) |
| [Seção EFD Fiscal/Contribuições/Reinf/Sintegra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oEFDFiscal/Contribui%C3%A7%C3%B5es/Reinf/Sintegra) |
| [Seção ICMS/ST/FUNRURAL/INSS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oICMS/ST/FUNRURAL/INSS) |
| [Seção PIS/COFINS/CSLL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oPIS/COFINS/CSLL) |
| [Seção IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oIPI) |
| [Seção ADRCST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oADRCST) |
| [Seção FCI – Ficha de Conteúdo de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oFCIFichadeConte%C3%BAdodeImporta%C3%A7%C3%A3o) |

---

![Tela](https://ajuda.sankhya.com.br/hc/article_attachments/16006987314199)

As marcações **"Calcular FUST?"** e **"Calcular FUNTTEL?"** devem ser feitas para gerar as contribuições FUST e FUNTTEL para pagamento.

Informe no campo **"Número do Item (Portaria 384/01)"**, o código específico do produto para a geração do ROI, relatório de movimentações que deve ser gerado periodicamente, assim como o SINTEGRA.

O gênero ao qual o produto pertence será definido no campo **"Gênero"**, e é necessário executar previamente o cadastro dos gêneros na tela [Gênero de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110873-G%C3%AAnero-de-Produtos). Caso o código informado neste campo esteja divergente do que for informado no campo **"NCM"**, o sistema exibirá a seguinte mensagem:

**"ATENÇÃO: o campo GÊNERO da aba IMPOSTOS está diferente do CAPÍTULO informado no campo Cód. NCM da aba GERAL."**

Porém, se optar por não alterar o campo, o sistema permitirá que as informações sejam salvas.

O CNPJ pertencente ao fabricante da mercadoria será descriminado através do campo **"CNPJ do Fabricante da Mercadoria"**.

Para que a informação do produto seja enviado pela API, preencha o campo **"Considerar na integração impostos"**, conforme as seguintes opções:

- **Código de Barras:** este recurso normalmente é aplicado para revenda e será utilizado quando o produto for universal, isto é, para um produto que seja comum entre as empresas. Além disso, ao selecionar essa opção, na aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras) preencha o campo **"Unidade de Volume"**.
- **Código do Produto:** esta opção geralmente é aplicada para indústrias, e se refere ao código interno do sistema que será utilizado para vincular o produto a uma empresa especifica.

Caso não selecione nenhuma das opções acima e na aba Código de Barras conste algum cadastro, o sistema irá utilizar a opção Código de Barras, do contrário, a opção Código do Produto será aplicada.

#### Seção FETHAB

Nesta seção, realize as configurações para o Imposto [FETHAB - MT](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002985761).

Por meio do campo **"Alíquota FETHAB"**, determine a alíquota do FETHAB que será aplicada no cálculo.

**Nota:** para o cálculo do FETHAB, o sistema irá multiplicar o **"UPF x Alíquota FETHAB"** de forma a encontrar o valor do FETHAB por tonelada. Assim, observe o exemplo a seguir:

UPF = 146,44 Alíquota FETHAB = 21,15% (para o Produto Soja)

Valor FETHAB por ton. = (UPF) x (Alíquota FETHAB)

Valor FETHAB por ton. = 146.,44 x 21,15%

Valor FETHAB por ton. = 30,97

Considere que o valor encontrado de 30,97 será aplicado por tonelada de soja comercializada, ou seja, se houver 10 toneladas de soja o cálculo será 10 x 30,97 = 309,70.

Sendo que, caso ocorra comercialização do produto cuja unidade comercializada não seja tonelada haverá necessidade de conversão para a unidade adotada conforme a seguinte regra:

Valor FETHAB por ton = 30,97

Valor do FETHAB por kg = 30,97/1000 = 0,0310

Valor do FETHAB por saca de 60kg = 60 x 0,0310 = 1,86

Posteriormente o sistema irá considerar a quantidade do produto lançada na nota e multiplicar pelo valor do FETHAB por unidade (kg, SC ou Ton), assim achará o valor final do imposto FETHAB, uma vez que esse imposto deve ser calculado por item e por nota, pois o mesmo é retido pelo cliente.

Defina o campo **"Unidade Padrão p/ FETHAB"** conforme o produto, tem-se que este será utilizado como base para a conversão das alíquotas alternativas.

O percentual do FETHAB poderá variar de acordo com produto comercializado, desta forma será necessário seguir as regras determinadas pela legislação da UF competente.

Nos campos **"Resp. pelo Recolhimento em Operações Internas"**, **"Resp. pelo Recolhimento em Operações Interestaduais"** e **"Resp. pelo Recolhimento em Operações de Exportação"**, existem as três alternativas abaixo para cada um deles:

- **Vazio:** ao selecionar essa opção, em determinado produto, a contribuição de FETHAB não será calculada;
- **Remetente:** caso selecione essa opção, indicará que o responsável por recolher a contribuição será aquele que está enviando o produto, portanto, ao efetuar uma venda deste produto o FETHAB será calculado e destacado no DANFE, no campo Dados Adicionais dos produtos/serviços, e no campo Dados Adicionais da Nota haverá a informação de que o responsável pelo recolhimento é o Remetente;
- **Destinatário:** selecionando essa opção, ao emitir uma venda, o FETHAB não será calculado, no entanto, no campo Dados Adicionais da Nota haverá a informação de que a responsabilidade do recolhimento é do Adquirente.

**Observação:** suponha-se que, numa mesma nota seja incluído dois ou mais itens com diferentes responsáveis pelo recolhimento para esta operação, o cálculo do FETHAB será realizado apenas para o produto em que o Remetente é o responsável pelo recolhimento da contribuição e a mensagem automática no campo Dados Adicionais da Nota irá apontar o Remetente como contribuinte substituto.

Caso não sejam realizadas as configurações relacionadas ao FETHAB e seja selecionada a opção Vazio, Remetente ou Destinatário nos campos Resp. pelo Recolhimento em Operações Internas, Resp. pelo Recolhimento em Operações Interestaduais ou Resp. pelo Recolhimento em Operações de Exportação em determinado produto, quando realizar a emissão de uma venda desse item em qualquer operação o FETHAB não será calculado.

**Nota:** o cálculo do FETHAB será realizado somente para o produto no qual o responsável pelo recolhimento for o Remetente em determinada operação, por exemplo, se no produto, o Remetente estiver como Responsável pelo Recolhimento em operação Interna, e para as outras operações estiver selecionada a opção Vazio ou Destinatário, então o cálculo será realizado apenas em Operação Interna.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção Imobilizado

O CIAP - Crédito de ICMS sobre Ativo Imobilizado é representado pela marcação **"Atualizar CIAP"**, sendo que esta só pode ser acionada para os produtos do tipo Imobilizado e serve para controlar os produtos que dão direito ao crédito de ICMS.

Os campos **"Identificação do Imobilizado"** e **"Utilização do Imobilizado"** deverão ser preenchidos para tratativa do SPED PIS/COFINS. Para que as informações incluídas nestes campos sejam gravadas, o campo Usado como presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) deve estar preenchido com a opção Imobilizado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção Contabilidade

Nesta seção é possível selecionar até quatro contas contábeis, utilizando os campos **"Conta contábil 1"**, **"Conta contábil 2"**, **"Conta contábil 3"** e **"Conta contábil 4"**, este recurso tem a funcionalidade de indicar cada conta contábil para efeitos de contabilização.

Existe a possibilidade de criação de campos adicionais para determinar as contas contábeis, elas são criadas a partir da tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados), vinculando a tabela **"TGFPRO"** na tabela **"TCBPLA"** através da aba [Ligações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaligaes).

![Imagem 22: Para mais informações, acesse o tópico Contas Flexíveis na Contabilização do artigo TOP Contabilização .](https://ajuda.sankhya.com.br/hc/article_attachments/16089265951767) Para mais informações, acesse o tópico [Contas Flexíveis na Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#contasflexveisnacontabilizao) do artigo [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o#top). 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção Prodepe

Indique o Código da Apuração do Incentivo PRODEPE/FUNCRESCE através do campo **"Cód. Apur. Inc. PRODEPE/FUNCRESCE"**.

Utilize o campo **"Indicador Esp. Inc. PRODEPE/FUNCRESCE"** para registrar o Indicador Especial do Incentivo PRODEPE/FUNCRESCE.

**Observação:** caso o Produto encontre-se com o Indicador Esp. Inc. PRODEPE/FUNCRESCE sem nenhuma opção selecionada, não será gerado o Registro C177; encontrando-se com a opção **"Sem incentivo"** indicada, terá para o Registro C177 seu respectivo código inserido no campo **"Cód. do Produto Sem Incentivo"** (tela [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI), aba [Prodepe](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI#abaprodepe)). Ainda em relação ao Indicador Esp. Inc. PRODEPE/FUNCRESCE, caso a opção **"Com incentivo"** esteja selecionada, tem-se duas situações para o Registro C177:

- Operação não incentivada no item com incentivo;
- Operação incentivada no item com incentivo.

Desta forma, as duas situações acima dependerão da opção selecionada no campo **"Tipo de Operação PRODEPE"** da tela [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714-CFOP#abageral).

Quando o campo **"% MVA Ajustado"** estiver preenchido, os seus dados serão empregados no cálculo da ST (Substituição Tributária). Quando estiver igual a zero (0), o sistema continuará usando o percentual informado no campo **"Margem Lucro (MVA)"**, do cadastro de [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abasubstituiotributria).

Quando os campos % MVA Ajustado e Margem Lucro (MVA) estiverem preenchidos, o sistema interpretará como Substituição Tributária e irá realizar a conversão do CFOP no item da nota conforme informado na TOP e preencherá o ST no cadastro de Alíquota de ICMS, aba Substituição Tributária.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção EFD Fiscal/Contribuições/Reinf/Sintegra

O campo **"Código Natureza Rendimento"** buscará o código da natureza de rendimentos da tabela de cadastro natureza de rendimento - TGFNRR para gerar os eventos  do Bloco 4000 da [EFD REINF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) e seus detalhamentos.

Através da marcação **"Enquadrado no Reintegra/Prev."**, indique que o produto em questão será inserido na geração do [Bloco P](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es#geraodoblocop) no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es).

Se a marcação **"Produto constante no apêndice I do RCTE/GO"** for acionada e o produto estiver sendo movimentado em uma operação de entrada, onde a UF da empresa for "GO" e a UF do parceiro for igual a UF da empresa e o valor de ST não somar ao total da nota, não será gerado o Registro 53 - Substituição Tributária Sintegra para esta movimentação.

No campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** aponte a atividade a ser relacionada ao produto na geração do Bloco P no EFD - Contribuições. Esta atividade deverá estar previamente cadastrada na rotina [Cód. Atividades Produtos e Serviços p/ CPRB](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608314-C%C3%B3d-Atividades-Produtos-e-Servi%C3%A7os-p-CPRB).

Através do campo **"Conta Contábil para EFD"**, defina qual conta contábil será gerada no [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). É necessário realizar previamente o cadastro das contas a serem utilizadas através da rotina [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas).

**Nota:** para a geração do Registro F130, o sistema irá utilizar a conta contábil inserida nesse campo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção ICMS/ST/FUNRURAL/INSS

A marcação **"Calcular ICMS"** quando acionada, indicará que o Imposto sobre Circulação de Mercadorias e Serviços, de competência Estadual deve incidir sobre o produto.

Acione a marcação **"Calcular DIFAL?"** para as situações onde o produto em questão trabalha com cálculo do DIFAL; se desmarcada, o item não se enquadrará neste caso. É importante mencionar que na aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) (também presente no Cadastro de Produtos) tem-se esta mesma marcação, que permite singularizar o cálculo associando a empresa ao produto. Com a marcação Calcular DIFAL presente nestas duas abas, o sistema segue a seguinte prioridade:

- Calcular DIFAL, aba Impostos / Informações por empresa marcado - o sistema procede com o cálculo do DIFAL;
- Calcular DIFAL, aba Impostos / Informações por empresa desmarcado - o sistema verifica se a marcação Calcular DIFAL na aba Impostos está realizada, e caso afirmativo, prossegue com o cálculo do DIFAL;
- Calcular DIFAL, aba Impostos / Informações por empresa desmarcado e Calcular DIFAL, aba Impostos também desmarcado - o cálculo do DIFAL não irá ocorrer para o produto em questão.

Quando a marcação **"Considerar débito ICMS nas consultas gerenciais"** estiver acionada, ao gerar relatórios gerenciais o sistema irá considerar como débito o ICMS sobre o produto.

A marcação **"Tem INSS"** quando acionada, indicará a necessidade de calcular o INSS para o produto. Juntamente com a referida marcação, efetue o preenchimento do percentual do INSS e do percentual de Redução de Base do INSS utilizando os campos **"% INSS"** e **"% Red.Base INSS"**.

Caso o produto selecionado se enquadre em alguma alíquota em específico, informe-a no campo **"Alíquota Geral"**.

No campo **"Alíquota ICMS do Fast Service"** será indicada a alíquota de ICMS a ser usada quando o produto é vendido pelo Fast Service, pois cupom fiscal não se encaixa nas regras normais de tributação de nota fiscal comum.

O campo **"Alíquota interna de ICMS"** será utilizado para executar o cálculo efetivo de ICMS na NFe.

**Observação:** para a geração do Registro 0200, e assim, a geração do campo **"12 - ALIQ\_ICMS"** no SPED, sistema segue uma hierarquia. Observe:

![Imagem 23: Primeiramente, o Sankhya Om irá considerar o preenchimento do campo Alíquota Interna de ICMS na aba 0200 do EFD do…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215060759) Primeiramente, o **Sankhya Om** irá considerar o preenchimento do campo Alíquota Interna de ICMS na aba [0200 do EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#0200doEFD) do Cadastro de Produtos;

![Imagem 24: Caso essa informação esteja ausente, esta será verificada no campo Alíquota Interna de ICMS da aba Impostos /…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215069975) Caso essa informação esteja ausente, esta será verificada no campo Alíquota Interna de ICMS da aba Impostos / informações por Empresa;

![Imagem 25: Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da…](https://ajuda.sankhya.com.br/hc/article_attachments/25993945648663) Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) do Cadastro de Produtos;

![Imagem 26: Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo "Alíq. Interna…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215084311) Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo **"Alíq. Interna Destino"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral).

Assim como o campo anterior, se o produto possuir uma configuração de MVA padrão específica, o campo **"MVA Padrão"** será responsável pela indicação da mesma.

Na configuração das alíquotas de ICMS, caso seja necessário incluir o produto que será envolvido por esta alíquota em algum grupo específico, o campo **"Grupo de ICMS 2"** será utilizado para inserção deste produto em um determinado grupo. Assim, este campo será apresentado para escolha como exceção na estruturação das alíquotas de ICMS.

O campo **"Número do Item (Instrução Normativa 673/04)"** é utilizado e apresentado quando o parâmetro **"Gerar Crédito Presumido conforme IN nº 673 - IN673CREDPRES"** estiver ativo. A desativação deste parâmetro fará com que a descrição do campo retorne para Número do Item (Portaria 384/01).

O campo **"Nro. Item REA/ICMS"** é habilitado pelo parâmetro **"Tem Regime Especial de Apuração de ICMS’- TEMREAICMS"**, e será empregado na rotina de geração de livros fiscais no MGE Livros Fiscais.

A utilização do campo **"Tipo de Partilha/Anexo"** se dará para as empresas que utilizarem o regime de tributação Simples Nacional vinculado ao produto. Aponte aqui qual é o tipo de partilha que o produto em questão esta enquadrado. Deste modo, ao realizar o cálculo dos impostos o sistema irá seguir as regras de partilha as quais o produto está vinculado. É possível definir dentre as seguintes opções:

- Anexo I - Comércio;
- Anexo II -Indústria;
- Anexo III - Rec. de locação de bens/móveis e prest. de serv. não relac. no § 5° - C do art. 18 da Lei;
- Anexo IV - Rec. decorrentes da prest. de serv. relacionados no § 5° - C do art. 18 da Lei;
- Anexo V - Rec. decorrentes da prest. de serv. relacionados no § 5° - I do art. 18 da Lei;
- Serviços de Atividades Físicas, Computação, Adm. e Loc. de Imóveis de Terceiros, Outros;
- Serviços da Atividade Intelectual como Medicina, Consultorias, Engenharia, Outros.

No campo **"Código de Barras da Un. Trib. diferente do padrão GTIN"** deve ser informado o código de barras próprio ou de terceiros que seja diferente do padrão GTIN correspondente aquele da menor unidade comercializável identificado por código de barras.

No campo **"Código de Barras diferente do padrão GTIN"** informe o código de barras próprio ou de terceiros que seja diferente do padrão GTIN.

Havendo a necessidade de efetuar o cálculo do Funrural no lugar do INSS para o produto selecionado, a marcação **"Calcular FUNRURAL"** deverá ser acionada. Além disso, é necessário definir a alíquota e o percentual da redução de base através dos campos **"% Funrural"** e **"% Red.Base Funrural"**.

Caso seja necessário calcular este imposto na empresa, realize as seguintes configurações:

1. Habilite o parâmetro **"Calcular Funrural no lugar de INSS? - TEMFUNRURAL"**, que é responsável pela exibição dos campos Calcular FUNRURAL, % Funrural e % Red.Base Funrural.
2. Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), acione a marcação **"Tem FUNFURAL/INSS"**;
3. Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abapropriedades), a marcação **"Calcula FUNRURAL/INSS?"** deve ser acionada;
4. No [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal), efetue a marcação **"Calcula FUNRURAL/INSS"**.

O campo **"Grupo de ICMS"** é empregado no cadastro de exceções de alíquotas. Abaixo observe um exemplo:

O referido campo é preenchido com o número 1, no [Cadastro de Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS) poderá ser incluída uma exceção por grupo de produtos, onde o grupo é 1. Sobre todos os produtos nos quais o grupo de ICMS for 1, incidirá a alíquota cadastrada na exceção.

No campo **"Classificação Substituição Tributária"** é realizada a definição da classificação do produto sobre o tipo de cálculo de ST a ser executado.

As opções apresentadas no campo **"Tipo de substituição"** irão influenciar o cálculo do CFOP e do ICMS do produto da seguinte forma:

- **A = Substituição na Compra e Venda:** quando o produto é configurado com esta opção, significa que a existência de ST irá depender das configurações de alíquotas de ICMS, ou seja, depende das UF's de origem e de destino envolvidas. Esta opção é a mais habitualmente empregada, sendo acionada portanto, quando a abrangência da aplicação da ST não envolva todas as UF's para as quais a empresa vende, ou quando existe mais de uma empresa em UF's diferentes e a definição de ST na compra for diferente para cada uma delas.
- **P = Venda com Substituição Tributária (ST na Venda):** esta opção deve ser selecionada para produtos sujeitos à ST nas saídas da empresa. Por exemplo, nas indústrias para os seus produtos acabados, sujeitos à Substituição Tributária nas vendas.
- **C = Revenda com Substituição Tributária (ST na Compra):** esta opção informa que o produto possui ST na Compra e consequentemente nunca na venda. Deste modo, seleciona-se esta opção para produtos com abrangência da ST Nacional ou que alcance todos os estados para os quais a empresa vende ou pretende vender seus produtos. Quando esta opção estiver marcada, o sistema irá calcular o ICMS cobrado anteriormente por substituição nas saídas deste produto, não havendo o destaque do imposto, para qualquer que seja o destino da mercadoria. Outro ponto a se destacar, é que produtos que utilizem esta opção, devem conter um tratamento diferente na apuração de custos, pois pode-se garantir que o custo do produto possui o ICMS embutido, visto que na venda não haverá o débito de ICMS.
- **N = Não tem:** os produtos que não estão sujeitos à substituição, devem estar com esta opção selecionada. É importante salientar que mesmo quando existir a configuração de alíquotas de ICMS apontando que deverá haver o cálculo da ST, se o produto estiver com esta opção selecionada não haverá o cálculo da Substituição.

Ainda sobre a opção N = Não tem, a CST e a Alíquota são mantidas de acordo com a Regra de Alíquota de ICMS capturada, onde os valores de ST não serão informados.

**Observação:** para produtos com Tipo de Substituição diferente da opção Não tem será calculada a CFOP específica para produtos com ST.

**Nota:** quando o campo Classificação Substituição Tributária estiver configurado com a opção **"Pneumáticos, câmaras de ar e protetores de borracha"**, o sistema irá utilizar uma fórmula diferente para calcular a Base de substituição:

```
 Base Substituição = {[Vlr. Total * (1 - %Redução da base)] + IPI} * {1 + %MVA}
```

A fórmula usual empregada com as outras classificações é:

```
 Base Substituição = {[(Vlr. Total + IPI) * (1 - %Redução da base)] * (1 + %MVA)}
```

A seguir, confira o enquadramento (Cód. Enq. Legal IPI Entrada ou Saída) adequado para cada tipo de Código Sit. Trib. IPI de Entrada ou Código Sit. Trib. IPI de Saída:

| **Código Sit. Trib. IPI Entrada ou Saída** | **Cód. Enq. Legal IPI Entrada ou Saída** |
| --- | --- |
| Código Sit. Trib. IPI Entrada = 02  Cód. Sit. Trib. IPI Saída = 52 | Enquadramento de 301 a 399 |
| Código Sit. Trib. IPI Entrada = 04  Cód. Sit. Trib. IPI Saída = 54 | Enquadramento de 001 a 099 |
| Código Sit. Trib. IPI Entrada = 05  Cód. Sit. Trib. IPI Saída = 55 | Enquadramento de 101 a 199 |

Para mais informações relacionados à tabela de códigos de enquadramento legal de IPI, consulte a NT 2015.002 disponível no link: <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=mCnJajU4BKU=> 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção PIS/COFINS/CSLL

Caso a marcação **"Desconsiderar desconto no cálculo de PIS/COFINS"** esteja efetuada, ao realizar a confirmação de uma nota de compra, fará com que o desconto não seja deduzido da base de cálculo do imposto.

O campo **"Cód. Natureza (PIS/COFINS M410/M810)"** é preenchido com valores que irão compor o arquivo [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). Caso este campo esteja preenchido, porém o campo **"Cód. Natureza (PIS/COFINS M410/M810)"** da tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) (aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)) esteja vazio, o sistema utilizará a informação do campo desta tela para a geração dos Registros M410/M810.

NCM - NCM / SH - NOMENCLATURA COMUM DO MERCOSUL / SISTEMA HARMONIZADO DE DESIGNAÇÃO E CODIFICAÇÃO DE MERCADORIAS.

- As mercadorias comercializadas internacionalmente pelo país são classificadas, desde 1996, de acordo com a Nomenclatura Comum do MERCOSUL (NCM), que é também adotada por Argentina, Paraguai e Uruguai. Os códigos de classificação da NCM são formados por oito dígitos, sendo tal classificação baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias, ou simplesmente Sistema harmonizado (SH). A inclusão de dois dígitos, após os seis do código numérico do SH, tem como intuito obter melhor detalhamento das mercadorias e suas respectivas classificações, além de satisfazer aos interesses de todos os Estados membros do MERCOSUL.
- É importante que o importador faça a correta classificação dos produtos adquiridos, com a finalidade de evitar a aplicação de penalidades pelas autoridades aduaneiras, além de utilizar as vantagens tarifárias decorrentes dos acordos bilaterais e multilaterais que o Brasil mantém no âmbito de seu comércio internacional. É recomendável também, que o exportador, com o intuito de aprimorar a classificação da mercadoria que pretende exportar ao Brasil, informe ao cliente brasileiro a classificação que utiliza em seus negócios externos, visto que nem sempre a classificação da NCM/SH coincide com a codificação utilizada pelo exportador nas duas últimas posições numéricas (oito dígitos).
- As vantagens advindas da correta classificação traduzem-se essencialmente na redução do Imposto de Importação, ou até mesmo em sua isenção, de acordo com os acordos comerciais vigentes. Neste sentido, é necessário que o exportador conheça os benefícios tributários do seu produto em relação ao mercado brasileiro, a fim de ganhar competitividade frente aos concorrentes de outros países que eventualmente não sejam favorecidos pelos tratados comerciais que o Brasil mantém no seu comércio exterior.
- Essa vantagem tributária será efetivamente formalizada durante o processo do despacho aduaneiro, quando o importador deverá estar de posse do Certificado de Origem, para eventual apresentação às autoridades aduaneiras, documento esse emitido pela entidade autorizada no país do exportador, no qual devem constar os fundamentos legais do acordo comercial que está sendo aproveitado nessa operação. A falta de apresentação do certificado de origem ocasiona a perda dessas vantagens, implicando o pagamento pelo importador do Imposto de Importação com as alíquotas normais.
- Note que da classificação incorreta das mercadorias na NCM/SH decorrem, além do pagamento de eventuais diferenças de alíquota na classificação correta, multas a serem aplicadas sobre o importador brasileiro, cujo valor corresponde, no mínimo, a 1% do valor aduaneiro, dependendo do tipo de infração.

**Observação:** a informação de NCM no DANFE e no XML da Nota (na tag **<NCM>**), será o conteúdo informado neste campo. Se o mesmo se encontrar vazio, a informação de NCM será retirada do campo **"Código Fiscal (NPC, NBM)"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI#abageral), no cadastro de [Alíquotas de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI). Sendo que, a referida informação estará configurada no campo **"IPI"**, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos), Cadastro de Produtos.

Os campos **"Grupo PIS"**, **"Grupo COFINS"** e **"Grupo CSLL"** serão preenchidos com os seus respectivos grupos, estes grupos necessitam estar previamente cadastrados nas telas [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS), [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS) e [Alíquotas de CSLL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109933-Al%C3%ADquotas-de-CSLL).

![Imagem 27: Ao processar tributos na tela dos impostos retornados pela IMendes ( Integração Impostos ), serão criadas…](https://ajuda.sankhya.com.br/hc/article_attachments/27540392620439) Ao processar tributos na tela dos impostos retornados pela IMendes ([Integração Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos)), serão criadas automaticamente regras nas telas Alíquotas de PIS e Alíquotas COFINS. Aqui no Cadastro de Produtos, essas regras serão preenchidas automaticamente nos campos Grupo PIS e Grupo COFINS.

**Nota:** caso queira informar uma exceção de PIS/COFINS na emissão NF-e's de Parceiros, realize as configurações abaixo:

1. Nos campos Grupo PIS e Grupo COFINS pode-se inserir a exceção de PIS e COFINS na emissão de NF-e's de Parceiros;
2. Em seguida, configure-a no campo **"Grupo PIS/COFINS"** da aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) após ligar o parâmetro **"Utiliza Grupo PIS/COFINS do Parceiro para localizar Aliq. PisCofins - UTILGRUPPF"**;
3. Por fim, no campo **"Grupo"** das telas [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS) e [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS), configue a exceção requerida no formato **"ALIQPISCOFINS: número da exceção"**.

Nas regras de contabilização da empresa, que são configuradas na tela [TOP Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608174-TOP-Contabiliza%C3%A7%C3%A3o), existe a possibilidade de configurar, para que o sistema busque uma das contas do produto para contabilizar. Para tanto, é necessário informar no campo **"Conta Contábil"** a conta pertinente ao produto, e na TOP Contabilização indica-se no campo **"Tipo de Conta Contábil"** a opção **"Variável"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção IPI

Efetue as marcações **"Tem IPI na venda"** e **"Tem IPI na compra"** quando o IPI for incidir na venda e na compra do produto.

O IPI - Imposto sobre Produtos Industrializados de competência Federal é um imposto com valores de alíquotas diversas. Quando este imposto for incidir na venda do produto, no campo **"IPI"** será indicado o código referente ao IPI, que deverá estar previamente cadastrado na tela [Alíquotas de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112013-Al%C3%ADquotas-de-IPI).

**Nota:** ao processar tributos na tela dos impostos retornados pela IMendes ([Integração Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053043573-Integra%C3%A7%C3%A3o-Impostos)), o campo IPI será preenchido automaticamente e as marcações **"Tem IPI na Venda"** e **"Tem IPI na Compra"** habilitadas conforme as tributações retornadas. 

Configure os campos **"Cód. Sit. Trib. IPI Entrada"** e **"Cód. Sit. Trib. IPI Saída"** de acordo com a situação tributária de entrada e saída do produto e/ou da empresa.

Através da lupa do campo **"NCM"** será possível pesquisar o NCM na tabela TIPI e não poderá digitar um NCM que não exista nessa tabela, caso faça, o sistema irá informar que o NCM é inexistente. Destaca-se ainda que os NCM's a serem utilizados podem ser cadastrados na tela [Cadastro NCM](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411248045591).

**Observação:** ao informar algum NCM em que a data de vigência já tenha finalizado, será exibida uma mensagem alertando que o NCM está fora da vigência, não sendo possível salvar.

Os campos **"% Carga Média Trib. Nacional"**, **"% Carga Média Trib. Federal"**, **"% Carga Média Trib. Estadual"**, **"% Carga Média Trib. Importação"** presentes nesta aba e na aba [Impostos/Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) devem ser preenchidos com os respectivos percentuais médios de tributação, são informações utilizadas nas configurações pertinentes à [Lei da Transparência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600174-Lei-da-Transpar%C3%AAncia).

Informe no campo **"Código Especificador ST"**, o código responsável por especificar a Substituição Tributária referente ao produto em questão. Este campo é participante nas configurações relacionadas à [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado).

**Nota:** de acordo com o [Guia Prático EFD-ICMS/IPI-Versão 3.1.6](http://sped.rfb.gov.br/arquivo/show/7291), o valor do CEST deve conter apenas sete dígitos; quando houver menos dígitos, o **Sankhya Om** sempre adicionará zeros à esquerda.

A marcação **"Ressarcimento de ST (CAT - 17/99)"** é responsável pelo preenchimento dos relatórios de ressarcimento de ST no módulo de Livros Fiscais. Além disso, ela trabalha em conjunto com o campo **"Rastreamento de Estoques"** apresentado na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque).

Os campos **"EAN/GTIN Produto p/ NF-e"** e **"Cód. Produto p/ NF-e/NFC-e/CF-e"** irão armazenar como será o controle da numeração que será enviada para a Geração do EFD.

**Observações:**

- Para que o sistema grave as alterações realizadas no campo Cód. Produto p/ NF-e/NFC-e/CF-e, habilite o parâmetro **"Gerar registro 0205 para a Referência no EFD - EFDGER0205REF"**. Deste modo, se o referido campo tiver sido alterado da opção **"Código do Produto"** para **"Referência"**, ao realizar a geração do registro 0200 o sistema irá gerar o registro 0205 e não uma nova linha do registro 0200.
- Os documentos CF-e são de uso exclusivo do [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/sections/360009668474-Sankhya-Checkout).
- Ao realizar uma venda CF-e no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web), a tag **<cProd>** do XML da nota será impressa conforme a definição do campo Cód. Produto p/ NF-e/NFC-e/CF-e, sendo as opções **"Código do Produto"**, que se refere ao campo Código do Painel Principal dessa tela, ou a opção **"Referência"**, que corresponde à informação do campo **"Referência"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral). Porém, se a opção Referência for selecionada, e o campo correspondente a este estiver vazio, o sistema irá utilizar do campo Código.
- Em relação ao campo EAN/GTIN Produto p/ NF-e, quando as opções **"Código de Barras Estoque"** e **"Cód.Barras da Unid. Alternativa ou Referência"** estiverem selecionadas, o campo 04 do Registro 0200 da [EFD ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI#top) será preenchido com o número do código de barras do Produto. Além disso, a opção selecionada no campo EAN/GTINproduto p/ NF-e, definirá qual o código de barras do produto será utilizado para preencher a tag <**cEAN**> e <**cEANTrib**> do xml das notas NFC-e. O [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Sankhya-Checkout) validará o código de barras de acordo com a tabela de prefixos da GS1 e o CFOP ao realizar o cálculo de imposto na tela [Administração de Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout).
- Quando se tratar de troca de produtos, o sistema irá preencher as tags <**cEAN**> e <**cEANTrib**> com o código de barras do novo produto.
- Ao habilitar o parâmetro **"Validar EAN/GTIN do Produto na emissão da NF-e/NFC - VALEANGTINPROD"**, se os campos **"EAN/GTIN Produto p/ NF-e:"** e **"EAN/GTIN Unid.Tributação:"** (Cadastro de Produtos, aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaunidadesalternativas)) estiverem selecionados com uma opção diferente de **"Não informar"**, as informações referente ao EAN/GTIN não poderão ser nulas.

Os dados informados no campo **"MVA Original para DRCST"** serão utilizados na geração dos registros 2113 com a modalidade 30 (Venda para Simples Nacional).

Quando a marcação **"Desconsiderar produto na geração da DRCST?"** estiver realizada, fará com que o item não seja considerado na geração da DRCST.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção ADRCST

Habilite a marcação **"Considerar geração da ADRCST-ST (PR)"**, se o produto em questão for na geração dos Arquivos referente ao ADRC-ST.

Assim como o campo **"MVA Original para ADRC-ST (PR)"**, que deve ser preenchido com o MVA do produto que será utilizado nas operações de Substituição Tributaria.

Preencha o campo **"Produto alimentício conforme art. 119 do Anexo IX do RICMS/2017 PR?"** para que os produtos alimentícios destinados à merenda escolar, órgãos da administração pública, cozinhas industriais, restaurantes e similares, pizzarias e lancheiras, nos termos do art. 119 do Anexo IX do RICMS/2017 PR, sejam gerados na ADRC-ST do registro [1410](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500003168922-Gera%C3%A7%C3%A3o-do-Arquivo-ADRC-ST-PR#sub-aba1400).

Selecione a marcação **"Produto sujeito ao FECOP"**, quando o produto for sujeito ao recolhimento do Fundo Estadual de Combate à Pobreza (FECOP).

E caso o produto esteja sujeito à cobrança do fundo, informe no campo **"Alíquota FECOP"** a porcentagem do recolhimento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos)

#### Seção FCI – Ficha de Conteúdo de Importação

Informe no campo **"Código da FCI"** o código gerado para produtos com parcela importada do exterior no site <https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/Servicos.aspx>. Estes códigos estarão no arquivo de retorno gerado por este site e será habilitado se, na aba Geral, o campo **"Origem do Produto"** estiver configurado com as opções 3, 5 ou 8.

**Nota:** quando o campo **"Código da FCI"** localizado na aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa) estiver configurado, os dados do campo Código da FCInão serão considerados pelo sistema.

No campo **"Valor de Comercialização – (R$)"**, terá o valor total da operação de saída interestadual.

Informe no campo **"Valor da Parcela Importada do Exterior – (R$)"**, o valor do produto que consta no documento fiscal emitido pelo remetente.

Para maiores detalhes sobre estes três últimos campos, acesse a documentação [Ficha de Conteúdo de Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600854-Ficha-de-Conte%C3%BAdo-de-Importa%C3%A7%C3%A3o).

**Observação:** ao salvar o produto, o sistema fará uma validação, que verifica o valor salvo no parâmetro **"Parcela Importada Mínima para FCI - PARCIMPFICI"**, permitindo o valor 0 e, consequentemente, impactando os campos Valor de Comercialização - (R$) e Valor da Parcela Importada do Exterior - (R$).

A fórmula VLRPARCIMPEXT / VLRCOMERC \* 100 é comparada com o valor do parâmetro; assim, o percentual de conteúdo de importação poderá ser menor do que 1%.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Plan. de Compra de Peças

O parâmetro **"Utiliza planejamento compras para concessionárias? - USAPLANCPCONCES"** habilitará esta aba e a rotina de [Planejamento de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112553-Planejamento-de-Compras) de peças que, refere-se à um processo específico de um parceiro Sankhya.

Nela tem-se as principais configurações do produto que serão levadas em consideração no planejamento de compras.

![Imagem 28: Nela tem-se as principais configurações do produto que serão levadas em consideração no planejamento de compras.](https://ajuda.sankhya.com.br/hc/article_attachments/4402110949271)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Apontamentos

Esta aba é habilitada pelo parâmetro **"Fatura Contrato por Peso? - FATCONTPORPESO"** e poderá ser utilizada em integração com o MGE Controle de Contratos e Serviços para executar a rotina de Faturamento de Contrato de Locação por Peso/Dia.

![Imagem 29: Esta aba é habilitada pelo parâmetro "Fatura Contrato por Peso? - FATCONTPORPESO" e poderá ser utilizada em integração…](https://ajuda.sankhya.com.br/hc/article_attachments/4402111215255)

Para execução da referida rotina, são necessárias as seguintes configurações:

Realize o lançamento de um produto curinga;

Os demais produtosque serão enviados/locados (remessa/retorno no Portal de Vendas), apontarão para esse produto curinga através do campo **"Produto/Serviço p/ agrupar apontamento"**. Este produto irá definir o valor a ser cobrado por peso locado.

É necessário cadastrar os produtos que serão locados, lembrando-se de colocar seu **"Peso Bruto"** na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque).

**Nota:** a rotina Faturamento de Contrato de Locação por Peso/Dia ainda não está disponível no **Sankhya Om**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Unidades Alternativas

![Imagem 30: Aba Unidades Alternativas](https://ajuda.sankhya.com.br/hc/article_attachments/12918571733143)

As funções desta aba podem ser encontradas abaixo:

| [Sub-aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Sub-abaGerals) |
| --- |
| [Sub-aba 0220 UND Conversão - EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Subaba0220UNDConvers%C3%A3oEFD) |
| [Botão Alterar Un. Alternativa...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oAlterarUn.Alternativa...) |
| [Botão Mostrar histórico...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oMostrarhist%C3%B3rico...) |

---

No Cadastro de Produtos, a unidade de medida empregada nas operações é informada no campo **"Unidade padrão"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral). As possíveis unidades alternativas deverão ser cadastradas nesta aba, por exemplo, o produto caneta pode ser vendido em unidades ou caixas. Considerando a unidade padrão como Unidade, a alternativa será Caixa. Sendo que, o sistema considera sempre a Unidade padrão para o cálculo das Unidades Alternativas.

Caso haja alguma Unidade Alternativa cadastrada, o sistema permitirá que a Unidade Padrão seja alterada para a Unidade Alternativa já cadastrada, permitindo assim, que estas duas sejam iguais.

Determine no campo **"Unidade"** a Unidade Alternativa para o produto em questão. É importante destacar que:

- Em relação a Unidade padrão recomenda-se que sempre seja informada a menor unidade comercializável possível. Por exemplo, caso sua empresa venda "Pisos" será informado Caixa para Pisos, pois geralmente não é comercializado menos que uma caixa de piso. Para os demais produtos informe Unidade.
- As Unidades alternativas preferencialmente devem ser maiores que a unidade padrão. Por exemplo, no caso da venda de pisos, as unidades alternativas podem ser: Pallet (de "n" Caixas, pode ser comercializada, ou seja, deve ser maior que a Unidade padrão) ou M2 (geralmente uma fração da Caixa, como essa é menor não deve ser comercializável, mas pode ser utilizada para fins de comparação de preços, estoque). Se for permitido a comercialização em unidades maiores, pode-se informar caixa com "x" unidades ou fardo de "y" unidades.

**Observação:** o sistema possibilita criar unidades alternativas com quantidades específicas associadas. Por exemplo:

- **C1:** representa uma caixa (CX) com X unidades;
- **C2:** representa uma caixa (CX) com Y unidades;
- **B1:** representa um pacote com Z unidades.

Não há limites para a utilização do alfabeto, ou seja, é possível criar qualquer combinação de Unidades e Quantidades desejadas, utilizando letras como identificadores.

### Sub-aba Geral

Escolha no campo **"Operação"** como será realizado o cálculo que definirá o valor da Unidade Alternativa que está sendo criada, dentre as opções:

- **Divide:** use esta opção quando a Unidade Alternativa for menor que a principal. Nesse caso, o sistema irá dividir a unidade padrão para chegar na qtd. 1 da unidade alternativa.

Exemplo:
Unid. Padrão: CX(com 10UN)
Unid. Alternativa: UN
Logo: Operação = Divide e Quantidade = 10

- **Multiplica:** selecione esta opção quando a Unidade Alternativa for maior que a principal. Assim, o sistema irá multiplicar a unidade padrão para chegar na qtd. 1 da unidade alternativa.

Exemplo:
Unid. Padrão: UN
Unid. Alternativa: CX(com 10UN)
Logo: Operação = Multiplica e Quantidade = 10

**Observação:** uma boa prática é usar sempre que possível a menor unidade como padrão, pois a operação Divide pode resultar em dízimas e impactar diversas rotinas/processos.

O valor informado no campo **"Multiplicador de Valor"** é levado para os detalhes de preço e posteriormente para a venda. Ainda referente a esse campo, caso o **"Volume"** (tela [Descontos Promocionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600034-Descontos-Promocionais)) não possuir promoção cadastrada, o sistema só utilizará o valor informado no Multiplicador de Valor. Se uma promoção for aplicada para este, o multiplicador será nulo.

Referente ao campo **"Qtd Casas Decimais UPF"**, destaca-se que na emissão da nota para que o cálculo do FETHAB seja realizado na realizado na Central de Vendas será necessário que um índice da UPF seja cadastrado na tela [Índices](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609014), e a referida Empresa esteja com a marcação **"Calcula FETHAB?"** (tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades)) efetuada, assim como o campo **"Alíquota FETHAB"** desta tela (aba Impostos) com o percentual determinado pela UF do emitente.

No campo **"Quantidade"** informe o valor correspondente à unidade alternativa. Por exemplo, ao informar a quantidade "20" entende-se que, cada caixa será composta por 20 unidades do produto.

![Imagem 31: A quantidade de casas decimais apresentadas neste campo, pode ser configurada no parâmetro "Qtd de casas decimais…](https://ajuda.sankhya.com.br/hc/article_attachments/20115572145303) A quantidade de casas decimais apresentadas neste campo, pode ser configurada no parâmetro **"Qtd de casas decimais apresentadas pelo DBEXplorer - DBEXPDEC"** e visualizadas em consultas no [DBExplorer](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603894), sendo que, caso seja configurada uma quantidade acima de 16, os valores das casas decimais exibidos nesta consulta serão apresentados truncados.

Por exemplo, o parâmetro foi configurado com 17 casas decimais e, no Cadastro de Produtos, aba Unidades Alternativas, foi configurada uma unidade alternativa com a quantidade "2,55", após realizar a consulta "SELECT CODPROD, CODVOL, QUANTIDADE FROM TGFVOA WHERE CODPROD = X", foi apresentado o valor de "2,54999999999999982" no campo Quantidade.

Lembrando que esse parâmetro é apenas para visualização das casas decimais ao realizar uma consulta, não interferindo no registro no banco de dados.

Ative a marcação **"Unid. Tributação"** caso deseje que as informações referentes a unidade alternativa sejam enviadas para o XML das notas lançadas.

**Observação:** o sistema irá buscar a Unidade Alternativa com a marcação Unid. Tributação ativada, independentemente do status da Unidade Alternativa, e transferir essa informação para o XML e DANFE. O campo Unid. Tributação tem prioridade sobre o campo ativo. Caso todas as Unidades Alternativas possuam **"não"** na opção Unid. Tributação, a Unidade Alternativa utilizada na emissão da nota será considerada tanto como unidade de comercialização como unidade de tributação no XML.

A definição da unidade de tributação informada no XML da nota fiscal eletrônica é feita automaticamente pelo sistema, conforme o tipo de operação realizada. Para operações de exportação, o sistema verifica se o cadastro do Produto possui o campo **“Descrição Un. Tributação Exportação”** preenchido; se existir, essa será a unidade utilizada no XML. 

Caso não esteja preenchido, mas a opção **“Un. Tributação Exportação em Toneladas”** esteja marcada, o sistema utilizará a unidade 'TON'. Se ambas as opções estiverem configuradas, prevalece a informação da **“Descrição Un. Tributação Exportação”**. Já para operações destinadas ao mercado interno, o sistema mantém o comportamento padrão e utiliza a unidade alternativa marcada como **“Unid. Tributação”** no cadastro do produto. Dessa forma, elimina-se a necessidade de ajustes manuais, garantindo que a unidade de tributação correta seja preenchida automaticamente no documento fiscal, conforme o contexto da operação.

O parâmetro **"Aceita unidade alternativa igual a principal? - UNALTIGUAL"**, permite ou não que seja efetuado o cadastro de Unidades Alternativas iguais à Unidade Principal. Sendo que, ao incluir uma Unidade Alternativa igual a Unidade Principal do produto, a quantidade deverá necessariamente ser igual a 1.

Ao acionar a marcação **"Un. Tributação Exportação em Toneladas"** tem-se o envio do valor **"TON"** na TAG **<uTrib>** quando o CFOP corresponder ao 1501, 2501,5501, 5502, 5504, 5505, 6501, 6502, 6504, 6505, 7101, 7102, 7127, 7501 ou 7949.

**Observação:** caso deseje que o sistema realize a conversão para Unidade Alternativa, a Un. Tributação Exportação em Toneladas não deverá ser ativada. Pode ser utilizado também o valor descrito no campo **"Descrição Un. Tributação Exportação"** quando informado, e se o CFOP for algum dos que estão mencionados acima.

Sendo assim, quando o CFOP não for nenhum dos descritos, o sistema não realizará a conversão de Unidade Alternativa.

---

**Notas:**

![Imagem 32: Em todas as telas do sistema de Movimentação de Produtos e Consultas de Preços e Estoque serão apresentadas as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215060759) Em todas as telas do sistema de Movimentação de Produtos e Consultas de Preços e Estoque serão apresentadas as opções de unidades cadastradas para o produto, ou seja, a Unidade Padrão e as Unidades Alternativas. Assim, após o lançamento do produto na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens) da Central - Compras | Vendas | Mov. Internas, quando for alterada a unidade padrão para à alternativa, na conversão da quantidade se o valor resultante não for exato, o sistema lançará o valor 0 (zero) para o campo **"Quantidade"**, nos itens da nota. Porém, se o campo **"Decimais p/ quantidade"** (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque)) possuir um valor configurado para casas decimais da quantidade, o sistema fará a quebra na conversão da unidade e apresentará o valor fracionado referente à quantidade para a Unidade Alternativa. De acordo com estas informações, analise um exemplo:

A unidade padrão é Litro, a unidade alternativa Caixa, multiplicando por 2. Logo, cada caixa comportará 2 litros. Se nos itens da nota for informada a quantidade 1 para unidade padrão, ao alterar para unidade alternativa o sistema irá zerar o campo **"Quantidade"** se o produto não possuir Decimais p/ quantidade, pois a quantidade informada de 1 litro corresponderá apenas à metade de uma unidade alternativa, sendo assim o valor resultante seria 0,50 (meia caixa) e o produto não permite esse valor sem a configuração de decimais.

![Imagem 33: O parâmetro "Decimais p/ cálculo de Volume Alternativo - DECVLRVOLALT" , definirá o número de casas decimais que o…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215069975) O parâmetro **"Decimais p/ cálculo de Volume Alternativo - DECVLRVOLALT"**, definirá o número de casas decimais que o sistema irá considerar na conversão de valores de produtos quando os mesmos forem vendidos em Unidades Alternativas. Sendo este útil nos casos em que o multiplicador para valor possuir várias casas decimais, assim o valor convertido será arredondado para um valor mais próximo do real.

Quando o referido parâmetro não estiver configurado, o sistema considerará 2 casas decimais na conversão do valor. Abaixo observe um exemplo desta informação:

O produto Z contém a unidade principal KG e a alternativa Caixa;

O valor na unidade principal é R$4,10;

O multiplicador para valor é 0,913415;

Ou seja, 4,10 x 0,913415 = 3,7450015.

Assim, o sistema irá arredondar para 3,75 (considerando só duas casas decimais) x 20 (multiplicador da quantidade) = 75,00. Se o parâmetro estiver configurado com o valor de 4 casas decimais, arredonda-se para 3,7450 (considerando 4 casas decimais) x 20 (multiplicador da quantidade) = 74,90.

![Imagem 34: O sistema irá considerar Unidades Alternativas por Controle Adicional de Estoque , sendo que, o campo "Controle" nesta…](https://ajuda.sankhya.com.br/hc/article_attachments/25993945648663) O sistema irá considerar Unidades Alternativas por Controle Adicional de Estoque, sendo que, o campo **"Controle"** nesta aba, só poderá ser preenchido quando o controle adicional de estoque (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), campo **"Controlar por"**) for do tipo **"Livre"** ou **"Lista"**. Estando configurado como Lista, os controles cadastrados serão apresentados nesta aba com o nome do campo de acordo com o campo **"Título"** da aba Medidas e Estoques.

![Imagem 35: Ao começar a utilizar Unidade Alternativa , é necessário conferir se os TXT's possuem tratamento para a mesma. Assim…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215084311) Ao começar a utilizar Unidade Alternativa, é necessário conferir se os TXT's possuem tratamento para a mesma. Assim sendo, deverá existir tratamento para os campos **"Unidade"**, **"Quantidade"** e **"Valor Unitário"**, conforme descrição abaixo:

Impressão Unidade Alternativa

if(&vvoa01=&vvol01,&vvoa01,&vvol01) - tratamento da unidade;

if(&vvoa01=&vvol01,&vqtd01,&vqta01) - tratamento de quantidade;

if(&vvoa01=&vvol01,&vvlr01,&vvla01) - tratamento para o valor unitário.

Informe no campo **"Descrição da unidade/qtd. para o DANFE"** uma descrição para a Unidade Alternativa que será apresentada no DANFE logo à frente da descrição do produto de modo a complementar a nomenclatura principal do mesmo. Analise o exemplo abaixo:

Produto: água sem gás

Campo Descrição da unidade/qtd. para o DANFE: caixa com 12 unid.

Logo, no DANFE, o produto será apresentado: **"Água sem gás | Caixa com 12 unid"**.

Para isso, é necessário:

- Acessar a tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) e desligar o parâmetro **"Usar a unidade padrão na NFe - USARUNIDPADNFE"**.
- Acessar as [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), filtrar a empresa a ser utilizada, selecionar no Botão Outras Opções... a opção **"Complemento para itens da nota (Web)"**, e acrescentar para Campos em Uso a variável **"Descrição de unidade/qtd. para o DANFE"**.

[GIF animado: Imagem 36: Acessar as Preferências da Empresa , filtrar a empresa a ser utilizada, selecionar no Botão Outras Opções... a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/4402111991319)

Feito isso, pode-se lançar uma nota utilizando a unidade alternativa, aprová-la e constatar no XML que a descrição virá concatenada com a tag **<infAdProd>**, juntamente com os demais campos em uso, selecionados nas Preferências da Empresa. Se o referido parâmetro estiver habilitado, a descrição de unidade/qtd para o DANFE não será apresentada no XML, somente as demais opções configuradas no XML.

No campo **"Descrição Un. Tributação Exportação"**, informe a unidade alternativa que será convertida, para que, assim, o sistema realize a conversão da unidade digitada na venda para exportação. De forma que, na geração do XML, o preenchimento deste fará com que a tag seja enviada com o valor selecionado no referido campo caso este possua os seguintes CFOP's:

- 1501;
- 2501;
- 5501;
- 5502;
- 5504;
- 5505;
- 6501;
- 6502;
- 6504;
- 6505;
- 7101;
- 7102;
- 7127;
- 7501;
- 7949.

**Observação:** ao gerar uma nota de complemento modificando a unidade do produto. Para que não haja conversão das unidades alternativas do produto deverá desabilitar a marcação Unid. Tributação e no campo Descrição Un. Tributação Exportação nenhuma opção selecionada.

A marcação **"Apresentar nas tarefas do WMS"** quando acionada, influenciará apenas nas Tarefas de Separação exibindo neste processo a Unidade Principal da tarefa entre parênteses e também a Unidade Alternativa que possuir o maior agrupamento.

![Imagem 37: O parâmetro "Valida volume ativo na central flex - grade? - VALCODVOLATIVO" garante que unidades alternativas…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215090071) O parâmetro **"Valida volume ativo na central flex - grade? - VALCODVOLATIVO"** garante que unidades alternativas desativadas não sejam utilizadas em novos lançamentos nas Centrais. Ele possui uma lista com os tipos de validação que o sistema pode realizar, conforme descrito abaixo:

- **Não valida:** apenas a existência do volume informado é validada;
- **Valida volume:** valida tanto a existência do volume quanto se ele está ativo. Se houver uma linha no cadastro de volume sem o controle informado e essa linha estiver ativa, todos os outros controles serão considerados ativos por herdar dessa linha;
- **Valida volume e controle:** verifica a existência do volume combinado com o controle informado pelo usuário na comercialização e se ambos estão ativos.

Recomenda-se ativar este parâmetro ao desabilitar a marcação **"Ativo"** localizada nessa aba.

---

A marcação **"Unidade de Tributação para RECOB"** quando habilitada, ativa o cálculo de PIS e COFINS sobre a receita gerada pela venda de álcool por cooperativas a comerciantes varejistas, aplicando as alíquotas de 19,81 e 91,10 por metro cúbico de álcool, respectivamente. 

Caso já exista um cadastro de uma Unidade Alternativa para o produto da nota que possua a marcação acima habilitada, não será possível configurar uma nova, caso o usuário tente, a seguinte mensagem surgirá na tela: 

**“Já existe outra unidade alternativa para este produto com a opção Unidade de Tributação para RECOB marcada, portanto, essa operação não poderá ser realizada”**

Para que o cálculo do PIS e do COFINS seja registrado no pop-up **"Consultar/Alterar Dados do Imposto do Item..."**, na grade de [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens), botão ![Imagem 38: Para que o cálculo do PIS e do COFINS seja registrado no pop-up "Consultar/Alterar Dados do Imposto do Item..." , na…](https://ajuda.sankhya.com.br/hc/article_attachments/16089681762455) **"Outras Opções"** das Centrais de [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) e de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), considerando o cálculo por meio do benefício RECOB, use as seguintes configurações:

- Cadastre um grupo específico para o **"Produto"** e **"Empresa"**da nota nas telas [Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS) e/ou [Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS), com CST igual a 03 e tipo de alíquota igual a **"Valor"**, definindo as alíquotas pertinentes a cada imposto;
- Vincule o grupo criado nos campos **"Grupo PIS"** e **"Grupo COFINS"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) do Cadastro de Produtos configurando a unidade alternativa a ser usada para a tributação do PIS e COFINS;
- Habilite a marcação Unidade de Tributação para RECOB;
- Acesse a tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), efetuue as marcações **"Calcula PIS"** e **"Calcula COFINS"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral).

Desse modo, quando incluir uma nota de saída no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) com os dados acima configurados para o cálculo do PIS e COFINS, o benefício estará incluído no cálculo, sendo que: 

- **Base de Cálculo** é a quantidade negociada no documento, convertida com base no volume de tributação configurado na aba Unidades Alternativas da tela Cadastro de Produtos que tenha a marcação Unidade Tributação para RECOB habilitada;
- **Base Cálc. Reduzida** é a quantidade negociada no documento, convertida com base no volume de tributação configurado na aba Unidades Alternativas da tela Cadastro de Produtos que tenha a marcação Unidade Tributação para RECOB habilitada, aplicando-se a redução se houver;
- **Alíquota** será preenchida conforme configuração das telas Alíquotas de PIS e Alíquotas de COFINS;
- **Valor** será o resultado da Base Cálc. Reduzida x Alíquota.

Com o cadastro realizado, ao gerar um XML da NF-e em arquivo para conferência aplicando as alíquotas informadas acima, por exemplo, o documento conterá os grupos de tags **<PISQtde>** e **<COFINSQte>** no produto, além das tags **<vPIS>** e **<vCOFINS>** do grupo totalizador, sendo que: 

(1)** PISQtde:**

- **<qBCProd>**0,5**</qBCProd>** será igual ao conteúdo do campo Base Cálc. Reduzida da TGFDIN do imposto PIS;
- **<vAliqProd>**19,81**</vAliqProd>** será igual ao conteúdo do campo Alíquota da TGDIN do imposto PIS;
- **<vPIS>** 9,90**</vPIS>** será igual ao conteúdo do campo Valor da TGFDIN do imposto PIS;

(1)** COFINSQtde:**

- **<qBCProd>**0,5**</qBCProd>** será igual ao conteúdo do campo Base Cálc. Reduzida da TGFDIN do imposto PIS;
- **<vAliqProd>**91,10**</vAliqProd>** será igual ao conteúdo do campo Alíquota da TGDIN do imposto PIS;
- **<vCOFINS>**45,60**</vCOFINS>** será igual ao conteúdo do campo Valor da TGFDIN do imposto PIS.

Dessa forma, ao gerar o arquivo na tela de [EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407916885271-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS), e validar no PVA, o registro C170 será preenchido da seguinte forma: 

(1)** PIS:**

- **QUANT\_BC\_PIS:** será igual ao conteúdo do campo Base Cálc. Reduzida da TGFDIN do imposto PIS;
- **ALIQ\_PIS\_QUANT:** será igual ao conteúdo do campo Alíquota da TGDIN do imposto PIS;
- **VL\_PIS:** será igual ao conteúdo do campo Valor da TGFDIN do imposto PIS.

(1)** COFINS:**

- **QUANT\_BC\_COFINS:** será igual ao conteúdo do campo Base Cálc. Reduzida da TGFDIN do imposto COFINS;
- **ALIQ\_COFINS\_QUANT:** será igual ao conteúdo do campo Alíquota da TGDIN do imposto COFINS;
- **VL\_COFINS:** será igual ao conteúdo do campo Valor da TGFDIN do imposto COFINS.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas)

### Sub-aba 0220 UND Conversão - EFD

![Imagem 39: Sub-aba 0220 UND Conversão - EFD](https://ajuda.sankhya.com.br/hc/article_attachments/12918607810455)

Nessa sub-aba define-se as **"Opções para gerar Registros 0220"** de acordo com as opções abaixo:

- **Utiliza Unidade Alternativa:** com essa opção, será utilizado o processo de conversão observando a unidade de medida existente na aba Unidades Alternativas e seu fator de conversão. Além disso, os registros C100 e C170 serão gerados com as informações de UND do Parceiro.
- **Utiliza UND do Produto Equivalente:** aqui será utilizada a unidade relacionada ao parceiro do lançamento da NFe existente na aba Produtos Equivalentes, junto com o fator de conversão apresentado na aba Geral.
- **A partir da função:** utilizará o retorno da função SNK\_GET\_XXXX, a ser personalizada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas)

### Botão Alterar Un. Alternativa...

O botão ![Imagem 40: O botão "Alterar Un. Alternativa..." localizado no topo dessa aba, é utilizado em casos que é necessário modificar a…](https://ajuda.sankhya.com.br/hc/article_attachments/16087720028567) **"Alterar Un. Alternativa..."** localizado no topo dessa aba, é utilizado em casos que é necessário modificar a unidade alternativa de um produto, aumentando ou diminuindo seus valores múltiplos, mantendo ou não o código de barras principal.

Para alterar a quantidade de uma unidade alternativa, realize os seguintes passos:

- Se a unidade alternativa nunca tiver sido utilizada nas rotinas do módulo WMS, será possível modificá-la normalmente pela aba Unidade Alternativa;
- Caso a unidade já tenha sido utilizada, será necessário fazer uso do botão Alterar Un. Alternativa...;
- Não é possível realizar uma alteração de unidade alternativa se existirem tarefas em aberto para a unidade em questão, ou ainda se houver estoque do produto nesta unidade em endereços que não estão bloqueados. Neste último caso portanto, será necessário efetuar o bloqueio prévio para esses endereços;
- Ao acionar o botão Alterar Un. Alternativa... será aberto o pop-up de nome **"Alteração unidade alternativa"** onde tem-se as seguintes definições:

Por meio do campo **"Alteração do Cód. Barras"** é feita a definição se o código de barras da unidade alternativa será mantido ou deverá ser modificado; esta análise é realizada com base nos processos entre empresas e fornecedores/clientes; para tal, utilize as opções Alterar o Cód. Barras para a nova unidade ou Manter o Cód. Barras para a nova unidade.

Informe a **"Nova quantidade"** da unidade alternativa neste campo; esta deve ser distinta da quantidade atual.

Insira o **"Novo código de barras"** da unidade alternativa, desde no campo Alteração do Cód. Barras a opção Alterar o Cód. Barras para a nova unidade tenha sido selecionada.

- Depois de informados os novos dados pertinentes à quantidade e ao código de barras, caso o produto não possua estoque na unidade que está sendo modificada, o botão **"Concluir"** ficará habilitado e, ao acioná-lo, completa-se a operação de alteração da unidade alternativa;
- Caso exista estoque em algum endereço para o produto na unidade alternativa que foi alterada, tem-se um próximo passo no pop-up onde são apresentadas duas grades, em que a primeira contém os endereços que possuem produtos na unidade antiga e a segunda exibe os endereços disponíveis para transferência do produto;
- Nessa situação, será necessário realizar a transferência de todos os produtos para os endereços disponíveis em unidade alternativa. Toma-se essa medida pois, a partir desse ponto, o estoque antigo na unidade modificada será tratado internamente pelo sistema como estando na unidade padrão;
- Para cada endereço de origem contendo o produto, pode alocar uma quantidade a ser transferida para os endereços da grade de destino. Para isso, basta selecionar um endereço de origem e informar uma quantidade na coluna **"Qtd. Transferir Un. Padrão"** da grade de destino. Inicialmente, as linhas estarão na coloração **vermelha** indicando que ainda é necessário transferir quantidades dos produtos. Quando toda a quantidade dos estoques de origem for transferida para os destinos, a linha ficará na coloração **verde**, indicando que a operação poderá ser concluída e as tarefas de transferência geradas. Tem-se também, um contador de quantidades a transferir, que visa auxiliar o usuário na tarefa de alocação de quantidades entre os endereços de destino. Caso não exista um endereço de destino, crie um endereço que aceite o produto (deve haver um relacionamento feito na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), aba [Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abaproduto));
- Ao clicar em Concluir, a unidade alternativa terá sua quantidade e código de barras atualizado; além disso, será gerado um histórico contendo a quantidade antiga e o código de barras antigo;

A partir dessa configuração, se for bipado o código de barras antigo, a quantidade do produto será convertida para a unidade padrão e o comportamento será como se o usuário tivesse bipado uma embalagem na unidade padrão com a quantidade equivalente à unidade do histórico. Se houve alocação de estoque, no segundo passo do pop-up Alteração unidade alternativa, serão geradas tarefas de transferência para os endereços de destino. As transferências também serão feitas todas na unidade padrão.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas)

### Botão Mostrar histórico...

O botão ![Imagem 41: O botão "Mostrar histórico..." ao ser acionado, apresenta um pop-up de nome "Histórico das Unidades Alternativas" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16087813689239) **"Mostrar histórico..."** ao ser acionado, apresenta um pop-up de nome **"Histórico das Unidades Alternativas"**, onde é possível consultar a relação das modificações em unidades alternativas que foram realizadas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Código de Barras

Nesta aba tem-se a possibilidade de cadastrar Códigos de Barras Adicionais para o produto em questão.

![Imagem 42: Nesta aba tem-se a possibilidade de cadastrar Códigos de Barras Adicionais para o produto em questão.](https://ajuda.sankhya.com.br/hc/article_attachments/4402112216215)

Informe no campo **"Cód. Barras"**, os valores que representam o novo código de barras.

No campo **"Unidade de Volume"** será informada a unidade a ser vinculado no novo código de barras.

**Importante:** os códigos de barras aqui cadastrados não podem ser utilizados como código de barras em uma NF-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Perfil de Consumo

![Imagem 43: Aba Perfil de Consumo](https://ajuda.sankhya.com.br/hc/article_attachments/4402117219223)

Esta aba é reservada ao cadastro do Perfil dos Parceiros que compram o produto que está sendo cadastrado. Sendo assim, é preciso que o Perfil a ser inserido seja cadastrado previamente na rotina de [Cadastros de Perfil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110753-Perfil) e seja do tipo Analítico.

No campo **"Perfil do parceiro"** informe o código do Perfil, ou clique no ícone em forma de lupa para pesquisar ou apresentar a hierarquia dos cadastros disponíveis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Família

![Imagem 44: Aba Família](https://ajuda.sankhya.com.br/hc/article_attachments/4402112242839)

No Cadastro de Produtos, a família é uma forma de agrupar produtos afins, para que o sistema os mantenha sempre com mesmo preço e para que exista uma forma mais sucinta de analisar as compras em grupo, tanto quanto individualmente.

Tem-se abaixo um exemplo de utilização desta aba:

| **Produtos da família: Geladeira 250 Litros** | |
| --- | --- |
| **Descrição** | **Preço** |
| Geladeira 250L Branca 220V | R$ 800,00 |
| Geladeira 250L Azul 220V | R$ 800,00 |
| Geladeira 250L Verde 220V | R$ 800,00 |
| Geladeira 250L Branca 110V | R$ 800,00 |
| Geladeira 250L Azul 110V | R$ 800,00 |
| Geladeira 250L Verde 110V | R$ 800,00 |

Na compra de um destes produtos, apenas os custos gerenciais dos itens e o preço de tabela pertencentes à família serão atualizados. Contudo, os custos de entrada com ICMS e custos médios não deverão ser atualizados, pois podem comprometer o fiscal do financeiro, uma vez que não houve uma compra para esses produtos.

> **Observação:** a apuração de custos não é realizada de forma cronológica considerando registros "por hora". A cronologia adotada é baseada em períodos "diários".

Quando temos produtos de família que não possuem custo ou estoque anterior e seus custos são calculados no mesmo dia, mesmo sendo em notas diferentes, todas as informações sobre os custos são calculadas de forma a achar a média para todos os campos. O cálculo do custo médio quando se trabalha com **FAMÍLIA** segue a fórmula:

```
$$Custo Médio = \frac{Custo Anterior + Custo da Entrada}{Estoque Anterior + Estoque da Entrada}$$
```

Caso a entrada de um dos produtos ocorra no dia anterior, o sistema já terá uma base de custos consolidada para ser adotada no cálculo dos demais itens da família.

Os campos **"Complemento"**, **"Marca"** e **"Referência"** são preenchidos automaticamente com os dados da aba **Geral** do produto cadastrado no campo **"Produto Filho"** desta aba.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Impostos / Informações por empresa

Esta aba é habilitada através da ativação do parâmetro **"Usa imposto de produtos por empresa? - EMPPRODIMPOST"**. A partir deste parâmetro, o sistema irá considerar as informações desta aba nas movimentações dos portais, emissão de cupons fiscais, transferência de estoque matriz/filial/matriz e exportação para Fast Service.

![Imagem 45: Esta aba é habilitada através da ativação do parâmetro "Usa imposto de produtos por empresa? - EMPPRODIMPOST" . A…](https://ajuda.sankhya.com.br/hc/article_attachments/4402117252119)

Quando houver exceção por empresa, ou seja, alguma linha nesta aba, o sistema considerará sempre essas informações. Quando se estiver usando empresas que não contenham uma linha cadastrada, o sistema fará os cálculos utilizando as configurações principais do Cadastro de Produtos.

Utilize as seguintes sub-abas para configurar:

| [Sub-aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#SubabaGeral) | [Sub-aba Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#SubabaImpostos) |
| --- | --- |

---

### Sub-aba Geral

No campo **"Grade Produto"** selecione a grade de produtos definida na tela **"Modelo de Grade"** para realizar as configurações utilizadas em produtos que possuírem produtos controlados por grade. 

**Importante:** os módulos [Cotação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113993), [WMS](https://ajuda.sankhya.com.br/hc/pt-br/sections/360007733394-WMS), [Produção](https://ajuda.sankhya.com.br/hc/pt-br/sections/360007784253-Produ%C3%A7%C3%A3o-W) e a [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia) não suportam o [Controle de Produtos por Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045269813-Controle-de-Produtos-por-Grade). 

É possível criar exceções por empresa no [Cadastro de Grupo de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os). Os campos **"Empresa"** e **"Grupo ICMS"** presentes na aba [Impostos por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294-Grupos-de-Produtos-Servi%C3%A7os#abaimpostosporempresa), funcionarão da mesma forma que aqui no Cadastro de Produtos. Quando houver uma empresa e um grupo cadastrado neste campos, o sistema considerará as exceções na alíquota de ICMS para o grupo escolhido.

Referente ao campo **"Tipo do item p/ SPED"**, a opção marcada nele será usada para a geração do SPED.

**Observação:** caso selecione opção Utilizar do "Usado como", o sistema utilizará a referência do campo para que este seja preenchido, ou seja, se no campo Usado como a opção Consumo esteja selecionada, será este que o sistema considerará para a geração do SPED.

Referente ao campo **"Alíquota interna de ICMS"**, este será utilizado para executar o cálculo efetivo de ICMS na NFe.

**Nota:** se o produto for substituto tributário e vendido sem incidência de ICMS recolhido na entrada da mercadoria, será necessário calcular o ICMS efetivo para geração das tags pRedBCEfet, pICMSEfet, vlrCMSEfet. Exemplo:

Caso o ICMS da mercadoria seja com CST 60, as tags referidas anteriormente preencherão os grupos ICMS60 e ICMSSN500.

Se o cálculo deste imposto for realizado normalmente, o sistema irá considerar o percentual da alíquota informado na tela [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral).

**Observação:** para a geração do Registro 0200, e assim, a geração do campo **"12 - ALIQ\_ICMS"** no SPED, sistema segue uma hierarquia. Observe:

![Imagem 46: Primeiramente, o Sankhya Om irá verificar o preenchimento do campo Alíquota Interna de ICMS na aba 0200 do EFD do…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215060759) Primeiramente, o **Sankhya Om** irá verificar o preenchimento do campo Alíquota Interna de ICMS na aba [0200 do EFD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#0200doEFD) do Cadastro de Produtos;

![Imagem 47: Caso essa informação esteja ausente, será verificada no campo Alíquota Interna de ICMS da aba Impostos / informações…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215069975) Caso essa informação esteja ausente, será verificada no campo Alíquota Interna de ICMS da aba Impostos / informações por Empresa;

![Imagem 48: Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da…](https://ajuda.sankhya.com.br/hc/article_attachments/25993945648663) Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) do Cadastro de Produtos;

![Imagem 49: Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo "Alíq. Interna…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215084311) Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo **"Alíq. Interna Destino"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral).

O valor preenchido no campo **"Perc. Red. Base Icms Efetivo"** irá impactar no cálculo da base do ICMS Efetivo, levando a informação ao campo **"Perc. Red. base Efetivo"** do impostos do item.

O campo **"Lead time de compra"** contém a mesma funcionalidade do campo Lead time de compra da aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) porém, aqui é possível cadastrar um lead time de compra para cada empresa.

A marcação **"Calcular DIFAL?"** permite singularizar o cálculo do DIFAL associando a empresa ao produto. Vale mencionar que, na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) (também no Cadastro de Produtos), tem-se esta mesma marcação, que é realizada em situações onde o produto em questão trabalha com cálculo do DIFAL; se desmarcada, o item não se enquadra neste caso. Com a marcação Calcular DIFAL presente nestas duas abas, o sistema segue a seguinte prioridade:

![Imagem 50: Calcular DIFAL, aba Impostos / Informações por empresa marcado - o sistema procede com o cálculo do DIFAL;](https://ajuda.sankhya.com.br/hc/article_attachments/24595215060759) Calcular DIFAL, aba Impostos / Informações por empresa marcado - o sistema procede com o cálculo do DIFAL;

![Imagem 51: Calcular DIFAL, aba Impostos / Informações por empresa desmarcado - o sistema verifica se a marcação Calcular DIFAL na…](https://ajuda.sankhya.com.br/hc/article_attachments/24595215069975) Calcular DIFAL, aba Impostos / Informações por empresa desmarcado - o sistema verifica se a marcação Calcular DIFAL na aba Impostos está realizada, e caso afirmativo, prossegue com o cálculo do DIFAL;

![Imagem 52: Calcular DIFAL, aba Impostos / Informações por empresa desmarcado e Calcular DIFAL , aba Impostos também desmarcado - o…](https://ajuda.sankhya.com.br/hc/article_attachments/25993945648663) Calcular DIFAL, aba Impostos / Informações por empresa desmarcado e Calcular DIFAL, aba Impostos também desmarcado - o cálculo do DIFAL não irá ocorrer para o produto em questão.

Caso o produto se enquadre em alguma alíquota em específico, esta alíquota será informada no campo **"Alíquota Geral"**.

Da mesma forma, possuindo o produto uma configuração de MVA Padrão específica, esta deverá ser indicada no campo **"MVA Padrão"**.

Na configuração das alíquotas de ICMS, caso seja necessário incluir o produto que será envolvido por esta alíquota, em algum grupo específico, faça uso do campo **"Grupo de ICMS 2"**, inserindo neste um determinado grupo. Este campo será apresentado para escolha como exceção na estruturação das alíquotas de ICMS, bem com o campo **"Código da Empresa"**, caso seja necessário configurar uma exceção por esta característica.

Existem operações que as empresas importam mercadorias diretamente do exterior e movimentam essa mercadoria entre suas unidades (matriz/filial), e esta movimentação caracteriza-se por ser uma importação interna e não direta como foi feita anteriormente. A situação tributária (CST) nas duas situações é diferente em cada empresa. O sistema atende a definição de **"Origem do produto"** por empresa para que na nota fiscal o sistema gere a CST corretamente de acordo com a movimentação realizada com a mercadoria, ou seja, o sistema calcula CST do mesmo produto considerando origens diferentes para empresas diferentes, para que o CST de cada nota fiscal fique correta. Observe abaixo um exemplo prático do comportamento do campo:

Suponha-se que tenha sido definido as alíquotas de ICMS de modo que o produto possua a tributação sempre igual a Tributada e c/ cobrança de substituição (10) e os cadastros nessa aba da seguinte forma:

| **Empresa** | **Origem do Produto** |
| --- | --- |
| 1 | 0 |
| 3 | 1 |
| 2 | 2 |

Sendo assim, quando houver movimentações deste produto com essas empresas o sistema se comportará da seguinte forma:

| **Quando movimentar com a empresa** | **Gera CST** |
| --- | --- |
| 1 | 010 |
| 2 | 110 |
| 3 | 210 |

Em notas movimentadas com a empresa 2 por exemplo, na impressão do DANFE o CST deverá considerar a origem do produto informada, que no nosso exemplo é o 1, ficando impresso então da seguinte forma:

CST = origem do produto + tributação

CST = 1 + 10

CST = 110

O sinal de soma (+), neste caso, apresenta somente a junção dos valores dos campos, não somando os dois matematicamente. Enquanto que, no XML o sistema deverá gerar o mesmo da seguinte forma:

**<orig>1</orig>** - origem do produto

**<CST>10</CST>** - tributação do produto

**CST Impresso no DANFE:** 110

Ao imprimir uma nota de venda com a empresa 1, cuja a origem do produto é 0, então o resultado seria o seguinte:

**<orig>0</orig>** - origem do produto

**<CST>10</CST>** - tributação do produto

**CST Impresso no DANFE:** 010

Caso realizasse a venda com a empresa 3 cuja a origem do produto é 3, o resultado seria:

**<orig>2</orig>** - origem do produto

**<CST>10</CST>** - tributação do produto

**CST Impresso no DANFE:** 210

Caso o campo **"Origem do Produto"** da aba Impostos / Informações por empresa esteja vazio, ou o sistema não encontre regras para buscar a origem do produto da aba Impostos por empresa, o sistema deverá considerar a informação do campo Origem do produto da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) do Cadastro de Produtos, e o comportamento da nota será conforme essa definição. Por exemplo: se lançar uma nota de venda com o produto da empresa 3 e o mesmo estiver com o campo **"Origem do produto"** em branco, o sistema buscará então o CST referente a origem do produto da aba Geral.

**Observação:** apesar dos exemplos terem sido feitos somente com relação aos tipos de origem vazio, zero, um e dois, esta funcionalidade também é válida para os demais tipos de origem do produto, como o três, quatro, cinco, seis e o sete.

Os campos **"IPI na Entrada"** e **"IPI na saída"** possuem as opções **"Conforme cadastro"**, **"Tem IPI"** e **"Não tem IPI"**. Dessa maneira, pode-se observar os seguintes comportamentos:

- Ao escolher a opção Conforme cadastro, o sistema irá considerar as informações da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostos).
- Se a empresa possuir IPI, então a opção Tem IPI deverá ser selecionada.
- Deve-se optar pela opção Não tem IPI caso a empresa não tenha IPI, sendo necessário considerar as informações de CST.

**Observação:** ao utilizar a opção Não tem IPI, o sistema irá buscar o CST configurado nessa aba e não realiza o cálculo do IPI, no entanto, se utilizar a opção Tem IPI será calculado.

O campo **"Ressarcimento de ST (CAT - 17/99)"** é responsável pelo preenchimento dos relatórios de ressarcimento de ST.

No campo **"Tipo de Controle de Estoque"**, o sistema fará o uso do tipo de controle por empresa conforme a opção configurada. Porém, o parâmetro **"Usa controle adicional de estoque por Empresa - CONTROLEADEMP"** precisa ser habilitado, pois, caso contrário, o tipo de controle definido no campo não funcionará mesmo se os campos estiverem corretamente configurados. Sabendo disso, o campo Tipo de Controle de Estoque dispõe das seguintes opções:

- **Data da validade:** utilizando desta opção, o estoque será controlado pela data de validade dos produtos. como por exemplo, as empresas de laticínios que aplicam esta opção no seu controle de estoque para dar saída primeiramente aos seus produtos perecíveis mais antigos;
- **Parceiro:** neste caso, tem-se o controle do estoque por parceiro;
- **Sem controle adicional:** com esta opção, não haverá controle adicional para o produto;
- **Número do lote:** por meio desta, o estoque será controlado pelo número do lote dos produtos.
- **Grade:** através desta, controle o estoque utilizando grade de produto.

Ao selecionar uma das opções acima, o preenchimento destas será realizado na [Central de Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas). Além disso, essas configurações irão impactar nas rotinas de configuração e inicialização do produto na Central, inclusão, alteração e exclusão de itens na Central, cálculo de impostos e geração do XML da NF-e e Faturamento.

O campo **"Local Padrão"** é destinado ao preenchimento de um local, onde o produto em questão será estocado. O local aqui informado será padrão para as movimentações do produto; quando este campo estiver preenchido e a marcação Usa local presente na aba Medidas e Estoque, sub-aba Estoque estiver efetuada, a configuração realizada no parâmetro **"Local Padrão para Pedidos e Notas - LOCALPADRAO"** será desconsiderada.

Informe no campo **"Código Especificador ST"**, o código responsável por especificar a Substituição Tributária referente ao produto em questão. Este campo é participante nas configurações relacionadas à [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado).

**Nota:** de acordo com o [Guia Prático EFD-ICMS/IPI-Versão 3.1.6](http://sped.rfb.gov.br/arquivo/show/7291), o valor do CEST deve conter apenas sete dígitos; quando houver menos dígitos, o **Sankhya Om** sempre adicionará zeros à esquerda.

Os campos % Carga Média Trib. Nacional, % Carga Média Trib. Federal, % Carga Média Trib. Estadual e % Carga Média Trib. Importação presentes nesta aba e na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) devem ser preenchidos com os respectivos percentuais médios de tributação, são informações utilizadas nas configurações pertinentes à [Lei da Transparência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600174-Lei-da-Transpar%C3%AAncia).

Os campos **"Usa data de Fabricação"** e **"Usa data de Validade"** estão relacionados ao controle de estoque de produtos; posto isto, se aplicam à produtos que utilizam controle adicional por número de lote e/ou data de validade (aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional).

**Observação:** para que os produtos sejam controlados por data de fabricação e/ou data de validade, habilite os parâmetros **"Usar data de Fabricação junto com Lote? - LOTEDTFAB"**, **"Usar data de validade junto com Lote? - LOTEDTVAL"** e **"Informações adicionais para Lotes? - LOTEINFO"**. Assim, o sistema procederá com as devidas validações.

Informe no campo **"Código da FCI"** o código gerado para produtos com parcela importada do exterior no site <https://portal.fazenda.sp.gov.br/servicos/fci/Paginas/Servicos.aspx>. Estes códigos estarão no arquivo de retorno gerado por este site. Vale ressaltar que, os dados deste campo terão prioridade sobre os dados configurados no campo **"Código da FCI"** localizado na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos).

No campo **"Grade Produto"** selecione o modelo utilizado caso o **"Controle Adicional**" for por **"Grade"**. Tem-se ainda que se a definição do modelo padrão for definida neste campo, esta configuração será utilizada nas operações de Compra e Venda.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos/informa%C3%A7%C3%B5esporempresa)

### Sub-aba Impostos

Defina no campo **"Enquadrado no Reintegra/Prev."** para quais empresas deseja gerar o registro R2060 do [EFD REINF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) utilizando as opções abaixo: 

- **Gerar:** ao escolher esta opção com o campo **"Cód. Atividade CPRB (Reintegra/Prev.)"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abaimpostos) preenchido, o sistema irá gerar o registro R2060 do EFD-REINF com as informações cadastradas na rotina Cód. Atividades Produtos e Serviços p/ CPRB. Caso o campo Cód. Atividade CPRB (Reintegra/Prev.) esteja em branco, então o sistema irá verificar o campo **"Código Atividade Reintegra/Prev"** também da aba Impostos e buscará as informações na aba [Reintegra/Prev](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abareintegraprevidncia) da [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) para gerar o registro R2060.
- **Não Gerar:** selecionando esta opção, o registro R2060 do EFD-REINF não será gerado mesmo se a marcação **"Enquadrado no Reintegra/Prev."** da aba Impostos estiver habilitada.
- **Em branco:** serão verificadas as configurações para geração do registro R2060 somente da aba Impostos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos/informa%C3%A7%C3%B5esporempresa) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Classificação por Produto

Informe nesta aba, um classificador que necessita estar previamente cadastrado na tela [Classificadores de produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598434-Classificadores-de-Produtos), sendo este responsável por classificar o produto cadastrado.

![Imagem 53: Informe nesta aba, um classificador que necessita estar previamente cadastrado na tela Classificadores de produtos ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4402112293143)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Produtos Alternativos

![Imagem 54: Aba Produtos Alternativos](https://ajuda.sankhya.com.br/hc/article_attachments/4402117294487)

O conceito de Produtos Alternativos é semelhante ao conceito de Família, mas existem algumas diferenças. Os Produtos Alternativos são produtos que podem substituir outros produtos por terem características semelhantes. Usualmente, não são do mesmo fornecedor e apresentam diferenças que afetam o preço, tais como tamanho, qualidade, marca, entre outros.

Além disso, no painel **"Outras Informações"** da [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353),  tem-se a opção **"Produtos Alternativos"** onde será apresentado um pop-up com os possíveis produtos que podem substituir o produto principal.

[GIF animado: Imagem 55: Além disso, no painel "Outras Informações" da Consulta de Produtos , tem-se a opção "Produtos Alternativos" onde será…](https://ajuda.sankhya.com.br/hc/article_attachments/14147354221975)

**Observação:** quando um produto principal estiver cadastrado em um [Grupo de produtos/serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294) com o campo **"Valida Estoque"** definido como **"Pela Empresa, mas aceita"**, o sistema irá apresentar o pop-up para escolha do produto alternativo, não sendo possível efetivar a inserção do produto principal sem estoque na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens).

Produtos de uma mesma família compartilham o mesmo preço. Normalmente são os mesmos produtos com variações em características que não afetam o preço, como cor, voltagem ou outros. Tem-se abaixo um exemplo prático:

- A Geladeira Vermelha Consul e a Geladeira Azul Consul são da mesma família.
- A Geladeira Vermelha Brastemp é um produto alternativo das duas.

O campo **"Referência (PA)"** é preenchido com a referência do produto alternativo. Como o produto alternativo é previamente cadastrado, preenchendo em seu cadastro o campo **"Referência"**, presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), esta informação será apresentada aqui quando o mesmo for vinculado a um produto.

Para adicionar uma prioridade ao produto alternativo, o parâmetro **"Tipo de direção para considerar na visualização de Produtos alternativos - TIPDIRPROALT"** deve estar configurado com a opção **"Unidirecional"**. Deste modo, o campo **"Prioridade dos produtos alternativos"** será apresentado para preenchimento.

O campo **"Quantidade de produto substituído"** corresponde à quantidade de peças necessárias para substituir o produto principal. Se o parâmetro TIPDIRPROALT estiver configurado com a opção **"Bidirecional"**,este campo não será apresentado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Produtos Específicos

Os produtos específicos podem ser denominados como produtos reais, ou seja, cria-se um produto genérico que represente vários outros produtos em rotinas e/ou processos que necessitem unificar as informações. Nesta aba, vincule os produtos específicos ao seu respectivo produto genérico. Assim, pode-se, na execução da análise de giro, levar em consideração o produto genérico consolidando os produtos reais, bem como nas cotações junto aos seus fornecedores.

![Imagem 56: Os produtos específicos podem ser denominados como produtos reais, ou seja, cria-se um produto genérico que represente…](https://ajuda.sankhya.com.br/hc/article_attachments/4402112379287)

No campo **"Produto específico"** indique qual o produto se deseja associar ao produto genérico em questão. Lembrando que é permitido vincular somente produtos específicos que contenham a mesma unidade padrão do produto genérico.

**Nota:** o produto genérico por ser um produto fictício não deve possuir estoque e nem participar de documentos que atualizam livros fiscais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Outros Impostos

Esta aba permite cadastrar outros impostos para o produto, além dos já cadastrados na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos).

![Imagem 57: Esta aba permite cadastrar outros impostos para o produto, além dos já cadastrados na aba Impostos .](https://ajuda.sankhya.com.br/hc/article_attachments/4402112461847)

Informe no campo **"Imposto"** o código do imposto que foi previamente cadastrado na tela de [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025236974-Impostos).

Existe ainda, a discriminação da **"Redução da Base de Imposto"** e o valor da **"Alíquota"**.

**Observação:** quando o [Cadastro do Imposto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos) for por base mensal, não será exibida nesta aba a linha do imposto; caso altere para o valor mínimo, a linha será apresentada na grade.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Alíquota Interna de Destino

Nesta aba, informe a **"UF"**, bem como a **"Alíquota Interna de Destino"** a ela relacionada. Informe também, o percentual de ICMS referente ao **"Fundo de Combate a Pobreza"** e **"Percentual Redução Base Difal"**. Esta aba é participante nas configurações relacionadas à [Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado).

![Imagem 58: Nesta aba, informe a "UF" , bem como a "Alíquota Interna de Destino" a ela relacionada. Informe também, o percentual de…](https://ajuda.sankhya.com.br/hc/article_attachments/4402117371927)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Funções que utilizam E.P.I

Esta aba será apresentada para utilização apenas se sua empresa possuir em sua licença o produto 30407 - CONTROLE DE EPI/W.

![Imagem 59: Esta aba será apresentada para utilização apenas se sua empresa possuir em sua licença o produto 30407 - CONTROLE DE…](https://ajuda.sankhya.com.br/hc/article_attachments/4402112559895)

Um produto é considerado E.P.I - Equipamento de Proteção Individual (Opcional) no sistema, quando informado na tabela de E.P.I por função no [Cadastro de E.P.I por Função](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109273-E-P-I-por-Fun%C3%A7%C3%A3o), ou quando nessa aba forem selecionadas as funções que utilizam o E.P.I.

No lançamento da requisição de um E.P.I, deve ser informado o código do funcionário que utilizará o E.P.I. Todos os produtos devem estar devidamente cadastrados para a função do funcionário em questão.

As devoluções de EPI deverão ser lançadas manualmente como Devolução de Requisição.

A opção **"Devolver"** da seleção de requisição não poderá ser utilizada, só será possível gerar requisição de um E.P.I, se a última requisição já estiver vencida. Se a marcação **"Exige devolução"** estiver efetuada no cadastro de E.P.I, não será possível lançar outra requisição para o mesmo funcionário com o mesmo E.P.I sem antes lançar uma devolução.

Os eventos **"EPI antes do Vencimento"** e **"EPI sem devolução"** solicitarão liberação, ao tentar lançar uma requisição de EPI que exige devolução sem lançar a devolução, ou tentar lançar um EPI sem que o outro esteja vencido.

Quando configurados os campos **"Centro Resultado Inicial"** e **"Centro Resultado Final"**, o sistema gerará a data de vencimento do EPI dependendo da informação dos mesmos.

**Observação:** se o Centro de Resultado informado na nota não estiver em nenhum dos intervalos informados na configuração dos EPIs, não será gravada a movimentação do EPI.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Produtos Equivalentes

Esta aba é utilizada para mapear os produtos da empresa com os produtos da instituição do parceiro, sendo empregada no [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) para identificar os produtos do XML em relação aos produtos do sistema.

![Imagem 60: Esta aba é utilizada para mapear os produtos da empresa com os produtos da instituição do parceiro, sendo empregada no…](https://ajuda.sankhya.com.br/hc/article_attachments/4402112618775)

Informe aqui, a equivalência entre o produto da empresa e o produto de seu fornecedor.

Essa equivalência servirá para que o processo de importação de XML possa acontecer tanto na Central de Compras quanto no Portal de importação de XML. Observe abaixo um exemplo da referida equivalência:

Informações do produto:

Cód. do produto: 1001;

Descrição: DISJUNTOR 220V 10AMP.

Código do produto no fornecedor: DQE1010;

EAN (código de barras) do produto: 7899260108587;

Descrição do produto no fornecedor: DISJ DQE 1P 10A 5/3kA127/220V.

As informações citadas acima servem para encontrar o produto no sistema no momento da importação do XML. Além disso, nessa aba informe o cód. do parceiro fornecedor que possui o código DQE1010 para o produto selecionado, conforme exemplo acima.

---

### Sub-aba Geral

No campo **"Parceiro"** informe o fornecedor ou fabricante do produto.

No campo **"Cód. Produto Equivalente"** será descrito o código do produto, sendo que este poderá ser formado por letras e números, corresponder ao número de fabricação do produto ou de sua identificação no fornecedor.

O sistema sugere a descrição do produto, porém este pode ser alterado através do campo **"Descrição do Produto Equivalente"** para qualquer outro nome, de acordo com a necessidade.

Por meio do campo **"Unidade"**, indique a unidade condizente ao produto em questão.

O **"Cód.Barra DUN 14"** é o nome genérico que, normalmente, se dá ao código de barras EAN 14 (GS1 14) e que é usado na identificação de caixas de despacho ou caixas de distribuição de um determinado produto. O DUN 14 é então representado pelo GTIN 14 que é montado da seguinte forma:

```
Sequencial de Identificação da Unidade Logística + Código EAN 13 sem o Dígito Verificador
+ o Dígito Verificador do DUN 14, correspondendo então a 14 dígitos
```

O que é o Sequencial DUN de Identificação da Unidade Logística?

Uma unidade logística, neste caso, é uma caixa de distribuição de um determinado produto. Suponha-se que uma fábrica produza o Sabonete Maçã cujo código de barras é representado pelo número: 7891234567895 (EAN13). E este Sabonete Maçã é distribuído aos distribuidores em caixas contendo 20 unidades, 50 unidades e 100 unidades.

Então o GTIN 14 para o código de barras DUN 14 será representado da seguinte forma:

Caixa com **20**  unidades: **1**7891234567892

Caixa com **50**  unidades: **2**7891234567899

Caixa com **100** unidades: **3**7891234567896

Onde os números 1, 2 e 3 representam o sequencial de agrupamento do item ou o tipo de unidade logística que está sendo empregada para o Sabonete Maçã. Onde 1 é a caixa com 20 unidades, 2 é a caixa com 50 unidades e 3 é a caixa com 100 unidades.

A quantidade de cada produto dentro de uma caixa de distribuição é determinada pelo fabricante e não precisa seguir o exemplo apresentado acima. No entanto quando um fabricante criar uma representação de GTIN 14 para um determinado produto este precisa ser anunciado aos seus distribuidores para que estes possam carregar suas bases de dados com este novo código, de modo que uma caixa ao chegar ao seu depósito e esta for lida pelos seus equipamentos de decodificação de código de barras seja possível verificar a quantidade de cada produto que está dando entrada em seu depósito.

O campo **"Unidade do Lote"** será preenchido automaticamente com a **"Unidade do Lote"** informada na aba Produtos por Parceiro da tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354).

Os dados do campo **"Multipl. Compra"** estabelecem que um determinado produto para um determinado parceiro sempre deve ser comprado em múltiplos deste valor. Por exemplo, o produto possui Multpl. Compra igual a 10, se após o cálculo da matriz o sistema indicar que precisa comprar 5, precisa-se comprar 10, se indicar para comprar 12, compre 20, ou seja, sempre compre em quantidade múltipla do valor do campo, arredondando para cima.

Esta configuração está relacionada com os campos Sug.Compra Mult.Cpa e Sug.Compra Giro Mult.Cpa no Giro do produto, assim a quantidade de compra será já ajustada e a geração do pedido já leva em consideração esta regra. Na central é feita uma validação na [Grade de Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), para que não seja possível incluir um item com uma quantidade que não atenda a regra acima.

**Nota:** a funcionalidade descrita acima, atende à rotina de geração de pedidos de compra através da [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro); uma segunda maneira de obtê-la, é configurando-se uma [Unidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025241634-Unidades) específica para compras; no Cadastro de Produtos, no campo **"Decimais para quantidade"**, aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abamedidas), informe "0" (zero); na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas), informe a unidade anteriormente cadastrada com seu Multiplicador correspondente e na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), informe esta mesma unidade no campo **"Unid. Compra"**; por fim, na configuração da Análise de Giro, efetue a marcação **"Usar Unidade de Compra?"** presente na sub-aba Outras configurações.

**Observação:** as modificações realizadas na aba [Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosequivalentes) serão validadas pelo sistema, apenas se ocorrerem nos campos Cód. Parceiro, Cód. Produto Equivalente, Controle e Cód. Barras Parceiro, de modo que na tentativa de alteração de algum deles, será apresentada a seguinte mensagem:

**"Já existe um produto equivalente cadastrado para este Parceiro, Produto Equivalente, Controle e Cód. Barras Parceiro."**

Esta validação de alteração dos campos ocorre independente da configuração realizada no parâmetro **"Considerar empresa na importação XML? - CONSEMPIMPXML"**; este parâmetro quando habilitado, faz com que o campo Código Empresa seja exibido nesta aba, de modo que será possível vincular o cadastro do Produto Equivalente em questão à [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) a qual o item pertence.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Tipos de Amostra

Através desta aba, poderão ser geradas amostras para serem coletadas fisicamente, com a finalidade de avaliar as características dos produtos. Para que esta aba seja apresentada é necessário que o parâmetro **"Controle de Laudo de Amostras? - CONTRLAUDOAMOST"** esteja habilitado.

![Imagem 61: Através desta aba, poderão ser geradas amostras para serem coletadas fisicamente, com a finalidade de avaliar as…](https://ajuda.sankhya.com.br/hc/article_attachments/4402117507223)

Informe no campo **"Tipo Amostra"**, o tipo de amostra relacionada ao produto em questão. A informação vinculada neste campo, deverá estar previamente cadastrada na tela [Tipos de Amostra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119013-Tipos-de-Amostra).

Preencha a **"Quantidade"** de amostras para o produto.

Realize no campo **"Fórmula"**, o cadastro da fórmula destinada ao cálculo da amostra. Acionando o botão ![Imagem 62: Realize no campo "Fórmula" , o cadastro da fórmula destinada ao cálculo da amostra. Acionando o botão "Fórmula"…](https://ajuda.sankhya.com.br/hc/article_attachments/16089026776727) **"Fórmula"** localizado à frente do campo, será aberta o pop-up **"Construtor de Expressões"** para montagem da fórmula, onde poderão ser utilizados os campos do cabeçalho das notas e dos itens.

![Imagem 63: Realize no campo "Fórmula" , o cadastro da fórmula destinada ao cálculo da amostra. Acionando o botão "Fórmula"…](https://ajuda.sankhya.com.br/hc/article_attachments/4402112828439)

Defina no campo **"Requisição de Nota de Entrada de PA"**, se serão geradas requisições para Produto acabado. Esta geração poderá ocorrer em duas situações:

- Não gerar de liberações parciais;
- Gerar sempre independente da produção.

Utilizando esta rotina juntamente com a ativação do parâmetro **"Utiliza Status do Lote? - UTILSTATUSLOTE"**, serão disponibilizados na tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota) dois campos que levam em consideração as informações aqui cadastradas, sendo eles **"Status do Lote"** e **"Base Cálc. Amostragem"**; estes dois campos são disponíveis no grid de itens e sua utilização é realizada nas Centrais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Medidas e Estoque

Nesta aba, realize as definições singulares acerca de cada produto, ou seja, se o item será tratado no estoque com base em algum critério e qual será esse critério, qual o peso líquido e bruto do produto, qual coloração será utilizada ao consultá-lo em outras rotinas do sistema, entre outros aspectos. 

| [Sub-aba Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abamedidas) | [Sub-aba Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestoque) |
| --- | --- |
| [Sub-aba Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) | [Sub-aba Cores p/ Consulta de Preços...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacorespconsultadepreoseestoquesctrlp) |

---

![Imagem 64: Sub-aba Cores p/ Consulta de Preços...](https://ajuda.sankhya.com.br/hc/article_attachments/4402112943255)

### Sub-aba Medidas

No campo **"Peso bruto"** será descrito o peso do produto sem desconto, como por exemplo, o peso do produto com a embalagem.

Indique no campo **"Peso líquido"** o peso do produto com desconto. Tem-se como exemplo, o peso de produto sem a embalagem.

O campo **"Registrar peso"** apresenta as seguintes opções:

- **Pela balança:** o peso será obtido por meio de balança (sem digitação do usuário);
- **Balança manual:** o peso poderá ser obtido pela balança, mas o usuário também pode digitá-lo;
- **Manualmente:** o peso será digitado;
- **Não registrar peso:** o produto não necessita de pesagem.

**Nota:** independente da opção Manualmente estar selecionada no campo Registrar Peso, o sistema sempre carregará para a tabela ITE o peso que encontra-se no Cadastro do Produto.

Os dados descritos no campo **"Metros cúbicos"** serão utilizados na rotina de [Formação de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga). Nos movimentos de compra e venda dos produtos mensurados por metro cúbico, o sistema calculará o valor do referido campo nas Centrais, da seguinte forma:

- Se a operação for na unidade principal do produto, o valor do metro cúbico considerado será o informado em seu respectivo campo desta aba, multiplicado pela quantidade;
- Se a operação for realizada utilizando a unidade alternativa do produto, o valor do metro cúbico considerado será o informado na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas), multiplicado pela quantidade.

Exemplo:

Produto X

Unidade principal =  UN

Aba Medidas e Estoque, campo Metro cúbico = 1000

Unidade Alternativa = PC

Aba Unidades Alternativas, campo Metro cúbico = 2000

Sendo negociado uma UN do item, o campo Metro Cúbico será = 1 \* 1000 = 1000;

Sendo negociada uma PC do item, o campo Metro Cúbico será = 1 \* 2000 = 2000.

**Observação:** no faturamento parcial de pedido, o metro cúbico será recalculado proporcionalmente a quantidade. Ou seja, se forem negociados 10 PC's, onde o metro cúbico original é "2000". Faturando-se três peças, o metro cúbico recalculado será 2000 / 10 \* 3 = 600.

O campo **"Quantidade de embalagens"** será preenchido com quantia de embalagens que serão utilizadas para transportar uma unidade do produto. Como por exemplo, um aparelho de som que possui três embalagens (duas com as caixas de som e uma com o aparelho), nesse caso, o campo seria preenchido com o valor 3 (três).

Informe no campo **"Decimais para quantidade"** o número de casas decimais que o sistema aceitará para a quantidade do produto. Ou seja, se por exemplo o produto é vendido em kg o mesmo deverá conter no mínimo duas casas decimais para representar 0,50 kg (meio quilo) ou três casas decimais para representar 0,350 g (trezentos e cinquenta gramas).

> **Importante**: ao cadastrar um produto, é fundamental atentar-se a configurações como **“Unidade alternativa”** e **“Decimais para Quantidade”**, garantindo a correta movimentação de estoque e o pleno cumprimento das obrigações fiscais. Do ponto de vista fiscal, a menor fração permitida para movimentação do produto **deve resultar em um valor unitário mínimo de R$ 0,01**. Isso significa que a combinação entre unidade de medida, quantidade decimal e custo do produto **não pode gerar valores inferiores a um centavo**, conforme exigido pela legislação fiscal vigente.

Através do campo **"Decimais para o valor"** será descrita a quantidade de casas decimais que o sistema aceitará para os valores do produto. Normalmente esta quantidade é de valor 2 (dois) para representar os centavos.

Para configurar casas decimais para venda:

- O sistema sempre utiliza a configuração efetuada no campo Decimais para o valor para lançar o item na venda;
- O parâmetro **"Decimais p/ cálculo de Volume Alternativo. - DECVLRVOLALT"** será utilizado somente quando o cliente trabalhar com unidades alternativas, ou seja, se o produto tiver volume alternativo e a quantidade do volume alternativo for diferente de 1 no lançamento do item.

Para configurar casas decimais para compra:

- Informe no parâmetro **"Decimais para Custo - CUSTODEC"** a quantidade de casas desejadas.

Informe no campo **"Unid. De Medida"**, a unidade de medida que será utilizada para preenchimento dos campos **"Altura"**, **"Largura"** e **"Espessura/Profundidade"**.

O campo **"Qtd. Notas entre laudos internos"** é habilitado pelo parâmetro **"Utiliza Qtd. Notas Entre Laudos Internos? - NFSLAUDOSINT"**, configure aqui a quantidade de notas que poderão ser utilizadas no laudo elaborado.

**Importante:** o laudo só poderá ser lançado pelo MGE em **"Rotinas/Lançamento de laudo para matéria-prima"**, onde a partir do campo **"Nro Único"** serão selecionadas as notas. Esta rotina do MGE possibilita o lançamento e controle de laudos internos de matérias-primas, atendendo a necessidade de certos segmentos de negócios, que precisam de laudo técnico das matérias-primas empregadas em seus produtos, além daquele que é disponibilizado pelos fornecedores. Isto é, precisam de uma Contraprova, que será gerada pelo laudo interno.

Quando habilitado o parâmetro **"Validar M3 por data de entrega? - VALM3DTENT"**, tem a exibição da marcação **"Validar capac. produção diária em M3"**. Quando acionada, o produto estará configurado para participar do controle de produção diária de M3, ou seja, em metros cúbicos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque)

### Sub-aba Estoque

![Imagem 65: Sub-aba Estoque](https://ajuda.sankhya.com.br/hc/article_attachments/4411117676439)

O campo **"Agrupamento mínimo"** comporta os dados pertinentes ao agrupamento mínimo para a venda ou compra do produto, ou seja, a negociação desse produto só poderá ser feita com quantidades múltiplas do valor (4 casas decimais) informado nesse campo. Todavia, se informar o valor 0 (zero), será aceita qualquer quantidade na compra.

Exemplo:

Tem-se o produto "Ovo" com sua Unidade padrão = unidade, é definido um agrupamento mínimo de 12 para o mesmo. Na inserção do item na nota, o campo **"Quantidade"** deverá ser preenchido com um múltiplo de 12.

No campo **"Prazo validade/tolerância"** será descrito o prazo de validade do produto dado em número de dias. Este campo é muito utilizado para produtos perecíveis, que precisam de controle por Data de Validade.

Informe no campo **"Lead time de compra"**, a quantidade de dias que serão considerados para encontrar o estoque mínimo com base no giro diário do produto, que é calculado pela [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro). Estes dados são denominados de Lead time de compra do produto, ou seja, a quantidade de dias entre o pedido de compra e a entrada do produto no estoque. O estoque mínimo deve durar esta quantidade de dias para que não falte o produto no estoque. O valor para esse campo pode ser calculado automaticamente através da tela [Lead Time de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594134-Lead-Time-de-Compra "br.com.sankhya.mgecom.cons.LeadTimeCompra").

Nos campos **"Estoque Mínimo"** e **"Estoque Máximo (Produto)"**  informe a quantidade mínima e máxima que poderá ser armazenada no estoque. Estes controles é de grande importância para informar a necessidade de compra dos produtos no estoque, evitando que falte produtos ou que estes fiquem estocados sem necessidade.

A marcação **"Usa local"** é empregada para definir se o produto é controlado por local ou não. Trabalhando-se com local, é necessário acionar esta marcação.

Existe a influência dos parâmetros **"Valor padrão para campo 'Usa Local' no produto - VLRPADUSALOCAL"** e **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** no controle por local. Quando ambos se encontram habilitados, no procedimento de  inclusão de um novo produto, a marcação Usa local será apresentada ativa.

Se o parâmetro UTILIZALOCAL estiver desligado, o parâmetro VLRPADUSALOCAL é ignorado pelo sistema.

Já os parâmetros **"Locais p/ desconsiderar produtos na explosão do KIT - DESCLOCALKIT"** e **"Controle automático por data validade lote p/ KIT - LOTAUTKIT"**, influenciarão o uso de local da seguinte forma:

- Ao se efetuar a venda, o sistema encontrará o **"Lote"** com a data mais próxima do vencimento, desconsiderando apenas os locais informados no parâmetro DESCLOCALKIT.
- Quando o parâmetro LOTAUTKIT estiver habilitado, o sistema terá um controle automático por data de validade de lote para kit. Efetuando a venda, o sistema localizará o Lote com a data mais próxima do vencimento. Na baixa dos **"Produtos"** componentes do KIT, não sendo encontrada Matéria Prima suficiente, a inclusão do produto acabado não será permitida.

**Observação:** ao ligar o parâmetro **"Valida Local da MP no KIT? - VALLOCKITMP"**, o sistema não permitirá o lançamento de Kit's com produtos que estejam com local 0 quando a marcação Usa local for habilitada.

Quando o campo **"% Aviso Var. Custo"** estiver diferente de zero, significa que, ao efetuar uma compra, o recálculo do custo verificará o valor que está informado neste campo, se este valor for maior que o descrito, o sistema emitirá uma mensagem informando que o valor do custo está maior que o percentual informado.

**Nota:** a marcação **"Imprime laudo por lote"** foi migrada do MGE, assim, no momento, a mesma não possui funcionalidade no **Sankhya Om**. 

Preencha o campo **"% Quebra Técnica"** com até 4 dígitos.

A marcação **"Produto Padrão?"** estará visível quando o parâmetro **"Exibe campo para informar se o produto é padrão - EXIBEPRODPADRAO"** estiver habilitado. Através desta marcação, indique que o produto em questão contém um peso padrão no ato da pesagem.

A marcação **"Calcular Giro pelo Agendador"** quando acionada, definirá que o produto que está sendo cadastrado irá fazer parte da Otimização do Giro, ou seja, durante o cálculo do giro de produtos pela Análise de Giro de Produtos, os produtos que contenham este campo assinalado, serão levados em consideração.

Habilitando a marcação **"Confere por Cód. Barra"**, indica-se que o produto terá sua conferência feita por código de barras na Central - [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas).

A marcação **"Calcula Ruptura de Estoque?"** permitirá que seja realizado o acompanhamento de rupturas dos itens desejados por meio da análise [Ruptura de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line#rupturadeestoque) na tela [Gerente Online](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line), com isso, o sistema irá registrar diariamente se o produto terminou o dia com o saldo zerado.

O campo **"Grupo de Produção"** permite a associação de um produto a um grupo de produção, previamente cadastrado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque)

### Sub-aba Controle Adicional

![Imagem 66: Sub-aba Controle Adicional](https://ajuda.sankhya.com.br/hc/article_attachments/4402113185559)

Para utilização das funcionalidades contidas nesta aba, alguns pontos necessitam ser analisados. Sendo eles:

**1)** O parâmetro **"Utiliza a coluna Controle para controlar o estoque - UTILIZACONTROLE"**, deve estar acionado;

**2)** Após acionar o referido parâmetro, a coluna Controle será apresentada nas Centrais e, nesta aba, será habilitado o campo **"Controlar por"**.

Assim sendo, caso o produto possua um controle adicional de estoque, uma das opções pertinentes ao campo Controlar por deverá ser selecionada. Abaixo aprenda sobre cada uma delas:

- **Grade:** ao selecionar essa opção, é possível escolher um **"Modelo de Grade"**, sendo que este será criado na tela **"Modelo de Grade"**. Assim, será possível selecionar o modelo que será utilizado na grade de produtos.
- **Data de validade:** essa opção fará com que o estoque seja controlado pela data de validade dos produtos. Tem-se como exemplo, as empresas de laticínios que aplicam esta opção no seu controle de estoque para dar saída primeiramente aos seus produtos perecíveis mais antigos.

Quando a Data de Validade dos produtos for menor que a data atual somada à quantidade dos dias definidos no parâmetro **"Mínimo de dias p/validade dos produtos na entrada - MINDIASVALENT"**, o sistema o informará por meio de uma mensagem que a Data de Validade não atende àquela informada no referido parâmetro. Será solicitado a liberação do [Evento 61 - Liberação de data de validade menor que o previsto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049307294-Tipos-de-Libera%C3%A7%C3%A3o-de-Limites#61-Libera%C3%A7%C3%A3odedatadevalidademenorqueoprevistro), sendo que a nota ficará pendente até que o usuário liberador realiza a análise e em seguida, a sua liberação. Lembre-se ainda que é necessário que o parâmetro **"Usar data de validade junto com Lote? - LOTEDTVAL"** esteja ligado, pois apenas assim, o sistema realizará a validação da Data de Validade dos produtos da nota.

- **Número do lote:** através desta opção, o estoque será controlado pelo número do lote dos produtos.

Caso o parâmetro **"Informações adicionais para Lotes? - LOTEINFO"** esteja ativado, trabalhando-se com um produto que possua Controle Adicional por Número de lote, o botão Estrutura será habilitado, e seu acionamento tem como finalidade a inclusão das informações pertinentes à confirmação do lote. Feito isso, ao inserir o produto em questão em uma Nota de Compra, será aberto o pop-up **"Informações de Controle Adicional"** onde, além dos dados correspondentes ao lote, será necessário que informar também o Parceiro.

Quando a marcação **"Atualizar Estoq. a partir da Confirmação"** (no cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)) estiver habilitada e o parâmetro LOTEDTVAL estiver ligado, o pop-up Informações de Controle Adicional não será apresentado no lançamento de uma Nota de Compra.

O lote precisa ser informado na nota quando o produto desta possui a opção Número do lote selecionada, caso contrário, a nota não será confirmada.

O botão **"Estrutura"** será habilitado quando o campo Controlado por estiver configurado com a opção Número do lote e os parâmetros **"Informações adicionais para Lotes? - LOTEINFO"** e **"Utiliza a coluna Local para controlar o estoque? - UTILIZALOCAL"** estiverem ligados; esse botão serve para configurar a estrutura do lote.

- **Lista:** neste caso, o estoque será controlado pela Lista de Opções configurada. Como por exemplo, para que o produto "Botina" tenha seu controle adicional por Lista de numeração, cadastre as numerações possíveis para controle de estoque deste produto, como N° 36, 37, 38, 39, 40. Para mais informações acesse [Inclusão facilitada de itens controlados por lista](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599354-Inclus%C3%A3o-Facilitada-de-Itens-nas-Centrais).
- **Livre:** selecionando esta opção, a empresa poderá utilizar um controle adicional diferente dos demais, a coluna Controle nos itens da nota assumirá a descrição do campo **"Título"** (localizado nesta aba) e ficará livre para digitação.

Para que a conversão da Unidade Alternativa para a Unidade Padrão de um produto ocorra sem impedimentos, trabalhando-se com itens que possuam controle adicional de estoque do tipo Livre ou por Lista, é necessário que a Unidade Alternativa cadastrada para este item, possua também Unidade e Controle devidamente informados.

Quando se tratar de um produto que possua estoque, o tipo de controle adicional de estoque configurado no campo Controlado Por só poderá ser alterado pelo usuário **"0 - SUP"**.

O campo **"Título"** estará habilitado apenas para as opções Lista e Livre, para que se possa digitar o nome do produto que garante sua identificação no estoque. Acessando a opção **"Pesquisar listas cadastradas"** localizada ao lado direito deste campo, será aberto um pop-up de pesquisa contendo as [Listas p/ Controle Adicional de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110193-Listas-p-Controle-Adicional-de-Estoque) cadastradas para seleção.

A nomenclatura do campo **"Controle tipo lista"** da tela [Movimentação Pró-ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295#Movimenta%C3%A7%C3%A3oPr%C3%B3Ativa) do Coletor **"TotalCross"** será definida conforme o inserido no campo Titulo dessa sub-aba. Caso esse campo esteja sem informação, o nome padrão Controle tipo lista será exibido no TotalCross.

Esse campo comporta até 30 caracteres, quando o texto for maior o componente do campo entenderá que o 31º caractere, é habilitado ao se selecionar a opção Lista do campo Controlar Por.

- **Parceiro:** neste caso, é possível ter o controle do estoque por parceiro. Pode-se ter uma ideia desta opção analisando o seguinte exemplo:

Produtos em consignação pertencem à empresa, mas estão estocados com os parceiros.

- **Série:** o estoque será controlado pelo número de série do produto, como por exemplo, na fabricação de computadores, televisores, refrigeradores, aparelhos celulares, entre outros.

No processo conceitual de Controle Adicional por Série, não está previsto o faturamento parcial.

- **Cartão Telefônico:** esta opção é habilitada pelo parâmetro **"Controle de Cartão Telefônico? - CONTROLECARTAO"**, assim como os campos **"Tamanho Lote"** e **"Tamanho Série"**. Esta opção fará o controle das movimentações de Cartões Telefônicos por Número de Série, ocorrendo da seguinte forma:

No campo Tamanho Lote será definido o número de caracteres do campo **"Controle"**, na grade Itens da Central - [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas). Da mesma forma que no campo Tamanho Série, defina o número de caracteres dos campos **"Série Inicial"** e **"Série Final"**. Lembrando que estes campos aparecerão nas Centrais apenas quando o parâmetro CONTROLECARTAO estiver ligado.

- **Sem controle adicional:** com esta opção, não haverá controle adicional para o produto.
- **Grade:** através desta opção, é possível controlar o estoque utilizando grade de produto.

Ao selecionar a opção Grade, será possível escolher o **"Modelo de Grade"** a ser utilizado no controle, bem como, através do botão **"Definir Grade Padrão"** (localizado ao lado do campo Modelo de Grade) definir uma **"Configuração para Compra"** e uma **"Configuração para Venda"**, informando se estes movimentos utilizarão a grade padrão e/ou a grade padrão fechada.

Optando apenas pelo uso da grade padrão para quantidade mínima, será permitido que editar os itens da nota, podendo apenas aumentar a quantidade dos itens nas centrais, não permitindo a exclusão de um item específico da grade, tendo que excluir todos.

Informe no campo **"Lista de Opções"**, as variações do produto de acordo com a configuração efetuada no campo Controlar por.

**Nota:** ao habilitar o parâmetro **"Controla Preços por Controle? - PRECOPORCONT"**, será apresentado um campo na tela de [Tabela de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603854-Tabelas-de-Pre%C3%A7os) com título e tipo de controle indicado nesta tela, assim poderão ser cadastrados diferentes valores para o mesmo produto.

A marcação **"Valida Cód. Barras de Nro Série Global"** quando acionada, indicará que o produto usa série Global. Lembrando que, esta marcação só será exibida se o parâmetro **"Usa Nmero de Srie Global? - USACBGLOBAL"** estiver ligado.

O campo **"Notificação para conferência"** é utilizado na tela de Conferência de Série. Ao fazer a conferência de uma série deste produto o sistema irá mostrar uma mensagem com o texto aqui informado.

A marcação **"Exige Número de série do Fabricante"** estará disponível quando o parâmetro **"Usa nro de série do fabricante - USANSFABRIC"** estiver habilitado. Sendo utilizada para indicar que, ao efetuar a conferência de uma nota de compra de uma série desse produto, será necessário informar também o número de série do fabricante.

Através do campo **"Tipo de série para NF-e"**, indique qual série será apresentada junto com a descrição do item na impressão da nota. Optando pela opção **"Fabricante"**, será impresso o Nro. de série do fabricante. Já para a opção Padrão ou vazio, será impresso o número de série global.

**Observação:** os 4 (quatro) campos descritos acima, fazem parte do [Controle de Produtos com Número de Série Global](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597254-Controle-de-Produtos-com-N%C3%BAmero-de-S%C3%A9rie-Global).

Para que a marcação **"Utiliza SmartCard?"** seja apresentada, o produto deve ser controlado por Série. O comportamento do sistema ao realizar esta marcação, é exposto em detalhes na documentação [Utiliza SmartCard](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599134-Utiliza-SmartCard).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque)

### Sub-aba Cores p/ Consulta de Preços e Estoques (Ctrl+P)

![Imagem 67: Sub-aba Cores p/ Consulta de Preços e Estoques (Ctrl+P)](https://ajuda.sankhya.com.br/hc/article_attachments/4402117677847)

Nesta aba, realize a configuração de cores nos produtos, de modo que estes sejam destacados na tela  [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos); esta configuração é utilizada apenas para personalização de visualização do produto nesta tela.

**Nota:** quando o produto está em promoção ou liquidação, a cor que irá prevalecer é a que está configurada na tela de Consulta de Produtos e não do Cadastro do Produto.

**Observação:** para que as cores de um produto configuradas no **Sankhya Om** sejam as mesmas no MGE, habilite o parâmetro **"Usa cores consulta de produtos compatível MGE? - CORPRODMGECOMP"**, entretanto, se este parâmetro estiver desabilitado, as cores apresentadas na Consulta de Produtos no **Sankhya Om** serão diferentes no MGE.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Componentes

Esta aba é utilizada para se trabalhar com produtos do tipo kit’s, quando a empresa não faz a produção destes, como por exemplo, cestas básicas.

![Imagem 68: Esta aba é utilizada para se trabalhar com produtos do tipo kit’s, quando a empresa não faz a produção destes, como por…](https://ajuda.sankhya.com.br/hc/article_attachments/4402113564951)

A **"Validação de Componentes"** se dará da seguinte forma:

- **Obrigatório:** a quantidade de componentes na Nota poderá ser maior ou igual à informada nesta aba.
- **Opcional:** o sistema não fará a validação dos componentes.
- **Qtd Iguais:** a quantidade de componentes desta aba tem que ser igual à quantidade de componentes que tiver na nota, ou seja, se aqui o componente Arroz tiver 5 kg, então na nota tem que haver para este componente (Arroz) exatamente 5 kg.

Informe no campo **"Matéria-Prima"**, o produto que fará parte do kit como matéria-prima.

O campo **"Referência (MP)"** é preenchido com a referência da matéria-prima. Esta informação é vinculada no campo **"Referência"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), quando a matéria-prima for cadastrada.

A quantidade que será utilizada da matéria-prima será indicada por meio do campo **"Qtd. Mistura"**.

Indique também se a matéria-prima **"Permite variação de controle"** e/ou se a mesma é uma **"MP de transição"**.

Além disso, nesta aba é possível incluir todos os produtos que compõem um Bem. Todos os componentes são produtos e devem ser previamente incluídos no Cadastro de Produtos. Ou seja, o bem inclui seus componentes, como exemplo: o produto Computador possui como componente o produto CD-ROM.

Ao habilitar o parâmetro **"Mostrar o controle na aba de componentes - CONTROLECOMPON"** será disponibilizado o campo **"Controle"** nesta aba, este campo permite definir no cadastro do componente o controle a ser utilizado, sendo que, quando não houver mais estoque o sistema permitirá que seja definido outro controle.

Para configurar o campo Controle é necessário que o produto a ser inserido como componente possua Controle Adicional (aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional)); deste modo, a informação inserida neste campo deverá ser correspondente ao tipo de controle adicional utilizado.

No exemplo abaixo, foi considerado para o produto **"Chapa de Alumínio 2mm"** o tipo de controle adicional por **"Número do lote"**; mediante isto, no campo Controle registre o número do lote equivalente ao mesmo.

![Imagem 69: No exemplo abaixo, foi considerado para o produto "Chapa de Alumínio 2mm" o tipo de controle adicional por "Número do…](https://ajuda.sankhya.com.br/hc/article_attachments/27241467308439)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Disponibilidade diária

Aqui serão cadastradas a Disponibilidade diária e a Disponibilidade diária máxima do produto. Por exemplo, se o produto se tratar de uma máquina que tem capacidade disponível apenas para 16 horas/dia, mas pode vir a ser usada na sua capacidade máxima de 24 horas/dia, dependendo da necessidade. Neste caso, é informado o valor 16 no campo **"Disp. Diária"** e o valor 24 no campo **"Disp. diária máx."**.

![Imagem 70: Aqui serão cadastradas a Disponibilidade diária e a Disponibilidade diária máxima do produto. Por exemplo, se o produto…](https://ajuda.sankhya.com.br/hc/article_attachments/4402114500247)

O campo **"Controle"** tem por característica ser um campo dinâmico, ou seja, ele varia sua descrição conforme o Controle Adicional de Estoque do produto, definido na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque).

No campo **"Local"**, informe o lugar que o produto se encontra disponível.

O período ao qual está sendo registrada a disponibilidade, será informado no campo **"Data do movimento"**. Caso o mesmo não seja preenchido, o sistema informará a data/hora atual.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Combustível

Esta aba é habilitada pela ativação do parâmetro **"Distribuidor de combustível? - COMBUSTIVEL"**.

![Imagem 71: Esta aba é habilitada pela ativação do parâmetro "Distribuidor de combustível? - COMBUSTIVEL" .](https://ajuda.sankhya.com.br/hc/article_attachments/4402118384535)

O campo **"Código ANP"** será preenchido apenas quando se tratar de produtos regulados pela ANP - Agência Nacional do Petróleo. Utilize a codificação de produtos do Sistema de Informações de Movimentação de produtos – SIMP.

No campo **"Autorização do CODIF"** as informações serão descritas quando a UF utilizar o CODIF (Sistema de Controle do Diferimento do Imposto nas Operações com AEAC - Álcool Etílico Anidro Combustível).

#### Seção Gás Liquefeito de Petróleo - GLP

O gás liquefeito de petróleo (GLP), também chamado de gás de petróleo liquefeito (GPL) é uma mistura de gases de hidrocarbonetos utilizado como combustível em aplicações de aquecimento (como em fogões) e veículos. O GLP ou GPL é a mistura de gases condensáveis presentes no gás natural ou dissolvidos no petróleo.

Os campos contidos nesta aba descreverão os percentuais de mistura e o valor de partida do GLP.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba WMS

Nesta aba é possível que se configure qual regra de WMS será utilizada para separação dos produtos e, além disso, permitirá que visualizar os endereços permitidos e proibidos para o produto, assim como o estoque mínimo e máximo do produto em cada endereço.

![Imagem 72: Nesta aba é possível que se configure qual regra de WMS será utilizada para separação dos produtos e, além disso,…](https://ajuda.sankhya.com.br/hc/article_attachments/4402114660375)

Nesta aba, estão disponíveis ainda as seguintes seções:

| [Seção Data de Validade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oDatadeValidade) | [Seção Diversos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oDiversos) |
| --- | --- |
| [Seção Norma de Paletização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Se%C3%A7%C3%A3oNormadePaletiza%C3%A7%C3%A3o) |  |

---

![Imagem 73: Aqui não se pode Incluir endereços. É permitido apenas removê-los.](https://ajuda.sankhya.com.br/hc/article_attachments/27540392620439) Aqui não se pode Incluir endereços. É permitido apenas removê-los.

A marcação **"Armazena por Lote"** leva em consideração principalmente o código do produto que está sendo armazenado e não o lote especifico que o mesmo possui. Quando efetuada, estarão disponíveis os seguintes procedimentos:

- O armazenamento de vários lotes do mesmo produto em um mesmo endereço vazio;
- Completar o endereço com lotes diferentes do mesmo produto;
- Armazenar para picking com lotes diferentes do mesmo produto;
- Ficará impedido de se efetuar a divisão do lote.

O campo **"Regra de WMS"** permite informar qual será a regra de separação do produto. São apresentadas as seguintes opções:

- **Ordem:** quando acionada, ao efetuar a separação, o sistema irá realizar a coleta nos endereços que estiverem com a prioridade preenchida do menor para o maior código, ou seja, fará a ordenação em ordem crescente. Esta configuração é efetuada manualmente pelo usuário, que informará qual endereço deverá ser separado primeiro;
- **FIFO:** realize esta marcação quando desejar que o produto seja controlado pela regra **"Primeiro que entra é o primeiro que sai (First in First out)"**. Para verificar mais informações sobre essa opção, acesse a documentação [Controle de Estoque por FIFO](https://ajuda.sankhya.com.br/hc/pt-br/articles/6734916739607-Controle-de-Estoque-com-FIFO).

Quando a marcação **"Usar controle adicional no WMS"** for acionada, a marcação **"Fragmenta lote no envio para separação"** será automaticamente ativada ao salvar o registro. Isso ocorrerá, pois para produtos controlados pelo WMS e com [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) por **"Número de lote"**, essa configuração deve ser aplicada.

A marcação **"Recuperação de Avaria?"** indica se, em caso de avaria, o produto poderá ou não ser recuperado.

O parâmetro **"Imprimir etiquetas de volume na conferência? - USAIMPRAGRUPMIN"** quando ligado, irá habilitar a marcação **"Imprimir Etiqueta de Volume por Agrupamento Mínimo"**, que quando estiver acionada, o parâmetro **"Imprimir etiquetas de volume na conferência? - IMPETIQVOLCONF"** habilitado e o sistema configurado para trabalhar com WMS, ao efetuar a impressão através do coletor, durante o envio da conferência para a doca de destino, o sistema fará a impressão da quantidade correta, de acordo com o agrupamento mínimo.

Abaixo observe um exemplo:

Tem-se um agrupamento mínimo de 5 produtos e o pedido foi feito com 20 produtos. Ao imprimir as etiquetas, serão geradas 4 etiquetas quando a opção estiver acionada. Estando desabilitada, serão impressas 20 etiquetas.

Ao habilitar a marcação **"Coletar Série na Conferência de Expedição do WMS?"**, o coletor TotalCross irá solicitar os dados de série dos produtos no momento da Conferência de Saída ou Conferência do Pedido por unidade do produto quando o **"Tipo de Separação"** acontecer **"Por Produto"**, ou seja, se a conferência tiver 10 produtos, deve ser informado uma série para cada um deles.

**Nota:** o número da série inserida deve ser alfanumérico, ou seja, uma série com letras e números.

Além disso, caso queira, pode-se também excluir as séries conforme a necessidade. 

Os campos **"Desvio máximo tolerado na conferência da separação"** e **"Desvio mínimo tolerado na conferência da separação"** permitem configurar uma tolerância de desvio de acordo com a unidade do produto no ato da conferência da separação. Deste modo, possibilitando o envio de uma quantidade diferente da que foi solicitada no ato da venda. Para tanto, é necessário que alguns pontos sejam atendidos:

- A unidade utilizada na conferência deve estar previamente configurada;
- A marcação Produto controlado por peso variável localizada nesta mesma aba, deve estar desabilitada.

Informe no campo **"Tamanho médio por peça (metros)"** a quantidade aproximada de metros que a peça irá conter, como por exemplo, o tamanho médio em metros de um rolo de tecido.

#### Seção Data de Validade

O controle de validade é uma ferramenta fundamental para um software de gerenciamento de estoques. Com esta ferramenta é possível controlar desde a entrada até a saída dos produtos que exigem este controle, disponibilizando informações quanto ao Shelf Life do produto em toda a cadeia de abastecimento.

Para que este controle seja efetuado de forma eficiente é necessário que as informações e configurações tenham exatidão, havendo informações divergentes os produtos poderão ter seu controle comprometido e por consequência vencerem no estoque. As informações quanto ao Shelf Life dos produtos devem ser solicitadas aos fornecedores, pois, são estes que detêm os dados corretos e confiáveis.

No campo **"Shelf Life"** informe em dias o prazo de validade dos produtos. É a partir desta informação que o sistema fará todas as validações e críticas, no momento em que for informada a data de fabricação e/ou validade do produto.

O campo **"Shelf Life mínimo para recebimento"** será preenchido com o prazo mínimo (em dias) de recebimento do produto, de acordo com o seu vencimento. Deste modo, a empresa restringe a entrada de mercadoria muito próxima ao vencimento.

De forma similar ao campo anterior, o campo **"Dias para expedição"** comportará o prazo mínimo (em dias) de expedição do produto. Assim, a expedição de uma mercadoria muito próxima ao vencimento será barrada.

Através do campo **"Política p/ dt.val.na estocagem"**, defina como se dará a estocagem do produto nos endereços de armazenagem, de acordo com a sua data de validade dentre as seguintes opções:

- Apenas datas dentro da mesma semana;
- Apenas datas dentro da mesma quinzena;
- Apenas datas dentro do mesmo mês;
- Aceitar datas diferentes;
- Nunca aceitar datas diferentes.

**Notas:**

- As datas de validade são controladas apenas nos endereços de armazenagem (Pulmão), portanto, sempre que o produto der entrada nos endereços de apanha (Picking) sua validade será nula, uma vez que, estes produtos serão automaticamente expedidos primeiro;
- As configurações são realizadas por produto, não sendo possível configurar, por exemplo, um determinado grupo de produtos.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abawms)

#### Seção Norma de Paletização

Quando a marcação **"Exigir Lastro e Camadas"** estiver assinalada, na edição ou inclusão do produto o sistema irá verificar se existe Lastro e Camadas tanto na aba WMS, quanto na aba [Unidades Alternativas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaunidadesalternativas), nesta ordem respectivamente.

Além disso, ao acionar o botão **"Lastro x Camada por Empresa"**, é possível realizar o cadastro das informações de Lastro e Camadas por empresa. Desse modo, ao gerar as tarefas de armazenagem será utilizado o valor do lastro x camada definido pela empresa do Recebimento.

Quando não houver lastro e camadas em nenhuma das abas, a seguinte mensagem será apresentada:

**"O produto X não possui lastro ou camadas informados para sua unidade padrão e uma unidade alternativa."**

Somente na aba WMS:

**"O produto X não possui lastro ou camadas informados para sua unidade padrão."**

Apenas na aba Unidades Alternativas:

**"O produto X não possui lastro ou camadas informados para uma unidade alternativa."**

Para que o sistema realize as validações acima, o parâmetro **"Exigir norma de paletização no WMS? - WMSEXIGENORMPAL"** deve estar habilitado e a marcação Exigir Lastro e Camadas efetivada. Caso o parâmetro se encontre desligado, o sistema não realizará nenhuma validação de Lastro e Camadas.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abawms)

#### Seção Diversos

Esta seção dispõe do campo **"Percentual para separação pulmão (0-100)"**, em que informa-se o percentual a ser considerado pelo sistema, para que o produto em questão seja separado no pulmão, no picking ou em ambos no ato do envio da onda de separação para expedição. Este percentual será aplicado ao estoque máximo cadastrado para o endereço vinculado ao produto, chegando assim, à quantidade de decisão.

Caso a quantidade solicitada no pedido for maior que o valor resultante nessa quantidade de decisão, o sistema irá gerar a tarefa de separação no endereço considerado como pulmão. Se a quantidade no pedido for maior ou igual, será realizada a separação habitual, ou seja, inicialmente o picking do produto será considerada.

Essa separação considera a unidade existente no pulmão em unidades maiores e o restante no picking com uma unidade menor, assim, as devidas conversões de unidade são realizadas. Desta forma, considere o exemplo:

Estoque Mínimo endereço Picking: 200
Estoque máximo endereço Picking: 1001
Percentual para separação pulmão (0-100): 45%
Quantidade de decisão: = 45% x 1001 = 450,45 = 450 (Número inteiro arredondado).

No exemplo, se um pedido de 440 unidades for gerado, a separação ocorrerá no endereço de pulmão do produto, pois a quantidade solicitada foi menor que a quantidade de decisão.

**Importante:** se o resultado do cálculo da quantidade de decisão for composto por casas decimais depois da vírgula (450,45, por exemplo), o sistema fará o arredondamento se o primeiro algarismo após a vírgula é menor que 5, caso afirmativo, este será arredondado pra baixo, ou seja, em um resultado de "**450,45"**, a quantidade decisão será de 450. Caso o primeiro número depois da vírgula seja maior ou igual a 5, o arredondamento será pra cima, ou seja, em um resultado de **"450,65"**, a quantidade decisão será 451.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abawms) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Flex

![Imagem 74: Aba Flex](https://ajuda.sankhya.com.br/hc/article_attachments/4402114740631)

A marcação **"Flex"** deve ser habilitada para que o produto possa ser utilizado no processo de Crédito Flex.

O Crédito Flex é uma forma de Conta Corrente na qual a empresa pode inserir um **"Saldo Disponível"** ao vendedor, dando a ele a faculdade de conceder acréscimos e descontos em suas negociações, em função de um preço base, gerando assim, crédito e/ou débito em sua conta.

Além de definir o produto como Flex, configure nesta aba o máximo de **"Descontos"** e **"Acréscimos Máximos"** que poderão ser concedidos ao produto na negociação.

**Observação:** as configurações de **"% Desconto Máximo"** e **"% Acréscimo Máximo"** definidas aqui, apenas serão utilizadas se não houver registros de **"%Des.Máx"** e **"%Desc.p/ Preço Base"** na grade da parte inferior desta aba.

Tanto o % Desconto Máximo, quanto o % Acréscimo Máximo são aplicados sobre o valor da Tabela de preço de venda (Negociação) e sobrepõem as configurações do [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores).

Para conceder **"Desconto por Quantidade Negociada do Produto"**, configure na grade desta aba, os campos **"Quantidade"**, **"% Desc.Máx"** e **"% Desc.p/Preço base"**.

Informe no campo Quantidade, a porção negociada do produto que permitirá utilizar os percentuais indicados nos campos % Desc.Máx. e % Desc.p/Preço base.

O campo % Desc.Máx irá comportar o percentual de desconto máximo permitido sobre o Preço Base. O Preço Base é o valor da Tabela da Negociação, menos o percentual indicado no campo % Desc.p/Preço base.

Indique no campo % Desc.p/Preço base, o percentual de desconto a ser aplicado no valor da Tabela da Negociação para se chegar ao preço base do Flex. Vale ressaltar que, este percentual não incide sobre o desconto permitido para o vendedor, apenas o % Desconto Máximo permitido, será abatido do saldo do vendedor.

A validação para os Descontos e Acréscimos no valor do produto Flex, terá a seguinte prioridade:

1. Produtos que possuem uma configuração de desconto por Quantidade, na aba Flex do Cadastro de Produtos (grade inferior desta aba);
2. Produtos que estejam configurados para trabalhar com percentual de Descontos e Acréscimos Máximos (na parte superior desta aba logo abaixo do campo Flex);
3. Se não houver descontos e acréscimos configurados na aba Flex, o sistema buscará as referências pra desconto e acréscimo informadas no Cadastros de Vendedores/Compradores.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Formação de Custo/Preço

![Imagem 75: Aba Formação de Custo/Preço](https://ajuda.sankhya.com.br/hc/article_attachments/4402114886551)

No campo **"% Margem de Lucro"** efetue o cadastro da margem de lucro que será calculada para o produto.

Através do campo **"Fórmula de Custo/Preço"** será indicada a fórmula que será utilizada na formação do preço do produto. Esta fórmula deverá estar previamente cadastrada na tela [Fórmulas de Custo/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599874-F%C3%B3rmulas-de-Custo-Pre%C3%A7o).

No campo **"Filtro p/ Cálc.Custo baseado no Financeiro"** será apontado um filtro previamente cadastrado na rotina [Filtro para cálculo CIP (Financeiro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118873-Filtro-para-c%C3%A1lculo-CIP-Financeiros-), para considerar na alocação dos custos aos produtos. Porém, se o produto não tiver uma fórmula de custo/preço informada, o sistema calculará o preço de venda a partir do último custo de reposição, mais a margem de lucro, informada nesta aba. Obtenha maiores informações acessando a documentação do [Cálculo de Custos sem Fórmula de Precificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597894-C%C3%A1lculo-de-Custos-sem-F%C3%B3rmula-de-Precifica%C3%A7%C3%A3o).

#### Parâmetros que influenciam a rotina de atualização de Custo/Preço

**Usar fórmula da empresa? - CUSTOFORMEMP:** este parâmetro definirá o local onde o sistema buscará a Fórmula Custo/Preço para atualização de custos. Quando desligado, o sistema buscará a fórmula informada nesta aba. Quando ligado, será utilizada a fórmula informada na aba [Estoque/Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abaestoquepreo), nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), permitindo uma atualização diferente para cada empresa, de acordo com as fórmulas informadas.

**Custo Por Empresa? - CUSTOPOREMP:** quando acionado, habilita o campo **"Fórmula de Custo/Preço"**, aba Estoque/Preço, nas Preferências da Empresa. Se o referido campo estiver preenchido, no lançamento de uma Nota de Compra o sistema alimentará a Tabela de Preço Padrão (informada também na aba Estoque/Preço), de acordo com a fórmula de precificação definida. Se o campo Fórmula de Custo/Preço estiver em branco o sistema buscará a fórmula informada aqui, para alimentar a Tabela de Preço Padrão, ou caso esta não esteja informada, a Tabela Padrão de código = 0.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Produtos sugeridos para venda

![Imagem 76: Aba Produtos sugeridos para venda](https://ajuda.sankhya.com.br/hc/article_attachments/4402118664087)

Os produtos cadastrados nesta aba serão sugeridos ao vendedor no momento da venda, ao se confirmar a inclusão do item.

No campo **"Produto/Serviço sugerido"** são cadastrados os produtos/serviços que serão sugeridos ao vendedor quando confirmar a inclusão do item na nota/pedido de venda.

**Observação:** quando o produto incluído no campo acima possuir o controle adicional por estoque definido no campo **"Controlar por"** da sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional) desta tela, este não poderá ser selecionado no pop-up **"Produtos sugeridos para venda"** ao clicar no botão ![Imagem 77: Observação: quando o produto incluído no campo acima possuir o controle adicional por estoque definido no campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16089439723543) **"Incluir itens"** na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradedeitens), de forma que, o sistema exibirá a seguinte mensagem:

**"Campo CONTROLE do produto xx - 'descrição do produto' deve ser informado"**

Informe no campo **"Qtd. Sugerida"**, a quantidade sugerida para a venda do produto/serviço sugerido. Esta quantidade poderá ser alterada pelo vendedor quando o sistema efetuar a sugestão.

A marcação **"Multiplica pela Qtd. Vendida"** quando acionada, no momento da sugestão da venda do produto/serviço tem-se como quantidade sugerida a quantidade negociada, multiplicada pela Qtd. Sugerida. Observe um exemplo:

O Produto A tem o Produto B como produto sugerido para venda. O Produto B foi cadastrado com Qtd. Sugerida = 4 e foi efetuada a marcação da opção Multiplica pela Qtd. Vendida. Ao confirmar a inclusão do produto A com a quantidade = 2, tem-se como sugestão de venda o produto B com a quantidade = 8, ou seja, 2 x 4. Sendo que, esta quantidade poderá ser alterada pelo vendedor.

Ao fazer uma venda, onde o produto vendido tenha produtos sugeridos para a venda, será apresentada na Central de Vendas um pop-up com os produtos sugeridos. Na parte inferior deste, tem-se o botão **"Não mostrar novamente"** que, ao ser acionado, os produtos sugeridos não serão mais apresentados em novos lançamentos na inclusão de itens na nota que está sendo incluída. Para que o pop-up volte a aparecer, é necessário fechar a Central e abrí-la novamente.

**Importante:** a rotina de sugestão de produtos na venda, está apta a ser realizada nos seguintes formatos:

1. Inclusão de um único produto via [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas);
2. Inclusão de um único produto via [Carrinho de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos#abaconfiguraodocarrinho);
3. Inclusão de múltiplos produtos via Carrinho de Compras;
4. Inclusão de múltiplos produtos repetidos juntamente à produtos diferentes no Carrinho de Compras;
5. Inclusão de múltiplos produtos diferentes, onde é sugerido o mesmo produto, cada um com sua respectiva sugestão, mesmo que em cada produto a marcação Multiplicar pela Qtd. Vendida esteja ou não realizada.

A coluna Qtd. Sugerida presente no pop-up Produtos sugeridos para venda irá respeitar os decimais para quantidade definidos no Cadastro do Produto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Estoque

![Imagem 78: Aba Estoque](https://ajuda.sankhya.com.br/hc/article_attachments/4402125092247)

No Cadastro do Produto, o controle de estoque envolve duas abas distintas [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque) e Estoque. Os campos contidos aqui, serão exibidos de acordo com as configurações prévias realizadas na aba Medidas e Estoque.

Esta aba apresenta também o estoque mínimo e máximo do produto por empresa. Sendo que, não deve-se confundir estes campos com o estoque mínimo e máximo da aba Medidas e Estoque, que representam o estoque geral por produto.

Estas informações serão úteis na matriz de [Análise de Giro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106673-An%C3%A1lise-de-Giro) do produto, que poderá ser parametrizada para analisar o estoque mínimo e máximo de forma geral por produto (aba Medidas e Estoque) ou analisar o estoque mínimo e máximo do produto por local de armazenagem ou por empresa (aba Estoque).

O **"Código de Barras"** informado nesta aba será utilizado na contagem de estoque do MGE Inventário. Podendo ser calculado através do botão **"Outras Opções..."**, por meio das opções **"Calcular Cód.Barra EAN13 para todos registros (Estoque)"** e **"Calcular Cód.Barra EAN13 p/ todos registros os que não possuam Cód.Barra (Estoque)"**.

**Observação:** se o registro do produto cadastrado vir a ser utilizado no [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056765053), é importante que os códigos aqui inseridos sejam exclusivos, ou seja, cada produto cadastrado, deve possuir o seu próprio código, caso contrário, o sistema utilizará um código aleatório no momento da venda.

Os campos **"Data de Validade"** e **"Data de Fabricação"** são informativos que visam facilitar a análise de estoque dos produtos e serão alimentados se o produto em questão possuir controle adicional por lote e na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral), as marcações **"Utiliza data de Fabricação"** e **"Utiliza data de Validade"** estiverem efetuadas. Estas datas também poderão ser visualizadas na tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos), no painel Detalhes de estoque.

Além disso, ao realizar a impressão de etiquetas se os campos Data de Validade e Data de Fabricação estiverem preenchidos e na tela [Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas) existir um modelo previamente cadastrado, a data de validade e fabricação do produto será apresentada em cada uma das etiquetas.

Os campos **"Parceiro"**, **"Tipo"** e **"Nome Parceiro"** permitem diferenciar quando o estoque for de terceiros.

Nesta aba, o campo **"Controle"** será alterado de acordo com a marcação no campo **"Controlar Por"** da aba Medidas e Estoque, sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional). Cada opção deste campo muda a funcionalidade do campo Controle, segue abaixo os tipos de comportamento:

- **Parceiro:** efetua-se a troca por um campo que executa pesquisas por parceiro;
- **Lote:** tem-se a alteração para um campo de descrição Lote;
- **Data de Validade:** modifica-se para um campo de nomenclatura Data de Validade;
- **Livre:** esse tipo permite determinar o nome do campo da seguinte forma (Título: Nome do Campo), e permite colocar qualquer informação no campo;
- **Lista:** possibilita determinar o nome do campo da seguinte forma (Título: Nome do Campo), e o campo de Opções (são as opções que vão aparecer no campo na aba Estoque);
- **Série:** muda-se para um campo contendo como descrição a Série;
- **Sem controle adicional:** deixa o campo com a descrição Controle e permite o usuário colocar a informação que desejar.
- **Grade:** com essa opção selecionada, será apresentado o botão **"Grade"**. Ao acioná-lo, é possível configurar os itens do controle conforme modelo de grade relacionado ao produto. Ressalta-se que, será possível selecionar apenas uma das opções dos controles. Considere o seguinte exemplo desta configuração:

Na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontroleadicional), configure o campo **"Controlar Por"** com a opção **"Grade"**, informe também o **"Modelo de Grade"**, no nosso exemplo, será utilizado o modelo Cor/Tamanho.

![Imagem 79: Na aba Medidas e Estoque , sub-aba Controle Adicional , configure o campo "Controlar Por" com a opção "Grade" , informe…](https://ajuda.sankhya.com.br/hc/article_attachments/9086244792855)

Com a configuração acima realizada, na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaestoque), acione o botão ![Imagem 80: Com a configuração acima realizada, na aba Estoque , acione o botão "Cadastrar Estoque" , assim, no campo "Controle"…](https://ajuda.sankhya.com.br/hc/article_attachments/16089538666775) **"Cadastrar Estoque"**, assim, no campo **"Controle"** será apresentado o botão **"Grade"**. Acione-o para selecionar a Cor e o Tamanho do produto:

[GIF animado: Imagem 81: Com a configuração acima realizada, na aba Estoque , acione o botão "Cadastrar Estoque" , assim, no campo "Controle"…](https://ajuda.sankhya.com.br/hc/article_attachments/9086307360535)

Agora, clique em **"Confirmar"**, desse modo, o campo Controle será alterado com a informação definida no pop-up. No nosso caso, ele foi modificado para "TAM/COR = TM:M/CR:AZ", indicando que o Tamanho selecionado foi Médio e a Cor configurada foi Azul. 

Para finalizar a configuração, verifique se os campos obrigatórios foram preenchidos e acione o botão **"Salvar"**. Feito isso, os campos serão desabilitados para edição.

Nesta aba é possível utilizar ainda, as seguintes funcionalidades:

### Botão Outras Opções...

Analise aqui as opções contidas no botão ![Imagem 82: Analise aqui as opções contidas no botão "Outras Opções..." , que representam funcionalidades de cunho significativo…](https://ajuda.sankhya.com.br/hc/article_attachments/16089681762455) **"Outras Opções..."**, que representam funcionalidades de cunho significativo para a rotina.

Abaixo a descrição de cada uma delas:

| [Calcular Cód.Barra EAN13 para todos registros (Estoque)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#CalcularC%C3%B3d.BarraEAN13paratodosregistros(Estoque)) |
| --- |
| [Imprimir Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ImprimirEtiquetas) |
| [Calcular Cód.Barra EAN13 p/ todos registros os que não possuam Cód.Barra (Estoque)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#CalcularC%C3%B3d.BarraEAN13p/todosregistrososquen%C3%A3opossuamC%C3%B3d.Barra(Estoque)) |
| [Cadastro Rápido p/ Controle de Grade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#CadastroR%C3%A1pidop/ControledeGrade) |

**Calcular Cód.Barra EAN13 para todos registros (Estoque)**

Esta opção calculará o Cód.Barra EAN13 para esta aba, com isso, espera-se que cada linha do estoque receba um código para permitir que o EAN13 varie por produto/local/controle/empresa. Não há, portanto, sentido no uso do Cód.Produto para compor o EAN13 neste caso, e o sistema não o usará, ou seja, é necessário que o parâmetro **"Base de Cálculo do Cód de Barras EAN13 - EAN13"** possua valor maior ou igual a zero. Usando essa opção, se algum registro de estoque já tiver Cód.Barras cadastrado, ele será recalculado e sobrescrito.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oOutrasOp%C3%A7%C3%B5es...)

**Imprimir Etiquetas**

Quando acionada, é exibido do pop-up **"Impressão de etiquetas"** que comporta os campos para configuração da impressão de etiquetas do estoque. 

![Imagem 83: Quando acionada, é exibido do pop-up "Impressão de etiquetas" que comporta os campos para configuração da impressão de…](https://ajuda.sankhya.com.br/hc/article_attachments/9087467934743)

No campo **"Modelo de Etiqueta"** será informado o modelo de etiqueta configurado previamente na tela [Modelos de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110993-Modelos-de-Etiquetas).

Informe a **"Quantidade"** de etiquetas que serão impressas. O sistema aceitará informar o valor 0 (zero), mas neste caso nenhuma etiqueta será impressa.

Ao ativar a marcação **"Imprimir de acordo com a quantidade em estoque"** será empregada a quantidade do produto em estoque como quantidade de etiquetas a serem impressas.

O preço do produto impresso na etiqueta será o valor informado na **"Tabela de Preços"** preenchida neste campo. Caso não seja informada nenhuma tabela, a etiqueta será impressa sem valor.

A **"Unidade"** alternativa informada neste campo será a unidade impressa na etiqueta para o(s) produto(s) selecionado(s).

Por meio do campo **"Complemento"** será apontado o complemento a ser impresso na etiqueta.

Indique aqui o **"Controle"** que será impresso na etiqueta.

Com a marcação **"Imprimir para todos os produtos selecionados"** habilitada, o sistema irá imprimir etiquetas para todos os estoques de todos os produtos.

Cada produto pode ter 1 ou mais estoques. Acionando a marcação **"Imprimir para todos os itens de estoque selecionados"**, o sistema irá imprimir etiquetas para todos os estoques daquele produto, ou seja, todos os estoques que estão carregados na aba Estoque.

Quando a marcação Imprimir para todos os produtos selecionados está acionada, o sistema habilita o campo **"Empresa Estoque"** para preenchimento. A empresa aqui informada será aplicada na impressão das etiquetas. Quando não indicada, tem-se a impressão de etiquetas de todas as empresas.

**Importante:** para impressão de etiquetas através desta aba, o modelo de etiqueta em questão pode ser configurado utilizando-se das seguintes variáveis:

- **CODVOL** - Volume;
- **PRECO** - Preço;
- **PRECOTABORIGEM** - Preço da tabela origem;
- **CODBARRAEST** - Código de barras do estoque;
- **CODLOCAL** - Cód. Local;
- **NOMELOCAL** - Descrição do local;
- **REFFORN** - Referência do fornecedor;
- **REFERENCIA** - Referência do produto;
- **LOCALIZACAO** - Localização do estoque;
- **CODPROD** - Cód. do produto;
- **DESCRPROD** - Descrição do produto;
- **COMPLDESC** - Complemento do produto;
- **MARCA** - Marca do produto;
- **CONTROLE** - Controle do estoque.

Ao solicitar a impressão das etiquetas, o sistema irá gerar um relatório com os dados selecionados e realizará a impressão na impressora padrão.

Através do parâmetro **"Impressora padrão para imp. etiquetas - IMPPADETIQPROD"** é possível selecionar a impressora que será utilizada na impressão das etiquetas. Este parâmetro contém as seguintes alternativas:

- **Impressora padrão:** neste caso, no campo **"Texto"** será apontado o valor Padrão ou Vazio para que a impressão de etiquetas ocorra através da impressora definida como padrão;
- **Impressora específica:** informe o nome de uma impressora específica para que as etiquetas sejam impressas através da mesma;
- **Permitir escolher impressora:** para que seja possível escolher a impressora, descreva qualquer palavra que não esteja nos casos citados acima.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oOutrasOp%C3%A7%C3%B5es...)

**Calcular Cód.Barra EAN13 p/ todos registros os que não possuam Cód.Barra (Estoque)**

Tem-se o cálculo do Cód.Barra EAN13 somente para os registros de Estoque que não contenham Cód.Barra já cadastrado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oOutrasOp%C3%A7%C3%B5es...)

**Cadastro Rápido p/ Controle de Grade**

Para utilizar esta opção, é necessário que na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#sub-abacontroleadicional), o campo **"Controlar Por"** esteja configurado com a opção **"Grade"**.

Ao acionar esta opção, será apresentado o pop-up **"Cadastro Rápido p/ Controle de Grade**". Nele, é possível configurar os itens do controle de grade relacionado ao produto. 

![Imagem 84: Ao acionar esta opção, será apresentado o pop-up "Cadastro Rápido p/ Controle de Grade ". Nele, é possível configurar…](https://ajuda.sankhya.com.br/hc/article_attachments/9214228151447)

Assim, selecione um ou mais itens do controle de grade e informe a **"Empresa"** e o **"Local"** onde o produto está armazenado.

Pode-se ainda informar os seguintes dados:

| - Parceiro - Tipo - Estoque Mínimo | - Estoque Máximo - Cód. de Barras - Ativo |
| --- | --- |

Caso tenha configurado mais de um item, ao clicar em **"Confirmar"** será gerado um registro para cada variação de produto configurada. Observe:

![Imagem 85: Caso tenha configurado mais de um item, ao clicar em "Confirmar" será gerado um registro para cada variação de produto…](https://ajuda.sankhya.com.br/hc/article_attachments/9214256806295)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Bot%C3%A3oOutrasOp%C3%A7%C3%B5es...)[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Imagem Alternativa

Nesta aba são inseridas as imagens relacionadas aos produtos que serão visualizadas na tela [Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos) por meio do link **"Características"**.

Será possível inserir somente imagens que tenham as extensões **".jpg"**, **".png"**, **".gif"** e **".bmp"**.

Essas imagens também poderão ser importadas através da opção **"Importar Imagens"** quando o botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360049231453-Cadastro-de-Produtos-Bot%C3%B5es-da-Tela#botooutrasopes...) é acionado.

![Imagem 86: Essas imagens também poderão ser importadas através da opção "Importar Imagens" quando o botão Outras Opções... é…](https://ajuda.sankhya.com.br/hc/article_attachments/4402119725463)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Bens

Esta aba é ativada quando a opção **"Imobilizado"** estiver selecionada no campo **"Usado Como"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) do Cadastro do Produto. Além disso, serão cadastradas aqui a estrutura, a taxa de depreciação, as contas contábeis e a especificação do bem.

Além disso, essa aba conta com as seguintes sub-abas:

| [Sub-aba Estrutura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abaestrutura) | [Sub-aba Taxas do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abataxasdoproduto) |
| --- | --- |
| [Sub-aba Contas do produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontasdoproduto) | [Sub-aba Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#botaooutrasopcoes) |  |

---

![Imagem 87: Botão Outras Opções](https://ajuda.sankhya.com.br/hc/article_attachments/4402125495703)

No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral), campo **"Atualização do Bem"**, encontram-se as informações sobre o que deverá ser configurado para o controle de imobilizado.

Detalhes sobre a aquisição dos bens, seus respectivos cálculos considerando sua utilização como Imobilizado, podem ser visualizados no processo de [Compra de Imobilizado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112513-Compra-de-Imobilizado-Melhorias).

### Sub-aba Estrutura

A estrutura é usada para configurar os detalhes ou as informações complementares que distinguirão os bens. Como por exemplo, se o produto for um carro, a estrutura poderá conter cor, placa, tipo, entre outros.

**Título:** o nome do campo. Ex: Cor.

**Ordem:** deverá conter a posição que o campo será apresentado para digitação nas Centrais de Atendimento.

**Tipo:** que tipo de caractere (numérico, texto, data) o campo aceitará no seu preenchimento.

**Tamanho:** determina em números de caracteres o tamanho do campo.

**Lista:** serve para criar uma lista para escolha posterior. Ex: vermelho, verde, azul. Deve-se escrever cada item em uma linha e teclar <ENTER> para saltar para a linha seguinte.

**Observação:** as informações contidas aqui, preencherão o campo **"Descrição do bem"** localizado na sub-aba Bens, aba Geral, que será explanada mais adiante neste documento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

### Sub-aba Taxas do produto

![Imagem 88: Sub-aba Taxas do produto](https://ajuda.sankhya.com.br/hc/article_attachments/4402125523223)

Indique aqui a data e a respectiva taxa de depreciação do bem. Estas informações são fornecidas pelo contador da empresa.

**Notas:**

- A data inicial terá como padrão a data do dia 1º do mês, independente de outra data do mês informada, ou seja, o sistema considera somente mês e ano.
- A taxa é o percentual de depreciação anual do bem informado, que no momento do cálculo da depreciação será dividida por doze (12) para encontrar a taxa mensal. Ela pode variar ao longo do tempo para permitir depreciação acelerada ou para suspender temporariamente a depreciação de um bem de acordo com a legislação vigente.

Esta sub-aba possuem as seguintes funcionalidades:

| [Taxa Fiscal/Contábil Tradicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Sub-aba20TaxaFiscal/Cont%C3%A1bilTradicional) | [Taxa p/Ajuste Lei 11.638](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Sub-abaTaxap/AjusteLei11.638) |
| --- | --- |

---

**Taxa Fiscal/Contábil Tradicional**

Por meio dessa sub-aba, as taxas de depreciação serão calculadas da maneira padrão. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abataxasdoproduto)

**Taxa p/Ajuste Lei 11.638**

Ao preencher esta sub-aba, o sistema atenderá à legislação Fiscal/Contábil Lei 11638, IN SRF 162/1998, que prevê o cálculo da depreciação com base em nova reavaliação e\ou na aquisição pelo prazo de vida útil dos bens.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abataxasdoproduto) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

### Sub-aba Contas do produto

![Imagem 89: Sub-aba Contas do produto](https://ajuda.sankhya.com.br/hc/article_attachments/4402119832727)

| [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaGeral) | [PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaPIS/COFINS) |
| --- | --- |

---

#### Geral

As duas primeiras opções serão utilizadas para registro da **"Depreciação Mensal do Bem"**:

- **Débito**

**Conta Contábil Depreciação:** conta em que será gerado o lançamento da despesa de depreciação na contabilidade Conta de natureza devedora.

**Histórico Conta Contábil:** código de histórico padrão utilizado na contabilização.

- **Crédito**

**Contra-Partida Depreciação:** conta em que será gerado o lançamento da dedução do Ativo Imobilizado na contabilidade Conta de natureza credora.

**Histórico CP Depreciação:** código de histórico padrão utilizado na contabilização.

As duas opções seguintes serão utilizadas para registro da **"Baixa de Depreciação do Bem"**:

- **Débito**

**Conta contábil baixa depreciação:** informe aqui a conta que representa a depreciação acumulada do bem.

**Histórico baixa depreciação:** código de histórico padrão utilizado na contabilização.

- **Crédito**

**Contra partida baixa depreciação:** informe aqui a conta de Custo de Vendas do Ativo Imobilizado.

**Histórico CP baixa depreciação:** código de histórico padrão utilizado na contabilização.

As duas últimas opções serão utilizadas para registro da **"Baixa do Bem"**:

- **Débito**

**Conta contábil baixa bem:** informe novamente a conta de Custo de Vendas do Ativo Imobilizado.

**Histórico baixa bem:** código de histórico padrão utilizado na contabilização.

- **Crédito**

**Contra partida baixa bem:** informe aqui a conta que representa o bem no Ativo Imobilizado.

**Histórico CP baixa bem:** código de histórico padrão utilizado na contabilização.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontasdoproduto)

**PIS/COFINS**

Nesta aba, são inseridas as contas para contabilização do crédito PIS/COFINS do ativo imobilizado.

Informe as Contas Contábeis e Contra-Partidas de Crédito de PIS e COFINS, bem como seus respectivos Históricos.

![Imagem 90: Informe as Contas Contábeis e Contra-Partidas de Crédito de PIS e COFINS , bem como seus respectivos Históricos .](https://ajuda.sankhya.com.br/hc/article_attachments/4402125561111)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abacontasdoproduto) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

### Sub-aba Bens

Nesta aba, deverão ser cadastrados todos os detalhes, conforme definidos na estrutura (caso exista) e demais informações referentes à compra, baixa e depreciação do bem específico.

No campo **"Código do Bem"** informe manualmente o código do Bem.

Esta aba deve ser usada para consulta ou para implantação de bens.

| [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Geralw) | [Depreciações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaDeprecia%C3%A7%C3%A3o) |
| --- | --- |
| [Impostos Recuperáveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaImpostosRecuper%C3%A1veis) | [Taxas Específicas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaTaxasEspec%C3%ADficas) |
| [Contas do Bem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaContasdoBem) | [CIAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaCIAP) |
| [Despesas Vinculadas aos Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaDespesasVinculadasaosBens) |  |

---

![Imagem 91: Despesas Vinculadas aos Bens](https://ajuda.sankhya.com.br/hc/article_attachments/4402125838999)

---

#### Geral

O campo **"Bem atual"** será preenchido com o produto que deu origem ao bem. Abaixo analise um exemplo:

Na compra de uma casa, efetua-se um cadastro desse bem. Após a execução de uma reforma nesta casa, ela passará a ser outro bem, já que o seu valor de mercado aumentará. Sendo assim, deve-se cadastrar outro bem (reforma da casa) e, no referido campo, indica-se a casa que foi cadastrada no momento da compra.

No campo **"Departamento"**, indique o setor ao qual o bem pertence. Departamento é uma nomenclatura adequada ao imobilizado, os departamentos são locais cadastrados na rotina [Locais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602894-Locais). Vale ressaltar que, quando este campo estiver preenchido, ao gerar o [Relatório Contábil do Patrimonial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4447889227415) com a marcação **"Imprimir o departamento nos relatórios analíticos"** habilitada, será apresentado o código e a descrição do departamento em que o Bem se encontra. 

**Observação:** para que o **"Cód. Departamento"** seja preenchido no momento da emissão da baixa do bem, realize as seguintes configurações:

- Nessa sub-aba, preencha o Departamento do bem que será utilizado na operação;
- Em seguida, na tela [Tipo de operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), localize o registro vinculado na nota; este deve estar com a opção **"Baixa/Venda"** do campo **"Atualização do Bem"** selecionada;
- Assim, ao informar o produto imobilizado e realizar a baixa de bens deste na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#bens)/[Central de Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594254-Central-de-Mov-Internas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), seu Departamento será apresentado conforme configurado anteriormente.

O campo **"Data da compra"** comporta o período em que ocorreu a aquisição do bem.

No campo **"Nota de compra"** existe a indicação do número correspondente a Nota Fiscal de compra.

Os dados exibidos no campo **"Dt. baixa"**, tem por finalidade de baixar totalmente o bem, com isto, encerra-se o processo de depreciação.

O número da nota fiscal da baixa será apresentado no campo **"Nf. Baixa"**.

Os dados indicados no campo **"Valor de aquisição"** correspondem ao valor unitário da aquisição do bem.

No campo **"Empresa"** será indicada a instituição da qual o bem foi adquirido. Quando este campo for preenchido, na tela [Ficha Patrimonial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601414) as colunas **"Cód. Proprietário"** e **"Nome Proprietário"** estarão preenchidas com a empresa que constará como proprietária do bem.

Através do campo **"Descrição Utilização do Bem"**, informe uma descrição sucinta da função do bem na atividade do estabelecimento.

O campo **"Util.Imobilizado"** determina qual a funcionalidade do bem dentro da empresa.

Indique por meio do campo **"Tem Créd.PIS/COFINS sobre Dep.mensal"** quais bens possuem crédito de PIS/COFINS em suas parcelas de depreciação.

Nos campos **"Cód.Sit.Tributária PIS"** e **"Cód.Sit.Tributária COFIN"** serão indicadas as regras tributárias do produto/empresa pertinentes a PIS e COFINS.

**Importante:** a tabela de CST de PIS e COFINS possui situações tributárias específicas para Entrada ou para Saída, sendo que esta definição deve ser respeitada com a finalidade de evitar posteriores erros de validação da [EFD - Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607674-EFD-Contribui%C3%A7%C3%B5es). Deste modo, o sistema efetuará a seguinte validação na inclusão de CST, para evitar configurações inconsistentes de alíquotas de PIS e COFINS:

- Quando informada uma CST na faixa de 50 a 98, o **"Tipo"** deverá ser igual à **"Entrada"**;
- Caso seja informada uma CST na faixa de 1 a 49, o Tipo deverá ser igual à **"Saída"**.

No campo **"Alíquota PIS"** será informado o percentual referente à alíquota do imposto.

Informe no campo **"Alíquota COFINS"**, o percentual pertinente a alíquota do imposto.

Ao considerar o campo **"Valor total dos Bens"** tem-se o somatório dos valores dos Bens na nota de aquisição (valor do produto) de acordo com os lançamentos realizados na tela [Vincular despesas ao Bem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595894-Vincular-despesas-ao-Bem).

Em relação ao campo **"Valor total das despesas"** apresenta-se nesse campo, a somatória dos rateios vinculados ao Bem conforme registros contidos na tela Vincular despesas ao Bem.

É possível contabilizar créditos de PIS/COFINS diretamente na aquisição do bem imobilizado, conforme a legislação vigente. Ao cadastrar ou editar um bem, utilize a opção **"Tem Créd. PIS/COFINS sobre Aquisição"** para ativar o controle.

![Imagem 92: É possível contabilizar créditos de PIS/COFINS diretamente na aquisição do bem imobilizado, conforme a legislação…](https://ajuda.sankhya.com.br/hc/article_attachments/36061423892503)

Ao marcar essa opção, informe o número de parcelas para apropriação do crédito (12 ou 48), conforme o tipo de bem.

O sistema irá dividir automaticamente o valor de PIS e COFINS recuperáveis em parcelas mensais, lançando-as de forma individualizada.

Caso o bem seja baixado ou vendido, o saldo de crédito não apropriado será estornado automaticamente.

O usuário é responsável por definir corretamente o tipo de bem e a quantidade de parcelas, conforme a legislação.

Utilize os relatórios e a ficha patrimonial para acompanhar o saldo e as parcelas contabilizadas.

Informe no campo **"Vlr. Parcela Exclusão BC Crédito"** o valor da parcela que se deseja excluir da base de cálculo de crédito.

O campo **"Valor do Bem a ser Depreciado"** será preenchido pelo sistema de acordo com o registro inserido no campo **"Valor atual do bem"** (aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens), sub-aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens), Depreciações), pois se trata do valor do bem a ser depreciado.

**Observação:** o parâmetro **"Permite mesmo código Bem para diferentes produtos? - MESMOBEMDIFPROD"**, quando ativado, permite o cadastro de dois ou mais bens com o mesmo código, desde que sejam produtos diferentes.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)

#### Depreciações

![Imagem 93: Depreciações](https://ajuda.sankhya.com.br/hc/article_attachments/4402119996695)

A data que irá iniciar a depreciação do bem será descrita por meio do campo **"Data inicial"**.

Informe no campo **"Data final"**, a data que irá encerrar o período de depreciação do bem, ou seja, tempo final da vida útil do bem, esta deverá ser informada manualmente, de acordo com a tabela disponível.

Os dados pertinentes ao campo **"Valor atual do bem"**, estão alinhados com a ocorrência de entradas pelo Portal de Compras, pois o mesmo será preenchido de forma automática de acordo com o Valor de Aquisição do bem e terá sempre este valor. Deste modo, este campo não será atualizado pelo sistema.

**Observação:** caso a entrada seja realizada diretamente no Cadastro do Bem, este valor deverá ser informado manualmente, sendo ele o valor bruto do bem, sem deduzir o Valor do Bem a ser Depreciado, uma vez que a depreciação será calculada sobre este valor.

No campo **"Valor depreciado inicial"** aponte o valor que já foi depreciado desde o primeiro cálculo de depreciação acumulado até a referência vigente, de forma manual. Este campo visa atender as empresas que possuem produtos de imobilizado e que adquiriram agora o sistema para ter o controle do que já depreciou para um bem específico.

A marcação **"Tem depreciação"** influencia no cálculo da depreciação mensal, ou seja, o sistema irá depreciar somente os bens com essa marcação acionada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)

#### Impostos Recuperáveis

![Imagem 94: Impostos Recuperáveis](https://ajuda.sankhya.com.br/hc/article_attachments/4402125929623)

Referente à esta, o valor apresentado no campo **"Valor total dos Bens"**, corresponderá ao valor do item na nota somado ao IPI e o ICMS ST, menos os descontos, em que as despesas acessórias serão levadas em consideração.

Os campos **"Valor do ICMS"** e **"Valor crédito ICMS por subst. tributária"** não estarão passíveis para digitação, pois serão os mesmos campos apresentados na sub-aba **"CIAP"**, portanto a alteração destes poderá ser realizada nos referidos campos na aba CIAP, sendo que o campo **"Digitado na compra"** será marcado automaticamente quando estes forem alterados.

**Observação:** ao acionar a marcação **"Somar FCP na Base de Crédito do CIAP?"** da aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#ababens) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), o campo **"Valor do ICMS"** será composto pela soma do valor do FCP Interno e Valor do ICMS.

A considerar os campos **"Cód. Usuário Manut. Compra"** e **"Data Manut. Compra"**, estes serão preenchidos automaticamente assim que for realizada a autorização manual de algum campo relacionado a esta tela, os dados referente a essas alterações ficarão gravados.

Ao realizar a alteração manual das informações carregadas de forma nativa, um pop-up serão exibido com a mensagem:

**"A informação que está sendo alterada tem como origem uma nota fiscal. Deseja realmente realizar alteração?"**

Na contabilização da baixa do bem, o sistema utilizará o Valor total dos Bens subtraindo os valores dos campos Valor do ICMS, Valor crédito ICMS por subst. tributária, **"Valor do PIS na compra"**, e **"Valor da COFINS na compra"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)

#### Taxas Específicas

![Imagem 95: Taxas Específicas](https://ajuda.sankhya.com.br/hc/article_attachments/4402125990167)

As taxas inseridas através desta aba são específicas para o Bem, diferentemente da sub-aba [Taxas do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abataxasdoproduto) que são taxas gerais para todos os bens gerados por aquele produto. Quando inserido um valor aqui, o sistema ignora as informações da sub-aba Taxas do Produto e usa os dados aqui contidos.

No campo **"Data Inicial"**, será informada a data que passará a valer a respectiva taxa. Esta data corresponderá sempre ao 1º dia do mês, devendo ser informado somente o mês e o ano. Sendo esta exclusiva para o bem, será a primeira a ser empregada pelo sistema, caso não exista, ocorrerá a busca pela data informada na sub-aba Taxas do Produto.

O percentual de depreciação anual do bem, será apontado no campo **"Taxa"**, que no momento do cálculo da depreciação será proporcional ao mês. Esta taxa pode variar ao longo do tempo para permitir depreciação acelerada ou para suspender temporariamente a depreciação de um bem específico de acordo com a legislação vigente. Sendo esta pertinente ao bem em referência.

**Observação:** ao preencher os campos da sub-aba Taxa Fiscal/Contábil Tradicional, o sistema utilizará as taxas de depreciação da maneira padrão. E por meio da sub-aba Taxa p/Ajuste Lei 11.638 o sistema atenderá à legislação Fiscal/Contábil Lei 11638, IN SRF 162/1998, que prevê o cálculo da depreciação com base em nova reavaliação e\ou na aquisição pelo prazo de vida útil dos bens.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)

#### Contas do Bem

Através desta aba,  realize a configuração das contas referentes ao bem imobilizado e as contas para contabilização do crédito PIS/COFINS do ativo imobilizado.

![Imagem 96: Através desta aba, realize a configuração das contas referentes ao bem imobilizado e as contas para contabilização do…](https://ajuda.sankhya.com.br/hc/article_attachments/4402120046615)

**Importante:** no **Sankhya Om** realiza-se apenas o cadastro das contas contábeis para o Bem na contabilização da depreciação do imobilizado. A rotina de geração do lote contábil é feita através do MGE.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens)

#### CIAP

![Imagem 97: CIAP](https://ajuda.sankhya.com.br/hc/article_attachments/4402126056343)

Esta aba é usada para controlar os bens imobilizados que dão direito ao crédito de ICMS.

O CIAP – Controle de Crédito de ICMS do Ativo Permanente foi instituído pelo Ajuste SINIEF n.º 08/97, sendo que a partir de 2010 o CIAP deixou de ser complementar passando a integrar o projeto SPED Fiscal através do Ato COTEPE 38/2009, modificado, posteriormente, pelo leiaute determinado no Ato COTEPE 47/2009, com obrigatoriedade de entrega a partir de janeiro/2011 para os contribuintes de ICMS, que apuram créditos de ICMS sobre o Ativo Imobilizado (Ajuste SINIEF 02/2010).

Assim todos os bens e direitos utilizados por uma empresa, para a realização de suas atividades, serão considerados como Ativo Imobilizado. É nesse contexto que o CIAP foi criado, para regulamentar o dispositivo da Lei Complementar no. 87/96 (Lei Kandir), que possibilitou a todos os contribuintes do ICMS a apropriação do crédito nas aquisições de bens destinados ao Ativo Permanente.

Desta forma, todas as operações que envolvam compras, vendas, baixas e transferência de maquinários, equipamentos, veículos, móveis, utensílios e edificações são demonstradas no CIAP.

**Importante:** os campos pertinentes à esta sub-aba só serão habilitados caso o imobilizado (produto) tenha a marcação **"Atualizar CIAP"** na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) do Cadastro do produto.

Para ter este controle, é necessário realizar no sistema a criação do parâmetro **"Quantidade de meses do CIAP - QTDMESESCIAP"**, conforme descrito abaixo, cujo valor será usado no cálculo da data final para o crédito de ICMS de imobilizados, quando for feita compra de bens:

Chave - QTDMESESCIAP;

Descrição - Quantidade de meses do CIAP;

Módulo - Patrimonial;

Menu - Diversas;

Aba - Cálculos;

Tipo - Inteiro;

Inteiro - 48.

**Observação:** ao acionar a marcação **"Somar FCP na Base de Crédito do CIAP?"** da aba [Bens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#ababens) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), o campo **"Valor do ICMS"** será composto pela soma do valor do FCP Interno e valor do ICMS.

Nesta aba, existem as seguintes funcionalidades:

| [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Sub-abaGeral) |
| --- |
| [Crédito Extemporâneo (Registro G126)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#Sub-abaCr%C3%A9ditoExtempor%C3%A2neo(RegistroG126)) |

---

**Geral**

Informe no campo **"Data inicial"**, o período de referência inicial do crédito de ICMS do bem. Sendo que, mesmo que informe-se uma data diferente de 01/XX/XXXX, o sistema sempre ajustará para que a data fique desta forma, ou seja, sempre no primeiro dia do mês.

Através do campo **"Data final"**, informe o período de referência final para crédito de ICMS do bem. Esse período será calculado automaticamente de acordo com os dados informados no campo Data inicial somados ao campo Quantidade de meses.

No campo **"Quantidade de meses"** será indicado o número de meses para diluição do crédito de ICMS, até o final do período.

Indique no campo **"Valor crédito de ICMS"**, o valor total do crédito de ICMS que será aproveitado até o final do período.

O campo **"Vida Útil do Bem (meses)"** comporta o tempo de vida útil do bem, ou seja, o número de meses para sua depreciação.

Informa-se no campo **"Valor Crédito de ICMS sobre Frete"** qual será o valor de Crédito ICMS aplicado sobre o Frete.

O campo **"Tipo de movimentação do bem ou componente"** apresenta as seguintes opções:

- SI - Saldo inicial de bens imobilizados;
- IM - Imobilização de bem individual;
- IA - Imobilização em Andamento - Componente;
- CI - Conclusão de imobilização em Andamento - Bem Resultante;
- MC - Imobilização oriunda do Ativo Circulante;
- BA - Baixa do bem - Fim do período de apropriação;
- AT - Alienação ou Transferência;
- PE - Perecimento, Extravio ou Deterioração;
- OT - Outras Saídas do Imobilizado.

**Importante:** quando o parâmetro **"Utiliza TIPOENTCIAP para geração do SPED - TIPOENTCIAPSPED"** estiver habilitado, durante a geração do SPED o valor informado no campo Tipo de movimentação do bem ou componente será atribuído no arquivo TXT de geração. Caso se encontre desligado, será analisada a Data Inicial do Bem e a Data Atual, calculada a diferença de meses entre as datas e informado **"IM"** caso a diferença seja igual a **"1"**, e sendo diferente de **"1"** será informado **"SI"**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaCIAP)

**Crédito Extemporâneo (Registro G126)**

O registro G126 tem por objetivo discriminar os demais valores a serem apropriados como créditos de ICMS do Ativo Imobilizado que não foram escriturados nos períodos anteriores (extemporâneos), quando a legislação permitir.

![Imagem 98: O registro G126 tem por objetivo discriminar os demais valores a serem apropriados como créditos de ICMS do Ativo…](https://ajuda.sankhya.com.br/hc/article_attachments/4402120114327)

Para geração do registro G126 no [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI), configure os seguintes campos:

Indique no campo **"Número da parcela"**, a numeração pertinente à parcela de apropriação do crédito. Sendo que, informe um valor menor ou igual ao contido no campo **"Quantidade de meses"** da aba Geral descrita anteriormente.

O campo **"Referência p/apropriação"** é alimentado com o Mês/Ano de geração.

No campo **"Base do crédito"** informe o valor da parcela.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#AbaCIAP)

#### Despesas Vinculadas aos Bens

Por meio desta aba, analise os lançamentos realizados na rotina [Vincular despesas ao Bem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595894-Vincular-despesas-ao-Bem) com a finalidade de visualizar de modo simplificado suas respectivas informações.

![Imagem 99: Por meio desta aba, analise os lançamentos realizados na rotina Vincular despesas ao Bem com a finalidade de visualizar…](https://ajuda.sankhya.com.br/hc/article_attachments/4402120137623)

O sistema disponibilizará nesta aba os seguintes campos:

- Código do bem;
- Produto;
- Nro. Único;
- Parceiro;
- Valor Rateio;
- Status do Rateio;
- Dt. Neg.;
- Vlr. Nota;
- Empresa;
- Vlr. do ICMS;
- ICMS sobre o frete;
- Dt. Entrada/Saída.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-ababens) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

#### Botão Outras Opções

![Imagem 100: Botão Outras Opções](https://ajuda.sankhya.com.br/hc/article_attachments/27241467309463)

Informe na opção **"Informar iniciais p/ cód. Bem"**, as iniciais do código do bem, de forma que no momento do cadastro de um bem, o sistema preencherá de imediato essas iniciais no campo código do bem.

Esta funcionalidade somente estará disponível se no botão Configurações da tela, opção Númeração..., a opção **"Numeração automática"** estiver desmarcada. Nestas ocasiões, o campo **"Código do bem"** estará disponível para preenchimento, de modo que o sistema preenche as iniciais que foram configuradas e o usuário consegue inserir mais informações. Quando a Numeração estiver definida como automática, o campo Código do bem não estará disponível para edição.

![Imagem 101: Esta funcionalidade somente estará disponível se no botão Configurações da tela , opção Númeração... , a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/4402127350807)

**Gerar cópias deste bem:** ao clicar no botão **"Gerar Códigos"** será apresentada na grade uma prévia de como será gerada a codificação dos bens inseridos. Ao clicar em **"Concluir"** será feita a inclusão dos bens.

![Imagem 102: Gerar cópias deste bem: ao clicar no botão "Gerar Códigos" será apresentada na grade uma prévia de como será gerada a…](https://ajuda.sankhya.com.br/hc/article_attachments/4402126289559)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#ababens) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Manufatura

Os recursos e componentes já cadastrados no sistema, precisam ser vinculados aos produtos acabados, seguindo sua respectiva estrutura. Este vínculo é realizado através destas sub-abas:

| [Recursos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#recursos) | [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#pesagem) |
| --- | --- |
| [Capacidades por Recurso](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#capacidadesporrecurso) | [Kanban](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#kanban) |
| [Componentes de Manufatura](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#componentesdemanufatura) |  |

---

### Sub-aba Recursos

![Imagem 103: Sub-aba Recursos](https://ajuda.sankhya.com.br/hc/article_attachments/14359489553687)

No campo **"Categoria de Recurso"** indique a categoria de recurso que será aplicada.

O campo **"Quantidade"** será utilizado para informar a porção necessária do recurso para o processamento do produto independente do centro de trabalho.

Através do campo **"Modificador de Capacidade"**, determine **"se"** e **"como"** o recurso modifica a capacidade de um centro de trabalho que esteja processando o produto, de acordo com as seguintes opções:

- **Neutra:** não modificará a capacidade padrão caso ocorra a inclusão de uma quantidade diferente deste recurso.
- **Proporcional:** altera a capacidade proporcionalmente em relação à quantidade alocada, até o teto da capacidade máxima do centro de trabalho. Analise um exemplo:

Se a capacidade padrão é 1000UN/Dia, utilizando 5 recursos deste tipo, então a cada unidade alocada deste recurso aumenta-se a capacidade em 20%.

- **Fator de capacidade:** irá modificar a capacidade de acordo com o fator da quantidade alocada, informada no campo Fator capacidade.

O campo **"Fator de capacidade"** é utilizado para determinar um fator de modificação da capacidade. Observe um exemplo:

Se a capacidade padrão é 1000UN/Dia, empregando 4 recursos deste tipo, conclui-se que cada recurso é responsável por 25% da capacidade. Portanto, se o valor neste campo for 0,5 o sistema vai aumentar a capacidade em 12,5% para cada nova unidade adicionada deste recurso.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamanufatura)

### Sub-aba Capacidades por Recurso

Nesta aba, determina-se capacidades para qualquer categoria de recurso considerando ou não um centro de trabalho.

![Imagem 104: Nesta aba, determina-se capacidades para qualquer categoria de recurso considerando ou não um centro de trabalho.](https://ajuda.sankhya.com.br/hc/article_attachments/14359480090775)

O campo **"Núm. da Regra"** exibirá o código da regra de capacidade que permitirá assim a sua identificação nos processos que forem utilizá-la.

Através do campo **"Categoria de Recurso"** determine uma categoria de recurso para a regra de capacidade configurada.

Utilize o campo **"Capacidade"** para indicar o domínio das regra de capacidade para a produção do produto.

Caso o produto selecionado possua um controle do tipo lista, o campo **"Controle"** será exibido contendo as opções de controle configuradas para o produto. Além disso, a sua descrição estará de acordo com o título do controle em questão.

O centro de trabalho que faz parte da regra de capacidade será indicado no campo **"Centro de Trabalho"**.

A capacidade mínima de operação do centro de trabalho que está processando o produto com aquela categoria de recurso, será indicada por meio do campo **"Capacidade Mínima"**. Caso este campo seja preenchido com o valor "zero", significa que não existe limite inferior.

Por meio do campo **"Capacidade"** é possível determinar a capacidade média de operação do centro de trabalho que está processando o produto com determinado recurso.

Deste mesmo modo, a capacidade máxima de operação do centro de trabalho que está processando o produto com o referido recurso é apontada no campo **"Capacidade Máxima"**. Geralmente essa capacidade tem ligação com o limite de máquinas ou limite de processamento com mão de obra. Ocorrendo deste campo se encontrar configurado com o valor "zero", o sistema utilizará a capacidade máxima do centro de trabalho.

O campo **"Tipo da Capacidade"** contém as seguintes opções:

- **Adicionar/Subtrair:** essa opção soma ou subtrai essa capacidade (capacidade mínima, capacidade padrão e capacidade máxima) à capacidade do centro de trabalho que será utilizado para o processamento desse produto.
- **Total:** essa opção determina que a capacidade configurada será a capacidade do centro de trabalho quando o mesmos estiver processando o produto com aquela categoria de recurso.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamanufatura)

### Sub-aba Componentes de Manufatura

![Imagem 105: Sub-aba Componentes de Manufatura](https://ajuda.sankhya.com.br/hc/article_attachments/14359535925911)

Informe no campo **"Componente de Manufatura"**, o componente que compõe o produto que está sendo apresentado.

No campo **"Quantidade"** é feita a especificação da quantidade do componente informado acima, que irá compor o produto. Assim como o campo anterior, este também é de preenchimento obrigatório.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamanufatura)

### Sub-aba Kanban

Nesta sub-aba, informe no campo **"Unidade de movimentação padrão"** a unidade padrão para movimentações de transferências geradas a partir das Ordens de Produção quando estas possuírem a marcação **"Utiliza kanban"** habilitada nas [Operações de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058460853-Configura%C3%A7%C3%A3o-de-Atividades-Nova#abaoperaesdeestoque) da tela [Processo Produtivo - Nova](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova).

![Imagem 106: Nesta sub-aba, informe no campo "Unidade de movimentação padrão" a unidade padrão para movimentações de transferências…](https://ajuda.sankhya.com.br/hc/article_attachments/14359540095127)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamanufatura) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba 0200 do EFD

Nesta aba serão realizados os cadastros das alíquotas internas que serão utilizadas na geração do campo **"12 - ALIQ\_ICMS"** do Registro 0200 do SPED Fiscal de períodos retroativos.

![Imagem 107: Nesta aba serão realizados os cadastros das alíquotas internas que serão utilizadas na geração do campo "12 -…](https://ajuda.sankhya.com.br/hc/article_attachments/7219394792983)

Assim, preencha os campos **"Data Referência"** e **"Alíquota Interna de ICMS"**. Lembre-se ainda que, caso complete o campo **"Empresa"**, este indicará que a alíquota cadastrada será exclusiva da Empresa informada.

Além disso, para a geração do Registro 0200, e assim, a geração do campo 12 - ALIQ\_ICMS no SPED, o sistema segue uma hierarquia. Observe:

1. Primeiramente, o **Sankhya Om** irá procurar o preenchimento do campo Alíquota Interna de ICMS dessa aba;
2. Não sendo identificado, esta informação será verificada no campo Alíquota Interna de ICMS da aba [Impostos/ informações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostosinformaesporempresa);
3. Em seguida, se o campo da aba acima também estiver vazio, o sistema irá verificar no campo Alíquota Interna de ICMS da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) do desta mesma tela;
4. Por fim, se nenhum dos campos acima estiverem completos, a informação do ICMS será buscada no campo **"Alíq. Interna Destino"** da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS).

**Nota:** quando duas alíquotas que possuam os campos Empresa vazios forem informadas nessa aba, na mesma referência, o sistema utilizará a primeira alíquota cadastrada para levá-la ao Registro 0200 e geração do EFD.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Anexos/Documentos

Esta aba permitirá a realização de upload de documentos/anexos que poderão ser anexados no Cadastro do Produto.

![Imagem 108: Esta aba permitirá a realização de upload de documentos/anexos que poderão ser anexados no Cadastro do Produto .](https://ajuda.sankhya.com.br/hc/article_attachments/4402126697239)

O botão ![Imagem 109: O botão "Visualizar" ficará habilitado sempre que uma das linhas da grade estiver selecionada e permitirá que o anexo…](https://ajuda.sankhya.com.br/hc/article_attachments/16090012376087) **"Visualizar"** ficará habilitado sempre que uma das linhas da grade estiver selecionada e permitirá que o anexo seja visualizado.

O parâmetro **"Guardar os anexos no banco de dados - GUARDAANEXOBD"** flexibiliza o tipo de armazenamento dos arquivos anexados a partir deste recurso, com as seguintes opções:

- **Banco de Dados:** o sistema armazena os arquivos no banco de dados (coluna **"Conteúdo"** da tabela TSIATA);
- **Diretório:** o sistema armazena os arquivos no diretório **"<pasta do usuário>/SankhyaW/Anexos"**. Se este diretório não existir, ele será criado automaticamente pelo sistema, e subpastas serão geradas para organizar os arquivos por ano, mês e dia. Não é possível alterar o local lógico de salvamento dos arquivos ao utilizar esta opção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba IPI por Parceiro

Ao realizar a vinculação de um parceiro e uma alíquota de IPI nesta aba e ao efetuar um lançamento contendo o produto em questão com o parceiro que foi configurado, há a aplicação desta alíquota de IPI no cálculo do IPI.

![Imagem 110: Ao realizar a vinculação de um parceiro e uma alíquota de IPI nesta aba e ao efetuar um lançamento contendo o produto…](https://ajuda.sankhya.com.br/hc/article_attachments/4402126735767)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Unidade de Mov./Armazenagem

Esta aba é responsável pela ligação entre o produto e a(s) unidade(s) de movimentação e armazenagem. Sendo que, cada U.M.A deverá estar previamente cadastrada na tela [Unidades de Movimentação e Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595714-Unidades-de-Movimenta%C3%A7%C3%A3o-e-Armazenagem).

![Imagem 111: Esta aba é responsável pela ligação entre o produto e a(s) unidade(s) de movimentação e armazenagem. Sendo que, cada…](https://ajuda.sankhya.com.br/hc/article_attachments/4402126762391)

No campo **"U.M.A"** será(ão) indicada(s) a unidade(s) de movimentação e armazenagem.

O campo **"Código de Barras"** permite realizar a busca do produto e unidade de movimentação através do seu código de barras no ato da Conferência. Sendo que, é necessário que na [Configuração da Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia) em sua aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia#abageral), o campo **"Buscar código de barras por"** esteja configurado com a opção **"Referência"**.

Informe no campo **"Volume"** a unidade previamente configurada como Unidade Padrão ou Unidade Alternativa do produto.

Caso o campo **"Padrão"** esteja habilitado, fará com que esta unidade de mov./armazenagem seja utilizada como padrão no ato da conferência dos produtos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Rastreamento Por Empresa

Nesta aba, cadastre o rastreamento de estoque por empresa. Essa configuração tem como principal finalidade, realizar a ligação dos impostos de ICMS e ST das notas de entrada com as notas de saída. Além disso, através do rastreamento de estoque, será possível realizar entregas de obrigações acessórias referente ao ressarcimento de ST, como por exemplo a CAT 42.

![Imagem 112: Nesta aba, cadastre o rastreamento de estoque por empresa. Essa configuração tem como principal finalidade, realizar a…](https://ajuda.sankhya.com.br/hc/article_attachments/4402310653591)

Primeiramente, informe no campo **"Cód. Empresa"** a instituição que será rastreada. Estarão disponíveis aqui, somente as empresas que estiverem configuradas com as opções **"Rastrear Doc. Fiscais"** ou **"Rastrear Doc. Fiscais e não Fiscais"** da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), campo **"Rastreamento de estoque"**.

Depois, preencha o campo **"Tipo de Rastreamento"**, de acordo com as seguintes opções:

- Sem rastreamento;
- Rastrear;
- Última compra;
- Rastrear com Controle;
- Rastrear com Local;
- Rastrear com Controle e Local.

**Nota:** as informações pertinentes ao campo Tipo de Rastreamento estão disponíveis no processo de [Rastreamento de Saída](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107993-Rastreamento-de-Sa%C3%ADda).

**Observação:** essa aba também pode ser utilizada para visualizar o processo de rastreamento configurado em outras telas, observe:

- Se o rastreamento for realizado, por meio da tela [Rastrear ST pela Última Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594694) o sistema informará a opção **"Última Compra"**, no campo Tipo de Rastreamento desta aba.
- Caso seja efetuado o rastreamento de forma nativa, ou seja, por meio da tela [Ativar/Reprocessar Rastreamento de Estoque/ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594854), é possível conferir nesta aba o Tipo de Rastreamento selecionado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Aba Controle FCI

![Imagem 113: Para habilitar esta aba, ligue o parâmetro "Usa FCI Junto com Lote?-USAFCIJUNTOLOTE" .](https://ajuda.sankhya.com.br/hc/article_attachments/16082119232151) Para habilitar esta aba, ligue o parâmetro**"Usa FCI Junto com Lote?-USAFCIJUNTOLOTE"**.

![Imagem 114: Para habilitar esta aba, ligue o parâmetro "Usa FCI Junto com Lote?-USAFCIJUNTOLOTE" .](https://ajuda.sankhya.com.br/hc/article_attachments/6141728444823)

O número do FCI vem informado na nota fiscal de entrada e somente poderá ser definido no Cadastro do Produto se a origem do produto estiver definida como 3, 5 ou 8. Desse modo, ao efetuar a entrada da nota no sistema, cadastre nesta aba, os dados de controle de FCI do produto, por meio dos seguintes campos:

- Código da FCI;
- Controle;
- Cód. Empresa;
- Local.

**Nota:** para que o código FCI seja utilizado nas movimentações posteriores, a marcação **"Ativo?"** deve ser efetuada.

![Imagem 115: Nota: para que o código FCI seja utilizado nas movimentações posteriores, a marcação "Ativo?" deve ser efetuada.](https://ajuda.sankhya.com.br/hc/article_attachments/17286471109783)

Deverá ser selecionado ao menos um dos filtros para realizar a seleção dos códigos FCI, isso deve ser feito por meio da opção **"Filtros Rápidos"** encontrada a esquerda da tela, conforme imagem acima, dessa forma caso abra a aba Controle FCI sem ter selecionado nenhum dos filtros rápidos, serão apresentados todos os códigos FCI cadastrados de todas as empresas, ativos e inativos daquele produto selecionado.

Por meio da opção **"Filtros personalizados"** poderão ser determinado filtros considerando os campos da tela e suas ligações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

## Parâmetros utilizados nesta rotina

**Ordenar filtros por ordem alfabética? - ORDENAFILTROS:** este parâmetro quando habilitado fará com que, os filtros personalizados que forem sendo criados, tenham seus nomes apresentados para escolha, em ordem alfabética.

**Modo grade configurável na pesquisa? - CONFMODGRDPESQ:** este parâmetro por padrão, é apresentado desativado; quando ligado, será possível realizar a configuração de ordenação das colunas nos pop-up's de pesquisa disponíveis no sistema, ou seja, pode-se ordenar as colunas da forma desejada, porém a primeira coluna, será a coluna referente ao campo utilizado como pesquisa.

**Observação:** ao visualizar a lista de abas disponíveis desta tela através do ícone ![clip3738](https://ajuda.sankhya.com.br/hc/article_attachments/360061923233) localizado na lateral superior direita, pode fazê-lo de forma ordenada alfabeticamente; este comportamento é atribuído a ativação do parâmetro **"Ordenar abas por ordem alfabética? - ORDENARABAS"**.

**Descrição para Referência - DESCRREF:** este parâmetro deve ser utilizado para alterar a nomenclatura do campo **"Referência"**, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral).

**Descrição para o peso liquido - DESCRPESOLIQ:** este parâmetro permite modificar o nome do campo **"Peso líquido"**, aba [Medidas e estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abamedidaseestoque), sub-aba [Medidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#sub-abamedidas).

**Descrição para Complemento - DESCRCOMPL:** por meio deste é possível mudar a descrição do campo **"Complemento"**, aba Geral.

**Descrição para Local - DESCRLOCAL:** este parâmetro deve ser configurado quando desejar modificar a nomenclatura do campo **"Local Padrão"**, aba Geral.

**Descrição para Localização - DESCRLOCALIZ:** deve ser utilizado para alterar o nome do campo **"Localização"**, aba Geral.

**Descrição para Marca - DESCRMARCA:** este parâmetro é empregado para alterar a descrição do campo **"Marca"**, aba Geral.

**Descrição para Referência - DESCRREF:** por meio deste, será possível modificar o nome do campo **"Referência"**, aba Geral.

**Saída c/Base IPI sem Desconto? - SAIIPISEMDESC:** quando estiver desligado, para movimentos de venda (nota, pedido, devolução), o sistema irá considerar (abater) o Vlr. Desconto do Vlr. Total do Item para cálculo do valor da Base do IPI. Se ligado, a Base do IPI é calculada sem levar em consideração o Vlr. Desconto, ou seja, mesmo que exista Desconto no item, a Base do IPI não será reduzida por esse desconto.

**Usa multipl. de valor so em vendas (ped/notas/dev) - MULTVLRSOVENDAS:** ao habilitá-lo, não será considerado para os pedidos, notas e devoluções de compra o campo Multiplicador para Valor, pois este parâmetro determina que o multiplicador de valor só deve ser usado nos pedidos, notas e devoluções de venda.

**UFs permitem o envio de 8 caracteres na tag cBenef - UFPER8CTAGCBENE:** neste parâmetro serão incluídas no campo **"Texto"**, as UFs que devem preencher com 8 caracteres a tag **<cBenef>** (campo **"Cód. de Benefício Fiscal na UF"**, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) desta tela).

**Nota:** este parâmetro não será aplicado quando tratar-se de empresas do estado do Paraná que são optantes pelo Simples Nacional.

**Validar códigos de barra repetido? - VALCODBARREPET:** ao encontrar-se habilitado, fará com que o sistema não permita a inserção de códigos de barras repetidos no campo **"Cód. de Barras"**, aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaestoque). Por outro lado, estando este parâmetro desabilitado, poderão ser utilizados códigos de barras repetidos para produtos diferentes.

**Observação:** será possível inserir códigos de barras iguais para produtos diferentes, mesmo com o parâmetro habilitado, desde que, os mesmos possuam controles diferentes.

**Copiar Cód. barra do estoque do produto - COPIACODBAREST:** para que este parâmetro funcione corretamente, é necessário que o Produto envolvido na operação possua Controle Adicional e um Código de Barras.

**Limite de tamanho para imagem do produto (KB) - LIMITIMGPROD:** através deste, pode-se configurar o limite do tamanho máximo das imagens utilizadas no Cadastro de Produtos.

**Priorizar Decimais p/ valor. Na central - PRIDVCEN:** ligando este parâmetro, o sistema irá priorizar a configuração das decimais do Cadastro de Produtos ao aplicar arredondamento na visualização das Centrais. Esse parâmetro não afeta os tipos de movimentação **"C-Compra"**, **"O-Pedido de compra"** e **"E-Devolução de compra"**.

**Usa volume lançamento cd. de barras (TGFBAR)? - UTILCODVOLBAR:** ao habilitá-lo, será utilizado o volume informado na aba [Código de Barras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacdigodebarras) do Cadastro de Produtos ao fazer um lançamento do item por Cód. de Barras na Central de Notas.

**Usa decimais p/ qtd. do produto ao validar estoque? - DECQTDPROVALEST:** com este parâmetro ligado, o sistema irá arredondar as casas decimais de acordo com a quantidade dos produtos. Além disso, com esse parâmetro habilitado, o estoque e reserva dos produtos devem ser ajustados para ficar em conformidade com o campo Decimais para quantidade da sub-aba Medidas da aba Medidas e Estoque dessa tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#top)

![Imagem 117: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16089265951767) Acesse também:

[Cadastro de Marcas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602814-Marcas)

[Cadastro de Serviço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o)

[Suporte a Venda de kits de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos)

[Explosão Automática de Lotes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599374-Explos%C3%A3o-Autom%C3%A1tica-de-Lotes)
