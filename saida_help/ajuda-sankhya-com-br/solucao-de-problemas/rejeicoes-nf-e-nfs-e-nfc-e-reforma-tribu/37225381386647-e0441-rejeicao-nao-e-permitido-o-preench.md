---
id: "37225381386647"
titulo: "E0441 Rejeição: Não é permitido o preenchimento de informações relativas à Dedução/Redução para o prestador de serviço ME/EPP, apurando pelo SN conforme parametrização do código de serviço administrado pelo município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225381386647-E0441-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-para-o-prestador-de-servi%C3%A7o-ME-EPP-apurando-pelo-SN-conforme-parametriza%C3%A7%C3%A3o-do-c%C3%B3digo-de-servi%C3%A7o-administrado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:01Z"
rotulos: ["Configuração", "Simples Nacional", "Impostos", "NFS-e", "ISSQN", "Cód. Natureza Oper. ISS (NFS-e)", "Microempresa (ME) ou Empresa de Pequeno Porte (EPP)", "Município de incidência do ISSQN", "ME/EPP", "Deduções ou reduções na base de cálculo do ISSQN", "Dedução/Redução para o prestador de serviço ME/EPP"]
---

# E0441 Rejeição: Não é permitido o preenchimento de informações relativas à Dedução/Redução para o prestador de serviço ME/EPP, apurando pelo SN conforme parametrização do código de serviço administrado pelo município de incidência do ISSQN.

**MENSAGEM**

E0441 Rejeição: Não é permitido o preenchimento de informações relativas à Dedução/Redução para o prestador de serviço ME/EPP, apurando pelo SN conforme parametrização do código de serviço administrado pelo município de incidência do ISSQN.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e, o sistema apresenta a mensagem de rejeição quando a empresa prestadora de serviço está configurada como **Microempresa (ME) ou Empresa de Pequeno Porte (EPP)** optante pelo **Simples Nacional**, e foram preenchidas informações de **dedução ou redução da base de cálculo do ISSQN** na nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)**  Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize o tipo de operação utilizado na emissão da NFS-e.

**(3)** Acesse a aba **"NFS-e"** e verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"**.

**(4)** Certifique-se de que **não esteja configurado com a opção "B - Com dedução/Materiais"**, pois esta opção não é permitida para empresas optantes pelo Simples Nacional.

**(5)** Altere o campo **"Cód. Natureza Oper. ISS (NFS-e)"** para uma das seguintes opções permitidas:

- **''A - Sem dedução''**
- **''C - Imune/Isenta ISSQN''**
- **''D - Devolução/Simples remessa''**
- **''J - Intermediação''**

**(5)** Acesse a tela [**"Empresa"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(6)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, sub-aba **''Geral''** verifique se o campo **"Cód. Reg. Esp. trib. ISS (NFS-e)"** está configurado corretamente.

**(7)** Para empresas optantes pelo Simples Nacional, utilize os códigos apropriados conforme o município, como **"M - MEI (Simples Nacional)"** ou equivalente.

**(8)** Após realizar os ajustes necessários, emita novamente a NFS-e. A nota deverá ser transmitida sem a rejeição.

**CAUSA**

A rejeição ocorre porque o **município de incidência do ISSQN não permite** que empresas prestadoras de serviço enquadradas como **Microempresa (ME) ou Empresa de Pequeno Porte (EPP)**, optantes pelo **Simples Nacional**, utilizem **deduções ou reduções na base de cálculo do ISSQN**. Quando o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está configurado com a opção **"B - Com dedução/Materiais"**, o sistema envia informações de dedução no XML da nota, o que viola as regras de validação da prefeitura para este regime tributário.
