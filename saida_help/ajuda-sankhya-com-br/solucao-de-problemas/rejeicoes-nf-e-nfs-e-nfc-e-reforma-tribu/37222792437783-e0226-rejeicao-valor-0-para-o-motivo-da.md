---
id: "37222792437783"
titulo: "E0226 Rejeição: Valor 0 para o motivo da não informação do NIF do tomador não é permitido na Sefin do Sistema Nacional NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222792437783-E0226-Rejei%C3%A7%C3%A3o-Valor-0-para-o-motivo-da-n%C3%A3o-informa%C3%A7%C3%A3o-do-NIF-do-tomador-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:25Z"
rotulos: ["Configuração", "Parceiro", "XML", "SEFAZ", "NFS-e", "Erro", "Identificação de Estrangeiro", "Tomador estrangeiro no padrão nacional", "nifTomador", "Valor 0 para o motivo da não informação do NIF", "Não é permitido o valor 0 (zero) para o motivo da não informação do NIF"]
---

# E0226 Rejeição: Valor 0 para o motivo da não informação do NIF do tomador não é permitido na Sefin do Sistema Nacional NFS-e.

**MENSAGEM**

E0226 Rejeição: Valor 0 para o motivo da não informação do NIF do tomador não é permitido na Sefin do Sistema Nacional NFS-e.

**SITUAÇÃO**

Ao emitir uma **NFS-e no padrão nacional** para um **tomador estrangeiro**, o sistema rejeitou a nota com a mensagem E0226, informando que não é permitido o valor 0 (zero) para o motivo da não informação do NIF do tomador.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o **tomador estrangeiro** para o qual a NFS-e será emitida.

**(3)** Acesse a aba **"Identificação"**, no campo **''Identificação de Estrangeiro''**, preencha com o código **''NIF''** Número de Identificação Fiscal) do tomador estrangeiro.

**(4)** Caso o tomador não possua NIF, verifique no **manual de integração da prefeitura** se há orientações específicas sobre como proceder com tomadores estrangeiros sem NIF.

**(5)**  Salve as alterações realizadas no cadastro do parceiro.

**(6)**  Emita novamente a **NFS-e** para o tomador estrangeiro.

**CAUSA**

A rejeição ocorre porque o campo **"Identificação de Estrangeiro"** no cadastro do parceiro tomador **não foi preenchido** ou foi preenchido com valor inválido. Quando uma NFS-e é emitida para um **tomador estrangeiro** no padrão nacional, a tag **<nifTomador>** é gerada no XML. Se o campo **"Identificação de Estrangeiro"** estiver vazio ou com valor 0 (zero), a tag será gerada sem informação válida, resultando na **rejeição E0226** pela Sefin do Sistema Nacional NFS-e, que não permite o valor 0 para o motivo da não informação do NIF.
