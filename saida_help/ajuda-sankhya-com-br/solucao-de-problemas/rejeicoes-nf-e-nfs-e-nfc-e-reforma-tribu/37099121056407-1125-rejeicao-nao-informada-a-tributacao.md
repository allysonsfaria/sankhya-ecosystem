---
id: "37099121056407"
titulo: "1125 Rejeição: Não informada a Tributação Monofásica de Combustível [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099121056407-1125-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-de-Combust%C3%ADvel-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:00Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Combustível", "Tributação Monofásica", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "NF-e ou NFC-e", "Tributação Monofásica de Combustível", "Ausência do grupo de tributação monofásica"]
---

# 1125 Rejeição: Não informada a Tributação Monofásica de Combustível [nItem: 999]

**MENSAGEM**

1125 Rejeição: Não informada a Tributação Monofásica de Combustível [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida para produto classificado como combustível sujeito à Tributação Monofásica, porém o grupo de Tributação Monofásica de Combustível não foi informado no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e verifique se a Classificação ICMS está configurado para um código que exige tributação monofásica de combustível.

**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a TOP utilizada está configurada corretamente para operações com combustíveis.

**(3)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(4)** Configure corretamente as alíquotas para tributação monofásica de combustíveis, verificando se o indicador **"ind\_gMonoPadrao"** está configurado como 1 (exige tributação monofásica).

**(5)** Ao emitir a nota fiscal, certifique-se de que o grupo de tributação monofásica (id: UB84a) esteja sendo informado corretamente para os itens de combustível, conforme exigido pelo Art. 172 da LC 214/2025.

**CAUSA**

A rejeição 1125 ocorre devido à **ausência do grupo de tributação monofásica** (id: UB84a) em um documento fiscal que contém itens classificados como combustíveis. De acordo com a regra de validação UB84a-10, quando o indicador **ind\_gMonoPadrao** está configurado como 1 na classificação tributária do produto, é **obrigatória** a informação da tributação monofásica, conforme estabelecido no Art. 172 da LC 214/2025. Esta validação é aplicada tanto para NF-e (modelo 55) quanto para NFC-e (modelo 65).
