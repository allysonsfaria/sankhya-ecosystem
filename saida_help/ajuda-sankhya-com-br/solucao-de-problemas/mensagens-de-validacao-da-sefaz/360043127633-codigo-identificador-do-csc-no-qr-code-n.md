---
id: "360043127633"
titulo: "Código Identificador do CSC no QR-Code não cadastrado na SEFAZ(NT2016.002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043127633-C%C3%B3digo-Identificador-do-CSC-no-QR-Code-n%C3%A3o-cadastrado-na-SEFAZ-NT2016-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:14Z"
rotulos: ["ERRONF", "Configuração", "XML", "SEFAZ", "462", "CSC não cadastrado", "Configure o Token NFC-e", "Gere NFC-e novamente", "Erro"]
---

# Código Identificador do CSC no QR-Code não cadastrado na SEFAZ(NT2016.002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16483332089111) MENSAGEM:**

[462 - Rejeição]: Código Identificador do CSC no QR-Code não cadastrado na SEFAZ.(NT2016.002)

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16483309691415) **SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16483309694487) Acesse: Comercial » Preferências » Empresa

Aba: **"NF-e/NFC-e"**

Campos:

- **"Sequencial do Token NFC-e":** Informe o código de 6 digital, extraído da Sefaz Estadual
- **"Token NFC-e":** Informe o código alfanumérico, extraído da Sefaz Estadual

![Imagem 4: "Token NFC-e": Informe o código alfanumérico, extraído da Sefaz Estadual](https://ajuda.sankhya.com.br/hc/article_attachments/14550251717015)

![Imagem 5: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16483332109079) Acesse: Configurações » Avançado » Preferências

Parâmetros:

- **"GERARQRCODEXML":** Ligado
- **"UFSQRCODEXML-UFs com QRCODE no XML da NFC-e?":** Informe a UF's, separado por vírgula se houve mais de 1(um).

![Imagem 6: Após o ajustes, gere novamente o cupom Eletrônico.](https://ajuda.sankhya.com.br/hc/article_attachments/16483332115223) Após o ajustes, gere novamente o cupom Eletrônico.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16483309706775) CAUSA:**

Quando for emitida uma NFC-e e o parâmetro CSC (Token) do emitente, no QR-Code não estiver cadastrado na Sefaz, será retornado a rejeição.

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16483309709207) OBSERVAÇÃO:**

(**NT2016.002**) - Nota Técnica

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Y6Lj7G0uHwc=>
