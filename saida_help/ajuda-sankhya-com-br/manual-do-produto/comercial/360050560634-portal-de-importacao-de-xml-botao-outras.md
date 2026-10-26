---
id: "360050560634"
titulo: "Portal de importação de XML - Botão Outras Opções"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-10-15T21:09:12Z"
rotulos: ["CT-e", "Configuração", "WMS", "Movimentação Financeira", "XML", "Importação", "TOP", "Importação Configuração Processamento", "Integração Eficiente: Portal de Importação de XML", "RATFRETESELEC"]
---

# Portal de importação de XML - Botão Outras Opções

```
 Módulo: Comercial > Rotinas 
```

---

O botão **"Outras Opções..."** no [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), representado pelo ícone ![Imagem 1: O botão "Outras Opções..." no Portal de importação de XML , representado pelo ícone está localizado na parte superior…](https://ajuda.sankhya.com.br/hc/article_attachments/16370839823639) está localizado na parte superior direita da tela. Neste artigo, descreveremos as funcionalidades nele disponíveis:

| Funcionalidades da tela |
| --- |
| [Enviar para o WMS (Recebimento)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#enviarparaowms(recebimento)) |
| [Preferências para Importar CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimportarct-e) |
| [Config. para liberações de divergências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#config.paralibera%C3%A7%C3%B5esdediverg%C3%AAncias) |
| [Preferências para importação de NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#prefer%C3%AAnciasparaimporta%C3%A7%C3%A3odenf-e) |
| [Prefer. para import. de NF-e de Emissão...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#pref.paraimport.denf-edeemiss%C3%A3o...) |
| [Config. de Modelo p/ NF-e Compra...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#config.demodelop/nf-ecompra...) |
| [Validar TOP na importação do XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#validartopnaimporta%C3%A7%C3%A3odoxml) |
| [Desconsiderar Ped. de Venda na Importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#DesconsiderarPed.deVendanaImporta%C3%A7%C3%A3o) |
| [Ajustar notas para DRCST...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#ajustarnotasparadrcst(chaveesequ%C3%AAnciafiscal)) |

## Enviar para o WMS (Recebimento)

Por meio desta opção, realiza-se o envio das notas de compra para o WMS depois que estas notas forem validadas no Portal de Importação de XML. Ao acionar esta opção, será aberto um pop-up onde realiza-se a escolha da doca de entrada disponível, encaminhando-a para o Recebimento.

As Notas Fiscais Eletrônicas de Terceiros que são enviadas para o Recebimento, também passarão pela validação efetuada pelo  parâmetro **"Validação da chave de acesso da NF-e de terceiros com os dados da nota - VALCHAVETERC"**, ou seja, ao serem enviadas, caso existam divergências, uma mensagem pertinente a tal divergência é exibida. Caso não seja dada a sequência na confirmação do procedimento (clicando-se em Não no pop-up apresentado), o campo **"Status WMS"** correspondente à nota, irá permanecer como **"Não enviado"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Preferências para Importar CT-e

Ao acionar esta opção, será aberto o pop-up Preferências para importação do CT-e, onde configuram-se as particularidades acerca da importação do CT-e:

![Imagem 2: Ao acionar esta opção, será aberto o pop-up Preferências para importação do CT-e , onde configuram-se as…](https://ajuda.sankhya.com.br/hc/article_attachments/23474825979415)

Os CT-e's importados podem ser:

- **De Terceiros:** quando o CNPJ do Tomador de serviço for cadastrado no sistema como empresa;
- **De Emissão Própria:** o CT-e recebe esta classificação, quando o CNPJ do Emitente do CT-e for cadastrado como empresa e esta empresa também é emitente de CT-e;
- **De Documento Anterior:** quando nem o Tomador do Serviço, nem o Emitente do CT-e forem cadastrados no sistema como empresa.

Diante disso, temos:

### Aba CT-e de Terceiros

Nesta aba, na seção **"Movimentação Financeira"** são definidas as preferências, ou seja, os valores padrão dos campos que obrigatoriamente precisam ser alimentados no financeiro do CT-e para que este seja construído. A importação/validação do CT-e consiste em definir as preferências aqui listadas, importar o arquivo XML do CT-e e em seguida processá-lo; o CT-e será composto pelo XML importado e as preferências do financeiro informadas neste pop-up.

O campo **"Tipo Operação"** é destinado à indicação de Tipos de Operação - TOP configurados com o modelo de documento **"57 - Conhecimento Transporte Rodoviário Eletrônico"**, bem como, o campo **"Tipo Operação CT-e OS"** comportará os **Tipos de Operação - TOP** que compreenderem o modelo de documento **"67 - Conhecimento de transporte eletrônico OS"**. A referida informação é configurada no cadastro de Tipos de Operação - TOP, aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), campo **"Modelo do Documento"**.

**Nota:** caso as opções **"Importar CT-e com Cabeçalho"** e **"Central de Compras"** (seção  Nota de Compra, campo **"Tipo de Importação"**) estejam selecionadas, este campo não será de preenchimento obrigatório.

É importante citar que a opção **"Obtenção do CFOP"** indica a forma com que será calculado o CFOP da nota que está sendo importada. Temos duas opções:

- **Conversão do CFOP:** esta opção é definida como padrão; por meio desta opção o sistema realizará a conversão do CFOP de saída gerado no XML do CT-e para um CFOP de entrada;
- **CFOP do Tipo de Operação:** esta opção ignora o CFOP gerado no XML do CT-e e utiliza a CFOP inserida no Cadastro do Tipo de Operação do financeiro de frete.

Ao habilitar a marcação **"Considerar ICMS do XML?"** e realizar a importação do XML do CT-e de terceiros na TOP financeira, o sistema adotará o valor do ICMS presente no XML em vez de calculá-lo. Esse valor será registrado no campo **"Vlr ICMS"** localizado na aba de Impostos na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), e essa informação será utilizada na elaboração do livro e na geração de obrigações acessórias, como o SPED [EFD - Contribuições PIS/COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/4407916885271-EFD-Contribui%C3%A7%C3%B5es-PIS-COFINS) e o SPED [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI).

**Priorização UF do Expedidor/Recebedor para Determinação de CFOP**

O sistema oferece a funcionalidade de priorizar as informações de UF do expedidor e recebedor para determinação correta do CFOP na importação de CT-e de terceiros.

Quando o campo "**Priorização UF do Expedidor/Recebedor para Determinação de CFOP"** estiver ativado, o sistema utiliza as tags <exped> (expedidor) e <receb> (recebedor) do CT-e para determinar a unidade federativa (UF) ao invés de utilizar as informações de remetente e destinatário. Isso impacta diretamente na classificação do CFOP:

- Mesmo UF: o CFOP é classificado como interna ou intermunicipal;

**Nota Importante:**
A configuração "Priorizar Expedidor/Recebedor para CFOP" sobrepõe o parâmetro USAPARREMDESCPA, ou seja, a configuração tem prioridade. O sistema apenas consultará o parâmetro se a configuração não estiver definida/ativada.

- UF Diferente: o CFOP é classificado como interestadual.

**Seção** **Nota de Compra**

Nesta seção, realize as configurações abaixo para que seja possível criar um Cabeçalho de Nota na Importação do XML do CT-e de Terceiros:

Ao efetuar a marcação **"Importar CT-e p/ Central de Compras"**, será habilitada a rotina de criação do Cabeçalho da Nota na Importação do XML do CT-E no Portal de Importação de XML.

**Observação:** para realizar a importação do CT-e sem que este gere parcela no financeiro, basta habilitar a marcação Importar CT-e com Cabeçalho e informar a TOP utilizada na Nota de Compra configurada com a opção **"Não atualizar"** do campo **"Financeiro"** (localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral) da tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TO)), além disso, é preciso ligar o parâmetro **"Validar Top ATUALFIN na imp. XML - VALTOPFINXML"**.

Você deve assinalar a marcação **"Processar arquivos XML de CT-e com parceiros duplicados"**, para realizar a importação do XML quando existir dois ou mais parceiros cadastrados com o mesmo CNPJ. Sendo que, o Código do Parceiro registrado na grade  será enviado para o [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953).

O campo **"Tipo de Importação"**apresenta as seguintes opções:

- **Movimentação Financeira:** a TOP utilizada no Financeiro do CT-e será a que foi informada no grupo Movimentação Financeira e a nota inserida na Central será confirmada;
- **Central de Compras:** a TOP utilizada no Financeiro do CT-e será a que foi informada no grupo Nota de Compra e a nota inserida na Central não será confirmada automaticamente.

![Imagem 3: Com a opção Central de Compras selecionada, deve-se também marcar a opção "Exige" ou "Exige confirmada" no campo "Exige…](https://ajuda.sankhya.com.br/hc/article_attachments/24732320689943) Com a opção Central de Compras selecionada, deve-se também marcar a opção **"Exige"** ou **"Exige confirmada"** no campo **"Exige vínculo com notas"**, seção Exigências de vínculos. Além disso, o parâmetro **"Ratear frete apenas c notas selec no P.Importação - RATFRETESELEC"** deve estar ligado para que o cálculo do custo do CT-e seja realizado.

**Nota:** para importar um XML de CT-e emitido pelo sistema Nota Fiscal Fácil, onde a tag **<tpEmis>** contém o valor 3, configure o campo Tipo de Importação com a opção Central de Compras e habilite a marcação Importar CT-e com Cabeçalho. Assim, ao processar o arquivo XML no [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML), o sistema importará o CT-e para a [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793).

**Nota:** quando a opção Central de Compras estiver selecionada, realiza-se a conversão e a informação desta irá preencher o campo **"CFOP"** (Tela Portal de Importação de XML, grade **"Itens"**).

**Observação:** ao fazer a importação do XML de um CT-e Tomado através do Portal de importação do XML, com o campo Tipo de Importação configurado com a opção **"Central de Compras"**, fará com que o campo **"Chave CT-e referenciada"** seja gravado no campo **"Chave CT-e de Referência"** da tela [Cadastro Livro ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607874), gerando a informação no livro e, consequentemente, gerada no registro D100 do EFD/ICMS/IPI.

**Nota:** para que o sistema não atualize o valor de frete, o tipo de importação na seção Nota de Compra deve ser igual à Movimentação Financeira. Além disso, o parâmetro **"Validar Top ATUALFIN na imp. XML - VALTOPFINXML"** deve estar ligado.

No campo **"Top p/ Cabeçalho CT-e"** insira a operação que será utilizada na criação do Cabeçalho da Nota na Importação do XML do CT-E no Portal de Importação de XML.

O campo **"Tipo de Negociação"** armazenará qual será o Tipo de Negociação utilizado na criação do Cabeçalho da Nota na Importação do XML do CT-E no Portal de Importação de XML.

Para que o financeiro do CT-e seja inserido normalmente, o sistema utiliza o valor informado na tag **<vTPrest>**, ou seja, o próprio valor do desdobramento.

**Nota:** não existe uma tag de vencimento, portanto, será definida da seguinte forma:
O sistema pegará a data de emissão do CT-e **<dhEmi>** e somará com a quantidade de dias o valor salvo no campo **"Prazo**" da primeira parcela de pagamento informada no Tipo de Negociação, utilizada para inserção do CT-e de Terceiros na Central de Compras; caso não exista valor informado, ou seja, valor igual a zero, o vencimento será a própria data de emissão.

Insira no campo **"Serviço Padrão"** o código do serviço a ser utilizado na criação do Cabeçalho da Nota e na geração do Item da Nota.

**Observação:** o campo acima será responsável por carregar os valores de CT-e, desde o desdobramento até os impostos e levar até o Cabeçalho da Nota.

Após realizar as configurações acima e processar o arquivo, o sistema informará o Nro. Único do Financeiro gerado; assim, caso acione o botão **"Abrir Documento"** do Portal de Importação de XML, o sistema abrirá a Central de Notas para que se realize todas as tratativas gerencias e fiscais relativas ao CT-e de Terceiros.

**Nota:** será possível visualizar os Cabeçalhos de Notas de Conhecimentos de Transportes através do filtro **"Tipo de Movimento"** localizado nos Portais, desde que, você possua as permissões ao Módulo **"Conhecimento de Transporte"** nos **"Controles de Acessos"**. 

Através do campo **"Buscar Pedido de Frete por"**, você pode definir como será capturado o **"Nro. Único de Pedido de Frete"**, para que possa realizar o vínculo com o CT-e de Terceiros importado. Este campo possui as seguintes opções:

- **Nro. Pedido de Frete:** esta opção resolverá o Nro. Único do Pedido de Frete através das NF-e's de Compra ou dos Pedidos de Compra ligados.
- **Nro. Ped. Frete ou Manual:** esta opção contempla o Nro. Pedido de Frete e, caso o sistema não consiga encontrá-lo ou encontre mais de um, será apresentada a mensagem:

**"Não foi possível encontrar o Pedido de Frete através da Nota de Compra e Pedido de Compra. Será necessário efetuar a ligação do Pedido de Frete manualmente".**

- **Parceiro/Valor ou Manual:** selecionando esta opção, o sistema tentará localizar o Pedido de Frete através da query e, caso não encontre ou localize mais de um, será exibida a seguinte mensagem:

**"Não foi encontrado pedido de frete com o parceiro emitente e valor do desdobramento igual ao do CT-e. Será necessário efetuar a ligação do Pedido de Frete Manualmente".**

- **Parc./Valor ou Nro. Ped. Frete ou Manual:** esta opção, quando selecionada, fará com que, primeiramente, tente-se localizar o Pedido de Frete através da opção **"Parceiro/Valor"** e, caso não localize nenhum ou encontre mais de um, tentará através da opção **"Nro. de Pedido de Frete"**; ainda sim, não encontrando nenhum ou localizando mais de um, será emitida a mensagem a seguir:

**"Não foi possível determinar o Pedido de Frete pelo Parceiro/Valor ou Nro. Pedido de Frete! Será necessário efetuar a ligação do Pedido de Frete manualmente!".**

- **Nro. Ped. Frete ou Parc./Valor ou Manual:** com esta opção, primeiramente será localizado o Pedido de Frete através da opção Nro. de Pedido de Frete; caso não encontre nenhum ou encontre mais de um, tentará localizar por meio da opção Parceiro/Valor; não localizando nenhum ou encontrando mais de um, apresenta-se a seguinte mensagem:

**"Não foi possível determinar o Pedido de Frete pelo Nro. Pedido de Frete ou Parceiro/Valor! Será necessário efetuar a ligação do Pedido de Frete manualmente!".**

**Observação:** assim, caso alguma das opções retorne com problema ou solicite que você realize a vinculação manual, será apresentada na aba **"Pedido de Frete"** uma lista de pedidos de frete, para que seja possível efetuar a vinculação. Assim, bastará que você selecione o pedido desejado e acione o botão **"Ligar Pedido de Frete ao CT-e"**.

**Nota:** caso a Importação de XML não esteja liberada para reprocessar, será necessário acionar o botão **"Liberar para Reprocessamento"** e refazer o passo a passo de vinculação manual; feito isto, bastará que seja processado o arquivo e, assim, o sistema dará prioridade para o Pedido de Frete ligado manualmente.

**Sub-seção** **Pedido de Frete**

Nesta sub-seção, deve-se preencher os campos para que o sistema utilize as informações relativas ao frete na importação de CT-e de Terceiros.

Os campos **"Centro de Resultado"**, **"Natureza"** e **"Projeto"** possuem as seguintes opções:

- **Usa do Financeiro:** selecionando-se esta opção, o sistema utilizará as configurações realizadas na seção **"Movimentação Financeira"**;
- **Usa do Pedido de Frete ou do Financeiro:** quando esta opção for selecionada, o sistema utilizará, primeiramente, os valores do pedido de frete; caso não encontre, utilizará as opções configuradas na seção Movimentação Financeira.

**Observação:** para que seja possível encontrar o Cabeçalho de Nota que representa o Pedido de Frete, será utilizada a seguinte sequência:

- Com o XML do CT-e informado, utilize as NF-e's referenciadas àquele CT-e através da tag <infDoc> do arquivo XML.
- Após a referenciação das NF-e's, será utilizada a Chave de NF-e, sendo que, as NF-e's que não possuem chave de acesso não serão usadas.

**Nota:** caso o sistema não encontre Chaves de NF-e, será exibida a seguinte mensagem:

**"Não foi possível criar o Cabeçalho do CT-e! Verifique se a opção "Exige vínculo com notas" está marcada e se existe(m) NFe(s) referenciada(s) no XML do CT-e".**

- Em seguida, será realizada uma busca no banco de dados de todos os Cabeçalhos de Notas que possuam a Chave NF-e igual a Chave NF-e do XML;
- Após localizar todos os Cabeçalhos referentes às Chaves de NF-e, será verificado o Nro. Único do Pedido de Frete vinculado; caso encontre mais de um Nro. Único para os Cabeçalhos de Notas localizados, será apresentada a mensagem a seguir:

**"Erro ao tentar encontrar o Pedido de Frete do CT-e. Foi detectado mais de um Nro. de Pedido de Frete dentre as NFe's vinculadas ao CT-e. Nro. ùnico dos Pedidos de Frete: XX, XX."**

As marcações **"Copiar Rateio"** e **"Copiar Observação do Item"** não dependem unicamente do Pedido de Frete, portanto, estas possuem validações extras, que são:

- Na Observação do Item, caso não encontre item registrado para o Cabeçalho de Pedido de Frete, será apresentada uma mensagem informando que não foi possível copiar as Observações do Item do Pedido de Frete. Da mesma forma, para o Rateio, não sendo encontrado rateio para o Cabeçalho de Pedido de Frete, também apresenta-se a mensagem informando que não fora possível realizar a cópia do rateio.

**Observação:** a validação não impedirá o processamento de importação, apenas não copiará as informações de observação e rateio do Pedido de Frete para o Cabeçalho de CT-e.

**Seção** **Exigências de vínculos**

Nesta seção, existe o campo Exige vínculo com notas, que possui as seguintes opções:

- **Não exige:** se esta opção for escolhida, fará com que o sistema não busque as notas pelas chaves de NF-e do arquivo XML.
- **Exige:** através desta opção, o Sankhya Om fará a busca de notas pelas chaves de NF-e do arquivo XML.
- **Exige confirmada:** caso você selecione esta opção, ao processar a importação, as notas que fazem parte deste CT-e deverão obrigatoriamente, estarem com o status confirmada.

**Observação:** selecionando a opção Exige confirmada, se alguma nota vinculada ao CT-e ainda não estiver com status confirmado, o processamento será interrompido, indicando quais as notas que ainda estão pendentes de confirmação.

**Nota:** para que o Financeiro seja gerado com a Origem igual a **"Estoque"** é necessário que a marcação Exige vínculo com notas esteja selecionada.

**Observações:**

- Se o parâmetro **"Aquisição de serviço de frete com frete incluso - AQSERVFRETINC"** estiver ligado e no campo Exige vínculo com notas for selecionada a opção Exige, o sistema permitirá o vínculo com a importação do XML mesmo se o frete incluso já for informado na nota referenciada;
- Além disso, com o parâmetro AQSERVFRETINC ativado, em operações de Ordem de Despacho, o cálculo do frete para a melhor transportadora (seja automático ou manual), desde que configurado como **"Incluso"** (no [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) da nota, aba [Transporte](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abatransporte), campo **"Tipo do frete"**), será registrado no campo **"Vlr. frete calc."**;
- Para a importação de frete incluso do tipo **"CIF"** (configurado no Rodapé da nota, aba Transporte, campo **"CIF/ FOB"**), com o parâmetro AQSERVFRETINC ligado, o valor do frete será registrado no campo **"Vlr frete total"** do cabeçalho da nota referenciada.

A marcação **"Exige pedido de frete"** quando realizada, todas as chaves do arquivo XML que forem notas de venda, devem obrigatoriamente estar vinculadas a um pedido de frete, ou seja, devem possuir valor no campo **"Nro. Pedido Frete"** (insira este campo no layout da nota por meio da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota)).

Note também a marcação **"Exige CTE Complementado"** que, quando assinalada, no momento de processar o XML será realizada uma verificação da existência do CT-e Complementado na movimentação financeira através da chave do CT-e. Tendo-se a existência do CT-e Complementado, será realizada a importação e processamento do CT-e Complementar.

Ainda sobre a seção Exigências de vínculos, existe a marcação **"Vincular notas não referenciadas"** que, ao ser acionada, permitirá o vínculo de notas fiscais eletrônicas não referenciadas em um CT-e importado, sendo que, para que ocorra o referido vínculo, é necessário que você fique atento para as seguintes condições:

1. Emprega-se somente notas com o tipo de movimento de Compra;
2. O número da nota deve ser igual ao número do documento transportado no XML do CT-e;
3. O Parceiro da nota deve ter o mesmo CNPJ/CPF do remetente do XML do CT-e;
4. A Empresa da nota necessita portar o mesmo CNPJ do destinatário do XML do CT-e;
5. A nota de compra não pode possuir qualquer vínculo com outro CT-e ou financeiro de frete.

**Nota:** ao ligar o parâmetro **"Importar CTE com cabeçalho validando valor frete? - IMPVALFRECTECAB"**, pode-se realizar o vínculo do pedido de frete por meio da seção Pedido de Frete desta tela manualmente,  se esse vínculo não for realizado de maneira automática pelo sistema. Assim, o valor do frete entre o XML e o pedido de frete será validado.

**Seção** **Critério para rateio do valor do frete**

A seção Critério para rateio do valor do frete conta com o campo **"Tipo"**, onde define-se como será o rateio do valor do frete, se por Valor total de cada nota ou Peso total da mercadoria de cada nota. Esse rateio vai servir pra quando o CT-e importado estiver vinculado a mais de uma nota.

**Seção** **Tolerância entre pedido de frete e CT-e**

Por fim, na seção Tolerância entre pedido de frete e CT-e, temos o campo **"Percentual"**, onde deve ser informado um percentual de tolerância aceitável para o valor do frete, ou seja, esse percentual será multiplicado pelo valor do pedido de frete e se esse valor for maior que a diferencia entre o valor do pedido do frete e o valor do CT-e será exibida uma mensagem de divergência na tela.

Temos ainda considerações importantes para tratar a respeito do CT-e; tais informações podem ser acessadas nos tópicos **"Particularidades do CT-e"**, **"CT-e importado com Pedido de Frete"** e **"Rateio do Frete"**, disponíveis mais abaixo nessa documentação.

**Nota:** trabalhando-se no Portal de importação de XML, a Tributação do CT-e quando este é de Terceiros, também será uma informação que o sistema está apto a importar, alimentando a tag **<CST>**. A Tributação do CT-e, sendo este de terceiro, pode ser informada na Movimentação Financeira, no campo Tributação CT-e (este campo é disponibilizado sempre que o documento for um CT-e). Além disso, na geração dos Livros Fiscais por meio da tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953), a Tributação do CT-e quando este é de terceiros, também será gerada.

### Aba CT-e de Emissão Própria

A configuração pertinente à esta aba, é realizada por empresa, ou seja, nas Preferências da Empresa, aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abact-e), temos a marcação **"Importar CT-e de Emissão Própria"** que, ao ser realizada, os CT-e's importados poderão ser classificados como de Emissão Própria.

Determina-se nesta aba o Tipo de Operação, o Tipo de Negociação e o Serviço Padrão a serem preferencialmente considerados, em se tratando de CT-e's de Emissão Própria.

Para realização da importação de CT-e's de Emissão Própria, é essencial que o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado seja do Tipo de Movimento **"Venda"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abageral)); além disso, na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), o campo CT-e deve estar definido com a opção **"Emissão Própria"**.

**Observação:** na grade principal do Portal de Importação de XML, temos o campo **"Tipo de Importação CT-e"**, onde os documentos serão classificados automaticamente de acordo com a situação em que Tomador do Serviço e Emitente se enquadram no sistema, ou ainda, podem ter sua classificação ajustada manualmente, quando for o caso.

Ao ativar a marcação **"Preencher o campo Parceiro Entrega CT-e"**, o sistema preencherá automaticamente com o parceiro destinatário do XML a coluna Parceiro Entrega CT-e e irá buscar no XML o município inicio (**<cMunIni>**) e o município fim (**<cMunFim>**) para preencher o **"Cód. Cid. Inicio CT-e"** e **"Cód. Cid. Fim CT-e"** do [Cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#gradecabealho) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

### Aba CT-e como Documento Anterior

Esta aba é funcional para que empresas transportadoras que sejam contratadas para realizar frete de **"Subcontratação"**, **"Redespacho"** e/ou **"Redespacho Intermediário"**, possam importar o CT-e anterior a fim de replicar informações para a emissão do novo CT-e.

Ao ativar a marcação **"Importar CT-e como Documento Anterior"**, os campos da seção Configurações serão habilitados para preenchimento de forma obrigatória.

É necessário determinar o Tipo de Negociação a ser utilizado na emissão do CT-e, bem como os Tipos de Operação - TOP utilizados nos casos de Subcontratação, Redespacho e Redespacho Intermediário.

**Observação:** o sistema só permitirá que sejam informadas TOP's que tenham o **"Tipo de serviço CT-e"** da aba [CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde) preenchido com o tipo de serviço adequado a cada um dos campos. Além disso, a funcionalidade da aba CT-e como Documento Anterior não se aplica as TOP's que tenham o **"Tipo de movimento"** determinado como **"I-Financeiro"**, visto que a partir dessa rotina serão gerados documentos para emissão de CT-e, os quais devem ser provenientes das Centrais de Notas.

No modo grade do Portal de Importação de XML, deve-se selecionar a opção **"Documento Anterior"** no campo Tipo de Importação CT-e. Ao indicar um ou mais CT-e's que estejam classificados como Documento Anterior, quando acionar o botão ![Imagem 4: No modo grade do Portal de Importação de XML , deve-se selecionar a opção "Documento Anterior" no campo Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/26557946403479) **"Processar Arquivo(s)"** será aberto o pop-up  **"Informações para importar CT-e como Documento Anterior"** para que seja feita a escolha do Tipo do Serviço e a Empresa que serão considerados para todos os documentos que se enquadrem nesta situação. Assim, de acordo com as configurações da TOP, será gerado um documento na Central de Vendas ou Compras para a emissão do novo CT-e com base do CT-e anterior.

**Nota:** o documento não será confirmado automaticamente, pois nesse momento, deve-se  acrescentar informações específicas para emissão do CT-e, como, serviço, valor, dados do seguro, dentre outros.

Sendo assim, o financeiro será incluído na Movimentação Financeira, de acordo com as configurações da TOP, após a confirmação do documento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Configuração para liberações de divergências

**Importante:** para utilização desta opção, na tela de [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos), a opção **"Configurar"**, correspondente à tela Portal de importação de XML deve estar assinalada para os que poderão efetuar tal procedimento e irá proceder com a análise/liberação através da tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites).

Acionando a opção Configuração para liberações de divergências será aberto o pop-up de mesmo nome, onde determinam-se as medidas a serem tomadas quando ao importar-se um XML existam aspectos em desacordo:

![Imagem 5: Acionando a opção Configuração para liberações de divergências será aberto o pop-up de mesmo nome, onde determinam-se…](https://ajuda.sankhya.com.br/hc/article_attachments/15239938066711)

A marcação **"Exigir liberação p/ impostos"**, quando efetuada, e na importação de um XML existir uma divergência a esse respeito, esta será solucionada apenas com a liberação de um responsável. O liberador deverá ter para ele configurada, a liberação do evento **"76 - Diferença de impostos"** (tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para Liberação"**).

**Converter a origem dos produtos?:**se essa opção estiver ativada e o XML contiver produtos importados com códigos de origem 1 ou 6, o sistema pode solicitar um evento de liberação de divergências para ajustar diferenças na **"Origem do produto"** dentro do Cadastro de Produtos, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abageral). Isso acontece quando a origem informada no XML não corresponde ao que está configurado no sistema.

Para que a referida marcação esteja ativa, o campo **"Com diferença de NCM, CEST, Origem ou FCI"** deve estar diferente da opção **"Não considerar divergência"**.

Por meio do campo Com diferença de NCM, CEST, Origem ou FCI a validação e liberação das divergências será realizada de forma agrupada. Neste campo, estão disponíveis as seguintes opções:

- **Exigir liberação e alterar cadastro:** caso exista divergência, será necessária a liberação do usuário; assim que este for liberado, haverá atualização das informações;
- **Exigir liberação e não alterar cadastro:** neste caso, tem-se o mesmo processo, contudo, o sistema não atualizará as informações;
- **Não exigir liberação e alterar cadastro:** havendo divergência, dispensa-se a liberação, mas ainda assim, as informações serão atualizadas;
- **Não considerar divergência:** por esta alternativa, não haverá validação de divergências.
- **Validar campos individualmente:** ao escolher esta opção, os campos abaixo serão disponibilizados para que a validação e liberação de divergências seja realizada individualmente:

  - Com diferença de NCM;
  - Com diferença de CEST;
  - Com diferença de Origem;
  - Com diferença de FCI.

Esses campos disponibilizam as mesmas opções do campo Com diferença de NCM, CEST, Origem ou FCI.

**![Imagem 6: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/20671720381719) Informações adicionais:**

- Caso o campo Com diferença de Origem esteja configurado com a opção Não considerar divergência, o campo Converter a origem dos produtos ficará desabilitado;
- Caso opte por exigir a liberação, surgindo uma divergência, esta poderá ser liberada somente por um usuário responsável. O liberador deverá ter para ele configurada, a liberação do evento **"75 - Diferença entre NCM, CEST ou Origem"** (tela Usuários, botão Outras Opções..., opção Limites para Liberação) e assim como para o evento acima citado, proceder com a análise/liberação através da tela Liberação de Limites;
- Se a única divergência que ocorrer na importação for da origem do produto, quando no XML a origem for (1,2,3 ou 8) e em seu [Cadastro de Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) a origem for (0,4,5,6 ou 7), esta não será considerada uma divergência pelo sistema e sua atualização será feita diretamente no Cadastro do Produto convertendo a origem com base na informação do XML. Essa divergência também não será apresentada nos Detalhes dos Produtos na tela de Liberação de Limites;
- Se, as origens não possuírem divergências, essa liberação não será necessária. Se solicitada, assim que a liberação for efetuada através desta opção, convertem-se as origens dos produtos e realiza-se a alteração do cadastro dos mesmos para os valores 2 e 7, respectivamente. Se o campo **"Com diferença de NCM, CEST, Origem ou FCI"** estiver com a opção **"Não exigir liberação e alterar cadastro"** selecionada, dispensa-se a liberação, e a conversão seguirá a mesma lógica de forma automática;
- Se no XML a origem for 1 e no cadastro do produto a origem também for 1, será alterado para 2, se a origem for 6 e no cadastro do produto a origem também for 6, será alterado para 7;
- É importante ressaltar que, ao realizar o processo de validação e liberação individualmente, caso surja uma divergência e opte por exigir a liberação, o usuário responsável poderá efetuar a liberação, desde que tenha sido configurado para ele o evento **"85 - Diferença entre NCM"**, **"86 - Diferença entre CEST"**, **"87 - Diferença entre Origem"** ou **"88 - Diferença entre FCI"**, na tela Usuários, botão Outras Opções..., opção Limites para Liberação e assim como para o evento acima citado, proceder com a análise/liberação através da tela Liberação de Limites;

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Preferências para importação de NF-e

Quando acionada esta opção, será exibido o pop-up **"Preferências para importação de NF-e"**:

![Imagem 7: Quando acionada esta opção, será exibido o pop-up "Preferências para importação de NF-e" :](https://ajuda.sankhya.com.br/hc/article_attachments/24293810505367)

Neste pop-up é disponibilizado o campo **"Importar transportadora"** que tem por finalidade importar a transportadora da mercadoria para a nota de compra, quando se tratar da modalidade de frete por conta do emitente (igual a "0") ou quando o frete se apresentar zerado.

Efetuando a marcação **"Atualizar informações de combustível do produto conforme o XML"**, os campos correspondentes às informações de combustível no Cadastro de Produtos (aba [Combustível](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacombustvel)) serão atualizados, onde o campo **"Percentual de mistura GLP"** receberá o valor da tag **<pGLP>** e o campo Descrição ANP, recebe o valor da tag **<descANP>**; tal atualização irá ocorrer, apenas se o campo **"Gênero"** também presente no Cadastro de Produtos, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos), estiver definido como 27 - Combustíveis minerais, óleos minerais e produtos de sua destilação, matérias betuminosas, ceras minerais.

**Observação:** o sistema irá realizar a importação dos dados correspondentes aos campos **"Percentual de mistura de Gás Natural Nacional"**, **"Percentual de mistura de Gás Natural Importado"** e **"Valor de Partida GLP (sem ICMS)"**; como mencionado acima, para que a importação ocorra, é necessário que o item seja do gênero 27 - Combustíveis minerais, óleos minerais e produtos de sua destilação, matérias betuminosas, ceras minerais (Cadastro de Produtos, aba Impostos, campo Gênero).

Ao realizar a marcação **"Atualizar código da Anvisa do produto conforme o XML"**, o campo Cód. ANVISA presente na aba [Medicamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abamedicamentos) do Cadastro de Produtos será atualizado; porém, essa atualização somente irá ocorrer, se o campo Gênero também presente no Cadastro de Produtos, aba Impostos, estiver definido como 30 - Produtos farmacêuticos; este campo irá receber do XML, a informação presente na tag **<cProdANVISA>**.

Quando a marcação **“Utilizar CST calculado pelo sistema habilitada”** estiver habilitada, o sistema a calcula o CST durante a importação da nota fiscal, com base nas regras configuradas.

- Só terá efeito se no campo **"Cálculo de ICMS, IPI e ISS"** da TOP estiver preenchido como **"Calcula e digita"**.
- O CST será realmente calculado apenas se não houver divergência de impostos entre o XML e as regras do sistema.
- Se houver divergência, mesmo com a opção marcada, o sistema manterá o CST do arquivo XML.

Ao habilitar a marcação **"Atualizar Referência do Produto conforme código EAN do XML"** e importar o XML da NF-e de compra onde exista vínculo de produto equivalente, o sistema atualizará a informação do campo **"Referência"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abageral) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos) com a informação da tag **<cEAN>** do XML em cada produto.

Ao realizar a marcação **"Utilizar tributação calculada pelo sistema"**, o sistema irá considerar a Tributação calculada pelo Sankhya Om ao invés da presente no XML em todas as ocasiões que não existirem divergências de impostos.

A marcação **"Converter CST de ST do XML para CST cobrada anteriormente"** determina que o sistema realize a conversão da tributação antes de incluí-la na nota. Esta é uma configuração que atende à ocasiões específicas, em que estas possuam substituição tributária, ou seja, as CST's 010, 030 ou 070 serão convertidas para uma tributação de ST cobrada anteriormente, CST 060.

**Nota:** as duas últimas marcações mencionadas são relacionadas ao tratamento das Divergências de Impostos.

Com a marcação **"Desconsiderar validação de divergência de ST com Garantido integra"** habilitada, se o campo do item CODOBSPADRAO(default 0) estiver com o valor igual ao valor do parâmetro CODOBSGARANTIDO(default 0) e a soma de ICMS ST for igual a zero, as divergências de imposto na tela Portal de importação serão anuladas. Portanto, mesmo se ocorrer uma mudança de impostos entre a compra (XML) e o pedido vinculado (Central), não será visualizada pelo usuário.

Quando a marcação **"Permite alteração da nota na Central"** estiver acionada, será possível alterar os dados de uma nota na Central mesmo que seu status no Portal de Importação de XML esteja como **"Importada"**.

A marcação **"Priorizar descrição para vinculação de produtos"**, quando acionada, ao realizar o processamento dos arquivos, a descrição dos produtos no XML passará a ser um fator de diferenciação entre eles. Ou seja, uma das linhas do produto conterá o valor da tag <**cProd**> e a outra a descrição e o valor da tag <**xProd**>. Sendo assim, se houverem produtos com o mesmo Código, NCM e EAN, a descrição do produto será o critério que irá diferenciá-los.

Se esta opção não for marcada, o sistema não fará a divergência das informações referente às tags <**cProd**> e <**xProd**>, incluindo assim, uma nova linha.

Quando a marcação **"Permitir selecionar parceiros com mesmo CNPJ do emitente"** for efetuada, será possível realizar a alteração do Parceiro após a importação do arquivo; porém, apenas os Parceiros que encontram-se selecionados como **"Fornecedores"** e que não possuam o mesmo CNPJ correspondente ao XML serão aceitos.

**Observação:** somente será possível realizar a alteração do Parceiro quando a tela estiver em modo grade.

**Nota:** se o Cód. Parceiro Transportadora que você deseja inserir estiver cadastrado na tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) o sistema o permitirá que seja salvo, caso contrário, será exibida a seguinte mensagem:

**"Existe notas que não foram importadas porque o usuário não tem acesso para utilizar o parceiro X".**

**Importante:** apesar de serem apresentados os Parceiros que você possui a permissão de trabalhar, apenas será permitida a alteração destes através da digitação do Código do Parceiro, caso contrário, será exibida a seguinte mensagem:

**"Existe notas que não foram importadas porque o usuário não tem acesso para utilizar o parceiro X".**

Ao selecionar a marcação **"Importar dados do Intermediador?"**, o sistema irá adicionar os dados do XML dos campos **"Indicador de Presença para NF-e/NFC-e"**, **"Indicador de Intermediador/Marketplace"** e **"Intermediador de Transação"** aos campos de mesmo nome no [cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradecabealho) das [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras).

**Nota:** a informação do campo Indicador de Intermediador/Marketplace, é provinda do XML em formato de CPF/CNPJ, de forma que, o XML do campo mencionado será preenchido com o código do Parceiro. Se o cadastro deste não houver um CPF/CNPJ cadastrado, o campo ficará vazio.

No campo **"Modelo de importação para Produtor Rural"** informe o modelo fixo e específico a ser utilizado para importação para parceiros fornecedores que são Produtores Rurais.

A configuração deste último campo visa atender aos fornecedores que vendem apenas através de uma operação. Para estas ocasiões, o campo **"Modelo para Importação de XML Compra"** deve estar devidamente informado com o modelo a ser utilizado na importação do XML. Com base nessa configuração, a importação/inserção do XML no Portal de Importação de XML, irá ocorrer obedecendo algumas prioridades:

**1º -** Será verificado se o parceiro fornecedor do XML é produtor rural; se for, será utilizado o modelo de importação definido para esses fornecedores (Portal de importação de XML, botão Outras Opções, Preferências para importação de NF-e, campo Modelo de importação para Produtor Rural), se não;

**2º -** O sistema analisa se o parceiro fornecedor do XML possui algum modelo de importação determinado como fixo (Cadastro de Parceiros, aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abafiscal), campo Modelo para Importação de XML Compra); se possuir, este modelo será utilizado, se não;

**3º -** Será verificado se existe alguma combinação de CFOP(s) com o(s) CFOP(s) do XML (Portal de importação de XML, botão Outras Opções, Configuração de Modelo p/ Compra por CFOP); se existir, o modelo de importação encontrado na combinação será utilizado, se não;

**4º -** O sistema irá verificar se o XML possui o campo xPed preenchido para obtenção do Tipo de Operação; se houver, essa busca será feita, se não;

**5º -** Por fim, o sistema irá verificar se existe modelo de importação de XML nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) destinatária da nota importada.

