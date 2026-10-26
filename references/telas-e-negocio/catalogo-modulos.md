# Catálogo de Módulos e Fluxos de Negócio (Sankhya OM)

Visão holística dos módulos operacionais e do encadeamento de dados no ERP.

---

## 1. Mapa dos Módulos Principais

### A. Comercial (Vendas e Compras)
- **Central de Vendas**: orçamentos, pedidos, notas fiscais de venda, devoluções.
- **Central de Compras**: cotações, pedidos de compra, notas de entrada de mercadorias.
- **Tabelas Centrais**: `TGFCAB` (cabeçalho), `TGFITE` (itens), `TGFFIN` (financeiro vinculado), `TGFVAR` (variação/ligação entre notas pai e filhas).

### B. Financeiro
- **Movimentação Financeira**: títulos de contas a pagar (`RECDESP = -1`) e a receber (`RECDESP = 1`).
- **Contas Bancárias e Conciliação**: extratos, lançamentos em conta (`TSICTA`, `TGFMBC`).
- **Tabela Central**: `TGFFIN`. Campos chave: `NUFIN`, `CODPARC`, `DTVENC`, `VLRDESDOB`, `DHBAIXA`, `VLRBAIXA`.

### C. Suprimentos e Estoque
- **Movimentação de Estoque**: kardex e saldos por empresa/local.
- **Tabelas Centrais**: `TGFEST` (saldo atual), `TGFCAB` + `TGFITE` (movimentações), `TGFLOC` (locais de estoque).

### D. Fiscal e Tributário
- **Apuração de Impostos**: ICMS, IPI, PIS, COFINS, ISS.
- **Emissão Eletrônica**: NF-e, NFS-e, CT-e, MDF-e.
- **Tabelas Centrais**: `TGFDIN` (detalhes de impostos da nota), `TGFNFSE` (dados específicos de NFS-e).

---

## 2. Fluxo Transacional Integrado (Life of a Transaction)

```
1. Pedido de Venda (TGFCAB / TIPMOV = 'P')
   ↓
2. Faturamento / Confirmação de Nota (TGFCAB / TIPMOV = 'V')
   ├── Baixa de Estoque (TGFEST atualizado pelo motor do Sankhya)
   ├── Geração do Título Financeiro a Receber (TGFFIN)
   ├── Apuração Fiscal dos Itens (TGFDIN)
   └── Transmissão do XML para a SEFAZ
```

Quando desenvolver regras de negócio ou extensões, compreenda em qual ponto do ciclo o código atuará:
- Validação prévia de itens: `@Listener` em `ItemNota` (`beforeInsert`/`beforeUpdate`).
- Bloqueio comercial ou alçada: `@BusinessRule` ou `@Listener` em `CabecalhoNota` (`beforeUpdate`).
- Ações pós-confirmação: `@Callback` ou `@Listener` (`afterUpdate` com checagem de `STATUSNOTA = 'L'`).
