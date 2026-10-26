# Tabelas Essenciais do Sankhya OM (Cheat Sheet)

Guia rápido com as principais tabelas, chaves primárias e campos indispensáveis para consultas e integrações.

---

## 1. Comercial e Movimentações

### TGFCAB (Cabeçalho da Nota / Pedido)
- **PK**: `NUNOTA` (Número Único da Nota)
- **Campos Principais**:
  - `CODPARC`: Código do Parceiro (FK `TGFPAR`)
  - `CODEMP`: Empresa emissora (FK `TSIEMP`)
  - `CODTIPOPER`: Tipo de Operação / TOP (FK `TGFTOP`)
  - `DHTIPOPER`: Data/hora do tipo de operação
  - `TIPMOV`: Tipo do Movimento (`V`=Venda, `C`=Compra, `P`=Pedido Venda, `O`=Pedido Compra, `D`=Devolução Venda, `E`=Devolução Compra)
  - `STATUSNOTA`: Status (`A`=Pendente, `L`=Confirmada, `C`=Cancelada)
  - `DTNEG`: Data de Negociação
  - `VLRNOTA`: Valor Total da Nota
  - `NUMNOTA`: Número da Nota Impressa / NF-e

### TGFITE (Itens da Nota / Pedido)
- **PK Composta**: `NUNOTA`, `SEQUENCIA`
- **Campos Principais**:
  - `CODPROD`: Código do Produto (FK `TGFPRO`)
  - `QTDNEG`: Quantidade Negociada
  - `VLRUNIT`: Valor Unitário
  - `VLRTOT`: Valor Total do Item
  - `CODVOL`: Unidade de Medida (FK `TGFVOL`)
  - `PERCDESC`: Percentual de Desconto
  - `VLRDESC`: Valor do Desconto

---

## 2. Cadastros Gerais

### TGFPAR (Parceiros: Clientes, Fornecedores, Vendedores)
- **PK**: `CODPARC`
- **Campos Principais**:
  - `NOMEPARC`: Nome / Razão Social
  - `RAZAOSOCIAL`: Nome Fantasia
  - `TIPPESSOA`: `F` (Física) ou `J` (Jurídica)
  - `CGC_CPF`: CNPJ ou CPF (apenas números)
  - `IDENTINSCEST`: Inscrição Estadual
  - `CODCID`: Cidade (FK `TSICID`)
  - `CODBAI`: Bairro (FK `TSIBAI`)
  - `CODEND`: Endereço / Logradouro (FK `TSIEND`)
  - `NUMEND`: Número do endereço
  - `CLIENTE`, `FORNECEDOR`, `VENDEDOR`, `TRANSPORTADORA`: Flags (`S` ou `N`)
  - `ATIVO`: Ativo (`S` ou `N`)

### TGFPRO (Produtos e Serviços)
- **PK**: `CODPROD`
- **Campos Principais**:
  - `DESCRPROD`: Descrição do Produto
  - `CODVOL`: Unidade padrão (FK `TGFVOL`)
  - `CODGRUPOPROD`: Grupo de Produtos (FK `TGFGRU`)
  - `MARCA`: Marca do produto
  - `USOPROD`: Uso do Produto (`R`=Revenda, `M`=Matéria-Prima, `S`=Serviço, `I`=Imobilizado, `C`=Consumo)
  - `ATIVO`: Ativo (`S` ou `N`)
  - `NCM`: Código Fiscal NCM

---

## 3. Financeiro

### TGFFIN (Títulos Financeiros)
- **PK**: `NUFIN`
- **Campos Principais**:
  - `NUNOTA`: Número da Nota de origem (FK `TGFCAB`, nulo se avulso)
  - `CODPARC`: Parceiro (FK `TGFPAR`)
  - `CODEMP`: Empresa (FK `TSIEMP`)
  - `CODTIPTIT`: Tipo de Título (FK `TGFTIT`, ex: Boleto, Cartão, Dinheiro)
  - `CODNAT`: Natureza Financeira (FK `TGFNAT`)
  - `RECDESP`: Receita ou Despesa (`1`=Receita, `-1`=Despesa)
  - `DTNEG`: Data de Negociação
  - `DTVENC`: Data de Vencimento
  - `DHBAIXA`: Data/Hora da Baixa (nulo se pendente)
  - `VLRDESDOB`: Valor Nominal / Desdobramento
  - `VLRBAIXA`: Valor Pago / Baixado

---

## 4. Estoque

### TGFEST (Saldos de Estoque)
- **PK Composta**: `CODEMP`, `CODPROD`, `CODLOCAL`, `CONTROLE`
- **Campos Principais**:
  - `ESTOQUE`: Saldo Atual em Estoque
  - `RESERVADO`: Quantidade Reservada em Pedidos Pendentes
  - `WMSBLOQUEADO`: Saldo Bloqueado pelo WMS
