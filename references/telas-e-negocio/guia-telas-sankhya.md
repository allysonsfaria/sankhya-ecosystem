# Guia de Funcionamento das Telas do Sankhya OM

As telas do ERP Sankhya OM operam sobre o Dicionário de Dados e o motor dinâmico DWF (Data Warehouse Framework).

---

## 1. Arquitetura Padrão de Tela no Sankhya OM

Toda tela nativa do Sankhya segue uma estrutura modular composta por:

1. **Barra de Navegação / Ações Superiores**:
   - Salvar, Cancelar, Excluir, Novo Registro.
   - Botão **Outras Opções...**: rotinas especiais, configurações, exportações, impressões.
   - **Botões de Ação Personalizados**: ações criadas por desenvolvedores que executam classes Java (`@ActionButton`) ou scripts.
2. **Modo Grade (Grid)**:
   - Apresenta múltiplos registros para busca rápida, ordenação e filtros dinâmicos.
   - Permite exibição de colunas customizadas e campos calculados (#type.sql#).
3. **Modo Formulário (Form / DynamicForm)**:
   - Exibe os detalhes do registro selecionado em abas contextuais (Geral, Fiscal, Endereço, Financeiro, etc.).
   - Os campos respeitam tipo de dado, máscara, validações e lista de opções configuradas no Dicionário de Dados.
4. **Painel de Filtros e Pesquisa**:
   - Filtro rápido e construtor de expressões avançadas.

---

## 2. Relação Entre Telas, Entidades e Tabelas

No Sankhya, o nome exibido na tela mapeia diretamente para uma entidade lógica do dicionário e uma ou mais tabelas físicas:

| Nome da Tela | Entidade JAPE | Tabela Física Principal | Descrição |
|---|---|---|---|
| **Cadastro de Parceiros** | `Parceiro` | `TGFPAR` | Clientes, fornecedores, vendedores, transportadoras |
| **Central de Vendas / Compras** | `CabecalhoNota` / `ItemNota` | `TGFCAB` / `TGFITE` | Pedidos, notas fiscais, orçamentos, faturamento |
| **Movimentação Financeira** | `Financeiro` | `TGFFIN` | Títulos a pagar, títulos a receber, baixas |
| **Cadastro de Produtos** | `Produto` | `TGFPRO` | Itens de estoque, serviços, matéria-prima |
| **Controle de Estoque** | `Estoque` | `TGFEST` | Saldos por empresa, local e controle |
| **Tipo de Operação (TOP)** | `TipoOperacao` | `TGFTOP` | Regras de movimentação fiscal e comercial |

---

## 3. Como Investigar o Comportamento de uma Tela

Quando o usuário solicitar desenvolvimento, integração ou esclarecimento sobre uma tela:
1. **Localizar o código e o manual da tela**: use o script `scripts/search_help.py <nome-da-tela>` para ver a documentação oficial.
2. **Identificar os parâmetros de sistema associados**: as telas possuem parâmetros (ex: `ACEITACGCBRANCO`, `EXIGELIMITECRED`, `CODPAISBRASIL`) que alteram regras de validação.
3. **Inspecionar as abas e dependências**: identificar se a tela depende de outras entidades (ex: para cadastrar Parceiro é necessário Cidade `TSICID` e Bairro `TSIBAI`).
