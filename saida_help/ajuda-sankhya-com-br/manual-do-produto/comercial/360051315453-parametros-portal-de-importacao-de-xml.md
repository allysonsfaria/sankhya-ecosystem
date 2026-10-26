---
id: "360051315453"
titulo: "Parâmetros - Portal de importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051315453-Par%C3%A2metros-Portal-de-importa%C3%A7%C3%A3o-de-XML"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-05T18:00:41Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "USACRPROJNATCAB", "VALCHAVETERC", "CONCNPJIEIMPXML", "DHSAIENTIMPXML", "TOPIMPORTXML", "VALBONIFPEDNOT", "Parâmetros", "br.com.sankhya.cac.ImportacaoXMLNota", "Parâmetros - Portal de importação de XML", "NATPADIMPCTEP", "CRPADIMPCTEP", "CFOPLIGNFEIXML", "TPVMODIMPDEVVEN", "IMPZIPMODFAST", "TOPDIGIMPXMLCTE", "IMPCTEIMPITERE", "IMPCOMVENMESBAS", "STPORDATA", "PERMALTTOPXML", "LIGPEDPARCMAT", "CALBCICMSXMLLOT", "Portal de Importação Parâmetros Validação", "Configurações e Opções", "Parâmetros do Portal de Importação de XML", "CTEALTVLRFREXNT", "CONFDIGICMSIPI", "Comercial"]
---

# Parâmetros - Portal de importação de XML

```
 Módulo: Comercial
```

---

Neste artigo, encontre os parâmetros que influenciam na rotina [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML).

**Seguro incide ICMS - SEGINCICMS:** com este parâmetro ligado, o valor do seguro é somado juntamente com o valor do ICMS.

**Validação da chave de acesso da NF-e de terceiros com os dados da nota - VALCHAVETERC:** visando a otimização do processo de validação do EFD Fiscal, no processo de compras, pode-se optar em validar a chave de acesso da NF-e no momento da entrada da nota; esta medida tem a intenção de evitar possíveis problemas de validação no EDF Fiscal quanto a chave de acesso e os dados da nota.

Primeiramente, é feita a importação do XML por da tela Portal de importação de XML, em seguida, ao realizar o lançamento da nota no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953), ocorre a validação da chave; esta validação depende da configuração do parâmetro VALCHAVETERC, onde são possíveis três opções de marcação:

- **Não valida:** quando o parâmetro estiver definido como Não valida (definição padrão), depois de importado o XML e, ao lançar a nota de compra na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793), mesmo que existam divergências entre a chave importada, e a chave lançada, a nota poderá ser confirmada sem que nenhuma mensagem seja apresentada.

- **Valida e avisa:** definindo o parâmetro com esta opção, depois da importação do XML, ao confirmar a nota na Central de Compras, caso existam divergências entre as chaves, será exibida uma mensagem semelhante a apresentada a seguir (a mensagem muda de acordo com as divergências encontradas):

**"Informação**

**Existem divergências entre a chave de acesso da nota e seus dados: cUF (Chave) = 31**

**Código IBGE (Sistema) = 35**

**AAMM (Chave) = 1406**

**Dt. Neg. (Sistema) = 1405**

**CNPJ (Chave) = 57499908000161**

**CNPJ do Parceiro (Sistema) = 57499908000164**

**mod (Chave) = 51**

**Modelo do Documento (Sistema) = 55**

**serie (Chave) = 000**

**Série da Nota (Sistema) = 001**

**nNF (Chave) = 000005935**

**Nro. Nota (Sistema) = 00005937**

**Estas informações devem ser verificadas, deseja continuar mesmo assim com a confirmação?"**

Mesmo com estas divergências, será possível realizar a confirmação da nota.

