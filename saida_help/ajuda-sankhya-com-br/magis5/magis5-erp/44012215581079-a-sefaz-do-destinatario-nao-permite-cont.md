---
id: "44012215581079"
titulo: "A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012215581079-A-SEFAZ-do-destinat%C3%A1rio-n%C3%A3o-permite-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:21Z"
rotulos: ["sync_hc", "magis5", "magis5_204048108328", "sync_hash_25d49d73e1c9"]
---

# A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual

## Este erro significa que a Secretaria da Fazenda (SEFAZ) do estado do destinatário da nota fiscal não permite que empresas ou destinatários que são isentos da obrigação de possuir uma Inscrição Estadual (IE) sejam tratados como contribuintes.

### Consulte o Cadastro de clientes

O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:

![Imagem 1: O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:](https://ajuda.sankhya.com.br/hc/article_attachments/44012250700183)

No menu, clique em Cadastros → Clientes e busque pelo cliente:

![Imagem 2: No menu, clique em Cadastros → Clientes e busque pelo cliente:](https://ajuda.sankhya.com.br/hc/article_attachments/44012224429847)

![Imagem 3: No menu, clique em Cadastros → Clientes e busque pelo cliente:](https://ajuda.sankhya.com.br/hc/article_attachments/44012204801687)

Clique em: Editar:

![Imagem 4: Clique em: Editar:](https://ajuda.sankhya.com.br/hc/article_attachments/44012223200023)

Em "Informações Principais", analise o cadastro do cliente. No exemplo abaixo, o campo IE não está preenchido:

![Imagem 5: Em "Informações Principais", analise o cadastro do cliente. No exemplo abaixo, o campo IE não está preenchido:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-69.png)

O não preenchimento da Inscrição Estadual pode significar que o cliente é Isento de IE ou que este campo não foi preenchido no momento do cadastro. Portanto, será necessário validar essa situação utilizando o [Sintegra](http://www.sintegra.gov.br/) ou o [Portal da Nota Fiscal Eletrônica](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc). Com o CNPJ em mãos, busque os dados do cliente:

![Imagem 6: O não preenchimento da Inscrição Estadual pode significar que o cliente é Isento de IE ou que este campo não foi…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-75.png)

Ao pesquisar o CNPJ do cliente, não é localizada a Inscrição Estadual, confirmando a informação que o cliente é isento:

![Imagem 7: Ao pesquisar o CNPJ do cliente, não é localizada a Inscrição Estadual, confirmando a informação que o cliente é isento:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-64.png)

Voltando no cadastro do cliente no Magis5 ERP, na aba Dados Fiscais, ajuste os seguintes campos:

![Imagem 8: Voltando no cadastro do cliente no Magis5 ERP, na aba Dados Fiscais, ajuste os seguintes campos:](https://ajuda.sankhya.com.br/hc/article_attachments/44012251039255)

Contribuinte ICMS: Marque não, visto que a Sefaz do destinatário não permite que empresas isentas de IE sejam tratadas como contribuintes.

Isento da I.E: Marque sim, visto que o cliente não possui Inscrição Estadual.

Após validar essas informações, clique em: Salvar.

---

### Emita a Nota Fiscal Manual

### Após o ajuste do cadastro do cliente, é necessário editar a tentativa de emissão da NFe.

### Na tela de vendas, clique em: Emitir NF-e Manual:

![Imagem 9: Na tela de vendas, clique em: Emitir NF-e Manual:](https://ajuda.sankhya.com.br/hc/article_attachments/44012237493783)

Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione consumidor final:

![Imagem 10: Na Visualização da Nota Fiscal, no campo “Consumidor Final”, selecione consumidor final:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-67-1024x145.png)

Preencha “Operação”, da nota fiscal:

![Imagem 11: Preencha “Operação”, da nota fiscal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-68-1024x190.png)

Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:

![Imagem 12: Após inserir a informação correta, clique em: Atualizar Informações e Recalcular Impostos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-37.png)

Caso haja alguma inconsistência, será exibido um pop-up com uma mensagem de erro.

Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:

![Imagem 13: Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-38.png)

Pronto, a nota está corrigida.

---

### Atualize o Status da Nota Fiscal

O processo para atualização da nota fiscal é de aproximadamente cinco minutos.

Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu → Vendas → Notas Fiscais, insira o número do pedido em: ID Pedido/Venda e clique em: Aplicar Filtro:

![Imagem 14: Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.sankhya.com.br/hc/article_attachments/44012223508375)

![Imagem 15: Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.sankhya.com.br/hc/article_attachments/44012251315095)

A nota estará processando autorização:

![Imagem 16: A nota estará processando autorização:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-41.png)

Neste caso, clique em: Ações → Atualizar Status:

![Imagem 17: Neste caso, clique em: Ações → Atualizar Status:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-43-1024x170.png)

Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido novamente:

![Imagem 18: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.sankhya.com.br/hc/article_attachments/44012237793687)
![Imagem 19: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-46-1024x65.png)

Se estiver errada, voltará a mensagem de erro de autorização.

![Imagem 20: Se estiver errada, voltará a mensagem de erro de autorização.](https://ajuda.sankhya.com.br/hc/article_attachments/44012237888791)

Neste caso, orientamos que procure a equipe de suporte.
