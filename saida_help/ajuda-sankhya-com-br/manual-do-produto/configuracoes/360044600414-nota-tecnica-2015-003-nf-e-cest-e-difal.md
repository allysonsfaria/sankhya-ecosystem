---
id: "360044600414"
titulo: "Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:50:03Z"
rotulos: ["Configuração", "NF-e", "Destino", "DIFAL", "XML", "SEFAZ", "Impostos", "Código Especificador ST", "Fundo de Combate a Pobreza", "Interna", "Partilha DIFAL", "UFDESTNFEBENFIS", "UFNFECOMIEHOM", "UFNFESEMCEST", "Nota Técnica 2015.003 - NF-e", "CEST e DIFAL Partilhado manual", "Alterações na Nota Técnica 2015.003: NF-e CEST e DIFAL Partilhado", "CEST"]
---

# Nota Técnica 2015.003 - NF-e, CEST e DIFAL Partilhado

A Nota Técnica 2015.003 (V106) trouxe novas tratativas para NF-e. Para atender a esta norma, fez-se necessário, a alteração do layout da NF-e, para que este receba informações da cobrança de ICMS nas operações interestaduais de vendas a consumidor final – não contribuinte do imposto; além da inclusão do campo para informar o CEST – Código Especificador da Substituição Tributária – permitindo maior controle da Substituição Tributária.

A partir das configurações abaixo, o Sankhya Om estará preparado para emitir NF-e com as tag's do grupo CEST; e do Diferencial de Alíquota das operações interestaduais destinadas a consumidor final - não contribuinte do ICMS. Para tanto, deve-se atentar para as seguintes informações:

