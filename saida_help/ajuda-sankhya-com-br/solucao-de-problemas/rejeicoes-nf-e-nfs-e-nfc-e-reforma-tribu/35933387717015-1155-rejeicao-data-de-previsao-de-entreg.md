---
id: "35933387717015"
titulo: "1155 Rejeição: Data de previsão de entrega anterior ao permitido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35933387717015-1155-Rejei%C3%A7%C3%A3o-Data-de-previs%C3%A3o-de-entrega-anterior-ao-permitido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:24:21Z"
rotulos: ["Fiscal", "NF-e", "Central de Vendas", "SEFAZ", "Erro", "Data de previsão de entrega anterior ao permitido", "1155 Rejeição", "Rejeição 1155", "Data de saída", "Data prevista de entrega"]
---

# 1155 Rejeição: Data de previsão de entrega anterior ao permitido

**MENSAGEM**

1155 Rejeição: Data de previsão de entrega anterior ao permitido.

**SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar transmitir uma nota fiscal cuja **"Data de Previsão de Entrega"** é anterior à **"Data de Saída"**. O erro ocorre durante o envio da nota fiscal para a SEFAZ, impedindo a autorização do documento.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**(2)** Localize e selecione a **nota fiscal** que apresentou a rejeição.

**(3)** Na aba **''Cabeçalho''** verifique as datas informadas nos campos:

- **''Dt. Entrada/Saída''**
- **''Previsão de entrega''**

**(4)** Se necessário, ajuste o campo "Previsão de Entrega" para que a data seja **igual ou posterior** à "Data de Saída", garantindo a consistência das informações.

**(5)** Após realizar os ajustes, **salve a nota fiscal** e efetue **novo envio para a SEFAZ**.

**CAUSA**

O erro ocorre porque a **"Data de Previsão de Entrega"** foi informada como anterior à **"Data de Saída"**, o que não é permitido pela legislação fiscal.