Através do campo **"Usar como Dt. Faturamento"**, determine se a data de faturamento da nota no momento de processar o XML, será igual à data de emissão ou igual à data de entrada/saída da mesma.

O campo **"Opção para Data de Previsão de Entrega"** permite definir como será exibida a data de previsão de entrega. Temos as seguintes opções:

- Não ordenar pela data de previsão de entrega;
- Ordenar pela data de previsão de entrega do item da nota;
- Buscar mais de uma data de previsão de entrega para cada item da nota.

**Nota:** ao realizar o vínculo entre o Pedido de Compra e a Nota de Compra através da Importação do XML e, utilizando o cadastro de **"Unidades Alternativas"** para os Produtos, pode ocorrer algumas divergências de quantidades devido aos arredondamentos, fazendo com que os pedidos encontrem-se pendentes.

Para evitar esse comportamento, localize no pop-up **Preferências para importação de NF-e** o campo **Variação máxima da quantidade em percentual,** que permite criar uma margem de tolerância para pequenas diferenças de quantidade entre o pedido de compra e o XML da nota fiscal. Assim, os pedidos não ficam pendentes por divergências de arredondamento,  especialmente no uso de unidades de medida diferentes.

A variação funciona com as regras abaixo:

- Só é aplicada se a quantidade pendente do pedido for maior que zero.
- É válida para diferenças de quantidade tanto para mais, quanto para menos.

