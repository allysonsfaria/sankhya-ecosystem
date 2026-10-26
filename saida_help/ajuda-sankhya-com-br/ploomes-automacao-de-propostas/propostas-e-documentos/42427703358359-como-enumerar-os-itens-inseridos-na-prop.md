---
id: "42427703358359"
titulo: "Como enumerar os itens inseridos na proposta e na venda."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427703358359-Como-enumerar-os-itens-inseridos-na-proposta-e-na-venda"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:08:27Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452301", "sync_hash_1565d9e58e3f"]
---

# Como enumerar os itens inseridos na proposta e na venda.

Nesse artigo mostro como configurar a proposta e a venda, para que os itens inseridos nela sigam um índice.

O primeiro passo seria selecionar o modelo de proposta onde você deseja configurar esse índice. Em administração > modelos e documentos > acessar o modelo da proposta.

No modelo, o primeiro passo será criar um campo na entendida Proposta, como evidenciado abaixo:

[![Imagem 1: No modelo, o primeiro passo será criar um campo na entendida Proposta, como evidenciado abaixo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328546/d1b53b5937918db4d558e8dc/NewGIF%2B-281-29.gif-expires%3D1619460000-signature%3Dd6332f912622e73b30220605c84beb08b52900ca6c11b2292828ad7cfda08d09?expires=1786536000&signature=941f2bc65f192d03ca7cd950d9da648c3568b81bcdbb560e5aaa84dc55704e7d&req=dyYuFct2mIVZFb4V1XW4gVcFwPpTWCuQs3JVflPmTmmxuKmb0cEWikFO8zSJ%0AjpHVcCj5j6kKopT20KCRPstUAQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258932659/60cbb2eff7bf257c80512fec/NewGIF+%281%29.gif?expires=1619460000&signature=d6332f912622e73b30220605c84beb08b52900ca6c11b2292828ad7cfda08d09)

As configurações do campo podem estar restritas para edição e ocultas do formulário, pois não é necessário o preenchimento na criação da proposta.

Inserimos o campo criado acima do campo nome do produto (ou no local onde você gostaria que essa informação seja preenchida certinha).

Com esse campo criado, vamos acessar o código fonte da proposta:

[![Imagem 2: Com esse campo criado, vamos acessar o código fonte da proposta:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328557/565e50df9448bd4e7a35af5f/image.png-expires%3D1619460000-signature%3Df646946cf5f409896abf402ef456baae5e6a0a7c68a653b81af449efef41d0f2?expires=1786536000&signature=0e3acc72babb12d71aeafea5249a64008455edd2691b6ff6ce139d1cbb47f3f5&req=dyYuFct2mIRYFb4V1XW4gcmmVYpE3wYV%2F4tGKubeVOUlHijszoxdBxqo1kFw%0AEY69pvC9JyqTQ%2BUzzKAqiT5k4A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258933883/c63e673e1d2a473a51a49014/image.png?expires=1619460000&signature=f646946cf5f409896abf402ef456baae5e6a0a7c68a653b81af449efef41d0f2)

Legenda:

1 - O campo criado que servirá para a criação do índice.

2- Onde acessar o código fonte.

Acessando p código fonte, vamos procurar pelo campo criado. Você pode usar um atalho de pesquisa (Ctrl + F) e digitar o campo criado, localizando-o certinho.

[![Imagem 3: Acessando p código fonte, vamos procurar pelo campo criado. Você pode usar um atalho de pesquisa (Ctrl + F) e digitar o…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328565/4ba669107c41f0aeec87baa6/image.png-expires%3D1619460000-signature%3D141e23c261d598c8690f3d4ff2be704f08b29fbcf8e1c63aae06a4dbb2a43f4c?expires=1786536000&signature=9b4d63c45a0c4085e193a3bf1a7514aa274937d7587675e8af99c2faf62c32f0&req=dyYuFct2mIdaFb4V1XW4gRcvtG02F5E0pAa2MREz%2BcI4I57u2%2BnEf5MkLVOD%0AFNjWzYtbUeWbe9PCmYIbfizVhg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258936203/c64493c55f85cee7ad292281/image.png?expires=1619460000&signature=141e23c261d598c8690f3d4ff2be704f08b29fbcf8e1c63aae06a4dbb2a43f4c)

A caixinha 1, representa onde a pesquisa abrindo o atalho irá abrir.

Deve-se atentar ao que foi sublinhando em amarelo, que representa as linhas na tabela.

O próximo passo será localizar onde vamos inserir a fórmula que irá fazer essa enumeração.

Irei inserir acima do campo de nome, para que essa informação venha primeiro.

[![Imagem 4: Irei inserir acima do campo de nome, para que essa informação venha primeiro.](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328571/e8e6b09191fb5bd2bbd4f97a/image.png-expires%3D1619460000-signature%3D1ef1f7fb09a387ceca9b426fd716ffe38cec38ac1c32c97455f1879ce7bd5a56?expires=1786536000&signature=da1782cd75de1055e7365f576057018837552ba511943aa46282f1b890c93297&req=dyYuFct2mIZeFb4V1XW4gdnuB7f5c%2BQZ3tjCy7iZB5rAv7nhaVquxL9M2O33%0AklUK2Q6MbYhOqdrM5KyUgVN8vA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258941561/f7183d317f4701d4006db32e/image.png?expires=1619460000&signature=1ef1f7fb09a387ceca9b426fd716ffe38cec38ac1c32c97455f1879ce7bd5a56)

O item 1 mostra o paragrafo onde está meu campo de nome e o campo criado de Numeração do Item.

Já o item 2, mostra a formula a ser inserida **entre <td> e </td>**, apresentada abaixo:

<index field-key="quote\_section\_products"> **inserir aqui o campo criado para a numeração** </index>

OBS: para realizar essa alteração em um documento de venda, a fórmula está ao fim do artigo.

Com esse inserção realizada, basta apertar em "OK" para salvar a alteração na formula.

Quando a aba de código fonte for fechada salvando a alteração, você irá notar que agora temos dois campos de Numeração do Item.

Com isso, podemos deletar do tabela o campo que possui o fundo vermelho, deixando apenas o que possui fundo rosa e borda amarela, conforme GIF e imagem abaixo.

[![Imagem 5: Com isso, podemos deletar do tabela o campo que possui o fundo vermelho, deixando apenas o que possui fundo rosa e…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328576/b728354671b67eadffc1e68c/art2.gif-expires%3D1619460000-signature%3D65256218eb62f26eb756f9fb800224af0ab33ccab66733b750547b9907592a3f?expires=1786536000&signature=9d50dc4afda4bc39630f0f21ea1b801a6c6b33d50bc5db4eea57387ae00df18f&req=dyYuFct2mIZZFb4V1XW4gRDtOOzH4j6Cmfg7l%2BkHJfLkBwnPcIpiND7g8%2B1V%0ASW%2F6X3spLlwSgR1l8%2FlKWHQgyQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258942515/8826cc5ded7f0e5329fb5b63/art2.gif?expires=1619460000&signature=65256218eb62f26eb756f9fb800224af0ab33ccab66733b750547b9907592a3f)

[![Imagem 6: Com isso, podemos deletar do tabela o campo que possui o fundo vermelho, deixando apenas o que possui fundo rosa e…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328583/d99eb052f2c6625a3665e242/image.png-expires%3D1619460000-signature%3Dc5761b6b2c5b9d70ea8cc52fe376ffbe015bed021ee0a570843a8919e2540491?expires=1786536000&signature=a89dcb6999a54a075ec21ae3ff07d243ccf95974aafdee435f740bd930300f6b&req=dyYuFct2mIlcFb4V1XW4gdY7WVVH4%2Fa9hpJsHYWthLSRuiB3T7Qg%2FQXrobgE%0AfwSjJA0s%2BEPstI7460bVKIIcDA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258943156/0a958e63597a90002fdf7dad/image.png?expires=1619460000&signature=c5761b6b2c5b9d70ea8cc52fe376ffbe015bed021ee0a570843a8919e2540491)

Ao final, basta salvar a proposta no canto superior direito e testar gerando uma proposta com o modelo que foi alterado.

Com as configurações certinhas, esse será o resultado:

[![Imagem 7: Com as configurações certinhas, esse será o resultado:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328594/4e00502fff713c72029d3da5/image.png-expires%3D1619460000-signature%3D47ac74b395b77bda5c02847b2c3071dc38540d62e487b6a67c8de1c8214e08f7?expires=1786536000&signature=2cf39cc7115a00b729b6df5f6692b2fff72d7afc6893bcdebcfd8377b8b3892c&req=dyYuFct2mIhbFb4V1XW4gcEgYcwallKlvkgYoazI2Elt22UF59Jd4nJLF3rW%0AhtIYPwtz0mJ9SSGwWPuXcNpxSw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/258943984/39cf7e46b1be27b116a84115/image.png?expires=1619460000&signature=47ac74b395b77bda5c02847b2c3071dc38540d62e487b6a67c8de1c8214e08f7)

OBS: Para aparecer na mesma linha, e não uma informação abaixo da outra, basta inserir os campos na mesma linha na edição do modleo da proposta.

Para alterar essa informação em uma venda, o passo a passo será o mesmo, porém a fórmula será a seguinte:

<index field-key="order\_section\_products">**inserir aqui o campo criado para a numeração**</index>
