---
id: "360044606494"
titulo: "Tipos de Título"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:45Z"
rotulos: ["Configuração", "CMC7", "Parceiro", "Movimentação Financeira", "Crédito", "Resultados Gerais", "TEF", "Preferências", "Financeiro", "ALTERATIPTIT", "Float", "Espécie", "Gerente On Line", "GOL-CVTIT", "LIMITE", "ORDEM DE CARGA", "RENEGTIPTIT", "TIPOPRAZO", "Tipos de Título", "Títulos Vencidos", "USALIBLIM", "VALLIMCRED", "br.com.sankhya.fin.cad.tipostitulo", "Tipos de Título manual", "HABFISCALPOSTIT", "Cadastro e configuração de Tipos de Títulos.", "Subtipos e controle financeiro detalhado.", "Regras e parâmetros específicos de pagamento."]
---

# Tipos de Título

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312314390935) Módulo: Financeiro > Arquivo > Cadastros
```

---

# Funcionalidade Tipos de Títulos

Nesta tela são cadastrados os Tipos de Títulos que, ao serem vinculados a um [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), serão utilizados pela empresa na geração de documentos para pagamento ou recebimento tais como, Boletos, Duplicatas, etc; são empregados nas [Centrais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas) em emissões de notas, de modo a alimentar o financeiro destas; além de compor os lançamentos na própria tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874).

[Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal)                                                          [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)

[Aba Fast Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abafastservice)                                                        [Aba Renegociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abarenegociao)

[Aba Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaacertodeordemdecarga)                             [Aba Super Sintegra (Livro Eletrônico)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abasupersintegralivroeletrnico)

[Aba Transferência de Cheques/Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abatransfernciadechequesttulos)                    [Aba Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto)

[Botões do topo da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#bot%C3%B5esdotopodatela)                                            [Parâmetros que influenciam nessa tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#parmetrosqueinfluenciamnessatela)

## Painel Principal

Inicialmente, para realização de um cadastro, informe os campos **"Tipo de Título"** e **"Descrição"**, que devem ser informados com o código de identificação do título (pode ser automática ou manual) e a nomenclatura do Tipo de Título, respectivamente.

![Imagem 2: Inicialmente, para realização de um cadastro, informe os campos "Tipo de Título" e "Descrição" , que devem ser…](https://ajuda.sankhya.com.br/hc/article_attachments/4403050293271)

Além disso, preencha o campo **"Subtipo"**, conforme as seguintes opções:

- A vista;
- A prazo;
- Parcelada;
- Cheque pré-datado;
- Crediário;
- Financeira;
- Cartão de Crédito;
- Cartão de Débito;
- Voucher;
- PIX;
- PIX POS.

**Nota:** ao realizar uma venda com o subtipo PIX POS, a opção Débito deve ser obrigatoriamente selecionada no campo Operação CTF nas [Preferências do Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto) para que não haja impacto no cálculo da data do vencimento.

Essas opções atuarão juntamente com a marcação **"Tipo de Título"** da opção **"Vendas por Subtipo do"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853-Prefer%C3%AAncias-Gerente-On-line#abageral) das [Preferências do Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108853) apresentando nos **"Resultados Gerais"** os valores dentro de cada subtipo do tipo de título configurado, ou seja: À vista, A prazo, Parcelada, Cheque pré-datado, Crediário, Financeira, Cartão de crédito, entre outras. Garantindo o controle real do que foi vendido à vista, a prazo, parcelado e etc., mesmo quando por exemplo, o cliente efetuar um pagamento parte em cartão de crédito e parte em cheque.

**Importante:** ao inserir/alterar um tipo de título com subtipo **"Cartão de débito"** ou **"Cartão de crédito"**, o campo **"Parc. Administradora"** (administradora do cartão) deverá ser informado. Caso você tente salvar um **"Tipo de Título"** que esteja nestas condições e que não esteja com o campo **"Parc. Administradora"** preenchido, o sistema emitirá a seguinte mensagem:

**"Campo 'Parc.Administradora' deve estar preenchido, com a operadora do cartão escolhido no campo subtipo."**

**Observação:** o campo **"Subtipo"** também faz parte da análise do Fast Service pois, uma vez que o parâmetro **"Prazo a utilizar na geração do financeiro - TIPOPRAZO"** esteja configurado como Tipo de Título, o Fast buscará neste campo as informações para compor o financeiro da venda do cupom fiscal.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Geral

![Imagem 3: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/4403050311831)

A marcação **"Ativo"**indicará que o Tipo do Título está ativo. Caso o tipo de título tenha a marcação Ativo desabilitada, o sistema validará o tipo de título nas seguintes telas:

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874)
- [Impressão de Cheques](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115313-Impress%C3%A3o-de-Cheques)
- [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s-)
- [Configuração de Tipos de Títulos p/ Acerto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606974-Configura%C3%A7%C3%A3o-de-Tipos-de-T%C3%ADtulos-p-Acerto)
- [Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606914-Gera%C3%A7%C3%A3o-Arquivo-de-Remessa)
- [Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos)
- [Portais de Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras), de [Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) e de [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas)
- [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)

**Nota:** nas telas que pedem como informação um título (como a de Movimentação Financeira), ao se procurar um título, os não ativos não serão listados.

A **"Espécie"**pode ser inserida manualmente ou utilizando o botão de pesquisa. Essa informação é utilizada na geração dos livros fiscais. Exemplo: Nota Fiscal, Cheque, Boleto.

**Observação:** o cadastro da Espécie será feito diretamente na tela Tipos de Título, sendo que, a lupa apenas facilitará a busca de todas as espécies cadastradas anteriormente. Caso cadastrarmos um novo Tipo de Título com uma espécie nova, no próximo título a ser cadastrado, a espécie que informamos anteriormente será disponibilizada.

**Nota:** nos livros fiscais, a informação da Espécie é utilizada para gerar o livro dos financeiros e as rotinas de Registro de Entrada e Saída e alguns registros do Sintegra também utilizam esta informação.

O campo **"Float (Carência)"**determina o número de dias que o banco levará para creditar títulos pagos pelos clientes na conta corrente da empresa. Exemplo de Float: Um boleto com vencimento no dia 25/11, cujo Tipo de Título consta um float = "02", aparecerá nos relatórios de fluxo de caixa com vencimento no dia 27/11 (neste exemplo não há feriado nem fim de semana entre os dias 25/11 e 27/11).

Com a marcação **"Considerar dias úteis"** habilitada, o sistema irá considerar a data de vencimento juntamente com a marcação **"Considerar float"** das telas [Agenda Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115533-Agenda-Financeira), [Fluxo de Caixa Sintético](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606254-Fluxo-de-Caixa-Sint%C3%A9tico-), [Fluxo de Caixa Matricial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606874-Fluxo-de-Caixa-Matricial) e [Fluxo de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051904053-Fluxo-de-Caixa) para exibir os títulos  análises nas telas mencionadas.

A Transferência Eletrônica de Fundos (TEF) é uma operação que permite efetuar vendas via cartões de crédito, acessando diretamente suas respectivas administradoras. Assim, no campo **"Forma Pagamento TEF"**, informe a Forma Pagamento TEF.

Além disso, ao lado do campo Forma Pagamento TEF, observe o ícone ![Imagem 4: Além disso, ao lado do campo Forma Pagamento TEF , observe o ícone que contém a seguinte informação:](https://ajuda.sankhya.com.br/hc/article_attachments/17213123007511)que contém a seguinte informação:

**“Forma de pagamento TEF ou Bandeiras de cartões: São identificadores que representam as empresas emissoras de cartões e tem o papel de facilitar as transações financeiras junto aos bancos. Ex: Mastercard, Visa, Elo dentre outras.”**

**Observação:** são permitidas somente as formas de pagamento abaixo especificadas. O intuito disso é possibilitar a utilização juntamente com o Fast Service. Desta forma, você não consegue informar qualquer forma de pagamento fora do padrão, evitando assim, a não abertura do TEF pelo Fast Service.

![Imagem 5: No entanto, caso não encontre a bandeira desejada, será possível cadastrá-la, basta digitar o nome da bandeira, e essa…](https://ajuda.sankhya.com.br/hc/article_attachments/17213123013655) No entanto, caso não encontre a bandeira desejada, será possível cadastrá-la, basta digitar o nome da bandeira, e essa inserção será feita e salva automaticamente.

Formas de Pagamentos permitidas:

- AMEX;
- REDECARD;
- REDECARD CHEQUE;
- TECBAN;
- TECBAN CHEQUE;
- VISANET;
- CIELO;
- MAXVAN;
- POLICARD;
- REDECOMPRAS;
- SODEXO;
- VALECARD;
- VEROCHEQUE;
- <VAZIO>.

**Importante:** o campo Forma Pagamento TEF não terá seu preenchimento exigido, caso a marcação Utiliza POS esteja realizada e no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal), o campo Subtipo esteja definido com as opções **"Cartão de Crédito"**, **"Cartão de Débito"** ou **"Voucher"**. Uma vez que o campo Utiliza POS não esteja assinalado, o preenchimento do campo Forma Pagamento TEF será indispensável.

Considere ainda que, quando a marcação Utiliza POS estiver habilitada, o campo Forma Pagamento TEF só ficará preenchido se o parâmetro **"Permite informar Fiscal quando o título for POS - HABFISCALPOSTIT"** estiver ligado, do contrário ao salvar a inclusão do Tipo de Título, o referido campo ficará vazio.

No campo **"% Taxa Administradora"** informe a porcentagem cobrada pela administradora de cartões de crédito na operação de TEF. Quando este campo tiver um percentual informado e o tipo de título for utilizado, a taxa será calculada no financeiro da nota e apresentada no campo Taxa Administrativa.

No campo **"Validar Qtd. Máx. Títulos Vencidos"** você define se será ou não validada a quantidade máxima de títulos vencidos, configurada na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) do [Cadastro do Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros). Assim, no faturamento de um título que tenha este campo configurado, o sistema verificará quantos títulos vencidos há para o parceiro. Se estes excederem a quantidade informada no campo **"Quant.Máx.Títulos Vencidos"** da aba Crédito no Cadastro do Parceiro, o sistema barrará o faturamento.

No campo **"Mensagem p/ exibir na tela de baixa"** você tem a opção de descrever textos para lembrá-lo sobre algo que julgar necessário. A mensagem será apresentada na tela de Movimentação Financeira no momento da baixa utilizando esse tipo de título.

Informe no campo **"Grupo p/ Limite Crédito"** se o título é ou não de terceiros, anotando neste a palavra **"Terceiros"** ou **"Grupo Terceiros"**. Geralmente são usadas essas descrições, porém o sistema aceitará qualquer descrição neste campo, validando-o da mesma forma. Esse procedimento é usual para **"Cheque Pré-datado"** e **"Cheque Pré-datado de Terceiros"**.

**Nota:** ao lançar um título pela tela de Movimentação Financeira cujo Tipo de Título esteja marcado como **"Terceiros"**, se esse ultrapassar o limite de crédito estabelecido no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros), aba [Limite de Crédito p/ Grupo Tip. Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abalimitedecrditopgrupotip.dettulo), o sistema não permitirá salvá-lo e emitirá a mensagem: Grupo: Terceiros Lim.: xxx Total: xxx.

É importante observar também as seguintes configurações:

- O parâmetro **"Usar liberação de limites por alçada? - USALIBLIM"** deve estar habilitado.
- O título a ser lançado deve ser de **"Receita"**.
- O parâmetro **"Valida limite de crédito? - VALLIMCRED"** deve ser diferente de **"Não valida"**.

A marcação **"Informar CMC7?"**deve ser utilizada apenas para tipo de título igual a **"Cheque"**. Na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874), quando você realiza a baixa de um título selecionando a opção **"Pagamento com Vários Títulos"**, se o tipo de título informado for um que possua esta marcação, o sistema abrirá, automaticamente, a tela para a Validação da Banda CMC7 do cheque que está sendo utilizado na baixa. A validação do cheque também poderá ser feita pela opção **"CMC7"**, do botão **"Outras opções..."**, na **"Movimentação Financeira"**, desde que o título esteja configurado para **"Informar o CMC7"**.

O campo **"Cód. Grupo"** associará o **"Tipo de Título"** que está sendo cadastro a um [Grupo de Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606414).

Nos campos de **"Contas contábeis"** são informadas as contas contábeis para comunicação com o Módulo de Contabilidade. Podem ser cadastradas até três contas contábeis: **"Conta contábil 1"**, **"Conta contábil 2"** e **"Conta contábil 3"**.

**Observação:** em relação aos campos **"Conta Contábil 1,2 e 3"** desta tela, você deve levar em consideração a máscara para **"Plano de Contas"** com a qual a empresa irá trabalhar pois, quando você clicar na tela de pesquisa dos campos de Conta Contábeis, o sistema buscará esta máscara para mostrar a hierarquia. A máscara para o Plano de Contas será configurada através do parâmetro **"Máscara para Plano de Contas - MASCPLANCTA"**, que precisa ser criado na base de dados.

Já o campo **"Parc. Administradora"** representa as empresas responsáveis por intermediar as transações realizadas com cartões de crédito entre os estabelecimentos comerciais e as instituições financeiras. Elas fornecem os equipamentos como máquinas de cartões de crédito/débito e sistemas necessários para que os estabelecimentos aceitem pagamentos com cartões.

No ícone ![Imagem 6: No ícone terá a seguinte informação:](https://ajuda.sankhya.com.br/hc/article_attachments/17213123007511) terá a seguinte informação:

**"O cadastro do Parc. Administrador deverá ser informado a fim de identificar o Parceiro responsável por intermediar as transações realizadas em cartões entre as instituições financeiras. Ex: Cielo,Redecar,GetNet, Stone dentre outras"**

Os campos **"Custo variável"**e **"Valor custo Variável"** permitirão análise futura dos Gastos Variáveis no [Gerente On-Line](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109613-Gerente-On-line) e, só estarão visíveis, se o parâmetro **"Usar % e Vlr Custo Variável do cad.de Tip.Títulos? - GOL-CVTIT"** estiver habilitado.

Estes dois campos atuam da seguinte forma no sistema:

- Crie um Tipo de Título informando nestes campos um percentual ou valor de custo variável, ou ainda, os dois;
- Logo após, associe este Tipo de Título a um [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o), aba **"Parcelas"**, no campo **"Tipo de Título"**;
- Todas as vendas que forem efetuadas com este Tipo de Negociação, irão impactar no **"Gasto Variável"**, em cima do percentual ou valor, ou os dois, informados no Tipo de Título;
- Esta análise pode ser feita no Gerente On-Line do MGE Comercial, filtrando a Nota de Venda pelo seu número, na guia **"Resultados Gerais"**, logo após, na guia **"Margem de Contribuição"**, na coluna **"Gasto Variável"**, você visualizará o Gasto Variável para a Nota em questão.

Insira no campo **"Código Detalhamento Receita (GNRE)"** o Código definido pela SEFAZ (Secretaria da Fazenda do Estado) para designar um determinado tipo de pagamento que no nosso caso será referente à GNRE.

Informe o **"Código do Produto (GNRE)"** conforme tabela da SEFAZ/UF de acordo com a exigência ou não desta.

O campo Código Detalhamento Receita (GNRE) é de preenchimento obrigatório para a geração. Já os campos **"Código detalhamento Receita (GNRE)"** e Código do Produto (GNRE), deverão ser preenchidos de acordo com a necessidade da UF, pois, existem UF’s como DF que exigem que estes campos sejam gerados no XML.

Saiba mais, através do link [GNRE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025392893-Gera%C3%A7%C3%A3o-de-Lote-GNRE).

**Ajusta Valor Presente:** Veja informações sobre [Contabilização de Financeiros com Ajuste ao Valor Presente](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598734) acessando o link.

Determine no campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** o tipo de pagamento a ser considerado no lançamento de NFC-e / NF-e / CF-e, de acordo com as seguintes opções:

- 01-Dinheiro;
- 02-Cheque;
- 03-Cartão de Crédito;
- 04-Cartão de Débito;
- 05-Cartão da Loja (Private Label);
- 10-Vale Alimentação;
- 11-Vale Refeição;
- 12-Vale Presente;
- 13-Vale Combustível;
- 14-Duplicata Mercantil (Desativado);
- 15-Boleto Bancário;
- 16-Depósito Bancário;
- 17-Pagamento Instantâneo (PIX) - Dinâmico;
- 18-Transferência bancária, Carteira Digital;
- 19-Programa de fidelidade, Cashback, Crédito Virtual;
- 20-Pagamento Instantâneo (PIX) – Estático;
- 21-Crédito em Loja;
- 22-Pagamento Eletrônico não Informado - falha de hardware do sistema emissor;
- 90-Sem pagamento;
- 99-Outros.

**Nota:** caso este campo seja definido com as opções **"Cartão de Crédito"** ou **"Cartão de Débito"** e no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal), o campo Subtipo também seja determinado com estas opções, será habilitada a aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto).

Para os subtipos **"Cartão de Crédito"**, **"Débito"** e **"PIX POS"** (Painel Principal, campo Subtipo), será habilitada a marcação "**Utiliza POS"**visando identificar os tipos de títulos que a empresa utiliza para realizar o recebimento via sistemas POS.

**Nota:** caso você queira que o pagamento realizado por Tipos de Título que utilizam a marcação Utiliza POS seja confirmado de imediato, utilize o parâmetro **"Confirma pagamento no POS? - CONFIRPAGTOPOS"**.

A marcação **"Informar NSU opcional"** pode ser habilitada para que o campo **"NSU"** do [Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web#Recebimento) por [Tipo de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) do [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web) não seja de preenchimento obrigatório, ou seja, este terá uma configuração opcional.

Você deve preencher o campo **"Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros)"** se o campo Tipo de pgto para NFC-e /NF-e /CF-e for igual à opção 99 - Outros. Assim, o sistema irá completar a tag <**xPag**> para que o preenchimento do campo Descrição do Tipo de Pagto NFC-e/NF-e/CF-e (Outros) seja identificado no XML.

Escolha no campo **"Indicador da Receita (registro F525 - EFD Cont.)"**, a opção que será utilizada para o preenchimento do registro F525.

**Nota:** lembre-se também que o campo **"Informações complem. (registro F525 - EFD Cont.)"** ficará disponível para preenchimento apenas se a opção **"99 - Outros"** do campo acima for selecionada.

Ao selecionar um Tipo de Título na Central de Notas, e este  título estiver com a marcação **"Proibir impressão boleto?"** realizada, este título não será impresso como boleto e também não possuirá taxa de boleto. Portanto, ao confirmar a nota na [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110973-Central-Compras-Vendas-Mov-Internas), poderá ser observado que no rodapé da nota em que o tipo de título selecionado está com essa marcação efetuada, as linhas [Cód. Barras Receb.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#graderodap) e **"Linha Dig. Receb."** não estarão preenchidas.

Essa configuração também influencia a exibição dos lançamentos na tela [Impressão de Boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094-Impress%C3%A3o-de-Boleto-s). Os títulos com a marcação Proibir impressão de boleto? ativada não serão exibidos na grade de seleção para a impressão de boletos.

**Seção Integrar EConect**

Com a marcação do campo **"Integrar com Econect"**, o tipo de título em questão realizará integração com o EConect.

O campo **"Cód. Finalizadora"** é de preenchimento obrigatório, caso a finalizadora seja diferente de cartão de crédito.

O campo **"Grupo Finalizadora"** é de preenchimento obrigatório, caso na SOCIN seja cadastrado um grupo de finalizadora dentro de uma finalizadora pai.

A informação **"Bandeira Cartão"** é de preenchimento obrigatório, caso a finalizadora seja Cartão de Crédito ou Débito. Este campo realizará o DE-PARA com o código da administradora de cartão de crédito. Você pode cadastrar uma ou mais bandeiras de cartão para o mesmo Tipo de Título, sendo seu separador a vírgula **","**. Por exemplo 3,10,2001.

Efetue a marcação **"Convênio"** caso o tipo de finalizadora no EConect seja Convênio Empresa ou Convênio Cliente, pois ambos possuem controle de saldo. Você pode obter maiores informações sobre os dois tipos de convênios ao final deste tópico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Fast Service

![Imagem 7: Aba Fast Service](https://ajuda.sankhya.com.br/hc/article_attachments/31969126017943)

Preencha o campo **Instituição Credenciadora do Cartão**, para que o sistema gere a tag necessária à emissão correta do CF-e.

Efetuando a marcação **"Utiliza no Fast Service?"**, esse tipo de título poderá ser usado no Fast Service.

O campo **"Baixa automática"** indicará se ocorrerá ou não baixa automática, ao utilizar esse tipo de título.

Quando a marcação **"Conferência"**estiver realizada neste cadastro, solicitará no Fast Service a conferência dos valores para fechamento do caixa na utilização deste Tipo de Título.

Se a marcação **"Imprime Comprovante?"** for efetuada, faz com que seja realizada a impressão de um relatório gerencial logo após a impressão de um cupom fiscal no Fast Service. Este relatório gerencial consiste em um documento padrão do sistema e de caráter não fiscal (não é possível editá-lo).

Informe no campo **"Prazo"** o valor em dias para prazo. Quando o parâmetro **"Prazo a utilizar na geração do financeiro - TIPOPRAZO"** estiver apontando para **"Tipo Título"**, o sistema lançará no financeiro do título, o vencimento, conforme a marcação.

**Nota:** existe limitação neste campo ao digitar valores menores que zero ou maiores que 32767. A seguinte mensagem será emitida:

**"Valores permitidos para o 'Prazo' de 0 a 32767."**

Caso informe um valor acima de 32767 o sistema emitirá a mensagem:

**"Propriedade 'TipoTitulo.PRAZO' com largura acima do limite"**

No campo **"Nro. Parcelas"** informe a quantidade de parcelas que podem ser utilizadas quando o Tipo de Título em questão for empregado. Essa configuração não possui ligação com nenhuma outra rotina do **Sankhya Om**, sendo válida exclusivamente para aqueles que fazem uso do Fast Service e [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Renegociação

Para que esta aba seja apresentada, é necessário que o parâmetro **"Calcular multa e juro pelo Tipo de Título - RENEGTIPTIT"** esteja ativado.

![Imagem 8: Para que esta aba seja apresentada, é necessário que o parâmetro "Calcular multa e juro pelo Tipo de Título -…](https://ajuda.sankhya.com.br/hc/article_attachments/6126317003159)

Informe a moeda no campo **"Cód. Moeda"**.

No campo **"% Juros"** informe o percentual de juros que será acrescentado no título ao utilizar esse Tipo de Título.

No campo **"% Multa"** informe o percentual de multa.

**Observação:** os cálculos feitos posteriormente na tela de [Renegociação de Títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115393) levarão em consideração estes três campos descritos acima.

Quando a marcação **"Imprimir Pix/Boleto/Duplicata p/ os títulos renegociados"** estiver realizada, fará com que para cada novo título na Renegociação de Títulos seja impresso um boleto/duplicata conforme modelo configurado na [Conta bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas). É importante salientar que o sistema irá olhar para o Tipo de Título informado no ato do parcelamento e que, essa marcação é levada em consideração independente do parâmetro RENEGTIPTIT estar ligado ou desligado.

---

#### 📌 Manutenção [Aprimoramento na Renegociação de Títulos]

🔧**Tipo**: Melhoria 📅**Data**: 28/05/2025 🛠️**Versão Aplicável**: 4.35b33

**Descrição**

O processo de **Renegociação de Títulos** foi aprimorado para oferecer uma experiência mais intuitiva e alinhada com suas escolhas. Agora, ao renegociar um título e optar por um novo tipo que não seja "Boleto" ou "Pix" (como, por exemplo, "Nota Fiscal"), o sistema entenderá sua intenção e não apresentará mais a janela para emissão de boletos ou Pix.

Isso significa que você não verá mais avisos desnecessários. A janela de emissão de boleto/Pix só aparecerá quando o novo tipo de título selecionado realmente for um "Boleto" ou "Pix", e se a **Conta Bancária** estiver configurada para emitir boletos, e o **Tipo de Título** estiver marcado para "Imprimir Pix/Boleto/Duplicata para os títulos renegociados".

Com essa melhoria, você pode prosseguir com suas renegociações de forma mais fluida, sabendo que o sistema reage de acordo com o tipo de título que você escolher, evitando etapas extras quando elas não são necessárias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Acerto de Ordem de Carga

![Imagem 9: Aba Acerto de Ordem de Carga](https://ajuda.sankhya.com.br/hc/article_attachments/4403057427095)

Nesta aba, efetue as marcações que serão utilizadas no Acerto de Ordem de Carga.

- Valor baixado pode ser igual ao Retornado?;
- Transferir a diferença entre o valor Retornado e o Baixado?;
- Pode Baixar?.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Super Sintegra (Livro Eletrônico)

![Imagem 10: Aba Super Sintegra (Livro Eletrônico)](https://ajuda.sankhya.com.br/hc/article_attachments/4403062929687)

O campo **"Indicador do Tipo de Título"** possui as seguintes opções de escolha:

- 00-Duplicata;
- 01-Cheque;
- 02-Promissória;
- 03-Recibo;
- 99-Outros.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Transferência de Cheques/Títulos

![Imagem 11: Aba Transferência de Cheques/Títulos](https://ajuda.sankhya.com.br/hc/article_attachments/4403062932375)

A marcação **"Pode transferir título pendente?"**indicará se um título Pendente poderá ser usado na tela de transferência de títulos antes de baixado.

A marcação **"Pode transferir depois de baixado?"** indicará se um título poderá ser usado na tela de transferência de títulos após a baixa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Aba Preferências de Cartão

As configurações realizadas nesta aba estão ligadas à rotina de [Integração com TEF AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873).

**Importante:** os campos desta aba serão habilitados para uso caso os campos **"Tipo de pagto para NFC-e / NF-e / CF-e"** e **"Subtipo"** presentes na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) e no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo##painelprincipal), respectivamente (também no Cadastro de Tipos de Título), estejam definidos como **"Cartão de Crédito"** ou **"Cartão de Débito"**.

![Imagem 12: Importante: os campos desta aba serão habilitados para uso caso os campos "Tipo de pagto para NFC-e / NF-e / CF-e" e…](https://ajuda.sankhya.com.br/hc/article_attachments/4403057458839)

Você deverá configurar todos os campos presentes nesta aba:

Determine no campo **"Operação CTF"** a operação primordial a ser realizada pelo CTF, dentre as seguintes opções:

- Débito;
- Créd. Parcelado Lojista (sem juros);
- Créd. Parcelado Administradora (com juros);
- Créd. à vista;
- Voucher;
- Débito Pré-datado;
- Débito Parcelado;
- Débito Parcelado com parcela à Vista.

Defina no campo **"Vencimento"**, de 1º a 31, qual a data de vencimento pertinente ao cartão.

Estabeleça no campo **"Tipo vencimento"** como se dará o vencimento do cartão; pode-se fazê-lo estabelecendo um dia fixo ou considerando a data atual somando-a ao vencimento. Temos as seguintes alternativas:

- Dia fixo;
- Hoje + Vencimento.

Após selecionar uma opção no campo Operação CTF, caso os campos Vencimento e Tipo de Vencimento não estejam preenchidos com nenhuma informação, a data de vencimento a ser puxada no momento da venda no PDV Web obedecerá a utilizada nas regras de recebimento de cartões, de acordo com cada modalidade:

**Operação CTF:** Débito
**Recebimento:** 1 dia

**Operação CTF:** Créd. a vista
**Recebimento:** 30 dias

**Operação CTF:** Créd. Parcelado Lojista (sem juros)
**Recebimento:** 30 dias

Sendo assim, se a empresa tiver uma negociação diferenciada com a operadora da POS ou TEF (por exemplo, antecipação de recebíveis), ela deverá ser configurada nos campos Vencimento e Tipo de Vencimento.

Informe no campo **"Qtd. parcelas"** a quantidade de parcelas a serem utilizadas nas transações com Cartão de Crédito e Cartão de Débito nas operações da TEF AUTTAR.

Caso a marcação **"Receber antes de aprovar a nota"** esteja realizada, na concretização de uma venda via Cartão de Crédito e Cartão de Débito, será possível proceder com a confirmação da nota somente após a finalização (aprovação) da operação do Cartão.

Ainda sobre a marcação acima, tem-se as seguintes observações:

- A Compensação de crédito com tipo de título configurado para Receber antes de aprovar a nota, só será realizada pelo sistema após a aprovação da nota na SEFAZ.
- No caso do recebimento por TEF, se o tipo de título for configurado para Receber antes de aprovar a nota, não haverá compensação de crédito.

Quando se tratar do lançamento de um pedido/nota de venda que contenha parcelamento, caso a divisão das parcelas apresente uma sobra, a prática normal do mercado é sempre jogar o arredondamento para a última parcela. Sendo que, algumas administradoras de crédito não trabalham desta forma, jogando assim o arredondamento para a primeira parcela. Deste modo, a marcação **"Ajusta arredondamento na 1ª parcela"**quando acionada, efetuará o arredondamento desta sobra na 1ª parcela. Caso a marcação esteja desabilitada, o arredondamento será efetuado na última parcela.

**Observação:** esta marcação propicia uma maior precisão na conciliação das transações, pelo fato de realizar a eliminação das diferenças de centavos.

Quando a marcação **"Truncar valores no parcelamento"** estiver habilitada, fará com que o sistema realize uma operação de **"Truncate"** (corte) no valor da parcela após realizar a divisão. Se estiver desligada, o sistema efetuará um **"Round"** (arredondamento) no valor da parcela. Abaixo temos um exemplo:

O valor de R$ 8.77 em 8x é igual 8.77 / 8 = 1.09625;

Com a marcação acionada, a parcela ficará em 1.09 e o parcelamento será 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.09, 1.14.
Se estiver desligada, a parcela será 1.10 e o parcelamento ficará 1.10, 1.10, 1.10, 1.10, 1.10, 1.10, 1.10, 1.07.

**Nota:** esta marcação trabalhará juntamente com a marcação Ajusta arredondamento na 1ª parcela. Desta forma, será possível escolher 4 tipos diferentes de configurações:

1.Arredondar jogando a diferença na última parcela;

2.Arredondar jogando a diferença na primeira parcela;

3.Cortar jogando a diferença na última parcela;

4.Cortar jogando a diferença na primeira parcela.

A marcação **"Tip. título cartão principal PDV Web"** só poderá ser habilitada quando a marcação **"Informar NSU opcional"** (aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral)) estiver desativada, pois, ela visa definir o título a ser apresentado nas opções de recebimento no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web). Além disso, só poderá ser usada em um único Tipo de Título em cada subtipo, por exemplo:

- Para o Subtipo configurado como Cartão de Crédito com a marcação **"Utiliza POS"** ativada, somente um Tipo de Título poderá ser marcado;
- Para o Subtipo  configurado como Cartão de Débito somente um Tipo de Título poderá ser marcado;
- Para o Subtipo configurado como Cartão de Débito com a marcação Utiliza POS somente um Tipo de Título poderá ser marcado.

Ao efetuar a marcação em mais de um título com o mesmo subtipo, e será exibida a seguinte mensagem de alerta:

**"Erro de validação.**

**A marcação "Tip. título cartão principal PDV Web" poderá ser selecionada em um único Tipo de Título em cada Subtipo."**

Desse modo, se a marcação Tip. título cartão principal PDV Web estiver habilitada, o campo Qde de Parcelas Máximas será apresentado com a informação do número máximo de parcelamento permitido em transações com cartão de crédito.

Além disso, ao acionar as duas marcações acima, o sistema ainda exibirá o campo **"Valor de parcela mínima para cartões"** que irá limitar o valor mínimo a ser recebido em cada parcela com vendas em cartões, ou em recebimentos em que a parcela seja maior que uma.

Caso a marcação Tip. título cartão principal PDV Web esteja habilitada no momento do recebimento, serão disponibilizados somente os tipos de títulos com a marcação listada nas opções de recebimento na tela do [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

Serão permitidas somente uma marcação para cada Tipo de Título único TEF e POS, por exemplo:

- **Cartão de Crédito TEF;**
- **Cartão de Crédito POS.**

Caso esta marcação não seja configurada, todos os tipos de títulos serão listados no momento do recebimento no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web).

Portanto, os tipos de títulos com a marcação Tip. título cartão principal PDV Web deverão ser informados nas seguintes opções.

- **Limite máximo de parcelas:** configurando o campo **“Quantidade de parcela mínima para cartões”** da tela Tipos de Título, aba [Preferências de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abaprefernciasdecarto) com qualquer número maior que 1, quando a quantidade de parcelas for superior ao valor máximo cadastrado, então uma mensagem de alerta aparecerá:

**“Qde de parcela não permitida.**

**Verifique a Qtde de parcelas máximas configurada em Tipo de Títulos>>Preferências de Cartões>>Qtde Máxima de Parcelas”**

- **Valor de parcela mínima:** ao configurar o campo **"Valor de parcela mínima para cartões"** com um valor maior que 1, o sistema irá validar se o valor de cada parcela é inferior ao mínimo definido. Se for, a seguinte mensagem de alerta será exibida:

**“Valor da parcela mínima de parcelamento inferior ao valor permitido.”**

Essa validação é aplicada apenas a recebimentos com **mais de uma parcela**. O valor não é validado quando a transação possui apenas uma parcela, o que permite o lançamento mesmo que o valor seja menor que o mínimo configurado.

**Cadastro de Bandeiras de Redes.**

Ao receber uma venda em cartão por meio de TEF ou POS, criando o movimento financeiro referente a este recebimento, o sistema buscará o tipo de título cadastrado correspondente a este feito, no entanto, caso não encontre o tipo de título correspondente,  ela será criada utilizando o tipo de título cuja marcação **“Tip. título cartão principal PDV Web”** estiver ativa.

**(1)** Quando configurado na Aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) os campos:

- Forma de Pagamento TEF ou Bandeiras: identificadores que representam as empresas emissoras de cartões e tem o papel de facilitar as transações financeiras junto aos bancos;
- % taxa Administradora: taxa negociada junto a Administradora de cartões a serem descontadas em cada transação;
- Parc. Administradora: o cadastro do Parc. Administrador deverá ser informado a fim de identificar o Parceiro responsável por intermediar as transações realizadas em cartões entre as instituições financeiras.

**(1)**Serão apresentadas automaticamente as informações de Rede e Bandeira, somente as opções estiverem previamente cadastradas nos Tipos de Títulos, no entanto, caso não tenha cadastrado nenhuma, será possível realizar a inserção manual desses dados diretamente no movimento financeiro.

Dessa forma, uma observação no campo **“Histórico”**, da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela) ficará visível contendo a seguinte descrição:

**“Título com rede X e bandeira Y e quantidade de parcelas Z não encontrada, faça o cadastro para a identificação correta ao receber no PDV."**

**Nota:** identificando o erro na identificação de bandeiras e taxas poderá ser feita a alteração diretamente no movimento financeiro.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Botões do topo da tela

Na parte superior da tela, teremos o botão ![Imagem 13: Na parte superior da tela, teremos o botão "Sankhya Place" , em que, ao clicar neste, o sistema o redirecionará para a…](https://ajuda.sankhya.com.br/hc/article_attachments/16584102540183) **"Sankhya Place"**, em que, ao clicar neste, o sistema o redirecionará para a tela Sankhya Place, em que exibirá conteúdos e soluções referentes ao conteúdo em que a tela estará inserido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)

## Parâmetros que influenciam nessa tela

**Calcular multa e juros pelo tipo de título? - RENEGTIPTIT:** quando este parâmetro está desligado, a aba de Renegociação não aparece na tela.

**Usar % e Vlr Custo Variável do cad.de Tip.Títulos? - GOL-CVTIT:** desabilitando este parâmetro não serão exibidos os campos % custo variável e Valor custo variável na aba Geral.

**Prazo a utilizar na geração do financeiro - TIPOPRAZO:** quando o parâmetro estiver configurado como **"Tipo de Título"**, o Fast Service buscará no campo **"Subtipo"** as informações para compor o financeiro da venda do cupom fiscal.

A máscara para o **"Plano de Contas"** será configurada através do parâmetro **"Máscara para Plano de Contas - MASCPLANCTA"**. Para criá-lo na base de dados, deve-se observar o seguinte script: INSERT INTO TSIPAR (CHAVE, DESCRICAO, CODUSU, TIPO, MODULO, CLASSE, ABA, LOGICO, INTEIRO, TEXTO) VALUES ('MASCPLANCTA', 'Máscara para Plano de Contas', 0, 'T', 'B', 'Diversas', 'Diversas', 'S', 0, '9\.9\.9\.99\.99999;1').

Quando o parâmetro **"Altera tipo de título em Títulos baixados? - ALTERATIPTIT"**estiver habilitado, será possível realizar a alteração do Tipo de Título em títulos já baixados. Caso esteja desativado, ao tentar modificar o Tipo de Título em um título já baixado, será apresentada a seguinte mensagem e tal procedimento não será concluído:

**"O campo "CODTIPTIT" não pode ser alterado em títulos baixados!"**

Ao ligar o parâmetro **"Utilizar o parc. administradora no financeiro TEF? - USARPARCADMFIN"**, o parceiro informado no campo **"Parc. Administradora"** será utilizado no campo **"Parceiro"** da tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) para os tipos de recebimento **"Cartão de Crédito"** ou **"Cartão POS"** forem usados no [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/sections/360009668474-Sankhya-Checkout).

**Usa recebimento com cartão (CTFClient)? - USARECEBCARTCTF:** quando o referido parâmetro estiver habilitado caracterizará o uso do parceiro cadastrado nos recebimentos na [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#top)