Exemplo prático: em um pedido de compra de 150 unidades, o campo **Variação máxima da quantidade em percentua**l está configurado com 10%. O sistema verifica se a variação é válida e em caso positivo, importa um XML com quantidades entre 135 e 165, marcando o pedido como atendido.

A fórmula que o sistema utiliza é: Tolerância % - ((Qtd. Pendente / Qtd. Negociada) \* 100). Se o resultado for um número positivo, a importação é aprovada.

Informando uma TOP no campo **"Top para simulação de impostos"**, será possível simular impostos ao processar um XML que utilize uma TOP com o campo **"Cálculo de ICMS, IPI e ISS"** configurado como **"Não calcula e não digita"** ou **"Não calcula e digita"**. Este comportamento serve apenas para simulação pois, ao conferir os impostos no campo **"Usar impostos"** do Portal de importação de XML, este estará desabilitado e com a opção **"Usar Impostos do Arquivo"** selecionada.

No campo **"Validar controle adicional"** teremos as opções **"Validar"** e **"Não validar"**, em que a opção Validar buscará informações do controle adicional no item do pedido para realizar o vínculo. Caso você selecione a opção Não validar, o sistema irá vincular o item do pedido sem necessidade do controle adicional.

**Observação:** a opção **"Validar"** só terá efeito se, na TOP de importação do documento, na aba [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaestoque), estiver ativada a marcação **"Exige conferência"**. Caso contrário, o vínculo não será realizado.

