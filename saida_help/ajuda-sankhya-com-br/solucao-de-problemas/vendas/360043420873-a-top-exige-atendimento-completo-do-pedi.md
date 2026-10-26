---
id: "360043420873"
titulo: "A TOP exige atendimento completo do pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043420873-A-TOP-exige-atendimento-completo-do-pedido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-25T18:47:01Z"
rotulos: ["#PUBLIFER", "CORE_E02687", "Configuração", "NF-e", "TOP", "Pedido Nota TOP", "Erro"]
---

# A TOP exige atendimento completo do pedido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117988064279) MENSAGEM:**

[CORE\_E02687]  A TOP Exige atendimento completo do pedido.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16118001259799) SITUAÇÃO:**

Ao criar uma nota, na confirmação a seguinte mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16118001289495) CAUSA:**

Ocorre ao emitir NF-e com TOP configurada para **"Exigir completo"** sem que exista a ligação de todos os itens do pedido  com a respectiva nota.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16118001261719) SOLUÇÃO:**

![Imagem 5: Acesse o cadastro do Tipo de Operação utilizado e verifique como encontra-se a configuração abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16118001268759) Acesse o cadastro do Tipo de Operação utilizado e verifique como encontra-se a configuração abaixo:

Aba **"Geral"** » Campo **"Exigir Pedido"**:

![Imagem 6: Aba "Geral" » Campo "Exigir Pedido" :](https://ajuda.sankhya.com.br/hc/article_attachments/14610662485527)

(2)** Não exigir:** Não exigirá nenhum tipo de origem, ou seja, a Nota não precisará estar vinculada a um Pedido.

(2)** Exigir algum item:** Exigirá que pelo menos um item da Nota tenha uma origem (Pedido).

(2)** Exigir completo**: Exigirá que todos os itens da Nota estejam ligados a uma origem (Pedido).

![Imagem 7: Caso a configuração acima esteja como " Exigir completo " é obrigatório que um pedido tenha sido selecionado para esse…](https://ajuda.sankhya.com.br/hc/article_attachments/16118001275287) Caso a configuração acima esteja como "**Exigir completo**" é obrigatório que um pedido tenha sido selecionado para esse faturamento e todos os itens tenham sido faturados.

![Imagem 8: Caso não deseje faturar todos os itens do pedido é necessário que a configuração acima seja revista, e definida como…](https://ajuda.sankhya.com.br/hc/article_attachments/16118001280535) Caso não deseje faturar todos os itens do pedido é necessário que a configuração acima seja revista, e definida como **"Exigir algum item"** ou **"Não exigir"**.

![Imagem 9: Se a alteração na TOP for realizada um novo lançamento deve ser feito.](https://ajuda.sankhya.com.br/hc/article_attachments/16118001284631) Se a alteração na TOP for realizada um novo lançamento deve ser feito.
