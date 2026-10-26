---
id: "10084388681879"
titulo: "Não é possível realizar uma compensação utilizando títulos de uma NF-e/NFS-e ainda não aprovada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10084388681879-N%C3%A3o-%C3%A9-poss%C3%ADvel-realizar-uma-compensa%C3%A7%C3%A3o-utilizando-t%C3%ADtulos-de-uma-NF-e-NFS-e-ainda-n%C3%A3o-aprovada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:04:43Z"
rotulos: ["NF-e", "Movimentação Financeira", "SEFAZ", "Financeiro", "CORE_E05595", "NFS-e", "Mensagem: Não é possível compensar títulos de NF-e/NFS-e não aprovada.", "Causa: Tentativa de compensação com nota não aprovada.", "Solução: Garantir que a nota esteja aprovada pela SEFA antes da compensação.", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Não é possível realizar uma compensação utilizando títulos de uma NF-e/NFS-e ainda não aprovada

**MENSAGEM:**

[CORE\_E05595] Não é possível realizar uma compensação utilizando títulos de uma NF-e/NFS-e ainda não aprovada.

**SITUAÇÃO:**

Ao confirmar uma nota a mensagem é apresentada.

**CAUSA:**

Ocorre quando tenta realizar uma compensação envolvendo uma nota ainda não aprovada.

**SOLUÇÃO:**

Essa mensagem é uma validação, ela consiste em:
**\*** Ter um financeiro gerado a partir de uma nota ou devolução que 'ainda não foi aprovada', para efetuar a baixa desse pela movimentação financeira ou compensação financeira, a nota deverá estar APROVADA pela SEFAZ.

![Imagem 1: Essa mensagem é uma validação, ela consiste em: * Ter um financeiro gerado a partir de uma nota ou devolução que 'ainda…](https://ajuda.sankhya.com.br/hc/article_attachments/42084059549335)

###