Os campos **"Centro do Resultado"**, **"Natureza"**, **"Projeto"**, **"Comprador"** e **"Tipo de negociação"** deverão ser configurados para que os mesmos sejam aproveitados do Pedido de Compra na inserção da Nota de Compra pela importação do seu arquivo XML. Desta forma, estes campos possuem as seguintes opções para seleção:

- **Modelo:** selecionando esta opção, ao realizar o processamento do XML, os campos citados acima terão seu preenchimento na grade do Portal de importação de XML, de acordo com o Modelo de Importação de XML configurado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa). Caso o modelo não possua a informação necessária, tem-se que, na grade também não possuirá; por exemplo, se o Comprador não encontrar-se preenchido no Modelo, na grade do Portal de Importação de XML o campo Comprador também se encontrará vazio.
- **Pedido do XML ou Modelo:** ao importar o XML e esta opção encontrar-se selecionada, fará com que o sistema encontre o Pedido de Compra a partir da tag **<xPed>** e, caso seja localizada a informação em comum entre o(s) pedido(s) disponível(is), a mesma deverá ser utilizada e preenchida na grade do Portal de Importação; de forma contrária, não sendo encontrada, a informação será preenchida de acordo com o Modelo de Importação de XML vinculado às Preferências da Empresa.
- **Pedido do XML ou Pedido Ligado Manualmente:** caso esta opção esteja selecionada, ao importar o XML, o sistema encontrará o Pedido de Compra a partir da tag **<xPed>** e, caso seja localizada a informação em comum entre o(s) pedido(s) disponível(is), esta deverá ser aproveitada e preenchida na grade do Portal; sendo encontrado mais de um pedido a partir desta tag e estes possuírem informações diferentes, a informação não será preenchida na grade do Portal.

