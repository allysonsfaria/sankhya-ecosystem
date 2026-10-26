---
id: "9320675816471"
titulo: "Matéria-prima com controle adicional de estoque não suportado: Código XXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9320675816471-Mat%C3%A9ria-prima-com-controle-adicional-de-estoque-n%C3%A3o-suportado-C%C3%B3digo-XXXX"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:08:43Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Manufatura", "PROD_E00017", "Controle adicional não suportado", "Produto com controle de validade gera erro", "Ajustar produto para controle por lote e ativar parâmetros necessários", "Erro"]
---

# Matéria-prima com controle adicional de estoque não suportado: Código XXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16702130250263) MENSAGEM:**

[PROD\_E00017]: Matéria-prima com controle adicional de estoque não suportado: XX Código XXXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16702103396375) SITUAÇÃO:**

Ao configurar a composição de produto e informar uma matéria prima que tenha controle adicional como data de validade a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16702103400983)SOLUÇÃO:**

![Imagem 4: O módulo Manufatura só trabalha com produtos com controle adicional, controlados por série, lista ou lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16702103405719) O módulo Manufatura só trabalha com produtos com controle adicional, controlados por série, lista ou lote.

![Imagem 5: Caso deseje utilizar data de validade nas matérias primas, o produto deve trabalhar com o tipo de controle igual a…](https://ajuda.sankhya.com.br/hc/article_attachments/16702103423127) Caso deseje utilizar data de validade nas matérias primas, o produto deve trabalhar com o tipo de controle igual a lote. Sendo assim, é necessário acesse o cadastro do **Produto** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), na aba **"Medidas e estoque"**, sub-aba **"Controle adicional"** e verifique se o campo "**Controlar por"** está definido como número de lote.

![Imagem 6: Caso deseje utilizar data de validade nas matérias primas, o produto deve trabalhar com o tipo de controle igual a…](https://ajuda.sankhya.com.br/hc/article_attachments/16702130285975)

![Imagem 7: Selecione também a marcação "Utiliza data de validade", juntamente com o parâmetro "LOTEDTVAL", habilitado na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16702103432855) Selecione também a marcação **"Utiliza data de validade",** juntamente com o parâmetro **"LOTEDTVAL",** habilitado na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências).

![Imagem 8: Selecione também a marcação "Utiliza data de validade", juntamente com o parâmetro "LOTEDTVAL", habilitado na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16702130298135)

![Imagem 9: Selecione também a marcação "Utiliza data de validade", juntamente com o parâmetro "LOTEDTVAL", habilitado na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/16702103444887)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16702130316055) CAUSA:**

Ao tentar informar um produto que trabalha com controle adicional diferente de Série, Lote ou Lista no cadastro do produto.
