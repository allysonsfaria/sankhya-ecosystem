---
id: "360045115233"
titulo: "Fechamento de Caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115233-Fechamento-de-Caixa"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:09Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "NF-e", "Movimentação Financeira", "Fechamento de Caixa", "Relatório de Caixa", "RELFECHCXLAY2", "br.com.sankhya.rel.fechamento.de.caixa", "Fechamento de Caixa manual", "Financeiro", "Valores de energia água gás seguro e IPTU na aba \"Geral\"", "Informe empreendimento referência e despesa rateável", "Preencha valores específicos e data de pagamento automática"]
---

# Fechamento de Caixa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312475598743) Módulo: Financeiro > Relatórios
```

---

**Importante:** esta tela somente estará disponível caso você possua o opcional Controle de Caixa.

Nesta tela, você poderá visualizar os relatórios de movimentações feitas no caixa.

![Imagem 2: Nesta tela, você poderá visualizar os relatórios de movimentações feitas no caixa.](https://ajuda.sankhya.com.br/hc/article_attachments/360082988133)

Por esta tela, além da possibilidade de criar filtros personalizados, é possível filtrar os movimentos dos caixas por período, através dos campos de data em **"Período da abertura"**.

Em **"Usuários"** é possível também, adicionar vários usuários caixa para serem filtrados de uma única vez.

Ao aplicar os filtros, os caixas são apresentados na grade, onde você poderá visualizar o relatório pelo botão **"Visualizar Relatório"** ou dando duplo clique sobre o caixa desejado.

#### Campos da grade:

**Núm. Caixa:** É o número sequencial que identifica o caixa, alimentado automaticamente a cada abertura de um novo caixa.

**Usuário:** Pessoa que opera o caixa; pode ser exclusivo (informado no cadastro de contas) ou informado ao entrar no sistema.

**Dt. Abertura:** Data e hora de abertura do caixa.

**Dt. Fechamento:** Data e hora de fechamento do caixa.

**Saldo Inicial:** Valor monetário do caixa, retirado do saldo da conta bancária do caixa do último fechamento.

**Observação:**caso seja desejado visualizar o relatório gerado por meio de um segundo tipo de layout, temos o parâmetro **"Relatório de Fechamento de Caixa Layout 2 - RELFECHCXLAY2"** que, ao ser ativado, fará com que as mesmas informações sejam distribuídas e apresentadas em grade, facilitando ainda mais sua interpretação.

**![Imagem 3: Implicações de Movimentos de Devolução no Caixa](https://ajuda.sankhya.com.br/hc/article_attachments/35204780818071) Implicações de Movimentos de Devolução no Caixa**

Ao realizar a **devolução de um cupom ou nota** por meio de um **usuário do tipo caixa**, a movimentação financeira correspondente é registrada e vinculada na tabela de Movimento de Caixa (**TGFMCX**).

Uma vez que este movimento esteja registrado e o **caixa seja fechado**, o sistema **impedirá o cancelamento da Nota Fiscal Eletrônica (NF-e)** de devolução, mesmo que o prazo legal de 24 horas ainda não tenha expirado. A mensagem de erro exibida será: **'O caixa desse cupom já foi fechado.'**. Este comportamento visa garantir a integridade e conciliação dos dados de caixa.

Para permitir o cancelamento da NF-e, o movimento **não pode estar vinculado a um caixa fechado**. Caso a devolução precise ser cancelada, o ideal é que o movimento **não seja feito por um usuário que participe da rotina de fechamento de caixa** ou que o cancelamento seja efetuado **antes do fechamento do caixa** que registrou a devolução.

#### Critérios de Impressão

![Imagem 4: Critérios de Impressão](https://ajuda.sankhya.com.br/hc/article_attachments/360081867494)

Em **"Critérios de Impressão"**, você pode configurar como deseja imprimir o relatório.

**Créditos/Débitos:** Essa parte do relatório exibe as movimentações que causaram alterações no saldo do caixa, como baixas, movimentações bancárias, etc. As movimentações bancárias são discriminadas pelo histórico do lançamento bancário.

Este campo possui as seguintes opções:

- **Não imprimir:** Com essa opção, o sistema não apresentará a parte de créditos e débitos no relatório.
- **Imprimir por Tipo de Título:** Com essa opção, o sistema apresentará no relatório os débitos e créditos, quebrando por tipo de título. Isso possibilita que você veja o quanto recebeu em dinheiro, cheque etc.

![Imagem 5: As transações realizadas via PIX não serão incluídas, nem somados ao "Vlr. Bruto Recebido" no relatório.](https://ajuda.sankhya.com.br/hc/article_attachments/29451415208343) As transações realizadas via PIX não serão incluídas, nem somados ao **"Vlr. Bruto Recebido"** no relatório.

Será possível ainda efetuar a marcação **"Analítico?"**, utilizado para mostrar no relatório os dados dos débitos e créditos, como Número da Nota, Cód. Parceiro, Data Alteração etc.

**Vendas:** Nessa área do relatório, o sistema exibe todas as movimentações feitas pela central de clientes, confirmação de pedidos e notas.

Abaixo, temos as opções disponíveis neste campo:

- **Não imprimir:** Se selecionado, a área de vendas não será apresentada no relatório.
- **Imprimir por Tipo de Operação:** Permite que você veja as movimentações por tipo de operação. Exemplo: Pedidos, Vendas etc.
- **Imprimir por Tipo de Negociação:** Se selecionado, os dados no relatório de vendas serão apresentados quebrando por tipo de negociação. Permite que você possa ver, por exemplo, o quanto vendeu a vista, a prazo, 30 dias etc.
- **Imprimir por Tipo de Título:** Permite que você veja as movimentações por tipo de título.

A marcação Analítico? fará com que o sistema mostre o número de cada nota e valor, no relatório.

**Produtos:** Apresenta a quantidade negociada pelo caixa por produto e grupo de produtos. Neste, tempos as opções a seguir:

- **Não imprimir:** Se selecionado, o sistema não apresentará os dados no relatório por produtos e grupos.
- **Imprimir por ambos:** Se selecionado, serão apresentados os dados das negociações por produtos e grupos, no relatório.
- **Imprimir por Produtos:** Marcando-se esta opção, serão exibidos as informações das negociações apenas por produtos.
- **Imprimir por Grupos:** Por esta opção, serão apresentadas as informações das negociações apenas por grupos.

A marcação Analítico? poderá ser realizada para mostrar as notas, respectiva quantidade e valor de produtos negociados pelo caixa.

Quando a marcação **"Créditos Compensados"** for selecionada, o sistema exibirá no relatório os créditos financeiros compensados durante a operação de caixa.
