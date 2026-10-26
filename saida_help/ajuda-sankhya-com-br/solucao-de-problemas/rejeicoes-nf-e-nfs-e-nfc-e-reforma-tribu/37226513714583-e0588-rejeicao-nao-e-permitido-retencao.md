---
id: "37226513714583"
titulo: "E0588 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que tenha algum regime especial de tributação na data de competência informada na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226513714583-E0588-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-reten%C3%A7%C3%A3o-do-ISSQN-para-o-prestador-do-servi%C3%A7o-que-tenha-algum-regime-especial-de-tributa%C3%A7%C3%A3o-na-data-de-compet%C3%AAncia-informada-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:53Z"
rotulos: ["Configuração", "Empresa", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Regime especial de tributação", "Retenção do ISSQN", "Tipo de Retenção do ISS", "Não é permitida a retenção do ISSQN", "Data de competência da nota"]
---

# E0588 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que tenha algum regime especial de tributação na data de competência informada na DPS.

**MENSAGEM**

E0588 Rejeição: Não é permitido retenção do ISSQN para o prestador do serviço que tenha algum regime especial de tributação na data de competência informada na DPS.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e, o sistema apresenta a mensagem de rejeição informando que **não é permitida a retenção do ISSQN** quando o prestador do serviço possui algum **regime especial de tributação** configurado na data de competência da nota.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e"**, verifique o campo **"Regime esp. trib. ISS (NFS-e)"** e identifique qual regime especial está configurado para a empresa.

**(3)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

**(4)** Na aba **''Fiscal''**, desabilite o campo **''Retém ISS''**.

**(5)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(6)** Na aba **"NFS-e"**, verifique se o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está configurado corretamente para operações sem retenção.

**(7)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(8)** No rodapé, verifique a aba **''Impostos''**, verifique se o campo **''Tipo de Retenção do ISS''** está configurado como **''Não Retido''**.

**(9)** Após realizar os ajustes, tente emitir novamente a NFS-e. 

**CAUSA**

A rejeição ocorre porque a **legislação municipal não permite** que empresas prestadoras de serviço com **regime especial de tributação do ISS** (como Microempresa Municipal, Estimativa, Sociedade de Profissionais, Cooperativa, MEI, Simples Nacional, entre outros) efetuem a **retenção do ISSQN** na nota fiscal. Quando o sistema identifica que a empresa possui um regime especial configurado e, simultaneamente, está marcada a retenção de ISS no cadastro do tomador ou na operação, a nota é rejeitada pela prefeitura.
