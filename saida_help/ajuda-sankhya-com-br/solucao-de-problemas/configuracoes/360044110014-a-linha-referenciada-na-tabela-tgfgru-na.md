---
id: "360044110014"
titulo: "A linha referenciada na tabela TGFGRU, não está cadastrada, ou não está ativa, ou não é analítica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110014-A-linha-referenciada-na-tabela-TGFGRU-n%C3%A3o-est%C3%A1-cadastrada-ou-n%C3%A3o-est%C3%A1-ativa-ou-n%C3%A3o-%C3%A9-anal%C3%ADtica"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:00Z"
rotulos: ["#Revisado Silvio", "Grupo de produtos não está ativo não é analítico ou não existe", "Produtos", "Configuração", "Grupo de Produtos", "Estoque", "Cadastro", "Erro ao Salvar Produto", "Ativação e Análise de Grupo", "Erro"]
---

# A linha referenciada na tabela TGFGRU, não está cadastrada, ou não está ativa, ou não é analítica

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16949614520215) MENSAGEM:**

A linha referenciada na tabela TGFGRU, não está cadastrada, ou não está ativa, ou não é analítica.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16949627403287) SITUAÇÃO:**

Ao salvar a inclusão de um produto, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16949627408535) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16949614527255) Acesse: Configurações » Cadastros » Produtos » Produtos

- Identifique no cadastro do produto, aba: **"Geral"**, campo **"Grupo"**, o código e nome do grupo vinculado ao produto.

![Imagem 5: Acesse: Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/article_attachments/16949614536983) Acesse: Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços

- Pesquise pelo grupo, após identifica-lo, verifique se o **Grupo** está **'Ativo'** e se o mesmo é **'Analítico'**. Se não estiver **Ativo**, verifique a possibilidade de ativá-lo.
- Se não for Analítico, verifique na hierarquia qual é o GRUPO a ser selecionado do tipo **'Analítico'** e informe o código ao produto.

**![Imagem 6: NOTA:](https://ajuda.sankhya.com.br/hc/article_attachments/16949627418647) NOTA:**

O grupo **0 - <SEM GRUPO>**, é um grupo default do sistema e deve existir na base de dados, considere não exclui-lo do sistema.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16949614543767) CAUSA:**

Ocorre quando o Grupo vinculado ao produto não está devidamente configurado para utilização.
