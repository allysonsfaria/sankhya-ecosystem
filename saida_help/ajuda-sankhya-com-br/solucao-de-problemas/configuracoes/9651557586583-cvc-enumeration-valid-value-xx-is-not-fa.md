---
id: "9651557586583"
titulo: "cvc-enumeration-valid: Value 'XX' is not facet-valid with respect to enumeration '[XX, XX]'. It must be a value from the enumeration. cvc-type.3.1.3: The value 'XX' of element 'mod' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9651557586583-cvc-enumeration-valid-Value-XX-is-not-facet-valid-with-respect-to-enumeration-XX-XX-It-must-be-a-value-from-the-enumeration-cvc-type-3-1-3-The-value-XX-of-element-mod-is-not-valid"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:00Z"
rotulos: ["CORE_E04895", "CT-e", "Configuração", "SEFAZ", "TOP", "CORE_E03978", "Problema de Validação no CT-e OS", "Erro", "Documentos Eletrônicos"]
---

# cvc-enumeration-valid: Value 'XX' is not facet-valid with respect to enumeration '[XX, XX]'. It must be a value from the enumeration. cvc-type.3.1.3: The value 'XX' of element 'mod' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18975980461335) MENSAGEM:**

[CORE\_E03978] cvc-enumeration-valid: Value 'XX' is not facet-valid with respect to enumeration '[XX, XX]'. It must be a value from the enumeration. cvc-type.3.1.3: The value 'XX' of element 'mod' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18975977191063) SITUAÇÃO:**

Ao tentar emitir CTE OS a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18975980472215) CAUSA:**

Configuração incorreta no cadastro do Tipo de Operação para a emissão de CT-e OS.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18975980478103) SOLUÇÃO:**

O CT-e OS se trata do Conhecimento de Transporte Eletrônico para Outros Serviços e para que seja realizada a emissão do CT-e OS de forma correta, você deve realizar as seguintes configurações:

Na tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), **aba NF-e/NFC-e**, o campo **"Modelo do Documento "**deverá estar com a opção**"67-Conhecimento Transporte Eletrônico Outros Serviços"** selecionada.

![Imagem 5: Na tela Tipos de Operação - TOP , aba NF-e/NFC-e , o campo "Modelo do Documento " deverá estar com a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/18975977208727)

Ainda nessa tela, na aba [CT-e/MD-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abactemde), o campo **"Tipo de serviço CT-e"** deve ser configurado com a opção**"7-transporte de valores"**.

![Imagem 6: Ainda nessa tela, na aba CT-e/MD-e , o campo "Tipo de serviço CT-e" deve ser configurado com a opção "7-transporte de…](https://ajuda.sankhya.com.br/hc/article_attachments/18975977214743)

[Conhecimento de Transporte Eletrônico - CT-e – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e#ct-eos)
