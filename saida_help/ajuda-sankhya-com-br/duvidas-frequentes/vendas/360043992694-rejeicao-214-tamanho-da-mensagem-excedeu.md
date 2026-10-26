---
id: "360043992694"
titulo: "Rejeição 214: Tamanho da mensagem excedeu o limite estabelecido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043992694-Rejei%C3%A7%C3%A3o-214-Tamanho-da-mensagem-excedeu-o-limite-estabelecido"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:57:02Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Divida NF-e grande em duas para retransmissão", "Informações extensas aumentam o tamanho do XML", "Mensagens acima de 500 KB são rejeitadas pela SEF", "Erro", "Documentos Eletrônicos", "Tamanho da mensagem"]
---

# Rejeição 214: Tamanho da mensagem excedeu o limite estabelecido

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16414535762967) SOLUÇÃO:**

Deve-se reduzir o tamanho da mensagem para realizar a retransmissão da NF-e a SEFAZ. Uma forma de reduzir o tamanho da mensagem é a divisão de uma NF-e em outras 2. Caso a NF-e contenha muitos produtos, divida esses produtos e emita 2 NF-e's com numerações diferentes para esse mesmo cliente.

Importante lembrar que informações adicionais/complementares e/ou observações muito extensas podem aumentar o tamanho em Kbytes do arquivo XML.

**![Imagem 2: Importante lembrar que informações adicionais/complementares e/ou observações muito extensas podem aumentar o tamanho…](https://ajuda.sankhya.com.br/hc/article_attachments/16414535766167) CAUSA:**

Segundo o Manual de Orientação ao Contribuinte, a mensagem enviada aos WebServices para autorização não deve ultrapassar o tamanho de 500 KB. Caso seja encaminhada a SEFAZ uma NF-e ou Lote de NF-e que possua um tamanho superior a 500 KB, a mensagem será descartada e retornada a rejeição "214 - Tamanho da mensagem excedeu o limite estabelecido".
