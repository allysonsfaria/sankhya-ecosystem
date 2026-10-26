---
id: "360056901114"
titulo: "A tabela contextualizada foi a tabela 0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056901114-A-tabela-contextualizada-foi-a-tabela-0"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:27:00Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "Correção", "Parceiro", "SEMALERTAPRECO", "contextualizada", "Preço de Tabela", "Erro", "Tabela de Preço"]
---

# A tabela contextualizada foi a tabela 0

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16251022219927) MENSAGEM**:

A tabela contextualizada foi a tabela 0.
Tipo de Tabela de Preço: Perfil do Parceiro
Produto "XPTO" sem preço de tabela, não pode ser vendido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16251022222999) SOLUÇÃO:**

Para correção, siga as instruções dispostas no artigo: [Produto sem preço de tabela, não pode ser vendido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043358713)

**Nota**: Esta informação é apresentada, quando o parâmetro **"SEMALERTAPRECO-Não mostrar alerta 'sem preço de tabela"** está desligado.

**![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16251050038935) OBSERVAÇÃO:**

**(1)** Parâmetros que influenciam:
**"SEMALERTAPRECO-Não mostrar alerta 'sem preço de tabela'"**, ao ser ligado, mesmo que o **"Aceitar valor unitário igual a zero na venda? ACEITARUNITZERO"** esteja desligado, não irá mostrar o alerta ao digitar o código do item na nota e continuará bloqueando itens com valor unitário zerado caso o ACEITARUNITZERO esteja desligado.

O parâmetro **"Aceitar valor unitário igual a zero na venda? ACEITARUNITZERO"**, quando ligado, deixa informar o produto com valor unitário zerado, em alguns casos esse não é o melhor comportamento.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16251050049943) CAUSA:**

Ocorre quando não foi definido de maneira correta uma tabela de preço para o produto, de acordo com o tipo de tabela de preço definido no parâmetro **"Tabela de preços por: - TIPTABPRECOS".**
