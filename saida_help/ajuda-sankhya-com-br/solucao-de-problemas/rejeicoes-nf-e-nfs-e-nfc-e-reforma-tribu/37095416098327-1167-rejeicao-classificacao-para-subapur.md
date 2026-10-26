---
id: "37095416098327"
titulo: "1167 Rejeição: Classificação para subapuração do IBS na ZFM não informada [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095416098327-1167-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-n%C3%A3o-informada-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:47Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "IBS", "Nota Fiscal Eletrônica (NF-e)", "NF-e (modelo 55)", "Alíquotas de CBS", "Alíquotas de IBS", "Nota Fiscal de Crédito", "Subapuração do IBS na Zona Franca de Manaus (ZFM)", "Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM", "ZFM"]
---

# 1167 Rejeição: Classificação para subapuração do IBS na ZFM não informada [nItem: 999]

**MENSAGEM**

1167 Rejeição: Classificação para subapuração do IBS na ZFM não informada [nItem: 999]

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) modelo 55 com o tipo de Nota Fiscal de Crédito configurado como "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM", o documento foi rejeitado pela SEFAZ porque não foi informada a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM).

**SOLUÇÃO**

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o tipo de operação utilizado para emissão da nota fiscal.

**(2)** Na aba **"NF-e/NFC-e/CF-e"**, verifique se o campo **"Tipo de Nota Fiscal de Crédito"** está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**.

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(4)** Verifique se o CST do IBS e CBS utilizado na operação permite a informação do grupo para apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM.

**(5)** Na seção **''Tributação''** do item, localize o grupo do IBS e CBS, e verifique o campo **''Código de Class. do Crédito Presumido''**.

**(6)** Preencha o campo com um dos valores válidos para a classificação de subapuração do IBS na ZFM.

**(7)** Salve as alterações e tente emitir a nota fiscal novamente.

**CAUSA**

A rejeição ocorre porque, de acordo com as regras de validação da SEFAZ, quando uma nota fiscal é emitida com o **Tipo de Nota Fiscal de Crédito** configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"**, é obrigatório informar a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM) para cada item da nota. Esta validação está relacionada às regras específicas para operações na Zona Franca de Manaus, conforme estabelecido na Lei Complementar 214/2025, que implementa a Reforma Tributária.

A classificação para subapuração do IBS na ZFM é necessária para o correto cálculo e apropriação do crédito presumido de IBS sobre o saldo devedor nas operações realizadas na Zona Franca de Manaus. Além disso, conforme a regra de validação UB110-10, não é possível repetir o mesmo Tipo de Classificação para o cálculo do crédito presumido na ZFM em mais de um item do documento fiscal quando o Tipo de Nota de Crédito for "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM".
