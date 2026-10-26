---
id: "32774891104151"
titulo: "Transferências de Estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32774891104151-Transfer%C3%AAncias-de-Estoque"
trilha: "Assistente de Melhores Práticas > Estocagem"
atualizado_em: "2026-09-28T15:53:21Z"
rotulos: ["Produtos", "Configuração", "WMS", "Movimentação Financeira", "TOP", "Estoque"]
---

# Transferências de Estoque

### Descrição

A funcionalidade **Transferências de Estoque** permite configurar e gerenciar as transferências de produtos entre diferentes locais de estoque ou entre empresas do grupo, garantindo controle adequado da movimentação de mercadorias.

Ela oferece os seguintes recursos:

- **Criação de Tipos de Operação (TOP):** Gera automaticamente os TOPs necessários para transferências internas (entre locais) e entre filiais.
- **Controle de Numeração:** Cria bases de numeração específicas para cada tipo de movimentação, respeitando regras fiscais e organizacionais.
- **Liberação de Acessos:** Concede permissões nos principais portais de movimentação (internas, vendas e compras) para os usuários selecionados.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **usuários e/ou grupos** responsáveis pela realização de transferências.
3. Clique em **"Avançar"**.
4. Revise o **resumo** com as informações configuradas para instalação.
5. Clique em **"Instalar"** para concluir.

### Detalhes da instalação

**Acessos liberados**

- **Portal de Movimentações Internas:** Consultar, Incluir, Alterar
- **Transferência (Central):** Consultar, Incluir, Alterar, Altera ligação entre documentos, Rateio, Imprimir/Reimprimir
- **Portal de Compras:** Consultar, Incluir, Alterar
- **Notas de Compra:** Consultar, Incluir, Alterar, Altera ligação entre documentos, Rateio, Imprimir/Reimprimir
- **Portal de Vendas:** Consultar, Incluir, Alterar
- **Notas de Venda:** Consultar, Incluir, Alterar, Altera ligação entre documentos, Rateio, Imprimir/Reimprimir

**Tabelas atualizadas**

- **TGFTOP – Tipos de Operação:**
  - Inclusão das TOPs: **1950** (Transferência entre Locais), **1452** (Transferência entre Filiais - Entrada) e **1152** (Transferência entre Filiais - Saída).
  - Atualização do campo **ATIVO** para ativar as TOPs inseridas.
- **TGFNUM – Numeração:**
  - Criação das bases de numeração para as operações:
  - **'TOP-1950'** – específica para a TOP 1950.
  - **'SEMNUM'** – base de numeração manual.
  - **'VENDA'** – padrão com série 1.

**Vale saber**

As transferências de estoque são cruciais para otimizar a movimentação de produtos. Ao configurá-las corretamente, você garante um controle preciso do seu inventário e agiliza as operações entre diferentes locais ou filiais, impactando positivamente suas estratégias de vendas e compras.
