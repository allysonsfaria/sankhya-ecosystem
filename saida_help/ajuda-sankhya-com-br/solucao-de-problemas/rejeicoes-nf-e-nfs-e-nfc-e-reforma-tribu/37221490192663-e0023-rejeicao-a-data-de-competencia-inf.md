---
id: "37221490192663"
titulo: "E0023 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data do indicador municipal, registrada no CNC do município correspondente ao município emissor da DPS (cLocEmi)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221490192663-E0023-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-deve-ser-igual-ou-posterior-%C3%A0-data-do-indicador-municipal-registrada-no-CNC-do-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-da-DPS-cLocEmi"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:37Z"
rotulos: ["Cidades", "SEFAZ", "Impostos", "Prefeituras", "Erro", "Cadastro Nacional de Contribuintes (CNC)", "Emissão de uma DPS", "Cobrança do IBS Municipal", "Layout da DPS"]
---

# E0023 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data do indicador municipal, registrada no CNC do município correspondente ao município emissor da DPS (cLocEmi).

**MENSAGEM**

E0023 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data do indicador municipal, registrada no CNC do município correspondente ao município emissor da DPS (cLocEmi).

**SITUAÇÃO**

A mensagem de erro é apresentada ao tentar realizar a **emissão de uma DPS** (Declaração Prévia de Serviços) com data de competência anterior à data em que o município emissor iniciou a cobrança do IBS Municipal, conforme registrado no **Cadastro Nacional de Contribuintes (CNC)**.

**SOLUÇÃO**

**(1)** Verifique a **data de competência** informada na DPS que está sendo emitida.

**(2)** Consulte, no **Cadastro Nacional de Contribuintes (CNC)**, a **data do indicador municipal** registrada para o município emissor da DPS, a qual define a partir de quando o município passou a **exigir o IBS Municipal**.

**(3)** Confirme se a **data de competência da DPS** é **igual ou posterior** à data do indicador municipal informada no CNC.

**(4)** Caso a data de competência esteja incorreta, **ajuste-a para uma data válida**, conforme o critério estabelecido pela **SEFAZ**.

**(5)** Após realizar os ajustes necessários, **gere novamente a DPS** e **efetue o envio ao ambiente autorizador**.

**CAUSA**

A rejeição ocorre porque o **layout da DPS exige** que a data de competência informada no documento seja **igual ou posterior à data** em que o município emissor iniciou a cobrança do IBS Municipal, conforme registrado no **Cadastro Nacional de Contribuintes (CNC)**. Esta validação garante que não sejam emitidas declarações com competência anterior ao início da vigência da tributação municipal, em conformidade com as regras estabelecidas pela **Lei Complementar nº 214/2025** e pela **Emenda Constitucional nº 132/2023**, que implementam a Reforma Tributária.
