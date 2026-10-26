---
id: "32378155158423"
titulo: "Provisões e Contas a pagar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32378155158423-Provis%C3%B5es-e-Contas-a-pagar"
trilha: "Assistente de Melhores Práticas > Pagamentos"
atualizado_em: "2026-07-22T14:31:36Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "TOP", "Financeiro"]
---

# Provisões e Contas a pagar

### Descrição

A funcionalidade **Provisões/Contas a Pagar** permite configurar os processos de lançamento de contas a pagar, tanto de valores reais quanto de provisões, definindo os responsáveis pela operação e liberando os acessos necessários para sua execução.
Libera acesso a:

- **Gestão de Movimentação Financeira:** Permite aos usuários consultar, incluir, alterar e excluir registros relacionados aos lançamentos de contas a pagar, tanto reais quanto provisões.
- **Configuração de Tipos de Operação (TOP):** Libera a criação e personalização do tipo de operação **"Lançamentos Financeiros"**, caso não exista. A TOP 1600 - Lançamentos - Financeiros é criada para controlar e categorizar todas as operações de lançamento de contas a pagar no sistema.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **grupos e/ou usuários** responsáveis pela baixa de contas a pagar.
3. Clique em **"Avançar"**.
4. Revise o **resumo com os grupos e usuários selecionados**.
5. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- **Movimentação Financeira**
  **Caminho:** Financeiro » Rotinas » Movimentação Financeira
  **Permissões:** Acesso à consulta e baixa de contas a pagar.

**Tabelas Atualizadas**

- **TGFTOP – Tipos de Operação**
  Inclusão e ativação da **TOP 1600 – Lançamentos Financeiros**, com base na base modelo.
  Caso não exista, a TOP é criada com todos os campos padrões definidos para a categoria **"Financeiro"**.

- **TSIUSU – Cadastro de Usuários**
  Atualização do campo **"Inibe acesso a despesas"** para **"Não"** nos usuários selecionados.
