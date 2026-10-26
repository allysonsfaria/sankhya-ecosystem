---
id: "37222212765847"
titulo: "E0123 Rejeição: O preenchimento do nome empresarial é obrigatório quando o prestador for identificado com NIF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222212765847-E0123-Rejei%C3%A7%C3%A3o-O-preenchimento-do-nome-empresarial-%C3%A9-obrigat%C3%B3rio-quando-o-prestador-for-identificado-com-NIF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:01Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Razão Social", "NFC-e", "Lei Complementar nº 214/2025", "NIF", "Prestador de serviço identificado com NIF", "É obrigatório informar o nome empresarial", "Documentos Eletrônicos"]
---

# E0123 Rejeição: O preenchimento do nome empresarial é obrigatório quando o prestador for identificado com NIF.

**MENSAGEM**

E0123 Rejeição: O preenchimento do nome empresarial é obrigatório quando o prestador for identificado com NIF.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) que contenha informações de um **prestador de serviço identificado com NIF** (Número de Identificação Fiscal do exterior), o sistema apresenta a rejeição E0123 caso o **campo "Razão Social"** do prestador não tenha sido preenchido.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize e selecione o **prestador de serviço** que está identificado com **NIF**.

**(3)** Na aba **''Fiscal''** na sessão **''Informações para REINF''**, verifique se o campo **''Indicativo no NIF''** está preenchido com uma das seguintes opções:

- **''Beneficiário com NIF''**;
- **''Beneficiário dispensado do NIF''**;
- **''País não exige NIF''**.

**(4)** Caso a opção **"Beneficiário com NIF"** esteja selecionada, preencha obrigatoriamente o campo **"Nro. do NIF – Número de Identificação Fiscal"**.

**(5)** Na aba **''Indetificação''** no campo **“Razão Social”** preencha a **razão social ou denominação completa do prestador de serviço**, exatamente conforme consta no cadastro oficial da empresa.

**(6)** Salve as alterações realizadas no cadastro do parceiro.

**(7)** Retorne ao documento fiscal e realize novamente a emissão da NF-e ou NFC-e.

**CAUSA**

A rejeição ocorre quando o documento fiscal eletrônico contém informações de um **prestador de serviço identificado com NIF** (Número de Identificação Fiscal do exterior), mas o **campo "Razão Social"** não foi preenchido no cadastro do parceiro. Conforme as regras de validação da SEFAZ estabelecidas pela **Lei Complementar nº 214/2025**, relacionada à Reforma Tributária, é **obrigatório informar o nome empresarial** quando o prestador for identificado com NIF, garantindo a correta identificação fiscal do prestador estrangeiro.