**Nota:** as Notas Fiscais Eletrônicas de Terceiros que são enviadas para o [Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025238814-Recebimento-de-Mercadorias), também passarão pela validação efetuada pelo referido parâmetro, ou seja, ao serem enviadas, caso existam divergências, uma mensagem semelhante à apresentada acima é exibida. Caso não seja dada a sequência na confirmação do procedimento (clicando em **"Não"**), o campo **"Status WMS"** correspondente à nota, irá permanecer como **"Não enviado"**.

Caso exista divergência apenas no número aleatório da chave, será apresenta a seguinte mensagem:

**"O número aleatório da chave de acesso digitada está divergente do número aleatório da NF-e. Favor verificar e corrigir a digitação da chave de acesso no sistema. Deseja continuar com a confirmação?".**

Mesmo com esta divergência, será possível realizar a confirmação da nota.

- **Valida e bloqueia:** definindo o parâmetro como Valida e bloqueia, ao confirmar a nota na Central de Compras, caso existam divergências entre as chaves, será exibida uma mensagem semelhante a apresentada a seguir (a mensagem muda de acordo com as divergências encontradas):

**"Erro**

**Existem divergências entre a chave de acesso da nota e seus dados:**

**cUF (Chave) = 31**

**Código IBGE (Sistema) = 35**

**AAMM (Chave) = 1406**

**Dt. Neg. (Sistema) = 1405**

**CNPJ (Chave)  = 57499907000161**

**CNPJ do Parceiro (Sistema) = 57499907000164**

**mod (Chave) = 51**

**Modelo do Documento (Sistema) = 55**

**serie (Chave) = 000**

**Série da Nota (Sistema) = 001**

**nNF (Chave) = 0000005935**

**Nro. Nota (Sistema) = 000005937"**

Diferentemente da configuração anterior, com esta definição no parâmetro, não será permitida que seja feita a confirmação da nota.

Encontrando divergência apenas no número aleatório, o sistema apresenta a seguinte mensagem:

**"O número aleatório da chave de acesso digitada está divergente do número aleatório da NF-e. Favor verificar e corrigir a digitação da chave de acesso no sistema".**

**Usa dhSaiEnt na import. do XML do portal de imp.? - DHSAIENTIMPXML:** por padrão, é apresentado ativado. Quando desabilitado, serão desconsiderados os valores das tag's <**dhSaiEnt**> e a data e hora atual, serão preenchidos com os campos **"Dt. Entrada/Saída"** e **"Hr. Entrada/Saída"**, respectivamente; assim como será desconsiderado o valor da tag <**dhEmiss**> e o campo **"Dt. do Movimento"** será preenchido com a data atual.

O parâmetro **DHSAIENTIMPXML**, no contexto da importação de XML, atualmente só é aplicável a NF-e.

**Somente ligação de pedido bonif. p/ compra bonif.? - VALBONIFPEDNOT:** durante o processo de importação de XML, é importante que o sistema verifique se as notas de compra bonificadas estão sendo ligadas somente a pedidos bonificados e notas de compra não bonificadas a pedidos bonificados. Para que o sistema faça tal validação, é necessário o ligar esse parâmetro (que por padrão é desligado).

Com o referido parâmetro ativado, na aba **"Pedidos"**, grade **"Itens importados"**, ao clicar no botão **"Ligar pedidos mais antigos"**, as ligações só poderão ser feitas entre notas bonificadas e pedidos bonificados e vice versa. Já na grade **"Pedidos disponíveis"**, ao clicar no botão **"Buscar novos pedidos"**, caso a nota seja bonificada, só serão apresentados pedidos bonificados e vice versa.

**Nota:** o sistema também realiza as validações a respeito de pedidos e notas bonificadas, quando este procedimento é realizado na Central de Compras por meio do botão Outras Opções, opção **"Importar XML de nota fiscal eletrônica"** ou **"Importar XML de nota fiscal eletrônica (substituindo itens)"**, e ainda pelo botão Outras Opções na grade de itens na opção **"Documentos relacionados"**; no pop-up que é aberto por meio desta opção, caso seja feita a tentativa de lidação de um pedido bonificado com alguma nota não bonificada e vice versa, será exibida uma mensagem de erro, impedindo tal ligação.

**Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB:** quando habilitado, fará com que os campos **"Projeto"**, **"Natureza"** e **"Centro de Resultado"** do **"Financeiro da Nota"**, estejam preenchidos com os mesmos dados apresentados nestes campos presentes no **"Cabeçalho da Nota"**. Caso algum destes campos seja modificado no Cabeçalho da Nota, quando esta alteração é salva, o Financeiro da Nota também é modificado.

Com o parâmetro acima mencionado desativado, o Centro de Resultado, Natureza e Projeto do Financeiro da Nota, serão alimentados com esta informação correspondente, na aba Parcelas do **"Tipo de Negociação"**. Caso estes campos não estejam preenchidos no Tipo de Negociação, os três campos no Financeiro da Nota serão alimentados com os mesmos informados no Cabeçalho da Nota.

Em específico para o Centro de Resultado, caso este não esteja informado no Tipo de Negociação, este será preenchido no Financeiro da Nota, com o valor informado no cadastro de **"Vendedores/Compradores"**; não sendo este informado, será pega a informação da aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios); caso este também não esteja informado, o Centro de Resultado do Financeiro da Nota irá seguir ao preenchimento realizado no Cabeçalho da Nota.

**TOP a ser utilizada no portal de importação de XML - TOPIMPORTXML:** possibilita a utilização de duas opções, a saber:

- TOP de destino do pedido de compra;
- Modelo de importação.

Optando-se por uma destas duas alternativas, o sistema apresenta o seguinte comportamento:

Quando o parâmetro TOPIMPORTXML estiver igual a **"TOP de destino do pedido de compra"**, o sistema sempre irá verificar o campo **<xPed>** do arquivo XML importado e tentar encontrar os pedidos de compra no sistema a partir do número encontrado.

- Se o XML importado não possuir a informação do campo **<xPed>**, o sistema não irá preencher a TOP para importação e ficará a seu cargo a informação da mesma.
- Se o XML importado possuir a informação do campo **<xPed>**, mas os pedidos de compra não forem encontrados no sistema, este não irá preencher a TOP para importação e ficará a seu cargo a informação da mesma.
- Se encontrar mais de um pedido, que tenham mais de uma TOP, o sistema não irá utilizar qualquer TOP para processar a importação do XML, ficando a seu cargo informar qual TOP deseja usar.
- Se encontrar um ou mais pedidos que possuam a mesma TOP, o sistema irá verificar qual a TOP de destino configurada em seu cadastro.

Quando o parâmetro TOPIMPORTXML estiver definido com a opção **"Modelo de importação"**, o sistema sempre irá utilizar a TOP do modelo de importação para processar a importação do XML.

Vale salientar que, em ambos os casos, pode-se editar a TOP sugerida pelo sistema para realizar a importação.

**Permitir alterar TOP na importação de XML de nota já criada? - PERMALTTOPXML:** quando ligado, na importação do XML de uma nota já criada, permite realizar a alteração do Tipo de Operação - TOP no Portal de Importação de XML. Sendo que, esta alteração só será permitida quando o campo **"Status"** estiver como Divergência ou Pendente.

**Pode ligar nota ao pedido com o parceiro matriz? - LIGPEDPARCMAT:** quando estiver ativado, na importação do XML se o Parceiro da Nota possuir um Parceiro Matriz, será apresentada uma janela para a escolha do Parceiro a ser utilizado na busca dos Pedidos para a ligação. Nesse caso, pode-se escolher o Parceiro da Nota ou o Parceiro Matriz.

**Considerar Data Negociação no cálculo do ICMS ST - STPORDATA:** este parâmetro determinará se a data de negociação da nota será considerada na busca do ICMS ST. Desta forma, quando este encontrar-se habilitado, ao realizar a importação de um XML onde o ICMS ST por pauta deverá ser calculado, a consulta será realizada utilizando a data de negociação. Por outro lado, caso este parâmetro esteja desabilitado, ao importar um XML, a data considerada para busca do imposto será a data atual.

