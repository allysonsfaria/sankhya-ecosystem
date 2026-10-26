---
id: "42427442760215"
titulo: "Como integrar o Ploomes com o ActiveCampaign (via Pluga)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427442760215-Como-integrar-o-Ploomes-com-o-ActiveCampaign-via-Pluga"
trilha: "PLOOMES: Automação de propostas  > Integrações via Pluga"
atualizado_em: "2026-08-10T18:03:11Z"
rotulos: ["sync_hc", "ploomes", "ploomes_14020209", "sync_hash_17d60ff482b3"]
---

# Como integrar o Ploomes com o ActiveCampaign (via Pluga)

**Observação:**

Essa integração foi desenvolvida pelo nosso parceiro Pluga. Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co).

## O que esta integração faz?

A cada **lead** que atinge uma **etapa** específica no ActiveCampaign, **criar ou atualizar** automaticamente um **cliente**, **oportunidade** ou **atividade** no Ploomes.

Ou então, quando um **card**, **cliente** ou **proposta** forem **atualizados** no Ploomes, **adicionar automaticamente** o lead em um **fluxo de automação** no ActiveCampaign.

## Requisitos

- Uma conta no Ploomes;
- Uma conta no ActiveCampaign;
- Uma conta na [Pluga](https://pluga.co/).

## Criando uma integração entre ActiveCampaign (origem) e Ploomes (destino)

Acesse a [Pluga](https://pluga.co/) e clique em “**Entrar**” ou em “**Cadastrar”** se este for o seu primeiro acesso;

![Imagem 1: Acesse a Pluga e clique em “ Entrar ” ou em “ Cadastrar” se este for o seu primeiro acesso;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148341910/0e101eb79fd2c484f5955b9e3a83/b51a5711-4648-40da-8eb8-558b6ed2d943?expires=1786536000&signature=8e54c2e4f13ec0eca31bb6bf10475668ed4a4d769355f230f12d90fac3f146e4&req=diEjHsp6nIheWfMW3nq%2BgaJHz3LG5NY2kGeYxqp51u7blbkwSbsmGUkllD0M%0AzgBz6qSTCbKq2RcxghovZKFgBZI%3D%0A)

Na área de usuário da Pluga, clique em “**Criar Automatização**”;

[GIF animado: Imagem 2: Na área de usuário da Pluga, clique em “ Criar Automatização ”;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148432737/9a78703811c1e5a1612ac8ea95cb/gif+pluga.gif?expires=1786536000&signature=cde46517bd3e1d5fcd3cf78d48cd80ef329f526f3583e130e32b0f834d1a5c67&req=diEjHs19n4ZcXvMW3nq%2Bgf1JMavqYCI93jfQmEBGKzzsCU5QJAqbPjCbVG1e%0AcGP%2F4OApVauHokQ2rgWlhM6VRZs%3D%0A)

Dê um título para a sua automatização;

![Imagem 3: Dê um título para a sua automatização;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148347865/c30d69c9a17367d241a8f6a2163d/f99d2cce-e647-4844-a219-7873c67de930?expires=1786536000&signature=27394c05c6b857e191a8231aba2fb4a0bf98fc6c83e421f9b8e8eb9e38cebe3b&req=diEjHsp6molZXPMW3nq%2BgY5RUW7JUbdY8cQzexP7%2FT1eAls0s9coT8MkQa7I%0A2Wych%2Ft1TPTbcHKXonyWdYDP%2BWg%3D%0A)

Selecione a ferramenta que você quer conectar ao Ploomes. Neste caso de uso selecionaremos o ActiveCampaign. Escolha também o gatilho, ou seja, o acontecimento na ferramenta que dará início à sua automatização. Neste caso de uso vamos selecionar “**Contato alcança etapa de uma automação**”, e clique em “**Continuar**”;

![Imagem 4: Selecione a ferramenta que você quer conectar ao Ploomes. Neste caso de uso selecionaremos o ActiveCampaign. Escolha…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148348627/f29d5d15f721a9f2cb5702c3fb70/0e3cedc0-8351-4b24-aed2-df4bdee60e5d?expires=1786536000&signature=96daa1858727c8f8c0c673c03d1efb6f0957379adfcae2f3898c88aaff1bff5e&req=diEjHsp6lYddXvMW3nq%2BgezgQAnjvuMkj37lx78tBR5rV3QsDAStc0GYfiFz%0Ajs%2FKyCtYKsMTKFZvDjg3eOsQo4Y%3D%0A)

Em seguida, você precisa conectar a sua conta do ActiveCampaign. Basta clicar em “**Conecte Sua Conta**” e realizar a autenticação. Essa etapa só precisa ser realizada na primeira conexão de cada ferramenta. Caso você crie uma nova integração com o ActiveCampaign sua conta já aparecerá entre as contas conectadas.

![Imagem 5: Em seguida, você precisa conectar a sua conta do ActiveCampaign. Basta clicar em “ Conecte Sua Conta ” e realizar a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148349113/543622bb5e985292eb7120c06a36/70af7eb7-6821-449f-96cb-b3bedd66bdd7?expires=1786536000&signature=34291093bc417525e9b49c605b0b60e027c04baa08d41306eb30f2fe4625ff40&req=diEjHsp6lIBeWvMW3nq%2BgV%2FkjtUt6h6NWfU98YAHw2kRqKPgKe2Vl169aPFF%0ABUOHsh1TFgyyygFFtQ6%2BXO8OQXE%3D%0A)

Caso queira, você consegue filtrar a sua automatização. Ou seja, dizer se ela vai precisar obedecer a algum critério para acontecer. Feito isso, clique em “**Continuar**”.

Uma vez que esse passo esteja concluído clique em **“Conectar Nova Ferramenta” para definir qual ferramenta irá receber os dados**.

![Imagem 6: Uma vez que esse passo esteja concluído clique em “Conectar Nova Ferramenta” para definir qual ferramenta irá receber…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148350261/15412fdae27ca1d4e0ef3cfd7d22/260c676f-fa9a-4db6-8d76-d733d853580c?expires=1786536000&signature=de8e03df373395480dd70aa066d4769fa72477bb14febc147f0b899dcfc21175&req=diEjHsp7nYNZWPMW3nq%2BgV8qRmEMf7Nge9plm0AYNmtEjv7NJ9M0IPXwFZOK%0Ay9h6wqz8oM%2FS4kU0gBT%2FQfacsfo%3D%0A)

Selecione o Ploomes como nova ferramenta a ser conectada, além da ação a ser trabalhada pela automatização. A ação funciona como uma resposta ao gatilho selecionado anteriormente, ou seja, ela acontece a partir do momento em que o gatilho é acionado. Uma vez selecionada a ferramenta de destino e a ação, é só clicar em **“Continuar”**.

![Imagem 7: Selecione o Ploomes como nova ferramenta a ser conectada, além da ação a ser trabalhada pela automatização. A ação…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148351150/f3f9735715c3f0ea6b891e71a977/fa8d8c2e-dbbf-4eee-9d23-2245ce2bb94b?expires=1786536000&signature=c98571908a537645479c09c0f26ac839f0dd22e24f499ed362fbedae4603b101&req=diEjHsp7nIBaWfMW3nq%2BgTsktedULQZyDq7L7kQhudVD5chrwJIMp0dVxJxl%0APjRExIOjMkOwzjceiuKcmYnpSVQ%3D%0A)

Conecte a chave da conta do Ploomes que deseja integrar. Caso não saiba como encontrá-la, clique em "**Veja o passo a passo para encontrar suas chaves de acesso**" e siga os passos indicados.

![Imagem 8: Conecte a chave da conta do Ploomes que deseja integrar. Caso não saiba como encontrá-la, clique em " Veja o passo a…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148351915/ebae4f9f235312157abc0fb82d0e/fe88a7c5-1c43-4eb1-b2be-97b9c7fb4e18?expires=1786536000&signature=fa47ecd241112edc084ab097d1043273542c2ecc22b18895eacb9441a115c354&req=diEjHsp7nIheXPMW3nq%2BgRg370nswexeJt4HB%2BpL1wk1AXaPeuC50oh7aM4i%0A0IIhFFqUwYwpGqOm%2BHyGRA9SIX8%3D%0A)

No último passo, você definirá quais informações constarão em cada campo do contato no Ploomes.

![Imagem 9: No último passo, você definirá quais informações constarão em cada campo do contato no Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148352256/e49e395b456f56b637ecec424df3/875d0b0e-a83d-4913-a336-b9303bd837fa?expires=1786536000&signature=fae729046514cdceb05ab32c055beb2cc7236f90246f236c8c1a4bc94028d5c1&req=diEjHsp7n4NaX%2FMW3nq%2BgapEcUtApIHWSXUVQcWL%2ByvSo9oxF3vr4xf8rmRt%0AQxeRKGDWxrYHMEneQffNVea4Lp8%3D%0A)

Ao terminar a personalização desses campos, é só clicar em “**Finalizar automatização**” no fim da página e pronto. Está criada a sua automatização.

![Imagem 10: Ao terminar a personalização desses campos, é só clicar em “ Finalizar automatização ” no fim da página e pronto. Está…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2148352893/2e43cc3a849d2d2aef043bd132b2/fc95d5ff-12b1-433c-872d-0b062aef0062?expires=1786536000&signature=45ba1f2653d6b4570c94b6100f9a52842009df3d1206bc7349698f94929a01c2&req=diEjHsp7n4lWWvMW3nq%2BgUstVb2MUv79lVHn55bziI1eXBF1e%2BdspwACCcuc%0AnZUjpzrXJonx5QI1D%2F0qDcmLtX0%3D%0A)

Caso queira, você ainda pode adicionar mais ferramentas em seu fluxo de trabalho e criar uma automatização **multi action**. Para isso, é só clicar em **“Conectar Nova Ferramenta”**.

---

Caso tenha ficado com alguma dúvida, o time da Pluga estará à disposição para te ajudar.

É só enviar um e-mail para [suporte@pluga.co](mailto:suporte@pluga.co) ou acessar [https://pluga.zendesk.com/hc/pt-br/requests/new.](https://pluga.zendesk.com/hc/pt-br/requests/new)
