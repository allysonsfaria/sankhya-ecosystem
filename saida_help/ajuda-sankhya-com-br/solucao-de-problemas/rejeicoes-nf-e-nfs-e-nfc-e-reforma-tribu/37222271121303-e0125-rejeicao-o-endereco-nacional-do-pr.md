---
id: "37222271121303"
titulo: "E0125 Rejeição: O endereço nacional do prestador do serviço deve ser informado na DPS quando for identificado pelo CNPJ ou CPF e o emitente da DPS for o tomador ou intermediário."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222271121303-E0125-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-prestador-do-servi%C3%A7o-deve-ser-informado-na-DPS-quando-for-identificado-pelo-CNPJ-ou-CPF-e-o-emitente-da-DPS-for-o-tomador-ou-intermedi%C3%A1rio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:57Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "Erro", "Emitente da DPS for o tomador ou intermediário", "Emitente é o tomador ou intermediário do serviço", "Endereço nacional do prestador não foi informado corretamente", "Prestador do serviço foi identificado por CNPJ ou CPF"]
---

# E0125 Rejeição: O endereço nacional do prestador do serviço deve ser informado na DPS quando for identificado pelo CNPJ ou CPF e o emitente da DPS for o tomador ou intermediário.

**MENSAGEM**

E0125 Rejeição: O endereço nacional do prestador do serviço deve ser informado na DPS quando for identificado pelo CNPJ ou CPF e o emitente da DPS for o tomador ou intermediário.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)** na qual o **emitente é o tomador ou intermediário** do serviço, e o **prestador do serviço foi identificado por CNPJ ou CPF**, mas o **endereço nacional do prestador não foi informado** corretamente no documento, a Sefaz apresenta a rejeição E0125.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Na aba **"Endereço"**, verifique se o **endereço nacional do prestador** está completo e correto, incluindo:

- **Logradouro**
- **Número**
- **Complemento** (se aplicável)
- **Bairro**
- **Município**
- **UF**
- **CEP**

**(3)** Caso alguma informação esteja **ausente ou incorreta**, preencha ou corrija os dados do endereço nacional do prestador.

**(4)** Salve as alterações.

**(5)** Retorne à tela de emissão da **DPS** e **gere novamente o documento fiscal**, garantindo que as informações do endereço do prestador sejam transmitidas corretamente.

**CAUSA**

A rejeição E0125 ocorre quando uma **Declaração de Prestação de Serviços (DPS)** é emitida pelo **tomador ou intermediário** do serviço, e o **prestador é identificado por CNPJ ou CPF**, mas o **endereço nacional do prestador não foi informado** no documento fiscal. Conforme as regras de validação da Sefaz estabelecidas pela **Lei Complementar nº 214/2025**, quando o emitente da DPS for o tomador ou intermediário e o prestador for pessoa jurídica ou física nacional, é **obrigatório informar o endereço completo do prestador** no território nacional.
