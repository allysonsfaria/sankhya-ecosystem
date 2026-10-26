---
id: "25511981681303"
titulo: "Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25511981681303-N%C3%A3o-pode-Alterar-Excluir-uma-tabela-com-data-anterior-a-ultima-data-da-tabela"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:45:29Z"
rotulos: ["Configuração", "Financeiro", "ORA-20101", "Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela", "Erro", "Tabela de Preço"]
---

# Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25511973498135) **MENSAGEM:**

ORA-20101: Não pode Alterar/Excluir uma tabela com data anterior a ultima data da tabela.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25511981668631)SOLUÇÃO:**

Caso a mensagem seja apresentada ao tentar duplicar uma tabela, defina uma data de vigor na tabela de destino que seja posterior à última data vigor da tabela de origem.

Se estiver tentando alterar ou excluir uma tabela com data de vigor anterior à última data de vigor da tabela o sistema não irá permitir.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25511973519383)CAUSA:**

A mensagem é apresentada ao acessar a tela **"Tabela de Preço",** clicar na opção **"Copiar Tabela"** e inserir uma data de vigor anterior à data de vigor da tabela copiada.

Também ao tentar alterar ou excluir uma tabela com data de vigor anterior à última data de vigor da tabela, a mensagem é apresentada.
