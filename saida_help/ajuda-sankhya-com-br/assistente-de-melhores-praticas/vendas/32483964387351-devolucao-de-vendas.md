---
id: "32483964387351"
titulo: "Devolução de Vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32483964387351-Devolu%C3%A7%C3%A3o-de-Vendas"
trilha: "Assistente de Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:31:05Z"
rotulos: ["Configuração", "Portal de Vendas", "Vendas", "Estoque", "Financeiro", "Documentos Eletrônicos"]
---

# Devolução de Vendas

### Descrição

A funcionalidade **Devolução de Vendas** permite configurar os acessos, parâmetros e tipos de operação necessários para o registro de devoluções de produtos vendidos, assegurando o correto cumprimento das obrigações fiscais, atualização de estoque e registros financeiros.

Ela oferece os seguintes recursos:

- **Gestão de Devoluções**: Permite consultar, incluir, alterar, excluir e configurar registros de devolução de vendas.
- **Liberação de Acessos**: Garante aos usuários selecionados o acesso às telas e rotinas relacionadas à devolução de vendas.
- **Tipos de Operação Pré-configurados**: Inclui automaticamente os Tipos de Operação (TOPs) necessários ao processo de devolução de vendas.
- **Configuração de Numeração**: Cria bases de numeração para as notas fiscais de devolução, caso não existam.
- **Parâmetros de Crédito**: Habilita regras para uso e compensação automática de créditos gerados por devolução.
- **Criação do Tipo de Título "Crédito de Clientes"**, caso ainda não exista no sistema.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **usuários ou grupos** responsáveis pelo lançamento das devoluções de vendas.
3. Clique em **"Avançar"** para revisar as configurações selecionadas.
4. Clique em **"Instalar"** para concluir a instalação.

### Detalhes da Instalação

**Acessos liberados**

- **Portal de Vendas**
  - Caminho: Comercial » Consulta » Portal de Vendas
  - Permissões: Incluir, Alterar, Consultar
- **Devolução de Vendas (Tipo de Movimento)**
  - Caminho: Comercial » Rotinas » Portal de Vendas » Devoluções
  - Permissões: Incluir, Alterar, Consultar, Excluir, Configurar, Numeração, Cancelar, Imprimir/Reimprimir, Rateio, Campos Adicionais

**Tabelas atualizadas**

- **TSIUSU – Cadastro de Usuários**
  - Remoção da restrição "Inibe acesso às vendas".
- **TGFTOP – Tipos de Operação**
  - Inclusão automática das TOPs de devolução da base modelo:
    - 1201, 1202, 1297, 1298, 1703 (compensação despesa), 1753 (compensação receita).
- **TGFNUM – Numeração**
  - Criação das bases de numeração "VENDA" e "Sem Numeração", se não existirem.
- **TSITIPTIT – Tipos de Título**
  - Criação do tipo de título **"CRÉDITO DE CLIENTES"**, caso ainda não exista.
- **TSIPAR – Parâmetros do Sistema**
  - AVISARCREDCLI - Avisar que o Cliente Possui Crédito = Ligado.
  - TIPTITCREDCLI - Tipo de Título para Compensação de Crédito = Código do tipo "CRÉDITO DE CLIENTES".
  - COMPENSACREDCLI - Compensar Crédito de Cliente Automaticamente = Desligado.
  - COMPDEVEMP - Compensar Dev.somente na mesma Empresa? = Ligado.
  - TOPBAIRECDEV - TOP baixa da receita na compensação de devolução = 1753.
  - TOPBAIDESPDEV - TOP baixa da despesa na compensação de devolução = 1703.
  - TOPBAIRECCOMP - Top Baixa de Receita de Compensação de Crédito = 1753.
  - TOPBAIDESPCOMP - Top Baixa de Despesa de Compensação de Crédito = 1703.
