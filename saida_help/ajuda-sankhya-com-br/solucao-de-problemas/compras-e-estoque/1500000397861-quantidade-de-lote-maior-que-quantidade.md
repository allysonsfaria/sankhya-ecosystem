---
id: "1500000397861"
titulo: "Quantidade de lote maior que quantidade informada no item. Não é possível proporcionalizar os lotes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500000397861-Quantidade-de-lote-maior-que-quantidade-informada-no-item-N%C3%A3o-%C3%A9-poss%C3%ADvel-proporcionalizar-os-lotes"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:26:18Z"
rotulos: ["Produtos", "NF-e", "XML", "Importação", "Estoque", "CORE_E03156", "Quantidade de lote", "Solução de importação de XML", "Erro CORE_E03156", "Erro"]
---

# Quantidade de lote maior que quantidade informada no item. Não é possível proporcionalizar os lotes

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16274387974551) MENSAGEM**:

[CORE\_E03156] Quantidade de lote maior que quantidade informada no item. Não é possível proporcionalizar os lotes.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16274387983639) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

Esta mensagem ocorre quando se está tentando importar um XML e algum item possui mais de uma tag "**qLote**" no xml e a quantidade for maior que a quantidade na tag "**qCom**", o sistema não tem parâmetros suficientes para proporcionalizar o "**qLote**".

**Vejamos o exemplo prático:**

-<det nItem="1">

**<qCom>1200.0000</qCom>**

-<rastro>
**<qLote>89600.000</qLote>**
<dFab>2020-06-01</dFab>
<dVal>2025-05-31</dVal>

</rastro>
<nLote>02005054</nLote>
**<qLote>30400.000</qLote>**
<dFab>2020-08-01</dFab>
<dVal>2025-07-31</dVal>

Se somarem as quantidades das 2 tags <qLote> chega em 120.000 porém na tag <qCom> está menor 1200.00

[GIF animado: Imagem 3: -<det nItem="1"> <qCom>1200.0000</qCom> -<rastro> <qLote>89600.000</qLote> <dFab>2020-06-01</dFab>…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000440442)

Veja como abrir o XML em um Navegador(Chrome, Firefox ou Internet Explorer para analise

A solução mais adequada é verificar com o fornecedor se houve algum incidente na geração da nota e solicite que faça a devida correção, para geração de nova nota de compra, onde o XML esteja correto.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16274404440343) CAUSA:**

Ocorre quando foi informada um lote maior que a quantidade comercializada do item.
