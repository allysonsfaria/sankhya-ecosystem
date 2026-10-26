---
id: "30916411553431"
titulo: "Tipo de Controle 'Herdar do PA' inválido. Produto ' ' não possui Controle Adicional controlado por Lista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30916411553431-Tipo-de-Controle-Herdar-do-PA-inv%C3%A1lido-Produto-n%C3%A3o-possui-Controle-Adicional-controlado-por-Lista"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:34:23Z"
rotulos: ["Produtos", "Configuração", "controle adicional", "TOP", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Tipo de Controle 'Herdar do PA' inválido", "PROD_E00169", "não possui Controle Adicional controlado por Lista", "lista", "literal", "Herdar do PA", "Erro"]
---

# Tipo de Controle 'Herdar do PA' inválido. Produto ' ' não possui Controle Adicional controlado por Lista

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30916422256023) **MENSAGEM:**

[PROD\_E00169]  Tipo de Controle 'Herdar do PA' inválido. Produto ' ' não possui Controle Adicional controlado por Lista.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30916422256919)SOLUÇÃO:**

![Imagem 3: Acesse a tela "Produtos" (Configurações » Cadastros » Produtos » Produtos) , na aba "Medidas e Estoque" , sub aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32610745057431) Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), na aba **"Medidas e Estoque"**, sub aba **"Controle Adicional",** verifique se o tipo de controle do PA, no campo **"Controlado Por", é diferente de "Lista".**

![Imagem 4: Caso seja, em seguida, acesse a tela "Composição do produto" (Produção » Cadastros » Composição do Produto) , aba…](https://ajuda.sankhya.com.br/hc/article_attachments/32610745058327) Caso seja, em seguida, acesse a tela **"Composição do produto"** (Produção » Cadastros » Composição do Produto), aba **"Sub-Produtos"**, no campo **"Tipo de controle"** selecione a opção**"Literal".**Pois, o tipo de controle do Subproduto **"Herdar do PA"** só pode ser usado quando o produto é controlado por Lista.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30916411537047)CAUSA:**

Ocorre quando tentamos utilizar o tipo de controle do Sub-Produto para Herdar do PA e o Produto Acabado não é controlado por Lista.
