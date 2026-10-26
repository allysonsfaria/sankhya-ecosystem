---
id: "37225694437527"
titulo: "E0470 Rejeição: Não informar o campo de descrição no caso ideDedRed diferente a 99 – Outras deduções."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225694437527-E0470-Rejei%C3%A7%C3%A3o-N%C3%A3o-informar-o-campo-de-descri%C3%A7%C3%A3o-no-caso-ideDedRed-diferente-a-99-Outras-dedu%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:42Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Lei Complementar nº 214/2025", "Código de identificação de dedução ou redução (ideDedRed)", "Dedução ou redução de base de cálculo", "Secretaria da Fazenda (Sefaz)", "Descrição da dedução/redução seja obrigatoriamente preenchido", "Nota Fiscal Eletrônica (NF-e)", "Nota Fiscal de Consumidor Eletrônica (NFC-e)", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# E0470 Rejeição: Não informar o campo de descrição no caso ideDedRed diferente a 99 – Outras deduções.

**MENSAGEM**

E0470 Rejeição: Não informar o campo de descrição no caso ideDedRed diferente a 99 – Outras deduções.

**SITUAÇÃO**

Durante a emissão de uma **Nota Fiscal Eletrônica (NF-e)** ou **Nota Fiscal de Consumidor Eletrônica (NFC-e)**, o sistema rejeitou o documento, impedindo a sua autorização, ao identificar uma inconsistência no preenchimento das informações de **dedução ou redução de base de cálculo** relacionadas ao **IBS** ou à **CBS**.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize a alíquota utilizada na operação que gerou a rejeição.

**(3)** Verifique se há configuração de **dedução ou redução de base de cálculo** para o IBS ou CBS nesta alíquota.

**(3)** Na aba **''Identificação''** na seção **''Dados do Produto/Serviço''**, verifique qual código está selecionado:

- Caso o código informado seja **diferente de “99 – Outras deduções”**, certifique-se de que o **campo de descrição correspondente esteja devidamente preenchido**, contendo informações claras e objetivas sobre a **natureza da dedução ou redução** aplicada.
- Quando o código informado for **“99 – Outras deduções”**, o **preenchimento do campo de descrição é opcional**, não sendo obrigatório para esse código específico.

**(4)** **Caso o campo de descrição esteja vazio e o código seja diferente de “99 – Outras deduções”**, preencha o **campo de descrição** com informações **claras e detalhadas** sobre a **dedução ou redução aplicada**, conforme orientação do **contador responsável**.

**(5)** Salve as alterações.

**(6)** Reemita o **documento fiscal eletrônico** e verifique se a **rejeição foi solucionada**.

**CAUSA**

A rejeição ocorre porque a **Secretaria da Fazenda (Sefaz)** exige que, quando for informado um **código de identificação de dedução ou redução (ideDedRed)** diferente de **"99 - Outras deduções"**, o campo de **descrição da dedução/redução seja obrigatoriamente preenchido**. Esta validação garante que as informações fiscais sobre deduções e reduções de base de cálculo do IBS e CBS estejam **devidamente documentadas e justificadas** no documento fiscal eletrônico, em conformidade com as regras da **Reforma Tributária** estabelecidas pela **Lei Complementar nº 214/2025**.
