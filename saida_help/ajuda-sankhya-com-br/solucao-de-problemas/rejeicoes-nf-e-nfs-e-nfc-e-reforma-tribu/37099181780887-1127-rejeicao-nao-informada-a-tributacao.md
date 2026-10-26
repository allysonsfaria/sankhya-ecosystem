---
id: "37099181780887"
titulo: "1127 Rejeição: Não informada a Tributação Monofásica de Combustível com Retenção [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099181780887-1127-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-com-Reten%C3%A7%C3%A3o-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:59Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Alíquotas de CBS", "Tributação Monofásica de Combustível", "Como resolver", "Tributação Monofásica de Combustível com Retenção", "Classificação tributária do produto", "ributação Monofásica com Retenção do imposto"]
---

# 1127 Rejeição: Não informada a Tributação Monofásica de Combustível com Retenção [nItem: 999]

**MENSAGEM**

1127 Rejeição: Não informada a Tributação Monofásica de Combustível com Retenção [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida para operação com combustível sujeita à Tributação Monofásica com Retenção, porém o grupo de tributação correspondente não foi informado no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se o produto está corretamente configurado como combustível que exigem tributação monofásica com retenção.

**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação está configurada corretamente para operações com combustíveis.

**(3)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e configure corretamente as alíquotas para tributação monofásica com retenção de combustíveis.

**(4)** Verifique se o indicador **"ind\_gMonoReten"** está configurado como **"1"** na classificação tributária do produto, indicando que é exigida a Tributação Monofásica de Combustível com Retenção.

**(5)** Ao emitir a nota fiscal, certifique-se de que o grupo de Tributação Monofásica com Retenção (ID: UB90) esteja devidamente preenchido para os itens de combustíveis que exigem essa tributação, conforme o Art. 178 da LC 214/2025.

**CAUSA**

A rejeição 1127 ocorre quando a classificação tributária do produto (**cClassTrib**) possui o indicador que exige Tributação Monofásica de Combustível com Retenção (**ind\_gMonoReten = 1**), mas o grupo de Tributação Monofásica com Retenção do imposto (ID: UB90) não foi informado na nota fiscal para o biocombustível a ser misturado, conforme exigido pelo Art. 178 da Lei Complementar 214/2025.