**Considerar CNPJ/CPF e IE na importação do XML? - CONCNPJIEIMPXML:** com o parâmetro ligado, ao realizar a importação do XML, o sistema irá considerar o CPF/CNPJ e Inscrição Estadual do destinatário do XML para localizar a Empresa. Caso o XML não possua a informação pertinente à Inscrição Estadual, será considerado apenas o CNPJ/CPF para identificação da Empresa e será exibida a seguinte mensagem:

**"Não encontramos empresas com CNPJ e IE iguais ao do XML, no entanto, foram encontradas múltiplas empresas com o mesmo CNPJ. Na importação, será considerada a empresa com o menor código de cadastro"**.

Ao tentar processar, o sistema faz novamente a validação do parâmetro CONCNPJIEIMPXML e exibe a seguinte mensagem ao usuário:

**"Não foi encontrado empresas com dados de destinatário CPF e IE ou emitente CPF e IE"**.

Se o parâmetro estiver desligado, o sistema considera apenas o CPF/CNPJ na validação da importação do XML. Isso significa que uma nota será importada para a empresa com o menor número de cadastro, mesmo que a Inscrição Estadual não corresponda ao XML, pois, com o parâmetro desativado, a Inscrição Estadual não é validada.

É importante destacar que, com o parâmetro CONCNPJIEIMPXML ativado, o sistema compara a Inscrição Estadual (IE) registrada no [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Cadastro-de-Empresas) com a tag **<IE>** do grupo **<Dest>** no XML da NFe. Caso a tag contenha zeros à esquerda, esses serão desconsiderados, permitindo a importação do XML mesmo que haja diferença na formatação da IE. 

Por outro lado, se o parâmetro estiver desativado, o sistema seguirá o comportamento padrão, validando apenas o CNPJ/CPF e desconsiderando a IE. Nesse caso, a NFe será importada para o cadastro que apresentar o menor número associado ao mesmo CNPJ/CPF do XML. 

O comportamento do parâmetro CONCNPJIEIMPXML ocorre apenas na rotina do Portal de Importação de XML.

**Importar arquivos ZIP pelo modo Rápido? - IMPZIPMODFAST:** ao habilitar este parâmetro, a importação de arquivos ZIP de XML via Portal de Importação será feita de forma otimizada, com os arquivos sendo tratados em lotes de 500, e não individualmente. Após a importação, o processamento dos arquivos seguirá conforme as configurações definidas na tela [Agenda do Processamento de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360063013313-Agenda-do-processamento-de-XML).

**Natureza padrão p/Importacao CTe Emiss. Prop.- NATPADIMPCTEP** e **CR padrão p/Importacao CTe Emiss. Prop.- CRPADIMPCTEP:** pode-se informar nestes parâmetros o código da Natureza e do CR, respectivamente, que serão utilizados na importação do XML de CTe de Emissão Própria.

**CFOPs p/ ligar notas c/ tag finNFe 1 na imp XML - CFOPLIGNFEIXML:** pode-se preencher este parâmetro com os CFOP's da nota de retorno, pois, dessa forma, quando a importação de um XML de retorno de industrialização for realizada, o sistema realizará o vínculo com a nota fiscal de remessa. Porém, se a chave de referência localizada na tag <**refNFe**>, não encontrar-se em nenhuma nota, o sistema exibirá a seguinte mensagem:

**"A nota nro. xxxxxx é uma nota de retorno, mas não possui notas eletrônicas de remessa correspondentes na base, a importação não será realizada."**

Portanto, na ausência da chave de referência, a marcação **"Desconsidera Nfe de orig. referenciada? (Importação de XML)"** da aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce) da [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) poderá ser acionada. Assim, a nota será importada, mas, o vínculo com a nota de origem não será realizado.

