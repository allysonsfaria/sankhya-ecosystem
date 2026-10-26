---
id: "360044603874"
titulo: "Suporte MPs Alternativas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603874-Suporte-MPs-Alternativas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:36Z"
rotulos: ["Produtos", "Configuração", "Impressão", "Estoque", "Produção", "Suporte MPs Alternativas manual", "Implementação e Uso de Matérias-Primas Alternativas"]
---

# Suporte MPs Alternativas

O Material Alternativo permite que seja produzido um determinado Produto Acabado (PA) a partir de uma ou mais matérias-primas alternativas, ou seja, a matéria-prima principal (aquela usada como matéria-prima primária). Essa substituição pode ser feita devido a uma falta de estoque, por exemplo.

Utilizaremos nessa documentação, o Produto Acabado Embalagem Plástica que é comercializado pela indústria "X". A imagem abaixo retrata como se dá o processo produtivo desse PA:

![Imagem 1: Utilizaremos nessa documentação, o Produto Acabado Embalagem Plástica que é comercializado pela indústria "X". A imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/4409610600599)

Vamos tratar no exemplo a seguir, os detalhes da atividade de Impressão:

![Imagem 2: Vamos tratar no exemplo a seguir, os detalhes da atividade de Impressão:](https://ajuda.sankhya.com.br/hc/article_attachments/4409633835543)

Existem duas matérias-primas (MPs) necessárias para que a atividade de Impressão aconteça, sendo elas o Molde de Impressão e a Tinta Laranja. Para a MP Tinta Laranja, existe a possibilidade se utilizar uma mistura de tinta vermelha + tinta amarela como matérias-primas alternativas. Essas MPs em conjunto podem substituir a MP principal.

#### Configurações

Após a definição da MP principal, você pode adicionar a matéria-prima alternativa para a mesma da seguinte forma:

Na [Configuração da Atividade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades) realizada na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314), aba [Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa), selecione o PA que será incluída a matéria-prima alternativa.

Em seguida, na sub-aba [Lista de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistademps), aponte a matéria-prima principal a ser inserida na matéria-prima alternativa. Na sub-aba **"Materiais Alternativos"**, serão cadastradas as MP's alternativas referentes a MP principal selecionada no passo anterior.

![Imagem 3: Em seguida, na sub-aba Lista de MPs , aponte a matéria-prima principal a ser inserida na matéria-prima alternativa. Na…](https://ajuda.sankhya.com.br/hc/article_attachments/4409624765719)

Defina no campo **"Material Alternativo"**, o material que será adicionado na lista de materiais alternativos da matéria-prima.

O campo **"Referência do Produto (Alternativo)"** apresenta o conteúdo do campo **"Referência"** presente na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral) do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113); neste caso, referente ao produto alternativo.

Indique a **"Quantidade"** do material alternativo ligado a uma unidade do material principal. No nosso exemplo, foi informado nesse campo 0.5 LT para as duas MPs alternativas, ou seja, para cada unidade do material principal se faz necessário 0.5 LT de cada matéria alternativa.

Informe a **"Unidade"** de medida a ser utilizada quando for considerado o material alternativo.

O **"Conjunto"** deve ser utilizado nos casos em que a matéria-prima é substituída por vários materiais alternativos simultaneamente. Com isso, estes materiais alternativos devem fazer parte do mesmo conjunto. Informe aqui apenas números.

No nosso exemplo foi informado no campo acima, 1 para ambas, pois a matéria-prima em questão (tinta laranja) é substituída por duas matérias alternativas ao mesmo tempo (tinta vermelha e tinta amarela). Logo, devem fazer parte do mesmo conjunto.

---

#### Utilizando MPs Alternativas

A definição de que uma determinada Ordem de Produção irá utilizar suas MPs principais e/ou alternativas acontece no lançamento da ordem, na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313) ao acionar o botão **"Extrato MPs"**, onde você será direcionado para a tela **"Extrato de Materiais"**.

