---
id: "37221529446295"
titulo: "E0029 Rejeição: O motivo da emissão não pode ser preenchido se o emitente for o prestador de serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221529446295-E0029-Rejei%C3%A7%C3%A3o-O-motivo-da-emiss%C3%A3o-n%C3%A3o-pode-ser-preenchido-se-o-emitente-for-o-prestador-de-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:35Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Transporte", "Passos para resolver", "Erro", "Como Resolver", "Prestador de serviço", "MDF-e (Manifesto Eletrônico de Documentos Fiscais)", "Motivo da Emissão", "restador de Serviço de Transporte", "Tipo de emitente", "Documentos Eletrônicos"]
---

# E0029 Rejeição: O motivo da emissão não pode ser preenchido se o emitente for o prestador de serviço.

**MENSAGEM**

E0029 Rejeição: O motivo da emissão não pode ser preenchido se o emitente for o prestador de serviço.

**SITUAÇÃO**

Ao emitir um **MDF-e** (Manifesto Eletrônico de Documentos Fiscais) no modal rodoviário, onde o **tipo de emitente** está configurado como **"Prestador de Serviço de Transporte"**, o sistema apresenta a rejeição acima caso o campo **"Motivo da Emissão"** tenha sido preenchido indevidamente.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Viagens de Transporte (MDF-e)"** (Comercial » Rotinas » Viagens de Transporte (MDF-e)).

**(2)** Localize o **MDF-e** que está apresentando a rejeição e acesse a aba **"MDF-e"**.

**(3)** Verifique se o campo **"Tipo de Emissão"** está configurado como **"Prestador de Serviço de Transporte"**.

**(4)** Certifique-se de que o campo **"Motivo da Emissão"** esteja **vazio** ou **não preenchido**, pois este campo não deve ser informado quando o emitente for prestador de serviço de transporte.

**(5)** Caso o campo esteja preenchido, **remova** a informação inserida.

**(6)** Salve as alterações realizadas.

**(7)** Gere um **novo lote** do MDF-e e tente realizar a transmissão novamente.

**CAUSA**

A rejeição **E0029** ocorre devido à **validação da SEFAZ** que impede o preenchimento do campo **"Motivo da Emissão"** quando o **tipo de emitente** do MDF-e for configurado como **"Prestador de Serviço de Transporte"**. Esta regra visa garantir que apenas os campos obrigatórios e permitidos para este tipo de operação sejam preenchidos, evitando inconsistências nas informações fiscais transmitidas.
