---
id: "10142612740247"
titulo: "Não é possível gerar Pedido Complementar para documentos de Venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10142612740247-N%C3%A3o-%C3%A9-poss%C3%ADvel-gerar-Pedido-Complementar-para-documentos-de-Venda"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:04:23Z"
rotulos: ["Conferência", "Configuração", "Vendas", "CORE_E01290", "Pedido complementar não gerado para venda", "Tentativa em documento de venda", "Permitido apenas para compras", "Erro", "Documentos Eletrônicos"]
---

# Não é possível gerar Pedido Complementar para documentos de Venda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19297830563735) MENSAGEM:**

[CORE\_E01290] Não é possível gerar Pedido Complementar para documentos de Venda.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297830569495) SITUAÇÃO:**

Ao alterar a configuração da conferência para gerar um pedido complementar (GERARPEDCOMPL = S) a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19297830574743) CAUSA:**

Ocorre ao tentar gerar o **"Pedido Complementar"** através de uma nota de venda.

![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297830583575) **SOLUÇÃO:**

Apenas será permitido gerar o **"Pedido Complementar"** ou a **"Nota de Devolução"** quando o documento que estiver sendo conferido for de **"Compra"**. Caso contrário, será emitida uma mensagem informando que não é possível gerar uma Nota de Devolução ou Pedido complementar para um documento de **"Venda"**, o processo será abortado e a conferência não será concluída.

Para mais informações sobre a fila de conferência basta acessar o link abaixo:

[Fila de Conferência – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)
