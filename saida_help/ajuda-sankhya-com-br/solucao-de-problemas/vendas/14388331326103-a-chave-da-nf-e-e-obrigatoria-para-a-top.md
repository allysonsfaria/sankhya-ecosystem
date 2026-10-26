---
id: "14388331326103"
titulo: "A chave da NF-e é obrigatória para a TOP XXXX "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14388331326103-A-chave-da-NF-e-%C3%A9-obrigat%C3%B3ria-para-a-TOP-XXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:49Z"
rotulos: ["Configuração", "Fiscal", "Tipo de Operação", "NF-e", "TOP", "CORE_E02962", "Chave da NF-e", "Erro"]
---

# A chave da NF-e é obrigatória para a TOP XXXX 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16860080853655) MENSAGEM:**

[CORE\_E02962]: A chave da NF-e é obrigatória para a TOP XXXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16860097374103)SOLUÇÃO:**

Verifique a configuração do campo **"Buscar NF de origem p/ referenciar na NFe"**no cadastro do [Tipo de Operação,](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) caso esteja marcado e a chave da nota de origem não for informada, a mensagem será apresentada.

![Imagem 3: Verifique a configuração do campo "Buscar NF de origem p/ referenciar na NFe" no cadastro do Tipo de Operação, caso…](https://ajuda.sankhya.com.br/hc/article_attachments/14389164106903)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16860097377175)CAUSA:**

Ocorre ao não informar a chave da nota de origem e a TOP exige que seja informada.
