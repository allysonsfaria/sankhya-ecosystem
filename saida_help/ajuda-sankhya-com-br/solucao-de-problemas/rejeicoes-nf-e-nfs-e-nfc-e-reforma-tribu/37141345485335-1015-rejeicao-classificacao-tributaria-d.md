---
id: "37141345485335"
titulo: "1015 Rejeição: Classificação Tributária do Imposto Seletivo informada inexistente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141345485335-1015-Rejei%C3%A7%C3%A3o-Classifica%C3%A7%C3%A3o-Tribut%C3%A1ria-do-Imposto-Seletivo-informada-inexistente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:35Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Código de Situação Tributária", "Alíquotas de IBS", "Imposto Seletivo (IS)", "Classificação Tributária do Imposto Seletivo"]
---

# 1015 Rejeição: Classificação Tributária do Imposto Seletivo informada inexistente [nItem: 999]

**MENSAGEM**

1015 Rejeição: Classificação Tributária do Imposto Seletivo informada inexistente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e) contendo produtos sujeitos ao Imposto Seletivo (IS), o documento foi rejeitado porque o código de **Classificação Tributária do Imposto Seletivo** informado não existe na tabela de classificações válidas da Sefaz.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e localize o produto que está gerando a rejeição.

**(2)** Na aba **''Impostos''**, verifique se o **Código de Situação Tributária** informado é válido conforme a tabela da Sefaz.

**(3)** Caso o código esteja incorreto, selecione um código válido da lista disponível no sistema.

**(4)** Alternativamente, acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se a configuração do Imposto Seletivo está correta para o produto em questão.

**(5)** Na aba **"Imposto Seletivo"**, verifique se o campo **"Classificação Tributária IS"** está preenchido com um código válido.

**(6)** Após realizar as correções, salve as alterações e tente emitir a nota fiscal novamente. 

**CAUSA**

Esta rejeição ocorre quando o sistema envia para a Sefaz um código de **Classificação Tributária do Imposto Seletivo** (campo cClassTribIS) que não consta na tabela oficial de classificações tributárias do Imposto Seletivo. O Imposto Seletivo, implementado pela Lei Complementar 214/2025 como parte da Reforma Tributária, possui uma tabela específica de classificações tributárias que deve ser respeitada na emissão de documentos fiscais.

A validação ocorre quando o sistema verifica se o código informado no campo cClassTribIS existe na tabela de Classificação Tributária do Imposto Seletivo. Se o código não existir ou estiver incorreto, a nota fiscal será rejeitada com o código de erro 1015.
