---
id: "360051731454"
titulo: "Títulos Renegociados não podem ter Receita/Despesa ou Provisão ou Valor do Desdobramento alterados."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051731454-T%C3%ADtulos-Renegociados-n%C3%A3o-podem-ter-Receita-Despesa-ou-Provis%C3%A3o-ou-Valor-do-Desdobramento-alterados"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:29:49Z"
rotulos: ["Movimentação Financeira", "Financeiro", "Renegociação", "CORE_E02408", "Títulos renegociados não podem ter valores alterados.", "Acesse \"Renegociação de Títulos\" e clique em \"Desfazer\" para reverter.", "Desfaça a renegociação para modificar receita/despesa ou provisão.", "Erro"]
---

# Títulos Renegociados não podem ter Receita/Despesa ou Provisão ou Valor do Desdobramento alterados.

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18864606568727) MENSAGEM**:

[CORE\_E02408] Títulos Renegociados não podem ter Receita/Despesa ou Provisão ou Valor do Desdobramento alterados.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18864606586007) SOLUÇÃO:**

- As alterações desejadas serão permitidas somente após desfazer a renegociação vinculada a tal título.
- Cabe analisar os motivos pelos quais essa alteração será realizada. (Lembre-se que caso sejam ajustes de valores, no momento da baixa temos os campos "desconto e/ou juros").

Caso deseje desfazer a renegociação, seguem as orientações:

![Imagem 3: Para o título que deseja desfazer a renegociação, busque na movimentação financeira o campo 'Nro Renegociação '.](https://ajuda.sankhya.com.br/hc/article_attachments/18864606602391) Para o título que deseja desfazer a renegociação, busque na movimentação financeira o campo **'Nro Renegociação'.**

![Imagem 4: Para o título que deseja desfazer a renegociação, busque na movimentação financeira o campo 'Nro Renegociação '.](https://ajuda.sankhya.com.br/hc/article_attachments/15935821040919)

![Imagem 5: Acesse a tela 'Renegociação de títulos' (Financeiro » Rotinas) , no filtro do lado direito "Renegociação", digite o…](https://ajuda.sankhya.com.br/hc/article_attachments/18864630997655) Acesse a tela 'Renegociação de títulos' (Financeiro » Rotinas), no filtro do lado direito "Renegociação", digite o 'Nro Renegociação' localizado no Item 1.

![Imagem 6: Na parte inferior serão apresentados os dados da renegociação gerada, basta clicar na opção DESFAZER .](https://ajuda.sankhya.com.br/hc/article_attachments/18864631020567) Na parte inferior serão apresentados os dados da renegociação gerada, basta clicar na opção **DESFAZER**.

![Imagem 7: Feito isso o título voltará a apresentar as informações originais, que antecederam sua renegociação, e não mais…](https://ajuda.sankhya.com.br/hc/article_attachments/18864631035799) Feito isso o título voltará a apresentar as informações originais, que antecederam sua renegociação,  e não mais impedirá as alterações.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15935867710743) CAUSA:**

Bloqueio inserido ao tentar alterar informações de títulos renegociados, sem que a renegociação tenha sido desfeita. Esse comportamento do sistema é para manter a integridade dos valores com vinculo no titulo original.
