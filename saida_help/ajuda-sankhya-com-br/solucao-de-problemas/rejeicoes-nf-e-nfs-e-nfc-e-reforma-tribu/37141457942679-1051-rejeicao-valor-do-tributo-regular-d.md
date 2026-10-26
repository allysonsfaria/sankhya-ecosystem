---
id: "37141457942679"
titulo: "1051 REJEIÇÃO: Valor do Tributo Regular do Município difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141457942679-1051-REJEI%C3%87%C3%83O-Valor-do-Tributo-Regular-do-Munic%C3%ADpio-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:16Z"
rotulos: ["Configuração", "NF-e", "Cidades", "SEFAZ", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS", "valor do Tributo Regular do IBS Municipal", "grupo de Tributação Regular", "Valor do Tributo Regular do IBS Municipal", "Alíquota Regular do IBS do Município"]
---

# 1051 REJEIÇÃO: Valor do Tributo Regular do Município difere do calculado [nItem: 999]

**MENSAGEM**

1051 Rejeição: Valor do Tributo Regular do Município difere do calculado [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com a informação do valor do Tributo Regular do IBS Municipal no grupo de Tributação Regular, apresentando divergência em relação ao valor esperado para esse enquadramento no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) utilizada no item rejeitado, confirmando se o CST informado exige tributação regular.

**(2)** Confira se a **"grupo de Tributação Regular"** (cClassTrib) está corretamente configurada e se possui indicador que exige informação do grupo de Tributação Regular.

**(3)** Verifique a **"Base de Cálculo"** (vBC) informada no grupo gIBSCBS e certifique-se de que está correta.

**(4)** Confira o campo **''Alíquota Regular do IBS do Município'**' (pAliqEfetRegIBSMun) informada no grupo gTribRegular.

**(5)** Recalcule o **"Valor do Tributo Regular do IBS Municipal"** (vTribRegIBSMun) utilizando a fórmula:

```
vTribRegIBSMun = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegIBSMun / 100)
```

**(6)** Corrija o valor do "Tributo Regular do IBS Municipal" (vTribRegIBSMun) no documento fiscal para que corresponda ao valor calculado pela fórmula acima.

**(7)** Reenvie o documento fiscal com os valores corrigidos.

**CAUSA**

A rejeição ocorre porque o valor do Tributo Regular do IBS Municipal (vTribRegIBSMun) informado no documento fiscal está diferente do valor calculado pela Sefaz. Conforme a regra de validação UB72b-10, quando informado o grupo Tributação Regular (gIBSCBS/gTribRegular), o valor do Tributo Regular do IBS Municipal deve ser resultante da multiplicação da Base de Cálculo pela Alíquota Efetiva Regular do IBS do Município dividida por 100.

Esta inconsistência pode ocorrer devido a:

- Erro no cálculo do valor do tributo no sistema emissor Configuração incorreta das alíquotas efetivas do IBS Municipal Arredondamento incorreto dos valores calculados Falha na aplicação da fórmula de cálculo estabelecida pela legislação
- A validação faz parte das regras estabelecidas pela Lei Complementar 214/2025 para a implementação da Reforma Tributária, garantindo a correta tributação do IBS Municipal no regime de tributação regular.
