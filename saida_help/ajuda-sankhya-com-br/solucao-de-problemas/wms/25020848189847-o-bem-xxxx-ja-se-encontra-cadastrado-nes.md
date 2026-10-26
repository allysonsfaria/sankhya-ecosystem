---
id: "25020848189847"
titulo: "O Bem 'XXXX' já se encontra cadastrado nesse produto, favor inserir com outro código"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25020848189847-O-Bem-XXXX-j%C3%A1-se-encontra-cadastrado-nesse-produto-favor-inserir-com-outro-c%C3%B3digo"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:46:17Z"
rotulos: ["Produtos", "Nota Fiscal", "Cadastro", "CORE_E06905", "O Bem 'XXXX' já se encontra cadastrado nesse produto", "Erro"]
---

# O Bem 'XXXX' já se encontra cadastrado nesse produto, favor inserir com outro código

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25020823863831) **MENSAGEM:**

[CORE\_E06905] O Bem 'XXXX' já se encontra cadastrado nesse produto, favor inserir com outro código

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25020848181271) **SOLUÇÃO:**

Existe uma relação PRODUTO X BEM, por meio da qual um mesmo código de BEM não pode se repetir dentro de cada PRODUTO, ou seja, um mesmo código de BEM não pode se repetir dentro de cada PRODUTO, só é possível repetir código de bem se for entre PRODUTOS diferentes.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25020848183575)**CAUSA:**

O erro é apresentado quando ao lançar uma nota de ativo se tenta adicionar ao produto um código de bem que já existe nesse PRODUTO.
