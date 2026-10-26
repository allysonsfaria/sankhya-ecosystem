---
id: "360042587194"
titulo: "NFC-e em operação não destinada a consumidor final"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042587194-NFC-e-em-opera%C3%A7%C3%A3o-n%C3%A3o-destinada-a-consumidor-final"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:01Z"
rotulos: ["ERRONF", "Configuração", "Fiscal", "Parceiro", "SEFAZ", "716", "Rejeição 716: NFC-e Não Consumidor Final", "Erro"]
---

# NFC-e em operação não destinada a consumidor final

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443527673623) MENSAGEM:**

[716-Rejeição]: NFC-e em operação não destinada a consumidor final.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443527675671) **SOLUÇÃO:**

Para correção, siga os passos abaixo:

**(1)** Configurações » Cadastros » Parceiros

- Aba: Fiscal
- Campo: Classificação ICMS = 'Consumidor Final Não Contribuinte'

Após o ajuste, redigite a Empresa ou Parceiro da NFC-e e gere o lote novamente.

Caso a operação de Venda não seja para um Consumidor Final, opte pela Emissão de uma NF-e(55)

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443527678999) CAUSA:**

Quando for emitida uma NFC-e e a Operação não ocorrer com Consumidor Normal, ou seja, o campo <indFinal> = 0 - "Consumidor Normal", será retornado a rejeição "716 - NFC-e em operação não destinada a consumidor final".

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443498315287) OBSERVAÇÃO:**

1- Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=>
