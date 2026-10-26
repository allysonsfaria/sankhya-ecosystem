---
id: "37226162207255"
titulo: "E0593 Rejeição: Não permitido o valor \"0 - Imunidade (tipo não informado na nota de origem)\" na DPS quando utilizado os Emissores Públicos Nacionais para emissão de NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226162207255-E0593-Rejei%C3%A7%C3%A3o-N%C3%A3o-permitido-o-valor-0-Imunidade-tipo-n%C3%A3o-informado-na-nota-de-origem-na-DPS-quando-utilizado-os-Emissores-P%C3%BAblicos-Nacionais-para-emiss%C3%A3o-de-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:15Z"
rotulos: ["Configuração", "Alíquota de ISS", "Impostos", "TOP", "Prefeituras", "NFS-e", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "0 - Imunidade (tipo não informado na nota de origem)", "natureza de operação do ISS", "Emissores Públicos Nacionais", "exigibilidade do ISS"]
---

# E0593 Rejeição: Não permitido o valor "0 - Imunidade (tipo não informado na nota de origem)" na DPS quando utilizado os Emissores Públicos Nacionais para emissão de NFS-e.

**MENSAGEM**

E0593 Rejeição: Não permitido o valor "0 - Imunidade (tipo não informado na nota de origem)" na DPS quando utilizado os Emissores Públicos Nacionais para emissão de NFS-e.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)** utilizando os **Emissores Públicos Nacionais**, o sistema rejeitou o documento com a mensagem E0593.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste a **natureza de operação do ISS** configurada no sistema:

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Configurações » Cadastros » Tipos de Operação).

**(2)** Localize e selecione o **Tipo de Operação** utilizado na emissão da NFS-e rejeitada.

**(3)** Acesse a aba **"NFS-e"**.

**(4)** No campo **"Cód. Natureza Oper. ISS (NFS-e)"**, selecione uma das opções válidas permitidas pela prefeitura:

- **''Exigível''**
- **''Não incidência''**
- **''Isenção''**
- **''Exportação''**
- **''Imunidade''**
- **''Exigibilidade suspensa por decisão judicial''**
- **''Exigibilidade suspensa por procedimento administrativo''**

**(5)** Salve as alterações realizadas.

**(6)** Emita novamente a **NFS-e** utilizando o Tipo de Operação ajustado. 

**CAUSA**

A rejeição ocorreu porque o código **"0 - Imunidade (tipo não informado na nota de origem)"** não é aceito pelos **Emissores Públicos Nacionais** para emissão de NFS-e. Este código específico não está entre as opções válidas de **exigibilidade do ISS** permitidas pelas prefeituras que utilizam o padrão ABRASF. O sistema deve enviar apenas os códigos de **1 a 7**, conforme especificado na documentação técnica da prefeitura.
