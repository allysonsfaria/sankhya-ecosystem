---
id: "360042587114"
titulo: "NFC-e em operação não presencial (NT2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042587114-NFC-e-em-opera%C3%A7%C3%A3o-n%C3%A3o-presencial-NT2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-18T20:54:16Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "NFC-e", "717", "Rejeição 717: NFC-e em Operação Não Presencial"]
---

# NFC-e em operação não presencial (NT2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16459847197591) MENSAGEM:**

[717-Rejeição]: NFC-e em operação não presencial (NT2013/005).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459868490647) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo.

![Imagem 3: Acesse: Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16459847207959) Acesse: Arquivo » Cadastros » Tipos de Operação - TOP

Aba: "**NF-e/NFC-e"**

Campo: "**Indicador de Presença para NF-e/NFC-e"** = 1 ou 4

- 1- Operação Presencial
- 4- NFC-e com entrega em domicílio

Caso a operação de Venda seja NÃO PRESENCIAL, opte pela Emissão de uma NF-e onde o indicador de Presença poderá ser 2, 3 ou 9.

![Imagem 4: Após o ajuste, gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16459868499735) Após o ajuste, gere o lote novamente.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16459868504855) CAUSA:**

Quando for emitida uma NFC-e e o Indicador de Presença do Comprador (indPres) for diferente de "1 - Operação presencial" ou diferente de "4 - NFC-e com entrega em domicílio".

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16459868507799) OBSERVAÇÃO:**

([NT2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.
