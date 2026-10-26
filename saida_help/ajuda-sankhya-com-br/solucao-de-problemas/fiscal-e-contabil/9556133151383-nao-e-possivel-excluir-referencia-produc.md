---
id: "9556133151383"
titulo: "Não é possível Excluir Referência Produção, pois existem registros com status \"Finalizado\" "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9556133151383-N%C3%A3o-%C3%A9-poss%C3%ADvel-Excluir-Refer%C3%AAncia-Produ%C3%A7%C3%A3o-pois-existem-registros-com-status-Finalizado"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:07:24Z"
rotulos: ["Eventos", "Fiscal", "Produção", "LIV_E00061", "Não é possível excluir referência com registros \"Finalizado\".", "Solução: Excluir referências só se não houver eventos finalizados.", "Ocorrido ao tentar excluir no ambiente Produção.", "Erro", "Reinf"]
---

# Não é possível Excluir Referência Produção, pois existem registros com status "Finalizado" 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18606331227287) MENSAGEM:**

[LIV\_E00061] Não é possível Excluir Referência Produção, pois existem registros com status "Finalizado".

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606331238167) SITUAÇÃO:**

Ao tentar excluir e gerar o REINF novamente, a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18606323484567) CAUSA:**

Tentativa de exclusão de referências em ambiente Produção.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18606331245335) SOLUÇÃO:**

Não é possível excluir referências no ambiente "Produção" uma vez que já foi executada a ação "Gerar", e nessa ação, gerou algum evento e o mesmo está com o campo Status igual a "Finalizado", inclusive o evento R1000.
