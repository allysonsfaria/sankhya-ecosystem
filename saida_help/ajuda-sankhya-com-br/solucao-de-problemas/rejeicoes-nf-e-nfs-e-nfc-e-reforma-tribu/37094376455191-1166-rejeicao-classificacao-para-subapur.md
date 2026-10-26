---
id: "37094376455191"
titulo: "1166 Rejeição: Classificação para subapuração do IBS na ZFM informado indevidamente. [nitem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37094376455191-1166-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-para-subapura%C3%A7%C3%A3o-do-IBS-na-ZFM-informado-indevidamente-nitem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:51Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NFC-e (modelo 65)", "Classificação para subapuração do IBS", "Crédito presumido para a ZFM", "Zona Franca de Manus (ZFM)"]
---

# 1166 Rejeição: Classificação para subapuração do IBS na ZFM informado indevidamente. [nitem: 999]

**MENSAGEM**

1166 Rejeição: Classificação para subapuração do IBS na ZFM informado indevidamente. [nitem: 999]

**SITUAÇÃO**

Ao emitir uma **NF-e**, o sistema retorna rejeição quando é informada a **classificação para subapuração do IBS na Zona Franca de Manaus (ZFM)** no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(2)** Verifique se os CSTs possuem o indicador **''Permite uso de crédito presumido para a ZFM''** habilitado.

**(3)** Acesse a tela **''Tipos de Operação - TOP''** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de nota fiscal de crédito está configurado.

**(4)** Na aba **''NF-e/NFC-e/CF-e''**, verifique seo  campo ''Tipo de Nota Fiscal de Crédito'' está configurado como **"02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM"** para operações que envolvam crédito presumido na ZFM.

**(5)** Caso esteja emitindo uma **NFC-e (modelo 65)**, remova qualquer informação relacionada ao **Crédito Presumido da Zona Franca de Manaus (ZFM)**, pois essa configuração **não é permitida para este modelo de documento fiscal**.

**(6)** Se o emitente for da **UF Amazonas** e possuir **inscrição como indústria incentivada**, certifique-se de que o **grupo do IBS para fornecimentos a partir da ZFM** esteja corretamente informado nos documentos fiscais, conforme as regras aplicáveis.

**(7)** Verifique se não há **duplicidade do Tipo de Classificação** utilizado para o cálculo do crédito presumido da ZFM em diferentes itens da nota fiscal. Caso exista, ajuste as configurações para evitar a repetição.

**CAUSA**

Esta rejeição ocorre devido a uma incompatibilidade entre o CST do IBS/CBS informado e a classificação para subapuração do IBS na Zona Franca de Manaus. Conforme as regras de validação da SEFAZ (UB131-10, UB131-20 e UB131-30), existem restrições específicas para o uso do grupo de crédito presumido do IBS na ZFM: O CST utilizado deve permitir o uso de crédito presumido para a ZFM (indicador ind\_gCredPresIBSZFM = 1).

Não é permitido o uso de Crédito Presumido ZFM na NFC-e modelo 65. O tipo de nota fiscal de crédito deve ser configurado como "02 - Apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM". Apenas emitentes da UF Amazonas com inscrição de indústria incentivada podem utilizar este grupo. A informação incorreta de qualquer um desses elementos resulta na rejeição do documento fiscal pela SEFAZ.
