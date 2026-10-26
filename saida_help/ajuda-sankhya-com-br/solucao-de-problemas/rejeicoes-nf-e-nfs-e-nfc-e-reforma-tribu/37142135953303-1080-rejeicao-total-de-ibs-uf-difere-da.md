---
id: "37142135953303"
titulo: "1080 Rejeição: Total de IBS UF difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37142135953303-1080-Rejei%C3%A7%C3%A3o-Total-de-IBS-UF-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:56Z"
rotulos: ["NF-e", "Central de Vendas", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de IBS", "Total de IBS UF difere da soma", "IBS UF difere", "Soma dos itens"]
---

# 1080 Rejeição: Total de IBS UF difere da soma dos itens

**MENSAGEM**

1080 Rejeição: Total de IBS UF difere da soma dos itens

**SITUAÇÃO**

Ao emitir um documento fiscal (NF-e) com valores de IBS da UF, o sistema identificou uma divergência entre o valor total do IBS da UF informado no grupo de totais do documento e o somatório dos valores de IBS da UF informados em cada item da nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Verifique os valores de IBS da UF em cada item da nota fiscal. Para isso:

- Selecione a aba **"Itens"** da nota fiscal.
- Anote o valor do campo **"vIBSUF"** de cada item.
- Some manualmente todos os valores anotados.

**(3)** Na grade **''Rodapé''**, na aba **''Totais''**, verifique o valor total do IBS da UF da nota fiscal e compare com a soma obtida no passo anterior.

**(4)** Caso identifique divergências, revise os cálculos de IBS em cada item, verificando:

- Se a **Base de cálculo do IBS** está correta em cada item.
- Se o campo **''Alíquota do IBS Estado''** está aplicada corretamente.
- Se existem **Créditos Presumidos** ou **Diferimentos** que possam estar afetando o cálculo.

**(5)** Ajuste os valores conforme necessário, garantindo que o total do IBS da UF seja exatamente igual à soma dos valores de IBS da UF de cada item.

**(6)** Após os ajustes, gere novamente o documento fiscal e envie para autorização.

**CAUSA**

Esta rejeição ocorre devido a uma inconsistência no cálculo do IBS da UF entre os itens e o total do documento fiscal. De acordo com as regras de validação da SEFAZ, o valor total do IBS da UF informado no grupo de totais do documento fiscal deve ser **exatamente igual** à soma dos valores de IBS da UF informados em cada item.

Esta validação é semelhante à que já existia para o ICMS interestadual (rejeição relacionada ao DIFAL), onde o valor total do ICMS Interestadual para a UF de destino deve corresponder ao somatório dos valores dos itens.Com a implementação da Reforma Tributária e a introdução do IBS, conforme a Lei Complementar 214/2025, esta validação foi estendida também para os novos tributos.

Problemas de arredondamento, cálculos incorretos ou inconsistências na aplicação de benefícios fiscais (como diferimentos, créditos presumidos ou reduções de alíquota) podem causar esta divergência entre o total e a soma dos itens.
