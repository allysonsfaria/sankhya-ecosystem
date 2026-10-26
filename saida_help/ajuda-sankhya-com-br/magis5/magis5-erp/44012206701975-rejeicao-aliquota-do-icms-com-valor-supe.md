---
id: "44012206701975"
titulo: "Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados [nItem:1]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012206701975-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-do-ICMS-com-valor-superior-a-4-por-cento-na-opera%C3%A7%C3%A3o-de-sa%C3%ADda-interestadual-com-produtos-importados-nItem-1"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:34Z"
rotulos: ["sync_hc", "magis5", "magis5_204051670537", "sync_hash_be0a0f08fab1"]
---

# Rejeição: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados [nItem:1]

## Este erro indica que há um problema relacionado à alíquota do Imposto sobre Circulação de Mercadorias e Serviços (ICMS) aplicada em uma operação de saída interestadual com produtos importados.

Para resolver esse erro, você pode considerar as seguintes etapas:

**VERIFIQUE OS ITENS QUE FAZEM PARTE DA VENDA**

Na tela de vendas, clique em: Visualizar Pedido/Venda:

![Imagem 1: Na tela de vendas, clique em: Visualizar Pedido/Venda:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-28.png)

Nos detalhes do pedido, copie o ID do produto:

![Imagem 2: Nos detalhes do pedido, copie o ID do produto:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-30.png)

No menu, clique em Cadastros → Produtos, insira o ID do produto no campo "ID/SKU" e clique em: Aplicar Filtros:

![Imagem 3: No menu, clique em Cadastros → Produtos, insira o ID do produto no campo "ID/SKU" e clique em: Aplicar Filtros:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-31-1024x261.png)

Clique em: Editar:

![Imagem 4: Clique em: Editar:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-32-1024x129.png)

Na aba Fiscal, analise a "Origem da Mercadoria":

![Imagem 5: Na aba Fiscal, analise a "Origem da Mercadoria":](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-33-1024x299.png)

1. O produto pode ser Estrangeiro (adquirida no mercado Interno) ou,
2. O produto pode ser Nacional, exceto as indicadas no código 3 a 5.

Guarde essa informação.

**EMITA A NOTA FISCAL MANUAL**

Após a verificação da origem da mercadoria, é necessário editar a tentativa de emissão da NF-e.

Na tela de vendas, clique em: Emitir NF-e Manual:

![Imagem 6: Na tela de vendas, clique em: Emitir NF-e Manual:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-34-1024x129.png)

Na Visualização da Nota Fiscal, insira a operação referente à Origem da Mercadoria que foi analisado no cadastro do produto.

Se o produto for de origem nacional, selecione: Venda de Mercadoria para Fora do Estado:

![Imagem 7: Se o produto for de origem nacional, selecione: Venda de Mercadoria para Fora do Estado:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-35.png)
![Imagem 8: Se o produto for de origem nacional, selecione: Venda de Mercadoria para Fora do Estado:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-12-1024x77.png)

Se o produto for de origem estrangeira, selecione: Venda de Mercadoria Adq ou Rec de Terceiros (Est):

![Imagem 9: Se o produto for de origem estrangeira, selecione: Venda de Mercadoria Adq ou Rec de Terceiros (Est):](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-36.png)

Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:

![Imagem 10: Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-37.png)

Caso haja alguma inconsistência, será exibido um pop-up com uma mensagem de erro.

Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:

![Imagem 11: Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-38.png)

Pronto, a nota está corrigida.

**ATUALIZE O STATUS DA NOTA FISCAL**

O processo para atualização da nota fiscal é de aproximadamente cinco minutos.

Para antecipar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu → Vendas → Notas Fiscais, insira o número do pedido em: ID Pedido/Venda e clique em: Aplicar Filtro:

![Imagem 12: Para antecipar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-39.png)

A nota estará processando autorização:

![Imagem 13: A nota estará processando autorização:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-41.png)

Neste caso, clique em: Ações → Atualizar Status:

![Imagem 14: Neste caso, clique em: Ações → Atualizar Status:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-43-1024x170.png)

Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido novamente:

![Imagem 15: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-45-1024x294.png)
![Imagem 16: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-46-1024x65.png)

Se estiver errada, voltará a mensagem de erro de autorização.

![Imagem 17: Se estiver errada, voltará a mensagem de erro de autorização.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-44-1024x144.png)

Neste caso, orientamos que procure a equipe de suporte.
