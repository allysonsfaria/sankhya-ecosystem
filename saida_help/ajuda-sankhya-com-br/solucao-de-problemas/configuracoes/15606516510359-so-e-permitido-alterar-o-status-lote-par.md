---
id: "15606516510359"
titulo: "Só é permitido alterar o status lote para 'Aguardando Aprovação' ou 'Quarentena'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15606516510359-S%C3%B3-%C3%A9-permitido-alterar-o-status-lote-para-Aguardando-Aprova%C3%A7%C3%A3o-ou-Quarentena"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:56:31Z"
rotulos: ["Produtos", "Configuração", "Controle de Qualidade", "TOP", "Estoque", "CORE_E04720", "Restrições na Alteração do Status do Lote"]
---

# Só é permitido alterar o status lote para 'Aguardando Aprovação' ou 'Quarentena'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17800388603927) MENSAGEM:**

[CORE\_E04720] Só é permitido alterar o status lote para 'Aguardando Aprovação' ou 'Quarentena'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17800378992023) SOLUÇÃO:**

Nesse caso o sistema vai exigir que seja feito o controle de qualidade, a TOP  tem que gerar amostra para lote.
Toda entrada de produto - nesse caso ajuste também - que são controlados por lote vão exigir o **[controle de qualidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596374-Controle-de-Qualidade-dos-Materiais).**

![Imagem 3: Nesse caso o sistema vai exigir que seja feito o controle de qualidade, a TOP tem que gerar amostra para lote. Toda…](https://ajuda.sankhya.com.br/hc/article_attachments/16982845062679)

Para produtos com a marcação 'Usa status do lote' da aba medidas e estoque o sistema sempre irá exigir o controle de qualidade nas entradas, seja ajuste, nota de compra, retorno de industrialização, etc.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17800388623255) CAUSA:**

Ocorre ao tentar alterar para Nenhum o campo 'Status Lote' na grade de itens da dentro das Centrais.
