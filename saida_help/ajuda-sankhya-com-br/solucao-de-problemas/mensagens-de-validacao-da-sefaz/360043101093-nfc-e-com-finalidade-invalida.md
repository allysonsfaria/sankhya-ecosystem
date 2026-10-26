---
id: "360043101093"
titulo: "NFC-e com finalidade inválida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101093-NFC-e-com-finalidade-inv%C3%A1lida"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:45Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "TOP", "NFC-e", "715", "Rejeição 715: Finalidade Inválida na NFC-e", "Erro"]
---

# NFC-e com finalidade inválida

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16443947598359) MENSAGEM:**

[715-Rejeição]: NFC-e com finalidade inválida.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16443931185943) SOLUÇÃO:**

Para correção siga os passos abaixo:

**(1)** Acesse o Cadastro de ["**Tipos de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)**"**, campo: "**Tipo de Emissão"** = **Normal**

![Imagem 3: (1) Acesse o Cadastro de " Tipos de Operação - TOP " , campo: " Tipo de Emissão" = Normal](https://ajuda.sankhya.com.br/hc/article_attachments/14359282964247)

Operações acobertadas por NFC-e sempre devem ter finalidade de emissão normal. Para correção se faz necessário modificar o campo para 1 na TOP utilizada pela nota. Caso a finalidade de emissão da NF-e seja diferente de Normal, opte pela emissão de uma NF-e (modelo 55).

Feita a correção, reenvie a NFC-e.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16443931187607) CAUSA:**

Caso seja emitida uma NFC-e (modelo 65), onde o tipo de emissão é diferente de Normal, será apresentada a Rejeição.
