---
id: "360042574994"
titulo: "Data de Emissão muito atrasada (NT2012/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042574994-Data-de-Emiss%C3%A3o-muito-atrasada-NT2012-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:24Z"
rotulos: ["ERRONF", "ERROMDFE", "ERROCTE", "Fiscal", "NF-e", "SEFAZ", "228", "NF-e com data muito atrasada", "Atraso na data de emissão", "Consultar legislação e reemitir", "Erro", "Documentos Eletrônicos", "NT2012/003"]
---

# Data de Emissão muito atrasada (NT2012/003)

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16474769689495) MENSAGEM**:

[228 - Rejeição]: Data de Emissão muito atrasada (NT2012/003).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474797425687) SOLUÇÃO:**

Considere o Comportamento da Aplicação, conforme abaixo:

![Imagem 3: Consulte a Legislação vigente da Sefaz do Estado para saber qual o atraso máximo permitido.](https://ajuda.sankhya.com.br/hc/article_attachments/16474797426199) Consulte a Legislação vigente da Sefaz do Estado para saber qual o atraso máximo permitido.

![Imagem 4: Caso o prazo tenha sido extrapolado, aconselha-se validar se essa NF-e consta como inexistente na SEFAZ…](https://ajuda.sankhya.com.br/hc/article_attachments/16474769699863) Caso o prazo tenha sido extrapolado, aconselha-se validar se essa NF-e consta como inexistente na SEFAZ Nacional/Estadual. Em caso positivo, proceda com a inutilização de sua numeração, sua exclusão.

![Imagem 5: Emita uma nova NF-e com datas atualizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/16474769703703) Emita uma nova NF-e com datas atualizadas.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474797431959) CAUSA:**

Quando se emite uma NF-e com data de emissão com atraso superior a 30 dias (ou limite de dias, a critério da Sefaz), contando a partir da data atual, será retornada a rejeição.

**![Imagem 7: Exceções a Regra:](https://ajuda.sankhya.com.br/hc/article_attachments/16474797434007) Exceções a Regra:**

- A critério da UF, a regra de validação poderá ser aplicada a todos os tipos de emissão.
- A critério da UF, pode ser aceita a NF-e com Data de Emissão muito atrasada, desde que tenha sido emitida em contingência (**tpEmis = 2, 4, 5**).

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474769707415) OBSERVAÇÃO:**

([NT2012/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=kE5icVGPKoo=)) - Nota Técnica.
