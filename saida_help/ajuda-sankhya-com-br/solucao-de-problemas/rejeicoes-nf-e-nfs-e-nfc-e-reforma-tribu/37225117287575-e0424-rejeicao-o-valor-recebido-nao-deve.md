---
id: "37225117287575"
titulo: "E0424 Rejeição: O valor recebido não deve ser informado na DPS quando o prestador ou tomador do serviço for o emitente da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225117287575-E0424-Rejei%C3%A7%C3%A3o-O-valor-recebido-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-prestador-ou-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:11Z"
rotulos: ["Central de Vendas", "Portal de Vendas", "SEFAZ", "Financeiro", "Passos para resolver", "Erro", "DPS (Declaração de Prestação de Serviços)", "Valor recebido", "Prestador ou tomador do serviço for o emitente da DPS", "Prestador ou tomador do serviço"]
---

# E0424 Rejeição: O valor recebido não deve ser informado na DPS quando o prestador ou tomador do serviço for o emitente da DPS.

**MENSAGEM**

E0424 Rejeição: O valor recebido não deve ser informado na DPS quando o prestador ou tomador do serviço for o emitente da DPS.

**SITUAÇÃO**

Mensagem apresentada ao tentar **emitir uma DPS** (Declaração de Prestação de Serviços) no sistema, quando o **valor recebido foi informado** indevidamente em operações onde o **emitente da DPS é também o prestador ou o tomador do serviço**.

**SOLUÇÃO**

**(1)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize o documento rejeitado.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Cabeçalho''**, verifique se o **emitente da DPS** é o **mesmo que o prestador do serviço** no campo **''Empresa''** ou o **tomador do serviço** no **''Parceiro''**.

**(3)** Na aba **''Financeiro''** remova o valor informado da DPS, deixando-o em branco ou zerado.

**(4)** Salve as alterações e **retransmita a DPS** para a Sefaz.

**CAUSA**

A rejeição ocorre quando, na **emissão de uma DPS**, o campo **"Valor Recebido"** é preenchido em situações onde o **emitente do documento é também o prestador ou o tomador do serviço**. Conforme as **regras de validação da Sefaz** estabelecidas pela **Lei Complementar nº 214/2025** (Reforma Tributária), o valor recebido **não deve ser informado** quando há identidade entre o emitente e uma das partes da operação (prestador ou tomador), pois isso caracteriza uma **operação interna** que não envolve recebimento de terceiros. A informação do valor recebido é aplicável apenas quando o **emitente da DPS é um intermediário** ou quando **prestador e tomador são distintos do emitente**.
