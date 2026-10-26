---
id: "360044226753"
titulo: "Marca deve ser informada, ao salvar Tarifas CIP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044226753-Marca-deve-ser-informada-ao-salvar-Tarifas-CIP"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T16:00:00Z"
rotulos: ["Produtos", "Configuração", "Preferências", "Financeiro", "Ativar parâmetro CFPSMARCAREFREP", "Marca deve ser informada", "Falta de Marca/Referência no produto", "Tarifa CIP"]
---

# Marca deve ser informada, ao salvar Tarifas CIP

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16418213869335) MENSAGEM:**

Marca deve ser informada

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418228568855) SITUAÇÃO:**

Ao tentar relacionar uma Tarifa CIP na aba **Tarifas** da tela **"[Filtro para cálculo CIP (Financeiros)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118873)"**, ocorre a mensagem:

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418228572183) SOLUÇÃO:**

![Imagem 4: Acesse Configurações » Avançado » Preferências e ligue o parâmetro "CFPSMARCAREFREP - Uso interno tela Produto/Serviço"](https://ajuda.sankhya.com.br/hc/article_attachments/16418228574743) Acesse Configurações » Avançado » Preferências e ligue o parâmetro **"CFPSMARCAREFREP - Uso interno tela Produto/Serviço"**

![Imagem 5: Acesse Cadastros » Filtro para cálculo CIP (Financeiros) , inclua a tarifa e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/16418213881495) Acesse Cadastros » Filtro para cálculo CIP (Financeiros), inclua a tarifa e salve.

Ao ligar o parâmetro o sistema não faz a validação de referência do produto e é possível salvar a inclusão da tarifa CIP.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16418213886231) CAUSA:**

Quando o produto, vinculado ao Grupo de Produto/Serviço, não possui informações de Marca/Referencia em seu cadastro e com o parâmetro desligado, o sistema valida esta informação no cadastro do produto.
