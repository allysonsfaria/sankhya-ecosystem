---
id: "360043661433"
titulo: "O produto referenciado por este pedido ou nota já está associado a outro pedido ou nota, não se pode atualizá-lo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043661433-O-produto-referenciado-por-este-pedido-ou-nota-j%C3%A1-est%C3%A1-associado-a-outro-pedido-ou-nota-n%C3%A3o-se-pode-atualiz%C3%A1-lo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:09Z"
rotulos: ["#PUBLIFER", "#revisadohugo", "Produtos", "NF-e", "Atualização", "Produto já associado a outro documento", "Verifique a ligação para documentos eletrônicos", "Exclua e insira o produto desejado", "Erro", "Documentos Eletrônicos"]
---

# O produto referenciado por este pedido ou nota já está associado a outro pedido ou nota, não se pode atualizá-lo

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16142957725207) MENSAGEM:**

SQL-50001 O produto referenciado por este pedido ou nota já está associado a outro pedido, ou nota, não se pode atualizá-lo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16142957728791) SITUAÇÃO:**

Mensagem apresentada ao tentar alterar o item de um lançamento, após faturá-lo através de um documento origem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16142965809687) SOLUÇÃO:**

![Imagem 4: Se necessário altere o produto que foi faturado por um documento origem, o procedimento correto é excluir o produto que…](https://ajuda.sankhya.com.br/hc/article_attachments/16142957737367) Se necessário altere o produto que foi faturado por um documento origem, o procedimento correto é **excluir o produto que não será mantido** na nota de destino e **inserir o produto desejado**.

![Imagem 5: Lembre-se que o item excluído perderá a ligação com o documento de origem e voltará a ficar pendente: SIM .](https://ajuda.sankhya.com.br/hc/article_attachments/16142957738391) Lembre-se que o item excluído perderá a ligação com o documento de origem e voltará a ficar **pendente: SIM**.

![Imagem 6: Para o faturamento de pedido/nota o impacto constatado é o citado no item 2. Porém, se esse processo for realizado para…](https://ajuda.sankhya.com.br/hc/article_attachments/16142965816855) Para o faturamento de pedido/nota o impacto constatado é o citado no item 2. Porém, se esse processo for realizado para documentos eletrônicos que exigem a chave referenciada, é importante ressaltar que essa ligação será perdida, sendo necessário vincular e preencher esse campo no layout da nota destino, evitando possíveis rejeições.

**(1)** Lembramos que é importante avaliar o processo com cautela, visto que é incompreensível vender o PRODUTO A e faturar/devolver o PRODUTO B. A prática recomendada é que o ajuste seja realizado considerando todos os documentos vinculados.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16142957745431) CAUSA:**

Mensagem apresentada ao tentar alterar o item de um lançamento, após faturá-lo através de um documento origem. A mensagem é causada pelas ligações entre os documentos, visto que as informações devem ser preservadas.
