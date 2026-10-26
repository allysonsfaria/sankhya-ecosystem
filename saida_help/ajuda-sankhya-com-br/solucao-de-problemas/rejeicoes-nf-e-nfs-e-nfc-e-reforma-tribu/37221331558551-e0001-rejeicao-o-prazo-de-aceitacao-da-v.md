---
id: "37221331558551"
titulo: "E0001 Rejeição: O prazo de aceitação da versão do leiaute da DPS expirou."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221331558551-E0001-Rejei%C3%A7%C3%A3o-O-prazo-de-aceita%C3%A7%C3%A3o-da-vers%C3%A3o-do-leiaute-da-DPS-expirou"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:46Z"
rotulos: ["Configuração", "Fiscal", "Atualização", "SEFAZ", "Passos para resolver", "Erro", "Como Resolver", "Declaração de Prestação de Serviços (DPS)", "Novo leiaute da DPS", "Prazos de vigência", "Versão do leiaute da DPS", "Prazo de validade da versão do leiaute", "Instalação da versão mais recente"]
---

# E0001 Rejeição: O prazo de aceitação da versão do leiaute da DPS expirou.

**MENSAGEM**

E0001 Rejeição: O prazo de aceitação da versão do leiaute da DPS expirou.

**SITUAÇÃO**

Ao tentar transmitir a **Declaração de Prestação de Serviços (DPS)** para a Secretaria da Fazenda (Sefaz), o documento foi rejeitado com a mensagem informando que **o prazo de validade da versão do leiaute utilizado expirou**.

**SOLUÇÃO**

Para resolver esta rejeição, é necessário **atualizar o sistema** para a versão que contemple o **leiaute vigente da DPS**. Siga os passos abaixo:

**(1)** Verifique se o sistema Sankhya está **atualizado para a versão mais recente** que suporta o leiaute vigente da DPS. Entre em contato com o setor responsável pelas atualizações do sistema para confirmar a **versão instalada.**

**(2)** Caso o sistema não esteja atualizado, solicite a **instalação da versão mais recente** que contemple as adequações necessárias para o **novo leiaute da DPS**.

**(3)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa) e verifique se a **versão do leiaute está configurada corretamente** conforme a data de vigência estabelecida pela Sefaz.

**(4)** Certifique-se de que a **data-base da escrituração** está dentro do período de validade da versão do leiaute selecionada. O sistema deve selecionar automaticamente a **versão vigente** conforme a data informada.

**(5)** Gere novamente a **DPS** e transmita o arquivo para a Sefaz. O documento deverá ser aceito com a **versão atualizada do leiaute**.

**CAUSA**

A rejeição ocorre porque o sistema está utilizando uma **versão de leiaute da DPS que já expirou** e não é mais aceita pela Sefaz. A Secretaria da Fazenda estabelece **prazos de vigência** para cada versão do leiaute, e após a data de expiração, apenas a **versão atualizada** é aceita para transmissão. Quando o sistema não está atualizado ou não seleciona automaticamente a versão vigente, o arquivo é rejeitado com a mensagem **E0001**.
