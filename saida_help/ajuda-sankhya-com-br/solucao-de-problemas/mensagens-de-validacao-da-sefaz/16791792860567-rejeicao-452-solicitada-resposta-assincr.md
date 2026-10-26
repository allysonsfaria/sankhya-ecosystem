---
id: "16791792860567"
titulo: "Rejeição 452: Solicitada resposta assíncrona para lote com somente uma NFC-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16791792860567-Rejei%C3%A7%C3%A3o-452-Solicitada-resposta-ass%C3%ADncrona-para-lote-com-somente-uma-NFC-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:54:26Z"
rotulos: ["Configuração", "XML", "SEFAZ", "NFC-e", "Rejeição 452", "Rejeição 452: Resposta Assíncrona para Lote com Uma NFC-e", "Erro", "Documentos Eletrônicos"]
---

# Rejeição 452: Solicitada resposta assíncrona para lote com somente uma NFC-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16791792848535)  MENSAGEM:**

Rejeição 452: Solicitada resposta assíncrona para lote com somente uma NFC-e

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16791745594135) SOLUÇÃO:**

Para enviar o XML de forma "Síncrona"(em que é permitido o envio de apenas uma nota), siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(2)** Busque e selecione a empresa da nota que recebeu a rejeição 452.

**(3)** Vá até a aba **"Documentos eletrônicos"**, sub aba "**NF-e/NFC-e",** depois selecione a seção **"NFC-e"** e nela marque a opção **"Usar modo síncrono para envio do XML?".**

**(4)** Após configurar corretamente o sistema gere o lote novamente.

**CAUSA:**

Nas preferências comerciais da **Empresa** - Comercial » Preferências » Empresa encontramos o campo "Usar modo Síncrono para envio do xml" na aba **NF-e/NFC-e** (Seção NFC-e), caso o campo esteja desmarcado ao emitir uma NFC-e o sistema assume o modo "Assíncrono" para envio do xml. No entanto, **caso esteja enviando apenas uma nota ocorre a rejeição 452.**
