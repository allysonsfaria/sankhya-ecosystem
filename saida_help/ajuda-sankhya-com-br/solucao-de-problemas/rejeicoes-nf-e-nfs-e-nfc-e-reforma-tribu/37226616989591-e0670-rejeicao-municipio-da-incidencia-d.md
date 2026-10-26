---
id: "37226616989591"
titulo: "E0670 Rejeição: Município da incidência do ISSQN não autoriza que o CPF do intermediário informado na DPS seja indicado para retenção deste imposto."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226616989591-E0670-Rejei%C3%A7%C3%A3o-Munic%C3%ADpio-da-incid%C3%AAncia-do-ISSQN-n%C3%A3o-autoriza-que-o-CPF-do-intermedi%C3%A1rio-informado-na-DPS-seja-indicado-para-reten%C3%A7%C3%A3o-deste-imposto"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:47Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Município de incidência do ISSQN", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Retenção de ISSQN configurada", "Retenção de ISSQN"]
---

# E0670 Rejeição: Município da incidência do ISSQN não autoriza que o CPF do intermediário informado na DPS seja indicado para retenção deste imposto.

**MENSAGEM**

E0670 Rejeição: Município da incidência do ISSQN não autoriza que o CPF do intermediário informado na DPS seja indicado para retenção deste imposto.

**SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica) com **intermediário de serviço informado** e com **retenção de ISSQN configurada**, o sistema apresenta a mensagem de rejeição acima, impedindo a autorização do documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Parceiros"** (Comercial » Arquivo » Cadastros » Parceiros) e localize o **cadastro do tomador do serviço**.

**(2)** Na aba **"Impostos"**, localize o campo **"ISSQN Retido"** e verifique a configuração atual:

- Se estiver marcado como **"1 - Com retenção de ISSQN"**, altere para **"2 - Sem retenção de ISSQN"**.

**(3)** Salve as alterações realizadas no cadastro do parceiro.

**(4)** Retorne à tela de emissão da NFS-e e **gere novamente o lote** da nota fiscal.

**(5)** Se o erro persistir, **valide no manual da Prefeitura do município** se é permitida a retenção de ISSQN quando há intermediário de serviço envolvido na operação.

**(6)** Caso a Prefeitura não permita a retenção nesta situação, **remova as informações do intermediário** ou mantenha a configuração **"Sem retenção de ISSQN"** no cadastro do parceiro.

**CAUSA**

A rejeição ocorre porque o **município de incidência do ISSQN não permite** que seja indicada a **retenção do imposto quando há um intermediário** (pessoa física ou jurídica) envolvido na prestação do serviço. Esta é uma **regra específica da legislação municipal**, que varia conforme o município emissor da nota fiscal.

O sistema enviou no XML da NFS-e tanto as informações do intermediário quanto a marcação de retenção do ISSQN, configuração que não é aceita pela Prefeitura.
