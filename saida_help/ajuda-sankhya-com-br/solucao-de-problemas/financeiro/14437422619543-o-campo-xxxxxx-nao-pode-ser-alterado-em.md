---
id: "14437422619543"
titulo: "O campo \"xxxxxx\" não pode ser alterado em títulos baixados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14437422619543-O-campo-xxxxxx-n%C3%A3o-pode-ser-alterado-em-t%C3%ADtulos-baixados"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-10-07T12:28:15Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "CORE_E02411", "Campos não alteráveis em títulos baixados", "Estornar título para editar campos", "Excluir pedido com faturamento parcial manualmente", "Erro"]
---

# O campo "xxxxxx" não pode ser alterado em títulos baixados

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16859518231063) MENSAGEM:**

[CORE\_E02411]: O campo "xxxxx" não pode ser alterado em títulos baixados!

### Na tela movimentação financeira

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859503184407)SOLUÇÃO:**

Acesse o título em questão, na **"Movimentação financeira"** (Financeiro » Rotinas » Movimentação Financeira) e faça o estorno do mesmo, caso deseje alterar algum campo.

![Imagem 3: Acesse o título em questão, na "Movimentação financeira" (Financeiro » Rotinas » Movimentação Financeira) e faça o…](https://ajuda.sankhya.com.br/hc/article_attachments/14437543822615)

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859503185303) OBSERVAÇÃO:**

Só é possível alterar alguns campos no lançamento se este for de origem financeira, ou seja, lançado direto na tela Movimentação financeira.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16859518237975)CAUSA:**

Ocorre ao tentar alterar o campo Empresa na movimentação financeira em títulos já baixados.

### Na tela pedidos de compra

**![Imagem 6: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859503184407) SOLUÇÃO:**

Como se trata de um comportamento do sistema, para solucionar o erro coloque manualmente o pedido como não pendente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16859518237975)CAUSA:**

Está ocorrendo o presente aviso quando se tenta excluir um pedido que teve por origem um faturamento parcial, pois o mesmo já está em processo de faturamento.
