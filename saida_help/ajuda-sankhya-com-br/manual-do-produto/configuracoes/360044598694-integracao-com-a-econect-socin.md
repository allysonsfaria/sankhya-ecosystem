---
id: "360044598694"
titulo: "Integração com a EConect-SOCIN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:48:01Z"
rotulos: ["Produtos", "Configuração", "Concentrador", "Corban", "EConect", "MGEIntegraEconect", "PDV", "Reprocessamento", "SOCIN", "Integração com a EConect-SOCIN manual", "TEF", "Integração", "Vendas"]
---

# Integração com a EConect-SOCIN

O Sankhya Om conta com todos os cadastros referentes à integração com a SOCIN. Esta integração visa disponibilizar às empresas uma solução que atenda a necessidade de um ponto de venda off-line realizando a integração de cadastros e vendas com o software de retaguarda, onde tem-se como público alvo, Supermercados e afins. Para utilização destes recursos, é necessário que a empresa possua em sua licença o opcional **"30676 - Integração com EConect-SOCIN"**.

Os link's abaixo disponibilizam os detalhes do comportamento no Sankhya-W, MGE, Concentrador, PDV, TEF, entre outros aspectos:

[Requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#requisitos)                                                                     [Restrições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#restries)

[Modelo da Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#modelodaintegrao)

Esta integração irá refletir em algumas telas do sistema (Sankhya-W). A saber:

[Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cadastrodeusurios)                                                 [Tabelas de Preços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#tabelasdepreos)

[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cadastrodeprodutos)                                                [Formação de Kit - Cesta Básica](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#formaodekit-cestabsica)

[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#prefernciasdaempresa)                                          [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cadastrodetiposdettulo) 

[Parceiros - Convênios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#parceiros-convnios)                                                [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cadastrodeparceiros)

[Configurações de Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraesdepreferncias)                                [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cadastrodetiposdenegociao)

[Pré-Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#pr-venda)                                                                    [Devolução](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#devoluo)

[Importação com diferentes parametrizações nos Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#importaocomdiferentesparametrizaesnostiposdettulo)

Para o Sankhya-W integrar as movimentações originadas da SOCIN, faz-se necessário a utilização do **"MGEIntegraEconect"** (executável em Delphi) onde será disponibilizado o menu **"Conexão > Integração com EConect"** com as funcionalidades acessadas nos link's abaixo:

[Conexão > Int. EConect > Config. para Importação do EConect](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#conexointegraocomeconectconfiguraoparaimportaodoeconect)

[Conexão > Int. EConect > Promoção EConect SOCIN](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#conexointegraocomeconectpromooeconectsocin)

[Conexão > Int. EConect > Agendador para Integração EConect](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#conexointegraocomeconectagendadorparaintegraoeconect)

**Concentrador | PDV | TEF | Corban | Reprocessamento:**

[Instalação do Concentrador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#instalaodoconcentrador)                                       [Configurações do Concentrador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraesdoconcentrador)

[Instalação do PDV](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#instalaodopdv)                                                        [Configuração TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraotef)

[Configuração da loja](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraodaloja)                                                    [Configuração das finalizadoras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraodasfinalizadoras)

[Configuração das finalizadoras por loja](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraodasfinalizadorasporloja)                    [Configuração do ponto de venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraodopontodevenda)

[Configuração da exp. e imp. de arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#configuraodaexportaoeimportaodearquivos)                  [Cat52 ECF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#cat52ecf)

[Agendamento de Carga](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#agendamentodecarga)                                              [Log de Cupons](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#logdecupons-devolues-maparesumo-clienteseconvnios)     

[Movimento Corban](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#movimentocorban)                                                      [Reprocessamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#reprocessamento) 

[Regras para aplicação do Reprocessamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#regrasparaaplicaodoreprocessamento)          [Transferência de valores (Troco)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#transfernciadevalorestroco)

## Requisitos

Esta integração possui alguns requisitos, divididos entre funcionais e não funcionais. Vejamos:

**Requisitos funcionais**

- Emissão de cupons fiscais em ECF;
- Emissão de NFC-e;
- Emissão de SAT (SP);
- Integração com vários modelos impressoras (ECF);
- Tabela de Preços única por loja;
- Consulta de Preços;
- Produtos com controles extras (cores, tamanhos, locais etc);
- Devolução Total ou Troca de produtos (cupom já fechado);
- Cancelar Item;
- Cancelar Cupom;
- Controlar Promoção Quantitativa;
- Controlar Promoção Casada (vende produto A e ganha produto B);
- Controlar crédito de Convênio/Conveniado;
- Imagem de logomarca da empresa na tela de vendas;
- Integração com balanças;
- Transferência eletrônica de fundos (TEF sobre IP / Dedicado);
- Recebimentos em múltiplos cartões;
- Abertura e fechamento de caixas;
- Conferência de caixa (Batimento de caixa);
- Leituras X;
- Reduções Z;
- Sangria e suprimento de caixas;
- Recebimento em múltiplas espécies (Dinheiro, cartão, Cheque);
- Leitura de produtos por códigos de barras;
- Senha para cancelamentos de cupom / item;
- Senha de desconto cupom / item;
- Nota fiscal paulista;
- Registrar o vendedor por item;
- Controle de licença.

**Requisitos não funcionais**

- Disponibilidade 24x7;
- Registro do item no cupom em um segundo;
- Instalação por base template do concentrador;
- Atualização automática do PDV pelo concentrador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Restrições

A Integração com a EConect - SOCIN possui algumas restrições, ou seja, processos que não são possíveis de serem executados.

- Não trabalha com múltiplas Tabelas de Preços;
- Não trabalha com valores no campo "taxa/desconto" do Tipo de Negociação;
- Não trabalha com imagens no Cadastro de Produtos;
- Não trabalha com cadastros de clientes no PDV;
- Não trabalha com validações do varejo ativada (crédito, atraso, desconto, estoque);
- Não trabalha com DAV;
- Não trabalha com pay&go;
- Não importa fechamento de caixa - O fechamento de caixa será conciliado através do financeiro Sankhya e o relatório Batimento de Caixa Socin.

**Observação:** nesse caso, pode-se adotar a solução Gsurf ou Lira; é preciso negociar valores com a empresa para substituição da solução de TEF.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Modelo da Integração

A Integração com a EConect - SOCIN tratará as seguintes funcionalidades:

- Exportação de Dados para PDV;
- Usuários;
- Produtos com Alíquota e preço;
- Variações do controle de estoque;
- Promoções;
- Vendedores;
- Pré-Venda;
- Convênios;
- Importação de Dados do PDV;
- Vendas;
- Reduções Z;
- Cancelamentos;
- Troca de produtos (devoluções);
- Recebimentos com TEF para posterior conciliação;
- Reprocessamento;
- Informações do SPED.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cadastro de Usuários

Na aba **"Identificação"**, tem-se a seção Integrar EConect:

![Imagem 1: Na aba "Identificação" , tem-se a seção Integrar EConect:](https://ajuda.sankhya.com.br/hc/article_attachments/9198676797719)

**Integrar com EConect:** Esta marcação quando realizada, tem-se que o usuário em questão poderá trabalhar com o EConect.

**Senha:** Informa-se neste campo a senha de acesso ao EConect, senha esta, que deve ser composta apenas por números.

**Cód. Ident.:** Este campo deve ser preenchido com o Código Identificador (formado apenas por números) do usuário em questão no EConect.

**Cód. Perfil:** Informa-se aqui o código referente perfil do usuário; pode-se inserir mais de um código neste campo, desde que estes sejam separados por vírgula e sejam diferentes de "0" (zero).

O campo **"Empresa"**, também presente na aba Identificação, se tornará de preenchimento obrigatório, caso o campo **"Integrar com EConect"** esteja marcado para identificar quais lojas o usuário poderá efetuar movimentações.

**Botão Outras Opções**

O botão **"Outras Opções"** permite a configuração da funcionalidade de Sangria (retirada parcial de um valor) ou Suprimento (inserção de um valor que não corresponde a uma venda) no caixa da empresa. Acionando-se a opção **"Configurações do Usuário"** presente no botão **"Outras Opções"** é exibido o pop-up **"Configurações Usuário"**, o campo **"Conta para sangria/Suprimento"** tem a finalidade de apontar a conta que será utilizada para realização do procedimento de Sangria/Suprimento.

![Imagem 2: O botão "Outras Opções" permite a configuração da funcionalidade de Sangria (retirada parcial de um valor) ou…](https://ajuda.sankhya.com.br/hc/article_attachments/9198720513175)

A partir dessas configurações, as movimentações de Sangria/Suprimento serão importadas para o ERP Sankhya.

A data a qual se iniciará a execução do referido processo na instituição será indicada no parâmetro **"Data de Início Sangria/Suprimento - DTINISANSUPECON"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Tabelas de Preços

![Imagem 3: Tabelas de Preços](https://ajuda.sankhya.com.br/hc/article_attachments/9198992866583)

Na configuração das Tabelas de Preços, deve-se atentar para:

**Integrar com EConect:** Esta marcação quando realizada, implica que a tabela de preços em questão realizará integração com o EConect.

Realizando-se a marcação anterior, o campo **"Observação"** poderá ser preenchido com um máximo de 20 caracteres.

Além disso, a marcação Integrar com EConect não poderá ser realizada quando a tabela em questão for a **"Tabela 0"** (zero).

Na configuração dos Produtos na Tabela de Preços (aba Exceções), o único registro aceito pela integração no campo **"Tipo"** será a opção **"Valor"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cadastro de Produtos

![Imagem 4: Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/9198997277975)

Na aba **"Venda"**, seção **"Integrar EConect"** tem-se a marcação **"Integrar com EConect"** que ao ser realizada, o produto em questão realizará integração com o EConect.

No campo **"Máx. Multiplicador"** informa-se a quantidade máxima que o produto selecionado pode ser vendido.

Com a marcação Integrar com EConect realizada, alguns campos no sistema passam a ser de preenchimento obrigatório; são eles:

**Aba Geral**

- Grupo;
- Referência (na integração não serão aceitos Códigos de Barras repetidos);
- Origem do produto;
- NCM;
- Usado como (produtos utilizados como **"Matéria-Prima"** e **"Revenda (por Fórmula)"** não podem ser utilizados na integração);

**Aba Impostos**

- % Carga Média Trib. Nacional;
- % Carga Média Trib. Federal;
- % Carga Média Trib. Estadual;
- % Carga Média Trib. Importação.

**Aba Impostos/Informações por empresa**

- Alíquota ICMS do EConect;

Caso as abas **"Código de Barras"** ou **"Unidades Alternativas"** contenham informações, o campo Código de Barras nelas presente, será também de preenchimento obrigatório.

O código de barras do produto pode também ser preenchido na aba **"Código de Barras"** como dito anteriormente, porém, a prioridade para importação será caso esteja preenchido no campo **"Referência"** da aba Geral. O objetivo desta tabela é identificar o código de barras para venda do produto.  

No caso da Unidade Principal, basta estar cadastrado com a marcação **"Integrar com Econect"** e possuir o **"Cód. Barras"** preenchido. Já para as Unidades Alternativas do produto, para que o código de barras seja importado para o Econect, é necessário que o campo **"Ativo"** esteja marcado, o Cód. Barras esteja preenchido e a **"Quantidade"** seja maior que **"0"** (zero).

**Observação:** os CFOP's que participarão da Integração com SOCIN são: 5101, 5102, 5115, 5401 e 5405.

As regras para definição do CFOP do produto são:

- Caso Parceiro Consignante esteja preenchido, o CFOP será 5115;

Sendo produto próprio:

- Tem ST, o CFOP será 5401;
- Não tem ST, o CFOP será 5101.

Se o produto for de terceiros:

- Tem ST, o CFOP será 5405;
- Não tem ST, o CFOP será 5102.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Formação de Kit - Cesta Básica

Para a montagem de Kit's (Cesta Básica), deve-se seguir os seguintes passos:

1.Habilita-se o parâmetro **"Informar Preço p/Componente no cad.Produto? - PRECOKIT"**;

2.Na alteração/inclusão dos Componentes, o produto Cesta Básica deverá estar com a opção **"Integrar com Econect"** desmarcada;

3.Deve-se selecionar os produtos que farão parte da Cesta Básica. Todos os produtos selecionados como componentes da Cesta Básica deverão estar marcados como **"Ativos"** e **"Integrar com Econect"**. Os produtos também deverão possuir tabela de preços cadastrada, onde a mesma também deverá estar marcada "Integrar com Econect". Todos os produtos da Cesta deverão dispor das mesmas configurações de um produto normal que é integrado com SOCIN;

4.Caso o produto na Cesta tenha um preço diferenciado do preço de venda unitário, deve-se preencher os campos **"Preço"** ou **"Desconto"** da aba **"Componentes"**;

5.Após finalizar a montagem da Cesta, a mesma deverá ter a marcação "Integrar com Econect" realizada. Caso exista algum erro de configuração em algum componente da Cesta, o sistema emitirá uma mensagem de alerta, para que seja feita a devida correção para a importação do produto;

6.Para que a Cesta seja enviada para o PDV, a integração deverá ser executada.

É importante mencionar que, para produtos que utilizam balança (horti-fruti por exemplo), a opção **"Utilizar Balança"** deverá ser marcada (Aba Medidas e Estoque, sub-aba Estoque).

Para produtos fracionáveis, a opção **"Decimais para quantidade"** (Aba Medidas e Estoque, sub-aba Medidas) deverá ser maior que **"0"** (zero).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Preferências da Empresa

Na configuração das preferências da empresa, tem-se a seção **"Integrar EConect"**:

![Imagem 5: Na configuração das preferências da empresa, tem-se a seção "Integrar EConect" :](https://ajuda.sankhya.com.br/hc/article_attachments/9199256871831)

**Loja na Integração EConect:** Através deste campo, realiza-se o "DE-PARA" entre o código da loja cadastrado no EConect e a empresa cadastrada no Sankhya-W. Este código deverá ser configurado de acordo com a Loja cadastrada no EConect. No momento da importação de cupom fiscal, finalizadora, financeiro etc, o sistema verificará a configuração deste campo para realizar o DE-PARA e importar a movimentação para a empresa correta.

O usuário utilizador da integração realiza as vendas no PDV (SOCIN), logo a SOCIN possui a responsabilidade de exportar para a base comum os registros referentes à venda realizada. Para a integração, tem-se 3 tipos de vendas:

- Cupom Fiscal (sempre será importado com série fixa 'CF');
- NFC-e (importado com a série de acordo com a disponibilização pela SOCIN);
- SAT (SP) (a série será de acordo com a configuração "Controle de Numeração" da TOP).

Os Tipos de Operação ligados à recarda de celular e às operações citadas, são informados nos campos **"TOP recarga celular EConect"**, **"TOP para NFC-e"** e **"TOP para SAT"**.

O Cupom Fiscal é um documento fiscal equivalente à nota fiscal, diferenciando-se desta por ter que ser emitido por impressora fiscal. As tabelas que são preenchidas na emissão do Cupom fiscal são:

- TB\_BDC\_CAPA\_CUPOM
- TB\_BDC\_DETALHE\_CUPOM

A NFC-e é um documento fiscal eletrônico, transmitido pelo estabelecimento comercial para a SEFAZ pela internet no ato da compra. Como a nota é autorizada de forma online pela SEFAZ e armazenada nos computadores da Secretaria, o consumidor conta com mais segurança e comodidade recebendo diretamente o documento em seu e-mail sem necessidade de impressão. As tabelas preenchidas na emissão na NFC-e são:

- TB\_BDC\_MOV\_NFC
- TB\_BDC\_CAPA\_CUPOM
- TB\_BDC\_DETALHE\_CUPOM

O SAT-CF-e (Sistema Autenticador e Transmissor de Cupons Fiscais Eletrônicos) documenta de forma eletrônica, as operações comerciais do varejo dos contribuintes do Estado de São Paulo, em substituição aos atuais equipamentos ECF (Emissor de Cupom Fiscal). As tabelas preenchidas na emissão do SAT(SP) são:

TB\_BDC\_MOV\_SAT

TB\_BDC\_CAPA\_CUPOM

TB\_BDC\_DETALHE\_CUPOM

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cadastro de Tipos de Título

Na configuração dos Tipos de Título, tem-se a seção **"Integrar EConect"**:

![Imagem 6: Na configuração dos Tipos de Título, tem-se a seção "Integrar EConect" :](https://ajuda.sankhya.com.br/hc/article_attachments/9199328676503)

**Integrar com Econect:** Quando marcado, tem-se que o tipo de título em questão realizará integração com o EConect.

**Cód. Finalizadora:** Campo de preenchimento obrigatório, caso a finalizadora seja diferente de cartão de crédito.

**Grupo Finalizadora:** De preenchimento obrigatório, caso na SOCIN seja cadastrado um grupo de finalizadora dentro de uma finalizadora pai.

**Bandeira Cartão:** Esta informação é de preenchimento obrigatório, caso a finalizadora seja Cartão de Crédito ou Débito. Este campo realizará o DE-PARA com o código da administradora de cartão de crédito. Pode-se cadastrar uma ou mais bandeiras de cartão para o mesmo Tipo de Título, sendo seu separador a vírgula **","**. Por exemplo 3,10,2001.

**Convênio:** Efetua-se esta marcação, caso o tipo de finalizadora no EConect seja Convênio empresa ou Convênio Cliente, pois ambos possuem controle de saldo. Pode-se obter maiores informações sobre os dois tipos de convênios ao final deste tópico.

Vejamos abaixo os códigos das bandeiras padrões:

**Crédito:**

|  | ![Imagem 7: Crédito :](https://ajuda.sankhya.com.br/hc/article_attachments/42310668201495) |  |
| --- | --- | --- |

**Débito:**

|  | ![Imagem 8: Débito :](https://ajuda.sankhya.com.br/hc/article_attachments/42310672415383) |  |
| --- | --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Importação com diferentes parametrizações nos Tipos de Título

Caso seja necessário cadastrar diferentes informações para cada Tipo de Título (Banco, Centro de Resultado, Natureza, Baixa Automática), pode-se utilizar do seguinte recurso:

1.Cadastrar uma negociação mista (Forma Recebto = -1);

2.Nas parcelas, cadastrar cada tipo de título com a sua respectiva característica (Banco, Centro de Resultado, Natureza). Lembrando que os tipos de títulos configurados deverão ter em seu cadastro a marcação **"Integrar com Econect"** realizada;

3.Habilitar o parâmetro **"Usa config. parcela negegocição mista EConect? - TTNEGMISECONECT"**.

Ao realizar a importação, o sistema irá verificar qual Tipo de Título está sendo utilizado e se no Tipo de Negociação misto possui esse tipo de título configurado. Se houver, será realizada a importação considerando as características específicas deste tipo de título.

**Nota:** na configuração cujo parâmetro de chave TTNEGMISECONECT está ligado, serão considerados apenas os tipos de título na aba parcelas da forma de recebimento mista -1. Todos os outros tipos de títulos configurados serão desconsiderados mesmo eles tendo a marcação **"IntegraEconect"** efetuada, não estando configurados na aba Parcelas do tipo de negociação -1.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cadastro de Parceiros

![Imagem 9: Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/9213356488087)

Na seção **"Integrar EConect"** presente na aba **"Crédito"** tem-se:

**Integração  Econect:** Quando marcado, tem-se que o parceiro em questão realizará integração com o EConect.

**Senha:** Informa-se neste campo de preenchimento obrigatório, a senha composta por números, para que ocorra a integração com o EConect.

Nos campos abaixo, utiliza-se ou Prazo ou Parcelamento:

**Prazos:** Informa-se aqui, o prazo para a fatura do cliente ser enviada (30,60,90 dias por exemplo).

**Partir de:** Define-se quando começará a contar o prazo da fatura. Tem-se as seguintes opções:

- Não se aplica
- Fora Mês
- Próximo dia útil
- Fora Semana
- Fora Dezena
- Fora Quinzena
- Fora Mês

**Parcelamentos:** Informa-se aqui, a quantidade de Parcelas que será quebrada a fatura.

**Partir de:** Determina-se quando o parcelamento das faturas terá início. As opções disponíveis são as mesmas para o campo Prazo.

**Dia Fechamento:** Neste campo, informa-se o dia de fechamento da fatura.

**Dia Pagamento:** Tem-se aqui, o dia de pagamento da fatura.

**Perfil:** Determina-se aqui, o perfil do cliente para a compra. Tem-se as seguintes opções:

- Pode ultrapassar limite;
- Somente até limite;
- Cliente sem limite.

Caso o limite do cliente seja extrapolado, esta opção irá determinar se ele pode continuar comprando ou não mesmo não possuindo crédito. Essa opção depende do relacionamento com o estabelecimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Parceiros - Convênios

O convênio de cliente parte do princípio da liberação de um crédito para o cliente consumir e pagar posteriormente, seja em boleto, em débito automático etc.

Na Integração Sankhya-Socin, trata-se dois tipos de convênios. São eles:

- Cliente;
- Conveniado.

Vejamos sobre eles:

**Cliente:**

O convênio de cliente parte do principio da liberação de um crédito para o cliente consumir e pagar posteriormente, seja em boleto, em débito automático etc.

Para cadastrar um convênio cliente, deve-se acessar a tela **"Configurações > Cadastros > Parceiros"** e realizar as seguintes configurações:

#### Aba Identificação

- Marcar a opção "Cliente";
- Informa-se a Razão Social do Parceiro;
- Campo "Convênio" onde é inserido o próprio código do parceiro;
- Inserir um CPF ou CNPJ válido (dependendo do tipo de pessoa);
- Informar a "Identidade" ou "Inscrição Estadual" (dependendo do tipo de pessoa).

#### Aba Endereço

- Cadastrar Endereço;
- Número;
- Bairro;
- Cidade;
- CEP;
- Telefone.

#### Aba Crédito

- Configurar Tabela de Preços (esta deverá possuir marcação integra EConect);
- Configurar Limite de crédito;
- Marcação "Integração Econect" realizada;
- Preencher a Senha (apenas números);
- Preencher Prazo de Parcelamento (separador será a Vírgula ",");
- Preencher Partir de;
- Preencher dia de fechamento e Pagamento;
- Preencher Perfil.

Ao confirmar, os registros estarão disponibilizados para a venda ONLINE do convênio cliente. Para disponibilizar os registros para venda OFFLINE do convênio, deve-se acessar na Integração E-conect (Conexão > Integração com SOCIN > Agendador para Integração ) e enviar as cargas para as lojas.

#### Empresa Convênio

A empresa convênio será uma empresa cadastrada no sistema onde o seu limite será distribuído entre todos os conveniados amarrados à ela.

Para cadastrar uma empresa convênio, deve-se acessar a tela **"Configurações > Cadastros > Parceiros"** e realizar as configurações semelhantes a do cliente, porém com algumas diferenças. São elas:

O limite cadastrado na aba Crédito será liberado para a empresa. Por exemplo, R$5.000,00. Esse valor será distribuído para todos os conveniados atrelados a esta empresa. Caso seja feita a tentativa de cadastrar conveniados para essa empresa cujo somatório dos limites ultrapasse o limite da empresa, o Sankhya-W irá barrar a operação.

Para a empresa convênio, a marcação **"Integração Econect"** não deverá estar realizada. Neste caso, os conveniados vinculados a essa empresa deverão ter esta marcação ativa. Desta forma, o sistema entenderá que este cadastro é uma empresa e os amarrados à ela são conveniados e que os limites da empresa deverão ser respeitados.

#### Conveniado

O conveniado é um parceiro atrelado à uma empresa (empresa convênio) e seu limite deverá respeitar o limite da empresa.

Para cadastrar um conveniado, a operação é semelhante ao cadastro dos clientes. A única diferença é que, é necessário ter-se uma Empresa Convênio cadastrada, e no campo **"Convênio"**, ao invés de informar-se o próprio **"Código do Parceiro"** vinculado, deve-se vincular o Código da **"Empresa Convênio"**.

Uma empresa pode possuir vários conveniados, sendo a sua única restrição que a soma dos limites dos conveniados não ultrapasse o limite estipulado na empresa convênio.

#### Dependentes

Além das configurações mencionadas até aqui, no sistema, tem-se a possibilidade de cadastrar **"Dependentes"** tanto para o cliente, quanto para o conveniado da empresa.

A configuração para ambos os dependentes será a mesma, diferenciando-se no ponto em que estando em um cliente ou em um conveniado (vide itens anteriores), o limite que os dependentes irão consumir será do cliente ou do conveniado a que estão vinculados.

Para cadastrar um "dependente", basta informá-lo na aba **"Contatos"** da tela **"Configurações > Cadastros > Parceiros"**.

As configurações abaixo deverão ser respeitadas para que o sistema considere um contato como **"Dependente"**:

- Informar o nome do Contato;
- Inserir no Cargo a informação **"DEPENDENTE"** (deve-se cadastrar este cargo desta maneira, ou seja, todo o nome em maiúsculo);
- Informar um CPF válido;
- Inserir uma senha (composta apenas de números);

#### Saldo Cliente/Convênio Acumulado

Após a inserção dos registros no Sankhya-W, o PDV da SOCIN conseguirá realizar vendas com cliente, convênio e dependentes. Desta forma, o acumulado do parceiro vinculado ao cupom será adicionado ao valor de cada venda. Será de responsabilidade do backoffice (setor administrativo/financeiro da empresa) realizar as baixas dos financeiros que foram pagos pelos clientes, convênios e dependentes.

Desta forma, o back-office deverá acessar a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira), filtrar os títulos em aberto para aquele cliente e realizar as baixas de acordo com os títulos que foram pagos.

Para verificar o acumulado do cliente/empresa no Sankhya-W, basta acessar a [Ficha de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025233894-Ficha-de-Parceiros). Uma vez configurado o usuário, clica-se na opção Cadastro, e na aba Crédito será demonstrado o campo Total Pendente, que será o acumulado daquele parceiro. Caso o campo esteja vazio, significa que o valor acumulado é zero "0".

**Observações:**

- Em uma venda com mais de um convênio, o último convênio digitado sairá no cabeçalho da nota;
- Para vendas com mais de um cliente, o último cliente digitado será exibido no cabeçalho da nota;
- Para vendas "Mistas" com convênio e cliente, o último convênio digitado sairá no cabeçalho da nota.

#### Detalhes de importação de cupons

- Para venda com mais de um convênio, o último convênio digitado sairá no cabeçalho da nota;
- Para venda com mais de um cliente, o último cliente digitado será apresentado no cabeçalho da nota;
- Para venda Mista com convênio e cliente, o último convênio digitado sairá no cabeçalho da nota.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cadastro de Tipos de Negociação

![Imagem 10: Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/9213393730327)

Na seção **"Integrar EConect"** presente na aba **"Características"** tem-se:

**Integrar com Econect:** Quando marcado, tem-se que o tipo de negociação em questão realizará integração com o EConect.

**Forma Recebto:** Informação de preenchimento obrigatório, este campo realizará o DE-PARA das formas de recebimento existentes no sistema da SOCIN com o Sankhya-W.

**Notas:**

- Para cupons que existem mais uma forma de pagamento, deve-se cadastrar o tipo de negociação **"MISTO"** e no campo Forma Recebto informa-se **"-1"** para que o sistema reconheça esta situação no momento da importação.
- Para os tipos de negociação utilizados em cliente e convênio, o campo **"Subtipo"** deverá ser diferente de **"Cartão de Crédito"**. Como sugestão, deverá ser cadastrado como **"A prazo"** ou **"Parcelado"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configurações de Preferências

Existem alguns parâmetros do sistema que participam da integração SOCIN; são eles:

**Código do Pai da Sessão SOCIN Econect - CODSECPAISOCIN:** Este parâmetro deverá ser preenchido para formar o nível do produto. Por padrão, sempre preenche-se este parâmetro com **"1"**.

**Empresa padrão para Integração Econect - CODEMPPDECONECT:** Este parâmetro deverá ser preenchido para identificar a empresa padrão que o sistema irá trabalhar. Por padrão, preenche-se este parâmetro com **"1"**.

**Nota de Devolução Modelo para Integração Econect. - NOTADEVOLSOCIN:** Este parâmetro deverá ser preenchido com o número único da nota de devolução modelo que o sistema irá importar na devolução (cabeçalho).

**Data início integração Sangria/Suprimento EConect - DTINISANSUPECON:** Este parâmetro é utilizado para configurar a data a partir da qual serão importados os lançamentos de Sangria e Suprimento.

**Tipo de título para Troco do Econect - TIPTITTROCOECON**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Devolução

A tabela **"TB\_BDC\_TROCA\_MERCADORIA"** é preenchida conforme movimentação de Devolução proveniente do PDV SOCIN. Para que essa tabela seja preenchida, não é necessária a realização total de uma troca, apenas a devolução preenche a tabela.

Tem-se uma rotina interna no sistema que ao realizar o preenchimento da tabela mencionada, a movimentação é automaticamente alimentada na rotina de devolução do Sankhya-W com uma nota à confirmar, ficando em responsabilidade do usuário realizar a confirmação da mesma.

**Importante:** a nota utilizada como **"Modelo de devolução"** deverá ter na configuração do Tipo de Operação-TOP utilizado, na aba **"Impostos"** o campo **"Cálculo de ICMS, IPI e ISS"** definido com a opção **"Calcula na Confirmação"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Pré-Venda

Na integração Sankhya – Socin, a pré-venda pode ser lançada de duas maneiras:

1.De forma convencional, através do Concentrador no menu **"Movimento > Vendas > Pré-Venda"**;

http://www.socin.com.br/mediawiki/index.php/Pr%C3%A9\_venda

2.Através de um Pedido de Venda no Sankhya-W; para que o Pedido de Venda seja exportado como pré-venda do Sankhya-W para o sistema da SOCIN, este deverá conter:

#### Tipo de Operação > Aba Geral:

- Tipo de Movimentação **"P-Pedido de Venda"**;
- Financeiro **"Não atualizar"**;
- Atualização do Estoque **"Nenhuma"**;
- Marcação **"A nota fica como pendente"** realizada.

#### Tipo de Operação > Aba Impostos:

- Cálculo de ICMS, IPI e ISS definido como **"Não calcula e não digita"**;

No lançamento, deve-se lançar um Pedido de Venda, com a TOP cadastrada com as especificações acima citadas e a Série "PV".

**Observações:**

- Para que a Pré-Venda seja disponibilizada para a SOCIN, esta deverá ser confirmada. Ao confirmá-la, será populada a tabela **TB\_BDC\_PRE\_VENDA**;
- A Pré-venda deverá possuir no MÍNIMO 1 item;
- Na seleção do pedido de venda, caso a pré-venda ainda não tenha sido utilizada pela SOCIN, ela será apresentada como Confirmada = **"Sim"** e Pendente = **"Sim"**;
- No PDV, ao pressionar a tecla **"H",** o usuário poderá digitar o número da pré-venda. O número da pré-venda na SOCIN será o Nro Único do documento no Sankhya-W.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Conexão > Integração com EConect > Configuração para Importação do EConect

No MGE, acessa-se a tela **"Conexão > Fast Service > Configuração para Importação do E-conect"**; nesta tela, encontram-se os campos que deverão ser preenchidos para que a importação do Cupom Fiscal emitido na SOCIN seja realizada para o Sankhya-W:

![Imagem 11: No MGE, acessa-se a tela "Conexão > Fast Service > Configuração para Importação do E-conect" ; n esta tela,…](https://ajuda.sankhya.com.br/hc/article_attachments/9213396624919)

Os campos citados abaixo são de preenchimento obrigatório para que a importação do cupom fiscal emitido na Socin seja importado para o Sankhya:

#### Aba Geral

- Empresa;
- TOP;
- Parceiro;
- Série;
- Natureza;
- Centro de Resultado;
- Conta Bancária;
- Lançamento Bancário;
- Top Baixa;
- Local;
- Cód. Máquina.

#### Aba Tipo de Negociação

- Dinheiro;
- Cheque;
- Cartão de Crédito;
- Cartão de Débito;
- Lançamento bancário suprimento;
- Lançamento bancário sangria.

**Observação:** as Preferências da Empresa também conta com um campo Local para realizar-se a diferenciação de local por empresa.

Caso esteja preenchido o campo Local apenas na tela **"Configuração para Importação do E-conect"**, o cupom fiscal irá utilizar os dados do campo Local aqui informado. Caso esteja preenchido na tela Configuração para importação do E-conect e também nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), o sistema utilizará o Local Padrão EConect que foi informado nas Preferências da empresa (aba Integrar EConect).

![Imagem 12: Para empresas que utilizam o Sankhya-Om, se faz necessária a utilização do módulo "MGEIntegraEconect" para acesso à…](https://ajuda.sankhya.com.br/hc/article_attachments/16637631962519) Para empresas que utilizam o Sankhya-Om, se faz necessária a utilização do módulo **"MGEIntegraEconect"** para acesso à tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Conexão > Integração com EConect > Promoção EConect SOCIN

A tela **"Conexão > Integração com EConect > Promoção EConect SOCIN"** (localizada na linha MGE) corresponde a tabela **"TB\_BDC\_PROMOCAO"**; tem-se aqui uma tela desenvolvida exclusivamente para a integração; ela não possui a necessidade de nenhuma marcação específica. Realiza-se apenas a inserção dos registros na aplicação e isso já faz com que estes registros sejam exportados para a tabela de integração da SOCIN.

![Imagem 13: A tela "Conexão > Integração com EConect > Promoção EConect SOCIN" (localizada na linha MGE) corresponde a tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/9213400839575)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Conexão > Integração com EConect > Agendador para Integração EConect

A tela "Conexão > Integração com EConect > Agendador para Integração EConect" ao ser populada, preenche a tabela "TB\_BDCOMUM\_CONTROLE"; esta tabela é alimentada conforme solicitação do Sankhya-W para exportação dos registros para o Concentrador SOCIN.

![Imagem 14: A tela "Conexão > Integração com EConect > Agendador para Integração EConect" ao ser populada, preenche a tabela…](https://ajuda.sankhya.com.br/hc/article_attachments/9213458232087)

#### Aba Produtos

Nesta aba são definidos os Produtos que serão enviados para o EConect.

#### Aba Agendamento

Caso queira-se realizar um agendamento, basta inserir um novo registro nesta tela selecionando a periodicidade que a integração será executada. Feitos esses cadastros, deve-se acessar o módulo **"Tarefas"** e o mesmo executará a rotina agendada. Essa operação faz com que todas as informações inseridas nas tabelas anteriormente citadas, sejam enviadas para o Concentrador SOCIN.

#### Aba Conversão de unidades de venda

Esta aba tem o objetivo de realizar o DE-PARA com as unidades cadastradas no Sankhya-W e as unidades disponibilizadas pelo Econect. Atualmente no Econect são disponibilizadas as unidades **"CT", "CX", "KG", "MT", "PC", "PT" e "UN"**. Como no Sankhya-W tem-se o cadastro de unidades conforme a necessidade de cada cliente, se faz necessário realizar o DE-PARA para que os registros sejam importados em conformidade com o EConect.

Todas as cargas serão enviadas diretamente para o concentrador. Uma vez os dados no concentrador, basta que o usuário realize o agendamento da carga para seu envio aos PDV's através do Concentrador SOCIN.

No rodapé desta tela, tem-se duas marcações facilitadoras. A saber:

**Enviar todos os preços:** Este recurso visa enviar o preço de todos os produtos de uma só vez para o concentrador.

**Enviar todos os produtos:** Esta marcação tem o objetivo de enviar todos os produtos de uma só vez para o concentrador.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Instalação do Concentrador

Entendamos o Concentrador como um intermediário entre o PDV para o Sankhya-W e vice-versa; ele irá concentrar as informações. Utilizaremos um único concentrador para configurar todas as lojas e seus PDV's, sendo que uma máquina exclusiva conterá as aplicações e sistema operacional Windows em qualquer versão.

Para que não ocorra duplicidade de documentações, apresentaremos os link's da documentação oficial do portal SOCIN (copie e cole cada link desejado em seu navegador).

http://www.socin.com.br/mediawiki/index.php/Instala%C3%A7%C3%A3o\_no\_Windows

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configurações do Concentrador

Utilizaremos um único concentrador para configurar todas as lojas e seus PDV's, sendo uma máquina exclusiva que irá conter as aplicações e sistema operacional Windows em qualquer versão.

Para que o concentrador comece a receber informações referentes a automação do Sankhya-W e PDV, será necessário seguir a documentação oficial do portal da SOCIN. Para não existir duplicidade de documentações, apresentaremos a link da documentação oficial do portal SOCIN:

http://www.socin.com.br/mediawiki\_teste\_28/index.php/Instala%C3%A7%C3%A3o\_do\_Concentrador\_Web

**Usuário:** servicos.jiva

**Senha:** socin123

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Instalação do PDV

Cada PDV precisará ser uma máquina exclusiva, que conterá a aplicação do PDV o sistema operacional linux e os devices de automação comercial como impressora, leitor de código de barras e leitores de cartão.

Por ser uma máquina exclusiva, as operações destinam-se apenas às movimentações de caixa e conexão via internet com back-office para consultas e outros trabalhos.

http://www.socin.com.br/mediawiki\_teste\_28/index.php/Categoria:Instala%C3%A7%C3%A3o\_PDV

**Usuário:** servicos.jiva

**Senha:** socin123

**Nota:** tanto a instalação do concentrador, quanto dos PDV's são de total responsabilidade da SOCIN.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração TEF

Para que as finalizadoras utilizem o sistema TEF, é necessário configurar os tipos de consultas e as transações que serão realizadas para as finalizadoras que recebem tratamentos dos tipos **"Cheque"**, **"Cartão de Débito e Crédito"**.

A tela **"SITEF"** do Concentrador permite configurar os tipos de transações que serão realizadas, de acordo com os serviços de Transferência Eletrônica de Fundos (TEF) que serão utilizados para as lojas.

Forma de Acesso: Menu Configuração > Transações > SITEF

http://www.socin.com.br/mediawiki/index.php/Configura%C3%A7%C3%A3o\_SITEF

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração da loja

A tela **"Loja do Concentrador"** é utilizada para realizar configurações referentes a Loja, ou seja, como o IP, a utilização ou não de promoções, do Restaurante e outros módulos. Desta forma, é possível realizar configurações para uma loja específica ou para todas, garantindo a diferenciação nas configurações e até certo ponto, exclusividade para determinada promoção que será utilizada ou um nível de preço de produtos.

Forma de acesso: Menu Configuração > Configuração Gerais > Loja

http://www.socin.com.br/mediawiki/index.php/Loja

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração das finalizadoras

A tela **"Finalizadora do Concentrador"** permite cadastrar as finalizadoras que serão utilizadas pelas lojas.

Forma de Acesso: Menu Cadastro > Finalizadoras > Finalizadora - Sigla finalizadora (deixar 0).

Deixar a descrição da finalizadora exatamente idêntica à ECF (BemaTech)

http://www.socin.com.br/mediawiki/index.php/Cadastro\_de\_finalizadora

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração das finalizadoras por loja

A tela **"Finalizadora por Loja"** do Concentrador permite configurar as finalizadoras cadastradas no sistema para cada loja. Para configurar as finalizadoras deve-se estar acessado à loja para a qual será realizada a configuração.

Forma de Acesso: Menu Cadastro > Finalizadoras > Loja

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração do ponto de venda

Configurações dos periféricos como impressora, leitor de código de barras, teclado, balança.

Para ter acesso a tela de cadastro do PDV, deve-se acessar o seguinte caminho:

Forma de acesso: Menu Cadastro > Cadastro Loja > Ponto de venda

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Configuração da exportação e importação de arquivos

Para a configuração será necessário obter com a SOCIN os scripts mais atualizados da base comum para o banco de dados desejado, em seguida solicitar a Sankhya os scripts de integração.

De posse de todos os scripts, eles devem ser executados no banco de dados no usuário do ERP.

Para não haver duplicidade de documentações, disponibilizamos abaixo o link da documentação oficial do portal SOCIN:

http://www.socin.com.br/mediawiki\_teste\_28/index.php/Categoria:Transa%C3%A7%C3%B5es

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Cat52 ECF

A tela **"Cat52 ECF"** permite realizar os cadastros das impressoras fiscais, de modo que estas possam gerar os arquivos das Notas Fiscais Paulistas.

Forma de Acesso: Menu Cadastro > Cadastros loja > Cat52 ECF

http://www.socin.com.br/mediawiki/index.php/Cat52\_ECF

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Agendamento de Carga

A tela **"Agendamento de Carga"** permite realizar os agendamentos de envios de cargas de dados para as lojas e os PDV's da rede. O Concentrador Matriz permite agendar cargas para todos os Concentradores Lojas e seus PDV's. Assim, os sistemas são atualizados com os dados dos novos cadastros e configurações.

**Importante:** na primeira carga, sempre é necessário marcá-la como **"Total"**.

Forma de acesso: Menu Carga > Agendamento de Carga

http://www.socin.com.br/mediawiki\_teste\_28/index.php/Agendamento\_de\_carga\_autom%C3%A1tica

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## LOG de Cupons - Devoluções - Mapa Resumo - Clientes e Convênios

A tela **"Conexão > Integração com SOCIN > Log Integração EConect SOCIN"** foi desenvolvida com o intuito de mostrar aos usuários, os cupons fiscais, as devoluções, os Mapas Resumo, as movimentações de Clientes e Convênio com erro (através do filtro "Tipo de Movimento"), que não foram importados para o Sankhya-W e o porque desta não importação, para que estes sejam tratados, ou seja, reprocessados para que sejam integrados ao sistema.

O erro da importação será demonstrado no campo **"Mensagem de Erro"**:

![Imagem 15: O erro da importação será demonstrado no campo "Mensagem de Erro" :](https://ajuda.sankhya.com.br/hc/article_attachments/9213512706327)

Para reprocessar, basta selecionar um registro clicando sobre o mesmo ou selecionar todos (com o botão direito do mouse) e clicar em Reprocessar. Caso o registro seja importado com sucesso, o mesmo não voltará a ser apresentado na grade. Caso ainda ocorra algum erro de importação, o registro será demonstrado na grade novamente para que o erro possa ser tratado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Movimento Corban

O Movimento CorBan (CORrespondente BANcário) é integrado através da tabela TB\_BDC\_MOVI\_CORBAN para o ERP Sankhya.

As seguintes parametrizações serão necessárias:

1.Configuração do Parâmetro **"Data de início integração CorBan Econect - DTINICORBANECON"** com a data que o usuário deseja iniciar a importação das movimentações de CORBAN;

2.Configurar o campo **"TOP para Corban"** localizado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) com uma TOP do tipo "Financeiro".

A partir desta configuração, todas as movimentações exportadas pelo Econect para a tabela TB\_BDC\_MOVI\_CORBAN serão integradas para o ERP Sankhya.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Reprocessamento

O sistema da SOCIN conta com uma rotina de reprocessamento de movimentações. Esta rotina serve para reprocessar as movimentações que foram enviadas à base comum em não conformidade. Os casos mais comuns em que o reprocessamento é realizado são:

- Divergência de valores entre o banco de dados e a ECF;
- Divergência entre itens impressos no cupom e ECF e etc;
- Divergência entre o valor do cupom e o somatório dos itens;
- Queda de energia provocando a divergência entre itens cancelados na ECF e no cupom;
- Diferença de valores no Mapa Resumo.

Para acessar a opção de reprocessamento no sistema da SOCIN, deve-se acessar o menu **"Movimento > Vendas > Reprocessamento"**.

O reprocessamento da SOCIN contempla as seguintes movimentações:

- Movimento de Venda (Cupom Fiscal/Cancelamento);
- Movimento de Mapa Resumo (resumo das movimentações da ECF);
- Movimento batimento de caixa (não contemplado na integração);
- Movimento Corban (não contemplado na integração);
- Movimento troco/Sangria/Suprimento (não contemplado na integração);
- Movimento troca mercadoria (devolução);
- Movimento recarga celular (não contemplado na integração).

As tabelas do banco de dados comum (Cupom Fiscal/Mapa Resumo/Devolução), possuem um campo **"SITUACAO\_INTEGRACAO"**, que indica se o registro foi ou não processado.

As rotinas que contemplam a integração SOCIN no Sankhya-W foram tratadas para que, quando se tenha um reprocessamento em qualquer tabela que seja realizada a integração de um registro já existente, as rotinas de inserção verifiquem se já existe o registro no sistema; caso exista, apenas será realizado o UPDATE da movimentação para que o reprocesso realizado na SOCIN fique de acordo com as movimentações inseridas no Sankhya-W.

http://www.socin.com.br/mediawiki\_teste\_28/index.php/Reprocessamento\_de\_movimento

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Regras para aplicação do Reprocessamento

**1-** Na rotina de importação de Cupom Fiscal, é realizada uma verificação se o mesmo já existe na base de dados, caso exista, irá barrar o reprocessamento se:

- O financeiro tiver sido baixado em data diferente da data de vencimento (venda a prazo);
- O movimento bancário estiver conciliado;
- O cupom tiver gerado um novo movimento na tabela TGFVAR (Devolução etc).

**2-** Na rotina de importação de troca/devolução de mercadorias, é realizada uma verificação se estas já existem na base de dados, caso existam, irá barrar o reprocessamento se:

- A nota já estiver confirmada.

Se alguma das travas acima forem acionadas, será gerado um lançamento na tabela de LOG com o motivo de erro para que o usuário verifique. Caso contrário, o movimento é excluído e o reprocessamento será realizado da movimentação configurada.

**3-** A rotina de importação de mapa resumo foi alterada para verificar se o registro que está sendo reprocessado já existe na base de dados; caso não exista, insere o movimento; caso exista, o sistema irá excluir o registro existente e realizar o reprocessamento, inserindo um novo registro com os valores atualizados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)

## Transferência de valores (Troco)

A rotina **"Transferência de Títulos"** conta com a funcionalidade **"Usar valor do troco EConect"** no botão direito do mouse, que ficará visível somente se o parâmetro de chave TIPTITTROCOECON estiver configurado.

Tal funcionalidade quando acionada, serão somados os trocos de todos os financeiros cujos tipos de título não estejam incluídos no parâmetro e que sejam:

- Do mesmo Caixa;
- Cupons inseridos pelo mesmo usuário;
- Da mesma empresa;
- Do mesmo período;
- Os títulos selecionados.

Ao realizar a transferência, o valor do troco será subtraído da soma dos títulos selecionados.

![Imagem 16: Esta customização está disponível apenas no MGE.](https://ajuda.sankhya.com.br/hc/article_attachments/16637631962519) Esta customização está disponível apenas no MGE.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598694-Integra%C3%A7%C3%A3o-com-a-EConect-SOCIN#top)
