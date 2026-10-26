---
id: "39385440321687"
titulo: "Valor total do pedido não atualiza após faturamento parcial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39385440321687-Valor-total-do-pedido-n%C3%A3o-atualiza-ap%C3%B3s-faturamento-parcial"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-08-27T02:26:42Z"
rotulos: ["Configuração", "Relatórios", "Portal de Vendas", "Atualização", "Financeiro", "Artigo criado KCS", "CVE - KCS"]
---

# Valor total do pedido não atualiza após faturamento parcial

**Situação**

Ao faturar parcialmente um pedido pelo **Portal de Vendas** (Comercial > Consulta > Portal de Vendas), o campo **"Vlr Total"** do cabeçalho continua mostrando o valor cheio do pedido, sem refletir o que ainda falta faturar.

**Solução**

Esse é o comportamento esperado do sistema.

Para acompanhar o valor faturado e o saldo pendente, você pode:

**(1)** Criar um **campo calculado**, subtraindo do valor total o que já foi faturado.
**(2)** Criar um **relatório customizado**, com valor total, valor faturado e saldo a faturar.

**Causa**

O "Vlr Total" representa o valor original negociado no pedido, e não é alterado pelos faturamentos parciais. Isso acontece porque o pedido e a nota fiscal são documentos distintos: um pedido pode gerar várias notas ao longo do tempo, e o sistema mantém esse campo fixo para preservar o valor da negociação.
