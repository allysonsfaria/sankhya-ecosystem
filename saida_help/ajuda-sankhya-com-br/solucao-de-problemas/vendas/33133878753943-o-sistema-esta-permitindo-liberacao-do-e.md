---
id: "33133878753943"
titulo: "O sistema está permitindo liberação do evento 23 - Bonificação mesmo tendo atingido o limite de liberação no período para o liberador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33133878753943-O-sistema-est%C3%A1-permitindo-libera%C3%A7%C3%A3o-do-evento-23-Bonifica%C3%A7%C3%A3o-mesmo-tendo-atingido-o-limite-de-libera%C3%A7%C3%A3o-no-per%C3%ADodo-para-o-liberador"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:29:27Z"
rotulos: ["Configuração", "Liberação de Limites", "TOP", "Vendas", "Bonificação"]
---

# O sistema está permitindo liberação do evento 23 - Bonificação mesmo tendo atingido o limite de liberação no período para o liberador

**MENSAGEM:**

[CORE\_E03924] Valor acima do permitido.

**SITUAÇÃO:**

Quando um pedido de venda do tipo bonificação é lançado e passa pela liberação do evento 23, o sistema bloqueia novas liberações ao atingir o limite configurado, exibindo a mensagem: "Valor acima do permitido". No entanto, se um dos pedidos liberados for faturado, o sistema permite novas liberações, possibilitando que o valor total ultrapasse o limite definido para o período.

**CAUSA:**

Esse cenário geralmente ocorre quando a TOP utilizada no faturamento não está configurada como **"Bonificação"**. Nesse caso, o valor do pedido deixa de ser considerado entre os pedidos pendentes de liberação, e o valor da nota fiscal também não é contabilizado como liberado, justamente porque a TOP utilizada no faturamento não corresponde ao tipo **"Bonificação".**

**SOLUÇÃO:**

Verifique se a TOP utilizada no faturamento está corretamente configurada. Para que a bonificação seja considerada no saldo de liberações do evento 23 – Bonificação, é necessário utilizar uma TOP com o campo "Bonificação" marcado na aba "Geral" do seu cadastro.

![Imagem 1: Verifique se a TOP utilizada no faturamento está corretamente configurada. Para que a bonificação seja considerada no…](https://ajuda.sankhya.com.br/hc/article_attachments/33181886985111)
