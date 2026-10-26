---
id: "37098961170711"
titulo: "1014 Rejeição: CST do Imposto Seletivo informado inexistente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098961170711-1014-Rejei%C3%A7%C3%A3o-CST-do-Imposto-Seletivo-informado-inexistente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:03Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Reforma Tributária", "NF-e ou NFC-e", "Imposto Seletivo", "CST do Imposto Seletivo", "Tabela de Códigos de Situação Tributária"]
---

# 1014 Rejeição: CST do Imposto Seletivo informado inexistente [nItem: 999]

**MENSAGEM**

1014 Rejeição: CST do Imposto Seletivo informado inexistente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) com produtos sujeitos ao Imposto Seletivo (IS), o documento foi rejeitado pela SEFAZ porque o Código de Situação Tributária (CST) do Imposto Seletivo informado não existe na tabela de códigos válidos estabelecida pela legislação.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(2)** Localize o produto que está gerando a rejeição e verifique a configuração do **"CST do Imposto Seletivo"** atribuído a ele.

**(3)** Selecione um **CST válido** para o Imposto Seletivo conforme a tabela de códigos estabelecida pela legislação da Reforma Tributária.

**(4)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto em questão.

**(5)** Na aba ''Impostos'' verifique se o **''NCM''** está configurado corretamente.

**(6)** Após realizar as correções, tente emitir a nota fiscal novamente. 

**CAUSA**

Esta rejeição ocorre quando o sistema envia um código de CST do Imposto Seletivo que não consta na tabela de Códigos de Situação Tributária válidos para o Imposto Seletivo. O Imposto Seletivo, introduzido pela Reforma Tributária (Lei Complementar nº 214/2025), possui uma tabela específica de CSTs que devem ser utilizados corretamente na emissão de documentos fiscais eletrônicos.

A regra de validação UB02-10 da SEFAZ verifica se o CST do Imposto Seletivo informado existe na tabela oficial. Quando um código inexistente é informado, a nota é rejeitada com o código 1014.
