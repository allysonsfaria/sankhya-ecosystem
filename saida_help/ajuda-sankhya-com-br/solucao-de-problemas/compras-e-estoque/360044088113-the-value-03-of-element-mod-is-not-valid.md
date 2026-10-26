---
id: "360044088113"
titulo: "The value '03' of element 'mod' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088113-The-value-03-of-element-mod-is-not-valid"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:44Z"
rotulos: ["#RevisadoBraga", "Configuração", "Fiscal", "NF-e", "SEFAZ", "TOP", "Valor Inválido para 'mod'", "Erro"]
---

# The value '03' of element 'mod' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16454514342039) MENSAGEM:**

cvc-enumeration-valid: Value '03' is not facet-valid with respect to enumeration '[01, 02]'. It must be a value from the enumeration.
cvc-type.3.1.3: The value '03' of element 'mod' is not valid.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454514344087) SITUAÇÃO:**

Ao realizar emissão de Devolução de Compra no **SankhyaW**, acessando o respectivo 'Portal' de emissão, na opção "**Outras Opções" »**"**Ver Acompanhamento**" é possível consultar a rejeição a seguir:ir:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16454566866839) SOLUÇÃO:**

![Imagem 4: Localize a nota de compra que originou a devolução, verifique o 'Tipo de Operação' utilizado na mesma. Através dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/16454514348951) Localize a nota de compra que originou a devolução, verifique o 'Tipo de Operação' utilizado na mesma. Através dessa TOP acesse a tela "**[Tipos de Operação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** e inicie as análises abaixo:

- Aba "**Livro Fiscal"** » "**Modelo do Documento"** = 01 - Nota Fiscal;
- Aba "**Impressão"** » campo "**NF-e"**, = Não usa.

![Imagem 5: Caso a TOP possua informações que diferem do item 1, realize os devidos ajustes e relance a nota de entrada. Para isso,…](https://ajuda.sankhya.com.br/hc/article_attachments/16454566870167) Caso a TOP possua informações que diferem do item 1, realize os devidos ajustes e relance a nota de entrada. Para isso, inutilize/exclua a devolução que gerou esse incidente.

![Imagem 6: Por fim, refaça o lançamento da nota de entrada, em seguida emita a devolução.](https://ajuda.sankhya.com.br/hc/article_attachments/16454566871703) Por fim, refaça o lançamento da nota de entrada, em seguida emita a devolução.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16454566874135) CAUSA:**

Rejeição apresentada, em sua maioria, na emissão de devoluções, onde a nota de origem possui informações diferentes do definido abaixo:

- "**NF-e"** = Não usa.
- "**Modelo do documento"** = 01.
