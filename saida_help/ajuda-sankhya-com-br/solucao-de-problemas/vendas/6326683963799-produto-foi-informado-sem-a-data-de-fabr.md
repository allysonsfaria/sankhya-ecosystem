---
id: "6326683963799"
titulo: "Produto foi informado sem a data de fabricação. Este dado será gerado no grupo de rastreamento do XML da NF-e conforme legislação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6326683963799-Produto-foi-informado-sem-a-data-de-fabrica%C3%A7%C3%A3o-Este-dado-ser%C3%A1-gerado-no-grupo-de-rastreamento-do-XML-da-NF-e-conforme-legisla%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:16:40Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "SEFAZ", "Estoque", "CORE_E01580", "Produto sem data de fabricação exigida por lei", "Informe a data de fabricação e validade se o produto exigir rastreamento", "Falta de data de fabricação para produtos com rastreamento configurado"]
---

# Produto foi informado sem a data de fabricação. Este dado será gerado no grupo de rastreamento do XML da NF-e conforme legislação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457145273239) MENSAGEM:**

[CORE\_E01580] Produto foi informado sem a data de fabricação. Este dado será gerado no grupo de rastreamento do XML da NF-e conforme legislação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457145280407) SOLUÇÃO:**

![Imagem 3: Caso o produto esteja configurado para ter o rastreamento de lote, conforme configurações detalhadas abaixo, será…](https://ajuda.sankhya.com.br/hc/article_attachments/16457128886679) Caso o produto esteja configurado para ter o rastreamento de lote, conforme configurações detalhadas abaixo, **será obrigatório informar a data de fabricação** e também a data de validade para transmitir essas informações para Sefaz. Essa informação se torna obrigatória independente das movimentações realizada na TOP (gerar estoque ou não).

**(1)** Tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)

**(1)** Aba **"Geral"**

**(1)** Campo: **"Tem rastro de lote"**

Verifique se a configuração acima está correta, caso contrário realize os devidos ajustes e refaça o faturamento.

**Observação:** Caso o rastreio seja necessário, mantenha a marcação citada no item 1 e informe a data de fabricação no lançamento.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457128896919)CAUSA:**

Caso o produto esteja configurado para ter o rastreamento e não for informada data de fabricação, a mensagem será apresentada.
