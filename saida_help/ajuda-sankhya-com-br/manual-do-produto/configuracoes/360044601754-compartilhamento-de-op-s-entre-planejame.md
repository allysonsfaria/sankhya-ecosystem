---
id: "360044601754"
titulo: "Compartilhamento de OP's entre Planejamentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601754-Compartilhamento-de-OP-s-entre-Planejamentos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:51:50Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Compartilhamento de OP's entre Planejamentos manual", "Produção", "Planejamento de Produção", "OP's"]
---

# Compartilhamento de OP's entre Planejamentos

Podem ocorrer casos em que tem-se produtos reunidos em grupos de produção de forma que, sua produção ocorre de maneira simultânea possuindo o mesmo número de lote. Quando isso ocorre, uma das etapas do planejamento onde alguns destes produtos são produzidos, é executada na prática em uma única produção, porém como são produtos diferentes o sistema gera uma OP para cada produto.

As configurações abaixo, visam permitir a geração de maneira automática, uma única OP para a etapa.

Na tela [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034), quando a marcação **"Compartilha Produção"** estiver efetuada, indica-se que a etapa é compartilhada com produtos de um mesmo grupo de produção.

![Imagem 1: Na tela Estrutura de Produção , quando a marcação "Compartilha Produção" estiver efetuada, indica-se que a etapa é…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006172041)

Os produtos pertencentes ao mesmo Grupo de Produção devem compartilhar a mesma estrutura de produção, desta forma, efetue o preenchimento do campo **"Estrutura de Produção"** da tela [Grupo de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611234) de modo a definir a qual Estrutura de Produção o grupo pertence. As estruturas de produção, são cadastradas previamente na tela [Estrutura de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611034).

![Imagem 2: Os produtos pertencentes ao mesmo Grupo de Produção devem compartilhar a mesma estrutura de produção, desta forma,…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006172781)

Quando for realizado um novo planejamento na tela [Planejamento de Produção e Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953), botão [Gerar Planejamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118953-Planejamento-de-Produ%C3%A7%C3%A3o-e-Compra#gerarplanejamento), caso o produto pertença a um Grupo de Produção, a estrutura de produção será obtida do preenchimento previamente efetuado no campo **"Estrutura de Produção"** informado na tela Grupos de Produção.

![Imagem 3: Quando for realizado um novo planejamento na tela Planejamento de Produção e Compra , botão Gerar Planejamento , caso o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006060522)

A tela [Acompanhamento da Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118993) conta com dois campos calculados**"Cobertura Estoque"** e **"Cobertura Estoque Fim"**, que são alimentados com base no estoque atual e a meta do mesmo. Além disso, na grade inferior, pode-se inserir alguma informação relevante para o processo por meio do campo **"Observação"**, onde através de um duplo clique em sua linha, é aberta uma janela para execução de seu preenchimento.

![Imagem 4: A tela Acompanhamento da Produção conta com dois campos calculados "Cobertura Estoque" e "Cobertura Estoque Fim" , que…](https://ajuda.sankhya.com.br/hc/article_attachments/1500006060982)

Quando for realizada a geração das produções, será apresentado na tela um pop-up para que seja informada uma data; este pop-up será exibido preenchido com a data de validade calculada na geração do planejamento; caso seja feita alguma alteração desta data, o valor inserido não poderá ser menor que a data atual. Esta data será salva nos campos **"Data de Faturamento"** e **"Data de Negociação"** do cabeçalho da nota.

Na geração das produções, será realizada uma busca pelo sistema de modo a verificar se existem outros planejamentos para o mesmo "grupo de produção + lote"; caso exista o sistema irá gerar as produções de todos de uma só vez.

Ainda sobre este comportamento, o sistema irá gerar as produções para o planejamento selecionado normalmente; caso ele encontre planejamentos equivalentes para o mesmo "grupo de produção + lote" na etapa em que é gerada a produção, ele verifica a marcação **"Compartilha Produção"**; caso esteja marcado, o sistema irá gerar apenas uma nota, em lote, para todas as MP's e PA's envolvidos em todos os planejamentos encontrados, inclusive o selecionado na tela. Caso o sistema encontre planejamentos equivalentes e a etapa que gera produção não esteja com a opção Compartilha Produção marcada, será gerada uma nota para cada planejamento.

Esta nova rotina, fará com que sejam geradas notas em "bacth" (fornada), gerando uma nota para todos os planejamentos em que o "grupo de produção + lote" sejam iguais e suas etapas que gerem produção, estejam com a opção de Compartilha Produção marcada.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601754-Compartilhamento-de-OP-s-entre-Planejamentos#top)
