---
id: "35699089524119"
titulo: "Situação da separação não permite gerar etiqueta de volume"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35699089524119-Situa%C3%A7%C3%A3o-da-separa%C3%A7%C3%A3o-n%C3%A3o-permite-gerar-etiqueta-de-volume"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:24:52Z"
rotulos: ["Conferência", "Impressão", "WMS", "Expedição de Mercadorias", "Estoque", "Etiquetas de Volumes", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Aguardando conferência de volumes", "Reimprimir etiquetas de volume", "Squad WMS"]
---

# Situação da separação não permite gerar etiqueta de volume

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/35699089513879) **MENSAGEM:**

Situação da separação não permite gerar etiqueta de volume

**SITUAÇÃO:**

Ao tentar Reimprimir etiqueta na tela **"Expedição de Mercadoria"**, a mensagem é apresentada

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/35699077757847)SOLUÇÃO:**

**(1)** Acesse a tela [**''Expedição de Mercadorias''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias) (WMS » Rotinas » Expedição de Mercadorias).

**(2)** Selecionar a opção **"Reimprimir etiquetas de volume".**

- Essa função está habilitada para **expedições** **cujo status** ainda está em **''Aguardando conferência de volumes''**.
- Quando a expedição se encontra **validada** e/ou **concluída**, **o sistema não permite a reimpressão** pela tela, pois o processo foi finalizado, impedindo alterações ou reemissões de etiquetas.
- Portanto, caso necessite fazer a **impressão de etiquetas** de uma expedição com **conferência validada** e/ou **concluída**, acesse a tela [**''Etiquetas de Volume''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume)**.**

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/35699077759127)CAUSA:**

A opção “Reimprimir etiquetas de volume” disponível na tela ''Expedição de Mercadorias'' só pode ser utilizada quando o status da expedição estiver em “Aguardando conferência de volumes”.

Caso a expedição já esteja com a conferência **validada** ou **concluída**, a reimpressão não será permitida por essa tela.

Nessas situações, a emissão das etiquetas deve ser realizada por meio da tela ''Etiquetas de Volume''.
