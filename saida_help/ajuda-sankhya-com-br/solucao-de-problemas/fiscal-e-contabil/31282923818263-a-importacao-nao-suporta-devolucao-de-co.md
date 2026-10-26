---
id: "31282923818263"
titulo: "A importação não suporta devolução de compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31282923818263-A-importa%C3%A7%C3%A3o-n%C3%A3o-suporta-devolu%C3%A7%C3%A3o-de-compra"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:33:25Z"
rotulos: ["Fiscal", "NF-e", "XML", "Importação", "Passos para resolver", "Razão do erro", "Detalhe do erro", "CORE_E02898", "importação não suporta devolução de compras", "Erro"]
---

# A importação não suporta devolução de compra

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31282897793559) **MENSAGEM:**

[CORE\_E02898] Chave XXXXX referenciada no XML é de uma compra Nro.Único XX. A importação não suporta devolução de compras.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31939690733975) SITUAÇÃO:**

Ao realizar uma importação de xml de uma nota de devolução de compras que seja de terceiro a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31282897794583)SOLUÇÃO:**

Este é um comportamento do sistema, que não realiza **importação de notas de devoluções de compra, sendo elas de terceiros.**

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31282897797271)CAUSA:**

O erro é apresentado quando se está importando o xml de uma nota de devolução de terceiro, o sistema verifica se a chave referenciada é de compras, se for o sistema faz a validação.
