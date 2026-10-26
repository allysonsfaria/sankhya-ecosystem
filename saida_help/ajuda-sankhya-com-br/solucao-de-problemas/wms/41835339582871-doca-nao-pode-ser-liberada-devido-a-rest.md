---
id: "41835339582871"
titulo: "Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41835339582871-Doca-n%C3%A3o-pode-ser-liberada-devido-a-restri%C3%A7%C3%A3o-de-configura%C3%A7%C3%A3o-Existem-os-seguintes-pedidos-pendentes"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-09-14T14:55:10Z"
rotulos: ["Configuração", "WMS", "Validação", "Preferências", "Liberação", "WMS - KCS", "Doca", "Regra para validar faturamento na liberação de doc", "pedidos de venda não faturados", "Valida e Bloqueia", "VALFATLIBDOCA"]
---

# Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes

**MENSAGEM**

Doca não pode ser liberada devido a restrição de configuração. Existem os seguintes pedidos pendentes

**SITUAÇÃO**

Ao tentar liberar a Doca pelo outras opções da tela expedição de mercadorias, o sistema apresenta a seguinte mensagem

**SOLUÇÃO**

**(1)** Acesse a tela **''Preferências''** (Configurações » Avançado » Preferências).

**(2)** Altere o parâmetro **''VALFATLIBDOCA''** - **''Regra para validar faturamento na liberação de doc''** para não valida.

**CAUSA**

É um comportamento sistêmico, pois, quando o parâmetro **''Regra para validar faturamento na liberação de doc''** - **''VALFATLIBDOCA"** que tem o objetivo de validar os pedidos de venda não faturados, está com a situação **Valida e Bloqueia**, o sistema não permite a liberação da doca até que o pedido de venda seja faturado.
