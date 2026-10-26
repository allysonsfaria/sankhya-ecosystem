---
id: "14522438394519"
titulo: "Nota já Confirmada, liberação não pode ser reprovada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14522438394519-Nota-j%C3%A1-Confirmada-libera%C3%A7%C3%A3o-n%C3%A3o-pode-ser-reprovada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:35Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "CORE_E02837", "Liberação não pode ser negada após confirmação", "Ocorre ao tentar negar liberação após confirmação", "Cancelar ou excluir o pedido é a solução", "Erro", "Documentos Eletrônicos"]
---

# Nota já Confirmada, liberação não pode ser reprovada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16843137617687) MENSAGEM:**

[CORE\_E02837]: Nota já Confirmada, liberação não pode ser reprovada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16843137619863)SOLUÇÃO:**

O evento de liberação ocorre antes da confirmação, toda validação realizada pela rotina é antes da confirmação do pedido, tanto que pra conseguir confirmar o pedido tem que ser realizada a liberação para o evento solicitado. Neste caso foi realizada a liberação e o pedido foi confirmado, por isso a mensagem é apresentada. Assim, o que pode ser feito é um cancelamento ou exclusão do pedido, mas negar a liberação não será possível.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16843150674455)CAUSA:**

Ocorre ao tentar negar a liberação de um pedido que já foi confirmado.
