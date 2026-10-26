---
id: "14522777839895"
titulo: "Nota Aguardando Autoriz. Parâmetro TOPNFEPENRET deve ter uma TOP informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14522777839895-Nota-Aguardando-Autoriz-Par%C3%A2metro-TOPNFEPENRET-deve-ter-uma-TOP-informada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:33Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "TOP", "CORE_E04911", "Configure a TOP para \"Pendente de Retorno\" no parâmetro", "Falta de TOP configurada para NF-e \"Pendente de Retorno\"", "NF-e aguardando autorização necessita de TOP informada", "Erro"]
---

# Nota Aguardando Autoriz. Parâmetro TOPNFEPENRET deve ter uma TOP informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16968239546007) MENSAGEM:**

[CORE\_E04911] Nota Aguardando Autoriz. Parâmetro **TOPNFEPENRET** deve ter uma TOP informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16968223469975)SOLUÇÃO:**

A marcação **"Enviar notas com Status Pendente de Retorno"** será habilitada apenas para as notas que, após seu lançamento, encontrarem-se com status **Aguardando autorização**. Estas notas deverão possuir a **TOP Pendente de Retorno,** configurada no parâmetro **"TOP para NF-e pendente de retorno - TOPNFEPENRET"**.

![Imagem 3: A marcação "Enviar notas com Status Pendente de Retorno" será habilitada apenas para as notas que, após seu lançamento,…](https://ajuda.sankhya.com.br/hc/article_attachments/14523122881943)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16968239549079)CAUSA:**

Quando o sistema tenta atribuir uma NF como: "Pendente de Retorno" e não encontra o cadastro de uma TOP para essa operação.
