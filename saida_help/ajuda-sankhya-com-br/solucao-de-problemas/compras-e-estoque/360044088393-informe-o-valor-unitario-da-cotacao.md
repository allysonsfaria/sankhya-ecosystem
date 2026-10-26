---
id: "360044088393"
titulo: "Informe o valor unitário da cotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044088393-Informe-o-valor-unit%C3%A1rio-da-cota%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:39Z"
rotulos: ["#RevisadoGui", "Produtos", "Configuração", "Importação", "Estoque", "Valor Unitário", "Ajuste de Decimais", "Importação de Pedidos", "Erro"]
---

# Informe o valor unitário da cotação

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16170383713175) MENSAGEM:**

Informe o valor unitário da cotação.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16170383715735) SITUAÇÃO:**

Ao tentar importar o Pedido do MGE para o Importação, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16170383717271) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: MGEImport » Arquivos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16170383719191) Acesse: MGEImport » Arquivos » Produtos

Aba: **Medidas e Estoque** - Campo "**Decimais p/ valor(Importação)"**

![Imagem 5: Aba: Medidas e Estoque - Campo " Decimais p/ valor(Importação)"](https://ajuda.sankhya.com.br/hc/article_attachments/14692474805783)

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17855159369879) IMPORTANTE:**

Este campo está disponível apenas no módulo MGEImportação

![Imagem 7: Após o ajuste efetue novamente a importação do pedido e confira os valores unitários do(s) produto(s).](https://ajuda.sankhya.com.br/hc/article_attachments/16170418786711) Após o ajuste efetue novamente a importação do pedido e confira os valores unitários do(s) produto(s).

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16170383724567) CAUSA:**

Ocorre quando o valor unitário está com poucas casas decimais, então a conversão da moeda estrangeira para a moeda real não é feita de forma a chegar um valor aceitável, pois a dizima foi desprezada.
