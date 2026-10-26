---
id: "24847006206871"
titulo: "Tarefa Conferência de Volumes não aparece no menu dos coletores WMS Superwaba/Android"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24847006206871-Tarefa-Confer%C3%AAncia-de-Volumes-n%C3%A3o-aparece-no-menu-dos-coletores-WMS-Superwaba-Android"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-07-22T14:46:26Z"
rotulos: ["Configuração", "WMS", "Superwaba", "Android", "Parâmetro", "Tarefa Conferência de Volumes"]
---

# Tarefa Conferência de Volumes não aparece no menu dos coletores WMS Superwaba/Android

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24847013380887) **MENSAGEM:**

Tarefa Conferência de Volumes não aparece no menu dos coletores WMS Superwaba/Android.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24847006189719)SOLUÇÃO:**

Para a tarefa **"Conferência de Volumes"** ser apresentada no menu do coletor, o parâmetro **"FORMVOLPOSCONF"** deve estar **"Desligado".** Assim, será visualizada a tarefa 12 - Conferência de Volumes e a tarefa 22- Formação de Volumes não será apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24847013387415)CAUSA:**

Com o parâmetro FORMVOLPOSCONF ligado, após a conferência por pedido, será feito a tarefa formação de volumes, não sendo necessário a realização da Tarefa Conferência de volumes.
