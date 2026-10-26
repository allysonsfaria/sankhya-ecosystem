---
id: "360043772474"
titulo: "Data de emissão CT-e posterior a data de recebimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043772474-Data-de-emiss%C3%A3o-CT-e-posterior-a-data-de-recebimento"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:59:09Z"
rotulos: ["ERROCTE", "#PUBLIFER", "#revisadohugo", "CT-e", "XML", "SEFAZ", "212", "CT-e emitido após recebimento", "Ajustar horários de emissão", "Conflito de horários de Sefaz", "Erro", "Documentos Eletrônicos"]
---

# Data de emissão CT-e posterior a data de recebimento

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454863455511) MENSAGEM:**

[212 - Rejeição]: Data de emissão CT-e posterior a data de recebimento.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454863458711) SOLUÇÃO:**

Existem duas situações que podem ocorrer esta mensagem:

**(2)** Suponhamos a emissão de um CT-e no dia 15/01/2020 com horário de emissão igual à 15:00:00 (GMT -03:00). Na SEFAZ Estadual, considere o horário local 14:50:00 (GMT -03:00). Como o horário de emissão do respectivo conhecimento de transporte é maior que o horário da SEFAZ, no momento de recebimento do documento, este será rejeitado.

**(2)** A segunda situação recorrente para essa validação são os períodos de início/fim do horário de verão. Em alguns Estados o fuso horário da SEFAZ é alterado  para o 'GMT -02:00', mas no sistema emissor não é realizada essa alteração e continua sendo usado o 'GMT -03:00'. Quando a CT-e chega no ambiente autorizador da SEFAZ, a rejeição ocorre.

**(1)** Dessa forma, aplique as soluções abaixo:

![Imagem 3: Verifique a data/Hora de emissão do CT-e e informe uma data/hora de emissão menor ou igual ao horário local da SEFAZ…](https://ajuda.sankhya.com.br/hc/article_attachments/16454863466519) Verifique a data/Hora de emissão do CT-e e informe uma data/hora de emissão menor ou igual ao horário local da SEFAZ autorizadora.

![Imagem 4: Verifique se o horário do servidor está sincronizado com o horário da SEFAZ do seu Estado.](https://ajuda.sankhya.com.br/hc/article_attachments/16454879061911) Verifique se o horário do servidor está sincronizado com o horário da SEFAZ do seu Estado.

![Imagem 5: Feito o ajuste, reenvie o CT-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16454863470359) Feito o ajuste, reenvie o CT-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454879066775) CAUSA:**

Quando for emitido um CT-e com Data/Hora de Emissão maior que a Data/Hora da Sefaz, no momento da recepção do documento será retornado a rejeição.
