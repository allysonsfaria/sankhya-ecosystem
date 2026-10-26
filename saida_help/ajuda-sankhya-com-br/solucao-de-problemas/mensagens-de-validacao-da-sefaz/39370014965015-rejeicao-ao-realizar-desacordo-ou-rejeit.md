---
id: "39370014965015"
titulo: "Rejeição ao Realizar Desacordo ou Rejeitar CT-e: Versão XML 3.0 Não Suportada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39370014965015-Rejei%C3%A7%C3%A3o-ao-Realizar-Desacordo-ou-Rejeitar-CT-e-Vers%C3%A3o-XML-3-0-N%C3%A3o-Suportada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-02T20:17:32Z"
rotulos: ["ERROCTE", "CT-e", "Configuração", "XML", "SEFAZ", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Rejeição ao Realizar Desacordo ou Rejeitar CT-e: Versão XML 3.0 Não Suportada

**MENSAGEM**

Rejeição: Cabecalho - Versao do arquivo XML não suportada [Versao 3 com vigencia encerrada (ATO COTEPE/ICMS 123/22), utilize a Versao 4.00]

**SITUAÇÃO**

Esta mensagem de rejeição ocorre ao tentar realizar o desacordo da prestação de serviço de um CT-e ou ao tentar rejeitar um CT-e no sistema. O erro é apresentado pela SEFAZ quando o arquivo XML está sendo processado com a versão 3.00 do CT-e, que teve sua vigência encerrada conforme o Ato Cotepe/Icms 123/22.

**SOLUÇÃO**

Para resolver este erro, configure a empresa para utilizar a versão 4.00 do CT-e. Siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).
**(2)** Navegue até a aba **"Documentos Fiscais Eletrônicos"**.
**(3)** Acesse a seção **"CT-e"** e depois **"Geral"**.
**(4)** Marque a opção **"Usar modo síncrono para envio do XML"**.
**(5)** No campo **"Versão CT-e"**, selecione a opção **"Versão CT-e 4.00"**.
**(6)** Salve as configurações realizadas.

Após realizar estas configurações, o arquivo será processado com sucesso utilizando a versão 4.00 do CT-e.

**CAUSA**

A rejeição ocorre porque a empresa está configurada para utilizar a versão 3.00 do CT-e, que teve sua vigência encerrada conforme determinação do Ato COTEPE/ICMS 123/22. A SEFAZ não aceita mais o processamento de arquivos XML nesta versão, sendo obrigatório o uso da versão 4.00 para envio e processamento de CT-e.
