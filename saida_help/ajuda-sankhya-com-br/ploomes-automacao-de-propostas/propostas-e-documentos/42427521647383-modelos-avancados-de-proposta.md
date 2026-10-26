---
id: "42427521647383"
titulo: "Modelos avançados de proposta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:14:33Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452274", "sync_hash_4637f7a1fdcd"]
---

# Modelos avançados de proposta

Descubra neste artigo o poder das fórmulas para automatizar cálculos em suas propostas, aprenda a ocultar informações confidenciais e a aplicar filtros aos produtos. Explore funcionalidades avançadas no gerador de modelos de propostas.

**O que você vai encontrar nesse artigo?**

- [O que são fórmulas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta#o-que-so-frmulas)

a) [Fórmulas simples](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta#frmulas-simples)
b) [Fórmulas condicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta#frmulas-condicionais)

- [O que são e para que servem os campos escondidos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta#campos-escondidos)
- [Como aplicar filtros nos produtos da proposta?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42427521647383-Modelos-avan%C3%A7ados-de-proposta#filtros-nos-grupos-de-produto)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

Antes de começarmos, é crucial que você já esteja familiarizado com os conceitos de campos de proposta, então recomendamos a leitura [desse artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427702983959). Para aqueles que já têm conhecimento no gerador de modelos de proposta, vamos em frente!

## O que são fórmulas?

Alguns campos em sua proposta podem requerer cálculos, e as fórmulas servem para executá-los automaticamente dentro de seus modelos. Por exemplo, para calcular o valor total de sua lista de produtos, o sistema realiza a seguinte operação: "Valor unitário" x "Quantidade". As fórmulas são personalizáveis; ou seja, se sua empresa possui uma lógica de cálculo específica, é possível incorporá-la no Ploomes!

Como exemplo, consideremos a fórmula do campo "Valor da proposta" no modelo padrão.

![Legenda: Tela de campos em modelo de proposta, contendo as guias de](https://downloads.intercomcdn.com/i/o/567001526/28ea8001f5660042c529352c/image.png?expires=1786536000&signature=e3bda8b1f4eaa41890f0e1af700b998e555c0ae9a49fc63cb2c224dbddaf5662&req=cSYgFsl%2FmINZFb4V1XW4gcIBpqztUuBjZe7M8BTvd2L6IYtSfRcmU1SYzcpo%0ApoahYkLxF6meAG1qbVIobWnfUg%3D%3D%0A)

```
Legenda: Tela de "Campos" no modelo de proposta, com uma seta vermelha apontando para a seção de "Proposta".
```

![Imagem 2: Como exemplo, consideremos a fórmula do campo "Valor da proposta" no modelo padrão.](https://downloads.intercomcdn.com/i/o/567002002/09123b75fa2056b2233ab90e/image.png?expires=1786536000&signature=738083099aa709885930139cfb0ff258b2ebcb15048662da66b302c98253f68e&req=cSYgFsl8nYFdFb4V1XW4gb2JXT34whN5pi6ANtsHqh4WlNI%2BhxvtZm8GwVj9%0AX4NTTXui1SjDUZABbSjEi%2BkRhQ%3D%3D%0A)

```
Legenda: tela de campos de proposta, com uma seta vermelha apontada para o ícone de edição ✏️ do campo "Valor".
```

Ao entrar nas configurações do campo "Valor", você verá esta tela, onde poderá editar a fórmula do campo:

![Imagem 3: Ao entrar nas configurações do campo "Valor", você verá esta tela, onde poderá editar a fórmula do campo:](https://downloads.intercomcdn.com/i/o/567002379/8d8cdd2feb1fa1550f4502a0/image.png?expires=1786536000&signature=fe17dee29aedefc12ec6a32b8764e74d8e399bd355816948f6e372ca069f5fc6&req=cSYgFsl8noZWFb4V1XW4gao1P44u3kCHFSa1fMJFykvl7rQR1FbHFy1SmifB%0Ai5IoHB9SexHtTfzzBCf%2BoB7hkg%3D%3D%0A)

```
Legenda: Tela do menu de edição do campo com uma seta vermelha apontando para "Configurar" a fórmula nas "Configurações avançadas".
```

![Imagem 4: Ao entrar nas configurações do campo "Valor", você verá esta tela, onde poderá editar a fórmula do campo:](https://downloads.intercomcdn.com/i/o/567002577/f926d0a73ba4fbdbf6419146/image.png?expires=1786536000&signature=1bdd274fd1ec66307a56bbe650a22eef04a750e7e960575b7f836c83857087aa&req=cSYgFsl8mIZYFb4V1XW4gb3dUe31cNxzHHXylIfIYgfOfeL6f0NZuZJSWIZT%0AotOM9frogPulaOn4PjzTf9i%2F2w%3D%3D%0A)

```
Legenda: Tela de configuração de fórmula, mostrando a fórmula simples padrão do campo "Valor" da proposta:
Total x ((100 - Discount) / 100
```

Exemplo prático com essa fórmula:
Valor total = R$1000,00
Desconto dado = 15%

Cálculo:
1000\*((100-15/100) > 1000\*(85/100) > 1000\*0,85

Resultado:
R$850,00

Nas edições do campo, você verá a opção "Bloquear edição por padrão", que significa que, ao preencher essas informações na criação da proposta, ele não permitirá edições. Essa configuração também aceita fórmulas.

![Imagem 5: Nas edições do campo, você verá a opção "Bloquear edição por padrão", que significa que, ao preencher essas informações…](https://downloads.intercomcdn.com/i/o/567003410/c3386ec19a65d0aac44463c8/image.png?expires=1786536000&signature=7db579b52c2519d20e51175a575a76c0d124d3680f2bdb99b5c012467cbf897b&req=cSYgFsl9mYBfFb4V1XW4gV5XFeAQby7aOtGiqQhDB5WZARYfKB8ybdhooahm%0AEIr9NPpmWrMQ3OHsg6Gx9wxBZw%3D%3D%0A)

```
Legenda: Tela do menu de edição do campo com destaque em "Configurações de edição e bloqueio do campo", onde a opção "Bloquear edição por padrão" está ativada.
```

Exemplo prático com essa configuração de bloqueio:

![Imagem 6: Exemplo prático com essa configuração de bloqueio:](https://downloads.intercomcdn.com/i/o/567005357/0d4629443271540baefd2aca/image.png?expires=1786536000&signature=faa202dfdc75f8a3d20218849d1d285e93e47a7d2864fb058fa62ae769246a62&req=cSYgFsl7noRYFb4V1XW4gUtGlSZRHFpredsiReGO9RNslKJKMcohm3kAmTlq%0ArLqY8eU%2FJOED%2FzgVYx1k4V9T9g%3D%3D%0A)

```
Legenda: Tela de campos de produto proposta, com uma seta vermelha apontada para o ícone de edição ✏️ do campo "Valor unitário".
```

![Imagem 7: Exemplo prático com essa configuração de bloqueio:](https://downloads.intercomcdn.com/i/o/567005844/09e8a6fa0a61bbb5668edffc/image.png?expires=1786536000&signature=a40a511de4825c4082fb24a75b34347e758e409da9e4800255422676feed2199&req=cSYgFsl7lYVbFb4V1XW4gYsbvpoFB14GAsCyxYy9uKdh3G4qbTPcgs%2B9srDW%0AuZg0LfEeYd4rWRKGsvFy4yU6uw%3D%3D%0A)

```
Legenda: Tela do menu de edição do campo com uma seta vermelha apontada para a opção "Bloquear edição por padrão", que está ativada.
```

Veja a seguir que, como a opção está com a edição travada, o campo "valor unitário", ao inserir um produto na proposta, não pode ser alterado.

[![Imagem 8: Veja a seguir que, como a opção está com a edição travada, o campo "valor unitário", ao inserir um produto na proposta,…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326806/060921c05d67e67f8c678414/image.png-expires%3D1619305200-signature%3D0bdbf44f5fe643ced0db19a0fcc3748c9a6f02916bf2d4d971adc2d56c46b327?expires=1786536000&signature=a6d034068e756f9589858707afe7f21c5443065dbe74540a2dd6a89dbc4f9a90&req=dyYuFct4lYFZFb4V1XW4gSD%2BzyhvoaFWS%2FgJdQVrRFcZreioxUMVPX%2BIjQvV%0AlSOYji%2BBRbn3VnZQaE6Q1PC49Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69658896/d9778781f2ce0943f931fec3/image.png?expires=1619305200&signature=0bdbf44f5fe643ced0db19a0fcc3748c9a6f02916bf2d4d971adc2d56c46b327)

```
Legenda: Tela de inserção de produto na proposta, destacando o fundo cinza no campo de "Valor unitário".
```

## Fórmulas simples

Um exemplo de fórmula simples é o mencionado anteriormente, com o desconto aplicado sobre o valor total da proposta. Fórmulas simples são aquelas que não exigem uma condição, ou seja, não dependem de uma informação para serem calculadas.

Vamos considerar um novo exemplo de fórmula simples:

Imagine que você venda um produto cujo valor unitário de tabela é R$100,00, mas na sua proposta comercial, você o oferece com uma margem de 10%.

Para ajustarmos isso, vamos até o modelo de proposta e editaremos o campo "Total" dos produtos da proposta.

![Imagem 9: Para ajustarmos isso, vamos até o modelo de proposta e editaremos o campo "Total" dos produtos da proposta.](https://downloads.intercomcdn.com/i/o/567006297/f5746bba8bdbdf910ac829eb/image.png?expires=1786536000&signature=07ce5c4f25514ddab4eb197824667b08889f54954839b66f3838dc8394322ce1&req=cSYgFsl4n4hYFb4V1XW4gUxcL22t02tVbBMpxgqdR0dIt%2BC2noeJR0qUgvAX%0A2MrFSUJx0K3fkam3XWIMRb89RQ%3D%3D%0A)

```
Legenda: Tela de campos de produtos da proposta, com uma seta vermelha apontando para o ícone de edição ✏️ do campo "Valor unitário".
```

Ao editar a fórmula desse campo, você verá a seguinte expressão:

![Imagem 10: Ao editar a fórmula desse campo, você verá a seguinte expressão:](https://downloads.intercomcdn.com/i/o/567006662/e2a7921867d94d4cef35b6ce/image.png?expires=1786536000&signature=5d3ec803eba22cf0a9819c7688b80e988e1e4272459b73bc6bcbeb460d2f3895&req=cSYgFsl4m4ddFb4V1XW4gdUGFkW0vmi6%2F811qdiqDTcKrxej6BASMKWqAGkV%0Aej8NbGfauHQepaeMGxwKyzmaEw%3D%3D%0A)

```
Legenda: Tela do menu das fórmulas, contendo a fórmula simples: quantidade vezes o valor unitário vezes ((100 menos desconto) dividido por 100).
```

Explicando a fórmula:

"Quantity x UnitPrice" é a quantidade do produto multiplicada pelo valor unitário do mesmo.

"((100 - Desconto) / 100)" é a margem aplicada.

Exemplo:

Quantidade: 2

Valor unitário: R$100,00

Desconto: 10

Cálculo: (2 x 100) x ((100 - 10) / 100) > 200 x 1,1

Resultado: R$220,00

Ela é semelhante à fórmula de desconto da proposta, mas adicionaremos uma margem de 10% no valor total da proposta. Portanto, alteraremos o trecho "((100 - Discount) / 100)" para "((100 + 10) / 100)".

Veja uma aplicação prática:

[![Imagem 11: Veja uma aplicação prática:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326852/84f7cd19469c46d699d06de8/image.png-expires%3D1619305200-signature%3Daa9be8076a2439d048ee6a1fdbb92869e81fbcbefd65bdd7e74f9b732a0a708a?expires=1786536000&signature=93b1ed1ee034a5e9f50c7139f6382a385354572edccd157374c525c736275b94&req=dyYuFct4lYRdFb4V1XW4gRcdHqkyEQSvEQw8BHFNk7EYWTC8dI86psnSPZoX%0A13DpkF2LM9R8NSmpz98dL7%2FJJg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69661506/f9c279031d1db4c7a58d945c/image.png?expires=1619305200&signature=aa9be8076a2439d048ee6a1fdbb92869e81fbcbefd65bdd7e74f9b732a0a708a)

```
Legenda: Tela de inserção de produto na proposta, destacando os valores:
Quantidade: 1;
Valor unitário: R$300,00;
Total: R$330,00.
```

Note que o total dos produtos está acrescido de 10% do valor unitário.

## Fórmulas condicionais

As fórmulas condicionais são aquelas que não são fixas, ou seja, o cálculo varia dependendo de uma informação específica. Esse tipo de fórmula é comumente usado nos cálculos de impostos, como ICMS, ISS, IPI, entre outros.

Vamos ver um exemplo de fórmula condicional:

Suponha que você seja um comerciante generoso e que, sempre que seu cliente faz uma compra acima de R$50.000,00, você concede um desconto de 10%. Como calcular esse desconto?

Primeiro, podemos dizer que é um desconto condicional, aplicado SOMENTE SE o valor total for maior que R$50.000,00.

Como é um desconto aplicado no total da lista de produtos da proposta, precisaremos editar a fórmula do campo "Total" no nosso modelo:

Vá até o menu "Fórmula condicional" do campo "Total"

[![Imagem 12: Vá até o menu "Fórmula condicional" do campo "Total"](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326861/670225d90d9c0fbeaac0a94c/image.png-expires%3D1619305200-signature%3D17f4a93d66b2293f5e15e32c4b54b6bb7adde321fed9c11c2b01ed7855c4a626?expires=1786536000&signature=87b2f63f25c14b8b521c9cc0a34f3d575141971ca8375aec49e0abe1a50e7fa5&req=dyYuFct4lYdeFb4V1XW4gaV21I%2FUnVV1KW%2B1jAq0OIfEJdTuPGLvrbdqLTdX%0AcQLvYfQ7CR9ocijyWwGT7%2F883g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69662230/92203fcc3ba587d5ef466060/image.png?expires=1619305200&signature=17f4a93d66b2293f5e15e32c4b54b6bb7adde321fed9c11c2b01ed7855c4a626)

```
Legenda: Tela de fórmula condicional.
```

Aqui você precisa adicionar uma condição, ou seja, algo que, se satisfeito, resultará em uma ação. No nosso caso, a condição é "Total da lista de produtos da proposta maior que R$50.000,00" e, se verdadeira, a ação a ser tomada é "Aplicar um desconto de 10%".

Veja como fica a nossa fórmula:

[![Imagem 13: Veja como fica a nossa fórmula:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326869/19d5ca626341156f661cd3ed/image.png-expires%3D1619305200-signature%3Dc8655e2c4e9ca25afbbbe7cadaf72fc9e56a811a66778dc74d42581a1009bdb7?expires=1786536000&signature=172f02d88fd578ca96d28cf5e14ea01223275182de4a0599f77869772ac0401a&req=dyYuFct4lYdWFb4V1XW4gcVH8nbVyfkUgcdoOqThRXmw5SocKQaZwqHHdsgd%0AQtE4PYOomeGbj9vrbj0zjKWVfw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69663060/04292741e24eebf0ff4e12ff/image.png?expires=1619305200&signature=c8655e2c4e9ca25afbbbe7cadaf72fc9e56a811a66778dc74d42581a1009bdb7)

```
Legenda: Tela de fórmula condicional, destacando as configurações:
Retângulo vermelho: condição a ser satisfeita;
Retângulo verde: ação a ser tomada se a condição for satisfeita;
Círculo preto: salvar a fórmula criada.
```

Vamos conferir se nossa fórmula está correta! Para isso, criaremos uma proposta cujo valor total dos produtos seja superior a R$50.000,00; observe:

[![Imagem 14: Vamos conferir se nossa fórmula está correta! Para isso, criaremos uma proposta cujo valor total dos produtos seja…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326877/ce0ebcbabfa9ec23d32391c7/image.png-expires%3D1619305200-signature%3D41d3cbd7e5b762885ce18823734ffe0000b2fd7fc590eb284ed8aada4e734f43?expires=1786536000&signature=b43df94edc03fa584fc5fef5b2f50b558843034ed3e5f86b01a4e8d78ce91678&req=dyYuFct4lYZYFb4V1XW4gZryCzypgV%2F8G4WaiMg3DXFVqVr9Hhw0AdhEfn10%0AP%2Bfrrh9qXvm4KJ%2Fpp%2BDPVwQc9w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69669150/3c24927b6b4a739ad20d9e1a/image.png?expires=1619305200&signature=41d3cbd7e5b762885ce18823734ffe0000b2fd7fc590eb284ed8aada4e734f43)

```
Legenda: Tela de inserção de produto na proposta, destacando em verde o campo "Total" que está R$174.900,00.
```

Em verde, vemos que o valor total dos produtos excede R$50.000,00, ou seja, ao calcular o valor total da lista desses produtos, deverá ser aplicado um desconto de 10%.

[![Imagem 15: Em verde, vemos que o valor total dos produtos excede R$50.000,00, ou seja, ao calcular o valor total da lista desses…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326883/e1aca81cf4fb5df0fa2fce05/image.png-expires%3D1619305200-signature%3Debd63cb57c5dd4db19c4dc3e8b33d76550025e2e46e9cf8fa312ce3accbe10e5?expires=1786536000&signature=0518610cb13ebd2b04189f744ae810c907525b56d1780eb4838c1164747a1815&req=dyYuFct4lYlcFb4V1XW4gWgOj6f9%2B2CTw8FkP4%2F1KlrLPu1tAQos7n3OPKvE%0ASKzM%2FHE85Y%2B5mgYLNYXt65ljYg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69669826/73a383e5ab1afe159e23f18c/image.png?expires=1619305200&signature=ebd63cb57c5dd4db19c4dc3e8b33d76550025e2e46e9cf8fa312ce3accbe10e5)

```
Legenda: Tela de produtos inseridos na proposta salva, destacando os totais:
Total do produto sem desconto: R$174.900,00;
Total da proposta: R$157.410,00.
```

Ao gerar a proposta, podemos notar em verde o valor total sem o desconto de 10% e, em vermelho, o valor total da proposta, com 10% de desconto aplicado devido ao preço exceder R$50.000,00.

Para ver um exemplo de fórmula condicional trabalhando com a lógica de impostos, confira [este artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427636933527).

## Campos escondidos

Como você já viu [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427702983959), seu formulário de proposta é configurado através dos campos do seu modelo, ou seja, você preenche as informações da proposta com os campos inseridos no gerador.

Não é sempre que você deseja enviar certas informações ao seu cliente; isto é, alguns dados da sua proposta são necessários para gerá-la, mas podem ser confidenciais ou simplesmente não interessantes para o consumidor final da negociação.

Vamos ver um exemplo de campo oculto:

Voltando ao exemplo dado anteriormente na seção "Fórmulas simples", ao gerar uma proposta com aquele modelo, o cliente final saberia que o valor unitário de tabela é 10% mais barato do que o ofertado a ele.

[![Imagem 16: Voltando ao exemplo dado anteriormente na seção "Fórmulas simples", ao gerar uma proposta com aquele modelo, o cliente…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326891/dc5dd36bb636708acf082c8e/image.png-expires%3D1619305200-signature%3D2a0960d2329f8aafb42575d27ac087341fecb1808c62d188221f076efb90ae6c?expires=1786536000&signature=e741773107b220a88866bcb6114e0bc19c890032e6ffc36594c070242c0a5dac&req=dyYuFct4lYheFb4V1XW4gaFUG8n1S8T52HowpKLlfzOnxYcdI31yHUV4%2BhXM%0Arpg1pVHQuQCWozZ3GlAp6ddGZQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670396/9b3051a11a75434593865273/image.png?expires=1619305200&signature=2a0960d2329f8aafb42575d27ac087341fecb1808c62d188221f076efb90ae6c)

```
Legenda: Tela de produtos inseridos na proposta salva, destacando os valores:
Valor unitário: R$100,00;
Total da proposta: R$110,00.
```

Por isso, podemos ir até o modelo da proposta e ocultar esse campo, veja:

[![Imagem 17: Por isso, podemos ir até o modelo da proposta e ocultar esse campo, veja:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326895/e2d6ed14a49890927443dfd4/image.png-expires%3D1619305200-signature%3D74800f16f4e289aa5c9ce42e99f442c85de4435762c777c4881e35a4716057c5?expires=1786536000&signature=2533e740cb8fd53ca90c860cf2f464267826568a955d659e4d3e4cb77f6b8fd2&req=dyYuFct4lYhaFb4V1XW4gXmg08xI9KqXsvpW280Iv8lcpDh7kTV26VhE5ilk%0ANH4Aw19amW85vxeguyZki8qM1g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670502/f51fc3eabbb4a8738ead2a5e/image.png?expires=1619305200&signature=74800f16f4e289aa5c9ce42e99f442c85de4435762c777c4881e35a4716057c5)

```
Legenda: Tela de produtos no modelo da proposta, destacando o campo "Produtos - a preencher. Valor unitário".
```

Ao clicarmos com o botão direito sobre o campo, podemos escolher a opção "Esconder campo":

[![Imagem 18: Ao clicarmos com o botão direito sobre o campo, podemos escolher a opção "Esconder campo":](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326906/998a4195d5f48c7e5a051cbe/image.png-expires%3D1619305200-signature%3Dd32bed379d137fda7484cc70661a66c1af8f93ae9c3e9e38ab99dde9b4be803b?expires=1786536000&signature=95830a6d12ec1535d75c5d5eee22e194e828b866dd76dac8ed312af4b0f74c01&req=dyYuFct4lIFZFb4V1XW4gTqcjfrUkN7QA369D9L6PoLGtqEijRXnyHQKKemZ%0AhqB0aWCFJCKlhrmz7OynSahq5g%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670549/8fde0daea63f7f6576e9a51a/image.png?expires=1619305200&signature=d32bed379d137fda7484cc70661a66c1af8f93ae9c3e9e38ab99dde9b4be803b)

```
Legenda: Tela de opções do campo ao clicar com o botão direito, destacando a opção "Esconder campo".
```

Observe como o campo não aparece mais no modelo:

[![Imagem 19: Observe como o campo não aparece mais no modelo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326914/2a07689fd454e1aadf337a21/image.png-expires%3D1619305200-signature%3D5e89bc9afc72a81d4a1793ceb0b424821d02ee8758caa8edc1077a8db7249ba8?expires=1786536000&signature=39467831f919bcc25fd22b7c15434625cbb29f851a7411770956c8b6e9070a28&req=dyYuFct4lIBbFb4V1XW4gZjJ6OK5Hy69mRFx7vGRD%2Fn3qxN1ZTfTuKM3T8Lf%0A39YLShWFaD%2BZAdDdpmCAjXrlsg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670611/0b2441e747a719f040af5277/image.png?expires=1619305200&signature=5e89bc9afc72a81d4a1793ceb0b424821d02ee8758caa8edc1077a8db7249ba8)

```
Legenda: Tela de produtos no modelo da proposta, destacando o espaço em branco onde ficava o campo "Produtos - a preencher. Valor unitário".
```

Obs.: Para reexibir os campos ocultos do seu modelo, basta clicar nesta opção do seu menu de ações:

[![Imagem 20: Obs.: Para reexibir os campos ocultos do seu modelo, basta clicar nesta opção do seu menu de ações:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326919/af2d4775e6d5f8e8927b3028/image.png-expires%3D1619305200-signature%3D8bd954a5c6d07e5ed447978eaa11ac399e616edfea122d88f22ada29814796d8?expires=1786536000&signature=5faebea2afa051dcae400e347160868db20887158d03b07b5162f74da342f85b&req=dyYuFct4lIBWFb4V1XW4gdMu3YggJ%2Brb05NS6L0PIWrTHubZOil2FCP3enGl%0AER4HrSvXynVmUEpsTpE8bjbZcg%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670637/fcc7b2ca362ed0c2bc888d62/image.png?expires=1619305200&signature=8bd954a5c6d07e5ed447978eaa11ac399e616edfea122d88f22ada29814796d8)

```
Legenda: Menu de ações do modelo da proposta, destacando o ícone de controle de campos ocultos.
```

Ao gerar uma nova proposta, veja como o valor unitário não aparece mais:

[![Imagem 21: Ao gerar uma nova proposta, veja como o valor unitário não aparece mais:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326921/c03c84f0cd22d7d1d09f0e0f/image.png-expires%3D1619305200-signature%3Dd2999ce81e831b379ef8dec98ecd36aaca8fbcd9b79eabc570b1c33edda35229?expires=1786536000&signature=f8711226b8f1b5465adc68b767d91f5422bd475c1b57625e96b0fca282fc9b85&req=dyYuFct4lINeFb4V1XW4gdQ0VJiiInnaLt8%2B2DkEV9Da1%2BAMJDz8UAh0Cexz%0AXedBGlcxt3RDpyXBDuUbCbu1fA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670817/f97c25472266a40fe9bdfd8d/image.png?expires=1619305200&signature=d2999ce81e831b379ef8dec98ecd36aaca8fbcd9b79eabc570b1c33edda35229)

```
Legenda: Tela de produtos inseridos na proposta salva, destacando o espaço em branco onde ficava o valor unitário do produto.
```

Você também pode ocultar outros campos que não deseja que apareçam na sua proposta, como por exemplo, "Prazo de entrega".

Para isso, vá até o modelo e oculte o campo "Prazo de entrega":

[![Imagem 22: Para isso, vá até o modelo e oculte o campo "Prazo de entrega":](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326930/1595ba7d3e444c0b7d27555e/image.png-expires%3D1619305200-signature%3D0bece05e33eba5dc3212e50f163126ac85ef2cc63c09650733892e1ba4c88d50?expires=1786536000&signature=7f87984f223c9df3a0bac05c0e2dd0e45847eb862abcc002ca1aa6042209c9a9&req=dyYuFct4lIJfFb4V1XW4gcBHtlLWJx13XkJESR4rWLR9ADnkxzzddMam9J9E%0Az%2Bbe5EZgi9JImf1xjYEtgvkA5Q%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670885/767540f2f2ab3b9717558741/image.png?expires=1619305200&signature=0bece05e33eba5dc3212e50f163126ac85ef2cc63c09650733892e1ba4c88d50)

```
Legenda: Tela de opções do campo ao clicar com o botão direito com a seta apontada para "Esconder campo".
```

Veja que o prazo de entrega é de 25 dias:

[![Imagem 23: Veja que o prazo de entrega é de 25 dias:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326939/38994b895e3f7ff65bf892cd/image.png-expires%3D1619305200-signature%3D1e46bd2d3484f005631f6482238f97424a5b33f6ad6fe233e89de64fde10d6fe?expires=1786536000&signature=fba48e9fe3d70c93c0a2b3fc94f2d9cc8b8f50814aba655e3a78c1e9ddcfa984&req=dyYuFct4lIJWFb4V1XW4gU1nUZT3TcjVJGzAnvWhFaKgLKXBEAiu4hJq7J0z%0AMNcSCn%2BAhv6fs8gyH2MnvIvd4w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670933/7ac5591cfc5eea52391c2ea3/image.png?expires=1619305200&signature=1e46bd2d3484f005631f6482238f97424a5b33f6ad6fe233e89de64fde10d6fe)

```
Legenda: Tela de inserção de produto na proposta, destacando o campo "Prazo de entrega" com o valor de "25 dias".
```

Mas na proposta, ele não é exibido, pois o campo está oculto!

[![Imagem 24: Mas na proposta, ele não é exibido, pois o campo está oculto!](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326943/2526ea324c0f7ebe81516779/image.png-expires%3D1619305200-signature%3D8fdce75ccdfb77904c863133be5f7c064da0ba7c412c8b0fd8d3acf91c252c24?expires=1786536000&signature=7f2855a3aa8e541032813a3ff79e8d3e846bb43c6878db6dd66b2c7c28fcd6be&req=dyYuFct4lIVcFb4V1XW4gaO%2BTHp9ojv3T9NVLhYQIYhrVLARBqrX5BvyAnc2%0AF%2FNDFUVtFZEctKUbnrk1kJc1OQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69670957/396fe21f2e3ec3f816829732/image.png?expires=1619305200&signature=8fdce75ccdfb77904c863133be5f7c064da0ba7c412c8b0fd8d3acf91c252c24)

```
Legenda: Tela de proposta salva, destacando o espaço em branco onde ficaria o prazo de entrega.
```

A função de ocultar campos também é útil caso você queira adicionar uma informação apenas no formulário, mas não quer que ela seja exibida na proposta, como por exemplo, "Transportadora".

Digamos que ao criar um negócio dentro do Ploomes e incluir a proposta, você precise cadastrar a Transportadora responsável por esse negócio, mas não quer que essa informação saia no seu PDF.

Primeiro passo: insira o campo "Transportadora" (criado) no seu modelo:

[![Imagem 25: Primeiro passo : insira o campo "Transportadora" (criado) no seu modelo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326950/40c22b6e6c006aa170e0384c/image.png-expires%3D1619305200-signature%3Db529eec4414b86abddf50a3f2541751be77db463a5d00f197498846b93349b20?expires=1786536000&signature=d1acd700f308f747a75f5bb3a2a33c114a987b8e42c695e4d5298de0ab43b8d1&req=dyYuFct4lIRfFb4V1XW4gWFeuFljssJfBM3OciffbFWQdbXVlreUTw40%2FjwA%0A0m0c06A5sg2miY6gBNMrsnnnuA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69671391/5f3aacb2defa56db064e3446/image.png?expires=1619305200&signature=b529eec4414b86abddf50a3f2541751be77db463a5d00f197498846b93349b20)

```
Legenda: Tela de campos de proposta, com destaque no campo "Transportadora", indicando que clicar nele faz com que seja inserido no modelo.
```

Segundo passo: oculte o campo:

[![Imagem 26: Segundo passo: oculte o campo:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326960/5b9c1528297367315ac727d9/image.png-expires%3D1619305200-signature%3Da24690c72f585b1b1a5f4397627684609d9ee98cfdb9e993a55c908e92397675?expires=1786536000&signature=3a28ce40dbfe965e3c7eeeffe8e611726001a9378c77bd98f7d3b49e93990066&req=dyYuFct4lIdfFb4V1XW4gZtIyyMbkJvTYopUDYYs1xKGVlh8%2B%2FOZJcgwbO8%2F%0A%2B0inJjJxVROC4tjPXgHS1w8jPA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69671409/fcf50501ba89e5a3579da20a/image.png?expires=1619305200&signature=a24690c72f585b1b1a5f4397627684609d9ee98cfdb9e993a55c908e92397675)

```
Legenda: Tela de opções do campo ao clicar com o botão direito, com a seta apontada para "Esconder campo".
```

Terceiro passo: salve o seu modelo e veja como fica o seu formulário!

Podemos notar que ao inserirmos a proposta, o campo de "Transportadora" é exibido no formulário:

[![Imagem 27: Podemos notar que ao inserirmos a proposta, o campo de "Transportadora" é exibido no formulário:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326973/4a94c240656980d1558bb7c9/image.png-expires%3D1619305200-signature%3D9a1e9aa066b0cead0f5cf0efdaef37326ea3a7c5213d6fd9e66848ce66a8bdc9?expires=1786536000&signature=432af7cf31c1cdcb80e1ea5439d3756af87d749c20a8660bc335a0faa5ca48db&req=dyYuFct4lIZcFb4V1XW4gX3XvmU5w1FYj1dz%2BsDFYI45pRXmz0SEdYLg4uLQ%0AbEuhxTNNC1ThRkIQFcmkHfKLxw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69671449/e27e1a82ba1c4d341e50d2f1/image.png?expires=1619305200&signature=9a1e9aa066b0cead0f5cf0efdaef37326ea3a7c5213d6fd9e66848ce66a8bdc9)

```
Legenda: Tela de proposta, destacando o campo "Transportadora".
```

Mas ao salvar a proposta, esse dado não aparece!

[![Imagem 28: Mas ao salvar a proposta, esse dado não aparece!](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326979/5f5f1cfb7b6991f216d7d94a/image.png-expires%3D1619305200-signature%3Dbe0f94a6dc241956553a6acc101e7957efdb5afb263b6394b52d3174f55f6b68?expires=1786536000&signature=a5c929077d9833ca1b455b6868af4e5c645f8e539ab13f1375fd6919bc10c2f0&req=dyYuFct4lIZWFb4V1XW4gciNi2WDZ3NVe6wWQLCwzvwovuAIxT%2F745Gnpapw%0AkuKWCdUcM%2BrZULx8wYaDy48hnw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69671489/957b932d3f2e31fb2bcfd325/image.png?expires=1619305200&signature=be0f94a6dc241956553a6acc101e7957efdb5afb263b6394b52d3174f55f6b68)

```
Legenda: Tela de proposta salva, destacando o espaço em branco onde ficaria a transportadora.
```

## Filtros nos produtos da proposta com grupos

Para obter mais informações sobre a tela de produtos, recomendamos a leitura [deste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427660389271) antes de prosseguir.

A disponibilização de filtros a partir dos grupos de produtos é um excelente processo caso você possua muitos produtos em um único grupo ou muitas informações semelhantes dentro de um grupo específico e queira que essas informações sejam filtros, a fim de tornar a sua pesquisa, e portanto, a inserção de produtos na proposta, mais rápida e eficaz.

Vamos ver um exemplo prático de filtros dentro dos grupos de produtos.

Através do seu modelo de proposta, dentro de uma lista de produtos, você pode seguir esse caminho:

[![Imagem 29: Através do seu modelo de proposta, dentro de uma lista de produtos, você pode seguir esse caminho:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369326987/d4579728393ee52ecf935c5d/image.png-expires%3D1619305200-signature%3Df042efe4b5b950b768124cdcfa46267d33bbe0352102d78cd3a5f0e3b464570c?expires=1786536000&signature=8cdaad511af4d59149fe4b8f2e48864e5dde8777a8a4e4ef8603a19d10d0896a&req=dyYuFct4lIlYFb4V1XW4gX18GIXm%2B91psdHvat3tMPgn0uE25zRg%2FoxPTFsP%0AWLgJKoAE7uFSbCrG6LIeJEV0Pw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69673831/c7a87337eae5145cb6bab1fd/image.png?expires=1619305200&signature=f042efe4b5b950b768124cdcfa46267d33bbe0352102d78cd3a5f0e3b464570c)

```
Legenda: Tela de opções do campo ao clicar com o botão direito, destacando a opção "Detalhes da seção".
```

Ao clicarmos com o botão direito em uma tabela de produtos, podemos selecionar os detalhes da seção, isto é, podemos nomear a seção, além de filtrarmos que grupos de produtos podem ser exibidos nessa seção!

**Se você vende tanto produtos quanto serviços, esse é um ótimo jeito de separá-los no seu modelo de proposta!**

**Crie uma seção para cada um, e escolha apenas os grupos que sejam de produtos ou que sejam de serviços.**

[![Imagem 30: Crie uma seção para cada um, e escolha apenas os grupos que sejam de produtos ou que sejam de serviços.](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327000/9da2d299fe002357dfcc7164/image.png-expires%3D1619305200-signature%3Da4e7f5cd98bc5afa4ec795e4de974ba9c68e9c3914fb171c4fc94dd1a6f51051?expires=1786536000&signature=8e7e73e38ca7d9221886cfe6816fc796dd64566805f85b6f5099e315ee34ab40&req=dyYuFct5nYFfFb4V1XW4gbwM6tsE%2F5YGR1RJXI8x%2BN2e3gtEglqmJdP%2F8mSY%0AfzBxoJZf1bWY0hiU48vKYko1kA%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69674057/7ee67ea4fa734dcaf4fa7652/image.png?expires=1619305200&signature=a4e7f5cd98bc5afa4ec795e4de974ba9c68e9c3914fb171c4fc94dd1a6f51051)

```
Legenda: Tela de detalhes da lista de produtos, destacando o botão "Editar filtro dessa tabela de produtos".
```

Agora, você pode escolher os grupos que serão exibidos nessa seção:

[![Imagem 31: Agora, você pode escolher os grupos que serão exibidos nessa seção:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369327003/314cb7536ec60e1610d41de8/image.png-expires%3D1619305200-signature%3Dc5b4f6add5725f0e2887de2e9dbadb9fe66467335357a822b7c79631203b0f52?expires=1786536000&signature=fdcb62635e98a6b15bfc704a41f7e8def5843e5f6ee135cad22b6e95d2c3d58b&req=dyYuFct5nYFcFb4V1XW4gc9ZBLdWwWYCCetK8nG6jULFNqydPl1jlUXcbMyi%0A96FeyvGBm6pLzOyWQ5TTenWqfw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/69674105/8949162190d37410210f16ac/image.png?expires=1619305200&signature=c5b4f6add5725f0e2887de2e9dbadb9fe66467335357a822b7c79631203b0f52)

```
Legenda: Tela da edição de filtro da tabela de produtos, destacando as opções de grupo para selecionar em "Selecione quais grupos de produtos essa tabela irá exibir".
```

Nesse caso, escolhi o grupo "serviços", já que é uma seção de serviços.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## Em conclusão

Neste artigo, vimos a importância das fórmulas no cálculo das suas propostas comerciais, além da funcionalidade "esconder campos" e ainda, filtros dentro dos grupos de produtos!

Para mais conhecimento, acesse a nossa Central de Conhecimento em [suporte.ploomes.com](https://suporte.ploomes.com/)

Até a próxima!
