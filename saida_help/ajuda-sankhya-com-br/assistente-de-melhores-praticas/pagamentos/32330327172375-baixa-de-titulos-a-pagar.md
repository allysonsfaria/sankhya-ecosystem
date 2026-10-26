---
id: "32330327172375"
titulo: "Baixa de Títulos a pagar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32330327172375-Baixa-de-T%C3%ADtulos-a-pagar"
trilha: "Assistente de Melhores Práticas > Pagamentos"
atualizado_em: "2026-07-22T14:31:44Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "TOP", "Financeiro"]
---

# Baixa de Títulos a pagar

### Descrição

A funcionalidade **Baixa de Títulos a pagar** permite configurar os processos de pagamento de contas a pagar, definindo os usuários responsáveis e liberando os acessos necessários para a execução da operação.

Ela oferece os seguintes recursos:

- **Gestão de Baixa de Títulos a Pagar**: Permite aos usuários consultar, incluir, alterar e excluir registros de baixa, controlando os pagamentos realizados.
- **Configuração de Tipos de Operação (TOP)**: Cria e ativa a TOP **"1700 - Pagamentos"**, usada para categorizar todas as operações de baixa no sistema.
- **Liberação de Acessos e Permissões**: Atualiza as permissões dos usuários e libera o acesso à funcionalidade de baixa de títulos.
- **Ajustes no Cadastro de Usuários**: Garante que os usuários não estejam com o campo "Inibe acesso a despesas" habilitado.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os grupos e/ou usuários responsáveis pela baixa de contas a pagar.
3. Clique em **"Avançar"**.
4. Revise o resumo com os grupos e usuários selecionados.
5. Clique em **"Instalar"**.

### Detalhes da instalação

**Acessos liberados**

- **Movimentação Financeira**
  Caminho: Financeiro » Rotinas » Movimentação Financeira
  Permissões: Acesso à consulta e baixa de contas a pagar.

**Tabelas Atualizadas**

- **TGFTOP – Tipos de Operação**
  - Inclusão e ativação da TOP **"1700 – Pagamentos"**, com base na base modelo.
  - Caso não exista, a TOP é criada com todos os campos padrões definidos para a categoria "Financeiro".
- **TSIUSU – Cadastro de Usuários**
  - Atualização do campo "Inibe acesso a despesas" para **"Não"** nos usuários selecionados.