![Imagem 4: A definição de que uma determinada Ordem de Produção irá utilizar suas MPs principais e/ou alternativas acontece no…](https://ajuda.sankhya.com.br/hc/article_attachments/4409624956823)

No contexto do exemplo que está sendo utilizado, se a Indústria **"X"** ao lançar uma ordem de produção do **"Processo Produtivo Embalagem Plástica"** observou no Extrato de Materiais que não existe estoque suficiente da MP Tinta Laranja. Este fato é possível de visualizar, pois a linha da referida MP será destacada na coloração **vermelha**, indicando que não há estoque suficiente da mesma (saldo negativo).

Além disso, você pode verificar na grade **"Matérias Primas"** as informações referentes às MPs principais necessárias para produção do PA Plástico Embalagem, considerando o tamanho do lote em questão. Para a MP Tinta Laranja a quantidade necessária para esta  produção é de 10 LT, conforme apresentado no campo **"Necessidade"**, porém, no campo **"Estoque"** mostra que existem apenas 5 LT, ou seja, a quantidade insuficiente para que toda produção aconteça.

![Imagem 5: Além disso, você pode verificar na grade " Matérias Primas" as informações referentes às MPs principais necessárias…](https://ajuda.sankhya.com.br/hc/article_attachments/4409634918551)

Ao selecionar a MP Tinta Laranja na grade Matérias Primas, é possível perceber que na grade **"Materiais Alternativos"** existem MPs alternativas (tinta amarela e tinta vermelha) capazes de substituí-la.

Deste modo, para substituir a referida MP por suas MPs alternativas, selecione uma MP alternativa na grade Materiais Alternativos. Nesse caso, conforme configurado anteriormente no cadastro das MPs alternativas, estas devem ser empregadas em conjunto para substituição da MP principal. Logo, quando selecionada uma MP alternativa nessa grade o sistema irá associar automaticamente os registros das outras MPs alternativas participantes do mesmo conjunto.

![Imagem 6: Deste modo, para substituir a referida MP por suas MPs alternativas, selecione uma MP alternativa na grade Materiais…](https://ajuda.sankhya.com.br/hc/article_attachments/4409635034647)

Note que, o salvar o registro, o campo **"Qtd. Usar"** da grade Materiais Alternativos, será preenchido automaticamente pelo sistema de forma que o valor atribuído a ele é igual ao valor do campo **"Necessidade"** presente na grade Matérias Primas, ou seja, o sistema entenderá que a substituição da MP principal total.

É possível observar ainda, que o campo **"Qtd. Substituída"** mostra o quanto da MP em questão está sendo substituída. Na imagem anterior, esse campo se encontra com o valor zerado, pois nenhuma substituição da MP principal foi realizada. Ao selecionar as MPs alternativas e salvar a alteração, o sistema entende a substituição e o valor do campo Qtd. Substituída é alterado.

No caso da imagem acima onde a substituição da MP está sendo feita por completo, o campo Qtd. Substituída é igual ao valor do campo Necessidade (grade Matérias Primas). Dessa forma, é possível observar que a substituição das MPs alternativas pela MP principal aconteceu e agora a linha da MP Tinta laranja não se encontra mais destacada em **vermelho**, indicando que já é possível a produção acontecer (saldo positivo). Já as linhas das MPs alternativas são destacadas em **azul**, o que indica a normalidade da substituição (saldo positivo).

Se as MPs alternativas fossem destacadas em **vermelho**, determinará que a substituição não pode acontecer (saldo negativo), visto que não existe estoque suficiente do material.

Caso não queira que a substituição da MP aconteça por completo devido à existência de parte da MP principal em estoque, o campo Qtd. Usar deve ser alterado conforme a necessidade.

Esse cenário pode ser observado na imagem abaixo, como existe parte da MP principal em estoque (5 LT). Então, opta-se por utilizar esse estoque já existente e apenas usar as MPs alternativas para completar a necessidade de 10 LT. Sendo assim, é alterada a quantidade a ser usada de MP alternativa no campo Qtd. Usar de 5 para 2,5.

![Imagem 7: Esse cenário pode ser observado na imagem abaixo, como existe parte da MP principal em estoque (5 LT). Então, opta-se…](https://ajuda.sankhya.com.br/hc/article_attachments/4409635238423)

Visto que, foi lançada uma Ordem de Produção utilizando materiais alternativos, é possível visualizar o uso deste por meio da execução dessa OP.

Na atividade de **"Impressão"**, uma Operação de Estoque foi configurada para que ao iniciar a atividade fosse realizado uma transferência das MPs necessárias que serão consumidas pela atividade. A transferência se dá do local Almoxarifado para o local Produção.

Após dar início a atividade de Impressão, é possível visualizar as movimentações que ocorreram das MPs entre locais da seguinte forma:

![Imagem 8: Após dar início a atividade de Impressão , é possível visualizar as movimentações que ocorreram das MPs entre locais da…](https://ajuda.sankhya.com.br/hc/article_attachments/4409639641751)

Ao selecionar a nota de transferência na grade superior **"Notas"**, você pode visualizar as MPs consumidas pela atividade na grade inferior **"Itens"** e as suas respectivas movimentações de estoque (local origem e local destino). Assim como, a quantidade utilizada.

**Nota:** a aba [Mov. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o#abamov.acessrias) estará visível também na tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313).

Como foi configurado no [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314) da atividade de Impressão, aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314#abaapontamento), o campo **"Tipo de apontamento"** como **"Apontamento de PA/MP"**, a tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274), na aba [Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274#abaapontamentos) irá receber os apontamentos do PA produzido:

![Imagem 9: Como foi configurado no Processo Produtivo da atividade de Impressão , aba Apontamento , o campo "Tipo de apontamento"…](https://ajuda.sankhya.com.br/hc/article_attachments/4409625630999)

Na inserção de um novo apontamento, esses produtos são carregados automaticamente pelo sistema, conforme a configuração de Apontamento da atividade no Processo Produtivo.

Também é apresentada de forma automática, a sugestão das informações necessárias para o apontamento desses produtos, como a quantidade de PA e MP gasta para a produção. Essas informações são baseadas nas configurações feitas no lançamento da OP, em Extrato de Materiais.

Além disso, o sistema ajusta o lote (controle) conforme a disponibilidade do mesmo conforme campo **"Lote"** da sub-aba Materiais. Nesse caso, a tinta amarela foi consumida de 2 lotes diferentes (1 e 2), pois a quantidade necessária da mesma não foi suprida utilizando apenas um lote.

Existe ainda a possibilidade de que as quantidades sugeridas no apontamento referentes aos produtos (PAs e MPs) sejam ajustadas, se necessário. Esse ajuste é feito na própria grade dos respectivos produtos nos seus respectivos campos (Qtd. apontada).

Caso a quantidade do Produto Acabado sofra modificações, assim, os registros das MPs na sub-aba Materiais serão ajustados proporcionalmente pelo sistema (desde que o material não esteja configurado para fixar quantidade **"Fixar qtd. apontada da MP ao editar qtd. apontada do PA"**).

Dessa forma, imaginemos, por exemplo, que na atividade de Impressão seja necessário executar um apontamento parcial, assim alterando a quantidade apontada do produto acabado de 200 para 100. Após salvar a alteração, o sistema realiza o ajuste das MPs de forma proporcional, sendo desnecessária a utilização das MPs alternativas (tinta amarela e tinta vermelha), ou seja, com a diminuição de PA produzido, a quantidade de MP principal (tinta laranja) foi suficiente para suprir a necessidade.

![Imagem 10: Dessa forma, imaginemos, por exemplo, que na atividade de Impressão seja necessário executar um apontamento parcial,…](https://ajuda.sankhya.com.br/hc/article_attachments/4409639938455)

**Observação:** caso a Qtd. apontada para o PA seja maior do que o Tamanho do Lote do PA na OP, deve-se informar manualmente a MP que será consumida para a quantidade que ultrapassa o tamanho do lote, pois, ao substituir uma MP principal por uma MP alternativa no lançamento de uma Ordem de Produção, após consumir a quantidade definida para cada MP, não é possível identificar se a quantidade a mais da MP que será consumida se trata da MP principal ou da MP alternativa. Dessa forma se for realizada substituição de MP principal por alternativa, e houver desvio de produção de PA para maior, caso a quantidade de MP consumida seja diferente da quantidade pré definida no lançamento da OP, deve-se informar qual a MP e a quantidade que deverá ser consumida ao realizar o apontamento de produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603874-Suporte-MPs-Alternativas#top)
