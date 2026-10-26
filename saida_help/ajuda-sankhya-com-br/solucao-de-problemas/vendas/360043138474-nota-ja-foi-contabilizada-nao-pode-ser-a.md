---
id: "360043138474"
titulo: "Nota já foi contabilizada, não pode ser alterada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043138474-Nota-j%C3%A1-foi-contabilizada-n%C3%A3o-pode-ser-alterada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-28T12:10:17Z"
rotulos: ["NF-e", "Movimentação Financeira", "Contabilização", "Financeiro", "ORA-20101", "Solução: Abrir lote excluir lançamento e alterar nota", "Nota já contabilizada não pode ser alterada", "Ocorre ao tentar criar ou alterar nota confirmada", "Erro"]
---

# Nota já foi contabilizada, não pode ser alterada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16145323247767) MENSAGEM:**

ORA-20101: Nota já foi contabilizada, não pode ser alterada.
ORA-06512: em "SANKHYA.TRG\_UPT\_TGFITE", line 705
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_UPT\_TGFITE'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145323252759) SITUAÇÃO:**

Ao tentar criar uma Nota de Devolução de Venda/Compra, a partir de uma Nota de Venda/Compra, ou alteração em Notas já confirmada, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16145323254807) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Contabilidade » Arquivos » Lançamentos contábeis](https://ajuda.sankhya.com.br/hc/article_attachments/16145307153943) Acesse: Contabilidade » Arquivos » Lançamentos contábeis

- Nesta tela faça uma pesquisa utilizando os filtros, de modo que encontre o documento.
- Se o LOTE já estiver fechado ao clicar em 'Editar Lançamento', ocorrerá o aviso: **Apenas lotes abertos podem receber lançamento contábil manual. O lote não está aberto, deseja reabri-lo?**
- Com o aval da Equipe de Contabilidade, pode ser aberto o Lote, clicando em SIM. Ou acessar a tela 'Contabilidade » Arquivos » Lotes Contábeis' e abrir o Lote do documento que precisa ser alterado.
- Ao clicar em 'Editar Lançamento', será possível acessar o documento contabilizado e exclui-lo, clicando no botão "**Excluir[F9]".**
- Após essa exclusão é possível alterar o documento e posteriormente a equipe Contábil, precisará contabilizar novamente o documento.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17875787364119) IMPORTANTE:**

Lembrando que, caso esta alteração esteja sendo feita em uma nota muito antiga, é necessário o acompanhamento da equipe Fiscal/Contábil da empresa para que não implique em alterações nos valores contabilizados e se realmente a equipe Fiscal/Contábil concorda em excluir o documento.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16145307161879) CAUSA:**

Ocorre quando um documento já contabilizado precisa ser alterado em sua raiz(Nota).

Esta validação também pode ocorrer em Títulos Financeiros, Movimentos Bancários, dentre outros, que de acordo com o processo da empresa, precisa ser contabilizado.
