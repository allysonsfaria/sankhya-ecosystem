---
id: "37226223658007"
titulo: "E0534 Rejeição: Não é permitido o preenchimento de informações relativas à benefício municipal para o prestador de serviço MEI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226223658007-E0534-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-benef%C3%ADcio-municipal-para-o-prestador-de-servi%C3%A7o-MEI"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:12Z"
rotulos: ["ISS", "Configuração", "Impostos", "NFS-e", "Erro", "Artigo atualizado KCS", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Benefício municipal para o prestador de serviço MEI", "Regime tributário simplificado e específico", "Microempresário Individual (MEI)", "Benefícios fiscais municipais", "MEI", "Docs Eletrônicos - KCS"]
---

# E0534 Rejeição: Não é permitido o preenchimento de informações relativas à benefício municipal para o prestador de serviço MEI

**MENSAGEM**

E0534 Rejeição: Não é permitido o preenchimento de informações relativas à benefício municipal para o prestador de serviço MEI

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o sistema rejeitou o documento com a mensagem de erro **E0534**. Esta rejeição ocorre quando a empresa está cadastrada como **Microempresário Individual (MEI)** e foram preenchidas informações relacionadas a **benefícios fiscais municipais** na nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa) e localize a empresa emissora da NFS-e.

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**, verifique se o campo **''Regime esp. tributação ISS (NFS-e)''** está configurado com a opção **"5 - Microempresário Individual (MEI)"**.

**(3)** Acesse a tela de emissão da **NFS-e** e remova qualquer informação relacionada a **benefícios fiscais municipais** que tenha sido preenchida no documento.

**(4)** Caso a empresa **não seja MEI**, retorne aos **passos 1 e 2** e ajuste o campo ''Regime esp. tributação ISS (NFS-e)'' para o regime tributário correspondente à realidade da empresa, conforme as opções disponíveis:

- **''1 – Microempresa Municipal''**
- **''2 – Estimativa''**
- **''3 – Sociedade de Profissionais''**
- **''4 – Cooperativa''**
- **''6 – Microempresa e Empresa de Pequeno Porte (ME/EPP)''**

**(5)**  Após realizar os ajustes necessários, emita novamente a **NFS-e**.

**CAUSA**

A rejeição ocorre porque a **legislação municipal não permite** que prestadores de serviço enquadrados como **Microempresário Individual (MEI)** utilizem benefícios fiscais municipais na emissão de NFS-e. O MEI possui um **regime tributário simplificado e específico**, incompatível com o preenchimento de informações sobre benefícios fiscais que são aplicáveis a outros regimes de tributação do ISS.