**Nota:** Não sendo encontrado qualquer pedido a partir desta tag, ocorrerão divergências de pedidos ligados e, assim que esta divergência for solucionada, no momento da validação da importação, a informação será aproveitada de acordo com o(s) pedido(s) ligado(s) manualmente na aba Pedidos do Portal de importação de XML, sendo que, poderão ser ligados dois ou mais pedidos.

**Observação:** A informação apenas será aproveitada caso a mesma seja encontrada de forma comum entre os pedidos; caso os pedidos ligados manualmente não possuam as informações em comum, estas não serão preenchidas na grade do Portal.

- **Pedido do XML ou Pedido Ligado Manualmente ou Modelo:** esta opção quando selecionada, terá o mesmo comportamento da opção anterior, com a diferença de que, no momento em que os pedidos ligados manualmente possuírem informações diferentes, esta será preenchida e aproveitada de acordo com o Modelo de Importação de XML vinculado às Preferências da Empresa.
- **Pedido do XML ou Pedido Ligado Manualmente ou Rateio:** esta opção se aplica apenas aos campos Centro do Resultado, Natureza e Projeto. Ao selecioná-la, na importação do XML, se encontrado mais de um pedido com número igual ao xPed do XML e estes tiverem informações iguais, os dados do CR, Natureza e Projeto dos pedidos vinculados serão utilizados no cabeçalho da nota e no Portal, sem realização de rateio. Caso os pedidos de compra lançados tenham CR, Natureza e Projeto diferentes, no cabeçalho da nota e no Portal serão usados os dados do pedido de maior valor, configurados no Modelo de importação de XML vinculado às Preferências da Empresa. Além disso, será realizado o rateio proporcionalizado de acordo com os CR, Naturezas e Projetos.