**Preferir TOP digitada na importao de CT-e?- TOPDIGIMPXMLCTE:** para a importação do XML do CT-e, o sistema não considera o [Tipo de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) informado na aba [Modelo de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abamodelodeimportaodexml) que foi vinculado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893). Isto é, atualmente o sistema busca a TOP definida no campo **"Tipo Operação"** localizado no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção [Preferências de Importação do CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e), seção**"Movimentação Financeira"**. No entanto, quando o parâmetro TOPDIGIMPXMLCTE estiver ligado, na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793) o sistema informará a TOP definida na grade do Portal de Importação.

Já quando o parâmetro TOPDIGIMPXMLCTE estiver desligado e a marcação **"Importar CT-e com Cabeçalho"** da seção **"Nota de Compra"** estiver marcada, o sistema informará no XML do Portal de Importação o Tipo Operação informado na seção Movimentação Financeira. E na Central de Compras, será apresentada a TOP informada na seção Nota de Compra.

**Importar CTE com regra de imposto da central? - IMPCTEIMPITERE:** com o parâmetro ligado ao importar um CT-e, o sistema irá calcular o CST IPI de acordo com as [Regras para buscar a CST de IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354-Regras-para-Buscar-a-CST-de-IPI-e-o-c%C3%A1lculo-do-imposto-no-Sistema-SankhyaW).

**Observação:** caso o parâmetro acima esteja habilitado e a marcação **"Tem IPI?"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) desligada, o sistema irá considerar o CST de IPI conforme configurado na TOP.

**Importa compra e venda na mesma base? - IMPCOMVENMESBAS:** para que uma nota de emissão própria pelo [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) fique com o Status NF-e igual à **"Aprovada"**, é necessário que este parâmetro esteja desligado.

**Nota:** se o CNPJ do emitente e do destinatário existirem na base, a nota primeiro será importada como compra para depois ser importada como NF-e de emissão própria.

**Priorizar Emissão Própria na importação de NF-e - PRIOEMISPROPNFE:** quando ligado, pode-se importar o mesmo XML na base duas vezes, priorizando o tipo Emissão Própria e, posteriormente o tipo Compra.

Porém, para que o parâmetro acima assuma o comportamento descrito, o parâmetro IMPCOMVENMESBAS deve ser ligado, caso contrário, o mesmo XML não será importado novamente e será exibida a mensagem:

**"Chave de acesso já existe no portal de vendas, número único xxxx, chave de acesso: 00000000000000000000000000000000000000000000000000000"**

Além disso, ao habilitar apenas o parâmetro IMPCOMVENMESBAS, o sistema ainda importará o mesmo XML duas vezes, mas na posição invertida, ou seja, priorizando a Compra e, posteriormente, a Emissão Própria.

**Utilizar Tip.Neg. do modelo ao importar Dev.Venda? - TPVMODIMPDEVVEN:** quando habilitado, o **"Tipo de Negociação"** informado no [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) que será considerado ao realizar a importação da nota de devolução no Portal de Importação de XML.

**Calcula Base de ICMS Proporcional Imp XML Lote? - CALBCICMSXMLLOT:** se a empresa utilizar a redução da base de cálculo e o parâmetro estiver ativado, durante a importação do XML, o sistema aplicará o cálculo inverso. Assim, ao invés de recompor a base de cálculo do imposto, a redução será considerada, resultando em uma base de cálculo de ICMS menor do que a informada no arquivo original.

**Valida controle por grade na importação do XML? - VALCONTGRADEXML:** quando ligado, o sistema irá validar a importação de produtos que possuem controle por grade, porém, a grade do produto deve ser configurada no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953).

**Tolerância p/ divergência impostos na Import. XML - TOLIMPIMPORTXML:** pode-se informar neste parâmetro, um valor para tolerância de arredondamento no recálculo de imposto. Porém, caso haja necessidade de importar os valores de imposto sem essa tolerância, o valor a ser informado no parâmetro deve ser configurado com **"0.00"**, desse modo, a divergência pode ser informada na tela onde pode-se escolher os valores do arquivo ou de recálculo.

