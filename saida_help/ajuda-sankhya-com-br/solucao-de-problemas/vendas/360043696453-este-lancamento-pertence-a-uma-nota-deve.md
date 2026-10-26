---
id: "360043696453"
titulo: "Este lançamento pertence a uma nota. Deve ser excluído pela Central"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696453-Este-lan%C3%A7amento-pertence-a-uma-nota-Deve-ser-exclu%C3%ADdo-pela-Central"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:22Z"
rotulos: ["#criadoRoger", "CORE_E02385", "Central de Vendas", "Movimentação Financeira", "Estoque", "Financeiro", "Excluir na Central de Vendas/Compras após cancelar a nota correspondente", "Lançamento ligado a uma nota", "Tentativa de exclusão na Movimentação Financeira", "Erro", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Este lançamento pertence a uma nota. Deve ser excluído pela Central

**MENSAGEM:**

[CORE\_E02385] Este lançamento pertence a uma nota. Deve ser excluído pela Central.

**SOLUÇÃO:**

**(1)** Não é permitido excluir um financeiro que foi originado através de um lançamento na Central de Vendas/Compras.

**(2)** A exclusão do financeiro só será permitida diante exclusão/cancelamento do documento/nota que o originou. Dessa forma, localize no **"Portal de Compras/Vendas"** o número nota correspondente e analise o procedimento mais adequado (Cancelamento/Exclusão/Devolução).

![Imagem 1: (2) A exclusão do financeiro só será permitida diante exclusão/cancelamento do documento/nota que o originou. Dessa…](https://ajuda.sankhya.com.br/hc/article_attachments/14712962793495)

**CAUSA:**

Ocorre quando ao tentar excluir pela **"Movimentação Financeira"** títulos com ORIGEM = Estoque.
