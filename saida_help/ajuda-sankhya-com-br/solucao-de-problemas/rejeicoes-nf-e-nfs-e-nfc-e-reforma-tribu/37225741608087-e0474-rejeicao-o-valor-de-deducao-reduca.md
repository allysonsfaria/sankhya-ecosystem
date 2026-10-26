---
id: "37225741608087"
titulo: "E0474 Rejeição: O valor de dedução/redução não pode ser superior ao valor dedutível/redutível."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225741608087-E0474-Rejei%C3%A7%C3%A3o-O-valor-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-n%C3%A3o-pode-ser-superior-ao-valor-dedut%C3%ADvel-redut%C3%ADvel"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:40Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "valor de dedução ou redução", "Limite máximo dedutível ou redutível", "Erro no cálculo automático", "Configuração incorreta", "Aplicação de percentuais de redução", "deduções e reduções", "Valor de dedução/redução não pode ser superior ao valor dedutível/redutível", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# E0474 Rejeição: O valor de dedução/redução não pode ser superior ao valor dedutível/redutível.

**MENSAGEM**

E0474 Rejeição: O valor de dedução/redução não pode ser superior ao valor dedutível/redutível.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) com informações de **dedução ou redução de base de cálculo** do IBS (Imposto sobre Bens e Serviços) ou CBS (Contribuição sobre Bens e Serviços), o usuário informou um **valor de dedução/redução superior ao valor máximo permitido** pela legislação. Isso ocorre quando o **valor informado excede o limite dedutível ou redutível** calculado para a operação, resultando na rejeição do documento pela SEFAZ.

**SOLUÇÃO**

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize o cadastro de alíquota utilizado no documento fiscal rejeitado.

**(3)** Verifique os campos relacionados a **deduções e reduções** da base de cálculo do IBS e CBS:

- Confira se o **valor de dedução informado** está dentro do limite permitido pela legislação.
- Certifique-se de que o **percentual de redução** aplicado não ultrapassa o valor dedutível/redutível calculado para a operação.
- Valide se as **configurações de CST (Código de Situação Tributária)** estão corretas e compatíveis com a operação realizada.

**(3)** Caso necessário, ajuste o **valor de dedução/redução** para que não exceda o limite máximo permitido, considerando:

- O **valor total da operação**.
- As **regras de tributação** aplicáveis ao produto ou serviço.
- Os **limites estabelecidos pela Lei Complementar nº 214/2025** e demais normas da Reforma Tributária.

**(4)** Revise o **cadastro do produto** na tela **"Produtos"** (INSERIR CAMINHO DA TELA) e confirme se as **informações tributárias** estão corretas e alinhadas com a alíquota cadastrada.

**(5)** Após realizar os ajustes necessários, **reemita o documento fiscal** para que seja validado pela SEFAZ sem a ocorrência da rejeição E0474.

**CAUSA**

A rejeição E0474 ocorre quando o **valor de dedução ou redução informado no documento fiscal** ultrapassa o **limite máximo dedutível ou redutível** estabelecido pela legislação tributária. Isso pode acontecer devido a:

- **Configuração incorreta** dos valores de dedução/redução no cadastro de alíquotas IBS e CBS;
- **Aplicação de percentuais de redução** incompatíveis com a base de cálculo da operação;
- **Erro no cálculo automático** do sistema ao processar as deduções permitidas;
- **Desconformidade com as regras** estabelecidas pela Lei Complementar nº 214/2025 e pela Reforma Tributária.
