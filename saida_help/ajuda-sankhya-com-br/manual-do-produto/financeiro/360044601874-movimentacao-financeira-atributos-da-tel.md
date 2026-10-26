---
id: "360044601874"
titulo: "Movimentação Financeira - Atributos da Tela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-09-03T10:30:10Z"
rotulos: ["AJUDA DO SKW", "Configuração", "Parceiro", "IMPMODCTABAIX", "Movimentação Financeira", "Movimentação Financeira - Atributos da Tela manual", "USADESCFIN", "QTDMAXREGEXPORT", "Impostos", "Estoque", "Financeiro", "TRAVAALTDHMOV", "OFEROPCBAIXTIT", "DECVLRMOEDA", "USARPARCADMFIN", "PERMTROCOCHEQUE", "ESTRECOMPOPC", "UTIORCDTENTSAI", "PERMTROCOCARTAO", "ABRERATDUPFIN", "BAIXAAGRUMOEDA", "DEFCAMGRD", "AGRTITMONREMEDI", "VALIDATIPONAT", "TROCATOPFIN", "USAFATPROVORC", "TAMVARSHISTCTBZ", "USAPRDTDTLANC", "RENNOSSONUM", "SUBSTHISTFIN", "TEFGATEWAY", "br.com.sankhya.fin.cad.movimentacaoFinanceira", "CONFAUTTEF", "TEFRECTIMEOUT", "Busca por receitas despesas e datas", "Campos principais e obrigatórios", "Cálculo e campos adicionais", "BLOQALTRAFINCTB"]
---

# Movimentação Financeira - Atributos da Tela

Neste artigo, conheça os componentes da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira); seus campos com seus respectivos preenchimentos, seus botões e as situações que estes podem e/ou devem ser acionados.

