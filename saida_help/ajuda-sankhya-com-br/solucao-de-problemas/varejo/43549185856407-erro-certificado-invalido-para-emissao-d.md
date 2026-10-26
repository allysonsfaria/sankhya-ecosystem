---
id: "43549185856407"
titulo: "Erro \"Certificado inválido para emissão de NFC-e no Checkout\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549185856407-Erro-Certificado-inv%C3%A1lido-para-emiss%C3%A3o-de-NFC-e-no-Checkout"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-09-30T13:30:42Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Erro "Certificado inválido para emissão de NFC-e no Checkout"

**Mensagem**

Certificado e inválido para emissão de NFCe. Verifique a data de validade"

![Imagem 1: Certificado e inválido para emissão de NFCe. Verifique a data de validade"](https://ajuda.sankhya.com.br/hc/article_attachments/43874944679191)

**Situação**

Esse alerta ocorre no Sankhya Checkout no momento em que o operador tenta emitir ou transmitir uma NFC-e.

**Solução**

Para regularizar a emissão, será necessário atualizar o certificado digital utilizado no caixa.

- Siga o passo a passo detalhado no artigo: [**Como incluir/alterar certificado no Sankhya Checkout**](https://ajuda.sankhya.com.br/hc/pt-br/articles/4414028967191-Como-incluir-alterar-certificado-no-Sankhya-Checkout).

Após a atualização, tente emitir a NFC-e novamente.

**Causa**

O bloqueio acontece porque o sistema ou a SEFAZ identificou que o certificado digital vinculado ao caixa apresenta alguma irregularidade. Isso geralmente ocorre quando o certificado está:

- Vencido;
- Inválido ou corrompido;
- Não autorizado ou sem as extensões obrigatórias para a emissão de NFC-e.
