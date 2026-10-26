---
id: "5694874588823"
titulo: "Pedido não aprovado por conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5694874588823-Pedido-n%C3%A3o-aprovado-por-confer%C3%AAncia"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:17:48Z"
rotulos: ["Conferência", "Configuração", "Faturamento", "Financeiro", "Pedido não aprovado", "Conferência de pedido", "Parâmetro EXIGECONFPEDVDA", "Erro"]
---

# Pedido não aprovado por conferência

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16306102527383) MENSAGEM:**

Pedido não aprovado por conferência.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16306130492439)SOLUÇÃO:**

Quando ativo esse parâmetro exige que o pedido esteja aprovado para seguir com o faturamento e não existe código no sistema que aprove automaticamente o pedido quando o parâmetro está ativo. Esse parâmetro veio do MGE, pois lá não tinha a rotina de conferência, havendo a necessidade desse parâmetro estar ativo. Para o **Sankhya Om** não é necessário o uso desse parâmetro, pois o próprio sistema já faz essa validação de acordo com as novas configurações da fila de conferencia.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16306102557463) CAUSA:**

Quando o parâmetro **"EXIGECONFPEDVDA"** está ligado é feita a validação, pois no delphi usa essa opção mas no **Sankhya Om** ela não precisa ficar marcada.
