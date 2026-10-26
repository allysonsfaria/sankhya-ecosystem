---
id: "26276713998487"
titulo: "Quantidade de séries MP não pode ser menor do que a quantidade apontada da matéria-prima: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26276713998487-Quantidade-de-s%C3%A9ries-MP-n%C3%A3o-pode-ser-menor-do-que-a-quantidade-apontada-da-mat%C3%A9ria-prima-X"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:42:54Z"
rotulos: ["Produtos", "Apontamento", "Estoque", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "PROD_E00246", "Quantidade de séries MP não pode ser menor", "quantidade apontada da matéria-prima:", "Erro"]
---

# Quantidade de séries MP não pode ser menor do que a quantidade apontada da matéria-prima: 'X'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26276737082647) **MENSAGEM:**

[PROD\_E00246] Quantidade de séries MP não pode ser menor do que a quantidade apontada da matéria-prima: X - 'PRODUTO X'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26276713970199)SOLUÇÃO:**

Acesse a tela **"Operações de produção"** (Caminho: Produção » Rotinas » Operações de Produção), vá até a aba **"Apontamentos"**, depois na sub-aba **"Itens"**, sub-aba **"Materiais"** e no botão **"Nro Série"** inclua a quantidade de séries das MPs que serão consumidas no apontamento do PA.

[GIF animado: Imagem 3: Acesse a tela "Operações de produção" (Caminho: Produção » Rotinas » Operações de Produção) , vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/26276713973527)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26276737091735)CAUSA:**

Ao confirmar um apontamento que utiliza MP controlada por série, sem definir as séries na mesma quantidade que serão consumidas na atividade, a mensagem é apresentada.
