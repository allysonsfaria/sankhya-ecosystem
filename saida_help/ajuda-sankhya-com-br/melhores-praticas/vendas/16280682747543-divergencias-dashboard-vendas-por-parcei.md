---
id: "16280682747543"
titulo: "Divergências dashboard Vendas por parceiro no Gerente-Online"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16280682747543-Diverg%C3%AAncias-dashboard-Vendas-por-parceiro-no-Gerente-Online"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-31T04:42:55Z"
rotulos: ["Produtos", "Relatórios", "NF-e", "Atualização", "Financeiro", "Divergência em relatório de desempenho de produtos e vendas", "Produto em kit sem custo devido à nota de entrada não confirmada", "Confirmar a nota de entrada para atualizar o faturamento total", "Artigo atualizado KCS", "CVE - KCS"]
---

# Divergências dashboard Vendas por parceiro no Gerente-Online

No **Gerente On-Line (GOL)**, dentro do ícone de **Análises**, a opção **"Vendas por Parceiros"** é comum de gerar dúvidas quando os valores da aba "Faturamento" não batem com os da aba "Geral", mesmo usando os mesmos filtros de período e parceiro.

Entender por que isso acontece evita decisões erradas baseadas em uma leitura incorreta dos números.

### Por que as abas mostram valores diferentes

- **Faturamento**: mostra o valor total das notas de venda confirmadas no período, sem depender de nenhuma outra informação.
- **Geral**: mostra a rentabilidade (margem e lucro) das vendas. Para calcular isso, o sistema precisa comparar o valor de venda com o custo do produto, e esse custo só existe se estiver cadastrado **para a empresa que vendeu o produto**.

### Causa mais comum da divergência

Quando um produto é vendido por uma empresa, mas não tem custo cadastrado para aquela empresa específica, o sistema não consegue calcular a rentabilidade dessa venda. Nesse caso:

- A venda aparece normalmente na aba **Faturamento** (a nota foi emitida e confirmada).
- Na aba **Geral**, essa venda pode não ser considerada corretamente no cálculo, reduzindo o total de rentabilidade exibido, mesmo que o faturamento da mesma venda esteja correto na outra aba.

A falta de custo geralmente acontece por dois motivos:

1. O produto nunca teve custo cadastrado para aquela empresa.
2. A nota de entrada do produto (ou dos componentes de um kit) ainda não foi confirmada, e por isso o custo não foi atualizado no sistema.

### Exemplo prático

Duas notas de R$ 525,00 foram emitidas pela "Empresa 3" com o "Produto 642", totalizando R$ 1.050,00. Esse valor aparece normalmente na aba **Faturamento**.

Se o "Produto 642" tiver custo cadastrado só para a "Empresa 1", ou se a nota de entrada dele não estiver confirmada, a aba **Geral** não consegue calcular a rentabilidade dessas duas vendas, e o total de R$ 1.050,00 não é refletido corretamente nessa aba. Daí a divergência entre as duas telas.

### Como resolver

1. Confirme se as notas de entrada do produto (ou dos componentes do kit) estão devidamente liberadas no sistema.
2. Verifique se o produto tem custo cadastrado para a empresa que realizou a venda.
3. Cadastre o custo faltante ou confirme a nota de entrada pendente.
4. Consulte novamente o painel "Vendas por Parceiros" para conferir se os valores ficaram consistentes entre as abas.

### Outras observações importantes

- O painel associa a venda à **loja vendedora**, não ao fornecedor original do produto na nota.
- Para análises que os painéis nativos do Gerente On-Line não cobrem, verifique os relatórios do **Place** ou solicite um relatório personalizado.