| [Configurações iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#configura%C3%A7%C3%B5esiniciais) | [UF's](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#ufs) |
| --- | --- |
| [Cálculos Realizados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#clculosrealizados) | [Emissão da NF-e c/cálculo do ICMS p/ UF...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#emissodanf-ecclculodoicmspufdolocaldeentrega) |
| [Geração dos Livros Fiscais com Parceiro...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#geraodoslivrosfiscaisconsiderandooparceirolocaldeentrega) | [Geração do EFD com o Parceiro "Local de...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#geraodoefdconsiderandooparceirolocaldeentrega) |
| [Emissão do DANFE com os valores do DI...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#emissododanfecomosvaloresdodifal) | [SEFAZ que não exigem o DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#sefazquenoexigemodifal) |

---

### Configurações iniciais

Inicialmente, na tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), nas abas [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos) e [Impostos/ Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa), tem-se o campo **"Código Especificador ST"**, onde você deve informar o código responsável por especificar a substituição tributária referente ao produto em questão.

[GIF animado: Imagem 1: Inicialmente, na tela de Cadastro de Produtos , nas abas Impostos e Impostos/ Informações por empresa , tem-se o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/4415883530007)

Depois, na aba [Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino), informe a **"UF"**, bem como a **"Aliq. Interna de Destino"** a ela relacionada. Preencha também, o campo **"Perc. ICMS Fundo Comb. Pobreza"** com o percentual de ICMS referente ao Fundo de Combate a Pobreza.

![Imagem 2: Depois, na aba Alíquota Interna de Destino , informe a "UF" , bem como a "Aliq. Interna de Destino" a ela relacionada.…](https://ajuda.sankhya.com.br/hc/article_attachments/4415883571991)

Feito isso, na tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934), preencha o campo **"Aliq. Interna Destino"** relacionada a UF e o campo **"% ICMS FCP"**.

![Imagem 3: Feito isso, na tela Alíquotas de ICMS , preencha o campo "Aliq. Interna Destino" relacionada a UF e o campo "% ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/4415899759383)

Agora, na tela [Partilha DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373), cadastre as partilhas referentes ao diferencial de alíquota; preencha a **"Data de Início Partilha"** e o **"Percentual de Partilha DIFAL"**.

![Imagem 4: Agora, na tela Partilha DIFAL , cadastre as partilhas referentes ao diferencial de alíquota; preencha a "Data de Início…](https://ajuda.sankhya.com.br/hc/article_attachments/4415883981975)

Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), tem-se a marcação **"Calcular DIFAL Partilhado"**, que quando realizada, define que para a TOP em questão, o cálculo do diferencial de alíquota partilhado será realizado.

![Imagem 5: Na tela Tipos de Operação - TOP , na aba Impostos , tem-se a marcação "Calcular DIFAL Partilhado" , que quando…](https://ajuda.sankhya.com.br/hc/article_attachments/4415899368471)

Este campo estará habilitado para utilização, apenas se a TOP for do tipo de movimento **"Pedido de Venda"**, **"Venda"**, **"Devolução de Venda"** ou **"Transferência"**.

Na tela **"Configurações » Cadastros » Produtos » Produtos"**, aba **"Impostos"**, marcar a opção **"Calcular DIFAL"**

![Imagem 6: Na tela "Configurações » Cadastros » Produtos » Produtos" , aba "Impostos" , marcar a opção "Calcular DIFAL"](https://ajuda.sankhya.com.br/hc/article_attachments/13642005991191)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### UF's

É possível emitir NF-e's em ambiente de homologação com a devida Inscrição Estadual. Com a Nota Técnica 2015.003, o ambiente de homologação valida a Inscrição Estadual para as Unidades Federativas que não aceitam Inscrições Estaduais Isentas.

Algumas SEFAZ passaram a exigir a Inscrição Estadual em ambiente de homologação; para atender a esta situação, no sistema tem-se o parâmetro **"UFs que exigem Insc. Estad. em homologação - UFNFECOMIEHOM"**, onde você deve informar os Estados que exigem essa informação; logo, para as empresas pertencentes a UF's que estejam listadas neste parâmetro, o sistema irá buscar o valor do CNPJ e IE válidos para essa Empresa/Parceiro, da forma como é feita em ambiente de produção.

Caso tenha-se empresas que sejam pertencentes a UF's que não estejam listadas no parâmetro, o comportamento do sistema não será modificado, ou seja, o campo I.E. ficará em branco na emissão da nota em ambiente de homologação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### Cálculos Realizados

Para realização do cálculo do DIFAL Partilhado, algumas condições devem ser satisfeitas; são elas:

- Deve-se ter uma movimentação do tipo **"Venda"**;
- A marcação **"Calcular DIFAL Partilhado"** (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)) deve estar habilitada;
- O parceiro deve ser classificado como **"Consumidor Final"** (tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), campo **"Classificação ICMS"**).

Com as condições atendidas, serão realizados os seguintes cálculos:

```
                                                                                       ![Imagem 7: Com as condições atendidas, serão realizados os seguintes cálculos:](https://ajuda.sankhya.com.br/hc/article_attachments/42310741290263)
TGFDIN.ICMSDIFALDEST = (TGFDIN.BASE * Alíquota de diferencial) * Percentual da partilha para
o destinatário;

TGFDIN. ICMSDIFALREM = (TGFDIN.BASE * Alíquota de diferencial) - TGFDIN.ICMSDIFALDEST
```

**Código Especificado ST**

Para o preenchimento do campo **"Código Especificador ST"** nos itens da nota, o sistema irá utilizar o valor salvo no campo **"Código Especificador ST"** da aba [Impostos /Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostosinformaesporempresa), da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), para empresa e produto informado; caso não exista, o sistema irá utilizar o valor salvo no campo **"Código Especificador ST"** aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), do Cadastro de Produtos. Se ambos os valores não existirem, o campo Código Especificador ST no item da nota ficará com valor nulo, consequentemente, a tag **<CEST>** não será gerada.

Caso existam UF's que devem ter seu XML sem o CEST, tem-se o parâmetro **"UFs que devem ter XML de NF-e sem o CEST - UFNFESEMCEST"**, onde você deve informar as siglas dos estados separados por vírgula; as empresas pertencentes às UF's informadas no parâmetro, não terão no XML a tag **<CEST>**.

**Cálculo do diferencial de Alíquota**

O diferencial será calculado pela fórmula:

```
![Imagem 8: O diferencial será calculado pela fórmula:](https://ajuda.sankhya.com.br/hc/article_attachments/42310741290263) Alíq. Interna Dest. - Alíquota.
```

O sistema primeiramente tentará buscar a alíquota interna na tabela TGFAID (Aliquota Interna Destino do Produto) para a empresa e produto informados, caso não encontre, tentará buscar a alíquota do ICMS informada no campo **"Alíq. Interna Dest."** do cadastro de Alíquotas de ICMS da regra utilizada para o item da NF-e que está sendo emitida.

**Cálculo do Percentual de Partilha**

O percentual de Partilha será obtido de acordo com a data de emissão da NF-e, respeitando as informações salvas da tabela TGFPDI (Percentuais de Partilha DIFAL). Além disso, pode-se inserir manualmente estas informações por meio da tela [Partilhas DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373) como mencionado acima.

Feitas todas as configurações e cálculos, vejamos um pequeno trecho de um XML gerado:

![Imagem 9: Feitas todas as configurações e cálculos, vejamos um pequeno trecho de um XML gerado:](https://ajuda.sankhya.com.br/hc/article_attachments/4415786446103)

**Cálculo do ICMS para o Fundo de Combate a Pobreza**

- Deve-se ter uma movimentação dos tipos **"Pedido de Venda"**, **"Venda"** ou **"Devolução de Venda"**;
- A marcação **"Calcular DIFAL Partilhado"** (aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), Tipos de Operação - TOP) deve estar habilitada;
- O parceiro deve ser classificado como **"Consumidor Final"** (tela Cadastro de Parceiros, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), campo **"Classificação ICMS"**).

O cálculo será realizado por item da seguinte forma:

```
![Imagem 10: O cálculo será realizado por item da seguinte forma:](https://ajuda.sankhya.com.br/hc/article_attachments/42310741290263) TGFDIN.VLRFCP = TGFDIN.BASE * Perc. ICMS para Fundo Comb. Pobreza
```

**Observação:** para o cálculo, inicialmente o sistema irá buscar o valor do campo **"TGFAID.PERCICMSFCP"** (aba [Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino), tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113)); caso não encontre será buscado o **"TGFICM.PERCICMSFCP"** (cadastro de [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)).

