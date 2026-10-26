---
id: "7759024273687"
titulo: "Cancelar uma nota que ja foi finalizada no WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7759024273687-Cancelar-uma-nota-que-ja-foi-finalizada-no-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:13:12Z"
rotulos: ["Produtos", "WMS", "Estoque", "não apagar", "#validadojhonatan", "ORA-20101", "Não é possível excluir nota", "Realizar devolução dos produtos", "Integridade das notas no WMS", "Erro"]
---

# Cancelar uma nota que ja foi finalizada no WMS

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16540276953879) MENSAGEM**:

ORA-20101: Impossível excluir. Existem recebimentos no WMS que não foram cancelados.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16540251163031) SITUAÇÃO:**

Ao tentar cancelar ou excluir uma nota já enviada para o WMS ocorre o erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16540251164567) SOLUÇÃO:**

Pode ser feito uma devolução dos produtos gerando uma nota de saída.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16540251167127)CAUSA:**

O comportamento do sistema hoje visa pela integridade das notas com os produtos, sendo assim, um recebimento que já está como concluído no WMS não é possível cancelar ou excluir a nota origem de entrada pelo sistema.
