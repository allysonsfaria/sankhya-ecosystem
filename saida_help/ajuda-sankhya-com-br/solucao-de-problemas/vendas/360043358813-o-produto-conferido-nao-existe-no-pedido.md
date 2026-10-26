---
id: "360043358813"
titulo: "O produto conferido não existe no pedido/nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358813-O-produto-conferido-n%C3%A3o-existe-no-pedido-nota"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-22T19:59:17Z"
rotulos: ["#criadoRoger", "CORE_E01288", "Produtos", "Conferência", "Estoque", "Cadastro", "Verifique código e código de barras", "Corrija cadastro e retorne à conferência", "Código do produto não encontrado", "Erro"]
---

# O produto conferido não existe no pedido/nota

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16108999449111) MENSAGEM:**

[CORE\_E01288] O produto conferido não existe no pedido/nota.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16109014787991) SITUAÇÃO:**

Ao realizar o processo de conferência através da rotina **“[Fila de Conferencia](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia)”**, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16108999460247) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Verifique se o código do produto que está sendo conferido está em conformidade com o código do produto inserido no…](https://ajuda.sankhya.com.br/hc/article_attachments/16109014794135) Verifique se o código do produto que está sendo conferido está em conformidade com o código do produto inserido no pedido ou nota.

![Imagem 5: Se o produto estiver correto, verifique na tela " Cadastro de Produtos " se o código de barras cadastrado no produto é…](https://ajuda.sankhya.com.br/hc/article_attachments/16108999464727) Se o produto estiver correto, verifique na tela **"[Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** se o código de barras cadastrado no produto é o mesmo registrado nos campos **“Referência”, "Cód. Barras"** (aba Código de Barras), **"Código de Barras"** (aba Unidade Alternativas) ou **"Cód. de Barras"** (aba Estoque).

![Imagem 6: Acesse a tela " Consulta de Produtos " , digite o código de barras e observe se será apresentado mais de um produto com…](https://ajuda.sankhya.com.br/hc/article_attachments/16109014797847) Acesse a tela **"[Consulta de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109353-Consulta-de-Produtos)"**, digite o código de barras e observe se será apresentado mais de um produto com o mesmo código de barras.

**(2)** Caso seja apresentado mais de um produto, verifique qual deles está com o código de barras informado incorretamente.

**(2)** Acesse o cadastro do produto com o código incorreto e corrija seu código de barras.

![Imagem 7: Finalizados os ajustes, retorne ao processo de conferência.](https://ajuda.sankhya.com.br/hc/article_attachments/16108999478679) Finalizados os ajustes, retorne ao processo de conferência.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16109014807703) CAUSA:**

Ocorre quando o sistema não localiza no cadastro de produtos o código e/ou código de barras informado.
