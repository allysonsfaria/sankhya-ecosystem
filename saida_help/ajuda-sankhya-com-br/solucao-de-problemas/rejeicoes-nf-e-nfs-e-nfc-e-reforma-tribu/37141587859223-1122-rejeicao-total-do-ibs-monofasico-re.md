---
id: "37141587859223"
titulo: "1122 Rejeição: Total do IBS monofásico retido anteriormente difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141587859223-1122-Rejei%C3%A7%C3%A3o-Total-do-IBS-monof%C3%A1sico-retido-anteriormente-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:59Z"
rotulos: ["Configuração", "NF-e", "Impostos", "Erro", "Reforma Tributária", "Alíquotas de IBS", "Total do IBS monofásico", "IBS monofásico retido", "IBS monofásico retido anteriormente difere da soma dos itens", "produtos sujeitos à tributação monofásica do IBS"]
---

# 1122 Rejeição: Total do IBS monofásico retido anteriormente difere da soma dos itens

**MENSAGEM**

1122 Rejeição: Total do IBS monofásico retido anteriormente difere da soma dos itens

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) contendo produtos sujeitos à tributação monofásica do IBS, o sistema identificou uma inconsistência entre o valor total do IBS monofásico retido anteriormente informado no rodapé do documento e o somatório dos valores de IBS monofásico retido anteriormente de cada item.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os valores de IBS monofásico retido anteriormente (**vIBSMonoRet**) informados em cada item do documento fiscal.

**(2)** Na grade **"Itens"**, verifique para cada produto se os valores de **IBS monofásico retido anteriormente** estão corretos, considerando:

- A quantidade tributável (**qTrib**) do item;
- A alíquota ad rem do IBS retido anteriormente (**adRemIBSRet**);
- A quantidade tributada que já foi retida anteriormente na cadeia (**qBCMonoRet**).

**(3)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e certifique de que CST do IBS está configurado para o regime monofásico.

**(4)** Verifique se há **arredondamentos** ou **truncamentos** nos cálculos que possam estar causando a diferença entre o total e a soma dos itens.

- O valor total no rodapé deve corresponder exatamente à soma dos valores dos itens.

**(5)** Caso esteja inserindo os valores manualmente, recalcule o documento utilizando a funcionalidade de **"Recálculo de Impostos"** para garantir que o sistema faça a totalização correta dos valores.

**(6)** Após as correções, verifique na aba **"Monofásica"** se o campo **"VIBSMONORET"** (Valor IBS monofásico retido) corresponde exatamente à soma dos valores de **"vIBSMonoRet"** de todos os itens do documento.

**CAUSA**

Esta rejeição ocorre quando o valor total do IBS monofásico retido anteriormente (**VIBSMONORET**) informado no grupo de totais do documento fiscal é **diferente** do somatório dos valores de IBS monofásico retido anteriormente (**vIBSMonoRet**) de cada item que compõe o documento.

A inconsistência pode ser causada por:

- Erros de cálculo manual nos valores de IBS monofásico retido anteriormente
- Problemas na conversão entre unidade comercial e unidade tributável
- Configuração incorreta do CST do IBS para produtos sujeitos à tributação monofásica
- Arredondamentos ou truncamentos que geram diferenças entre o total e a soma dos itens
- Falha na totalização automática dos valores no sistema

De acordo com as regras da Reforma Tributária (Lei Complementar 214/2025), os valores de IBS monofásico retido anteriormente devem ser consistentes entre os itens e o total do documento fiscal, garantindo a correta escrituração e apuração dos tributos.
