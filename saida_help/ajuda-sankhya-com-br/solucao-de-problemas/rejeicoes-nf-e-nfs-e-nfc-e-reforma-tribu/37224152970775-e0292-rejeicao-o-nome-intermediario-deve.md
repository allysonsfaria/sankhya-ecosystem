---
id: "37224152970775"
titulo: "E0292 Rejeição: O nome intermediário deve ser preenchido obrigatoriamente quando o NIF do intermediário for preenchido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224152970775-E0292-Rejei%C3%A7%C3%A3o-O-nome-intermedi%C3%A1rio-deve-ser-preenchido-obrigatoriamente-quando-o-NIF-do-intermedi%C3%A1rio-for-preenchido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:51Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Erro", "Lei Complementar nº 214/2025", "NIF (Número de Identificação Fiscal)", "NIF do Intermediador", "Nome do Intermediador", "Intermediador da operação"]
---

# E0292 Rejeição: O nome intermediário deve ser preenchido obrigatoriamente quando o NIF do intermediário for preenchido.

**MENSAGEM**

E0292 Rejeição: O nome intermediário deve ser preenchido obrigatoriamente quando o NIF do intermediário for preenchido.

**SITUAÇÃO**

Ao tentar emitir uma NF-e ou NFC-e que possui um **intermediador da operação** identificado com **NIF (Número de Identificação Fiscal)**, mas sem o preenchimento do campo **"Nome do Intermediador"**, o sistema retorna a rejeição E0292.

**SOLUÇÃO**

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do intermediador da operação.

**(3)** Na aba **"Identificação"**, verifique se o campo **"Identificação de Estrangeiro"** está preenchido com o **NIF** do intermediador.

**(4)** Certifique-se de que o campo **"Razão social"** do intermediador esteja **devidamente preenchido** com o nome completo ou razão social.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(5)** Retorne à nota fiscal e tente realizar a emissão novamente.

**CAUSA**

A rejeição E0292 ocorre devido à **validação da SEFAZ** que exige o preenchimento obrigatório do **nome do intermediador** quando o campo **"NIF do Intermediador"** estiver informado no documento fiscal. Esta validação garante a **identificação completa** do intermediador estrangeiro na operação, conforme as regras estabelecidas pela Reforma Tributária e pela Lei Complementar nº 214/2025.
