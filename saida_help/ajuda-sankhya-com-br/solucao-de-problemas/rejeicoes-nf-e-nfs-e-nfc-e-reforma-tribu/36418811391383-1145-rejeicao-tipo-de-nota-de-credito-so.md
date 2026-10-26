---
id: "36418811391383"
titulo: "1145\tRejeição: Tipo de nota de crédito só pode ser usado a partir de janeiro/2029"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36418811391383-1145-Rejei%C3%A7%C3%A3o-Tipo-de-nota-de-cr%C3%A9dito-s%C3%B3-pode-ser-usado-a-partir-de-janeiro-2029"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:23:00Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Impostos", "TOP", "Erro", "Tipo de nota de crédito", "1145 Rejeição", "Rejeição 1145", "só pode ser usado a partir de janeiro/2029", "tipo de nota de crédito", "janeiro de 2029", "data de emissão anterior", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# 1145	Rejeição: Tipo de nota de crédito só pode ser usado a partir de janeiro/2029

**MENSAGEM**

1145 Rejeição: Tipo de nota de crédito só pode ser usado a partir de janeiro/2029

**SITUAÇÃO**

A rejeição é apresentada durante o processamento da importação do XML quando a nota fiscal utiliza um **tipo de nota de crédito** cuja validade está prevista apenas a partir de **janeiro de 2029**, enquanto a data de emissão do documento é anterior a esse período.

**SOLUÇÃO**

Siga o passo a passo para corrigir a rejeição:

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, verifique o campo **''Tipo Operação''** e identifique o TOP utilizado na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP identificado no passo anterior.

**(5)** Na aba **"NF-e/NFC-e/CF-e"**, verifique o campo **"Tipo de nota fiscal de crédito"** e altere o tipo de crédito.

- Se o tipo atual for **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, altere para um tipo válido para a data de emissão atual.

**(6)** Salve e transmita novamente a NF-e para a SEFAZ.

**CAUSA**

A rejeição ocorre devido ao uso de um **tipo de nota de crédito** específico (como o tipo "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM") que possui **validade restrita** a partir de janeiro de 2029, mas está sendo aplicado em uma nota fiscal com **data de emissão anterior** a este período, causando incompatibilidade temporal na validação fiscal.
