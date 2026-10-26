---
id: "42732788421271"
titulo: "Processo Adequação da NF-e e NFC-e à NT 2025.001 v.1.00"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42732788421271-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-e-NFC-e-%C3%A0-NT-2025-001-v-1-00"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e e NFC-e à NT 2025.001 v.1.00

**Módulo:** Fiscal e Contábil › Documentos Eletrônicos
**Caminho de acesso:** Menu Principal › Preferências › Empresa › aba NF-e/NFC-e

---

**Você encontra neste artigo:**

| ↳ [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732788421271-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-e-NFC-e-%C3%A0-NT-2025-001-v-1-00#h_01M00YY9E02J6FEX28ZSNEZVEX)     ↳ [NF-e — grupo de cobrança em parcela única](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732788421271-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-e-NFC-e-%C3%A0-NT-2025-001-v-1-00#h_01M00YY9E2ZBVKE27BG77NDC9Z) | ↳ [NFC-e — versão do QR Code](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732788421271-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-e-NFC-e-%C3%A0-NT-2025-001-v-1-00#h_01M00YY9E3Q3VTWBDVBKDX44CJ) |
| --- | --- |

## O que é e para que serve

A **Nota Técnica 2025.001 v.1.00** traz dois ajustes independentes: um na geração do grupo de cobrança da NF-e para notas com parcela única, e outro na versão do QR Code exigida para a NFC-e. Este artigo não cobre as adequações de IBS/CBS/IS da Reforma Tributária — essas fazem parte da NT 2025.002, com artigo próprio.

## NF-e — grupo de cobrança em parcela única

Com a vigência da NT 2025.001 v.1.00, ao emitir uma nota fiscal com apenas uma parcela cujo vencimento seja igual à data de emissão do documento, o grupo de cobrança não é mais incluído no XML da NF-e. Essa adequação atende à nova regra da NT e evita a rejeição "853 – Dados de cobrança não devem ser informados para pagamento à vista".

## NFC-e — versão do QR Code

Você pode escolher, por UF, qual versão do QR Code usar: 2.0 ou 3.0, por meio do campo **Versão QR Code** (aba NF-e/NFC-e, sub-aba NFC-e). Escolhendo a versão 2.0, o sistema continua funcionando como antes; escolhendo a versão 3.0, o sistema monta o QR Code conforme a regra atual da SEFAZ, tanto para emissão normal quanto para contingência. O QR Code aparece normalmente na nota fiscal e, quando escaneado, abre um link direto com os dados da nota.

| **⚠️ Atenção**  A partir da NT 2025.001, a NFC-e deve usar a versão 3 do QR Code para garantir a geração atualizada. Configure também a UF da empresa no parâmetro UFSQRCODEXML — UFs com QRCODE no XML da NFC-e. |
| --- |
