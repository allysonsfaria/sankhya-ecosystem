---
id: "360053082414"
titulo: "Preferências do Sankhya Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Sankhya Checkout"
atualizado_em: "2026-07-29T16:03:00Z"
rotulos: ["Configuração", "Impressão", "Caixa", "Integração", "Preferências", "Sankhya Checkout", "Configure conferência sangria automática e contas", "Ajuste impressão de códigos descrições e mensagens", "Configure alertas e caminho para arquivos não integrados"]
---

# Preferências do Sankhya Checkout

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314998014103) Módulo: Configurações > Sankhya Checkout 
```

---

Neste artigo trataremos do menu **"Preferências"**do [Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394).

Para acessar esse menu vá até ícone  no canto superior esquerdo do Checkout, posteriormente clique no menu nomeado Preferências, assim teremos as seguintes abas:

| [Aba Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abacaixa) | [Aba Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abaimpress%C3%A3o) | [Aba Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abaintegra%C3%A7%C3%A3o) |
| --- | --- | --- |
| [Aba Lity](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abality) | [Aba Login](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abalogin) | [Aba SAT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abaSAT) |
| [Aba Sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abasistema) | [Aba Venda](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#abavenda) |  |

## Aba Caixa

Neste tópico abordaremos os parâmetros referentes da aba Caixa.

**Conferir Caixa no ERP:** para utilizar este, é necessário que o parâmetro **"Exigir conferência ao fechar caixa"** esteja ligado. Desta forma, em Conferir Caixa no ERP será permitido que o caixa seja exportado mesmo aguardando conferência. No momento em que você fechar o caixa, o sistema deixará pronto o pacote para exportação ao ERP. Assim, com o parâmetro ligado, o sistema passará a enviar as sangrias de caixa ao ERP assim que estas forem realizadas.

Além disso, caso tenha dinheiro no caixa no fechamento, a informação do dinheiro em caixa será obrigatória. Então, o sistema fará uma sangria automática do dinheiro informado para que esta seja enviada ao ERP. Destacamos ainda, que o caixa sempre será encerrado com valor zerado para que o saldo inicial do próximo caixa seja zero.

Se este estiver desligado, o totalizador das sangrias manuais e automáticas serão enviadas somente no fechamento de caixa.

Além disso, ao fechar o caixa serão apresentados todos os tipos de títulos para conferência.

Habilitando a marcação **"Exige conferência ao fechar o caixa"** será possível ainda, fazer o registro de cada um dos títulos de forma manual, para que na impressão do fechamento de caixa, estes valores sejam registrados de forma íntegra.

**Observação:** caso o usuário possua a função gerente e caixa, será possível que ele visualize os valores calculados e tenha a opção de inserir o valor informado no momento do fechamento de caixa.

**Conta para Débito da Sangria no ERP:** para que as informações de fechamento do caixa sejam exportadas é necessário que este parâmetro seja maior que zero ou o parâmetro Conferir caixa no ERP esteja habilitado.

**Conta para Crédito da Sangria no ERP:** neste parâmetro insira o código da conta para Sangria.

**Código forma para pagamento para despesa:** informe o código da forma de pagamento da despesa.

**Código forma pagamento para receita:** informe o código da forma de pagamento da receita. Considere o parâmetro anterior e o mencionado aqui como sendo as formas de pagamento para geração de despesa ou receita quando a conferência do caixa for executada e for necessário a geração desta no ERP.

**Exigir CPF/CNPJ na nota acima de:** quando um determinado valor for inserido neste parâmetro, o sistema irá exigir o CPF quando o valor da compra o ultrapassar. Sendo que, o parceiro deverá ser identificado na tela de vendas e ser cadastrado como parceiro ou apenas como adquirente do CPF, nome ou telefone.

**Exigir conferência ao fechar caixa:** quando este parâmetro estiver habilitado e o fechamento do caixa for realizado, o sistema consultará os valores registrados e gerará um fechamento cego, calculando a diferença entre os valores do sistema e os informados pelo caixa. E ainda, o sistema apresentará o layout de **"Conferência de Caixa"** e, quando desmarcado, exibirá o layout de **"Fechamento de caixa"**.

Além disso, o usuário caixa não poderá visualizar o campo **"Calculado"** no pop-up Fechamento de caixa.

**Observação:** a operação de conferência é exclusiva para usuários com perfil de caixa. Perfis de gerentes não tem a restrição de ocultação de valores.

**Nota:** quando este parâmetro estiver ligado, o sistema não exibirá as seguintes informações:

- Saldo inicial na tela e no relatório de fechamento de caixa e na tela de abertura de caixa;
- Valores calculados pelo sistema no relatório de fechamento de caixa;
- Valor total de sangria e suprimento no relatório de fechamento de caixa;
- Valor disponível para sangria na mensagem de validação do valor a ser sangrado.

**Exportar movimentações pendentes ao fechar caixa:** quando você ligar esse parâmetro, o checkout irá realizar a exportação das movimentações pendentes no fechamento de caixa, sendo que, o sistema não poderá ser encerrado antes destas estarem concluídas. Lembre-se, o ERP deve estar online para as exportações serem realizadas.

**Gerar sangria ao fechar caixa:**se você marcar este parâmetro, no fechamento de caixa todo o dinheiro será retirado pelo sistema e transferido para a conta configurada no ERP, assim quando o caixa for aberto novamente o saldo inicial será iniciado com zero.

**Mostra informações adicionais de fechamento de caixa:** ao selecioná-lo, os valores de cartão crédito/débito e quantidade de notas do caixa serão transferidos para o relatório. Além disso, dados referentes aos valores adquiridos em trocas e devoluções, valores devolvidos em créditos, e descontos concedidos em vendas também poderão ser conferidos na tela **"Fechamento de Caixa"** e ao imprimir o cupom fiscal.

conferir os valores adquiridos a partir de trocas e devoluções, valores devolvidos em créditos, além dos descontos concedidos na venda

**Valor máximo em dinheiro no caixa:** quando você clicar no referido campo do parâmetro, o sistema abrirá o pop-up **"Manutenção de Parâmetro"** em que pode-se informar o valor máximo no caixa para fazer a sangria, sendo que, o valor mínimo para ser inserido deverá ser de R$ 300,00.

**Abrir gaveta na sangria e suprimento de caixa:** ao habilitar o referido parâmetro, e realizar a sangria ou o suprimento, em um caixa com status em aberto, o sistema acionará automaticamente a abertura de gaveta.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba Impressão

Esta aba dispõe dos parâmetros:

**Imprimir código de barras da troca no comprovante NFCe?:** ao acionar esse parâmetro, o código da troca realizada não será impressa na Nota Fiscal, de forma que, será possível economizar no tamanho da impressão do comprovante.

**Imprimir operador de caixa na observação:**para esta função ser executada corretamente, na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao) marque a opção **"Caixa"** no cadastro do funcionário.

**Imprimir descrição resumida do item no comprovante NFCe?:** ao habilitar este, os itens da nota fiscal serão impressos de forma resumida no comprovante.

**Mensagem padrão para a nota:**se você inserir um valor no campo de texto do parâmetro, esta será a mensagem padrão exibida no cupom, por exemplo "Obrigado pela preferência, volte sempre!".

**Utilizar endereço do cliente na nota?:**quando o parceiro é adquirente, por sua vez não possuirá cadastro no sistema. Assim quando uma entrega para este precisar ser realizada, este parâmetro deve ser marcado.

**Utilizar impressão otimizada?:** com esse parâmetro habilitado, o sistema irá reduzir os espaços em branco da impressão padrão, o que irá possibilitar a economia dos papéis a serem impressos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba Integração

Os parâmetros disponíveis nesta aba são:

**Avisar notas inutilizadas não integradas:** ao ativar esse parâmetro, o sistema irá emitir uma mensagem o informando que o Checkout possui notas inutilizadas que não foram integradas. Essa mensagem também será exibida nas notificações do sistema por meio do ícone ![Imagem 2: Avisar notas inutilizadas não integradas: ao ativar esse parâmetro, o sistema irá emitir uma mensagem o informando que…](https://ajuda.sankhya.com.br/hc/article_attachments/21657456232343) **"Notificações"**.

**Caminho para Salvar movimentos não integrados com ERP:** insira nesse parâmetro, o caminho ou pasta onde os arquivos JSON dos movimentos não integrados no ERP ficarão salvos. Saiba mais sobre este processo, clicando no link [Salvar arquivos de backup](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056765053#salvararquivosdebackup).

**Código da TOP para sangria:**  informe aqui a TOP para realizar a sangria e suprimento. Destacamos que para esse parâmetro funcionar corretamente será necessário que você também informe os Códigos de lançamento nos parâmetros descritos abaixo.

**Código de lançamento bancário para sangria:**insira neste o código de lançamento para sangria.

**Código lançamento para Suprimento:** preencha este parâmetro com o código de lançamento para o Suprimento.

**Nota:** se os três últimos parâmetros mencionados não estiverem com os valores do ERP devidamente informados, os registros ficarão presos na tela de ADM do Checkout impossibilitados de completar a integração.

**Grupos de produto que não são integrados:** deve-se inserir aqui os Grupos de produtos que não serão integrados, sendo que este serão aqueles produtos de consumo da próprio empresa, por exemplo.

**Intervalo de integração com o ERP (minutos): v**ocê poderá inserir o tempo em minutos entre as integrações com o ERP, sendo que o tempo será aceito apenas antes de integrar.

**Realiza troca somente com cupom da empresa de venda?:** se este for selecionado, o cupom a ser apresentado necessita ser da mesma empresa em que a venda foi realizada, ou não será possível a realização de troca nem a requisição de senha do gerente para liberação.

**Realiza troca somente com cupom?:** ao selecionar esta marcação, será necessário apresentar o cupom da compra realizada, e que esta seja da mesma empresa para que a troca da mercadoria seja efetuada, caso contrário a troca não é realizada ou o gerente poderá ser requisitado para realizar a ação mediante apresentação de senha.

**Registra financeiro de troca como pendente:** se você efetuar a marcação deste parâmetro, na troca da integração todo financeiro será gerado como pendente Movimentação Financeira do ERP, essa ação poderá ser feita de acordo com a necessidade.

**Tipo de título para recebimento em voucher:** no campo desse parâmetro, você informará o código do **"Tipo de Título"** cadastrado na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) do Sankhya Om, que será utilizado para o pagamento com voucher na tela de vendas do Chekout através da opção **"(F8) Voucher"**. Esse tipo de pagamento também poderá ser efetuado por meio da opção **"(F7) Cartão POS"** ao selecionar a opção **"Voucher"** no campo **"Tipo de Pagamento"**. Será possível verificar se a integração foi realizada com o Tipo de Título especificado, na aba [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#abafinanceiro) do [Rodapé](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas#graderodap) da [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas).

**Tipo de título para lançamento de crédito para cliente**, **Tipo de título para recebimento a prazo** e **Tipo de título para recebimento a vista:** referente a esses parâmetros, para cada um destes realize na tela [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo) as configurações para as formas de pagamentos que serão utilizadas pelos clientes. Desta forma, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abageral) da tela mencionada preencha o campo **"Tipo de pgto para NFC-e / NF-e / CF-e:"**, informe também o **"Subtipo"** do tipo de título a ser utilizado no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#painelprincipal), e marque a opção **"Utiliza no Fast Service?"** na aba [Fast Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo#abafastservice).

**Tipo de Título para recebimento em PIX:** nesse parâmetro você informará o Tipo de Título criado para o recebimento de pagamentos realizados com o PIX. Para maiores detalhes sobre essa funcionalidade acesse o tópico[Recebimentos PIX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360056765053-Processos-de-vendas#recebimentospix).

**Tipo de Título em PIX POS** e **Tipo de Título para recebimento em PIX TEF:** nesses parâmetros informe os códigos dos Tipos de Títulos criados para os recebimentos de pagamentos realizados com o PIX. Para maiores detalhes sobre essa funcionalidade acesse o link [Recebimentos via PIX TEF](https://ajuda.sankhya.com.br/hc/pt-br/articles/14203362302487).

**Tipo de título para recebimento em cartão de crédito**, **Tipo de título para recebimento em cartão de crédito POS**, **Tipo de título para recebimento em cartão de débito** e **Tipo de título para recebimento em cartão de débito POS:** semelhante aos parâmetros anteriores na tela Tipos de Título configure para cada um dos tipos de título, em que na aba Geral deve-se preencher os campos **"Espécie"**, **"Forma de pagamento TEF"** e Tipo de pgto para NFC-e / NF-e / CF-e, informe também o Subtipo do tipo de título a ser utilizado no Painel Principal, e marque a opção Utiliza no Fast Service? na aba Fast Service.

**Observação:** teremos que para os parâmetros Tipo de título para recebimento em cartão de crédito POS e Tipo de título para recebimento em cartão de débito POS deve-se ligar a marcação **"Utiliza POS"**.

**Tipo de Título para recebimento em Cheque:** referente a este parâmetro, na tela Tipos de Título, na aba Geral preencha o campo Tipo de pagto NFC-e/NF-e/CF-e, no Painel Principal informe o Tipo de Título e o  Subtipo e marque a opção Utiliza no Fast Service? na aba Fast Service.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba Lity

Nesta aba, você irá habilitar no checkout o clube de benefícios.

Ao ligar a funcionalidade e dar um nome ao clube, vá até o menu **"Preferências da empresa"**, em seguida **"Preferências Integração Lity"** e defina um **"Usuário"** e **"Senha"** do usuário do Sankhya Om, em que será utilizado para conciliar as informações com o Sankhya Checkout:

[GIF animado: Imagem 3: Ao ligar a funcionalidade e dar um nome ao clube, vá até o menu "Preferências da empresa" , em seguida "Preferências…](https://ajuda.sankhya.com.br/hc/article_attachments/1500002029381)

Assim, ao iniciar uma venda, o sistema irá questioná-lo se o cliente faz parte do clube de benefícios que você cadastrou anteriormente. Caso este seja, você deverá digitar o CPF, uma vez que o telefone será por onde o cliente receberá o link onde ele fará o download do app:

[GIF animado: Imagem 4: Ao clicar no quadro "Economia" , os detalhes do desconto a ser aplicado será exibido. Sendo que, uma vez que o cliente…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001973842)

Ao clicar no quadro **"Economia"**, os detalhes do desconto a ser aplicado será exibido. Sendo que, uma vez que o cliente possuir um valor de venda que ultrapasse o valor do desconto, este será aplicado automaticamente.

![Imagem 5: GIF animado: Imagem 4: Ao clicar no quadro "Economia" , os detalhes do desconto a ser aplicado será exibido. Sendo que,…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001973862)

**Observação:** ao realizar o cancelamento de uma nota por meio da Central de Notas do Sankhya Om, você poderá conferir este movimento com status **"Não Processado"** na **"Administração do Checkout"**, aba [Importação de Movimentações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout#abaimporta%C3%A7%C3%A3odemovimenta%C3%A7%C3%B5es).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba Login

Nesta aba teremos o parâmetro **"Imagem exibida no login"** em que você poderá inserir o caminho da imagem que será exibida quando o login for feito.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba SAT

Nesta aba, por meio do campo **"Versão dos dados Sat/MFE"** você poderá informar a versão de leiaute do SAT.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba sistema

Na aba Sistema, teremos os parâmetros:

**Dias até expirarem as movimentações do sistema:** neste você irá inserir a quantidade de dias até expirarem as movimentações do sistema. E caso faça uso deste, todos os movimentos antigos já integrados com ERP serão excluídos do PDV sem condições de recuperação e será salvo se um backup manual for feito.

**Exibir teclas de atalho para auxílio do usuário?** e **Usar modo escuro:** defina esses parâmetros conforme as suas preferências.

**Segundos para consultar situação na Sefaz novamente inutilização:** aqui, pode-se definir o tempo que o sistema utiliza para realizar a consulta de uma nota na Sefaz antes de inutilizá-la no Checkout.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

## Aba Venda

Nesta, você terá disponível:

**Aplicar desconto quantitativo no Recebimento:** se este parâmetro for marcado, o sistema irá calcular os descontos e apresentará na tela de cupons.

**Considerar a bandeira do cartão em transação TEF:** você selecionará este, caso na transação TEF a bandeira seja retornada e se no Cadastro de Tipo de Título do ERP a bandeira for utilizada no campo Forma pagamento TEF.

**Cor da fonte do caixa** e **Cor da fonte para consulta de preço:** você poderá preencher estes parâmetros de acordo com sua preferência.

**Exibe opções de parcelamento do ERP:** as opções dispostas nesse parâmetro poderão ser utilizadas quando um pagamento for realizado com Cartão de Crédito, Pagamento POS, ou A Prazo. Assim, observe abaixo:

- **1-Não:** ao selecionar essa opção, será possível escolher o tipo de parcelamento conforme as suas definições nos [Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) e [Tipos de Título](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606494-Tipos-de-T%C3%ADtulo).
- **2-Usa com Todas as Tabelas de Preço:** com esta opção definida, no momento do recebimento, o caixa poderá receber com os Tipos de Negociação Cartão de Crédito, POS, ou a Prazo configurados no sistema.

**Observação:** as opções de parcelas só serão exbidas se no Sankhya Om, tela Tipo de Negociação, aba [Características](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o#abacaractersticas), a marcação **"Utiliza no fast service"** estiver assinalada.

- **3-Usa com Restrição por Tabela de Preço:** quando essa opção for selecionada, uma tabela de preço especifíca poderá ser utilizada, além disso, os Tipos de Negociação também podem ser definidos junto à essa configuração. Para isso, na tela [Administração de Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053), selecione a Tabela e o Tipo de Negociação de sua preferência na sub-aba **"Restrição de Preços"** da aba [Cálculo de Preço](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout#abac%C3%A1lculodepre%C3%A7o).

**Nota:** o Sankhya Checkout normalmente faz o uso da tabela padrão ou a mais recente, para visualizar qual tabela o sistema está utilizando basta usar o comando **"SELECT \* FROM TPRECO"** na aba **"NUTAB"** no DBExplore.

**Exige identificação do consumidor na troca:** caso opte por utilizar esta ação, no momento da troca de mercadoria será exigido a identificação do parceiro, seja este já cadastrado ou sendo cadastrado no momento da troca.

**Fixa 1 como quantidade na soma de volumes:** insira o volume fracionado que será utilizado, sendo que aquele introduzido aqui será considerado como volume.

**Fonte do cálculo da Carga média tributária:** neste parâmetro informe a fonte de tabela de alíquotas. Destacamos que é utilizado junto com informações fiscais do Cadastro de produto para colocar a carga média de impostos do cupom.

**Formatação do código de barras:** na tela de Venda, para a leitura do código de barras por peso, esse parâmetro deverá ser marcado. Caso esteja mal configurado, o produto não será encontrado e para configurar será necessário o código do cliente para informar as posições.

**Gerar cadastro para parceiro Adquirente:** quando um parceiro for cadastrado no Checkout no momento de uma venda, mas o endereço dele não, um endereço padrão será automaticamente cadastrado. Destacamos ainda que o novo parceiro será cadastrado no Checkout se a marcação **"Integrar Parceiros"** (menu **"Cadastros"**, **"Checkouts"**) estiver selecionada e ele for cadastrado na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao).

**Habilitar liberação por token:** ao ligar esse parâmetro, se o vendedor não possuir autorização para realizar certa operação no momento da venda, o sistema irá pedir o token cadastrado no registro do usuário que realizará a liberação da operação para o usuário vendedor, sendo esse token cadastrado no campo **"Token de Identificação do Checkout"** da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abageral), tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) no registro do usuário liberador.

![Imagem 6: Para saber mais sobre o campo Token de Identificação do Checkout , acesse a tela Usuários .](https://ajuda.sankhya.com.br/hc/article_attachments/28294322553111) Para saber mais sobre o campo Token de Identificação do Checkout, acesse a tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874).

**Imagem padrão do caixa:** configure o caminho para inserção da imagem do caixa.

**Imagem padrão para produtos sem imagem:** Insira aqui o caminho da imagem para aqueles produtos que não possuem uma imagem cadastrada.

**Incluir info. complementares junto com info. do fisco:** para utilizar este parâmetro, será necessário que seu cadastro esteja cadastrado com algum tipo de complemento.

**Informar "Sem GTIN" para EAN inválidos:** se este parâmetro estiver desmarcado, o campo **"EAN/GTIN Produto p/ NF-e:"** ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaimpostos)) precisa ser configurado corretamente.

**Observação:** este parâmetro não influenciará no cálculo de imposto da [Administração do Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout), pois o cálculo seguirá as marcações do ERP para validar ou não o GTIN.

**Obriga informar motivo de troca:** se marcado, será exigido um motivo para troca, sendo que apenas com uma liberação essa troca poderá ser feita sem o motivo exigido pelo parâmetro.

**Primeira linha de mensagem do caixa e Primeira linha de mensagem do caixa livre:** nesses parâmetros, você poderá inserir a mensagem que será exibida na tela do caixa e a quando este estiver livre.

**Repete último local digitado?:** para tal, o controle deverá ser definido no Cadastro do produto no ERP.

**Segunda linha da mensagem do caixa e segunda linha da mensagem de caixa livre:** aqui, insira a segunda linha das mensagens que você quer que apareçam na tela do caixa.

**Segundos para esperar SEFAZ responder antes de entrar em contingência (30s recomendado sefaz):** você poderá determinar o tempo de espera em segundos. Sendo que a contingência automática controlada pelo sistema não acontecerá mais se você ativar a contingência manual clicando no ícone da SEFAZ.

**Segundos para limpar a tela do caixa após a venda:** por meio deste o sistema definirá o tempo em que a última venda ficará visível no caixa apenas para visualização dos totais.

**Tamanho do código de barras para Conferência:** defina neste parâmetro o tamanho do código de barras do produto.

**UFs que solicitam CPF na venda com cupom fiscal:** se forem informados UFs neste parâmetro, sempre que houver uma venda o CPF do parceiro deverá ser informado.

**Usa o EAN do produto vendido na impressão:** caso este parâmetro seja utilizado, a impressão realizada terá o mesmo código bipado, se não o código a ser exibido será o do produto.

**Utiliza vendedor único por venda?:** quando esse parâmetro for habilitado, o checkout permitirá que você informe o vendedor a qualquer momento da venda, um vez que, ele será utilizado em todos os itens e no cabeçalho desta. Porém, caso o vendedor não seja informado, ao final da venda o sistema irá solicitá-lo. **Validar desconto máximo no rodapé em tempo real:** validar desconto máximo no rodapé em tempo real: Ao ligar esse parâmetro, os descontos que forem aplicados para o total da nota venda sofrerão a validação no exato momento que o desconto for aplicado, sendo que, haverá a possibilidade de solicitação de liberação caso o desconto ultrapasse o limite informado no perfil do usuário caixa.

**Validar desconto máximo por perfil:** com este marcado, você poderá preencher o campo **"% Desconto máximo"** no Cadastro de Perfil do Checkout. Para mais informações deste acesse o link [Liberação de Desconto por Perfil](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Sankhya-Checkout#libera%C3%A7%C3%A3o%20de%20desconto%20por%20perfil).

**Vendedor obrigatório na venda:** se você selecionar este parâmetro, lembre-se de cadastrar o vendedor no [Cadastro de Vendedores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores), assim, no fim da venda será o preenchimento do vendedor, caso não o tenha informado antes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053082414-Prefer%C3%AAncias-do-Sankhya-Checkout#top)

![Imagem 7: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16417585676439) Acesse também:

[Sankhya Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595394-Sankhya-Checkout#libera%C3%A7%C3%A3o%20de%20desconto%20por%20perfil)

[Administração de Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050978053-Administra%C3%A7%C3%A3o-de-Checkout)

[Menu do Checkout](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001985901-Menu-do-Checkout)
