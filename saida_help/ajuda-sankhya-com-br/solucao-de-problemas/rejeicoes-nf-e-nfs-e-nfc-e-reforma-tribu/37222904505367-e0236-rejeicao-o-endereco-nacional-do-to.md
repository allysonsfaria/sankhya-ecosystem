---
id: "37222904505367"
titulo: "E0236 Rejeição: O endereço nacional do tomador do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222904505367-E0236-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-n%C3%A3o-deve-ser-informado-na-DPS-quando-o-pr%C3%B3prio-tomador-do-servi%C3%A7o-for-o-emitente-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:15Z"
rotulos: ["Parceiro", "Central de Vendas", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Saiba como resolver", "Documento de Prestação de Serviço (DPS)", "Endereço nacional do tomador do serviço", "Dados de endereço nacional do tomador do serviço", "Próprio emitente da DPS é o tomador do serviço"]
---

# E0236 Rejeição: O endereço nacional do tomador do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

**MENSAGEM**

E0236 Rejeição: O endereço nacional do tomador do serviço não deve ser informado na DPS quando o próprio tomador do serviço for o emitente da DPS.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviço (DPS)**, o usuário informou os **dados de endereço nacional do tomador do serviço**, sendo que o **próprio emitente da DPS é o tomador do serviço**. Nesta situação, a SEFAZ rejeitou o documento com a mensagem E0236.

**SOLUÇÃO**

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Cabeçalho''**, verifque se o campo **''Parceiro'' (Tomador de Serviço)**, está preenchido com a mesma empresa emitente da DPS.

**(3)** **Remova as informações de endereço nacional** do tomador do serviço, uma vez que estes dados **não devem ser informados** quando o tomador for o próprio emitente.

**(4)** Realize novamente a **transmissão da DPS** para a SEFAZ. 

**CAUSA**

A rejeição ocorre porque a **regra de validação da SEFAZ** determina que, quando o **tomador do serviço for o próprio emitente da DPS**, os **dados de endereço nacional do tomador não devem ser informados** no documento fiscal. Esta validação visa **evitar redundância de informações**, uma vez que os dados do emitente já constam no documento. Ao preencher o endereço do tomador nesta situação, o sistema identifica a **inconsistência** e rejeita a DPS com a mensagem E0236.