As despesas acessórias também podem incidir no ICMS do Fundo de Combate a Pobreza, da mesma forma que ocorre com o DIFAL. Logo, se houver alguma despesa, seu valor irá incidir sobre o valor total do item.

**Importante:** as situações em que a Alíquota de ICMS é igual a Alíquota Interna de Destino, para o DIFAL não há cálculo, no entanto, caso seja informado o **"Perc. ICMS Fundo Comb. Pobreza"**, será calculado o valor do ICMS para o Fundo de Combate a Pobreza, e todas as tag's pertencentes ao Grupo das vendas interestaduais para consumidor final, não contribuinte do ICMS, serão geradas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### Emissão da NF-e c/cálculo do ICMS p/ UF do Local de Entrega

Dando seguimento às determinações feitas pela Nota Técnica 2015.003, tem-se a geração de NF-e's, onde o cálculo de ICMS para estas é feito considerando a UF (Unidade Federativa) do Local de Entrega. Para que este comportamento ocorra, deve-se atentar para os seguintes pontos:

Na tela de [Cadastros de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos), o campo **"CPF/CNPJ"** deve estar devidamente informado; nele poderá ser informado um máximo de 14 dígitos. Além do campo CPF/CNPJ, o campo **"Cód. Cidade"** uma vez inserido, não poderá ser modificado.

Dentro deste comportamento, tem-se a Geração do DIFAL considerando o Contato do Local de Entrega. Na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), tem-se o campo **"Cód. Contato Entrega"**, onde informa-se o contato correspondende ao Local de Entrega do Parceiro. Esta informação poderá ser preenchida apenas para operações de venda a Consumidor Final não Contribuinte do ICMS.

**Importante:** quando o campo Cód. Contato Entrega estiver preenchido, as regras fiscais para busca da alíquota do ICMS e o devido cálculo do ICMS Próprio da operação, bem como para o cálculo do DIFAL (se for o caso), serão regidas pela "UF Emitente x UF Local de Entrega" (campos citados à seguir). Se o referido campo não estiver preenchido, o sistema irá seguir as regras normais de tributação para o ICMS Próprio e DIFAL.

Quando a nota possuir **"Contato de Entrega"** o sistema não utilizará a validação do campo **"Gerar endereço de entrega no XML da NF-e"**, presente no cadastro de [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025388653-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), e informará a tag **<entrega>** no XML com os dados do contato.

Também na Central de Vendas, tem-se os campos **"UF Emitente"**, **"UF Destinatário"** e **"UF Local Entrega"**; tem-se desta forma três UF's, sendo que o cálculo do ICMS e do DIFAL será regido pela UF Emitente e UF Local de Entrega, quando estiverem informadas.

