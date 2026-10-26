---
id: "37097699277207"
titulo: "1078 Rejeição: Total Devolvido do IBS UF difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097699277207-1078-Rejei%C3%A7%C3%A3o-Total-Devolvido-do-IBS-UF-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:32Z"
rotulos: ["Fiscal", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Alíquotas de IBS", "Como resolver", "Soma dos itens", "IBS UF informados nos itens", "Total Devolvido do IBS UF"]
---

# 1078 Rejeição: Total Devolvido do IBS UF difere da soma dos itens

**MENSAGEM**

1078 Rejeição: Total Devolvido do IBS UF difere da soma dos itens

**SITUAÇÃO**

Ao emitir uma Nota Fiscal Eletrônica (NF-e) com valores de IBS da UF (Imposto sobre Bens e Serviços da Unidade Federativa), o documento foi rejeitado pela SEFAZ porque o valor total do IBS UF informado no grupo de totais da nota não corresponde à soma dos valores de IBS UF informados em cada item da nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a nota fiscal rejeitada e verifique os valores de IBS UF informados em cada item da nota.

**(2)** Some manualmente os valores do campo **"vIBSUF"** de todos os itens da nota fiscal.

**(3)** Compare o resultado da soma com o valor total do IBS UF informado no grupo de totais da nota (campo **"vIBSUF"** dentro do grupo **"total"**).

**(4)** Caso haja divergência, ajuste os valores dos itens ou o valor total para que sejam compatíveis entre si.

**(5)** Após os ajustes, gere o lote novamente e envie a nota fiscal para autorização. 

**CAUSA**

Esta rejeição ocorre devido a uma **inconsistência matemática** entre os valores de IBS UF informados nos itens da nota fiscal e o valor total informado no grupo de totais do documento. De acordo com as regras de validação da SEFAZ, o valor total do IBS UF deve ser **exatamente igual** à soma dos valores de IBS UF de cada item da nota fiscal.

Esta validação é semelhante a outras validações de totalização já existentes, como a que verifica se o valor total do ICMS Interestadual da UF de destino corresponde ao somatório dos itens, garantindo a consistência matemática do documento fiscal eletrônico.
