---
id: "37223068866583"
titulo: "E0262 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao intermediário do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223068866583-E0262-Rejei%C3%A7%C3%A3o-Na-emiss%C3%A3o-da-NFS-e-n%C3%A3o-%C3%A9-permitido-que-o-prestador-do-servi%C3%A7o-seja-igual-ao-intermedi%C3%A1rio-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:04Z"
rotulos: ["Fiscal", "Prefeituras", "NFS-e", "Passos para resolver", "Erro", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "Intermediário do serviço", "CNPJ/CPF do prestador do serviço", "Prestador do serviço é igual ao intermediário do serviço"]
---

# E0262 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao intermediário do serviço.

**MENSAGEM**

E0262 Rejeição: Na emissão da NFS-e não é permitido que o prestador do serviço seja igual ao intermediário do serviço.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o sistema identifica que o **CNPJ/CPF do prestador do serviço** é o mesmo do **intermediário do serviço**, resultando na rejeição da nota pela prefeitura.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela de **emissão da NFS-e** e verifique se há informações de **intermediário do serviço** preenchidas.

**(2)** Caso o serviço **não possua intermediário**, remova as informações do campo **"Intermediário"** ou deixe-o em branco.

**(3)** Se o serviço **realmente possui um intermediário**, certifique-se de que o **CNPJ/CPF informado** seja diferente do CNPJ/CPF da empresa prestadora do serviço.

**(4)** Após realizar os ajustes necessários, emita novamente a **NFS-e**.

**CAUSA**

A rejeição ocorre quando o sistema identifica que o **CNPJ/CPF do prestador do serviço** é idêntico ao **CNPJ/CPF do intermediário** informado na NFS-e. De acordo com as regras da prefeitura, **não é permitido que a mesma empresa seja prestadora e intermediária** do serviço simultaneamente, pois isso caracteriza uma inconsistência fiscal. O intermediário deve ser sempre uma **terceira parte** envolvida na operação.
