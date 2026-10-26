---
id: "37223202875287"
titulo: "E0281 Rejeição: O NIF ou cNaoNIF do intermediário deve ser informado quando o grupo de informações de endereço no exterior do intermediário de serviços foi informado."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223202875287-E0281-Rejei%C3%A7%C3%A3o-O-NIF-ou-cNaoNIF-do-intermedi%C3%A1rio-deve-ser-informado-quando-o-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-no-exterior-do-intermedi%C3%A1rio-de-servi%C3%A7os-foi-informado"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:57Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "NIF (Número de Identificação Fiscal)", "Identificação de Estrangeiro", "Intermediário de serviços estrangeiro", "Grupo de endereço no exterior do intermediário", "Código de não preenchimento do NIF", "É obrigatório informar o NIF ou justificar sua ausência", "Não preencheu o NIF", "Endereço no exterior do intermediário", "NF-e ou NFC-e", "O NIF ou cNaoNIF do intermediário deve ser informado"]
---

# E0281 Rejeição: O NIF ou cNaoNIF do intermediário deve ser informado quando o grupo de informações de endereço no exterior do intermediário de serviços foi informado.

**MENSAGEM**

E0281 Rejeição: O NIF ou cNaoNIF do intermediário deve ser informado quando o grupo de informações de endereço no exterior do intermediário de serviços foi informado.

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com intermediário de serviços estrangeiro, o usuário informou o **endereço no exterior do intermediário**, porém **não preencheu o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF) do intermediário. Com isso, a nota fiscal foi rejeitada pela Sefaz com a mensagem de erro E0281.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do interdiário estrangeiro utilizado na operação.

**(3)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o número do passaporte ou documento estrangeiro do intermediário.

**(4)** Caso o intermediário possua **NIF** (Número de Identificação Fiscal no país de residência), informe este número no campo apropriado do cadastro.

**(5)** Caso o intermediário **não possua NIF**, informe o **código de não preenchimento do NIF** (cNaoNIF) conforme as opções disponíveis:

- **''1 - Dispensado do NIF''**
- **''2 - Não obrigado a inscrição''**
- **''3 - Outros''**

**(6)** Salve as alterações realizadas no cadastro do parceiro.

**(7)** Retorne à **NF-e** ou **NFC-e** que apresentou a rejeição e realize um **novo lançamento** do documento fiscal. 

**CAUSA**

A rejeição ocorre quando é emitida uma **NF-e** ou **NFC-e** com **intermediário de serviços estrangeiro** e o sistema identifica que foi informado o **grupo de endereço no exterior do intermediário**, porém **não foi preenchido o NIF** (Número de Identificação Fiscal) ou o **código de não preenchimento do NIF** (cNaoNIF). Conforme as regras de validação da Sefaz, quando há informações de endereço no exterior do intermediário, é **obrigatório informar o NIF ou justificar sua ausência** através do código cNaoNIF, garantindo a correta identificação fiscal do intermediário estrangeiro na operação.
