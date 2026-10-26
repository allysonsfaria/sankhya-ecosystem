---
id: "44012267261975"
titulo: "Como corrigir o erro \"o campo unidade_comercial é obrigatório\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012267261975-Como-corrigir-o-erro-o-campo-unidade-comercial-%C3%A9-obrigat%C3%B3rio"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:23Z"
rotulos: ["sync_hc", "magis5", "magis5_204048360254", "sync_hash_ef9fbecadee7"]
---

# Como corrigir o erro "o campo unidade_comercial é obrigatório"

## Este erro significa que, ao criar a NF-e para um produto, o campo que indica a unidade de medida comercial (unidade\_comercial) não foi preenchido, embora seja um campo obrigatório de acordo com as normas fiscais.

Para resolver esse erro, iremos demonstrar um passo-a-passo com o produto "Escada Articulada de Alumínio". Você pode considerar as seguintes etapas:

### Verifique os itens que fazem parte da Venda.

Na tela de pedidos, clique em: Visualizar Pedido/Venda:

![Imagem 1: Na tela de pedidos, clique em: Visualizar Pedido/Venda:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-84.png)

Nos detalhes do pedido, copie o ID do produto:

![Imagem 2: Nos detalhes do pedido, copie o ID do produto:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-85.png)

No menu, clique em Cadastros → Produtos, insira o ID do produto no campo “ID/SKU” e clique em: Aplicar Filtros:

![Imagem 3: No menu, clique em Cadastros → Produtos, insira o ID do produto no campo “ID/SKU” e clique em: Aplicar Filtros:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-86.png)

Analise todo o cadastro fiscal do produto na aba Fiscal.

No exemplo abaixo, o campo NCM e a Origem da Mercadoria precisavam ser preenchidos:

![Imagem 4: No exemplo abaixo, o campo NCM e a Origem da Mercadoria precisavam ser preenchidos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-88-1024x215.png)

Após validar e corrigir o cadastro do produto, clique em: Salvar.

---

### Emita a Nota Fiscal Manual

### Após o ajuste do cadastro do cliente, é necessário editar a tentativa de emissão da NFe.

Na tela de vendas, clique em: Emitir NF-e Manual:

![Imagem 5: Na tela de vendas, clique em: Emitir NF-e Manual:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-34-1024x129.png)

Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione consumidor final:

![Imagem 6: Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione consumidor final:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-67-1024x145.png)

Preencha “Operação”, da nota fiscal:

![Imagem 7: Preencha “Operação”, da nota fiscal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-68-1024x190.png)

Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:

![Imagem 8: Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-37.png)

Caso haja alguma inconsistência, será exibido um pop-up com uma mensagem de erro.

Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:

![Imagem 9: Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-38.png)

Pronto, a nota está corrigida.

---

### Atualize os status da Nota Fiscal

### O processo para atualização da nota fiscal é de aproximadamente cinco minutos.

Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu → Vendas → Notas Fiscais, insira o número do pedido em: ID Pedido/Venda e clique em: Aplicar Filtro:

![Imagem 10: Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-39.png)

A nota estará processando autorização:

![Imagem 11: A nota estará processando autorização:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-41.png)

Neste caso, clique em: Ações → Atualizar Status:

![Imagem 12: Neste caso, clique em: Ações → Atualizar Status:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-43-1024x170.png)

Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido novamente:

![Imagem 13: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-45-1024x294.png)
![Imagem 14: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-46-1024x65.png)

Se estiver errada, voltará a mensagem de erro de autorização.

![Imagem 15: Se estiver errada, voltará a mensagem de erro de autorização.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-44-1024x144.png)

Neste caso, orientamos que procure a equipe de suporte.