| Atributos da Tela |
| --- |
| [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#filtros) |
| [Guias da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela) |
| [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela) |
| [Parâmetros que influenciam nessa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#par%C3%A2metrosqueinfluenciamnessarotina) |

---

## Filtros

### Filtros Rápidos

Na parte superior da tela são apresentados os Filtros Rápidos. 

Os filtros **"Receitas + Despesas"**, **"Pendentes + Baixados"** e **"Real + Provisão"** trabalham em pares, ou seja, sempre será necessário assinalar:

- Receitas e/ou Despesas;
- Real e/ou Provisão;
- Pendentes e/ou Baixados.

![Imagem 1: Pendentes e/ou Baixados.](https://ajuda.sankhya.com.br/hc/article_attachments/21350332202519)

Ao deslizar o scroll para a direita é possível refinar ainda mais a busca pelos títulos usando os filtros:

| - Data de Vencimento; - Data da Negociação; - Data da Baixa; - Data da Entrada e Saída; - Número da Nota; | - Número Único (da nota); - Número Único do Pedido; - Parceiro; - Histórico. |
| --- | --- |

[GIF animado: Imagem 2: Histórico.](https://ajuda.sankhya.com.br/hc/article_attachments/21350964247191)

Na busca dos títulos utilizando a **"Data de Vencimento"** é possível configurar o parâmetro **"Qtd máxima dias na Movimentação financeira - MAXDIASMOVFIN"** com o número máximo de dias que a pesquisa irá retornar. Considere o seguinte exemplo dessa rotina:

Informando no parâmetro 10 dias e no filtro de Data de Vencimento um período superior a 10 dias ou ao deixar a Data de Vencimento em branco, o sistema retornará a seguinte mensagem:

**"Informe um período de até 10 dias para "Data de vencimento" ou informe um filtro por Número único."**

Ao realizar uma pesquisa pelo campo **"Nro Único do Pedido"** serão exibidos tanto os títulos originais (Origem: Estoque), quanto os títulos renegociados (Origem: Financeiro). Dessa forma, os pedidos em movimentações perdem a referência de nota x pedido, como por exemplo, as renegociações. Lembrando que, esse campo não é alimentado automaticamente pelo Nro único do pedido dos Portais. Considere ainda que, ele é de preenchimento manual/filtro na Renegociação de Títulos ou na própria Movimentação Financeira.

Pode-se ainda filtrar pelas **"Empresas"**, **"Naturezas"**, **"Centro de Resultado"**, **"Contas Bancárias"**, **"Bancos"** e/ou **"Projetos"**, informando um ou 'N' registros da entidade que está utilizando.

![Imagem 3: Caso esteja utilizando a tela com o seu Usuário e não configure nenhum filtro no Painel de Filtros , o sistema buscará…](https://ajuda.sankhya.com.br/hc/article_attachments/16423433429655) Caso esteja utilizando a tela com o seu Usuário e não configure nenhum filtro no Painel de Filtros, o sistema buscará as configurações de filtro do usuário SUP. No entanto, ao limpar ou modificar o registro de um filtro, o sistema deixará de buscar as configurações do usuário SUP.

Informados os filtros, clique no botão ![Imagem 4: Informados os filtros, clique no botão "Aplicar" para que o resultado das configurações seja exibido na tela.…](https://ajuda.sankhya.com.br/hc/article_attachments/21380978557591) **"Aplicar"** para que o resultado das configurações seja exibido na tela. Dependendo do caso, utilize a tela em ![Imagem 5: Informados os filtros, clique no botão "Aplicar" para que o resultado das configurações seja exibido na tela.…](https://ajuda.sankhya.com.br/hc/article_attachments/21351501151639) **"Modo Formulário"** que pode facilitar a localização dos registros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#top)

### Filtros Personalizados

Além da utilização dos filtros fixos na tela descritos acima, pode-se através do botão ![Imagem 6: Além da utilização dos filtros fixos na tela descritos acima, pode-se através do botão "Filtros" realizar a formulação…](https://ajuda.sankhya.com.br/hc/article_attachments/21350878174615) **"Filtros"** realizar a formulação de filtros específicos para exibição mais ágil dos títulos desejados.

[GIF animado: Imagem 7: Além da utilização dos filtros fixos na tela descritos acima, pode-se através do botão "Filtros" realizar a formulação…](https://ajuda.sankhya.com.br/hc/article_attachments/21351183069591)

Quando o parâmetro **"Ordenar filtros por ordem alfabética? - ORDENAFILTROS"** estiver ativado, os filtros personalizados que forem criados terão seus nomes apresentados para escolha em ordem alfabética.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#top)

## Guias da Tela

Para acessar as guias da tela Movimentação Financeira, clique em ![Imagem 8: Para acessar as guias da tela Movimentação Financeira , clique em "Modo Formulário" . A seguir, saiba como configurar…](https://ajuda.sankhya.com.br/hc/article_attachments/21351501151639) **"Modo Formulário"**. A seguir, saiba como configurar cada uma delas.

| [Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal) | [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Lan%C3%A7amento) |
| --- | --- |
| [Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Cobran%C3%A7a) | [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#impostos) |
| [Despesas Administrativas/Judiciárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#DespesasAdministrativas/Judici%C3%A1rias) | [GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#GNRE) |
| [Dados do Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#DadosdoCart%C3%A3o) | [EFD Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#EFDReinf) |

![Imagem 9: Por meio do botão Configurações pode-se ordenar os campos de cada guia.](https://ajuda.sankhya.com.br/hc/article_attachments/21352113026711) Por meio do botão ![Imagem 10: Por meio do botão Configurações pode-se ordenar os campos de cada guia.](https://ajuda.sankhya.com.br/hc/article_attachments/21352113037335) [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Configura%C3%A7%C3%B5es) pode-se ordenar os campos de cada guia. 

### Principal

Nesta guia são apresentados os campos globais da Movimentação Financeira; os dados aqui presentes são de preenchimento obrigatório e são automaticamente gerados quando a inclusão do título é concluída.

![Imagem 11: Nesta guia são apresentados os campos globais da Movimentação Financeira ; os dados aqui presentes são de preenchimento…](https://ajuda.sankhya.com.br/hc/article_attachments/21352835646487)

O **"Nro Único"** é o código único do título gerado internamente pelo sistema que servirá como controle interno. É um campo muito utilizado para localizar lançamentos.

**Observação:** independente da marcação **"Numeração Automática"** localizada no botão **![Imagem 12: Observação: independente da marcação "Numeração Automática" localizada no botão "Configurações" estar efetuada, o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/21352113037335) "Configurações"** estar efetuada, o campo Nro Único seguirá a numeração automática, desse modo, não é possível realizar a alteração de forma manual.

Em **"Nro Nota"**, informe a numeração da nota fiscal ou número do documento. Nos lançamentos com origem nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) fica registrado aqui o número da nota fiscal e este não poderá ser alterado.

Ao lado do campo Nro Nota é possível visualizar o botão ![Imagem 13: Ao lado do campo Nro Nota é possível visualizar o botão "Ir para a Central de Notas" ; ao acioná-lo, a tela será…](https://ajuda.sankhya.com.br/hc/article_attachments/21381424131351) **"Ir para a Central de Notas"**; ao acioná-lo, a tela será redirecionado para o registro da referida nota, caso esta possua origem financeira.

Tem-se no campo **"Série da Nota"**, a informação oriunda da Central correspondente à série da nota fiscal; algumas notas fiscais podem ter além do número, uma série específica, por exemplo, série D, série única, entre outras.

Informe no campo **"Parceiro"**, o Fornecedor ou Cliente do título, de despesa ou receita, respectivamente. Seu cadastro é previamente realizado na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros).

Tem-se no campo **"Empresa"**, a empresa responsável pela negociação com o parceiro, seja este fornecedor ou cliente. As empresas são previamente incluídas no sistema por meio da tela [Cadastro de Empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas) e ativadas para uso através das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa).

#### Seção Geral

![Imagem 14: Seção Geral](https://ajuda.sankhya.com.br/hc/article_attachments/21352835657623)

O campo **"Origem"** indica se o título foi originado nas Centrais (a partir de pedidos/notas de venda, compra, entre outras) ou no Financeiro, se for um título incluído diretamente na Movimentação Financeira; com isso, poderá ser preenchido com a opção **"Estoque"**ou **"Financeiro"**, respectivamente.

O **"Desdobramento"** de um título, refere-se ao número ou letra correspondente a parcela do título, ou seja, o desdobramento 1 equivale a 1ª parcela, o desdobramento 2 equivale à parcela 2, e assim sucessivamente. A geração dos desdobramentos de um título é derivada da configuração realizada no [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) utilizado no título.

Será possível escolher no campo **"Tipo Operação"** os [Tipos de Operação- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) cujo Tipo de Movimento é Financeiro. É um campo necessário para integração com Contabilidade, Livros Fiscais ou Controle Orçamentário.

Utilize o campo **"Número da Duplicata"** para registrar o número da duplicata, é uma forma de agrupar títulos. Este campo pode ser gerado automaticamente ao formar uma duplicata, na tela de [Formação de Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114693-Forma%C3%A7%C3%A3o-de-Duplicatas "br.com.sankhya.mgefin.formacao.duplicata"), onde todos os títulos que farão parte da duplicata formada irão possuir a mesma numeração.

O campo **"Desdobramento Duplicata"** diferencia as parcelas da duplicata, assim como o desdobramento diferencia as parcelas da nota.

Tem-se no campo **"Nosso Número"** a identificação do número do boleto que poderá ser gerado na tela [Impressão de boleto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-). Apresenta também o número do cheque que foi emitido durante a baixa de um título.

O campo **"Vendedor"** é alimentado com o código do vendedor responsável pela venda nas negociações geradoras de [Receita](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oquesoreceitasedespesas). Esta informação também é empregada na validação de restrição de TOP na baixa e para impressão na autenticação de documentos.

Se o título financeiro selecionado for gerado a partir da rotina de [Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/24340556304919-Gest%C3%A3o-de-Fechamento-de-Caixa#Ocorr%C3%AAncias) na tela [Gestão de Fechamento de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/24340556304919-Gest%C3%A3o-de-Fechamento-de-Caixa), o número da ocorrência será informado no campo **"Nr. da Ocorrência Caixa"**.

**Importante:** para excluir um título financeiro gerado a partir de ocorrências, é necessário limpar as informações do campo Nr. da Ocorrência Caixa.

Caso existam, informe no campo **"Despesas com Cartório"** o valor das despesas com cartório.

Tem-se no campo **"Valor do IRF"** o valor do IRRF calculado na nota; pode-se também incluir esta informação manualmente no próprio campo.

Se o parâmetro **"Percentual da Multa - PERCMULTA"** estiver igual a zero, o valor informado no campo **"Valor da Multa"** será apresentado, automaticamente, no campo Multa na tela de baixa e o sistema o levará em consideração para cálculo do título vencido. Se este parâmetro estiver diferente de zero, a Multa será modificada, no momento da baixa do título vencido, de acordo com o valor informado no parâmetro, independente do valor informado neste campo.

O campo **"Valor do Cheque"** corresponde ao valor total pago ou recebido. É utilizado para cálculo do troco, quando o cliente paga um valor maior que o valor do desdobramento. Por exemplo:

Ao pagar uma conta de valor igual a R$66,00, o cliente utiliza uma nota de R$100,00; deste modo, no campo Valor do Cheque fica registrada a quantia de R$100,00.

No campo **"Taxa Administradora"** será apresentado a tarifa calculada de acordo com o percentual informado no campo % Taxa Administradora presente no [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) ([aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)), que se refere a taxa cobrada pela administradora de cartões de crédito nas operações relacionadas ao TEF (Transferência Eletrônica de Fundos).

**Observação:** não será permitida a alteração do valor da Taxa Administradora, caso o parâmetro **"Reiniciar Tx Admin. na alteração do título? - RECTXADMFIN"** esteja ligado.

Tem-se no campo **"Valor do Vendor"** o valor do vendor calculado (acrescido) na nota. Trata-se de uma alternativa de financiamento de vendas que permite à uma empresa vender o seu produto a prazo e recebê-lo à vista. O banco, mediante uma taxa de intermediação, compra o crédito do fornecedor pagando-o à vista e financia a empresa compradora com garantia do fornecedor. Resumindo, é uma forma de financiamento de vendas para empresas, em que quem contrata o crédito é o fornecedor do bem, mas quem o paga é o comprador.

O **"Vlr Desconto"** pode ser inserido manualmente ou pode advir do desconto concedido na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), ou seja, origem Estoque e levar o valor do desconto para o financeiro.

Tem-se no campo **"Nro Remessa"** o número de controle para geração dos arquivos de cobrança ou pagamento em Intercâmbios Eletrônicos de Dados (EDI). Esta configuração é realizada no [Cadastro de Contas Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) ([aba Intercâmbio Eletrônico de Dados (EDI)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abaintercmbioeletrnicodedadosedi), campo Sequência remessa) e incrementado automaticamente na geração de arquivo para banco.

O campo **"Autorizado"** é utilizado para verificar se o título em questão foi ou não autorizado pela rotina [Autorização de Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606274). Esse campo não é validado na baixa do título.

Quando um título é aprovado na tela Autorização de Pagamentos, o campo **"Autorizado"** ficará como **"Sim"**. Por outro lado, quando o título não é autorizado, o campo ficará como **"Não"**.

**Importante:** quando o parâmetro **"Exige Autoriz.Pagto p/remessa de Despesa? - EXIGAUTREMDESP"** estiver desligado, ao selecionar no campo **"Tipo"** das configurações da [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa-Configura%C3%A7%C3%B5es#filtros), a opção **"Despesas"**, **"Receitas"** ou **"Ambos"**, o sistema deverá gerar o arquivo remessa normalmente, independente do status da autorização. Já quando estiver ligado, teremos os seguintes comportamentos:

- Quando selecionado o Tipo Despesas, o sistema deverá filtrar na tela de Geração Arquivo de Remessa somente os títulos de Despesa com o campo Autorizado igual a Sim, para gerar a remessa.
- Ao filtrar o Tipo Receitas serão exibidas todas as receitas para a geração da remessa, independente se estão autorizadas ou não.
- E por fim, se o filtro for feito para Ambos será apresentada a mensagem abaixo:

**"Com o parâmetro "Exige Autoriz.Pagto p/remessa de Despesa?" ligado, não é possível gerar a remessa de receitas junto com despesas".**

**Nota:** esse comportamento referente ao parâmetro EXIGAUTREMDESP só está disponível para o layout HTML5.

**Observação:** quando ocorrer alguma alteração no **"Valor Líquido"**, **"Data de vencimento"** ou parcelamento de um título de Despesa, após à sua aprovação na tela de [Autorização de Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606274-Autoriza%C3%A7%C3%A3o-de-Pagamentos), o sistema retornará esse título para o status de **"Não autorizado"** na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela), para que o mesmo possa ser reanalisado e aprovado novamente, caso entre na regra de autorização. O mesmo acontece com o parcelamento de um título de Despesa, tornando o campo Autorizado de todas as parcelas igual a Não, ou seja, **"Não Autorizado"**.

**Nota:** se forem alterados campos de valores (Vlr. Desconto, Vlr. Juros e outros), que impactam no valor apresentado no campo **"Valor Líquido"** de um título e/ou alteram a **"Data de vencimento"**, a marcação de Aprovado do título será automaticamente retirada, mudando seu status para não autorizada. O mesmo com o parcelamento de um título, tornando-se não autorizada em todas as parcelas. 

Pode-se configurar o tipo de juro no campo **"Tipo Juro"** de acordo com as opções:

- **Incluso:** ele já constará no valor do desdobramento;
- **Extra nota:** o valor total será o valor do desdobramento somado aos juros na hora da baixa.

Tem-se no campo **"Conta Baixa"**, a [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) em que foi realizado o débito ou crédito do valor durante a baixa do título.

**Observação:** como não há atualização bancária nos casos de compensação bancária, quando houverem lançamentos financeiros baixados que estão relacionados à uma compensação, o campo Conta Baixa ficará vazio.

O campo **"Tipo Marcação Cheque"** indica se será ou não emitido cheque para o título em questão. No caso de emitir, indica-se como será a emissão. Por exemplo, se será Nominal ao Fornecedor, Nominal ao Banco, Não Nominal e outros. E ainda se serão emitidos vários títulos em um único cheque. Esta marcação de cheques também pode ser realizada na [Impressão de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques), antes de imprimi-lo.

No campo **"Código de Barras"** é registrado o código de barras presente em alguns documentos de despesa. É utilizado também para registrar o código de um cheque na tela de baixa.

A **"Variação Cambial"** é a diferença no valor do título na data da negociação e o valor corrigido pela variação da moeda registrada no título. Variações cambiais (monetárias) são as atualizações dos direitos de crédito e das obrigações do contribuinte, sempre que referidas atualizações não forem pré-fixadas, mas sim determinadas posteriormente em função da taxa de câmbio, de índices ou de coeficientes aplicáveis por disposição legal ou contratual. São exemplos de variações cambiais (monetárias):

- **Ativas:** ganhos de câmbio, correção monetária pós-fixada e outras formas de atualizações não pré-fixadas, mediante contratos, (Conforme RIR/99, art. 375);
- **Passivas:** perdas de câmbio, correção monetária e outras atualizações não pré-fixadas, mediante contratos, (Conforme RIR/99, art. 377).

O tratamento contábil para as variações cambiais (monetárias) se dará da seguinte forma:

As variações dos direitos de crédito e das obrigações do contribuinte, em função da taxa de câmbio, índices ou coeficientes aplicáveis por disposição legal ou contratual serão consideradas para efeitos de legislação do imposto de renda da contribuição social sobre o lucro líquido, como receitas ou despesas financeiras, conforme o caso. (Lei nº 9.718, de 1998, art. 9º).

---

**![Imagem 15: Informações adicionais sobre a Variação Cambial](https://ajuda.sankhya.com.br/hc/article_attachments/21371460815895) Informações adicionais sobre a Variação Cambial**

**(1)** O campo Variação Cambial só trará valor negativo se o valor da cotação atual for menor que a cotação anterior, e positivo se a cotação atual for maior que a cotação anterior; para isso, tem que haver mais de uma cotação para moeda selecionada.

**(1)** Se o parâmetro **"Utiliza Sankhya Civil? - USASNKCIVIL"** estiver habilitado, ao tentar baixar um título, com ou sem moeda definida, a Variação Cambial não será recalculada. Se o parâmetro **"Considera Variação Cambial p/ Juros e Multas? - VARCAMBJURMULT"** também estiver ligado, os juros e multas serão calculados usando como base o valor cheio (Vlr. Desdobramento + Variação Cambial); caso esteja desligado, será utilizado o valor vazio (sem Variação Cambial inclusa), mesmo que o parâmetro USASNKCIVIL esteja ligado, ou seja, o parâmetro VARCAMBJURMULT apenas possuirá valor se o USASNKCIVIL estiver ligado, caso contrário, não irá exercer influência nos processos.

**(1)** Ao estornar um título, a Variação Cambial não será zerada, ela virá com o valor original que estava no título antes da baixa. Ao realizar uma baixa parcial ou rateio de títulos, a Variação Cambial será proporcional ao Vlr. Desdobramento. Ao estornar um título que foi rateado, a Variação Cambial é somada a Variação Cambial original. Por exemplo:

Supondo um Vlr. Desdobramento = $500,00 e Variação Cambial = $100,00, o total da baixa será = $600,00 (16,67% de Variação Cambial); caso o título seja baixado com $300,00, então o restante será Vlr. Desdobramento = $250,00 e Variação Cambial = $50,00, deixando um título pendente no valor de $300,00.

**(1)**  Caso a Variação Cambial seja negativa na baixa parcial, deve-se ativar o parâmetro **"Permite variação cambial negativa? - VARCAMBIALNEG"** para que seja feita a sua proporcionalização.

---

O campo **"TXID PIX"** será automaticamente preenchido com o ID da transação PIX. Sendo que, esse ID é gerado quando houver uma cobrança PIX, seja esta um recebimento imediato, cobrança CNAB ou uma cobrança API.

Por meio do campo **"Contato"**, tem-se o nome do Contato do Parceiro na Movimentação Financeira. Sendo assim nas Centrais, quando é inserido o Contato, este será registrado também no financeiro. Este campo pode ser utilizado também como uma opção a mais na geração de relatórios.

Tem-se no campo **"Veículo"** a especificação do veículo empregado os gastos, podendo ser utilizado para apurações posteriores.

O campo **"Nro. Único Devolução"** é utilizado para armazenar o número de devolução gerado através da rotina de [Devolução de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606774-Devolu%C3%A7%C3%A3o-de-Cheques).

O campo **"Vlr Moeda"** é alimentado com o valor da cotação da moeda na Data da Negociação do título.

**Importante:** na tela de Movimentação Financeira, ao gerar um novo título que tenha moeda informada, será exibido um pop-up contendo as informações de moeda correspondente àquele título. Este pop-up também é aberto no momento da inclusão da moeda ou através de Outras Opções... > Cotação de Moedas. Para maiores detalhes sobre os valores em moeda, clique em [Apresentação de Valores de Moeda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110233-Apresenta%C3%A7%C3%A3o-de-Valores-em-Moeda).

O campo **"Monitora Ocorrência de Remessa"** está disponível somente para visualização e faz parte do processo de Cobrança Registrada. Para mais informações acesse o link [Controle/monitoramento de Cobranças Registradas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111753-Controle-monitoramento-de-Cobran%C3%A7as-Registradas).

Referente aos campos **"Chave CT-e"** (Chave de Acesso do Conhecimento de Transporte) e **"Chave CT-e de referência"** (Chave de Acesso do Conhecimento de Transporte Referenciado), caso a Movimentação Financeira lançada esteja vinculada a uma [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) cujo Modelo do Documento seja 57 – Conhecimento de Transporte Rodoviário e atualiza Livro Fiscal ([aba Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal)), o sistema solicitará o preenchimento destas informações.

Ao efetuar o lançamento de uma nota de compra que possui o frete Extra-Nota, será aberta a opção de Financeiro de Fretes e nesta serão apresentados os campos Chave CT-e e Chave CT-e referência. E da mesma forma que ocorre na Movimentação Financeira, se informada neste lançamento uma TOP que também esteja com o Modelo do Documento igual a 57, o sistema solicitará a obrigatoriedade deste campo. Este comportamento se repete no momento do rateio de frete para várias notas de compra efetuado no [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es), opção **"Frete de Múltiplas Notas"**.

Estes campos são campos digitáveis e por isso é de sua responsabilidade informá-los. O sistema não faz validação da chave informada.

**Nota:** os campos Chave CT-e e Chave CT-e de referência serão utilizados para a geração do Livro Fiscal e também pelo SPED. Além disso, a quantidade de caracteres informados nestes dois campos, é devidamente validada no sistema, ou seja, ambos não podem ser preenchidos com uma quantidade inferior a 44 (quarenta e quatro) caracteres.

O campo **"Dt. Prevista p/ Baixa"** é utilizado para informar a data prevista para Baixa e esta é considerada na tela de [Gerência de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606894-Ger%C3%AAncia-de-Cobran%C3%A7a) caso a opção **"Somente com previsão vencida?"** nesta mesma tela esteja marcada.

É possível alterar a marcação **"PDD"** (Provisão de Devedores Duvidosos) se o título não estiver contabilizado, caso esteja, a seguinte mensagem é apresentada:

**"PDD não pode ser alterado. Este título já foi contabilizado."**  

Se o título for Adiantamento/Empréstimo a marcação PDD não pode ser modificada, se for a seguinte mensagem é apresentada:

**"Não pode alterar PDD de Adiantamento/Empréstimo."**

Saiba mais detalhes sobre Contabilização de títulos de devedores duvidosos em [Contabilização de Devedores Duvidosos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607634-Contabiliza%C3%A7%C3%A3o-de-Devedores-Duvidosos).

Os campos **"Nf. Entrada Fixação/Sequência"**, **"Nf. Complemento Fixação"**, **"Nro Nota Complemento Fixação"**, **"Série Complemento Fixação"**, **"Nro Nota Entrada Fixação"**, **"Série Entrada Fixação"** e **"CNPJ/CPF"** serão alimentados quando existir integração com o módulo MGE Armazém.

O campo **"Observação padrão"** deverá ser preenchido para que os lançamentos originados do Financeiro alimentem o Registro 0450 do SPED Fiscal.

### Auditoria

A seção Auditoria exibe o registro de quem alterou o título pela última vez.

- **Cód. Usuário:** exibe o código e o nome do usuário responsável pela última alteração no título.
- **Últ. Alteração:** indica a data e a hora da última alteração realizada.

> **Nota:** os campos da seção Auditoria são preenchidos automaticamente pelo Sankhya Om a cada alteração salva no título — eles não são editáveis manualmente.

### MIT

A seção MIT reúne as informações utilizadas na geração do arquivo do Módulo de Inclusão de Tributos (MIT), rotina que está diretamente ligada à geração da **DCTF**.

No campo **Período de Referência MIT**, você deve informar a **data de apuração** à qual o débito específico se refere.

- **Como utilizar:** preencha este campo caso a data de apuração do débito seja diferente da data inicial padrão de geração do arquivo. Se o campo for deixado em branco, o sistema utilizará automaticamente a data inicial da geração.
- **Saiba mais:** as informações inseridas nesta seção refletem diretamente na geração do arquivo do MIT. Para mais detalhes sobre esse processo, consulte o artigo **[Geração do Arquivo DCTF]**.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### Lançamento

Esta guia é composta pelos campos de preenchimento obrigatório na realização do lançamento de um título na Movimentação Financeira; todos os campos assinalados com um asterisco (**\***) são de indispensável preenchimento.

![Imagem 16: Esta guia é composta pelos campos de preenchimento obrigatório na realização do lançamento de um título na Movimentação…](https://ajuda.sankhya.com.br/hc/article_attachments/21353177862039)

As informações de preenchimento obrigatório são:

No campo **"Receita/Despesa"** determina se o título em questão corresponde a uma receita (atualiza contas a receber) ou uma despesa (atualiza contas a pagar).

O campo **"Dt. Vencimento"** deve receber a data de vencimento do título em questão.

Na **"Dt. Negociação"** registra-se a data em que a despesa/receita foi negociada.

**Nota:** aqueles títulos que possuem a Dt. Negociação anterior à data em que a [Conta](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) desse título foi criada, poderão ser enviados ao MS/banco, desse modo, esses títulos terão registro automático.

O **"Vlr do Desdobramento"** é o valor do título, sendo que cada desdobramento corresponde a um título.

**Observação:** não é permitida a alteração do Vlr. do Desdobramento quando o boleto for emitido por uma conta bancária configurada com API do Banco (campo **"Selecione o serviço"**, localizado na aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas) da tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)). Caso necessário renegocie o título.

**Nota:** quando uma conta for configurada para emitir os boletos via API do Banco e o parâmetro **"Calcula valor liquido boleta? - VLRLIQBOL"** estiver ligado, será enviado para o campo **"Valor Original"** o valor apresentado no campo **"Vlr. Líquido"**. Caso o parâmetro esteja desligado, o **"Vlr. Desdobramento"** será enviado para o campo Valor Original. 

Já o campo **"PIX Copia e Cola"** será preenchido automaticamente quando o PIX fornecido pelo banco do cliente estiver presente no arquivo de retorno. 

**Nota:** a informação do campo acima é preenchida a partir do [Processamento do Arquivo de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115573-Processamento-do-Arquivo-de-Retorno), quando a marcação **"Gravar QR Code Pix"** do pop-up [Configurações de Ocorrência de Retorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111033-Configura%C3%A7%C3%A3o-Arquivo-de-Retorno#parametrizaesdeocorrnciasdoretorno) estiver selecionada.

Os campos **"Vlr Juros"** e **"Vlr Multa"** serão alimentados automaticamente com os valores correspondentes aos juros e multas oriundos da Receita Federal, ao gerar uma guia de GNRE a partir de um dia após a emissão da nota fiscal e [Consultar Status GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/Consultar%20Status%20GNRE) por meio da tela Geração de Lote GNRE.

Indique o **"Banco"** no qual serão efetuadas as operações de pagamento ou recebimento. Esta informação também é utilizada para agrupar títulos para emissão de cheques.

Tem-se aqui o **"Tipo de Título"** utilizado para o pagamento das receitas/despesas, por exemplo, cheque, boleto, entre outras. Vale ressaltar que esta informação deve ser pré-incluída no sistema através do [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo).

**Nota:** o parâmetro **"Altera tipo de título em Títulos baixados? - ALTERATIPTIT"** quando ativado, possibilita a alteração do Tipo de Título em títulos já baixados. Caso esteja desativado, ao tentar-se modificar o Tipo de Título em um título já baixado, será apresentada a seguinte mensagem e tal procedimento não será concluído:

**"O campo "CODTIPTIT" não pode ser alterado em títulos baixados!"**

O campo **"Natureza"** é uma forma de classificação das Receitas e Despesas para posterior análise de desempenho destes grupos. Costuma-se chamá-la de Plano de Contas Gerencial, pois, normalmente essas naturezas têm uma ligação direta com as Contas Contábeis. As naturezas são pré-cadastradas na tela [Cadastros de Natureza de Receitas e Despesas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598774-Natureza-de-Receitas-e-Despesas).

Os demais campos não são de preenchimento obrigatório e alguns deles são alimentados automaticamente pelo sistema:

A informação do **"Centro de Resultado"** também auxilia na classificação de receitas e despesas para obtenção dos resultados financeiros da empresa dentro dos diversos departamentos, ou seja, quem está gastando o quê. Deve-se cadastrá-los previamente na tela [Cadastro de Centro de Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606754-Centros-de-Resultado).

O espaço do campo **"Histórico"** é reservado à inclusão de qualquer observação complementar a respeito do lançamento. O campo Histórico pode ser preenchido com informações que não ultrapassem o máximo de 45 caracteres. Porém, pode-se alterar manualmente nas tabelas TGFMBC e TGFMBC\_EXC a estrutura deste campo, utilizando uma ferramenta de gerenciamento de banco de dados. Ou seja, pode-se ampliar o limite de caracteres do referido campo de acordo com o desejado.

**Observação:** não será possível desabilitar manualmente a marcação **"Provisão"** em um título financeiro que esteja ligado à um orçamento e que haja provisão. Caso isto ocorra, será exibida a seguinte mensagem:

**"Não é permitido alteração do campo provisão em financeiros com previsão de Meta/Orçamento. Meta/orçamento: X, Financeiro: X".**

O conteúdo do campo **"Período de Referência"** deve ser preenchido com o dia 01 de cada mês, assim, este será utilizado para preencher o campo **"Período de Apuração"** da sub-aba [R11 - Pagamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#sub-abar11-pagamentos) da aba [R10 - Débitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF#abar10-d%C3%A9bitos) (tela [Geração do Arquivo DCTF](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF)). Além disso, essa data será utilizada no arquivo DCTF associada a cada tributo do validador.

**Nota:** para que o campo Período de Referência seja liberado para edição, habilite o parâmetro **"Permite edição do período de referência na Movimen - EDTPERREFMOV"**, assim será possível informar uma data diferente do dia 01.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### Cobrança

![Imagem 17: Cobrança](https://ajuda.sankhya.com.br/hc/article_attachments/21353333160983)

No campo **"PIX Copia e Cola"** dessa guia, insira os dados de cobrança PIX cujo o título seja uma receita, real e pendente, em que, a cobrança será realizada na conta bancária apta para acontecer via CNAB ou API, dessa forma, a impressão ocorrerá normalmente. Caso contrário, o sistema exibirá uma mensagem o informando que a conta não está preparada para a criação da cobrança PIX via API e a impressão será cancelada.

Além disso, se houver uma alteração de conta bancaria da cobrança PIX gerada, o sistema não permitirá que essa mudança ocorra e exibirá a seguinte mensagem:

**"Há uma cobrança PIX vinculada ao título [xxxx] e, por isso, a conta não pode ser alterada. Caso haja necessidade, esse título deve ser renegociado."**

Esta alteração só será possível se a conta estiver configurada para emitir os boletos via API do Banco (configuração realizada na tela [Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), aba [Boleto(s) e Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas)).

**Observação:** quando houver um título Financeiro que possua os campos **"Nosso número"**, **"Linha Dig. Receb."**, **"Cód. Barras Receb."** e **"Código de Barras"** preenchidos, quando for acionado o botão **"Duplicar"** os dados destes campos serão apagados. 

**Nota:** caso altere o campo **"Conta"** e/ou apague as informações do campo **"Nosso Número"** de uma conta configurada para API do Banco, o boleto vinculado ao título será cancelado. 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### Impostos

![Imagem 18: Impostos](https://ajuda.sankhya.com.br/hc/article_attachments/25935016173463)

Os campos **"Vlr INSS / Vlr ICMS / Base ICMS / %ICMS"** podem ser preenchidos manualmente ou podem derivar dos cálculos de INSS/ICMS da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), ou seja, origem Estoque e levar o valor dos impostos para o financeiro.

Tem-se no campo **"Vlr IRF"** o valor do IRRF e o campo **“Vlr ISS”** o valor do ISS calculados na nota; pode-se também incluir esta informação manualmente no próprio campo.

As marcações **“INSS Retido”**, **“IRRF Retido”** e **“ISS Retido”** quando habilitadas faz com que o valor do respectivo imposto seja deduzido no total do financeiro.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### GNRE

Nesta guia são apresentados os dados correspondentes a **"GNRE - Guia Nacional de Recolhimento de Tributos Estaduais"**. Esta guia é trabalhada na tela [Geração de Lote GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115053-Gera%C3%A7%C3%A3o-de-Lote-GNRE).

![Imagem 19: Nesta guia são apresentados os dados correspondentes a "GNRE - Guia Nacional de Recolhimento de Tributos Estaduais" .…](https://ajuda.sankhya.com.br/hc/article_attachments/21353333182615)

Informe nesta guia o **"Número Lote GNRE"**, o **"Motivo Rejeição GNRE"** caso exista, e o **"Status GNRE"**.

No campo **"Chave de acesso NFe"** indique a chave de acesso da Nota Fiscal Eletrônica para movimento financeiro, de forma a possibilitar uma maior rastreabilidade para o documento. Este campo será preenchido logo após gerar o lote de uma Nota de Venda.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### Despesas Administrativas/Judiciárias

Nesta guia, realize uma das marcações para indicar qual o tipo do título de despesa judicial.

![Imagem 20: Nesta guia, realize uma das marcações para indicar qual o tipo do título de despesa judicial.](https://ajuda.sankhya.com.br/hc/article_attachments/21353399633943)

Sendo estas:

- Custas Processuais?;
- Depósito Judicial?;
- Desp. com Advogado(s)?.

Desse modo, ao habilitar uma destas as outras duas ficarão indisponíveis para seleção.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### EFD Reinf

Aqui serão exibidas todas as informações referentes a geração dos eventos do Bloco 4000 da [EFD Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) e seus detalhamentos.

![Imagem 21: Aqui serão exibidas todas as informações referentes a geração dos eventos do Bloco 4000 da EFD Reinf e seus…](https://ajuda.sankhya.com.br/hc/article_attachments/21353501096215)

Informe o **"Código Natureza Rendimento"** para gerar os eventos do Bloco 4000 da EFD Reinf e seus detalhamentos.

Para que os campos da aba EFD Reinf sejam habilitados, o [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) do lançamento deve estar com a marcação **"Gerar informações do EFD Reinf Grupo 4000?"** efetuada. Além disso, a pesquisa da Natureza de Rendimento exibirá apenas os códigos ativos e cuja data de vigência seja compatível com a data do lançamento financeiro.

Habilite a marcação **"Sem IR Retido Exterior"** se não houver nenhum valor de IR retido no Exterior. **Esta marcação só será habilitada pelo sistema se a UF do Parceiro for igual a EX (Exterior).**

O campo **"Tributação IRRF - Exterior REINF"** será habilitado para edição quando a marcação Sem IR Retido Exterior estiver efetuada. Nele, deverá ser informado o tipo de retenção do IRRF conforme as opções abaixo:

- 40-Não retenção do IRRF - isenção estabelecida em convênio;
- 41-Não retenção do IRRF - isenção prevista em lei interna;
- 42-Não retenção do IRRF - alíquota zero prevista em lei interna;
- 43-Não retenção do IRRF - pagamento antecipado do imposto;
- 44-Não retenção do IRRF - medida Judicial (informação do processo judicial);
- 50-Não retenção do IRRF - outras hipóteses.

A marcação **"Tem Dedução Base IRPF?"** será ativada automaticamente se o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#painelprincipal) for identificado como Pessoa Física e/ou se o [Código de Natureza de Rendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367) indicado estiver com alguma informação no campo **"Tipo de Dedução"**. Além disso, com esta marcação ativa será habilitada a opção Dependentes no botão Outras opções para que sejam preenchidos os dados dos possíveis dependentes.

O campo **"Tipo Dedução"** será habilitado quando a marcação Tem dedução Base IRPF? estiver efetuada. Este campo poderá ficar em branco ou definido com as opções **"1 - Previdência oficial"** ou **"8 – Desconto simplificado mensal"**.

O **"Valor de Dedução Base IRPF"** deverá ser preenchido se a opção 1 - Previdência Oficial for indicada no campo Tipo Dedução.

**Observação:** quando houver valores informados nos campos referentes a dedução e/ou isenção, o sistema irá deduzi-los do valor total do título para compor a base de cálculo do imposto retido que será gravado na tabela de impostos do financeiro. Sabendo disso, tem-se abaixo o cálculo a ser realizado:

```
       Base do IRRF = Valor Desdobramento (aba Lançamento) - Valor De Dedução
           (localizado no pop-up "Dependentes de Financeiro Dedução", por meio da
           opção Dependentes do botão Outras Opções dessa tela) - Valor de Dedução
           Base IRPF (aba EFD-Reinf) - Valor de isenção (aba EFD-Reinf).
```

**Lançamento de Dependentes e Pensão:** ao acessar o pop-up **Dependentes** (através do botão Outras Opções), você deverá preencher:

- **Tipo Dedução:** selecione "5 - Pensão alimentícia" ou "7 - Dependentes".
- **Dependentes:** o sistema buscará os dependentes previamente cadastrados na aba Dependente IR (REINF) do Cadastro de Parceiros, respeitando o período de vigência.
- **Valor Dedução:** informe o valor a ser deduzido.

A marcação **"IRRF Isento?"** será habilitada se o [Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#painelprincipal) for identificado como Pessoa Física e o [Código de Natureza de Rendimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367) informado, estiver com alguma informação no campo **"Tipo Rendimento Isento"**.

Caso a marcação acima esteja efetuada, o campo **"Tipo de Isenção"** será habilitado para que o tipo de isenção seja selecionado de acordo com as seguintes opções:

- 1- Parcela Isenta 65 anos;
- 2- Diária de viagem;
- 3- Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho;
- 4- Abono pecuniário;
- 5- Valor Pago a titular, sócio ME ou EPP, exceto pró-labore, aluguéis e serviços prestados;
- 6- Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço;
- 7- Compl. de aposentadoria, Ref. às contribuições efetuadas no período de 01/01/1989 a 31/12/1995;
- 8- Ajuda de custo;
- 9- Rendimentos pagos sem retenção do IR na fonte - Lei 10.833/2003;
- 10- Auxílio moradia;
- 99- Outros (especificar).

Selecionando a opção **1- Parcela Isenta 65 anos**, o sistema habilitará o campo específico **"Valor parcela isenção 65 anos"**, que deve ser preenchido com o valor correspondente.

Selecionando qualquer Tipo de Isenção e informando o campo IRRF Isento?, preencha o campo **"Valor de Isenção"** com o respectivo valor correspondente a isenção mencionada.

O campo **"Data do Laudo"** deverá ser preenchido quando a opção 6-Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço for indicada no campo Tipo de Isenção. 

Já o campo **"Descrição"** será habilitado se a opção 99 - Outros (especificar) do campo Tipo de Isenção for escolhida.

**Retenção de IRRF para o Exterior (Pop-up Outros Impostos)** Caso a operação com o exterior sofra a retenção do imposto, o detalhamento deverá ser feito no pop-up **Outros Impostos** (na tela de Movimentação Financeira).

O campo **"Tributação IRRF - Exterior REINF"** será habilitado se a Natureza de Rendimento estiver preenchida, o tipo de imposto for IRF e a UF do parceiro for EX. Nele, selecione o código aplicado:

- 10 - Retenção do IRRF - alíquota padrão.
- 11 - Retenção do IRRF - alíquota da tabela progressiva.
- 12 - Retenção do IRRF - alíquota diferenciada (países com tributação favorecida).
- 13 - Retenção do IRRF - alíquota limitada conforme cláusula em convênio.
- 30 - Retenção do IRRF - outras hipóteses.

Se a sua retenção de impostos ocorrer de forma automática, o sistema importará este código diretamente da mesma regra de onde buscou a alíquota do IRF.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela)

### Dados do Cartão

![Imagem 22: Dados do Cartão](https://ajuda.sankhya.com.br/hc/article_attachments/21851589194135)

No momento da criação do Movimento Financeiro, o sistema buscará o [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) cadastrado correspondente ao recebimento realizado, assim já será preenchida a Identificação da Bandeira e a Taxa de Cartão conforme configuração da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) da tela Tipos de Título correspondente.

![Imagem 23: Caso o Movimento Financeiro esteja com qualquer inconsistência por não ter um Tipo de Título correspondente, será…](https://ajuda.sankhya.com.br/hc/article_attachments/16423433429655) Caso o Movimento Financeiro esteja com qualquer inconsistência por não ter um Tipo de Título correspondente, será possível realizar a alteração ao atualizar os dados do novo Tipo de Título dentro daquela movimentação, incluindo as informações referentes a bandeira e taxas correspondentes.

Nessa aba será possível visualizar os seguintes campos:

- **Taxa Administradora:** refere-se a taxa do cartão, o qual já será preenchido automaticamente;
- **Autorização:** relaciona-se ao número de autorização da adquirente referente a transação concluída;
- **NSU:** esse campo é referente ao Número Sequencial Único. É um número único gerado para identificar uma transação;
- **Nome rede:** nome da adquirente responsável pela transação;
- **Bandeira:** informará exatamente a bandeira transacionada da operação conforme o Tipo de Título selecionado na criação do Movimento Financeiro.

![Imagem 24: Para utilizar essa aba será necessário "Configurar formulário" , assim clique no botão "Configurações" e adicione um…](https://ajuda.sankhya.com.br/hc/article_attachments/21830790958743) Para utilizar essa aba será necessário **"Configurar formulário"**, assim clique no botão ![Imagem 25: Para utilizar essa aba será necessário "Configurar formulário" , assim clique no botão "Configurações" e adicione um…](https://ajuda.sankhya.com.br/hc/article_attachments/21352113037335) **"Configurações"** e adicione um novo grupo acionando o botão ![Imagem 26: Para utilizar essa aba será necessário "Configurar formulário" , assim clique no botão "Configurações" e adicione um…](https://ajuda.sankhya.com.br/hc/article_attachments/21851589197591) **"Adicionar novo grupo"**, utilize o botão ![Imagem 27: Para utilizar essa aba será necessário "Configurar formulário" , assim clique no botão "Configurações" e adicione um…](https://ajuda.sankhya.com.br/hc/article_attachments/21851589203223) **"Editar"** para configurá-lo como **"Dados do Cartão"**, e então adicione os campos acima, entenda melhor pelo passo a passo a seguir:

[GIF animado: Imagem 28: Para utilizar essa aba será necessário "Configurar formulário" , assim clique no botão "Configurações" e adicione um…](https://ajuda.sankhya.com.br/hc/article_attachments/21851599153303)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Guiasdatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#top)

## Botões da tela

A seguir, conheça a funcionalidade de cada botão presente na tela Movimentação Financeira:

| [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Configura%C3%A7%C3%B5es) | [Baixar título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Baixart%C3%ADtulo) |
| --- | --- |
| [Estornar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Estornar) | [Parcelar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Parcelar) |
| [Ver Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#VerRenegocia%C3%A7%C3%A3o) | [Ratear](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Ratear) |
| [Receber](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Receber) | [Duplicar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Duplicar) |
| [Mais opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Maisop%C3%A7%C3%B5es) | [Exportar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Exportar) |

### Imagem 29: Configurações Configurações

Ao acionar o referido botão será possível realizar as seguintes configurações na tela:

#### Modo de visualização

![Imagem 30: Modo de visualização](https://ajuda.sankhya.com.br/hc/article_attachments/21377723719191)

Nesta guia é possível configurar os campos e as guias que ficarão disponíveis na tela.

Ao ativar a marcação **"Grade"** será exibido o botão **"Configurar Grade"**. Através deste botão é possível definir quais colunas deseja visualizar na tela e também organizar a ordem dessas colunas.

Por outro lado, ao ativar a marcação **"Formulário"** será possível configurar as guias da tela, adicionando ou removendo campos conforme necessário.

#### Intervalo de Vencimento

![Imagem 31: Intervalo de Vencimento](https://ajuda.sankhya.com.br/hc/article_attachments/21377723730455)

Configure o Intervalo de Vencimento de acordo com as opções:

- **Última data utilizada:** a data de vencimento será preenchida, automaticamente, pela última data utilizada no filtro dos títulos vencidos.
- **Hoje:** a data de vencimento será preenchida, automaticamente, pela data do dia e trará apenas os títulos que estão vencendo naquele dia.
- **Semana Corrente:** a data de vencimento será preenchida, automaticamente, com data inicial referente ao primeiro dia da semana e data final referente ao último dia da semana, e trará apenas os títulos com vencimento naquela semana.
- **Mês Corrente:** a data de vencimento será preenchida, automaticamente, com data inicial referente ao primeiro dia do mês e data final referente ao último dia do mês, e trará apenas os títulos com vencimento naquele mês.
- **Limpar data:** o intervalo da data de vencimento virá sempre em branco, e ao aplicar o filtro o sistema trará todos os títulos lançados no sistema, de acordo com os demais campos de filtro, independente da data de vencimento dos títulos.
- **Personalizado:** por meio dessa marcação, habilita-se os campos **"Últimos Dias"** e **"Próximos dias"**, para compor um filtro por vencimento que apresente os títulos dentro destes parâmetros. Por exemplo:

Considerando que no campo **"Último(s)"** foi informado um valor de 3 dias e no campo **"Próximo(s)"** um valor de 2 dias. Então, o sistema trará todos os títulos que vencerão no intervalo de 3 dias antes da data atual e 2 dias depois da data atual. Se a data atual é, por exemplo, 10/03/2018, logo serão apresentados os títulos com vencimento a partir do dia 07/03/2018 até o dia 12/03/2018.

**Nota:** independente destas configurações, o sistema permitirá a digitação do intervalo de vencimento diretamente no campo **"Data de Vencimento"**.

#### Preferências Adicionais

![Imagem 32: Preferências Adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/21377739247639)

Ao habilitar a marcação **"Totalizar pelo valor líquido"**, o totalizador da grade será apresentado pelo total dos valores líquidos dos títulos. Se a marcação estiver desmarcada, a totalização apresentada estará acrescida no valor do desdobramento.

Através da marcação **"Mostrar renegociados"** determina-se se os títulos renegociados serão ou não apresentados na Movimentação Financeira; optando por não visualizá-los, esta opção deverá ser desmarcada. Para que a referida marcação esteja disponível juntamente com as opções de coloração, o parâmetro **"Visualizar títulos renegociados? - VERTITRENEG"** deve estar habilitado.

O parâmetro **"Tipo de cálc. juros/multa na baixa agrupada - TIPCALCJURBXAG"** permite configurar o cálculo do juros e multa em uma baixa agrupada, das seguintes formas:

- **Menor vencimento:** tem-se o agrupamento dos títulos e o cálculo do juros/multa pelo menor vencimento dos títulos sobre o montante final.
- **Título à título:** irá ocorrer o cálculo do juros/multa de cada título e logo após estes títulos serão agrupados. O montante final será a soma dos valores separados.

**Observação:** para que o campo Cálc. juros/multa baixa agrupada seja apresentado, o parâmetro **"Baixa de múltiplos títulos - OFEROPCBAIXTIT"** deve estar configurado com a opção **"Baixa com renegociação"**.

#### Cores Grade

![Imagem 33: Cores Grade](https://ajuda.sankhya.com.br/hc/article_attachments/21377739259671)

Neste campo, será possível visualizar a cor de apresentação dos títulos de Receita, Despesa, Antecipados e Renegociados no modo grade.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 34: Baixar título Baixar título

O processo de Baixa de Títulos é de suma importância no controle de contas pagas e a pagar, recebidas e a receber em uma empresa. Nesse sistema, esse processo possui algumas ramificações; por esse motivo, sua documentação encontra-se em um tópico específico para melhor detalhá-la.

![Imagem 35: Clique no link Movimentação Financeira - Baixa de Títulos para acessar as particularidades deste processo.](https://ajuda.sankhya.com.br/hc/article_attachments/21344384424343) Clique no link [Movimentação Financeira - Baixa de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos) para acessar as particularidades deste processo.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 36: Estornar Estornar

Como o [Estorno](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueefetuaroestornodeumttulo) é o processo inverso da [Baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oquerealizarabaixadeumttulo), para realizá-lo é necessário que o título em questão esteja baixado. Uma vez definido o título e clicando no botão Estornar será aberto o pop-up **"Estornar título"**:

![Imagem 37: Como o Estorno é o processo inverso da Baixa , para realizá-lo é necessário que o título em questão esteja baixado. Uma…](https://ajuda.sankhya.com.br/hc/article_attachments/21369749988759)

Este pop-up é apenas para confirmação do procedimento de Estorno; nele poderão ser visualizadas a **"Data"** em que a baixa foi realizada, o **"Valor baixado"**, a **"Conta bancária"** na qual a baixa foi realizada e caso exista, o **"Histórico"** inserido para o título.

Ao selecionar múltiplos registros baixados e clicar no botão **"Estornar"** será aberta a janela **"Estornar múltiplos títulos"**. Para confirmação, são exibidas algumas informações dos títulos selecionados: **"Estorno de múltiplos títulos"** com as informações de **"Receita/Despesa"**, **"Nro Único"**, **"Nro Nota"**, **"Vlr Baixa"**, **"Data Baixa"**, **"Origem"**, **"Conciliado"** e **"Dh. Conciliação"**:

![Imagem 38: Ao selecionar múltiplos registros baixados e clicar no botão "Estornar" será aberta a janela "Estornar múltiplos…](https://ajuda.sankhya.com.br/hc/article_attachments/21369757578775)

As marcações desta tela funcionarão da seguinte forma:

- **Estornar títulos conciliados:**ao ser habilitada, irá estornar todos os títulos, inclusive os conciliados, No entanto, caso esteja desabilitada serão estornados apenas os não conciliados;
- **Estornar títulos baixa agrupada:**estando habilitada, serão estornados os títulos que foram baixados de forma agrupada;
- **Recompor título original:** se marcada, o estorno tentará recompor o título original que foi dividido em duas ou mais parcelas no momento da baixa.

Ao confirmar o estorno dos títulos apresentados na janela acima, será apresentada uma etapa de resumo com as abas **"Não Estornados"** e **"Estornados"**, considerando que, na aba Não Estornados serão listados os títulos que não puderam ser estornados e sua justificativa e, na aba Estornados com sucesso, teremos os títulos que foram estornados:

[GIF animado: Imagem 39: Ao confirmar o estorno dos títulos apresentados na janela acima, será apresentada uma etapa de resumo com as abas "Não…](https://ajuda.sankhya.com.br/hc/article_attachments/21369757586199)

**Observação:** a aba Estornados com sucesso apenas será exibida caso não hajam títulos com impedimentos ao estorno e, consequentemente, a aba Não Estornados será ocultada e vice-versa.

**Importante:** após o recebimento da nota não será permitido o seu estorno caso a Empresa informada esteja configurada com a opção **"TEF"** no campo **"Tipo de PIX"** (tela de [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapix)). 

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 40: Parcelar Parcelar

Para efetuar o parcelamento de um título, deve-se primeiramente selecioná-lo na grade principal da tela; em seguida, clique no botão **"Parcelar"**, assim será exibida a seguinte tela:

![Imagem 41: Para efetuar o parcelamento de um título, deve-se primeiramente selecioná-lo na grade principal da tela; em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/21372019387799)

#### Dados básicos

Informe, inicialmente, a quantidade de **"Parcelas"** a serem geradas para o título em questão.

Tem-se as seguintes opções para definição da **"Frequência de pagamento"**:

| - Diária; - Semanal; - Dezena; - Quinzenal; - 30, 60, 90, 120...; - Mensal; | - Bimestral; - Trimestral; - Quadrimestral; - Semestral; - Anual; - Personalizada**\***. |
| --- | --- |

**\***Selecionando a opção Personalizada será aberto o campo para definição do **"Intervalo de dias"** para a frequência de parcelamento.

Preencha o campo **"Entrada"** com o valor corresponde a entrada do parcelamento.

#### Juros e multa

Neste quadrante, determine como será a gravação dos juros e multas calculados no parcelamento do título. 

Determine no campo **"Taxa de juros"** a taxa de juros a ser utilizada no parcelamento.

Nos campos **"Modo de exibição dos juros"** e **"Modo de exibição da multa"** tem-se as seguintes alternativas:

- **Somado ao valor:** esta opção soma os juros e/ou multas ao valor de cada parcela.
- **Separado do valor:** neste caso, os juros e/ou multas calculados serão gravados separadamente do valor de cada parcela.
- **Separado do valor (negociado):** por esta opção, os juros e/ou multas serão gravados nos campos **"Vlr Juros Negociados"** e **"Vlr Multa Negociada"**, respectivamente.

As marcações abaixo estarão disponíveis somente após o preenchimento do campo Taxa de juros:

**Juros Simples:** serão calculados juros simples para as parcelas.

**Juros Composto:** serão calculados juros compostos para as parcelas.

**Juros Composto com valores de parcelas fixos:** serão calculados juros compostos, porém as parcelas serão divididas de modo que fiquem iguais (fixas).

Defina no campo **"Taxa de multa"**, a taxa de multa aplicada sobre o valor total do parcelamento, independente do vencimento dos títulos parcelados.

#### Data de vencimento

Configure aqui, por meio das opções abaixo a data de vencimento das parcelas:  

- **A partir da data de vencimento original do título:** por meio desta opção, serão calculadas as parcelas com base na data do primeiro vencimento do título original;
- **A partir da data de negociação do título:** será utilizada a data de negociação do título original, para cálculo da data base de vencimento das parcelas;
- **Data base para cálculo do vencimento:** a data base será a própria data em que o parcelamento está sendo realizado;

#### Configurações Adicionais

A data de negociação dos novos títulos gerados a partir de um parcelamento será definida de acordo com as opções localizadas no campo **"Data de negociação do título"**: 

- **Negociação original:** todos os títulos parcelados apresentarão data de negociação igual à data de negociação do título original;
- **Igual ao novo vencimento:** por meio desta opção, todos os títulos parcelados apresentarão data de negociação de acordo com a Frequência. Considere um exemplo:

Suponha um título original parcelado em 3 vezes com a data de negociação em 09/04/2018, frequência definida como Mensal, opção Igual ao novo vencimento marcada; com isso, terá:

- 1ª parcela data de negociação = 08/05/2018

- 2ª parcela data de negociação = 08/06/2018

- 3ª parcela data de negociação = 08/07/2018

- **Hoje:** por meio desta opção, todos os títulos parcelados apresentarão data de negociação igual a data da realização do parcelamento.

Por meio do campo **"Desdobramento inicial"**, determine qual será o número do desdobramento inicial quando as parcelas forem geradas.

Com a marcação **"Copiar rateio para as parcelas?"** ligada, caso o título que está sendo parcelado tenha sido rateado, este rateio será considerado também nas parcelas.

> 📌 **Importante** **— Reagrupar parcelas (voltar para 1 título)**

O processo de parcelamento não possui uma ação direta de "desfazer". Caso o parcelamento tenha sido realizado de forma indevida e o usuário deseje **reagrupar as parcelas em um único título consolidado** (ex: transformar 4 parcelas de R$ 25,00 de volta em 1 título de R$ 100,00), deve-se utilizar a rotina de **Renegociação de Títulos**.

**Passo a passo para reagrupar:**

1. Acesse a tela **Renegociação de Títulos**;
2. Selecione todas as parcelas que deseja unificar;
3. Realize o agrupamento, definindo a renegociação para apenas 1 parcela com o valor total somado.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### ![Imagem 42: Ver renegociação](https://ajuda.sankhya.com.br/hc/article_attachments/42312261262487) Ver renegociação

A Renegociação de títulos consiste na geração de um novo título de receita ou despesa com base no título original (ou títulos originais) mudando os vencimentos e valores conforme a renegociação, por exemplo, pode-se renegociar o vencimento do título, parcelá-lo e agrupar 2 ou mais títulos em um único título, de acordo com a necessidade do cliente.

O procedimento de [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393-Renegocia%C3%A7%C3%A3o-de-T%C3%ADtulos) é realizado na tela com esta mesma nomenclatura. Porém, na Movimentação Financeira acionando o botão **"Ver renegociação"** será exibido o pop-up **"Consulta de renegociação"**, que permite a visualização e consulta dos títulos que foram renegociados. O Filtro pode ser configurado com base no número da renegociação presente nos filtros personalizados, levando-se em consideração os demais campos de filtro como vencimento, receitas, despesas, entre outras.

![Imagem 43: O procedimento de Renegociação de Títulos é realizado na tela com esta mesma nomenclatura. Porém, na Movimentação…](https://ajuda.sankhya.com.br/hc/article_attachments/21373596865175)

Na grade superior são apresentados os Títulos originais e na inferior os Títulos renegociados, sendo que ambas possuem o botão **"Configuração da Grade"** possibilitando assim a organização das colunas da forma desejada.

**Nota:** para os títulos renegociados só está disponível a ação de visualização através do botão Ver renegociação.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### ![Imagem 44: Ratear](https://ajuda.sankhya.com.br/hc/article_attachments/42312284185495)  Ratear

O [Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira#oqueumrateiofinanceiro) é uma divisão proporcional de recursos de acordo com critérios pré-estabelecidos. Existem duas maneiras de se efetuar o rateio: manualmente ou utilizando um critério pré-definido na tela [Critérios de Rateio](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606574-Crit%C3%A9rios-de-Rateio).

Uma vez lançado o título na Movimentação Financeira com todos os dados necessários, acione o botão **"Ratear"**, desse modo a seguinte tela será exibida:

![Imagem 45: Uma vez lançado o título na Movimentação Financeira com todos os dados necessários, acione o botão "Ratear" , desse…](https://ajuda.sankhya.com.br/hc/article_attachments/21369757594263)

Ao optar pelo critério pré-definido, busque o preceito desejado no campo **"Critério de rateio"** localizado no alto da tela, assim, os respectivos dados de rateio serão apresentados.

Para melhor visualização e edição dos dados, clique no botão ![Imagem 46: Para melhor visualização e edição dos dados, clique no botão "Modo Formulário" .](https://ajuda.sankhya.com.br/hc/article_attachments/21351501151639) **"Modo Formulário"**.

[GIF animado: Imagem 47: Para melhor visualização e edição dos dados, clique no botão "Modo Formulário" .](https://ajuda.sankhya.com.br/hc/article_attachments/21369757597463)

No campo **"Parceiro"** pode-se ajustar o parceiro conforme a necessidade. Para que esse campo fique disponível nessa tela é necessário habilitar o parâmetro **"Permitir rateio por parceiro? - RATPARC"**.

Caso deseje efetuar a inclusão do rateio de forma manual, clique em **"Cadastrar"** e informe os dados desejados.

[GIF animado: Imagem 48: Caso deseje efetuar a inclusão do rateio de forma manual, clique em "Cadastrar" e informe os dados desejados .](https://ajuda.sankhya.com.br/hc/article_attachments/21369750029975)

Quando um veículo está vinculado a um **"Centro de Resultado"**, o rateio deve ser feito exclusivamente para esse centro, impossibilitando a utilização de um Centro de Resultado diferente do que está configurado na tela [Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos).

Feito isso, clique no botão ![Imagem 49: Feito isso, clique no botão "Confirmar" localizado na parte superior da tela para que o rateio seja registrado.](https://ajuda.sankhya.com.br/hc/article_attachments/21371397846039) **"Confirmar"** localizado na parte superior da tela para que o rateio seja registrado.

![Imagem 50: A soma dos percentuais na finalização do rateio deverá ser igual a 100; caso contrário, ao confirmar o rateio o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/16423433429655) A soma dos percentuais na finalização do rateio deverá ser igual a 100; caso contrário, ao confirmar o rateio o sistema apresentará a seguinte mensagem: 

**"O título deve ser 100% rateado!"**.

Após o rateio, o botão assume a nomenclatura **"Rateado"**. Ao acioná-lo, os rateios efetuados na nota de origem do registro financeiro são apresentados somente para consulta.

Considere ainda que, o sistema não permitirá qualquer alteração ou exclusão de rateio em títulos contabilizados, se o parâmetro **"Bloquear alterao rateio-financeiro j contabilizado. - BLOQALTRAFINCTB"** estiver ligado.

---

![Imagem 51: Informações adicionais sobre o Rateio](https://ajuda.sankhya.com.br/hc/article_attachments/21371460815895) **Informações adicionais sobre o Rateio**

**(1)** O **Sankhya Om** não possibilita o rateio de Movimentações Financeiras que foram geradas e rateadas pelas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas). Neste caso, é apresentada a mensagem **"Financeiro já rateado pela nota"**. Essa mensagem ocorre na tela Movimentações Financeiras quando solicitada a opção Ratear, sendo que, o título seja proveniente de uma nota/pedido de compra/venda, o qual já tenha sido rateado nas Centrais.

**(1)** A situação inversa também ocorre, ou seja, no caso de um financeiro originado de nota/pedido de compra/venda, ser rateado na Movimentação Financeira, ao tentar realizar novamente a operação de rateio, pelas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) será exibida a mensagem **"Nota já rateada pelo financeiro"**.

**(1)** O parâmetro **"Abrir rateio p/ títulos duplicados no financeiro - ABRERATDUPFIN"** quando ativado, na duplicação de um título que possua rateio o sistema abrirá uma caixa de diálogo questionando se deseja ou não, copiar o rateio do título original. Se o referido parâmetro estiver desligado, o rateio do título original sempre será copiado.

**Observação:** o **Sankhya Om realiza o rateio do título considerando o valor do desdobramento. No entanto, os valores de juros e multas são visualizados somente nas análises gerenciais. Para que isso ocorra, é necessário efetuar a parametrização da tela** [**Naturezas Especiais**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606154-Naturezas-Especiais)**.**

---

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 52: Receber Receber

A utilização deste botão está vinculada no processo descrito no tópico [Integração com TEF AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR). Este será habilitado mediante as seguintes condições:

**(1)** Habilitação do parâmetro **"Usa recebimento com cartão (CTFClient)? - USARECEBCARTCTF"**. Sendo que este é responsável por realizar os recebimentos de vendas efetivadas via TEF AUTTAR;
**(1)** Definição da opção **"Auttar"**, **"PayGo"** ou **"SiTef"** no parâmetro **"Gateway de recebimento com cartão (TEF) - TEFGATEWAY"**;

**Observação:** caso no parâmetro TEFGATEWAY a opção **"Não usa"** for definida, ao clicar em ![Imagem 53: Observação: caso no parâmetro TEFGATEWAY a opção "Não usa" for definida, ao clicar em Receber , o sistema irá exibir a…](https://ajuda.sankhya.com.br/hc/article_attachments/21374221523991) Receber, o sistema irá exibir a mensagem abaixo:

**"O gateway para operações TEF não está ativo"**

**(1)** E ainda, filtragem de um título de Receita, Real e Pendente.

Além disso, o referido botão, só estará disponível caso selecione um título de **"Receita"**, **"Real"** ou **"Pendente"**. Selecionando um título que não possua essas especificações, e tentar utilizar o botão Receber, um pop-up será apresentado, com a seguinte mensagem:

**“Recebimento indisponível. O título precisa ser uma receita, real e pendente.”**

Seguindo corretamente a configuração acima, ao clicar em Receber, o pop-up **"Receber título com cartão"** surgirá na tela:

![Imagem 54: Seguindo corretamente a configuração acima, ao clicar em Receber , o pop-up "Receber título com cartão" surgirá na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/21373256393879)

Ao pesquisar determinado **"Tipo de Cartão"** neste pop-up, somente os títulos financeiros semelhantes a ele serão apresentados se o parâmetro **"Filtrar Tipos de título similares no Rec. Cartão? - FTIPTITRECCAR"** for ligado.

Após o preenchimento dos campos do pop-up, será possível visualizar os campos **"Valor Total"** que será igual ao valor do título, ou a soma dos títulos caso o recebimento seja baseado em mais de um título,  **"Saldo"**e **"Valor recebido"**.

**Nota:** antes de o recebimento ser efetivado o campo Saldo terá o mesmo valor do campo Valor Total, e o Valor recebido será igual a zero.

Assim, tendo realizado todas as etapas acima, ao pressionar o botão Receber, a comunicação com o TEF será acionada e o usuário precisará informar o cartão e a senha para prosseguir com o recebimento, feito isso, os dados serão carregados na grade inferior conforme o recebimento e um comprovante será gerado ao lado direito da tela.

Dessa forma, o campo Valor recebido será atualizado e o valor do Saldo será a diferença entre o Valor total e o Valor recebido.

O campo **"Parcelas"** estará habilitado para edição quando o campo **"Qtd. parcelas"** da tela Tipos de Título aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto) for maior que 1, e quando selecionar a opção **"Créd. Parcelado Lojista (sem juros)"** ou **"Créd. Parcelado com parcela à Vista"** do campo **"Operação CTF"** também da aba Preferências de Cartão.

**Nota:** além disso, ao habilitar o parâmetro FTIPTITRECCAR, o campo Parcelas será automaticamente preenchido com as informações já cadastradas no campo Qtd. Parcelas da aba Preferência de Cartão da tela Tipos de Título do título utilizado na operação.

No entanto, caso o tipo do cartão seja **"Créd.Parcelado Administradora (com juros)"** ou Cred. Parcelado Lojista (sem juros) e a quantidade de parcelas for igual a 1, a seguinte mensagem de aviso surgirá na tela:

**“Para operações de crédito parcelado é necessário informar a quantidade de parcelas maior que 1”**

**Nota:** se o campo Operação CTF for definido com a opção **"Débito Pré-Datado"**, **"Créd. a vista"** ou **"Débito"** o campo Parcelas será automaticamente preenchido com a quantidade 1, independente da configuração do campo Qtd. parcelas.

Assim, quando preenchidos os campos **"Tipo de Cartão"**, **"Valor da transação"** e Parcelas, o botão ![Imagem 55: Assim, quando preenchidos os campos "Tipo de Cartão" , "Valor da transação" e Parcelas , o botão "Receber" será…](https://ajuda.sankhya.com.br/hc/article_attachments/21785817753623) **"Receber"** será habilitado para que a conexão com o recebimento TEF seja realizada para a inserção do cartão e em seguida, da sua senha.

Para realizar o recebimento com múltiplos títulos, deve-se habilitar a marcação **"Usar renegociação"** da opção [Pref. de Recebimento com cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#pref.derecebimentocomcarto) do botão [Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es).

Lembre-se que os títulos selecionados devem ser do mesmo Parceiro. Caso contrário, o sistema exibirá a mensagem abaixo:

**"A rotina não está preparada para títulos de parceiros diferentes.**
**Código: CORE\_E03316"**

Dado que o recebimento foi realizado com mais de um cartão, ao realizar uma parte do pagamento, o saldo será atualizado com o valor restante.

Porém, se realizado com apenas um cartão, mas ainda houver saldo para receber, o Valor da transação será atualizado com o valor restante do saldo para que o pagamento da diferença seja efetuado.

Dessa forma, clique no botão ![Imagem 56: Dessa forma, clique no botão Finalizar para concluir o recebimento.](https://ajuda.sankhya.com.br/hc/article_attachments/21910961949719) Finalizar para concluir o recebimento.

Com o parâmetro **"Confirmar automaticamente o recebimento TEF? - CONFAUTTEF"** ligado, o recebimento será concluído de forma automática sem a necessidade de  Finalizar o pagamento.

**Nota:** durante o processamento do recebimento, o botões Receber e Finalizar estarão desabilitados e uma mensagem informando o tempo restante da conclusão da ação ficará visível no rodapé do pop-up.

![Imagem 57: Nota: durante o processamento do recebimento, o botões Receber e Finalizar estarão desabilitados e uma mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/21911045086999)

**Observação:** pode-se ainda, informar no campo **"Inteiro"** do parâmetro **"Tempo em seg. p/ timeout no Recebimento TEF - TEFRECTIMEOUT"** o tempo de tolerância antes da conclusão do processo por meio das API's de pagamento. Caso o pagamento não seja realizado antes do fim da contagem, será exibida uma mensagem o informando sobre um erro no processamento da transação.

[GIF animado: Imagem 58: Observação: pode-se ainda, informar no campo "Inteiro" do parâmetro "Tempo em seg. p/ timeout no Recebimento TEF -…](https://ajuda.sankhya.com.br/hc/article_attachments/21911527728407)

Caso o pagamento com múltiplos títulos do mesmo Parceiro seja realizado com uma TOP renegociação (Pref. de recebimento com cartão) configurada, ao clicar no botão Receber, o campo Valor da transação estará preenchido com os valores dos títulos somado ao valor de juros e multas no pop-up Receber título com cartão, se as marcações **"Calcular juros até a data final"** e **"Zerar juros e multas"** das Pref. de recebimento com cartão estiverem habilitadas.

Se informado um valor de transação maior que o valor restante do saldo, ao clicar em Receber, a seguinte mensagem aparecerá na tela:

**"O valor total da transação não pode ser maior que o valor total dos títulos"**

Dito isso, se ao realizar o recebimento, apareça qualquer erro na tentativa de Finalizar, acesse o **Sankhya Om** novamente, selecione o registro anterior e clique no botão Receber, então um pop-up informando que existem recebimentos pendentes de confirmação surgirá na tela:

**“Existem recebimentos pendentes para este(s) título(s). Caso queira iniciar um novo recebimento, os registros pendentes serão anulados. Deseja prosseguir? Sim ou não”**

Selecionando a opção **"Sim"** o sistema limpará a pendência e abrirá o pop-up de recebimento, tornando o título disponível novamente para receber via cartão, seguindo o fluxo correto. No entanto, caso selecione **"Não"** o pop-up será fechado.

**Observação:** caso informe um Tipo de Título ou Tipo de Cartão que não existe ou que não está configurado para recebimento com cartão, uma mensagem de erro informando que ele não poderá ser utilizado surgirá na tela.

Caso realize um recebimento que possua apenas uma parcela, e nas [Pref. de recebimento com cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es#pref.derecebimentocomcarto) a marcação **"Usar renegociação"** esteja habilitada uma nova renegociação com novo título será gerada.

No entanto, se o recebimento houver múltiplas parcelas e a marcação Usar renegociação estiver habilitada, será gerado um novo título para cada parcela.

---

![Imagem 59: Informações adicionais acerca do Recebimento com cartão:](https://ajuda.sankhya.com.br/hc/article_attachments/21371460815895) **Informações adicionais acerca do Recebimento com cartão:**

Caso o parâmetro **"Confirmar automaticamete o recebimento TEF? - CONFAUTTEF"** esteja habilitado, ao realizar o recebimento com cartão e o saldo estiver igual a zero, o pop-up **"Receber título com cartão"**é fechado e o procedimento do recebimento será concluído automaticamente.

Mas, se o parâmetro CONFAUTTEF estiver desligado, o pop-up continuará aberto até o usuário clicar em **"Finalizar"** para concluir o recebimento.

Finalizado o recebimento, será gerado novos títulos de acordo com os dados preenchidos e enviados, sendo possível imprimir o comprovante.

Ao finalizar a impressão, caso o parâmetro **"Refresh automatico Mov.Fin. conclusão receb. TEF? - REFAUTMOVFINTEF"** esteja desligado, a seguinte mensagem surgirá na tela:

**"Recebimento realizado com sucesso**
**Você pode ver o(s) título(s) gerado(s) por este recebimento ou recarregar a tela com o filtro anteriormente aplicado.**
**Como deseja prosseguir?**

**Ver títulos / Reaplicar filtro"**

Pressione **"Ver títulos"** e todos os títulos criados serão apresentados conforme configuração e recebimento.

Na opção **"Reaplicar filtro"**, o usuário voltará para a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) com os filtros anteriormente aplicados e a seguinte mensagem será apresentada: 

**“O filtro foi replicado com sucesso”**

Se o parâmetro REFAUTMOVFINTEF estiver ligado ao finalizar a impressão do comprovante, será apresentado somente o título recebido no momento da operação atual.

Quando o recebimento via cartão é realizado com o Pay&Go aberto e o processo é encerrado antes da conclusão do recebimento, uma mensagem será exibida na tela, informando que:

**"Ocorreu um erro no processamento da transação. Recomenda-se verificar o status da transação junto a operadora e em seguida tentar reprocessar o recebimentou ou proceder com o recebimento administrativo.**

**Erro: OPERACAO CANCELADA"**

Além disso, durante o processo de recebimento, caso ocorra o encerramento do [Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394-Sankhya-Web-Connection), a mensagem apresentada será:

**"Ocorreu um erro no processamento da transação. Recomenda-se verificar o status da transação junto a operadora e em seguida tentar reprocessar o recebimentou ou proceder com o recebimento administrativo.**

**Erro: Falha de processamento"**

No entanto, se por algum motivo, não for encontrada as pastas C:\PAYGO\Req ou C:\PAYGO\Resp, ou seja, o Web Connection esteja ativo mas o client Pay&Go não, outra mensagem será apresentada:

**"Erro na transação**

**Recomendamos que você verifique o status da transação junto à operadora e, em seguida, tente novamente processar o pagamento ou ainda utilizar o "Recebimento com cartão administrativo" disponível no menu "Outras opções".**

**Erro: Não foi possível copiar o arquivo definitivo intpos.tpm para o novo arquivo intpos.001"**

Mensagens como as mostradas acima surgirão na tela também nas hipóteses de falha em comunicação ao receber ou ao concluir/confirmar. Nesses casos, cancele a transação.

**Observação:** caso queira utilizar um parceiro administrador no financeiro, quando o recebimento for por meio de cartão (TEF ou POS) é necessário ativar o parâmetro **"Utilizar o parc. administradora no financeiro TEF?- USARPARCADMFIN"** e informar o campo **"Parc. administradora"** localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) da tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494). 

---

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 60: Duplicar Duplicar

O botão **"Duplicar"** na Movimentação Financeira ignora o controle de acessos; o que irá determinar se o usuário poderá ou não duplicar um título é o parâmetro **"Permite Duplicar Financeiro? - PERDUPLFIN"**; se o mesmo estiver ligado, ele poderá duplicar, se desligado, não será permitido.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 61: Mais Opções Mais Opções

Para conferir a funcionalidade de cada opção deste botão, acesse o artigo [Movimentação Financeira - Botão Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es).

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela)

### Imagem 62: Exportar Exportar

Por meio do botão Exportar, pode-se exportar o título por meio de PDF, planilhas xls e/ou xlsx.

![Imagem 63: Por meio do botão Exportar, pode-se exportar o título por meio de PDF, planilhas xls e/ou xlsx.](https://ajuda.sankhya.com.br/hc/article_attachments/21373770770583)

Por meio das opções **"ADM - Nota de Débito"** e **"Extrato de KM para cobrança ao cliente"** será possível visualizar os relatórios formatados referente ao Reembolso de KM. Essas opções são exclusivas para usuários Sankhya.

![Imagem 64: Caso queira exportar todas as páginas disponíveis na Movimentação Financeira , clique no botão Exportar e escolha entre…](https://ajuda.sankhya.com.br/hc/article_attachments/21830790958743) Caso queira exportar todas as páginas disponíveis na Movimentação Financeira, clique no botão Exportar e escolha entre as opções **"PDF (.pdf)"** ou **"Planilha (.xlsx)"**. Já, para exportar somente uma das linhas, selecione-a e realize o mesmo processo. Existe ainda a possibilidade de exportar apenas a página atual, faça isso pelo botão Exportar sem selecionar nenhuma linha, e em seguida pressione a opção **"Somente a página atual"**. 

[GIF animado: Imagem 65: Caso queira exportar todas as páginas disponíveis na Movimentação Financeira , clique no botão Exportar e escolha entre…](https://ajuda.sankhya.com.br/hc/article_attachments/21830790977559)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#botesdatela) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#top)

## Parâmetros que influenciam nessa rotina

**Decimais p/ valores de Moeda - DECVLRMOEDA:** caso seja necessário determinar a quantidade de casas decimais a serem consideradas para o arredondamento do campo Vlr Moeda, configure este parâmetro com a quantidade desejada; por padrão, este parâmetro é definido com a quantidade 5 (cinco). Além disso, a configuração realizada no parâmetro em questão, irá compor os valores dos campos Vlr Moeda (Cabeçalho de Notas), Cotação do cadastro de [Valores de Moedas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604754-Valores-de-Moedas), além do próprio campo Vlr Moeda da Movimentação Financeira, como já mencionado.

**Substitui Histórico do Fin.com o Hist.da Baixa? - SUBSTHISTFIN:** se este parâmetro estiver Ligado, o sistema insere no histórico do Financeiro o mesmo histórico da Baixa. No caso da [Baixa Automática](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115773-Baixa-Autom%C3%A1tica), tem-se a opção de sobreposição, substituindo o histórico do financeiro pelo da baixa ou concatenar, acrescentando o histórico da baixa no histórico do financeiro.

**Imprimir modelo da conta na Hora da Baixa? - IMPMODCTABAIX:** se este parâmetro estiver Ligado e na [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) relacionada ao título a marcação **"Emite"** presente na aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas) esteja realizada, logo após a baixa, qualquer modelo que esteja informado também na aba Boletos(s)/Duplicatas do Cadastro de Contas Bancárias, no campo **"Modelo"** será utilizado para impressão automática, independente do tipo.

**Proibir alterar Data de Movto? - TRAVAALTDHMOV:** se este parâmetro estiver desativado será permitida a alteração da Data de Movimento na Movimentação Financeira; caso esteja acionado, não será possível modificar a Data de Movimento.

**Abrir rateio p/ títulos duplicados no financeiro? - ABRERATDUPFIN:** este parâmetro quando ligado, na duplicação de um título que possua rateio, o sistema apresentará um pop-up questionando se deseja ou não copiar o rateio do título original. Se desligado, o rateio do título original será sempre copiado.

**Renumera nosso número sempre? - RENNOSSONUM:** se este parâmetro estiver ativado, o sistema irá sobrepor ou gerar nosso número, código de barras e linha digitável para título. Nesta situação, para gerar o nosso número, o banco da conta será analisado e se não estiver dentre os bancos já implementados no sistema, será apresentada a mensagem:

**"Banco xxx não implementado no Sankhya-W para geração de boleto."**

Para que mantenha o parâmetro ligado e não apresente a mensagem tem-se duas opções:

1. Se a [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) estiver cadastrada com o Tipo de conta definido como Caixa-Tesouraria ou Caixa (PDV), o banco não será analisado;
2. Se o convênio for de código 1, o parâmetro não será analisado, nem o banco.

Se o parâmetro citado estiver desligado, o sistema não irá sobrepor o número. Não existindo esse número, este será gerado, a menos que o Tipo da Conta seja Caixa-Tesouraria ou Caixa (PDV).

**Importante:**

- Caso indique no caminho da impressora um arquivo TXT, o sistema gerará o arquivo no lugar indicado e apresentará um pop-up solicitando abertura ou não do arquivo gerado.
- Se for informado no caminho da impressora a palavra **"PADRÃO"**, a impressora padrão do sistema será buscada para impressão, mas se tiver com um modelo de arquivo txt e a impressora padrão for PDF, a impressão não será feita, porque arquivo txt não é impresso em PDF.
- O parâmetro **"Utilizar Pré-Data para Data Lançamento - USAPRDTDTLANC"** deve estar desligado para que seja possível visualizar um título financeiro com cheque pré-datado tendo realizado a baixa. Caso o parâmetro esteja ligado, só será possível a visualização da baixa do título se for realizada a filtragem pela Data de Vencimento.

**Notas:**

- As informações para impressão serão buscadas da conta bancária do título e não da conta de baixa;
- A conta do título deve estar marcada com a opção **"Emite"** presente na aba [Boleto(s)/Duplicatas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#ababoletosduplicatas) do Cadastro de [Contas Bancárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas), caso contrário, a impressão não será realizada.

**Permite troco p/ cartão (Créd/Déb/Voucher)? - PERMTROCOCARTAO:** quando este parâmetro estiver desabilitado, não será permitido o troco em títulos de cartão: débito, crédito ou voucher. Caso esteja habilitado, será autorizado o troco em títulos de cartão.

**Observação:** utilizando o pagamento com vários títulos, o sistema buscará um título que permite o troco antes de lançar uma exceção.

**Usar Desconto Financeiro por Parceiro? - USADESCFIN:** quando estiver ligado, será habilitada a aba [Descontos Financeiros por Parceiro/Período](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606354-Descontos-Financeiros-por-Parceiro) na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros). Diante disto, pode-se realizar Descontos por Parceiro utilizando as informações inseridas nesta aba e/ou na tela [Descontos Financeiros por Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606354-Descontos-Financeiros-por-Parceiro).

**Nota:** para que o sistema considere na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) o desconto informado na aba ou tela acima mencionadas, faz-se necessário que o consultor ou implantador crie suas próprias regras para aplicação desta função por meio do botão ![Imagem 66: Nota: p ara que o sistema considere na tela Movimentação Financeira o desconto informado na aba ou tela acima…](https://ajuda.sankhya.com.br/hc/article_attachments/21401694014359) **"Ações"** .

**Utiliza orçamento por data de entrada e saída - UTIORCDTENTSAI:** quando este parâmetro encontrar-se habilitado, os lançamentos realizados nesta tela e nas Centrais de Nota terão como obrigatório o preenchimento do campo **"Dt. Entrada/Saída"**.

**Observação:** ao tentar confirmar um registro onde a Data de Entrada/Saída seja menor do que a Data de Negociação, o sistema emitirá a seguinte mensagem:

**"Data de Entrada/Saída deve ser maior ou igual a data de Negociação".**

**Estorno com Recomposição Opcional? - ESTRECOMPOPC:** este parâmetro quando estiver habilitado e o título for correspondente à recomposição, no momento de finalizar o estorno o sistema apresentará um pop-up questionando se deseja recompor o título original. Por outro lado, quando encontrar-se desabilitado, será apresentada uma mensagem informando que ao concluir, será recomposto o título original, ou seja, não poderá realizar o estorno.

**Aumentar limite de caracteres do Histórico - TAMVARSHISTCTBZ:** através deste parâmetro, pode-se aumentar ou diminuir o limite de caracteres permitidos para o Histórico de Lançamentos Contábeis com origem do financeiro.

**Usa faturamento provisão (Meta/Orçamento) - USAFATPROVORC:** habilitando este parâmetro, serão apresentadas as opções **"Faturar provisão Meta/Orçamento"** e **"Estornar provisão Meta/Orçamento"** no botão [Mais Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Mais-Op%C3%A7%C3%B5es) da Movimentação Financeira.

**Observação:** selecionando a opção Faturar provisão Meta/Orçamento será aberto um pop-up e, neste momento, pode-se alterar o vencimento e valor de provisão, escolher opções para utilizar o valor e vencimento original ou então, definir se o rateio será ou não copiado para o novo título.

**Permite a troca da TOP para mov. financeiro baixado? - TROCATOPFIN:** este parâmetro, quando ativado, permitirá a troca da TOP de títulos já baixados; do contrário, estando desabilitado, o sistema proibirá a troca da TOP dos títulos que já foram baixados, emitindo a seguinte mensagem:

**"Não é permitido alterar a TOP de um título já baixado. Em caso de dúvidas, contate o administrador do sistema!".**

**Permite troco p/ cheque? - PERMTROCOCHEQUE:** quando este parâmetro estiver desligado, não será possível efetuar uma baixa com troco, quando o recebimento for feito com o [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) **"Cheque"**; caso seja realizado o recebimento de um título utilizando o pagamento com vários títulos e o parâmetro estiver ligado, o sistema tentará encontrar um título que permita troco antes de lançar uma exceção.

**Valida tipo de natureza (Receita / Despesa) na movimentação financeira - VALIDATIPONAT:** quando este parâmetro estiver ligado, na Movimentação Financeira só será permitido lançar naturezas do Tipo = Receita para os títulos que são de Receitas e naturezas do Tipo = Despesa, somente em financeiros de Despesas.

**Agrup. títulos monitorados na ger. remessa de EDI? - AGRTITMONREMEDI:** ao ligar esse parâmetro, pode-se monitorar os títulos agrupados em boletos na remessa de EDI. Assim, ao realizar alterações nos títulos como descontos, cancelamentos, ou baixa agrupados, essas alterações incidirão no envio de EDI.

**Baixa de múltiplos títulos - OFEROPCBAIXTIT:** ao habilitá-lo e selecionar a opção **"Baixa automática"** do campo **"Valor"**, quando mais de um título for selecionado para realizar a baixa agrupada, o sistema irá automaticamente transferi-lo para a tela Baixa Automática e os títulos selecionados serão exibidos.

**Zerar campos ao duplicar registro na Mov. Fin. - DEFCAMGRD:** nesse parâmetro, pode-se informar os campos que serão zerados quando um registro for duplicado na Movimentação Financeira. É importante incluir um ponto e vírgula (;) entre cada campo e ao final da lista. Por exemplo:

- DTNEG;
- DTNEG;NUMNOTA;VLRDESDOB;

**Utilizar o parc. administradora no financeiro TEF? - USARPARCADMFIN:** caso queira utilizar o parceiro administrador no financeiro, quando o recebimento for por meio de cartão (TEF ou POS) é necessário ativar este parâmetro e informar o campo **"Parc. administradora"** localizado na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) da tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494). 

**Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT:** por meio desse parâmetro, pode-se limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades Exportar como PDF, Exportar como planilha e Visualizar em cubo. Informe um número inteiro, que representa o limite de registro que serão exportados, por exemplo 50 registros, 100 registros; dependendo da necessidade da Empresa.

**Baixa agrupada com Moedas e cotações diferentes - BAIXAAGRUMOEDA:** ao ligar esse parâmetro, o sistema irá realizar a baixa agrupada de títulos em moedas iguais, mas com cotações diferentes. Para realizar essa baixa, verifique também se os parâmetros **"Mostrar valores de moedas convertido no financeiro - MOSTRAVLRMOEDA"** e **"Baixa de múltiplos títulos - OFEROPCBAIXTIT"** estão ligados. Dessa forma, na Movimentação Financeira, selecione dois ou mais títulos com moedas estrangeiras iguais e cotações diferentes. Assim, a somatória dos títulos realizada no campo **"Vlr. Desdob. Moeda"** da sub-aba **"Fechamento Baixa em Moeda"** dessa tela será efetuada conforme a sua cotação individual. 

**Permite editar/excluir tít. receb. administrativo? - PERMEDITRECADM:** caso queira realizar determinada alteração em recebimentos com cartão na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414), basta ligar esse parâmetro. Porém, é importante ressaltar que se não houver a conferência de lançamentos do cartão e baixa manual na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753), poderão ocorrer inconsistências nos lançamentos e/ou recebimentos.

**Realizar compensação de devolução usando acerto - COMPDEVACERTO:**quando ligado, esse parâmetro irá preencher o campo **"Nro Compensação/Acerto"** da aba Geral dessa tela caso haja uma compensação de devolução realizada na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas). 

**Zerar multa qdo estorno? - ZERARMULTEST:** se este parâmetro estiver ligado, ao realizar o Estorno de uma Baixa no financeiro, o campo **"Multa"** será zerado.

**Modo grade configurável na pesquisa? - CONFMODGRDPESQ:** por padrão é apresentado desativado, quando ligado será possível realizar a configuração de ordenação das colunas nos pop-up's de pesquisa disponíveis no sistema, ou seja, pode-se ordenar as colunas da forma desejada, porém a primeira coluna será a coluna referente ao campo utilizado como pesquisa. 

**Tempo em seg. p/ timeout no Recebimento TEF - TEFRECTIMEOUT:** no campo **"Inteiro"** desse parâmetro, pode-se informar a tolerância de tempo antes da conclusão do processo por meio das API's de recebimento.

**Observação:** o valor inserido neste parâmetro deve ser 0 ou superior a 60.

**Confirmar automaticamete o recebimento TEF? - CONFAUTTEF:** quando ligado, o recebimento será concluído de forma automática.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#top)

![Imagem 67: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/21344384424343) Acesse também:

[Movimentação Financeira - Conceitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira)

[Movimentação Financeira - Baixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos)

[Movimentação Financeira - Botão Mais Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es)
