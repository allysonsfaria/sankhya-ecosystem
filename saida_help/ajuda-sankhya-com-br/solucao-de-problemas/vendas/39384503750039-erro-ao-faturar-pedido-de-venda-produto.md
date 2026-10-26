---
id: "39384503750039"
titulo: "Erro ao faturar pedido de venda: produto avulso incorporado ao kit"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39384503750039-Erro-ao-faturar-pedido-de-venda-produto-avulso-incorporado-ao-kit"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-27T01:58:48Z"
rotulos: ["Produtos", "Configuração", "Kit", "Faturamento", "Pedido de Venda", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Erro ao faturar pedido de venda: produto avulso incorporado ao kit

O sistema pode agrupar indevidamente um produto avulso aos componentes de um kit no momento do faturamento.

**SITUAÇÃO**

Ao faturar um Pedido de Venda que contém um Kit e, também, um Produto Avulso que é componente desse mesmo kit, o faturamento pode somar as quantidades do avulso junto ao componente do kit, gerando um único item na nota em vez de dois itens separados.

**SOLUÇÃO**

Para evitar que o produto avulso seja incorporado ao kit no faturamento, desabilite o parâmetro **"Agrupar Faturamento Sempre" (AGRUPFATSEMP)**:

**(1)** Acesse Configurações > Avançado > Parâmetros do Sistema.
**(2)** Desabilite AGRUPFATSEMP e AGRUPAPROD.
**(3)** Se o faturamento costuma unir vários pedidos em uma nota, mantenha ACEITARPRODREP habilitado.
**(4)** Salve e refaça o faturamento do pedido.

**Atenção:** desabilitar AGRUPFATSEMP impede o uso conjunto do detalhamento de lote pela conferência de faturamento (o sistema acusa erro se ambos estiverem ativos) e pode alterar a consolidação de múltiplos pedidos em uma mesma nota. Avalie o impacto antes de aplicar em produção. Não há hoje um parâmetro que impeça esse agrupamento de forma garantida — a solução acima remove os gatilhos conhecidos, mas não é uma trava estrutural do sistema para o cenário kit x avulso.

**CAUSA**

O faturamento consolida em um único item da nota todas as linhas do pedido com o mesmo produto, depósito e lote/controle, sem diferenciar se a linha é um componente de kit ou um item vendido avulso. Essa consolidação só acontece quando o sistema ordena os itens do pedido por produto (em vez de manter a ordem de lançamento original), o que é disparado por qualquer um destes parâmetros, se habilitado:

- **AGRUPFATSEMP -** Agrupar produto repetido em qualquer faturamento
- **AGRUPAPROD -** Agrupar produtos comuns em item
- **ACEITARPRODREP** - desabilitado, ao unir mais de um pedido na mesma nota
