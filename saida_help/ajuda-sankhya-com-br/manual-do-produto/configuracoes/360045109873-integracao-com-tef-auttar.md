---
id: "360045109873"
titulo: "Integração com TEF AUTTAR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-08T13:23:01Z"
rotulos: ["SERVDIRMOD", "Configuração", "Central de Vendas", "Movimentação Financeira", "TEF", "Auttar", "Integração", "MODIMPCOMPTEF", "USARECEBCARTCTF", "Integração com TEF AUTTAR manual", "Financeiro", "Implementação do TEF AUTTAR"]
---

# Integração com TEF AUTTAR

**Premissas:**

**1.**Completa configuração do ERP (Sankhya-W) conforme instruções abaixo;

**2.**[Instalação e configuração do CTFClient "WEBSOCKET"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#instalaodoctfclient) (responsabilidade do implantador Auttar).

Visando propiciar para os usuários do sistema uma integração com o TEF, de modo que estes possam realizar suas operações de prestação de serviço ou venda de mercadorias (principalmente quando se tratar de NFC-e - maior uso por parte de varejistas), com base em transações com cartão de crédito e/ou débito.

Tal integração se dará juntamente a empresa [AUTTAR](https://www.auttar.com.br/) e seu produto CTFFast (TEF na Nuvem) (CTF - Concentrador de Transações Financeiras).

Por meio das configurações descritas abaixo, será possível efetuar o recebimento e o cancelamento de recebimentos de títulos correspondentes às notas de produtos e serviços via cartão de crédito e débito, tanto na Movimentação Financeira, quanto na Central de Vendas.

**Observação:** tanto na Auttar quanto na PayGo não é possível realizar o estorno parcial de transações de cartão. Ou seja, tendo-se um produto de R$5 reais que foi adquirido pelo cliente em 3 unidades, dá-se um total de R$15 reais. Se por algum motivo o cliente desejar devolver 2 unidades do produto, não será possível realizar o estorno do valor de R$10 reais. Ambas as empresas trabalham com NSU, assim a transação de R$15 reais deve ser estornada em valor integral para que uma nova venda no valor de R$5 reais seja realizada. Já o SITEF possui a funcionalidade de estorno com NSU e permite também que seja informado um valor específico a ser estornado. Deste modo, caso o cliente realize uma compra de R$15 reais, pode-se realizar o estorno deste valor ou até mesmo de um valor menor.

Vejamos os detalhes acerca das configurações a serem realizadas no sistema, bem como seu consequente comportamento:

[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#preferncias)                                                                   [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdettulo)

[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdenegociao)                                                    [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdeoperao-top)

[Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#centraldevendas)                                                         [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#movimentaofinanceira)

[Tipos de Transações Atendidas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdetransaesatendidas)                                 [Restrições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#restries)

[Preferências de recebimento com cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#prefernciasderecebimentocomcarto)                [Conciliação cartão de crédito AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#conciliaocartodecrditoauttar)

[Comprovantes de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#comprovantesderecebimento)                                 [Instalação do CTFClient](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#instalaodoctfclient) 

[Aplicativo – CTFClient](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#aplicativoctfclient)                                                  [Considerações Finais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#consideraesfinais)

[Mapa de Cartões AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025233214-Mapa-de-Cart%C3%B5es-AUTTAR)

## Preferências

Primeiramente, é essencial que nas [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias), o parâmetro **"Usa recebimento com cartão (CTFClient)? - USARECEBCARTCTF"** seja habilitado; esta medida irá capacitar no Sankhya-Om a comunicação com o TEF-AUTTAR.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Tipos de Título

No [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), determina-se na aba Geral, a **"Forma de pagamento"** como TEF-AUTTAR; esta informação posteriormente irá auxiliar nas análises gerenciais. Configura-se também o campo **"Tipo de pgto para NFC-e / NF-e / CF-e"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) com as opções 03-Cartão de Crédito ou 04-Cartão de Débito:

![Imagem 1: No Cadastro de Tipos de Título , determina-se na aba Geral , a "Forma de pagamento" como TEF-AUTTAR ; esta informação…](https://ajuda.sankhya.com.br/hc/article_attachments/4418999627671)

No [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal), campo Subtipo, a categoria do tipo de título em questão, que nesta ocasião, deve ser definido dentre as seguintes opções:

- Cartão de crédito;
- Cartão de débito;
- Voucher**\***;

**\*** Título, recibo ou documento que comprova o pagamento e o direito a um serviço ou a um produto. Os vouchers são muitas vezes utilizados como estratégia de marketing por várias empresas, que oferecem descontos para que os clientes comprem algum produto ou serviço.

**Importante:** na realização do recebimento em cartão através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025237294-Central-de-Vendas), para que ocorra a baixa do título correspondente no financeiro, é necessário que o Tipo de Título vinculado ao [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113513-Tipo-de-Negocia%C3%A7%C3%A3o) utilizado no lançamento de tal registro, esteja com a marcação **"Baixa Automática?"** efetuada (vide imagem acima).

Ainda no [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo), é necessário atentar-se para a aba Preferências de Cartão:

![Imagem 2: Ainda no Cadastro de Tipos de Título , é necessário atentar-se para a aba Preferências de Cartão :](https://ajuda.sankhya.com.br/hc/article_attachments/4418999643031)

Os campos desta aba serão habilitados para uso, caso os campos **"Tipo de pagto para NFC-e / NF-e / CF-e"** e **"Subtipo"** presentes na aba Geral e Painel Principal, respectivamente (também no [Cadastro de Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo)), estejam definidos como **"Cartão de Crédito"** ou **"Cartão de Débito"**.

Deve-se configurar todos os campos presentes na aba. A saber:

Operação CTF: Determina-se neste campo, a operação primordial a ser realizada pelo CTF. Tem-se as seguintes opções:

- Voucher;
- Créd. à vista;
- Créd. Parcelado Administradora (com juros);
- Débito;
- Débito Parcelado com parcela à Vista;
- Débito Parcelado;
- Débito Pré-datado;
- Créd. Parcelado Lojista (sem juros).

Vencimento: Define-se de 1º a 31, qual a data de vencimento pertinente ao cartão.

Tipo vencimento: Deve-se estabelecer como se dará o vencimento do cartão; pode-se fazê-lo estabelecendo um dia fixo ou considerando a data atual somando-a ao vencimento. Tem-se as seguintes alternativas:

- Dia fixo;
- Hoje + Vencimento.

**Qtd. parcelas:** Informa-se a quantidade de parcelas a serem utilizadas nas transações com Cartão de Crédito e Cartão de Débito nas operações da TEF AUTTAR.

**Receber antes de aprovar a nota:** Caso esta marcação esteja realizada, na concretização de uma venda via Cartão de Crédito e Cartão de Débito, será possível proceder com a confirmação da nota somente após a finalização (aprovação) da operação do Cartão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Tipos de Negociação

No [Cadastro de Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113513-Tipo-de-Negocia%C3%A7%C3%A3o), na aba Parcelas, deve-se ter vinculado o Tipo de Título configurado na instrução anterior, ou seja, associado ao cadastro de recebimento do TEF AUTTAR:

![Imagem 3: No Cadastro de Tipos de Negociação , na aba Parcelas , deve-se ter vinculado o Tipo de Título configurado na instrução…](https://ajuda.sankhya.com.br/hc/article_attachments/4419018251287)

Para realizar o recebimento com cartão através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), é necessário que a marcação **"Baixa na confirmação"** também presente na [aba Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abaparcelas) esteja realizada; deste modo, ao confirmar o documento, será aberta a tela para processamento do recebimento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Tipos de Operação - TOP

O [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado, na aba Geral, deve ter o campo Financeiro definido como **"Receitas"**, e na aba Financeiro, a Atualização do financeiro, deve ser de **"Inclusão"**.

![Imagem 4: O Tipo de Operação - TOP utilizado, na aba Geral , deve ter o campo Financeiro definido como "Receitas" , e na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/4418998904343)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Central de Vendas

Para que seja possível realizar o recebimento de uma venda via TEF AUTTAR através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), é de extrema importância que as orientações passadas anteriormente nos tópicos [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#preferncias), [Tipo de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdenegociao) e [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#tiposdeoperao-top), sejam corretamente realizadas.

**Observação:**a rotina de recebimento com cartão para vendas via TEF AUTTAR não pode ser utilizada pelo [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas). Essa operação deve ser feita pela Central de Vendas, após o documento ter sido aberto.

Através da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas), o recebimento é realizado utilizando-se o botão **"Receber"** localizado na [aba Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro) da grade [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) da nota:

![Imagem 5: Através da Central de Vendas , o recebimento é realizado utilizando-se o botão "Receber" localizado na aba Financeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/4419013107863)

Pode-se realizar o recebimento da nota com a possibilidade de utilizar mais de um Tipo de Título, parte em débito, parte em crédito, por exemplo. Além disso, pode-se realizar a baixa automática do título após seu recebimento. É possível receber somente uma nota por vez; caso seja necessário receber mais de uma nota/título, deve-se fazê-lo por meio da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) (deve-se atentar para os acessos fornecidos aos usuários que irão executar tal procedimento na Movimentação Financeira).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Movimentação Financeira

Na tela de [Movimentações Financeiras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025240934-Movimenta%C3%A7%C3%A3o-Financeira), depois de realizada a ativação do parâmetro de chave USARECEBCARTCTF como mencionado no tópico [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#preferncias), será apresentado para utilização, o botão  **"Receber"**, no qual você poderá receber o pagamento de títulos por cartão.

**Observação:** ao pesquisar determinado **"Tipo de título"** no pop-up **"Recebimento com cartão"**, somente os títulos financeiros semelhante a ele serão apresentados se o parâmetro **"Filtrar Tipos de título similares no Rec. Cartão? - FTIPTITRECCAR"** for ligado.

![Imagem 6: Observação: ao pesquisar determinado "Tipo de título" no pop-up "Recebimento com cartão" , somente os títulos…](https://ajuda.sankhya.com.br/hc/article_attachments/6624087698711)

**Observação:** o **"Tempo restante"** é exibido no rodapé da tela para você verificar quando o TEF não responder à requisição de recebimento. Assim, se o tempo limite de resposta for excedido, será apresentada a seguinte mensagem:

**"Ocorreu um erro no processamento da transação. Recomenda-se verificar o status da transação junto a operadora e em seguida tentar reprocessar o recebimento ou proceder com o recebimento administrativo."**

Após isso, o título estará elegível para realizar o Recebimento com cartão (Administrativo).

Além disso, no botão ![Imagem 7: Além disso, no botão Outras Opções... serão disponibilizadas as opções relacionadas à rotina de recebimento do TEF…](https://ajuda.sankhya.com.br/hc/article_attachments/16637461546903) Outras Opções... serão disponibilizadas as opções relacionadas à rotina de recebimento do TEF AUTTAR:

![Imagem 8: Além disso, no botão Outras Opções... serão disponibilizadas as opções relacionadas à rotina de recebimento do TEF…](https://ajuda.sankhya.com.br/hc/article_attachments/6624377235351)

- **Cancelar recebimento com cartão:** Este tipo de cancelamento quando utilizado, invalida o título em questão no sistema e sua correspondente movimentação junto a Auttar.
- **Cancelar recebimento com cartão (Administrativo):** Esta modalidade de cancelamento, é utilizada em casos onde o usuário não possui alçada suficiente para fazê-lo, ou ocorreram problemas de disponibilidade da Auttar. Ao utilizar esta opção, o título será invalidado apenas no sistema, sendo necessário acionar a Auttar posteriormente para que seja efetuado o cancelamento da transação na Administradora de cartão.

**Observação:** o cancelamento de uma transação é realizado apenas pela tela de Movimentação Financeira.

- **Pref. de recebimento com cartão:** Tem-se nesta opção as particularidades acerca do recebimento com cartão; são definições realizadas e salvas por usuário. No tópico [Preferências de recebimento com cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#prefernciasderecebimentocomcarto), explanamos melhor sobre esta opção.
- **Reimprimir comprovante:** Para que sejam impressos os comprovantes, a impressora vinculada à máquina deve ter o nome cadastrado como IMPRESSORATEF. No caso da utilização do Windows, esta configuração é realizada no Painel de Controle > Dispositivos e Impressoras.
- **Recebimento com cartão (Administrativo):** Acesse a documentação [Recebimento com cartão (Administrativo)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111893-Movimenta%C3%A7%C3%A3o-Financeira-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#recebimentocomcart%C3%A3o(administrativo)) para verificar as informações sobre essa opção.

![Imagem 9: Recebimento com cartão (Administrativo): Acesse a documentação Recebimento com cartão (Administrativo) para verificar…](https://ajuda.sankhya.com.br/hc/article_attachments/5268449028247)

**Importante:** a impressora homologada pela Sankhya atualmente é a modelo **"Daruma DR800"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Tipos de Transações Atendidas

Vejamos os Tipos de transações atendidas (Operações TEF):

#### Crédito:

112 - À Vista

113 - Crédito Parcelado Lojista (sem juros)

114 - Crédito Parcelado Administradora (com juros)

#### Débito:

101 - Débito

103 - Débito Pré-datado

104 - Débito Parcelado

105 - Débito Parcelado com parcela à vista

106 - Voucher

#### Cancelamento:

128 - Cancelamento

128.1 - Cancelamento automático junto à AUTTAR

128.2 - Cancelamento (Administrativo) - Cancelamento apenas no ERP, ficando a responsabilidade do back-office comunicar a AUTTAR

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Restrições

- A instalação/configuração do integrador Auttar (CTFClient) é de total responsabilidade do suporte técnico da AUTTAR;
- A integração permite o recebimento das bandeiras mapeadas pela Auttar. Vide documento [Mapa de Cartões AUTTAR](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602474-Mapa-de-Cart%C3%B5es-AUTTAR);
- O produto poderá ter limitações de recebimento por bandeira (por exemplo, American Express) de acordo com o contrato realizado junto à AUTTAR;
- Demais tipos de operação não contempladas neste documento deverão ser previstas em implementações futuras;
- A administradora responsável pelo recebimento deverá ser negociada junto à AUTTAR (Santander, Cielo, Rede etc);
- O Sankhya-W não se responsabiliza por indisponibilidade de comunicação entre o CTFClient e a administradora de crédito contratada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Preferências de recebimento com cartão

Apresentado por meio da opção Pref. de recebimento com cartão presente no botão Outras Opções..., o pop-up com esta mesma nomenclatura, permite que sejam definidas as peculiaridades acerca dos recebimentos com cartão. Esta é uma configuração que deverá ser feita para cada usuário em específico que utilizar a rotina.

![Imagem 10: Apresentado por meio da opção Pref. de recebimento com cartão presente no botão Outras Opções... , o pop-up com esta…](https://ajuda.sankhya.com.br/hc/article_attachments/4418998083863)

Observe os detalhes do pop-up:

**Calcular juros até a data atual?:** Através desta marcação, o sistema calcula os juros de títulos vencidos anteriormente à data atual da baixa com cartão.

**Zerar juros e multas?:** Por esta definição, os juros e multas serão zerados.

**Observação:** caso ambas as marcações Calcular juros até a data atual? e Zerar juros e multas? sejam realizadas, ao efetuar a baixa, o sistema dará preferência para a opção de Zerar juros e multas.

**Dados de baixa**

**Empresa baixa:** Determina-se a [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112913-Empresas) a ser utilizada na baixa do título recebido com o cartão.

**Conta baixa:** Define-se a [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) na qual será efetuada a baixa do título recebido com o cartão.

**TOP baixa:** Informa-se o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) a ser empregado na baixa do título recebido com o cartão.

**Lançamento:** Determina-se o [Lançamento bancário](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694-Hist%C3%B3ricos-Lan%C3%A7amentos-Banc%C3%A1rios) que será realizado quando a baixa do título recebido com cartão ocorrer.

**Título residual**

- Vencimento mais próximo;
- Vencimento mais distante;
- Hoje.

Estas marcações são utilizadas para o cálculo do vencimento do título residual, quando efetua-se um recebimento com cartão a menor. Esta situação ocorre apenas quando for utilizado o recebimento com cartão fora da Tela de Recebimento que é apresentada automaticamente ao se efetuar o recebimento com cartão de crédito.

#### Renegociação

**Usar renegociação:** Ao realizar esta marcação, o sistema irá inibir o título original, exibindo o novo título que se encontra baixado. Caso esta marcação não seja realizada, será feita a baixa e atualização dos dados do próprio título normalmente.

**TOP renegociação:** Informa-se aqui, o Tipo de Operação - TOP que será utilizado na baixa do título recebido com cartão.

**Importante:** no recebimento de um título que possua datas padronizadas, caso a data de vencimento coincida com sábados, domingos ou feriados, o vencimento será transferido para o dia seguinte. Em se tratando de feriados, esta situação ocorre desde que se tenham feriados cadastrados no sistema.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Conciliação cartão de crédito AUTTAR

Este tópico visa orientar na configuração do layout de retorno e processamento do arquivo vindo da Auttar. Uma vez processado o arquivo, a baixa ocorre automaticamente juntamente à conciliação bancária do mesmo. Vejamos:

- O layout de processamento de arquivo de retorno de cartão para a Auttar já é disponibilizado pré-configurado no sistema, bastando importá-lo pelo Sankhya Om. Este procedimento de importação é realizado por meio da tela [Layout de Processamento de Arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607054).

![Imagem 11: O layout de processamento de arquivo de retorno de cartão para a Auttar já é disponibilizado pré-configurado no…](https://ajuda.sankhya.com.br/hc/article_attachments/4418998312471)

- Nesta tela, através do botão Outras Opções... tem-se a opção **"Criar arquivo a partir de um modelo"**, que ao ser acionada abre um pop-up com esta mesma nomenclatura para escolha do modelo Auttar e criação do modelo.
- Para que a Prévia/Processamento do arquivo de retorno ocorra de forma correta, é necessário que todos os campos presentes na tela [Conciliação de Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606334) estejam pré-configurados.

![Imagem 12: Para que a Prévia/Processamento do arquivo de retorno ocorra de forma correta, é necessário que todos os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/4418984126743)

- Ao clicar-se nos botões Prévia, Processar ou Log, a tela é direcionada para os detalhes do log executando a finalidade correspondente ao botão acionado; pode-se retornar aos dados da baixa, clicando-se no botão Processamento.
- Caso exista algum erro no processamento do arquivo de retorno de cartão, a mensagem correspondente ao problema encontrado será apresentada na tela. São possíveis mensagens:

Não foi possível processar o arquivo. A estrutura do layout não é adequada a estrutura do arquivo ou não foram encontrados os identificadores correspondentes.

Não foi encontrado o NSU gerado pela Autorizadora (campo NSU\_ADQUIRENTE).

Campo NSU\_ADQUIRENTE não configurado no layout.

Não foram encontradas transações (TGFTEF) para o NSU {XXX}.

Foram encontrados múltiplos títulos para o NSU {XXX}.

Financeiro não encontrado.

Título já foi baixado.

O valor de baixa do título {XXX} está diferente do valor da transação {XX,XX}.

O arquivo de retorno não foi encontrado.

A empresa de baixa é obrigatória.

A conta de baixa é obrigatória.

O Tipo de Operação de baixa é obrigatório.

O lançamento obrigatório.

O layout de configuração é obrigatório.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Comprovantes de Recebimento

Ao trabalhar com a integração TEF Auttar, é parte do processo, realizar para os clientes a impressão de comprovantes de recebimento. Esta impressão acontece com base em um arquivo modelo previamente configurado e vinculado ao sistema. Vejamos:

#### Criação do modelo de comprovante

Na construção do modelo a ser utilizado, que deve ser no formato **".txt"**, pode-se trabalhar com três variáveis que representam os três modelos de comprovante gerados pela Auttar:

**1 -** &cupomEstabelecimento

**2 -** &cupomCliente

**3 -** &cupomReduzido

Tem-se também a função **"moverLinhas"**, que será utilizada na centralização da impressão do comprovante. Esta função recebe dois parâmetros:

moverLinhas(string texto, int colunas)

onde,

string texto = texto a ser impresso

int colunas = quantidade de colunas para realização da tabulação à direita

Além disso, tem-se a função **"guilhotinaDaruma"**, que permitirá que sejam efetuados cortes dos comprovantes:

guilhotinaDaruma()

**Vínculo do modelo de comprovante no sistema**

Uma vez configurado o modelo de comprovante de recebimento, este será trabalhado no sistema, através do parâmetro **"Modelo para impressão de comprovantes TEF - MODIMPCOMPTEF"**, onde informa-se o nome do arquivo que foi criado na instrução anterior juntamente com sua extensão, por exemplo, modeloTEF.txt.

Além disso, o caminho correspondente ao diretório em que o modelo de comprovante foi salvo, deve ser inserido no parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**, por exemplo, C:\Modelo\

**Exemplo de modelo de comprovante**

Um modelo de comprovante pode ser elaborado associando-se as variáveis e funções descritas acima, de acordo com a necessidade e processo de cada empresa. Vejamos um exemplo de modelo criado e sua respectiva impressão:

![Imagem 13: Um modelo de comprovante pode ser elaborado associando-se as variáveis e funções descritas acima, de acordo com a…](https://ajuda.sankhya.com.br/hc/article_attachments/5268499918871)

![Imagem 14: Um modelo de comprovante pode ser elaborado associando-se as variáveis e funções descritas acima, de acordo com a…](https://ajuda.sankhya.com.br/hc/article_attachments/5268512870807)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Instalação do CTFClient

**Observação:** a instalação, configuração e disponibilidade dos serviços do CTFClient é de responsabilidade da Auttar.

Vejamos abaixo, os passos para instalação do CTFClient:

**1.**Instalar o CTFClient (WEBSOCKET) com acessos de Usuário Administrador. Executa-se (duplo clique) o arquivo denominado **"setup.exe"**;

**2.**Deve-se seguir os seguintes passos de instalação:

**Passo 1:**

![Imagem 15: Passo 1:](https://ajuda.sankhya.com.br/hc/article_attachments/5268485250199)

**Passo 2:**

![Imagem 16: Passo 2:](https://ajuda.sankhya.com.br/hc/article_attachments/5268550766103)

**Passo 3:**

![Imagem 17: Passo 3:](https://ajuda.sankhya.com.br/hc/article_attachments/5268530165527)

**Passo 4:**

![Imagem 18: Passo 4:](https://ajuda.sankhya.com.br/hc/article_attachments/5268584976407)

**3.**Dar acesso a todos os usuários à pasta instalada;

**4.**Iniciar o CTFClient como administrador e selecionar a opção 1 - INICIALIZAÇÃO. Depois que a mensagem "CTFCLIENT Inicializado com sucesso" for apresentada, deve-se pressionar a tecla ENTER e selecionar a opção 6 - SAIR:

![Imagem 19: 4. Iniciar o CTFClient como administrador e selecionar a opção 1 - INICIALIZAÇÃO . Depois que a mensagem " CTFCLIENT…](https://ajuda.sankhya.com.br/hc/article_attachments/5268609857431)

**5.**Feito esse processo, a [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira) e a [Central](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) já estarão conectando com o CTFClient.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Aplicativo – CTFClient

Para que a integração funcione e as transações financeiras sejam processadas, é necessário que o aplicativo **"CTFClient"** esteja instalado e devidamente configurado na máquina/estação que irá executar a operação, ou seja, máquina/estação onde o Sankhya-W estiver sendo executado.

![Imagem 20: Para que a integração funcione e as transações financeiras sejam processadas, é necessário que o aplicativo "CTFClient"…](https://ajuda.sankhya.com.br/hc/article_attachments/5268612009879)

**Importante:** a instalação e configuração deste aplicativo é de responsabilidade da AUTTAR, ou conforme negociação da empresa com os mesmos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

## Considerações Finais

Através das configurações relatadas até aqui, pode-se realizar os passos gerais descritos abaixo, mas que irão se diferenciar de acordo com as definições de cada processo e empresa quanto ao Tipos de Títulos, Baixa dos registros, Datas de Vencimento etc. Vejamos:

- Acessar a tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira);
- Selecionar o título que deseja-se receber;
- Clicar no botão Receber;
- Será aberto o pop-up Recebimento com cartão;
- Seleciona-se o Tipo de Título a ser utilizado;
- Determina-se a Quantidade de Parcelas, quando for o caso;
- Clica-se no botão Receber;
- Ao clicar no botão Receber, o sistema imediatamente faz a comunicação com o TEF AUTTAR e solicita os dados do cartão do cliente (número do cartão, data de validade e código de segurança);
- Depois de inseridos os dados do cartão do cliente, o sistema efetua a comunicação com o TEF AUTTAR e libera as informações do Total dos Títulos, Total Recebido e Saldo a Receber, além de exibir um resumo do comprovante;
- Ao Concluir o procedimento, o sistema registra a transação juntamente ao TEF AUTTAR;
- Por fim, o sistema exibe um pop-up de Confirmação informando que a operação foi realizada com sucesso, e se deseja-se visualizar o(s) título(s).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109873-Integra%C3%A7%C3%A3o-com-TEF-AUTTAR#top)

![Imagem 21: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16637534125463) Acesse também:

[TEF - Transação Eletrônica de Fundos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108253-TEF-Transa%C3%A7%C3%A3o-Eletr%C3%B4nica-de-Fundos)
