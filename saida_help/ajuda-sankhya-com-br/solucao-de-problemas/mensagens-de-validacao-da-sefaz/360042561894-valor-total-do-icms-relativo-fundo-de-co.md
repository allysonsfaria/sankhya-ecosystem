---
id: "360042561894"
titulo: "Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino difere do somatório do valor dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042561894-Valor-total-do-ICMS-relativo-Fundo-de-Combate-%C3%A0-Pobreza-FCP-da-UF-de-destino-difere-do-somat%C3%B3rio-do-valor-dos-itens"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:48Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "798", "Divergência no Valor do ICMS FCP", "FCP"]
---

# Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino difere do somatório do valor dos itens

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16460198943383) MENSAGEM:**

[798-Rejeição]: Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino difere do somatório do valor dos itens.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16460198949015) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16460198957463) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: Impostos

Campo "**Calcular DIFAL Partilhado"** **marque**

Cálculo de ICMS, IPI e ISS: Calcula e Digita-para **Venda** e Não calcula e digita para **Devolução de Venda**

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16460167506967) Acesse: Configurações » Cadastros » Produtos » Produtos

Aba: "**Impostos"** ou "**Impostos/Informações por empresa"**

Campo "**Calcular ICMS"**: marque

**Nota**: Se o produto for Kit ou Componente do kit, considere calcular o imposto ou para o KIT ou para os componentes.

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16460167510551) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Considere ter um regra de ICMS, devidamente registrada de acordo com o tipo de movimentação, que tenha o campo "**Tipo de Calculo Difal"** e "**Aliq. Interna Destino"**, devidamente configurados, para o cálculo do Difal.

Tais informações devem ser previamente consultadas com o Contador da empresa, para o correto cadastro da regra de ICMS.

![Imagem 6: Após os ajustes, inutilize a numeração, exclua a nota e fature ou gere a nota novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16460198966551) Após os ajustes, inutilize a numeração, exclua a nota e fature ou gere a nota novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16460198970007) CAUSA:**

Quando for emitida uma NF-e e nos totais do documento o Valor do ICMS relativo ao Fundo de Combate à Pobreza para a UF de Destino (ICMSTot / vFCPUFDest)  **FOR**apresentado valor que difere somatório do Valor do ICMS relativo ao Fundo de Combate à Pobreza para a UF de Destino (ICMSUFDest / vFCPUFDest) de cada item, será retornado a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16460167526167) OBSERVAÇÃO:**

([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zJGzcwysHPo=)) - Nota técnica.
