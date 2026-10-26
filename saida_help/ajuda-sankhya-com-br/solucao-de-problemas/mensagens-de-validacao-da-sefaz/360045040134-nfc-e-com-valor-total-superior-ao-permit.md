---
id: "360045040134"
titulo: "NFC-e com valor total superior ao permitido para destinatário não identificado (Código) [Limite]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045040134-NFC-e-com-valor-total-superior-ao-permitido-para-destinat%C3%A1rio-n%C3%A3o-identificado-C%C3%B3digo-Limite"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:33:15Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "SEFAZ", "750", "Rejeição 750: NFC-e Valor Total Excedente", "Erro"]
---

# NFC-e com valor total superior ao permitido para destinatário não identificado (Código) [Limite]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16455119309335) MENSAGEM:**

[750 - Rejeição]: NFC-e com valor total superior ao permitido para destinatário não identificado (Código) [Limite]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455119314455) SOLUÇÃO:**

![Imagem 3: Verifique com a SEFAZ do seu Estado qual o valor permitido para venda não identificada. Caso o valor tenha…](https://ajuda.sankhya.com.br/hc/article_attachments/16455119325207) Verifique com a SEFAZ do seu Estado qual o valor permitido para venda não identificada. Caso o valor tenha ultrapassado,**o destinatário deverá ser devidamente cadastrado** (tag:dest/CNPJ, dest/CPF ou dest/idEstrang) e informado no lançamento da nota.

- Acesse a tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"**(Caminho de acesso: Configurações » Cadastros » Parceiros)
- Cadastre parceiro identificado através do "**CNPJ"**, "**CPF"** ou "**idEstrangeiro"**.

![Imagem 4: Após informar o parceiro destinatário corretamente, gere um novo lote da nota.](https://ajuda.sankhya.com.br/hc/article_attachments/16455119329431) Após informar o parceiro destinatário corretamente, gere um novo lote da nota.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16455119344151) CAUSA:**

Quando for emitida uma NFC-e com Valor Total (vNF) superior a R$ 10.000,00 (dez mil reais) e o Destinatário da NFC-e não for identificado através do CNPJ, CPF ou idEstrangeiro, será retornado a rejeição.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455119348247) OBSERVAÇÃO:**

Valor definido a critério da UF: [Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)
