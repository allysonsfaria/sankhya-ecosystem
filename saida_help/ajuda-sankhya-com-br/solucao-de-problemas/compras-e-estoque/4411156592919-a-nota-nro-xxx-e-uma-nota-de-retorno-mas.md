---
id: "4411156592919"
titulo: " A nota Nro. xxx é uma nota de retorno, mas não possui notas eletrônicas de remessa correspondentes na base, a importação não será realizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411156592919--A-nota-Nro-xxx-%C3%A9-uma-nota-de-retorno-mas-n%C3%A3o-possui-notas-eletr%C3%B4nicas-de-remessa-correspondentes-na-base-a-importa%C3%A7%C3%A3o-n%C3%A3o-ser%C3%A1-realizada"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:21:10Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "TOP", "#validadoRaiane", "Ajuste de Configuração para Nota de Retorno", "Incompatibilidade de Nota de Retorno", "Nota de Retorno sem Remessa", "Erro"]
---

#  A nota Nro. xxx é uma nota de retorno, mas não possui notas eletrônicas de remessa correspondentes na base, a importação não será realizada

#### Imagem 1: MENSAGEM: MENSAGEM:

A nota Nro. xxx é uma nota de retorno, mas não possui notas eletrônicas de remessa correspondentes na base, a importação não será realizada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136483508503) SOLUÇÃO:**

Para a resolução do incidente, siga os passos abaixo:

![Imagem 3: Acesse a tela Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16136497416983) Acesse a tela **Comercial » Arquivo » Cadastros » Tipos de Operação - TOP**

![Imagem 4: Desmarque a opção "Desconsidera Nfe de orig. referenciada" .](https://ajuda.sankhya.com.br/hc/article_attachments/16136483515543) Desmarque a opção **"Desconsidera Nfe de orig. referenciada"**.

![Imagem 5: Desmarque a opção "Desconsidera Nfe de orig. referenciada" .](https://ajuda.sankhya.com.br/hc/article_attachments/15696252438039)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16136483537303) OBSERVAÇÃO:**

A mensagem de erro ocorre no portal de importação XML (Comercial » Rotinas » Portal de importação de XL).

**![Imagem 7: Causa:](https://ajuda.sankhya.com.br/hc/article_attachments/16136483539735) Causa:**

O incidente é causado por  uma nova marcação na TOP. Geralmente essa mensagem ocorre em nota de transferência, remessa, retorno. Esse campo foi acrescentado para atender uma nova implementação.
