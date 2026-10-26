---
id: "37097980156951"
titulo: "1120 Rejeição: Total do IBS monofásico sujeito a retenção difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37097980156951-1120-Rejei%C3%A7%C3%A3o-Total-do-IBS-monof%C3%A1sico-sujeito-a-reten%C3%A7%C3%A3o-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-14T17:17:35Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de IBS", "Total do IBS monofásico", "IBS monofásico", "Soma dos itens", "IBS monofásico sujeito à retenção"]
---

# 1120 Rejeição: Total do IBS monofásico sujeito a retenção difere da soma dos itens

**MENSAGEM**

1120 Rejeição: Total do IBS monofásico sujeito a retenção difere da soma dos itens

**SITUAÇÃO**

O valor total do IBS monofásico sujeito à retenção informado no grupo de totais da NF-e ou NFC-e difere do somatório dos valores de IBS monofásico sujeito à retenção dos itens do documento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os valores de IBS monofásico sujeito á retenção em cada item da nota fiscal.

**(2)** Abra a nota fiscal rejeitada e verifique item por item os valores de **IBS monofásico sujeito à retenção** (campo vIBSMonoReten) para cada produto.

**(3)** Confira se o valor total do IBS monofásico sujeito à retenção (campo VIBSMONORETEN) no rodapé da nota corresponde exatamente à soma dos valores individuais de cada item.

**(4)** Caso haja divergência, corrija o valor total para que corresponda exatamente à soma dos valores dos itens. O sistema deve calcular automaticamente este valor, mas se estiver sendo informado manualmente, ajuste-o para refletir a soma correta.

**(5)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se as configurações para os produtos da nota fiscal estão corretas, especialmente para produtos sujeitos á tributação monofásica.

**(6)** Certifique-se de que o **Código de Situação Tributária (CST)** esteja configurado corretamente para os produtos sujeitos à tributação monofásica com retenção.

**(7)** Após realizar as correções necessárias, tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre devido à inconsistência entre o valor total do IBS monofásico sujeito à retenção declarado no grupo de totais da NF-e/NFC-e e o somatório dos valores individuais de cada item. De acordo com as regras de validação da Sefaz, o valor total do IBS monofásico sujeito à retenção (campo VIBSMONORETEN) deve ser exatamente igual à soma dos valores de IBS monofásico sujeito à retenção (campo vIBSMonoReten) de todos os itens da nota fiscal.

A validação é semelhante à que ocorre com outros campos de totalização, como a base de cálculo do ICMS. O sistema verifica se a equação "VIBSMONORETEN = ∑(vIBSMonoReten de cada item)" é verdadeira. Se houver qualquer diferença, mesmo que de centavos, a nota será rejeitada. Esta validação faz parte das regras implementadas com a Reforma Tributária (Lei Complementar 214/2025) para garantir a consistência dos valores declarados nos documentos fiscais eletrônicos relacionados ao IBS monofásico sujeito à retenção.
