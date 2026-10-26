---
id: "37223104463511"
titulo: "E0266 Rejeição: CPF do intermediário informado na DPS é inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223104463511-E0266-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:02Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Erro", "Declaração de Prestação de Serviços (DPS)", "NF-e ou NFC-e", "CPF do intermediário", "CPF informado na DPS", "CPF do intermediário informado é inválido", "Sequência numérica incorreta dígitos verificadores inválidos"]
---

# E0266 Rejeição: CPF do intermediário informado na DPS é inválido.

**MENSAGEM**

E0266 Rejeição: CPF do intermediário informado na DPS é inválido.

**SITUAÇÃO**

Ao transmitir uma **NF-e** ou **NFC-e** contendo informações de intermediário da operação na **Declaração de Prestação de Serviços (DPS)**, o sistema retorna a rejeição informando que o **CPF do intermediário** está inválido. Esta situação ocorre durante o processo de autorização do documento fiscal junto à SEFAZ.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do **intermediário** informado na operação.

**(3)** Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"** e verifique se o **CPF informado** está correto e válido.

**(4)** Certifique-se de que o CPF possui **11 dígitos**, sem pontos, traços ou espaços em branco, e que o **dígito verificador** (últimos dois números) está correto.

**(5)** Caso o CPF esteja incorreto ou inválido, corrija a informação inserindo um **CPF válido** na Receita Federal do Brasil.

**(6)** Salve as alterações realizadas no cadastro do parceiro.

**(7)** Retorne ao documento fiscal e redigite as informações do **cabeçalho da nota**, incluindo os dados da **empresa** e do **intermediário**, para que o sistema recalcule os dados corretamente.

**(8)** Gere um novo lote e transmita novamente a **NF-e** ou **NFC-e** para a SEFAZ. 

**OBSERVAÇÃO:** Caso o problema persista após as correções, inutilize a numeração do documento, exclua a nota e gere uma nova NF-e ou NFC-e com as informações corretas.

**CAUSA**

A rejeição ocorre quando o **CPF do intermediário** informado na **Declaração de Prestação de Serviços (DPS)** está inválido, seja por conter **sequência numérica incorreta**, **dígitos verificadores inválidos**, ou por estar preenchido apenas com zeros. A SEFAZ valida o CPF informado e, caso não esteja em conformidade com as regras da Receita Federal, retorna a rejeição E0266.
