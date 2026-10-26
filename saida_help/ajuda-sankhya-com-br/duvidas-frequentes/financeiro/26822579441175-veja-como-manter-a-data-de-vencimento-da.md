---
id: "26822579441175"
titulo: "Veja como manter a data de vencimento das parcelas ao faturar um pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26822579441175-Veja-como-manter-a-data-de-vencimento-das-parcelas-ao-faturar-um-pedido"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:40:37Z"
rotulos: ["Configuração", "Pedido", "TOP", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "manter a data de vencimento das parcelas ao faturar um pedido", "faturamento", "mesma data de vencimento"]
---

# Veja como manter a data de vencimento das parcelas ao faturar um pedido

**(1)** Este artigo tem o objetivo de realizar as devidas configurações para que seja enviado para o faturamento a mesma data de vencimento que foi gerada no pedido (provisão).

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26822579430551)SOLUÇÃO:**

![Imagem 2: Acesse as configurações da tela "Comercial > Tipo de Operação - TOP", aba "Financeiro" .](https://ajuda.sankhya.com.br/hc/article_attachments/26822579431959) Acesse as configurações da tela "Comercial > Tipo de Operação - TOP", aba **"Financeiro"**.

**(1)** Configure o campo **"Tipo de Alteração da Data de Vencimento"** como **Manter**.

![Imagem 3: Habilite o parâmetro "MTDTVENAPRZO - Manter venc. na cópia de financeiros do faturamento?" . Pois, ainda que cite…](https://ajuda.sankhya.com.br/hc/article_attachments/26822564114199) Habilite o parâmetro **"MTDTVENAPRZO - Manter venc. na cópia de financeiros do faturamento?"**. Pois, ainda que cite "cópia", o sistema entende que ao faturar um pedido o mesmo título de provisão seja levada para o título real.

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26822564115607) OBSERVAÇÃO:**

Quando existem dois pedidos para o mesmo parceiro, mesmo que tenham data de vencimento e tipo de negociação idênticos, ao faturar agrupando em uma só nota, o sistema segue o cálculo normal da data de vencimento conforme configuração do tipo de negociação, ou seja, é um comportamento do sistema não manter a data do vencimento nesse caso.
