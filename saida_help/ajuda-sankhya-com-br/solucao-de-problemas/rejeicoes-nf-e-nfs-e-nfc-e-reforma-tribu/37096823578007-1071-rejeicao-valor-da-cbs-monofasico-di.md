---
id: "37096823578007"
titulo: "1071 Rejeição: Valor da CBS monofásico difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096823578007-1071-Rejei%C3%A7%C3%A3o-Valor-da-CBS-monof%C3%A1sico-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:06Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Alíquotas de CBS", "Alíquotas de IBS", "Tributação monofásica da CBS", "CBS monofásico difere do calculado", "Código de Situação Tributária'"]
---

# 1071 Rejeição: Valor da CBS monofásico difere do calculado [nItem: 999]

**MENSAGEM**

1071 Rejeição: Valor da CBS monofásico difere do calculado [nItem: 999]

**SITUAÇÃO**

Ao emitir uma nota fiscal eletrônica (NF-e/NFC-e) com produtos sujeitos à tributação monofásica da CBS, o documento foi rejeitado pela SEFAZ porque o valor total da CBS Monofásica do item não está sendo calculado corretamente conforme a fórmula estabelecida pela legislação.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configurado corretamente para a tributação monofásica da CBS.

**(2)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(3)** Verifique se o campo **''Código de Situação Tributária''** **(CST)** configurado é compatível com a tributação monofásica da CBS.

**(4)** Certifique-se de que os valores dos campos **"CBS Monofásico"**, **"CBS Monofásico Retido"** e **"CBS Monofásico Diferido"** estão preenchidos corretamente na nota fiscal.

**(5)** Verifique se o cálculo do valor total da CBS Monofásica está seguindo a fórmula:

```
vTotCBSMonoItem = vCBSMono + vCBSMonoReten - vCBSMonoDif.
```

**(6)** Caso necessário, ajuste os valores manualmente na tela de emissão da nota fiscal para garantir que o cálculo esteja correto.

**(7)** Se o problema persistir, verifique se o **"Tipo de Operação (TOP)"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) está configurado corretamente para operações com produtos sujeitos à tributação monofásica.

**CAUSA**

Esta rejeição ocorre quando o valor total da CBS Monofásica do item (vTotCBSMonoItem) informado na nota fiscal **não corresponde** ao resultado da fórmula: vTotCBSMonoItem = vCBSMono + vCBSMonoReten - vCBSMonoDif. De acordo com a regra de validação UB105-10 da SEFAZ, quando informado o grupo do IBS e CBS monofásico (gIBSCBSMono), o valor total da CBS Monofásica do item deve ser calculado conforme a fórmula mencionada.

Esta validação está em conformidade com as disposições da Lei Complementar 214/2025, que estabelece as regras para a tributação monofásica no âmbito da Reforma Tributária. O erro pode ocorrer devido a **inconsistências no cadastro do produto**, **configuração incorreta das alíquotas** ou **falha no cálculo automático** dos valores durante a emissão da nota fiscal.
