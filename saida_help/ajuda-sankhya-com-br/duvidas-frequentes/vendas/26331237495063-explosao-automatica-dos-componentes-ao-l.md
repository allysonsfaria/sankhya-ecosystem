---
id: "26331237495063"
titulo: "Explosão automática dos componentes ao lançar um kit não está sendo feita"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26331237495063-Explos%C3%A3o-autom%C3%A1tica-dos-componentes-ao-lan%C3%A7ar-um-kit-n%C3%A3o-est%C3%A1-sendo-feita"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:42:32Z"
rotulos: ["Produtos", "Configuração", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Explosão automática dos componentes ao lançar um kit não está sendo feita", "Erro"]
---

# Explosão automática dos componentes ao lançar um kit não está sendo feita

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26428983729047) **SITUAÇÃO:**

Ao lançar um produto kit não está acontecendo a explosão automática dos lotes, se lançar os componentes fora do kit,  acontece a explosão normalmente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26331176760343)SOLUÇÃO:**

A marcação na top **"Atualiza estoque MP"** deve estar como **"Reservar"** no caso de pedidos e **"Baixar"** no caso da nota.  Para marcar este campo, primeiro mude o campo **"Atualização do estoque"** para nenhum e o campo de Atualização Estoque MP será liberado, depois de preenchê-lo, volte no campo de Atualização do estoque e configure novamente.

![Imagem 3: A marcação na top "Atualiza estoque MP" deve estar como "Reservar" no caso de pedidos e "Baixar" no caso da nota. Para…](https://ajuda.sankhya.com.br/hc/article_attachments/26331237485079)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26331237485847)CAUSA:**

Esse problema ocorre porque para haver a explosão de lotes uma das regras é que o estoque precisa Reservar ou Baixar.
