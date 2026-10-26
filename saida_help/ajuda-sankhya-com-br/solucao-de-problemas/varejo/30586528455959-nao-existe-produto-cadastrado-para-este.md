---
id: "30586528455959"
titulo: "Não existe produto cadastrado para este código de barras"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30586528455959-N%C3%A3o-existe-produto-cadastrado-para-este-c%C3%B3digo-de-barras"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T14:35:35Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Impostos", "Sankhya Checkout", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Não existe produto cadastrado para este código de barras", "Erro"]
---

# Não existe produto cadastrado para este código de barras

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30586506818967) **MENSAGEM:**

Não existe produto cadastrado para este código de barras!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30586506819095)SOLUÇÃO:**

![Imagem 3: Verifique a informação que está preenchida no campo " EAN/GTIN Produto p/ NF-e ", aba "Impostos" da tela "Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/30591933676055) Verifique a informação que está preenchida no campo "**EAN/GTIN Produto p/ NF-e**", aba **"Impostos"** da tela **"Produtos (Cadastro)".** O sistema usa a informação deste campo para o código de barras.

![Imagem 4: Verifique a informação que está preenchida no campo " EAN/GTIN Produto p/ NF-e ", aba "Impostos" da tela "Produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/30586528453271)

(1)** Exemplo:** se a opção estiver definida como **"Referência"**, é necessário que o campo **"Referência"** na aba **"Geral"** do produto contenha a referência desejada.

![Imagem 5: Após realizar o ajuste acima, sincronize as configurações com o Sankhya Checkout .](https://ajuda.sankhya.com.br/hc/article_attachments/30591933679895)  Após realizar o ajuste acima, sincronize as configurações com o **Sankhya Checkout**.

Esse processo deve ser feito na tela "**Administração de Checkout"** (Configurações > Sankhya Checkout > Administração de Checkout). Depois, é preciso aguardar a sincronização para o **Sankhya Checkout**.

Quando a sincronização for concluída, um aviso será exibido no ícone correspondente. Para finalizar, selecione a opção **"Atualizar agora"** e a atualização dos dados será iniciada.

![Imagem 6: Quando a sincronização for concluída, um aviso será exibido no ícone correspondente. Para finalizar, selecione a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/30592035984407)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30586528453783)CAUSA:**

Mensagem ocorre quando não existe informações no campo próprio seguindo a configuração do campo EAN/GTIN Produto p/ NF-e no cadastro do produto.