O cálculo para operações com ICMS-ST e para as operações de Venda à Ordem, não sofrerão alterações com relação a UF do Contato Local de Entrega.

Tendo-se o campo Cód. Contato Entrega preenchido, as tag's do Local de Entrega também deverão ser preenchidas, conforme especificadas na tabela abaixo no XML da NF-e:

![Imagem 11: Observação: os dados para preenchimento destas tag's são alimentados na aba Contatos do Cadastro de Parceiros .](https://ajuda.sankhya.com.br/hc/article_attachments/9472438742039)**Observação:** os dados para preenchimento destas tag's são alimentados na aba [Contatos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abacontatos) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### Geração dos Livros Fiscais considerando o Parceiro "Local de Entrega"

Na tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI) tem-se os campos **"Contato de Entrega"** e **"UF de Entrega"** presentes na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874-Cadastro-Livro-ICMS-IPI#abageral); tem-se nestes campos o código do contato e sua respectiva UF; estas informações são as inseridas na emissão da NF-e.

[GIF animado: Imagem 12: Na tela Cadastro Livro ICMS/IPI tem-se os campos "Contato de Entrega" e "UF de Entrega" presentes na aba Geral ; tem-se…](https://ajuda.sankhya.com.br/hc/article_attachments/4415884542999)

Em consequência do procedimento realizado na tela anterior, na tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI) os campos **"Contato de Entrega"** e **"UF de Entrega"** também são gerados, de acordo com o preenchimento feito na emissão da NF-e.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### Geração do EFD considerando o Parceiro "Local de Entrega"

Na geração do EFD - Escrituração Fiscal Digital, os registros C115 – campos 01, 02, 07, 08, 09 e 10 são alimentados com os dados do Contato do Parceiro, devidamente identificado no campo Contato de Entrega.

Este registro somente é gerado, se for configurada a **"Observação"** para ser gerado o registro C110, pois o registro C11B A "filho" deste.

![Imagem 13: Este registro somente é gerado, se for configurada a "Observação" para ser gerado o registro C110, pois o registro C11B…](https://ajuda.sankhya.com.br/hc/article_attachments/15635714769047)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### Emissão do DANFE com os valores do DIFAL

Na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), quando for emitido um DANFE, e este for do modelo Padrão, para notas que calcularam DIFAL, tem-se no campo **"Informações Complementares"**, os valores totais do ICMS Interestadual (oriundos da tabela TGFCAB), com base nos seguintes campos:

- DIFAL da UF destino (TGFCAB\_VLRICMSDIFALDEST);
- FCP (TGFCAB\_VLRICMSFCP);
- DIFAL da UF de Origem (TGFCAB\_VLRICMSDIFALREM).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)

### SEFAZ que não exigem o DIFAL

Para a SEFAZ que não exigir o DIFAL (grupo **<ICMSUFDest>**), devido às UF's origem/destino participarem de Protocolos ou Convênios que definem os benefícios fiscais tais como Isenção, por exemplo, o sistema deverá ser configurado da seguinte forma:

- No parâmetro **"UFs destino NF-e com benefício fiscal para DIFAL - UFDESTNFEBENFIS"** que por padrão é vazio, informa-se a sigla de cada UF da SEFAZ de destino (separada por vírgula); caso a SEFAZ de origem/destino estejam amparadas por benefícios fiscais, ou seja, a alíquota interestadual é igual a zero.
- Alíquota interestadual deve ser igual a zero.
- CST's deverão estar configurados igual a 40, 41, 50, 51, ou 60.

Desta forma, o valor do DIFAL e do Fundo de Combate à Pobreza, não serão calculados quando o produto estiver com a alíquota interestadual igual a zero, e o "Cód.Tributação(CST)" for igual a 40, 41, 50, 51 ou 60, e a UF destino esteja no parâmetro UFDESTNFEBENFIS.

Não existindo o cálculo do DIFAL, o grupo **<ICMSUFDest>** não será gerado.

A geração do grupo **<ICMSUFDest>** no XML não foi alterada e sua premissa continua sendo a existência de valor em algum dos campos referentes ao DIFAL ou ao Fundo de Combate à Pobreza.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600414-Nota-T%C3%A9cnica-2015-003-NF-e-CEST-e-DIFAL-Partilhado#top)
