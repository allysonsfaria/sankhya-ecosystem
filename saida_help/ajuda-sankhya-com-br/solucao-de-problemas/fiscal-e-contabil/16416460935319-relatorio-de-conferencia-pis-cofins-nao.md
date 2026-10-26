---
id: "16416460935319"
titulo: "Relatório de Conferência PIS/COFINS não está considerando o desconto no valor total dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16416460935319-Relat%C3%B3rio-de-Confer%C3%AAncia-PIS-COFINS-n%C3%A3o-est%C3%A1-considerando-o-desconto-no-valor-total-dos-itens"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:55:18Z"
rotulos: ["Configuração", "Relatórios", "NF-e", "Impostos", "Preferências", "Solução: Verifique o campo \"VLRLIQITEMNFE\" no cabeçalho da nota.", "Problema: Relatório PIS/COFINS não inclui desconto nos itens.", "Ajuste: Marque \"Considera valor líquido do item\" em preferências."]
---

# Relatório de Conferência PIS/COFINS não está considerando o desconto no valor total dos itens

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16866608470295) SITUAÇÃO:**

Ao emitir o relatório de conferência PIS/COFINS, o sistema não está considerando o valor do desconto aplicado nos itens das notas para preenchimento do campo "Valor Total dos Itens" do documento

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16866598593303) SOLUÇÃO:**

Na emissão do relatório de conferência do PIS/COFINS, o sistema considera o valor do campo **VLRLIQITEMNFE** no cabeçalho da nota (TGFCAB) para preenchimento do valor total dos itens.
 Caso o campo em questão esteja com o valor 'N', o sistema vai considerar o total bruto do item para geração do relatório. Ou seja, ele não vai levar em conta o desconto do produto.
No cabeçalho da nota, esse campo se refere à marcação da opção "Considera valor líquido do item para NFe (geração do XML e imp. Danfe)", presente nas preferências da empresa (Comercial > Preferências > Empresa). Como essa opção se encontra desmarcado, o sistema realmente vai apresentar o valor bruto do item.
