---
id: "13230289815447"
titulo: "Não foi possível encontrar o parceiro remetente  XML importado não possui tag correspondente "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13230289815447-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-parceiro-remetente-XML-importado-n%C3%A3o-possui-tag-correspondente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:00:19Z"
rotulos: ["CT-e", "Parceiro", "XML", "Importação", "SEFAZ", "Falta de Tag <rem> no XML Importado", "Erro"]
---

# Não foi possível encontrar o parceiro remetente  XML importado não possui tag correspondente 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17147793767831) MENSAGEM:**

Não foi possível encontrar o parceiro remetente, XML importado não possui tag correspondente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17147793769751) SOLUÇÃO:**

**(1)** Acione o fornecedor, solicite que seja incluída essa informação e refaça o XML, caso não queira acionar o Fornecedor, inclua a nota Manualmente pelo Portal de compras.

**(1)** O que é **Remetente**?

É o ator (pessoa) participante em um CT-e, responsável por promover a saída inicial da carga. Poderá não ser informado quando o Tipo de Serviço for igual a "3 - Redespacho Intermediário" ou "4 - Serviço Vinculado a Multimodal".

| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | `<``rem``>`  `<``CNPJ``>99999999999999</``CNPJ``>`  `<``IE``>999999999999</``IE``>`  `<``xNome``>CT-e EMITIDO EM AMBIENTE DE HOMOLOGAÇÃO - SEM VALOR FISCAL</``xNome``>`  `<``enderReme``>`  `<``xLgr``>TIETE</``xLgr``>`  `<``nro``>999</``nro``>`  `<``xCpl``>LESTE</``xCpl``>`  `<``xBairro``>BARRANCA TIETE</``xBairro``>`  `<``cMun``>3536703</``cMun``>`  `<``xMun``>PEDERNEIRAS</``xMun``>`  `<``CEP``>17280000</``CEP``>`  `<``UF``>SP</``UF``>`  `</``enderReme``>`  `</``rem``>` |
| --- | --- |

**(1)** Confira mais informações de configurações no [Portal de importação de XML - Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050560634-Portal-de-importa%C3%A7%C3%A3o-de-XML-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg2ODI5MTc4OTQsInRpY2tldF9pZCI6MjY5NjM4LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTY4MTkxMjIxNX0.BOvFMrUvqSoNYWR65dC4fnVL_3fs8j7Md_bXxtIb0uw)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17147763662999) CAUSA:**

Ocorre pela falta da tag <rem> onde o sistema exige essa informação no momento da importação
