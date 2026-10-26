---
id: "360058522254"
titulo: "Item X do pedido/nota YYYY já foi faturado. Não pode ser excluído."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058522254-Item-X-do-pedido-nota-YYYY-j%C3%A1-foi-faturado-N%C3%A3o-pode-ser-exclu%C3%ADdo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-01T01:31:44Z"
rotulos: ["#criadoroger", "NF-e", "Faturamento", "Central de Vendas", "CORE_E01541", "Exclua nota cancele NF-e ou desligue nota", "Item já faturado", "Verifique documento destino", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Item X do pedido/nota YYYY já foi faturado. Não pode ser excluído.

**MENSAGEM**

[CORE\_E01541] Erro ao remover entidade: item do pedido/nota já foi faturado. não pode ser excluído.

**SITUAÇÃO**

Esta mensagem aparece ao tentar excluir um pedido de venda no Portal de vendas. Isso ocorre quando o sistema identifica que o item possui um faturamento vinculado ou uma quantidade entregue preenchida, impedindo a exclusão do documento por questões de integridade de dados.

**SOLUÇÃO**

A exclusão não será permitida até que as notas de destino sejam tratadas. Siga os passos abaixo para analisar e corrigir o cenário:

**(1)** Identifique o documento de destino. acesse o pedido de venda, selecione o item e clique em **"Outras Opções"** > **"Documentos Relacionados"**. na grade inferior, dê um duplo clique no documento de destino para visualizá-lo.

**(2)** Analise o documento e verifique se o item possui **"Quantidade Entregue"** preenchida indevidamente, mesmo que não haja uma nota fiscal ativa vinculada.

**(3)** Realize a tratativa necessária:

- Nota destino não confirmada ou NF-e de terceiros: exclua o lançamento.
- Nota fiscal eletrônica dentro do prazo: proceda com o cancelamento da mesma.
- Desligar a Nota: na Central de Vendas, utilize a opção **"Outras Opções"** > **"Desligar a Nota dos Pedidos"** para remover a vinculação entre a nota e o pedido.

**(4)** Caso excepcional (quantidade entregue preenchida sem nota): se confirmado que não existe nota fiscal, mas o campo **"QTDENTREGUE"** permanece preenchido, realize uma intervenção via banco de dados.

**(5)** Após a execução da correção, tente novamente excluir o pedido.

**Observação:** se o erro for recorrente, abra um chamado técnico para verificar possíveis falhas em triggers (como a **"TRG\_UPT\_TGFITE"**) ou customizações que impactem o preenchimento indevido da quantidade entregue.

**CAUSA**

O sistema bloqueia a exclusão para manter a integridade dos dados ao detectar que o item foi faturado ou possui movimentação registrada. isso pode ser causado por:

- Existência de nota fiscal de destino vinculada;
- Falha na trigger de atualização de estoque ou quantidade entregue;
- Exclusão de notas fiscais sem atualização do pedido original;
- Interrupções no processo de faturamento ou customizações indevidas.
