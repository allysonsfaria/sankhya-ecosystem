---
id: "32379653390743"
titulo: "Provisões e Contas a receber"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32379653390743-Provis%C3%B5es-e-Contas-a-receber"
trilha: "Assistente de Melhores Práticas > Recebimentos"
atualizado_em: "2026-07-22T14:31:34Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "Contas a Receber"]
---

# Provisões e Contas a receber

### Descrição

A funcionalidade **Provisões e Contas a Receber** permite configurar e liberar acessos para usuários responsáveis pelos lançamentos de contas a receber, sejam reais ou provisões, garantindo o controle adequado na movimentação financeira.

Libera acesso a:

- **Movimentação Financeira**: Permite realizar, alterar e consultar lançamentos de contas a receber no sistema.
- **Tipo de Operação "Lançamento Financeiro"**: Criação e utilização do tipo de operação específico para lançamentos financeiros, incluindo provisões e contas reais.
- **Acessos e permissões**: Ajustes nas permissões de usuários, removendo restrições e liberando acesso para ações financeiras essenciais.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **grupos e/ou usuários** responsáveis pela baixa de contas a receber.
3. Clique em **"Avançar"**.
4. Revise o **resumo com os grupos e usuários selecionados**.
5. Clique em **"Instalar"**.

### Detalhes da instalação

**Acessos liberados**

- **Movimentação Financeira**\*\*
  **Caminho**: Financeiro » Rotinas » Movimentação Financeira
  **Permissões**: Acesso à consulta e baixa de contas a receber.

**Tabelas Atualizadas**

- **TGFTOP – Tipos de Operação**\*\*
  - Inclusão e ativação da **TOP 1600 – Lançamentos Financeiros**, com base na base modelo.
  Caso não exista, a TOP é criada com todos os campos padrões definidos para a categoria **"Financeiro"**.
- **TSIUSU – Cadastro de Usuários**\*\*
  - Atualização do campo **"Inibe acesso às receitas"** para **"Não"** nos usuários selecionados.
