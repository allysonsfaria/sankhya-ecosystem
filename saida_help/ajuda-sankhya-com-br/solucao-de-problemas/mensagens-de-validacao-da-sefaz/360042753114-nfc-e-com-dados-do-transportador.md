---
id: "360042753114"
titulo: "NFC-e com dados do Transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753114-NFC-e-com-dados-do-Transportador"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:23Z"
rotulos: ["ERRONF", "#criadoRoger", "#revisadohugo", "Configuração", "SEFAZ", "TOP", "754", "Rejeição 754: Dados do Transportador na NFC-e", "Erro"]
---

# NFC-e com dados do Transportador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16452368790551) MENSAGEM:**

[754-Rejeição]: NFC-e com dados do Transportador.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16452368795543) SOLUÇÃO:**

Para correção siga os passos abaixo:

 Identificada se a operação é Presencial ou não, vejamos as configurações da TOP.

![Imagem 3: Acesse: " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP ):](https://ajuda.sankhya.com.br/hc/article_attachments/16452384442775) Acesse: "[**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP):

Aba: "**NF-e/NFC-e",**

Opção: "**Indicador de Presença para NF-e/NFC-e"**: **1-Operação Presencial** ou **4-NFC-e com entrega em domicílio**

- No caso de uma "NFC-e (**Modelo = 65**)", são válidos os indicadores de presença "**1**" ou "**4**";

- Caso seja Operação Presencial: Não informe Transportadora na NFC-e

- Caso seja Operação com Entrega em domicílio: informe dados da Transportadora na NFC-e.

![Imagem 4: Diante dessas informações, efetue o ajuste na respectiva nota ou na TOP, caso haja alteração na TOP ou criação de outra…](https://ajuda.sankhya.com.br/hc/article_attachments/16452368800791) Diante dessas informações, efetue o ajuste na respectiva nota ou na TOP, caso haja alteração na TOP ou criação de outra TOP para representar outro 'Indicador de Presença', inutilize a NFC-e e faça novamente o seu lançamento.

**![Imagem 5: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16452368803351) CAUSA**:

Quando for emitida uma NFC-e com dados do Transportador e o Indicador de presença do comprador  for diferente de "4 - NFC-e em operação com entrega a domicílio", será retornado a rejeição.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16452368806423) OBSERVAÇÃO:**

[Manual de Orientação do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=9hd38oni4Nc=)
