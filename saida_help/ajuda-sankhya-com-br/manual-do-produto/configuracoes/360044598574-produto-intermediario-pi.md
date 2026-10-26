---
id: "360044598574"
titulo: "Produto Intermediário (PI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598574-Produto-Intermedi%C3%A1rio-PI"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:47:45Z"
rotulos: ["Produtos", "Configuração", "Evento", "Dependências", "Sub-Ordem", "Ordem de Produção", "Aguardar PI", "Produto Intermediário (PI)", "Produto Intermediário (PI) manual", "Estoque", "Produção"]
---

# Produto Intermediário (PI)

O Produto Intermediário também chamado de PI, consiste em um produto já acabado proveniente de outra produção e que é empregado como matéria-prima de um ou vários novos Produtos Acabados (PA). Logo, é necessário que exista esse produto momentos antes de consumi-lo na produção do PA.

Um PI pode ou não ser um produto de venda. Existirá estoque do PI, mesmo que ele tenha sido gerado para consumo de uma Ordem de Produção de Produto Acabado.

A geração de um PI pode ser consequência das seguintes situações:

- **Uma Ordem de Produção independente:** Gerada a partir da demanda direta do produto, por exemplo, para atender a uma venda ou simplesmente estoque do produto.
- **Uma OP dependente de outra OP de PA:** Gerada a partir da demanda indireta do produto, por exemplo, para produção de shampoos (PA) é necessário que antes a mistura do produto (PI) esteja pronta.

Considere os seguintes exemplos:

