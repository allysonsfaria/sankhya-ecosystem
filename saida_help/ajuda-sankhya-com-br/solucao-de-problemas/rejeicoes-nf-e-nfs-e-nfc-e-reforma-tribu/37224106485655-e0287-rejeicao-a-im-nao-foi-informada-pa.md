---
id: "37224106485655"
titulo: "E0287 Rejeição: A IM não foi informada para o emitente intermediário do serviço na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224106485655-E0287-Rejei%C3%A7%C3%A3o-A-IM-n%C3%A3o-foi-informada-para-o-emitente-intermedi%C3%A1rio-do-servi%C3%A7o-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:55Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Erro", "Documento de Prestação de Serviços (DPS)", "Inscrição Municipal (IM)", "Identificação fiscal do emitente intermediário do serviço", "Emitente intermediário do serviço", "IM não foi informada para o emitente intermediário"]
---

# E0287 Rejeição: A IM não foi informada para o emitente intermediário do serviço na DPS.

**MENSAGEM**

E0287 Rejeição: A IM não foi informada para o emitente intermediário do serviço na DPS.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário informou um **emitente intermediário do serviço**, porém **não preencheu a Inscrição Municipal (IM)** deste intermediário. Como a IM é uma informação obrigatória para identificação fiscal do prestador intermediário, a Sefaz rejeitou o documento com a mensagem E0287.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Empresas''** (Configurações » Cadastros » Empresas).

**(2)** Localize o cadastro do emitente intermediário do serviço informado da DPS.

**(3)** Na aba **"Geral"**, no campo **"Inscrição Municipal (IM)"**, preencha com a inscrição municipal correta do intermediário.

**(4)** Salve as alterações realizadas no cadastro do parceiro.

**(5)** Retorne ao Documento de Prestação de Serviços (DPS) rejeitado e atualize as informações do emitente intermediário, garantindo que a **IM** esteja preenchida.

**(6)** Transmita novamente o documento para a Sefaz. 

**CAUSA**

A rejeição ocorre porque a **Inscrição Municipal (IM)** é uma informação **obrigatória** para identificação fiscal do **emitente intermediário do serviço** no Documento de Prestação de Serviços (DPS). Quando este campo não é preenchido no cadastro do parceiro ou não é transmitido corretamente no documento fiscal, a Sefaz não consegue validar a regularidade fiscal do intermediário e, consequentemente, rejeita o documento com a mensagem E0287.
