---
id: "42427484483479"
titulo: "Condicionais em campos no Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484483479-Condicionais-em-campos-no-Ploomes"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:02:52Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6957918", "sync_hash_5a71ecaeaae6"]
---

# Condicionais em campos no Ploomes

Olá Ploomers! Primeiramente para fazer uma condicional, é necessário conhecimento básico de Javascript e entender como funciona uma condicional em cada caso de uso. As condicionais no Javascript funcionam como uma "tomada de decisão".

Seres humanos tomam decisões que afetam suas vidas o tempo todo, desde pequenas ("devo comer um biscoito ou dois?") até grandes ("devo ficar no meu país de origem e trabalhar na fazenda do meu pai ou devo mudar para a América e estudar engenharia?").

## Sumário

[Declarações - if/else](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484483479-Condicionais-em-campos-no-Ploomes#h_a72a031826)

[Utilizando condicionais no Ploomes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484483479-Condicionais-em-campos-no-Ploomes#h_1e8ae72f74)

[Exemplo prático](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484483479-Condicionais-em-campos-no-Ploomes#h_7deceec366)

## Declarações - if/else

De longe o tipo mais comum de declaração condicional que você usará em JavaScript — as modestas declarações if/else.

Veja a sintaxe básica do if/else no pseudocódigo:

```
if (condicao) {
  codigo para executar caso a condição seja verdadeira
} else {
  senão, executar este código
}
```

Aqui nós temos:

1. A palavra reservada if seguida de um par de parênteses.
2. Um teste condicional, localizado dentro dos parênteses (normalmente "este valor é maior que esse?", ou "este valor existe?"). Esta condição pode fazer uso dos operadores de comparação que discutimos no último módulo, e podem retornar **true** (verdadeiro) ou **false** (falso).
3. Um par de chaves, e dentro dele temos código — pode ser qualquer código que queiramos, e só vai ser executado se o teste condicional retornar true.
4. A palavra reservada else.
5. Outro par de chaves, dentro dele temos mais um pouco de código — pode ser qualquer código que queiramos, e só vai executar se o teste condicional retornar um valor diferente de true, neste caso not true, ou false.

Vamos utilizar um exemplo de texto acima com nosso pseudocódigo, no caso utilizaremos "devo comer um biscoito ou dois?":

```
if(se estiver com pouca fome){
  Comer um biscoito
} else {
  Comer dois biscoitos ou mais.
}
```

DICA: o if ele funciona como um "se" e o else como um "senão".

## Utilizando condicionais na Ploomes

Na criação do cliente do tipo “Empresa” vamos fazer 2 campos, um campo “Quantidade de pessoas na empresa” e um campo “Tamanho da empresa”. O campo de quantidade de pessoas na empresa será do tipo “Número Inteiro”, e o campo tamanho da empresa será do tipo “Texto Simples”.

Quando preencher o campo “Quantidade de pessoas na empresa”, se a quantidade for menor que 100, o campo tamanho da empresa será preenchido automaticamente com “Pequeno Porte”. Se não ela será preenchida com “Médio/Grande Porte”.

###

### Mãos à obra:

Os campos que devem ser criados:

![Imagem 1: Os campos que devem ser criados:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173533348/35788cb602e6e73ececa24c9837a/image.png?expires=1786536000&signature=c2cdf07aea74105e3a761bcbd23135a8bcba9151387ee31cd4eee77239ebe1a3&req=diEgFcx9noJbUfMW3nq%2BgTil99mI9vKn%2BvbRn45VbHayudy0jonKI5jgZm1l%0ADBSgE4la%2BEyDbxELe6RSqZane7M%3D%0A)

![Imagem 2: Os campos que devem ser criados:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173534730/598d8532947aec9578a93c058ce5/image.png?expires=1786536000&signature=0639f95a410f7b818152df9aa627bbad85c9f0d87dac03f61e8fbe819fcc1f0b&req=diEgFcx9mYZcWfMW3nq%2BgVN58oF2G92JU4ytF6WXBCdO902aGu8UfOBqGf4m%0AUAUaszZ95ZloHw%2FOJ0m3yHBmVQ0%3D%0A)

Dentro do campo “Tamanho da Empresa” o campo “Campo bloqueado” tem de estar preenchido. Isso se dá pelo campo ser de texto simples - queremos que seja preenchido apenas pela fórmula, e nunca manualmente. Assim garantimos uma melhor governança de dados.

![Imagem 3: Dentro do campo “Tamanho da Empresa” o campo “Campo bloqueado” tem de estar preenchido. Isso se dá pelo campo ser de…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173536929/8efed0c25322aa8c17dc2bf9f628/image.png?expires=1786536000&signature=2f7878546785667bc8ea6f81997ef87cba0461df27e945db20cb9ff71da4bba7&req=diEgFcx9m4hdUPMW3nq%2Bgf97U%2FBHWLK%2BwjtShNkdXA1HwFX4lT6L0DyX0Ryv%0AVGjA6im5fClupMiRpJUGkn8spto%3D%0A)

Agora clique em “Configurações avançadas” e em “Fórmula”, clique em “Configurar”:

![Imagem 4: Agora clique em “Configurações avançadas” e em “Fórmula”, clique em “Configurar”:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173539183/549a8d1fce7385eacab5df1c7642/image.png?expires=1786536000&signature=1208befb679361b1792b4daf4631ef5cbec14bf1d9556b19657bc3d64f92b962&req=diEgFcx9lIBXWvMW3nq%2BgbXRjXqt10vNoePnCDeC96BGI5udnYG4yJntiWcZ%0AE4gYb8p9Pb6lBR%2FXXXOidnVNuOM%3D%0A)

Vamos iniciar a criação da condicional no campo, lembrando o campo que deve ser preenchido é o “Tamanho da Empresa” então a condicional irá ser inserida nele.

Como ficara á fórmula condicional:

Quando quantidade de pessoas na empresa for menor que 100 o tamanho da empresa será de Pequeno Porte, senão Médio/Grande Porte.

```
if([Cliente.Quantidade de Pessoas na Empresa] < 100){
  "Pequeno Porte"
} else {
  "Médio/Grande Porte"
}
```

![Imagem 5: Quando quantidade de pessoas na empresa for menor que 100 o tamanho da empresa será de Pequeno Porte, senão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173546248/b750bd7175450f27e1fb1b686e3e/image.png?expires=1786536000&signature=4f92149dfc0cde8619058b644fce67c368df9523af31dd14d6f3b9aee138b620&req=diEgFcx6m4NbUfMW3nq%2BgcIbVPuCawjCOWpesFffttf7mG8x4xLdknn%2FG0QC%0A9%2B1SCletu3e5SHeuI6EP66BH9Gs%3D%0A)

Agora salve clicando em “Salvar” o campo “Tamanho da Empresa” para salvar todas as configurações feitas neste campo:

![Imagem 6: Agora salve clicando em “Salvar” o campo “Tamanho da Empresa” para salvar todas as configurações feitas neste campo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173553539/3bcd052485a0aa08932c3a5c418e/image.png?expires=1786536000&signature=5afc342c4c61ef6e5332526fc2e88f51fc370c3aff027806d23ae4a1207432fc&req=diEgFcx7noRcUPMW3nq%2BgcqVQEBFY%2BtMZODNU7EFUP6RXed%2BqR4twhUwssVb%0AtHtX32aj4Wk5%2F%2BeT0%2BXGQx4tSdM%3D%0A)

E por fim o campo com a nossa condicional, funcionando:

![Imagem 7: E por fim o campo com a nossa condicional, funcionando:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173549768/93017d20443b8cf48b9d63e00805/image.png?expires=1786536000&signature=0c67f6fe079c33960a0c3f4d1cc8526740aa30ccbaad2fa6a5bcc04c6857025c&req=diEgFcx6lIZZUfMW3nq%2BgdKa53ry9WbYnI1qOPPfRsViXG44K9o6uFY%2FqC9l%0AEffs3SWr7Xz%2B%2FACH7vkqd6KrJUU%3D%0A)

![Imagem 8: E por fim o campo com a nossa condicional, funcionando:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2173550224/1e668c80c8650fbc202f84ada68d/image.png?expires=1786536000&signature=8c823312b7c09514ded44718bdf73216679388bfdae68d23759a41c23df9dd58&req=diEgFcx7nYNdXfMW3nq%2BgYKtKUFSkw%2BJkPMvcSaV9QVmzGGPhzidopULoD0P%0ANPniyAe5K4JgTwP7VLu9URb9Uog%3D%0A)

Para criar uma condicional é necessário entender a necessidade de uso, entender se é possível criar algo com está condicional e se for possível aplicar. E agora sim, você tem um campo com condicional inserido e também conhecimento básico de JavaScript 😉.
