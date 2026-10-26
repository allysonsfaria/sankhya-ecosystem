---
id: "10325919517847"
titulo: "TOP para NF-e Pendente de Retorno não pode atualizar estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10325919517847-TOP-para-NF-e-Pendente-de-Retorno-n%C3%A3o-pode-atualizar-estoque"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:03:54Z"
rotulos: ["Configuração", "NF-e", "TOP", "Estoque", "Financeiro", "CORE_E02623", "não pode atualizar estoque.", "Atualização do Estoque", "TOP para NF-e Pendente de Retorno não pode atualizar estoque."]
---

# TOP para NF-e Pendente de Retorno não pode atualizar estoque

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18887649507223) MENSAGEM:**

[CORE\_E02623] TOP para NF-e Pendente de Retorno não pode atualizar estoque.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18887626430231) SITUAÇÃO:**

Ao tentar incluir a Top para NF-e  pendente de retorno na aba impressão de uma outra TOP a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18887649523991) SOLUÇÃO:**

Verifique a configuração do **Tipo de Operação** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) para NF-e pendente de retorno, observe o campo "Atualização do Estoque", na aba **Estoque.**Ele não pode estar configurado como 'Atualizar'. Portanto, caso necessário, faça o ajuste e realize novamente o lançamento.

![Imagem 4: Verifique a configuração do Tipo de Operação (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) para NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/10325915696919)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18887649545879)CAUSA:**

Ocorre quando o Tipo de Operação está atualizando estoque.
