---
id: "360042719654"
titulo: "NFC-e para operação interestadual ou com o exterior"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042719654-NFC-e-para-opera%C3%A7%C3%A3o-interestadual-ou-com-o-exterior"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:58Z"
rotulos: ["ERRONF", "#criadoRoger", "#RevisadoBraga", "Configuração", "Fiscal", "SEFAZ", "TOP", "CFOP", "707", "Rejeição 707: NFC-e para Operação Interestadual ou Exterior"]
---

# NFC-e para operação interestadual ou com o exterior

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16452024195223) MENSAGEM:**

[707-Rejeição]: NFC-e para operação interestadual ou com o exterior.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16452024199575) SOLUÇÃO:**

Para correção siga os passos abaixo:

![Imagem 3: Avalie se para a emissão a ser realizada de fato é válida a utilização de uma Nota Fiscal de Consumidor (NFC-e). Visto…](https://ajuda.sankhya.com.br/hc/article_attachments/16452024201623) Avalie se para a emissão a ser realizada de fato é válida a utilização de uma Nota Fiscal de Consumidor (NFC-e). Visto que:

Em Operações acobertadas por NFC-e é **permitido apenas que sejam Estaduais** (idDest = 1). Para Operações Interestaduais ou com o Exterior, opte pela emissão de uma NF-e (modelo 55). Para corrigir a NFC-e, deve-se informar a Operação como Estadual.

![Imagem 4: Caso não se trate de uma operação Estadual, sintonize com o contador e avalie a possibilidade de emissão de uma NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/16452024206103) Caso não se trate de uma operação Estadual, sintonize com o contador e avalie a possibilidade de emissão de uma NF-e (Modelo 55).

![Imagem 5: Se tratar-se de uma NFC-e, certifique-se que as configurações de CFOP foram realizadas corretamente:](https://ajuda.sankhya.com.br/hc/article_attachments/16452008686871) Se tratar-se de uma NFC-e, certifique-se que as configurações de CFOP foram realizadas corretamente:

- Acesse: "[**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)
- Aba: "**Livro Fiscal"**
- Campo: **"CFOP's para Dentro do Estado": [CFOP'S iniciadas com 1 ou 5]**
- Certifique-se que a CFOP informado não é uma CFOP de transação Interestadual (iniciado em 6) ou Exterior (iniciado em 7). Dúvidas, alinhe com o Contador qual o correto CFOP.

![Imagem 6: Se necessário ajustes na TOP, inutilize a NFC-e rejeitada e proceda com uma nova emissão.](https://ajuda.sankhya.com.br/hc/article_attachments/16452008687511) Se necessário ajustes na TOP, inutilize a NFC-e rejeitada e proceda com uma nova emissão.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16452008688919) CAUSA:**

Quando for emitida uma NFC-e para uma Operação Interestadual ou Operação com o Exterior Será retornado a rejeição.
