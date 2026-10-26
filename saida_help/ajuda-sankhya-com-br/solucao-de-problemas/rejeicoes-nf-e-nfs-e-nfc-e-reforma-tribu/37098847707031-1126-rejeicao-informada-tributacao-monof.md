---
id: "37098847707031"
titulo: "1126 Rejeição: Informada Tributação Monofásica de Combustível indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098847707031-1126-Rejei%C3%A7%C3%A3o-Informada-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:08Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Tributação Monofásica de Combustível", "Classificação Tributária", "Regime de tributação"]
---

# 1126 Rejeição: Informada Tributação Monofásica de Combustível indevidamente [nItem: 999]

**MENSAGEM**

1126 Rejeição: Informada Tributação Monofásica de Combustível indevidamente [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com indicação de Tributação Monofásica de Combustível para produto que não se enquadra nesse regime de tributação conforme as regras estabelecidas no Art. 172 da Lei Complementar 214/2025.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique se o produto em questão realmente se enquadra na tributação monofásica de combustíveis. Caso não se enquadre, **remova** a informação de tributação monofásica do documento fiscal.

**(2)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e verifique a **Classificação ICMS** do produto.

- Certifique-se de que está corretamente configurada de acordo com a natureza do produto.

**(3)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a configuração do tipo de operação está adequada para o produto em questão.

**(4)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se o indicador **"ind\_gMonoPadrao"** está configurado como 0 (zero) para o CST utilizado, indicando que não permite a Tributação Monofásica de Combustível.

**CAUSA**

A rejeição 1126 ocorre quando o sistema identifica que foi informada indevidamente a Tributação Monofásica de Combustível (id: UB84a) para um produto que não se enquadra nesse tipo de tributação. Conforme a regra de validação UB84a-20, quando a classificação tributária (cClassTrib) possui indicador que não permite Tributação Monofásica de Combustível (ind\_gMonoPadrao = 0), não deve ser informada a Tributação Monofásica, observado o Art. 172 da LC 214/2025.

Esta inconsistência pode ocorrer devido a uma configuração incorreta do produto, do tipo de operação ou da classificação tributária no sistema, resultando na tentativa de aplicar um regime tributário inadequado para o item em questão.
