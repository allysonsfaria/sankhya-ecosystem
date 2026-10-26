---
id: "37227013649431"
titulo: "E0676 Rejeição: Não é permitido o preenchimento das informações relativas aos tributos federais quando o emitente for identificado como MEI na data de competência informada na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37227013649431-E0676-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-das-informa%C3%A7%C3%B5es-relativas-aos-tributos-federais-quando-o-emitente-for-identificado-como-MEI-na-data-de-compet%C3%AAncia-informada-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-05T18:59:47Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Microempreendedor Individual (MEI)", "Tributos Federais", "NF-e ou NFC-e com tributos federais", "MEI"]
---

# E0676 Rejeição: Não é permitido o preenchimento das informações relativas aos tributos federais quando o emitente for identificado como MEI na data de competência informada na DPS.

**MENSAGEM**

E0676 Rejeição: Não é permitido o preenchimento das informações relativas aos tributos federais quando o emitente for identificado como MEI na data de competência informada na DPS.

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com informações de **tributos federais** (CBS - Contribuição sobre Bens e Serviços), sendo que a empresa emitente está cadastrada como **Microempreendedor Individual (MEI)** na data de competência informada no documento fiscal, o sistema da Sefaz rejeita a operação com a mensagem E0676.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresa) e localize o cadastro da empresa emitente.

**(2)** Na aba **''Naturezas''**, verifique se a empresta está cadastrada como MEI **(Microempreendedor Individual)** no campo **''Cód. Regime Tribut''** ou em campos relacionados ao enquadramento fiscal.

**(3)** Caso a empresa seja **MEI**, não preencha as informações de **tributos federais (CBS)** no documento fiscal, pois empresas enquadradas neste regime **não estão sujeitas** à tributação federal nos moldes da Reforma Tributária.

**(4)** Acesse a tela **"Alíquota IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquota CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS), e verifique se há alíquotas de CBS configuradas para os produtos ou serviços da operação.

**(5)** Remova ou desative as alíquotas de **CBS** vinculadas aos produtos/serviços quando a empresa emitente for **MEI**, garantindo que o campo **"Código de situação tributária'' (CST)** esteja configurado adequadamente para **''não tributação''** ou **''isenção''**.

**(6)** Após realizar os ajustes necessários, emita novamente o documento fiscal.

**CAUSA**

A rejeição ocorre porque **empresas enquadradas como MEI** (Microempreendedor Individual) **não estão sujeitas** ao recolhimento de tributos federais nos moldes da Reforma Tributária, como a **CBS**. Quando o sistema identifica que o emitente é **MEI** na data de competência do documento e detecta o preenchimento de informações de tributos federais, a Sefaz rejeita automaticamente a operação para garantir a conformidade com a legislação tributária vigente.
