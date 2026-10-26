---
id: "35815751414167"
titulo: "1153 Rejeição: NFC-e com data de previsão de entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35815751414167-1153-Rejei%C3%A7%C3%A3o-NFC-e-com-data-de-previs%C3%A3o-de-entrega"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:24:39Z"
rotulos: ["Portal de Vendas", "SEFAZ", "Passos para resolver", "Erro", "NFC-e com data de previsão de entrega", "1153 Rejeição", "Rejeição 1153", "Como Resolver", "Artigo atualizado KCS", "Previsão de Entrega", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# 1153 Rejeição: NFC-e com data de previsão de entrega

**MENSAGEM**

1153 Rejeição: NFC-e com data de previsão de entrega.

**SITUAÇÃO**

A mensagem é apresentada ao tentar transmitir uma nota fiscal eletrônica (NFC-e) no sistema quando o campo **"Previsão de Entrega"** (**dPrevEntrega)** está preenchido. Isso ocorre durante o processo de emissão ou reenvio da nota fiscal.

**SOLUÇÃO**

Para solucionar, identifique a natureza do erro conforme as instruções abaixo:

**(1)**  Acesse a tela **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas).

**(2)**  Localize e selecione a NFC-e que apresentou a rejeição.

**(3)**  Encontre o campo **"Previsão de Entrega"** (**dPrevEntrega**).

**(4)** Remova qualquer data informada no campo **"Previsão de Entrega"**, deixando-o em branco.

**(5)**  Salve a nota e transmita novamente para a SEFAZ.

**CAUSA**

A **Rejeição 1153: NFC-e com data de previsão de entrega** ocorre porque o sistema da SEFAZ não permite que uma Nota Fiscal de Consumidor Eletrônica (NFC-e - modelo 65) contenha data de previsão de entrega. Essa tag é exclusiva para NF-e modelo 55.
