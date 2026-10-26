---
id: "34129799452823"
titulo: "Rejeição 285: Certificado Transmissor difere ICP-Brasil"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34129799452823-Rejei%C3%A7%C3%A3o-285-Certificado-Transmissor-difere-ICP-Brasil"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:27:40Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Rejeição 285", "certificado digital utilizado", "Certificado Transmissor difere ICP-Brasil", "apresentada ao tentar transmitir uma nota fiscal eletrônica", "não está de acordo com o padrão ICP-Brasil", "Documentos Eletrônicos"]
---

# Rejeição 285: Certificado Transmissor difere ICP-Brasil

**MENSAGEM**

Rejeição 285: Certificado Transmissor difere ICP-Brasil

**SITUAÇÃO**

A mensagem de rejeição é apresentada ao tentar transmitir uma nota fiscal eletrônica quando o certificado digital utilizado não está de acordo com o padrão ICP-Brasil exigido pela SEFAZ.

**SOLUÇÃO**

**(1)**  **Instabilidade na SEFAZ**

Aguarde alguns minutos e tente reenviar o documento, pois a rejeição pode ser causada por instabilidade temporária nos servidores da SEFAZ.

**(2)**  **Falta de Cadeias de Certificação**

Verifique se o certificado digital está corretamente configurado e atualizado. Certifique-se de que todas as cadeias de certificação estejam instaladas.
 • Caso necessário, realize a correção da cadeia de certificado seguindo as orientações disponíveis em [Link correção Cadeia de certificado da sefaz](https://ajuda.sankhya.com.br/hc/pt-br/articles/Link%20corre%C3%A7%C3%A3o%20Cadeia%20de%20certificado%20da%20sefaz).

**(3)** **Dados inválidos**

Confira se os dados da nota fiscal, como **"CNPJ"**, **"CFOP"** e **"destinatário"**, estão corretos e completos.

**(4)** **Problemas de validação de XML**

Valide o arquivo XML para garantir que ele segue o esquema exigido pela SEFAZ e não possui erros de formatação ou estrutura.

**(5)** **Certificado digital vencido**

Verifique se o certificado digital não está vencido. Caso esteja, providencie a renovação antes de tentar nova transmissão.

**CAUSA**

A rejeição ocorre quando o certificado digital utilizado, as cadeias de certificação, os dados da nota fiscal ou o arquivo XML estão em desconformidade com os requisitos da SEFAZ.
