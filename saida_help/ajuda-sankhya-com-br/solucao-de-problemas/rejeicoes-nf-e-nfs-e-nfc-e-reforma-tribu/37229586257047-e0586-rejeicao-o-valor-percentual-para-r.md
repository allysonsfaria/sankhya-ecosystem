---
id: "37229586257047"
titulo: "E0586 Rejeição: O valor percentual para redução da base de cálculo deve ser maior que 0 e menor ou igual ao percentual parametrizado pelo município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229586257047-E0586-Rejei%C3%A7%C3%A3o-O-valor-percentual-para-redu%C3%A7%C3%A3o-da-base-de-c%C3%A1lculo-deve-ser-maior-que-0-e-menor-ou-igual-ao-percentual-parametrizado-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:50Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "NFS-e com redução", "percentual de redução inválido", "edução da base de cálculo do ISSQN", "redução da base de cálculo do ISSQN", "Redução e Deferimentos", "limites estabelecidos pelo município"]
---

# E0586 Rejeição: O valor percentual para redução da base de cálculo deve ser maior que 0 e menor ou igual ao percentual parametrizado pelo município de incidência do ISSQN.

**MENSAGEM:**

E0586 Rejeição: O valor percentual para redução da base de cálculo deve ser maior que 0 e menor ou igual ao percentual parametrizado pelo município de incidência do ISSQN.

**SITUAÇÃO:**

Ao emitir uma NFS-e com redução da base de cálculo do ISSQN, a nota foi rejeitada. O sistema indicou que o percentual de redução informado está inválido.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Aliquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS).

**(2)** Localize a alíquota utilizada no documento fiscal rejeitado.

**(3)** Verifique a seção **''Redução e Deferimentos''** está configurado para o ISSQN, e certifique-se de que:

- O valor seja **maior que zero (0)**;
- O valor seja **menor ou igual ao percentual máximo** permitido pelo município de incidência do ISSQN.

**(3)** Verifique a legislação municipal ou entre em contato com a prefeitura do município de incidência para confirmar o **percentual máximo de redução da base de cálculo** permitido para o serviço prestado.

**(4)** Ajuste o campo **''% Redução Alíquota (Gov.)''**, informando um valor **válido conforme os limites estabelecidos pelo município**.

**(5)** Salve as alterações.

**(6)** Retorne ao documento fiscal rejeitado e tente emitir novamente, garantindo que o percentual de redução esteja correto.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida se o percentual de redução da base de cálculo do ISSQN** informado no documento fiscal está dentro dos **limites estabelecidos pelo município** de incidência do serviço. Quando o percentual configurado é **igual a zero ou ultrapassa o limite máximo** permitido pela legislação municipal, o documento é rejeitado para garantir a conformidade fiscal e evitar inconsistências no recolhimento do imposto.