**Excl. ICMS BC PIS/COFINS Ent. Portal Imp. MP 1159 - EXCICMSBCPISCOF:** com o parâmetro ativado, na importação de XML o sistema terá o seguinte comportamento: 

- **Na importação de XML de compra de mercadorias para uso e consumo - contribuinte do ICMS:** o sistema irá subtrair o valor que consta na tag **<vICMS>** da base de cálculo do PIS/COFINS;
- **Na importação de XML de compra de mercadoria para uso e consumo - optante pelo simples nacional:** o sistema irá subtrair o valor que consta na tag **<vCredICMSSN>** da base de cálculo do PIS/COFINS;
- **Na importação de XML de compra de combustível e lubrificantes:** quando o CST for 60 e o campo **"Classificação Substituição Tributária - TGFPRO.CLASSUBTRIB"** da tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaimpostos) for igual a **"6 - Derivados de petróleo, lubrificantes e outros produtos"**, o sistema irá subtrair o valor que consta na tag **<vICMSSTRet>** da base de cálculo do PIS/COFINS;
- **Na importação de XML de compra de combustível e lubrificantes:** quando o CST for 61 e o campo Classificação Substituição Tributária - TGFPRO.CLASSUBTRIB da tela Cadastro de Produtos, aba Impostos for igual a 6 - Derivados de petróleo, lubrificantes e outros produtos, o sistema irá subtrair o valor que consta na tag **<vICMSMonoRet>** da base de cálculo do PIS/COFINS;
- **Na importação de XML de aquisição de frete por CT-e, (situação em que o valor pode ser tomado como crédito pelo destinatário):** quando a UF de origem da prestação for igual a UF do emitente,  o sistema irá subtrair o valor que consta na tag **<vICMS>** da base de cálculo do PIS/COFINS;
- **Na importação de XML de aquisição de frete por CT-e, (situação em que o valor pode ser tomado como crédito pelo destinatário):** quando a UF de origem da prestação for diferente da UF do emitente, o sistema irá subtrair o valor que consta na tag **<vICMSOutraUF>** da base de cálculo do PIS/COFINS.

**N Alt vlr frete extra nota propria ao importar CTe? - CTEALTVLRFREXNT:** quando este parâmetro estiver habilitado, ao importar um CT-e com nota própria referenciada, que possua o campo **"Tipo do Frete"** preenchido com a opção **"Extra nota"** na aba **"Transportes"** das Centrais de [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatransporte) e [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#abatransporte), as informações sobre **"Vlr. do Frete"**, **"Base do ICMS do Frete"** e **"ICMS sobre o frete"** não serão alteradas. 

**Vlr total da nota e peso p/ calc. do rateio de frete -** **VLRTOTNOTAPESO:**  quando este parâmetro estiver ativado, o sistema distribui o valor total da carga entre as notas fiscais. Caso esteja desativado, utiliza diretamente o valor da nota fiscal (**VLRNOTA**) da tabela **TGFCAB**, sem rateio.

**Base ICMS Simples Nacional na Importação XML - CALCBICMSSNTRI:** este parâmetro de sistema controla como o valor da Base de Cálculo do ICMS Tributada deve ser determinado em documentos do Simples Nacional, importados via XML, especialmente quando o valor do ICMS é zero.

O parâmetro **CONFDIGICMSIPI ("Confere ICMS e IPI digitados?")** controla se o Sankhya deve validar e recalcular automaticamente os campos de ICMS e IPI quando esses valores são alterados manualmente durante o lançamento de itens em Notas Fiscais de Compra.

Este parâmetro atua como uma camada adicional de proteção, garantindo consistência matemática entre os campos de imposto, mesmo quando o usuário faz alterações manuais na tela, independente do tipo de cálculo configurado na Tipo de Operação (TOP).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051315453-Par%C3%A2metros-Portal-de-importa%C3%A7%C3%A3o-de-XML#top)
