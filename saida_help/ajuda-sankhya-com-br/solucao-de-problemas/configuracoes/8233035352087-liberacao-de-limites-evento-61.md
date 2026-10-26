---
id: "8233035352087"
titulo: "Liberação de Limites Evento 61 "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8233035352087-Libera%C3%A7%C3%A3o-de-Limites-Evento-61"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-28T19:40:47Z"
rotulos: ["Produtos", "Configuração", "Eventos", "Estoque", "não apagar", "61", "Gerenciamento de Validade de Produtos: Liberação de Data Antecipada"]
---

# Liberação de Limites Evento 61 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361674467991) MENSAGEM:**

61- Liberação de data de validade menor que o previsto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361674468887)SOLUÇÃO:**

Este evento está diretamente ligado ao parâmetro 'Mínimo de dias para validade dos produtos na entrada' (MINDIASVALENT). No lançamento de Notas de Compra, ao incluir um produto controlado por Lote e Data de Validade (parâmetro 'LOTEDTVAL' ligado), o sistema validará a Data de validade, informada para o produto, com a configuração definida no parâmetro MINDIASVALENT.
Se a Data de validade for menor ou igual a data atual mais os dias do parâmetro MINDIASVALENT, o sistema avisará ao usuário que a data está inválida. Se o usuário ainda assim confirmar a nota, será solicitado a liberação deste evento.
Os produtos, lotes e datas inválidas ficarão registrados na Observação da liberação. Após a liberação será possível confirmar a nota.
Se o usuário fizer alguma alteração na Data de validade de algum produto ou inserir um novo produto com data inválida, o sistema fará outra solicitação de liberação.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361689567639)CAUSA:**

O evento 61 está diretamente ligado aos parâmetros, **"MINDIASVALENT"**,  **"LOTEDTVAL"** para o uso e correto funcionamento.
