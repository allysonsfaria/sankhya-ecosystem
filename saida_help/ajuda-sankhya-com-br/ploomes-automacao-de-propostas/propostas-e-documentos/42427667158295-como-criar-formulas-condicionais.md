---
id: "42427667158295"
titulo: "Como criar fórmulas condicionais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427667158295-Como-criar-f%C3%B3rmulas-condicionais"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:14:18Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452346", "sync_hash_5838f9750b49"]
---

# Como criar fórmulas condicionais

## Este artigo explica como configurar fórmulas cujos resultados dependam de condições variáveis

As fórmulas condicionais são aquelas que não são fórmulas fixas, ou seja, dependendo de determinada informação, o cálculo varia. Esse tipo de fórmula é comumente usada nos cálculos de impostos, como ICMS, ISS, IPI, entre outros.
Vamos dar um exemplo de fórmula condicional:

Suponha que você é um comerciante muito generoso e que sempre que o seu cliente faça uma compra acima de R$50.000,00, você concede a ele um desconto de 10%. Como calcular esse desconto?

Primeiro, podemos dizer que é um desconto condicional, visto que só será aplicado SE o valor total for maior que R$50.000,00.

Como é um desconto aplicado no total da lista dos produtos da proposta, precisaremos editar a fórmula do campo "Total" do nosso modelo, basta acessar **Administração > Modelos de Documentos** :

Escolha o modelo da proposta e realize os passos do exemplo abaixo:

[GIF animado: Imagem 1: Escolha o modelo da proposta e realize os passos do exemplo abaixo:](https://downloads.intercomcdn.com/i/o/383000777/483de91c4e4ab2615c485664/edit_formula_total.gif?expires=1786536000&signature=243aa6c9c42d55ed3123d4a4c418afd5f93ba61a6147ff78f54ba6135a77e5af&req=dygkFsl%2BmoZYFb4V1XW4gazkbdbjRCmyXze%2FboyVgbLfr8Atf%2FQVpDe7PeE4%0AcOKI2ACpFcqxI7X%2Bau9V0ubgAQ%3D%3D%0A)

Aqui você precisa adicionar uma condição, isto é, algo que se for satisfeito, deverá resultar em uma ação. No nosso caso, a condição que deve ser satisfeita é "Total da lista dos produtos da proposta maior que R$50.000,00" e se isso for verdade, a ação a ser tomada é "Aplicar um desconto de 10%".

Veja como fica a nossa fórmula:

![Imagem 2: Veja como fica a nossa fórmula:](https://downloads.intercomcdn.com/i/o/383003021/de4153f9deb8fc9d3149cf8a/image.png?expires=1786536000&signature=139e31989ba2098ee7c9c482ff5846e7979f18b915339d4164847b49aa7edc80&req=dygkFsl9nYNeFb4V1XW4gQbTwZHqXfmDjxQ18aWvNQizJIFq74Fxj9E%2BOoov%0A1CAHCTqYXn35PBxLZCZeEotCQw%3D%3D%0A)

Legenda da imagem:

Retângulo vermelho: condição a ser satisfeita
 Retângulo verde: ação a ser tomada caso a condição seja satisfeita
 Círculo preto: salvar a fórmula criada.

Vamos conferir se a nossa fórmula está correta! Para isso, criaremos uma proposta cujo valor total dos produtos seja superior a R$50.000,00, observe:

![Imagem 3: Vamos conferir se a nossa fórmula está correta! Para isso, criaremos uma proposta cujo valor total dos produtos seja…](https://downloads.intercomcdn.com/i/o/383008127/5268ec9b7120d5468f30d5dd/image.png?expires=1786536000&signature=803a7d18799e54c4b7c743b5130c85a3f0f73c7edbca9ec3e34cbd8818abcb64&req=dygkFsl2nINYFb4V1XW4gTtwcmYM8LFmoUpZ%2BNGEwqIL0L%2FwcW6fL2NruwsZ%0ACQwXw%2Bwgo9PPLr2smSqISBHNmg%3D%3D%0A)

Ao gerar a proposta, podemos notar que o valor total já contempla o desconto de 10%, pois a soma dos produtos excede R$50.000.

Removendo um dos produtos, o desconto não é aplicado:

![Imagem 4: Removendo um dos produtos, o desconto não é aplicado:](https://downloads.intercomcdn.com/i/o/383009157/701fb1bb24ecf8eacfb7e206/image.png?expires=1786536000&signature=1183abcfd2e824a577f494a274a66bdd17d266dcc9f6fc381754f02a4031b92f&req=dygkFsl3nIRYFb4V1XW4gT7eJM7v8e0AUODvC3QuAmouzPkYAilc5JU1MatD%0AdQpbhG0e2od9psFzwrCusnGDgg%3D%3D%0A)

Para ver um exemplo de fórmula condicional trabalhando com a lógica de impostos, confira [esse](https://sankhya.zendesk.com/hc/pt-br/articles/42427636933527) artigo.
