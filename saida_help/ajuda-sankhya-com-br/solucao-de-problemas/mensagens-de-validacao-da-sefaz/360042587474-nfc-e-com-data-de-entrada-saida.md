---
id: "360042587474"
titulo: "NFC-e com data de entrada/saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042587474-NFC-e-com-data-de-entrada-sa%C3%ADda"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:59Z"
rotulos: ["ERRONF", "Configuração", "Portal de Vendas", "SEFAZ", "TOP", "705", "Rejeição 705: Data de Entrada/Saída na NFC-e", "Erro"]
---

# NFC-e com data de entrada/saída

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443669393559) **MENSAGEM:**

[705-Rejeição]: NFC-e com data de entrada/saída.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443639796247) **SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Acesse o " Portal de Vendas" , pesquise pela NFC-e e retire o conteúdo do campo " Data de Entrada/Saída " no cabeçalho…](https://ajuda.sankhya.com.br/hc/article_attachments/16443669394839) Acesse o "[**Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), pesquise pela NFC-e e retire o conteúdo do campo "**Data de Entrada/Saída**" no cabeçalho da NFC-e;

![Imagem 4: Após o ajuste, gere o lote da NFC-e novamente;](https://ajuda.sankhya.com.br/hc/article_attachments/16443639798167) Após o ajuste, gere o lote da NFC-e novamente;

![Imagem 5: Verifique a configuração do "Tipo de Operação - TOP ", aba " NF-e/NFC-e ", campo " Imprimir NF-e sem Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16443639798935) Verifique a configuração do **["Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)",** aba "**NF-e/NFC-e**", campo "**Imprimir NF-e sem Data de Entrada/Saída**:".

![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443639799447) **CAUSA:**

Quando for emitida uma NFC-e e for informado a Data de Entrada/Saída (dhSaiEnt) será retornado a rejeição.

![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17855629185047) **OBSERVAÇÃO:**

Nota Técnica: <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=>
