---
id: "44012190055319"
titulo: "Rejeição: Operação com não contribuinte deve indicar operação com consumidor final"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012190055319-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-n%C3%A3o-contribuinte-deve-indicar-opera%C3%A7%C3%A3o-com-consumidor-final"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:04Z"
rotulos: ["sync_hc", "magis5", "sync_hash_8fb6e947a243", "magis5_204056246810"]
---

# Rejeição: Operação com não contribuinte deve indicar operação com consumidor final

## Este erro ocorre durante a tentativa de emissão da nota fiscal, quando o destinatário é PJ (ou seja, possui um CNPJ), porém, no seu cadastro, o cliente está classificado como "Não Contribuinte ICMS".

### Consulta e Corrija o Cadastro de Cliente

O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:

![Imagem 1: O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-49-1024x104.png)

No menu, clique em **Cadastros → Clientes** e busque pelo cliente:

![Imagem 2: No menu, clique em Cadastros → Clientes e busque pelo cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-50.png)

Clique em **"Editar"**:

![Imagem 3: Clique em "Editar" :](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-51.png)

Em "Informações Principais", analise o cadastro do cliente:

![Imagem 4: Em "Informações Principais", analise o cadastro do cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-57.png)

Neste momento, é interessante validar a Inscrição Estadual no cadastro do cliente (caso não esteja preenchido). Para conferir, utilizando o [Sintegra](http://www.sintegra.gov.br/) ou o [Portal da Nota Fiscal Eletrônica](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc), com o CNPJ em mãos, busque os dados do cliente:

![Imagem 5: Neste momento, é interessante validar a Inscrição Estadual no cadastro do cliente (caso não esteja preenchido). Para…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-76.png)

Ao pesquisar, os dados do cliente são exibidos:

![Imagem 6: Ao pesquisar, os dados do cliente são exibidos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-78.png)

Caso o cliente possua Inscrição Estadual, insira-a no cadastro do cliente:

![Imagem 7: Caso o cliente possua Inscrição Estadual, insira-a no cadastro do cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-55.png)

Caso o cliente não possua Inscrição Estadual, deixe o campo em branco.

Na aba "Dados Fiscais", atente-se aos seguintes campos:

![Imagem 8: Na aba "Dados Fiscais", atente-se aos seguintes campos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-56.png)

Contribuinte ICMS: Marque sim, visto que o cliente é Pessoa Jurídica (PJ) e consequentemente, Contribuinte ICMS.

Isento da I.E:

1. Marque sim caso o cliente não possua Inscrição estadual e,
2. Marque não caso o cliente possua inscrição estadual.

Após validar essas informações, clique em: Salvar.

---

### Emita a Nota Fiscal Manual

Após a correção do cadastro do cliente, é necessário editar a tentativa de emissão da NF-e.

Na tela de vendas, clique em: Emitir NF-e Manual:

![Imagem 9: Na tela de vendas, clique em: Emitir NF-e Manual:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-34-1024x129.png)

Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione normal:

![Imagem 10: Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione normal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-71-1024x157.png)

Preencha “Operação”, da nota fiscal:

![Imagem 11: Preencha “Operação”, da nota fiscal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-72.png)

Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:

![Imagem 12: Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-37.png)

Caso haja alguma inconsistência, será exibido um pop-up com uma mensagem de erro.

Caso esteja correto, não será exibida nenhuma mensagem. Clique em: **Transmitir NF-e**:

![Imagem 13: Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e :](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-38.png)

Pronto, a nota está corrigida.

---

### Atualize o Status da Nota Fiscal

O processo para atualização da nota fiscal é de aproximadamente cinco minutos.

Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu → Vendas → Notas Fiscais, insira o número do pedido em: ID Pedido/Venda e clique em: Aplicar Filtro:

![Imagem 14: Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-39.png)

A nota estará processando autorização:

![Imagem 15: A nota estará processando autorização:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-41.png)

Neste caso, clique em: Ações → Atualizar Status:

![Imagem 16: Neste caso, clique em: Ações → Atualizar Status:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-43-1024x170.png)

Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido novamente:

![Imagem 17: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-45-1024x294.png)
![Imagem 18: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-46-1024x65.png)

Se estiver errada, voltará a mensagem de erro de autorização.

![Imagem 19: Se estiver errada, voltará a mensagem de erro de autorização.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-44-1024x144.png)

Neste caso, orientamos que procure a equipe de suporte.
