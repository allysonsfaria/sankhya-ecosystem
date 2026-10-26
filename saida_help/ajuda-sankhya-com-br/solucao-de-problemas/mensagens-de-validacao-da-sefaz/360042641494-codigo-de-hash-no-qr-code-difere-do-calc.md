---
id: "360042641494"
titulo: "Código de Hash no QR-Code difere do calculado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042641494-C%C3%B3digo-de-Hash-no-QR-Code-difere-do-calculado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:31Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "464", "Validar TOKEN no site SEFAZ", "Ajustar TOKEN em preferências", "QR-Code Hash divergente", "Erro", "TOKEN NFC-e"]
---

# Código de Hash no QR-Code difere do calculado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504754645143) MENSAGEM:**

[464 - Rejeição]: Código de Hash no QR-Code difere do calculado.(NT2016.002)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504754646551) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse o Site da SEFAZ Estadual e procure validar o certificado, acessando o ambiente de 'Nota Fiscal de Consumidor…](https://ajuda.sankhya.com.br/hc/article_attachments/16504718318999) Acesse o Site da SEFAZ Estadual e procure validar o certificado, acessando o ambiente de 'Nota Fiscal de Consumidor Eletrônica' e busque a informação do  'TOKEN'.

![Imagem 4: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16504718324759) Acesse: Comercial » Preferências » Empresa

- Aba: **"NF-e/NFC-e"**
- Campo: **"TOKEN NFC-e":** coloque neste campo o mesmo código, buscado anteriormente no Site da SEFAZ Estadual'

![Imagem 5: Após o ajuste, emita uma nota NFC-e para buscar as informações do Hash e gerar o QR-Code corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16504718327191) Após o ajuste, emita uma nota NFC-e para buscar as informações do Hash e gerar o QR-Code corretamente.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16504754656663)CAUSA:**

Quando for emitida uma NFC-e e o QR-Code calculado pelo sistema for diferente do calculado pela Sefaz, será retornado a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504754657943) OBSERVAÇÃO:**

([NT2016.002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=)) - Nota Técnica
