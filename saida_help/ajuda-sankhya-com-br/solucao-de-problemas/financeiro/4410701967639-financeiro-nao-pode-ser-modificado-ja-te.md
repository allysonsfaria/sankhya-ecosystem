---
id: "4410701967639"
titulo: "Financeiro não pode ser modificado. Já tem provisão baixada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410701967639-Financeiro-n%C3%A3o-pode-ser-modificado-J%C3%A1-tem-provis%C3%A3o-baixada"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:21:14Z"
rotulos: ["Configuração", "Movimentação Financeira", "TOP", "Financeiro", "#validadoSilvio", "CORE_E02787", "CORE_E03481", "Comportamento nativo do sistema", "Faturamento parcial/total baixa provisão cria novo título real", "Financeiro não pode modificar provisão baixada", "Erro"]
---

# Financeiro não pode ser modificado. Já tem provisão baixada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16121402739863) MENSAGEM:**

[CORE\_E02787] Financeiro não pode ser modificado. Já tem provisão baixada.

[CORE\_E03481] Financeiro não pode ser modificado. Já tem provisão baixada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16121377091095) SOLUÇÃO:**

É um comportamento nativo do sistema.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16121402744471) CAUSA:**

Os pedidos de ''compra' ou 'Venda'' geralmente são configurados para atualizar o financeiro de forma **''provisionada'',** se assim estiver na TOP.  Quando se realiza o faturamento parcial ou integral deste pedido, sua **''provisão financeira''** é baixada (parcial ou total) e um novo titulo 'REAL' é incluído na movimentação financeira.

Ao tentar realizar alguma modificação em campos que podem interferir no financeiro dos Pedidos que já foram faturados, a mensagem de **aviso** é apresentada.

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16121377101591) OBSERVAÇÃO:**

Campos adicionais não entram nesta regra.
