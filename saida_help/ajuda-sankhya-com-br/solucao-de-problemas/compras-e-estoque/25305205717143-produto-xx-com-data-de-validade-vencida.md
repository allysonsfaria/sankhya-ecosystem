---
id: "25305205717143"
titulo: "Produto XX com data de validade vencida para o Lote YY"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25305205717143-Produto-XX-com-data-de-validade-vencida-para-o-Lote-YY"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:45:58Z"
rotulos: ["Produto", "NF-e", "TOP", "Estoque", "CORE_E01935", "Produto XX vencido no Lote YY", "Verificar se ajuste gera nota fiscal.", "Ajuste estoque do lote com data errada", "Erro"]
---

# Produto XX com data de validade vencida para o Lote YY

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25305212020759) MENSAGEM:**

[CORE\_E01935] Produto XX com data de validade vencida para o Lote YY

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25305212022423)SOLUÇÃO:**

Acesse a tela **"Produto"**, busque pelo produto que está dando erro. Vá até a aba **"Estoque"** e verifique se existe **mais de uma linha de estoque de um mesmo lote, com diferentes datas de validade,**  para a mesma Empresa, Controle e Local.

![Imagem 3: Acesse a tela "Produto" , busque pelo produto que está dando erro. Vá até a aba "Estoque" e verifique se existe mais de…](https://ajuda.sankhya.com.br/hc/article_attachments/25305212023447)

**Caso exista, usando uma TOP de Ajuste de estoque, faça o ajuste do estoque que apresenta a data de validade errada, pois um mesmo lote só pode ter uma data de validade.**

**Importante:** antes de fazer o ajuste de estoque, acesse a TOP de ajuste, vá até a aba **"NF-e/NFC-e/CF-e"**e observe no campo **"NF-e"** se a TOP gera ou não gera nota fiscal. Assim, ajuste a TOP de acordo com a definição contábil da empresa, seja ela gerar ou não gerar nota fiscal em movimentações de ajuste de estoque.

![Imagem 4: Importante: antes de fazer o ajuste de estoque, acesse a TOP de ajuste, vá até a aba "NF-e/NFC-e/CF-e" e observe no…](https://ajuda.sankhya.com.br/hc/article_attachments/25305212026647)

![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25305212029207) **CAUSA:**

A mensagem é apresentada quando existe mais um linha de estoque, com diferentes datas de validade, para a mesma empresa, controle e local.
