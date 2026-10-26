---
id: "37225302557719"
titulo: "E0439 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o benefício municipal informado na DPS for do tipo \"Isenção\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225302557719-E0439-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-o-preenchimento-dos-campos-do-grupo-de-informa%C3%A7%C3%B5es-relativas-%C3%A0-Dedu%C3%A7%C3%A3o-Redu%C3%A7%C3%A3o-do-ISSQN-quando-o-benef%C3%ADcio-municipal-informado-na-DPS-for-do-tipo-Isen%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:03Z"
rotulos: ["Configuração", "SEFAZ", "Financeiro", "NFS-e", "ISSQN", "NFS-e (Nota Fiscal de Serviço Eletrônica)", "Grupo de Dedução/Redução do ISSQN", "Benefício municipal do tipo \"Isenção\"", "Consistência das informações fiscais"]
---

# E0439 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o benefício municipal informado na DPS for do tipo "Isenção".

**MENSAGEM**

E0439 Rejeição: Não é permitido o preenchimento dos campos do grupo de informações relativas à Dedução/Redução do ISSQN, quando o benefício municipal informado na DPS for do tipo "Isenção".

**SITUAÇÃO**

Ao emitir uma NFS-e (Nota Fiscal de Serviço Eletrônica), o usuário configurou na DPS (Declaração de Prestação de Serviços) um **benefício municipal do tipo "Isenção"** e, simultaneamente, preencheu campos relacionados ao **grupo de Dedução/Redução do ISSQN**. Essa combinação viola as regras de validação da Sefaz, resultando na rejeição da nota fiscal com a mensagem E0439.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Localize o tipo de operação utilizado no documento fiscal rejeitado.

**(3)** Navegue até a aba **"NFS-e"** e verifique as configurações relacionadas ao ISSQN.

**(4)** No campo **“Cód. Natureza Oper. ISS (NFS-e)”**, verifique se está configurado com a opção **“3 – Isenção”**.

- Essa configuração indica que o **benefício municipal aplicado é do tipo isenção**.

**(5)** Verifique se há preenchimento nos campos relacionados a **deduções ou reduções do ISSQN**, tais como:

- **"Valor de Dedução"**
- **"Indicador de Dedução"**
- **"Valor Deduções"**
- **"Desconto Condicionado para NFS-e"**

**(6)** Caso existam valores preenchidos nos campos de **dedução ou redução do ISSQN** e o benefício municipal esteja configurado como **“3 – Isenção”**, realize uma das seguintes ações:

- **Remova os valores** dos campos de dedução/redução do ISSQN, mantendo apenas a configuração de **isenção**
- **Altere o tipo de benefício municipal** no campo **“Cód. Natureza Oper. ISS (NFS-e)”** para uma opção diferente de **“3 – Isenção”**, caso a operação realmente envolva **deduções ou reduções**.

**(7)** Salve as alterações.

**(8)** Retorne ao documento fiscal rejeitado e realize uma nova tentativa de emissão da NFS-e.

**CAUSA**

A rejeição ocorre porque a **Sefaz não permite** que sejam informados simultaneamente um **benefício municipal do tipo "Isenção"** e valores no **grupo de Dedução/Redução do ISSQN**. Quando uma operação é classificada como isenta, não há base de cálculo sobre a qual aplicar deduções ou reduções, tornando o preenchimento desses campos incompatível com a natureza da operação. A validação visa garantir a **consistência das informações fiscais** enviadas no XML da NFS-e, evitando contradições entre o tipo de benefício declarado e os valores tributários informados.
