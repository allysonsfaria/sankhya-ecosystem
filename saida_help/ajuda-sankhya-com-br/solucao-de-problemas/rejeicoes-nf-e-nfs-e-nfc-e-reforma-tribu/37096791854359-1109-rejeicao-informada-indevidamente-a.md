---
id: "37096791854359"
titulo: "1109 Rejeição: Informada indevidamente a Tributação Monofásica Retida anteriormente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37096791854359-1109-Rejei%C3%A7%C3%A3o-Informada-indevidamente-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-Retida-anteriormente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:10Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "SEFAZ", "Impostos", "Assistente de Configuração Integral da Reforma Tributária", "Tributação Monofásica Retida anteriormente", "Classificação do ICMS", "grupo de tributação monofásica retida anteriormente", "indicador \"ind_gMonoRet\""]
---

# 1109 Rejeição: Informada indevidamente a Tributação Monofásica Retida anteriormente [nItem: 999]

**MENSAGEM**

1109 Rejeição: Informada indevidamente a Tributação Monofásica Retida anteriormente [nItem: 999]

**SITUAÇÃO**

Rejeição apresentada na validação do documento fiscal em razão de inconsistência relacionada ao grupo **Tributação Monofásica Retida anteriormente** no item da nota.

**SOLUÇÃO**

**(1)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está corretamente classificado quanto à tributação monofásica de combustíveis.

**(2)** Verifique o campo **"Classificação ICMS"** do produto e certifique-se de que está configurado adequadamente para o tipo de produto em questão.

**(3)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o indicador **"ind\_gMonoRet"** está configurado como 0 (zero) para a classificação tributária do produto.

**(4)** Caso o produto não deva ter tributação monofásica retida anteriormente, remova este grupo de tributação da nota fiscal, ajustando a configuração tributária do item.

**(5)** Se o produto realmente deve ter tributação monofásica retida anteriormente, ajuste a classificação tributária do produto para uma que permita este tipo de tributação (com indicador **"ind\_gMonoRet"** = 1).

**CAUSA**

A rejeição 1109 ocorre devido a uma inconsistência entre a classificação tributária do produto e a informação de tributação monofásica retida anteriormente na nota fiscal. Conforme a regra de validação UB94-20, quando a classificação tributária do produto possui o indicador **"ind\_gMonoRet"** = 0 (que não permite tributação monofásica de combustível cobrada anteriormente), não deve ser informado o grupo de tributação monofásica retida anteriormente (ID: UB94).

Esta validação está baseada no artigo 180 da Lei Complementar 214/2025, que estabelece regras específicas para a tributação monofásica de combustíveis. Quando um produto não se enquadra nas condições previstas neste artigo para ter tributação monofásica retida anteriormente, a inclusão deste grupo tributário na nota fiscal gera a rejeição.
