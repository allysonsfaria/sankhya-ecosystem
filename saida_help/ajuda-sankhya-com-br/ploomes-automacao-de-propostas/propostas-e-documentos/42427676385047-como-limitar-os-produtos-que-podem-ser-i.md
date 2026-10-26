---
id: "42427676385047"
titulo: "Como limitar os produtos que podem ser inseridos em uma tabela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427676385047-Como-limitar-os-produtos-que-podem-ser-inseridos-em-uma-tabela"
trilha: "PLOOMES: Automação de propostas  > Propostas e documentos"
atualizado_em: "2026-08-11T16:14:03Z"
rotulos: ["sync_hc", "ploomes", "ploomes_6629860", "sync_hash_b84250e81bfa"]
---

# Como limitar os produtos que podem ser inseridos em uma tabela

Ao criarmos diferentes modelos de propostas ou seções de produtos, pode surgir a necessidade de limitar a adição dos produtos em um bloco específico. Na prática, posso ter um bloco apenas para serviços; outro para produtos de vendas recorrentes; outro para equipamentos, e por aí vai.

**Observação:** "Lista de produtos", "Seção", "Bloco" e "Tabela", nesse artigo, referem-se à parte da proposta onde adiciono produtos.

Para fazer essa configuração, acesse o modelo do documento em **Administração - Modelos de documento.**

Clique com o botão direito do mouse sobre a tabela de produtos, e acesse os '**Detalhes da seção'**

![Imagem 1: Clique com o botão direito do mouse sobre a tabela de produtos, e acesse os ' Detalhes da seção'](https://downloads.intercomcdn.com/i/o/595396488/2a985f75c3ced6c0d10f3139/image.png?expires=1786536000&signature=40509c5ee38bb1e1164f4da04d9d013f0c3920c48c3018e074672d8a2fe3230b&req=cSkiFcB4mYlXFb4V1XW4gb2ZTyQmuCRSb0YkDgXLChoOtdhNePh73s9ub25n%0ALP9%2F7T7XsMHdcUEw0IbpnGboYw%3D%3D%0A)

![Imagem 2: Clique com o botão direito do mouse sobre a tabela de produtos, e acesse os ' Detalhes da seção'](https://downloads.intercomcdn.com/i/o/595396795/9c91c69c47367cddb8b9e1ea/image.png?expires=1786536000&signature=226f8b1b4b2460cb7a38b31bc0b6e561d08df927b8c71c1c9c43bdfb7150ffd1&req=cSkiFcB4mohaFb4V1XW4gWGwHfZoQTqt1OMn37IJTvREsqBpklNDek4R5Fos%0AU%2Bo6O0bjjjzPubmGnH6T3LZgRQ%3D%3D%0A)

Os detalhes da seção consistem em 5 configurações:

**Código da lista de produtos**

O código é o que define a seção. Se duas tabelas de produto tiverem o mesmo código, se comportarão como uma única tabela. Na prática, posso criar uma tabela para mostrar apenas os valores dos produtos e outra com informações técnicas.

**Nome da lista de produtos**

Define qual o título exibido no formulário da proposta.

**Exibir seção mesmo sem produtos**

Quando ativo, a seção aparece no documento mesmo se nenhum produto for inserido.

**Exibir seção sempre expandida**

Mostra a seção sempre aberta no formulário

**Editar filtro dessa tabela de produtos**

Essa é a configuração que vai realmente definir quais produtos podem ser inseridos nessa seção.

![Imagem 3: Essa é a configuração que vai realmente definir quais produtos podem ser inseridos nessa seção.](https://downloads.intercomcdn.com/i/o/595401271/3ee73ef9c8285ad60c4af865/image.png?expires=1786536000&signature=622a3038144abc1f389c4eb8faf117f2b45cdfc0e772d2e47dd3f7a97c66cd07&req=cSkiEsl%2Fn4ZeFb4V1XW4gbLvHxEYNlmXkHZ4Fj96HbPKo%2FsARU2njLIwEoST%0Af0wdPlfMsDEnr1XxkNQ7p0pYUw%3D%3D%0A)

Posso filtrar por grupos, famílias ou marcadores.

Também posso limitar a seção a aceitar apenas produtos de cliente.

**Configuração de filtros**

Com a configuração abaixo, é necessário que meu produto faça parte de um dos dois grupos selecionados.

![Imagem 4: Com a configuração abaixo, é necessário que meu produto faça parte de um dos dois grupos selecionados.](https://downloads.intercomcdn.com/i/o/595403143/e4741e343dc45546fde71f72/image.png?expires=1786536000&signature=fab97229aa13771afebea888c180a100006e2751610020a8e614c5a3a7da274b&req=cSkiEsl9nIVcFb4V1XW4gZYBPrmZdaGVl1bk0mfNFfR6eEFPNruVrIweDrTe%0AOPBybGj24tbKrEZ%2BORkhQkT%2BsQ%3D%3D%0A)

A próxima configuração requer que o produto faça parte de um dos grupos **e** de uma das famílias **e** tenha o marcador preenchido como "Ativo".

![Imagem 5: A próxima configuração requer que o produto faça parte de um dos grupos e de uma das famílias e tenha o marcador…](https://downloads.intercomcdn.com/i/o/595405124/058cd90d0a95b9ac52535f2b/image.png?expires=1786536000&signature=7b1132771bdbd56874b4bb034134ce7aa5f43c0089df09ddbb005bdf9f2262b1&req=cSkiEsl7nINbFb4V1XW4gdmQVEMu%2FkWSyv9xUt3i47Dxw7YDI3UClVG2hgOr%0AeRU0t%2BnowL%2Ble6BehXWfm0RsQQ%3D%3D%0A)
