---
id: "39364925741719"
titulo: "[CORE_E04678] Não existem produtos/quantidades disponíveis ao gerar remessa de nota de entrega futura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39364925741719--CORE-E04678-N%C3%A3o-existem-produtos-quantidades-dispon%C3%ADveis-ao-gerar-remessa-de-nota-de-entrega-futura"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-10-15T12:07:15Z"
rotulos: ["NF-e", "Central de Vendas", "Estoque", "Erro", "Artigo criado KCS", "CVE - KCS", "Entrega Futura"]
---

# [CORE_E04678] Não existem produtos/quantidades disponíveis ao gerar remessa de nota de entrega futura

**MENSAGEM**

[CORE\_E04678] Não existem produtos/quantidades disponíveis para essa operação.

**SITUAÇÃO**

Ao tentar gerar uma **"Nota Fiscal de Remessa"** a partir de uma **"Nota de Simples Faturamento para Entrega Futura"**, o sistema exibe a mensagem de erro informando que não existem produtos ou quantidades disponíveis para a operação, mesmo quando a nota de origem ainda mostra saldo na coluna **"Qtd. pendente"**.

**SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse o **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e localize a nota de simples faturamento para entrega futura que originou o erro.

**(2)** Na grade de itens da nota, verifique a coluna **"Qtd. corte"**. Um valor maior que zero indica que existe corte aplicado no item, e esse corte reduz a quantidade disponível para remessa.

**(3)** Caso identifique cortes nos itens, altere a **"Qtd. corte"** para **0 (zero)** e salve, para liberar os produtos.

**(4)** Após limpar o corte, tente novamente gerar a nota de remessa a partir da nota de entrega futura.

**(5)** Confirme se os itens agora estão disponíveis e se a nota de remessa foi gerada com sucesso.

**Observação:** se a "Qtd. corte" e a "Qtd. pendente" estiverem zeradas, todo o saldo da nota já foi remetido e a mensagem é o comportamento esperado.

**CAUSA**

O erro ocorre quando existe um corte aplicado nos itens da nota de simples faturamento para entrega futura. Para gerar a remessa, o sistema considera disponível a quantidade negociada, menos a quantidade já entregue, menos a **"Qtd. corte"**. Quando o corte cobre todo o saldo restante, o item não fica disponível, mesmo que a coluna "Qtd. pendente" ainda mostre saldo, porque essa coluna não desconta o corte. Ao remover o corte, os itens voltam a ficar disponíveis para o processo de remessa. 

O corte pode ter sido informado manualmente na coluna "Qtd. corte" ou gerado em uma remessa anterior em que, na tela de faturamento, foi informada uma quantidade menor que o saldo ou algum item foi deixado de fora. Nesses casos, a diferença é gravada como corte e, se o parâmetro "**Zerar Corte após faturamento?**" (**ZERARQTDCONF**) estiver desligado, esse corte permanece na nota. Se o erro se repetir após remessas parciais, verifique esse parâmetro.
