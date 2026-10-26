---
id: "37098858134935"
titulo: "1128 Rejeição: Informada indevidamente a Tributação Monofásica de Combustível com Retenção [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098858134935-1128-Rejei%C3%A7%C3%A3o-Informada-indevidamente-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:06Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Tributação Monofásica", "Passos para resolver", "Erro", "Como Resolver", "Tributação Monofásica de Combustível", "Tributação Monofásica de Combustível com Retenção", "Retenção do Imposto"]
---

# 1128 Rejeição: Informada indevidamente a Tributação Monofásica de Combustível com Retenção [nItem: 999]

**MENSAGEM**

1128 Rejeição: Informada indevidamente a Tributação Monofásica de Combustível com Retenção [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com **indicação de Tributação Monofásica com Retenção** sobre biocombustível a ser misturado para produto cuja classificação tributária não permite esse enquadramento.

**SOLUÇÃO**

**(1)** Verifique se o produto possui tributação monofásica com retenção. Se não for o caso, acesse a tela **''Tipos de Operação - TOP''** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e selecione o TOP utilizado na operação.

**(2)** Na aba ''**Impostos''**, verifique se os campos **“Tem CBS”** e **“Tem IBS”** estão marcados indevidamente. Caso estejam selecionados, desmarque as opções correspondentes.

**(3)** Caso o produto realmente deva ter tributação monofásica com retenção, acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique a **Classificação ICMS** do produto.

**(4)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se a classificação tributária do produto está configurada corretamente com o indicador **"ind\_gMonoReten"** definido como 1 (permitido).

**(5)** Ajuste a classificação tributária do produto para que seja compatível com a tributação monofásica com retenção, conforme estabelecido no Art. 178 da LC 214/2025.

**CAUSA**

A rejeição 1128 ocorre quando o sistema detecta que foi informada indevidamente a Tributação Monofásica com Retenção do imposto (id: UB90) sobre o biocombustível a ser misturado, enquanto a classificação tributária do produto possui o indicador **ind\_gMonoReten = 0**, o que significa que este tipo de produto não permite a tributação monofásica com retenção.

Esta validação está baseada no Art. 178 da Lei Complementar 214/2025, que estabelece regras específicas para a tributação monofásica de combustíveis. Quando o indicador **ind\_gMonoReten** está configurado como 0 na classificação tributária do produto, o sistema entende que este produto não deve ter a tributação monofásica com retenção aplicada, e qualquer tentativa de informar este tipo de tributação resultará na rejeição 1128.
