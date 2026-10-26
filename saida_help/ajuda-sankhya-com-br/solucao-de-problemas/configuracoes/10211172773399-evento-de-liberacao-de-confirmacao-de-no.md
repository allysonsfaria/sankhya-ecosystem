---
id: "10211172773399"
titulo: "Evento de liberação de Confirmação de nota (Evento 18) não pode possuir valor diferente de 1"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10211172773399-Evento-de-libera%C3%A7%C3%A3o-de-Confirma%C3%A7%C3%A3o-de-nota-Evento-18-n%C3%A3o-pode-possuir-valor-diferente-de-1"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:17Z"
rotulos: ["Configuração", "Eventos", "Fiscal", "NF-e", "SEFAZ", "CORE_E02841", "Restrição de Valor no Evento de Liberação"]
---

# Evento de liberação de Confirmação de nota (Evento 18) não pode possuir valor diferente de 1

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19034869099031) MENSAGEM:**

[CORE\_E02841] Evento de liberação de Confirmação de nota (Evento 18) não pode possuir valor diferente de 1.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19034840092567) SITUAÇÃO:**

Ao tentar fazer a liberação de um lançamento a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19034840104727) CAUSA:**

Ocorre quando é alterado o valor a ser liberado entretanto, o evento configurado é o 18 de confirmação de nota.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19034869117847) SOLUÇÃO:**

O evento 18 é usado apenas para solicitar liberação para confirmação do pedido, e não considera valores.

Caso deseje que seja possível alterar o valor ou necessite alterar o valor do pedido/nota, configure para esse processo o evento 44 ao invés do evento 18. Pois, a permissão de alteração de valores está condicionada ao evento 44.
