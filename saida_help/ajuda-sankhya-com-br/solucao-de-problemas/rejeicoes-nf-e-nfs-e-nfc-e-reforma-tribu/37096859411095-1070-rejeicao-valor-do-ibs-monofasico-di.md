---
id: "37096859411095"
titulo: "1070 Rejeição: Valor do IBS monofásico difere do calculado [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096859411095-1070-Rejei%C3%A7%C3%A3o-Valor-do-IBS-monof%C3%A1sico-difere-do-calculado-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:08Z"
rotulos: ["Configuração", "NF-e", "Impostos", "IBS", "Alíquotas de CBS", "Alíquotas de IBS", "IBS monofásico", "Cálculo do IBS monofásico", "Valor do IBS monofásico", "IBS monofásico difere do calculado", "Valor calculado conforme a fórmula estabelecida pela legislação"]
---

# 1070 Rejeição: Valor do IBS monofásico difere do calculado [nItem: 999]

**MENSAGEM**

1070 Rejeição: Valor do IBS monofásico difere do calculado [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada quando o valor total do **IBS Monofásico do item (vTotIBSMonoItem)** informado na nota fiscal eletrônica está divergente do valor esperado para esse item.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está configutado corretamente para a tributação monofásica do IBS.

**(2)** Confira se o campo **"Classificação ICMS"** está com o valor adequado para produtos sujeitos à tributação monofásica.

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(4)** Verifique se o **"Código de situação tributária"** **(CST)** selecionado permite a utilização do IBS Monofásico.

- O indicador **"ind\_gIBSCBSMono"** deve estar configurado como 1 para permitir a tributação monofásica.

**(5)** Verifique os valores informados nos campos do grupo **"gIBSCBSMono"** e certifique-se de que estão corretos:

- Valor do IBS Monofásico (**"vIBSMono"**)
- Valor do IBS Monofásico Retido (**"vIBSMonoReten"**)
- Valor do IBS Monofásico Diferido (**"vIBSMonoDif"**)

**(6)** Recalcule o valor total do IBS Monofásico do item utilizando a fórmula:

```
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif
```

**(7)** Caso esteja utilizando o **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), verifique se todas as configurações estão corretas para o cálculo do IBS monofásico.

**(8)** Após realizar as correções necessárias, tente emitir a nota fiscal novamente para verificar se a rejeição foi solucionada.

**CAUSA**

A rejeição ocorre devido à **inconsistência no cálculo do valor total do IBS Monofásico** do item (vTotIBSMonoItem). Conforme a regra de validação UB104-10, aplicável aos modelos de documentos 55 e 65, quando informado o **grupo do IBS e CBS monofásico** (grupo: gIBSCBSMono), **o valor total do IBS Monofásico do item deve ser resultante da fórmula**:

```
vTotIBSMonoItem = vIBSMono + vIBSMonoReten - vIBSMonoDif.
```

Esta validação está fundamentada no artigo 178 da Lei Complementar 214/2025, que estabelece as regras para a tributação monofásica no contexto da Reforma Tributária. Quando o sistema detecta que o valor informado não corresponde ao resultado da fórmula, a nota fiscal é rejeitada com o código 1070.
