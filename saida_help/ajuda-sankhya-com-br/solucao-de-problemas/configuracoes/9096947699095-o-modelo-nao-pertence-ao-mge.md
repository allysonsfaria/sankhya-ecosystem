---
id: "9096947699095"
titulo: "O modelo não pertence ao MGE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9096947699095-O-modelo-n%C3%A3o-pertence-ao-MGE"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-24T12:42:12Z"
rotulos: ["Configuração", "Impressão", "CORE_E04328", "Erro de Modelo de Impressão no MGE", "Erro", "Sankhya Om", "Documentos Eletrônicos"]
---

# O modelo não pertence ao MGE

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19351462313879) MENSAGEM:**

[CORE\_E04328] O modelo não pertence ao MGE!!

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351442899095) SITUAÇÃO:**

Ao tentar imprimir um modelo baixado pela tela de modelos de impressão.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19351462336023) CAUSA:**

Usar modelos de arquivos TXT sem a função correta.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19351462339991) SOLUÇÃO:**

A função **"SIADE"** é utilizada para que nossos sistemas possam reconhecer o modelo que está sendo configurado como um modelo de impressão válido e deve estar presente em todos os modelos de impressão em formato TXT e HTML, lembrando que a linha Web não realiza a impressão de modelos em HTML.

Esta função deverá estar sempre na primeira linha, no primeiro bite do modelo, com a seguinte estrutura:

![Imagem 5: Esta função deverá estar sempre na primeira linha, no primeiro bite do modelo, com a seguinte estrutura:](https://ajuda.sankhya.com.br/hc/article_attachments/9096803087767)

Caso esta função não seja encontrada no local correto, o sistema emitirá a mensagem:

**"Modelo não pertence ao MGE".**

Importante: Caso queira, poderá verificar todas as informações sobre o formatador de arquivos TXT no link abaixo:

[Formatando arquivos TXT - Sankhya-Om – Sankhya Gestão de Negócios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603134-Formatando-arquivos-TXT-Sankhya-W?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg1NDEwOTM1OTMsInRpY2tldF9pZCI6NTExOTYsImNoYW5uZWxfaWQiOjYzLCJ0eXBlIjoiU0VBUkNIIiwiZXhwIjoxNjEwMjA1NzIyfQ.H5r6CTpWWWTM2g0WZdC19xvDil05IRrP0-deR-f6u4o)