**Importante:** Todos os comportamentos acima mencionados apenas serão executados quando a TOP de Compra exigir ligação de pedido no momento de Importar o XML, Processar o mesmo ou Validar a Importação.

Desta forma, diante do exposto acima, as informações referente à Centro do Resultado, Natureza, Projeto, Comprador e Tipo de negociação poderão ser aproveitadas de forma automática, sem que seja necessário alterar a Nota de Compra após sua inserção na Central de Compras; além disto, estas mesmas informações poderão ser alteradas manualmente no pop-up Preferências para importação de NF-e caso não possam ser obtidas automaticamente através dos Pedidos de Compras.

Os campos **"Nro. da Cotação"**, **"Observação"** e **"Observação do Item"** possuem as seguintes opções para seleção:

- **XML:** esta opção é a regra padrão do sistema, onde serão utilizadas as informações explícitas no XML da NF-e nas tag's **<infCpl>** e **<infAdFisco>**.
- **Pedido do XML ou XML:** selecionando esta opção, o sistema primeiramente utilizará as informações do Pedido de Compra vinculado na NF-e (**<xPed>** e **<nItemPed>**); caso não haja, utilizará a opção XML.
- **Pedido do XML ou Pedido Ligado Manualmente:** o sistema usará as informações do Pedido de Compra vinculado na NF-e (**<xPed>** e **<nItemPed>**) caso haja; por outro lado, não havendo, serão utilizadas as informações dos Pedidos Ligados Manualmente no Portal de Importação.
- **Pedido do XML ou Pedido Ligado Manualmente ou XML:** serão utilizadas as informações do Pedido de Compra vinculado na NF-e em primeiro momento, caso haja; não havendo, em segundo momento serão utilizadas as informações de Pedido Ligado Manualmente ao Portal de Importação; caso contrário, o sistema utilizará o XML processado.

Em relação ao campo **"Validação do Financeiro"**, este permitirá que você configure a validação financeira entre o sistema e o XML. Assim, você poderá escolher uma das seguintes opções:

- **Usar do sistema:** selecionando esta opção, ao processar o XML, não será validada a divergência financeira, sendo que, a Movimentação Financeira gerada para a nota importada deverá encontrar-se de acordo com o Tipo de Negociação configurado para a nota que será inserida, ou seja, deve-se respeitar a negociação financeira do sistema.
- **Usar do arquivo:** em relação à esta opção, quando selecionada, realizasse o processamento do XML, não será validada a divergência financeira e, a Movimentação Financeira gerada para a nota importada deverá estar em conformidade com o arquivo XML, ou seja, obedecendo a negociação financeira do XML; caso o XML não possua negociação financeira, será utilizada, automaticamente, a negociação financeira do sistema.

**Nota:** para verificar se o XML possui ou não uma negociação financeira, bastará validar a existência da tag **<cobr>**; existindo, isto indicará que o XML possui negociação financeira, caso contrário, o mesmo não possui.

- **Validar:** trata-se de comportamento padrão do sistema. Selecionando esta opção, ao processar o XML, será avaliada a divergência financeira para que o usuário decida qual será importada.

**Importante:** nos casos em que houver geração de Movimentação Financeira na inserção da nota a partir do processamento, esta apenas será gerada caso o Tipo de Operação - TOP usado encontre-se configurado para Atualizar Financeiro; caso contrário, não deverá ser avaliada a divergência financeira existente, mesmo que esteja configurada para isto, tampouco deverá ser gerada qualquer Movimentação Financeira para a nota inserida.

Através do campo **"Cópia de Rateio"**, no processo de ligação de pedidos feito no Portal de Importação de XML, será possível copiar o(s) rateio(s) do(s) pedido(s) de compra para a nota importada.

**Observação:** esta funcionalidade será aplicada na ligação dos pedidos automáticos feitos pela tag **<xPed>** e na ligação manual realizada, quando ocorrerem divergências de pedidos ligados.

O campo **"Valor limite aceitável de divergência de ICMS-ST"** funcionará apenas quando a marcação **"Apura divergência de ICMS-ST"** estiver selecionada. Assim, informe o valor em R$ (reais) aceitável de divergência para o imposto de ICMS-ST.

