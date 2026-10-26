---
id: "42427646964375"
titulo: "Checklists condicionais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427646964375-Checklists-condicionais"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-10T18:07:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452176", "sync_hash_166c785850a1"]
---

# Checklists condicionais

Como criar uma checklist condicional que aparece ou não dependendo de filtros.

Nesse artigo ensino a criar checklists condicionais. Isso é útil para situações em que uma informação é obrigatória para um tipo de negócio e não para outro. Um bom exemplo é o campo de CNPJ para clientes internacionais.

Para criar um checklist, entro na configuração do meu funil:

![Imagem 1: Para criar um checklist, entro na configuração do meu funil:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324301/f596cff7a71bc7f448e0b247/mceclip0.png?expires=1786536000&signature=1a8b7c7bea1376fd5424a24a74e8ac134ca7b83496411a7ca5fc56d94514c485&req=dyYuFct6noFeFb4V1XW4geSvOBVlBSzf6ROue0pOv9%2BmMMugKdAPA%2FZnOFjB%0AFndFZ1GHyFERhOtvGGt%2BdvUwIA%3D%3D%0A)

![Imagem 2: Para criar um checklist, entro na configuração do meu funil:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324304/3326a415caab0767a84e7208/mceclip1.png?expires=1786536000&signature=165d0e4156338ef6fb60d086f15cfdaf83df2aaf6fbfbabe45f98b4b0495fd46&req=dyYuFct6noFbFb4V1XW4gVFTGbE3a7TkEhMTUTqInp%2FvffVEVs7VAAW2bNia%0AQ%2Fdl4vqVpQT%2F5IO3tokOanXHpw%3D%3D%0A)

Checklists ficam dentro de seus **estágios**:

![Imagem 3: Checklists ficam dentro de seus estágios :](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324308/70676d4e3204b740b7246efd/mceclip2.png?expires=1786536000&signature=e24a3a365e8ae72c6ca184d5b035b3d9e385a4fd940a6ce60093b1262c260f1a&req=dyYuFct6noFXFb4V1XW4gcGnS6oPnYz1%2F8pQ0Vfoml8gKXule06ouRHhP1RG%0Ak0bKdKXyy0ilBOC3kgNj7L6BZg%3D%3D%0A)

![Imagem 4: Checklists ficam dentro de seus estágios :](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324312/feacb98225dbf14559dc7316/mceclip4.png?expires=1786536000&signature=1ba561fe944e92b8d29c63cf3c027e98c9e81d6bfeca35b0bd16c60d2093c0d3&req=dyYuFct6noBdFb4V1XW4gVk2drGaL8A2MjNdRrZVe9s20GB7r7B8OBQOzxhw%0AXomv0uD%2BBTe%2B4gqEKuaAkOE2%2Bw%3D%3D%0A)

Cada um desses blocos leva uma condição.
No "Dados da empresa", peço o CNPJ e a Região de vendas (campo customizado) apenas para clientes do tipo Empresa (pessoa jurídica) com país sendo Brasil ou não preenchido.

![Imagem 5: Cada um desses blocos leva uma condição. No "Dados da empresa", peço o CNPJ e a Região de vendas (campo customizado)…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324319/1ac452de3dff9a0235ca09d8/mceclip6.png?expires=1786536000&signature=10c35928b0dc5e8b90b8dd0a56138be6a47ba910cf688bf8c618de880c0ecc5b&req=dyYuFct6noBWFb4V1XW4gdk3I0qGuv0E1dRFGx7P0W7SNuHETcwxf1WTnqZ5%0AEFv4T2PHggf59WjqU3w%2BfEhNJw%3D%3D%0A)

![Imagem 6: Cada um desses blocos leva uma condição. No "Dados da empresa", peço o CNPJ e a Região de vendas (campo customizado)…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324327/30e7c03432a45bb1fc4a413d/mceclip7.png?expires=1786536000&signature=d5ca275c86be7f9f506f366da740e1412e49f25bc9ab633ed59fda32df683d76&req=dyYuFct6noNYFb4V1XW4gYFx8fnaCUpNYs3wlLsnRdONBjL6wC7Kn96QRz2V%0AIE4IZLOeUoNCTuR8GgQma2TaJA%3D%3D%0A)

Nesse exemplo, clientes do Brasil precisam preencher CNPJ:

![Imagem 7: Nesse exemplo, clientes do Brasil precisam preencher CNPJ:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324329/1845940d2351952290b90dc1/mceclip8.png?expires=1786536000&signature=9e3367f470a56dd8ba96cda8e2a6866b28122e229570fb5e9a3d17823fa5a611&req=dyYuFct6noNWFb4V1XW4gSYHhgQPCb1hxxZU2wA7vrcV0nqWMOOqmbuOUolQ%0A9LGsjHQcw312BLg4kvS4qUVfCQ%3D%3D%0A)

Já pessoas, mesmo que sejam do Brasil, não:

![Imagem 8: Já pessoas, mesmo que sejam do Brasil, não:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324335/4b72493429222e1049e09b8a/mceclip9.png?expires=1786536000&signature=5ccd56e3d42f3374385312ced9809bea936b4ad29e8b1f14fae86803fd701d7b&req=dyYuFct6noJaFb4V1XW4gVy3DPIZg0nzUCpKcy3dENkUcN41r%2FhgVVeAxHW%2F%0AnFMQ%2FE3yaEgx%2BL2TEvE1WOqdOQ%3D%3D%0A)

E nem Empresas do exterior:

![Imagem 9: E nem Empresas do exterior:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369324343/d1d964ac96a48bce091fba44/mceclip10.png?expires=1786536000&signature=8c41d1c122d8a98c9b7ec5430a562116c83f5cbe8db3839e619107ab47894361&req=dyYuFct6noVcFb4V1XW4gSNxZXP%2BlDdOxEG0FuwuIXqdi9fkdVnshNBnSFFN%0AdJS6DDQKyIk4a9uUdIhyVbbRPw%3D%3D%0A)
