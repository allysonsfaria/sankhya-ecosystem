---
id: "18880283321239"
titulo: "Propriedade 'EventoMDF.NRORECIBO' com largura acima do limite: (15 > 1)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18880283321239-Propriedade-EventoMDF-NRORECIBO-com-largura-acima-do-limite-15-1"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:52:01Z"
rotulos: ["ERROMDFE", "MDF-e", "Configuração", "XML", "DBExplorer", "Limite Excedido para 'EventoMDF.NRORECIBO'"]
---

# Propriedade 'EventoMDF.NRORECIBO' com largura acima do limite: (15 > 1)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18880283298711) **MENSAGEM:**

Propriedade 'EventoMDF.NRORECIBO' com largura acima do limite: (15 > 1).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18880290803351)CAUSA:**

Quando há divergência entre as tabelas.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18880254764567)SOLUÇÃO:**

Acesse a tela **DBExplorer** (Configurações » Avançado » DBExplorer) e busque pelas tabelas TGFMDFE e TGFEMDF, observando o campo NRORECIBO.

![Imagem 4: Acesse a tela DBExplorer (Configurações » Avançado » DBExplorer) e busque pelas tabelas TGFMDFE e TGFEMDF, observando o…](https://ajuda.sankhya.com.br/hc/article_attachments/19056619078935)

![Imagem 5: Acesse a tela DBExplorer (Configurações » Avançado » DBExplorer) e busque pelas tabelas TGFMDFE e TGFEMDF, observando o…](https://ajuda.sankhya.com.br/hc/article_attachments/19056619090199)

No exemplo acima na TGFMDFE o campo NRORECIBO está com tamanho de 15 e na TGFEMDF esta como 1. Para correção, ajuste os campos de maneira que fiquem iguais (com 15).
