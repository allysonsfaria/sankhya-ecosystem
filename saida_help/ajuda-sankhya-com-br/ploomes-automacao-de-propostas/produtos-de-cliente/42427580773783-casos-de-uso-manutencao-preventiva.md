---
id: "42427580773783"
titulo: "Casos de uso - Manutenção preventiva"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427580773783-Casos-de-uso-Manuten%C3%A7%C3%A3o-preventiva"
trilha: "PLOOMES: Automação de propostas  > Produtos de Cliente"
atualizado_em: "2026-08-11T16:14:26Z"
rotulos: ["sync_hc", "ploomes", "ploomes_7956529", "sync_hash_27367002d10e"]
---

# Casos de uso - Manutenção preventiva

Para este caso, vamos usar de exemplo uma empresa que possui um time especializado em manutenções preventivas. Essas manutenções são geradas automaticamente com base na periodicidade de cada produto.

Dentro deste contexto, vamos montar uma automação de produto do cliente para criar uma tarefa quando chegar o momento da manutenção do produto.

1. Verifique se os produtos estão cadastrados de forma correta no Ploomes;

   Para detalhes do módulo de produtos do cliente, clique aqui.

2. Criar um campo de Data que guarde a informação da periodicidade da manutenção do produto;

![Imagem 1: 2. Criar um campo de Data que guarde a informação da periodicidade da manutenção do produto;](https://downloads.intercomcdn.com/i/o/752944434/f4f6ab74d1346a2755c84fe2/image.png?expires=1786536000&signature=801ebf0dc8446933ba7ce856f0d0894b870039349dcc37a5b04755140ded300d&req=cyUlH816mYJbFb4V1XW4gQP2qIKWpGmlcHMtHko5Ujhv8KwEkI%2FTbDQrcKta%0A%2Bev2iSH%2FpPLcZLasyE8UIlZSKg%3D%3D%0A)

![Imagem 2: 2. Criar um campo de Data que guarde a informação da periodicidade da manutenção do produto;](https://downloads.intercomcdn.com/i/o/752948178/3b9dfd53cc687999e272366a/image.png?expires=1786536000&signature=75d0983ba47855cb179be7745d7706614d4e8d7a62567b82edbd85c458bcfaba&req=cyUlH812nIZXFb4V1XW4ge9Y%2FDuy0Yz%2BjNRWQPSIvzc7uMkjhdksK4xsOl1p%0ACm%2Bmz7C1t1FWtLjH74T9ErlBEA%3D%3D%0A)

Dentro do contexto do nosso caso, você deve preencher o campo de data, com a data da última manutenção que ocorreu.

3. Vamos criar a automação para notificar o responsável sobre a manutenção.

A automação fica com a seguinte configuração:

Adminstração > Automação > Produto de Cliente

![Imagem 3: Adminstração > Automação > Produto de Cliente](https://downloads.intercomcdn.com/i/o/752949011/63b893320dc76ad2030b6fb4/image.png?expires=1786536000&signature=c4b8d3811772063dafc7753c38824c452a0127c73c3020c04018911bdee104e3&req=cyUlH813nYBeFb4V1XW4gU96lHiwM32kSIBYsNw%2FovU8pFeGali8IiDJmbpr%0AOfih3Fh%2FBeB6mU%2F00YEJjrjynw%3D%3D%0A)

![Imagem 4: Adminstração > Automação > Produto de Cliente](https://downloads.intercomcdn.com/i/o/752949661/4a7a8270be557d354433ef83/image.png?expires=1786536000&signature=9dc2399d9a16b2cc1dd26b67d845190a393730bd262ed785999ce6fa8e1b7cdc&req=cyUlH813m4deFb4V1XW4gZ3vsy4OH7ySy%2FbTtVyrAPjk37%2FMStYXll6HKn7s%0ASc%2F4QwmQ2aryWWQ%2BuWJExh2H0A%3D%3D%0A)

![Imagem 5: Adminstração > Automação > Produto de Cliente](https://downloads.intercomcdn.com/i/o/752949837/d2c087f922a0d6bd9c77b823/image.png?expires=1786536000&signature=4545b0c1f3479c8830b06e161e1c98387f64d1f6cb4a3ee23c21b62075c2b3de&req=cyUlH813lYJYFb4V1XW4gSdI5cOdgZt7qDTxV2ZG5OW3l3twQ3SV7gADp4j3%0A2i6LQ6gRRp3pPqx%2FYLKiGIgg2w%3D%3D%0A)

![Imagem 6: Adminstração > Automação > Produto de Cliente](https://downloads.intercomcdn.com/i/o/752950511/57af65aacdce695cfc99a5f4/image.png?expires=1786536000&signature=ea2d210caba7b3be2b15e7156be5a9903bd50f6b003a5e103ffc6de75c1e7c2e&req=cyUlH8x%2BmIBeFb4V1XW4gckde8m%2BVWSK9QtHWX5IzcAgKUtHv%2FBf4KvA4Pri%0A6gxjW8m%2Foe5g192MA0AMIJJHCg%3D%3D%0A)

Utilizamos o filtro desta forma, para rodar todo dia. A automação vai pegar todos os produtos que estão há 180 dias (6 meses) sem manutenção, assim a automação roda e cria a tarefa para o usuário.

Caso você queira uma manutenção com menos tempo, você pode utilizar o filtro de "últimos N dias" com 80 dias e outro com 79 dias, para pegar a data exata, como mostrado no print acima.

Caso queira saber mais sobre produtos de cliente, clique aqui.

---

Esse artigo te ajudou? Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

Ficou com alguma dúvida? Não hesite em chamar o Suporte pelo chat.
