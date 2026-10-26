---
id: "31092671856663"
titulo: "[WMS_E01003] Não foi selecionada uma linha que está relacionada a uma tarefa do WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31092671856663--WMS-E01003-N%C3%A3o-foi-selecionada-uma-linha-que-est%C3%A1-relacionada-a-uma-tarefa-do-WMS"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:33:37Z"
rotulos: ["Configuração", "WMS", "Executantes", "Recebimento", "Estoque", "Gerência do WMS", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Tarefa do WMS", "Não foi selecionada uma linha", "Squad WMS", "WMS_E01003", "Tarefa"]
---

# [WMS_E01003] Não foi selecionada uma linha que está relacionada a uma tarefa do WMS

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31092688446999) **MENSAGEM:**

[WMS\_E01003] Não foi selecionada uma linha que está relacionada a uma tarefa do WMS

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31092671841175)SOLUÇÃO:**

**(1)** Acesse a tela [**''Gerência do WMS''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS) (WMS » Gerência » Gerência do WMS).

**(2)** Verifique se existe tarefas geradas em Itens do Recebimento.

**(3)** Acesse a tela [**''Tarefa de Recebimento''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS) (WMS » Rotinas » Tarefas de Recebimento) e gere a tarefa de armazenagem para o recebimento.

- Uma vez que a tarefa existe, é possível atribuir um executante normalmente.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31092671843351)CAUSA:**

A mensagem aparece porque não foi gerada uma tarefa de armazenagem para o recebimento.

Sem essa tarefa, não há número de tarefa criado, impossibilitando a vinculação de um executante na tela ''Gerência do WMS''.

Portanto, a condição essencial para atribuir um operador é primeiro criar a tarefa de armazenagem.
