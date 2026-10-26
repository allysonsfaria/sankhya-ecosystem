---
id: "37141541826455"
titulo: "1158 Rejeição: Tipo de Nota de Crédito não permite o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141541826455-1158-Rejei%C3%A7%C3%A3o-Tipo-de-Nota-de-Cr%C3%A9dito-n%C3%A3o-permite-o-grupo-para-apropria%C3%A7%C3%A3o-de-cr%C3%A9dito-presumido-de-IBS-sobre-o-saldo-devedor-na-ZFM-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:04Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "Crédito", "Impostos", "Regra de validação", "grupo gCredPresIBSZFM", "crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus", "grupo para apropriação de crédito presumido de IBS", "saldo devedor na ZFM"]
---

# 1158 Rejeição: Tipo de Nota de Crédito não permite o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

**MENSAGEM**

1158 Rejeição: Tipo de Nota de Crédito não permite o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM [nItem: 999]

**SITUAÇÃO**

A NF-e foi emitida com a informação de apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus, utilizando o grupo gCredPresIBSZFM, associada a um tipo de nota de crédito diferente do previsto para esse enquadramento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique o tipo de nota de crédito que está sendo utilizado na NF-e através da tela de **"Notas Fiscais"** (Gestão Fiscal » Movimentação » Notas Fiscais).

**(2)** Altere o tipo de nota de crédito para **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (art. 450, § 1º, LC 214/25)"** ou remova o grupo de apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM.

**(3)** Caso opte por alterar o tipo de nota de crédito, certifique-se de que a finalidade da NF-e esteja configurada como **"5 - Nota de crédito"**.

**(4)** Verifique se a empresa emitente está localizada no **Amazonas (UF 13)** e possui inscrição de indústria incentivada, pois apenas empresas com estas características podem utilizar este tipo de nota de crédito.

**(5)** Certifique-se de que a data de emissão da nota seja a partir de **janeiro de 2029**, pois este tipo de nota de crédito só poderá ser utilizado a partir desta data, conforme a regra de validação B25.2-30.

**(6)** Verifique se o CST utilizado permite o uso do grupo de crédito presumido para a ZFM (indicador ind\_gCredPresIBSZFM = 1).

**CAUSA**

Esta rejeição ocorre devido à incompatibilidade entre o tipo de nota de crédito selecionado e a tentativa de informar o grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM. De acordo com a regra de validação UB131-40, o grupo gCredPresIBSZFM só pode ser informado quando o tipo de nota de crédito for **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

A Lei Complementar 214/25, em seu artigo 450, § 1º, estabelece condições específicas para a apropriação de crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus, e a SEFAZ implementou validações rigorosas para garantir que este benefício fiscal seja utilizado apenas nas situações previstas em lei.
