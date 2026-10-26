---
id: "37095667941783"
titulo: "1017 Rejeição: Obrigatório informação de alíquota específica de Imposto Seletivo [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095667941783-1017-Rejei%C3%A7%C3%A3o-Obrigat%C3%B3rio-informa%C3%A7%C3%A3o-de-al%C3%ADquota-espec%C3%ADfica-de-Imposto-Seletivo-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:38Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Reforma Tributária", "Alíquotas de IBS", "Assistente de Configuração Integral da Reforma Tributária", "Imposto Seletivo", "Alíquota Específica", "Alíquota específica de Imposto Seletivo", "Falta de informação da alíquota específica do Imposto Seletivo"]
---

# 1017 Rejeição: Obrigatório informação de alíquota específica de Imposto Seletivo [nItem: 999]

**MENSAGEM**

1017 Rejeição: Obrigatório informação de alíquota específica de Imposto Seletivo [nItem: 999]

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com produtos sujeitos ao Imposto Seletivo, enquadrados em NCMs específicos, sem a informação da alíquota específica do Imposto Seletivo no documento fiscal ou com essa alíquota registrada com valor zero.

**SOLUÇÃO**

**(1)** Acesse a tela **"Assistente de Configuração Integral da Reforma Tributária"** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(2)** Localize a aba **"Imposto Seletivo"** e verifique se o produto com NCM sujeito ao Imposto Seletivo (2401, 2402, 2403, 2404, 2203, 2204, 2205, 2206, 2208) está configurado corretamente.

**(3)** Certifique-se de que o campo **"Alíquota Específica"** esteja preenchido com um valor maior que zero para os produtos com os NCMs mencionados.

**(4)** Verifique também se o **"CSTIS"** (Código de Situação Tributária do Imposto Seletivo) está configurado corretamente para o produto, de acordo com a operação realizada.

**(5)** Após realizar as configurações necessárias, tente emitir o documento fiscal novamente.

**CAUSA**

A rejeição 1017 ocorre devido à **falta de informação da alíquota específica do Imposto Seletivo** para produtos com NCMs específicos (2401, 2402, 2403, 2404, 2203, 2204, 2205, 2206, 2208). Conforme a regra de validação UB07-10, quando o CSTIS exige o grupo do Imposto Seletivo e o produto possui um dos NCMs mencionados, é obrigatório informar a alíquota específica (tag: imposto/IS/pISEspec) com valor diferente de zero.

Esta regra faz parte das implementações da Reforma Tributária, conforme a Lei Complementar 214/2025, que estabelece a tributação específica para produtos como tabaco, bebidas alcoólicas e outros itens sujeitos ao Imposto Seletivo.
