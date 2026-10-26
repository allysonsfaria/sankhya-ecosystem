---
id: "37222208047511"
titulo: "E0128 Rejeição: O endereço do prestador do serviço não deve ser informado na DPS quando o próprio prestador for o emitente da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222208047511-E0128-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-do-prestador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-prestador-for-o-emitente-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:58Z"
rotulos: ["Central de Vendas", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "Emitente da DPS", "DPS (Documento de Prestação de Serviços)", "Prestador do serviço", "Prestador do serviço é o próprio emitente"]
---

# E0128 Rejeição: O endereço do prestador do serviço não deve ser informado na DPS quando o próprio prestador for o emitente da DPS.

**MENSAGEM**

E0128 Rejeição: O endereço do prestador do serviço não deve ser informado na DPS quando o próprio prestador for o emitente da DPS.

**SITUAÇÃO**

Mensagem apresentada ao emitir uma **DPS (Documento de Prestação de Serviços)** em que o **prestador do serviço é o próprio emitente** do documento fiscal, mas foram informados dados de endereço do prestador no grupo específico destinado a essa finalidade.

**SOLUÇÃO**

Para resolver esta rejeição, **não informe o endereço do prestador** no grupo específico da DPS quando o prestador for o próprio emitente do documento:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Verifique se o **prestador do serviço** informado no documento é o **mesmo emitente da DPS**.

**(3)** Certifique-se de que o **grupo de endereço do prestador** não esteja preenchido na DPS, pois quando o prestador é o próprio emitente, **essas informações não devem ser informadas**.

**(4)** Remova qualquer informação de endereço do prestador que tenha sido preenchida indevidamente.

**(5)** Salve as alterações e tente emitir novamente a DPS.

**CAUSA**

A rejeição ocorre porque, de acordo com as **regras de validação da Sefaz** estabelecidas pela **Lei Complementar nº 214/2025** (Reforma Tributária), quando o **prestador do serviço é o próprio emitente da DPS**, o grupo de informações de endereço do prestador **não deve ser preenchido** no documento fiscal. Isso acontece porque os dados do emitente já constam no cabeçalho do documento, tornando **redundante e incorreta** a inclusão dessas informações novamente no grupo específico do prestador. A validação visa garantir a **consistência e integridade** dos dados transmitidos à Sefaz.
