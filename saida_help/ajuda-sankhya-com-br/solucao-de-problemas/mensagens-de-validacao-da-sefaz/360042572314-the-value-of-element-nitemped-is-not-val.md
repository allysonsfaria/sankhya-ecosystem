---
id: "360042572314"
titulo: "The value ' ' of element 'nItemPed' is not valid"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042572314-The-value-of-element-nItemPed-is-not-valid"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:36Z"
rotulos: ["ERRONF", "DUVIDANF", "#PUBLIFER", "Configuração", "NF-e", "XML", "Valor Inválido de 'nItemPed'", "Erro"]
---

# The value ' ' of element 'nItemPed' is not valid

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443704199063) MENSAGEM:**

cvc-pattern-valid: Value ' ' is not facet-valid with respect to pattern '[0-9]{1,6}' for type #AnonType\_nItemPedproddetinfNFeTNFe'. cvc-type.3.1.3: The value ' ' of element 'nItemPed' is not valid.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443679291543)SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Verifique a informação inserida no campo 'Seq. no Pedido' para todos os itens da nota:](https://ajuda.sankhya.com.br/hc/article_attachments/16443704200215) Verifique a informação inserida no campo **'Seq. no Pedido'** para todos os itens da nota:

![Imagem 4: Verifique a informação inserida no campo 'Seq. no Pedido' para todos os itens da nota:](https://ajuda.sankhya.com.br/hc/article_attachments/14357857732503)

![Imagem 5: Ajuste a informação para um "número" sequencial válida. Caso não trabalhe com o envio da tag <nItemPed> no XML, limpe…](https://ajuda.sankhya.com.br/hc/article_attachments/16443679293335) Ajuste a informação para um "número" sequencial válida.  Caso não trabalhe com o envio da tag <nItemPed> no XML, limpe essa informação. Realizado o ajuste devido, redigite o cabeçalho da nota e gere um novo lote da respectiva nota.

**![Imagem 6: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16443679294615) IMPORTANTE:**

Caso não visualize esse campo, adicione o mesmo através do '**Configurador de Layout da nota**' , para mais detalhes: [Como inserir um campo no layout da nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043058973)
