---
id: "36156238693015"
titulo: "1027 Rejeição: NF referenciada informada indevidamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36156238693015-1027-Rejei%C3%A7%C3%A3o-NF-referenciada-informada-indevidamente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:23:31Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Impostos", "TOP", "Erro", "1027 Rejeição:", "NF referenciada informada indevidamente", "Rejeição 1027", "nota fiscal de \"Crédito\"", "Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"]
---

# 1027 Rejeição: NF referenciada informada indevidamente

**MENSAGEM**

1027 Rejeição: NF referenciada informada indevidamente

**SITUAÇÃO**

Ao emitir uma nota fiscal de **crédito** do tipo **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**, o usuário preencheu ou manteve uma **"NF Referenciada"** na tela de edição da NF-e, isso gerou a rejeição 1027 durante o envio da nota à Sefaz.

**SOLUÇÃO**

**(1)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Localize a nota fiscal que está com a rejeição.

**(3)** Na grade **''Cabeçalho''**, verifique no campo **''Tipo Operação''** o TOP utilizado na nota.

**(4)** Acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP identificado no passo anterior.

**(5)** Na aba **"NF-e/NFC-e/CF-e"** e verifique se no campo **"NF-e"** está selecionada a opção **"Nota de crédito".**

**(6)** Em seguida, no campo **"Tipo de Nota Fiscal de Crédito",** verifique se está selecionada a opção **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**.

**(1)** Caso o TOP seja de **crédito, do tipo "**Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM" **siga os passos abaixo**:

**(7)** Retorne à nota fiscal que apresentou a rejeição, acesse a aba **“NF-e/NFS-e”** e remova todas as notas informadas no campo **“Chave NF-e Referenciada”**.

**(8)** Salve as alterações.

**(9)** Após realizar as correções, transmita novamente a **NF-e** para a **Sefaz**.

**CAUSA**

A rejeição ocorre porque, para notas fiscais do tipo **"Apropriação de Crédito Presumido de IBS sobre o saldo devedor na ZFM"**, não é permitido informar nenhuma **"NF Referenciada"** no XML. A presença da tag **<NFref>** viola a regra da Sefaz, impedindo a transmissão da nota.
