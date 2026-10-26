---
id: "8337704977431"
titulo: "Informado CST de diferimento sem as informações de diferimento [nItem: xxx]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8337704977431-Informado-CST-de-diferimento-sem-as-informa%C3%A7%C3%B5es-de-diferimento-nItem-xxx"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-05T19:02:18Z"
rotulos: ["NF-e", "SEFAZ", "ICMS", "Impostos", "não apagar", "929", "CST de Diferimento sem Informações Adequadas [nItem: xxx]", "Documentos Eletrônicos"]
---

# Informado CST de diferimento sem as informações de diferimento [nItem: xxx]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361691542807) MENSAGEM:**

[929 - Rejeição]: Informado CST de diferimento sem as informações de diferimento [nItem: xxx]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361676423447)SOLUÇÃO:**

Caso se trate de uma NF-e (modelo 55) ou NFC-e (modelo 65) e o CST for igual a 51 - Diferimento, deve informe os seguintes campos de valores:

Valor do ICMS de operação - Tag vICMSOp
Modalidade BC ICMS - Tag modBC
Redução de BC ICMS - Tag pRedBC
Valor da BC do ICMS - Tag vBC
Alíquota de ICMS - Tag pICMS
Valor do ICMS - Tag vICMS 
Valor do ICMS de operação - Tag vICMSOp
Percentual do diferimento - Tag pDif 
Valor do ICMS diferido - Tag vICMSDif

De acordo com a NT(Nota Técnica 2019.001) temos algumas exceções para a regra de validação:

![Imagem 3: A regra não se aplica quando a Finalidade de emissão da NFe (tag: finNFe) é igual a Devolução de Mercadoria e…](https://ajuda.sankhya.com.br/hc/article_attachments/16361676423959) A regra não se aplica quando a Finalidade de emissão da NFe (tag: finNFe) é igual a Devolução de Mercadoria e Identificador de local de destino da operação (tag: idDest) igual a Operação interestadual ou com o Exterior.

![Imagem 4: A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de…](https://ajuda.sankhya.com.br/hc/article_attachments/16361691544727) A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a Devolução de Mercadoria;

![Imagem 5: A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste;](https://ajuda.sankhya.com.br/hc/article_attachments/16361691546135) A critério da UF, a regra não se aplica quando Finalidade de emissão da NF-e (tag: finNFe) igual a NF-e de Ajuste;

![Imagem 6: A critério da UF, a regra não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.](https://ajuda.sankhya.com.br/hc/article_attachments/16361676430487) A critério da UF, a regra não se aplica quando Tipo de Operação (tag: tpNF) igual à Entrada.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361691547159)CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e o CST - Código da Situação Tributária de ICMS for igual a 51 - Diferimento, deve informar todos os valores de diferimento;
