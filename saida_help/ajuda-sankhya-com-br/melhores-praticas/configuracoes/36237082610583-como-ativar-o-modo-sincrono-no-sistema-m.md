---
id: "36237082610583"
titulo: "Como ativar o modo Síncrono no sistema Mitra/Jiva G1"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36237082610583-Como-ativar-o-modo-S%C3%ADncrono-no-sistema-Mitra-Jiva-G1"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:23:20Z"
rotulos: ["Configuração", "Mitra", "NF-e", "XML", "SEFAZ", "Preferências", "Como", "Jiva G1", "Sistema Mitra/JivaG1", "Ativar modo síncrono", "modo Síncrono", "no sistema", "G1", "Síncrono", "ativar", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Como ativar o modo Síncrono no sistema Mitra/Jiva G1

O **"modo síncrono"** para envio de XML no SankhyaW permite que a emissão de documentos fiscais eletrônicos ocorra de forma mais ágil, aguardando o retorno imediato da SEFAZ. Esta funcionalidade está disponível a partir da versão 4.66 do banco de dados.

**(1)** Acesse a opção**"Avançado"** (Avançado >> Preferências >> Empresa);

**(2)** Localize a empresa responsável pela emissão da NF-e e/ou NFC-e;

**(3)** Marque a opção **"Usar modo Síncrono para envio do XML"** ;

**(4)** Clique em **"Salvar"**;

**(5)** Saia do sistema e acesse-o novamente para que a nova configuração seja aplicada corretamente.

![Imagem 1: (5) Saia do sistema e acesse-o novamente para que a nova configuração seja aplicada corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/36316973162775)

### Outros documentos fiscais com modo síncrono

Além da **NF-e**, o modo síncrono também está disponível para outros documentos fiscais eletrônicos via parâmetro:

- **NFC-e, CT-e e MDF-e.**

**Importante:**

A partir das versões mais recentes dos webservices da SEFAZ (NF-e e NFC-e), o envio das notas fiscais passou a ser obrigatoriamente realizado no modo **"Síncrono"**. Isso significa que, ao transmitir a NF-e, o sistema aguarda a resposta imediata da SEFAZ, eliminando a necessidade de realizar consultas posteriores ao lote.
