---
id: "42427614176151"
titulo: "Como criar um hyperlink por fórmula"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427614176151-Como-criar-um-hyperlink-por-f%C3%B3rmula"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:05:44Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452349", "sync_hash_e732f7d7f02c"]
---

# Como criar um hyperlink por fórmula

Como criar um texto clicável a partir de um link

Para criar um hyperlink automático, vou criar um campo de texto simples para receber o link e um campo de texto multilinha para gerar o hyperlink.

Criando o primeiro campo de texto simples:

![Imagem 1: Para criar um hyperlink automático, vou criar um campo de texto simples para receber o link e um campo de texto…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329328/22911809f6e700c7defc6e66/mceclip1.png?expires=1786536000&signature=4c195e4a04009a6ea73c38d272704c7c0ed162d82be77c6548ed541b3506ffd0&req=dyYuFct3noNXFb4V1XW4gfvsYAMywtZ%2FXqSDARi620D6WeRYyiUi3Afo9oxQ%0AHWDKKb%2FuHaeEXp5HSZCaMa%2Bsew%3D%3D%0A)

Criando um segundo campo de texto multilinha e configurando a fórmula para isso basta expandir as "Configurações Avançadas":

![Imagem 2: Criando um segundo campo de texto multilinha e configurando a fórmula para isso basta expandir as "Configurações…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329330/0fad4b9f992e783cd902d0ad/mceclip2.png?expires=1786536000&signature=5d4e424f87c3cc996b71d956c7eb35add9e93b48ab869abc832fd31bd96f4594&req=dyYuFct3noJfFb4V1XW4gWDMOiCBunynYUuD868NeaXT2npDNAfjohfctMOb%0AHm0F7KCNG7xi5Aem%2BZbDqFfr2w%3D%3D%0A)

![Imagem 3: Criando um segundo campo de texto multilinha e configurando a fórmula para isso basta expandir as "Configurações…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329337/dea6d885d5ff37764db121ad/mceclip3.png?expires=1786536000&signature=b056defc9fbfe3248fd022fe32d5c109b4e2edde9f25499d10abf14e37b13441&req=dyYuFct3noJYFb4V1XW4gSq4JArPd3c2spD%2BovSWuDnsYEnO%2BygfEksm0c2W%0A6TjRJ5gL7DEBCSzN5kzu%2FUNkOg%3D%3D%0A)

Na fórmula, cole o seguinte:

```
"<a href=\'https://[campo de link]\'>Seu texto aqui</a>"
```

Agora precisamos substituir o campo. No meu caso, criei no formulário de cliente. Isso pode ser feito em qualquer módulo.

[GIF animado: Imagem 4: Agora precisamos substituir o campo. No meu caso, criei no formulário de cliente. Isso pode ser feito em qualquer…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329345/ae7dc93cbe71a67c830fd544/criar_hyperlink.gif?expires=1786536000&signature=e11445f781b5906681461cb6e5ebd94548223ad028a159beceeff66efa94435e&req=dyYuFct3noVaFb4V1XW4gfrSUSqHWP9XhWdaB7qdygkaMjexmp7GXeBdo%2FcR%0A8Wh5uvwjVNcDj4PEeQw8jKOCkA%3D%3D%0A)

ATENÇÃO: É obrigatório inserir a variável. Se apenas colar o texto ou digitar o nome do campo, o sistema não identifica que você está buscando um campo.

[GIF animado: Imagem 5: ATENÇÃO: É obrigatório inserir a variável. Se apenas colar o texto ou digitar o nome do campo, o sistema não identifica…](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369329352/b1c3eaa523bafbff3ab777b1/hyperlink2.gif?expires=1786536000&signature=aede0cbbdd8c3aa578c17ce4777f0a56622ae24a367a1553d7e7642b3a25a2bc&req=dyYuFct3noRdFb4V1XW4gTREW7J8ApxKy9QwqyvisvsdfwwuMfHCLr4YAHLo%0Ajw6ce6w8GWbO5tawkVB68DzuCw%3D%3D%0A)
