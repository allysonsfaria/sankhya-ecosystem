---
id: "360043230873"
titulo: "NFC-e com Data-Hora de emissão atrasada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043230873-NFC-e-com-Data-Hora-de-emiss%C3%A3o-atrasada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:10Z"
rotulos: ["ERRONF", "XML", "Atualização", "SEFAZ", "NFC-e", "704", "Rejeição 704: Data-Hora de Emissão Atrasada na NFC-e", "Erro", "Documentos Eletrônicos"]
---

# NFC-e com Data-Hora de emissão atrasada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16089252315159) MENSAGEM:**

704- Rejeição: NFC-e com Data-Hora de emissão atrasada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16089252320663) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Consulte a Legislação vigente da Sefaz do Estado para saber qual o atraso máximo permitido.](https://ajuda.sankhya.com.br/hc/article_attachments/16089237075095) Consulte a Legislação vigente da Sefaz do Estado para saber qual o atraso máximo permitido.

![Imagem 4: Caso o prazo tenha sido extrapolado, aconselha-se validar se essa NFC-e consta como inexistente no Portal NFC-e do seu…](https://ajuda.sankhya.com.br/hc/article_attachments/16089252326551) Caso o prazo tenha sido extrapolado, aconselha-se validar se essa NFC-e consta como inexistente no Portal NFC-e do seu Estado. Em caso positivo, proceda com a inutilização de sua numeração, sua exclusão.

![Imagem 5: Emita uma nova NFC-e com datas atualizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/16089237079191) Emita uma nova NFC-e com datas atualizadas.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16089252330263) CAUSA:**

Quando a Data-Hora de emissão da NFC-e possuir um atraso de mais de 5 minutos em relação ao horário de recepção da Sefaz, será retornado a rejeição "704 - NFC-e com Data-Hora de emissão atrasada".