1. O produto acabado comercializado pela Indústria "X" é embalagem plástica de polietileno. É necessário produzir um PI que componha essa embalagem plástica que é a tinta (tinta vermelha, tinta amarela, entre outras) aplicada sobre o PA.
   Os PA's embalagem (plástico filme que envolve o produto) **"Embalagem 1"** e **"Embalagem 2"** compartilham o mesmo PI Tinta Vermelha.
   É possível executar a fabricação da tinta e começar a extrusão da embalagem. Já a impressão de fato, deve acontecer apenas quando a tinta estiver pronta.
   ![Imagem 1: O produto acabado comercializado pela Indústria "X" é embalagem plástica de polietileno. É necessário produzir um PI…](https://ajuda.sankhya.com.br/hc/article_attachments/9397171035415)
   ![Imagem 2: O produto acabado comercializado pela Indústria "X" é embalagem plástica de polietileno. É necessário produzir um PI…](https://ajuda.sankhya.com.br/hc/article_attachments/9397171722007)
   ![Imagem 3: O produto acabado comercializado pela Indústria "X" é embalagem plástica de polietileno. É necessário produzir um PI…](https://ajuda.sankhya.com.br/hc/article_attachments/9397172503959)
2. Suponhamos que uma indústria produza PA's que compartilham o mesmo PI, **"Shampoo Ben 10"** e **"Shampoo Turma da Mônica"**. Ambos utilizam a mesma mistura base de shampoo, porém são embalados em dois frascos distintos e são de fato produtos distintos. É impossível caminhar com o processo (envase do shampoo) sem a mistura estar pronta.

![Imagem 4: Suponhamos que uma indústria produza PA's que compartilham o mesmo PI, "Shampoo Ben 10" e "Shampoo Turma da Mônica" .…](https://ajuda.sankhya.com.br/hc/article_attachments/9396654474903)

![Imagem 5: Suponhamos que uma indústria produza PA's que compartilham o mesmo PI, "Shampoo Ben 10" e "Shampoo Turma da Mônica" .…](https://ajuda.sankhya.com.br/hc/article_attachments/9396638813719)

![Imagem 6: Suponhamos que uma indústria produza PA's que compartilham o mesmo PI, "Shampoo Ben 10" e "Shampoo Turma da Mônica" .…](https://ajuda.sankhya.com.br/hc/article_attachments/9396638402199)

---

#### Configurações

![Imagem 7: Deve-se sempre configurar o PI em algum Processo Produtivo antes de vinculá-lo como Matéria-Prima de algum PA.](https://ajuda.sankhya.com.br/hc/article_attachments/16702462863255) Deve-se sempre configurar o PI em algum Processo Produtivo antes de vinculá-lo como Matéria-Prima de algum PA.

Com o PI definido, basta adicioná-lo à **"Lista de MP's"** de seu PA. Essa definição irá gerar uma configuração de PI na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), aba [Produtos(PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaprodutospa). Sempre retorne à esta aba e realize as devidas configurações.

![Imagem 8: Com o PI definido, basta adicioná-lo à "Lista de MP's" de seu PA. Essa definição irá gerar uma configuração de PI na…](https://ajuda.sankhya.com.br/hc/article_attachments/9396637744151)

No campo **"Tipo do PI"** defina qual a relação entre o produto PI e o produto PA, ou seja, para fabricar o Produto Acabado, deve-se utilizar o PI buscando do **"Estoque"** ou lançando **"Sub-ordem"** de produção para ele. 

O campo **"Tipo de sub-ordem"** define o comportamento do sistema na geração/utilização de Ordens de Produção do PI. A utilização deste campo é significativa quando o campo Tipo do PI for definido como Sub-Ordem. Temos as seguintes opções:

- **Sempre iniciar uma nova:** Sempre que o sistema iniciar uma Ordem Principal, será iniciada uma sub-ordem para os PI's. No Lançamento de Ordens de Produção sempre será gerada uma nova OP para o PI. Ao efetuar o lançamento essa Ordem será aberta.
- **Iniciar quando não existir em aberto:** Antes de iniciar a sub-ordem, o sistema verifica se existe uma Ordem Principal em aberto para aquele PI. Caso não exista, será inicializada uma nova. No Lançamento de Ordens de Produção será utilizada uma OP do PI já existente acrescentando a quantidade; caso não exista, será criada uma nova OP. Ao efetuar o lançamento, o sistema irá buscar por uma OP já aberta do PI com saldo disponível e empregando-a. Não existindo OP uma nova Ordem será gerada.
- **Sempre usar uma em aberto:** Ao iniciar uma Ordem Principal, será gerada uma dependência entre esta e uma ordem já aberta do PI, com a quantidade suficiente para a composição dos PA's a serem produzidos na Ordem Principal. No Lançamento de Ordens de Produção será utilizada uma OP do PI já existente acrescentando a quantidade, não existindo será criada uma nova OP para o PI. Ao efetuar o lançamento, o sistema irá buscar por uma OP já aberta do PI com saldo disponível e utilizará a mesma. Caso não exista OP, uma mensagem de erro será apresentada.

Quando se realiza a produção de um produto intermediário e este serve de "ponto de partida" para a produção de um PA, a marcação **"Aguardar a sub-ordem"** fará com que a produção do PA, só tenha início após a finalização da produção deste PI. A Ordem de Produção do PA existirá, porém será inicializada de forma automática apenas quando a OP do PI for finalizada.

Caso esse momento de espera seja apenas após um determinado ponto do processo produtivo, a alternativa é utilizar o evento **"Aguardar PI"**.

Defina no campo **"Tipo de número de lote"** o critério de numeração dos lotes dos PI's e PA's dentre as opções abaixo:

- **PA usa o mesmo lote do PI:** No lançamento de um PI, a numeração do lote do PA que virá em seguida seguirá a numeração do PI.
- **PI usa o mesmo lote do PA:** Seguindo o mesmo critério da opção anterior, esta marcação irá realizar o processo inverso, ou seja, o PI lançado irá receber a mesma numeração de lote do PA.
- **Nro. de lote independente:** Através dessa marcação, temos a possibilidade de informar as numerações de PIs e PAs de forma independente.

O evento **"Aguardar PI"** do tipo intermediário, interrompe a execução do Processo Produtivo até que a Ordem de Produção de PI ao qual o PA depende esteja finalizada. Para isso, é preciso configurar quais são os PI's para o PA em questão, que devem ser aguardados.

Para isso, basta editar o evento selecionando a opção **"Editar"** ou através de um duplo clique sobre o elemento, para que o pop-up **"Configuração de Evento"** seja aberto. Deste modo, defina o PA e insira os PI's que deseja aguardar:

![Imagem 9: Para isso, basta editar o evento selecionando a opção "Editar" ou através de um duplo clique sobre o elemento, para que…](https://ajuda.sankhya.com.br/hc/article_attachments/9396651718039)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598574-Produto-Intermedi%C3%A1rio-PI#top)

---

#### Lançamento

O lançamento de Ordens de Produção compostas por PI's é facilmente compreendido. De acordo com o **"Tipo de PI"**, ao lançar uma Ordem de Produção do PA, o sistema lança de forma automática a OP do PI conforme configuração (apenas quando o Tipo de PI for Sub-Ordem):

![Imagem 10: O lançamento de Ordens de Produção compostas por PI's é facilmente compreendido. De acordo com o "Tipo de PI" , ao…](https://ajuda.sankhya.com.br/hc/article_attachments/9396636302103)

De acordo com o **"Tipo de Ordem"** definido para o PI em questão, são definidas as dependências dos PI's x PA; sendo apresentadas na aba **"Dependências"**, as OP's, os produtos, as quantidades e o Tipo de Sub OP dos Produtos Intermediários que o PA selecionado necessita.

É importante observar que no lançamento de OP sempre é carregado o Tipo da Sub OP; deste modo, os critérios para lançamento de OP são executados novamente na geração da Ordem de Produção.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598574-Produto-Intermedi%C3%A1rio-PI#top)

---

#### Ordens de Produção

A execução de uma Ordem de Produção que depende de PI ou de uma OP de PI, não possui nenhuma diferença para Ordens de Produção comuns.

É válido observar o **"Status"** das Ordens de Produção que são geradas após efetivar seu lançamento, pois anteriormente foi definida uma regra de espera entre as OP's (aguardar a Sub-Ordem):

![Imagem 11: É válido observar o "Status" das Ordens de Produção que são geradas após efetivar seu lançamento, pois anteriormente…](https://ajuda.sankhya.com.br/hc/article_attachments/9396616405655)

Vale salientar que a inicialização de forma manual por parte do usuário de uma Ordem de Produção de PA que aguarda PI, não é bloqueada pelo sistema.

Outra informação interessante de ser observada após o lançamento das Ordens de Produção, são os vínculos criados entre as ordens. Essas informações são visualizadas através da aba **"Dependência"** da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o).

![Imagem 12: Outra informação interessante de ser observada após o lançamento das Ordens de Produção, são os vínculos criados entre…](https://ajuda.sankhya.com.br/hc/article_attachments/9396634981399)

![Imagem 13: Outra informação interessante de ser observada após o lançamento das Ordens de Produção, são os vínculos criados entre…](https://ajuda.sankhya.com.br/hc/article_attachments/9396615081495)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598574-Produto-Intermedi%C3%A1rio-PI#top)
