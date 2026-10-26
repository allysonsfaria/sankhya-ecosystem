---
id: "37097446922263"
titulo: "1038 Rejeição: DFeReferenciado não informado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097446922263-1038-Rejei%C3%A7%C3%A3o-DFeReferenciado-n%C3%A3o-informado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:43Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Passos para resolver", "Erro", "Como Resolver", "Nota de Débito", "CST do IBS/CBS", "Transferência de Crédito do IBS/CBS", "DFeReferenciado", "Documentos Eletrônicos"]
---

# 1038 Rejeição: DFeReferenciado não informado [nItem: 999]

**MENSAGEM**

1038 Rejeição: DFeReferenciado não informado [nItem: 999]

**SITUAÇÃO**

A NF-e foi emitida com CST do IBS/CBS que exige a indicação de documento fiscal referenciado, porém a referência ao documento anterior não foi informada.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a finalidade da nota está configurada corretamente para operações de transferência de crédito.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, certifique-se de que o campo **"NF-e"** esteja configurado com a finalidade **''Nota de Débito"** para operações de transferência de crédito.

**(3)** Verifique se o campo **"Tipo de Nota Fiscal de Débito"** está configurado como **"05 - Transferência de crédito de sucessão"** ou **"01 - Transferência de créditos para Cooperativas"**, conforme a operação que está sendo realizada.

**(4)** Ao emitir a nota fiscal, acesse a aba de **"Documentos Referenciados"** e adicione o documento fiscal eletrônico que originou o crédito a ser transferido.

**(5)** Preencha corretamente todos os dados do documento referenciado, como chave de acesso, número da nota, série e data de emissão.

**(6)** Certifique-se de que o CST do IBS/CBS utilizado na nota seja compatível com operações de transferência de crédito e que os valores do IBS e da CBS sejam maiores que zero.

**CAUSA**

Esta rejeição ocorre devido à exigência da Sefaz de que, em operações específicas como transferência de crédito do IBS/CBS, seja informado o documento fiscal eletrônico que originou o crédito a ser transferido. Conforme as regras de validação UB106-30 e UB106-31, quando a nota fiscal é emitida com finalidade de débito (finNFe=6) e o tipo de nota de débito é "05 - Transferência de crédito de sucessão" ou "01 - Transferência de créditos para Cooperativas", é obrigatório informar o grupo de transferência de crédito e, consequentemente, o documento fiscal referenciado que originou esse crédito. A ausência dessa informação resulta na rejeição 1038.
