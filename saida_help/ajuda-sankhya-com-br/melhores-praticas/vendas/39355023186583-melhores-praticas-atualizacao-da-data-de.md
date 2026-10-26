---
id: "39355023186583"
titulo: "Melhores Práticas: \"Atualização da data de última venda\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39355023186583-Melhores-Pr%C3%A1ticas-Atualiza%C3%A7%C3%A3o-da-data-de-%C3%BAltima-venda"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-08-17T01:04:54Z"
rotulos: ["Produtos", "Configuração", "Relatórios Gerenciais", "TOP", "Estoque", "Artigo criado KCS", "CVE - KCS"]
---

# Melhores Práticas: "Atualização da data de última venda"

O sistema Sankhya permite controlar a **atualização da data de última venda** dos produtos através da configuração do campo **"Atualizar Última Venda"** nos **"Tipos de Operação"** . Esta funcionalidade é essencial para análises de vendas, gestão de estoque e relatórios gerenciais.

A configuração determina **se e quando** a data de última venda será atualizada no cadastro do produto, podendo ser definida para não atualizar ou atualizar em momentos específicos do processo de venda.

### Opções de configuração disponíveis

O campo **"Atualizar Última Venda"** possui as seguintes opções de configuração:

**N - Não Atualizar:** A data de última venda do produto não será atualizada quando utilizar este tipo de operação. Esta opção é recomendada para operações que não representam vendas efetivas, como devoluções, transferências ou operações de despesa/receita.

**S - Data de Saída:** A data de última venda será atualizada com a **data de saída** da nota fiscal. Esta é a opção mais comum para operações de venda, produção e atendimento.

**F - Data de Faturamento:** A data de última venda será atualizada com a **data de faturamento** da operação. Utilize esta opção quando o controle deve considerar o momento do faturamento.

**G - Data de Negociação:** A data de última venda será atualizada com a **data de negociação**. Esta opção é útil para controles que precisam considerar o momento inicial da negociação comercial.

### Tipos de Operação e configurações padrão

Diferentes Tipos de Operação podem ter configurações distintas para atualização da última venda:

**Operações de Venda:** Os tipos de operação como **"Top de Produção"**, **"Top de Atendimento"** e **"Top de Saída"** geralmente são configurados para atualizar a última venda com a data de saída (S), faturamento (F) ou negociação (G).

**Operações Auxiliares:** Os tipos de operação como **"Top de Entrada"**, **"Top de Back Order"**, **"TOP Despesa"** e **"TOP Receita"** podem ser configurados para não atualizar (N) a última venda, dependendo da necessidade do negócio.
