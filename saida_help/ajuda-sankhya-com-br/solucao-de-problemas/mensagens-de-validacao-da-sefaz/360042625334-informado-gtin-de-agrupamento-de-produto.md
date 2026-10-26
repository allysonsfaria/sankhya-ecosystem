---
id: "360042625334"
titulo: "Informado GTIN de agrupamento de produtos homogêneos (GTIN-14) no GTIN da unidade tributável [nItem: 999](NT2017/001)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042625334-Informado-GTIN-de-agrupamento-de-produtos-homog%C3%AAneos-GTIN-14-no-GTIN-da-unidade-tribut%C3%A1vel-nItem-999-NT2017-001"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:32Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "887", "Rejeição [887] - GTIN-14 no GTIN da unidade tributável", "Ajuste campos EAN/GTIN conforme unidade tributária", "GTIN-14 inválido para unidade tributável na NF-e", "GTIN"]
---

# Informado GTIN de agrupamento de produtos homogêneos (GTIN-14) no GTIN da unidade tributável [nItem: 999](NT2017/001)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16487743899159) MENSAGEM:**

[887 - Rejeição]: Informado GTIN de agrupamento de produtos homogêneos (GTIN-14) no GTIN da unidade tributável [nItem: 999](NT2017/001).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16487743902231) SOLUÇÃO:**

Considere o comportamento da aplicação, conforme abaixo:

![Imagem 3: Se a operação for realizada com a 'Unidade Padrão' e NÃO possuirmos uma 'Unidade Alternativa' marcada como 'Unidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/16487699203351) Se a operação for realizada com a 'Unidade Padrão' e **NÃO** possuirmos uma 'Unidade Alternativa' marcada como 'Unidade de Tributação', no XML as tags cEAN e cEANTrib serão preenchidas conforme aba Impostos, campo 'EAN/GTIN Produto p/ NF-e'.

As tag's **<cEAN>** e **<cEANTrib>**, serão preenchidas conforme o campo abaixo:

Tela: **"Produtos"**

Aba: **"Impostos"**
Campo **"EAN/GTIN" Produto p/ NF-e":** de acordo com a Definição das opções

![Imagem 4: A operação é feita com a 'Unidade de Tributação', porém EXISTE uma 'Unidade Alternativa' cadastrada e na mesma marcada…](https://ajuda.sankhya.com.br/hc/article_attachments/16487699205527) A operação é feita com a 'Unidade de Tributação', porém **EXISTE** uma 'Unidade Alternativa' cadastrada e na mesma marcada como 'Unidade de Tributação', dessa forma a tag cEAN será preenchida conforme a configuração do campo 'EAN/GTIN Produto p/ NF-e'. Já a tag cEANTrib conforme campo 'EAN/GTIN Unid.Tributação' da aba 'Unidade Alternativa'.

O campo **"Unidade Tributação"** fica na aba: **"Unidade Alternativa"**, opção "**Unid. Tributação"**

A tag **<cEAN>**, será preenchida conforme o campo abaixo:
Aba: **"Impostos"**
Campo **"EAN/GTIN Produto p/ NF-e:"** de acordo com a Definição das opções

A tag <**cEANTrib**>, será preenchida conforme o campo abaixo
Aba: **"Unidade Alternativa"**
Campo **"EAN/GTIN Unid.Tributação":**  de acordo com a Definição das opções

Conforme o comportamento acima, efetue os ajustes necessários, segundo o processo da empresa,. Considere sempre consultar a área Fiscal da Empresa, caso haja dúvidas. Após os ajustes lance novamente os produtos ou fature a Nota e gere Lote.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16487743910423) CAUSA:**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65), e o Código de Barras da Unidade Tributável (tag: cEANTrib) informado seja de um agrupamento de produtos homogêneos (GTIN-14), haverá a rejeição.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16487743914135) OBSERVAÇÃO:**

([NT2017/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=4DaFPH8v5ac=)) - Nota Técnica.