**Nota:** desta forma, deverão ir para a rotina de [Apuração de Divergências de ICMS-ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595094) as notas que possuam as condições abaixo no Portal de Importação do XML:

- Item com ST no XML importado X item sem o ST calculado no Sankhya Om;
- Item sem o ST no XML importado X item com ST calculado no Sankhya Om;
- Item com ST no XML importado X item com ST calculado no Sankhya Om e que a divergência de valores seja acima de R$0,50.

**Importante:** nosso sistema possui o seguinte comportamento na importação de uma NF-e pelo Portal de Importação de XML:

- O campo **"Dt. Negociação"** da nota utiliza o valor da tag **<dhEmi>**;
- Os campos **"Dt. Entrada"** e **"Dt. Saída"** possuem duas regras:

Se o parâmetro **"Usa dhSaiEnt na import. do XML do portal de imp.? - DHSAIENTIMPXML"** estiver ligado ou se a NF-e for de Emissão Própria, o valor da tag **<dhSaiEnt>** será utilizado;

De forma contrária, será utilizada a data e hora atual.

- O campo **"Hr. Ent./Saída"** utiliza a mesma regra dos campos Dt. Entrada e Dt. Saída, porém, este utilizará apenas a hora;
- O campo **"Dt. Movimento"** possui duas regras:

Se o parâmetro Usa dhSaiEnt na import. do XML do portal de imp.? - DHSAIENTIMPXML estiver habilitado ou se a NF-e for de Emissão Própria, o valor da tag **<dhEmi>** é utilizado;

Caso contrário, o valor da tag **<dhSaiEnt>** que será usado;

- Em relação ao campo **"Dt. Faturamento"**, este utiliza as regras a seguir:

Se a NF-e for de Emissão Própria, o valor da tag **<dhEmi>** é utilizado;

Se o campo **"Usar como Dt. Faturamento"** tiver com a opção **"Dt. Emissão da Nota"** selecionada, o valor da tag **<dhEmi>** será utilizado;

Caso contrário, a mesma regra para preencher os campos Dt. Entrada e Dt. Saída será aplicada aqui.

Quando você selecionar a marcação **"Filtrar somente pedidos?"**, na aba Pedidos, o sistema trará apenas os pedidos de compra dos orçamentos, caso essa opção for desmarcada nas Preferências para importação de NF-e serão filtrados os pedidos e orçamentos.

Através do campo **"Configuração data extemporânea"** você escolhe a quantidade de dias em que o sistema deverá analisar para identificar se a nota é ou não extemporânea, de acordo com as seguintes opções:

- Sem Config;
- Após 15 dias;
- Após 30 dias;
- Após 45 dias;

**Observação:** a contagem é feita a partir da data de negociação caso seja nota de emissão própria e, a partir da data de entrada e saída, se for de terceiro.

Assim, ao acessar a nota na Central, após a importação/processamento do XML, o campo **"Data extemporânea"** apresentará a data de processamento do XML pelo sistema.

A marcação **"Permitir vinculo Manual para NFe Devolução para NFe Venda"** quando efetuada, determina se o Portal de Importação permitirá o vínculo manualmente das referências entre as NFe de Devolução e NFe de Venda.

**Nota:** durante o processamento do arquivo importado, caso o XML da nota de devolução apresente alguma inconsistência com relação à nota de origem, será exibida a mensagem abaixo:

**"Devolver nota com erro de validação".**

Assim, a aba **"Seleção de notas de venda"** será habilitada na tela Portal de importação de XML, contendo as notas de venda do mesmo parceiro da nota de devolução para serem vinculadas:

![Imagem 8: Assim, a aba "Seleção de notas de venda" será habilitada na tela Portal de importação de XML , contendo as notas de…](https://ajuda.sankhya.com.br/hc/article_attachments/7631791472919)

Ainda nessa aba, na grade **"Itens disponíveis"**, caso você queira editar a quantidade de produtos disponíveis, clique duas vezes sobre a coluna **"Disponível"** e informe o valor desejado.

Para efetuar a importação do arquivo utilizando a opção **"Usar Impostos do Arquivo"** do campo **"Usar impostos"** da aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML#divergnciasdeimpostos) dessa tela, habilite a marcação **"Realizar conversão do CST de IPI do XML"**, assim, o código do arquivo XML será convertido para o CST do sistema e apresentará a informação referente ao CST de IPI para escrituração. Porém, caso o arquivo não tenha o código CST, o processo não será interrompido, e assim, ao final deste a seguinte mensagem será apresentada:

**"Arquivo NF-e: xxxx - xxxxxxxxxx importado com sucesso!**

**A opção “Realizar conversão do CST de IPI do XML” nas Preferências para importação de NF-e está marcada e não foi possível encontrar CST de IPI no XML. Verifique a opção marcada."**

Quando a marcação **"Considerar valores de IPI da nota de Venda na nota da Devolução de Venda"** for habilitada, ao importar uma nota de Devolução de Venda de terceiro com o campo **"Chave NF-e"** do cabeçalho preenchido e, consequentemente esta seja referenciada na tag **<refNFe>**, ao processar a nota o sistema irá recuperar os valores do IPI da nota fiscal da nota de venda e aplicá-las na Devolução desta. 

**Observação:** o valor do IPI será proporcionalizado em caso de devolução de venda parcial.

Caso queira que a tag **<vIPIDevol>** seja gerada e destacada no xml, o sistema deve ser configurado da seguinte maneira:

- Além de acionar a marcação Considerar valores de IPI da nota de Venda na nota de Devolução de Venda;
- Ative também as marcações **"Trabalha com IPI?"** e **"Destacar o IPI na tag <vIPIDevolv> em devoluções"** da aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades) das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa);
- Na tela [Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), defina o campo **"Tipo de Movimento"** com a opção **"D-Devolução de Venda"**;
- Na mesma tela, aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), configure o campo **"Cálculo de ICMS, IPI e ISS"** com a opção **"Não Calcula e Digita"**;
- Por fim, a NF-e deve ser igual a terceiros.

Com a marcação **"Considerar CFOP de bonificação na importação do XML"** habilitada, o sistema irá validar a tag **<CFOP>** do XML de cada um dos itens e aplicar as conversões abaixo:

- Quando o CFOP da tag acima for 5910, esta será convertida para 1910;
- No entanto, quando este for 6910, será convertido para 2910.

Porém, com a marcação acima desligada, ao importar um XML com produtos que contêm a tag **<CFOP>** igual 5910 ou 6910 e abri-lo na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), o sistema irá aplicar a regra de conversão e cálculo do CFOP conforme os campos das seções **"CFOP's para FORA do estado"** e **"CFOP's para DENTRO do estado"** do [Cadastro no Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)).

**Observação:** para que o sistema realize a conversão do CFOP, além da marcação Considerar CFOP de bonificação na importação do XML acionada, o campo **"Tipo NF-e"** da tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354#inclusodosarquivosnoportal) deve ser configurado com a opção **"NF-e Normal Compra"**.

A marcação **"Gravar chaves referenciadas não vinculadas"** ativa a gravação das chaves referenciadas inexistentes no sistema, junto ao cabeçalho da nota. Além disso, ela ativa a aba **“Chave Referenciada”** no Cabeçalho do Portal de Importação do XML.

**“Validar o CSOSN para o registro do CFOP nas entradas de fornecedores do simples nacional”** também é uma marcação, mas que tem como finalidade  realizar o registro do CFOP durante a importação de XML emitido por um parceiro optante pelo Simples Nacional, com base na CSOSN.

Logo, ao importar um XML com características do Simples Nacional, ou seja, contendo CSOSN e com a respectiva marcação habilitada, o sistema adotará as seguintes regras:

- Para itens classificados com CSOSN tributados (101, 102, 300, 400 e 900), o "Tipo de Substituição", do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos), será considerado **"N = Não tem"**;
- Nesse caso, o CFOP registrado na nota será o indicado no TOP configurado.

Essa funcionalidade será aplicada apenas aos produtos configurados com o campo **"Usado como"**, também do Cadastro de Produtos, definido como **"Revenda"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Preferências para importação de NF-e de Emissão Própria

Acionando esta opção temos a exibição do pop-up **"Preferências para importação de NF-e de Emissão Própria"**:

