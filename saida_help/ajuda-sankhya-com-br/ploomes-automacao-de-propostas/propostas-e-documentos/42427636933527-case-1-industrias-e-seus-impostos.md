---
id: "42427636933527"
titulo: "Case #1: Indústrias e seus impostos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427636933527-Case-1-Ind%C3%BAstrias-e-seus-impostos"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:14:12Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452306", "sync_hash_4ec77d21f1d0"]
---

# Case #1: Indústrias e seus impostos

Como adaptar o seu modelo de proposta comercial de acordo com o seu segmento e ramo de atuação.

Primeiramente, antes de prosseguir com a leitura desse case, recomendamos que você leia [esse](https://sankhya.zendesk.com/hc/pt-br/articles/42427521647383) artigo, onde explicamos teoricamente o que são somatórios, condicionais, fórmulas, filtros nos grupos de produto e campos escondidos no seu modelo de proposta.

Dito isso, vamos começar a explorar esse primeiro caso de uso das propostas comerciais dentro do Ploomes.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
**O que você vai encontrar nesse artigo?**

- ICMS (simples) – Como calcular esse imposto nas suas negociações?
- IPI – Como adequar as variações desse imposto nos seus diferentes produtos?
- Um exemplo prático de como montar o seu modelo de proposta

## ICMS

O ICMS é um imposto condicional, isto é, depende da origem e do destino da mercadoria. Nesse artigo, vamos estudar um caso onde a alíquota do ICMS não varie de acordo com as mercadorias, apenas com a rota de transporte do produto ou serviço. Veja a tabela com todas as alíquotas em porcentagem do ICMS no Brasil.

[![Imagem 1: O ICMS é um imposto condicional, isto é, depende da origem e do destino da mercadoria. Nesse artigo, vamos estudar um…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329669/46210f1980da4ffa57ae1e60/image.png-expires%3D1619632800-signature%3D8928d7cf623171c7788b410fd3e695297293f6f80e3335e63dd644f857160a20?expires=1786536000&signature=fcbeb49e1d38c724a321af1caf1c27837ccc53f807fdcdb1fc4e981f1c4ceee5&req=dyYuFct3m4dWFb4V1XW4gRuESNWRFin7wnOLmtTtbO7Hn5nDf2erYM%2B5GSCB%0A4LUd0Oz0BnCMvUhm5xSw18QsLQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69622689/f53cfc948df16b7c77e318d8/image.png?expires=1619632800&signature=8928d7cf623171c7788b410fd3e695297293f6f80e3335e63dd644f857160a20)

Fonte: <https://blog.sage.com.br/tabela-icms-2018-atualizada/>

Para fins didáticos, vamos imaginar que a sua empresa tenha sede em SP, e venda produtos apenas para os estados de SP e RJ.

Sabendo disso, temos duas formas de calcular esse ICMS:
Quando a alíquota depende apenas da origem e do destino das nossas vendas ou quando ela varia com a mercadoria. Em um outro artigo, iremos trazer a lógica do ICMS aplicada a variância da alíquota por mercadoria.

Dito isso, de acordo com a tabela, se vendermos para um cliente de SP, o ICMS aplicado é de 18%. Se o cliente for do RJ, essa alíquota é de 12%.

## Vamos ver como isso funciona dentro do Ploomes!

Para que você se familiarize com os modelos de proposta, leia esse artigo antes de prosseguir.

O primeiro passo é criar um campo na sua proposta, visto que a alíquota nesse caso depende apenas da rota do transporte, chamado "ICMS" do tipo "porcentagem".

[![Imagem 2: O primeiro passo é criar um campo na sua proposta, visto que a alíquota nesse caso depende apenas da rota do…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329676/9f05d987dc91c50bd3af11b2/image.png-expires%3D1619632800-signature%3Dba1c7457df72dd7d4db86b27eec14fcf970ec624a312262af36fffad1b730788?expires=1786536000&signature=fd9eb410b4775b019190c1951195f21c4adb58a24ba1ab25d908f1711258e334&req=dyYuFct3m4ZZFb4V1XW4gZgNKsWJVOfH%2BHIGs5ST8DL03BgmkLElVx8SifnL%0ALHBbWR9Em%2B1UEAc%2BeTNnYCyL%2Bg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69771554/08b4f3d76da6556b6c04c21a/image.png?expires=1619632800&signature=ba1c7457df72dd7d4db86b27eec14fcf970ec624a312262af36fffad1b730788)

Como sabemos que o valor desse campo varia de acordo com o endereço do cliente, precisamos criar uma fórmula condicional desse tipo:

[![Imagem 3: Como sabemos que o valor desse campo varia de acordo com o endereço do cliente, precisamos criar uma fórmula…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329686/bb040626029ce01cd67743c9/image.png-expires%3D1619632800-signature%3Db67bb329246a51111b7be8b1d72c3bcdee14e72d1b1a81dd588436b1c18d73fa?expires=1786536000&signature=a90a127f8e17bf356476f6081c533dd7e0f3411c3ed37f2e6f39848f748bd959&req=dyYuFct3m4lZFb4V1XW4gTrlHoLiqEegRsbFiX3dOtsaArfA89ZqPnAtbCOj%0A4a4dHmonBpk6yu3J0SUymvKTvQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69772617/fbc147b72dc55a0ba0dd8813/image.png?expires=1619632800&signature=b67bb329246a51111b7be8b1d72c3bcdee14e72d1b1a81dd588436b1c18d73fa)

**Obs.:** dê zoom (Control +) para poder visualizar melhor

Para confirmar, vamos criar negócios com clientes de São Paulo e com clientes do Rio de Janeiro.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=bsfFcL7HsDY)

Vemos que ao selecionar um cliente do RJ, o ICMS automaticamente resulta em 12%, e ao selecionar um cliente de SP, 18%.

Agora, precisamos fazer com que o Ploomes calcule o VALOR do ICMS. Para isso, vamos criar um campo chamado "Valor ICMS" no seu modelo.

[![Imagem 4: Agora, precisamos fazer com que o Ploomes calcule o VALOR do ICMS. Para isso, vamos criar um campo chamado "Valor ICMS"…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329693/7a2b5720324fc6889e297067/image.png-expires%3D1619632800-signature%3D1c00ac111c96a408329bddda72045e623d5c76d6a76a8ada2793791fee0ecc6c?expires=1786536000&signature=7be9d9f4a3537711fe2adeca049a7adb6ef600e3bffbdf4c0f540b6487e9a3f5&req=dyYuFct3m4hcFb4V1XW4gXjV99ZqWkjMYgcAySIambqRGxHCKwTMvCIlQcmE%0AXo63rAJcYrkUiATqdIcuQhpD0g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69777977/5b041b01a9495f0604e424a4/image.png?expires=1619632800&signature=1c00ac111c96a408329bddda72045e623d5c76d6a76a8ada2793791fee0ecc6c)

O valor do imposto é calculado através da multiplicação do valor da mercadoria pela alíquota do ICMS, por exemplo:

Se for um cliente de São Paulo, cujo valor total da lista de produtos seja R$1.000,00 o cálculo será realizado dessa maneira:

1000\*0,18 = 180, portanto, o valor do ICMS é de R$180,00.

Obs.: Como nesse caso o ICMS não varia de acordo com o produto, podemos calcular o imposto através do total da proposta (afinal, se tivermos 10 produtos com o valor de R$100,00, não precisamos somar 10 vezes 10% desses R$100,00, podemos diretamente calcular 10% de R$1000,00)

Configurando a fórmula do campo "Valor do ICMS":

[![Imagem 5: Configurando a fórmula do campo "Valor do ICMS":](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329701/ea4378244d1171978dee4ce0/image.png-expires%3D1619632800-signature%3Dada1a15100d6987121f46490672c59c728ae30fcbf736fe4ac12b65c84451e0c?expires=1786536000&signature=afee8ab096f0fb0c58b0cae4c7d68cbea7045515e6fba233d16e1ada78692a9d&req=dyYuFct3moFeFb4V1XW4gaXWN1iD5j5Pw8S5CFtN3ocLGyh49NqdDIjWkwq8%0ATM4Pdi%2BIh5v%2BmJocySH2uXJpbw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69867065/a2eb67c247f5c236d6a8784c/image.png?expires=1619632800&signature=ada1a15100d6987121f46490672c59c728ae30fcbf736fe4ac12b65c84451e0c)

Vamos conferir se o ICMS está sendo calculado corretamente!

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=deqHaviLlKA)

Obs.: Para aprender a adicionar uma margem no valor unitário, como apresentada no vídeo, leia [esse](https://sankhya.zendesk.com/hc/pt-br/articles/42427521647383) artigo.

Vimos que o valor do ICMS está sendo calculado automaticamente de acordo com o valor total dos produtos e da alíquota!

## IPI

O IPI é um imposto sobre os seus produtos e a sua alíquota varia de acordo com a essencialidade das mercadorias.
Para fins didáticos, separamos as alíquotas dos IPI dos produtos dentro de grupos, veja:

[![Imagem 6: O IPI é um imposto sobre os seus produtos e a sua alíquota varia de acordo com a essencialidade das mercadorias. Para…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329710/d54800bf98716bf189498e9d/image.png-expires%3D1619632800-signature%3Dd1de5336e0533258a3f5e021e52354bc5805194263a88090a5471e4966eb5ff0?expires=1786536000&signature=c015585f003b0149f7ab5d8d9fe8007cf214668d53c3267300a44354a041201d&req=dyYuFct3moBfFb4V1XW4gfESnNzUBhQsBJtrB8DscN1PYXkvNpvIqupbqPj3%0Ajk%2Fx%2Bh17CCQbZ9FUuRX9Ksq4Tw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69868667/ec6ed28f7dc7bcb0877dcc40/image.png?expires=1619632800&signature=d1de5336e0533258a3f5e021e52354bc5805194263a88090a5471e4966eb5ff0)

Criando o campo "Possui IPI?"

[![Imagem 7: Criando o campo "Possui IPI?"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329718/9627478d4ccd2bc7b6715f68/image.png-expires%3D1619632800-signature%3Debc9bb462bfbecac6d51c1c5ecb90a005d6b99a2df120495cfb5890b2942c7c1?expires=1786536000&signature=e5bed544752ac81f2147a68da046405d1db07208e0a0f9e9ede14c136bae7942&req=dyYuFct3moBXFb4V1XW4gfvqlYruKIY0OLfFWxwy81DMMJJHamsjnb0%2FiQNE%0A36BEZO3a7tbXjTv%2FIjlY7ADTtA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69868841/e8ca53537d0c9bac3875cf3b/image.png?expires=1619632800&signature=ebc9bb462bfbecac6d51c1c5ecb90a005d6b99a2df120495cfb5890b2942c7c1)

Criando o campo "Valor do IPI"

[![Imagem 8: Criando o campo "Valor do IPI"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329723/5af49404208b02e9704cb3d2/image.png-expires%3D1619632800-signature%3D74615240c62087aba95d78fe3219266ded5aef9afa70bc77debf667d24959512?expires=1786536000&signature=9adf4c5cb165d58e03d254033bedcf9f423a4a150a1bc5906237c1c916487107&req=dyYuFct3moNcFb4V1XW4gaVgIOpaxnidA95c5AJ1w%2BcZPfG7iRpkFRFeRefh%0AYyAQHppWmuacREurcFbC0KImrw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69868881/d50c554e9dc3f97712993d8f/image.png?expires=1619632800&signature=74615240c62087aba95d78fe3219266ded5aef9afa70bc77debf667d24959512)

Como alguns dos seus produtos não possuem IPI, isto é, possuem alíquota igual a zero, e outros possuem alíquotas variadas, vamos criar quatro seções no modelo da proposta: três para produtos com IPI e uma para produtos sem a incidência desse imposto.

No modelo, podemos criar quatro tabelas de produto, veja:

[![Imagem 9: No modelo, podemos criar quatro tabelas de produto, veja:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329730/a7328bd3ba0e6ae1556922dc/image.png-expires%3D1619632800-signature%3D459b53ec72ba2d7b8083428d454fa0b488a081eed699af60d862cfeab4c501c1?expires=1786536000&signature=fa8c3594302049a695d98be261fbc9f9209eb64bdee1a85b3edef1629cfbfc75&req=dyYuFct3moJfFb4V1XW4gTueMNq4eGNZgQO9WATP1xBSUqg9bFfE5%2BM2S7Jj%0AeeXXHkqfO5GUv1Nw5WvaoXzx7w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69872278/110ccd7a04dc81ad4eab1043/image.png?expires=1619632800&signature=459b53ec72ba2d7b8083428d454fa0b488a081eed699af60d862cfeab4c501c1)

As três primeiras, conterão os produtos que têm alíquota de IPI maior que zero. A quarta por sua vez, apenas os produtos cuja alíquota seja igual a zero.

Para nomear a seção desses produtos, vamos clicar com o botão direito sobre a tabela e em seguida em "Detalhes da seção"

[![Imagem 10: Para nomear a seção desses produtos, vamos clicar com o botão direito sobre a tabela e em seguida em "Detalhes da seção"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329737/92035125a16b9a2503e4ac00/image.png-expires%3D1619632800-signature%3D182549de62412a37049949f23cfbd9f1739b89e7c6bc5b5a982d0178d88d56b1?expires=1786536000&signature=f010d3d319449b9121c3c6350fe13efbe56a55cfcf1be0e492bc900dc0bc5907&req=dyYuFct3moJYFb4V1XW4gU3jaACJ6YX3XSeVfZkIwCmMmjULX30CQ9ttTylJ%0ACb%2Bzii5NLQFhPs3FJtLdwddCNw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69869420/ade4bbe0180f0aa7f23e5757/image.png?expires=1619632800&signature=182549de62412a37049949f23cfbd9f1739b89e7c6bc5b5a982d0178d88d56b1)

E aqui, poderemos dar um nome a essa seção, observe:

[![Imagem 11: E aqui, poderemos dar um nome a essa seção, observe:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329745/944e960b2e6e18060fc24602/image.png-expires%3D1619632800-signature%3D311a4cfa6c683ce4f68a898718b6c9b0f2627ef6b67cc462d845b468d841f9d3?expires=1786536000&signature=7168ed49ab4a569a3bb99c9c9cb3a2c1ebd036f072963f1f39f7fa6807409bd9&req=dyYuFct3moVaFb4V1XW4gU3Y30cY%2FGKeOIWHkh82xLMATetv5estihYC5z2u%0AVDyJLak84oTGG%2BQJrsaYErnWAg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69872344/88828d0767fabf32b1efb11a/image.png?expires=1619632800&signature=311a4cfa6c683ce4f68a898718b6c9b0f2627ef6b67cc462d845b468d841f9d3)

Feito isso nas quatro seções, veja como fica a disposição dessas tabelas de produto na hora de criarmos um negócio:

[![Imagem 12: Feito isso nas quatro seções, veja como fica a disposição dessas tabelas de produto na hora de criarmos um negócio:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329749/ac0ec4412213d748bc3805d6/image.png-expires%3D1619632800-signature%3D3cefdb655291c5c9d4e0df56d0d900681fb8ee46a73813398ef3f812b1b8ad64?expires=1786536000&signature=fe1836c81c591304a64e8fed0f53bd15eb713182d805f6818f28d5eafcbd1614&req=dyYuFct3moVWFb4V1XW4gZaHDGAZFJAqZgbhMJHy4cVBYOT9Fl%2FLB7vhCgxZ%0Aiuc4mnnm3bsGj6ERFaXpg0QAsA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69872645/eea539ebf15ae30e4855de37/image.png?expires=1619632800&signature=3cefdb655291c5c9d4e0df56d0d900681fb8ee46a73813398ef3f812b1b8ad64)

Agora, precisamos filtrar os grupos que aparecem em cada uma dessas seções, isto é, os grupos "Automóveis", "Pneu" e "Serviços" precisam estar listados nas suas respectivas seções enquanto os outros, na seção cuja alíquota seja igual a zero.

Para isso, vamos novamente até os "Detalhes da seção" e clicaremos em "Editar filtro dessa tabela de produtos"

[![Imagem 13: Para isso, vamos novamente até os "Detalhes da seção" e clicaremos em "Editar filtro dessa tabela de produtos"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329755/e02e957eeb08e2f774b7ce56/image.png-expires%3D1619632800-signature%3Dfecd26d694b623ef214920c6227ff5985ce1e1fe590362747fe56ff89fcf947d?expires=1786536000&signature=39ab80224f8fb75e5ac390a50c2ddd217a352a228bf9104d02a1d966531fb402&req=dyYuFct3moRaFb4V1XW4gQXOFSBOlWQSVkIFN45Cr716ZkVkrCVDsHM6JGh3%0AQbBu6X1eYu3xLdQtiOo6mPDP8Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69872713/75b3a0276d8128b3d9bad676/image.png?expires=1619632800&signature=fecd26d694b623ef214920c6227ff5985ce1e1fe590362747fe56ff89fcf947d)

Agora, você poderá escolher quais os grupos que devem ser listados nessa seção:

[![Imagem 14: Agora, você poderá escolher quais os grupos que devem ser listados nessa seção:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329760/3c01a83c077a8b5bc6cd25bc/image.png-expires%3D1619632800-signature%3D83011c8c8c7556d1f02b4a8ec4ab8587513f60a6c04465b85814fb93abc8ea50?expires=1786536000&signature=ec874e959f8f8617b266e1d7a6d3c0e5ac3d5f83cd190508dd301312f30e80b3&req=dyYuFct3modfFb4V1XW4gfT9Rk%2FN0aTh0m3RJsQMqXjqrr%2FsJGYkP6lMXt3w%0AgRtttcjeIxpn6CHBq2OtInlE9Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69872765/2b38fb600e4a0e714cb1e7ad/image.png?expires=1619632800&signature=83011c8c8c7556d1f02b4a8ec4ab8587513f60a6c04465b85814fb93abc8ea50)

Feito isso nas quatro seções, vamos ver como fica o nosso formulário de novo negócio!

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=S_m0EtSZCm0)

Podemos perceber que as seções estão filtrando os grupos corretamente, de acordo com a nossa classificação!

## Calculando o IPI na sua proposta

O cálculo do IPI é igual ao valor da mercadoria multiplicado pela alíquota, veja esse exemplo:

Valor da mercadoria: R$200,00
Alíquota do IPI: 15%
Valor do IPI: 200\*0,15 = R$30,00

Vamos criar um campo chamado "Valor do IPI XX%" para cada seção da sua proposta:

[![Imagem 15: Vamos criar um campo chamado "Valor do IPI XX%" para cada seção da sua proposta:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329764/1051b9b9af152766d1d47801/image.png-expires%3D1619632800-signature%3Dc7b5c19c6ebcd1e95d4f4e64837b82b560d25e22a4057b0aed3a1be67d1cddf9?expires=1786536000&signature=a34497db7cc22cc7467c198ef422d20555b2d38e9db0df07fc15a9195ded085d&req=dyYuFct3modbFb4V1XW4gffx0Cdlva3uNE5pmwBd%2Bk6JSZ8n1j%2BiTqZCSi%2FT%0AVnpK4HTmO2qqrEnLbPcdgW1nEA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69875373/246f71e1cc52ca296df34e07/image.png?expires=1619632800&signature=c7b5c19c6ebcd1e95d4f4e64837b82b560d25e22a4057b0aed3a1be67d1cddf9)

E em seguida, adicioná-lo dentro de cada uma das tabelas de produto, como na seguinte imagem:

[![Imagem 16: E em seguida, adicioná-lo dentro de cada uma das tabelas de produto, como na seguinte imagem:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329770/4340b4511211d1cf4be9ab95/image.png-expires%3D1619632800-signature%3Db554ca44ca0a5010437584f6566ca256eb7e6e825f24488192db8af1c6fb84f7?expires=1786536000&signature=29a72abcf703d8d159e3f2ed0033acf82935b4b6cbefe69e2a4894844bb65e15&req=dyYuFct3moZfFb4V1XW4gTgQs4dTGarB03fWqMAuam6gUPmyUgMNddKOLODW%0AyakuFZWXw%2Bb%2B8sgJ1jIq08%2Bjew%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69874737/fdb8cb77a94bfdfc889d7a10/image.png?expires=1619632800&signature=b554ca44ca0a5010437584f6566ca256eb7e6e825f24488192db8af1c6fb84f7)

Para que o campo calcule o valor do IPI, precisaremos da seguinte fórmula:

[![Imagem 17: Para que o campo calcule o valor do IPI, precisaremos da seguinte fórmula:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329779/595a11b617a04df26dddf362/image.png-expires%3D1619632800-signature%3D74ef133b1992e773122674a561138a3e384c6e9c6748dc6edd18ff067e13b733?expires=1786536000&signature=ed1aeeeee15dd1f9483d9457d47cec12c7bbad9c825d600cb39bf6caa5071566&req=dyYuFct3moZWFb4V1XW4gUUo1JQDQalDzfU3B%2F73A99gTNgdscC8zvNwFlNi%0AqXf3zZbfRS0bHQK%2Bhx54gtORag%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69874899/94409498be69eab0a986dd49/image.png?expires=1619632800&signature=74ef133b1992e773122674a561138a3e384c6e9c6748dc6edd18ff067e13b733)

No campo Total do IPI 15%, a divisão é "15/100", no campo Total do IPI 20%, "20/100" e no campo Total do IPI 30%, "30/100".

Vamos conferir se os valores estão sendo calculados corretamente!

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=YA9ZL4tr10w)

Podemos observar que o IPI está sendo calculado corretamente de acordo com cada seção.

Vamos calcular agora o valor total do IPI na proposta, isto é, a soma de todos os totais até agora!

O primeiro passo é criar um campo na proposta chamado "Valor IPI", como esse:

[![Imagem 18: O primeiro passo é criar um campo na proposta chamado "Valor IPI", como esse:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329789/95e8b0c4f733f58bf5186564/image.png-expires%3D1619632800-signature%3D37adcfe2fd7134eb12789212772277d163c8dd7998405b6d111a4891a6b0cf67?expires=1786536000&signature=023c1e80969bf095878fc5cafd7bbc042ca1f8d0fcf19203da48f30e5e4e6f08&req=dyYuFct3molWFb4V1XW4gd0y%2FeHCSjk46tF00qIH2kngotgDnH%2BMKHHbnIZA%0Az6OMDI%2FXVJOlkpO4R%2BPuMeGrcA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69875430/14b207a2ce74b44abd2df847/image.png?expires=1619632800&signature=37adcfe2fd7134eb12789212772277d163c8dd7998405b6d111a4891a6b0cf67)

O segundo passo é configurar a fórmula, de maneira que o campo some todos os campos "Valor do IPI XX%" e traga o resultado desejado.

[![Imagem 19: O segundo passo é configurar a fórmula, de maneira que o campo some todos os campos "Valor do IPI XX%" e traga o…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369329794/a56a3be44587b71f8eede509/image.png-expires%3D1619632800-signature%3Da1565e4a1f2ba082544c832a1584b0f514bad241dbf928f8ba1d61b0c8c68237?expires=1786536000&signature=4cd98005b72873c01fdd173e1d0a6f04ab38132b57089e02964ec9ff9e45b7b3&req=dyYuFct3mohbFb4V1XW4geU%2FaufSbYc9ddWmX%2B9%2FaJn9h6GunO0o6ScPVg7D%0AbI0BNAzpSx7tpWH1s9Qgq0%2FSaQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69875512/3ff48cb2c4a31c2b3f14b949/image.png?expires=1619632800&signature=a1565e4a1f2ba082544c832a1584b0f514bad241dbf928f8ba1d61b0c8c68237)

Confira a fórmula do campo em ação!

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=8PSIZ8M3yNI)

## Modelo de proposta

De nada adianta sabermos tudo sobre as fórmulas e campos de proposta, se não conseguirmos ter um modelo funcional que atenda às nossas necessidades.

Com todas essas informações em mente, assista a esse vídeo, onde eu mostro o modelo completo, gerando uma proposta teste aplicando as lógicas de ICMS e IPI.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=-hsTBhTNvZg)

## Concluindo

Com esse artigo, esperamos que vocês consigam cada vez mais autonomia nas edições e alterações nos seus modelos de proposta comerciais.

Lembre-se, estamos à disposição no chat para quaisquer dúvidas, sugestões e críticas.

Confira a nossa Central de Conhecimento em [suporte.ploomes.com](https://suporte.ploomes.com/pt-BR/)

Nos vemos online!
