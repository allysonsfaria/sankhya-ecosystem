---
id: "34777747224727"
titulo: "WMS_E00811: Item(ns) de tarefa(s) para o nro. mapa está(ão) com situação: 'Fechada'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34777747224727-WMS-E00811-Item-ns-de-tarefa-s-para-o-nro-mapa-est%C3%A1-%C3%A3o-com-situa%C3%A7%C3%A3o-Fechada"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:26:42Z"
rotulos: ["Configuração", "WMS", "Movimentação Financeira", "Expedição de Mercadorias", "Estoque", "Erro", "Execução de Tarefas Impressas WMS", "WMS_E00811", "Item(ns) de tarefa(s) para o nro. mapa está(ão) com situação: 'Fechada'"]
---

# WMS_E00811: Item(ns) de tarefa(s) para o nro. mapa está(ão) com situação: 'Fechada'

**MENSAGEM**

[WMS\_E00811] Item(ns) de tarefa(s) para o nro. mapa está(ão) com situação: 'Fechada'

**SITUAÇÃO**

Esta mensagem aparece quando o usuário tenta cancelar a execução de uma tarefa no mapa, mas a tarefa já foi finalizada e possui situação diferente de **"Em Execução"**.

**SOLUÇÃO**

**(1)** Acesse a tela **"Execução de Tarefas Impressas WMS"** (WMS » Rotinas » Execução de Tarefas Impressas WMS) e identifique a situação da tarefa que está sendo selecionada.

**(2)** Verifique se a situação da tarefa está como **"Em Execução"**. Caso esteja diferente, significa que a tarefa já foi finalizada e o sistema não permite alterar a situação de tarefa fechada.

**(3)** Caso seja necessário cancelar, cancele toda a separação pela tela **"Expedição de Mercadorias"** (WMS » Rotinas » Expedição de Mercadorias) e faça o retorno das mercadorias.

**CAUSA**

A mensagem ocorre quando uma tarefa já foi finalizada e o usuário tenta cancelar a execução da tarefa do mapa. O sistema não permite alterações em tarefas com situação **"Fechada"**.
