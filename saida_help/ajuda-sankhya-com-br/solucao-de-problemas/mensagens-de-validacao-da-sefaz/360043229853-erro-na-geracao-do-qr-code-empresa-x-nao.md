---
id: "360043229853"
titulo: "Erro na geração do QR Code. Empresa 'X' não possui Token NFC-e configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043229853-Erro-na-gera%C3%A7%C3%A3o-do-QR-Code-Empresa-X-n%C3%A3o-possui-Token-NFC-e-configurado"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:13Z"
rotulos: ["ERRONF", "Configuração", "SEFAZ", "Token", "Preferências", "Erro sem Token NFC-e", "Configure Token em Preferências", "NFC-e sem CSC configurado", "Erro"]
---

# Erro na geração do QR Code. Empresa 'X' não possui Token NFC-e configurado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16087374494359) **MENSAGEM:**

Erro na geração do QR Code. Empresa 'X' não possui Token NFC-e configurado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16087387466135) SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Realize as configurações para geração do Token em Comercial » Preferências » Empresa:](https://ajuda.sankhya.com.br/hc/article_attachments/16087387467927) Realize as configurações para geração do Token em Comercial » Preferências » **Empresa:**

Aba: **"NF-e/NFC-e"**:

- **"Sequencial do TOKEN NFC-e**"
- **"Token NFC-e"**

![Imagem 4: "Token NFC-e"](https://ajuda.sankhya.com.br/hc/article_attachments/14660651659671)

Os dados dos dois campos acima são fornecidos pela equipe Fiscal/Contábil da empresa. Junto a SEFAZ do Estado se faz o cadastro e são fornecidos o TOKEN(CSC) e o sequencial do TOKEN(ID).

![Imagem 5: Após o preenchimento dos campos com os valores corretos gere o lote novamente da NFC-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16087374502679) Após o preenchimento dos campos com os valores corretos gere o lote novamente da NFC-e.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16087374509207) CAUSA:**

Quando for emitida uma NFC-e com CSC (Token) não configurado no sistema, será apresentada a mensagem.
