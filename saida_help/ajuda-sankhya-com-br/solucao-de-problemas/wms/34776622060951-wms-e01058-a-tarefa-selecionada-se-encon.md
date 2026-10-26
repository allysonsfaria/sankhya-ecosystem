---
id: "34776622060951"
titulo: "WMS_E01058: A tarefa selecionada se encontra fechada ou em execução no coletor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34776622060951-WMS-E01058-A-tarefa-selecionada-se-encontra-fechada-ou-em-execu%C3%A7%C3%A3o-no-coletor"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:45Z"
rotulos: ["WMS", "Gerência do WMS", "Erro", "WMS_E01058", "A tarefa selecionada se encontra fechada", "Cancelar a Execução do Mapa", "[WMS_E01058] A tarefa selecionada se encontra fechada ou em execução no coletor.", "em execução no coletor", "Execução de Tarefas Impressas", "Execução de Tarefas Impressas WMS", "Squad WMS", "Coletor de Dados", "Execução de Tarefas"]
---

# WMS_E01058: A tarefa selecionada se encontra fechada ou em execução no coletor

**MENSAGEM**

[WMS\_E01058] A tarefa selecionada se encontra fechada ou em execução no coletor.

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta buscar uma tarefa pelo coletor de dados ou pela tela de **"Execução de Tarefas Impressas"** e a tarefa já está sendo executada por outro usuário ou já foi finalizada.

**SOLUÇÃO**

**(1)** Acesse a tela **"Gerência do WMS"** (WMS » Gerência » Gerência do WMS) para verificar o status da tarefa selecionada.

**(2)** Verifique se a tarefa está em execução e identifique qual usuário está executando a tarefa.

**(3)** **Se a rotina estiver sendo executada pelo coletor de dados:**

- Acesse o coletor com o usuário da tarefa
- Rejeite todas as tarefas que ainda estão em execução

**(4)** **Se a rotina estiver sendo executada pela tela de Execução de Tarefas Impressas:**

- Acesse a tela **"Execução de Tarefas Impressas WMS"** (WMS » Rotinas » Execução de Tarefas Impressas WMS)
- Clique em **"Cancelar a Execução do Mapa"**

**CAUSA**

A mensagem ocorre quando uma tarefa já está sendo executada por um usuário ou já foi finalizada, impedindo que outro usuário acesse a mesma tarefa simultaneamente.
