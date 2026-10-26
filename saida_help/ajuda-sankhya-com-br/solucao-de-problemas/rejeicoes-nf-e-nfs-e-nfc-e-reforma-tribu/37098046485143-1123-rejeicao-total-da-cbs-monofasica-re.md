---
id: "37098046485143"
titulo: "1123 Rejeição: Total da CBS monofásica retida anteriormente difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098046485143-1123-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-retida-anteriormente-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:22Z"
rotulos: ["NF-e", "SEFAZ", "Impostos", "Erro", "Alíquotas de CBS", "Inconsistência no cálculo da CBS monofásica retid", "Valor total da CBS monofásica", "vCBSMonoRet", "CBS monofásica retida anteriormente difere da soma dos itens"]
---

# 1123 Rejeição: Total da CBS monofásica retida anteriormente difere da soma dos itens

**MENSAGEM**

1123 Rejeição: Total da CBS monofásica retida anteriormente difere da soma dos itens

**SITUAÇÃO**

A nota fiscal foi emitida com divergência entre o valor total da CBS monofásica retida anteriormente informado no rodapé do documento e os valores de CBS monofásica retida anteriormente registrados nos itens da nota.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e verifique os valores da CBS monofásica retida anteriormente em cada item da nota fiscal.

**(2)** Selecione a nota fiscal rejeitada e clique na aba **"Itens"** para visualizar todos os itens da nota.

**(3)** Para cada item que possui tributação monofásica, verifique o valor informado no campo **"vCBSMonoRet"** (valor da CBS monofásica retida anteriormente).

**(4)** Calcule manualmente a soma de todos os valores de **"vCBSMonoRet"** de cada item e compare com o valor total informado no rodapé da nota (campo **"vCBSMonoRet"** do grupo **"IBSCBSTot"**).

**(5)** Caso identifique divergências, corrija os valores da CBS monofásica retida anteriormente em cada item ou ajuste o valor total no rodapé da nota, garantindo que o somatório dos itens seja igual ao valor total informado.

**(6)** Acesse a tela **''Alíquota de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e verifique se a configuração do ''Código de Situação Tributária'' (CST) está correto para cada item.

**(7)** Certifique-se de que os itens que possuem tributação monofásica retida anteriormente estejam utilizando um CST que permita essa informação (verifique o indicador **"ind\_gMonoRet"** associado ao CST).

**(8)** Após realizar as correções necessárias, recalcule os impostos da nota fiscal e tente emitir novamente o documento. 

**CAUSA**

A rejeição 1123 ocorre devido a uma inconsistência no cálculo da CBS monofásica retida anteriormente. Conforme a regra de validação UB105-10 da SEFAZ, o valor total da CBS monofásica do item (vTotCBSMonoItem) deve ser resultante da fórmula: vTotCBSMonoItem = vCBSMono + vCBSMonoReten - vCBSMonoDif.

Esta inconsistência pode ocorrer por diversos motivos:

• Erro no cálculo automático dos valores da CBS monofásica retida anteriormente;

• Alteração manual incorreta dos valores em algum item da nota;

• Utilização de CST inadequado para a operação, que não permite a informação de tributação monofásica retida anteriormente (conforme regras UB94-10 e UB94-20);

• Falha na totalização dos valores no rodapé da nota fiscal.

A validação é exigida pela Lei Complementar 214/2025, que estabelece as regras para a tributação monofásica no âmbito da Reforma Tributária, garantindo a correta apuração e recolhimento da CBS.
