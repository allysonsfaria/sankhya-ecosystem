---
id: "360043026093"
titulo: "Certificado Assinatura erro no acesso a LCR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043026093-Certificado-Assinatura-erro-no-acesso-a-LCR"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:58Z"
rotulos: ["ERRONF", "ERROMDFE", "ERROCTE", "#PUBLIFER", "NF-e", "SEFAZ", "296", "Erro na LCR", "Aguarde e teste novamente", "SEFAZ não acessou LCR", "Certificado Digital", "Erro", "LCR"]
---

# Certificado Assinatura erro no acesso a LCR

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457071798039) MENSAGEM:**

[296 - Rejeição]: Certificado Assinatura erro no acesso a LCR.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457071799575) SOLUÇÃO:**

Essa situação normalmente ocorre de forma momentânea, sendo recomendado que aguarde alguns minutos e volte a testar a emissão/comunicação atual. Caso esse prazo se prolongue, orientamos a contactar a SEFAZ e/ou a empresa emissora do certificado digital para alinhar possíveis causas e tratativas para o problema.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457056155543) CAUSA:**

Ao realizar a comunicação com a SEFAZ, essa verifica se o Certificado assinante está na Lista de Certificados Revogados (LCR). Se por alguma indisponibilidade a SEFAZ não consegue realizar essa consulta, a rejeição é retornada.

Essa rejeição não significa que seu certificado esteja revogado. O problema ocorre porque a Sefaz não conseguiu consultar uma lista para checar a validade do certificado. Trata-se de um problema interno da Sefaz e não quer dizer que o seu certificado esteja com problema.
