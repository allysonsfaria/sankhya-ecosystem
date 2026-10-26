---
id: "42427524600855"
titulo: "Importação de Produto Pai e Filho (Opcionais)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427524600855-Importa%C3%A7%C3%A3o-de-Produto-Pai-e-Filho-Opcionais"
trilha: "PLOOMES: Automação de propostas  > Produtos"
atualizado_em: "2026-08-11T16:14:36Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5616948", "sync_hash_b06866e0c54c"]
---

# Importação de Produto Pai e Filho (Opcionais)

Antes de realizar a importação para produtos pai e filho, você pode [aprender tudo sobre a tela de produtos.](https://sankhya.zendesk.com/hc/pt-br/articles/42427660389271)

## Conceito

Os produtos filhos ou opcionais são como os outros produtos da base, porém, eles podem ser vendidos tanto de maneira avulsa, quanto como parte de um outro produto.

Um produto X ser opcional de um produto Y não significa necessariamente dizer que o produto Y também é opcional do produto X. A inclusão de opcionais, hoje, precisa ser feita de maneira manual ou através de importação, uma vez que é um vínculo de alguns produtos específicos.

Incluir opcionais significa que, ao criar uma proposta onde você esteja vendendo esse produto (pai), o Ploomes automaticamente sugere outro produto (filho/opcional) para fazer parte desse negócio.

Ao clicarmos no nome do produto recém criado, podemos clicar em "Opcionais", e essa nova tela irá se abrir:

![Imagem 1: Ao clicarmos no nome do produto recém criado, podemos clicar em "Opcionais", e essa nova tela irá se abrir:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369325459/21377e1283c66de4f5670d2f/mceclip8.png?expires=1786536000&signature=7f26b363a419b08175c9556bfbff6cbb23a96beb372404e02cbf3186a7ed6735&req=dyYuFct7mYRWFb4V1XW4gaqjJOmgopTp99DChqULLKJ36QNdjQJ8BkxWE%2BvG%0AWW5QFW9CQ0dxK4oRoTYf6q319w%3D%3D%0A)

**Adicionar produtos como opcionais** significa dizer ao Ploomes que vários produtos podem estar vinculados, independente de qual grupo pertença.

**Adicionar grupos** **como opcionais** significa, por sua vez, dizer ao Ploomes que apenas os produtos de determinado grupo pode servir como opcional.

Ao inserirmos esse produto em uma proposta, veja o que acontece com o formulário de preenchimento:

![Imagem 2: Ao inserirmos esse produto em uma proposta, veja o que acontece com o formulário de preenchimento:](https://ploomes-52ceb6b026db.intercom-attachments-1.com/i/o/369325465/69bc5a2ec57d8f7678370ae6/mceclip0.png?expires=1786536000&signature=c54aa1b0b7d2518e7e6e8ef98d5ab5b118cd6fb565f09c43df00d47cdf39de55&req=dyYuFct7mYdaFb4V1XW4gTqEi5vveaCeu6yku1m2FN%2FjsU0QetcFnOfbCEiT%0Aw5qXv7qW5liei0Bs%2B5duDZ62gA%3D%3D%0A)

## Importação

Para importar produtos vamos na entidade de Produtos (Menu Esquerdo) > Menu > Importar Produtos pelo Excel:

![Imagem 3: Para importar produtos vamos na entidade de Produtos (Menu Esquerdo) > Menu > Importar Produtos pelo Excel:](https://downloads.intercomcdn.com/i/o/397627204/7dc3696550129adaadf16b7c/image.png?expires=1786536000&signature=f54f6aa6637f2316c8c6e7931eb0de6b392879b9c14f734027083012781bc99d&req=dykgEMt5n4FbFb4V1XW4gWk0JDG%2BGTj64BuvmoLg1LTWUAtR2aaaJbUiKoEJ%0Azs%2Bu8xH26tqb1uhVyOaXSmcbGA%3D%3D%0A)

## Planilha

Para importar produtos é obrigatório no mapeamento ter Nome e Grupo.

Uma importação com produto filho (opcional) é obrigatório (além do Nome) as colunas de:

**Categoria:** representa o nome da aba que irá aparecer no produto pai para exibir os filhos.

**Padrão:** representa se o opcional vem selecionado por padrão ou não.

No **mapeamento** ambos são da entidade de vínculo, para acessar essa entidade na importação de produtos é necessário ativar a chave: Importar Vínculos de Produtos.

![Imagem 4: No mapeamento ambos são da entidade de vínculo, para acessar essa entidade na importação de produtos é necessário…](https://downloads.intercomcdn.com/i/o/397631913/ddd762296385b86ddb8be7b9/image.png?expires=1786536000&signature=91b232282831fc3ccee194fa5424f04f46a0367bf78184241f2b7ea9d4a1b87e&req=dykgEMp%2FlIBcFb4V1XW4gbScaHpJY8%2B6IuWPcE9MIX1qt%2FgZAX5y9te16m2t%0AILLEgpD5VmrtSzKBnMNFpCrbng%3D%3D%0A)

**Exemplo de Mapeamento e Planilha:**

![Imagem 5: Exemplo de Mapeamento e Planilha:](https://downloads.intercomcdn.com/i/o/397631017/636a1f71a40edd433a9f6767/image.png?expires=1786536000&signature=4460967032629f08c0c7f1d8547f0f0b6d736c0ee14cc2a53510ebbcf6e556ed&req=dykgEMp%2FnYBYFb4V1XW4gRPGwuwh3YMDUbtj12kIwnDvxAgVWv%2BVlmIKJXfF%0As1hA%2BH%2BhGsy2DqZ6wp%2F0Fzr0PQ%3D%3D%0A)

Colunas A e B: entidade de Produto Pai

Coluna C: entidade de Grupo do Produto Pai

Colunas D até F: entidade de Produto Filho

Colunas G e H: entidade de Vínculo.

![Imagem 6: Colunas G e H: entidade de Vínculo.](https://downloads.intercomcdn.com/i/o/397633520/6edc5dcc90a709e726d437e2/image.png?expires=1786536000&signature=0bb3da44bc8977c7398ac3d06193a38d99eefc60d199ed1f94e67d6f96eced22&req=dykgEMp9mINfFb4V1XW4gdJuWxRDJmvvYOo1Ze65duXwNDuZE%2B4Tw%2FY7XBWD%0Aig7iS5Zb2OiMR4sywpef%2FQBNcA%3D%3D%0A)

Detectamos por duplicado o Código do Pai e Grupo do Produto Pai > Nome, pois não queremos que criem duplicados, somente criei um produto pai com dois opcionais em um grupo já existente.

Caso não detecte por duplicado, cada linha será criado um produto pai, um grupo e um opcional.

![Imagem 7: Detectamos por duplicado o Código do Pai e Grupo do Produto Pai > Nome, pois não queremos que criem duplicados, somente…](https://downloads.intercomcdn.com/i/o/397634757/64975bd9f28fa51313eb1ffd/image.png?expires=1786536000&signature=48ab68d879c8d3ac787ad330bf5eeb58b1f30556c0d3926ee77367e399945722&req=dykgEMp6moRYFb4V1XW4gWOhiF3gM2wPPXZxtBMsYxm2DB9ecIECeqtgzAzs%0AxGD45aaDhOdSHir3yS6i7TxLRg%3D%3D%0A)

O grupo não é necessário no filho, o mesmo estará ligado ao grupo do pai.

![Imagem 8: O grupo não é necessário no filho, o mesmo estará ligado ao grupo do pai.](https://downloads.intercomcdn.com/i/o/397635586/8a65192694e61bf33021ce24/image.png?expires=1786536000&signature=5b5ad331258d9c9b6783b852f1e70d0503613c6be1627a264a1259c885640331&req=dykgEMp7mIlZFb4V1XW4gX3OV3HCGiXRP9cTrLSuMqPUQG09E1mQzD78VChI%0AziHFLKwVzMZVq%2FyliDyG%2BaWz1Q%3D%3D%0A)

## Demonstração

**Categoria:**

![Imagem 9: Categoria:](https://downloads.intercomcdn.com/i/o/397636663/d1f92b804b79b2b397664b19/image.png?expires=1786536000&signature=a150e6c2bf7676ae968a726dcc8f5c417abcc3978a6f999fce7af7ed3669b792&req=dykgEMp4m4dcFb4V1XW4gcKDmVCAyBXF5yhrQW11voqRYcPHCUiE4BnLzh8f%0A4AwBKNTtcq8wjAOTzPnZYhK%2FdA%3D%3D%0A)

**Proposta:**

![Imagem 10: Proposta:](https://downloads.intercomcdn.com/i/o/397640281/f8b4cc8096290e8f5b9fc5b4/image.png?expires=1786536000&signature=6e7d67d0b0e8a09160a7cfbd80c7536df062aa17a9fedfde959065e92a3563cb&req=dykgEM1%2Bn4leFb4V1XW4gV1XdDg7ctz6tXoFbwJRgmQOTUI8zikDGwT8L5He%0AUWDRjpF8f5WfyzZI9xhpeGRKmQ%3D%3D%0A)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts, casos de uso e webinars.

Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.

[![Imagem 11: Abaixo você confere uma sugestão de conteúdo disponível em nossa plataforma que se relaciona ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048786154/2b2ddf57805322730a9a7edf492e/Teste+01.png?expires=1786536000&signature=a8c57da9583f5830ae722ec8c08483c6b5aed03abe5872098f256b4a830275fe&req=diAjHs52m4BaXfMW3nq%2BgWCYfzas17qfqKHY2bVyOoORXP7wsWdzMFIU6m50%0APEi%2F5VlzCW%2Fj%2BXpTjRD589RIHuc%3D%0A)](https://universidade.ploomes.com/courses/boas-praticas-para-a-importacao-de-dados)
