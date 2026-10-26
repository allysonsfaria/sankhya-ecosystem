---
id: "12499991131927"
titulo: "Este Volume foi usado em cotações não pode ser excluído"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12499991131927-Este-Volume-foi-usado-em-cota%C3%A7%C3%B5es-n%C3%A3o-pode-ser-exclu%C3%ADdo"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:00:50Z"
rotulos: ["Produtos", "Configuração", "Fórmulas", "Estoque", "SQL-50001", "Erro ao Excluir Volume em Cotações", "Erro"]
---

# Este Volume foi usado em cotações não pode ser excluído

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16362802163095) MENSAGEM:**

[SQL-50001]: Este Volume foi usado em cotações não pode ser excluído.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16362791997207) SOLUÇÃO:**

O erro será apresentado quando existir um registro na TGFICP com o determinado Produto e Unidade. A TGFICP (ItemComposicaoProduto) valida se existem Matérias-Primas compondo a Produção de determinado produto.

Ao acessar a tela **"Fórmula de Composição do Produto"** é possível identificar se existe um registro do Produto com seus componentes, e essa ligação entre produto final e componentes é o impeditivo da exclusão. Se encontrar nessa rotina, é recomendado rever sobre essa Fórmula de Composição do Produto e, caso desejar, excluir as Matérias Primas vinculadas a ele.

Também é possível identificar componentes pela aba de "**Componentes"** do Cadastros do Produto. Se necessário, faça a exclusão das Matérias Primas vinculadas a ele.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16362791998871) CAUSA:**

Esse erro ocorre ao tentar excluir uma Unidade Alternativa do produto (Matéria-Prima), mas a mesma já foi utilizada como composição no processo produtivo e não foi excluído o registro.
