---
id: "360045109333"
titulo: "Nota Fiscal Eletrônica e Nota Fiscal Consumidor Eletrônica 4.00"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:55:40Z"
rotulos: ["DUVIDANF", "Configuração", "NF-e", "XML", "SEFAZ", "Nota Fiscal Eletrônica e Nota Fiscal Consumidor Eletrônica 4.00 manual", "Impostos", "NFC-e", "Atualização NF-e e NFC-e 4.00: Configurações e Novidades", "Documentos Eletrônicos"]
---

# Nota Fiscal Eletrônica e Nota Fiscal Consumidor Eletrônica 4.00

A nova versão da NF-e e NFC-e 4.00 foi estabelecida por meio da divulgação da [Nota técnica (2016.002)](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=), tendo em vista a preparação da estrutura para compreensão das atualizações na legislação.

Inicie a utilização do novo layout configurando nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaGeral) (aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)), o campo **"Versão NF-e/NFC-e"**, que deve ser alimentado com a opção **"Versão NF-e e NFC-e 4.00"**.

**Observação:** é de suma importância realizar os testes/homologação em uma base de dados distinta, para só depois utilizar o ambiente de produção.

Acesse os link's abaixo, para conhecer as novas funcionalidade e configurações desta rotina:

| [Acessibilidade nos Portais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#acessibilidadenosportais) |  | [Alterações Relacionadas ao Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#alteraesrelacionadasaopagamento) |
| --- | --- | --- |
| [Indicador de Presença](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#indicadordepresena) |  | [Notas Referenciadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#notasreferenciadas) |
| [Grupo Controle de ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#grupocontroledest) |  | [Rastreabilidade do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#rastreabilidadedoproduto) |
| [Combustíveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#combustveis) |  | [Produtos Sem GTIN](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#produtossemgtin) |
| [Cálculo do FCP (Interno)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#clculodofcpinterno) |  | [Modalidades de Frete](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#modalidadesdefrete) |
| [Placa de Veículo Estrangeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#placadeveculoestrangeiro) |  | [Grupo Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#grupoparcelas) |
| [Utilização de tag’s específicas no XML...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#utilizaodetagsespecficasnoxmlnf-enfc-e4.0) |  | [Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#parmetros) |

## Acessibilidade nos Portais

Foi disponibilizado no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953)/[Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)/[Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593), botão ![Imagem 1: Foi disponibilizado no Portal de Compras / Vendas / Mov. Internas , botão "Outras Opções" , a opção "Conheça as…](https://ajuda.sankhya.com.br/hc/article_attachments/16669498918679) **"Outras Opções"**, a opção **"Conheça as novidades da NF-e e NFC-e versão 4.00"**, que visa propiciar uma forma rápida e direta para se compreender as alterações e configurações pertinentes à nova versão.

![Imagem 2: Foi disponibilizado no Portal de Compras / Vendas / Mov. Internas , botão "Outras Opções" , a opção "Conheça as…](https://ajuda.sankhya.com.br/hc/article_attachments/4415786168215)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Alterações Relacionadas ao Pagamento

Com relação a forma de pagamento, não se encontrará presente no XML desta versão o elemento indicador da forma de pagamento (indPag). Este elemento era alimentado com o valor configurado no cadastro de [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), campo **"Subtipo"**.

No cadastro [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral), campo **"Tipo de pgto para NFC-e / NF-e / CF-e"**, temos a inclusão de dois novos tipos de pagamento. São estes:

- 14 - Duplicata Mercantil;
- 90 - Sem Pagamento.

![Imagem 3: 90 - Sem Pagamento.](https://ajuda.sankhya.com.br/hc/article_attachments/4415787136279)

Além disso, foram incluídas novas formas de pagamento pelo TEF, sendo elas:

- SOROCRED;
- DINERSCLUB;
- ELO;
- HIPERCARD;
- AURA;
- CABA.

![Imagem 4: CABA.](https://ajuda.sankhya.com.br/hc/article_attachments/4415794511767)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Indicador de Presença

Uma nova opção a ser utilizada por vendedores ambulantes foi criada para o indicador de presença do comprador no estabelecimento. Esta nova opção, **"5 - Presencial, fora do estabelecimento"** será configurada no cadastro [Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [NF-e/NFC-E](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), por meio do campo **"Indicador de Presença para NF-e/NFC-e"**.

![Imagem 5: Uma nova opção a ser utilizada por vendedores ambulantes foi criada para o indicador de presença do comprador no…](https://ajuda.sankhya.com.br/hc/article_attachments/4415788118167)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Notas Referenciadas

Passou a ser permitido pela Sefaz o Modelo 02, um novo tipo de modelo de documento a ser referenciado. Temos como exemplo, a nota de devolução que conseguirá referenciar uma nota que não seja NF-e, neste caso, modelo 02.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Grupo Controle de ST

Foram criados novos grupos e novos campos com informações a respeito dos produtos/serviços. Dentre eles, temos o exemplo do **"Grupo das informações para controle da ST"**, composto pelos campos **"CNPJ do Fabricante da Mercadoria"** e **"Indicador de Escala Relevante"**.

Ainda sobre as informações a respeito de ST, foi acrescentado também no grupo do Produto o campo **"Cód. de Benefício Fiscal na UF"**, que deverá ser alimentado com o mesmo código adotado na EFD e outras declarações, para as UFs que o exigem.

![Imagem 6: Ainda sobre as informações a respeito de ST, foi acrescentado também no grupo do Produto o campo "Cód. de Benefício…](https://ajuda.sankhya.com.br/hc/article_attachments/4415805424151)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Rastreabilidade do Produto

Foi elaborado um novo grupo destinado a permitir a rastreabilidade de qualquer produto submetido às regulações sanitárias, além de defensivos agrícolas, produtos veterinários, odontológicos, medicamentos, entre outros. Para isto, no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral), foi disponibilizado a marcação **"Tem Rastro do Lote"**.

![Imagem 7: Foi elaborado um novo grupo destinado a permitir a rastreabilidade de qualquer produto submetido às regulações…](https://ajuda.sankhya.com.br/hc/article_attachments/4415805060631)

Para realizar a marcação Tem Rastro do Lote, se faz necessário que o produto em questão esteja configurado na aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedidaseestoque), sub-aba [Controle Adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#sub-abacontroleadicional), com o campo **"Controlar por"** indicando a opção **"Número do lote"**:

![Imagem 8: Para realizar a marcação Tem Rastro do Lote , se faz necessário que o produto em questão esteja configurado na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4415806035863)

Além disso, os parâmetros **"Usar data de Fabricação junto com Lote? - LOTEDTFAB"** e **"Usar data de validade junto com Lote? - LOTEDTVAL"** devem estar habilitados.

Os campos **"nLote"**, **"qLote"**, **"dFab"** e **"dVal"** que faziam parte do grupo de Medicamentos (med) na versão anterior, agora passaram a fazer parte do grupo de Rastreamento do produto (rastro).

No grupo de Medicamentos foi incluído o campo **"Cód. ANVISA"**, que pode ser configurado no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abamedicamentos).

![Imagem 9: No grupo de Medicamentos foi incluído o campo "Cód. ANVISA" , que pode ser configurado no Cadastro de Produtos , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4415796363031)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Combustíveis

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Combustível](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abacombustvel), foram acrescentados os seguintes campos para os produtos do tipo Combustível:

- Descrição ANP (descAnp);
- Percentual de mistura GLP (pGLP);
- Percentual de mistura de Gás Natural Nacional (pGNn);
- Percentual de mistura de Gás Natural Importado (pGNi);
- Valor de Partida GLP (sem ICMS) (vPart).

![Imagem 10: Valor de Partida GLP (sem ICMS) (vPart).](https://ajuda.sankhya.com.br/hc/article_attachments/4415796525463)

As tag’s <**pGLP**>, <**pGNn**> e <**pGNi**>, serão sempre geradas juntas no XML, desde que alguma delas contenha valor > 0. Para isso, é necessário observar as validações abaixo:

- Informando algum dos percentuais do grupo de Gás Liquefeito de Petróleo - GLP, esses valores devem estar entre 0 e 100;
- O Valor de Partida GLP (sem ICMS), se informado, deve ser maior ou igual à zero;
- A soma dos três percentuais do grupo de Gás Liquefeito de Petróleo - GLP deve totalizar 0 ou 100%.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Produtos Sem GTIN

No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), caso o campo **"EAN/GTIN Produto p/ NF-e"** esteja definido com a opção **"Não informar"**, no XML de NF-e ou NFC-e gerados na versão 4.00, as tag's cEAN e cEANTRIB serão alimentadas com a informação **"SEM GTIN"**.

![Imagem 11: No Cadastro de Produtos , aba Impostos , caso o campo "EAN/GTIN Produto p/ NF-e" esteja definido com a opção "Não…](https://ajuda.sankhya.com.br/hc/article_attachments/4415891035159)

Temos abaixo dois exemplos de trechos de XML. Primeiramente, um produto com o GTIN informado:

```
<prod>

<cProd>88</cProd>

<cEAN>7896755400034</cEAN>

<xProd>Descrição do Produto</xProd>
```

Abaixo, um produto sem o GTIN informado em seu cadastro:

```
<prod>

<cProd>66</cProd>

<cEAN>SEM GTIN</cEAN>

<xProd>Descrição do Produto</xProd>
```

Ainda sobre o Cadastro de Produtos, também na aba Impostos, temos os campos **"CNPJ do Fabricante da Mercadoria"**, **"Cód. de Agregação"**, **"Indicador de Escala Relevante"** e **"Cód. de Benefício Fiscal na UF"**, que podem ser preenchidos diretamente no lançamento de notas na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) (por meio da configuração prévia do [Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)) ou incluídas no próprio Cadastro de Produtos de modo a facilitar o lançamento dos produtos sendo carregadas automaticamente na grade de itens da Central.

**Nota:** quando o campo Indicador de Escala Relevante for configurado com a opção **"Produzido em Escala NÃO Relevante"** e o campo CNPJ do Fabricante da Mercadoria não estiver preenchido, o sistema irá gerar no XML as tag's <indEscala>N<indEscala> e <CNPJFab>00000000000000</CNPJFab> (com zeros) podendo resultar em rejeição ao tentar aprovar a nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Cálculo do FCP (Interno)

O FCP (Valor do Fundo de Combate a Pobreza) caracteriza um acréscimo do ICMS de no máximo 2% nas operações com determinados produtos (estabelecido na legislação de cada estado). Sendo este destinado a amenizar o impacto das desigualdades sociais entre os estados brasileiros.

**Importante:** o cálculo do FCP (interno) não deve ser confundido com o FCP do DIFAL. Sendo que, a base cálculo DIFAL não leva em consideração o FCP.

A modificação principal realizada nesta versão, está relacionada ao cálculo dos valores devidos em decorrência do percentual de ICMS relativo ao Fundo de Combate a Pobreza. Este cálculo será realizado de acordo com as configurações a seguir:

No cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), marque a opção **"Calcular FCP (ICMS/ST) Interno?"**:

![Imagem 12: No cadastro de Tipos de Operação - TOP , aba Impostos , marque a opção "Calcular FCP (ICMS/ST) Interno?" :](https://ajuda.sankhya.com.br/hc/article_attachments/4415899083671)

No cadastro de [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934#abageral), o campo **"% ICMS FCP Interno"** deve apontar o percentual relacionado ao Fundo de Combate a Pobreza:

![Imagem 13: No cadastro de Alíquotas de ICMS , aba Geral , o campo "% ICMS FCP Interno" deve apontar o percentual relacionado ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4415899267991)

Ainda nesta aba, o campo **"Tributação"** deverá estar com uma das seguintes opções selecionadas:

#### Para o cálculo do FCP ICMS:

00        Tributada integralmente

10        Tributada e com cobrança do ICMS por ST

20        Com redução de base de cálculo

51        Com diferimento

70        Com redução de base de cálculo e cobrança do ICMS por ST

90        Outras

#### Para o cálculo do FCP ST:

10        Tributada e com cobrança do ICMS por ST

30        Isenta e não tributada e com cobrança por substituição

70        Com redução de base de cálculo e cobrança do ICMS por ST

90        Outras

Ainda no cadastro de Alíquotas de ICMS, aba [Substituição Tributária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934#abasubstituiotributria), você deve discriminar no campo **"% ST FCP Interno/Coeficiente FECOP"** seu respectivo percentual:

![Imagem 14: Ainda no c adastro de Alíquotas de ICMS , aba Substituição Tributária , você deve discriminar no campo "% ST FCP…](https://ajuda.sankhya.com.br/hc/article_attachments/4415892238359)

Tem-se a criação do campo **"Fórmula para Base de Cálculo do DIFAL"** que está relacionado ao cálculo do DIFAL. A base DIFAL era empregada para o cálculo do Fundo de Combate a Pobreza, atualmente existe uma base específica para o referido cálculo.

**Nota:** o FCP interno não leva em consideração benefícios fiscais na base.

Na grade **"Itens"** da [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras)/[Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)/[Mov. Interna](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas), por meio do botão **"Outras Opções"**, a opção **"Consultar/Alterar Dados do Imposto do Item..."** permite visualizar os valores obtidos com o cálculo do FCP interno.

![Imagem 15: Na grade "Itens" da Central de Compras / Vendas / Mov. Interna , por meio do botão "Outras Opções" , a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/4415884388119)

Também foram adicionados na grade Itens, os campos abaixo, relacionados ao cálculo do ST FCP Interno. 

- Base ST FCP Interno Anterior;
- % ST FCP Interno Anterior;
- Vlr. ST FCP Interno Anterior;

**Observação:** o cálculo do FCP Interno não irá considerar o FCP ICMS no cálculo do FCP ST, sendo portanto, realizado com base na seguinte fórmula:

```
![Imagem 16: Observação: o cálculo do FCP Interno não irá considerar o FCP ICMS no cálculo do FCP ST , sendo portanto, realizado com…](https://ajuda.sankhya.com.br/hc/article_attachments/42310878825623)  FCP ST = (Base FCP * (Percentual FCP/100)) - Valor FCP ICMS
```

Além disso, anteriormente a geração do cálculo do diferencial de alíquota era efetuada somente na geração do livro. Foram criados os campos **"Alíquota de Diferencial"** e **"Valor de Diferencial"** ([Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Consultar/Alterar Dados do Imposto do Item](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#consultaralterardadosdoimpostodoitem)), que comportarão os dados pertinentes a geração do cálculo que será realizada na confirmação do item da nota. Para tanto, é necessário configurar no parâmetro o momento ao qual a geração do cálculo será executada, conforme as opções abaixo:

- **No livro:** O cálculo será realizado somente na geração do livro;
- **Na central:** Será calculado na confirmação do item, e as despesas acessórias na confirmação da nota;
- **Na central e recálculo no livro:** Segue o mesmo comportamento da opção anterior. Porém, quando gerado o livro as notas serão recalculadas.

Na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874), aba [ICMS/IPI/ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874#abaicmsipi), temos a inclusão dos campos **"Vlr. ICMS FCP Interno"** e **"Vlr. ST FCP Interno"**, que irão receber o cálculo do FCP Interno.

![Imagem 17: Na tela Cadastro Livro ICMS/IPI , aba ICMS/IPI/ST , temos a inclusão dos campos "Vlr. ICMS FCP Interno" e "Vlr. ST FCP…](https://ajuda.sankhya.com.br/hc/article_attachments/4415901723543)

Além disso, na tela [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654#abageral), estão disponibilizadas no campo **"Tipo imposto"**, as novas opções para o cálculo do FCP Interno:

![Imagem 18: Além disso, na tela Ajuste da Apuração de ICMS e ICMS ST , aba Geral , estão disponibilizadas no campo "Tipo imposto" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4415886773911)

**Importante:** para que as informações pertinentes às Bases FCP e FCP ST e seus respectivos valores sejam demonstrados no DANFE e no XML, é necessário que nas [Preferências de Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#botooutrasopes), opção **"Complemento para Itens da Nota (Web)"**, as variáveis abaixo sejam selecionadas para uso:

- Base FCP (ICMS);
- Valor FCP (ICMS);
- Base FCP (ST);
- Valor FCP (ST).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Modalidades de Frete

Foram acrescentadas duas novas opções para a modalidades de frete, sendo possível visualizá-las no Rodapé da nota, por meio do campo **"CIF / FOB"**:

![Imagem 19: Foram acrescentadas duas novas opções para a modalidades de frete, sendo possível visualizá-las no Rodapé da nota, por…](https://ajuda.sankhya.com.br/hc/article_attachments/4415895389591)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Placa de Veículo Estrangeiro

Conforme a Nota Técnica 2011.005 disponibilizada no site [www.nfe.fazenda.gov.br](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=), nas operações de comércio exterior cujo transporte seja realizado por veículo estrangeiro, as placas dos veículos devem ser informadas em um dos seguintes formatos:

- XXX999 (Argentina, Paraguai e Uruguai);
- XX9999 (Chile e Uruguai);
- XXXX999 (Colômbia e Uruguai).

Quando a placa não se enquadrar em um destes formatos, seus dados serão apresentados nas informações adicionais da nota fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Grupo Parcelas

O Grupo Duplicata foi renomeado para a descrição Parcelas. Além disso, foram adicionadas algumas observações sobre os seguintes campos obrigatórios:

- **Número da Parcela (tag nDup):** Número de parcelas contendo 3 algarismos sequenciais e consecutivos, por exemplo: 001,002,003.
- **Data de vencimento (tag dVenc):** Data de vencimento (formato AAAA-MM-DD) em ordem crescente, como por exemplo: 2018-06-01, 2018-07-01, 2018-08-01.

**Nota:** o grupo Parcelas será exibido somente quando o parâmetro **"Esconder detalhes do campo Fatura/Duplicata na NFE - ESCDETDUPLNFE"** estiver habilitado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Utilização de tag’s específicas no XML NF-e/NFC-e 4.0

**Importante:** as informações inseridas neste tópico são específicas para os usuários localizados no estado do Rio Grande do Sul, considerando as diretrizes instauradas no Decreto nº 54.308/2018 e na Instrução Normativa RE nº 048/18 que tornam obrigatório o envio das tag’s <pRedBCEfet>, <vBCEfet>, <pICMSEfet> e <vICMSEfet> estando estas vinculadas ao ICMS Efetivo.

Diante do exposto, é relevante mencionar que o ICMS Efetivo tem como finalidade definir o valor do ICMS de acordo com o seu respectivo regime de tributação e que as referidas tag's definem o valor do ICMS em uma operação que considere o consumidor final na qual o imposto não tenha sido calculado.

**Observação:** utiliza-se como imposto não calculado o código **"CST 060 - Tributação ICMS cobrado anteriormente por substituição tributária"**.

Ainda neste contexto, faz-se necessário mencionar as seguintes informações:

- **Tag <pRedBCEfet>:** Trata-se do percentual de redução da base de cálculo efetiva, considerando o percentual de redução, caso submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva <vBCEfet>;
- **Tag <vBCEfet>:** Definida pelo valor da base de cálculo efetiva, sendo o valor da base de cálculo atribuída à operação própria do contribuinte substituído, caso submetida ao regime comum de tributação, obtida pelo produto do Vprod por (1 - pRedBCEfet);
- **Tag <pICMSEfet>:** Refere-se a alíquota do ICMS efetiva, considerando a alíquota do ICMS na operação a consumidor final, caso submetida ao regime comum de tributação;
- **Tag <vICMSEfet>:** Considera o valor do ICMS efetivo, obtido pelo produto do valor contido na tag <pICMSEfet> pelo valor registrado na tag <vBCEfet>, caso submetida ao regime comum de tributação.

**Importante:** esta implementação tem como finalidade adequar o sistema para a geração do XML de acordo com as exigências da SEFAZ/RS.

---

Em relação ao processo para a geração do XML que contemple as obrigatoriedades previstas, é indispensável:

1.  Proceder com as Configurações dos Valores conforme especificações abaixo:

Configuração A - No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos), campo **"Tipo de Substituição"** selecione a opção **"Revenda com subst. tributária (cálculo de Subst. na compra)"**; posteriormente, ainda nesta aba, preencha os campos **"Alíquota Interna de ICMS"** e **"Perc. Red. Base Icms Efetivo"**.

Configuração B - Ainda no Cadastro de Produtos, aba [Impostos/Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa), campo **"Tipo de substituição"**, selecione a opção **"Revenda com subst. tributária (cálculo de Subst. na compra)"**; após este procedimento, considerando esta aba, você deve inserir as informações necessárias nos campos **"Perc. Red. Base Icms Efetivo"** e **"Alíquota Interna de ICMS"**.

**Observação:** para este caso, o parâmetro **"Usa imposto de produtos por empresa? - EMPPRODIMPOST"** deve estar habilitado.

Após realizar estas configurações,  acesse a tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934#abageral), seção **"Informações de ICMS Efetivo"** e registre as devidas informações nos campos **"Perc. Red. Base"** e **"Alíquota Interna (CST 60)"**.

2. Temos abaixo o detalhamento dos cálculos que correspondem aos itens especificados nas Configurações dos Valores:

 No Tipo de Cálculo A, as tag's estão estruturadas da seguinte forma:

- **<vBCEfet> -** Base = Valor Unit. Produto x Quantidade (valores da nota);
- **<pRedBCEfet> -** %Redução de Base = Perc. Red. Base Icms Efetivo (Cadastro de Produtos, aba Impostos);
- **<pICMSEfet> -** Alíquota = Alíquota Interna de ICMS (Cadastro de Produtos, aba Impostos);
- **<vICMSEfet> -** (Base x %Redução) x Alíquota.

No Tipo de Cálculo B, as tag's estão estruturadas da seguinte maneira:

- **<vBCEfet> -** Base = Valor Unit. Produto x Quantidade (valores da nota);
- **<pRedBCEfet> -** %Redução de Base = Perc. Red. Base Icms Efetivo (Cadastro de Produtos, aba Impostos / Informações por empresa);
- **<pICMSEfet> -** Alíquota = Alíquota Interna de ICMS (Cadastro de Produtos, aba Impostos / Informações por empresa);
- **<vICMSEfet>** - (Base x %Redução) x Alíquota.

No Tipo de Cálculo C, as tag's estão estruturadas da seguinte forma:

- **<vBCEfet> -** Base = Valor Unit. Produto x Quantidade (valores da nota);
- **<pRedBCEfet> -** %Redução de Base = Perc. Red. Base (Alíquotas de ICMS, aba Geral);
- **<pICMSEfet> -** Alíquota = Alíquota Interna (CST 60) - (Alíquotas de ICMS, aba Geral);
- **<vICMSEfet> -** (Base x %Redução) x Alíquota.

3. Para a Geração das informações no XML deve-se considerar:

Em relação aos cálculos dos impostos classificados como CST 060, existem tag’s vinculadas ao mesmo que não podem ser geradas considerando o consumidor final, tais como <vBCSTRet>, <pST> e <vICMSSTRet>.

Posto isto, configure o campo **"Valor da ST Anterior no CST 60 do XML de NF-e p/ consumidor final"** localizado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) (sub-aba [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e), aba [Documentos Fiscais Eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos)) para realizar os devidos ajustes, sendo pertinente considerar as opções vinculadas ao referido campo, conforme abaixo:

- **Colocar Valor -** As tag’s serão geradas no arquivo XML independente se o parceiro estiver classificado como consumidor final;
- **Colocar Zero -** Quando o parceiro tratar-se de consumidor final as tag’s no arquivo XML serão geradas com valor zerado.

Para realizar a geração da tag <indFinal> configure o campo **"Classificação ICMS"** ([Cadastro de Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal)), selecionando uma das seguintes opções **"Consumidor Final Não Contribuinte"** ou **"Consumidor Final Contribuinte"**; após isto, deve-se gerar a tag <indFinal> com a opção (1 - Consumidor Final).

**Observação:** considerando que tenham sido realizadas todas as configurações mencionadas anteriormente, deve-se gerar o XML da NF-e por meio do campo **"Gerar XML da NF-e em arquivo para conferência"** localizado no [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela), [Grade - Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo), **"Opções para Nota Fiscal Eletrônica"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)

## Parâmetros

Foi criado o parâmetro **"UFs que omitem o schema NFe 4.0 v1.60B - UFNFEOMITV160B"** por padrão vazio, o mesmo será utilizado para preenchimentos da(s) UF(s) que esteja(m) rejeitando o envido das tag's conforme as últimas alterações da Nota Técnica 2016.002 - V.160.

O preenchimento deste parâmetro deve ser realizado apenas nesta situação (problemas devido a SEFAZ ainda não se encontrar devidamente adequada), nas próximas atualizações deve-se retirar a(s) UF(s) informada(s) no mesmo.

Ao acessar a tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654) e acionar o botão **"NF-e"**, utilizando a opção **"Gerar XML da NF-e em arquivo para conferência"** o sistema procederá com a exportação do arquivo com seus respectivos dados. Ainda neste contexto, em relação ao endereço do parceiro contido no arquivo, é necessário que o parâmetro **"Tamanho do Endereço do Parceiro no TXT - TAMENDCLI"** esteja configurado de forma a definir a quantidade de caracteres que compõem o endereço mencionado. Assim, no campo **"Inteiro"**, deve-se informar o número de caracteres necessários para registrar este endereço completo.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109333-Nota-Fiscal-Eletr%C3%B4nica-e-Nota-Fiscal-Consumidor-Eletr%C3%B4nica-4-00#top)
