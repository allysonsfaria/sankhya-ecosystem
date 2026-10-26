---
id: "360043674493"
titulo: "Pedido/Nota XXXXX com solicitação de liberação com valor liberado inferior ao valor solicitado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043674493-Pedido-Nota-XXXXX-com-solicita%C3%A7%C3%A3o-de-libera%C3%A7%C3%A3o-com-valor-liberado-inferior-ao-valor-solicitado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:28Z"
rotulos: ["#criadoRoger", "#revisadohugo", "CORE_E03069", "Configuração", "Movimentação Financeira", "Liberação de Limites", "Valor solicitado maior que liberado", "Valor liberado inferior", "Reacessar e liberar limite", "Erro"]
---

# Pedido/Nota XXXXX com solicitação de liberação com valor liberado inferior ao valor solicitado

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16142049221143) MENSAGEM**:

[CORE\_E03069] Pedido/Nota XXXXX com solicitação de liberação com valor liberado inferior ao valor solicitado.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16142058535575) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a rotina "Liberação de Limites" (Caminho de acesso: Configurações » Avançado) com o usuário que efetuou a…](https://ajuda.sankhya.com.br/hc/article_attachments/16142058538007) Acesse a rotina **"Liberação de Limites"** (Caminho de acesso: Configurações » Avançado) com o usuário que efetuou a liberação anteriormente, através do duplo-clique, o evento ficará disponível novamente para nova Liberação.

![Imagem 4: Acesse a rotina "Liberação de Limites" (Caminho de acesso: Configurações » Avançado) com o usuário que efetuou a…](https://ajuda.sankhya.com.br/hc/article_attachments/14685878940695)

![Imagem 5: Após a liberação o pedido/nota poderá ser confirmado/faturado.](https://ajuda.sankhya.com.br/hc/article_attachments/16142058540439) Após a liberação o pedido/nota poderá ser confirmado/faturado.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16142049229463)CAUSA**:

Ocorre quando já houve liberação para o evento e após esta liberação houve alteração no lançamento, deixando o valor solicitado atual maior que o liberado anteriormente, sendo necessário que o usuário liberador realize a liberação do evento novamente.
