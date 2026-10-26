---
id: "360043733834"
titulo: "Não há tarefas de armazenagem para o produto 999999999999 na doca 888888"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043733834-N%C3%A3o-h%C3%A1-tarefas-de-armazenagem-para-o-produto-999999999999-na-doca-888888"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:17Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "WMS", "Estoque", "Sem tarefas de armazenagem na doca", "Equipamento/Usuário não liberado", "Definir permissões para Equipamento e Usuário", "Squad WMS"]
---

# Não há tarefas de armazenagem para o produto 999999999999 na doca 888888

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16418157889559) MENSAGEM:**

Não há tarefas de armazenagem para o produto 999999999999 na doca 888888.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418157891479) SOLUÇÃO:**

 Para correção, siga os passos abaixo:

![Imagem 3: Acesse MGEWMS » Arquivos » Cadastros » Tipo de Equipamento , aba Tarefas que podem ser executadas por este tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16418157893655) Acesse MGEWMS » Arquivos » Cadastros » Tipo de Equipamento, aba **Tarefas que podem ser executadas por este tipo de Equipamento** e defina as tarefas conforme o tipo de Equipamento suportado. Na aba **Unidades permitidas para este tipo de Equipamento** defina as Unidades conforme o tipo de Equipamento suportado

![Imagem 4: Acesse MGEWMS » Arquivos » Cadastros » Definir Tarefa e Volume por usuário , aba Unidades permitidas para este Usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/16418157894935) Acesse MGEWMS » Arquivos » Cadastros » Definir Tarefa e Volume por usuário, aba **Unidades permitidas para este Usuário** e defina as Unidades conforme o Usuário. Na aba **Tarefas que podem ser executadas por este Usuário** defina as tarefas que são permitidas para este Usuário.

![Imagem 5: Após os ajustes, busque novamente a tarefa no Coletor.](https://ajuda.sankhya.com.br/hc/article_attachments/16418180029335) Após os ajustes, busque novamente a tarefa no Coletor.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16418157898007) CAUSA:**

Ocorre quando Equipamento e/ou Usuário não esta devidamente liberado para movimentar o respectivo produto na Doca.
