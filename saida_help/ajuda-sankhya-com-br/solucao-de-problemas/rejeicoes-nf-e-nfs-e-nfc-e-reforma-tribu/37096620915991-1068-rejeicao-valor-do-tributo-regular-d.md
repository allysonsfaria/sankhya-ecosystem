---
id: "37096620915991"
titulo: "1068 Rejeição: Valor do Tributo Regular da CBS difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096620915991-1068-Rejei%C3%A7%C3%A3o-Valor-do-Tributo-Regular-da-CBS-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:15Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Código de Situação Tributária", "Classificação Tributária do IBS e da CBS", "Alíquotas de CBS", "Valor do Tributo Regular", "Tributo Regular da CBS difere do calculado", "Valor do Tributo Regular da CBS"]
---

# 1068 Rejeição: Valor do Tributo Regular da CBS difere do calculado [nItem: 999]

**MENSAGEM**

1068 Rejeição: Valor do Tributo Regular da CBS difere do calculado [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma **Nota Fiscal Eletrônica (NF-e)** ou **Nota Fiscal de Consumidor Eletrônica (NFC-e)** com produtos sujeitos à tributação regular da CBS (Contribuição sobre Bens e Serviços), o documento foi rejeitado pela SEFAZ porque o **valor do tributo regular da CBS** informado no documento fiscal está diferente do valor calculado pelo sistema da SEFAZ.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Verifique se o ''**Código de Situação Tributária'' (CST)** utilizado na operação exige o preenchimento do grupo de **Tributação Regular**.

**(3)** Confira se o valor do tributo regular da CBS está sendo calculado corretamente, seguindo a fórmula:

```
vTribRegCBS = gIBSCBS/vBC x (gTribRegular/pAliqEfetRegCBS / 100)
```

Onde:

```
vTribRegCBS = Valor do Tributo Regular da CBS vBC = Base de Cálculo pAliqEfetRegCBS = Alíquota Efetiva Regular da CBS.
```

**(4)** Verifique se a **Classificação Tributária do IBS e da CBS** (cClassTrib) está corretamente configurada e se está exigindo a informação do grupo de Tributação Regular.

**(5)** Após realizar as correções, tente emitir o documento fiscal novamente.

**CAUSA**

Esta rejeição ocorre quando o **valor do tributo regular da CBS informado no documento fiscal não corresponde ao valor calculado pela SEFAZ**, conforme a regra de validação UB72d-10. De acordo com esta regra, quando informado o grupo da Tributação Regular (gIBSCBS/gTribRegular), o valor do tributo regular da CBS (vTribRegCBS) deve ser resultante da multiplicação da Base de Cálculo pela Alíquota Efetiva Regular da CBS dividida por 100.

A divergência pode ocorrer devido a:

- Erro no cálculo do valor do tributo regular da CBS no sistema emissor;
- Configuração incorreta da alíquota efetiva regular da CBS;
- Inconsistência na base de cálculo utilizada Arredondamento incorreto dos valores calculados.

Esta validação está prevista na Lei Complementar 214/2025, que implementa a Reforma Tributária e estabelece as regras para o **cálculo e informação dos tributos IBS e CBS** nos documentos fiscais eletrônicos.
