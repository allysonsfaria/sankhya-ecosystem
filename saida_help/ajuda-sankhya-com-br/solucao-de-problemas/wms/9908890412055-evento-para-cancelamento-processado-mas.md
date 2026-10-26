---
id: "9908890412055"
titulo: "Evento para Cancelamento processado, mas o evento não foi vinculado ao MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9908890412055-Evento-para-Cancelamento-processado-mas-o-evento-n%C3%A3o-foi-vinculado-ao-MDF-e"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:05:25Z"
rotulos: ["ERROMDFE", "MDF-e", "SEFAZ", "Cancelamento", "Transporte", "CORE_E03555", "Evento cancelado não vinculado ao MDF-e", "Mercadoria circulada; emita novo MDF-e", "Erro ao cancelar MDF-e em circulação", "Documentos Eletrônicos"]
---

# Evento para Cancelamento processado, mas o evento não foi vinculado ao MDF-e

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19034896849047) MENSAGEM:**

[CORE\_E03555] Evento para Cancelamento processado, mas o evento não foi vinculado ao MDF-e. Status de retorno: XXX, motivo: Rejeição: Circulação de MDF-e verificada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19034896856087) SITUAÇÃO:**

Ao tentar cancelar o MDF-e a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19034935146519) CAUSA:**

Ocorre ao tentar cancelar um MDF-e que já teve sua mercadoria circulada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19034896865559) SOLUÇÃO:**

Esta rejeição ocorre quando a nota fiscal que está sendo cancelada já está em circulação e, possivelmente, passou em um posto fiscal. Ou seja, a mercadoria já foi circulada e o cancelamento não poderá ser efetuado. Caso precise alterar algo, ou até mesmo emitir outro, encerre e emita outro MDF-e.
