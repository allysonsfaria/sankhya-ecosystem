---
id: "35944511260439"
titulo: "1157 Rejeição: Data de previsão de entrega não permitida para a modalidade de frete informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35944511260439-1157-Rejei%C3%A7%C3%A3o-Data-de-previs%C3%A3o-de-entrega-n%C3%A3o-permitida-para-a-modalidade-de-frete-informada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-08-25T00:08:52Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Transporte", "Erro", "1157 Rejeição", "Data de previsão de entrega", "não permitida para a modalidade de frete informada", "Rejeição 1157"]
---

# 1157 Rejeição: Data de previsão de entrega não permitida para a modalidade de frete informada

**MENSAGEM**

1157 Rejeição: Data de previsão de entrega não permitida para a modalidade de frete informada.

**SITUAÇÃO**

A rejeição é apresentada ao emitir uma nota fiscal quando o campo **“Previsão de Entrega”** está preenchido e a **Modalidade de Frete** selecionada é uma das seguintes opções: **1 – Contratação do Frete por conta do Destinatário (FOB)**; **4 – Transporte Próprio por conta do Destinatário**; **9 – Sem Ocorrência de Transporte**.

**SOLUÇÃO**

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Identifique e selecione a nota fiscal que apresentou a rejeição.

**(3)** Na aba **"Transporte",** verifique a opção selecionada no campo **"CIF / FOB":**

- **''Terceiros''**
- **''Transp. próprio remetente''**
- **''Sem frete''**
- **''Transporte próprio destinatário''**
- **''CIF - Contratação do frente por conta do remetente''**
- **''FOB - Contratação do frete por conta do destinatário''**

**(4)** Corrija a inconsistência conforme o cenário identificado:

Localize o campo “Previsão de Entrega” e remova a data informada caso a modalidade selecionada no campo “CIF/FOB” seja uma das seguintes:

- ''FOB – Contratação do frete por conta do destinatário'';
- ''Transp. próprio destinatário'';
- ''Sem frete''.

Caso a modalidade de transporte correta seja diferente das opções acima, altere o campo **“CIF/FOB”** conforme a necessidade. Nessa situação, a data informada em **“Previsão de Entrega”** poderá ser mantida.

**(5)** Salve as alterações realizadas na nota fiscal.

**(6)** Transmita novamente a nota fiscal para a SEFAZ.

**CAUSA**

Conforme as regras da Sefaz, o preenchimento do campo **"Previsão de Entrega"** não é permitido nas seguintes modalidades de frete:

- FOB - Contratação do frete por conta do destinatário
- Transporte próprio destinatário
- Sem frete
