---
id: "37141560708503"
titulo: "1138 Rejeição: Não é permitido o uso de Crédito Presumido ZFM na NFC-e modelo 65 [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141560708503-1138-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-uso-de-Cr%C3%A9dito-Presumido-ZFM-na-NFC-e-modelo-65-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:05Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NFC-e", "NFC-e (modelo 65)", "Grupo de crédito presumido do IBS", "Crédito presumido não é permitido para o modelo de documento fiscal NFC-e", "IBS para a Zona Franca de Manaus (grupo: gCredPresIBSZFM)", "Crédito Presumido"]
---

# 1138 Rejeição: Não é permitido o uso de Crédito Presumido ZFM na NFC-e modelo 65 [nItem: 999]

**MENSAGEM**

1138 Rejeição: Não é permitido o uso de Crédito Presumido ZFM na NFC-e modelo 65 [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma **NFC-e (Nota Fiscal de Consumidor Eletrônica – modelo 65)**, o sistema retorna rejeição ao identificar o **preenchimento do grupo de crédito presumido do IBS relacionado à Zona Franca de Manaus (ZFM)**. A rejeição ocorre no momento da validação do documento fiscal eletrônico pela SEFAZ, impedindo a autorização da NFC-e.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique o modelo de documento fiscal que está sendo emitido. Se for uma NFC-e (modelo 65), não utilize o grupo de crédito presumido para a Zona Franca de Manaus.

**(2)** Caso precise utilizar o crédito presumido para a ZFM, altere o modelo do documento fiscal para NF-e (modelo 55), que permite este tipo de crédito.

**(3)** Acesse a tela de [**"Tipos de Operação"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Fiscal » Cadastros » Tipos de Operação) e verifique se o tipo de operação está configurado corretamente para o modelo de documento fiscal que deseja emitir.

**(4)** Acesse a tela **''Alíquota do IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS), e verifique as configurações do CST:

- Certifique-se de que não está sendo utilizado um código que permita o uso de crédito presumido da ZFM em documentos modelo 65.

**(5)** Remova qualquer informação relacionada ao grupo de crédito presumido da ZFM (gCredPresIBSZFM) do documento fiscal modelo 65 antes de tentar emiti-lo novamente.

**CAUSA**

A rejeição ocorre devido a uma regra de validação específica da SEFAZ (UB131-10) que impede o uso do grupo de crédito presumido do IBS para a Zona Franca de Manaus (grupo: gCredPresIBSZFM) em documentos fiscais do modelo 65 (NFC-e). Esta restrição está alinhada com a Lei Complementar 214/2025, que estabelece regras específicas para a apropriação de créditos presumidos relacionados à Zona Franca de Manaus, limitando seu uso apenas para documentos fiscais do modelo 55 (NF-e).
