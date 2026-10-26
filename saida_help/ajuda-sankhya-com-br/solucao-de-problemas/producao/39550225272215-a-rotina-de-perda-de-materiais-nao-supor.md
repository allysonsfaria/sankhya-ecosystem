---
id: "39550225272215"
titulo: "A rotina de perda de materiais não suporta explosão automática de lotes."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39550225272215-A-rotina-de-perda-de-materiais-n%C3%A3o-suporta-explos%C3%A3o-autom%C3%A1tica-de-lotes"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-09-08T17:18:48Z"
rotulos: ["Configuração", "Lote", "Estoque", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Artigo criado KCS", "Produção - KCS"]
---

# A rotina de perda de materiais não suporta explosão automática de lotes.

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/39550225259159) **MENSAGEM:**

[PROD\_E00609]: A rotina de perda de materiais não suporta explosão automática de lotes. Favor informar o lote da matéria prima para confirmar o apontamento.

**SITUAÇÃO:**

Ao realizar apontamentos em Operações de Produção (Produção >> Rotinas >> Operações de Produção) ou em Apontamento de Produção (Produção >> Rotinas >> Apontamento de Produção), o sistema apresenta a mensagem acima ao confirmar o apontamento que gera a nota de produção.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/39550209139095)SOLUÇÃO:**

É necessário **informar o lote da matéria-prima** na aba de Materiais ao lançar a perda, no campo **"Controle"**.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/39550225262487)CAUSA:**

O sistema, ao consumir matéria-prima, seleciona automaticamente os lotes mais próximos da validade. Em alguns casos, **mais de um lote pode ser utilizado**. Portanto, quando a perda é informada **sem o lote**, o sistema não consegue identificar de qual lote aquela perda deve ser baixada, consequentemente apresentando a mensagem de erro.
