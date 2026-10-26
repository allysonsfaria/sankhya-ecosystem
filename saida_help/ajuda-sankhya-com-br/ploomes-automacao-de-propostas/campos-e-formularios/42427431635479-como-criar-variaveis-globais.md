---
id: "42427431635479"
titulo: "Como criar variáveis globais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427431635479-Como-criar-vari%C3%A1veis-globais"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-11T16:14:50Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452344", "sync_hash_83f9ee30b273"]
---

# Como criar variáveis globais

## Este artigo visa explicar como criar variáveis que possam ser utilizadas para diferentes contextos

**INTRODUÇÃO**
O Ploomes permite que novos campos sejam criados para suas entidades (Leads, Clientes, Negócios, Produtos, etc), mas existem variáveis que não pertencem a um produto, cliente ou negócio específicos. Elas são variáveis globais, ou seja, que precisam ser acessíveis e compartilhadas para a conta como um todo. Além disso, é bastante prático poder centralizá-las em um único ponto para facilitar o gerenciamento. Assim, uma vez que seus valores são alterados, a alteração é automaticamente refletida para todas as entidades de sua conta que a utilizam.

Imagine que a composição do preço de seus produtos leve em consideração algumas variáveis como por exemplo:

1. Cotação do dólar
2. Fator (valor numérico que multiplica o preço de acordo com algum critério interno)
3. Desconto promocional
4. Margem de lucro

Entre várias outras possibilidades. Todas essas variáveis mencionadas não fazem parte de um escopo específico e podem ser compartilhadas entre várias entidades. Pegando como base o exemplo que utilizamos neste artigo, sempre que seus valores forem alterados, a mudança precisa ser refletida diretamente na precificação de produtos e serviços nas propostas e nas vendas.

**SOLUÇÃO**
Para casos como este, a solução é criar campos para a **Empresa**. Na tela de edição de campos é possivel criar uma seção e campos para isso, como mostrado abaixo:

![Imagem 1: SOLUÇÃO Para casos como este, a solução é criar campos para a Empresa . Na tela de edição de campos é possivel criar…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2250914840/d50cf274f47214e4fd8be2758fa5/image.png?expires=1786536000&signature=679170a39333d078dfd0cf47a17eb002b623698d3f00a89a51174012425ed305&req=diIiFsB%2FmYlbWfMW3nq%2BgeBaqhZ8r6J2BGzr1hqPWNWrp9oaGQiCQeLypk04%0A7bEHM185%2BMQcWVA3twgx%2Ban%2BjS8%3D%0A)

Na imagem podemos ver os campos de exemplo já criados. Para acessar esta tela basta clicar em **"Administração" > "Campos e formulários"**. Para criar os campos necessários basta clicar em **"Novo campo"** . Para saber mais, o link a seguir detalha como criar campos em formulários:
**[Link para criação de campos](https://sankhya.zendesk.com/hc/pt-br/articles/42427491040791)**

Com isto feito, você pode ir até a tela de administração(**"Administração" > "Dados da empresa")** e informar os valores atuais destes campos, como exibido na próxima imagem:

![Imagem 2: Com isto feito, você pode ir até a tela de administração( "Administração" > "Dados da empresa") e informar os valores…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2250919495/1e5f87332e8806b3ec607565e370/image.png?expires=1786536000&signature=9baea37c160590e27b8817c3b88163afa799e54ed9dedc34ce3db7c0cac0f91e&req=diIiFsB%2FlIVWXPMW3nq%2BgR6FKJgAYjR9LqLPNNWeTBmHoFm66I4ykznAsT97%0ArRyOOtOzZfCgl4OYvfJmVtahY5g%3D%0A)

Depois de atribuir um valor para os campos já é possível utilizá-los em fórmulas de propostas, por exemplo:

![Imagem 3: Depois de atribuir um valor para os campos já é possível utilizá-los em fórmulas de propostas, por exemplo:](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2250926435/288e636a426ff99a07ff19e3ed20/image.png?expires=1786536000&signature=416b8175a91c16ce948a25614809e16091fead7e79663c3b2fcc2f930bac07b3&req=diIiFsB8m4VcXPMW3nq%2BgfsKpOEVcaYdL5nL4XJWsAPNDo1Jf4ZgiBQI2sef%0Asah0xKRTudTg%2BBiSZ2Ks1Z5egHg%3D%0A)

Agora todas as propostas geradas conseguirão ler os valores destes campos Globais e sempre que você precisar fazer algum ajuste, basta ir até a Administração e alterar seus valores ("**Administração" > "Sua empresa"**) e essa mudança refletirá automaticamente em todas as propostas geradas à partir deste momento.

Este é apenas um exemplo de uso. Como mencionado anteriormente, estas variáveis ficam acessíveis para a conta toda e podem ser utilizadas para diferentes finalidades e em diferentes entidades. Uma outra dica prática é que elas podem ser atualizadas com a frequência necessária via API, automaticamente. No exemplo da cotação do dólar, é possível criar um serviço que diariamente busque a cotação do Banco Central e atualize na conta.

Uma outra vantagem para esta abordagem é que o usuário final não precisa saber quais os valores que estão sendo trabalhados, já que a configuração destas variáveis é restrita aos administradores. No momento da geração da proposta, por exemplo, o Ploomes utilizará os valores definidos porém estes não serão visíveis no formulário.
