---
id: "4421546912023"
titulo: "TOP de Destino deve ser do tipo VENDA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4421546912023-TOP-de-Destino-deve-ser-do-tipo-VENDA"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:19:25Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Vendas", "#causaraiz", "CORE_E02568", "Configurar TOP para \"V-Venda\" na TOP de destino", "Erro ao configurar TOP com TIPMOV \"P\"", "Adicionar restrições/exceções na TOP de origem", "Erro"]
---

# TOP de Destino deve ser do tipo VENDA

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16305191896471) MENSAGEM:**

[CORE\_E02568] Em uma TOP com o TIPMOV ='P', ao tentar configurar o campo "TOP P/ Faturamento", informando uma outra TOP com o mesmo TIPO DE MOVIMENTO, a mensagem "TOP de Destino deve ser do tipo VENDA " será apresentada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305187998487) SOLUÇÃO:**

Para que seja possível 'faturar' uma TOP para outra com o mesmo TIPMOV, faça o seguinte procedimento:

![Imagem 3: Nas configurações da TOP de Orçamento, selecione Outras opções' -> "Restrições/Exceções";](https://ajuda.sankhya.com.br/hc/article_attachments/16305191910039) Nas configurações da TOP de Orçamento, selecione Outras opções' -> "Restrições/Exceções";

![Imagem 4: Em TOP Destino, selecione "Restrições' e realize a inclusão da TOP de Pedido desejada;](https://ajuda.sankhya.com.br/hc/article_attachments/16305191913623) Em TOP Destino, selecione **"Restrições'** e realize a inclusão da TOP de Pedido desejada;

![Imagem 5: Em TOP Destino, selecione "Restrições' e realize a inclusão da TOP de Pedido desejada;](https://ajuda.sankhya.com.br/hc/article_attachments/15752235350551)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305191916695) OBSERVAÇÃO:**

Esta mesma validação pode ocorrer para TOP´s com outros TIPMOV (EX: Pedido de compra) porém, o procedimento a ser adotado é o mesmo.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16305188012823) CAUSA:**

Para TOP de origem com o tipo de movimento P-Pedido de Venda, é necessário que o tipo de movimento da TOP selecionada para faturamento seja V- Venda.
