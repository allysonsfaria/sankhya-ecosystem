---
id: "360043004953"
titulo: "The content of element 'exporta' is not complete. One of '{\"http://www.portalfiscal.inf.br/nfe\":xLocExporta}' is expected"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043004953-The-content-of-element-exporta-is-not-complete-One-of-http-www-portalfiscal-inf-br-nfe-xLocExporta-is-expected"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:18Z"
rotulos: ["ERRONF", "NF-e", "XML", "SEFAZ", "CFOP", "Falta de Dados no Elemento 'exporta'", "Erro", "Documentos Eletrônicos"]
---

# The content of element 'exporta' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":xLocExporta}' is expected

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16314968738199) MENSAGEM:**

cvc-complex-type.2.4.b: The content of element 'exporta' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":xLocExporta}' is expected.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16314968744343) **SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a Central de Notas e identifique no rodapé os campos "Local do Embarque" e "UF Local Embarque" . Preencha os 2…](https://ajuda.sankhya.com.br/hc/article_attachments/16314968747671) Acesse a **Central de Notas** e identifique no rodapé os campos **"Local do Embarque"** e **"UF Local Embarque"**. Preencha os 2 campos corretamente.

![Local](https://ajuda.sankhya.com.br/hc/article_attachments/15660356732567)

![Imagem 5: Após os ajustes, transmita a NF-e novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16314996376855) Após os ajustes, transmita a NF-e novamente.

![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16314996379159) **CAUSA:**

Ocorre quando está emitindo uma **Nota de Exportação** com CFOP iniciada em 7 (Ex: CFOP 7949) e não foi preenchida Local de Embarque e UF de Embarque. Caso não seja uma nota de Exportação, considere ajustar a CFOP de acordo com o tipo de movimento da nota.
