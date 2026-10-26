---
id: "37226599163287"
titulo: "REJEIÇÃO E0667: Município da incidência do ISSQN não autoriza que o CPF do tomador informado na DPS seja indicado para retenção deste imposto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226599163287-REJEI%C3%87%C3%83O-E0667-Munic%C3%ADpio-da-incid%C3%AAncia-do-ISSQN-n%C3%A3o-autoriza-que-o-CPF-do-tomador-informado-na-DPS-seja-indicado-para-reten%C3%A7%C3%A3o-deste-imposto"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:48Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Prefeituras", "NFS-e", "Erro", "Inscrição Municipal (IM)", "Retenção do ISSQN", "Município da incidência do ISSQN", "Retenção de ISS", "Manual da prefeitura do município"]
---

# REJEIÇÃO E0667: Município da incidência do ISSQN não autoriza que o CPF do tomador informado na DPS seja indicado para retenção deste imposto

**MENSAGEM**

E0667 Rejeição: Município da incidência do ISSQN não autoriza que o CPF do tomador informado na DPS seja indicado para retenção deste imposto.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e com **retenção de ISSQN** para um tomador de serviço **pessoa física** (identificado por CPF), a nota é rejeitada pela prefeitura com a mensagem acima, indicando que o município não permite que pessoas físicas sejam responsáveis pela retenção do imposto.

**SOLUÇÃO**

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Na aba **''Fiscal'**' verifique o campo **''Retém ISS''**.

**(3)** Se necessário, desabilite a configuração relacionada a retenção de ISS.

**(4)** Caso o tomador seja **pessoa jurídica** e esteja devidamente inscrito no município, verifique se:

- O **"CNPJ"** está correto no cadastro do parceiro.
- A **"Inscrição Municipal"** está preenchida corretamente.
- O tomador está **cadastrado na base de dados do município** como contribuinte autorizado a reter ISS.

**(5)** Consulte o **manual da prefeitura do município** onde ocorre a prestação do serviço para verificar se há **restrições quanto à retenção de ISS por pessoas físicas.**

**(6)** Após realizar os ajustes necessários, **emita novamente a NFS-e**. 

**CAUSA**

A rejeição ocorre porque o **município não permite que pessoas físicas** (identificadas por CPF) sejam responsáveis pela **retenção do ISSQN**. A legislação municipal estabelece que apenas **pessoas jurídicas devidamente inscritas** no município podem efetuar a retenção do imposto. Quando a nota é emitida com retenção de ISS para um tomador pessoa física, ou quando o tomador pessoa jurídica não está cadastrado na base de dados do município, a prefeitura rejeita o documento fiscal com a mensagem E0667.
