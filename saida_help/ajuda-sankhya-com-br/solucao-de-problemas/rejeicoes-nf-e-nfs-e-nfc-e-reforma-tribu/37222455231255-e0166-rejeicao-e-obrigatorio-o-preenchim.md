---
id: "37222455231255"
titulo: "E0166 Rejeição: É obrigatório o preenchimento do campo de regime de apuração dos tributos do SN para o optante do Simples Nacional ME/EPP."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222455231255-E0166-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-o-preenchimento-do-campo-de-regime-de-apura%C3%A7%C3%A3o-dos-tributos-do-SN-para-o-optante-do-Simples-Nacional-ME-EPP"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:47Z"
rotulos: ["Configuração", "Simples Nacional", "Impostos", "NFS-e", "NFS-e (Nota Fiscal de Serviço Eletrônica)", "optante pelo Simples Nacional", "Empresas ME/EPP optantes pelo Simples Nacional", "Regime de Apuração dos Tributos do Simples Nacional"]
---

# E0166 Rejeição: É obrigatório o preenchimento do campo de regime de apuração dos tributos do SN para o optante do Simples Nacional ME/EPP.

**MENSAGEM**

E0166 Rejeição: É obrigatório o preenchimento do campo de regime de apuração dos tributos do SN para o optante do Simples Nacional ME/EPP.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica) para uma empresa optante pelo **Simples Nacional**, o sistema apresenta a rejeição informando que é obrigatório o preenchimento do campo **"Regime de Apuração dos Tributos do Simples Nacional"**.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(2)** Na aba **"Naturezas"**, verifique se o campo **''Optante pelo SIMPLES''** está habilitado.

**(3)** Certifique-se de que o campo **"Cód. Regime Tribut."** está configurado como **"Simples Nacional"** ou **"Simples Nacional - Sublimite"**.

**(4)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(5)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**.

**(6)** Preencha o campo **"Regime de Apuração dos Tributos do Simples Nacional"** com uma das opções disponíveis:

- **''1 - Reg. Apuração Trib. Fed. e Mun. pelo SN''**
- **''2 - Reg. Apuração Trib. Fed. pelo SN e ISS pela NFSe conforme legislação municipal''**
- **''3 - Reg. Apuração Trib. Fed. e Mun. pela NFSe conforme legislação Fed. e Mun. de cada tributo''**

**(7)** Salve as alterações realizadas.

**(8)** Gere novamente a NFS-e e valide se a rejeição foi corrigida.

**CAUSA**

A rejeição ocorre quando a empresa está cadastrada como **optante pelo Simples Nacional**, mas o campo **"Regime de Apuração dos Tributos do Simples Nacional"** não foi preenchido na tela ''Empresa'' (Comercial » Preferências » Empresa). Este campo é **obrigatório** para empresas ME/EPP optantes pelo Simples Nacional que emitem NFS-e, pois define como os tributos federais e municipais serão apurados e informados no documento fiscal eletrônico.
