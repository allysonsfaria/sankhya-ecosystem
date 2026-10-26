---
id: "21518134633495"
titulo: "Rejeição 635: NF-e com mesmo número e série já transmitida e aguardando processamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21518134633495-Rejei%C3%A7%C3%A3o-635-NF-e-com-mesmo-n%C3%BAmero-e-s%C3%A9rie-j%C3%A1-transmitida-e-aguardando-processamento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:50:04Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "635", "Erro", "Documentos Eletrônicos"]
---

# Rejeição 635: NF-e com mesmo número e série já transmitida e aguardando processamento

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/21518142050199) **MENSAGEM:**

Rejeição 635: NF-e com mesmo número e série já transmitida e aguardando processamento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21518142053655)SOLUÇÃO:**

Deve-se aguardar que o retorno do documento que está em processamento seja devolvido. Como trata-se de lentidão nos servidores da SEFAZ, é necessário aguardar a sincronização pois não podemos alterar informações dessa nota pois pode ocorrer a sincronização entre a SEFAZ estadual e nacional e assim ocorrer algum problema fiscal.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/21518142055575)CAUSA:**

Quando for emitido uma NF-e, e durante o seu processamento na SEFAZ, essa mesma NF-e for reenviada, será retornado a rejeição "635 - NF-e com mesmo número e série já transmitida e aguardando processamento". Essa rejeição é ocasionada em situações onde os servidores da SEFAZ apresentam algum tipo de problema interno, ocasionando lentidão ou falha no processamento das NF-e recebidas.

**Exemplo:**

Foi emitido a NF-e de número 10 e série 1, mas a SEFAZ está demorando para autorizar a NF-e e o emitente envia novamente a NF-e para processamento. Quando a SEFAZ receber o novo lote da NF-e e verificar que já uma mensagem para a mesma NF-e em processamento, a rejeitará o último envio pelo motivo 635.

Veja regra de validação da SEFAZ:

![Imagem 4: Veja regra de validação da SEFAZ:](https://ajuda.sankhya.com.br/hc/article_attachments/21518134628887)