![Imagem 9: Acionando esta opção temos a exibição do pop-up "Preferências para importação de NF-e de Emissão Própria" :](https://ajuda.sankhya.com.br/hc/article_attachments/4410728315671)

Através deste pop-up serão inseridas as informações que irão possibilitar a importação dos arquivos de XML das notas fiscais eletrônicas de emissão própria. Sendo que, as TOP's utilizadas deverão conter as seguintes configurações:

[Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP):

- Na aba [Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpresso), o campo **"NF-e"** deve estar configurado com a opção **"Emissão Própria"**;
- Configure na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), o campo **"Cálculo de ICMS, IPI e ISS"** selecionando a opção **"Não calcula e digita"**;
- Na aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias) serão configurados todos os impostos pertinentes as despesas acessórias de frete, destaque, embalagem e seguro.

[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa):

- Na aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais), acione a marcação **"Importa NF-e de emissão própria?"**.

**Importante:** o sistema suportará a importação de NF-e Emissão Própria de empresa optante pelo Simples Nacional via Portal de Importação de XML. Para isso, ressalta-se que além dos XML emitidos com CRT 3 - Regime Normal, o sistema validará também os CRT abaixo:

1 - Simples Nacional (<CRT>1</CRT>);

2 - Simples Nacional - excesso de sublimite da receita bruta (<CRT>2</CRT>).

**Observação:** o Tipo de Negociação utilizado irá determinar como serão gerados os financeiros das notas importadas.

Será possível realizar a importação de NF-e de Compra de Emissão Própria e o Parceiro com CPF/CNPJ iguais e IE diferentes, desde que o campo **"Tipo de Operação para Compra"** encontre-se preenchido com a TOP a ser utilizada e a marcação **"Considera Inscrição Estadual para seleção do parceiro da importação"** esteja efetuada.

Também é possível efetuar a importação de NF-e de Venda de Emissão Própria e o Parceiro com CPF/CNPJ iguais e IE diferentes, desde que o campo **"Tipo de Operação para Venda"** esteja preenchido com a TOP de venda a ser utilizada e a marcação Considera Inscrição Estadual para seleção do parceiro da importação esteja acionada. 

**Observação:** quando a marcação Considera Inscrição Estadual para seleção do parceiro da importação estiver realizada, o sistema buscará o Parceiro por IE e CPF/CNPJ iguais à informação constante no XML.

**Nota:** se a empresa emitente da NF-e possuir a configuração do campo Importa NF-e de emissão própria? e emitir a nota no Portal de Vendas, esta será importada como uma nota de Terceiros. A nota em questão também será importada dessa forma, caso seja emitida no Portal de Importação de XML e confirmada por meio do Portal de Vendas.

Ao selecionar a marcação **"Importar dados do Intermediador?"**, o sistema irá adicionar os dados do XML dos campos **"Indicador de Presença para NF-e/NFC-e"**, **"Indicador de Intermediador/Marketplace"** e **"Intermediador de Transação"** aos campos de mesmo nome no [cabeçalho](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradecabealho) das [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras).

**Nota:** a informação do campo Indicador de Intermediador/Marketplace, é provinda do XML em formato de CPF/CNPJ, de forma que, o XML do campo mencionado será preenchido com o código do Parceiro. Se o cadastro deste não houver um CPF/CNPJ cadastrado, o campo ficará vazio.

**Observação**: a configuração do campo "Top para simulação de impostos" nas 'Preferências para importação de NF-e' influência diretamente na geração da nota de emissão própria. Caso a nota gerada não seja a configurada com a top  como emissão própria, analisar o campo 'Top para simulação de impostos'

A documentação abaixo foi inserida no artigo Portal de importação de XML - Botão Outras Opções:

Em relação ao campo **"Validação do Financeiro"**, este permitirá que você configure a validação financeira entre o sistema e o XML. Assim, você poderá escolher uma das seguintes opções:

- **Usar do sistema:** selecionando esta opção, ao processar o XML, não será validada a divergência financeira, sendo que, a Movimentação Financeira gerada para a nota importada deverá encontrar-se de acordo com o Tipo de Negociação configurado para a nota que será inserida, ou seja, deve-se respeitar a negociação financeira do sistema.
- **Usar do arquivo:** em relação a esta opção, quando selecionada, realizasse o processamento do XML, não será validada a divergência financeira e, a Movimentação Financeira gerada para a nota importada deverá estar em conformidade com o arquivo XML, ou seja, obedecendo à negociação financeira do XML; caso o XML não possua negociação financeira, será utilizada, automaticamente, a negociação financeira do sistema.

**Nota:** para verificar se o XML possui ou não uma negociação financeira, bastará validar a existência da tag **<cobr>**; existindo, isto indicará que o XML possui negociação financeira, caso contrário, o mesmo não possui.

- **Validar:** trata-se de comportamento padrão do sistema. Selecionando esta opção, ao processar o XML, será avaliada a divergência financeira para que o usuário decida qual será importada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Configuração de Modelo p/ NF-e Compra por CFOP

Ao acionar esta opção, será aberto um pop-up com esta mesma nomenclatura, onde define-se uma equivalência entre o CFOP da Nota de Compra e o modelo de importação. Para cada combinação de CFOP realizada neste pop-up, é preciso que exista um modelo de importação.

![Imagem 10: Ao acionar esta opção, será aberto um pop-up com esta mesma nomenclatura, onde define-se uma equivalência entre o CFOP…](https://ajuda.sankhya.com.br/hc/article_attachments/15239918182039)

**Nota:** no momento da importação do XML, para definição do modelo de importação a ser utilizado, o sistema levará em consideração todas as CFOP's da nota de compra. Caso a nota possua mais de três CFOP's entre os itens, não será possível definir o modelo de importação a partir das combinações de CFOP existentes.

**Observação:** esta opção só funcionará ao realizar a importação do XML de um Produtor Rural.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Validar TOP na importação do XML

Quando a marcação **"Validar TOP na importação de XML"** estiver selecionada, no campo **"Cód. Tipo Operação"** será possível selecionar apenas as TOP's pré-definidas no cadastro (sendo esta definição, realizada na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514) e posteriormente, vinculado no campo **"Modelos de notas e pedidos"**, aba [Modelo de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abamodelodeimportaodexml) da tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa)), não permitindo a utilização de qualquer outro código. Porém, quando desmarcada, o sistema disponibilizará apenas as TOP's ativas, sendo que todas estas poderão ser utilizadas.

**Observação:** a utilização do parâmetro **"TOP a ser utilizada no portal de importação de XML - TOPIMPORTXML"** possibilita a utilização de duas opções, a saber:

- TOP de destino do pedido de compra;
- Modelo de importação.

Optando-se por uma destas duas alternativas, o sistema apresenta o seguinte comportamento:

Quando o parâmetro TOPIMPORTXML estiver igual a **"TOP de destino do pedido de compra"**, o sistema sempre irá verificar o campo **<xPed>** do arquivo XML importado e tentar encontrar os pedidos de compra no sistema a partir do número encontrado.

- Se o XML importado não possuir a informação do campo **<xPed>**, o sistema não irá preencher a TOP para importação e ficará a seu cargo a informação da mesma.
- Se o XML importado possuir a informação do campo **<xPed>**, mas os pedidos de compra não forem encontrados no sistema, este não irá preencher a TOP para importação e ficará a seu cargo a informação da mesma.
- Se encontrar mais de um pedido, que tenham mais de uma TOP, o sistema não irá utilizar qualquer TOP para processar a importação do XML, ficando a seu cargo informar qual TOP deseja usar.
- Se encontrar um ou mais pedidos que possuam a mesma TOP, o sistema irá verificar qual a TOP de destino configurada em seu cadastro.

Quando o parâmetro TOPIMPORTXML estiver definido com a opção **"Modelo de importação"**, o sistema sempre irá utilizar a TOP do modelo de importação para processar a importação do XML.

Vale salientar que, em ambos os casos, você poderá editar a TOP sugerida pelo sistema para realizar a importação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Desconsiderar Ped. de Venda na Importação

Quando essa marcação está ativada, o sistema passa a exibir apenas pedidos de compra na lista de pedidos disponíveis ao ligar pedidos mais antigos.

Dessa forma, o usuário pode controlar a exibição dos pedidos conforme a sua necessidade, garantindo que apenas os pedidos relevantes sejam exibidos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)

## Ajustar notas para DRCST (Chave e Sequência Fiscal)

Por meio desta opção, o sistema irá utilizar os itens do XML de importação do Registro 2130 para ser utilizado na Geração do DRCST.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#top)
