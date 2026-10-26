---
id: "44012702191511"
titulo: "[TMS] - Importação de nota fiscal - O tamanho máximo permitido é de 256KB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012702191511--TMS-Importa%C3%A7%C3%A3o-de-nota-fiscal-O-tamanho-m%C3%A1ximo-permitido-%C3%A9-de-256KB"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13433294", "sync_hash_194e53bd9111"]
---

# [TMS] - Importação de nota fiscal - O tamanho máximo permitido é de 256KB

**Menu:** Operacional > Importação > Nota Fiscal > Importação

**Objetivo:** Entender como corrigir a mensagem apresentada pelo sistema na importação de XML de nota fiscal.

**Considerações:**

- Possuir um arquivo XML de nota fiscal onde o tamanho seja superior a 256KB;

Durante a importação de XML de nota fiscal através do menu Operacional > Importação > Nota Fiscal > Importação, o sistema faz uma série de validações, dentre elas o tamanho do arquivo. Caso o arquivo seja superior a 256KB, então o sistema irá apresentar a seguinte mensagem: O tamanho máximo permitido é de 256KB.

![Imagem 1: Durante a importação de XML de nota fiscal através do menu Operacional > Importação > Nota Fiscal > Importação, o…](https://ajuda.sankhya.com.br/hc/article_attachments/44012747793303)

O sistema possui essa trava caso o arquivo possua tamanho superior a 256KB. Para visualizar o tamanho do arquivo, pode-se clicar com o botão direito do mouse sobre o arquivo e escolher a opção "Propriedades". No exemplo da imagem acima o tamanho do arquivo é superior a 259KB.

![Imagem 2: O sistema possui essa trava caso o arquivo possua tamanho superior a 256KB. Para visualizar o tamanho do arquivo,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012743030295)

Portanto, para que possa importar com sucesso a nota fiscal no sistema, deve-se enviá-la via e-mail, no caso, para o e-mail que foi definido no TMS para importação de anexos (parâmetro: destinatarioEmailImportacaoEmpresa).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
