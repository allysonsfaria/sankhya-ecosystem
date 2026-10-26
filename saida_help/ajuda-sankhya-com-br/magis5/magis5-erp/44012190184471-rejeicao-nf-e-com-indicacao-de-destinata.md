---
id: "44012190184471"
titulo: "Rejeição: NF-e com indicação de destinatário isento de IE, com a informação da IE do destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012190184471-Rejei%C3%A7%C3%A3o-NF-e-com-indica%C3%A7%C3%A3o-de-destinat%C3%A1rio-isento-de-IE-com-a-informa%C3%A7%C3%A3o-da-IE-do-destinat%C3%A1rio"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:23:06Z"
rotulos: ["sync_hc", "magis5", "magis5_204056240161", "sync_hash_69b297af388f"]
---

# Rejeição: NF-e com indicação de destinatário isento de IE, com a informação da IE do destinatário

## Este erro significa que a NF-e foi emitida com o campo da Inscrição Estadual (IE) do Destinatário preenchido e nas informações fiscais do cliente está informando que o contribuinte é isento de Inscrição Estadual (IE).

**Consulta e Corrija o Cadastro de Cliente**

O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:

![Imagem 1: O primeiro passo é identificar o cadastro do cliente. Na tela de pedidos, copie o nome do cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-49-1024x104.png)

No menu, clique em Cadastros → Clientes e busque pelo cliente:

![Imagem 2: No menu, clique em Cadastros → Clientes e busque pelo cliente:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-50.png)

Clique em: Editar:

![Imagem 3: Clique em: Editar:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-51.png)

Em "Informações Principais", veja se o campo IE está preenchido:

![Imagem 4: Em "Informações Principais", veja se o campo IE está preenchido:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-60.png)

Na aba "Dados Fiscais", atente-se aos seguintes campos:

![Imagem 5: Na aba "Dados Fiscais", atente-se aos seguintes campos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-56.png)

Considerando que o cliente é PJ e possui IE preenchida, será necessário verificar o preenchimento dos seguintes campos:

Contribuinte ICMS: Marque sim, visto que o cliente é Pessoa Jurídica (PJ) e consequentemente, Contribuinte ICMS.

Isento da I.E: Marque não, visto que o cliente possui um número de IE preenchido em seu cadastro.

Após corrigir essas informações, clique em: Salvar.

---

### Emita a Nota Fiscal Manual

Após a correção do cadastro do cliente, é necessário editar a tentativa de emissão da NF-e.

Na tela de vendas, clique em: Emitir NF-e Manual:

![Imagem 6: Na tela de vendas, clique em: Emitir NF-e Manual:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-34-1024x129.png)

Na Visualização da Nota Fiscal, no campo "Consumidor Final", selecione normal:

![Imagem 7: Na Visualização da Nota Fiscal, no campo "Consumidor Final", selecione normal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-61-1024x171.png)

Preencha "Operação", da nota fiscal:

![Imagem 8: Preencha "Operação", da nota fiscal:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-62-1024x358.png)

Após inserir as informações corretas, clique em: Atualizar Informações e Recalcular Impostos:

![Imagem 9: Após inserir as informações corretas, clique em: Atualizar Informações e Recalcular Impostos:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-37.png)

Caso haja alguma inconsistência, será exibido um pop-up com uma mensagem de erro.

Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:

![Imagem 10: Caso esteja correto, não será exibida nenhuma mensagem. Clique em: Transmitir NF-e:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-38.png)

Pronto, a nota está corrigida.

---

### Atualize o Status da Nota Fiscal

O processo para atualização da nota fiscal é de aproximadamente cinco minutos.

Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu → Vendas → Notas Fiscais, insira o número do pedido em: ID Pedido/Venda e clique em: Aplicar Filtro:

![Imagem 11: Para adiantar este processo, é possível atualizar o status da nota fiscal de forma manual. Para isso, acesse: Menu →…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-39.png)

A nota estará processando autorização:

![Imagem 12: A nota estará processando autorização:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-41.png)

Neste caso, clique em: Ações → Atualizar Status:

![Imagem 13: Neste caso, clique em: Ações → Atualizar Status:](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-43-1024x170.png)

Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido novamente:

![Imagem 14: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-45-1024x294.png)
![Imagem 15: Se a correção estiver correta, a nota fiscal irá sumir da tela e será necessário localizar pelo número do pedido…](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-46-1024x65.png)

Se estiver errada, voltará a mensagem de erro de autorização.

![Imagem 16: Se estiver errada, voltará a mensagem de erro de autorização.](https://ajuda.artemis5.com.br/wp-content/uploads/sites/2/2023/09/image-44-1024x144.png)

Neste caso, orientamos que procure a equipe de suporte.
