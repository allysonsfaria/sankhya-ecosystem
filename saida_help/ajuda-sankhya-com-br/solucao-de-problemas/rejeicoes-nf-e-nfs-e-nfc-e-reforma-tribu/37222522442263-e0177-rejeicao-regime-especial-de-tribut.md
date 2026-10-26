---
id: "37222522442263"
titulo: "E0177 Rejeição: Regime especial de tributação informado na DPS não é admitido na parametrização do município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222522442263-E0177-Rejei%C3%A7%C3%A3o-Regime-especial-de-tributa%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-%C3%A9-admitido-na-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:42Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Regime especial de tributação do ISS", "Município de incidência do ISSQN", "Códigos de regime especial", "Regime especial de tributação informado na DPS", "Parametrização do município de incidência do ISSQN", "Documentos Eletrônicos"]
---

# E0177 Rejeição: Regime especial de tributação informado na DPS não é admitido na parametrização do município de incidência do ISSQN.

**MENSAGEM**

E0177 Rejeição: Regime especial de tributação informado na DPS não é admitido na parametrização do município de incidência do ISSQN.

**SITUAÇÃO**

Ao emitir uma **NFS-e**, a nota é rejeitada pela prefeitura com a mensagem de erro informando que o **regime especial de tributação** configurado não é permitido para o município de incidência do ISSQN.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)**  Acesse a tela **"Empresa"** (Configurações » Empresa » Preferências).

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"** sub-aba **"Geral"**.

**(3)** No campo **"Regime esp. trib. ISS (NFS-e)"**, verifique qual regime especial de tributação está configurado.

**(4)** Consulte o **manual da prefeitura** do município de incidência do ISSQN para identificar quais regimes especiais de tributação são admitidos. Os regimes disponíveis no sistema podem variar conforme o município, incluindo opções como:

- **''Microempresa municipal''**
- **''Estimativa''**
- **''Sociedade de profissionais''**
- **''Cooperativa''**
- **''Microempresário e Empresa de Pequeno Porte (ME EPP)''**
- **''Microempresário Individual (MEI)''**
- **''ISSQN Profissionais Autônomos''**
- **''Movimento Mensal''**

**(5)** Altere o campo **"Regime esp. trib. ISS (NFS-e)"** para um código de regime especial que seja **compatível com a parametrização do município** de incidência do ISSQN.

**(6)** Salve as alterações e tente emitir novamente a **NFS-e**.

**CAUSA**

A rejeição ocorre porque o **regime especial de tributação do ISS** configurado nas **Preferências da Empresa** não é permitido pela prefeitura do município de incidência informado na nota fiscal. Cada município possui suas próprias regras e **aceita apenas determinados códigos de regime especial**, conforme sua legislação tributária local.
