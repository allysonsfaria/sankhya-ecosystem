---
id: "37672563090455"
titulo: "Como validar estoque de produtos no pedido de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37672563090455-Como-validar-estoque-de-produtos-no-pedido-de-venda"
trilha: "Universidade Sankhya > Jornada de Vendas"
atualizado_em: "2026-07-22T14:10:56Z"
rotulos: ["Produtos", "Configuração", "Portal de Vendas", "TOP", "Estoque"]
---

# Como validar estoque de produtos no pedido de venda

| Categoria |
| --- |
| [Cenário prático de como validar estoque de produtos no pedido de venda:](https://ajuda.sankhya.com.br/hc/pt-br/articles/37672563090455-Como-validar-estoque-de-produtos-no-pedido-de-venda#h_01KEYQ4GSBXRT1QJQNB4JDZ7B3) |
| [Chegou a sua vez! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37672563090455-Como-validar-estoque-de-produtos-no-pedido-de-venda#h_01KEYQ4S6BVZE5HGW6YTY92K4R) |
| [Cenário Prático Como validar Estoque por Empresa/Local no Pedido de Venda:](https://ajuda.sankhya.com.br/hc/pt-br/articles/37672563090455-Como-validar-estoque-de-produtos-no-pedido-de-venda#h_01KEYPNZWETTGVNYAZGHN83269) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37672563090455-Como-validar-estoque-de-produtos-no-pedido-de-venda#h_01KEYPJV1PPJAWTK938G7RR8XF) |

## Validar estoque de produtos no pedido de venda e por Empresa/Local

#### Cenário prático de como validar estoque de produtos no pedido de venda:

**Contexto:** Na empresa **ABC Corp.**, o responsável pelo controle de estoque precisa garantir que os produtos tenham saldo positivo no momento da venda, evitando problemas na hora de efetivar os pedidos. No entanto, a configuração atual do ERP Sankhya permite a realização de vendas mesmo quando o estoque está zerado ou negativo.

Isso significa que, em algumas situações, um pedido pode ser registrado com uma quantidade maior do que a disponível no estoque, o que pode gerar divergências no controle e na reposição de mercadorias.

**Tarefa:** Crie um novo pedido de venda e insira uma quantidade de produtos maior do que o disponível no estoque. Observe o comportamento do sistema ao permitir essa venda e reflita sobre os impactos dessa prática na gestão de estoque.

#### Chegou a sua vez! Realize as movimentações no ERP Sankhya

1. **Validação do Produto**

- Acesse a tela **Produtos**
  Menu: Configurações » Cadastros » Produtos
- Selecione o produto e dê um **duplo clique** para abrir as configurações.
- Na aba **Geral**, no campo **Grupo**, verifique a qual grupo o produto está vinculado.

2. **Grupos de Produtos/Serviços**

- Acesse a tela **Grupos de Produtos/Serviços**
  Menu: Configurações » Cadastros » Produtos
- Digite o grupo vinculado ao produto que pesquisou anteriormente.
- Na Aba **Estoque,** no campo **Valida estoque**, selecione a opção **Pela Empresa, mas aceita.** Dessa forma, será permitido seguir com a venda do produto deixando o estoque negativo, se por acaso ele não for suficiente.

3. **Consulta de Produtos**

- Acesse a tela **Consulta de Produtos**
  Menu: Comercial » Consulta » Consulta de Produtos
- No campo **Buscar**, digite o nome do produto e pressione **Enter** para carregar as informações.
- Na sub-Aba **Detalhes de Estoque**, você poderá visualizar a quantidade disponível do produto em estoque.

4. **Registrar o pedido de venda**

- Acesse a tela **Portal de Vendas**
  Menu: Comercial » Consulta » Portal de Vendas
- No campo **Tipo de Movimento**, selecione a opção **Pedido de Venda**.
- Clique no ícone ao lado do campo e escolha a **TOP de “Pedido de Venda”**.
- Dê um duplo clique e o sistema redirecionará para a **Central de Vendas**

5. **Preencher o Cabeçalho do Orçamento**
   Na **Central de Vendas**, preencha os seguintes campos obrigatórios:

- **Empresa**: Selecionar a empresa responsável pela operação.
- **Parceiro**: Informar o cliente ou parceiro de negócio.
- **Tipo de Operação**: Escolher “**Pedido de Venda”**.
- **Tipo de Negociação**: Informar a modalidade de negociação acordada.
- **Vendedor**: Selecionar o vendedor responsável pela negociação.
- **Natureza**: Preencher este campo caso a preferência **EXIGNATCFR** (Exigir natureza na central/financeiro/rateio) esteja ativada.
- **Centro de Resultado (CR)**: Informar o centro de resultado, caso a preferência **EXIGCRCFR** esteja ativada.
- Após preencher todos os campos, clique em **Salvar[F7]** para registrar as informações.

6. **Preencher o painel de Itens**
   **No painel de itens, insira as seguintes informações obrigatórias:**

- **Produto**: Adicionar o produto negociado.
- **Controle**: Preencher este campo se houver necessidade de controle específico.
- **Local**: Informar o local, caso o produto exija essa configuração.
- **Quantidade**: Registrar a quantidade maior que a disponível no local.
- **Valor Unitário**: Inserir o valor acordado por unidade.
- Clique em **Salvar[F7]** para registrar os itens no orçamento.
- Apresentará um pop-up com a seguinte informação **(Não há estoque suficiente para “ \_” Deseja efetivá-lo?)**
- Com essa mensagem o sistema está validando o estoque.

7. **Validação final**
   **No rodapé, revise as informações relacionadas a:**

- **Transporte**: Confirme os dados de frete ou transporte.
- **Impostos**: Valide a aplicação correta dos tributos.
- **Financeiro**: Certifique-se de que as condições de pagamento estão corretas.
- Se todas as informações estiverem corretas, clique no botão **"Confirmar"** para validar o pedido de venda.

#### Cenário Prático Como validar Estoque por Empresa/Local no Pedido de Venda:

**Contexto:** Na empresa **ABC Corp.**, o responsável pelo controle de estoque precisa garantir que os produtos tenham saldo positivo no momento da venda, evitando problemas na hora de efetivar os pedidos. No entanto, considerando o controle por local e um estoque negativo, não será possível realizar a venda.

**Tarefa:** Crie um novo pedido de venda e insira uma quantidade de produtos maior do que o disponível no estoque. Observe o comportamento do sistema ao permitir essa venda e reflita sobre os impactos dessa prática na gestão de estoque.

**Chegou a sua vez! Realize as movimentações no ERP Sankhya**

1. **Validação do Produto**

- Acesse a tela **Produtos**
  Menu: Configurações » Cadastros » Produtos
- Selecione o produto e dê um **duplo clique** para abrir as configurações.
- Na aba **Geral**, no campo **Grupo**, verifique a qual grupo o produto está vinculado.

2. **Grupos de Produtos/Serviços**

- Acesse a tela **Grupos de Produtos/Serviços**
  Menu: Configurações » Cadastros » Produtos
- Digite o grupo vinculado ao produto que pesquisou anteriormente.
- Na Aba **Estoque,** no campo **Valida estoque**, selecione a opção **Empresa/Local.** Assim, o sistema irá impedir que o registro do item seja salvo, caso a quantidade disponível no local informado seja insuficiente.

3. **Consulta de Produtos**

- Acesse a tela **Consulta de Produtos**
  Menu: Comercial » Consulta » Consulta de Produtos
- No campo **Buscar**, digite o nome do produto e pressione **Enter** para carregar as informações.
- Na sub-Aba **Detalhes de Estoque**, você poderá visualizar a quantidade disponível do produto em estoque.

4. **Registrar o pedido de venda**

- Acesse a tela **Portal de Vendas**
  Menu: Comercial » Consulta » Portal de Vendas
- No campo **Tipo de Movimento**, selecione a opção **Pedido de Venda**.
- Clique no ícone ao lado do campo e escolha a **TOP de Pedido de Venda**.
- Dê um duplo clique e o sistema redirecionará para a **Central de Vendas**.

5. **Preencher o Cabeçalho do Orçamento**
   Na **Central de Vendas**, preencha os seguintes campos obrigatórios:

- **Empresa**: Selecionar a empresa responsável pela operação.
- **Parceiro**: Informar o cliente ou parceiro de negócio.
- **Tipo de Operação**: Escolher “**Pedido de Venda”**.
- **Tipo de Negociação**: Informar a modalidade de negociação acordada.
- **Vendedor**: Selecionar o vendedor responsável pela negociação.
- **Natureza**: Preencher este campo caso a preferência **EXIGNATCFR** (Exigir natureza na central/financeiro/rateio) esteja ativada.
- **Centro de Resultado (CR)**: Informar o centro de resultado, caso a preferência **EXIGCRCFR** esteja ativada.
- Após preencher todos os campos, clique em **Salvar[F7]** para registrar as informações.

6. **Preencher o painel de Itens**
   **No painel de itens, insira as seguintes informações obrigatórias:**

- **Produto**: Adicionar o produto negociado.
- **Controle**: Preencher este campo se houver necessidade de controle específico.
- **Local**: Informar o local, caso o produto exija essa configuração.
- **Quantidade**: Registrar a quantidade maior que a disponível no estoque.
- **Valor Unitário**: Inserir o valor acordado por unidade.
- Clique em **Salvar[F7]** para registrar os itens no orçamento.

**O sistema exibirá um pop-up com a seguinte mensagem:**

- **Aviso:** Estoque insuficiente.
- **Empresa:** [Nome da empresa]
- **Produto:** [Nome do produto]
- **Local:** [Local do estoque]

**Essa mensagem indica que o sistema está validando o estoque, impedindo o salvamento do produto caso a quantidade disponível no local informado seja insuficiente.**

#### Correção e Repetição

- Certifique-se de que o grupo do produto foi corretamente identificado na aba **Geral** antes de prosseguir com a validação do estoque.
- Verifique se a opção de **validação de estoque** foi selecionada corretamente na aba **Estoque** dentro da tela **Grupos de Produtos/Serviços**.
- Confirme se a consulta de produtos exibe a quantidade correta de estoque disponível antes de lançar o pedido de venda.
- Caso a validação do estoque não ocorra conforme esperado, revise as configurações de validação no grupo do produto e tente novamente.

Para reforçar o aprendizado, realize o processo novamente utilizando um produto diferente e valide as configurações de estoque.
