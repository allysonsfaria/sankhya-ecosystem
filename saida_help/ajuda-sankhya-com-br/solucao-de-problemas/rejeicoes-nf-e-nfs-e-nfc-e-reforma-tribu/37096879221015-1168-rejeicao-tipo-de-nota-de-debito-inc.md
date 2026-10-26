---
id: "37096879221015"
titulo: "1168 Rejeição: Tipo de Nota de Débito incompatível com o CST [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096879221015-1168-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-D%C3%A9bito-incompat%C3%ADvel-com-o-CST-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:04Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "CST", "Transferência de Crédito", "Nota de Débito incompatível com o CST", "Nota Fiscal de Débito (finNFe=6)", "grupo IBSCBS\\gTransfCred (grupo de transferência de crédito)"]
---

# 1168 Rejeição: Tipo de Nota de Débito incompatível com o CST [nItem: 999]

**MENSAGEM**

1168 Rejeição: Tipo de Nota de Débito incompatível com o CST [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal de Débito (finNFe=6) com transferência de crédito, o sistema está rejeitando a operação porque o tipo de nota de débito selecionado não é compatível com o CST informado no grupo de transferência de crédito (gTransfCred).

**SOLUÇÃO**

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o tipo de operação utilizado para emissão da nota fiscal de débito.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"NF-e"** está configurado com a opção **"Nota de Débito"**.

**(3)** No campo **"Tipo de Nota Fiscal de Débito"**, selecione uma das opções compatíveis com o CST informado no grupo de transferência de crédito: **"01 - Transferência de créditos para Cooperativas"** **"05 - Transferência de crédito de sucessão"**.

**(4)** Salve as alterações e tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre porque, de acordo com a regra de validação UB106-31 da Sefaz, quando informado o grupo IBSCBS\gTransfCred (grupo de transferência de crédito), o tipo de nota de débito deve ser **obrigatoriamente** "05 - Transferência de crédito de sucessão" ou "01 - Transferência de créditos para Cooperativas". Qualquer outro tipo de nota de débito informado resultará nesta rejeição.

A validação faz parte das regras implementadas para a Reforma Tributária, garantindo que as transferências de crédito de IBS e CBS sejam realizadas apenas nas situações previstas na legislação.
