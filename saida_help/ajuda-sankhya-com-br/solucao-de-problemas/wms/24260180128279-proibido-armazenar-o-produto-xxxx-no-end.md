---
id: "24260180128279"
titulo: "Proibido armazenar o produto XXXX no endereço YYYY"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24260180128279-Proibido-armazenar-o-produto-XXXX-no-endere%C3%A7o-YYYY"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:47:08Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "WMS_E00833", "Armazenamento proibido", "Endereço não vinculado ao produto/grupo", "Validar endereço e configurar como \"Permitir\" ou \"Exclusivo\"", "Squad WMS"]
---

# Proibido armazenar o produto XXXX no endereço YYYY

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24260232841751) **MENSAGEM:**

[WMS\_E00833] Proibido armazenar o produto XXXX no endereço YYYY

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24260180109975)**SOLUÇÃO:**

Validar se o **"[Endereço de armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313)"** de destino apresentando na mensagem esta configurado atraves da aba Produto como **"Permitir" ou "Exclusivo"**, ou na aba Grupo de Produtos como **"Permitir",** caso esteja, é nessario incluir o produto ou o grupo de produto vinculado ao endereço apresentado. Pois, com a marcação deferente de **"Proibir"** fica estabelecido que naquele endereço deverá ser permitido apenas os produtos ou grupos cadastrados.

![Imagem 3: Validar se o " Endereço de armazenamento " de destino apresentando na mensagem esta configurado atraves da aba Produto…](https://ajuda.sankhya.com.br/hc/article_attachments/24511858181911)

![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24260232848535)**CAUSA:**

A mensagem é apresentada ao realizar movimentação de um produto para um endereço de armazenagem sem vinculo com o produto ou grupo de produto.
