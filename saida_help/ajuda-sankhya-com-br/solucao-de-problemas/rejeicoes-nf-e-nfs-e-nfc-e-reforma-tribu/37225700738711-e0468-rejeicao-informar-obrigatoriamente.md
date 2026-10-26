---
id: "37225700738711"
titulo: "E0468 Rejeição: Informar, obrigatoriamente, o campo de descrição no caso ideDedRed igual a 99 – Outras deduções."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225700738711-E0468-Rejei%C3%A7%C3%A3o-Informar-obrigatoriamente-o-campo-de-descri%C3%A7%C3%A3o-no-caso-ideDedRed-igual-a-99-Outras-dedu%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:43Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Reforma Tributária", "Legislação da Reforma Tributária", "Alíquotas de CBS", "Alíquotas de IBS", "Campo de descrição no caso ideDedRed", "Deduções da base de cálculo do IBS e CBS", "Identificador de dedução ou redução"]
---

# E0468 Rejeição: Informar, obrigatoriamente, o campo de descrição no caso ideDedRed igual a 99 – Outras deduções.

**MENSAGEM**

E0468 Rejeição: Informar, obrigatoriamente, o campo de descrição no caso ideDedRed igual a 99 – Outras deduções.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e com informações de **deduções da base de cálculo do IBS e CBS**, o documento é rejeitado pela Sefaz quando o campo **"Identificador de dedução ou redução"** está preenchido com a opção **"99 - Outras deduções"**, mas o campo de **descrição complementar** não foi informado.

**SOLUÇÃO**

**(1)** Acesse a tela **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e/ou **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize o cadastro de alíquota utilizado na operação que gerou a rejeição.

**(2)** Na aba **''Tributação'**', verifique o campo do **''Código de Classificação Tributária''** e confirme se o campo **''% de Redução de Alíquota''** está preenchido corretamente conforme a legislação.

**(3)** Salve as alterações realizadas no cadastro.

**(4)** Realize novamente a emissão do documento fiscal para validar as correções junto à Sefaz.

**CAUSA**

A rejeição ocorre porque a **legislação da Reforma Tributária** exige que, quando o identificador de dedução ou redução for igual a **"99 - Outras deduções"**, seja informada obrigatoriamente uma **descrição complementar** que especifique a natureza da dedução aplicada. Sem essa informação, o documento fiscal não atende aos requisitos de validação da Sefaz e é rejeitado.
