---
id: "4959486434967"
titulo: "Não foi possível fixar as parcelas para o faturamento do documento xxx, pois o tipo de negociação possui \"Vencimento Pré-Fixado no Pedido\" e a quantidade de parcelas dos documentos (Origem -> Destino) é diferente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4959486434967-N%C3%A3o-foi-poss%C3%ADvel-fixar-as-parcelas-para-o-faturamento-do-documento-xxx-pois-o-tipo-de-negocia%C3%A7%C3%A3o-possui-Vencimento-Pr%C3%A9-Fixado-no-Pedido-e-a-quantidade-de-parcelas-dos-documentos-Origem-Destino-%C3%A9-diferente"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:18:20Z"
rotulos: ["Configuração", "Movimentação Financeira", "Ordem de Serviço", "TOP", "Financeiro", "não apagar", "#causaraizunidades", "[CORE_E0280]", "Problema de Parcelas no Faturamento devido a Configurações Incompatíveis", "Erro"]
---

# Não foi possível fixar as parcelas para o faturamento do documento xxx, pois o tipo de negociação possui "Vencimento Pré-Fixado no Pedido" e a quantidade de parcelas dos documentos (Origem -> Destino) é diferente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361097421975) MENSAGEM:**

[CORE\_E0280] Não foi possível fixar as parcelas para o faturamento do documento xxx, pois o tipo de negociação possui "Vencimento Pré-Fixado no Pedido" e a quantidade de parcelas dos documentos (Origem » Destino) é diferente.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361121128343)CAUSA:**

O problema ocorre pois a aplicação está inserindo apenas a primeira parcela do financeiro de origem no faturamento. Esse comportamento é causado pela marcação na TOP de pedido Faturamento relacionado a Ordem de Serviço que estava igual a Pelo Mód. Serviço pelas Parcelas do Financeiro.
Essa opção não deveria estar sendo usada pois ela trabalha juntamente com a opção Calcular comissão para O.S, que estava desmarcada.

- [Cálculo de Comissão por OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604674-C%C3%A1lculo-de-Comiss%C3%A3o-por-OS)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361121127063)SOLUÇÃO:**

Se o campo **"Calcular comissão para O.S"** estiver desmarcado, revise a marcação na TOP de pedido **"Faturamento relacionado a Ordem de Serviço"** se está com a opção **"Pelo Mód. Serviço pelas Parcelas do Financeiro",** pois ambos trabalham juntamente .

Portanto, se Calcular comissão para O.S estiver desmarcado, mude o campo Faturamento relacionado a Ordem de Serviço para: "Pela Central de Atendimento ao Cliente", e gere um novo pedido que a mensagem não será mais apresentada.

**![Imagem 4: OBSERVAÇÃO: verifique o parâmetro "RECALVENCAPROV", pois este deve permanecer desligado. Ou desmarque a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/16361097424919) OBSERVAÇÃO:** verifique o parâmetro **"RECALVENCAPROV",** pois este deve permanecer desligado. Ou desmarque a opção **"Vencimento pré-fixado no pedido"**no tipo de negociação.
