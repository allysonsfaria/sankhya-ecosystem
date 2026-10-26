---
id: "42427551982103"
titulo: "Como contar o maior valor de um campo de produto da proposta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427551982103-Como-contar-o-maior-valor-de-um-campo-de-produto-da-proposta"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-10T18:04:57Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452286", "sync_hash_05fb88aaf577"]
---

# Como contar o maior valor de um campo de produto da proposta

Para essa configuração, precisamos criar dois campos;
O primeiro, um campo de produto da proposta do tipo texto simples. Precisamos desse campo para criar uma lista de valores no segundo campo que criaremos, um de bloco.

Nesse exemplo, vou analisar qual dos meus produtos tem a maior **quantidade**, mas podemos usar qualquer valor.

A fórmula do primeiro campo fica:

```
";[Produto da proposta.Quantidade]"
```

![Imagem 1: A fórmula do primeiro campo fica:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1541600646/bb650415fcd4635a4afb5672c040/image.png?expires=1786536000&signature=66c1c155332213a45e73c56d94016804a35e5e7d6baa8c97b8142cd4e7860364&req=dSUjF89%2BnYdbX%2FMW3nq%2BgS7SIteDB7b4XZi%2FAYN6Tgc0izBjR8vO59v4ZaVT%0A1%2FsUIWt04R%2Byqng%2Bct89%2Ba75vcA%3D%0A)

Chamei esse campo de "Qtd texto"

Vamos criar agora o campo de bloco. Dei o título de "Maior Quantidade"

![Imagem 2: Vamos criar agora o campo de bloco. Dei o título de "Maior Quantidade"](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1541600250/b6d9cea6ffc7348dda916f7b1182/image.png?expires=1786536000&signature=21b118b571a1ef8e830c475881ba4b5887761b4c32138ba8c3e097a0aeff9e6c&req=dSUjF89%2BnYNaWfMW3nq%2Bgck7bNeuoBTki2LVBGmwNyB%2FLCI7bDQNW5OYLqeb%0A07h5PAUfVF7fNjhpwWPQkHdy7A0%3D%0A)

```
const quantidade = "[Produto da proposta.Qtd Texto]"
Math.max.apply(null, quantidade.split(';').map(Number))
```

[GIF animado: Imagem 3: Vamos criar agora o campo de bloco. Dei o título de "Maior Quantidade"](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1541630612/b0abc973176b8aa8933be3766431/Maior+Quantidade.gif?expires=1786536000&signature=ba48ac880db0f79b58c553e88a460ed76ada601ae80f3b989939dcc690ea1117&req=dSUjF899nYdeW%2FMW3nq%2BgV2XY0Wm%2Fk53wIxtmpmtvw0SauMDPa9QcdBqbaE3%0AV4GIoFBH59OeV7Hw5dcnLLaXiCs%3D%0A)
