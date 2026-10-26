---
id: "8425348813463"
titulo: "Impossível converter para uma string válida: null"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8425348813463-Imposs%C3%ADvel-converter-para-uma-string-v%C3%A1lida-null"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:12:01Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "EFD", "não apagar", "Ao gerar SPED ICMS erro aparece", "Impossível converter string válida: null", "Preencha campo \"Dt. Docto\" em Ajuste de Apuração", "Erro"]
---

# Impossível converter para uma string válida: null

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16596637213975) MENSAGEM**:

Impossível converter para uma string válida: null.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16596677252119) SITUAÇÃO:**

Ao tentar gerar o SPED ICMS a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16596677253783) SOLUÇÃO:**

Acesse a tela **"Ajuste de Apuração de ICMS e ICMS ST"** (Caminho de acesso à tela: Livros Fiscais » Arquivos » Ajuste da Apuração de ICMS e ICMS ST) e verifique se todos os lançamentos estão com o campo "**Dt. Docto"** preenchidos, caso não estejam faça o preenchimento e salve.

![Imagem 4: Acesse a tela " Ajuste de Apuração de ICMS e ICMS ST" (Caminho de acesso à tela: Livros Fiscais » Arquivos » Ajuste da…](https://ajuda.sankhya.com.br/hc/article_attachments/16596677254679)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16596637224471)CAUSA:**

Esse erro é causado no processo de geração do EFD ICMS/IPI quando temos na tela Ajuste da apuração de icms e icms st lançamentos que, na aba "Ajuste", estejam com o campo Dt. Docto vazio.
