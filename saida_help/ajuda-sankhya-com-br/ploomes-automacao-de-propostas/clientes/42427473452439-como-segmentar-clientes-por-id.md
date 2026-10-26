---
id: "42427473452439"
titulo: "Como segmentar clientes por ID?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427473452439-Como-segmentar-clientes-por-ID"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-11T16:14:42Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452146", "sync_hash_e2b738502813"]
---

# Como segmentar clientes por ID?

Caso sua base de clientes possua mais de 50 mil itens (linhas), não será possível exportar a aba completa de uma única vez.

Nessa situação, você pode criar **abas segmentadas por ID**, dividindo os clientes em intervalos específicos. Dessa forma, será possível exportar toda a base em partes, garantindo que nenhum registro fique de fora

## Como realizar a criação?

Primeiramente, adicione a coluna **ID** na aba que deseja exportar, para que seja possível visualizar e organizar os registros por intervalo antes de realizar a exportação.

- Acesse a tela de **Clientes;**
- Clique no ícone de **engrenagem** ao lado das colunas;
- Adicione a coluna **ID** para visualizar essa informação na listagem;
- Aproveite para incluir também as demais informações que deseja exportar.

[GIF animado: Imagem 1: Aproveite para incluir também as demais informações que deseja exportar.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053908907/e0ca909c875f6cd2e72b728a4565/configurarColunas.gif?expires=1786536000&signature=810b341948c91d9cc005cf2d956e3b9c9a9a5caffbd22dcd0ae488933d028586&req=diAiFcB%2BlYhfXvMW3nq%2BgdASifpkTdQLS1fsyHIGFK6Tq%2BIjzZzut23lEzb0%0Ae%2BwBljiW1kZRB2Q97NslIBHxZJo%3D%0A)

Após adicionar a coluna **ID** na aba, clique sobre o título da coluna para ordenar os clientes, organizando-os do **menor para o maior ID**.

![Imagem 2: Após adicionar a coluna ID na aba, clique sobre o título da coluna para ordenar os clientes, organizando-os do menor…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2053937484/41113499d717c7555573348588dc/image.png?expires=1786536000&signature=c752c79bb1b8823bafcf1f6c5a91b41935544853bee07b16f3d6eb01ecd6d0cb&req=diAiFcB9moVXXfMW3nq%2BgS62zXpQk8Li71eTiTljwR4V7H8KhdhRmnjfD5P8%0Ae%2BTXNEIbsBhqVuvhjo3iLE%2Fb3aU%3D%0A)

Anote o **ID mais baixo** exibido na listagem para utilizá-lo como referência no filtro. No exemplo, o menor ID identificado é **604000116**.

Em seguida, avance pelas páginas da listagem até identificar o **último ID** que fará parte desse primeiro intervalo. No exemplo, o maior ID considerado será **605790754**.

Agora, crie uma **Nova aba** (ou duplique a aba existente para manter as mesmas colunas e configurações) e adicione o seguinte filtro com base no intervalo identificado:

![Imagem 3: Agora, crie uma Nova aba (ou duplique a aba existente para manter as mesmas colunas e configurações) e adicione o…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2054036107/b1f26ea910beabdf4a9bf24823fb/image.png?expires=1786536000&signature=10b7100b636d34b7bcb97677655c9cf00a02f7dbac7eaeff204e9604a79fc5e8&req=diAiEsl9m4BfXvMW3nq%2BgaJooI36MXziq1fH6L1tmoDc9oGUp6rC1dQnq%2F8Q%0AdnhPqYt%2B%2BrJXEGAe%2Fq7Do0rEGSI%3D%0A)

Após criar a primeira aba com o intervalo de IDs, duplique essa aba para manter a mesma configuração de colunas e filtros. Em seguida, substitua o **ID mínimo** pelo **ID máximo** utilizado na aba anterior, e defina um **novo ID máximo**, correspondente ao próximo intervalo de registros.

Repita esse processo até segmentar toda a base de clientes.

![Imagem 4: Repita esse processo até segmentar toda a base de clientes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2054136924/82ae4bc0174fd399220434c8f907/image.png?expires=1786536000&signature=c57d70562c216b0e48ff564390986bf3c9f83afd30315964b6c09bb2fb26083b&req=diAiEsh9m4hdXfMW3nq%2BgQidghtN%2B%2FEWyDLV3iKpjTlfqy%2F1Wi0gDw27ft0p%0AFjoVwEvKCaM%2FfVFrA9WhBoTfspg%3D%0A)

Dessa forma, você conseguirá exportar todos os registros em partes, respeitando o limite de exportação da plataforma.

Veja também:

[Como exportar abas pelo Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427507239063)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
