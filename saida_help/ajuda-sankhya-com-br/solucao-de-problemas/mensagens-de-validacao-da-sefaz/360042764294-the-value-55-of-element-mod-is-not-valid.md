---
id: "360042764294"
titulo: "The value '55' of element 'mod' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042764294-The-value-55-of-element-mod-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:05:55Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "Valor '55' de 'mod' Inválido", "Erro"]
---

# The value '55' of element 'mod' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16514737913623) MENSAGEM:**

The value '55' of element 'mod' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16514721330071) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Localize a nota de compra que originou a devolução, verifique o 'Tipo de Operação' utilizado na mesma. Através dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/16514737917335) Localize a nota de compra que originou a devolução, verifique o 'Tipo de Operação' utilizado na mesma. Através dessa TOP acesse a tela "[Tipos de Operação-TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (Caminho de acesso: Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros) e inicie as análises abaixo:

- Aba **"NF-e/NFC-e"** » "**Modelo do Documento"**: 55 - Nota Fiscal Eletrônica.
- Aba **"NF-e/NFC-e"** » campo "**NF-e"**: Terceiros.

![Imagem 4: Abra a nota de origem através da Central de Compras e verifique se existe " Chave NF-e" informada. Em caso negativo,…](https://ajuda.sankhya.com.br/hc/article_attachments/16514737918999) Abra a nota de origem através da Central de Compras e verifique se existe "**Chave NF-e"** informada. Em caso negativo, insira essa informação.

![Imagem 5: Caso a TOP possua informações que diferem do item 1, realize os devidos ajustes e relance a nota de entrada. Para isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/16514721337111) Caso a TOP possua informações que diferem do item 1, realize os devidos ajustes e relance a nota de entrada. Para isso, inutilize/exclua a devolução que gerou esse incidente.

![Imagem 6: Por fim, refaça o lançamento da nota de entrada, em seguida emita a devolução.](https://ajuda.sankhya.com.br/hc/article_attachments/16514721342103) Por fim, refaça o lançamento da nota de entrada, em seguida emita a devolução.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16514721344151)CAUSA:**

Rejeição apresentada, em sua maioria, na emissão de devoluções, onde a nota de origem possui informações diferentes do definido abaixo:

- "**NF-e**" = [Normal]
- "**Modelo do documento**" = [55]
- "**Chave NF-e**" = [Preenchida e existente na SEFAZ].

**![Imagem 8: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16514737928855) IMPORTANTE:**

Mesmo que atualmente as informações acima estejam corretas, o ajuste pode ter sido realizado após lançamento da nota. Dessa forma indicamos a realização das etapas 3 e 4.
