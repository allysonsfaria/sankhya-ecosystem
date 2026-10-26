---
id: "360043200913"
titulo: "Falha no reconhecimento da autoria ou integridade do arquivo digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043200913-Falha-no-reconhecimento-da-autoria-ou-integridade-do-arquivo-digital"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:31Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoGilmar", "NF-e", "XML", "SEFAZ", "202", "Falha no reconhecimento do arquivo digital", "Aguarde estabilização e reenviar nota", "Alterações no template da SEFaz", "Erro", "Documentos Eletrônicos"]
---

# Falha no reconhecimento da autoria ou integridade do arquivo digital

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16447963707927) MENSAGEM:**

[202-Rejeição]: Falha no reconhecimento da autoria ou integridade do arquivo digital.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16447963711511) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Quando houver alguma alteração nos templates utilizados pela Sefaz, caso seja gerada alguma nota que não esteja de acordo com o padrão exigido, a resposta será essa rejeição. **Na maioria das vezes essa rejeição está relacionada a uma falha da própria SEFAZ.**

Neste caso, aguarde a estabilização dos servidores da Secretaria da Fazenda e gere o lote/enviar a nota novamente.

**![Imagem 3: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16447963712407) CAUSA**:

Quando é feito o envio de uma NF-e, os templates são como moldes da mensagem. Os Webservices aguardam essa mensagem de acordo com esse template, portanto, se houver alterações no arquivo template e o emitente da NF-e não estiver gerando essa NF-e de acordo com o novo template, a nota será rejeitada.
