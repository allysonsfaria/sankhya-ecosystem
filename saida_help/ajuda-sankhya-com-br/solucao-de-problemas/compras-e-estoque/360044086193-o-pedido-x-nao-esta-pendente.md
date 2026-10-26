---
id: "360044086193"
titulo: "O pedido 'X' não está pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044086193-O-pedido-X-n%C3%A3o-est%C3%A1-pendente"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:00Z"
rotulos: ["#criadoRoger", "CORE_E04604", "Configuração", "Faturamento", "Central de Vendas", "TOP", "Preferências", "Pedido Não Pendente para Faturamento", "Erro"]
---

# O pedido 'X' não está pendente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16107485992727) MENSAGEM:**

[CORE\_E04604] O pedido 'X' não esta pendente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16107485996567) SOLUÇÃO:**

![Imagem 3: Identifique se o pedido já foi totalmente faturado: Abra o lançamento na respectiva " Central…](https://ajuda.sankhya.com.br/hc/article_attachments/16107486000663) Identifique se o pedido já foi totalmente faturado: Abra o lançamento na respectiva "**Central (Compras/Vendas/Mov.Interna)"**, na grade de itens, **"Outras Opções"** » **"Documentos Relacionados"** verifique se já existe um **"Documento de Destino"**:

Caso seja identificado através do item 1, que o faturamento já tenha sido realizado totalmente, não será possível faturar esse pedido novamente, justificando a mensagem apresentada.

Caso o faturamento não tenha sido total ou não tenha acontecido, siga com as próximas análises:

![Imagem 4: Certifique-se que a TOP de Pedido utilizada foi configurada com a opção "A nota fica como pendente" .](https://ajuda.sankhya.com.br/hc/article_attachments/16107486004247) Certifique-se que a TOP de Pedido utilizada foi configurada com a opção **"A nota fica como pendente"**.

**(2)** Tela **"[Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"**, aba **"Geral"**, campo A nota fica como pendente.

![Imagem 5: Caso trate-se de movimentação de compra, certifique-se que o parâmetro abaixo esteja Ligado :](https://ajuda.sankhya.com.br/hc/article_attachments/16107515689751) Caso trate-se de movimentação de compra, certifique-se que o parâmetro abaixo esteja **Ligado**:

**(2)** Tela **"Preferências"** (Configurações » Avançado), chave **"PEDCPAPEND - Deixar Ped./Nota Compra pendente?"**

![Imagem 6: Caso tenha sido necessário algum dos ajustes mencionados nos itens 2 e 3 é possível compreender o motivo dos pedidos…](https://ajuda.sankhya.com.br/hc/article_attachments/16107486010391) Caso tenha sido necessário algum dos ajustes mencionados nos itens 2 e 3 é possível compreender o motivo dos pedidos serem mantidos como **Não Pendentes**, impossibilitando o seu faturamento. Dessa forma realize os ajustes, duplique esse pedido e avalie o comportamento para os próximos lançamentos.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16107486013335) CAUSA:**

Mensagem apresentada ao tentar faturar um pedido que esteja com o campo **"Pendente"** = Não.
