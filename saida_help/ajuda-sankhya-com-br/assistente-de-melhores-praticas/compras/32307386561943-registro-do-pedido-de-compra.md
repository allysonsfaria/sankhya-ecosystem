---
id: "32307386561943"
titulo: "Registro do Pedido de compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32307386561943-Registro-do-Pedido-de-compra"
trilha: "Assistente de Melhores Práticas > Compras"
atualizado_em: "2026-09-30T21:38:41Z"
rotulos: ["Configuração", "Parceiro", "Pedido de Compra", "TOP", "Estoque", "Financeiro"]
---

# Registro do Pedido de compra

### Descrição

Permite o lançamento de pedidos de compra, abrangendo desde a coleta e inserção de dados até a revisão, aprovação e envio. Com isso, garante **flexibilidade, controle, adaptabilidade e precisão** no processo.

**Recursos Disponíveis**

- **Consulta ao Portal de Compras:** Usuários selecionados podem acessar e consultar os pedidos de compra.
- **Vinculação do Comprador ao Pedido:** Compradores são automaticamente vinculados aos pedidos que adicionam.
- **Configuração do Tipo de Operação:** Define os tipos de operação para pedidos de compra, facilitando o controle das despesas provisionadas. Isso melhora o fluxo de caixa e a gestão do estoque da empresa.

### Como instalar

1. Clique em **"Iniciar"**.

2. Selecione os usuários e/ou grupos de usuários que atuam como compradores na organização.

3. Escolha se deseja registrar o comprador responsável nos pedidos, selecionando **"Sim"** ou **"Não"**.

4. Revise o resumo das informações para configuração.

5. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Para cada usuário comprador informado, o sistema realiza os acessos abaixo:**

- **TGFVEN** – Cadastro de Comprador (se aplicável)
- **TSIUSU** – Vinculação do comprador ao campo **"Vendedor"** no cadastro de usuário
- **TDDPER** – Liberação de acesso para consulta, inclusão, impressão e rateio de pedidos no **Portal de Compras**

**Outras Tabelas Atualizadas**

- **TGFTOP** – Ativação e ajustes na **TOP 1301 – Pedido de Compra (Revenda)** (se existente)
- **TGFNUM** - Ajustes na numeração da TOP para as empresas existentes

### Como simular

O registro do pedido mantém um histórico para futuras consultas e negociações com fornecedores.

**Como acessar:**

Vá para Comercial \> Consulta \> Portal de Compras.

1-Na tela Portal de Compras.

2-No campo Tipo de Movimento, selecione Pedido de Compra.

3-Clique na seta ao lado do ícone correspondente e escolha a TOP de Pedido de Compra.

**O sistema abrirá a tela Central de Compras para preenchimento das informações.**

**Preenchimento do cabeçalho:**

Informe os seguintes campos e clique em **Salvar**:

- Empresa.
- Parceiro.
- Tipo de Operação.
- Tipo de Negociação.
- Data de Negociação (Dt. Neg.).
- Natureza (obrigatório se a preferência EXIGNATCFR estiver ativada).
- Centro de Resultado (obrigatório se a preferência EXIGCRCFR estiver ativada).

**Preenchimento dos itens:**

No painel de Itens, informe os seguintes campos e clique em **Salvar**:

- Produto.
- Controle (se aplicável).
- Local (se configurado para uso).
- Quantidade.
- Valor Unitário (Vlr. unitário).

Verifique as informações do rodapé: Transporte, Impostos e Financeiro. Se estiverem corretas, clique em Confirmar para concluir o processo.

**Vale saber**

Registrar os pedidos de compra direto pelo sistema ajuda a organizar melhor as negociações com fornecedores e dá mais previsibilidade ao fluxo de caixa. Se você marcar que deseja vincular o comprador, o sistema vai registrar automaticamente quem está por trás de cada pedido — isso traz mais rastreabilidade e facilita o acompanhamento depois.

E lembre: quanto mais completo o preenchimento, mais precisas serão as análises futuras!
