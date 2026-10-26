---
id: "42427698324887"
titulo: "Reciclagem de negócios perdidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427698324887-Reciclagem-de-neg%C3%B3cios-perdidos"
trilha: "PLOOMES: Automação de propostas  > Negócios e funis"
atualizado_em: "2026-08-11T16:13:53Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452167", "sync_hash_abc8d04795cd"]
---

# Reciclagem de negócios perdidos

Veja como as automações podem ajudá-lo a segmentar sua base de clientes e recuperar oportunidades perdidas

Esse artigo é uma boa prática e, para fins didáticos, partiremos do seguinte cenário hipotético:

“Preciso segmentar minha base de clientes para saber quais possuem negócios perdidos e tentar recuperá-los com uma ação de marketing”.

Os passos, de maneira geral, para fazer isso acontecer, são os seguintes:

- Definir um critério para diferenciar os clientes que perderam um negócio dos outros clientes.
- Criar uma aba no módulo de clientes os segmentando por esse critério
- Criação de uma automação para que, sempre que um negócio for perdido, o Ploomes edite esse critério, levando o cliente desse negócio para a aba criada.

**Definição do critério:**

Podemos criar um campo personalizado para separar nossa carteira de clientes, mas nesse caso de uso, vamos utilizar o campo “marcadores”. Para isso, criaremos o marcador “reciclagem”, na cor vermelha (personalizável), clicando em Clientes > Menu > Configurar marcadores de clientes:

[![Imagem 1: Podemos criar um campo personalizado para separar nossa carteira de clientes, mas nesse caso de uso, vamos utilizar o…](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369323669/32edbaa4816b3f17068571b6/image.png-expires%3D1619229600-signature%3De05ea022b705f3c3f02cceb38a667d01f5ff6164adc4c71fbcd8eb2b3729cc78?expires=1786536000&signature=2a1a503ad43ef9cec3160607b632ddfd11da8f37ce27361ea34f185dc8af69b7&req=dyYuFct9m4dWFb4V1XW4gbkprT%2BS3OXqdqn5CgPDjBnwITDKuNT2q8BtSeUU%0AJcf85PlpKnJBQqpKWtLm2lLcXw%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/109396057/1cf0e88c35db866fd7d999da/image.png)

**Criação da aba:**

Agora vamos criar uma nova aba com o seguinte filtro:

[![Imagem 2: Agora vamos criar uma nova aba com o seguinte filtro:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369323675/7183c4434c7d80404e40d27c/image.png-expires%3D1619229600-signature%3Dc9e7e2e5c3169b7ed280b5cc1aa35e54b6e5b723741988b04a55e268b974a37f?expires=1786536000&signature=b9de5c51f037aaf308edbc108ce4c6ff3f86566b8fc52cdf6947fd7e93cf0747&req=dyYuFct9m4ZaFb4V1XW4gQGM2jjYOGpvVCxjd5dZFLVkrmYfir9NPkhq%2BLZ7%0A698JvfjSIXssseKMUYx%2BzJGvag%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/109396148/d541660da57353b4f6e596ce/image.png)

Ou seja, sempre que um cliente possuir esse marcador, ele será transportado para essa aba.

**Controle automático dos marcadores:**

Vamos criar a seguinte automação em TODOS os estágios do funil de vendas:

[![Imagem 3: Vamos criar a seguinte automação em TODOS os estágios do funil de vendas:](https://ploomes-52ceb6b026db.intercom-attachments-7.com/i/o/369323683/6fd5432e6d37e0d9b31261c3/image.png-expires%3D1619229600-signature%3D1029302c5ecd79659853ae7dc63c958f1d29b87f707dd495defcee1df77db1e5?expires=1786536000&signature=7b1bb7a3dd55a7e31fa2eb8de4f2238ccb22c8ed9268b9d8984d7bf4559a7d6d&req=dyYuFct9m4lcFb4V1XW4gVj5H81ApepYMmC2P6MQxX35yCU3yugHd6VbXQD%2B%0AK%2FjM7tV%2BStxAYKz4GpY98uXx2A%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/109396255/e0d068681cf5e8b74e0b4f71/image.png)

Com essa regra, adicionaremos o marcador “reciclagem” em todos os clientes cujo negócio for perdido, independente do estágio, fazendo com que eles sejam enviados automaticamente para a aba previamente criado, trazendo visibilidade e poder para tomada de decisão por parte do nosso cliente.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

Bônus:

Integração com Mailchimp! Podemos integrar as abas do módulo de clientes com o Mailchimp, plataforma de e-mail marketing, para automatizarmos e enviarmos de forma massiva, e-mails para recuperação de clientes perdidos. Para saber mais sobre essa integração, acesse [esse](https://sankhya.zendesk.com/hc/pt-br/articles/42427459357719) link.
