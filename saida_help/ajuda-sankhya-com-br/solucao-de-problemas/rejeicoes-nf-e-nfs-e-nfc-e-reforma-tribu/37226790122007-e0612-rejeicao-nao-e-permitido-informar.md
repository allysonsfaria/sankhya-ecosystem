---
id: "37226790122007"
titulo: "E0612 Rejeição: Não é permitido informar alíquota quando o benefício municipal informado na DPS for do tipo \"Isenção\" ou \"Alíquota Diferenciada\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226790122007-E0612-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-informar-al%C3%ADquota-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o-ou-Al%C3%ADquota-Diferenciada"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:37Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "Benefício fiscal municipal", "Alíquotas de IBS", "Alíquota Diferenciada", "Isenção", "Alíquota municipal do IBS", "Declaração de Prévia Simplificada", "Documentos Eletrônicos"]
---

# E0612 Rejeição: Não é permitido informar alíquota quando o benefício municipal informado na DPS for do tipo "Isenção" ou "Alíquota Diferenciada".

**MENSAGEM**

E0612 Rejeição: Não é permitido informar alíquota quando o benefício municipal informado na DPS for do tipo "Isenção" ou "Alíquota Diferenciada".

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e/NFC-e), o usuário **informou uma alíquota municipal do IBS** para um item que possui um **benefício fiscal municipal** cadastrado na Declaração de Prévia Simplificada (DPS) do tipo **"Isenção"** ou **"Alíquota Diferenciada"**. Esta combinação não é permitida pela Sefaz, resultando na rejeição do documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize a configuração de alíquota utilizada no documento fiscal rejeitado.

**(2)** Verifique se o campo **"Código de Benefício Fiscal Municipal"** está preenchido com um código do tipo **"Isenção"** ou **"Alíquota Diferenciada".**

**(3)** Realize um dos ajustes abaixo, conforme orientação do seu contador:

- **Opção 1:** Se o benefício fiscal for do tipo **"Isenção"**, certifique-se de que o campo **"Alíquota Municipal IBS"** esteja **zerado ou em branco**. Quando há isenção, não deve ser informada alíquota.
- **Opção 2:** Se o benefício fiscal for do tipo **"Alíquota Diferenciada"**, remova a alíquota do campo **"Alíquota Municipal IBS"**, pois a alíquota diferenciada já está contemplada no próprio benefício fiscal cadastrado na DPS.
- **Opção 3:** Se a operação não possui benefício fiscal de isenção ou alíquota diferenciada, remova ou corrija o **"Código de Benefício Fiscal Municipal"** informado incorretamente.

**(4)** Salve as alterações realizadas na configuração de alíquota.

**(5)** Reemita o documento fiscal eletrônico para que as correções sejam aplicadas e o documento seja aceito pela Sefaz.

**CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que seja informada uma alíquota municipal do IBS quando o benefício fiscal municipal cadastrado na DPS for do tipo **"Isenção"** ou **"Alíquota Diferenciada"**. Isso acontece porque:

- No caso de **isenção**, não há incidência de imposto, portanto, a alíquota deve ser zero ou não informada.
- No caso de **alíquota diferenciada**, a alíquota específica já está definida no próprio benefício fiscal, não sendo necessário informar uma alíquota adicional no campo de alíquota municipal.

A **inconsistência entre o benefício fiscal e a alíquota informada** gera conflito nas regras de validação da Sefaz, resultando na rejeição E0612.
