---
id: "360043579554"
titulo: "Pedido não encontrado ou não está pendente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043579554-Pedido-n%C3%A3o-encontrado-ou-n%C3%A3o-est%C3%A1-pendente"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:01:28Z"
rotulos: ["Produtos", "Parceiro", "Pedido de Compra", "Importação", "TOP", "Correção de Erro", "Importação de Itens", "Erro", "Comércio Exterior"]
---

# Pedido não encontrado ou não está pendente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16192285192727) MENSAGEM:**

Pedido não encontrado ou não está pendente. 

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192316097175) SITUAÇÃO:**

Ao utilizar a opção: **Importar itens do pedido de Compra**, no Processo de Importação do Módulo Comercio Exterior, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192285198231) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP :](https://ajuda.sankhya.com.br/hc/article_attachments/16192285200791) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP:

- Campo **"Tipo de Movimento":** O-Pedido de Compra

Aba: **Geral**

- Campo **"Digitar Informações sobre Importação":** marcado

![Imagem 5: Campo "Digitar Informações sobre Importação": marcado](https://ajuda.sankhya.com.br/hc/article_attachments/14683170331543)

![Imagem 6: Verifique se o parceiro do lançamento do Pedido de Compra é igual ao parceiro informado na Aba: Cadastro do processo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16192316104855) Verifique se o parceiro do lançamento do Pedido de Compra é igual ao parceiro informado na Aba: **Cadastro** do processo de importação.

![Imagem 7: Verifique se a Empresa do Lançamento do Pedido de Compra é igual a Empresa informada na Aba: Cadastro do processo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16192316106647) Verifique se a Empresa do Lançamento do Pedido de Compra é igual a Empresa informada na Aba: Cadastro do processo de importação.

![Imagem 8: Verifique se algum produto do Pedido de Compra foi entregue. Caso a quantidade entregue for maior que a quantidade…](https://ajuda.sankhya.com.br/hc/article_attachments/16192316108567) Verifique se algum produto do Pedido de Compra foi entregue. Caso a quantidade entregue for maior que a quantidade negociada em um dos itens do pedido, ocorrerá o erro.

![Imagem 9: Verifique se o processo de Importação foi ligado anteriormente a algum outro pedido, esta ligação ocorre através da…](https://ajuda.sankhya.com.br/hc/article_attachments/16192316111255) Verifique se o processo de Importação foi ligado anteriormente a algum outro pedido, esta ligação ocorre através da tabela 'TCEVAR'.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16192316113047) CAUSA:**

Ocorre ao utilizar a Rotina de **Importar itens do Pedido de Compra** no Processo de Importação e alguma das considerações acima não foi atendida.
