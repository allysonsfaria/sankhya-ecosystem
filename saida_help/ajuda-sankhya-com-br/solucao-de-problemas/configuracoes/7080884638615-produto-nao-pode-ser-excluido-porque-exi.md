---
id: "7080884638615"
titulo: "Produto não pode ser excluído porque existe dependência de 'Exceções das Tabelas de Preço'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7080884638615-Produto-n%C3%A3o-pode-ser-exclu%C3%ADdo-porque-existe-depend%C3%AAncia-de-Exce%C3%A7%C3%B5es-das-Tabelas-de-Pre%C3%A7o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:15:14Z"
rotulos: ["Produtos", "Configuração", "Estoque", "CORE_E03832", "Dependência de Exceções de Tabela de Preço", "Erro", "Tabelas de Preço"]
---

# Produto não pode ser excluído porque existe dependência de 'Exceções das Tabelas de Preço'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16480918788759) MENSAGEM:**

[CORE\_E03832] Produto não pode ser excluído porque existe dependência de 'Exceções das Tabelas de Preço'.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16480949632791) CAUSA:**

Mensagem apresentada ao tentar excluir um produto que está vinculado a tabela TGFEXC [Exceções da tabela de preços].

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16480949638295) SOLUÇÃO:**

Produtos que possuem ligações em outras tabelas não podem ser excluídos. Caso esse produto não seja mais movimentado, recomenda-se que seja **inativado** (desmarque a opção 'ativo');

**(1)** A ligação citada nessa mensagem, trata-se da **'Tabela de Preço - Exceções';**
