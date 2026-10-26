---
id: "37225721331735"
titulo: "E0472 Rejeição: A data de emissão do documento informado na DPS não pode ser posterior à data de competência da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225721331735-E0472-Rejei%C3%A7%C3%A3o-A-data-de-emiss%C3%A3o-do-documento-informado-na-DPS-n%C3%A3o-pode-ser-posterior-%C3%A0-data-de-compet%C3%AAncia-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:41Z"
rotulos: ["NF-e", "SEFAZ", "NFS-e", "Regra de validação", "Erro", "Declaração de Prestação de Serviços (DPS)", "Sefaz valida a cronologia temporal", "Data de emissão é posterior à data de competência", "Data de emissão do documento informado na DP"]
---

# E0472 Rejeição: A data de emissão do documento informado na DPS não pode ser posterior à data de competência da DPS.

**MENSAGEM**

E0472 Rejeição: A data de emissão do documento informado na DPS não pode ser posterior à data de competência da DPS.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o usuário informou um documento fiscal cuja **data de emissão é posterior à data de competência** declarada na DPS. Esta inconsistência temporal viola as regras de validação da Sefaz, resultando na rejeição do documento eletrônico.

**SOLUÇÃO**

Para corrigir esta rejeição, ajuste as datas do documento fiscal seguindo os passos abaixo:

**(1)** Verifique a **"Data de Competência"** informada na DPS que está sendo transmitida.

**(2)** Acesse o documento fiscal vinculado à DPS e localize o campo **"Data de Emissão"**.

**(3)** Certifique-se de que a **"Data de Emissão"** do documento seja **igual ou anterior** à **"Data de Competência"** da DPS.

**(4)** Caso a data de emissão esteja incorreta, ajuste-a para uma data válida que respeite a regra de validação.

**(5)** Salve as alterações realizadas no documento fiscal.

**(6)** Reenvie a DPS para autorização junto à Sefaz.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida a cronologia temporal** dos documentos fiscais vinculados à DPS. A **data de emissão** do documento não pode ser **posterior à data de competência** declarada, pois isso caracteriza uma **inconsistência lógica**: um documento não pode ser emitido em uma data futura em relação ao período de competência ao qual ele se refere. Esta validação garante a **integridade e veracidade** das informações prestadas ao fisco.
