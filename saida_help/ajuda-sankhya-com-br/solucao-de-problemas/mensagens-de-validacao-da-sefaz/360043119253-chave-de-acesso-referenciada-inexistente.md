---
id: "360043119253"
titulo: "Chave de Acesso referenciada inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043119253-Chave-de-Acesso-referenciada-inexistente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-08-07T13:06:28Z"
rotulos: ["ERRONF", "NF-e", "XML", "SEFAZ", "267", "Rejeição", "Chave inexistente", "NF-e deve estar aprovada", "Transmitir após aprovação", "Documentos Eletrônicos"]
---

# Chave de Acesso referenciada inexistente

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504985988119) **MENSAGEM:**

[267 - Rejeição]: Chave de Acesso referenciada inexistente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504985990807) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Se emitida uma NF-e em ambiente normal, de 'Venda' por exemplo, a Devolução de Venda deverá ser transmitida somente…](https://ajuda.sankhya.com.br/hc/article_attachments/16504985994007) Se emitida uma NF-e em ambiente normal, de 'Venda' por exemplo, a Devolução de Venda deverá ser transmitida somente quando a NF-e de Venda estiver APROVADA pela SEFAZ, caso contrário, será emitida a mensagem:

\*Número Único: XXXXX. Nota NF-e tem que estar "APROVADA" para dar origem a outra nota.

![Imagem 4: Se a NF-e referenciada for transmitida em Contingência (tpEmis=2,4 ou 5) e ainda não foi aprovada pela SEFAZ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16505006600983) Se a NF-e referenciada for transmitida em Contingência (tpEmis=2,4 ou 5) e ainda não foi aprovada pela SEFAZ, primeiramente faça a regularização dela, para que seja possível referenciar esta NF-e em uma nova NF-e.

![Imagem 5: Assim que a NF-e referenciada for APROVADA pela SEFAZ, transmita a NF-e na qual está referenciada.](https://ajuda.sankhya.com.br/hc/article_attachments/16505006605335) Assim que a NF-e referenciada for APROVADA pela SEFAZ, transmita a NF-e na qual está referenciada.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504986006807) OBSERVAÇÃO:**

A exceção acima não se aplica para Nf-e Complementar (finNFe=2).

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16504986014487) CAUSA:**

Quando for emitida uma NF-e referenciando a Chave de Acesso de outra NF-e (modelo 55) que ainda não foi autorizada (não consta na base de dados da Sefaz), será retornada a rejeição.
