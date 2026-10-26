---
id: "360043674133"
titulo: "O Pedido/Nota de origem provisionou financeiro, a TOP de destino tem que atualizar o financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674133-O-Pedido-Nota-de-origem-provisionou-financeiro-a-TOP-de-destino-tem-que-atualizar-o-financeiro"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:33Z"
rotulos: ["CORE_E04608", "Configuração", "Movimentação Financeira", "Atualização", "TOP", "Financeiro", "TOP origem provisiona financeiro", "TOP destino deve atualizar financeiro", "Reconfigure ambas as TOPs refaça faturamento"]
---

# O Pedido/Nota de origem provisionou financeiro, a TOP de destino tem que atualizar o financeiro

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16138255399191) MENSAGEM:**

[CORE\_E04608] O Pedido/Nota de origem provisionou financeiro, a TOP de destino tem que atualizar o financeiro.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16138255402775)SOLUÇÃO:**

![Imagem 3: Alinhe com a equipe de faturamento para entender o processo realizado, de forma que a atualização de provisão do…](https://ajuda.sankhya.com.br/hc/article_attachments/16138255404183) Alinhe com a equipe de faturamento para entender o processo realizado, de forma que a atualização de provisão do financeiro na TOP de Origem seja ligada a uma TOP de Destino que**não tenha** a marcação **Financeiro: não atualizar.**

![Imagem 4: Sintonizado sobre o processo, reconfigure a marcação abaixo em ambas as TOP'S, de forma que a atualização do financeiro…](https://ajuda.sankhya.com.br/hc/article_attachments/16138255405847) Sintonizado sobre o processo, reconfigure a marcação abaixo em ambas as TOP'S, de forma que a atualização do financeiro seja correspondente.

- Se TOP Origem, campo **"Financeiro":** atualizar e campo **"Atualização do Financeiro"**: provisionar.
- Na TOP Destino, o campo **"Financeiro"** deve ser diferente de 'Não atualizar'.

![Imagem 5: Realizado os devidos ajustes, refaça o processo de faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16138255407895) Realizado os devidos ajustes, refaça o processo de faturamento.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17874286436375) IMPORTANTE:**

Ressaltamos que se necessário algum ajuste na TOP de ORIGEM, a nota deve ser relançada.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16138291556503) CAUSA:**

Ocorre quando a TOP de origem tenha provisionado financeiro e a TOP de destino não estiver configurada para atualizar financeiro.
