---
id: "37095237560471"
titulo: "1165 Rejeição: Não é permitido informar a classificação para subapuração do IBS na ZFM na NFC-e modelo 65 [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095237560471-1165-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-a-classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-na-NFC-e-modelo-65-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:49Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NFC-e", "Modelo do Documento", "Alíquotas de CBS", "Alíquotas de IBS", "65 - Nota Fiscal Eletrônica de Venda a Cosumidor", "Classificação para subapuração do IBS na ZFM"]
---

# 1165 Rejeição: Não é permitido informar a classificação para subapuração do IBS na ZFM na NFC-e modelo 65 [nItem: 999]

**MENSAGEM**

1165 Rejeição: Não é permitido informar a classificação para subapuração do IBS na ZFM na NFC-e modelo 65 [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma NFC-e (modelo 65) com informações de classificação para subapuração do IBS na Zona Franca de Manaus (ZFM), a nota fiscal foi rejeitada pela SEFAZ com a mensagem de erro 1165.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Verifique se o modelo de documento fiscal está configurado como NFC-e (modelo 65).

**(3)** Na aba **"NF-e/NFC-e/CF-e"**, confirme se o campo **"Modelo do Documento"** está configurado como **"65 - Nota Fiscal Eletrônica de Venda a Cosumidor''**.

**(4)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(5)** Verifique as configurações de CST do IBS e CBS utilizadas na operação.

**(6)** Remova qualquer informação relacionada à **classificação para subapuração do IBS na ZFM** que esteja sendo enviada na NFC-e.

**(7)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e certifique-se de que não estão sendo configurados benefícios fiscais da ZFM para documentos modelo 65 (NFC-e).

**CAUSA**

A rejeição ocorre porque, de acordo com as regras de validação da SEFAZ (regra UB131-10), **não é permitido informar a classificação para subapuração do IBS na Zona Franca de Manaus (ZFM) em documentos fiscais do modelo 65 (NFC-e)**.

Esta restrição está alinhada com a Lei Complementar 214/2025, que estabelece tratamentos diferenciados para a ZFM, mas que são aplicáveis apenas para documentos fiscais modelo 55 (NF-e).

Os benefícios fiscais relacionados à ZFM, incluindo créditos presumidos e classificações específicas para subapuração do IBS, são exclusivos para operações documentadas por NF-e (modelo 55), não sendo aplicáveis às operações de varejo documentadas por NFC-e (modelo 65).
