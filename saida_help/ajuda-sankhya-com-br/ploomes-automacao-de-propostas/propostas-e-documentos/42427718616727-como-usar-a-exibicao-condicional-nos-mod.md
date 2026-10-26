---
id: "42427718616727"
titulo: "Como usar a exibição condicional nos modelos de proposta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427718616727-Como-usar-a-exibi%C3%A7%C3%A3o-condicional-nos-modelos-de-proposta"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:08:26Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452295", "sync_hash_d29b3ae68351"]
---

# Como usar a exibição condicional nos modelos de proposta

Como fazer com que um texto ou campo apareça na proposta dependendo de condições

Digamos que eu tenha um modelo que mostre a descrição dos meus produtos debaixo de um texto "Descrição:", mas alguns produtos não têm descrição e o campo vem vazio.
Nesse caso, quero que não apareça escrito "Descrição" se o campo [Produto.Descrição] for vazio (nulo).
Posso fazer isso pela edição normal do modelo ou pelo HTML.

**Criando condicionais pelo editor:**

[![Imagem 1: Criando condicionais pelo editor:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328205/6e7fc1050aa0f12592114c91/image.png-expires%3D1619528400-signature%3D22bffa64b8173a6c42b1ff57718c6342f3cd17963e61c9f8ad379aec902d1a11?expires=1786536000&signature=16c90d973ed548f4d11220fad23a9cbdd0207d38d331c090f1c47d1cc666d4d2&req=dyYuFct2n4FaFb4V1XW4gfN49UadCrq%2BkxKmYHSC2Gv%2FjdKZ1SSYpl726v6c%0AwFjV71yGgXlD6yzSOqV0i57yZQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/157879094/795b8bd17fa1aabde267e6ae/image.png?expires=1619528400&signature=22bffa64b8173a6c42b1ff57718c6342f3cd17963e61c9f8ad379aec902d1a11)

Seleciono a parte que quero que tenha a condicional e clico com o botão direito:

[![Imagem 2: Seleciono a parte que quero que tenha a condicional e clico com o botão direito:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328210/61d3a028154122375dc065ca/image.png-expires%3D1619528400-signature%3D011d05160c666b21cddc5457efd0cd02d546def14aab2368baa4600e95bc3f45?expires=1786536000&signature=780fc16327d82726fc0e269eedac088dd38414abfccad9bfea7d14805efa9d63&req=dyYuFct2n4BfFb4V1XW4gVWxTRMjTAvrG385UsuXXqMORpifRkrkXtws%2BBWD%0AiUELucocUCYWWFliG3YdSQRx2Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/157879201/0918ff623f9dc819700a4a10/image.png?expires=1619528400&signature=011d05160c666b21cddc5457efd0cd02d546def14aab2368baa4600e95bc3f45)

Clico depois em Exibição condicional:

[![Imagem 3: Clico depois em Exibição condicional:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328217/097970a27c999ace42ea0daf/image.png-expires%3D1619528400-signature%3D4189a58d330441d56ac3887d7735263dbb1d96f42bea811c4e83591f080f7c45?expires=1786536000&signature=3356e5a79aef8395c4ab2dea54d4aa99b8ffea947a0c2f547b110f85e85133b3&req=dyYuFct2n4BYFb4V1XW4gZgKIByePqOQOqTA2u8Fq6xW8Dgtih4ZzJ%2BdeeqA%0AmqeIkQ2YGVC3hxxczpminaLHEA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/157879531/149681a066be2c4b82abb937/image.png?expires=1619528400&signature=4189a58d330441d56ac3887d7735263dbb1d96f42bea811c4e83591f080f7c45)

A ideia dessa condição é "Mostrar dados se chegar à condição"

[![Imagem 4: A ideia dessa condição é "Mostrar dados se chegar à condição"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328226/394fb4d981871547bffe75d2/cond.gif-expires%3D1619528400-signature%3D0c104b38c9ca93709381d0b7b537110a77f87e0708d7f53e9a8f9d201d7fdf38?expires=1786536000&signature=5528f46637e218361bb443c3eb788b453185eb6ca2e859b27d0422ef7f8f3af7&req=dyYuFct2n4NZFb4V1XW4gTw4JWOPdKePi7yfz%2FwO8xV9phqi1hBQRQQhFI6%2B%0AR7b6ZBPSZ5ybK3h4zKDRG10%2BoA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/157880184/229a17c43348d7e7a93aa974/cond.gif?expires=1619528400&signature=0c104b38c9ca93709381d0b7b537110a77f87e0708d7f53e9a8f9d201d7fdf38)

Naveguei até o campo descrição e adicionei a condição.
Note como ficou verde o entorno da parte afetada. O verde claro indica uma condicional.

**Editando condicionais pelo código-fonte:**A tag de condicional vem dentro de um span ou div, e é assim:

condition-field-key="[CHAVE DO CAMPO]" condition-operation="[OPERAÇÃO]" condition-value="[VALOR]"

Agora vamos substituir os valores:
[CHAVE DO CAMPO] é a chave encontrada entre as tags <field> e </field>. No caso da descrição, encontro assim:

[![Imagem 5: condition-field-key="(CHAVE DO CAMPO)" condition-operation="(OPERAÇÃO)" condition-value="(VALOR)" Agora vamos…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369328232/ee3e675811fa172f25d1cb3f/key.gif-expires%3D1619528400-signature%3D5e89e38deda3487277030c3075391e32b339f16247ab3ce05278c054acc77ffc?expires=1786536000&signature=b6c93b4ecfdea48b5afdc0151da414b0097c12ff0ce0ad5d3bd371df9608ad9e&req=dyYuFct2n4JdFb4V1XW4gUBG6F3FTuK4fPDu04MeUfGvY2EdqO%2FBOw15oEdO%0AIvtAPiYgORPGE1qy4nvRXo0Lcg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/157882570/25ab4fe3f3dce2fb4d7632a9/key.gif?expires=1619528400&signature=5e89e38deda3487277030c3075391e32b339f16247ab3ce05278c054acc77ffc)

Copiei e colei, agora tenho product\_479FD0EF-980A-44ED-ACFC-514D5CF1AA3B.
[OPERAÇÃO] vou substituir por um desses:

- eq (igual a)

- ne (diferente de)

- gt (maior que)

- ge (maior ou igual)

- lt (menor que)

- le (menor ou igual)

Como quero que seja diferente de vazio, vou escolher "ne"

Em [VALOR] vou preencher com o valor que minha condicional tem que atingir. Como quero diferente de vazio, vou preencher com null (nulo). A linha com condicional fica assim:
<p ><span condition-field-key="product\_479FD0EF-980A-44ED-ACFC-514D5CF1AA3B" condition-operation="ne" condition-value="null">Descrição:</span></p>
