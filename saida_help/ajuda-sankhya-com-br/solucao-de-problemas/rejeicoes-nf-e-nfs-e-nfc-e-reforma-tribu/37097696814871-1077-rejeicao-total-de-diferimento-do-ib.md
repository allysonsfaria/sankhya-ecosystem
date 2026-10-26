---
id: "37097696814871"
titulo: "1077 Rejeição: Total de Diferimento do IBS UF difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097696814871-1077-Rejei%C3%A7%C3%A3o-Total-de-Diferimento-do-IBS-UF-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:33Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de IBS", "Código de Situação Tributária (CST)", "Soma dos itens", "Total de Diferimento do IBS UF", "Valor total do diferimento do IBS da UF"]
---

# 1077 Rejeição: Total de Diferimento do IBS UF difere da soma dos itens

**MENSAGEM**

1077 Rejeição: Total de Diferimento do IBS UF difere da soma dos itens

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com diferimento do IBS da UF, o documento foi rejeitado pela SEFAZ porque o valor total do diferimento informado no documento fiscal não corresponde à soma dos valores de diferimento calculados em cada item.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se o **Código de Situação Tributária (CST)** utilizado nos itens da nota permite o uso de diferimento. Apenas CSTs com indicador de diferimento (ind\_gDif = 1) podem utilizar esta funcionalidade.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se os percentuais de diferimento estão configurados corretamente para cada item.

**(3)** Para cada item da nota que possui diferimento, confira se o valor do diferimento (vDif) está sendo calculado corretamente pela fórmula:

```
vDif = vBC x (pIBSUF / 100) x (pDif / 100) Onde: vBC = Base de cálculo do IBS pIBSUF = Percentual do IBS da UF pDif = Percentual do diferimento
```

**(4)** Verifique se o valor total de **diferimento** informado no documento fiscal corresponde exatamente ao somatório dos valores de diferimento dos itens da nota.

**(5)** Caso identifique divergências, ajuste os valores de diferimento nos itens ou realize o recálculo dos impostos para que o sistema atualize automaticamente os totais do documento.

**CAUSA**

Esta rejeição ocorre quando há uma inconsistência entre o valor total do diferimento do IBS da UF informado no documento fiscal e a soma dos valores de diferimento calculados em cada item. Conforme as regras de validação da SEFAZ, o valor total do diferimento deve ser exatamente igual à soma dos valores de diferimento de todos os itens da nota.

A divergência pode ocorrer por diversos motivos, como:

- Cálculo incorreto do valor de diferimento em um ou mais itens
- Erro na aplicação da fórmula de cálculo do diferimento (vDif = vBC x (pIBSUF / 100) x (pDif / 100))
- Inconsistência nos percentuais de diferimento configurados
- Falha na totalização dos valores de diferimento no documento fiscal

O sistema deve garantir que o valor total do diferimento do IBS da UF seja calculado corretamente, somando os valores de diferimento de todos os itens, conforme exigido pela validação UB23-10 da SEFAZ.
