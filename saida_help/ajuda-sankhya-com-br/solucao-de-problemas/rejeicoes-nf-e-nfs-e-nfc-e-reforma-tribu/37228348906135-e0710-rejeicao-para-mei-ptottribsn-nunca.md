---
id: "37228348906135"
titulo: "E0710 Rejeição: Para MEI pTotTribSN nunca poderá ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37228348906135-E0710-Rejei%C3%A7%C3%A3o-Para-MEI-pTotTribSN-nunca-poder%C3%A1-ser-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-18T19:33:15Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "NFS-e", "Erro", "Rejeição E0710", "Para MEI pTotTribSN nunca poderá ser informado", "MEI pTotTribSN", "pTotTribSN", "valor aproximado total de tributos do Simples Nacional", "E0710 Rejeição", "MEI"]
---

# E0710 Rejeição: Para MEI pTotTribSN nunca poderá ser informado

**MENSAGEM**

E0710 Rejeição: Para MEI pTotTribSN nunca poderá ser informado.

**SITUAÇÃO**

Ao emitir uma **NFS-e** para um destinatário cadastrado como **Microempreendedor Individual (MEI)**, o sistema preencheu automaticamente o campo **pTotTribSN** (valor aproximado total de tributos do Simples Nacional) no documento fiscal. Ao tentar transmitir o documento eletrônico, a **SEFAZ rejeitou a nota** com a mensagem de erro E0710.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o destinatário da nota fiscal que foi rejeitada.

**(3)** Na aba **''Fiscal''**, verifique se o parceiro está com a marcação **''Micro empresário individual''** está habilitada.

**(4)** Confirme se o cadastro do parceiro está correto:

- Se o destinatário **realmente é MEI**, mantenha a marcação habilitada e prossiga para o próximo passo.
- Se o destinatário **não é MEI**, desabilite a marcação **"Micro empresário individual"** e salve o cadastro.

**(5)** Caso o destinatário seja MEI, verifique a **configuração tributária** utilizada na emissão do documento fiscal e certifique-se de que **não está sendo calculado ou informado o valor aproximado de tributos** (pTotTribSN) para este tipo de contribuinte.

**(6)** Cancele a nota fiscal rejeitada e **emita novamente o documento**, garantindo que o campo **pTotTribSN não seja preenchido** quando o destinatário for MEI.

**(7)** Transmita o documento fiscal novamente para a SEFAZ.

**CAUSA**

A rejeição ocorre porque, de acordo com a **legislação fiscal**, o **Microempreendedor Individual (MEI)** possui um regime tributário diferenciado e simplificado. Por essa razão, **não é permitido informar o valor aproximado de tributos do Simples Nacional (pTotTribSN)** em documentos fiscais destinados a MEI. Quando o sistema identifica que o destinatário é MEI e o campo pTotTribSN está preenchido, a **SEFAZ rejeita automaticamente** o documento com a mensagem E0710.
