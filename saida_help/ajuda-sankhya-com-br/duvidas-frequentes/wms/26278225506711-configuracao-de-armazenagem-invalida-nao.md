---
id: "26278225506711"
titulo: "Configuração de armazenagem inválida. Não existem configurações ativas : Regra X"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26278225506711-Configura%C3%A7%C3%A3o-de-armazenagem-inv%C3%A1lida-N%C3%A3o-existem-configura%C3%A7%C3%B5es-ativas-Regra-X"
trilha: "Dúvidas Frequentes > WMS"
atualizado_em: "2026-07-22T14:42:47Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro"]
---

# Configuração de armazenagem inválida. Não existem configurações ativas : Regra X

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26278203207319) **MENSAGEM:**

Configuração de Armazenagem inválida. Não existem configurações ativas : Regra X

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26278203210903)SOLUÇÃO:**

Acesse a tela **"Produto"** (Caminho: Configurações » Cadastros » Produtos » Produtos), verifique qual a regra de armazenagem vinculada no campo **"Regra Armazenagem",** na aba **"WMS".** Caso não tenha regra definida, o sistema valida a regra marcada como padrão.

Em seguida, acesse a tela **"Configuração de Armazenagem"** (Caminho: WMS » Rotinas » Configuração de Armazenagem), verifique a regra vinculada ao produto ou regra padrão e observe qual a sequência das regras de armazenagem ativa que será validada na geração das tarefas para o produto.

[GIF animado: Imagem 3: Em seguida, acesse a tela "Configuração de Armazenagem" (Caminho: WMS » Rotinas » Configuração de Armazenagem) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/26278203213335)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26278203215127)CAUSA:**

Ocorre quando a regra de armazenagem cadastrada no produto não esta habilitada, ou quando alguma das regras de armazenagem não está ativa.
