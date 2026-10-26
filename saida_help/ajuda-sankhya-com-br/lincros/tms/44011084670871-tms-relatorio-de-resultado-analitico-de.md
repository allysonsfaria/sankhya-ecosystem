---
id: "44011084670871"
titulo: "[TMS] - Relatório de resultado analítico de simulação de histórico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011084670871--TMS-Relat%C3%B3rio-de-resultado-anal%C3%ADtico-de-simula%C3%A7%C3%A3o-de-hist%C3%B3rico"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:54:21Z"
rotulos: ["sync_hc", "lincros", "lincros_13439664", "sync_hash_6cede6d43ca0"]
---

# [TMS] - Relatório de resultado analítico de simulação de histórico

Quando são passados os filtros para o relatório, ele leva em consideração o filtro **"Tipo valor"** para exibir o valor na coluna **"Custo unit. atual"**. O valor do campo é determinado de acordo com os cálculos abaixo:

- "Calculado(C)" = soma do Valor Total do Frete Calculado (conhecimento.getValorTotalFreteCalculado()) / soma da Quantidade de Itens (conhecimento.getQuantidadeItens())
- "Realizado(R)" = soma do Valor Total do Frete (conhecimento.getValorTotalFrete()) / soma da Quantidade de Itens (conhecimento.getQuantidadeItens())
- "Ideal(I)" = soma do Valor Total de Frete da Melhor Transportadora (conhecimento.getMelhorTransportadoraConhecimento().getValorTotalFrete()) / soma da Quantidade de Itens (conhecimento.getQuantidadeItens())
- "Inicial(N)" = soma do Valor Total do Frete Calculado na Origem (conhecimento.getValorTotalFreteCalculadoOrigem()) / soma da Quantidade de Itens (conhecimento.getQuantidadeItens())

Já a coluna **"Custo unit. novo"** é calculada através da fórmula abaixo:

- Custo unitário novo = soma do Valor Total de Frete Calculado na Carga (carga.getValorTotalFreteCalculado()) / soma da Quantidade de Itens (conhecimento.getQuantidadeItens())
