---
id: "9034634432151"
titulo: "Não é possível inserir o produto sem informar o lote quando o parâmetro LOTAUTCENT estiver ligado e o grupo de produtos não estiver validando estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9034634432151-N%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-o-produto-sem-informar-o-lote-quando-o-par%C3%A2metro-LOTAUTCENT-estiver-ligado-e-o-grupo-de-produtos-n%C3%A3o-estiver-validando-estoque"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-16T14:19:39Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Estoque", "CORE_E01165", "Verificar lote/local no lançamento ou corrigir o grupo de produto", "Erro ao inserir produto sem lote informado", "NF-e sem lote/local ou grupo de produto sem validação de estoque", "Erro"]
---

# Não é possível inserir o produto sem informar o lote quando o parâmetro LOTAUTCENT estiver ligado e o grupo de produtos não estiver validando estoque

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16672473941271) MENSAGEM:**

[CORE\_E01165]: Não é possível inserir o produto sem informar o lote quando o parâmetro LOTAUTCENT estiver ligado e o grupo de produtos não estiver validando estoque.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672476520855) SITUAÇÃO:**

- Ao emitir NF-e a mensagem é apresentada;
- Ao iniciar a operação de produção.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16672473947671)SOLUÇÃO:**

![Imagem 4: Na emissão da nota, verifique se o local e o lote estão sendo informados no lançamento. Caso esses campos não estejam…](https://ajuda.sankhya.com.br/hc/article_attachments/16672473948439) Na emissão da nota, verifique se o local e o lote estão sendo informados no lançamento. Caso esses campos não estejam visíveis, inclua no layout, pela tela **"Configurador de layout da nota"**;

**OU**

![Imagem 5: Identifique o grupo de produto que não está fazendo a validação corretamente do estoque, analise o processo produtivo e…](https://ajuda.sankhya.com.br/hc/article_attachments/16672476527127) Identifique o grupo de produto que não está fazendo a validação corretamente do estoque, analise o processo produtivo e identifique a MP que está configurada com esse grupo de produto. Em seguida, corrija o grupo de produto.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16672473951639) CAUSA:**

Quando é lançada a NF-e sem informar lote e local, ou utilizar um grupo de produto que não está fazendo a validação corretamente do estoque.
