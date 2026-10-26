---
id: "9400540439959"
titulo: "TOP de destino deve ser do tipo compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9400540439959-TOP-de-destino-deve-ser-do-tipo-compra"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:06Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Devolução", "CORE_E02569", "CORE_E02571", "Restrição de TOP: Tipo Compra Necessário", "Erro", "Compras"]
---

# TOP de destino deve ser do tipo compra

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18926175180567) MENSAGEM:**

[CORE\_E02569] TOP de destino deve ser do tipo compra.

[CORE\_E02571] TOP de Destino deve ser do tipo COMPRA ou DEVOLUÇÃO DE COMPRA.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18926175189911) SITUAÇÃO:**

Em uma TOP com o TIPMOV ='O' , ao tentar configurar o campo "TOP P/ Faturamento" na Aba Geral, informando uma outra TOP com o mesmo TIPO DE MOVIMENTO, a mensagem "TOP de Destino deve ser do tipo COMPRA " será apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18926175197719)SOLUÇÃO:**

Para que seja possível 'faturar' uma TOP para outra com o mesmo TIPMOV, usuário deverá utilizar o seguinte procedimento:

![Imagem 4: Acesse as configurações da TOP, selecione Outras opções' -> "Restrições/Exceções";](https://ajuda.sankhya.com.br/hc/article_attachments/18926236861079) Acesse as configurações da TOP, selecione **Outras opções' -> "Restrições/Exceções";**

![Imagem 5: Em TOP Destino, selecione "Restrições' e realize a inclusão da TOP de Pedido desejada;](https://ajuda.sankhya.com.br/hc/article_attachments/18926175205783) Em TOP Destino, selecione **"Restrições'** e realize a inclusão da TOP de Pedido desejada;

![Imagem 6: Em TOP Destino, selecione "Restrições' e realize a inclusão da TOP de Pedido desejada;](https://ajuda.sankhya.com.br/hc/article_attachments/14597628977175)

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18926236868375) OBSERVAÇÃO:**

Esta mesma validação pode ocorrer para TOP's com outros TIPMOV (EX: Pedido de venda) porém, o procedimento a ser adotado é o mesmo.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18926236877463)CAUSA:**

Ocorre devido a TOP de origem com o tipo de movimento = O - Pedido de Compra estar selecionada, sendo necessário que o tipo de movimento da TOP selecionada para faturamento seja C- Compra.
