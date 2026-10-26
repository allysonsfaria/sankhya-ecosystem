---
id: "360045115653"
titulo: "Movimentação Bancária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653-Movimenta%C3%A7%C3%A3o-Banc%C3%A1ria"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:45:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contas", "Moeda", "Movimentação Financeira", "Financeiro", "DECVLRMOEDA", "Movimentação Bancária", "Lançamentos", "Transferência de Numerários", "br.com.sankhya.fin.cad.movimentacaobancaria", "Movimentação Bancária manual", "Transferências internas entre contas", "Código Descrição Tipo Conta Origem/Destino", "Data Tipo e valores em moedas", "SUBSTCONTA substitui se ligado"]
---

# Movimentação Bancária

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312493081367) Módulo: Financeiro > Rotinas
```

---

A Movimentação Bancária é utilizada para efetuar lançamentos entre contas correntes, aplicações e caixas. É também conhecida como Transferência de Numerários. Sua característica básica é a não geração de receitas e despesas para a empresa, controlando somente entradas e saídas de valores entre contas.

Enquanto a [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) gerencia entradas e saídas monetárias entre a empresa e o ambiente externo, a Movimentação Bancária gerencia entradas e saídas monetárias internas.

#### ![Imagem 2: Enquanto a Movimentação Financeira gerencia entradas e saídas monetárias entre a empresa e o ambiente externo, a…](https://ajuda.sankhya.com.br/hc/article_attachments/42312493081751)

---

### Painel de Filtros

Encontre os registros da Movimentação Bancária de forma rápida, por meio dos filtros:

- Data de Lançamento;
- Tipo de Operação;
- Núm. Único do Pedido;
- Lançamento;
- Histórico;
- Tipo de Movimento.

Além disso, pode-se filtrar pelas Contas Bancárias e Lançamentos Bancários. Para isso, nas seções **"Conta Origem"** e **"Lançamento Origem"**, clique no botão ![Imagem 3: Além disso, pode-se filtrar pelas Contas Bancárias e Lançamentos Bancários . Para isso, nas seções "Conta Origem" e…](https://ajuda.sankhya.com.br/hc/article_attachments/21574542050583) **"Pesquisar"** para buscar e selecionar os registros desejados.

[GIF animado: Imagem 4: Além disso, pode-se filtrar pelas Contas Bancárias e Lançamentos Bancários . Para isso, nas seções "Conta Origem" e…](https://ajuda.sankhya.com.br/hc/article_attachments/21574570966423)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653-Movimenta%C3%A7%C3%A3o-Banc%C3%A1ria#top)

### Aba Geral

![Imagem 5: Aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/21574542066199)

Nesta aba, existem os seguintes campos: 

**Tipo de Movimento:** neste campo, indique a espécie da movimentação a ser registrada no sistema. A escolha de qualquer uma dessas opções não interfere na funcionalidade da tela. Os possíveis tipos de movimento são:

- **Saque:** o saque é utilizado, por exemplo, para retirar dinheiro de uma conta bancária e transferi-lo para o caixa;
- **Depósito:** retirada no final do dia dos recebimentos do caixa para uma conta bancária;
- **Resgate:** é utilizado para transferir dinheiro de uma conta aplicação para uma conta corrente;
- **Aplicação:** é o oposto do resgate, ou seja, é a transferência da conta-corrente ou do caixa para uma conta aplicação;
- **Transferência:** movimentação entre contas bancárias.

**Nr. Movimento:** esta informação será preenchida conforme a base de numeração determinada no [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) definido para operações de movimento bancário.

**Dt. Lançamento:** neste campo, terá a data em que a movimentação será registrada e considerada no sistema. Ele deve ser preenchido com a data efetiva em que houve a transferência de numerário, para que os saldos das contas fiquem corretos.

**Tipo de Operação:** informe neste campo a TOP a ser utilizada para a movimentação. Serão disponibilizadas para escolha neste campo, Tipos de Operação cujo Tipo de Movimento seja **"B - Movimento Bancário"**.

**Nr. Documento:** esse campo registra a numeração do documento utilizado para efetuar a movimentação. Se a movimentação foi feita por meio de um cheque, por exemplo, informe aqui o número do cheque; o mesmo deve ocorrer se ela foi feita por depósito bancário, DOC, transferência eletrônica, dentre outros.

**Vlr. Lançamento:** neste campo, o valor da movimentação bancária, ou seja, o montante correspondente a operação que será realizada.

**Histórico:** esse campo é utilizado para registrar um descritivo da operação realizada, com o propósito de facilitar futuras consultas. Por exemplo: "Transferência de fundos para cobertura da conta garantida no Banco A".

**Observação:** quando uma sangria ou suprimento for realizado no [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119653-Central-de-Vendas-PDV-Web), caso não preencha o campo Histórico, ao verificar a conta em que essas ações foram realizadas, na Movimentação Bancária o campo Histórico estará preenchido com o texto **"Histórico Sangria"** ou **"Histórico Suprimento"** conforme a ação realizada. 

**Conta Origem:** informe neste campo, a conta bancária da qual será debitado o valor do lançamento, ou seja, de qual conta sairá o montante a ser transferido.

**Lanç. Origem:** registre neste campo o histórico-padrão do lançamento bancário na conta de origem. Esta informação é cadastrada previamente na tela [Históricos Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694). Neste campo é possível informar apenas históricos com o Tipo do Lançamento igual a **"Débito"**.

**Conta Destino:** neste campo tem-se a conta destino, em que será creditada a quantia movimentada.

**Lanç. Destino:** aqui está o histórico-padrão do lançamento bancário na conta de destino. Esta informação é cadastrada previamente na tela [Históricos Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694). Será possível que você informe apenas históricos com o Tipo do Lançamento igual a **"Crédito"**.

**Observação:** quando o parâmetro **"Cód. lançto p/Suprimento- CODLANCSUPRIME"** estiver configurado com o código do registro cadastrado na tela [Histórico Lançamentos Bancários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606694-Hist%C3%B3ricos-Lan%C3%A7amentos-Banc%C3%A1rios), após a execução da rotina de Suprimento na tela [PDV Web](https://ajuda.sankhya.com.br/hc/pt-br/articles/8046603009047-PDV-Web#Fun%C3%A7%C3%B5esdeCaixa), o campo Lançamento Destino da conta de Sangria/Suprimento será preenchido com o código fornecido no parâmetro.

**Conciliado:** esta marcação se assinalada, estará indicando que a **"Conta de Origem"** do lançamento foi conciliada ([Conciliação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673)).

**Conciliado Destino:** esta marcação se realizada, indicará que a **"Conta de Destino"** do lançamento foi conciliada ([Conciliação Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115673)).

**Vlr. Moeda:** na Movimentação Bancária só haverá a solicitação do valor de moeda, se na [Conta Bancária](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) o campo Moeda presente na aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros) tiver sido informado.

**Nota:** considere ainda que, existem três regras para a utilização de moedas na Movimentação Bancária. São elas:

1. Quando as duas contas possuírem configuração de Moeda, o sistema exibirá uma mensagem informando que uma das contas não deve utilizar Moeda. Pois, nesse caso, a conversão sempre será feita para o Real.

2. Se apenas uma das contas possuir configuração de Moeda, o Vlr. Moeda deve ser maior que zero. Caso contrário, a seguinte mensagem será apresentada:

**"Valor de Moeda deve ser maior que zero".**

Exemplo:

Conta 1 - Moeda = 0 Real
Conta 2 - Moeda = 1 Dolar

Na transferência bancária, a Conta 1 envia R$ 100,00 reais para a conta 2 e informa-se R$5,00 reais no campo Vlr Moeda. Então a conversão será vista no campo Vlr. Lançamento Destino que, nesse caso apresentará R$ 20,00 dólares.

3. Quando as duas contas não possuírem configuração de Moeda, o Vlr. Moeda deve ser zero. Do contrário, o sistema confirmará essa informação por meio de uma mensagem.

É importante ressaltar que as despesas bancárias deverão ser incluídas na movimentação financeira como uma despesa, já que houve saída de numerários da empresa para o ambiente externo.

**Observação:** a duplicação de uma movimentação bancária não preserva a informação dos campos **"Número"** e **"Número do Documento"**.

![Imagem 6: C aso seja necessário determinar com quantas casas decimais o campo VLRMOEDA deve ser arredondado, efetue a…](https://ajuda.sankhya.com.br/hc/article_attachments/21575668831639) Caso seja necessário determinar com quantas casas decimais o campo VLRMOEDA deve ser arredondado, efetue a configuração do parâmetro **"Decimais p/ valores de Moeda - DECVLRMOEDA"** informando a quantidade desejada. Por padrão, este parâmetro é apresentado com a quantidade "5".

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653-Movimenta%C3%A7%C3%A3o-Banc%C3%A1ria#top)

### Exemplos de Movimentação Bancária

Abaixo, é possível analisar alguns exemplos de movimentação bancária ou transferências de numerário:

![Imagem 7: Uma empresa possui R$ 100.000,00 de saldo total em sua conta corrente no Banco A, mas possui um saldo negativo de R$…](https://ajuda.sankhya.com.br/hc/article_attachments/16372627285399) Uma empresa possui R$ 100.000,00 de saldo total em sua conta corrente no Banco A, mas possui um saldo negativo de R$ 10.000,00 em uma conta corrente no Banco B, perfazendo um saldo total de R$ 90.000,00 nas duas contas:

|  | ![Imagem 8: Uma empresa possui R$ 100.000,00 de saldo total em sua conta corrente no Banco A, mas possui um saldo negativo de R$…](https://ajuda.sankhya.com.br/hc/article_attachments/42312493082007) |  |
| --- | --- | --- |

Para saldar o débito da Conta B, o gestor financeiro providencia uma Movimentação Bancária entre as contas, realizando a transferência de numerários no montante de R$20.000,00:

|  | ![Imagem 9: Para saldar o débito da Conta B, o gestor financeiro providencia uma Movimentação Bancária entre as contas, realizando…](https://ajuda.sankhya.com.br/hc/article_attachments/42312480359319) |  |
| --- | --- | --- |

Essa movimentação gera um débito na Conta A e o crédito correspondente na Conta B, de modo que o saldo total da empresa na soma das duas contas permanece o mesmo, ou seja, não houve geração de receita nem despesa.

|  | ![Imagem 10: Essa movimentação gera um débito na Conta A e o crédito correspondente na Conta B, de modo que o saldo total da empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/42312480359959) |  |
| --- | --- | --- |

![Imagem 11: Suponha agora, uma loja que possui 5 caixas onde os clientes fazem o pagamento das compras. No início do dia, não há…](https://ajuda.sankhya.com.br/hc/article_attachments/16372670967447) Suponha agora, uma loja que possui 5 caixas onde os clientes fazem o pagamento das compras. No início do dia, não há dinheiro algum nos caixas, portanto a tesouraria (Caixa Central) faz transferências de numerários para os caixas (uma movimentação para cada caixa), de modo que haja dinheiro para o troco. Ao final do dia, os caixas transferem todo o seu saldo para a tesouraria e, após conferidas todas as movimentações, o caixa central transfere dos recursos para o banco.

|  | ![Imagem 12: Suponha agora, uma loja que possui 5 caixas onde os clientes fazem o pagamento das compras. No início do dia, não há…](https://ajuda.sankhya.com.br/hc/article_attachments/42312493085463) |  |
| --- | --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653-Movimenta%C3%A7%C3%A3o-Banc%C3%A1ria#top)

### Parâmetros que influenciam nessa rotina

**Substitui Conta do Financeiro com Conta Baixa - SUBSTCONTA:** quando este parâmetro está ligado, a conta informada no campo **"Conta"** no momento da [baixa de títulos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600534-Movimenta%C3%A7%C3%A3o-Financeira-Baixa-de-T%C3%ADtulos#top) substituirá a conta registrada no campo **"Conta Baixa"** localizada no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874-Movimenta%C3%A7%C3%A3o-Financeira-Atributos-da-Tela#Principal) da tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Se o parâmetro estiver desligado, mesmo que uma conta diferente seja informada na baixa de títulos, o sistema manterá a conta registrada originalmente no campo Conta Baixa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115653-Movimenta%C3%A7%C3%A3o-Banc%C3%A1ria#top)
