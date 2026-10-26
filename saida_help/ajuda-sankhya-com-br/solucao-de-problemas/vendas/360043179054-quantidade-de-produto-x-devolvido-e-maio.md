---
id: "360043179054"
titulo: "Quantidade de produto 'X' devolvido é maior que o total disponível para devolução das notas de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179054-Quantidade-de-produto-X-devolvido-%C3%A9-maior-que-o-total-dispon%C3%ADvel-para-devolu%C3%A7%C3%A3o-das-notas-de-venda"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-24T12:42:03Z"
rotulos: ["#PUBLIFER", "NF-e", "Importação", "Vendas", "Estoque", "Devolução", "Produto devolvido excede total disponível", "Verificar notas de origem no XML de devolução", "Não é possível devolver itens já devolvidos", "Documentos Eletrônicos"]
---

# Quantidade de produto 'X' devolvido é maior que o total disponível para devolução das notas de venda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16162261769111) MENSAGEM:**

Quantidade de produto 'X' devolvido é maior que o total disponível para devolução das notas de venda.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162261770647) SITUAÇÃO:**

Mensagem apresentada ao importar XML de notas de devolução.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162314264983) SOLUÇÃO:**

![Imagem 4: Verifique quais são as notas de origem (venda) referenciadas no XML de devolução que está sendo importado.](https://ajuda.sankhya.com.br/hc/article_attachments/16162261777175) Verifique quais são as notas de origem (venda) referenciadas no XML de devolução que está sendo importado.

Essa informação é visualizada na tag **<refNFe>**, conforme exemplo abaixo:

![Imagem 5: Essa informação é visualizada na tag <refNFe> , conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/14676728462359)

![Imagem 6: Localize no " Portal de Vendas " (através da chave acima) a nota de venda origem da devolução a ser importada.](https://ajuda.sankhya.com.br/hc/article_attachments/16162314268567) Localize no **"[Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)"** (através da chave acima) a nota de venda origem da devolução a ser importada.

![Imagem 7: Abra a nota na Central e certifique-se que para os itens a serem devolvidos já existe uma nota de devolução vinculada:](https://ajuda.sankhya.com.br/hc/article_attachments/16162314270871) Abra a nota na Central e certifique-se que para os itens a serem devolvidos já existe uma nota de devolução vinculada:

**(2)** Outras Opções » **Documentos Relacionados** » Documentos de Destino:

![Imagem 8: (2) Outras Opções » Documentos Relacionados » Documentos de Destino:](https://ajuda.sankhya.com.br/hc/article_attachments/14685244561943)

![Imagem 9: (2) Outras Opções » Documentos Relacionados » Documentos de Destino:](https://ajuda.sankhya.com.br/hc/article_attachments/12271637235351)

![Imagem 10: Para o caso acima, não é possível realizar uma nova devolução para a nota de venda/origem referenciada. Alinhe…](https://ajuda.sankhya.com.br/hc/article_attachments/16162314283031) Para o caso acima, não é possível realizar uma nova devolução para a nota de venda/origem referenciada. Alinhe internamente qual das notas procede, realizando as devidas tratativas.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16162261802775) CAUSA:**

Mensagem apresentada quando para a nota referenciada na respectiva nota de devolução, não existem mais itens pendentes de devolução, visto que outra devolução já foi efetuada.
