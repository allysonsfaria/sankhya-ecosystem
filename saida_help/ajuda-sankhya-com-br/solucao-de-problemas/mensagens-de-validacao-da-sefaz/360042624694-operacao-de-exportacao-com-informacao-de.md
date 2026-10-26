---
id: "360042624694"
titulo: "Operação de Exportação com informação de ICMS incompatível. (NT2010/010)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042624694-Opera%C3%A7%C3%A3o-de-Exporta%C3%A7%C3%A3o-com-informa%C3%A7%C3%A3o-de-ICMS-incompat%C3%ADvel-NT2010-010"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:40Z"
rotulos: ["ERRONF", "NF-e", "SEFAZ", "ICMS", "Impostos", "CFOP", "527", "ICMS Incompatível em Exportação", "Exportacao"]
---

# Operação de Exportação com informação de ICMS incompatível. (NT2010/010)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16509635223831) MENSAGEM:**

[527 - Rejeição]: Operação de Exportação com informação de ICMS incompatível. (NT2010/010)

**![Imagem 2: SOLUÇÃO: Para correção deste erro, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16509635228439) SOLUÇÃO:**
Para correção deste erro, siga os passos abaixo:

![Imagem 3: No item da nota, identifique o campo " Cód. Aliq. ICMS" , anote esse código e pesquisa o em Alíquotas de ICMS.](https://ajuda.sankhya.com.br/hc/article_attachments/16509641879447) No item da nota, identifique o campo "**Cód. Aliq. ICMS"**, anote esse código e pesquisa o em Alíquotas de ICMS.

![Imagem 4: Para isso, acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS Pesquise pela Regra de ICMS que…](https://ajuda.sankhya.com.br/hc/article_attachments/16509641882391) Para isso, acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS
Pesquise pela Regra de ICMS que incidiu na NFe e faça o ajuste nos campos:
Aba: **"Geral"**
Tributação = 041-Não Tributada
Aba: **"Simples Nacional"**
CSOSN = 300-Imune [Caso houver incidência de CSOSN]

![Imagem 5: Após os ajustes redigite Empresa/Parceiro da Nota e gere Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16509641886231) Após os ajustes redigite Empresa/Parceiro da Nota e gere Lote novamente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16509641888919) CAUSA:**

Quando for emitida uma NF-e que indica uma Operação de Exportação, ou seja, com o CFOP iniciado pelo dígito "7" (sete) e for informado CST de ICMS diferente de "41 - Não tributada" ou CSOSN diferente de "300 - Imune" será retornada a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16509635240471) OBSERVAÇÃO:**

([NT2010/010](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AtaVevRXCIQ=)) - Nota técnica
