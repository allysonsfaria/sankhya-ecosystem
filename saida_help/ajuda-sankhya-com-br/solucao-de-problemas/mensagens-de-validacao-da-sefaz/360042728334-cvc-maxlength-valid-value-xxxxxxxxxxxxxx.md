---
id: "360042728334"
titulo: "cvc-maxLength-valid: Value 'XXXXXXXXXXXXXXX' with length = '701' is not facet-valid with respecto to maxLength '500' for type "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042728334-cvc-maxLength-valid-Value-XXXXXXXXXXXXXXX-with-length-701-is-not-facet-valid-with-respecto-to-maxLength-500-for-type"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:32Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoClaudio", "CORE_E04895", "Configuração", "NF-e", "XML", "SEFAZ", "Reduza infAdProd para 500 caracteres", "Use infCpl para detalhes longos", "Gere lote da NF-e novamente", "Erro", "Documentos Eletrônicos"]
---

# cvc-maxLength-valid: Value 'XXXXXXXXXXXXXXX' with length = '701' is not facet-valid with respecto to maxLength '500' for type 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513600701079) MENSAGEM:**

cvc-maxLength-valid: Value 'Serie(s): 1,10,100,101,102,103,104,105,106,107,108,109,11,110,111,112,113,114,115,116,117,118,119,12,120,121,122,123,124,125,126,127,128,129,13,130,131,132,133,134,135,136,137,138,139,14,140,141,142,143,144,145,146,147,148,149,15,150,151,152,153,154,155,156,157,158,159,16,160,161,162,163,164,165,166,167,168,169,17,170,171,172,173,174,175,176,177,178,179,18,180,181,182,183,184,185,186,187,188,189,19,190,191,192,193,194,195,196,197,198,199,2,20,200,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,35,36,37,38,39,4,40,41,42,43,44,45,46,47,48,49,5,50,51,52,53,54,55,56,57,58,59,6,60,61,62,63,64,65,66,67,68,69,7,70,71,72,73,74,75,76,77,78,79,8,80,81,82,83,84,85,86,87,88,89,9,90,91,92,93,94,95,96,97,98,99' with length = '701' is not facet-valid with respecto to maxLength '500' for type '#AnonType\_infAdProddetinfNFeTNFe'.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16513624817175) SOLUÇÃO**:

Para correção, siga os passos abaixo:

- Conforme orientações do Manual da Sefaz, a tag <infAdProd> suporta até 500 carácteres, no exemplo da mensagem de erro acima está com 701 carácteres, causando a rejeição.

![Imagem 3: Ligue o parâmetro " ENVOBSNFE-Envia Observação na NFe" e descreva as informações necessárias nos campos de Observação…](https://ajuda.sankhya.com.br/hc/article_attachments/16513600709399) Ligue o parâmetro "**ENVOBSNFE-Envia Observação na NFe"** e descreva as informações necessárias nos campos de Observação do cabeçalho da nota, para a tag <infCpl>, que suporte até 5000 carácteres.

Ajuste as informações e, após isso, gere novamente o lote da NF-e.

**![Imagem 4: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16513600712087) CAUSA**:

Ocorre quando as informações complementares dos itens, extrapolou a quantidade máxima definida pela SEFAZ. Grande volume de informações é orientado a ser inserido na Observação da Nota.
